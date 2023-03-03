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


class AddTagsToStreamInputRequestModel(BaseModel):
    tags: Mapping[str, str] = Field(alias="Tags")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class HashKeyRangeModel(BaseModel):
    starting_hash_key: str = Field(alias="StartingHashKey")
    ending_hash_key: str = Field(alias="EndingHashKey")


class ConsumerDescriptionModel(BaseModel):
    consumer_name: str = Field(alias="ConsumerName")
    consumer_arn: str = Field(alias="ConsumerARN")
    consumer_status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(
        alias="ConsumerStatus"
    )
    consumer_creation_timestamp: datetime = Field(alias="ConsumerCreationTimestamp")
    stream_arn: str = Field(alias="StreamARN")


class ConsumerModel(BaseModel):
    consumer_name: str = Field(alias="ConsumerName")
    consumer_arn: str = Field(alias="ConsumerARN")
    consumer_status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(
        alias="ConsumerStatus"
    )
    consumer_creation_timestamp: datetime = Field(alias="ConsumerCreationTimestamp")


class StreamModeDetailsModel(BaseModel):
    stream_mode: Literal["ON_DEMAND", "PROVISIONED"] = Field(alias="StreamMode")


class DecreaseStreamRetentionPeriodInputRequestModel(BaseModel):
    retention_period_hours: int = Field(alias="RetentionPeriodHours")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DeleteStreamInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    enforce_consumer_deletion: Optional[bool] = Field(
        default=None, alias="EnforceConsumerDeletion"
    )
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DeregisterStreamConsumerInputRequestModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    consumer_name: Optional[str] = Field(default=None, alias="ConsumerName")
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerARN")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeStreamConsumerInputRequestModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    consumer_name: Optional[str] = Field(default=None, alias="ConsumerName")
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerARN")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeStreamInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeStreamSummaryInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DisableEnhancedMonitoringInputRequestModel(BaseModel):
    shard_level_metrics: Sequence[
        Literal[
            "ALL",
            "IncomingBytes",
            "IncomingRecords",
            "IteratorAgeMilliseconds",
            "OutgoingBytes",
            "OutgoingRecords",
            "ReadProvisionedThroughputExceeded",
            "WriteProvisionedThroughputExceeded",
        ]
    ] = Field(alias="ShardLevelMetrics")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class EnableEnhancedMonitoringInputRequestModel(BaseModel):
    shard_level_metrics: Sequence[
        Literal[
            "ALL",
            "IncomingBytes",
            "IncomingRecords",
            "IteratorAgeMilliseconds",
            "OutgoingBytes",
            "OutgoingRecords",
            "ReadProvisionedThroughputExceeded",
            "WriteProvisionedThroughputExceeded",
        ]
    ] = Field(alias="ShardLevelMetrics")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class EnhancedMetricsModel(BaseModel):
    shard_level_metrics: Optional[
        List[
            Literal[
                "ALL",
                "IncomingBytes",
                "IncomingRecords",
                "IteratorAgeMilliseconds",
                "OutgoingBytes",
                "OutgoingRecords",
                "ReadProvisionedThroughputExceeded",
                "WriteProvisionedThroughputExceeded",
            ]
        ]
    ] = Field(default=None, alias="ShardLevelMetrics")


class GetRecordsInputRequestModel(BaseModel):
    shard_iterator: str = Field(alias="ShardIterator")
    limit: Optional[int] = Field(default=None, alias="Limit")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class RecordModel(BaseModel):
    sequence_number: str = Field(alias="SequenceNumber")
    data: bytes = Field(alias="Data")
    partition_key: str = Field(alias="PartitionKey")
    approximate_arrival_timestamp: Optional[datetime] = Field(
        default=None, alias="ApproximateArrivalTimestamp"
    )
    encryption_type: Optional[Literal["KMS", "NONE"]] = Field(
        default=None, alias="EncryptionType"
    )


