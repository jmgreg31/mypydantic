# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountModificationModel(BaseModel):
    modification_state: Optional[Literal["COMPLETED", "FAILED", "PENDING"]] = Field(
        default=None, alias="ModificationState"
    )
    dedicated_tenancy_support: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DedicatedTenancySupport"
    )
    dedicated_tenancy_management_cidr_range: Optional[str] = Field(
        default=None, alias="DedicatedTenancyManagementCidrRange"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class AssociateConnectionAliasRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    resource_id: str = Field(alias="ResourceId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateIpGroupsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    group_ids: Sequence[str] = Field(alias="GroupIds")


class IpRuleItemModel(BaseModel):
    ip_rule: Optional[str] = Field(default=None, alias="ipRule")
    rule_desc: Optional[str] = Field(default=None, alias="ruleDesc")


class CertificateBasedAuthPropertiesModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )


class ClientPropertiesModel(BaseModel):
    reconnect_enabled: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ReconnectEnabled"
    )
    log_upload_enabled: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="LogUploadEnabled"
    )


class ComputeTypeModel(BaseModel):
    name: Optional[
        Literal[
            "GRAPHICS",
            "GRAPHICSPRO",
            "GRAPHICSPRO_G4DN",
            "GRAPHICS_G4DN",
            "PERFORMANCE",
            "POWER",
            "POWERPRO",
            "STANDARD",
            "VALUE",
        ]
    ] = Field(default=None, alias="Name")


