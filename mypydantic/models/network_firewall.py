# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressModel(BaseModel):
    address_definition: str = Field(alias="AddressDefinition")


class AssociateFirewallPolicyRequestModel(BaseModel):
    firewall_policy_arn: str = Field(alias="FirewallPolicyArn")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SubnetMappingModel(BaseModel):
    subnet_id: str = Field(alias="SubnetId")
    ip_address_type: Optional[Literal["DUALSTACK", "IPV4"]] = Field(
        default=None, alias="IPAddressType"
    )


class AttachmentModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    status: Optional[Literal["CREATING", "DELETING", "READY", "SCALING"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class IPSetMetadataModel(BaseModel):
    resolved_cidrcount: Optional[int] = Field(default=None, alias="ResolvedCIDRCount")


class EncryptionConfigurationModel(BaseModel):
    type: Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_KMS"] = Field(alias="Type")
    key_id: Optional[str] = Field(default=None, alias="KeyId")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class SourceMetadataModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    source_update_token: Optional[str] = Field(default=None, alias="SourceUpdateToken")


class DeleteFirewallPolicyRequestModel(BaseModel):
    firewall_policy_name: Optional[str] = Field(
        default=None, alias="FirewallPolicyName"
    )
    firewall_policy_arn: Optional[str] = Field(default=None, alias="FirewallPolicyArn")


class DeleteFirewallRequestModel(BaseModel):
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteRuleGroupRequestModel(BaseModel):
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    rule_group_arn: Optional[str] = Field(default=None, alias="RuleGroupArn")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")


class DescribeFirewallPolicyRequestModel(BaseModel):
    firewall_policy_name: Optional[str] = Field(
        default=None, alias="FirewallPolicyName"
    )
    firewall_policy_arn: Optional[str] = Field(default=None, alias="FirewallPolicyArn")


class DescribeFirewallRequestModel(BaseModel):
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")


class DescribeLoggingConfigurationRequestModel(BaseModel):
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class DescribeResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DescribeRuleGroupMetadataRequestModel(BaseModel):
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    rule_group_arn: Optional[str] = Field(default=None, alias="RuleGroupArn")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")


class StatefulRuleOptionsModel(BaseModel):
    rule_order: Optional[Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]] = Field(
        default=None, alias="RuleOrder"
    )


class DescribeRuleGroupRequestModel(BaseModel):
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    rule_group_arn: Optional[str] = Field(default=None, alias="RuleGroupArn")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")


class DimensionModel(BaseModel):
    value: str = Field(alias="Value")


class DisassociateSubnetsRequestModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class FirewallMetadataModel(BaseModel):
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")


class FirewallPolicyMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")


class StatefulEngineOptionsModel(BaseModel):
    rule_order: Optional[Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]] = Field(
        default=None, alias="RuleOrder"
    )
    stream_exception_policy: Optional[Literal["CONTINUE", "DROP"]] = Field(
        default=None, alias="StreamExceptionPolicy"
    )


class StatelessRuleGroupReferenceModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    priority: int = Field(alias="Priority")


class HeaderModel(BaseModel):
    protocol: Literal[
        "DCERPC",
        "DHCP",
        "DNS",
        "FTP",
        "HTTP",
        "ICMP",
        "IKEV2",
        "IMAP",
        "IP",
        "KRB5",
        "MSN",
        "NTP",
        "SMB",
        "SMTP",
        "SSH",
        "TCP",
        "TFTP",
        "TLS",
        "UDP",
    ] = Field(alias="Protocol")
    source: str = Field(alias="Source")
    source_port: str = Field(alias="SourcePort")
    direction: Literal["ANY", "FORWARD"] = Field(alias="Direction")
    destination: str = Field(alias="Destination")
    destination_port: str = Field(alias="DestinationPort")


class IPSetReferenceModel(BaseModel):
    reference_arn: Optional[str] = Field(default=None, alias="ReferenceArn")


class IPSetModel(BaseModel):
    definition: Sequence[str] = Field(alias="Definition")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListFirewallPoliciesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFirewallsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    vpc_ids: Optional[Sequence[str]] = Field(default=None, alias="VpcIds")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRuleGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    scope: Optional[Literal["ACCOUNT", "MANAGED"]] = Field(default=None, alias="Scope")
    managed_type: Optional[
        Literal["AWS_MANAGED_DOMAIN_LISTS", "AWS_MANAGED_THREAT_SIGNATURES"]
    ] = Field(default=None, alias="ManagedType")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")


class RuleGroupMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class LogDestinationConfigModel(BaseModel):
    log_type: Literal["ALERT", "FLOW"] = Field(alias="LogType")
    log_destination_type: Literal[
        "CloudWatchLogs", "KinesisDataFirehose", "S3"
    ] = Field(alias="LogDestinationType")
    log_destination: Dict[str, str] = Field(alias="LogDestination")


class PortRangeModel(BaseModel):
    from_port: int = Field(alias="FromPort")
    to_port: int = Field(alias="ToPort")


class TCPFlagFieldModel(BaseModel):
    flags: Sequence[
        Literal["ACK", "CWR", "ECE", "FIN", "PSH", "RST", "SYN", "URG"]
    ] = Field(alias="Flags")
    masks: Optional[
        Sequence[Literal["ACK", "CWR", "ECE", "FIN", "PSH", "RST", "SYN", "URG"]]
    ] = Field(default=None, alias="Masks")


class PerObjectStatusModel(BaseModel):
    sync_status: Optional[
        Literal["CAPACITY_CONSTRAINED", "IN_SYNC", "PENDING"]
    ] = Field(default=None, alias="SyncStatus")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")


class PortSetModel(BaseModel):
    definition: Optional[Sequence[str]] = Field(default=None, alias="Definition")


class PutResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")


class RuleOptionModel(BaseModel):
    keyword: str = Field(alias="Keyword")
    settings: Optional[Sequence[str]] = Field(default=None, alias="Settings")


class RulesSourceListModel(BaseModel):
    targets: Sequence[str] = Field(alias="Targets")
    target_types: Sequence[Literal["HTTP_HOST", "TLS_SNI"]] = Field(alias="TargetTypes")
    generated_rules_type: Literal["ALLOWLIST", "DENYLIST"] = Field(
        alias="GeneratedRulesType"
    )