class GetShardIteratorInputRequestModel(BaseModel):
    shard_id: str = Field(alias="ShardId")
    shard_iterator_type: Literal[
        "AFTER_SEQUENCE_NUMBER",
        "AT_SEQUENCE_NUMBER",
        "AT_TIMESTAMP",
        "LATEST",
        "TRIM_HORIZON",
    ] = Field(alias="ShardIteratorType")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    starting_sequence_number: Optional[str] = Field(
        default=None, alias="StartingSequenceNumber"
    )
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class IncreaseStreamRetentionPeriodInputRequestModel(BaseModel):
    retention_period_hours: int = Field(alias="RetentionPeriodHours")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class InternalFailureExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSAccessDeniedExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSDisabledExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSInvalidStateExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSNotFoundExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSOptInRequiredModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class KMSThrottlingExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class ShardFilterModel(BaseModel):
    type: Literal[
        "AFTER_SHARD_ID",
        "AT_LATEST",
        "AT_TIMESTAMP",
        "AT_TRIM_HORIZON",
        "FROM_TIMESTAMP",
        "FROM_TRIM_HORIZON",
    ] = Field(alias="Type")
    shard_id: Optional[str] = Field(default=None, alias="ShardId")
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")


class ListStreamConsumersInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    stream_creation_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StreamCreationTimestamp"
    )


class ListStreamsInputRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_stream_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartStreamName"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForStreamInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    exclusive_start_tag_key: Optional[str] = Field(
        default=None, alias="ExclusiveStartTagKey"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class MergeShardsInputRequestModel(BaseModel):
    shard_to_merge: str = Field(alias="ShardToMerge")
    adjacent_shard_to_merge: str = Field(alias="AdjacentShardToMerge")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class PutRecordInputRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")
    partition_key: str = Field(alias="PartitionKey")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    explicit_hash_key: Optional[str] = Field(default=None, alias="ExplicitHashKey")
    sequence_number_for_ordering: Optional[str] = Field(
        default=None, alias="SequenceNumberForOrdering"
    )
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class PutRecordsRequestEntryModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")
    partition_key: str = Field(alias="PartitionKey")
    explicit_hash_key: Optional[str] = Field(default=None, alias="ExplicitHashKey")


class PutRecordsResultEntryModel(BaseModel):
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")
    shard_id: Optional[str] = Field(default=None, alias="ShardId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class RegisterStreamConsumerInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    consumer_name: str = Field(alias="ConsumerName")


class RemoveTagsFromStreamInputRequestModel(BaseModel):
    tag_keys: Sequence[str] = Field(alias="TagKeys")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class ResourceInUseExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class ResourceNotFoundExceptionModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class SequenceNumberRangeModel(BaseModel):
    starting_sequence_number: str = Field(alias="StartingSequenceNumber")
    ending_sequence_number: Optional[str] = Field(
        default=None, alias="EndingSequenceNumber"
    )


class SplitShardInputRequestModel(BaseModel):
    shard_to_split: str = Field(alias="ShardToSplit")
    new_starting_hash_key: str = Field(alias="NewStartingHashKey")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class StartStreamEncryptionInputRequestModel(BaseModel):
    encryption_type: Literal["KMS", "NONE"] = Field(alias="EncryptionType")
    key_id: str = Field(alias="KeyId")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class StartingPositionModel(BaseModel):
    type: Literal[
        "AFTER_SEQUENCE_NUMBER",
        "AT_SEQUENCE_NUMBER",
        "AT_TIMESTAMP",
        "LATEST",
        "TRIM_HORIZON",
    ] = Field(alias="Type")
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")


class StopStreamEncryptionInputRequestModel(BaseModel):
    encryption_type: Literal["KMS", "NONE"] = Field(alias="EncryptionType")
    key_id: str = Field(alias="KeyId")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class UpdateShardCountInputRequestModel(BaseModel):
    target_shard_count: int = Field(alias="TargetShardCount")
    scaling_type: Literal["UNIFORM_SCALING"] = Field(alias="ScalingType")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class ChildShardModel(BaseModel):
    shard_id: str = Field(alias="ShardId")
    parent_shards: List[str] = Field(alias="ParentShards")
    hash_key_range: HashKeyRangeModel = Field(alias="HashKeyRange")


class CreateStreamInputRequestModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    shard_count: Optional[int] = Field(default=None, alias="ShardCount")
    stream_mode_details: Optional[StreamModeDetailsModel] = Field(
        default=None, alias="StreamModeDetails"
    )


class StreamSummaryModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    stream_arn: str = Field(alias="StreamARN")
    stream_status: Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"] = Field(
        alias="StreamStatus"
    )
    stream_mode_details: Optional[StreamModeDetailsModel] = Field(
        default=None, alias="StreamModeDetails"
    )
    stream_creation_timestamp: Optional[datetime] = Field(
        default=None, alias="StreamCreationTimestamp"
    )


class UpdateStreamModeInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    stream_mode_details: StreamModeDetailsModel = Field(alias="StreamModeDetails")


class DescribeLimitsOutputModel(BaseModel):
    shard_limit: int = Field(alias="ShardLimit")
    open_shard_count: int = Field(alias="OpenShardCount")
    on_demand_stream_count: int = Field(alias="OnDemandStreamCount")
    on_demand_stream_count_limit: int = Field(alias="OnDemandStreamCountLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStreamConsumerOutputModel(BaseModel):
    consumer_description: ConsumerDescriptionModel = Field(alias="ConsumerDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnhancedMonitoringOutputModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    current_shard_level_metrics: List[
        Literal[
            "ALL",
            "IncomingBytes",
            "IncomingRecords",
            "IteratorAgeMilliseconds",
            "OutgoingBytes",
            "OutgoingRecords",
            "ReadProvisionedThroughputExceeded",
            "WriteProvisionedThroughputExceeded",
        ]
    ] = Field(alias="CurrentShardLevelMetrics")
    desired_shard_level_metrics: List[
        Literal[
            "ALL",
            "IncomingBytes",
            "IncomingRecords",
            "IteratorAgeMilliseconds",
            "OutgoingBytes",
            "OutgoingRecords",
            "ReadProvisionedThroughputExceeded",
            "WriteProvisionedThroughputExceeded",
        ]
    ] = Field(alias="DesiredShardLevelMetrics")
    stream_arn: str = Field(alias="StreamARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetShardIteratorOutputModel(BaseModel):
    shard_iterator: str = Field(alias="ShardIterator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamConsumersOutputModel(BaseModel):
    consumers: List[ConsumerModel] = Field(alias="Consumers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRecordOutputModel(BaseModel):
    shard_id: str = Field(alias="ShardId")
    sequence_number: str = Field(alias="SequenceNumber")
    encryption_type: Literal["KMS", "NONE"] = Field(alias="EncryptionType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterStreamConsumerOutputModel(BaseModel):
    consumer: ConsumerModel = Field(alias="Consumer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateShardCountOutputModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    current_shard_count: int = Field(alias="CurrentShardCount")
    target_shard_count: int = Field(alias="TargetShardCount")
    stream_arn: str = Field(alias="StreamARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStreamInputDescribeStreamPaginateModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamConsumersInputListStreamConsumersPaginateModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    stream_creation_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StreamCreationTimestamp"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamsInputListStreamsPaginateModel(BaseModel):
    exclusive_start_stream_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartStreamName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStreamInputStreamExistsWaitModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStreamInputStreamNotExistsWaitModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class StreamDescriptionSummaryModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    stream_arn: str = Field(alias="StreamARN")
    stream_status: Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"] = Field(
        alias="StreamStatus"
    )
    retention_period_hours: int = Field(alias="RetentionPeriodHours")
    stream_creation_timestamp: datetime = Field(alias="StreamCreationTimestamp")
    enhanced_monitoring: List[EnhancedMetricsModel] = Field(alias="EnhancedMonitoring")
    open_shard_count: int = Field(alias="OpenShardCount")
    stream_mode_details: Optional[StreamModeDetailsModel] = Field(
        default=None, alias="StreamModeDetails"
    )
    encryption_type: Optional[Literal["KMS", "NONE"]] = Field(
        default=None, alias="EncryptionType"
    )
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    consumer_count: Optional[int] = Field(default=None, alias="ConsumerCount")


class ListShardsInputListShardsPaginateModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )
    stream_creation_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StreamCreationTimestamp"
    )
    shard_filter: Optional[ShardFilterModel] = Field(default=None, alias="ShardFilter")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListShardsInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    stream_creation_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StreamCreationTimestamp"
    )
    shard_filter: Optional[ShardFilterModel] = Field(default=None, alias="ShardFilter")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class ListTagsForStreamOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    has_more_tags: bool = Field(alias="HasMoreTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRecordsInputRequestModel(BaseModel):
    records: Sequence[PutRecordsRequestEntryModel] = Field(alias="Records")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class PutRecordsOutputModel(BaseModel):
    failed_record_count: int = Field(alias="FailedRecordCount")
    records: List[PutRecordsResultEntryModel] = Field(alias="Records")
    encryption_type: Literal["KMS", "NONE"] = Field(alias="EncryptionType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ShardModel(BaseModel):
    shard_id: str = Field(alias="ShardId")
    hash_key_range: HashKeyRangeModel = Field(alias="HashKeyRange")
    sequence_number_range: SequenceNumberRangeModel = Field(alias="SequenceNumberRange")
    parent_shard_id: Optional[str] = Field(default=None, alias="ParentShardId")
    adjacent_parent_shard_id: Optional[str] = Field(
        default=None, alias="AdjacentParentShardId"
    )


class SubscribeToShardInputRequestModel(BaseModel):
    consumer_arn: str = Field(alias="ConsumerARN")
    shard_id: str = Field(alias="ShardId")
    starting_position: StartingPositionModel = Field(alias="StartingPosition")


class GetRecordsOutputModel(BaseModel):
    records: List[RecordModel] = Field(alias="Records")
    next_shard_iterator: str = Field(alias="NextShardIterator")
    millis_behind_latest: int = Field(alias="MillisBehindLatest")
    child_shards: List[ChildShardModel] = Field(alias="ChildShards")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscribeToShardEventModel(BaseModel):
    records: List[RecordModel] = Field(alias="Records")
    continuation_sequence_number: str = Field(alias="ContinuationSequenceNumber")
    millis_behind_latest: int = Field(alias="MillisBehindLatest")
    child_shards: Optional[List[ChildShardModel]] = Field(
        default=None, alias="ChildShards"
    )


class ListStreamsOutputModel(BaseModel):
    stream_names: List[str] = Field(alias="StreamNames")
    has_more_streams: bool = Field(alias="HasMoreStreams")
    next_token: str = Field(alias="NextToken")
    stream_summaries: List[StreamSummaryModel] = Field(alias="StreamSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStreamSummaryOutputModel(BaseModel):
    stream_description_summary: StreamDescriptionSummaryModel = Field(
        alias="StreamDescriptionSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListShardsOutputModel(BaseModel):
    shards: List[ShardModel] = Field(alias="Shards")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamDescriptionModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    stream_arn: str = Field(alias="StreamARN")
    stream_status: Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"] = Field(
        alias="StreamStatus"
    )
    shards: List[ShardModel] = Field(alias="Shards")
    has_more_shards: bool = Field(alias="HasMoreShards")
    retention_period_hours: int = Field(alias="RetentionPeriodHours")
    stream_creation_timestamp: datetime = Field(alias="StreamCreationTimestamp")
    enhanced_monitoring: List[EnhancedMetricsModel] = Field(alias="EnhancedMonitoring")
    stream_mode_details: Optional[StreamModeDetailsModel] = Field(
        default=None, alias="StreamModeDetails"
    )
    encryption_type: Optional[Literal["KMS", "NONE"]] = Field(
        default=None, alias="EncryptionType"
    )
    key_id: Optional[str] = Field(default=None, alias="KeyId")


class SubscribeToShardEventStreamModel(BaseModel):
    subscribe_to_shard_event: SubscribeToShardEventModel = Field(
        alias="SubscribeToShardEvent"
    )
    resource_not_found_exception: Optional[ResourceNotFoundExceptionModel] = Field(
        default=None, alias="ResourceNotFoundException"
    )
    resource_in_use_exception: Optional[ResourceInUseExceptionModel] = Field(
        default=None, alias="ResourceInUseException"
    )
    kms_disabled_exception: Optional[KMSDisabledExceptionModel] = Field(
        default=None, alias="KMSDisabledException"
    )
    kms_invalid_state_exception: Optional[KMSInvalidStateExceptionModel] = Field(
        default=None, alias="KMSInvalidStateException"
    )
    kms_access_denied_exception: Optional[KMSAccessDeniedExceptionModel] = Field(
        default=None, alias="KMSAccessDeniedException"
    )
    kms_not_found_exception: Optional[KMSNotFoundExceptionModel] = Field(
        default=None, alias="KMSNotFoundException"
    )
    kms_opt_in_required: Optional[KMSOptInRequiredModel] = Field(
        default=None, alias="KMSOptInRequired"
    )
    kms_throttling_exception: Optional[KMSThrottlingExceptionModel] = Field(
        default=None, alias="KMSThrottlingException"
    )
    internal_failure_exception: Optional[InternalFailureExceptionModel] = Field(
        default=None, alias="InternalFailureException"
    )


class DescribeStreamOutputModel(BaseModel):
    stream_description: StreamDescriptionModel = Field(alias="StreamDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscribeToShardOutputModel(BaseModel):
    event_stream: SubscribeToShardEventStreamModel = Field(alias="EventStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
