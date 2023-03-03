# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttachmentItemModel(BaseModel):
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    attachment_id: Optional[str] = Field(default=None, alias="AttachmentId")
    attachment_name: Optional[str] = Field(default=None, alias="AttachmentName")
    status: Optional[Literal["APPROVED", "IN_PROGRESS", "REJECTED"]] = Field(
        default=None, alias="Status"
    )


class CompleteAttachmentUploadRequestModel(BaseModel):
    attachment_ids: Sequence[str] = Field(alias="AttachmentIds")
    client_token: str = Field(alias="ClientToken")
    connection_token: str = Field(alias="ConnectionToken")


class ConnectionCredentialsModel(BaseModel):
    connection_token: Optional[str] = Field(default=None, alias="ConnectionToken")
    expiry: Optional[str] = Field(default=None, alias="Expiry")


class CreateParticipantConnectionRequestModel(BaseModel):
    participant_token: str = Field(alias="ParticipantToken")
    type: Optional[Sequence[Literal["CONNECTION_CREDENTIALS", "WEBSOCKET"]]] = Field(
        default=None, alias="Type"
    )
    connect_participant: Optional[bool] = Field(
        default=None, alias="ConnectParticipant"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class WebsocketModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    connection_expiry: Optional[str] = Field(default=None, alias="ConnectionExpiry")


class DisconnectParticipantRequestModel(BaseModel):
    connection_token: str = Field(alias="ConnectionToken")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class GetAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")
    connection_token: str = Field(alias="ConnectionToken")


class StartPositionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    absolute_time: Optional[str] = Field(default=None, alias="AbsoluteTime")
    most_recent: Optional[int] = Field(default=None, alias="MostRecent")


class ReceiptModel(BaseModel):
    delivered_timestamp: Optional[str] = Field(default=None, alias="DeliveredTimestamp")
    read_timestamp: Optional[str] = Field(default=None, alias="ReadTimestamp")
    recipient_participant_id: Optional[str] = Field(
        default=None, alias="RecipientParticipantId"
    )


class SendEventRequestModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    connection_token: str = Field(alias="ConnectionToken")
    content: Optional[str] = Field(default=None, alias="Content")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class SendMessageRequestModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    content: str = Field(alias="Content")
    connection_token: str = Field(alias="ConnectionToken")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class StartAttachmentUploadRequestModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    attachment_size_in_bytes: int = Field(alias="AttachmentSizeInBytes")
    attachment_name: str = Field(alias="AttachmentName")
    client_token: str = Field(alias="ClientToken")
    connection_token: str = Field(alias="ConnectionToken")


class UploadMetadataModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    url_expiry: Optional[str] = Field(default=None, alias="UrlExpiry")
    headers_to_include: Optional[Dict[str, str]] = Field(
        default=None, alias="HeadersToInclude"
    )


class GetAttachmentResponseModel(BaseModel):
    url: str = Field(alias="Url")
    url_expiry: str = Field(alias="UrlExpiry")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEventResponseModel(BaseModel):
    id: str = Field(alias="Id")
    absolute_time: str = Field(alias="AbsoluteTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendMessageResponseModel(BaseModel):
    id: str = Field(alias="Id")
    absolute_time: str = Field(alias="AbsoluteTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateParticipantConnectionResponseModel(BaseModel):
    websocket: WebsocketModel = Field(alias="Websocket")
    connection_credentials: ConnectionCredentialsModel = Field(
        alias="ConnectionCredentials"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTranscriptRequestModel(BaseModel):
    connection_token: str = Field(alias="ConnectionToken")
    contact_id: Optional[str] = Field(default=None, alias="ContactId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    scan_direction: Optional[Literal["BACKWARD", "FORWARD"]] = Field(
        default=None, alias="ScanDirection"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    start_position: Optional[StartPositionModel] = Field(
        default=None, alias="StartPosition"
    )


class MessageMetadataModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    receipts: Optional[List[ReceiptModel]] = Field(default=None, alias="Receipts")


class StartAttachmentUploadResponseModel(BaseModel):
    attachment_id: str = Field(alias="AttachmentId")
    upload_metadata: UploadMetadataModel = Field(alias="UploadMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ItemModel(BaseModel):
    absolute_time: Optional[str] = Field(default=None, alias="AbsoluteTime")
    content: Optional[str] = Field(default=None, alias="Content")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[
        Literal[
            "ATTACHMENT",
            "CHAT_ENDED",
            "CONNECTION_ACK",
            "EVENT",
            "MESSAGE",
            "MESSAGE_DELIVERED",
            "MESSAGE_READ",
            "PARTICIPANT_JOINED",
            "PARTICIPANT_LEFT",
            "TRANSFER_FAILED",
            "TRANSFER_SUCCEEDED",
            "TYPING",
        ]
    ] = Field(default=None, alias="Type")
    participant_id: Optional[str] = Field(default=None, alias="ParticipantId")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    participant_role: Optional[Literal["AGENT", "CUSTOMER", "SYSTEM"]] = Field(
        default=None, alias="ParticipantRole"
    )
    attachments: Optional[List[AttachmentItemModel]] = Field(
        default=None, alias="Attachments"
    )
    message_metadata: Optional[MessageMetadataModel] = Field(
        default=None, alias="MessageMetadata"
    )
    related_contact_id: Optional[str] = Field(default=None, alias="RelatedContactId")
    contact_id: Optional[str] = Field(default=None, alias="ContactId")


class GetTranscriptResponseModel(BaseModel):
    initial_contact_id: str = Field(alias="InitialContactId")
    transcript: List[ItemModel] = Field(alias="Transcript")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
