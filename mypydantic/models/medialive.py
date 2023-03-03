# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AacSettingsModel(BaseModel):
    bitrate: Optional[float] = Field(default=None, alias="Bitrate")
    coding_mode: Optional[
        Literal[
            "AD_RECEIVER_MIX",
            "CODING_MODE_1_0",
            "CODING_MODE_1_1",
            "CODING_MODE_2_0",
            "CODING_MODE_5_1",
        ]
    ] = Field(default=None, alias="CodingMode")
    input_type: Optional[Literal["BROADCASTER_MIXED_AD", "NORMAL"]] = Field(
        default=None, alias="InputType"
    )
    profile: Optional[Literal["HEV1", "HEV2", "LC"]] = Field(
        default=None, alias="Profile"
    )
    rate_control_mode: Optional[Literal["CBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    raw_format: Optional[Literal["LATM_LOAS", "NONE"]] = Field(
        default=None, alias="RawFormat"
    )
    sample_rate: Optional[float] = Field(default=None, alias="SampleRate")
    spec: Optional[Literal["MPEG2", "MPEG4"]] = Field(default=None, alias="Spec")
    vbr_quality: Optional[Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]] = Field(
        default=None, alias="VbrQuality"
    )


class Ac3SettingsModel(BaseModel):
    bitrate: Optional[float] = Field(default=None, alias="Bitrate")
    bitstream_mode: Optional[
        Literal[
            "COMMENTARY",
            "COMPLETE_MAIN",
            "DIALOGUE",
            "EMERGENCY",
            "HEARING_IMPAIRED",
            "MUSIC_AND_EFFECTS",
            "VISUALLY_IMPAIRED",
            "VOICE_OVER",
        ]
    ] = Field(default=None, alias="BitstreamMode")
    coding_mode: Optional[
        Literal[
            "CODING_MODE_1_0",
            "CODING_MODE_1_1",
            "CODING_MODE_2_0",
            "CODING_MODE_3_2_LFE",
        ]
    ] = Field(default=None, alias="CodingMode")
    dialnorm: Optional[int] = Field(default=None, alias="Dialnorm")
    drc_profile: Optional[Literal["FILM_STANDARD", "NONE"]] = Field(
        default=None, alias="DrcProfile"
    )
    lfe_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="LfeFilter"
    )
    metadata_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="MetadataControl"
    )


class AcceptInputDeviceTransferRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")


class AncillarySourceSettingsModel(BaseModel):
    source_ancillary_channel_number: Optional[int] = Field(
        default=None, alias="SourceAncillaryChannelNumber"
    )


class ArchiveS3SettingsModel(BaseModel):
    canned_acl: Optional[
        Literal[
            "AUTHENTICATED_READ",
            "BUCKET_OWNER_FULL_CONTROL",
            "BUCKET_OWNER_READ",
            "PUBLIC_READ",
        ]
    ] = Field(default=None, alias="CannedAcl")


class OutputLocationRefModel(BaseModel):
    destination_ref_id: Optional[str] = Field(default=None, alias="DestinationRefId")


class InputChannelLevelModel(BaseModel):
    gain: int = Field(alias="Gain")
    input_channel: int = Field(alias="InputChannel")


class Eac3AtmosSettingsModel(BaseModel):
    bitrate: Optional[float] = Field(default=None, alias="Bitrate")
    coding_mode: Optional[
        Literal["CODING_MODE_5_1_4", "CODING_MODE_7_1_4", "CODING_MODE_9_1_6"]
    ] = Field(default=None, alias="CodingMode")
    dialnorm: Optional[int] = Field(default=None, alias="Dialnorm")
    drc_line: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DrcLine")
    drc_rf: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DrcRf")
    height_trim: Optional[float] = Field(default=None, alias="HeightTrim")
    surround_trim: Optional[float] = Field(default=None, alias="SurroundTrim")


class Eac3SettingsModel(BaseModel):
    attenuation_control: Optional[Literal["ATTENUATE_3_DB", "NONE"]] = Field(
        default=None, alias="AttenuationControl"
    )
    bitrate: Optional[float] = Field(default=None, alias="Bitrate")
    bitstream_mode: Optional[
        Literal[
            "COMMENTARY",
            "COMPLETE_MAIN",
            "EMERGENCY",
            "HEARING_IMPAIRED",
            "VISUALLY_IMPAIRED",
        ]
    ] = Field(default=None, alias="BitstreamMode")
    coding_mode: Optional[
        Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
    ] = Field(default=None, alias="CodingMode")
    dc_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DcFilter"
    )
    dialnorm: Optional[int] = Field(default=None, alias="Dialnorm")
    drc_line: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DrcLine")
    drc_rf: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DrcRf")
    lfe_control: Optional[Literal["LFE", "NO_LFE"]] = Field(
        default=None, alias="LfeControl"
    )
    lfe_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="LfeFilter"
    )
    lo_ro_center_mix_level: Optional[float] = Field(
        default=None, alias="LoRoCenterMixLevel"
    )
    lo_ro_surround_mix_level: Optional[float] = Field(
        default=None, alias="LoRoSurroundMixLevel"
    )
    lt_rt_center_mix_level: Optional[float] = Field(
        default=None, alias="LtRtCenterMixLevel"
    )
    lt_rt_surround_mix_level: Optional[float] = Field(
        default=None, alias="LtRtSurroundMixLevel"
    )
    metadata_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="MetadataControl"
    )
    passthrough_control: Optional[Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]] = Field(
        default=None, alias="PassthroughControl"
    )
    phase_control: Optional[Literal["NO_SHIFT", "SHIFT_90_DEGREES"]] = Field(
        default=None, alias="PhaseControl"
    )
    stereo_downmix: Optional[
        Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
    ] = Field(default=None, alias="StereoDownmix")
    surround_ex_mode: Optional[Literal["DISABLED", "ENABLED", "NOT_INDICATED"]] = Field(
        default=None, alias="SurroundExMode"
    )
    surround_mode: Optional[Literal["DISABLED", "ENABLED", "NOT_INDICATED"]] = Field(
        default=None, alias="SurroundMode"
    )


class Mp2SettingsModel(BaseModel):
    bitrate: Optional[float] = Field(default=None, alias="Bitrate")
    coding_mode: Optional[Literal["CODING_MODE_1_0", "CODING_MODE_2_0"]] = Field(
        default=None, alias="CodingMode"
    )
    sample_rate: Optional[float] = Field(default=None, alias="SampleRate")


class WavSettingsModel(BaseModel):
    bit_depth: Optional[float] = Field(default=None, alias="BitDepth")
    coding_mode: Optional[
        Literal[
            "CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_4_0", "CODING_MODE_8_0"
        ]
    ] = Field(default=None, alias="CodingMode")
    sample_rate: Optional[float] = Field(default=None, alias="SampleRate")


class AudioNormalizationSettingsModel(BaseModel):
    algorithm: Optional[Literal["ITU_1770_1", "ITU_1770_2"]] = Field(
        default=None, alias="Algorithm"
    )
    algorithm_control: Optional[Literal["CORRECT_AUDIO"]] = Field(
        default=None, alias="AlgorithmControl"
    )
    target_lkfs: Optional[float] = Field(default=None, alias="TargetLkfs")


class AudioDolbyEDecodeModel(BaseModel):
    program_selection: Literal[
        "ALL_CHANNELS",
        "PROGRAM_1",
        "PROGRAM_2",
        "PROGRAM_3",
        "PROGRAM_4",
        "PROGRAM_5",
        "PROGRAM_6",
        "PROGRAM_7",
        "PROGRAM_8",
    ] = Field(alias="ProgramSelection")


class AudioHlsRenditionSelectionModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    name: str = Field(alias="Name")


class AudioLanguageSelectionModel(BaseModel):
    language_code: str = Field(alias="LanguageCode")
    language_selection_policy: Optional[Literal["LOOSE", "STRICT"]] = Field(
        default=None, alias="LanguageSelectionPolicy"
    )


class InputLocationModel(BaseModel):
    uri: str = Field(alias="Uri")
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    username: Optional[str] = Field(default=None, alias="Username")


class AudioPidSelectionModel(BaseModel):
    pid: int = Field(alias="Pid")


class AudioSilenceFailoverSettingsModel(BaseModel):
    audio_selector_name: str = Field(alias="AudioSelectorName")
    audio_silence_threshold_msec: Optional[int] = Field(
        default=None, alias="AudioSilenceThresholdMsec"
    )


class AudioTrackModel(BaseModel):
    track: int = Field(alias="Track")


class EsamModel(BaseModel):
    acquisition_point_id: str = Field(alias="AcquisitionPointId")
    pois_endpoint: str = Field(alias="PoisEndpoint")
    ad_avail_offset: Optional[int] = Field(default=None, alias="AdAvailOffset")
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    username: Optional[str] = Field(default=None, alias="Username")
    zone_identity: Optional[str] = Field(default=None, alias="ZoneIdentity")


class Scte35SpliceInsertModel(BaseModel):
    ad_avail_offset: Optional[int] = Field(default=None, alias="AdAvailOffset")
    no_regional_blackout_flag: Optional[Literal["FOLLOW", "IGNORE"]] = Field(
        default=None, alias="NoRegionalBlackoutFlag"
    )
    web_delivery_allowed_flag: Optional[Literal["FOLLOW", "IGNORE"]] = Field(
        default=None, alias="WebDeliveryAllowedFlag"
    )


class Scte35TimeSignalAposModel(BaseModel):
    ad_avail_offset: Optional[int] = Field(default=None, alias="AdAvailOffset")
    no_regional_blackout_flag: Optional[Literal["FOLLOW", "IGNORE"]] = Field(
        default=None, alias="NoRegionalBlackoutFlag"
    )
    web_delivery_allowed_flag: Optional[Literal["FOLLOW", "IGNORE"]] = Field(
        default=None, alias="WebDeliveryAllowedFlag"
    )


class BatchDeleteRequestModel(BaseModel):
    channel_ids: Optional[Sequence[str]] = Field(default=None, alias="ChannelIds")
    input_ids: Optional[Sequence[str]] = Field(default=None, alias="InputIds")
    input_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="InputSecurityGroupIds"
    )
    multiplex_ids: Optional[Sequence[str]] = Field(default=None, alias="MultiplexIds")


class BatchFailedResultModelModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    code: Optional[str] = Field(default=None, alias="Code")
    id: Optional[str] = Field(default=None, alias="Id")
    message: Optional[str] = Field(default=None, alias="Message")


class BatchSuccessfulResultModelModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    state: Optional[str] = Field(default=None, alias="State")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchScheduleActionDeleteRequestModel(BaseModel):
    action_names: Sequence[str] = Field(alias="ActionNames")


class BatchStartRequestModel(BaseModel):
    channel_ids: Optional[Sequence[str]] = Field(default=None, alias="ChannelIds")
    multiplex_ids: Optional[Sequence[str]] = Field(default=None, alias="MultiplexIds")


class BatchStopRequestModel(BaseModel):
    channel_ids: Optional[Sequence[str]] = Field(default=None, alias="ChannelIds")
    multiplex_ids: Optional[Sequence[str]] = Field(default=None, alias="MultiplexIds")


class CancelInputDeviceTransferRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")


class EbuTtDDestinationSettingsModel(BaseModel):
    copyright_holder: Optional[str] = Field(default=None, alias="CopyrightHolder")
    fill_line_gap: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FillLineGap"
    )
    font_family: Optional[str] = Field(default=None, alias="FontFamily")
    style_control: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="StyleControl"
    )


class TtmlDestinationSettingsModel(BaseModel):
    style_control: Optional[Literal["PASSTHROUGH", "USE_CONFIGURED"]] = Field(
        default=None, alias="StyleControl"
    )


class WebvttDestinationSettingsModel(BaseModel):
    style_control: Optional[Literal["NO_STYLE_DATA", "PASSTHROUGH"]] = Field(
        default=None, alias="StyleControl"
    )


class CaptionLanguageMappingModel(BaseModel):
    caption_channel: int = Field(alias="CaptionChannel")
    language_code: str = Field(alias="LanguageCode")
    language_description: str = Field(alias="LanguageDescription")


class CaptionRectangleModel(BaseModel):
    height: float = Field(alias="Height")
    left_offset: float = Field(alias="LeftOffset")
    top_offset: float = Field(alias="TopOffset")
    width: float = Field(alias="Width")


class DvbSubSourceSettingsModel(BaseModel):
    ocr_language: Optional[Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]] = Field(
        default=None, alias="OcrLanguage"
    )
    pid: Optional[int] = Field(default=None, alias="Pid")


class EmbeddedSourceSettingsModel(BaseModel):
    convert608_to708: Optional[Literal["DISABLED", "UPCONVERT"]] = Field(
        default=None, alias="Convert608To708"
    )
    scte20_detection: Optional[Literal["AUTO", "OFF"]] = Field(
        default=None, alias="Scte20Detection"
    )
    source608_channel_number: Optional[int] = Field(
        default=None, alias="Source608ChannelNumber"
    )
    source608_track_number: Optional[int] = Field(
        default=None, alias="Source608TrackNumber"
    )


class Scte20SourceSettingsModel(BaseModel):
    convert608_to708: Optional[Literal["DISABLED", "UPCONVERT"]] = Field(
        default=None, alias="Convert608To708"
    )
    source608_channel_number: Optional[int] = Field(
        default=None, alias="Source608ChannelNumber"
    )


class Scte27SourceSettingsModel(BaseModel):
    ocr_language: Optional[Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]] = Field(
        default=None, alias="OcrLanguage"
    )
    pid: Optional[int] = Field(default=None, alias="Pid")


class CdiInputSpecificationModel(BaseModel):
    resolution: Optional[Literal["FHD", "HD", "SD", "UHD"]] = Field(
        default=None, alias="Resolution"
    )


class ChannelEgressEndpointModel(BaseModel):
    source_ip: Optional[str] = Field(default=None, alias="SourceIp")


class InputSpecificationModel(BaseModel):
    codec: Optional[Literal["AVC", "HEVC", "MPEG2"]] = Field(
        default=None, alias="Codec"
    )
    maximum_bitrate: Optional[
        Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
    ] = Field(default=None, alias="MaximumBitrate")
    resolution: Optional[Literal["HD", "SD", "UHD"]] = Field(
        default=None, alias="Resolution"
    )


class MaintenanceStatusModel(BaseModel):
    maintenance_day: Optional[
        Literal[
            "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
        ]
    ] = Field(default=None, alias="MaintenanceDay")
    maintenance_deadline: Optional[str] = Field(
        default=None, alias="MaintenanceDeadline"
    )
    maintenance_scheduled_date: Optional[str] = Field(
        default=None, alias="MaintenanceScheduledDate"
    )
    maintenance_start_time: Optional[str] = Field(
        default=None, alias="MaintenanceStartTime"
    )


