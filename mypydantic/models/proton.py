# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptEnvironmentAccountConnectionInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class EnvironmentAccountConnectionModel(BaseModel):
    arn: str = Field(alias="arn")
    environment_account_id: str = Field(alias="environmentAccountId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    management_account_id: str = Field(alias="managementAccountId")
    requested_at: datetime = Field(alias="requestedAt")
    role_arn: str = Field(alias="roleArn")
    status: Literal["CONNECTED", "PENDING", "REJECTED"] = Field(alias="status")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class RepositoryBranchModel(BaseModel):
    arn: str = Field(alias="arn")
    branch: str = Field(alias="branch")
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )


class CancelComponentDeploymentInputRequestModel(BaseModel):
    component_name: str = Field(alias="componentName")


class ComponentModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    environment_name: str = Field(alias="environmentName")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    description: Optional[str] = Field(default=None, alias="description")
    last_deployment_attempted_at: Optional[datetime] = Field(
        default=None, alias="lastDeploymentAttemptedAt"
    )
    last_deployment_succeeded_at: Optional[datetime] = Field(
        default=None, alias="lastDeploymentSucceededAt"
    )
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    service_spec: Optional[str] = Field(default=None, alias="serviceSpec")


class CancelEnvironmentDeploymentInputRequestModel(BaseModel):
    environment_name: str = Field(alias="environmentName")


class CancelServiceInstanceDeploymentInputRequestModel(BaseModel):
    service_instance_name: str = Field(alias="serviceInstanceName")
    service_name: str = Field(alias="serviceName")


class ServiceInstanceModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    environment_name: str = Field(alias="environmentName")
    last_deployment_attempted_at: datetime = Field(alias="lastDeploymentAttemptedAt")
    last_deployment_succeeded_at: datetime = Field(alias="lastDeploymentSucceededAt")
    name: str = Field(alias="name")
    service_name: str = Field(alias="serviceName")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_minor_version: str = Field(alias="templateMinorVersion")
    template_name: str = Field(alias="templateName")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    spec: Optional[str] = Field(default=None, alias="spec")


class CancelServicePipelineDeploymentInputRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")


class ServicePipelineModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    last_deployment_attempted_at: datetime = Field(alias="lastDeploymentAttemptedAt")
    last_deployment_succeeded_at: datetime = Field(alias="lastDeploymentSucceededAt")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_minor_version: str = Field(alias="templateMinorVersion")
    template_name: str = Field(alias="templateName")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    spec: Optional[str] = Field(default=None, alias="spec")


class CompatibleEnvironmentTemplateInputModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    template_name: str = Field(alias="templateName")


class CompatibleEnvironmentTemplateModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    template_name: str = Field(alias="templateName")


class ComponentSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    environment_name: str = Field(alias="environmentName")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    last_deployment_attempted_at: Optional[datetime] = Field(
        default=None, alias="lastDeploymentAttemptedAt"
    )
    last_deployment_succeeded_at: Optional[datetime] = Field(
        default=None, alias="lastDeploymentSucceededAt"
    )
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class ResourceCountsSummaryModel(BaseModel):
    total: int = Field(alias="total")
    behind_major: Optional[int] = Field(default=None, alias="behindMajor")
    behind_minor: Optional[int] = Field(default=None, alias="behindMinor")
    failed: Optional[int] = Field(default=None, alias="failed")
    up_to_date: Optional[int] = Field(default=None, alias="upToDate")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class RepositoryBranchInputModel(BaseModel):
    branch: str = Field(alias="branch")
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )


class EnvironmentTemplateModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="provisioning"
    )
    recommended_version: Optional[str] = Field(default=None, alias="recommendedVersion")


class EnvironmentTemplateVersionModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    status: Literal[
        "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    recommended_minor_version: Optional[str] = Field(
        default=None, alias="recommendedMinorVersion"
    )
    schema_: Optional[str] = Field(default=None, alias="schema")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class RepositoryModel(BaseModel):
    arn: str = Field(alias="arn")
    connection_arn: str = Field(alias="connectionArn")
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")


class ServiceTemplateModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    pipeline_provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="pipelineProvisioning"
    )
    recommended_version: Optional[str] = Field(default=None, alias="recommendedVersion")


class CreateTemplateSyncConfigInputRequestModel(BaseModel):
    branch: str = Field(alias="branch")
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")
    subdirectory: Optional[str] = Field(default=None, alias="subdirectory")


class TemplateSyncConfigModel(BaseModel):
    branch: str = Field(alias="branch")
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")
    subdirectory: Optional[str] = Field(default=None, alias="subdirectory")


class DeleteComponentInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteEnvironmentAccountConnectionInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteEnvironmentTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteEnvironmentTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")


class DeleteRepositoryInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )


class DeleteServiceInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteServiceTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteServiceTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")


class DeleteTemplateSyncConfigInputRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")


class EnvironmentAccountConnectionSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    environment_account_id: str = Field(alias="environmentAccountId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    management_account_id: str = Field(alias="managementAccountId")
    requested_at: datetime = Field(alias="requestedAt")
    role_arn: str = Field(alias="roleArn")
    status: Literal["CONNECTED", "PENDING", "REJECTED"] = Field(alias="status")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")


class EnvironmentSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    last_deployment_attempted_at: datetime = Field(alias="lastDeploymentAttemptedAt")
    last_deployment_succeeded_at: datetime = Field(alias="lastDeploymentSucceededAt")
    name: str = Field(alias="name")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_minor_version: str = Field(alias="templateMinorVersion")
    template_name: str = Field(alias="templateName")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    description: Optional[str] = Field(default=None, alias="description")
    environment_account_connection_id: Optional[str] = Field(
        default=None, alias="environmentAccountConnectionId"
    )
    environment_account_id: Optional[str] = Field(
        default=None, alias="environmentAccountId"
    )
    proton_service_role_arn: Optional[str] = Field(
        default=None, alias="protonServiceRoleArn"
    )
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="provisioning"
    )


class EnvironmentTemplateFilterModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    template_name: str = Field(alias="templateName")


class EnvironmentTemplateSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="provisioning"
    )
    recommended_version: Optional[str] = Field(default=None, alias="recommendedVersion")


class EnvironmentTemplateVersionSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    status: Literal[
        "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    recommended_minor_version: Optional[str] = Field(
        default=None, alias="recommendedMinorVersion"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetComponentInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetEnvironmentAccountConnectionInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetEnvironmentTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetEnvironmentTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")


class GetRepositoryInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )


class GetRepositorySyncStatusInputRequestModel(BaseModel):
    branch: str = Field(alias="branch")
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    sync_type: Literal["TEMPLATE_SYNC"] = Field(alias="syncType")


class GetServiceInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetServiceInstanceInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    service_name: str = Field(alias="serviceName")


class GetServiceTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetServiceTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")


class GetTemplateSyncConfigInputRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")


class GetTemplateSyncStatusInputRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")
    template_version: str = Field(alias="templateVersion")


