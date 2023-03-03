# Model Generated: Thu Mar  2 21:56:17 2023

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


class RecoveryOptionTypeModel(BaseModel):
    priority: int = Field(alias="Priority")
    name: Literal["admin_only", "verified_email", "verified_phone_number"] = Field(
        alias="Name"
    )


class AccountTakeoverActionTypeModel(BaseModel):
    notify: bool = Field(alias="Notify")
    event_action: Literal[
        "BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"
    ] = Field(alias="EventAction")


class AdminAddUserToGroupRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    group_name: str = Field(alias="GroupName")


class AdminConfirmSignUpRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class MessageTemplateTypeModel(BaseModel):
    s_ms_message: Optional[str] = Field(default=None, alias="SMSMessage")
    email_message: Optional[str] = Field(default=None, alias="EmailMessage")
    email_subject: Optional[str] = Field(default=None, alias="EmailSubject")


class AttributeTypeModel(BaseModel):
    name: str = Field(alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AdminDeleteUserAttributesRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    user_attribute_names: Sequence[str] = Field(alias="UserAttributeNames")


class AdminDeleteUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class ProviderUserIdentifierTypeModel(BaseModel):
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")
    provider_attribute_name: Optional[str] = Field(
        default=None, alias="ProviderAttributeName"
    )
    provider_attribute_value: Optional[str] = Field(
        default=None, alias="ProviderAttributeValue"
    )


class AdminDisableUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class AdminEnableUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class AdminForgetDeviceRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    device_key: str = Field(alias="DeviceKey")


class AdminGetDeviceRequestModel(BaseModel):
    device_key: str = Field(alias="DeviceKey")
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class AdminGetUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class MFAOptionTypeModel(BaseModel):
    delivery_medium: Optional[Literal["EMAIL", "SMS"]] = Field(
        default=None, alias="DeliveryMedium"
    )
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")


class AnalyticsMetadataTypeModel(BaseModel):
    analytics_endpoint_id: Optional[str] = Field(
        default=None, alias="AnalyticsEndpointId"
    )


class AdminListDevicesRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    limit: Optional[int] = Field(default=None, alias="Limit")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class AdminListGroupsForUserRequestModel(BaseModel):
    username: str = Field(alias="Username")
    user_pool_id: str = Field(alias="UserPoolId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GroupTypeModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    precedence: Optional[int] = Field(default=None, alias="Precedence")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class AdminListUserAuthEventsRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class AdminRemoveUserFromGroupRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    group_name: str = Field(alias="GroupName")


class AdminResetUserPasswordRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class SMSMfaSettingsTypeModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    preferred_mfa: Optional[bool] = Field(default=None, alias="PreferredMfa")


class SoftwareTokenMfaSettingsTypeModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    preferred_mfa: Optional[bool] = Field(default=None, alias="PreferredMfa")


class AdminSetUserPasswordRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")
    permanent: Optional[bool] = Field(default=None, alias="Permanent")


class AdminUpdateAuthEventFeedbackRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    event_id: str = Field(alias="EventId")
    feedback_value: Literal["Invalid", "Valid"] = Field(alias="FeedbackValue")


class AdminUpdateDeviceStatusRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    device_key: str = Field(alias="DeviceKey")
    device_remembered_status: Optional[Literal["not_remembered", "remembered"]] = Field(
        default=None, alias="DeviceRememberedStatus"
    )


class AdminUserGlobalSignOutRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")


class AnalyticsConfigurationTypeModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    user_data_shared: Optional[bool] = Field(default=None, alias="UserDataShared")


class AssociateSoftwareTokenRequestModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="AccessToken")
    session: Optional[str] = Field(default=None, alias="Session")


class ChallengeResponseTypeModel(BaseModel):
    challenge_name: Optional[Literal["Mfa", "Password"]] = Field(
        default=None, alias="ChallengeName"
    )
    challenge_response: Optional[Literal["Failure", "Success"]] = Field(
        default=None, alias="ChallengeResponse"
    )


class EventContextDataTypeModel(BaseModel):
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    city: Optional[str] = Field(default=None, alias="City")
    country: Optional[str] = Field(default=None, alias="Country")


class EventFeedbackTypeModel(BaseModel):
    feedback_value: Literal["Invalid", "Valid"] = Field(alias="FeedbackValue")
    provider: str = Field(alias="Provider")
    feedback_date: Optional[datetime] = Field(default=None, alias="FeedbackDate")


class EventRiskTypeModel(BaseModel):
    risk_decision: Optional[Literal["AccountTakeover", "Block", "NoRisk"]] = Field(
        default=None, alias="RiskDecision"
    )
    risk_level: Optional[Literal["High", "Low", "Medium"]] = Field(
        default=None, alias="RiskLevel"
    )
    compromised_credentials_detected: Optional[bool] = Field(
        default=None, alias="CompromisedCredentialsDetected"
    )


class NewDeviceMetadataTypeModel(BaseModel):
    device_key: Optional[str] = Field(default=None, alias="DeviceKey")
    device_group_key: Optional[str] = Field(default=None, alias="DeviceGroupKey")


class ChangePasswordRequestModel(BaseModel):
    previous_password: str = Field(alias="PreviousPassword")
    proposed_password: str = Field(alias="ProposedPassword")
    access_token: str = Field(alias="AccessToken")


class CodeDeliveryDetailsTypeModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")
    delivery_medium: Optional[Literal["EMAIL", "SMS"]] = Field(
        default=None, alias="DeliveryMedium"
    )
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")


class CompromisedCredentialsActionsTypeModel(BaseModel):
    event_action: Literal["BLOCK", "NO_ACTION"] = Field(alias="EventAction")


class DeviceSecretVerifierConfigTypeModel(BaseModel):
    password_verifier: Optional[str] = Field(default=None, alias="PasswordVerifier")
    salt: Optional[str] = Field(default=None, alias="Salt")


class UserContextDataTypeModel(BaseModel):
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    encoded_data: Optional[str] = Field(default=None, alias="EncodedData")


class HttpHeaderModel(BaseModel):
    header_name: Optional[str] = Field(default=None, alias="headerName")
    header_value: Optional[str] = Field(default=None, alias="headerValue")


class CreateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_pool_id: str = Field(alias="UserPoolId")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    precedence: Optional[int] = Field(default=None, alias="Precedence")


class CreateIdentityProviderRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    provider_name: str = Field(alias="ProviderName")
    provider_type: Literal[
        "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
    ] = Field(alias="ProviderType")
    provider_details: Mapping[str, str] = Field(alias="ProviderDetails")
    attribute_mapping: Optional[Mapping[str, str]] = Field(
        default=None, alias="AttributeMapping"
    )
    idp_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="IdpIdentifiers"
    )


class IdentityProviderTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")
    provider_type: Optional[
        Literal[
            "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
        ]
    ] = Field(default=None, alias="ProviderType")
    provider_details: Optional[Dict[str, str]] = Field(
        default=None, alias="ProviderDetails"
    )
    attribute_mapping: Optional[Dict[str, str]] = Field(
        default=None, alias="AttributeMapping"
    )
    idp_identifiers: Optional[List[str]] = Field(default=None, alias="IdpIdentifiers")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class ResourceServerScopeTypeModel(BaseModel):
    scope_name: str = Field(alias="ScopeName")
    scope_description: str = Field(alias="ScopeDescription")


class CreateUserImportJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    user_pool_id: str = Field(alias="UserPoolId")
    cloud_watch_logs_role_arn: str = Field(alias="CloudWatchLogsRoleArn")


class UserImportJobTypeModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    completion_date: Optional[datetime] = Field(default=None, alias="CompletionDate")
    status: Optional[
        Literal[
            "Created",
            "Expired",
            "Failed",
            "InProgress",
            "Pending",
            "Stopped",
            "Stopping",
            "Succeeded",
        ]
    ] = Field(default=None, alias="Status")
    cloud_watch_logs_role_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsRoleArn"
    )
    imported_users: Optional[int] = Field(default=None, alias="ImportedUsers")
    skipped_users: Optional[int] = Field(default=None, alias="SkippedUsers")
    failed_users: Optional[int] = Field(default=None, alias="FailedUsers")
    completion_message: Optional[str] = Field(default=None, alias="CompletionMessage")


class TokenValidityUnitsTypeModel(BaseModel):
    access_token: Optional[Literal["days", "hours", "minutes", "seconds"]] = Field(
        default=None, alias="AccessToken"
    )
    id_token: Optional[Literal["days", "hours", "minutes", "seconds"]] = Field(
        default=None, alias="IdToken"
    )
    refresh_token: Optional[Literal["days", "hours", "minutes", "seconds"]] = Field(
        default=None, alias="RefreshToken"
    )


class CustomDomainConfigTypeModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class DeviceConfigurationTypeModel(BaseModel):
    challenge_required_on_new_device: Optional[bool] = Field(
        default=None, alias="ChallengeRequiredOnNewDevice"
    )
    device_only_remembered_on_user_prompt: Optional[bool] = Field(
        default=None, alias="DeviceOnlyRememberedOnUserPrompt"
    )


class EmailConfigurationTypeModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    reply_to_email_address: Optional[str] = Field(
        default=None, alias="ReplyToEmailAddress"
    )
    email_sending_account: Optional[Literal["COGNITO_DEFAULT", "DEVELOPER"]] = Field(
        default=None, alias="EmailSendingAccount"
    )
    from_: Optional[str] = Field(default=None, alias="From")
    configuration_set: Optional[str] = Field(default=None, alias="ConfigurationSet")


class SmsConfigurationTypeModel(BaseModel):
    sns_caller_arn: str = Field(alias="SnsCallerArn")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    sns_region: Optional[str] = Field(default=None, alias="SnsRegion")


class UserAttributeUpdateSettingsTypeModel(BaseModel):
    attributes_require_verification_before_update: Optional[
        Sequence[Literal["email", "phone_number"]]
    ] = Field(default=None, alias="AttributesRequireVerificationBeforeUpdate")


class UserPoolAddOnsTypeModel(BaseModel):
    advanced_security_mode: Literal["AUDIT", "ENFORCED", "OFF"] = Field(
        alias="AdvancedSecurityMode"
    )


class UsernameConfigurationTypeModel(BaseModel):
    case_sensitive: bool = Field(alias="CaseSensitive")


class VerificationMessageTemplateTypeModel(BaseModel):
    sms_message: Optional[str] = Field(default=None, alias="SmsMessage")
    email_message: Optional[str] = Field(default=None, alias="EmailMessage")
    email_subject: Optional[str] = Field(default=None, alias="EmailSubject")
    email_message_by_link: Optional[str] = Field(
        default=None, alias="EmailMessageByLink"
    )
    email_subject_by_link: Optional[str] = Field(
        default=None, alias="EmailSubjectByLink"
    )
    default_email_option: Optional[
        Literal["CONFIRM_WITH_CODE", "CONFIRM_WITH_LINK"]
    ] = Field(default=None, alias="DefaultEmailOption")


class CustomEmailLambdaVersionConfigTypeModel(BaseModel):
    lambda_version: Literal["V1_0"] = Field(alias="LambdaVersion")
    lambda_arn: str = Field(alias="LambdaArn")


class CustomSMSLambdaVersionConfigTypeModel(BaseModel):
    lambda_version: Literal["V1_0"] = Field(alias="LambdaVersion")
    lambda_arn: str = Field(alias="LambdaArn")


class DeleteGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_pool_id: str = Field(alias="UserPoolId")


class DeleteIdentityProviderRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    provider_name: str = Field(alias="ProviderName")


class DeleteResourceServerRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    identifier: str = Field(alias="Identifier")


class DeleteUserAttributesRequestModel(BaseModel):
    user_attribute_names: Sequence[str] = Field(alias="UserAttributeNames")
    access_token: str = Field(alias="AccessToken")


class DeleteUserPoolClientRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: str = Field(alias="ClientId")


class DeleteUserPoolDomainRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    user_pool_id: str = Field(alias="UserPoolId")


class DeleteUserPoolRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")


class DeleteUserRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")


class DescribeIdentityProviderRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    provider_name: str = Field(alias="ProviderName")


class DescribeResourceServerRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    identifier: str = Field(alias="Identifier")


class DescribeRiskConfigurationRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")


class DescribeUserImportJobRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    job_id: str = Field(alias="JobId")


class DescribeUserPoolClientRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: str = Field(alias="ClientId")


class DescribeUserPoolDomainRequestModel(BaseModel):
    domain: str = Field(alias="Domain")


class DescribeUserPoolRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")


class ForgetDeviceRequestModel(BaseModel):
    device_key: str = Field(alias="DeviceKey")
    access_token: Optional[str] = Field(default=None, alias="AccessToken")


class GetCSVHeaderRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")


class GetDeviceRequestModel(BaseModel):
    device_key: str = Field(alias="DeviceKey")
    access_token: Optional[str] = Field(default=None, alias="AccessToken")


class GetGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_pool_id: str = Field(alias="UserPoolId")


class GetIdentityProviderByIdentifierRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    idp_identifier: str = Field(alias="IdpIdentifier")


class GetSigningCertificateRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")


class GetUICustomizationRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")


class UICustomizationTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    image_url: Optional[str] = Field(default=None, alias="ImageUrl")
    cs_s: Optional[str] = Field(default=None, alias="CSS")
    cs_s_version: Optional[str] = Field(default=None, alias="CSSVersion")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class GetUserAttributeVerificationCodeRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    attribute_name: str = Field(alias="AttributeName")
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class GetUserPoolMfaConfigRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")


class SoftwareTokenMfaConfigTypeModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class GetUserRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")


class GlobalSignOutRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")


class ListDevicesRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class ListGroupsRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListIdentityProvidersRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProviderDescriptionModel(BaseModel):
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")
    provider_type: Optional[
        Literal[
            "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
        ]
    ] = Field(default=None, alias="ProviderType")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class ListResourceServersRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListUserImportJobsRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    max_results: int = Field(alias="MaxResults")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class ListUserPoolClientsRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UserPoolClientDescriptionModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    client_name: Optional[str] = Field(default=None, alias="ClientName")


class ListUserPoolsRequestModel(BaseModel):
    max_results: int = Field(alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListUsersInGroupRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    group_name: str = Field(alias="GroupName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListUsersRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")
    filter: Optional[str] = Field(default=None, alias="Filter")


class NotifyEmailTypeModel(BaseModel):
    subject: str = Field(alias="Subject")
    html_body: Optional[str] = Field(default=None, alias="HtmlBody")
    text_body: Optional[str] = Field(default=None, alias="TextBody")


class NumberAttributeConstraintsTypeModel(BaseModel):
    min_value: Optional[str] = Field(default=None, alias="MinValue")
    max_value: Optional[str] = Field(default=None, alias="MaxValue")


class PasswordPolicyTypeModel(BaseModel):
    minimum_length: Optional[int] = Field(default=None, alias="MinimumLength")
    require_uppercase: Optional[bool] = Field(default=None, alias="RequireUppercase")
    require_lowercase: Optional[bool] = Field(default=None, alias="RequireLowercase")
    require_numbers: Optional[bool] = Field(default=None, alias="RequireNumbers")
    require_symbols: Optional[bool] = Field(default=None, alias="RequireSymbols")
    temporary_password_validity_days: Optional[int] = Field(
        default=None, alias="TemporaryPasswordValidityDays"
    )


class RevokeTokenRequestModel(BaseModel):
    token: str = Field(alias="Token")
    client_id: str = Field(alias="ClientId")
    client_secret: Optional[str] = Field(default=None, alias="ClientSecret")


class RiskExceptionConfigurationTypeModel(BaseModel):
    blocked_ip_range_list: Optional[List[str]] = Field(
        default=None, alias="BlockedIPRangeList"
    )
    skipped_ip_range_list: Optional[List[str]] = Field(
        default=None, alias="SkippedIPRangeList"
    )


class StringAttributeConstraintsTypeModel(BaseModel):
    min_length: Optional[str] = Field(default=None, alias="MinLength")
    max_length: Optional[str] = Field(default=None, alias="MaxLength")


class SetUICustomizationRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    cs_s: Optional[str] = Field(default=None, alias="CSS")
    image_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ImageFile"
    )


class StartUserImportJobRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    job_id: str = Field(alias="JobId")


class StopUserImportJobRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    job_id: str = Field(alias="JobId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAuthEventFeedbackRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    event_id: str = Field(alias="EventId")
    feedback_token: str = Field(alias="FeedbackToken")
    feedback_value: Literal["Invalid", "Valid"] = Field(alias="FeedbackValue")


class UpdateDeviceStatusRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    device_key: str = Field(alias="DeviceKey")
    device_remembered_status: Optional[Literal["not_remembered", "remembered"]] = Field(
        default=None, alias="DeviceRememberedStatus"
    )


class UpdateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_pool_id: str = Field(alias="UserPoolId")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    precedence: Optional[int] = Field(default=None, alias="Precedence")


class UpdateIdentityProviderRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    provider_name: str = Field(alias="ProviderName")
    provider_details: Optional[Mapping[str, str]] = Field(
        default=None, alias="ProviderDetails"
    )
    attribute_mapping: Optional[Mapping[str, str]] = Field(
        default=None, alias="AttributeMapping"
    )
    idp_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="IdpIdentifiers"
    )


class VerifySoftwareTokenRequestModel(BaseModel):
    user_code: str = Field(alias="UserCode")
    access_token: Optional[str] = Field(default=None, alias="AccessToken")
    session: Optional[str] = Field(default=None, alias="Session")
    friendly_device_name: Optional[str] = Field(
        default=None, alias="FriendlyDeviceName"
    )


class VerifyUserAttributeRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    attribute_name: str = Field(alias="AttributeName")
    code: str = Field(alias="Code")


class AccountRecoverySettingTypeModel(BaseModel):
    recovery_mechanisms: Optional[Sequence[RecoveryOptionTypeModel]] = Field(
        default=None, alias="RecoveryMechanisms"
    )


class AccountTakeoverActionsTypeModel(BaseModel):
    low_action: Optional[AccountTakeoverActionTypeModel] = Field(
        default=None, alias="LowAction"
    )
    medium_action: Optional[AccountTakeoverActionTypeModel] = Field(
        default=None, alias="MediumAction"
    )
    high_action: Optional[AccountTakeoverActionTypeModel] = Field(
        default=None, alias="HighAction"
    )


class AdminCreateUserConfigTypeModel(BaseModel):
    allow_admin_create_user_only: Optional[bool] = Field(
        default=None, alias="AllowAdminCreateUserOnly"
    )
    unused_account_validity_days: Optional[int] = Field(
        default=None, alias="UnusedAccountValidityDays"
    )
    invite_message_template: Optional[MessageTemplateTypeModel] = Field(
        default=None, alias="InviteMessageTemplate"
    )


class AdminCreateUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    user_attributes: Optional[Sequence[AttributeTypeModel]] = Field(
        default=None, alias="UserAttributes"
    )
    validation_data: Optional[Sequence[AttributeTypeModel]] = Field(
        default=None, alias="ValidationData"
    )
    temporary_password: Optional[str] = Field(default=None, alias="TemporaryPassword")
    force_alias_creation: Optional[bool] = Field(
        default=None, alias="ForceAliasCreation"
    )
    message_action: Optional[Literal["RESEND", "SUPPRESS"]] = Field(
        default=None, alias="MessageAction"
    )
    desired_delivery_mediums: Optional[Sequence[Literal["EMAIL", "SMS"]]] = Field(
        default=None, alias="DesiredDeliveryMediums"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class AdminUpdateUserAttributesRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    user_attributes: Sequence[AttributeTypeModel] = Field(alias="UserAttributes")
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class DeviceTypeModel(BaseModel):
    device_key: Optional[str] = Field(default=None, alias="DeviceKey")
    device_attributes: Optional[List[AttributeTypeModel]] = Field(
        default=None, alias="DeviceAttributes"
    )
    device_create_date: Optional[datetime] = Field(
        default=None, alias="DeviceCreateDate"
    )
    device_last_modified_date: Optional[datetime] = Field(
        default=None, alias="DeviceLastModifiedDate"
    )
    device_last_authenticated_date: Optional[datetime] = Field(
        default=None, alias="DeviceLastAuthenticatedDate"
    )


class UpdateUserAttributesRequestModel(BaseModel):
    user_attributes: Sequence[AttributeTypeModel] = Field(alias="UserAttributes")
    access_token: str = Field(alias="AccessToken")
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class AssociateSoftwareTokenResponseModel(BaseModel):
    secret_code: str = Field(alias="SecretCode")
    session: str = Field(alias="Session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmDeviceResponseModel(BaseModel):
    user_confirmation_necessary: bool = Field(alias="UserConfirmationNecessary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserPoolDomainResponseModel(BaseModel):
    cloud_front_domain: str = Field(alias="CloudFrontDomain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCSVHeaderResponseModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    cs_vheader: List[str] = Field(alias="CSVHeader")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSigningCertificateResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserPoolDomainResponseModel(BaseModel):
    cloud_front_domain: str = Field(alias="CloudFrontDomain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifySoftwareTokenResponseModel(BaseModel):
    status: Literal["ERROR", "SUCCESS"] = Field(alias="Status")
    session: str = Field(alias="Session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminDisableProviderForUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    user: ProviderUserIdentifierTypeModel = Field(alias="User")


class AdminLinkProviderForUserRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    destination_user: ProviderUserIdentifierTypeModel = Field(alias="DestinationUser")
    source_user: ProviderUserIdentifierTypeModel = Field(alias="SourceUser")


class AdminGetUserResponseModel(BaseModel):
    username: str = Field(alias="Username")
    user_attributes: List[AttributeTypeModel] = Field(alias="UserAttributes")
    user_create_date: datetime = Field(alias="UserCreateDate")
    user_last_modified_date: datetime = Field(alias="UserLastModifiedDate")
    enabled: bool = Field(alias="Enabled")
    user_status: Literal[
        "ARCHIVED",
        "COMPROMISED",
        "CONFIRMED",
        "FORCE_CHANGE_PASSWORD",
        "RESET_REQUIRED",
        "UNCONFIRMED",
        "UNKNOWN",
    ] = Field(alias="UserStatus")
    mfaoptions: List[MFAOptionTypeModel] = Field(alias="MFAOptions")
    preferred_mfa_setting: str = Field(alias="PreferredMfaSetting")
    user_mfasetting_list: List[str] = Field(alias="UserMFASettingList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminSetUserSettingsRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    mfaoptions: Sequence[MFAOptionTypeModel] = Field(alias="MFAOptions")


class GetUserResponseModel(BaseModel):
    username: str = Field(alias="Username")
    user_attributes: List[AttributeTypeModel] = Field(alias="UserAttributes")
    mfaoptions: List[MFAOptionTypeModel] = Field(alias="MFAOptions")
    preferred_mfa_setting: str = Field(alias="PreferredMfaSetting")
    user_mfasetting_list: List[str] = Field(alias="UserMFASettingList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetUserSettingsRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    mfaoptions: Sequence[MFAOptionTypeModel] = Field(alias="MFAOptions")


class UserTypeModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    attributes: Optional[List[AttributeTypeModel]] = Field(
        default=None, alias="Attributes"
    )
    user_create_date: Optional[datetime] = Field(default=None, alias="UserCreateDate")
    user_last_modified_date: Optional[datetime] = Field(
        default=None, alias="UserLastModifiedDate"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    user_status: Optional[
        Literal[
            "ARCHIVED",
            "COMPROMISED",
            "CONFIRMED",
            "FORCE_CHANGE_PASSWORD",
            "RESET_REQUIRED",
            "UNCONFIRMED",
            "UNKNOWN",
        ]
    ] = Field(default=None, alias="UserStatus")
    mfaoptions: Optional[List[MFAOptionTypeModel]] = Field(
        default=None, alias="MFAOptions"
    )


class AdminListGroupsForUserRequestAdminListGroupsForUserPaginateModel(BaseModel):
    username: str = Field(alias="Username")
    user_pool_id: str = Field(alias="UserPoolId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    username: str = Field(alias="Username")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsRequestListGroupsPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIdentityProvidersRequestListIdentityProvidersPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceServersRequestListResourceServersPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserPoolClientsRequestListUserPoolClientsPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserPoolsRequestListUserPoolsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersInGroupRequestListUsersInGroupPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    group_name: str = Field(alias="GroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    filter: Optional[str] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class AdminListGroupsForUserResponseModel(BaseModel):
    groups: List[GroupTypeModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    group: GroupTypeModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupResponseModel(BaseModel):
    group: GroupTypeModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupTypeModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupResponseModel(BaseModel):
    group: GroupTypeModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminSetUserMFAPreferenceRequestModel(BaseModel):
    username: str = Field(alias="Username")
    user_pool_id: str = Field(alias="UserPoolId")
    s_ms_mfa_settings: Optional[SMSMfaSettingsTypeModel] = Field(
        default=None, alias="SMSMfaSettings"
    )
    software_token_mfa_settings: Optional[SoftwareTokenMfaSettingsTypeModel] = Field(
        default=None, alias="SoftwareTokenMfaSettings"
    )


class SetUserMFAPreferenceRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    s_ms_mfa_settings: Optional[SMSMfaSettingsTypeModel] = Field(
        default=None, alias="SMSMfaSettings"
    )
    software_token_mfa_settings: Optional[SoftwareTokenMfaSettingsTypeModel] = Field(
        default=None, alias="SoftwareTokenMfaSettings"
    )


class AuthEventTypeModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    event_type: Optional[
        Literal["ForgotPassword", "PasswordChange", "ResendCode", "SignIn", "SignUp"]
    ] = Field(default=None, alias="EventType")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    event_response: Optional[Literal["Fail", "InProgress", "Pass"]] = Field(
        default=None, alias="EventResponse"
    )
    event_risk: Optional[EventRiskTypeModel] = Field(default=None, alias="EventRisk")
    challenge_responses: Optional[List[ChallengeResponseTypeModel]] = Field(
        default=None, alias="ChallengeResponses"
    )
    event_context_data: Optional[EventContextDataTypeModel] = Field(
        default=None, alias="EventContextData"
    )
    event_feedback: Optional[EventFeedbackTypeModel] = Field(
        default=None, alias="EventFeedback"
    )


class AuthenticationResultTypeModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="AccessToken")
    expires_in: Optional[int] = Field(default=None, alias="ExpiresIn")
    token_type: Optional[str] = Field(default=None, alias="TokenType")
    refresh_token: Optional[str] = Field(default=None, alias="RefreshToken")
    id_token: Optional[str] = Field(default=None, alias="IdToken")
    new_device_metadata: Optional[NewDeviceMetadataTypeModel] = Field(
        default=None, alias="NewDeviceMetadata"
    )


class ForgotPasswordResponseModel(BaseModel):
    code_delivery_details: CodeDeliveryDetailsTypeModel = Field(
        alias="CodeDeliveryDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserAttributeVerificationCodeResponseModel(BaseModel):
    code_delivery_details: CodeDeliveryDetailsTypeModel = Field(
        alias="CodeDeliveryDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResendConfirmationCodeResponseModel(BaseModel):
    code_delivery_details: CodeDeliveryDetailsTypeModel = Field(
        alias="CodeDeliveryDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SignUpResponseModel(BaseModel):
    user_confirmed: bool = Field(alias="UserConfirmed")
    code_delivery_details: CodeDeliveryDetailsTypeModel = Field(
        alias="CodeDeliveryDetails"
    )
    user_sub: str = Field(alias="UserSub")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserAttributesResponseModel(BaseModel):
    code_delivery_details_list: List[CodeDeliveryDetailsTypeModel] = Field(
        alias="CodeDeliveryDetailsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompromisedCredentialsRiskConfigurationTypeModel(BaseModel):
    actions: CompromisedCredentialsActionsTypeModel = Field(alias="Actions")
    event_filter: Optional[
        List[Literal["PASSWORD_CHANGE", "SIGN_IN", "SIGN_UP"]]
    ] = Field(default=None, alias="EventFilter")


class ConfirmDeviceRequestModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    device_key: str = Field(alias="DeviceKey")
    device_secret_verifier_config: Optional[
        DeviceSecretVerifierConfigTypeModel
    ] = Field(default=None, alias="DeviceSecretVerifierConfig")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")


class ConfirmForgotPasswordRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    username: str = Field(alias="Username")
    confirmation_code: str = Field(alias="ConfirmationCode")
    password: str = Field(alias="Password")
    secret_hash: Optional[str] = Field(default=None, alias="SecretHash")
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class ConfirmSignUpRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    username: str = Field(alias="Username")
    confirmation_code: str = Field(alias="ConfirmationCode")
    secret_hash: Optional[str] = Field(default=None, alias="SecretHash")
    force_alias_creation: Optional[bool] = Field(
        default=None, alias="ForceAliasCreation"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class ForgotPasswordRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    username: str = Field(alias="Username")
    secret_hash: Optional[str] = Field(default=None, alias="SecretHash")
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class InitiateAuthRequestModel(BaseModel):
    auth_flow: Literal[
        "ADMIN_NO_SRP_AUTH",
        "ADMIN_USER_PASSWORD_AUTH",
        "CUSTOM_AUTH",
        "REFRESH_TOKEN",
        "REFRESH_TOKEN_AUTH",
        "USER_PASSWORD_AUTH",
        "USER_SRP_AUTH",
    ] = Field(alias="AuthFlow")
    client_id: str = Field(alias="ClientId")
    auth_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="AuthParameters"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )


class ResendConfirmationCodeRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    username: str = Field(alias="Username")
    secret_hash: Optional[str] = Field(default=None, alias="SecretHash")
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class RespondToAuthChallengeRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    session: Optional[str] = Field(default=None, alias="Session")
    challenge_responses: Optional[Mapping[str, str]] = Field(
        default=None, alias="ChallengeResponses"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class SignUpRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")
    secret_hash: Optional[str] = Field(default=None, alias="SecretHash")
    user_attributes: Optional[Sequence[AttributeTypeModel]] = Field(
        default=None, alias="UserAttributes"
    )
    validation_data: Optional[Sequence[AttributeTypeModel]] = Field(
        default=None, alias="ValidationData"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    user_context_data: Optional[UserContextDataTypeModel] = Field(
        default=None, alias="UserContextData"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class ContextDataTypeModel(BaseModel):
    ip_address: str = Field(alias="IpAddress")
    server_name: str = Field(alias="ServerName")
    server_path: str = Field(alias="ServerPath")
    http_headers: Sequence[HttpHeaderModel] = Field(alias="HttpHeaders")
    encoded_data: Optional[str] = Field(default=None, alias="EncodedData")


class CreateIdentityProviderResponseModel(BaseModel):
    identity_provider: IdentityProviderTypeModel = Field(alias="IdentityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIdentityProviderResponseModel(BaseModel):
    identity_provider: IdentityProviderTypeModel = Field(alias="IdentityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityProviderByIdentifierResponseModel(BaseModel):
    identity_provider: IdentityProviderTypeModel = Field(alias="IdentityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIdentityProviderResponseModel(BaseModel):
    identity_provider: IdentityProviderTypeModel = Field(alias="IdentityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceServerRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    identifier: str = Field(alias="Identifier")
    name: str = Field(alias="Name")
    scopes: Optional[Sequence[ResourceServerScopeTypeModel]] = Field(
        default=None, alias="Scopes"
    )


class ResourceServerTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    name: Optional[str] = Field(default=None, alias="Name")
    scopes: Optional[List[ResourceServerScopeTypeModel]] = Field(
        default=None, alias="Scopes"
    )


class UpdateResourceServerRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    identifier: str = Field(alias="Identifier")
    name: str = Field(alias="Name")
    scopes: Optional[Sequence[ResourceServerScopeTypeModel]] = Field(
        default=None, alias="Scopes"
    )


class CreateUserImportJobResponseModel(BaseModel):
    user_import_job: UserImportJobTypeModel = Field(alias="UserImportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserImportJobResponseModel(BaseModel):
    user_import_job: UserImportJobTypeModel = Field(alias="UserImportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserImportJobsResponseModel(BaseModel):
    user_import_jobs: List[UserImportJobTypeModel] = Field(alias="UserImportJobs")
    pagination_token: str = Field(alias="PaginationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartUserImportJobResponseModel(BaseModel):
    user_import_job: UserImportJobTypeModel = Field(alias="UserImportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopUserImportJobResponseModel(BaseModel):
    user_import_job: UserImportJobTypeModel = Field(alias="UserImportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserPoolClientRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_name: str = Field(alias="ClientName")
    generate_secret: Optional[bool] = Field(default=None, alias="GenerateSecret")
    refresh_token_validity: Optional[int] = Field(
        default=None, alias="RefreshTokenValidity"
    )
    access_token_validity: Optional[int] = Field(
        default=None, alias="AccessTokenValidity"
    )
    id_token_validity: Optional[int] = Field(default=None, alias="IdTokenValidity")
    token_validity_units: Optional[TokenValidityUnitsTypeModel] = Field(
        default=None, alias="TokenValidityUnits"
    )
    read_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="ReadAttributes"
    )
    write_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="WriteAttributes"
    )
    explicit_auth_flows: Optional[
        Sequence[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
            ]
        ]
    ] = Field(default=None, alias="ExplicitAuthFlows")
    supported_identity_providers: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedIdentityProviders"
    )
    callback_urls: Optional[Sequence[str]] = Field(default=None, alias="CallbackURLs")
    logout_urls: Optional[Sequence[str]] = Field(default=None, alias="LogoutURLs")
    default_redirect_uri: Optional[str] = Field(
        default=None, alias="DefaultRedirectURI"
    )
    allowed_oauth_flows: Optional[
        Sequence[Literal["client_credentials", "code", "implicit"]]
    ] = Field(default=None, alias="AllowedOAuthFlows")
    allowed_oauth_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedOAuthScopes"
    )
    allowed_oauth_flows_user_pool_client: Optional[bool] = Field(
        default=None, alias="AllowedOAuthFlowsUserPoolClient"
    )
    analytics_configuration: Optional[AnalyticsConfigurationTypeModel] = Field(
        default=None, alias="AnalyticsConfiguration"
    )
    prevent_user_existence_errors: Optional[Literal["ENABLED", "LEGACY"]] = Field(
        default=None, alias="PreventUserExistenceErrors"
    )
    enable_token_revocation: Optional[bool] = Field(
        default=None, alias="EnableTokenRevocation"
    )
    enable_propagate_additional_user_context_data: Optional[bool] = Field(
        default=None, alias="EnablePropagateAdditionalUserContextData"
    )
    auth_session_validity: Optional[int] = Field(
        default=None, alias="AuthSessionValidity"
    )


class UpdateUserPoolClientRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: str = Field(alias="ClientId")
    client_name: Optional[str] = Field(default=None, alias="ClientName")
    refresh_token_validity: Optional[int] = Field(
        default=None, alias="RefreshTokenValidity"
    )
    access_token_validity: Optional[int] = Field(
        default=None, alias="AccessTokenValidity"
    )
    id_token_validity: Optional[int] = Field(default=None, alias="IdTokenValidity")
    token_validity_units: Optional[TokenValidityUnitsTypeModel] = Field(
        default=None, alias="TokenValidityUnits"
    )
    read_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="ReadAttributes"
    )
    write_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="WriteAttributes"
    )
    explicit_auth_flows: Optional[
        Sequence[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
            ]
        ]
    ] = Field(default=None, alias="ExplicitAuthFlows")
    supported_identity_providers: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedIdentityProviders"
    )
    callback_urls: Optional[Sequence[str]] = Field(default=None, alias="CallbackURLs")
    logout_urls: Optional[Sequence[str]] = Field(default=None, alias="LogoutURLs")
    default_redirect_uri: Optional[str] = Field(
        default=None, alias="DefaultRedirectURI"
    )
    allowed_oauth_flows: Optional[
        Sequence[Literal["client_credentials", "code", "implicit"]]
    ] = Field(default=None, alias="AllowedOAuthFlows")
    allowed_oauth_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedOAuthScopes"
    )
    allowed_oauth_flows_user_pool_client: Optional[bool] = Field(
        default=None, alias="AllowedOAuthFlowsUserPoolClient"
    )
    analytics_configuration: Optional[AnalyticsConfigurationTypeModel] = Field(
        default=None, alias="AnalyticsConfiguration"
    )
    prevent_user_existence_errors: Optional[Literal["ENABLED", "LEGACY"]] = Field(
        default=None, alias="PreventUserExistenceErrors"
    )
    enable_token_revocation: Optional[bool] = Field(
        default=None, alias="EnableTokenRevocation"
    )
    enable_propagate_additional_user_context_data: Optional[bool] = Field(
        default=None, alias="EnablePropagateAdditionalUserContextData"
    )
    auth_session_validity: Optional[int] = Field(
        default=None, alias="AuthSessionValidity"
    )


class UserPoolClientTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    client_name: Optional[str] = Field(default=None, alias="ClientName")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    client_secret: Optional[str] = Field(default=None, alias="ClientSecret")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    refresh_token_validity: Optional[int] = Field(
        default=None, alias="RefreshTokenValidity"
    )
    access_token_validity: Optional[int] = Field(
        default=None, alias="AccessTokenValidity"
    )
    id_token_validity: Optional[int] = Field(default=None, alias="IdTokenValidity")
    token_validity_units: Optional[TokenValidityUnitsTypeModel] = Field(
        default=None, alias="TokenValidityUnits"
    )
    read_attributes: Optional[List[str]] = Field(default=None, alias="ReadAttributes")
    write_attributes: Optional[List[str]] = Field(default=None, alias="WriteAttributes")
    explicit_auth_flows: Optional[
        List[
            Literal[
                "ADMIN_NO_SRP_AUTH",
                "ALLOW_ADMIN_USER_PASSWORD_AUTH",
                "ALLOW_CUSTOM_AUTH",
                "ALLOW_REFRESH_TOKEN_AUTH",
                "ALLOW_USER_PASSWORD_AUTH",
                "ALLOW_USER_SRP_AUTH",
                "CUSTOM_AUTH_FLOW_ONLY",
                "USER_PASSWORD_AUTH",
            ]
        ]
    ] = Field(default=None, alias="ExplicitAuthFlows")
    supported_identity_providers: Optional[List[str]] = Field(
        default=None, alias="SupportedIdentityProviders"
    )
    callback_urls: Optional[List[str]] = Field(default=None, alias="CallbackURLs")
    logout_urls: Optional[List[str]] = Field(default=None, alias="LogoutURLs")
    default_redirect_uri: Optional[str] = Field(
        default=None, alias="DefaultRedirectURI"
    )
    allowed_oauth_flows: Optional[
        List[Literal["client_credentials", "code", "implicit"]]
    ] = Field(default=None, alias="AllowedOAuthFlows")
    allowed_oauth_scopes: Optional[List[str]] = Field(
        default=None, alias="AllowedOAuthScopes"
    )
    allowed_oauth_flows_user_pool_client: Optional[bool] = Field(
        default=None, alias="AllowedOAuthFlowsUserPoolClient"
    )
    analytics_configuration: Optional[AnalyticsConfigurationTypeModel] = Field(
        default=None, alias="AnalyticsConfiguration"
    )
    prevent_user_existence_errors: Optional[Literal["ENABLED", "LEGACY"]] = Field(
        default=None, alias="PreventUserExistenceErrors"
    )
    enable_token_revocation: Optional[bool] = Field(
        default=None, alias="EnableTokenRevocation"
    )
    enable_propagate_additional_user_context_data: Optional[bool] = Field(
        default=None, alias="EnablePropagateAdditionalUserContextData"
    )
    auth_session_validity: Optional[int] = Field(
        default=None, alias="AuthSessionValidity"
    )


class CreateUserPoolDomainRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    user_pool_id: str = Field(alias="UserPoolId")
    custom_domain_config: Optional[CustomDomainConfigTypeModel] = Field(
        default=None, alias="CustomDomainConfig"
    )


class DomainDescriptionTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    aws_account_id: Optional[str] = Field(default=None, alias="AWSAccountId")
    domain: Optional[str] = Field(default=None, alias="Domain")
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    cloud_front_distribution: Optional[str] = Field(
        default=None, alias="CloudFrontDistribution"
    )
    version: Optional[str] = Field(default=None, alias="Version")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    custom_domain_config: Optional[CustomDomainConfigTypeModel] = Field(
        default=None, alias="CustomDomainConfig"
    )


class UpdateUserPoolDomainRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    user_pool_id: str = Field(alias="UserPoolId")
    custom_domain_config: CustomDomainConfigTypeModel = Field(
        alias="CustomDomainConfig"
    )


class SmsMfaConfigTypeModel(BaseModel):
    sms_authentication_message: Optional[str] = Field(
        default=None, alias="SmsAuthenticationMessage"
    )
    sms_configuration: Optional[SmsConfigurationTypeModel] = Field(
        default=None, alias="SmsConfiguration"
    )


class LambdaConfigTypeModel(BaseModel):
    pre_sign_up: Optional[str] = Field(default=None, alias="PreSignUp")
    custom_message: Optional[str] = Field(default=None, alias="CustomMessage")
    post_confirmation: Optional[str] = Field(default=None, alias="PostConfirmation")
    pre_authentication: Optional[str] = Field(default=None, alias="PreAuthentication")
    post_authentication: Optional[str] = Field(default=None, alias="PostAuthentication")
    define_auth_challenge: Optional[str] = Field(
        default=None, alias="DefineAuthChallenge"
    )
    create_auth_challenge: Optional[str] = Field(
        default=None, alias="CreateAuthChallenge"
    )
    verify_auth_challenge_response: Optional[str] = Field(
        default=None, alias="VerifyAuthChallengeResponse"
    )
    pre_token_generation: Optional[str] = Field(
        default=None, alias="PreTokenGeneration"
    )
    user_migration: Optional[str] = Field(default=None, alias="UserMigration")
    custom_s_ms_sender: Optional[CustomSMSLambdaVersionConfigTypeModel] = Field(
        default=None, alias="CustomSMSSender"
    )
    custom_email_sender: Optional[CustomEmailLambdaVersionConfigTypeModel] = Field(
        default=None, alias="CustomEmailSender"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyID")


class GetUICustomizationResponseModel(BaseModel):
    uicustomization: UICustomizationTypeModel = Field(alias="UICustomization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetUICustomizationResponseModel(BaseModel):
    uicustomization: UICustomizationTypeModel = Field(alias="UICustomization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityProvidersResponseModel(BaseModel):
    providers: List[ProviderDescriptionModel] = Field(alias="Providers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserPoolClientsResponseModel(BaseModel):
    user_pool_clients: List[UserPoolClientDescriptionModel] = Field(
        alias="UserPoolClients"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotifyConfigurationTypeModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    from_: Optional[str] = Field(default=None, alias="From")
    reply_to: Optional[str] = Field(default=None, alias="ReplyTo")
    block_email: Optional[NotifyEmailTypeModel] = Field(
        default=None, alias="BlockEmail"
    )
    no_action_email: Optional[NotifyEmailTypeModel] = Field(
        default=None, alias="NoActionEmail"
    )
    mfa_email: Optional[NotifyEmailTypeModel] = Field(default=None, alias="MfaEmail")


class UserPoolPolicyTypeModel(BaseModel):
    password_policy: Optional[PasswordPolicyTypeModel] = Field(
        default=None, alias="PasswordPolicy"
    )


class SchemaAttributeTypeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    attribute_data_type: Optional[
        Literal["Boolean", "DateTime", "Number", "String"]
    ] = Field(default=None, alias="AttributeDataType")
    developer_only_attribute: Optional[bool] = Field(
        default=None, alias="DeveloperOnlyAttribute"
    )
    mutable: Optional[bool] = Field(default=None, alias="Mutable")
    required: Optional[bool] = Field(default=None, alias="Required")
    number_attribute_constraints: Optional[NumberAttributeConstraintsTypeModel] = Field(
        default=None, alias="NumberAttributeConstraints"
    )
    string_attribute_constraints: Optional[StringAttributeConstraintsTypeModel] = Field(
        default=None, alias="StringAttributeConstraints"
    )


class AdminGetDeviceResponseModel(BaseModel):
    device: DeviceTypeModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminListDevicesResponseModel(BaseModel):
    devices: List[DeviceTypeModel] = Field(alias="Devices")
    pagination_token: str = Field(alias="PaginationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceResponseModel(BaseModel):
    device: DeviceTypeModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesResponseModel(BaseModel):
    devices: List[DeviceTypeModel] = Field(alias="Devices")
    pagination_token: str = Field(alias="PaginationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminCreateUserResponseModel(BaseModel):
    user: UserTypeModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersInGroupResponseModel(BaseModel):
    users: List[UserTypeModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    users: List[UserTypeModel] = Field(alias="Users")
    pagination_token: str = Field(alias="PaginationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminListUserAuthEventsResponseModel(BaseModel):
    auth_events: List[AuthEventTypeModel] = Field(alias="AuthEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminInitiateAuthResponseModel(BaseModel):
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    session: str = Field(alias="Session")
    challenge_parameters: Dict[str, str] = Field(alias="ChallengeParameters")
    authentication_result: AuthenticationResultTypeModel = Field(
        alias="AuthenticationResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminRespondToAuthChallengeResponseModel(BaseModel):
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    session: str = Field(alias="Session")
    challenge_parameters: Dict[str, str] = Field(alias="ChallengeParameters")
    authentication_result: AuthenticationResultTypeModel = Field(
        alias="AuthenticationResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateAuthResponseModel(BaseModel):
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    session: str = Field(alias="Session")
    challenge_parameters: Dict[str, str] = Field(alias="ChallengeParameters")
    authentication_result: AuthenticationResultTypeModel = Field(
        alias="AuthenticationResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RespondToAuthChallengeResponseModel(BaseModel):
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    session: str = Field(alias="Session")
    challenge_parameters: Dict[str, str] = Field(alias="ChallengeParameters")
    authentication_result: AuthenticationResultTypeModel = Field(
        alias="AuthenticationResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdminInitiateAuthRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: str = Field(alias="ClientId")
    auth_flow: Literal[
        "ADMIN_NO_SRP_AUTH",
        "ADMIN_USER_PASSWORD_AUTH",
        "CUSTOM_AUTH",
        "REFRESH_TOKEN",
        "REFRESH_TOKEN_AUTH",
        "USER_PASSWORD_AUTH",
        "USER_SRP_AUTH",
    ] = Field(alias="AuthFlow")
    auth_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="AuthParameters"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    context_data: Optional[ContextDataTypeModel] = Field(
        default=None, alias="ContextData"
    )


class AdminRespondToAuthChallengeRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: str = Field(alias="ClientId")
    challenge_name: Literal[
        "ADMIN_NO_SRP_AUTH",
        "CUSTOM_CHALLENGE",
        "DEVICE_PASSWORD_VERIFIER",
        "DEVICE_SRP_AUTH",
        "MFA_SETUP",
        "NEW_PASSWORD_REQUIRED",
        "PASSWORD_VERIFIER",
        "SELECT_MFA_TYPE",
        "SMS_MFA",
        "SOFTWARE_TOKEN_MFA",
    ] = Field(alias="ChallengeName")
    challenge_responses: Optional[Mapping[str, str]] = Field(
        default=None, alias="ChallengeResponses"
    )
    session: Optional[str] = Field(default=None, alias="Session")
    analytics_metadata: Optional[AnalyticsMetadataTypeModel] = Field(
        default=None, alias="AnalyticsMetadata"
    )
    context_data: Optional[ContextDataTypeModel] = Field(
        default=None, alias="ContextData"
    )
    client_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="ClientMetadata"
    )


class CreateResourceServerResponseModel(BaseModel):
    resource_server: ResourceServerTypeModel = Field(alias="ResourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourceServerResponseModel(BaseModel):
    resource_server: ResourceServerTypeModel = Field(alias="ResourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceServersResponseModel(BaseModel):
    resource_servers: List[ResourceServerTypeModel] = Field(alias="ResourceServers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceServerResponseModel(BaseModel):
    resource_server: ResourceServerTypeModel = Field(alias="ResourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserPoolClientResponseModel(BaseModel):
    user_pool_client: UserPoolClientTypeModel = Field(alias="UserPoolClient")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserPoolClientResponseModel(BaseModel):
    user_pool_client: UserPoolClientTypeModel = Field(alias="UserPoolClient")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserPoolClientResponseModel(BaseModel):
    user_pool_client: UserPoolClientTypeModel = Field(alias="UserPoolClient")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserPoolDomainResponseModel(BaseModel):
    domain_description: DomainDescriptionTypeModel = Field(alias="DomainDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserPoolMfaConfigResponseModel(BaseModel):
    sms_mfa_configuration: SmsMfaConfigTypeModel = Field(alias="SmsMfaConfiguration")
    software_token_mfa_configuration: SoftwareTokenMfaConfigTypeModel = Field(
        alias="SoftwareTokenMfaConfiguration"
    )
    mfa_configuration: Literal["OFF", "ON", "OPTIONAL"] = Field(
        alias="MfaConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetUserPoolMfaConfigRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    sms_mfa_configuration: Optional[SmsMfaConfigTypeModel] = Field(
        default=None, alias="SmsMfaConfiguration"
    )
    software_token_mfa_configuration: Optional[SoftwareTokenMfaConfigTypeModel] = Field(
        default=None, alias="SoftwareTokenMfaConfiguration"
    )
    mfa_configuration: Optional[Literal["OFF", "ON", "OPTIONAL"]] = Field(
        default=None, alias="MfaConfiguration"
    )


class SetUserPoolMfaConfigResponseModel(BaseModel):
    sms_mfa_configuration: SmsMfaConfigTypeModel = Field(alias="SmsMfaConfiguration")
    software_token_mfa_configuration: SoftwareTokenMfaConfigTypeModel = Field(
        alias="SoftwareTokenMfaConfiguration"
    )
    mfa_configuration: Literal["OFF", "ON", "OPTIONAL"] = Field(
        alias="MfaConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserPoolDescriptionTypeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    lambda_config: Optional[LambdaConfigTypeModel] = Field(
        default=None, alias="LambdaConfig"
    )
    status: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Status"
    )
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class AccountTakeoverRiskConfigurationTypeModel(BaseModel):
    actions: AccountTakeoverActionsTypeModel = Field(alias="Actions")
    notify_configuration: Optional[NotifyConfigurationTypeModel] = Field(
        default=None, alias="NotifyConfiguration"
    )


class UpdateUserPoolRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    policies: Optional[UserPoolPolicyTypeModel] = Field(default=None, alias="Policies")
    deletion_protection: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="DeletionProtection"
    )
    lambda_config: Optional[LambdaConfigTypeModel] = Field(
        default=None, alias="LambdaConfig"
    )
    auto_verified_attributes: Optional[
        Sequence[Literal["email", "phone_number"]]
    ] = Field(default=None, alias="AutoVerifiedAttributes")
    sms_verification_message: Optional[str] = Field(
        default=None, alias="SmsVerificationMessage"
    )
    email_verification_message: Optional[str] = Field(
        default=None, alias="EmailVerificationMessage"
    )
    email_verification_subject: Optional[str] = Field(
        default=None, alias="EmailVerificationSubject"
    )
    verification_message_template: Optional[
        VerificationMessageTemplateTypeModel
    ] = Field(default=None, alias="VerificationMessageTemplate")
    sms_authentication_message: Optional[str] = Field(
        default=None, alias="SmsAuthenticationMessage"
    )
    user_attribute_update_settings: Optional[
        UserAttributeUpdateSettingsTypeModel
    ] = Field(default=None, alias="UserAttributeUpdateSettings")
    mfa_configuration: Optional[Literal["OFF", "ON", "OPTIONAL"]] = Field(
        default=None, alias="MfaConfiguration"
    )
    device_configuration: Optional[DeviceConfigurationTypeModel] = Field(
        default=None, alias="DeviceConfiguration"
    )
    email_configuration: Optional[EmailConfigurationTypeModel] = Field(
        default=None, alias="EmailConfiguration"
    )
    sms_configuration: Optional[SmsConfigurationTypeModel] = Field(
        default=None, alias="SmsConfiguration"
    )
    user_pool_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserPoolTags"
    )
    admin_create_user_config: Optional[AdminCreateUserConfigTypeModel] = Field(
        default=None, alias="AdminCreateUserConfig"
    )
    user_pool_add_ons: Optional[UserPoolAddOnsTypeModel] = Field(
        default=None, alias="UserPoolAddOns"
    )
    account_recovery_setting: Optional[AccountRecoverySettingTypeModel] = Field(
        default=None, alias="AccountRecoverySetting"
    )


class AddCustomAttributesRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    custom_attributes: Sequence[SchemaAttributeTypeModel] = Field(
        alias="CustomAttributes"
    )


class CreateUserPoolRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")
    policies: Optional[UserPoolPolicyTypeModel] = Field(default=None, alias="Policies")
    deletion_protection: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="DeletionProtection"
    )
    lambda_config: Optional[LambdaConfigTypeModel] = Field(
        default=None, alias="LambdaConfig"
    )
    auto_verified_attributes: Optional[
        Sequence[Literal["email", "phone_number"]]
    ] = Field(default=None, alias="AutoVerifiedAttributes")
    alias_attributes: Optional[
        Sequence[Literal["email", "phone_number", "preferred_username"]]
    ] = Field(default=None, alias="AliasAttributes")
    username_attributes: Optional[Sequence[Literal["email", "phone_number"]]] = Field(
        default=None, alias="UsernameAttributes"
    )
    sms_verification_message: Optional[str] = Field(
        default=None, alias="SmsVerificationMessage"
    )
    email_verification_message: Optional[str] = Field(
        default=None, alias="EmailVerificationMessage"
    )
    email_verification_subject: Optional[str] = Field(
        default=None, alias="EmailVerificationSubject"
    )
    verification_message_template: Optional[
        VerificationMessageTemplateTypeModel
    ] = Field(default=None, alias="VerificationMessageTemplate")
    sms_authentication_message: Optional[str] = Field(
        default=None, alias="SmsAuthenticationMessage"
    )
    mfa_configuration: Optional[Literal["OFF", "ON", "OPTIONAL"]] = Field(
        default=None, alias="MfaConfiguration"
    )
    user_attribute_update_settings: Optional[
        UserAttributeUpdateSettingsTypeModel
    ] = Field(default=None, alias="UserAttributeUpdateSettings")
    device_configuration: Optional[DeviceConfigurationTypeModel] = Field(
        default=None, alias="DeviceConfiguration"
    )
    email_configuration: Optional[EmailConfigurationTypeModel] = Field(
        default=None, alias="EmailConfiguration"
    )
    sms_configuration: Optional[SmsConfigurationTypeModel] = Field(
        default=None, alias="SmsConfiguration"
    )
    user_pool_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserPoolTags"
    )
    admin_create_user_config: Optional[AdminCreateUserConfigTypeModel] = Field(
        default=None, alias="AdminCreateUserConfig"
    )
    schema_: Optional[Sequence[SchemaAttributeTypeModel]] = Field(
        default=None, alias="Schema"
    )
    user_pool_add_ons: Optional[UserPoolAddOnsTypeModel] = Field(
        default=None, alias="UserPoolAddOns"
    )
    username_configuration: Optional[UsernameConfigurationTypeModel] = Field(
        default=None, alias="UsernameConfiguration"
    )
    account_recovery_setting: Optional[AccountRecoverySettingTypeModel] = Field(
        default=None, alias="AccountRecoverySetting"
    )


class UserPoolTypeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    policies: Optional[UserPoolPolicyTypeModel] = Field(default=None, alias="Policies")
    deletion_protection: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="DeletionProtection"
    )
    lambda_config: Optional[LambdaConfigTypeModel] = Field(
        default=None, alias="LambdaConfig"
    )
    status: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Status"
    )
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    schema_attributes: Optional[List[SchemaAttributeTypeModel]] = Field(
        default=None, alias="SchemaAttributes"
    )
    auto_verified_attributes: Optional[List[Literal["email", "phone_number"]]] = Field(
        default=None, alias="AutoVerifiedAttributes"
    )
    alias_attributes: Optional[
        List[Literal["email", "phone_number", "preferred_username"]]
    ] = Field(default=None, alias="AliasAttributes")
    username_attributes: Optional[List[Literal["email", "phone_number"]]] = Field(
        default=None, alias="UsernameAttributes"
    )
    sms_verification_message: Optional[str] = Field(
        default=None, alias="SmsVerificationMessage"
    )
    email_verification_message: Optional[str] = Field(
        default=None, alias="EmailVerificationMessage"
    )
    email_verification_subject: Optional[str] = Field(
        default=None, alias="EmailVerificationSubject"
    )
    verification_message_template: Optional[
        VerificationMessageTemplateTypeModel
    ] = Field(default=None, alias="VerificationMessageTemplate")
    sms_authentication_message: Optional[str] = Field(
        default=None, alias="SmsAuthenticationMessage"
    )
    user_attribute_update_settings: Optional[
        UserAttributeUpdateSettingsTypeModel
    ] = Field(default=None, alias="UserAttributeUpdateSettings")
    mfa_configuration: Optional[Literal["OFF", "ON", "OPTIONAL"]] = Field(
        default=None, alias="MfaConfiguration"
    )
    device_configuration: Optional[DeviceConfigurationTypeModel] = Field(
        default=None, alias="DeviceConfiguration"
    )
    estimated_number_of_users: Optional[int] = Field(
        default=None, alias="EstimatedNumberOfUsers"
    )
    email_configuration: Optional[EmailConfigurationTypeModel] = Field(
        default=None, alias="EmailConfiguration"
    )
    sms_configuration: Optional[SmsConfigurationTypeModel] = Field(
        default=None, alias="SmsConfiguration"
    )
    user_pool_tags: Optional[Dict[str, str]] = Field(default=None, alias="UserPoolTags")
    sms_configuration_failure: Optional[str] = Field(
        default=None, alias="SmsConfigurationFailure"
    )
    email_configuration_failure: Optional[str] = Field(
        default=None, alias="EmailConfigurationFailure"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    custom_domain: Optional[str] = Field(default=None, alias="CustomDomain")
    admin_create_user_config: Optional[AdminCreateUserConfigTypeModel] = Field(
        default=None, alias="AdminCreateUserConfig"
    )
    user_pool_add_ons: Optional[UserPoolAddOnsTypeModel] = Field(
        default=None, alias="UserPoolAddOns"
    )
    username_configuration: Optional[UsernameConfigurationTypeModel] = Field(
        default=None, alias="UsernameConfiguration"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    account_recovery_setting: Optional[AccountRecoverySettingTypeModel] = Field(
        default=None, alias="AccountRecoverySetting"
    )


class ListUserPoolsResponseModel(BaseModel):
    user_pools: List[UserPoolDescriptionTypeModel] = Field(alias="UserPools")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RiskConfigurationTypeModel(BaseModel):
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    compromised_credentials_risk_configuration: Optional[
        CompromisedCredentialsRiskConfigurationTypeModel
    ] = Field(default=None, alias="CompromisedCredentialsRiskConfiguration")
    account_takeover_risk_configuration: Optional[
        AccountTakeoverRiskConfigurationTypeModel
    ] = Field(default=None, alias="AccountTakeoverRiskConfiguration")
    risk_exception_configuration: Optional[RiskExceptionConfigurationTypeModel] = Field(
        default=None, alias="RiskExceptionConfiguration"
    )
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )


class SetRiskConfigurationRequestModel(BaseModel):
    user_pool_id: str = Field(alias="UserPoolId")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    compromised_credentials_risk_configuration: Optional[
        CompromisedCredentialsRiskConfigurationTypeModel
    ] = Field(default=None, alias="CompromisedCredentialsRiskConfiguration")
    account_takeover_risk_configuration: Optional[
        AccountTakeoverRiskConfigurationTypeModel
    ] = Field(default=None, alias="AccountTakeoverRiskConfiguration")
    risk_exception_configuration: Optional[RiskExceptionConfigurationTypeModel] = Field(
        default=None, alias="RiskExceptionConfiguration"
    )


class CreateUserPoolResponseModel(BaseModel):
    user_pool: UserPoolTypeModel = Field(alias="UserPool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserPoolResponseModel(BaseModel):
    user_pool: UserPoolTypeModel = Field(alias="UserPool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRiskConfigurationResponseModel(BaseModel):
    risk_configuration: RiskConfigurationTypeModel = Field(alias="RiskConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetRiskConfigurationResponseModel(BaseModel):
    risk_configuration: RiskConfigurationTypeModel = Field(alias="RiskConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
