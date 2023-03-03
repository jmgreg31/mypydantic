# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ADMChannelRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    client_secret: str = Field(alias="ClientSecret")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ADMChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class ADMMessageModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    consolidation_key: Optional[str] = Field(default=None, alias="ConsolidationKey")
    data: Optional[Mapping[str, str]] = Field(default=None, alias="Data")
    expires_after: Optional[str] = Field(default=None, alias="ExpiresAfter")
    icon_reference: Optional[str] = Field(default=None, alias="IconReference")
    image_icon_url: Optional[str] = Field(default=None, alias="ImageIconUrl")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    md5: Optional[str] = Field(default=None, alias="MD5")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    small_image_icon_url: Optional[str] = Field(default=None, alias="SmallImageIconUrl")
    sound: Optional[str] = Field(default=None, alias="Sound")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class APNSChannelRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    team_id: Optional[str] = Field(default=None, alias="TeamId")
    token_key: Optional[str] = Field(default=None, alias="TokenKey")
    token_key_id: Optional[str] = Field(default=None, alias="TokenKeyId")


class APNSChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    has_token_key: Optional[bool] = Field(default=None, alias="HasTokenKey")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class APNSMessageModel(BaseModel):
    ap_ns_push_type: Optional[str] = Field(default=None, alias="APNSPushType")
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    badge: Optional[int] = Field(default=None, alias="Badge")
    body: Optional[str] = Field(default=None, alias="Body")
    category: Optional[str] = Field(default=None, alias="Category")
    collapse_id: Optional[str] = Field(default=None, alias="CollapseId")
    data: Optional[Mapping[str, str]] = Field(default=None, alias="Data")
    media_url: Optional[str] = Field(default=None, alias="MediaUrl")
    preferred_authentication_method: Optional[str] = Field(
        default=None, alias="PreferredAuthenticationMethod"
    )
    priority: Optional[str] = Field(default=None, alias="Priority")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    sound: Optional[str] = Field(default=None, alias="Sound")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    thread_id: Optional[str] = Field(default=None, alias="ThreadId")
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class APNSPushNotificationTemplateModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    media_url: Optional[str] = Field(default=None, alias="MediaUrl")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    sound: Optional[str] = Field(default=None, alias="Sound")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class APNSSandboxChannelRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    team_id: Optional[str] = Field(default=None, alias="TeamId")
    token_key: Optional[str] = Field(default=None, alias="TokenKey")
    token_key_id: Optional[str] = Field(default=None, alias="TokenKeyId")


class APNSSandboxChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    has_token_key: Optional[bool] = Field(default=None, alias="HasTokenKey")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class APNSVoipChannelRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    team_id: Optional[str] = Field(default=None, alias="TeamId")
    token_key: Optional[str] = Field(default=None, alias="TokenKey")
    token_key_id: Optional[str] = Field(default=None, alias="TokenKeyId")


class APNSVoipChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    has_token_key: Optional[bool] = Field(default=None, alias="HasTokenKey")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class APNSVoipSandboxChannelRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    team_id: Optional[str] = Field(default=None, alias="TeamId")
    token_key: Optional[str] = Field(default=None, alias="TokenKey")
    token_key_id: Optional[str] = Field(default=None, alias="TokenKeyId")


class APNSVoipSandboxChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    default_authentication_method: Optional[str] = Field(
        default=None, alias="DefaultAuthenticationMethod"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    has_token_key: Optional[bool] = Field(default=None, alias="HasTokenKey")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class ActivityResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    id: str = Field(alias="Id")
    end: Optional[str] = Field(default=None, alias="End")
    result: Optional[str] = Field(default=None, alias="Result")
    scheduled_start: Optional[str] = Field(default=None, alias="ScheduledStart")
    start: Optional[str] = Field(default=None, alias="Start")
    state: Optional[str] = Field(default=None, alias="State")
    successful_endpoint_count: Optional[int] = Field(
        default=None, alias="SuccessfulEndpointCount"
    )
    timezones_completed_count: Optional[int] = Field(
        default=None, alias="TimezonesCompletedCount"
    )
    timezones_total_count: Optional[int] = Field(
        default=None, alias="TimezonesTotalCount"
    )
    total_endpoint_count: Optional[int] = Field(
        default=None, alias="TotalEndpointCount"
    )
    treatment_id: Optional[str] = Field(default=None, alias="TreatmentId")


class ContactCenterActivityModel(BaseModel):
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")


class HoldoutActivityModel(BaseModel):
    percentage: int = Field(alias="Percentage")
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")


class AddressConfigurationModel(BaseModel):
    body_override: Optional[str] = Field(default=None, alias="BodyOverride")
    channel_type: Optional[
        Literal[
            "ADM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "BAIDU",
            "CUSTOM",
            "EMAIL",
            "GCM",
            "IN_APP",
            "PUSH",
            "SMS",
            "VOICE",
        ]
    ] = Field(default=None, alias="ChannelType")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    title_override: Optional[str] = Field(default=None, alias="TitleOverride")


class AndroidPushNotificationTemplateModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    image_icon_url: Optional[str] = Field(default=None, alias="ImageIconUrl")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    small_image_icon_url: Optional[str] = Field(default=None, alias="SmallImageIconUrl")
    sound: Optional[str] = Field(default=None, alias="Sound")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class ApplicationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")


class CampaignHookModel(BaseModel):
    lambda_function_name: Optional[str] = Field(
        default=None, alias="LambdaFunctionName"
    )
    mode: Optional[Literal["DELIVERY", "FILTER"]] = Field(default=None, alias="Mode")
    web_url: Optional[str] = Field(default=None, alias="WebUrl")


class CampaignLimitsModel(BaseModel):
    daily: Optional[int] = Field(default=None, alias="Daily")
    maximum_duration: Optional[int] = Field(default=None, alias="MaximumDuration")
    messages_per_second: Optional[int] = Field(default=None, alias="MessagesPerSecond")
    total: Optional[int] = Field(default=None, alias="Total")
    session: Optional[int] = Field(default=None, alias="Session")


class QuietTimeModel(BaseModel):
    end: Optional[str] = Field(default=None, alias="End")
    start: Optional[str] = Field(default=None, alias="Start")


class AttributeDimensionModel(BaseModel):
    values: Sequence[str] = Field(alias="Values")
    attribute_type: Optional[
        Literal[
            "AFTER", "BEFORE", "BETWEEN", "CONTAINS", "EXCLUSIVE", "INCLUSIVE", "ON"
        ]
    ] = Field(default=None, alias="AttributeType")


class AttributesResourceModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    attribute_type: str = Field(alias="AttributeType")
    attributes: Optional[List[str]] = Field(default=None, alias="Attributes")


class BaiduChannelRequestModel(BaseModel):
    api_key: str = Field(alias="ApiKey")
    secret_key: str = Field(alias="SecretKey")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class BaiduChannelResponseModel(BaseModel):
    credential: str = Field(alias="Credential")
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class BaiduMessageModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    data: Optional[Mapping[str, str]] = Field(default=None, alias="Data")
    icon_reference: Optional[str] = Field(default=None, alias="IconReference")
    image_icon_url: Optional[str] = Field(default=None, alias="ImageIconUrl")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    small_image_icon_url: Optional[str] = Field(default=None, alias="SmallImageIconUrl")
    sound: Optional[str] = Field(default=None, alias="Sound")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class CampaignCustomMessageModel(BaseModel):
    data: Optional[str] = Field(default=None, alias="Data")


class CampaignEmailMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    from_address: Optional[str] = Field(default=None, alias="FromAddress")
    html_body: Optional[str] = Field(default=None, alias="HtmlBody")
    title: Optional[str] = Field(default=None, alias="Title")


class CampaignStateModel(BaseModel):
    campaign_status: Optional[
        Literal[
            "COMPLETED",
            "DELETED",
            "EXECUTING",
            "INVALID",
            "PAUSED",
            "PENDING_NEXT_RUN",
            "SCHEDULED",
        ]
    ] = Field(default=None, alias="CampaignStatus")


class CustomDeliveryConfigurationModel(BaseModel):
    delivery_uri: str = Field(alias="DeliveryUri")
    endpoint_types: Optional[
        Sequence[
            Literal[
                "ADM",
                "APNS",
                "APNS_SANDBOX",
                "APNS_VOIP",
                "APNS_VOIP_SANDBOX",
                "BAIDU",
                "CUSTOM",
                "EMAIL",
                "GCM",
                "IN_APP",
                "PUSH",
                "SMS",
                "VOICE",
            ]
        ]
    ] = Field(default=None, alias="EndpointTypes")


class CampaignSmsMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    message_type: Optional[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        default=None, alias="MessageType"
    )
    origination_number: Optional[str] = Field(default=None, alias="OriginationNumber")
    sender_id: Optional[str] = Field(default=None, alias="SenderId")
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")


class ChannelResponseModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class ClosedDaysRuleModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    start_date_time: Optional[str] = Field(default=None, alias="StartDateTime")
    end_date_time: Optional[str] = Field(default=None, alias="EndDateTime")


class WaitTimeModel(BaseModel):
    wait_for: Optional[str] = Field(default=None, alias="WaitFor")
    wait_until: Optional[str] = Field(default=None, alias="WaitUntil")


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EmailTemplateRequestModel(BaseModel):
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    html_part: Optional[str] = Field(default=None, alias="HtmlPart")
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    subject: Optional[str] = Field(default=None, alias="Subject")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    text_part: Optional[str] = Field(default=None, alias="TextPart")


class CreateTemplateMessageBodyModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    message: Optional[str] = Field(default=None, alias="Message")
    request_id: Optional[str] = Field(default=None, alias="RequestID")


class ExportJobRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    s3_url_prefix: str = Field(alias="S3UrlPrefix")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")
    segment_version: Optional[int] = Field(default=None, alias="SegmentVersion")


class ImportJobRequestModel(BaseModel):
    format: Literal["CSV", "JSON"] = Field(alias="Format")
    role_arn: str = Field(alias="RoleArn")
    s3_url: str = Field(alias="S3Url")
    define_segment: Optional[bool] = Field(default=None, alias="DefineSegment")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    register_endpoints: Optional[bool] = Field(default=None, alias="RegisterEndpoints")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")


class TemplateCreateMessageBodyModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    message: Optional[str] = Field(default=None, alias="Message")
    request_id: Optional[str] = Field(default=None, alias="RequestID")


class CreateRecommenderConfigurationModel(BaseModel):
    recommendation_provider_role_arn: str = Field(alias="RecommendationProviderRoleArn")
    recommendation_provider_uri: str = Field(alias="RecommendationProviderUri")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    recommendation_provider_id_type: Optional[str] = Field(
        default=None, alias="RecommendationProviderIdType"
    )
    recommendation_transformer_uri: Optional[str] = Field(
        default=None, alias="RecommendationTransformerUri"
    )
    recommendations_display_name: Optional[str] = Field(
        default=None, alias="RecommendationsDisplayName"
    )
    recommendations_per_message: Optional[int] = Field(
        default=None, alias="RecommendationsPerMessage"
    )


class RecommenderConfigurationResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    id: str = Field(alias="Id")
    last_modified_date: str = Field(alias="LastModifiedDate")
    recommendation_provider_role_arn: str = Field(alias="RecommendationProviderRoleArn")
    recommendation_provider_uri: str = Field(alias="RecommendationProviderUri")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    recommendation_provider_id_type: Optional[str] = Field(
        default=None, alias="RecommendationProviderIdType"
    )
    recommendation_transformer_uri: Optional[str] = Field(
        default=None, alias="RecommendationTransformerUri"
    )
    recommendations_display_name: Optional[str] = Field(
        default=None, alias="RecommendationsDisplayName"
    )
    recommendations_per_message: Optional[int] = Field(
        default=None, alias="RecommendationsPerMessage"
    )


class SMSTemplateRequestModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )


class VoiceTemplateRequestModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    voice_id: Optional[str] = Field(default=None, alias="VoiceId")


class JourneyCustomMessageModel(BaseModel):
    data: Optional[str] = Field(default=None, alias="Data")


class DefaultButtonConfigurationModel(BaseModel):
    button_action: Literal["CLOSE", "DEEP_LINK", "LINK"] = Field(alias="ButtonAction")
    text: str = Field(alias="Text")
    background_color: Optional[str] = Field(default=None, alias="BackgroundColor")
    border_radius: Optional[int] = Field(default=None, alias="BorderRadius")
    link: Optional[str] = Field(default=None, alias="Link")
    text_color: Optional[str] = Field(default=None, alias="TextColor")


class DefaultMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )


class DefaultPushNotificationMessageModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    data: Optional[Mapping[str, str]] = Field(default=None, alias="Data")
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class DefaultPushNotificationTemplateModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    sound: Optional[str] = Field(default=None, alias="Sound")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class DeleteAdmChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteApnsChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteApnsSandboxChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteApnsVoipChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteApnsVoipSandboxChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteAppRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteBaiduChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteCampaignRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")


class DeleteEmailChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class EmailChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    configuration_set: Optional[str] = Field(default=None, alias="ConfigurationSet")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    from_address: Optional[str] = Field(default=None, alias="FromAddress")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    identity: Optional[str] = Field(default=None, alias="Identity")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    messages_per_second: Optional[int] = Field(default=None, alias="MessagesPerSecond")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    version: Optional[int] = Field(default=None, alias="Version")


class DeleteEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class MessageBodyModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    request_id: Optional[str] = Field(default=None, alias="RequestID")


class DeleteEndpointRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_id: str = Field(alias="EndpointId")


class DeleteEventStreamRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class EventStreamModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    destination_stream_arn: str = Field(alias="DestinationStreamArn")
    role_arn: str = Field(alias="RoleArn")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    last_updated_by: Optional[str] = Field(default=None, alias="LastUpdatedBy")


class DeleteGcmChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GCMChannelResponseModel(BaseModel):
    credential: str = Field(alias="Credential")
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class DeleteInAppTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class DeleteJourneyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")


class DeletePushTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class DeleteRecommenderConfigurationRequestModel(BaseModel):
    recommender_id: str = Field(alias="RecommenderId")


class DeleteSegmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")


class DeleteSmsChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class SMSChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    promotional_messages_per_second: Optional[int] = Field(
        default=None, alias="PromotionalMessagesPerSecond"
    )
    sender_id: Optional[str] = Field(default=None, alias="SenderId")
    short_code: Optional[str] = Field(default=None, alias="ShortCode")
    transactional_messages_per_second: Optional[int] = Field(
        default=None, alias="TransactionalMessagesPerSecond"
    )
    version: Optional[int] = Field(default=None, alias="Version")


class DeleteSmsTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class DeleteUserEndpointsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    user_id: str = Field(alias="UserId")


class DeleteVoiceChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class VoiceChannelResponseModel(BaseModel):
    platform: str = Field(alias="Platform")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    has_credential: Optional[bool] = Field(default=None, alias="HasCredential")
    id: Optional[str] = Field(default=None, alias="Id")
    is_archived: Optional[bool] = Field(default=None, alias="IsArchived")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    version: Optional[int] = Field(default=None, alias="Version")


class DeleteVoiceTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class GCMMessageModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    collapse_key: Optional[str] = Field(default=None, alias="CollapseKey")
    data: Optional[Mapping[str, str]] = Field(default=None, alias="Data")
    icon_reference: Optional[str] = Field(default=None, alias="IconReference")
    image_icon_url: Optional[str] = Field(default=None, alias="ImageIconUrl")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    priority: Optional[str] = Field(default=None, alias="Priority")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    restricted_package_name: Optional[str] = Field(
        default=None, alias="RestrictedPackageName"
    )
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    small_image_icon_url: Optional[str] = Field(default=None, alias="SmallImageIconUrl")
    sound: Optional[str] = Field(default=None, alias="Sound")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class SMSMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    keyword: Optional[str] = Field(default=None, alias="Keyword")
    media_url: Optional[str] = Field(default=None, alias="MediaUrl")
    message_type: Optional[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        default=None, alias="MessageType"
    )
    origination_number: Optional[str] = Field(default=None, alias="OriginationNumber")
    sender_id: Optional[str] = Field(default=None, alias="SenderId")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")


class VoiceMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    origination_number: Optional[str] = Field(default=None, alias="OriginationNumber")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    voice_id: Optional[str] = Field(default=None, alias="VoiceId")


class EmailChannelRequestModel(BaseModel):
    from_address: str = Field(alias="FromAddress")
    identity: str = Field(alias="Identity")
    configuration_set: Optional[str] = Field(default=None, alias="ConfigurationSet")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class JourneyEmailMessageModel(BaseModel):
    from_address: Optional[str] = Field(default=None, alias="FromAddress")


class RawEmailModel(BaseModel):
    data: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Data"
    )


class EmailTemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    html_part: Optional[str] = Field(default=None, alias="HtmlPart")
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    subject: Optional[str] = Field(default=None, alias="Subject")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    text_part: Optional[str] = Field(default=None, alias="TextPart")
    version: Optional[str] = Field(default=None, alias="Version")


class EndpointDemographicModel(BaseModel):
    app_version: Optional[str] = Field(default=None, alias="AppVersion")
    locale: Optional[str] = Field(default=None, alias="Locale")
    make: Optional[str] = Field(default=None, alias="Make")
    model: Optional[str] = Field(default=None, alias="Model")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    platform: Optional[str] = Field(default=None, alias="Platform")
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class EndpointLocationModel(BaseModel):
    city: Optional[str] = Field(default=None, alias="City")
    country: Optional[str] = Field(default=None, alias="Country")
    latitude: Optional[float] = Field(default=None, alias="Latitude")
    longitude: Optional[float] = Field(default=None, alias="Longitude")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")
    region: Optional[str] = Field(default=None, alias="Region")


class EndpointUserModel(BaseModel):
    user_attributes: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="UserAttributes"
    )
    user_id: Optional[str] = Field(default=None, alias="UserId")


class EndpointItemResponseModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    status_code: Optional[int] = Field(default=None, alias="StatusCode")


class EndpointMessageResultModel(BaseModel):
    delivery_status: Literal[
        "DUPLICATE",
        "OPT_OUT",
        "PERMANENT_FAILURE",
        "SUCCESSFUL",
        "TEMPORARY_FAILURE",
        "THROTTLED",
        "UNKNOWN_FAILURE",
    ] = Field(alias="DeliveryStatus")
    status_code: int = Field(alias="StatusCode")
    address: Optional[str] = Field(default=None, alias="Address")
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    updated_token: Optional[str] = Field(default=None, alias="UpdatedToken")


class EndpointSendConfigurationModel(BaseModel):
    body_override: Optional[str] = Field(default=None, alias="BodyOverride")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )
    title_override: Optional[str] = Field(default=None, alias="TitleOverride")


class MetricDimensionModel(BaseModel):
    comparison_operator: str = Field(alias="ComparisonOperator")
    value: float = Field(alias="Value")


class SetDimensionModel(BaseModel):
    values: Sequence[str] = Field(alias="Values")
    dimension_type: Optional[Literal["EXCLUSIVE", "INCLUSIVE"]] = Field(
        default=None, alias="DimensionType"
    )


class EventItemResponseModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    status_code: Optional[int] = Field(default=None, alias="StatusCode")


class SessionModel(BaseModel):
    id: str = Field(alias="Id")
    start_timestamp: str = Field(alias="StartTimestamp")
    duration: Optional[int] = Field(default=None, alias="Duration")
    stop_timestamp: Optional[str] = Field(default=None, alias="StopTimestamp")


class ExportJobResourceModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    s3_url_prefix: str = Field(alias="S3UrlPrefix")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")
    segment_version: Optional[int] = Field(default=None, alias="SegmentVersion")


class GCMChannelRequestModel(BaseModel):
    api_key: str = Field(alias="ApiKey")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class GPSCoordinatesModel(BaseModel):
    latitude: float = Field(alias="Latitude")
    longitude: float = Field(alias="Longitude")


class GetAdmChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApnsChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApnsSandboxChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApnsVoipChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApnsVoipSandboxChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetAppRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApplicationDateRangeKpiRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    kpi_name: str = Field(alias="KpiName")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class GetApplicationSettingsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetAppsRequestModel(BaseModel):
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetBaiduChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetCampaignActivitiesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetCampaignDateRangeKpiRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    kpi_name: str = Field(alias="KpiName")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class GetCampaignRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")


class GetCampaignVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    version: str = Field(alias="Version")


class GetCampaignVersionsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetCampaignsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetChannelsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetEmailChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class GetEndpointRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_id: str = Field(alias="EndpointId")


class GetEventStreamRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetExportJobRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    job_id: str = Field(alias="JobId")


class GetExportJobsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetGcmChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetImportJobRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    job_id: str = Field(alias="JobId")


class GetImportJobsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetInAppMessagesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_id: str = Field(alias="EndpointId")


class GetInAppTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class GetJourneyDateRangeKpiRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")
    kpi_name: str = Field(alias="KpiName")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")


class GetJourneyExecutionActivityMetricsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_activity_id: str = Field(alias="JourneyActivityId")
    journey_id: str = Field(alias="JourneyId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")


class JourneyExecutionActivityMetricsResponseModel(BaseModel):
    activity_type: str = Field(alias="ActivityType")
    application_id: str = Field(alias="ApplicationId")
    journey_activity_id: str = Field(alias="JourneyActivityId")
    journey_id: str = Field(alias="JourneyId")
    last_evaluated_time: str = Field(alias="LastEvaluatedTime")
    metrics: Dict[str, str] = Field(alias="Metrics")


class GetJourneyExecutionMetricsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")


class JourneyExecutionMetricsResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")
    last_evaluated_time: str = Field(alias="LastEvaluatedTime")
    metrics: Dict[str, str] = Field(alias="Metrics")


class GetJourneyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")


class GetPushTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class GetRecommenderConfigurationRequestModel(BaseModel):
    recommender_id: str = Field(alias="RecommenderId")


class GetRecommenderConfigurationsRequestModel(BaseModel):
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetSegmentExportJobsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetSegmentImportJobsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetSegmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")


class GetSegmentVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")
    version: str = Field(alias="Version")


class GetSegmentVersionsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetSegmentsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class GetSmsChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetSmsTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class SMSTemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    body: Optional[str] = Field(default=None, alias="Body")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class GetUserEndpointsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    user_id: str = Field(alias="UserId")


class GetVoiceChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetVoiceTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    version: Optional[str] = Field(default=None, alias="Version")


class VoiceTemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    body: Optional[str] = Field(default=None, alias="Body")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")
    voice_id: Optional[str] = Field(default=None, alias="VoiceId")


class ImportJobResourceModel(BaseModel):
    format: Literal["CSV", "JSON"] = Field(alias="Format")
    role_arn: str = Field(alias="RoleArn")
    s3_url: str = Field(alias="S3Url")
    define_segment: Optional[bool] = Field(default=None, alias="DefineSegment")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    register_endpoints: Optional[bool] = Field(default=None, alias="RegisterEndpoints")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")
    segment_name: Optional[str] = Field(default=None, alias="SegmentName")


class InAppMessageBodyConfigModel(BaseModel):
    alignment: Literal["CENTER", "LEFT", "RIGHT"] = Field(alias="Alignment")
    body: str = Field(alias="Body")
    text_color: str = Field(alias="TextColor")


class OverrideButtonConfigurationModel(BaseModel):
    button_action: Literal["CLOSE", "DEEP_LINK", "LINK"] = Field(alias="ButtonAction")
    link: Optional[str] = Field(default=None, alias="Link")


