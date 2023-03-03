# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionTargetModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    description: Optional[str] = Field(default=None, alias="Description")


class AppModel(BaseModel):
    app_name: str = Field(alias="AppName")
    protocol: str = Field(alias="Protocol")
    port: int = Field(alias="Port")


class AssociateAdminAccountRequestModel(BaseModel):
    admin_account: str = Field(alias="AdminAccount")


class AssociateThirdPartyFirewallRequestModel(BaseModel):
    third_party_firewall: Literal[
        "FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    ] = Field(alias="ThirdPartyFirewall")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AwsEc2NetworkInterfaceViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    violating_security_groups: Optional[List[str]] = Field(
        default=None, alias="ViolatingSecurityGroups"
    )


class PartialMatchModel(BaseModel):
    reference: Optional[str] = Field(default=None, alias="Reference")
    target_violation_reasons: Optional[List[str]] = Field(
        default=None, alias="TargetViolationReasons"
    )


class BatchAssociateResourceRequestModel(BaseModel):
    resource_set_identifier: str = Field(alias="ResourceSetIdentifier")
    items: Sequence[str] = Field(alias="Items")


class FailedItemModel(BaseModel):
    uri: Optional[str] = Field(default=None, alias="URI")
    reason: Optional[
        Literal[
            "NOT_VALID_ACCOUNT_ID",
            "NOT_VALID_ARN",
            "NOT_VALID_PARTITION",
            "NOT_VALID_REGION",
            "NOT_VALID_RESOURCE_TYPE",
            "NOT_VALID_SERVICE",
        ]
    ] = Field(default=None, alias="Reason")


class BatchDisassociateResourceRequestModel(BaseModel):
    resource_set_identifier: str = Field(alias="ResourceSetIdentifier")
    items: Sequence[str] = Field(alias="Items")


class ComplianceViolatorModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    violation_reason: Optional[
        Literal[
            "BLACK_HOLE_ROUTE_DETECTED",
            "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET",
            "FIREWALL_SUBNET_IS_OUT_OF_SCOPE",
            "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE",
            "FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT",
            "FMS_CREATED_SECURITY_GROUP_EDITED",
            "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE",
            "INTERNET_TRAFFIC_NOT_INSPECTED",
            "INVALID_ROUTE_CONFIGURATION",
            "MISSING_EXPECTED_ROUTE_TABLE",
            "MISSING_FIREWALL",
            "MISSING_FIREWALL_SUBNET_IN_AZ",
            "MISSING_TARGET_GATEWAY",
            "NETWORK_FIREWALL_POLICY_MODIFIED",
            "RESOURCE_INCORRECT_WEB_ACL",
            "RESOURCE_MISSING_DNS_FIREWALL",
            "RESOURCE_MISSING_SECURITY_GROUP",
            "RESOURCE_MISSING_SHIELD_PROTECTION",
            "RESOURCE_MISSING_WEB_ACL",
            "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
            "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
            "ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT",
            "SECURITY_GROUP_REDUNDANT",
            "SECURITY_GROUP_UNUSED",
            "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY",
            "UNEXPECTED_FIREWALL_ROUTES",
            "UNEXPECTED_TARGET_GATEWAY_ROUTES",
            "WEB_ACL_MISSING_RULE_GROUP",
        ]
    ] = Field(default=None, alias="ViolationReason")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    metadata: Optional[Dict[str, str]] = Field(default=None, alias="Metadata")


class DeleteAppsListRequestModel(BaseModel):
    list_id: str = Field(alias="ListId")


class DeletePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    delete_all_policy_resources: Optional[bool] = Field(
        default=None, alias="DeleteAllPolicyResources"
    )


class DeleteProtocolsListRequestModel(BaseModel):
    list_id: str = Field(alias="ListId")


class DeleteResourceSetRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class DisassociateThirdPartyFirewallRequestModel(BaseModel):
    third_party_firewall: Literal[
        "FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    ] = Field(alias="ThirdPartyFirewall")


class DiscoveredResourceModel(BaseModel):
    uri: Optional[str] = Field(default=None, alias="URI")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    type: Optional[str] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")


class DnsDuplicateRuleGroupViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    violation_target_description: Optional[str] = Field(
        default=None, alias="ViolationTargetDescription"
    )


class DnsRuleGroupLimitExceededViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    violation_target_description: Optional[str] = Field(
        default=None, alias="ViolationTargetDescription"
    )
    number_of_rule_groups_already_associated: Optional[int] = Field(
        default=None, alias="NumberOfRuleGroupsAlreadyAssociated"
    )


class DnsRuleGroupPriorityConflictViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    violation_target_description: Optional[str] = Field(
        default=None, alias="ViolationTargetDescription"
    )
    conflicting_priority: Optional[int] = Field(
        default=None, alias="ConflictingPriority"
    )
    conflicting_policy_id: Optional[str] = Field(
        default=None, alias="ConflictingPolicyId"
    )
    unavailable_priorities: Optional[List[int]] = Field(
        default=None, alias="UnavailablePriorities"
    )


class EvaluationResultModel(BaseModel):
    compliance_status: Optional[Literal["COMPLIANT", "NON_COMPLIANT"]] = Field(
        default=None, alias="ComplianceStatus"
    )
    violator_count: Optional[int] = Field(default=None, alias="ViolatorCount")
    evaluation_limit_exceeded: Optional[bool] = Field(
        default=None, alias="EvaluationLimitExceeded"
    )


class ExpectedRouteModel(BaseModel):
    ip_v4_cidr: Optional[str] = Field(default=None, alias="IpV4Cidr")
    prefix_list_id: Optional[str] = Field(default=None, alias="PrefixListId")
    ip_v6_cidr: Optional[str] = Field(default=None, alias="IpV6Cidr")
    contributing_subnets: Optional[List[str]] = Field(
        default=None, alias="ContributingSubnets"
    )
    allowed_targets: Optional[List[str]] = Field(default=None, alias="AllowedTargets")
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")


class FMSPolicyUpdateFirewallCreationConfigActionModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    firewall_creation_config: Optional[str] = Field(
        default=None, alias="FirewallCreationConfig"
    )


class FirewallSubnetIsOutOfScopeViolationModel(BaseModel):
    firewall_subnet_id: Optional[str] = Field(default=None, alias="FirewallSubnetId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_availability_zone: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_availability_zone_id: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZoneId"
    )
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")


class FirewallSubnetMissingVPCEndpointViolationModel(BaseModel):
    firewall_subnet_id: Optional[str] = Field(default=None, alias="FirewallSubnetId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_availability_zone: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_availability_zone_id: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZoneId"
    )


class GetAppsListRequestModel(BaseModel):
    list_id: str = Field(alias="ListId")
    default_list: Optional[bool] = Field(default=None, alias="DefaultList")


class GetComplianceDetailRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    member_account: str = Field(alias="MemberAccount")


class GetPolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")


class GetProtectionStatusRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    member_account_id: Optional[str] = Field(default=None, alias="MemberAccountId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetProtocolsListRequestModel(BaseModel):
    list_id: str = Field(alias="ListId")
    default_list: Optional[bool] = Field(default=None, alias="DefaultList")


class ProtocolsListDataModel(BaseModel):
    list_name: str = Field(alias="ListName")
    protocols_list: List[str] = Field(alias="ProtocolsList")
    list_id: Optional[str] = Field(default=None, alias="ListId")
    list_update_token: Optional[str] = Field(default=None, alias="ListUpdateToken")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    previous_protocols_list: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="PreviousProtocolsList"
    )


class GetResourceSetRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class ResourceSetModel(BaseModel):
    name: str = Field(alias="Name")
    resource_type_list: List[str] = Field(alias="ResourceTypeList")
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class GetThirdPartyFirewallAssociationStatusRequestModel(BaseModel):
    third_party_firewall: Literal[
        "FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    ] = Field(alias="ThirdPartyFirewall")


class GetViolationDetailsRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    member_account: str = Field(alias="MemberAccount")
    resource_id: str = Field(alias="ResourceId")
    resource_type: str = Field(alias="ResourceType")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAppsListsRequestModel(BaseModel):
    max_results: int = Field(alias="MaxResults")
    default_lists: Optional[bool] = Field(default=None, alias="DefaultLists")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListComplianceStatusRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDiscoveredResourcesRequestModel(BaseModel):
    member_account_ids: Sequence[str] = Field(alias="MemberAccountIds")
    resource_type: str = Field(alias="ResourceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMemberAccountsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPoliciesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PolicySummaryModel(BaseModel):
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    security_service_type: Optional[
        Literal[
            "DNS_FIREWALL",
            "IMPORT_NETWORK_FIREWALL",
            "NETWORK_FIREWALL",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
            "SHIELD_ADVANCED",
            "THIRD_PARTY_FIREWALL",
            "WAF",
            "WAFV2",
        ]
    ] = Field(default=None, alias="SecurityServiceType")
    remediation_enabled: Optional[bool] = Field(
        default=None, alias="RemediationEnabled"
    )
    delete_unused_fmmanaged_resources: Optional[bool] = Field(
        default=None, alias="DeleteUnusedFMManagedResources"
    )


class ListProtocolsListsRequestModel(BaseModel):
    max_results: int = Field(alias="MaxResults")
    default_lists: Optional[bool] = Field(default=None, alias="DefaultLists")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProtocolsListDataSummaryModel(BaseModel):
    list_arn: Optional[str] = Field(default=None, alias="ListArn")
    list_id: Optional[str] = Field(default=None, alias="ListId")
    list_name: Optional[str] = Field(default=None, alias="ListName")
    protocols_list: Optional[List[str]] = Field(default=None, alias="ProtocolsList")


class ListResourceSetResourcesRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResourceModel(BaseModel):
    uri: str = Field(alias="URI")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class ListResourceSetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResourceSetSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ListThirdPartyFirewallFirewallPoliciesRequestModel(BaseModel):
    third_party_firewall: Literal[
        "FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    ] = Field(alias="ThirdPartyFirewall")
    max_results: int = Field(alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ThirdPartyFirewallFirewallPolicyModel(BaseModel):
    firewall_policy_id: Optional[str] = Field(default=None, alias="FirewallPolicyId")
    firewall_policy_name: Optional[str] = Field(
        default=None, alias="FirewallPolicyName"
    )


class RouteModel(BaseModel):
    destination_type: Optional[Literal["IPV4", "IPV6", "PREFIX_LIST"]] = Field(
        default=None, alias="DestinationType"
    )
    target_type: Optional[
        Literal[
            "CARRIER_GATEWAY",
            "EGRESS_ONLY_INTERNET_GATEWAY",
            "GATEWAY",
            "INSTANCE",
            "LOCAL_GATEWAY",
            "NAT_GATEWAY",
            "NETWORK_INTERFACE",
            "TRANSIT_GATEWAY",
            "VPC_ENDPOINT",
            "VPC_PEERING_CONNECTION",
        ]
    ] = Field(default=None, alias="TargetType")
    destination: Optional[str] = Field(default=None, alias="Destination")
    target: Optional[str] = Field(default=None, alias="Target")


class NetworkFirewallMissingExpectedRTViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    current_route_table: Optional[str] = Field(default=None, alias="CurrentRouteTable")
    expected_route_table: Optional[str] = Field(
        default=None, alias="ExpectedRouteTable"
    )


class NetworkFirewallMissingFirewallViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    target_violation_reason: Optional[str] = Field(
        default=None, alias="TargetViolationReason"
    )


class NetworkFirewallMissingSubnetViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    target_violation_reason: Optional[str] = Field(
        default=None, alias="TargetViolationReason"
    )


class StatefulEngineOptionsModel(BaseModel):
    rule_order: Optional[Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]] = Field(
        default=None, alias="RuleOrder"
    )


class StatelessRuleGroupModel(BaseModel):
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    priority: Optional[int] = Field(default=None, alias="Priority")


class NetworkFirewallPolicyModel(BaseModel):
    firewall_deployment_model: Optional[Literal["CENTRALIZED", "DISTRIBUTED"]] = Field(
        default=None, alias="FirewallDeploymentModel"
    )


class NetworkFirewallStatefulRuleGroupOverrideModel(BaseModel):
    action: Optional[Literal["DROP_TO_ALERT"]] = Field(default=None, alias="Action")


class ThirdPartyFirewallPolicyModel(BaseModel):
    firewall_deployment_model: Optional[Literal["CENTRALIZED", "DISTRIBUTED"]] = Field(
        default=None, alias="FirewallDeploymentModel"
    )


class ResourceTagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class PutNotificationChannelRequestModel(BaseModel):
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    sns_role_name: str = Field(alias="SnsRoleName")


class ThirdPartyFirewallMissingExpectedRouteTableViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    current_route_table: Optional[str] = Field(default=None, alias="CurrentRouteTable")
    expected_route_table: Optional[str] = Field(
        default=None, alias="ExpectedRouteTable"
    )


class ThirdPartyFirewallMissingFirewallViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    target_violation_reason: Optional[str] = Field(
        default=None, alias="TargetViolationReason"
    )


class ThirdPartyFirewallMissingSubnetViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    vp_c: Optional[str] = Field(default=None, alias="VPC")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    target_violation_reason: Optional[str] = Field(
        default=None, alias="TargetViolationReason"
    )


class SecurityGroupRuleDescriptionModel(BaseModel):
    ip_v4_range: Optional[str] = Field(default=None, alias="IPV4Range")
    ip_v6_range: Optional[str] = Field(default=None, alias="IPV6Range")
    prefix_list_id: Optional[str] = Field(default=None, alias="PrefixListId")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class EC2AssociateRouteTableActionModel(BaseModel):
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")
    subnet_id: Optional[ActionTargetModel] = Field(default=None, alias="SubnetId")
    gateway_id: Optional[ActionTargetModel] = Field(default=None, alias="GatewayId")


class EC2CopyRouteTableActionModel(BaseModel):
    vpc_id: ActionTargetModel = Field(alias="VpcId")
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")


class EC2CreateRouteActionModel(BaseModel):
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )
    destination_prefix_list_id: Optional[str] = Field(
        default=None, alias="DestinationPrefixListId"
    )
    destination_ipv6_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationIpv6CidrBlock"
    )
    vpc_endpoint_id: Optional[ActionTargetModel] = Field(
        default=None, alias="VpcEndpointId"
    )
    gateway_id: Optional[ActionTargetModel] = Field(default=None, alias="GatewayId")


class EC2CreateRouteTableActionModel(BaseModel):
    vpc_id: ActionTargetModel = Field(alias="VpcId")
    description: Optional[str] = Field(default=None, alias="Description")


class EC2DeleteRouteActionModel(BaseModel):
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )
    destination_prefix_list_id: Optional[str] = Field(
        default=None, alias="DestinationPrefixListId"
    )
    destination_ipv6_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationIpv6CidrBlock"
    )


