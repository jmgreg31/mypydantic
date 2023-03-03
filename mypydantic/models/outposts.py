# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressModel(BaseModel):
    address_line1: str = Field(alias="AddressLine1")
    city: str = Field(alias="City")
    state_or_region: str = Field(alias="StateOrRegion")
    postal_code: str = Field(alias="PostalCode")
    country_code: str = Field(alias="CountryCode")
    contact_name: Optional[str] = Field(default=None, alias="ContactName")
    contact_phone_number: Optional[str] = Field(
        default=None, alias="ContactPhoneNumber"
    )
    address_line2: Optional[str] = Field(default=None, alias="AddressLine2")
    address_line3: Optional[str] = Field(default=None, alias="AddressLine3")
    district_or_county: Optional[str] = Field(default=None, alias="DistrictOrCounty")
    municipality: Optional[str] = Field(default=None, alias="Municipality")


class AssetLocationModel(BaseModel):
    rack_elevation: Optional[float] = Field(default=None, alias="RackElevation")


class ComputeAttributesModel(BaseModel):
    host_id: Optional[str] = Field(default=None, alias="HostId")
    state: Optional[Literal["ACTIVE", "ISOLATED", "RETIRING"]] = Field(
        default=None, alias="State"
    )


class CancelOrderInputRequestModel(BaseModel):
    order_id: str = Field(alias="OrderId")


class EC2CapacityModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    max_size: Optional[str] = Field(default=None, alias="MaxSize")
    quantity: Optional[str] = Field(default=None, alias="Quantity")


class ConnectionDetailsModel(BaseModel):
    client_public_key: Optional[str] = Field(default=None, alias="ClientPublicKey")
    server_public_key: Optional[str] = Field(default=None, alias="ServerPublicKey")
    server_endpoint: Optional[str] = Field(default=None, alias="ServerEndpoint")
    client_tunnel_address: Optional[str] = Field(
        default=None, alias="ClientTunnelAddress"
    )
    server_tunnel_address: Optional[str] = Field(
        default=None, alias="ServerTunnelAddress"
    )
    allowed_ips: Optional[List[str]] = Field(default=None, alias="AllowedIps")


