# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AuthorizationModel(BaseModel):
    cdn_identifier_secret: str = Field(alias="CdnIdentifierSecret")
    secrets_role_arn: str = Field(alias="SecretsRoleArn")


class EgressAccessLogsModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")


class IngressAccessLogsModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")


class HlsManifestCreateOrUpdateParametersModel(BaseModel):
    id: str = Field(alias="Id")
    ad_markers: Optional[
        Literal["DATERANGE", "NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
    ] = Field(default=None, alias="AdMarkers")
    ad_triggers: Optional[
        Sequence[
            Literal[
                "BREAK",
                "DISTRIBUTOR_ADVERTISEMENT",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_ADVERTISEMENT",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "SPLICE_INSERT",
            ]
        ]
    ] = Field(default=None, alias="AdTriggers")
    ads_on_delivery_restrictions: Optional[
        Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
    ] = Field(default=None, alias="AdsOnDeliveryRestrictions")
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    playlist_type: Optional[Literal["EVENT", "NONE", "VOD"]] = Field(
        default=None, alias="PlaylistType"
    )
    playlist_window_seconds: Optional[int] = Field(
        default=None, alias="PlaylistWindowSeconds"
    )
    program_date_time_interval_seconds: Optional[int] = Field(
        default=None, alias="ProgramDateTimeIntervalSeconds"
    )


class StreamSelectionModel(BaseModel):
    max_video_bits_per_second: Optional[int] = Field(
        default=None, alias="MaxVideoBitsPerSecond"
    )
    min_video_bits_per_second: Optional[int] = Field(
        default=None, alias="MinVideoBitsPerSecond"
    )
    stream_order: Optional[
        Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"]
    ] = Field(default=None, alias="StreamOrder")


class HlsManifestModel(BaseModel):
    id: str = Field(alias="Id")
    ad_markers: Optional[
        Literal["DATERANGE", "NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
    ] = Field(default=None, alias="AdMarkers")
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    playlist_type: Optional[Literal["EVENT", "NONE", "VOD"]] = Field(
        default=None, alias="PlaylistType"
    )
    playlist_window_seconds: Optional[int] = Field(
        default=None, alias="PlaylistWindowSeconds"
    )
    program_date_time_interval_seconds: Optional[int] = Field(
        default=None, alias="ProgramDateTimeIntervalSeconds"
    )
    url: Optional[str] = Field(default=None, alias="Url")
    ad_triggers: Optional[
        List[
            Literal[
                "BREAK",
                "DISTRIBUTOR_ADVERTISEMENT",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_ADVERTISEMENT",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "SPLICE_INSERT",
            ]
        ]
    ] = Field(default=None, alias="AdTriggers")
    ads_on_delivery_restrictions: Optional[
        Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
    ] = Field(default=None, alias="AdsOnDeliveryRestrictions")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateChannelRequestModel(BaseModel):
    id: str = Field(alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class S3DestinationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    manifest_key: str = Field(alias="ManifestKey")
    role_arn: str = Field(alias="RoleArn")


class DeleteChannelRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteOriginEndpointRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeChannelRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeHarvestJobRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeOriginEndpointRequestModel(BaseModel):
    id: str = Field(alias="Id")


class EncryptionContractConfigurationModel(BaseModel):
    preset_speke20_audio: Literal[
        "PRESET-AUDIO-1", "PRESET-AUDIO-2", "PRESET-AUDIO-3", "SHARED", "UNENCRYPTED"
    ] = Field(alias="PresetSpeke20Audio")
    preset_speke20_video: Literal[
        "PRESET-VIDEO-1",
        "PRESET-VIDEO-2",
        "PRESET-VIDEO-3",
        "PRESET-VIDEO-4",
        "PRESET-VIDEO-5",
        "PRESET-VIDEO-6",
        "PRESET-VIDEO-7",
        "PRESET-VIDEO-8",
        "SHARED",
        "UNENCRYPTED",
    ] = Field(alias="PresetSpeke20Video")


class IngestEndpointModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    password: Optional[str] = Field(default=None, alias="Password")
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListChannelsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHarvestJobsRequestModel(BaseModel):
    include_channel_id: Optional[str] = Field(default=None, alias="IncludeChannelId")
    include_status: Optional[str] = Field(default=None, alias="IncludeStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOriginEndpointsRequestModel(BaseModel):
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RotateChannelCredentialsRequestModel(BaseModel):
    id: str = Field(alias="Id")


class RotateIngestEndpointCredentialsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    ingest_endpoint_id: str = Field(alias="IngestEndpointId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateChannelRequestModel(BaseModel):
    id: str = Field(alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")


class ConfigureLogsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    egress_access_logs: Optional[EgressAccessLogsModel] = Field(
        default=None, alias="EgressAccessLogs"
    )
    ingress_access_logs: Optional[IngressAccessLogsModel] = Field(
        default=None, alias="IngressAccessLogs"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHarvestJobRequestModel(BaseModel):
    end_time: str = Field(alias="EndTime")
    id: str = Field(alias="Id")
    origin_endpoint_id: str = Field(alias="OriginEndpointId")
    s3_destination: S3DestinationModel = Field(alias="S3Destination")
    start_time: str = Field(alias="StartTime")


class CreateHarvestJobResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_id: str = Field(alias="ChannelId")
    created_at: str = Field(alias="CreatedAt")
    end_time: str = Field(alias="EndTime")
    id: str = Field(alias="Id")
    origin_endpoint_id: str = Field(alias="OriginEndpointId")
    s3_destination: S3DestinationModel = Field(alias="S3Destination")
    start_time: str = Field(alias="StartTime")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHarvestJobResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_id: str = Field(alias="ChannelId")
    created_at: str = Field(alias="CreatedAt")
    end_time: str = Field(alias="EndTime")
    id: str = Field(alias="Id")
    origin_endpoint_id: str = Field(alias="OriginEndpointId")
    s3_destination: S3DestinationModel = Field(alias="S3Destination")
    start_time: str = Field(alias="StartTime")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HarvestJobModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    end_time: Optional[str] = Field(default=None, alias="EndTime")
    id: Optional[str] = Field(default=None, alias="Id")
    origin_endpoint_id: Optional[str] = Field(default=None, alias="OriginEndpointId")
    s3_destination: Optional[S3DestinationModel] = Field(
        default=None, alias="S3Destination"
    )
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )


class SpekeKeyProviderModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    role_arn: str = Field(alias="RoleArn")
    system_ids: Sequence[str] = Field(alias="SystemIds")
    url: str = Field(alias="Url")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    encryption_contract_configuration: Optional[
        EncryptionContractConfigurationModel
    ] = Field(default=None, alias="EncryptionContractConfiguration")


class HlsIngestModel(BaseModel):
    ingest_endpoints: Optional[List[IngestEndpointModel]] = Field(
        default=None, alias="IngestEndpoints"
    )


class ListChannelsRequestListChannelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHarvestJobsRequestListHarvestJobsPaginateModel(BaseModel):
    include_channel_id: Optional[str] = Field(default=None, alias="IncludeChannelId")
    include_status: Optional[str] = Field(default=None, alias="IncludeStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOriginEndpointsRequestListOriginEndpointsPaginateModel(BaseModel):
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHarvestJobsResponseModel(BaseModel):
    harvest_jobs: List[HarvestJobModel] = Field(alias="HarvestJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CmafEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    encryption_method: Optional[Literal["AES_CTR", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionMethod"
    )
    key_rotation_interval_seconds: Optional[int] = Field(
        default=None, alias="KeyRotationIntervalSeconds"
    )


class DashEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")
    key_rotation_interval_seconds: Optional[int] = Field(
        default=None, alias="KeyRotationIntervalSeconds"
    )


class HlsEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    encryption_method: Optional[Literal["AES_128", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionMethod"
    )
    key_rotation_interval_seconds: Optional[int] = Field(
        default=None, alias="KeyRotationIntervalSeconds"
    )
    repeat_ext_xkey: Optional[bool] = Field(default=None, alias="RepeatExtXKey")


class MssEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")


class ChannelModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    egress_access_logs: Optional[EgressAccessLogsModel] = Field(
        default=None, alias="EgressAccessLogs"
    )
    hls_ingest: Optional[HlsIngestModel] = Field(default=None, alias="HlsIngest")
    id: Optional[str] = Field(default=None, alias="Id")
    ingress_access_logs: Optional[IngressAccessLogsModel] = Field(
        default=None, alias="IngressAccessLogs"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ConfigureLogsResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateChannelCredentialsResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateIngestEndpointCredentialsResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    hls_ingest: HlsIngestModel = Field(alias="HlsIngest")
    id: str = Field(alias="Id")
    ingress_access_logs: IngressAccessLogsModel = Field(alias="IngressAccessLogs")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CmafPackageCreateOrUpdateParametersModel(BaseModel):
    encryption: Optional[CmafEncryptionModel] = Field(default=None, alias="Encryption")
    hls_manifests: Optional[Sequence[HlsManifestCreateOrUpdateParametersModel]] = Field(
        default=None, alias="HlsManifests"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    segment_prefix: Optional[str] = Field(default=None, alias="SegmentPrefix")
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class CmafPackageModel(BaseModel):
    encryption: Optional[CmafEncryptionModel] = Field(default=None, alias="Encryption")
    hls_manifests: Optional[List[HlsManifestModel]] = Field(
        default=None, alias="HlsManifests"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    segment_prefix: Optional[str] = Field(default=None, alias="SegmentPrefix")
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class DashPackageModel(BaseModel):
    ad_triggers: Optional[
        Sequence[
            Literal[
                "BREAK",
                "DISTRIBUTOR_ADVERTISEMENT",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_ADVERTISEMENT",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "SPLICE_INSERT",
            ]
        ]
    ] = Field(default=None, alias="AdTriggers")
    ads_on_delivery_restrictions: Optional[
        Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
    ] = Field(default=None, alias="AdsOnDeliveryRestrictions")
    encryption: Optional[DashEncryptionModel] = Field(default=None, alias="Encryption")
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    manifest_layout: Optional[Literal["COMPACT", "FULL"]] = Field(
        default=None, alias="ManifestLayout"
    )
    manifest_window_seconds: Optional[int] = Field(
        default=None, alias="ManifestWindowSeconds"
    )
    min_buffer_time_seconds: Optional[int] = Field(
        default=None, alias="MinBufferTimeSeconds"
    )
    min_update_period_seconds: Optional[int] = Field(
        default=None, alias="MinUpdatePeriodSeconds"
    )
    period_triggers: Optional[Sequence[Literal["ADS"]]] = Field(
        default=None, alias="PeriodTriggers"
    )
    profile: Optional[
        Literal["DVB_DASH_2014", "HBBTV_1_5", "HYBRIDCAST", "NONE"]
    ] = Field(default=None, alias="Profile")
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    segment_template_format: Optional[
        Literal["NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"]
    ] = Field(default=None, alias="SegmentTemplateFormat")
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )
    suggested_presentation_delay_seconds: Optional[int] = Field(
        default=None, alias="SuggestedPresentationDelaySeconds"
    )
    utc_timing: Optional[
        Literal["HTTP-HEAD", "HTTP-ISO", "HTTP-XSDATE", "NONE"]
    ] = Field(default=None, alias="UtcTiming")
    utc_timing_uri: Optional[str] = Field(default=None, alias="UtcTimingUri")


class HlsPackageModel(BaseModel):
    ad_markers: Optional[
        Literal["DATERANGE", "NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
    ] = Field(default=None, alias="AdMarkers")
    ad_triggers: Optional[
        Sequence[
            Literal[
                "BREAK",
                "DISTRIBUTOR_ADVERTISEMENT",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_ADVERTISEMENT",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "SPLICE_INSERT",
            ]
        ]
    ] = Field(default=None, alias="AdTriggers")
    ads_on_delivery_restrictions: Optional[
        Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
    ] = Field(default=None, alias="AdsOnDeliveryRestrictions")
    encryption: Optional[HlsEncryptionModel] = Field(default=None, alias="Encryption")
    include_dvb_subtitles: Optional[bool] = Field(
        default=None, alias="IncludeDvbSubtitles"
    )
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    playlist_type: Optional[Literal["EVENT", "NONE", "VOD"]] = Field(
        default=None, alias="PlaylistType"
    )
    playlist_window_seconds: Optional[int] = Field(
        default=None, alias="PlaylistWindowSeconds"
    )
    program_date_time_interval_seconds: Optional[int] = Field(
        default=None, alias="ProgramDateTimeIntervalSeconds"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )
    use_audio_rendition_group: Optional[bool] = Field(
        default=None, alias="UseAudioRenditionGroup"
    )


class MssPackageModel(BaseModel):
    encryption: Optional[MssEncryptionModel] = Field(default=None, alias="Encryption")
    manifest_window_seconds: Optional[int] = Field(
        default=None, alias="ManifestWindowSeconds"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class ListChannelsResponseModel(BaseModel):
    channels: List[ChannelModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOriginEndpointRequestModel(BaseModel):
    channel_id: str = Field(alias="ChannelId")
    id: str = Field(alias="Id")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )
    cmaf_package: Optional[CmafPackageCreateOrUpdateParametersModel] = Field(
        default=None, alias="CmafPackage"
    )
    dash_package: Optional[DashPackageModel] = Field(default=None, alias="DashPackage")
    description: Optional[str] = Field(default=None, alias="Description")
    hls_package: Optional[HlsPackageModel] = Field(default=None, alias="HlsPackage")
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    mss_package: Optional[MssPackageModel] = Field(default=None, alias="MssPackage")
    origination: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="Origination"
    )
    startover_window_seconds: Optional[int] = Field(
        default=None, alias="StartoverWindowSeconds"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    time_delay_seconds: Optional[int] = Field(default=None, alias="TimeDelaySeconds")
    whitelist: Optional[Sequence[str]] = Field(default=None, alias="Whitelist")


class CreateOriginEndpointResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    channel_id: str = Field(alias="ChannelId")
    cmaf_package: CmafPackageModel = Field(alias="CmafPackage")
    dash_package: DashPackageModel = Field(alias="DashPackage")
    description: str = Field(alias="Description")
    hls_package: HlsPackageModel = Field(alias="HlsPackage")
    id: str = Field(alias="Id")
    manifest_name: str = Field(alias="ManifestName")
    mss_package: MssPackageModel = Field(alias="MssPackage")
    origination: Literal["ALLOW", "DENY"] = Field(alias="Origination")
    startover_window_seconds: int = Field(alias="StartoverWindowSeconds")
    tags: Dict[str, str] = Field(alias="Tags")
    time_delay_seconds: int = Field(alias="TimeDelaySeconds")
    url: str = Field(alias="Url")
    whitelist: List[str] = Field(alias="Whitelist")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOriginEndpointResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    channel_id: str = Field(alias="ChannelId")
    cmaf_package: CmafPackageModel = Field(alias="CmafPackage")
    dash_package: DashPackageModel = Field(alias="DashPackage")
    description: str = Field(alias="Description")
    hls_package: HlsPackageModel = Field(alias="HlsPackage")
    id: str = Field(alias="Id")
    manifest_name: str = Field(alias="ManifestName")
    mss_package: MssPackageModel = Field(alias="MssPackage")
    origination: Literal["ALLOW", "DENY"] = Field(alias="Origination")
    startover_window_seconds: int = Field(alias="StartoverWindowSeconds")
    tags: Dict[str, str] = Field(alias="Tags")
    time_delay_seconds: int = Field(alias="TimeDelaySeconds")
    url: str = Field(alias="Url")
    whitelist: List[str] = Field(alias="Whitelist")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginEndpointModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    cmaf_package: Optional[CmafPackageModel] = Field(default=None, alias="CmafPackage")
    dash_package: Optional[DashPackageModel] = Field(default=None, alias="DashPackage")
    description: Optional[str] = Field(default=None, alias="Description")
    hls_package: Optional[HlsPackageModel] = Field(default=None, alias="HlsPackage")
    id: Optional[str] = Field(default=None, alias="Id")
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    mss_package: Optional[MssPackageModel] = Field(default=None, alias="MssPackage")
    origination: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="Origination"
    )
    startover_window_seconds: Optional[int] = Field(
        default=None, alias="StartoverWindowSeconds"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    time_delay_seconds: Optional[int] = Field(default=None, alias="TimeDelaySeconds")
    url: Optional[str] = Field(default=None, alias="Url")
    whitelist: Optional[List[str]] = Field(default=None, alias="Whitelist")


class UpdateOriginEndpointRequestModel(BaseModel):
    id: str = Field(alias="Id")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )
    cmaf_package: Optional[CmafPackageCreateOrUpdateParametersModel] = Field(
        default=None, alias="CmafPackage"
    )
    dash_package: Optional[DashPackageModel] = Field(default=None, alias="DashPackage")
    description: Optional[str] = Field(default=None, alias="Description")
    hls_package: Optional[HlsPackageModel] = Field(default=None, alias="HlsPackage")
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    mss_package: Optional[MssPackageModel] = Field(default=None, alias="MssPackage")
    origination: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="Origination"
    )
    startover_window_seconds: Optional[int] = Field(
        default=None, alias="StartoverWindowSeconds"
    )
    time_delay_seconds: Optional[int] = Field(default=None, alias="TimeDelaySeconds")
    whitelist: Optional[Sequence[str]] = Field(default=None, alias="Whitelist")


class UpdateOriginEndpointResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    channel_id: str = Field(alias="ChannelId")
    cmaf_package: CmafPackageModel = Field(alias="CmafPackage")
    dash_package: DashPackageModel = Field(alias="DashPackage")
    description: str = Field(alias="Description")
    hls_package: HlsPackageModel = Field(alias="HlsPackage")
    id: str = Field(alias="Id")
    manifest_name: str = Field(alias="ManifestName")
    mss_package: MssPackageModel = Field(alias="MssPackage")
    origination: Literal["ALLOW", "DENY"] = Field(alias="Origination")
    startover_window_seconds: int = Field(alias="StartoverWindowSeconds")
    tags: Dict[str, str] = Field(alias="Tags")
    time_delay_seconds: int = Field(alias="TimeDelaySeconds")
    url: str = Field(alias="Url")
    whitelist: List[str] = Field(alias="Whitelist")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOriginEndpointsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    origin_endpoints: List[OriginEndpointModel] = Field(alias="OriginEndpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
