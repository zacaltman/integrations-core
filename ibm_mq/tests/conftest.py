# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.ibm_mq import IbmMqCheck


@pytest.fixture
def check():
    return IbmMqCheck('ibm_mq', {}, {})


@pytest.fixture
def instance():
    return {
        'channel': 'DEV.ADMIN.SVRCONN',
        'queue_manager': 'datadog',
        'host': 'localhost',
        'port': '1414',
        'username': 'admin',
        'password': 'passw0rd',
    }
