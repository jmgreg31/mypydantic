# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class SessionKeysAbpV1_0_xModel(BaseModel):
    nwk_s_key: Optional[str] = Field(default=None, alias="NwkSKey")
    app_s_key: Optional[str] = Field(default=None, alias="AppSKey")


class SessionKeysAbpV1_1Model(BaseModel):
    fnwk_s_int_key: Optional[str] = Field(default=None, alias="FNwkSIntKey")
    s_nwk_s_int_key: Optional[str] = Field(default=None, alias="SNwkSIntKey")
    nwk_s_enc_key: Optional[str] = Field(default=None, alias="NwkSEncKey")
    app_s_key: Optional[str] = Field(default=None, alias="AppSKey")


class AccuracyModel(BaseModel):
    horizontal_accuracy: Optional[float] = Field(
        default=None, alias="HorizontalAccuracy"
    )
    vertical_accuracy: Optional[float] = Field(default=None, alias="VerticalAccuracy")


class ApplicationConfigModel(BaseModel):
    fport: Optional[int] = Field(default=None, alias="FPort")
    type: Optional[Literal["SemtechGeolocation"]] = Field(default=None, alias="Type")
    destination_name: Optional[str] = Field(default=None, alias="DestinationName")


class SidewalkAccountInfoModel(BaseModel):
    amazon_id: Optional[str] = Field(default=None, alias="AmazonId")
    app_server_private_key: Optional[str] = Field(
        default=None, alias="AppServerPrivateKey"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateMulticastGroupWithFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    multicast_group_id: str = Field(alias="MulticastGroupId")


class AssociateWirelessDeviceWithFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    wireless_device_id: str = Field(alias="WirelessDeviceId")


class AssociateWirelessDeviceWithMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    wireless_device_id: str = Field(alias="WirelessDeviceId")


class AssociateWirelessDeviceWithThingRequestModel(BaseModel):
    id: str = Field(alias="Id")
    thing_arn: str = Field(alias="ThingArn")


class AssociateWirelessGatewayWithCertificateRequestModel(BaseModel):
    id: str = Field(alias="Id")
    iot_certificate_id: str = Field(alias="IotCertificateId")


class AssociateWirelessGatewayWithThingRequestModel(BaseModel):
    id: str = Field(alias="Id")
    thing_arn: str = Field(alias="ThingArn")


class BeaconingModel(BaseModel):
    data_rate: Optional[int] = Field(default=None, alias="DataRate")
    frequencies: Optional[Sequence[int]] = Field(default=None, alias="Frequencies")


class CancelMulticastGroupSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class CdmaLocalIdModel(BaseModel):
    pn_offset: int = Field(alias="PnOffset")
    cdma_channel: int = Field(alias="CdmaChannel")


class CdmaNmrObjModel(BaseModel):
    pn_offset: int = Field(alias="PnOffset")
    cdma_channel: int = Field(alias="CdmaChannel")
    pilot_power: Optional[int] = Field(default=None, alias="PilotPower")
    base_station_id: Optional[int] = Field(default=None, alias="BaseStationId")


class CertificateListModel(BaseModel):
    signing_alg: Literal["Ed25519", "P256r1"] = Field(alias="SigningAlg")
    value: str = Field(alias="Value")


class LoRaWANConnectionStatusEventNotificationConfigurationsModel(BaseModel):
    gateway_eui_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="GatewayEuiEventTopic"
    )


class LoRaWANConnectionStatusResourceTypeEventConfigurationModel(BaseModel):
    wireless_gateway_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessGatewayEventTopic"
    )


class LoRaWANDeviceProfileModel(BaseModel):
    supports_class_b: Optional[bool] = Field(default=None, alias="SupportsClassB")
    class_btimeout: Optional[int] = Field(default=None, alias="ClassBTimeout")
    ping_slot_period: Optional[int] = Field(default=None, alias="PingSlotPeriod")
    ping_slot_dr: Optional[int] = Field(default=None, alias="PingSlotDr")
    ping_slot_freq: Optional[int] = Field(default=None, alias="PingSlotFreq")
    supports_class_c: Optional[bool] = Field(default=None, alias="SupportsClassC")
    class_ctimeout: Optional[int] = Field(default=None, alias="ClassCTimeout")
    mac_version: Optional[str] = Field(default=None, alias="MacVersion")
    reg_params_revision: Optional[str] = Field(default=None, alias="RegParamsRevision")
    rx_delay1: Optional[int] = Field(default=None, alias="RxDelay1")
    rx_dr_offset1: Optional[int] = Field(default=None, alias="RxDrOffset1")
    rx_data_rate2: Optional[int] = Field(default=None, alias="RxDataRate2")
    rx_freq2: Optional[int] = Field(default=None, alias="RxFreq2")
    factory_preset_freqs_list: Optional[Sequence[int]] = Field(
        default=None, alias="FactoryPresetFreqsList"
    )
    max_eirp: Optional[int] = Field(default=None, alias="MaxEirp")
    max_duty_cycle: Optional[int] = Field(default=None, alias="MaxDutyCycle")
    rf_region: Optional[str] = Field(default=None, alias="RfRegion")
    supports_join: Optional[bool] = Field(default=None, alias="SupportsJoin")
    supports32_bit_fcnt: Optional[bool] = Field(default=None, alias="Supports32BitFCnt")


class LoRaWANFuotaTaskModel(BaseModel):
    rf_region: Optional[Literal["AS923-1", "AU915", "EU868", "US915"]] = Field(
        default=None, alias="RfRegion"
    )


class LoRaWANMulticastModel(BaseModel):
    rf_region: Optional[Literal["AS923-1", "AU915", "EU868", "US915"]] = Field(
        default=None, alias="RfRegion"
    )
    dl_class: Optional[Literal["ClassB", "ClassC"]] = Field(
        default=None, alias="DlClass"
    )


class TraceContentModel(BaseModel):
    wireless_device_frame_info: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="WirelessDeviceFrameInfo"
    )
    log_level: Optional[Literal["DISABLED", "ERROR", "INFO"]] = Field(
        default=None, alias="LogLevel"
    )


class LoRaWANServiceProfileModel(BaseModel):
    add_gw_metadata: Optional[bool] = Field(default=None, alias="AddGwMetadata")
    dr_min: Optional[int] = Field(default=None, alias="DrMin")
    dr_max: Optional[int] = Field(default=None, alias="DrMax")


class CreateWirelessGatewayTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    wireless_gateway_task_definition_id: str = Field(
        alias="WirelessGatewayTaskDefinitionId"
    )


class DeleteDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteDeviceProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteNetworkAnalyzerConfigurationRequestModel(BaseModel):
    configuration_name: str = Field(alias="ConfigurationName")


class DeleteQueuedMessagesRequestModel(BaseModel):
    id: str = Field(alias="Id")
    message_id: str = Field(alias="MessageId")
    wireless_device_type: Optional[Literal["LoRaWAN", "Sidewalk"]] = Field(
        default=None, alias="WirelessDeviceType"
    )


class DeleteServiceProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteWirelessDeviceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteWirelessGatewayRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteWirelessGatewayTaskDefinitionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteWirelessGatewayTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DestinationsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    expression_type: Optional[Literal["MqttTopic", "RuleName"]] = Field(
        default=None, alias="ExpressionType"
    )
    expression: Optional[str] = Field(default=None, alias="Expression")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class DeviceProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")


class SidewalkEventNotificationConfigurationsModel(BaseModel):
    amazon_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="AmazonIdEventTopic"
    )


class SidewalkResourceTypeEventConfigurationModel(BaseModel):
    wireless_device_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceEventTopic"
    )


