# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class SecretsManagerAccessTokenConfigurationModel(BaseModel):
    header_name: Optional[str] = Field(default=None, alias="HeaderName")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    secret_string_key: Optional[str] = Field(default=None, alias="SecretStringKey")


class SlateSourceModel(BaseModel):
    source_location_name: Optional[str] = Field(
        default=None, alias="SourceLocationName"
    )
    vod_source_name: Optional[str] = Field(default=None, alias="VodSourceName")


class SpliceInsertMessageModel(BaseModel):
    avail_num: Optional[int] = Field(default=None, alias="AvailNum")
    avails_expected: Optional[int] = Field(default=None, alias="AvailsExpected")
    splice_event_id: Optional[int] = Field(default=None, alias="SpliceEventId")
    unique_program_id: Optional[int] = Field(default=None, alias="UniqueProgramId")


class AdMarkerPassthroughModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AlertModel(BaseModel):
    alert_code: str = Field(alias="AlertCode")
    alert_message: str = Field(alias="AlertMessage")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    related_resource_arns: List[str] = Field(alias="RelatedResourceArns")
    resource_arn: str = Field(alias="ResourceArn")


class AvailMatchingCriteriaModel(BaseModel):
    dynamic_variable: str = Field(alias="DynamicVariable")
    operator: Literal["EQUALS"] = Field(alias="Operator")


class AvailSuppressionModel(BaseModel):
    mode: Optional[Literal["BEHIND_LIVE_EDGE", "OFF"]] = Field(
        default=None, alias="Mode"
    )
    value: Optional[str] = Field(default=None, alias="Value")


class BumperModel(BaseModel):
    end_url: Optional[str] = Field(default=None, alias="EndUrl")
    start_url: Optional[str] = Field(default=None, alias="StartUrl")


class CdnConfigurationModel(BaseModel):
    ad_segment_url_prefix: Optional[str] = Field(
        default=None, alias="AdSegmentUrlPrefix"
    )
    content_segment_url_prefix: Optional[str] = Field(
        default=None, alias="ContentSegmentUrlPrefix"
    )


class LogConfigurationForChannelModel(BaseModel):
    log_types: Optional[List[Literal["AS_RUN"]]] = Field(default=None, alias="LogTypes")


class ClipRangeModel(BaseModel):
    end_offset_millis: int = Field(alias="EndOffsetMillis")


class ConfigureLogsForChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    log_types: Sequence[Literal["AS_RUN"]] = Field(alias="LogTypes")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConfigureLogsForPlaybackConfigurationRequestModel(BaseModel):
    percent_enabled: int = Field(alias="PercentEnabled")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")


class HttpPackageConfigurationModel(BaseModel):
    path: str = Field(alias="Path")
    source_group: str = Field(alias="SourceGroup")
    type: Literal["DASH", "HLS"] = Field(alias="Type")


class PrefetchRetrievalModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="EndTime")
    dynamic_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="DynamicVariables"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class DefaultSegmentDeliveryConfigurationModel(BaseModel):
    base_url: Optional[str] = Field(default=None, alias="BaseUrl")


class HttpConfigurationModel(BaseModel):
    base_url: str = Field(alias="BaseUrl")


class SegmentDeliveryConfigurationModel(BaseModel):
    base_url: Optional[str] = Field(default=None, alias="BaseUrl")
    name: Optional[str] = Field(default=None, alias="Name")


class DashConfigurationForPutModel(BaseModel):
    mpd_location: Optional[str] = Field(default=None, alias="MpdLocation")
    origin_manifest_type: Optional[Literal["MULTI_PERIOD", "SINGLE_PERIOD"]] = Field(
        default=None, alias="OriginManifestType"
    )


class DashConfigurationModel(BaseModel):
    manifest_endpoint_prefix: Optional[str] = Field(
        default=None, alias="ManifestEndpointPrefix"
    )
    mpd_location: Optional[str] = Field(default=None, alias="MpdLocation")
    origin_manifest_type: Optional[Literal["MULTI_PERIOD", "SINGLE_PERIOD"]] = Field(
        default=None, alias="OriginManifestType"
    )


