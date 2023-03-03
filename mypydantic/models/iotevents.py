# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcknowledgeFlowModel(BaseModel):
    enabled: bool = Field(alias="enabled")


class ClearTimerActionModel(BaseModel):
    timer_name: str = Field(alias="timerName")


class ResetTimerActionModel(BaseModel):
    timer_name: str = Field(alias="timerName")


class SetTimerActionModel(BaseModel):
    timer_name: str = Field(alias="timerName")
    seconds: Optional[int] = Field(default=None, alias="seconds")
    duration_expression: Optional[str] = Field(default=None, alias="durationExpression")


class SetVariableActionModel(BaseModel):
    variable_name: str = Field(alias="variableName")
    value: str = Field(alias="value")


class InitializationConfigurationModel(BaseModel):
    disabled_on_initialization: bool = Field(alias="disabledOnInitialization")


class AlarmModelSummaryModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    alarm_model_description: Optional[str] = Field(
        default=None, alias="alarmModelDescription"
    )
    alarm_model_name: Optional[str] = Field(default=None, alias="alarmModelName")


class AlarmModelVersionSummaryModel(BaseModel):
    alarm_model_name: Optional[str] = Field(default=None, alias="alarmModelName")
    alarm_model_arn: Optional[str] = Field(default=None, alias="alarmModelArn")
    alarm_model_version: Optional[str] = Field(default=None, alias="alarmModelVersion")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    status: Optional[Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class SimpleRuleModel(BaseModel):
    input_property: str = Field(alias="inputProperty")
    comparison_operator: Literal[
        "EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "NOT_EQUAL"
    ] = Field(alias="comparisonOperator")
    threshold: str = Field(alias="threshold")


class AnalysisResultLocationModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")


class AssetPropertyTimestampModel(BaseModel):
    time_in_seconds: str = Field(alias="timeInSeconds")
    offset_in_nanos: Optional[str] = Field(default=None, alias="offsetInNanos")


class AssetPropertyVariantModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    integer_value: Optional[str] = Field(default=None, alias="integerValue")
    double_value: Optional[str] = Field(default=None, alias="doubleValue")
    boolean_value: Optional[str] = Field(default=None, alias="booleanValue")


class AttributeModel(BaseModel):
    json_path: str = Field(alias="jsonPath")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DetectorModelConfigurationModel(BaseModel):
    detector_model_name: Optional[str] = Field(default=None, alias="detectorModelName")
    detector_model_version: Optional[str] = Field(
        default=None, alias="detectorModelVersion"
    )
    detector_model_description: Optional[str] = Field(
        default=None, alias="detectorModelDescription"
    )
    detector_model_arn: Optional[str] = Field(default=None, alias="detectorModelArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "DEPRECATED",
            "DRAFT",
            "FAILED",
            "INACTIVE",
            "PAUSED",
        ]
    ] = Field(default=None, alias="status")
    key: Optional[str] = Field(default=None, alias="key")
    evaluation_method: Optional[Literal["BATCH", "SERIAL"]] = Field(
        default=None, alias="evaluationMethod"
    )


class InputConfigurationModel(BaseModel):
    input_name: str = Field(alias="inputName")
    input_arn: str = Field(alias="inputArn")
    creation_time: datetime = Field(alias="creationTime")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    status: Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"] = Field(
        alias="status"
    )
    input_description: Optional[str] = Field(default=None, alias="inputDescription")


class DeleteAlarmModelRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")


class DeleteDetectorModelRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")


class DeleteInputRequestModel(BaseModel):
    input_name: str = Field(alias="inputName")


class DescribeAlarmModelRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    alarm_model_version: Optional[str] = Field(default=None, alias="alarmModelVersion")


class DescribeDetectorModelAnalysisRequestModel(BaseModel):
    analysis_id: str = Field(alias="analysisId")


class DescribeDetectorModelRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    detector_model_version: Optional[str] = Field(
        default=None, alias="detectorModelVersion"
    )


class DescribeInputRequestModel(BaseModel):
    input_name: str = Field(alias="inputName")


class DetectorDebugOptionModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")


class DetectorModelSummaryModel(BaseModel):
    detector_model_name: Optional[str] = Field(default=None, alias="detectorModelName")
    detector_model_description: Optional[str] = Field(
        default=None, alias="detectorModelDescription"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")


class DetectorModelVersionSummaryModel(BaseModel):
    detector_model_name: Optional[str] = Field(default=None, alias="detectorModelName")
    detector_model_version: Optional[str] = Field(
        default=None, alias="detectorModelVersion"
    )
    detector_model_arn: Optional[str] = Field(default=None, alias="detectorModelArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "DEPRECATED",
            "DRAFT",
            "FAILED",
            "INACTIVE",
            "PAUSED",
        ]
    ] = Field(default=None, alias="status")
    evaluation_method: Optional[Literal["BATCH", "SERIAL"]] = Field(
        default=None, alias="evaluationMethod"
    )


