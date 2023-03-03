# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ATIMetricDataPointModel(BaseModel):
    cr: Optional[float] = Field(default=None, alias="cr")
    adr: Optional[float] = Field(default=None, alias="adr")
    threshold: Optional[float] = Field(default=None, alias="threshold")
    atodr: Optional[float] = Field(default=None, alias="atodr")


class ATIModelPerformanceModel(BaseModel):
    asi: Optional[float] = Field(default=None, alias="asi")


class AggregatedLogOddsMetricModel(BaseModel):
    variable_names: List[str] = Field(alias="variableNames")
    aggregated_variables_importance: float = Field(
        alias="aggregatedVariablesImportance"
    )


class AggregatedVariablesImpactExplanationModel(BaseModel):
    event_variable_names: Optional[List[str]] = Field(
        default=None, alias="eventVariableNames"
    )
    relative_impact: Optional[str] = Field(default=None, alias="relativeImpact")
    log_odds_impact: Optional[float] = Field(default=None, alias="logOddsImpact")


class AllowDenyListModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    variable_type: Optional[str] = Field(default=None, alias="variableType")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    updated_time: Optional[str] = Field(default=None, alias="updatedTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class BatchCreateVariableErrorModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    code: Optional[int] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class VariableEntryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    data_type: Optional[str] = Field(default=None, alias="dataType")
    data_source: Optional[str] = Field(default=None, alias="dataSource")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    description: Optional[str] = Field(default=None, alias="description")
    variable_type: Optional[str] = Field(default=None, alias="variableType")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetVariableErrorModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    code: Optional[int] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class BatchGetVariableRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="names")


class VariableModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    data_type: Optional[Literal["BOOLEAN", "FLOAT", "INTEGER", "STRING"]] = Field(
        default=None, alias="dataType"
    )
    data_source: Optional[
        Literal["EVENT", "EXTERNAL_MODEL_SCORE", "MODEL_SCORE"]
    ] = Field(default=None, alias="dataSource")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    description: Optional[str] = Field(default=None, alias="description")
    variable_type: Optional[str] = Field(default=None, alias="variableType")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class BatchImportModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    status: Optional[
        Literal[
            "CANCELED",
            "CANCEL_IN_PROGRESS",
            "COMPLETE",
            "FAILED",
            "IN_PROGRESS",
            "IN_PROGRESS_INITIALIZING",
        ]
    ] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    start_time: Optional[str] = Field(default=None, alias="startTime")
    completion_time: Optional[str] = Field(default=None, alias="completionTime")
    input_path: Optional[str] = Field(default=None, alias="inputPath")
    output_path: Optional[str] = Field(default=None, alias="outputPath")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    iam_role_arn: Optional[str] = Field(default=None, alias="iamRoleArn")
    arn: Optional[str] = Field(default=None, alias="arn")
    processed_records_count: Optional[int] = Field(
        default=None, alias="processedRecordsCount"
    )
    failed_records_count: Optional[int] = Field(
        default=None, alias="failedRecordsCount"
    )
    total_records_count: Optional[int] = Field(default=None, alias="totalRecordsCount")


class BatchPredictionModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    status: Optional[
        Literal[
            "CANCELED",
            "CANCEL_IN_PROGRESS",
            "COMPLETE",
            "FAILED",
            "IN_PROGRESS",
            "IN_PROGRESS_INITIALIZING",
        ]
    ] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    start_time: Optional[str] = Field(default=None, alias="startTime")
    completion_time: Optional[str] = Field(default=None, alias="completionTime")
    last_heartbeat_time: Optional[str] = Field(default=None, alias="lastHeartbeatTime")
    input_path: Optional[str] = Field(default=None, alias="inputPath")
    output_path: Optional[str] = Field(default=None, alias="outputPath")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    detector_name: Optional[str] = Field(default=None, alias="detectorName")
    detector_version: Optional[str] = Field(default=None, alias="detectorVersion")
    iam_role_arn: Optional[str] = Field(default=None, alias="iamRoleArn")
    arn: Optional[str] = Field(default=None, alias="arn")
    processed_records_count: Optional[int] = Field(
        default=None, alias="processedRecordsCount"
    )
    total_records_count: Optional[int] = Field(default=None, alias="totalRecordsCount")


class CancelBatchImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class CancelBatchPredictionJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class ModelVersionModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")
    arn: Optional[str] = Field(default=None, alias="arn")


class RuleModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    rule_id: str = Field(alias="ruleId")
    rule_version: str = Field(alias="ruleVersion")


class ExternalEventsDetailModel(BaseModel):
    data_location: str = Field(alias="dataLocation")
    data_access_role_arn: str = Field(alias="dataAccessRoleArn")


