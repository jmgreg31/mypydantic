# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CategoricalValuesModel(BaseModel):
    status: Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"] = Field(
        alias="Status"
    )
    number_of_category: Optional[int] = Field(default=None, alias="NumberOfCategory")


class CountPercentModel(BaseModel):
    count: int = Field(alias="Count")
    percentage: float = Field(alias="Percentage")


class DatasetSchemaModel(BaseModel):
    inline_data_schema: Optional[str] = Field(default=None, alias="InlineDataSchema")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLabelRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    rating: Literal["ANOMALY", "NEUTRAL", "NO_ANOMALY"] = Field(alias="Rating")
    client_token: str = Field(alias="ClientToken")
    fault_code: Optional[str] = Field(default=None, alias="FaultCode")
    notes: Optional[str] = Field(default=None, alias="Notes")
    equipment: Optional[str] = Field(default=None, alias="Equipment")


class DataPreProcessingConfigurationModel(BaseModel):
    target_sampling_rate: Optional[
        Literal[
            "PT10M",
            "PT10S",
            "PT15M",
            "PT15S",
            "PT1H",
            "PT1M",
            "PT1S",
            "PT30M",
            "PT30S",
            "PT5M",
            "PT5S",
        ]
    ] = Field(default=None, alias="TargetSamplingRate")


class DuplicateTimestampsModel(BaseModel):
    total_number_of_duplicate_timestamps: int = Field(
        alias="TotalNumberOfDuplicateTimestamps"
    )


class InvalidSensorDataModel(BaseModel):
    affected_sensor_count: int = Field(alias="AffectedSensorCount")
    total_number_of_invalid_values: int = Field(alias="TotalNumberOfInvalidValues")


class MissingSensorDataModel(BaseModel):
    affected_sensor_count: int = Field(alias="AffectedSensorCount")
    total_number_of_missing_values: int = Field(alias="TotalNumberOfMissingValues")


class UnsupportedTimestampsModel(BaseModel):
    total_number_of_unsupported_timestamps: int = Field(
        alias="TotalNumberOfUnsupportedTimestamps"
    )


class DatasetSummaryModel(BaseModel):
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    status: Optional[Literal["ACTIVE", "CREATED", "INGESTION_IN_PROGRESS"]] = Field(
        default=None, alias="Status"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class DeleteDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")


class DeleteInferenceSchedulerRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")


class DeleteLabelGroupRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")


class DeleteLabelRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    label_id: str = Field(alias="LabelId")


class DeleteModelRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class DescribeDataIngestionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")


class DescribeInferenceSchedulerRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")


class DescribeLabelGroupRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")


class DescribeLabelRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    label_id: str = Field(alias="LabelId")


class DescribeModelRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class InferenceEventSummaryModel(BaseModel):
    inference_scheduler_arn: Optional[str] = Field(
        default=None, alias="InferenceSchedulerArn"
    )
    inference_scheduler_name: Optional[str] = Field(
        default=None, alias="InferenceSchedulerName"
    )
    event_start_time: Optional[datetime] = Field(default=None, alias="EventStartTime")
    event_end_time: Optional[datetime] = Field(default=None, alias="EventEndTime")
    diagnostics: Optional[str] = Field(default=None, alias="Diagnostics")
    event_duration_in_seconds: Optional[int] = Field(
        default=None, alias="EventDurationInSeconds"
    )


class S3ObjectModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")


class InferenceInputNameConfigurationModel(BaseModel):
    timestamp_format: Optional[str] = Field(default=None, alias="TimestampFormat")
    component_timestamp_delimiter: Optional[str] = Field(
        default=None, alias="ComponentTimestampDelimiter"
    )


class InferenceS3InputConfigurationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class InferenceS3OutputConfigurationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class InferenceSchedulerSummaryModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    inference_scheduler_name: Optional[str] = Field(
        default=None, alias="InferenceSchedulerName"
    )
    inference_scheduler_arn: Optional[str] = Field(
        default=None, alias="InferenceSchedulerArn"
    )
    status: Optional[Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]] = Field(
        default=None, alias="Status"
    )
    data_delay_offset_in_minutes: Optional[int] = Field(
        default=None, alias="DataDelayOffsetInMinutes"
    )
    data_upload_frequency: Optional[
        Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"]
    ] = Field(default=None, alias="DataUploadFrequency")
    latest_inference_result: Optional[Literal["ANOMALOUS", "NORMAL"]] = Field(
        default=None, alias="LatestInferenceResult"
    )


