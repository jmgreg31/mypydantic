# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CloseTunnelRequestModel(BaseModel):
    tunnel_id: str = Field(alias="tunnelId")
    delete: Optional[bool] = Field(default=None, alias="delete")


class ConnectionStateModel(BaseModel):
    status: Optional[Literal["CONNECTED", "DISCONNECTED"]] = Field(
        default=None, alias="status"
    )
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class DescribeTunnelRequestModel(BaseModel):
    tunnel_id: str = Field(alias="tunnelId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DestinationConfigModel(BaseModel):
    services: List[str] = Field(alias="services")
    thing_name: Optional[str] = Field(default=None, alias="thingName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ListTunnelsRequestModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TunnelSummaryModel(BaseModel):
    tunnel_id: Optional[str] = Field(default=None, alias="tunnelId")
    tunnel_arn: Optional[str] = Field(default=None, alias="tunnelArn")
    status: Optional[Literal["CLOSED", "OPEN"]] = Field(default=None, alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class TimeoutConfigModel(BaseModel):
    max_lifetime_timeout_minutes: Optional[int] = Field(
        default=None, alias="maxLifetimeTimeoutMinutes"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class OpenTunnelResponseModel(BaseModel):
    tunnel_id: str = Field(alias="tunnelId")
    tunnel_arn: str = Field(alias="tunnelArn")
    source_access_token: str = Field(alias="sourceAccessToken")
    destination_access_token: str = Field(alias="destinationAccessToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateTunnelAccessTokenResponseModel(BaseModel):
    tunnel_arn: str = Field(alias="tunnelArn")
    source_access_token: str = Field(alias="sourceAccessToken")
    destination_access_token: str = Field(alias="destinationAccessToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateTunnelAccessTokenRequestModel(BaseModel):
    tunnel_id: str = Field(alias="tunnelId")
    client_mode: Literal["ALL", "DESTINATION", "SOURCE"] = Field(alias="clientMode")
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="destinationConfig"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class ListTunnelsResponseModel(BaseModel):
    tunnel_summaries: List[TunnelSummaryModel] = Field(alias="tunnelSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OpenTunnelRequestModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="destinationConfig"
    )
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )


class TunnelModel(BaseModel):
    tunnel_id: Optional[str] = Field(default=None, alias="tunnelId")
    tunnel_arn: Optional[str] = Field(default=None, alias="tunnelArn")
    status: Optional[Literal["CLOSED", "OPEN"]] = Field(default=None, alias="status")
    source_connection_state: Optional[ConnectionStateModel] = Field(
        default=None, alias="sourceConnectionState"
    )
    destination_connection_state: Optional[ConnectionStateModel] = Field(
        default=None, alias="destinationConnectionState"
    )
    description: Optional[str] = Field(default=None, alias="description")
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="destinationConfig"
    )
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class DescribeTunnelResponseModel(BaseModel):
    tunnel: TunnelModel = Field(alias="tunnel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