class FieldValidationMessageModel(BaseModel):
    field_name: Optional[str] = Field(default=None, alias="fieldName")
    identifier: Optional[str] = Field(default=None, alias="identifier")
    title: Optional[str] = Field(default=None, alias="title")
    content: Optional[str] = Field(default=None, alias="content")
    type: Optional[str] = Field(default=None, alias="type")


class FileValidationMessageModel(BaseModel):
    title: Optional[str] = Field(default=None, alias="title")
    content: Optional[str] = Field(default=None, alias="content")
    type: Optional[str] = Field(default=None, alias="type")


class DeleteBatchImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class DeleteBatchPredictionJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class DeleteDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")


class DeleteDetectorVersionRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")


class DeleteEntityTypeRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteEventRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    delete_audit_history: Optional[bool] = Field(
        default=None, alias="deleteAuditHistory"
    )


class DeleteEventTypeRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteEventsByEventTypeRequestModel(BaseModel):
    event_type_name: str = Field(alias="eventTypeName")


class DeleteExternalModelRequestModel(BaseModel):
    model_endpoint: str = Field(alias="modelEndpoint")


class DeleteLabelRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteListRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteModelRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")


class DeleteModelVersionRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")


class DeleteOutcomeRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteVariableRequestModel(BaseModel):
    name: str = Field(alias="name")


class DescribeDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DetectorVersionSummaryModel(BaseModel):
    detector_version_id: Optional[str] = Field(default=None, alias="detectorVersionId")
    status: Optional[Literal["ACTIVE", "DRAFT", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")


class DescribeModelVersionsRequestModel(BaseModel):
    model_id: Optional[str] = Field(default=None, alias="modelId")
    model_version_number: Optional[str] = Field(
        default=None, alias="modelVersionNumber"
    )
    model_type: Optional[
        Literal[
            "ACCOUNT_TAKEOVER_INSIGHTS",
            "ONLINE_FRAUD_INSIGHTS",
            "TRANSACTION_FRAUD_INSIGHTS",
        ]
    ] = Field(default=None, alias="modelType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DetectorModel(BaseModel):
    detector_id: Optional[str] = Field(default=None, alias="detectorId")
    description: Optional[str] = Field(default=None, alias="description")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class EntityModel(BaseModel):
    entity_type: str = Field(alias="entityType")
    entity_id: str = Field(alias="entityId")


class EntityTypeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class EvaluatedExternalModelModel(BaseModel):
    model_endpoint: Optional[str] = Field(default=None, alias="modelEndpoint")
    use_event_variables: Optional[bool] = Field(default=None, alias="useEventVariables")
    input_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="inputVariables"
    )
    output_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="outputVariables"
    )


class EvaluatedRuleModel(BaseModel):
    rule_id: Optional[str] = Field(default=None, alias="ruleId")
    rule_version: Optional[str] = Field(default=None, alias="ruleVersion")
    expression: Optional[str] = Field(default=None, alias="expression")
    expression_with_values: Optional[str] = Field(
        default=None, alias="expressionWithValues"
    )
    outcomes: Optional[List[str]] = Field(default=None, alias="outcomes")
    evaluated: Optional[bool] = Field(default=None, alias="evaluated")
    matched: Optional[bool] = Field(default=None, alias="matched")


class EventPredictionSummaryModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="eventId")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    event_timestamp: Optional[str] = Field(default=None, alias="eventTimestamp")
    prediction_timestamp: Optional[str] = Field(
        default=None, alias="predictionTimestamp"
    )
    detector_id: Optional[str] = Field(default=None, alias="detectorId")
    detector_version_id: Optional[str] = Field(default=None, alias="detectorVersionId")


class IngestedEventStatisticsModel(BaseModel):
    number_of_events: Optional[int] = Field(default=None, alias="numberOfEvents")
    event_data_size_in_bytes: Optional[int] = Field(
        default=None, alias="eventDataSizeInBytes"
    )
    least_recent_event: Optional[str] = Field(default=None, alias="leastRecentEvent")
    most_recent_event: Optional[str] = Field(default=None, alias="mostRecentEvent")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")


class EventVariableSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")
    source: Optional[str] = Field(default=None, alias="source")


class ExternalModelSummaryModel(BaseModel):
    model_endpoint: Optional[str] = Field(default=None, alias="modelEndpoint")
    model_source: Optional[Literal["SAGEMAKER"]] = Field(
        default=None, alias="modelSource"
    )


class ModelInputConfigurationModel(BaseModel):
    use_event_variables: bool = Field(alias="useEventVariables")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    format: Optional[Literal["APPLICATION_JSON", "TEXT_CSV"]] = Field(
        default=None, alias="format"
    )
    json_input_template: Optional[str] = Field(default=None, alias="jsonInputTemplate")
    csv_input_template: Optional[str] = Field(default=None, alias="csvInputTemplate")


