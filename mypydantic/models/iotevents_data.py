# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcknowledgeActionConfigurationModel(BaseModel):
    note: Optional[str] = Field(default=None, alias="note")


class AcknowledgeAlarmActionRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    alarm_model_name: str = Field(alias="alarmModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    note: Optional[str] = Field(default=None, alias="note")


class AlarmSummaryModel(BaseModel):
    alarm_model_name: Optional[str] = Field(default=None, alias="alarmModelName")
    alarm_model_version: Optional[str] = Field(default=None, alias="alarmModelVersion")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    state_name: Optional[
        Literal[
            "ACKNOWLEDGED", "ACTIVE", "DISABLED", "LATCHED", "NORMAL", "SNOOZE_DISABLED"
        ]
    ] = Field(default=None, alias="stateName")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class BatchAlarmActionErrorEntryModel(BaseModel):
    request_id: Optional[str] = Field(default=None, alias="requestId")
    error_code: Optional[
        Literal[
            "InternalFailureException",
            "InvalidRequestException",
            "ResourceNotFoundException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDeleteDetectorErrorEntryModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="messageId")
    error_code: Optional[
        Literal[
            "InternalFailureException",
            "InvalidRequestException",
            "ResourceNotFoundException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class DeleteDetectorRequestModel(BaseModel):
    message_id: str = Field(alias="messageId")
    detector_model_name: str = Field(alias="detectorModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")


class DisableAlarmActionRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    alarm_model_name: str = Field(alias="alarmModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    note: Optional[str] = Field(default=None, alias="note")


class EnableAlarmActionRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    alarm_model_name: str = Field(alias="alarmModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    note: Optional[str] = Field(default=None, alias="note")


class BatchPutMessageErrorEntryModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="messageId")
    error_code: Optional[
        Literal[
            "InternalFailureException",
            "InvalidRequestException",
            "ResourceNotFoundException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class ResetAlarmActionRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    alarm_model_name: str = Field(alias="alarmModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    note: Optional[str] = Field(default=None, alias="note")


class SnoozeAlarmActionRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    alarm_model_name: str = Field(alias="alarmModelName")
    snooze_duration: int = Field(alias="snoozeDuration")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    note: Optional[str] = Field(default=None, alias="note")


class BatchUpdateDetectorErrorEntryModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="messageId")
    error_code: Optional[
        Literal[
            "InternalFailureException",
            "InvalidRequestException",
            "ResourceNotFoundException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class DisableActionConfigurationModel(BaseModel):
    note: Optional[str] = Field(default=None, alias="note")


class EnableActionConfigurationModel(BaseModel):
    note: Optional[str] = Field(default=None, alias="note")


class ResetActionConfigurationModel(BaseModel):
    note: Optional[str] = Field(default=None, alias="note")


class SnoozeActionConfigurationModel(BaseModel):
    snooze_duration: Optional[int] = Field(default=None, alias="snoozeDuration")
    note: Optional[str] = Field(default=None, alias="note")


class DescribeAlarmRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")


class DescribeDetectorRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")


class TimerDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    seconds: int = Field(alias="seconds")


class VariableDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    value: str = Field(alias="value")


class DetectorStateSummaryModel(BaseModel):
    state_name: Optional[str] = Field(default=None, alias="stateName")


class TimerModel(BaseModel):
    name: str = Field(alias="name")
    timestamp: datetime = Field(alias="timestamp")


class VariableModel(BaseModel):
    name: str = Field(alias="name")
    value: str = Field(alias="value")


class ListAlarmsRequestModel(BaseModel):
    alarm_model_name: str = Field(alias="alarmModelName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDetectorsRequestModel(BaseModel):
    detector_model_name: str = Field(alias="detectorModelName")
    state_name: Optional[str] = Field(default=None, alias="stateName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class TimestampValueModel(BaseModel):
    time_in_millis: Optional[int] = Field(default=None, alias="timeInMillis")


class SimpleRuleEvaluationModel(BaseModel):
    input_property_value: Optional[str] = Field(
        default=None, alias="inputPropertyValue"
    )
    operator: Optional[
        Literal[
            "EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "NOT_EQUAL"
        ]
    ] = Field(default=None, alias="operator")
    threshold_value: Optional[str] = Field(default=None, alias="thresholdValue")


class StateChangeConfigurationModel(BaseModel):
    trigger_type: Optional[Literal["SNOOZE_TIMEOUT"]] = Field(
        default=None, alias="triggerType"
    )


class BatchAcknowledgeAlarmRequestModel(BaseModel):
    acknowledge_action_requests: Sequence[AcknowledgeAlarmActionRequestModel] = Field(
        alias="acknowledgeActionRequests"
    )


class BatchAcknowledgeAlarmResponseModel(BaseModel):
    error_entries: List[BatchAlarmActionErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisableAlarmResponseModel(BaseModel):
    error_entries: List[BatchAlarmActionErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchEnableAlarmResponseModel(BaseModel):
    error_entries: List[BatchAlarmActionErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchResetAlarmResponseModel(BaseModel):
    error_entries: List[BatchAlarmActionErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchSnoozeAlarmResponseModel(BaseModel):
    error_entries: List[BatchAlarmActionErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAlarmsResponseModel(BaseModel):
    alarm_summaries: List[AlarmSummaryModel] = Field(alias="alarmSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteDetectorResponseModel(BaseModel):
    batch_delete_detector_error_entries: List[
        BatchDeleteDetectorErrorEntryModel
    ] = Field(alias="batchDeleteDetectorErrorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteDetectorRequestModel(BaseModel):
    detectors: Sequence[DeleteDetectorRequestModel] = Field(alias="detectors")


class BatchDisableAlarmRequestModel(BaseModel):
    disable_action_requests: Sequence[DisableAlarmActionRequestModel] = Field(
        alias="disableActionRequests"
    )


class BatchEnableAlarmRequestModel(BaseModel):
    enable_action_requests: Sequence[EnableAlarmActionRequestModel] = Field(
        alias="enableActionRequests"
    )


class BatchPutMessageResponseModel(BaseModel):
    batch_put_message_error_entries: List[BatchPutMessageErrorEntryModel] = Field(
        alias="BatchPutMessageErrorEntries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchResetAlarmRequestModel(BaseModel):
    reset_action_requests: Sequence[ResetAlarmActionRequestModel] = Field(
        alias="resetActionRequests"
    )


class BatchSnoozeAlarmRequestModel(BaseModel):
    snooze_action_requests: Sequence[SnoozeAlarmActionRequestModel] = Field(
        alias="snoozeActionRequests"
    )


class BatchUpdateDetectorResponseModel(BaseModel):
    batch_update_detector_error_entries: List[
        BatchUpdateDetectorErrorEntryModel
    ] = Field(alias="batchUpdateDetectorErrorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomerActionModel(BaseModel):
    action_name: Optional[
        Literal["ACKNOWLEDGE", "DISABLE", "ENABLE", "RESET", "SNOOZE"]
    ] = Field(default=None, alias="actionName")
    snooze_action_configuration: Optional[SnoozeActionConfigurationModel] = Field(
        default=None, alias="snoozeActionConfiguration"
    )
    enable_action_configuration: Optional[EnableActionConfigurationModel] = Field(
        default=None, alias="enableActionConfiguration"
    )
    disable_action_configuration: Optional[DisableActionConfigurationModel] = Field(
        default=None, alias="disableActionConfiguration"
    )
    acknowledge_action_configuration: Optional[
        AcknowledgeActionConfigurationModel
    ] = Field(default=None, alias="acknowledgeActionConfiguration")
    reset_action_configuration: Optional[ResetActionConfigurationModel] = Field(
        default=None, alias="resetActionConfiguration"
    )


class DetectorStateDefinitionModel(BaseModel):
    state_name: str = Field(alias="stateName")
    variables: Sequence[VariableDefinitionModel] = Field(alias="variables")
    timers: Sequence[TimerDefinitionModel] = Field(alias="timers")


class DetectorSummaryModel(BaseModel):
    detector_model_name: Optional[str] = Field(default=None, alias="detectorModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    detector_model_version: Optional[str] = Field(
        default=None, alias="detectorModelVersion"
    )
    state: Optional[DetectorStateSummaryModel] = Field(default=None, alias="state")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class DetectorStateModel(BaseModel):
    state_name: str = Field(alias="stateName")
    variables: List[VariableModel] = Field(alias="variables")
    timers: List[TimerModel] = Field(alias="timers")


class MessageModel(BaseModel):
    message_id: str = Field(alias="messageId")
    input_name: str = Field(alias="inputName")
    payload: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="payload"
    )
    timestamp: Optional[TimestampValueModel] = Field(default=None, alias="timestamp")


class RuleEvaluationModel(BaseModel):
    simple_rule_evaluation: Optional[SimpleRuleEvaluationModel] = Field(
        default=None, alias="simpleRuleEvaluation"
    )


class SystemEventModel(BaseModel):
    event_type: Optional[Literal["STATE_CHANGE"]] = Field(
        default=None, alias="eventType"
    )
    state_change_configuration: Optional[StateChangeConfigurationModel] = Field(
        default=None, alias="stateChangeConfiguration"
    )


class UpdateDetectorRequestModel(BaseModel):
    message_id: str = Field(alias="messageId")
    detector_model_name: str = Field(alias="detectorModelName")
    state: DetectorStateDefinitionModel = Field(alias="state")
    key_value: Optional[str] = Field(default=None, alias="keyValue")


class ListDetectorsResponseModel(BaseModel):
    detector_summaries: List[DetectorSummaryModel] = Field(alias="detectorSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectorModel(BaseModel):
    detector_model_name: Optional[str] = Field(default=None, alias="detectorModelName")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    detector_model_version: Optional[str] = Field(
        default=None, alias="detectorModelVersion"
    )
    state: Optional[DetectorStateModel] = Field(default=None, alias="state")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class BatchPutMessageRequestModel(BaseModel):
    messages: Sequence[MessageModel] = Field(alias="messages")


class AlarmStateModel(BaseModel):
    state_name: Optional[
        Literal[
            "ACKNOWLEDGED", "ACTIVE", "DISABLED", "LATCHED", "NORMAL", "SNOOZE_DISABLED"
        ]
    ] = Field(default=None, alias="stateName")
    rule_evaluation: Optional[RuleEvaluationModel] = Field(
        default=None, alias="ruleEvaluation"
    )
    customer_action: Optional[CustomerActionModel] = Field(
        default=None, alias="customerAction"
    )
    system_event: Optional[SystemEventModel] = Field(default=None, alias="systemEvent")


class BatchUpdateDetectorRequestModel(BaseModel):
    detectors: Sequence[UpdateDetectorRequestModel] = Field(alias="detectors")


class DescribeDetectorResponseModel(BaseModel):
    detector: DetectorModel = Field(alias="detector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AlarmModel(BaseModel):
    alarm_model_name: Optional[str] = Field(default=None, alias="alarmModelName")
    alarm_model_version: Optional[str] = Field(default=None, alias="alarmModelVersion")
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    alarm_state: Optional[AlarmStateModel] = Field(default=None, alias="alarmState")
    severity: Optional[int] = Field(default=None, alias="severity")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class DescribeAlarmResponseModel(BaseModel):
    alarm: AlarmModel = Field(alias="alarm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
