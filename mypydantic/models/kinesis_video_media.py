# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class StartSelectorModel(BaseModel):
    start_selector_type: Literal[
        "CONTINUATION_TOKEN",
        "EARLIEST",
        "FRAGMENT_NUMBER",
        "NOW",
        "PRODUCER_TIMESTAMP",
        "SERVER_TIMESTAMP",
    ] = Field(alias="StartSelectorType")
    after_fragment_number: Optional[str] = Field(
        default=None, alias="AfterFragmentNumber"
    )
    start_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartTimestamp"
    )
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetMediaInputRequestModel(BaseModel):
    start_selector: StartSelectorModel = Field(alias="StartSelector")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class GetMediaOutputModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    payload: Type[StreamingBody] = Field(alias="Payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
