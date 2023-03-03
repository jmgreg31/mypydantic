# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class FirewallRuleGroupAssociationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    firewall_rule_group_id: Optional[str] = Field(
        default=None, alias="FirewallRuleGroupId"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    name: Optional[str] = Field(default=None, alias="Name")
    priority: Optional[int] = Field(default=None, alias="Priority")
    mutation_protection: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="MutationProtection"
    )
    managed_owner_name: Optional[str] = Field(default=None, alias="ManagedOwnerName")
    status: Optional[Literal["COMPLETE", "DELETING", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class IpAddressUpdateModel(BaseModel):
    ip_id: Optional[str] = Field(default=None, alias="IpId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    ip: Optional[str] = Field(default=None, alias="Ip")


class ResolverEndpointModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    direction: Optional[Literal["INBOUND", "OUTBOUND"]] = Field(
        default=None, alias="Direction"
    )
    ip_address_count: Optional[int] = Field(default=None, alias="IpAddressCount")
    host_vp_cid: Optional[str] = Field(default=None, alias="HostVPCId")
    status: Optional[
        Literal[
            "ACTION_NEEDED",
            "AUTO_RECOVERING",
            "CREATING",
            "DELETING",
            "OPERATIONAL",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class AssociateResolverQueryLogConfigRequestModel(BaseModel):
    resolver_query_log_config_id: str = Field(alias="ResolverQueryLogConfigId")
    resource_id: str = Field(alias="ResourceId")


class ResolverQueryLogConfigAssociationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    resolver_query_log_config_id: Optional[str] = Field(
        default=None, alias="ResolverQueryLogConfigId"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    status: Optional[
        Literal["ACTION_NEEDED", "ACTIVE", "CREATING", "DELETING", "FAILED"]
    ] = Field(default=None, alias="Status")
    error: Optional[
        Literal[
            "ACCESS_DENIED", "DESTINATION_NOT_FOUND", "INTERNAL_SERVICE_ERROR", "NONE"
        ]
    ] = Field(default=None, alias="Error")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")


class AssociateResolverRuleRequestModel(BaseModel):
    resolver_rule_id: str = Field(alias="ResolverRuleId")
    vp_cid: str = Field(alias="VPCId")
    name: Optional[str] = Field(default=None, alias="Name")


class ResolverRuleAssociationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    resolver_rule_id: Optional[str] = Field(default=None, alias="ResolverRuleId")
    name: Optional[str] = Field(default=None, alias="Name")
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")
    status: Optional[
        Literal["COMPLETE", "CREATING", "DELETING", "FAILED", "OVERRIDDEN"]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class FirewallDomainListModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    domain_count: Optional[int] = Field(default=None, alias="DomainCount")
    status: Optional[
        Literal[
            "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    managed_owner_name: Optional[str] = Field(default=None, alias="ManagedOwnerName")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class FirewallRuleGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    rule_count: Optional[int] = Field(default=None, alias="RuleCount")
    status: Optional[Literal["COMPLETE", "DELETING", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    share_status: Optional[
        Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
    ] = Field(default=None, alias="ShareStatus")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class CreateFirewallRuleRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    priority: int = Field(alias="Priority")
    action: Literal["ALERT", "ALLOW", "BLOCK"] = Field(alias="Action")
    name: str = Field(alias="Name")
    block_response: Optional[Literal["NODATA", "NXDOMAIN", "OVERRIDE"]] = Field(
        default=None, alias="BlockResponse"
    )
    block_override_domain: Optional[str] = Field(
        default=None, alias="BlockOverrideDomain"
    )
    block_override_dns_type: Optional[Literal["CNAME"]] = Field(
        default=None, alias="BlockOverrideDnsType"
    )
    block_override_ttl: Optional[int] = Field(default=None, alias="BlockOverrideTtl")


class FirewallRuleModel(BaseModel):
    firewall_rule_group_id: Optional[str] = Field(
        default=None, alias="FirewallRuleGroupId"
    )
    firewall_domain_list_id: Optional[str] = Field(
        default=None, alias="FirewallDomainListId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    priority: Optional[int] = Field(default=None, alias="Priority")
    action: Optional[Literal["ALERT", "ALLOW", "BLOCK"]] = Field(
        default=None, alias="Action"
    )
    block_response: Optional[Literal["NODATA", "NXDOMAIN", "OVERRIDE"]] = Field(
        default=None, alias="BlockResponse"
    )
    block_override_domain: Optional[str] = Field(
        default=None, alias="BlockOverrideDomain"
    )
    block_override_dns_type: Optional[Literal["CNAME"]] = Field(
        default=None, alias="BlockOverrideDnsType"
    )
    block_override_ttl: Optional[int] = Field(default=None, alias="BlockOverrideTtl")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class IpAddressRequestModel(BaseModel):
    subnet_id: str = Field(alias="SubnetId")
    ip: Optional[str] = Field(default=None, alias="Ip")


class ResolverQueryLogConfigModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    status: Optional[Literal["CREATED", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    share_status: Optional[
        Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
    ] = Field(default=None, alias="ShareStatus")
    association_count: Optional[int] = Field(default=None, alias="AssociationCount")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")


class TargetAddressModel(BaseModel):
    ip: str = Field(alias="Ip")
    port: Optional[int] = Field(default=None, alias="Port")


class DeleteFirewallDomainListRequestModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")


class DeleteFirewallRuleGroupRequestModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")


class DeleteFirewallRuleRequestModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")


class DeleteResolverEndpointRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")


class DeleteResolverQueryLogConfigRequestModel(BaseModel):
    resolver_query_log_config_id: str = Field(alias="ResolverQueryLogConfigId")


class DeleteResolverRuleRequestModel(BaseModel):
    resolver_rule_id: str = Field(alias="ResolverRuleId")


class DisassociateFirewallRuleGroupRequestModel(BaseModel):
    firewall_rule_group_association_id: str = Field(
        alias="FirewallRuleGroupAssociationId"
    )


class DisassociateResolverQueryLogConfigRequestModel(BaseModel):
    resolver_query_log_config_id: str = Field(alias="ResolverQueryLogConfigId")
    resource_id: str = Field(alias="ResourceId")


class DisassociateResolverRuleRequestModel(BaseModel):
    vp_cid: str = Field(alias="VPCId")
    resolver_rule_id: str = Field(alias="ResolverRuleId")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class FirewallConfigModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    firewall_fail_open: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FirewallFailOpen"
    )


class FirewallDomainListMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    managed_owner_name: Optional[str] = Field(default=None, alias="ManagedOwnerName")


class FirewallRuleGroupMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    share_status: Optional[
        Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
    ] = Field(default=None, alias="ShareStatus")


class GetFirewallConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")


class GetFirewallDomainListRequestModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")


class GetFirewallRuleGroupAssociationRequestModel(BaseModel):
    firewall_rule_group_association_id: str = Field(
        alias="FirewallRuleGroupAssociationId"
    )


class GetFirewallRuleGroupPolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GetFirewallRuleGroupRequestModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")


class GetResolverConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")


class ResolverConfigModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    autodefined_reverse: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
    ] = Field(default=None, alias="AutodefinedReverse")


class GetResolverDnssecConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")


class ResolverDnssecConfigModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    validation_status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
    ] = Field(default=None, alias="ValidationStatus")


class GetResolverEndpointRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")


class GetResolverQueryLogConfigAssociationRequestModel(BaseModel):
    resolver_query_log_config_association_id: str = Field(
        alias="ResolverQueryLogConfigAssociationId"
    )


class GetResolverQueryLogConfigPolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GetResolverQueryLogConfigRequestModel(BaseModel):
    resolver_query_log_config_id: str = Field(alias="ResolverQueryLogConfigId")


class GetResolverRuleAssociationRequestModel(BaseModel):
    resolver_rule_association_id: str = Field(alias="ResolverRuleAssociationId")


class GetResolverRulePolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GetResolverRuleRequestModel(BaseModel):
    resolver_rule_id: str = Field(alias="ResolverRuleId")


class ImportFirewallDomainsRequestModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    operation: Literal["REPLACE"] = Field(alias="Operation")
    domain_file_url: str = Field(alias="DomainFileUrl")


class IpAddressResponseModel(BaseModel):
    ip_id: Optional[str] = Field(default=None, alias="IpId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    ip: Optional[str] = Field(default=None, alias="Ip")
    status: Optional[
        Literal[
            "ATTACHED",
            "ATTACHING",
            "CREATING",
            "DELETE_FAILED_FAS_EXPIRED",
            "DELETING",
            "DETACHING",
            "FAILED_CREATION",
            "FAILED_RESOURCE_GONE",
            "REMAP_ATTACHING",
            "REMAP_DETACHING",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListFirewallConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFirewallDomainListsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFirewallDomainsRequestModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFirewallRuleGroupAssociationsRequestModel(BaseModel):
    firewall_rule_group_id: Optional[str] = Field(
        default=None, alias="FirewallRuleGroupId"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    status: Optional[Literal["COMPLETE", "DELETING", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFirewallRuleGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFirewallRulesRequestModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    action: Optional[Literal["ALERT", "ALLOW", "BLOCK"]] = Field(
        default=None, alias="Action"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListResolverConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListResolverEndpointIpAddressesRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PutFirewallRuleGroupPolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    firewall_rule_group_policy: str = Field(alias="FirewallRuleGroupPolicy")


class PutResolverQueryLogConfigPolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    resolver_query_log_config_policy: str = Field(alias="ResolverQueryLogConfigPolicy")


class PutResolverRulePolicyRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    resolver_rule_policy: str = Field(alias="ResolverRulePolicy")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFirewallConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    firewall_fail_open: Literal["DISABLED", "ENABLED"] = Field(alias="FirewallFailOpen")


class UpdateFirewallDomainsRequestModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    operation: Literal["ADD", "REMOVE", "REPLACE"] = Field(alias="Operation")
    domains: Sequence[str] = Field(alias="Domains")


class UpdateFirewallRuleGroupAssociationRequestModel(BaseModel):
    firewall_rule_group_association_id: str = Field(
        alias="FirewallRuleGroupAssociationId"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    mutation_protection: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="MutationProtection"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateFirewallRuleRequestModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    action: Optional[Literal["ALERT", "ALLOW", "BLOCK"]] = Field(
        default=None, alias="Action"
    )
    block_response: Optional[Literal["NODATA", "NXDOMAIN", "OVERRIDE"]] = Field(
        default=None, alias="BlockResponse"
    )
    block_override_domain: Optional[str] = Field(
        default=None, alias="BlockOverrideDomain"
    )
    block_override_dns_type: Optional[Literal["CNAME"]] = Field(
        default=None, alias="BlockOverrideDnsType"
    )
    block_override_ttl: Optional[int] = Field(default=None, alias="BlockOverrideTtl")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateResolverConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    autodefined_reverse_flag: Literal["DISABLE", "ENABLE"] = Field(
        alias="AutodefinedReverseFlag"
    )


class UpdateResolverDnssecConfigRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    validation: Literal["DISABLE", "ENABLE"] = Field(alias="Validation")


class UpdateResolverEndpointRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")
    name: Optional[str] = Field(default=None, alias="Name")


class AssociateFirewallRuleGroupRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    vpc_id: str = Field(alias="VpcId")
    priority: int = Field(alias="Priority")
    name: str = Field(alias="Name")
    mutation_protection: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="MutationProtection"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateFirewallDomainListRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    name: str = Field(alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateFirewallRuleGroupRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    name: str = Field(alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateResolverQueryLogConfigRequestModel(BaseModel):
    name: str = Field(alias="Name")
    destination_arn: str = Field(alias="DestinationArn")
    creator_request_id: str = Field(alias="CreatorRequestId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class AssociateFirewallRuleGroupResponseModel(BaseModel):
    firewall_rule_group_association: FirewallRuleGroupAssociationModel = Field(
        alias="FirewallRuleGroupAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateFirewallRuleGroupResponseModel(BaseModel):
    firewall_rule_group_association: FirewallRuleGroupAssociationModel = Field(
        alias="FirewallRuleGroupAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFirewallRuleGroupAssociationResponseModel(BaseModel):
    firewall_rule_group_association: FirewallRuleGroupAssociationModel = Field(
        alias="FirewallRuleGroupAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFirewallRuleGroupPolicyResponseModel(BaseModel):
    firewall_rule_group_policy: str = Field(alias="FirewallRuleGroupPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverQueryLogConfigPolicyResponseModel(BaseModel):
    resolver_query_log_config_policy: str = Field(alias="ResolverQueryLogConfigPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverRulePolicyResponseModel(BaseModel):
    resolver_rule_policy: str = Field(alias="ResolverRulePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportFirewallDomainsResponseModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
    ] = Field(alias="Status")
    status_message: str = Field(alias="StatusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallDomainsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    domains: List[str] = Field(alias="Domains")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallRuleGroupAssociationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_rule_group_associations: List[FirewallRuleGroupAssociationModel] = Field(
        alias="FirewallRuleGroupAssociations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutFirewallRuleGroupPolicyResponseModel(BaseModel):
    return_value: bool = Field(alias="ReturnValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResolverQueryLogConfigPolicyResponseModel(BaseModel):
    return_value: bool = Field(alias="ReturnValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResolverRulePolicyResponseModel(BaseModel):
    return_value: bool = Field(alias="ReturnValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallDomainsResponseModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
    ] = Field(alias="Status")
    status_message: str = Field(alias="StatusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallRuleGroupAssociationResponseModel(BaseModel):
    firewall_rule_group_association: FirewallRuleGroupAssociationModel = Field(
        alias="FirewallRuleGroupAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResolverEndpointIpAddressRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")
    ip_address: IpAddressUpdateModel = Field(alias="IpAddress")


class DisassociateResolverEndpointIpAddressRequestModel(BaseModel):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")
    ip_address: IpAddressUpdateModel = Field(alias="IpAddress")


class AssociateResolverEndpointIpAddressResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResolverEndpointResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResolverEndpointResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResolverEndpointIpAddressResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverEndpointResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverEndpointsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    max_results: int = Field(alias="MaxResults")
    resolver_endpoints: List[ResolverEndpointModel] = Field(alias="ResolverEndpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResolverEndpointResponseModel(BaseModel):
    resolver_endpoint: ResolverEndpointModel = Field(alias="ResolverEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResolverQueryLogConfigResponseModel(BaseModel):
    resolver_query_log_config_association: ResolverQueryLogConfigAssociationModel = (
        Field(alias="ResolverQueryLogConfigAssociation")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResolverQueryLogConfigResponseModel(BaseModel):
    resolver_query_log_config_association: ResolverQueryLogConfigAssociationModel = (
        Field(alias="ResolverQueryLogConfigAssociation")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverQueryLogConfigAssociationResponseModel(BaseModel):
    resolver_query_log_config_association: ResolverQueryLogConfigAssociationModel = (
        Field(alias="ResolverQueryLogConfigAssociation")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverQueryLogConfigAssociationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    total_filtered_count: int = Field(alias="TotalFilteredCount")
    resolver_query_log_config_associations: List[
        ResolverQueryLogConfigAssociationModel
    ] = Field(alias="ResolverQueryLogConfigAssociations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResolverRuleResponseModel(BaseModel):
    resolver_rule_association: ResolverRuleAssociationModel = Field(
        alias="ResolverRuleAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResolverRuleResponseModel(BaseModel):
    resolver_rule_association: ResolverRuleAssociationModel = Field(
        alias="ResolverRuleAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverRuleAssociationResponseModel(BaseModel):
    resolver_rule_association: ResolverRuleAssociationModel = Field(
        alias="ResolverRuleAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverRuleAssociationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    max_results: int = Field(alias="MaxResults")
    resolver_rule_associations: List[ResolverRuleAssociationModel] = Field(
        alias="ResolverRuleAssociations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFirewallDomainListResponseModel(BaseModel):
    firewall_domain_list: FirewallDomainListModel = Field(alias="FirewallDomainList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallDomainListResponseModel(BaseModel):
    firewall_domain_list: FirewallDomainListModel = Field(alias="FirewallDomainList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFirewallDomainListResponseModel(BaseModel):
    firewall_domain_list: FirewallDomainListModel = Field(alias="FirewallDomainList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFirewallRuleGroupResponseModel(BaseModel):
    firewall_rule_group: FirewallRuleGroupModel = Field(alias="FirewallRuleGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallRuleGroupResponseModel(BaseModel):
    firewall_rule_group: FirewallRuleGroupModel = Field(alias="FirewallRuleGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFirewallRuleGroupResponseModel(BaseModel):
    firewall_rule_group: FirewallRuleGroupModel = Field(alias="FirewallRuleGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFirewallRuleResponseModel(BaseModel):
    firewall_rule: FirewallRuleModel = Field(alias="FirewallRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallRuleResponseModel(BaseModel):
    firewall_rule: FirewallRuleModel = Field(alias="FirewallRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallRulesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_rules: List[FirewallRuleModel] = Field(alias="FirewallRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallRuleResponseModel(BaseModel):
    firewall_rule: FirewallRuleModel = Field(alias="FirewallRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResolverEndpointRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    direction: Literal["INBOUND", "OUTBOUND"] = Field(alias="Direction")
    ip_addresses: Sequence[IpAddressRequestModel] = Field(alias="IpAddresses")
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateResolverQueryLogConfigResponseModel(BaseModel):
    resolver_query_log_config: ResolverQueryLogConfigModel = Field(
        alias="ResolverQueryLogConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResolverQueryLogConfigResponseModel(BaseModel):
    resolver_query_log_config: ResolverQueryLogConfigModel = Field(
        alias="ResolverQueryLogConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverQueryLogConfigResponseModel(BaseModel):
    resolver_query_log_config: ResolverQueryLogConfigModel = Field(
        alias="ResolverQueryLogConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverQueryLogConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    total_filtered_count: int = Field(alias="TotalFilteredCount")
    resolver_query_log_configs: List[ResolverQueryLogConfigModel] = Field(
        alias="ResolverQueryLogConfigs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResolverRuleRequestModel(BaseModel):
    creator_request_id: str = Field(alias="CreatorRequestId")
    rule_type: Literal["FORWARD", "RECURSIVE", "SYSTEM"] = Field(alias="RuleType")
    domain_name: str = Field(alias="DomainName")
    name: Optional[str] = Field(default=None, alias="Name")
    target_ips: Optional[Sequence[TargetAddressModel]] = Field(
        default=None, alias="TargetIps"
    )
    resolver_endpoint_id: Optional[str] = Field(
        default=None, alias="ResolverEndpointId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ResolverRuleConfigModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    target_ips: Optional[Sequence[TargetAddressModel]] = Field(
        default=None, alias="TargetIps"
    )
    resolver_endpoint_id: Optional[str] = Field(
        default=None, alias="ResolverEndpointId"
    )


class ResolverRuleModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    status: Optional[Literal["COMPLETE", "DELETING", "FAILED", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    rule_type: Optional[Literal["FORWARD", "RECURSIVE", "SYSTEM"]] = Field(
        default=None, alias="RuleType"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    target_ips: Optional[List[TargetAddressModel]] = Field(
        default=None, alias="TargetIps"
    )
    resolver_endpoint_id: Optional[str] = Field(
        default=None, alias="ResolverEndpointId"
    )
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    share_status: Optional[
        Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
    ] = Field(default=None, alias="ShareStatus")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    modification_time: Optional[str] = Field(default=None, alias="ModificationTime")


class ListResolverDnssecConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListResolverEndpointsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListResolverQueryLogConfigAssociationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListResolverQueryLogConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListResolverRuleAssociationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListResolverRulesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class GetFirewallConfigResponseModel(BaseModel):
    firewall_config: FirewallConfigModel = Field(alias="FirewallConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_configs: List[FirewallConfigModel] = Field(alias="FirewallConfigs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallConfigResponseModel(BaseModel):
    firewall_config: FirewallConfigModel = Field(alias="FirewallConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallDomainListsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_domain_lists: List[FirewallDomainListMetadataModel] = Field(
        alias="FirewallDomainLists"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallRuleGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_rule_groups: List[FirewallRuleGroupMetadataModel] = Field(
        alias="FirewallRuleGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverConfigResponseModel(BaseModel):
    resolver_config: ResolverConfigModel = Field(alias="ResolverConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    resolver_configs: List[ResolverConfigModel] = Field(alias="ResolverConfigs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResolverConfigResponseModel(BaseModel):
    resolver_config: ResolverConfigModel = Field(alias="ResolverConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverDnssecConfigResponseModel(BaseModel):
    resolver_dns_s_ecconfig: ResolverDnssecConfigModel = Field(
        alias="ResolverDNSSECConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverDnssecConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    resolver_dnssec_configs: List[ResolverDnssecConfigModel] = Field(
        alias="ResolverDnssecConfigs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResolverDnssecConfigResponseModel(BaseModel):
    resolver_dns_s_ecconfig: ResolverDnssecConfigModel = Field(
        alias="ResolverDNSSECConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverEndpointIpAddressesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    max_results: int = Field(alias="MaxResults")
    ip_addresses: List[IpAddressResponseModel] = Field(alias="IpAddresses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallConfigsRequestListFirewallConfigsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallDomainListsRequestListFirewallDomainListsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallDomainsRequestListFirewallDomainsPaginateModel(BaseModel):
    firewall_domain_list_id: str = Field(alias="FirewallDomainListId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallRuleGroupAssociationsRequestListFirewallRuleGroupAssociationsPaginateModel(
    BaseModel
):
    firewall_rule_group_id: Optional[str] = Field(
        default=None, alias="FirewallRuleGroupId"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    status: Optional[Literal["COMPLETE", "DELETING", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallRuleGroupsRequestListFirewallRuleGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallRulesRequestListFirewallRulesPaginateModel(BaseModel):
    firewall_rule_group_id: str = Field(alias="FirewallRuleGroupId")
    priority: Optional[int] = Field(default=None, alias="Priority")
    action: Optional[Literal["ALERT", "ALLOW", "BLOCK"]] = Field(
        default=None, alias="Action"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverConfigsRequestListResolverConfigsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverDnssecConfigsRequestListResolverDnssecConfigsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverEndpointIpAddressesRequestListResolverEndpointIpAddressesPaginateModel(
    BaseModel
):
    resolver_endpoint_id: str = Field(alias="ResolverEndpointId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverEndpointsRequestListResolverEndpointsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverQueryLogConfigAssociationsRequestListResolverQueryLogConfigAssociationsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverQueryLogConfigsRequestListResolverQueryLogConfigsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverRuleAssociationsRequestListResolverRuleAssociationsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolverRulesRequestListResolverRulesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class UpdateResolverRuleRequestModel(BaseModel):
    resolver_rule_id: str = Field(alias="ResolverRuleId")
    config: ResolverRuleConfigModel = Field(alias="Config")


class CreateResolverRuleResponseModel(BaseModel):
    resolver_rule: ResolverRuleModel = Field(alias="ResolverRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResolverRuleResponseModel(BaseModel):
    resolver_rule: ResolverRuleModel = Field(alias="ResolverRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverRuleResponseModel(BaseModel):
    resolver_rule: ResolverRuleModel = Field(alias="ResolverRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolverRulesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    max_results: int = Field(alias="MaxResults")
    resolver_rules: List[ResolverRuleModel] = Field(alias="ResolverRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResolverRuleResponseModel(BaseModel):
    resolver_rule: ResolverRuleModel = Field(alias="ResolverRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
