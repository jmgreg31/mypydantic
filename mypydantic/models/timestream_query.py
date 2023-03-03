# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelQueryRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ColumnInfoModel(BaseModel):
    type: Dict[str, Any] = Field(alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")


class ScheduleConfigurationModel(BaseModel):
    schedule_expression: str = Field(alias="ScheduleExpression")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class RowModel(BaseModel):
    data: List[DatumModel] = Field(alias="Data")


class TimeSeriesDataPointModel(BaseModel):
    time: str = Field(alias="Time")
    value: DatumModel = Field(alias="Value")


class DeleteScheduledQueryRequestModel(BaseModel):
    scheduled_query_arn: str = Field(alias="ScheduledQueryArn")


class EndpointModel(BaseModel):
    address: str = Field(alias="Address")
    cache_period_in_minutes: int = Field(alias="CachePeriodInMinutes")


class DescribeScheduledQueryRequestModel(BaseModel):
    scheduled_query_arn: str = Field(alias="ScheduledQueryArn")


class DimensionMappingModel(BaseModel):
    name: str = Field(alias="Name")
    dimension_value_type: Literal["VARCHAR"] = Field(alias="DimensionValueType")


class S3ConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    object_key_prefix: Optional[str] = Field(default=None, alias="ObjectKeyPrefix")
    encryption_option: Optional[Literal["SSE_KMS", "SSE_S3"]] = Field(
        default=None, alias="EncryptionOption"
    )


class S3ReportLocationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    object_key: Optional[str] = Field(default=None, alias="ObjectKey")


class ExecuteScheduledQueryRequestModel(BaseModel):
    scheduled_query_arn: str = Field(alias="ScheduledQueryArn")
    invocation_time: Union[datetime, str] = Field(alias="InvocationTime")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ExecutionStatsModel(BaseModel):
    execution_time_in_millis: Optional[int] = Field(
        default=None, alias="ExecutionTimeInMillis"
    )
    data_writes: Optional[int] = Field(default=None, alias="DataWrites")
    bytes_metered: Optional[int] = Field(default=None, alias="BytesMetered")
    records_ingested: Optional[int] = Field(default=None, alias="RecordsIngested")
    query_result_rows: Optional[int] = Field(default=None, alias="QueryResultRows")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListScheduledQueriesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MultiMeasureAttributeMappingModel(BaseModel):
    source_column: str = Field(alias="SourceColumn")
    measure_value_type: Literal[
        "BIGINT", "BOOLEAN", "DOUBLE", "TIMESTAMP", "VARCHAR"
    ] = Field(alias="MeasureValueType")
    target_multi_measure_attribute_name: Optional[str] = Field(
        default=None, alias="TargetMultiMeasureAttributeName"
    )


class SnsConfigurationModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class ParameterMappingModel(BaseModel):
    name: str = Field(alias="Name")
    type: TypeModel = Field(alias="Type")


class PrepareQueryRequestModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    validate_only: Optional[bool] = Field(default=None, alias="ValidateOnly")


class SelectColumnModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[TypeModel] = Field(default=None, alias="Type")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    aliased: Optional[bool] = Field(default=None, alias="Aliased")


class QueryRequestModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_rows: Optional[int] = Field(default=None, alias="MaxRows")


class QueryStatusModel(BaseModel):
    progress_percentage: Optional[float] = Field(
        default=None, alias="ProgressPercentage"
    )
    cumulative_bytes_scanned: Optional[int] = Field(
        default=None, alias="CumulativeBytesScanned"
    )
    cumulative_bytes_metered: Optional[int] = Field(
        default=None, alias="CumulativeBytesMetered"
    )


class TimestreamDestinationModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")


class TypeModel(BaseModel):
    scalar_type: Optional[
        Literal[
            "BIGINT",
            "BOOLEAN",
            "DATE",
            "DOUBLE",
            "INTEGER",
            "INTERVAL_DAY_TO_SECOND",
            "INTERVAL_YEAR_TO_MONTH",
            "TIME",
            "TIMESTAMP",
            "UNKNOWN",
            "VARCHAR",
        ]
    ] = Field(default=None, alias="ScalarType")
    array_column_info: Optional[Dict[str, Any]] = Field(
        default=None, alias="ArrayColumnInfo"
    )
    time_series_measure_value_column_info: Optional[Dict[str, Any]] = Field(
        default=None, alias="TimeSeriesMeasureValueColumnInfo"
    )
    row_column_info: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="RowColumnInfo"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateScheduledQueryRequestModel(BaseModel):
    scheduled_query_arn: str = Field(alias="ScheduledQueryArn")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")


class CancelQueryResponseModel(BaseModel):
    cancellation_message: str = Field(alias="CancellationMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduledQueryResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DatumModel(BaseModel):
    scalar_value: Optional[str] = Field(default=None, alias="ScalarValue")
    time_series_value: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="TimeSeriesValue"
    )
    array_value: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="ArrayValue"
    )
    row_value: Optional[Dict[str, Any]] = Field(default=None, alias="RowValue")
    null_value: Optional[bool] = Field(default=None, alias="NullValue")


class DescribeEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ErrorReportConfigurationModel(BaseModel):
    s3_configuration: S3ConfigurationModel = Field(alias="S3Configuration")


class ErrorReportLocationModel(BaseModel):
    s3_report_location: Optional[S3ReportLocationModel] = Field(
        default=None, alias="S3ReportLocation"
    )


