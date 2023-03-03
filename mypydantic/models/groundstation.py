# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ComponentVersionModel(BaseModel):
    component_type: Literal["DIGITIZER", "LAMINAR_FLOW", "PRISM"] = Field(
        alias="componentType"
    )
    versions: Sequence[str] = Field(alias="versions")


class AggregateStatusModel(BaseModel):
    status: Literal["ACTIVE", "FAILED", "INACTIVE", "SUCCESS"] = Field(alias="status")
    signature_map: Optional[Mapping[str, bool]] = Field(
        default=None, alias="signatureMap"
    )


class AntennaDemodDecodeDetailsModel(BaseModel):
    output_node: Optional[str] = Field(default=None, alias="outputNode")


class DecodeConfigModel(BaseModel):
    unvalidated_js_on: str = Field(alias="unvalidatedJSON")


class DemodulationConfigModel(BaseModel):
    unvalidated_js_on: str = Field(alias="unvalidatedJSON")


class EirpModel(BaseModel):
    units: Literal["dBW"] = Field(alias="units")
    value: float = Field(alias="value")


class CancelContactRequestModel(BaseModel):
    contact_id: str = Field(alias="contactId")


class ComponentStatusDataModel(BaseModel):
    capability_arn: str = Field(alias="capabilityArn")
    component_type: Literal["DIGITIZER", "LAMINAR_FLOW", "PRISM"] = Field(
        alias="componentType"
    )
    dataflow_id: str = Field(alias="dataflowId")
    status: Literal["ACTIVE", "FAILED", "INACTIVE", "SUCCESS"] = Field(alias="status")
    bytes_received: Optional[int] = Field(default=None, alias="bytesReceived")
    bytes_sent: Optional[int] = Field(default=None, alias="bytesSent")
    packets_dropped: Optional[int] = Field(default=None, alias="packetsDropped")


class S3RecordingDetailsModel(BaseModel):
    bucket_arn: Optional[str] = Field(default=None, alias="bucketArn")
    key_template: Optional[str] = Field(default=None, alias="keyTemplate")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConfigListItemModel(BaseModel):
    config_arn: Optional[str] = Field(default=None, alias="configArn")
    config_id: Optional[str] = Field(default=None, alias="configId")
    config_type: Optional[
        Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "s3-recording",
            "tracking",
            "uplink-echo",
        ]
    ] = Field(default=None, alias="configType")
    name: Optional[str] = Field(default=None, alias="name")


class DataflowEndpointConfigModel(BaseModel):
    dataflow_endpoint_name: str = Field(alias="dataflowEndpointName")
    dataflow_endpoint_region: Optional[str] = Field(
        default=None, alias="dataflowEndpointRegion"
    )


class S3RecordingConfigModel(BaseModel):
    bucket_arn: str = Field(alias="bucketArn")
    role_arn: str = Field(alias="roleArn")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class TrackingConfigModel(BaseModel):
    autotrack: Literal["PREFERRED", "REMOVED", "REQUIRED"] = Field(alias="autotrack")


class UplinkEchoConfigModel(BaseModel):
    antenna_uplink_config_arn: str = Field(alias="antennaUplinkConfigArn")
    enabled: bool = Field(alias="enabled")


class SocketAddressModel(BaseModel):
    name: str = Field(alias="name")
    port: int = Field(alias="port")


class ElevationModel(BaseModel):
    unit: Literal["DEGREE_ANGLE", "RADIAN"] = Field(alias="unit")
    value: float = Field(alias="value")


