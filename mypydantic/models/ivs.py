# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AudioConfigurationModel(BaseModel):
    channels: Optional[int] = Field(default=None, alias="channels")
    codec: Optional[str] = Field(default=None, alias="codec")
    sample_rate: Optional[int] = Field(default=None, alias="sampleRate")
    target_bitrate: Optional[int] = Field(default=None, alias="targetBitrate")


class BatchErrorModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class BatchGetChannelRequestModel(BaseModel):
    arns: Sequence[str] = Field(alias="arns")


class ChannelModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    authorized: Optional[bool] = Field(default=None, alias="authorized")
    ingest_endpoint: Optional[str] = Field(default=None, alias="ingestEndpoint")
    latency_mode: Optional[Literal["LOW", "NORMAL"]] = Field(
        default=None, alias="latencyMode"
    )
    name: Optional[str] = Field(default=None, alias="name")
    playback_url: Optional[str] = Field(default=None, alias="playbackUrl")
    recording_configuration_arn: Optional[str] = Field(
        default=None, alias="recordingConfigurationArn"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[Literal["BASIC", "STANDARD"]] = Field(default=None, alias="type")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetStreamKeyRequestModel(BaseModel):
    arns: Sequence[str] = Field(alias="arns")


class StreamKeyModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    channel_arn: Optional[str] = Field(default=None, alias="channelArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    value: Optional[str] = Field(default=None, alias="value")


class ChannelSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    authorized: Optional[bool] = Field(default=None, alias="authorized")
    latency_mode: Optional[Literal["LOW", "NORMAL"]] = Field(
        default=None, alias="latencyMode"
    )
    name: Optional[str] = Field(default=None, alias="name")
    recording_configuration_arn: Optional[str] = Field(
        default=None, alias="recordingConfigurationArn"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateChannelRequestModel(BaseModel):
    authorized: Optional[bool] = Field(default=None, alias="authorized")
    latency_mode: Optional[Literal["LOW", "NORMAL"]] = Field(
        default=None, alias="latencyMode"
    )
    name: Optional[str] = Field(default=None, alias="name")
    recording_configuration_arn: Optional[str] = Field(
        default=None, alias="recordingConfigurationArn"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    type: Optional[Literal["BASIC", "STANDARD"]] = Field(default=None, alias="type")


class ThumbnailConfigurationModel(BaseModel):
    recording_mode: Optional[Literal["DISABLED", "INTERVAL"]] = Field(
        default=None, alias="recordingMode"
    )
    target_interval_seconds: Optional[int] = Field(
        default=None, alias="targetIntervalSeconds"
    )


class CreateStreamKeyRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteChannelRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeletePlaybackKeyPairRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteRecordingConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteStreamKeyRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class S3DestinationConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")


class GetChannelRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetPlaybackKeyPairRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class PlaybackKeyPairModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    fingerprint: Optional[str] = Field(default=None, alias="fingerprint")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class GetRecordingConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetStreamKeyRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetStreamRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")


class StreamModel(BaseModel):
    channel_arn: Optional[str] = Field(default=None, alias="channelArn")
    health: Optional[Literal["HEALTHY", "STARVING", "UNKNOWN"]] = Field(
        default=None, alias="health"
    )
    playback_url: Optional[str] = Field(default=None, alias="playbackUrl")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    state: Optional[Literal["LIVE", "OFFLINE"]] = Field(default=None, alias="state")
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    viewer_count: Optional[int] = Field(default=None, alias="viewerCount")


class GetStreamSessionRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    stream_id: Optional[str] = Field(default=None, alias="streamId")


class ImportPlaybackKeyPairRequestModel(BaseModel):
    public_key_material: str = Field(alias="publicKeyMaterial")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class VideoConfigurationModel(BaseModel):
    avc_level: Optional[str] = Field(default=None, alias="avcLevel")
    avc_profile: Optional[str] = Field(default=None, alias="avcProfile")
    codec: Optional[str] = Field(default=None, alias="codec")
    encoder: Optional[str] = Field(default=None, alias="encoder")
    target_bitrate: Optional[int] = Field(default=None, alias="targetBitrate")
    target_framerate: Optional[int] = Field(default=None, alias="targetFramerate")
    video_height: Optional[int] = Field(default=None, alias="videoHeight")
    video_width: Optional[int] = Field(default=None, alias="videoWidth")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListChannelsRequestModel(BaseModel):
    filter_by_name: Optional[str] = Field(default=None, alias="filterByName")
    filter_by_recording_configuration_arn: Optional[str] = Field(
        default=None, alias="filterByRecordingConfigurationArn"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPlaybackKeyPairsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PlaybackKeyPairSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListRecordingConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListStreamKeysRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StreamKeySummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    channel_arn: Optional[str] = Field(default=None, alias="channelArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListStreamSessionsRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StreamSessionSummaryModel(BaseModel):
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    has_error_event: Optional[bool] = Field(default=None, alias="hasErrorEvent")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    stream_id: Optional[str] = Field(default=None, alias="streamId")


class StreamFiltersModel(BaseModel):
    health: Optional[Literal["HEALTHY", "STARVING", "UNKNOWN"]] = Field(
        default=None, alias="health"
    )


class StreamSummaryModel(BaseModel):
    channel_arn: Optional[str] = Field(default=None, alias="channelArn")
    health: Optional[Literal["HEALTHY", "STARVING", "UNKNOWN"]] = Field(
        default=None, alias="health"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    state: Optional[Literal["LIVE", "OFFLINE"]] = Field(default=None, alias="state")
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    viewer_count: Optional[int] = Field(default=None, alias="viewerCount")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PutMetadataRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    metadata: str = Field(alias="metadata")


class StopStreamRequestModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")


class StreamEventModel(BaseModel):
    event_time: Optional[datetime] = Field(default=None, alias="eventTime")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateChannelRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    authorized: Optional[bool] = Field(default=None, alias="authorized")
    latency_mode: Optional[Literal["LOW", "NORMAL"]] = Field(
        default=None, alias="latencyMode"
    )
    name: Optional[str] = Field(default=None, alias="name")
    recording_configuration_arn: Optional[str] = Field(
        default=None, alias="recordingConfigurationArn"
    )
    type: Optional[Literal["BASIC", "STANDARD"]] = Field(default=None, alias="type")


class BatchGetChannelResponseModel(BaseModel):
    channels: List[ChannelModel] = Field(alias="channels")
    errors: List[BatchErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetStreamKeyResponseModel(BaseModel):
    errors: List[BatchErrorModel] = Field(alias="errors")
    stream_keys: List[StreamKeyModel] = Field(alias="streamKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="channel")
    stream_key: StreamKeyModel = Field(alias="streamKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamKeyResponseModel(BaseModel):
    stream_key: StreamKeyModel = Field(alias="streamKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamKeyResponseModel(BaseModel):
    stream_key: StreamKeyModel = Field(alias="streamKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsResponseModel(BaseModel):
    channels: List[ChannelSummaryModel] = Field(alias="channels")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationConfigurationModel(BaseModel):
    s3: Optional[S3DestinationConfigurationModel] = Field(default=None, alias="s3")


class GetPlaybackKeyPairResponseModel(BaseModel):
    key_pair: PlaybackKeyPairModel = Field(alias="keyPair")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportPlaybackKeyPairResponseModel(BaseModel):
    key_pair: PlaybackKeyPairModel = Field(alias="keyPair")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamResponseModel(BaseModel):
    stream: StreamModel = Field(alias="stream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IngestConfigurationModel(BaseModel):
    audio: Optional[AudioConfigurationModel] = Field(default=None, alias="audio")
    video: Optional[VideoConfigurationModel] = Field(default=None, alias="video")


class ListChannelsRequestListChannelsPaginateModel(BaseModel):
    filter_by_name: Optional[str] = Field(default=None, alias="filterByName")
    filter_by_recording_configuration_arn: Optional[str] = Field(
        default=None, alias="filterByRecordingConfigurationArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlaybackKeyPairsRequestListPlaybackKeyPairsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecordingConfigurationsRequestListRecordingConfigurationsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamKeysRequestListStreamKeysPaginateModel(BaseModel):
    channel_arn: str = Field(alias="channelArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlaybackKeyPairsResponseModel(BaseModel):
    key_pairs: List[PlaybackKeyPairSummaryModel] = Field(alias="keyPairs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamKeysResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    stream_keys: List[StreamKeySummaryModel] = Field(alias="streamKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamSessionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    stream_sessions: List[StreamSessionSummaryModel] = Field(alias="streamSessions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamsRequestListStreamsPaginateModel(BaseModel):
    filter_by: Optional[StreamFiltersModel] = Field(default=None, alias="filterBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamsRequestModel(BaseModel):
    filter_by: Optional[StreamFiltersModel] = Field(default=None, alias="filterBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListStreamsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    streams: List[StreamSummaryModel] = Field(alias="streams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecordingConfigurationRequestModel(BaseModel):
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="name")
    recording_reconnect_window_seconds: Optional[int] = Field(
        default=None, alias="recordingReconnectWindowSeconds"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    thumbnail_configuration: Optional[ThumbnailConfigurationModel] = Field(
        default=None, alias="thumbnailConfiguration"
    )


class RecordingConfigurationSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    state: Literal["ACTIVE", "CREATE_FAILED", "CREATING"] = Field(alias="state")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class RecordingConfigurationModel(BaseModel):
    arn: str = Field(alias="arn")
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    state: Literal["ACTIVE", "CREATE_FAILED", "CREATING"] = Field(alias="state")
    name: Optional[str] = Field(default=None, alias="name")
    recording_reconnect_window_seconds: Optional[int] = Field(
        default=None, alias="recordingReconnectWindowSeconds"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    thumbnail_configuration: Optional[ThumbnailConfigurationModel] = Field(
        default=None, alias="thumbnailConfiguration"
    )


class ListRecordingConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    recording_configurations: List[RecordingConfigurationSummaryModel] = Field(
        alias="recordingConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecordingConfigurationResponseModel(BaseModel):
    recording_configuration: RecordingConfigurationModel = Field(
        alias="recordingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecordingConfigurationResponseModel(BaseModel):
    recording_configuration: RecordingConfigurationModel = Field(
        alias="recordingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamSessionModel(BaseModel):
    channel: Optional[ChannelModel] = Field(default=None, alias="channel")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    ingest_configuration: Optional[IngestConfigurationModel] = Field(
        default=None, alias="ingestConfiguration"
    )
    recording_configuration: Optional[RecordingConfigurationModel] = Field(
        default=None, alias="recordingConfiguration"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    truncated_events: Optional[List[StreamEventModel]] = Field(
        default=None, alias="truncatedEvents"
    )


class GetStreamSessionResponseModel(BaseModel):
    stream_session: StreamSessionModel = Field(alias="streamSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
