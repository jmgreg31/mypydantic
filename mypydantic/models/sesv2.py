# Model Generated: Thu Mar  2 21:56:23 2023

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


class ReviewDetailsModel(BaseModel):
    status: Optional[Literal["DENIED", "FAILED", "GRANTED", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    case_id: Optional[str] = Field(default=None, alias="CaseId")


class BatchGetMetricDataQueryModel(BaseModel):
    id: str = Field(alias="Id")
    namespace: Literal["VDM"] = Field(alias="Namespace")
    metric: Literal[
        "CLICK",
        "COMPLAINT",
        "DELIVERY",
        "DELIVERY_CLICK",
        "DELIVERY_COMPLAINT",
        "DELIVERY_OPEN",
        "OPEN",
        "PERMANENT_BOUNCE",
        "SEND",
        "TRANSIENT_BOUNCE",
    ] = Field(alias="Metric")
    start_date: Union[datetime, str] = Field(alias="StartDate")
    end_date: Union[datetime, str] = Field(alias="EndDate")
    dimensions: Optional[
        Mapping[Literal["CONFIGURATION_SET", "EMAIL_IDENTITY", "ISP"], str]
    ] = Field(default=None, alias="Dimensions")


class MetricDataErrorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    code: Optional[Literal["ACCESS_DENIED", "INTERNAL_FAILURE"]] = Field(
        default=None, alias="Code"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class MetricDataResultModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    timestamps: Optional[List[datetime]] = Field(default=None, alias="Timestamps")
    values: Optional[List[int]] = Field(default=None, alias="Values")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BlacklistEntryModel(BaseModel):
    rbl_name: Optional[str] = Field(default=None, alias="RblName")
    listing_time: Optional[datetime] = Field(default=None, alias="ListingTime")
    description: Optional[str] = Field(default=None, alias="Description")


class ContentModel(BaseModel):
    data: str = Field(alias="Data")
    charset: Optional[str] = Field(default=None, alias="Charset")


class TemplateModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    template_arn: Optional[str] = Field(default=None, alias="TemplateArn")
    template_data: Optional[str] = Field(default=None, alias="TemplateData")


class BulkEmailEntryResultModel(BaseModel):
    status: Optional[
        Literal[
            "ACCOUNT_DAILY_QUOTA_EXCEEDED",
            "ACCOUNT_SENDING_PAUSED",
            "ACCOUNT_SUSPENDED",
            "ACCOUNT_THROTTLED",
            "CONFIGURATION_SET_NOT_FOUND",
            "CONFIGURATION_SET_SENDING_PAUSED",
            "FAILED",
            "INVALID_PARAMETER",
            "INVALID_SENDING_POOL_NAME",
            "MAIL_FROM_DOMAIN_NOT_VERIFIED",
            "MESSAGE_REJECTED",
            "SUCCESS",
            "TEMPLATE_NOT_FOUND",
            "TRANSIENT_FAILURE",
        ]
    ] = Field(default=None, alias="Status")
    error: Optional[str] = Field(default=None, alias="Error")
    message_id: Optional[str] = Field(default=None, alias="MessageId")


class DestinationModel(BaseModel):
    to_addresses: Optional[Sequence[str]] = Field(default=None, alias="ToAddresses")
    cc_addresses: Optional[Sequence[str]] = Field(default=None, alias="CcAddresses")
    bcc_addresses: Optional[Sequence[str]] = Field(default=None, alias="BccAddresses")


class MessageTagModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class CloudWatchDimensionConfigurationModel(BaseModel):
    dimension_name: str = Field(alias="DimensionName")
    dimension_value_source: Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"] = Field(
        alias="DimensionValueSource"
    )
    default_dimension_value: str = Field(alias="DefaultDimensionValue")


class ContactListDestinationModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    contact_list_import_action: Literal["DELETE", "PUT"] = Field(
        alias="ContactListImportAction"
    )


class ContactListModel(BaseModel):
    contact_list_name: Optional[str] = Field(default=None, alias="ContactListName")
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class TopicPreferenceModel(BaseModel):
    topic_name: str = Field(alias="TopicName")
    subscription_status: Literal["OPT_IN", "OPT_OUT"] = Field(
        alias="SubscriptionStatus"
    )


class DeliveryOptionsModel(BaseModel):
    tls_policy: Optional[Literal["OPTIONAL", "REQUIRE"]] = Field(
        default=None, alias="TlsPolicy"
    )
    sending_pool_name: Optional[str] = Field(default=None, alias="SendingPoolName")


class ReputationOptionsModel(BaseModel):
    reputation_metrics_enabled: Optional[bool] = Field(
        default=None, alias="ReputationMetricsEnabled"
    )
    last_fresh_start: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastFreshStart"
    )


class SendingOptionsModel(BaseModel):
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")


class SuppressionOptionsModel(BaseModel):
    suppressed_reasons: Optional[Sequence[Literal["BOUNCE", "COMPLAINT"]]] = Field(
        default=None, alias="SuppressedReasons"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class TrackingOptionsModel(BaseModel):
    custom_redirect_domain: str = Field(alias="CustomRedirectDomain")


class TopicModel(BaseModel):
    topic_name: str = Field(alias="TopicName")
    display_name: str = Field(alias="DisplayName")
    default_subscription_status: Literal["OPT_IN", "OPT_OUT"] = Field(
        alias="DefaultSubscriptionStatus"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: str = Field(alias="FromEmailAddress")
    template_subject: str = Field(alias="TemplateSubject")
    template_content: str = Field(alias="TemplateContent")
    success_redirection_url: str = Field(alias="SuccessRedirectionURL")
    failure_redirection_url: str = Field(alias="FailureRedirectionURL")


class CreateEmailIdentityPolicyRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    policy_name: str = Field(alias="PolicyName")
    policy: str = Field(alias="Policy")


class DkimSigningAttributesModel(BaseModel):
    domain_signing_selector: Optional[str] = Field(
        default=None, alias="DomainSigningSelector"
    )
    domain_signing_private_key: Optional[str] = Field(
        default=None, alias="DomainSigningPrivateKey"
    )
    next_signing_key_length: Optional[Literal["RSA_1024_BIT", "RSA_2048_BIT"]] = Field(
        default=None, alias="NextSigningKeyLength"
    )


class DkimAttributesModel(BaseModel):
    signing_enabled: Optional[bool] = Field(default=None, alias="SigningEnabled")
    status: Optional[
        Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
    ] = Field(default=None, alias="Status")
    tokens: Optional[List[str]] = Field(default=None, alias="Tokens")
    signing_attributes_origin: Optional[Literal["AWS_SES", "EXTERNAL"]] = Field(
        default=None, alias="SigningAttributesOrigin"
    )
    next_signing_key_length: Optional[Literal["RSA_1024_BIT", "RSA_2048_BIT"]] = Field(
        default=None, alias="NextSigningKeyLength"
    )
    current_signing_key_length: Optional[
        Literal["RSA_1024_BIT", "RSA_2048_BIT"]
    ] = Field(default=None, alias="CurrentSigningKeyLength")
    last_key_generation_timestamp: Optional[datetime] = Field(
        default=None, alias="LastKeyGenerationTimestamp"
    )


class EmailTemplateContentModel(BaseModel):
    subject: Optional[str] = Field(default=None, alias="Subject")
    text: Optional[str] = Field(default=None, alias="Text")
    html: Optional[str] = Field(default=None, alias="Html")


class ImportDataSourceModel(BaseModel):
    s3_url: str = Field(alias="S3Url")
    data_format: Literal["CSV", "JSON"] = Field(alias="DataFormat")


class CustomVerificationEmailTemplateMetadataModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    template_subject: Optional[str] = Field(default=None, alias="TemplateSubject")
    success_redirection_url: Optional[str] = Field(
        default=None, alias="SuccessRedirectionURL"
    )
    failure_redirection_url: Optional[str] = Field(
        default=None, alias="FailureRedirectionURL"
    )


class DomainIspPlacementModel(BaseModel):
    isp_name: Optional[str] = Field(default=None, alias="IspName")
    inbox_raw_count: Optional[int] = Field(default=None, alias="InboxRawCount")
    spam_raw_count: Optional[int] = Field(default=None, alias="SpamRawCount")
    inbox_percentage: Optional[float] = Field(default=None, alias="InboxPercentage")
    spam_percentage: Optional[float] = Field(default=None, alias="SpamPercentage")


class VolumeStatisticsModel(BaseModel):
    inbox_raw_count: Optional[int] = Field(default=None, alias="InboxRawCount")
    spam_raw_count: Optional[int] = Field(default=None, alias="SpamRawCount")
    projected_inbox: Optional[int] = Field(default=None, alias="ProjectedInbox")
    projected_spam: Optional[int] = Field(default=None, alias="ProjectedSpam")


class DashboardAttributesModel(BaseModel):
    engagement_metrics: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="EngagementMetrics"
    )


class DashboardOptionsModel(BaseModel):
    engagement_metrics: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="EngagementMetrics"
    )


class DedicatedIpPoolModel(BaseModel):
    pool_name: str = Field(alias="PoolName")
    scaling_mode: Literal["MANAGED", "STANDARD"] = Field(alias="ScalingMode")


class DedicatedIpModel(BaseModel):
    ip: str = Field(alias="Ip")
    warmup_status: Literal["DONE", "IN_PROGRESS"] = Field(alias="WarmupStatus")
    warmup_percentage: int = Field(alias="WarmupPercentage")
    pool_name: Optional[str] = Field(default=None, alias="PoolName")


class DeleteConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")


class DeleteConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteContactListRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")


class DeleteContactRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    email_address: str = Field(alias="EmailAddress")


class DeleteCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class DeleteDedicatedIpPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")


class DeleteEmailIdentityPolicyRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    policy_name: str = Field(alias="PolicyName")


class DeleteEmailIdentityRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")


class DeleteEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class DeleteSuppressedDestinationRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")


class DeliverabilityTestReportModel(BaseModel):
    report_id: Optional[str] = Field(default=None, alias="ReportId")
    report_name: Optional[str] = Field(default=None, alias="ReportName")
    subject: Optional[str] = Field(default=None, alias="Subject")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    deliverability_test_status: Optional[Literal["COMPLETED", "IN_PROGRESS"]] = Field(
        default=None, alias="DeliverabilityTestStatus"
    )


class DomainDeliverabilityCampaignModel(BaseModel):
    campaign_id: Optional[str] = Field(default=None, alias="CampaignId")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    subject: Optional[str] = Field(default=None, alias="Subject")
    from_address: Optional[str] = Field(default=None, alias="FromAddress")
    sending_ips: Optional[List[str]] = Field(default=None, alias="SendingIps")
    first_seen_date_time: Optional[datetime] = Field(
        default=None, alias="FirstSeenDateTime"
    )
    last_seen_date_time: Optional[datetime] = Field(
        default=None, alias="LastSeenDateTime"
    )
    inbox_count: Optional[int] = Field(default=None, alias="InboxCount")
    spam_count: Optional[int] = Field(default=None, alias="SpamCount")
    read_rate: Optional[float] = Field(default=None, alias="ReadRate")
    delete_rate: Optional[float] = Field(default=None, alias="DeleteRate")
    read_delete_rate: Optional[float] = Field(default=None, alias="ReadDeleteRate")
    projected_volume: Optional[int] = Field(default=None, alias="ProjectedVolume")
    esps: Optional[List[str]] = Field(default=None, alias="Esps")


class InboxPlacementTrackingOptionModel(BaseModel):
    global_: Optional[bool] = Field(default=None, alias="Global")
    tracked_isps: Optional[List[str]] = Field(default=None, alias="TrackedIsps")


class RawMessageModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")


class EmailTemplateMetadataModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )


class KinesisFirehoseDestinationModel(BaseModel):
    iam_role_arn: str = Field(alias="IamRoleArn")
    delivery_stream_arn: str = Field(alias="DeliveryStreamArn")


class PinpointDestinationModel(BaseModel):
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")


class SnsDestinationModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class FailureInfoModel(BaseModel):
    failed_records_s3_url: Optional[str] = Field(
        default=None, alias="FailedRecordsS3Url"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class SendQuotaModel(BaseModel):
    max24_hour_send: Optional[float] = Field(default=None, alias="Max24HourSend")
    max_send_rate: Optional[float] = Field(default=None, alias="MaxSendRate")
    sent_last24_hours: Optional[float] = Field(default=None, alias="SentLast24Hours")


class SuppressionAttributesModel(BaseModel):
    suppressed_reasons: Optional[List[Literal["BOUNCE", "COMPLAINT"]]] = Field(
        default=None, alias="SuppressedReasons"
    )


class GetBlacklistReportsRequestModel(BaseModel):
    blacklist_item_names: Sequence[str] = Field(alias="BlacklistItemNames")


class GetConfigurationSetEventDestinationsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class GetConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class GetContactListRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")


class GetContactRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    email_address: str = Field(alias="EmailAddress")


class GetCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class GetDedicatedIpPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")


class GetDedicatedIpRequestModel(BaseModel):
    ip: str = Field(alias="Ip")


class GetDedicatedIpsRequestModel(BaseModel):
    pool_name: Optional[str] = Field(default=None, alias="PoolName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class GetDeliverabilityTestReportRequestModel(BaseModel):
    report_id: str = Field(alias="ReportId")


class PlacementStatisticsModel(BaseModel):
    inbox_percentage: Optional[float] = Field(default=None, alias="InboxPercentage")
    spam_percentage: Optional[float] = Field(default=None, alias="SpamPercentage")
    missing_percentage: Optional[float] = Field(default=None, alias="MissingPercentage")
    spf_percentage: Optional[float] = Field(default=None, alias="SpfPercentage")
    dkim_percentage: Optional[float] = Field(default=None, alias="DkimPercentage")


class GetDomainDeliverabilityCampaignRequestModel(BaseModel):
    campaign_id: str = Field(alias="CampaignId")


class GetDomainStatisticsReportRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    start_date: Union[datetime, str] = Field(alias="StartDate")
    end_date: Union[datetime, str] = Field(alias="EndDate")


class GetEmailIdentityPoliciesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")


class GetEmailIdentityRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")


class MailFromAttributesModel(BaseModel):
    mail_from_domain: str = Field(alias="MailFromDomain")
    mail_from_domain_status: Literal[
        "FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"
    ] = Field(alias="MailFromDomainStatus")
    behavior_on_mx_failure: Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"] = Field(
        alias="BehaviorOnMxFailure"
    )


class GetEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class GetImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class GetSuppressedDestinationRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")


class GuardianAttributesModel(BaseModel):
    optimized_shared_delivery: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptimizedSharedDelivery"
    )