class ListScheduledQueriesRequestListScheduledQueriesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class QueryRequestQueryPaginateModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MixedMeasureMappingModel(BaseModel):
    measure_value_type: Literal[
        "BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "VARCHAR"
    ] = Field(alias="MeasureValueType")
    measure_name: Optional[str] = Field(default=None, alias="MeasureName")
    source_column: Optional[str] = Field(default=None, alias="SourceColumn")
    target_measure_name: Optional[str] = Field(default=None, alias="TargetMeasureName")
    multi_measure_attribute_mappings: Optional[
        Sequence[MultiMeasureAttributeMappingModel]
    ] = Field(default=None, alias="MultiMeasureAttributeMappings")


class MultiMeasureMappingsModel(BaseModel):
    multi_measure_attribute_mappings: Sequence[
        MultiMeasureAttributeMappingModel
    ] = Field(alias="MultiMeasureAttributeMappings")
    target_multi_measure_name: Optional[str] = Field(
        default=None, alias="TargetMultiMeasureName"
    )


class NotificationConfigurationModel(BaseModel):
    sns_configuration: SnsConfigurationModel = Field(alias="SnsConfiguration")


class PrepareQueryResponseModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    columns: List[SelectColumnModel] = Field(alias="Columns")
    parameters: List[ParameterMappingModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryResponseModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    next_token: str = Field(alias="NextToken")
    rows: List[RowModel] = Field(alias="Rows")
    column_info: List[ColumnInfoModel] = Field(alias="ColumnInfo")
    query_status: QueryStatusModel = Field(alias="QueryStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetDestinationModel(BaseModel):
    timestream_destination: Optional[TimestreamDestinationModel] = Field(
        default=None, alias="TimestreamDestination"
    )


class ScheduledQueryRunSummaryModel(BaseModel):
    invocation_time: Optional[datetime] = Field(default=None, alias="InvocationTime")
    trigger_time: Optional[datetime] = Field(default=None, alias="TriggerTime")
    run_status: Optional[
        Literal[
            "AUTO_TRIGGER_FAILURE",
            "AUTO_TRIGGER_SUCCESS",
            "MANUAL_TRIGGER_FAILURE",
            "MANUAL_TRIGGER_SUCCESS",
        ]
    ] = Field(default=None, alias="RunStatus")
    execution_stats: Optional[ExecutionStatsModel] = Field(
        default=None, alias="ExecutionStats"
    )
    error_report_location: Optional[ErrorReportLocationModel] = Field(
        default=None, alias="ErrorReportLocation"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class TimestreamConfigurationModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    time_column: str = Field(alias="TimeColumn")
    dimension_mappings: Sequence[DimensionMappingModel] = Field(
        alias="DimensionMappings"
    )
    multi_measure_mappings: Optional[MultiMeasureMappingsModel] = Field(
        default=None, alias="MultiMeasureMappings"
    )
    mixed_measure_mappings: Optional[Sequence[MixedMeasureMappingModel]] = Field(
        default=None, alias="MixedMeasureMappings"
    )
    measure_name_column: Optional[str] = Field(default=None, alias="MeasureNameColumn")


class ScheduledQueryModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    previous_invocation_time: Optional[datetime] = Field(
        default=None, alias="PreviousInvocationTime"
    )
    next_invocation_time: Optional[datetime] = Field(
        default=None, alias="NextInvocationTime"
    )
    error_report_configuration: Optional[ErrorReportConfigurationModel] = Field(
        default=None, alias="ErrorReportConfiguration"
    )
    target_destination: Optional[TargetDestinationModel] = Field(
        default=None, alias="TargetDestination"
    )
    last_run_status: Optional[
        Literal[
            "AUTO_TRIGGER_FAILURE",
            "AUTO_TRIGGER_SUCCESS",
            "MANUAL_TRIGGER_FAILURE",
            "MANUAL_TRIGGER_SUCCESS",
        ]
    ] = Field(default=None, alias="LastRunStatus")


class TargetConfigurationModel(BaseModel):
    timestream_configuration: TimestreamConfigurationModel = Field(
        alias="TimestreamConfiguration"
    )


class ListScheduledQueriesResponseModel(BaseModel):
    scheduled_queries: List[ScheduledQueryModel] = Field(alias="ScheduledQueries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduledQueryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    query_string: str = Field(alias="QueryString")
    schedule_configuration: ScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    notification_configuration: NotificationConfigurationModel = Field(
        alias="NotificationConfiguration"
    )
    scheduled_query_execution_role_arn: str = Field(
        alias="ScheduledQueryExecutionRoleArn"
    )
    error_report_configuration: ErrorReportConfigurationModel = Field(
        alias="ErrorReportConfiguration"
    )
    target_configuration: Optional[TargetConfigurationModel] = Field(
        default=None, alias="TargetConfiguration"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ScheduledQueryDescriptionModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    query_string: str = Field(alias="QueryString")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    schedule_configuration: ScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    notification_configuration: NotificationConfigurationModel = Field(
        alias="NotificationConfiguration"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    previous_invocation_time: Optional[datetime] = Field(
        default=None, alias="PreviousInvocationTime"
    )
    next_invocation_time: Optional[datetime] = Field(
        default=None, alias="NextInvocationTime"
    )
    target_configuration: Optional[TargetConfigurationModel] = Field(
        default=None, alias="TargetConfiguration"
    )
    scheduled_query_execution_role_arn: Optional[str] = Field(
        default=None, alias="ScheduledQueryExecutionRoleArn"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    error_report_configuration: Optional[ErrorReportConfigurationModel] = Field(
        default=None, alias="ErrorReportConfiguration"
    )
    last_run_summary: Optional[ScheduledQueryRunSummaryModel] = Field(
        default=None, alias="LastRunSummary"
    )
    recently_failed_runs: Optional[List[ScheduledQueryRunSummaryModel]] = Field(
        default=None, alias="RecentlyFailedRuns"
    )


class DescribeScheduledQueryResponseModel(BaseModel):
    scheduled_query: ScheduledQueryDescriptionModel = Field(alias="ScheduledQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
