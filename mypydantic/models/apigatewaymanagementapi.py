# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class IdentityModel(BaseModel):
    source_ip: str = Field(alias="SourceIp")
    user_agent: str = Field(alias="UserAgent")


class PostToConnectionRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")
    connection_id: str = Field(alias="ConnectionId")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectionResponseModel(BaseModel):
    connected_at: datetime = Field(alias="ConnectedAt")
    identity: IdentityModel = Field(alias="Identity")
    last_active_at: datetime = Field(alias="LastActiveAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