class GuardianOptionsModel(BaseModel):
    optimized_shared_delivery: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptimizedSharedDelivery"
    )


class IdentityInfoModel(BaseModel):
    identity_type: Optional[
        Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
    ] = Field(default=None, alias="IdentityType")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")
    verification_status: Optional[
        Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
    ] = Field(default=None, alias="VerificationStatus")


class SuppressionListDestinationModel(BaseModel):
    suppression_list_import_action: Literal["DELETE", "PUT"] = Field(
        alias="SuppressionListImportAction"
    )


class ListConfigurationSetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListContactListsRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TopicFilterModel(BaseModel):
    topic_name: Optional[str] = Field(default=None, alias="TopicName")
    use_default_if_preference_unavailable: Optional[bool] = Field(
        default=None, alias="UseDefaultIfPreferenceUnavailable"
    )


class ListCustomVerificationEmailTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListDedicatedIpPoolsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListDeliverabilityTestReportsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListDomainDeliverabilityCampaignsRequestModel(BaseModel):
    start_date: Union[datetime, str] = Field(alias="StartDate")
    end_date: Union[datetime, str] = Field(alias="EndDate")
    subscribed_domain: str = Field(alias="SubscribedDomain")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListEmailIdentitiesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListEmailTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListImportJobsRequestModel(BaseModel):
    import_destination_type: Optional[
        Literal["CONTACT_LIST", "SUPPRESSION_LIST"]
    ] = Field(default=None, alias="ImportDestinationType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListManagementOptionsModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    topic_name: Optional[str] = Field(default=None, alias="TopicName")


class ListRecommendationsRequestModel(BaseModel):
    filter: Optional[
        Mapping[Literal["IMPACT", "RESOURCE_ARN", "STATUS", "TYPE"], str]
    ] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class RecommendationModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    type: Optional[Literal["DKIM", "DMARC", "SPF"]] = Field(default=None, alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["FIXED", "OPEN"]] = Field(default=None, alias="Status")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    impact: Optional[Literal["HIGH", "LOW"]] = Field(default=None, alias="Impact")


class ListSuppressedDestinationsRequestModel(BaseModel):
    reasons: Optional[Sequence[Literal["BOUNCE", "COMPLAINT"]]] = Field(
        default=None, alias="Reasons"
    )
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class SuppressedDestinationSummaryModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    reason: Literal["BOUNCE", "COMPLAINT"] = Field(alias="Reason")
    last_update_time: datetime = Field(alias="LastUpdateTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PutAccountDedicatedIpWarmupAttributesRequestModel(BaseModel):
    auto_warmup_enabled: Optional[bool] = Field(default=None, alias="AutoWarmupEnabled")


class PutAccountDetailsRequestModel(BaseModel):
    mail_type: Literal["MARKETING", "TRANSACTIONAL"] = Field(alias="MailType")
    website_url: str = Field(alias="WebsiteURL")
    use_case_description: str = Field(alias="UseCaseDescription")
    contact_language: Optional[Literal["EN", "JA"]] = Field(
        default=None, alias="ContactLanguage"
    )
    additional_contact_email_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalContactEmailAddresses"
    )
    production_access_enabled: Optional[bool] = Field(
        default=None, alias="ProductionAccessEnabled"
    )


class PutAccountSendingAttributesRequestModel(BaseModel):
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")


class PutAccountSuppressionAttributesRequestModel(BaseModel):
    suppressed_reasons: Optional[Sequence[Literal["BOUNCE", "COMPLAINT"]]] = Field(
        default=None, alias="SuppressedReasons"
    )


class PutConfigurationSetDeliveryOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tls_policy: Optional[Literal["OPTIONAL", "REQUIRE"]] = Field(
        default=None, alias="TlsPolicy"
    )
    sending_pool_name: Optional[str] = Field(default=None, alias="SendingPoolName")


class PutConfigurationSetReputationOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    reputation_metrics_enabled: Optional[bool] = Field(
        default=None, alias="ReputationMetricsEnabled"
    )


class PutConfigurationSetSendingOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")


class PutConfigurationSetSuppressionOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    suppressed_reasons: Optional[Sequence[Literal["BOUNCE", "COMPLAINT"]]] = Field(
        default=None, alias="SuppressedReasons"
    )


class PutConfigurationSetTrackingOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    custom_redirect_domain: Optional[str] = Field(
        default=None, alias="CustomRedirectDomain"
    )


class PutDedicatedIpInPoolRequestModel(BaseModel):
    ip: str = Field(alias="Ip")
    destination_pool_name: str = Field(alias="DestinationPoolName")


class PutDedicatedIpWarmupAttributesRequestModel(BaseModel):
    ip: str = Field(alias="Ip")
    warmup_percentage: int = Field(alias="WarmupPercentage")


class PutEmailIdentityConfigurationSetAttributesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class PutEmailIdentityDkimAttributesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    signing_enabled: Optional[bool] = Field(default=None, alias="SigningEnabled")


class PutEmailIdentityFeedbackAttributesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    email_forwarding_enabled: Optional[bool] = Field(
        default=None, alias="EmailForwardingEnabled"
    )


class PutEmailIdentityMailFromAttributesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    mail_from_domain: Optional[str] = Field(default=None, alias="MailFromDomain")
    behavior_on_mx_failure: Optional[
        Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
    ] = Field(default=None, alias="BehaviorOnMxFailure")


class PutSuppressedDestinationRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    reason: Literal["BOUNCE", "COMPLAINT"] = Field(alias="Reason")


class ReplacementTemplateModel(BaseModel):
    replacement_template_data: Optional[str] = Field(
        default=None, alias="ReplacementTemplateData"
    )


class SendCustomVerificationEmailRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    template_name: str = Field(alias="TemplateName")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class SuppressedDestinationAttributesModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    feedback_id: Optional[str] = Field(default=None, alias="FeedbackId")


class TestRenderEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_data: str = Field(alias="TemplateData")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: str = Field(alias="FromEmailAddress")
    template_subject: str = Field(alias="TemplateSubject")
    template_content: str = Field(alias="TemplateContent")
    success_redirection_url: str = Field(alias="SuccessRedirectionURL")
    failure_redirection_url: str = Field(alias="FailureRedirectionURL")


class UpdateEmailIdentityPolicyRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    policy_name: str = Field(alias="PolicyName")
    policy: str = Field(alias="Policy")


class AccountDetailsModel(BaseModel):
    mail_type: Optional[Literal["MARKETING", "TRANSACTIONAL"]] = Field(
        default=None, alias="MailType"
    )
    website_url: Optional[str] = Field(default=None, alias="WebsiteURL")
    contact_language: Optional[Literal["EN", "JA"]] = Field(
        default=None, alias="ContactLanguage"
    )
    use_case_description: Optional[str] = Field(
        default=None, alias="UseCaseDescription"
    )
    additional_contact_email_addresses: Optional[List[str]] = Field(
        default=None, alias="AdditionalContactEmailAddresses"
    )
    review_details: Optional[ReviewDetailsModel] = Field(
        default=None, alias="ReviewDetails"
    )


class BatchGetMetricDataRequestModel(BaseModel):
    queries: Sequence[BatchGetMetricDataQueryModel] = Field(alias="Queries")


class BatchGetMetricDataResponseModel(BaseModel):
    results: List[MetricDataResultModel] = Field(alias="Results")
    errors: List[MetricDataErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeliverabilityTestReportResponseModel(BaseModel):
    report_id: str = Field(alias="ReportId")
    deliverability_test_status: Literal["COMPLETED", "IN_PROGRESS"] = Field(
        alias="DeliverabilityTestStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCustomVerificationEmailTemplateResponseModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: str = Field(alias="FromEmailAddress")
    template_subject: str = Field(alias="TemplateSubject")
    template_content: str = Field(alias="TemplateContent")
    success_redirection_url: str = Field(alias="SuccessRedirectionURL")
    failure_redirection_url: str = Field(alias="FailureRedirectionURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEmailIdentityPoliciesResponseModel(BaseModel):
    policies: Dict[str, str] = Field(alias="Policies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationSetsResponseModel(BaseModel):
    configuration_sets: List[str] = Field(alias="ConfigurationSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDedicatedIpPoolsResponseModel(BaseModel):
    dedicated_ip_pools: List[str] = Field(alias="DedicatedIpPools")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEmailIdentityDkimSigningAttributesResponseModel(BaseModel):
    dkim_status: Literal[
        "FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"
    ] = Field(alias="DkimStatus")
    dkim_tokens: List[str] = Field(alias="DkimTokens")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendCustomVerificationEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestRenderEmailTemplateResponseModel(BaseModel):
    rendered_template: str = Field(alias="RenderedTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlacklistReportsResponseModel(BaseModel):
    blacklist_report: Dict[str, List[BlacklistEntryModel]] = Field(
        alias="BlacklistReport"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BodyModel(BaseModel):
    text: Optional[ContentModel] = Field(default=None, alias="Text")
    html: Optional[ContentModel] = Field(default=None, alias="Html")


class BulkEmailContentModel(BaseModel):
    template: Optional[TemplateModel] = Field(default=None, alias="Template")


class SendBulkEmailResponseModel(BaseModel):
    bulk_email_entry_results: List[BulkEmailEntryResultModel] = Field(
        alias="BulkEmailEntryResults"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloudWatchDestinationModel(BaseModel):
    dimension_configurations: Sequence[CloudWatchDimensionConfigurationModel] = Field(
        alias="DimensionConfigurations"
    )


class ListContactListsResponseModel(BaseModel):
    contact_lists: List[ContactListModel] = Field(alias="ContactLists")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContactModel(BaseModel):
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    topic_preferences: Optional[List[TopicPreferenceModel]] = Field(
        default=None, alias="TopicPreferences"
    )
    topic_default_preferences: Optional[List[TopicPreferenceModel]] = Field(
        default=None, alias="TopicDefaultPreferences"
    )
    unsubscribe_all: Optional[bool] = Field(default=None, alias="UnsubscribeAll")
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class CreateContactRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    email_address: str = Field(alias="EmailAddress")
    topic_preferences: Optional[Sequence[TopicPreferenceModel]] = Field(
        default=None, alias="TopicPreferences"
    )
    unsubscribe_all: Optional[bool] = Field(default=None, alias="UnsubscribeAll")
    attributes_data: Optional[str] = Field(default=None, alias="AttributesData")


class GetContactResponseModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    email_address: str = Field(alias="EmailAddress")
    topic_preferences: List[TopicPreferenceModel] = Field(alias="TopicPreferences")
    topic_default_preferences: List[TopicPreferenceModel] = Field(
        alias="TopicDefaultPreferences"
    )
    unsubscribe_all: bool = Field(alias="UnsubscribeAll")
    attributes_data: str = Field(alias="AttributesData")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    last_updated_timestamp: datetime = Field(alias="LastUpdatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContactRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    email_address: str = Field(alias="EmailAddress")
    topic_preferences: Optional[Sequence[TopicPreferenceModel]] = Field(
        default=None, alias="TopicPreferences"
    )
    unsubscribe_all: Optional[bool] = Field(default=None, alias="UnsubscribeAll")
    attributes_data: Optional[str] = Field(default=None, alias="AttributesData")


class CreateDedicatedIpPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    scaling_mode: Optional[Literal["MANAGED", "STANDARD"]] = Field(
        default=None, alias="ScalingMode"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateContactListRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    topics: Optional[Sequence[TopicModel]] = Field(default=None, alias="Topics")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetContactListResponseModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    topics: List[TopicModel] = Field(alias="Topics")
    description: str = Field(alias="Description")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    last_updated_timestamp: datetime = Field(alias="LastUpdatedTimestamp")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContactListRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    topics: Optional[Sequence[TopicModel]] = Field(default=None, alias="Topics")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateEmailIdentityRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dkim_signing_attributes: Optional[DkimSigningAttributesModel] = Field(
        default=None, alias="DkimSigningAttributes"
    )
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class PutEmailIdentityDkimSigningAttributesRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    signing_attributes_origin: Literal["AWS_SES", "EXTERNAL"] = Field(
        alias="SigningAttributesOrigin"
    )
    signing_attributes: Optional[DkimSigningAttributesModel] = Field(
        default=None, alias="SigningAttributes"
    )


class CreateEmailIdentityResponseModel(BaseModel):
    identity_type: Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"] = Field(
        alias="IdentityType"
    )
    verified_for_sending_status: bool = Field(alias="VerifiedForSendingStatus")
    dkim_attributes: DkimAttributesModel = Field(alias="DkimAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_content: EmailTemplateContentModel = Field(alias="TemplateContent")


class GetEmailTemplateResponseModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_content: EmailTemplateContentModel = Field(alias="TemplateContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_content: EmailTemplateContentModel = Field(alias="TemplateContent")


class ListCustomVerificationEmailTemplatesResponseModel(BaseModel):
    custom_verification_email_templates: List[
        CustomVerificationEmailTemplateMetadataModel
    ] = Field(alias="CustomVerificationEmailTemplates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DailyVolumeModel(BaseModel):
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    volume_statistics: Optional[VolumeStatisticsModel] = Field(
        default=None, alias="VolumeStatistics"
    )
    domain_isp_placements: Optional[List[DomainIspPlacementModel]] = Field(
        default=None, alias="DomainIspPlacements"
    )


class OverallVolumeModel(BaseModel):
    volume_statistics: Optional[VolumeStatisticsModel] = Field(
        default=None, alias="VolumeStatistics"
    )
    read_rate_percent: Optional[float] = Field(default=None, alias="ReadRatePercent")
    domain_isp_placements: Optional[List[DomainIspPlacementModel]] = Field(
        default=None, alias="DomainIspPlacements"
    )


class GetDedicatedIpPoolResponseModel(BaseModel):
    dedicated_ip_pool: DedicatedIpPoolModel = Field(alias="DedicatedIpPool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDedicatedIpResponseModel(BaseModel):
    dedicated_ip: DedicatedIpModel = Field(alias="DedicatedIp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDedicatedIpsResponseModel(BaseModel):
    dedicated_ips: List[DedicatedIpModel] = Field(alias="DedicatedIps")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeliverabilityTestReportsResponseModel(BaseModel):
    deliverability_test_reports: List[DeliverabilityTestReportModel] = Field(
        alias="DeliverabilityTestReports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainDeliverabilityCampaignResponseModel(BaseModel):
    domain_deliverability_campaign: DomainDeliverabilityCampaignModel = Field(
        alias="DomainDeliverabilityCampaign"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainDeliverabilityCampaignsResponseModel(BaseModel):
    domain_deliverability_campaigns: List[DomainDeliverabilityCampaignModel] = Field(
        alias="DomainDeliverabilityCampaigns"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainDeliverabilityTrackingOptionModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    subscription_start_date: Optional[datetime] = Field(
        default=None, alias="SubscriptionStartDate"
    )
    inbox_placement_tracking_option: Optional[
        InboxPlacementTrackingOptionModel
    ] = Field(default=None, alias="InboxPlacementTrackingOption")


class ListEmailTemplatesResponseModel(BaseModel):
    templates_metadata: List[EmailTemplateMetadataModel] = Field(
        alias="TemplatesMetadata"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IspPlacementModel(BaseModel):
    isp_name: Optional[str] = Field(default=None, alias="IspName")
    placement_statistics: Optional[PlacementStatisticsModel] = Field(
        default=None, alias="PlacementStatistics"
    )


class GetEmailIdentityResponseModel(BaseModel):
    identity_type: Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"] = Field(
        alias="IdentityType"
    )
    feedback_forwarding_status: bool = Field(alias="FeedbackForwardingStatus")
    verified_for_sending_status: bool = Field(alias="VerifiedForSendingStatus")
    dkim_attributes: DkimAttributesModel = Field(alias="DkimAttributes")
    mail_from_attributes: MailFromAttributesModel = Field(alias="MailFromAttributes")
    policies: Dict[str, str] = Field(alias="Policies")
    tags: List[TagModel] = Field(alias="Tags")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    verification_status: Literal[
        "FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"
    ] = Field(alias="VerificationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VdmAttributesModel(BaseModel):
    vdm_enabled: Literal["DISABLED", "ENABLED"] = Field(alias="VdmEnabled")
    dashboard_attributes: Optional[DashboardAttributesModel] = Field(
        default=None, alias="DashboardAttributes"
    )
    guardian_attributes: Optional[GuardianAttributesModel] = Field(
        default=None, alias="GuardianAttributes"
    )


class VdmOptionsModel(BaseModel):
    dashboard_options: Optional[DashboardOptionsModel] = Field(
        default=None, alias="DashboardOptions"
    )
    guardian_options: Optional[GuardianOptionsModel] = Field(
        default=None, alias="GuardianOptions"
    )


class ListEmailIdentitiesResponseModel(BaseModel):
    email_identities: List[IdentityInfoModel] = Field(alias="EmailIdentities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportDestinationModel(BaseModel):
    suppression_list_destination: Optional[SuppressionListDestinationModel] = Field(
        default=None, alias="SuppressionListDestination"
    )
    contact_list_destination: Optional[ContactListDestinationModel] = Field(
        default=None, alias="ContactListDestination"
    )


class ListContactsFilterModel(BaseModel):
    filtered_status: Optional[Literal["OPT_IN", "OPT_OUT"]] = Field(
        default=None, alias="FilteredStatus"
    )
    topic_filter: Optional[TopicFilterModel] = Field(default=None, alias="TopicFilter")


class ListRecommendationsResponseModel(BaseModel):
    recommendations: List[RecommendationModel] = Field(alias="Recommendations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSuppressedDestinationsResponseModel(BaseModel):
    suppressed_destination_summaries: List[SuppressedDestinationSummaryModel] = Field(
        alias="SuppressedDestinationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplacementEmailContentModel(BaseModel):
    replacement_template: Optional[ReplacementTemplateModel] = Field(
        default=None, alias="ReplacementTemplate"
    )


class SuppressedDestinationModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    reason: Literal["BOUNCE", "COMPLAINT"] = Field(alias="Reason")
    last_update_time: datetime = Field(alias="LastUpdateTime")
    attributes: Optional[SuppressedDestinationAttributesModel] = Field(
        default=None, alias="Attributes"
    )


class MessageModel(BaseModel):
    subject: ContentModel = Field(alias="Subject")
    body: BodyModel = Field(alias="Body")


class EventDestinationDefinitionModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    matching_event_types: Optional[
        Sequence[
            Literal[
                "BOUNCE",
                "CLICK",
                "COMPLAINT",
                "DELIVERY",
                "DELIVERY_DELAY",
                "OPEN",
                "REJECT",
                "RENDERING_FAILURE",
                "SEND",
                "SUBSCRIPTION",
            ]
        ]
    ] = Field(default=None, alias="MatchingEventTypes")
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    cloud_watch_destination: Optional[CloudWatchDestinationModel] = Field(
        default=None, alias="CloudWatchDestination"
    )
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )
    pinpoint_destination: Optional[PinpointDestinationModel] = Field(
        default=None, alias="PinpointDestination"
    )


class EventDestinationModel(BaseModel):
    name: str = Field(alias="Name")
    matching_event_types: List[
        Literal[
            "BOUNCE",
            "CLICK",
            "COMPLAINT",
            "DELIVERY",
            "DELIVERY_DELAY",
            "OPEN",
            "REJECT",
            "RENDERING_FAILURE",
            "SEND",
            "SUBSCRIPTION",
        ]
    ] = Field(alias="MatchingEventTypes")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    cloud_watch_destination: Optional[CloudWatchDestinationModel] = Field(
        default=None, alias="CloudWatchDestination"
    )
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )
    pinpoint_destination: Optional[PinpointDestinationModel] = Field(
        default=None, alias="PinpointDestination"
    )


class ListContactsResponseModel(BaseModel):
    contacts: List[ContactModel] = Field(alias="Contacts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainStatisticsReportResponseModel(BaseModel):
    overall_volume: OverallVolumeModel = Field(alias="OverallVolume")
    daily_volumes: List[DailyVolumeModel] = Field(alias="DailyVolumes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeliverabilityDashboardOptionsResponseModel(BaseModel):
    dashboard_enabled: bool = Field(alias="DashboardEnabled")
    subscription_expiry_date: datetime = Field(alias="SubscriptionExpiryDate")
    account_status: Literal["ACTIVE", "DISABLED", "PENDING_EXPIRATION"] = Field(
        alias="AccountStatus"
    )
    active_subscribed_domains: List[DomainDeliverabilityTrackingOptionModel] = Field(
        alias="ActiveSubscribedDomains"
    )
    pending_expiration_subscribed_domains: List[
        DomainDeliverabilityTrackingOptionModel
    ] = Field(alias="PendingExpirationSubscribedDomains")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDeliverabilityDashboardOptionRequestModel(BaseModel):
    dashboard_enabled: bool = Field(alias="DashboardEnabled")
    subscribed_domains: Optional[
        Sequence[DomainDeliverabilityTrackingOptionModel]
    ] = Field(default=None, alias="SubscribedDomains")


class GetDeliverabilityTestReportResponseModel(BaseModel):
    deliverability_test_report: DeliverabilityTestReportModel = Field(
        alias="DeliverabilityTestReport"
    )
    overall_placement: PlacementStatisticsModel = Field(alias="OverallPlacement")
    isp_placements: List[IspPlacementModel] = Field(alias="IspPlacements")
    message: str = Field(alias="Message")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountResponseModel(BaseModel):
    dedicated_ip_auto_warmup_enabled: bool = Field(alias="DedicatedIpAutoWarmupEnabled")
    enforcement_status: str = Field(alias="EnforcementStatus")
    production_access_enabled: bool = Field(alias="ProductionAccessEnabled")
    send_quota: SendQuotaModel = Field(alias="SendQuota")
    sending_enabled: bool = Field(alias="SendingEnabled")
    suppression_attributes: SuppressionAttributesModel = Field(
        alias="SuppressionAttributes"
    )
    details: AccountDetailsModel = Field(alias="Details")
    vdm_attributes: VdmAttributesModel = Field(alias="VdmAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccountVdmAttributesRequestModel(BaseModel):
    vdm_attributes: VdmAttributesModel = Field(alias="VdmAttributes")


class CreateConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tracking_options: Optional[TrackingOptionsModel] = Field(
        default=None, alias="TrackingOptions"
    )
    delivery_options: Optional[DeliveryOptionsModel] = Field(
        default=None, alias="DeliveryOptions"
    )
    reputation_options: Optional[ReputationOptionsModel] = Field(
        default=None, alias="ReputationOptions"
    )
    sending_options: Optional[SendingOptionsModel] = Field(
        default=None, alias="SendingOptions"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    suppression_options: Optional[SuppressionOptionsModel] = Field(
        default=None, alias="SuppressionOptions"
    )
    vdm_options: Optional[VdmOptionsModel] = Field(default=None, alias="VdmOptions")


class GetConfigurationSetResponseModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tracking_options: TrackingOptionsModel = Field(alias="TrackingOptions")
    delivery_options: DeliveryOptionsModel = Field(alias="DeliveryOptions")
    reputation_options: ReputationOptionsModel = Field(alias="ReputationOptions")
    sending_options: SendingOptionsModel = Field(alias="SendingOptions")
    tags: List[TagModel] = Field(alias="Tags")
    suppression_options: SuppressionOptionsModel = Field(alias="SuppressionOptions")
    vdm_options: VdmOptionsModel = Field(alias="VdmOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConfigurationSetVdmOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    vdm_options: Optional[VdmOptionsModel] = Field(default=None, alias="VdmOptions")


class CreateImportJobRequestModel(BaseModel):
    import_destination: ImportDestinationModel = Field(alias="ImportDestination")
    import_data_source: ImportDataSourceModel = Field(alias="ImportDataSource")


class GetImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    import_destination: ImportDestinationModel = Field(alias="ImportDestination")
    import_data_source: ImportDataSourceModel = Field(alias="ImportDataSource")
    failure_info: FailureInfoModel = Field(alias="FailureInfo")
    job_status: Literal["COMPLETED", "CREATED", "FAILED", "PROCESSING"] = Field(
        alias="JobStatus"
    )
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    completed_timestamp: datetime = Field(alias="CompletedTimestamp")
    processed_records_count: int = Field(alias="ProcessedRecordsCount")
    failed_records_count: int = Field(alias="FailedRecordsCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportJobSummaryModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    import_destination: Optional[ImportDestinationModel] = Field(
        default=None, alias="ImportDestination"
    )
    job_status: Optional[
        Literal["COMPLETED", "CREATED", "FAILED", "PROCESSING"]
    ] = Field(default=None, alias="JobStatus")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    processed_records_count: Optional[int] = Field(
        default=None, alias="ProcessedRecordsCount"
    )
    failed_records_count: Optional[int] = Field(
        default=None, alias="FailedRecordsCount"
    )


class ListContactsRequestModel(BaseModel):
    contact_list_name: str = Field(alias="ContactListName")
    filter: Optional[ListContactsFilterModel] = Field(default=None, alias="Filter")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BulkEmailEntryModel(BaseModel):
    destination: DestinationModel = Field(alias="Destination")
    replacement_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="ReplacementTags"
    )
    replacement_email_content: Optional[ReplacementEmailContentModel] = Field(
        default=None, alias="ReplacementEmailContent"
    )


class GetSuppressedDestinationResponseModel(BaseModel):
    suppressed_destination: SuppressedDestinationModel = Field(
        alias="SuppressedDestination"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmailContentModel(BaseModel):
    simple: Optional[MessageModel] = Field(default=None, alias="Simple")
    raw: Optional[RawMessageModel] = Field(default=None, alias="Raw")
    template: Optional[TemplateModel] = Field(default=None, alias="Template")


class CreateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")
    event_destination: EventDestinationDefinitionModel = Field(alias="EventDestination")


class UpdateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")
    event_destination: EventDestinationDefinitionModel = Field(alias="EventDestination")


class GetConfigurationSetEventDestinationsResponseModel(BaseModel):
    event_destinations: List[EventDestinationModel] = Field(alias="EventDestinations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImportJobsResponseModel(BaseModel):
    import_jobs: List[ImportJobSummaryModel] = Field(alias="ImportJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendBulkEmailRequestModel(BaseModel):
    default_content: BulkEmailContentModel = Field(alias="DefaultContent")
    bulk_email_entries: Sequence[BulkEmailEntryModel] = Field(alias="BulkEmailEntries")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    from_email_address_identity_arn: Optional[str] = Field(
        default=None, alias="FromEmailAddressIdentityArn"
    )
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    feedback_forwarding_email_address: Optional[str] = Field(
        default=None, alias="FeedbackForwardingEmailAddress"
    )
    feedback_forwarding_email_address_identity_arn: Optional[str] = Field(
        default=None, alias="FeedbackForwardingEmailAddressIdentityArn"
    )
    default_email_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="DefaultEmailTags"
    )
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class CreateDeliverabilityTestReportRequestModel(BaseModel):
    from_email_address: str = Field(alias="FromEmailAddress")
    content: EmailContentModel = Field(alias="Content")
    report_name: Optional[str] = Field(default=None, alias="ReportName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class SendEmailRequestModel(BaseModel):
    content: EmailContentModel = Field(alias="Content")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    from_email_address_identity_arn: Optional[str] = Field(
        default=None, alias="FromEmailAddressIdentityArn"
    )
    destination: Optional[DestinationModel] = Field(default=None, alias="Destination")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    feedback_forwarding_email_address: Optional[str] = Field(
        default=None, alias="FeedbackForwardingEmailAddress"
    )
    feedback_forwarding_email_address_identity_arn: Optional[str] = Field(
        default=None, alias="FeedbackForwardingEmailAddressIdentityArn"
    )
    email_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="EmailTags"
    )
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    list_management_options: Optional[ListManagementOptionsModel] = Field(
        default=None, alias="ListManagementOptions"
    )
