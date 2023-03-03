# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GetIceServerConfigRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    service: Optional[Literal["TURN"]] = Field(default=None, alias="Service")
    username: Optional[str] = Field(default=None, alias="Username")


class IceServerModel(BaseModel):
    uris: Optional[List[str]] = Field(default=None, alias="Uris")
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    ttl: Optional[int] = Field(default=None, alias="Ttl")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SendAlexaOfferToMasterRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    sender_client_id: str = Field(alias="SenderClientId")
    message_payload: str = Field(alias="MessagePayload")


class GetIceServerConfigResponseModel(BaseModel):
    ice_server_list: List[IceServerModel] = Field(alias="IceServerList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendAlexaOfferToMasterResponseModel(BaseModel):
    answer: str = Field(alias="Answer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
