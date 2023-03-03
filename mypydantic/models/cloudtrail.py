# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AdvancedFieldSelectorModel(BaseModel):
    field: str = Field(alias="Field")
    equals: Optional[Sequence[str]] = Field(default=None, alias="Equals")
    starts_with: Optional[Sequence[str]] = Field(default=None, alias="StartsWith")
    ends_with: Optional[Sequence[str]] = Field(default=None, alias="EndsWith")
    not_equals: Optional[Sequence[str]] = Field(default=None, alias="NotEquals")
    not_starts_with: Optional[Sequence[str]] = Field(
        default=None, alias="NotStartsWith"
    )
    not_ends_with: Optional[Sequence[str]] = Field(default=None, alias="NotEndsWith")


class CancelQueryRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    event_data_store: Optional[str] = Field(default=None, alias="EventDataStore")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ChannelModel(BaseModel):
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    name: Optional[str] = Field(default=None, alias="Name")


class DestinationModel(BaseModel):
    type: Literal["AWS_SERVICE", "EVENT_DATA_STORE"] = Field(alias="Type")
    location: str = Field(alias="Location")


class DataResourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    values: Optional[List[str]] = Field(default=None, alias="Values")


class DeleteChannelRequestModel(BaseModel):
    channel: str = Field(alias="Channel")


class DeleteEventDataStoreRequestModel(BaseModel):
    event_data_store: str = Field(alias="EventDataStore")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteTrailRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeregisterOrganizationDelegatedAdminRequestModel(BaseModel):
    delegated_admin_account_id: str = Field(alias="DelegatedAdminAccountId")


class DescribeQueryRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    event_data_store: Optional[str] = Field(default=None, alias="EventDataStore")


class QueryStatisticsForDescribeQueryModel(BaseModel):
    events_matched: Optional[int] = Field(default=None, alias="EventsMatched")
    events_scanned: Optional[int] = Field(default=None, alias="EventsScanned")
    bytes_scanned: Optional[int] = Field(default=None, alias="BytesScanned")
    execution_time_in_millis: Optional[int] = Field(
        default=None, alias="ExecutionTimeInMillis"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class DescribeTrailsRequestModel(BaseModel):
    trail_name_list: Optional[Sequence[str]] = Field(
        default=None, alias="trailNameList"
    )
    include_shadow_trails: Optional[bool] = Field(
        default=None, alias="includeShadowTrails"
    )


class TrailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    sns_topic_name: Optional[str] = Field(default=None, alias="SnsTopicName")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicARN")
    include_global_service_events: Optional[bool] = Field(
        default=None, alias="IncludeGlobalServiceEvents"
    )
    is_multi_region_trail: Optional[bool] = Field(
        default=None, alias="IsMultiRegionTrail"
    )
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    trail_arn: Optional[str] = Field(default=None, alias="TrailARN")
    log_file_validation_enabled: Optional[bool] = Field(
        default=None, alias="LogFileValidationEnabled"
    )
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    cloud_watch_logs_role_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsRoleArn"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    has_custom_event_selectors: Optional[bool] = Field(
        default=None, alias="HasCustomEventSelectors"
    )
    has_insight_selectors: Optional[bool] = Field(
        default=None, alias="HasInsightSelectors"
    )
    is_organization_trail: Optional[bool] = Field(
        default=None, alias="IsOrganizationTrail"
    )


class ResourceModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class GetChannelRequestModel(BaseModel):
    channel: str = Field(alias="Channel")


class IngestionStatusModel(BaseModel):
    latest_ingestion_success_time: Optional[datetime] = Field(
        default=None, alias="LatestIngestionSuccessTime"
    )
    latest_ingestion_success_event_id: Optional[str] = Field(
        default=None, alias="LatestIngestionSuccessEventID"
    )
    latest_ingestion_error_code: Optional[str] = Field(
        default=None, alias="LatestIngestionErrorCode"
    )
    latest_ingestion_attempt_time: Optional[datetime] = Field(
        default=None, alias="LatestIngestionAttemptTime"
    )
    latest_ingestion_attempt_event_id: Optional[str] = Field(
        default=None, alias="LatestIngestionAttemptEventID"
    )