class PayloadModel(BaseModel):
    content_expression: str = Field(alias="contentExpression")
    type: Literal["JSON", "STRING"] = Field(alias="type")


class EmailContentModel(BaseModel):
    subject: Optional[str] = Field(default=None, alias="subject")
    additional_message: Optional[str] = Field(default=None, alias="additionalMessage")


class GetDetectorModelAnalysisResultsRequestModel(BaseModel):
    analysis_id: str = Field(alias="analysisId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class IotEventsInputIdentifierModel(BaseModel):
    input_name: str = Field(alias="inputName")


class InputSummaryModel(BaseModel):
    input_name: Optional[str] = Field(default=None, alias="inputName")
    input_description: Optional[str] = Field(default=None, alias="inputDescription")
    input_arn: Optional[str] = Field(default=None, alias="inputArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]] = Field(
        default=None, alias="status"
    )


class IotSiteWiseAssetModelPropertyIdentifierModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    property_id: str = Field(alias="propertyId")


class ListAlarmModelVersionsRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAlarmModelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDetectorModelVersionsRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDetectorModelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RoutedResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")


class ListInputsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class SSOIdentityModel(BaseModel):
    identity_store_id: str = Field(alias="identityStoreId")
    user_id: Optional[str] = Field(default=None, alias="userId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AlarmCapabilitiesModel(BaseModel):
    initialization_configuration: Optional[InitializationConfigurationModel] = Field(
        default=None, alias="initializationConfiguration"
    )
    acknowledge_flow: Optional[AcknowledgeFlowModel] = Field(
        default=None, alias="acknowledgeFlow"
    )


class AlarmRuleModel(BaseModel):
    simple_rule: Optional[SimpleRuleModel] = Field(default=None, alias="simpleRule")


class AnalysisResultModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    level: Optional[Literal["ERROR", "INFO", "WARNING"]] = Field(
        default=None, alias="level"
    )
    message: Optional[str] = Field(default=None, alias="message")
    locations: Optional[List[AnalysisResultLocationModel]] = Field(
        default=None, alias="locations"
    )


class AssetPropertyValueModel(BaseModel):
    value: Optional[AssetPropertyVariantModel] = Field(default=None, alias="value")
    timestamp: Optional[AssetPropertyTimestampModel] = Field(
        default=None, alias="timestamp"
    )
    quality: Optional[str] = Field(default=None, alias="quality")


class InputDefinitionModel(BaseModel):
    attributes: Sequence[AttributeModel] = Field(alias="attributes")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateAlarmModelResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    alarm_model_arn: str = Field(alias="alarmModelArn")
    alarm_model_version: str = Field(alias="alarmModelVersion")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    status: Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDetectorModelAnalysisResponseModel(BaseModel):
    status: Literal["COMPLETE", "FAILED", "RUNNING"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAlarmModelVersionsResponseModel(BaseModel):
    alarm_model_version_summaries: List[AlarmModelVersionSummaryModel] = Field(
        alias="alarmModelVersionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAlarmModelsResponseModel(BaseModel):
    alarm_model_summaries: List[AlarmModelSummaryModel] = Field(
        alias="alarmModelSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDetectorModelAnalysisResponseModel(BaseModel):
    analysis_id: str = Field(alias="analysisId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAlarmModelResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    alarm_model_arn: str = Field(alias="alarmModelArn")
    alarm_model_version: str = Field(alias="alarmModelVersion")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    status: Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDetectorModelResponseModel(BaseModel):
    detector_model_configuration: DetectorModelConfigurationModel = Field(
        alias="detectorModelConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDetectorModelResponseModel(BaseModel):
    detector_model_configuration: DetectorModelConfigurationModel = Field(
        alias="detectorModelConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInputResponseModel(BaseModel):
    input_configuration: InputConfigurationModel = Field(alias="inputConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInputResponseModel(BaseModel):
    input_configuration: InputConfigurationModel = Field(alias="inputConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingOptionsModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    level: Literal["DEBUG", "ERROR", "INFO"] = Field(alias="level")
    enabled: bool = Field(alias="enabled")
    detector_debug_options: Optional[List[DetectorDebugOptionModel]] = Field(
        default=None, alias="detectorDebugOptions"
    )


class ListDetectorModelsResponseModel(BaseModel):
    detector_model_summaries: List[DetectorModelSummaryModel] = Field(
        alias="detectorModelSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDetectorModelVersionsResponseModel(BaseModel):
    detector_model_version_summaries: List[DetectorModelVersionSummaryModel] = Field(
        alias="detectorModelVersionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DynamoDBActionModel(BaseModel):
    hash_key_field: str = Field(alias="hashKeyField")
    hash_key_value: str = Field(alias="hashKeyValue")
    table_name: str = Field(alias="tableName")
    hash_key_type: Optional[str] = Field(default=None, alias="hashKeyType")
    range_key_type: Optional[str] = Field(default=None, alias="rangeKeyType")
    range_key_field: Optional[str] = Field(default=None, alias="rangeKeyField")
    range_key_value: Optional[str] = Field(default=None, alias="rangeKeyValue")
    operation: Optional[str] = Field(default=None, alias="operation")
    payload_field: Optional[str] = Field(default=None, alias="payloadField")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class DynamoDBv2ActionModel(BaseModel):
    table_name: str = Field(alias="tableName")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class FirehoseActionModel(BaseModel):
    delivery_stream_name: str = Field(alias="deliveryStreamName")
    separator: Optional[str] = Field(default=None, alias="separator")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class IotEventsActionModel(BaseModel):
    input_name: str = Field(alias="inputName")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class IotTopicPublishActionModel(BaseModel):
    mqtt_topic: str = Field(alias="mqttTopic")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class LambdaActionModel(BaseModel):
    function_arn: str = Field(alias="functionArn")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class SNSTopicPublishActionModel(BaseModel):
    target_arn: str = Field(alias="targetArn")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class SqsActionModel(BaseModel):
    queue_url: str = Field(alias="queueUrl")
    use_base64: Optional[bool] = Field(default=None, alias="useBase64")
    payload: Optional[PayloadModel] = Field(default=None, alias="payload")


class ListInputsResponseModel(BaseModel):
    input_summaries: List[InputSummaryModel] = Field(alias="inputSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IotSiteWiseInputIdentifierModel(BaseModel):
    iot_site_wise_asset_model_property_identifier: Optional[
        IotSiteWiseAssetModelPropertyIdentifierModel
    ] = Field(default=None, alias="iotSiteWiseAssetModelPropertyIdentifier")


class ListInputRoutingsResponseModel(BaseModel):
    routed_resources: List[RoutedResourceModel] = Field(alias="routedResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecipientDetailModel(BaseModel):
    sso_identity: Optional[SSOIdentityModel] = Field(default=None, alias="ssoIdentity")


class GetDetectorModelAnalysisResultsResponseModel(BaseModel):
    analysis_results: List[AnalysisResultModel] = Field(alias="analysisResults")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IotSiteWiseActionModel(BaseModel):
    entry_id: Optional[str] = Field(default=None, alias="entryId")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    property_value: Optional[AssetPropertyValueModel] = Field(
        default=None, alias="propertyValue"
    )


class CreateInputRequestModel(BaseModel):
    input_name: str = Field(alias="inputName")
    input_definition: InputDefinitionModel = Field(alias="inputDefinition")
    input_description: Optional[str] = Field(default=None, alias="inputDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class InputModel(BaseModel):
    input_configuration: Optional[InputConfigurationModel] = Field(
        default=None, alias="inputConfiguration"
    )
    input_definition: Optional[InputDefinitionModel] = Field(
        default=None, alias="inputDefinition"
    )


class UpdateInputRequestModel(BaseModel):
    input_name: str = Field(alias="inputName")
    input_definition: InputDefinitionModel = Field(alias="inputDefinition")
    input_description: Optional[str] = Field(default=None, alias="inputDescription")


class DescribeLoggingOptionsResponseModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingOptionsRequestModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")


class NotificationTargetActionsModel(BaseModel):
    lambda_action: Optional[LambdaActionModel] = Field(
        default=None, alias="lambdaAction"
    )


class InputIdentifierModel(BaseModel):
    iot_events_input_identifier: Optional[IotEventsInputIdentifierModel] = Field(
        default=None, alias="iotEventsInputIdentifier"
    )
    iot_site_wise_input_identifier: Optional[IotSiteWiseInputIdentifierModel] = Field(
        default=None, alias="iotSiteWiseInputIdentifier"
    )


class EmailRecipientsModel(BaseModel):
    to: Optional[Sequence[RecipientDetailModel]] = Field(default=None, alias="to")


class SMSConfigurationModel(BaseModel):
    recipients: Sequence[RecipientDetailModel] = Field(alias="recipients")
    sender_id: Optional[str] = Field(default=None, alias="senderId")
    additional_message: Optional[str] = Field(default=None, alias="additionalMessage")


class ActionModel(BaseModel):
    set_variable: Optional[SetVariableActionModel] = Field(
        default=None, alias="setVariable"
    )
    sns: Optional[SNSTopicPublishActionModel] = Field(default=None, alias="sns")
    iot_topic_publish: Optional[IotTopicPublishActionModel] = Field(
        default=None, alias="iotTopicPublish"
    )
    set_timer: Optional[SetTimerActionModel] = Field(default=None, alias="setTimer")
    clear_timer: Optional[ClearTimerActionModel] = Field(
        default=None, alias="clearTimer"
    )
    reset_timer: Optional[ResetTimerActionModel] = Field(
        default=None, alias="resetTimer"
    )
    lambda_: Optional[LambdaActionModel] = Field(default=None, alias="lambda")
    iot_events: Optional[IotEventsActionModel] = Field(default=None, alias="iotEvents")
    sqs: Optional[SqsActionModel] = Field(default=None, alias="sqs")
    firehose: Optional[FirehoseActionModel] = Field(default=None, alias="firehose")
    dynamo_db: Optional[DynamoDBActionModel] = Field(default=None, alias="dynamoDB")
    dynamo_dbv2: Optional[DynamoDBv2ActionModel] = Field(
        default=None, alias="dynamoDBv2"
    )
    iot_site_wise: Optional[IotSiteWiseActionModel] = Field(
        default=None, alias="iotSiteWise"
    )


class AlarmActionModel(BaseModel):
    sns: Optional[SNSTopicPublishActionModel] = Field(default=None, alias="sns")
    iot_topic_publish: Optional[IotTopicPublishActionModel] = Field(
        default=None, alias="iotTopicPublish"
    )
    lambda_: Optional[LambdaActionModel] = Field(default=None, alias="lambda")
    iot_events: Optional[IotEventsActionModel] = Field(default=None, alias="iotEvents")
    sqs: Optional[SqsActionModel] = Field(default=None, alias="sqs")
    firehose: Optional[FirehoseActionModel] = Field(default=None, alias="firehose")
    dynamo_db: Optional[DynamoDBActionModel] = Field(default=None, alias="dynamoDB")
    dynamo_dbv2: Optional[DynamoDBv2ActionModel] = Field(
        default=None, alias="dynamoDBv2"
    )
    iot_site_wise: Optional[IotSiteWiseActionModel] = Field(
        default=None, alias="iotSiteWise"
    )


class DescribeInputResponseModel(BaseModel):
    input: InputModel = Field(alias="input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInputRoutingsRequestModel(BaseModel):
    input_identifier: InputIdentifierModel = Field(alias="inputIdentifier")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class EmailConfigurationModel(BaseModel):
    from_: str = Field(alias="from")
    recipients: EmailRecipientsModel = Field(alias="recipients")
    content: Optional[EmailContentModel] = Field(default=None, alias="content")


class EventModel(BaseModel):
    event_name: str = Field(alias="eventName")
    condition: Optional[str] = Field(default=None, alias="condition")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="actions")


class TransitionEventModel(BaseModel):
    event_name: str = Field(alias="eventName")
    condition: str = Field(alias="condition")
    next_state: str = Field(alias="nextState")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="actions")


class AlarmEventActionsModel(BaseModel):
    alarm_actions: Optional[Sequence[AlarmActionModel]] = Field(
        default=None, alias="alarmActions"
    )


class NotificationActionModel(BaseModel):
    action: NotificationTargetActionsModel = Field(alias="action")
    sms_configurations: Optional[Sequence[SMSConfigurationModel]] = Field(
        default=None, alias="smsConfigurations"
    )
    email_configurations: Optional[Sequence[EmailConfigurationModel]] = Field(
        default=None, alias="emailConfigurations"
    )


class OnEnterLifecycleModel(BaseModel):
    events: Optional[Sequence[EventModel]] = Field(default=None, alias="events")


class OnExitLifecycleModel(BaseModel):
    events: Optional[Sequence[EventModel]] = Field(default=None, alias="events")


class OnInputLifecycleModel(BaseModel):
    events: Optional[Sequence[EventModel]] = Field(default=None, alias="events")
    transition_events: Optional[Sequence[TransitionEventModel]] = Field(
        default=None, alias="transitionEvents"
    )


class AlarmNotificationModel(BaseModel):
    notification_actions: Optional[Sequence[NotificationActionModel]] = Field(
        default=None, alias="notificationActions"
    )


class StateModel(BaseModel):
    state_name: str = Field(alias="stateName")
    on_input: Optional[OnInputLifecycleModel] = Field(default=None, alias="onInput")
    on_enter: Optional[OnEnterLifecycleModel] = Field(default=None, alias="onEnter")
    on_exit: Optional[OnExitLifecycleModel] = Field(default=None, alias="onExit")


class CreateAlarmModelRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    role_arn: str = Field(alias="roleArn")
    alarm_rule: AlarmRuleModel = Field(alias="alarmRule")
    alarm_model_description: Optional[str] = Field(
        default=None, alias="alarmModelDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    key: Optional[str] = Field(default=None, alias="key")
    severity: Optional[int] = Field(default=None, alias="severity")
    alarm_notification: Optional[AlarmNotificationModel] = Field(
        default=None, alias="alarmNotification"
    )
    alarm_event_actions: Optional[AlarmEventActionsModel] = Field(
        default=None, alias="alarmEventActions"
    )
    alarm_capabilities: Optional[AlarmCapabilitiesModel] = Field(
        default=None, alias="alarmCapabilities"
    )


class DescribeAlarmModelResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    alarm_model_arn: str = Field(alias="alarmModelArn")
    alarm_model_version: str = Field(alias="alarmModelVersion")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    status: Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    alarm_model_name: str = Field(alias="alarmModelName")
    alarm_model_description: str = Field(alias="alarmModelDescription")
    role_arn: str = Field(alias="roleArn")
    key: str = Field(alias="key")
    severity: int = Field(alias="severity")
    alarm_rule: AlarmRuleModel = Field(alias="alarmRule")
    alarm_notification: AlarmNotificationModel = Field(alias="alarmNotification")
    alarm_event_actions: AlarmEventActionsModel = Field(alias="alarmEventActions")
    alarm_capabilities: AlarmCapabilitiesModel = Field(alias="alarmCapabilities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAlarmModelRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    role_arn: str = Field(alias="roleArn")
    alarm_rule: AlarmRuleModel = Field(alias="alarmRule")
    alarm_model_description: Optional[str] = Field(
        default=None, alias="alarmModelDescription"
    )
    severity: Optional[int] = Field(default=None, alias="severity")
    alarm_notification: Optional[AlarmNotificationModel] = Field(
        default=None, alias="alarmNotification"
    )
    alarm_event_actions: Optional[AlarmEventActionsModel] = Field(
        default=None, alias="alarmEventActions"
    )
    alarm_capabilities: Optional[AlarmCapabilitiesModel] = Field(
        default=None, alias="alarmCapabilities"
    )


class DetectorModelDefinitionModel(BaseModel):
    states: Sequence[StateModel] = Field(alias="states")
    initial_state_name: str = Field(alias="initialStateName")


class CreateDetectorModelRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    detector_model_definition: DetectorModelDefinitionModel = Field(
        alias="detectorModelDefinition"
    )
    role_arn: str = Field(alias="roleArn")
    detector_model_description: Optional[str] = Field(
        default=None, alias="detectorModelDescription"
    )
    key: Optional[str] = Field(default=None, alias="key")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    evaluation_method: Optional[Literal["BATCH", "SERIAL"]] = Field(
        default=None, alias="evaluationMethod"
    )


class DetectorModelModel(BaseModel):
    detector_model_definition: Optional[DetectorModelDefinitionModel] = Field(
        default=None, alias="detectorModelDefinition"
    )
    detector_model_configuration: Optional[DetectorModelConfigurationModel] = Field(
        default=None, alias="detectorModelConfiguration"
    )


class StartDetectorModelAnalysisRequestModel(BaseModel):
    detector_model_definition: DetectorModelDefinitionModel = Field(
        alias="detectorModelDefinition"
    )


class UpdateDetectorModelRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    detector_model_definition: DetectorModelDefinitionModel = Field(
        alias="detectorModelDefinition"
    )
    role_arn: str = Field(alias="roleArn")
    detector_model_description: Optional[str] = Field(
        default=None, alias="detectorModelDescription"
    )
    evaluation_method: Optional[Literal["BATCH", "SERIAL"]] = Field(
        default=None, alias="evaluationMethod"
    )


class DescribeDetectorModelResponseModel(BaseModel):
    detector_model: DetectorModelModel = Field(alias="detectorModel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
