# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class SingleMasterConfigurationModel(BaseModel):
    message_ttl_seconds: Optional[int] = Field(default=None, alias="MessageTtlSeconds")


class ChannelNameConditionModel(BaseModel):
    comparison_operator: Optional[Literal["BEGINS_WITH"]] = Field(
        default=None, alias="ComparisonOperator"
    )
    comparison_value: Optional[str] = Field(default=None, alias="ComparisonValue")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateStreamInputRequestModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    media_type: Optional[str] = Field(default=None, alias="MediaType")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    data_retention_in_hours: Optional[int] = Field(
        default=None, alias="DataRetentionInHours"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteSignalingChannelInputRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")


class DeleteStreamInputRequestModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")


class LocalSizeConfigModel(BaseModel):
    max_local_media_size_in_mb: Optional[int] = Field(
        default=None, alias="MaxLocalMediaSizeInMB"
    )
    strategy_on_full_size: Optional[
        Literal["DELETE_OLDEST_MEDIA", "DENY_NEW_MEDIA"]
    ] = Field(default=None, alias="StrategyOnFullSize")


class DescribeEdgeConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DescribeImageGenerationConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeMappedResourceConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MappedResourceConfigurationListItemModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    arn: Optional[str] = Field(default=None, alias="ARN")


class DescribeMediaStorageConfigurationInputRequestModel(BaseModel):
    channel_name: Optional[str] = Field(default=None, alias="ChannelName")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelARN")


class MediaStorageConfigurationModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DescribeNotificationConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class DescribeSignalingChannelInputRequestModel(BaseModel):
    channel_name: Optional[str] = Field(default=None, alias="ChannelName")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelARN")


class DescribeStreamInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class StreamInfoModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    media_type: Optional[str] = Field(default=None, alias="MediaType")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    version: Optional[str] = Field(default=None, alias="Version")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    data_retention_in_hours: Optional[int] = Field(
        default=None, alias="DataRetentionInHours"
    )


class GetDataEndpointInputRequestModel(BaseModel):
    ap_iname: Literal[
        "GET_CLIP",
        "GET_DASH_STREAMING_SESSION_URL",
        "GET_HLS_STREAMING_SESSION_URL",
        "GET_IMAGES",
        "GET_MEDIA",
        "GET_MEDIA_FOR_FRAGMENT_LIST",
        "LIST_FRAGMENTS",
        "PUT_MEDIA",
    ] = Field(alias="APIName")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class SingleMasterChannelEndpointConfigurationModel(BaseModel):
    protocols: Optional[Sequence[Literal["HTTPS", "WEBRTC", "WSS"]]] = Field(
        default=None, alias="Protocols"
    )
    role: Optional[Literal["MASTER", "VIEWER"]] = Field(default=None, alias="Role")


class ResourceEndpointListItemModel(BaseModel):
    protocol: Optional[Literal["HTTPS", "WEBRTC", "WSS"]] = Field(
        default=None, alias="Protocol"
    )
    resource_endpoint: Optional[str] = Field(default=None, alias="ResourceEndpoint")


class ImageGenerationDestinationConfigModel(BaseModel):
    uri: str = Field(alias="Uri")
    destination_region: str = Field(alias="DestinationRegion")


class StreamNameConditionModel(BaseModel):
    comparison_operator: Optional[Literal["BEGINS_WITH"]] = Field(
        default=None, alias="ComparisonOperator"
    )
    comparison_value: Optional[str] = Field(default=None, alias="ComparisonValue")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForStreamInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class MediaSourceConfigModel(BaseModel):
    media_uri_secret_arn: str = Field(alias="MediaUriSecretArn")
    media_uri_type: Literal["FILE_URI", "RTSP_URI"] = Field(alias="MediaUriType")


class NotificationDestinationConfigModel(BaseModel):
    uri: str = Field(alias="Uri")


class ScheduleConfigModel(BaseModel):
    schedule_expression: str = Field(alias="ScheduleExpression")
    duration_in_seconds: int = Field(alias="DurationInSeconds")


class TagStreamInputRequestModel(BaseModel):
    tags: Mapping[str, str] = Field(alias="Tags")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_key_list: Sequence[str] = Field(alias="TagKeyList")


class UntagStreamInputRequestModel(BaseModel):
    tag_key_list: Sequence[str] = Field(alias="TagKeyList")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class UpdateDataRetentionInputRequestModel(BaseModel):
    current_version: str = Field(alias="CurrentVersion")
    operation: Literal["DECREASE_DATA_RETENTION", "INCREASE_DATA_RETENTION"] = Field(
        alias="Operation"
    )
    data_retention_change_in_hours: int = Field(alias="DataRetentionChangeInHours")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class UpdateStreamInputRequestModel(BaseModel):
    current_version: str = Field(alias="CurrentVersion")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    media_type: Optional[str] = Field(default=None, alias="MediaType")


class ChannelInfoModel(BaseModel):
    channel_name: Optional[str] = Field(default=None, alias="ChannelName")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelARN")
    channel_type: Optional[Literal["FULL_MESH", "SINGLE_MASTER"]] = Field(
        default=None, alias="ChannelType"
    )
    channel_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="ChannelStatus")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    single_master_configuration: Optional[SingleMasterConfigurationModel] = Field(
        default=None, alias="SingleMasterConfiguration"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class UpdateSignalingChannelInputRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    current_version: str = Field(alias="CurrentVersion")
    single_master_configuration: Optional[SingleMasterConfigurationModel] = Field(
        default=None, alias="SingleMasterConfiguration"
    )


class ListSignalingChannelsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    channel_name_condition: Optional[ChannelNameConditionModel] = Field(
        default=None, alias="ChannelNameCondition"
    )


class CreateSignalingChannelInputRequestModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    channel_type: Optional[Literal["FULL_MESH", "SINGLE_MASTER"]] = Field(
        default=None, alias="ChannelType"
    )
    single_master_configuration: Optional[SingleMasterConfigurationModel] = Field(
        default=None, alias="SingleMasterConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateSignalingChannelOutputModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamOutputModel(BaseModel):
    stream_arn: str = Field(alias="StreamARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataEndpointOutputModel(BaseModel):
    data_endpoint: str = Field(alias="DataEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForStreamOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletionConfigModel(BaseModel):
    edge_retention_in_hours: Optional[int] = Field(
        default=None, alias="EdgeRetentionInHours"
    )
    local_size_config: Optional[LocalSizeConfigModel] = Field(
        default=None, alias="LocalSizeConfig"
    )
    delete_after_upload: Optional[bool] = Field(default=None, alias="DeleteAfterUpload")


class DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateModel(
    BaseModel
):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSignalingChannelsInputListSignalingChannelsPaginateModel(BaseModel):
    channel_name_condition: Optional[ChannelNameConditionModel] = Field(
        default=None, alias="ChannelNameCondition"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMappedResourceConfigurationOutputModel(BaseModel):
    mapped_resource_configuration_list: List[
        MappedResourceConfigurationListItemModel
    ] = Field(alias="MappedResourceConfigurationList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMediaStorageConfigurationOutputModel(BaseModel):
    media_storage_configuration: MediaStorageConfigurationModel = Field(
        alias="MediaStorageConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMediaStorageConfigurationInputRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    media_storage_configuration: MediaStorageConfigurationModel = Field(
        alias="MediaStorageConfiguration"
    )


class DescribeStreamOutputModel(BaseModel):
    stream_info: StreamInfoModel = Field(alias="StreamInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamsOutputModel(BaseModel):
    stream_info_list: List[StreamInfoModel] = Field(alias="StreamInfoList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSignalingChannelEndpointInputRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelARN")
    single_master_channel_endpoint_configuration: Optional[
        SingleMasterChannelEndpointConfigurationModel
    ] = Field(default=None, alias="SingleMasterChannelEndpointConfiguration")


class GetSignalingChannelEndpointOutputModel(BaseModel):
    resource_endpoint_list: List[ResourceEndpointListItemModel] = Field(
        alias="ResourceEndpointList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageGenerationConfigurationModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    image_selector_type: Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"] = Field(
        alias="ImageSelectorType"
    )
    destination_config: ImageGenerationDestinationConfigModel = Field(
        alias="DestinationConfig"
    )
    sampling_interval: int = Field(alias="SamplingInterval")
    format: Literal["JPEG", "PNG"] = Field(alias="Format")
    format_config: Optional[Dict[Literal["JPEGQuality"], str]] = Field(
        default=None, alias="FormatConfig"
    )
    width_pixels: Optional[int] = Field(default=None, alias="WidthPixels")
    height_pixels: Optional[int] = Field(default=None, alias="HeightPixels")


class ListStreamsInputListStreamsPaginateModel(BaseModel):
    stream_name_condition: Optional[StreamNameConditionModel] = Field(
        default=None, alias="StreamNameCondition"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    stream_name_condition: Optional[StreamNameConditionModel] = Field(
        default=None, alias="StreamNameCondition"
    )


class NotificationConfigurationModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    destination_config: NotificationDestinationConfigModel = Field(
        alias="DestinationConfig"
    )


class RecorderConfigModel(BaseModel):
    media_source_config: MediaSourceConfigModel = Field(alias="MediaSourceConfig")
    schedule_config: Optional[ScheduleConfigModel] = Field(
        default=None, alias="ScheduleConfig"
    )


class UploaderConfigModel(BaseModel):
    schedule_config: ScheduleConfigModel = Field(alias="ScheduleConfig")


class DescribeSignalingChannelOutputModel(BaseModel):
    channel_info: ChannelInfoModel = Field(alias="ChannelInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSignalingChannelsOutputModel(BaseModel):
    channel_info_list: List[ChannelInfoModel] = Field(alias="ChannelInfoList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageGenerationConfigurationOutputModel(BaseModel):
    image_generation_configuration: ImageGenerationConfigurationModel = Field(
        alias="ImageGenerationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateImageGenerationConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    image_generation_configuration: Optional[ImageGenerationConfigurationModel] = Field(
        default=None, alias="ImageGenerationConfiguration"
    )


class DescribeNotificationConfigurationOutputModel(BaseModel):
    notification_configuration: NotificationConfigurationModel = Field(
        alias="NotificationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNotificationConfigurationInputRequestModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )


class EdgeConfigModel(BaseModel):
    hub_device_arn: str = Field(alias="HubDeviceArn")
    recorder_config: RecorderConfigModel = Field(alias="RecorderConfig")
    uploader_config: Optional[UploaderConfigModel] = Field(
        default=None, alias="UploaderConfig"
    )
    deletion_config: Optional[DeletionConfigModel] = Field(
        default=None, alias="DeletionConfig"
    )


class DescribeEdgeConfigurationOutputModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    stream_arn: str = Field(alias="StreamARN")
    creation_time: datetime = Field(alias="CreationTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    sync_status: Literal[
        "ACKNOWLEDGED", "DELETE_FAILED", "DELETING", "IN_SYNC", "SYNCING", "SYNC_FAILED"
    ] = Field(alias="SyncStatus")
    failed_status_details: str = Field(alias="FailedStatusDetails")
    edge_config: EdgeConfigModel = Field(alias="EdgeConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartEdgeConfigurationUpdateInputRequestModel(BaseModel):
    edge_config: EdgeConfigModel = Field(alias="EdgeConfig")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    stream_arn: Optional[str] = Field(default=None, alias="StreamARN")


class StartEdgeConfigurationUpdateOutputModel(BaseModel):
    stream_name: str = Field(alias="StreamName")
    stream_arn: str = Field(alias="StreamARN")
    creation_time: datetime = Field(alias="CreationTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    sync_status: Literal[
        "ACKNOWLEDGED", "DELETE_FAILED", "DELETING", "IN_SYNC", "SYNCING", "SYNC_FAILED"
    ] = Field(alias="SyncStatus")
    failed_status_details: str = Field(alias="FailedStatusDetails")
    edge_config: EdgeConfigModel = Field(alias="EdgeConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
