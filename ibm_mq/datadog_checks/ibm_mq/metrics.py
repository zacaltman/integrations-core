# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

QUEUE_METRICS = {
    'service_interval': 'MQIA_Q_SERVICE_INTERVAL',
    'inhibit_put': 'MQIA_INHIBIT_PUT',
    'depth_low_limit': 'MQIA_Q_DEPTH_LOW_LIMIT',
    'inhibit_get': 'MQIA_INHIBIT_GET',
    'harden_get_backout': 'MQIA_HARDEN_GET_BACKOUT',
    'service_interval_event': 'MQIA_Q_SERVICE_INTERVAL_EVENT',
    'trigger_control': 'MQIA_TRIGGER_CONTROL',
    'usage': 'MQIA_USAGE',
    'scope': 'MQIA_SCOPE',
    'type': 'MQIA_Q_TYPE',
    'depth_max': 'MQIA_MAX_Q_DEPTH',
    'backout_threshold': 'MQIA_BACKOUT_THRESHOLD',
    'depth_high_event': 'MQIA_Q_DEPTH_HIGH_EVENT',
    'depth_low_event': 'MQIA_Q_DEPTH_LOW_EVENT',
    'trigger_message_priority': 'MQIA_TRIGGER_MSG_PRIORITY',
    'depth_current': 'MQIA_CURRENT_Q_DEPTH',
    'depth_max_event': 'MQIA_Q_DEPTH_MAX_EVENT',
    'open_input_count': 'MQIA_OPEN_INPUT_COUNT',
    'persistence': 'MQIA_DEF_PERSISTENCE',
    'trigger_depth': 'MQIA_TRIGGER_DEPTH',
    'max_message_length': 'MQIA_MAX_MSG_LENGTH',
    'depth_high_limit': 'MQIA_Q_DEPTH_HIGH_LIMIT',
    'priority': 'MQIA_DEF_PRIORITY',
    'input_open_option': 'MQIA_DEF_INPUT_OPEN_OPTION',
    'message_delivery_sequence': 'MQIA_MSG_DELIVERY_SEQUENCE',
    'retention_interval': 'MQIA_RETENTION_INTERVAL',
    'open_output_count': 'MQIA_OPEN_OUTPUT_COUNT',
    'trigger_type': 'MQIA_TRIGGER_TYPE',
}

QUEUE_TAGS = {

}

QUEUE_MANAGER_METRICS = {
    'dist_lists': 'MQIA_DIST_LISTS',
    'max_msg_list': 'MQIA_MAX_MSG_LENGTH',
}

QUEUE_MANAGER_TAGS = {
    'QMgrIdentifier': 'MQCA_Q_MGR_IDENTIFIER',
    'ProcessName': 'MQCA_PROCESS_NAME',
}

CREATION = {
    'CreationTime': 'MQCA_CREATION_TIME',
    'CreationDate': 'MQCA_CREATION_DATE',
}