class DashPlaylistSettingsModel(BaseModel):
    manifest_window_seconds: Optional[int] = Field(
        default=None, alias="ManifestWindowSeconds"
    )
    min_buffer_time_seconds: Optional[int] = Field(
        default=None, alias="MinBufferTimeSeconds"
    )
    min_update_period_seconds: Optional[int] = Field(
        default=None, alias="MinUpdatePeriodSeconds"
    )
    suggested_presentation_delay_seconds: Optional[int] = Field(
        default=None, alias="SuggestedPresentationDelaySeconds"
    )


class DeleteChannelPolicyRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class DeleteChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class DeleteLiveSourceRequestModel(BaseModel):
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")


class DeletePlaybackConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeletePrefetchScheduleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")


class DeleteProgramRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    program_name: str = Field(alias="ProgramName")


class DeleteSourceLocationRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")


class DeleteVodSourceRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")


class DescribeChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class DescribeLiveSourceRequestModel(BaseModel):
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")


class DescribeProgramRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    program_name: str = Field(alias="ProgramName")


class DescribeSourceLocationRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")


class DescribeVodSourceRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")


class GetChannelPolicyRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetChannelScheduleRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    duration_minutes: Optional[str] = Field(default=None, alias="DurationMinutes")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetPlaybackConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class HlsConfigurationModel(BaseModel):
    manifest_endpoint_prefix: Optional[str] = Field(
        default=None, alias="ManifestEndpointPrefix"
    )


class LivePreRollConfigurationModel(BaseModel):
    ad_decision_server_url: Optional[str] = Field(
        default=None, alias="AdDecisionServerUrl"
    )
    max_duration_seconds: Optional[int] = Field(
        default=None, alias="MaxDurationSeconds"
    )


class LogConfigurationModel(BaseModel):
    percent_enabled: int = Field(alias="PercentEnabled")


class GetPrefetchScheduleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")


class HlsPlaylistSettingsModel(BaseModel):
    manifest_window_seconds: Optional[int] = Field(
        default=None, alias="ManifestWindowSeconds"
    )


class ListAlertsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLiveSourcesRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPlaybackConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPrefetchSchedulesRequestModel(BaseModel):
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")


class ListSourceLocationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListVodSourcesRequestModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PutChannelPolicyRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    policy: str = Field(alias="Policy")


class ScheduleAdBreakModel(BaseModel):
    approximate_duration_seconds: Optional[int] = Field(
        default=None, alias="ApproximateDurationSeconds"
    )
    approximate_start_time: Optional[datetime] = Field(
        default=None, alias="ApproximateStartTime"
    )
    source_location_name: Optional[str] = Field(
        default=None, alias="SourceLocationName"
    )
    vod_source_name: Optional[str] = Field(default=None, alias="VodSourceName")


class TransitionModel(BaseModel):
    relative_position: Literal["AFTER_PROGRAM", "BEFORE_PROGRAM"] = Field(
        alias="RelativePosition"
    )
    type: str = Field(alias="Type")
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    relative_program: Optional[str] = Field(default=None, alias="RelativeProgram")
    scheduled_start_time_millis: Optional[int] = Field(
        default=None, alias="ScheduledStartTimeMillis"
    )


