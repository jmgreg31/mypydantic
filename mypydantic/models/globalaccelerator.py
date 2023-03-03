# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceleratorAttributesModel(BaseModel):
    flow_logs_enabled: Optional[bool] = Field(default=None, alias="FlowLogsEnabled")
    flow_logs_s3_bucket: Optional[str] = Field(default=None, alias="FlowLogsS3Bucket")
    flow_logs_s3_prefix: Optional[str] = Field(default=None, alias="FlowLogsS3Prefix")


class AcceleratorEventModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class IpSetModel(BaseModel):
    ip_family: Optional[str] = Field(default=None, alias="IpFamily")
    ip_addresses: Optional[List[str]] = Field(default=None, alias="IpAddresses")
    ip_address_family: Optional[Literal["IPv4", "IPv6"]] = Field(
        default=None, alias="IpAddressFamily"
    )


class CustomRoutingEndpointConfigurationModel(BaseModel):
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")


class CustomRoutingEndpointDescriptionModel(BaseModel):
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EndpointConfigurationModel(BaseModel):
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    weight: Optional[int] = Field(default=None, alias="Weight")
    client_ip_preservation_enabled: Optional[bool] = Field(
        default=None, alias="ClientIPPreservationEnabled"
    )


class EndpointDescriptionModel(BaseModel):
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    weight: Optional[int] = Field(default=None, alias="Weight")
    health_state: Optional[Literal["HEALTHY", "INITIAL", "UNHEALTHY"]] = Field(
        default=None, alias="HealthState"
    )
    health_reason: Optional[str] = Field(default=None, alias="HealthReason")
    client_ip_preservation_enabled: Optional[bool] = Field(
        default=None, alias="ClientIPPreservationEnabled"
    )


class AdvertiseByoipCidrRequestModel(BaseModel):
    cidr: str = Field(alias="Cidr")


class AllowCustomRoutingTrafficRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")
    endpoint_id: str = Field(alias="EndpointId")
    destination_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="DestinationAddresses"
    )
    destination_ports: Optional[Sequence[int]] = Field(
        default=None, alias="DestinationPorts"
    )
    allow_all_traffic_to_endpoint: Optional[bool] = Field(
        default=None, alias="AllowAllTrafficToEndpoint"
    )


class ByoipCidrEventModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class CidrAuthorizationContextModel(BaseModel):
    message: str = Field(alias="Message")
    signature: str = Field(alias="Signature")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CustomRoutingDestinationConfigurationModel(BaseModel):
    from_port: int = Field(alias="FromPort")
    to_port: int = Field(alias="ToPort")
    protocols: Sequence[Literal["TCP", "UDP"]] = Field(alias="Protocols")


class PortRangeModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")


class PortOverrideModel(BaseModel):
    listener_port: Optional[int] = Field(default=None, alias="ListenerPort")
    endpoint_port: Optional[int] = Field(default=None, alias="EndpointPort")


class CustomRoutingAcceleratorAttributesModel(BaseModel):
    flow_logs_enabled: Optional[bool] = Field(default=None, alias="FlowLogsEnabled")
    flow_logs_s3_bucket: Optional[str] = Field(default=None, alias="FlowLogsS3Bucket")
    flow_logs_s3_prefix: Optional[str] = Field(default=None, alias="FlowLogsS3Prefix")


class CustomRoutingDestinationDescriptionModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")
    protocols: Optional[List[Literal["TCP", "UDP"]]] = Field(
        default=None, alias="Protocols"
    )


class DeleteAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DeleteCustomRoutingAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DeleteCustomRoutingEndpointGroupRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class DeleteCustomRoutingListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")


class DeleteEndpointGroupRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class DeleteListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")


class DenyCustomRoutingTrafficRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")
    endpoint_id: str = Field(alias="EndpointId")
    destination_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="DestinationAddresses"
    )
    destination_ports: Optional[Sequence[int]] = Field(
        default=None, alias="DestinationPorts"
    )
    deny_all_traffic_to_endpoint: Optional[bool] = Field(
        default=None, alias="DenyAllTrafficToEndpoint"
    )


class DeprovisionByoipCidrRequestModel(BaseModel):
    cidr: str = Field(alias="Cidr")


class DescribeAcceleratorAttributesRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DescribeAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DescribeCustomRoutingAcceleratorAttributesRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DescribeCustomRoutingAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")


class DescribeCustomRoutingEndpointGroupRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class DescribeCustomRoutingListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")


class DescribeEndpointGroupRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class DescribeListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")


class SocketAddressModel(BaseModel):
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    port: Optional[int] = Field(default=None, alias="Port")


class EndpointIdentifierModel(BaseModel):
    endpoint_id: str = Field(alias="EndpointId")
    client_ip_preservation_enabled: Optional[bool] = Field(
        default=None, alias="ClientIPPreservationEnabled"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAcceleratorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListByoipCidrsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomRoutingAcceleratorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomRoutingEndpointGroupsRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomRoutingListenersRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomRoutingPortMappingsByDestinationRequestModel(BaseModel):
    endpoint_id: str = Field(alias="EndpointId")
    destination_address: str = Field(alias="DestinationAddress")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomRoutingPortMappingsRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEndpointGroupsRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListListenersRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RemoveCustomRoutingEndpointsRequestModel(BaseModel):
    endpoint_ids: Sequence[str] = Field(alias="EndpointIds")
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAcceleratorAttributesRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    flow_logs_enabled: Optional[bool] = Field(default=None, alias="FlowLogsEnabled")
    flow_logs_s3_bucket: Optional[str] = Field(default=None, alias="FlowLogsS3Bucket")
    flow_logs_s3_prefix: Optional[str] = Field(default=None, alias="FlowLogsS3Prefix")


class UpdateAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdateCustomRoutingAcceleratorAttributesRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    flow_logs_enabled: Optional[bool] = Field(default=None, alias="FlowLogsEnabled")
    flow_logs_s3_bucket: Optional[str] = Field(default=None, alias="FlowLogsS3Bucket")
    flow_logs_s3_prefix: Optional[str] = Field(default=None, alias="FlowLogsS3Prefix")


class UpdateCustomRoutingAcceleratorRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class WithdrawByoipCidrRequestModel(BaseModel):
    cidr: str = Field(alias="Cidr")


class AcceleratorModel(BaseModel):
    accelerator_arn: Optional[str] = Field(default=None, alias="AcceleratorArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    ip_sets: Optional[List[IpSetModel]] = Field(default=None, alias="IpSets")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    status: Optional[Literal["DEPLOYED", "IN_PROGRESS"]] = Field(
        default=None, alias="Status"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    dual_stack_dns_name: Optional[str] = Field(default=None, alias="DualStackDnsName")
    events: Optional[List[AcceleratorEventModel]] = Field(default=None, alias="Events")


class CustomRoutingAcceleratorModel(BaseModel):
    accelerator_arn: Optional[str] = Field(default=None, alias="AcceleratorArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    ip_sets: Optional[List[IpSetModel]] = Field(default=None, alias="IpSets")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    status: Optional[Literal["DEPLOYED", "IN_PROGRESS"]] = Field(
        default=None, alias="Status"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class AddCustomRoutingEndpointsRequestModel(BaseModel):
    endpoint_configurations: Sequence[CustomRoutingEndpointConfigurationModel] = Field(
        alias="EndpointConfigurations"
    )
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class AddCustomRoutingEndpointsResponseModel(BaseModel):
    endpoint_descriptions: List[CustomRoutingEndpointDescriptionModel] = Field(
        alias="EndpointDescriptions"
    )
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAcceleratorAttributesResponseModel(BaseModel):
    accelerator_attributes: AcceleratorAttributesModel = Field(
        alias="AcceleratorAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAcceleratorAttributesResponseModel(BaseModel):
    accelerator_attributes: AcceleratorAttributesModel = Field(
        alias="AcceleratorAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddEndpointsRequestModel(BaseModel):
    endpoint_configurations: Sequence[EndpointConfigurationModel] = Field(
        alias="EndpointConfigurations"
    )
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class AddEndpointsResponseModel(BaseModel):
    endpoint_descriptions: List[EndpointDescriptionModel] = Field(
        alias="EndpointDescriptions"
    )
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ByoipCidrModel(BaseModel):
    cidr: Optional[str] = Field(default=None, alias="Cidr")
    state: Optional[
        Literal[
            "ADVERTISING",
            "DEPROVISIONED",
            "FAILED_ADVERTISING",
            "FAILED_DEPROVISION",
            "FAILED_PROVISION",
            "FAILED_WITHDRAW",
            "PENDING_ADVERTISING",
            "PENDING_DEPROVISIONING",
            "PENDING_PROVISIONING",
            "PENDING_WITHDRAWING",
            "READY",
        ]
    ] = Field(default=None, alias="State")
    events: Optional[List[ByoipCidrEventModel]] = Field(default=None, alias="Events")


class ProvisionByoipCidrRequestModel(BaseModel):
    cidr: str = Field(alias="Cidr")
    cidr_authorization_context: CidrAuthorizationContextModel = Field(
        alias="CidrAuthorizationContext"
    )


class CreateAcceleratorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    idempotency_token: str = Field(alias="IdempotencyToken")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    ip_addresses: Optional[Sequence[str]] = Field(default=None, alias="IpAddresses")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCustomRoutingAcceleratorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    idempotency_token: str = Field(alias="IdempotencyToken")
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    ip_addresses: Optional[Sequence[str]] = Field(default=None, alias="IpAddresses")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateCustomRoutingEndpointGroupRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    endpoint_group_region: str = Field(alias="EndpointGroupRegion")
    destination_configurations: Sequence[
        CustomRoutingDestinationConfigurationModel
    ] = Field(alias="DestinationConfigurations")
    idempotency_token: str = Field(alias="IdempotencyToken")


class CreateCustomRoutingListenerRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    port_ranges: Sequence[PortRangeModel] = Field(alias="PortRanges")
    idempotency_token: str = Field(alias="IdempotencyToken")


class CreateListenerRequestModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    port_ranges: Sequence[PortRangeModel] = Field(alias="PortRanges")
    protocol: Literal["TCP", "UDP"] = Field(alias="Protocol")
    idempotency_token: str = Field(alias="IdempotencyToken")
    client_affinity: Optional[Literal["NONE", "SOURCE_IP"]] = Field(
        default=None, alias="ClientAffinity"
    )


class CustomRoutingListenerModel(BaseModel):
    listener_arn: Optional[str] = Field(default=None, alias="ListenerArn")
    port_ranges: Optional[List[PortRangeModel]] = Field(
        default=None, alias="PortRanges"
    )


class ListenerModel(BaseModel):
    listener_arn: Optional[str] = Field(default=None, alias="ListenerArn")
    port_ranges: Optional[List[PortRangeModel]] = Field(
        default=None, alias="PortRanges"
    )
    protocol: Optional[Literal["TCP", "UDP"]] = Field(default=None, alias="Protocol")
    client_affinity: Optional[Literal["NONE", "SOURCE_IP"]] = Field(
        default=None, alias="ClientAffinity"
    )


class UpdateCustomRoutingListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    port_ranges: Sequence[PortRangeModel] = Field(alias="PortRanges")


class UpdateListenerRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    port_ranges: Optional[Sequence[PortRangeModel]] = Field(
        default=None, alias="PortRanges"
    )
    protocol: Optional[Literal["TCP", "UDP"]] = Field(default=None, alias="Protocol")
    client_affinity: Optional[Literal["NONE", "SOURCE_IP"]] = Field(
        default=None, alias="ClientAffinity"
    )


class CreateEndpointGroupRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    endpoint_group_region: str = Field(alias="EndpointGroupRegion")
    idempotency_token: str = Field(alias="IdempotencyToken")
    endpoint_configurations: Optional[Sequence[EndpointConfigurationModel]] = Field(
        default=None, alias="EndpointConfigurations"
    )
    traffic_dial_percentage: Optional[float] = Field(
        default=None, alias="TrafficDialPercentage"
    )
    health_check_port: Optional[int] = Field(default=None, alias="HealthCheckPort")
    health_check_protocol: Optional[Literal["HTTP", "HTTPS", "TCP"]] = Field(
        default=None, alias="HealthCheckProtocol"
    )
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    threshold_count: Optional[int] = Field(default=None, alias="ThresholdCount")
    port_overrides: Optional[Sequence[PortOverrideModel]] = Field(
        default=None, alias="PortOverrides"
    )


class EndpointGroupModel(BaseModel):
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    endpoint_group_region: Optional[str] = Field(
        default=None, alias="EndpointGroupRegion"
    )
    endpoint_descriptions: Optional[List[EndpointDescriptionModel]] = Field(
        default=None, alias="EndpointDescriptions"
    )
    traffic_dial_percentage: Optional[float] = Field(
        default=None, alias="TrafficDialPercentage"
    )
    health_check_port: Optional[int] = Field(default=None, alias="HealthCheckPort")
    health_check_protocol: Optional[Literal["HTTP", "HTTPS", "TCP"]] = Field(
        default=None, alias="HealthCheckProtocol"
    )
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    threshold_count: Optional[int] = Field(default=None, alias="ThresholdCount")
    port_overrides: Optional[List[PortOverrideModel]] = Field(
        default=None, alias="PortOverrides"
    )


class UpdateEndpointGroupRequestModel(BaseModel):
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")
    endpoint_configurations: Optional[Sequence[EndpointConfigurationModel]] = Field(
        default=None, alias="EndpointConfigurations"
    )
    traffic_dial_percentage: Optional[float] = Field(
        default=None, alias="TrafficDialPercentage"
    )
    health_check_port: Optional[int] = Field(default=None, alias="HealthCheckPort")
    health_check_protocol: Optional[Literal["HTTP", "HTTPS", "TCP"]] = Field(
        default=None, alias="HealthCheckProtocol"
    )
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    threshold_count: Optional[int] = Field(default=None, alias="ThresholdCount")
    port_overrides: Optional[Sequence[PortOverrideModel]] = Field(
        default=None, alias="PortOverrides"
    )


class DescribeCustomRoutingAcceleratorAttributesResponseModel(BaseModel):
    accelerator_attributes: CustomRoutingAcceleratorAttributesModel = Field(
        alias="AcceleratorAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCustomRoutingAcceleratorAttributesResponseModel(BaseModel):
    accelerator_attributes: CustomRoutingAcceleratorAttributesModel = Field(
        alias="AcceleratorAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomRoutingEndpointGroupModel(BaseModel):
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    endpoint_group_region: Optional[str] = Field(
        default=None, alias="EndpointGroupRegion"
    )
    destination_descriptions: Optional[
        List[CustomRoutingDestinationDescriptionModel]
    ] = Field(default=None, alias="DestinationDescriptions")
    endpoint_descriptions: Optional[
        List[CustomRoutingEndpointDescriptionModel]
    ] = Field(default=None, alias="EndpointDescriptions")


class DestinationPortMappingModel(BaseModel):
    accelerator_arn: Optional[str] = Field(default=None, alias="AcceleratorArn")
    accelerator_socket_addresses: Optional[List[SocketAddressModel]] = Field(
        default=None, alias="AcceleratorSocketAddresses"
    )
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    endpoint_group_region: Optional[str] = Field(
        default=None, alias="EndpointGroupRegion"
    )
    destination_socket_address: Optional[SocketAddressModel] = Field(
        default=None, alias="DestinationSocketAddress"
    )
    ip_address_type: Optional[Literal["DUAL_STACK", "IPV4"]] = Field(
        default=None, alias="IpAddressType"
    )
    destination_traffic_state: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DestinationTrafficState"
    )


class PortMappingModel(BaseModel):
    accelerator_port: Optional[int] = Field(default=None, alias="AcceleratorPort")
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    destination_socket_address: Optional[SocketAddressModel] = Field(
        default=None, alias="DestinationSocketAddress"
    )
    protocols: Optional[List[Literal["TCP", "UDP"]]] = Field(
        default=None, alias="Protocols"
    )
    destination_traffic_state: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DestinationTrafficState"
    )


class RemoveEndpointsRequestModel(BaseModel):
    endpoint_identifiers: Sequence[EndpointIdentifierModel] = Field(
        alias="EndpointIdentifiers"
    )
    endpoint_group_arn: str = Field(alias="EndpointGroupArn")


class ListAcceleratorsRequestListAcceleratorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListByoipCidrsRequestListByoipCidrsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomRoutingAcceleratorsRequestListCustomRoutingAcceleratorsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomRoutingListenersRequestListCustomRoutingListenersPaginateModel(
    BaseModel
):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomRoutingPortMappingsByDestinationRequestListCustomRoutingPortMappingsByDestinationPaginateModel(
    BaseModel
):
    endpoint_id: str = Field(alias="EndpointId")
    destination_address: str = Field(alias="DestinationAddress")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomRoutingPortMappingsRequestListCustomRoutingPortMappingsPaginateModel(
    BaseModel
):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    endpoint_group_arn: Optional[str] = Field(default=None, alias="EndpointGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEndpointGroupsRequestListEndpointGroupsPaginateModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListListenersRequestListListenersPaginateModel(BaseModel):
    accelerator_arn: str = Field(alias="AcceleratorArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class CreateAcceleratorResponseModel(BaseModel):
    accelerator: AcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAcceleratorResponseModel(BaseModel):
    accelerator: AcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAcceleratorsResponseModel(BaseModel):
    accelerators: List[AcceleratorModel] = Field(alias="Accelerators")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAcceleratorResponseModel(BaseModel):
    accelerator: AcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomRoutingAcceleratorResponseModel(BaseModel):
    accelerator: CustomRoutingAcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomRoutingAcceleratorResponseModel(BaseModel):
    accelerator: CustomRoutingAcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomRoutingAcceleratorsResponseModel(BaseModel):
    accelerators: List[CustomRoutingAcceleratorModel] = Field(alias="Accelerators")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCustomRoutingAcceleratorResponseModel(BaseModel):
    accelerator: CustomRoutingAcceleratorModel = Field(alias="Accelerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdvertiseByoipCidrResponseModel(BaseModel):
    byoip_cidr: ByoipCidrModel = Field(alias="ByoipCidr")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeprovisionByoipCidrResponseModel(BaseModel):
    byoip_cidr: ByoipCidrModel = Field(alias="ByoipCidr")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListByoipCidrsResponseModel(BaseModel):
    byoip_cidrs: List[ByoipCidrModel] = Field(alias="ByoipCidrs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionByoipCidrResponseModel(BaseModel):
    byoip_cidr: ByoipCidrModel = Field(alias="ByoipCidr")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WithdrawByoipCidrResponseModel(BaseModel):
    byoip_cidr: ByoipCidrModel = Field(alias="ByoipCidr")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomRoutingListenerResponseModel(BaseModel):
    listener: CustomRoutingListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomRoutingListenerResponseModel(BaseModel):
    listener: CustomRoutingListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomRoutingListenersResponseModel(BaseModel):
    listeners: List[CustomRoutingListenerModel] = Field(alias="Listeners")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCustomRoutingListenerResponseModel(BaseModel):
    listener: CustomRoutingListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateListenerResponseModel(BaseModel):
    listener: ListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeListenerResponseModel(BaseModel):
    listener: ListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListListenersResponseModel(BaseModel):
    listeners: List[ListenerModel] = Field(alias="Listeners")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateListenerResponseModel(BaseModel):
    listener: ListenerModel = Field(alias="Listener")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointGroupResponseModel(BaseModel):
    endpoint_group: EndpointGroupModel = Field(alias="EndpointGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointGroupResponseModel(BaseModel):
    endpoint_group: EndpointGroupModel = Field(alias="EndpointGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointGroupsResponseModel(BaseModel):
    endpoint_groups: List[EndpointGroupModel] = Field(alias="EndpointGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointGroupResponseModel(BaseModel):
    endpoint_group: EndpointGroupModel = Field(alias="EndpointGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomRoutingEndpointGroupResponseModel(BaseModel):
    endpoint_group: CustomRoutingEndpointGroupModel = Field(alias="EndpointGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomRoutingEndpointGroupResponseModel(BaseModel):
    endpoint_group: CustomRoutingEndpointGroupModel = Field(alias="EndpointGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomRoutingEndpointGroupsResponseModel(BaseModel):
    endpoint_groups: List[CustomRoutingEndpointGroupModel] = Field(
        alias="EndpointGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomRoutingPortMappingsByDestinationResponseModel(BaseModel):
    destination_port_mappings: List[DestinationPortMappingModel] = Field(
        alias="DestinationPortMappings"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomRoutingPortMappingsResponseModel(BaseModel):
    port_mappings: List[PortMappingModel] = Field(alias="PortMappings")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
