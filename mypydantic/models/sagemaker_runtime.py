# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from typing import Any, Dict, IO, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class InvokeEndpointAsyncInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    input_location: str = Field(alias="InputLocation")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    accept: Optional[str] = Field(default=None, alias="Accept")
    custom_attributes: Optional[str] = Field(default=None, alias="CustomAttributes")
    inference_id: Optional[str] = Field(default=None, alias="InferenceId")
    request_ttl_seconds: Optional[int] = Field(default=None, alias="RequestTTLSeconds")
    invocation_timeout_seconds: Optional[int] = Field(
        default=None, alias="InvocationTimeoutSeconds"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class InvokeEndpointInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Body")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    accept: Optional[str] = Field(default=None, alias="Accept")
    custom_attributes: Optional[str] = Field(default=None, alias="CustomAttributes")
    target_model: Optional[str] = Field(default=None, alias="TargetModel")
    target_variant: Optional[str] = Field(default=None, alias="TargetVariant")
    target_container_hostname: Optional[str] = Field(
        default=None, alias="TargetContainerHostname"
    )
    inference_id: Optional[str] = Field(default=None, alias="InferenceId")
    enable_explanations: Optional[str] = Field(default=None, alias="EnableExplanations")


class InvokeEndpointAsyncOutputModel(BaseModel):
    inference_id: str = Field(alias="InferenceId")
    output_location: str = Field(alias="OutputLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvokeEndpointOutputModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    content_type: str = Field(alias="ContentType")
    invoked_production_variant: str = Field(alias="InvokedProductionVariant")
    custom_attributes: str = Field(alias="CustomAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
