# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssetShallowModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    id: Optional[str] = Field(default=None, alias="Id")
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    source_role_arn: Optional[str] = Field(default=None, alias="SourceRoleArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class AuthorizationModel(BaseModel):
    cdn_identifier_secret: str = Field(alias="CdnIdentifierSecret")
    secrets_role_arn: str = Field(alias="SecretsRoleArn")


class EgressAccessLogsModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateAssetRequestModel(BaseModel):
    id: str = Field(alias="Id")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    source_arn: str = Field(alias="SourceArn")
    source_role_arn: str = Field(alias="SourceRoleArn")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class EgressEndpointModel(BaseModel):
    packaging_configuration_id: Optional[str] = Field(
        default=None, alias="PackagingConfigurationId"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    url: Optional[str] = Field(default=None, alias="Url")


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


class DeleteAssetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeletePackagingConfigurationRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeletePackagingGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeAssetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribePackagingConfigurationRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribePackagingGroupRequestModel(BaseModel):
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


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAssetsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")


class ListPackagingConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")


class ListPackagingGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdatePackagingGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )


class ConfigureLogsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    egress_access_logs: Optional[EgressAccessLogsModel] = Field(
        default=None, alias="EgressAccessLogs"
    )


class CreatePackagingGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )
    egress_access_logs: Optional[EgressAccessLogsModel] = Field(
        default=None, alias="EgressAccessLogs"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class PackagingGroupModel(BaseModel):
    approximate_asset_count: Optional[int] = Field(
        default=None, alias="ApproximateAssetCount"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    authorization: Optional[AuthorizationModel] = Field(
        default=None, alias="Authorization"
    )
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    egress_access_logs: Optional[EgressAccessLogsModel] = Field(
        default=None, alias="EgressAccessLogs"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ConfigureLogsResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    domain_name: str = Field(alias="DomainName")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    id: str = Field(alias="Id")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePackagingGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    domain_name: str = Field(alias="DomainName")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    id: str = Field(alias="Id")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackagingGroupResponseModel(BaseModel):
    approximate_asset_count: int = Field(alias="ApproximateAssetCount")
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    domain_name: str = Field(alias="DomainName")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    id: str = Field(alias="Id")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetsResponseModel(BaseModel):
    assets: List[AssetShallowModel] = Field(alias="Assets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePackagingGroupResponseModel(BaseModel):
    approximate_asset_count: int = Field(alias="ApproximateAssetCount")
    arn: str = Field(alias="Arn")
    authorization: AuthorizationModel = Field(alias="Authorization")
    domain_name: str = Field(alias="DomainName")
    egress_access_logs: EgressAccessLogsModel = Field(alias="EgressAccessLogs")
    id: str = Field(alias="Id")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: str = Field(alias="CreatedAt")
    egress_endpoints: List[EgressEndpointModel] = Field(alias="EgressEndpoints")
    id: str = Field(alias="Id")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    resource_id: str = Field(alias="ResourceId")
    source_arn: str = Field(alias="SourceArn")
    source_role_arn: str = Field(alias="SourceRoleArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: str = Field(alias="CreatedAt")
    egress_endpoints: List[EgressEndpointModel] = Field(alias="EgressEndpoints")
    id: str = Field(alias="Id")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    resource_id: str = Field(alias="ResourceId")
    source_arn: str = Field(alias="SourceArn")
    source_role_arn: str = Field(alias="SourceRoleArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DashManifestModel(BaseModel):
    manifest_layout: Optional[Literal["COMPACT", "FULL"]] = Field(
        default=None, alias="ManifestLayout"
    )
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    min_buffer_time_seconds: Optional[int] = Field(
        default=None, alias="MinBufferTimeSeconds"
    )
    profile: Optional[Literal["HBBTV_1_5", "NONE"]] = Field(
        default=None, alias="Profile"
    )
    scte_markers_source: Optional[Literal["MANIFEST", "SEGMENTS"]] = Field(
        default=None, alias="ScteMarkersSource"
    )
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class HlsManifestModel(BaseModel):
    ad_markers: Optional[Literal["NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]] = Field(
        default=None, alias="AdMarkers"
    )
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    program_date_time_interval_seconds: Optional[int] = Field(
        default=None, alias="ProgramDateTimeIntervalSeconds"
    )
    repeat_ext_xkey: Optional[bool] = Field(default=None, alias="RepeatExtXKey")
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class MssManifestModel(BaseModel):
    manifest_name: Optional[str] = Field(default=None, alias="ManifestName")
    stream_selection: Optional[StreamSelectionModel] = Field(
        default=None, alias="StreamSelection"
    )


class SpekeKeyProviderModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    system_ids: Sequence[str] = Field(alias="SystemIds")
    url: str = Field(alias="Url")
    encryption_contract_configuration: Optional[
        EncryptionContractConfigurationModel
    ] = Field(default=None, alias="EncryptionContractConfiguration")


class ListAssetsRequestListAssetsPaginateModel(BaseModel):
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateModel(
    BaseModel
):
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackagingGroupsRequestListPackagingGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackagingGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    packaging_groups: List[PackagingGroupModel] = Field(alias="PackagingGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CmafEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )


class DashEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")


class HlsEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    encryption_method: Optional[Literal["AES_128", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionMethod"
    )


class MssEncryptionModel(BaseModel):
    speke_key_provider: SpekeKeyProviderModel = Field(alias="SpekeKeyProvider")


class CmafPackageModel(BaseModel):
    hls_manifests: Sequence[HlsManifestModel] = Field(alias="HlsManifests")
    encryption: Optional[CmafEncryptionModel] = Field(default=None, alias="Encryption")
    include_encoder_configuration_in_segments: Optional[bool] = Field(
        default=None, alias="IncludeEncoderConfigurationInSegments"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )


class DashPackageModel(BaseModel):
    dash_manifests: Sequence[DashManifestModel] = Field(alias="DashManifests")
    encryption: Optional[DashEncryptionModel] = Field(default=None, alias="Encryption")
    include_encoder_configuration_in_segments: Optional[bool] = Field(
        default=None, alias="IncludeEncoderConfigurationInSegments"
    )
    include_iframe_only_stream: Optional[bool] = Field(
        default=None, alias="IncludeIframeOnlyStream"
    )
    period_triggers: Optional[Sequence[Literal["ADS"]]] = Field(
        default=None, alias="PeriodTriggers"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    segment_template_format: Optional[
        Literal["NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"]
    ] = Field(default=None, alias="SegmentTemplateFormat")


class HlsPackageModel(BaseModel):
    hls_manifests: Sequence[HlsManifestModel] = Field(alias="HlsManifests")
    encryption: Optional[HlsEncryptionModel] = Field(default=None, alias="Encryption")
    include_dvb_subtitles: Optional[bool] = Field(
        default=None, alias="IncludeDvbSubtitles"
    )
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )
    use_audio_rendition_group: Optional[bool] = Field(
        default=None, alias="UseAudioRenditionGroup"
    )


class MssPackageModel(BaseModel):
    mss_manifests: Sequence[MssManifestModel] = Field(alias="MssManifests")
    encryption: Optional[MssEncryptionModel] = Field(default=None, alias="Encryption")
    segment_duration_seconds: Optional[int] = Field(
        default=None, alias="SegmentDurationSeconds"
    )


class CreatePackagingConfigurationRequestModel(BaseModel):
    id: str = Field(alias="Id")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    cmaf_package: Optional[CmafPackageModel] = Field(default=None, alias="CmafPackage")
    dash_package: Optional[DashPackageModel] = Field(default=None, alias="DashPackage")
    hls_package: Optional[HlsPackageModel] = Field(default=None, alias="HlsPackage")
    mss_package: Optional[MssPackageModel] = Field(default=None, alias="MssPackage")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreatePackagingConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cmaf_package: CmafPackageModel = Field(alias="CmafPackage")
    dash_package: DashPackageModel = Field(alias="DashPackage")
    hls_package: HlsPackageModel = Field(alias="HlsPackage")
    id: str = Field(alias="Id")
    mss_package: MssPackageModel = Field(alias="MssPackage")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackagingConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    cmaf_package: CmafPackageModel = Field(alias="CmafPackage")
    dash_package: DashPackageModel = Field(alias="DashPackage")
    hls_package: HlsPackageModel = Field(alias="HlsPackage")
    id: str = Field(alias="Id")
    mss_package: MssPackageModel = Field(alias="MssPackage")
    packaging_group_id: str = Field(alias="PackagingGroupId")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PackagingConfigurationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    cmaf_package: Optional[CmafPackageModel] = Field(default=None, alias="CmafPackage")
    dash_package: Optional[DashPackageModel] = Field(default=None, alias="DashPackage")
    hls_package: Optional[HlsPackageModel] = Field(default=None, alias="HlsPackage")
    id: Optional[str] = Field(default=None, alias="Id")
    mss_package: Optional[MssPackageModel] = Field(default=None, alias="MssPackage")
    packaging_group_id: Optional[str] = Field(default=None, alias="PackagingGroupId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListPackagingConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    packaging_configurations: List[PackagingConfigurationModel] = Field(
        alias="PackagingConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