class InAppMessageHeaderConfigModel(BaseModel):
    alignment: Literal["CENTER", "LEFT", "RIGHT"] = Field(alias="Alignment")
    header: str = Field(alias="Header")
    text_color: str = Field(alias="TextColor")


class JourneyChannelSettingsModel(BaseModel):
    connect_campaign_arn: Optional[str] = Field(
        default=None, alias="ConnectCampaignArn"
    )
    connect_campaign_execution_role_arn: Optional[str] = Field(
        default=None, alias="ConnectCampaignExecutionRoleArn"
    )


class JourneyLimitsModel(BaseModel):
    daily_cap: Optional[int] = Field(default=None, alias="DailyCap")
    endpoint_reentry_cap: Optional[int] = Field(
        default=None, alias="EndpointReentryCap"
    )
    messages_per_second: Optional[int] = Field(default=None, alias="MessagesPerSecond")
    endpoint_reentry_interval: Optional[str] = Field(
        default=None, alias="EndpointReentryInterval"
    )


class JourneyPushMessageModel(BaseModel):
    time_to_live: Optional[str] = Field(default=None, alias="TimeToLive")


class JourneyScheduleModel(BaseModel):
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class JourneySMSMessageModel(BaseModel):
    message_type: Optional[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        default=None, alias="MessageType"
    )
    origination_number: Optional[str] = Field(default=None, alias="OriginationNumber")
    sender_id: Optional[str] = Field(default=None, alias="SenderId")
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")


class JourneyStateRequestModel(BaseModel):
    state: Optional[
        Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
    ] = Field(default=None, alias="State")


class ListJourneysRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    token: Optional[str] = Field(default=None, alias="Token")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagsModelModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")


class ListTemplateVersionsRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_type: str = Field(alias="TemplateType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")


class ListTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[str] = Field(default=None, alias="PageSize")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    template_type: Optional[str] = Field(default=None, alias="TemplateType")