class IngestionS3InputConfigurationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    key_pattern: Optional[str] = Field(default=None, alias="KeyPattern")


class MissingCompleteSensorDataModel(BaseModel):
    affected_sensor_count: int = Field(alias="AffectedSensorCount")


class SensorsWithShortDateRangeModel(BaseModel):
    affected_sensor_count: int = Field(alias="AffectedSensorCount")


class LabelGroupSummaryModel(BaseModel):
    label_group_name: Optional[str] = Field(default=None, alias="LabelGroupName")
    label_group_arn: Optional[str] = Field(default=None, alias="LabelGroupArn")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class LabelSummaryModel(BaseModel):
    label_group_name: Optional[str] = Field(default=None, alias="LabelGroupName")
    label_id: Optional[str] = Field(default=None, alias="LabelId")
    label_group_arn: Optional[str] = Field(default=None, alias="LabelGroupArn")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    rating: Optional[Literal["ANOMALY", "NEUTRAL", "NO_ANOMALY"]] = Field(
        default=None, alias="Rating"
    )
    fault_code: Optional[str] = Field(default=None, alias="FaultCode")
    equipment: Optional[str] = Field(default=None, alias="Equipment")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class LabelsS3InputConfigurationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class LargeTimestampGapsModel(BaseModel):
    status: Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"] = Field(
        alias="Status"
    )
    number_of_large_timestamp_gaps: Optional[int] = Field(
        default=None, alias="NumberOfLargeTimestampGaps"
    )
    max_timestamp_gap_in_days: Optional[int] = Field(
        default=None, alias="MaxTimestampGapInDays"
    )


class ListDataIngestionJobsRequestModel(BaseModel):
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class ListDatasetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    dataset_name_begins_with: Optional[str] = Field(
        default=None, alias="DatasetNameBeginsWith"
    )


class ListInferenceEventsRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    interval_start_time: Union[datetime, str] = Field(alias="IntervalStartTime")
    interval_end_time: Union[datetime, str] = Field(alias="IntervalEndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInferenceExecutionsRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    data_start_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="DataStartTimeAfter"
    )
    data_end_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="DataEndTimeBefore"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class ListInferenceSchedulersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    inference_scheduler_name_begins_with: Optional[str] = Field(
        default=None, alias="InferenceSchedulerNameBeginsWith"
    )
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    status: Optional[Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]] = Field(
        default=None, alias="Status"
    )


class ListLabelGroupsRequestModel(BaseModel):
    label_group_name_begins_with: Optional[str] = Field(
        default=None, alias="LabelGroupNameBeginsWith"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLabelsRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    interval_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="IntervalStartTime"
    )
    interval_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="IntervalEndTime"
    )
    fault_code: Optional[str] = Field(default=None, alias="FaultCode")
    equipment: Optional[str] = Field(default=None, alias="Equipment")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListModelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    model_name_begins_with: Optional[str] = Field(
        default=None, alias="ModelNameBeginsWith"
    )
    dataset_name_begins_with: Optional[str] = Field(
        default=None, alias="DatasetNameBeginsWith"
    )


class ModelSummaryModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class ListSensorStatisticsRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    ingestion_job_id: Optional[str] = Field(default=None, alias="IngestionJobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class MonotonicValuesModel(BaseModel):
    status: Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"] = Field(
        alias="Status"
    )
    monotonicity: Optional[Literal["DECREASING", "INCREASING", "STATIC"]] = Field(
        default=None, alias="Monotonicity"
    )


class MultipleOperatingModesModel(BaseModel):
    status: Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"] = Field(
        alias="Status"
    )


class StartInferenceSchedulerRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")


class StopInferenceSchedulerRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateLabelGroupRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    fault_codes: Optional[Sequence[str]] = Field(default=None, alias="FaultCodes")


class CreateDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    client_token: str = Field(alias="ClientToken")
    dataset_schema: Optional[DatasetSchemaModel] = Field(
        default=None, alias="DatasetSchema"
    )
    server_side_kms_key_id: Optional[str] = Field(
        default=None, alias="ServerSideKmsKeyId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateLabelGroupRequestModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    client_token: str = Field(alias="ClientToken")
    fault_codes: Optional[Sequence[str]] = Field(default=None, alias="FaultCodes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateDatasetResponseModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    dataset_arn: str = Field(alias="DatasetArn")
    status: Literal["ACTIVE", "CREATED", "INGESTION_IN_PROGRESS"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInferenceSchedulerResponseModel(BaseModel):
    inference_scheduler_arn: str = Field(alias="InferenceSchedulerArn")
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    status: Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLabelGroupResponseModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    label_group_arn: str = Field(alias="LabelGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLabelResponseModel(BaseModel):
    label_id: str = Field(alias="LabelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESS"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLabelGroupResponseModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    label_group_arn: str = Field(alias="LabelGroupArn")
    fault_codes: List[str] = Field(alias="FaultCodes")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLabelResponseModel(BaseModel):
    label_group_name: str = Field(alias="LabelGroupName")
    label_group_arn: str = Field(alias="LabelGroupArn")
    label_id: str = Field(alias="LabelId")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    rating: Literal["ANOMALY", "NEUTRAL", "NO_ANOMALY"] = Field(alias="Rating")
    fault_code: str = Field(alias="FaultCode")
    notes: str = Field(alias="Notes")
    equipment: str = Field(alias="Equipment")
    created_at: datetime = Field(alias="CreatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataIngestionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESS"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartInferenceSchedulerResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    model_name: str = Field(alias="ModelName")
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    inference_scheduler_arn: str = Field(alias="InferenceSchedulerArn")
    status: Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopInferenceSchedulerResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    model_name: str = Field(alias="ModelName")
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    inference_scheduler_arn: str = Field(alias="InferenceSchedulerArn")
    status: Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    dataset_summaries: List[DatasetSummaryModel] = Field(alias="DatasetSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInferenceEventsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    inference_event_summaries: List[InferenceEventSummaryModel] = Field(
        alias="InferenceEventSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IngestedFilesSummaryModel(BaseModel):
    total_number_of_files: int = Field(alias="TotalNumberOfFiles")
    ingested_number_of_files: int = Field(alias="IngestedNumberOfFiles")
    discarded_files: Optional[List[S3ObjectModel]] = Field(
        default=None, alias="DiscardedFiles"
    )


class InferenceInputConfigurationModel(BaseModel):
    s3_input_configuration: Optional[InferenceS3InputConfigurationModel] = Field(
        default=None, alias="S3InputConfiguration"
    )
    input_time_zone_offset: Optional[str] = Field(
        default=None, alias="InputTimeZoneOffset"
    )
    inference_input_name_configuration: Optional[
        InferenceInputNameConfigurationModel
    ] = Field(default=None, alias="InferenceInputNameConfiguration")


class InferenceOutputConfigurationModel(BaseModel):
    s3_output_configuration: InferenceS3OutputConfigurationModel = Field(
        alias="S3OutputConfiguration"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ListInferenceSchedulersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    inference_scheduler_summaries: List[InferenceSchedulerSummaryModel] = Field(
        alias="InferenceSchedulerSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IngestionInputConfigurationModel(BaseModel):
    s3_input_configuration: IngestionS3InputConfigurationModel = Field(
        alias="S3InputConfiguration"
    )


class InsufficientSensorDataModel(BaseModel):
    missing_complete_sensor_data: MissingCompleteSensorDataModel = Field(
        alias="MissingCompleteSensorData"
    )
    sensors_with_short_date_range: SensorsWithShortDateRangeModel = Field(
        alias="SensorsWithShortDateRange"
    )


class ListLabelGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    label_group_summaries: List[LabelGroupSummaryModel] = Field(
        alias="LabelGroupSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLabelsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    label_summaries: List[LabelSummaryModel] = Field(alias="LabelSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LabelsInputConfigurationModel(BaseModel):
    s3_input_configuration: Optional[LabelsS3InputConfigurationModel] = Field(
        default=None, alias="S3InputConfiguration"
    )
    label_group_name: Optional[str] = Field(default=None, alias="LabelGroupName")


class ListModelsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    model_summaries: List[ModelSummaryModel] = Field(alias="ModelSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SensorStatisticsSummaryModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="ComponentName")
    sensor_name: Optional[str] = Field(default=None, alias="SensorName")
    data_exists: Optional[bool] = Field(default=None, alias="DataExists")
    missing_values: Optional[CountPercentModel] = Field(
        default=None, alias="MissingValues"
    )
    invalid_values: Optional[CountPercentModel] = Field(
        default=None, alias="InvalidValues"
    )
    invalid_date_entries: Optional[CountPercentModel] = Field(
        default=None, alias="InvalidDateEntries"
    )
    duplicate_timestamps: Optional[CountPercentModel] = Field(
        default=None, alias="DuplicateTimestamps"
    )
    categorical_values: Optional[CategoricalValuesModel] = Field(
        default=None, alias="CategoricalValues"
    )
    multiple_operating_modes: Optional[MultipleOperatingModesModel] = Field(
        default=None, alias="MultipleOperatingModes"
    )
    large_timestamp_gaps: Optional[LargeTimestampGapsModel] = Field(
        default=None, alias="LargeTimestampGaps"
    )
    monotonic_values: Optional[MonotonicValuesModel] = Field(
        default=None, alias="MonotonicValues"
    )
    data_start_time: Optional[datetime] = Field(default=None, alias="DataStartTime")
    data_end_time: Optional[datetime] = Field(default=None, alias="DataEndTime")


class CreateInferenceSchedulerRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    data_upload_frequency: Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"] = Field(
        alias="DataUploadFrequency"
    )
    data_input_configuration: InferenceInputConfigurationModel = Field(
        alias="DataInputConfiguration"
    )
    data_output_configuration: InferenceOutputConfigurationModel = Field(
        alias="DataOutputConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    client_token: str = Field(alias="ClientToken")
    data_delay_offset_in_minutes: Optional[int] = Field(
        default=None, alias="DataDelayOffsetInMinutes"
    )
    server_side_kms_key_id: Optional[str] = Field(
        default=None, alias="ServerSideKmsKeyId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeInferenceSchedulerResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    model_name: str = Field(alias="ModelName")
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    inference_scheduler_arn: str = Field(alias="InferenceSchedulerArn")
    status: Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"] = Field(alias="Status")
    data_delay_offset_in_minutes: int = Field(alias="DataDelayOffsetInMinutes")
    data_upload_frequency: Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"] = Field(
        alias="DataUploadFrequency"
    )
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    data_input_configuration: InferenceInputConfigurationModel = Field(
        alias="DataInputConfiguration"
    )
    data_output_configuration: InferenceOutputConfigurationModel = Field(
        alias="DataOutputConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    server_side_kms_key_id: str = Field(alias="ServerSideKmsKeyId")
    latest_inference_result: Literal["ANOMALOUS", "NORMAL"] = Field(
        alias="LatestInferenceResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InferenceExecutionSummaryModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    inference_scheduler_name: Optional[str] = Field(
        default=None, alias="InferenceSchedulerName"
    )
    inference_scheduler_arn: Optional[str] = Field(
        default=None, alias="InferenceSchedulerArn"
    )
    scheduled_start_time: Optional[datetime] = Field(
        default=None, alias="ScheduledStartTime"
    )
    data_start_time: Optional[datetime] = Field(default=None, alias="DataStartTime")
    data_end_time: Optional[datetime] = Field(default=None, alias="DataEndTime")
    data_input_configuration: Optional[InferenceInputConfigurationModel] = Field(
        default=None, alias="DataInputConfiguration"
    )
    data_output_configuration: Optional[InferenceOutputConfigurationModel] = Field(
        default=None, alias="DataOutputConfiguration"
    )
    customer_result_object: Optional[S3ObjectModel] = Field(
        default=None, alias="CustomerResultObject"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    failed_reason: Optional[str] = Field(default=None, alias="FailedReason")


class UpdateInferenceSchedulerRequestModel(BaseModel):
    inference_scheduler_name: str = Field(alias="InferenceSchedulerName")
    data_delay_offset_in_minutes: Optional[int] = Field(
        default=None, alias="DataDelayOffsetInMinutes"
    )
    data_upload_frequency: Optional[
        Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"]
    ] = Field(default=None, alias="DataUploadFrequency")
    data_input_configuration: Optional[InferenceInputConfigurationModel] = Field(
        default=None, alias="DataInputConfiguration"
    )
    data_output_configuration: Optional[InferenceOutputConfigurationModel] = Field(
        default=None, alias="DataOutputConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class DataIngestionJobSummaryModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    ingestion_input_configuration: Optional[IngestionInputConfigurationModel] = Field(
        default=None, alias="IngestionInputConfiguration"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class StartDataIngestionJobRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    ingestion_input_configuration: IngestionInputConfigurationModel = Field(
        alias="IngestionInputConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    client_token: str = Field(alias="ClientToken")


class DataQualitySummaryModel(BaseModel):
    insufficient_sensor_data: InsufficientSensorDataModel = Field(
        alias="InsufficientSensorData"
    )
    missing_sensor_data: MissingSensorDataModel = Field(alias="MissingSensorData")
    invalid_sensor_data: InvalidSensorDataModel = Field(alias="InvalidSensorData")
    unsupported_timestamps: UnsupportedTimestampsModel = Field(
        alias="UnsupportedTimestamps"
    )
    duplicate_timestamps: DuplicateTimestampsModel = Field(alias="DuplicateTimestamps")


class CreateModelRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    dataset_name: str = Field(alias="DatasetName")
    client_token: str = Field(alias="ClientToken")
    dataset_schema: Optional[DatasetSchemaModel] = Field(
        default=None, alias="DatasetSchema"
    )
    labels_input_configuration: Optional[LabelsInputConfigurationModel] = Field(
        default=None, alias="LabelsInputConfiguration"
    )
    training_data_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="TrainingDataStartTime"
    )
    training_data_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="TrainingDataEndTime"
    )
    evaluation_data_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="EvaluationDataStartTime"
    )
    evaluation_data_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="EvaluationDataEndTime"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    data_pre_processing_configuration: Optional[
        DataPreProcessingConfigurationModel
    ] = Field(default=None, alias="DataPreProcessingConfiguration")
    server_side_kms_key_id: Optional[str] = Field(
        default=None, alias="ServerSideKmsKeyId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    off_condition: Optional[str] = Field(default=None, alias="OffCondition")


class DescribeModelResponseModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    model_arn: str = Field(alias="ModelArn")
    dataset_name: str = Field(alias="DatasetName")
    dataset_arn: str = Field(alias="DatasetArn")
    schema_: str = Field(alias="Schema")
    labels_input_configuration: LabelsInputConfigurationModel = Field(
        alias="LabelsInputConfiguration"
    )
    training_data_start_time: datetime = Field(alias="TrainingDataStartTime")
    training_data_end_time: datetime = Field(alias="TrainingDataEndTime")
    evaluation_data_start_time: datetime = Field(alias="EvaluationDataStartTime")
    evaluation_data_end_time: datetime = Field(alias="EvaluationDataEndTime")
    role_arn: str = Field(alias="RoleArn")
    data_pre_processing_configuration: DataPreProcessingConfigurationModel = Field(
        alias="DataPreProcessingConfiguration"
    )
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESS"] = Field(alias="Status")
    training_execution_start_time: datetime = Field(alias="TrainingExecutionStartTime")
    training_execution_end_time: datetime = Field(alias="TrainingExecutionEndTime")
    failed_reason: str = Field(alias="FailedReason")
    model_metrics: str = Field(alias="ModelMetrics")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    created_at: datetime = Field(alias="CreatedAt")
    server_side_kms_key_id: str = Field(alias="ServerSideKmsKeyId")
    off_condition: str = Field(alias="OffCondition")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSensorStatisticsResponseModel(BaseModel):
    sensor_statistics_summaries: List[SensorStatisticsSummaryModel] = Field(
        alias="SensorStatisticsSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInferenceExecutionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    inference_execution_summaries: List[InferenceExecutionSummaryModel] = Field(
        alias="InferenceExecutionSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataIngestionJobsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    data_ingestion_job_summaries: List[DataIngestionJobSummaryModel] = Field(
        alias="DataIngestionJobSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataIngestionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    dataset_arn: str = Field(alias="DatasetArn")
    ingestion_input_configuration: IngestionInputConfigurationModel = Field(
        alias="IngestionInputConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    created_at: datetime = Field(alias="CreatedAt")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCESS"] = Field(alias="Status")
    failed_reason: str = Field(alias="FailedReason")
    data_quality_summary: DataQualitySummaryModel = Field(alias="DataQualitySummary")
    ingested_files_summary: IngestedFilesSummaryModel = Field(
        alias="IngestedFilesSummary"
    )
    status_detail: str = Field(alias="StatusDetail")
    ingested_data_size: int = Field(alias="IngestedDataSize")
    data_start_time: datetime = Field(alias="DataStartTime")
    data_end_time: datetime = Field(alias="DataEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetResponseModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    dataset_arn: str = Field(alias="DatasetArn")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    status: Literal["ACTIVE", "CREATED", "INGESTION_IN_PROGRESS"] = Field(
        alias="Status"
    )
    schema_: str = Field(alias="Schema")
    server_side_kms_key_id: str = Field(alias="ServerSideKmsKeyId")
    ingestion_input_configuration: IngestionInputConfigurationModel = Field(
        alias="IngestionInputConfiguration"
    )
    data_quality_summary: DataQualitySummaryModel = Field(alias="DataQualitySummary")
    ingested_files_summary: IngestedFilesSummaryModel = Field(
        alias="IngestedFilesSummary"
    )
    role_arn: str = Field(alias="RoleArn")
    data_start_time: datetime = Field(alias="DataStartTime")
    data_end_time: datetime = Field(alias="DataEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
