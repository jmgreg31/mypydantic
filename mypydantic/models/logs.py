# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateKmsKeyRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    kms_key_id: str = Field(alias="kmsKeyId")


class CancelExportTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class CreateExportTaskRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    from_time: int = Field(alias="fromTime")
    to: int = Field(alias="to")
    destination: str = Field(alias="destination")
    task_name: Optional[str] = Field(default=None, alias="taskName")
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )
    destination_prefix: Optional[str] = Field(default=None, alias="destinationPrefix")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLogGroupRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateLogStreamRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    log_stream_name: str = Field(alias="logStreamName")


class DeleteDataProtectionPolicyRequestModel(BaseModel):
    log_group_identifier: str = Field(alias="logGroupIdentifier")


class DeleteDestinationRequestModel(BaseModel):
    destination_name: str = Field(alias="destinationName")


class DeleteLogGroupRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")


class DeleteLogStreamRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    log_stream_name: str = Field(alias="logStreamName")


class DeleteMetricFilterRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    filter_name: str = Field(alias="filterName")


class DeleteQueryDefinitionRequestModel(BaseModel):
    query_definition_id: str = Field(alias="queryDefinitionId")


class DeleteResourcePolicyRequestModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")


class DeleteRetentionPolicyRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")


class DeleteSubscriptionFilterRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    filter_name: str = Field(alias="filterName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeDestinationsRequestModel(BaseModel):
    destination_name_prefix: Optional[str] = Field(
        default=None, alias="DestinationNamePrefix"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")


class DestinationModel(BaseModel):
    destination_name: Optional[str] = Field(default=None, alias="destinationName")
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    access_policy: Optional[str] = Field(default=None, alias="accessPolicy")
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_time: Optional[int] = Field(default=None, alias="creationTime")


class DescribeExportTasksRequestModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    status_code: Optional[
        Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ]
    ] = Field(default=None, alias="statusCode")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")


class DescribeLogGroupsRequestModel(BaseModel):
    account_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="accountIdentifiers"
    )
    log_group_name_prefix: Optional[str] = Field(
        default=None, alias="logGroupNamePrefix"
    )
    log_group_name_pattern: Optional[str] = Field(
        default=None, alias="logGroupNamePattern"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")
    include_linked_accounts: Optional[bool] = Field(
        default=None, alias="includeLinkedAccounts"
    )


class LogGroupModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    creation_time: Optional[int] = Field(default=None, alias="creationTime")
    retention_in_days: Optional[int] = Field(default=None, alias="retentionInDays")
    metric_filter_count: Optional[int] = Field(default=None, alias="metricFilterCount")
    arn: Optional[str] = Field(default=None, alias="arn")
    stored_bytes: Optional[int] = Field(default=None, alias="storedBytes")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    data_protection_status: Optional[
        Literal["ACTIVATED", "ARCHIVED", "DELETED", "DISABLED"]
    ] = Field(default=None, alias="dataProtectionStatus")


class DescribeLogStreamsRequestModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )
    order_by: Optional[Literal["LastEventTime", "LogStreamName"]] = Field(
        default=None, alias="orderBy"
    )
    descending: Optional[bool] = Field(default=None, alias="descending")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")


