# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessControlRuleModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    effect: Optional[Literal["ALLOW", "DENY"]] = Field(default=None, alias="Effect")
    description: Optional[str] = Field(default=None, alias="Description")
    ip_ranges: Optional[List[str]] = Field(default=None, alias="IpRanges")
    not_ip_ranges: Optional[List[str]] = Field(default=None, alias="NotIpRanges")
    actions: Optional[List[str]] = Field(default=None, alias="Actions")
    not_actions: Optional[List[str]] = Field(default=None, alias="NotActions")
    user_ids: Optional[List[str]] = Field(default=None, alias="UserIds")
    not_user_ids: Optional[List[str]] = Field(default=None, alias="NotUserIds")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")
    impersonation_role_ids: Optional[List[str]] = Field(
        default=None, alias="ImpersonationRoleIds"
    )
    not_impersonation_role_ids: Optional[List[str]] = Field(
        default=None, alias="NotImpersonationRoleIds"
    )


class AssociateDelegateToResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")
    entity_id: str = Field(alias="EntityId")


class AssociateMemberToGroupRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")
    member_id: str = Field(alias="MemberId")


class AssumeImpersonationRoleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class LambdaAvailabilityProviderModel(BaseModel):
    lambda_arn: str = Field(alias="LambdaArn")


class RedactedEwsAvailabilityProviderModel(BaseModel):
    ews_endpoint: Optional[str] = Field(default=None, alias="EwsEndpoint")
    ews_username: Optional[str] = Field(default=None, alias="EwsUsername")


class BookingOptionsModel(BaseModel):
    auto_accept_requests: Optional[bool] = Field(
        default=None, alias="AutoAcceptRequests"
    )
    auto_decline_recurring_requests: Optional[bool] = Field(
        default=None, alias="AutoDeclineRecurringRequests"
    )
    auto_decline_conflicting_requests: Optional[bool] = Field(
        default=None, alias="AutoDeclineConflictingRequests"
    )


class CancelMailboxExportJobRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    job_id: str = Field(alias="JobId")
    organization_id: str = Field(alias="OrganizationId")


class CreateAliasRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    alias: str = Field(alias="Alias")


class EwsAvailabilityProviderModel(BaseModel):
    ews_endpoint: str = Field(alias="EwsEndpoint")
    ews_username: str = Field(alias="EwsUsername")
    ews_password: str = Field(alias="EwsPassword")


class CreateGroupRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")


class ImpersonationRuleModel(BaseModel):
    impersonation_rule_id: str = Field(alias="ImpersonationRuleId")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    target_users: Optional[Sequence[str]] = Field(default=None, alias="TargetUsers")
    not_target_users: Optional[Sequence[str]] = Field(
        default=None, alias="NotTargetUsers"
    )


class CreateMobileDeviceAccessRuleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    device_types: Optional[Sequence[str]] = Field(default=None, alias="DeviceTypes")
    not_device_types: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceTypes"
    )
    device_models: Optional[Sequence[str]] = Field(default=None, alias="DeviceModels")
    not_device_models: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceModels"
    )
    device_operating_systems: Optional[Sequence[str]] = Field(
        default=None, alias="DeviceOperatingSystems"
    )
    not_device_operating_systems: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceOperatingSystems"
    )
    device_user_agents: Optional[Sequence[str]] = Field(
        default=None, alias="DeviceUserAgents"
    )
    not_device_user_agents: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceUserAgents"
    )


class DomainModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")


class CreateResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")
    type: Literal["EQUIPMENT", "ROOM"] = Field(alias="Type")


class CreateUserRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")
    display_name: str = Field(alias="DisplayName")
    password: str = Field(alias="Password")


class DelegateModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal["GROUP", "USER"] = Field(alias="Type")


class DeleteAccessControlRuleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")


class DeleteAliasRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    alias: str = Field(alias="Alias")


class DeleteAvailabilityConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")


class DeleteEmailMonitoringConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class DeleteGroupRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")


class DeleteImpersonationRoleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")


class DeleteMailboxPermissionsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    grantee_id: str = Field(alias="GranteeId")


class DeleteMobileDeviceAccessOverrideRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")
    device_id: str = Field(alias="DeviceId")


class DeleteMobileDeviceAccessRuleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    mobile_device_access_rule_id: str = Field(alias="MobileDeviceAccessRuleId")


class DeleteOrganizationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    delete_directory: bool = Field(alias="DeleteDirectory")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")


class DeleteRetentionPolicyRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    id: str = Field(alias="Id")


class DeleteUserRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")


class DeregisterFromWorkMailRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")


class DeregisterMailDomainRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")


class DescribeEmailMonitoringConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class DescribeGroupRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")


class DescribeInboundDmarcSettingsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class DescribeMailboxExportJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    organization_id: str = Field(alias="OrganizationId")


class DescribeOrganizationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class DescribeResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")


class DescribeUserRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")


class DisassociateDelegateFromResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")
    entity_id: str = Field(alias="EntityId")


class DisassociateMemberFromGroupRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")
    member_id: str = Field(alias="MemberId")


class DnsRecordModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    value: Optional[str] = Field(default=None, alias="Value")


class FolderConfigurationModel(BaseModel):
    name: Literal[
        "DELETED_ITEMS", "DRAFTS", "INBOX", "JUNK_EMAIL", "SENT_ITEMS"
    ] = Field(alias="Name")
    action: Literal["DELETE", "NONE", "PERMANENTLY_DELETE"] = Field(alias="Action")
    period: Optional[int] = Field(default=None, alias="Period")


class GetAccessControlEffectRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    ip_address: str = Field(alias="IpAddress")
    action: str = Field(alias="Action")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    impersonation_role_id: Optional[str] = Field(
        default=None, alias="ImpersonationRoleId"
    )


class GetDefaultRetentionPolicyRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class GetImpersonationRoleEffectRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")
    target_user: str = Field(alias="TargetUser")


class ImpersonationMatchedRuleModel(BaseModel):
    impersonation_rule_id: Optional[str] = Field(
        default=None, alias="ImpersonationRuleId"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class GetImpersonationRoleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")


class GetMailDomainRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")


class GetMailboxDetailsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")


class GetMobileDeviceAccessEffectRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    device_model: Optional[str] = Field(default=None, alias="DeviceModel")
    device_operating_system: Optional[str] = Field(
        default=None, alias="DeviceOperatingSystem"
    )
    device_user_agent: Optional[str] = Field(default=None, alias="DeviceUserAgent")


class MobileDeviceAccessMatchedRuleModel(BaseModel):
    mobile_device_access_rule_id: Optional[str] = Field(
        default=None, alias="MobileDeviceAccessRuleId"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class GetMobileDeviceAccessOverrideRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")
    device_id: str = Field(alias="DeviceId")


class GroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    email: Optional[str] = Field(default=None, alias="Email")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="State"
    )
    enabled_date: Optional[datetime] = Field(default=None, alias="EnabledDate")
    disabled_date: Optional[datetime] = Field(default=None, alias="DisabledDate")


class ImpersonationRoleModel(BaseModel):
    impersonation_role_id: Optional[str] = Field(
        default=None, alias="ImpersonationRoleId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["FULL_ACCESS", "READ_ONLY"]] = Field(
        default=None, alias="Type"
    )
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")


class ListAccessControlRulesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAliasesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAvailabilityConfigurationsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGroupMembersRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MemberModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["GROUP", "USER"]] = Field(default=None, alias="Type")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="State"
    )
    enabled_date: Optional[datetime] = Field(default=None, alias="EnabledDate")
    disabled_date: Optional[datetime] = Field(default=None, alias="DisabledDate")


class ListGroupsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListImpersonationRolesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMailDomainsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MailDomainSummaryModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    default_domain: Optional[bool] = Field(default=None, alias="DefaultDomain")


class ListMailboxExportJobsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MailboxExportJobModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    description: Optional[str] = Field(default=None, alias="Description")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_path: Optional[str] = Field(default=None, alias="S3Path")
    estimated_progress: Optional[int] = Field(default=None, alias="EstimatedProgress")
    state: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "RUNNING"]] = Field(
        default=None, alias="State"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class ListMailboxPermissionsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PermissionModel(BaseModel):
    grantee_id: str = Field(alias="GranteeId")
    grantee_type: Literal["GROUP", "USER"] = Field(alias="GranteeType")
    permission_values: List[
        Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]
    ] = Field(alias="PermissionValues")


class ListMobileDeviceAccessOverridesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MobileDeviceAccessOverrideModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="UserId")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    effect: Optional[Literal["ALLOW", "DENY"]] = Field(default=None, alias="Effect")
    description: Optional[str] = Field(default=None, alias="Description")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")


class ListMobileDeviceAccessRulesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")


class MobileDeviceAccessRuleModel(BaseModel):
    mobile_device_access_rule_id: Optional[str] = Field(
        default=None, alias="MobileDeviceAccessRuleId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    effect: Optional[Literal["ALLOW", "DENY"]] = Field(default=None, alias="Effect")
    device_types: Optional[List[str]] = Field(default=None, alias="DeviceTypes")
    not_device_types: Optional[List[str]] = Field(default=None, alias="NotDeviceTypes")
    device_models: Optional[List[str]] = Field(default=None, alias="DeviceModels")
    not_device_models: Optional[List[str]] = Field(
        default=None, alias="NotDeviceModels"
    )
    device_operating_systems: Optional[List[str]] = Field(
        default=None, alias="DeviceOperatingSystems"
    )
    not_device_operating_systems: Optional[List[str]] = Field(
        default=None, alias="NotDeviceOperatingSystems"
    )
    device_user_agents: Optional[List[str]] = Field(
        default=None, alias="DeviceUserAgents"
    )
    not_device_user_agents: Optional[List[str]] = Field(
        default=None, alias="NotDeviceUserAgents"
    )
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")


class ListOrganizationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OrganizationSummaryModel(BaseModel):
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    alias: Optional[str] = Field(default=None, alias="Alias")
    default_mail_domain: Optional[str] = Field(default=None, alias="DefaultMailDomain")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    state: Optional[str] = Field(default=None, alias="State")


class ListResourceDelegatesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListResourcesRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResourceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    email: Optional[str] = Field(default=None, alias="Email")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["EQUIPMENT", "ROOM"]] = Field(default=None, alias="Type")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="State"
    )
    enabled_date: Optional[datetime] = Field(default=None, alias="EnabledDate")
    disabled_date: Optional[datetime] = Field(default=None, alias="DisabledDate")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ListUsersRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class UserModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    email: Optional[str] = Field(default=None, alias="Email")
    name: Optional[str] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="State"
    )
    user_role: Optional[Literal["RESOURCE", "SYSTEM_USER", "USER"]] = Field(
        default=None, alias="UserRole"
    )
    enabled_date: Optional[datetime] = Field(default=None, alias="EnabledDate")
    disabled_date: Optional[datetime] = Field(default=None, alias="DisabledDate")


class PutAccessControlRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    description: str = Field(alias="Description")
    organization_id: str = Field(alias="OrganizationId")
    ip_ranges: Optional[Sequence[str]] = Field(default=None, alias="IpRanges")
    not_ip_ranges: Optional[Sequence[str]] = Field(default=None, alias="NotIpRanges")
    actions: Optional[Sequence[str]] = Field(default=None, alias="Actions")
    not_actions: Optional[Sequence[str]] = Field(default=None, alias="NotActions")
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="UserIds")
    not_user_ids: Optional[Sequence[str]] = Field(default=None, alias="NotUserIds")
    impersonation_role_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ImpersonationRoleIds"
    )
    not_impersonation_role_ids: Optional[Sequence[str]] = Field(
        default=None, alias="NotImpersonationRoleIds"
    )


class PutEmailMonitoringConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    role_arn: str = Field(alias="RoleArn")
    log_group_arn: str = Field(alias="LogGroupArn")


class PutInboundDmarcSettingsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    enforced: bool = Field(alias="Enforced")


class PutMailboxPermissionsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    grantee_id: str = Field(alias="GranteeId")
    permission_values: Sequence[
        Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]
    ] = Field(alias="PermissionValues")


class PutMobileDeviceAccessOverrideRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")
    device_id: str = Field(alias="DeviceId")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    description: Optional[str] = Field(default=None, alias="Description")


class RegisterMailDomainRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class RegisterToWorkMailRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    email: str = Field(alias="Email")


class ResetPasswordRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")
    password: str = Field(alias="Password")


class StartMailboxExportJobRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    role_arn: str = Field(alias="RoleArn")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_prefix: str = Field(alias="S3Prefix")
    description: Optional[str] = Field(default=None, alias="Description")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDefaultMailDomainRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")


class UpdateMailboxQuotaRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    user_id: str = Field(alias="UserId")
    mailbox_quota: int = Field(alias="MailboxQuota")


class UpdateMobileDeviceAccessRuleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    mobile_device_access_rule_id: str = Field(alias="MobileDeviceAccessRuleId")
    name: str = Field(alias="Name")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    description: Optional[str] = Field(default=None, alias="Description")
    device_types: Optional[Sequence[str]] = Field(default=None, alias="DeviceTypes")
    not_device_types: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceTypes"
    )
    device_models: Optional[Sequence[str]] = Field(default=None, alias="DeviceModels")
    not_device_models: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceModels"
    )
    device_operating_systems: Optional[Sequence[str]] = Field(
        default=None, alias="DeviceOperatingSystems"
    )
    not_device_operating_systems: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceOperatingSystems"
    )
    device_user_agents: Optional[Sequence[str]] = Field(
        default=None, alias="DeviceUserAgents"
    )
    not_device_user_agents: Optional[Sequence[str]] = Field(
        default=None, alias="NotDeviceUserAgents"
    )


class UpdatePrimaryEmailAddressRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    email: str = Field(alias="Email")


