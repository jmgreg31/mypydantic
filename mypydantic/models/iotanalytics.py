# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
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


class AddAttributesActivityModel(BaseModel):
    name: str = Field(alias="name")
    attributes: Mapping[str, str] = Field(alias="attributes")
    next: Optional[str] = Field(default=None, alias="next")


class BatchPutMessageErrorEntryModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="messageId")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class MessageModel(BaseModel):
    message_id: str = Field(alias="messageId")
    payload: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="payload"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CancelPipelineReprocessingRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    reprocessing_id: str = Field(alias="reprocessingId")


class ChannelActivityModel(BaseModel):
    name: str = Field(alias="name")
    channel_name: str = Field(alias="channelName")
    next: Optional[str] = Field(default=None, alias="next")


class ChannelMessagesModel(BaseModel):
    s3_paths: Optional[Sequence[str]] = Field(default=None, alias="s3Paths")


class EstimatedResourceSizeModel(BaseModel):
    estimated_size_in_bytes: Optional[float] = Field(
        default=None, alias="estimatedSizeInBytes"
    )
    estimated_on: Optional[datetime] = Field(default=None, alias="estimatedOn")


class CustomerManagedChannelS3StorageSummaryModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class CustomerManagedChannelS3StorageModel(BaseModel):
    bucket: str = Field(alias="bucket")
    role_arn: str = Field(alias="roleArn")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class RetentionPeriodModel(BaseModel):
    unlimited: Optional[bool] = Field(default=None, alias="unlimited")
    number_of_days: Optional[int] = Field(default=None, alias="numberOfDays")


class ColumnModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")


class ResourceConfigurationModel(BaseModel):
    compute_type: Literal["ACU_1", "ACU_2"] = Field(alias="computeType")
    volume_size_in_gb: int = Field(alias="volumeSizeInGB")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class CreateDatasetContentRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    version_id: Optional[str] = Field(default=None, alias="versionId")


class VersioningConfigurationModel(BaseModel):
    unlimited: Optional[bool] = Field(default=None, alias="unlimited")
    max_versions: Optional[int] = Field(default=None, alias="maxVersions")


class CustomerManagedDatastoreS3StorageSummaryModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class CustomerManagedDatastoreS3StorageModel(BaseModel):
    bucket: str = Field(alias="bucket")
    role_arn: str = Field(alias="roleArn")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class DatasetActionSummaryModel(BaseModel):
    action_name: Optional[str] = Field(default=None, alias="actionName")
    action_type: Optional[Literal["CONTAINER", "QUERY"]] = Field(
        default=None, alias="actionType"
    )


class IotEventsDestinationConfigurationModel(BaseModel):
    input_name: str = Field(alias="inputName")
    role_arn: str = Field(alias="roleArn")


class DatasetContentStatusModel(BaseModel):
    state: Optional[Literal["CREATING", "FAILED", "SUCCEEDED"]] = Field(
        default=None, alias="state"
    )
    reason: Optional[str] = Field(default=None, alias="reason")


class DatasetContentVersionValueModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")


class DatasetEntryModel(BaseModel):
    entry_name: Optional[str] = Field(default=None, alias="entryName")
    data_uri: Optional[str] = Field(default=None, alias="dataURI")


class ScheduleModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="expression")


class TriggeringDatasetModel(BaseModel):
    name: str = Field(alias="name")


class DatastoreActivityModel(BaseModel):
    name: str = Field(alias="name")
    datastore_name: str = Field(alias="datastoreName")


class IotSiteWiseCustomerManagedDatastoreS3StorageSummaryModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class IotSiteWiseCustomerManagedDatastoreS3StorageModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class PartitionModel(BaseModel):
    attribute_name: str = Field(alias="attributeName")


class TimestampPartitionModel(BaseModel):
    attribute_name: str = Field(alias="attributeName")
    timestamp_format: Optional[str] = Field(default=None, alias="timestampFormat")


class DeleteChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")


class DeleteDatasetContentRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    version_id: Optional[str] = Field(default=None, alias="versionId")


class DeleteDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")


class DeleteDatastoreRequestModel(BaseModel):
    datastore_name: str = Field(alias="datastoreName")


class DeletePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")


class DeltaTimeSessionWindowConfigurationModel(BaseModel):
    timeout_in_minutes: int = Field(alias="timeoutInMinutes")


class DeltaTimeModel(BaseModel):
    offset_seconds: int = Field(alias="offsetSeconds")
    time_expression: str = Field(alias="timeExpression")


class DescribeChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    include_statistics: Optional[bool] = Field(default=None, alias="includeStatistics")


class DescribeDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")


class DescribeDatastoreRequestModel(BaseModel):
    datastore_name: str = Field(alias="datastoreName")
    include_statistics: Optional[bool] = Field(default=None, alias="includeStatistics")


class LoggingOptionsModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    level: Literal["ERROR"] = Field(alias="level")
    enabled: bool = Field(alias="enabled")


class DescribePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")


class DeviceRegistryEnrichActivityModel(BaseModel):
    name: str = Field(alias="name")
    attribute: str = Field(alias="attribute")
    thing_name: str = Field(alias="thingName")
    role_arn: str = Field(alias="roleArn")
    next: Optional[str] = Field(default=None, alias="next")


class DeviceShadowEnrichActivityModel(BaseModel):
    name: str = Field(alias="name")
    attribute: str = Field(alias="attribute")
    thing_name: str = Field(alias="thingName")
    role_arn: str = Field(alias="roleArn")
    next: Optional[str] = Field(default=None, alias="next")


class FilterActivityModel(BaseModel):
    name: str = Field(alias="name")
    filter: str = Field(alias="filter")
    next: Optional[str] = Field(default=None, alias="next")


class GetDatasetContentRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    version_id: Optional[str] = Field(default=None, alias="versionId")


class GlueConfigurationModel(BaseModel):
    table_name: str = Field(alias="tableName")
    database_name: str = Field(alias="databaseName")


class LambdaActivityModel(BaseModel):
    name: str = Field(alias="name")
    lambda_name: str = Field(alias="lambdaName")
    batch_size: int = Field(alias="batchSize")
    next: Optional[str] = Field(default=None, alias="next")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListChannelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetContentsRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    scheduled_on_or_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduledOnOrAfter"
    )
    scheduled_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduledBefore"
    )


class ListDatasetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatastoresRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListPipelinesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MathActivityModel(BaseModel):
    name: str = Field(alias="name")
    attribute: str = Field(alias="attribute")
    math: str = Field(alias="math")
    next: Optional[str] = Field(default=None, alias="next")


class OutputFileUriValueModel(BaseModel):
    file_name: str = Field(alias="fileName")


class RemoveAttributesActivityModel(BaseModel):
    name: str = Field(alias="name")
    attributes: Sequence[str] = Field(alias="attributes")
    next: Optional[str] = Field(default=None, alias="next")


class SelectAttributesActivityModel(BaseModel):
    name: str = Field(alias="name")
    attributes: Sequence[str] = Field(alias="attributes")
    next: Optional[str] = Field(default=None, alias="next")


class ReprocessingSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    status: Optional[Literal["CANCELLED", "FAILED", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")


class SampleChannelDataRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    max_messages: Optional[int] = Field(default=None, alias="maxMessages")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchPutMessageRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    messages: Sequence[MessageModel] = Field(alias="messages")


class BatchPutMessageResponseModel(BaseModel):
    batch_put_message_error_entries: List[BatchPutMessageErrorEntryModel] = Field(
        alias="batchPutMessageErrorEntries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetContentResponseModel(BaseModel):
    version_id: str = Field(alias="versionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePipelineResponseModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_arn: str = Field(alias="pipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunPipelineActivityResponseModel(BaseModel):
    payloads: List[bytes] = Field(alias="payloads")
    log_result: str = Field(alias="logResult")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SampleChannelDataResponseModel(BaseModel):
    payloads: List[bytes] = Field(alias="payloads")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPipelineReprocessingResponseModel(BaseModel):
    reprocessing_id: str = Field(alias="reprocessingId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPipelineReprocessingRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    channel_messages: Optional[ChannelMessagesModel] = Field(
        default=None, alias="channelMessages"
    )


class ChannelStatisticsModel(BaseModel):
    size: Optional[EstimatedResourceSizeModel] = Field(default=None, alias="size")


class DatastoreStatisticsModel(BaseModel):
    size: Optional[EstimatedResourceSizeModel] = Field(default=None, alias="size")


class ChannelStorageSummaryModel(BaseModel):
    service_managed_s3: Optional[Dict[str, Any]] = Field(
        default=None, alias="serviceManagedS3"
    )
    customer_managed_s3: Optional[CustomerManagedChannelS3StorageSummaryModel] = Field(
        default=None, alias="customerManagedS3"
    )


class ChannelStorageModel(BaseModel):
    service_managed_s3: Optional[Mapping[str, Any]] = Field(
        default=None, alias="serviceManagedS3"
    )
    customer_managed_s3: Optional[CustomerManagedChannelS3StorageModel] = Field(
        default=None, alias="customerManagedS3"
    )


class CreateChannelResponseModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    channel_arn: str = Field(alias="channelArn")
    retention_period: RetentionPeriodModel = Field(alias="retentionPeriod")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    dataset_arn: str = Field(alias="datasetArn")
    retention_period: RetentionPeriodModel = Field(alias="retentionPeriod")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatastoreResponseModel(BaseModel):
    datastore_name: str = Field(alias="datastoreName")
    datastore_arn: str = Field(alias="datastoreArn")
    retention_period: RetentionPeriodModel = Field(alias="retentionPeriod")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SchemaDefinitionModel(BaseModel):
    columns: Optional[Sequence[ColumnModel]] = Field(default=None, alias="columns")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class DatasetContentSummaryModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    status: Optional[DatasetContentStatusModel] = Field(default=None, alias="status")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    schedule_time: Optional[datetime] = Field(default=None, alias="scheduleTime")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")


class GetDatasetContentResponseModel(BaseModel):
    entries: List[DatasetEntryModel] = Field(alias="entries")
    timestamp: datetime = Field(alias="timestamp")
    status: DatasetContentStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasetTriggerModel(BaseModel):
    schedule: Optional[ScheduleModel] = Field(default=None, alias="schedule")
    dataset: Optional[TriggeringDatasetModel] = Field(default=None, alias="dataset")


class DatastoreIotSiteWiseMultiLayerStorageSummaryModel(BaseModel):
    customer_managed_s3_storage: Optional[
        IotSiteWiseCustomerManagedDatastoreS3StorageSummaryModel
    ] = Field(default=None, alias="customerManagedS3Storage")


class DatastoreIotSiteWiseMultiLayerStorageModel(BaseModel):
    customer_managed_s3_storage: IotSiteWiseCustomerManagedDatastoreS3StorageModel = (
        Field(alias="customerManagedS3Storage")
    )


class DatastorePartitionModel(BaseModel):
    attribute_partition: Optional[PartitionModel] = Field(
        default=None, alias="attributePartition"
    )
    timestamp_partition: Optional[TimestampPartitionModel] = Field(
        default=None, alias="timestampPartition"
    )


class LateDataRuleConfigurationModel(BaseModel):
    delta_time_session_window_configuration: Optional[
        DeltaTimeSessionWindowConfigurationModel
    ] = Field(default=None, alias="deltaTimeSessionWindowConfiguration")


class QueryFilterModel(BaseModel):
    delta_time: Optional[DeltaTimeModel] = Field(default=None, alias="deltaTime")


class DescribeLoggingOptionsResponseModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingOptionsRequestModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")


class S3DestinationConfigurationModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")
    role_arn: str = Field(alias="roleArn")
    glue_configuration: Optional[GlueConfigurationModel] = Field(
        default=None, alias="glueConfiguration"
    )


class ListChannelsRequestListChannelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetContentsRequestListDatasetContentsPaginateModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    scheduled_on_or_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduledOnOrAfter"
    )
    scheduled_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduledBefore"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetsRequestListDatasetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatastoresRequestListDatastoresPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesRequestListPipelinesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class VariableModel(BaseModel):
    name: str = Field(alias="name")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    dataset_content_version_value: Optional[DatasetContentVersionValueModel] = Field(
        default=None, alias="datasetContentVersionValue"
    )
    output_file_uri_value: Optional[OutputFileUriValueModel] = Field(
        default=None, alias="outputFileUriValue"
    )


class PipelineActivityModel(BaseModel):
    channel: Optional[ChannelActivityModel] = Field(default=None, alias="channel")
    lambda_: Optional[LambdaActivityModel] = Field(default=None, alias="lambda")
    datastore: Optional[DatastoreActivityModel] = Field(default=None, alias="datastore")
    add_attributes: Optional[AddAttributesActivityModel] = Field(
        default=None, alias="addAttributes"
    )
    remove_attributes: Optional[RemoveAttributesActivityModel] = Field(
        default=None, alias="removeAttributes"
    )
    select_attributes: Optional[SelectAttributesActivityModel] = Field(
        default=None, alias="selectAttributes"
    )
    filter: Optional[FilterActivityModel] = Field(default=None, alias="filter")
    math: Optional[MathActivityModel] = Field(default=None, alias="math")
    device_registry_enrich: Optional[DeviceRegistryEnrichActivityModel] = Field(
        default=None, alias="deviceRegistryEnrich"
    )
    device_shadow_enrich: Optional[DeviceShadowEnrichActivityModel] = Field(
        default=None, alias="deviceShadowEnrich"
    )


class PipelineSummaryModel(BaseModel):
    pipeline_name: Optional[str] = Field(default=None, alias="pipelineName")
    reprocessing_summaries: Optional[List[ReprocessingSummaryModel]] = Field(
        default=None, alias="reprocessingSummaries"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class ChannelSummaryModel(BaseModel):
    channel_name: Optional[str] = Field(default=None, alias="channelName")
    channel_storage: Optional[ChannelStorageSummaryModel] = Field(
        default=None, alias="channelStorage"
    )
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    last_message_arrival_time: Optional[datetime] = Field(
        default=None, alias="lastMessageArrivalTime"
    )


class ChannelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    storage: Optional[ChannelStorageModel] = Field(default=None, alias="storage")
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    last_message_arrival_time: Optional[datetime] = Field(
        default=None, alias="lastMessageArrivalTime"
    )


class CreateChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    channel_storage: Optional[ChannelStorageModel] = Field(
        default=None, alias="channelStorage"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    channel_storage: Optional[ChannelStorageModel] = Field(
        default=None, alias="channelStorage"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )


class ParquetConfigurationModel(BaseModel):
    schema_definition: Optional[SchemaDefinitionModel] = Field(
        default=None, alias="schemaDefinition"
    )


class ListDatasetContentsResponseModel(BaseModel):
    dataset_content_summaries: List[DatasetContentSummaryModel] = Field(
        alias="datasetContentSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasetSummaryModel(BaseModel):
    dataset_name: Optional[str] = Field(default=None, alias="datasetName")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    triggers: Optional[List[DatasetTriggerModel]] = Field(
        default=None, alias="triggers"
    )
    actions: Optional[List[DatasetActionSummaryModel]] = Field(
        default=None, alias="actions"
    )


class DatastoreStorageSummaryModel(BaseModel):
    service_managed_s3: Optional[Dict[str, Any]] = Field(
        default=None, alias="serviceManagedS3"
    )
    customer_managed_s3: Optional[
        CustomerManagedDatastoreS3StorageSummaryModel
    ] = Field(default=None, alias="customerManagedS3")
    iot_site_wise_multi_layer_storage: Optional[
        DatastoreIotSiteWiseMultiLayerStorageSummaryModel
    ] = Field(default=None, alias="iotSiteWiseMultiLayerStorage")


class DatastoreStorageModel(BaseModel):
    service_managed_s3: Optional[Mapping[str, Any]] = Field(
        default=None, alias="serviceManagedS3"
    )
    customer_managed_s3: Optional[CustomerManagedDatastoreS3StorageModel] = Field(
        default=None, alias="customerManagedS3"
    )
    iot_site_wise_multi_layer_storage: Optional[
        DatastoreIotSiteWiseMultiLayerStorageModel
    ] = Field(default=None, alias="iotSiteWiseMultiLayerStorage")


class DatastorePartitionsModel(BaseModel):
    partitions: Optional[Sequence[DatastorePartitionModel]] = Field(
        default=None, alias="partitions"
    )


class LateDataRuleModel(BaseModel):
    rule_configuration: LateDataRuleConfigurationModel = Field(
        alias="ruleConfiguration"
    )
    rule_name: Optional[str] = Field(default=None, alias="ruleName")


class SqlQueryDatasetActionModel(BaseModel):
    sql_query: str = Field(alias="sqlQuery")
    filters: Optional[Sequence[QueryFilterModel]] = Field(default=None, alias="filters")


class DatasetContentDeliveryDestinationModel(BaseModel):
    iot_events_destination_configuration: Optional[
        IotEventsDestinationConfigurationModel
    ] = Field(default=None, alias="iotEventsDestinationConfiguration")
    s3_destination_configuration: Optional[S3DestinationConfigurationModel] = Field(
        default=None, alias="s3DestinationConfiguration"
    )


class ContainerDatasetActionModel(BaseModel):
    image: str = Field(alias="image")
    execution_role_arn: str = Field(alias="executionRoleArn")
    resource_configuration: ResourceConfigurationModel = Field(
        alias="resourceConfiguration"
    )
    variables: Optional[Sequence[VariableModel]] = Field(
        default=None, alias="variables"
    )


class CreatePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_activities: Sequence[PipelineActivityModel] = Field(
        alias="pipelineActivities"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PipelineModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    activities: Optional[List[PipelineActivityModel]] = Field(
        default=None, alias="activities"
    )
    reprocessing_summaries: Optional[List[ReprocessingSummaryModel]] = Field(
        default=None, alias="reprocessingSummaries"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class RunPipelineActivityRequestModel(BaseModel):
    pipeline_activity: PipelineActivityModel = Field(alias="pipelineActivity")
    payloads: Sequence[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        alias="payloads"
    )


class UpdatePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_activities: Sequence[PipelineActivityModel] = Field(
        alias="pipelineActivities"
    )


class ListPipelinesResponseModel(BaseModel):
    pipeline_summaries: List[PipelineSummaryModel] = Field(alias="pipelineSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsResponseModel(BaseModel):
    channel_summaries: List[ChannelSummaryModel] = Field(alias="channelSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="channel")
    statistics: ChannelStatisticsModel = Field(alias="statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FileFormatConfigurationModel(BaseModel):
    json_configuration: Optional[Mapping[str, Any]] = Field(
        default=None, alias="jsonConfiguration"
    )
    parquet_configuration: Optional[ParquetConfigurationModel] = Field(
        default=None, alias="parquetConfiguration"
    )


class ListDatasetsResponseModel(BaseModel):
    dataset_summaries: List[DatasetSummaryModel] = Field(alias="datasetSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatastoreSummaryModel(BaseModel):
    datastore_name: Optional[str] = Field(default=None, alias="datastoreName")
    datastore_storage: Optional[DatastoreStorageSummaryModel] = Field(
        default=None, alias="datastoreStorage"
    )
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    last_message_arrival_time: Optional[datetime] = Field(
        default=None, alias="lastMessageArrivalTime"
    )
    file_format_type: Optional[Literal["JSON", "PARQUET"]] = Field(
        default=None, alias="fileFormatType"
    )
    datastore_partitions: Optional[DatastorePartitionsModel] = Field(
        default=None, alias="datastorePartitions"
    )


class DatasetContentDeliveryRuleModel(BaseModel):
    destination: DatasetContentDeliveryDestinationModel = Field(alias="destination")
    entry_name: Optional[str] = Field(default=None, alias="entryName")


class DatasetActionModel(BaseModel):
    action_name: Optional[str] = Field(default=None, alias="actionName")
    query_action: Optional[SqlQueryDatasetActionModel] = Field(
        default=None, alias="queryAction"
    )
    container_action: Optional[ContainerDatasetActionModel] = Field(
        default=None, alias="containerAction"
    )


class DescribePipelineResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatastoreRequestModel(BaseModel):
    datastore_name: str = Field(alias="datastoreName")
    datastore_storage: Optional[DatastoreStorageModel] = Field(
        default=None, alias="datastoreStorage"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    file_format_configuration: Optional[FileFormatConfigurationModel] = Field(
        default=None, alias="fileFormatConfiguration"
    )
    datastore_partitions: Optional[DatastorePartitionsModel] = Field(
        default=None, alias="datastorePartitions"
    )


class DatastoreModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    storage: Optional[DatastoreStorageModel] = Field(default=None, alias="storage")
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    last_message_arrival_time: Optional[datetime] = Field(
        default=None, alias="lastMessageArrivalTime"
    )
    file_format_configuration: Optional[FileFormatConfigurationModel] = Field(
        default=None, alias="fileFormatConfiguration"
    )
    datastore_partitions: Optional[DatastorePartitionsModel] = Field(
        default=None, alias="datastorePartitions"
    )


class UpdateDatastoreRequestModel(BaseModel):
    datastore_name: str = Field(alias="datastoreName")
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    datastore_storage: Optional[DatastoreStorageModel] = Field(
        default=None, alias="datastoreStorage"
    )
    file_format_configuration: Optional[FileFormatConfigurationModel] = Field(
        default=None, alias="fileFormatConfiguration"
    )


class ListDatastoresResponseModel(BaseModel):
    datastore_summaries: List[DatastoreSummaryModel] = Field(alias="datastoreSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    actions: Sequence[DatasetActionModel] = Field(alias="actions")
    triggers: Optional[Sequence[DatasetTriggerModel]] = Field(
        default=None, alias="triggers"
    )
    content_delivery_rules: Optional[Sequence[DatasetContentDeliveryRuleModel]] = Field(
        default=None, alias="contentDeliveryRules"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    versioning_configuration: Optional[VersioningConfigurationModel] = Field(
        default=None, alias="versioningConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    late_data_rules: Optional[Sequence[LateDataRuleModel]] = Field(
        default=None, alias="lateDataRules"
    )


class DatasetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    actions: Optional[List[DatasetActionModel]] = Field(default=None, alias="actions")
    triggers: Optional[List[DatasetTriggerModel]] = Field(
        default=None, alias="triggers"
    )
    content_delivery_rules: Optional[List[DatasetContentDeliveryRuleModel]] = Field(
        default=None, alias="contentDeliveryRules"
    )
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    versioning_configuration: Optional[VersioningConfigurationModel] = Field(
        default=None, alias="versioningConfiguration"
    )
    late_data_rules: Optional[List[LateDataRuleModel]] = Field(
        default=None, alias="lateDataRules"
    )


class UpdateDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    actions: Sequence[DatasetActionModel] = Field(alias="actions")
    triggers: Optional[Sequence[DatasetTriggerModel]] = Field(
        default=None, alias="triggers"
    )
    content_delivery_rules: Optional[Sequence[DatasetContentDeliveryRuleModel]] = Field(
        default=None, alias="contentDeliveryRules"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )
    versioning_configuration: Optional[VersioningConfigurationModel] = Field(
        default=None, alias="versioningConfiguration"
    )
    late_data_rules: Optional[Sequence[LateDataRuleModel]] = Field(
        default=None, alias="lateDataRules"
    )


class DescribeDatastoreResponseModel(BaseModel):
    datastore: DatastoreModel = Field(alias="datastore")
    statistics: DatastoreStatisticsModel = Field(alias="statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetResponseModel(BaseModel):
    dataset: DatasetModel = Field(alias="dataset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
