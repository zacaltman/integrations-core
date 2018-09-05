# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

QUEUE_METRICS = {
    'QServiceInterval': 'MQIA_Q_SERVICE_INTERVAL',
    'Shareability': 'MQIA_SHAREABILITY',
    'InhibitPut': 'MQIA_INHIBIT_PUT',
    'QDepthLowLimit': 'MQIA_Q_DEPTH_LOW_LIMIT',
    'InhibitGet': 'MQIA_INHIBIT_GET',
    'HardenGetBackout': 'MQIA_HARDEN_GET_BACKOUT',
    'QServiceIntervalEvent': 'MQIA_Q_SERVICE_INTERVAL_EVENT',
    'InitiationQName': 'MQCA_INITIATION_Q_NAME',
    'TriggerControl': 'MQIA_TRIGGER_CONTROL',
    'Usage': 'MQIA_USAGE',
    'Scope': 'MQIA_SCOPE',
    'QType': 'MQIA_Q_TYPE',
    'MaxQDepth': 'MQIA_MAX_Q_DEPTH',
    'BackoutThreshold': 'MQIA_BACKOUT_THRESHOLD',
	'TriggerData': 'MQCA_TRIGGER_DATA',
	'QDepthHighEvent': 'MQIA_Q_DEPTH_HIGH_EVENT',
	'DefinitionType': 'MQIA_DEFINITION_TYPE',
	'QDepthLowEvent': 'MQIA_Q_DEPTH_LOW_EVENT',
	'TriggerMsgPriority': 'MQIA_TRIGGER_MSG_PRIORITY',
	'CurrentQDepth': 'MQIA_CURRENT_Q_DEPTH',
	'QDepthMaxEvent': 'MQIA_Q_DEPTH_MAX_EVENT',
	'OpenInputCount': 'MQIA_OPEN_INPUT_COUNT',
	'DefPersistence': 'MQIA_DEF_PERSISTENCE',
	'TriggerDepth': 'MQIA_TRIGGER_DEPTH',
	'MaxMsgLength': 'MQIA_MAX_MSG_LENGTH',
	'QDepthHighLimit': 'MQIA_Q_DEPTH_HIGH_LIMIT',
	'DefPriority': 'MQIA_DEF_PRIORITY',
	'DefInputOpenOption': 'MQIA_DEF_INPUT_OPEN_OPTION',
	'MsgDeliverySequence': 'MQIA_MSG_DELIVERY_SEQUENCE',
	'DefBind': 'MQIA_DEF_BIND',
	'ClusterName': 'MQCA_CLUSTER_NAME',
	'RetentionInterval': 'MQIA_RETENTION_INTERVAL',
	'OpenOutputCount': 'MQIA_OPEN_OUTPUT_COUNT',
	'TriggerType': 'MQIA_TRIGGER_TYPE',
	'QDesc': 'MQCA_Q_DESC'
}

QUEUE_TAGS = {

}

QUEUE_MANAGER_METRICS = {
    'DistLists': 'MQIA_DIST_LISTS',
	'MaxMsgLength': 'MQIA_MAX_MSG_LENGTH',
}

QUEUE_MANAGER_TAGS = {
	'QMgrIdentifier': 'MQCA_Q_MGR_IDENTIFIER',
	'ProcessName': 'MQCA_PROCESS_NAME',
}

CREATION = {
    'CreationTime': 'MQCA_CREATION_TIME',
	'CreationDate': 'MQCA_CREATION_DATE',
}
