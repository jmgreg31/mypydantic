# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddHeaderActionModel(BaseModel):
    header_name: str = Field(alias="HeaderName")
    header_value: str = Field(alias="HeaderValue")


class ContentModel(BaseModel):
    data: str = Field(alias="Data")
    charset: Optional[str] = Field(default=None, alias="Charset")


class BounceActionModel(BaseModel):
    smtp_reply_code: str = Field(alias="SmtpReplyCode")
    message: str = Field(alias="Message")
    sender: str = Field(alias="Sender")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    status_code: Optional[str] = Field(default=None, alias="StatusCode")


class BulkEmailDestinationStatusModel(BaseModel):
    status: Optional[
        Literal[
            "AccountDailyQuotaExceeded",
            "AccountSendingPaused",
            "AccountSuspended",
            "AccountThrottled",
            "ConfigurationSetDoesNotExist",
            "ConfigurationSetSendingPaused",
            "Failed",
            "InvalidParameterValue",
            "InvalidSendingPoolName",
            "MailFromDomainNotVerified",
            "MessageRejected",
            "Success",
            "TemplateDoesNotExist",
            "TransientFailure",
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


class CloneReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    original_rule_set_name: str = Field(alias="OriginalRuleSetName")


class CloudWatchDimensionConfigurationModel(BaseModel):
    dimension_name: str = Field(alias="DimensionName")
    dimension_value_source: Literal["emailHeader", "linkTag", "messageTag"] = Field(
        alias="DimensionValueSource"
    )
    default_dimension_value: str = Field(alias="DefaultDimensionValue")


class ConfigurationSetModel(BaseModel):
    name: str = Field(alias="Name")


class TrackingOptionsModel(BaseModel):
    custom_redirect_domain: Optional[str] = Field(
        default=None, alias="CustomRedirectDomain"
    )


class CreateCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: str = Field(alias="FromEmailAddress")
    template_subject: str = Field(alias="TemplateSubject")
    template_content: str = Field(alias="TemplateContent")
    success_redirection_url: str = Field(alias="SuccessRedirectionURL")
    failure_redirection_url: str = Field(alias="FailureRedirectionURL")


class CreateReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")


class TemplateModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    subject_part: Optional[str] = Field(default=None, alias="SubjectPart")
    text_part: Optional[str] = Field(default=None, alias="TextPart")
    html_part: Optional[str] = Field(default=None, alias="HtmlPart")


class CustomVerificationEmailTemplateModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    template_subject: Optional[str] = Field(default=None, alias="TemplateSubject")
    success_redirection_url: Optional[str] = Field(
        default=None, alias="SuccessRedirectionURL"
    )
    failure_redirection_url: Optional[str] = Field(
        default=None, alias="FailureRedirectionURL"
    )


class DeleteConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")


class DeleteConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteConfigurationSetTrackingOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class DeleteIdentityPolicyRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    policy_name: str = Field(alias="PolicyName")


class DeleteIdentityRequestModel(BaseModel):
    identity: str = Field(alias="Identity")


class DeleteReceiptFilterRequestModel(BaseModel):
    filter_name: str = Field(alias="FilterName")


class DeleteReceiptRuleRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule_name: str = Field(alias="RuleName")


class DeleteReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")


class DeleteTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class DeleteVerifiedEmailAddressRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")


class DeliveryOptionsModel(BaseModel):
    tls_policy: Optional[Literal["Optional", "Require"]] = Field(
        default=None, alias="TlsPolicy"
    )


class ReceiptRuleSetMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    configuration_set_attribute_names: Optional[
        Sequence[
            Literal[
                "deliveryOptions",
                "eventDestinations",
                "reputationOptions",
                "trackingOptions",
            ]
        ]
    ] = Field(default=None, alias="ConfigurationSetAttributeNames")


class ReputationOptionsModel(BaseModel):
    sending_enabled: Optional[bool] = Field(default=None, alias="SendingEnabled")
    reputation_metrics_enabled: Optional[bool] = Field(
        default=None, alias="ReputationMetricsEnabled"
    )
    last_fresh_start: Optional[datetime] = Field(default=None, alias="LastFreshStart")


class DescribeReceiptRuleRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule_name: str = Field(alias="RuleName")


class DescribeReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")


class KinesisFirehoseDestinationModel(BaseModel):
    iamrole_arn: str = Field(alias="IAMRoleARN")
    delivery_stream_arn: str = Field(alias="DeliveryStreamARN")


class SNSDestinationModel(BaseModel):
    topic_arn: str = Field(alias="TopicARN")


class ExtensionFieldModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class GetCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class GetIdentityDkimAttributesRequestModel(BaseModel):
    identities: Sequence[str] = Field(alias="Identities")


class IdentityDkimAttributesModel(BaseModel):
    dkim_enabled: bool = Field(alias="DkimEnabled")
    dkim_verification_status: Literal[
        "Failed", "NotStarted", "Pending", "Success", "TemporaryFailure"
    ] = Field(alias="DkimVerificationStatus")
    dkim_tokens: Optional[List[str]] = Field(default=None, alias="DkimTokens")


class GetIdentityMailFromDomainAttributesRequestModel(BaseModel):
    identities: Sequence[str] = Field(alias="Identities")


class IdentityMailFromDomainAttributesModel(BaseModel):
    mail_from_domain: str = Field(alias="MailFromDomain")
    mail_from_domain_status: Literal[
        "Failed", "Pending", "Success", "TemporaryFailure"
    ] = Field(alias="MailFromDomainStatus")
    behavior_on_mxfailure: Literal["RejectMessage", "UseDefaultValue"] = Field(
        alias="BehaviorOnMXFailure"
    )


class GetIdentityNotificationAttributesRequestModel(BaseModel):
    identities: Sequence[str] = Field(alias="Identities")


class IdentityNotificationAttributesModel(BaseModel):
    bounce_topic: str = Field(alias="BounceTopic")
    complaint_topic: str = Field(alias="ComplaintTopic")
    delivery_topic: str = Field(alias="DeliveryTopic")
    forwarding_enabled: bool = Field(alias="ForwardingEnabled")
    headers_in_bounce_notifications_enabled: Optional[bool] = Field(
        default=None, alias="HeadersInBounceNotificationsEnabled"
    )
    headers_in_complaint_notifications_enabled: Optional[bool] = Field(
        default=None, alias="HeadersInComplaintNotificationsEnabled"
    )
    headers_in_delivery_notifications_enabled: Optional[bool] = Field(
        default=None, alias="HeadersInDeliveryNotificationsEnabled"
    )


class GetIdentityPoliciesRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    policy_names: Sequence[str] = Field(alias="PolicyNames")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetIdentityVerificationAttributesRequestModel(BaseModel):
    identities: Sequence[str] = Field(alias="Identities")


class IdentityVerificationAttributesModel(BaseModel):
    verification_status: Literal[
        "Failed", "NotStarted", "Pending", "Success", "TemporaryFailure"
    ] = Field(alias="VerificationStatus")
    verification_token: Optional[str] = Field(default=None, alias="VerificationToken")


class SendDataPointModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    delivery_attempts: Optional[int] = Field(default=None, alias="DeliveryAttempts")
    bounces: Optional[int] = Field(default=None, alias="Bounces")
    complaints: Optional[int] = Field(default=None, alias="Complaints")
    rejects: Optional[int] = Field(default=None, alias="Rejects")


class GetTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")


class LambdaActionModel(BaseModel):
    function_arn: str = Field(alias="FunctionArn")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    invocation_type: Optional[Literal["Event", "RequestResponse"]] = Field(
        default=None, alias="InvocationType"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListConfigurationSetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListCustomVerificationEmailTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIdentitiesRequestModel(BaseModel):
    identity_type: Optional[Literal["Domain", "EmailAddress"]] = Field(
        default=None, alias="IdentityType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListIdentityPoliciesRequestModel(BaseModel):
    identity: str = Field(alias="Identity")


class ListReceiptRuleSetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class TemplateMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )


class PutIdentityPolicyRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    policy_name: str = Field(alias="PolicyName")
    policy: str = Field(alias="Policy")


class RawMessageModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")


class S3ActionModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    object_key_prefix: Optional[str] = Field(default=None, alias="ObjectKeyPrefix")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class SNSActionModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    encoding: Optional[Literal["Base64", "UTF-8"]] = Field(
        default=None, alias="Encoding"
    )


class StopActionModel(BaseModel):
    scope: Literal["RuleSet"] = Field(alias="Scope")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class WorkmailActionModel(BaseModel):
    organization_arn: str = Field(alias="OrganizationArn")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class ReceiptIpFilterModel(BaseModel):
    policy: Literal["Allow", "Block"] = Field(alias="Policy")
    cidr: str = Field(alias="Cidr")


class ReorderReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule_names: Sequence[str] = Field(alias="RuleNames")


class SendCustomVerificationEmailRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    template_name: str = Field(alias="TemplateName")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class SetActiveReceiptRuleSetRequestModel(BaseModel):
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")


class SetIdentityDkimEnabledRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    dkim_enabled: bool = Field(alias="DkimEnabled")


class SetIdentityFeedbackForwardingEnabledRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    forwarding_enabled: bool = Field(alias="ForwardingEnabled")


class SetIdentityHeadersInNotificationsEnabledRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    notification_type: Literal["Bounce", "Complaint", "Delivery"] = Field(
        alias="NotificationType"
    )
    enabled: bool = Field(alias="Enabled")


class SetIdentityMailFromDomainRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    mail_from_domain: Optional[str] = Field(default=None, alias="MailFromDomain")
    behavior_on_mxfailure: Optional[
        Literal["RejectMessage", "UseDefaultValue"]
    ] = Field(default=None, alias="BehaviorOnMXFailure")


class SetIdentityNotificationTopicRequestModel(BaseModel):
    identity: str = Field(alias="Identity")
    notification_type: Literal["Bounce", "Complaint", "Delivery"] = Field(
        alias="NotificationType"
    )
    sns_topic: Optional[str] = Field(default=None, alias="SnsTopic")


class SetReceiptRulePositionRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule_name: str = Field(alias="RuleName")
    after: Optional[str] = Field(default=None, alias="After")


class TestRenderTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    template_data: str = Field(alias="TemplateData")


class UpdateAccountSendingEnabledRequestModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdateConfigurationSetReputationMetricsEnabledRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    enabled: bool = Field(alias="Enabled")


class UpdateConfigurationSetSendingEnabledRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    enabled: bool = Field(alias="Enabled")


class UpdateCustomVerificationEmailTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: Optional[str] = Field(default=None, alias="FromEmailAddress")
    template_subject: Optional[str] = Field(default=None, alias="TemplateSubject")
    template_content: Optional[str] = Field(default=None, alias="TemplateContent")
    success_redirection_url: Optional[str] = Field(
        default=None, alias="SuccessRedirectionURL"
    )
    failure_redirection_url: Optional[str] = Field(
        default=None, alias="FailureRedirectionURL"
    )


class VerifyDomainDkimRequestModel(BaseModel):
    domain: str = Field(alias="Domain")


class VerifyDomainIdentityRequestModel(BaseModel):
    domain: str = Field(alias="Domain")


class VerifyEmailAddressRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")


class VerifyEmailIdentityRequestModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")


class BodyModel(BaseModel):
    text: Optional[ContentModel] = Field(default=None, alias="Text")
    html: Optional[ContentModel] = Field(default=None, alias="Html")


class BulkEmailDestinationModel(BaseModel):
    destination: DestinationModel = Field(alias="Destination")
    replacement_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="ReplacementTags"
    )
    replacement_template_data: Optional[str] = Field(
        default=None, alias="ReplacementTemplateData"
    )


class SendTemplatedEmailRequestModel(BaseModel):
    source: str = Field(alias="Source")
    destination: DestinationModel = Field(alias="Destination")
    template: str = Field(alias="Template")
    template_data: str = Field(alias="TemplateData")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    return_path: Optional[str] = Field(default=None, alias="ReturnPath")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    return_path_arn: Optional[str] = Field(default=None, alias="ReturnPathArn")
    tags: Optional[Sequence[MessageTagModel]] = Field(default=None, alias="Tags")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    template_arn: Optional[str] = Field(default=None, alias="TemplateArn")


class CloudWatchDestinationModel(BaseModel):
    dimension_configurations: Sequence[CloudWatchDimensionConfigurationModel] = Field(
        alias="DimensionConfigurations"
    )


class CreateConfigurationSetRequestModel(BaseModel):
    configuration_set: ConfigurationSetModel = Field(alias="ConfigurationSet")


class CreateConfigurationSetTrackingOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tracking_options: TrackingOptionsModel = Field(alias="TrackingOptions")


class UpdateConfigurationSetTrackingOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tracking_options: TrackingOptionsModel = Field(alias="TrackingOptions")


class CreateTemplateRequestModel(BaseModel):
    template: TemplateModel = Field(alias="Template")


class UpdateTemplateRequestModel(BaseModel):
    template: TemplateModel = Field(alias="Template")


class PutConfigurationSetDeliveryOptionsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    delivery_options: Optional[DeliveryOptionsModel] = Field(
        default=None, alias="DeliveryOptions"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSendingEnabledResponseModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCustomVerificationEmailTemplateResponseModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    from_email_address: str = Field(alias="FromEmailAddress")
    template_subject: str = Field(alias="TemplateSubject")
    template_content: str = Field(alias="TemplateContent")
    success_redirection_url: str = Field(alias="SuccessRedirectionURL")
    failure_redirection_url: str = Field(alias="FailureRedirectionURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityPoliciesResponseModel(BaseModel):
    policies: Dict[str, str] = Field(alias="Policies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSendQuotaResponseModel(BaseModel):
    max24_hour_send: float = Field(alias="Max24HourSend")
    max_send_rate: float = Field(alias="MaxSendRate")
    sent_last24_hours: float = Field(alias="SentLast24Hours")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateResponseModel(BaseModel):
    template: TemplateModel = Field(alias="Template")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationSetsResponseModel(BaseModel):
    configuration_sets: List[ConfigurationSetModel] = Field(alias="ConfigurationSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomVerificationEmailTemplatesResponseModel(BaseModel):
    custom_verification_email_templates: List[
        CustomVerificationEmailTemplateModel
    ] = Field(alias="CustomVerificationEmailTemplates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentitiesResponseModel(BaseModel):
    identities: List[str] = Field(alias="Identities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityPoliciesResponseModel(BaseModel):
    policy_names: List[str] = Field(alias="PolicyNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReceiptRuleSetsResponseModel(BaseModel):
    rule_sets: List[ReceiptRuleSetMetadataModel] = Field(alias="RuleSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVerifiedEmailAddressesResponseModel(BaseModel):
    verified_email_addresses: List[str] = Field(alias="VerifiedEmailAddresses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendBounceResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendBulkTemplatedEmailResponseModel(BaseModel):
    status: List[BulkEmailDestinationStatusModel] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendCustomVerificationEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendRawEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendTemplatedEmailResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestRenderTemplateResponseModel(BaseModel):
    rendered_template: str = Field(alias="RenderedTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyDomainDkimResponseModel(BaseModel):
    dkim_tokens: List[str] = Field(alias="DkimTokens")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyDomainIdentityResponseModel(BaseModel):
    verification_token: str = Field(alias="VerificationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MessageDsnModel(BaseModel):
    reporting_mta: str = Field(alias="ReportingMta")
    arrival_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ArrivalDate"
    )
    extension_fields: Optional[Sequence[ExtensionFieldModel]] = Field(
        default=None, alias="ExtensionFields"
    )


class RecipientDsnFieldsModel(BaseModel):
    action: Literal["delayed", "delivered", "expanded", "failed", "relayed"] = Field(
        alias="Action"
    )
    status: str = Field(alias="Status")
    final_recipient: Optional[str] = Field(default=None, alias="FinalRecipient")
    remote_mta: Optional[str] = Field(default=None, alias="RemoteMta")
    diagnostic_code: Optional[str] = Field(default=None, alias="DiagnosticCode")
    last_attempt_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAttemptDate"
    )
    extension_fields: Optional[Sequence[ExtensionFieldModel]] = Field(
        default=None, alias="ExtensionFields"
    )


class GetIdentityDkimAttributesResponseModel(BaseModel):
    dkim_attributes: Dict[str, IdentityDkimAttributesModel] = Field(
        alias="DkimAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityMailFromDomainAttributesResponseModel(BaseModel):
    mail_from_domain_attributes: Dict[
        str, IdentityMailFromDomainAttributesModel
    ] = Field(alias="MailFromDomainAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityNotificationAttributesResponseModel(BaseModel):
    notification_attributes: Dict[str, IdentityNotificationAttributesModel] = Field(
        alias="NotificationAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityVerificationAttributesRequestIdentityExistsWaitModel(BaseModel):
    identities: Sequence[str] = Field(alias="Identities")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetIdentityVerificationAttributesResponseModel(BaseModel):
    verification_attributes: Dict[str, IdentityVerificationAttributesModel] = Field(
        alias="VerificationAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSendStatisticsResponseModel(BaseModel):
    send_data_points: List[SendDataPointModel] = Field(alias="SendDataPoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationSetsRequestListConfigurationSetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIdentitiesRequestListIdentitiesPaginateModel(BaseModel):
    identity_type: Optional[Literal["Domain", "EmailAddress"]] = Field(
        default=None, alias="IdentityType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplatesRequestListTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplatesResponseModel(BaseModel):
    templates_metadata: List[TemplateMetadataModel] = Field(alias="TemplatesMetadata")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendRawEmailRequestModel(BaseModel):
    raw_message: RawMessageModel = Field(alias="RawMessage")
    source: Optional[str] = Field(default=None, alias="Source")
    destinations: Optional[Sequence[str]] = Field(default=None, alias="Destinations")
    from_arn: Optional[str] = Field(default=None, alias="FromArn")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    return_path_arn: Optional[str] = Field(default=None, alias="ReturnPathArn")
    tags: Optional[Sequence[MessageTagModel]] = Field(default=None, alias="Tags")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class ReceiptActionModel(BaseModel):
    s3_action: Optional[S3ActionModel] = Field(default=None, alias="S3Action")
    bounce_action: Optional[BounceActionModel] = Field(
        default=None, alias="BounceAction"
    )
    workmail_action: Optional[WorkmailActionModel] = Field(
        default=None, alias="WorkmailAction"
    )
    lambda_action: Optional[LambdaActionModel] = Field(
        default=None, alias="LambdaAction"
    )
    stop_action: Optional[StopActionModel] = Field(default=None, alias="StopAction")
    add_header_action: Optional[AddHeaderActionModel] = Field(
        default=None, alias="AddHeaderAction"
    )
    s_ns_action: Optional[SNSActionModel] = Field(default=None, alias="SNSAction")


class ReceiptFilterModel(BaseModel):
    name: str = Field(alias="Name")
    ip_filter: ReceiptIpFilterModel = Field(alias="IpFilter")


class MessageModel(BaseModel):
    subject: ContentModel = Field(alias="Subject")
    body: BodyModel = Field(alias="Body")


class SendBulkTemplatedEmailRequestModel(BaseModel):
    source: str = Field(alias="Source")
    template: str = Field(alias="Template")
    destinations: Sequence[BulkEmailDestinationModel] = Field(alias="Destinations")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    return_path: Optional[str] = Field(default=None, alias="ReturnPath")
    return_path_arn: Optional[str] = Field(default=None, alias="ReturnPathArn")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    default_tags: Optional[Sequence[MessageTagModel]] = Field(
        default=None, alias="DefaultTags"
    )
    template_arn: Optional[str] = Field(default=None, alias="TemplateArn")
    default_template_data: Optional[str] = Field(
        default=None, alias="DefaultTemplateData"
    )


class EventDestinationModel(BaseModel):
    name: str = Field(alias="Name")
    matching_event_types: Sequence[
        Literal[
            "bounce",
            "click",
            "complaint",
            "delivery",
            "open",
            "reject",
            "renderingFailure",
            "send",
        ]
    ] = Field(alias="MatchingEventTypes")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    cloud_watch_destination: Optional[CloudWatchDestinationModel] = Field(
        default=None, alias="CloudWatchDestination"
    )
    s_ns_destination: Optional[SNSDestinationModel] = Field(
        default=None, alias="SNSDestination"
    )


class BouncedRecipientInfoModel(BaseModel):
    recipient: str = Field(alias="Recipient")
    recipient_arn: Optional[str] = Field(default=None, alias="RecipientArn")
    bounce_type: Optional[
        Literal[
            "ContentRejected",
            "DoesNotExist",
            "ExceededQuota",
            "MessageTooLarge",
            "TemporaryFailure",
            "Undefined",
        ]
    ] = Field(default=None, alias="BounceType")
    recipient_dsn_fields: Optional[RecipientDsnFieldsModel] = Field(
        default=None, alias="RecipientDsnFields"
    )


class ReceiptRuleModel(BaseModel):
    name: str = Field(alias="Name")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tls_policy: Optional[Literal["Optional", "Require"]] = Field(
        default=None, alias="TlsPolicy"
    )
    recipients: Optional[Sequence[str]] = Field(default=None, alias="Recipients")
    actions: Optional[Sequence[ReceiptActionModel]] = Field(
        default=None, alias="Actions"
    )
    scan_enabled: Optional[bool] = Field(default=None, alias="ScanEnabled")


class CreateReceiptFilterRequestModel(BaseModel):
    filter: ReceiptFilterModel = Field(alias="Filter")


class ListReceiptFiltersResponseModel(BaseModel):
    filters: List[ReceiptFilterModel] = Field(alias="Filters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendEmailRequestModel(BaseModel):
    source: str = Field(alias="Source")
    destination: DestinationModel = Field(alias="Destination")
    message: MessageModel = Field(alias="Message")
    reply_to_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ReplyToAddresses"
    )
    return_path: Optional[str] = Field(default=None, alias="ReturnPath")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    return_path_arn: Optional[str] = Field(default=None, alias="ReturnPathArn")
    tags: Optional[Sequence[MessageTagModel]] = Field(default=None, alias="Tags")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class CreateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: EventDestinationModel = Field(alias="EventDestination")


class DescribeConfigurationSetResponseModel(BaseModel):
    configuration_set: ConfigurationSetModel = Field(alias="ConfigurationSet")
    event_destinations: List[EventDestinationModel] = Field(alias="EventDestinations")
    tracking_options: TrackingOptionsModel = Field(alias="TrackingOptions")
    delivery_options: DeliveryOptionsModel = Field(alias="DeliveryOptions")
    reputation_options: ReputationOptionsModel = Field(alias="ReputationOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: EventDestinationModel = Field(alias="EventDestination")


class SendBounceRequestModel(BaseModel):
    original_message_id: str = Field(alias="OriginalMessageId")
    bounce_sender: str = Field(alias="BounceSender")
    bounced_recipient_info_list: Sequence[BouncedRecipientInfoModel] = Field(
        alias="BouncedRecipientInfoList"
    )
    explanation: Optional[str] = Field(default=None, alias="Explanation")
    message_dsn: Optional[MessageDsnModel] = Field(default=None, alias="MessageDsn")
    bounce_sender_arn: Optional[str] = Field(default=None, alias="BounceSenderArn")


class CreateReceiptRuleRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule: ReceiptRuleModel = Field(alias="Rule")
    after: Optional[str] = Field(default=None, alias="After")


class DescribeActiveReceiptRuleSetResponseModel(BaseModel):
    metadata: ReceiptRuleSetMetadataModel = Field(alias="Metadata")
    rules: List[ReceiptRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReceiptRuleResponseModel(BaseModel):
    rule: ReceiptRuleModel = Field(alias="Rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReceiptRuleSetResponseModel(BaseModel):
    metadata: ReceiptRuleSetMetadataModel = Field(alias="Metadata")
    rules: List[ReceiptRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReceiptRuleRequestModel(BaseModel):
    rule_set_name: str = Field(alias="RuleSetName")
    rule: ReceiptRuleModel = Field(alias="Rule")
