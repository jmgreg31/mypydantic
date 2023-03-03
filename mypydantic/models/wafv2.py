# Model Generated: Thu Mar  2 21:56:24 2023

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


class AWSManagedRulesBotControlRuleSetModel(BaseModel):
    inspection_level: Literal["COMMON", "TARGETED"] = Field(alias="InspectionLevel")


class ActionConditionModel(BaseModel):
    action: Literal[
        "ALLOW", "BLOCK", "CAPTCHA", "CHALLENGE", "COUNT", "EXCLUDED_AS_COUNT"
    ] = Field(alias="Action")


class AndStatementModel(BaseModel):
    statements: Sequence[StatementModel] = Field(alias="Statements")


class AssociateWebACLRequestModel(BaseModel):
    web_acl_arn: str = Field(alias="WebACLArn")
    resource_arn: str = Field(alias="ResourceArn")


class BodyModel(BaseModel):
    oversize_handling: Optional[Literal["CONTINUE", "MATCH", "NO_MATCH"]] = Field(
        default=None, alias="OversizeHandling"
    )


class TextTransformationModel(BaseModel):
    priority: int = Field(alias="Priority")
    type: Literal[
        "BASE64_DECODE",
        "BASE64_DECODE_EXT",
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "CSS_DECODE",
        "ESCAPE_SEQ_DECODE",
        "HEX_DECODE",
        "HTML_ENTITY_DECODE",
        "JS_DECODE",
        "LOWERCASE",
        "MD5",
        "NONE",
        "NORMALIZE_PATH",
        "NORMALIZE_PATH_WIN",
        "REMOVE_NULLS",
        "REPLACE_COMMENTS",
        "REPLACE_NULLS",
        "SQL_HEX_DECODE",
        "URL_DECODE",
        "URL_DECODE_UNI",
        "UTF8_TO_UNICODE",
    ] = Field(alias="Type")


class ImmunityTimePropertyModel(BaseModel):
    immunity_time: int = Field(alias="ImmunityTime")


class CaptchaResponseModel(BaseModel):
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    solve_timestamp: Optional[int] = Field(default=None, alias="SolveTimestamp")
    failure_reason: Optional[
        Literal[
            "TOKEN_DOMAIN_MISMATCH", "TOKEN_EXPIRED", "TOKEN_INVALID", "TOKEN_MISSING"
        ]
    ] = Field(default=None, alias="FailureReason")


class ChallengeResponseModel(BaseModel):
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    solve_timestamp: Optional[int] = Field(default=None, alias="SolveTimestamp")
    failure_reason: Optional[
        Literal[
            "TOKEN_DOMAIN_MISMATCH", "TOKEN_EXPIRED", "TOKEN_INVALID", "TOKEN_MISSING"
        ]
    ] = Field(default=None, alias="FailureReason")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class LabelNameConditionModel(BaseModel):
    label_name: str = Field(alias="LabelName")


