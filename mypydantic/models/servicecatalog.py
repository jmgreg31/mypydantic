# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptPortfolioShareInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    portfolio_share_type: Optional[
        Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
    ] = Field(default=None, alias="PortfolioShareType")


class AccessLevelFilterModel(BaseModel):
    key: Optional[Literal["Account", "Role", "User"]] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AssociateBudgetWithResourceInputRequestModel(BaseModel):
    budget_name: str = Field(alias="BudgetName")
    resource_id: str = Field(alias="ResourceId")


class AssociatePrincipalWithPortfolioInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    principal_arn: str = Field(alias="PrincipalARN")
    principal_type: Literal["IAM", "IAM_PATTERN"] = Field(alias="PrincipalType")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class AssociateProductWithPortfolioInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    source_portfolio_id: Optional[str] = Field(default=None, alias="SourcePortfolioId")


class AssociateServiceActionWithProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    service_action_id: str = Field(alias="ServiceActionId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class AssociateTagOptionWithResourceInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_option_id: str = Field(alias="TagOptionId")


class ServiceActionAssociationModel(BaseModel):
    service_action_id: str = Field(alias="ServiceActionId")
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")


class FailedServiceActionAssociationModel(BaseModel):
    service_action_id: Optional[str] = Field(default=None, alias="ServiceActionId")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    error_code: Optional[
        Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BudgetDetailModel(BaseModel):
    budget_name: Optional[str] = Field(default=None, alias="BudgetName")


class CloudWatchDashboardModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class CodeStarParametersModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    repository: str = Field(alias="Repository")
    branch: str = Field(alias="Branch")
    artifact_path: str = Field(alias="ArtifactPath")


class ConstraintDetailModel(BaseModel):
    constraint_id: Optional[str] = Field(default=None, alias="ConstraintId")
    type: Optional[str] = Field(default=None, alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    owner: Optional[str] = Field(default=None, alias="Owner")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    portfolio_id: Optional[str] = Field(default=None, alias="PortfolioId")


class ConstraintSummaryModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")


class CopyProductInputRequestModel(BaseModel):
    source_product_arn: str = Field(alias="SourceProductArn")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    target_product_id: Optional[str] = Field(default=None, alias="TargetProductId")
    target_product_name: Optional[str] = Field(default=None, alias="TargetProductName")
    source_provisioning_artifact_identifiers: Optional[
        Sequence[Mapping[Literal["Id"], str]]
    ] = Field(default=None, alias="SourceProvisioningArtifactIdentifiers")
    copy_options: Optional[Sequence[Literal["CopyTags"]]] = Field(
        default=None, alias="CopyOptions"
    )


class CreateConstraintInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    product_id: str = Field(alias="ProductId")
    parameters: str = Field(alias="Parameters")
    type: str = Field(alias="Type")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    description: Optional[str] = Field(default=None, alias="Description")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PortfolioDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")


class OrganizationNodeModel(BaseModel):
    type: Optional[Literal["ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT"]] = Field(
        default=None, alias="Type"
    )
    value: Optional[str] = Field(default=None, alias="Value")


class ProvisioningArtifactPropertiesModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    info: Optional[Mapping[str, str]] = Field(default=None, alias="Info")
    type: Optional[
        Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"]
    ] = Field(default=None, alias="Type")
    disable_template_validation: Optional[bool] = Field(
        default=None, alias="DisableTemplateValidation"
    )


class ProvisioningArtifactDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[
        Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"]
    ] = Field(default=None, alias="Type")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    active: Optional[bool] = Field(default=None, alias="Active")
    guidance: Optional[Literal["DEFAULT", "DEPRECATED"]] = Field(
        default=None, alias="Guidance"
    )
    source_revision: Optional[str] = Field(default=None, alias="SourceRevision")


class UpdateProvisioningParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    use_previous_value: Optional[bool] = Field(default=None, alias="UsePreviousValue")


class CreateServiceActionInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    definition_type: Literal["SSM_AUTOMATION"] = Field(alias="DefinitionType")
    definition: Mapping[
        Literal["AssumeRole", "Name", "Parameters", "Version"], str
    ] = Field(alias="Definition")
    idempotency_token: str = Field(alias="IdempotencyToken")
    description: Optional[str] = Field(default=None, alias="Description")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class CreateTagOptionInputRequestModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class TagOptionDetailModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    active: Optional[bool] = Field(default=None, alias="Active")
    id: Optional[str] = Field(default=None, alias="Id")
    owner: Optional[str] = Field(default=None, alias="Owner")


class DeleteConstraintInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DeletePortfolioInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DeleteProductInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DeleteProvisionedProductPlanInputRequestModel(BaseModel):
    plan_id: str = Field(alias="PlanId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    ignore_errors: Optional[bool] = Field(default=None, alias="IgnoreErrors")


class DeleteProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DeleteServiceActionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DeleteTagOptionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeConstraintInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DescribeCopyProductStatusInputRequestModel(BaseModel):
    copy_product_token: str = Field(alias="CopyProductToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DescribePortfolioInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DescribePortfolioShareStatusInputRequestModel(BaseModel):
    portfolio_share_token: str = Field(alias="PortfolioShareToken")


class DescribePortfolioSharesInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    type: Literal[
        "ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT", "ORGANIZATION_MEMBER_ACCOUNT"
    ] = Field(alias="Type")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class PortfolioShareDetailModel(BaseModel):
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    type: Optional[
        Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATIONAL_UNIT",
            "ORGANIZATION_MEMBER_ACCOUNT",
        ]
    ] = Field(default=None, alias="Type")
    accepted: Optional[bool] = Field(default=None, alias="Accepted")
    share_tag_options: Optional[bool] = Field(default=None, alias="ShareTagOptions")
    share_principals: Optional[bool] = Field(default=None, alias="SharePrincipals")


class DescribeProductAsAdminInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    source_portfolio_id: Optional[str] = Field(default=None, alias="SourcePortfolioId")


class ProvisioningArtifactSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    provisioning_artifact_metadata: Optional[Dict[str, str]] = Field(
        default=None, alias="ProvisioningArtifactMetadata"
    )


class DescribeProductInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class LaunchPathModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class ProductViewSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    name: Optional[str] = Field(default=None, alias="Name")
    owner: Optional[str] = Field(default=None, alias="Owner")
    short_description: Optional[str] = Field(default=None, alias="ShortDescription")
    type: Optional[Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"]] = Field(
        default=None, alias="Type"
    )
    distributor: Optional[str] = Field(default=None, alias="Distributor")
    has_default_path: Optional[bool] = Field(default=None, alias="HasDefaultPath")
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_description: Optional[str] = Field(default=None, alias="SupportDescription")
    support_url: Optional[str] = Field(default=None, alias="SupportUrl")


class ProvisioningArtifactModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    guidance: Optional[Literal["DEFAULT", "DEPRECATED"]] = Field(
        default=None, alias="Guidance"
    )


class DescribeProductViewInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DescribeProvisionedProductInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class ProvisionedProductDetailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[str] = Field(default=None, alias="Type")
    id: Optional[str] = Field(default=None, alias="Id")
    status: Optional[
        Literal["AVAILABLE", "ERROR", "PLAN_IN_PROGRESS", "TAINTED", "UNDER_CHANGE"]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    last_record_id: Optional[str] = Field(default=None, alias="LastRecordId")
    last_provisioning_record_id: Optional[str] = Field(
        default=None, alias="LastProvisioningRecordId"
    )
    last_successful_provisioning_record_id: Optional[str] = Field(
        default=None, alias="LastSuccessfulProvisioningRecordId"
    )
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    launch_role_arn: Optional[str] = Field(default=None, alias="LaunchRoleArn")


class DescribeProvisionedProductPlanInputRequestModel(BaseModel):
    plan_id: str = Field(alias="PlanId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class DescribeProvisioningArtifactInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    provisioning_artifact_name: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactName"
    )
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    verbose: Optional[bool] = Field(default=None, alias="Verbose")


class DescribeProvisioningParametersInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    provisioning_artifact_name: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactName"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    path_name: Optional[str] = Field(default=None, alias="PathName")


class ProvisioningArtifactOutputModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    description: Optional[str] = Field(default=None, alias="Description")


class ProvisioningArtifactPreferencesModel(BaseModel):
    stack_set_accounts: Optional[List[str]] = Field(
        default=None, alias="StackSetAccounts"
    )
    stack_set_regions: Optional[List[str]] = Field(
        default=None, alias="StackSetRegions"
    )


class TagOptionSummaryModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[List[str]] = Field(default=None, alias="Values")


class UsageInstructionModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class DescribeRecordInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class RecordOutputModel(BaseModel):
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_value: Optional[str] = Field(default=None, alias="OutputValue")
    description: Optional[str] = Field(default=None, alias="Description")


class DescribeServiceActionExecutionParametersInputRequestModel(BaseModel):
    provisioned_product_id: str = Field(alias="ProvisionedProductId")
    service_action_id: str = Field(alias="ServiceActionId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class ExecutionParameterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    default_values: Optional[List[str]] = Field(default=None, alias="DefaultValues")


class DescribeServiceActionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DescribeTagOptionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DisassociateBudgetFromResourceInputRequestModel(BaseModel):
    budget_name: str = Field(alias="BudgetName")
    resource_id: str = Field(alias="ResourceId")


class DisassociatePrincipalFromPortfolioInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    principal_arn: str = Field(alias="PrincipalARN")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    principal_type: Optional[Literal["IAM", "IAM_PATTERN"]] = Field(
        default=None, alias="PrincipalType"
    )


class DisassociateProductFromPortfolioInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DisassociateServiceActionFromProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    service_action_id: str = Field(alias="ServiceActionId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class DisassociateTagOptionFromResourceInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_option_id: str = Field(alias="TagOptionId")


class ExecuteProvisionedProductPlanInputRequestModel(BaseModel):
    plan_id: str = Field(alias="PlanId")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class ExecuteProvisionedProductServiceActionInputRequestModel(BaseModel):
    provisioned_product_id: str = Field(alias="ProvisionedProductId")
    service_action_id: str = Field(alias="ServiceActionId")
    execute_token: str = Field(alias="ExecuteToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )


class GetProvisionedProductOutputsInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    provisioned_product_id: Optional[str] = Field(
        default=None, alias="ProvisionedProductId"
    )
    provisioned_product_name: Optional[str] = Field(
        default=None, alias="ProvisionedProductName"
    )
    output_keys: Optional[Sequence[str]] = Field(default=None, alias="OutputKeys")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ImportAsProvisionedProductInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    provisioned_product_name: str = Field(alias="ProvisionedProductName")
    physical_id: str = Field(alias="PhysicalId")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class LastSyncModel(BaseModel):
    last_sync_time: Optional[datetime] = Field(default=None, alias="LastSyncTime")
    last_sync_status: Optional[Literal["FAILED", "SUCCEEDED"]] = Field(
        default=None, alias="LastSyncStatus"
    )
    last_sync_status_message: Optional[str] = Field(
        default=None, alias="LastSyncStatusMessage"
    )
    last_successful_sync_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulSyncTime"
    )
    last_successful_sync_provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="LastSuccessfulSyncProvisioningArtifactId"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAcceptedPortfolioSharesInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    portfolio_share_type: Optional[
        Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
    ] = Field(default=None, alias="PortfolioShareType")


class ListBudgetsForResourceInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListConstraintsForPortfolioInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListLaunchPathsInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListOrganizationPortfolioAccessInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    organization_node_type: Literal[
        "ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT"
    ] = Field(alias="OrganizationNodeType")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListPortfolioAccessInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    organization_parent_id: Optional[str] = Field(
        default=None, alias="OrganizationParentId"
    )
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListPortfoliosForProductInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListPortfoliosInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class ListPrincipalsForPortfolioInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class PrincipalModel(BaseModel):
    principal_arn: Optional[str] = Field(default=None, alias="PrincipalARN")
    principal_type: Optional[Literal["IAM", "IAM_PATTERN"]] = Field(
        default=None, alias="PrincipalType"
    )


class ProvisionedProductPlanSummaryModel(BaseModel):
    plan_name: Optional[str] = Field(default=None, alias="PlanName")
    plan_id: Optional[str] = Field(default=None, alias="PlanId")
    provision_product_id: Optional[str] = Field(
        default=None, alias="ProvisionProductId"
    )
    provision_product_name: Optional[str] = Field(
        default=None, alias="ProvisionProductName"
    )
    plan_type: Optional[Literal["CLOUDFORMATION"]] = Field(
        default=None, alias="PlanType"
    )
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )


class ListProvisioningArtifactsForServiceActionInputRequestModel(BaseModel):
    service_action_id: str = Field(alias="ServiceActionId")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class ListProvisioningArtifactsInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class ListRecordHistorySearchFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ListResourcesForTagOptionInputRequestModel(BaseModel):
    tag_option_id: str = Field(alias="TagOptionId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ResourceDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="ARN")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class ListServiceActionsForProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class ServiceActionSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    definition_type: Optional[Literal["SSM_AUTOMATION"]] = Field(
        default=None, alias="DefinitionType"
    )


class ListServiceActionsInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListStackInstancesForProvisionedProductInputRequestModel(BaseModel):
    provisioned_product_id: str = Field(alias="ProvisionedProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class StackInstanceModel(BaseModel):
    account: Optional[str] = Field(default=None, alias="Account")
    region: Optional[str] = Field(default=None, alias="Region")
    stack_instance_status: Optional[
        Literal["CURRENT", "INOPERABLE", "OUTDATED"]
    ] = Field(default=None, alias="StackInstanceStatus")


class ListTagOptionsFiltersModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    active: Optional[bool] = Field(default=None, alias="Active")


class ParameterConstraintsModel(BaseModel):
    allowed_values: Optional[List[str]] = Field(default=None, alias="AllowedValues")
    allowed_pattern: Optional[str] = Field(default=None, alias="AllowedPattern")
    constraint_description: Optional[str] = Field(
        default=None, alias="ConstraintDescription"
    )
    max_length: Optional[str] = Field(default=None, alias="MaxLength")
    min_length: Optional[str] = Field(default=None, alias="MinLength")
    max_value: Optional[str] = Field(default=None, alias="MaxValue")
    min_value: Optional[str] = Field(default=None, alias="MinValue")


class ProductViewAggregationValueModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    approximate_count: Optional[int] = Field(default=None, alias="ApproximateCount")


class ProvisioningParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ProvisioningPreferencesModel(BaseModel):
    stack_set_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="StackSetAccounts"
    )
    stack_set_regions: Optional[Sequence[str]] = Field(
        default=None, alias="StackSetRegions"
    )
    stack_set_failure_tolerance_count: Optional[int] = Field(
        default=None, alias="StackSetFailureToleranceCount"
    )
    stack_set_failure_tolerance_percentage: Optional[int] = Field(
        default=None, alias="StackSetFailureTolerancePercentage"
    )
    stack_set_max_concurrency_count: Optional[int] = Field(
        default=None, alias="StackSetMaxConcurrencyCount"
    )
    stack_set_max_concurrency_percentage: Optional[int] = Field(
        default=None, alias="StackSetMaxConcurrencyPercentage"
    )


class RecordErrorModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")


class RecordTagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class RejectPortfolioShareInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    portfolio_share_type: Optional[
        Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
    ] = Field(default=None, alias="PortfolioShareType")


class ResourceTargetDefinitionModel(BaseModel):
    attribute: Optional[
        Literal[
            "CREATIONPOLICY",
            "DELETIONPOLICY",
            "METADATA",
            "PROPERTIES",
            "TAGS",
            "UPDATEPOLICY",
        ]
    ] = Field(default=None, alias="Attribute")
    name: Optional[str] = Field(default=None, alias="Name")
    requires_recreation: Optional[Literal["ALWAYS", "CONDITIONALLY", "NEVER"]] = Field(
        default=None, alias="RequiresRecreation"
    )


class SearchProductsAsAdminInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    portfolio_id: Optional[str] = Field(default=None, alias="PortfolioId")
    filters: Optional[
        Mapping[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"],
            Sequence[str],
        ]
    ] = Field(default=None, alias="Filters")
    sort_by: Optional[Literal["CreationDate", "Title", "VersionCount"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    product_source: Optional[Literal["ACCOUNT"]] = Field(
        default=None, alias="ProductSource"
    )


class SearchProductsInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    filters: Optional[
        Mapping[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"],
            Sequence[str],
        ]
    ] = Field(default=None, alias="Filters")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    sort_by: Optional[Literal["CreationDate", "Title", "VersionCount"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ShareErrorModel(BaseModel):
    accounts: Optional[List[str]] = Field(default=None, alias="Accounts")
    message: Optional[str] = Field(default=None, alias="Message")
    error: Optional[str] = Field(default=None, alias="Error")


class TerminateProvisionedProductInputRequestModel(BaseModel):
    terminate_token: str = Field(alias="TerminateToken")
    provisioned_product_name: Optional[str] = Field(
        default=None, alias="ProvisionedProductName"
    )
    provisioned_product_id: Optional[str] = Field(
        default=None, alias="ProvisionedProductId"
    )
    ignore_errors: Optional[bool] = Field(default=None, alias="IgnoreErrors")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    retain_physical_resources: Optional[bool] = Field(
        default=None, alias="RetainPhysicalResources"
    )


class UpdateConstraintInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[str] = Field(default=None, alias="Parameters")


class UpdateProvisioningPreferencesModel(BaseModel):
    stack_set_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="StackSetAccounts"
    )
    stack_set_regions: Optional[Sequence[str]] = Field(
        default=None, alias="StackSetRegions"
    )
    stack_set_failure_tolerance_count: Optional[int] = Field(
        default=None, alias="StackSetFailureToleranceCount"
    )
    stack_set_failure_tolerance_percentage: Optional[int] = Field(
        default=None, alias="StackSetFailureTolerancePercentage"
    )
    stack_set_max_concurrency_count: Optional[int] = Field(
        default=None, alias="StackSetMaxConcurrencyCount"
    )
    stack_set_max_concurrency_percentage: Optional[int] = Field(
        default=None, alias="StackSetMaxConcurrencyPercentage"
    )
    stack_set_operation_type: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="StackSetOperationType"
    )


class UpdateProvisionedProductPropertiesInputRequestModel(BaseModel):
    provisioned_product_id: str = Field(alias="ProvisionedProductId")
    provisioned_product_properties: Mapping[
        Literal["LAUNCH_ROLE", "OWNER"], str
    ] = Field(alias="ProvisionedProductProperties")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class UpdateProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    active: Optional[bool] = Field(default=None, alias="Active")
    guidance: Optional[Literal["DEFAULT", "DEPRECATED"]] = Field(
        default=None, alias="Guidance"
    )


class UpdateServiceActionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    definition: Optional[
        Mapping[Literal["AssumeRole", "Name", "Parameters", "Version"], str]
    ] = Field(default=None, alias="Definition")
    description: Optional[str] = Field(default=None, alias="Description")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class UpdateTagOptionInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    value: Optional[str] = Field(default=None, alias="Value")
    active: Optional[bool] = Field(default=None, alias="Active")


class ListProvisionedProductPlansInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    provision_product_id: Optional[str] = Field(
        default=None, alias="ProvisionProductId"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )


class ScanProvisionedProductsInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class SearchProvisionedProductsInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    filters: Optional[Mapping[Literal["SearchQuery"], Sequence[str]]] = Field(
        default=None, alias="Filters"
    )
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class BatchAssociateServiceActionWithProvisioningArtifactInputRequestModel(BaseModel):
    service_action_associations: Sequence[ServiceActionAssociationModel] = Field(
        alias="ServiceActionAssociations"
    )
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class BatchDisassociateServiceActionFromProvisioningArtifactInputRequestModel(
    BaseModel
):
    service_action_associations: Sequence[ServiceActionAssociationModel] = Field(
        alias="ServiceActionAssociations"
    )
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class BatchAssociateServiceActionWithProvisioningArtifactOutputModel(BaseModel):
    failed_service_action_associations: List[
        FailedServiceActionAssociationModel
    ] = Field(alias="FailedServiceActionAssociations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateServiceActionFromProvisioningArtifactOutputModel(BaseModel):
    failed_service_action_associations: List[
        FailedServiceActionAssociationModel
    ] = Field(alias="FailedServiceActionAssociations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyProductOutputModel(BaseModel):
    copy_product_token: str = Field(alias="CopyProductToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePortfolioShareOutputModel(BaseModel):
    portfolio_share_token: str = Field(alias="PortfolioShareToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisionedProductPlanOutputModel(BaseModel):
    plan_name: str = Field(alias="PlanName")
    plan_id: str = Field(alias="PlanId")
    provision_product_id: str = Field(alias="ProvisionProductId")
    provisioned_product_name: str = Field(alias="ProvisionedProductName")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePortfolioShareOutputModel(BaseModel):
    portfolio_share_token: str = Field(alias="PortfolioShareToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCopyProductStatusOutputModel(BaseModel):
    copy_product_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="CopyProductStatus"
    )
    target_product_id: str = Field(alias="TargetProductId")
    status_detail: str = Field(alias="StatusDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAWSOrganizationsAccessStatusOutputModel(BaseModel):
    access_status: Literal["DISABLED", "ENABLED", "UNDER_CHANGE"] = Field(
        alias="AccessStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPortfolioAccessOutputModel(BaseModel):
    account_ids: List[str] = Field(alias="AccountIds")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePortfolioShareOutputModel(BaseModel):
    portfolio_share_token: str = Field(alias="PortfolioShareToken")
    status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR", "IN_PROGRESS", "NOT_STARTED"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProvisionedProductPropertiesOutputModel(BaseModel):
    provisioned_product_id: str = Field(alias="ProvisionedProductId")
    provisioned_product_properties: Dict[Literal["LAUNCH_ROLE", "OWNER"], str] = Field(
        alias="ProvisionedProductProperties"
    )
    record_id: str = Field(alias="RecordId")
    status: Literal[
        "CREATED", "FAILED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBudgetsForResourceOutputModel(BaseModel):
    budgets: List[BudgetDetailModel] = Field(alias="Budgets")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceConnectionParametersModel(BaseModel):
    code_star: Optional[CodeStarParametersModel] = Field(default=None, alias="CodeStar")


class CreateConstraintOutputModel(BaseModel):
    constraint_detail: ConstraintDetailModel = Field(alias="ConstraintDetail")
    constraint_parameters: str = Field(alias="ConstraintParameters")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConstraintOutputModel(BaseModel):
    constraint_detail: ConstraintDetailModel = Field(alias="ConstraintDetail")
    constraint_parameters: str = Field(alias="ConstraintParameters")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConstraintsForPortfolioOutputModel(BaseModel):
    constraint_details: List[ConstraintDetailModel] = Field(alias="ConstraintDetails")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConstraintOutputModel(BaseModel):
    constraint_detail: ConstraintDetailModel = Field(alias="ConstraintDetail")
    constraint_parameters: str = Field(alias="ConstraintParameters")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePortfolioInputRequestModel(BaseModel):
    display_name: str = Field(alias="DisplayName")
    provider_name: str = Field(alias="ProviderName")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class LaunchPathSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    constraint_summaries: Optional[List[ConstraintSummaryModel]] = Field(
        default=None, alias="ConstraintSummaries"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    name: Optional[str] = Field(default=None, alias="Name")


class ProvisionedProductAttributeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[str] = Field(default=None, alias="Type")
    id: Optional[str] = Field(default=None, alias="Id")
    status: Optional[
        Literal["AVAILABLE", "ERROR", "PLAN_IN_PROGRESS", "TAINTED", "UNDER_CHANGE"]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    last_record_id: Optional[str] = Field(default=None, alias="LastRecordId")
    last_provisioning_record_id: Optional[str] = Field(
        default=None, alias="LastProvisioningRecordId"
    )
    last_successful_provisioning_record_id: Optional[str] = Field(
        default=None, alias="LastSuccessfulProvisioningRecordId"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    physical_id: Optional[str] = Field(default=None, alias="PhysicalId")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    provisioning_artifact_name: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactName"
    )
    user_arn: Optional[str] = Field(default=None, alias="UserArn")
    user_arn_session: Optional[str] = Field(default=None, alias="UserArnSession")


class UpdatePortfolioInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")
    add_tags: Optional[Sequence[TagModel]] = Field(default=None, alias="AddTags")
    remove_tags: Optional[Sequence[str]] = Field(default=None, alias="RemoveTags")


class CreatePortfolioOutputModel(BaseModel):
    portfolio_detail: PortfolioDetailModel = Field(alias="PortfolioDetail")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAcceptedPortfolioSharesOutputModel(BaseModel):
    portfolio_details: List[PortfolioDetailModel] = Field(alias="PortfolioDetails")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPortfoliosForProductOutputModel(BaseModel):
    portfolio_details: List[PortfolioDetailModel] = Field(alias="PortfolioDetails")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPortfoliosOutputModel(BaseModel):
    portfolio_details: List[PortfolioDetailModel] = Field(alias="PortfolioDetails")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePortfolioOutputModel(BaseModel):
    portfolio_detail: PortfolioDetailModel = Field(alias="PortfolioDetail")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePortfolioShareInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    organization_node: Optional[OrganizationNodeModel] = Field(
        default=None, alias="OrganizationNode"
    )
    share_tag_options: Optional[bool] = Field(default=None, alias="ShareTagOptions")
    share_principals: Optional[bool] = Field(default=None, alias="SharePrincipals")


class DeletePortfolioShareInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    organization_node: Optional[OrganizationNodeModel] = Field(
        default=None, alias="OrganizationNode"
    )


class ListOrganizationPortfolioAccessOutputModel(BaseModel):
    organization_nodes: List[OrganizationNodeModel] = Field(alias="OrganizationNodes")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePortfolioShareInputRequestModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    organization_node: Optional[OrganizationNodeModel] = Field(
        default=None, alias="OrganizationNode"
    )
    share_tag_options: Optional[bool] = Field(default=None, alias="ShareTagOptions")
    share_principals: Optional[bool] = Field(default=None, alias="SharePrincipals")


class CreateProvisioningArtifactInputRequestModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    parameters: ProvisioningArtifactPropertiesModel = Field(alias="Parameters")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")


class CreateProvisioningArtifactOutputModel(BaseModel):
    provisioning_artifact_detail: ProvisioningArtifactDetailModel = Field(
        alias="ProvisioningArtifactDetail"
    )
    info: Dict[str, str] = Field(alias="Info")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProvisioningArtifactOutputModel(BaseModel):
    provisioning_artifact_detail: ProvisioningArtifactDetailModel = Field(
        alias="ProvisioningArtifactDetail"
    )
    info: Dict[str, str] = Field(alias="Info")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisioningArtifactsOutputModel(BaseModel):
    provisioning_artifact_details: List[ProvisioningArtifactDetailModel] = Field(
        alias="ProvisioningArtifactDetails"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProvisioningArtifactOutputModel(BaseModel):
    provisioning_artifact_detail: ProvisioningArtifactDetailModel = Field(
        alias="ProvisioningArtifactDetail"
    )
    info: Dict[str, str] = Field(alias="Info")
    status: Literal["AVAILABLE", "CREATING", "FAILED"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisionedProductPlanInputRequestModel(BaseModel):
    plan_name: str = Field(alias="PlanName")
    plan_type: Literal["CLOUDFORMATION"] = Field(alias="PlanType")
    product_id: str = Field(alias="ProductId")
    provisioned_product_name: str = Field(alias="ProvisionedProductName")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationArns"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    provisioning_parameters: Optional[
        Sequence[UpdateProvisioningParameterModel]
    ] = Field(default=None, alias="ProvisioningParameters")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ProvisionedProductPlanDetailsModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    path_id: Optional[str] = Field(default=None, alias="PathId")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    plan_name: Optional[str] = Field(default=None, alias="PlanName")
    plan_id: Optional[str] = Field(default=None, alias="PlanId")
    provision_product_id: Optional[str] = Field(
        default=None, alias="ProvisionProductId"
    )
    provision_product_name: Optional[str] = Field(
        default=None, alias="ProvisionProductName"
    )
    plan_type: Optional[Literal["CLOUDFORMATION"]] = Field(
        default=None, alias="PlanType"
    )
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    status: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESS",
            "EXECUTE_FAILED",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_SUCCESS",
        ]
    ] = Field(default=None, alias="Status")
    updated_time: Optional[datetime] = Field(default=None, alias="UpdatedTime")
    notification_arns: Optional[List[str]] = Field(
        default=None, alias="NotificationArns"
    )
    provisioning_parameters: Optional[List[UpdateProvisioningParameterModel]] = Field(
        default=None, alias="ProvisioningParameters"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class CreateTagOptionOutputModel(BaseModel):
    tag_option_detail: TagOptionDetailModel = Field(alias="TagOptionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePortfolioOutputModel(BaseModel):
    portfolio_detail: PortfolioDetailModel = Field(alias="PortfolioDetail")
    tags: List[TagModel] = Field(alias="Tags")
    tag_options: List[TagOptionDetailModel] = Field(alias="TagOptions")
    budgets: List[BudgetDetailModel] = Field(alias="Budgets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTagOptionOutputModel(BaseModel):
    tag_option_detail: TagOptionDetailModel = Field(alias="TagOptionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagOptionsOutputModel(BaseModel):
    tag_option_details: List[TagOptionDetailModel] = Field(alias="TagOptionDetails")
    page_token: str = Field(alias="PageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTagOptionOutputModel(BaseModel):
    tag_option_detail: TagOptionDetailModel = Field(alias="TagOptionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePortfolioSharesOutputModel(BaseModel):
    next_page_token: str = Field(alias="NextPageToken")
    portfolio_share_details: List[PortfolioShareDetailModel] = Field(
        alias="PortfolioShareDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProductOutputModel(BaseModel):
    product_view_summary: ProductViewSummaryModel = Field(alias="ProductViewSummary")
    provisioning_artifacts: List[ProvisioningArtifactModel] = Field(
        alias="ProvisioningArtifacts"
    )
    budgets: List[BudgetDetailModel] = Field(alias="Budgets")
    launch_paths: List[LaunchPathModel] = Field(alias="LaunchPaths")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProductViewOutputModel(BaseModel):
    product_view_summary: ProductViewSummaryModel = Field(alias="ProductViewSummary")
    provisioning_artifacts: List[ProvisioningArtifactModel] = Field(
        alias="ProvisioningArtifacts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisioningArtifactViewModel(BaseModel):
    product_view_summary: Optional[ProductViewSummaryModel] = Field(
        default=None, alias="ProductViewSummary"
    )
    provisioning_artifact: Optional[ProvisioningArtifactModel] = Field(
        default=None, alias="ProvisioningArtifact"
    )


class DescribeProvisionedProductOutputModel(BaseModel):
    provisioned_product_detail: ProvisionedProductDetailModel = Field(
        alias="ProvisionedProductDetail"
    )
    cloud_watch_dashboards: List[CloudWatchDashboardModel] = Field(
        alias="CloudWatchDashboards"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScanProvisionedProductsOutputModel(BaseModel):
    provisioned_products: List[ProvisionedProductDetailModel] = Field(
        alias="ProvisionedProducts"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProvisionedProductOutputsOutputModel(BaseModel):
    outputs: List[RecordOutputModel] = Field(alias="Outputs")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServiceActionExecutionParametersOutputModel(BaseModel):
    service_action_parameters: List[ExecutionParameterModel] = Field(
        alias="ServiceActionParameters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateModel(
    BaseModel
):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    portfolio_share_type: Optional[
        Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
    ] = Field(default=None, alias="PortfolioShareType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateModel(
    BaseModel
):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLaunchPathsInputListLaunchPathsPaginateModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateModel(
    BaseModel
):
    portfolio_id: str = Field(alias="PortfolioId")
    organization_node_type: Literal[
        "ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT"
    ] = Field(alias="OrganizationNodeType")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPortfoliosForProductInputListPortfoliosForProductPaginateModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPortfoliosInputListPortfoliosPaginateModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateModel(BaseModel):
    portfolio_id: str = Field(alias="PortfolioId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisionedProductPlansInputListProvisionedProductPlansPaginateModel(
    BaseModel
):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    provision_product_id: Optional[str] = Field(
        default=None, alias="ProvisionProductId"
    )
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateModel(
    BaseModel
):
    service_action_id: str = Field(alias="ServiceActionId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcesForTagOptionInputListResourcesForTagOptionPaginateModel(BaseModel):
    tag_option_id: str = Field(alias="TagOptionId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateModel(
    BaseModel
):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: str = Field(alias="ProvisioningArtifactId")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceActionsInputListServiceActionsPaginateModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ScanProvisionedProductsInputScanProvisionedProductsPaginateModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchProductsAsAdminInputSearchProductsAsAdminPaginateModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    portfolio_id: Optional[str] = Field(default=None, alias="PortfolioId")
    filters: Optional[
        Mapping[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"],
            Sequence[str],
        ]
    ] = Field(default=None, alias="Filters")
    sort_by: Optional[Literal["CreationDate", "Title", "VersionCount"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    product_source: Optional[Literal["ACCOUNT"]] = Field(
        default=None, alias="ProductSource"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrincipalsForPortfolioOutputModel(BaseModel):
    principals: List[PrincipalModel] = Field(alias="Principals")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisionedProductPlansOutputModel(BaseModel):
    provisioned_product_plans: List[ProvisionedProductPlanSummaryModel] = Field(
        alias="ProvisionedProductPlans"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecordHistoryInputListRecordHistoryPaginateModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    search_filter: Optional[ListRecordHistorySearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecordHistoryInputRequestModel(BaseModel):
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    access_level_filter: Optional[AccessLevelFilterModel] = Field(
        default=None, alias="AccessLevelFilter"
    )
    search_filter: Optional[ListRecordHistorySearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ListResourcesForTagOptionOutputModel(BaseModel):
    resource_details: List[ResourceDetailModel] = Field(alias="ResourceDetails")
    page_token: str = Field(alias="PageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceActionsForProvisioningArtifactOutputModel(BaseModel):
    service_action_summaries: List[ServiceActionSummaryModel] = Field(
        alias="ServiceActionSummaries"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceActionsOutputModel(BaseModel):
    service_action_summaries: List[ServiceActionSummaryModel] = Field(
        alias="ServiceActionSummaries"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServiceActionDetailModel(BaseModel):
    service_action_summary: Optional[ServiceActionSummaryModel] = Field(
        default=None, alias="ServiceActionSummary"
    )
    definition: Optional[
        Dict[Literal["AssumeRole", "Name", "Parameters", "Version"], str]
    ] = Field(default=None, alias="Definition")


class ListStackInstancesForProvisionedProductOutputModel(BaseModel):
    stack_instances: List[StackInstanceModel] = Field(alias="StackInstances")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagOptionsInputListTagOptionsPaginateModel(BaseModel):
    filters: Optional[ListTagOptionsFiltersModel] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagOptionsInputRequestModel(BaseModel):
    filters: Optional[ListTagOptionsFiltersModel] = Field(default=None, alias="Filters")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    page_token: Optional[str] = Field(default=None, alias="PageToken")


class ProvisioningArtifactParameterModel(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    parameter_type: Optional[str] = Field(default=None, alias="ParameterType")
    is_no_echo: Optional[bool] = Field(default=None, alias="IsNoEcho")
    description: Optional[str] = Field(default=None, alias="Description")
    parameter_constraints: Optional[ParameterConstraintsModel] = Field(
        default=None, alias="ParameterConstraints"
    )


class SearchProductsOutputModel(BaseModel):
    product_view_summaries: List[ProductViewSummaryModel] = Field(
        alias="ProductViewSummaries"
    )
    product_view_aggregations: Dict[
        str, List[ProductViewAggregationValueModel]
    ] = Field(alias="ProductViewAggregations")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionProductInputRequestModel(BaseModel):
    provisioned_product_name: str = Field(alias="ProvisionedProductName")
    provision_token: str = Field(alias="ProvisionToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    provisioning_artifact_name: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactName"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    path_name: Optional[str] = Field(default=None, alias="PathName")
    provisioning_parameters: Optional[Sequence[ProvisioningParameterModel]] = Field(
        default=None, alias="ProvisioningParameters"
    )
    provisioning_preferences: Optional[ProvisioningPreferencesModel] = Field(
        default=None, alias="ProvisioningPreferences"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationArns"
    )


class RecordDetailModel(BaseModel):
    record_id: Optional[str] = Field(default=None, alias="RecordId")
    provisioned_product_name: Optional[str] = Field(
        default=None, alias="ProvisionedProductName"
    )
    status: Optional[
        Literal["CREATED", "FAILED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    updated_time: Optional[datetime] = Field(default=None, alias="UpdatedTime")
    provisioned_product_type: Optional[str] = Field(
        default=None, alias="ProvisionedProductType"
    )
    record_type: Optional[str] = Field(default=None, alias="RecordType")
    provisioned_product_id: Optional[str] = Field(
        default=None, alias="ProvisionedProductId"
    )
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    record_errors: Optional[List[RecordErrorModel]] = Field(
        default=None, alias="RecordErrors"
    )
    record_tags: Optional[List[RecordTagModel]] = Field(
        default=None, alias="RecordTags"
    )
    launch_role_arn: Optional[str] = Field(default=None, alias="LaunchRoleArn")


class ResourceChangeDetailModel(BaseModel):
    target: Optional[ResourceTargetDefinitionModel] = Field(
        default=None, alias="Target"
    )
    evaluation: Optional[Literal["DYNAMIC", "STATIC"]] = Field(
        default=None, alias="Evaluation"
    )
    causing_entity: Optional[str] = Field(default=None, alias="CausingEntity")


class ShareDetailsModel(BaseModel):
    successful_shares: Optional[List[str]] = Field(
        default=None, alias="SuccessfulShares"
    )
    share_errors: Optional[List[ShareErrorModel]] = Field(
        default=None, alias="ShareErrors"
    )


class UpdateProvisionedProductInputRequestModel(BaseModel):
    update_token: str = Field(alias="UpdateToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    provisioned_product_name: Optional[str] = Field(
        default=None, alias="ProvisionedProductName"
    )
    provisioned_product_id: Optional[str] = Field(
        default=None, alias="ProvisionedProductId"
    )
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    provisioning_artifact_name: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactName"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    path_name: Optional[str] = Field(default=None, alias="PathName")
    provisioning_parameters: Optional[
        Sequence[UpdateProvisioningParameterModel]
    ] = Field(default=None, alias="ProvisioningParameters")
    provisioning_preferences: Optional[UpdateProvisioningPreferencesModel] = Field(
        default=None, alias="ProvisioningPreferences"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class SourceConnectionDetailModel(BaseModel):
    type: Optional[Literal["CODESTAR"]] = Field(default=None, alias="Type")
    connection_parameters: Optional[SourceConnectionParametersModel] = Field(
        default=None, alias="ConnectionParameters"
    )
    last_sync: Optional[LastSyncModel] = Field(default=None, alias="LastSync")


class SourceConnectionModel(BaseModel):
    connection_parameters: SourceConnectionParametersModel = Field(
        alias="ConnectionParameters"
    )
    type: Optional[Literal["CODESTAR"]] = Field(default=None, alias="Type")


class ListLaunchPathsOutputModel(BaseModel):
    launch_path_summaries: List[LaunchPathSummaryModel] = Field(
        alias="LaunchPathSummaries"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchProvisionedProductsOutputModel(BaseModel):
    provisioned_products: List[ProvisionedProductAttributeModel] = Field(
        alias="ProvisionedProducts"
    )
    total_results_count: int = Field(alias="TotalResultsCount")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisioningArtifactsForServiceActionOutputModel(BaseModel):
    provisioning_artifact_views: List[ProvisioningArtifactViewModel] = Field(
        alias="ProvisioningArtifactViews"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceActionOutputModel(BaseModel):
    service_action_detail: ServiceActionDetailModel = Field(alias="ServiceActionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServiceActionOutputModel(BaseModel):
    service_action_detail: ServiceActionDetailModel = Field(alias="ServiceActionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceActionOutputModel(BaseModel):
    service_action_detail: ServiceActionDetailModel = Field(alias="ServiceActionDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProvisioningParametersOutputModel(BaseModel):
    provisioning_artifact_parameters: List[ProvisioningArtifactParameterModel] = Field(
        alias="ProvisioningArtifactParameters"
    )
    constraint_summaries: List[ConstraintSummaryModel] = Field(
        alias="ConstraintSummaries"
    )
    usage_instructions: List[UsageInstructionModel] = Field(alias="UsageInstructions")
    tag_options: List[TagOptionSummaryModel] = Field(alias="TagOptions")
    provisioning_artifact_preferences: ProvisioningArtifactPreferencesModel = Field(
        alias="ProvisioningArtifactPreferences"
    )
    provisioning_artifact_outputs: List[ProvisioningArtifactOutputModel] = Field(
        alias="ProvisioningArtifactOutputs"
    )
    provisioning_artifact_output_keys: List[ProvisioningArtifactOutputModel] = Field(
        alias="ProvisioningArtifactOutputKeys"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRecordOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    record_outputs: List[RecordOutputModel] = Field(alias="RecordOutputs")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteProvisionedProductPlanOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteProvisionedProductServiceActionOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportAsProvisionedProductOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecordHistoryOutputModel(BaseModel):
    record_details: List[RecordDetailModel] = Field(alias="RecordDetails")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionProductOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateProvisionedProductOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProvisionedProductOutputModel(BaseModel):
    record_detail: RecordDetailModel = Field(alias="RecordDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceChangeModel(BaseModel):
    action: Optional[Literal["ADD", "MODIFY", "REMOVE"]] = Field(
        default=None, alias="Action"
    )
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    replacement: Optional[Literal["CONDITIONAL", "FALSE", "TRUE"]] = Field(
        default=None, alias="Replacement"
    )
    scope: Optional[
        List[
            Literal[
                "CREATIONPOLICY",
                "DELETIONPOLICY",
                "METADATA",
                "PROPERTIES",
                "TAGS",
                "UPDATEPOLICY",
            ]
        ]
    ] = Field(default=None, alias="Scope")
    details: Optional[List[ResourceChangeDetailModel]] = Field(
        default=None, alias="Details"
    )


class DescribePortfolioShareStatusOutputModel(BaseModel):
    portfolio_share_token: str = Field(alias="PortfolioShareToken")
    portfolio_id: str = Field(alias="PortfolioId")
    organization_node_value: str = Field(alias="OrganizationNodeValue")
    status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR", "IN_PROGRESS", "NOT_STARTED"
    ] = Field(alias="Status")
    share_details: ShareDetailsModel = Field(alias="ShareDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProductViewDetailModel(BaseModel):
    product_view_summary: Optional[ProductViewSummaryModel] = Field(
        default=None, alias="ProductViewSummary"
    )
    status: Optional[Literal["AVAILABLE", "CREATING", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    product_arn: Optional[str] = Field(default=None, alias="ProductARN")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    source_connection: Optional[SourceConnectionDetailModel] = Field(
        default=None, alias="SourceConnection"
    )


class CreateProductInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    owner: str = Field(alias="Owner")
    product_type: Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"] = Field(
        alias="ProductType"
    )
    idempotency_token: str = Field(alias="IdempotencyToken")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    description: Optional[str] = Field(default=None, alias="Description")
    distributor: Optional[str] = Field(default=None, alias="Distributor")
    support_description: Optional[str] = Field(default=None, alias="SupportDescription")
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_url: Optional[str] = Field(default=None, alias="SupportUrl")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    provisioning_artifact_parameters: Optional[
        ProvisioningArtifactPropertiesModel
    ] = Field(default=None, alias="ProvisioningArtifactParameters")
    source_connection: Optional[SourceConnectionModel] = Field(
        default=None, alias="SourceConnection"
    )


class UpdateProductInputRequestModel(BaseModel):
    id: str = Field(alias="Id")
    accept_language: Optional[str] = Field(default=None, alias="AcceptLanguage")
    name: Optional[str] = Field(default=None, alias="Name")
    owner: Optional[str] = Field(default=None, alias="Owner")
    description: Optional[str] = Field(default=None, alias="Description")
    distributor: Optional[str] = Field(default=None, alias="Distributor")
    support_description: Optional[str] = Field(default=None, alias="SupportDescription")
    support_email: Optional[str] = Field(default=None, alias="SupportEmail")
    support_url: Optional[str] = Field(default=None, alias="SupportUrl")
    add_tags: Optional[Sequence[TagModel]] = Field(default=None, alias="AddTags")
    remove_tags: Optional[Sequence[str]] = Field(default=None, alias="RemoveTags")
    source_connection: Optional[SourceConnectionModel] = Field(
        default=None, alias="SourceConnection"
    )


class DescribeProvisionedProductPlanOutputModel(BaseModel):
    provisioned_product_plan_details: ProvisionedProductPlanDetailsModel = Field(
        alias="ProvisionedProductPlanDetails"
    )
    resource_changes: List[ResourceChangeModel] = Field(alias="ResourceChanges")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProductOutputModel(BaseModel):
    product_view_detail: ProductViewDetailModel = Field(alias="ProductViewDetail")
    provisioning_artifact_detail: ProvisioningArtifactDetailModel = Field(
        alias="ProvisioningArtifactDetail"
    )
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProductAsAdminOutputModel(BaseModel):
    product_view_detail: ProductViewDetailModel = Field(alias="ProductViewDetail")
    provisioning_artifact_summaries: List[ProvisioningArtifactSummaryModel] = Field(
        alias="ProvisioningArtifactSummaries"
    )
    tags: List[TagModel] = Field(alias="Tags")
    tag_options: List[TagOptionDetailModel] = Field(alias="TagOptions")
    budgets: List[BudgetDetailModel] = Field(alias="Budgets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchProductsAsAdminOutputModel(BaseModel):
    product_view_details: List[ProductViewDetailModel] = Field(
        alias="ProductViewDetails"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProductOutputModel(BaseModel):
    product_view_detail: ProductViewDetailModel = Field(alias="ProductViewDetail")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