class LineItemRequestModel(BaseModel):
    catalog_item_id: Optional[str] = Field(default=None, alias="CatalogItemId")
    quantity: Optional[int] = Field(default=None, alias="Quantity")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateOutpostInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    site_id: str = Field(alias="SiteId")
    description: Optional[str] = Field(default=None, alias="Description")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    availability_zone_id: Optional[str] = Field(
        default=None, alias="AvailabilityZoneId"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    supported_hardware_type: Optional[Literal["RACK", "SERVER"]] = Field(
        default=None, alias="SupportedHardwareType"
    )


class OutpostModel(BaseModel):
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    outpost_arn: Optional[str] = Field(default=None, alias="OutpostArn")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    life_cycle_status: Optional[str] = Field(default=None, alias="LifeCycleStatus")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    availability_zone_id: Optional[str] = Field(
        default=None, alias="AvailabilityZoneId"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    site_arn: Optional[str] = Field(default=None, alias="SiteArn")
    supported_hardware_type: Optional[Literal["RACK", "SERVER"]] = Field(
        default=None, alias="SupportedHardwareType"
    )


class RackPhysicalPropertiesModel(BaseModel):
    power_draw_kva: Optional[
        Literal["POWER_10_KVA", "POWER_15_KVA", "POWER_30_KVA", "POWER_5_KVA"]
    ] = Field(default=None, alias="PowerDrawKva")
    power_phase: Optional[Literal["SINGLE_PHASE", "THREE_PHASE"]] = Field(
        default=None, alias="PowerPhase"
    )
    power_connector: Optional[
        Literal["AH530P7W", "AH532P6W", "IEC309", "L6_30P"]
    ] = Field(default=None, alias="PowerConnector")
    power_feed_drop: Optional[Literal["ABOVE_RACK", "BELOW_RACK"]] = Field(
        default=None, alias="PowerFeedDrop"
    )
    uplink_gbps: Optional[
        Literal["UPLINK_100G", "UPLINK_10G", "UPLINK_1G", "UPLINK_40G"]
    ] = Field(default=None, alias="UplinkGbps")
    uplink_count: Optional[
        Literal[
            "UPLINK_COUNT_1",
            "UPLINK_COUNT_12",
            "UPLINK_COUNT_16",
            "UPLINK_COUNT_2",
            "UPLINK_COUNT_3",
            "UPLINK_COUNT_4",
            "UPLINK_COUNT_5",
            "UPLINK_COUNT_6",
            "UPLINK_COUNT_7",
            "UPLINK_COUNT_8",
        ]
    ] = Field(default=None, alias="UplinkCount")
    fiber_optic_cable_type: Optional[Literal["MULTI_MODE", "SINGLE_MODE"]] = Field(
        default=None, alias="FiberOpticCableType"
    )
    optical_standard: Optional[
        Literal[
            "OPTIC_1000BASE_LX",
            "OPTIC_1000BASE_SX",
            "OPTIC_100GBASE_CWDM4",
            "OPTIC_100GBASE_LR4",
            "OPTIC_100GBASE_SR4",
            "OPTIC_100G_PSM4_MSA",
            "OPTIC_10GBASE_IR",
            "OPTIC_10GBASE_LR",
            "OPTIC_10GBASE_SR",
            "OPTIC_40GBASE_ESR",
            "OPTIC_40GBASE_IR4_LR4L",
            "OPTIC_40GBASE_LR4",
            "OPTIC_40GBASE_SR",
        ]
    ] = Field(default=None, alias="OpticalStandard")
    maximum_supported_weight_lbs: Optional[
        Literal[
            "MAX_1400_LBS", "MAX_1600_LBS", "MAX_1800_LBS", "MAX_2000_LBS", "NO_LIMIT"
        ]
    ] = Field(default=None, alias="MaximumSupportedWeightLbs")


class DeleteOutpostInputRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")


class DeleteSiteInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")


class GetCatalogItemInputRequestModel(BaseModel):
    catalog_item_id: str = Field(alias="CatalogItemId")


class GetConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class GetOrderInputRequestModel(BaseModel):
    order_id: str = Field(alias="OrderId")


class GetOutpostInputRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")


class GetOutpostInstanceTypesInputRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class InstanceTypeItemModel(BaseModel):
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")


class GetSiteAddressInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")
    address_type: Literal["OPERATING_ADDRESS", "SHIPPING_ADDRESS"] = Field(
        alias="AddressType"
    )


class GetSiteInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")


class LineItemAssetInformationModel(BaseModel):
    asset_id: Optional[str] = Field(default=None, alias="AssetId")
    mac_address_list: Optional[List[str]] = Field(default=None, alias="MacAddressList")


class ShipmentInformationModel(BaseModel):
    shipment_tracking_number: Optional[str] = Field(
        default=None, alias="ShipmentTrackingNumber"
    )
    shipment_carrier: Optional[Literal["DBS", "DHL", "FEDEX", "UPS"]] = Field(
        default=None, alias="ShipmentCarrier"
    )


class ListAssetsInputRequestModel(BaseModel):
    outpost_identifier: str = Field(alias="OutpostIdentifier")
    host_id_filter: Optional[Sequence[str]] = Field(default=None, alias="HostIdFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    status_filter: Optional[Sequence[Literal["ACTIVE", "RETIRING"]]] = Field(
        default=None, alias="StatusFilter"
    )


class ListCatalogItemsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    item_class_filter: Optional[Sequence[Literal["RACK", "SERVER"]]] = Field(
        default=None, alias="ItemClassFilter"
    )
    supported_storage_filter: Optional[Sequence[Literal["EBS", "S3"]]] = Field(
        default=None, alias="SupportedStorageFilter"
    )
    ec2_family_filter: Optional[Sequence[str]] = Field(
        default=None, alias="EC2FamilyFilter"
    )


class ListOrdersInputRequestModel(BaseModel):
    outpost_identifier_filter: Optional[str] = Field(
        default=None, alias="OutpostIdentifierFilter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OrderSummaryModel(BaseModel):
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")
    order_id: Optional[str] = Field(default=None, alias="OrderId")
    order_type: Optional[Literal["OUTPOST", "REPLACEMENT"]] = Field(
        default=None, alias="OrderType"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "ERROR",
            "FULFILLED",
            "INSTALLING",
            "IN_PROGRESS",
            "PENDING",
            "PREPARING",
            "PROCESSING",
            "RECEIVED",
        ]
    ] = Field(default=None, alias="Status")
    line_item_counts_by_status: Optional[
        Dict[
            Literal[
                "BUILDING",
                "CANCELLED",
                "DELIVERED",
                "ERROR",
                "INSTALLED",
                "INSTALLING",
                "PREPARING",
                "REPLACED",
                "SHIPPED",
            ],
            int,
        ]
    ] = Field(default=None, alias="LineItemCountsByStatus")
    order_submission_date: Optional[datetime] = Field(
        default=None, alias="OrderSubmissionDate"
    )
    order_fulfilled_date: Optional[datetime] = Field(
        default=None, alias="OrderFulfilledDate"
    )


class ListOutpostsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    life_cycle_status_filter: Optional[Sequence[str]] = Field(
        default=None, alias="LifeCycleStatusFilter"
    )
    availability_zone_filter: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZoneFilter"
    )
    availability_zone_id_filter: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZoneIdFilter"
    )


class ListSitesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    operating_address_country_code_filter: Optional[Sequence[str]] = Field(
        default=None, alias="OperatingAddressCountryCodeFilter"
    )
    operating_address_state_or_region_filter: Optional[Sequence[str]] = Field(
        default=None, alias="OperatingAddressStateOrRegionFilter"
    )
    operating_address_city_filter: Optional[Sequence[str]] = Field(
        default=None, alias="OperatingAddressCityFilter"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class StartConnectionRequestModel(BaseModel):
    device_serial_number: str = Field(alias="DeviceSerialNumber")
    asset_id: str = Field(alias="AssetId")
    client_public_key: str = Field(alias="ClientPublicKey")
    network_interface_device_index: int = Field(alias="NetworkInterfaceDeviceIndex")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateOutpostInputRequestModel(BaseModel):
    outpost_id: str = Field(alias="OutpostId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    supported_hardware_type: Optional[Literal["RACK", "SERVER"]] = Field(
        default=None, alias="SupportedHardwareType"
    )


class UpdateSiteInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    notes: Optional[str] = Field(default=None, alias="Notes")


class UpdateSiteRackPhysicalPropertiesInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")
    power_draw_kva: Optional[
        Literal["POWER_10_KVA", "POWER_15_KVA", "POWER_30_KVA", "POWER_5_KVA"]
    ] = Field(default=None, alias="PowerDrawKva")
    power_phase: Optional[Literal["SINGLE_PHASE", "THREE_PHASE"]] = Field(
        default=None, alias="PowerPhase"
    )
    power_connector: Optional[
        Literal["AH530P7W", "AH532P6W", "IEC309", "L6_30P"]
    ] = Field(default=None, alias="PowerConnector")
    power_feed_drop: Optional[Literal["ABOVE_RACK", "BELOW_RACK"]] = Field(
        default=None, alias="PowerFeedDrop"
    )
    uplink_gbps: Optional[
        Literal["UPLINK_100G", "UPLINK_10G", "UPLINK_1G", "UPLINK_40G"]
    ] = Field(default=None, alias="UplinkGbps")
    uplink_count: Optional[
        Literal[
            "UPLINK_COUNT_1",
            "UPLINK_COUNT_12",
            "UPLINK_COUNT_16",
            "UPLINK_COUNT_2",
            "UPLINK_COUNT_3",
            "UPLINK_COUNT_4",
            "UPLINK_COUNT_5",
            "UPLINK_COUNT_6",
            "UPLINK_COUNT_7",
            "UPLINK_COUNT_8",
        ]
    ] = Field(default=None, alias="UplinkCount")
    fiber_optic_cable_type: Optional[Literal["MULTI_MODE", "SINGLE_MODE"]] = Field(
        default=None, alias="FiberOpticCableType"
    )
    optical_standard: Optional[
        Literal[
            "OPTIC_1000BASE_LX",
            "OPTIC_1000BASE_SX",
            "OPTIC_100GBASE_CWDM4",
            "OPTIC_100GBASE_LR4",
            "OPTIC_100GBASE_SR4",
            "OPTIC_100G_PSM4_MSA",
            "OPTIC_10GBASE_IR",
            "OPTIC_10GBASE_LR",
            "OPTIC_10GBASE_SR",
            "OPTIC_40GBASE_ESR",
            "OPTIC_40GBASE_IR4_LR4L",
            "OPTIC_40GBASE_LR4",
            "OPTIC_40GBASE_SR",
        ]
    ] = Field(default=None, alias="OpticalStandard")
    maximum_supported_weight_lbs: Optional[
        Literal[
            "MAX_1400_LBS", "MAX_1600_LBS", "MAX_1800_LBS", "MAX_2000_LBS", "NO_LIMIT"
        ]
    ] = Field(default=None, alias="MaximumSupportedWeightLbs")


class UpdateSiteAddressInputRequestModel(BaseModel):
    site_id: str = Field(alias="SiteId")
    address_type: Literal["OPERATING_ADDRESS", "SHIPPING_ADDRESS"] = Field(
        alias="AddressType"
    )
    address: AddressModel = Field(alias="Address")


class AssetInfoModel(BaseModel):
    asset_id: Optional[str] = Field(default=None, alias="AssetId")
    rack_id: Optional[str] = Field(default=None, alias="RackId")
    asset_type: Optional[Literal["COMPUTE"]] = Field(default=None, alias="AssetType")
    compute_attributes: Optional[ComputeAttributesModel] = Field(
        default=None, alias="ComputeAttributes"
    )
    asset_location: Optional[AssetLocationModel] = Field(
        default=None, alias="AssetLocation"
    )


class CatalogItemModel(BaseModel):
    catalog_item_id: Optional[str] = Field(default=None, alias="CatalogItemId")
    item_status: Optional[Literal["AVAILABLE", "DISCONTINUED"]] = Field(
        default=None, alias="ItemStatus"
    )
    ec2_capacities: Optional[List[EC2CapacityModel]] = Field(
        default=None, alias="EC2Capacities"
    )
    power_kva: Optional[float] = Field(default=None, alias="PowerKva")
    weight_lbs: Optional[int] = Field(default=None, alias="WeightLbs")
    supported_uplink_gbps: Optional[List[int]] = Field(
        default=None, alias="SupportedUplinkGbps"
    )
    supported_storage: Optional[List[Literal["EBS", "S3"]]] = Field(
        default=None, alias="SupportedStorage"
    )


class CreateOrderInputRequestModel(BaseModel):
    outpost_identifier: str = Field(alias="OutpostIdentifier")
    line_items: Sequence[LineItemRequestModel] = Field(alias="LineItems")
    payment_option: Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"] = Field(
        alias="PaymentOption"
    )
    payment_term: Optional[Literal["ONE_YEAR", "THREE_YEARS"]] = Field(
        default=None, alias="PaymentTerm"
    )


class GetConnectionResponseModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")
    connection_details: ConnectionDetailsModel = Field(alias="ConnectionDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSiteAddressOutputModel(BaseModel):
    site_id: str = Field(alias="SiteId")
    address_type: Literal["OPERATING_ADDRESS", "SHIPPING_ADDRESS"] = Field(
        alias="AddressType"
    )
    address: AddressModel = Field(alias="Address")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartConnectionResponseModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")
    underlay_ip_address: str = Field(alias="UnderlayIpAddress")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSiteAddressOutputModel(BaseModel):
    address_type: Literal["OPERATING_ADDRESS", "SHIPPING_ADDRESS"] = Field(
        alias="AddressType"
    )
    address: AddressModel = Field(alias="Address")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOutpostOutputModel(BaseModel):
    outpost: OutpostModel = Field(alias="Outpost")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOutpostOutputModel(BaseModel):
    outpost: OutpostModel = Field(alias="Outpost")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOutpostsOutputModel(BaseModel):
    outposts: List[OutpostModel] = Field(alias="Outposts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOutpostOutputModel(BaseModel):
    outpost: OutpostModel = Field(alias="Outpost")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSiteInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    notes: Optional[str] = Field(default=None, alias="Notes")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    operating_address: Optional[AddressModel] = Field(
        default=None, alias="OperatingAddress"
    )
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="ShippingAddress"
    )
    rack_physical_properties: Optional[RackPhysicalPropertiesModel] = Field(
        default=None, alias="RackPhysicalProperties"
    )


class SiteModel(BaseModel):
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    site_arn: Optional[str] = Field(default=None, alias="SiteArn")
    notes: Optional[str] = Field(default=None, alias="Notes")
    operating_address_country_code: Optional[str] = Field(
        default=None, alias="OperatingAddressCountryCode"
    )
    operating_address_state_or_region: Optional[str] = Field(
        default=None, alias="OperatingAddressStateOrRegion"
    )
    operating_address_city: Optional[str] = Field(
        default=None, alias="OperatingAddressCity"
    )
    rack_physical_properties: Optional[RackPhysicalPropertiesModel] = Field(
        default=None, alias="RackPhysicalProperties"
    )


class GetOutpostInstanceTypesOutputModel(BaseModel):
    instance_types: List[InstanceTypeItemModel] = Field(alias="InstanceTypes")
    next_token: str = Field(alias="NextToken")
    outpost_id: str = Field(alias="OutpostId")
    outpost_arn: str = Field(alias="OutpostArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LineItemModel(BaseModel):
    catalog_item_id: Optional[str] = Field(default=None, alias="CatalogItemId")
    line_item_id: Optional[str] = Field(default=None, alias="LineItemId")
    quantity: Optional[int] = Field(default=None, alias="Quantity")
    status: Optional[
        Literal[
            "BUILDING",
            "CANCELLED",
            "DELIVERED",
            "ERROR",
            "INSTALLED",
            "INSTALLING",
            "PREPARING",
            "REPLACED",
            "SHIPPED",
        ]
    ] = Field(default=None, alias="Status")
    shipment_information: Optional[ShipmentInformationModel] = Field(
        default=None, alias="ShipmentInformation"
    )
    asset_information_list: Optional[List[LineItemAssetInformationModel]] = Field(
        default=None, alias="AssetInformationList"
    )
    previous_line_item_id: Optional[str] = Field(
        default=None, alias="PreviousLineItemId"
    )
    previous_order_id: Optional[str] = Field(default=None, alias="PreviousOrderId")


class ListOrdersOutputModel(BaseModel):
    orders: List[OrderSummaryModel] = Field(alias="Orders")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetsOutputModel(BaseModel):
    assets: List[AssetInfoModel] = Field(alias="Assets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCatalogItemOutputModel(BaseModel):
    catalog_item: CatalogItemModel = Field(alias="CatalogItem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCatalogItemsOutputModel(BaseModel):
    catalog_items: List[CatalogItemModel] = Field(alias="CatalogItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSiteOutputModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSiteOutputModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSitesOutputModel(BaseModel):
    sites: List[SiteModel] = Field(alias="Sites")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSiteOutputModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSiteRackPhysicalPropertiesOutputModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrderModel(BaseModel):
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")
    order_id: Optional[str] = Field(default=None, alias="OrderId")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "ERROR",
            "FULFILLED",
            "INSTALLING",
            "IN_PROGRESS",
            "PENDING",
            "PREPARING",
            "PROCESSING",
            "RECEIVED",
        ]
    ] = Field(default=None, alias="Status")
    line_items: Optional[List[LineItemModel]] = Field(default=None, alias="LineItems")
    payment_option: Optional[
        Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
    ] = Field(default=None, alias="PaymentOption")
    order_submission_date: Optional[datetime] = Field(
        default=None, alias="OrderSubmissionDate"
    )
    order_fulfilled_date: Optional[datetime] = Field(
        default=None, alias="OrderFulfilledDate"
    )
    payment_term: Optional[Literal["ONE_YEAR", "THREE_YEARS"]] = Field(
        default=None, alias="PaymentTerm"
    )
    order_type: Optional[Literal["OUTPOST", "REPLACEMENT"]] = Field(
        default=None, alias="OrderType"
    )


class CreateOrderOutputModel(BaseModel):
    order: OrderModel = Field(alias="Order")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrderOutputModel(BaseModel):
    order: OrderModel = Field(alias="Order")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