class ModelOutputConfigurationModel(BaseModel):
    format: Literal["APPLICATION_JSONLINES", "TEXT_CSV"] = Field(alias="format")
    json_key_to_variable_map: Optional[Dict[str, str]] = Field(
        default=None, alias="jsonKeyToVariableMap"
    )
    csv_index_to_variable_map: Optional[Dict[str, str]] = Field(
        default=None, alias="csvIndexToVariableMap"
    )


class FilterConditionModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="value")


class GetBatchImportJobsRequestModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetBatchPredictionJobsRequestModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetDeleteEventsByEventTypeStatusRequestModel(BaseModel):
    event_type_name: str = Field(alias="eventTypeName")


class GetDetectorVersionRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")


class GetDetectorsRequestModel(BaseModel):
    detector_id: Optional[str] = Field(default=None, alias="detectorId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEntityTypesRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEventPredictionMetadataRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    prediction_timestamp: str = Field(alias="predictionTimestamp")


class ModelEndpointDataBlobModel(BaseModel):
    byte_buffer: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="byteBuffer")
    content_type: Optional[str] = Field(default=None, alias="contentType")


class RuleResultModel(BaseModel):
    rule_id: Optional[str] = Field(default=None, alias="ruleId")
    outcomes: Optional[List[str]] = Field(default=None, alias="outcomes")


class GetEventRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")


class GetEventTypesRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetExternalModelsRequestModel(BaseModel):
    model_endpoint: Optional[str] = Field(default=None, alias="modelEndpoint")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class KMSKeyModel(BaseModel):
    kms_encryption_key_arn: Optional[str] = Field(
        default=None, alias="kmsEncryptionKeyArn"
    )


class GetLabelsRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class LabelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class GetListElementsRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetListsMetadataRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetModelVersionRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")


class GetModelsRequestModel(BaseModel):
    model_id: Optional[str] = Field(default=None, alias="modelId")
    model_type: Optional[
        Literal[
            "ACCOUNT_TAKEOVER_INSIGHTS",
            "ONLINE_FRAUD_INSIGHTS",
            "TRANSACTION_FRAUD_INSIGHTS",
        ]
    ] = Field(default=None, alias="modelType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ModelModel(BaseModel):
    model_id: Optional[str] = Field(default=None, alias="modelId")
    model_type: Optional[
        Literal[
            "ACCOUNT_TAKEOVER_INSIGHTS",
            "ONLINE_FRAUD_INSIGHTS",
            "TRANSACTION_FRAUD_INSIGHTS",
        ]
    ] = Field(default=None, alias="modelType")
    description: Optional[str] = Field(default=None, alias="description")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class GetOutcomesRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class OutcomeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class GetRulesRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    rule_id: Optional[str] = Field(default=None, alias="ruleId")
    rule_version: Optional[str] = Field(default=None, alias="ruleVersion")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RuleDetailModel(BaseModel):
    rule_id: Optional[str] = Field(default=None, alias="ruleId")
    description: Optional[str] = Field(default=None, alias="description")
    detector_id: Optional[str] = Field(default=None, alias="detectorId")
    rule_version: Optional[str] = Field(default=None, alias="ruleVersion")
    expression: Optional[str] = Field(default=None, alias="expression")
    language: Optional[Literal["DETECTORPL"]] = Field(default=None, alias="language")
    outcomes: Optional[List[str]] = Field(default=None, alias="outcomes")
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class GetVariablesRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class IngestedEventsTimeWindowModel(BaseModel):
    start_time: str = Field(alias="startTime")
    end_time: str = Field(alias="endTime")


class LabelSchemaModel(BaseModel):
    label_mapper: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="labelMapper"
    )
    unlabeled_events_treatment: Optional[
        Literal["AUTO", "FRAUD", "IGNORE", "LEGIT"]
    ] = Field(default=None, alias="unlabeledEventsTreatment")