class VpcOutputSettingsDescriptionModel(BaseModel):
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    network_interface_ids: Optional[List[str]] = Field(
        default=None, alias="NetworkInterfaceIds"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")


class PipelineDetailModel(BaseModel):
    active_input_attachment_name: Optional[str] = Field(
        default=None, alias="ActiveInputAttachmentName"
    )
    active_input_switch_action_name: Optional[str] = Field(
        default=None, alias="ActiveInputSwitchActionName"
    )
    active_motion_graphics_action_name: Optional[str] = Field(
        default=None, alias="ActiveMotionGraphicsActionName"
    )
    active_motion_graphics_uri: Optional[str] = Field(
        default=None, alias="ActiveMotionGraphicsUri"
    )
    pipeline_id: Optional[str] = Field(default=None, alias="PipelineId")


class ClaimDeviceRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class MaintenanceCreateSettingsModel(BaseModel):
    maintenance_day: Optional[
        Literal[
            "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
        ]
    ] = Field(default=None, alias="MaintenanceDay")
    maintenance_start_time: Optional[str] = Field(
        default=None, alias="MaintenanceStartTime"
    )


class VpcOutputSettingsModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    public_address_allocation_ids: Optional[Sequence[str]] = Field(
        default=None, alias="PublicAddressAllocationIds"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class InputDestinationRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class InputDeviceSettingsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class InputSourceRequestModel(BaseModel):
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")


class InputVpcRequestModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class MediaConnectFlowRequestModel(BaseModel):
    flow_arn: Optional[str] = Field(default=None, alias="FlowArn")


class InputWhitelistRuleCidrModel(BaseModel):
    cidr: Optional[str] = Field(default=None, alias="Cidr")


class MultiplexSettingsModel(BaseModel):
    transport_stream_bitrate: int = Field(alias="TransportStreamBitrate")
    transport_stream_id: int = Field(alias="TransportStreamId")
    maximum_video_buffer_delay_milliseconds: Optional[int] = Field(
        default=None, alias="MaximumVideoBufferDelayMilliseconds"
    )
    transport_stream_reserved_bitrate: Optional[int] = Field(
        default=None, alias="TransportStreamReservedBitrate"
    )


class CreatePartnerInputRequestModel(BaseModel):
    input_id: str = Field(alias="InputId")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")


class DeleteInputRequestModel(BaseModel):
    input_id: str = Field(alias="InputId")


class DeleteInputSecurityGroupRequestModel(BaseModel):
    input_security_group_id: str = Field(alias="InputSecurityGroupId")


class DeleteMultiplexProgramRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    program_name: str = Field(alias="ProgramName")


class MultiplexProgramPacketIdentifiersMapModel(BaseModel):
    audio_pids: Optional[List[int]] = Field(default=None, alias="AudioPids")
    dvb_sub_pids: Optional[List[int]] = Field(default=None, alias="DvbSubPids")
    dvb_teletext_pid: Optional[int] = Field(default=None, alias="DvbTeletextPid")
    etv_platform_pid: Optional[int] = Field(default=None, alias="EtvPlatformPid")
    etv_signal_pid: Optional[int] = Field(default=None, alias="EtvSignalPid")
    klv_data_pids: Optional[List[int]] = Field(default=None, alias="KlvDataPids")
    pcr_pid: Optional[int] = Field(default=None, alias="PcrPid")
    pmt_pid: Optional[int] = Field(default=None, alias="PmtPid")
    private_metadata_pid: Optional[int] = Field(
        default=None, alias="PrivateMetadataPid"
    )
    scte27_pids: Optional[List[int]] = Field(default=None, alias="Scte27Pids")
    scte35_pid: Optional[int] = Field(default=None, alias="Scte35Pid")
    timed_metadata_pid: Optional[int] = Field(default=None, alias="TimedMetadataPid")
    video_pid: Optional[int] = Field(default=None, alias="VideoPid")


class MultiplexProgramPipelineDetailModel(BaseModel):
    active_channel_pipeline: Optional[str] = Field(
        default=None, alias="ActiveChannelPipeline"
    )
    pipeline_id: Optional[str] = Field(default=None, alias="PipelineId")


class DeleteMultiplexRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")


class DeleteReservationRequestModel(BaseModel):
    reservation_id: str = Field(alias="ReservationId")


class RenewalSettingsModel(BaseModel):
    automatic_renewal: Optional[Literal["DISABLED", "ENABLED", "UNAVAILABLE"]] = Field(
        default=None, alias="AutomaticRenewal"
    )
    renewal_count: Optional[int] = Field(default=None, alias="RenewalCount")


class ReservationResourceSpecificationModel(BaseModel):
    channel_class: Optional[Literal["SINGLE_PIPELINE", "STANDARD"]] = Field(
        default=None, alias="ChannelClass"
    )
    codec: Optional[Literal["AUDIO", "AVC", "HEVC", "LINK", "MPEG2"]] = Field(
        default=None, alias="Codec"
    )
    maximum_bitrate: Optional[
        Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
    ] = Field(default=None, alias="MaximumBitrate")
    maximum_framerate: Optional[Literal["MAX_30_FPS", "MAX_60_FPS"]] = Field(
        default=None, alias="MaximumFramerate"
    )
    resolution: Optional[Literal["FHD", "HD", "SD", "UHD"]] = Field(
        default=None, alias="Resolution"
    )
    resource_type: Optional[Literal["CHANNEL", "INPUT", "MULTIPLEX", "OUTPUT"]] = Field(
        default=None, alias="ResourceType"
    )
    special_feature: Optional[
        Literal["ADVANCED_AUDIO", "AUDIO_NORMALIZATION", "MGHD", "MGUHD"]
    ] = Field(default=None, alias="SpecialFeature")
    video_quality: Optional[Literal["ENHANCED", "PREMIUM", "STANDARD"]] = Field(
        default=None, alias="VideoQuality"
    )


class DeleteScheduleRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")


class DeleteTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")


class DescribeInputDeviceRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")


class InputDeviceHdSettingsModel(BaseModel):
    active_input: Optional[Literal["HDMI", "SDI"]] = Field(
        default=None, alias="ActiveInput"
    )
    configured_input: Optional[Literal["AUTO", "HDMI", "SDI"]] = Field(
        default=None, alias="ConfiguredInput"
    )
    device_state: Optional[Literal["IDLE", "STREAMING"]] = Field(
        default=None, alias="DeviceState"
    )
    framerate: Optional[float] = Field(default=None, alias="Framerate")
    height: Optional[int] = Field(default=None, alias="Height")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    scan_type: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="ScanType"
    )
    width: Optional[int] = Field(default=None, alias="Width")
    latency_ms: Optional[int] = Field(default=None, alias="LatencyMs")


class InputDeviceNetworkSettingsModel(BaseModel):
    dns_addresses: Optional[List[str]] = Field(default=None, alias="DnsAddresses")
    gateway: Optional[str] = Field(default=None, alias="Gateway")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    ip_scheme: Optional[Literal["DHCP", "STATIC"]] = Field(
        default=None, alias="IpScheme"
    )
    subnet_mask: Optional[str] = Field(default=None, alias="SubnetMask")


class InputDeviceUhdSettingsModel(BaseModel):
    active_input: Optional[Literal["HDMI", "SDI"]] = Field(
        default=None, alias="ActiveInput"
    )
    configured_input: Optional[Literal["AUTO", "HDMI", "SDI"]] = Field(
        default=None, alias="ConfiguredInput"
    )
    device_state: Optional[Literal["IDLE", "STREAMING"]] = Field(
        default=None, alias="DeviceState"
    )
    framerate: Optional[float] = Field(default=None, alias="Framerate")
    height: Optional[int] = Field(default=None, alias="Height")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    scan_type: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="ScanType"
    )
    width: Optional[int] = Field(default=None, alias="Width")
    latency_ms: Optional[int] = Field(default=None, alias="LatencyMs")


class DescribeInputDeviceThumbnailRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")
    accept: Literal["image/jpeg"] = Field(alias="Accept")


class DescribeInputRequestModel(BaseModel):
    input_id: str = Field(alias="InputId")


class InputSourceModel(BaseModel):
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")


class MediaConnectFlowModel(BaseModel):
    flow_arn: Optional[str] = Field(default=None, alias="FlowArn")


class DescribeInputSecurityGroupRequestModel(BaseModel):
    input_security_group_id: str = Field(alias="InputSecurityGroupId")


class InputWhitelistRuleModel(BaseModel):
    cidr: Optional[str] = Field(default=None, alias="Cidr")


class DescribeMultiplexProgramRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    program_name: str = Field(alias="ProgramName")


class DescribeMultiplexRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")


class DescribeOfferingRequestModel(BaseModel):
    offering_id: str = Field(alias="OfferingId")


class DescribeReservationRequestModel(BaseModel):
    reservation_id: str = Field(alias="ReservationId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeScheduleRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DvbNitSettingsModel(BaseModel):
    network_id: int = Field(alias="NetworkId")
    network_name: str = Field(alias="NetworkName")
    rep_interval: Optional[int] = Field(default=None, alias="RepInterval")


class DvbSdtSettingsModel(BaseModel):
    output_sdt: Optional[
        Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
    ] = Field(default=None, alias="OutputSdt")
    rep_interval: Optional[int] = Field(default=None, alias="RepInterval")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_provider_name: Optional[str] = Field(
        default=None, alias="ServiceProviderName"
    )


class DvbTdtSettingsModel(BaseModel):
    rep_interval: Optional[int] = Field(default=None, alias="RepInterval")


class FeatureActivationsModel(BaseModel):
    input_prepare_schedule_actions: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="InputPrepareScheduleActions"
    )


class NielsenConfigurationModel(BaseModel):
    distributor_id: Optional[str] = Field(default=None, alias="DistributorId")
    nielsen_pcm_to_id3_tagging: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="NielsenPcmToId3Tagging"
    )


class TimecodeConfigModel(BaseModel):
    source: Literal["EMBEDDED", "SYSTEMCLOCK", "ZEROBASED"] = Field(alias="Source")
    sync_threshold: Optional[int] = Field(default=None, alias="SyncThreshold")


class InputLossFailoverSettingsModel(BaseModel):
    input_loss_threshold_msec: Optional[int] = Field(
        default=None, alias="InputLossThresholdMsec"
    )


class VideoBlackFailoverSettingsModel(BaseModel):
    black_detect_threshold: Optional[float] = Field(
        default=None, alias="BlackDetectThreshold"
    )
    video_black_threshold_msec: Optional[int] = Field(
        default=None, alias="VideoBlackThresholdMsec"
    )


class FecOutputSettingsModel(BaseModel):
    column_depth: Optional[int] = Field(default=None, alias="ColumnDepth")
    include_fec: Optional[Literal["COLUMN", "COLUMN_AND_ROW"]] = Field(
        default=None, alias="IncludeFec"
    )
    row_length: Optional[int] = Field(default=None, alias="RowLength")


class FixedModeScheduleActionStartSettingsModel(BaseModel):
    time: str = Field(alias="Time")


class Fmp4HlsSettingsModel(BaseModel):
    audio_rendition_sets: Optional[str] = Field(
        default=None, alias="AudioRenditionSets"
    )
    nielsen_id3_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="NielsenId3Behavior"
    )
    timed_metadata_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadataBehavior"
    )


class FollowModeScheduleActionStartSettingsModel(BaseModel):
    follow_point: Literal["END", "START"] = Field(alias="FollowPoint")
    reference_action_name: str = Field(alias="ReferenceActionName")


class FrameCaptureS3SettingsModel(BaseModel):
    canned_acl: Optional[
        Literal[
            "AUTHENTICATED_READ",
            "BUCKET_OWNER_FULL_CONTROL",
            "BUCKET_OWNER_READ",
            "PUBLIC_READ",
        ]
    ] = Field(default=None, alias="CannedAcl")


class FrameCaptureOutputSettingsModel(BaseModel):
    name_modifier: Optional[str] = Field(default=None, alias="NameModifier")


class TimecodeBurninSettingsModel(BaseModel):
    font_size: Literal["EXTRA_SMALL_10", "LARGE_48", "MEDIUM_32", "SMALL_16"] = Field(
        alias="FontSize"
    )
    position: Literal[
        "BOTTOM_CENTER",
        "BOTTOM_LEFT",
        "BOTTOM_RIGHT",
        "MIDDLE_CENTER",
        "MIDDLE_LEFT",
        "MIDDLE_RIGHT",
        "TOP_CENTER",
        "TOP_LEFT",
        "TOP_RIGHT",
    ] = Field(alias="Position")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class H264ColorSpaceSettingsModel(BaseModel):
    color_space_passthrough_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="ColorSpacePassthroughSettings"
    )
    rec601_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Rec601Settings"
    )
    rec709_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Rec709Settings"
    )


class TemporalFilterSettingsModel(BaseModel):
    post_filter_sharpening: Optional[Literal["AUTO", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="PostFilterSharpening"
    )
    strength: Optional[
        Literal[
            "AUTO",
            "STRENGTH_1",
            "STRENGTH_10",
            "STRENGTH_11",
            "STRENGTH_12",
            "STRENGTH_13",
            "STRENGTH_14",
            "STRENGTH_15",
            "STRENGTH_16",
            "STRENGTH_2",
            "STRENGTH_3",
            "STRENGTH_4",
            "STRENGTH_5",
            "STRENGTH_6",
            "STRENGTH_7",
            "STRENGTH_8",
            "STRENGTH_9",
        ]
    ] = Field(default=None, alias="Strength")


class Hdr10SettingsModel(BaseModel):
    max_cll: Optional[int] = Field(default=None, alias="MaxCll")
    max_fall: Optional[int] = Field(default=None, alias="MaxFall")


class HlsAkamaiSettingsModel(BaseModel):
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    filecache_duration: Optional[int] = Field(default=None, alias="FilecacheDuration")
    http_transfer_mode: Optional[Literal["CHUNKED", "NON_CHUNKED"]] = Field(
        default=None, alias="HttpTransferMode"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")
    salt: Optional[str] = Field(default=None, alias="Salt")
    token: Optional[str] = Field(default=None, alias="Token")


class HlsBasicPutSettingsModel(BaseModel):
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    filecache_duration: Optional[int] = Field(default=None, alias="FilecacheDuration")
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")


class HlsMediaStoreSettingsModel(BaseModel):
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    filecache_duration: Optional[int] = Field(default=None, alias="FilecacheDuration")
    media_store_storage_class: Optional[Literal["TEMPORAL"]] = Field(
        default=None, alias="MediaStoreStorageClass"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")


class HlsS3SettingsModel(BaseModel):
    canned_acl: Optional[
        Literal[
            "AUTHENTICATED_READ",
            "BUCKET_OWNER_FULL_CONTROL",
            "BUCKET_OWNER_READ",
            "PUBLIC_READ",
        ]
    ] = Field(default=None, alias="CannedAcl")


class HlsWebdavSettingsModel(BaseModel):
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    filecache_duration: Optional[int] = Field(default=None, alias="FilecacheDuration")
    http_transfer_mode: Optional[Literal["CHUNKED", "NON_CHUNKED"]] = Field(
        default=None, alias="HttpTransferMode"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")


class HlsId3SegmentTaggingScheduleActionSettingsModel(BaseModel):
    tag: str = Field(alias="Tag")


class HlsInputSettingsModel(BaseModel):
    bandwidth: Optional[int] = Field(default=None, alias="Bandwidth")
    buffer_segments: Optional[int] = Field(default=None, alias="BufferSegments")
    retries: Optional[int] = Field(default=None, alias="Retries")
    retry_interval: Optional[int] = Field(default=None, alias="RetryInterval")
    scte35_source: Optional[Literal["MANIFEST", "SEGMENTS"]] = Field(
        default=None, alias="Scte35Source"
    )


class HlsTimedMetadataScheduleActionSettingsModel(BaseModel):
    id3: str = Field(alias="Id3")


class StartTimecodeModel(BaseModel):
    timecode: Optional[str] = Field(default=None, alias="Timecode")


class StopTimecodeModel(BaseModel):
    last_frame_clipping_behavior: Optional[
        Literal["EXCLUDE_LAST_FRAME", "INCLUDE_LAST_FRAME"]
    ] = Field(default=None, alias="LastFrameClippingBehavior")
    timecode: Optional[str] = Field(default=None, alias="Timecode")


class InputDestinationVpcModel(BaseModel):
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )


class InputDeviceConfigurableSettingsModel(BaseModel):
    configured_input: Optional[Literal["AUTO", "HDMI", "SDI"]] = Field(
        default=None, alias="ConfiguredInput"
    )
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    latency_ms: Optional[int] = Field(default=None, alias="LatencyMs")


class InputDeviceRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class ListChannelsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInputDeviceTransfersRequestModel(BaseModel):
    transfer_type: str = Field(alias="TransferType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TransferringInputDeviceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    message: Optional[str] = Field(default=None, alias="Message")
    target_customer_id: Optional[str] = Field(default=None, alias="TargetCustomerId")
    transfer_type: Optional[Literal["INCOMING", "OUTGOING"]] = Field(
        default=None, alias="TransferType"
    )


class ListInputDevicesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInputSecurityGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInputsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMultiplexProgramsRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MultiplexProgramSummaryModel(BaseModel):
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    program_name: Optional[str] = Field(default=None, alias="ProgramName")


class ListMultiplexesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOfferingsRequestModel(BaseModel):
    channel_class: Optional[str] = Field(default=None, alias="ChannelClass")
    channel_configuration: Optional[str] = Field(
        default=None, alias="ChannelConfiguration"
    )
    codec: Optional[str] = Field(default=None, alias="Codec")
    duration: Optional[str] = Field(default=None, alias="Duration")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    maximum_bitrate: Optional[str] = Field(default=None, alias="MaximumBitrate")
    maximum_framerate: Optional[str] = Field(default=None, alias="MaximumFramerate")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    special_feature: Optional[str] = Field(default=None, alias="SpecialFeature")
    video_quality: Optional[str] = Field(default=None, alias="VideoQuality")


class ListReservationsRequestModel(BaseModel):
    channel_class: Optional[str] = Field(default=None, alias="ChannelClass")
    codec: Optional[str] = Field(default=None, alias="Codec")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    maximum_bitrate: Optional[str] = Field(default=None, alias="MaximumBitrate")
    maximum_framerate: Optional[str] = Field(default=None, alias="MaximumFramerate")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    special_feature: Optional[str] = Field(default=None, alias="SpecialFeature")
    video_quality: Optional[str] = Field(default=None, alias="VideoQuality")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class M3u8SettingsModel(BaseModel):
    audio_frames_per_pes: Optional[int] = Field(default=None, alias="AudioFramesPerPes")
    audio_pids: Optional[str] = Field(default=None, alias="AudioPids")
    ecm_pid: Optional[str] = Field(default=None, alias="EcmPid")
    nielsen_id3_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="NielsenId3Behavior"
    )
    pat_interval: Optional[int] = Field(default=None, alias="PatInterval")
    pcr_control: Optional[
        Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
    ] = Field(default=None, alias="PcrControl")
    pcr_period: Optional[int] = Field(default=None, alias="PcrPeriod")
    pcr_pid: Optional[str] = Field(default=None, alias="PcrPid")
    pmt_interval: Optional[int] = Field(default=None, alias="PmtInterval")
    pmt_pid: Optional[str] = Field(default=None, alias="PmtPid")
    program_num: Optional[int] = Field(default=None, alias="ProgramNum")
    scte35_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Behavior"
    )
    scte35_pid: Optional[str] = Field(default=None, alias="Scte35Pid")
    timed_metadata_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadataBehavior"
    )
    timed_metadata_pid: Optional[str] = Field(default=None, alias="TimedMetadataPid")
    transport_stream_id: Optional[int] = Field(default=None, alias="TransportStreamId")
    video_pid: Optional[str] = Field(default=None, alias="VideoPid")


class MaintenanceUpdateSettingsModel(BaseModel):
    maintenance_day: Optional[
        Literal[
            "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
        ]
    ] = Field(default=None, alias="MaintenanceDay")
    maintenance_scheduled_date: Optional[str] = Field(
        default=None, alias="MaintenanceScheduledDate"
    )
    maintenance_start_time: Optional[str] = Field(
        default=None, alias="MaintenanceStartTime"
    )


class MediaPackageOutputDestinationSettingsModel(BaseModel):
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")


class MotionGraphicsActivateScheduleActionSettingsModel(BaseModel):
    duration: Optional[int] = Field(default=None, alias="Duration")
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")


class MotionGraphicsSettingsModel(BaseModel):
    html_motion_graphics_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="HtmlMotionGraphicsSettings"
    )


