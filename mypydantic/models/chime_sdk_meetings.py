# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttendeeCapabilitiesModel(BaseModel):
    audio: Literal["None", "Receive", "Send", "SendReceive"] = Field(alias="Audio")
    video: Literal["None", "Receive", "Send", "SendReceive"] = Field(alias="Video")
    content: Literal["None", "Receive", "Send", "SendReceive"] = Field(alias="Content")


class AttendeeIdItemModel(BaseModel):
    attendee_id: str = Field(alias="AttendeeId")


class AudioFeaturesModel(BaseModel):
    echo_reduction: Optional[Literal["AVAILABLE", "UNAVAILABLE"]] = Field(
        default=None, alias="EchoReduction"
    )


class CreateAttendeeErrorModel(BaseModel):
    external_user_id: Optional[str] = Field(default=None, alias="ExternalUserId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class NotificationsConfigurationModel(BaseModel):
    lambda_function_arn: Optional[str] = Field(default=None, alias="LambdaFunctionArn")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    sqs_queue_arn: Optional[str] = Field(default=None, alias="SqsQueueArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")


class DeleteMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class EngineTranscribeMedicalSettingsModel(BaseModel):
    language_code: Literal["en-US"] = Field(alias="LanguageCode")
    specialty: Literal[
        "CARDIOLOGY", "NEUROLOGY", "ONCOLOGY", "PRIMARYCARE", "RADIOLOGY", "UROLOGY"
    ] = Field(alias="Specialty")
    type: Literal["CONVERSATION", "DICTATION"] = Field(alias="Type")
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    region: Optional[
        Literal[
            "ap-southeast-2",
            "auto",
            "ca-central-1",
            "eu-west-1",
            "us-east-1",
            "us-east-2",
            "us-west-2",
        ]
    ] = Field(default=None, alias="Region")
    content_identification_type: Optional[Literal["PHI"]] = Field(
        default=None, alias="ContentIdentificationType"
    )


class EngineTranscribeSettingsModel(BaseModel):
    language_code: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-US",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    vocabulary_filter_method: Optional[Literal["mask", "remove", "tag"]] = Field(
        default=None, alias="VocabularyFilterMethod"
    )
    vocabulary_filter_name: Optional[str] = Field(
        default=None, alias="VocabularyFilterName"
    )
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    region: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-southeast-2",
            "auto",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-gov-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="Region")
    enable_partial_results_stabilization: Optional[bool] = Field(
        default=None, alias="EnablePartialResultsStabilization"
    )
    partial_results_stability: Optional[Literal["high", "low", "medium"]] = Field(
        default=None, alias="PartialResultsStability"
    )
    content_identification_type: Optional[Literal["PII"]] = Field(
        default=None, alias="ContentIdentificationType"
    )
    content_redaction_type: Optional[Literal["PII"]] = Field(
        default=None, alias="ContentRedactionType"
    )
    pii_entity_types: Optional[str] = Field(default=None, alias="PiiEntityTypes")
    language_model_name: Optional[str] = Field(default=None, alias="LanguageModelName")
    identify_language: Optional[bool] = Field(default=None, alias="IdentifyLanguage")
    language_options: Optional[str] = Field(default=None, alias="LanguageOptions")
    preferred_language: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-US",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
        ]
    ] = Field(default=None, alias="PreferredLanguage")


class GetAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")


class GetMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class ListAttendeesRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class MediaPlacementModel(BaseModel):
    audio_host_url: Optional[str] = Field(default=None, alias="AudioHostUrl")
    audio_fallback_url: Optional[str] = Field(default=None, alias="AudioFallbackUrl")
    signaling_url: Optional[str] = Field(default=None, alias="SignalingUrl")
    turn_control_url: Optional[str] = Field(default=None, alias="TurnControlUrl")
    screen_data_url: Optional[str] = Field(default=None, alias="ScreenDataUrl")
    screen_viewing_url: Optional[str] = Field(default=None, alias="ScreenViewingUrl")
    screen_sharing_url: Optional[str] = Field(default=None, alias="ScreenSharingUrl")
    event_ingestion_url: Optional[str] = Field(default=None, alias="EventIngestionUrl")


class StopMeetingTranscriptionRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AttendeeModel(BaseModel):
    external_user_id: Optional[str] = Field(default=None, alias="ExternalUserId")
    attendee_id: Optional[str] = Field(default=None, alias="AttendeeId")
    join_token: Optional[str] = Field(default=None, alias="JoinToken")
    capabilities: Optional[AttendeeCapabilitiesModel] = Field(
        default=None, alias="Capabilities"
    )


class CreateAttendeeRequestItemModel(BaseModel):
    external_user_id: str = Field(alias="ExternalUserId")
    capabilities: Optional[AttendeeCapabilitiesModel] = Field(
        default=None, alias="Capabilities"
    )


class CreateAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    external_user_id: str = Field(alias="ExternalUserId")
    capabilities: Optional[AttendeeCapabilitiesModel] = Field(
        default=None, alias="Capabilities"
    )


class UpdateAttendeeCapabilitiesRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")
    capabilities: AttendeeCapabilitiesModel = Field(alias="Capabilities")


class BatchUpdateAttendeeCapabilitiesExceptRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    excluded_attendee_ids: Sequence[AttendeeIdItemModel] = Field(
        alias="ExcludedAttendeeIds"
    )
    capabilities: AttendeeCapabilitiesModel = Field(alias="Capabilities")


class MeetingFeaturesConfigurationModel(BaseModel):
    audio: Optional[AudioFeaturesModel] = Field(default=None, alias="Audio")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TranscriptionConfigurationModel(BaseModel):
    engine_transcribe_settings: Optional[EngineTranscribeSettingsModel] = Field(
        default=None, alias="EngineTranscribeSettings"
    )
    engine_transcribe_medical_settings: Optional[
        EngineTranscribeMedicalSettingsModel
    ] = Field(default=None, alias="EngineTranscribeMedicalSettings")


class BatchCreateAttendeeResponseModel(BaseModel):
    attendees: List[AttendeeModel] = Field(alias="Attendees")
    errors: List[CreateAttendeeErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAttendeeResponseModel(BaseModel):
    attendee: AttendeeModel = Field(alias="Attendee")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAttendeeResponseModel(BaseModel):
    attendee: AttendeeModel = Field(alias="Attendee")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttendeesResponseModel(BaseModel):
    attendees: List[AttendeeModel] = Field(alias="Attendees")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAttendeeCapabilitiesResponseModel(BaseModel):
    attendee: AttendeeModel = Field(alias="Attendee")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendees: Sequence[CreateAttendeeRequestItemModel] = Field(alias="Attendees")


class CreateMeetingRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    media_region: str = Field(alias="MediaRegion")
    external_meeting_id: str = Field(alias="ExternalMeetingId")
    meeting_host_id: Optional[str] = Field(default=None, alias="MeetingHostId")
    notifications_configuration: Optional[NotificationsConfigurationModel] = Field(
        default=None, alias="NotificationsConfiguration"
    )
    meeting_features: Optional[MeetingFeaturesConfigurationModel] = Field(
        default=None, alias="MeetingFeatures"
    )
    primary_meeting_id: Optional[str] = Field(default=None, alias="PrimaryMeetingId")
    tenant_ids: Optional[Sequence[str]] = Field(default=None, alias="TenantIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateMeetingWithAttendeesRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    media_region: str = Field(alias="MediaRegion")
    external_meeting_id: str = Field(alias="ExternalMeetingId")
    attendees: Sequence[CreateAttendeeRequestItemModel] = Field(alias="Attendees")
    meeting_host_id: Optional[str] = Field(default=None, alias="MeetingHostId")
    meeting_features: Optional[MeetingFeaturesConfigurationModel] = Field(
        default=None, alias="MeetingFeatures"
    )
    notifications_configuration: Optional[NotificationsConfigurationModel] = Field(
        default=None, alias="NotificationsConfiguration"
    )
    primary_meeting_id: Optional[str] = Field(default=None, alias="PrimaryMeetingId")
    tenant_ids: Optional[Sequence[str]] = Field(default=None, alias="TenantIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MeetingModel(BaseModel):
    meeting_id: Optional[str] = Field(default=None, alias="MeetingId")
    meeting_host_id: Optional[str] = Field(default=None, alias="MeetingHostId")
    external_meeting_id: Optional[str] = Field(default=None, alias="ExternalMeetingId")
    media_region: Optional[str] = Field(default=None, alias="MediaRegion")
    media_placement: Optional[MediaPlacementModel] = Field(
        default=None, alias="MediaPlacement"
    )
    meeting_features: Optional[MeetingFeaturesConfigurationModel] = Field(
        default=None, alias="MeetingFeatures"
    )
    primary_meeting_id: Optional[str] = Field(default=None, alias="PrimaryMeetingId")
    tenant_ids: Optional[List[str]] = Field(default=None, alias="TenantIds")
    meeting_arn: Optional[str] = Field(default=None, alias="MeetingArn")


class StartMeetingTranscriptionRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    transcription_configuration: TranscriptionConfigurationModel = Field(
        alias="TranscriptionConfiguration"
    )


class CreateMeetingResponseModel(BaseModel):
    meeting: MeetingModel = Field(alias="Meeting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMeetingWithAttendeesResponseModel(BaseModel):
    meeting: MeetingModel = Field(alias="Meeting")
    attendees: List[AttendeeModel] = Field(alias="Attendees")
    errors: List[CreateAttendeeErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMeetingResponseModel(BaseModel):
    meeting: MeetingModel = Field(alias="Meeting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