class EC2ReplaceRouteActionModel(BaseModel):
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )
    destination_prefix_list_id: Optional[str] = Field(
        default=None, alias="DestinationPrefixListId"
    )
    destination_ipv6_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationIpv6CidrBlock"
    )
    gateway_id: Optional[ActionTargetModel] = Field(default=None, alias="GatewayId")


class EC2ReplaceRouteTableAssociationActionModel(BaseModel):
    association_id: ActionTargetModel = Field(alias="AssociationId")
    route_table_id: ActionTargetModel = Field(alias="RouteTableId")
    description: Optional[str] = Field(default=None, alias="Description")


class AppsListDataSummaryModel(BaseModel):
    list_arn: Optional[str] = Field(default=None, alias="ListArn")
    list_id: Optional[str] = Field(default=None, alias="ListId")
    list_name: Optional[str] = Field(default=None, alias="ListName")
    apps_list: Optional[List[AppModel]] = Field(default=None, alias="AppsList")


class AppsListDataModel(BaseModel):
    list_name: str = Field(alias="ListName")
    apps_list: List[AppModel] = Field(alias="AppsList")
    list_id: Optional[str] = Field(default=None, alias="ListId")
    list_update_token: Optional[str] = Field(default=None, alias="ListUpdateToken")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    previous_apps_list: Optional[Dict[str, List[AppModel]]] = Field(
        default=None, alias="PreviousAppsList"
    )


