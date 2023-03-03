# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class RouteFilterPrefixModel(BaseModel):
    cidr: Optional[str] = Field(default=None, alias="cidr")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AllocateConnectionOnInterconnectRequestModel(BaseModel):
    bandwidth: str = Field(alias="bandwidth")
    connection_name: str = Field(alias="connectionName")
    owner_account: str = Field(alias="ownerAccount")
    interconnect_id: str = Field(alias="interconnectId")
    vlan: int = Field(alias="vlan")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class AssociateConnectionWithLagRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    lag_id: str = Field(alias="lagId")


class AssociateHostedConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    parent_connection_id: str = Field(alias="parentConnectionId")


class AssociateMacSecKeyRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    secret_arn: Optional[str] = Field(default=None, alias="secretARN")
    ckn: Optional[str] = Field(default=None, alias="ckn")
    cak: Optional[str] = Field(default=None, alias="cak")


class MacSecKeyModel(BaseModel):
    secret_arn: Optional[str] = Field(default=None, alias="secretARN")
    ckn: Optional[str] = Field(default=None, alias="ckn")
    state: Optional[str] = Field(default=None, alias="state")
    start_on: Optional[str] = Field(default=None, alias="startOn")


class AssociateVirtualInterfaceRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    connection_id: str = Field(alias="connectionId")


class AssociatedGatewayModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[Literal["transitGateway", "virtualPrivateGateway"]] = Field(
        default=None, alias="type"
    )
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    region: Optional[str] = Field(default=None, alias="region")


class BGPPeerModel(BaseModel):
    bgp_peer_id: Optional[str] = Field(default=None, alias="bgpPeerId")
    asn: Optional[int] = Field(default=None, alias="asn")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    bgp_peer_state: Optional[
        Literal["available", "deleted", "deleting", "pending", "verifying"]
    ] = Field(default=None, alias="bgpPeerState")
    bgp_status: Optional[Literal["down", "unknown", "up"]] = Field(
        default=None, alias="bgpStatus"
    )
    aws_device_v2: Optional[str] = Field(default=None, alias="awsDeviceV2")
    aws_logical_device_id: Optional[str] = Field(
        default=None, alias="awsLogicalDeviceId"
    )


class ConfirmConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")


class ConfirmCustomerAgreementRequestModel(BaseModel):
    agreement_name: Optional[str] = Field(default=None, alias="agreementName")


class ConfirmPrivateVirtualInterfaceRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )


class ConfirmPublicVirtualInterfaceRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")


class ConfirmTransitVirtualInterfaceRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")


class NewBGPPeerModel(BaseModel):
    asn: Optional[int] = Field(default=None, alias="asn")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")


class CreateDirectConnectGatewayRequestModel(BaseModel):
    direct_connect_gateway_name: str = Field(alias="directConnectGatewayName")
    amazon_side_asn: Optional[int] = Field(default=None, alias="amazonSideAsn")


class DirectConnectGatewayModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    direct_connect_gateway_name: Optional[str] = Field(
        default=None, alias="directConnectGatewayName"
    )
    amazon_side_asn: Optional[int] = Field(default=None, alias="amazonSideAsn")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    direct_connect_gateway_state: Optional[
        Literal["available", "deleted", "deleting", "pending"]
    ] = Field(default=None, alias="directConnectGatewayState")
    state_change_error: Optional[str] = Field(default=None, alias="stateChangeError")


class CustomerAgreementModel(BaseModel):
    agreement_name: Optional[str] = Field(default=None, alias="agreementName")
    status: Optional[str] = Field(default=None, alias="status")


class DeleteBGPPeerRequestModel(BaseModel):
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    asn: Optional[int] = Field(default=None, alias="asn")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    bgp_peer_id: Optional[str] = Field(default=None, alias="bgpPeerId")


class DeleteConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")


class DeleteDirectConnectGatewayAssociationProposalRequestModel(BaseModel):
    proposal_id: str = Field(alias="proposalId")


class DeleteDirectConnectGatewayAssociationRequestModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="associationId")
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")


class DeleteDirectConnectGatewayRequestModel(BaseModel):
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")


class DeleteInterconnectRequestModel(BaseModel):
    interconnect_id: str = Field(alias="interconnectId")


class DeleteLagRequestModel(BaseModel):
    lag_id: str = Field(alias="lagId")


class DeleteVirtualInterfaceRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")


class DescribeConnectionLoaRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    loa_content_type: Optional[Literal["application/pdf"]] = Field(
        default=None, alias="loaContentType"
    )


class LoaModel(BaseModel):
    loa_content: Optional[bytes] = Field(default=None, alias="loaContent")
    loa_content_type: Optional[Literal["application/pdf"]] = Field(
        default=None, alias="loaContentType"
    )


class DescribeConnectionsOnInterconnectRequestModel(BaseModel):
    interconnect_id: str = Field(alias="interconnectId")


