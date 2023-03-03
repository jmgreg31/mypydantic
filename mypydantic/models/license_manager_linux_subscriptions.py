# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    operator: Optional[Literal["Contains", "Equal", "NotEqual"]] = Field(
        default=None, alias="Operator"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class LinuxSubscriptionsDiscoverySettingsModel(BaseModel):
    organization_integration: Literal["Disabled", "Enabled"] = Field(
        alias="OrganizationIntegration"
    )
    source_regions: List[str] = Field(alias="SourceRegions")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class InstanceModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountID")
    ami_id: Optional[str] = Field(default=None, alias="AmiId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceID")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    last_updated_time: Optional[str] = Field(default=None, alias="LastUpdatedTime")
    product_code: Optional[List[str]] = Field(default=None, alias="ProductCode")
    region: Optional[str] = Field(default=None, alias="Region")
    status: Optional[str] = Field(default=None, alias="Status")
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    usage_operation: Optional[str] = Field(default=None, alias="UsageOperation")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class SubscriptionModel(BaseModel):
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")


class ListLinuxSubscriptionInstancesRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLinuxSubscriptionsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateServiceSettingsRequestModel(BaseModel):
    linux_subscriptions_discovery: Literal["Disabled", "Enabled"] = Field(
        alias="LinuxSubscriptionsDiscovery"
    )
    linux_subscriptions_discovery_settings: LinuxSubscriptionsDiscoverySettingsModel = (
        Field(alias="LinuxSubscriptionsDiscoverySettings")
    )
    allow_update: Optional[bool] = Field(default=None, alias="AllowUpdate")


class GetServiceSettingsResponseModel(BaseModel):
    home_regions: List[str] = Field(alias="HomeRegions")
    linux_subscriptions_discovery: Literal["Disabled", "Enabled"] = Field(
        alias="LinuxSubscriptionsDiscovery"
    )
    linux_subscriptions_discovery_settings: LinuxSubscriptionsDiscoverySettingsModel = (
        Field(alias="LinuxSubscriptionsDiscoverySettings")
    )
    status: Literal["Completed", "Failed", "InProgress", "Successful"] = Field(
        alias="Status"
    )
    status_message: Dict[str, str] = Field(alias="StatusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceSettingsResponseModel(BaseModel):
    home_regions: List[str] = Field(alias="HomeRegions")
    linux_subscriptions_discovery: Literal["Disabled", "Enabled"] = Field(
        alias="LinuxSubscriptionsDiscovery"
    )
    linux_subscriptions_discovery_settings: LinuxSubscriptionsDiscoverySettingsModel = (
        Field(alias="LinuxSubscriptionsDiscoverySettings")
    )
    status: Literal["Completed", "Failed", "InProgress", "Successful"] = Field(
        alias="Status"
    )
    status_message: Dict[str, str] = Field(alias="StatusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLinuxSubscriptionInstancesResponseModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLinuxSubscriptionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    subscriptions: List[SubscriptionModel] = Field(alias="Subscriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
