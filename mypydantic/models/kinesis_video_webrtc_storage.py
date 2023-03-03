# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from typing import Dict

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class JoinStorageSessionInputRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