class SegmentationDescriptorModel(BaseModel):
    segment_num: Optional[int] = Field(default=None, alias="SegmentNum")
    segmentation_event_id: Optional[int] = Field(
        default=None, alias="SegmentationEventId"
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


class StartChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class StopChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateProgramTransitionModel(BaseModel):
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    scheduled_start_time_millis: Optional[int] = Field(
        default=None, alias="ScheduledStartTimeMillis"
    )


class AccessConfigurationModel(BaseModel):
    access_type: Optional[Literal["S3_SIGV4", "SECRETS_MANAGER_ACCESS_TOKEN"]] = Field(
        default=None, alias="AccessType"
    )
    secrets_manager_access_token_configuration: Optional[
        SecretsManagerAccessTokenConfigurationModel
    ] = Field(default=None, alias="SecretsManagerAccessTokenConfiguration")


class ManifestProcessingRulesModel(BaseModel):
    ad_marker_passthrough: Optional[AdMarkerPassthroughModel] = Field(
        default=None, alias="AdMarkerPassthrough"
    )


class PrefetchConsumptionModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="EndTime")
    avail_matching_criteria: Optional[Sequence[AvailMatchingCriteriaModel]] = Field(
        default=None, alias="AvailMatchingCriteria"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class ConfigureLogsForChannelResponseModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    log_types: List[Literal["AS_RUN"]] = Field(alias="LogTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigureLogsForPlaybackConfigurationResponseModel(BaseModel):
    percent_enabled: int = Field(alias="PercentEnabled")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAlertsResponseModel(BaseModel):
    items: List[AlertModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLiveSourceRequestModel(BaseModel):
    http_package_configurations: Sequence[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateLiveSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVodSourceRequestModel(BaseModel):
    http_package_configurations: Sequence[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateVodSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLiveSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVodSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LiveSourceModel(BaseModel):
    arn: str = Field(alias="Arn")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateLiveSourceRequestModel(BaseModel):
    http_package_configurations: Sequence[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")


class UpdateLiveSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    live_source_name: str = Field(alias="LiveSourceName")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVodSourceRequestModel(BaseModel):
    http_package_configurations: Sequence[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")


class UpdateVodSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VodSourceModel(BaseModel):
    arn: str = Field(alias="Arn")
    http_package_configurations: List[HttpPackageConfigurationModel] = Field(
        alias="HttpPackageConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetChannelScheduleRequestGetChannelSchedulePaginateModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    duration_minutes: Optional[str] = Field(default=None, alias="DurationMinutes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAlertsRequestListAlertsPaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListChannelsRequestListChannelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLiveSourcesRequestListLiveSourcesPaginateModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateModel(BaseModel):
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSourceLocationsRequestListSourceLocationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVodSourcesRequestListVodSourcesPaginateModel(BaseModel):
    source_location_name: str = Field(alias="SourceLocationName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RequestOutputItemModel(BaseModel):
    manifest_name: str = Field(alias="ManifestName")
    source_group: str = Field(alias="SourceGroup")
    dash_playlist_settings: Optional[DashPlaylistSettingsModel] = Field(
        default=None, alias="DashPlaylistSettings"
    )
    hls_playlist_settings: Optional[HlsPlaylistSettingsModel] = Field(
        default=None, alias="HlsPlaylistSettings"
    )


class ResponseOutputItemModel(BaseModel):
    manifest_name: str = Field(alias="ManifestName")
    playback_url: str = Field(alias="PlaybackUrl")
    source_group: str = Field(alias="SourceGroup")
    dash_playlist_settings: Optional[DashPlaylistSettingsModel] = Field(
        default=None, alias="DashPlaylistSettings"
    )
    hls_playlist_settings: Optional[HlsPlaylistSettingsModel] = Field(
        default=None, alias="HlsPlaylistSettings"
    )


class ScheduleEntryModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    program_name: str = Field(alias="ProgramName")
    source_location_name: str = Field(alias="SourceLocationName")
    approximate_duration_seconds: Optional[int] = Field(
        default=None, alias="ApproximateDurationSeconds"
    )
    approximate_start_time: Optional[datetime] = Field(
        default=None, alias="ApproximateStartTime"
    )
    live_source_name: Optional[str] = Field(default=None, alias="LiveSourceName")
    schedule_ad_breaks: Optional[List[ScheduleAdBreakModel]] = Field(
        default=None, alias="ScheduleAdBreaks"
    )
    schedule_entry_type: Optional[Literal["FILLER_SLATE", "PROGRAM"]] = Field(
        default=None, alias="ScheduleEntryType"
    )
    vod_source_name: Optional[str] = Field(default=None, alias="VodSourceName")


class ScheduleConfigurationModel(BaseModel):
    transition: TransitionModel = Field(alias="Transition")
    clip_range: Optional[ClipRangeModel] = Field(default=None, alias="ClipRange")


class TimeSignalMessageModel(BaseModel):
    segmentation_descriptors: Optional[Sequence[SegmentationDescriptorModel]] = Field(
        default=None, alias="SegmentationDescriptors"
    )


class UpdateProgramScheduleConfigurationModel(BaseModel):
    clip_range: Optional[ClipRangeModel] = Field(default=None, alias="ClipRange")
    transition: Optional[UpdateProgramTransitionModel] = Field(
        default=None, alias="Transition"
    )


class CreateSourceLocationRequestModel(BaseModel):
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    source_location_name: str = Field(alias="SourceLocationName")
    access_configuration: Optional[AccessConfigurationModel] = Field(
        default=None, alias="AccessConfiguration"
    )
    default_segment_delivery_configuration: Optional[
        DefaultSegmentDeliveryConfigurationModel
    ] = Field(default=None, alias="DefaultSegmentDeliveryConfiguration")
    segment_delivery_configurations: Optional[
        Sequence[SegmentDeliveryConfigurationModel]
    ] = Field(default=None, alias="SegmentDeliveryConfigurations")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateSourceLocationResponseModel(BaseModel):
    access_configuration: AccessConfigurationModel = Field(alias="AccessConfiguration")
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    default_segment_delivery_configuration: DefaultSegmentDeliveryConfigurationModel = (
        Field(alias="DefaultSegmentDeliveryConfiguration")
    )
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    segment_delivery_configurations: List[SegmentDeliveryConfigurationModel] = Field(
        alias="SegmentDeliveryConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSourceLocationResponseModel(BaseModel):
    access_configuration: AccessConfigurationModel = Field(alias="AccessConfiguration")
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    default_segment_delivery_configuration: DefaultSegmentDeliveryConfigurationModel = (
        Field(alias="DefaultSegmentDeliveryConfiguration")
    )
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    segment_delivery_configurations: List[SegmentDeliveryConfigurationModel] = Field(
        alias="SegmentDeliveryConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceLocationModel(BaseModel):
    arn: str = Field(alias="Arn")
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    source_location_name: str = Field(alias="SourceLocationName")
    access_configuration: Optional[AccessConfigurationModel] = Field(
        default=None, alias="AccessConfiguration"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    default_segment_delivery_configuration: Optional[
        DefaultSegmentDeliveryConfigurationModel
    ] = Field(default=None, alias="DefaultSegmentDeliveryConfiguration")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    segment_delivery_configurations: Optional[
        List[SegmentDeliveryConfigurationModel]
    ] = Field(default=None, alias="SegmentDeliveryConfigurations")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateSourceLocationRequestModel(BaseModel):
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    source_location_name: str = Field(alias="SourceLocationName")
    access_configuration: Optional[AccessConfigurationModel] = Field(
        default=None, alias="AccessConfiguration"
    )
    default_segment_delivery_configuration: Optional[
        DefaultSegmentDeliveryConfigurationModel
    ] = Field(default=None, alias="DefaultSegmentDeliveryConfiguration")
    segment_delivery_configurations: Optional[
        Sequence[SegmentDeliveryConfigurationModel]
    ] = Field(default=None, alias="SegmentDeliveryConfigurations")


class UpdateSourceLocationResponseModel(BaseModel):
    access_configuration: AccessConfigurationModel = Field(alias="AccessConfiguration")
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    default_segment_delivery_configuration: DefaultSegmentDeliveryConfigurationModel = (
        Field(alias="DefaultSegmentDeliveryConfiguration")
    )
    http_configuration: HttpConfigurationModel = Field(alias="HttpConfiguration")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    segment_delivery_configurations: List[SegmentDeliveryConfigurationModel] = Field(
        alias="SegmentDeliveryConfigurations"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPlaybackConfigurationResponseModel(BaseModel):
    ad_decision_server_url: str = Field(alias="AdDecisionServerUrl")
    avail_suppression: AvailSuppressionModel = Field(alias="AvailSuppression")
    bumper: BumperModel = Field(alias="Bumper")
    cdn_configuration: CdnConfigurationModel = Field(alias="CdnConfiguration")
    configuration_aliases: Dict[str, Dict[str, str]] = Field(
        alias="ConfigurationAliases"
    )
    dash_configuration: DashConfigurationModel = Field(alias="DashConfiguration")
    hls_configuration: HlsConfigurationModel = Field(alias="HlsConfiguration")
    live_pre_roll_configuration: LivePreRollConfigurationModel = Field(
        alias="LivePreRollConfiguration"
    )
    log_configuration: LogConfigurationModel = Field(alias="LogConfiguration")
    manifest_processing_rules: ManifestProcessingRulesModel = Field(
        alias="ManifestProcessingRules"
    )
    name: str = Field(alias="Name")
    personalization_threshold_seconds: int = Field(
        alias="PersonalizationThresholdSeconds"
    )
    playback_configuration_arn: str = Field(alias="PlaybackConfigurationArn")
    playback_endpoint_prefix: str = Field(alias="PlaybackEndpointPrefix")
    session_initialization_endpoint_prefix: str = Field(
        alias="SessionInitializationEndpointPrefix"
    )
    slate_ad_url: str = Field(alias="SlateAdUrl")
    tags: Dict[str, str] = Field(alias="Tags")
    transcode_profile_name: str = Field(alias="TranscodeProfileName")
    video_content_source_url: str = Field(alias="VideoContentSourceUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PlaybackConfigurationModel(BaseModel):
    ad_decision_server_url: Optional[str] = Field(
        default=None, alias="AdDecisionServerUrl"
    )
    avail_suppression: Optional[AvailSuppressionModel] = Field(
        default=None, alias="AvailSuppression"
    )
    bumper: Optional[BumperModel] = Field(default=None, alias="Bumper")
    cdn_configuration: Optional[CdnConfigurationModel] = Field(
        default=None, alias="CdnConfiguration"
    )
    configuration_aliases: Optional[Dict[str, Dict[str, str]]] = Field(
        default=None, alias="ConfigurationAliases"
    )
    dash_configuration: Optional[DashConfigurationModel] = Field(
        default=None, alias="DashConfiguration"
    )
    hls_configuration: Optional[HlsConfigurationModel] = Field(
        default=None, alias="HlsConfiguration"
    )
    live_pre_roll_configuration: Optional[LivePreRollConfigurationModel] = Field(
        default=None, alias="LivePreRollConfiguration"
    )
    log_configuration: Optional[LogConfigurationModel] = Field(
        default=None, alias="LogConfiguration"
    )
    manifest_processing_rules: Optional[ManifestProcessingRulesModel] = Field(
        default=None, alias="ManifestProcessingRules"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    personalization_threshold_seconds: Optional[int] = Field(
        default=None, alias="PersonalizationThresholdSeconds"
    )
    playback_configuration_arn: Optional[str] = Field(
        default=None, alias="PlaybackConfigurationArn"
    )
    playback_endpoint_prefix: Optional[str] = Field(
        default=None, alias="PlaybackEndpointPrefix"
    )
    session_initialization_endpoint_prefix: Optional[str] = Field(
        default=None, alias="SessionInitializationEndpointPrefix"
    )
    slate_ad_url: Optional[str] = Field(default=None, alias="SlateAdUrl")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    transcode_profile_name: Optional[str] = Field(
        default=None, alias="TranscodeProfileName"
    )
    video_content_source_url: Optional[str] = Field(
        default=None, alias="VideoContentSourceUrl"
    )


class PutPlaybackConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    ad_decision_server_url: Optional[str] = Field(
        default=None, alias="AdDecisionServerUrl"
    )
    avail_suppression: Optional[AvailSuppressionModel] = Field(
        default=None, alias="AvailSuppression"
    )
    bumper: Optional[BumperModel] = Field(default=None, alias="Bumper")
    cdn_configuration: Optional[CdnConfigurationModel] = Field(
        default=None, alias="CdnConfiguration"
    )
    configuration_aliases: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="ConfigurationAliases"
    )
    dash_configuration: Optional[DashConfigurationForPutModel] = Field(
        default=None, alias="DashConfiguration"
    )
    live_pre_roll_configuration: Optional[LivePreRollConfigurationModel] = Field(
        default=None, alias="LivePreRollConfiguration"
    )
    manifest_processing_rules: Optional[ManifestProcessingRulesModel] = Field(
        default=None, alias="ManifestProcessingRules"
    )
    personalization_threshold_seconds: Optional[int] = Field(
        default=None, alias="PersonalizationThresholdSeconds"
    )
    slate_ad_url: Optional[str] = Field(default=None, alias="SlateAdUrl")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    transcode_profile_name: Optional[str] = Field(
        default=None, alias="TranscodeProfileName"
    )
    video_content_source_url: Optional[str] = Field(
        default=None, alias="VideoContentSourceUrl"
    )


class PutPlaybackConfigurationResponseModel(BaseModel):
    ad_decision_server_url: str = Field(alias="AdDecisionServerUrl")
    avail_suppression: AvailSuppressionModel = Field(alias="AvailSuppression")
    bumper: BumperModel = Field(alias="Bumper")
    cdn_configuration: CdnConfigurationModel = Field(alias="CdnConfiguration")
    configuration_aliases: Dict[str, Dict[str, str]] = Field(
        alias="ConfigurationAliases"
    )
    dash_configuration: DashConfigurationModel = Field(alias="DashConfiguration")
    hls_configuration: HlsConfigurationModel = Field(alias="HlsConfiguration")
    live_pre_roll_configuration: LivePreRollConfigurationModel = Field(
        alias="LivePreRollConfiguration"
    )
    log_configuration: LogConfigurationModel = Field(alias="LogConfiguration")
    manifest_processing_rules: ManifestProcessingRulesModel = Field(
        alias="ManifestProcessingRules"
    )
    name: str = Field(alias="Name")
    personalization_threshold_seconds: int = Field(
        alias="PersonalizationThresholdSeconds"
    )
    playback_configuration_arn: str = Field(alias="PlaybackConfigurationArn")
    playback_endpoint_prefix: str = Field(alias="PlaybackEndpointPrefix")
    session_initialization_endpoint_prefix: str = Field(
        alias="SessionInitializationEndpointPrefix"
    )
    slate_ad_url: str = Field(alias="SlateAdUrl")
    tags: Dict[str, str] = Field(alias="Tags")
    transcode_profile_name: str = Field(alias="TranscodeProfileName")
    video_content_source_url: str = Field(alias="VideoContentSourceUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePrefetchScheduleRequestModel(BaseModel):
    consumption: PrefetchConsumptionModel = Field(alias="Consumption")
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    retrieval: PrefetchRetrievalModel = Field(alias="Retrieval")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")


class CreatePrefetchScheduleResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    consumption: PrefetchConsumptionModel = Field(alias="Consumption")
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    retrieval: PrefetchRetrievalModel = Field(alias="Retrieval")
    stream_id: str = Field(alias="StreamId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPrefetchScheduleResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    consumption: PrefetchConsumptionModel = Field(alias="Consumption")
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    retrieval: PrefetchRetrievalModel = Field(alias="Retrieval")
    stream_id: str = Field(alias="StreamId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PrefetchScheduleModel(BaseModel):
    arn: str = Field(alias="Arn")
    consumption: PrefetchConsumptionModel = Field(alias="Consumption")
    name: str = Field(alias="Name")
    playback_configuration_name: str = Field(alias="PlaybackConfigurationName")
    retrieval: PrefetchRetrievalModel = Field(alias="Retrieval")
    stream_id: Optional[str] = Field(default=None, alias="StreamId")


class ListLiveSourcesResponseModel(BaseModel):
    items: List[LiveSourceModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVodSourcesResponseModel(BaseModel):
    items: List[VodSourceModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    outputs: Sequence[RequestOutputItemModel] = Field(alias="Outputs")
    playback_mode: Literal["LINEAR", "LOOP"] = Field(alias="PlaybackMode")
    filler_slate: Optional[SlateSourceModel] = Field(default=None, alias="FillerSlate")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    tier: Optional[Literal["BASIC", "STANDARD"]] = Field(default=None, alias="Tier")


class UpdateChannelRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    outputs: Sequence[RequestOutputItemModel] = Field(alias="Outputs")
    filler_slate: Optional[SlateSourceModel] = Field(default=None, alias="FillerSlate")


class ChannelModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    channel_state: str = Field(alias="ChannelState")
    log_configuration: LogConfigurationForChannelModel = Field(alias="LogConfiguration")
    outputs: List[ResponseOutputItemModel] = Field(alias="Outputs")
    playback_mode: str = Field(alias="PlaybackMode")
    tier: str = Field(alias="Tier")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    filler_slate: Optional[SlateSourceModel] = Field(default=None, alias="FillerSlate")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class CreateChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    channel_state: Literal["RUNNING", "STOPPED"] = Field(alias="ChannelState")
    creation_time: datetime = Field(alias="CreationTime")
    filler_slate: SlateSourceModel = Field(alias="FillerSlate")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    outputs: List[ResponseOutputItemModel] = Field(alias="Outputs")
    playback_mode: str = Field(alias="PlaybackMode")
    tags: Dict[str, str] = Field(alias="Tags")
    tier: str = Field(alias="Tier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    channel_state: Literal["RUNNING", "STOPPED"] = Field(alias="ChannelState")
    creation_time: datetime = Field(alias="CreationTime")
    filler_slate: SlateSourceModel = Field(alias="FillerSlate")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    log_configuration: LogConfigurationForChannelModel = Field(alias="LogConfiguration")
    outputs: List[ResponseOutputItemModel] = Field(alias="Outputs")
    playback_mode: str = Field(alias="PlaybackMode")
    tags: Dict[str, str] = Field(alias="Tags")
    tier: str = Field(alias="Tier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    channel_state: Literal["RUNNING", "STOPPED"] = Field(alias="ChannelState")
    creation_time: datetime = Field(alias="CreationTime")
    filler_slate: SlateSourceModel = Field(alias="FillerSlate")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    outputs: List[ResponseOutputItemModel] = Field(alias="Outputs")
    playback_mode: str = Field(alias="PlaybackMode")
    tags: Dict[str, str] = Field(alias="Tags")
    tier: str = Field(alias="Tier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelScheduleResponseModel(BaseModel):
    items: List[ScheduleEntryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdBreakModel(BaseModel):
    message_type: Optional[Literal["SPLICE_INSERT", "TIME_SIGNAL"]] = Field(
        default=None, alias="MessageType"
    )
    offset_millis: Optional[int] = Field(default=None, alias="OffsetMillis")
    slate: Optional[SlateSourceModel] = Field(default=None, alias="Slate")
    splice_insert_message: Optional[SpliceInsertMessageModel] = Field(
        default=None, alias="SpliceInsertMessage"
    )
    time_signal_message: Optional[TimeSignalMessageModel] = Field(
        default=None, alias="TimeSignalMessage"
    )


class ListSourceLocationsResponseModel(BaseModel):
    items: List[SourceLocationModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlaybackConfigurationsResponseModel(BaseModel):
    items: List[PlaybackConfigurationModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPrefetchSchedulesResponseModel(BaseModel):
    items: List[PrefetchScheduleModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsResponseModel(BaseModel):
    items: List[ChannelModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProgramRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    program_name: str = Field(alias="ProgramName")
    schedule_configuration: ScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    source_location_name: str = Field(alias="SourceLocationName")
    ad_breaks: Optional[Sequence[AdBreakModel]] = Field(default=None, alias="AdBreaks")
    live_source_name: Optional[str] = Field(default=None, alias="LiveSourceName")
    vod_source_name: Optional[str] = Field(default=None, alias="VodSourceName")


class CreateProgramResponseModel(BaseModel):
    ad_breaks: List[AdBreakModel] = Field(alias="AdBreaks")
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    clip_range: ClipRangeModel = Field(alias="ClipRange")
    creation_time: datetime = Field(alias="CreationTime")
    duration_millis: int = Field(alias="DurationMillis")
    live_source_name: str = Field(alias="LiveSourceName")
    program_name: str = Field(alias="ProgramName")
    scheduled_start_time: datetime = Field(alias="ScheduledStartTime")
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProgramResponseModel(BaseModel):
    ad_breaks: List[AdBreakModel] = Field(alias="AdBreaks")
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    clip_range: ClipRangeModel = Field(alias="ClipRange")
    creation_time: datetime = Field(alias="CreationTime")
    duration_millis: int = Field(alias="DurationMillis")
    live_source_name: str = Field(alias="LiveSourceName")
    program_name: str = Field(alias="ProgramName")
    scheduled_start_time: datetime = Field(alias="ScheduledStartTime")
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProgramRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    program_name: str = Field(alias="ProgramName")
    schedule_configuration: UpdateProgramScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    ad_breaks: Optional[Sequence[AdBreakModel]] = Field(default=None, alias="AdBreaks")


class UpdateProgramResponseModel(BaseModel):
    ad_breaks: List[AdBreakModel] = Field(alias="AdBreaks")
    arn: str = Field(alias="Arn")
    channel_name: str = Field(alias="ChannelName")
    clip_range: ClipRangeModel = Field(alias="ClipRange")
    creation_time: datetime = Field(alias="CreationTime")
    duration_millis: int = Field(alias="DurationMillis")
    live_source_name: str = Field(alias="LiveSourceName")
    program_name: str = Field(alias="ProgramName")
    scheduled_start_time: datetime = Field(alias="ScheduledStartTime")
    source_location_name: str = Field(alias="SourceLocationName")
    vod_source_name: str = Field(alias="VodSourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
