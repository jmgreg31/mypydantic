# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteThingShadowRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    shadow_name: Optional[str] = Field(default=None, alias="shadowName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetRetainedMessageRequestModel(BaseModel):
    topic: str = Field(alias="topic")


class GetThingShadowRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    shadow_name: Optional[str] = Field(default=None, alias="shadowName")


class ListNamedShadowsForThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    page_size: Optional[int] = Field(default=None, alias="pageSize")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRetainedMessagesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RetainedMessageSummaryModel(BaseModel):
    topic: Optional[str] = Field(default=None, alias="topic")
    payload_size: Optional[int] = Field(default=None, alias="payloadSize")
    qos: Optional[int] = Field(default=None, alias="qos")
    last_modified_time: Optional[int] = Field(default=None, alias="lastModifiedTime")


class PublishRequestModel(BaseModel):
    topic: str = Field(alias="topic")
    qos: Optional[int] = Field(default=None, alias="qos")
    retain: Optional[bool] = Field(default=None, alias="retain")
    payload: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="payload"
    )
    user_properties: Optional[str] = Field(default=None, alias="userProperties")
    payload_format_indicator: Optional[
        Literal["UNSPECIFIED_BYTES", "UTF8_DATA"]
    ] = Field(default=None, alias="payloadFormatIndicator")
    content_type: Optional[str] = Field(default=None, alias="contentType")
    response_topic: Optional[str] = Field(default=None, alias="responseTopic")
    correlation_data: Optional[str] = Field(default=None, alias="correlationData")
    message_expiry: Optional[int] = Field(default=None, alias="messageExpiry")


class UpdateThingShadowRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    payload: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="payload"
    )
    shadow_name: Optional[str] = Field(default=None, alias="shadowName")


class DeleteThingShadowResponseModel(BaseModel):
    payload: Type[StreamingBody] = Field(alias="payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRetainedMessageResponseModel(BaseModel):
    topic: str = Field(alias="topic")
    payload: bytes = Field(alias="payload")
    qos: int = Field(alias="qos")
    last_modified_time: int = Field(alias="lastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetThingShadowResponseModel(BaseModel):
    payload: Type[StreamingBody] = Field(alias="payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNamedShadowsForThingResponseModel(BaseModel):
    results: List[str] = Field(alias="results")
    next_token: str = Field(alias="nextToken")
    timestamp: int = Field(alias="timestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThingShadowResponseModel(BaseModel):
    payload: Type[StreamingBody] = Field(alias="payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRetainedMessagesRequestListRetainedMessagesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRetainedMessagesResponseModel(BaseModel):
    retained_topics: List[RetainedMessageSummaryModel] = Field(alias="retainedTopics")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
