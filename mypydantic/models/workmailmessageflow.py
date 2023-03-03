# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Dict, Optional, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GetRawMessageContentRequestModel(BaseModel):
    message_id: str = Field(alias="messageId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class S3ReferenceModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")
    object_version: Optional[str] = Field(default=None, alias="objectVersion")


class GetRawMessageContentResponseModel(BaseModel):
    message_content: Type[StreamingBody] = Field(alias="messageContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RawMessageContentModel(BaseModel):
    s3_reference: S3ReferenceModel = Field(alias="s3Reference")


class PutRawMessageContentRequestModel(BaseModel):
    message_id: str = Field(alias="messageId")
    content: RawMessageContentModel = Field(alias="content")