class MessageModel(BaseModel):
    action: Optional[Literal["DEEP_LINK", "OPEN_APP", "URL"]] = Field(
        default=None, alias="Action"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    image_icon_url: Optional[str] = Field(default=None, alias="ImageIconUrl")
    image_small_icon_url: Optional[str] = Field(default=None, alias="ImageSmallIconUrl")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    json_body: Optional[str] = Field(default=None, alias="JsonBody")
    media_url: Optional[str] = Field(default=None, alias="MediaUrl")
    raw_content: Optional[str] = Field(default=None, alias="RawContent")
    silent_push: Optional[bool] = Field(default=None, alias="SilentPush")
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    title: Optional[str] = Field(default=None, alias="Title")
    url: Optional[str] = Field(default=None, alias="Url")


class MessageResultModel(BaseModel):
    delivery_status: Literal[
        "DUPLICATE",
        "OPT_OUT",
        "PERMANENT_FAILURE",
        "SUCCESSFUL",
        "TEMPORARY_FAILURE",
        "THROTTLED",
        "UNKNOWN_FAILURE",
    ] = Field(alias="DeliveryStatus")
    status_code: int = Field(alias="StatusCode")
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    updated_token: Optional[str] = Field(default=None, alias="UpdatedToken")


class NumberValidateRequestModel(BaseModel):
    iso_country_code: Optional[str] = Field(default=None, alias="IsoCountryCode")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")


class NumberValidateResponseModel(BaseModel):
    carrier: Optional[str] = Field(default=None, alias="Carrier")
    city: Optional[str] = Field(default=None, alias="City")
    cleansed_phone_number_e164: Optional[str] = Field(
        default=None, alias="CleansedPhoneNumberE164"
    )
    cleansed_phone_number_national: Optional[str] = Field(
        default=None, alias="CleansedPhoneNumberNational"
    )
    country: Optional[str] = Field(default=None, alias="Country")
    country_code_iso2: Optional[str] = Field(default=None, alias="CountryCodeIso2")
    country_code_numeric: Optional[str] = Field(
        default=None, alias="CountryCodeNumeric"
    )
    county: Optional[str] = Field(default=None, alias="County")
    original_country_code_iso2: Optional[str] = Field(
        default=None, alias="OriginalCountryCodeIso2"
    )
    original_phone_number: Optional[str] = Field(
        default=None, alias="OriginalPhoneNumber"
    )
    phone_type: Optional[str] = Field(default=None, alias="PhoneType")
    phone_type_code: Optional[int] = Field(default=None, alias="PhoneTypeCode")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    zip_code: Optional[str] = Field(default=None, alias="ZipCode")


class OpenHoursRuleModel(BaseModel):
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    end_time: Optional[str] = Field(default=None, alias="EndTime")


class WriteEventStreamModel(BaseModel):
    destination_stream_arn: str = Field(alias="DestinationStreamArn")
    role_arn: str = Field(alias="RoleArn")


class RandomSplitEntryModel(BaseModel):
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    percentage: Optional[int] = Field(default=None, alias="Percentage")


class RecencyDimensionModel(BaseModel):
    duration: Literal["DAY_14", "DAY_30", "DAY_7", "HR_24"] = Field(alias="Duration")
    recency_type: Literal["ACTIVE", "INACTIVE"] = Field(alias="RecencyType")


class UpdateAttributesRequestModel(BaseModel):
    blacklist: Optional[Sequence[str]] = Field(default=None, alias="Blacklist")


class ResultRowValueModel(BaseModel):
    key: str = Field(alias="Key")
    type: str = Field(alias="Type")
    value: str = Field(alias="Value")


class SMSChannelRequestModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    sender_id: Optional[str] = Field(default=None, alias="SenderId")
    short_code: Optional[str] = Field(default=None, alias="ShortCode")


class SegmentConditionModel(BaseModel):
    segment_id: str = Field(alias="SegmentId")


class SegmentReferenceModel(BaseModel):
    id: str = Field(alias="Id")
    version: Optional[int] = Field(default=None, alias="Version")


class SegmentImportResourceModel(BaseModel):
    external_id: str = Field(alias="ExternalId")
    format: Literal["CSV", "JSON"] = Field(alias="Format")
    role_arn: str = Field(alias="RoleArn")
    s3_url: str = Field(alias="S3Url")
    size: int = Field(alias="Size")
    channel_counts: Optional[Dict[str, int]] = Field(
        default=None, alias="ChannelCounts"
    )


class SendOTPMessageRequestParametersModel(BaseModel):
    brand_name: str = Field(alias="BrandName")
    channel: str = Field(alias="Channel")
    destination_identity: str = Field(alias="DestinationIdentity")
    origination_identity: str = Field(alias="OriginationIdentity")
    reference_id: str = Field(alias="ReferenceId")
    allowed_attempts: Optional[int] = Field(default=None, alias="AllowedAttempts")
    code_length: Optional[int] = Field(default=None, alias="CodeLength")
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    language: Optional[str] = Field(default=None, alias="Language")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
    validity_period: Optional[int] = Field(default=None, alias="ValidityPeriod")


class SimpleEmailPartModel(BaseModel):
    charset: Optional[str] = Field(default=None, alias="Charset")
    data: Optional[str] = Field(default=None, alias="Data")


class TemplateActiveVersionRequestModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")


class TemplateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class TemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class TemplateVersionResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: str = Field(alias="TemplateType")
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateRecommenderConfigurationModel(BaseModel):
    recommendation_provider_role_arn: str = Field(alias="RecommendationProviderRoleArn")
    recommendation_provider_uri: str = Field(alias="RecommendationProviderUri")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    recommendation_provider_id_type: Optional[str] = Field(
        default=None, alias="RecommendationProviderIdType"
    )
    recommendation_transformer_uri: Optional[str] = Field(
        default=None, alias="RecommendationTransformerUri"
    )
    recommendations_display_name: Optional[str] = Field(
        default=None, alias="RecommendationsDisplayName"
    )
    recommendations_per_message: Optional[int] = Field(
        default=None, alias="RecommendationsPerMessage"
    )


class VoiceChannelRequestModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class VerificationResponseModel(BaseModel):
    valid: Optional[bool] = Field(default=None, alias="Valid")


class VerifyOTPMessageRequestParametersModel(BaseModel):
    destination_identity: str = Field(alias="DestinationIdentity")
    otp: str = Field(alias="Otp")
    reference_id: str = Field(alias="ReferenceId")


class UpdateAdmChannelRequestModel(BaseModel):
    admchannel_request: ADMChannelRequestModel = Field(alias="ADMChannelRequest")
    application_id: str = Field(alias="ApplicationId")


class UpdateApnsChannelRequestModel(BaseModel):
    ap_ns_channel_request: APNSChannelRequestModel = Field(alias="APNSChannelRequest")
    application_id: str = Field(alias="ApplicationId")


class UpdateApnsSandboxChannelRequestModel(BaseModel):
    ap_ns_sandbox_channel_request: APNSSandboxChannelRequestModel = Field(
        alias="APNSSandboxChannelRequest"
    )
    application_id: str = Field(alias="ApplicationId")


class UpdateApnsVoipChannelRequestModel(BaseModel):
    ap_ns_voip_channel_request: APNSVoipChannelRequestModel = Field(
        alias="APNSVoipChannelRequest"
    )
    application_id: str = Field(alias="ApplicationId")


class UpdateApnsVoipSandboxChannelRequestModel(BaseModel):
    ap_ns_voip_sandbox_channel_request: APNSVoipSandboxChannelRequestModel = Field(
        alias="APNSVoipSandboxChannelRequest"
    )
    application_id: str = Field(alias="ApplicationId")


class ActivitiesResponseModel(BaseModel):
    item: List[ActivityResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ApplicationsResponseModel(BaseModel):
    item: Optional[List[ApplicationResponseModel]] = Field(default=None, alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ApplicationSettingsResourceModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_hook: Optional[CampaignHookModel] = Field(
        default=None, alias="CampaignHook"
    )
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    limits: Optional[CampaignLimitsModel] = Field(default=None, alias="Limits")
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")


class WriteApplicationSettingsRequestModel(BaseModel):
    campaign_hook: Optional[CampaignHookModel] = Field(
        default=None, alias="CampaignHook"
    )
    cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchMetricsEnabled"
    )
    event_tagging_enabled: Optional[bool] = Field(
        default=None, alias="EventTaggingEnabled"
    )
    limits: Optional[CampaignLimitsModel] = Field(default=None, alias="Limits")
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")


class UpdateBaiduChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    baidu_channel_request: BaiduChannelRequestModel = Field(alias="BaiduChannelRequest")


class ChannelsResponseModel(BaseModel):
    channels: Dict[str, ChannelResponseModel] = Field(alias="Channels")


class ClosedDaysModel(BaseModel):
    email: Optional[Sequence[ClosedDaysRuleModel]] = Field(default=None, alias="EMAIL")
    s_ms: Optional[Sequence[ClosedDaysRuleModel]] = Field(default=None, alias="SMS")
    p_us_h: Optional[Sequence[ClosedDaysRuleModel]] = Field(default=None, alias="PUSH")
    voice: Optional[Sequence[ClosedDaysRuleModel]] = Field(default=None, alias="VOICE")
    cus_tom: Optional[Sequence[ClosedDaysRuleModel]] = Field(
        default=None, alias="CUSTOM"
    )


class WaitActivityModel(BaseModel):
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    wait_time: Optional[WaitTimeModel] = Field(default=None, alias="WaitTime")


class CreateAppRequestModel(BaseModel):
    create_application_request: CreateApplicationRequestModel = Field(
        alias="CreateApplicationRequest"
    )


class CreateAppResponseModel(BaseModel):
    application_response: ApplicationResponseModel = Field(alias="ApplicationResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAdmChannelResponseModel(BaseModel):
    admchannel_response: ADMChannelResponseModel = Field(alias="ADMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApnsChannelResponseModel(BaseModel):
    ap_ns_channel_response: APNSChannelResponseModel = Field(
        alias="APNSChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApnsSandboxChannelResponseModel(BaseModel):
    ap_ns_sandbox_channel_response: APNSSandboxChannelResponseModel = Field(
        alias="APNSSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApnsVoipChannelResponseModel(BaseModel):
    ap_ns_voip_channel_response: APNSVoipChannelResponseModel = Field(
        alias="APNSVoipChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApnsVoipSandboxChannelResponseModel(BaseModel):
    ap_ns_voip_sandbox_channel_response: APNSVoipSandboxChannelResponseModel = Field(
        alias="APNSVoipSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppResponseModel(BaseModel):
    application_response: ApplicationResponseModel = Field(alias="ApplicationResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBaiduChannelResponseModel(BaseModel):
    baidu_channel_response: BaiduChannelResponseModel = Field(
        alias="BaiduChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAdmChannelResponseModel(BaseModel):
    admchannel_response: ADMChannelResponseModel = Field(alias="ADMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApnsChannelResponseModel(BaseModel):
    ap_ns_channel_response: APNSChannelResponseModel = Field(
        alias="APNSChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApnsSandboxChannelResponseModel(BaseModel):
    ap_ns_sandbox_channel_response: APNSSandboxChannelResponseModel = Field(
        alias="APNSSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApnsVoipChannelResponseModel(BaseModel):
    ap_ns_voip_channel_response: APNSVoipChannelResponseModel = Field(
        alias="APNSVoipChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApnsVoipSandboxChannelResponseModel(BaseModel):
    ap_ns_voip_sandbox_channel_response: APNSVoipSandboxChannelResponseModel = Field(
        alias="APNSVoipSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppResponseModel(BaseModel):
    application_response: ApplicationResponseModel = Field(alias="ApplicationResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBaiduChannelResponseModel(BaseModel):
    baidu_channel_response: BaiduChannelResponseModel = Field(
        alias="BaiduChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveAttributesResponseModel(BaseModel):
    attributes_resource: AttributesResourceModel = Field(alias="AttributesResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAdmChannelResponseModel(BaseModel):
    admchannel_response: ADMChannelResponseModel = Field(alias="ADMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApnsChannelResponseModel(BaseModel):
    ap_ns_channel_response: APNSChannelResponseModel = Field(
        alias="APNSChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApnsSandboxChannelResponseModel(BaseModel):
    ap_ns_sandbox_channel_response: APNSSandboxChannelResponseModel = Field(
        alias="APNSSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApnsVoipChannelResponseModel(BaseModel):
    ap_ns_voip_channel_response: APNSVoipChannelResponseModel = Field(
        alias="APNSVoipChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApnsVoipSandboxChannelResponseModel(BaseModel):
    ap_ns_voip_sandbox_channel_response: APNSVoipSandboxChannelResponseModel = Field(
        alias="APNSVoipSandboxChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBaiduChannelResponseModel(BaseModel):
    baidu_channel_response: BaiduChannelResponseModel = Field(
        alias="BaiduChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEmailTemplateRequestModel(BaseModel):
    email_template_request: EmailTemplateRequestModel = Field(
        alias="EmailTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")


class UpdateEmailTemplateRequestModel(BaseModel):
    email_template_request: EmailTemplateRequestModel = Field(
        alias="EmailTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")
    create_new_version: Optional[bool] = Field(default=None, alias="CreateNewVersion")
    version: Optional[str] = Field(default=None, alias="Version")


class CreateEmailTemplateResponseModel(BaseModel):
    create_template_message_body: CreateTemplateMessageBodyModel = Field(
        alias="CreateTemplateMessageBody"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePushTemplateResponseModel(BaseModel):
    create_template_message_body: CreateTemplateMessageBodyModel = Field(
        alias="CreateTemplateMessageBody"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSmsTemplateResponseModel(BaseModel):
    create_template_message_body: CreateTemplateMessageBodyModel = Field(
        alias="CreateTemplateMessageBody"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVoiceTemplateResponseModel(BaseModel):
    create_template_message_body: CreateTemplateMessageBodyModel = Field(
        alias="CreateTemplateMessageBody"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExportJobRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    export_job_request: ExportJobRequestModel = Field(alias="ExportJobRequest")


class CreateImportJobRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    import_job_request: ImportJobRequestModel = Field(alias="ImportJobRequest")


class CreateInAppTemplateResponseModel(BaseModel):
    template_create_message_body: TemplateCreateMessageBodyModel = Field(
        alias="TemplateCreateMessageBody"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecommenderConfigurationRequestModel(BaseModel):
    create_recommender_configuration: CreateRecommenderConfigurationModel = Field(
        alias="CreateRecommenderConfiguration"
    )


class CreateRecommenderConfigurationResponseModel(BaseModel):
    recommender_configuration_response: RecommenderConfigurationResponseModel = Field(
        alias="RecommenderConfigurationResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRecommenderConfigurationResponseModel(BaseModel):
    recommender_configuration_response: RecommenderConfigurationResponseModel = Field(
        alias="RecommenderConfigurationResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommenderConfigurationResponseModel(BaseModel):
    recommender_configuration_response: RecommenderConfigurationResponseModel = Field(
        alias="RecommenderConfigurationResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecommenderConfigurationsResponseModel(BaseModel):
    item: List[RecommenderConfigurationResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateRecommenderConfigurationResponseModel(BaseModel):
    recommender_configuration_response: RecommenderConfigurationResponseModel = Field(
        alias="RecommenderConfigurationResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSmsTemplateRequestModel(BaseModel):
    s_ms_template_request: SMSTemplateRequestModel = Field(alias="SMSTemplateRequest")
    template_name: str = Field(alias="TemplateName")


class UpdateSmsTemplateRequestModel(BaseModel):
    s_ms_template_request: SMSTemplateRequestModel = Field(alias="SMSTemplateRequest")
    template_name: str = Field(alias="TemplateName")
    create_new_version: Optional[bool] = Field(default=None, alias="CreateNewVersion")
    version: Optional[str] = Field(default=None, alias="Version")


class CreateVoiceTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    voice_template_request: VoiceTemplateRequestModel = Field(
        alias="VoiceTemplateRequest"
    )


class UpdateVoiceTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    voice_template_request: VoiceTemplateRequestModel = Field(
        alias="VoiceTemplateRequest"
    )
    create_new_version: Optional[bool] = Field(default=None, alias="CreateNewVersion")
    version: Optional[str] = Field(default=None, alias="Version")


class CustomMessageActivityModel(BaseModel):
    delivery_uri: Optional[str] = Field(default=None, alias="DeliveryUri")
    endpoint_types: Optional[
        Sequence[
            Literal[
                "ADM",
                "APNS",
                "APNS_SANDBOX",
                "APNS_VOIP",
                "APNS_VOIP_SANDBOX",
                "BAIDU",
                "CUSTOM",
                "EMAIL",
                "GCM",
                "IN_APP",
                "PUSH",
                "SMS",
                "VOICE",
            ]
        ]
    ] = Field(default=None, alias="EndpointTypes")
    message_config: Optional[JourneyCustomMessageModel] = Field(
        default=None, alias="MessageConfig"
    )
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    template_version: Optional[str] = Field(default=None, alias="TemplateVersion")


class PushNotificationTemplateRequestModel(BaseModel):
    adm: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="ADM"
    )
    ap_ns: Optional[APNSPushNotificationTemplateModel] = Field(
        default=None, alias="APNS"
    )
    baidu: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="Baidu"
    )
    default: Optional[DefaultPushNotificationTemplateModel] = Field(
        default=None, alias="Default"
    )
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    gcm: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="GCM"
    )
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )


class PushNotificationTemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    adm: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="ADM"
    )
    ap_ns: Optional[APNSPushNotificationTemplateModel] = Field(
        default=None, alias="APNS"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    baidu: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="Baidu"
    )
    default: Optional[DefaultPushNotificationTemplateModel] = Field(
        default=None, alias="Default"
    )
    default_substitutions: Optional[str] = Field(
        default=None, alias="DefaultSubstitutions"
    )
    gcm: Optional[AndroidPushNotificationTemplateModel] = Field(
        default=None, alias="GCM"
    )
    recommender_id: Optional[str] = Field(default=None, alias="RecommenderId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class DeleteEmailChannelResponseModel(BaseModel):
    email_channel_response: EmailChannelResponseModel = Field(
        alias="EmailChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEmailChannelResponseModel(BaseModel):
    email_channel_response: EmailChannelResponseModel = Field(
        alias="EmailChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEmailChannelResponseModel(BaseModel):
    email_channel_response: EmailChannelResponseModel = Field(
        alias="EmailChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEmailTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInAppTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePushTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSmsTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVoiceTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEmailTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointsBatchResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInAppTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePushTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSmsTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateActiveVersionResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceTemplateResponseModel(BaseModel):
    message_body: MessageBodyModel = Field(alias="MessageBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventStreamResponseModel(BaseModel):
    event_stream: EventStreamModel = Field(alias="EventStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEventStreamResponseModel(BaseModel):
    event_stream: EventStreamModel = Field(alias="EventStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEventStreamResponseModel(BaseModel):
    event_stream: EventStreamModel = Field(alias="EventStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGcmChannelResponseModel(BaseModel):
    gcmchannel_response: GCMChannelResponseModel = Field(alias="GCMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGcmChannelResponseModel(BaseModel):
    gcmchannel_response: GCMChannelResponseModel = Field(alias="GCMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGcmChannelResponseModel(BaseModel):
    gcmchannel_response: GCMChannelResponseModel = Field(alias="GCMChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSmsChannelResponseModel(BaseModel):
    s_ms_channel_response: SMSChannelResponseModel = Field(alias="SMSChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSmsChannelResponseModel(BaseModel):
    s_ms_channel_response: SMSChannelResponseModel = Field(alias="SMSChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSmsChannelResponseModel(BaseModel):
    s_ms_channel_response: SMSChannelResponseModel = Field(alias="SMSChannelResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVoiceChannelResponseModel(BaseModel):
    voice_channel_response: VoiceChannelResponseModel = Field(
        alias="VoiceChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceChannelResponseModel(BaseModel):
    voice_channel_response: VoiceChannelResponseModel = Field(
        alias="VoiceChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceChannelResponseModel(BaseModel):
    voice_channel_response: VoiceChannelResponseModel = Field(
        alias="VoiceChannelResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEmailChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    email_channel_request: EmailChannelRequestModel = Field(alias="EmailChannelRequest")


class EmailMessageActivityModel(BaseModel):
    message_config: Optional[JourneyEmailMessageModel] = Field(
        default=None, alias="MessageConfig"
    )
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    template_version: Optional[str] = Field(default=None, alias="TemplateVersion")


class GetEmailTemplateResponseModel(BaseModel):
    email_template_response: EmailTemplateResponseModel = Field(
        alias="EmailTemplateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointBatchItemModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    attributes: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Attributes"
    )
    channel_type: Optional[
        Literal[
            "ADM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "BAIDU",
            "CUSTOM",
            "EMAIL",
            "GCM",
            "IN_APP",
            "PUSH",
            "SMS",
            "VOICE",
        ]
    ] = Field(default=None, alias="ChannelType")
    demographic: Optional[EndpointDemographicModel] = Field(
        default=None, alias="Demographic"
    )
    effective_date: Optional[str] = Field(default=None, alias="EffectiveDate")
    endpoint_status: Optional[str] = Field(default=None, alias="EndpointStatus")
    id: Optional[str] = Field(default=None, alias="Id")
    location: Optional[EndpointLocationModel] = Field(default=None, alias="Location")
    metrics: Optional[Mapping[str, float]] = Field(default=None, alias="Metrics")
    opt_out: Optional[str] = Field(default=None, alias="OptOut")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    user: Optional[EndpointUserModel] = Field(default=None, alias="User")


class EndpointRequestModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    attributes: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Attributes"
    )
    channel_type: Optional[
        Literal[
            "ADM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "BAIDU",
            "CUSTOM",
            "EMAIL",
            "GCM",
            "IN_APP",
            "PUSH",
            "SMS",
            "VOICE",
        ]
    ] = Field(default=None, alias="ChannelType")
    demographic: Optional[EndpointDemographicModel] = Field(
        default=None, alias="Demographic"
    )
    effective_date: Optional[str] = Field(default=None, alias="EffectiveDate")
    endpoint_status: Optional[str] = Field(default=None, alias="EndpointStatus")
    location: Optional[EndpointLocationModel] = Field(default=None, alias="Location")
    metrics: Optional[Mapping[str, float]] = Field(default=None, alias="Metrics")
    opt_out: Optional[str] = Field(default=None, alias="OptOut")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    user: Optional[EndpointUserModel] = Field(default=None, alias="User")


class EndpointResponseModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    attributes: Optional[Dict[str, List[str]]] = Field(default=None, alias="Attributes")
    channel_type: Optional[
        Literal[
            "ADM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "BAIDU",
            "CUSTOM",
            "EMAIL",
            "GCM",
            "IN_APP",
            "PUSH",
            "SMS",
            "VOICE",
        ]
    ] = Field(default=None, alias="ChannelType")
    cohort_id: Optional[str] = Field(default=None, alias="CohortId")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    demographic: Optional[EndpointDemographicModel] = Field(
        default=None, alias="Demographic"
    )
    effective_date: Optional[str] = Field(default=None, alias="EffectiveDate")
    endpoint_status: Optional[str] = Field(default=None, alias="EndpointStatus")
    id: Optional[str] = Field(default=None, alias="Id")
    location: Optional[EndpointLocationModel] = Field(default=None, alias="Location")
    metrics: Optional[Dict[str, float]] = Field(default=None, alias="Metrics")
    opt_out: Optional[str] = Field(default=None, alias="OptOut")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    user: Optional[EndpointUserModel] = Field(default=None, alias="User")


class PublicEndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    attributes: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Attributes"
    )
    channel_type: Optional[
        Literal[
            "ADM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "BAIDU",
            "CUSTOM",
            "EMAIL",
            "GCM",
            "IN_APP",
            "PUSH",
            "SMS",
            "VOICE",
        ]
    ] = Field(default=None, alias="ChannelType")
    demographic: Optional[EndpointDemographicModel] = Field(
        default=None, alias="Demographic"
    )
    effective_date: Optional[str] = Field(default=None, alias="EffectiveDate")
    endpoint_status: Optional[str] = Field(default=None, alias="EndpointStatus")
    location: Optional[EndpointLocationModel] = Field(default=None, alias="Location")
    metrics: Optional[Mapping[str, float]] = Field(default=None, alias="Metrics")
    opt_out: Optional[str] = Field(default=None, alias="OptOut")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    user: Optional[EndpointUserModel] = Field(default=None, alias="User")


class SendUsersMessageResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    result: Optional[Dict[str, Dict[str, EndpointMessageResultModel]]] = Field(
        default=None, alias="Result"
    )


class EventDimensionsModel(BaseModel):
    attributes: Optional[Mapping[str, AttributeDimensionModel]] = Field(
        default=None, alias="Attributes"
    )
    event_type: Optional[SetDimensionModel] = Field(default=None, alias="EventType")
    metrics: Optional[Mapping[str, MetricDimensionModel]] = Field(
        default=None, alias="Metrics"
    )


class SegmentDemographicsModel(BaseModel):
    app_version: Optional[SetDimensionModel] = Field(default=None, alias="AppVersion")
    channel: Optional[SetDimensionModel] = Field(default=None, alias="Channel")
    device_type: Optional[SetDimensionModel] = Field(default=None, alias="DeviceType")
    make: Optional[SetDimensionModel] = Field(default=None, alias="Make")
    model: Optional[SetDimensionModel] = Field(default=None, alias="Model")
    platform: Optional[SetDimensionModel] = Field(default=None, alias="Platform")


class ItemResponseModel(BaseModel):
    endpoint_item_response: Optional[EndpointItemResponseModel] = Field(
        default=None, alias="EndpointItemResponse"
    )
    events_item_response: Optional[Dict[str, EventItemResponseModel]] = Field(
        default=None, alias="EventsItemResponse"
    )


class EventModel(BaseModel):
    event_type: str = Field(alias="EventType")
    timestamp: str = Field(alias="Timestamp")
    app_package_name: Optional[str] = Field(default=None, alias="AppPackageName")
    app_title: Optional[str] = Field(default=None, alias="AppTitle")
    app_version_code: Optional[str] = Field(default=None, alias="AppVersionCode")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    client_sdk_version: Optional[str] = Field(default=None, alias="ClientSdkVersion")
    metrics: Optional[Mapping[str, float]] = Field(default=None, alias="Metrics")
    sdk_name: Optional[str] = Field(default=None, alias="SdkName")
    session: Optional[SessionModel] = Field(default=None, alias="Session")


class ExportJobResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_date: str = Field(alias="CreationDate")
    definition: ExportJobResourceModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    job_status: Literal[
        "COMPLETED",
        "COMPLETING",
        "CREATED",
        "FAILED",
        "FAILING",
        "INITIALIZING",
        "PENDING_JOB",
        "PREPARING_FOR_INITIALIZATION",
        "PROCESSING",
    ] = Field(alias="JobStatus")
    type: str = Field(alias="Type")
    completed_pieces: Optional[int] = Field(default=None, alias="CompletedPieces")
    completion_date: Optional[str] = Field(default=None, alias="CompletionDate")
    failed_pieces: Optional[int] = Field(default=None, alias="FailedPieces")
    failures: Optional[List[str]] = Field(default=None, alias="Failures")
    total_failures: Optional[int] = Field(default=None, alias="TotalFailures")
    total_pieces: Optional[int] = Field(default=None, alias="TotalPieces")
    total_processed: Optional[int] = Field(default=None, alias="TotalProcessed")


class UpdateGcmChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    gcmchannel_request: GCMChannelRequestModel = Field(alias="GCMChannelRequest")


class GPSPointDimensionModel(BaseModel):
    coordinates: GPSCoordinatesModel = Field(alias="Coordinates")
    range_in_kilometers: Optional[float] = Field(
        default=None, alias="RangeInKilometers"
    )


class GetJourneyExecutionActivityMetricsResponseModel(BaseModel):
    journey_execution_activity_metrics_response: JourneyExecutionActivityMetricsResponseModel = Field(
        alias="JourneyExecutionActivityMetricsResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJourneyExecutionMetricsResponseModel(BaseModel):
    journey_execution_metrics_response: JourneyExecutionMetricsResponseModel = Field(
        alias="JourneyExecutionMetricsResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSmsTemplateResponseModel(BaseModel):
    s_ms_template_response: SMSTemplateResponseModel = Field(
        alias="SMSTemplateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceTemplateResponseModel(BaseModel):
    voice_template_response: VoiceTemplateResponseModel = Field(
        alias="VoiceTemplateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportJobResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_date: str = Field(alias="CreationDate")
    definition: ImportJobResourceModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    job_status: Literal[
        "COMPLETED",
        "COMPLETING",
        "CREATED",
        "FAILED",
        "FAILING",
        "INITIALIZING",
        "PENDING_JOB",
        "PREPARING_FOR_INITIALIZATION",
        "PROCESSING",
    ] = Field(alias="JobStatus")
    type: str = Field(alias="Type")
    completed_pieces: Optional[int] = Field(default=None, alias="CompletedPieces")
    completion_date: Optional[str] = Field(default=None, alias="CompletionDate")
    failed_pieces: Optional[int] = Field(default=None, alias="FailedPieces")
    failures: Optional[List[str]] = Field(default=None, alias="Failures")
    total_failures: Optional[int] = Field(default=None, alias="TotalFailures")
    total_pieces: Optional[int] = Field(default=None, alias="TotalPieces")
    total_processed: Optional[int] = Field(default=None, alias="TotalProcessed")


class InAppMessageButtonModel(BaseModel):
    android: Optional[OverrideButtonConfigurationModel] = Field(
        default=None, alias="Android"
    )
    default_config: Optional[DefaultButtonConfigurationModel] = Field(
        default=None, alias="DefaultConfig"
    )
    ios: Optional[OverrideButtonConfigurationModel] = Field(default=None, alias="IOS")
    web: Optional[OverrideButtonConfigurationModel] = Field(default=None, alias="Web")


class PushMessageActivityModel(BaseModel):
    message_config: Optional[JourneyPushMessageModel] = Field(
        default=None, alias="MessageConfig"
    )
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    template_version: Optional[str] = Field(default=None, alias="TemplateVersion")


class SMSMessageActivityModel(BaseModel):
    message_config: Optional[JourneySMSMessageModel] = Field(
        default=None, alias="MessageConfig"
    )
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    template_version: Optional[str] = Field(default=None, alias="TemplateVersion")


class UpdateJourneyStateRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")
    journey_state_request: JourneyStateRequestModel = Field(alias="JourneyStateRequest")


class ListTagsForResourceResponseModel(BaseModel):
    tags_model: TagsModelModel = Field(alias="TagsModel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags_model: TagsModelModel = Field(alias="TagsModel")


class MessageResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_result: Optional[Dict[str, EndpointMessageResultModel]] = Field(
        default=None, alias="EndpointResult"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    result: Optional[Dict[str, MessageResultModel]] = Field(
        default=None, alias="Result"
    )


class PhoneNumberValidateRequestModel(BaseModel):
    number_validate_request: NumberValidateRequestModel = Field(
        alias="NumberValidateRequest"
    )


class PhoneNumberValidateResponseModel(BaseModel):
    number_validate_response: NumberValidateResponseModel = Field(
        alias="NumberValidateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OpenHoursModel(BaseModel):
    email: Optional[
        Mapping[
            Literal[
                "FRIDAY",
                "MONDAY",
                "SATURDAY",
                "SUNDAY",
                "THURSDAY",
                "TUESDAY",
                "WEDNESDAY",
            ],
            Sequence[OpenHoursRuleModel],
        ]
    ] = Field(default=None, alias="EMAIL")
    s_ms: Optional[
        Mapping[
            Literal[
                "FRIDAY",
                "MONDAY",
                "SATURDAY",
                "SUNDAY",
                "THURSDAY",
                "TUESDAY",
                "WEDNESDAY",
            ],
            Sequence[OpenHoursRuleModel],
        ]
    ] = Field(default=None, alias="SMS")
    p_us_h: Optional[
        Mapping[
            Literal[
                "FRIDAY",
                "MONDAY",
                "SATURDAY",
                "SUNDAY",
                "THURSDAY",
                "TUESDAY",
                "WEDNESDAY",
            ],
            Sequence[OpenHoursRuleModel],
        ]
    ] = Field(default=None, alias="PUSH")
    voice: Optional[
        Mapping[
            Literal[
                "FRIDAY",
                "MONDAY",
                "SATURDAY",
                "SUNDAY",
                "THURSDAY",
                "TUESDAY",
                "WEDNESDAY",
            ],
            Sequence[OpenHoursRuleModel],
        ]
    ] = Field(default=None, alias="VOICE")
    cus_tom: Optional[
        Mapping[
            Literal[
                "FRIDAY",
                "MONDAY",
                "SATURDAY",
                "SUNDAY",
                "THURSDAY",
                "TUESDAY",
                "WEDNESDAY",
            ],
            Sequence[OpenHoursRuleModel],
        ]
    ] = Field(default=None, alias="CUSTOM")


class PutEventStreamRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    write_event_stream: WriteEventStreamModel = Field(alias="WriteEventStream")


class RandomSplitActivityModel(BaseModel):
    branches: Optional[Sequence[RandomSplitEntryModel]] = Field(
        default=None, alias="Branches"
    )


class SegmentBehaviorsModel(BaseModel):
    recency: Optional[RecencyDimensionModel] = Field(default=None, alias="Recency")


class RemoveAttributesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    attribute_type: str = Field(alias="AttributeType")
    update_attributes_request: UpdateAttributesRequestModel = Field(
        alias="UpdateAttributesRequest"
    )


class ResultRowModel(BaseModel):
    grouped_bys: List[ResultRowValueModel] = Field(alias="GroupedBys")
    values: List[ResultRowValueModel] = Field(alias="Values")


class UpdateSmsChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    s_ms_channel_request: SMSChannelRequestModel = Field(alias="SMSChannelRequest")


class SendOTPMessageRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    send_otp_message_request_parameters: SendOTPMessageRequestParametersModel = Field(
        alias="SendOTPMessageRequestParameters"
    )


class SimpleEmailModel(BaseModel):
    html_part: Optional[SimpleEmailPartModel] = Field(default=None, alias="HtmlPart")
    subject: Optional[SimpleEmailPartModel] = Field(default=None, alias="Subject")
    text_part: Optional[SimpleEmailPartModel] = Field(default=None, alias="TextPart")


class UpdateTemplateActiveVersionRequestModel(BaseModel):
    template_active_version_request: TemplateActiveVersionRequestModel = Field(
        alias="TemplateActiveVersionRequest"
    )
    template_name: str = Field(alias="TemplateName")
    template_type: str = Field(alias="TemplateType")


class TemplateConfigurationModel(BaseModel):
    email_template: Optional[TemplateModel] = Field(default=None, alias="EmailTemplate")
    push_template: Optional[TemplateModel] = Field(default=None, alias="PushTemplate")
    s_ms_template: Optional[TemplateModel] = Field(default=None, alias="SMSTemplate")
    voice_template: Optional[TemplateModel] = Field(default=None, alias="VoiceTemplate")


class TemplatesResponseModel(BaseModel):
    item: List[TemplateResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TemplateVersionsResponseModel(BaseModel):
    item: List[TemplateVersionResponseModel] = Field(alias="Item")
    message: Optional[str] = Field(default=None, alias="Message")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    request_id: Optional[str] = Field(default=None, alias="RequestID")


class UpdateRecommenderConfigurationRequestModel(BaseModel):
    recommender_id: str = Field(alias="RecommenderId")
    update_recommender_configuration: UpdateRecommenderConfigurationModel = Field(
        alias="UpdateRecommenderConfiguration"
    )


class UpdateVoiceChannelRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    voice_channel_request: VoiceChannelRequestModel = Field(alias="VoiceChannelRequest")


class VerifyOTPMessageResponseModel(BaseModel):
    verification_response: VerificationResponseModel = Field(
        alias="VerificationResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyOTPMessageRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    verify_otp_message_request_parameters: VerifyOTPMessageRequestParametersModel = (
        Field(alias="VerifyOTPMessageRequestParameters")
    )


class GetCampaignActivitiesResponseModel(BaseModel):
    activities_response: ActivitiesResponseModel = Field(alias="ActivitiesResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppsResponseModel(BaseModel):
    applications_response: ApplicationsResponseModel = Field(
        alias="ApplicationsResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationSettingsResponseModel(BaseModel):
    application_settings_resource: ApplicationSettingsResourceModel = Field(
        alias="ApplicationSettingsResource"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationSettingsResponseModel(BaseModel):
    application_settings_resource: ApplicationSettingsResourceModel = Field(
        alias="ApplicationSettingsResource"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationSettingsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    write_application_settings_request: WriteApplicationSettingsRequestModel = Field(
        alias="WriteApplicationSettingsRequest"
    )


class GetChannelsResponseModel(BaseModel):
    channels_response: ChannelsResponseModel = Field(alias="ChannelsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommenderConfigurationsResponseModel(BaseModel):
    list_recommender_configurations_response: ListRecommenderConfigurationsResponseModel = Field(
        alias="ListRecommenderConfigurationsResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePushTemplateRequestModel(BaseModel):
    push_notification_template_request: PushNotificationTemplateRequestModel = Field(
        alias="PushNotificationTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")


class UpdatePushTemplateRequestModel(BaseModel):
    push_notification_template_request: PushNotificationTemplateRequestModel = Field(
        alias="PushNotificationTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")
    create_new_version: Optional[bool] = Field(default=None, alias="CreateNewVersion")
    version: Optional[str] = Field(default=None, alias="Version")


class GetPushTemplateResponseModel(BaseModel):
    push_notification_template_response: PushNotificationTemplateResponseModel = Field(
        alias="PushNotificationTemplateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointBatchRequestModel(BaseModel):
    item: Sequence[EndpointBatchItemModel] = Field(alias="Item")


class UpdateEndpointRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_id: str = Field(alias="EndpointId")
    endpoint_request: EndpointRequestModel = Field(alias="EndpointRequest")


class DeleteEndpointResponseModel(BaseModel):
    endpoint_response: EndpointResponseModel = Field(alias="EndpointResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointsResponseModel(BaseModel):
    item: List[EndpointResponseModel] = Field(alias="Item")


class GetEndpointResponseModel(BaseModel):
    endpoint_response: EndpointResponseModel = Field(alias="EndpointResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendUsersMessagesResponseModel(BaseModel):
    send_users_message_response: SendUsersMessageResponseModel = Field(
        alias="SendUsersMessageResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CampaignEventFilterModel(BaseModel):
    dimensions: EventDimensionsModel = Field(alias="Dimensions")
    filter_type: Literal["ENDPOINT", "SYSTEM"] = Field(alias="FilterType")


class EventConditionModel(BaseModel):
    dimensions: Optional[EventDimensionsModel] = Field(default=None, alias="Dimensions")
    message_activity: Optional[str] = Field(default=None, alias="MessageActivity")


class EventFilterModel(BaseModel):
    dimensions: EventDimensionsModel = Field(alias="Dimensions")
    filter_type: Literal["ENDPOINT", "SYSTEM"] = Field(alias="FilterType")


class EventsResponseModel(BaseModel):
    results: Optional[Dict[str, ItemResponseModel]] = Field(
        default=None, alias="Results"
    )


class EventsBatchModel(BaseModel):
    endpoint: PublicEndpointModel = Field(alias="Endpoint")
    events: Mapping[str, EventModel] = Field(alias="Events")


class CreateExportJobResponseModel(BaseModel):
    export_job_response: ExportJobResponseModel = Field(alias="ExportJobResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportJobsResponseModel(BaseModel):
    item: List[ExportJobResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetExportJobResponseModel(BaseModel):
    export_job_response: ExportJobResponseModel = Field(alias="ExportJobResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SegmentLocationModel(BaseModel):
    country: Optional[SetDimensionModel] = Field(default=None, alias="Country")
    gp_s_point: Optional[GPSPointDimensionModel] = Field(default=None, alias="GPSPoint")


class CreateImportJobResponseModel(BaseModel):
    import_job_response: ImportJobResponseModel = Field(alias="ImportJobResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImportJobResponseModel(BaseModel):
    import_job_response: ImportJobResponseModel = Field(alias="ImportJobResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportJobsResponseModel(BaseModel):
    item: List[ImportJobResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class InAppMessageContentModel(BaseModel):
    background_color: Optional[str] = Field(default=None, alias="BackgroundColor")
    body_config: Optional[InAppMessageBodyConfigModel] = Field(
        default=None, alias="BodyConfig"
    )
    header_config: Optional[InAppMessageHeaderConfigModel] = Field(
        default=None, alias="HeaderConfig"
    )
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    primary_btn: Optional[InAppMessageButtonModel] = Field(
        default=None, alias="PrimaryBtn"
    )
    secondary_btn: Optional[InAppMessageButtonModel] = Field(
        default=None, alias="SecondaryBtn"
    )


class SendMessagesResponseModel(BaseModel):
    message_response: MessageResponseModel = Field(alias="MessageResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendOTPMessageResponseModel(BaseModel):
    message_response: MessageResponseModel = Field(alias="MessageResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BaseKpiResultModel(BaseModel):
    rows: List[ResultRowModel] = Field(alias="Rows")


class EmailMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    feedback_forwarding_address: Optional[str] = Field(
        default=None, alias="FeedbackForwardingAddress"
    )
    from_address: Optional[str] = Field(default=None, alias="FromAddress")
    raw_email: Optional[RawEmailModel] = Field(default=None, alias="RawEmail")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    simple_email: Optional[SimpleEmailModel] = Field(default=None, alias="SimpleEmail")
    substitutions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Substitutions"
    )


class ListTemplatesResponseModel(BaseModel):
    templates_response: TemplatesResponseModel = Field(alias="TemplatesResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplateVersionsResponseModel(BaseModel):
    template_versions_response: TemplateVersionsResponseModel = Field(
        alias="TemplateVersionsResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointsBatchRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    endpoint_batch_request: EndpointBatchRequestModel = Field(
        alias="EndpointBatchRequest"
    )


class DeleteUserEndpointsResponseModel(BaseModel):
    endpoints_response: EndpointsResponseModel = Field(alias="EndpointsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserEndpointsResponseModel(BaseModel):
    endpoints_response: EndpointsResponseModel = Field(alias="EndpointsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InAppCampaignScheduleModel(BaseModel):
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    event_filter: Optional[CampaignEventFilterModel] = Field(
        default=None, alias="EventFilter"
    )
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")


class ScheduleModel(BaseModel):
    start_time: str = Field(alias="StartTime")
    end_time: Optional[str] = Field(default=None, alias="EndTime")
    event_filter: Optional[CampaignEventFilterModel] = Field(
        default=None, alias="EventFilter"
    )
    frequency: Optional[
        Literal["DAILY", "EVENT", "HOURLY", "IN_APP_EVENT", "MONTHLY", "ONCE", "WEEKLY"]
    ] = Field(default=None, alias="Frequency")
    is_local_time: Optional[bool] = Field(default=None, alias="IsLocalTime")
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class EventStartConditionModel(BaseModel):
    event_filter: Optional[EventFilterModel] = Field(default=None, alias="EventFilter")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")


class PutEventsResponseModel(BaseModel):
    events_response: EventsResponseModel = Field(alias="EventsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventsRequestModel(BaseModel):
    batch_item: Mapping[str, EventsBatchModel] = Field(alias="BatchItem")


class GetExportJobsResponseModel(BaseModel):
    export_jobs_response: ExportJobsResponseModel = Field(alias="ExportJobsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentExportJobsResponseModel(BaseModel):
    export_jobs_response: ExportJobsResponseModel = Field(alias="ExportJobsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SegmentDimensionsModel(BaseModel):
    attributes: Optional[Mapping[str, AttributeDimensionModel]] = Field(
        default=None, alias="Attributes"
    )
    behavior: Optional[SegmentBehaviorsModel] = Field(default=None, alias="Behavior")
    demographic: Optional[SegmentDemographicsModel] = Field(
        default=None, alias="Demographic"
    )
    location: Optional[SegmentLocationModel] = Field(default=None, alias="Location")
    metrics: Optional[Mapping[str, MetricDimensionModel]] = Field(
        default=None, alias="Metrics"
    )
    user_attributes: Optional[Mapping[str, AttributeDimensionModel]] = Field(
        default=None, alias="UserAttributes"
    )


class GetImportJobsResponseModel(BaseModel):
    import_jobs_response: ImportJobsResponseModel = Field(alias="ImportJobsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentImportJobsResponseModel(BaseModel):
    import_jobs_response: ImportJobsResponseModel = Field(alias="ImportJobsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CampaignInAppMessageModel(BaseModel):
    body: Optional[str] = Field(default=None, alias="Body")
    content: Optional[Sequence[InAppMessageContentModel]] = Field(
        default=None, alias="Content"
    )
    custom_config: Optional[Mapping[str, str]] = Field(
        default=None, alias="CustomConfig"
    )
    layout: Optional[
        Literal[
            "BOTTOM_BANNER",
            "CAROUSEL",
            "MIDDLE_BANNER",
            "MOBILE_FEED",
            "OVERLAYS",
            "TOP_BANNER",
        ]
    ] = Field(default=None, alias="Layout")


class InAppMessageModel(BaseModel):
    content: Optional[List[InAppMessageContentModel]] = Field(
        default=None, alias="Content"
    )
    custom_config: Optional[Dict[str, str]] = Field(default=None, alias="CustomConfig")
    layout: Optional[
        Literal[
            "BOTTOM_BANNER",
            "CAROUSEL",
            "MIDDLE_BANNER",
            "MOBILE_FEED",
            "OVERLAYS",
            "TOP_BANNER",
        ]
    ] = Field(default=None, alias="Layout")


class InAppTemplateRequestModel(BaseModel):
    content: Optional[Sequence[InAppMessageContentModel]] = Field(
        default=None, alias="Content"
    )
    custom_config: Optional[Mapping[str, str]] = Field(
        default=None, alias="CustomConfig"
    )
    layout: Optional[
        Literal[
            "BOTTOM_BANNER",
            "CAROUSEL",
            "MIDDLE_BANNER",
            "MOBILE_FEED",
            "OVERLAYS",
            "TOP_BANNER",
        ]
    ] = Field(default=None, alias="Layout")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )


class InAppTemplateResponseModel(BaseModel):
    creation_date: str = Field(alias="CreationDate")
    last_modified_date: str = Field(alias="LastModifiedDate")
    template_name: str = Field(alias="TemplateName")
    template_type: Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"] = Field(
        alias="TemplateType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    content: Optional[List[InAppMessageContentModel]] = Field(
        default=None, alias="Content"
    )
    custom_config: Optional[Dict[str, str]] = Field(default=None, alias="CustomConfig")
    layout: Optional[
        Literal[
            "BOTTOM_BANNER",
            "CAROUSEL",
            "MIDDLE_BANNER",
            "MOBILE_FEED",
            "OVERLAYS",
            "TOP_BANNER",
        ]
    ] = Field(default=None, alias="Layout")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class ApplicationDateRangeKpiResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    end_time: datetime = Field(alias="EndTime")
    kpi_name: str = Field(alias="KpiName")
    kpi_result: BaseKpiResultModel = Field(alias="KpiResult")
    start_time: datetime = Field(alias="StartTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CampaignDateRangeKpiResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    end_time: datetime = Field(alias="EndTime")
    kpi_name: str = Field(alias="KpiName")
    kpi_result: BaseKpiResultModel = Field(alias="KpiResult")
    start_time: datetime = Field(alias="StartTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class JourneyDateRangeKpiResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    end_time: datetime = Field(alias="EndTime")
    journey_id: str = Field(alias="JourneyId")
    kpi_name: str = Field(alias="KpiName")
    kpi_result: BaseKpiResultModel = Field(alias="KpiResult")
    start_time: datetime = Field(alias="StartTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DirectMessageConfigurationModel(BaseModel):
    admmessage: Optional[ADMMessageModel] = Field(default=None, alias="ADMMessage")
    ap_ns_message: Optional[APNSMessageModel] = Field(default=None, alias="APNSMessage")
    baidu_message: Optional[BaiduMessageModel] = Field(
        default=None, alias="BaiduMessage"
    )
    default_message: Optional[DefaultMessageModel] = Field(
        default=None, alias="DefaultMessage"
    )
    default_push_notification_message: Optional[
        DefaultPushNotificationMessageModel
    ] = Field(default=None, alias="DefaultPushNotificationMessage")
    email_message: Optional[EmailMessageModel] = Field(
        default=None, alias="EmailMessage"
    )
    gcmmessage: Optional[GCMMessageModel] = Field(default=None, alias="GCMMessage")
    s_ms_message: Optional[SMSMessageModel] = Field(default=None, alias="SMSMessage")
    voice_message: Optional[VoiceMessageModel] = Field(
        default=None, alias="VoiceMessage"
    )


class StartConditionModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    event_start_condition: Optional[EventStartConditionModel] = Field(
        default=None, alias="EventStartCondition"
    )
    segment_start_condition: Optional[SegmentConditionModel] = Field(
        default=None, alias="SegmentStartCondition"
    )


class PutEventsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    events_request: EventsRequestModel = Field(alias="EventsRequest")


class SegmentGroupModel(BaseModel):
    dimensions: Optional[Sequence[SegmentDimensionsModel]] = Field(
        default=None, alias="Dimensions"
    )
    source_segments: Optional[Sequence[SegmentReferenceModel]] = Field(
        default=None, alias="SourceSegments"
    )
    source_type: Optional[Literal["ALL", "ANY", "NONE"]] = Field(
        default=None, alias="SourceType"
    )
    type: Optional[Literal["ALL", "ANY", "NONE"]] = Field(default=None, alias="Type")


class SimpleConditionModel(BaseModel):
    event_condition: Optional[EventConditionModel] = Field(
        default=None, alias="EventCondition"
    )
    segment_condition: Optional[SegmentConditionModel] = Field(
        default=None, alias="SegmentCondition"
    )
    segment_dimensions: Optional[SegmentDimensionsModel] = Field(
        default=None, alias="SegmentDimensions"
    )


class MessageConfigurationModel(BaseModel):
    admmessage: Optional[MessageModel] = Field(default=None, alias="ADMMessage")
    ap_ns_message: Optional[MessageModel] = Field(default=None, alias="APNSMessage")
    baidu_message: Optional[MessageModel] = Field(default=None, alias="BaiduMessage")
    custom_message: Optional[CampaignCustomMessageModel] = Field(
        default=None, alias="CustomMessage"
    )
    default_message: Optional[MessageModel] = Field(
        default=None, alias="DefaultMessage"
    )
    email_message: Optional[CampaignEmailMessageModel] = Field(
        default=None, alias="EmailMessage"
    )
    gcmmessage: Optional[MessageModel] = Field(default=None, alias="GCMMessage")
    s_ms_message: Optional[CampaignSmsMessageModel] = Field(
        default=None, alias="SMSMessage"
    )
    in_app_message: Optional[CampaignInAppMessageModel] = Field(
        default=None, alias="InAppMessage"
    )


class InAppMessageCampaignModel(BaseModel):
    campaign_id: Optional[str] = Field(default=None, alias="CampaignId")
    daily_cap: Optional[int] = Field(default=None, alias="DailyCap")
    in_app_message: Optional[InAppMessageModel] = Field(
        default=None, alias="InAppMessage"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    schedule: Optional[InAppCampaignScheduleModel] = Field(
        default=None, alias="Schedule"
    )
    session_cap: Optional[int] = Field(default=None, alias="SessionCap")
    total_cap: Optional[int] = Field(default=None, alias="TotalCap")
    treatment_id: Optional[str] = Field(default=None, alias="TreatmentId")


class CreateInAppTemplateRequestModel(BaseModel):
    in_app_template_request: InAppTemplateRequestModel = Field(
        alias="InAppTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")


class UpdateInAppTemplateRequestModel(BaseModel):
    in_app_template_request: InAppTemplateRequestModel = Field(
        alias="InAppTemplateRequest"
    )
    template_name: str = Field(alias="TemplateName")
    create_new_version: Optional[bool] = Field(default=None, alias="CreateNewVersion")
    version: Optional[str] = Field(default=None, alias="Version")


class GetInAppTemplateResponseModel(BaseModel):
    in_app_template_response: InAppTemplateResponseModel = Field(
        alias="InAppTemplateResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationDateRangeKpiResponseModel(BaseModel):
    application_date_range_kpi_response: ApplicationDateRangeKpiResponseModel = Field(
        alias="ApplicationDateRangeKpiResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCampaignDateRangeKpiResponseModel(BaseModel):
    campaign_date_range_kpi_response: CampaignDateRangeKpiResponseModel = Field(
        alias="CampaignDateRangeKpiResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJourneyDateRangeKpiResponseModel(BaseModel):
    journey_date_range_kpi_response: JourneyDateRangeKpiResponseModel = Field(
        alias="JourneyDateRangeKpiResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MessageRequestModel(BaseModel):
    message_configuration: DirectMessageConfigurationModel = Field(
        alias="MessageConfiguration"
    )
    addresses: Optional[Mapping[str, AddressConfigurationModel]] = Field(
        default=None, alias="Addresses"
    )
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    endpoints: Optional[Mapping[str, EndpointSendConfigurationModel]] = Field(
        default=None, alias="Endpoints"
    )
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    trace_id: Optional[str] = Field(default=None, alias="TraceId")


class SendUsersMessageRequestModel(BaseModel):
    message_configuration: DirectMessageConfigurationModel = Field(
        alias="MessageConfiguration"
    )
    users: Mapping[str, EndpointSendConfigurationModel] = Field(alias="Users")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    trace_id: Optional[str] = Field(default=None, alias="TraceId")


class SegmentGroupListModel(BaseModel):
    groups: Optional[Sequence[SegmentGroupModel]] = Field(default=None, alias="Groups")
    include: Optional[Literal["ALL", "ANY", "NONE"]] = Field(
        default=None, alias="Include"
    )


class ConditionModel(BaseModel):
    conditions: Optional[Sequence[SimpleConditionModel]] = Field(
        default=None, alias="Conditions"
    )
    operator: Optional[Literal["ALL", "ANY"]] = Field(default=None, alias="Operator")


class MultiConditionalBranchModel(BaseModel):
    condition: Optional[SimpleConditionModel] = Field(default=None, alias="Condition")
    next_activity: Optional[str] = Field(default=None, alias="NextActivity")


class TreatmentResourceModel(BaseModel):
    id: str = Field(alias="Id")
    size_percent: int = Field(alias="SizePercent")
    custom_delivery_configuration: Optional[CustomDeliveryConfigurationModel] = Field(
        default=None, alias="CustomDeliveryConfiguration"
    )
    message_configuration: Optional[MessageConfigurationModel] = Field(
        default=None, alias="MessageConfiguration"
    )
    schedule: Optional[ScheduleModel] = Field(default=None, alias="Schedule")
    state: Optional[CampaignStateModel] = Field(default=None, alias="State")
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    treatment_description: Optional[str] = Field(
        default=None, alias="TreatmentDescription"
    )
    treatment_name: Optional[str] = Field(default=None, alias="TreatmentName")


class WriteTreatmentResourceModel(BaseModel):
    size_percent: int = Field(alias="SizePercent")
    custom_delivery_configuration: Optional[CustomDeliveryConfigurationModel] = Field(
        default=None, alias="CustomDeliveryConfiguration"
    )
    message_configuration: Optional[MessageConfigurationModel] = Field(
        default=None, alias="MessageConfiguration"
    )
    schedule: Optional[ScheduleModel] = Field(default=None, alias="Schedule")
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    treatment_description: Optional[str] = Field(
        default=None, alias="TreatmentDescription"
    )
    treatment_name: Optional[str] = Field(default=None, alias="TreatmentName")


class InAppMessagesResponseModel(BaseModel):
    in_app_message_campaigns: Optional[List[InAppMessageCampaignModel]] = Field(
        default=None, alias="InAppMessageCampaigns"
    )


class SendMessagesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    message_request: MessageRequestModel = Field(alias="MessageRequest")


class SendUsersMessagesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    send_users_message_request: SendUsersMessageRequestModel = Field(
        alias="SendUsersMessageRequest"
    )


class SegmentResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    creation_date: str = Field(alias="CreationDate")
    id: str = Field(alias="Id")
    segment_type: Literal["DIMENSIONAL", "IMPORT"] = Field(alias="SegmentType")
    dimensions: Optional[SegmentDimensionsModel] = Field(
        default=None, alias="Dimensions"
    )
    import_definition: Optional[SegmentImportResourceModel] = Field(
        default=None, alias="ImportDefinition"
    )
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    name: Optional[str] = Field(default=None, alias="Name")
    segment_groups: Optional[SegmentGroupListModel] = Field(
        default=None, alias="SegmentGroups"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    version: Optional[int] = Field(default=None, alias="Version")


class WriteSegmentRequestModel(BaseModel):
    dimensions: Optional[SegmentDimensionsModel] = Field(
        default=None, alias="Dimensions"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    segment_groups: Optional[SegmentGroupListModel] = Field(
        default=None, alias="SegmentGroups"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ConditionalSplitActivityModel(BaseModel):
    condition: Optional[ConditionModel] = Field(default=None, alias="Condition")
    evaluation_wait_time: Optional[WaitTimeModel] = Field(
        default=None, alias="EvaluationWaitTime"
    )
    false_activity: Optional[str] = Field(default=None, alias="FalseActivity")
    true_activity: Optional[str] = Field(default=None, alias="TrueActivity")


class MultiConditionalSplitActivityModel(BaseModel):
    branches: Optional[Sequence[MultiConditionalBranchModel]] = Field(
        default=None, alias="Branches"
    )
    default_activity: Optional[str] = Field(default=None, alias="DefaultActivity")
    evaluation_wait_time: Optional[WaitTimeModel] = Field(
        default=None, alias="EvaluationWaitTime"
    )


class CampaignResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    creation_date: str = Field(alias="CreationDate")
    id: str = Field(alias="Id")
    last_modified_date: str = Field(alias="LastModifiedDate")
    segment_id: str = Field(alias="SegmentId")
    segment_version: int = Field(alias="SegmentVersion")
    additional_treatments: Optional[List[TreatmentResourceModel]] = Field(
        default=None, alias="AdditionalTreatments"
    )
    custom_delivery_configuration: Optional[CustomDeliveryConfigurationModel] = Field(
        default=None, alias="CustomDeliveryConfiguration"
    )
    default_state: Optional[CampaignStateModel] = Field(
        default=None, alias="DefaultState"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    holdout_percent: Optional[int] = Field(default=None, alias="HoldoutPercent")
    hook: Optional[CampaignHookModel] = Field(default=None, alias="Hook")
    is_paused: Optional[bool] = Field(default=None, alias="IsPaused")
    limits: Optional[CampaignLimitsModel] = Field(default=None, alias="Limits")
    message_configuration: Optional[MessageConfigurationModel] = Field(
        default=None, alias="MessageConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    schedule: Optional[ScheduleModel] = Field(default=None, alias="Schedule")
    state: Optional[CampaignStateModel] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    treatment_description: Optional[str] = Field(
        default=None, alias="TreatmentDescription"
    )
    treatment_name: Optional[str] = Field(default=None, alias="TreatmentName")
    version: Optional[int] = Field(default=None, alias="Version")
    priority: Optional[int] = Field(default=None, alias="Priority")


class WriteCampaignRequestModel(BaseModel):
    additional_treatments: Optional[Sequence[WriteTreatmentResourceModel]] = Field(
        default=None, alias="AdditionalTreatments"
    )
    custom_delivery_configuration: Optional[CustomDeliveryConfigurationModel] = Field(
        default=None, alias="CustomDeliveryConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    holdout_percent: Optional[int] = Field(default=None, alias="HoldoutPercent")
    hook: Optional[CampaignHookModel] = Field(default=None, alias="Hook")
    is_paused: Optional[bool] = Field(default=None, alias="IsPaused")
    limits: Optional[CampaignLimitsModel] = Field(default=None, alias="Limits")
    message_configuration: Optional[MessageConfigurationModel] = Field(
        default=None, alias="MessageConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    schedule: Optional[ScheduleModel] = Field(default=None, alias="Schedule")
    segment_id: Optional[str] = Field(default=None, alias="SegmentId")
    segment_version: Optional[int] = Field(default=None, alias="SegmentVersion")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )
    treatment_description: Optional[str] = Field(
        default=None, alias="TreatmentDescription"
    )
    treatment_name: Optional[str] = Field(default=None, alias="TreatmentName")
    priority: Optional[int] = Field(default=None, alias="Priority")


class GetInAppMessagesResponseModel(BaseModel):
    in_app_messages_response: InAppMessagesResponseModel = Field(
        alias="InAppMessagesResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSegmentResponseModel(BaseModel):
    segment_response: SegmentResponseModel = Field(alias="SegmentResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSegmentResponseModel(BaseModel):
    segment_response: SegmentResponseModel = Field(alias="SegmentResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentResponseModel(BaseModel):
    segment_response: SegmentResponseModel = Field(alias="SegmentResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentVersionResponseModel(BaseModel):
    segment_response: SegmentResponseModel = Field(alias="SegmentResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SegmentsResponseModel(BaseModel):
    item: List[SegmentResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateSegmentResponseModel(BaseModel):
    segment_response: SegmentResponseModel = Field(alias="SegmentResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSegmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    write_segment_request: WriteSegmentRequestModel = Field(alias="WriteSegmentRequest")


class UpdateSegmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    segment_id: str = Field(alias="SegmentId")
    write_segment_request: WriteSegmentRequestModel = Field(alias="WriteSegmentRequest")


class ActivityModel(BaseModel):
    cus_tom: Optional[CustomMessageActivityModel] = Field(default=None, alias="CUSTOM")
    conditional_split: Optional[ConditionalSplitActivityModel] = Field(
        default=None, alias="ConditionalSplit"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    email: Optional[EmailMessageActivityModel] = Field(default=None, alias="EMAIL")
    holdout: Optional[HoldoutActivityModel] = Field(default=None, alias="Holdout")
    multi_condition: Optional[MultiConditionalSplitActivityModel] = Field(
        default=None, alias="MultiCondition"
    )
    p_us_h: Optional[PushMessageActivityModel] = Field(default=None, alias="PUSH")
    random_split: Optional[RandomSplitActivityModel] = Field(
        default=None, alias="RandomSplit"
    )
    s_ms: Optional[SMSMessageActivityModel] = Field(default=None, alias="SMS")
    wait: Optional[WaitActivityModel] = Field(default=None, alias="Wait")
    contact_center: Optional[ContactCenterActivityModel] = Field(
        default=None, alias="ContactCenter"
    )


class CampaignsResponseModel(BaseModel):
    item: List[CampaignResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateCampaignResponseModel(BaseModel):
    campaign_response: CampaignResponseModel = Field(alias="CampaignResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCampaignResponseModel(BaseModel):
    campaign_response: CampaignResponseModel = Field(alias="CampaignResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCampaignResponseModel(BaseModel):
    campaign_response: CampaignResponseModel = Field(alias="CampaignResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCampaignVersionResponseModel(BaseModel):
    campaign_response: CampaignResponseModel = Field(alias="CampaignResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCampaignResponseModel(BaseModel):
    campaign_response: CampaignResponseModel = Field(alias="CampaignResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCampaignRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    write_campaign_request: WriteCampaignRequestModel = Field(
        alias="WriteCampaignRequest"
    )


class UpdateCampaignRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    campaign_id: str = Field(alias="CampaignId")
    write_campaign_request: WriteCampaignRequestModel = Field(
        alias="WriteCampaignRequest"
    )


class GetSegmentVersionsResponseModel(BaseModel):
    segments_response: SegmentsResponseModel = Field(alias="SegmentsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentsResponseModel(BaseModel):
    segments_response: SegmentsResponseModel = Field(alias="SegmentsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JourneyResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    activities: Optional[Dict[str, ActivityModel]] = Field(
        default=None, alias="Activities"
    )
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    limits: Optional[JourneyLimitsModel] = Field(default=None, alias="Limits")
    local_time: Optional[bool] = Field(default=None, alias="LocalTime")
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")
    refresh_frequency: Optional[str] = Field(default=None, alias="RefreshFrequency")
    schedule: Optional[JourneyScheduleModel] = Field(default=None, alias="Schedule")
    start_activity: Optional[str] = Field(default=None, alias="StartActivity")
    start_condition: Optional[StartConditionModel] = Field(
        default=None, alias="StartCondition"
    )
    state: Optional[
        Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    wait_for_quiet_time: Optional[bool] = Field(default=None, alias="WaitForQuietTime")
    refresh_on_segment_update: Optional[bool] = Field(
        default=None, alias="RefreshOnSegmentUpdate"
    )
    journey_channel_settings: Optional[JourneyChannelSettingsModel] = Field(
        default=None, alias="JourneyChannelSettings"
    )
    sending_schedule: Optional[bool] = Field(default=None, alias="SendingSchedule")
    open_hours: Optional[OpenHoursModel] = Field(default=None, alias="OpenHours")
    closed_days: Optional[ClosedDaysModel] = Field(default=None, alias="ClosedDays")


class WriteJourneyRequestModel(BaseModel):
    name: str = Field(alias="Name")
    activities: Optional[Mapping[str, ActivityModel]] = Field(
        default=None, alias="Activities"
    )
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    limits: Optional[JourneyLimitsModel] = Field(default=None, alias="Limits")
    local_time: Optional[bool] = Field(default=None, alias="LocalTime")
    quiet_time: Optional[QuietTimeModel] = Field(default=None, alias="QuietTime")
    refresh_frequency: Optional[str] = Field(default=None, alias="RefreshFrequency")
    schedule: Optional[JourneyScheduleModel] = Field(default=None, alias="Schedule")
    start_activity: Optional[str] = Field(default=None, alias="StartActivity")
    start_condition: Optional[StartConditionModel] = Field(
        default=None, alias="StartCondition"
    )
    state: Optional[
        Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
    ] = Field(default=None, alias="State")
    wait_for_quiet_time: Optional[bool] = Field(default=None, alias="WaitForQuietTime")
    refresh_on_segment_update: Optional[bool] = Field(
        default=None, alias="RefreshOnSegmentUpdate"
    )
    journey_channel_settings: Optional[JourneyChannelSettingsModel] = Field(
        default=None, alias="JourneyChannelSettings"
    )
    sending_schedule: Optional[bool] = Field(default=None, alias="SendingSchedule")
    open_hours: Optional[OpenHoursModel] = Field(default=None, alias="OpenHours")
    closed_days: Optional[ClosedDaysModel] = Field(default=None, alias="ClosedDays")


class GetCampaignVersionsResponseModel(BaseModel):
    campaigns_response: CampaignsResponseModel = Field(alias="CampaignsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCampaignsResponseModel(BaseModel):
    campaigns_response: CampaignsResponseModel = Field(alias="CampaignsResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJourneyResponseModel(BaseModel):
    journey_response: JourneyResponseModel = Field(alias="JourneyResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteJourneyResponseModel(BaseModel):
    journey_response: JourneyResponseModel = Field(alias="JourneyResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJourneyResponseModel(BaseModel):
    journey_response: JourneyResponseModel = Field(alias="JourneyResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JourneysResponseModel(BaseModel):
    item: List[JourneyResponseModel] = Field(alias="Item")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateJourneyResponseModel(BaseModel):
    journey_response: JourneyResponseModel = Field(alias="JourneyResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJourneyStateResponseModel(BaseModel):
    journey_response: JourneyResponseModel = Field(alias="JourneyResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJourneyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    write_journey_request: WriteJourneyRequestModel = Field(alias="WriteJourneyRequest")


class UpdateJourneyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    journey_id: str = Field(alias="JourneyId")
    write_journey_request: WriteJourneyRequestModel = Field(alias="WriteJourneyRequest")


class ListJourneysResponseModel(BaseModel):
    journeys_response: JourneysResponseModel = Field(alias="JourneysResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
