# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CloudWatchLogsDestinationConfigurationModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")


class CreateChatTokenRequestModel(BaseModel):
    room_identifier: str = Field(alias="roomIdentifier")
    user_id: str = Field(alias="userId")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    capabilities: Optional[
        Sequence[Literal["DELETE_MESSAGE", "DISCONNECT_USER", "SEND_MESSAGE"]]
    ] = Field(default=None, alias="capabilities")
    session_duration_in_minutes: Optional[int] = Field(
        default=None, alias="sessionDurationInMinutes"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class MessageReviewHandlerModel(BaseModel):
    fallback_result: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="fallbackResult"
    )
    uri: Optional[str] = Field(default=None, alias="uri")


class DeleteLoggingConfigurationRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")


class DeleteMessageRequestModel(BaseModel):
    id: str = Field(alias="id")
    room_identifier: str = Field(alias="roomIdentifier")
    reason: Optional[str] = Field(default=None, alias="reason")


class DeleteRoomRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")


class FirehoseDestinationConfigurationModel(BaseModel):
    delivery_stream_name: str = Field(alias="deliveryStreamName")


class S3DestinationConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")


class DisconnectUserRequestModel(BaseModel):
    room_identifier: str = Field(alias="roomIdentifier")
    user_id: str = Field(alias="userId")
    reason: Optional[str] = Field(default=None, alias="reason")


class GetLoggingConfigurationRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")


class GetRoomRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")


class ListLoggingConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRoomsRequestModel(BaseModel):
    logging_configuration_identifier: Optional[str] = Field(
        default=None, alias="loggingConfigurationIdentifier"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    message_review_handler_uri: Optional[str] = Field(
        default=None, alias="messageReviewHandlerUri"
    )
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class SendEventRequestModel(BaseModel):
    event_name: str = Field(alias="eventName")
    room_identifier: str = Field(alias="roomIdentifier")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CreateChatTokenResponseModel(BaseModel):
    session_expiration_time: datetime = Field(alias="sessionExpirationTime")
    token: str = Field(alias="token")
    token_expiration_time: datetime = Field(alias="tokenExpirationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMessageResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEventResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoomRequestModel(BaseModel):
    logging_configuration_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="loggingConfigurationIdentifiers"
    )
    maximum_message_length: Optional[int] = Field(
        default=None, alias="maximumMessageLength"
    )
    maximum_message_rate_per_second: Optional[int] = Field(
        default=None, alias="maximumMessageRatePerSecond"
    )
    message_review_handler: Optional[MessageReviewHandlerModel] = Field(
        default=None, alias="messageReviewHandler"
    )
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateRoomResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    id: str = Field(alias="id")
    logging_configuration_identifiers: List[str] = Field(
        alias="loggingConfigurationIdentifiers"
    )
    maximum_message_length: int = Field(alias="maximumMessageLength")
    maximum_message_rate_per_second: int = Field(alias="maximumMessageRatePerSecond")
    message_review_handler: MessageReviewHandlerModel = Field(
        alias="messageReviewHandler"
    )
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoomResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    id: str = Field(alias="id")
    logging_configuration_identifiers: List[str] = Field(
        alias="loggingConfigurationIdentifiers"
    )
    maximum_message_length: int = Field(alias="maximumMessageLength")
    maximum_message_rate_per_second: int = Field(alias="maximumMessageRatePerSecond")
    message_review_handler: MessageReviewHandlerModel = Field(
        alias="messageReviewHandler"
    )
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RoomSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    id: Optional[str] = Field(default=None, alias="id")
    logging_configuration_identifiers: Optional[List[str]] = Field(
        default=None, alias="loggingConfigurationIdentifiers"
    )
    message_review_handler: Optional[MessageReviewHandlerModel] = Field(
        default=None, alias="messageReviewHandler"
    )
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime")


class UpdateRoomRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")
    logging_configuration_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="loggingConfigurationIdentifiers"
    )
    maximum_message_length: Optional[int] = Field(
        default=None, alias="maximumMessageLength"
    )
    maximum_message_rate_per_second: Optional[int] = Field(
        default=None, alias="maximumMessageRatePerSecond"
    )
    message_review_handler: Optional[MessageReviewHandlerModel] = Field(
        default=None, alias="messageReviewHandler"
    )
    name: Optional[str] = Field(default=None, alias="name")


class UpdateRoomResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    id: str = Field(alias="id")
    logging_configuration_identifiers: List[str] = Field(
        alias="loggingConfigurationIdentifiers"
    )
    maximum_message_length: int = Field(alias="maximumMessageLength")
    maximum_message_rate_per_second: int = Field(alias="maximumMessageRatePerSecond")
    message_review_handler: MessageReviewHandlerModel = Field(
        alias="messageReviewHandler"
    )
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationConfigurationModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsDestinationConfigurationModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    firehose: Optional[FirehoseDestinationConfigurationModel] = Field(
        default=None, alias="firehose"
    )
    s3: Optional[S3DestinationConfigurationModel] = Field(default=None, alias="s3")


class ListRoomsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    rooms: List[RoomSummaryModel] = Field(alias="rooms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggingConfigurationRequestModel(BaseModel):
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateLoggingConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    state: Literal["ACTIVE"] = Field(alias="state")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoggingConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    state: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="state")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingConfigurationSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    destination_configuration: Optional[DestinationConfigurationModel] = Field(
        default=None, alias="destinationConfiguration"
    )
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    state: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DELETE_FAILED",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="state")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    update_time: Optional[datetime] = Field(default=None, alias="updateTime")


class UpdateLoggingConfigurationRequestModel(BaseModel):
    identifier: str = Field(alias="identifier")
    destination_configuration: Optional[DestinationConfigurationModel] = Field(
        default=None, alias="destinationConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="name")


class UpdateLoggingConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    create_time: datetime = Field(alias="createTime")
    destination_configuration: DestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    state: Literal["ACTIVE"] = Field(alias="state")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLoggingConfigurationsResponseModel(BaseModel):
    logging_configurations: List[LoggingConfigurationSummaryModel] = Field(
        alias="loggingConfigurations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