class CookieMatchPatternModel(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_cookies: Optional[Sequence[str]] = Field(
        default=None, alias="IncludedCookies"
    )
    excluded_cookies: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedCookies"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class IPSetSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class RegexModel(BaseModel):
    regex_string: Optional[str] = Field(default=None, alias="RegexString")


class RegexPatternSetSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class CustomResponseBodyModel(BaseModel):
    content_type: Literal["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"] = Field(
        alias="ContentType"
    )
    content: str = Field(alias="Content")


class VisibilityConfigModel(BaseModel):
    sampled_requests_enabled: bool = Field(alias="SampledRequestsEnabled")
    cloud_watch_metrics_enabled: bool = Field(alias="CloudWatchMetricsEnabled")
    metric_name: str = Field(alias="MetricName")


class RuleGroupSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class WebACLSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class CustomHTTPHeaderModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DeleteFirewallManagerRuleGroupsRequestModel(BaseModel):
    web_acl_arn: str = Field(alias="WebACLArn")
    web_acl_lock_token: str = Field(alias="WebACLLockToken")


class DeleteIPSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteLoggingConfigurationRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeletePermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteRegexPatternSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteRuleGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteWebACLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DescribeManagedRuleGroupRequestModel(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    version_name: Optional[str] = Field(default=None, alias="VersionName")


class LabelSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class DisassociateWebACLRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ExcludedRuleModel(BaseModel):
    name: str = Field(alias="Name")


class SingleHeaderModel(BaseModel):
    name: str = Field(alias="Name")


class SingleQueryArgumentModel(BaseModel):
    name: str = Field(alias="Name")


class ForwardedIPConfigModel(BaseModel):
    header_name: str = Field(alias="HeaderName")
    fallback_behavior: Literal["MATCH", "NO_MATCH"] = Field(alias="FallbackBehavior")


class GenerateMobileSdkReleaseUrlRequestModel(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    release_version: str = Field(alias="ReleaseVersion")


class GetIPSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class IPSetModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    ip_address_version: Literal["IPV4", "IPV6"] = Field(alias="IPAddressVersion")
    addresses: List[str] = Field(alias="Addresses")
    description: Optional[str] = Field(default=None, alias="Description")


class GetLoggingConfigurationRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetManagedRuleSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class GetMobileSdkReleaseRequestModel(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    release_version: str = Field(alias="ReleaseVersion")


class GetPermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetRateBasedStatementManagedKeysRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    web_acl_name: str = Field(alias="WebACLName")
    web_acl_id: str = Field(alias="WebACLId")
    rule_name: str = Field(alias="RuleName")
    rule_group_rule_name: Optional[str] = Field(default=None, alias="RuleGroupRuleName")


class RateBasedStatementManagedKeysIPSetModel(BaseModel):
    ip_address_version: Optional[Literal["IPV4", "IPV6"]] = Field(
        default=None, alias="IPAddressVersion"
    )
    addresses: Optional[List[str]] = Field(default=None, alias="Addresses")


class GetRegexPatternSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class GetRuleGroupRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    scope: Optional[Literal["CLOUDFRONT", "REGIONAL"]] = Field(
        default=None, alias="Scope"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")


class TimeWindowModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class GetWebACLForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetWebACLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class HTTPHeaderModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class HeaderMatchPatternModel(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_headers: Optional[Sequence[str]] = Field(
        default=None, alias="IncludedHeaders"
    )
    excluded_headers: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedHeaders"
    )


class IPSetForwardedIPConfigModel(BaseModel):
    header_name: str = Field(alias="HeaderName")
    fallback_behavior: Literal["MATCH", "NO_MATCH"] = Field(alias="FallbackBehavior")
    position: Literal["ANY", "FIRST", "LAST"] = Field(alias="Position")


class JsonMatchPatternModel(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_paths: Optional[Sequence[str]] = Field(default=None, alias="IncludedPaths")


class LabelMatchStatementModel(BaseModel):
    scope: Literal["LABEL", "NAMESPACE"] = Field(alias="Scope")
    key: str = Field(alias="Key")


class LabelModel(BaseModel):
    name: str = Field(alias="Name")


class ListAvailableManagedRuleGroupVersionsRequestModel(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleGroupVersionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )


class ListAvailableManagedRuleGroupsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleGroupSummaryModel(BaseModel):
    vendor_name: Optional[str] = Field(default=None, alias="VendorName")
    name: Optional[str] = Field(default=None, alias="Name")
    versioning_supported: Optional[bool] = Field(
        default=None, alias="VersioningSupported"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ListIPSetsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListLoggingConfigurationsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListManagedRuleSetsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleSetSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")


class ListMobileSdkReleasesRequestModel(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ReleaseSummaryModel(BaseModel):
    release_version: Optional[str] = Field(default=None, alias="ReleaseVersion")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class ListRegexPatternSetsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListResourcesForWebACLRequestModel(BaseModel):
    web_acl_arn: str = Field(alias="WebACLArn")
    resource_type: Optional[
        Literal[
            "API_GATEWAY",
            "APPLICATION_LOAD_BALANCER",
            "APPSYNC",
            "APP_RUNNER_SERVICE",
            "COGNITO_USER_POOL",
        ]
    ] = Field(default=None, alias="ResourceType")


class ListRuleGroupsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListWebACLsRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PasswordFieldModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class UsernameFieldModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class ManagedRuleSetVersionModel(BaseModel):
    associated_rule_group_arn: Optional[str] = Field(
        default=None, alias="AssociatedRuleGroupArn"
    )
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    forecasted_lifetime: Optional[int] = Field(default=None, alias="ForecastedLifetime")
    publish_timestamp: Optional[datetime] = Field(
        default=None, alias="PublishTimestamp"
    )
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )
    expiry_timestamp: Optional[datetime] = Field(default=None, alias="ExpiryTimestamp")


class NotStatementModel(BaseModel):
    statement: Dict[str, Any] = Field(alias="Statement")


class OrStatementModel(BaseModel):
    statements: Sequence[StatementModel] = Field(alias="Statements")


class VersionToPublishModel(BaseModel):
    associated_rule_group_arn: Optional[str] = Field(
        default=None, alias="AssociatedRuleGroupArn"
    )
    forecasted_lifetime: Optional[int] = Field(default=None, alias="ForecastedLifetime")


class PutPermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")


class ResponseInspectionBodyContainsModel(BaseModel):
    success_strings: Sequence[str] = Field(alias="SuccessStrings")
    failure_strings: Sequence[str] = Field(alias="FailureStrings")


class ResponseInspectionHeaderModel(BaseModel):
    name: str = Field(alias="Name")
    success_values: Sequence[str] = Field(alias="SuccessValues")
    failure_values: Sequence[str] = Field(alias="FailureValues")


class ResponseInspectionJsonModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    success_values: Sequence[str] = Field(alias="SuccessValues")
    failure_values: Sequence[str] = Field(alias="FailureValues")


class ResponseInspectionStatusCodeModel(BaseModel):
    success_codes: Sequence[int] = Field(alias="SuccessCodes")
    failure_codes: Sequence[int] = Field(alias="FailureCodes")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateIPSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    addresses: Sequence[str] = Field(alias="Addresses")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateManagedRuleSetVersionExpiryDateRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")
    version_to_expire: str = Field(alias="VersionToExpire")
    expiry_timestamp: Union[datetime, str] = Field(alias="ExpiryTimestamp")


class CaptchaConfigModel(BaseModel):
    immunity_time_property: Optional[ImmunityTimePropertyModel] = Field(
        default=None, alias="ImmunityTimeProperty"
    )


class ChallengeConfigModel(BaseModel):
    immunity_time_property: Optional[ImmunityTimePropertyModel] = Field(
        default=None, alias="ImmunityTimeProperty"
    )


class CheckCapacityResponseModel(BaseModel):
    capacity: int = Field(alias="Capacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallManagerRuleGroupsResponseModel(BaseModel):
    next_web_acl_lock_token: str = Field(alias="NextWebACLLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateMobileSdkReleaseUrlResponseModel(BaseModel):
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPermissionPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesForWebACLResponseModel(BaseModel):
    resource_arns: List[str] = Field(alias="ResourceArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutManagedRuleSetVersionsResponseModel(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIPSetResponseModel(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateManagedRuleSetVersionExpiryDateResponseModel(BaseModel):
    expiring_version: str = Field(alias="ExpiringVersion")
    expiry_timestamp: datetime = Field(alias="ExpiryTimestamp")
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegexPatternSetResponseModel(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleGroupResponseModel(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWebACLResponseModel(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConditionModel(BaseModel):
    action_condition: Optional[ActionConditionModel] = Field(
        default=None, alias="ActionCondition"
    )
    label_name_condition: Optional[LabelNameConditionModel] = Field(
        default=None, alias="LabelNameCondition"
    )


class CookiesModel(BaseModel):
    match_pattern: CookieMatchPatternModel = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    oversize_handling: Literal["CONTINUE", "MATCH", "NO_MATCH"] = Field(
        alias="OversizeHandling"
    )


class CreateIPSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    ip_address_version: Literal["IPV4", "IPV6"] = Field(alias="IPAddressVersion")
    addresses: Sequence[str] = Field(alias="Addresses")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MobileSdkReleaseModel(BaseModel):
    release_version: Optional[str] = Field(default=None, alias="ReleaseVersion")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    release_notes: Optional[str] = Field(default=None, alias="ReleaseNotes")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class TagInfoForResourceModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateIPSetResponseModel(BaseModel):
    summary: IPSetSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIPSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    ip_sets: List[IPSetSummaryModel] = Field(alias="IPSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRegexPatternSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    regular_expression_list: Sequence[RegexModel] = Field(alias="RegularExpressionList")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class RegexPatternSetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")
    description: Optional[str] = Field(default=None, alias="Description")
    regular_expression_list: Optional[List[RegexModel]] = Field(
        default=None, alias="RegularExpressionList"
    )


class UpdateRegexPatternSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    regular_expression_list: Sequence[RegexModel] = Field(alias="RegularExpressionList")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateRegexPatternSetResponseModel(BaseModel):
    summary: RegexPatternSetSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRegexPatternSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    regex_pattern_sets: List[RegexPatternSetSummaryModel] = Field(
        alias="RegexPatternSets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleGroupResponseModel(BaseModel):
    summary: RuleGroupSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRuleGroupsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rule_groups: List[RuleGroupSummaryModel] = Field(alias="RuleGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWebACLResponseModel(BaseModel):
    summary: WebACLSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebACLsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    web_acls: List[WebACLSummaryModel] = Field(alias="WebACLs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomRequestHandlingModel(BaseModel):
    insert_headers: Sequence[CustomHTTPHeaderModel] = Field(alias="InsertHeaders")


class CustomResponseModel(BaseModel):
    response_code: int = Field(alias="ResponseCode")
    custom_response_body_key: Optional[str] = Field(
        default=None, alias="CustomResponseBodyKey"
    )
    response_headers: Optional[Sequence[CustomHTTPHeaderModel]] = Field(
        default=None, alias="ResponseHeaders"
    )


class GeoMatchStatementModel(BaseModel):
    country_codes: Optional[
        Sequence[
            Literal[
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AO",
                "AQ",
                "AR",
                "AS",
                "AT",
                "AU",
                "AW",
                "AX",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BQ",
                "BR",
                "BS",
                "BT",
                "BV",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CC",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CU",
                "CV",
                "CW",
                "CX",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FM",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GF",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GP",
                "GQ",
                "GR",
                "GS",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HM",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "Type[IO]",
                "IQ",
                "IR",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KP",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MH",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MP",
                "MQ",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NF",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PS",
                "PT",
                "PW",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SD",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "SS",
                "ST",
                "SV",
                "SX",
                "SY",
                "SZ",
                "TC",
                "TD",
                "TF",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "UM",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VI",
                "VN",
                "VU",
                "WF",
                "WS",
                "XK",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
            ]
        ]
    ] = Field(default=None, alias="CountryCodes")
    forwarded_ip_config: Optional[ForwardedIPConfigModel] = Field(
        default=None, alias="ForwardedIPConfig"
    )


class RateBasedStatementModel(BaseModel):
    limit: int = Field(alias="Limit")
    aggregate_key_type: Literal["FORWARDED_IP", "IP"] = Field(alias="AggregateKeyType")
    scope_down_statement: Optional[StatementModel] = Field(
        default=None, alias="ScopeDownStatement"
    )
    forwarded_ip_config: Optional[ForwardedIPConfigModel] = Field(
        default=None, alias="ForwardedIPConfig"
    )


class GetIPSetResponseModel(BaseModel):
    ip_set: IPSetModel = Field(alias="IPSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRateBasedStatementManagedKeysResponseModel(BaseModel):
    managed_keys_ip_v4: RateBasedStatementManagedKeysIPSetModel = Field(
        alias="ManagedKeysIPV4"
    )
    managed_keys_ip_v6: RateBasedStatementManagedKeysIPSetModel = Field(
        alias="ManagedKeysIPV6"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSampledRequestsRequestModel(BaseModel):
    web_acl_arn: str = Field(alias="WebAclArn")
    rule_metric_name: str = Field(alias="RuleMetricName")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    time_window: TimeWindowModel = Field(alias="TimeWindow")
    max_items: int = Field(alias="MaxItems")


class HTTPRequestModel(BaseModel):
    client_ip: Optional[str] = Field(default=None, alias="ClientIP")
    country: Optional[str] = Field(default=None, alias="Country")
    uri: Optional[str] = Field(default=None, alias="URI")
    method: Optional[str] = Field(default=None, alias="Method")
    http_version: Optional[str] = Field(default=None, alias="HTTPVersion")
    headers: Optional[List[HTTPHeaderModel]] = Field(default=None, alias="Headers")


class HeadersModel(BaseModel):
    match_pattern: HeaderMatchPatternModel = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    oversize_handling: Literal["CONTINUE", "MATCH", "NO_MATCH"] = Field(
        alias="OversizeHandling"
    )


class IPSetReferenceStatementModel(BaseModel):
    arn: str = Field(alias="ARN")
    ip_set_forwarded_ip_config: Optional[IPSetForwardedIPConfigModel] = Field(
        default=None, alias="IPSetForwardedIPConfig"
    )


class JsonBodyModel(BaseModel):
    match_pattern: JsonMatchPatternModel = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    invalid_fallback_behavior: Optional[
        Literal["EVALUATE_AS_STRING", "MATCH", "NO_MATCH"]
    ] = Field(default=None, alias="InvalidFallbackBehavior")
    oversize_handling: Optional[Literal["CONTINUE", "MATCH", "NO_MATCH"]] = Field(
        default=None, alias="OversizeHandling"
    )


class ListAvailableManagedRuleGroupVersionsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    versions: List[ManagedRuleGroupVersionModel] = Field(alias="Versions")
    current_default_version: str = Field(alias="CurrentDefaultVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableManagedRuleGroupsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    managed_rule_groups: List[ManagedRuleGroupSummaryModel] = Field(
        alias="ManagedRuleGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedRuleSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    managed_rule_sets: List[ManagedRuleSetSummaryModel] = Field(alias="ManagedRuleSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMobileSdkReleasesResponseModel(BaseModel):
    release_summaries: List[ReleaseSummaryModel] = Field(alias="ReleaseSummaries")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestInspectionModel(BaseModel):
    payload_type: Literal["FORM_ENCODED", "JSON"] = Field(alias="PayloadType")
    username_field: UsernameFieldModel = Field(alias="UsernameField")
    password_field: PasswordFieldModel = Field(alias="PasswordField")


class ManagedRuleSetModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    description: Optional[str] = Field(default=None, alias="Description")
    published_versions: Optional[Dict[str, ManagedRuleSetVersionModel]] = Field(
        default=None, alias="PublishedVersions"
    )
    recommended_version: Optional[str] = Field(default=None, alias="RecommendedVersion")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")


class PutManagedRuleSetVersionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")
    recommended_version: Optional[str] = Field(default=None, alias="RecommendedVersion")
    versions_to_publish: Optional[Mapping[str, VersionToPublishModel]] = Field(
        default=None, alias="VersionsToPublish"
    )


class ResponseInspectionModel(BaseModel):
    status_code: Optional[ResponseInspectionStatusCodeModel] = Field(
        default=None, alias="StatusCode"
    )
    header: Optional[ResponseInspectionHeaderModel] = Field(
        default=None, alias="Header"
    )
    body_contains: Optional[ResponseInspectionBodyContainsModel] = Field(
        default=None, alias="BodyContains"
    )
    json_: Optional[ResponseInspectionJsonModel] = Field(default=None, alias="Json")


class FilterModel(BaseModel):
    behavior: Literal["DROP", "KEEP"] = Field(alias="Behavior")
    requirement: Literal["MEETS_ALL", "MEETS_ANY"] = Field(alias="Requirement")
    conditions: List[ConditionModel] = Field(alias="Conditions")


class GetMobileSdkReleaseResponseModel(BaseModel):
    mobile_sdk_release: MobileSdkReleaseModel = Field(alias="MobileSdkRelease")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    tag_info_for_resource: TagInfoForResourceModel = Field(alias="TagInfoForResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegexPatternSetResponseModel(BaseModel):
    regex_pattern_set: RegexPatternSetModel = Field(alias="RegexPatternSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AllowActionModel(BaseModel):
    custom_request_handling: Optional[CustomRequestHandlingModel] = Field(
        default=None, alias="CustomRequestHandling"
    )


class CaptchaActionModel(BaseModel):
    custom_request_handling: Optional[CustomRequestHandlingModel] = Field(
        default=None, alias="CustomRequestHandling"
    )


class ChallengeActionModel(BaseModel):
    custom_request_handling: Optional[CustomRequestHandlingModel] = Field(
        default=None, alias="CustomRequestHandling"
    )


class CountActionModel(BaseModel):
    custom_request_handling: Optional[CustomRequestHandlingModel] = Field(
        default=None, alias="CustomRequestHandling"
    )


class BlockActionModel(BaseModel):
    custom_response: Optional[CustomResponseModel] = Field(
        default=None, alias="CustomResponse"
    )


class SampledHTTPRequestModel(BaseModel):
    request: HTTPRequestModel = Field(alias="Request")
    weight: int = Field(alias="Weight")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    action: Optional[str] = Field(default=None, alias="Action")
    rule_name_within_rule_group: Optional[str] = Field(
        default=None, alias="RuleNameWithinRuleGroup"
    )
    request_headers_inserted: Optional[List[HTTPHeaderModel]] = Field(
        default=None, alias="RequestHeadersInserted"
    )
    response_code_sent: Optional[int] = Field(default=None, alias="ResponseCodeSent")
    labels: Optional[List[LabelModel]] = Field(default=None, alias="Labels")
    captcha_response: Optional[CaptchaResponseModel] = Field(
        default=None, alias="CaptchaResponse"
    )
    challenge_response: Optional[ChallengeResponseModel] = Field(
        default=None, alias="ChallengeResponse"
    )
    overridden_action: Optional[str] = Field(default=None, alias="OverriddenAction")


class FieldToMatchModel(BaseModel):
    single_header: Optional[SingleHeaderModel] = Field(
        default=None, alias="SingleHeader"
    )
    single_query_argument: Optional[SingleQueryArgumentModel] = Field(
        default=None, alias="SingleQueryArgument"
    )
    all_query_arguments: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AllQueryArguments"
    )
    uri_path: Optional[Mapping[str, Any]] = Field(default=None, alias="UriPath")
    query_string: Optional[Mapping[str, Any]] = Field(default=None, alias="QueryString")
    body: Optional[BodyModel] = Field(default=None, alias="Body")
    method: Optional[Mapping[str, Any]] = Field(default=None, alias="Method")
    json_body: Optional[JsonBodyModel] = Field(default=None, alias="JsonBody")
    headers: Optional[HeadersModel] = Field(default=None, alias="Headers")
    cookies: Optional[CookiesModel] = Field(default=None, alias="Cookies")


class GetManagedRuleSetResponseModel(BaseModel):
    managed_rule_set: ManagedRuleSetModel = Field(alias="ManagedRuleSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AWSManagedRulesATPRuleSetModel(BaseModel):
    login_path: str = Field(alias="LoginPath")
    request_inspection: Optional[RequestInspectionModel] = Field(
        default=None, alias="RequestInspection"
    )
    response_inspection: Optional[ResponseInspectionModel] = Field(
        default=None, alias="ResponseInspection"
    )


class LoggingFilterModel(BaseModel):
    filters: List[FilterModel] = Field(alias="Filters")
    default_behavior: Literal["DROP", "KEEP"] = Field(alias="DefaultBehavior")


class OverrideActionModel(BaseModel):
    count: Optional[CountActionModel] = Field(default=None, alias="Count")
    none_: Optional[Mapping[str, Any]] = Field(default=None, alias="None")


class DefaultActionModel(BaseModel):
    block: Optional[BlockActionModel] = Field(default=None, alias="Block")
    allow: Optional[AllowActionModel] = Field(default=None, alias="Allow")


class RuleActionModel(BaseModel):
    block: Optional[BlockActionModel] = Field(default=None, alias="Block")
    allow: Optional[AllowActionModel] = Field(default=None, alias="Allow")
    count: Optional[CountActionModel] = Field(default=None, alias="Count")
    captcha: Optional[CaptchaActionModel] = Field(default=None, alias="Captcha")
    challenge: Optional[ChallengeActionModel] = Field(default=None, alias="Challenge")


class GetSampledRequestsResponseModel(BaseModel):
    sampled_requests: List[SampledHTTPRequestModel] = Field(alias="SampledRequests")
    population_size: int = Field(alias="PopulationSize")
    time_window: TimeWindowModel = Field(alias="TimeWindow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ByteMatchStatementModel(BaseModel):
    search_string: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="SearchString"
    )
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )
    positional_constraint: Literal[
        "CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"
    ] = Field(alias="PositionalConstraint")


class RegexMatchStatementModel(BaseModel):
    regex_string: str = Field(alias="RegexString")
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )


class RegexPatternSetReferenceStatementModel(BaseModel):
    arn: str = Field(alias="ARN")
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )


class SizeConstraintStatementModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    comparison_operator: Literal["EQ", "GE", "GT", "LE", "LT", "NE"] = Field(
        alias="ComparisonOperator"
    )
    size: int = Field(alias="Size")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )


class SqliMatchStatementModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )
    sensitivity_level: Optional[Literal["HIGH", "LOW"]] = Field(
        default=None, alias="SensitivityLevel"
    )


class XssMatchStatementModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformationModel] = Field(
        alias="TextTransformations"
    )


class ManagedRuleGroupConfigModel(BaseModel):
    login_path: Optional[str] = Field(default=None, alias="LoginPath")
    payload_type: Optional[Literal["FORM_ENCODED", "JSON"]] = Field(
        default=None, alias="PayloadType"
    )
    username_field: Optional[UsernameFieldModel] = Field(
        default=None, alias="UsernameField"
    )
    password_field: Optional[PasswordFieldModel] = Field(
        default=None, alias="PasswordField"
    )
    aws_managed_rules_bot_control_rule_set: Optional[
        AWSManagedRulesBotControlRuleSetModel
    ] = Field(default=None, alias="AWSManagedRulesBotControlRuleSet")
    aws_managed_rules_atp_rule_set: Optional[AWSManagedRulesATPRuleSetModel] = Field(
        default=None, alias="AWSManagedRulesATPRuleSet"
    )


class LoggingConfigurationModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    log_destination_configs: List[str] = Field(alias="LogDestinationConfigs")
    redacted_fields: Optional[List[FieldToMatchModel]] = Field(
        default=None, alias="RedactedFields"
    )
    managed_by_firewall_manager: Optional[bool] = Field(
        default=None, alias="ManagedByFirewallManager"
    )
    logging_filter: Optional[LoggingFilterModel] = Field(
        default=None, alias="LoggingFilter"
    )


class RuleActionOverrideModel(BaseModel):
    name: str = Field(alias="Name")
    action_to_use: RuleActionModel = Field(alias="ActionToUse")


class RuleSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    action: Optional[RuleActionModel] = Field(default=None, alias="Action")


class RuleModel(BaseModel):
    name: str = Field(alias="Name")
    priority: int = Field(alias="Priority")
    statement: StatementModel = Field(alias="Statement")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    action: Optional[RuleActionModel] = Field(default=None, alias="Action")
    override_action: Optional[OverrideActionModel] = Field(
        default=None, alias="OverrideAction"
    )
    rule_labels: Optional[Sequence[LabelModel]] = Field(
        default=None, alias="RuleLabels"
    )
    captcha_config: Optional[CaptchaConfigModel] = Field(
        default=None, alias="CaptchaConfig"
    )
    challenge_config: Optional[ChallengeConfigModel] = Field(
        default=None, alias="ChallengeConfig"
    )


class GetLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLoggingConfigurationsResponseModel(BaseModel):
    logging_configurations: List[LoggingConfigurationModel] = Field(
        alias="LoggingConfigurations"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingConfigurationRequestModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )


class PutLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ManagedRuleGroupStatementModel(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    excluded_rules: Optional[Sequence[ExcludedRuleModel]] = Field(
        default=None, alias="ExcludedRules"
    )
    scope_down_statement: Optional[StatementModel] = Field(
        default=None, alias="ScopeDownStatement"
    )
    managed_rule_group_configs: Optional[Sequence[ManagedRuleGroupConfigModel]] = Field(
        default=None, alias="ManagedRuleGroupConfigs"
    )
    rule_action_overrides: Optional[Sequence[RuleActionOverrideModel]] = Field(
        default=None, alias="RuleActionOverrides"
    )


class RuleGroupReferenceStatementModel(BaseModel):
    arn: str = Field(alias="ARN")
    excluded_rules: Optional[Sequence[ExcludedRuleModel]] = Field(
        default=None, alias="ExcludedRules"
    )
    rule_action_overrides: Optional[Sequence[RuleActionOverrideModel]] = Field(
        default=None, alias="RuleActionOverrides"
    )


class DescribeManagedRuleGroupResponseModel(BaseModel):
    version_name: str = Field(alias="VersionName")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    capacity: int = Field(alias="Capacity")
    rules: List[RuleSummaryModel] = Field(alias="Rules")
    label_namespace: str = Field(alias="LabelNamespace")
    available_labels: List[LabelSummaryModel] = Field(alias="AvailableLabels")
    consumed_labels: List[LabelSummaryModel] = Field(alias="ConsumedLabels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckCapacityRequestModel(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    rules: Sequence[RuleModel] = Field(alias="Rules")


class CreateRuleGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    capacity: int = Field(alias="Capacity")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[RuleModel]] = Field(default=None, alias="Rules")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )


class CreateWebACLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    default_action: DefaultActionModel = Field(alias="DefaultAction")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[RuleModel]] = Field(default=None, alias="Rules")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfigModel] = Field(
        default=None, alias="CaptchaConfig"
    )
    challenge_config: Optional[ChallengeConfigModel] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[Sequence[str]] = Field(default=None, alias="TokenDomains")


class RuleGroupModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    capacity: int = Field(alias="Capacity")
    arn: str = Field(alias="ARN")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[List[RuleModel]] = Field(default=None, alias="Rules")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")
    custom_response_bodies: Optional[Dict[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    available_labels: Optional[List[LabelSummaryModel]] = Field(
        default=None, alias="AvailableLabels"
    )
    consumed_labels: Optional[List[LabelSummaryModel]] = Field(
        default=None, alias="ConsumedLabels"
    )


class UpdateRuleGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[RuleModel]] = Field(default=None, alias="Rules")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )


class UpdateWebACLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    default_action: DefaultActionModel = Field(alias="DefaultAction")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[RuleModel]] = Field(default=None, alias="Rules")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfigModel] = Field(
        default=None, alias="CaptchaConfig"
    )
    challenge_config: Optional[ChallengeConfigModel] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[Sequence[str]] = Field(default=None, alias="TokenDomains")


class FirewallManagerStatementModel(BaseModel):
    managed_rule_group_statement: Optional[ManagedRuleGroupStatementModel] = Field(
        default=None, alias="ManagedRuleGroupStatement"
    )
    rule_group_reference_statement: Optional[RuleGroupReferenceStatementModel] = Field(
        default=None, alias="RuleGroupReferenceStatement"
    )


class StatementModel(BaseModel):
    byte_match_statement: Optional[ByteMatchStatementModel] = Field(
        default=None, alias="ByteMatchStatement"
    )
    sqli_match_statement: Optional[SqliMatchStatementModel] = Field(
        default=None, alias="SqliMatchStatement"
    )
    xss_match_statement: Optional[XssMatchStatementModel] = Field(
        default=None, alias="XssMatchStatement"
    )
    size_constraint_statement: Optional[SizeConstraintStatementModel] = Field(
        default=None, alias="SizeConstraintStatement"
    )
    geo_match_statement: Optional[GeoMatchStatementModel] = Field(
        default=None, alias="GeoMatchStatement"
    )
    rule_group_reference_statement: Optional[RuleGroupReferenceStatementModel] = Field(
        default=None, alias="RuleGroupReferenceStatement"
    )
    ip_set_reference_statement: Optional[IPSetReferenceStatementModel] = Field(
        default=None, alias="IPSetReferenceStatement"
    )
    regex_pattern_set_reference_statement: Optional[
        RegexPatternSetReferenceStatementModel
    ] = Field(default=None, alias="RegexPatternSetReferenceStatement")
    rate_based_statement: Optional[Dict[str, Any]] = Field(
        default=None, alias="RateBasedStatement"
    )
    and_statement: Optional[Dict[str, Any]] = Field(default=None, alias="AndStatement")
    or_statement: Optional[Dict[str, Any]] = Field(default=None, alias="OrStatement")
    not_statement: Optional[Dict[str, Any]] = Field(default=None, alias="NotStatement")
    managed_rule_group_statement: Optional[Dict[str, Any]] = Field(
        default=None, alias="ManagedRuleGroupStatement"
    )
    label_match_statement: Optional[LabelMatchStatementModel] = Field(
        default=None, alias="LabelMatchStatement"
    )
    regex_match_statement: Optional[RegexMatchStatementModel] = Field(
        default=None, alias="RegexMatchStatement"
    )


class GetRuleGroupResponseModel(BaseModel):
    rule_group: RuleGroupModel = Field(alias="RuleGroup")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FirewallManagerRuleGroupModel(BaseModel):
    name: str = Field(alias="Name")
    priority: int = Field(alias="Priority")
    firewall_manager_statement: FirewallManagerStatementModel = Field(
        alias="FirewallManagerStatement"
    )
    override_action: OverrideActionModel = Field(alias="OverrideAction")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")


class WebACLModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    default_action: DefaultActionModel = Field(alias="DefaultAction")
    visibility_config: VisibilityConfigModel = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[List[RuleModel]] = Field(default=None, alias="Rules")
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    pre_process_firewall_manager_rule_groups: Optional[
        List[FirewallManagerRuleGroupModel]
    ] = Field(default=None, alias="PreProcessFirewallManagerRuleGroups")
    post_process_firewall_manager_rule_groups: Optional[
        List[FirewallManagerRuleGroupModel]
    ] = Field(default=None, alias="PostProcessFirewallManagerRuleGroups")
    managed_by_firewall_manager: Optional[bool] = Field(
        default=None, alias="ManagedByFirewallManager"
    )
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")
    custom_response_bodies: Optional[Dict[str, CustomResponseBodyModel]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfigModel] = Field(
        default=None, alias="CaptchaConfig"
    )
    challenge_config: Optional[ChallengeConfigModel] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[List[str]] = Field(default=None, alias="TokenDomains")


class GetWebACLForResourceResponseModel(BaseModel):
    web_acl: WebACLModel = Field(alias="WebACL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWebACLResponseModel(BaseModel):
    web_acl: WebACLModel = Field(alias="WebACL")
    lock_token: str = Field(alias="LockToken")
    application_integration_url: str = Field(alias="ApplicationIntegrationURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