class ConnectClientAddInModel(BaseModel):
    add_in_id: Optional[str] = Field(default=None, alias="AddInId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    name: Optional[str] = Field(default=None, alias="Name")
    url: Optional[str] = Field(default=None, alias="URL")


class ConnectionAliasAssociationModel(BaseModel):
    association_status: Optional[
        Literal[
            "ASSOCIATED_WITH_OWNER_ACCOUNT",
            "ASSOCIATED_WITH_SHARED_ACCOUNT",
            "NOT_ASSOCIATED",
            "PENDING_ASSOCIATION",
            "PENDING_DISASSOCIATION",
        ]
    ] = Field(default=None, alias="AssociationStatus")
    associated_account_id: Optional[str] = Field(
        default=None, alias="AssociatedAccountId"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    connection_identifier: Optional[str] = Field(
        default=None, alias="ConnectionIdentifier"
    )


class ConnectionAliasPermissionModel(BaseModel):
    shared_account_id: str = Field(alias="SharedAccountId")
    allow_association: bool = Field(alias="AllowAssociation")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CreateConnectClientAddInRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    name: str = Field(alias="Name")
    url: str = Field(alias="URL")


class PendingCreateStandbyWorkspacesRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    state: Optional[
        Literal[
            "ADMIN_MAINTENANCE",
            "AVAILABLE",
            "ERROR",
            "IMPAIRED",
            "MAINTENANCE",
            "PENDING",
            "REBOOTING",
            "REBUILDING",
            "RESTORING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUSPENDED",
            "TERMINATED",
            "TERMINATING",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")


class RootStorageModel(BaseModel):
    capacity: Optional[str] = Field(default=None, alias="Capacity")


class UserStorageModel(BaseModel):
    capacity: Optional[str] = Field(default=None, alias="Capacity")


class OperatingSystemModel(BaseModel):
    type: Optional[Literal["LINUX", "WINDOWS"]] = Field(default=None, alias="Type")


class DefaultClientBrandingAttributesModel(BaseModel):
    logo_url: Optional[str] = Field(default=None, alias="LogoUrl")
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_link: Optional[str] = Field(default=None, alias="SupportLink")
    forgot_password_link: Optional[str] = Field(
        default=None, alias="ForgotPasswordLink"
    )
    login_message: Optional[Dict[str, str]] = Field(default=None, alias="LoginMessage")


class DefaultImportClientBrandingAttributesModel(BaseModel):
    logo: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Logo"
    )
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_link: Optional[str] = Field(default=None, alias="SupportLink")
    forgot_password_link: Optional[str] = Field(
        default=None, alias="ForgotPasswordLink"
    )
    login_message: Optional[Mapping[str, str]] = Field(
        default=None, alias="LoginMessage"
    )


class DefaultWorkspaceCreationPropertiesModel(BaseModel):
    enable_work_docs: Optional[bool] = Field(default=None, alias="EnableWorkDocs")
    enable_internet_access: Optional[bool] = Field(
        default=None, alias="EnableInternetAccess"
    )
    default_ou: Optional[str] = Field(default=None, alias="DefaultOu")
    custom_security_group_id: Optional[str] = Field(
        default=None, alias="CustomSecurityGroupId"
    )
    user_enabled_as_local_administrator: Optional[bool] = Field(
        default=None, alias="UserEnabledAsLocalAdministrator"
    )
    enable_maintenance_mode: Optional[bool] = Field(
        default=None, alias="EnableMaintenanceMode"
    )


class DeleteClientBrandingRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    platforms: Sequence[
        Literal[
            "DeviceTypeAndroid",
            "DeviceTypeIos",
            "DeviceTypeLinux",
            "DeviceTypeOsx",
            "DeviceTypeWeb",
            "DeviceTypeWindows",
        ]
    ] = Field(alias="Platforms")


class DeleteConnectClientAddInRequestModel(BaseModel):
    add_in_id: str = Field(alias="AddInId")
    resource_id: str = Field(alias="ResourceId")


class DeleteConnectionAliasRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")


class DeleteIpGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class DeleteTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DeleteWorkspaceBundleRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")


class DeleteWorkspaceImageRequestModel(BaseModel):
    image_id: str = Field(alias="ImageId")


class DeregisterWorkspaceDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccountModificationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeClientBrandingRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")


class IosClientBrandingAttributesModel(BaseModel):
    logo_url: Optional[str] = Field(default=None, alias="LogoUrl")
    logo2x_url: Optional[str] = Field(default=None, alias="Logo2xUrl")
    logo3x_url: Optional[str] = Field(default=None, alias="Logo3xUrl")
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_link: Optional[str] = Field(default=None, alias="SupportLink")
    forgot_password_link: Optional[str] = Field(
        default=None, alias="ForgotPasswordLink"
    )
    login_message: Optional[Dict[str, str]] = Field(default=None, alias="LoginMessage")


class DescribeClientPropertiesRequestModel(BaseModel):
    resource_ids: Sequence[str] = Field(alias="ResourceIds")


class DescribeConnectClientAddInsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeConnectionAliasPermissionsRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeConnectionAliasesRequestModel(BaseModel):
    alias_ids: Optional[Sequence[str]] = Field(default=None, alias="AliasIds")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeIpGroupsRequestModel(BaseModel):
    group_ids: Optional[Sequence[str]] = Field(default=None, alias="GroupIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")


class DescribeWorkspaceBundlesRequestModel(BaseModel):
    bundle_ids: Optional[Sequence[str]] = Field(default=None, alias="BundleIds")
    owner: Optional[str] = Field(default=None, alias="Owner")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeWorkspaceDirectoriesRequestModel(BaseModel):
    directory_ids: Optional[Sequence[str]] = Field(default=None, alias="DirectoryIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeWorkspaceImagePermissionsRequestModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ImagePermissionModel(BaseModel):
    shared_account_id: Optional[str] = Field(default=None, alias="SharedAccountId")


class DescribeWorkspaceImagesRequestModel(BaseModel):
    image_ids: Optional[Sequence[str]] = Field(default=None, alias="ImageIds")
    image_type: Optional[Literal["OWNED", "SHARED"]] = Field(
        default=None, alias="ImageType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeWorkspaceSnapshotsRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")


class SnapshotModel(BaseModel):
    snapshot_time: Optional[datetime] = Field(default=None, alias="SnapshotTime")


class DescribeWorkspacesConnectionStatusRequestModel(BaseModel):
    workspace_ids: Optional[Sequence[str]] = Field(default=None, alias="WorkspaceIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class WorkspaceConnectionStatusModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")
    connection_state: Optional[Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"]] = Field(
        default=None, alias="ConnectionState"
    )
    connection_state_check_timestamp: Optional[datetime] = Field(
        default=None, alias="ConnectionStateCheckTimestamp"
    )
    last_known_user_connection_timestamp: Optional[datetime] = Field(
        default=None, alias="LastKnownUserConnectionTimestamp"
    )


class DescribeWorkspacesRequestModel(BaseModel):
    workspace_ids: Optional[Sequence[str]] = Field(default=None, alias="WorkspaceIds")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DisassociateConnectionAliasRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")


class DisassociateIpGroupsRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    group_ids: Sequence[str] = Field(alias="GroupIds")


class FailedWorkspaceChangeRequestModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class IosImportClientBrandingAttributesModel(BaseModel):
    logo: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Logo"
    )
    logo2x: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Logo2x"
    )
    logo3x: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Logo3x"
    )
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_link: Optional[str] = Field(default=None, alias="SupportLink")
    forgot_password_link: Optional[str] = Field(
        default=None, alias="ForgotPasswordLink"
    )
    login_message: Optional[Mapping[str, str]] = Field(
        default=None, alias="LoginMessage"
    )


class ListAvailableManagementCidrRangesRequestModel(BaseModel):
    management_cidr_range_constraint: str = Field(alias="ManagementCidrRangeConstraint")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MigrateWorkspaceRequestModel(BaseModel):
    source_workspace_id: str = Field(alias="SourceWorkspaceId")
    bundle_id: str = Field(alias="BundleId")


class ModificationStateModel(BaseModel):
    resource: Optional[Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]] = Field(
        default=None, alias="Resource"
    )
    state: Optional[Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]] = Field(
        default=None, alias="State"
    )


