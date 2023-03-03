# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AliasICPRecordalModel(BaseModel):
    cname: Optional[str] = Field(default=None, alias="CNAME")
    icp_recordal_status: Optional[Literal["APPROVED", "PENDING", "SUSPENDED"]] = Field(
        default=None, alias="ICPRecordalStatus"
    )


class AliasesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class CachedMethodsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[
        Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(alias="Items")


class AssociateAliasRequestModel(BaseModel):
    target_distribution_id: str = Field(alias="TargetDistributionId")
    alias: str = Field(alias="Alias")


class TrustedKeyGroupsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class TrustedSignersModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class CookieNamesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class HeadersModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class QueryStringNamesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class CloudFrontOriginAccessIdentityConfigModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    comment: str = Field(alias="Comment")


class CloudFrontOriginAccessIdentitySummaryModel(BaseModel):
    id: str = Field(alias="Id")
    s3_canonical_user_id: str = Field(alias="S3CanonicalUserId")
    comment: str = Field(alias="Comment")


class ConflictingAliasModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="Alias")
    distribution_id: Optional[str] = Field(default=None, alias="DistributionId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class ContentTypeProfileModel(BaseModel):
    format: Literal["URLEncoded"] = Field(alias="Format")
    content_type: str = Field(alias="ContentType")
    profile_id: Optional[str] = Field(default=None, alias="ProfileId")


class StagingDistributionDnsNamesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class ContinuousDeploymentSingleHeaderConfigModel(BaseModel):
    header: str = Field(alias="Header")
    value: str = Field(alias="Value")


class SessionStickinessConfigModel(BaseModel):
    idle_ttl: int = Field(alias="IdleTTL")
    maximum_ttl: int = Field(alias="MaximumTTL")


class CopyDistributionRequestModel(BaseModel):
    primary_distribution_id: str = Field(alias="PrimaryDistributionId")
    caller_reference: str = Field(alias="CallerReference")
    staging: Optional[bool] = Field(default=None, alias="Staging")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FunctionConfigModel(BaseModel):
    comment: str = Field(alias="Comment")
    runtime: Literal["cloudfront-js-1.0"] = Field(alias="Runtime")


class KeyGroupConfigModel(BaseModel):
    name: str = Field(alias="Name")
    items: Sequence[str] = Field(alias="Items")
    comment: Optional[str] = Field(default=None, alias="Comment")


class OriginAccessControlConfigModel(BaseModel):
    name: str = Field(alias="Name")
    signing_protocol: Literal["sigv4"] = Field(alias="SigningProtocol")
    signing_behavior: Literal["always", "never", "no-override"] = Field(
        alias="SigningBehavior"
    )
    origin_access_control_origin_type: Literal["mediastore", "s3"] = Field(
        alias="OriginAccessControlOriginType"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class PublicKeyConfigModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    name: str = Field(alias="Name")
    encoded_key: str = Field(alias="EncodedKey")
    comment: Optional[str] = Field(default=None, alias="Comment")


class CustomErrorResponseModel(BaseModel):
    error_code: int = Field(alias="ErrorCode")
    response_page_path: Optional[str] = Field(default=None, alias="ResponsePagePath")
    response_code: Optional[str] = Field(default=None, alias="ResponseCode")
    error_caching_min_ttl: Optional[int] = Field(
        default=None, alias="ErrorCachingMinTTL"
    )


class OriginCustomHeaderModel(BaseModel):
    header_name: str = Field(alias="HeaderName")
    header_value: str = Field(alias="HeaderValue")


class OriginSslProtocolsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]] = Field(alias="Items")


class DeleteCachePolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteCloudFrontOriginAccessIdentityRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteContinuousDeploymentPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteFieldLevelEncryptionConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteFieldLevelEncryptionProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    if_match: str = Field(alias="IfMatch")


class DeleteKeyGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteMonitoringSubscriptionRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")


class DeleteOriginAccessControlRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteOriginRequestPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeletePublicKeyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteRealtimeLogConfigRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="ARN")


class DeleteResponseHeadersPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DeleteStreamingDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DescribeFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    stage: Optional[Literal["DEVELOPMENT", "LIVE"]] = Field(default=None, alias="Stage")


class LoggingConfigModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    include_cookies: bool = Field(alias="IncludeCookies")
    bucket: str = Field(alias="Bucket")
    prefix: str = Field(alias="Prefix")


class ViewerCertificateModel(BaseModel):
    cloud_front_default_certificate: Optional[bool] = Field(
        default=None, alias="CloudFrontDefaultCertificate"
    )
    iamcertificate_id: Optional[str] = Field(default=None, alias="IAMCertificateId")
    acmcertificate_arn: Optional[str] = Field(default=None, alias="ACMCertificateArn")
    s_s_l_support_method: Optional[Literal["sni-only", "static-ip", "vip"]] = Field(
        default=None, alias="SSLSupportMethod"
    )
    minimum_protocol_version: Optional[
        Literal[
            "SSLv3",
            "TLSv1",
            "TLSv1.1_2016",
            "TLSv1.2_2018",
            "TLSv1.2_2019",
            "TLSv1.2_2021",
            "TLSv1_2016",
        ]
    ] = Field(default=None, alias="MinimumProtocolVersion")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    certificate_source: Optional[Literal["acm", "cloudfront", "iam"]] = Field(
        default=None, alias="CertificateSource"
    )


class DistributionIdListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class FieldPatternsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class KinesisStreamConfigModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    stream_arn: str = Field(alias="StreamARN")


class QueryStringCacheKeysModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class FunctionAssociationModel(BaseModel):
    function_arn: str = Field(alias="FunctionARN")
    event_type: Literal[
        "origin-request", "origin-response", "viewer-request", "viewer-response"
    ] = Field(alias="EventType")


class FunctionMetadataModel(BaseModel):
    function_arn: str = Field(alias="FunctionARN")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    stage: Optional[Literal["DEVELOPMENT", "LIVE"]] = Field(default=None, alias="Stage")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class GeoRestrictionModel(BaseModel):
    restriction_type: Literal["blacklist", "none", "whitelist"] = Field(
        alias="RestrictionType"
    )
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class GetCachePolicyConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetCachePolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetCloudFrontOriginAccessIdentityConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetCloudFrontOriginAccessIdentityRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetContinuousDeploymentPolicyConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetContinuousDeploymentPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetDistributionConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFieldLevelEncryptionConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFieldLevelEncryptionProfileConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFieldLevelEncryptionProfileRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFieldLevelEncryptionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    stage: Optional[Literal["DEVELOPMENT", "LIVE"]] = Field(default=None, alias="Stage")


class GetInvalidationRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    id: str = Field(alias="Id")


class GetKeyGroupConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetKeyGroupRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetMonitoringSubscriptionRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")


class GetOriginAccessControlConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetOriginAccessControlRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetOriginRequestPolicyConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetOriginRequestPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetPublicKeyConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetPublicKeyRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetRealtimeLogConfigRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="ARN")


class GetResponseHeadersPolicyConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetResponseHeadersPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetStreamingDistributionConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetStreamingDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class PathsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class InvalidationSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    create_time: datetime = Field(alias="CreateTime")
    status: str = Field(alias="Status")


class KeyPairIdsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[str]] = Field(default=None, alias="Items")


class LambdaFunctionAssociationModel(BaseModel):
    lambda_function_arn: str = Field(alias="LambdaFunctionARN")
    event_type: Literal[
        "origin-request", "origin-response", "viewer-request", "viewer-response"
    ] = Field(alias="EventType")
    include_body: Optional[bool] = Field(default=None, alias="IncludeBody")


