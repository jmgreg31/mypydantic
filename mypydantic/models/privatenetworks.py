# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcknowledgeOrderReceiptRequestModel(BaseModel):
    order_arn: str = Field(alias="orderArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ActivateDeviceIdentifierRequestModel(BaseModel):
    device_identifier_arn: str = Field(alias="deviceIdentifierArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeviceIdentifierModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    device_identifier_arn: Optional[str] = Field(
        default=None, alias="deviceIdentifierArn"
    )
    iccid: Optional[str] = Field(default=None, alias="iccid")
    imsi: Optional[str] = Field(default=None, alias="imsi")
    network_arn: Optional[str] = Field(default=None, alias="networkArn")
    order_arn: Optional[str] = Field(default=None, alias="orderArn")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    traffic_group_arn: Optional[str] = Field(default=None, alias="trafficGroupArn")
    vendor: Optional[str] = Field(default=None, alias="vendor")


class AddressModel(BaseModel):
    city: str = Field(alias="city")
    country: str = Field(alias="country")
    name: str = Field(alias="name")
    postal_code: str = Field(alias="postalCode")
    state_or_province: str = Field(alias="stateOrProvince")
    street1: str = Field(alias="street1")
    company: Optional[str] = Field(default=None, alias="company")
    phone_number: Optional[str] = Field(default=None, alias="phoneNumber")
    street2: Optional[str] = Field(default=None, alias="street2")
    street3: Optional[str] = Field(default=None, alias="street3")


class PositionModel(BaseModel):
    elevation: Optional[float] = Field(default=None, alias="elevation")
    elevation_reference: Optional[Literal["AGL", "AMSL"]] = Field(
        default=None, alias="elevationReference"
    )
    elevation_unit: Optional[Literal["FEET"]] = Field(
        default=None, alias="elevationUnit"
    )
    latitude: Optional[float] = Field(default=None, alias="latitude")
    longitude: Optional[float] = Field(default=None, alias="longitude")


class CreateNetworkRequestModel(BaseModel):
    network_name: str = Field(alias="networkName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class NetworkModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    network_name: str = Field(alias="networkName")
    status: Literal[
        "AVAILABLE", "CREATED", "DELETED", "DEPROVISIONING", "PROVISIONING"
    ] = Field(alias="status")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    description: Optional[str] = Field(default=None, alias="description")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class DeactivateDeviceIdentifierRequestModel(BaseModel):
    device_identifier_arn: str = Field(alias="deviceIdentifierArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteNetworkRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteNetworkSiteRequestModel(BaseModel):
    network_site_arn: str = Field(alias="networkSiteArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetDeviceIdentifierRequestModel(BaseModel):
    device_identifier_arn: str = Field(alias="deviceIdentifierArn")


class GetNetworkRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")


class GetNetworkResourceRequestModel(BaseModel):
    network_resource_arn: str = Field(alias="networkResourceArn")


class GetNetworkSiteRequestModel(BaseModel):
    network_site_arn: str = Field(alias="networkSiteArn")


class GetOrderRequestModel(BaseModel):
    order_arn: str = Field(alias="orderArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDeviceIdentifiersRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[
        Mapping[Literal["ORDER", "STATUS", "TRAFFIC_GROUP"], Sequence[str]]
    ] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    start_token: Optional[str] = Field(default=None, alias="startToken")


class ListNetworkResourcesRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[Mapping[Literal["ORDER", "STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    start_token: Optional[str] = Field(default=None, alias="startToken")


class ListNetworkSitesRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    start_token: Optional[str] = Field(default=None, alias="startToken")


class ListNetworksRequestModel(BaseModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    start_token: Optional[str] = Field(default=None, alias="startToken")


class ListOrdersRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[
        Mapping[Literal["NETWORK_SITE", "STATUS"], Sequence[str]]
    ] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    start_token: Optional[str] = Field(default=None, alias="startToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class NameValuePairModel(BaseModel):
    name: str = Field(alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class TrackingInformationModel(BaseModel):
    tracking_number: Optional[str] = Field(default=None, alias="trackingNumber")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateNetworkSiteRequestModel(BaseModel):
    network_site_arn: str = Field(alias="networkSiteArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PingResponseModel(BaseModel):
    status: str = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivateDeviceIdentifierResponseModel(BaseModel):
    device_identifier: DeviceIdentifierModel = Field(alias="deviceIdentifier")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeactivateDeviceIdentifierResponseModel(BaseModel):
    device_identifier: DeviceIdentifierModel = Field(alias="deviceIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceIdentifierResponseModel(BaseModel):
    device_identifier: DeviceIdentifierModel = Field(alias="deviceIdentifier")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceIdentifiersResponseModel(BaseModel):
    device_identifiers: List[DeviceIdentifierModel] = Field(alias="deviceIdentifiers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivateNetworkSiteRequestModel(BaseModel):
    network_site_arn: str = Field(alias="networkSiteArn")
    shipping_address: AddressModel = Field(alias="shippingAddress")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ReturnInformationModel(BaseModel):
    replacement_order_arn: Optional[str] = Field(
        default=None, alias="replacementOrderArn"
    )
    return_reason: Optional[str] = Field(default=None, alias="returnReason")
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="shippingAddress"
    )
    shipping_label: Optional[str] = Field(default=None, alias="shippingLabel")


class StartNetworkResourceUpdateRequestModel(BaseModel):
    network_resource_arn: str = Field(alias="networkResourceArn")
    update_type: Literal["REPLACE", "RETURN"] = Field(alias="updateType")
    return_reason: Optional[str] = Field(default=None, alias="returnReason")
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="shippingAddress"
    )


class ConfigureAccessPointRequestModel(BaseModel):
    access_point_arn: str = Field(alias="accessPointArn")
    cpi_secret_key: Optional[str] = Field(default=None, alias="cpiSecretKey")
    cpi_user_id: Optional[str] = Field(default=None, alias="cpiUserId")
    cpi_user_password: Optional[str] = Field(default=None, alias="cpiUserPassword")
    cpi_username: Optional[str] = Field(default=None, alias="cpiUsername")
    position: Optional[PositionModel] = Field(default=None, alias="position")


class CreateNetworkResponseModel(BaseModel):
    network: NetworkModel = Field(alias="network")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNetworkResponseModel(BaseModel):
    network: NetworkModel = Field(alias="network")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkResponseModel(BaseModel):
    network: NetworkModel = Field(alias="network")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworksResponseModel(BaseModel):
    networks: List[NetworkModel] = Field(alias="networks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[
        Mapping[Literal["ORDER", "STATUS", "TRAFFIC_GROUP"], Sequence[str]]
    ] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNetworkResourcesRequestListNetworkResourcesPaginateModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[Mapping[Literal["ORDER", "STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNetworkSitesRequestListNetworkSitesPaginateModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNetworksRequestListNetworksPaginateModel(BaseModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrdersRequestListOrdersPaginateModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    filters: Optional[
        Mapping[Literal["NETWORK_SITE", "STATUS"], Sequence[str]]
    ] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class NetworkResourceDefinitionModel(BaseModel):
    count: int = Field(alias="count")
    type: Literal["DEVICE_IDENTIFIER", "RADIO_UNIT"] = Field(alias="type")
    options: Optional[List[NameValuePairModel]] = Field(default=None, alias="options")


class OrderModel(BaseModel):
    acknowledgment_status: Optional[
        Literal["ACKNOWLEDGED", "ACKNOWLEDGING", "UNACKNOWLEDGED"]
    ] = Field(default=None, alias="acknowledgmentStatus")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    network_arn: Optional[str] = Field(default=None, alias="networkArn")
    network_site_arn: Optional[str] = Field(default=None, alias="networkSiteArn")
    order_arn: Optional[str] = Field(default=None, alias="orderArn")
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="shippingAddress"
    )
    tracking_information: Optional[List[TrackingInformationModel]] = Field(
        default=None, alias="trackingInformation"
    )


class NetworkResourceModel(BaseModel):
    attributes: Optional[List[NameValuePairModel]] = Field(
        default=None, alias="attributes"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    description: Optional[str] = Field(default=None, alias="description")
    health: Optional[Literal["HEALTHY", "INITIAL", "UNHEALTHY"]] = Field(
        default=None, alias="health"
    )
    model: Optional[str] = Field(default=None, alias="model")
    network_arn: Optional[str] = Field(default=None, alias="networkArn")
    network_resource_arn: Optional[str] = Field(
        default=None, alias="networkResourceArn"
    )
    network_site_arn: Optional[str] = Field(default=None, alias="networkSiteArn")
    order_arn: Optional[str] = Field(default=None, alias="orderArn")
    position: Optional[PositionModel] = Field(default=None, alias="position")
    return_information: Optional[ReturnInformationModel] = Field(
        default=None, alias="returnInformation"
    )
    serial_number: Optional[str] = Field(default=None, alias="serialNumber")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATING_SHIPPING_LABEL",
            "DELETED",
            "DELETING",
            "PENDING",
            "PENDING_RETURN",
            "PROVISIONED",
            "PROVISIONING",
            "SHIPPED",
        ]
    ] = Field(default=None, alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    type: Optional[Literal["RADIO_UNIT"]] = Field(default=None, alias="type")
    vendor: Optional[str] = Field(default=None, alias="vendor")


class SitePlanModel(BaseModel):
    options: Optional[List[NameValuePairModel]] = Field(default=None, alias="options")
    resource_definitions: Optional[List[NetworkResourceDefinitionModel]] = Field(
        default=None, alias="resourceDefinitions"
    )


class AcknowledgeOrderReceiptResponseModel(BaseModel):
    order: OrderModel = Field(alias="order")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrderResponseModel(BaseModel):
    order: OrderModel = Field(alias="order")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrdersResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    orders: List[OrderModel] = Field(alias="orders")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigureAccessPointResponseModel(BaseModel):
    access_point: NetworkResourceModel = Field(alias="accessPoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkResourceResponseModel(BaseModel):
    network_resource: NetworkResourceModel = Field(alias="networkResource")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworkResourcesResponseModel(BaseModel):
    network_resources: List[NetworkResourceModel] = Field(alias="networkResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartNetworkResourceUpdateResponseModel(BaseModel):
    network_resource: NetworkResourceModel = Field(alias="networkResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkSiteRequestModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    network_site_name: str = Field(alias="networkSiteName")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    availability_zone_id: Optional[str] = Field(
        default=None, alias="availabilityZoneId"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    pending_plan: Optional[SitePlanModel] = Field(default=None, alias="pendingPlan")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class NetworkSiteModel(BaseModel):
    network_arn: str = Field(alias="networkArn")
    network_site_arn: str = Field(alias="networkSiteArn")
    network_site_name: str = Field(alias="networkSiteName")
    status: Literal[
        "AVAILABLE", "CREATED", "DELETED", "DEPROVISIONING", "PROVISIONING"
    ] = Field(alias="status")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    availability_zone_id: Optional[str] = Field(
        default=None, alias="availabilityZoneId"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    current_plan: Optional[SitePlanModel] = Field(default=None, alias="currentPlan")
    description: Optional[str] = Field(default=None, alias="description")
    pending_plan: Optional[SitePlanModel] = Field(default=None, alias="pendingPlan")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class UpdateNetworkSitePlanRequestModel(BaseModel):
    network_site_arn: str = Field(alias="networkSiteArn")
    pending_plan: SitePlanModel = Field(alias="pendingPlan")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ActivateNetworkSiteResponseModel(BaseModel):
    network_site: NetworkSiteModel = Field(alias="networkSite")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkSiteResponseModel(BaseModel):
    network_site: NetworkSiteModel = Field(alias="networkSite")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNetworkSiteResponseModel(BaseModel):
    network_site: NetworkSiteModel = Field(alias="networkSite")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkSiteResponseModel(BaseModel):
    network_site: NetworkSiteModel = Field(alias="networkSite")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworkSitesResponseModel(BaseModel):
    network_sites: List[NetworkSiteModel] = Field(alias="networkSites")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNetworkSiteResponseModel(BaseModel):
    network_site: NetworkSiteModel = Field(alias="networkSite")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
