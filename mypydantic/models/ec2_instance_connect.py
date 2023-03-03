# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from typing import Dict, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SendSSHPublicKeyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    instance_os_user: str = Field(alias="InstanceOSUser")
    s_s_hpublic_key: str = Field(alias="SSHPublicKey")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")


class SendSerialConsoleSSHPublicKeyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    s_s_hpublic_key: str = Field(alias="SSHPublicKey")
    serial_port: Optional[int] = Field(default=None, alias="SerialPort")


class SendSSHPublicKeyResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    success: bool = Field(alias="Success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendSerialConsoleSSHPublicKeyResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    success: bool = Field(alias="Success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
