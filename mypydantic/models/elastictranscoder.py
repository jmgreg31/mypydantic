# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from typing import Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class EncryptionModel(BaseModel):
    mode: Optional[str] = Field(default=None, alias="Mode")
    key: Optional[str] = Field(default=None, alias="Key")
    key_md5: Optional[str] = Field(default=None, alias="KeyMd5")
    initialization_vector: Optional[str] = Field(
        default=None, alias="InitializationVector"
    )


class AudioCodecOptionsModel(BaseModel):
    profile: Optional[str] = Field(default=None, alias="Profile")
    bit_depth: Optional[str] = Field(default=None, alias="BitDepth")
    bit_order: Optional[str] = Field(default=None, alias="BitOrder")
    signed: Optional[str] = Field(default=None, alias="Signed")


class CancelJobRequestModel(BaseModel):
    id: str = Field(alias="Id")


class TimeSpanModel(BaseModel):
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    duration: Optional[str] = Field(default=None, alias="Duration")


class HlsContentProtectionModel(BaseModel):
    method: Optional[str] = Field(default=None, alias="Method")
    key: Optional[str] = Field(default=None, alias="Key")
    key_md5: Optional[str] = Field(default=None, alias="KeyMd5")
    initialization_vector: Optional[str] = Field(
        default=None, alias="InitializationVector"
    )
    license_acquisition_url: Optional[str] = Field(
        default=None, alias="LicenseAcquisitionUrl"
    )
    key_storage_policy: Optional[str] = Field(default=None, alias="KeyStoragePolicy")


class PlayReadyDrmModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    key: Optional[str] = Field(default=None, alias="Key")
    key_md5: Optional[str] = Field(default=None, alias="KeyMd5")
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    initialization_vector: Optional[str] = Field(
        default=None, alias="InitializationVector"
    )
    license_acquisition_url: Optional[str] = Field(
        default=None, alias="LicenseAcquisitionUrl"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class NotificationsModel(BaseModel):
    progressing: Optional[str] = Field(default=None, alias="Progressing")
    completed: Optional[str] = Field(default=None, alias="Completed")
    warning: Optional[str] = Field(default=None, alias="Warning")
    error: Optional[str] = Field(default=None, alias="Error")


class WarningModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class ThumbnailsModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    interval: Optional[str] = Field(default=None, alias="Interval")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    aspect_ratio: Optional[str] = Field(default=None, alias="AspectRatio")
    max_width: Optional[str] = Field(default=None, alias="MaxWidth")
    max_height: Optional[str] = Field(default=None, alias="MaxHeight")
    sizing_policy: Optional[str] = Field(default=None, alias="SizingPolicy")
    padding_policy: Optional[str] = Field(default=None, alias="PaddingPolicy")


class DeletePipelineRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeletePresetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DetectedPropertiesModel(BaseModel):
    width: Optional[int] = Field(default=None, alias="Width")
    height: Optional[int] = Field(default=None, alias="Height")
    frame_rate: Optional[str] = Field(default=None, alias="FrameRate")
    file_size: Optional[int] = Field(default=None, alias="FileSize")
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")


class TimingModel(BaseModel):
    submit_time_millis: Optional[int] = Field(default=None, alias="SubmitTimeMillis")
    start_time_millis: Optional[int] = Field(default=None, alias="StartTimeMillis")
    finish_time_millis: Optional[int] = Field(default=None, alias="FinishTimeMillis")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListJobsByPipelineRequestModel(BaseModel):
    pipeline_id: str = Field(alias="PipelineId")
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListJobsByStatusRequestModel(BaseModel):
    status: str = Field(alias="Status")
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListPipelinesRequestModel(BaseModel):
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListPresetsRequestModel(BaseModel):
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class PermissionModel(BaseModel):
    grantee_type: Optional[str] = Field(default=None, alias="GranteeType")
    grantee: Optional[str] = Field(default=None, alias="Grantee")
    access: Optional[Sequence[str]] = Field(default=None, alias="Access")


class PresetWatermarkModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    max_width: Optional[str] = Field(default=None, alias="MaxWidth")
    max_height: Optional[str] = Field(default=None, alias="MaxHeight")
    sizing_policy: Optional[str] = Field(default=None, alias="SizingPolicy")
    horizontal_align: Optional[str] = Field(default=None, alias="HorizontalAlign")
    horizontal_offset: Optional[str] = Field(default=None, alias="HorizontalOffset")
    vertical_align: Optional[str] = Field(default=None, alias="VerticalAlign")
    vertical_offset: Optional[str] = Field(default=None, alias="VerticalOffset")
    opacity: Optional[str] = Field(default=None, alias="Opacity")
    target: Optional[str] = Field(default=None, alias="Target")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class ReadJobRequestModel(BaseModel):
    id: str = Field(alias="Id")


class ReadPipelineRequestModel(BaseModel):
    id: str = Field(alias="Id")


class ReadPresetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class TestRoleRequestModel(BaseModel):
    role: str = Field(alias="Role")
    input_bucket: str = Field(alias="InputBucket")
    output_bucket: str = Field(alias="OutputBucket")
    topics: Sequence[str] = Field(alias="Topics")


class UpdatePipelineStatusRequestModel(BaseModel):
    id: str = Field(alias="Id")
    status: str = Field(alias="Status")


class ArtworkModel(BaseModel):
    input_key: Optional[str] = Field(default=None, alias="InputKey")
    max_width: Optional[str] = Field(default=None, alias="MaxWidth")
    max_height: Optional[str] = Field(default=None, alias="MaxHeight")
    sizing_policy: Optional[str] = Field(default=None, alias="SizingPolicy")
    padding_policy: Optional[str] = Field(default=None, alias="PaddingPolicy")
    album_art_format: Optional[str] = Field(default=None, alias="AlbumArtFormat")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")


class CaptionFormatModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    pattern: Optional[str] = Field(default=None, alias="Pattern")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")


class CaptionSourceModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    language: Optional[str] = Field(default=None, alias="Language")
    time_offset: Optional[str] = Field(default=None, alias="TimeOffset")
    label: Optional[str] = Field(default=None, alias="Label")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")


class JobWatermarkModel(BaseModel):
    preset_watermark_id: Optional[str] = Field(default=None, alias="PresetWatermarkId")
    input_key: Optional[str] = Field(default=None, alias="InputKey")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")


class AudioParametersModel(BaseModel):
    codec: Optional[str] = Field(default=None, alias="Codec")
    sample_rate: Optional[str] = Field(default=None, alias="SampleRate")
    bit_rate: Optional[str] = Field(default=None, alias="BitRate")
    channels: Optional[str] = Field(default=None, alias="Channels")
    audio_packing_mode: Optional[str] = Field(default=None, alias="AudioPackingMode")
    codec_options: Optional[AudioCodecOptionsModel] = Field(
        default=None, alias="CodecOptions"
    )


class ClipModel(BaseModel):
    time_span: Optional[TimeSpanModel] = Field(default=None, alias="TimeSpan")


class CreateJobPlaylistModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    format: Optional[str] = Field(default=None, alias="Format")
    output_keys: Optional[Sequence[str]] = Field(default=None, alias="OutputKeys")
    hls_content_protection: Optional[HlsContentProtectionModel] = Field(
        default=None, alias="HlsContentProtection"
    )
    play_ready_drm: Optional[PlayReadyDrmModel] = Field(
        default=None, alias="PlayReadyDrm"
    )


class PlaylistModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    format: Optional[str] = Field(default=None, alias="Format")
    output_keys: Optional[List[str]] = Field(default=None, alias="OutputKeys")
    hls_content_protection: Optional[HlsContentProtectionModel] = Field(
        default=None, alias="HlsContentProtection"
    )
    play_ready_drm: Optional[PlayReadyDrmModel] = Field(
        default=None, alias="PlayReadyDrm"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    status_detail: Optional[str] = Field(default=None, alias="StatusDetail")


class TestRoleResponseModel(BaseModel):
    success: str = Field(alias="Success")
    messages: List[str] = Field(alias="Messages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineNotificationsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    notifications: NotificationsModel = Field(alias="Notifications")


class ListJobsByPipelineRequestListJobsByPipelinePaginateModel(BaseModel):
    pipeline_id: str = Field(alias="PipelineId")
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsByStatusRequestListJobsByStatusPaginateModel(BaseModel):
    status: str = Field(alias="Status")
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesRequestListPipelinesPaginateModel(BaseModel):
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPresetsRequestListPresetsPaginateModel(BaseModel):
    ascending: Optional[str] = Field(default=None, alias="Ascending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PipelineOutputConfigModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    storage_class: Optional[str] = Field(default=None, alias="StorageClass")
    permissions: Optional[Sequence[PermissionModel]] = Field(
        default=None, alias="Permissions"
    )


class VideoParametersModel(BaseModel):
    codec: Optional[str] = Field(default=None, alias="Codec")
    codec_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="CodecOptions"
    )
    keyframes_max_dist: Optional[str] = Field(default=None, alias="KeyframesMaxDist")
    fixed_gop: Optional[str] = Field(default=None, alias="FixedGOP")
    bit_rate: Optional[str] = Field(default=None, alias="BitRate")
    frame_rate: Optional[str] = Field(default=None, alias="FrameRate")
    max_frame_rate: Optional[str] = Field(default=None, alias="MaxFrameRate")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    aspect_ratio: Optional[str] = Field(default=None, alias="AspectRatio")
    max_width: Optional[str] = Field(default=None, alias="MaxWidth")
    max_height: Optional[str] = Field(default=None, alias="MaxHeight")
    display_aspect_ratio: Optional[str] = Field(
        default=None, alias="DisplayAspectRatio"
    )
    sizing_policy: Optional[str] = Field(default=None, alias="SizingPolicy")
    padding_policy: Optional[str] = Field(default=None, alias="PaddingPolicy")
    watermarks: Optional[Sequence[PresetWatermarkModel]] = Field(
        default=None, alias="Watermarks"
    )


class ReadJobRequestJobCompleteWaitModel(BaseModel):
    id: str = Field(alias="Id")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class JobAlbumArtModel(BaseModel):
    merge_policy: Optional[str] = Field(default=None, alias="MergePolicy")
    artwork: Optional[Sequence[ArtworkModel]] = Field(default=None, alias="Artwork")


class CaptionsModel(BaseModel):
    merge_policy: Optional[str] = Field(default=None, alias="MergePolicy")
    caption_sources: Optional[Sequence[CaptionSourceModel]] = Field(
        default=None, alias="CaptionSources"
    )
    caption_formats: Optional[Sequence[CaptionFormatModel]] = Field(
        default=None, alias="CaptionFormats"
    )


class InputCaptionsModel(BaseModel):
    merge_policy: Optional[str] = Field(default=None, alias="MergePolicy")
    caption_sources: Optional[Sequence[CaptionSourceModel]] = Field(
        default=None, alias="CaptionSources"
    )


class CreatePipelineRequestModel(BaseModel):
    name: str = Field(alias="Name")
    input_bucket: str = Field(alias="InputBucket")
    role: str = Field(alias="Role")
    output_bucket: Optional[str] = Field(default=None, alias="OutputBucket")
    aws_kms_key_arn: Optional[str] = Field(default=None, alias="AwsKmsKeyArn")
    notifications: Optional[NotificationsModel] = Field(
        default=None, alias="Notifications"
    )
    content_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ContentConfig"
    )
    thumbnail_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ThumbnailConfig"
    )


class PipelineModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    input_bucket: Optional[str] = Field(default=None, alias="InputBucket")
    output_bucket: Optional[str] = Field(default=None, alias="OutputBucket")
    role: Optional[str] = Field(default=None, alias="Role")
    aws_kms_key_arn: Optional[str] = Field(default=None, alias="AwsKmsKeyArn")
    notifications: Optional[NotificationsModel] = Field(
        default=None, alias="Notifications"
    )
    content_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ContentConfig"
    )
    thumbnail_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ThumbnailConfig"
    )


class UpdatePipelineRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    input_bucket: Optional[str] = Field(default=None, alias="InputBucket")
    role: Optional[str] = Field(default=None, alias="Role")
    aws_kms_key_arn: Optional[str] = Field(default=None, alias="AwsKmsKeyArn")
    notifications: Optional[NotificationsModel] = Field(
        default=None, alias="Notifications"
    )
    content_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ContentConfig"
    )
    thumbnail_config: Optional[PipelineOutputConfigModel] = Field(
        default=None, alias="ThumbnailConfig"
    )


class CreatePresetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    container: str = Field(alias="Container")
    description: Optional[str] = Field(default=None, alias="Description")
    video: Optional[VideoParametersModel] = Field(default=None, alias="Video")
    audio: Optional[AudioParametersModel] = Field(default=None, alias="Audio")
    thumbnails: Optional[ThumbnailsModel] = Field(default=None, alias="Thumbnails")


class PresetModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    container: Optional[str] = Field(default=None, alias="Container")
    audio: Optional[AudioParametersModel] = Field(default=None, alias="Audio")
    video: Optional[VideoParametersModel] = Field(default=None, alias="Video")
    thumbnails: Optional[ThumbnailsModel] = Field(default=None, alias="Thumbnails")
    type: Optional[str] = Field(default=None, alias="Type")


class CreateJobOutputModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    thumbnail_pattern: Optional[str] = Field(default=None, alias="ThumbnailPattern")
    thumbnail_encryption: Optional[EncryptionModel] = Field(
        default=None, alias="ThumbnailEncryption"
    )
    rotate: Optional[str] = Field(default=None, alias="Rotate")
    preset_id: Optional[str] = Field(default=None, alias="PresetId")
    segment_duration: Optional[str] = Field(default=None, alias="SegmentDuration")
    watermarks: Optional[Sequence[JobWatermarkModel]] = Field(
        default=None, alias="Watermarks"
    )
    album_art: Optional[JobAlbumArtModel] = Field(default=None, alias="AlbumArt")
    composition: Optional[Sequence[ClipModel]] = Field(
        default=None, alias="Composition"
    )
    captions: Optional[CaptionsModel] = Field(default=None, alias="Captions")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")


class JobOutputModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    key: Optional[str] = Field(default=None, alias="Key")
    thumbnail_pattern: Optional[str] = Field(default=None, alias="ThumbnailPattern")
    thumbnail_encryption: Optional[EncryptionModel] = Field(
        default=None, alias="ThumbnailEncryption"
    )
    rotate: Optional[str] = Field(default=None, alias="Rotate")
    preset_id: Optional[str] = Field(default=None, alias="PresetId")
    segment_duration: Optional[str] = Field(default=None, alias="SegmentDuration")
    status: Optional[str] = Field(default=None, alias="Status")
    status_detail: Optional[str] = Field(default=None, alias="StatusDetail")
    duration: Optional[int] = Field(default=None, alias="Duration")
    width: Optional[int] = Field(default=None, alias="Width")
    height: Optional[int] = Field(default=None, alias="Height")
    frame_rate: Optional[str] = Field(default=None, alias="FrameRate")
    file_size: Optional[int] = Field(default=None, alias="FileSize")
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    watermarks: Optional[List[JobWatermarkModel]] = Field(
        default=None, alias="Watermarks"
    )
    album_art: Optional[JobAlbumArtModel] = Field(default=None, alias="AlbumArt")
    composition: Optional[List[ClipModel]] = Field(default=None, alias="Composition")
    captions: Optional[CaptionsModel] = Field(default=None, alias="Captions")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    applied_color_space_conversion: Optional[str] = Field(
        default=None, alias="AppliedColorSpaceConversion"
    )


class JobInputModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    frame_rate: Optional[str] = Field(default=None, alias="FrameRate")
    resolution: Optional[str] = Field(default=None, alias="Resolution")
    aspect_ratio: Optional[str] = Field(default=None, alias="AspectRatio")
    interlaced: Optional[str] = Field(default=None, alias="Interlaced")
    container: Optional[str] = Field(default=None, alias="Container")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    time_span: Optional[TimeSpanModel] = Field(default=None, alias="TimeSpan")
    input_captions: Optional[InputCaptionsModel] = Field(
        default=None, alias="InputCaptions"
    )
    detected_properties: Optional[DetectedPropertiesModel] = Field(
        default=None, alias="DetectedProperties"
    )


class CreatePipelineResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="Pipeline")
    warnings: List[WarningModel] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPipelinesResponseModel(BaseModel):
    pipelines: List[PipelineModel] = Field(alias="Pipelines")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReadPipelineResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="Pipeline")
    warnings: List[WarningModel] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineNotificationsResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="Pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="Pipeline")
    warnings: List[WarningModel] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineStatusResponseModel(BaseModel):
    pipeline: PipelineModel = Field(alias="Pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePresetResponseModel(BaseModel):
    preset: PresetModel = Field(alias="Preset")
    warning: str = Field(alias="Warning")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPresetsResponseModel(BaseModel):
    presets: List[PresetModel] = Field(alias="Presets")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReadPresetResponseModel(BaseModel):
    preset: PresetModel = Field(alias="Preset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobRequestModel(BaseModel):
    pipeline_id: str = Field(alias="PipelineId")
    input: Optional[JobInputModel] = Field(default=None, alias="Input")
    inputs: Optional[Sequence[JobInputModel]] = Field(default=None, alias="Inputs")
    output: Optional[CreateJobOutputModel] = Field(default=None, alias="Output")
    outputs: Optional[Sequence[CreateJobOutputModel]] = Field(
        default=None, alias="Outputs"
    )
    output_key_prefix: Optional[str] = Field(default=None, alias="OutputKeyPrefix")
    playlists: Optional[Sequence[CreateJobPlaylistModel]] = Field(
        default=None, alias="Playlists"
    )
    user_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserMetadata"
    )


class JobModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    pipeline_id: Optional[str] = Field(default=None, alias="PipelineId")
    input: Optional[JobInputModel] = Field(default=None, alias="Input")
    inputs: Optional[List[JobInputModel]] = Field(default=None, alias="Inputs")
    output: Optional[JobOutputModel] = Field(default=None, alias="Output")
    outputs: Optional[List[JobOutputModel]] = Field(default=None, alias="Outputs")
    output_key_prefix: Optional[str] = Field(default=None, alias="OutputKeyPrefix")
    playlists: Optional[List[PlaylistModel]] = Field(default=None, alias="Playlists")
    status: Optional[str] = Field(default=None, alias="Status")
    user_metadata: Optional[Dict[str, str]] = Field(default=None, alias="UserMetadata")
    timing: Optional[TimingModel] = Field(default=None, alias="Timing")


class CreateJobResponseModel(BaseModel):
    job: JobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsByPipelineResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsByStatusResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReadJobResponseModel(BaseModel):
    job: JobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