class ListCachePoliciesRequestModel(BaseModel):
    type: Optional[Literal["custom", "managed"]] = Field(default=None, alias="Type")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListCloudFrontOriginAccessIdentitiesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListConflictingAliasesRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    alias: str = Field(alias="Alias")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListContinuousDeploymentPoliciesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsByCachePolicyIdRequestModel(BaseModel):
    cache_policy_id: str = Field(alias="CachePolicyId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsByKeyGroupRequestModel(BaseModel):
    key_group_id: str = Field(alias="KeyGroupId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsByOriginRequestPolicyIdRequestModel(BaseModel):
    origin_request_policy_id: str = Field(alias="OriginRequestPolicyId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsByRealtimeLogConfigRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")
    realtime_log_config_name: Optional[str] = Field(
        default=None, alias="RealtimeLogConfigName"
    )
    realtime_log_config_arn: Optional[str] = Field(
        default=None, alias="RealtimeLogConfigArn"
    )


class ListDistributionsByResponseHeadersPolicyIdRequestModel(BaseModel):
    response_headers_policy_id: str = Field(alias="ResponseHeadersPolicyId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsByWebACLIdRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListDistributionsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListFieldLevelEncryptionConfigsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListFieldLevelEncryptionProfilesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListFunctionsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")
    stage: Optional[Literal["DEVELOPMENT", "LIVE"]] = Field(default=None, alias="Stage")


class ListInvalidationsRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListKeyGroupsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListOriginAccessControlsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListOriginRequestPoliciesRequestModel(BaseModel):
    type: Optional[Literal["custom", "managed"]] = Field(default=None, alias="Type")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListPublicKeysRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListRealtimeLogConfigsRequestModel(BaseModel):
    max_items: Optional[str] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListResponseHeadersPoliciesRequestModel(BaseModel):
    type: Optional[Literal["custom", "managed"]] = Field(default=None, alias="Type")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListStreamingDistributionsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListTagsForResourceRequestModel(BaseModel):
    resource: str = Field(alias="Resource")


class RealtimeMetricsSubscriptionConfigModel(BaseModel):
    realtime_metrics_subscription_status: Literal["Disabled", "Enabled"] = Field(
        alias="RealtimeMetricsSubscriptionStatus"
    )


class OriginAccessControlSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    signing_protocol: Literal["sigv4"] = Field(alias="SigningProtocol")
    signing_behavior: Literal["always", "never", "no-override"] = Field(
        alias="SigningBehavior"
    )
    origin_access_control_origin_type: Literal["mediastore", "s3"] = Field(
        alias="OriginAccessControlOriginType"
    )


class StatusCodesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[int] = Field(alias="Items")


class OriginGroupMemberModel(BaseModel):
    origin_id: str = Field(alias="OriginId")


class OriginShieldModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    origin_shield_region: Optional[str] = Field(
        default=None, alias="OriginShieldRegion"
    )


class S3OriginConfigModel(BaseModel):
    origin_access_identity: str = Field(alias="OriginAccessIdentity")


class PublicKeySummaryModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    created_time: datetime = Field(alias="CreatedTime")
    encoded_key: str = Field(alias="EncodedKey")
    comment: Optional[str] = Field(default=None, alias="Comment")


class PublishFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    if_match: str = Field(alias="IfMatch")


class QueryArgProfileModel(BaseModel):
    query_arg: str = Field(alias="QueryArg")
    profile_id: str = Field(alias="ProfileId")


class ResponseHeadersPolicyAccessControlAllowHeadersModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Sequence[str] = Field(alias="Items")


class ResponseHeadersPolicyAccessControlAllowMethodsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Sequence[
        Literal["ALL", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(alias="Items")


class ResponseHeadersPolicyAccessControlAllowOriginsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Sequence[str] = Field(alias="Items")


class ResponseHeadersPolicyAccessControlExposeHeadersModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class ResponseHeadersPolicyServerTimingHeadersConfigModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    sampling_rate: Optional[float] = Field(default=None, alias="SamplingRate")


class ResponseHeadersPolicyContentSecurityPolicyModel(BaseModel):
    override: bool = Field(alias="Override")
    content_security_policy: str = Field(alias="ContentSecurityPolicy")


class ResponseHeadersPolicyContentTypeOptionsModel(BaseModel):
    override: bool = Field(alias="Override")


class ResponseHeadersPolicyCustomHeaderModel(BaseModel):
    header: str = Field(alias="Header")
    value: str = Field(alias="Value")
    override: bool = Field(alias="Override")


class ResponseHeadersPolicyFrameOptionsModel(BaseModel):
    override: bool = Field(alias="Override")
    frame_option: Literal["DENY", "SAMEORIGIN"] = Field(alias="FrameOption")


class ResponseHeadersPolicyReferrerPolicyModel(BaseModel):
    override: bool = Field(alias="Override")
    referrer_policy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ] = Field(alias="ReferrerPolicy")


class ResponseHeadersPolicyRemoveHeaderModel(BaseModel):
    header: str = Field(alias="Header")


class ResponseHeadersPolicyStrictTransportSecurityModel(BaseModel):
    override: bool = Field(alias="Override")
    access_control_max_age_sec: int = Field(alias="AccessControlMaxAgeSec")
    include_subdomains: Optional[bool] = Field(default=None, alias="IncludeSubdomains")
    preload: Optional[bool] = Field(default=None, alias="Preload")


class ResponseHeadersPolicyXSSProtectionModel(BaseModel):
    override: bool = Field(alias="Override")
    protection: bool = Field(alias="Protection")
    mode_block: Optional[bool] = Field(default=None, alias="ModeBlock")
    report_uri: Optional[str] = Field(default=None, alias="ReportUri")


class S3OriginModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    origin_access_identity: str = Field(alias="OriginAccessIdentity")


class StreamingLoggingConfigModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    bucket: str = Field(alias="Bucket")
    prefix: str = Field(alias="Prefix")


class TagKeysModel(BaseModel):
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class TestFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    if_match: str = Field(alias="IfMatch")
    event_object: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="EventObject"
    )
    stage: Optional[Literal["DEVELOPMENT", "LIVE"]] = Field(default=None, alias="Stage")


class UpdateDistributionWithStagingConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")
    staging_distribution_id: Optional[str] = Field(
        default=None, alias="StagingDistributionId"
    )
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class AllowedMethodsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[
        Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(alias="Items")
    cached_methods: Optional[CachedMethodsModel] = Field(
        default=None, alias="CachedMethods"
    )


class CachePolicyCookiesConfigModel(BaseModel):
    cookie_behavior: Literal["all", "allExcept", "none", "whitelist"] = Field(
        alias="CookieBehavior"
    )
    cookies: Optional[CookieNamesModel] = Field(default=None, alias="Cookies")


class CookiePreferenceModel(BaseModel):
    forward: Literal["all", "none", "whitelist"] = Field(alias="Forward")
    whitelisted_names: Optional[CookieNamesModel] = Field(
        default=None, alias="WhitelistedNames"
    )


class OriginRequestPolicyCookiesConfigModel(BaseModel):
    cookie_behavior: Literal["all", "allExcept", "none", "whitelist"] = Field(
        alias="CookieBehavior"
    )
    cookies: Optional[CookieNamesModel] = Field(default=None, alias="Cookies")


class CachePolicyHeadersConfigModel(BaseModel):
    header_behavior: Literal["none", "whitelist"] = Field(alias="HeaderBehavior")
    headers: Optional[HeadersModel] = Field(default=None, alias="Headers")


class OriginRequestPolicyHeadersConfigModel(BaseModel):
    header_behavior: Literal[
        "allExcept", "allViewer", "allViewerAndWhitelistCloudFront", "none", "whitelist"
    ] = Field(alias="HeaderBehavior")
    headers: Optional[HeadersModel] = Field(default=None, alias="Headers")


class CachePolicyQueryStringsConfigModel(BaseModel):
    query_string_behavior: Literal["all", "allExcept", "none", "whitelist"] = Field(
        alias="QueryStringBehavior"
    )
    query_strings: Optional[QueryStringNamesModel] = Field(
        default=None, alias="QueryStrings"
    )


class OriginRequestPolicyQueryStringsConfigModel(BaseModel):
    query_string_behavior: Literal["all", "allExcept", "none", "whitelist"] = Field(
        alias="QueryStringBehavior"
    )
    query_strings: Optional[QueryStringNamesModel] = Field(
        default=None, alias="QueryStrings"
    )


class CloudFrontOriginAccessIdentityModel(BaseModel):
    id: str = Field(alias="Id")
    s3_canonical_user_id: str = Field(alias="S3CanonicalUserId")
    cloud_front_origin_access_identity_config: Optional[
        CloudFrontOriginAccessIdentityConfigModel
    ] = Field(default=None, alias="CloudFrontOriginAccessIdentityConfig")


class CreateCloudFrontOriginAccessIdentityRequestModel(BaseModel):
    cloud_front_origin_access_identity_config: CloudFrontOriginAccessIdentityConfigModel = Field(
        alias="CloudFrontOriginAccessIdentityConfig"
    )


class UpdateCloudFrontOriginAccessIdentityRequestModel(BaseModel):
    cloud_front_origin_access_identity_config: CloudFrontOriginAccessIdentityConfigModel = Field(
        alias="CloudFrontOriginAccessIdentityConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class CloudFrontOriginAccessIdentityListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[CloudFrontOriginAccessIdentitySummaryModel]] = Field(
        default=None, alias="Items"
    )


class ConflictingAliasesListModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    quantity: Optional[int] = Field(default=None, alias="Quantity")
    items: Optional[List[ConflictingAliasModel]] = Field(default=None, alias="Items")


class ContentTypeProfilesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[ContentTypeProfileModel]] = Field(
        default=None, alias="Items"
    )


class ContinuousDeploymentSingleWeightConfigModel(BaseModel):
    weight: float = Field(alias="Weight")
    session_stickiness_config: Optional[SessionStickinessConfigModel] = Field(
        default=None, alias="SessionStickinessConfig"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCloudFrontOriginAccessIdentityConfigResultModel(BaseModel):
    cloud_front_origin_access_identity_config: CloudFrontOriginAccessIdentityConfigModel = Field(
        alias="CloudFrontOriginAccessIdentityConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionResultModel(BaseModel):
    function_code: Type[StreamingBody] = Field(alias="FunctionCode")
    etag: str = Field(alias="ETag")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    function_config: FunctionConfigModel = Field(alias="FunctionConfig")
    function_code: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="FunctionCode"
    )


class UpdateFunctionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    if_match: str = Field(alias="IfMatch")
    function_config: FunctionConfigModel = Field(alias="FunctionConfig")
    function_code: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="FunctionCode"
    )


class CreateKeyGroupRequestModel(BaseModel):
    key_group_config: KeyGroupConfigModel = Field(alias="KeyGroupConfig")


class GetKeyGroupConfigResultModel(BaseModel):
    key_group_config: KeyGroupConfigModel = Field(alias="KeyGroupConfig")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class KeyGroupModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    key_group_config: KeyGroupConfigModel = Field(alias="KeyGroupConfig")


class UpdateKeyGroupRequestModel(BaseModel):
    key_group_config: KeyGroupConfigModel = Field(alias="KeyGroupConfig")
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class CreateOriginAccessControlRequestModel(BaseModel):
    origin_access_control_config: OriginAccessControlConfigModel = Field(
        alias="OriginAccessControlConfig"
    )


class GetOriginAccessControlConfigResultModel(BaseModel):
    origin_access_control_config: OriginAccessControlConfigModel = Field(
        alias="OriginAccessControlConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginAccessControlModel(BaseModel):
    id: str = Field(alias="Id")
    origin_access_control_config: Optional[OriginAccessControlConfigModel] = Field(
        default=None, alias="OriginAccessControlConfig"
    )


class UpdateOriginAccessControlRequestModel(BaseModel):
    origin_access_control_config: OriginAccessControlConfigModel = Field(
        alias="OriginAccessControlConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class CreatePublicKeyRequestModel(BaseModel):
    public_key_config: PublicKeyConfigModel = Field(alias="PublicKeyConfig")


class GetPublicKeyConfigResultModel(BaseModel):
    public_key_config: PublicKeyConfigModel = Field(alias="PublicKeyConfig")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublicKeyModel(BaseModel):
    id: str = Field(alias="Id")
    created_time: datetime = Field(alias="CreatedTime")
    public_key_config: PublicKeyConfigModel = Field(alias="PublicKeyConfig")


class UpdatePublicKeyRequestModel(BaseModel):
    public_key_config: PublicKeyConfigModel = Field(alias="PublicKeyConfig")
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class CustomErrorResponsesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[CustomErrorResponseModel]] = Field(default=None, alias="Items")


class CustomHeadersModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[OriginCustomHeaderModel]] = Field(default=None, alias="Items")


class CustomOriginConfigModel(BaseModel):
    http_port: int = Field(alias="HTTPPort")
    http_s_port: int = Field(alias="HTTPSPort")
    origin_protocol_policy: Literal["http-only", "https-only", "match-viewer"] = Field(
        alias="OriginProtocolPolicy"
    )
    origin_ssl_protocols: Optional[OriginSslProtocolsModel] = Field(
        default=None, alias="OriginSslProtocols"
    )
    origin_read_timeout: Optional[int] = Field(default=None, alias="OriginReadTimeout")
    origin_keepalive_timeout: Optional[int] = Field(
        default=None, alias="OriginKeepaliveTimeout"
    )


class ListDistributionsByCachePolicyIdResultModel(BaseModel):
    distribution_id_list: DistributionIdListModel = Field(alias="DistributionIdList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsByKeyGroupResultModel(BaseModel):
    distribution_id_list: DistributionIdListModel = Field(alias="DistributionIdList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsByOriginRequestPolicyIdResultModel(BaseModel):
    distribution_id_list: DistributionIdListModel = Field(alias="DistributionIdList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsByResponseHeadersPolicyIdResultModel(BaseModel):
    distribution_id_list: DistributionIdListModel = Field(alias="DistributionIdList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EncryptionEntityModel(BaseModel):
    public_key_id: str = Field(alias="PublicKeyId")
    provider_id: str = Field(alias="ProviderId")
    field_patterns: FieldPatternsModel = Field(alias="FieldPatterns")


class EndPointModel(BaseModel):
    stream_type: str = Field(alias="StreamType")
    kinesis_stream_config: Optional[KinesisStreamConfigModel] = Field(
        default=None, alias="KinesisStreamConfig"
    )


class FunctionAssociationsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[FunctionAssociationModel]] = Field(default=None, alias="Items")


class FunctionSummaryModel(BaseModel):
    name: str = Field(alias="Name")
    function_config: FunctionConfigModel = Field(alias="FunctionConfig")
    function_metadata: FunctionMetadataModel = Field(alias="FunctionMetadata")
    status: Optional[str] = Field(default=None, alias="Status")


class RestrictionsModel(BaseModel):
    geo_restriction: GeoRestrictionModel = Field(alias="GeoRestriction")


class GetDistributionRequestDistributionDeployedWaitModel(BaseModel):
    id: str = Field(alias="Id")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetInvalidationRequestInvalidationCompletedWaitModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    id: str = Field(alias="Id")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingDistributionRequestStreamingDistributionDeployedWaitModel(BaseModel):
    id: str = Field(alias="Id")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class InvalidationBatchModel(BaseModel):
    paths: PathsModel = Field(alias="Paths")
    caller_reference: str = Field(alias="CallerReference")


class InvalidationListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[InvalidationSummaryModel]] = Field(default=None, alias="Items")


class KGKeyPairIdsModel(BaseModel):
    key_group_id: Optional[str] = Field(default=None, alias="KeyGroupId")
    key_pair_ids: Optional[KeyPairIdsModel] = Field(default=None, alias="KeyPairIds")


class SignerModel(BaseModel):
    aws_account_number: Optional[str] = Field(default=None, alias="AwsAccountNumber")
    key_pair_ids: Optional[KeyPairIdsModel] = Field(default=None, alias="KeyPairIds")


class LambdaFunctionAssociationsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[LambdaFunctionAssociationModel]] = Field(
        default=None, alias="Items"
    )


class ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDistributionsRequestListDistributionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInvalidationsRequestListInvalidationsPaginateModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamingDistributionsRequestListStreamingDistributionsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MonitoringSubscriptionModel(BaseModel):
    realtime_metrics_subscription_config: Optional[
        RealtimeMetricsSubscriptionConfigModel
    ] = Field(default=None, alias="RealtimeMetricsSubscriptionConfig")


class OriginAccessControlListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[OriginAccessControlSummaryModel]] = Field(
        default=None, alias="Items"
    )


class OriginGroupFailoverCriteriaModel(BaseModel):
    status_codes: StatusCodesModel = Field(alias="StatusCodes")


class OriginGroupMembersModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[OriginGroupMemberModel] = Field(alias="Items")


class PublicKeyListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[PublicKeySummaryModel]] = Field(default=None, alias="Items")


class QueryArgProfilesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[QueryArgProfileModel]] = Field(default=None, alias="Items")


