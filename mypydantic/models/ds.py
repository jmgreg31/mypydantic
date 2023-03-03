# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptSharedDirectoryRequestModel(BaseModel):
    shared_directory_id: str = Field(alias="SharedDirectoryId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SharedDirectoryModel(BaseModel):
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    owner_directory_id: Optional[str] = Field(default=None, alias="OwnerDirectoryId")
    share_method: Optional[Literal["HANDSHAKE", "ORGANIZATIONS"]] = Field(
        default=None, alias="ShareMethod"
    )
    shared_account_id: Optional[str] = Field(default=None, alias="SharedAccountId")
    shared_directory_id: Optional[str] = Field(default=None, alias="SharedDirectoryId")
    share_status: Optional[
        Literal[
            "Deleted",
            "Deleting",
            "PendingAcceptance",
            "RejectFailed",
            "Rejected",
            "Rejecting",
            "ShareFailed",
            "Shared",
            "Sharing",
        ]
    ] = Field(default=None, alias="ShareStatus")
    share_notes: Optional[str] = Field(default=None, alias="ShareNotes")
    created_date_time: Optional[datetime] = Field(default=None, alias="CreatedDateTime")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )


class IpRouteModel(BaseModel):
    cidr_ip: Optional[str] = Field(default=None, alias="CidrIp")
    description: Optional[str] = Field(default=None, alias="Description")


class DirectoryVpcSettingsModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AttributeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class CancelSchemaExtensionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    schema_extension_id: str = Field(alias="SchemaExtensionId")


class CertificateInfoModel(BaseModel):
    certificate_id: Optional[str] = Field(default=None, alias="CertificateId")
    common_name: Optional[str] = Field(default=None, alias="CommonName")
    state: Optional[
        Literal[
            "DeregisterFailed",
            "Deregistered",
            "Deregistering",
            "RegisterFailed",
            "Registered",
            "Registering",
        ]
    ] = Field(default=None, alias="State")
    expiry_date_time: Optional[datetime] = Field(default=None, alias="ExpiryDateTime")
    type: Optional[Literal["ClientCertAuth", "ClientLDAPS"]] = Field(
        default=None, alias="Type"
    )


class ClientCertAuthSettingsModel(BaseModel):
    ocs_p_url: Optional[str] = Field(default=None, alias="OCSPUrl")


class ClientAuthenticationSettingInfoModel(BaseModel):
    type: Optional[Literal["SmartCard", "SmartCardOrPassword"]] = Field(
        default=None, alias="Type"
    )
    status: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Status"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )


class ConditionalForwarderModel(BaseModel):
    remote_domain_name: Optional[str] = Field(default=None, alias="RemoteDomainName")
    dns_ip_addrs: Optional[List[str]] = Field(default=None, alias="DnsIpAddrs")
    replication_scope: Optional[Literal["Domain"]] = Field(
        default=None, alias="ReplicationScope"
    )


class DirectoryConnectSettingsModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    customer_dns_ips: Sequence[str] = Field(alias="CustomerDnsIps")
    customer_user_name: str = Field(alias="CustomerUserName")


class CreateAliasRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    alias: str = Field(alias="Alias")


class CreateConditionalForwarderRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    remote_domain_name: str = Field(alias="RemoteDomainName")
    dns_ip_addrs: Sequence[str] = Field(alias="DnsIpAddrs")


class CreateLogSubscriptionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    log_group_name: str = Field(alias="LogGroupName")


class CreateSnapshotRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    name: Optional[str] = Field(default=None, alias="Name")


class CreateTrustRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    remote_domain_name: str = Field(alias="RemoteDomainName")
    trust_password: str = Field(alias="TrustPassword")
    trust_direction: Literal[
        "One-Way: Incoming", "One-Way: Outgoing", "Two-Way"
    ] = Field(alias="TrustDirection")
    trust_type: Optional[Literal["External", "Forest"]] = Field(
        default=None, alias="TrustType"
    )
    conditional_forwarder_ip_addrs: Optional[Sequence[str]] = Field(
        default=None, alias="ConditionalForwarderIpAddrs"
    )
    selective_auth: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="SelectiveAuth"
    )


class DeleteConditionalForwarderRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    remote_domain_name: str = Field(alias="RemoteDomainName")


class DeleteDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class DeleteLogSubscriptionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class DeleteSnapshotRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")


class DeleteTrustRequestModel(BaseModel):
    trust_id: str = Field(alias="TrustId")
    delete_associated_conditional_forwarder: Optional[bool] = Field(
        default=None, alias="DeleteAssociatedConditionalForwarder"
    )


class DeregisterCertificateRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    certificate_id: str = Field(alias="CertificateId")


class DeregisterEventTopicRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    topic_name: str = Field(alias="TopicName")


class DescribeCertificateRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    certificate_id: str = Field(alias="CertificateId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeClientAuthenticationSettingsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Optional[Literal["SmartCard", "SmartCardOrPassword"]] = Field(
        default=None, alias="Type"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeConditionalForwardersRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    remote_domain_names: Optional[Sequence[str]] = Field(
        default=None, alias="RemoteDomainNames"
    )


class DescribeDirectoriesRequestModel(BaseModel):
    directory_ids: Optional[Sequence[str]] = Field(default=None, alias="DirectoryIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeDomainControllersRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    domain_controller_ids: Optional[Sequence[str]] = Field(
        default=None, alias="DomainControllerIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DomainControllerModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    domain_controller_id: Optional[str] = Field(
        default=None, alias="DomainControllerId"
    )
    dns_ip_addr: Optional[str] = Field(default=None, alias="DnsIpAddr")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    status: Optional[
        Literal[
            "Active",
            "Creating",
            "Deleted",
            "Deleting",
            "Failed",
            "Impaired",
            "Restoring",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    launch_time: Optional[datetime] = Field(default=None, alias="LaunchTime")
    status_last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="StatusLastUpdatedDateTime"
    )


class DescribeEventTopicsRequestModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    topic_names: Optional[Sequence[str]] = Field(default=None, alias="TopicNames")


class EventTopicModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    topic_name: Optional[str] = Field(default=None, alias="TopicName")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    created_date_time: Optional[datetime] = Field(default=None, alias="CreatedDateTime")
    status: Optional[
        Literal["Deleted", "Failed", "Registered", "Topic not found"]
    ] = Field(default=None, alias="Status")


class DescribeLDAPSSettingsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Optional[Literal["Client"]] = Field(default=None, alias="Type")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class LDAPSSettingInfoModel(BaseModel):
    l_dap_s_status: Optional[
        Literal["Disabled", "EnableFailed", "Enabled", "Enabling"]
    ] = Field(default=None, alias="LDAPSStatus")
    l_dap_s_status_reason: Optional[str] = Field(
        default=None, alias="LDAPSStatusReason"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )


class DescribeRegionsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeSettingsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    status: Optional[
        Literal["Default", "Failed", "Requested", "Updated", "Updating"]
    ] = Field(default=None, alias="Status")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SettingEntryModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    applied_value: Optional[str] = Field(default=None, alias="AppliedValue")
    requested_value: Optional[str] = Field(default=None, alias="RequestedValue")
    request_status: Optional[
        Literal["Default", "Failed", "Requested", "Updated", "Updating"]
    ] = Field(default=None, alias="RequestStatus")
    request_detailed_status: Optional[
        Dict[str, Literal["Default", "Failed", "Requested", "Updated", "Updating"]]
    ] = Field(default=None, alias="RequestDetailedStatus")
    request_status_message: Optional[str] = Field(
        default=None, alias="RequestStatusMessage"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )
    last_requested_date_time: Optional[datetime] = Field(
        default=None, alias="LastRequestedDateTime"
    )


class DescribeSharedDirectoriesRequestModel(BaseModel):
    owner_directory_id: str = Field(alias="OwnerDirectoryId")
    shared_directory_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SharedDirectoryIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeSnapshotsRequestModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    snapshot_ids: Optional[Sequence[str]] = Field(default=None, alias="SnapshotIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class SnapshotModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    type: Optional[Literal["Auto", "Manual"]] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["Completed", "Creating", "Failed"]] = Field(
        default=None, alias="Status"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")


class DescribeTrustsRequestModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    trust_ids: Optional[Sequence[str]] = Field(default=None, alias="TrustIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class TrustModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    trust_id: Optional[str] = Field(default=None, alias="TrustId")
    remote_domain_name: Optional[str] = Field(default=None, alias="RemoteDomainName")
    trust_type: Optional[Literal["External", "Forest"]] = Field(
        default=None, alias="TrustType"
    )
    trust_direction: Optional[
        Literal["One-Way: Incoming", "One-Way: Outgoing", "Two-Way"]
    ] = Field(default=None, alias="TrustDirection")
    trust_state: Optional[
        Literal[
            "Created",
            "Creating",
            "Deleted",
            "Deleting",
            "Failed",
            "UpdateFailed",
            "Updated",
            "Updating",
            "Verified",
            "VerifyFailed",
            "Verifying",
        ]
    ] = Field(default=None, alias="TrustState")
    created_date_time: Optional[datetime] = Field(default=None, alias="CreatedDateTime")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )
    state_last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="StateLastUpdatedDateTime"
    )
    trust_state_reason: Optional[str] = Field(default=None, alias="TrustStateReason")
    selective_auth: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="SelectiveAuth"
    )


class DescribeUpdateDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    update_type: Literal["OS"] = Field(alias="UpdateType")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DirectoryConnectSettingsDescriptionModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    customer_user_name: Optional[str] = Field(default=None, alias="CustomerUserName")
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    connect_ips: Optional[List[str]] = Field(default=None, alias="ConnectIps")


class DirectoryVpcSettingsDescriptionModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )


