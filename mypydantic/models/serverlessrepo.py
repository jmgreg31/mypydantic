# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationDependencySummaryModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    semantic_version: str = Field(alias="SemanticVersion")


class ApplicationPolicyStatementModel(BaseModel):
    actions: List[str] = Field(alias="Actions")
    principals: List[str] = Field(alias="Principals")
    principal_org_ids: Optional[List[str]] = Field(
        default=None, alias="PrincipalOrgIDs"
    )
    statement_id: Optional[str] = Field(default=None, alias="StatementId")


class ApplicationSummaryModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    author: str = Field(alias="Author")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    home_page_url: Optional[str] = Field(default=None, alias="HomePageUrl")
    labels: Optional[List[str]] = Field(default=None, alias="Labels")
    spdx_license_id: Optional[str] = Field(default=None, alias="SpdxLicenseId")


class CreateApplicationRequestModel(BaseModel):
    author: str = Field(alias="Author")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    home_page_url: Optional[str] = Field(default=None, alias="HomePageUrl")
    labels: Optional[Sequence[str]] = Field(default=None, alias="Labels")
    license_body: Optional[str] = Field(default=None, alias="LicenseBody")
    license_url: Optional[str] = Field(default=None, alias="LicenseUrl")
    readme_body: Optional[str] = Field(default=None, alias="ReadmeBody")
    readme_url: Optional[str] = Field(default=None, alias="ReadmeUrl")
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")
    source_code_archive_url: Optional[str] = Field(
        default=None, alias="SourceCodeArchiveUrl"
    )
    source_code_url: Optional[str] = Field(default=None, alias="SourceCodeUrl")
    spdx_license_id: Optional[str] = Field(default=None, alias="SpdxLicenseId")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateUrl")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateApplicationVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    semantic_version: str = Field(alias="SemanticVersion")
    source_code_archive_url: Optional[str] = Field(
        default=None, alias="SourceCodeArchiveUrl"
    )
    source_code_url: Optional[str] = Field(default=None, alias="SourceCodeUrl")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateUrl")


class ParameterDefinitionModel(BaseModel):
    name: str = Field(alias="Name")
    referenced_by_resources: List[str] = Field(alias="ReferencedByResources")
    allowed_pattern: Optional[str] = Field(default=None, alias="AllowedPattern")
    allowed_values: Optional[List[str]] = Field(default=None, alias="AllowedValues")
    constraint_description: Optional[str] = Field(
        default=None, alias="ConstraintDescription"
    )
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    description: Optional[str] = Field(default=None, alias="Description")
    max_length: Optional[int] = Field(default=None, alias="MaxLength")
    max_value: Optional[int] = Field(default=None, alias="MaxValue")
    min_length: Optional[int] = Field(default=None, alias="MinLength")
    min_value: Optional[int] = Field(default=None, alias="MinValue")
    no_echo: Optional[bool] = Field(default=None, alias="NoEcho")
    type: Optional[str] = Field(default=None, alias="Type")


class ParameterValueModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateCloudFormationTemplateRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApplicationPolicyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")


class GetCloudFormationTemplateRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    template_id: str = Field(alias="TemplateId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationDependenciesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")


class ListApplicationVersionsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VersionSummaryModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_time: str = Field(alias="CreationTime")
    semantic_version: str = Field(alias="SemanticVersion")
    source_code_url: Optional[str] = Field(default=None, alias="SourceCodeUrl")


class ListApplicationsRequestModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RollbackTriggerModel(BaseModel):
    arn: str = Field(alias="Arn")
    type: str = Field(alias="Type")


class UnshareApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    organization_id: str = Field(alias="OrganizationId")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    author: Optional[str] = Field(default=None, alias="Author")
    description: Optional[str] = Field(default=None, alias="Description")
    home_page_url: Optional[str] = Field(default=None, alias="HomePageUrl")
    labels: Optional[Sequence[str]] = Field(default=None, alias="Labels")
    readme_body: Optional[str] = Field(default=None, alias="ReadmeBody")
    readme_url: Optional[str] = Field(default=None, alias="ReadmeUrl")


class PutApplicationPolicyRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    statements: Sequence[ApplicationPolicyStatementModel] = Field(alias="Statements")


class CreateCloudFormationChangeSetResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    change_set_id: str = Field(alias="ChangeSetId")
    semantic_version: str = Field(alias="SemanticVersion")
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCloudFormationTemplateResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_time: str = Field(alias="CreationTime")
    expiration_time: str = Field(alias="ExpirationTime")
    semantic_version: str = Field(alias="SemanticVersion")
    status: Literal["ACTIVE", "EXPIRED", "PREPARING"] = Field(alias="Status")
    template_id: str = Field(alias="TemplateId")
    template_url: str = Field(alias="TemplateUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationPolicyResponseModel(BaseModel):
    statements: List[ApplicationPolicyStatementModel] = Field(alias="Statements")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCloudFormationTemplateResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_time: str = Field(alias="CreationTime")
    expiration_time: str = Field(alias="ExpirationTime")
    semantic_version: str = Field(alias="SemanticVersion")
    status: Literal["ACTIVE", "EXPIRED", "PREPARING"] = Field(alias="Status")
    template_id: str = Field(alias="TemplateId")
    template_url: str = Field(alias="TemplateUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationDependenciesResponseModel(BaseModel):
    dependencies: List[ApplicationDependencySummaryModel] = Field(alias="Dependencies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    applications: List[ApplicationSummaryModel] = Field(alias="Applications")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutApplicationPolicyResponseModel(BaseModel):
    statements: List[ApplicationPolicyStatementModel] = Field(alias="Statements")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationVersionResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_time: str = Field(alias="CreationTime")
    parameter_definitions: List[ParameterDefinitionModel] = Field(
        alias="ParameterDefinitions"
    )
    required_capabilities: List[
        Literal[
            "CAPABILITY_AUTO_EXPAND",
            "CAPABILITY_IAM",
            "CAPABILITY_NAMED_IAM",
            "CAPABILITY_RESOURCE_POLICY",
        ]
    ] = Field(alias="RequiredCapabilities")
    resources_supported: bool = Field(alias="ResourcesSupported")
    semantic_version: str = Field(alias="SemanticVersion")
    source_code_archive_url: str = Field(alias="SourceCodeArchiveUrl")
    source_code_url: str = Field(alias="SourceCodeUrl")
    template_url: str = Field(alias="TemplateUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VersionModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    creation_time: str = Field(alias="CreationTime")
    parameter_definitions: List[ParameterDefinitionModel] = Field(
        alias="ParameterDefinitions"
    )
    required_capabilities: List[
        Literal[
            "CAPABILITY_AUTO_EXPAND",
            "CAPABILITY_IAM",
            "CAPABILITY_NAMED_IAM",
            "CAPABILITY_RESOURCE_POLICY",
        ]
    ] = Field(alias="RequiredCapabilities")
    resources_supported: bool = Field(alias="ResourcesSupported")
    semantic_version: str = Field(alias="SemanticVersion")
    template_url: str = Field(alias="TemplateUrl")
    source_code_archive_url: Optional[str] = Field(
        default=None, alias="SourceCodeArchiveUrl"
    )
    source_code_url: Optional[str] = Field(default=None, alias="SourceCodeUrl")


class ListApplicationDependenciesRequestListApplicationDependenciesPaginateModel(
    BaseModel
):
    application_id: str = Field(alias="ApplicationId")
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationVersionsRequestListApplicationVersionsPaginateModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionSummaryModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackConfigurationModel(BaseModel):
    monitoring_time_in_minutes: Optional[int] = Field(
        default=None, alias="MonitoringTimeInMinutes"
    )
    rollback_triggers: Optional[Sequence[RollbackTriggerModel]] = Field(
        default=None, alias="RollbackTriggers"
    )


class CreateApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    author: str = Field(alias="Author")
    creation_time: str = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    home_page_url: str = Field(alias="HomePageUrl")
    is_verified_author: bool = Field(alias="IsVerifiedAuthor")
    labels: List[str] = Field(alias="Labels")
    license_url: str = Field(alias="LicenseUrl")
    name: str = Field(alias="Name")
    readme_url: str = Field(alias="ReadmeUrl")
    spdx_license_id: str = Field(alias="SpdxLicenseId")
    verified_author_url: str = Field(alias="VerifiedAuthorUrl")
    version: VersionModel = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    author: str = Field(alias="Author")
    creation_time: str = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    home_page_url: str = Field(alias="HomePageUrl")
    is_verified_author: bool = Field(alias="IsVerifiedAuthor")
    labels: List[str] = Field(alias="Labels")
    license_url: str = Field(alias="LicenseUrl")
    name: str = Field(alias="Name")
    readme_url: str = Field(alias="ReadmeUrl")
    spdx_license_id: str = Field(alias="SpdxLicenseId")
    verified_author_url: str = Field(alias="VerifiedAuthorUrl")
    version: VersionModel = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    author: str = Field(alias="Author")
    creation_time: str = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    home_page_url: str = Field(alias="HomePageUrl")
    is_verified_author: bool = Field(alias="IsVerifiedAuthor")
    labels: List[str] = Field(alias="Labels")
    license_url: str = Field(alias="LicenseUrl")
    name: str = Field(alias="Name")
    readme_url: str = Field(alias="ReadmeUrl")
    spdx_license_id: str = Field(alias="SpdxLicenseId")
    verified_author_url: str = Field(alias="VerifiedAuthorUrl")
    version: VersionModel = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCloudFormationChangeSetRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    stack_name: str = Field(alias="StackName")
    capabilities: Optional[Sequence[str]] = Field(default=None, alias="Capabilities")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationArns"
    )
    parameter_overrides: Optional[Sequence[ParameterValueModel]] = Field(
        default=None, alias="ParameterOverrides"
    )
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    semantic_version: Optional[str] = Field(default=None, alias="SemanticVersion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
