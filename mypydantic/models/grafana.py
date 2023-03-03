# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssertionAttributesModel(BaseModel):
    email: Optional[str] = Field(default=None, alias="email")
    groups: Optional[str] = Field(default=None, alias="groups")
    login: Optional[str] = Field(default=None, alias="login")
    name: Optional[str] = Field(default=None, alias="name")
    org: Optional[str] = Field(default=None, alias="org")
    role: Optional[str] = Field(default=None, alias="role")


class AssociateLicenseRequestModel(BaseModel):
    license_type: Literal["ENTERPRISE", "ENTERPRISE_FREE_TRIAL"] = Field(
        alias="licenseType"
    )
    workspace_id: str = Field(alias="workspaceId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AwsSsoAuthenticationModel(BaseModel):
    sso_client_id: Optional[str] = Field(default=None, alias="ssoClientId")


class AuthenticationSummaryModel(BaseModel):
    providers: List[Literal["AWS_SSO", "SAML"]] = Field(alias="providers")
    saml_configuration_status: Optional[
        Literal["CONFIGURED", "NOT_CONFIGURED"]
    ] = Field(default=None, alias="samlConfigurationStatus")


class CreateWorkspaceApiKeyRequestModel(BaseModel):
    key_name: str = Field(alias="keyName")
    key_role: str = Field(alias="keyRole")
    seconds_to_live: int = Field(alias="secondsToLive")
    workspace_id: str = Field(alias="workspaceId")


class NetworkAccessConfigurationModel(BaseModel):
    prefix_list_ids: List[str] = Field(alias="prefixListIds")
    vpce_ids: List[str] = Field(alias="vpceIds")


class VpcConfigurationModel(BaseModel):
    security_group_ids: List[str] = Field(alias="securityGroupIds")
    subnet_ids: List[str] = Field(alias="subnetIds")


class DeleteWorkspaceApiKeyRequestModel(BaseModel):
    key_name: str = Field(alias="keyName")
    workspace_id: str = Field(alias="workspaceId")


class DeleteWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DescribeWorkspaceAuthenticationRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DescribeWorkspaceConfigurationRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DescribeWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DisassociateLicenseRequestModel(BaseModel):
    license_type: Literal["ENTERPRISE", "ENTERPRISE_FREE_TRIAL"] = Field(
        alias="licenseType"
    )
    workspace_id: str = Field(alias="workspaceId")


class IdpMetadataModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="url")
    xml: Optional[str] = Field(default=None, alias="xml")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListPermissionsRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    group_id: Optional[str] = Field(default=None, alias="groupId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    user_id: Optional[str] = Field(default=None, alias="userId")
    user_type: Optional[Literal["SSO_GROUP", "SSO_USER"]] = Field(
        default=None, alias="userType"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListWorkspacesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UserModel(BaseModel):
    id: str = Field(alias="id")
    type: Literal["SSO_GROUP", "SSO_USER"] = Field(alias="type")


class RoleValuesModel(BaseModel):
    admin: Optional[List[str]] = Field(default=None, alias="admin")
    editor: Optional[List[str]] = Field(default=None, alias="editor")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateWorkspaceConfigurationRequestModel(BaseModel):
    configuration: str = Field(alias="configuration")
    workspace_id: str = Field(alias="workspaceId")


class CreateWorkspaceApiKeyResponseModel(BaseModel):
    key: str = Field(alias="key")
    key_name: str = Field(alias="keyName")
    workspace_id: str = Field(alias="workspaceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWorkspaceApiKeyResponseModel(BaseModel):
    key_name: str = Field(alias="keyName")
    workspace_id: str = Field(alias="workspaceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceConfigurationResponseModel(BaseModel):
    configuration: str = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkspaceSummaryModel(BaseModel):
    authentication: AuthenticationSummaryModel = Field(alias="authentication")
    created: datetime = Field(alias="created")
    endpoint: str = Field(alias="endpoint")
    grafana_version: str = Field(alias="grafanaVersion")
    id: str = Field(alias="id")
    modified: datetime = Field(alias="modified")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "CREATION_FAILED",
        "DELETING",
        "DELETION_FAILED",
        "FAILED",
        "LICENSE_REMOVAL_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
        "UPGRADE_FAILED",
        "UPGRADING",
    ] = Field(alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    notification_destinations: Optional[List[Literal["SNS"]]] = Field(
        default=None, alias="notificationDestinations"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateWorkspaceRequestModel(BaseModel):
    account_access_type: Literal["CURRENT_ACCOUNT", "ORGANIZATION"] = Field(
        alias="accountAccessType"
    )
    authentication_providers: Sequence[Literal["AWS_SSO", "SAML"]] = Field(
        alias="authenticationProviders"
    )
    permission_type: Literal["CUSTOMER_MANAGED", "SERVICE_MANAGED"] = Field(
        alias="permissionType"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    configuration: Optional[str] = Field(default=None, alias="configuration")
    network_access_control: Optional[NetworkAccessConfigurationModel] = Field(
        default=None, alias="networkAccessControl"
    )
    organization_role_name: Optional[str] = Field(
        default=None, alias="organizationRoleName"
    )
    stack_set_name: Optional[str] = Field(default=None, alias="stackSetName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="vpcConfiguration"
    )
    workspace_data_sources: Optional[
        Sequence[
            Literal[
                "AMAZON_OPENSEARCH_SERVICE",
                "ATHENA",
                "CLOUDWATCH",
                "PROMETHEUS",
                "REDSHIFT",
                "SITEWISE",
                "TIMESTREAM",
                "TWINMAKER",
                "XRAY",
            ]
        ]
    ] = Field(default=None, alias="workspaceDataSources")
    workspace_description: Optional[str] = Field(
        default=None, alias="workspaceDescription"
    )
    workspace_name: Optional[str] = Field(default=None, alias="workspaceName")
    workspace_notification_destinations: Optional[Sequence[Literal["SNS"]]] = Field(
        default=None, alias="workspaceNotificationDestinations"
    )
    workspace_organizational_units: Optional[Sequence[str]] = Field(
        default=None, alias="workspaceOrganizationalUnits"
    )
    workspace_role_arn: Optional[str] = Field(default=None, alias="workspaceRoleArn")


class UpdateWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    account_access_type: Optional[Literal["CURRENT_ACCOUNT", "ORGANIZATION"]] = Field(
        default=None, alias="accountAccessType"
    )
    network_access_control: Optional[NetworkAccessConfigurationModel] = Field(
        default=None, alias="networkAccessControl"
    )
    organization_role_name: Optional[str] = Field(
        default=None, alias="organizationRoleName"
    )
    permission_type: Optional[Literal["CUSTOMER_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="permissionType"
    )
    remove_network_access_configuration: Optional[bool] = Field(
        default=None, alias="removeNetworkAccessConfiguration"
    )
    remove_vpc_configuration: Optional[bool] = Field(
        default=None, alias="removeVpcConfiguration"
    )
    stack_set_name: Optional[str] = Field(default=None, alias="stackSetName")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="vpcConfiguration"
    )
    workspace_data_sources: Optional[
        Sequence[
            Literal[
                "AMAZON_OPENSEARCH_SERVICE",
                "ATHENA",
                "CLOUDWATCH",
                "PROMETHEUS",
                "REDSHIFT",
                "SITEWISE",
                "TIMESTREAM",
                "TWINMAKER",
                "XRAY",
            ]
        ]
    ] = Field(default=None, alias="workspaceDataSources")
    workspace_description: Optional[str] = Field(
        default=None, alias="workspaceDescription"
    )
    workspace_name: Optional[str] = Field(default=None, alias="workspaceName")
    workspace_notification_destinations: Optional[Sequence[Literal["SNS"]]] = Field(
        default=None, alias="workspaceNotificationDestinations"
    )
    workspace_organizational_units: Optional[Sequence[str]] = Field(
        default=None, alias="workspaceOrganizationalUnits"
    )
    workspace_role_arn: Optional[str] = Field(default=None, alias="workspaceRoleArn")


class WorkspaceDescriptionModel(BaseModel):
    authentication: AuthenticationSummaryModel = Field(alias="authentication")
    created: datetime = Field(alias="created")
    data_sources: List[
        Literal[
            "AMAZON_OPENSEARCH_SERVICE",
            "ATHENA",
            "CLOUDWATCH",
            "PROMETHEUS",
            "REDSHIFT",
            "SITEWISE",
            "TIMESTREAM",
            "TWINMAKER",
            "XRAY",
        ]
    ] = Field(alias="dataSources")
    endpoint: str = Field(alias="endpoint")
    grafana_version: str = Field(alias="grafanaVersion")
    id: str = Field(alias="id")
    modified: datetime = Field(alias="modified")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "CREATION_FAILED",
        "DELETING",
        "DELETION_FAILED",
        "FAILED",
        "LICENSE_REMOVAL_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
        "UPGRADE_FAILED",
        "UPGRADING",
    ] = Field(alias="status")
    account_access_type: Optional[Literal["CURRENT_ACCOUNT", "ORGANIZATION"]] = Field(
        default=None, alias="accountAccessType"
    )
    description: Optional[str] = Field(default=None, alias="description")
    free_trial_consumed: Optional[bool] = Field(default=None, alias="freeTrialConsumed")
    free_trial_expiration: Optional[datetime] = Field(
        default=None, alias="freeTrialExpiration"
    )
    license_expiration: Optional[datetime] = Field(
        default=None, alias="licenseExpiration"
    )
    license_type: Optional[Literal["ENTERPRISE", "ENTERPRISE_FREE_TRIAL"]] = Field(
        default=None, alias="licenseType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    network_access_control: Optional[NetworkAccessConfigurationModel] = Field(
        default=None, alias="networkAccessControl"
    )
    notification_destinations: Optional[List[Literal["SNS"]]] = Field(
        default=None, alias="notificationDestinations"
    )
    organization_role_name: Optional[str] = Field(
        default=None, alias="organizationRoleName"
    )
    organizational_units: Optional[List[str]] = Field(
        default=None, alias="organizationalUnits"
    )
    permission_type: Optional[Literal["CUSTOMER_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="permissionType"
    )
    stack_set_name: Optional[str] = Field(default=None, alias="stackSetName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="vpcConfiguration"
    )
    workspace_role_arn: Optional[str] = Field(default=None, alias="workspaceRoleArn")


class ListPermissionsRequestListPermissionsPaginateModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    group_id: Optional[str] = Field(default=None, alias="groupId")
    user_id: Optional[str] = Field(default=None, alias="userId")
    user_type: Optional[Literal["SSO_GROUP", "SSO_USER"]] = Field(
        default=None, alias="userType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkspacesRequestListWorkspacesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PermissionEntryModel(BaseModel):
    role: Literal["ADMIN", "EDITOR", "VIEWER"] = Field(alias="role")
    user: UserModel = Field(alias="user")


class UpdateInstructionModel(BaseModel):
    action: Literal["ADD", "REVOKE"] = Field(alias="action")
    role: Literal["ADMIN", "EDITOR", "VIEWER"] = Field(alias="role")
    users: Sequence[UserModel] = Field(alias="users")


class SamlConfigurationModel(BaseModel):
    idp_metadata: IdpMetadataModel = Field(alias="idpMetadata")
    allowed_organizations: Optional[List[str]] = Field(
        default=None, alias="allowedOrganizations"
    )
    assertion_attributes: Optional[AssertionAttributesModel] = Field(
        default=None, alias="assertionAttributes"
    )
    login_validity_duration: Optional[int] = Field(
        default=None, alias="loginValidityDuration"
    )
    role_values: Optional[RoleValuesModel] = Field(default=None, alias="roleValues")


class ListWorkspacesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workspaces: List[WorkspaceSummaryModel] = Field(alias="workspaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateLicenseResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkspaceResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWorkspaceResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateLicenseResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkspaceResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    permissions: List[PermissionEntryModel] = Field(alias="permissions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateErrorModel(BaseModel):
    caused_by: UpdateInstructionModel = Field(alias="causedBy")
    code: int = Field(alias="code")
    message: str = Field(alias="message")


class UpdatePermissionsRequestModel(BaseModel):
    update_instruction_batch: Sequence[UpdateInstructionModel] = Field(
        alias="updateInstructionBatch"
    )
    workspace_id: str = Field(alias="workspaceId")


class SamlAuthenticationModel(BaseModel):
    status: Literal["CONFIGURED", "NOT_CONFIGURED"] = Field(alias="status")
    configuration: Optional[SamlConfigurationModel] = Field(
        default=None, alias="configuration"
    )


class UpdateWorkspaceAuthenticationRequestModel(BaseModel):
    authentication_providers: Sequence[Literal["AWS_SSO", "SAML"]] = Field(
        alias="authenticationProviders"
    )
    workspace_id: str = Field(alias="workspaceId")
    saml_configuration: Optional[SamlConfigurationModel] = Field(
        default=None, alias="samlConfiguration"
    )


class UpdatePermissionsResponseModel(BaseModel):
    errors: List[UpdateErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthenticationDescriptionModel(BaseModel):
    providers: List[Literal["AWS_SSO", "SAML"]] = Field(alias="providers")
    aws_sso: Optional[AwsSsoAuthenticationModel] = Field(default=None, alias="awsSso")
    saml: Optional[SamlAuthenticationModel] = Field(default=None, alias="saml")


class DescribeWorkspaceAuthenticationResponseModel(BaseModel):
    authentication: AuthenticationDescriptionModel = Field(alias="authentication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkspaceAuthenticationResponseModel(BaseModel):
    authentication: AuthenticationDescriptionModel = Field(alias="authentication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