class PredictionTimeRangeModel(BaseModel):
    start_time: str = Field(alias="startTime")
    end_time: str = Field(alias="endTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class LogOddsMetricModel(BaseModel):
    variable_name: str = Field(alias="variableName")
    variable_type: str = Field(alias="variableType")
    variable_importance: float = Field(alias="variableImportance")


class MetricDataPointModel(BaseModel):
    fpr: Optional[float] = Field(default=None, alias="fpr")
    precision: Optional[float] = Field(default=None, alias="precision")
    tpr: Optional[float] = Field(default=None, alias="tpr")
    threshold: Optional[float] = Field(default=None, alias="threshold")


class OFIMetricDataPointModel(BaseModel):
    fpr: Optional[float] = Field(default=None, alias="fpr")
    precision: Optional[float] = Field(default=None, alias="precision")
    tpr: Optional[float] = Field(default=None, alias="tpr")
    threshold: Optional[float] = Field(default=None, alias="threshold")


class UncertaintyRangeModel(BaseModel):
    lower_bound_value: float = Field(alias="lowerBoundValue")
    upper_bound_value: float = Field(alias="upperBoundValue")


class VariableImpactExplanationModel(BaseModel):
    event_variable_name: Optional[str] = Field(default=None, alias="eventVariableName")
    relative_impact: Optional[str] = Field(default=None, alias="relativeImpact")
    log_odds_impact: Optional[float] = Field(default=None, alias="logOddsImpact")


class PutKMSEncryptionKeyRequestModel(BaseModel):
    kms_encryption_key_arn: str = Field(alias="kmsEncryptionKeyArn")


class TFIMetricDataPointModel(BaseModel):
    fpr: Optional[float] = Field(default=None, alias="fpr")
    precision: Optional[float] = Field(default=None, alias="precision")
    tpr: Optional[float] = Field(default=None, alias="tpr")
    threshold: Optional[float] = Field(default=None, alias="threshold")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateDetectorVersionMetadataRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    description: str = Field(alias="description")


class UpdateDetectorVersionStatusRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    status: Literal["ACTIVE", "DRAFT", "INACTIVE"] = Field(alias="status")


class UpdateEventLabelRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    assigned_label: str = Field(alias="assignedLabel")
    label_timestamp: str = Field(alias="labelTimestamp")


class UpdateListRequestModel(BaseModel):
    name: str = Field(alias="name")
    elements: Optional[Sequence[str]] = Field(default=None, alias="elements")
    description: Optional[str] = Field(default=None, alias="description")
    update_mode: Optional[Literal["APPEND", "REMOVE", "REPLACE"]] = Field(
        default=None, alias="updateMode"
    )
    variable_type: Optional[str] = Field(default=None, alias="variableType")


class UpdateModelRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateModelVersionStatusRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")
    status: Literal["ACTIVE", "INACTIVE", "TRAINING_CANCELLED"] = Field(alias="status")


class UpdateVariableRequestModel(BaseModel):
    name: str = Field(alias="name")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    description: Optional[str] = Field(default=None, alias="description")
    variable_type: Optional[str] = Field(default=None, alias="variableType")


class ATITrainingMetricsValueModel(BaseModel):
    metric_data_points: Optional[List[ATIMetricDataPointModel]] = Field(
        default=None, alias="metricDataPoints"
    )
    model_performance: Optional[ATIModelPerformanceModel] = Field(
        default=None, alias="modelPerformance"
    )


class AggregatedVariablesImportanceMetricsModel(BaseModel):
    log_odds_metrics: Optional[List[AggregatedLogOddsMetricModel]] = Field(
        default=None, alias="logOddsMetrics"
    )


class CreateBatchImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    input_path: str = Field(alias="inputPath")
    output_path: str = Field(alias="outputPath")
    event_type_name: str = Field(alias="eventTypeName")
    iam_role_arn: str = Field(alias="iamRoleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateBatchPredictionJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    input_path: str = Field(alias="inputPath")
    output_path: str = Field(alias="outputPath")
    event_type_name: str = Field(alias="eventTypeName")
    detector_name: str = Field(alias="detectorName")
    iam_role_arn: str = Field(alias="iamRoleArn")
    detector_version: Optional[str] = Field(default=None, alias="detectorVersion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateListRequestModel(BaseModel):
    name: str = Field(alias="name")
    elements: Optional[Sequence[str]] = Field(default=None, alias="elements")
    variable_type: Optional[str] = Field(default=None, alias="variableType")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateModelRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    event_type_name: str = Field(alias="eventTypeName")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="ruleId")
    detector_id: str = Field(alias="detectorId")
    expression: str = Field(alias="expression")
    language: Literal["DETECTORPL"] = Field(alias="language")
    outcomes: Sequence[str] = Field(alias="outcomes")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateVariableRequestModel(BaseModel):
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "FLOAT", "INTEGER", "STRING"] = Field(
        alias="dataType"
    )
    data_source: Literal["EVENT", "EXTERNAL_MODEL_SCORE", "MODEL_SCORE"] = Field(
        alias="dataSource"
    )
    default_value: str = Field(alias="defaultValue")
    description: Optional[str] = Field(default=None, alias="description")
    variable_type: Optional[str] = Field(default=None, alias="variableType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    event_type_name: str = Field(alias="eventTypeName")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutEntityTypeRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutEventTypeRequestModel(BaseModel):
    name: str = Field(alias="name")
    event_variables: Sequence[str] = Field(alias="eventVariables")
    entity_types: Sequence[str] = Field(alias="entityTypes")
    description: Optional[str] = Field(default=None, alias="description")
    labels: Optional[Sequence[str]] = Field(default=None, alias="labels")
    event_ingestion: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="eventIngestion"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutLabelRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutOutcomeRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tags: Sequence[TagModel] = Field(alias="tags")


class BatchCreateVariableRequestModel(BaseModel):
    variable_entries: Sequence[VariableEntryModel] = Field(alias="variableEntries")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class BatchCreateVariableResultModel(BaseModel):
    errors: List[BatchCreateVariableErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDetectorVersionResultModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    status: Literal["ACTIVE", "DRAFT", "INACTIVE"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelVersionResultModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")
    status: str = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventsByEventTypeResultModel(BaseModel):
    event_type_name: str = Field(alias="eventTypeName")
    events_deletion_status: str = Field(alias="eventsDeletionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeleteEventsByEventTypeStatusResultModel(BaseModel):
    event_type_name: str = Field(alias="eventTypeName")
    events_deletion_status: Literal[
        "CANCELED",
        "CANCEL_IN_PROGRESS",
        "COMPLETE",
        "FAILED",
        "IN_PROGRESS",
        "IN_PROGRESS_INITIALIZING",
    ] = Field(alias="eventsDeletionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetListElementsResultModel(BaseModel):
    elements: List[str] = Field(alias="elements")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetListsMetadataResultModel(BaseModel):
    lists: List[AllowDenyListModel] = Field(alias="lists")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelVersionResultModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")
    status: str = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetVariableResultModel(BaseModel):
    variables: List[VariableModel] = Field(alias="variables")
    errors: List[BatchGetVariableErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVariablesResultModel(BaseModel):
    variables: List[VariableModel] = Field(alias="variables")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBatchImportJobsResultModel(BaseModel):
    batch_imports: List[BatchImportModel] = Field(alias="batchImports")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBatchPredictionJobsResultModel(BaseModel):
    batch_predictions: List[BatchPredictionModel] = Field(alias="batchPredictions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelScoresModel(BaseModel):
    model_version: Optional[ModelVersionModel] = Field(
        default=None, alias="modelVersion"
    )
    scores: Optional[Dict[str, float]] = Field(default=None, alias="scores")


class CreateDetectorVersionRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    rules: Sequence[RuleModel] = Field(alias="rules")
    description: Optional[str] = Field(default=None, alias="description")
    external_model_endpoints: Optional[Sequence[str]] = Field(
        default=None, alias="externalModelEndpoints"
    )
    model_versions: Optional[Sequence[ModelVersionModel]] = Field(
        default=None, alias="modelVersions"
    )
    rule_execution_mode: Optional[Literal["ALL_MATCHED", "FIRST_MATCHED"]] = Field(
        default=None, alias="ruleExecutionMode"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRuleResultModel(BaseModel):
    rule: RuleModel = Field(alias="rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRuleRequestModel(BaseModel):
    rule: RuleModel = Field(alias="rule")


class GetDetectorVersionResultModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    description: str = Field(alias="description")
    external_model_endpoints: List[str] = Field(alias="externalModelEndpoints")
    model_versions: List[ModelVersionModel] = Field(alias="modelVersions")
    rules: List[RuleModel] = Field(alias="rules")
    status: Literal["ACTIVE", "DRAFT", "INACTIVE"] = Field(alias="status")
    last_updated_time: str = Field(alias="lastUpdatedTime")
    created_time: str = Field(alias="createdTime")
    rule_execution_mode: Literal["ALL_MATCHED", "FIRST_MATCHED"] = Field(
        alias="ruleExecutionMode"
    )
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDetectorVersionRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    external_model_endpoints: Sequence[str] = Field(alias="externalModelEndpoints")
    rules: Sequence[RuleModel] = Field(alias="rules")
    description: Optional[str] = Field(default=None, alias="description")
    model_versions: Optional[Sequence[ModelVersionModel]] = Field(
        default=None, alias="modelVersions"
    )
    rule_execution_mode: Optional[Literal["ALL_MATCHED", "FIRST_MATCHED"]] = Field(
        default=None, alias="ruleExecutionMode"
    )


class UpdateRuleMetadataRequestModel(BaseModel):
    rule: RuleModel = Field(alias="rule")
    description: str = Field(alias="description")


class UpdateRuleVersionRequestModel(BaseModel):
    rule: RuleModel = Field(alias="rule")
    expression: str = Field(alias="expression")
    language: Literal["DETECTORPL"] = Field(alias="language")
    outcomes: Sequence[str] = Field(alias="outcomes")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateRuleVersionResultModel(BaseModel):
    rule: RuleModel = Field(alias="rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataValidationMetricsModel(BaseModel):
    file_level_messages: Optional[List[FileValidationMessageModel]] = Field(
        default=None, alias="fileLevelMessages"
    )
    field_level_messages: Optional[List[FieldValidationMessageModel]] = Field(
        default=None, alias="fieldLevelMessages"
    )


class DescribeDetectorResultModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    detector_version_summaries: List[DetectorVersionSummaryModel] = Field(
        alias="detectorVersionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDetectorsResultModel(BaseModel):
    detectors: List[DetectorModel] = Field(alias="detectors")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="eventId")
    event_type_name: Optional[str] = Field(default=None, alias="eventTypeName")
    event_timestamp: Optional[str] = Field(default=None, alias="eventTimestamp")
    event_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="eventVariables"
    )
    current_label: Optional[str] = Field(default=None, alias="currentLabel")
    label_timestamp: Optional[str] = Field(default=None, alias="labelTimestamp")
    entities: Optional[List[EntityModel]] = Field(default=None, alias="entities")


class SendEventRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    event_timestamp: str = Field(alias="eventTimestamp")
    event_variables: Mapping[str, str] = Field(alias="eventVariables")
    entities: Sequence[EntityModel] = Field(alias="entities")
    assigned_label: Optional[str] = Field(default=None, alias="assignedLabel")
    label_timestamp: Optional[str] = Field(default=None, alias="labelTimestamp")


class GetEntityTypesResultModel(BaseModel):
    entity_types: List[EntityTypeModel] = Field(alias="entityTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventPredictionsResultModel(BaseModel):
    event_prediction_summaries: List[EventPredictionSummaryModel] = Field(
        alias="eventPredictionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventTypeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    event_variables: Optional[List[str]] = Field(default=None, alias="eventVariables")
    labels: Optional[List[str]] = Field(default=None, alias="labels")
    entity_types: Optional[List[str]] = Field(default=None, alias="entityTypes")
    event_ingestion: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="eventIngestion"
    )
    ingested_event_statistics: Optional[IngestedEventStatisticsModel] = Field(
        default=None, alias="ingestedEventStatistics"
    )
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class ExternalModelOutputsModel(BaseModel):
    external_model: Optional[ExternalModelSummaryModel] = Field(
        default=None, alias="externalModel"
    )
    outputs: Optional[Dict[str, str]] = Field(default=None, alias="outputs")


class ExternalModelModel(BaseModel):
    model_endpoint: Optional[str] = Field(default=None, alias="modelEndpoint")
    model_source: Optional[Literal["SAGEMAKER"]] = Field(
        default=None, alias="modelSource"
    )
    invoke_model_endpoint_role_arn: Optional[str] = Field(
        default=None, alias="invokeModelEndpointRoleArn"
    )
    input_configuration: Optional[ModelInputConfigurationModel] = Field(
        default=None, alias="inputConfiguration"
    )
    output_configuration: Optional[ModelOutputConfigurationModel] = Field(
        default=None, alias="outputConfiguration"
    )
    model_endpoint_status: Optional[Literal["ASSOCIATED", "DISSOCIATED"]] = Field(
        default=None, alias="modelEndpointStatus"
    )
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")


class PutExternalModelRequestModel(BaseModel):
    model_endpoint: str = Field(alias="modelEndpoint")
    model_source: Literal["SAGEMAKER"] = Field(alias="modelSource")
    invoke_model_endpoint_role_arn: str = Field(alias="invokeModelEndpointRoleArn")
    input_configuration: ModelInputConfigurationModel = Field(
        alias="inputConfiguration"
    )
    output_configuration: ModelOutputConfigurationModel = Field(
        alias="outputConfiguration"
    )
    model_endpoint_status: Literal["ASSOCIATED", "DISSOCIATED"] = Field(
        alias="modelEndpointStatus"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetEventPredictionRequestModel(BaseModel):
    detector_id: str = Field(alias="detectorId")
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    entities: Sequence[EntityModel] = Field(alias="entities")
    event_timestamp: str = Field(alias="eventTimestamp")
    event_variables: Mapping[str, str] = Field(alias="eventVariables")
    detector_version_id: Optional[str] = Field(default=None, alias="detectorVersionId")
    external_model_endpoint_data_blobs: Optional[
        Mapping[str, ModelEndpointDataBlobModel]
    ] = Field(default=None, alias="externalModelEndpointDataBlobs")


class GetKMSEncryptionKeyResultModel(BaseModel):
    kms_key: KMSKeyModel = Field(alias="kmsKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLabelsResultModel(BaseModel):
    labels: List[LabelModel] = Field(alias="labels")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelsResultModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    models: List[ModelModel] = Field(alias="models")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOutcomesResultModel(BaseModel):
    outcomes: List[OutcomeModel] = Field(alias="outcomes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRulesResultModel(BaseModel):
    rule_details: List[RuleDetailModel] = Field(alias="ruleDetails")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IngestedEventsDetailModel(BaseModel):
    ingested_events_time_window: IngestedEventsTimeWindowModel = Field(
        alias="ingestedEventsTimeWindow"
    )


class TrainingDataSchemaModel(BaseModel):
    model_variables: Sequence[str] = Field(alias="modelVariables")
    label_schema: Optional[LabelSchemaModel] = Field(default=None, alias="labelSchema")


class ListEventPredictionsRequestModel(BaseModel):
    event_id: Optional[FilterConditionModel] = Field(default=None, alias="eventId")
    event_type: Optional[FilterConditionModel] = Field(default=None, alias="eventType")
    detector_id: Optional[FilterConditionModel] = Field(
        default=None, alias="detectorId"
    )
    detector_version_id: Optional[FilterConditionModel] = Field(
        default=None, alias="detectorVersionId"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="predictionTimeRange"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class VariableImportanceMetricsModel(BaseModel):
    log_odds_metrics: Optional[List[LogOddsMetricModel]] = Field(
        default=None, alias="logOddsMetrics"
    )


class TrainingMetricsModel(BaseModel):
    auc: Optional[float] = Field(default=None, alias="auc")
    metric_data_points: Optional[List[MetricDataPointModel]] = Field(
        default=None, alias="metricDataPoints"
    )


class OFIModelPerformanceModel(BaseModel):
    auc: Optional[float] = Field(default=None, alias="auc")
    uncertainty_range: Optional[UncertaintyRangeModel] = Field(
        default=None, alias="uncertaintyRange"
    )


class TFIModelPerformanceModel(BaseModel):
    auc: Optional[float] = Field(default=None, alias="auc")
    uncertainty_range: Optional[UncertaintyRangeModel] = Field(
        default=None, alias="uncertaintyRange"
    )


class PredictionExplanationsModel(BaseModel):
    variable_impact_explanations: Optional[
        List[VariableImpactExplanationModel]
    ] = Field(default=None, alias="variableImpactExplanations")
    aggregated_variables_impact_explanations: Optional[
        List[AggregatedVariablesImpactExplanationModel]
    ] = Field(default=None, alias="aggregatedVariablesImpactExplanations")


class GetEventResultModel(BaseModel):
    event: EventModel = Field(alias="event")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEventTypesResultModel(BaseModel):
    event_types: List[EventTypeModel] = Field(alias="eventTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEventPredictionResultModel(BaseModel):
    model_scores: List[ModelScoresModel] = Field(alias="modelScores")
    rule_results: List[RuleResultModel] = Field(alias="ruleResults")
    external_model_outputs: List[ExternalModelOutputsModel] = Field(
        alias="externalModelOutputs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExternalModelsResultModel(BaseModel):
    external_models: List[ExternalModelModel] = Field(alias="externalModels")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelVersionRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    major_version_number: str = Field(alias="majorVersionNumber")
    external_events_detail: Optional[ExternalEventsDetailModel] = Field(
        default=None, alias="externalEventsDetail"
    )
    ingested_events_detail: Optional[IngestedEventsDetailModel] = Field(
        default=None, alias="ingestedEventsDetail"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateModelVersionRequestModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    training_data_source: Literal["EXTERNAL_EVENTS", "INGESTED_EVENTS"] = Field(
        alias="trainingDataSource"
    )
    training_data_schema: TrainingDataSchemaModel = Field(alias="trainingDataSchema")
    external_events_detail: Optional[ExternalEventsDetailModel] = Field(
        default=None, alias="externalEventsDetail"
    )
    ingested_events_detail: Optional[IngestedEventsDetailModel] = Field(
        default=None, alias="ingestedEventsDetail"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetModelVersionResultModel(BaseModel):
    model_id: str = Field(alias="modelId")
    model_type: Literal[
        "ACCOUNT_TAKEOVER_INSIGHTS",
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
    ] = Field(alias="modelType")
    model_version_number: str = Field(alias="modelVersionNumber")
    training_data_source: Literal["EXTERNAL_EVENTS", "INGESTED_EVENTS"] = Field(
        alias="trainingDataSource"
    )
    training_data_schema: TrainingDataSchemaModel = Field(alias="trainingDataSchema")
    external_events_detail: ExternalEventsDetailModel = Field(
        alias="externalEventsDetail"
    )
    ingested_events_detail: IngestedEventsDetailModel = Field(
        alias="ingestedEventsDetail"
    )
    status: str = Field(alias="status")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrainingResultModel(BaseModel):
    data_validation_metrics: Optional[DataValidationMetricsModel] = Field(
        default=None, alias="dataValidationMetrics"
    )
    training_metrics: Optional[TrainingMetricsModel] = Field(
        default=None, alias="trainingMetrics"
    )
    variable_importance_metrics: Optional[VariableImportanceMetricsModel] = Field(
        default=None, alias="variableImportanceMetrics"
    )


class OFITrainingMetricsValueModel(BaseModel):
    metric_data_points: Optional[List[OFIMetricDataPointModel]] = Field(
        default=None, alias="metricDataPoints"
    )
    model_performance: Optional[OFIModelPerformanceModel] = Field(
        default=None, alias="modelPerformance"
    )


class TFITrainingMetricsValueModel(BaseModel):
    metric_data_points: Optional[List[TFIMetricDataPointModel]] = Field(
        default=None, alias="metricDataPoints"
    )
    model_performance: Optional[TFIModelPerformanceModel] = Field(
        default=None, alias="modelPerformance"
    )


class ModelVersionEvaluationModel(BaseModel):
    output_variable_name: Optional[str] = Field(
        default=None, alias="outputVariableName"
    )
    evaluation_score: Optional[str] = Field(default=None, alias="evaluationScore")
    prediction_explanations: Optional[PredictionExplanationsModel] = Field(
        default=None, alias="predictionExplanations"
    )


class TrainingMetricsV2Model(BaseModel):
    ofi: Optional[OFITrainingMetricsValueModel] = Field(default=None, alias="ofi")
    tfi: Optional[TFITrainingMetricsValueModel] = Field(default=None, alias="tfi")
    ati: Optional[ATITrainingMetricsValueModel] = Field(default=None, alias="ati")


class EvaluatedModelVersionModel(BaseModel):
    model_id: Optional[str] = Field(default=None, alias="modelId")
    model_version: Optional[str] = Field(default=None, alias="modelVersion")
    model_type: Optional[str] = Field(default=None, alias="modelType")
    evaluations: Optional[List[ModelVersionEvaluationModel]] = Field(
        default=None, alias="evaluations"
    )


class TrainingResultV2Model(BaseModel):
    data_validation_metrics: Optional[DataValidationMetricsModel] = Field(
        default=None, alias="dataValidationMetrics"
    )
    training_metrics_v2: Optional[TrainingMetricsV2Model] = Field(
        default=None, alias="trainingMetricsV2"
    )
    variable_importance_metrics: Optional[VariableImportanceMetricsModel] = Field(
        default=None, alias="variableImportanceMetrics"
    )
    aggregated_variables_importance_metrics: Optional[
        AggregatedVariablesImportanceMetricsModel
    ] = Field(default=None, alias="aggregatedVariablesImportanceMetrics")


class GetEventPredictionMetadataResultModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_type_name: str = Field(alias="eventTypeName")
    entity_id: str = Field(alias="entityId")
    entity_type: str = Field(alias="entityType")
    event_timestamp: str = Field(alias="eventTimestamp")
    detector_id: str = Field(alias="detectorId")
    detector_version_id: str = Field(alias="detectorVersionId")
    detector_version_status: str = Field(alias="detectorVersionStatus")
    event_variables: List[EventVariableSummaryModel] = Field(alias="eventVariables")
    rules: List[EvaluatedRuleModel] = Field(alias="rules")
    rule_execution_mode: Literal["ALL_MATCHED", "FIRST_MATCHED"] = Field(
        alias="ruleExecutionMode"
    )
    outcomes: List[str] = Field(alias="outcomes")
    evaluated_model_versions: List[EvaluatedModelVersionModel] = Field(
        alias="evaluatedModelVersions"
    )
    evaluated_external_models: List[EvaluatedExternalModelModel] = Field(
        alias="evaluatedExternalModels"
    )
    prediction_timestamp: str = Field(alias="predictionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelVersionDetailModel(BaseModel):
    model_id: Optional[str] = Field(default=None, alias="modelId")
    model_type: Optional[
        Literal[
            "ACCOUNT_TAKEOVER_INSIGHTS",
            "ONLINE_FRAUD_INSIGHTS",
            "TRANSACTION_FRAUD_INSIGHTS",
        ]
    ] = Field(default=None, alias="modelType")
    model_version_number: Optional[str] = Field(
        default=None, alias="modelVersionNumber"
    )
    status: Optional[str] = Field(default=None, alias="status")
    training_data_source: Optional[
        Literal["EXTERNAL_EVENTS", "INGESTED_EVENTS"]
    ] = Field(default=None, alias="trainingDataSource")
    training_data_schema: Optional[TrainingDataSchemaModel] = Field(
        default=None, alias="trainingDataSchema"
    )
    external_events_detail: Optional[ExternalEventsDetailModel] = Field(
        default=None, alias="externalEventsDetail"
    )
    ingested_events_detail: Optional[IngestedEventsDetailModel] = Field(
        default=None, alias="ingestedEventsDetail"
    )
    training_result: Optional[TrainingResultModel] = Field(
        default=None, alias="trainingResult"
    )
    last_updated_time: Optional[str] = Field(default=None, alias="lastUpdatedTime")
    created_time: Optional[str] = Field(default=None, alias="createdTime")
    arn: Optional[str] = Field(default=None, alias="arn")
    training_result_v2: Optional[TrainingResultV2Model] = Field(
        default=None, alias="trainingResultV2"
    )


class DescribeModelVersionsResultModel(BaseModel):
    model_version_details: List[ModelVersionDetailModel] = Field(
        alias="modelVersionDetails"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