class DescribeConnectionsRequestModel(BaseModel):
    connection_id: Optional[str] = Field(default=None, alias="connectionId")


class DescribeDirectConnectGatewayAssociationProposalsRequestModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    proposal_id: Optional[str] = Field(default=None, alias="proposalId")
    associated_gateway_id: Optional[str] = Field(
        default=None, alias="associatedGatewayId"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeDirectConnectGatewayAssociationsRequestModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="associationId")
    associated_gateway_id: Optional[str] = Field(
        default=None, alias="associatedGatewayId"
    )
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")


class DescribeDirectConnectGatewayAttachmentsRequestModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DirectConnectGatewayAttachmentModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    virtual_interface_region: Optional[str] = Field(
        default=None, alias="virtualInterfaceRegion"
    )
    virtual_interface_owner_account: Optional[str] = Field(
        default=None, alias="virtualInterfaceOwnerAccount"
    )
    attachment_state: Optional[
        Literal["attached", "attaching", "detached", "detaching"]
    ] = Field(default=None, alias="attachmentState")
    attachment_type: Optional[
        Literal["PrivateVirtualInterface", "TransitVirtualInterface"]
    ] = Field(default=None, alias="attachmentType")
    state_change_error: Optional[str] = Field(default=None, alias="stateChangeError")


class DescribeDirectConnectGatewaysRequestModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeHostedConnectionsRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")


class DescribeInterconnectLoaRequestModel(BaseModel):
    interconnect_id: str = Field(alias="interconnectId")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    loa_content_type: Optional[Literal["application/pdf"]] = Field(
        default=None, alias="loaContentType"
    )


class DescribeInterconnectsRequestModel(BaseModel):
    interconnect_id: Optional[str] = Field(default=None, alias="interconnectId")


class DescribeLagsRequestModel(BaseModel):
    lag_id: Optional[str] = Field(default=None, alias="lagId")


class DescribeLoaRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    loa_content_type: Optional[Literal["application/pdf"]] = Field(
        default=None, alias="loaContentType"
    )


class DescribeRouterConfigurationRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    router_type_identifier: Optional[str] = Field(
        default=None, alias="routerTypeIdentifier"
    )


class RouterTypeModel(BaseModel):
    vendor: Optional[str] = Field(default=None, alias="vendor")
    platform: Optional[str] = Field(default=None, alias="platform")
    software: Optional[str] = Field(default=None, alias="software")
    xslt_template_name: Optional[str] = Field(default=None, alias="xsltTemplateName")
    xslt_template_name_for_mac_sec: Optional[str] = Field(
        default=None, alias="xsltTemplateNameForMacSec"
    )
    router_type_identifier: Optional[str] = Field(
        default=None, alias="routerTypeIdentifier"
    )


class DescribeTagsRequestModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="resourceArns")


class DescribeVirtualInterfacesRequestModel(BaseModel):
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )


class DisassociateConnectionFromLagRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    lag_id: str = Field(alias="lagId")


class DisassociateMacSecKeyRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    secret_arn: str = Field(alias="secretARN")


class ListVirtualInterfaceTestHistoryRequestModel(BaseModel):
    test_id: Optional[str] = Field(default=None, alias="testId")
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    bgp_peers: Optional[Sequence[str]] = Field(default=None, alias="bgpPeers")
    status: Optional[str] = Field(default=None, alias="status")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VirtualInterfaceTestHistoryModel(BaseModel):
    test_id: Optional[str] = Field(default=None, alias="testId")
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    bgp_peers: Optional[List[str]] = Field(default=None, alias="bgpPeers")
    status: Optional[str] = Field(default=None, alias="status")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    test_duration_in_minutes: Optional[int] = Field(
        default=None, alias="testDurationInMinutes"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")


class LocationModel(BaseModel):
    location_code: Optional[str] = Field(default=None, alias="locationCode")
    location_name: Optional[str] = Field(default=None, alias="locationName")
    region: Optional[str] = Field(default=None, alias="region")
    available_port_speeds: Optional[List[str]] = Field(
        default=None, alias="availablePortSpeeds"
    )
    available_providers: Optional[List[str]] = Field(
        default=None, alias="availableProviders"
    )
    available_mac_sec_port_speeds: Optional[List[str]] = Field(
        default=None, alias="availableMacSecPortSpeeds"
    )


class StartBgpFailoverTestRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    bgp_peers: Optional[Sequence[str]] = Field(default=None, alias="bgpPeers")
    test_duration_in_minutes: Optional[int] = Field(
        default=None, alias="testDurationInMinutes"
    )


class StopBgpFailoverTestRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    connection_name: Optional[str] = Field(default=None, alias="connectionName")
    encryption_mode: Optional[str] = Field(default=None, alias="encryptionMode")


class UpdateDirectConnectGatewayRequestModel(BaseModel):
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")
    new_direct_connect_gateway_name: str = Field(alias="newDirectConnectGatewayName")


class UpdateLagRequestModel(BaseModel):
    lag_id: str = Field(alias="lagId")
    lag_name: Optional[str] = Field(default=None, alias="lagName")
    minimum_links: Optional[int] = Field(default=None, alias="minimumLinks")
    encryption_mode: Optional[str] = Field(default=None, alias="encryptionMode")


class UpdateVirtualInterfaceAttributesRequestModel(BaseModel):
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    enable_site_link: Optional[bool] = Field(default=None, alias="enableSiteLink")
    virtual_interface_name: Optional[str] = Field(
        default=None, alias="virtualInterfaceName"
    )


class VirtualGatewayModel(BaseModel):
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    virtual_gateway_state: Optional[str] = Field(
        default=None, alias="virtualGatewayState"
    )


class AcceptDirectConnectGatewayAssociationProposalRequestModel(BaseModel):
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")
    proposal_id: str = Field(alias="proposalId")
    associated_gateway_owner_account: str = Field(alias="associatedGatewayOwnerAccount")
    override_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="overrideAllowedPrefixesToDirectConnectGateway")


