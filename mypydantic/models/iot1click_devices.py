# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ClaimDevicesByClaimCodeRequestModel(BaseModel):
    claim_code: str = Field(alias="ClaimCode")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeDeviceRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class DeviceDescriptionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    remaining_life: Optional[float] = Field(default=None, alias="RemainingLife")
    type: Optional[str] = Field(default=None, alias="Type")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DeviceModel(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(default=None, alias="Attributes")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    type: Optional[str] = Field(default=None, alias="Type")


class DeviceMethodModel(BaseModel):
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    method_name: Optional[str] = Field(default=None, alias="MethodName")


class FinalizeDeviceClaimRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GetDeviceMethodsRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class InitiateDeviceClaimRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDeviceEventsRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    from_time_stamp: Union[datetime, str] = Field(alias="FromTimeStamp")
    to_time_stamp: Union[datetime, str] = Field(alias="ToTimeStamp")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDevicesRequestModel(BaseModel):
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UnclaimDeviceRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDeviceStateRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ClaimDevicesByClaimCodeResponseModel(BaseModel):
    claim_code: str = Field(alias="ClaimCode")
    total: int = Field(alias="Total")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FinalizeDeviceClaimResponseModel(BaseModel):
    state: str = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateDeviceClaimResponseModel(BaseModel):
    state: str = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvokeDeviceMethodResponseModel(BaseModel):
    device_method_response: str = Field(alias="DeviceMethodResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnclaimDeviceResponseModel(BaseModel):
    state: str = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDeviceResponseModel(BaseModel):
    device_description: DeviceDescriptionModel = Field(alias="DeviceDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesResponseModel(BaseModel):
    devices: List[DeviceDescriptionModel] = Field(alias="Devices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceEventModel(BaseModel):
    device: Optional[DeviceModel] = Field(default=None, alias="Device")
    std_event: Optional[str] = Field(default=None, alias="StdEvent")


class GetDeviceMethodsResponseModel(BaseModel):
    device_methods: List[DeviceMethodModel] = Field(alias="DeviceMethods")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvokeDeviceMethodRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    device_method: Optional[DeviceMethodModel] = Field(
        default=None, alias="DeviceMethod"
    )
    device_method_parameters: Optional[str] = Field(
        default=None, alias="DeviceMethodParameters"
    )


class ListDeviceEventsRequestListDeviceEventsPaginateModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    from_time_stamp: Union[datetime, str] = Field(alias="FromTimeStamp")
    to_time_stamp: Union[datetime, str] = Field(alias="ToTimeStamp")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicesRequestListDevicesPaginateModel(BaseModel):
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceEventsResponseModel(BaseModel):
    events: List[DeviceEventModel] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