class LogStreamModel(BaseModel):
    log_stream_name: Optional[str] = Field(default=None, alias="logStreamName")
    creation_time: Optional[int] = Field(default=None, alias="creationTime")
    first_event_timestamp: Optional[int] = Field(
        default=None, alias="firstEventTimestamp"
    )
    last_event_timestamp: Optional[int] = Field(
        default=None, alias="lastEventTimestamp"
    )
    last_ingestion_time: Optional[int] = Field(default=None, alias="lastIngestionTime")
    upload_sequence_token: Optional[str] = Field(
        default=None, alias="uploadSequenceToken"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    stored_bytes: Optional[int] = Field(default=None, alias="storedBytes")


class DescribeMetricFiltersRequestModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    filter_name_prefix: Optional[str] = Field(default=None, alias="filterNamePrefix")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    metric_namespace: Optional[str] = Field(default=None, alias="metricNamespace")


class DescribeQueriesRequestModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    status: Optional[
        Literal[
            "Cancelled",
            "Complete",
            "Failed",
            "Running",
            "Scheduled",
            "Timeout",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class QueryInfoModel(BaseModel):
    query_id: Optional[str] = Field(default=None, alias="queryId")
    query_string: Optional[str] = Field(default=None, alias="queryString")
    status: Optional[
        Literal[
            "Cancelled",
            "Complete",
            "Failed",
            "Running",
            "Scheduled",
            "Timeout",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")


class DescribeQueryDefinitionsRequestModel(BaseModel):
    query_definition_name_prefix: Optional[str] = Field(
        default=None, alias="queryDefinitionNamePrefix"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class QueryDefinitionModel(BaseModel):
    query_definition_id: Optional[str] = Field(default=None, alias="queryDefinitionId")
    name: Optional[str] = Field(default=None, alias="name")
    query_string: Optional[str] = Field(default=None, alias="queryString")
    last_modified: Optional[int] = Field(default=None, alias="lastModified")
    log_group_names: Optional[List[str]] = Field(default=None, alias="logGroupNames")


class DescribeResourcePoliciesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")


class ResourcePolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    policy_document: Optional[str] = Field(default=None, alias="policyDocument")
    last_updated_time: Optional[int] = Field(default=None, alias="lastUpdatedTime")


class DescribeSubscriptionFiltersRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    filter_name_prefix: Optional[str] = Field(default=None, alias="filterNamePrefix")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")


class SubscriptionFilterModel(BaseModel):
    filter_name: Optional[str] = Field(default=None, alias="filterName")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    filter_pattern: Optional[str] = Field(default=None, alias="filterPattern")
    destination_arn: Optional[str] = Field(default=None, alias="destinationArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    distribution: Optional[Literal["ByLogStream", "Random"]] = Field(
        default=None, alias="distribution"
    )
    creation_time: Optional[int] = Field(default=None, alias="creationTime")


class DisassociateKmsKeyRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")


class ExportTaskExecutionInfoModel(BaseModel):
    creation_time: Optional[int] = Field(default=None, alias="creationTime")
    completion_time: Optional[int] = Field(default=None, alias="completionTime")


class ExportTaskStatusModel(BaseModel):
    code: Optional[
        Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class FilterLogEventsRequestModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )
    log_stream_names: Optional[Sequence[str]] = Field(
        default=None, alias="logStreamNames"
    )
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )
    start_time: Optional[int] = Field(default=None, alias="startTime")
    end_time: Optional[int] = Field(default=None, alias="endTime")
    filter_pattern: Optional[str] = Field(default=None, alias="filterPattern")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")
    interleaved: Optional[bool] = Field(default=None, alias="interleaved")
    unmask: Optional[bool] = Field(default=None, alias="unmask")


class FilteredLogEventModel(BaseModel):
    log_stream_name: Optional[str] = Field(default=None, alias="logStreamName")
    timestamp: Optional[int] = Field(default=None, alias="timestamp")
    message: Optional[str] = Field(default=None, alias="message")
    ingestion_time: Optional[int] = Field(default=None, alias="ingestionTime")
    event_id: Optional[str] = Field(default=None, alias="eventId")


class SearchedLogStreamModel(BaseModel):
    log_stream_name: Optional[str] = Field(default=None, alias="logStreamName")
    searched_completely: Optional[bool] = Field(
        default=None, alias="searchedCompletely"
    )


class GetDataProtectionPolicyRequestModel(BaseModel):
    log_group_identifier: str = Field(alias="logGroupIdentifier")


class GetLogEventsRequestModel(BaseModel):
    log_stream_name: str = Field(alias="logStreamName")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )
    start_time: Optional[int] = Field(default=None, alias="startTime")
    end_time: Optional[int] = Field(default=None, alias="endTime")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    limit: Optional[int] = Field(default=None, alias="limit")
    start_from_head: Optional[bool] = Field(default=None, alias="startFromHead")
    unmask: Optional[bool] = Field(default=None, alias="unmask")


class OutputLogEventModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="timestamp")
    message: Optional[str] = Field(default=None, alias="message")
    ingestion_time: Optional[int] = Field(default=None, alias="ingestionTime")


class GetLogGroupFieldsRequestModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    time: Optional[int] = Field(default=None, alias="time")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )


class LogGroupFieldModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    percent: Optional[int] = Field(default=None, alias="percent")


class GetLogRecordRequestModel(BaseModel):
    log_record_pointer: str = Field(alias="logRecordPointer")
    unmask: Optional[bool] = Field(default=None, alias="unmask")


class GetQueryResultsRequestModel(BaseModel):
    query_id: str = Field(alias="queryId")


class QueryStatisticsModel(BaseModel):
    records_matched: Optional[float] = Field(default=None, alias="recordsMatched")
    records_scanned: Optional[float] = Field(default=None, alias="recordsScanned")
    bytes_scanned: Optional[float] = Field(default=None, alias="bytesScanned")


class ResultFieldModel(BaseModel):
    field: Optional[str] = Field(default=None, alias="field")
    value: Optional[str] = Field(default=None, alias="value")


class InputLogEventModel(BaseModel):
    timestamp: int = Field(alias="timestamp")
    message: str = Field(alias="message")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTagsLogGroupRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")


class MetricFilterMatchRecordModel(BaseModel):
    event_number: Optional[int] = Field(default=None, alias="eventNumber")
    event_message: Optional[str] = Field(default=None, alias="eventMessage")
    extracted_values: Optional[Dict[str, str]] = Field(
        default=None, alias="extractedValues"
    )


class MetricTransformationModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_namespace: str = Field(alias="metricNamespace")
    metric_value: str = Field(alias="metricValue")
    default_value: Optional[float] = Field(default=None, alias="defaultValue")
    dimensions: Optional[Dict[str, str]] = Field(default=None, alias="dimensions")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="unit")


class PutDataProtectionPolicyRequestModel(BaseModel):
    log_group_identifier: str = Field(alias="logGroupIdentifier")
    policy_document: str = Field(alias="policyDocument")


class PutDestinationPolicyRequestModel(BaseModel):
    destination_name: str = Field(alias="destinationName")
    access_policy: str = Field(alias="accessPolicy")
    force_update: Optional[bool] = Field(default=None, alias="forceUpdate")


class PutDestinationRequestModel(BaseModel):
    destination_name: str = Field(alias="destinationName")
    target_arn: str = Field(alias="targetArn")
    role_arn: str = Field(alias="roleArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class RejectedLogEventsInfoModel(BaseModel):
    too_new_log_event_start_index: Optional[int] = Field(
        default=None, alias="tooNewLogEventStartIndex"
    )
    too_old_log_event_end_index: Optional[int] = Field(
        default=None, alias="tooOldLogEventEndIndex"
    )
    expired_log_event_end_index: Optional[int] = Field(
        default=None, alias="expiredLogEventEndIndex"
    )


class PutQueryDefinitionRequestModel(BaseModel):
    name: str = Field(alias="name")
    query_string: str = Field(alias="queryString")
    query_definition_id: Optional[str] = Field(default=None, alias="queryDefinitionId")
    log_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="logGroupNames"
    )


class PutResourcePolicyRequestModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    policy_document: Optional[str] = Field(default=None, alias="policyDocument")


class PutRetentionPolicyRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    retention_in_days: int = Field(alias="retentionInDays")


class PutSubscriptionFilterRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    filter_name: str = Field(alias="filterName")
    filter_pattern: str = Field(alias="filterPattern")
    destination_arn: str = Field(alias="destinationArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    distribution: Optional[Literal["ByLogStream", "Random"]] = Field(
        default=None, alias="distribution"
    )


class StartQueryRequestModel(BaseModel):
    start_time: int = Field(alias="startTime")
    end_time: int = Field(alias="endTime")
    query_string: str = Field(alias="queryString")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="logGroupNames"
    )
    log_group_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="logGroupIdentifiers"
    )
    limit: Optional[int] = Field(default=None, alias="limit")