class RadiusSettingsModel(BaseModel):
    radius_servers: Optional[List[str]] = Field(default=None, alias="RadiusServers")
    radius_port: Optional[int] = Field(default=None, alias="RadiusPort")
    radius_timeout: Optional[int] = Field(default=None, alias="RadiusTimeout")
    radius_retries: Optional[int] = Field(default=None, alias="RadiusRetries")
    shared_secret: Optional[str] = Field(default=None, alias="SharedSecret")
    authentication_protocol: Optional[
        Literal["CHAP", "MS-CHAPv1", "MS-CHAPv2", "PAP"]
    ] = Field(default=None, alias="AuthenticationProtocol")
    display_label: Optional[str] = Field(default=None, alias="DisplayLabel")
    use_same_username: Optional[bool] = Field(default=None, alias="UseSameUsername")


class RegionsInfoModel(BaseModel):
    primary_region: Optional[str] = Field(default=None, alias="PrimaryRegion")
    additional_regions: Optional[List[str]] = Field(
        default=None, alias="AdditionalRegions"
    )


class DirectoryLimitsModel(BaseModel):
    cloud_only_directories_limit: Optional[int] = Field(
        default=None, alias="CloudOnlyDirectoriesLimit"
    )
    cloud_only_directories_current_count: Optional[int] = Field(
        default=None, alias="CloudOnlyDirectoriesCurrentCount"
    )
    cloud_only_directories_limit_reached: Optional[bool] = Field(
        default=None, alias="CloudOnlyDirectoriesLimitReached"
    )
    cloud_only_microsoft_adlimit: Optional[int] = Field(
        default=None, alias="CloudOnlyMicrosoftADLimit"
    )
    cloud_only_microsoft_adcurrent_count: Optional[int] = Field(
        default=None, alias="CloudOnlyMicrosoftADCurrentCount"
    )
    cloud_only_microsoft_adlimit_reached: Optional[bool] = Field(
        default=None, alias="CloudOnlyMicrosoftADLimitReached"
    )
    connected_directories_limit: Optional[int] = Field(
        default=None, alias="ConnectedDirectoriesLimit"
    )
    connected_directories_current_count: Optional[int] = Field(
        default=None, alias="ConnectedDirectoriesCurrentCount"
    )
    connected_directories_limit_reached: Optional[bool] = Field(
        default=None, alias="ConnectedDirectoriesLimitReached"
    )


class DisableClientAuthenticationRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Literal["SmartCard", "SmartCardOrPassword"] = Field(alias="Type")


class DisableLDAPSRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Literal["Client"] = Field(alias="Type")


class DisableRadiusRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class DisableSsoRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    password: Optional[str] = Field(default=None, alias="Password")


class EnableClientAuthenticationRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Literal["SmartCard", "SmartCardOrPassword"] = Field(alias="Type")


class EnableLDAPSRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Literal["Client"] = Field(alias="Type")


class EnableSsoRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    password: Optional[str] = Field(default=None, alias="Password")


class GetSnapshotLimitsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class SnapshotLimitsModel(BaseModel):
    manual_snapshots_limit: Optional[int] = Field(
        default=None, alias="ManualSnapshotsLimit"
    )
    manual_snapshots_current_count: Optional[int] = Field(
        default=None, alias="ManualSnapshotsCurrentCount"
    )
    manual_snapshots_limit_reached: Optional[bool] = Field(
        default=None, alias="ManualSnapshotsLimitReached"
    )


class IpRouteInfoModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    cidr_ip: Optional[str] = Field(default=None, alias="CidrIp")
    ip_route_status_msg: Optional[
        Literal["AddFailed", "Added", "Adding", "RemoveFailed", "Removed", "Removing"]
    ] = Field(default=None, alias="IpRouteStatusMsg")
    added_date_time: Optional[datetime] = Field(default=None, alias="AddedDateTime")
    ip_route_status_reason: Optional[str] = Field(
        default=None, alias="IpRouteStatusReason"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ListCertificatesRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListIpRoutesRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListLogSubscriptionsRequestModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class LogSubscriptionModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    subscription_created_date_time: Optional[datetime] = Field(
        default=None, alias="SubscriptionCreatedDateTime"
    )


class ListSchemaExtensionsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class SchemaExtensionInfoModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    schema_extension_id: Optional[str] = Field(default=None, alias="SchemaExtensionId")
    description: Optional[str] = Field(default=None, alias="Description")
    schema_extension_status: Optional[
        Literal[
            "CancelInProgress",
            "Cancelled",
            "Completed",
            "CreatingSnapshot",
            "Failed",
            "Initializing",
            "Replicating",
            "RollbackInProgress",
            "UpdatingSchema",
        ]
    ] = Field(default=None, alias="SchemaExtensionStatus")
    schema_extension_status_reason: Optional[str] = Field(
        default=None, alias="SchemaExtensionStatusReason"
    )
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class OSUpdateSettingsModel(BaseModel):
    os_version: Optional[Literal["SERVER_2012", "SERVER_2019"]] = Field(
        default=None, alias="OSVersion"
    )


class RegisterEventTopicRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    topic_name: str = Field(alias="TopicName")


class RejectSharedDirectoryRequestModel(BaseModel):
    shared_directory_id: str = Field(alias="SharedDirectoryId")


class RemoveIpRoutesRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    cidr_ips: Sequence[str] = Field(alias="CidrIps")


class RemoveRegionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class RemoveTagsFromResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ResetUserPasswordRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    user_name: str = Field(alias="UserName")
    new_password: str = Field(alias="NewPassword")


class RestoreFromSnapshotRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")


class SettingModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class ShareTargetModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal["ACCOUNT"] = Field(alias="Type")


class StartSchemaExtensionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    create_snapshot_before_schema_extension: bool = Field(
        alias="CreateSnapshotBeforeSchemaExtension"
    )
    ldif_content: str = Field(alias="LdifContent")
    description: str = Field(alias="Description")


class UnshareTargetModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal["ACCOUNT"] = Field(alias="Type")


class UpdateConditionalForwarderRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    remote_domain_name: str = Field(alias="RemoteDomainName")
    dns_ip_addrs: Sequence[str] = Field(alias="DnsIpAddrs")


class UpdateNumberOfDomainControllersRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    desired_number: int = Field(alias="DesiredNumber")


class UpdateTrustRequestModel(BaseModel):
    trust_id: str = Field(alias="TrustId")
    selective_auth: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="SelectiveAuth"
    )


