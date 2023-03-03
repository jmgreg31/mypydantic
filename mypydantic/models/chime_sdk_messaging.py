# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AppInstanceUserMembershipSummaryModel(BaseModel):
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    read_marker_timestamp: Optional[datetime] = Field(
        default=None, alias="ReadMarkerTimestamp"
    )
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class AssociateChannelFlowRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class IdentityModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


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
    chime_bearer: str = Field(alias="ChimeBearer")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ChannelAssociatedWithFlowSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")


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


class PushNotificationPreferencesModel(BaseModel):
    allow_notifications: Literal["ALL", "FILTERED", "NONE"] = Field(
        alias="AllowNotifications"
    )
    filter_rule: Optional[str] = Field(default=None, alias="FilterRule")


class MessageAttributeValueModel(BaseModel):
    string_values: Optional[Sequence[str]] = Field(default=None, alias="StringValues")


class PushNotificationConfigurationModel(BaseModel):
    title: Optional[str] = Field(default=None, alias="Title")
    body: Optional[str] = Field(default=None, alias="Body")
    type: Optional[Literal["DEFAULT", "VOIP"]] = Field(default=None, alias="Type")


class ChannelMessageStatusStructureModel(BaseModel):
    value: Optional[Literal["DENIED", "FAILED", "PENDING", "SENT"]] = Field(
        default=None, alias="Value"
    )
    detail: Optional[str] = Field(default=None, alias="Detail")


class ElasticChannelConfigurationModel(BaseModel):
    maximum_sub_channels: int = Field(alias="MaximumSubChannels")
    target_memberships_per_sub_channel: int = Field(
        alias="TargetMembershipsPerSubChannel"
    )
    minimum_membership_percentage: int = Field(alias="MinimumMembershipPercentage")


class CreateChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    type: Literal["DEFAULT", "HIDDEN"] = Field(alias="Type")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class CreateChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DeleteChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DeleteChannelFlowRequestModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")


class DeleteChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class DeleteChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class DeleteChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DeleteChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class DescribeChannelBanRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DescribeChannelFlowRequestModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")


class DescribeChannelMembershipForAppInstanceUserRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DescribeChannelMembershipRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class DescribeChannelModeratedByAppInstanceUserRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DescribeChannelModeratorRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator_arn: str = Field(alias="ChannelModeratorArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DescribeChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class DisassociateChannelFlowRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class GetChannelMembershipPreferencesRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")


class GetChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class GetChannelMessageStatusRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class MessagingSessionEndpointModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")


class LambdaConfigurationModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    invocation_type: Literal["ASYNC"] = Field(alias="InvocationType")


class ListChannelBansRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelFlowsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelMembershipsForAppInstanceUserRequestModel(BaseModel):
    chime_bearer: str = Field(alias="ChimeBearer")
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelMembershipsRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class ListChannelMessagesRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    not_before: Optional[Union[datetime, str]] = Field(default=None, alias="NotBefore")
    not_after: Optional[Union[datetime, str]] = Field(default=None, alias="NotAfter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class ListChannelModeratorsRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelsAssociatedWithChannelFlowRequestModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelsModeratedByAppInstanceUserRequestModel(BaseModel):
    chime_bearer: str = Field(alias="ChimeBearer")
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListChannelsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSubChannelsRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SubChannelSummaryModel(BaseModel):
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")
    membership_count: Optional[int] = Field(default=None, alias="MembershipCount")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class RedactChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class SearchFieldModel(BaseModel):
    key: Literal["MEMBERS"] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal["EQUALS", "INCLUDES"] = Field(alias="Operator")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    chime_bearer: str = Field(alias="ChimeBearer")
    content: Optional[str] = Field(default=None, alias="Content")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class UpdateChannelReadMarkerRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class UpdateChannelRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    name: Optional[str] = Field(default=None, alias="Name")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class BatchChannelMembershipsModel(BaseModel):
    invited_by: Optional[IdentityModel] = Field(default=None, alias="InvitedBy")
    type: Optional[Literal["DEFAULT", "HIDDEN"]] = Field(default=None, alias="Type")
    members: Optional[List[IdentityModel]] = Field(default=None, alias="Members")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


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
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class ChannelModeratorSummaryModel(BaseModel):
    moderator: Optional[IdentityModel] = Field(default=None, alias="Moderator")


class ChannelModeratorModel(BaseModel):
    moderator: Optional[IdentityModel] = Field(default=None, alias="Moderator")
    channel_arn: Optional[str] = Field(default=None, alias="ChannelArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    created_by: Optional[IdentityModel] = Field(default=None, alias="CreatedBy")


class ChannelFlowCallbackResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    callback_id: str = Field(alias="CallbackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelBanResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelFlowResponseModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelMembershipResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelModeratorResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    channel_moderator: IdentityModel = Field(alias="ChannelModerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RedactChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelFlowResponseModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelReadMarkerResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChannelsAssociatedWithChannelFlowResponseModel(BaseModel):
    channels: List[ChannelAssociatedWithFlowSummaryModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
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


class SearchChannelsResponseModel(BaseModel):
    channels: List[ChannelSummaryModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChannelMembershipPreferencesModel(BaseModel):
    push_notifications: Optional[PushNotificationPreferencesModel] = Field(
        default=None, alias="PushNotifications"
    )


class ChannelMessageCallbackModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    content: Optional[str] = Field(default=None, alias="Content")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    push_notification: Optional[PushNotificationConfigurationModel] = Field(
        default=None, alias="PushNotification"
    )
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class SendChannelMessageRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    content: str = Field(alias="Content")
    type: Literal["CONTROL", "STANDARD"] = Field(alias="Type")
    persistence: Literal["NON_PERSISTENT", "PERSISTENT"] = Field(alias="Persistence")
    client_request_token: str = Field(alias="ClientRequestToken")
    chime_bearer: str = Field(alias="ChimeBearer")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    push_notification: Optional[PushNotificationConfigurationModel] = Field(
        default=None, alias="PushNotification"
    )
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


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
    status: Optional[ChannelMessageStatusStructureModel] = Field(
        default=None, alias="Status"
    )
    message_attributes: Optional[Dict[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )


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
    status: Optional[ChannelMessageStatusStructureModel] = Field(
        default=None, alias="Status"
    )
    message_attributes: Optional[Dict[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    sub_channel_id: Optional[str] = Field(default=None, alias="SubChannelId")


class GetChannelMessageStatusResponseModel(BaseModel):
    status: ChannelMessageStatusStructureModel = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    status: ChannelMessageStatusStructureModel = Field(alias="Status")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChannelMessageResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    message_id: str = Field(alias="MessageId")
    status: ChannelMessageStatusStructureModel = Field(alias="Status")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
    channel_flow_arn: Optional[str] = Field(default=None, alias="ChannelFlowArn")
    elastic_channel_configuration: Optional[ElasticChannelConfigurationModel] = Field(
        default=None, alias="ElasticChannelConfiguration"
    )


class CreateChannelRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    chime_bearer: str = Field(alias="ChimeBearer")
    mode: Optional[Literal["RESTRICTED", "UNRESTRICTED"]] = Field(
        default=None, alias="Mode"
    )
    privacy: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Privacy"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    channel_id: Optional[str] = Field(default=None, alias="ChannelId")
    member_arns: Optional[Sequence[str]] = Field(default=None, alias="MemberArns")
    moderator_arns: Optional[Sequence[str]] = Field(default=None, alias="ModeratorArns")
    elastic_channel_configuration: Optional[ElasticChannelConfigurationModel] = Field(
        default=None, alias="ElasticChannelConfiguration"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class GetMessagingSessionEndpointResponseModel(BaseModel):
    endpoint: MessagingSessionEndpointModel = Field(alias="Endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProcessorConfigurationModel(BaseModel):
    lambda_: LambdaConfigurationModel = Field(alias="Lambda")


class ListSubChannelsResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    sub_channels: List[SubChannelSummaryModel] = Field(alias="SubChannels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchChannelsRequestModel(BaseModel):
    fields: Sequence[SearchFieldModel] = Field(alias="Fields")
    chime_bearer: Optional[str] = Field(default=None, alias="ChimeBearer")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


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


class GetChannelMembershipPreferencesResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    preferences: ChannelMembershipPreferencesModel = Field(alias="Preferences")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutChannelMembershipPreferencesRequestModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member_arn: str = Field(alias="MemberArn")
    chime_bearer: str = Field(alias="ChimeBearer")
    preferences: ChannelMembershipPreferencesModel = Field(alias="Preferences")


class PutChannelMembershipPreferencesResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    member: IdentityModel = Field(alias="Member")
    preferences: ChannelMembershipPreferencesModel = Field(alias="Preferences")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChannelFlowCallbackRequestModel(BaseModel):
    callback_id: str = Field(alias="CallbackId")
    channel_arn: str = Field(alias="ChannelArn")
    channel_message: ChannelMessageCallbackModel = Field(alias="ChannelMessage")
    delete_resource: Optional[bool] = Field(default=None, alias="DeleteResource")


class ListChannelMessagesResponseModel(BaseModel):
    channel_arn: str = Field(alias="ChannelArn")
    next_token: str = Field(alias="NextToken")
    channel_messages: List[ChannelMessageSummaryModel] = Field(alias="ChannelMessages")
    sub_channel_id: str = Field(alias="SubChannelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChannelMessageResponseModel(BaseModel):
    channel_message: ChannelMessageModel = Field(alias="ChannelMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelResponseModel(BaseModel):
    channel: ChannelModel = Field(alias="Channel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProcessorModel(BaseModel):
    name: str = Field(alias="Name")
    configuration: ProcessorConfigurationModel = Field(alias="Configuration")
    execution_order: int = Field(alias="ExecutionOrder")
    fallback_action: Literal["ABORT", "CONTINUE"] = Field(alias="FallbackAction")


class ChannelFlowSummaryModel(BaseModel):
    channel_flow_arn: Optional[str] = Field(default=None, alias="ChannelFlowArn")
    name: Optional[str] = Field(default=None, alias="Name")
    processors: Optional[List[ProcessorModel]] = Field(default=None, alias="Processors")


class ChannelFlowModel(BaseModel):
    channel_flow_arn: Optional[str] = Field(default=None, alias="ChannelFlowArn")
    processors: Optional[List[ProcessorModel]] = Field(default=None, alias="Processors")
    name: Optional[str] = Field(default=None, alias="Name")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class CreateChannelFlowRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    processors: Sequence[ProcessorModel] = Field(alias="Processors")
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateChannelFlowRequestModel(BaseModel):
    channel_flow_arn: str = Field(alias="ChannelFlowArn")
    processors: Sequence[ProcessorModel] = Field(alias="Processors")
    name: str = Field(alias="Name")


class ListChannelFlowsResponseModel(BaseModel):
    channel_flows: List[ChannelFlowSummaryModel] = Field(alias="ChannelFlows")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChannelFlowResponseModel(BaseModel):
    channel_flow: ChannelFlowModel = Field(alias="ChannelFlow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
