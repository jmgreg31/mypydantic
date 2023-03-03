# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessLogModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    emit_interval: Optional[int] = Field(default=None, alias="EmitInterval")
    s3_bucket_prefix: Optional[str] = Field(default=None, alias="S3BucketPrefix")


class AddAvailabilityZonesInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    availability_zones: Sequence[str] = Field(alias="AvailabilityZones")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AdditionalAttributeModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AppCookieStickinessPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    cookie_name: Optional[str] = Field(default=None, alias="CookieName")


class ApplySecurityGroupsToLoadBalancerInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    security_groups: Sequence[str] = Field(alias="SecurityGroups")


class AttachLoadBalancerToSubnetsInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    subnets: Sequence[str] = Field(alias="Subnets")


class BackendServerDescriptionModel(BaseModel):
    instance_port: Optional[int] = Field(default=None, alias="InstancePort")
    policy_names: Optional[List[str]] = Field(default=None, alias="PolicyNames")


class HealthCheckModel(BaseModel):
    target: str = Field(alias="Target")
    interval: int = Field(alias="Interval")
    timeout: int = Field(alias="Timeout")
    unhealthy_threshold: int = Field(alias="UnhealthyThreshold")
    healthy_threshold: int = Field(alias="HealthyThreshold")


class ConnectionDrainingModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class ConnectionSettingsModel(BaseModel):
    idle_timeout: int = Field(alias="IdleTimeout")


class ListenerModel(BaseModel):
    protocol: str = Field(alias="Protocol")
    load_balancer_port: int = Field(alias="LoadBalancerPort")
    instance_port: int = Field(alias="InstancePort")
    instance_protocol: Optional[str] = Field(default=None, alias="InstanceProtocol")
    s_s_l_certificate_id: Optional[str] = Field(default=None, alias="SSLCertificateId")


class CreateAppCookieStickinessPolicyInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    policy_name: str = Field(alias="PolicyName")
    cookie_name: str = Field(alias="CookieName")


class CreateLBCookieStickinessPolicyInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    policy_name: str = Field(alias="PolicyName")
    cookie_expiration_period: Optional[int] = Field(
        default=None, alias="CookieExpirationPeriod"
    )


class PolicyAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class CrossZoneLoadBalancingModel(BaseModel):
    enabled: bool = Field(alias="Enabled")


class DeleteAccessPointInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")


class DeleteLoadBalancerListenerInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    load_balancer_ports: Sequence[int] = Field(alias="LoadBalancerPorts")


class DeleteLoadBalancerPolicyInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    policy_name: str = Field(alias="PolicyName")


class InstanceModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccessPointsInputRequestModel(BaseModel):
    load_balancer_names: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerNames"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class DescribeAccountLimitsInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class LimitModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    max: Optional[str] = Field(default=None, alias="Max")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class InstanceStateModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    state: Optional[str] = Field(default=None, alias="State")
    reason_code: Optional[str] = Field(default=None, alias="ReasonCode")
    description: Optional[str] = Field(default=None, alias="Description")


class DescribeLoadBalancerAttributesInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")


class DescribeLoadBalancerPoliciesInputRequestModel(BaseModel):
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")


class DescribeLoadBalancerPolicyTypesInputRequestModel(BaseModel):
    policy_type_names: Optional[Sequence[str]] = Field(
        default=None, alias="PolicyTypeNames"
    )


class DescribeTagsInputRequestModel(BaseModel):
    load_balancer_names: Sequence[str] = Field(alias="LoadBalancerNames")


class DetachLoadBalancerFromSubnetsInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    subnets: Sequence[str] = Field(alias="Subnets")


class LBCookieStickinessPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    cookie_expiration_period: Optional[int] = Field(
        default=None, alias="CookieExpirationPeriod"
    )


class SourceSecurityGroupModel(BaseModel):
    owner_alias: Optional[str] = Field(default=None, alias="OwnerAlias")
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class PolicyAttributeDescriptionModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class PolicyAttributeTypeDescriptionModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_type: Optional[str] = Field(default=None, alias="AttributeType")
    description: Optional[str] = Field(default=None, alias="Description")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    cardinality: Optional[str] = Field(default=None, alias="Cardinality")


class RemoveAvailabilityZonesInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    availability_zones: Sequence[str] = Field(alias="AvailabilityZones")


class TagKeyOnlyModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")


class SetLoadBalancerListenerSSLCertificateInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    load_balancer_port: int = Field(alias="LoadBalancerPort")
    s_s_l_certificate_id: str = Field(alias="SSLCertificateId")


class SetLoadBalancerPoliciesForBackendServerInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instance_port: int = Field(alias="InstancePort")
    policy_names: Sequence[str] = Field(alias="PolicyNames")


class SetLoadBalancerPoliciesOfListenerInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    load_balancer_port: int = Field(alias="LoadBalancerPort")
    policy_names: Sequence[str] = Field(alias="PolicyNames")


class AddAvailabilityZonesOutputModel(BaseModel):
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplySecurityGroupsToLoadBalancerOutputModel(BaseModel):
    security_groups: List[str] = Field(alias="SecurityGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachLoadBalancerToSubnetsOutputModel(BaseModel):
    subnets: List[str] = Field(alias="Subnets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPointOutputModel(BaseModel):
    dns_name: str = Field(alias="DNSName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachLoadBalancerFromSubnetsOutputModel(BaseModel):
    subnets: List[str] = Field(alias="Subnets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveAvailabilityZonesOutputModel(BaseModel):
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsInputRequestModel(BaseModel):
    load_balancer_names: Sequence[str] = Field(alias="LoadBalancerNames")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagDescriptionModel(BaseModel):
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ConfigureHealthCheckInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    health_check: HealthCheckModel = Field(alias="HealthCheck")


class ConfigureHealthCheckOutputModel(BaseModel):
    health_check: HealthCheckModel = Field(alias="HealthCheck")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPointInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    listeners: Sequence[ListenerModel] = Field(alias="Listeners")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    scheme: Optional[str] = Field(default=None, alias="Scheme")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateLoadBalancerListenerInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    listeners: Sequence[ListenerModel] = Field(alias="Listeners")


class ListenerDescriptionModel(BaseModel):
    listener: Optional[ListenerModel] = Field(default=None, alias="Listener")
    policy_names: Optional[List[str]] = Field(default=None, alias="PolicyNames")


class CreateLoadBalancerPolicyInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    policy_name: str = Field(alias="PolicyName")
    policy_type_name: str = Field(alias="PolicyTypeName")
    policy_attributes: Optional[Sequence[PolicyAttributeModel]] = Field(
        default=None, alias="PolicyAttributes"
    )


class LoadBalancerAttributesModel(BaseModel):
    cross_zone_load_balancing: Optional[CrossZoneLoadBalancingModel] = Field(
        default=None, alias="CrossZoneLoadBalancing"
    )
    access_log: Optional[AccessLogModel] = Field(default=None, alias="AccessLog")
    connection_draining: Optional[ConnectionDrainingModel] = Field(
        default=None, alias="ConnectionDraining"
    )
    connection_settings: Optional[ConnectionSettingsModel] = Field(
        default=None, alias="ConnectionSettings"
    )
    additional_attributes: Optional[List[AdditionalAttributeModel]] = Field(
        default=None, alias="AdditionalAttributes"
    )


class DeregisterEndPointsInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Sequence[InstanceModel] = Field(alias="Instances")


class DeregisterEndPointsOutputModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndPointStateInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Optional[Sequence[InstanceModel]] = Field(
        default=None, alias="Instances"
    )


class RegisterEndPointsInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Sequence[InstanceModel] = Field(alias="Instances")


class RegisterEndPointsOutputModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccessPointsInputDescribeLoadBalancersPaginateModel(BaseModel):
    load_balancer_names: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAccountLimitsInputDescribeAccountLimitsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAccountLimitsOutputModel(BaseModel):
    limits: List[LimitModel] = Field(alias="Limits")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndPointStateInputAnyInstanceInServiceWaitModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Optional[Sequence[InstanceModel]] = Field(
        default=None, alias="Instances"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndPointStateInputInstanceDeregisteredWaitModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Optional[Sequence[InstanceModel]] = Field(
        default=None, alias="Instances"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndPointStateInputInstanceInServiceWaitModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    instances: Optional[Sequence[InstanceModel]] = Field(
        default=None, alias="Instances"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndPointStateOutputModel(BaseModel):
    instance_states: List[InstanceStateModel] = Field(alias="InstanceStates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PoliciesModel(BaseModel):
    app_cookie_stickiness_policies: Optional[
        List[AppCookieStickinessPolicyModel]
    ] = Field(default=None, alias="AppCookieStickinessPolicies")
    l_bcookie_stickiness_policies: Optional[
        List[LBCookieStickinessPolicyModel]
    ] = Field(default=None, alias="LBCookieStickinessPolicies")
    other_policies: Optional[List[str]] = Field(default=None, alias="OtherPolicies")


class PolicyDescriptionModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_type_name: Optional[str] = Field(default=None, alias="PolicyTypeName")
    policy_attribute_descriptions: Optional[
        List[PolicyAttributeDescriptionModel]
    ] = Field(default=None, alias="PolicyAttributeDescriptions")


class PolicyTypeDescriptionModel(BaseModel):
    policy_type_name: Optional[str] = Field(default=None, alias="PolicyTypeName")
    description: Optional[str] = Field(default=None, alias="Description")
    policy_attribute_type_descriptions: Optional[
        List[PolicyAttributeTypeDescriptionModel]
    ] = Field(default=None, alias="PolicyAttributeTypeDescriptions")


class RemoveTagsInputRequestModel(BaseModel):
    load_balancer_names: Sequence[str] = Field(alias="LoadBalancerNames")
    tags: Sequence[TagKeyOnlyModel] = Field(alias="Tags")


class DescribeTagsOutputModel(BaseModel):
    tag_descriptions: List[TagDescriptionModel] = Field(alias="TagDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancerAttributesOutputModel(BaseModel):
    load_balancer_attributes: LoadBalancerAttributesModel = Field(
        alias="LoadBalancerAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyLoadBalancerAttributesInputRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    load_balancer_attributes: LoadBalancerAttributesModel = Field(
        alias="LoadBalancerAttributes"
    )


class ModifyLoadBalancerAttributesOutputModel(BaseModel):
    load_balancer_name: str = Field(alias="LoadBalancerName")
    load_balancer_attributes: LoadBalancerAttributesModel = Field(
        alias="LoadBalancerAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoadBalancerDescriptionModel(BaseModel):
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    canonical_hosted_zone_name: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneName"
    )
    canonical_hosted_zone_name_id: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneNameID"
    )
    listener_descriptions: Optional[List[ListenerDescriptionModel]] = Field(
        default=None, alias="ListenerDescriptions"
    )
    policies: Optional[PoliciesModel] = Field(default=None, alias="Policies")
    backend_server_descriptions: Optional[List[BackendServerDescriptionModel]] = Field(
        default=None, alias="BackendServerDescriptions"
    )
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    subnets: Optional[List[str]] = Field(default=None, alias="Subnets")
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")
    instances: Optional[List[InstanceModel]] = Field(default=None, alias="Instances")
    health_check: Optional[HealthCheckModel] = Field(default=None, alias="HealthCheck")
    source_security_group: Optional[SourceSecurityGroupModel] = Field(
        default=None, alias="SourceSecurityGroup"
    )
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    scheme: Optional[str] = Field(default=None, alias="Scheme")


class DescribeLoadBalancerPoliciesOutputModel(BaseModel):
    policy_descriptions: List[PolicyDescriptionModel] = Field(
        alias="PolicyDescriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancerPolicyTypesOutputModel(BaseModel):
    policy_type_descriptions: List[PolicyTypeDescriptionModel] = Field(
        alias="PolicyTypeDescriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccessPointsOutputModel(BaseModel):
    load_balancer_descriptions: List[LoadBalancerDescriptionModel] = Field(
        alias="LoadBalancerDescriptions"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
