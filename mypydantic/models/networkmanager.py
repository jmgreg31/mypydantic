# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AWSLocationModel(BaseModel):
    zone: Optional[str] = Field(default=None, alias="Zone")
    subnet_arn: Optional[str] = Field(default=None, alias="SubnetArn")


class AcceptAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AccountStatusModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    s_l_rdeployment_status: Optional[str] = Field(
        default=None, alias="SLRDeploymentStatus"
    )


class AssociateConnectPeerRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connect_peer_id: str = Field(alias="ConnectPeerId")
    device_id: str = Field(alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")


class ConnectPeerAssociationModel(BaseModel):
    connect_peer_id: Optional[str] = Field(default=None, alias="ConnectPeerId")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    state: Optional[Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]] = Field(
        default=None, alias="State"
    )


class AssociateCustomerGatewayRequestModel(BaseModel):
    customer_gateway_arn: str = Field(alias="CustomerGatewayArn")
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")


class CustomerGatewayAssociationModel(BaseModel):
    customer_gateway_arn: Optional[str] = Field(
        default=None, alias="CustomerGatewayArn"
    )
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    state: Optional[Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]] = Field(
        default=None, alias="State"
    )


class AssociateLinkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")
    link_id: str = Field(alias="LinkId")


class LinkAssociationModel(BaseModel):
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    link_association_state: Optional[
        Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
    ] = Field(default=None, alias="LinkAssociationState")


class AssociateTransitGatewayConnectPeerRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_connect_peer_arn: str = Field(alias="TransitGatewayConnectPeerArn")
    device_id: str = Field(alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")


class TransitGatewayConnectPeerAssociationModel(BaseModel):
    transit_gateway_connect_peer_arn: Optional[str] = Field(
        default=None, alias="TransitGatewayConnectPeerArn"
    )
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    state: Optional[Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]] = Field(
        default=None, alias="State"
    )


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class BandwidthModel(BaseModel):
    upload_speed: Optional[int] = Field(default=None, alias="UploadSpeed")
    download_speed: Optional[int] = Field(default=None, alias="DownloadSpeed")


class BgpOptionsModel(BaseModel):
    peer_asn: Optional[int] = Field(default=None, alias="PeerAsn")


class ConnectAttachmentOptionsModel(BaseModel):
    protocol: Optional[Literal["GRE"]] = Field(default=None, alias="Protocol")


class ConnectPeerBgpConfigurationModel(BaseModel):
    core_network_asn: Optional[int] = Field(default=None, alias="CoreNetworkAsn")
    peer_asn: Optional[int] = Field(default=None, alias="PeerAsn")
    core_network_address: Optional[str] = Field(
        default=None, alias="CoreNetworkAddress"
    )
    peer_address: Optional[str] = Field(default=None, alias="PeerAddress")


class ConnectionHealthModel(BaseModel):
    type: Optional[Literal["BGP", "IPSEC"]] = Field(default=None, alias="Type")
    status: Optional[Literal["DOWN", "UP"]] = Field(default=None, alias="Status")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class CoreNetworkChangeEventValuesModel(BaseModel):
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")
    attachment_id: Optional[str] = Field(default=None, alias="AttachmentId")
    cidr: Optional[str] = Field(default=None, alias="Cidr")


class CoreNetworkChangeValuesModel(BaseModel):
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")
    edge_locations: Optional[List[str]] = Field(default=None, alias="EdgeLocations")
    asn: Optional[int] = Field(default=None, alias="Asn")
    cidr: Optional[str] = Field(default=None, alias="Cidr")
    destination_identifier: Optional[str] = Field(
        default=None, alias="DestinationIdentifier"
    )
    inside_cidr_blocks: Optional[List[str]] = Field(
        default=None, alias="InsideCidrBlocks"
    )
    shared_segments: Optional[List[str]] = Field(default=None, alias="SharedSegments")


class CoreNetworkEdgeModel(BaseModel):
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    asn: Optional[int] = Field(default=None, alias="Asn")
    inside_cidr_blocks: Optional[List[str]] = Field(
        default=None, alias="InsideCidrBlocks"
    )


class CoreNetworkPolicyErrorModel(BaseModel):
    error_code: str = Field(alias="ErrorCode")
    message: str = Field(alias="Message")
    path: Optional[str] = Field(default=None, alias="Path")


class CoreNetworkPolicyVersionModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    policy_version_id: Optional[int] = Field(default=None, alias="PolicyVersionId")
    alias: Optional[Literal["LATEST", "LIVE"]] = Field(default=None, alias="Alias")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    change_set_state: Optional[
        Literal[
            "EXECUTING",
            "EXECUTION_SUCCEEDED",
            "FAILED_GENERATION",
            "OUT_OF_DATE",
            "PENDING_GENERATION",
            "READY_TO_EXECUTE",
        ]
    ] = Field(default=None, alias="ChangeSetState")


class CoreNetworkSegmentEdgeIdentifierModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")


class CoreNetworkSegmentModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    edge_locations: Optional[List[str]] = Field(default=None, alias="EdgeLocations")
    shared_segments: Optional[List[str]] = Field(default=None, alias="SharedSegments")


class LocationModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    latitude: Optional[str] = Field(default=None, alias="Latitude")
    longitude: Optional[str] = Field(default=None, alias="Longitude")


class VpcOptionsModel(BaseModel):
    ipv6_support: Optional[bool] = Field(default=None, alias="Ipv6Support")
    appliance_mode_support: Optional[bool] = Field(
        default=None, alias="ApplianceModeSupport"
    )


class DeleteAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class DeleteConnectPeerRequestModel(BaseModel):
    connect_peer_id: str = Field(alias="ConnectPeerId")


class DeleteConnectionRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connection_id: str = Field(alias="ConnectionId")


class DeleteCoreNetworkPolicyVersionRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")


class DeleteCoreNetworkRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")


class DeleteDeviceRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")


class DeleteGlobalNetworkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")


class DeleteLinkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    link_id: str = Field(alias="LinkId")


class DeletePeeringRequestModel(BaseModel):
    peering_id: str = Field(alias="PeeringId")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteSiteRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    site_id: str = Field(alias="SiteId")


class DeregisterTransitGatewayRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_arn: str = Field(alias="TransitGatewayArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeGlobalNetworksRequestModel(BaseModel):
    global_network_ids: Optional[Sequence[str]] = Field(
        default=None, alias="GlobalNetworkIds"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DisassociateConnectPeerRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connect_peer_id: str = Field(alias="ConnectPeerId")


class DisassociateCustomerGatewayRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    customer_gateway_arn: str = Field(alias="CustomerGatewayArn")


class DisassociateLinkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")
    link_id: str = Field(alias="LinkId")


class DisassociateTransitGatewayConnectPeerRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_connect_peer_arn: str = Field(alias="TransitGatewayConnectPeerArn")


class ExecuteCoreNetworkChangeSetRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")


class GetConnectAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class GetConnectPeerAssociationsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connect_peer_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ConnectPeerIds"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetConnectPeerRequestModel(BaseModel):
    connect_peer_id: str = Field(alias="ConnectPeerId")


class GetConnectionsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connection_ids: Optional[Sequence[str]] = Field(default=None, alias="ConnectionIds")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCoreNetworkChangeEventsRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCoreNetworkChangeSetRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCoreNetworkPolicyRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: Optional[int] = Field(default=None, alias="PolicyVersionId")
    alias: Optional[Literal["LATEST", "LIVE"]] = Field(default=None, alias="Alias")


class GetCoreNetworkRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")


class GetCustomerGatewayAssociationsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    customer_gateway_arns: Optional[Sequence[str]] = Field(
        default=None, alias="CustomerGatewayArns"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetDevicesRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_ids: Optional[Sequence[str]] = Field(default=None, alias="DeviceIds")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetLinkAssociationsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetLinksRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    link_ids: Optional[Sequence[str]] = Field(default=None, alias="LinkIds")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    type: Optional[str] = Field(default=None, alias="Type")
    provider: Optional[str] = Field(default=None, alias="Provider")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetNetworkResourceCountsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NetworkResourceCountModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    count: Optional[int] = Field(default=None, alias="Count")


class GetNetworkResourceRelationshipsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RelationshipModel(BaseModel):
    from_: Optional[str] = Field(default=None, alias="From")
    to: Optional[str] = Field(default=None, alias="To")


class GetNetworkResourcesRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetNetworkTelemetryRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetRouteAnalysisRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    route_analysis_id: str = Field(alias="RouteAnalysisId")


class GetSiteToSiteVpnAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class GetSitesRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    site_ids: Optional[Sequence[str]] = Field(default=None, alias="SiteIds")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTransitGatewayConnectPeerAssociationsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_connect_peer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TransitGatewayConnectPeerArns"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTransitGatewayPeeringRequestModel(BaseModel):
    peering_id: str = Field(alias="PeeringId")


class GetTransitGatewayRegistrationsRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TransitGatewayArns"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTransitGatewayRouteTableAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class GetVpcAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class ListAttachmentsRequestModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    attachment_type: Optional[
        Literal["CONNECT", "SITE_TO_SITE_VPN", "TRANSIT_GATEWAY_ROUTE_TABLE", "VPC"]
    ] = Field(default=None, alias="AttachmentType")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    state: Optional[
        Literal[
            "AVAILABLE",
            "CREATING",
            "DELETING",
            "FAILED",
            "PENDING_ATTACHMENT_ACCEPTANCE",
            "PENDING_NETWORK_UPDATE",
            "PENDING_TAG_ACCEPTANCE",
            "REJECTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConnectPeersRequestModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    connect_attachment_id: Optional[str] = Field(
        default=None, alias="ConnectAttachmentId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCoreNetworkPolicyVersionsRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCoreNetworksRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOrganizationServiceAccessStatusRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPeeringsRequestModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    peering_type: Optional[Literal["TRANSIT_GATEWAY"]] = Field(
        default=None, alias="PeeringType"
    )
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NetworkResourceSummaryModel(BaseModel):
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    definition: Optional[str] = Field(default=None, alias="Definition")
    name_tag: Optional[str] = Field(default=None, alias="NameTag")
    is_middlebox: Optional[bool] = Field(default=None, alias="IsMiddlebox")


class NetworkRouteDestinationModel(BaseModel):
    core_network_attachment_id: Optional[str] = Field(
        default=None, alias="CoreNetworkAttachmentId"
    )
    transit_gateway_attachment_id: Optional[str] = Field(
        default=None, alias="TransitGatewayAttachmentId"
    )
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")


class PutCoreNetworkPolicyRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_document: str = Field(alias="PolicyDocument")
    description: Optional[str] = Field(default=None, alias="Description")
    latest_version_id: Optional[int] = Field(default=None, alias="LatestVersionId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class PutResourcePolicyRequestModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")
    resource_arn: str = Field(alias="ResourceArn")


class RegisterTransitGatewayRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_arn: str = Field(alias="TransitGatewayArn")


class RejectAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")


class RestoreCoreNetworkPolicyVersionRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")


class RouteAnalysisCompletionModel(BaseModel):
    result_code: Optional[Literal["CONNECTED", "NOT_CONNECTED"]] = Field(
        default=None, alias="ResultCode"
    )
    reason_code: Optional[
        Literal[
            "BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND",
            "CYCLIC_PATH_DETECTED",
            "INACTIVE_ROUTE_FOR_DESTINATION_FOUND",
            "MAX_HOPS_EXCEEDED",
            "NO_DESTINATION_ARN_PROVIDED",
            "POSSIBLE_MIDDLEBOX",
            "ROUTE_NOT_FOUND",
            "TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH",
            "TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND",
            "TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY",
            "TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND",
        ]
    ] = Field(default=None, alias="ReasonCode")
    reason_context: Optional[Dict[str, str]] = Field(
        default=None, alias="ReasonContext"
    )


class RouteAnalysisEndpointOptionsSpecificationModel(BaseModel):
    transit_gateway_attachment_arn: Optional[str] = Field(
        default=None, alias="TransitGatewayAttachmentArn"
    )
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class RouteAnalysisEndpointOptionsModel(BaseModel):
    transit_gateway_attachment_arn: Optional[str] = Field(
        default=None, alias="TransitGatewayAttachmentArn"
    )
    transit_gateway_arn: Optional[str] = Field(default=None, alias="TransitGatewayArn")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class StartOrganizationServiceAccessUpdateRequestModel(BaseModel):
    action: str = Field(alias="Action")


class TransitGatewayRegistrationStateReasonModel(BaseModel):
    code: Optional[
        Literal["AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateConnectionRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connection_id: str = Field(alias="ConnectionId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    connected_link_id: Optional[str] = Field(default=None, alias="ConnectedLinkId")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateCoreNetworkRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateGlobalNetworkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateNetworkResourceMetadataRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    resource_arn: str = Field(alias="ResourceArn")
    metadata: Mapping[str, str] = Field(alias="Metadata")


class GetResourcePolicyResponseModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNetworkResourceMetadataResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    metadata: Dict[str, str] = Field(alias="Metadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrganizationStatusModel(BaseModel):
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    organization_aws_service_access_status: Optional[str] = Field(
        default=None, alias="OrganizationAwsServiceAccessStatus"
    )
    s_l_rdeployment_status: Optional[str] = Field(
        default=None, alias="SLRDeploymentStatus"
    )
    account_status_list: Optional[List[AccountStatusModel]] = Field(
        default=None, alias="AccountStatusList"
    )


class AssociateConnectPeerResponseModel(BaseModel):
    connect_peer_association: ConnectPeerAssociationModel = Field(
        alias="ConnectPeerAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateConnectPeerResponseModel(BaseModel):
    connect_peer_association: ConnectPeerAssociationModel = Field(
        alias="ConnectPeerAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectPeerAssociationsResponseModel(BaseModel):
    connect_peer_associations: List[ConnectPeerAssociationModel] = Field(
        alias="ConnectPeerAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateCustomerGatewayResponseModel(BaseModel):
    customer_gateway_association: CustomerGatewayAssociationModel = Field(
        alias="CustomerGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateCustomerGatewayResponseModel(BaseModel):
    customer_gateway_association: CustomerGatewayAssociationModel = Field(
        alias="CustomerGatewayAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCustomerGatewayAssociationsResponseModel(BaseModel):
    customer_gateway_associations: List[CustomerGatewayAssociationModel] = Field(
        alias="CustomerGatewayAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateLinkResponseModel(BaseModel):
    link_association: LinkAssociationModel = Field(alias="LinkAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateLinkResponseModel(BaseModel):
    link_association: LinkAssociationModel = Field(alias="LinkAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLinkAssociationsResponseModel(BaseModel):
    link_associations: List[LinkAssociationModel] = Field(alias="LinkAssociations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateTransitGatewayConnectPeerResponseModel(BaseModel):
    transit_gateway_connect_peer_association: TransitGatewayConnectPeerAssociationModel = Field(
        alias="TransitGatewayConnectPeerAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateTransitGatewayConnectPeerResponseModel(BaseModel):
    transit_gateway_connect_peer_association: TransitGatewayConnectPeerAssociationModel = Field(
        alias="TransitGatewayConnectPeerAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTransitGatewayConnectPeerAssociationsResponseModel(BaseModel):
    transit_gateway_connect_peer_associations: List[
        TransitGatewayConnectPeerAssociationModel
    ] = Field(alias="TransitGatewayConnectPeerAssociations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectPeerSummaryModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    connect_attachment_id: Optional[str] = Field(
        default=None, alias="ConnectAttachmentId"
    )
    connect_peer_id: Optional[str] = Field(default=None, alias="ConnectPeerId")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    connect_peer_state: Optional[
        Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]
    ] = Field(default=None, alias="ConnectPeerState")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ConnectionModel(BaseModel):
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    connected_device_id: Optional[str] = Field(default=None, alias="ConnectedDeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    connected_link_id: Optional[str] = Field(default=None, alias="ConnectedLinkId")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CoreNetworkSummaryModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    core_network_arn: Optional[str] = Field(default=None, alias="CoreNetworkArn")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateConnectionRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")
    connected_device_id: str = Field(alias="ConnectedDeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    connected_link_id: Optional[str] = Field(default=None, alias="ConnectedLinkId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCoreNetworkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    policy_document: Optional[str] = Field(default=None, alias="PolicyDocument")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateGlobalNetworkRequestModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSiteToSiteVpnAttachmentRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    vpn_connection_arn: str = Field(alias="VpnConnectionArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateTransitGatewayPeeringRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    transit_gateway_arn: str = Field(alias="TransitGatewayArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateTransitGatewayRouteTableAttachmentRequestModel(BaseModel):
    peering_id: str = Field(alias="PeeringId")
    transit_gateway_route_table_arn: str = Field(alias="TransitGatewayRouteTableArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class GlobalNetworkModel(BaseModel):
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    global_network_arn: Optional[str] = Field(default=None, alias="GlobalNetworkArn")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkResourceModel(BaseModel):
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    definition: Optional[str] = Field(default=None, alias="Definition")
    definition_timestamp: Optional[datetime] = Field(
        default=None, alias="DefinitionTimestamp"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    metadata: Optional[Dict[str, str]] = Field(default=None, alias="Metadata")


class PeeringModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    core_network_arn: Optional[str] = Field(default=None, alias="CoreNetworkArn")
    peering_id: Optional[str] = Field(default=None, alias="PeeringId")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    peering_type: Optional[Literal["TRANSIT_GATEWAY"]] = Field(
        default=None, alias="PeeringType"
    )
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class ProposedSegmentChangeModel(BaseModel):
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    attachment_policy_rule_number: Optional[int] = Field(
        default=None, alias="AttachmentPolicyRuleNumber"
    )
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateLinkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    bandwidth: BandwidthModel = Field(alias="Bandwidth")
    site_id: str = Field(alias="SiteId")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    provider: Optional[str] = Field(default=None, alias="Provider")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class LinkModel(BaseModel):
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    link_arn: Optional[str] = Field(default=None, alias="LinkArn")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    bandwidth: Optional[BandwidthModel] = Field(default=None, alias="Bandwidth")
    provider: Optional[str] = Field(default=None, alias="Provider")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class UpdateLinkRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    link_id: str = Field(alias="LinkId")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    bandwidth: Optional[BandwidthModel] = Field(default=None, alias="Bandwidth")
    provider: Optional[str] = Field(default=None, alias="Provider")


class CreateConnectPeerRequestModel(BaseModel):
    connect_attachment_id: str = Field(alias="ConnectAttachmentId")
    peer_address: str = Field(alias="PeerAddress")
    inside_cidr_blocks: Sequence[str] = Field(alias="InsideCidrBlocks")
    core_network_address: Optional[str] = Field(
        default=None, alias="CoreNetworkAddress"
    )
    bgp_options: Optional[BgpOptionsModel] = Field(default=None, alias="BgpOptions")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateConnectAttachmentRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    edge_location: str = Field(alias="EdgeLocation")
    transport_attachment_id: str = Field(alias="TransportAttachmentId")
    options: ConnectAttachmentOptionsModel = Field(alias="Options")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ConnectPeerConfigurationModel(BaseModel):
    core_network_address: Optional[str] = Field(
        default=None, alias="CoreNetworkAddress"
    )
    peer_address: Optional[str] = Field(default=None, alias="PeerAddress")
    inside_cidr_blocks: Optional[List[str]] = Field(
        default=None, alias="InsideCidrBlocks"
    )
    protocol: Optional[Literal["GRE"]] = Field(default=None, alias="Protocol")
    bgp_configurations: Optional[List[ConnectPeerBgpConfigurationModel]] = Field(
        default=None, alias="BgpConfigurations"
    )


class NetworkTelemetryModel(BaseModel):
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    address: Optional[str] = Field(default=None, alias="Address")
    health: Optional[ConnectionHealthModel] = Field(default=None, alias="Health")


class CoreNetworkChangeEventModel(BaseModel):
    type: Optional[
        Literal[
            "ATTACHMENT_MAPPING",
            "ATTACHMENT_POLICIES_CONFIGURATION",
            "ATTACHMENT_ROUTE_PROPAGATION",
            "ATTACHMENT_ROUTE_STATIC",
            "CORE_NETWORK_CONFIGURATION",
            "CORE_NETWORK_EDGE",
            "CORE_NETWORK_SEGMENT",
            "SEGMENTS_CONFIGURATION",
            "SEGMENT_ACTIONS_CONFIGURATION",
        ]
    ] = Field(default=None, alias="Type")
    action: Optional[Literal["ADD", "MODIFY", "REMOVE"]] = Field(
        default=None, alias="Action"
    )
    identifier_path: Optional[str] = Field(default=None, alias="IdentifierPath")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    status: Optional[
        Literal["COMPLETE", "FAILED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="Status")
    values: Optional[CoreNetworkChangeEventValuesModel] = Field(
        default=None, alias="Values"
    )


class CoreNetworkChangeModel(BaseModel):
    type: Optional[
        Literal[
            "ATTACHMENT_MAPPING",
            "ATTACHMENT_POLICIES_CONFIGURATION",
            "ATTACHMENT_ROUTE_PROPAGATION",
            "ATTACHMENT_ROUTE_STATIC",
            "CORE_NETWORK_CONFIGURATION",
            "CORE_NETWORK_EDGE",
            "CORE_NETWORK_SEGMENT",
            "SEGMENTS_CONFIGURATION",
            "SEGMENT_ACTIONS_CONFIGURATION",
        ]
    ] = Field(default=None, alias="Type")
    action: Optional[Literal["ADD", "MODIFY", "REMOVE"]] = Field(
        default=None, alias="Action"
    )
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    previous_values: Optional[CoreNetworkChangeValuesModel] = Field(
        default=None, alias="PreviousValues"
    )
    new_values: Optional[CoreNetworkChangeValuesModel] = Field(
        default=None, alias="NewValues"
    )
    identifier_path: Optional[str] = Field(default=None, alias="IdentifierPath")


class CoreNetworkPolicyModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    policy_version_id: Optional[int] = Field(default=None, alias="PolicyVersionId")
    alias: Optional[Literal["LATEST", "LIVE"]] = Field(default=None, alias="Alias")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    change_set_state: Optional[
        Literal[
            "EXECUTING",
            "EXECUTION_SUCCEEDED",
            "FAILED_GENERATION",
            "OUT_OF_DATE",
            "PENDING_GENERATION",
            "READY_TO_EXECUTE",
        ]
    ] = Field(default=None, alias="ChangeSetState")
    policy_errors: Optional[List[CoreNetworkPolicyErrorModel]] = Field(
        default=None, alias="PolicyErrors"
    )
    policy_document: Optional[str] = Field(default=None, alias="PolicyDocument")


class ListCoreNetworkPolicyVersionsResponseModel(BaseModel):
    core_network_policy_versions: List[CoreNetworkPolicyVersionModel] = Field(
        alias="CoreNetworkPolicyVersions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RouteTableIdentifierModel(BaseModel):
    transit_gateway_route_table_arn: Optional[str] = Field(
        default=None, alias="TransitGatewayRouteTableArn"
    )
    core_network_segment_edge: Optional[CoreNetworkSegmentEdgeIdentifierModel] = Field(
        default=None, alias="CoreNetworkSegmentEdge"
    )


class CoreNetworkModel(BaseModel):
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    core_network_arn: Optional[str] = Field(default=None, alias="CoreNetworkArn")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    segments: Optional[List[CoreNetworkSegmentModel]] = Field(
        default=None, alias="Segments"
    )
    edges: Optional[List[CoreNetworkEdgeModel]] = Field(default=None, alias="Edges")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateDeviceRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    aws_location: Optional[AWSLocationModel] = Field(default=None, alias="AWSLocation")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    vendor: Optional[str] = Field(default=None, alias="Vendor")
    model: Optional[str] = Field(default=None, alias="Model")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSiteRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    description: Optional[str] = Field(default=None, alias="Description")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DeviceModel(BaseModel):
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    aws_location: Optional[AWSLocationModel] = Field(default=None, alias="AWSLocation")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    vendor: Optional[str] = Field(default=None, alias="Vendor")
    model: Optional[str] = Field(default=None, alias="Model")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class SiteModel(BaseModel):
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    site_arn: Optional[str] = Field(default=None, alias="SiteArn")
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    description: Optional[str] = Field(default=None, alias="Description")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    state: Optional[Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class UpdateDeviceRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: str = Field(alias="DeviceId")
    aws_location: Optional[AWSLocationModel] = Field(default=None, alias="AWSLocation")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    vendor: Optional[str] = Field(default=None, alias="Vendor")
    model: Optional[str] = Field(default=None, alias="Model")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    site_id: Optional[str] = Field(default=None, alias="SiteId")


class UpdateSiteRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    site_id: str = Field(alias="SiteId")
    description: Optional[str] = Field(default=None, alias="Description")
    location: Optional[LocationModel] = Field(default=None, alias="Location")


class CreateVpcAttachmentRequestModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    vpc_arn: str = Field(alias="VpcArn")
    subnet_arns: Sequence[str] = Field(alias="SubnetArns")
    options: Optional[VpcOptionsModel] = Field(default=None, alias="Options")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UpdateVpcAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")
    add_subnet_arns: Optional[Sequence[str]] = Field(
        default=None, alias="AddSubnetArns"
    )
    remove_subnet_arns: Optional[Sequence[str]] = Field(
        default=None, alias="RemoveSubnetArns"
    )
    options: Optional[VpcOptionsModel] = Field(default=None, alias="Options")


class DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateModel(BaseModel):
    global_network_ids: Optional[Sequence[str]] = Field(
        default=None, alias="GlobalNetworkIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateModel(
    BaseModel
):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connect_peer_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ConnectPeerIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetConnectionsRequestGetConnectionsPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    connection_ids: Optional[Sequence[str]] = Field(default=None, alias="ConnectionIds")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateModel(
    BaseModel
):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateModel(BaseModel):
    core_network_id: str = Field(alias="CoreNetworkId")
    policy_version_id: int = Field(alias="PolicyVersionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateModel(
    BaseModel
):
    global_network_id: str = Field(alias="GlobalNetworkId")
    customer_gateway_arns: Optional[Sequence[str]] = Field(
        default=None, alias="CustomerGatewayArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDevicesRequestGetDevicesPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_ids: Optional[Sequence[str]] = Field(default=None, alias="DeviceIds")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetLinkAssociationsRequestGetLinkAssociationsPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    link_id: Optional[str] = Field(default=None, alias="LinkId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetLinksRequestGetLinksPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    link_ids: Optional[Sequence[str]] = Field(default=None, alias="LinkIds")
    site_id: Optional[str] = Field(default=None, alias="SiteId")
    type: Optional[str] = Field(default=None, alias="Type")
    provider: Optional[str] = Field(default=None, alias="Provider")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateModel(
    BaseModel
):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetNetworkResourcesRequestGetNetworkResourcesPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetNetworkTelemetryRequestGetNetworkTelemetryPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    registered_gateway_arn: Optional[str] = Field(
        default=None, alias="RegisteredGatewayArn"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSitesRequestGetSitesPaginateModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    site_ids: Optional[Sequence[str]] = Field(default=None, alias="SiteIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateModel(
    BaseModel
):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_connect_peer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TransitGatewayConnectPeerArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateModel(
    BaseModel
):
    global_network_id: str = Field(alias="GlobalNetworkId")
    transit_gateway_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TransitGatewayArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachmentsRequestListAttachmentsPaginateModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    attachment_type: Optional[
        Literal["CONNECT", "SITE_TO_SITE_VPN", "TRANSIT_GATEWAY_ROUTE_TABLE", "VPC"]
    ] = Field(default=None, alias="AttachmentType")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    state: Optional[
        Literal[
            "AVAILABLE",
            "CREATING",
            "DELETING",
            "FAILED",
            "PENDING_ATTACHMENT_ACCEPTANCE",
            "PENDING_NETWORK_UPDATE",
            "PENDING_TAG_ACCEPTANCE",
            "REJECTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConnectPeersRequestListConnectPeersPaginateModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    connect_attachment_id: Optional[str] = Field(
        default=None, alias="ConnectAttachmentId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateModel(
    BaseModel
):
    core_network_id: str = Field(alias="CoreNetworkId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoreNetworksRequestListCoreNetworksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPeeringsRequestListPeeringsPaginateModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    peering_type: Optional[Literal["TRANSIT_GATEWAY"]] = Field(
        default=None, alias="PeeringType"
    )
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetNetworkResourceCountsResponseModel(BaseModel):
    network_resource_counts: List[NetworkResourceCountModel] = Field(
        alias="NetworkResourceCounts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkResourceRelationshipsResponseModel(BaseModel):
    relationships: List[RelationshipModel] = Field(alias="Relationships")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PathComponentModel(BaseModel):
    sequence: Optional[int] = Field(default=None, alias="Sequence")
    resource: Optional[NetworkResourceSummaryModel] = Field(
        default=None, alias="Resource"
    )
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )


class NetworkRouteModel(BaseModel):
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )
    destinations: Optional[List[NetworkRouteDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    prefix_list_id: Optional[str] = Field(default=None, alias="PrefixListId")
    state: Optional[Literal["ACTIVE", "BLACKHOLE"]] = Field(default=None, alias="State")
    type: Optional[Literal["PROPAGATED", "STATIC"]] = Field(default=None, alias="Type")


class StartRouteAnalysisRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    source: RouteAnalysisEndpointOptionsSpecificationModel = Field(alias="Source")
    destination: RouteAnalysisEndpointOptionsSpecificationModel = Field(
        alias="Destination"
    )
    include_return_path: Optional[bool] = Field(default=None, alias="IncludeReturnPath")
    use_middleboxes: Optional[bool] = Field(default=None, alias="UseMiddleboxes")


class TransitGatewayRegistrationModel(BaseModel):
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    transit_gateway_arn: Optional[str] = Field(default=None, alias="TransitGatewayArn")
    state: Optional[TransitGatewayRegistrationStateReasonModel] = Field(
        default=None, alias="State"
    )


class ListOrganizationServiceAccessStatusResponseModel(BaseModel):
    organization_status: OrganizationStatusModel = Field(alias="OrganizationStatus")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartOrganizationServiceAccessUpdateResponseModel(BaseModel):
    organization_status: OrganizationStatusModel = Field(alias="OrganizationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectPeersResponseModel(BaseModel):
    connect_peers: List[ConnectPeerSummaryModel] = Field(alias="ConnectPeers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectionsResponseModel(BaseModel):
    connections: List[ConnectionModel] = Field(alias="Connections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCoreNetworksResponseModel(BaseModel):
    core_networks: List[CoreNetworkSummaryModel] = Field(alias="CoreNetworks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGlobalNetworkResponseModel(BaseModel):
    global_network: GlobalNetworkModel = Field(alias="GlobalNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGlobalNetworkResponseModel(BaseModel):
    global_network: GlobalNetworkModel = Field(alias="GlobalNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGlobalNetworksResponseModel(BaseModel):
    global_networks: List[GlobalNetworkModel] = Field(alias="GlobalNetworks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGlobalNetworkResponseModel(BaseModel):
    global_network: GlobalNetworkModel = Field(alias="GlobalNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkResourcesResponseModel(BaseModel):
    network_resources: List[NetworkResourceModel] = Field(alias="NetworkResources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePeeringResponseModel(BaseModel):
    peering: PeeringModel = Field(alias="Peering")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPeeringsResponseModel(BaseModel):
    peerings: List[PeeringModel] = Field(alias="Peerings")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransitGatewayPeeringModel(BaseModel):
    peering: Optional[PeeringModel] = Field(default=None, alias="Peering")
    transit_gateway_arn: Optional[str] = Field(default=None, alias="TransitGatewayArn")
    transit_gateway_peering_attachment_id: Optional[str] = Field(
        default=None, alias="TransitGatewayPeeringAttachmentId"
    )


class AttachmentModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    core_network_arn: Optional[str] = Field(default=None, alias="CoreNetworkArn")
    attachment_id: Optional[str] = Field(default=None, alias="AttachmentId")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    attachment_type: Optional[
        Literal["CONNECT", "SITE_TO_SITE_VPN", "TRANSIT_GATEWAY_ROUTE_TABLE", "VPC"]
    ] = Field(default=None, alias="AttachmentType")
    state: Optional[
        Literal[
            "AVAILABLE",
            "CREATING",
            "DELETING",
            "FAILED",
            "PENDING_ATTACHMENT_ACCEPTANCE",
            "PENDING_NETWORK_UPDATE",
            "PENDING_TAG_ACCEPTANCE",
            "REJECTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    attachment_policy_rule_number: Optional[int] = Field(
        default=None, alias="AttachmentPolicyRuleNumber"
    )
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    proposed_segment_change: Optional[ProposedSegmentChangeModel] = Field(
        default=None, alias="ProposedSegmentChange"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class CreateLinkResponseModel(BaseModel):
    link: LinkModel = Field(alias="Link")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLinkResponseModel(BaseModel):
    link: LinkModel = Field(alias="Link")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLinksResponseModel(BaseModel):
    links: List[LinkModel] = Field(alias="Links")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLinkResponseModel(BaseModel):
    link: LinkModel = Field(alias="Link")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectPeerModel(BaseModel):
    core_network_id: Optional[str] = Field(default=None, alias="CoreNetworkId")
    connect_attachment_id: Optional[str] = Field(
        default=None, alias="ConnectAttachmentId"
    )
    connect_peer_id: Optional[str] = Field(default=None, alias="ConnectPeerId")
    edge_location: Optional[str] = Field(default=None, alias="EdgeLocation")
    state: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    configuration: Optional[ConnectPeerConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class GetNetworkTelemetryResponseModel(BaseModel):
    network_telemetry: List[NetworkTelemetryModel] = Field(alias="NetworkTelemetry")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreNetworkChangeEventsResponseModel(BaseModel):
    core_network_change_events: List[CoreNetworkChangeEventModel] = Field(
        alias="CoreNetworkChangeEvents"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreNetworkChangeSetResponseModel(BaseModel):
    core_network_changes: List[CoreNetworkChangeModel] = Field(
        alias="CoreNetworkChanges"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCoreNetworkPolicyVersionResponseModel(BaseModel):
    core_network_policy: CoreNetworkPolicyModel = Field(alias="CoreNetworkPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreNetworkPolicyResponseModel(BaseModel):
    core_network_policy: CoreNetworkPolicyModel = Field(alias="CoreNetworkPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutCoreNetworkPolicyResponseModel(BaseModel):
    core_network_policy: CoreNetworkPolicyModel = Field(alias="CoreNetworkPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreCoreNetworkPolicyVersionResponseModel(BaseModel):
    core_network_policy: CoreNetworkPolicyModel = Field(alias="CoreNetworkPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkRoutesRequestModel(BaseModel):
    global_network_id: str = Field(alias="GlobalNetworkId")
    route_table_identifier: RouteTableIdentifierModel = Field(
        alias="RouteTableIdentifier"
    )
    exact_cidr_matches: Optional[Sequence[str]] = Field(
        default=None, alias="ExactCidrMatches"
    )
    longest_prefix_matches: Optional[Sequence[str]] = Field(
        default=None, alias="LongestPrefixMatches"
    )
    subnet_of_matches: Optional[Sequence[str]] = Field(
        default=None, alias="SubnetOfMatches"
    )
    supernet_of_matches: Optional[Sequence[str]] = Field(
        default=None, alias="SupernetOfMatches"
    )
    prefix_list_ids: Optional[Sequence[str]] = Field(
        default=None, alias="PrefixListIds"
    )
    states: Optional[Sequence[Literal["ACTIVE", "BLACKHOLE"]]] = Field(
        default=None, alias="States"
    )
    types: Optional[Sequence[Literal["PROPAGATED", "STATIC"]]] = Field(
        default=None, alias="Types"
    )
    destination_filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="DestinationFilters"
    )


class CreateCoreNetworkResponseModel(BaseModel):
    core_network: CoreNetworkModel = Field(alias="CoreNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCoreNetworkResponseModel(BaseModel):
    core_network: CoreNetworkModel = Field(alias="CoreNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreNetworkResponseModel(BaseModel):
    core_network: CoreNetworkModel = Field(alias="CoreNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCoreNetworkResponseModel(BaseModel):
    core_network: CoreNetworkModel = Field(alias="CoreNetwork")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeviceResponseModel(BaseModel):
    device: DeviceModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDeviceResponseModel(BaseModel):
    device: DeviceModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevicesResponseModel(BaseModel):
    devices: List[DeviceModel] = Field(alias="Devices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeviceResponseModel(BaseModel):
    device: DeviceModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSiteResponseModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSiteResponseModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSitesResponseModel(BaseModel):
    sites: List[SiteModel] = Field(alias="Sites")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSiteResponseModel(BaseModel):
    site: SiteModel = Field(alias="Site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RouteAnalysisPathModel(BaseModel):
    completion_status: Optional[RouteAnalysisCompletionModel] = Field(
        default=None, alias="CompletionStatus"
    )
    path: Optional[List[PathComponentModel]] = Field(default=None, alias="Path")


class GetNetworkRoutesResponseModel(BaseModel):
    route_table_arn: str = Field(alias="RouteTableArn")
    core_network_segment_edge: CoreNetworkSegmentEdgeIdentifierModel = Field(
        alias="CoreNetworkSegmentEdge"
    )
    route_table_type: Literal[
        "CORE_NETWORK_SEGMENT", "TRANSIT_GATEWAY_ROUTE_TABLE"
    ] = Field(alias="RouteTableType")
    route_table_timestamp: datetime = Field(alias="RouteTableTimestamp")
    network_routes: List[NetworkRouteModel] = Field(alias="NetworkRoutes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterTransitGatewayResponseModel(BaseModel):
    transit_gateway_registration: TransitGatewayRegistrationModel = Field(
        alias="TransitGatewayRegistration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTransitGatewayRegistrationsResponseModel(BaseModel):
    transit_gateway_registrations: List[TransitGatewayRegistrationModel] = Field(
        alias="TransitGatewayRegistrations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTransitGatewayResponseModel(BaseModel):
    transit_gateway_registration: TransitGatewayRegistrationModel = Field(
        alias="TransitGatewayRegistration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTransitGatewayPeeringResponseModel(BaseModel):
    transit_gateway_peering: TransitGatewayPeeringModel = Field(
        alias="TransitGatewayPeering"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTransitGatewayPeeringResponseModel(BaseModel):
    transit_gateway_peering: TransitGatewayPeeringModel = Field(
        alias="TransitGatewayPeering"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptAttachmentResponseModel(BaseModel):
    attachment: AttachmentModel = Field(alias="Attachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectAttachmentModel(BaseModel):
    attachment: Optional[AttachmentModel] = Field(default=None, alias="Attachment")
    transport_attachment_id: Optional[str] = Field(
        default=None, alias="TransportAttachmentId"
    )
    options: Optional[ConnectAttachmentOptionsModel] = Field(
        default=None, alias="Options"
    )


class DeleteAttachmentResponseModel(BaseModel):
    attachment: AttachmentModel = Field(alias="Attachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachmentsResponseModel(BaseModel):
    attachments: List[AttachmentModel] = Field(alias="Attachments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectAttachmentResponseModel(BaseModel):
    attachment: AttachmentModel = Field(alias="Attachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SiteToSiteVpnAttachmentModel(BaseModel):
    attachment: Optional[AttachmentModel] = Field(default=None, alias="Attachment")
    vpn_connection_arn: Optional[str] = Field(default=None, alias="VpnConnectionArn")


class TransitGatewayRouteTableAttachmentModel(BaseModel):
    attachment: Optional[AttachmentModel] = Field(default=None, alias="Attachment")
    peering_id: Optional[str] = Field(default=None, alias="PeeringId")
    transit_gateway_route_table_arn: Optional[str] = Field(
        default=None, alias="TransitGatewayRouteTableArn"
    )


class VpcAttachmentModel(BaseModel):
    attachment: Optional[AttachmentModel] = Field(default=None, alias="Attachment")
    subnet_arns: Optional[List[str]] = Field(default=None, alias="SubnetArns")
    options: Optional[VpcOptionsModel] = Field(default=None, alias="Options")


class CreateConnectPeerResponseModel(BaseModel):
    connect_peer: ConnectPeerModel = Field(alias="ConnectPeer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConnectPeerResponseModel(BaseModel):
    connect_peer: ConnectPeerModel = Field(alias="ConnectPeer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectPeerResponseModel(BaseModel):
    connect_peer: ConnectPeerModel = Field(alias="ConnectPeer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RouteAnalysisModel(BaseModel):
    global_network_id: Optional[str] = Field(default=None, alias="GlobalNetworkId")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    route_analysis_id: Optional[str] = Field(default=None, alias="RouteAnalysisId")
    start_timestamp: Optional[datetime] = Field(default=None, alias="StartTimestamp")
    status: Optional[Literal["COMPLETED", "FAILED", "RUNNING"]] = Field(
        default=None, alias="Status"
    )
    source: Optional[RouteAnalysisEndpointOptionsModel] = Field(
        default=None, alias="Source"
    )
    destination: Optional[RouteAnalysisEndpointOptionsModel] = Field(
        default=None, alias="Destination"
    )
    include_return_path: Optional[bool] = Field(default=None, alias="IncludeReturnPath")
    use_middleboxes: Optional[bool] = Field(default=None, alias="UseMiddleboxes")
    forward_path: Optional[RouteAnalysisPathModel] = Field(
        default=None, alias="ForwardPath"
    )
    return_path: Optional[RouteAnalysisPathModel] = Field(
        default=None, alias="ReturnPath"
    )


class CreateConnectAttachmentResponseModel(BaseModel):
    connect_attachment: ConnectAttachmentModel = Field(alias="ConnectAttachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectAttachmentResponseModel(BaseModel):
    connect_attachment: ConnectAttachmentModel = Field(alias="ConnectAttachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSiteToSiteVpnAttachmentResponseModel(BaseModel):
    site_to_site_vpn_attachment: SiteToSiteVpnAttachmentModel = Field(
        alias="SiteToSiteVpnAttachment"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSiteToSiteVpnAttachmentResponseModel(BaseModel):
    site_to_site_vpn_attachment: SiteToSiteVpnAttachmentModel = Field(
        alias="SiteToSiteVpnAttachment"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTransitGatewayRouteTableAttachmentResponseModel(BaseModel):
    transit_gateway_route_table_attachment: TransitGatewayRouteTableAttachmentModel = (
        Field(alias="TransitGatewayRouteTableAttachment")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTransitGatewayRouteTableAttachmentResponseModel(BaseModel):
    transit_gateway_route_table_attachment: TransitGatewayRouteTableAttachmentModel = (
        Field(alias="TransitGatewayRouteTableAttachment")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcAttachmentResponseModel(BaseModel):
    vpc_attachment: VpcAttachmentModel = Field(alias="VpcAttachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVpcAttachmentResponseModel(BaseModel):
    vpc_attachment: VpcAttachmentModel = Field(alias="VpcAttachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVpcAttachmentResponseModel(BaseModel):
    vpc_attachment: VpcAttachmentModel = Field(alias="VpcAttachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRouteAnalysisResponseModel(BaseModel):
    route_analysis: RouteAnalysisModel = Field(alias="RouteAnalysis")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRouteAnalysisResponseModel(BaseModel):
    route_analysis: RouteAnalysisModel = Field(alias="RouteAnalysis")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