class VerifyTrustRequestModel(BaseModel):
    trust_id: str = Field(alias="TrustId")


class ConnectDirectoryResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAliasResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    alias: str = Field(alias="Alias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDirectoryResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMicrosoftADResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotResultModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrustResultModel(BaseModel):
    trust_id: str = Field(alias="TrustId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDirectoryResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotResultModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTrustResultModel(BaseModel):
    trust_id: str = Field(alias="TrustId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterCertificateResultModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectSharedDirectoryResultModel(BaseModel):
    shared_directory_id: str = Field(alias="SharedDirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ShareDirectoryResultModel(BaseModel):
    shared_directory_id: str = Field(alias="SharedDirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSchemaExtensionResultModel(BaseModel):
    schema_extension_id: str = Field(alias="SchemaExtensionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnshareDirectoryResultModel(BaseModel):
    shared_directory_id: str = Field(alias="SharedDirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSettingsResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrustResultModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    trust_id: str = Field(alias="TrustId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyTrustResultModel(BaseModel):
    trust_id: str = Field(alias="TrustId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptSharedDirectoryResultModel(BaseModel):
    shared_directory: SharedDirectoryModel = Field(alias="SharedDirectory")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSharedDirectoriesResultModel(BaseModel):
    shared_directories: List[SharedDirectoryModel] = Field(alias="SharedDirectories")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddIpRoutesRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    ip_routes: Sequence[IpRouteModel] = Field(alias="IpRoutes")
    update_security_group_for_directory_controllers: Optional[bool] = Field(
        default=None, alias="UpdateSecurityGroupForDirectoryControllers"
    )


class AddRegionRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    region_name: str = Field(alias="RegionName")
    vp_csettings: DirectoryVpcSettingsModel = Field(alias="VPCSettings")


class RegionDescriptionModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    region_type: Optional[Literal["Additional", "Primary"]] = Field(
        default=None, alias="RegionType"
    )
    status: Optional[
        Literal[
            "Active",
            "Created",
            "Creating",
            "Deleted",
            "Deleting",
            "Failed",
            "Impaired",
            "Inoperable",
            "Requested",
            "RestoreFailed",
            "Restoring",
        ]
    ] = Field(default=None, alias="Status")
    vpc_settings: Optional[DirectoryVpcSettingsModel] = Field(
        default=None, alias="VpcSettings"
    )
    desired_number_of_domain_controllers: Optional[int] = Field(
        default=None, alias="DesiredNumberOfDomainControllers"
    )
    launch_time: Optional[datetime] = Field(default=None, alias="LaunchTime")
    status_last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="StatusLastUpdatedDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )


class AddTagsToResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateDirectoryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    password: str = Field(alias="Password")
    size: Literal["Large", "Small"] = Field(alias="Size")
    short_name: Optional[str] = Field(default=None, alias="ShortName")
    description: Optional[str] = Field(default=None, alias="Description")
    vpc_settings: Optional[DirectoryVpcSettingsModel] = Field(
        default=None, alias="VpcSettings"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateMicrosoftADRequestModel(BaseModel):
    name: str = Field(alias="Name")
    password: str = Field(alias="Password")
    vpc_settings: DirectoryVpcSettingsModel = Field(alias="VpcSettings")
    short_name: Optional[str] = Field(default=None, alias="ShortName")
    description: Optional[str] = Field(default=None, alias="Description")
    edition: Optional[Literal["Enterprise", "Standard"]] = Field(
        default=None, alias="Edition"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResultModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComputerModel(BaseModel):
    computer_id: Optional[str] = Field(default=None, alias="ComputerId")
    computer_name: Optional[str] = Field(default=None, alias="ComputerName")
    computer_attributes: Optional[List[AttributeModel]] = Field(
        default=None, alias="ComputerAttributes"
    )


class CreateComputerRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    computer_name: str = Field(alias="ComputerName")
    password: str = Field(alias="Password")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="OrganizationalUnitDistinguishedName"
    )
    computer_attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="ComputerAttributes"
    )


class ListCertificatesResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    certificates_info: List[CertificateInfoModel] = Field(alias="CertificatesInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CertificateModel(BaseModel):
    certificate_id: Optional[str] = Field(default=None, alias="CertificateId")
    state: Optional[
        Literal[
            "DeregisterFailed",
            "Deregistered",
            "Deregistering",
            "RegisterFailed",
            "Registered",
            "Registering",
        ]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    common_name: Optional[str] = Field(default=None, alias="CommonName")
    registered_date_time: Optional[datetime] = Field(
        default=None, alias="RegisteredDateTime"
    )
    expiry_date_time: Optional[datetime] = Field(default=None, alias="ExpiryDateTime")
    type: Optional[Literal["ClientCertAuth", "ClientLDAPS"]] = Field(
        default=None, alias="Type"
    )
    client_cert_auth_settings: Optional[ClientCertAuthSettingsModel] = Field(
        default=None, alias="ClientCertAuthSettings"
    )


class RegisterCertificateRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    certificate_data: str = Field(alias="CertificateData")
    type: Optional[Literal["ClientCertAuth", "ClientLDAPS"]] = Field(
        default=None, alias="Type"
    )
    client_cert_auth_settings: Optional[ClientCertAuthSettingsModel] = Field(
        default=None, alias="ClientCertAuthSettings"
    )


class DescribeClientAuthenticationSettingsResultModel(BaseModel):
    client_authentication_settings_info: List[
        ClientAuthenticationSettingInfoModel
    ] = Field(alias="ClientAuthenticationSettingsInfo")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConditionalForwardersResultModel(BaseModel):
    conditional_forwarders: List[ConditionalForwarderModel] = Field(
        alias="ConditionalForwarders"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectDirectoryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    password: str = Field(alias="Password")
    size: Literal["Large", "Small"] = Field(alias="Size")
    connect_settings: DirectoryConnectSettingsModel = Field(alias="ConnectSettings")
    short_name: Optional[str] = Field(default=None, alias="ShortName")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateModel(
    BaseModel
):
    directory_id: str = Field(alias="DirectoryId")
    type: Optional[Literal["SmartCard", "SmartCardOrPassword"]] = Field(
        default=None, alias="Type"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDirectoriesRequestDescribeDirectoriesPaginateModel(BaseModel):
    directory_ids: Optional[Sequence[str]] = Field(default=None, alias="DirectoryIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDomainControllersRequestDescribeDomainControllersPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    domain_controller_ids: Optional[Sequence[str]] = Field(
        default=None, alias="DomainControllerIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    type: Optional[Literal["Client"]] = Field(default=None, alias="Type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRegionsRequestDescribeRegionsPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateModel(BaseModel):
    owner_directory_id: str = Field(alias="OwnerDirectoryId")
    shared_directory_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SharedDirectoryIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotsRequestDescribeSnapshotsPaginateModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    snapshot_ids: Optional[Sequence[str]] = Field(default=None, alias="SnapshotIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTrustsRequestDescribeTrustsPaginateModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    trust_ids: Optional[Sequence[str]] = Field(default=None, alias="TrustIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    update_type: Literal["OS"] = Field(alias="UpdateType")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCertificatesRequestListCertificatesPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIpRoutesRequestListIpRoutesPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLogSubscriptionsRequestListLogSubscriptionsPaginateModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemaExtensionsRequestListSchemaExtensionsPaginateModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDomainControllersResultModel(BaseModel):
    domain_controllers: List[DomainControllerModel] = Field(alias="DomainControllers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventTopicsResultModel(BaseModel):
    event_topics: List[EventTopicModel] = Field(alias="EventTopics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLDAPSSettingsResultModel(BaseModel):
    l_dap_s_settings_info: List[LDAPSSettingInfoModel] = Field(
        alias="LDAPSSettingsInfo"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSettingsResultModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    setting_entries: List[SettingEntryModel] = Field(alias="SettingEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotsResultModel(BaseModel):
    snapshots: List[SnapshotModel] = Field(alias="Snapshots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrustsResultModel(BaseModel):
    trusts: List[TrustModel] = Field(alias="Trusts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableRadiusRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    radius_settings: RadiusSettingsModel = Field(alias="RadiusSettings")


class OwnerDirectoryDescriptionModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    dns_ip_addrs: Optional[List[str]] = Field(default=None, alias="DnsIpAddrs")
    vpc_settings: Optional[DirectoryVpcSettingsDescriptionModel] = Field(
        default=None, alias="VpcSettings"
    )
    radius_settings: Optional[RadiusSettingsModel] = Field(
        default=None, alias="RadiusSettings"
    )
    radius_status: Optional[Literal["Completed", "Creating", "Failed"]] = Field(
        default=None, alias="RadiusStatus"
    )


class UpdateRadiusRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    radius_settings: RadiusSettingsModel = Field(alias="RadiusSettings")


class GetDirectoryLimitsResultModel(BaseModel):
    directory_limits: DirectoryLimitsModel = Field(alias="DirectoryLimits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnapshotLimitsResultModel(BaseModel):
    snapshot_limits: SnapshotLimitsModel = Field(alias="SnapshotLimits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIpRoutesResultModel(BaseModel):
    ip_routes_info: List[IpRouteInfoModel] = Field(alias="IpRoutesInfo")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLogSubscriptionsResultModel(BaseModel):
    log_subscriptions: List[LogSubscriptionModel] = Field(alias="LogSubscriptions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemaExtensionsResultModel(BaseModel):
    schema_extensions_info: List[SchemaExtensionInfoModel] = Field(
        alias="SchemaExtensionsInfo"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDirectorySetupRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    update_type: Literal["OS"] = Field(alias="UpdateType")
    os_update_settings: Optional[OSUpdateSettingsModel] = Field(
        default=None, alias="OSUpdateSettings"
    )
    create_snapshot_before_update: Optional[bool] = Field(
        default=None, alias="CreateSnapshotBeforeUpdate"
    )


class UpdateValueModel(BaseModel):
    os_update_settings: Optional[OSUpdateSettingsModel] = Field(
        default=None, alias="OSUpdateSettings"
    )


class UpdateSettingsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    settings: Sequence[SettingModel] = Field(alias="Settings")


class ShareDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    share_target: ShareTargetModel = Field(alias="ShareTarget")
    share_method: Literal["HANDSHAKE", "ORGANIZATIONS"] = Field(alias="ShareMethod")
    share_notes: Optional[str] = Field(default=None, alias="ShareNotes")


class UnshareDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    unshare_target: UnshareTargetModel = Field(alias="UnshareTarget")


class DescribeRegionsResultModel(BaseModel):
    regions_description: List[RegionDescriptionModel] = Field(
        alias="RegionsDescription"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateComputerResultModel(BaseModel):
    computer: ComputerModel = Field(alias="Computer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCertificateResultModel(BaseModel):
    certificate: CertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DirectoryDescriptionModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    name: Optional[str] = Field(default=None, alias="Name")
    short_name: Optional[str] = Field(default=None, alias="ShortName")
    size: Optional[Literal["Large", "Small"]] = Field(default=None, alias="Size")
    edition: Optional[Literal["Enterprise", "Standard"]] = Field(
        default=None, alias="Edition"
    )
    alias: Optional[str] = Field(default=None, alias="Alias")
    access_url: Optional[str] = Field(default=None, alias="AccessUrl")
    description: Optional[str] = Field(default=None, alias="Description")
    dns_ip_addrs: Optional[List[str]] = Field(default=None, alias="DnsIpAddrs")
    stage: Optional[
        Literal[
            "Active",
            "Created",
            "Creating",
            "Deleted",
            "Deleting",
            "Failed",
            "Impaired",
            "Inoperable",
            "Requested",
            "RestoreFailed",
            "Restoring",
        ]
    ] = Field(default=None, alias="Stage")
    share_status: Optional[
        Literal[
            "Deleted",
            "Deleting",
            "PendingAcceptance",
            "RejectFailed",
            "Rejected",
            "Rejecting",
            "ShareFailed",
            "Shared",
            "Sharing",
        ]
    ] = Field(default=None, alias="ShareStatus")
    share_method: Optional[Literal["HANDSHAKE", "ORGANIZATIONS"]] = Field(
        default=None, alias="ShareMethod"
    )
    share_notes: Optional[str] = Field(default=None, alias="ShareNotes")
    launch_time: Optional[datetime] = Field(default=None, alias="LaunchTime")
    stage_last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="StageLastUpdatedDateTime"
    )
    type: Optional[
        Literal["ADConnector", "MicrosoftAD", "SharedMicrosoftAD", "SimpleAD"]
    ] = Field(default=None, alias="Type")
    vpc_settings: Optional[DirectoryVpcSettingsDescriptionModel] = Field(
        default=None, alias="VpcSettings"
    )
    connect_settings: Optional[DirectoryConnectSettingsDescriptionModel] = Field(
        default=None, alias="ConnectSettings"
    )
    radius_settings: Optional[RadiusSettingsModel] = Field(
        default=None, alias="RadiusSettings"
    )
    radius_status: Optional[Literal["Completed", "Creating", "Failed"]] = Field(
        default=None, alias="RadiusStatus"
    )
    stage_reason: Optional[str] = Field(default=None, alias="StageReason")
    sso_enabled: Optional[bool] = Field(default=None, alias="SsoEnabled")
    desired_number_of_domain_controllers: Optional[int] = Field(
        default=None, alias="DesiredNumberOfDomainControllers"
    )
    owner_directory_description: Optional[OwnerDirectoryDescriptionModel] = Field(
        default=None, alias="OwnerDirectoryDescription"
    )
    regions_info: Optional[RegionsInfoModel] = Field(default=None, alias="RegionsInfo")
    os_version: Optional[Literal["SERVER_2012", "SERVER_2019"]] = Field(
        default=None, alias="OsVersion"
    )


class UpdateInfoEntryModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    status: Optional[Literal["UpdateFailed", "Updated", "Updating"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    initiated_by: Optional[str] = Field(default=None, alias="InitiatedBy")
    new_value: Optional[UpdateValueModel] = Field(default=None, alias="NewValue")
    previous_value: Optional[UpdateValueModel] = Field(
        default=None, alias="PreviousValue"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdatedDateTime"
    )


class DescribeDirectoriesResultModel(BaseModel):
    directory_descriptions: List[DirectoryDescriptionModel] = Field(
        alias="DirectoryDescriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUpdateDirectoryResultModel(BaseModel):
    update_activities: List[UpdateInfoEntryModel] = Field(alias="UpdateActivities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