class ResponseHeadersPolicyCorsConfigModel(BaseModel):
    access_control_allow_origins: ResponseHeadersPolicyAccessControlAllowOriginsModel = Field(
        alias="AccessControlAllowOrigins"
    )
    access_control_allow_headers: ResponseHeadersPolicyAccessControlAllowHeadersModel = Field(
        alias="AccessControlAllowHeaders"
    )
    access_control_allow_methods: ResponseHeadersPolicyAccessControlAllowMethodsModel = Field(
        alias="AccessControlAllowMethods"
    )
    access_control_allow_credentials: bool = Field(
        alias="AccessControlAllowCredentials"
    )
    origin_override: bool = Field(alias="OriginOverride")
    access_control_expose_headers: Optional[
        ResponseHeadersPolicyAccessControlExposeHeadersModel
    ] = Field(default=None, alias="AccessControlExposeHeaders")
    access_control_max_age_sec: Optional[int] = Field(
        default=None, alias="AccessControlMaxAgeSec"
    )


class ResponseHeadersPolicyCustomHeadersConfigModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[ResponseHeadersPolicyCustomHeaderModel]] = Field(
        default=None, alias="Items"
    )


class ResponseHeadersPolicyRemoveHeadersConfigModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[ResponseHeadersPolicyRemoveHeaderModel]] = Field(
        default=None, alias="Items"
    )


