# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.checks import AgentCheck

from six import iteritems
from ast import literal_eval

try:
    import pymqi
except ImportError:
    pymqi = None

from . import errors, metrics


class IbmMqCheck(AgentCheck):

    METRIC_PREFIX = 'ibm_mq'

    def check(self, instance):
        if not pymqi:
            self.log.error("You need to install pymqi")
            raise errors.PymqiException("You need to install pymqi")

        channel = instance.get('channel')
        queue_manager_name = instance.get('queue_manager', 'default')

        host = instance.get('host')
        port = instance.get('port')

        host_and_port = "{}({})".format(host, port)

        username = instance.get('username')
        password = instance.get('password')

        custom_tags = instance.get('tags', [])

        tags = [
            "queue_manager:{}".format(queue_manager_name),
            "host:{}".format(host),
            "port:{}".format(port)
        ]

        tags += custom_tags

        if username and password:
            queue_manager = pymqi.connect(queue_manager_name, channel, host_and_port, username, password)
        else:
            queue_manager = pymqi.connect(queue_manager_name, channel, host_and_port)

        self.queue_manager_stats(queue_manager, tags)

        queues = instance.get('queues', [])

        for queue_name in queues:
            queue_tags = tags + ["queue:{}".format(queue_name)]
            try:
                queue = pymqi.Queue(queue_manager, queue_name)
                self.queue_stats(queue, queue_tags)
            except Exception as e:
                self.log.warning('Cannot connect to queue {}: {}'.format(queue_name, e))

    def queue_manager_stats(self, queue_manager, tags):
        for mname, value in iteritems(metrics.QUEUE_MANAGER_METRICS):
            try:
                arg = 'queue_manager.inquire(pymqi.CMQC.{})'.format(value)
                m = eval(arg)

                mname = '{}.queue_manager.{}'.format(self.METRIC_PREFIX, mname)
                self.gauge(mname, m, tags=tags)
                self.log.info("{} {} tags={}".format(mname, m, tags))
            except pymqi.Error as e:
                self.log.info("Error getting queue manager stats: {}".format(e))

    def queue_stats(self, queue, tags):
        for mname, value in iteritems(metrics.QUEUE_METRICS):
            try:
                arg = 'queue.inquire(pymqi.CMQC.{})'.format(value)
                m = eval(arg)
                mname = '{}.queue.{}'.format(self.METRIC_PREFIX, mname)
                self.gauge(mname, m, tags=tags)
                self.log.info("{} {} tags={}".format(mname, m, tags))
            except pymqi.Error as e:
                self.log.info("Error getting queue stats: {}".format(e))
            except Exception as e:
                self.log.info("Error! {} {} {}".format(mname, value, e))