class MsSmoothOutputSettingsModel(BaseModel):
    h265_packaging_type: Optional[Literal["HEV1", "HVC1"]] = Field(
        default=None, alias="H265PackagingType"
    )
    name_modifier: Optional[str] = Field(default=None, alias="NameModifier")


class MultiplexMediaConnectOutputDestinationSettingsModel(BaseModel):
    entitlement_arn: Optional[str] = Field(default=None, alias="EntitlementArn")


class MultiplexProgramChannelDestinationSettingsModel(BaseModel):
    multiplex_id: Optional[str] = Field(default=None, alias="MultiplexId")
    program_name: Optional[str] = Field(default=None, alias="ProgramName")


class MultiplexProgramServiceDescriptorModel(BaseModel):
    provider_name: str = Field(alias="ProviderName")
    service_name: str = Field(alias="ServiceName")


class MultiplexSettingsSummaryModel(BaseModel):
    transport_stream_bitrate: Optional[int] = Field(
        default=None, alias="TransportStreamBitrate"
    )


class MultiplexStatmuxVideoSettingsModel(BaseModel):
    maximum_bitrate: Optional[int] = Field(default=None, alias="MaximumBitrate")
    minimum_bitrate: Optional[int] = Field(default=None, alias="MinimumBitrate")
    priority: Optional[int] = Field(default=None, alias="Priority")


class NielsenCBETModel(BaseModel):
    cbet_check_digit_string: str = Field(alias="CbetCheckDigitString")
    cbet_stepaside: Literal["DISABLED", "ENABLED"] = Field(alias="CbetStepaside")
    csid: str = Field(alias="Csid")


class NielsenNaesIiNwModel(BaseModel):
    check_digit_string: str = Field(alias="CheckDigitString")
    sid: float = Field(alias="Sid")


class OutputDestinationSettingsModel(BaseModel):
    password_param: Optional[str] = Field(default=None, alias="PasswordParam")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")


class RtmpGroupSettingsModel(BaseModel):
    ad_markers: Optional[Sequence[Literal["ON_CUE_POINT_SCTE35"]]] = Field(
        default=None, alias="AdMarkers"
    )
    authentication_scheme: Optional[Literal["AKAMAI", "COMMON"]] = Field(
        default=None, alias="AuthenticationScheme"
    )
    cache_full_behavior: Optional[
        Literal["DISCONNECT_IMMEDIATELY", "WAIT_FOR_SERVER"]
    ] = Field(default=None, alias="CacheFullBehavior")
    cache_length: Optional[int] = Field(default=None, alias="CacheLength")
    caption_data: Optional[
        Literal["ALL", "FIELD1_608", "FIELD1_AND_FIELD2_608"]
    ] = Field(default=None, alias="CaptionData")
    input_loss_action: Optional[Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]] = Field(
        default=None, alias="InputLossAction"
    )
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")


class UdpGroupSettingsModel(BaseModel):
    input_loss_action: Optional[
        Literal["DROP_PROGRAM", "DROP_TS", "EMIT_PROGRAM"]
    ] = Field(default=None, alias="InputLossAction")
    timed_metadata_id3_frame: Optional[Literal["NONE", "PRIV", "TDRL"]] = Field(
        default=None, alias="TimedMetadataId3Frame"
    )
    timed_metadata_id3_period: Optional[int] = Field(
        default=None, alias="TimedMetadataId3Period"
    )


class PipelinePauseStateSettingsModel(BaseModel):
    pipeline_id: Literal["PIPELINE_0", "PIPELINE_1"] = Field(alias="PipelineId")


class RebootInputDeviceRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")
    force: Optional[Literal["NO", "YES"]] = Field(default=None, alias="Force")


class RejectInputDeviceTransferRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")


class Scte35InputScheduleActionSettingsModel(BaseModel):
    mode: Literal["FIXED", "FOLLOW_ACTIVE"] = Field(alias="Mode")
    input_attachment_name_reference: Optional[str] = Field(
        default=None, alias="InputAttachmentNameReference"
    )


class Scte35ReturnToNetworkScheduleActionSettingsModel(BaseModel):
    splice_event_id: int = Field(alias="SpliceEventId")


class Scte35SpliceInsertScheduleActionSettingsModel(BaseModel):
    splice_event_id: int = Field(alias="SpliceEventId")
    duration: Optional[int] = Field(default=None, alias="Duration")


class StaticImageDeactivateScheduleActionSettingsModel(BaseModel):
    fade_out: Optional[int] = Field(default=None, alias="FadeOut")
    layer: Optional[int] = Field(default=None, alias="Layer")


class Scte35DeliveryRestrictionsModel(BaseModel):
    archive_allowed_flag: Literal["ARCHIVE_ALLOWED", "ARCHIVE_NOT_ALLOWED"] = Field(
        alias="ArchiveAllowedFlag"
    )
    device_restrictions: Literal[
        "NONE", "RESTRICT_GROUP0", "RESTRICT_GROUP1", "RESTRICT_GROUP2"
    ] = Field(alias="DeviceRestrictions")
    no_regional_blackout_flag: Literal[
        "NO_REGIONAL_BLACKOUT", "REGIONAL_BLACKOUT"
    ] = Field(alias="NoRegionalBlackoutFlag")
    web_delivery_allowed_flag: Literal[
        "WEB_DELIVERY_ALLOWED", "WEB_DELIVERY_NOT_ALLOWED"
    ] = Field(alias="WebDeliveryAllowedFlag")


class StartChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")


class StartInputDeviceMaintenanceWindowRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")


class StartMultiplexRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")


class StopChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")


class StopMultiplexRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")


class TransferInputDeviceRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")
    target_customer_id: Optional[str] = Field(default=None, alias="TargetCustomerId")
    target_region: Optional[str] = Field(default=None, alias="TargetRegion")
    transfer_message: Optional[str] = Field(default=None, alias="TransferMessage")


class VideoSelectorPidModel(BaseModel):
    pid: Optional[int] = Field(default=None, alias="Pid")


class VideoSelectorProgramIdModel(BaseModel):
    program_id: Optional[int] = Field(default=None, alias="ProgramId")


class ArchiveCdnSettingsModel(BaseModel):
    archive_s3_settings: Optional[ArchiveS3SettingsModel] = Field(
        default=None, alias="ArchiveS3Settings"
    )


class MediaPackageGroupSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")


class MsSmoothGroupSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")
    acquisition_point_id: Optional[str] = Field(
        default=None, alias="AcquisitionPointId"
    )
    audio_only_timecode_control: Optional[
        Literal["PASSTHROUGH", "USE_CONFIGURED_CLOCK"]
    ] = Field(default=None, alias="AudioOnlyTimecodeControl")
    certificate_mode: Optional[Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]] = Field(
        default=None, alias="CertificateMode"
    )
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    event_id: Optional[str] = Field(default=None, alias="EventId")
    event_id_mode: Optional[
        Literal["NO_EVENT_ID", "USE_CONFIGURED", "USE_TIMESTAMP"]
    ] = Field(default=None, alias="EventIdMode")
    event_stop_behavior: Optional[Literal["NONE", "SEND_EOS"]] = Field(
        default=None, alias="EventStopBehavior"
    )
    filecache_duration: Optional[int] = Field(default=None, alias="FilecacheDuration")
    fragment_length: Optional[int] = Field(default=None, alias="FragmentLength")
    input_loss_action: Optional[Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]] = Field(
        default=None, alias="InputLossAction"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    restart_delay: Optional[int] = Field(default=None, alias="RestartDelay")
    segmentation_mode: Optional[
        Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
    ] = Field(default=None, alias="SegmentationMode")
    send_delay_ms: Optional[int] = Field(default=None, alias="SendDelayMs")
    sparse_track_type: Optional[
        Literal["NONE", "SCTE_35", "SCTE_35_WITHOUT_SEGMENTATION"]
    ] = Field(default=None, alias="SparseTrackType")
    stream_manifest_behavior: Optional[Literal["DO_NOT_SEND", "SEND"]] = Field(
        default=None, alias="StreamManifestBehavior"
    )
    timestamp_offset: Optional[str] = Field(default=None, alias="TimestampOffset")
    timestamp_offset_mode: Optional[
        Literal["USE_CONFIGURED_OFFSET", "USE_EVENT_START_DATE"]
    ] = Field(default=None, alias="TimestampOffsetMode")


class MultiplexOutputSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")


class RtmpOutputSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")
    certificate_mode: Optional[Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]] = Field(
        default=None, alias="CertificateMode"
    )
    connection_retry_interval: Optional[int] = Field(
        default=None, alias="ConnectionRetryInterval"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")


class AudioChannelMappingModel(BaseModel):
    input_channel_levels: Sequence[InputChannelLevelModel] = Field(
        alias="InputChannelLevels"
    )
    output_channel: int = Field(alias="OutputChannel")


class AudioCodecSettingsModel(BaseModel):
    aac_settings: Optional[AacSettingsModel] = Field(default=None, alias="AacSettings")
    ac3_settings: Optional[Ac3SettingsModel] = Field(default=None, alias="Ac3Settings")
    eac3_atmos_settings: Optional[Eac3AtmosSettingsModel] = Field(
        default=None, alias="Eac3AtmosSettings"
    )
    eac3_settings: Optional[Eac3SettingsModel] = Field(
        default=None, alias="Eac3Settings"
    )
    mp2_settings: Optional[Mp2SettingsModel] = Field(default=None, alias="Mp2Settings")
    pass_through_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="PassThroughSettings"
    )
    wav_settings: Optional[WavSettingsModel] = Field(default=None, alias="WavSettings")


class AudioOnlyHlsSettingsModel(BaseModel):
    audio_group_id: Optional[str] = Field(default=None, alias="AudioGroupId")
    audio_only_image: Optional[InputLocationModel] = Field(
        default=None, alias="AudioOnlyImage"
    )
    audio_track_type: Optional[
        Literal[
            "ALTERNATE_AUDIO_AUTO_SELECT",
            "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
            "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
            "AUDIO_ONLY_VARIANT_STREAM",
        ]
    ] = Field(default=None, alias="AudioTrackType")
    segment_type: Optional[Literal["AAC", "FMP4"]] = Field(
        default=None, alias="SegmentType"
    )


