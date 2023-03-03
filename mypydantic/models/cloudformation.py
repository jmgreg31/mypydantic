# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountGateResultModel(BaseModel):
    status: Optional[Literal["FAILED", "SKIPPED", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")


class AccountLimitModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[int] = Field(default=None, alias="Value")


class LoggingConfigModel(BaseModel):
    log_role_arn: str = Field(alias="LogRoleArn")
    log_group_name: str = Field(alias="LogGroupName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AutoDeploymentModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    retain_stacks_on_account_removal: Optional[bool] = Field(
        default=None, alias="RetainStacksOnAccountRemoval"
    )


class TypeConfigurationIdentifierModel(BaseModel):
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    type_configuration_alias: Optional[str] = Field(
        default=None, alias="TypeConfigurationAlias"
    )
    type_configuration_arn: Optional[str] = Field(
        default=None, alias="TypeConfigurationArn"
    )
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")


class TypeConfigurationDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    alias: Optional[str] = Field(default=None, alias="Alias")
    configuration: Optional[str] = Field(default=None, alias="Configuration")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    is_default_configuration: Optional[bool] = Field(
        default=None, alias="IsDefaultConfiguration"
    )


class CancelUpdateStackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class CancelUpdateStackInputStackCancelUpdateModel(BaseModel):
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ChangeSetHookResourceTargetDetailsModel(BaseModel):
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_action: Optional[
        Literal["Add", "Dynamic", "Import", "Modify", "Remove"]
    ] = Field(default=None, alias="ResourceAction")


class ChangeSetSummaryModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    change_set_id: Optional[str] = Field(default=None, alias="ChangeSetId")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    execution_status: Optional[
        Literal[
            "AVAILABLE",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "EXECUTE_IN_PROGRESS",
            "OBSOLETE",
            "UNAVAILABLE",
        ]
    ] = Field(default=None, alias="ExecutionStatus")
    status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_IN_PROGRESS",
            "CREATE_PENDING",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_PENDING",
            "FAILED",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    description: Optional[str] = Field(default=None, alias="Description")
    include_nested_stacks: Optional[bool] = Field(
        default=None, alias="IncludeNestedStacks"
    )
    parent_change_set_id: Optional[str] = Field(default=None, alias="ParentChangeSetId")
    root_change_set_id: Optional[str] = Field(default=None, alias="RootChangeSetId")


class ContinueUpdateRollbackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    resources_to_skip: Optional[Sequence[str]] = Field(
        default=None, alias="ResourcesToSkip"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ParameterModel(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    use_previous_value: Optional[bool] = Field(default=None, alias="UsePreviousValue")
    resolved_value: Optional[str] = Field(default=None, alias="ResolvedValue")


class ResourceToImportModel(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_identifier: Mapping[str, str] = Field(alias="ResourceIdentifier")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeploymentTargetsModel(BaseModel):
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    accounts_url: Optional[str] = Field(default=None, alias="AccountsUrl")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    account_filter_type: Optional[
        Literal["DIFFERENCE", "INTERSECTION", "NONE", "UNION"]
    ] = Field(default=None, alias="AccountFilterType")


class StackSetOperationPreferencesModel(BaseModel):
    region_concurrency_type: Optional[Literal["PARALLEL", "SEQUENTIAL"]] = Field(
        default=None, alias="RegionConcurrencyType"
    )
    region_order: Optional[Sequence[str]] = Field(default=None, alias="RegionOrder")
    failure_tolerance_count: Optional[int] = Field(
        default=None, alias="FailureToleranceCount"
    )
    failure_tolerance_percentage: Optional[int] = Field(
        default=None, alias="FailureTolerancePercentage"
    )
    max_concurrent_count: Optional[int] = Field(
        default=None, alias="MaxConcurrentCount"
    )
    max_concurrent_percentage: Optional[int] = Field(
        default=None, alias="MaxConcurrentPercentage"
    )


class ManagedExecutionModel(BaseModel):
    active: Optional[bool] = Field(default=None, alias="Active")


class DeactivateTypeInputRequestModel(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")


class DeleteChangeSetInputRequestModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")


class DeleteStackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    retain_resources: Optional[Sequence[str]] = Field(
        default=None, alias="RetainResources"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteStackInputStackDeleteModel(BaseModel):
    retain_resources: Optional[Sequence[str]] = Field(
        default=None, alias="RetainResources"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteStackSetInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DeregisterTypeInputRequestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccountLimitsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeChangeSetHooksInputRequestModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeChangeSetInputRequestModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePublisherInputRequestModel(BaseModel):
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")


class DescribeStackDriftDetectionStatusInputRequestModel(BaseModel):
    stack_drift_detection_id: str = Field(alias="StackDriftDetectionId")


class DescribeStackEventsInputRequestModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StackEventModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    event_id: str = Field(alias="EventId")
    stack_name: str = Field(alias="StackName")
    timestamp: datetime = Field(alias="Timestamp")
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_SKIPPED",
            "IMPORT_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_COMPLETE",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "ROLLBACK_COMPLETE",
            "ROLLBACK_FAILED",
            "ROLLBACK_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="ResourceStatus")
    resource_status_reason: Optional[str] = Field(
        default=None, alias="ResourceStatusReason"
    )
    resource_properties: Optional[str] = Field(default=None, alias="ResourceProperties")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    hook_type: Optional[str] = Field(default=None, alias="HookType")
    hook_status: Optional[
        Literal[
            "HOOK_COMPLETE_FAILED",
            "HOOK_COMPLETE_SUCCEEDED",
            "HOOK_FAILED",
            "HOOK_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="HookStatus")
    hook_status_reason: Optional[str] = Field(default=None, alias="HookStatusReason")
    hook_invocation_point: Optional[Literal["PRE_PROVISION"]] = Field(
        default=None, alias="HookInvocationPoint"
    )
    hook_failure_mode: Optional[Literal["FAIL", "WARN"]] = Field(
        default=None, alias="HookFailureMode"
    )


class DescribeStackInstanceInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    stack_instance_account: str = Field(alias="StackInstanceAccount")
    stack_instance_region: str = Field(alias="StackInstanceRegion")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStackResourceDriftsInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    stack_resource_drift_status_filters: Optional[
        Sequence[Literal["DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"]]
    ] = Field(default=None, alias="StackResourceDriftStatusFilters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeStackResourceInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")


class DescribeStackResourcesInputRequestModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )


class DescribeStackSetInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStackSetOperationInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStacksInputRequestModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeTypeInputRequestModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    arn: Optional[str] = Field(default=None, alias="Arn")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    public_version_number: Optional[str] = Field(
        default=None, alias="PublicVersionNumber"
    )


class RequiredActivatedTypeModel(BaseModel):
    type_name_alias: Optional[str] = Field(default=None, alias="TypeNameAlias")
    original_type_name: Optional[str] = Field(default=None, alias="OriginalTypeName")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    supported_major_versions: Optional[List[int]] = Field(
        default=None, alias="SupportedMajorVersions"
    )


class DescribeTypeRegistrationInputRequestModel(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")


class DetectStackDriftInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_ids: Optional[Sequence[str]] = Field(
        default=None, alias="LogicalResourceIds"
    )


class DetectStackResourceDriftInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")


class ExecuteChangeSetInputRequestModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")


class ExportModel(BaseModel):
    exporting_stack_id: Optional[str] = Field(default=None, alias="ExportingStackId")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class GetStackPolicyInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")


class GetTemplateInputRequestModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    template_stage: Optional[Literal["Original", "Processed"]] = Field(
        default=None, alias="TemplateStage"
    )


class GetTemplateSummaryInputRequestModel(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ResourceIdentifierSummaryModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    logical_resource_ids: Optional[List[str]] = Field(
        default=None, alias="LogicalResourceIds"
    )
    resource_identifiers: Optional[List[str]] = Field(
        default=None, alias="ResourceIdentifiers"
    )


class ListChangeSetsInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExportsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListImportsInputRequestModel(BaseModel):
    export_name: str = Field(alias="ExportName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StackInstanceFilterModel(BaseModel):
    name: Optional[Literal["DETAILED_STATUS", "LAST_OPERATION_ID"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[str] = Field(default=None, alias="Values")


class ListStackResourcesInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OperationResultFilterModel(BaseModel):
    name: Optional[Literal["OPERATION_RESULT_STATUS"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[str] = Field(default=None, alias="Values")


class ListStackSetOperationsInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ListStackSetsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ListStacksInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    stack_status_filter: Optional[
        Sequence[
            Literal[
                "CREATE_COMPLETE",
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETE_COMPLETE",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_IN_PROGRESS",
                "IMPORT_ROLLBACK_COMPLETE",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "REVIEW_IN_PROGRESS",
                "ROLLBACK_COMPLETE",
                "ROLLBACK_FAILED",
                "ROLLBACK_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="StackStatusFilter")


class ListTypeRegistrationsInputRequestModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    registration_status_filter: Optional[
        Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="RegistrationStatusFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTypeVersionsInputRequestModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    arn: Optional[str] = Field(default=None, alias="Arn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    deprecated_status: Optional[Literal["DEPRECATED", "LIVE"]] = Field(
        default=None, alias="DeprecatedStatus"
    )
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")


class TypeVersionSummaryModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    is_default_version: Optional[bool] = Field(default=None, alias="IsDefaultVersion")
    arn: Optional[str] = Field(default=None, alias="Arn")
    time_created: Optional[datetime] = Field(default=None, alias="TimeCreated")
    description: Optional[str] = Field(default=None, alias="Description")
    public_version_number: Optional[str] = Field(
        default=None, alias="PublicVersionNumber"
    )


class TypeFiltersModel(BaseModel):
    category: Optional[
        Literal["ACTIVATED", "AWS_TYPES", "REGISTERED", "THIRD_PARTY"]
    ] = Field(default=None, alias="Category")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    type_name_prefix: Optional[str] = Field(default=None, alias="TypeNamePrefix")


class TypeSummaryModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    default_version_id: Optional[str] = Field(default=None, alias="DefaultVersionId")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    description: Optional[str] = Field(default=None, alias="Description")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    original_type_name: Optional[str] = Field(default=None, alias="OriginalTypeName")
    public_version_number: Optional[str] = Field(
        default=None, alias="PublicVersionNumber"
    )
    latest_public_version: Optional[str] = Field(
        default=None, alias="LatestPublicVersion"
    )
    publisher_identity: Optional[
        Literal["AWS_Marketplace", "Bitbucket", "GitHub"]
    ] = Field(default=None, alias="PublisherIdentity")
    publisher_name: Optional[str] = Field(default=None, alias="PublisherName")
    is_activated: Optional[bool] = Field(default=None, alias="IsActivated")


class ModuleInfoModel(BaseModel):
    type_hierarchy: Optional[str] = Field(default=None, alias="TypeHierarchy")
    logical_id_hierarchy: Optional[str] = Field(
        default=None, alias="LogicalIdHierarchy"
    )


class OutputModel(BaseModel):
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_value: Optional[str] = Field(default=None, alias="OutputValue")
    description: Optional[str] = Field(default=None, alias="Description")
    export_name: Optional[str] = Field(default=None, alias="ExportName")


class ParameterConstraintsModel(BaseModel):
    allowed_values: Optional[List[str]] = Field(default=None, alias="AllowedValues")


class PhysicalResourceIdContextKeyValuePairModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PropertyDifferenceModel(BaseModel):
    property_path: str = Field(alias="PropertyPath")
    expected_value: str = Field(alias="ExpectedValue")
    actual_value: str = Field(alias="ActualValue")
    difference_type: Literal["ADD", "NOT_EQUAL", "REMOVE"] = Field(
        alias="DifferenceType"
    )


class PublishTypeInputRequestModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    public_version_number: Optional[str] = Field(
        default=None, alias="PublicVersionNumber"
    )


class RecordHandlerProgressInputRequestModel(BaseModel):
    bearer_token: str = Field(alias="BearerToken")
    operation_status: Literal["FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"] = Field(
        alias="OperationStatus"
    )
    current_operation_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"]
    ] = Field(default=None, alias="CurrentOperationStatus")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "AlreadyExists",
            "GeneralServiceException",
            "HandlerInternalFailure",
            "InternalFailure",
            "InvalidCredentials",
            "InvalidRequest",
            "InvalidTypeConfiguration",
            "NetworkFailure",
            "NonCompliant",
            "NotFound",
            "NotStabilized",
            "NotUpdatable",
            "ResourceConflict",
            "ServiceInternalError",
            "ServiceLimitExceeded",
            "Throttling",
            "Unknown",
            "UnsupportedTarget",
        ]
    ] = Field(default=None, alias="ErrorCode")
    resource_model: Optional[str] = Field(default=None, alias="ResourceModel")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class RegisterPublisherInputRequestModel(BaseModel):
    accept_terms_and_conditions: Optional[bool] = Field(
        default=None, alias="AcceptTermsAndConditions"
    )
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")


class ResourceTargetDefinitionModel(BaseModel):
    attribute: Optional[
        Literal[
            "CreationPolicy",
            "DeletionPolicy",
            "Metadata",
            "Properties",
            "Tags",
            "UpdatePolicy",
        ]
    ] = Field(default=None, alias="Attribute")
    name: Optional[str] = Field(default=None, alias="Name")
    requires_recreation: Optional[Literal["Always", "Conditionally", "Never"]] = Field(
        default=None, alias="RequiresRecreation"
    )


class RollbackTriggerModel(BaseModel):
    arn: str = Field(alias="Arn")
    type: str = Field(alias="Type")


class RollbackStackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ServiceResourceEventRequestModel(BaseModel):
    id: str = Field(alias="id")


class ServiceResourceStackRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceStackResourceRequestModel(BaseModel):
    stack_name: str = Field(alias="stack_name")
    logical_id: str = Field(alias="logical_id")


class ServiceResourceStackResourceSummaryRequestModel(BaseModel):
    stack_name: str = Field(alias="stack_name")
    logical_id: str = Field(alias="logical_id")


class SetStackPolicyInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")


class SetTypeConfigurationInputRequestModel(BaseModel):
    configuration: str = Field(alias="Configuration")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    configuration_alias: Optional[str] = Field(default=None, alias="ConfigurationAlias")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )


class SetModelaultVersionInputRequestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class SignalResourceInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")
    unique_id: str = Field(alias="UniqueId")
    status: Literal["FAILURE", "SUCCESS"] = Field(alias="Status")


class StackDriftInformationSummaryModel(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackDriftInformationModel(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackInstanceComprehensiveStatusModel(BaseModel):
    detailed_status: Optional[
        Literal["CANCELLED", "FAILED", "INOPERABLE", "PENDING", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="DetailedStatus")


class StackResourceDriftInformationModel(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackResourceDriftInformationSummaryModel(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackResourceRequestModel(BaseModel):
    logical_id: str = Field(alias="logical_id")


class StackSetDriftDetectionDetailsModel(BaseModel):
    drift_status: Optional[Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"]] = Field(
        default=None, alias="DriftStatus"
    )
    drift_detection_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "STOPPED"]
    ] = Field(default=None, alias="DriftDetectionStatus")
    last_drift_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastDriftCheckTimestamp"
    )
    total_stack_instances_count: Optional[int] = Field(
        default=None, alias="TotalStackInstancesCount"
    )
    drifted_stack_instances_count: Optional[int] = Field(
        default=None, alias="DriftedStackInstancesCount"
    )
    in_sync_stack_instances_count: Optional[int] = Field(
        default=None, alias="InSyncStackInstancesCount"
    )
    in_progress_stack_instances_count: Optional[int] = Field(
        default=None, alias="InProgressStackInstancesCount"
    )
    failed_stack_instances_count: Optional[int] = Field(
        default=None, alias="FailedStackInstancesCount"
    )


class StackSetOperationStatusDetailsModel(BaseModel):
    failed_stack_instances_count: Optional[int] = Field(
        default=None, alias="FailedStackInstancesCount"
    )


class StopStackSetOperationInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class TemplateParameterModel(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    no_echo: Optional[bool] = Field(default=None, alias="NoEcho")
    description: Optional[str] = Field(default=None, alias="Description")


class TestTypeInputRequestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    log_delivery_bucket: Optional[str] = Field(default=None, alias="LogDeliveryBucket")


class UpdateTerminationProtectionInputRequestModel(BaseModel):
    enable_termination_protection: bool = Field(alias="EnableTerminationProtection")
    stack_name: str = Field(alias="StackName")


class ValidateTemplateInputRequestModel(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")


class StackSetOperationResultSummaryModel(BaseModel):
    account: Optional[str] = Field(default=None, alias="Account")
    region: Optional[str] = Field(default=None, alias="Region")
    status: Optional[
        Literal["CANCELLED", "FAILED", "PENDING", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    account_gate_result: Optional[AccountGateResultModel] = Field(
        default=None, alias="AccountGateResult"
    )
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )


class ActivateTypeInputRequestModel(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    public_type_arn: Optional[str] = Field(default=None, alias="PublicTypeArn")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type_name_alias: Optional[str] = Field(default=None, alias="TypeNameAlias")
    auto_update: Optional[bool] = Field(default=None, alias="AutoUpdate")
    logging_config: Optional[LoggingConfigModel] = Field(
        default=None, alias="LoggingConfig"
    )
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    version_bump: Optional[Literal["MAJOR", "MINOR"]] = Field(
        default=None, alias="VersionBump"
    )
    major_version: Optional[int] = Field(default=None, alias="MajorVersion")


class RegisterTypeInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    schema_handler_package: str = Field(alias="SchemaHandlerPackage")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    logging_config: Optional[LoggingConfigModel] = Field(
        default=None, alias="LoggingConfig"
    )
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ActivateTypeOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChangeSetOutputModel(BaseModel):
    id: str = Field(alias="Id")
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStackInstancesOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStackOutputModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStackSetOutputModel(BaseModel):
    stack_set_id: str = Field(alias="StackSetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStackInstancesOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountLimitsOutputModel(BaseModel):
    account_limits: List[AccountLimitModel] = Field(alias="AccountLimits")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePublisherOutputModel(BaseModel):
    publisher_id: str = Field(alias="PublisherId")
    publisher_status: Literal["UNVERIFIED", "VERIFIED"] = Field(alias="PublisherStatus")
    identity_provider: Literal["AWS_Marketplace", "Bitbucket", "GitHub"] = Field(
        alias="IdentityProvider"
    )
    publisher_profile: str = Field(alias="PublisherProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackDriftDetectionStatusOutputModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    stack_drift_detection_id: str = Field(alias="StackDriftDetectionId")
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    detection_status: Literal[
        "DETECTION_COMPLETE", "DETECTION_FAILED", "DETECTION_IN_PROGRESS"
    ] = Field(alias="DetectionStatus")
    detection_status_reason: str = Field(alias="DetectionStatusReason")
    drifted_stack_resource_count: int = Field(alias="DriftedStackResourceCount")
    timestamp: datetime = Field(alias="Timestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTypeRegistrationOutputModel(BaseModel):
    progress_status: Literal["COMPLETE", "FAILED", "IN_PROGRESS"] = Field(
        alias="ProgressStatus"
    )
    description: str = Field(alias="Description")
    type_arn: str = Field(alias="TypeArn")
    type_version_arn: str = Field(alias="TypeVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectStackDriftOutputModel(BaseModel):
    stack_drift_detection_id: str = Field(alias="StackDriftDetectionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectStackSetDriftOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EstimateTemplateCostOutputModel(BaseModel):
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStackPolicyOutputModel(BaseModel):
    stack_policy_body: str = Field(alias="StackPolicyBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateOutputModel(BaseModel):
    template_body: Dict[str, Any] = Field(alias="TemplateBody")
    stages_available: List[Literal["Original", "Processed"]] = Field(
        alias="StagesAvailable"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportStacksToStackSetOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImportsOutputModel(BaseModel):
    imports: List[str] = Field(alias="Imports")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTypeRegistrationsOutputModel(BaseModel):
    registration_token_list: List[str] = Field(alias="RegistrationTokenList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModuleInfoResponseMetadataModel(BaseModel):
    type_hierarchy: str = Field(alias="TypeHierarchy")
    logical_id_hierarchy: str = Field(alias="LogicalIdHierarchy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishTypeOutputModel(BaseModel):
    public_type_arn: str = Field(alias="PublicTypeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterPublisherOutputModel(BaseModel):
    publisher_id: str = Field(alias="PublisherId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTypeOutputModel(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackStackOutputModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetTypeConfigurationOutputModel(BaseModel):
    configuration_arn: str = Field(alias="ConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StackDriftInformationResponseMetadataModel(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StackResourceDriftInformationResponseMetadataModel(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StackResourceDriftInformationSummaryResponseMetadataModel(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestTypeOutputModel(BaseModel):
    type_version_arn: str = Field(alias="TypeVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStackInstancesOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStackOutputModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStackSetOutputModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTerminationProtectionOutputModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDescribeTypeConfigurationsErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    type_configuration_identifier: Optional[TypeConfigurationIdentifierModel] = Field(
        default=None, alias="TypeConfigurationIdentifier"
    )


class BatchDescribeTypeConfigurationsInputRequestModel(BaseModel):
    type_configuration_identifiers: Sequence[TypeConfigurationIdentifierModel] = Field(
        alias="TypeConfigurationIdentifiers"
    )


class ChangeSetHookTargetDetailsModel(BaseModel):
    target_type: Optional[Literal["RESOURCE"]] = Field(default=None, alias="TargetType")
    resource_target_details: Optional[ChangeSetHookResourceTargetDetailsModel] = Field(
        default=None, alias="ResourceTargetDetails"
    )


class ListChangeSetsOutputModel(BaseModel):
    summaries: List[ChangeSetSummaryModel] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EstimateTemplateCostInputRequestModel(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class CreateStackInstancesInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargetsModel] = Field(
        default=None, alias="DeploymentTargets"
    )
    parameter_overrides: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="ParameterOverrides"
    )
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DeleteStackInstancesInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    retain_stacks: bool = Field(alias="RetainStacks")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargetsModel] = Field(
        default=None, alias="DeploymentTargets"
    )
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DetectStackSetDriftInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ImportStacksToStackSetInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    stack_ids: Optional[Sequence[str]] = Field(default=None, alias="StackIds")
    stack_ids_url: Optional[str] = Field(default=None, alias="StackIdsUrl")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class UpdateStackInstancesInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargetsModel] = Field(
        default=None, alias="DeploymentTargets"
    )
    parameter_overrides: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="ParameterOverrides"
    )
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class CreateStackSetInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    description: Optional[str] = Field(default=None, alias="Description")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    auto_deployment: Optional[AutoDeploymentModel] = Field(
        default=None, alias="AutoDeployment"
    )
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    managed_execution: Optional[ManagedExecutionModel] = Field(
        default=None, alias="ManagedExecution"
    )


class StackSetSummaryModel(BaseModel):
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    auto_deployment: Optional[AutoDeploymentModel] = Field(
        default=None, alias="AutoDeployment"
    )
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    drift_status: Optional[
        Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"]
    ] = Field(default=None, alias="DriftStatus")
    last_drift_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastDriftCheckTimestamp"
    )
    managed_execution: Optional[ManagedExecutionModel] = Field(
        default=None, alias="ManagedExecution"
    )


class UpdateStackSetInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    description: Optional[str] = Field(default=None, alias="Description")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    deployment_targets: Optional[DeploymentTargetsModel] = Field(
        default=None, alias="DeploymentTargets"
    )
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    auto_deployment: Optional[AutoDeploymentModel] = Field(
        default=None, alias="AutoDeployment"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    managed_execution: Optional[ManagedExecutionModel] = Field(
        default=None, alias="ManagedExecution"
    )


class DescribeAccountLimitsInputDescribeAccountLimitsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeChangeSetInputDescribeChangeSetPaginateModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStackEventsInputDescribeStackEventsPaginateModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStacksInputDescribeStacksPaginateModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListChangeSetsInputListChangeSetsPaginateModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExportsInputListExportsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImportsInputListImportsPaginateModel(BaseModel):
    export_name: str = Field(alias="ExportName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackResourcesInputListStackResourcesPaginateModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetOperationsInputListStackSetOperationsPaginateModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetsInputListStackSetsPaginateModel(BaseModel):
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStacksInputListStacksPaginateModel(BaseModel):
    stack_status_filter: Optional[
        Sequence[
            Literal[
                "CREATE_COMPLETE",
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETE_COMPLETE",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_IN_PROGRESS",
                "IMPORT_ROLLBACK_COMPLETE",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "REVIEW_IN_PROGRESS",
                "ROLLBACK_COMPLETE",
                "ROLLBACK_FAILED",
                "ROLLBACK_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="StackStatusFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeChangeSetInputChangeSetCreateCompleteWaitModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackCreateCompleteWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackDeleteCompleteWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackExistsWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackImportCompleteWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackRollbackCompleteWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStacksInputStackUpdateCompleteWaitModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTypeRegistrationInputTypeRegistrationCompleteWaitModel(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStackEventsOutputModel(BaseModel):
    stack_events: List[StackEventModel] = Field(alias="StackEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTypeOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    type: Literal["HOOK", "MODULE", "RESOURCE"] = Field(alias="Type")
    type_name: str = Field(alias="TypeName")
    default_version_id: str = Field(alias="DefaultVersionId")
    is_default_version: bool = Field(alias="IsDefaultVersion")
    type_tests_status: Literal["FAILED", "IN_PROGRESS", "NOT_TESTED", "PASSED"] = Field(
        alias="TypeTestsStatus"
    )
    type_tests_status_description: str = Field(alias="TypeTestsStatusDescription")
    description: str = Field(alias="Description")
    schema_: str = Field(alias="Schema")
    provisioning_type: Literal[
        "FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"
    ] = Field(alias="ProvisioningType")
    deprecated_status: Literal["DEPRECATED", "LIVE"] = Field(alias="DeprecatedStatus")
    logging_config: LoggingConfigModel = Field(alias="LoggingConfig")
    required_activated_types: List[RequiredActivatedTypeModel] = Field(
        alias="RequiredActivatedTypes"
    )
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    visibility: Literal["PRIVATE", "PUBLIC"] = Field(alias="Visibility")
    source_url: str = Field(alias="SourceUrl")
    documentation_url: str = Field(alias="DocumentationUrl")
    last_updated: datetime = Field(alias="LastUpdated")
    time_created: datetime = Field(alias="TimeCreated")
    configuration_schema: str = Field(alias="ConfigurationSchema")
    publisher_id: str = Field(alias="PublisherId")
    original_type_name: str = Field(alias="OriginalTypeName")
    original_type_arn: str = Field(alias="OriginalTypeArn")
    public_version_number: str = Field(alias="PublicVersionNumber")
    latest_public_version: str = Field(alias="LatestPublicVersion")
    is_activated: bool = Field(alias="IsActivated")
    auto_update: bool = Field(alias="AutoUpdate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExportsOutputModel(BaseModel):
    exports: List[ExportModel] = Field(alias="Exports")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStackInstancesInputListStackInstancesPaginateModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    filters: Optional[Sequence[StackInstanceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    stack_instance_account: Optional[str] = Field(
        default=None, alias="StackInstanceAccount"
    )
    stack_instance_region: Optional[str] = Field(
        default=None, alias="StackInstanceRegion"
    )
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackInstancesInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[StackInstanceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    stack_instance_account: Optional[str] = Field(
        default=None, alias="StackInstanceAccount"
    )
    stack_instance_region: Optional[str] = Field(
        default=None, alias="StackInstanceRegion"
    )
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ListStackSetOperationResultsInputListStackSetOperationResultsPaginateModel(
    BaseModel
):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    filters: Optional[Sequence[OperationResultFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetOperationResultsInputRequestModel(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    filters: Optional[Sequence[OperationResultFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ListTypeVersionsOutputModel(BaseModel):
    type_version_summaries: List[TypeVersionSummaryModel] = Field(
        alias="TypeVersionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTypesInputListTypesPaginateModel(BaseModel):
    visibility: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Visibility"
    )
    provisioning_type: Optional[
        Literal["FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"]
    ] = Field(default=None, alias="ProvisioningType")
    deprecated_status: Optional[Literal["DEPRECATED", "LIVE"]] = Field(
        default=None, alias="DeprecatedStatus"
    )
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    filters: Optional[TypeFiltersModel] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTypesInputRequestModel(BaseModel):
    visibility: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Visibility"
    )
    provisioning_type: Optional[
        Literal["FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"]
    ] = Field(default=None, alias="ProvisioningType")
    deprecated_status: Optional[Literal["DEPRECATED", "LIVE"]] = Field(
        default=None, alias="DeprecatedStatus"
    )
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    filters: Optional[TypeFiltersModel] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTypesOutputModel(BaseModel):
    type_summaries: List[TypeSummaryModel] = Field(alias="TypeSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParameterDeclarationModel(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    parameter_type: Optional[str] = Field(default=None, alias="ParameterType")
    no_echo: Optional[bool] = Field(default=None, alias="NoEcho")
    description: Optional[str] = Field(default=None, alias="Description")
    parameter_constraints: Optional[ParameterConstraintsModel] = Field(
        default=None, alias="ParameterConstraints"
    )


class StackResourceDriftModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_type: str = Field(alias="ResourceType")
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    timestamp: datetime = Field(alias="Timestamp")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    physical_resource_id_context: Optional[
        List[PhysicalResourceIdContextKeyValuePairModel]
    ] = Field(default=None, alias="PhysicalResourceIdContext")
    expected_properties: Optional[str] = Field(default=None, alias="ExpectedProperties")
    actual_properties: Optional[str] = Field(default=None, alias="ActualProperties")
    property_differences: Optional[List[PropertyDifferenceModel]] = Field(
        default=None, alias="PropertyDifferences"
    )
    module_info: Optional[ModuleInfoModel] = Field(default=None, alias="ModuleInfo")


class ResourceChangeDetailModel(BaseModel):
    target: Optional[ResourceTargetDefinitionModel] = Field(
        default=None, alias="Target"
    )
    evaluation: Optional[Literal["Dynamic", "Static"]] = Field(
        default=None, alias="Evaluation"
    )
    change_source: Optional[
        Literal[
            "Automatic",
            "DirectModification",
            "ParameterReference",
            "ResourceAttribute",
            "ResourceReference",
        ]
    ] = Field(default=None, alias="ChangeSource")
    causing_entity: Optional[str] = Field(default=None, alias="CausingEntity")


class RollbackConfigurationResponseMetadataModel(BaseModel):
    rollback_triggers: List[RollbackTriggerModel] = Field(alias="RollbackTriggers")
    monitoring_time_in_minutes: int = Field(alias="MonitoringTimeInMinutes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackConfigurationModel(BaseModel):
    rollback_triggers: Optional[Sequence[RollbackTriggerModel]] = Field(
        default=None, alias="RollbackTriggers"
    )
    monitoring_time_in_minutes: Optional[int] = Field(
        default=None, alias="MonitoringTimeInMinutes"
    )


class StackSummaryModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    creation_time: datetime = Field(alias="CreationTime")
    stack_status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "IMPORT_COMPLETE",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "REVIEW_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ] = Field(alias="StackStatus")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    template_description: Optional[str] = Field(
        default=None, alias="TemplateDescription"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    deletion_time: Optional[datetime] = Field(default=None, alias="DeletionTime")
    stack_status_reason: Optional[str] = Field(default=None, alias="StackStatusReason")
    parent_id: Optional[str] = Field(default=None, alias="ParentId")
    root_id: Optional[str] = Field(default=None, alias="RootId")
    drift_information: Optional[StackDriftInformationSummaryModel] = Field(
        default=None, alias="DriftInformation"
    )


class StackInstanceSummaryModel(BaseModel):
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    region: Optional[str] = Field(default=None, alias="Region")
    account: Optional[str] = Field(default=None, alias="Account")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    status: Optional[Literal["CURRENT", "INOPERABLE", "OUTDATED"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    stack_instance_status: Optional[StackInstanceComprehensiveStatusModel] = Field(
        default=None, alias="StackInstanceStatus"
    )
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )
    drift_status: Optional[
        Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"]
    ] = Field(default=None, alias="DriftStatus")
    last_drift_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastDriftCheckTimestamp"
    )
    last_operation_id: Optional[str] = Field(default=None, alias="LastOperationId")


class StackInstanceModel(BaseModel):
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    region: Optional[str] = Field(default=None, alias="Region")
    account: Optional[str] = Field(default=None, alias="Account")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    parameter_overrides: Optional[List[ParameterModel]] = Field(
        default=None, alias="ParameterOverrides"
    )
    status: Optional[Literal["CURRENT", "INOPERABLE", "OUTDATED"]] = Field(
        default=None, alias="Status"
    )
    stack_instance_status: Optional[StackInstanceComprehensiveStatusModel] = Field(
        default=None, alias="StackInstanceStatus"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )
    drift_status: Optional[
        Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"]
    ] = Field(default=None, alias="DriftStatus")
    last_drift_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastDriftCheckTimestamp"
    )
    last_operation_id: Optional[str] = Field(default=None, alias="LastOperationId")


class StackResourceDetailModel(BaseModel):
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_type: str = Field(alias="ResourceType")
    last_updated_timestamp: datetime = Field(alias="LastUpdatedTimestamp")
    resource_status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SKIPPED",
        "IMPORT_COMPLETE",
        "IMPORT_FAILED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ] = Field(alias="ResourceStatus")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_status_reason: Optional[str] = Field(
        default=None, alias="ResourceStatusReason"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    drift_information: Optional[StackResourceDriftInformationModel] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfoModel] = Field(default=None, alias="ModuleInfo")


class StackResourceModel(BaseModel):
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_type: str = Field(alias="ResourceType")
    timestamp: datetime = Field(alias="Timestamp")
    resource_status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SKIPPED",
        "IMPORT_COMPLETE",
        "IMPORT_FAILED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ] = Field(alias="ResourceStatus")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_status_reason: Optional[str] = Field(
        default=None, alias="ResourceStatusReason"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    drift_information: Optional[StackResourceDriftInformationModel] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfoModel] = Field(default=None, alias="ModuleInfo")


class StackResourceSummaryModel(BaseModel):
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_type: str = Field(alias="ResourceType")
    last_updated_timestamp: datetime = Field(alias="LastUpdatedTimestamp")
    resource_status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SKIPPED",
        "IMPORT_COMPLETE",
        "IMPORT_FAILED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ] = Field(alias="ResourceStatus")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_status_reason: Optional[str] = Field(
        default=None, alias="ResourceStatusReason"
    )
    drift_information: Optional[StackResourceDriftInformationSummaryModel] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfoModel] = Field(default=None, alias="ModuleInfo")


class StackSetModel(BaseModel):
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    parameters: Optional[List[ParameterModel]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        List[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    stack_set_arn: Optional[str] = Field(default=None, alias="StackSetARN")
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    stack_set_drift_detection_details: Optional[
        StackSetDriftDetectionDetailsModel
    ] = Field(default=None, alias="StackSetDriftDetectionDetails")
    auto_deployment: Optional[AutoDeploymentModel] = Field(
        default=None, alias="AutoDeployment"
    )
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    organizational_unit_ids: Optional[List[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    managed_execution: Optional[ManagedExecutionModel] = Field(
        default=None, alias="ManagedExecution"
    )
    regions: Optional[List[str]] = Field(default=None, alias="Regions")


class StackSetOperationSummaryModel(BaseModel):
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    action: Optional[Literal["CREATE", "DELETE", "DETECT_DRIFT", "UPDATE"]] = Field(
        default=None, alias="Action"
    )
    status: Optional[
        Literal["FAILED", "QUEUED", "RUNNING", "STOPPED", "STOPPING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    end_timestamp: Optional[datetime] = Field(default=None, alias="EndTimestamp")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    status_details: Optional[StackSetOperationStatusDetailsModel] = Field(
        default=None, alias="StatusDetails"
    )
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )


class StackSetOperationModel(BaseModel):
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    action: Optional[Literal["CREATE", "DELETE", "DETECT_DRIFT", "UPDATE"]] = Field(
        default=None, alias="Action"
    )
    status: Optional[
        Literal["FAILED", "QUEUED", "RUNNING", "STOPPED", "STOPPING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    operation_preferences: Optional[StackSetOperationPreferencesModel] = Field(
        default=None, alias="OperationPreferences"
    )
    retain_stacks: Optional[bool] = Field(default=None, alias="RetainStacks")
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    end_timestamp: Optional[datetime] = Field(default=None, alias="EndTimestamp")
    deployment_targets: Optional[DeploymentTargetsModel] = Field(
        default=None, alias="DeploymentTargets"
    )
    stack_set_drift_detection_details: Optional[
        StackSetDriftDetectionDetailsModel
    ] = Field(default=None, alias="StackSetDriftDetectionDetails")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    status_details: Optional[StackSetOperationStatusDetailsModel] = Field(
        default=None, alias="StatusDetails"
    )


class ValidateTemplateOutputModel(BaseModel):
    parameters: List[TemplateParameterModel] = Field(alias="Parameters")
    description: str = Field(alias="Description")
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    capabilities_reason: str = Field(alias="CapabilitiesReason")
    declared_transforms: List[str] = Field(alias="DeclaredTransforms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStackSetOperationResultsOutputModel(BaseModel):
    summaries: List[StackSetOperationResultSummaryModel] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDescribeTypeConfigurationsOutputModel(BaseModel):
    errors: List[BatchDescribeTypeConfigurationsErrorModel] = Field(alias="Errors")
    unprocessed_type_configurations: List[TypeConfigurationIdentifierModel] = Field(
        alias="UnprocessedTypeConfigurations"
    )
    type_configurations: List[TypeConfigurationDetailsModel] = Field(
        alias="TypeConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeSetHookModel(BaseModel):
    invocation_point: Optional[Literal["PRE_PROVISION"]] = Field(
        default=None, alias="InvocationPoint"
    )
    failure_mode: Optional[Literal["FAIL", "WARN"]] = Field(
        default=None, alias="FailureMode"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    type_configuration_version_id: Optional[str] = Field(
        default=None, alias="TypeConfigurationVersionId"
    )
    target_details: Optional[ChangeSetHookTargetDetailsModel] = Field(
        default=None, alias="TargetDetails"
    )


class ListStackSetsOutputModel(BaseModel):
    summaries: List[StackSetSummaryModel] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateSummaryOutputModel(BaseModel):
    parameters: List[ParameterDeclarationModel] = Field(alias="Parameters")
    description: str = Field(alias="Description")
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    capabilities_reason: str = Field(alias="CapabilitiesReason")
    resource_types: List[str] = Field(alias="ResourceTypes")
    version: str = Field(alias="Version")
    metadata: str = Field(alias="Metadata")
    declared_transforms: List[str] = Field(alias="DeclaredTransforms")
    resource_identifier_summaries: List[ResourceIdentifierSummaryModel] = Field(
        alias="ResourceIdentifierSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackResourceDriftsOutputModel(BaseModel):
    stack_resource_drifts: List[StackResourceDriftModel] = Field(
        alias="StackResourceDrifts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectStackResourceDriftOutputModel(BaseModel):
    stack_resource_drift: StackResourceDriftModel = Field(alias="StackResourceDrift")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceChangeModel(BaseModel):
    action: Optional[Literal["Add", "Dynamic", "Import", "Modify", "Remove"]] = Field(
        default=None, alias="Action"
    )
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    replacement: Optional[Literal["Conditional", "False", "True"]] = Field(
        default=None, alias="Replacement"
    )
    scope: Optional[
        List[
            Literal[
                "CreationPolicy",
                "DeletionPolicy",
                "Metadata",
                "Properties",
                "Tags",
                "UpdatePolicy",
            ]
        ]
    ] = Field(default=None, alias="Scope")
    details: Optional[List[ResourceChangeDetailModel]] = Field(
        default=None, alias="Details"
    )
    change_set_id: Optional[str] = Field(default=None, alias="ChangeSetId")
    module_info: Optional[ModuleInfoModel] = Field(default=None, alias="ModuleInfo")


class CreateChangeSetInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    change_set_name: str = Field(alias="ChangeSetName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    change_set_type: Optional[Literal["CREATE", "IMPORT", "UPDATE"]] = Field(
        default=None, alias="ChangeSetType"
    )
    resources_to_import: Optional[Sequence[ResourceToImportModel]] = Field(
        default=None, alias="ResourcesToImport"
    )
    include_nested_stacks: Optional[bool] = Field(
        default=None, alias="IncludeNestedStacks"
    )


class CreateStackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    timeout_in_minutes: Optional[int] = Field(default=None, alias="TimeoutInMinutes")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    on_failure: Optional[Literal["DELETE", "DO_NOTHING", "ROLLBACK"]] = Field(
        default=None, alias="OnFailure"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )


class CreateStackInputServiceResourceCreateStackModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    timeout_in_minutes: Optional[int] = Field(default=None, alias="TimeoutInMinutes")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    on_failure: Optional[Literal["DELETE", "DO_NOTHING", "ROLLBACK"]] = Field(
        default=None, alias="OnFailure"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )


class StackModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    creation_time: datetime = Field(alias="CreationTime")
    stack_status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "IMPORT_COMPLETE",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_COMPLETE",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "REVIEW_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
        "UPDATE_ROLLBACK_FAILED",
        "UPDATE_ROLLBACK_IN_PROGRESS",
    ] = Field(alias="StackStatus")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    change_set_id: Optional[str] = Field(default=None, alias="ChangeSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[List[ParameterModel]] = Field(default=None, alias="Parameters")
    deletion_time: Optional[datetime] = Field(default=None, alias="DeletionTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    stack_status_reason: Optional[str] = Field(default=None, alias="StackStatusReason")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    notification_arns: Optional[List[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    timeout_in_minutes: Optional[int] = Field(default=None, alias="TimeoutInMinutes")
    capabilities: Optional[
        List[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    outputs: Optional[List[OutputModel]] = Field(default=None, alias="Outputs")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )
    parent_id: Optional[str] = Field(default=None, alias="ParentId")
    root_id: Optional[str] = Field(default=None, alias="RootId")
    drift_information: Optional[StackDriftInformationModel] = Field(
        default=None, alias="DriftInformation"
    )


class UpdateStackInputRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    stack_policy_during_update_body: Optional[str] = Field(
        default=None, alias="StackPolicyDuringUpdateBody"
    )
    stack_policy_during_update_url: Optional[str] = Field(
        default=None, alias="StackPolicyDuringUpdateURL"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class UpdateStackInputStackUpdateModel(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    stack_policy_during_update_body: Optional[str] = Field(
        default=None, alias="StackPolicyDuringUpdateBody"
    )
    stack_policy_during_update_url: Optional[str] = Field(
        default=None, alias="StackPolicyDuringUpdateURL"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfigurationModel] = Field(
        default=None, alias="RollbackConfiguration"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ListStacksOutputModel(BaseModel):
    stack_summaries: List[StackSummaryModel] = Field(alias="StackSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStackInstancesOutputModel(BaseModel):
    summaries: List[StackInstanceSummaryModel] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackInstanceOutputModel(BaseModel):
    stack_instance: StackInstanceModel = Field(alias="StackInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackResourceOutputModel(BaseModel):
    stack_resource_detail: StackResourceDetailModel = Field(alias="StackResourceDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackResourcesOutputModel(BaseModel):
    stack_resources: List[StackResourceModel] = Field(alias="StackResources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStackResourcesOutputModel(BaseModel):
    stack_resource_summaries: List[StackResourceSummaryModel] = Field(
        alias="StackResourceSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackSetOutputModel(BaseModel):
    stack_set: StackSetModel = Field(alias="StackSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStackSetOperationsOutputModel(BaseModel):
    summaries: List[StackSetOperationSummaryModel] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackSetOperationOutputModel(BaseModel):
    stack_set_operation: StackSetOperationModel = Field(alias="StackSetOperation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChangeSetHooksOutputModel(BaseModel):
    change_set_id: str = Field(alias="ChangeSetId")
    change_set_name: str = Field(alias="ChangeSetName")
    hooks: List[ChangeSetHookModel] = Field(alias="Hooks")
    status: Literal["PLANNED", "PLANNING", "UNAVAILABLE"] = Field(alias="Status")
    next_token: str = Field(alias="NextToken")
    stack_id: str = Field(alias="StackId")
    stack_name: str = Field(alias="StackName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeModel(BaseModel):
    type: Optional[Literal["Resource"]] = Field(default=None, alias="Type")
    hook_invocation_count: Optional[int] = Field(
        default=None, alias="HookInvocationCount"
    )
    resource_change: Optional[ResourceChangeModel] = Field(
        default=None, alias="ResourceChange"
    )


class DescribeStacksOutputModel(BaseModel):
    stacks: List[StackModel] = Field(alias="Stacks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeChangeSetOutputModel(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    change_set_id: str = Field(alias="ChangeSetId")
    stack_id: str = Field(alias="StackId")
    stack_name: str = Field(alias="StackName")
    description: str = Field(alias="Description")
    parameters: List[ParameterModel] = Field(alias="Parameters")
    creation_time: datetime = Field(alias="CreationTime")
    execution_status: Literal[
        "AVAILABLE",
        "EXECUTE_COMPLETE",
        "EXECUTE_FAILED",
        "EXECUTE_IN_PROGRESS",
        "OBSOLETE",
        "UNAVAILABLE",
    ] = Field(alias="ExecutionStatus")
    status: Literal[
        "CREATE_COMPLETE",
        "CREATE_IN_PROGRESS",
        "CREATE_PENDING",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_PENDING",
        "FAILED",
    ] = Field(alias="Status")
    status_reason: str = Field(alias="StatusReason")
    notification_arns: List[str] = Field(alias="NotificationARNs")
    rollback_configuration: RollbackConfigurationModel = Field(
        alias="RollbackConfiguration"
    )
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    tags: List[TagModel] = Field(alias="Tags")
    changes: List[ChangeModel] = Field(alias="Changes")
    next_token: str = Field(alias="NextToken")
    include_nested_stacks: bool = Field(alias="IncludeNestedStacks")
    parent_change_set_id: str = Field(alias="ParentChangeSetId")
    root_change_set_id: str = Field(alias="RootChangeSetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