class CreateDirectConnectGatewayAssociationProposalRequestModel(BaseModel):
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")
    direct_connect_gateway_owner_account: str = Field(
        alias="directConnectGatewayOwnerAccount"
    )
    gateway_id: str = Field(alias="gatewayId")
    add_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="addAllowedPrefixesToDirectConnectGateway")
    remove_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="removeAllowedPrefixesToDirectConnectGateway")


class CreateDirectConnectGatewayAssociationRequestModel(BaseModel):
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")
    gateway_id: Optional[str] = Field(default=None, alias="gatewayId")
    add_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="addAllowedPrefixesToDirectConnectGateway")
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")


class UpdateDirectConnectGatewayAssociationRequestModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="associationId")
    add_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="addAllowedPrefixesToDirectConnectGateway")
    remove_allowed_prefixes_to_direct_connect_gateway: Optional[
        Sequence[RouteFilterPrefixModel]
    ] = Field(default=None, alias="removeAllowedPrefixesToDirectConnectGateway")


class ConfirmConnectionResponseModel(BaseModel):
    connection_state: Literal[
        "available",
        "deleted",
        "deleting",
        "down",
        "ordering",
        "pending",
        "rejected",
        "requested",
        "unknown",
    ] = Field(alias="connectionState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmCustomerAgreementResponseModel(BaseModel):
    status: str = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmPrivateVirtualInterfaceResponseModel(BaseModel):
    virtual_interface_state: Literal[
        "available",
        "confirming",
        "deleted",
        "deleting",
        "down",
        "pending",
        "rejected",
        "unknown",
        "verifying",
    ] = Field(alias="virtualInterfaceState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmPublicVirtualInterfaceResponseModel(BaseModel):
    virtual_interface_state: Literal[
        "available",
        "confirming",
        "deleted",
        "deleting",
        "down",
        "pending",
        "rejected",
        "unknown",
        "verifying",
    ] = Field(alias="virtualInterfaceState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmTransitVirtualInterfaceResponseModel(BaseModel):
    virtual_interface_state: Literal[
        "available",
        "confirming",
        "deleted",
        "deleting",
        "down",
        "pending",
        "rejected",
        "unknown",
        "verifying",
    ] = Field(alias="virtualInterfaceState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInterconnectResponseModel(BaseModel):
    interconnect_state: Literal[
        "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
    ] = Field(alias="interconnectState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualInterfaceResponseModel(BaseModel):
    virtual_interface_state: Literal[
        "available",
        "confirming",
        "deleted",
        "deleting",
        "down",
        "pending",
        "rejected",
        "unknown",
        "verifying",
    ] = Field(alias="virtualInterfaceState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoaResponseMetadataModel(BaseModel):
    loa_content: bytes = Field(alias="loaContent")
    loa_content_type: Literal["application/pdf"] = Field(alias="loaContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AllocateHostedConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    owner_account: str = Field(alias="ownerAccount")
    bandwidth: str = Field(alias="bandwidth")
    connection_name: str = Field(alias="connectionName")
    vlan: int = Field(alias="vlan")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateConnectionRequestModel(BaseModel):
    location: str = Field(alias="location")
    bandwidth: str = Field(alias="bandwidth")
    connection_name: str = Field(alias="connectionName")
    lag_id: Optional[str] = Field(default=None, alias="lagId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    request_macsec: Optional[bool] = Field(default=None, alias="requestMACSec")


class CreateInterconnectRequestModel(BaseModel):
    interconnect_name: str = Field(alias="interconnectName")
    bandwidth: str = Field(alias="bandwidth")
    location: str = Field(alias="location")
    lag_id: Optional[str] = Field(default=None, alias="lagId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    provider_name: Optional[str] = Field(default=None, alias="providerName")


class CreateLagRequestModel(BaseModel):
    number_of_connections: int = Field(alias="numberOfConnections")
    location: str = Field(alias="location")
    connections_bandwidth: str = Field(alias="connectionsBandwidth")
    lag_name: str = Field(alias="lagName")
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    child_connection_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="childConnectionTags"
    )
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    request_macsec: Optional[bool] = Field(default=None, alias="requestMACSec")


class InterconnectResponseMetadataModel(BaseModel):
    interconnect_id: str = Field(alias="interconnectId")
    interconnect_name: str = Field(alias="interconnectName")
    interconnect_state: Literal[
        "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
    ] = Field(alias="interconnectState")
    region: str = Field(alias="region")
    location: str = Field(alias="location")
    bandwidth: str = Field(alias="bandwidth")
    loa_issue_time: datetime = Field(alias="loaIssueTime")
    lag_id: str = Field(alias="lagId")
    aws_device: str = Field(alias="awsDevice")
    jumbo_frame_capable: bool = Field(alias="jumboFrameCapable")
    aws_device_v2: str = Field(alias="awsDeviceV2")
    aws_logical_device_id: str = Field(alias="awsLogicalDeviceId")
    has_logical_redundancy: Literal["no", "unknown", "yes"] = Field(
        alias="hasLogicalRedundancy"
    )
    tags: List[TagModel] = Field(alias="tags")
    provider_name: str = Field(alias="providerName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InterconnectModel(BaseModel):
    interconnect_id: Optional[str] = Field(default=None, alias="interconnectId")
    interconnect_name: Optional[str] = Field(default=None, alias="interconnectName")
    interconnect_state: Optional[
        Literal[
            "available",
            "deleted",
            "deleting",
            "down",
            "pending",
            "requested",
            "unknown",
        ]
    ] = Field(default=None, alias="interconnectState")
    region: Optional[str] = Field(default=None, alias="region")
    location: Optional[str] = Field(default=None, alias="location")
    bandwidth: Optional[str] = Field(default=None, alias="bandwidth")
    loa_issue_time: Optional[datetime] = Field(default=None, alias="loaIssueTime")
    lag_id: Optional[str] = Field(default=None, alias="lagId")
    aws_device: Optional[str] = Field(default=None, alias="awsDevice")
    jumbo_frame_capable: Optional[bool] = Field(default=None, alias="jumboFrameCapable")
    aws_device_v2: Optional[str] = Field(default=None, alias="awsDeviceV2")
    aws_logical_device_id: Optional[str] = Field(
        default=None, alias="awsLogicalDeviceId"
    )
    has_logical_redundancy: Optional[Literal["no", "unknown", "yes"]] = Field(
        default=None, alias="hasLogicalRedundancy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    provider_name: Optional[str] = Field(default=None, alias="providerName")


class NewPrivateVirtualInterfaceAllocationModel(BaseModel):
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    vlan: int = Field(alias="vlan")
    asn: int = Field(alias="asn")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class NewPrivateVirtualInterfaceModel(BaseModel):
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    vlan: int = Field(alias="vlan")
    asn: int = Field(alias="asn")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    enable_site_link: Optional[bool] = Field(default=None, alias="enableSiteLink")


class NewPublicVirtualInterfaceAllocationModel(BaseModel):
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    vlan: int = Field(alias="vlan")
    asn: int = Field(alias="asn")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    route_filter_prefixes: Optional[Sequence[RouteFilterPrefixModel]] = Field(
        default=None, alias="routeFilterPrefixes"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class NewPublicVirtualInterfaceModel(BaseModel):
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    vlan: int = Field(alias="vlan")
    asn: int = Field(alias="asn")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    route_filter_prefixes: Optional[Sequence[RouteFilterPrefixModel]] = Field(
        default=None, alias="routeFilterPrefixes"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class NewTransitVirtualInterfaceAllocationModel(BaseModel):
    virtual_interface_name: Optional[str] = Field(
        default=None, alias="virtualInterfaceName"
    )
    vlan: Optional[int] = Field(default=None, alias="vlan")
    asn: Optional[int] = Field(default=None, alias="asn")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class NewTransitVirtualInterfaceModel(BaseModel):
    virtual_interface_name: Optional[str] = Field(
        default=None, alias="virtualInterfaceName"
    )
    vlan: Optional[int] = Field(default=None, alias="vlan")
    asn: Optional[int] = Field(default=None, alias="asn")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    enable_site_link: Optional[bool] = Field(default=None, alias="enableSiteLink")


class ResourceTagModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class AssociateMacSecKeyResponseModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    mac_sec_keys: List[MacSecKeyModel] = Field(alias="macSecKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectionResponseMetadataModel(BaseModel):
    owner_account: str = Field(alias="ownerAccount")
    connection_id: str = Field(alias="connectionId")
    connection_name: str = Field(alias="connectionName")
    connection_state: Literal[
        "available",
        "deleted",
        "deleting",
        "down",
        "ordering",
        "pending",
        "rejected",
        "requested",
        "unknown",
    ] = Field(alias="connectionState")
    region: str = Field(alias="region")
    location: str = Field(alias="location")
    bandwidth: str = Field(alias="bandwidth")
    vlan: int = Field(alias="vlan")
    partner_name: str = Field(alias="partnerName")
    loa_issue_time: datetime = Field(alias="loaIssueTime")
    lag_id: str = Field(alias="lagId")
    aws_device: str = Field(alias="awsDevice")
    jumbo_frame_capable: bool = Field(alias="jumboFrameCapable")
    aws_device_v2: str = Field(alias="awsDeviceV2")
    aws_logical_device_id: str = Field(alias="awsLogicalDeviceId")
    has_logical_redundancy: Literal["no", "unknown", "yes"] = Field(
        alias="hasLogicalRedundancy"
    )
    tags: List[TagModel] = Field(alias="tags")
    provider_name: str = Field(alias="providerName")
    mac_sec_capable: bool = Field(alias="macSecCapable")
    port_encryption_status: str = Field(alias="portEncryptionStatus")
    encryption_mode: str = Field(alias="encryptionMode")
    mac_sec_keys: List[MacSecKeyModel] = Field(alias="macSecKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectionModel(BaseModel):
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    connection_name: Optional[str] = Field(default=None, alias="connectionName")
    connection_state: Optional[
        Literal[
            "available",
            "deleted",
            "deleting",
            "down",
            "ordering",
            "pending",
            "rejected",
            "requested",
            "unknown",
        ]
    ] = Field(default=None, alias="connectionState")
    region: Optional[str] = Field(default=None, alias="region")
    location: Optional[str] = Field(default=None, alias="location")
    bandwidth: Optional[str] = Field(default=None, alias="bandwidth")
    vlan: Optional[int] = Field(default=None, alias="vlan")
    partner_name: Optional[str] = Field(default=None, alias="partnerName")
    loa_issue_time: Optional[datetime] = Field(default=None, alias="loaIssueTime")
    lag_id: Optional[str] = Field(default=None, alias="lagId")
    aws_device: Optional[str] = Field(default=None, alias="awsDevice")
    jumbo_frame_capable: Optional[bool] = Field(default=None, alias="jumboFrameCapable")
    aws_device_v2: Optional[str] = Field(default=None, alias="awsDeviceV2")
    aws_logical_device_id: Optional[str] = Field(
        default=None, alias="awsLogicalDeviceId"
    )
    has_logical_redundancy: Optional[Literal["no", "unknown", "yes"]] = Field(
        default=None, alias="hasLogicalRedundancy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    mac_sec_capable: Optional[bool] = Field(default=None, alias="macSecCapable")
    port_encryption_status: Optional[str] = Field(
        default=None, alias="portEncryptionStatus"
    )
    encryption_mode: Optional[str] = Field(default=None, alias="encryptionMode")
    mac_sec_keys: Optional[List[MacSecKeyModel]] = Field(
        default=None, alias="macSecKeys"
    )


class DisassociateMacSecKeyResponseModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    mac_sec_keys: List[MacSecKeyModel] = Field(alias="macSecKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DirectConnectGatewayAssociationProposalModel(BaseModel):
    proposal_id: Optional[str] = Field(default=None, alias="proposalId")
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    direct_connect_gateway_owner_account: Optional[str] = Field(
        default=None, alias="directConnectGatewayOwnerAccount"
    )
    proposal_state: Optional[Literal["accepted", "deleted", "requested"]] = Field(
        default=None, alias="proposalState"
    )
    associated_gateway: Optional[AssociatedGatewayModel] = Field(
        default=None, alias="associatedGateway"
    )
    existing_allowed_prefixes_to_direct_connect_gateway: Optional[
        List[RouteFilterPrefixModel]
    ] = Field(default=None, alias="existingAllowedPrefixesToDirectConnectGateway")
    requested_allowed_prefixes_to_direct_connect_gateway: Optional[
        List[RouteFilterPrefixModel]
    ] = Field(default=None, alias="requestedAllowedPrefixesToDirectConnectGateway")


class DirectConnectGatewayAssociationModel(BaseModel):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    direct_connect_gateway_owner_account: Optional[str] = Field(
        default=None, alias="directConnectGatewayOwnerAccount"
    )
    association_state: Optional[
        Literal[
            "associated", "associating", "disassociated", "disassociating", "updating"
        ]
    ] = Field(default=None, alias="associationState")
    state_change_error: Optional[str] = Field(default=None, alias="stateChangeError")
    associated_gateway: Optional[AssociatedGatewayModel] = Field(
        default=None, alias="associatedGateway"
    )
    association_id: Optional[str] = Field(default=None, alias="associationId")
    allowed_prefixes_to_direct_connect_gateway: Optional[
        List[RouteFilterPrefixModel]
    ] = Field(default=None, alias="allowedPrefixesToDirectConnectGateway")
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    virtual_gateway_region: Optional[str] = Field(
        default=None, alias="virtualGatewayRegion"
    )
    virtual_gateway_owner_account: Optional[str] = Field(
        default=None, alias="virtualGatewayOwnerAccount"
    )


class VirtualInterfaceResponseMetadataModel(BaseModel):
    owner_account: str = Field(alias="ownerAccount")
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    location: str = Field(alias="location")
    connection_id: str = Field(alias="connectionId")
    virtual_interface_type: str = Field(alias="virtualInterfaceType")
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    vlan: int = Field(alias="vlan")
    asn: int = Field(alias="asn")
    amazon_side_asn: int = Field(alias="amazonSideAsn")
    auth_key: str = Field(alias="authKey")
    amazon_address: str = Field(alias="amazonAddress")
    customer_address: str = Field(alias="customerAddress")
    address_family: Literal["ipv4", "ipv6"] = Field(alias="addressFamily")
    virtual_interface_state: Literal[
        "available",
        "confirming",
        "deleted",
        "deleting",
        "down",
        "pending",
        "rejected",
        "unknown",
        "verifying",
    ] = Field(alias="virtualInterfaceState")
    customer_router_config: str = Field(alias="customerRouterConfig")
    mtu: int = Field(alias="mtu")
    jumbo_frame_capable: bool = Field(alias="jumboFrameCapable")
    virtual_gateway_id: str = Field(alias="virtualGatewayId")
    direct_connect_gateway_id: str = Field(alias="directConnectGatewayId")
    route_filter_prefixes: List[RouteFilterPrefixModel] = Field(
        alias="routeFilterPrefixes"
    )
    bgp_peers: List[BGPPeerModel] = Field(alias="bgpPeers")
    region: str = Field(alias="region")
    aws_device_v2: str = Field(alias="awsDeviceV2")
    aws_logical_device_id: str = Field(alias="awsLogicalDeviceId")
    tags: List[TagModel] = Field(alias="tags")
    site_link_enabled: bool = Field(alias="siteLinkEnabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualInterfaceModel(BaseModel):
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    location: Optional[str] = Field(default=None, alias="location")
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    virtual_interface_type: Optional[str] = Field(
        default=None, alias="virtualInterfaceType"
    )
    virtual_interface_name: Optional[str] = Field(
        default=None, alias="virtualInterfaceName"
    )
    vlan: Optional[int] = Field(default=None, alias="vlan")
    asn: Optional[int] = Field(default=None, alias="asn")
    amazon_side_asn: Optional[int] = Field(default=None, alias="amazonSideAsn")
    auth_key: Optional[str] = Field(default=None, alias="authKey")
    amazon_address: Optional[str] = Field(default=None, alias="amazonAddress")
    customer_address: Optional[str] = Field(default=None, alias="customerAddress")
    address_family: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="addressFamily"
    )
    virtual_interface_state: Optional[
        Literal[
            "available",
            "confirming",
            "deleted",
            "deleting",
            "down",
            "pending",
            "rejected",
            "unknown",
            "verifying",
        ]
    ] = Field(default=None, alias="virtualInterfaceState")
    customer_router_config: Optional[str] = Field(
        default=None, alias="customerRouterConfig"
    )
    mtu: Optional[int] = Field(default=None, alias="mtu")
    jumbo_frame_capable: Optional[bool] = Field(default=None, alias="jumboFrameCapable")
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    route_filter_prefixes: Optional[List[RouteFilterPrefixModel]] = Field(
        default=None, alias="routeFilterPrefixes"
    )
    bgp_peers: Optional[List[BGPPeerModel]] = Field(default=None, alias="bgpPeers")
    region: Optional[str] = Field(default=None, alias="region")
    aws_device_v2: Optional[str] = Field(default=None, alias="awsDeviceV2")
    aws_logical_device_id: Optional[str] = Field(
        default=None, alias="awsLogicalDeviceId"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    site_link_enabled: Optional[bool] = Field(default=None, alias="siteLinkEnabled")


class CreateBGPPeerRequestModel(BaseModel):
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    new_bgp_peer: Optional[NewBGPPeerModel] = Field(default=None, alias="newBGPPeer")


class CreateDirectConnectGatewayResultModel(BaseModel):
    direct_connect_gateway: DirectConnectGatewayModel = Field(
        alias="directConnectGateway"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDirectConnectGatewayResultModel(BaseModel):
    direct_connect_gateway: DirectConnectGatewayModel = Field(
        alias="directConnectGateway"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDirectConnectGatewaysResultModel(BaseModel):
    direct_connect_gateways: List[DirectConnectGatewayModel] = Field(
        alias="directConnectGateways"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDirectConnectGatewayResponseModel(BaseModel):
    direct_connect_gateway: DirectConnectGatewayModel = Field(
        alias="directConnectGateway"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomerMetadataResponseModel(BaseModel):
    agreements: List[CustomerAgreementModel] = Field(alias="agreements")
    nni_partner_type: Literal["nonPartner", "v1", "v2"] = Field(alias="nniPartnerType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectionLoaResponseModel(BaseModel):
    loa: LoaModel = Field(alias="loa")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInterconnectLoaResponseModel(BaseModel):
    loa: LoaModel = Field(alias="loa")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDirectConnectGatewayAssociationsRequestDescribeDirectConnectGatewayAssociationsPaginateModel(
    BaseModel
):
    association_id: Optional[str] = Field(default=None, alias="associationId")
    associated_gateway_id: Optional[str] = Field(
        default=None, alias="associatedGatewayId"
    )
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    virtual_gateway_id: Optional[str] = Field(default=None, alias="virtualGatewayId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDirectConnectGatewayAttachmentsRequestDescribeDirectConnectGatewayAttachmentsPaginateModel(
    BaseModel
):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    virtual_interface_id: Optional[str] = Field(
        default=None, alias="virtualInterfaceId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDirectConnectGatewaysRequestDescribeDirectConnectGatewaysPaginateModel(
    BaseModel
):
    direct_connect_gateway_id: Optional[str] = Field(
        default=None, alias="directConnectGatewayId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDirectConnectGatewayAttachmentsResultModel(BaseModel):
    direct_connect_gateway_attachments: List[
        DirectConnectGatewayAttachmentModel
    ] = Field(alias="directConnectGatewayAttachments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRouterConfigurationResponseModel(BaseModel):
    customer_router_config: str = Field(alias="customerRouterConfig")
    router: RouterTypeModel = Field(alias="router")
    virtual_interface_id: str = Field(alias="virtualInterfaceId")
    virtual_interface_name: str = Field(alias="virtualInterfaceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualInterfaceTestHistoryResponseModel(BaseModel):
    virtual_interface_test_history: List[VirtualInterfaceTestHistoryModel] = Field(
        alias="virtualInterfaceTestHistory"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBgpFailoverTestResponseModel(BaseModel):
    virtual_interface_test: VirtualInterfaceTestHistoryModel = Field(
        alias="virtualInterfaceTest"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopBgpFailoverTestResponseModel(BaseModel):
    virtual_interface_test: VirtualInterfaceTestHistoryModel = Field(
        alias="virtualInterfaceTest"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LocationsModel(BaseModel):
    locations: List[LocationModel] = Field(alias="locations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualGatewaysModel(BaseModel):
    virtual_gateways: List[VirtualGatewayModel] = Field(alias="virtualGateways")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InterconnectsModel(BaseModel):
    interconnects: List[InterconnectModel] = Field(alias="interconnects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AllocatePrivateVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    owner_account: str = Field(alias="ownerAccount")
    new_private_virtual_interface_allocation: NewPrivateVirtualInterfaceAllocationModel = Field(
        alias="newPrivateVirtualInterfaceAllocation"
    )


class CreatePrivateVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    new_private_virtual_interface: NewPrivateVirtualInterfaceModel = Field(
        alias="newPrivateVirtualInterface"
    )


class AllocatePublicVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    owner_account: str = Field(alias="ownerAccount")
    new_public_virtual_interface_allocation: NewPublicVirtualInterfaceAllocationModel = Field(
        alias="newPublicVirtualInterfaceAllocation"
    )


class CreatePublicVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    new_public_virtual_interface: NewPublicVirtualInterfaceModel = Field(
        alias="newPublicVirtualInterface"
    )


class AllocateTransitVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    owner_account: str = Field(alias="ownerAccount")
    new_transit_virtual_interface_allocation: NewTransitVirtualInterfaceAllocationModel = Field(
        alias="newTransitVirtualInterfaceAllocation"
    )


class CreateTransitVirtualInterfaceRequestModel(BaseModel):
    connection_id: str = Field(alias="connectionId")
    new_transit_virtual_interface: NewTransitVirtualInterfaceModel = Field(
        alias="newTransitVirtualInterface"
    )


class DescribeTagsResponseModel(BaseModel):
    resource_tags: List[ResourceTagModel] = Field(alias="resourceTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectionsModel(BaseModel):
    connections: List[ConnectionModel] = Field(alias="connections")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LagResponseMetadataModel(BaseModel):
    connections_bandwidth: str = Field(alias="connectionsBandwidth")
    number_of_connections: int = Field(alias="numberOfConnections")
    lag_id: str = Field(alias="lagId")
    owner_account: str = Field(alias="ownerAccount")
    lag_name: str = Field(alias="lagName")
    lag_state: Literal[
        "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
    ] = Field(alias="lagState")
    location: str = Field(alias="location")
    region: str = Field(alias="region")
    minimum_links: int = Field(alias="minimumLinks")
    aws_device: str = Field(alias="awsDevice")
    aws_device_v2: str = Field(alias="awsDeviceV2")
    aws_logical_device_id: str = Field(alias="awsLogicalDeviceId")
    connections: List[ConnectionModel] = Field(alias="connections")
    allows_hosted_connections: bool = Field(alias="allowsHostedConnections")
    jumbo_frame_capable: bool = Field(alias="jumboFrameCapable")
    has_logical_redundancy: Literal["no", "unknown", "yes"] = Field(
        alias="hasLogicalRedundancy"
    )
    tags: List[TagModel] = Field(alias="tags")
    provider_name: str = Field(alias="providerName")
    mac_sec_capable: bool = Field(alias="macSecCapable")
    encryption_mode: str = Field(alias="encryptionMode")
    mac_sec_keys: List[MacSecKeyModel] = Field(alias="macSecKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LagModel(BaseModel):
    connections_bandwidth: Optional[str] = Field(
        default=None, alias="connectionsBandwidth"
    )
    number_of_connections: Optional[int] = Field(
        default=None, alias="numberOfConnections"
    )
    lag_id: Optional[str] = Field(default=None, alias="lagId")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    lag_name: Optional[str] = Field(default=None, alias="lagName")
    lag_state: Optional[
        Literal[
            "available",
            "deleted",
            "deleting",
            "down",
            "pending",
            "requested",
            "unknown",
        ]
    ] = Field(default=None, alias="lagState")
    location: Optional[str] = Field(default=None, alias="location")
    region: Optional[str] = Field(default=None, alias="region")
    minimum_links: Optional[int] = Field(default=None, alias="minimumLinks")
    aws_device: Optional[str] = Field(default=None, alias="awsDevice")
    aws_device_v2: Optional[str] = Field(default=None, alias="awsDeviceV2")
    aws_logical_device_id: Optional[str] = Field(
        default=None, alias="awsLogicalDeviceId"
    )
    connections: Optional[List[ConnectionModel]] = Field(
        default=None, alias="connections"
    )
    allows_hosted_connections: Optional[bool] = Field(
        default=None, alias="allowsHostedConnections"
    )
    jumbo_frame_capable: Optional[bool] = Field(default=None, alias="jumboFrameCapable")
    has_logical_redundancy: Optional[Literal["no", "unknown", "yes"]] = Field(
        default=None, alias="hasLogicalRedundancy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    provider_name: Optional[str] = Field(default=None, alias="providerName")
    mac_sec_capable: Optional[bool] = Field(default=None, alias="macSecCapable")
    encryption_mode: Optional[str] = Field(default=None, alias="encryptionMode")
    mac_sec_keys: Optional[List[MacSecKeyModel]] = Field(
        default=None, alias="macSecKeys"
    )


class CreateDirectConnectGatewayAssociationProposalResultModel(BaseModel):
    direct_connect_gateway_association_proposal: DirectConnectGatewayAssociationProposalModel = Field(
        alias="directConnectGatewayAssociationProposal"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDirectConnectGatewayAssociationProposalResultModel(BaseModel):
    direct_connect_gateway_association_proposal: DirectConnectGatewayAssociationProposalModel = Field(
        alias="directConnectGatewayAssociationProposal"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDirectConnectGatewayAssociationProposalsResultModel(BaseModel):
    direct_connect_gateway_association_proposals: List[
        DirectConnectGatewayAssociationProposalModel
    ] = Field(alias="directConnectGatewayAssociationProposals")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptDirectConnectGatewayAssociationProposalResultModel(BaseModel):
    direct_connect_gateway_association: DirectConnectGatewayAssociationModel = Field(
        alias="directConnectGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDirectConnectGatewayAssociationResultModel(BaseModel):
    direct_connect_gateway_association: DirectConnectGatewayAssociationModel = Field(
        alias="directConnectGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDirectConnectGatewayAssociationResultModel(BaseModel):
    direct_connect_gateway_association: DirectConnectGatewayAssociationModel = Field(
        alias="directConnectGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDirectConnectGatewayAssociationsResultModel(BaseModel):
    direct_connect_gateway_associations: List[
        DirectConnectGatewayAssociationModel
    ] = Field(alias="directConnectGatewayAssociations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDirectConnectGatewayAssociationResultModel(BaseModel):
    direct_connect_gateway_association: DirectConnectGatewayAssociationModel = Field(
        alias="directConnectGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AllocateTransitVirtualInterfaceResultModel(BaseModel):
    virtual_interface: VirtualInterfaceModel = Field(alias="virtualInterface")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBGPPeerResponseModel(BaseModel):
    virtual_interface: VirtualInterfaceModel = Field(alias="virtualInterface")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTransitVirtualInterfaceResultModel(BaseModel):
    virtual_interface: VirtualInterfaceModel = Field(alias="virtualInterface")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBGPPeerResponseModel(BaseModel):
    virtual_interface: VirtualInterfaceModel = Field(alias="virtualInterface")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualInterfacesModel(BaseModel):
    virtual_interfaces: List[VirtualInterfaceModel] = Field(alias="virtualInterfaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LagsModel(BaseModel):
    lags: List[LagModel] = Field(alias="lags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
