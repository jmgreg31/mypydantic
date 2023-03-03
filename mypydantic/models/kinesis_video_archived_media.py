# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ClipTimestampRangeModel(BaseModel):
    start_timestamp: Union[datetime, str] = Field(alias="StartTimestamp")
    end_timestamp: Union[datetime, str] = Field(alias="EndTimestamp")


class DASHTimestampRangeModel(BaseModel):
    start_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartTimestamp"
    )
    end_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="EndTimestamp"
    )


class TimestampRangeModel(BaseModel):
    start_timestamp: Union[datetime, str] = Field(alias="StartTimestamp")
    end_timestamp: Union[datetime, str] = Field(alias="EndTimestamp")


class FragmentModel(BaseModel):
    fragment_number: Optional[str] = Field(default=None, alias="FragmentNumber")
    fragment_size_in_bytes: Optional[int] = Field(
        default=None, alias="FragmentSizeInBytes"
    )
    producer_timestamp: Optional[datetime] = Field(
        default=None, alias="ProducerTimestamp"
    )
    server_timestamp: Optional[datetime] = Field(default=None, alias="ServerTimestamp")
    fragment_length_in_milliseconds: Optional[int] = Field(
        default=None, alias="FragmentLengthInMilliseconds"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetImagesInputRequestModel(BaseModel):
    image_selector_type: Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"] = Field(
        alias="ImageSelectorType"
    )
    start_timestamp: Union[datetime, str] = Field(alias="StartTimestamp")
    end_timestamp: Union[datetime, str] = Field(alias="EndTimestamp")
    sampling_interval: int = Field(alias="SamplingInterval")
    format: Literal["JPEG", "PNG"] = Field(alias="Format")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    format_config: Optional[Mapping[Literal["JPEGQuality"], str]] = Field(
        default=None, alias="FormatConfig"
    )
    width_pixels: Optional[int] = Field(default=None, alias="WidthPixels")
    height_pixels: Optional[int] = Field(default=None, alias="HeightPixels")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ImageModel(BaseModel):
    time_stamp: Optional[datetime] = Field(default=None, alias="TimeStamp")
    error: Optional[Literal["MEDIA_ERROR", "NO_MEDIA"]] = Field(
        default=None, alias="Error"
    )
    image_content: Optional[str] = Field(default=None, alias="ImageContent")


class GetMediaForFragmentListInputRequestModel(BaseModel):
    fragments: Sequence[str] = Field(alias="Fragments")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class HLSTimestampRangeModel(BaseModel):
    start_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartTimestamp"
    )
    end_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="EndTimestamp"
    )


class ClipFragmentSelectorModel(BaseModel):
    fragment_selector_type: Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"] = Field(
        alias="FragmentSelectorType"
    )
    timestamp_range: ClipTimestampRangeModel = Field(alias="TimestampRange")


class DASHFragmentSelectorModel(BaseModel):
    fragment_selector_type: Optional[
        Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
    ] = Field(default=None, alias="FragmentSelectorType")
    timestamp_range: Optional[DASHTimestampRangeModel] = Field(
        default=None, alias="TimestampRange"
    )


class FragmentSelectorModel(BaseModel):
    fragment_selector_type: Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"] = Field(
        alias="FragmentSelectorType"
    )
    timestamp_range: TimestampRangeModel = Field(alias="TimestampRange")


class GetClipOutputModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    payload: Type[StreamingBody] = Field(alias="Payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDASHStreamingSessionURLOutputModel(BaseModel):
    das_hstreaming_session_url: str = Field(alias="DASHStreamingSessionURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHLSStreamingSessionURLOutputModel(BaseModel):
    hl_s_streaming_session_url: str = Field(alias="HLSStreamingSessionURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMediaForFragmentListOutputModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    payload: Type[StreamingBody] = Field(alias="Payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFragmentsOutputModel(BaseModel):
    fragments: List[FragmentModel] = Field(alias="Fragments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImagesInputGetImagesPaginateModel(BaseModel):
    image_selector_type: Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"] = Field(
        alias="ImageSelectorType"
    )
    start_timestamp: Union[datetime, str] = Field(alias="StartTimestamp")
    end_timestamp: Union[datetime, str] = Field(alias="EndTimestamp")
    sampling_interval: int = Field(alias="SamplingInterval")
    format: Literal["JPEG", "PNG"] = Field(alias="Format")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    format_config: Optional[Mapping[Literal["JPEGQuality"], str]] = Field(
        default=None, alias="FormatConfig"
    )
    width_pixels: Optional[int] = Field(default=None, alias="WidthPixels")
    height_pixels: Optional[int] = Field(default=None, alias="HeightPixels")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetImagesOutputModel(BaseModel):
    images: List[ImageModel] = Field(alias="Images")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HLSFragmentSelectorModel(BaseModel):
    fragment_selector_type: Optional[
        Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
    ] = Field(default=None, alias="FragmentSelectorType")
    timestamp_range: Optional[HLSTimestampRangeModel] = Field(
        default=None, alias="TimestampRange"
    )


class GetClipInputRequestModel(BaseModel):
    clip_fragment_selector: ClipFragmentSelectorModel = Field(
        alias="ClipFragmentSelector"
    )
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class GetDASHStreamingSessionURLInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    playback_mode: Optional[Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]] = Field(
        default=None, alias="PlaybackMode"
    )
    display_fragment_timestamp: Optional[Literal["ALWAYS", "NEVER"]] = Field(
        default=None, alias="DisplayFragmentTimestamp"
    )
    display_fragment_number: Optional[Literal["ALWAYS", "NEVER"]] = Field(
        default=None, alias="DisplayFragmentNumber"
    )
    das_hfragment_selector: Optional[DASHFragmentSelectorModel] = Field(
        default=None, alias="DASHFragmentSelector"
    )
    expires: Optional[int] = Field(default=None, alias="Expires")
    max_manifest_fragment_results: Optional[int] = Field(
        default=None, alias="MaxManifestFragmentResults"
    )


class ListFragmentsInputListFragmentsPaginateModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    fragment_selector: Optional[FragmentSelectorModel] = Field(
        default=None, alias="FragmentSelector"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFragmentsInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    fragment_selector: Optional[FragmentSelectorModel] = Field(
        default=None, alias="FragmentSelector"
    )


class GetHLSStreamingSessionURLInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    playback_mode: Optional[Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]] = Field(
        default=None, alias="PlaybackMode"
    )
    hl_s_fragment_selector: Optional[HLSFragmentSelectorModel] = Field(
        default=None, alias="HLSFragmentSelector"
    )
    container_format: Optional[Literal["FRAGMENTED_MP4", "MPEG_TS"]] = Field(
        default=None, alias="ContainerFormat"
    )
    discontinuity_mode: Optional[
        Literal["ALWAYS", "NEVER", "ON_DISCONTINUITY"]
    ] = Field(default=None, alias="DiscontinuityMode")
    display_fragment_timestamp: Optional[Literal["ALWAYS", "NEVER"]] = Field(
        default=None, alias="DisplayFragmentTimestamp"
    )
    expires: Optional[int] = Field(default=None, alias="Expires")
    max_media_playlist_fragment_results: Optional[int] = Field(
        default=None, alias="MaxMediaPlaylistFragmentResults"
    )