class DisassociateAwsAccountFromPartnerAccountRequestModel(BaseModel):
    partner_account_id: str = Field(alias="PartnerAccountId")
    partner_type: Literal["Sidewalk"] = Field(alias="PartnerType")


class DisassociateMulticastGroupFromFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    multicast_group_id: str = Field(alias="MulticastGroupId")


class DisassociateWirelessDeviceFromFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    wireless_device_id: str = Field(alias="WirelessDeviceId")


class DisassociateWirelessDeviceFromMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    wireless_device_id: str = Field(alias="WirelessDeviceId")


class DisassociateWirelessDeviceFromThingRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DisassociateWirelessGatewayFromCertificateRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DisassociateWirelessGatewayFromThingRequestModel(BaseModel):
    id: str = Field(alias="Id")


class PositioningModel(BaseModel):
    clock_sync: Optional[int] = Field(default=None, alias="ClockSync")
    stream: Optional[int] = Field(default=None, alias="Stream")
    gnss: Optional[int] = Field(default=None, alias="Gnss")


class FuotaTaskModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class GatewayListItemModel(BaseModel):
    gateway_id: str = Field(alias="GatewayId")
    downlink_frequency: int = Field(alias="DownlinkFrequency")


class GetDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetDeviceProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")


class LoRaWANFuotaTaskGetInfoModel(BaseModel):
    rf_region: Optional[str] = Field(default=None, alias="RfRegion")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")


class GetMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")


class LoRaWANMulticastGetModel(BaseModel):
    rf_region: Optional[Literal["AS923-1", "AU915", "EU868", "US915"]] = Field(
        default=None, alias="RfRegion"
    )
    dl_class: Optional[Literal["ClassB", "ClassC"]] = Field(
        default=None, alias="DlClass"
    )
    number_of_devices_requested: Optional[int] = Field(
        default=None, alias="NumberOfDevicesRequested"
    )
    number_of_devices_in_group: Optional[int] = Field(
        default=None, alias="NumberOfDevicesInGroup"
    )


class GetMulticastGroupSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class LoRaWANMulticastSessionModel(BaseModel):
    dl_dr: Optional[int] = Field(default=None, alias="DlDr")
    dl_freq: Optional[int] = Field(default=None, alias="DlFreq")
    session_start_time: Optional[datetime] = Field(
        default=None, alias="SessionStartTime"
    )
    session_timeout: Optional[int] = Field(default=None, alias="SessionTimeout")


class GetNetworkAnalyzerConfigurationRequestModel(BaseModel):
    configuration_name: str = Field(alias="ConfigurationName")


class GetPartnerAccountRequestModel(BaseModel):
    partner_account_id: str = Field(alias="PartnerAccountId")
    partner_type: Literal["Sidewalk"] = Field(alias="PartnerType")


class SidewalkAccountInfoWithFingerprintModel(BaseModel):
    amazon_id: Optional[str] = Field(default=None, alias="AmazonId")
    fingerprint: Optional[str] = Field(default=None, alias="Fingerprint")
    arn: Optional[str] = Field(default=None, alias="Arn")


class GetPositionConfigurationRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )


class GnssModel(BaseModel):
    payload: str = Field(alias="Payload")
    capture_time: Optional[float] = Field(default=None, alias="CaptureTime")
    capture_time_accuracy: Optional[float] = Field(
        default=None, alias="CaptureTimeAccuracy"
    )
    assist_position: Optional[Sequence[float]] = Field(
        default=None, alias="AssistPosition"
    )
    assist_altitude: Optional[float] = Field(default=None, alias="AssistAltitude")
    use2_dsolver: Optional[bool] = Field(default=None, alias="Use2DSolver")


class IpModel(BaseModel):
    ip_address: str = Field(alias="IpAddress")


class WiFiAccessPointModel(BaseModel):
    mac_address: str = Field(alias="MacAddress")
    rss: int = Field(alias="Rss")


class GetPositionRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )


class GetResourceEventConfigurationRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    identifier_type: Literal[
        "DevEui",
        "GatewayEui",
        "PartnerAccountId",
        "WirelessDeviceId",
        "WirelessGatewayId",
    ] = Field(alias="IdentifierType")
    partner_type: Optional[Literal["Sidewalk"]] = Field(
        default=None, alias="PartnerType"
    )


class GetResourceLogLevelRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: str = Field(alias="ResourceType")


class GetResourcePositionRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )


class GetServiceEndpointRequestModel(BaseModel):
    service_type: Optional[Literal["CUPS", "LNS"]] = Field(
        default=None, alias="ServiceType"
    )


class GetServiceProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")


class LoRaWANGetServiceProfileInfoModel(BaseModel):
    ul_rate: Optional[int] = Field(default=None, alias="UlRate")
    ul_bucket_size: Optional[int] = Field(default=None, alias="UlBucketSize")
    ul_rate_policy: Optional[str] = Field(default=None, alias="UlRatePolicy")
    dl_rate: Optional[int] = Field(default=None, alias="DlRate")
    dl_bucket_size: Optional[int] = Field(default=None, alias="DlBucketSize")
    dl_rate_policy: Optional[str] = Field(default=None, alias="DlRatePolicy")
    add_gw_metadata: Optional[bool] = Field(default=None, alias="AddGwMetadata")
    dev_status_req_freq: Optional[int] = Field(default=None, alias="DevStatusReqFreq")
    report_dev_status_battery: Optional[bool] = Field(
        default=None, alias="ReportDevStatusBattery"
    )
    report_dev_status_margin: Optional[bool] = Field(
        default=None, alias="ReportDevStatusMargin"
    )
    dr_min: Optional[int] = Field(default=None, alias="DrMin")
    dr_max: Optional[int] = Field(default=None, alias="DrMax")
    channel_mask: Optional[str] = Field(default=None, alias="ChannelMask")
    pr_allowed: Optional[bool] = Field(default=None, alias="PrAllowed")
    hr_allowed: Optional[bool] = Field(default=None, alias="HrAllowed")
    ra_allowed: Optional[bool] = Field(default=None, alias="RaAllowed")
    nwk_geo_loc: Optional[bool] = Field(default=None, alias="NwkGeoLoc")
    target_per: Optional[int] = Field(default=None, alias="TargetPer")
    min_gw_diversity: Optional[int] = Field(default=None, alias="MinGwDiversity")


class GetWirelessDeviceRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    identifier_type: Literal[
        "DevEui", "SidewalkManufacturingSn", "ThingName", "WirelessDeviceId"
    ] = Field(alias="IdentifierType")


class GetWirelessDeviceStatisticsRequestModel(BaseModel):
    wireless_device_id: str = Field(alias="WirelessDeviceId")


class SidewalkDeviceMetadataModel(BaseModel):
    rssi: Optional[int] = Field(default=None, alias="Rssi")
    battery_level: Optional[Literal["critical", "low", "normal"]] = Field(
        default=None, alias="BatteryLevel"
    )
    event: Optional[
        Literal["ack", "discovered", "lost", "nack", "passthrough"]
    ] = Field(default=None, alias="Event")
    device_state: Optional[
        Literal[
            "Provisioned",
            "RegisteredNotSeen",
            "RegisteredReachable",
            "RegisteredUnreachable",
        ]
    ] = Field(default=None, alias="DeviceState")


class GetWirelessGatewayCertificateRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetWirelessGatewayFirmwareInformationRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetWirelessGatewayRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    identifier_type: Literal["GatewayEui", "ThingName", "WirelessGatewayId"] = Field(
        alias="IdentifierType"
    )


class GetWirelessGatewayStatisticsRequestModel(BaseModel):
    wireless_gateway_id: str = Field(alias="WirelessGatewayId")


class GetWirelessGatewayTaskDefinitionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetWirelessGatewayTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GlobalIdentityModel(BaseModel):
    lac: int = Field(alias="Lac")
    geran_cid: int = Field(alias="GeranCid")


class GsmLocalIdModel(BaseModel):
    bsic: int = Field(alias="Bsic")
    bcch: int = Field(alias="Bcch")


class LoRaWANJoinEventNotificationConfigurationsModel(BaseModel):
    dev_eui_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="DevEuiEventTopic"
    )


class LoRaWANJoinResourceTypeEventConfigurationModel(BaseModel):
    wireless_device_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceEventTopic"
    )


class ListDestinationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDeviceProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEventConfigurationsRequestModel(BaseModel):
    resource_type: Literal[
        "SidewalkAccount", "WirelessDevice", "WirelessGateway"
    ] = Field(alias="ResourceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFuotaTasksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMulticastGroupsByFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MulticastGroupByFuotaTaskModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class ListMulticastGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MulticastGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListNetworkAnalyzerConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NetworkAnalyzerConfigurationsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListPartnerAccountsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPositionConfigurationsRequestModel(BaseModel):
    resource_type: Optional[Literal["WirelessDevice", "WirelessGateway"]] = Field(
        default=None, alias="ResourceType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListQueuedMessagesRequestModel(BaseModel):
    id: str = Field(alias="Id")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    wireless_device_type: Optional[Literal["LoRaWAN", "Sidewalk"]] = Field(
        default=None, alias="WirelessDeviceType"
    )


class ListServiceProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ServiceProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListWirelessDevicesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    destination_name: Optional[str] = Field(default=None, alias="DestinationName")
    device_profile_id: Optional[str] = Field(default=None, alias="DeviceProfileId")
    service_profile_id: Optional[str] = Field(default=None, alias="ServiceProfileId")
    wireless_device_type: Optional[Literal["LoRaWAN", "Sidewalk"]] = Field(
        default=None, alias="WirelessDeviceType"
    )
    fuota_task_id: Optional[str] = Field(default=None, alias="FuotaTaskId")
    multicast_group_id: Optional[str] = Field(default=None, alias="MulticastGroupId")


class ListWirelessGatewayTaskDefinitionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    task_definition_type: Optional[Literal["UPDATE"]] = Field(
        default=None, alias="TaskDefinitionType"
    )


class ListWirelessGatewaysRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class LoRaWANGatewayMetadataModel(BaseModel):
    gateway_eui: Optional[str] = Field(default=None, alias="GatewayEui")
    snr: Optional[float] = Field(default=None, alias="Snr")
    rssi: Optional[float] = Field(default=None, alias="Rssi")


class OtaaV1_0_xModel(BaseModel):
    app_key: Optional[str] = Field(default=None, alias="AppKey")
    app_eui: Optional[str] = Field(default=None, alias="AppEui")
    gen_app_key: Optional[str] = Field(default=None, alias="GenAppKey")


class OtaaV1_1Model(BaseModel):
    app_key: Optional[str] = Field(default=None, alias="AppKey")
    nwk_key: Optional[str] = Field(default=None, alias="NwkKey")
    join_eui: Optional[str] = Field(default=None, alias="JoinEui")


class LoRaWANGatewayVersionModel(BaseModel):
    package_version: Optional[str] = Field(default=None, alias="PackageVersion")
    model: Optional[str] = Field(default=None, alias="Model")
    station: Optional[str] = Field(default=None, alias="Station")


class LoRaWANListDeviceModel(BaseModel):
    dev_eui: Optional[str] = Field(default=None, alias="DevEui")


class LoRaWANMulticastMetadataModel(BaseModel):
    fport: Optional[int] = Field(default=None, alias="FPort")


class LoRaWANStartFuotaTaskModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class UpdateAbpV1_0_xModel(BaseModel):
    fcnt_start: Optional[int] = Field(default=None, alias="FCntStart")


class UpdateAbpV1_1Model(BaseModel):
    fcnt_start: Optional[int] = Field(default=None, alias="FCntStart")


class LteLocalIdModel(BaseModel):
    pci: int = Field(alias="Pci")
    earfcn: int = Field(alias="Earfcn")


class LteNmrObjModel(BaseModel):
    pci: int = Field(alias="Pci")
    earfcn: int = Field(alias="Earfcn")
    eutran_cid: int = Field(alias="EutranCid")
    rsrp: Optional[int] = Field(default=None, alias="Rsrp")
    rsrq: Optional[float] = Field(default=None, alias="Rsrq")


class SemtechGnssConfigurationModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    fec: Literal["NONE", "ROSE"] = Field(alias="Fec")


class SemtechGnssDetailModel(BaseModel):
    provider: Optional[Literal["Semtech"]] = Field(default=None, alias="Provider")
    type: Optional[Literal["GNSS"]] = Field(default=None, alias="Type")
    status: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Status"
    )
    fec: Optional[Literal["NONE", "ROSE"]] = Field(default=None, alias="Fec")


class PutResourceLogLevelRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: str = Field(alias="ResourceType")
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")


class ResetResourceLogLevelRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: str = Field(alias="ResourceType")


class SidewalkSendDataToDeviceModel(BaseModel):
    seq: Optional[int] = Field(default=None, alias="Seq")
    message_type: Optional[
        Literal[
            "CUSTOM_COMMAND_ID_GET",
            "CUSTOM_COMMAND_ID_NOTIFY",
            "CUSTOM_COMMAND_ID_RESP",
            "CUSTOM_COMMAND_ID_SET",
        ]
    ] = Field(default=None, alias="MessageType")
    ack_mode_retry_duration_secs: Optional[int] = Field(
        default=None, alias="AckModeRetryDurationSecs"
    )


class SidewalkUpdateAccountModel(BaseModel):
    app_server_private_key: Optional[str] = Field(
        default=None, alias="AppServerPrivateKey"
    )


class TdscdmaLocalIdModel(BaseModel):
    uarfcn: int = Field(alias="Uarfcn")
    cell_params: int = Field(alias="CellParams")


class TdscdmaNmrObjModel(BaseModel):
    uarfcn: int = Field(alias="Uarfcn")
    cell_params: int = Field(alias="CellParams")
    utran_cid: Optional[int] = Field(default=None, alias="UtranCid")
    rscp: Optional[int] = Field(default=None, alias="Rscp")
    path_loss: Optional[int] = Field(default=None, alias="PathLoss")


class TestWirelessDeviceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    expression_type: Optional[Literal["MqttTopic", "RuleName"]] = Field(
        default=None, alias="ExpressionType"
    )
    expression: Optional[str] = Field(default=None, alias="Expression")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class UpdatePositionRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )
    position: Sequence[float] = Field(alias="Position")


class UpdateResourcePositionRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )
    geo_json_payload: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="GeoJsonPayload")


class UpdateWirelessGatewayRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    join_eui_filters: Optional[Sequence[Sequence[str]]] = Field(
        default=None, alias="JoinEuiFilters"
    )
    net_id_filters: Optional[Sequence[str]] = Field(default=None, alias="NetIdFilters")


class WcdmaLocalIdModel(BaseModel):
    uarfcndl: int = Field(alias="Uarfcndl")
    psc: int = Field(alias="Psc")


class WcdmaNmrObjModel(BaseModel):
    uarfcndl: int = Field(alias="Uarfcndl")
    psc: int = Field(alias="Psc")
    utran_cid: int = Field(alias="UtranCid")
    rscp: Optional[int] = Field(default=None, alias="Rscp")
    path_loss: Optional[int] = Field(default=None, alias="PathLoss")


