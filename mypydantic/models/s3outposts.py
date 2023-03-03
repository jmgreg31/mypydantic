# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateEndpointRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")
    subnet_id: str = Field(alias="SubnetId")
    security_group_id: str = Field(alias="SecurityGroupId")
    access_type: Optional[Literal["CustomerOwnedIp", "Private"]] = Field(
        default=None, alias="AccessType"
    )
    customer_owned_ipv4_pool: Optional[str] = Field(
        default=None, alias="CustomerOwnedIpv4Pool"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteEndpointRequestModel(BaseModel):
    endpoint_id: str = Field(alias="EndpointId")
    outpost_id: str = Field(alias="OutpostId")


class NetworkInterfaceModel(BaseModel):
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEndpointsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListOutpostsWithS3RequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OutpostModel(BaseModel):
    outpost_arn: Optional[str] = Field(default=None, alias="OutpostArn")
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    capacity_in_bytes: Optional[int] = Field(default=None, alias="CapacityInBytes")


class ListSharedEndpointsRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class CreateEndpointResultModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointModel(BaseModel):
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    outposts_id: Optional[str] = Field(default=None, alias="OutpostsId")
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    status: Optional[Literal["Available", "Deleting", "Pending"]] = Field(
        default=None, alias="Status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="NetworkInterfaces"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")
    access_type: Optional[Literal["CustomerOwnedIp", "Private"]] = Field(
        default=None, alias="AccessType"
    )
    customer_owned_ipv4_pool: Optional[str] = Field(
        default=None, alias="CustomerOwnedIpv4Pool"
    )


class ListEndpointsRequestListEndpointsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOutpostsWithS3RequestListOutpostsWithS3PaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSharedEndpointsRequestListSharedEndpointsPaginateModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOutpostsWithS3ResultModel(BaseModel):
    outposts: List[OutpostModel] = Field(alias="Outposts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointsResultModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSharedEndpointsResultModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