class AssociateThirdPartyFirewallResponseModel(BaseModel):
    third_party_firewall_status: Literal[
        "NOT_EXIST",
        "OFFBOARDING",
        "OFFBOARD_COMPLETE",
        "ONBOARDING",
        "ONBOARD_COMPLETE",
    ] = Field(alias="ThirdPartyFirewallStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateThirdPartyFirewallResponseModel(BaseModel):
    third_party_firewall_status: Literal[
        "NOT_EXIST",
        "OFFBOARDING",
        "OFFBOARD_COMPLETE",
        "ONBOARDING",
        "ONBOARD_COMPLETE",
    ] = Field(alias="ThirdPartyFirewallStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAdminAccountResponseModel(BaseModel):
    admin_account: str = Field(alias="AdminAccount")
    role_status: Literal[
        "CREATING", "DELETED", "DELETING", "PENDING_DELETION", "READY"
    ] = Field(alias="RoleStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNotificationChannelResponseModel(BaseModel):
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    sns_role_name: str = Field(alias="SnsRoleName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProtectionStatusResponseModel(BaseModel):
    admin_account_id: str = Field(alias="AdminAccountId")
    service_type: Literal[
        "DNS_FIREWALL",
        "IMPORT_NETWORK_FIREWALL",
        "NETWORK_FIREWALL",
        "SECURITY_GROUPS_COMMON",
        "SECURITY_GROUPS_CONTENT_AUDIT",
        "SECURITY_GROUPS_USAGE_AUDIT",
        "SHIELD_ADVANCED",
        "THIRD_PARTY_FIREWALL",
        "WAF",
        "WAFV2",
    ] = Field(alias="ServiceType")
    data: str = Field(alias="Data")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetThirdPartyFirewallAssociationStatusResponseModel(BaseModel):
    third_party_firewall_status: Literal[
        "NOT_EXIST",
        "OFFBOARDING",
        "OFFBOARD_COMPLETE",
        "ONBOARDING",
        "ONBOARD_COMPLETE",
    ] = Field(alias="ThirdPartyFirewallStatus")
    marketplace_onboarding_status: Literal[
        "COMPLETE", "NOT_COMPLETE", "NO_SUBSCRIPTION"
    ] = Field(alias="MarketplaceOnboardingStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMemberAccountsResponseModel(BaseModel):
    member_accounts: List[str] = Field(alias="MemberAccounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AwsEc2InstanceViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    aws_ec2_network_interface_violations: Optional[
        List[AwsEc2NetworkInterfaceViolationModel]
    ] = Field(default=None, alias="AwsEc2NetworkInterfaceViolations")


class BatchAssociateResourceResponseModel(BaseModel):
    resource_set_identifier: str = Field(alias="ResourceSetIdentifier")
    failed_items: List[FailedItemModel] = Field(alias="FailedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateResourceResponseModel(BaseModel):
    resource_set_identifier: str = Field(alias="ResourceSetIdentifier")
    failed_items: List[FailedItemModel] = Field(alias="FailedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyComplianceDetailModel(BaseModel):
    policy_owner: Optional[str] = Field(default=None, alias="PolicyOwner")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    member_account: Optional[str] = Field(default=None, alias="MemberAccount")
    violators: Optional[List[ComplianceViolatorModel]] = Field(
        default=None, alias="Violators"
    )
    evaluation_limit_exceeded: Optional[bool] = Field(
        default=None, alias="EvaluationLimitExceeded"
    )
    expired_at: Optional[datetime] = Field(default=None, alias="ExpiredAt")
    issue_info_map: Optional[
        Dict[Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"], str]
    ] = Field(default=None, alias="IssueInfoMap")


class ListDiscoveredResourcesResponseModel(BaseModel):
    items: List[DiscoveredResourceModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyComplianceStatusModel(BaseModel):
    policy_owner: Optional[str] = Field(default=None, alias="PolicyOwner")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    member_account: Optional[str] = Field(default=None, alias="MemberAccount")
    evaluation_results: Optional[List[EvaluationResultModel]] = Field(
        default=None, alias="EvaluationResults"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    issue_info_map: Optional[
        Dict[Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"], str]
    ] = Field(default=None, alias="IssueInfoMap")


class NetworkFirewallMissingExpectedRoutesViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    expected_routes: Optional[List[ExpectedRouteModel]] = Field(
        default=None, alias="ExpectedRoutes"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class GetProtocolsListResponseModel(BaseModel):
    protocols_list: ProtocolsListDataModel = Field(alias="ProtocolsList")
    protocols_list_arn: str = Field(alias="ProtocolsListArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProtocolsListResponseModel(BaseModel):
    protocols_list: ProtocolsListDataModel = Field(alias="ProtocolsList")
    protocols_list_arn: str = Field(alias="ProtocolsListArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceSetResponseModel(BaseModel):
    resource_set: ResourceSetModel = Field(alias="ResourceSet")
    resource_set_arn: str = Field(alias="ResourceSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourceSetResponseModel(BaseModel):
    resource_set: ResourceSetModel = Field(alias="ResourceSet")
    resource_set_arn: str = Field(alias="ResourceSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppsListsRequestListAppsListsPaginateModel(BaseModel):
    default_lists: Optional[bool] = Field(default=None, alias="DefaultLists")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComplianceStatusRequestListComplianceStatusPaginateModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMemberAccountsRequestListMemberAccountsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesRequestListPoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProtocolsListsRequestListProtocolsListsPaginateModel(BaseModel):
    default_lists: Optional[bool] = Field(default=None, alias="DefaultLists")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateModel(
    BaseModel
):
    third_party_firewall: Literal[
        "FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"
    ] = Field(alias="ThirdPartyFirewall")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesResponseModel(BaseModel):
    policy_list: List[PolicySummaryModel] = Field(alias="PolicyList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProtocolsListsResponseModel(BaseModel):
    protocols_lists: List[ProtocolsListDataSummaryModel] = Field(alias="ProtocolsLists")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceSetResourcesResponseModel(BaseModel):
    items: List[ResourceModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceSetsResponseModel(BaseModel):
    resource_sets: List[ResourceSetSummaryModel] = Field(alias="ResourceSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProtocolsListRequestModel(BaseModel):
    protocols_list: ProtocolsListDataModel = Field(alias="ProtocolsList")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class PutResourceSetRequestModel(BaseModel):
    resource_set: ResourceSetModel = Field(alias="ResourceSet")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_list: Sequence[TagModel] = Field(alias="TagList")


class ListThirdPartyFirewallFirewallPoliciesResponseModel(BaseModel):
    third_party_firewall_firewall_policies: List[
        ThirdPartyFirewallFirewallPolicyModel
    ] = Field(alias="ThirdPartyFirewallFirewallPolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkFirewallBlackHoleRouteDetectedViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    violating_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ViolatingRoutes"
    )


class NetworkFirewallInternetTrafficNotInspectedViolationModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    subnet_availability_zone: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    violating_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ViolatingRoutes"
    )
    is_route_table_used_in_different_az: Optional[bool] = Field(
        default=None, alias="IsRouteTableUsedInDifferentAZ"
    )
    current_firewall_subnet_route_table: Optional[str] = Field(
        default=None, alias="CurrentFirewallSubnetRouteTable"
    )
    expected_firewall_endpoint: Optional[str] = Field(
        default=None, alias="ExpectedFirewallEndpoint"
    )
    firewall_subnet_id: Optional[str] = Field(default=None, alias="FirewallSubnetId")
    expected_firewall_subnet_routes: Optional[List[ExpectedRouteModel]] = Field(
        default=None, alias="ExpectedFirewallSubnetRoutes"
    )
    actual_firewall_subnet_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ActualFirewallSubnetRoutes"
    )
    internet_gateway_id: Optional[str] = Field(default=None, alias="InternetGatewayId")
    current_internet_gateway_route_table: Optional[str] = Field(
        default=None, alias="CurrentInternetGatewayRouteTable"
    )
    expected_internet_gateway_routes: Optional[List[ExpectedRouteModel]] = Field(
        default=None, alias="ExpectedInternetGatewayRoutes"
    )
    actual_internet_gateway_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ActualInternetGatewayRoutes"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class NetworkFirewallInvalidRouteConfigurationViolationModel(BaseModel):
    affected_subnets: Optional[List[str]] = Field(default=None, alias="AffectedSubnets")
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    is_route_table_used_in_different_az: Optional[bool] = Field(
        default=None, alias="IsRouteTableUsedInDifferentAZ"
    )
    violating_route: Optional[RouteModel] = Field(default=None, alias="ViolatingRoute")
    current_firewall_subnet_route_table: Optional[str] = Field(
        default=None, alias="CurrentFirewallSubnetRouteTable"
    )
    expected_firewall_endpoint: Optional[str] = Field(
        default=None, alias="ExpectedFirewallEndpoint"
    )
    actual_firewall_endpoint: Optional[str] = Field(
        default=None, alias="ActualFirewallEndpoint"
    )
    expected_firewall_subnet_id: Optional[str] = Field(
        default=None, alias="ExpectedFirewallSubnetId"
    )
    actual_firewall_subnet_id: Optional[str] = Field(
        default=None, alias="ActualFirewallSubnetId"
    )
    expected_firewall_subnet_routes: Optional[List[ExpectedRouteModel]] = Field(
        default=None, alias="ExpectedFirewallSubnetRoutes"
    )
    actual_firewall_subnet_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ActualFirewallSubnetRoutes"
    )
    internet_gateway_id: Optional[str] = Field(default=None, alias="InternetGatewayId")
    current_internet_gateway_route_table: Optional[str] = Field(
        default=None, alias="CurrentInternetGatewayRouteTable"
    )
    expected_internet_gateway_routes: Optional[List[ExpectedRouteModel]] = Field(
        default=None, alias="ExpectedInternetGatewayRoutes"
    )
    actual_internet_gateway_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ActualInternetGatewayRoutes"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class NetworkFirewallUnexpectedFirewallRoutesViolationModel(BaseModel):
    firewall_subnet_id: Optional[str] = Field(default=None, alias="FirewallSubnetId")
    violating_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ViolatingRoutes"
    )
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    firewall_endpoint: Optional[str] = Field(default=None, alias="FirewallEndpoint")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class NetworkFirewallUnexpectedGatewayRoutesViolationModel(BaseModel):
    gateway_id: Optional[str] = Field(default=None, alias="GatewayId")
    violating_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ViolatingRoutes"
    )
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class RouteHasOutOfScopeEndpointViolationModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    route_table_id: Optional[str] = Field(default=None, alias="RouteTableId")
    violating_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="ViolatingRoutes"
    )
    subnet_availability_zone: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_availability_zone_id: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZoneId"
    )
    current_firewall_subnet_route_table: Optional[str] = Field(
        default=None, alias="CurrentFirewallSubnetRouteTable"
    )
    firewall_subnet_id: Optional[str] = Field(default=None, alias="FirewallSubnetId")
    firewall_subnet_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="FirewallSubnetRoutes"
    )
    internet_gateway_id: Optional[str] = Field(default=None, alias="InternetGatewayId")
    current_internet_gateway_route_table: Optional[str] = Field(
        default=None, alias="CurrentInternetGatewayRouteTable"
    )
    internet_gateway_routes: Optional[List[RouteModel]] = Field(
        default=None, alias="InternetGatewayRoutes"
    )


class StatefulRuleGroupModel(BaseModel):
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    override: Optional[NetworkFirewallStatefulRuleGroupOverrideModel] = Field(
        default=None, alias="Override"
    )


class PolicyOptionModel(BaseModel):
    network_firewall_policy: Optional[NetworkFirewallPolicyModel] = Field(
        default=None, alias="NetworkFirewallPolicy"
    )
    third_party_firewall_policy: Optional[ThirdPartyFirewallPolicyModel] = Field(
        default=None, alias="ThirdPartyFirewallPolicy"
    )


class SecurityGroupRemediationActionModel(BaseModel):
    remediation_action_type: Optional[Literal["MODIFY", "REMOVE"]] = Field(
        default=None, alias="RemediationActionType"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    remediation_result: Optional[SecurityGroupRuleDescriptionModel] = Field(
        default=None, alias="RemediationResult"
    )
    is_default_action: Optional[bool] = Field(default=None, alias="IsDefaultAction")


class RemediationActionModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    ec2_create_route_action: Optional[EC2CreateRouteActionModel] = Field(
        default=None, alias="EC2CreateRouteAction"
    )
    ec2_replace_route_action: Optional[EC2ReplaceRouteActionModel] = Field(
        default=None, alias="EC2ReplaceRouteAction"
    )
    ec2_delete_route_action: Optional[EC2DeleteRouteActionModel] = Field(
        default=None, alias="EC2DeleteRouteAction"
    )
    ec2_copy_route_table_action: Optional[EC2CopyRouteTableActionModel] = Field(
        default=None, alias="EC2CopyRouteTableAction"
    )
    ec2_replace_route_table_association_action: Optional[
        EC2ReplaceRouteTableAssociationActionModel
    ] = Field(default=None, alias="EC2ReplaceRouteTableAssociationAction")
    ec2_associate_route_table_action: Optional[
        EC2AssociateRouteTableActionModel
    ] = Field(default=None, alias="EC2AssociateRouteTableAction")
    ec2_create_route_table_action: Optional[EC2CreateRouteTableActionModel] = Field(
        default=None, alias="EC2CreateRouteTableAction"
    )
    fms_policy_update_firewall_creation_config_action: Optional[
        FMSPolicyUpdateFirewallCreationConfigActionModel
    ] = Field(default=None, alias="FMSPolicyUpdateFirewallCreationConfigAction")


class ListAppsListsResponseModel(BaseModel):
    apps_lists: List[AppsListDataSummaryModel] = Field(alias="AppsLists")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppsListResponseModel(BaseModel):
    apps_list: AppsListDataModel = Field(alias="AppsList")
    apps_list_arn: str = Field(alias="AppsListArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppsListRequestModel(BaseModel):
    apps_list: AppsListDataModel = Field(alias="AppsList")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class PutAppsListResponseModel(BaseModel):
    apps_list: AppsListDataModel = Field(alias="AppsList")
    apps_list_arn: str = Field(alias="AppsListArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComplianceDetailResponseModel(BaseModel):
    policy_compliance_detail: PolicyComplianceDetailModel = Field(
        alias="PolicyComplianceDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComplianceStatusResponseModel(BaseModel):
    policy_compliance_status_list: List[PolicyComplianceStatusModel] = Field(
        alias="PolicyComplianceStatusList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkFirewallPolicyDescriptionModel(BaseModel):
    stateless_rule_groups: Optional[List[StatelessRuleGroupModel]] = Field(
        default=None, alias="StatelessRuleGroups"
    )
    stateless_default_actions: Optional[List[str]] = Field(
        default=None, alias="StatelessDefaultActions"
    )
    stateless_fragment_default_actions: Optional[List[str]] = Field(
        default=None, alias="StatelessFragmentDefaultActions"
    )
    stateless_custom_actions: Optional[List[str]] = Field(
        default=None, alias="StatelessCustomActions"
    )
    stateful_rule_groups: Optional[List[StatefulRuleGroupModel]] = Field(
        default=None, alias="StatefulRuleGroups"
    )
    stateful_default_actions: Optional[List[str]] = Field(
        default=None, alias="StatefulDefaultActions"
    )
    stateful_engine_options: Optional[StatefulEngineOptionsModel] = Field(
        default=None, alias="StatefulEngineOptions"
    )


class SecurityServicePolicyDataModel(BaseModel):
    type: Literal[
        "DNS_FIREWALL",
        "IMPORT_NETWORK_FIREWALL",
        "NETWORK_FIREWALL",
        "SECURITY_GROUPS_COMMON",
        "SECURITY_GROUPS_CONTENT_AUDIT",
        "SECURITY_GROUPS_USAGE_AUDIT",
        "SHIELD_ADVANCED",
        "THIRD_PARTY_FIREWALL",
        "WAF",
        "WAFV2",
    ] = Field(alias="Type")
    managed_service_data: Optional[str] = Field(
        default=None, alias="ManagedServiceData"
    )
    policy_option: Optional[PolicyOptionModel] = Field(
        default=None, alias="PolicyOption"
    )


class AwsVPCSecurityGroupViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    violation_target_description: Optional[str] = Field(
        default=None, alias="ViolationTargetDescription"
    )
    partial_matches: Optional[List[PartialMatchModel]] = Field(
        default=None, alias="PartialMatches"
    )
    possible_security_group_remediation_actions: Optional[
        List[SecurityGroupRemediationActionModel]
    ] = Field(default=None, alias="PossibleSecurityGroupRemediationActions")


class RemediationActionWithOrderModel(BaseModel):
    remediation_action: Optional[RemediationActionModel] = Field(
        default=None, alias="RemediationAction"
    )
    order: Optional[int] = Field(default=None, alias="Order")


class NetworkFirewallPolicyModifiedViolationModel(BaseModel):
    violation_target: Optional[str] = Field(default=None, alias="ViolationTarget")
    current_policy_description: Optional[NetworkFirewallPolicyDescriptionModel] = Field(
        default=None, alias="CurrentPolicyDescription"
    )
    expected_policy_description: Optional[
        NetworkFirewallPolicyDescriptionModel
    ] = Field(default=None, alias="ExpectedPolicyDescription")


class PolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    security_service_policy_data: SecurityServicePolicyDataModel = Field(
        alias="SecurityServicePolicyData"
    )
    resource_type: str = Field(alias="ResourceType")
    exclude_resource_tags: bool = Field(alias="ExcludeResourceTags")
    remediation_enabled: bool = Field(alias="RemediationEnabled")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_update_token: Optional[str] = Field(default=None, alias="PolicyUpdateToken")
    resource_type_list: Optional[List[str]] = Field(
        default=None, alias="ResourceTypeList"
    )
    resource_tags: Optional[List[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )
    delete_unused_fmmanaged_resources: Optional[bool] = Field(
        default=None, alias="DeleteUnusedFMManagedResources"
    )
    include_map: Optional[Dict[Literal["ACCOUNT", "ORG_UNIT"], List[str]]] = Field(
        default=None, alias="IncludeMap"
    )
    exclude_map: Optional[Dict[Literal["ACCOUNT", "ORG_UNIT"], List[str]]] = Field(
        default=None, alias="ExcludeMap"
    )
    resource_set_ids: Optional[List[str]] = Field(default=None, alias="ResourceSetIds")
    policy_description: Optional[str] = Field(default=None, alias="PolicyDescription")


class PossibleRemediationActionModel(BaseModel):
    ordered_remediation_actions: List[RemediationActionWithOrderModel] = Field(
        alias="OrderedRemediationActions"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    is_default_action: Optional[bool] = Field(default=None, alias="IsDefaultAction")


class GetPolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    policy_arn: str = Field(alias="PolicyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPolicyRequestModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class PutPolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    policy_arn: str = Field(alias="PolicyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PossibleRemediationActionsModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    actions: Optional[List[PossibleRemediationActionModel]] = Field(
        default=None, alias="Actions"
    )


class ResourceViolationModel(BaseModel):
    aws_vp_csecurity_group_violation: Optional[
        AwsVPCSecurityGroupViolationModel
    ] = Field(default=None, alias="AwsVPCSecurityGroupViolation")
    aws_ec2_network_interface_violation: Optional[
        AwsEc2NetworkInterfaceViolationModel
    ] = Field(default=None, alias="AwsEc2NetworkInterfaceViolation")
    aws_ec2_instance_violation: Optional[AwsEc2InstanceViolationModel] = Field(
        default=None, alias="AwsEc2InstanceViolation"
    )
    network_firewall_missing_firewall_violation: Optional[
        NetworkFirewallMissingFirewallViolationModel
    ] = Field(default=None, alias="NetworkFirewallMissingFirewallViolation")
    network_firewall_missing_subnet_violation: Optional[
        NetworkFirewallMissingSubnetViolationModel
    ] = Field(default=None, alias="NetworkFirewallMissingSubnetViolation")
    network_firewall_missing_expected_rtviolation: Optional[
        NetworkFirewallMissingExpectedRTViolationModel
    ] = Field(default=None, alias="NetworkFirewallMissingExpectedRTViolation")
    network_firewall_policy_modified_violation: Optional[
        NetworkFirewallPolicyModifiedViolationModel
    ] = Field(default=None, alias="NetworkFirewallPolicyModifiedViolation")
    network_firewall_internet_traffic_not_inspected_violation: Optional[
        NetworkFirewallInternetTrafficNotInspectedViolationModel
    ] = Field(default=None, alias="NetworkFirewallInternetTrafficNotInspectedViolation")
    network_firewall_invalid_route_configuration_violation: Optional[
        NetworkFirewallInvalidRouteConfigurationViolationModel
    ] = Field(default=None, alias="NetworkFirewallInvalidRouteConfigurationViolation")
    network_firewall_black_hole_route_detected_violation: Optional[
        NetworkFirewallBlackHoleRouteDetectedViolationModel
    ] = Field(default=None, alias="NetworkFirewallBlackHoleRouteDetectedViolation")
    network_firewall_unexpected_firewall_routes_violation: Optional[
        NetworkFirewallUnexpectedFirewallRoutesViolationModel
    ] = Field(default=None, alias="NetworkFirewallUnexpectedFirewallRoutesViolation")
    network_firewall_unexpected_gateway_routes_violation: Optional[
        NetworkFirewallUnexpectedGatewayRoutesViolationModel
    ] = Field(default=None, alias="NetworkFirewallUnexpectedGatewayRoutesViolation")
    network_firewall_missing_expected_routes_violation: Optional[
        NetworkFirewallMissingExpectedRoutesViolationModel
    ] = Field(default=None, alias="NetworkFirewallMissingExpectedRoutesViolation")
    dns_rule_group_priority_conflict_violation: Optional[
        DnsRuleGroupPriorityConflictViolationModel
    ] = Field(default=None, alias="DnsRuleGroupPriorityConflictViolation")
    dns_duplicate_rule_group_violation: Optional[
        DnsDuplicateRuleGroupViolationModel
    ] = Field(default=None, alias="DnsDuplicateRuleGroupViolation")
    dns_rule_group_limit_exceeded_violation: Optional[
        DnsRuleGroupLimitExceededViolationModel
    ] = Field(default=None, alias="DnsRuleGroupLimitExceededViolation")
    possible_remediation_actions: Optional[PossibleRemediationActionsModel] = Field(
        default=None, alias="PossibleRemediationActions"
    )
    firewall_subnet_is_out_of_scope_violation: Optional[
        FirewallSubnetIsOutOfScopeViolationModel
    ] = Field(default=None, alias="FirewallSubnetIsOutOfScopeViolation")
    route_has_out_of_scope_endpoint_violation: Optional[
        RouteHasOutOfScopeEndpointViolationModel
    ] = Field(default=None, alias="RouteHasOutOfScopeEndpointViolation")
    third_party_firewall_missing_firewall_violation: Optional[
        ThirdPartyFirewallMissingFirewallViolationModel
    ] = Field(default=None, alias="ThirdPartyFirewallMissingFirewallViolation")
    third_party_firewall_missing_subnet_violation: Optional[
        ThirdPartyFirewallMissingSubnetViolationModel
    ] = Field(default=None, alias="ThirdPartyFirewallMissingSubnetViolation")
    third_party_firewall_missing_expected_route_table_violation: Optional[
        ThirdPartyFirewallMissingExpectedRouteTableViolationModel
    ] = Field(
        default=None, alias="ThirdPartyFirewallMissingExpectedRouteTableViolation"
    )
    firewall_subnet_missing_vp_cendpoint_violation: Optional[
        FirewallSubnetMissingVPCEndpointViolationModel
    ] = Field(default=None, alias="FirewallSubnetMissingVPCEndpointViolation")


class ViolationDetailModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    member_account: str = Field(alias="MemberAccount")
    resource_id: str = Field(alias="ResourceId")
    resource_type: str = Field(alias="ResourceType")
    resource_violations: List[ResourceViolationModel] = Field(
        alias="ResourceViolations"
    )
    resource_tags: Optional[List[TagModel]] = Field(default=None, alias="ResourceTags")
    resource_description: Optional[str] = Field(
        default=None, alias="ResourceDescription"
    )


class GetViolationDetailsResponseModel(BaseModel):
    violation_detail: ViolationDetailModel = Field(alias="ViolationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