class ResponseHeadersPolicySecurityHeadersConfigModel(BaseModel):
    xs_s_protection: Optional[ResponseHeadersPolicyXSSProtectionModel] = Field(
        default=None, alias="XSSProtection"
    )
    frame_options: Optional[ResponseHeadersPolicyFrameOptionsModel] = Field(
        default=None, alias="FrameOptions"
    )
    referrer_policy: Optional[ResponseHeadersPolicyReferrerPolicyModel] = Field(
        default=None, alias="ReferrerPolicy"
    )
    content_security_policy: Optional[
        ResponseHeadersPolicyContentSecurityPolicyModel
    ] = Field(default=None, alias="ContentSecurityPolicy")
    content_type_options: Optional[
        ResponseHeadersPolicyContentTypeOptionsModel
    ] = Field(default=None, alias="ContentTypeOptions")
    strict_transport_security: Optional[
        ResponseHeadersPolicyStrictTransportSecurityModel
    ] = Field(default=None, alias="StrictTransportSecurity")


class StreamingDistributionSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    status: str = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    domain_name: str = Field(alias="DomainName")
    s3_origin: S3OriginModel = Field(alias="S3Origin")
    aliases: AliasesModel = Field(alias="Aliases")
    trusted_signers: TrustedSignersModel = Field(alias="TrustedSigners")
    comment: str = Field(alias="Comment")
    price_class: Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"] = Field(
        alias="PriceClass"
    )
    enabled: bool = Field(alias="Enabled")


class StreamingDistributionConfigModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    s3_origin: S3OriginModel = Field(alias="S3Origin")
    comment: str = Field(alias="Comment")
    trusted_signers: TrustedSignersModel = Field(alias="TrustedSigners")
    enabled: bool = Field(alias="Enabled")
    aliases: Optional[AliasesModel] = Field(default=None, alias="Aliases")
    logging: Optional[StreamingLoggingConfigModel] = Field(
        default=None, alias="Logging"
    )
    price_class: Optional[
        Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
    ] = Field(default=None, alias="PriceClass")


class UntagResourceRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tag_keys: TagKeysModel = Field(alias="TagKeys")


class TagsModel(BaseModel):
    items: Optional[Sequence[TagModel]] = Field(default=None, alias="Items")


class ForwardedValuesModel(BaseModel):
    query_string: bool = Field(alias="QueryString")
    cookies: CookiePreferenceModel = Field(alias="Cookies")
    headers: Optional[HeadersModel] = Field(default=None, alias="Headers")
    query_string_cache_keys: Optional[QueryStringCacheKeysModel] = Field(
        default=None, alias="QueryStringCacheKeys"
    )


class ParametersInCacheKeyAndForwardedToOriginModel(BaseModel):
    enable_accept_encoding_gzip: bool = Field(alias="EnableAcceptEncodingGzip")
    headers_config: CachePolicyHeadersConfigModel = Field(alias="HeadersConfig")
    cookies_config: CachePolicyCookiesConfigModel = Field(alias="CookiesConfig")
    query_strings_config: CachePolicyQueryStringsConfigModel = Field(
        alias="QueryStringsConfig"
    )
    enable_accept_encoding_brotli: Optional[bool] = Field(
        default=None, alias="EnableAcceptEncodingBrotli"
    )


class OriginRequestPolicyConfigModel(BaseModel):
    name: str = Field(alias="Name")
    headers_config: OriginRequestPolicyHeadersConfigModel = Field(alias="HeadersConfig")
    cookies_config: OriginRequestPolicyCookiesConfigModel = Field(alias="CookiesConfig")
    query_strings_config: OriginRequestPolicyQueryStringsConfigModel = Field(
        alias="QueryStringsConfig"
    )
    comment: Optional[str] = Field(default=None, alias="Comment")