class AvailBlankingModel(BaseModel):
    avail_blanking_image: Optional[InputLocationModel] = Field(
        default=None, alias="AvailBlankingImage"
    )
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class BlackoutSlateModel(BaseModel):
    blackout_slate_image: Optional[InputLocationModel] = Field(
        default=None, alias="BlackoutSlateImage"
    )
    network_end_blackout: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="NetworkEndBlackout"
    )
    network_end_blackout_image: Optional[InputLocationModel] = Field(
        default=None, alias="NetworkEndBlackoutImage"
    )
    network_id: Optional[str] = Field(default=None, alias="NetworkId")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class BurnInDestinationSettingsModel(BaseModel):
    alignment: Optional[Literal["CENTERED", "LEFT", "SMART"]] = Field(
        default=None, alias="Alignment"
    )
    background_color: Optional[Literal["BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="BackgroundColor"
    )
    background_opacity: Optional[int] = Field(default=None, alias="BackgroundOpacity")
    font: Optional[InputLocationModel] = Field(default=None, alias="Font")
    font_color: Optional[
        Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="FontColor")
    font_opacity: Optional[int] = Field(default=None, alias="FontOpacity")
    font_resolution: Optional[int] = Field(default=None, alias="FontResolution")
    font_size: Optional[str] = Field(default=None, alias="FontSize")
    outline_color: Optional[
        Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="OutlineColor")
    outline_size: Optional[int] = Field(default=None, alias="OutlineSize")
    shadow_color: Optional[Literal["BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="ShadowColor"
    )
    shadow_opacity: Optional[int] = Field(default=None, alias="ShadowOpacity")
    shadow_xoffset: Optional[int] = Field(default=None, alias="ShadowXOffset")
    shadow_yoffset: Optional[int] = Field(default=None, alias="ShadowYOffset")
    teletext_grid_control: Optional[Literal["FIXED", "SCALED"]] = Field(
        default=None, alias="TeletextGridControl"
    )
    xposition: Optional[int] = Field(default=None, alias="XPosition")
    yposition: Optional[int] = Field(default=None, alias="YPosition")


class DvbSubDestinationSettingsModel(BaseModel):
    alignment: Optional[Literal["CENTERED", "LEFT", "SMART"]] = Field(
        default=None, alias="Alignment"
    )
    background_color: Optional[Literal["BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="BackgroundColor"
    )
    background_opacity: Optional[int] = Field(default=None, alias="BackgroundOpacity")
    font: Optional[InputLocationModel] = Field(default=None, alias="Font")
    font_color: Optional[
        Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="FontColor")
    font_opacity: Optional[int] = Field(default=None, alias="FontOpacity")
    font_resolution: Optional[int] = Field(default=None, alias="FontResolution")
    font_size: Optional[str] = Field(default=None, alias="FontSize")
    outline_color: Optional[
        Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="OutlineColor")
    outline_size: Optional[int] = Field(default=None, alias="OutlineSize")
    shadow_color: Optional[Literal["BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="ShadowColor"
    )
    shadow_opacity: Optional[int] = Field(default=None, alias="ShadowOpacity")
    shadow_xoffset: Optional[int] = Field(default=None, alias="ShadowXOffset")
    shadow_yoffset: Optional[int] = Field(default=None, alias="ShadowYOffset")
    teletext_grid_control: Optional[Literal["FIXED", "SCALED"]] = Field(
        default=None, alias="TeletextGridControl"
    )
    xposition: Optional[int] = Field(default=None, alias="XPosition")
    yposition: Optional[int] = Field(default=None, alias="YPosition")


class InputLossBehaviorModel(BaseModel):
    black_frame_msec: Optional[int] = Field(default=None, alias="BlackFrameMsec")
    input_loss_image_color: Optional[str] = Field(
        default=None, alias="InputLossImageColor"
    )
    input_loss_image_slate: Optional[InputLocationModel] = Field(
        default=None, alias="InputLossImageSlate"
    )
    input_loss_image_type: Optional[Literal["COLOR", "SLATE"]] = Field(
        default=None, alias="InputLossImageType"
    )
    repeat_frame_msec: Optional[int] = Field(default=None, alias="RepeatFrameMsec")


class StaticImageActivateScheduleActionSettingsModel(BaseModel):
    image: InputLocationModel = Field(alias="Image")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fade_in: Optional[int] = Field(default=None, alias="FadeIn")
    fade_out: Optional[int] = Field(default=None, alias="FadeOut")
    height: Optional[int] = Field(default=None, alias="Height")
    image_x: Optional[int] = Field(default=None, alias="ImageX")
    image_y: Optional[int] = Field(default=None, alias="ImageY")
    layer: Optional[int] = Field(default=None, alias="Layer")
    opacity: Optional[int] = Field(default=None, alias="Opacity")
    width: Optional[int] = Field(default=None, alias="Width")


class StaticKeySettingsModel(BaseModel):
    static_key_value: str = Field(alias="StaticKeyValue")
    key_provider_server: Optional[InputLocationModel] = Field(
        default=None, alias="KeyProviderServer"
    )


class AudioTrackSelectionModel(BaseModel):
    tracks: Sequence[AudioTrackModel] = Field(alias="Tracks")
    dolby_edecode: Optional[AudioDolbyEDecodeModel] = Field(
        default=None, alias="DolbyEDecode"
    )


class AvailSettingsModel(BaseModel):
    esam: Optional[EsamModel] = Field(default=None, alias="Esam")
    scte35_splice_insert: Optional[Scte35SpliceInsertModel] = Field(
        default=None, alias="Scte35SpliceInsert"
    )
    scte35_time_signal_apos: Optional[Scte35TimeSignalAposModel] = Field(
        default=None, alias="Scte35TimeSignalApos"
    )


class BatchDeleteResponseModel(BaseModel):
    failed: List[BatchFailedResultModelModel] = Field(alias="Failed")
    successful: List[BatchSuccessfulResultModelModel] = Field(alias="Successful")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchStartResponseModel(BaseModel):
    failed: List[BatchFailedResultModelModel] = Field(alias="Failed")
    successful: List[BatchSuccessfulResultModelModel] = Field(alias="Successful")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchStopResponseModel(BaseModel):
    failed: List[BatchFailedResultModelModel] = Field(alias="Failed")
    successful: List[BatchSuccessfulResultModelModel] = Field(alias="Successful")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInputDeviceThumbnailResponseModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    content_type: Literal["image/jpeg"] = Field(alias="ContentType")
    content_length: int = Field(alias="ContentLength")
    etag: str = Field(alias="ETag")
    last_modified: datetime = Field(alias="LastModified")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TeletextSourceSettingsModel(BaseModel):
    output_rectangle: Optional[CaptionRectangleModel] = Field(
        default=None, alias="OutputRectangle"
    )
    page_number: Optional[str] = Field(default=None, alias="PageNumber")


class CreateInputRequestModel(BaseModel):
    destinations: Optional[Sequence[InputDestinationRequestModel]] = Field(
        default=None, alias="Destinations"
    )
    input_devices: Optional[Sequence[InputDeviceSettingsModel]] = Field(
        default=None, alias="InputDevices"
    )
    input_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="InputSecurityGroups"
    )
    media_connect_flows: Optional[Sequence[MediaConnectFlowRequestModel]] = Field(
        default=None, alias="MediaConnectFlows"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    sources: Optional[Sequence[InputSourceRequestModel]] = Field(
        default=None, alias="Sources"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    type: Optional[
        Literal[
            "AWS_CDI",
            "INPUT_DEVICE",
            "MEDIACONNECT",
            "MP4_FILE",
            "RTMP_PULL",
            "RTMP_PUSH",
            "RTP_PUSH",
            "TS_FILE",
            "UDP_PUSH",
            "URL_PULL",
        ]
    ] = Field(default=None, alias="Type")
    vpc: Optional[InputVpcRequestModel] = Field(default=None, alias="Vpc")


class CreateInputSecurityGroupRequestModel(BaseModel):
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    whitelist_rules: Optional[Sequence[InputWhitelistRuleCidrModel]] = Field(
        default=None, alias="WhitelistRules"
    )


class UpdateInputSecurityGroupRequestModel(BaseModel):
    input_security_group_id: str = Field(alias="InputSecurityGroupId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    whitelist_rules: Optional[Sequence[InputWhitelistRuleCidrModel]] = Field(
        default=None, alias="WhitelistRules"
    )


class CreateMultiplexRequestModel(BaseModel):
    availability_zones: Sequence[str] = Field(alias="AvailabilityZones")
    multiplex_settings: MultiplexSettingsModel = Field(alias="MultiplexSettings")
    name: str = Field(alias="Name")
    request_id: str = Field(alias="RequestId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateMultiplexRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    multiplex_settings: Optional[MultiplexSettingsModel] = Field(
        default=None, alias="MultiplexSettings"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class PurchaseOfferingRequestModel(BaseModel):
    count: int = Field(alias="Count")
    offering_id: str = Field(alias="OfferingId")
    name: Optional[str] = Field(default=None, alias="Name")
    renewal_settings: Optional[RenewalSettingsModel] = Field(
        default=None, alias="RenewalSettings"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    start: Optional[str] = Field(default=None, alias="Start")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateReservationRequestModel(BaseModel):
    reservation_id: str = Field(alias="ReservationId")
    name: Optional[str] = Field(default=None, alias="Name")
    renewal_settings: Optional[RenewalSettingsModel] = Field(
        default=None, alias="RenewalSettings"
    )


class DeleteReservationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    count: int = Field(alias="Count")
    currency_code: str = Field(alias="CurrencyCode")
    duration: int = Field(alias="Duration")
    duration_units: Literal["MONTHS"] = Field(alias="DurationUnits")
    end: str = Field(alias="End")
    fixed_price: float = Field(alias="FixedPrice")
    name: str = Field(alias="Name")
    offering_description: str = Field(alias="OfferingDescription")
    offering_id: str = Field(alias="OfferingId")
    offering_type: Literal["NO_UPFRONT"] = Field(alias="OfferingType")
    region: str = Field(alias="Region")
    renewal_settings: RenewalSettingsModel = Field(alias="RenewalSettings")
    reservation_id: str = Field(alias="ReservationId")
    resource_specification: ReservationResourceSpecificationModel = Field(
        alias="ResourceSpecification"
    )
    start: str = Field(alias="Start")
    state: Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    usage_price: float = Field(alias="UsagePrice")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOfferingResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    currency_code: str = Field(alias="CurrencyCode")
    duration: int = Field(alias="Duration")
    duration_units: Literal["MONTHS"] = Field(alias="DurationUnits")
    fixed_price: float = Field(alias="FixedPrice")
    offering_description: str = Field(alias="OfferingDescription")
    offering_id: str = Field(alias="OfferingId")
    offering_type: Literal["NO_UPFRONT"] = Field(alias="OfferingType")
    region: str = Field(alias="Region")
    resource_specification: ReservationResourceSpecificationModel = Field(
        alias="ResourceSpecification"
    )
    usage_price: float = Field(alias="UsagePrice")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    count: int = Field(alias="Count")
    currency_code: str = Field(alias="CurrencyCode")
    duration: int = Field(alias="Duration")
    duration_units: Literal["MONTHS"] = Field(alias="DurationUnits")
    end: str = Field(alias="End")
    fixed_price: float = Field(alias="FixedPrice")
    name: str = Field(alias="Name")
    offering_description: str = Field(alias="OfferingDescription")
    offering_id: str = Field(alias="OfferingId")
    offering_type: Literal["NO_UPFRONT"] = Field(alias="OfferingType")
    region: str = Field(alias="Region")
    renewal_settings: RenewalSettingsModel = Field(alias="RenewalSettings")
    reservation_id: str = Field(alias="ReservationId")
    resource_specification: ReservationResourceSpecificationModel = Field(
        alias="ResourceSpecification"
    )
    start: str = Field(alias="Start")
    state: Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    usage_price: float = Field(alias="UsagePrice")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OfferingModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    duration: Optional[int] = Field(default=None, alias="Duration")
    duration_units: Optional[Literal["MONTHS"]] = Field(
        default=None, alias="DurationUnits"
    )
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    offering_description: Optional[str] = Field(
        default=None, alias="OfferingDescription"
    )
    offering_id: Optional[str] = Field(default=None, alias="OfferingId")
    offering_type: Optional[Literal["NO_UPFRONT"]] = Field(
        default=None, alias="OfferingType"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_specification: Optional[ReservationResourceSpecificationModel] = Field(
        default=None, alias="ResourceSpecification"
    )
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")


class ReservationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    count: Optional[int] = Field(default=None, alias="Count")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    duration: Optional[int] = Field(default=None, alias="Duration")
    duration_units: Optional[Literal["MONTHS"]] = Field(
        default=None, alias="DurationUnits"
    )
    end: Optional[str] = Field(default=None, alias="End")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    name: Optional[str] = Field(default=None, alias="Name")
    offering_description: Optional[str] = Field(
        default=None, alias="OfferingDescription"
    )
    offering_id: Optional[str] = Field(default=None, alias="OfferingId")
    offering_type: Optional[Literal["NO_UPFRONT"]] = Field(
        default=None, alias="OfferingType"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    renewal_settings: Optional[RenewalSettingsModel] = Field(
        default=None, alias="RenewalSettings"
    )
    reservation_id: Optional[str] = Field(default=None, alias="ReservationId")
    resource_specification: Optional[ReservationResourceSpecificationModel] = Field(
        default=None, alias="ResourceSpecification"
    )
    start: Optional[str] = Field(default=None, alias="Start")
    state: Optional[Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")


class DescribeChannelRequestChannelCreatedWaitModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeChannelRequestChannelDeletedWaitModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeChannelRequestChannelRunningWaitModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeChannelRequestChannelStoppedWaitModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInputRequestInputAttachedWaitModel(BaseModel):
    input_id: str = Field(alias="InputId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInputRequestInputDeletedWaitModel(BaseModel):
    input_id: str = Field(alias="InputId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInputRequestInputDetachedWaitModel(BaseModel):
    input_id: str = Field(alias="InputId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeMultiplexRequestMultiplexCreatedWaitModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeMultiplexRequestMultiplexDeletedWaitModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeMultiplexRequestMultiplexRunningWaitModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeMultiplexRequestMultiplexStoppedWaitModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInputDeviceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    connection_state: Literal["CONNECTED", "DISCONNECTED"] = Field(
        alias="ConnectionState"
    )
    device_settings_sync_state: Literal["SYNCED", "SYNCING"] = Field(
        alias="DeviceSettingsSyncState"
    )
    device_update_status: Literal["NOT_UP_TO_DATE", "UPDATING", "UP_TO_DATE"] = Field(
        alias="DeviceUpdateStatus"
    )
    hd_device_settings: InputDeviceHdSettingsModel = Field(alias="HdDeviceSettings")
    id: str = Field(alias="Id")
    mac_address: str = Field(alias="MacAddress")
    name: str = Field(alias="Name")
    network_settings: InputDeviceNetworkSettingsModel = Field(alias="NetworkSettings")
    serial_number: str = Field(alias="SerialNumber")
    type: Literal["HD", "UHD"] = Field(alias="Type")
    uhd_device_settings: InputDeviceUhdSettingsModel = Field(alias="UhdDeviceSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputDeviceSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    connection_state: Optional[Literal["CONNECTED", "DISCONNECTED"]] = Field(
        default=None, alias="ConnectionState"
    )
    device_settings_sync_state: Optional[Literal["SYNCED", "SYNCING"]] = Field(
        default=None, alias="DeviceSettingsSyncState"
    )
    device_update_status: Optional[
        Literal["NOT_UP_TO_DATE", "UPDATING", "UP_TO_DATE"]
    ] = Field(default=None, alias="DeviceUpdateStatus")
    hd_device_settings: Optional[InputDeviceHdSettingsModel] = Field(
        default=None, alias="HdDeviceSettings"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    mac_address: Optional[str] = Field(default=None, alias="MacAddress")
    name: Optional[str] = Field(default=None, alias="Name")
    network_settings: Optional[InputDeviceNetworkSettingsModel] = Field(
        default=None, alias="NetworkSettings"
    )
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    type: Optional[Literal["HD", "UHD"]] = Field(default=None, alias="Type")
    uhd_device_settings: Optional[InputDeviceUhdSettingsModel] = Field(
        default=None, alias="UhdDeviceSettings"
    )


class UpdateInputDeviceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    connection_state: Literal["CONNECTED", "DISCONNECTED"] = Field(
        alias="ConnectionState"
    )
    device_settings_sync_state: Literal["SYNCED", "SYNCING"] = Field(
        alias="DeviceSettingsSyncState"
    )
    device_update_status: Literal["NOT_UP_TO_DATE", "UPDATING", "UP_TO_DATE"] = Field(
        alias="DeviceUpdateStatus"
    )
    hd_device_settings: InputDeviceHdSettingsModel = Field(alias="HdDeviceSettings")
    id: str = Field(alias="Id")
    mac_address: str = Field(alias="MacAddress")
    name: str = Field(alias="Name")
    network_settings: InputDeviceNetworkSettingsModel = Field(alias="NetworkSettings")
    serial_number: str = Field(alias="SerialNumber")
    type: Literal["HD", "UHD"] = Field(alias="Type")
    uhd_device_settings: InputDeviceUhdSettingsModel = Field(alias="UhdDeviceSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInputSecurityGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    inputs: List[str] = Field(alias="Inputs")
    state: Literal["DELETED", "IDLE", "IN_USE", "UPDATING"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    whitelist_rules: List[InputWhitelistRuleModel] = Field(alias="WhitelistRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputSecurityGroupModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    inputs: Optional[List[str]] = Field(default=None, alias="Inputs")
    state: Optional[Literal["DELETED", "IDLE", "IN_USE", "UPDATING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    whitelist_rules: Optional[List[InputWhitelistRuleModel]] = Field(
        default=None, alias="WhitelistRules"
    )


class DescribeScheduleRequestDescribeSchedulePaginateModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListChannelsRequestListChannelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInputDeviceTransfersRequestListInputDeviceTransfersPaginateModel(BaseModel):
    transfer_type: str = Field(alias="TransferType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInputDevicesRequestListInputDevicesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInputSecurityGroupsRequestListInputSecurityGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInputsRequestListInputsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMultiplexProgramsRequestListMultiplexProgramsPaginateModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMultiplexesRequestListMultiplexesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOfferingsRequestListOfferingsPaginateModel(BaseModel):
    channel_class: Optional[str] = Field(default=None, alias="ChannelClass")
    channel_configuration: Optional[str] = Field(
        default=None, alias="ChannelConfiguration"
    )
    codec: Optional[str] = Field(default=None, alias="Codec")
    duration: Optional[str] = Field(default=None, alias="Duration")
    maximum_bitrate: Optional[str] = Field(default=None, alias="MaximumBitrate")
    maximum_framerate: Optional[str] = Field(default=None, alias="MaximumFramerate")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    special_feature: Optional[str] = Field(default=None, alias="SpecialFeature")
    video_quality: Optional[str] = Field(default=None, alias="VideoQuality")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReservationsRequestListReservationsPaginateModel(BaseModel):
    channel_class: Optional[str] = Field(default=None, alias="ChannelClass")
    codec: Optional[str] = Field(default=None, alias="Codec")
    maximum_bitrate: Optional[str] = Field(default=None, alias="MaximumBitrate")
    maximum_framerate: Optional[str] = Field(default=None, alias="MaximumFramerate")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    special_feature: Optional[str] = Field(default=None, alias="SpecialFeature")
    video_quality: Optional[str] = Field(default=None, alias="VideoQuality")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class M2tsSettingsModel(BaseModel):
    absent_input_audio_behavior: Optional[Literal["DROP", "ENCODE_SILENCE"]] = Field(
        default=None, alias="AbsentInputAudioBehavior"
    )
    arib: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="Arib")
    arib_captions_pid: Optional[str] = Field(default=None, alias="AribCaptionsPid")
    arib_captions_pid_control: Optional[Literal["AUTO", "USE_CONFIGURED"]] = Field(
        default=None, alias="AribCaptionsPidControl"
    )
    audio_buffer_model: Optional[Literal["ATSC", "DVB"]] = Field(
        default=None, alias="AudioBufferModel"
    )
    audio_frames_per_pes: Optional[int] = Field(default=None, alias="AudioFramesPerPes")
    audio_pids: Optional[str] = Field(default=None, alias="AudioPids")
    audio_stream_type: Optional[Literal["ATSC", "DVB"]] = Field(
        default=None, alias="AudioStreamType"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    buffer_model: Optional[Literal["MULTIPLEX", "NONE"]] = Field(
        default=None, alias="BufferModel"
    )
    cc_descriptor: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="CcDescriptor"
    )
    dvb_nit_settings: Optional[DvbNitSettingsModel] = Field(
        default=None, alias="DvbNitSettings"
    )
    dvb_sdt_settings: Optional[DvbSdtSettingsModel] = Field(
        default=None, alias="DvbSdtSettings"
    )
    dvb_sub_pids: Optional[str] = Field(default=None, alias="DvbSubPids")
    dvb_tdt_settings: Optional[DvbTdtSettingsModel] = Field(
        default=None, alias="DvbTdtSettings"
    )
    dvb_teletext_pid: Optional[str] = Field(default=None, alias="DvbTeletextPid")
    ebif: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(default=None, alias="Ebif")
    ebp_audio_interval: Optional[
        Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
    ] = Field(default=None, alias="EbpAudioInterval")
    ebp_lookahead_ms: Optional[int] = Field(default=None, alias="EbpLookaheadMs")
    ebp_placement: Optional[Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]] = Field(
        default=None, alias="EbpPlacement"
    )
    ecm_pid: Optional[str] = Field(default=None, alias="EcmPid")
    es_rate_in_pes: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="EsRateInPes"
    )
    etv_platform_pid: Optional[str] = Field(default=None, alias="EtvPlatformPid")
    etv_signal_pid: Optional[str] = Field(default=None, alias="EtvSignalPid")
    fragment_time: Optional[float] = Field(default=None, alias="FragmentTime")
    klv: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(default=None, alias="Klv")
    klv_data_pids: Optional[str] = Field(default=None, alias="KlvDataPids")
    nielsen_id3_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="NielsenId3Behavior"
    )
    null_packet_bitrate: Optional[float] = Field(
        default=None, alias="NullPacketBitrate"
    )
    pat_interval: Optional[int] = Field(default=None, alias="PatInterval")
    pcr_control: Optional[
        Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
    ] = Field(default=None, alias="PcrControl")
    pcr_period: Optional[int] = Field(default=None, alias="PcrPeriod")
    pcr_pid: Optional[str] = Field(default=None, alias="PcrPid")
    pmt_interval: Optional[int] = Field(default=None, alias="PmtInterval")
    pmt_pid: Optional[str] = Field(default=None, alias="PmtPid")
    program_num: Optional[int] = Field(default=None, alias="ProgramNum")
    rate_mode: Optional[Literal["CBR", "VBR"]] = Field(default=None, alias="RateMode")
    scte27_pids: Optional[str] = Field(default=None, alias="Scte27Pids")
    scte35_control: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Control"
    )
    scte35_pid: Optional[str] = Field(default=None, alias="Scte35Pid")
    segmentation_markers: Optional[
        Literal[
            "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
        ]
    ] = Field(default=None, alias="SegmentationMarkers")
    segmentation_style: Optional[Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]] = Field(
        default=None, alias="SegmentationStyle"
    )
    segmentation_time: Optional[float] = Field(default=None, alias="SegmentationTime")
    timed_metadata_behavior: Optional[Literal["NO_PASSTHROUGH", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadataBehavior"
    )
    timed_metadata_pid: Optional[str] = Field(default=None, alias="TimedMetadataPid")
    transport_stream_id: Optional[int] = Field(default=None, alias="TransportStreamId")
    video_pid: Optional[str] = Field(default=None, alias="VideoPid")
    scte35_preroll_pullup_milliseconds: Optional[float] = Field(
        default=None, alias="Scte35PrerollPullupMilliseconds"
    )


class FailoverConditionSettingsModel(BaseModel):
    audio_silence_settings: Optional[AudioSilenceFailoverSettingsModel] = Field(
        default=None, alias="AudioSilenceSettings"
    )
    input_loss_settings: Optional[InputLossFailoverSettingsModel] = Field(
        default=None, alias="InputLossSettings"
    )
    video_black_settings: Optional[VideoBlackFailoverSettingsModel] = Field(
        default=None, alias="VideoBlackSettings"
    )


class ScheduleActionStartSettingsModel(BaseModel):
    fixed_mode_schedule_action_start_settings: Optional[
        FixedModeScheduleActionStartSettingsModel
    ] = Field(default=None, alias="FixedModeScheduleActionStartSettings")
    follow_mode_schedule_action_start_settings: Optional[
        FollowModeScheduleActionStartSettingsModel
    ] = Field(default=None, alias="FollowModeScheduleActionStartSettings")
    immediate_mode_schedule_action_start_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="ImmediateModeScheduleActionStartSettings"
    )


class FrameCaptureCdnSettingsModel(BaseModel):
    frame_capture_s3_settings: Optional[FrameCaptureS3SettingsModel] = Field(
        default=None, alias="FrameCaptureS3Settings"
    )


class FrameCaptureSettingsModel(BaseModel):
    capture_interval: Optional[int] = Field(default=None, alias="CaptureInterval")
    capture_interval_units: Optional[Literal["MILLISECONDS", "SECONDS"]] = Field(
        default=None, alias="CaptureIntervalUnits"
    )
    timecode_burnin_settings: Optional[TimecodeBurninSettingsModel] = Field(
        default=None, alias="TimecodeBurninSettings"
    )


class H264FilterSettingsModel(BaseModel):
    temporal_filter_settings: Optional[TemporalFilterSettingsModel] = Field(
        default=None, alias="TemporalFilterSettings"
    )


class H265FilterSettingsModel(BaseModel):
    temporal_filter_settings: Optional[TemporalFilterSettingsModel] = Field(
        default=None, alias="TemporalFilterSettings"
    )


class Mpeg2FilterSettingsModel(BaseModel):
    temporal_filter_settings: Optional[TemporalFilterSettingsModel] = Field(
        default=None, alias="TemporalFilterSettings"
    )


class H265ColorSpaceSettingsModel(BaseModel):
    color_space_passthrough_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="ColorSpacePassthroughSettings"
    )
    dolby_vision81_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="DolbyVision81Settings"
    )
    hdr10_settings: Optional[Hdr10SettingsModel] = Field(
        default=None, alias="Hdr10Settings"
    )
    rec601_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Rec601Settings"
    )
    rec709_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Rec709Settings"
    )


class VideoSelectorColorSpaceSettingsModel(BaseModel):
    hdr10_settings: Optional[Hdr10SettingsModel] = Field(
        default=None, alias="Hdr10Settings"
    )


class HlsCdnSettingsModel(BaseModel):
    hls_akamai_settings: Optional[HlsAkamaiSettingsModel] = Field(
        default=None, alias="HlsAkamaiSettings"
    )
    hls_basic_put_settings: Optional[HlsBasicPutSettingsModel] = Field(
        default=None, alias="HlsBasicPutSettings"
    )
    hls_media_store_settings: Optional[HlsMediaStoreSettingsModel] = Field(
        default=None, alias="HlsMediaStoreSettings"
    )
    hls_s3_settings: Optional[HlsS3SettingsModel] = Field(
        default=None, alias="HlsS3Settings"
    )
    hls_webdav_settings: Optional[HlsWebdavSettingsModel] = Field(
        default=None, alias="HlsWebdavSettings"
    )


class NetworkInputSettingsModel(BaseModel):
    hls_input_settings: Optional[HlsInputSettingsModel] = Field(
        default=None, alias="HlsInputSettings"
    )
    server_validation: Optional[
        Literal["CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME", "CHECK_CRYPTOGRAPHY_ONLY"]
    ] = Field(default=None, alias="ServerValidation")


class InputClippingSettingsModel(BaseModel):
    input_timecode_source: Literal["EMBEDDED", "ZEROBASED"] = Field(
        alias="InputTimecodeSource"
    )
    start_timecode: Optional[StartTimecodeModel] = Field(
        default=None, alias="StartTimecode"
    )
    stop_timecode: Optional[StopTimecodeModel] = Field(
        default=None, alias="StopTimecode"
    )


class InputDestinationModel(BaseModel):
    ip: Optional[str] = Field(default=None, alias="Ip")
    port: Optional[str] = Field(default=None, alias="Port")
    url: Optional[str] = Field(default=None, alias="Url")
    vpc: Optional[InputDestinationVpcModel] = Field(default=None, alias="Vpc")


class UpdateInputDeviceRequestModel(BaseModel):
    input_device_id: str = Field(alias="InputDeviceId")
    hd_device_settings: Optional[InputDeviceConfigurableSettingsModel] = Field(
        default=None, alias="HdDeviceSettings"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    uhd_device_settings: Optional[InputDeviceConfigurableSettingsModel] = Field(
        default=None, alias="UhdDeviceSettings"
    )


class UpdateInputRequestModel(BaseModel):
    input_id: str = Field(alias="InputId")
    destinations: Optional[Sequence[InputDestinationRequestModel]] = Field(
        default=None, alias="Destinations"
    )
    input_devices: Optional[Sequence[InputDeviceRequestModel]] = Field(
        default=None, alias="InputDevices"
    )
    input_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="InputSecurityGroups"
    )
    media_connect_flows: Optional[Sequence[MediaConnectFlowRequestModel]] = Field(
        default=None, alias="MediaConnectFlows"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    sources: Optional[Sequence[InputSourceRequestModel]] = Field(
        default=None, alias="Sources"
    )


class ListInputDeviceTransfersResponseModel(BaseModel):
    input_device_transfers: List[TransferringInputDeviceSummaryModel] = Field(
        alias="InputDeviceTransfers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMultiplexProgramsResponseModel(BaseModel):
    multiplex_programs: List[MultiplexProgramSummaryModel] = Field(
        alias="MultiplexPrograms"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StandardHlsSettingsModel(BaseModel):
    m3u8_settings: M3u8SettingsModel = Field(alias="M3u8Settings")
    audio_rendition_sets: Optional[str] = Field(
        default=None, alias="AudioRenditionSets"
    )


class MotionGraphicsConfigurationModel(BaseModel):
    motion_graphics_settings: MotionGraphicsSettingsModel = Field(
        alias="MotionGraphicsSettings"
    )
    motion_graphics_insertion: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="MotionGraphicsInsertion"
    )


class MultiplexOutputDestinationModel(BaseModel):
    media_connect_settings: Optional[
        MultiplexMediaConnectOutputDestinationSettingsModel
    ] = Field(default=None, alias="MediaConnectSettings")


class MultiplexSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    multiplex_settings: Optional[MultiplexSettingsSummaryModel] = Field(
        default=None, alias="MultiplexSettings"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pipelines_running_count: Optional[int] = Field(
        default=None, alias="PipelinesRunningCount"
    )
    program_count: Optional[int] = Field(default=None, alias="ProgramCount")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "IDLE",
            "RECOVERING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class MultiplexVideoSettingsModel(BaseModel):
    constant_bitrate: Optional[int] = Field(default=None, alias="ConstantBitrate")
    statmux_settings: Optional[MultiplexStatmuxVideoSettingsModel] = Field(
        default=None, alias="StatmuxSettings"
    )


class NielsenWatermarksSettingsModel(BaseModel):
    nielsen_cbet_settings: Optional[NielsenCBETModel] = Field(
        default=None, alias="NielsenCbetSettings"
    )
    nielsen_distribution_type: Optional[
        Literal["FINAL_DISTRIBUTOR", "PROGRAM_CONTENT"]
    ] = Field(default=None, alias="NielsenDistributionType")
    nielsen_naes_ii_nw_settings: Optional[NielsenNaesIiNwModel] = Field(
        default=None, alias="NielsenNaesIiNwSettings"
    )


class OutputDestinationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    media_package_settings: Optional[
        Sequence[MediaPackageOutputDestinationSettingsModel]
    ] = Field(default=None, alias="MediaPackageSettings")
    multiplex_settings: Optional[
        MultiplexProgramChannelDestinationSettingsModel
    ] = Field(default=None, alias="MultiplexSettings")
    settings: Optional[Sequence[OutputDestinationSettingsModel]] = Field(
        default=None, alias="Settings"
    )


class PauseStateScheduleActionSettingsModel(BaseModel):
    pipelines: Optional[Sequence[PipelinePauseStateSettingsModel]] = Field(
        default=None, alias="Pipelines"
    )


class Scte35SegmentationDescriptorModel(BaseModel):
    segmentation_cancel_indicator: Literal[
        "SEGMENTATION_EVENT_CANCELED", "SEGMENTATION_EVENT_NOT_CANCELED"
    ] = Field(alias="SegmentationCancelIndicator")
    segmentation_event_id: int = Field(alias="SegmentationEventId")
    delivery_restrictions: Optional[Scte35DeliveryRestrictionsModel] = Field(
        default=None, alias="DeliveryRestrictions"
    )
    segment_num: Optional[int] = Field(default=None, alias="SegmentNum")
    segmentation_duration: Optional[int] = Field(
        default=None, alias="SegmentationDuration"
    )
    segmentation_type_id: Optional[int] = Field(
        default=None, alias="SegmentationTypeId"
    )
    segmentation_upid: Optional[str] = Field(default=None, alias="SegmentationUpid")
    segmentation_upid_type: Optional[int] = Field(
        default=None, alias="SegmentationUpidType"
    )
    segments_expected: Optional[int] = Field(default=None, alias="SegmentsExpected")
    sub_segment_num: Optional[int] = Field(default=None, alias="SubSegmentNum")
    sub_segments_expected: Optional[int] = Field(
        default=None, alias="SubSegmentsExpected"
    )


class VideoSelectorSettingsModel(BaseModel):
    video_selector_pid: Optional[VideoSelectorPidModel] = Field(
        default=None, alias="VideoSelectorPid"
    )
    video_selector_program_id: Optional[VideoSelectorProgramIdModel] = Field(
        default=None, alias="VideoSelectorProgramId"
    )


class ArchiveGroupSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")
    archive_cdn_settings: Optional[ArchiveCdnSettingsModel] = Field(
        default=None, alias="ArchiveCdnSettings"
    )
    rollover_interval: Optional[int] = Field(default=None, alias="RolloverInterval")


class RemixSettingsModel(BaseModel):
    channel_mappings: Sequence[AudioChannelMappingModel] = Field(
        alias="ChannelMappings"
    )
    channels_in: Optional[int] = Field(default=None, alias="ChannelsIn")
    channels_out: Optional[int] = Field(default=None, alias="ChannelsOut")


class CaptionDestinationSettingsModel(BaseModel):
    arib_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AribDestinationSettings"
    )
    burn_in_destination_settings: Optional[BurnInDestinationSettingsModel] = Field(
        default=None, alias="BurnInDestinationSettings"
    )
    dvb_sub_destination_settings: Optional[DvbSubDestinationSettingsModel] = Field(
        default=None, alias="DvbSubDestinationSettings"
    )
    ebu_tt_ddestination_settings: Optional[EbuTtDDestinationSettingsModel] = Field(
        default=None, alias="EbuTtDDestinationSettings"
    )
    embedded_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="EmbeddedDestinationSettings"
    )
    embedded_plus_scte20_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="EmbeddedPlusScte20DestinationSettings"
    )
    rtmp_caption_info_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="RtmpCaptionInfoDestinationSettings"
    )
    scte20_plus_embedded_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Scte20PlusEmbeddedDestinationSettings"
    )
    scte27_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="Scte27DestinationSettings"
    )
    smpte_tt_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="SmpteTtDestinationSettings"
    )
    teletext_destination_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="TeletextDestinationSettings"
    )
    ttml_destination_settings: Optional[TtmlDestinationSettingsModel] = Field(
        default=None, alias="TtmlDestinationSettings"
    )
    webvtt_destination_settings: Optional[WebvttDestinationSettingsModel] = Field(
        default=None, alias="WebvttDestinationSettings"
    )


class GlobalConfigurationModel(BaseModel):
    initial_audio_gain: Optional[int] = Field(default=None, alias="InitialAudioGain")
    input_end_action: Optional[Literal["NONE", "SWITCH_AND_LOOP_INPUTS"]] = Field(
        default=None, alias="InputEndAction"
    )
    input_loss_behavior: Optional[InputLossBehaviorModel] = Field(
        default=None, alias="InputLossBehavior"
    )
    output_locking_mode: Optional[Literal["EPOCH_LOCKING", "PIPELINE_LOCKING"]] = Field(
        default=None, alias="OutputLockingMode"
    )
    output_timing_source: Optional[Literal["INPUT_CLOCK", "SYSTEM_CLOCK"]] = Field(
        default=None, alias="OutputTimingSource"
    )
    support_low_framerate_inputs: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SupportLowFramerateInputs"
    )


class KeyProviderSettingsModel(BaseModel):
    static_key_settings: Optional[StaticKeySettingsModel] = Field(
        default=None, alias="StaticKeySettings"
    )


class AudioSelectorSettingsModel(BaseModel):
    audio_hls_rendition_selection: Optional[AudioHlsRenditionSelectionModel] = Field(
        default=None, alias="AudioHlsRenditionSelection"
    )
    audio_language_selection: Optional[AudioLanguageSelectionModel] = Field(
        default=None, alias="AudioLanguageSelection"
    )
    audio_pid_selection: Optional[AudioPidSelectionModel] = Field(
        default=None, alias="AudioPidSelection"
    )
    audio_track_selection: Optional[AudioTrackSelectionModel] = Field(
        default=None, alias="AudioTrackSelection"
    )


class AvailConfigurationModel(BaseModel):
    avail_settings: Optional[AvailSettingsModel] = Field(
        default=None, alias="AvailSettings"
    )


class CaptionSelectorSettingsModel(BaseModel):
    ancillary_source_settings: Optional[AncillarySourceSettingsModel] = Field(
        default=None, alias="AncillarySourceSettings"
    )
    arib_source_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AribSourceSettings"
    )
    dvb_sub_source_settings: Optional[DvbSubSourceSettingsModel] = Field(
        default=None, alias="DvbSubSourceSettings"
    )
    embedded_source_settings: Optional[EmbeddedSourceSettingsModel] = Field(
        default=None, alias="EmbeddedSourceSettings"
    )
    scte20_source_settings: Optional[Scte20SourceSettingsModel] = Field(
        default=None, alias="Scte20SourceSettings"
    )
    scte27_source_settings: Optional[Scte27SourceSettingsModel] = Field(
        default=None, alias="Scte27SourceSettings"
    )
    teletext_source_settings: Optional[TeletextSourceSettingsModel] = Field(
        default=None, alias="TeletextSourceSettings"
    )


class ListOfferingsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    offerings: List[OfferingModel] = Field(alias="Offerings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReservationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reservations: List[ReservationModel] = Field(alias="Reservations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseOfferingResponseModel(BaseModel):
    reservation: ReservationModel = Field(alias="Reservation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReservationResponseModel(BaseModel):
    reservation: ReservationModel = Field(alias="Reservation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInputDevicesResponseModel(BaseModel):
    input_devices: List[InputDeviceSummaryModel] = Field(alias="InputDevices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInputSecurityGroupResponseModel(BaseModel):
    security_group: InputSecurityGroupModel = Field(alias="SecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInputSecurityGroupsResponseModel(BaseModel):
    input_security_groups: List[InputSecurityGroupModel] = Field(
        alias="InputSecurityGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInputSecurityGroupResponseModel(BaseModel):
    security_group: InputSecurityGroupModel = Field(alias="SecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ArchiveContainerSettingsModel(BaseModel):
    m2ts_settings: Optional[M2tsSettingsModel] = Field(
        default=None, alias="M2tsSettings"
    )
    raw_settings: Optional[Mapping[str, Any]] = Field(default=None, alias="RawSettings")


class UdpContainerSettingsModel(BaseModel):
    m2ts_settings: Optional[M2tsSettingsModel] = Field(
        default=None, alias="M2tsSettings"
    )


class FailoverConditionModel(BaseModel):
    failover_condition_settings: Optional[FailoverConditionSettingsModel] = Field(
        default=None, alias="FailoverConditionSettings"
    )


class FrameCaptureGroupSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")
    frame_capture_cdn_settings: Optional[FrameCaptureCdnSettingsModel] = Field(
        default=None, alias="FrameCaptureCdnSettings"
    )


class H264SettingsModel(BaseModel):
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    afd_signaling: Optional[Literal["AUTO", "FIXED", "NONE"]] = Field(
        default=None, alias="AfdSignaling"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    buf_fill_pct: Optional[int] = Field(default=None, alias="BufFillPct")
    buf_size: Optional[int] = Field(default=None, alias="BufSize")
    color_metadata: Optional[Literal["IGNORE", "INSERT"]] = Field(
        default=None, alias="ColorMetadata"
    )
    color_space_settings: Optional[H264ColorSpaceSettingsModel] = Field(
        default=None, alias="ColorSpaceSettings"
    )
    entropy_encoding: Optional[Literal["CABAC", "CAVLC"]] = Field(
        default=None, alias="EntropyEncoding"
    )
    filter_settings: Optional[H264FilterSettingsModel] = Field(
        default=None, alias="FilterSettings"
    )
    fixed_afd: Optional[
        Literal[
            "AFD_0000",
            "AFD_0010",
            "AFD_0011",
            "AFD_0100",
            "AFD_1000",
            "AFD_1001",
            "AFD_1010",
            "AFD_1011",
            "AFD_1101",
            "AFD_1110",
            "AFD_1111",
        ]
    ] = Field(default=None, alias="FixedAfd")
    flicker_aq: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAq"
    )
    force_field_pictures: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ForceFieldPictures"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_breference: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="GopBReference"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_num_bframes: Optional[int] = Field(default=None, alias="GopNumBFrames")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    level: Optional[
        Literal[
            "H264_LEVEL_1",
            "H264_LEVEL_1_1",
            "H264_LEVEL_1_2",
            "H264_LEVEL_1_3",
            "H264_LEVEL_2",
            "H264_LEVEL_2_1",
            "H264_LEVEL_2_2",
            "H264_LEVEL_3",
            "H264_LEVEL_3_1",
            "H264_LEVEL_3_2",
            "H264_LEVEL_4",
            "H264_LEVEL_4_1",
            "H264_LEVEL_4_2",
            "H264_LEVEL_5",
            "H264_LEVEL_5_1",
            "H264_LEVEL_5_2",
            "H264_LEVEL_AUTO",
        ]
    ] = Field(default=None, alias="Level")
    look_ahead_rate_control: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="LookAheadRateControl"
    )
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    min_iinterval: Optional[int] = Field(default=None, alias="MinIInterval")
    num_ref_frames: Optional[int] = Field(default=None, alias="NumRefFrames")
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    profile: Optional[
        Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
    ] = Field(default=None, alias="Profile")
    quality_level: Optional[Literal["ENHANCED_QUALITY", "STANDARD_QUALITY"]] = Field(
        default=None, alias="QualityLevel"
    )
    qvbr_quality_level: Optional[int] = Field(default=None, alias="QvbrQualityLevel")
    rate_control_mode: Optional[Literal["CBR", "MULTIPLEX", "QVBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    scan_type: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="ScanType"
    )
    scene_change_detect: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SceneChangeDetect"
    )
    slices: Optional[int] = Field(default=None, alias="Slices")
    softness: Optional[int] = Field(default=None, alias="Softness")
    spatial_aq: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAq"
    )
    subgop_length: Optional[Literal["DYNAMIC", "FIXED"]] = Field(
        default=None, alias="SubgopLength"
    )
    syntax: Optional[Literal["DEFAULT", "RP2027"]] = Field(default=None, alias="Syntax")
    temporal_aq: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalAq"
    )
    timecode_insertion: Optional[Literal["DISABLED", "PIC_TIMING_SEI"]] = Field(
        default=None, alias="TimecodeInsertion"
    )
    timecode_burnin_settings: Optional[TimecodeBurninSettingsModel] = Field(
        default=None, alias="TimecodeBurninSettings"
    )


class Mpeg2SettingsModel(BaseModel):
    framerate_denominator: int = Field(alias="FramerateDenominator")
    framerate_numerator: int = Field(alias="FramerateNumerator")
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    afd_signaling: Optional[Literal["AUTO", "FIXED", "NONE"]] = Field(
        default=None, alias="AfdSignaling"
    )
    color_metadata: Optional[Literal["IGNORE", "INSERT"]] = Field(
        default=None, alias="ColorMetadata"
    )
    color_space: Optional[Literal["AUTO", "PASSTHROUGH"]] = Field(
        default=None, alias="ColorSpace"
    )
    display_aspect_ratio: Optional[
        Literal["DISPLAYRATIO16X9", "DISPLAYRATIO4X3"]
    ] = Field(default=None, alias="DisplayAspectRatio")
    filter_settings: Optional[Mpeg2FilterSettingsModel] = Field(
        default=None, alias="FilterSettings"
    )
    fixed_afd: Optional[
        Literal[
            "AFD_0000",
            "AFD_0010",
            "AFD_0011",
            "AFD_0100",
            "AFD_1000",
            "AFD_1001",
            "AFD_1010",
            "AFD_1011",
            "AFD_1101",
            "AFD_1110",
            "AFD_1111",
        ]
    ] = Field(default=None, alias="FixedAfd")
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_num_bframes: Optional[int] = Field(default=None, alias="GopNumBFrames")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    scan_type: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="ScanType"
    )
    subgop_length: Optional[Literal["DYNAMIC", "FIXED"]] = Field(
        default=None, alias="SubgopLength"
    )
    timecode_insertion: Optional[Literal["DISABLED", "GOP_TIMECODE"]] = Field(
        default=None, alias="TimecodeInsertion"
    )
    timecode_burnin_settings: Optional[TimecodeBurninSettingsModel] = Field(
        default=None, alias="TimecodeBurninSettings"
    )


class H265SettingsModel(BaseModel):
    framerate_denominator: int = Field(alias="FramerateDenominator")
    framerate_numerator: int = Field(alias="FramerateNumerator")
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    afd_signaling: Optional[Literal["AUTO", "FIXED", "NONE"]] = Field(
        default=None, alias="AfdSignaling"
    )
    alternative_transfer_function: Optional[Literal["INSERT", "OMIT"]] = Field(
        default=None, alias="AlternativeTransferFunction"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    buf_size: Optional[int] = Field(default=None, alias="BufSize")
    color_metadata: Optional[Literal["IGNORE", "INSERT"]] = Field(
        default=None, alias="ColorMetadata"
    )
    color_space_settings: Optional[H265ColorSpaceSettingsModel] = Field(
        default=None, alias="ColorSpaceSettings"
    )
    filter_settings: Optional[H265FilterSettingsModel] = Field(
        default=None, alias="FilterSettings"
    )
    fixed_afd: Optional[
        Literal[
            "AFD_0000",
            "AFD_0010",
            "AFD_0011",
            "AFD_0100",
            "AFD_1000",
            "AFD_1001",
            "AFD_1010",
            "AFD_1011",
            "AFD_1101",
            "AFD_1110",
            "AFD_1111",
        ]
    ] = Field(default=None, alias="FixedAfd")
    flicker_aq: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAq"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    level: Optional[
        Literal[
            "H265_LEVEL_1",
            "H265_LEVEL_2",
            "H265_LEVEL_2_1",
            "H265_LEVEL_3",
            "H265_LEVEL_3_1",
            "H265_LEVEL_4",
            "H265_LEVEL_4_1",
            "H265_LEVEL_5",
            "H265_LEVEL_5_1",
            "H265_LEVEL_5_2",
            "H265_LEVEL_6",
            "H265_LEVEL_6_1",
            "H265_LEVEL_6_2",
            "H265_LEVEL_AUTO",
        ]
    ] = Field(default=None, alias="Level")
    look_ahead_rate_control: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="LookAheadRateControl"
    )
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    min_iinterval: Optional[int] = Field(default=None, alias="MinIInterval")
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    profile: Optional[Literal["MAIN", "MAIN_10BIT"]] = Field(
        default=None, alias="Profile"
    )
    qvbr_quality_level: Optional[int] = Field(default=None, alias="QvbrQualityLevel")
    rate_control_mode: Optional[Literal["CBR", "MULTIPLEX", "QVBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    scan_type: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="ScanType"
    )
    scene_change_detect: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SceneChangeDetect"
    )
    slices: Optional[int] = Field(default=None, alias="Slices")
    tier: Optional[Literal["HIGH", "MAIN"]] = Field(default=None, alias="Tier")
    timecode_insertion: Optional[Literal["DISABLED", "PIC_TIMING_SEI"]] = Field(
        default=None, alias="TimecodeInsertion"
    )
    timecode_burnin_settings: Optional[TimecodeBurninSettingsModel] = Field(
        default=None, alias="TimecodeBurninSettings"
    )


class InputPrepareScheduleActionSettingsModel(BaseModel):
    input_attachment_name_reference: Optional[str] = Field(
        default=None, alias="InputAttachmentNameReference"
    )
    input_clipping_settings: Optional[InputClippingSettingsModel] = Field(
        default=None, alias="InputClippingSettings"
    )
    url_path: Optional[Sequence[str]] = Field(default=None, alias="UrlPath")


class InputSwitchScheduleActionSettingsModel(BaseModel):
    input_attachment_name_reference: str = Field(alias="InputAttachmentNameReference")
    input_clipping_settings: Optional[InputClippingSettingsModel] = Field(
        default=None, alias="InputClippingSettings"
    )
    url_path: Optional[Sequence[str]] = Field(default=None, alias="UrlPath")


class DescribeInputResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    attached_channels: List[str] = Field(alias="AttachedChannels")
    destinations: List[InputDestinationModel] = Field(alias="Destinations")
    id: str = Field(alias="Id")
    input_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="InputClass")
    input_devices: List[InputDeviceSettingsModel] = Field(alias="InputDevices")
    input_partner_ids: List[str] = Field(alias="InputPartnerIds")
    input_source_type: Literal["DYNAMIC", "STATIC"] = Field(alias="InputSourceType")
    media_connect_flows: List[MediaConnectFlowModel] = Field(alias="MediaConnectFlows")
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    security_groups: List[str] = Field(alias="SecurityGroups")
    sources: List[InputSourceModel] = Field(alias="Sources")
    state: Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"] = Field(
        alias="State"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal[
        "AWS_CDI",
        "INPUT_DEVICE",
        "MEDIACONNECT",
        "MP4_FILE",
        "RTMP_PULL",
        "RTMP_PUSH",
        "RTP_PUSH",
        "TS_FILE",
        "UDP_PUSH",
        "URL_PULL",
    ] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    attached_channels: Optional[List[str]] = Field(
        default=None, alias="AttachedChannels"
    )
    destinations: Optional[List[InputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    input_class: Optional[Literal["SINGLE_PIPELINE", "STANDARD"]] = Field(
        default=None, alias="InputClass"
    )
    input_devices: Optional[List[InputDeviceSettingsModel]] = Field(
        default=None, alias="InputDevices"
    )
    input_partner_ids: Optional[List[str]] = Field(
        default=None, alias="InputPartnerIds"
    )
    input_source_type: Optional[Literal["DYNAMIC", "STATIC"]] = Field(
        default=None, alias="InputSourceType"
    )
    media_connect_flows: Optional[List[MediaConnectFlowModel]] = Field(
        default=None, alias="MediaConnectFlows"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    sources: Optional[List[InputSourceModel]] = Field(default=None, alias="Sources")
    state: Optional[
        Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    type: Optional[
        Literal[
            "AWS_CDI",
            "INPUT_DEVICE",
            "MEDIACONNECT",
            "MP4_FILE",
            "RTMP_PULL",
            "RTMP_PUSH",
            "RTP_PUSH",
            "TS_FILE",
            "UDP_PUSH",
            "URL_PULL",
        ]
    ] = Field(default=None, alias="Type")


class HlsSettingsModel(BaseModel):
    audio_only_hls_settings: Optional[AudioOnlyHlsSettingsModel] = Field(
        default=None, alias="AudioOnlyHlsSettings"
    )
    fmp4_hls_settings: Optional[Fmp4HlsSettingsModel] = Field(
        default=None, alias="Fmp4HlsSettings"
    )
    frame_capture_hls_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="FrameCaptureHlsSettings"
    )
    standard_hls_settings: Optional[StandardHlsSettingsModel] = Field(
        default=None, alias="StandardHlsSettings"
    )


class DeleteMultiplexResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    destinations: List[MultiplexOutputDestinationModel] = Field(alias="Destinations")
    id: str = Field(alias="Id")
    multiplex_settings: MultiplexSettingsModel = Field(alias="MultiplexSettings")
    name: str = Field(alias="Name")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    program_count: int = Field(alias="ProgramCount")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMultiplexResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    destinations: List[MultiplexOutputDestinationModel] = Field(alias="Destinations")
    id: str = Field(alias="Id")
    multiplex_settings: MultiplexSettingsModel = Field(alias="MultiplexSettings")
    name: str = Field(alias="Name")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    program_count: int = Field(alias="ProgramCount")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MultiplexModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    destinations: Optional[List[MultiplexOutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    multiplex_settings: Optional[MultiplexSettingsModel] = Field(
        default=None, alias="MultiplexSettings"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pipelines_running_count: Optional[int] = Field(
        default=None, alias="PipelinesRunningCount"
    )
    program_count: Optional[int] = Field(default=None, alias="ProgramCount")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "IDLE",
            "RECOVERING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class StartMultiplexResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    destinations: List[MultiplexOutputDestinationModel] = Field(alias="Destinations")
    id: str = Field(alias="Id")
    multiplex_settings: MultiplexSettingsModel = Field(alias="MultiplexSettings")
    name: str = Field(alias="Name")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    program_count: int = Field(alias="ProgramCount")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopMultiplexResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    destinations: List[MultiplexOutputDestinationModel] = Field(alias="Destinations")
    id: str = Field(alias="Id")
    multiplex_settings: MultiplexSettingsModel = Field(alias="MultiplexSettings")
    name: str = Field(alias="Name")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    program_count: int = Field(alias="ProgramCount")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMultiplexesResponseModel(BaseModel):
    multiplexes: List[MultiplexSummaryModel] = Field(alias="Multiplexes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MultiplexProgramSettingsModel(BaseModel):
    program_number: int = Field(alias="ProgramNumber")
    preferred_channel_pipeline: Optional[
        Literal["CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1"]
    ] = Field(default=None, alias="PreferredChannelPipeline")
    service_descriptor: Optional[MultiplexProgramServiceDescriptorModel] = Field(
        default=None, alias="ServiceDescriptor"
    )
    video_settings: Optional[MultiplexVideoSettingsModel] = Field(
        default=None, alias="VideoSettings"
    )


class AudioWatermarkSettingsModel(BaseModel):
    nielsen_watermarks_settings: Optional[NielsenWatermarksSettingsModel] = Field(
        default=None, alias="NielsenWatermarksSettings"
    )


class UpdateChannelClassRequestModel(BaseModel):
    channel_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="ChannelClass")
    channel_id: str = Field(alias="ChannelId")
    destinations: Optional[Sequence[OutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )


class Scte35DescriptorSettingsModel(BaseModel):
    segmentation_descriptor_scte35_descriptor_settings: Scte35SegmentationDescriptorModel = Field(
        alias="SegmentationDescriptorScte35DescriptorSettings"
    )


class VideoSelectorModel(BaseModel):
    color_space: Optional[
        Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
    ] = Field(default=None, alias="ColorSpace")
    color_space_settings: Optional[VideoSelectorColorSpaceSettingsModel] = Field(
        default=None, alias="ColorSpaceSettings"
    )
    color_space_usage: Optional[Literal["FALLBACK", "FORCE"]] = Field(
        default=None, alias="ColorSpaceUsage"
    )
    selector_settings: Optional[VideoSelectorSettingsModel] = Field(
        default=None, alias="SelectorSettings"
    )


class CaptionDescriptionModel(BaseModel):
    caption_selector_name: str = Field(alias="CaptionSelectorName")
    name: str = Field(alias="Name")
    accessibility: Optional[
        Literal[
            "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES",
            "IMPLEMENTS_ACCESSIBILITY_FEATURES",
        ]
    ] = Field(default=None, alias="Accessibility")
    destination_settings: Optional[CaptionDestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    language_description: Optional[str] = Field(
        default=None, alias="LanguageDescription"
    )


class HlsGroupSettingsModel(BaseModel):
    destination: OutputLocationRefModel = Field(alias="Destination")
    ad_markers: Optional[
        Sequence[Literal["ADOBE", "ELEMENTAL", "ELEMENTAL_SCTE35"]]
    ] = Field(default=None, alias="AdMarkers")
    base_url_content: Optional[str] = Field(default=None, alias="BaseUrlContent")
    base_url_content1: Optional[str] = Field(default=None, alias="BaseUrlContent1")
    base_url_manifest: Optional[str] = Field(default=None, alias="BaseUrlManifest")
    base_url_manifest1: Optional[str] = Field(default=None, alias="BaseUrlManifest1")
    caption_language_mappings: Optional[Sequence[CaptionLanguageMappingModel]] = Field(
        default=None, alias="CaptionLanguageMappings"
    )
    caption_language_setting: Optional[Literal["INSERT", "NONE", "OMIT"]] = Field(
        default=None, alias="CaptionLanguageSetting"
    )
    client_cache: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ClientCache"
    )
    codec_specification: Optional[Literal["RFC_4281", "RFC_6381"]] = Field(
        default=None, alias="CodecSpecification"
    )
    constant_iv: Optional[str] = Field(default=None, alias="ConstantIv")
    directory_structure: Optional[
        Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
    ] = Field(default=None, alias="DirectoryStructure")
    discontinuity_tags: Optional[Literal["INSERT", "NEVER_INSERT"]] = Field(
        default=None, alias="DiscontinuityTags"
    )
    encryption_type: Optional[Literal["AES128", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionType"
    )
    hls_cdn_settings: Optional[HlsCdnSettingsModel] = Field(
        default=None, alias="HlsCdnSettings"
    )
    hls_id3_segment_tagging: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="HlsId3SegmentTagging"
    )
    iframe_only_playlists: Optional[Literal["DISABLED", "STANDARD"]] = Field(
        default=None, alias="IFrameOnlyPlaylists"
    )
    incomplete_segment_behavior: Optional[Literal["AUTO", "SUPPRESS"]] = Field(
        default=None, alias="IncompleteSegmentBehavior"
    )
    index_nsegments: Optional[int] = Field(default=None, alias="IndexNSegments")
    input_loss_action: Optional[Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]] = Field(
        default=None, alias="InputLossAction"
    )
    iv_in_manifest: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="IvInManifest"
    )
    iv_source: Optional[Literal["EXPLICIT", "FOLLOWS_SEGMENT_NUMBER"]] = Field(
        default=None, alias="IvSource"
    )
    keep_segments: Optional[int] = Field(default=None, alias="KeepSegments")
    key_format: Optional[str] = Field(default=None, alias="KeyFormat")
    key_format_versions: Optional[str] = Field(default=None, alias="KeyFormatVersions")
    key_provider_settings: Optional[KeyProviderSettingsModel] = Field(
        default=None, alias="KeyProviderSettings"
    )
    manifest_compression: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="ManifestCompression"
    )
    manifest_duration_format: Optional[Literal["FLOATING_POINT", "INTEGER"]] = Field(
        default=None, alias="ManifestDurationFormat"
    )
    min_segment_length: Optional[int] = Field(default=None, alias="MinSegmentLength")
    mode: Optional[Literal["LIVE", "VOD"]] = Field(default=None, alias="Mode")
    output_selection: Optional[
        Literal[
            "MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY", "VARIANT_MANIFESTS_AND_SEGMENTS"
        ]
    ] = Field(default=None, alias="OutputSelection")
    program_date_time: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="ProgramDateTime"
    )
    program_date_time_clock: Optional[
        Literal["INITIALIZE_FROM_OUTPUT_TIMECODE", "SYSTEM_CLOCK"]
    ] = Field(default=None, alias="ProgramDateTimeClock")
    program_date_time_period: Optional[int] = Field(
        default=None, alias="ProgramDateTimePeriod"
    )
    redundant_manifest: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="RedundantManifest"
    )
    segment_length: Optional[int] = Field(default=None, alias="SegmentLength")
    segmentation_mode: Optional[
        Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
    ] = Field(default=None, alias="SegmentationMode")
    segments_per_subdirectory: Optional[int] = Field(
        default=None, alias="SegmentsPerSubdirectory"
    )
    stream_inf_resolution: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="StreamInfResolution"
    )
    timed_metadata_id3_frame: Optional[Literal["NONE", "PRIV", "TDRL"]] = Field(
        default=None, alias="TimedMetadataId3Frame"
    )
    timed_metadata_id3_period: Optional[int] = Field(
        default=None, alias="TimedMetadataId3Period"
    )
    timestamp_delta_milliseconds: Optional[int] = Field(
        default=None, alias="TimestampDeltaMilliseconds"
    )
    ts_file_mode: Optional[Literal["SEGMENTED_FILES", "SINGLE_FILE"]] = Field(
        default=None, alias="TsFileMode"
    )


class AudioSelectorModel(BaseModel):
    name: str = Field(alias="Name")
    selector_settings: Optional[AudioSelectorSettingsModel] = Field(
        default=None, alias="SelectorSettings"
    )


class CaptionSelectorModel(BaseModel):
    name: str = Field(alias="Name")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    selector_settings: Optional[CaptionSelectorSettingsModel] = Field(
        default=None, alias="SelectorSettings"
    )


class ArchiveOutputSettingsModel(BaseModel):
    container_settings: ArchiveContainerSettingsModel = Field(alias="ContainerSettings")
    extension: Optional[str] = Field(default=None, alias="Extension")
    name_modifier: Optional[str] = Field(default=None, alias="NameModifier")


class UdpOutputSettingsModel(BaseModel):
    container_settings: UdpContainerSettingsModel = Field(alias="ContainerSettings")
    destination: OutputLocationRefModel = Field(alias="Destination")
    buffer_msec: Optional[int] = Field(default=None, alias="BufferMsec")
    fec_output_settings: Optional[FecOutputSettingsModel] = Field(
        default=None, alias="FecOutputSettings"
    )


class AutomaticInputFailoverSettingsModel(BaseModel):
    secondary_input_id: str = Field(alias="SecondaryInputId")
    error_clear_time_msec: Optional[int] = Field(
        default=None, alias="ErrorClearTimeMsec"
    )
    failover_conditions: Optional[Sequence[FailoverConditionModel]] = Field(
        default=None, alias="FailoverConditions"
    )
    input_preference: Optional[
        Literal["EQUAL_INPUT_PREFERENCE", "PRIMARY_INPUT_PREFERRED"]
    ] = Field(default=None, alias="InputPreference")


class VideoCodecSettingsModel(BaseModel):
    frame_capture_settings: Optional[FrameCaptureSettingsModel] = Field(
        default=None, alias="FrameCaptureSettings"
    )
    h264_settings: Optional[H264SettingsModel] = Field(
        default=None, alias="H264Settings"
    )
    h265_settings: Optional[H265SettingsModel] = Field(
        default=None, alias="H265Settings"
    )
    mpeg2_settings: Optional[Mpeg2SettingsModel] = Field(
        default=None, alias="Mpeg2Settings"
    )


class CreateInputResponseModel(BaseModel):
    input: InputModel = Field(alias="Input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePartnerInputResponseModel(BaseModel):
    input: InputModel = Field(alias="Input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInputsResponseModel(BaseModel):
    inputs: List[InputModel] = Field(alias="Inputs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInputResponseModel(BaseModel):
    input: InputModel = Field(alias="Input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HlsOutputSettingsModel(BaseModel):
    hls_settings: HlsSettingsModel = Field(alias="HlsSettings")
    h265_packaging_type: Optional[Literal["HEV1", "HVC1"]] = Field(
        default=None, alias="H265PackagingType"
    )
    name_modifier: Optional[str] = Field(default=None, alias="NameModifier")
    segment_modifier: Optional[str] = Field(default=None, alias="SegmentModifier")


class CreateMultiplexResponseModel(BaseModel):
    multiplex: MultiplexModel = Field(alias="Multiplex")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMultiplexResponseModel(BaseModel):
    multiplex: MultiplexModel = Field(alias="Multiplex")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMultiplexProgramRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    multiplex_program_settings: MultiplexProgramSettingsModel = Field(
        alias="MultiplexProgramSettings"
    )
    program_name: str = Field(alias="ProgramName")
    request_id: str = Field(alias="RequestId")


class DeleteMultiplexProgramResponseModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    multiplex_program_settings: MultiplexProgramSettingsModel = Field(
        alias="MultiplexProgramSettings"
    )
    packet_identifiers_map: MultiplexProgramPacketIdentifiersMapModel = Field(
        alias="PacketIdentifiersMap"
    )
    pipeline_details: List[MultiplexProgramPipelineDetailModel] = Field(
        alias="PipelineDetails"
    )
    program_name: str = Field(alias="ProgramName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMultiplexProgramResponseModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    multiplex_program_settings: MultiplexProgramSettingsModel = Field(
        alias="MultiplexProgramSettings"
    )
    packet_identifiers_map: MultiplexProgramPacketIdentifiersMapModel = Field(
        alias="PacketIdentifiersMap"
    )
    pipeline_details: List[MultiplexProgramPipelineDetailModel] = Field(
        alias="PipelineDetails"
    )
    program_name: str = Field(alias="ProgramName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MultiplexProgramModel(BaseModel):
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    multiplex_program_settings: Optional[MultiplexProgramSettingsModel] = Field(
        default=None, alias="MultiplexProgramSettings"
    )
    packet_identifiers_map: Optional[MultiplexProgramPacketIdentifiersMapModel] = Field(
        default=None, alias="PacketIdentifiersMap"
    )
    pipeline_details: Optional[List[MultiplexProgramPipelineDetailModel]] = Field(
        default=None, alias="PipelineDetails"
    )
    program_name: Optional[str] = Field(default=None, alias="ProgramName")


class UpdateMultiplexProgramRequestModel(BaseModel):
    multiplex_id: str = Field(alias="MultiplexId")
    program_name: str = Field(alias="ProgramName")
    multiplex_program_settings: Optional[MultiplexProgramSettingsModel] = Field(
        default=None, alias="MultiplexProgramSettings"
    )


class AudioDescriptionModel(BaseModel):
    audio_selector_name: str = Field(alias="AudioSelectorName")
    name: str = Field(alias="Name")
    audio_normalization_settings: Optional[AudioNormalizationSettingsModel] = Field(
        default=None, alias="AudioNormalizationSettings"
    )
    audio_type: Optional[
        Literal[
            "CLEAN_EFFECTS",
            "HEARING_IMPAIRED",
            "UNDEFINED",
            "VISUAL_IMPAIRED_COMMENTARY",
        ]
    ] = Field(default=None, alias="AudioType")
    audio_type_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="AudioTypeControl"
    )
    audio_watermarking_settings: Optional[AudioWatermarkSettingsModel] = Field(
        default=None, alias="AudioWatermarkingSettings"
    )
    codec_settings: Optional[AudioCodecSettingsModel] = Field(
        default=None, alias="CodecSettings"
    )
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    language_code_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="LanguageCodeControl"
    )
    remix_settings: Optional[RemixSettingsModel] = Field(
        default=None, alias="RemixSettings"
    )
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class Scte35DescriptorModel(BaseModel):
    scte35_descriptor_settings: Scte35DescriptorSettingsModel = Field(
        alias="Scte35DescriptorSettings"
    )


class OutputGroupSettingsModel(BaseModel):
    archive_group_settings: Optional[ArchiveGroupSettingsModel] = Field(
        default=None, alias="ArchiveGroupSettings"
    )
    frame_capture_group_settings: Optional[FrameCaptureGroupSettingsModel] = Field(
        default=None, alias="FrameCaptureGroupSettings"
    )
    hls_group_settings: Optional[HlsGroupSettingsModel] = Field(
        default=None, alias="HlsGroupSettings"
    )
    media_package_group_settings: Optional[MediaPackageGroupSettingsModel] = Field(
        default=None, alias="MediaPackageGroupSettings"
    )
    ms_smooth_group_settings: Optional[MsSmoothGroupSettingsModel] = Field(
        default=None, alias="MsSmoothGroupSettings"
    )
    multiplex_group_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="MultiplexGroupSettings"
    )
    rtmp_group_settings: Optional[RtmpGroupSettingsModel] = Field(
        default=None, alias="RtmpGroupSettings"
    )
    udp_group_settings: Optional[UdpGroupSettingsModel] = Field(
        default=None, alias="UdpGroupSettings"
    )


class InputSettingsModel(BaseModel):
    audio_selectors: Optional[Sequence[AudioSelectorModel]] = Field(
        default=None, alias="AudioSelectors"
    )
    caption_selectors: Optional[Sequence[CaptionSelectorModel]] = Field(
        default=None, alias="CaptionSelectors"
    )
    deblock_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DeblockFilter"
    )
    denoise_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DenoiseFilter"
    )
    filter_strength: Optional[int] = Field(default=None, alias="FilterStrength")
    input_filter: Optional[Literal["AUTO", "DISABLED", "FORCED"]] = Field(
        default=None, alias="InputFilter"
    )
    network_input_settings: Optional[NetworkInputSettingsModel] = Field(
        default=None, alias="NetworkInputSettings"
    )
    scte35_pid: Optional[int] = Field(default=None, alias="Scte35Pid")
    smpte2038_data_preference: Optional[Literal["IGNORE", "PREFER"]] = Field(
        default=None, alias="Smpte2038DataPreference"
    )
    source_end_behavior: Optional[Literal["CONTINUE", "LOOP"]] = Field(
        default=None, alias="SourceEndBehavior"
    )
    video_selector: Optional[VideoSelectorModel] = Field(
        default=None, alias="VideoSelector"
    )


class VideoDescriptionModel(BaseModel):
    name: str = Field(alias="Name")
    codec_settings: Optional[VideoCodecSettingsModel] = Field(
        default=None, alias="CodecSettings"
    )
    height: Optional[int] = Field(default=None, alias="Height")
    respond_to_afd: Optional[Literal["NONE", "PASSTHROUGH", "RESPOND"]] = Field(
        default=None, alias="RespondToAfd"
    )
    scaling_behavior: Optional[Literal["DEFAULT", "STRETCH_TO_OUTPUT"]] = Field(
        default=None, alias="ScalingBehavior"
    )
    sharpness: Optional[int] = Field(default=None, alias="Sharpness")
    width: Optional[int] = Field(default=None, alias="Width")


class OutputSettingsModel(BaseModel):
    archive_output_settings: Optional[ArchiveOutputSettingsModel] = Field(
        default=None, alias="ArchiveOutputSettings"
    )
    frame_capture_output_settings: Optional[FrameCaptureOutputSettingsModel] = Field(
        default=None, alias="FrameCaptureOutputSettings"
    )
    hls_output_settings: Optional[HlsOutputSettingsModel] = Field(
        default=None, alias="HlsOutputSettings"
    )
    media_package_output_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="MediaPackageOutputSettings"
    )
    ms_smooth_output_settings: Optional[MsSmoothOutputSettingsModel] = Field(
        default=None, alias="MsSmoothOutputSettings"
    )
    multiplex_output_settings: Optional[MultiplexOutputSettingsModel] = Field(
        default=None, alias="MultiplexOutputSettings"
    )
    rtmp_output_settings: Optional[RtmpOutputSettingsModel] = Field(
        default=None, alias="RtmpOutputSettings"
    )
    udp_output_settings: Optional[UdpOutputSettingsModel] = Field(
        default=None, alias="UdpOutputSettings"
    )


class CreateMultiplexProgramResponseModel(BaseModel):
    multiplex_program: MultiplexProgramModel = Field(alias="MultiplexProgram")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMultiplexProgramResponseModel(BaseModel):
    multiplex_program: MultiplexProgramModel = Field(alias="MultiplexProgram")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class Scte35TimeSignalScheduleActionSettingsModel(BaseModel):
    scte35_descriptors: Sequence[Scte35DescriptorModel] = Field(
        alias="Scte35Descriptors"
    )


class InputAttachmentModel(BaseModel):
    automatic_input_failover_settings: Optional[
        AutomaticInputFailoverSettingsModel
    ] = Field(default=None, alias="AutomaticInputFailoverSettings")
    input_attachment_name: Optional[str] = Field(
        default=None, alias="InputAttachmentName"
    )
    input_id: Optional[str] = Field(default=None, alias="InputId")
    input_settings: Optional[InputSettingsModel] = Field(
        default=None, alias="InputSettings"
    )


class OutputModel(BaseModel):
    output_settings: OutputSettingsModel = Field(alias="OutputSettings")
    audio_description_names: Optional[Sequence[str]] = Field(
        default=None, alias="AudioDescriptionNames"
    )
    caption_description_names: Optional[Sequence[str]] = Field(
        default=None, alias="CaptionDescriptionNames"
    )
    output_name: Optional[str] = Field(default=None, alias="OutputName")
    video_description_name: Optional[str] = Field(
        default=None, alias="VideoDescriptionName"
    )


class ScheduleActionSettingsModel(BaseModel):
    hls_id3_segment_tagging_settings: Optional[
        HlsId3SegmentTaggingScheduleActionSettingsModel
    ] = Field(default=None, alias="HlsId3SegmentTaggingSettings")
    hls_timed_metadata_settings: Optional[
        HlsTimedMetadataScheduleActionSettingsModel
    ] = Field(default=None, alias="HlsTimedMetadataSettings")
    input_prepare_settings: Optional[InputPrepareScheduleActionSettingsModel] = Field(
        default=None, alias="InputPrepareSettings"
    )
    input_switch_settings: Optional[InputSwitchScheduleActionSettingsModel] = Field(
        default=None, alias="InputSwitchSettings"
    )
    motion_graphics_image_activate_settings: Optional[
        MotionGraphicsActivateScheduleActionSettingsModel
    ] = Field(default=None, alias="MotionGraphicsImageActivateSettings")
    motion_graphics_image_deactivate_settings: Optional[Mapping[str, Any]] = Field(
        default=None, alias="MotionGraphicsImageDeactivateSettings"
    )
    pause_state_settings: Optional[PauseStateScheduleActionSettingsModel] = Field(
        default=None, alias="PauseStateSettings"
    )
    scte35_input_settings: Optional[Scte35InputScheduleActionSettingsModel] = Field(
        default=None, alias="Scte35InputSettings"
    )
    scte35_return_to_network_settings: Optional[
        Scte35ReturnToNetworkScheduleActionSettingsModel
    ] = Field(default=None, alias="Scte35ReturnToNetworkSettings")
    scte35_splice_insert_settings: Optional[
        Scte35SpliceInsertScheduleActionSettingsModel
    ] = Field(default=None, alias="Scte35SpliceInsertSettings")
    scte35_time_signal_settings: Optional[
        Scte35TimeSignalScheduleActionSettingsModel
    ] = Field(default=None, alias="Scte35TimeSignalSettings")
    static_image_activate_settings: Optional[
        StaticImageActivateScheduleActionSettingsModel
    ] = Field(default=None, alias="StaticImageActivateSettings")
    static_image_deactivate_settings: Optional[
        StaticImageDeactivateScheduleActionSettingsModel
    ] = Field(default=None, alias="StaticImageDeactivateSettings")


class ChannelSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    cdi_input_specification: Optional[CdiInputSpecificationModel] = Field(
        default=None, alias="CdiInputSpecification"
    )
    channel_class: Optional[Literal["SINGLE_PIPELINE", "STANDARD"]] = Field(
        default=None, alias="ChannelClass"
    )
    destinations: Optional[List[OutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    egress_endpoints: Optional[List[ChannelEgressEndpointModel]] = Field(
        default=None, alias="EgressEndpoints"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    input_attachments: Optional[List[InputAttachmentModel]] = Field(
        default=None, alias="InputAttachments"
    )
    input_specification: Optional[InputSpecificationModel] = Field(
        default=None, alias="InputSpecification"
    )
    log_level: Optional[
        Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
    ] = Field(default=None, alias="LogLevel")
    maintenance: Optional[MaintenanceStatusModel] = Field(
        default=None, alias="Maintenance"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pipelines_running_count: Optional[int] = Field(
        default=None, alias="PipelinesRunningCount"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "IDLE",
            "RECOVERING",
            "RUNNING",
            "STARTING",
            "STOPPING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    vpc: Optional[VpcOutputSettingsDescriptionModel] = Field(default=None, alias="Vpc")


class OutputGroupModel(BaseModel):
    output_group_settings: OutputGroupSettingsModel = Field(alias="OutputGroupSettings")
    outputs: Sequence[OutputModel] = Field(alias="Outputs")
    name: Optional[str] = Field(default=None, alias="Name")


class ScheduleActionModel(BaseModel):
    action_name: str = Field(alias="ActionName")
    schedule_action_settings: ScheduleActionSettingsModel = Field(
        alias="ScheduleActionSettings"
    )
    schedule_action_start_settings: ScheduleActionStartSettingsModel = Field(
        alias="ScheduleActionStartSettings"
    )


class ListChannelsResponseModel(BaseModel):
    channels: List[ChannelSummaryModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EncoderSettingsModel(BaseModel):
    audio_descriptions: Sequence[AudioDescriptionModel] = Field(
        alias="AudioDescriptions"
    )
    output_groups: Sequence[OutputGroupModel] = Field(alias="OutputGroups")
    timecode_config: TimecodeConfigModel = Field(alias="TimecodeConfig")
    video_descriptions: Sequence[VideoDescriptionModel] = Field(
        alias="VideoDescriptions"
    )
    avail_blanking: Optional[AvailBlankingModel] = Field(
        default=None, alias="AvailBlanking"
    )
    avail_configuration: Optional[AvailConfigurationModel] = Field(
        default=None, alias="AvailConfiguration"
    )
    blackout_slate: Optional[BlackoutSlateModel] = Field(
        default=None, alias="BlackoutSlate"
    )
    caption_descriptions: Optional[Sequence[CaptionDescriptionModel]] = Field(
        default=None, alias="CaptionDescriptions"
    )
    feature_activations: Optional[FeatureActivationsModel] = Field(
        default=None, alias="FeatureActivations"
    )
    global_configuration: Optional[GlobalConfigurationModel] = Field(
        default=None, alias="GlobalConfiguration"
    )
    motion_graphics_configuration: Optional[MotionGraphicsConfigurationModel] = Field(
        default=None, alias="MotionGraphicsConfiguration"
    )
    nielsen_configuration: Optional[NielsenConfigurationModel] = Field(
        default=None, alias="NielsenConfiguration"
    )


class BatchScheduleActionCreateRequestModel(BaseModel):
    schedule_actions: Sequence[ScheduleActionModel] = Field(alias="ScheduleActions")


class BatchScheduleActionCreateResultModel(BaseModel):
    schedule_actions: List[ScheduleActionModel] = Field(alias="ScheduleActions")


class BatchScheduleActionDeleteResultModel(BaseModel):
    schedule_actions: List[ScheduleActionModel] = Field(alias="ScheduleActions")


class DescribeScheduleResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schedule_actions: List[ScheduleActionModel] = Field(alias="ScheduleActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChannelModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    cdi_input_specification: Optional[CdiInputSpecificationModel] = Field(
        default=None, alias="CdiInputSpecification"
    )
    channel_class: Optional[Literal["SINGLE_PIPELINE", "STANDARD"]] = Field(
        default=None, alias="ChannelClass"
    )
    destinations: Optional[List[OutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    egress_endpoints: Optional[List[ChannelEgressEndpointModel]] = Field(
        default=None, alias="EgressEndpoints"
    )
    encoder_settings: Optional[EncoderSettingsModel] = Field(
        default=None, alias="EncoderSettings"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    input_attachments: Optional[List[InputAttachmentModel]] = Field(
        default=None, alias="InputAttachments"
    )
    input_specification: Optional[InputSpecificationModel] = Field(
        default=None, alias="InputSpecification"
    )
    log_level: Optional[
        Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
    ] = Field(default=None, alias="LogLevel")
    maintenance: Optional[MaintenanceStatusModel] = Field(
        default=None, alias="Maintenance"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pipeline_details: Optional[List[PipelineDetailModel]] = Field(
        default=None, alias="PipelineDetails"
    )
    pipelines_running_count: Optional[int] = Field(
        default=None, alias="PipelinesRunningCount"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "IDLE",
            "RECOVERING",
            "RUNNING",
            "STARTING",
            "STOPPING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    vpc: Optional[VpcOutputSettingsDescriptionModel] = Field(default=None, alias="Vpc")


class CreateChannelRequestModel(BaseModel):
    cdi_input_specification: Optional[CdiInputSpecificationModel] = Field(
        default=None, alias="CdiInputSpecification"
    )
    channel_class: Optional[Literal["SINGLE_PIPELINE", "STANDARD"]] = Field(
        default=None, alias="ChannelClass"
    )
    destinations: Optional[Sequence[OutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    encoder_settings: Optional[EncoderSettingsModel] = Field(
        default=None, alias="EncoderSettings"
    )
    input_attachments: Optional[Sequence[InputAttachmentModel]] = Field(
        default=None, alias="InputAttachments"
    )
    input_specification: Optional[InputSpecificationModel] = Field(
        default=None, alias="InputSpecification"
    )
    log_level: Optional[
        Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
    ] = Field(default=None, alias="LogLevel")
    maintenance: Optional[MaintenanceCreateSettingsModel] = Field(
        default=None, alias="Maintenance"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    reserved: Optional[str] = Field(default=None, alias="Reserved")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    vpc: Optional[VpcOutputSettingsModel] = Field(default=None, alias="Vpc")


class DeleteChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cdi_input_specification: CdiInputSpecificationModel = Field(
        alias="CdiInputSpecification"
    )
    channel_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="ChannelClass")
    destinations: List[OutputDestinationModel] = Field(alias="Destinations")
    egress_endpoints: List[ChannelEgressEndpointModel] = Field(alias="EgressEndpoints")
    encoder_settings: EncoderSettingsModel = Field(alias="EncoderSettings")
    id: str = Field(alias="Id")
    input_attachments: List[InputAttachmentModel] = Field(alias="InputAttachments")
    input_specification: InputSpecificationModel = Field(alias="InputSpecification")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"] = Field(
        alias="LogLevel"
    )
    maintenance: MaintenanceStatusModel = Field(alias="Maintenance")
    name: str = Field(alias="Name")
    pipeline_details: List[PipelineDetailModel] = Field(alias="PipelineDetails")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    role_arn: str = Field(alias="RoleArn")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc: VpcOutputSettingsDescriptionModel = Field(alias="Vpc")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cdi_input_specification: CdiInputSpecificationModel = Field(
        alias="CdiInputSpecification"
    )
    channel_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="ChannelClass")
    destinations: List[OutputDestinationModel] = Field(alias="Destinations")
    egress_endpoints: List[ChannelEgressEndpointModel] = Field(alias="EgressEndpoints")
    encoder_settings: EncoderSettingsModel = Field(alias="EncoderSettings")
    id: str = Field(alias="Id")
    input_attachments: List[InputAttachmentModel] = Field(alias="InputAttachments")
    input_specification: InputSpecificationModel = Field(alias="InputSpecification")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"] = Field(
        alias="LogLevel"
    )
    maintenance: MaintenanceStatusModel = Field(alias="Maintenance")
    name: str = Field(alias="Name")
    pipeline_details: List[PipelineDetailModel] = Field(alias="PipelineDetails")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    role_arn: str = Field(alias="RoleArn")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc: VpcOutputSettingsDescriptionModel = Field(alias="Vpc")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cdi_input_specification: CdiInputSpecificationModel = Field(
        alias="CdiInputSpecification"
    )
    channel_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="ChannelClass")
    destinations: List[OutputDestinationModel] = Field(alias="Destinations")
    egress_endpoints: List[ChannelEgressEndpointModel] = Field(alias="EgressEndpoints")
    encoder_settings: EncoderSettingsModel = Field(alias="EncoderSettings")
    id: str = Field(alias="Id")
    input_attachments: List[InputAttachmentModel] = Field(alias="InputAttachments")
    input_specification: InputSpecificationModel = Field(alias="InputSpecification")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"] = Field(
        alias="LogLevel"
    )
    maintenance: MaintenanceStatusModel = Field(alias="Maintenance")
    name: str = Field(alias="Name")
    pipeline_details: List[PipelineDetailModel] = Field(alias="PipelineDetails")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    role_arn: str = Field(alias="RoleArn")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc: VpcOutputSettingsDescriptionModel = Field(alias="Vpc")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cdi_input_specification: CdiInputSpecificationModel = Field(
        alias="CdiInputSpecification"
    )
    channel_class: Literal["SINGLE_PIPELINE", "STANDARD"] = Field(alias="ChannelClass")
    destinations: List[OutputDestinationModel] = Field(alias="Destinations")
    egress_endpoints: List[ChannelEgressEndpointModel] = Field(alias="EgressEndpoints")
    encoder_settings: EncoderSettingsModel = Field(alias="EncoderSettings")
    id: str = Field(alias="Id")
    input_attachments: List[InputAttachmentModel] = Field(alias="InputAttachments")
    input_specification: InputSpecificationModel = Field(alias="InputSpecification")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"] = Field(
        alias="LogLevel"
    )
    maintenance: MaintenanceStatusModel = Field(alias="Maintenance")
    name: str = Field(alias="Name")
    pipeline_details: List[PipelineDetailModel] = Field(alias="PipelineDetails")
    pipelines_running_count: int = Field(alias="PipelinesRunningCount")
    role_arn: str = Field(alias="RoleArn")
    state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETED",
        "DELETING",
        "IDLE",
        "RECOVERING",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc: VpcOutputSettingsDescriptionModel = Field(alias="Vpc")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    cdi_input_specification: Optional[CdiInputSpecificationModel] = Field(
        default=None, alias="CdiInputSpecification"
    )
    destinations: Optional[Sequence[OutputDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    encoder_settings: Optional[EncoderSettingsModel] = Field(
        default=None, alias="EncoderSettings"
    )
    input_attachments: Optional[Sequence[InputAttachmentModel]] = Field(
        default=None, alias="InputAttachments"
    )
    input_specification: Optional[InputSpecificationModel] = Field(
        default=None, alias="InputSpecification"
    )
    log_level: Optional[
        Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
    ] = Field(default=None, alias="LogLevel")
    maintenance: Optional[MaintenanceUpdateSettingsModel] = Field(
        default=None, alias="Maintenance"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class BatchUpdateScheduleRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    creates: Optional[BatchScheduleActionCreateRequestModel] = Field(
        default=None, alias="Creates"
    )
    deletes: Optional[BatchScheduleActionDeleteRequestModel] = Field(
        default=None, alias="Deletes"
    )


class BatchUpdateScheduleResponseModel(BaseModel):
    creates: BatchScheduleActionCreateResultModel = Field(alias="Creates")
    deletes: BatchScheduleActionDeleteResultModel = Field(alias="Deletes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelClassResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
