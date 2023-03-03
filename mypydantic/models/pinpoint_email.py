# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BlacklistEntryModel(BaseModel):
    rbl_name: Optional[str] = Field(default=None, alias="RblName")
    listing_time: Optional[datetime] = Field(default=None, alias="ListingTime")
    description: Optional[str] = Field(default=None, alias="Description")


class ContentModel(BaseModel):
    data: str = Field(alias="Data")
    charset: Optional[str] = Field(default=None, alias="Charset")


class CloudWatchDimensionConfigurationModel(BaseModel):
    dimension_name: str = Field(alias="DimensionName")
    dimension_value_source: Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"] = Field(
        alias="DimensionValueSource"
    )
    default_dimension_value: str = Field(alias="DefaultDimensionValue")


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


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class TrackingOptionsModel(BaseModel):
    custom_redirect_domain: str = Field(alias="CustomRedirectDomain")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DkimAttributesModel(BaseModel):
    signing_enabled: Optional[bool] = Field(default=None, alias="SigningEnabled")
    status: Optional[
        Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
    ] = Field(default=None, alias="Status")
    tokens: Optional[List[str]] = Field(default=None, alias="Tokens")


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


class DeleteDedicatedIpPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")


class DeleteEmailIdentityRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")


class DeliverabilityTestReportModel(BaseModel):
    report_id: Optional[str] = Field(default=None, alias="ReportId")
    report_name: Optional[str] = Field(default=None, alias="ReportName")
    subject: Optional[str] = Field(default=None, alias="Subject")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    deliverability_test_status: Optional[Literal["COMPLETED", "IN_PROGRESS"]] = Field(
        default=None, alias="DeliverabilityTestStatus"
    )


class DestinationModel(BaseModel):
    to_addresses: Optional[Sequence[str]] = Field(default=None, alias="ToAddresses")
    cc_addresses: Optional[Sequence[str]] = Field(default=None, alias="CcAddresses")
    bcc_addresses: Optional[Sequence[str]] = Field(default=None, alias="BccAddresses")


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


class TemplateModel(BaseModel):
    template_arn: Optional[str] = Field(default=None, alias="TemplateArn")
    template_data: Optional[str] = Field(default=None, alias="TemplateData")


class KinesisFirehoseDestinationModel(BaseModel):
    iam_role_arn: str = Field(alias="IamRoleArn")
    delivery_stream_arn: str = Field(alias="DeliveryStreamArn")


class PinpointDestinationModel(BaseModel):
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")


class SnsDestinationModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class SendQuotaModel(BaseModel):
    max24_hour_send: Optional[float] = Field(default=None, alias="Max24HourSend")
    max_send_rate: Optional[float] = Field(default=None, alias="MaxSendRate")
    sent_last24_hours: Optional[float] = Field(default=None, alias="SentLast24Hours")


class GetBlacklistReportsRequestModel(BaseModel):
    blacklist_item_names: Sequence[str] = Field(alias="BlacklistItemNames")


class GetConfigurationSetEventDestinationsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class GetConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class GetDedicatedIpRequestModel(BaseModel):
    ip: str = Field(alias="Ip")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


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


class IdentityInfoModel(BaseModel):
    identity_type: Optional[
        Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
    ] = Field(default=None, alias="IdentityType")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")


class ListConfigurationSetsRequestModel(BaseModel):
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


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class MessageTagModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class PutAccountDedicatedIpWarmupAttributesRequestModel(BaseModel):
    auto_warmup_enabled: Optional[bool] = Field(default=None, alias="AutoWarmupEnabled")


class PutAccountSendingAttributesRequestModel(BaseModel):
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")


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


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class BodyModel(BaseModel):
    text: Optional[ContentModel] = Field(default=None, alias="Text")
    html: Optional[ContentModel] = Field(default=None, alias="Html")


class CloudWatchDestinationModel(BaseModel):
    dimension_configurations: Sequence[CloudWatchDimensionConfigurationModel] = Field(
        alias="DimensionConfigurations"
    )


class CreateDedicatedIpPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateEmailIdentityRequestModel(BaseModel):
    email_identity: str = Field(alias="EmailIdentity")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


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


class CreateDeliverabilityTestReportResponseModel(BaseModel):
    report_id: str = Field(alias="ReportId")
    deliverability_test_status: Literal["COMPLETED", "IN_PROGRESS"] = Field(
        alias="DeliverabilityTestStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlacklistReportsResponseModel(BaseModel):
    blacklist_report: Dict[str, List[BlacklistEntryModel]] = Field(
        alias="BlacklistReport"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConfigurationSetResponseModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tracking_options: TrackingOptionsModel = Field(alias="TrackingOptions")
    delivery_options: DeliveryOptionsModel = Field(alias="DeliveryOptions")
    reputation_options: ReputationOptionsModel = Field(alias="ReputationOptions")
    sending_options: SendingOptionsModel = Field(alias="SendingOptions")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationSetsResponseModel(BaseModel):
    configuration_sets: List[str] = Field(alias="ConfigurationSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDedicatedIpPoolsResponseModel(BaseModel):
    dedicated_ip_pools: List[str] = Field(alias="DedicatedIpPools")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEmailIdentityResponseModel(BaseModel):
    identity_type: Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"] = Field(
        alias="IdentityType"
    )
    verified_for_sending_status: bool = Field(alias="VerifiedForSendingStatus")
    dkim_attributes: DkimAttributesModel = Field(alias="DkimAttributes")
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


class GetAccountResponseModel(BaseModel):
    send_quota: SendQuotaModel = Field(alias="SendQuota")
    sending_enabled: bool = Field(alias="SendingEnabled")
    dedicated_ip_auto_warmup_enabled: bool = Field(alias="DedicatedIpAutoWarmupEnabled")
    enforcement_status: str = Field(alias="EnforcementStatus")
    production_access_enabled: bool = Field(alias="ProductionAccessEnabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDedicatedIpsRequestGetDedicatedIpsPaginateModel(BaseModel):
    pool_name: Optional[str] = Field(default=None, alias="PoolName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfigurationSetsRequestListConfigurationSetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEmailIdentitiesRequestListEmailIdentitiesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


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
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEmailIdentitiesResponseModel(BaseModel):
    email_identities: List[IdentityInfoModel] = Field(alias="EmailIdentities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
                "OPEN",
                "REJECT",
                "RENDERING_FAILURE",
                "SEND",
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
            "OPEN",
            "REJECT",
            "RENDERING_FAILURE",
            "SEND",
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


class CreateDeliverabilityTestReportRequestModel(BaseModel):
    from_email_address: str = Field(alias="FromEmailAddress")
    content: EmailContentModel = Field(alias="Content")
    report_name: Optional[str] = Field(default=None, alias="ReportName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class SendEmailRequestModel(BaseModel):
    destination: DestinationModel = Field(alias="Destination")
    content: EmailContentModel = Field(alias="Content")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    feedback_forwarding_email_address: Optional[str] = Field(
        default=None, alias="FeedbackForwardingEmailAddress"
    )
    email_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="EmailTags"
    )
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