class WirelessDeviceEventLogOptionModel(BaseModel):
    event: Literal[
        "Downlink_Data", "Join", "Registration", "Rejoin", "Uplink_Data"
    ] = Field(alias="Event")
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")


class WirelessGatewayEventLogOptionModel(BaseModel):
    event: Literal["CUPS_Request", "Certificate"] = Field(alias="Event")
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")


class AbpV1_0_xModel(BaseModel):
    dev_addr: Optional[str] = Field(default=None, alias="DevAddr")
    session_keys: Optional[SessionKeysAbpV1_0_xModel] = Field(
        default=None, alias="SessionKeys"
    )
    fcnt_start: Optional[int] = Field(default=None, alias="FCntStart")


class AbpV1_1Model(BaseModel):
    dev_addr: Optional[str] = Field(default=None, alias="DevAddr")
    session_keys: Optional[SessionKeysAbpV1_1Model] = Field(
        default=None, alias="SessionKeys"
    )
    fcnt_start: Optional[int] = Field(default=None, alias="FCntStart")


class AssociateAwsAccountWithPartnerAccountRequestModel(BaseModel):
    sidewalk: SidewalkAccountInfoModel = Field(alias="Sidewalk")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    expression_type: Literal["MqttTopic", "RuleName"] = Field(alias="ExpressionType")
    expression: str = Field(alias="Expression")
    role_arn: str = Field(alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class StartBulkAssociateWirelessDeviceWithMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    query_string: Optional[str] = Field(default=None, alias="QueryString")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    query_string: Optional[str] = Field(default=None, alias="QueryString")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class AssociateAwsAccountWithPartnerAccountResponseModel(BaseModel):
    sidewalk: SidewalkAccountInfoModel = Field(alias="Sidewalk")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateWirelessGatewayWithCertificateResponseModel(BaseModel):
    iot_certificate_id: str = Field(alias="IotCertificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDestinationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeviceProfileResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFuotaTaskResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMulticastGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkAnalyzerConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceProfileResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWirelessDeviceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWirelessGatewayResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWirelessGatewayTaskDefinitionResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWirelessGatewayTaskResponseModel(BaseModel):
    wireless_gateway_task_definition_id: str = Field(
        alias="WirelessGatewayTaskDefinitionId"
    )
    status: Literal[
        "COMPLETED", "FAILED", "FIRST_RETRY", "IN_PROGRESS", "PENDING", "SECOND_RETRY"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDestinationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    expression: str = Field(alias="Expression")
    expression_type: Literal["MqttTopic", "RuleName"] = Field(alias="ExpressionType")
    description: str = Field(alias="Description")
    role_arn: str = Field(alias="RoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPositionEstimateResponseModel(BaseModel):
    geo_json_payload: Type[StreamingBody] = Field(alias="GeoJsonPayload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPositionResponseModel(BaseModel):
    position: List[float] = Field(alias="Position")
    accuracy: AccuracyModel = Field(alias="Accuracy")
    solver_type: Literal["GNSS"] = Field(alias="SolverType")
    solver_provider: Literal["Semtech"] = Field(alias="SolverProvider")
    solver_version: str = Field(alias="SolverVersion")
    timestamp: str = Field(alias="Timestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceLogLevelResponseModel(BaseModel):
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePositionResponseModel(BaseModel):
    geo_json_payload: Type[StreamingBody] = Field(alias="GeoJsonPayload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceEndpointResponseModel(BaseModel):
    service_type: Literal["CUPS", "LNS"] = Field(alias="ServiceType")
    service_endpoint: str = Field(alias="ServiceEndpoint")
    server_trust: str = Field(alias="ServerTrust")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWirelessGatewayCertificateResponseModel(BaseModel):
    iot_certificate_id: str = Field(alias="IotCertificateId")
    lo_ra_wannetwork_server_certificate_id: str = Field(
        alias="LoRaWANNetworkServerCertificateId"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWirelessGatewayStatisticsResponseModel(BaseModel):
    wireless_gateway_id: str = Field(alias="WirelessGatewayId")
    last_uplink_received_at: str = Field(alias="LastUplinkReceivedAt")
    connection_status: Literal["Connected", "Disconnected"] = Field(
        alias="ConnectionStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWirelessGatewayTaskResponseModel(BaseModel):
    wireless_gateway_id: str = Field(alias="WirelessGatewayId")
    wireless_gateway_task_definition_id: str = Field(
        alias="WirelessGatewayTaskDefinitionId"
    )
    last_uplink_received_at: str = Field(alias="LastUplinkReceivedAt")
    task_created_at: str = Field(alias="TaskCreatedAt")
    status: Literal[
        "COMPLETED", "FAILED", "FIRST_RETRY", "IN_PROGRESS", "PENDING", "SECOND_RETRY"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendDataToMulticastGroupResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendDataToWirelessDeviceResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestWirelessDeviceResponseModel(BaseModel):
    result: str = Field(alias="Result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoRaWANGatewayModel(BaseModel):
    gateway_eui: Optional[str] = Field(default=None, alias="GatewayEui")
    rf_region: Optional[str] = Field(default=None, alias="RfRegion")
    join_eui_filters: Optional[Sequence[Sequence[str]]] = Field(
        default=None, alias="JoinEuiFilters"
    )
    net_id_filters: Optional[Sequence[str]] = Field(default=None, alias="NetIdFilters")
    sub_bands: Optional[Sequence[int]] = Field(default=None, alias="SubBands")
    beaconing: Optional[BeaconingModel] = Field(default=None, alias="Beaconing")


class CdmaObjModel(BaseModel):
    system_id: int = Field(alias="SystemId")
    network_id: int = Field(alias="NetworkId")
    base_station_id: int = Field(alias="BaseStationId")
    registration_zone: Optional[int] = Field(default=None, alias="RegistrationZone")
    cdma_local_id: Optional[CdmaLocalIdModel] = Field(default=None, alias="CdmaLocalId")
    pilot_power: Optional[int] = Field(default=None, alias="PilotPower")
    base_lat: Optional[float] = Field(default=None, alias="BaseLat")
    base_lng: Optional[float] = Field(default=None, alias="BaseLng")
    cdma_nmr: Optional[Sequence[CdmaNmrObjModel]] = Field(default=None, alias="CdmaNmr")


class SidewalkDeviceModel(BaseModel):
    amazon_id: Optional[str] = Field(default=None, alias="AmazonId")
    sidewalk_id: Optional[str] = Field(default=None, alias="SidewalkId")
    sidewalk_manufacturing_sn: Optional[str] = Field(
        default=None, alias="SidewalkManufacturingSn"
    )
    device_certificates: Optional[List[CertificateListModel]] = Field(
        default=None, alias="DeviceCertificates"
    )


class SidewalkListDeviceModel(BaseModel):
    amazon_id: Optional[str] = Field(default=None, alias="AmazonId")
    sidewalk_id: Optional[str] = Field(default=None, alias="SidewalkId")
    sidewalk_manufacturing_sn: Optional[str] = Field(
        default=None, alias="SidewalkManufacturingSn"
    )
    device_certificates: Optional[List[CertificateListModel]] = Field(
        default=None, alias="DeviceCertificates"
    )


class ConnectionStatusEventConfigurationModel(BaseModel):
    lo_ra_wan: Optional[
        LoRaWANConnectionStatusEventNotificationConfigurationsModel
    ] = Field(default=None, alias="LoRaWAN")
    wireless_gateway_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessGatewayIdEventTopic"
    )


class ConnectionStatusResourceTypeEventConfigurationModel(BaseModel):
    lo_ra_wan: Optional[
        LoRaWANConnectionStatusResourceTypeEventConfigurationModel
    ] = Field(default=None, alias="LoRaWAN")


class CreateDeviceProfileRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    lo_ra_wan: Optional[LoRaWANDeviceProfileModel] = Field(
        default=None, alias="LoRaWAN"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class GetDeviceProfileResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    lo_ra_wan: LoRaWANDeviceProfileModel = Field(alias="LoRaWAN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFuotaTaskRequestModel(BaseModel):
    firmware_update_image: str = Field(alias="FirmwareUpdateImage")
    firmware_update_role: str = Field(alias="FirmwareUpdateRole")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    lo_ra_wan: Optional[LoRaWANFuotaTaskModel] = Field(default=None, alias="LoRaWAN")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    redundancy_percent: Optional[int] = Field(default=None, alias="RedundancyPercent")
    fragment_size_bytes: Optional[int] = Field(default=None, alias="FragmentSizeBytes")
    fragment_interval_ms: Optional[int] = Field(
        default=None, alias="FragmentIntervalMS"
    )


class UpdateFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    lo_ra_wan: Optional[LoRaWANFuotaTaskModel] = Field(default=None, alias="LoRaWAN")
    firmware_update_image: Optional[str] = Field(
        default=None, alias="FirmwareUpdateImage"
    )
    firmware_update_role: Optional[str] = Field(
        default=None, alias="FirmwareUpdateRole"
    )
    redundancy_percent: Optional[int] = Field(default=None, alias="RedundancyPercent")
    fragment_size_bytes: Optional[int] = Field(default=None, alias="FragmentSizeBytes")
    fragment_interval_ms: Optional[int] = Field(
        default=None, alias="FragmentIntervalMS"
    )


class CreateMulticastGroupRequestModel(BaseModel):
    lo_ra_wan: LoRaWANMulticastModel = Field(alias="LoRaWAN")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    lo_ra_wan: Optional[LoRaWANMulticastModel] = Field(default=None, alias="LoRaWAN")


class CreateNetworkAnalyzerConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    trace_content: Optional[TraceContentModel] = Field(
        default=None, alias="TraceContent"
    )
    wireless_devices: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessDevices"
    )
    wireless_gateways: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessGateways"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class GetNetworkAnalyzerConfigurationResponseModel(BaseModel):
    trace_content: TraceContentModel = Field(alias="TraceContent")
    wireless_devices: List[str] = Field(alias="WirelessDevices")
    wireless_gateways: List[str] = Field(alias="WirelessGateways")
    description: str = Field(alias="Description")
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNetworkAnalyzerConfigurationRequestModel(BaseModel):
    configuration_name: str = Field(alias="ConfigurationName")
    trace_content: Optional[TraceContentModel] = Field(
        default=None, alias="TraceContent"
    )
    wireless_devices_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessDevicesToAdd"
    )
    wireless_devices_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessDevicesToRemove"
    )
    wireless_gateways_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessGatewaysToAdd"
    )
    wireless_gateways_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="WirelessGatewaysToRemove"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateServiceProfileRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    lo_ra_wan: Optional[LoRaWANServiceProfileModel] = Field(
        default=None, alias="LoRaWAN"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ListDestinationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    destination_list: List[DestinationsModel] = Field(alias="DestinationList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceProfilesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    device_profile_list: List[DeviceProfileModel] = Field(alias="DeviceProfileList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceRegistrationStateEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkEventNotificationConfigurationsModel] = Field(
        default=None, alias="Sidewalk"
    )
    wireless_device_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceIdEventTopic"
    )


class MessageDeliveryStatusEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkEventNotificationConfigurationsModel] = Field(
        default=None, alias="Sidewalk"
    )
    wireless_device_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceIdEventTopic"
    )


class ProximityEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkEventNotificationConfigurationsModel] = Field(
        default=None, alias="Sidewalk"
    )
    wireless_device_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceIdEventTopic"
    )


class DeviceRegistrationStateResourceTypeEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkResourceTypeEventConfigurationModel] = Field(
        default=None, alias="Sidewalk"
    )


class MessageDeliveryStatusResourceTypeEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkResourceTypeEventConfigurationModel] = Field(
        default=None, alias="Sidewalk"
    )


class ProximityResourceTypeEventConfigurationModel(BaseModel):
    sidewalk: Optional[SidewalkResourceTypeEventConfigurationModel] = Field(
        default=None, alias="Sidewalk"
    )


class FPortsModel(BaseModel):
    fuota: Optional[int] = Field(default=None, alias="Fuota")
    multicast: Optional[int] = Field(default=None, alias="Multicast")
    clock_sync: Optional[int] = Field(default=None, alias="ClockSync")
    positioning: Optional[PositioningModel] = Field(default=None, alias="Positioning")
    applications: Optional[Sequence[ApplicationConfigModel]] = Field(
        default=None, alias="Applications"
    )


class UpdateFPortsModel(BaseModel):
    positioning: Optional[PositioningModel] = Field(default=None, alias="Positioning")
    applications: Optional[Sequence[ApplicationConfigModel]] = Field(
        default=None, alias="Applications"
    )


class ListFuotaTasksResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    fuota_task_list: List[FuotaTaskModel] = Field(alias="FuotaTaskList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParticipatingGatewaysModel(BaseModel):
    downlink_mode: Literal["CONCURRENT", "SEQUENTIAL", "USING_UPLINK_GATEWAY"] = Field(
        alias="DownlinkMode"
    )
    gateway_list: List[GatewayListItemModel] = Field(alias="GatewayList")
    transmission_interval: int = Field(alias="TransmissionInterval")


class GetFuotaTaskResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    status: Literal[
        "Delete_Waiting",
        "FuotaDone",
        "FuotaSession_Waiting",
        "In_FuotaSession",
        "Pending",
    ] = Field(alias="Status")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    lo_ra_wan: LoRaWANFuotaTaskGetInfoModel = Field(alias="LoRaWAN")
    firmware_update_image: str = Field(alias="FirmwareUpdateImage")
    firmware_update_role: str = Field(alias="FirmwareUpdateRole")
    created_at: datetime = Field(alias="CreatedAt")
    redundancy_percent: int = Field(alias="RedundancyPercent")
    fragment_size_bytes: int = Field(alias="FragmentSizeBytes")
    fragment_interval_ms: int = Field(alias="FragmentIntervalMS")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMulticastGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    status: str = Field(alias="Status")
    lo_ra_wan: LoRaWANMulticastGetModel = Field(alias="LoRaWAN")
    created_at: datetime = Field(alias="CreatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMulticastGroupSessionResponseModel(BaseModel):
    lo_ra_wan: LoRaWANMulticastSessionModel = Field(alias="LoRaWAN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMulticastGroupSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    lo_ra_wan: LoRaWANMulticastSessionModel = Field(alias="LoRaWAN")


class GetPartnerAccountResponseModel(BaseModel):
    sidewalk: SidewalkAccountInfoWithFingerprintModel = Field(alias="Sidewalk")
    account_linked: bool = Field(alias="AccountLinked")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPartnerAccountsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    sidewalk: List[SidewalkAccountInfoWithFingerprintModel] = Field(alias="Sidewalk")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceProfileResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    lo_ra_wan: LoRaWANGetServiceProfileInfoModel = Field(alias="LoRaWAN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GsmNmrObjModel(BaseModel):
    bsic: int = Field(alias="Bsic")
    bcch: int = Field(alias="Bcch")
    rx_level: Optional[int] = Field(default=None, alias="RxLevel")
    global_identity: Optional[GlobalIdentityModel] = Field(
        default=None, alias="GlobalIdentity"
    )


class JoinEventConfigurationModel(BaseModel):
    lo_ra_wan: Optional[LoRaWANJoinEventNotificationConfigurationsModel] = Field(
        default=None, alias="LoRaWAN"
    )
    wireless_device_id_event_topic: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="WirelessDeviceIdEventTopic"
    )


class JoinResourceTypeEventConfigurationModel(BaseModel):
    lo_ra_wan: Optional[LoRaWANJoinResourceTypeEventConfigurationModel] = Field(
        default=None, alias="LoRaWAN"
    )


class ListMulticastGroupsByFuotaTaskResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    multicast_group_list: List[MulticastGroupByFuotaTaskModel] = Field(
        alias="MulticastGroupList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMulticastGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    multicast_group_list: List[MulticastGroupModel] = Field(alias="MulticastGroupList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworkAnalyzerConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    network_analyzer_configuration_list: List[
        NetworkAnalyzerConfigurationsModel
    ] = Field(alias="NetworkAnalyzerConfigurationList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceProfilesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    service_profile_list: List[ServiceProfileModel] = Field(alias="ServiceProfileList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoRaWANDeviceMetadataModel(BaseModel):
    dev_eui: Optional[str] = Field(default=None, alias="DevEui")
    fport: Optional[int] = Field(default=None, alias="FPort")
    data_rate: Optional[int] = Field(default=None, alias="DataRate")
    frequency: Optional[int] = Field(default=None, alias="Frequency")
    timestamp: Optional[str] = Field(default=None, alias="Timestamp")
    gateways: Optional[List[LoRaWANGatewayMetadataModel]] = Field(
        default=None, alias="Gateways"
    )


class LoRaWANGatewayCurrentVersionModel(BaseModel):
    current_version: Optional[LoRaWANGatewayVersionModel] = Field(
        default=None, alias="CurrentVersion"
    )


class LoRaWANUpdateGatewayTaskCreateModel(BaseModel):
    update_signature: Optional[str] = Field(default=None, alias="UpdateSignature")
    sig_key_crc: Optional[int] = Field(default=None, alias="SigKeyCrc")
    current_version: Optional[LoRaWANGatewayVersionModel] = Field(
        default=None, alias="CurrentVersion"
    )
    update_version: Optional[LoRaWANGatewayVersionModel] = Field(
        default=None, alias="UpdateVersion"
    )


class LoRaWANUpdateGatewayTaskEntryModel(BaseModel):
    current_version: Optional[LoRaWANGatewayVersionModel] = Field(
        default=None, alias="CurrentVersion"
    )
    update_version: Optional[LoRaWANGatewayVersionModel] = Field(
        default=None, alias="UpdateVersion"
    )


class MulticastWirelessMetadataModel(BaseModel):
    lo_ra_wan: Optional[LoRaWANMulticastMetadataModel] = Field(
        default=None, alias="LoRaWAN"
    )


class StartFuotaTaskRequestModel(BaseModel):
    id: str = Field(alias="Id")
    lo_ra_wan: Optional[LoRaWANStartFuotaTaskModel] = Field(
        default=None, alias="LoRaWAN"
    )


class LteObjModel(BaseModel):
    mcc: int = Field(alias="Mcc")
    mnc: int = Field(alias="Mnc")
    eutran_cid: int = Field(alias="EutranCid")
    tac: Optional[int] = Field(default=None, alias="Tac")
    lte_local_id: Optional[LteLocalIdModel] = Field(default=None, alias="LteLocalId")
    lte_timing_advance: Optional[int] = Field(default=None, alias="LteTimingAdvance")
    rsrp: Optional[int] = Field(default=None, alias="Rsrp")
    rsrq: Optional[float] = Field(default=None, alias="Rsrq")
    nr_capable: Optional[bool] = Field(default=None, alias="NrCapable")
    lte_nmr: Optional[Sequence[LteNmrObjModel]] = Field(default=None, alias="LteNmr")


class PositionSolverConfigurationsModel(BaseModel):
    semtech_gnss: Optional[SemtechGnssConfigurationModel] = Field(
        default=None, alias="SemtechGnss"
    )


class PositionSolverDetailsModel(BaseModel):
    semtech_gnss: Optional[SemtechGnssDetailModel] = Field(
        default=None, alias="SemtechGnss"
    )


class UpdatePartnerAccountRequestModel(BaseModel):
    sidewalk: SidewalkUpdateAccountModel = Field(alias="Sidewalk")
    partner_account_id: str = Field(alias="PartnerAccountId")
    partner_type: Literal["Sidewalk"] = Field(alias="PartnerType")


class TdscdmaObjModel(BaseModel):
    mcc: int = Field(alias="Mcc")
    mnc: int = Field(alias="Mnc")
    utran_cid: int = Field(alias="UtranCid")
    lac: Optional[int] = Field(default=None, alias="Lac")
    tdscdma_local_id: Optional[TdscdmaLocalIdModel] = Field(
        default=None, alias="TdscdmaLocalId"
    )
    tdscdma_timing_advance: Optional[int] = Field(
        default=None, alias="TdscdmaTimingAdvance"
    )
    rscp: Optional[int] = Field(default=None, alias="Rscp")
    path_loss: Optional[int] = Field(default=None, alias="PathLoss")
    tdscdma_nmr: Optional[Sequence[TdscdmaNmrObjModel]] = Field(
        default=None, alias="TdscdmaNmr"
    )


class WcdmaObjModel(BaseModel):
    mcc: int = Field(alias="Mcc")
    mnc: int = Field(alias="Mnc")
    utran_cid: int = Field(alias="UtranCid")
    lac: Optional[int] = Field(default=None, alias="Lac")
    wcdma_local_id: Optional[WcdmaLocalIdModel] = Field(
        default=None, alias="WcdmaLocalId"
    )
    rscp: Optional[int] = Field(default=None, alias="Rscp")
    path_loss: Optional[int] = Field(default=None, alias="PathLoss")
    wcdma_nmr: Optional[Sequence[WcdmaNmrObjModel]] = Field(
        default=None, alias="WcdmaNmr"
    )


class WirelessDeviceLogOptionModel(BaseModel):
    type: Literal["LoRaWAN", "Sidewalk"] = Field(alias="Type")
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")
    events: Optional[List[WirelessDeviceEventLogOptionModel]] = Field(
        default=None, alias="Events"
    )


class WirelessGatewayLogOptionModel(BaseModel):
    type: Literal["LoRaWAN"] = Field(alias="Type")
    log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(alias="LogLevel")
    events: Optional[List[WirelessGatewayEventLogOptionModel]] = Field(
        default=None, alias="Events"
    )


class CreateWirelessGatewayRequestModel(BaseModel):
    lo_ra_wan: LoRaWANGatewayModel = Field(alias="LoRaWAN")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class GetWirelessGatewayResponseModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    description: str = Field(alias="Description")
    lo_ra_wan: LoRaWANGatewayModel = Field(alias="LoRaWAN")
    arn: str = Field(alias="Arn")
    thing_name: str = Field(alias="ThingName")
    thing_arn: str = Field(alias="ThingArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WirelessGatewayStatisticsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    lo_ra_wan: Optional[LoRaWANGatewayModel] = Field(default=None, alias="LoRaWAN")
    last_uplink_received_at: Optional[str] = Field(
        default=None, alias="LastUplinkReceivedAt"
    )


class WirelessDeviceStatisticsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["LoRaWAN", "Sidewalk"]] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    destination_name: Optional[str] = Field(default=None, alias="DestinationName")
    last_uplink_received_at: Optional[str] = Field(
        default=None, alias="LastUplinkReceivedAt"
    )
    lo_ra_wan: Optional[LoRaWANListDeviceModel] = Field(default=None, alias="LoRaWAN")
    sidewalk: Optional[SidewalkListDeviceModel] = Field(default=None, alias="Sidewalk")
    fuota_device_status: Optional[
        Literal[
            "FragAlgo_unsupported",
            "FragIndex_unsupported",
            "Initial",
            "MICError",
            "MemoryError",
            "MissingFrag",
            "Not_enough_memory",
            "Package_Not_Supported",
            "SessionCnt_replay",
            "Successful",
            "Wrong_descriptor",
        ]
    ] = Field(default=None, alias="FuotaDeviceStatus")
    multicast_device_status: Optional[str] = Field(
        default=None, alias="MulticastDeviceStatus"
    )
    mc_group_id: Optional[int] = Field(default=None, alias="McGroupId")


class LoRaWANDeviceModel(BaseModel):
    dev_eui: Optional[str] = Field(default=None, alias="DevEui")
    device_profile_id: Optional[str] = Field(default=None, alias="DeviceProfileId")
    service_profile_id: Optional[str] = Field(default=None, alias="ServiceProfileId")
    otaa_v1_1: Optional[OtaaV1_1Model] = Field(default=None, alias="OtaaV1_1")
    otaa_v1_0x: Optional[OtaaV1_0_xModel] = Field(default=None, alias="OtaaV1_0_x")
    abp_v1_1: Optional[AbpV1_1Model] = Field(default=None, alias="AbpV1_1")
    abp_v1_0x: Optional[AbpV1_0_xModel] = Field(default=None, alias="AbpV1_0_x")
    fports: Optional[FPortsModel] = Field(default=None, alias="FPorts")


class LoRaWANUpdateDeviceModel(BaseModel):
    device_profile_id: Optional[str] = Field(default=None, alias="DeviceProfileId")
    service_profile_id: Optional[str] = Field(default=None, alias="ServiceProfileId")
    abp_v1_1: Optional[UpdateAbpV1_1Model] = Field(default=None, alias="AbpV1_1")
    abp_v1_0x: Optional[UpdateAbpV1_0_xModel] = Field(default=None, alias="AbpV1_0_x")
    fports: Optional[UpdateFPortsModel] = Field(default=None, alias="FPorts")


class LoRaWANSendDataToDeviceModel(BaseModel):
    fport: Optional[int] = Field(default=None, alias="FPort")
    participating_gateways: Optional[ParticipatingGatewaysModel] = Field(
        default=None, alias="ParticipatingGateways"
    )


class GsmObjModel(BaseModel):
    mcc: int = Field(alias="Mcc")
    mnc: int = Field(alias="Mnc")
    lac: int = Field(alias="Lac")
    geran_cid: int = Field(alias="GeranCid")
    gsm_local_id: Optional[GsmLocalIdModel] = Field(default=None, alias="GsmLocalId")
    gsm_timing_advance: Optional[int] = Field(default=None, alias="GsmTimingAdvance")
    rx_level: Optional[int] = Field(default=None, alias="RxLevel")
    gsm_nmr: Optional[Sequence[GsmNmrObjModel]] = Field(default=None, alias="GsmNmr")


class EventNotificationItemConfigurationsModel(BaseModel):
    device_registration_state: Optional[
        DeviceRegistrationStateEventConfigurationModel
    ] = Field(default=None, alias="DeviceRegistrationState")
    proximity: Optional[ProximityEventConfigurationModel] = Field(
        default=None, alias="Proximity"
    )
    join: Optional[JoinEventConfigurationModel] = Field(default=None, alias="Join")
    connection_status: Optional[ConnectionStatusEventConfigurationModel] = Field(
        default=None, alias="ConnectionStatus"
    )
    message_delivery_status: Optional[
        MessageDeliveryStatusEventConfigurationModel
    ] = Field(default=None, alias="MessageDeliveryStatus")


class GetResourceEventConfigurationResponseModel(BaseModel):
    device_registration_state: DeviceRegistrationStateEventConfigurationModel = Field(
        alias="DeviceRegistrationState"
    )
    proximity: ProximityEventConfigurationModel = Field(alias="Proximity")
    join: JoinEventConfigurationModel = Field(alias="Join")
    connection_status: ConnectionStatusEventConfigurationModel = Field(
        alias="ConnectionStatus"
    )
    message_delivery_status: MessageDeliveryStatusEventConfigurationModel = Field(
        alias="MessageDeliveryStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceEventConfigurationRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    identifier_type: Literal[
        "DevEui",
        "GatewayEui",
        "PartnerAccountId",
        "WirelessDeviceId",
        "WirelessGatewayId",
    ] = Field(alias="IdentifierType")
    partner_type: Optional[Literal["Sidewalk"]] = Field(
        default=None, alias="PartnerType"
    )
    device_registration_state: Optional[
        DeviceRegistrationStateEventConfigurationModel
    ] = Field(default=None, alias="DeviceRegistrationState")
    proximity: Optional[ProximityEventConfigurationModel] = Field(
        default=None, alias="Proximity"
    )
    join: Optional[JoinEventConfigurationModel] = Field(default=None, alias="Join")
    connection_status: Optional[ConnectionStatusEventConfigurationModel] = Field(
        default=None, alias="ConnectionStatus"
    )
    message_delivery_status: Optional[
        MessageDeliveryStatusEventConfigurationModel
    ] = Field(default=None, alias="MessageDeliveryStatus")


class GetEventConfigurationByResourceTypesResponseModel(BaseModel):
    device_registration_state: DeviceRegistrationStateResourceTypeEventConfigurationModel = Field(
        alias="DeviceRegistrationState"
    )
    proximity: ProximityResourceTypeEventConfigurationModel = Field(alias="Proximity")
    join: JoinResourceTypeEventConfigurationModel = Field(alias="Join")
    connection_status: ConnectionStatusResourceTypeEventConfigurationModel = Field(
        alias="ConnectionStatus"
    )
    message_delivery_status: MessageDeliveryStatusResourceTypeEventConfigurationModel = Field(
        alias="MessageDeliveryStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEventConfigurationByResourceTypesRequestModel(BaseModel):
    device_registration_state: Optional[
        DeviceRegistrationStateResourceTypeEventConfigurationModel
    ] = Field(default=None, alias="DeviceRegistrationState")
    proximity: Optional[ProximityResourceTypeEventConfigurationModel] = Field(
        default=None, alias="Proximity"
    )
    join: Optional[JoinResourceTypeEventConfigurationModel] = Field(
        default=None, alias="Join"
    )
    connection_status: Optional[
        ConnectionStatusResourceTypeEventConfigurationModel
    ] = Field(default=None, alias="ConnectionStatus")
    message_delivery_status: Optional[
        MessageDeliveryStatusResourceTypeEventConfigurationModel
    ] = Field(default=None, alias="MessageDeliveryStatus")


class GetWirelessDeviceStatisticsResponseModel(BaseModel):
    wireless_device_id: str = Field(alias="WirelessDeviceId")
    last_uplink_received_at: str = Field(alias="LastUplinkReceivedAt")
    lo_ra_wan: LoRaWANDeviceMetadataModel = Field(alias="LoRaWAN")
    sidewalk: SidewalkDeviceMetadataModel = Field(alias="Sidewalk")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWirelessGatewayFirmwareInformationResponseModel(BaseModel):
    lo_ra_wan: LoRaWANGatewayCurrentVersionModel = Field(alias="LoRaWAN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWirelessGatewayTaskCreateModel(BaseModel):
    update_data_source: Optional[str] = Field(default=None, alias="UpdateDataSource")
    update_data_role: Optional[str] = Field(default=None, alias="UpdateDataRole")
    lo_ra_wan: Optional[LoRaWANUpdateGatewayTaskCreateModel] = Field(
        default=None, alias="LoRaWAN"
    )


class UpdateWirelessGatewayTaskEntryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    lo_ra_wan: Optional[LoRaWANUpdateGatewayTaskEntryModel] = Field(
        default=None, alias="LoRaWAN"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")


class SendDataToMulticastGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    payload_data: str = Field(alias="PayloadData")
    wireless_metadata: MulticastWirelessMetadataModel = Field(alias="WirelessMetadata")


class PutPositionConfigurationRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    resource_type: Literal["WirelessDevice", "WirelessGateway"] = Field(
        alias="ResourceType"
    )
    solvers: Optional[PositionSolverConfigurationsModel] = Field(
        default=None, alias="Solvers"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")


class GetPositionConfigurationResponseModel(BaseModel):
    solvers: PositionSolverDetailsModel = Field(alias="Solvers")
    destination: str = Field(alias="Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PositionConfigurationItemModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    resource_type: Optional[Literal["WirelessDevice", "WirelessGateway"]] = Field(
        default=None, alias="ResourceType"
    )
    solvers: Optional[PositionSolverDetailsModel] = Field(default=None, alias="Solvers")
    destination: Optional[str] = Field(default=None, alias="Destination")


class GetLogLevelsByResourceTypesResponseModel(BaseModel):
    default_log_level: Literal["DISABLED", "ERROR", "INFO"] = Field(
        alias="DefaultLogLevel"
    )
    wireless_gateway_log_options: List[WirelessGatewayLogOptionModel] = Field(
        alias="WirelessGatewayLogOptions"
    )
    wireless_device_log_options: List[WirelessDeviceLogOptionModel] = Field(
        alias="WirelessDeviceLogOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLogLevelsByResourceTypesRequestModel(BaseModel):
    default_log_level: Optional[Literal["DISABLED", "ERROR", "INFO"]] = Field(
        default=None, alias="DefaultLogLevel"
    )
    wireless_device_log_options: Optional[
        Sequence[WirelessDeviceLogOptionModel]
    ] = Field(default=None, alias="WirelessDeviceLogOptions")
    wireless_gateway_log_options: Optional[
        Sequence[WirelessGatewayLogOptionModel]
    ] = Field(default=None, alias="WirelessGatewayLogOptions")


class ListWirelessGatewaysResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    wireless_gateway_list: List[WirelessGatewayStatisticsModel] = Field(
        alias="WirelessGatewayList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWirelessDevicesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    wireless_device_list: List[WirelessDeviceStatisticsModel] = Field(
        alias="WirelessDeviceList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWirelessDeviceRequestModel(BaseModel):
    type: Literal["LoRaWAN", "Sidewalk"] = Field(alias="Type")
    destination_name: str = Field(alias="DestinationName")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    lo_ra_wan: Optional[LoRaWANDeviceModel] = Field(default=None, alias="LoRaWAN")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    positioning: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Positioning"
    )


class GetWirelessDeviceResponseModel(BaseModel):
    type: Literal["LoRaWAN", "Sidewalk"] = Field(alias="Type")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    destination_name: str = Field(alias="DestinationName")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    thing_name: str = Field(alias="ThingName")
    thing_arn: str = Field(alias="ThingArn")
    lo_ra_wan: LoRaWANDeviceModel = Field(alias="LoRaWAN")
    sidewalk: SidewalkDeviceModel = Field(alias="Sidewalk")
    positioning: Literal["Disabled", "Enabled"] = Field(alias="Positioning")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWirelessDeviceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    destination_name: Optional[str] = Field(default=None, alias="DestinationName")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    lo_ra_wan: Optional[LoRaWANUpdateDeviceModel] = Field(default=None, alias="LoRaWAN")
    positioning: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Positioning"
    )


class DownlinkQueueMessageModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    transmit_mode: Optional[int] = Field(default=None, alias="TransmitMode")
    received_at: Optional[str] = Field(default=None, alias="ReceivedAt")
    lo_ra_wan: Optional[LoRaWANSendDataToDeviceModel] = Field(
        default=None, alias="LoRaWAN"
    )


class WirelessMetadataModel(BaseModel):
    lo_ra_wan: Optional[LoRaWANSendDataToDeviceModel] = Field(
        default=None, alias="LoRaWAN"
    )
    sidewalk: Optional[SidewalkSendDataToDeviceModel] = Field(
        default=None, alias="Sidewalk"
    )


class CellTowersModel(BaseModel):
    gsm: Optional[Sequence[GsmObjModel]] = Field(default=None, alias="Gsm")
    wcdma: Optional[Sequence[WcdmaObjModel]] = Field(default=None, alias="Wcdma")
    tdscdma: Optional[Sequence[TdscdmaObjModel]] = Field(default=None, alias="Tdscdma")
    lte: Optional[Sequence[LteObjModel]] = Field(default=None, alias="Lte")
    cdma: Optional[Sequence[CdmaObjModel]] = Field(default=None, alias="Cdma")


class EventConfigurationItemModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    identifier_type: Optional[
        Literal[
            "DevEui",
            "GatewayEui",
            "PartnerAccountId",
            "WirelessDeviceId",
            "WirelessGatewayId",
        ]
    ] = Field(default=None, alias="IdentifierType")
    partner_type: Optional[Literal["Sidewalk"]] = Field(
        default=None, alias="PartnerType"
    )
    events: Optional[EventNotificationItemConfigurationsModel] = Field(
        default=None, alias="Events"
    )


class CreateWirelessGatewayTaskDefinitionRequestModel(BaseModel):
    auto_create_tasks: bool = Field(alias="AutoCreateTasks")
    name: Optional[str] = Field(default=None, alias="Name")
    update: Optional[UpdateWirelessGatewayTaskCreateModel] = Field(
        default=None, alias="Update"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetWirelessGatewayTaskDefinitionResponseModel(BaseModel):
    auto_create_tasks: bool = Field(alias="AutoCreateTasks")
    name: str = Field(alias="Name")
    update: UpdateWirelessGatewayTaskCreateModel = Field(alias="Update")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWirelessGatewayTaskDefinitionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    task_definitions: List[UpdateWirelessGatewayTaskEntryModel] = Field(
        alias="TaskDefinitions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPositionConfigurationsResponseModel(BaseModel):
    position_configuration_list: List[PositionConfigurationItemModel] = Field(
        alias="PositionConfigurationList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueuedMessagesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    downlink_queue_messages_list: List[DownlinkQueueMessageModel] = Field(
        alias="DownlinkQueueMessagesList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendDataToWirelessDeviceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    transmit_mode: int = Field(alias="TransmitMode")
    payload_data: str = Field(alias="PayloadData")
    wireless_metadata: Optional[WirelessMetadataModel] = Field(
        default=None, alias="WirelessMetadata"
    )


class GetPositionEstimateRequestModel(BaseModel):
    wi_fi_access_points: Optional[Sequence[WiFiAccessPointModel]] = Field(
        default=None, alias="WiFiAccessPoints"
    )
    cell_towers: Optional[CellTowersModel] = Field(default=None, alias="CellTowers")
    ip: Optional[IpModel] = Field(default=None, alias="Ip")
    gnss: Optional[GnssModel] = Field(default=None, alias="Gnss")
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")


class ListEventConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    event_configurations_list: List[EventConfigurationItemModel] = Field(
        alias="EventConfigurationsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
