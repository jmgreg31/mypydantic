# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BackupObjectModel(BaseModel):
    name: str = Field(alias="Name")
    object_checksum: str = Field(alias="ObjectChecksum")
    object_checksum_algorithm: Literal["SUMMARY"] = Field(
        alias="ObjectChecksumAlgorithm"
    )
    object_token: str = Field(alias="ObjectToken")
    chunks_count: Optional[int] = Field(default=None, alias="ChunksCount")
    metadata_string: Optional[str] = Field(default=None, alias="MetadataString")


class ChunkModel(BaseModel):
    index: int = Field(alias="Index")
    length: int = Field(alias="Length")
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")
    chunk_token: str = Field(alias="ChunkToken")


class DeleteObjectInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    object_name: str = Field(alias="ObjectName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetChunkInputRequestModel(BaseModel):
    storage_job_id: str = Field(alias="StorageJobId")
    chunk_token: str = Field(alias="ChunkToken")


class GetObjectMetadataInputRequestModel(BaseModel):
    storage_job_id: str = Field(alias="StorageJobId")
    object_token: str = Field(alias="ObjectToken")


class ListChunksInputRequestModel(BaseModel):
    storage_job_id: str = Field(alias="StorageJobId")
    object_token: str = Field(alias="ObjectToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListObjectsInputRequestModel(BaseModel):
    storage_job_id: str = Field(alias="StorageJobId")
    starting_object_name: Optional[str] = Field(
        default=None, alias="StartingObjectName"
    )
    starting_object_prefix: Optional[str] = Field(
        default=None, alias="StartingObjectPrefix"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )


class NotifyObjectCompleteInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    upload_id: str = Field(alias="UploadId")
    object_checksum: str = Field(alias="ObjectChecksum")
    object_checksum_algorithm: Literal["SUMMARY"] = Field(
        alias="ObjectChecksumAlgorithm"
    )
    metadata_string: Optional[str] = Field(default=None, alias="MetadataString")
    metadata_blob: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="MetadataBlob")
    metadata_blob_length: Optional[int] = Field(
        default=None, alias="MetadataBlobLength"
    )
    metadata_blob_checksum: Optional[str] = Field(
        default=None, alias="MetadataBlobChecksum"
    )
    metadata_blob_checksum_algorithm: Optional[Literal["SHA256"]] = Field(
        default=None, alias="MetadataBlobChecksumAlgorithm"
    )


class PutChunkInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    upload_id: str = Field(alias="UploadId")
    chunk_index: int = Field(alias="ChunkIndex")
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")
    length: int = Field(alias="Length")
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")


class PutObjectInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    object_name: str = Field(alias="ObjectName")
    metadata_string: Optional[str] = Field(default=None, alias="MetadataString")
    inline_chunk: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="InlineChunk")
    inline_chunk_length: Optional[int] = Field(default=None, alias="InlineChunkLength")
    inline_chunk_checksum: Optional[str] = Field(
        default=None, alias="InlineChunkChecksum"
    )
    inline_chunk_checksum_algorithm: Optional[str] = Field(
        default=None, alias="InlineChunkChecksumAlgorithm"
    )
    object_checksum: Optional[str] = Field(default=None, alias="ObjectChecksum")
    object_checksum_algorithm: Optional[Literal["SUMMARY"]] = Field(
        default=None, alias="ObjectChecksumAlgorithm"
    )
    throw_on_duplicate: Optional[bool] = Field(default=None, alias="ThrowOnDuplicate")


class StartObjectInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    object_name: str = Field(alias="ObjectName")
    throw_on_duplicate: Optional[bool] = Field(default=None, alias="ThrowOnDuplicate")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChunkOutputModel(BaseModel):
    data: Type[StreamingBody] = Field(alias="Data")
    length: int = Field(alias="Length")
    checksum: str = Field(alias="Checksum")
    checksum_algorithm: Literal["SHA256"] = Field(alias="ChecksumAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectMetadataOutputModel(BaseModel):
    metadata_string: str = Field(alias="MetadataString")
    metadata_blob: Type[StreamingBody] = Field(alias="MetadataBlob")
    metadata_blob_length: int = Field(alias="MetadataBlobLength")
    metadata_blob_checksum: str = Field(alias="MetadataBlobChecksum")
    metadata_blob_checksum_algorithm: Literal["SHA256"] = Field(
        alias="MetadataBlobChecksumAlgorithm"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChunksOutputModel(BaseModel):
    chunk_list: List[ChunkModel] = Field(alias="ChunkList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListObjectsOutputModel(BaseModel):
    object_list: List[BackupObjectModel] = Field(alias="ObjectList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotifyObjectCompleteOutputModel(BaseModel):
    object_checksum: str = Field(alias="ObjectChecksum")
    object_checksum_algorithm: Literal["SUMMARY"] = Field(
        alias="ObjectChecksumAlgorithm"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutChunkOutputModel(BaseModel):
    chunk_checksum: str = Field(alias="ChunkChecksum")
    chunk_checksum_algorithm: Literal["SHA256"] = Field(alias="ChunkChecksumAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectOutputModel(BaseModel):
    inline_chunk_checksum: str = Field(alias="InlineChunkChecksum")
    inline_chunk_checksum_algorithm: Literal["SHA256"] = Field(
        alias="InlineChunkChecksumAlgorithm"
    )
    object_checksum: str = Field(alias="ObjectChecksum")
    object_checksum_algorithm: Literal["SUMMARY"] = Field(
        alias="ObjectChecksumAlgorithm"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartObjectOutputModel(BaseModel):
    upload_id: str = Field(alias="UploadId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
