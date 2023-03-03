# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessDetailModel(BaseModel):
    service_name: str = Field(alias="ServiceName")
    service_namespace: str = Field(alias="ServiceNamespace")
    region: Optional[str] = Field(default=None, alias="Region")
    entity_path: Optional[str] = Field(default=None, alias="EntityPath")
    last_authenticated_time: Optional[datetime] = Field(
        default=None, alias="LastAuthenticatedTime"
    )
    total_authenticated_entities: Optional[int] = Field(
        default=None, alias="TotalAuthenticatedEntities"
    )


class AccessKeyLastUsedModel(BaseModel):
    last_used_date: datetime = Field(alias="LastUsedDate")
    service_name: str = Field(alias="ServiceName")
    region: str = Field(alias="Region")


class AccessKeyMetadataModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class AccessKeyModel(BaseModel):
    user_name: str = Field(alias="UserName")
    access_key_id: str = Field(alias="AccessKeyId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    secret_access_key: str = Field(alias="SecretAccessKey")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class AddClientIDToOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    client_id: str = Field(alias="ClientID")


class AddRoleToInstanceProfileRequestInstanceProfileAddRoleModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class AddRoleToInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    role_name: str = Field(alias="RoleName")


class AddUserToGroupRequestGroupAddUserModel(BaseModel):
    user_name: str = Field(alias="UserName")


class AddUserToGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_name: str = Field(alias="UserName")


class AddUserToGroupRequestUserAddGroupModel(BaseModel):
    group_name: str = Field(alias="GroupName")


class AttachGroupPolicyRequestGroupAttachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class AttachGroupPolicyRequestPolicyAttachGroupModel(BaseModel):
    group_name: str = Field(alias="GroupName")


class AttachGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_arn: str = Field(alias="PolicyArn")


class AttachRolePolicyRequestPolicyAttachRoleModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class AttachRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_arn: str = Field(alias="PolicyArn")


class AttachRolePolicyRequestRoleAttachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class AttachUserPolicyRequestPolicyAttachUserModel(BaseModel):
    user_name: str = Field(alias="UserName")


class AttachUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_arn: str = Field(alias="PolicyArn")


class AttachUserPolicyRequestUserAttachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AttachedPermissionsBoundaryModel(BaseModel):
    permissions_boundary_type: Optional[Literal["PermissionsBoundaryPolicy"]] = Field(
        default=None, alias="PermissionsBoundaryType"
    )
    permissions_boundary_arn: Optional[str] = Field(
        default=None, alias="PermissionsBoundaryArn"
    )


class AttachedPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")


class ChangePasswordRequestModel(BaseModel):
    old_password: str = Field(alias="OldPassword")
    new_password: str = Field(alias="NewPassword")


class ChangePasswordRequestServiceResourceChangePasswordModel(BaseModel):
    old_password: str = Field(alias="OldPassword")
    new_password: str = Field(alias="NewPassword")


class ContextEntryModel(BaseModel):
    context_key_name: Optional[str] = Field(default=None, alias="ContextKeyName")
    context_key_values: Optional[Sequence[str]] = Field(
        default=None, alias="ContextKeyValues"
    )
    context_key_type: Optional[
        Literal[
            "binary",
            "binaryList",
            "boolean",
            "booleanList",
            "date",
            "dateList",
            "ip",
            "ipList",
            "numeric",
            "numericList",
            "string",
            "stringList",
        ]
    ] = Field(default=None, alias="ContextKeyType")


class CreateAccessKeyRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")


class CreateAccountAliasRequestModel(BaseModel):
    account_alias: str = Field(alias="AccountAlias")


class CreateAccountAliasRequestServiceResourceCreateAccountAliasModel(BaseModel):
    account_alias: str = Field(alias="AccountAlias")


class CreateGroupRequestGroupCreateModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")


class CreateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    path: Optional[str] = Field(default=None, alias="Path")


class CreateGroupRequestServiceResourceCreateGroupModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    path: Optional[str] = Field(default=None, alias="Path")


class GroupModel(BaseModel):
    path: str = Field(alias="Path")
    group_name: str = Field(alias="GroupName")
    group_id: str = Field(alias="GroupId")
    arn: str = Field(alias="Arn")
    create_date: datetime = Field(alias="CreateDate")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateLoginProfileRequestLoginProfileCreateModel(BaseModel):
    password: str = Field(alias="Password")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class CreateLoginProfileRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    password: str = Field(alias="Password")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class CreateLoginProfileRequestUserCreateLoginProfileModel(BaseModel):
    password: str = Field(alias="Password")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class LoginProfileModel(BaseModel):
    user_name: str = Field(alias="UserName")
    create_date: datetime = Field(alias="CreateDate")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class CreatePolicyVersionRequestPolicyCreateVersionModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")
    set_as_default: Optional[bool] = Field(default=None, alias="SetAsDefault")


class CreatePolicyVersionRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    policy_document: str = Field(alias="PolicyDocument")
    set_as_default: Optional[bool] = Field(default=None, alias="SetAsDefault")


class PolicyVersionModel(BaseModel):
    document: Optional[str] = Field(default=None, alias="Document")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    is_default_version: Optional[bool] = Field(default=None, alias="IsDefaultVersion")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class CreateServiceLinkedRoleRequestModel(BaseModel):
    aws_service_name: str = Field(alias="AWSServiceName")
    description: Optional[str] = Field(default=None, alias="Description")
    custom_suffix: Optional[str] = Field(default=None, alias="CustomSuffix")


class CreateServiceSpecificCredentialRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    service_name: str = Field(alias="ServiceName")


class ServiceSpecificCredentialModel(BaseModel):
    create_date: datetime = Field(alias="CreateDate")
    service_name: str = Field(alias="ServiceName")
    service_user_name: str = Field(alias="ServiceUserName")
    service_password: str = Field(alias="ServicePassword")
    service_specific_credential_id: str = Field(alias="ServiceSpecificCredentialId")
    user_name: str = Field(alias="UserName")
    status: Literal["Active", "Inactive"] = Field(alias="Status")


class DeactivateMFADeviceRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    serial_number: str = Field(alias="SerialNumber")


class DeleteAccessKeyRequestModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class DeleteAccountAliasRequestModel(BaseModel):
    account_alias: str = Field(alias="AccountAlias")


class DeleteGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_name: str = Field(alias="PolicyName")


class DeleteGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")


class DeleteInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")


class DeleteLoginProfileRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")


class DeleteOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")


class DeletePolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class DeletePolicyVersionRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    version_id: str = Field(alias="VersionId")


class DeleteRolePermissionsBoundaryRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class DeleteRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_name: str = Field(alias="PolicyName")


class DeleteRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class DeleteSAMLProviderRequestModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")


class DeleteSSHPublicKeyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_id: str = Field(alias="SSHPublicKeyId")


class DeleteServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")


class DeleteServiceLinkedRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class DeleteServiceSpecificCredentialRequestModel(BaseModel):
    service_specific_credential_id: str = Field(alias="ServiceSpecificCredentialId")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class DeleteSigningCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class DeleteUserPermissionsBoundaryRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")


class DeleteUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_name: str = Field(alias="PolicyName")


class DeleteUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")


class DeleteVirtualMFADeviceRequestModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")


class RoleUsageTypeModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    resources: Optional[List[str]] = Field(default=None, alias="Resources")


class DetachGroupPolicyRequestGroupDetachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class DetachGroupPolicyRequestPolicyDetachGroupModel(BaseModel):
    group_name: str = Field(alias="GroupName")


class DetachGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_arn: str = Field(alias="PolicyArn")


class DetachRolePolicyRequestPolicyDetachRoleModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class DetachRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_arn: str = Field(alias="PolicyArn")


class DetachRolePolicyRequestRoleDetachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class DetachUserPolicyRequestPolicyDetachUserModel(BaseModel):
    user_name: str = Field(alias="UserName")


class DetachUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_arn: str = Field(alias="PolicyArn")


class DetachUserPolicyRequestUserDetachPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class EnableMFADeviceRequestMfaDeviceAssociateModel(BaseModel):
    authentication_code1: str = Field(alias="AuthenticationCode1")
    authentication_code2: str = Field(alias="AuthenticationCode2")


class EnableMFADeviceRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    serial_number: str = Field(alias="SerialNumber")
    authentication_code1: str = Field(alias="AuthenticationCode1")
    authentication_code2: str = Field(alias="AuthenticationCode2")


class EnableMFADeviceRequestUserEnableMfaModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")
    authentication_code1: str = Field(alias="AuthenticationCode1")
    authentication_code2: str = Field(alias="AuthenticationCode2")


class EntityInfoModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    type: Literal["GROUP", "ROLE", "USER"] = Field(alias="Type")
    id: str = Field(alias="Id")
    path: Optional[str] = Field(default=None, alias="Path")


class ErrorDetailsModel(BaseModel):
    message: str = Field(alias="Message")
    code: str = Field(alias="Code")


class OrganizationsDecisionDetailModel(BaseModel):
    allowed_by_organizations: Optional[bool] = Field(
        default=None, alias="AllowedByOrganizations"
    )


class PermissionsBoundaryDecisionDetailModel(BaseModel):
    allowed_by_permissions_boundary: Optional[bool] = Field(
        default=None, alias="AllowedByPermissionsBoundary"
    )


class GenerateOrganizationsAccessReportRequestModel(BaseModel):
    entity_path: str = Field(alias="EntityPath")
    organizations_policy_id: Optional[str] = Field(
        default=None, alias="OrganizationsPolicyId"
    )


class GenerateServiceLastAccessedDetailsRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    granularity: Optional[Literal["ACTION_LEVEL", "SERVICE_LEVEL"]] = Field(
        default=None, alias="Granularity"
    )


class GetAccessKeyLastUsedRequestModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetAccountAuthorizationDetailsRequestModel(BaseModel):
    filter: Optional[
        Sequence[
            Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
        ]
    ] = Field(default=None, alias="Filter")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class PasswordPolicyModel(BaseModel):
    minimum_password_length: Optional[int] = Field(
        default=None, alias="MinimumPasswordLength"
    )
    require_symbols: Optional[bool] = Field(default=None, alias="RequireSymbols")
    require_numbers: Optional[bool] = Field(default=None, alias="RequireNumbers")
    require_uppercase_characters: Optional[bool] = Field(
        default=None, alias="RequireUppercaseCharacters"
    )
    require_lowercase_characters: Optional[bool] = Field(
        default=None, alias="RequireLowercaseCharacters"
    )
    allow_users_to_change_password: Optional[bool] = Field(
        default=None, alias="AllowUsersToChangePassword"
    )
    expire_passwords: Optional[bool] = Field(default=None, alias="ExpirePasswords")
    max_password_age: Optional[int] = Field(default=None, alias="MaxPasswordAge")
    password_reuse_prevention: Optional[int] = Field(
        default=None, alias="PasswordReusePrevention"
    )
    hard_expiry: Optional[bool] = Field(default=None, alias="HardExpiry")


class GetContextKeysForCustomPolicyRequestModel(BaseModel):
    policy_input_list: Sequence[str] = Field(alias="PolicyInputList")


class GetContextKeysForPrincipalPolicyRequestModel(BaseModel):
    policy_source_arn: str = Field(alias="PolicySourceArn")
    policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PolicyInputList"
    )


class GetGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_name: str = Field(alias="PolicyName")


class GetGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")


class GetLoginProfileRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")


class GetOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")


class GetOrganizationsAccessReportRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")
    sort_key: Optional[
        Literal[
            "LAST_AUTHENTICATED_TIME_ASCENDING",
            "LAST_AUTHENTICATED_TIME_DESCENDING",
            "SERVICE_NAMESPACE_ASCENDING",
            "SERVICE_NAMESPACE_DESCENDING",
        ]
    ] = Field(default=None, alias="SortKey")


class GetPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")


class GetPolicyVersionRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    version_id: str = Field(alias="VersionId")


class GetRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_name: str = Field(alias="PolicyName")


class GetRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class GetSAMLProviderRequestModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")


class GetSSHPublicKeyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_id: str = Field(alias="SSHPublicKeyId")
    encoding: Literal["PEM", "SSH"] = Field(alias="Encoding")


class SSHPublicKeyModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_id: str = Field(alias="SSHPublicKeyId")
    fingerprint: str = Field(alias="Fingerprint")
    s_s_hpublic_key_body: str = Field(alias="SSHPublicKeyBody")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    upload_date: Optional[datetime] = Field(default=None, alias="UploadDate")


class GetServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")


class GetServiceLastAccessedDetailsRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GetServiceLastAccessedDetailsWithEntitiesRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    service_namespace: str = Field(alias="ServiceNamespace")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GetServiceLinkedRoleDeletionStatusRequestModel(BaseModel):
    deletion_task_id: str = Field(alias="DeletionTaskId")


class GetUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_name: str = Field(alias="PolicyName")


class GetUserRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")


class PolicyDetailModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_document: Optional[str] = Field(default=None, alias="PolicyDocument")


class GroupPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")


class ListAccessKeysRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListAccountAliasesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListAttachedGroupPoliciesRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListAttachedRolePoliciesRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListAttachedUserPoliciesRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListEntitiesForPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    entity_filter: Optional[
        Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
    ] = Field(default=None, alias="EntityFilter")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    policy_usage_filter: Optional[
        Literal["PermissionsBoundary", "PermissionsPolicy"]
    ] = Field(default=None, alias="PolicyUsageFilter")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class PolicyGroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_id: Optional[str] = Field(default=None, alias="GroupId")


class PolicyRoleModel(BaseModel):
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    role_id: Optional[str] = Field(default=None, alias="RoleId")


class PolicyUserModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    user_id: Optional[str] = Field(default=None, alias="UserId")


class ListGroupPoliciesRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListGroupsForUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListGroupsRequestModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListInstanceProfileTagsRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListInstanceProfilesForRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListInstanceProfilesRequestModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListMFADeviceTagsRequestModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListMFADevicesRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class MFADeviceModel(BaseModel):
    user_name: str = Field(alias="UserName")
    serial_number: str = Field(alias="SerialNumber")
    enable_date: datetime = Field(alias="EnableDate")


class ListOpenIDConnectProviderTagsRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class OpenIDConnectProviderListEntryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class PolicyGrantingServiceAccessModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_type: Literal["INLINE", "MANAGED"] = Field(alias="PolicyType")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")
    entity_type: Optional[Literal["GROUP", "ROLE", "USER"]] = Field(
        default=None, alias="EntityType"
    )
    entity_name: Optional[str] = Field(default=None, alias="EntityName")


class ListPoliciesGrantingServiceAccessRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    service_namespaces: Sequence[str] = Field(alias="ServiceNamespaces")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListPoliciesRequestModel(BaseModel):
    scope: Optional[Literal["AWS", "All", "Local"]] = Field(default=None, alias="Scope")
    only_attached: Optional[bool] = Field(default=None, alias="OnlyAttached")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    policy_usage_filter: Optional[
        Literal["PermissionsBoundary", "PermissionsPolicy"]
    ] = Field(default=None, alias="PolicyUsageFilter")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListPolicyTagsRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListPolicyVersionsRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListRolePoliciesRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListRoleTagsRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListRolesRequestModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListSAMLProviderTagsRequestModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class SAMLProviderListEntryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    valid_until: Optional[datetime] = Field(default=None, alias="ValidUntil")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class ListSSHPublicKeysRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class SSHPublicKeyMetadataModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_id: str = Field(alias="SSHPublicKeyId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    upload_date: datetime = Field(alias="UploadDate")


class ListServerCertificateTagsRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListServerCertificatesRequestModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ServerCertificateMetadataModel(BaseModel):
    path: str = Field(alias="Path")
    server_certificate_name: str = Field(alias="ServerCertificateName")
    server_certificate_id: str = Field(alias="ServerCertificateId")
    arn: str = Field(alias="Arn")
    upload_date: Optional[datetime] = Field(default=None, alias="UploadDate")
    expiration: Optional[datetime] = Field(default=None, alias="Expiration")


class ListServiceSpecificCredentialsRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")


class ServiceSpecificCredentialMetadataModel(BaseModel):
    user_name: str = Field(alias="UserName")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    service_user_name: str = Field(alias="ServiceUserName")
    create_date: datetime = Field(alias="CreateDate")
    service_specific_credential_id: str = Field(alias="ServiceSpecificCredentialId")
    service_name: str = Field(alias="ServiceName")


class ListSigningCertificatesRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class SigningCertificateModel(BaseModel):
    user_name: str = Field(alias="UserName")
    certificate_id: str = Field(alias="CertificateId")
    certificate_body: str = Field(alias="CertificateBody")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    upload_date: Optional[datetime] = Field(default=None, alias="UploadDate")


class ListUserPoliciesRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListUserTagsRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListUsersRequestModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListVirtualMFADevicesRequestModel(BaseModel):
    assignment_status: Optional[Literal["Any", "Assigned", "Unassigned"]] = Field(
        default=None, alias="AssignmentStatus"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class PositionModel(BaseModel):
    line: Optional[int] = Field(default=None, alias="Line")
    column: Optional[int] = Field(default=None, alias="Column")


class PutGroupPolicyRequestGroupCreatePolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")


class PutGroupPolicyRequestGroupPolicyPutModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")


class PutGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")


class PutRolePermissionsBoundaryRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    permissions_boundary: str = Field(alias="PermissionsBoundary")


class PutRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")


class PutRolePolicyRequestRolePolicyPutModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")


class PutUserPermissionsBoundaryRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    permissions_boundary: str = Field(alias="PermissionsBoundary")


class PutUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")


class PutUserPolicyRequestUserCreatePolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")


class PutUserPolicyRequestUserPolicyPutModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")


class RemoveClientIDFromOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    client_id: str = Field(alias="ClientID")


class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleModel(BaseModel):
    role_name: str = Field(alias="RoleName")


class RemoveRoleFromInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    role_name: str = Field(alias="RoleName")


class RemoveUserFromGroupRequestGroupRemoveUserModel(BaseModel):
    user_name: str = Field(alias="UserName")


class RemoveUserFromGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    user_name: str = Field(alias="UserName")


class RemoveUserFromGroupRequestUserRemoveGroupModel(BaseModel):
    group_name: str = Field(alias="GroupName")


class ResetServiceSpecificCredentialRequestModel(BaseModel):
    service_specific_credential_id: str = Field(alias="ServiceSpecificCredentialId")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class ResyncMFADeviceRequestMfaDeviceResyncModel(BaseModel):
    authentication_code1: str = Field(alias="AuthenticationCode1")
    authentication_code2: str = Field(alias="AuthenticationCode2")


class ResyncMFADeviceRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    serial_number: str = Field(alias="SerialNumber")
    authentication_code1: str = Field(alias="AuthenticationCode1")
    authentication_code2: str = Field(alias="AuthenticationCode2")


class RoleLastUsedModel(BaseModel):
    last_used_date: Optional[datetime] = Field(default=None, alias="LastUsedDate")
    region: Optional[str] = Field(default=None, alias="Region")


class RolePolicyRequestModel(BaseModel):
    name: str = Field(alias="name")


class TrackedActionLastAccessedModel(BaseModel):
    action_name: Optional[str] = Field(default=None, alias="ActionName")
    last_accessed_entity: Optional[str] = Field(
        default=None, alias="LastAccessedEntity"
    )
    last_accessed_time: Optional[datetime] = Field(
        default=None, alias="LastAccessedTime"
    )
    last_accessed_region: Optional[str] = Field(
        default=None, alias="LastAccessedRegion"
    )


class ServiceResourceAccessKeyPairRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")
    id: str = Field(alias="id")
    secret: str = Field(alias="secret")


class ServiceResourceAccessKeyRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")
    id: str = Field(alias="id")


class ServiceResourceAssumeRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="role_name")


class ServiceResourceGroupPolicyRequestModel(BaseModel):
    group_name: str = Field(alias="group_name")
    name: str = Field(alias="name")


class ServiceResourceGroupRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceInstanceProfileRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceLoginProfileRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")


class ServiceResourceMfaDeviceRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")
    serial_number: str = Field(alias="serial_number")


class ServiceResourcePolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="policy_arn")


class ServiceResourcePolicyVersionRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    version_id: str = Field(alias="version_id")


class ServiceResourceRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="role_name")
    name: str = Field(alias="name")


class ServiceResourceRoleRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceSamlProviderRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ServiceResourceServerCertificateRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceSigningCertificateRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")
    id: str = Field(alias="id")


class ServiceResourceUserPolicyRequestModel(BaseModel):
    user_name: str = Field(alias="user_name")
    name: str = Field(alias="name")


class ServiceResourceUserRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceVirtualMfaDeviceRequestModel(BaseModel):
    serial_number: str = Field(alias="serial_number")


class SetDefaultPolicyVersionRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    version_id: str = Field(alias="VersionId")


class SetSecurityTokenServicePreferencesRequestModel(BaseModel):
    global_endpoint_token_version: Literal["v1Token", "v2Token"] = Field(
        alias="GlobalEndpointTokenVersion"
    )


class UntagInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagMFADeviceRequestModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagSAMLProviderRequestModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UntagUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAccessKeyRequestAccessKeyActivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateAccessKeyRequestAccessKeyDeactivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateAccessKeyRequestAccessKeyPairActivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateAccessKeyRequestAccessKeyPairDeactivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateAccessKeyRequestModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateModel(BaseModel):
    minimum_password_length: Optional[int] = Field(
        default=None, alias="MinimumPasswordLength"
    )
    require_symbols: Optional[bool] = Field(default=None, alias="RequireSymbols")
    require_numbers: Optional[bool] = Field(default=None, alias="RequireNumbers")
    require_uppercase_characters: Optional[bool] = Field(
        default=None, alias="RequireUppercaseCharacters"
    )
    require_lowercase_characters: Optional[bool] = Field(
        default=None, alias="RequireLowercaseCharacters"
    )
    allow_users_to_change_password: Optional[bool] = Field(
        default=None, alias="AllowUsersToChangePassword"
    )
    max_password_age: Optional[int] = Field(default=None, alias="MaxPasswordAge")
    password_reuse_prevention: Optional[int] = Field(
        default=None, alias="PasswordReusePrevention"
    )
    hard_expiry: Optional[bool] = Field(default=None, alias="HardExpiry")


class UpdateAccountPasswordPolicyRequestModel(BaseModel):
    minimum_password_length: Optional[int] = Field(
        default=None, alias="MinimumPasswordLength"
    )
    require_symbols: Optional[bool] = Field(default=None, alias="RequireSymbols")
    require_numbers: Optional[bool] = Field(default=None, alias="RequireNumbers")
    require_uppercase_characters: Optional[bool] = Field(
        default=None, alias="RequireUppercaseCharacters"
    )
    require_lowercase_characters: Optional[bool] = Field(
        default=None, alias="RequireLowercaseCharacters"
    )
    allow_users_to_change_password: Optional[bool] = Field(
        default=None, alias="AllowUsersToChangePassword"
    )
    max_password_age: Optional[int] = Field(default=None, alias="MaxPasswordAge")
    password_reuse_prevention: Optional[int] = Field(
        default=None, alias="PasswordReusePrevention"
    )
    hard_expiry: Optional[bool] = Field(default=None, alias="HardExpiry")


class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyModel(
    BaseModel
):
    minimum_password_length: Optional[int] = Field(
        default=None, alias="MinimumPasswordLength"
    )
    require_symbols: Optional[bool] = Field(default=None, alias="RequireSymbols")
    require_numbers: Optional[bool] = Field(default=None, alias="RequireNumbers")
    require_uppercase_characters: Optional[bool] = Field(
        default=None, alias="RequireUppercaseCharacters"
    )
    require_lowercase_characters: Optional[bool] = Field(
        default=None, alias="RequireLowercaseCharacters"
    )
    allow_users_to_change_password: Optional[bool] = Field(
        default=None, alias="AllowUsersToChangePassword"
    )
    max_password_age: Optional[int] = Field(default=None, alias="MaxPasswordAge")
    password_reuse_prevention: Optional[int] = Field(
        default=None, alias="PasswordReusePrevention"
    )
    hard_expiry: Optional[bool] = Field(default=None, alias="HardExpiry")


class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateModel(BaseModel):
    policy_document: str = Field(alias="PolicyDocument")


class UpdateAssumeRolePolicyRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_document: str = Field(alias="PolicyDocument")


class UpdateGroupRequestGroupUpdateModel(BaseModel):
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_group_name: Optional[str] = Field(default=None, alias="NewGroupName")


class UpdateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_group_name: Optional[str] = Field(default=None, alias="NewGroupName")


class UpdateLoginProfileRequestLoginProfileUpdateModel(BaseModel):
    password: Optional[str] = Field(default=None, alias="Password")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class UpdateLoginProfileRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    password: Optional[str] = Field(default=None, alias="Password")
    password_reset_required: Optional[bool] = Field(
        default=None, alias="PasswordResetRequired"
    )


class UpdateOpenIDConnectProviderThumbprintRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    thumbprint_list: Sequence[str] = Field(alias="ThumbprintList")


class UpdateRoleDescriptionRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    description: str = Field(alias="Description")


class UpdateRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    description: Optional[str] = Field(default=None, alias="Description")
    max_session_duration: Optional[int] = Field(
        default=None, alias="MaxSessionDuration"
    )


class UpdateSAMLProviderRequestModel(BaseModel):
    s_aml_metadata_document: str = Field(alias="SAMLMetadataDocument")
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")


class UpdateSAMLProviderRequestSamlProviderUpdateModel(BaseModel):
    s_aml_metadata_document: str = Field(alias="SAMLMetadataDocument")


class UpdateSSHPublicKeyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_id: str = Field(alias="SSHPublicKeyId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")


class UpdateServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_server_certificate_name: Optional[str] = Field(
        default=None, alias="NewServerCertificateName"
    )


class UpdateServerCertificateRequestServerCertificateUpdateModel(BaseModel):
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_server_certificate_name: Optional[str] = Field(
        default=None, alias="NewServerCertificateName"
    )