class GetEventDataStoreRequestModel(BaseModel):
    event_data_store: str = Field(alias="EventDataStore")


class GetEventSelectorsRequestModel(BaseModel):
    trail_name: str = Field(alias="TrailName")


class GetImportRequestModel(BaseModel):
    import_id: str = Field(alias="ImportId")


class ImportStatisticsModel(BaseModel):
    prefixes_found: Optional[int] = Field(default=None, alias="PrefixesFound")
    prefixes_completed: Optional[int] = Field(default=None, alias="PrefixesCompleted")
    files_completed: Optional[int] = Field(default=None, alias="FilesCompleted")
    events_completed: Optional[int] = Field(default=None, alias="EventsCompleted")
    failed_entries: Optional[int] = Field(default=None, alias="FailedEntries")


class GetInsightSelectorsRequestModel(BaseModel):
    trail_name: str = Field(alias="TrailName")


class InsightSelectorModel(BaseModel):
    insight_type: Optional[
        Literal["ApiCallRateInsight", "ApiErrorRateInsight"]
    ] = Field(default=None, alias="InsightType")


class GetQueryResultsRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    event_data_store: Optional[str] = Field(default=None, alias="EventDataStore")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_query_results: Optional[int] = Field(default=None, alias="MaxQueryResults")


class QueryStatisticsModel(BaseModel):
    results_count: Optional[int] = Field(default=None, alias="ResultsCount")
    total_results_count: Optional[int] = Field(default=None, alias="TotalResultsCount")
    bytes_scanned: Optional[int] = Field(default=None, alias="BytesScanned")


class GetResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetTrailRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetTrailStatusRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ImportFailureListItemModel(BaseModel):
    location: Optional[str] = Field(default=None, alias="Location")
    status: Optional[Literal["FAILED", "RETRY", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    error_type: Optional[str] = Field(default=None, alias="ErrorType")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class S3ImportSourceModel(BaseModel):
    s3_location_uri: str = Field(alias="S3LocationUri")
    s3_bucket_region: str = Field(alias="S3BucketRegion")
    s3_bucket_access_role_arn: str = Field(alias="S3BucketAccessRoleArn")


class ImportsListItemModel(BaseModel):
    import_id: Optional[str] = Field(default=None, alias="ImportId")
    import_status: Optional[
        Literal["COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"]
    ] = Field(default=None, alias="ImportStatus")
    destinations: Optional[List[str]] = Field(default=None, alias="Destinations")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class ListChannelsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEventDataStoresRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListImportFailuresRequestModel(BaseModel):
    import_id: str = Field(alias="ImportId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListImportsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    destination: Optional[str] = Field(default=None, alias="Destination")
    import_status: Optional[
        Literal["COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"]
    ] = Field(default=None, alias="ImportStatus")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPublicKeysRequestModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PublicKeyModel(BaseModel):
    value: Optional[bytes] = Field(default=None, alias="Value")
    validity_start_time: Optional[datetime] = Field(
        default=None, alias="ValidityStartTime"
    )
    validity_end_time: Optional[datetime] = Field(default=None, alias="ValidityEndTime")
    fingerprint: Optional[str] = Field(default=None, alias="Fingerprint")


class ListQueriesRequestModel(BaseModel):
    event_data_store: str = Field(alias="EventDataStore")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    query_status: Optional[
        Literal["CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"]
    ] = Field(default=None, alias="QueryStatus")


class QueryModel(BaseModel):
    query_id: Optional[str] = Field(default=None, alias="QueryId")
    query_status: Optional[
        Literal["CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"]
    ] = Field(default=None, alias="QueryStatus")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class ListTagsRequestModel(BaseModel):
    resource_id_list: Sequence[str] = Field(alias="ResourceIdList")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTrailsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TrailInfoModel(BaseModel):
    trail_arn: Optional[str] = Field(default=None, alias="TrailARN")
    name: Optional[str] = Field(default=None, alias="Name")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")


class LookupAttributeModel(BaseModel):
    attribute_key: Literal[
        "AccessKeyId",
        "EventId",
        "EventName",
        "EventSource",
        "ReadOnly",
        "ResourceName",
        "ResourceType",
        "Username",
    ] = Field(alias="AttributeKey")
    attribute_value: str = Field(alias="AttributeValue")


class PutResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_policy: str = Field(alias="ResourcePolicy")


class RegisterOrganizationDelegatedAdminRequestModel(BaseModel):
    member_account_id: str = Field(alias="MemberAccountId")


class RestoreEventDataStoreRequestModel(BaseModel):
    event_data_store: str = Field(alias="EventDataStore")


class StartLoggingRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartQueryRequestModel(BaseModel):
    query_statement: str = Field(alias="QueryStatement")
    delivery_s3_uri: Optional[str] = Field(default=None, alias="DeliveryS3Uri")


class StopImportRequestModel(BaseModel):
    import_id: str = Field(alias="ImportId")


class StopLoggingRequestModel(BaseModel):
    name: str = Field(alias="Name")


class UpdateTrailRequestModel(BaseModel):
    name: str = Field(alias="Name")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    sns_topic_name: Optional[str] = Field(default=None, alias="SnsTopicName")
    include_global_service_events: Optional[bool] = Field(
        default=None, alias="IncludeGlobalServiceEvents"
    )
    is_multi_region_trail: Optional[bool] = Field(
        default=None, alias="IsMultiRegionTrail"
    )
    enable_log_file_validation: Optional[bool] = Field(
        default=None, alias="EnableLogFileValidation"
    )
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    cloud_watch_logs_role_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsRoleArn"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    is_organization_trail: Optional[bool] = Field(
        default=None, alias="IsOrganizationTrail"
    )


class AddTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags_list: Sequence[TagModel] = Field(alias="TagsList")


class CreateTrailRequestModel(BaseModel):
    name: str = Field(alias="Name")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    sns_topic_name: Optional[str] = Field(default=None, alias="SnsTopicName")
    include_global_service_events: Optional[bool] = Field(
        default=None, alias="IncludeGlobalServiceEvents"
    )
    is_multi_region_trail: Optional[bool] = Field(
        default=None, alias="IsMultiRegionTrail"
    )
    enable_log_file_validation: Optional[bool] = Field(
        default=None, alias="EnableLogFileValidation"
    )
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    cloud_watch_logs_role_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsRoleArn"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    is_organization_trail: Optional[bool] = Field(
        default=None, alias="IsOrganizationTrail"
    )
    tags_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagsList")


class RemoveTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags_list: Sequence[TagModel] = Field(alias="TagsList")


class ResourceTagModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    tags_list: Optional[List[TagModel]] = Field(default=None, alias="TagsList")


class AdvancedEventSelectorModel(BaseModel):
    field_selectors: Sequence[AdvancedFieldSelectorModel] = Field(
        alias="FieldSelectors"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class CancelQueryResponseModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    query_status: Literal[
        "CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"
    ] = Field(alias="QueryStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrailResponseModel(BaseModel):
    name: str = Field(alias="Name")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key_prefix: str = Field(alias="S3KeyPrefix")
    sns_topic_name: str = Field(alias="SnsTopicName")
    sns_topic_arn: str = Field(alias="SnsTopicARN")
    include_global_service_events: bool = Field(alias="IncludeGlobalServiceEvents")
    is_multi_region_trail: bool = Field(alias="IsMultiRegionTrail")
    trail_arn: str = Field(alias="TrailARN")
    log_file_validation_enabled: bool = Field(alias="LogFileValidationEnabled")
    cloud_watch_logs_log_group_arn: str = Field(alias="CloudWatchLogsLogGroupArn")
    cloud_watch_logs_role_arn: str = Field(alias="CloudWatchLogsRoleArn")
    kms_key_id: str = Field(alias="KmsKeyId")
    is_organization_trail: bool = Field(alias="IsOrganizationTrail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_policy: str = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrailStatusResponseModel(BaseModel):
    is_logging: bool = Field(alias="IsLogging")
    latest_delivery_error: str = Field(alias="LatestDeliveryError")
    latest_notification_error: str = Field(alias="LatestNotificationError")
    latest_delivery_time: datetime = Field(alias="LatestDeliveryTime")
    latest_notification_time: datetime = Field(alias="LatestNotificationTime")
    start_logging_time: datetime = Field(alias="StartLoggingTime")
    stop_logging_time: datetime = Field(alias="StopLoggingTime")
    latest_cloud_watch_logs_delivery_error: str = Field(
        alias="LatestCloudWatchLogsDeliveryError"
    )
    latest_cloud_watch_logs_delivery_time: datetime = Field(
        alias="LatestCloudWatchLogsDeliveryTime"
    )
    latest_digest_delivery_time: datetime = Field(alias="LatestDigestDeliveryTime")
    latest_digest_delivery_error: str = Field(alias="LatestDigestDeliveryError")
    latest_delivery_attempt_time: str = Field(alias="LatestDeliveryAttemptTime")
    latest_notification_attempt_time: str = Field(alias="LatestNotificationAttemptTime")
    latest_notification_attempt_succeeded: str = Field(
        alias="LatestNotificationAttemptSucceeded"
    )
    latest_delivery_attempt_succeeded: str = Field(
        alias="LatestDeliveryAttemptSucceeded"
    )
    time_logging_started: str = Field(alias="TimeLoggingStarted")
    time_logging_stopped: str = Field(alias="TimeLoggingStopped")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_policy: str = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartQueryResponseModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrailResponseModel(BaseModel):
    name: str = Field(alias="Name")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key_prefix: str = Field(alias="S3KeyPrefix")
    sns_topic_name: str = Field(alias="SnsTopicName")
    sns_topic_arn: str = Field(alias="SnsTopicARN")
    include_global_service_events: bool = Field(alias="IncludeGlobalServiceEvents")
    is_multi_region_trail: bool = Field(alias="IsMultiRegionTrail")
    trail_arn: str = Field(alias="TrailARN")
    log_file_validation_enabled: bool = Field(alias="LogFileValidationEnabled")
    cloud_watch_logs_log_group_arn: str = Field(alias="CloudWatchLogsLogGroupArn")
    cloud_watch_logs_role_arn: str = Field(alias="CloudWatchLogsRoleArn")
    kms_key_id: str = Field(alias="KmsKeyId")
    is_organization_trail: bool = Field(alias="IsOrganizationTrail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsResponseModel(BaseModel):
    channels: List[ChannelModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelRequestModel(BaseModel):
    name: str = Field(alias="Name")
    source: str = Field(alias="Source")
    destinations: Sequence[DestinationModel] = Field(alias="Destinations")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    name: str = Field(alias="Name")
    source: str = Field(alias="Source")
    destinations: List[DestinationModel] = Field(alias="Destinations")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelRequestModel(BaseModel):
    channel: str = Field(alias="Channel")
    destinations: Optional[Sequence[DestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    name: str = Field(alias="Name")
    source: str = Field(alias="Source")
    destinations: List[DestinationModel] = Field(alias="Destinations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventSelectorModel(BaseModel):
    read_write_type: Optional[Literal["All", "ReadOnly", "WriteOnly"]] = Field(
        default=None, alias="ReadWriteType"
    )
    include_management_events: Optional[bool] = Field(
        default=None, alias="IncludeManagementEvents"
    )
    data_resources: Optional[List[DataResourceModel]] = Field(
        default=None, alias="DataResources"
    )
    exclude_management_event_sources: Optional[List[str]] = Field(
        default=None, alias="ExcludeManagementEventSources"
    )


class DescribeQueryResponseModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    query_string: str = Field(alias="QueryString")
    query_status: Literal[
        "CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"
    ] = Field(alias="QueryStatus")
    query_statistics: QueryStatisticsForDescribeQueryModel = Field(
        alias="QueryStatistics"
    )
    error_message: str = Field(alias="ErrorMessage")
    delivery_s3_uri: str = Field(alias="DeliveryS3Uri")
    delivery_status: Literal[
        "ACCESS_DENIED",
        "ACCESS_DENIED_SIGNING_FILE",
        "CANCELLED",
        "FAILED",
        "FAILED_SIGNING_FILE",
        "PENDING",
        "RESOURCE_NOT_FOUND",
        "SUCCESS",
        "UNKNOWN",
    ] = Field(alias="DeliveryStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrailsResponseModel(BaseModel):
    trail_list: List[TrailModel] = Field(alias="trailList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrailResponseModel(BaseModel):
    trail: TrailModel = Field(alias="Trail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    event_name: Optional[str] = Field(default=None, alias="EventName")
    read_only: Optional[str] = Field(default=None, alias="ReadOnly")
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    event_source: Optional[str] = Field(default=None, alias="EventSource")
    username: Optional[str] = Field(default=None, alias="Username")
    resources: Optional[List[ResourceModel]] = Field(default=None, alias="Resources")
    cloud_trail_event: Optional[str] = Field(default=None, alias="CloudTrailEvent")


class GetInsightSelectorsResponseModel(BaseModel):
    trail_arn: str = Field(alias="TrailARN")
    insight_selectors: List[InsightSelectorModel] = Field(alias="InsightSelectors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutInsightSelectorsRequestModel(BaseModel):
    trail_name: str = Field(alias="TrailName")
    insight_selectors: Sequence[InsightSelectorModel] = Field(alias="InsightSelectors")


class PutInsightSelectorsResponseModel(BaseModel):
    trail_arn: str = Field(alias="TrailARN")
    insight_selectors: List[InsightSelectorModel] = Field(alias="InsightSelectors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryResultsResponseModel(BaseModel):
    query_status: Literal[
        "CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"
    ] = Field(alias="QueryStatus")
    query_statistics: QueryStatisticsModel = Field(alias="QueryStatistics")
    query_result_rows: List[List[Dict[str, str]]] = Field(alias="QueryResultRows")
    next_token: str = Field(alias="NextToken")
    error_message: str = Field(alias="ErrorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImportFailuresResponseModel(BaseModel):
    failures: List[ImportFailureListItemModel] = Field(alias="Failures")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportSourceModel(BaseModel):
    s3: S3ImportSourceModel = Field(alias="S3")


class ListImportsResponseModel(BaseModel):
    imports: List[ImportsListItemModel] = Field(alias="Imports")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImportFailuresRequestListImportFailuresPaginateModel(BaseModel):
    import_id: str = Field(alias="ImportId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImportsRequestListImportsPaginateModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")
    import_status: Optional[
        Literal["COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"]
    ] = Field(default=None, alias="ImportStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPublicKeysRequestListPublicKeysPaginateModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsRequestListTagsPaginateModel(BaseModel):
    resource_id_list: Sequence[str] = Field(alias="ResourceIdList")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrailsRequestListTrailsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPublicKeysResponseModel(BaseModel):
    public_key_list: List[PublicKeyModel] = Field(alias="PublicKeyList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueriesResponseModel(BaseModel):
    queries: List[QueryModel] = Field(alias="Queries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrailsResponseModel(BaseModel):
    trails: List[TrailInfoModel] = Field(alias="Trails")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LookupEventsRequestLookupEventsPaginateModel(BaseModel):
    lookup_attributes: Optional[Sequence[LookupAttributeModel]] = Field(
        default=None, alias="LookupAttributes"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    event_category: Optional[Literal["insight"]] = Field(
        default=None, alias="EventCategory"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LookupEventsRequestModel(BaseModel):
    lookup_attributes: Optional[Sequence[LookupAttributeModel]] = Field(
        default=None, alias="LookupAttributes"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    event_category: Optional[Literal["insight"]] = Field(
        default=None, alias="EventCategory"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsResponseModel(BaseModel):
    resource_tag_list: List[ResourceTagModel] = Field(alias="ResourceTagList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventDataStoreRequestModel(BaseModel):
    name: str = Field(alias="Name")
    advanced_event_selectors: Optional[Sequence[AdvancedEventSelectorModel]] = Field(
        default=None, alias="AdvancedEventSelectors"
    )
    multi_region_enabled: Optional[bool] = Field(
        default=None, alias="MultiRegionEnabled"
    )
    organization_enabled: Optional[bool] = Field(
        default=None, alias="OrganizationEnabled"
    )
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    termination_protection_enabled: Optional[bool] = Field(
        default=None, alias="TerminationProtectionEnabled"
    )
    tags_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagsList")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class CreateEventDataStoreResponseModel(BaseModel):
    event_data_store_arn: str = Field(alias="EventDataStoreArn")
    name: str = Field(alias="Name")
    status: Literal["CREATED", "ENABLED", "PENDING_DELETION"] = Field(alias="Status")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    multi_region_enabled: bool = Field(alias="MultiRegionEnabled")
    organization_enabled: bool = Field(alias="OrganizationEnabled")
    retention_period: int = Field(alias="RetentionPeriod")
    termination_protection_enabled: bool = Field(alias="TerminationProtectionEnabled")
    tags_list: List[TagModel] = Field(alias="TagsList")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    kms_key_id: str = Field(alias="KmsKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventDataStoreModel(BaseModel):
    event_data_store_arn: Optional[str] = Field(default=None, alias="EventDataStoreArn")
    name: Optional[str] = Field(default=None, alias="Name")
    termination_protection_enabled: Optional[bool] = Field(
        default=None, alias="TerminationProtectionEnabled"
    )
    status: Optional[Literal["CREATED", "ENABLED", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )
    advanced_event_selectors: Optional[List[AdvancedEventSelectorModel]] = Field(
        default=None, alias="AdvancedEventSelectors"
    )
    multi_region_enabled: Optional[bool] = Field(
        default=None, alias="MultiRegionEnabled"
    )
    organization_enabled: Optional[bool] = Field(
        default=None, alias="OrganizationEnabled"
    )
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class GetEventDataStoreResponseModel(BaseModel):
    event_data_store_arn: str = Field(alias="EventDataStoreArn")
    name: str = Field(alias="Name")
    status: Literal["CREATED", "ENABLED", "PENDING_DELETION"] = Field(alias="Status")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    multi_region_enabled: bool = Field(alias="MultiRegionEnabled")
    organization_enabled: bool = Field(alias="OrganizationEnabled")
    retention_period: int = Field(alias="RetentionPeriod")
    termination_protection_enabled: bool = Field(alias="TerminationProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    kms_key_id: str = Field(alias="KmsKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreEventDataStoreResponseModel(BaseModel):
    event_data_store_arn: str = Field(alias="EventDataStoreArn")
    name: str = Field(alias="Name")
    status: Literal["CREATED", "ENABLED", "PENDING_DELETION"] = Field(alias="Status")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    multi_region_enabled: bool = Field(alias="MultiRegionEnabled")
    organization_enabled: bool = Field(alias="OrganizationEnabled")
    retention_period: int = Field(alias="RetentionPeriod")
    termination_protection_enabled: bool = Field(alias="TerminationProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    kms_key_id: str = Field(alias="KmsKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceConfigModel(BaseModel):
    apply_to_all_regions: Optional[bool] = Field(
        default=None, alias="ApplyToAllRegions"
    )
    advanced_event_selectors: Optional[List[AdvancedEventSelectorModel]] = Field(
        default=None, alias="AdvancedEventSelectors"
    )


class UpdateEventDataStoreRequestModel(BaseModel):
    event_data_store: str = Field(alias="EventDataStore")
    name: Optional[str] = Field(default=None, alias="Name")
    advanced_event_selectors: Optional[Sequence[AdvancedEventSelectorModel]] = Field(
        default=None, alias="AdvancedEventSelectors"
    )
    multi_region_enabled: Optional[bool] = Field(
        default=None, alias="MultiRegionEnabled"
    )
    organization_enabled: Optional[bool] = Field(
        default=None, alias="OrganizationEnabled"
    )
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    termination_protection_enabled: Optional[bool] = Field(
        default=None, alias="TerminationProtectionEnabled"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class UpdateEventDataStoreResponseModel(BaseModel):
    event_data_store_arn: str = Field(alias="EventDataStoreArn")
    name: str = Field(alias="Name")
    status: Literal["CREATED", "ENABLED", "PENDING_DELETION"] = Field(alias="Status")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    multi_region_enabled: bool = Field(alias="MultiRegionEnabled")
    organization_enabled: bool = Field(alias="OrganizationEnabled")
    retention_period: int = Field(alias="RetentionPeriod")
    termination_protection_enabled: bool = Field(alias="TerminationProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    kms_key_id: str = Field(alias="KmsKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEventSelectorsResponseModel(BaseModel):
    trail_arn: str = Field(alias="TrailARN")
    event_selectors: List[EventSelectorModel] = Field(alias="EventSelectors")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEventSelectorsRequestModel(BaseModel):
    trail_name: str = Field(alias="TrailName")
    event_selectors: Optional[Sequence[EventSelectorModel]] = Field(
        default=None, alias="EventSelectors"
    )
    advanced_event_selectors: Optional[Sequence[AdvancedEventSelectorModel]] = Field(
        default=None, alias="AdvancedEventSelectors"
    )


class PutEventSelectorsResponseModel(BaseModel):
    trail_arn: str = Field(alias="TrailARN")
    event_selectors: List[EventSelectorModel] = Field(alias="EventSelectors")
    advanced_event_selectors: List[AdvancedEventSelectorModel] = Field(
        alias="AdvancedEventSelectors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LookupEventsResponseModel(BaseModel):
    events: List[EventModel] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImportResponseModel(BaseModel):
    import_id: str = Field(alias="ImportId")
    destinations: List[str] = Field(alias="Destinations")
    import_source: ImportSourceModel = Field(alias="ImportSource")
    start_event_time: datetime = Field(alias="StartEventTime")
    end_event_time: datetime = Field(alias="EndEventTime")
    import_status: Literal[
        "COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"
    ] = Field(alias="ImportStatus")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    import_statistics: ImportStatisticsModel = Field(alias="ImportStatistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportRequestModel(BaseModel):
    destinations: Optional[Sequence[str]] = Field(default=None, alias="Destinations")
    import_source: Optional[ImportSourceModel] = Field(
        default=None, alias="ImportSource"
    )
    start_event_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartEventTime"
    )
    end_event_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="EndEventTime"
    )
    import_id: Optional[str] = Field(default=None, alias="ImportId")


class StartImportResponseModel(BaseModel):
    import_id: str = Field(alias="ImportId")
    destinations: List[str] = Field(alias="Destinations")
    import_source: ImportSourceModel = Field(alias="ImportSource")
    start_event_time: datetime = Field(alias="StartEventTime")
    end_event_time: datetime = Field(alias="EndEventTime")
    import_status: Literal[
        "COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"
    ] = Field(alias="ImportStatus")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopImportResponseModel(BaseModel):
    import_id: str = Field(alias="ImportId")
    import_source: ImportSourceModel = Field(alias="ImportSource")
    destinations: List[str] = Field(alias="Destinations")
    import_status: Literal[
        "COMPLETED", "FAILED", "INITIALIZING", "IN_PROGRESS", "STOPPED"
    ] = Field(alias="ImportStatus")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    updated_timestamp: datetime = Field(alias="UpdatedTimestamp")
    start_event_time: datetime = Field(alias="StartEventTime")
    end_event_time: datetime = Field(alias="EndEventTime")
    import_statistics: ImportStatisticsModel = Field(alias="ImportStatistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventDataStoresResponseModel(BaseModel):
    event_data_stores: List[EventDataStoreModel] = Field(alias="EventDataStores")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    name: str = Field(alias="Name")
    source: str = Field(alias="Source")
    source_config: SourceConfigModel = Field(alias="SourceConfig")
    destinations: List[DestinationModel] = Field(alias="Destinations")
    ingestion_status: IngestionStatusModel = Field(alias="IngestionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