class RevisionModel(BaseModel):
    branch: str = Field(alias="branch")
    directory: str = Field(alias="directory")
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    sha: str = Field(alias="sha")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListComponentOutputsInputRequestModel(BaseModel):
    component_name: str = Field(alias="componentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class OutputModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value_string: Optional[str] = Field(default=None, alias="valueString")


class ListComponentProvisionedResourcesInputRequestModel(BaseModel):
    component_name: str = Field(alias="componentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ProvisionedResourceModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="identifier")
    name: Optional[str] = Field(default=None, alias="name")
    provisioning_engine: Optional[Literal["CLOUDFORMATION", "TERRAFORM"]] = Field(
        default=None, alias="provisioningEngine"
    )


class ListComponentsInputRequestModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class ListEnvironmentAccountConnectionsInputRequestModel(BaseModel):
    requested_by: Literal["ENVIRONMENT_ACCOUNT", "MANAGEMENT_ACCOUNT"] = Field(
        alias="requestedBy"
    )
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    statuses: Optional[Sequence[Literal["CONNECTED", "PENDING", "REJECTED"]]] = Field(
        default=None, alias="statuses"
    )


class ListEnvironmentOutputsInputRequestModel(BaseModel):
    environment_name: str = Field(alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEnvironmentProvisionedResourcesInputRequestModel(BaseModel):
    environment_name: str = Field(alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEnvironmentTemplateVersionsInputRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEnvironmentTemplatesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRepositoriesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RepositorySummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )


class ListRepositorySyncDefinitionsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    sync_type: Literal["TEMPLATE_SYNC"] = Field(alias="syncType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RepositorySyncDefinitionModel(BaseModel):
    branch: str = Field(alias="branch")
    directory: str = Field(alias="directory")
    parent: str = Field(alias="parent")
    target: str = Field(alias="target")


class ListServiceInstanceOutputsInputRequestModel(BaseModel):
    service_instance_name: str = Field(alias="serviceInstanceName")
    service_name: str = Field(alias="serviceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListServiceInstanceProvisionedResourcesInputRequestModel(BaseModel):
    service_instance_name: str = Field(alias="serviceInstanceName")
    service_name: str = Field(alias="serviceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListServiceInstancesFilterModel(BaseModel):
    key: Optional[
        Literal[
            "createdAtAfter",
            "createdAtBefore",
            "deployedTemplateVersionStatus",
            "deploymentStatus",
            "environmentName",
            "lastDeploymentAttemptedAtAfter",
            "lastDeploymentAttemptedAtBefore",
            "name",
            "serviceName",
            "templateName",
        ]
    ] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ServiceInstanceSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    environment_name: str = Field(alias="environmentName")
    last_deployment_attempted_at: datetime = Field(alias="lastDeploymentAttemptedAt")
    last_deployment_succeeded_at: datetime = Field(alias="lastDeploymentSucceededAt")
    name: str = Field(alias="name")
    service_name: str = Field(alias="serviceName")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_minor_version: str = Field(alias="templateMinorVersion")
    template_name: str = Field(alias="templateName")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )


class ListServicePipelineOutputsInputRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListServicePipelineProvisionedResourcesInputRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListServiceTemplateVersionsInputRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ServiceTemplateVersionSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    status: Literal[
        "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    recommended_minor_version: Optional[str] = Field(
        default=None, alias="recommendedMinorVersion"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ListServiceTemplatesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ServiceTemplateSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    pipeline_provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="pipelineProvisioning"
    )
    recommended_version: Optional[str] = Field(default=None, alias="recommendedVersion")


class ListServicesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ServiceSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_FAILED_CLEANUP_COMPLETE",
        "CREATE_FAILED_CLEANUP_FAILED",
        "CREATE_FAILED_CLEANUP_IN_PROGRESS",
        "CREATE_IN_PROGRESS",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_COMPLETE_CLEANUP_FAILED",
        "UPDATE_FAILED",
        "UPDATE_FAILED_CLEANUP_COMPLETE",
        "UPDATE_FAILED_CLEANUP_FAILED",
        "UPDATE_FAILED_CLEANUP_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RejectEnvironmentAccountConnectionInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class RepositorySyncEventModel(BaseModel):
    event: str = Field(alias="event")
    time: datetime = Field(alias="time")
    type: str = Field(alias="type")
    external_id: Optional[str] = Field(default=None, alias="externalId")


class ResourceSyncEventModel(BaseModel):
    event: str = Field(alias="event")
    time: datetime = Field(alias="time")
    type: str = Field(alias="type")
    external_id: Optional[str] = Field(default=None, alias="externalId")


class S3ObjectSourceModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateComponentInputRequestModel(BaseModel):
    deployment_type: Literal["CURRENT_VERSION", "NONE"] = Field(alias="deploymentType")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    service_spec: Optional[str] = Field(default=None, alias="serviceSpec")
    template_file: Optional[str] = Field(default=None, alias="templateFile")


class UpdateEnvironmentAccountConnectionInputRequestModel(BaseModel):
    id: str = Field(alias="id")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class UpdateEnvironmentTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")


class UpdateEnvironmentTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[
        Literal["DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"]
    ] = Field(default=None, alias="status")


class UpdateServiceInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    spec: Optional[str] = Field(default=None, alias="spec")


class UpdateServiceInstanceInputRequestModel(BaseModel):
    deployment_type: Literal[
        "CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"
    ] = Field(alias="deploymentType")
    name: str = Field(alias="name")
    service_name: str = Field(alias="serviceName")
    spec: Optional[str] = Field(default=None, alias="spec")
    template_major_version: Optional[str] = Field(
        default=None, alias="templateMajorVersion"
    )
    template_minor_version: Optional[str] = Field(
        default=None, alias="templateMinorVersion"
    )


class UpdateServicePipelineInputRequestModel(BaseModel):
    deployment_type: Literal[
        "CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"
    ] = Field(alias="deploymentType")
    service_name: str = Field(alias="serviceName")
    spec: str = Field(alias="spec")
    template_major_version: Optional[str] = Field(
        default=None, alias="templateMajorVersion"
    )
    template_minor_version: Optional[str] = Field(
        default=None, alias="templateMinorVersion"
    )


class UpdateServiceTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")


class UpdateTemplateSyncConfigInputRequestModel(BaseModel):
    branch: str = Field(alias="branch")
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    template_name: str = Field(alias="templateName")
    template_type: Literal["ENVIRONMENT", "SERVICE"] = Field(alias="templateType")
    subdirectory: Optional[str] = Field(default=None, alias="subdirectory")


class AcceptEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentAccountConnectionOutputModel(BaseModel):
    environment_account_connection: EnvironmentAccountConnectionModel = Field(
        alias="environmentAccountConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccountSettingsModel(BaseModel):
    pipeline_codebuild_role_arn: Optional[str] = Field(
        default=None, alias="pipelineCodebuildRoleArn"
    )
    pipeline_provisioning_repository: Optional[RepositoryBranchModel] = Field(
        default=None, alias="pipelineProvisioningRepository"
    )
    pipeline_service_role_arn: Optional[str] = Field(
        default=None, alias="pipelineServiceRoleArn"
    )


class EnvironmentModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deployment_status: Literal[
        "CANCELLED",
        "CANCELLING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "IN_PROGRESS",
        "SUCCEEDED",
    ] = Field(alias="deploymentStatus")
    last_deployment_attempted_at: datetime = Field(alias="lastDeploymentAttemptedAt")
    last_deployment_succeeded_at: datetime = Field(alias="lastDeploymentSucceededAt")
    name: str = Field(alias="name")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_minor_version: str = Field(alias="templateMinorVersion")
    template_name: str = Field(alias="templateName")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="deploymentStatusMessage"
    )
    description: Optional[str] = Field(default=None, alias="description")
    environment_account_connection_id: Optional[str] = Field(
        default=None, alias="environmentAccountConnectionId"
    )
    environment_account_id: Optional[str] = Field(
        default=None, alias="environmentAccountId"
    )
    proton_service_role_arn: Optional[str] = Field(
        default=None, alias="protonServiceRoleArn"
    )
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="provisioning"
    )
    provisioning_repository: Optional[RepositoryBranchModel] = Field(
        default=None, alias="provisioningRepository"
    )
    spec: Optional[str] = Field(default=None, alias="spec")


class CancelComponentDeploymentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateComponentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteComponentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateComponentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelServiceInstanceDeploymentOutputModel(BaseModel):
    service_instance: ServiceInstanceModel = Field(alias="serviceInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceInstanceOutputModel(BaseModel):
    service_instance: ServiceInstanceModel = Field(alias="serviceInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceInstanceOutputModel(BaseModel):
    service_instance: ServiceInstanceModel = Field(alias="serviceInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelServicePipelineDeploymentOutputModel(BaseModel):
    pipeline: ServicePipelineModel = Field(alias="pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServiceModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    name: str = Field(alias="name")
    spec: str = Field(alias="spec")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_FAILED_CLEANUP_COMPLETE",
        "CREATE_FAILED_CLEANUP_FAILED",
        "CREATE_FAILED_CLEANUP_IN_PROGRESS",
        "CREATE_IN_PROGRESS",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_COMPLETE_CLEANUP_FAILED",
        "UPDATE_FAILED",
        "UPDATE_FAILED_CLEANUP_COMPLETE",
        "UPDATE_FAILED_CLEANUP_FAILED",
        "UPDATE_FAILED_CLEANUP_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    branch_name: Optional[str] = Field(default=None, alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")
    pipeline: Optional[ServicePipelineModel] = Field(default=None, alias="pipeline")
    repository_connection_arn: Optional[str] = Field(
        default=None, alias="repositoryConnectionArn"
    )
    repository_id: Optional[str] = Field(default=None, alias="repositoryId")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class UpdateServicePipelineOutputModel(BaseModel):
    pipeline: ServicePipelineModel = Field(alias="pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceTemplateVersionInputRequestModel(BaseModel):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")
    compatible_environment_templates: Optional[
        Sequence[CompatibleEnvironmentTemplateInputModel]
    ] = Field(default=None, alias="compatibleEnvironmentTemplates")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[
        Literal["DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"]
    ] = Field(default=None, alias="status")
    supported_component_sources: Optional[
        Sequence[Literal["DIRECTLY_DEFINED"]]
    ] = Field(default=None, alias="supportedComponentSources")


class ServiceTemplateVersionModel(BaseModel):
    arn: str = Field(alias="arn")
    compatible_environment_templates: List[CompatibleEnvironmentTemplateModel] = Field(
        alias="compatibleEnvironmentTemplates"
    )
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    status: Literal[
        "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
    ] = Field(alias="status")
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    recommended_minor_version: Optional[str] = Field(
        default=None, alias="recommendedMinorVersion"
    )
    schema_: Optional[str] = Field(default=None, alias="schema")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    supported_component_sources: Optional[List[Literal["DIRECTLY_DEFINED"]]] = Field(
        default=None, alias="supportedComponentSources"
    )


class ListComponentsOutputModel(BaseModel):
    components: List[ComponentSummaryModel] = Field(alias="components")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CountsSummaryModel(BaseModel):
    components: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="components"
    )
    environment_templates: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="environmentTemplates"
    )
    environments: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="environments"
    )
    pipelines: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="pipelines"
    )
    service_instances: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="serviceInstances"
    )
    service_templates: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="serviceTemplates"
    )
    services: Optional[ResourceCountsSummaryModel] = Field(
        default=None, alias="services"
    )


class CreateComponentInputRequestModel(BaseModel):
    manifest: str = Field(alias="manifest")
    name: str = Field(alias="name")
    template_file: str = Field(alias="templateFile")
    description: Optional[str] = Field(default=None, alias="description")
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    service_spec: Optional[str] = Field(default=None, alias="serviceSpec")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateEnvironmentAccountConnectionInputRequestModel(BaseModel):
    environment_name: str = Field(alias="environmentName")
    management_account_id: str = Field(alias="managementAccountId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateEnvironmentTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="provisioning"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRepositoryInputRequestModel(BaseModel):
    connection_arn: str = Field(alias="connectionArn")
    name: str = Field(alias="name")
    provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="provider"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateServiceInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    spec: str = Field(alias="spec")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_name: str = Field(alias="templateName")
    branch_name: Optional[str] = Field(default=None, alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")
    repository_connection_arn: Optional[str] = Field(
        default=None, alias="repositoryConnectionArn"
    )
    repository_id: Optional[str] = Field(default=None, alias="repositoryId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    template_minor_version: Optional[str] = Field(
        default=None, alias="templateMinorVersion"
    )


class CreateServiceTemplateInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    pipeline_provisioning: Optional[Literal["CUSTOMER_MANAGED"]] = Field(
        default=None, alias="pipelineProvisioning"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    spec: str = Field(alias="spec")
    template_major_version: str = Field(alias="templateMajorVersion")
    template_name: str = Field(alias="templateName")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    description: Optional[str] = Field(default=None, alias="description")
    environment_account_connection_id: Optional[str] = Field(
        default=None, alias="environmentAccountConnectionId"
    )
    proton_service_role_arn: Optional[str] = Field(
        default=None, alias="protonServiceRoleArn"
    )
    provisioning_repository: Optional[RepositoryBranchInputModel] = Field(
        default=None, alias="provisioningRepository"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    template_minor_version: Optional[str] = Field(
        default=None, alias="templateMinorVersion"
    )


class UpdateAccountSettingsInputRequestModel(BaseModel):
    delete_pipeline_provisioning_repository: Optional[bool] = Field(
        default=None, alias="deletePipelineProvisioningRepository"
    )
    pipeline_codebuild_role_arn: Optional[str] = Field(
        default=None, alias="pipelineCodebuildRoleArn"
    )
    pipeline_provisioning_repository: Optional[RepositoryBranchInputModel] = Field(
        default=None, alias="pipelineProvisioningRepository"
    )
    pipeline_service_role_arn: Optional[str] = Field(
        default=None, alias="pipelineServiceRoleArn"
    )


class UpdateEnvironmentInputRequestModel(BaseModel):
    deployment_type: Literal[
        "CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"
    ] = Field(alias="deploymentType")
    name: str = Field(alias="name")
    codebuild_role_arn: Optional[str] = Field(default=None, alias="codebuildRoleArn")
    component_role_arn: Optional[str] = Field(default=None, alias="componentRoleArn")
    description: Optional[str] = Field(default=None, alias="description")
    environment_account_connection_id: Optional[str] = Field(
        default=None, alias="environmentAccountConnectionId"
    )
    proton_service_role_arn: Optional[str] = Field(
        default=None, alias="protonServiceRoleArn"
    )
    provisioning_repository: Optional[RepositoryBranchInputModel] = Field(
        default=None, alias="provisioningRepository"
    )
    spec: Optional[str] = Field(default=None, alias="spec")
    template_major_version: Optional[str] = Field(
        default=None, alias="templateMajorVersion"
    )
    template_minor_version: Optional[str] = Field(
        default=None, alias="templateMinorVersion"
    )


class CreateEnvironmentTemplateOutputModel(BaseModel):
    environment_template: EnvironmentTemplateModel = Field(alias="environmentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEnvironmentTemplateOutputModel(BaseModel):
    environment_template: EnvironmentTemplateModel = Field(alias="environmentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentTemplateOutputModel(BaseModel):
    environment_template: EnvironmentTemplateModel = Field(alias="environmentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentTemplateOutputModel(BaseModel):
    environment_template: EnvironmentTemplateModel = Field(alias="environmentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentTemplateVersionOutputModel(BaseModel):
    environment_template_version: EnvironmentTemplateVersionModel = Field(
        alias="environmentTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEnvironmentTemplateVersionOutputModel(BaseModel):
    environment_template_version: EnvironmentTemplateVersionModel = Field(
        alias="environmentTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentTemplateVersionOutputModel(BaseModel):
    environment_template_version: EnvironmentTemplateVersionModel = Field(
        alias="environmentTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentTemplateVersionOutputModel(BaseModel):
    environment_template_version: EnvironmentTemplateVersionModel = Field(
        alias="environmentTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryOutputModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryOutputModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryOutputModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceTemplateOutputModel(BaseModel):
    service_template: ServiceTemplateModel = Field(alias="serviceTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceTemplateOutputModel(BaseModel):
    service_template: ServiceTemplateModel = Field(alias="serviceTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceTemplateOutputModel(BaseModel):
    service_template: ServiceTemplateModel = Field(alias="serviceTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceTemplateOutputModel(BaseModel):
    service_template: ServiceTemplateModel = Field(alias="serviceTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTemplateSyncConfigOutputModel(BaseModel):
    template_sync_config: TemplateSyncConfigModel = Field(alias="templateSyncConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTemplateSyncConfigOutputModel(BaseModel):
    template_sync_config: TemplateSyncConfigModel = Field(alias="templateSyncConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateSyncConfigOutputModel(BaseModel):
    template_sync_config: TemplateSyncConfigModel = Field(alias="templateSyncConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateSyncConfigOutputModel(BaseModel):
    template_sync_config: TemplateSyncConfigModel = Field(alias="templateSyncConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentAccountConnectionsOutputModel(BaseModel):
    environment_account_connections: List[
        EnvironmentAccountConnectionSummaryModel
    ] = Field(alias="environmentAccountConnections")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsOutputModel(BaseModel):
    environments: List[EnvironmentSummaryModel] = Field(alias="environments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsInputRequestModel(BaseModel):
    environment_templates: Optional[Sequence[EnvironmentTemplateFilterModel]] = Field(
        default=None, alias="environmentTemplates"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEnvironmentTemplatesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    templates: List[EnvironmentTemplateSummaryModel] = Field(alias="templates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentTemplateVersionsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    template_versions: List[EnvironmentTemplateVersionSummaryModel] = Field(
        alias="templateVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentInputComponentDeletedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetComponentInputComponentDeployedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetEnvironmentInputEnvironmentDeployedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitModel(
    BaseModel
):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceInputServiceCreatedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceInputServiceDeletedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceInputServicePipelineDeployedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceInputServiceUpdatedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceInstanceInputServiceInstanceDeployedWaitModel(BaseModel):
    name: str = Field(alias="name")
    service_name: str = Field(alias="serviceName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitModel(
    BaseModel
):
    major_version: str = Field(alias="majorVersion")
    minor_version: str = Field(alias="minorVersion")
    template_name: str = Field(alias="templateName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListComponentOutputsInputListComponentOutputsPaginateModel(BaseModel):
    component_name: str = Field(alias="componentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateModel(
    BaseModel
):
    component_name: str = Field(alias="componentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentsInputListComponentsPaginateModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    service_instance_name: Optional[str] = Field(
        default=None, alias="serviceInstanceName"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateModel(
    BaseModel
):
    requested_by: Literal["ENVIRONMENT_ACCOUNT", "MANAGEMENT_ACCOUNT"] = Field(
        alias="requestedBy"
    )
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    statuses: Optional[Sequence[Literal["CONNECTED", "PENDING", "REJECTED"]]] = Field(
        default=None, alias="statuses"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentOutputsInputListEnvironmentOutputsPaginateModel(BaseModel):
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateModel(
    BaseModel
):
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateModel(
    BaseModel
):
    template_name: str = Field(alias="templateName")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentsInputListEnvironmentsPaginateModel(BaseModel):
    environment_templates: Optional[Sequence[EnvironmentTemplateFilterModel]] = Field(
        default=None, alias="environmentTemplates"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositoriesInputListRepositoriesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateModel(
    BaseModel
):
    repository_name: str = Field(alias="repositoryName")
    repository_provider: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="repositoryProvider"
    )
    sync_type: Literal["TEMPLATE_SYNC"] = Field(alias="syncType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateModel(BaseModel):
    service_instance_name: str = Field(alias="serviceInstanceName")
    service_name: str = Field(alias="serviceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateModel(
    BaseModel
):
    service_instance_name: str = Field(alias="serviceInstanceName")
    service_name: str = Field(alias="serviceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicePipelineOutputsInputListServicePipelineOutputsPaginateModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateModel(
    BaseModel
):
    service_name: str = Field(alias="serviceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateModel(
    BaseModel
):
    template_name: str = Field(alias="templateName")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceTemplatesInputListServiceTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesInputListServicesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceInputListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentOutputsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    outputs: List[OutputModel] = Field(alias="outputs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentOutputsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    outputs: List[OutputModel] = Field(alias="outputs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceInstanceOutputsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    outputs: List[OutputModel] = Field(alias="outputs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicePipelineOutputsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    outputs: List[OutputModel] = Field(alias="outputs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotifyResourceDeploymentStatusChangeInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="outputs")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ListComponentProvisionedResourcesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    provisioned_resources: List[ProvisionedResourceModel] = Field(
        alias="provisionedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentProvisionedResourcesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    provisioned_resources: List[ProvisionedResourceModel] = Field(
        alias="provisionedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceInstanceProvisionedResourcesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    provisioned_resources: List[ProvisionedResourceModel] = Field(
        alias="provisionedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicePipelineProvisionedResourcesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    provisioned_resources: List[ProvisionedResourceModel] = Field(
        alias="provisionedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositoriesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    repositories: List[RepositorySummaryModel] = Field(alias="repositories")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositorySyncDefinitionsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sync_definitions: List[RepositorySyncDefinitionModel] = Field(
        alias="syncDefinitions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceInstancesInputListServiceInstancesPaginateModel(BaseModel):
    filters: Optional[Sequence[ListServiceInstancesFilterModel]] = Field(
        default=None, alias="filters"
    )
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    sort_by: Optional[
        Literal[
            "createdAt",
            "deploymentStatus",
            "environmentName",
            "lastDeploymentAttemptedAt",
            "name",
            "serviceName",
            "templateName",
        ]
    ] = Field(default=None, alias="sortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceInstancesInputRequestModel(BaseModel):
    filters: Optional[Sequence[ListServiceInstancesFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    sort_by: Optional[
        Literal[
            "createdAt",
            "deploymentStatus",
            "environmentName",
            "lastDeploymentAttemptedAt",
            "name",
            "serviceName",
            "templateName",
        ]
    ] = Field(default=None, alias="sortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )


class ListServiceInstancesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    service_instances: List[ServiceInstanceSummaryModel] = Field(
        alias="serviceInstances"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceTemplateVersionsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    template_versions: List[ServiceTemplateVersionSummaryModel] = Field(
        alias="templateVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceTemplatesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    templates: List[ServiceTemplateSummaryModel] = Field(alias="templates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    services: List[ServiceSummaryModel] = Field(alias="services")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RepositorySyncAttemptModel(BaseModel):
    events: List[RepositorySyncEventModel] = Field(alias="events")
    started_at: datetime = Field(alias="startedAt")
    status: Literal[
        "FAILED", "INITIATED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"
    ] = Field(alias="status")


class ResourceSyncAttemptModel(BaseModel):
    events: List[ResourceSyncEventModel] = Field(alias="events")
    initial_revision: RevisionModel = Field(alias="initialRevision")
    started_at: datetime = Field(alias="startedAt")
    status: Literal["FAILED", "INITIATED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="status"
    )
    target: str = Field(alias="target")
    target_revision: RevisionModel = Field(alias="targetRevision")


class TemplateVersionSourceInputModel(BaseModel):
    s3: Optional[S3ObjectSourceModel] = Field(default=None, alias="s3")


class GetAccountSettingsOutputModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="accountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountSettingsOutputModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="accountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelEnvironmentDeploymentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEnvironmentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceOutputModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceOutputModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceOutputModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceOutputModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceTemplateVersionOutputModel(BaseModel):
    service_template_version: ServiceTemplateVersionModel = Field(
        alias="serviceTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceTemplateVersionOutputModel(BaseModel):
    service_template_version: ServiceTemplateVersionModel = Field(
        alias="serviceTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceTemplateVersionOutputModel(BaseModel):
    service_template_version: ServiceTemplateVersionModel = Field(
        alias="serviceTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceTemplateVersionOutputModel(BaseModel):
    service_template_version: ServiceTemplateVersionModel = Field(
        alias="serviceTemplateVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcesSummaryOutputModel(BaseModel):
    counts: CountsSummaryModel = Field(alias="counts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositorySyncStatusOutputModel(BaseModel):
    latest_sync: RepositorySyncAttemptModel = Field(alias="latestSync")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateSyncStatusOutputModel(BaseModel):
    desired_state: RevisionModel = Field(alias="desiredState")
    latest_successful_sync: ResourceSyncAttemptModel = Field(
        alias="latestSuccessfulSync"
    )
    latest_sync: ResourceSyncAttemptModel = Field(alias="latestSync")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentTemplateVersionInputRequestModel(BaseModel):
    source: TemplateVersionSourceInputModel = Field(alias="source")
    template_name: str = Field(alias="templateName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateServiceTemplateVersionInputRequestModel(BaseModel):
    compatible_environment_templates: Sequence[
        CompatibleEnvironmentTemplateInputModel
    ] = Field(alias="compatibleEnvironmentTemplates")
    source: TemplateVersionSourceInputModel = Field(alias="source")
    template_name: str = Field(alias="templateName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    major_version: Optional[str] = Field(default=None, alias="majorVersion")
    supported_component_sources: Optional[
        Sequence[Literal["DIRECTLY_DEFINED"]]
    ] = Field(default=None, alias="supportedComponentSources")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
