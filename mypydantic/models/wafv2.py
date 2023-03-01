# Model Generated: Wed Mar  1 11:15:22 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    IO,
    Any,
    Dict,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Union,
    Type,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AWSManagedRulesBotControlRuleSet(BaseModel):
    inspection_level: Literal["COMMON", "TARGETED"] = Field(alias="InspectionLevel")


class ActionCondition(BaseModel):
    action: Literal[
        "ALLOW", "BLOCK", "CAPTCHA", "CHALLENGE", "COUNT", "EXCLUDED_AS_COUNT"
    ] = Field(alias="Action")


class AndStatement(BaseModel):
    statements: Sequence[Statement] = Field(alias="Statements")


class AssociateWebACLRequest(BaseModel):
    web_acl_arn: str = Field(alias="WebACLArn")
    resource_arn: str = Field(alias="ResourceArn")


class Body(BaseModel):
    oversize_handling: Optional[Literal["CONTINUE", "MATCH", "NO_MATCH"]] = Field(
        default=None, alias="OversizeHandling"
    )


class TextTransformation(BaseModel):
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


class ImmunityTimeProperty(BaseModel):
    immunity_time: int = Field(alias="ImmunityTime")


class CaptchaResponse(BaseModel):
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    solve_timestamp: Optional[int] = Field(default=None, alias="SolveTimestamp")
    failure_reason: Optional[
        Literal[
            "TOKEN_DOMAIN_MISMATCH", "TOKEN_EXPIRED", "TOKEN_INVALID", "TOKEN_MISSING"
        ]
    ] = Field(default=None, alias="FailureReason")


class ChallengeResponse(BaseModel):
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    solve_timestamp: Optional[int] = Field(default=None, alias="SolveTimestamp")
    failure_reason: Optional[
        Literal[
            "TOKEN_DOMAIN_MISMATCH", "TOKEN_EXPIRED", "TOKEN_INVALID", "TOKEN_MISSING"
        ]
    ] = Field(default=None, alias="FailureReason")


