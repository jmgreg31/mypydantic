# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountSettingsModel(BaseModel):
    disable_remote_control: Optional[bool] = Field(
        default=None, alias="DisableRemoteControl"
    )
    enable_dial_out: Optional[bool] = Field(default=None, alias="EnableDialOut")


class SigninDelegateGroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class AddressModel(BaseModel):
    street_name: Optional[str] = Field(default=None, alias="streetName")
    street_suffix: Optional[str] = Field(default=None, alias="streetSuffix")
    post_directional: Optional[str] = Field(default=None, alias="postDirectional")
    pre_directional: Optional[str] = Field(default=None, alias="preDirectional")
    street_number: Optional[str] = Field(default=None, alias="streetNumber")
    city: Optional[str] = Field(default=None, alias="city")
    state: Optional[str] = Field(default=None, alias="state")
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    postal_code_plus4: Optional[str] = Field(default=None, alias="postalCodePlus4")
    country: Optional[str] = Field(default=None, alias="country")


class AlexaForBusinessMetadataModel(BaseModel):
    is_alexa_for_business_enabled: Optional[bool] = Field(
        default=None, alias="IsAlexaForBusinessEnabled"
    )
    alexa_for_business_room_arn: Optional[str] = Field(
        default=None, alias="AlexaForBusinessRoomArn"
    )


class IdentityModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ChannelRetentionSettingsModel(BaseModel):
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class AppInstanceStreamingConfigurationModel(BaseModel):
    app_instance_data_type: Literal["Channel", "ChannelMessage"] = Field(
        alias="AppInstanceDataType"
    )
    resource_arn: str = Field(alias="ResourceArn")


class AppInstanceSummaryModel(BaseModel):
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class AppInstanceModel(BaseModel):
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class AppInstanceUserMembershipSummaryModel(BaseModel):
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    read_marker_timestamp: Optional[datetime] = Field(
        default=None, alias="ReadMarkerTimestamp"
    )


class AppInstanceUserSummaryModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class AppInstanceUserModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class AudioArtifactsConfigurationModel(BaseModel):
    mux_type: Literal["AudioOnly", "AudioWithActiveSpeakerVideo"] = Field(
        alias="MuxType"
    )


class ContentArtifactsConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")
    mux_type: Optional[Literal["ContentOnly"]] = Field(default=None, alias="MuxType")


class VideoArtifactsConfigurationModel(BaseModel):
    state: Literal["Disabled", "Enabled"] = Field(alias="State")
    mux_type: Optional[Literal["VideoOnly"]] = Field(default=None, alias="MuxType")


class AssociatePhoneNumberWithUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")
    e164_phone_number: str = Field(alias="E164PhoneNumber")


class AssociatePhoneNumbersWithVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")
    force_associate: Optional[bool] = Field(default=None, alias="ForceAssociate")


class PhoneNumberErrorModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PhoneNumberAssociationsExist",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociatePhoneNumbersWithVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")
    force_associate: Optional[bool] = Field(default=None, alias="ForceAssociate")


class AttendeeModel(BaseModel):
    external_user_id: Optional[str] = Field(default=None, alias="ExternalUserId")
    attendee_id: Optional[str] = Field(default=None, alias="AttendeeId")
    join_token: Optional[str] = Field(default=None, alias="JoinToken")


class CreateAttendeeErrorModel(BaseModel):
    external_user_id: Optional[str] = Field(default=None, alias="ExternalUserId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchCreateChannelMembershipErrorModel(BaseModel):
    member_arn: Optional[str] = Field(default=None, alias="MemberArn")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PhoneNumberAssociationsExist",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchCreateChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arns: Sequence[str] = Field(alias="MemberArns")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class MembershipItemModel(BaseModel):
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    role: Optional[Literal["Administrator", "Member"]] = Field(
        default=None, alias="Role"
    )


class MemberErrorModel(BaseModel):
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PhoneNumberAssociationsExist",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchDeletePhoneNumberRequestModel(BaseModel):
    phone_number_ids: Sequence[str] = Field(alias="PhoneNumberIds")


class BatchSuspendUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id_list: Sequence[str] = Field(alias="UserIdList")


class UserErrorModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="UserId")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "BadRequest",
            "Conflict",
            "Forbidden",
            "NotFound",
            "PhoneNumberAssociationsExist",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchUnsuspendUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id_list: Sequence[str] = Field(alias="UserIdList")


class UpdatePhoneNumberRequestItemModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    product_type: Optional[
        Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    calling_name: Optional[str] = Field(default=None, alias="CallingName")


class BotModel(BaseModel):
    bot_id: Optional[str] = Field(default=None, alias="BotId")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    bot_type: Optional[Literal["ChatBot"]] = Field(default=None, alias="BotType")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    bot_email: Optional[str] = Field(default=None, alias="BotEmail")
    security_token: Optional[str] = Field(default=None, alias="SecurityToken")


class BusinessCallingSettingsModel(BaseModel):
    cdr_bucket: Optional[str] = Field(default=None, alias="CdrBucket")


class CandidateAddressModel(BaseModel):
    street_info: Optional[str] = Field(default=None, alias="streetInfo")
    street_number: Optional[str] = Field(default=None, alias="streetNumber")
    city: Optional[str] = Field(default=None, alias="city")
    state: Optional[str] = Field(default=None, alias="state")
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    postal_code_plus4: Optional[str] = Field(default=None, alias="postalCodePlus4")
    country: Optional[str] = Field(default=None, alias="country")


class ChannelSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    last_message_timestamp: Optional[datetime] = Field(
        default=None, alias="LastMessageTimestamp"
    )


class ConversationRetentionSettingsModel(BaseModel):
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class CreateAccountRequestModel(BaseModel):
    name: str = Field(alias="Name")


class CreateAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateBotRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    display_name: str = Field(alias="DisplayName")
    domain: Optional[str] = Field(default=None, alias="Domain")


class CreateChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class CreateChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    type: Literal["DEFAULT", "HIDDEN"] = Field(alias="Type")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class CreateChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class CreateMeetingDialOutRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    from_phone_number: str = Field(alias="FromPhoneNumber")
    to_phone_number: str = Field(alias="ToPhoneNumber")
    join_token: str = Field(alias="JoinToken")


class MeetingNotificationConfigurationModel(BaseModel):
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    sqs_queue_arn: Optional[str] = Field(default=None, alias="SqsQueueArn")


class CreatePhoneNumberOrderRequestModel(BaseModel):
    product_type: Literal[
        "BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"
    ] = Field(alias="ProductType")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class GeoMatchParamsModel(BaseModel):
    country: str = Field(alias="Country")
    area_code: str = Field(alias="AreaCode")


class CreateRoomMembershipRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    member_id: str = Field(alias="MemberId")
    role: Optional[Literal["Administrator", "Member"]] = Field(
        default=None, alias="Role"
    )


class CreateRoomRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class RoomModel(BaseModel):
    room_id: Optional[str] = Field(default=None, alias="RoomId")
    name: Optional[str] = Field(default=None, alias="Name")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class CreateSipMediaApplicationCallRequestModel(BaseModel):
    from_phone_number: str = Field(alias="FromPhoneNumber")
    to_phone_number: str = Field(alias="ToPhoneNumber")
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    sip_headers: Optional[Mapping[str, str]] = Field(default=None, alias="SipHeaders")


class SipMediaApplicationCallModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class SipMediaApplicationEndpointModel(BaseModel):
    lambda_arn: Optional[str] = Field(default=None, alias="LambdaArn")


class SipRuleTargetApplicationModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class CreateUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    username: Optional[str] = Field(default=None, alias="Username")
    email: Optional[str] = Field(default=None, alias="Email")
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )


class VoiceConnectorItemModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    priority: int = Field(alias="Priority")


class CreateVoiceConnectorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    require_encryption: bool = Field(alias="RequireEncryption")
    aws_region: Optional[Literal["us-east-1", "us-west-2"]] = Field(
        default=None, alias="AwsRegion"
    )


class VoiceConnectorModel(BaseModel):
    voice_connector_id: Optional[str] = Field(default=None, alias="VoiceConnectorId")
    aws_region: Optional[Literal["us-east-1", "us-west-2"]] = Field(
        default=None, alias="AwsRegion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    outbound_host_name: Optional[str] = Field(default=None, alias="OutboundHostName")
    require_encryption: Optional[bool] = Field(default=None, alias="RequireEncryption")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    voice_connector_arn: Optional[str] = Field(default=None, alias="VoiceConnectorArn")


class CredentialModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")


class DNISEmergencyCallingConfigurationModel(BaseModel):
    emergency_phone_number: str = Field(alias="EmergencyPhoneNumber")
    calling_country: str = Field(alias="CallingCountry")
    test_phone_number: Optional[str] = Field(default=None, alias="TestPhoneNumber")


class DeleteAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class DeleteAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DeleteAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DeleteAppInstanceStreamingConfigurationsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DeleteAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")


class DeleteAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")


class DeleteChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DeleteChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DeleteChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DeleteChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DeleteChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DeleteEventsConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")


class DeleteMediaCapturePipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class DeleteMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class DeletePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class DeleteProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")


class DeleteRoomMembershipRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    member_id: str = Field(alias="MemberId")


class DeleteRoomRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")


class DeleteSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class DeleteSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")


class DeleteVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")


class DeleteVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    usernames: Sequence[str] = Field(alias="Usernames")


class DeleteVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DescribeAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DescribeAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DescribeAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")


class DescribeChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DescribeChannelMembershipForAppInstanceUserRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DescribeChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DescribeChannelModeratedByAppInstanceUserRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DescribeChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DescribeChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class DisassociatePhoneNumberFromUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")


class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class DisassociatePhoneNumbersFromVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class DisassociateSigninDelegateGroupsFromAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    group_names: Sequence[str] = Field(alias="GroupNames")


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
    language_code: Literal[
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
    ] = Field(alias="LanguageCode")
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


class EventsConfigurationModel(BaseModel):
    bot_id: Optional[str] = Field(default=None, alias="BotId")
    outbound_events_http_s_endpoint: Optional[str] = Field(
        default=None, alias="OutboundEventsHTTPSEndpoint"
    )
    lambda_function_arn: Optional[str] = Field(default=None, alias="LambdaFunctionArn")


class GetAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class GetAccountSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class GetAppInstanceRetentionSettingsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class GetAppInstanceStreamingConfigurationsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class GetAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")


class GetBotRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")


class GetChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class GetEventsConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")


class VoiceConnectorSettingsModel(BaseModel):
    cdr_bucket: Optional[str] = Field(default=None, alias="CdrBucket")


class GetMediaCapturePipelineRequestModel(BaseModel):
    media_pipeline_id: str = Field(alias="MediaPipelineId")


class GetMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class MessagingSessionEndpointModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")


class GetPhoneNumberOrderRequestModel(BaseModel):
    phone_number_order_id: str = Field(alias="PhoneNumberOrderId")


class GetPhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class GetProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")


class GetRetentionSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class GetRoomRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")


class GetSipMediaApplicationLoggingConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class SipMediaApplicationLoggingConfigurationModel(BaseModel):
    enable_sip_media_application_message_logs: Optional[bool] = Field(
        default=None, alias="EnableSipMediaApplicationMessageLogs"
    )


class GetSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class GetSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")


class GetUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")


class GetUserSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")


class GetVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")


class GetVoiceConnectorLoggingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class LoggingConfigurationModel(BaseModel):
    enable_s_ip_logs: Optional[bool] = Field(default=None, alias="EnableSIPLogs")
    enable_media_metric_logs: Optional[bool] = Field(
        default=None, alias="EnableMediaMetricLogs"
    )


class GetVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class ProxyModel(BaseModel):
    default_session_expiry_minutes: Optional[int] = Field(
        default=None, alias="DefaultSessionExpiryMinutes"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    fall_back_phone_number: Optional[str] = Field(
        default=None, alias="FallBackPhoneNumber"
    )
    phone_number_countries: Optional[List[str]] = Field(
        default=None, alias="PhoneNumberCountries"
    )


class GetVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorTerminationHealthRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class TerminationHealthModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    source: Optional[str] = Field(default=None, alias="Source")


class GetVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class TerminationModel(BaseModel):
    cps_limit: Optional[int] = Field(default=None, alias="CpsLimit")
    default_phone_number: Optional[str] = Field(
        default=None, alias="DefaultPhoneNumber"
    )
    calling_regions: Optional[List[str]] = Field(default=None, alias="CallingRegions")
    cidr_allowed_list: Optional[List[str]] = Field(
        default=None, alias="CidrAllowedList"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class InviteModel(BaseModel):
    invite_id: Optional[str] = Field(default=None, alias="InviteId")
    status: Optional[Literal["Accepted", "Failed", "Pending"]] = Field(
        default=None, alias="Status"
    )
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    email_status: Optional[Literal["Failed", "NotSent", "Sent"]] = Field(
        default=None, alias="EmailStatus"
    )


class InviteUsersRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_email_list: Sequence[str] = Field(alias="UserEmailList")
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccountsRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    user_email: Optional[str] = Field(default=None, alias="UserEmail")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAppInstanceAdminsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppInstanceUsersRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppInstancesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAttendeeTagsRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")


class ListAttendeesRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListBotsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelBansRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelMembershipsForAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelMembershipsRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelMessagesRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    not_before: Optional[Union[datetime, str]] = Field(default=None, alias="NotBefore")
    not_after: Optional[Union[datetime, str]] = Field(default=None, alias="NotAfter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelModeratorsRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelsModeratedByAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListChannelsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListMediaCapturePipelinesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMeetingTagsRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class ListMeetingsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPhoneNumberOrdersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPhoneNumbersRequestModel(BaseModel):
    status: Optional[
        Literal[
            "AcquireFailed",
            "AcquireInProgress",
            "Assigned",
            "DeleteFailed",
            "DeleteInProgress",
            "ReleaseFailed",
            "ReleaseInProgress",
            "Unassigned",
        ]
    ] = Field(default=None, alias="Status")
    product_type: Optional[
        Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    filter_name: Optional[
        Literal[
            "AccountId",
            "SipRuleId",
            "UserId",
            "VoiceConnectorGroupId",
            "VoiceConnectorId",
        ]
    ] = Field(default=None, alias="FilterName")
    filter_value: Optional[str] = Field(default=None, alias="FilterValue")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListProxySessionsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    status: Optional[Literal["Closed", "InProgress", "Open"]] = Field(
        default=None, alias="Status"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRoomMembershipsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRoomsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSipMediaApplicationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSipRulesRequestModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSupportedPhoneNumberCountriesRequestModel(BaseModel):
    product_type: Literal[
        "BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"
    ] = Field(alias="ProductType")


class PhoneNumberCountryModel(BaseModel):
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    supported_phone_number_types: Optional[List[Literal["Local", "TollFree"]]] = Field(
        default=None, alias="SupportedPhoneNumberTypes"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class ListUsersRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_email: Optional[str] = Field(default=None, alias="UserEmail")
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVoiceConnectorGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class ListVoiceConnectorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class LogoutUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")


class MediaPlacementModel(BaseModel):
    audio_host_url: Optional[str] = Field(default=None, alias="AudioHostUrl")
    audio_fallback_url: Optional[str] = Field(default=None, alias="AudioFallbackUrl")
    screen_data_url: Optional[str] = Field(default=None, alias="ScreenDataUrl")
    screen_sharing_url: Optional[str] = Field(default=None, alias="ScreenSharingUrl")
    screen_viewing_url: Optional[str] = Field(default=None, alias="ScreenViewingUrl")
    signaling_url: Optional[str] = Field(default=None, alias="SignalingUrl")
    turn_control_url: Optional[str] = Field(default=None, alias="TurnControlUrl")
    event_ingestion_url: Optional[str] = Field(default=None, alias="EventIngestionUrl")


class MemberModel(BaseModel):
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    member_type: Optional[Literal["Bot", "User", "Webhook"]] = Field(
        default=None, alias="MemberType"
    )
    email: Optional[str] = Field(default=None, alias="Email")
    full_name: Optional[str] = Field(default=None, alias="FullName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class OrderedPhoneNumberModel(BaseModel):
    e164_phone_number: Optional[str] = Field(default=None, alias="E164PhoneNumber")
    status: Optional[Literal["Acquired", "Failed", "Processing"]] = Field(
        default=None, alias="Status"
    )


class OriginationRouteModel(BaseModel):
    host: Optional[str] = Field(default=None, alias="Host")
    port: Optional[int] = Field(default=None, alias="Port")
    protocol: Optional[Literal["TCP", "UDP"]] = Field(default=None, alias="Protocol")
    priority: Optional[int] = Field(default=None, alias="Priority")
    weight: Optional[int] = Field(default=None, alias="Weight")


class ParticipantModel(BaseModel):
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    proxy_phone_number: Optional[str] = Field(default=None, alias="ProxyPhoneNumber")


class PhoneNumberAssociationModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    name: Optional[
        Literal[
            "AccountId",
            "SipRuleId",
            "UserId",
            "VoiceConnectorGroupId",
            "VoiceConnectorId",
        ]
    ] = Field(default=None, alias="Name")
    associated_timestamp: Optional[datetime] = Field(
        default=None, alias="AssociatedTimestamp"
    )


class PhoneNumberCapabilitiesModel(BaseModel):
    inbound_call: Optional[bool] = Field(default=None, alias="InboundCall")
    outbound_call: Optional[bool] = Field(default=None, alias="OutboundCall")
    inbound_s_ms: Optional[bool] = Field(default=None, alias="InboundSMS")
    outbound_s_ms: Optional[bool] = Field(default=None, alias="OutboundSMS")
    inbound_mms: Optional[bool] = Field(default=None, alias="InboundMMS")
    outbound_mms: Optional[bool] = Field(default=None, alias="OutboundMMS")


class PutEventsConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")
    outbound_events_http_s_endpoint: Optional[str] = Field(
        default=None, alias="OutboundEventsHTTPSEndpoint"
    )
    lambda_function_arn: Optional[str] = Field(default=None, alias="LambdaFunctionArn")


class PutVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    default_session_expiry_minutes: int = Field(alias="DefaultSessionExpiryMinutes")
    phone_number_pool_countries: Sequence[str] = Field(alias="PhoneNumberPoolCountries")
    fall_back_phone_number: Optional[str] = Field(
        default=None, alias="FallBackPhoneNumber"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class RedactChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class RedactConversationMessageRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    conversation_id: str = Field(alias="ConversationId")
    message_id: str = Field(alias="MessageId")


class RedactRoomMessageRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    message_id: str = Field(alias="MessageId")


class RegenerateSecurityTokenRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")


class ResetPersonalPINRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")


class RestorePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class RoomRetentionSettingsModel(BaseModel):
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class SearchAvailablePhoneNumbersRequestModel(BaseModel):
    area_code: Optional[str] = Field(default=None, alias="AreaCode")
    city: Optional[str] = Field(default=None, alias="City")
    country: Optional[str] = Field(default=None, alias="Country")
    state: Optional[str] = Field(default=None, alias="State")
    toll_free_prefix: Optional[str] = Field(default=None, alias="TollFreePrefix")
    phone_number_type: Optional[Literal["Local", "TollFree"]] = Field(
        default=None, alias="PhoneNumberType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SelectedVideoStreamsModel(BaseModel):
    attendee_ids: Optional[Sequence[str]] = Field(default=None, alias="AttendeeIds")
    external_user_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ExternalUserIds"
    )


class SendChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    content: str = Field(alias="Content")
    type: Literal["CONTROL", "STANDARD"] = Field(alias="Type")
    persistence: Literal["NON_PERSISTENT", "PERSISTENT"] = Field(alias="Persistence")
    client_request_token: str = Field(alias="ClientRequestToken")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class StopMeetingTranscriptionRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")


class StreamingNotificationTargetModel(BaseModel):
    notification_target: Literal["EventBridge", "SNS", "SQS"] = Field(
        alias="NotificationTarget"
    )


class TelephonySettingsModel(BaseModel):
    inbound_calling: bool = Field(alias="InboundCalling")
    outbound_calling: bool = Field(alias="OutboundCalling")
    s_ms: bool = Field(alias="SMS")


class UntagAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: Optional[str] = Field(default=None, alias="Name")
    default_license: Optional[Literal["Basic", "Plus", "Pro", "ProTrial"]] = Field(
        default=None, alias="DefaultLicense"
    )


class UpdateAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    name: str = Field(alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class UpdateAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    name: str = Field(alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class UpdateBotRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bot_id: str = Field(alias="BotId")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class UpdateChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    content: Optional[str] = Field(default=None, alias="Content")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class UpdateChannelReadMarkerRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class UpdateChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    name: str = Field(alias="Name")
    mode: Literal["RESTRICTED", "UNRESTRICTED"] = Field(alias="Mode")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class UpdatePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    product_type: Optional[
        Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    calling_name: Optional[str] = Field(default=None, alias="CallingName")


class UpdatePhoneNumberSettingsRequestModel(BaseModel):
    calling_name: str = Field(alias="CallingName")


class UpdateProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")
    capabilities: Sequence[Literal["SMS", "Voice"]] = Field(alias="Capabilities")
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")


class UpdateRoomMembershipRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    member_id: str = Field(alias="MemberId")
    role: Optional[Literal["Administrator", "Member"]] = Field(
        default=None, alias="Role"
    )


class UpdateRoomRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateSipMediaApplicationCallRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    transaction_id: str = Field(alias="TransactionId")
    arguments: Mapping[str, str] = Field(alias="Arguments")


class UpdateVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    name: str = Field(alias="Name")
    require_encryption: bool = Field(alias="RequireEncryption")


class ValidateE911AddressRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    street_number: str = Field(alias="StreetNumber")
    street_info: str = Field(alias="StreetInfo")
    city: str = Field(alias="City")
    state: str = Field(alias="State")
    country: str = Field(alias="Country")
    postal_code: str = Field(alias="PostalCode")


class UpdateAccountSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    account_settings: AccountSettingsModel = Field(alias="AccountSettings")


class AccountModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    account_type: Optional[
        Literal["EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC", "Team"]
    ] = Field(default=None, alias="AccountType")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    default_license: Optional[Literal["Basic", "Plus", "Pro", "ProTrial"]] = Field(
        default=None, alias="DefaultLicense"
    )
    supported_licenses: Optional[
        List[Literal["Basic", "Plus", "Pro", "ProTrial"]]
    ] = Field(default=None, alias="SupportedLicenses")
    account_status: Optional[Literal["Active", "Suspended"]] = Field(
        default=None, alias="AccountStatus"
    )
    signin_delegate_groups: Optional[List[SigninDelegateGroupModel]] = Field(
        default=None, alias="SigninDelegateGroups"
    )


class AssociateSigninDelegateGroupsWithAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    signin_delegate_groups: Sequence[SigninDelegateGroupModel] = Field(
        alias="SigninDelegateGroups"
    )


class UpdateUserRequestItemModel(BaseModel):
    user_id: str = Field(alias="UserId")
    license_type: Optional[Literal["Basic", "Plus", "Pro", "ProTrial"]] = Field(
        default=None, alias="LicenseType"
    )
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )
    alexa_for_business_metadata: Optional[AlexaForBusinessMetadataModel] = Field(
        default=None, alias="AlexaForBusinessMetadata"
    )


class UpdateUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")
    license_type: Optional[Literal["Basic", "Plus", "Pro", "ProTrial"]] = Field(
        default=None, alias="LicenseType"
    )
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )
    alexa_for_business_metadata: Optional[AlexaForBusinessMetadataModel] = Field(
        default=None, alias="AlexaForBusinessMetadata"
    )


class UserModel(BaseModel):
    user_id: str = Field(alias="UserId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    primary_email: Optional[str] = Field(default=None, alias="PrimaryEmail")
    primary_provisioned_number: Optional[str] = Field(
        default=None, alias="PrimaryProvisionedNumber"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    license_type: Optional[Literal["Basic", "Plus", "Pro", "ProTrial"]] = Field(
        default=None, alias="LicenseType"
    )
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )
    user_registration_status: Optional[
        Literal["Registered", "Suspended", "Unregistered"]
    ] = Field(default=None, alias="UserRegistrationStatus")
    user_invitation_status: Optional[Literal["Accepted", "Failed", "Pending"]] = Field(
        default=None, alias="UserInvitationStatus"
    )
    registered_on: Optional[datetime] = Field(default=None, alias="RegisteredOn")
    invited_on: Optional[datetime] = Field(default=None, alias="InvitedOn")
    alexa_for_business_metadata: Optional[AlexaForBusinessMetadataModel] = Field(
        default=None, alias="AlexaForBusinessMetadata"
    )
    personal_p_in: Optional[str] = Field(default=None, alias="PersonalPIN")


class AppInstanceAdminSummaryModel(BaseModel):
    admin: Optional[IdentityModel] = Field(default=None, alias="Admin")


class AppInstanceAdminModel(BaseModel):
    admin: Optional[IdentityModel] = Field(default=None, alias="Admin")
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )


class BatchChannelMembershipsModel(BaseModel):
    invited_by: Optional[IdentityModel] = Field(default=None, alias="InvitedBy")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    members: Optional[List[IdentityModel]] = Field(default=None, alias="Members")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")


class ChannelBanSummaryModel(BaseModel):
    member: Optional[IdentityModel] = Field(default=None, alias="Member")


class ChannelBanModel(BaseModel):
    member: Optional[IdentityModel] = Field(default=None, alias="Member")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    created_by: Optional[IdentityModel] = Field(default=None, alias="CreatedBy")


class ChannelMembershipSummaryModel(BaseModel):
    member: Optional[IdentityModel] = Field(default=None, alias="Member")


class ChannelMembershipModel(BaseModel):
    invited_by: Optional[IdentityModel] = Field(default=None, alias="InvitedBy")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    member: Optional[IdentityModel] = Field(default=None, alias="Member")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class ChannelMessageSummaryModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    content: Optional[str] = Field(default=None, alias="Content")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    type: Optional[Literal["CONTROL", "STANDARD"]] = Field(default=None, alias="Type")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    last_edited_timestamp: Optional[datetime] = Field(
        default=None, alias="LastEditedTimestamp"
    )
    sender: Optional[IdentityModel] = Field(default=None, alias="Sender")
    redacted: Optional[bool] = Field(default=None, alias="Redacted")


class ChannelMessageModel(BaseModel):
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    content: Optional[str] = Field(default=None, alias="Content")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    type: Optional[Literal["CONTROL", "STANDARD"]] = Field(default=None, alias="Type")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_edited_timestamp: Optional[datetime] = Field(
        default=None, alias="LastEditedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    sender: Optional[IdentityModel] = Field(default=None, alias="Sender")
    redacted: Optional[bool] = Field(default=None, alias="Redacted")
    persistence: Optional[Literal["NON_PERSISTENT", "PERSISTENT"]] = Field(
        default=None, alias="Persistence"
    )


class ChannelModeratorSummaryModel(BaseModel):
    moderator: Optional[IdentityModel] = Field(default=None, alias="Moderator")


class ChannelModeratorModel(BaseModel):
    moderator: Optional[IdentityModel] = Field(default=None, alias="Moderator")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    created_by: Optional[IdentityModel] = Field(default=None, alias="CreatedBy")


class ChannelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    created_by: Optional[IdentityModel] = Field(default=None, alias="CreatedBy")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_message_timestamp: Optional[datetime] = Field(
        default=None, alias="LastMessageTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class AppInstanceRetentionSettingsModel(BaseModel):
    channel_retention_settings: Optional[ChannelRetentionSettingsModel] = Field(
        default=None, alias="ChannelRetentionSettings"
    )


class PutAppInstanceStreamingConfigurationsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_streaming_configurations: Sequence[
        AppInstanceStreamingConfigurationModel
    ] = Field(alias="AppInstanceStreamingConfigurations")


class ArtifactsConfigurationModel(BaseModel):
    audio: AudioArtifactsConfigurationModel = Field(alias="Audio")
    video: VideoArtifactsConfigurationModel = Field(alias="Video")
    content: ContentArtifactsConfigurationModel = Field(alias="Content")


class AssociatePhoneNumbersWithVoiceConnectorGroupResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociatePhoneNumbersWithVoiceConnectorResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeletePhoneNumberResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePhoneNumberResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceAdminResponseModel(BaseModel):
    app_instance_admin: IdentityModel = Field(alias="AppInstanceAdmin")
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceUserResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelBanResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelMembershipResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelModeratorResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator: IdentityModel = Field(alias="ChannelModerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMeetingDialOutResponseModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceResponseModel(BaseModel):
    app_instance: AppInstanceModel = Field(alias="AppInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceUserResponseModel(BaseModel):
    app_instance_user: AppInstanceUserModel = Field(alias="AppInstanceUser")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePhoneNumbersFromVoiceConnectorResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSettingsResponseModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="AccountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppInstanceStreamingConfigurationsResponseModel(BaseModel):
    app_instance_streaming_configurations: List[
        AppInstanceStreamingConfigurationModel
    ] = Field(alias="AppInstanceStreamingConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberSettingsResponseModel(BaseModel):
    calling_name: str = Field(alias="CallingName")
    calling_name_updated_timestamp: datetime = Field(
        alias="CallingNameUpdatedTimestamp"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstanceUsersResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_users: List[AppInstanceUserSummaryModel] = Field(
        alias="AppInstanceUsers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstancesResponseModel(BaseModel):
    app_instances: List[AppInstanceSummaryModel] = Field(alias="AppInstances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorTerminationCredentialsResponseModel(BaseModel):
    usernames: List[str] = Field(alias="Usernames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppInstanceStreamingConfigurationsResponseModel(BaseModel):
    app_instance_streaming_configurations: List[
        AppInstanceStreamingConfigurationModel
    ] = Field(alias="AppInstanceStreamingConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RedactChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAvailablePhoneNumbersResponseModel(BaseModel):
    e164_phone_numbers: List[str] = Field(alias="E164PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppInstanceResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppInstanceUserResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelReadMarkerResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
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


class BatchCreateAttendeeResponseModel(BaseModel):
    attendees: List[AttendeeModel] = Field(alias="Attendees")
    errors: List[CreateAttendeeErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateRoomMembershipRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    room_id: str = Field(alias="RoomId")
    membership_item_list: Sequence[MembershipItemModel] = Field(
        alias="MembershipItemList"
    )


class BatchCreateRoomMembershipResponseModel(BaseModel):
    errors: List[MemberErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchSuspendUserResponseModel(BaseModel):
    user_errors: List[UserErrorModel] = Field(alias="UserErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUnsuspendUserResponseModel(BaseModel):
    user_errors: List[UserErrorModel] = Field(alias="UserErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateUserResponseModel(BaseModel):
    user_errors: List[UserErrorModel] = Field(alias="UserErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePhoneNumberRequestModel(BaseModel):
    update_phone_number_request_items: Sequence[
        UpdatePhoneNumberRequestItemModel
    ] = Field(alias="UpdatePhoneNumberRequestItems")


class CreateBotResponseModel(BaseModel):
    bot: BotModel = Field(alias="Bot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotResponseModel(BaseModel):
    bot: BotModel = Field(alias="Bot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBotsResponseModel(BaseModel):
    bots: List[BotModel] = Field(alias="Bots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegenerateSecurityTokenResponseModel(BaseModel):
    bot: BotModel = Field(alias="Bot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotResponseModel(BaseModel):
    bot: BotModel = Field(alias="Bot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateE911AddressResponseModel(BaseModel):
    validation_result: int = Field(alias="ValidationResult")
    address_external_id: str = Field(alias="AddressExternalId")
    address: AddressModel = Field(alias="Address")
    candidate_address_list: List[CandidateAddressModel] = Field(
        alias="CandidateAddressList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChannelMembershipForAppInstanceUserSummaryModel(BaseModel):
    channel_summary: Optional[ChannelSummaryModel] = Field(
        default=None, alias="ChannelSummary"
    )
    app_instance_user_membership_summary: Optional[
        AppInstanceUserMembershipSummaryModel
    ] = Field(default=None, alias="AppInstanceUserMembershipSummary")


class ChannelModeratedByAppInstanceUserSummaryModel(BaseModel):
    channel_summary: Optional[ChannelSummaryModel] = Field(
        default=None, alias="ChannelSummary"
    )


class ListChannelsResponseModel(BaseModel):
    channels: List[ChannelSummaryModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateAppInstanceUserRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_user_id: str = Field(alias="AppInstanceUserId")
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateAttendeeRequestItemModel(BaseModel):
    external_user_id: str = Field(alias="ExternalUserId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    external_user_id: str = Field(alias="ExternalUserId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateChannelRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")


class ListAttendeeTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMeetingTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendee_id: str = Field(alias="AttendeeId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagMeetingRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateMeetingRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    external_meeting_id: Optional[str] = Field(default=None, alias="ExternalMeetingId")
    meeting_host_id: Optional[str] = Field(default=None, alias="MeetingHostId")
    media_region: Optional[str] = Field(default=None, alias="MediaRegion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    notifications_configuration: Optional[
        MeetingNotificationConfigurationModel
    ] = Field(default=None, alias="NotificationsConfiguration")


class CreateProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    participant_phone_numbers: Sequence[str] = Field(alias="ParticipantPhoneNumbers")
    capabilities: Sequence[Literal["SMS", "Voice"]] = Field(alias="Capabilities")
    name: Optional[str] = Field(default=None, alias="Name")
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")
    number_selection_behavior: Optional[Literal["AvoidSticky", "PreferSticky"]] = Field(
        default=None, alias="NumberSelectionBehavior"
    )
    geo_match_level: Optional[Literal["AreaCode", "Country"]] = Field(
        default=None, alias="GeoMatchLevel"
    )
    geo_match_params: Optional[GeoMatchParamsModel] = Field(
        default=None, alias="GeoMatchParams"
    )


class CreateRoomResponseModel(BaseModel):
    room: RoomModel = Field(alias="Room")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoomResponseModel(BaseModel):
    room: RoomModel = Field(alias="Room")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoomsResponseModel(BaseModel):
    rooms: List[RoomModel] = Field(alias="Rooms")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoomResponseModel(BaseModel):
    room: RoomModel = Field(alias="Room")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSipMediaApplicationCallResponseModel(BaseModel):
    sip_media_application_call: SipMediaApplicationCallModel = Field(
        alias="SipMediaApplicationCall"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipMediaApplicationCallResponseModel(BaseModel):
    sip_media_application_call: SipMediaApplicationCallModel = Field(
        alias="SipMediaApplicationCall"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSipMediaApplicationRequestModel(BaseModel):
    aws_region: str = Field(alias="AwsRegion")
    name: str = Field(alias="Name")
    endpoints: Sequence[SipMediaApplicationEndpointModel] = Field(alias="Endpoints")


class SipMediaApplicationModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    name: Optional[str] = Field(default=None, alias="Name")
    endpoints: Optional[List[SipMediaApplicationEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class UpdateSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    name: Optional[str] = Field(default=None, alias="Name")
    endpoints: Optional[Sequence[SipMediaApplicationEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )


class CreateSipRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    trigger_type: Literal["RequestUriHostname", "ToPhoneNumber"] = Field(
        alias="TriggerType"
    )
    trigger_value: str = Field(alias="TriggerValue")
    target_applications: Sequence[SipRuleTargetApplicationModel] = Field(
        alias="TargetApplications"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class SipRuleModel(BaseModel):
    sip_rule_id: Optional[str] = Field(default=None, alias="SipRuleId")
    name: Optional[str] = Field(default=None, alias="Name")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    trigger_type: Optional[Literal["RequestUriHostname", "ToPhoneNumber"]] = Field(
        default=None, alias="TriggerType"
    )
    trigger_value: Optional[str] = Field(default=None, alias="TriggerValue")
    target_applications: Optional[List[SipRuleTargetApplicationModel]] = Field(
        default=None, alias="TargetApplications"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class UpdateSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")
    name: str = Field(alias="Name")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    target_applications: Optional[Sequence[SipRuleTargetApplicationModel]] = Field(
        default=None, alias="TargetApplications"
    )


class CreateVoiceConnectorGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    voice_connector_items: Optional[Sequence[VoiceConnectorItemModel]] = Field(
        default=None, alias="VoiceConnectorItems"
    )


class UpdateVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    name: str = Field(alias="Name")
    voice_connector_items: Sequence[VoiceConnectorItemModel] = Field(
        alias="VoiceConnectorItems"
    )


class VoiceConnectorGroupModel(BaseModel):
    voice_connector_group_id: Optional[str] = Field(
        default=None, alias="VoiceConnectorGroupId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    voice_connector_items: Optional[List[VoiceConnectorItemModel]] = Field(
        default=None, alias="VoiceConnectorItems"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    voice_connector_group_arn: Optional[str] = Field(
        default=None, alias="VoiceConnectorGroupArn"
    )


class CreateVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorsResponseModel(BaseModel):
    voice_connectors: List[VoiceConnectorModel] = Field(alias="VoiceConnectors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    credentials: Optional[Sequence[CredentialModel]] = Field(
        default=None, alias="Credentials"
    )


class EmergencyCallingConfigurationModel(BaseModel):
    dnis: Optional[List[DNISEmergencyCallingConfigurationModel]] = Field(
        default=None, alias="DNIS"
    )


class TranscriptionConfigurationModel(BaseModel):
    engine_transcribe_settings: Optional[EngineTranscribeSettingsModel] = Field(
        default=None, alias="EngineTranscribeSettings"
    )
    engine_transcribe_medical_settings: Optional[
        EngineTranscribeMedicalSettingsModel
    ] = Field(default=None, alias="EngineTranscribeMedicalSettings")


class GetEventsConfigurationResponseModel(BaseModel):
    events_configuration: EventsConfigurationModel = Field(alias="EventsConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEventsConfigurationResponseModel(BaseModel):
    events_configuration: EventsConfigurationModel = Field(alias="EventsConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGlobalSettingsResponseModel(BaseModel):
    business_calling: BusinessCallingSettingsModel = Field(alias="BusinessCalling")
    voice_connector: VoiceConnectorSettingsModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGlobalSettingsRequestModel(BaseModel):
    business_calling: Optional[BusinessCallingSettingsModel] = Field(
        default=None, alias="BusinessCalling"
    )
    voice_connector: Optional[VoiceConnectorSettingsModel] = Field(
        default=None, alias="VoiceConnector"
    )


class GetMessagingSessionEndpointResponseModel(BaseModel):
    endpoint: MessagingSessionEndpointModel = Field(alias="Endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipMediaApplicationLoggingConfigurationResponseModel(BaseModel):
    sip_media_application_logging_configuration: SipMediaApplicationLoggingConfigurationModel = Field(
        alias="SipMediaApplicationLoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSipMediaApplicationLoggingConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    sip_media_application_logging_configuration: Optional[
        SipMediaApplicationLoggingConfigurationModel
    ] = Field(default=None, alias="SipMediaApplicationLoggingConfiguration")


class PutSipMediaApplicationLoggingConfigurationResponseModel(BaseModel):
    sip_media_application_logging_configuration: SipMediaApplicationLoggingConfigurationModel = Field(
        alias="SipMediaApplicationLoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorLoggingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )


class PutVoiceConnectorLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorProxyResponseModel(BaseModel):
    proxy: ProxyModel = Field(alias="Proxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorProxyResponseModel(BaseModel):
    proxy: ProxyModel = Field(alias="Proxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorTerminationHealthResponseModel(BaseModel):
    termination_health: TerminationHealthModel = Field(alias="TerminationHealth")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorTerminationResponseModel(BaseModel):
    termination: TerminationModel = Field(alias="Termination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    termination: TerminationModel = Field(alias="Termination")


class PutVoiceConnectorTerminationResponseModel(BaseModel):
    termination: TerminationModel = Field(alias="Termination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InviteUsersResponseModel(BaseModel):
    invites: List[InviteModel] = Field(alias="Invites")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsRequestListAccountsPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    user_email: Optional[str] = Field(default=None, alias="UserEmail")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_email: Optional[str] = Field(default=None, alias="UserEmail")
    user_type: Optional[Literal["PrivateUser", "SharedDevice"]] = Field(
        default=None, alias="UserType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSupportedPhoneNumberCountriesResponseModel(BaseModel):
    phone_number_countries: List[PhoneNumberCountryModel] = Field(
        alias="PhoneNumberCountries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MeetingModel(BaseModel):
    meeting_id: Optional[str] = Field(default=None, alias="MeetingId")
    external_meeting_id: Optional[str] = Field(default=None, alias="ExternalMeetingId")
    media_placement: Optional[MediaPlacementModel] = Field(
        default=None, alias="MediaPlacement"
    )
    media_region: Optional[str] = Field(default=None, alias="MediaRegion")


class RoomMembershipModel(BaseModel):
    room_id: Optional[str] = Field(default=None, alias="RoomId")
    member: Optional[MemberModel] = Field(default=None, alias="Member")
    role: Optional[Literal["Administrator", "Member"]] = Field(
        default=None, alias="Role"
    )
    invited_by: Optional[str] = Field(default=None, alias="InvitedBy")
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class PhoneNumberOrderModel(BaseModel):
    phone_number_order_id: Optional[str] = Field(
        default=None, alias="PhoneNumberOrderId"
    )
    product_type: Optional[
        Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    status: Optional[Literal["Failed", "Partial", "Processing", "Successful"]] = Field(
        default=None, alias="Status"
    )
    ordered_phone_numbers: Optional[List[OrderedPhoneNumberModel]] = Field(
        default=None, alias="OrderedPhoneNumbers"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class OriginationModel(BaseModel):
    routes: Optional[List[OriginationRouteModel]] = Field(default=None, alias="Routes")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class ProxySessionModel(BaseModel):
    voice_connector_id: Optional[str] = Field(default=None, alias="VoiceConnectorId")
    proxy_session_id: Optional[str] = Field(default=None, alias="ProxySessionId")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["Closed", "InProgress", "Open"]] = Field(
        default=None, alias="Status"
    )
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")
    capabilities: Optional[List[Literal["SMS", "Voice"]]] = Field(
        default=None, alias="Capabilities"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    ended_timestamp: Optional[datetime] = Field(default=None, alias="EndedTimestamp")
    participants: Optional[List[ParticipantModel]] = Field(
        default=None, alias="Participants"
    )
    number_selection_behavior: Optional[Literal["AvoidSticky", "PreferSticky"]] = Field(
        default=None, alias="NumberSelectionBehavior"
    )
    geo_match_level: Optional[Literal["AreaCode", "Country"]] = Field(
        default=None, alias="GeoMatchLevel"
    )
    geo_match_params: Optional[GeoMatchParamsModel] = Field(
        default=None, alias="GeoMatchParams"
    )


class PhoneNumberModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    e164_phone_number: Optional[str] = Field(default=None, alias="E164PhoneNumber")
    country: Optional[str] = Field(default=None, alias="Country")
    type: Optional[Literal["Local", "TollFree"]] = Field(default=None, alias="Type")
    product_type: Optional[
        Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    status: Optional[
        Literal[
            "AcquireFailed",
            "AcquireInProgress",
            "Assigned",
            "DeleteFailed",
            "DeleteInProgress",
            "ReleaseFailed",
            "ReleaseInProgress",
            "Unassigned",
        ]
    ] = Field(default=None, alias="Status")
    capabilities: Optional[PhoneNumberCapabilitiesModel] = Field(
        default=None, alias="Capabilities"
    )
    associations: Optional[List[PhoneNumberAssociationModel]] = Field(
        default=None, alias="Associations"
    )
    calling_name: Optional[str] = Field(default=None, alias="CallingName")
    calling_name_status: Optional[
        Literal["Unassigned", "UpdateFailed", "UpdateInProgress", "UpdateSucceeded"]
    ] = Field(default=None, alias="CallingNameStatus")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    deletion_timestamp: Optional[datetime] = Field(
        default=None, alias="DeletionTimestamp"
    )


class RetentionSettingsModel(BaseModel):
    room_retention_settings: Optional[RoomRetentionSettingsModel] = Field(
        default=None, alias="RoomRetentionSettings"
    )
    conversation_retention_settings: Optional[
        ConversationRetentionSettingsModel
    ] = Field(default=None, alias="ConversationRetentionSettings")


class SourceConfigurationModel(BaseModel):
    selected_video_streams: Optional[SelectedVideoStreamsModel] = Field(
        default=None, alias="SelectedVideoStreams"
    )


class StreamingConfigurationModel(BaseModel):
    data_retention_in_hours: int = Field(alias="DataRetentionInHours")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    streaming_notification_targets: Optional[
        List[StreamingNotificationTargetModel]
    ] = Field(default=None, alias="StreamingNotificationTargets")


class UserSettingsModel(BaseModel):
    telephony: TelephonySettingsModel = Field(alias="Telephony")


class CreateAccountResponseModel(BaseModel):
    account: AccountModel = Field(alias="Account")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountResponseModel(BaseModel):
    account: AccountModel = Field(alias="Account")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="Accounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountResponseModel(BaseModel):
    account: AccountModel = Field(alias="Account")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateUserRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    update_user_request_items: Sequence[UpdateUserRequestItemModel] = Field(
        alias="UpdateUserRequestItems"
    )


class CreateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetPersonalPINResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstanceAdminsResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_admins: List[AppInstanceAdminSummaryModel] = Field(
        alias="AppInstanceAdmins"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceAdminResponseModel(BaseModel):
    app_instance_admin: AppInstanceAdminModel = Field(alias="AppInstanceAdmin")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateChannelMembershipResponseModel(BaseModel):
    batch_channel_memberships: BatchChannelMembershipsModel = Field(
        alias="BatchChannelMemberships"
    )
    errors: List[BatchCreateChannelMembershipErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelBansResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    next_token: str = Field(alias="NextToken")
    channel_bans: List[ChannelBanSummaryModel] = Field(alias="ChannelBans")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelBanResponseModel(BaseModel):
    channel_ban: ChannelBanModel = Field(alias="ChannelBan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelMembershipsResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_memberships: List[ChannelMembershipSummaryModel] = Field(
        alias="ChannelMemberships"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelMembershipResponseModel(BaseModel):
    channel_membership: ChannelMembershipModel = Field(alias="ChannelMembership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelMessagesResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    next_token: str = Field(alias="NextToken")
    channel_messages: List[ChannelMessageSummaryModel] = Field(alias="ChannelMessages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelMessageResponseModel(BaseModel):
    channel_message: ChannelMessageModel = Field(alias="ChannelMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelModeratorsResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    next_token: str = Field(alias="NextToken")
    channel_moderators: List[ChannelModeratorSummaryModel] = Field(
        alias="ChannelModerators"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelModeratorResponseModel(BaseModel):
    channel_moderator: ChannelModeratorModel = Field(alias="ChannelModerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppInstanceRetentionSettingsResponseModel(BaseModel):
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppInstanceRetentionSettingsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )


class PutAppInstanceRetentionSettingsResponseModel(BaseModel):
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelMembershipForAppInstanceUserResponseModel(BaseModel):
    channel_membership: ChannelMembershipForAppInstanceUserSummaryModel = Field(
        alias="ChannelMembership"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelMembershipsForAppInstanceUserResponseModel(BaseModel):
    channel_memberships: List[ChannelMembershipForAppInstanceUserSummaryModel] = Field(
        alias="ChannelMemberships"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelModeratedByAppInstanceUserResponseModel(BaseModel):
    channel: ChannelModeratedByAppInstanceUserSummaryModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsModeratedByAppInstanceUserResponseModel(BaseModel):
    channels: List[ChannelModeratedByAppInstanceUserSummaryModel] = Field(
        alias="Channels"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateAttendeeRequestModel(BaseModel):
    meeting_id: str = Field(alias="MeetingId")
    attendees: Sequence[CreateAttendeeRequestItemModel] = Field(alias="Attendees")


class CreateMeetingWithAttendeesRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    external_meeting_id: Optional[str] = Field(default=None, alias="ExternalMeetingId")
    meeting_host_id: Optional[str] = Field(default=None, alias="MeetingHostId")
    media_region: Optional[str] = Field(default=None, alias="MediaRegion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    notifications_configuration: Optional[
        MeetingNotificationConfigurationModel
    ] = Field(default=None, alias="NotificationsConfiguration")
    attendees: Optional[Sequence[CreateAttendeeRequestItemModel]] = Field(
        default=None, alias="Attendees"
    )


class CreateSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSipMediaApplicationsResponseModel(BaseModel):
    sip_media_applications: List[SipMediaApplicationModel] = Field(
        alias="SipMediaApplications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSipRulesResponseModel(BaseModel):
    sip_rules: List[SipRuleModel] = Field(alias="SipRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorGroupsResponseModel(BaseModel):
    voice_connector_groups: List[VoiceConnectorGroupModel] = Field(
        alias="VoiceConnectorGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorEmergencyCallingConfigurationResponseModel(BaseModel):
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )


class PutVoiceConnectorEmergencyCallingConfigurationResponseModel(BaseModel):
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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


class ListMeetingsResponseModel(BaseModel):
    meetings: List[MeetingModel] = Field(alias="Meetings")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoomMembershipResponseModel(BaseModel):
    room_membership: RoomMembershipModel = Field(alias="RoomMembership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoomMembershipsResponseModel(BaseModel):
    room_memberships: List[RoomMembershipModel] = Field(alias="RoomMemberships")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoomMembershipResponseModel(BaseModel):
    room_membership: RoomMembershipModel = Field(alias="RoomMembership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePhoneNumberOrderResponseModel(BaseModel):
    phone_number_order: PhoneNumberOrderModel = Field(alias="PhoneNumberOrder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberOrderResponseModel(BaseModel):
    phone_number_order: PhoneNumberOrderModel = Field(alias="PhoneNumberOrder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumberOrdersResponseModel(BaseModel):
    phone_number_orders: List[PhoneNumberOrderModel] = Field(alias="PhoneNumberOrders")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorOriginationResponseModel(BaseModel):
    origination: OriginationModel = Field(alias="Origination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    origination: OriginationModel = Field(alias="Origination")


class PutVoiceConnectorOriginationResponseModel(BaseModel):
    origination: OriginationModel = Field(alias="Origination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProxySessionsResponseModel(BaseModel):
    proxy_sessions: List[ProxySessionModel] = Field(alias="ProxySessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumbersResponseModel(BaseModel):
    phone_numbers: List[PhoneNumberModel] = Field(alias="PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestorePhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRetentionSettingsResponseModel(BaseModel):
    retention_settings: RetentionSettingsModel = Field(alias="RetentionSettings")
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRetentionSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    retention_settings: RetentionSettingsModel = Field(alias="RetentionSettings")


class PutRetentionSettingsResponseModel(BaseModel):
    retention_settings: RetentionSettingsModel = Field(alias="RetentionSettings")
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChimeSdkMeetingConfigurationModel(BaseModel):
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="SourceConfiguration"
    )
    artifacts_configuration: Optional[ArtifactsConfigurationModel] = Field(
        default=None, alias="ArtifactsConfiguration"
    )


class GetVoiceConnectorStreamingConfigurationResponseModel(BaseModel):
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )


class PutVoiceConnectorStreamingConfigurationResponseModel(BaseModel):
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserSettingsResponseModel(BaseModel):
    user_settings: UserSettingsModel = Field(alias="UserSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserSettingsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    user_id: str = Field(alias="UserId")
    user_settings: UserSettingsModel = Field(alias="UserSettings")


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


class MediaCapturePipelineModel(BaseModel):
    media_pipeline_id: Optional[str] = Field(default=None, alias="MediaPipelineId")
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


class ListMediaCapturePipelinesResponseModel(BaseModel):
    media_capture_pipelines: List[MediaCapturePipelineModel] = Field(
        alias="MediaCapturePipelines"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