class KmsKeyModel(BaseModel):
    kms_alias_arn: Optional[str] = Field(default=None, alias="kmsAliasArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class DataflowEndpointListItemModel(BaseModel):
    dataflow_endpoint_group_arn: Optional[str] = Field(
        default=None, alias="dataflowEndpointGroupArn"
    )
    dataflow_endpoint_group_id: Optional[str] = Field(
        default=None, alias="dataflowEndpointGroupId"
    )


class DeleteConfigRequestModel(BaseModel):
    config_id: str = Field(alias="configId")
    config_type: Literal[
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "antenna-uplink",
        "dataflow-endpoint",
        "s3-recording",
        "tracking",
        "uplink-echo",
    ] = Field(alias="configType")


class DeleteDataflowEndpointGroupRequestModel(BaseModel):
    dataflow_endpoint_group_id: str = Field(alias="dataflowEndpointGroupId")


class DeleteEphemerisRequestModel(BaseModel):
    ephemeris_id: str = Field(alias="ephemerisId")


class DeleteMissionProfileRequestModel(BaseModel):
    mission_profile_id: str = Field(alias="missionProfileId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeContactRequestModel(BaseModel):
    contact_id: str = Field(alias="contactId")


class DescribeEphemerisRequestModel(BaseModel):
    ephemeris_id: str = Field(alias="ephemerisId")


class DiscoveryDataModel(BaseModel):
    capability_arns: Sequence[str] = Field(alias="capabilityArns")
    private_ip_addresses: Sequence[str] = Field(alias="privateIpAddresses")
    public_ip_addresses: Sequence[str] = Field(alias="publicIpAddresses")


class SecurityDetailsModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    security_group_ids: Sequence[str] = Field(alias="securityGroupIds")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")


class S3ObjectModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")
    version: Optional[str] = Field(default=None, alias="version")


class EphemerisMetaDataModel(BaseModel):
    source: Literal["CUSTOMER_PROVIDED", "SPACE_TRACK"] = Field(alias="source")
    ephemeris_id: Optional[str] = Field(default=None, alias="ephemerisId")
    epoch: Optional[datetime] = Field(default=None, alias="epoch")
    name: Optional[str] = Field(default=None, alias="name")


class FrequencyBandwidthModel(BaseModel):
    units: Literal["GHz", "MHz", "kHz"] = Field(alias="units")
    value: float = Field(alias="value")


class FrequencyModel(BaseModel):
    units: Literal["GHz", "MHz", "kHz"] = Field(alias="units")
    value: float = Field(alias="value")


class GetAgentConfigurationRequestModel(BaseModel):
    agent_id: str = Field(alias="agentId")


class GetConfigRequestModel(BaseModel):
    config_id: str = Field(alias="configId")
    config_type: Literal[
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "antenna-uplink",
        "dataflow-endpoint",
        "s3-recording",
        "tracking",
        "uplink-echo",
    ] = Field(alias="configType")


class GetDataflowEndpointGroupRequestModel(BaseModel):
    dataflow_endpoint_group_id: str = Field(alias="dataflowEndpointGroupId")


class GetMinuteUsageRequestModel(BaseModel):
    month: int = Field(alias="month")
    year: int = Field(alias="year")


class GetMissionProfileRequestModel(BaseModel):
    mission_profile_id: str = Field(alias="missionProfileId")


class GetSatelliteRequestModel(BaseModel):
    satellite_id: str = Field(alias="satelliteId")


class GroundStationDataModel(BaseModel):
    ground_station_id: Optional[str] = Field(default=None, alias="groundStationId")
    ground_station_name: Optional[str] = Field(default=None, alias="groundStationName")
    region: Optional[str] = Field(default=None, alias="region")


class IntegerRangeModel(BaseModel):
    maximum: int = Field(alias="maximum")
    minimum: int = Field(alias="minimum")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListContactsRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    start_time: Union[datetime, str] = Field(alias="startTime")
    status_list: Sequence[
        Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "AWS_FAILED",
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ]
    ] = Field(alias="statusList")
    ground_station: Optional[str] = Field(default=None, alias="groundStation")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    mission_profile_arn: Optional[str] = Field(default=None, alias="missionProfileArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    satellite_arn: Optional[str] = Field(default=None, alias="satelliteArn")


class ListDataflowEndpointGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEphemeridesRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    satellite_id: str = Field(alias="satelliteId")
    start_time: Union[datetime, str] = Field(alias="startTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    status_list: Optional[
        Sequence[
            Literal["DISABLED", "ENABLED", "ERROR", "EXPIRED", "INVALID", "VALIDATING"]
        ]
    ] = Field(default=None, alias="statusList")


class ListGroundStationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    satellite_id: Optional[str] = Field(default=None, alias="satelliteId")


class ListMissionProfilesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MissionProfileListItemModel(BaseModel):
    mission_profile_arn: Optional[str] = Field(default=None, alias="missionProfileArn")
    mission_profile_id: Optional[str] = Field(default=None, alias="missionProfileId")
    name: Optional[str] = Field(default=None, alias="name")
    region: Optional[str] = Field(default=None, alias="region")


class ListSatellitesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ReserveContactRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    ground_station: str = Field(alias="groundStation")
    mission_profile_arn: str = Field(alias="missionProfileArn")
    satellite_arn: str = Field(alias="satelliteArn")
    start_time: Union[datetime, str] = Field(alias="startTime")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class TimeRangeModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    start_time: Union[datetime, str] = Field(alias="startTime")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateEphemerisRequestModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    ephemeris_id: str = Field(alias="ephemerisId")
    name: Optional[str] = Field(default=None, alias="name")
    priority: Optional[int] = Field(default=None, alias="priority")


class AgentDetailsModel(BaseModel):
    agent_version: str = Field(alias="agentVersion")
    component_versions: Sequence[ComponentVersionModel] = Field(
        alias="componentVersions"
    )
    instance_id: str = Field(alias="instanceId")
    instance_type: str = Field(alias="instanceType")
    reserved_cpu_cores: Sequence[int] = Field(alias="reservedCpuCores")


class UpdateAgentStatusRequestModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    aggregate_status: AggregateStatusModel = Field(alias="aggregateStatus")
    component_statuses: Sequence[ComponentStatusDataModel] = Field(
        alias="componentStatuses"
    )
    task_id: str = Field(alias="taskId")


class ConfigIdResponseModel(BaseModel):
    config_arn: str = Field(alias="configArn")
    config_id: str = Field(alias="configId")
    config_type: Literal[
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "antenna-uplink",
        "dataflow-endpoint",
        "s3-recording",
        "tracking",
        "uplink-echo",
    ] = Field(alias="configType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContactIdResponseModel(BaseModel):
    contact_id: str = Field(alias="contactId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataflowEndpointGroupIdResponseModel(BaseModel):
    dataflow_endpoint_group_id: str = Field(alias="dataflowEndpointGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EphemerisIdResponseModel(BaseModel):
    ephemeris_id: str = Field(alias="ephemerisId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAgentConfigurationResponseModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    tasking_document: str = Field(alias="taskingDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMinuteUsageResponseModel(BaseModel):
    estimated_minutes_remaining: int = Field(alias="estimatedMinutesRemaining")
    is_reserved_minutes_customer: bool = Field(alias="isReservedMinutesCustomer")
    total_reserved_minute_allocation: int = Field(alias="totalReservedMinuteAllocation")
    total_scheduled_minutes: int = Field(alias="totalScheduledMinutes")
    upcoming_minutes_scheduled: int = Field(alias="upcomingMinutesScheduled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MissionProfileIdResponseModel(BaseModel):
    mission_profile_id: str = Field(alias="missionProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterAgentResponseModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAgentStatusResponseModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigsResponseModel(BaseModel):
    config_list: List[ConfigListItemModel] = Field(alias="configList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectionDetailsModel(BaseModel):
    socket_address: SocketAddressModel = Field(alias="socketAddress")
    mtu: Optional[int] = Field(default=None, alias="mtu")


class DataflowEndpointModel(BaseModel):
    address: Optional[SocketAddressModel] = Field(default=None, alias="address")
    mtu: Optional[int] = Field(default=None, alias="mtu")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[
        Literal["created", "creating", "deleted", "deleting", "failed"]
    ] = Field(default=None, alias="status")


class ContactDataModel(BaseModel):
    contact_id: Optional[str] = Field(default=None, alias="contactId")
    contact_status: Optional[
        Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "AWS_FAILED",
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ]
    ] = Field(default=None, alias="contactStatus")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    ground_station: Optional[str] = Field(default=None, alias="groundStation")
    maximum_elevation: Optional[ElevationModel] = Field(
        default=None, alias="maximumElevation"
    )
    mission_profile_arn: Optional[str] = Field(default=None, alias="missionProfileArn")
    post_pass_end_time: Optional[datetime] = Field(
        default=None, alias="postPassEndTime"
    )
    pre_pass_start_time: Optional[datetime] = Field(
        default=None, alias="prePassStartTime"
    )
    region: Optional[str] = Field(default=None, alias="region")
    satellite_arn: Optional[str] = Field(default=None, alias="satelliteArn")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateMissionProfileRequestModel(BaseModel):
    dataflow_edges: Sequence[Sequence[str]] = Field(alias="dataflowEdges")
    minimum_viable_contact_duration_seconds: int = Field(
        alias="minimumViableContactDurationSeconds"
    )
    name: str = Field(alias="name")
    tracking_config_arn: str = Field(alias="trackingConfigArn")
    contact_post_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPostPassDurationSeconds"
    )
    contact_pre_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPrePassDurationSeconds"
    )
    streams_kms_key: Optional[KmsKeyModel] = Field(default=None, alias="streamsKmsKey")
    streams_kms_role: Optional[str] = Field(default=None, alias="streamsKmsRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetMissionProfileResponseModel(BaseModel):
    contact_post_pass_duration_seconds: int = Field(
        alias="contactPostPassDurationSeconds"
    )
    contact_pre_pass_duration_seconds: int = Field(
        alias="contactPrePassDurationSeconds"
    )
    dataflow_edges: List[List[str]] = Field(alias="dataflowEdges")
    minimum_viable_contact_duration_seconds: int = Field(
        alias="minimumViableContactDurationSeconds"
    )
    mission_profile_arn: str = Field(alias="missionProfileArn")
    mission_profile_id: str = Field(alias="missionProfileId")
    name: str = Field(alias="name")
    region: str = Field(alias="region")
    streams_kms_key: KmsKeyModel = Field(alias="streamsKmsKey")
    streams_kms_role: str = Field(alias="streamsKmsRole")
    tags: Dict[str, str] = Field(alias="tags")
    tracking_config_arn: str = Field(alias="trackingConfigArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMissionProfileRequestModel(BaseModel):
    mission_profile_id: str = Field(alias="missionProfileId")
    contact_post_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPostPassDurationSeconds"
    )
    contact_pre_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPrePassDurationSeconds"
    )
    dataflow_edges: Optional[Sequence[Sequence[str]]] = Field(
        default=None, alias="dataflowEdges"
    )
    minimum_viable_contact_duration_seconds: Optional[int] = Field(
        default=None, alias="minimumViableContactDurationSeconds"
    )
    name: Optional[str] = Field(default=None, alias="name")
    streams_kms_key: Optional[KmsKeyModel] = Field(default=None, alias="streamsKmsKey")
    streams_kms_role: Optional[str] = Field(default=None, alias="streamsKmsRole")
    tracking_config_arn: Optional[str] = Field(default=None, alias="trackingConfigArn")


class ListDataflowEndpointGroupsResponseModel(BaseModel):
    dataflow_endpoint_group_list: List[DataflowEndpointListItemModel] = Field(
        alias="dataflowEndpointGroupList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContactRequestContactScheduledWaitModel(BaseModel):
    contact_id: str = Field(alias="contactId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class EphemerisDescriptionModel(BaseModel):
    ephemeris_data: Optional[str] = Field(default=None, alias="ephemerisData")
    source_s3_object: Optional[S3ObjectModel] = Field(
        default=None, alias="sourceS3Object"
    )


class EphemerisItemModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    ephemeris_id: Optional[str] = Field(default=None, alias="ephemerisId")
    name: Optional[str] = Field(default=None, alias="name")
    priority: Optional[int] = Field(default=None, alias="priority")
    source_s3_object: Optional[S3ObjectModel] = Field(
        default=None, alias="sourceS3Object"
    )
    status: Optional[
        Literal["DISABLED", "ENABLED", "ERROR", "EXPIRED", "INVALID", "VALIDATING"]
    ] = Field(default=None, alias="status")


class OEMEphemerisModel(BaseModel):
    oem_data: Optional[str] = Field(default=None, alias="oemData")
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="s3Object")


class GetSatelliteResponseModel(BaseModel):
    current_ephemeris: EphemerisMetaDataModel = Field(alias="currentEphemeris")
    ground_stations: List[str] = Field(alias="groundStations")
    norad_satellite_id: int = Field(alias="noradSatelliteID")
    satellite_arn: str = Field(alias="satelliteArn")
    satellite_id: str = Field(alias="satelliteId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SatelliteListItemModel(BaseModel):
    current_ephemeris: Optional[EphemerisMetaDataModel] = Field(
        default=None, alias="currentEphemeris"
    )
    ground_stations: Optional[List[str]] = Field(default=None, alias="groundStations")
    norad_satellite_id: Optional[int] = Field(default=None, alias="noradSatelliteID")
    satellite_arn: Optional[str] = Field(default=None, alias="satelliteArn")
    satellite_id: Optional[str] = Field(default=None, alias="satelliteId")


class SpectrumConfigModel(BaseModel):
    bandwidth: FrequencyBandwidthModel = Field(alias="bandwidth")
    center_frequency: FrequencyModel = Field(alias="centerFrequency")
    polarization: Optional[Literal["LEFT_HAND", "NONE", "RIGHT_HAND"]] = Field(
        default=None, alias="polarization"
    )


class UplinkSpectrumConfigModel(BaseModel):
    center_frequency: FrequencyModel = Field(alias="centerFrequency")
    polarization: Optional[Literal["LEFT_HAND", "NONE", "RIGHT_HAND"]] = Field(
        default=None, alias="polarization"
    )


class ListGroundStationsResponseModel(BaseModel):
    ground_station_list: List[GroundStationDataModel] = Field(alias="groundStationList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RangedSocketAddressModel(BaseModel):
    name: str = Field(alias="name")
    port_range: IntegerRangeModel = Field(alias="portRange")


class ListConfigsRequestListConfigsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContactsRequestListContactsPaginateModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    start_time: Union[datetime, str] = Field(alias="startTime")
    status_list: Sequence[
        Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "AWS_FAILED",
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ]
    ] = Field(alias="statusList")
    ground_station: Optional[str] = Field(default=None, alias="groundStation")
    mission_profile_arn: Optional[str] = Field(default=None, alias="missionProfileArn")
    satellite_arn: Optional[str] = Field(default=None, alias="satelliteArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEphemeridesRequestListEphemeridesPaginateModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    satellite_id: str = Field(alias="satelliteId")
    start_time: Union[datetime, str] = Field(alias="startTime")
    status_list: Optional[
        Sequence[
            Literal["DISABLED", "ENABLED", "ERROR", "EXPIRED", "INVALID", "VALIDATING"]
        ]
    ] = Field(default=None, alias="statusList")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroundStationsRequestListGroundStationsPaginateModel(BaseModel):
    satellite_id: Optional[str] = Field(default=None, alias="satelliteId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMissionProfilesRequestListMissionProfilesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSatellitesRequestListSatellitesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMissionProfilesResponseModel(BaseModel):
    mission_profile_list: List[MissionProfileListItemModel] = Field(
        alias="missionProfileList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TLEDataModel(BaseModel):
    tle_line1: str = Field(alias="tleLine1")
    tle_line2: str = Field(alias="tleLine2")
    valid_time_range: TimeRangeModel = Field(alias="validTimeRange")


class RegisterAgentRequestModel(BaseModel):
    agent_details: AgentDetailsModel = Field(alias="agentDetails")
    discovery_data: DiscoveryDataModel = Field(alias="discoveryData")


class ListContactsResponseModel(BaseModel):
    contact_list: List[ContactDataModel] = Field(alias="contactList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EphemerisTypeDescriptionModel(BaseModel):
    oem: Optional[EphemerisDescriptionModel] = Field(default=None, alias="oem")
    tle: Optional[EphemerisDescriptionModel] = Field(default=None, alias="tle")


class ListEphemeridesResponseModel(BaseModel):
    ephemerides: List[EphemerisItemModel] = Field(alias="ephemerides")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSatellitesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    satellites: List[SatelliteListItemModel] = Field(alias="satellites")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AntennaDownlinkConfigModel(BaseModel):
    spectrum_config: SpectrumConfigModel = Field(alias="spectrumConfig")


class AntennaDownlinkDemodDecodeConfigModel(BaseModel):
    decode_config: DecodeConfigModel = Field(alias="decodeConfig")
    demodulation_config: DemodulationConfigModel = Field(alias="demodulationConfig")
    spectrum_config: SpectrumConfigModel = Field(alias="spectrumConfig")


class AntennaUplinkConfigModel(BaseModel):
    spectrum_config: UplinkSpectrumConfigModel = Field(alias="spectrumConfig")
    target_eirp: EirpModel = Field(alias="targetEirp")
    transmit_disabled: Optional[bool] = Field(default=None, alias="transmitDisabled")


class RangedConnectionDetailsModel(BaseModel):
    socket_address: RangedSocketAddressModel = Field(alias="socketAddress")
    mtu: Optional[int] = Field(default=None, alias="mtu")


class TLEEphemerisModel(BaseModel):
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="s3Object")
    tle_data: Optional[Sequence[TLEDataModel]] = Field(default=None, alias="tleData")


class DescribeEphemerisResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    enabled: bool = Field(alias="enabled")
    ephemeris_id: str = Field(alias="ephemerisId")
    invalid_reason: Literal[
        "KMS_KEY_INVALID",
        "METADATA_INVALID",
        "TIME_RANGE_INVALID",
        "TRAJECTORY_INVALID",
        "VALIDATION_ERROR",
    ] = Field(alias="invalidReason")
    name: str = Field(alias="name")
    priority: int = Field(alias="priority")
    satellite_id: str = Field(alias="satelliteId")
    status: Literal[
        "DISABLED", "ENABLED", "ERROR", "EXPIRED", "INVALID", "VALIDATING"
    ] = Field(alias="status")
    supplied_data: EphemerisTypeDescriptionModel = Field(alias="suppliedData")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigTypeDataModel(BaseModel):
    antenna_downlink_config: Optional[AntennaDownlinkConfigModel] = Field(
        default=None, alias="antennaDownlinkConfig"
    )
    antenna_downlink_demod_decode_config: Optional[
        AntennaDownlinkDemodDecodeConfigModel
    ] = Field(default=None, alias="antennaDownlinkDemodDecodeConfig")
    antenna_uplink_config: Optional[AntennaUplinkConfigModel] = Field(
        default=None, alias="antennaUplinkConfig"
    )
    dataflow_endpoint_config: Optional[DataflowEndpointConfigModel] = Field(
        default=None, alias="dataflowEndpointConfig"
    )
    s3_recording_config: Optional[S3RecordingConfigModel] = Field(
        default=None, alias="s3RecordingConfig"
    )
    tracking_config: Optional[TrackingConfigModel] = Field(
        default=None, alias="trackingConfig"
    )
    uplink_echo_config: Optional[UplinkEchoConfigModel] = Field(
        default=None, alias="uplinkEchoConfig"
    )


class AwsGroundStationAgentEndpointModel(BaseModel):
    egress_address: ConnectionDetailsModel = Field(alias="egressAddress")
    ingress_address: RangedConnectionDetailsModel = Field(alias="ingressAddress")
    name: str = Field(alias="name")
    agent_status: Optional[Literal["ACTIVE", "FAILED", "INACTIVE", "SUCCESS"]] = Field(
        default=None, alias="agentStatus"
    )
    audit_results: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="auditResults"
    )


class EphemerisDataModel(BaseModel):
    oem: Optional[OEMEphemerisModel] = Field(default=None, alias="oem")
    tle: Optional[TLEEphemerisModel] = Field(default=None, alias="tle")


class CreateConfigRequestModel(BaseModel):
    config_data: ConfigTypeDataModel = Field(alias="configData")
    name: str = Field(alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetConfigResponseModel(BaseModel):
    config_arn: str = Field(alias="configArn")
    config_data: ConfigTypeDataModel = Field(alias="configData")
    config_id: str = Field(alias="configId")
    config_type: Literal[
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "antenna-uplink",
        "dataflow-endpoint",
        "s3-recording",
        "tracking",
        "uplink-echo",
    ] = Field(alias="configType")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfigRequestModel(BaseModel):
    config_data: ConfigTypeDataModel = Field(alias="configData")
    config_id: str = Field(alias="configId")
    config_type: Literal[
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "antenna-uplink",
        "dataflow-endpoint",
        "s3-recording",
        "tracking",
        "uplink-echo",
    ] = Field(alias="configType")
    name: str = Field(alias="name")


class EndpointDetailsModel(BaseModel):
    aws_ground_station_agent_endpoint: Optional[
        AwsGroundStationAgentEndpointModel
    ] = Field(default=None, alias="awsGroundStationAgentEndpoint")
    endpoint: Optional[DataflowEndpointModel] = Field(default=None, alias="endpoint")
    security_details: Optional[SecurityDetailsModel] = Field(
        default=None, alias="securityDetails"
    )


class CreateEphemerisRequestModel(BaseModel):
    name: str = Field(alias="name")
    satellite_id: str = Field(alias="satelliteId")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    ephemeris: Optional[EphemerisDataModel] = Field(default=None, alias="ephemeris")
    expiration_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="expirationTime"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    priority: Optional[int] = Field(default=None, alias="priority")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ConfigDetailsModel(BaseModel):
    antenna_demod_decode_details: Optional[AntennaDemodDecodeDetailsModel] = Field(
        default=None, alias="antennaDemodDecodeDetails"
    )
    endpoint_details: Optional[EndpointDetailsModel] = Field(
        default=None, alias="endpointDetails"
    )
    s3_recording_details: Optional[S3RecordingDetailsModel] = Field(
        default=None, alias="s3RecordingDetails"
    )


class CreateDataflowEndpointGroupRequestModel(BaseModel):
    endpoint_details: Sequence[EndpointDetailsModel] = Field(alias="endpointDetails")
    contact_post_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPostPassDurationSeconds"
    )
    contact_pre_pass_duration_seconds: Optional[int] = Field(
        default=None, alias="contactPrePassDurationSeconds"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetDataflowEndpointGroupResponseModel(BaseModel):
    contact_post_pass_duration_seconds: int = Field(
        alias="contactPostPassDurationSeconds"
    )
    contact_pre_pass_duration_seconds: int = Field(
        alias="contactPrePassDurationSeconds"
    )
    dataflow_endpoint_group_arn: str = Field(alias="dataflowEndpointGroupArn")
    dataflow_endpoint_group_id: str = Field(alias="dataflowEndpointGroupId")
    endpoints_details: List[EndpointDetailsModel] = Field(alias="endpointsDetails")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationModel(BaseModel):
    config_details: Optional[ConfigDetailsModel] = Field(
        default=None, alias="configDetails"
    )
    config_id: Optional[str] = Field(default=None, alias="configId")
    config_type: Optional[
        Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "s3-recording",
            "tracking",
            "uplink-echo",
        ]
    ] = Field(default=None, alias="configType")
    dataflow_destination_region: Optional[str] = Field(
        default=None, alias="dataflowDestinationRegion"
    )


class SourceModel(BaseModel):
    config_details: Optional[ConfigDetailsModel] = Field(
        default=None, alias="configDetails"
    )
    config_id: Optional[str] = Field(default=None, alias="configId")
    config_type: Optional[
        Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "s3-recording",
            "tracking",
            "uplink-echo",
        ]
    ] = Field(default=None, alias="configType")
    dataflow_source_region: Optional[str] = Field(
        default=None, alias="dataflowSourceRegion"
    )


class DataflowDetailModel(BaseModel):
    destination: Optional[DestinationModel] = Field(default=None, alias="destination")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    source: Optional[SourceModel] = Field(default=None, alias="source")


class DescribeContactResponseModel(BaseModel):
    contact_id: str = Field(alias="contactId")
    contact_status: Literal[
        "AVAILABLE",
        "AWS_CANCELLED",
        "AWS_FAILED",
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "FAILED",
        "FAILED_TO_SCHEDULE",
        "PASS",
        "POSTPASS",
        "PREPASS",
        "SCHEDULED",
        "SCHEDULING",
    ] = Field(alias="contactStatus")
    dataflow_list: List[DataflowDetailModel] = Field(alias="dataflowList")
    end_time: datetime = Field(alias="endTime")
    error_message: str = Field(alias="errorMessage")
    ground_station: str = Field(alias="groundStation")
    maximum_elevation: ElevationModel = Field(alias="maximumElevation")
    mission_profile_arn: str = Field(alias="missionProfileArn")
    post_pass_end_time: datetime = Field(alias="postPassEndTime")
    pre_pass_start_time: datetime = Field(alias="prePassStartTime")
    region: str = Field(alias="region")
    satellite_arn: str = Field(alias="satelliteArn")
    start_time: datetime = Field(alias="startTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
