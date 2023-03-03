# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AudioConcatenationConfigurationModel(BaseModel):
    state: Literal["Enabled"] = Field(alias="State")


class CompositedVideoConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class ContentConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class DataChannelConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class MeetingEventsConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class TranscriptionMessagesConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class VideoConcatenationConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")


class AudioArtifactsConfigurationModel(BaseModel):
    mux_type: Literal[
        "AudioOnly", "AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"
    ] = Field(alias="MuxType")


class ContentArtifactsConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")
    mux_type: Optional[Literal["ContentOnly"]] = Field(default=None, alias="MuxType")


class VideoArtifactsConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")
    mux_type: Optional[Literal["VideoOnly"]] = Field(default=None, alias="MuxType")


class S3BucketSinkConfigurationModel(BaseModel):
    destination: str = Field(alias="Destination")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteMediaCapturePipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class DeleteMediaPipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class GetMediaCapturePipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class GetMediaPipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class PresenterOnlyConfigurationModel(BaseModel):
    presenter_position: Optional[
        Literal["BottomLeft", "BottomRight", "TopLeft", "TopRight"]
    ] = Field(default=None, alias="PresenterPosition")


class ListMediaCapturePipelinesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MediaCapturePipelineSummaryModel(BaseModel):
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
    media_pipeline_arn: Optional[str] = Field(default=None, alias="MediaPipelineArn")


class ListMediaPipelinesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MediaPipelineSummaryModel(BaseModel):
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
    media_pipeline_arn: Optional[str] = Field(default=None, alias="MediaPipelineArn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class LiveConnectorRTMPConfigurationModel(BaseModel):
    url: str = Field(alias="Url")
    audio_channels: Optional[Literal["Mono", "Stereo"]] = Field(
        default=None, alias="AudioChannels"
    )
    audio_sample_rate: Optional[str] = Field(default=None, alias="AudioSampleRate")


class SelectedVideoStreamsModel(BaseModel):
    attendee_ids: Optional[Sequence[str]] = Field(default=None, alias="AttendeeIds")
    external_user_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ExternalUserIds"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ArtifactsConcatenationConfigurationModel(BaseModel):
    audio: AudioConcatenationConfigurationModel = Field(alias="Audio")
    video: VideoConcatenationConfigurationModel = Field(alias="Video")
    content: ContentConcatenationConfigurationModel = Field(alias="Content")
    data_channel: DataChannelConcatenationConfigurationModel = Field(
        alias="DataChannel"
    )
    transcription_messages: TranscriptionMessagesConcatenationConfigurationModel = (
        Field(alias="TranscriptionMessages")
    )
    meeting_events: MeetingEventsConcatenationConfigurationModel = Field(
        alias="MeetingEvents"
    )
    composited_video: CompositedVideoConcatenationConfigurationModel = Field(
        alias="CompositedVideo"
    )


class ConcatenationSinkModel(BaseModel):
    type: Literal["S3Bucket"] = Field(alias="Type")
    s3_bucket_sink_configuration: S3BucketSinkConfigurationModel = Field(
        alias="S3BucketSinkConfiguration"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GridViewConfigurationModel(BaseModel):
    content_share_layout: Literal["Horizontal", "PresenterOnly", "Vertical"] = Field(
        alias="ContentShareLayout"
    )
    presenter_only_configuration: Optional[PresenterOnlyConfigurationModel] = Field(
        default=None, alias="PresenterOnlyConfiguration"
    )


class ListMediaCapturePipelinesResponseModel(BaseModel):
    media_capture_pipelines: List[MediaCapturePipelineSummaryModel] = Field(
        alias="MediaCapturePipelines"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMediaPipelinesResponseModel(BaseModel):
    media_pipelines: List[MediaPipelineSummaryModel] = Field(alias="MediaPipelines")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LiveConnectorSinkConfigurationModel(BaseModel):
    sink_type: Literal["RTMP"] = Field(alias="SinkType")
    rtmp_configuration: LiveConnectorRTMPConfigurationModel = Field(
        alias="RTMPConfiguration"
    )


class SourceConfigurationModel(BaseModel):
    selected_video_streams: Optional[SelectedVideoStreamsModel] = Field(
        default=None, alias="SelectedVideoStreams"
    )


class ChimeSdkMeetingConcatenationConfigurationModel(BaseModel):
    artifacts_configuration: ArtifactsConcatenationConfigurationModel = Field(
        alias="ArtifactsConfiguration"
    )


class CompositedVideoArtifactsConfigurationModel(BaseModel):
    grid_view_configuration: GridViewConfigurationModel = Field(
        alias="GridViewConfiguration"
    )
    layout: Optional[Literal["GridView"]] = Field(default=None, alias="Layout")
    resolution: Optional[Literal["FHD", "HD"]] = Field(default=None, alias="Resolution")


class MediaCapturePipelineSourceConfigurationModel(BaseModel):
    media_pipeline_arn: str = Field(alias="MediaPipelineArn")
    chime_sdk_meeting_configuration: ChimeSdkMeetingConcatenationConfigurationModel = (
        Field(alias="ChimeSdkMeetingConfiguration")
    )


class ArtifactsConfigurationModel(BaseModel):
    audio: AudioArtifactsConfigurationModel = Field(alias="Audio")
    video: VideoArtifactsConfigurationModel = Field(alias="Video")
    content: ContentArtifactsConfigurationModel = Field(alias="Content")
    composited_video: Optional[CompositedVideoArtifactsConfigurationModel] = Field(
        default=None, alias="CompositedVideo"
    )


class ChimeSdkMeetingLiveConnectorConfigurationModel(BaseModel):
    arn: str = Field(alias="Arn")
    mux_type: Literal[
        "AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"
    ] = Field(alias="MuxType")
    composited_video: Optional[CompositedVideoArtifactsConfigurationModel] = Field(
        default=None, alias="CompositedVideo"
    )
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="SourceConfiguration"
    )


class ConcatenationSourceModel(BaseModel):
    type: Literal["MediaCapturePipeline"] = Field(alias="Type")
    media_capture_pipeline_source_configuration: MediaCapturePipelineSourceConfigurationModel = Field(
        alias="MediaCapturePipelineSourceConfiguration"
    )


class ChimeSdkMeetingConfigurationModel(BaseModel):
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="SourceConfiguration"
    )
    artifacts_configuration: Optional[ArtifactsConfigurationModel] = Field(
        default=None, alias="ArtifactsConfiguration"
    )


class LiveConnectorSourceConfigurationModel(BaseModel):
    source_type: Literal["ChimeSdkMeeting"] = Field(alias="SourceType")
    chime_sdk_meeting_live_connector_configuration: ChimeSdkMeetingLiveConnectorConfigurationModel = Field(
        alias="ChimeSdkMeetingLiveConnectorConfiguration"
    )


class CreateMediaConcatenationPipelineRequestModel(BaseModel):
    sources: Sequence[ConcatenationSourceModel] = Field(alias="Sources")
    sinks: Sequence[ConcatenationSinkModel] = Field(alias="Sinks")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MediaConcatenationPipelineModel(BaseModel):
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
    media_pipeline_arn: Optional[str] = Field(default=None, alias="MediaPipelineArn")
    sources: Optional[List[ConcatenationSourceModel]] = Field(
        default=None, alias="Sources"
    )
    sinks: Optional[List[ConcatenationSinkModel]] = Field(default=None, alias="Sinks")
    status: Optional[
        Literal["Failed", "InProgress", "Initializing", "Stopped", "Stopping"]
    ] = Field(default=None, alias="Status")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class CreateMediaCapturePipelineRequestModel(BaseModel):
    source_type: Literal["ChimeSdkMeeting"] = Field(alias="SourceType")
    source_arn: str = Field(alias="SourceArn")
    sink_type: Literal["S3Bucket"] = Field(alias="SinkType")
    sink_arn: str = Field(alias="SinkArn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    chime_sdk_meeting_configuration: Optional[
        ChimeSdkMeetingConfigurationModel
    ] = Field(default=None, alias="ChimeSdkMeetingConfiguration")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MediaCapturePipelineModel(BaseModel):
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
    media_pipeline_arn: Optional[str] = Field(default=None, alias="MediaPipelineArn")
    source_type: Optional[Literal["ChimeSdkMeeting"]] = Field(
        default=None, alias="SourceType"
    )
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    status: Optional[
        Literal["Failed", "InProgress", "Initializing", "Stopped", "Stopping"]
    ] = Field(default=None, alias="Status")
    sink_type: Optional[Literal["S3Bucket"]] = Field(default=None, alias="SinkType")
    sink_arn: Optional[str] = Field(default=None, alias="SinkArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    chime_sdk_meeting_configuration: Optional[
        ChimeSdkMeetingConfigurationModel
    ] = Field(default=None, alias="ChimeSdkMeetingConfiguration")


class CreateMediaLiveConnectorPipelineRequestModel(BaseModel):
    sources: Sequence[LiveConnectorSourceConfigurationModel] = Field(alias="Sources")
    sinks: Sequence[LiveConnectorSinkConfigurationModel] = Field(alias="Sinks")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MediaLiveConnectorPipelineModel(BaseModel):
    sources: Optional[List[LiveConnectorSourceConfigurationModel]] = Field(
        default=None, alias="Sources"
    )
    sinks: Optional[List[LiveConnectorSinkConfigurationModel]] = Field(
        default=None, alias="Sinks"
    )
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
    media_pipeline_arn: Optional[str] = Field(default=None, alias="MediaPipelineArn")
    status: Optional[
        Literal["Failed", "InProgress", "Initializing", "Stopped", "Stopping"]
    ] = Field(default=None, alias="Status")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class CreateMediaConcatenationPipelineResponseModel(BaseModel):
    media_concatenation_pipeline: MediaConcatenationPipelineModel = Field(
        alias="MediaConcatenationPipeline"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMediaCapturePipelineResponseModel(BaseModel):
    media_capture_pipeline: MediaCapturePipelineModel = Field(
        alias="MediaCapturePipeline"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMediaCapturePipelineResponseModel(BaseModel):
    media_capture_pipeline: MediaCapturePipelineModel = Field(
        alias="MediaCapturePipeline"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMediaLiveConnectorPipelineResponseModel(BaseModel):
    media_live_connector_pipeline: MediaLiveConnectorPipelineModel = Field(
        alias="MediaLiveConnectorPipeline"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MediaPipelineModel(BaseModel):
    media_capture_pipeline: Optional[MediaCapturePipelineModel] = Field(
        default=None, alias="MediaCapturePipeline"
    )
    media_live_connector_pipeline: Optional[MediaLiveConnectorPipelineModel] = Field(
        default=None, alias="MediaLiveConnectorPipeline"
    )
    media_concatenation_pipeline: Optional[MediaConcatenationPipelineModel] = Field(
        default=None, alias="MediaConcatenationPipeline"
    )


class GetMediaPipelineResponseModel(BaseModel):
    media_pipeline: MediaPipelineModel = Field(alias="MediaPipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
