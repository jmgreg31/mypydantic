# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AuthenticateCognitoActionConfigModel(BaseModel):
    user_pool_arn: str = Field(alias="UserPoolArn")
    user_pool_client_id: str = Field(alias="UserPoolClientId")
    user_pool_domain: str = Field(alias="UserPoolDomain")
    session_cookie_name: Optional[str] = Field(default=None, alias="SessionCookieName")
    scope: Optional[str] = Field(default=None, alias="Scope")
    session_timeout: Optional[int] = Field(default=None, alias="SessionTimeout")
    authentication_request_extra_params: Optional[Mapping[str, str]] = Field(
        default=None, alias="AuthenticationRequestExtraParams"
    )
    on_unauthenticated_request: Optional[
        Literal["allow", "authenticate", "deny"]
    ] = Field(default=None, alias="OnUnauthenticatedRequest")


class AuthenticateOidcActionConfigModel(BaseModel):
    issuer: str = Field(alias="Issuer")
    authorization_endpoint: str = Field(alias="AuthorizationEndpoint")
    token_endpoint: str = Field(alias="TokenEndpoint")
    user_info_endpoint: str = Field(alias="UserInfoEndpoint")
    client_id: str = Field(alias="ClientId")
    client_secret: Optional[str] = Field(default=None, alias="ClientSecret")
    session_cookie_name: Optional[str] = Field(default=None, alias="SessionCookieName")
    scope: Optional[str] = Field(default=None, alias="Scope")
    session_timeout: Optional[int] = Field(default=None, alias="SessionTimeout")
    authentication_request_extra_params: Optional[Mapping[str, str]] = Field(
        default=None, alias="AuthenticationRequestExtraParams"
    )
    on_unauthenticated_request: Optional[
        Literal["allow", "authenticate", "deny"]
    ] = Field(default=None, alias="OnUnauthenticatedRequest")
    use_existing_client_secret: Optional[bool] = Field(
        default=None, alias="UseExistingClientSecret"
    )


class FixedResponseActionConfigModel(BaseModel):
    status_code: str = Field(alias="StatusCode")
    message_body: Optional[str] = Field(default=None, alias="MessageBody")
    content_type: Optional[str] = Field(default=None, alias="ContentType")


class RedirectActionConfigModel(BaseModel):
    status_code: Literal["HTTP_301", "HTTP_302"] = Field(alias="StatusCode")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    port: Optional[str] = Field(default=None, alias="Port")
    host: Optional[str] = Field(default=None, alias="Host")
    path: Optional[str] = Field(default=None, alias="Path")
    query: Optional[str] = Field(default=None, alias="Query")


class CertificateModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class LoadBalancerAddressModel(BaseModel):
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    allocation_id: Optional[str] = Field(default=None, alias="AllocationId")
    private_ipv4_address: Optional[str] = Field(
        default=None, alias="PrivateIPv4Address"
    )
    ipv6_address: Optional[str] = Field(default=None, alias="IPv6Address")


class CipherModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    priority: Optional[int] = Field(default=None, alias="Priority")


class SubnetMappingModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    allocation_id: Optional[str] = Field(default=None, alias="AllocationId")
    private_ipv4_address: Optional[str] = Field(
        default=None, alias="PrivateIPv4Address"
    )
    ipv6_address: Optional[str] = Field(default=None, alias="IPv6Address")


class MatcherModel(BaseModel):
    http_code: Optional[str] = Field(default=None, alias="HttpCode")
    grpc_code: Optional[str] = Field(default=None, alias="GrpcCode")


class DeleteListenerInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")


class DeleteLoadBalancerInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")


class DeleteRuleInputRequestModel(BaseModel):
    rule_arn: str = Field(alias="RuleArn")


class DeleteTargetGroupInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")


class TargetDescriptionModel(BaseModel):
    id: str = Field(alias="Id")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccountLimitsInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class LimitModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    max: Optional[str] = Field(default=None, alias="Max")


class DescribeListenerCertificatesInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class DescribeListenersInputRequestModel(BaseModel):
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    listener_arns: Optional[Sequence[str]] = Field(default=None, alias="ListenerArns")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class DescribeLoadBalancerAttributesInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")


class LoadBalancerAttributeModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeLoadBalancersInputRequestModel(BaseModel):
    load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class DescribeRulesInputRequestModel(BaseModel):
    listener_arn: Optional[str] = Field(default=None, alias="ListenerArn")
    rule_arns: Optional[Sequence[str]] = Field(default=None, alias="RuleArns")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class DescribeSSLPoliciesInputRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    load_balancer_type: Optional[Literal["application", "gateway", "network"]] = Field(
        default=None, alias="LoadBalancerType"
    )


class DescribeTagsInputRequestModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="ResourceArns")


class DescribeTargetGroupAttributesInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")


class TargetGroupAttributeModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class DescribeTargetGroupsInputRequestModel(BaseModel):
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    target_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TargetGroupArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class TargetGroupStickinessConfigModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")


class TargetGroupTupleModel(BaseModel):
    target_group_arn: Optional[str] = Field(default=None, alias="TargetGroupArn")
    weight: Optional[int] = Field(default=None, alias="Weight")


class HostHeaderConditionConfigModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class HttpHeaderConditionConfigModel(BaseModel):
    http_header_name: Optional[str] = Field(default=None, alias="HttpHeaderName")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class HttpRequestMethodConditionConfigModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class LoadBalancerStateModel(BaseModel):
    code: Optional[
        Literal["active", "active_impaired", "failed", "provisioning"]
    ] = Field(default=None, alias="Code")
    reason: Optional[str] = Field(default=None, alias="Reason")


class PathPatternConditionConfigModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class QueryStringKeyValuePairModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class RemoveTagsInputRequestModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="ResourceArns")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class SourceIpConditionConfigModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class RulePriorityPairModel(BaseModel):
    rule_arn: Optional[str] = Field(default=None, alias="RuleArn")
    priority: Optional[int] = Field(default=None, alias="Priority")


class SetIpAddressTypeInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")
    ip_address_type: Literal["dualstack", "ipv4"] = Field(alias="IpAddressType")


class SetSecurityGroupsInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")
    security_groups: Sequence[str] = Field(alias="SecurityGroups")


class TargetHealthModel(BaseModel):
    state: Optional[
        Literal["draining", "healthy", "initial", "unavailable", "unhealthy", "unused"]
    ] = Field(default=None, alias="State")
    reason: Optional[
        Literal[
            "Elb.InitialHealthChecking",
            "Elb.InternalError",
            "Elb.RegistrationInProgress",
            "Target.DeregistrationInProgress",
            "Target.FailedHealthChecks",
            "Target.HealthCheckDisabled",
            "Target.InvalidState",
            "Target.IpUnusable",
            "Target.NotInUse",
            "Target.NotRegistered",
            "Target.ResponseCodeMismatch",
            "Target.Timeout",
        ]
    ] = Field(default=None, alias="Reason")
    description: Optional[str] = Field(default=None, alias="Description")


class AddListenerCertificatesInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    certificates: Sequence[CertificateModel] = Field(alias="Certificates")


class RemoveListenerCertificatesInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    certificates: Sequence[CertificateModel] = Field(alias="Certificates")


class AddListenerCertificatesOutputModel(BaseModel):
    certificates: List[CertificateModel] = Field(alias="Certificates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeListenerCertificatesOutputModel(BaseModel):
    certificates: List[CertificateModel] = Field(alias="Certificates")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetIpAddressTypeOutputModel(BaseModel):
    ip_address_type: Literal["dualstack", "ipv4"] = Field(alias="IpAddressType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetSecurityGroupsOutputModel(BaseModel):
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsInputRequestModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="ResourceArns")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class AvailabilityZoneModel(BaseModel):
    zone_name: Optional[str] = Field(default=None, alias="ZoneName")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")
    load_balancer_addresses: Optional[List[LoadBalancerAddressModel]] = Field(
        default=None, alias="LoadBalancerAddresses"
    )


class SslPolicyModel(BaseModel):
    ssl_protocols: Optional[List[str]] = Field(default=None, alias="SslProtocols")
    ciphers: Optional[List[CipherModel]] = Field(default=None, alias="Ciphers")
    name: Optional[str] = Field(default=None, alias="Name")
    supported_load_balancer_types: Optional[List[str]] = Field(
        default=None, alias="SupportedLoadBalancerTypes"
    )


class CreateLoadBalancerInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")
    subnet_mappings: Optional[Sequence[SubnetMappingModel]] = Field(
        default=None, alias="SubnetMappings"
    )
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    scheme: Optional[Literal["internal", "internet-facing"]] = Field(
        default=None, alias="Scheme"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    type: Optional[Literal["application", "gateway", "network"]] = Field(
        default=None, alias="Type"
    )
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="IpAddressType"
    )
    customer_owned_ipv4_pool: Optional[str] = Field(
        default=None, alias="CustomerOwnedIpv4Pool"
    )


class SetSubnetsInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")
    subnet_mappings: Optional[Sequence[SubnetMappingModel]] = Field(
        default=None, alias="SubnetMappings"
    )
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="IpAddressType"
    )


class CreateTargetGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="Protocol")
    protocol_version: Optional[str] = Field(default=None, alias="ProtocolVersion")
    port: Optional[int] = Field(default=None, alias="Port")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    health_check_protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="HealthCheckProtocol")
    health_check_port: Optional[str] = Field(default=None, alias="HealthCheckPort")
    health_check_enabled: Optional[bool] = Field(
        default=None, alias="HealthCheckEnabled"
    )
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    health_check_timeout_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckTimeoutSeconds"
    )
    healthy_threshold_count: Optional[int] = Field(
        default=None, alias="HealthyThresholdCount"
    )
    unhealthy_threshold_count: Optional[int] = Field(
        default=None, alias="UnhealthyThresholdCount"
    )
    matcher: Optional[MatcherModel] = Field(default=None, alias="Matcher")
    target_type: Optional[Literal["alb", "instance", "ip", "lambda"]] = Field(
        default=None, alias="TargetType"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    ip_address_type: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpAddressType"
    )


class ModifyTargetGroupInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    health_check_protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="HealthCheckProtocol")
    health_check_port: Optional[str] = Field(default=None, alias="HealthCheckPort")
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    health_check_enabled: Optional[bool] = Field(
        default=None, alias="HealthCheckEnabled"
    )
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    health_check_timeout_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckTimeoutSeconds"
    )
    healthy_threshold_count: Optional[int] = Field(
        default=None, alias="HealthyThresholdCount"
    )
    unhealthy_threshold_count: Optional[int] = Field(
        default=None, alias="UnhealthyThresholdCount"
    )
    matcher: Optional[MatcherModel] = Field(default=None, alias="Matcher")