class UpdateServiceSpecificCredentialRequestModel(BaseModel):
    service_specific_credential_id: str = Field(alias="ServiceSpecificCredentialId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class UpdateSigningCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    status: Literal["Active", "Inactive"] = Field(alias="Status")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class UpdateSigningCertificateRequestSigningCertificateActivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateSigningCertificateRequestSigningCertificateDeactivateModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )


class UpdateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_user_name: Optional[str] = Field(default=None, alias="NewUserName")


class UpdateUserRequestUserUpdateModel(BaseModel):
    new_path: Optional[str] = Field(default=None, alias="NewPath")
    new_user_name: Optional[str] = Field(default=None, alias="NewUserName")


class UploadSSHPublicKeyRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    s_s_hpublic_key_body: str = Field(alias="SSHPublicKeyBody")


class UploadSigningCertificateRequestModel(BaseModel):
    certificate_body: str = Field(alias="CertificateBody")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class UploadSigningCertificateRequestServiceResourceCreateSigningCertificateModel(
    BaseModel
):
    certificate_body: str = Field(alias="CertificateBody")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class UserAccessKeyRequestModel(BaseModel):
    id: str = Field(alias="id")


class UserMfaDeviceRequestModel(BaseModel):
    serial_number: str = Field(alias="serial_number")


class UserPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")


class UserSigningCertificateRequestModel(BaseModel):
    id: str = Field(alias="id")


class AttachedPermissionsBoundaryResponseMetadataModel(BaseModel):
    permissions_boundary_type: Literal["PermissionsBoundaryPolicy"] = Field(
        alias="PermissionsBoundaryType"
    )
    permissions_boundary_arn: str = Field(alias="PermissionsBoundaryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessKeyResponseModel(BaseModel):
    access_key: AccessKeyModel = Field(alias="AccessKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceLinkedRoleResponseModel(BaseModel):
    deletion_task_id: str = Field(alias="DeletionTaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateCredentialReportResponseModel(BaseModel):
    state: Literal["COMPLETE", "INPROGRESS", "STARTED"] = Field(alias="State")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateOrganizationsAccessReportResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateServiceLastAccessedDetailsResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessKeyLastUsedResponseModel(BaseModel):
    user_name: str = Field(alias="UserName")
    access_key_last_used: AccessKeyLastUsedModel = Field(alias="AccessKeyLastUsed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSummaryResponseModel(BaseModel):
    summary_map: Dict[
        Literal[
            "AccessKeysPerUserQuota",
            "AccountAccessKeysPresent",
            "AccountMFAEnabled",
            "AccountSigningCertificatesPresent",
            "AttachedPoliciesPerGroupQuota",
            "AttachedPoliciesPerRoleQuota",
            "AttachedPoliciesPerUserQuota",
            "GlobalEndpointTokenVersion",
            "GroupPolicySizeQuota",
            "Groups",
            "GroupsPerUserQuota",
            "GroupsQuota",
            "MFADevices",
            "MFADevicesInUse",
            "Policies",
            "PoliciesQuota",
            "PolicySizeQuota",
            "PolicyVersionsInUse",
            "PolicyVersionsInUseQuota",
            "ServerCertificates",
            "ServerCertificatesQuota",
            "SigningCertificatesPerUserQuota",
            "UserPolicySizeQuota",
            "Users",
            "UsersQuota",
            "VersionsPerPolicyQuota",
        ],
        int,
    ] = Field(alias="SummaryMap")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContextKeysForPolicyResponseModel(BaseModel):
    context_key_names: List[str] = Field(alias="ContextKeyNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCredentialReportResponseModel(BaseModel):
    content: bytes = Field(alias="Content")
    report_format: Literal["text/csv"] = Field(alias="ReportFormat")
    generated_time: datetime = Field(alias="GeneratedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupPolicyResponseModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRolePolicyResponseModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserPolicyResponseModel(BaseModel):
    user_name: str = Field(alias="UserName")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessKeysResponseModel(BaseModel):
    access_key_metadata: List[AccessKeyMetadataModel] = Field(alias="AccessKeyMetadata")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAliasesResponseModel(BaseModel):
    account_aliases: List[str] = Field(alias="AccountAliases")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupPoliciesResponseModel(BaseModel):
    policy_names: List[str] = Field(alias="PolicyNames")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRolePoliciesResponseModel(BaseModel):
    policy_names: List[str] = Field(alias="PolicyNames")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserPoliciesResponseModel(BaseModel):
    policy_names: List[str] = Field(alias="PolicyNames")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RoleLastUsedResponseMetadataModel(BaseModel):
    last_used_date: datetime = Field(alias="LastUsedDate")
    region: str = Field(alias="Region")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServerCertificateMetadataResponseMetadataModel(BaseModel):
    path: str = Field(alias="Path")
    server_certificate_name: str = Field(alias="ServerCertificateName")
    server_certificate_id: str = Field(alias="ServerCertificateId")
    arn: str = Field(alias="Arn")
    upload_date: datetime = Field(alias="UploadDate")
    expiration: datetime = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSAMLProviderResponseModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachedGroupPoliciesResponseModel(BaseModel):
    attached_policies: List[AttachedPolicyModel] = Field(alias="AttachedPolicies")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachedRolePoliciesResponseModel(BaseModel):
    attached_policies: List[AttachedPolicyModel] = Field(alias="AttachedPolicies")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachedUserPoliciesResponseModel(BaseModel):
    attached_policies: List[AttachedPolicyModel] = Field(alias="AttachedPolicies")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SimulateCustomPolicyRequestModel(BaseModel):
    policy_input_list: Sequence[str] = Field(alias="PolicyInputList")
    action_names: Sequence[str] = Field(alias="ActionNames")
    permissions_boundary_policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PermissionsBoundaryPolicyInputList"
    )
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    resource_policy: Optional[str] = Field(default=None, alias="ResourcePolicy")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    caller_arn: Optional[str] = Field(default=None, alias="CallerArn")
    context_entries: Optional[Sequence[ContextEntryModel]] = Field(
        default=None, alias="ContextEntries"
    )
    resource_handling_option: Optional[str] = Field(
        default=None, alias="ResourceHandlingOption"
    )
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class SimulatePrincipalPolicyRequestModel(BaseModel):
    policy_source_arn: str = Field(alias="PolicySourceArn")
    action_names: Sequence[str] = Field(alias="ActionNames")
    policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PolicyInputList"
    )
    permissions_boundary_policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PermissionsBoundaryPolicyInputList"
    )
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    resource_policy: Optional[str] = Field(default=None, alias="ResourcePolicy")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    caller_arn: Optional[str] = Field(default=None, alias="CallerArn")
    context_entries: Optional[Sequence[ContextEntryModel]] = Field(
        default=None, alias="ContextEntries"
    )
    resource_handling_option: Optional[str] = Field(
        default=None, alias="ResourceHandlingOption"
    )
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class CreateGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsForUserResponseModel(BaseModel):
    groups: List[GroupModel] = Field(alias="Groups")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupModel] = Field(alias="Groups")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    path: Optional[str] = Field(default=None, alias="Path")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateInstanceProfileRequestServiceResourceCreateInstanceProfileModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    path: Optional[str] = Field(default=None, alias="Path")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateOpenIDConnectProviderRequestModel(BaseModel):
    url: str = Field(alias="Url")
    thumbprint_list: Sequence[str] = Field(alias="ThumbprintList")
    client_idlist: Optional[Sequence[str]] = Field(default=None, alias="ClientIDList")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateOpenIDConnectProviderResponseModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    path: Optional[str] = Field(default=None, alias="Path")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreatePolicyRequestServiceResourceCreatePolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    path: Optional[str] = Field(default=None, alias="Path")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    assume_role_policy_document: str = Field(alias="AssumeRolePolicyDocument")
    path: Optional[str] = Field(default=None, alias="Path")
    description: Optional[str] = Field(default=None, alias="Description")
    max_session_duration: Optional[int] = Field(
        default=None, alias="MaxSessionDuration"
    )
    permissions_boundary: Optional[str] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateRoleRequestServiceResourceCreateRoleModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    assume_role_policy_document: str = Field(alias="AssumeRolePolicyDocument")
    path: Optional[str] = Field(default=None, alias="Path")
    description: Optional[str] = Field(default=None, alias="Description")
    max_session_duration: Optional[int] = Field(
        default=None, alias="MaxSessionDuration"
    )
    permissions_boundary: Optional[str] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSAMLProviderRequestModel(BaseModel):
    s_aml_metadata_document: str = Field(alias="SAMLMetadataDocument")
    name: str = Field(alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSAMLProviderRequestServiceResourceCreateSamlProviderModel(BaseModel):
    s_aml_metadata_document: str = Field(alias="SAMLMetadataDocument")
    name: str = Field(alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSAMLProviderResponseModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    path: Optional[str] = Field(default=None, alias="Path")
    permissions_boundary: Optional[str] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserRequestServiceResourceCreateUserModel(BaseModel):
    user_name: str = Field(alias="UserName")
    path: Optional[str] = Field(default=None, alias="Path")
    permissions_boundary: Optional[str] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserRequestUserCreateModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    permissions_boundary: Optional[str] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateVirtualMFADeviceRequestModel(BaseModel):
    virtual_mfadevice_name: str = Field(alias="VirtualMFADeviceName")
    path: Optional[str] = Field(default=None, alias="Path")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceModel(
    BaseModel
):
    virtual_mfadevice_name: str = Field(alias="VirtualMFADeviceName")
    path: Optional[str] = Field(default=None, alias="Path")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetOpenIDConnectProviderResponseModel(BaseModel):
    url: str = Field(alias="Url")
    client_idlist: List[str] = Field(alias="ClientIDList")
    thumbprint_list: List[str] = Field(alias="ThumbprintList")
    create_date: datetime = Field(alias="CreateDate")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSAMLProviderResponseModel(BaseModel):
    s_aml_metadata_document: str = Field(alias="SAMLMetadataDocument")
    create_date: datetime = Field(alias="CreateDate")
    valid_until: datetime = Field(alias="ValidUntil")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceProfileTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMFADeviceTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOpenIDConnectProviderTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPolicyTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoleTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSAMLProviderTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServerCertificateTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    path: Optional[str] = Field(default=None, alias="Path")
    default_version_id: Optional[str] = Field(default=None, alias="DefaultVersionId")
    attachment_count: Optional[int] = Field(default=None, alias="AttachmentCount")
    permissions_boundary_usage_count: Optional[int] = Field(
        default=None, alias="PermissionsBoundaryUsageCount"
    )
    is_attachable: Optional[bool] = Field(default=None, alias="IsAttachable")
    description: Optional[str] = Field(default=None, alias="Description")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    update_date: Optional[datetime] = Field(default=None, alias="UpdateDate")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class TagInstanceProfileRequestModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagMFADeviceRequestModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagOpenIDConnectProviderRequestModel(BaseModel):
    open_idconnect_provider_arn: str = Field(alias="OpenIDConnectProviderArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagRoleRequestModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagSAMLProviderRequestModel(BaseModel):
    s_aml_provider_arn: str = Field(alias="SAMLProviderArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class UploadServerCertificateRequestModel(BaseModel):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    certificate_body: str = Field(alias="CertificateBody")
    private_key: str = Field(alias="PrivateKey")
    path: Optional[str] = Field(default=None, alias="Path")
    certificate_chain: Optional[str] = Field(default=None, alias="CertificateChain")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UploadServerCertificateRequestServiceResourceCreateServerCertificateModel(
    BaseModel
):
    server_certificate_name: str = Field(alias="ServerCertificateName")
    certificate_body: str = Field(alias="CertificateBody")
    private_key: str = Field(alias="PrivateKey")
    path: Optional[str] = Field(default=None, alias="Path")
    certificate_chain: Optional[str] = Field(default=None, alias="CertificateChain")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UserResponseMetadataModel(BaseModel):
    path: str = Field(alias="Path")
    user_name: str = Field(alias="UserName")
    user_id: str = Field(alias="UserId")
    arn: str = Field(alias="Arn")
    create_date: datetime = Field(alias="CreateDate")
    password_last_used: datetime = Field(alias="PasswordLastUsed")
    permissions_boundary: AttachedPermissionsBoundaryModel = Field(
        alias="PermissionsBoundary"
    )
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserModel(BaseModel):
    path: str = Field(alias="Path")
    user_name: str = Field(alias="UserName")
    user_id: str = Field(alias="UserId")
    arn: str = Field(alias="Arn")
    create_date: datetime = Field(alias="CreateDate")
    password_last_used: Optional[datetime] = Field(
        default=None, alias="PasswordLastUsed"
    )
    permissions_boundary: Optional[AttachedPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateLoginProfileResponseModel(BaseModel):
    login_profile: LoginProfileModel = Field(alias="LoginProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoginProfileResponseModel(BaseModel):
    login_profile: LoginProfileModel = Field(alias="LoginProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePolicyVersionResponseModel(BaseModel):
    policy_version: PolicyVersionModel = Field(alias="PolicyVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyVersionResponseModel(BaseModel):
    policy_version: PolicyVersionModel = Field(alias="PolicyVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPolicyVersionsResponseModel(BaseModel):
    versions: List[PolicyVersionModel] = Field(alias="Versions")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ManagedPolicyDetailModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    path: Optional[str] = Field(default=None, alias="Path")
    default_version_id: Optional[str] = Field(default=None, alias="DefaultVersionId")
    attachment_count: Optional[int] = Field(default=None, alias="AttachmentCount")
    permissions_boundary_usage_count: Optional[int] = Field(
        default=None, alias="PermissionsBoundaryUsageCount"
    )
    is_attachable: Optional[bool] = Field(default=None, alias="IsAttachable")
    description: Optional[str] = Field(default=None, alias="Description")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    update_date: Optional[datetime] = Field(default=None, alias="UpdateDate")
    policy_version_list: Optional[List[PolicyVersionModel]] = Field(
        default=None, alias="PolicyVersionList"
    )


class CreateServiceSpecificCredentialResponseModel(BaseModel):
    service_specific_credential: ServiceSpecificCredentialModel = Field(
        alias="ServiceSpecificCredential"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetServiceSpecificCredentialResponseModel(BaseModel):
    service_specific_credential: ServiceSpecificCredentialModel = Field(
        alias="ServiceSpecificCredential"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletionTaskFailureReasonTypeModel(BaseModel):
    reason: Optional[str] = Field(default=None, alias="Reason")
    role_usage_list: Optional[List[RoleUsageTypeModel]] = Field(
        default=None, alias="RoleUsageList"
    )


class EntityDetailsModel(BaseModel):
    entity_info: EntityInfoModel = Field(alias="EntityInfo")
    last_authenticated: Optional[datetime] = Field(
        default=None, alias="LastAuthenticated"
    )


class GetOrganizationsAccessReportResponseModel(BaseModel):
    job_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS"] = Field(alias="JobStatus")
    job_creation_date: datetime = Field(alias="JobCreationDate")
    job_completion_date: datetime = Field(alias="JobCompletionDate")
    number_of_services_accessible: int = Field(alias="NumberOfServicesAccessible")
    number_of_services_not_accessed: int = Field(alias="NumberOfServicesNotAccessed")
    access_details: List[AccessDetailModel] = Field(alias="AccessDetails")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    error_details: ErrorDetailsModel = Field(alias="ErrorDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateModel(
    BaseModel
):
    filter: Optional[
        Sequence[
            Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
        ]
    ] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetGroupRequestGetGroupPaginateModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccessKeysRequestListAccessKeysPaginateModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountAliasesRequestListAccountAliasesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateModel(BaseModel):
    user_name: str = Field(alias="UserName")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    entity_filter: Optional[
        Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
    ] = Field(default=None, alias="EntityFilter")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    policy_usage_filter: Optional[
        Literal["PermissionsBoundary", "PermissionsPolicy"]
    ] = Field(default=None, alias="PolicyUsageFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupPoliciesRequestListGroupPoliciesPaginateModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsForUserRequestListGroupsForUserPaginateModel(BaseModel):
    user_name: str = Field(alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsRequestListGroupsPaginateModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateModel(
    BaseModel
):
    role_name: str = Field(alias="RoleName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceProfilesRequestListInstanceProfilesPaginateModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMFADevicesRequestListMFADevicesPaginateModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesRequestListPoliciesPaginateModel(BaseModel):
    scope: Optional[Literal["AWS", "All", "Local"]] = Field(default=None, alias="Scope")
    only_attached: Optional[bool] = Field(default=None, alias="OnlyAttached")
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    policy_usage_filter: Optional[
        Literal["PermissionsBoundary", "PermissionsPolicy"]
    ] = Field(default=None, alias="PolicyUsageFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPolicyVersionsRequestListPolicyVersionsPaginateModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRolePoliciesRequestListRolePoliciesPaginateModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRolesRequestListRolesPaginateModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSSHPublicKeysRequestListSSHPublicKeysPaginateModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServerCertificatesRequestListServerCertificatesPaginateModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSigningCertificatesRequestListSigningCertificatesPaginateModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserPoliciesRequestListUserPoliciesPaginateModel(BaseModel):
    user_name: str = Field(alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserTagsRequestListUserTagsPaginateModel(BaseModel):
    user_name: str = Field(alias="UserName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    path_prefix: Optional[str] = Field(default=None, alias="PathPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateModel(BaseModel):
    assignment_status: Optional[Literal["Any", "Assigned", "Unassigned"]] = Field(
        default=None, alias="AssignmentStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SimulateCustomPolicyRequestSimulateCustomPolicyPaginateModel(BaseModel):
    policy_input_list: Sequence[str] = Field(alias="PolicyInputList")
    action_names: Sequence[str] = Field(alias="ActionNames")
    permissions_boundary_policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PermissionsBoundaryPolicyInputList"
    )
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    resource_policy: Optional[str] = Field(default=None, alias="ResourcePolicy")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    caller_arn: Optional[str] = Field(default=None, alias="CallerArn")
    context_entries: Optional[Sequence[ContextEntryModel]] = Field(
        default=None, alias="ContextEntries"
    )
    resource_handling_option: Optional[str] = Field(
        default=None, alias="ResourceHandlingOption"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateModel(BaseModel):
    policy_source_arn: str = Field(alias="PolicySourceArn")
    action_names: Sequence[str] = Field(alias="ActionNames")
    policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PolicyInputList"
    )
    permissions_boundary_policy_input_list: Optional[Sequence[str]] = Field(
        default=None, alias="PermissionsBoundaryPolicyInputList"
    )
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    resource_policy: Optional[str] = Field(default=None, alias="ResourcePolicy")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    caller_arn: Optional[str] = Field(default=None, alias="CallerArn")
    context_entries: Optional[Sequence[ContextEntryModel]] = Field(
        default=None, alias="ContextEntries"
    )
    resource_handling_option: Optional[str] = Field(
        default=None, alias="ResourceHandlingOption"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAccountPasswordPolicyResponseModel(BaseModel):
    password_policy: PasswordPolicyModel = Field(alias="PasswordPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceProfileRequestInstanceProfileExistsWaitModel(BaseModel):
    instance_profile_name: str = Field(alias="InstanceProfileName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetPolicyRequestPolicyExistsWaitModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetRoleRequestRoleExistsWaitModel(BaseModel):
    role_name: str = Field(alias="RoleName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetUserRequestUserExistsWaitModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetSSHPublicKeyResponseModel(BaseModel):
    s_s_hpublic_key: SSHPublicKeyModel = Field(alias="SSHPublicKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadSSHPublicKeyResponseModel(BaseModel):
    s_s_hpublic_key: SSHPublicKeyModel = Field(alias="SSHPublicKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GroupDetailModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    group_policy_list: Optional[List[PolicyDetailModel]] = Field(
        default=None, alias="GroupPolicyList"
    )
    attached_managed_policies: Optional[List[AttachedPolicyModel]] = Field(
        default=None, alias="AttachedManagedPolicies"
    )


class UserDetailModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    user_policy_list: Optional[List[PolicyDetailModel]] = Field(
        default=None, alias="UserPolicyList"
    )
    group_list: Optional[List[str]] = Field(default=None, alias="GroupList")
    attached_managed_policies: Optional[List[AttachedPolicyModel]] = Field(
        default=None, alias="AttachedManagedPolicies"
    )
    permissions_boundary: Optional[AttachedPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListEntitiesForPolicyResponseModel(BaseModel):
    policy_groups: List[PolicyGroupModel] = Field(alias="PolicyGroups")
    policy_users: List[PolicyUserModel] = Field(alias="PolicyUsers")
    policy_roles: List[PolicyRoleModel] = Field(alias="PolicyRoles")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMFADevicesResponseModel(BaseModel):
    mfadevices: List[MFADeviceModel] = Field(alias="MFADevices")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOpenIDConnectProvidersResponseModel(BaseModel):
    open_idconnect_provider_list: List[OpenIDConnectProviderListEntryModel] = Field(
        alias="OpenIDConnectProviderList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesGrantingServiceAccessEntryModel(BaseModel):
    service_namespace: Optional[str] = Field(default=None, alias="ServiceNamespace")
    policies: Optional[List[PolicyGrantingServiceAccessModel]] = Field(
        default=None, alias="Policies"
    )


class ListSAMLProvidersResponseModel(BaseModel):
    s_aml_provider_list: List[SAMLProviderListEntryModel] = Field(
        alias="SAMLProviderList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSSHPublicKeysResponseModel(BaseModel):
    s_s_hpublic_keys: List[SSHPublicKeyMetadataModel] = Field(alias="SSHPublicKeys")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServerCertificatesResponseModel(BaseModel):
    server_certificate_metadata_list: List[ServerCertificateMetadataModel] = Field(
        alias="ServerCertificateMetadataList"
    )
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServerCertificateModel(BaseModel):
    server_certificate_metadata: ServerCertificateMetadataModel = Field(
        alias="ServerCertificateMetadata"
    )
    certificate_body: str = Field(alias="CertificateBody")
    certificate_chain: Optional[str] = Field(default=None, alias="CertificateChain")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class UploadServerCertificateResponseModel(BaseModel):
    server_certificate_metadata: ServerCertificateMetadataModel = Field(
        alias="ServerCertificateMetadata"
    )
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceSpecificCredentialsResponseModel(BaseModel):
    service_specific_credentials: List[ServiceSpecificCredentialMetadataModel] = Field(
        alias="ServiceSpecificCredentials"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSigningCertificatesResponseModel(BaseModel):
    certificates: List[SigningCertificateModel] = Field(alias="Certificates")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadSigningCertificateResponseModel(BaseModel):
    certificate: SigningCertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StatementModel(BaseModel):
    source_policy_id: Optional[str] = Field(default=None, alias="SourcePolicyId")
    source_policy_type: Optional[
        Literal[
            "aws-managed", "group", "none", "resource", "role", "user", "user-managed"
        ]
    ] = Field(default=None, alias="SourcePolicyType")
    start_position: Optional[PositionModel] = Field(default=None, alias="StartPosition")
    end_position: Optional[PositionModel] = Field(default=None, alias="EndPosition")


class RoleModel(BaseModel):
    path: str = Field(alias="Path")
    role_name: str = Field(alias="RoleName")
    role_id: str = Field(alias="RoleId")
    arn: str = Field(alias="Arn")
    create_date: datetime = Field(alias="CreateDate")
    assume_role_policy_document: Optional[str] = Field(
        default=None, alias="AssumeRolePolicyDocument"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    max_session_duration: Optional[int] = Field(
        default=None, alias="MaxSessionDuration"
    )
    permissions_boundary: Optional[AttachedPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    role_last_used: Optional[RoleLastUsedModel] = Field(
        default=None, alias="RoleLastUsed"
    )


class ServiceLastAccessedModel(BaseModel):
    service_name: str = Field(alias="ServiceName")
    service_namespace: str = Field(alias="ServiceNamespace")
    last_authenticated: Optional[datetime] = Field(
        default=None, alias="LastAuthenticated"
    )
    last_authenticated_entity: Optional[str] = Field(
        default=None, alias="LastAuthenticatedEntity"
    )
    last_authenticated_region: Optional[str] = Field(
        default=None, alias="LastAuthenticatedRegion"
    )
    total_authenticated_entities: Optional[int] = Field(
        default=None, alias="TotalAuthenticatedEntities"
    )
    tracked_actions_last_accessed: Optional[
        List[TrackedActionLastAccessedModel]
    ] = Field(default=None, alias="TrackedActionsLastAccessed")


class CreatePolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesResponseModel(BaseModel):
    policies: List[PolicyModel] = Field(alias="Policies")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    users: List[UserModel] = Field(alias="Users")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualMFADeviceModel(BaseModel):
    serial_number: str = Field(alias="SerialNumber")
    base32_string_seed: Optional[bytes] = Field(default=None, alias="Base32StringSeed")
    qrcode_p_ng: Optional[bytes] = Field(default=None, alias="QRCodePNG")
    user: Optional[UserModel] = Field(default=None, alias="User")
    enable_date: Optional[datetime] = Field(default=None, alias="EnableDate")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class GetServiceLinkedRoleDeletionStatusResponseModel(BaseModel):
    status: Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"] = Field(
        alias="Status"
    )
    reason: DeletionTaskFailureReasonTypeModel = Field(alias="Reason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceLastAccessedDetailsWithEntitiesResponseModel(BaseModel):
    job_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS"] = Field(alias="JobStatus")
    job_creation_date: datetime = Field(alias="JobCreationDate")
    job_completion_date: datetime = Field(alias="JobCompletionDate")
    entity_details_list: List[EntityDetailsModel] = Field(alias="EntityDetailsList")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    error: ErrorDetailsModel = Field(alias="Error")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesGrantingServiceAccessResponseModel(BaseModel):
    policies_granting_service_access: List[
        ListPoliciesGrantingServiceAccessEntryModel
    ] = Field(alias="PoliciesGrantingServiceAccess")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServerCertificateResponseModel(BaseModel):
    server_certificate: ServerCertificateModel = Field(alias="ServerCertificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceSpecificResultModel(BaseModel):
    eval_resource_name: str = Field(alias="EvalResourceName")
    eval_resource_decision: Literal["allowed", "explicitDeny", "implicitDeny"] = Field(
        alias="EvalResourceDecision"
    )
    matched_statements: Optional[List[StatementModel]] = Field(
        default=None, alias="MatchedStatements"
    )
    missing_context_values: Optional[List[str]] = Field(
        default=None, alias="MissingContextValues"
    )
    eval_decision_details: Optional[
        Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]]
    ] = Field(default=None, alias="EvalDecisionDetails")
    permissions_boundary_decision_detail: Optional[
        PermissionsBoundaryDecisionDetailModel
    ] = Field(default=None, alias="PermissionsBoundaryDecisionDetail")


class CreateRoleResponseModel(BaseModel):
    role: RoleModel = Field(alias="Role")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceLinkedRoleResponseModel(BaseModel):
    role: RoleModel = Field(alias="Role")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoleResponseModel(BaseModel):
    role: RoleModel = Field(alias="Role")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceProfileModel(BaseModel):
    path: str = Field(alias="Path")
    instance_profile_name: str = Field(alias="InstanceProfileName")
    instance_profile_id: str = Field(alias="InstanceProfileId")
    arn: str = Field(alias="Arn")
    create_date: datetime = Field(alias="CreateDate")
    roles: List[RoleModel] = Field(alias="Roles")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListRolesResponseModel(BaseModel):
    roles: List[RoleModel] = Field(alias="Roles")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoleDescriptionResponseModel(BaseModel):
    role: RoleModel = Field(alias="Role")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceLastAccessedDetailsResponseModel(BaseModel):
    job_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS"] = Field(alias="JobStatus")
    job_type: Literal["ACTION_LEVEL", "SERVICE_LEVEL"] = Field(alias="JobType")
    job_creation_date: datetime = Field(alias="JobCreationDate")
    services_last_accessed: List[ServiceLastAccessedModel] = Field(
        alias="ServicesLastAccessed"
    )
    job_completion_date: datetime = Field(alias="JobCompletionDate")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    error: ErrorDetailsModel = Field(alias="Error")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVirtualMFADeviceResponseModel(BaseModel):
    virtual_mfadevice: VirtualMFADeviceModel = Field(alias="VirtualMFADevice")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualMFADevicesResponseModel(BaseModel):
    virtual_mfadevices: List[VirtualMFADeviceModel] = Field(alias="VirtualMFADevices")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluationResultModel(BaseModel):
    eval_action_name: str = Field(alias="EvalActionName")
    eval_decision: Literal["allowed", "explicitDeny", "implicitDeny"] = Field(
        alias="EvalDecision"
    )
    eval_resource_name: Optional[str] = Field(default=None, alias="EvalResourceName")
    matched_statements: Optional[List[StatementModel]] = Field(
        default=None, alias="MatchedStatements"
    )
    missing_context_values: Optional[List[str]] = Field(
        default=None, alias="MissingContextValues"
    )
    organizations_decision_detail: Optional[OrganizationsDecisionDetailModel] = Field(
        default=None, alias="OrganizationsDecisionDetail"
    )
    permissions_boundary_decision_detail: Optional[
        PermissionsBoundaryDecisionDetailModel
    ] = Field(default=None, alias="PermissionsBoundaryDecisionDetail")
    eval_decision_details: Optional[
        Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]]
    ] = Field(default=None, alias="EvalDecisionDetails")
    resource_specific_results: Optional[List[ResourceSpecificResultModel]] = Field(
        default=None, alias="ResourceSpecificResults"
    )


class CreateInstanceProfileResponseModel(BaseModel):
    instance_profile: InstanceProfileModel = Field(alias="InstanceProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceProfileResponseModel(BaseModel):
    instance_profile: InstanceProfileModel = Field(alias="InstanceProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceProfilesForRoleResponseModel(BaseModel):
    instance_profiles: List[InstanceProfileModel] = Field(alias="InstanceProfiles")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceProfilesResponseModel(BaseModel):
    instance_profiles: List[InstanceProfileModel] = Field(alias="InstanceProfiles")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RoleDetailModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    role_id: Optional[str] = Field(default=None, alias="RoleId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    assume_role_policy_document: Optional[str] = Field(
        default=None, alias="AssumeRolePolicyDocument"
    )
    instance_profile_list: Optional[List[InstanceProfileModel]] = Field(
        default=None, alias="InstanceProfileList"
    )
    role_policy_list: Optional[List[PolicyDetailModel]] = Field(
        default=None, alias="RolePolicyList"
    )
    attached_managed_policies: Optional[List[AttachedPolicyModel]] = Field(
        default=None, alias="AttachedManagedPolicies"
    )
    permissions_boundary: Optional[AttachedPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    role_last_used: Optional[RoleLastUsedModel] = Field(
        default=None, alias="RoleLastUsed"
    )


class SimulatePolicyResponseModel(BaseModel):
    evaluation_results: List[EvaluationResultModel] = Field(alias="EvaluationResults")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountAuthorizationDetailsResponseModel(BaseModel):
    user_detail_list: List[UserDetailModel] = Field(alias="UserDetailList")
    group_detail_list: List[GroupDetailModel] = Field(alias="GroupDetailList")
    role_detail_list: List[RoleDetailModel] = Field(alias="RoleDetailList")
    policies: List[ManagedPolicyDetailModel] = Field(alias="Policies")
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
