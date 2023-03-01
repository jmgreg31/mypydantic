# Model Generated: Wed Mar  1 14:20:28 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountGateResult(BaseModel):
    status: Optional[Literal["FAILED", "SKIPPED", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")


class AccountLimit(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[int] = Field(default=None, alias="Value")


class LoggingConfig(BaseModel):
    log_role_arn: str = Field(alias="LogRoleArn")
    log_group_name: str = Field(alias="LogGroupName")


class ResponseMetadata(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AutoDeployment(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    retain_stacks_on_account_removal: Optional[bool] = Field(
        default=None, alias="RetainStacksOnAccountRemoval"
    )


class TypeConfigurationIdentifier(BaseModel):
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


class TypeConfigurationDetails(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    alias: Optional[str] = Field(default=None, alias="Alias")
    configuration: Optional[str] = Field(default=None, alias="Configuration")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    is_default_configuration: Optional[bool] = Field(
        default=None, alias="IsDefaultConfiguration"
    )


class CancelUpdateStackInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class CancelUpdateStackInputStackCancelUpdate(BaseModel):
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ChangeSetHookResourceTargetDetails(BaseModel):
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_action: Optional[
        Literal["Add", "Dynamic", "Import", "Modify", "Remove"]
    ] = Field(default=None, alias="ResourceAction")


class ChangeSetSummary(BaseModel):
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


class ContinueUpdateRollbackInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    resources_to_skip: Optional[Sequence[str]] = Field(
        default=None, alias="ResourcesToSkip"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class Parameter(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    use_previous_value: Optional[bool] = Field(default=None, alias="UsePreviousValue")
    resolved_value: Optional[str] = Field(default=None, alias="ResolvedValue")


class ResourceToImport(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    logical_resource_id: str = Field(alias="LogicalResourceId")
    resource_identifier: Mapping[str, str] = Field(alias="ResourceIdentifier")


class Tag(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeploymentTargets(BaseModel):
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    accounts_url: Optional[str] = Field(default=None, alias="AccountsUrl")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    account_filter_type: Optional[
        Literal["DIFFERENCE", "INTERSECTION", "NONE", "UNION"]
    ] = Field(default=None, alias="AccountFilterType")


class StackSetOperationPreferences(BaseModel):
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


class ManagedExecution(BaseModel):
    active: Optional[bool] = Field(default=None, alias="Active")


class DeactivateTypeInputRequest(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")


class DeleteChangeSetInputRequest(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")


class DeleteStackInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    retain_resources: Optional[Sequence[str]] = Field(
        default=None, alias="RetainResources"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteStackInputStackDelete(BaseModel):
    retain_resources: Optional[Sequence[str]] = Field(
        default=None, alias="RetainResources"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteStackSetInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DeregisterTypeInputRequest(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class PaginatorConfig(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccountLimitsInputRequest(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeChangeSetHooksInputRequest(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")


class WaiterConfig(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeChangeSetInputRequest(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePublisherInputRequest(BaseModel):
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")


class DescribeStackDriftDetectionStatusInputRequest(BaseModel):
    stack_drift_detection_id: str = Field(alias="StackDriftDetectionId")


class DescribeStackEventsInputRequest(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StackEvent(BaseModel):
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


class DescribeStackInstanceInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    stack_instance_account: str = Field(alias="StackInstanceAccount")
    stack_instance_region: str = Field(alias="StackInstanceRegion")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStackResourceDriftsInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    stack_resource_drift_status_filters: Optional[
        Sequence[Literal["DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"]]
    ] = Field(default=None, alias="StackResourceDriftStatusFilters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeStackResourceInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")


class DescribeStackResourcesInputRequest(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    logical_resource_id: Optional[str] = Field(default=None, alias="LogicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="PhysicalResourceId"
    )


class DescribeStackSetInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStackSetOperationInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DescribeStacksInputRequest(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeTypeInputRequest(BaseModel):
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


class RequiredActivatedType(BaseModel):
    type_name_alias: Optional[str] = Field(default=None, alias="TypeNameAlias")
    original_type_name: Optional[str] = Field(default=None, alias="OriginalTypeName")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    supported_major_versions: Optional[List[int]] = Field(
        default=None, alias="SupportedMajorVersions"
    )


class DescribeTypeRegistrationInputRequest(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")


class DetectStackDriftInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_ids: Optional[Sequence[str]] = Field(
        default=None, alias="LogicalResourceIds"
    )


class DetectStackResourceDriftInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")


class ExecuteChangeSetInputRequest(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")


class Export(BaseModel):
    exporting_stack_id: Optional[str] = Field(default=None, alias="ExportingStackId")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class GetStackPolicyInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")


class GetTemplateInputRequest(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    template_stage: Optional[Literal["Original", "Processed"]] = Field(
        default=None, alias="TemplateStage"
    )


class GetTemplateSummaryInputRequest(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ResourceIdentifierSummary(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    logical_resource_ids: Optional[List[str]] = Field(
        default=None, alias="LogicalResourceIds"
    )
    resource_identifiers: Optional[List[str]] = Field(
        default=None, alias="ResourceIdentifiers"
    )


class ListChangeSetsInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExportsInputRequest(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListImportsInputRequest(BaseModel):
    export_name: str = Field(alias="ExportName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StackInstanceFilter(BaseModel):
    name: Optional[Literal["DETAILED_STATUS", "LAST_OPERATION_ID"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[str] = Field(default=None, alias="Values")


class ListStackResourcesInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OperationResultFilter(BaseModel):
    name: Optional[Literal["OPERATION_RESULT_STATUS"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[str] = Field(default=None, alias="Values")


class ListStackSetOperationsInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ListStackSetsInputRequest(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ListStacksInputRequest(BaseModel):
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


class ListTypeRegistrationsInputRequest(BaseModel):
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


class ListTypeVersionsInputRequest(BaseModel):
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


class TypeVersionSummary(BaseModel):
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


class TypeFilters(BaseModel):
    category: Optional[
        Literal["ACTIVATED", "AWS_TYPES", "REGISTERED", "THIRD_PARTY"]
    ] = Field(default=None, alias="Category")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    type_name_prefix: Optional[str] = Field(default=None, alias="TypeNamePrefix")


class TypeSummary(BaseModel):
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


class ModuleInfo(BaseModel):
    type_hierarchy: Optional[str] = Field(default=None, alias="TypeHierarchy")
    logical_id_hierarchy: Optional[str] = Field(
        default=None, alias="LogicalIdHierarchy"
    )


class Output(BaseModel):
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_value: Optional[str] = Field(default=None, alias="OutputValue")
    description: Optional[str] = Field(default=None, alias="Description")
    export_name: Optional[str] = Field(default=None, alias="ExportName")


class ParameterConstraints(BaseModel):
    allowed_values: Optional[List[str]] = Field(default=None, alias="AllowedValues")


class PhysicalResourceIdContextKeyValuePair(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PropertyDifference(BaseModel):
    property_path: str = Field(alias="PropertyPath")
    expected_value: str = Field(alias="ExpectedValue")
    actual_value: str = Field(alias="ActualValue")
    difference_type: Literal["ADD", "NOT_EQUAL", "REMOVE"] = Field(
        alias="DifferenceType"
    )


class PublishTypeInputRequest(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    public_version_number: Optional[str] = Field(
        default=None, alias="PublicVersionNumber"
    )


class RecordHandlerProgressInputRequest(BaseModel):
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


class RegisterPublisherInputRequest(BaseModel):
    accept_terms_and_conditions: Optional[bool] = Field(
        default=None, alias="AcceptTermsAndConditions"
    )
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")


class ResourceTargetDefinition(BaseModel):
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


class RollbackTrigger(BaseModel):
    arn: str = Field(alias="Arn")
    type: str = Field(alias="Type")


class RollbackStackInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ServiceResourceEventRequest(BaseModel):
    id: str = Field(alias="id")


class ServiceResourceStackRequest(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceStackResourceRequest(BaseModel):
    stack_name: str = Field(alias="stack_name")
    logical_id: str = Field(alias="logical_id")


class ServiceResourceStackResourceSummaryRequest(BaseModel):
    stack_name: str = Field(alias="stack_name")
    logical_id: str = Field(alias="logical_id")


class SetStackPolicyInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")


class SetTypeConfigurationInputRequest(BaseModel):
    configuration: str = Field(alias="Configuration")
    type_arn: Optional[str] = Field(default=None, alias="TypeArn")
    configuration_alias: Optional[str] = Field(default=None, alias="ConfigurationAlias")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )


class SetaultVersionInputRequest(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class SignalResourceInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    logical_resource_id: str = Field(alias="LogicalResourceId")
    unique_id: str = Field(alias="UniqueId")
    status: Literal["FAILURE", "SUCCESS"] = Field(alias="Status")


class StackDriftInformationSummary(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackDriftInformation(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackInstanceComprehensiveStatus(BaseModel):
    detailed_status: Optional[
        Literal["CANCELLED", "FAILED", "INOPERABLE", "PENDING", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="DetailedStatus")


class StackResourceDriftInformation(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackResourceDriftInformationSummary(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: Optional[datetime] = Field(
        default=None, alias="LastCheckTimestamp"
    )


class StackResourceRequest(BaseModel):
    logical_id: str = Field(alias="logical_id")


class StackSetDriftDetectionDetails(BaseModel):
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


class StackSetOperationStatusDetails(BaseModel):
    failed_stack_instances_count: Optional[int] = Field(
        default=None, alias="FailedStackInstancesCount"
    )


class StopStackSetOperationInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class TemplateParameter(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    no_echo: Optional[bool] = Field(default=None, alias="NoEcho")
    description: Optional[str] = Field(default=None, alias="Description")


class TestTypeInputRequest(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    log_delivery_bucket: Optional[str] = Field(default=None, alias="LogDeliveryBucket")


class UpdateTerminationProtectionInputRequest(BaseModel):
    enable_termination_protection: bool = Field(alias="EnableTerminationProtection")
    stack_name: str = Field(alias="StackName")


class ValidateTemplateInputRequest(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")


class StackSetOperationResultSummary(BaseModel):
    account: Optional[str] = Field(default=None, alias="Account")
    region: Optional[str] = Field(default=None, alias="Region")
    status: Optional[
        Literal["CANCELLED", "FAILED", "PENDING", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    account_gate_result: Optional[AccountGateResult] = Field(
        default=None, alias="AccountGateResult"
    )
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )


class ActivateTypeInputRequest(BaseModel):
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    public_type_arn: Optional[str] = Field(default=None, alias="PublicTypeArn")
    publisher_id: Optional[str] = Field(default=None, alias="PublisherId")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    type_name_alias: Optional[str] = Field(default=None, alias="TypeNameAlias")
    auto_update: Optional[bool] = Field(default=None, alias="AutoUpdate")
    logging_config: Optional[LoggingConfig] = Field(default=None, alias="LoggingConfig")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    version_bump: Optional[Literal["MAJOR", "MINOR"]] = Field(
        default=None, alias="VersionBump"
    )
    major_version: Optional[int] = Field(default=None, alias="MajorVersion")


class RegisterTypeInputRequest(BaseModel):
    type_name: str = Field(alias="TypeName")
    schema_handler_package: str = Field(alias="SchemaHandlerPackage")
    type: Optional[Literal["HOOK", "MODULE", "RESOURCE"]] = Field(
        default=None, alias="Type"
    )
    logging_config: Optional[LoggingConfig] = Field(default=None, alias="LoggingConfig")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ActivateTypeOutput(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateChangeSetOutput(BaseModel):
    id: str = Field(alias="Id")
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateStackInstancesOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateStackOutput(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateStackSetOutput(BaseModel):
    stack_set_id: str = Field(alias="StackSetId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DeleteStackInstancesOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeAccountLimitsOutput(BaseModel):
    account_limits: List[AccountLimit] = Field(alias="AccountLimits")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribePublisherOutput(BaseModel):
    publisher_id: str = Field(alias="PublisherId")
    publisher_status: Literal["UNVERIFIED", "VERIFIED"] = Field(alias="PublisherStatus")
    identity_provider: Literal["AWS_Marketplace", "Bitbucket", "GitHub"] = Field(
        alias="IdentityProvider"
    )
    publisher_profile: str = Field(alias="PublisherProfile")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackDriftDetectionStatusOutput(BaseModel):
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
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeTypeRegistrationOutput(BaseModel):
    progress_status: Literal["COMPLETE", "FAILED", "IN_PROGRESS"] = Field(
        alias="ProgressStatus"
    )
    description: str = Field(alias="Description")
    type_arn: str = Field(alias="TypeArn")
    type_version_arn: str = Field(alias="TypeVersionArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DetectStackDriftOutput(BaseModel):
    stack_drift_detection_id: str = Field(alias="StackDriftDetectionId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DetectStackSetDriftOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class EmptyResponseMetadata(BaseModel):
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class EstimateTemplateCostOutput(BaseModel):
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetStackPolicyOutput(BaseModel):
    stack_policy_body: str = Field(alias="StackPolicyBody")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetTemplateOutput(BaseModel):
    template_body: Dict[str, Any] = Field(alias="TemplateBody")
    stages_available: List[Literal["Original", "Processed"]] = Field(
        alias="StagesAvailable"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ImportStacksToStackSetOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListImportsOutput(BaseModel):
    imports: List[str] = Field(alias="Imports")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListTypeRegistrationsOutput(BaseModel):
    registration_token_list: List[str] = Field(alias="RegistrationTokenList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ModuleInfoResponseMetadata(BaseModel):
    type_hierarchy: str = Field(alias="TypeHierarchy")
    logical_id_hierarchy: str = Field(alias="LogicalIdHierarchy")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PublishTypeOutput(BaseModel):
    public_type_arn: str = Field(alias="PublicTypeArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RegisterPublisherOutput(BaseModel):
    publisher_id: str = Field(alias="PublisherId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RegisterTypeOutput(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RollbackStackOutput(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class SetTypeConfigurationOutput(BaseModel):
    configuration_arn: str = Field(alias="ConfigurationArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class StackDriftInformationResponseMetadata(BaseModel):
    stack_drift_status: Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"] = Field(
        alias="StackDriftStatus"
    )
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class StackResourceDriftInformationResponseMetadata(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class StackResourceDriftInformationSummaryResponseMetadata(BaseModel):
    stack_resource_drift_status: Literal[
        "DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"
    ] = Field(alias="StackResourceDriftStatus")
    last_check_timestamp: datetime = Field(alias="LastCheckTimestamp")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class TestTypeOutput(BaseModel):
    type_version_arn: str = Field(alias="TypeVersionArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateStackInstancesOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateStackOutput(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateStackSetOutput(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateTerminationProtectionOutput(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class BatchDescribeTypeConfigurationsError(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    type_configuration_identifier: Optional[TypeConfigurationIdentifier] = Field(
        default=None, alias="TypeConfigurationIdentifier"
    )


class BatchDescribeTypeConfigurationsInputRequest(BaseModel):
    type_configuration_identifiers: Sequence[TypeConfigurationIdentifier] = Field(
        alias="TypeConfigurationIdentifiers"
    )


class ChangeSetHookTargetDetails(BaseModel):
    target_type: Optional[Literal["RESOURCE"]] = Field(default=None, alias="TargetType")
    resource_target_details: Optional[ChangeSetHookResourceTargetDetails] = Field(
        default=None, alias="ResourceTargetDetails"
    )


class ListChangeSetsOutput(BaseModel):
    summaries: List[ChangeSetSummary] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class EstimateTemplateCostInputRequest(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")


class CreateStackInstancesInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargets] = Field(
        default=None, alias="DeploymentTargets"
    )
    parameter_overrides: Optional[Sequence[Parameter]] = Field(
        default=None, alias="ParameterOverrides"
    )
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DeleteStackInstancesInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    retain_stacks: bool = Field(alias="RetainStacks")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargets] = Field(
        default=None, alias="DeploymentTargets"
    )
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class DetectStackSetDriftInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class ImportStacksToStackSetInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    stack_ids: Optional[Sequence[str]] = Field(default=None, alias="StackIds")
    stack_ids_url: Optional[str] = Field(default=None, alias="StackIdsUrl")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class UpdateStackInstancesInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    regions: Sequence[str] = Field(alias="Regions")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    deployment_targets: Optional[DeploymentTargets] = Field(
        default=None, alias="DeploymentTargets"
    )
    parameter_overrides: Optional[Sequence[Parameter]] = Field(
        default=None, alias="ParameterOverrides"
    )
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )


class CreateStackSetInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    description: Optional[str] = Field(default=None, alias="Description")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    auto_deployment: Optional[AutoDeployment] = Field(
        default=None, alias="AutoDeployment"
    )
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    managed_execution: Optional[ManagedExecution] = Field(
        default=None, alias="ManagedExecution"
    )


class StackSetSummary(BaseModel):
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    auto_deployment: Optional[AutoDeployment] = Field(
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
    managed_execution: Optional[ManagedExecution] = Field(
        default=None, alias="ManagedExecution"
    )


class UpdateStackSetInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    description: Optional[str] = Field(default=None, alias="Description")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    deployment_targets: Optional[DeploymentTargets] = Field(
        default=None, alias="DeploymentTargets"
    )
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    auto_deployment: Optional[AutoDeployment] = Field(
        default=None, alias="AutoDeployment"
    )
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    managed_execution: Optional[ManagedExecution] = Field(
        default=None, alias="ManagedExecution"
    )


class DescribeAccountLimitsInputDescribeAccountLimitsPaginate(BaseModel):
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeChangeSetInputDescribeChangeSetPaginate(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStackEventsInputDescribeStackEventsPaginate(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStacksInputDescribeStacksPaginate(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListChangeSetsInputListChangeSetsPaginate(BaseModel):
    stack_name: str = Field(alias="StackName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExportsInputListExportsPaginate(BaseModel):
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImportsInputListImportsPaginate(BaseModel):
    export_name: str = Field(alias="ExportName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackResourcesInputListStackResourcesPaginate(BaseModel):
    stack_name: str = Field(alias="StackName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetOperationsInputListStackSetOperationsPaginate(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetsInputListStackSetsPaginate(BaseModel):
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStacksInputListStacksPaginate(BaseModel):
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
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeChangeSetInputChangeSetCreateCompleteWait(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackCreateCompleteWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackDeleteCompleteWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackExistsWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackImportCompleteWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackRollbackCompleteWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStacksInputStackUpdateCompleteWait(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeTypeRegistrationInputTypeRegistrationCompleteWait(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class DescribeStackEventsOutput(BaseModel):
    stack_events: List[StackEvent] = Field(alias="StackEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeTypeOutput(BaseModel):
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
    schema: str = Field(alias="Schema")
    provisioning_type: Literal[
        "FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"
    ] = Field(alias="ProvisioningType")
    deprecated_status: Literal["DEPRECATED", "LIVE"] = Field(alias="DeprecatedStatus")
    logging_config: LoggingConfig = Field(alias="LoggingConfig")
    required_activated_types: List[RequiredActivatedType] = Field(
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
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListExportsOutput(BaseModel):
    exports: List[Export] = Field(alias="Exports")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListStackInstancesInputListStackInstancesPaginate(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    filters: Optional[Sequence[StackInstanceFilter]] = Field(
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
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackInstancesInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[StackInstanceFilter]] = Field(
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


class ListStackSetOperationResultsInputListStackSetOperationResultsPaginate(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    filters: Optional[Sequence[OperationResultFilter]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStackSetOperationResultsInputRequest(BaseModel):
    stack_set_name: str = Field(alias="StackSetName")
    operation_id: str = Field(alias="OperationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    call_as: Optional[Literal["DELEGATED_ADMIN", "SELF"]] = Field(
        default=None, alias="CallAs"
    )
    filters: Optional[Sequence[OperationResultFilter]] = Field(
        default=None, alias="Filters"
    )


class ListTypeVersionsOutput(BaseModel):
    type_version_summaries: List[TypeVersionSummary] = Field(
        alias="TypeVersionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListTypesInputListTypesPaginate(BaseModel):
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
    filters: Optional[TypeFilters] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTypesInputRequest(BaseModel):
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
    filters: Optional[TypeFilters] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTypesOutput(BaseModel):
    type_summaries: List[TypeSummary] = Field(alias="TypeSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ParameterDeclaration(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="ParameterKey")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    parameter_type: Optional[str] = Field(default=None, alias="ParameterType")
    no_echo: Optional[bool] = Field(default=None, alias="NoEcho")
    description: Optional[str] = Field(default=None, alias="Description")
    parameter_constraints: Optional[ParameterConstraints] = Field(
        default=None, alias="ParameterConstraints"
    )


class StackResourceDrift(BaseModel):
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
        List[PhysicalResourceIdContextKeyValuePair]
    ] = Field(default=None, alias="PhysicalResourceIdContext")
    expected_properties: Optional[str] = Field(default=None, alias="ExpectedProperties")
    actual_properties: Optional[str] = Field(default=None, alias="ActualProperties")
    property_differences: Optional[List[PropertyDifference]] = Field(
        default=None, alias="PropertyDifferences"
    )
    module_info: Optional[ModuleInfo] = Field(default=None, alias="ModuleInfo")


class ResourceChangeDetail(BaseModel):
    target: Optional[ResourceTargetDefinition] = Field(default=None, alias="Target")
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


class RollbackConfigurationResponseMetadata(BaseModel):
    rollback_triggers: List[RollbackTrigger] = Field(alias="RollbackTriggers")
    monitoring_time_in_minutes: int = Field(alias="MonitoringTimeInMinutes")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RollbackConfiguration(BaseModel):
    rollback_triggers: Optional[Sequence[RollbackTrigger]] = Field(
        default=None, alias="RollbackTriggers"
    )
    monitoring_time_in_minutes: Optional[int] = Field(
        default=None, alias="MonitoringTimeInMinutes"
    )


class StackSummary(BaseModel):
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
    drift_information: Optional[StackDriftInformationSummary] = Field(
        default=None, alias="DriftInformation"
    )


class StackInstanceSummary(BaseModel):
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    region: Optional[str] = Field(default=None, alias="Region")
    account: Optional[str] = Field(default=None, alias="Account")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    status: Optional[Literal["CURRENT", "INOPERABLE", "OUTDATED"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    stack_instance_status: Optional[StackInstanceComprehensiveStatus] = Field(
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


class StackInstance(BaseModel):
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    region: Optional[str] = Field(default=None, alias="Region")
    account: Optional[str] = Field(default=None, alias="Account")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    parameter_overrides: Optional[List[Parameter]] = Field(
        default=None, alias="ParameterOverrides"
    )
    status: Optional[Literal["CURRENT", "INOPERABLE", "OUTDATED"]] = Field(
        default=None, alias="Status"
    )
    stack_instance_status: Optional[StackInstanceComprehensiveStatus] = Field(
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


class StackResourceDetail(BaseModel):
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
    drift_information: Optional[StackResourceDriftInformation] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfo] = Field(default=None, alias="ModuleInfo")


class StackResource(BaseModel):
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
    drift_information: Optional[StackResourceDriftInformation] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfo] = Field(default=None, alias="ModuleInfo")


class StackResourceSummary(BaseModel):
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
    drift_information: Optional[StackResourceDriftInformationSummary] = Field(
        default=None, alias="DriftInformation"
    )
    module_info: Optional[ModuleInfo] = Field(default=None, alias="ModuleInfo")


class StackSet(BaseModel):
    stack_set_name: Optional[str] = Field(default=None, alias="StackSetName")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "DELETED"]] = Field(default=None, alias="Status")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    parameters: Optional[List[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        List[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    tags: Optional[List[Tag]] = Field(default=None, alias="Tags")
    stack_set_arn: Optional[str] = Field(default=None, alias="StackSetARN")
    administration_role_arn: Optional[str] = Field(
        default=None, alias="AdministrationRoleARN"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    stack_set_drift_detection_details: Optional[StackSetDriftDetectionDetails] = Field(
        default=None, alias="StackSetDriftDetectionDetails"
    )
    auto_deployment: Optional[AutoDeployment] = Field(
        default=None, alias="AutoDeployment"
    )
    permission_model: Optional[Literal["SELF_MANAGED", "SERVICE_MANAGED"]] = Field(
        default=None, alias="PermissionModel"
    )
    organizational_unit_ids: Optional[List[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    managed_execution: Optional[ManagedExecution] = Field(
        default=None, alias="ManagedExecution"
    )
    regions: Optional[List[str]] = Field(default=None, alias="Regions")


class StackSetOperationSummary(BaseModel):
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
    status_details: Optional[StackSetOperationStatusDetails] = Field(
        default=None, alias="StatusDetails"
    )
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
        default=None, alias="OperationPreferences"
    )


class StackSetOperation(BaseModel):
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    stack_set_id: Optional[str] = Field(default=None, alias="StackSetId")
    action: Optional[Literal["CREATE", "DELETE", "DETECT_DRIFT", "UPDATE"]] = Field(
        default=None, alias="Action"
    )
    status: Optional[
        Literal["FAILED", "QUEUED", "RUNNING", "STOPPED", "STOPPING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    operation_preferences: Optional[StackSetOperationPreferences] = Field(
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
    deployment_targets: Optional[DeploymentTargets] = Field(
        default=None, alias="DeploymentTargets"
    )
    stack_set_drift_detection_details: Optional[StackSetDriftDetectionDetails] = Field(
        default=None, alias="StackSetDriftDetectionDetails"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    status_details: Optional[StackSetOperationStatusDetails] = Field(
        default=None, alias="StatusDetails"
    )


class ValidateTemplateOutput(BaseModel):
    parameters: List[TemplateParameter] = Field(alias="Parameters")
    description: str = Field(alias="Description")
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    capabilities_reason: str = Field(alias="CapabilitiesReason")
    declared_transforms: List[str] = Field(alias="DeclaredTransforms")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListStackSetOperationResultsOutput(BaseModel):
    summaries: List[StackSetOperationResultSummary] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class BatchDescribeTypeConfigurationsOutput(BaseModel):
    errors: List[BatchDescribeTypeConfigurationsError] = Field(alias="Errors")
    unprocessed_type_configurations: List[TypeConfigurationIdentifier] = Field(
        alias="UnprocessedTypeConfigurations"
    )
    type_configurations: List[TypeConfigurationDetails] = Field(
        alias="TypeConfigurations"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ChangeSetHook(BaseModel):
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
    target_details: Optional[ChangeSetHookTargetDetails] = Field(
        default=None, alias="TargetDetails"
    )


class ListStackSetsOutput(BaseModel):
    summaries: List[StackSetSummary] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetTemplateSummaryOutput(BaseModel):
    parameters: List[ParameterDeclaration] = Field(alias="Parameters")
    description: str = Field(alias="Description")
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    capabilities_reason: str = Field(alias="CapabilitiesReason")
    resource_types: List[str] = Field(alias="ResourceTypes")
    version: str = Field(alias="Version")
    metadata: str = Field(alias="Metadata")
    declared_transforms: List[str] = Field(alias="DeclaredTransforms")
    resource_identifier_summaries: List[ResourceIdentifierSummary] = Field(
        alias="ResourceIdentifierSummaries"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackResourceDriftsOutput(BaseModel):
    stack_resource_drifts: List[StackResourceDrift] = Field(alias="StackResourceDrifts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DetectStackResourceDriftOutput(BaseModel):
    stack_resource_drift: StackResourceDrift = Field(alias="StackResourceDrift")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ResourceChange(BaseModel):
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
    details: Optional[List[ResourceChangeDetail]] = Field(default=None, alias="Details")
    change_set_id: Optional[str] = Field(default=None, alias="ChangeSetId")
    module_info: Optional[ModuleInfo] = Field(default=None, alias="ModuleInfo")


class CreateChangeSetInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    change_set_name: str = Field(alias="ChangeSetName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    use_previous_template: Optional[bool] = Field(
        default=None, alias="UsePreviousTemplate"
    )
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
        default=None, alias="RollbackConfiguration"
    )
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    change_set_type: Optional[Literal["CREATE", "IMPORT", "UPDATE"]] = Field(
        default=None, alias="ChangeSetType"
    )
    resources_to_import: Optional[Sequence[ResourceToImport]] = Field(
        default=None, alias="ResourcesToImport"
    )
    include_nested_stacks: Optional[bool] = Field(
        default=None, alias="IncludeNestedStacks"
    )


class CreateStackInputRequest(BaseModel):
    stack_name: str = Field(alias="StackName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
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
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )


class CreateStackInputServiceResourceCreateStack(BaseModel):
    stack_name: str = Field(alias="StackName")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    template_url: Optional[str] = Field(default=None, alias="TemplateURL")
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
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
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )


class Stack(BaseModel):
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
    parameters: Optional[List[Parameter]] = Field(default=None, alias="Parameters")
    deletion_time: Optional[datetime] = Field(default=None, alias="DeletionTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
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
    outputs: Optional[List[Output]] = Field(default=None, alias="Outputs")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    tags: Optional[List[Tag]] = Field(default=None, alias="Tags")
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )
    parent_id: Optional[str] = Field(default=None, alias="ParentId")
    root_id: Optional[str] = Field(default=None, alias="RootId")
    drift_information: Optional[StackDriftInformation] = Field(
        default=None, alias="DriftInformation"
    )


class UpdateStackInputRequest(BaseModel):
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
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
        default=None, alias="RollbackConfiguration"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class UpdateStackInputStackUpdate(BaseModel):
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
    parameters: Optional[Sequence[Parameter]] = Field(default=None, alias="Parameters")
    capabilities: Optional[
        Sequence[
            Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
        ]
    ] = Field(default=None, alias="Capabilities")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    rollback_configuration: Optional[RollbackConfiguration] = Field(
        default=None, alias="RollbackConfiguration"
    )
    stack_policy_body: Optional[str] = Field(default=None, alias="StackPolicyBody")
    stack_policy_url: Optional[str] = Field(default=None, alias="StackPolicyURL")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationARNs"
    )
    tags: Optional[Sequence[Tag]] = Field(default=None, alias="Tags")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ListStacksOutput(BaseModel):
    stack_summaries: List[StackSummary] = Field(alias="StackSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListStackInstancesOutput(BaseModel):
    summaries: List[StackInstanceSummary] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackInstanceOutput(BaseModel):
    stack_instance: StackInstance = Field(alias="StackInstance")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackResourceOutput(BaseModel):
    stack_resource_detail: StackResourceDetail = Field(alias="StackResourceDetail")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackResourcesOutput(BaseModel):
    stack_resources: List[StackResource] = Field(alias="StackResources")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListStackResourcesOutput(BaseModel):
    stack_resource_summaries: List[StackResourceSummary] = Field(
        alias="StackResourceSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackSetOutput(BaseModel):
    stack_set: StackSet = Field(alias="StackSet")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListStackSetOperationsOutput(BaseModel):
    summaries: List[StackSetOperationSummary] = Field(alias="Summaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeStackSetOperationOutput(BaseModel):
    stack_set_operation: StackSetOperation = Field(alias="StackSetOperation")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeChangeSetHooksOutput(BaseModel):
    change_set_id: str = Field(alias="ChangeSetId")
    change_set_name: str = Field(alias="ChangeSetName")
    hooks: List[ChangeSetHook] = Field(alias="Hooks")
    status: Literal["PLANNED", "PLANNING", "UNAVAILABLE"] = Field(alias="Status")
    next_token: str = Field(alias="NextToken")
    stack_id: str = Field(alias="StackId")
    stack_name: str = Field(alias="StackName")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class Change(BaseModel):
    type: Optional[Literal["Resource"]] = Field(default=None, alias="Type")
    hook_invocation_count: Optional[int] = Field(
        default=None, alias="HookInvocationCount"
    )
    resource_change: Optional[ResourceChange] = Field(
        default=None, alias="ResourceChange"
    )


class DescribeStacksOutput(BaseModel):
    stacks: List[Stack] = Field(alias="Stacks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class DescribeChangeSetOutput(BaseModel):
    change_set_name: str = Field(alias="ChangeSetName")
    change_set_id: str = Field(alias="ChangeSetId")
    stack_id: str = Field(alias="StackId")
    stack_name: str = Field(alias="StackName")
    description: str = Field(alias="Description")
    parameters: List[Parameter] = Field(alias="Parameters")
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
    rollback_configuration: RollbackConfiguration = Field(alias="RollbackConfiguration")
    capabilities: List[
        Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    ] = Field(alias="Capabilities")
    tags: List[Tag] = Field(alias="Tags")
    changes: List[Change] = Field(alias="Changes")
    next_token: str = Field(alias="NextToken")
    include_nested_stacks: bool = Field(alias="IncludeNestedStacks")
    parent_change_set_id: str = Field(alias="ParentChangeSetId")
    root_change_set_id: str = Field(alias="RootChangeSetId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")