class StatefulRuleGroupOverrideModel(BaseModel):
    action: Optional[Literal["DROP_TO_ALERT"]] = Field(default=None, alias="Action")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFirewallDeleteProtectionRequestModel(BaseModel):
    delete_protection: bool = Field(alias="DeleteProtection")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class UpdateFirewallDescriptionRequestModel(BaseModel):
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateFirewallPolicyChangeProtectionRequestModel(BaseModel):
    firewall_policy_change_protection: bool = Field(
        alias="FirewallPolicyChangeProtection"
    )
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class UpdateSubnetChangeProtectionRequestModel(BaseModel):
    subnet_change_protection: bool = Field(alias="SubnetChangeProtection")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class AssociateFirewallPolicyResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    firewall_policy_arn: str = Field(alias="FirewallPolicyArn")
    update_token: str = Field(alias="UpdateToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallDeleteProtectionResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    delete_protection: bool = Field(alias="DeleteProtection")
    update_token: str = Field(alias="UpdateToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallDescriptionResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    description: str = Field(alias="Description")
    update_token: str = Field(alias="UpdateToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallPolicyChangeProtectionResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    firewall_policy_change_protection: bool = Field(
        alias="FirewallPolicyChangeProtection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubnetChangeProtectionResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    subnet_change_protection: bool = Field(alias="SubnetChangeProtection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateSubnetsRequestModel(BaseModel):
    subnet_mappings: Sequence[SubnetMappingModel] = Field(alias="SubnetMappings")
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")


class AssociateSubnetsResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    subnet_mappings: List[SubnetMappingModel] = Field(alias="SubnetMappings")
    update_token: str = Field(alias="UpdateToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateSubnetsResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    subnet_mappings: List[SubnetMappingModel] = Field(alias="SubnetMappings")
    update_token: str = Field(alias="UpdateToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CIDRSummaryModel(BaseModel):
    available_cidrcount: Optional[int] = Field(default=None, alias="AvailableCIDRCount")
    utilized_cidrcount: Optional[int] = Field(default=None, alias="UtilizedCIDRCount")
    ip_set_references: Optional[Dict[str, IPSetMetadataModel]] = Field(
        default=None, alias="IPSetReferences"
    )


class UpdateFirewallEncryptionConfigurationRequestModel(BaseModel):
    update_token: Optional[str] = Field(default=None, alias="UpdateToken")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class UpdateFirewallEncryptionConfigurationResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    update_token: str = Field(alias="UpdateToken")
    encryption_configuration: EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFirewallRequestModel(BaseModel):
    firewall_name: str = Field(alias="FirewallName")
    firewall_policy_arn: str = Field(alias="FirewallPolicyArn")
    vpc_id: str = Field(alias="VpcId")
    subnet_mappings: Sequence[SubnetMappingModel] = Field(alias="SubnetMappings")
    delete_protection: Optional[bool] = Field(default=None, alias="DeleteProtection")
    subnet_change_protection: Optional[bool] = Field(
        default=None, alias="SubnetChangeProtection"
    )
    firewall_policy_change_protection: Optional[bool] = Field(
        default=None, alias="FirewallPolicyChangeProtection"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class FirewallPolicyResponseModel(BaseModel):
    firewall_policy_name: str = Field(alias="FirewallPolicyName")
    firewall_policy_arn: str = Field(alias="FirewallPolicyArn")
    firewall_policy_id: str = Field(alias="FirewallPolicyId")
    description: Optional[str] = Field(default=None, alias="Description")
    firewall_policy_status: Optional[Literal["ACTIVE", "DELETING"]] = Field(
        default=None, alias="FirewallPolicyStatus"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    consumed_stateless_rule_capacity: Optional[int] = Field(
        default=None, alias="ConsumedStatelessRuleCapacity"
    )
    consumed_stateful_rule_capacity: Optional[int] = Field(
        default=None, alias="ConsumedStatefulRuleCapacity"
    )
    number_of_associations: Optional[int] = Field(
        default=None, alias="NumberOfAssociations"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class FirewallModel(BaseModel):
    firewall_policy_arn: str = Field(alias="FirewallPolicyArn")
    vpc_id: str = Field(alias="VpcId")
    subnet_mappings: List[SubnetMappingModel] = Field(alias="SubnetMappings")
    firewall_id: str = Field(alias="FirewallId")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    delete_protection: Optional[bool] = Field(default=None, alias="DeleteProtection")
    subnet_change_protection: Optional[bool] = Field(
        default=None, alias="SubnetChangeProtection"
    )
    firewall_policy_change_protection: Optional[bool] = Field(
        default=None, alias="FirewallPolicyChangeProtection"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class ListTagsForResourceResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class RuleGroupResponseModel(BaseModel):
    rule_group_arn: str = Field(alias="RuleGroupArn")
    rule_group_name: str = Field(alias="RuleGroupName")
    rule_group_id: str = Field(alias="RuleGroupId")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    rule_group_status: Optional[Literal["ACTIVE", "DELETING"]] = Field(
        default=None, alias="RuleGroupStatus"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    consumed_capacity: Optional[int] = Field(default=None, alias="ConsumedCapacity")
    number_of_associations: Optional[int] = Field(
        default=None, alias="NumberOfAssociations"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    source_metadata: Optional[SourceMetadataModel] = Field(
        default=None, alias="SourceMetadata"
    )
    sns_topic: Optional[str] = Field(default=None, alias="SnsTopic")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class DescribeRuleGroupMetadataResponseModel(BaseModel):
    rule_group_arn: str = Field(alias="RuleGroupArn")
    rule_group_name: str = Field(alias="RuleGroupName")
    description: str = Field(alias="Description")
    type: Literal["STATEFUL", "STATELESS"] = Field(alias="Type")
    capacity: int = Field(alias="Capacity")
    stateful_rule_options: StatefulRuleOptionsModel = Field(alias="StatefulRuleOptions")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishMetricActionModel(BaseModel):
    dimensions: Sequence[DimensionModel] = Field(alias="Dimensions")


class ListFirewallsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewalls: List[FirewallMetadataModel] = Field(alias="Firewalls")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFirewallPoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    firewall_policies: List[FirewallPolicyMetadataModel] = Field(
        alias="FirewallPolicies"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReferenceSetsModel(BaseModel):
    ip_set_references: Optional[Mapping[str, IPSetReferenceModel]] = Field(
        default=None, alias="IPSetReferences"
    )


class ListFirewallPoliciesRequestListFirewallPoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFirewallsRequestListFirewallsPaginateModel(BaseModel):
    vpc_ids: Optional[Sequence[str]] = Field(default=None, alias="VpcIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRuleGroupsRequestListRuleGroupsPaginateModel(BaseModel):
    scope: Optional[Literal["ACCOUNT", "MANAGED"]] = Field(default=None, alias="Scope")
    managed_type: Optional[
        Literal["AWS_MANAGED_DOMAIN_LISTS", "AWS_MANAGED_THREAT_SIGNATURES"]
    ] = Field(default=None, alias="ManagedType")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRuleGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    rule_groups: List[RuleGroupMetadataModel] = Field(alias="RuleGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingConfigurationModel(BaseModel):
    log_destination_configs: List[LogDestinationConfigModel] = Field(
        alias="LogDestinationConfigs"
    )


class MatchAttributesModel(BaseModel):
    sources: Optional[Sequence[AddressModel]] = Field(default=None, alias="Sources")
    destinations: Optional[Sequence[AddressModel]] = Field(
        default=None, alias="Destinations"
    )
    source_ports: Optional[Sequence[PortRangeModel]] = Field(
        default=None, alias="SourcePorts"
    )
    destination_ports: Optional[Sequence[PortRangeModel]] = Field(
        default=None, alias="DestinationPorts"
    )
    protocols: Optional[Sequence[int]] = Field(default=None, alias="Protocols")
    tcp_flags: Optional[Sequence[TCPFlagFieldModel]] = Field(
        default=None, alias="TCPFlags"
    )


class SyncStateModel(BaseModel):
    attachment: Optional[AttachmentModel] = Field(default=None, alias="Attachment")
    config: Optional[Dict[str, PerObjectStatusModel]] = Field(
        default=None, alias="Config"
    )


class RuleVariablesModel(BaseModel):
    ip_sets: Optional[Mapping[str, IPSetModel]] = Field(default=None, alias="IPSets")
    port_sets: Optional[Mapping[str, PortSetModel]] = Field(
        default=None, alias="PortSets"
    )


class StatefulRuleModel(BaseModel):
    action: Literal["ALERT", "DROP", "PASS", "REJECT"] = Field(alias="Action")
    header: HeaderModel = Field(alias="Header")
    rule_options: Sequence[RuleOptionModel] = Field(alias="RuleOptions")


class StatefulRuleGroupReferenceModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    priority: Optional[int] = Field(default=None, alias="Priority")
    override: Optional[StatefulRuleGroupOverrideModel] = Field(
        default=None, alias="Override"
    )


class CapacityUsageSummaryModel(BaseModel):
    cidrs: Optional[CIDRSummaryModel] = Field(default=None, alias="CIDRs")


class CreateFirewallPolicyResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_policy_response: FirewallPolicyResponseModel = Field(
        alias="FirewallPolicyResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallPolicyResponseModel(BaseModel):
    firewall_policy_response: FirewallPolicyResponseModel = Field(
        alias="FirewallPolicyResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallPolicyResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_policy_response: FirewallPolicyResponseModel = Field(
        alias="FirewallPolicyResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleGroupResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    rule_group_response: RuleGroupResponseModel = Field(alias="RuleGroupResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRuleGroupResponseModel(BaseModel):
    rule_group_response: RuleGroupResponseModel = Field(alias="RuleGroupResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleGroupResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    rule_group_response: RuleGroupResponseModel = Field(alias="RuleGroupResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionDefinitionModel(BaseModel):
    publish_metric_action: Optional[PublishMetricActionModel] = Field(
        default=None, alias="PublishMetricAction"
    )


class DescribeLoggingConfigurationResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLoggingConfigurationRequestModel(BaseModel):
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    logging_configuration: Optional[LoggingConfigurationModel] = Field(
        default=None, alias="LoggingConfiguration"
    )


class UpdateLoggingConfigurationResponseModel(BaseModel):
    firewall_arn: str = Field(alias="FirewallArn")
    firewall_name: str = Field(alias="FirewallName")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleDefinitionModel(BaseModel):
    match_attributes: MatchAttributesModel = Field(alias="MatchAttributes")
    actions: Sequence[str] = Field(alias="Actions")


class FirewallStatusModel(BaseModel):
    status: Literal["DELETING", "PROVISIONING", "READY"] = Field(alias="Status")
    configuration_sync_state_summary: Literal[
        "CAPACITY_CONSTRAINED", "IN_SYNC", "PENDING"
    ] = Field(alias="ConfigurationSyncStateSummary")
    sync_states: Optional[Dict[str, SyncStateModel]] = Field(
        default=None, alias="SyncStates"
    )
    capacity_usage_summary: Optional[CapacityUsageSummaryModel] = Field(
        default=None, alias="CapacityUsageSummary"
    )


class CustomActionModel(BaseModel):
    action_name: str = Field(alias="ActionName")
    action_definition: ActionDefinitionModel = Field(alias="ActionDefinition")


class StatelessRuleModel(BaseModel):
    rule_definition: RuleDefinitionModel = Field(alias="RuleDefinition")
    priority: int = Field(alias="Priority")


class CreateFirewallResponseModel(BaseModel):
    firewall: FirewallModel = Field(alias="Firewall")
    firewall_status: FirewallStatusModel = Field(alias="FirewallStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFirewallResponseModel(BaseModel):
    firewall: FirewallModel = Field(alias="Firewall")
    firewall_status: FirewallStatusModel = Field(alias="FirewallStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFirewallResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall: FirewallModel = Field(alias="Firewall")
    firewall_status: FirewallStatusModel = Field(alias="FirewallStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FirewallPolicyModel(BaseModel):
    stateless_default_actions: Sequence[str] = Field(alias="StatelessDefaultActions")
    stateless_fragment_default_actions: Sequence[str] = Field(
        alias="StatelessFragmentDefaultActions"
    )
    stateless_rule_group_references: Optional[
        Sequence[StatelessRuleGroupReferenceModel]
    ] = Field(default=None, alias="StatelessRuleGroupReferences")
    stateless_custom_actions: Optional[Sequence[CustomActionModel]] = Field(
        default=None, alias="StatelessCustomActions"
    )
    stateful_rule_group_references: Optional[
        Sequence[StatefulRuleGroupReferenceModel]
    ] = Field(default=None, alias="StatefulRuleGroupReferences")
    stateful_default_actions: Optional[Sequence[str]] = Field(
        default=None, alias="StatefulDefaultActions"
    )
    stateful_engine_options: Optional[StatefulEngineOptionsModel] = Field(
        default=None, alias="StatefulEngineOptions"
    )


class StatelessRulesAndCustomActionsModel(BaseModel):
    stateless_rules: Sequence[StatelessRuleModel] = Field(alias="StatelessRules")
    custom_actions: Optional[Sequence[CustomActionModel]] = Field(
        default=None, alias="CustomActions"
    )


class CreateFirewallPolicyRequestModel(BaseModel):
    firewall_policy_name: str = Field(alias="FirewallPolicyName")
    firewall_policy: FirewallPolicyModel = Field(alias="FirewallPolicy")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class DescribeFirewallPolicyResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_policy_response: FirewallPolicyResponseModel = Field(
        alias="FirewallPolicyResponse"
    )
    firewall_policy: FirewallPolicyModel = Field(alias="FirewallPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFirewallPolicyRequestModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    firewall_policy: FirewallPolicyModel = Field(alias="FirewallPolicy")
    firewall_policy_arn: Optional[str] = Field(default=None, alias="FirewallPolicyArn")
    firewall_policy_name: Optional[str] = Field(
        default=None, alias="FirewallPolicyName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class RulesSourceModel(BaseModel):
    rules_string: Optional[str] = Field(default=None, alias="RulesString")
    rules_source_list: Optional[RulesSourceListModel] = Field(
        default=None, alias="RulesSourceList"
    )
    stateful_rules: Optional[Sequence[StatefulRuleModel]] = Field(
        default=None, alias="StatefulRules"
    )
    stateless_rules_and_custom_actions: Optional[
        StatelessRulesAndCustomActionsModel
    ] = Field(default=None, alias="StatelessRulesAndCustomActions")


class RuleGroupModel(BaseModel):
    rules_source: RulesSourceModel = Field(alias="RulesSource")
    rule_variables: Optional[RuleVariablesModel] = Field(
        default=None, alias="RuleVariables"
    )
    reference_sets: Optional[ReferenceSetsModel] = Field(
        default=None, alias="ReferenceSets"
    )
    stateful_rule_options: Optional[StatefulRuleOptionsModel] = Field(
        default=None, alias="StatefulRuleOptions"
    )


class CreateRuleGroupRequestModel(BaseModel):
    rule_group_name: str = Field(alias="RuleGroupName")
    type: Literal["STATEFUL", "STATELESS"] = Field(alias="Type")
    capacity: int = Field(alias="Capacity")
    rule_group: Optional[RuleGroupModel] = Field(default=None, alias="RuleGroup")
    rules: Optional[str] = Field(default=None, alias="Rules")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    source_metadata: Optional[SourceMetadataModel] = Field(
        default=None, alias="SourceMetadata"
    )


class DescribeRuleGroupResponseModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    rule_group: RuleGroupModel = Field(alias="RuleGroup")
    rule_group_response: RuleGroupResponseModel = Field(alias="RuleGroupResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleGroupRequestModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    rule_group_arn: Optional[str] = Field(default=None, alias="RuleGroupArn")
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    rule_group: Optional[RuleGroupModel] = Field(default=None, alias="RuleGroup")
    rules: Optional[str] = Field(default=None, alias="Rules")
    type: Optional[Literal["STATEFUL", "STATELESS"]] = Field(default=None, alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    source_metadata: Optional[SourceMetadataModel] = Field(
        default=None, alias="SourceMetadata"
    )