class ResponseMetadata(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class LabelNameCondition(BaseModel):
    label_name: str = Field(alias="LabelName")


class CookieMatchPattern(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_cookies: Optional[Sequence[str]] = Field(
        default=None, alias="IncludedCookies"
    )
    excluded_cookies: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedCookies"
    )


class Tag(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class IPSetSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class Regex(BaseModel):
    regex_string: Optional[str] = Field(default=None, alias="RegexString")


class RegexPatternSetSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class CustomResponseBody(BaseModel):
    content_type: Literal["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"] = Field(
        alias="ContentType"
    )
    content: str = Field(alias="Content")


class VisibilityConfig(BaseModel):
    sampled_requests_enabled: bool = Field(alias="SampledRequestsEnabled")
    cloud_watch_metrics_enabled: bool = Field(alias="CloudWatchMetricsEnabled")
    metric_name: str = Field(alias="MetricName")


class RuleGroupSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class WebACLSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")


class CustomHTTPHeader(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DeleteFirewallManagerRuleGroupsRequest(BaseModel):
    web_acl_arn: str = Field(alias="WebACLArn")
    web_acl_lock_token: str = Field(alias="WebACLLockToken")


class DeleteIPSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteLoggingConfigurationRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeletePermissionPolicyRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteRegexPatternSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteRuleGroupRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DeleteWebACLRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")


class DescribeManagedRuleGroupRequest(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    version_name: Optional[str] = Field(default=None, alias="VersionName")


class LabelSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class DisassociateWebACLRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ExcludedRule(BaseModel):
    name: str = Field(alias="Name")


class SingleHeader(BaseModel):
    name: str = Field(alias="Name")


class SingleQueryArgument(BaseModel):
    name: str = Field(alias="Name")


class ForwardedIPConfig(BaseModel):
    header_name: str = Field(alias="HeaderName")
    fallback_behavior: Literal["MATCH", "NO_MATCH"] = Field(alias="FallbackBehavior")


class GenerateMobileSdkReleaseUrlRequest(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    release_version: str = Field(alias="ReleaseVersion")


class GetIPSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class IPSet(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    ip_address_version: Literal["IPV4", "IPV6"] = Field(alias="IPAddressVersion")
    addresses: List[str] = Field(alias="Addresses")
    description: Optional[str] = Field(default=None, alias="Description")


class GetLoggingConfigurationRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetManagedRuleSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class GetMobileSdkReleaseRequest(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    release_version: str = Field(alias="ReleaseVersion")


class GetPermissionPolicyRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetRateBasedStatementManagedKeysRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    web_acl_name: str = Field(alias="WebACLName")
    web_acl_id: str = Field(alias="WebACLId")
    rule_name: str = Field(alias="RuleName")
    rule_group_rule_name: Optional[str] = Field(default=None, alias="RuleGroupRuleName")


class RateBasedStatementManagedKeysIPSet(BaseModel):
    ip_address_version: Optional[Literal["IPV4", "IPV6"]] = Field(
        default=None, alias="IPAddressVersion"
    )
    addresses: Optional[List[str]] = Field(default=None, alias="Addresses")


class GetRegexPatternSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class GetRuleGroupRequest(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    scope: Optional[Literal["CLOUDFRONT", "REGIONAL"]] = Field(
        default=None, alias="Scope"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")


class TimeWindow(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class GetWebACLForResourceRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetWebACLRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")


class HTTPHeader(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class HeaderMatchPattern(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_headers: Optional[Sequence[str]] = Field(
        default=None, alias="IncludedHeaders"
    )
    excluded_headers: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedHeaders"
    )


class IPSetForwardedIPConfig(BaseModel):
    header_name: str = Field(alias="HeaderName")
    fallback_behavior: Literal["MATCH", "NO_MATCH"] = Field(alias="FallbackBehavior")
    position: Literal["ANY", "FIRST", "LAST"] = Field(alias="Position")


class JsonMatchPattern(BaseModel):
    all: Optional[Mapping[str, Any]] = Field(default=None, alias="All")
    included_paths: Optional[Sequence[str]] = Field(default=None, alias="IncludedPaths")


class LabelMatchStatement(BaseModel):
    scope: Literal["LABEL", "NAMESPACE"] = Field(alias="Scope")
    key: str = Field(alias="Key")


class Label(BaseModel):
    name: str = Field(alias="Name")


class ListAvailableManagedRuleGroupVersionsRequest(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleGroupVersion(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )


class ListAvailableManagedRuleGroupsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleGroupSummary(BaseModel):
    vendor_name: Optional[str] = Field(default=None, alias="VendorName")
    name: Optional[str] = Field(default=None, alias="Name")
    versioning_supported: Optional[bool] = Field(
        default=None, alias="VersioningSupported"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ListIPSetsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListLoggingConfigurationsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListManagedRuleSetsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ManagedRuleSetSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    lock_token: Optional[str] = Field(default=None, alias="LockToken")
    arn: Optional[str] = Field(default=None, alias="ARN")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")


class ListMobileSdkReleasesRequest(BaseModel):
    platform: Literal["ANDROID", "IOS"] = Field(alias="Platform")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ReleaseSummary(BaseModel):
    release_version: Optional[str] = Field(default=None, alias="ReleaseVersion")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class ListRegexPatternSetsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListResourcesForWebACLRequest(BaseModel):
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


class ListRuleGroupsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListTagsForResourceRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListWebACLsRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PasswordField(BaseModel):
    identifier: str = Field(alias="Identifier")


class UsernameField(BaseModel):
    identifier: str = Field(alias="Identifier")


class ManagedRuleSetVersion(BaseModel):
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


class NotStatement(BaseModel):
    statement: Dict[str, Any] = Field(alias="Statement")


class OrStatement(BaseModel):
    statements: Sequence[Statement] = Field(alias="Statements")


class VersionToPublish(BaseModel):
    associated_rule_group_arn: Optional[str] = Field(
        default=None, alias="AssociatedRuleGroupArn"
    )
    forecasted_lifetime: Optional[int] = Field(default=None, alias="ForecastedLifetime")


class PutPermissionPolicyRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")


class ResponseInspectionBodyContains(BaseModel):
    success_strings: Sequence[str] = Field(alias="SuccessStrings")
    failure_strings: Sequence[str] = Field(alias="FailureStrings")


class ResponseInspectionHeader(BaseModel):
    name: str = Field(alias="Name")
    success_values: Sequence[str] = Field(alias="SuccessValues")
    failure_values: Sequence[str] = Field(alias="FailureValues")


class ResponseInspectionJson(BaseModel):
    identifier: str = Field(alias="Identifier")
    success_values: Sequence[str] = Field(alias="SuccessValues")
    failure_values: Sequence[str] = Field(alias="FailureValues")


class ResponseInspectionStatusCode(BaseModel):
    success_codes: Sequence[int] = Field(alias="SuccessCodes")
    failure_codes: Sequence[int] = Field(alias="FailureCodes")


class UntagResourceRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateIPSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    addresses: Sequence[str] = Field(alias="Addresses")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateManagedRuleSetVersionExpiryDateRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")
    version_to_expire: str = Field(alias="VersionToExpire")
    expiry_timestamp: Union[datetime, str] = Field(alias="ExpiryTimestamp")


class CaptchaConfig(BaseModel):
    immunity_time_property: Optional[ImmunityTimeProperty] = Field(
        default=None, alias="ImmunityTimeProperty"
    )


class ChallengeConfig(BaseModel):
    immunity_time_property: Optional[ImmunityTimeProperty] = Field(
        default=None, alias="ImmunityTimeProperty"
    )


class CheckCapacityResponse(BaseModel):
    capacity: int = Field(alias="Capacity")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DeleteFirewallManagerRuleGroupsResponse(BaseModel):
    next_web_acl_lock_token: str = Field(alias="NextWebACLLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GenerateMobileSdkReleaseUrlResponse(BaseModel):
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetPermissionPolicyResponse(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListResourcesForWebACLResponse(BaseModel):
    resource_arns: List[str] = Field(alias="ResourceArns")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PutManagedRuleSetVersionsResponse(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateIPSetResponse(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateManagedRuleSetVersionExpiryDateResponse(BaseModel):
    expiring_version: str = Field(alias="ExpiringVersion")
    expiry_timestamp: datetime = Field(alias="ExpiryTimestamp")
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateRegexPatternSetResponse(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateRuleGroupResponse(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateWebACLResponse(BaseModel):
    next_lock_token: str = Field(alias="NextLockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class Condition(BaseModel):
    action_condition: Optional[ActionCondition] = Field(
        default=None, alias="ActionCondition"
    )
    label_name_condition: Optional[LabelNameCondition] = Field(
        default=None, alias="LabelNameCondition"
    )


class Cookies(BaseModel):
    match_pattern: CookieMatchPattern = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    oversize_handling: Literal["CONTINUE", "MATCH", "NO_MATCH"] = Field(
        alias="OversizeHandling"
    )


class CreateIPSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    ip_address_version: Literal["IPV4", "IPV6"] = Field(alias="IPAddressVersion")
    addresses: Sequence[str] = Field(alias="Addresses")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")


class MobileSdkRelease(BaseModel):
    release_version: Optional[str] = Field(default=None, alias="ReleaseVersion")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    release_notes: Optional[str] = Field(default=None, alias="ReleaseNotes")
    tags: Optional[List[Tag]] = Field(default=None, alias="Tags")


class TagInfoForResource(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tag_list: Optional[List[Tag]] = Field(default=None, alias="TagList")


class TagResourceRequest(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[Tag] = Field(alias="Tags")


class CreateIPSetResponse(BaseModel):
    summary: IPSetSummary = Field(alias="Summary")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListIPSetsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    ip_sets: List[IPSetSummary] = Field(alias="IPSets")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateRegexPatternSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    regular_expression_list: Sequence[Regex] = Field(alias="RegularExpressionList")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")


class RegexPatternSet(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")
    description: Optional[str] = Field(default=None, alias="Description")
    regular_expression_list: Optional[List[Regex]] = Field(
        default=None, alias="RegularExpressionList"
    )


class UpdateRegexPatternSetRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    regular_expression_list: Sequence[Regex] = Field(alias="RegularExpressionList")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateRegexPatternSetResponse(BaseModel):
    summary: RegexPatternSetSummary = Field(alias="Summary")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListRegexPatternSetsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    regex_pattern_sets: List[RegexPatternSetSummary] = Field(alias="RegexPatternSets")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateRuleGroupResponse(BaseModel):
    summary: RuleGroupSummary = Field(alias="Summary")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListRuleGroupsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rule_groups: List[RuleGroupSummary] = Field(alias="RuleGroups")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateWebACLResponse(BaseModel):
    summary: WebACLSummary = Field(alias="Summary")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListWebACLsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    web_acls: List[WebACLSummary] = Field(alias="WebACLs")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CustomRequestHandling(BaseModel):
    insert_headers: Sequence[CustomHTTPHeader] = Field(alias="InsertHeaders")


class CustomResponse(BaseModel):
    response_code: int = Field(alias="ResponseCode")
    custom_response_body_key: Optional[str] = Field(
        default=None, alias="CustomResponseBodyKey"
    )
    response_headers: Optional[Sequence[CustomHTTPHeader]] = Field(
        default=None, alias="ResponseHeaders"
    )


class GeoMatchStatement(BaseModel):
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
    forwarded_ip_config: Optional[ForwardedIPConfig] = Field(
        default=None, alias="ForwardedIPConfig"
    )


class RateBasedStatement(BaseModel):
    limit: int = Field(alias="Limit")
    aggregate_key_type: Literal["FORWARDED_IP", "IP"] = Field(alias="AggregateKeyType")
    scope_down_statement: Optional[Statement] = Field(
        default=None, alias="ScopeDownStatement"
    )
    forwarded_ip_config: Optional[ForwardedIPConfig] = Field(
        default=None, alias="ForwardedIPConfig"
    )


class GetIPSetResponse(BaseModel):
    ip_set: IPSet = Field(alias="IPSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetRateBasedStatementManagedKeysResponse(BaseModel):
    managed_keys_ip_v4: RateBasedStatementManagedKeysIPSet = Field(
        alias="ManagedKeysIPV4"
    )
    managed_keys_ip_v6: RateBasedStatementManagedKeysIPSet = Field(
        alias="ManagedKeysIPV6"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetSampledRequestsRequest(BaseModel):
    web_acl_arn: str = Field(alias="WebAclArn")
    rule_metric_name: str = Field(alias="RuleMetricName")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    time_window: TimeWindow = Field(alias="TimeWindow")
    max_items: int = Field(alias="MaxItems")


class HTTPRequest(BaseModel):
    client_ip: Optional[str] = Field(default=None, alias="ClientIP")
    country: Optional[str] = Field(default=None, alias="Country")
    uri: Optional[str] = Field(default=None, alias="URI")
    method: Optional[str] = Field(default=None, alias="Method")
    http_version: Optional[str] = Field(default=None, alias="HTTPVersion")
    headers: Optional[List[HTTPHeader]] = Field(default=None, alias="Headers")


class Headers(BaseModel):
    match_pattern: HeaderMatchPattern = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    oversize_handling: Literal["CONTINUE", "MATCH", "NO_MATCH"] = Field(
        alias="OversizeHandling"
    )


class IPSetReferenceStatement(BaseModel):
    arn: str = Field(alias="ARN")
    ip_set_forwarded_ip_config: Optional[IPSetForwardedIPConfig] = Field(
        default=None, alias="IPSetForwardedIPConfig"
    )


class JsonBody(BaseModel):
    match_pattern: JsonMatchPattern = Field(alias="MatchPattern")
    match_scope: Literal["ALL", "KEY", "VALUE"] = Field(alias="MatchScope")
    invalid_fallback_behavior: Optional[
        Literal["EVALUATE_AS_STRING", "MATCH", "NO_MATCH"]
    ] = Field(default=None, alias="InvalidFallbackBehavior")
    oversize_handling: Optional[Literal["CONTINUE", "MATCH", "NO_MATCH"]] = Field(
        default=None, alias="OversizeHandling"
    )


class ListAvailableManagedRuleGroupVersionsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    versions: List[ManagedRuleGroupVersion] = Field(alias="Versions")
    current_default_version: str = Field(alias="CurrentDefaultVersion")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListAvailableManagedRuleGroupsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    managed_rule_groups: List[ManagedRuleGroupSummary] = Field(
        alias="ManagedRuleGroups"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListManagedRuleSetsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    managed_rule_sets: List[ManagedRuleSetSummary] = Field(alias="ManagedRuleSets")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListMobileSdkReleasesResponse(BaseModel):
    release_summaries: List[ReleaseSummary] = Field(alias="ReleaseSummaries")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RequestInspection(BaseModel):
    payload_type: Literal["FORM_ENCODED", "JSON"] = Field(alias="PayloadType")
    username_field: UsernameField = Field(alias="UsernameField")
    password_field: PasswordField = Field(alias="PasswordField")


class ManagedRuleSet(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    description: Optional[str] = Field(default=None, alias="Description")
    published_versions: Optional[Dict[str, ManagedRuleSetVersion]] = Field(
        default=None, alias="PublishedVersions"
    )
    recommended_version: Optional[str] = Field(default=None, alias="RecommendedVersion")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")


class PutManagedRuleSetVersionsRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    lock_token: str = Field(alias="LockToken")
    recommended_version: Optional[str] = Field(default=None, alias="RecommendedVersion")
    versions_to_publish: Optional[Mapping[str, VersionToPublish]] = Field(
        default=None, alias="VersionsToPublish"
    )


class ResponseInspection(BaseModel):
    status_code: Optional[ResponseInspectionStatusCode] = Field(
        default=None, alias="StatusCode"
    )
    header: Optional[ResponseInspectionHeader] = Field(default=None, alias="Header")
    body_contains: Optional[ResponseInspectionBodyContains] = Field(
        default=None, alias="BodyContains"
    )
    json_: Optional[ResponseInspectionJson] = Field(default=None, alias="Json")


class Filter(BaseModel):
    behavior: Literal["DROP", "KEEP"] = Field(alias="Behavior")
    requirement: Literal["MEETS_ALL", "MEETS_ANY"] = Field(alias="Requirement")
    conditions: List[Condition] = Field(alias="Conditions")


class GetMobileSdkReleaseResponse(BaseModel):
    mobile_sdk_release: MobileSdkRelease = Field(alias="MobileSdkRelease")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListTagsForResourceResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    tag_info_for_resource: TagInfoForResource = Field(alias="TagInfoForResource")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetRegexPatternSetResponse(BaseModel):
    regex_pattern_set: RegexPatternSet = Field(alias="RegexPatternSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class AllowAction(BaseModel):
    custom_request_handling: Optional[CustomRequestHandling] = Field(
        default=None, alias="CustomRequestHandling"
    )


class CaptchaAction(BaseModel):
    custom_request_handling: Optional[CustomRequestHandling] = Field(
        default=None, alias="CustomRequestHandling"
    )


class ChallengeAction(BaseModel):
    custom_request_handling: Optional[CustomRequestHandling] = Field(
        default=None, alias="CustomRequestHandling"
    )


class CountAction(BaseModel):
    custom_request_handling: Optional[CustomRequestHandling] = Field(
        default=None, alias="CustomRequestHandling"
    )


class BlockAction(BaseModel):
    custom_response: Optional[CustomResponse] = Field(
        default=None, alias="CustomResponse"
    )


class SampledHTTPRequest(BaseModel):
    request: HTTPRequest = Field(alias="Request")
    weight: int = Field(alias="Weight")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    action: Optional[str] = Field(default=None, alias="Action")
    rule_name_within_rule_group: Optional[str] = Field(
        default=None, alias="RuleNameWithinRuleGroup"
    )
    request_headers_inserted: Optional[List[HTTPHeader]] = Field(
        default=None, alias="RequestHeadersInserted"
    )
    response_code_sent: Optional[int] = Field(default=None, alias="ResponseCodeSent")
    labels: Optional[List[Label]] = Field(default=None, alias="Labels")
    captcha_response: Optional[CaptchaResponse] = Field(
        default=None, alias="CaptchaResponse"
    )
    challenge_response: Optional[ChallengeResponse] = Field(
        default=None, alias="ChallengeResponse"
    )
    overridden_action: Optional[str] = Field(default=None, alias="OverriddenAction")


class FieldToMatch(BaseModel):
    single_header: Optional[SingleHeader] = Field(default=None, alias="SingleHeader")
    single_query_argument: Optional[SingleQueryArgument] = Field(
        default=None, alias="SingleQueryArgument"
    )
    all_query_arguments: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AllQueryArguments"
    )
    uri_path: Optional[Mapping[str, Any]] = Field(default=None, alias="UriPath")
    query_string: Optional[Mapping[str, Any]] = Field(default=None, alias="QueryString")
    body: Optional[Body] = Field(default=None, alias="Body")
    method: Optional[Mapping[str, Any]] = Field(default=None, alias="Method")
    json_body: Optional[JsonBody] = Field(default=None, alias="JsonBody")
    headers: Optional[Headers] = Field(default=None, alias="Headers")
    cookies: Optional[Cookies] = Field(default=None, alias="Cookies")


class GetManagedRuleSetResponse(BaseModel):
    managed_rule_set: ManagedRuleSet = Field(alias="ManagedRuleSet")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class AWSManagedRulesATPRuleSet(BaseModel):
    login_path: str = Field(alias="LoginPath")
    request_inspection: Optional[RequestInspection] = Field(
        default=None, alias="RequestInspection"
    )
    response_inspection: Optional[ResponseInspection] = Field(
        default=None, alias="ResponseInspection"
    )


class LoggingFilter(BaseModel):
    filters: List[Filter] = Field(alias="Filters")
    default_behavior: Literal["DROP", "KEEP"] = Field(alias="DefaultBehavior")


class OverrideAction(BaseModel):
    count: Optional[CountAction] = Field(default=None, alias="Count")
    none_: Optional[Mapping[str, Any]] = Field(default=None, alias="None")


class DefaultAction(BaseModel):
    block: Optional[BlockAction] = Field(default=None, alias="Block")
    allow: Optional[AllowAction] = Field(default=None, alias="Allow")


class RuleAction(BaseModel):
    block: Optional[BlockAction] = Field(default=None, alias="Block")
    allow: Optional[AllowAction] = Field(default=None, alias="Allow")
    count: Optional[CountAction] = Field(default=None, alias="Count")
    captcha: Optional[CaptchaAction] = Field(default=None, alias="Captcha")
    challenge: Optional[ChallengeAction] = Field(default=None, alias="Challenge")


class GetSampledRequestsResponse(BaseModel):
    sampled_requests: List[SampledHTTPRequest] = Field(alias="SampledRequests")
    population_size: int = Field(alias="PopulationSize")
    time_window: TimeWindow = Field(alias="TimeWindow")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ByteMatchStatement(BaseModel):
    search_string: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="SearchString"
    )
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )
    positional_constraint: Literal[
        "CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"
    ] = Field(alias="PositionalConstraint")


class RegexMatchStatement(BaseModel):
    regex_string: str = Field(alias="RegexString")
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )


class RegexPatternSetReferenceStatement(BaseModel):
    arn: str = Field(alias="ARN")
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )


class SizeConstraintStatement(BaseModel):
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    comparison_operator: Literal["EQ", "GE", "GT", "LE", "LT", "NE"] = Field(
        alias="ComparisonOperator"
    )
    size: int = Field(alias="Size")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )


class SqliMatchStatement(BaseModel):
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )
    sensitivity_level: Optional[Literal["HIGH", "LOW"]] = Field(
        default=None, alias="SensitivityLevel"
    )


class XssMatchStatement(BaseModel):
    field_to_match: FieldToMatch = Field(alias="FieldToMatch")
    text_transformations: Sequence[TextTransformation] = Field(
        alias="TextTransformations"
    )


class ManagedRuleGroupConfig(BaseModel):
    login_path: Optional[str] = Field(default=None, alias="LoginPath")
    payload_type: Optional[Literal["FORM_ENCODED", "JSON"]] = Field(
        default=None, alias="PayloadType"
    )
    username_field: Optional[UsernameField] = Field(default=None, alias="UsernameField")
    password_field: Optional[PasswordField] = Field(default=None, alias="PasswordField")
    aws_managed_rules_bot_control_rule_set: Optional[
        AWSManagedRulesBotControlRuleSet
    ] = Field(default=None, alias="AWSManagedRulesBotControlRuleSet")
    aws_managed_rules_atp_rule_set: Optional[AWSManagedRulesATPRuleSet] = Field(
        default=None, alias="AWSManagedRulesATPRuleSet"
    )


class LoggingConfiguration(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    log_destination_configs: List[str] = Field(alias="LogDestinationConfigs")
    redacted_fields: Optional[List[FieldToMatch]] = Field(
        default=None, alias="RedactedFields"
    )
    managed_by_firewall_manager: Optional[bool] = Field(
        default=None, alias="ManagedByFirewallManager"
    )
    logging_filter: Optional[LoggingFilter] = Field(default=None, alias="LoggingFilter")


class RuleActionOverride(BaseModel):
    name: str = Field(alias="Name")
    action_to_use: RuleAction = Field(alias="ActionToUse")


class RuleSummary(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    action: Optional[RuleAction] = Field(default=None, alias="Action")


class Rule(BaseModel):
    name: str = Field(alias="Name")
    priority: int = Field(alias="Priority")
    statement: Statement = Field(alias="Statement")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    action: Optional[RuleAction] = Field(default=None, alias="Action")
    override_action: Optional[OverrideAction] = Field(
        default=None, alias="OverrideAction"
    )
    rule_labels: Optional[Sequence[Label]] = Field(default=None, alias="RuleLabels")
    captcha_config: Optional[CaptchaConfig] = Field(default=None, alias="CaptchaConfig")
    challenge_config: Optional[ChallengeConfig] = Field(
        default=None, alias="ChallengeConfig"
    )


class GetLoggingConfigurationResponse(BaseModel):
    logging_configuration: LoggingConfiguration = Field(alias="LoggingConfiguration")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListLoggingConfigurationsResponse(BaseModel):
    logging_configurations: List[LoggingConfiguration] = Field(
        alias="LoggingConfigurations"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PutLoggingConfigurationRequest(BaseModel):
    logging_configuration: LoggingConfiguration = Field(alias="LoggingConfiguration")


class PutLoggingConfigurationResponse(BaseModel):
    logging_configuration: LoggingConfiguration = Field(alias="LoggingConfiguration")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ManagedRuleGroupStatement(BaseModel):
    vendor_name: str = Field(alias="VendorName")
    name: str = Field(alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    excluded_rules: Optional[Sequence[ExcludedRule]] = Field(
        default=None, alias="ExcludedRules"
    )
    scope_down_statement: Optional[Statement] = Field(
        default=None, alias="ScopeDownStatement"
    )
    managed_rule_group_configs: Optional[Sequence[ManagedRuleGroupConfig]] = Field(
        default=None, alias="ManagedRuleGroupConfigs"
    )
    rule_action_overrides: Optional[Sequence[RuleActionOverride]] = Field(
        default=None, alias="RuleActionOverrides"
    )


class RuleGroupReferenceStatement(BaseModel):
    arn: str = Field(alias="ARN")
    excluded_rules: Optional[Sequence[ExcludedRule]] = Field(
        default=None, alias="ExcludedRules"
    )
    rule_action_overrides: Optional[Sequence[RuleActionOverride]] = Field(
        default=None, alias="RuleActionOverrides"
    )


class DescribeManagedRuleGroupResponse(BaseModel):
    version_name: str = Field(alias="VersionName")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    capacity: int = Field(alias="Capacity")
    rules: List[RuleSummary] = Field(alias="Rules")
    label_namespace: str = Field(alias="LabelNamespace")
    available_labels: List[LabelSummary] = Field(alias="AvailableLabels")
    consumed_labels: List[LabelSummary] = Field(alias="ConsumedLabels")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CheckCapacityRequest(BaseModel):
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    rules: Sequence[Rule] = Field(alias="Rules")


class CreateRuleGroupRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    capacity: int = Field(alias="Capacity")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[Rule]] = Field(default=None, alias="Rules")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )


class CreateWebACLRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    default_action: DefaultAction = Field(alias="DefaultAction")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[Rule]] = Field(default=None, alias="Rules")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfig] = Field(default=None, alias="CaptchaConfig")
    challenge_config: Optional[ChallengeConfig] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[Sequence[str]] = Field(default=None, alias="TokenDomains")


class RuleGroup(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    capacity: int = Field(alias="Capacity")
    arn: str = Field(alias="ARN")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[List[Rule]] = Field(default=None, alias="Rules")
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")
    custom_response_bodies: Optional[Dict[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    available_labels: Optional[List[LabelSummary]] = Field(
        default=None, alias="AvailableLabels"
    )
    consumed_labels: Optional[List[LabelSummary]] = Field(
        default=None, alias="ConsumedLabels"
    )


class UpdateRuleGroupRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[Rule]] = Field(default=None, alias="Rules")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )


class UpdateWebACLRequest(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["CLOUDFRONT", "REGIONAL"] = Field(alias="Scope")
    id: str = Field(alias="Id")
    default_action: DefaultAction = Field(alias="DefaultAction")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    lock_token: str = Field(alias="LockToken")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[Rule]] = Field(default=None, alias="Rules")
    custom_response_bodies: Optional[Mapping[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfig] = Field(default=None, alias="CaptchaConfig")
    challenge_config: Optional[ChallengeConfig] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[Sequence[str]] = Field(default=None, alias="TokenDomains")


class FirewallManagerStatement(BaseModel):
    managed_rule_group_statement: Optional[ManagedRuleGroupStatement] = Field(
        default=None, alias="ManagedRuleGroupStatement"
    )
    rule_group_reference_statement: Optional[RuleGroupReferenceStatement] = Field(
        default=None, alias="RuleGroupReferenceStatement"
    )


class Statement(BaseModel):
    byte_match_statement: Optional[ByteMatchStatement] = Field(
        default=None, alias="ByteMatchStatement"
    )
    sqli_match_statement: Optional[SqliMatchStatement] = Field(
        default=None, alias="SqliMatchStatement"
    )
    xss_match_statement: Optional[XssMatchStatement] = Field(
        default=None, alias="XssMatchStatement"
    )
    size_constraint_statement: Optional[SizeConstraintStatement] = Field(
        default=None, alias="SizeConstraintStatement"
    )
    geo_match_statement: Optional[GeoMatchStatement] = Field(
        default=None, alias="GeoMatchStatement"
    )
    rule_group_reference_statement: Optional[RuleGroupReferenceStatement] = Field(
        default=None, alias="RuleGroupReferenceStatement"
    )
    ip_set_reference_statement: Optional[IPSetReferenceStatement] = Field(
        default=None, alias="IPSetReferenceStatement"
    )
    regex_pattern_set_reference_statement: Optional[
        RegexPatternSetReferenceStatement
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
    label_match_statement: Optional[LabelMatchStatement] = Field(
        default=None, alias="LabelMatchStatement"
    )
    regex_match_statement: Optional[RegexMatchStatement] = Field(
        default=None, alias="RegexMatchStatement"
    )


class GetRuleGroupResponse(BaseModel):
    rule_group: RuleGroup = Field(alias="RuleGroup")
    lock_token: str = Field(alias="LockToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FirewallManagerRuleGroup(BaseModel):
    name: str = Field(alias="Name")
    priority: int = Field(alias="Priority")
    firewall_manager_statement: FirewallManagerStatement = Field(
        alias="FirewallManagerStatement"
    )
    override_action: OverrideAction = Field(alias="OverrideAction")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")


class WebACL(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    default_action: DefaultAction = Field(alias="DefaultAction")
    visibility_config: VisibilityConfig = Field(alias="VisibilityConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[List[Rule]] = Field(default=None, alias="Rules")
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    pre_process_firewall_manager_rule_groups: Optional[
        List[FirewallManagerRuleGroup]
    ] = Field(default=None, alias="PreProcessFirewallManagerRuleGroups")
    post_process_firewall_manager_rule_groups: Optional[
        List[FirewallManagerRuleGroup]
    ] = Field(default=None, alias="PostProcessFirewallManagerRuleGroups")
    managed_by_firewall_manager: Optional[bool] = Field(
        default=None, alias="ManagedByFirewallManager"
    )
    label_namespace: Optional[str] = Field(default=None, alias="LabelNamespace")
    custom_response_bodies: Optional[Dict[str, CustomResponseBody]] = Field(
        default=None, alias="CustomResponseBodies"
    )
    captcha_config: Optional[CaptchaConfig] = Field(default=None, alias="CaptchaConfig")
    challenge_config: Optional[ChallengeConfig] = Field(
        default=None, alias="ChallengeConfig"
    )
    token_domains: Optional[List[str]] = Field(default=None, alias="TokenDomains")


class GetWebACLForResourceResponse(BaseModel):
    web_acl: WebACL = Field(alias="WebACL")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetWebACLResponse(BaseModel):
    web_acl: WebACL = Field(alias="WebACL")
    lock_token: str = Field(alias="LockToken")
    application_integration_url: str = Field(alias="ApplicationIntegrationURL")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")