class AssumeImpersonationRoleResponseModel(BaseModel):
    token: str = Field(alias="Token")
    expires_in: int = Field(alias="ExpiresIn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImpersonationRoleResponseModel(BaseModel):
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMobileDeviceAccessRuleResponseModel(BaseModel):
    mobile_device_access_rule_id: str = Field(alias="MobileDeviceAccessRuleId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOrganizationResponseModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceResponseModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteOrganizationResponseModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    state: str = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEmailMonitoringConfigurationResponseModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    log_group_arn: str = Field(alias="LogGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupResponseModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    name: str = Field(alias="Name")
    email: str = Field(alias="Email")
    state: Literal["DELETED", "DISABLED", "ENABLED"] = Field(alias="State")
    enabled_date: datetime = Field(alias="EnabledDate")
    disabled_date: datetime = Field(alias="DisabledDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInboundDmarcSettingsResponseModel(BaseModel):
    enforced: bool = Field(alias="Enforced")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMailboxExportJobResponseModel(BaseModel):
    entity_id: str = Field(alias="EntityId")
    description: str = Field(alias="Description")
    role_arn: str = Field(alias="RoleArn")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_prefix: str = Field(alias="S3Prefix")
    s3_path: str = Field(alias="S3Path")
    estimated_progress: int = Field(alias="EstimatedProgress")
    state: Literal["CANCELLED", "COMPLETED", "FAILED", "RUNNING"] = Field(alias="State")
    error_info: str = Field(alias="ErrorInfo")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationResponseModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    alias: str = Field(alias="Alias")
    state: str = Field(alias="State")
    directory_id: str = Field(alias="DirectoryId")
    directory_type: str = Field(alias="DirectoryType")
    default_mail_domain: str = Field(alias="DefaultMailDomain")
    completed_date: datetime = Field(alias="CompletedDate")
    error_message: str = Field(alias="ErrorMessage")
    arn: str = Field(alias="ARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    name: str = Field(alias="Name")
    email: str = Field(alias="Email")
    display_name: str = Field(alias="DisplayName")
    state: Literal["DELETED", "DISABLED", "ENABLED"] = Field(alias="State")
    user_role: Literal["RESOURCE", "SYSTEM_USER", "USER"] = Field(alias="UserRole")
    enabled_date: datetime = Field(alias="EnabledDate")
    disabled_date: datetime = Field(alias="DisabledDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessControlEffectResponseModel(BaseModel):
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    matched_rules: List[str] = Field(alias="MatchedRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMailboxDetailsResponseModel(BaseModel):
    mailbox_quota: int = Field(alias="MailboxQuota")
    mailbox_size: float = Field(alias="MailboxSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMobileDeviceAccessOverrideResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    device_id: str = Field(alias="DeviceId")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    description: str = Field(alias="Description")
    date_created: datetime = Field(alias="DateCreated")
    date_modified: datetime = Field(alias="DateModified")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessControlRulesResponseModel(BaseModel):
    rules: List[AccessControlRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesResponseModel(BaseModel):
    aliases: List[str] = Field(alias="Aliases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMailboxExportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestAvailabilityConfigurationResponseModel(BaseModel):
    test_passed: bool = Field(alias="TestPassed")
    failure_reason: str = Field(alias="FailureReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AvailabilityConfigurationModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    provider_type: Optional[Literal["EWS", "LAMBDA"]] = Field(
        default=None, alias="ProviderType"
    )
    ews_provider: Optional[RedactedEwsAvailabilityProviderModel] = Field(
        default=None, alias="EwsProvider"
    )
    lambda_provider: Optional[LambdaAvailabilityProviderModel] = Field(
        default=None, alias="LambdaProvider"
    )
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")


class DescribeResourceResponseModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    email: str = Field(alias="Email")
    name: str = Field(alias="Name")
    type: Literal["EQUIPMENT", "ROOM"] = Field(alias="Type")
    booking_options: BookingOptionsModel = Field(alias="BookingOptions")
    state: Literal["DELETED", "DISABLED", "ENABLED"] = Field(alias="State")
    enabled_date: datetime = Field(alias="EnabledDate")
    disabled_date: datetime = Field(alias="DisabledDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")
    name: Optional[str] = Field(default=None, alias="Name")
    booking_options: Optional[BookingOptionsModel] = Field(
        default=None, alias="BookingOptions"
    )


class CreateAvailabilityConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    ews_provider: Optional[EwsAvailabilityProviderModel] = Field(
        default=None, alias="EwsProvider"
    )
    lambda_provider: Optional[LambdaAvailabilityProviderModel] = Field(
        default=None, alias="LambdaProvider"
    )


class TestAvailabilityConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    ews_provider: Optional[EwsAvailabilityProviderModel] = Field(
        default=None, alias="EwsProvider"
    )
    lambda_provider: Optional[LambdaAvailabilityProviderModel] = Field(
        default=None, alias="LambdaProvider"
    )


class UpdateAvailabilityConfigurationRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    domain_name: str = Field(alias="DomainName")
    ews_provider: Optional[EwsAvailabilityProviderModel] = Field(
        default=None, alias="EwsProvider"
    )
    lambda_provider: Optional[LambdaAvailabilityProviderModel] = Field(
        default=None, alias="LambdaProvider"
    )


class CreateImpersonationRoleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")
    type: Literal["FULL_ACCESS", "READ_ONLY"] = Field(alias="Type")
    rules: Sequence[ImpersonationRuleModel] = Field(alias="Rules")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")


class GetImpersonationRoleResponseModel(BaseModel):
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")
    name: str = Field(alias="Name")
    type: Literal["FULL_ACCESS", "READ_ONLY"] = Field(alias="Type")
    description: str = Field(alias="Description")
    rules: List[ImpersonationRuleModel] = Field(alias="Rules")
    date_created: datetime = Field(alias="DateCreated")
    date_modified: datetime = Field(alias="DateModified")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateImpersonationRoleRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    impersonation_role_id: str = Field(alias="ImpersonationRoleId")
    name: str = Field(alias="Name")
    type: Literal["FULL_ACCESS", "READ_ONLY"] = Field(alias="Type")
    rules: Sequence[ImpersonationRuleModel] = Field(alias="Rules")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateOrganizationRequestModel(BaseModel):
    alias: str = Field(alias="Alias")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    domains: Optional[Sequence[DomainModel]] = Field(default=None, alias="Domains")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    enable_interoperability: Optional[bool] = Field(
        default=None, alias="EnableInteroperability"
    )


class ListResourceDelegatesResponseModel(BaseModel):
    delegates: List[DelegateModel] = Field(alias="Delegates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMailDomainResponseModel(BaseModel):
    records: List[DnsRecordModel] = Field(alias="Records")
    is_test_domain: bool = Field(alias="IsTestDomain")
    is_default: bool = Field(alias="IsDefault")
    ownership_verification_status: Literal["FAILED", "PENDING", "VERIFIED"] = Field(
        alias="OwnershipVerificationStatus"
    )
    dkim_verification_status: Literal["FAILED", "PENDING", "VERIFIED"] = Field(
        alias="DkimVerificationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDefaultRetentionPolicyResponseModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    folder_configurations: List[FolderConfigurationModel] = Field(
        alias="FolderConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRetentionPolicyRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    name: str = Field(alias="Name")
    folder_configurations: Sequence[FolderConfigurationModel] = Field(
        alias="FolderConfigurations"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")


class GetImpersonationRoleEffectResponseModel(BaseModel):
    type: Literal["FULL_ACCESS", "READ_ONLY"] = Field(alias="Type")
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    matched_rules: List[ImpersonationMatchedRuleModel] = Field(alias="MatchedRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMobileDeviceAccessEffectResponseModel(BaseModel):
    effect: Literal["ALLOW", "DENY"] = Field(alias="Effect")
    matched_rules: List[MobileDeviceAccessMatchedRuleModel] = Field(
        alias="MatchedRules"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImpersonationRolesResponseModel(BaseModel):
    roles: List[ImpersonationRoleModel] = Field(alias="Roles")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesRequestListAliasesPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateModel(
    BaseModel
):
    organization_id: str = Field(alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupMembersRequestListGroupMembersPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    group_id: str = Field(alias="GroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsRequestListGroupsPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMailboxPermissionsRequestListMailboxPermissionsPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    entity_id: str = Field(alias="EntityId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationsRequestListOrganizationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceDelegatesRequestListResourceDelegatesPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    resource_id: str = Field(alias="ResourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcesRequestListResourcesPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="Members")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMailDomainsResponseModel(BaseModel):
    mail_domains: List[MailDomainSummaryModel] = Field(alias="MailDomains")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMailboxExportJobsResponseModel(BaseModel):
    jobs: List[MailboxExportJobModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMailboxPermissionsResponseModel(BaseModel):
    permissions: List[PermissionModel] = Field(alias="Permissions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMobileDeviceAccessOverridesResponseModel(BaseModel):
    overrides: List[MobileDeviceAccessOverrideModel] = Field(alias="Overrides")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMobileDeviceAccessRulesResponseModel(BaseModel):
    rules: List[MobileDeviceAccessRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationsResponseModel(BaseModel):
    organization_summaries: List[OrganizationSummaryModel] = Field(
        alias="OrganizationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesResponseModel(BaseModel):
    resources: List[ResourceModel] = Field(alias="Resources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailabilityConfigurationsResponseModel(BaseModel):
    availability_configurations: List[AvailabilityConfigurationModel] = Field(
        alias="AvailabilityConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
