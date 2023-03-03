# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BlockModel(BaseModel):
    block_index: Optional[int] = Field(default=None, alias="BlockIndex")
    block_token: Optional[str] = Field(default=None, alias="BlockToken")


class ChangedBlockModel(BaseModel):
    block_index: Optional[int] = Field(default=None, alias="BlockIndex")
    first_block_token: Optional[str] = Field(default=None, alias="FirstBlockToken")
    second_block_token: Optional[str] = Field(default=None, alias="SecondBlockToken")


class CompleteSnapshotRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    changed_blocks_count: int = Field(alias="ChangedBlocksCount")
    checksum: Optional[str] = Field(default=None, alias="Checksum")
    checksum_algorithm: Optional[Literal["SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_aggregation_method: Optional[Literal["LINEAR"]] = Field(
        default=None, alias="ChecksumAggregationMethod"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetSnapshotBlockRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    block_index: int = Field(alias="BlockIndex")
    block_token: str = Field(alias="BlockToken")


class ListChangedBlocksRequestModel(BaseModel):
    second_snapshot_id: str = Field(alias="SecondSnapshotId")
    first_snapshot_id: Optional[str] = Field(default=None, alias="FirstSnapshotId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    starting_block_index: Optional[int] = Field(
        default=None, alias="StartingBlockIndex"
    )


class ListSnapshotBlocksRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    starting_block_index: Optional[int] = Field(
        default=None, alias="StartingBlockIndex"
    )


class PutSnapshotBlockRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    block_index: int = Field(alias="BlockIndex")
    block_data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="BlockData"
    )
    data_length: int = Field(alias="DataLength")
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")
    progress: Optional[int] = Field(default=None, alias="Progress")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CompleteSnapshotResponseModel(BaseModel):
    status: Literal["completed", "error", "pending"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnapshotBlockResponseModel(BaseModel):
    data_length: int = Field(alias="DataLength")
    block_data: Type[StreamingBody] = Field(alias="BlockData")
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChangedBlocksResponseModel(BaseModel):
    changed_blocks: List[ChangedBlockModel] = Field(alias="ChangedBlocks")
    expiry_time: datetime = Field(alias="ExpiryTime")
    volume_size: int = Field(alias="VolumeSize")
    block_size: int = Field(alias="BlockSize")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSnapshotBlocksResponseModel(BaseModel):
    blocks: List[BlockModel] = Field(alias="Blocks")
    expiry_time: datetime = Field(alias="ExpiryTime")
    volume_size: int = Field(alias="VolumeSize")
    block_size: int = Field(alias="BlockSize")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSnapshotBlockResponseModel(BaseModel):
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSnapshotRequestModel(BaseModel):
    volume_size: int = Field(alias="VolumeSize")
    parent_snapshot_id: Optional[str] = Field(default=None, alias="ParentSnapshotId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class StartSnapshotResponseModel(BaseModel):
    description: str = Field(alias="Description")
    snapshot_id: str = Field(alias="SnapshotId")
    owner_id: str = Field(alias="OwnerId")
    status: Literal["completed", "error", "pending"] = Field(alias="Status")
    start_time: datetime = Field(alias="StartTime")
    volume_size: int = Field(alias="VolumeSize")
    block_size: int = Field(alias="BlockSize")
    tags: List[TagModel] = Field(alias="Tags")
    parent_snapshot_id: str = Field(alias="ParentSnapshotId")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