class StopQueryRequestModel(BaseModel):
    query_id: str = Field(alias="queryId")


class TagLogGroupRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    tags: Mapping[str, str] = Field(alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TestMetricFilterRequestModel(BaseModel):
    filter_pattern: str = Field(alias="filterPattern")
    log_event_messages: Sequence[str] = Field(alias="logEventMessages")


class UntagLogGroupRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    tags: Sequence[str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CreateExportTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteQueryDefinitionResponseModel(BaseModel):
    success: bool = Field(alias="success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataProtectionPolicyResponseModel(BaseModel):
    log_group_identifier: str = Field(alias="logGroupIdentifier")
    policy_document: str = Field(alias="policyDocument")
    last_updated_time: int = Field(alias="lastUpdatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLogRecordResponseModel(BaseModel):
    log_record: Dict[str, str] = Field(alias="logRecord")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsLogGroupResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDataProtectionPolicyResponseModel(BaseModel):
    log_group_identifier: str = Field(alias="logGroupIdentifier")
    policy_document: str = Field(alias="policyDocument")
    last_updated_time: int = Field(alias="lastUpdatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutQueryDefinitionResponseModel(BaseModel):
    query_definition_id: str = Field(alias="queryDefinitionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartQueryResponseModel(BaseModel):
    query_id: str = Field(alias="queryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopQueryResponseModel(BaseModel):
    success: bool = Field(alias="success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDestinationsRequestDescribeDestinationsPaginateModel(BaseModel):
    destination_name_prefix: Optional[str] = Field(
        default=None, alias="DestinationNamePrefix"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeExportTasksRequestDescribeExportTasksPaginateModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    status_code: Optional[
        Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ]
    ] = Field(default=None, alias="statusCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLogGroupsRequestDescribeLogGroupsPaginateModel(BaseModel):
    account_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="accountIdentifiers"
    )
    log_group_name_prefix: Optional[str] = Field(
        default=None, alias="logGroupNamePrefix"
    )
    log_group_name_pattern: Optional[str] = Field(
        default=None, alias="logGroupNamePattern"
    )
    include_linked_accounts: Optional[bool] = Field(
        default=None, alias="includeLinkedAccounts"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLogStreamsRequestDescribeLogStreamsPaginateModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )
    order_by: Optional[Literal["LastEventTime", "LogStreamName"]] = Field(
        default=None, alias="orderBy"
    )
    descending: Optional[bool] = Field(default=None, alias="descending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMetricFiltersRequestDescribeMetricFiltersPaginateModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    filter_name_prefix: Optional[str] = Field(default=None, alias="filterNamePrefix")
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    metric_namespace: Optional[str] = Field(default=None, alias="metricNamespace")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeQueriesRequestDescribeQueriesPaginateModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    status: Optional[
        Literal[
            "Cancelled",
            "Complete",
            "Failed",
            "Running",
            "Scheduled",
            "Timeout",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeResourcePoliciesRequestDescribeResourcePoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSubscriptionFiltersRequestDescribeSubscriptionFiltersPaginateModel(
    BaseModel
):
    log_group_name: str = Field(alias="logGroupName")
    filter_name_prefix: Optional[str] = Field(default=None, alias="filterNamePrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class FilterLogEventsRequestFilterLogEventsPaginateModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_group_identifier: Optional[str] = Field(
        default=None, alias="logGroupIdentifier"
    )
    log_stream_names: Optional[Sequence[str]] = Field(
        default=None, alias="logStreamNames"
    )
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )
    start_time: Optional[int] = Field(default=None, alias="startTime")
    end_time: Optional[int] = Field(default=None, alias="endTime")
    filter_pattern: Optional[str] = Field(default=None, alias="filterPattern")
    interleaved: Optional[bool] = Field(default=None, alias="interleaved")
    unmask: Optional[bool] = Field(default=None, alias="unmask")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDestinationsResponseModel(BaseModel):
    destinations: List[DestinationModel] = Field(alias="destinations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDestinationResponseModel(BaseModel):
    destination: DestinationModel = Field(alias="destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLogGroupsResponseModel(BaseModel):
    log_groups: List[LogGroupModel] = Field(alias="logGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLogStreamsResponseModel(BaseModel):
    log_streams: List[LogStreamModel] = Field(alias="logStreams")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeQueriesResponseModel(BaseModel):
    queries: List[QueryInfoModel] = Field(alias="queries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeQueryDefinitionsResponseModel(BaseModel):
    query_definitions: List[QueryDefinitionModel] = Field(alias="queryDefinitions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePoliciesResponseModel(BaseModel):
    resource_policies: List[ResourcePolicyModel] = Field(alias="resourcePolicies")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="resourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSubscriptionFiltersResponseModel(BaseModel):
    subscription_filters: List[SubscriptionFilterModel] = Field(
        alias="subscriptionFilters"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportTaskModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    task_name: Optional[str] = Field(default=None, alias="taskName")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    from_: Optional[int] = Field(default=None, alias="from")
    to: Optional[int] = Field(default=None, alias="to")
    destination: Optional[str] = Field(default=None, alias="destination")
    destination_prefix: Optional[str] = Field(default=None, alias="destinationPrefix")
    status: Optional[ExportTaskStatusModel] = Field(default=None, alias="status")
    execution_info: Optional[ExportTaskExecutionInfoModel] = Field(
        default=None, alias="executionInfo"
    )


class FilterLogEventsResponseModel(BaseModel):
    events: List[FilteredLogEventModel] = Field(alias="events")
    searched_log_streams: List[SearchedLogStreamModel] = Field(
        alias="searchedLogStreams"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLogEventsResponseModel(BaseModel):
    events: List[OutputLogEventModel] = Field(alias="events")
    next_forward_token: str = Field(alias="nextForwardToken")
    next_backward_token: str = Field(alias="nextBackwardToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLogGroupFieldsResponseModel(BaseModel):
    log_group_fields: List[LogGroupFieldModel] = Field(alias="logGroupFields")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryResultsResponseModel(BaseModel):
    results: List[List[ResultFieldModel]] = Field(alias="results")
    statistics: QueryStatisticsModel = Field(alias="statistics")
    status: Literal[
        "Cancelled", "Complete", "Failed", "Running", "Scheduled", "Timeout", "Unknown"
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLogEventsRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    log_stream_name: str = Field(alias="logStreamName")
    log_events: Sequence[InputLogEventModel] = Field(alias="logEvents")
    sequence_token: Optional[str] = Field(default=None, alias="sequenceToken")


class TestMetricFilterResponseModel(BaseModel):
    matches: List[MetricFilterMatchRecordModel] = Field(alias="matches")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricFilterModel(BaseModel):
    filter_name: Optional[str] = Field(default=None, alias="filterName")
    filter_pattern: Optional[str] = Field(default=None, alias="filterPattern")
    metric_transformations: Optional[List[MetricTransformationModel]] = Field(
        default=None, alias="metricTransformations"
    )
    creation_time: Optional[int] = Field(default=None, alias="creationTime")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")


class PutMetricFilterRequestModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    filter_name: str = Field(alias="filterName")
    filter_pattern: str = Field(alias="filterPattern")
    metric_transformations: Sequence[MetricTransformationModel] = Field(
        alias="metricTransformations"
    )


class PutLogEventsResponseModel(BaseModel):
    next_sequence_token: str = Field(alias="nextSequenceToken")
    rejected_log_events_info: RejectedLogEventsInfoModel = Field(
        alias="rejectedLogEventsInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExportTasksResponseModel(BaseModel):
    export_tasks: List[ExportTaskModel] = Field(alias="exportTasks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMetricFiltersResponseModel(BaseModel):
    metric_filters: List[MetricFilterModel] = Field(alias="metricFilters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
