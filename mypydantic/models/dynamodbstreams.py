# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttributeValueModel(BaseModel):
    s: Optional[str] = Field(default=None, alias="S")
    n: Optional[str] = Field(default=None, alias="N")
    b: Optional[bytes] = Field(default=None, alias="B")
    s_s: Optional[List[str]] = Field(default=None, alias="SS")
    ns: Optional[List[str]] = Field(default=None, alias="NS")
    bs: Optional[List[bytes]] = Field(default=None, alias="BS")
    m: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="M")
    l: Optional[List[Dict[str, Any]]] = Field(default=None, alias="L")
    nul_l: Optional[bool] = Field(default=None, alias="NULL")
    bool: Optional[bool] = Field(default=None, alias="BOOL")


class DescribeStreamInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamArn")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_shard_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartShardId"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetRecordsInputRequestModel(BaseModel):
    shard_iterator: str = Field(alias="ShardIterator")
    limit: Optional[int] = Field(default=None, alias="Limit")


class GetShardIteratorInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamArn")
    shard_id: str = Field(alias="ShardId")
    shard_iterator_type: Literal[
        "AFTER_SEQUENCE_NUMBER", "AT_SEQUENCE_NUMBER", "LATEST", "TRIM_HORIZON"
    ] = Field(alias="ShardIteratorType")
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")


class IdentityModel(BaseModel):
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    type: Optional[str] = Field(default=None, alias="Type")


class KeySchemaElementModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    key_type: Literal["HASH", "RANGE"] = Field(alias="KeyType")


class ListStreamsInputRequestModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_stream_arn: Optional[str] = Field(
        default=None, alias="ExclusiveStartStreamArn"
    )


class StreamModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamArn")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    stream_label: Optional[str] = Field(default=None, alias="StreamLabel")


class StreamRecordModel(BaseModel):
    approximate_creation_date_time: Optional[datetime] = Field(
        default=None, alias="ApproximateCreationDateTime"
    )
    keys: Optional[Dict[str, AttributeValueModel]] = Field(default=None, alias="Keys")
    new_image: Optional[Dict[str, AttributeValueModel]] = Field(
        default=None, alias="NewImage"
    )
    old_image: Optional[Dict[str, AttributeValueModel]] = Field(
        default=None, alias="OldImage"
    )
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")
    size_bytes: Optional[int] = Field(default=None, alias="SizeBytes")
    stream_view_type: Optional[
        Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
    ] = Field(default=None, alias="StreamViewType")


class SequenceNumberRangeModel(BaseModel):
    starting_sequence_number: Optional[str] = Field(
        default=None, alias="StartingSequenceNumber"
    )
    ending_sequence_number: Optional[str] = Field(
        default=None, alias="EndingSequenceNumber"
    )


class GetShardIteratorOutputModel(BaseModel):
    shard_iterator: str = Field(alias="ShardIterator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamsOutputModel(BaseModel):
    streams: List[StreamModel] = Field(alias="Streams")
    last_evaluated_stream_arn: str = Field(alias="LastEvaluatedStreamArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecordModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="eventID")
    event_name: Optional[Literal["INSERT", "MODIFY", "REMOVE"]] = Field(
        default=None, alias="eventName"
    )
    event_version: Optional[str] = Field(default=None, alias="eventVersion")
    event_source: Optional[str] = Field(default=None, alias="eventSource")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    dynamodb: Optional[StreamRecordModel] = Field(default=None, alias="dynamodb")
    user_identity: Optional[IdentityModel] = Field(default=None, alias="userIdentity")


class ShardModel(BaseModel):
    shard_id: Optional[str] = Field(default=None, alias="ShardId")
    sequence_number_range: Optional[SequenceNumberRangeModel] = Field(
        default=None, alias="SequenceNumberRange"
    )
    parent_shard_id: Optional[str] = Field(default=None, alias="ParentShardId")


class GetRecordsOutputModel(BaseModel):
    records: List[RecordModel] = Field(alias="Records")
    next_shard_iterator: str = Field(alias="NextShardIterator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamDescriptionModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamArn")
    stream_label: Optional[str] = Field(default=None, alias="StreamLabel")
    stream_status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
    ] = Field(default=None, alias="StreamStatus")
    stream_view_type: Optional[
        Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
    ] = Field(default=None, alias="StreamViewType")
    creation_request_date_time: Optional[datetime] = Field(
        default=None, alias="CreationRequestDateTime"
    )
    table_name: Optional[str] = Field(default=None, alias="TableName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    shards: Optional[List[ShardModel]] = Field(default=None, alias="Shards")
    last_evaluated_shard_id: Optional[str] = Field(
        default=None, alias="LastEvaluatedShardId"
    )


class DescribeStreamOutputModel(BaseModel):
    stream_description: StreamDescriptionModel = Field(alias="StreamDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