class CreateCloudFrontOriginAccessIdentityResultModel(BaseModel):
    cloud_front_origin_access_identity: CloudFrontOriginAccessIdentityModel = Field(
        alias="CloudFrontOriginAccessIdentity"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCloudFrontOriginAccessIdentityResultModel(BaseModel):
    cloud_front_origin_access_identity: CloudFrontOriginAccessIdentityModel = Field(
        alias="CloudFrontOriginAccessIdentity"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCloudFrontOriginAccessIdentityResultModel(BaseModel):
    cloud_front_origin_access_identity: CloudFrontOriginAccessIdentityModel = Field(
        alias="CloudFrontOriginAccessIdentity"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCloudFrontOriginAccessIdentitiesResultModel(BaseModel):
    cloud_front_origin_access_identity_list: CloudFrontOriginAccessIdentityListModel = (
        Field(alias="CloudFrontOriginAccessIdentityList")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConflictingAliasesResultModel(BaseModel):
    conflicting_aliases_list: ConflictingAliasesListModel = Field(
        alias="ConflictingAliasesList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContentTypeProfileConfigModel(BaseModel):
    forward_when_content_type_is_unknown: bool = Field(
        alias="ForwardWhenContentTypeIsUnknown"
    )
    content_type_profiles: Optional[ContentTypeProfilesModel] = Field(
        default=None, alias="ContentTypeProfiles"
    )


class TrafficConfigModel(BaseModel):
    type: Literal["SingleHeader", "SingleWeight"] = Field(alias="Type")
    single_weight_config: Optional[ContinuousDeploymentSingleWeightConfigModel] = Field(
        default=None, alias="SingleWeightConfig"
    )
    single_header_config: Optional[ContinuousDeploymentSingleHeaderConfigModel] = Field(
        default=None, alias="SingleHeaderConfig"
    )


class CreateKeyGroupResultModel(BaseModel):
    key_group: KeyGroupModel = Field(alias="KeyGroup")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyGroupResultModel(BaseModel):
    key_group: KeyGroupModel = Field(alias="KeyGroup")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class KeyGroupSummaryModel(BaseModel):
    key_group: KeyGroupModel = Field(alias="KeyGroup")


class UpdateKeyGroupResultModel(BaseModel):
    key_group: KeyGroupModel = Field(alias="KeyGroup")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOriginAccessControlResultModel(BaseModel):
    origin_access_control: OriginAccessControlModel = Field(alias="OriginAccessControl")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOriginAccessControlResultModel(BaseModel):
    origin_access_control: OriginAccessControlModel = Field(alias="OriginAccessControl")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOriginAccessControlResultModel(BaseModel):
    origin_access_control: OriginAccessControlModel = Field(alias="OriginAccessControl")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePublicKeyResultModel(BaseModel):
    public_key: PublicKeyModel = Field(alias="PublicKey")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPublicKeyResultModel(BaseModel):
    public_key: PublicKeyModel = Field(alias="PublicKey")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePublicKeyResultModel(BaseModel):
    public_key: PublicKeyModel = Field(alias="PublicKey")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginModel(BaseModel):
    id: str = Field(alias="Id")
    domain_name: str = Field(alias="DomainName")
    origin_path: Optional[str] = Field(default=None, alias="OriginPath")
    custom_headers: Optional[CustomHeadersModel] = Field(
        default=None, alias="CustomHeaders"
    )
    s3_origin_config: Optional[S3OriginConfigModel] = Field(
        default=None, alias="S3OriginConfig"
    )
    custom_origin_config: Optional[CustomOriginConfigModel] = Field(
        default=None, alias="CustomOriginConfig"
    )
    connection_attempts: Optional[int] = Field(default=None, alias="ConnectionAttempts")
    connection_timeout: Optional[int] = Field(default=None, alias="ConnectionTimeout")
    origin_shield: Optional[OriginShieldModel] = Field(
        default=None, alias="OriginShield"
    )
    origin_access_control_id: Optional[str] = Field(
        default=None, alias="OriginAccessControlId"
    )


class EncryptionEntitiesModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[Sequence[EncryptionEntityModel]] = Field(
        default=None, alias="Items"
    )


class CreateRealtimeLogConfigRequestModel(BaseModel):
    end_points: Sequence[EndPointModel] = Field(alias="EndPoints")
    fields: Sequence[str] = Field(alias="Fields")
    name: str = Field(alias="Name")
    sampling_rate: int = Field(alias="SamplingRate")


class RealtimeLogConfigModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    sampling_rate: int = Field(alias="SamplingRate")
    end_points: List[EndPointModel] = Field(alias="EndPoints")
    fields: List[str] = Field(alias="Fields")


class UpdateRealtimeLogConfigRequestModel(BaseModel):
    end_points: Optional[Sequence[EndPointModel]] = Field(
        default=None, alias="EndPoints"
    )
    fields: Optional[Sequence[str]] = Field(default=None, alias="Fields")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="ARN")
    sampling_rate: Optional[int] = Field(default=None, alias="SamplingRate")


class CreateFunctionResultModel(BaseModel):
    function_summary: FunctionSummaryModel = Field(alias="FunctionSummary")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFunctionResultModel(BaseModel):
    function_summary: FunctionSummaryModel = Field(alias="FunctionSummary")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[FunctionSummaryModel]] = Field(default=None, alias="Items")


class PublishFunctionResultModel(BaseModel):
    function_summary: FunctionSummaryModel = Field(alias="FunctionSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestResultModel(BaseModel):
    function_summary: Optional[FunctionSummaryModel] = Field(
        default=None, alias="FunctionSummary"
    )
    compute_utilization: Optional[str] = Field(default=None, alias="ComputeUtilization")
    function_execution_logs: Optional[List[str]] = Field(
        default=None, alias="FunctionExecutionLogs"
    )
    function_error_message: Optional[str] = Field(
        default=None, alias="FunctionErrorMessage"
    )
    function_output: Optional[str] = Field(default=None, alias="FunctionOutput")


class UpdateFunctionResultModel(BaseModel):
    function_summary: FunctionSummaryModel = Field(alias="FunctionSummary")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInvalidationRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    invalidation_batch: InvalidationBatchModel = Field(alias="InvalidationBatch")


class InvalidationModel(BaseModel):
    id: str = Field(alias="Id")
    status: str = Field(alias="Status")
    create_time: datetime = Field(alias="CreateTime")
    invalidation_batch: InvalidationBatchModel = Field(alias="InvalidationBatch")


class ListInvalidationsResultModel(BaseModel):
    invalidation_list: InvalidationListModel = Field(alias="InvalidationList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActiveTrustedKeyGroupsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    quantity: int = Field(alias="Quantity")
    items: Optional[List[KGKeyPairIdsModel]] = Field(default=None, alias="Items")


class ActiveTrustedSignersModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    quantity: int = Field(alias="Quantity")
    items: Optional[List[SignerModel]] = Field(default=None, alias="Items")


class CreateMonitoringSubscriptionRequestModel(BaseModel):
    distribution_id: str = Field(alias="DistributionId")
    monitoring_subscription: MonitoringSubscriptionModel = Field(
        alias="MonitoringSubscription"
    )


class CreateMonitoringSubscriptionResultModel(BaseModel):
    monitoring_subscription: MonitoringSubscriptionModel = Field(
        alias="MonitoringSubscription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMonitoringSubscriptionResultModel(BaseModel):
    monitoring_subscription: MonitoringSubscriptionModel = Field(
        alias="MonitoringSubscription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOriginAccessControlsResultModel(BaseModel):
    origin_access_control_list: OriginAccessControlListModel = Field(
        alias="OriginAccessControlList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginGroupModel(BaseModel):
    id: str = Field(alias="Id")
    failover_criteria: OriginGroupFailoverCriteriaModel = Field(
        alias="FailoverCriteria"
    )
    members: OriginGroupMembersModel = Field(alias="Members")


class ListPublicKeysResultModel(BaseModel):
    public_key_list: PublicKeyListModel = Field(alias="PublicKeyList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryArgProfileConfigModel(BaseModel):
    forward_when_query_arg_profile_is_unknown: bool = Field(
        alias="ForwardWhenQueryArgProfileIsUnknown"
    )
    query_arg_profiles: Optional[QueryArgProfilesModel] = Field(
        default=None, alias="QueryArgProfiles"
    )


class ResponseHeadersPolicyConfigModel(BaseModel):
    name: str = Field(alias="Name")
    comment: Optional[str] = Field(default=None, alias="Comment")
    cors_config: Optional[ResponseHeadersPolicyCorsConfigModel] = Field(
        default=None, alias="CorsConfig"
    )
    security_headers_config: Optional[
        ResponseHeadersPolicySecurityHeadersConfigModel
    ] = Field(default=None, alias="SecurityHeadersConfig")
    server_timing_headers_config: Optional[
        ResponseHeadersPolicyServerTimingHeadersConfigModel
    ] = Field(default=None, alias="ServerTimingHeadersConfig")
    custom_headers_config: Optional[
        ResponseHeadersPolicyCustomHeadersConfigModel
    ] = Field(default=None, alias="CustomHeadersConfig")
    remove_headers_config: Optional[
        ResponseHeadersPolicyRemoveHeadersConfigModel
    ] = Field(default=None, alias="RemoveHeadersConfig")


class StreamingDistributionListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[StreamingDistributionSummaryModel]] = Field(
        default=None, alias="Items"
    )


class CreateStreamingDistributionRequestModel(BaseModel):
    streaming_distribution_config: StreamingDistributionConfigModel = Field(
        alias="StreamingDistributionConfig"
    )


class GetStreamingDistributionConfigResultModel(BaseModel):
    streaming_distribution_config: StreamingDistributionConfigModel = Field(
        alias="StreamingDistributionConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStreamingDistributionRequestModel(BaseModel):
    streaming_distribution_config: StreamingDistributionConfigModel = Field(
        alias="StreamingDistributionConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class ListTagsForResourceResultModel(BaseModel):
    tags: TagsModel = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamingDistributionConfigWithTagsModel(BaseModel):
    streaming_distribution_config: StreamingDistributionConfigModel = Field(
        alias="StreamingDistributionConfig"
    )
    tags: TagsModel = Field(alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tags: TagsModel = Field(alias="Tags")


class CacheBehaviorModel(BaseModel):
    path_pattern: str = Field(alias="PathPattern")
    target_origin_id: str = Field(alias="TargetOriginId")
    viewer_protocol_policy: Literal[
        "allow-all", "https-only", "redirect-to-https"
    ] = Field(alias="ViewerProtocolPolicy")
    trusted_signers: Optional[TrustedSignersModel] = Field(
        default=None, alias="TrustedSigners"
    )
    trusted_key_groups: Optional[TrustedKeyGroupsModel] = Field(
        default=None, alias="TrustedKeyGroups"
    )
    allowed_methods: Optional[AllowedMethodsModel] = Field(
        default=None, alias="AllowedMethods"
    )
    smooth_streaming: Optional[bool] = Field(default=None, alias="SmoothStreaming")
    compress: Optional[bool] = Field(default=None, alias="Compress")
    lambda_function_associations: Optional[LambdaFunctionAssociationsModel] = Field(
        default=None, alias="LambdaFunctionAssociations"
    )
    function_associations: Optional[FunctionAssociationsModel] = Field(
        default=None, alias="FunctionAssociations"
    )
    field_level_encryption_id: Optional[str] = Field(
        default=None, alias="FieldLevelEncryptionId"
    )
    realtime_log_config_arn: Optional[str] = Field(
        default=None, alias="RealtimeLogConfigArn"
    )
    cache_policy_id: Optional[str] = Field(default=None, alias="CachePolicyId")
    origin_request_policy_id: Optional[str] = Field(
        default=None, alias="OriginRequestPolicyId"
    )
    response_headers_policy_id: Optional[str] = Field(
        default=None, alias="ResponseHeadersPolicyId"
    )
    forwarded_values: Optional[ForwardedValuesModel] = Field(
        default=None, alias="ForwardedValues"
    )
    min_ttl: Optional[int] = Field(default=None, alias="MinTTL")
    default_ttl: Optional[int] = Field(default=None, alias="DefaultTTL")
    max_ttl: Optional[int] = Field(default=None, alias="MaxTTL")


class DefaultCacheBehaviorModel(BaseModel):
    target_origin_id: str = Field(alias="TargetOriginId")
    viewer_protocol_policy: Literal[
        "allow-all", "https-only", "redirect-to-https"
    ] = Field(alias="ViewerProtocolPolicy")
    trusted_signers: Optional[TrustedSignersModel] = Field(
        default=None, alias="TrustedSigners"
    )
    trusted_key_groups: Optional[TrustedKeyGroupsModel] = Field(
        default=None, alias="TrustedKeyGroups"
    )
    allowed_methods: Optional[AllowedMethodsModel] = Field(
        default=None, alias="AllowedMethods"
    )
    smooth_streaming: Optional[bool] = Field(default=None, alias="SmoothStreaming")
    compress: Optional[bool] = Field(default=None, alias="Compress")
    lambda_function_associations: Optional[LambdaFunctionAssociationsModel] = Field(
        default=None, alias="LambdaFunctionAssociations"
    )
    function_associations: Optional[FunctionAssociationsModel] = Field(
        default=None, alias="FunctionAssociations"
    )
    field_level_encryption_id: Optional[str] = Field(
        default=None, alias="FieldLevelEncryptionId"
    )
    realtime_log_config_arn: Optional[str] = Field(
        default=None, alias="RealtimeLogConfigArn"
    )
    cache_policy_id: Optional[str] = Field(default=None, alias="CachePolicyId")
    origin_request_policy_id: Optional[str] = Field(
        default=None, alias="OriginRequestPolicyId"
    )
    response_headers_policy_id: Optional[str] = Field(
        default=None, alias="ResponseHeadersPolicyId"
    )
    forwarded_values: Optional[ForwardedValuesModel] = Field(
        default=None, alias="ForwardedValues"
    )
    min_ttl: Optional[int] = Field(default=None, alias="MinTTL")
    default_ttl: Optional[int] = Field(default=None, alias="DefaultTTL")
    max_ttl: Optional[int] = Field(default=None, alias="MaxTTL")


class CachePolicyConfigModel(BaseModel):
    name: str = Field(alias="Name")
    min_ttl: int = Field(alias="MinTTL")
    comment: Optional[str] = Field(default=None, alias="Comment")
    default_ttl: Optional[int] = Field(default=None, alias="DefaultTTL")
    max_ttl: Optional[int] = Field(default=None, alias="MaxTTL")
    parameters_in_cache_key_and_forwarded_to_origin: Optional[
        ParametersInCacheKeyAndForwardedToOriginModel
    ] = Field(default=None, alias="ParametersInCacheKeyAndForwardedToOrigin")


class CreateOriginRequestPolicyRequestModel(BaseModel):
    origin_request_policy_config: OriginRequestPolicyConfigModel = Field(
        alias="OriginRequestPolicyConfig"
    )


class GetOriginRequestPolicyConfigResultModel(BaseModel):
    origin_request_policy_config: OriginRequestPolicyConfigModel = Field(
        alias="OriginRequestPolicyConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginRequestPolicyModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    origin_request_policy_config: OriginRequestPolicyConfigModel = Field(
        alias="OriginRequestPolicyConfig"
    )


class UpdateOriginRequestPolicyRequestModel(BaseModel):
    origin_request_policy_config: OriginRequestPolicyConfigModel = Field(
        alias="OriginRequestPolicyConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class ContinuousDeploymentPolicyConfigModel(BaseModel):
    staging_distribution_dns_names: StagingDistributionDnsNamesModel = Field(
        alias="StagingDistributionDnsNames"
    )
    enabled: bool = Field(alias="Enabled")
    traffic_config: Optional[TrafficConfigModel] = Field(
        default=None, alias="TrafficConfig"
    )


class KeyGroupListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[KeyGroupSummaryModel]] = Field(default=None, alias="Items")


class OriginsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: List[OriginModel] = Field(alias="Items")


class FieldLevelEncryptionProfileConfigModel(BaseModel):
    name: str = Field(alias="Name")
    caller_reference: str = Field(alias="CallerReference")
    encryption_entities: EncryptionEntitiesModel = Field(alias="EncryptionEntities")
    comment: Optional[str] = Field(default=None, alias="Comment")


class FieldLevelEncryptionProfileSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    encryption_entities: EncryptionEntitiesModel = Field(alias="EncryptionEntities")
    comment: Optional[str] = Field(default=None, alias="Comment")


class CreateRealtimeLogConfigResultModel(BaseModel):
    realtime_log_config: RealtimeLogConfigModel = Field(alias="RealtimeLogConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRealtimeLogConfigResultModel(BaseModel):
    realtime_log_config: RealtimeLogConfigModel = Field(alias="RealtimeLogConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RealtimeLogConfigsModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    items: Optional[List[RealtimeLogConfigModel]] = Field(default=None, alias="Items")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")


class UpdateRealtimeLogConfigResultModel(BaseModel):
    realtime_log_config: RealtimeLogConfigModel = Field(alias="RealtimeLogConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionsResultModel(BaseModel):
    function_list: FunctionListModel = Field(alias="FunctionList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestFunctionResultModel(BaseModel):
    test_result: TestResultModel = Field(alias="TestResult")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInvalidationResultModel(BaseModel):
    location: str = Field(alias="Location")
    invalidation: InvalidationModel = Field(alias="Invalidation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInvalidationResultModel(BaseModel):
    invalidation: InvalidationModel = Field(alias="Invalidation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamingDistributionModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    status: str = Field(alias="Status")
    domain_name: str = Field(alias="DomainName")
    active_trusted_signers: ActiveTrustedSignersModel = Field(
        alias="ActiveTrustedSigners"
    )
    streaming_distribution_config: StreamingDistributionConfigModel = Field(
        alias="StreamingDistributionConfig"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class OriginGroupsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[OriginGroupModel]] = Field(default=None, alias="Items")


class FieldLevelEncryptionConfigModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    comment: Optional[str] = Field(default=None, alias="Comment")
    query_arg_profile_config: Optional[QueryArgProfileConfigModel] = Field(
        default=None, alias="QueryArgProfileConfig"
    )
    content_type_profile_config: Optional[ContentTypeProfileConfigModel] = Field(
        default=None, alias="ContentTypeProfileConfig"
    )


class FieldLevelEncryptionSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    comment: Optional[str] = Field(default=None, alias="Comment")
    query_arg_profile_config: Optional[QueryArgProfileConfigModel] = Field(
        default=None, alias="QueryArgProfileConfig"
    )
    content_type_profile_config: Optional[ContentTypeProfileConfigModel] = Field(
        default=None, alias="ContentTypeProfileConfig"
    )


class CreateResponseHeadersPolicyRequestModel(BaseModel):
    response_headers_policy_config: ResponseHeadersPolicyConfigModel = Field(
        alias="ResponseHeadersPolicyConfig"
    )


class GetResponseHeadersPolicyConfigResultModel(BaseModel):
    response_headers_policy_config: ResponseHeadersPolicyConfigModel = Field(
        alias="ResponseHeadersPolicyConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResponseHeadersPolicyModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_headers_policy_config: ResponseHeadersPolicyConfigModel = Field(
        alias="ResponseHeadersPolicyConfig"
    )


class UpdateResponseHeadersPolicyRequestModel(BaseModel):
    response_headers_policy_config: ResponseHeadersPolicyConfigModel = Field(
        alias="ResponseHeadersPolicyConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class ListStreamingDistributionsResultModel(BaseModel):
    streaming_distribution_list: StreamingDistributionListModel = Field(
        alias="StreamingDistributionList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamingDistributionWithTagsRequestModel(BaseModel):
    streaming_distribution_config_with_tags: StreamingDistributionConfigWithTagsModel = Field(
        alias="StreamingDistributionConfigWithTags"
    )


class CacheBehaviorsModel(BaseModel):
    quantity: int = Field(alias="Quantity")
    items: Optional[List[CacheBehaviorModel]] = Field(default=None, alias="Items")


class CachePolicyModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    cache_policy_config: CachePolicyConfigModel = Field(alias="CachePolicyConfig")


class CreateCachePolicyRequestModel(BaseModel):
    cache_policy_config: CachePolicyConfigModel = Field(alias="CachePolicyConfig")


class GetCachePolicyConfigResultModel(BaseModel):
    cache_policy_config: CachePolicyConfigModel = Field(alias="CachePolicyConfig")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCachePolicyRequestModel(BaseModel):
    cache_policy_config: CachePolicyConfigModel = Field(alias="CachePolicyConfig")
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class CreateOriginRequestPolicyResultModel(BaseModel):
    origin_request_policy: OriginRequestPolicyModel = Field(alias="OriginRequestPolicy")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOriginRequestPolicyResultModel(BaseModel):
    origin_request_policy: OriginRequestPolicyModel = Field(alias="OriginRequestPolicy")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginRequestPolicySummaryModel(BaseModel):
    type: Literal["custom", "managed"] = Field(alias="Type")
    origin_request_policy: OriginRequestPolicyModel = Field(alias="OriginRequestPolicy")


class UpdateOriginRequestPolicyResultModel(BaseModel):
    origin_request_policy: OriginRequestPolicyModel = Field(alias="OriginRequestPolicy")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContinuousDeploymentPolicyModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    continuous_deployment_policy_config: ContinuousDeploymentPolicyConfigModel = Field(
        alias="ContinuousDeploymentPolicyConfig"
    )


class CreateContinuousDeploymentPolicyRequestModel(BaseModel):
    continuous_deployment_policy_config: ContinuousDeploymentPolicyConfigModel = Field(
        alias="ContinuousDeploymentPolicyConfig"
    )


class GetContinuousDeploymentPolicyConfigResultModel(BaseModel):
    continuous_deployment_policy_config: ContinuousDeploymentPolicyConfigModel = Field(
        alias="ContinuousDeploymentPolicyConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContinuousDeploymentPolicyRequestModel(BaseModel):
    continuous_deployment_policy_config: ContinuousDeploymentPolicyConfigModel = Field(
        alias="ContinuousDeploymentPolicyConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class ListKeyGroupsResultModel(BaseModel):
    key_group_list: KeyGroupListModel = Field(alias="KeyGroupList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFieldLevelEncryptionProfileRequestModel(BaseModel):
    field_level_encryption_profile_config: FieldLevelEncryptionProfileConfigModel = (
        Field(alias="FieldLevelEncryptionProfileConfig")
    )


class FieldLevelEncryptionProfileModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    field_level_encryption_profile_config: FieldLevelEncryptionProfileConfigModel = (
        Field(alias="FieldLevelEncryptionProfileConfig")
    )


class GetFieldLevelEncryptionProfileConfigResultModel(BaseModel):
    field_level_encryption_profile_config: FieldLevelEncryptionProfileConfigModel = (
        Field(alias="FieldLevelEncryptionProfileConfig")
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFieldLevelEncryptionProfileRequestModel(BaseModel):
    field_level_encryption_profile_config: FieldLevelEncryptionProfileConfigModel = (
        Field(alias="FieldLevelEncryptionProfileConfig")
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class FieldLevelEncryptionProfileListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[FieldLevelEncryptionProfileSummaryModel]] = Field(
        default=None, alias="Items"
    )


class ListRealtimeLogConfigsResultModel(BaseModel):
    realtime_log_configs: RealtimeLogConfigsModel = Field(alias="RealtimeLogConfigs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamingDistributionResultModel(BaseModel):
    streaming_distribution: StreamingDistributionModel = Field(
        alias="StreamingDistribution"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamingDistributionWithTagsResultModel(BaseModel):
    streaming_distribution: StreamingDistributionModel = Field(
        alias="StreamingDistribution"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamingDistributionResultModel(BaseModel):
    streaming_distribution: StreamingDistributionModel = Field(
        alias="StreamingDistribution"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStreamingDistributionResultModel(BaseModel):
    streaming_distribution: StreamingDistributionModel = Field(
        alias="StreamingDistribution"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFieldLevelEncryptionConfigRequestModel(BaseModel):
    field_level_encryption_config: FieldLevelEncryptionConfigModel = Field(
        alias="FieldLevelEncryptionConfig"
    )


class FieldLevelEncryptionModel(BaseModel):
    id: str = Field(alias="Id")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    field_level_encryption_config: FieldLevelEncryptionConfigModel = Field(
        alias="FieldLevelEncryptionConfig"
    )


class GetFieldLevelEncryptionConfigResultModel(BaseModel):
    field_level_encryption_config: FieldLevelEncryptionConfigModel = Field(
        alias="FieldLevelEncryptionConfig"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFieldLevelEncryptionConfigRequestModel(BaseModel):
    field_level_encryption_config: FieldLevelEncryptionConfigModel = Field(
        alias="FieldLevelEncryptionConfig"
    )
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class FieldLevelEncryptionListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[FieldLevelEncryptionSummaryModel]] = Field(
        default=None, alias="Items"
    )


class CreateResponseHeadersPolicyResultModel(BaseModel):
    response_headers_policy: ResponseHeadersPolicyModel = Field(
        alias="ResponseHeadersPolicy"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResponseHeadersPolicyResultModel(BaseModel):
    response_headers_policy: ResponseHeadersPolicyModel = Field(
        alias="ResponseHeadersPolicy"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResponseHeadersPolicySummaryModel(BaseModel):
    type: Literal["custom", "managed"] = Field(alias="Type")
    response_headers_policy: ResponseHeadersPolicyModel = Field(
        alias="ResponseHeadersPolicy"
    )


class UpdateResponseHeadersPolicyResultModel(BaseModel):
    response_headers_policy: ResponseHeadersPolicyModel = Field(
        alias="ResponseHeadersPolicy"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DistributionConfigModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    origins: OriginsModel = Field(alias="Origins")
    default_cache_behavior: DefaultCacheBehaviorModel = Field(
        alias="DefaultCacheBehavior"
    )
    comment: str = Field(alias="Comment")
    enabled: bool = Field(alias="Enabled")
    aliases: Optional[AliasesModel] = Field(default=None, alias="Aliases")
    default_root_object: Optional[str] = Field(default=None, alias="DefaultRootObject")
    origin_groups: Optional[OriginGroupsModel] = Field(
        default=None, alias="OriginGroups"
    )
    cache_behaviors: Optional[CacheBehaviorsModel] = Field(
        default=None, alias="CacheBehaviors"
    )
    custom_error_responses: Optional[CustomErrorResponsesModel] = Field(
        default=None, alias="CustomErrorResponses"
    )
    logging: Optional[LoggingConfigModel] = Field(default=None, alias="Logging")
    price_class: Optional[
        Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
    ] = Field(default=None, alias="PriceClass")
    viewer_certificate: Optional[ViewerCertificateModel] = Field(
        default=None, alias="ViewerCertificate"
    )
    restrictions: Optional[RestrictionsModel] = Field(
        default=None, alias="Restrictions"
    )
    web_acl_id: Optional[str] = Field(default=None, alias="WebACLId")
    http_version: Optional[Literal["http1.1", "http2", "http2and3", "http3"]] = Field(
        default=None, alias="HttpVersion"
    )
    is_ip_v6_enabled: Optional[bool] = Field(default=None, alias="IsIPV6Enabled")
    continuous_deployment_policy_id: Optional[str] = Field(
        default=None, alias="ContinuousDeploymentPolicyId"
    )
    staging: Optional[bool] = Field(default=None, alias="Staging")


class DistributionSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    status: str = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    domain_name: str = Field(alias="DomainName")
    aliases: AliasesModel = Field(alias="Aliases")
    origins: OriginsModel = Field(alias="Origins")
    default_cache_behavior: DefaultCacheBehaviorModel = Field(
        alias="DefaultCacheBehavior"
    )
    cache_behaviors: CacheBehaviorsModel = Field(alias="CacheBehaviors")
    custom_error_responses: CustomErrorResponsesModel = Field(
        alias="CustomErrorResponses"
    )
    comment: str = Field(alias="Comment")
    price_class: Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"] = Field(
        alias="PriceClass"
    )
    enabled: bool = Field(alias="Enabled")
    viewer_certificate: ViewerCertificateModel = Field(alias="ViewerCertificate")
    restrictions: RestrictionsModel = Field(alias="Restrictions")
    web_acl_id: str = Field(alias="WebACLId")
    http_version: Literal["http1.1", "http2", "http2and3", "http3"] = Field(
        alias="HttpVersion"
    )
    is_ip_v6_enabled: bool = Field(alias="IsIPV6Enabled")
    staging: bool = Field(alias="Staging")
    origin_groups: Optional[OriginGroupsModel] = Field(
        default=None, alias="OriginGroups"
    )
    alias_icp_recordals: Optional[List[AliasICPRecordalModel]] = Field(
        default=None, alias="AliasICPRecordals"
    )


class CachePolicySummaryModel(BaseModel):
    type: Literal["custom", "managed"] = Field(alias="Type")
    cache_policy: CachePolicyModel = Field(alias="CachePolicy")


class CreateCachePolicyResultModel(BaseModel):
    cache_policy: CachePolicyModel = Field(alias="CachePolicy")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCachePolicyResultModel(BaseModel):
    cache_policy: CachePolicyModel = Field(alias="CachePolicy")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCachePolicyResultModel(BaseModel):
    cache_policy: CachePolicyModel = Field(alias="CachePolicy")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OriginRequestPolicyListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[OriginRequestPolicySummaryModel]] = Field(
        default=None, alias="Items"
    )


class ContinuousDeploymentPolicySummaryModel(BaseModel):
    continuous_deployment_policy: ContinuousDeploymentPolicyModel = Field(
        alias="ContinuousDeploymentPolicy"
    )


class CreateContinuousDeploymentPolicyResultModel(BaseModel):
    continuous_deployment_policy: ContinuousDeploymentPolicyModel = Field(
        alias="ContinuousDeploymentPolicy"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContinuousDeploymentPolicyResultModel(BaseModel):
    continuous_deployment_policy: ContinuousDeploymentPolicyModel = Field(
        alias="ContinuousDeploymentPolicy"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContinuousDeploymentPolicyResultModel(BaseModel):
    continuous_deployment_policy: ContinuousDeploymentPolicyModel = Field(
        alias="ContinuousDeploymentPolicy"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFieldLevelEncryptionProfileResultModel(BaseModel):
    field_level_encryption_profile: FieldLevelEncryptionProfileModel = Field(
        alias="FieldLevelEncryptionProfile"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFieldLevelEncryptionProfileResultModel(BaseModel):
    field_level_encryption_profile: FieldLevelEncryptionProfileModel = Field(
        alias="FieldLevelEncryptionProfile"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFieldLevelEncryptionProfileResultModel(BaseModel):
    field_level_encryption_profile: FieldLevelEncryptionProfileModel = Field(
        alias="FieldLevelEncryptionProfile"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFieldLevelEncryptionProfilesResultModel(BaseModel):
    field_level_encryption_profile_list: FieldLevelEncryptionProfileListModel = Field(
        alias="FieldLevelEncryptionProfileList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFieldLevelEncryptionConfigResultModel(BaseModel):
    field_level_encryption: FieldLevelEncryptionModel = Field(
        alias="FieldLevelEncryption"
    )
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFieldLevelEncryptionResultModel(BaseModel):
    field_level_encryption: FieldLevelEncryptionModel = Field(
        alias="FieldLevelEncryption"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFieldLevelEncryptionConfigResultModel(BaseModel):
    field_level_encryption: FieldLevelEncryptionModel = Field(
        alias="FieldLevelEncryption"
    )
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFieldLevelEncryptionConfigsResultModel(BaseModel):
    field_level_encryption_list: FieldLevelEncryptionListModel = Field(
        alias="FieldLevelEncryptionList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResponseHeadersPolicyListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[ResponseHeadersPolicySummaryModel]] = Field(
        default=None, alias="Items"
    )


class CreateDistributionRequestModel(BaseModel):
    distribution_config: DistributionConfigModel = Field(alias="DistributionConfig")


class DistributionConfigWithTagsModel(BaseModel):
    distribution_config: DistributionConfigModel = Field(alias="DistributionConfig")
    tags: TagsModel = Field(alias="Tags")


class DistributionModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="ARN")
    status: str = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    in_progress_invalidation_batches: int = Field(alias="InProgressInvalidationBatches")
    domain_name: str = Field(alias="DomainName")
    distribution_config: DistributionConfigModel = Field(alias="DistributionConfig")
    active_trusted_signers: Optional[ActiveTrustedSignersModel] = Field(
        default=None, alias="ActiveTrustedSigners"
    )
    active_trusted_key_groups: Optional[ActiveTrustedKeyGroupsModel] = Field(
        default=None, alias="ActiveTrustedKeyGroups"
    )
    alias_icp_recordals: Optional[List[AliasICPRecordalModel]] = Field(
        default=None, alias="AliasICPRecordals"
    )


class GetDistributionConfigResultModel(BaseModel):
    distribution_config: DistributionConfigModel = Field(alias="DistributionConfig")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionRequestModel(BaseModel):
    distribution_config: DistributionConfigModel = Field(alias="DistributionConfig")
    id: str = Field(alias="Id")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")


class DistributionListModel(BaseModel):
    marker: str = Field(alias="Marker")
    max_items: int = Field(alias="MaxItems")
    is_truncated: bool = Field(alias="IsTruncated")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[DistributionSummaryModel]] = Field(default=None, alias="Items")


class CachePolicyListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[CachePolicySummaryModel]] = Field(default=None, alias="Items")


class ListOriginRequestPoliciesResultModel(BaseModel):
    origin_request_policy_list: OriginRequestPolicyListModel = Field(
        alias="OriginRequestPolicyList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContinuousDeploymentPolicyListModel(BaseModel):
    max_items: int = Field(alias="MaxItems")
    quantity: int = Field(alias="Quantity")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    items: Optional[List[ContinuousDeploymentPolicySummaryModel]] = Field(
        default=None, alias="Items"
    )


class ListResponseHeadersPoliciesResultModel(BaseModel):
    response_headers_policy_list: ResponseHeadersPolicyListModel = Field(
        alias="ResponseHeadersPolicyList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionWithTagsRequestModel(BaseModel):
    distribution_config_with_tags: DistributionConfigWithTagsModel = Field(
        alias="DistributionConfigWithTags"
    )


class CopyDistributionResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionWithTagsResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    location: str = Field(alias="Location")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDistributionResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionWithStagingConfigResultModel(BaseModel):
    distribution: DistributionModel = Field(alias="Distribution")
    etag: str = Field(alias="ETag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsByRealtimeLogConfigResultModel(BaseModel):
    distribution_list: DistributionListModel = Field(alias="DistributionList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsByWebACLIdResultModel(BaseModel):
    distribution_list: DistributionListModel = Field(alias="DistributionList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributionsResultModel(BaseModel):
    distribution_list: DistributionListModel = Field(alias="DistributionList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCachePoliciesResultModel(BaseModel):
    cache_policy_list: CachePolicyListModel = Field(alias="CachePolicyList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContinuousDeploymentPoliciesResultModel(BaseModel):
    continuous_deployment_policy_list: ContinuousDeploymentPolicyListModel = Field(
        alias="ContinuousDeploymentPolicyList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