class ModifyAccountRequestModel(BaseModel):
    dedicated_tenancy_support: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="DedicatedTenancySupport"
    )
    dedicated_tenancy_management_cidr_range: Optional[str] = Field(
        default=None, alias="DedicatedTenancyManagementCidrRange"
    )


class SamlPropertiesModel(BaseModel):
    status: Optional[
        Literal["DISABLED", "ENABLED", "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK"]
    ] = Field(default=None, alias="Status")
    user_access_url: Optional[str] = Field(default=None, alias="UserAccessUrl")
    relay_state_parameter_name: Optional[str] = Field(
        default=None, alias="RelayStateParameterName"
    )


class SelfservicePermissionsModel(BaseModel):
    restart_workspace: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="RestartWorkspace"
    )
    increase_volume_size: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="IncreaseVolumeSize"
    )
    change_compute_type: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ChangeComputeType"
    )
    switch_running_mode: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SwitchRunningMode"
    )
    rebuild_workspace: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="RebuildWorkspace"
    )


class WorkspaceAccessPropertiesModel(BaseModel):
    device_type_windows: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeWindows"
    )
    device_type_osx: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeOsx"
    )
    device_type_web: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeWeb"
    )
    device_type_ios: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeIos"
    )
    device_type_android: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeAndroid"
    )
    device_type_chrome_os: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeChromeOs"
    )
    device_type_zero_client: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeZeroClient"
    )
    device_type_linux: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="DeviceTypeLinux"
    )


class WorkspaceCreationPropertiesModel(BaseModel):
    enable_work_docs: Optional[bool] = Field(default=None, alias="EnableWorkDocs")
    enable_internet_access: Optional[bool] = Field(
        default=None, alias="EnableInternetAccess"
    )
    default_ou: Optional[str] = Field(default=None, alias="DefaultOu")
    custom_security_group_id: Optional[str] = Field(
        default=None, alias="CustomSecurityGroupId"
    )
    user_enabled_as_local_administrator: Optional[bool] = Field(
        default=None, alias="UserEnabledAsLocalAdministrator"
    )
    enable_maintenance_mode: Optional[bool] = Field(
        default=None, alias="EnableMaintenanceMode"
    )


class WorkspacePropertiesModel(BaseModel):
    running_mode: Optional[Literal["ALWAYS_ON", "AUTO_STOP", "MANUAL"]] = Field(
        default=None, alias="RunningMode"
    )
    running_mode_auto_stop_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="RunningModeAutoStopTimeoutInMinutes"
    )
    root_volume_size_gib: Optional[int] = Field(default=None, alias="RootVolumeSizeGib")
    user_volume_size_gib: Optional[int] = Field(default=None, alias="UserVolumeSizeGib")
    compute_type_name: Optional[
        Literal[
            "GRAPHICS",
            "GRAPHICSPRO",
            "GRAPHICSPRO_G4DN",
            "GRAPHICS_G4DN",
            "PERFORMANCE",
            "POWER",
            "POWERPRO",
            "STANDARD",
            "VALUE",
        ]
    ] = Field(default=None, alias="ComputeTypeName")
    protocols: Optional[Sequence[Literal["PCOIP", "WSP"]]] = Field(
        default=None, alias="Protocols"
    )


class ModifyWorkspaceStateRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")
    workspace_state: Literal["ADMIN_MAINTENANCE", "AVAILABLE"] = Field(
        alias="WorkspaceState"
    )


class RebootRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")


class RebuildRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")


class RelatedWorkspacePropertiesModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")
    region: Optional[str] = Field(default=None, alias="Region")
    state: Optional[
        Literal[
            "ADMIN_MAINTENANCE",
            "AVAILABLE",
            "ERROR",
            "IMPAIRED",
            "MAINTENANCE",
            "PENDING",
            "REBOOTING",
            "REBUILDING",
            "RESTORING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUSPENDED",
            "TERMINATED",
            "TERMINATING",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    type: Optional[Literal["PRIMARY", "STANDBY"]] = Field(default=None, alias="Type")


class RestoreWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")


class RevokeIpRulesRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    user_rules: Sequence[str] = Field(alias="UserRules")


class StartRequestModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")


class StopRequestModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")


class TerminateRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")


class UpdateConnectClientAddInRequestModel(BaseModel):
    add_in_id: str = Field(alias="AddInId")
    resource_id: str = Field(alias="ResourceId")
    name: Optional[str] = Field(default=None, alias="Name")
    url: Optional[str] = Field(default=None, alias="URL")


class UpdateResultModel(BaseModel):
    update_available: Optional[bool] = Field(default=None, alias="UpdateAvailable")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateWorkspaceBundleRequestModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    image_id: Optional[str] = Field(default=None, alias="ImageId")


class UpdateWorkspaceImagePermissionRequestModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    allow_copy_image: bool = Field(alias="AllowCopyImage")
    shared_account_id: str = Field(alias="SharedAccountId")


class AssociateConnectionAliasResultModel(BaseModel):
    connection_identifier: str = Field(alias="ConnectionIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyWorkspaceImageResultModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectClientAddInResultModel(BaseModel):
    add_in_id: str = Field(alias="AddInId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectionAliasResultModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIpGroupResultModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUpdatedWorkspaceImageResultModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountModificationsResultModel(BaseModel):
    account_modifications: List[AccountModificationModel] = Field(
        alias="AccountModifications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountResultModel(BaseModel):
    dedicated_tenancy_support: Literal["DISABLED", "ENABLED"] = Field(
        alias="DedicatedTenancySupport"
    )
    dedicated_tenancy_management_cidr_range: str = Field(
        alias="DedicatedTenancyManagementCidrRange"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportWorkspaceImageResultModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableManagementCidrRangesResultModel(BaseModel):
    management_cidr_ranges: List[str] = Field(alias="ManagementCidrRanges")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MigrateWorkspaceResultModel(BaseModel):
    source_workspace_id: str = Field(alias="SourceWorkspaceId")
    target_workspace_id: str = Field(alias="TargetWorkspaceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizeIpRulesRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    user_rules: Sequence[IpRuleItemModel] = Field(alias="UserRules")


class UpdateRulesOfIpGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    user_rules: Sequence[IpRuleItemModel] = Field(alias="UserRules")


class WorkspacesIpGroupModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="groupId")
    group_name: Optional[str] = Field(default=None, alias="groupName")
    group_desc: Optional[str] = Field(default=None, alias="groupDesc")
    user_rules: Optional[List[IpRuleItemModel]] = Field(default=None, alias="userRules")


class ModifyCertificateBasedAuthPropertiesRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    certificate_based_auth_properties: Optional[
        CertificateBasedAuthPropertiesModel
    ] = Field(default=None, alias="CertificateBasedAuthProperties")
    properties_to_delete: Optional[
        Sequence[Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]]
    ] = Field(default=None, alias="PropertiesToDelete")


class ClientPropertiesResultModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    client_properties: Optional[ClientPropertiesModel] = Field(
        default=None, alias="ClientProperties"
    )


class ModifyClientPropertiesRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    client_properties: ClientPropertiesModel = Field(alias="ClientProperties")


class DescribeConnectClientAddInsResultModel(BaseModel):
    add_ins: List[ConnectClientAddInModel] = Field(alias="AddIns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectionAliasModel(BaseModel):
    connection_string: Optional[str] = Field(default=None, alias="ConnectionString")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    state: Optional[Literal["CREATED", "CREATING", "DELETING"]] = Field(
        default=None, alias="State"
    )
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    associations: Optional[List[ConnectionAliasAssociationModel]] = Field(
        default=None, alias="Associations"
    )


class DescribeConnectionAliasPermissionsResultModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    connection_alias_permissions: List[ConnectionAliasPermissionModel] = Field(
        alias="ConnectionAliasPermissions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectionAliasPermissionRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    connection_alias_permission: ConnectionAliasPermissionModel = Field(
        alias="ConnectionAliasPermission"
    )


class CopyWorkspaceImageRequestModel(BaseModel):
    name: str = Field(alias="Name")
    source_image_id: str = Field(alias="SourceImageId")
    source_region: str = Field(alias="SourceRegion")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateConnectionAliasRequestModel(BaseModel):
    connection_string: str = Field(alias="ConnectionString")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateIpGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    group_desc: Optional[str] = Field(default=None, alias="GroupDesc")
    user_rules: Optional[Sequence[IpRuleItemModel]] = Field(
        default=None, alias="UserRules"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateUpdatedWorkspaceImageRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    source_image_id: str = Field(alias="SourceImageId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateWorkspaceImageRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    workspace_id: str = Field(alias="WorkspaceId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeTagsResultModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportWorkspaceImageRequestModel(BaseModel):
    ec2_image_id: str = Field(alias="Ec2ImageId")
    ingestion_process: Literal[
        "BYOL_GRAPHICS",
        "BYOL_GRAPHICSPRO",
        "BYOL_GRAPHICS_G4DN",
        "BYOL_GRAPHICS_G4DN_BYOP",
        "BYOL_REGULAR",
        "BYOL_REGULAR_BYOP",
        "BYOL_REGULAR_WSP",
    ] = Field(alias="IngestionProcess")
    image_name: str = Field(alias="ImageName")
    image_description: str = Field(alias="ImageDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    applications: Optional[
        Sequence[Literal["Microsoft_Office_2016", "Microsoft_Office_2019"]]
    ] = Field(default=None, alias="Applications")


class RegisterWorkspaceDirectoryRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    enable_work_docs: bool = Field(alias="EnableWorkDocs")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    enable_self_service: Optional[bool] = Field(default=None, alias="EnableSelfService")
    tenancy: Optional[Literal["DEDICATED", "SHARED"]] = Field(
        default=None, alias="Tenancy"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StandbyWorkspaceModel(BaseModel):
    primary_workspace_id: str = Field(alias="PrimaryWorkspaceId")
    directory_id: str = Field(alias="DirectoryId")
    volume_encryption_key: Optional[str] = Field(
        default=None, alias="VolumeEncryptionKey"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateWorkspaceBundleRequestModel(BaseModel):
    bundle_name: str = Field(alias="BundleName")
    bundle_description: str = Field(alias="BundleDescription")
    image_id: str = Field(alias="ImageId")
    compute_type: ComputeTypeModel = Field(alias="ComputeType")
    user_storage: UserStorageModel = Field(alias="UserStorage")
    root_storage: Optional[RootStorageModel] = Field(default=None, alias="RootStorage")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class WorkspaceBundleModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    name: Optional[str] = Field(default=None, alias="Name")
    owner: Optional[str] = Field(default=None, alias="Owner")
    description: Optional[str] = Field(default=None, alias="Description")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    root_storage: Optional[RootStorageModel] = Field(default=None, alias="RootStorage")
    user_storage: Optional[UserStorageModel] = Field(default=None, alias="UserStorage")
    compute_type: Optional[ComputeTypeModel] = Field(default=None, alias="ComputeType")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    state: Optional[Literal["AVAILABLE", "ERROR", "PENDING"]] = Field(
        default=None, alias="State"
    )
    bundle_type: Optional[Literal["REGULAR", "STANDBY"]] = Field(
        default=None, alias="BundleType"
    )


class CreateWorkspaceImageResultModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    operating_system: OperatingSystemModel = Field(alias="OperatingSystem")
    state: Literal["AVAILABLE", "ERROR", "PENDING"] = Field(alias="State")
    required_tenancy: Literal["DEDICATED", "DEFAULT"] = Field(alias="RequiredTenancy")
    created: datetime = Field(alias="Created")
    owner_account_id: str = Field(alias="OwnerAccountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountModificationsRequestDescribeAccountModificationsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeIpGroupsRequestDescribeIpGroupsPaginateModel(BaseModel):
    group_ids: Optional[Sequence[str]] = Field(default=None, alias="GroupIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateModel(BaseModel):
    bundle_ids: Optional[Sequence[str]] = Field(default=None, alias="BundleIds")
    owner: Optional[str] = Field(default=None, alias="Owner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateModel(
    BaseModel
):
    directory_ids: Optional[Sequence[str]] = Field(default=None, alias="DirectoryIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateModel(BaseModel):
    image_ids: Optional[Sequence[str]] = Field(default=None, alias="ImageIds")
    image_type: Optional[Literal["OWNED", "SHARED"]] = Field(
        default=None, alias="ImageType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateModel(
    BaseModel
):
    workspace_ids: Optional[Sequence[str]] = Field(default=None, alias="WorkspaceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeWorkspacesRequestDescribeWorkspacesPaginateModel(BaseModel):
    workspace_ids: Optional[Sequence[str]] = Field(default=None, alias="WorkspaceIds")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAvailableManagementCidrRangesRequestListAvailableManagementCidrRangesPaginateModel(
    BaseModel
):
    management_cidr_range_constraint: str = Field(alias="ManagementCidrRangeConstraint")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClientBrandingResultModel(BaseModel):
    device_type_windows: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeWindows"
    )
    device_type_osx: DefaultClientBrandingAttributesModel = Field(alias="DeviceTypeOsx")
    device_type_android: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeAndroid"
    )
    device_type_ios: IosClientBrandingAttributesModel = Field(alias="DeviceTypeIos")
    device_type_linux: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeLinux"
    )
    device_type_web: DefaultClientBrandingAttributesModel = Field(alias="DeviceTypeWeb")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportClientBrandingResultModel(BaseModel):
    device_type_windows: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeWindows"
    )
    device_type_osx: DefaultClientBrandingAttributesModel = Field(alias="DeviceTypeOsx")
    device_type_android: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeAndroid"
    )
    device_type_ios: IosClientBrandingAttributesModel = Field(alias="DeviceTypeIos")
    device_type_linux: DefaultClientBrandingAttributesModel = Field(
        alias="DeviceTypeLinux"
    )
    device_type_web: DefaultClientBrandingAttributesModel = Field(alias="DeviceTypeWeb")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceImagePermissionsResultModel(BaseModel):
    image_id: str = Field(alias="ImageId")
    image_permissions: List[ImagePermissionModel] = Field(alias="ImagePermissions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceSnapshotsResultModel(BaseModel):
    rebuild_snapshots: List[SnapshotModel] = Field(alias="RebuildSnapshots")
    restore_snapshots: List[SnapshotModel] = Field(alias="RestoreSnapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspacesConnectionStatusResultModel(BaseModel):
    workspaces_connection_status: List[WorkspaceConnectionStatusModel] = Field(
        alias="WorkspacesConnectionStatus"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedWorkspaceChangeRequestModel] = Field(
        alias="FailedRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebuildWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedWorkspaceChangeRequestModel] = Field(
        alias="FailedRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedWorkspaceChangeRequestModel] = Field(
        alias="FailedRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedWorkspaceChangeRequestModel] = Field(
        alias="FailedRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedWorkspaceChangeRequestModel] = Field(
        alias="FailedRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportClientBrandingRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    device_type_windows: Optional[DefaultImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeWindows"
    )
    device_type_osx: Optional[DefaultImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeOsx"
    )
    device_type_android: Optional[DefaultImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeAndroid"
    )
    device_type_ios: Optional[IosImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeIos"
    )
    device_type_linux: Optional[DefaultImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeLinux"
    )
    device_type_web: Optional[DefaultImportClientBrandingAttributesModel] = Field(
        default=None, alias="DeviceTypeWeb"
    )


class ModifySamlPropertiesRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    saml_properties: Optional[SamlPropertiesModel] = Field(
        default=None, alias="SamlProperties"
    )
    properties_to_delete: Optional[
        Sequence[
            Literal[
                "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME",
                "SAML_PROPERTIES_USER_ACCESS_URL",
            ]
        ]
    ] = Field(default=None, alias="PropertiesToDelete")


class ModifySelfservicePermissionsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    selfservice_permissions: SelfservicePermissionsModel = Field(
        alias="SelfservicePermissions"
    )


class ModifyWorkspaceAccessPropertiesRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    workspace_access_properties: WorkspaceAccessPropertiesModel = Field(
        alias="WorkspaceAccessProperties"
    )


class WorkspaceDirectoryModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    alias: Optional[str] = Field(default=None, alias="Alias")
    directory_name: Optional[str] = Field(default=None, alias="DirectoryName")
    registration_code: Optional[str] = Field(default=None, alias="RegistrationCode")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    dns_ip_addresses: Optional[List[str]] = Field(default=None, alias="DnsIpAddresses")
    customer_user_name: Optional[str] = Field(default=None, alias="CustomerUserName")
    iam_role_id: Optional[str] = Field(default=None, alias="IamRoleId")
    directory_type: Optional[Literal["AD_CONNECTOR", "SIMPLE_AD"]] = Field(
        default=None, alias="DirectoryType"
    )
    workspace_security_group_id: Optional[str] = Field(
        default=None, alias="WorkspaceSecurityGroupId"
    )
    state: Optional[
        Literal["DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"]
    ] = Field(default=None, alias="State")
    workspace_creation_properties: Optional[
        DefaultWorkspaceCreationPropertiesModel
    ] = Field(default=None, alias="WorkspaceCreationProperties")
    ip_group_ids: Optional[List[str]] = Field(default=None, alias="ipGroupIds")
    workspace_access_properties: Optional[WorkspaceAccessPropertiesModel] = Field(
        default=None, alias="WorkspaceAccessProperties"
    )
    tenancy: Optional[Literal["DEDICATED", "SHARED"]] = Field(
        default=None, alias="Tenancy"
    )
    selfservice_permissions: Optional[SelfservicePermissionsModel] = Field(
        default=None, alias="SelfservicePermissions"
    )
    saml_properties: Optional[SamlPropertiesModel] = Field(
        default=None, alias="SamlProperties"
    )
    certificate_based_auth_properties: Optional[
        CertificateBasedAuthPropertiesModel
    ] = Field(default=None, alias="CertificateBasedAuthProperties")


class ModifyWorkspaceCreationPropertiesRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    workspace_creation_properties: WorkspaceCreationPropertiesModel = Field(
        alias="WorkspaceCreationProperties"
    )


class ModifyWorkspacePropertiesRequestModel(BaseModel):
    workspace_id: str = Field(alias="WorkspaceId")
    workspace_properties: WorkspacePropertiesModel = Field(alias="WorkspaceProperties")


class WorkspaceRequestModel(BaseModel):
    directory_id: str = Field(alias="DirectoryId")
    user_name: str = Field(alias="UserName")
    bundle_id: str = Field(alias="BundleId")
    volume_encryption_key: Optional[str] = Field(
        default=None, alias="VolumeEncryptionKey"
    )
    user_volume_encryption_enabled: Optional[bool] = Field(
        default=None, alias="UserVolumeEncryptionEnabled"
    )
    root_volume_encryption_enabled: Optional[bool] = Field(
        default=None, alias="RootVolumeEncryptionEnabled"
    )
    workspace_properties: Optional[WorkspacePropertiesModel] = Field(
        default=None, alias="WorkspaceProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class RebootWorkspacesRequestModel(BaseModel):
    reboot_workspace_requests: Sequence[RebootRequestModel] = Field(
        alias="RebootWorkspaceRequests"
    )


class RebuildWorkspacesRequestModel(BaseModel):
    rebuild_workspace_requests: Sequence[RebuildRequestModel] = Field(
        alias="RebuildWorkspaceRequests"
    )


class WorkspaceModel(BaseModel):
    workspace_id: Optional[str] = Field(default=None, alias="WorkspaceId")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    state: Optional[
        Literal[
            "ADMIN_MAINTENANCE",
            "AVAILABLE",
            "ERROR",
            "IMPAIRED",
            "MAINTENANCE",
            "PENDING",
            "REBOOTING",
            "REBUILDING",
            "RESTORING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUSPENDED",
            "TERMINATED",
            "TERMINATING",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    bundle_id: Optional[str] = Field(default=None, alias="BundleId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    computer_name: Optional[str] = Field(default=None, alias="ComputerName")
    volume_encryption_key: Optional[str] = Field(
        default=None, alias="VolumeEncryptionKey"
    )
    user_volume_encryption_enabled: Optional[bool] = Field(
        default=None, alias="UserVolumeEncryptionEnabled"
    )
    root_volume_encryption_enabled: Optional[bool] = Field(
        default=None, alias="RootVolumeEncryptionEnabled"
    )
    workspace_properties: Optional[WorkspacePropertiesModel] = Field(
        default=None, alias="WorkspaceProperties"
    )
    modification_states: Optional[List[ModificationStateModel]] = Field(
        default=None, alias="ModificationStates"
    )
    related_workspaces: Optional[List[RelatedWorkspacePropertiesModel]] = Field(
        default=None, alias="RelatedWorkspaces"
    )


class StartWorkspacesRequestModel(BaseModel):
    start_workspace_requests: Sequence[StartRequestModel] = Field(
        alias="StartWorkspaceRequests"
    )


class StopWorkspacesRequestModel(BaseModel):
    stop_workspace_requests: Sequence[StopRequestModel] = Field(
        alias="StopWorkspaceRequests"
    )


class TerminateWorkspacesRequestModel(BaseModel):
    terminate_workspace_requests: Sequence[TerminateRequestModel] = Field(
        alias="TerminateWorkspaceRequests"
    )


class WorkspaceImageModel(BaseModel):
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    operating_system: Optional[OperatingSystemModel] = Field(
        default=None, alias="OperatingSystem"
    )
    state: Optional[Literal["AVAILABLE", "ERROR", "PENDING"]] = Field(
        default=None, alias="State"
    )
    required_tenancy: Optional[Literal["DEDICATED", "DEFAULT"]] = Field(
        default=None, alias="RequiredTenancy"
    )
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    created: Optional[datetime] = Field(default=None, alias="Created")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    updates: Optional[UpdateResultModel] = Field(default=None, alias="Updates")


class DescribeIpGroupsResultModel(BaseModel):
    result: List[WorkspacesIpGroupModel] = Field(alias="Result")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClientPropertiesResultModel(BaseModel):
    client_properties_list: List[ClientPropertiesResultModel] = Field(
        alias="ClientPropertiesList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectionAliasesResultModel(BaseModel):
    connection_aliases: List[ConnectionAliasModel] = Field(alias="ConnectionAliases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStandbyWorkspacesRequestModel(BaseModel):
    primary_region: str = Field(alias="PrimaryRegion")
    standby_workspaces: Sequence[StandbyWorkspaceModel] = Field(
        alias="StandbyWorkspaces"
    )


class FailedCreateStandbyWorkspacesRequestModel(BaseModel):
    standby_workspace_request: Optional[StandbyWorkspaceModel] = Field(
        default=None, alias="StandbyWorkspaceRequest"
    )
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class CreateWorkspaceBundleResultModel(BaseModel):
    workspace_bundle: WorkspaceBundleModel = Field(alias="WorkspaceBundle")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceBundlesResultModel(BaseModel):
    bundles: List[WorkspaceBundleModel] = Field(alias="Bundles")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceDirectoriesResultModel(BaseModel):
    directories: List[WorkspaceDirectoryModel] = Field(alias="Directories")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkspacesRequestModel(BaseModel):
    workspaces: Sequence[WorkspaceRequestModel] = Field(alias="Workspaces")


class FailedCreateWorkspaceRequestModel(BaseModel):
    workspace_request: Optional[WorkspaceRequestModel] = Field(
        default=None, alias="WorkspaceRequest"
    )
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class DescribeWorkspacesResultModel(BaseModel):
    workspaces: List[WorkspaceModel] = Field(alias="Workspaces")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceImagesResultModel(BaseModel):
    images: List[WorkspaceImageModel] = Field(alias="Images")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStandbyWorkspacesResultModel(BaseModel):
    failed_standby_requests: List[FailedCreateStandbyWorkspacesRequestModel] = Field(
        alias="FailedStandbyRequests"
    )
    pending_standby_requests: List[PendingCreateStandbyWorkspacesRequestModel] = Field(
        alias="PendingStandbyRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkspacesResultModel(BaseModel):
    failed_requests: List[FailedCreateWorkspaceRequestModel] = Field(
        alias="FailedRequests"
    )
    pending_requests: List[WorkspaceModel] = Field(alias="PendingRequests")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
