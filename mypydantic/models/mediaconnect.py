# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class VpcInterfaceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    subnet_id: str = Field(alias="SubnetId")
    network_interface_type: Optional[Literal["efa", "ena"]] = Field(
        default=None, alias="NetworkInterfaceType"
    )


class VpcInterfaceModel(BaseModel):
    name: str = Field(alias="Name")
    network_interface_ids: List[str] = Field(alias="NetworkInterfaceIds")
    network_interface_type: Literal["efa", "ena"] = Field(alias="NetworkInterfaceType")
    role_arn: str = Field(alias="RoleArn")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_id: str = Field(alias="SubnetId")


class AddMaintenanceModel(BaseModel):
    maintenance_day: Literal[
        "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
    ] = Field(alias="MaintenanceDay")
    maintenance_start_hour: str = Field(alias="MaintenanceStartHour")


class EncryptionModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    algorithm: Optional[Literal["aes128", "aes192", "aes256"]] = Field(
        default=None, alias="Algorithm"
    )
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    key_type: Optional[Literal["speke", "srt-password", "static-key"]] = Field(
        default=None, alias="KeyType"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    url: Optional[str] = Field(default=None, alias="Url")


class VpcInterfaceAttachmentModel(BaseModel):
    vpc_interface_name: Optional[str] = Field(default=None, alias="VpcInterfaceName")


class DeleteFlowRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeFlowRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")


class MessagesModel(BaseModel):
    errors: List[str] = Field(alias="Errors")


class DescribeOfferingRequestModel(BaseModel):
    offering_arn: str = Field(alias="OfferingArn")


class DescribeReservationRequestModel(BaseModel):
    reservation_arn: str = Field(alias="ReservationArn")


class InterfaceRequestModel(BaseModel):
    name: str = Field(alias="Name")


class InterfaceModel(BaseModel):
    name: str = Field(alias="Name")


class EncodingParametersRequestModel(BaseModel):
    compression_factor: float = Field(alias="CompressionFactor")
    encoder_profile: Literal["high", "main"] = Field(alias="EncoderProfile")


class EncodingParametersModel(BaseModel):
    compression_factor: float = Field(alias="CompressionFactor")
    encoder_profile: Literal["high", "main"] = Field(alias="EncoderProfile")


class SourcePriorityModel(BaseModel):
    primary_source: Optional[str] = Field(default=None, alias="PrimarySource")


class MaintenanceModel(BaseModel):
    maintenance_day: Optional[
        Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = Field(default=None, alias="MaintenanceDay")
    maintenance_deadline: Optional[str] = Field(
        default=None, alias="MaintenanceDeadline"
    )
    maintenance_scheduled_date: Optional[str] = Field(
        default=None, alias="MaintenanceScheduledDate"
    )
    maintenance_start_hour: Optional[str] = Field(
        default=None, alias="MaintenanceStartHour"
    )


class FmtpRequestModel(BaseModel):
    channel_order: Optional[str] = Field(default=None, alias="ChannelOrder")
    colorimetry: Optional[
        Literal["BT2020", "BT2100", "BT601", "BT709", "ST2065-1", "ST2065-3", "XYZ"]
    ] = Field(default=None, alias="Colorimetry")
    exact_framerate: Optional[str] = Field(default=None, alias="ExactFramerate")
    par: Optional[str] = Field(default=None, alias="Par")
    range: Optional[Literal["FULL", "FULLPROTECT", "NARROW"]] = Field(
        default=None, alias="Range"
    )
    scan_mode: Optional[
        Literal["interlace", "progressive", "progressive-segmented-frame"]
    ] = Field(default=None, alias="ScanMode")
    tcs: Optional[
        Literal[
            "BT2100LINHLG",
            "BT2100LINPQ",
            "DENSITY",
            "HLG",
            "LINEAR",
            "PQ",
            "SDR",
            "ST2065-1",
            "ST428-1",
        ]
    ] = Field(default=None, alias="Tcs")


class FmtpModel(BaseModel):
    channel_order: Optional[str] = Field(default=None, alias="ChannelOrder")
    colorimetry: Optional[
        Literal["BT2020", "BT2100", "BT601", "BT709", "ST2065-1", "ST2065-3", "XYZ"]
    ] = Field(default=None, alias="Colorimetry")
    exact_framerate: Optional[str] = Field(default=None, alias="ExactFramerate")
    par: Optional[str] = Field(default=None, alias="Par")
    range: Optional[Literal["FULL", "FULLPROTECT", "NARROW"]] = Field(
        default=None, alias="Range"
    )
    scan_mode: Optional[
        Literal["interlace", "progressive", "progressive-segmented-frame"]
    ] = Field(default=None, alias="ScanMode")
    tcs: Optional[
        Literal[
            "BT2100LINHLG",
            "BT2100LINPQ",
            "DENSITY",
            "HLG",
            "LINEAR",
            "PQ",
            "SDR",
            "ST2065-1",
            "ST428-1",
        ]
    ] = Field(default=None, alias="Tcs")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEntitlementsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedEntitlementModel(BaseModel):
    entitlement_arn: str = Field(alias="EntitlementArn")
    entitlement_name: str = Field(alias="EntitlementName")
    data_transfer_subscriber_fee_percent: Optional[int] = Field(
        default=None, alias="DataTransferSubscriberFeePercent"
    )


class ListFlowsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOfferingsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListReservationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ResourceSpecificationModel(BaseModel):
    resource_type: Literal["Mbps_Outbound_Bandwidth"] = Field(alias="ResourceType")
    reserved_bitrate: Optional[int] = Field(default=None, alias="ReservedBitrate")


class TransportModel(BaseModel):
    protocol: Literal[
        "cdi",
        "fujitsu-qos",
        "rist",
        "rtp",
        "rtp-fec",
        "srt-caller",
        "srt-listener",
        "st2110-jpegxs",
        "zixi-pull",
        "zixi-push",
    ] = Field(alias="Protocol")
    cidr_allow_list: Optional[List[str]] = Field(default=None, alias="CidrAllowList")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    max_latency: Optional[int] = Field(default=None, alias="MaxLatency")
    max_sync_buffer: Optional[int] = Field(default=None, alias="MaxSyncBuffer")
    min_latency: Optional[int] = Field(default=None, alias="MinLatency")
    remote_id: Optional[str] = Field(default=None, alias="RemoteId")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    sender_ip_address: Optional[str] = Field(default=None, alias="SenderIpAddress")
    smoothing_latency: Optional[int] = Field(default=None, alias="SmoothingLatency")
    source_listener_address: Optional[str] = Field(
        default=None, alias="SourceListenerAddress"
    )
    source_listener_port: Optional[int] = Field(
        default=None, alias="SourceListenerPort"
    )
    stream_id: Optional[str] = Field(default=None, alias="StreamId")


class PurchaseOfferingRequestModel(BaseModel):
    offering_arn: str = Field(alias="OfferingArn")
    reservation_name: str = Field(alias="ReservationName")
    start: str = Field(alias="Start")


class RemoveFlowMediaStreamRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_stream_name: str = Field(alias="MediaStreamName")


class RemoveFlowOutputRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    output_arn: str = Field(alias="OutputArn")


class RemoveFlowSourceRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    source_arn: str = Field(alias="SourceArn")


class RemoveFlowVpcInterfaceRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    vpc_interface_name: str = Field(alias="VpcInterfaceName")


class RevokeFlowEntitlementRequestModel(BaseModel):
    entitlement_arn: str = Field(alias="EntitlementArn")
    flow_arn: str = Field(alias="FlowArn")


class StartFlowRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")


class StopFlowRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateEncryptionModel(BaseModel):
    algorithm: Optional[Literal["aes128", "aes192", "aes256"]] = Field(
        default=None, alias="Algorithm"
    )
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    key_type: Optional[Literal["speke", "srt-password", "static-key"]] = Field(
        default=None, alias="KeyType"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    url: Optional[str] = Field(default=None, alias="Url")


class UpdateMaintenanceModel(BaseModel):
    maintenance_day: Optional[
        Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = Field(default=None, alias="MaintenanceDay")
    maintenance_scheduled_date: Optional[str] = Field(
        default=None, alias="MaintenanceScheduledDate"
    )
    maintenance_start_hour: Optional[str] = Field(
        default=None, alias="MaintenanceStartHour"
    )


class DeleteFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    status: Literal[
        "ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveFlowMediaStreamResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_stream_name: str = Field(alias="MediaStreamName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveFlowOutputResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    output_arn: str = Field(alias="OutputArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveFlowSourceResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    source_arn: str = Field(alias="SourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveFlowVpcInterfaceResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    non_deleted_network_interface_ids: List[str] = Field(
        alias="NonDeletedNetworkInterfaceIds"
    )
    vpc_interface_name: str = Field(alias="VpcInterfaceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeFlowEntitlementResponseModel(BaseModel):
    entitlement_arn: str = Field(alias="EntitlementArn")
    flow_arn: str = Field(alias="FlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    status: Literal[
        "ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    status: Literal[
        "ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddFlowVpcInterfacesRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    vpc_interfaces: Sequence[VpcInterfaceRequestModel] = Field(alias="VpcInterfaces")


class AddFlowVpcInterfacesResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    vpc_interfaces: List[VpcInterfaceModel] = Field(alias="VpcInterfaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EntitlementModel(BaseModel):
    entitlement_arn: str = Field(alias="EntitlementArn")
    name: str = Field(alias="Name")
    subscribers: List[str] = Field(alias="Subscribers")
    data_transfer_subscriber_fee_percent: Optional[int] = Field(
        default=None, alias="DataTransferSubscriberFeePercent"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    entitlement_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="EntitlementStatus"
    )


class GrantEntitlementRequestModel(BaseModel):
    subscribers: Sequence[str] = Field(alias="Subscribers")
    data_transfer_subscriber_fee_percent: Optional[int] = Field(
        default=None, alias="DataTransferSubscriberFeePercent"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    entitlement_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="EntitlementStatus"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class DescribeFlowRequestFlowActiveWaitModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeFlowRequestFlowDeletedWaitModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeFlowRequestFlowStandbyWaitModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DestinationConfigurationRequestModel(BaseModel):
    destination_ip: str = Field(alias="DestinationIp")
    destination_port: int = Field(alias="DestinationPort")
    interface: InterfaceRequestModel = Field(alias="Interface")


class InputConfigurationRequestModel(BaseModel):
    input_port: int = Field(alias="InputPort")
    interface: InterfaceRequestModel = Field(alias="Interface")


class DestinationConfigurationModel(BaseModel):
    destination_ip: str = Field(alias="DestinationIp")
    destination_port: int = Field(alias="DestinationPort")
    interface: InterfaceModel = Field(alias="Interface")
    outbound_ip: str = Field(alias="OutboundIp")


class InputConfigurationModel(BaseModel):
    input_ip: str = Field(alias="InputIp")
    input_port: int = Field(alias="InputPort")
    interface: InterfaceModel = Field(alias="Interface")


class FailoverConfigModel(BaseModel):
    failover_mode: Optional[Literal["FAILOVER", "MERGE"]] = Field(
        default=None, alias="FailoverMode"
    )
    recovery_window: Optional[int] = Field(default=None, alias="RecoveryWindow")
    source_priority: Optional[SourcePriorityModel] = Field(
        default=None, alias="SourcePriority"
    )
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class UpdateFailoverConfigModel(BaseModel):
    failover_mode: Optional[Literal["FAILOVER", "MERGE"]] = Field(
        default=None, alias="FailoverMode"
    )
    recovery_window: Optional[int] = Field(default=None, alias="RecoveryWindow")
    source_priority: Optional[SourcePriorityModel] = Field(
        default=None, alias="SourcePriority"
    )
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class ListedFlowModel(BaseModel):
    availability_zone: str = Field(alias="AvailabilityZone")
    description: str = Field(alias="Description")
    flow_arn: str = Field(alias="FlowArn")
    name: str = Field(alias="Name")
    source_type: Literal["ENTITLED", "OWNED"] = Field(alias="SourceType")
    status: Literal[
        "ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    maintenance: Optional[MaintenanceModel] = Field(default=None, alias="Maintenance")


class MediaStreamAttributesRequestModel(BaseModel):
    fmtp: Optional[FmtpRequestModel] = Field(default=None, alias="Fmtp")
    lang: Optional[str] = Field(default=None, alias="Lang")


class MediaStreamAttributesModel(BaseModel):
    fmtp: FmtpModel = Field(alias="Fmtp")
    lang: Optional[str] = Field(default=None, alias="Lang")


class ListEntitlementsRequestListEntitlementsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFlowsRequestListFlowsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOfferingsRequestListOfferingsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReservationsRequestListReservationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEntitlementsResponseModel(BaseModel):
    entitlements: List[ListedEntitlementModel] = Field(alias="Entitlements")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OfferingModel(BaseModel):
    currency_code: str = Field(alias="CurrencyCode")
    duration: int = Field(alias="Duration")
    duration_units: Literal["MONTHS"] = Field(alias="DurationUnits")
    offering_arn: str = Field(alias="OfferingArn")
    offering_description: str = Field(alias="OfferingDescription")
    price_per_unit: str = Field(alias="PricePerUnit")
    price_units: Literal["HOURLY"] = Field(alias="PriceUnits")
    resource_specification: ResourceSpecificationModel = Field(
        alias="ResourceSpecification"
    )


class ReservationModel(BaseModel):
    currency_code: str = Field(alias="CurrencyCode")
    duration: int = Field(alias="Duration")
    duration_units: Literal["MONTHS"] = Field(alias="DurationUnits")
    end: str = Field(alias="End")
    offering_arn: str = Field(alias="OfferingArn")
    offering_description: str = Field(alias="OfferingDescription")
    price_per_unit: str = Field(alias="PricePerUnit")
    price_units: Literal["HOURLY"] = Field(alias="PriceUnits")
    reservation_arn: str = Field(alias="ReservationArn")
    reservation_name: str = Field(alias="ReservationName")
    reservation_state: Literal["ACTIVE", "CANCELED", "EXPIRED", "PROCESSING"] = Field(
        alias="ReservationState"
    )
    resource_specification: ResourceSpecificationModel = Field(
        alias="ResourceSpecification"
    )
    start: str = Field(alias="Start")


class UpdateFlowEntitlementRequestModel(BaseModel):
    entitlement_arn: str = Field(alias="EntitlementArn")
    flow_arn: str = Field(alias="FlowArn")
    description: Optional[str] = Field(default=None, alias="Description")
    encryption: Optional[UpdateEncryptionModel] = Field(
        default=None, alias="Encryption"
    )
    entitlement_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="EntitlementStatus"
    )
    subscribers: Optional[Sequence[str]] = Field(default=None, alias="Subscribers")


class GrantFlowEntitlementsResponseModel(BaseModel):
    entitlements: List[EntitlementModel] = Field(alias="Entitlements")
    flow_arn: str = Field(alias="FlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowEntitlementResponseModel(BaseModel):
    entitlement: EntitlementModel = Field(alias="Entitlement")
    flow_arn: str = Field(alias="FlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GrantFlowEntitlementsRequestModel(BaseModel):
    entitlements: Sequence[GrantEntitlementRequestModel] = Field(alias="Entitlements")
    flow_arn: str = Field(alias="FlowArn")


class MediaStreamOutputConfigurationRequestModel(BaseModel):
    encoding_name: Literal["jxsv", "pcm", "raw", "smpte291"] = Field(
        alias="EncodingName"
    )
    media_stream_name: str = Field(alias="MediaStreamName")
    destination_configurations: Optional[
        Sequence[DestinationConfigurationRequestModel]
    ] = Field(default=None, alias="DestinationConfigurations")
    encoding_parameters: Optional[EncodingParametersRequestModel] = Field(
        default=None, alias="EncodingParameters"
    )


class MediaStreamSourceConfigurationRequestModel(BaseModel):
    encoding_name: Literal["jxsv", "pcm", "raw", "smpte291"] = Field(
        alias="EncodingName"
    )
    media_stream_name: str = Field(alias="MediaStreamName")
    input_configurations: Optional[Sequence[InputConfigurationRequestModel]] = Field(
        default=None, alias="InputConfigurations"
    )


class MediaStreamOutputConfigurationModel(BaseModel):
    encoding_name: Literal["jxsv", "pcm", "raw", "smpte291"] = Field(
        alias="EncodingName"
    )
    media_stream_name: str = Field(alias="MediaStreamName")
    destination_configurations: Optional[List[DestinationConfigurationModel]] = Field(
        default=None, alias="DestinationConfigurations"
    )
    encoding_parameters: Optional[EncodingParametersModel] = Field(
        default=None, alias="EncodingParameters"
    )


class MediaStreamSourceConfigurationModel(BaseModel):
    encoding_name: Literal["jxsv", "pcm", "raw", "smpte291"] = Field(
        alias="EncodingName"
    )
    media_stream_name: str = Field(alias="MediaStreamName")
    input_configurations: Optional[List[InputConfigurationModel]] = Field(
        default=None, alias="InputConfigurations"
    )


class UpdateFlowRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    source_failover_config: Optional[UpdateFailoverConfigModel] = Field(
        default=None, alias="SourceFailoverConfig"
    )
    maintenance: Optional[UpdateMaintenanceModel] = Field(
        default=None, alias="Maintenance"
    )


class ListFlowsResponseModel(BaseModel):
    flows: List[ListedFlowModel] = Field(alias="Flows")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddMediaStreamRequestModel(BaseModel):
    media_stream_id: int = Field(alias="MediaStreamId")
    media_stream_name: str = Field(alias="MediaStreamName")
    media_stream_type: Literal["ancillary-data", "audio", "video"] = Field(
        alias="MediaStreamType"
    )
    attributes: Optional[MediaStreamAttributesRequestModel] = Field(
        default=None, alias="Attributes"
    )
    clock_rate: Optional[int] = Field(default=None, alias="ClockRate")
    description: Optional[str] = Field(default=None, alias="Description")
    video_format: Optional[str] = Field(default=None, alias="VideoFormat")


class UpdateFlowMediaStreamRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_stream_name: str = Field(alias="MediaStreamName")
    attributes: Optional[MediaStreamAttributesRequestModel] = Field(
        default=None, alias="Attributes"
    )
    clock_rate: Optional[int] = Field(default=None, alias="ClockRate")
    description: Optional[str] = Field(default=None, alias="Description")
    media_stream_type: Optional[Literal["ancillary-data", "audio", "video"]] = Field(
        default=None, alias="MediaStreamType"
    )
    video_format: Optional[str] = Field(default=None, alias="VideoFormat")


class MediaStreamModel(BaseModel):
    fmt: int = Field(alias="Fmt")
    media_stream_id: int = Field(alias="MediaStreamId")
    media_stream_name: str = Field(alias="MediaStreamName")
    media_stream_type: Literal["ancillary-data", "audio", "video"] = Field(
        alias="MediaStreamType"
    )
    attributes: Optional[MediaStreamAttributesModel] = Field(
        default=None, alias="Attributes"
    )
    clock_rate: Optional[int] = Field(default=None, alias="ClockRate")
    description: Optional[str] = Field(default=None, alias="Description")
    video_format: Optional[str] = Field(default=None, alias="VideoFormat")


class DescribeOfferingResponseModel(BaseModel):
    offering: OfferingModel = Field(alias="Offering")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOfferingsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    offerings: List[OfferingModel] = Field(alias="Offerings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservationResponseModel(BaseModel):
    reservation: ReservationModel = Field(alias="Reservation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReservationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reservations: List[ReservationModel] = Field(alias="Reservations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseOfferingResponseModel(BaseModel):
    reservation: ReservationModel = Field(alias="Reservation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddOutputRequestModel(BaseModel):
    protocol: Literal[
        "cdi",
        "fujitsu-qos",
        "rist",
        "rtp",
        "rtp-fec",
        "srt-caller",
        "srt-listener",
        "st2110-jpegxs",
        "zixi-pull",
        "zixi-push",
    ] = Field(alias="Protocol")
    cidr_allow_list: Optional[Sequence[str]] = Field(
        default=None, alias="CidrAllowList"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    destination: Optional[str] = Field(default=None, alias="Destination")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    max_latency: Optional[int] = Field(default=None, alias="MaxLatency")
    media_stream_output_configurations: Optional[
        Sequence[MediaStreamOutputConfigurationRequestModel]
    ] = Field(default=None, alias="MediaStreamOutputConfigurations")
    min_latency: Optional[int] = Field(default=None, alias="MinLatency")
    name: Optional[str] = Field(default=None, alias="Name")
    port: Optional[int] = Field(default=None, alias="Port")
    remote_id: Optional[str] = Field(default=None, alias="RemoteId")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    smoothing_latency: Optional[int] = Field(default=None, alias="SmoothingLatency")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")
    vpc_interface_attachment: Optional[VpcInterfaceAttachmentModel] = Field(
        default=None, alias="VpcInterfaceAttachment"
    )


class UpdateFlowOutputRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    output_arn: str = Field(alias="OutputArn")
    cidr_allow_list: Optional[Sequence[str]] = Field(
        default=None, alias="CidrAllowList"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    destination: Optional[str] = Field(default=None, alias="Destination")
    encryption: Optional[UpdateEncryptionModel] = Field(
        default=None, alias="Encryption"
    )
    max_latency: Optional[int] = Field(default=None, alias="MaxLatency")
    media_stream_output_configurations: Optional[
        Sequence[MediaStreamOutputConfigurationRequestModel]
    ] = Field(default=None, alias="MediaStreamOutputConfigurations")
    min_latency: Optional[int] = Field(default=None, alias="MinLatency")
    port: Optional[int] = Field(default=None, alias="Port")
    protocol: Optional[
        Literal[
            "cdi",
            "fujitsu-qos",
            "rist",
            "rtp",
            "rtp-fec",
            "srt-caller",
            "srt-listener",
            "st2110-jpegxs",
            "zixi-pull",
            "zixi-push",
        ]
    ] = Field(default=None, alias="Protocol")
    remote_id: Optional[str] = Field(default=None, alias="RemoteId")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    sender_ip_address: Optional[str] = Field(default=None, alias="SenderIpAddress")
    smoothing_latency: Optional[int] = Field(default=None, alias="SmoothingLatency")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")
    vpc_interface_attachment: Optional[VpcInterfaceAttachmentModel] = Field(
        default=None, alias="VpcInterfaceAttachment"
    )


class SetSourceRequestModel(BaseModel):
    decryption: Optional[EncryptionModel] = Field(default=None, alias="Decryption")
    description: Optional[str] = Field(default=None, alias="Description")
    entitlement_arn: Optional[str] = Field(default=None, alias="EntitlementArn")
    ingest_port: Optional[int] = Field(default=None, alias="IngestPort")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    max_latency: Optional[int] = Field(default=None, alias="MaxLatency")
    max_sync_buffer: Optional[int] = Field(default=None, alias="MaxSyncBuffer")
    media_stream_source_configurations: Optional[
        Sequence[MediaStreamSourceConfigurationRequestModel]
    ] = Field(default=None, alias="MediaStreamSourceConfigurations")
    min_latency: Optional[int] = Field(default=None, alias="MinLatency")
    name: Optional[str] = Field(default=None, alias="Name")
    protocol: Optional[
        Literal[
            "cdi",
            "fujitsu-qos",
            "rist",
            "rtp",
            "rtp-fec",
            "srt-caller",
            "srt-listener",
            "st2110-jpegxs",
            "zixi-pull",
            "zixi-push",
        ]
    ] = Field(default=None, alias="Protocol")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    sender_ip_address: Optional[str] = Field(default=None, alias="SenderIpAddress")
    source_listener_address: Optional[str] = Field(
        default=None, alias="SourceListenerAddress"
    )
    source_listener_port: Optional[int] = Field(
        default=None, alias="SourceListenerPort"
    )
    stream_id: Optional[str] = Field(default=None, alias="StreamId")
    vpc_interface_name: Optional[str] = Field(default=None, alias="VpcInterfaceName")
    whitelist_cidr: Optional[str] = Field(default=None, alias="WhitelistCidr")


class UpdateFlowSourceRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    source_arn: str = Field(alias="SourceArn")
    decryption: Optional[UpdateEncryptionModel] = Field(
        default=None, alias="Decryption"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    entitlement_arn: Optional[str] = Field(default=None, alias="EntitlementArn")
    ingest_port: Optional[int] = Field(default=None, alias="IngestPort")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    max_latency: Optional[int] = Field(default=None, alias="MaxLatency")
    max_sync_buffer: Optional[int] = Field(default=None, alias="MaxSyncBuffer")
    media_stream_source_configurations: Optional[
        Sequence[MediaStreamSourceConfigurationRequestModel]
    ] = Field(default=None, alias="MediaStreamSourceConfigurations")
    min_latency: Optional[int] = Field(default=None, alias="MinLatency")
    protocol: Optional[
        Literal[
            "cdi",
            "fujitsu-qos",
            "rist",
            "rtp",
            "rtp-fec",
            "srt-caller",
            "srt-listener",
            "st2110-jpegxs",
            "zixi-pull",
            "zixi-push",
        ]
    ] = Field(default=None, alias="Protocol")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    sender_ip_address: Optional[str] = Field(default=None, alias="SenderIpAddress")
    source_listener_address: Optional[str] = Field(
        default=None, alias="SourceListenerAddress"
    )
    source_listener_port: Optional[int] = Field(
        default=None, alias="SourceListenerPort"
    )
    stream_id: Optional[str] = Field(default=None, alias="StreamId")
    vpc_interface_name: Optional[str] = Field(default=None, alias="VpcInterfaceName")
    whitelist_cidr: Optional[str] = Field(default=None, alias="WhitelistCidr")


class OutputModel(BaseModel):
    name: str = Field(alias="Name")
    output_arn: str = Field(alias="OutputArn")
    data_transfer_subscriber_fee_percent: Optional[int] = Field(
        default=None, alias="DataTransferSubscriberFeePercent"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    destination: Optional[str] = Field(default=None, alias="Destination")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    entitlement_arn: Optional[str] = Field(default=None, alias="EntitlementArn")
    listener_address: Optional[str] = Field(default=None, alias="ListenerAddress")
    media_live_input_arn: Optional[str] = Field(default=None, alias="MediaLiveInputArn")
    media_stream_output_configurations: Optional[
        List[MediaStreamOutputConfigurationModel]
    ] = Field(default=None, alias="MediaStreamOutputConfigurations")
    port: Optional[int] = Field(default=None, alias="Port")
    transport: Optional[TransportModel] = Field(default=None, alias="Transport")
    vpc_interface_attachment: Optional[VpcInterfaceAttachmentModel] = Field(
        default=None, alias="VpcInterfaceAttachment"
    )


class SourceModel(BaseModel):
    name: str = Field(alias="Name")
    source_arn: str = Field(alias="SourceArn")
    data_transfer_subscriber_fee_percent: Optional[int] = Field(
        default=None, alias="DataTransferSubscriberFeePercent"
    )
    decryption: Optional[EncryptionModel] = Field(default=None, alias="Decryption")
    description: Optional[str] = Field(default=None, alias="Description")
    entitlement_arn: Optional[str] = Field(default=None, alias="EntitlementArn")
    ingest_ip: Optional[str] = Field(default=None, alias="IngestIp")
    ingest_port: Optional[int] = Field(default=None, alias="IngestPort")
    media_stream_source_configurations: Optional[
        List[MediaStreamSourceConfigurationModel]
    ] = Field(default=None, alias="MediaStreamSourceConfigurations")
    sender_control_port: Optional[int] = Field(default=None, alias="SenderControlPort")
    sender_ip_address: Optional[str] = Field(default=None, alias="SenderIpAddress")
    transport: Optional[TransportModel] = Field(default=None, alias="Transport")
    vpc_interface_name: Optional[str] = Field(default=None, alias="VpcInterfaceName")
    whitelist_cidr: Optional[str] = Field(default=None, alias="WhitelistCidr")


class AddFlowMediaStreamsRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_streams: Sequence[AddMediaStreamRequestModel] = Field(alias="MediaStreams")


class AddFlowMediaStreamsResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_streams: List[MediaStreamModel] = Field(alias="MediaStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowMediaStreamResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    media_stream: MediaStreamModel = Field(alias="MediaStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddFlowOutputsRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    outputs: Sequence[AddOutputRequestModel] = Field(alias="Outputs")


class AddFlowSourcesRequestModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    sources: Sequence[SetSourceRequestModel] = Field(alias="Sources")


class CreateFlowRequestModel(BaseModel):
    name: str = Field(alias="Name")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    entitlements: Optional[Sequence[GrantEntitlementRequestModel]] = Field(
        default=None, alias="Entitlements"
    )
    media_streams: Optional[Sequence[AddMediaStreamRequestModel]] = Field(
        default=None, alias="MediaStreams"
    )
    outputs: Optional[Sequence[AddOutputRequestModel]] = Field(
        default=None, alias="Outputs"
    )
    source: Optional[SetSourceRequestModel] = Field(default=None, alias="Source")
    source_failover_config: Optional[FailoverConfigModel] = Field(
        default=None, alias="SourceFailoverConfig"
    )
    sources: Optional[Sequence[SetSourceRequestModel]] = Field(
        default=None, alias="Sources"
    )
    vpc_interfaces: Optional[Sequence[VpcInterfaceRequestModel]] = Field(
        default=None, alias="VpcInterfaces"
    )
    maintenance: Optional[AddMaintenanceModel] = Field(
        default=None, alias="Maintenance"
    )


class AddFlowOutputsResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    outputs: List[OutputModel] = Field(alias="Outputs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowOutputResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    output: OutputModel = Field(alias="Output")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddFlowSourcesResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    sources: List[SourceModel] = Field(alias="Sources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FlowModel(BaseModel):
    availability_zone: str = Field(alias="AvailabilityZone")
    entitlements: List[EntitlementModel] = Field(alias="Entitlements")
    flow_arn: str = Field(alias="FlowArn")
    name: str = Field(alias="Name")
    outputs: List[OutputModel] = Field(alias="Outputs")
    source: SourceModel = Field(alias="Source")
    status: Literal[
        "ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    description: Optional[str] = Field(default=None, alias="Description")
    egress_ip: Optional[str] = Field(default=None, alias="EgressIp")
    media_streams: Optional[List[MediaStreamModel]] = Field(
        default=None, alias="MediaStreams"
    )
    source_failover_config: Optional[FailoverConfigModel] = Field(
        default=None, alias="SourceFailoverConfig"
    )
    sources: Optional[List[SourceModel]] = Field(default=None, alias="Sources")
    vpc_interfaces: Optional[List[VpcInterfaceModel]] = Field(
        default=None, alias="VpcInterfaces"
    )
    maintenance: Optional[MaintenanceModel] = Field(default=None, alias="Maintenance")


class UpdateFlowSourceResponseModel(BaseModel):
    flow_arn: str = Field(alias="FlowArn")
    source: SourceModel = Field(alias="Source")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFlowResponseModel(BaseModel):
    flow: FlowModel = Field(alias="Flow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFlowResponseModel(BaseModel):
    flow: FlowModel = Field(alias="Flow")
    messages: MessagesModel = Field(alias="Messages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowResponseModel(BaseModel):
    flow: FlowModel = Field(alias="Flow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