class TargetGroupModel(BaseModel):
    target_group_arn: Optional[str] = Field(default=None, alias="TargetGroupArn")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="Protocol")
    port: Optional[int] = Field(default=None, alias="Port")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    health_check_protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="HealthCheckProtocol")
    health_check_port: Optional[str] = Field(default=None, alias="HealthCheckPort")
    health_check_enabled: Optional[bool] = Field(
        default=None, alias="HealthCheckEnabled"
    )
    health_check_interval_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckIntervalSeconds"
    )
    health_check_timeout_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckTimeoutSeconds"
    )
    healthy_threshold_count: Optional[int] = Field(
        default=None, alias="HealthyThresholdCount"
    )
    unhealthy_threshold_count: Optional[int] = Field(
        default=None, alias="UnhealthyThresholdCount"
    )
    health_check_path: Optional[str] = Field(default=None, alias="HealthCheckPath")
    matcher: Optional[MatcherModel] = Field(default=None, alias="Matcher")
    load_balancer_arns: Optional[List[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    target_type: Optional[Literal["alb", "instance", "ip", "lambda"]] = Field(
        default=None, alias="TargetType"
    )
    protocol_version: Optional[str] = Field(default=None, alias="ProtocolVersion")
    ip_address_type: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpAddressType"
    )


class DeregisterTargetsInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    targets: Sequence[TargetDescriptionModel] = Field(alias="Targets")


class DescribeTargetHealthInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    targets: Optional[Sequence[TargetDescriptionModel]] = Field(
        default=None, alias="Targets"
    )


class RegisterTargetsInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    targets: Sequence[TargetDescriptionModel] = Field(alias="Targets")


class DescribeAccountLimitsInputDescribeAccountLimitsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateModel(
    BaseModel
):
    listener_arn: str = Field(alias="ListenerArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeListenersInputDescribeListenersPaginateModel(BaseModel):
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    listener_arns: Optional[Sequence[str]] = Field(default=None, alias="ListenerArns")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLoadBalancersInputDescribeLoadBalancersPaginateModel(BaseModel):
    load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRulesInputDescribeRulesPaginateModel(BaseModel):
    listener_arn: Optional[str] = Field(default=None, alias="ListenerArn")
    rule_arns: Optional[Sequence[str]] = Field(default=None, alias="RuleArns")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    load_balancer_type: Optional[Literal["application", "gateway", "network"]] = Field(
        default=None, alias="LoadBalancerType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTargetGroupsInputDescribeTargetGroupsPaginateModel(BaseModel):
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    target_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TargetGroupArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAccountLimitsOutputModel(BaseModel):
    limits: List[LimitModel] = Field(alias="Limits")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancerAttributesOutputModel(BaseModel):
    attributes: List[LoadBalancerAttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyLoadBalancerAttributesInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")
    attributes: Sequence[LoadBalancerAttributeModel] = Field(alias="Attributes")


class ModifyLoadBalancerAttributesOutputModel(BaseModel):
    attributes: List[LoadBalancerAttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancersInputLoadBalancerAvailableWaitModel(BaseModel):
    load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeLoadBalancersInputLoadBalancerExistsWaitModel(BaseModel):
    load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeLoadBalancersInputLoadBalancersDeletedWaitModel(BaseModel):
    load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerArns"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTargetHealthInputTargetDeregisteredWaitModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    targets: Optional[Sequence[TargetDescriptionModel]] = Field(
        default=None, alias="Targets"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTargetHealthInputTargetInServiceWaitModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    targets: Optional[Sequence[TargetDescriptionModel]] = Field(
        default=None, alias="Targets"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTargetGroupAttributesOutputModel(BaseModel):
    attributes: List[TargetGroupAttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyTargetGroupAttributesInputRequestModel(BaseModel):
    target_group_arn: str = Field(alias="TargetGroupArn")
    attributes: Sequence[TargetGroupAttributeModel] = Field(alias="Attributes")


class ModifyTargetGroupAttributesOutputModel(BaseModel):
    attributes: List[TargetGroupAttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ForwardActionConfigModel(BaseModel):
    target_groups: Optional[Sequence[TargetGroupTupleModel]] = Field(
        default=None, alias="TargetGroups"
    )
    target_group_stickiness_config: Optional[TargetGroupStickinessConfigModel] = Field(
        default=None, alias="TargetGroupStickinessConfig"
    )


class QueryStringConditionConfigModel(BaseModel):
    values: Optional[Sequence[QueryStringKeyValuePairModel]] = Field(
        default=None, alias="Values"
    )


class SetRulePrioritiesInputRequestModel(BaseModel):
    rule_priorities: Sequence[RulePriorityPairModel] = Field(alias="RulePriorities")


class TargetHealthDescriptionModel(BaseModel):
    target: Optional[TargetDescriptionModel] = Field(default=None, alias="Target")
    health_check_port: Optional[str] = Field(default=None, alias="HealthCheckPort")
    target_health: Optional[TargetHealthModel] = Field(
        default=None, alias="TargetHealth"
    )


class DescribeTagsOutputModel(BaseModel):
    tag_descriptions: List[TagDescriptionModel] = Field(alias="TagDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoadBalancerModel(BaseModel):
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    canonical_hosted_zone_id: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneId"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    scheme: Optional[Literal["internal", "internet-facing"]] = Field(
        default=None, alias="Scheme"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    state: Optional[LoadBalancerStateModel] = Field(default=None, alias="State")
    type: Optional[Literal["application", "gateway", "network"]] = Field(
        default=None, alias="Type"
    )
    availability_zones: Optional[List[AvailabilityZoneModel]] = Field(
        default=None, alias="AvailabilityZones"
    )
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="IpAddressType"
    )
    customer_owned_ipv4_pool: Optional[str] = Field(
        default=None, alias="CustomerOwnedIpv4Pool"
    )


class SetSubnetsOutputModel(BaseModel):
    availability_zones: List[AvailabilityZoneModel] = Field(alias="AvailabilityZones")
    ip_address_type: Literal["dualstack", "ipv4"] = Field(alias="IpAddressType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSSLPoliciesOutputModel(BaseModel):
    ssl_policies: List[SslPolicyModel] = Field(alias="SslPolicies")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTargetGroupOutputModel(BaseModel):
    target_groups: List[TargetGroupModel] = Field(alias="TargetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTargetGroupsOutputModel(BaseModel):
    target_groups: List[TargetGroupModel] = Field(alias="TargetGroups")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyTargetGroupOutputModel(BaseModel):
    target_groups: List[TargetGroupModel] = Field(alias="TargetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionModel(BaseModel):
    type: Literal[
        "authenticate-cognito",
        "authenticate-oidc",
        "fixed-response",
        "forward",
        "redirect",
    ] = Field(alias="Type")
    target_group_arn: Optional[str] = Field(default=None, alias="TargetGroupArn")
    authenticate_oidc_config: Optional[AuthenticateOidcActionConfigModel] = Field(
        default=None, alias="AuthenticateOidcConfig"
    )
    authenticate_cognito_config: Optional[AuthenticateCognitoActionConfigModel] = Field(
        default=None, alias="AuthenticateCognitoConfig"
    )
    order: Optional[int] = Field(default=None, alias="Order")
    redirect_config: Optional[RedirectActionConfigModel] = Field(
        default=None, alias="RedirectConfig"
    )
    fixed_response_config: Optional[FixedResponseActionConfigModel] = Field(
        default=None, alias="FixedResponseConfig"
    )
    forward_config: Optional[ForwardActionConfigModel] = Field(
        default=None, alias="ForwardConfig"
    )


class RuleConditionModel(BaseModel):
    field: Optional[str] = Field(default=None, alias="Field")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    host_header_config: Optional[HostHeaderConditionConfigModel] = Field(
        default=None, alias="HostHeaderConfig"
    )
    path_pattern_config: Optional[PathPatternConditionConfigModel] = Field(
        default=None, alias="PathPatternConfig"
    )
    http_header_config: Optional[HttpHeaderConditionConfigModel] = Field(
        default=None, alias="HttpHeaderConfig"
    )
    query_string_config: Optional[QueryStringConditionConfigModel] = Field(
        default=None, alias="QueryStringConfig"
    )
    http_request_method_config: Optional[HttpRequestMethodConditionConfigModel] = Field(
        default=None, alias="HttpRequestMethodConfig"
    )
    source_ip_config: Optional[SourceIpConditionConfigModel] = Field(
        default=None, alias="SourceIpConfig"
    )


class DescribeTargetHealthOutputModel(BaseModel):
    target_health_descriptions: List[TargetHealthDescriptionModel] = Field(
        alias="TargetHealthDescriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoadBalancerOutputModel(BaseModel):
    load_balancers: List[LoadBalancerModel] = Field(alias="LoadBalancers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancersOutputModel(BaseModel):
    load_balancers: List[LoadBalancerModel] = Field(alias="LoadBalancers")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateListenerInputRequestModel(BaseModel):
    load_balancer_arn: str = Field(alias="LoadBalancerArn")
    default_actions: Sequence[ActionModel] = Field(alias="DefaultActions")
    protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="Protocol")
    port: Optional[int] = Field(default=None, alias="Port")
    ssl_policy: Optional[str] = Field(default=None, alias="SslPolicy")
    certificates: Optional[Sequence[CertificateModel]] = Field(
        default=None, alias="Certificates"
    )
    alpn_policy: Optional[Sequence[str]] = Field(default=None, alias="AlpnPolicy")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListenerModel(BaseModel):
    listener_arn: Optional[str] = Field(default=None, alias="ListenerArn")
    load_balancer_arn: Optional[str] = Field(default=None, alias="LoadBalancerArn")
    port: Optional[int] = Field(default=None, alias="Port")
    protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="Protocol")
    certificates: Optional[List[CertificateModel]] = Field(
        default=None, alias="Certificates"
    )
    ssl_policy: Optional[str] = Field(default=None, alias="SslPolicy")
    default_actions: Optional[List[ActionModel]] = Field(
        default=None, alias="DefaultActions"
    )
    alpn_policy: Optional[List[str]] = Field(default=None, alias="AlpnPolicy")


class ModifyListenerInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    port: Optional[int] = Field(default=None, alias="Port")
    protocol: Optional[
        Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
    ] = Field(default=None, alias="Protocol")
    ssl_policy: Optional[str] = Field(default=None, alias="SslPolicy")
    certificates: Optional[Sequence[CertificateModel]] = Field(
        default=None, alias="Certificates"
    )
    default_actions: Optional[Sequence[ActionModel]] = Field(
        default=None, alias="DefaultActions"
    )
    alpn_policy: Optional[Sequence[str]] = Field(default=None, alias="AlpnPolicy")


class CreateRuleInputRequestModel(BaseModel):
    listener_arn: str = Field(alias="ListenerArn")
    conditions: Sequence[RuleConditionModel] = Field(alias="Conditions")
    priority: int = Field(alias="Priority")
    actions: Sequence[ActionModel] = Field(alias="Actions")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ModifyRuleInputRequestModel(BaseModel):
    rule_arn: str = Field(alias="RuleArn")
    conditions: Optional[Sequence[RuleConditionModel]] = Field(
        default=None, alias="Conditions"
    )
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="Actions")


class RuleModel(BaseModel):
    rule_arn: Optional[str] = Field(default=None, alias="RuleArn")
    priority: Optional[str] = Field(default=None, alias="Priority")
    conditions: Optional[List[RuleConditionModel]] = Field(
        default=None, alias="Conditions"
    )
    actions: Optional[List[ActionModel]] = Field(default=None, alias="Actions")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")


class CreateListenerOutputModel(BaseModel):
    listeners: List[ListenerModel] = Field(alias="Listeners")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeListenersOutputModel(BaseModel):
    listeners: List[ListenerModel] = Field(alias="Listeners")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyListenerOutputModel(BaseModel):
    listeners: List[ListenerModel] = Field(alias="Listeners")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleOutputModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRulesOutputModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyRuleOutputModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetRulePrioritiesOutputModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
