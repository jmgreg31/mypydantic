# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, Optional, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GetLatestConfigurationRequestModel(BaseModel):
    configuration_token: str = Field(alias="ConfigurationToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class StartConfigurationSessionRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    configuration_profile_identifier: str = Field(
        alias="ConfigurationProfileIdentifier"
    )
    required_minimum_poll_interval_in_seconds: Optional[int] = Field(
        default=None, alias="RequiredMinimumPollIntervalInSeconds"
    )


class GetLatestConfigurationResponseModel(BaseModel):
    next_poll_configuration_token: str = Field(alias="NextPollConfigurationToken")
    next_poll_interval_in_seconds: int = Field(alias="NextPollIntervalInSeconds")
    content_type: str = Field(alias="ContentType")
    configuration: Type[StreamingBody] = Field(alias="Configuration")
    version_label: str = Field(alias="VersionLabel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartConfigurationSessionResponseModel(BaseModel):
    initial_configuration_token: str = Field(alias="InitialConfigurationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
