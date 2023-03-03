# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountSharingInfoModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    shared_document_version: Optional[str] = Field(
        default=None, alias="SharedDocumentVersion"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AlarmModel(BaseModel):
    name: str = Field(alias="Name")


class AlarmStateInformationModel(BaseModel):
    name: str = Field(alias="Name")
    state: Literal["ALARM", "UNKNOWN"] = Field(alias="State")


class AssociateOpsItemRelatedItemRequestModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")
    association_type: str = Field(alias="AssociationType")
    resource_type: str = Field(alias="ResourceType")
    resource_uri: str = Field(alias="ResourceUri")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociationOverviewModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    detailed_status: Optional[str] = Field(default=None, alias="DetailedStatus")
    association_status_aggregated_count: Optional[Dict[str, int]] = Field(
        default=None, alias="AssociationStatusAggregatedCount"
    )


class AssociationStatusModel(BaseModel):
    date: datetime = Field(alias="Date")
    name: Literal["Failed", "Pending", "Success"] = Field(alias="Name")
    message: str = Field(alias="Message")
    additional_info: Optional[str] = Field(default=None, alias="AdditionalInfo")


class TargetModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class AssociationExecutionFilterModel(BaseModel):
    key: Literal["CreatedTime", "ExecutionId", "Status"] = Field(alias="Key")
    value: str = Field(alias="Value")
    type: Literal["EQUAL", "GREATER_THAN", "LESS_THAN"] = Field(alias="Type")


class OutputSourceModel(BaseModel):
    output_source_id: Optional[str] = Field(default=None, alias="OutputSourceId")
    output_source_type: Optional[str] = Field(default=None, alias="OutputSourceType")


class AssociationExecutionTargetsFilterModel(BaseModel):
    key: Literal["ResourceId", "ResourceType", "Status"] = Field(alias="Key")
    value: str = Field(alias="Value")


class AssociationFilterModel(BaseModel):
    key: Literal[
        "AssociationId",
        "AssociationName",
        "AssociationStatusName",
        "InstanceId",
        "LastExecutedAfter",
        "LastExecutedBefore",
        "Name",
        "ResourceGroupName",
    ] = Field(alias="key")
    value: str = Field(alias="value")


class AttachmentContentModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    size: Optional[int] = Field(default=None, alias="Size")
    hash: Optional[str] = Field(default=None, alias="Hash")
    hash_type: Optional[Literal["Sha256"]] = Field(default=None, alias="HashType")
    url: Optional[str] = Field(default=None, alias="Url")


class AttachmentInformationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class AttachmentsSourceModel(BaseModel):
    key: Optional[Literal["AttachmentReference", "S3FileUrl", "SourceUrl"]] = Field(
        default=None, alias="Key"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    name: Optional[str] = Field(default=None, alias="Name")


class AutomationExecutionFilterModel(BaseModel):
    key: Literal[
        "AutomationSubtype",
        "AutomationType",
        "CurrentAction",
        "DocumentNamePrefix",
        "ExecutionId",
        "ExecutionStatus",
        "OpsItemId",
        "ParentExecutionId",
        "StartTimeAfter",
        "StartTimeBefore",
        "TagKey",
        "TargetResourceGroup",
    ] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class ResolvedTargetsModel(BaseModel):
    parameter_values: Optional[List[str]] = Field(default=None, alias="ParameterValues")
    truncated: Optional[bool] = Field(default=None, alias="Truncated")


class ProgressCountersModel(BaseModel):
    total_steps: Optional[int] = Field(default=None, alias="TotalSteps")
    success_steps: Optional[int] = Field(default=None, alias="SuccessSteps")
    failed_steps: Optional[int] = Field(default=None, alias="FailedSteps")
    cancelled_steps: Optional[int] = Field(default=None, alias="CancelledSteps")
    timed_out_steps: Optional[int] = Field(default=None, alias="TimedOutSteps")


class PatchSourceModel(BaseModel):
    name: str = Field(alias="Name")
    products: Sequence[str] = Field(alias="Products")
    configuration: str = Field(alias="Configuration")


class CancelCommandRequestModel(BaseModel):
    command_id: str = Field(alias="CommandId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class CancelMaintenanceWindowExecutionRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")


class CloudWatchOutputConfigModel(BaseModel):
    cloud_watch_log_group_name: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupName"
    )
    cloud_watch_output_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchOutputEnabled"
    )


class CommandFilterModel(BaseModel):
    key: Literal[
        "DocumentName", "ExecutionStage", "InvokedAfter", "InvokedBefore", "Status"
    ] = Field(alias="key")
    value: str = Field(alias="value")


class CommandPluginModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["Cancelled", "Failed", "InProgress", "Pending", "Success", "TimedOut"]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    response_start_date_time: Optional[datetime] = Field(
        default=None, alias="ResponseStartDateTime"
    )
    response_finish_date_time: Optional[datetime] = Field(
        default=None, alias="ResponseFinishDateTime"
    )
    output: Optional[str] = Field(default=None, alias="Output")
    standard_output_url: Optional[str] = Field(default=None, alias="StandardOutputUrl")
    standard_error_url: Optional[str] = Field(default=None, alias="StandardErrorUrl")
    output_s3_region: Optional[str] = Field(default=None, alias="OutputS3Region")
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="OutputS3BucketName"
    )
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")


class NotificationConfigModel(BaseModel):
    notification_arn: Optional[str] = Field(default=None, alias="NotificationArn")
    notification_events: Optional[
        List[Literal["All", "Cancelled", "Failed", "InProgress", "Success", "TimedOut"]]
    ] = Field(default=None, alias="NotificationEvents")
    notification_type: Optional[Literal["Command", "Invocation"]] = Field(
        default=None, alias="NotificationType"
    )


class ComplianceExecutionSummaryModel(BaseModel):
    execution_time: datetime = Field(alias="ExecutionTime")
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    execution_type: Optional[str] = Field(default=None, alias="ExecutionType")


class ComplianceItemEntryModel(BaseModel):
    severity: Literal[
        "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
    ] = Field(alias="Severity")
    status: Literal["COMPLIANT", "NON_COMPLIANT"] = Field(alias="Status")
    id: Optional[str] = Field(default=None, alias="Id")
    title: Optional[str] = Field(default=None, alias="Title")
    details: Optional[Mapping[str, str]] = Field(default=None, alias="Details")


class ComplianceStringFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    type: Optional[
        Literal["BEGIN_WITH", "EQUAL", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL"]
    ] = Field(default=None, alias="Type")


class SeveritySummaryModel(BaseModel):
    critical_count: Optional[int] = Field(default=None, alias="CriticalCount")
    high_count: Optional[int] = Field(default=None, alias="HighCount")
    medium_count: Optional[int] = Field(default=None, alias="MediumCount")
    low_count: Optional[int] = Field(default=None, alias="LowCount")
    informational_count: Optional[int] = Field(default=None, alias="InformationalCount")
    unspecified_count: Optional[int] = Field(default=None, alias="UnspecifiedCount")


class RegistrationMetadataItemModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DocumentRequiresModel(BaseModel):
    name: str = Field(alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    require_type: Optional[str] = Field(default=None, alias="RequireType")
    version_name: Optional[str] = Field(default=None, alias="VersionName")


class OpsItemDataValueModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[Literal["SearchableString", "String"]] = Field(
        default=None, alias="Type"
    )


class OpsItemNotificationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class RelatedOpsItemModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")


class MetadataValueModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")


class DeleteActivationRequestModel(BaseModel):
    activation_id: str = Field(alias="ActivationId")


class DeleteAssociationRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")


class DeleteDocumentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    force: Optional[bool] = Field(default=None, alias="Force")


class DeleteInventoryRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    schema_delete_option: Optional[Literal["DeleteSchema", "DisableSchema"]] = Field(
        default=None, alias="SchemaDeleteOption"
    )
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")


class DeleteOpsMetadataRequestModel(BaseModel):
    ops_metadata_arn: str = Field(alias="OpsMetadataArn")


class DeleteParameterRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteParametersRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")


class DeletePatchBaselineRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")


class DeleteResourceDataSyncRequestModel(BaseModel):
    sync_name: str = Field(alias="SyncName")
    sync_type: Optional[str] = Field(default=None, alias="SyncType")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy_id: str = Field(alias="PolicyId")
    policy_hash: str = Field(alias="PolicyHash")


class DeregisterManagedInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class DeregisterPatchBaselineForPatchGroupRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    patch_group: str = Field(alias="PatchGroup")


class DeregisterTargetFromMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_target_id: str = Field(alias="WindowTargetId")
    safe: Optional[bool] = Field(default=None, alias="Safe")


class DeregisterTaskFromMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")


class DescribeActivationsFilterModel(BaseModel):
    filter_key: Optional[
        Literal["ActivationIds", "DefaultInstanceName", "IamRole"]
    ] = Field(default=None, alias="FilterKey")
    filter_values: Optional[Sequence[str]] = Field(default=None, alias="FilterValues")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAssociationRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")


class StepExecutionFilterModel(BaseModel):
    key: Literal[
        "Action",
        "StartTimeAfter",
        "StartTimeBefore",
        "StepExecutionId",
        "StepExecutionStatus",
        "StepName",
    ] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class PatchOrchestratorFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class PatchModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    release_date: Optional[datetime] = Field(default=None, alias="ReleaseDate")
    title: Optional[str] = Field(default=None, alias="Title")
    description: Optional[str] = Field(default=None, alias="Description")
    content_url: Optional[str] = Field(default=None, alias="ContentUrl")
    vendor: Optional[str] = Field(default=None, alias="Vendor")
    product_family: Optional[str] = Field(default=None, alias="ProductFamily")
    product: Optional[str] = Field(default=None, alias="Product")
    classification: Optional[str] = Field(default=None, alias="Classification")
    msrc_severity: Optional[str] = Field(default=None, alias="MsrcSeverity")
    kb_number: Optional[str] = Field(default=None, alias="KbNumber")
    msrc_number: Optional[str] = Field(default=None, alias="MsrcNumber")
    language: Optional[str] = Field(default=None, alias="Language")
    advisory_ids: Optional[List[str]] = Field(default=None, alias="AdvisoryIds")
    bugzilla_ids: Optional[List[str]] = Field(default=None, alias="BugzillaIds")
    cveids: Optional[List[str]] = Field(default=None, alias="CVEIds")
    name: Optional[str] = Field(default=None, alias="Name")
    epoch: Optional[int] = Field(default=None, alias="Epoch")
    version: Optional[str] = Field(default=None, alias="Version")
    release: Optional[str] = Field(default=None, alias="Release")
    arch: Optional[str] = Field(default=None, alias="Arch")
    severity: Optional[str] = Field(default=None, alias="Severity")
    repository: Optional[str] = Field(default=None, alias="Repository")


class DescribeDocumentPermissionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    permission_type: Literal["Share"] = Field(alias="PermissionType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeDocumentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    version_name: Optional[str] = Field(default=None, alias="VersionName")


class DescribeEffectiveInstanceAssociationsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class InstanceAssociationModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    content: Optional[str] = Field(default=None, alias="Content")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")


class DescribeEffectivePatchesForPatchBaselineRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstanceAssociationsStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class InstanceInformationFilterModel(BaseModel):
    key: Literal[
        "ActivationIds",
        "AgentVersion",
        "AssociationStatus",
        "IamRole",
        "InstanceIds",
        "PingStatus",
        "PlatformTypes",
        "ResourceType",
    ] = Field(alias="key")
    value_set: Sequence[str] = Field(alias="valueSet")


class InstanceInformationStringFilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class InstancePatchStateFilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    type: Literal["Equal", "GreaterThan", "LessThan", "NotEqual"] = Field(alias="Type")


class InstancePatchStateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    patch_group: str = Field(alias="PatchGroup")
    baseline_id: str = Field(alias="BaselineId")
    operation_start_time: datetime = Field(alias="OperationStartTime")
    operation_end_time: datetime = Field(alias="OperationEndTime")
    operation: Literal["Install", "Scan"] = Field(alias="Operation")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    install_override_list: Optional[str] = Field(
        default=None, alias="InstallOverrideList"
    )
    owner_information: Optional[str] = Field(default=None, alias="OwnerInformation")
    installed_count: Optional[int] = Field(default=None, alias="InstalledCount")
    installed_other_count: Optional[int] = Field(
        default=None, alias="InstalledOtherCount"
    )
    installed_pending_reboot_count: Optional[int] = Field(
        default=None, alias="InstalledPendingRebootCount"
    )
    installed_rejected_count: Optional[int] = Field(
        default=None, alias="InstalledRejectedCount"
    )
    missing_count: Optional[int] = Field(default=None, alias="MissingCount")
    failed_count: Optional[int] = Field(default=None, alias="FailedCount")
    unreported_not_applicable_count: Optional[int] = Field(
        default=None, alias="UnreportedNotApplicableCount"
    )
    not_applicable_count: Optional[int] = Field(
        default=None, alias="NotApplicableCount"
    )
    last_no_reboot_install_operation_time: Optional[datetime] = Field(
        default=None, alias="LastNoRebootInstallOperationTime"
    )
    reboot_option: Optional[Literal["NoReboot", "RebootIfNeeded"]] = Field(
        default=None, alias="RebootOption"
    )
    critical_non_compliant_count: Optional[int] = Field(
        default=None, alias="CriticalNonCompliantCount"
    )
    security_non_compliant_count: Optional[int] = Field(
        default=None, alias="SecurityNonCompliantCount"
    )
    other_non_compliant_count: Optional[int] = Field(
        default=None, alias="OtherNonCompliantCount"
    )


class DescribeInstancePatchStatesRequestModel(BaseModel):
    instance_ids: Sequence[str] = Field(alias="InstanceIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PatchComplianceDataModel(BaseModel):
    title: str = Field(alias="Title")
    kbid: str = Field(alias="KBId")
    classification: str = Field(alias="Classification")
    severity: str = Field(alias="Severity")
    state: Literal[
        "FAILED",
        "INSTALLED",
        "INSTALLED_OTHER",
        "INSTALLED_PENDING_REBOOT",
        "INSTALLED_REJECTED",
        "MISSING",
        "NOT_APPLICABLE",
    ] = Field(alias="State")
    installed_time: datetime = Field(alias="InstalledTime")
    cveids: Optional[str] = Field(default=None, alias="CVEIds")


class DescribeInventoryDeletionsRequestModel(BaseModel):
    deletion_id: Optional[str] = Field(default=None, alias="DeletionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MaintenanceWindowFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class MaintenanceWindowExecutionTaskInvocationIdentityModel(BaseModel):
    window_execution_id: Optional[str] = Field(default=None, alias="WindowExecutionId")
    task_execution_id: Optional[str] = Field(default=None, alias="TaskExecutionId")
    invocation_id: Optional[str] = Field(default=None, alias="InvocationId")
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    task_type: Optional[
        Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
    ] = Field(default=None, alias="TaskType")
    parameters: Optional[str] = Field(default=None, alias="Parameters")
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "SKIPPED_OVERLAPPING",
            "SUCCESS",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    owner_information: Optional[str] = Field(default=None, alias="OwnerInformation")
    window_target_id: Optional[str] = Field(default=None, alias="WindowTargetId")


class MaintenanceWindowExecutionModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    window_execution_id: Optional[str] = Field(default=None, alias="WindowExecutionId")
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "SKIPPED_OVERLAPPING",
            "SUCCESS",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class ScheduledWindowExecutionModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    name: Optional[str] = Field(default=None, alias="Name")
    execution_time: Optional[str] = Field(default=None, alias="ExecutionTime")


class MaintenanceWindowIdentityForTargetModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    name: Optional[str] = Field(default=None, alias="Name")


class MaintenanceWindowIdentityModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    duration: Optional[int] = Field(default=None, alias="Duration")
    cutoff: Optional[int] = Field(default=None, alias="Cutoff")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    schedule_timezone: Optional[str] = Field(default=None, alias="ScheduleTimezone")
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    next_execution_time: Optional[str] = Field(default=None, alias="NextExecutionTime")


class OpsItemFilterModel(BaseModel):
    key: Literal[
        "AccountId",
        "ActualEndTime",
        "ActualStartTime",
        "AutomationId",
        "Category",
        "ChangeRequestByApproverArn",
        "ChangeRequestByApproverName",
        "ChangeRequestByRequesterArn",
        "ChangeRequestByRequesterName",
        "ChangeRequestByTargetsResourceGroup",
        "ChangeRequestByTemplate",
        "CreatedBy",
        "CreatedTime",
        "InsightByType",
        "LastModifiedTime",
        "OperationalData",
        "OperationalDataKey",
        "OperationalDataValue",
        "OpsItemId",
        "OpsItemType",
        "PlannedEndTime",
        "PlannedStartTime",
        "Priority",
        "ResourceId",
        "Severity",
        "Source",
        "Status",
        "Title",
    ] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal["Contains", "Equal", "GreaterThan", "LessThan"] = Field(
        alias="Operator"
    )


class ParameterStringFilterModel(BaseModel):
    key: str = Field(alias="Key")
    option: Optional[str] = Field(default=None, alias="Option")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class ParametersFilterModel(BaseModel):
    key: Literal["KeyId", "Name", "Type"] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class PatchBaselineIdentityModel(BaseModel):
    baseline_id: Optional[str] = Field(default=None, alias="BaselineId")
    baseline_name: Optional[str] = Field(default=None, alias="BaselineName")
    operating_system: Optional[
        Literal[
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "AMAZON_LINUX_2022",
            "CENTOS",
            "DEBIAN",
            "MACOS",
            "ORACLE_LINUX",
            "RASPBIAN",
            "REDHAT_ENTERPRISE_LINUX",
            "ROCKY_LINUX",
            "SUSE",
            "UBUNTU",
            "WINDOWS",
        ]
    ] = Field(default=None, alias="OperatingSystem")
    baseline_description: Optional[str] = Field(
        default=None, alias="BaselineDescription"
    )
    default_baseline: Optional[bool] = Field(default=None, alias="DefaultBaseline")


class DescribePatchGroupStateRequestModel(BaseModel):
    patch_group: str = Field(alias="PatchGroup")


class DescribePatchPropertiesRequestModel(BaseModel):
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    property: Literal[
        "CLASSIFICATION",
        "MSRC_SEVERITY",
        "PRIORITY",
        "PRODUCT",
        "PRODUCT_FAMILY",
        "SEVERITY",
    ] = Field(alias="Property")
    patch_set: Optional[Literal["APPLICATION", "OS"]] = Field(
        default=None, alias="PatchSet"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SessionFilterModel(BaseModel):
    key: Literal[
        "InvokedAfter", "InvokedBefore", "Owner", "SessionId", "Status", "Target"
    ] = Field(alias="key")
    value: str = Field(alias="value")


class DisassociateOpsItemRelatedItemRequestModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")
    association_id: str = Field(alias="AssociationId")


class DocumentDefaultVersionDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    default_version: Optional[str] = Field(default=None, alias="DefaultVersion")
    default_version_name: Optional[str] = Field(
        default=None, alias="DefaultVersionName"
    )


class DocumentParameterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["String", "StringList"]] = Field(default=None, alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class ReviewInformationModel(BaseModel):
    reviewed_time: Optional[datetime] = Field(default=None, alias="ReviewedTime")
    status: Optional[
        Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="Status")
    reviewer: Optional[str] = Field(default=None, alias="Reviewer")


class DocumentFilterModel(BaseModel):
    key: Literal["DocumentType", "Name", "Owner", "PlatformTypes"] = Field(alias="key")
    value: str = Field(alias="value")


class DocumentKeyValuesFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DocumentReviewCommentSourceModel(BaseModel):
    type: Optional[Literal["Comment"]] = Field(default=None, alias="Type")
    content: Optional[str] = Field(default=None, alias="Content")


class DocumentVersionInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    is_default_version: Optional[bool] = Field(default=None, alias="IsDefaultVersion")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )
    status: Optional[
        Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
    ] = Field(default=None, alias="Status")
    status_information: Optional[str] = Field(default=None, alias="StatusInformation")
    review_status: Optional[
        Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="ReviewStatus")


class PatchStatusModel(BaseModel):
    deployment_status: Optional[
        Literal[
            "APPROVED", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED", "PENDING_APPROVAL"
        ]
    ] = Field(default=None, alias="DeploymentStatus")
    compliance_level: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceLevel")
    approval_date: Optional[datetime] = Field(default=None, alias="ApprovalDate")


class FailureDetailsModel(BaseModel):
    failure_stage: Optional[str] = Field(default=None, alias="FailureStage")
    failure_type: Optional[str] = Field(default=None, alias="FailureType")
    details: Optional[Dict[str, List[str]]] = Field(default=None, alias="Details")


class GetAutomationExecutionRequestModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")


class GetCalendarStateRequestModel(BaseModel):
    calendar_names: Sequence[str] = Field(alias="CalendarNames")
    at_time: Optional[str] = Field(default=None, alias="AtTime")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetCommandInvocationRequestModel(BaseModel):
    command_id: str = Field(alias="CommandId")
    instance_id: str = Field(alias="InstanceId")
    plugin_name: Optional[str] = Field(default=None, alias="PluginName")


class GetConnectionStatusRequestModel(BaseModel):
    target: str = Field(alias="Target")


class GetDefaultPatchBaselineRequestModel(BaseModel):
    operating_system: Optional[
        Literal[
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "AMAZON_LINUX_2022",
            "CENTOS",
            "DEBIAN",
            "MACOS",
            "ORACLE_LINUX",
            "RASPBIAN",
            "REDHAT_ENTERPRISE_LINUX",
            "ROCKY_LINUX",
            "SUSE",
            "UBUNTU",
            "WINDOWS",
        ]
    ] = Field(default=None, alias="OperatingSystem")


class GetDocumentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )


class InventoryFilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    type: Optional[
        Literal["BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"]
    ] = Field(default=None, alias="Type")


class ResultAttributeModel(BaseModel):
    type_name: str = Field(alias="TypeName")


class GetInventorySchemaRequestModel(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    aggregator: Optional[bool] = Field(default=None, alias="Aggregator")
    sub_type: Optional[bool] = Field(default=None, alias="SubType")


class GetMaintenanceWindowExecutionRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")


class GetMaintenanceWindowExecutionTaskInvocationRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_id: str = Field(alias="TaskId")
    invocation_id: str = Field(alias="InvocationId")


class GetMaintenanceWindowExecutionTaskRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_id: str = Field(alias="TaskId")


class MaintenanceWindowTaskParameterValueExpressionModel(BaseModel):
    values: Optional[List[str]] = Field(default=None, alias="Values")


class GetMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")


class GetMaintenanceWindowTaskRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")


class LoggingInfoModel(BaseModel):
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_region: str = Field(alias="S3Region")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")


class GetOpsItemRequestModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")
    ops_item_arn: Optional[str] = Field(default=None, alias="OpsItemArn")


class GetOpsMetadataRequestModel(BaseModel):
    ops_metadata_arn: str = Field(alias="OpsMetadataArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OpsFilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    type: Optional[
        Literal["BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"]
    ] = Field(default=None, alias="Type")


class OpsResultAttributeModel(BaseModel):
    type_name: str = Field(alias="TypeName")


class GetParameterHistoryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetParameterRequestModel(BaseModel):
    name: str = Field(alias="Name")
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")


class ParameterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["SecureString", "String", "StringList"]] = Field(
        default=None, alias="Type"
    )
    value: Optional[str] = Field(default=None, alias="Value")
    version: Optional[int] = Field(default=None, alias="Version")
    selector: Optional[str] = Field(default=None, alias="Selector")
    source_result: Optional[str] = Field(default=None, alias="SourceResult")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")
    data_type: Optional[str] = Field(default=None, alias="DataType")


class GetParametersRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")


class GetPatchBaselineForPatchGroupRequestModel(BaseModel):
    patch_group: str = Field(alias="PatchGroup")
    operating_system: Optional[
        Literal[
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "AMAZON_LINUX_2022",
            "CENTOS",
            "DEBIAN",
            "MACOS",
            "ORACLE_LINUX",
            "RASPBIAN",
            "REDHAT_ENTERPRISE_LINUX",
            "ROCKY_LINUX",
            "SUSE",
            "UBUNTU",
            "WINDOWS",
        ]
    ] = Field(default=None, alias="OperatingSystem")


class GetPatchBaselineRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")


class GetResourcePoliciesRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetResourcePoliciesResponseEntryModel(BaseModel):
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_hash: Optional[str] = Field(default=None, alias="PolicyHash")
    policy: Optional[str] = Field(default=None, alias="Policy")


class GetServiceSettingRequestModel(BaseModel):
    setting_id: str = Field(alias="SettingId")


class ServiceSettingModel(BaseModel):
    setting_id: Optional[str] = Field(default=None, alias="SettingId")
    setting_value: Optional[str] = Field(default=None, alias="SettingValue")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_user: Optional[str] = Field(default=None, alias="LastModifiedUser")
    arn: Optional[str] = Field(default=None, alias="ARN")
    status: Optional[str] = Field(default=None, alias="Status")


class InstanceAggregatedAssociationOverviewModel(BaseModel):
    detailed_status: Optional[str] = Field(default=None, alias="DetailedStatus")
    instance_association_status_aggregated_count: Optional[Dict[str, int]] = Field(
        default=None, alias="InstanceAssociationStatusAggregatedCount"
    )


class S3OutputLocationModel(BaseModel):
    output_s3_region: Optional[str] = Field(default=None, alias="OutputS3Region")
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="OutputS3BucketName"
    )
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")


class S3OutputUrlModel(BaseModel):
    output_url: Optional[str] = Field(default=None, alias="OutputUrl")


class InventoryDeletionSummaryItemModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")
    count: Optional[int] = Field(default=None, alias="Count")
    remaining_count: Optional[int] = Field(default=None, alias="RemainingCount")


class InventoryItemAttributeModel(BaseModel):
    name: str = Field(alias="Name")
    data_type: Literal["number", "string"] = Field(alias="DataType")


class InventoryItemModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    schema_version: str = Field(alias="SchemaVersion")
    capture_time: str = Field(alias="CaptureTime")
    content_hash: Optional[str] = Field(default=None, alias="ContentHash")
    content: Optional[Sequence[Mapping[str, str]]] = Field(
        default=None, alias="Content"
    )
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")


class InventoryResultItemModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    schema_version: str = Field(alias="SchemaVersion")
    content: List[Dict[str, str]] = Field(alias="Content")
    capture_time: Optional[str] = Field(default=None, alias="CaptureTime")
    content_hash: Optional[str] = Field(default=None, alias="ContentHash")


class LabelParameterVersionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    labels: Sequence[str] = Field(alias="Labels")
    parameter_version: Optional[int] = Field(default=None, alias="ParameterVersion")


class ListAssociationVersionsRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDocumentMetadataHistoryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    metadata: Literal["DocumentReviews"] = Field(alias="Metadata")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDocumentVersionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OpsItemEventFilterModel(BaseModel):
    key: Literal["OpsItemId"] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal["Equal"] = Field(alias="Operator")


class OpsItemRelatedItemsFilterModel(BaseModel):
    key: Literal["AssociationId", "ResourceType", "ResourceUri"] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal["Equal"] = Field(alias="Operator")


class OpsMetadataFilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class OpsMetadataModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    ops_metadata_arn: Optional[str] = Field(default=None, alias="OpsMetadataArn")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_user: Optional[str] = Field(default=None, alias="LastModifiedUser")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class ListResourceDataSyncRequestModel(BaseModel):
    sync_type: Optional[str] = Field(default=None, alias="SyncType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_type: Literal[
        "Association",
        "Automation",
        "Document",
        "MaintenanceWindow",
        "ManagedInstance",
        "OpsItem",
        "OpsMetadata",
        "Parameter",
        "PatchBaseline",
    ] = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")


class MaintenanceWindowAutomationParametersModel(BaseModel):
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")


class MaintenanceWindowLambdaParametersModel(BaseModel):
    client_context: Optional[str] = Field(default=None, alias="ClientContext")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    payload: Optional[bytes] = Field(default=None, alias="Payload")


class MaintenanceWindowStepFunctionsParametersModel(BaseModel):
    input: Optional[str] = Field(default=None, alias="Input")
    name: Optional[str] = Field(default=None, alias="Name")


class ModifyDocumentPermissionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    permission_type: Literal["Share"] = Field(alias="PermissionType")
    account_ids_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="AccountIdsToAdd"
    )
    account_ids_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="AccountIdsToRemove"
    )
    shared_document_version: Optional[str] = Field(
        default=None, alias="SharedDocumentVersion"
    )


class OpsEntityItemModel(BaseModel):
    capture_time: Optional[str] = Field(default=None, alias="CaptureTime")
    content: Optional[List[Dict[str, str]]] = Field(default=None, alias="Content")


class OpsItemIdentityModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class ParameterInlinePolicyModel(BaseModel):
    policy_text: Optional[str] = Field(default=None, alias="PolicyText")
    policy_type: Optional[str] = Field(default=None, alias="PolicyType")
    policy_status: Optional[str] = Field(default=None, alias="PolicyStatus")


class PatchFilterModel(BaseModel):
    key: Literal[
        "ADVISORY_ID",
        "ARCH",
        "BUGZILLA_ID",
        "CLASSIFICATION",
        "CVE_ID",
        "EPOCH",
        "MSRC_SEVERITY",
        "NAME",
        "PATCH_ID",
        "PATCH_SET",
        "PRIORITY",
        "PRODUCT",
        "PRODUCT_FAMILY",
        "RELEASE",
        "REPOSITORY",
        "SECTION",
        "SECURITY",
        "SEVERITY",
        "VERSION",
    ] = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class PutResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_hash: Optional[str] = Field(default=None, alias="PolicyHash")


class RegisterDefaultPatchBaselineRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")


class RegisterPatchBaselineForPatchGroupRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    patch_group: str = Field(alias="PatchGroup")


class RemoveTagsFromResourceRequestModel(BaseModel):
    resource_type: Literal[
        "Association",
        "Automation",
        "Document",
        "MaintenanceWindow",
        "ManagedInstance",
        "OpsItem",
        "OpsMetadata",
        "Parameter",
        "PatchBaseline",
    ] = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ResetServiceSettingRequestModel(BaseModel):
    setting_id: str = Field(alias="SettingId")


class ResourceDataSyncOrganizationalUnitModel(BaseModel):
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )


class ResourceDataSyncDestinationDataSharingModel(BaseModel):
    destination_data_sharing_type: Optional[str] = Field(
        default=None, alias="DestinationDataSharingType"
    )


class ResumeSessionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class SendAutomationSignalRequestModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    signal_type: Literal[
        "Approve", "Reject", "Resume", "StartStep", "StopStep"
    ] = Field(alias="SignalType")
    payload: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Payload"
    )


class SessionManagerOutputUrlModel(BaseModel):
    s3_output_url: Optional[str] = Field(default=None, alias="S3OutputUrl")
    cloud_watch_output_url: Optional[str] = Field(
        default=None, alias="CloudWatchOutputUrl"
    )


class StartAssociationsOnceRequestModel(BaseModel):
    association_ids: Sequence[str] = Field(alias="AssociationIds")


class StartSessionRequestModel(BaseModel):
    target: str = Field(alias="Target")
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    reason: Optional[str] = Field(default=None, alias="Reason")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )


class StopAutomationExecutionRequestModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    type: Optional[Literal["Cancel", "Complete"]] = Field(default=None, alias="Type")


class TerminateSessionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class UnlabelParameterVersionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    parameter_version: int = Field(alias="ParameterVersion")
    labels: Sequence[str] = Field(alias="Labels")


class UpdateDocumentDefaultVersionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document_version: str = Field(alias="DocumentVersion")


class UpdateMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    schedule_timezone: Optional[str] = Field(default=None, alias="ScheduleTimezone")
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    duration: Optional[int] = Field(default=None, alias="Duration")
    cutoff: Optional[int] = Field(default=None, alias="Cutoff")
    allow_unassociated_targets: Optional[bool] = Field(
        default=None, alias="AllowUnassociatedTargets"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    replace: Optional[bool] = Field(default=None, alias="Replace")


class UpdateManagedInstanceRoleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    iam_role: str = Field(alias="IamRole")


class UpdateServiceSettingRequestModel(BaseModel):
    setting_id: str = Field(alias="SettingId")
    setting_value: str = Field(alias="SettingValue")


class ActivationModel(BaseModel):
    activation_id: Optional[str] = Field(default=None, alias="ActivationId")
    description: Optional[str] = Field(default=None, alias="Description")
    default_instance_name: Optional[str] = Field(
        default=None, alias="DefaultInstanceName"
    )
    iam_role: Optional[str] = Field(default=None, alias="IamRole")
    registration_limit: Optional[int] = Field(default=None, alias="RegistrationLimit")
    registrations_count: Optional[int] = Field(default=None, alias="RegistrationsCount")
    expiration_date: Optional[datetime] = Field(default=None, alias="ExpirationDate")
    expired: Optional[bool] = Field(default=None, alias="Expired")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class AddTagsToResourceRequestModel(BaseModel):
    resource_type: Literal[
        "Association",
        "Automation",
        "Document",
        "MaintenanceWindow",
        "ManagedInstance",
        "OpsItem",
        "OpsMetadata",
        "Parameter",
        "PatchBaseline",
    ] = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateMaintenanceWindowRequestModel(BaseModel):
    name: str = Field(alias="Name")
    schedule: str = Field(alias="Schedule")
    duration: int = Field(alias="Duration")
    cutoff: int = Field(alias="Cutoff")
    allow_unassociated_targets: bool = Field(alias="AllowUnassociatedTargets")
    description: Optional[str] = Field(default=None, alias="Description")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    schedule_timezone: Optional[str] = Field(default=None, alias="ScheduleTimezone")
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PutParameterRequestModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["SecureString", "String", "StringList"]] = Field(
        default=None, alias="Type"
    )
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    overwrite: Optional[bool] = Field(default=None, alias="Overwrite")
    allowed_pattern: Optional[str] = Field(default=None, alias="AllowedPattern")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    tier: Optional[Literal["Advanced", "Intelligent-Tiering", "Standard"]] = Field(
        default=None, alias="Tier"
    )
    policies: Optional[str] = Field(default=None, alias="Policies")
    data_type: Optional[str] = Field(default=None, alias="DataType")


class AlarmConfigurationModel(BaseModel):
    alarms: Sequence[AlarmModel] = Field(alias="Alarms")
    ignore_poll_alarm_failure: Optional[bool] = Field(
        default=None, alias="IgnorePollAlarmFailure"
    )


class AssociateOpsItemRelatedItemResponseModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelMaintenanceWindowExecutionResultModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateActivationResultModel(BaseModel):
    activation_id: str = Field(alias="ActivationId")
    activation_code: str = Field(alias="ActivationCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOpsItemResponseModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")
    ops_item_arn: str = Field(alias="OpsItemArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOpsMetadataResultModel(BaseModel):
    ops_metadata_arn: str = Field(alias="OpsMetadataArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteParametersResultModel(BaseModel):
    deleted_parameters: List[str] = Field(alias="DeletedParameters")
    invalid_parameters: List[str] = Field(alias="InvalidParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterPatchBaselineForPatchGroupResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    patch_group: str = Field(alias="PatchGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterTargetFromMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_target_id: str = Field(alias="WindowTargetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterTaskFromMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDocumentPermissionResponseModel(BaseModel):
    account_ids: List[str] = Field(alias="AccountIds")
    account_sharing_info_list: List[AccountSharingInfoModel] = Field(
        alias="AccountSharingInfoList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePatchGroupStateResultModel(BaseModel):
    instances: int = Field(alias="Instances")
    instances_with_installed_patches: int = Field(alias="InstancesWithInstalledPatches")
    instances_with_installed_other_patches: int = Field(
        alias="InstancesWithInstalledOtherPatches"
    )
    instances_with_installed_pending_reboot_patches: int = Field(
        alias="InstancesWithInstalledPendingRebootPatches"
    )
    instances_with_installed_rejected_patches: int = Field(
        alias="InstancesWithInstalledRejectedPatches"
    )
    instances_with_missing_patches: int = Field(alias="InstancesWithMissingPatches")
    instances_with_failed_patches: int = Field(alias="InstancesWithFailedPatches")
    instances_with_not_applicable_patches: int = Field(
        alias="InstancesWithNotApplicablePatches"
    )
    instances_with_unreported_not_applicable_patches: int = Field(
        alias="InstancesWithUnreportedNotApplicablePatches"
    )
    instances_with_critical_non_compliant_patches: int = Field(
        alias="InstancesWithCriticalNonCompliantPatches"
    )
    instances_with_security_non_compliant_patches: int = Field(
        alias="InstancesWithSecurityNonCompliantPatches"
    )
    instances_with_other_non_compliant_patches: int = Field(
        alias="InstancesWithOtherNonCompliantPatches"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePatchPropertiesResultModel(BaseModel):
    properties: List[Dict[str, str]] = Field(alias="Properties")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCalendarStateResponseModel(BaseModel):
    state: Literal["CLOSED", "OPEN"] = Field(alias="State")
    at_time: str = Field(alias="AtTime")
    next_transition_time: str = Field(alias="NextTransitionTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectionStatusResponseModel(BaseModel):
    target: str = Field(alias="Target")
    status: Literal["Connected", "NotConnected"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDefaultPatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeployablePatchSnapshotForInstanceResultModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    snapshot_id: str = Field(alias="SnapshotId")
    snapshot_download_url: str = Field(alias="SnapshotDownloadUrl")
    product: str = Field(alias="Product")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMaintenanceWindowExecutionResultModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_ids: List[str] = Field(alias="TaskIds")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "SKIPPED_OVERLAPPING",
        "SUCCESS",
        "TIMED_OUT",
    ] = Field(alias="Status")
    status_details: str = Field(alias="StatusDetails")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMaintenanceWindowExecutionTaskInvocationResultModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_execution_id: str = Field(alias="TaskExecutionId")
    invocation_id: str = Field(alias="InvocationId")
    execution_id: str = Field(alias="ExecutionId")
    task_type: Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"] = Field(
        alias="TaskType"
    )
    parameters: str = Field(alias="Parameters")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "SKIPPED_OVERLAPPING",
        "SUCCESS",
        "TIMED_OUT",
    ] = Field(alias="Status")
    status_details: str = Field(alias="StatusDetails")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    owner_information: str = Field(alias="OwnerInformation")
    window_target_id: str = Field(alias="WindowTargetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    start_date: str = Field(alias="StartDate")
    end_date: str = Field(alias="EndDate")
    schedule: str = Field(alias="Schedule")
    schedule_timezone: str = Field(alias="ScheduleTimezone")
    schedule_offset: int = Field(alias="ScheduleOffset")
    next_execution_time: str = Field(alias="NextExecutionTime")
    duration: int = Field(alias="Duration")
    cutoff: int = Field(alias="Cutoff")
    allow_unassociated_targets: bool = Field(alias="AllowUnassociatedTargets")
    enabled: bool = Field(alias="Enabled")
    created_date: datetime = Field(alias="CreatedDate")
    modified_date: datetime = Field(alias="ModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPatchBaselineForPatchGroupResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    patch_group: str = Field(alias="PatchGroup")
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LabelParameterVersionResultModel(BaseModel):
    invalid_labels: List[str] = Field(alias="InvalidLabels")
    parameter_version: int = Field(alias="ParameterVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInventoryEntriesResultModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    instance_id: str = Field(alias="InstanceId")
    schema_version: str = Field(alias="SchemaVersion")
    capture_time: str = Field(alias="CaptureTime")
    entries: List[Dict[str, str]] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutInventoryResultModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutParameterResultModel(BaseModel):
    version: int = Field(alias="Version")
    tier: Literal["Advanced", "Intelligent-Tiering", "Standard"] = Field(alias="Tier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    policy_hash: str = Field(alias="PolicyHash")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDefaultPatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterPatchBaselineForPatchGroupResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    patch_group: str = Field(alias="PatchGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTargetWithMaintenanceWindowResultModel(BaseModel):
    window_target_id: str = Field(alias="WindowTargetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTaskWithMaintenanceWindowResultModel(BaseModel):
    window_task_id: str = Field(alias="WindowTaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResumeSessionResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    token_value: str = Field(alias="TokenValue")
    stream_url: str = Field(alias="StreamUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAutomationExecutionResultModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartChangeRequestExecutionResultModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSessionResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    token_value: str = Field(alias="TokenValue")
    stream_url: str = Field(alias="StreamUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateSessionResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnlabelParameterVersionResultModel(BaseModel):
    removed_labels: List[str] = Field(alias="RemovedLabels")
    invalid_labels: List[str] = Field(alias="InvalidLabels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMaintenanceWindowResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    start_date: str = Field(alias="StartDate")
    end_date: str = Field(alias="EndDate")
    schedule: str = Field(alias="Schedule")
    schedule_timezone: str = Field(alias="ScheduleTimezone")
    schedule_offset: int = Field(alias="ScheduleOffset")
    duration: int = Field(alias="Duration")
    cutoff: int = Field(alias="Cutoff")
    allow_unassociated_targets: bool = Field(alias="AllowUnassociatedTargets")
    enabled: bool = Field(alias="Enabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOpsMetadataResultModel(BaseModel):
    ops_metadata_arn: str = Field(alias="OpsMetadataArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssociationStatusRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_id: str = Field(alias="InstanceId")
    association_status: AssociationStatusModel = Field(alias="AssociationStatus")


class AssociationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    last_execution_date: Optional[datetime] = Field(
        default=None, alias="LastExecutionDate"
    )
    overview: Optional[AssociationOverviewModel] = Field(default=None, alias="Overview")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )


class DescribeMaintenanceWindowsForTargetRequestModel(BaseModel):
    targets: Sequence[TargetModel] = Field(alias="Targets")
    resource_type: Literal["INSTANCE", "RESOURCE_GROUP"] = Field(alias="ResourceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MaintenanceWindowTargetModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    window_target_id: Optional[str] = Field(default=None, alias="WindowTargetId")
    resource_type: Optional[Literal["INSTANCE", "RESOURCE_GROUP"]] = Field(
        default=None, alias="ResourceType"
    )
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    owner_information: Optional[str] = Field(default=None, alias="OwnerInformation")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class RegisterTargetWithMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    resource_type: Literal["INSTANCE", "RESOURCE_GROUP"] = Field(alias="ResourceType")
    targets: Sequence[TargetModel] = Field(alias="Targets")
    owner_information: Optional[str] = Field(default=None, alias="OwnerInformation")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UpdateMaintenanceWindowTargetRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_target_id: str = Field(alias="WindowTargetId")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    owner_information: Optional[str] = Field(default=None, alias="OwnerInformation")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    replace: Optional[bool] = Field(default=None, alias="Replace")


class UpdateMaintenanceWindowTargetResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_target_id: str = Field(alias="WindowTargetId")
    targets: List[TargetModel] = Field(alias="Targets")
    owner_information: str = Field(alias="OwnerInformation")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssociationExecutionsRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    filters: Optional[Sequence[AssociationExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class AssociationExecutionTargetModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    status: Optional[str] = Field(default=None, alias="Status")
    detailed_status: Optional[str] = Field(default=None, alias="DetailedStatus")
    last_execution_date: Optional[datetime] = Field(
        default=None, alias="LastExecutionDate"
    )
    output_source: Optional[OutputSourceModel] = Field(
        default=None, alias="OutputSource"
    )


class DescribeAssociationExecutionTargetsRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    execution_id: str = Field(alias="ExecutionId")
    filters: Optional[Sequence[AssociationExecutionTargetsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAssociationsRequestModel(BaseModel):
    association_filter_list: Optional[Sequence[AssociationFilterModel]] = Field(
        default=None, alias="AssociationFilterList"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateDocumentRequestModel(BaseModel):
    content: str = Field(alias="Content")
    name: str = Field(alias="Name")
    attachments: Optional[Sequence[AttachmentsSourceModel]] = Field(
        default=None, alias="Attachments"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )
    target_type: Optional[str] = Field(default=None, alias="TargetType")


class DescribeAutomationExecutionsRequestModel(BaseModel):
    filters: Optional[Sequence[AutomationExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCommandInvocationResultModel(BaseModel):
    command_id: str = Field(alias="CommandId")
    instance_id: str = Field(alias="InstanceId")
    comment: str = Field(alias="Comment")
    document_name: str = Field(alias="DocumentName")
    document_version: str = Field(alias="DocumentVersion")
    plugin_name: str = Field(alias="PluginName")
    response_code: int = Field(alias="ResponseCode")
    execution_start_date_time: str = Field(alias="ExecutionStartDateTime")
    execution_elapsed_time: str = Field(alias="ExecutionElapsedTime")
    execution_end_date_time: str = Field(alias="ExecutionEndDateTime")
    status: Literal[
        "Cancelled",
        "Cancelling",
        "Delayed",
        "Failed",
        "InProgress",
        "Pending",
        "Success",
        "TimedOut",
    ] = Field(alias="Status")
    status_details: str = Field(alias="StatusDetails")
    standard_output_content: str = Field(alias="StandardOutputContent")
    standard_output_url: str = Field(alias="StandardOutputUrl")
    standard_error_content: str = Field(alias="StandardErrorContent")
    standard_error_url: str = Field(alias="StandardErrorUrl")
    cloud_watch_output_config: CloudWatchOutputConfigModel = Field(
        alias="CloudWatchOutputConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCommandInvocationsRequestModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[CommandFilterModel]] = Field(
        default=None, alias="Filters"
    )
    details: Optional[bool] = Field(default=None, alias="Details")


class ListCommandsRequestModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[CommandFilterModel]] = Field(
        default=None, alias="Filters"
    )


class CommandInvocationModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_name: Optional[str] = Field(default=None, alias="InstanceName")
    comment: Optional[str] = Field(default=None, alias="Comment")
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    requested_date_time: Optional[datetime] = Field(
        default=None, alias="RequestedDateTime"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Cancelling",
            "Delayed",
            "Failed",
            "InProgress",
            "Pending",
            "Success",
            "TimedOut",
        ]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    trace_output: Optional[str] = Field(default=None, alias="TraceOutput")
    standard_output_url: Optional[str] = Field(default=None, alias="StandardOutputUrl")
    standard_error_url: Optional[str] = Field(default=None, alias="StandardErrorUrl")
    command_plugins: Optional[List[CommandPluginModel]] = Field(
        default=None, alias="CommandPlugins"
    )
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    notification_config: Optional[NotificationConfigModel] = Field(
        default=None, alias="NotificationConfig"
    )
    cloud_watch_output_config: Optional[CloudWatchOutputConfigModel] = Field(
        default=None, alias="CloudWatchOutputConfig"
    )


class MaintenanceWindowRunCommandParametersModel(BaseModel):
    comment: Optional[str] = Field(default=None, alias="Comment")
    cloud_watch_output_config: Optional[CloudWatchOutputConfigModel] = Field(
        default=None, alias="CloudWatchOutputConfig"
    )
    document_hash: Optional[str] = Field(default=None, alias="DocumentHash")
    document_hash_type: Optional[Literal["Sha1", "Sha256"]] = Field(
        default=None, alias="DocumentHashType"
    )
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    notification_config: Optional[NotificationConfigModel] = Field(
        default=None, alias="NotificationConfig"
    )
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="OutputS3BucketName"
    )
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    timeout_seconds: Optional[int] = Field(default=None, alias="TimeoutSeconds")


class ComplianceItemModel(BaseModel):
    compliance_type: Optional[str] = Field(default=None, alias="ComplianceType")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    id: Optional[str] = Field(default=None, alias="Id")
    title: Optional[str] = Field(default=None, alias="Title")
    status: Optional[Literal["COMPLIANT", "NON_COMPLIANT"]] = Field(
        default=None, alias="Status"
    )
    severity: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="Severity")
    execution_summary: Optional[ComplianceExecutionSummaryModel] = Field(
        default=None, alias="ExecutionSummary"
    )
    details: Optional[Dict[str, str]] = Field(default=None, alias="Details")


class PutComplianceItemsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: str = Field(alias="ResourceType")
    compliance_type: str = Field(alias="ComplianceType")
    execution_summary: ComplianceExecutionSummaryModel = Field(alias="ExecutionSummary")
    items: Sequence[ComplianceItemEntryModel] = Field(alias="Items")
    item_content_hash: Optional[str] = Field(default=None, alias="ItemContentHash")
    upload_type: Optional[Literal["COMPLETE", "PARTIAL"]] = Field(
        default=None, alias="UploadType"
    )


class ListComplianceItemsRequestModel(BaseModel):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="ResourceIds")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListComplianceSummariesRequestModel(BaseModel):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListResourceComplianceSummariesRequestModel(BaseModel):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class CompliantSummaryModel(BaseModel):
    compliant_count: Optional[int] = Field(default=None, alias="CompliantCount")
    severity_summary: Optional[SeveritySummaryModel] = Field(
        default=None, alias="SeveritySummary"
    )


class NonCompliantSummaryModel(BaseModel):
    non_compliant_count: Optional[int] = Field(default=None, alias="NonCompliantCount")
    severity_summary: Optional[SeveritySummaryModel] = Field(
        default=None, alias="SeveritySummary"
    )


class CreateActivationRequestModel(BaseModel):
    iam_role: str = Field(alias="IamRole")
    description: Optional[str] = Field(default=None, alias="Description")
    default_instance_name: Optional[str] = Field(
        default=None, alias="DefaultInstanceName"
    )
    registration_limit: Optional[int] = Field(default=None, alias="RegistrationLimit")
    expiration_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExpirationDate"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    registration_metadata: Optional[Sequence[RegistrationMetadataItemModel]] = Field(
        default=None, alias="RegistrationMetadata"
    )


class CreateDocumentRequestModel(BaseModel):
    content: str = Field(alias="Content")
    name: str = Field(alias="Name")
    requires: Optional[Sequence[DocumentRequiresModel]] = Field(
        default=None, alias="Requires"
    )
    attachments: Optional[Sequence[AttachmentsSourceModel]] = Field(
        default=None, alias="Attachments"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    document_type: Optional[
        Literal[
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "Automation",
            "Automation.ChangeTemplate",
            "ChangeCalendar",
            "CloudFormation",
            "Command",
            "ConformancePackTemplate",
            "DeploymentStrategy",
            "Package",
            "Policy",
            "ProblemAnalysis",
            "ProblemAnalysisTemplate",
            "QuickSetup",
            "Session",
        ]
    ] = Field(default=None, alias="DocumentType")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DocumentIdentifierModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    platform_types: Optional[List[Literal["Linux", "MacOS", "Windows"]]] = Field(
        default=None, alias="PlatformTypes"
    )
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    document_type: Optional[
        Literal[
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "Automation",
            "Automation.ChangeTemplate",
            "ChangeCalendar",
            "CloudFormation",
            "Command",
            "ConformancePackTemplate",
            "DeploymentStrategy",
            "Package",
            "Policy",
            "ProblemAnalysis",
            "ProblemAnalysisTemplate",
            "QuickSetup",
            "Session",
        ]
    ] = Field(default=None, alias="DocumentType")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    requires: Optional[List[DocumentRequiresModel]] = Field(
        default=None, alias="Requires"
    )
    review_status: Optional[
        Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="ReviewStatus")
    author: Optional[str] = Field(default=None, alias="Author")


class GetDocumentResultModel(BaseModel):
    name: str = Field(alias="Name")
    created_date: datetime = Field(alias="CreatedDate")
    display_name: str = Field(alias="DisplayName")
    version_name: str = Field(alias="VersionName")
    document_version: str = Field(alias="DocumentVersion")
    status: Literal["Active", "Creating", "Deleting", "Failed", "Updating"] = Field(
        alias="Status"
    )
    status_information: str = Field(alias="StatusInformation")
    content: str = Field(alias="Content")
    document_type: Literal[
        "ApplicationConfiguration",
        "ApplicationConfigurationSchema",
        "Automation",
        "Automation.ChangeTemplate",
        "ChangeCalendar",
        "CloudFormation",
        "Command",
        "ConformancePackTemplate",
        "DeploymentStrategy",
        "Package",
        "Policy",
        "ProblemAnalysis",
        "ProblemAnalysisTemplate",
        "QuickSetup",
        "Session",
    ] = Field(alias="DocumentType")
    document_format: Literal["JSON", "TEXT", "YAML"] = Field(alias="DocumentFormat")
    requires: List[DocumentRequiresModel] = Field(alias="Requires")
    attachments_content: List[AttachmentContentModel] = Field(
        alias="AttachmentsContent"
    )
    review_status: Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"] = Field(
        alias="ReviewStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OpsItemSummaryModel(BaseModel):
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    source: Optional[str] = Field(default=None, alias="Source")
    status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "Closed",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Open",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "Resolved",
            "RunbookInProgress",
            "Scheduled",
            "TimedOut",
        ]
    ] = Field(default=None, alias="Status")
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    title: Optional[str] = Field(default=None, alias="Title")
    operational_data: Optional[Dict[str, OpsItemDataValueModel]] = Field(
        default=None, alias="OperationalData"
    )
    category: Optional[str] = Field(default=None, alias="Category")
    severity: Optional[str] = Field(default=None, alias="Severity")
    ops_item_type: Optional[str] = Field(default=None, alias="OpsItemType")
    actual_start_time: Optional[datetime] = Field(default=None, alias="ActualStartTime")
    actual_end_time: Optional[datetime] = Field(default=None, alias="ActualEndTime")
    planned_start_time: Optional[datetime] = Field(
        default=None, alias="PlannedStartTime"
    )
    planned_end_time: Optional[datetime] = Field(default=None, alias="PlannedEndTime")


class CreateOpsItemRequestModel(BaseModel):
    description: str = Field(alias="Description")
    source: str = Field(alias="Source")
    title: str = Field(alias="Title")
    ops_item_type: Optional[str] = Field(default=None, alias="OpsItemType")
    operational_data: Optional[Mapping[str, OpsItemDataValueModel]] = Field(
        default=None, alias="OperationalData"
    )
    notifications: Optional[Sequence[OpsItemNotificationModel]] = Field(
        default=None, alias="Notifications"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    related_ops_items: Optional[Sequence[RelatedOpsItemModel]] = Field(
        default=None, alias="RelatedOpsItems"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    category: Optional[str] = Field(default=None, alias="Category")
    severity: Optional[str] = Field(default=None, alias="Severity")
    actual_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActualStartTime"
    )
    actual_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActualEndTime"
    )
    planned_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="PlannedStartTime"
    )
    planned_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="PlannedEndTime"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class OpsItemModel(BaseModel):
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    ops_item_type: Optional[str] = Field(default=None, alias="OpsItemType")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    description: Optional[str] = Field(default=None, alias="Description")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    notifications: Optional[List[OpsItemNotificationModel]] = Field(
        default=None, alias="Notifications"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    related_ops_items: Optional[List[RelatedOpsItemModel]] = Field(
        default=None, alias="RelatedOpsItems"
    )
    status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "Closed",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Open",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "Resolved",
            "RunbookInProgress",
            "Scheduled",
            "TimedOut",
        ]
    ] = Field(default=None, alias="Status")
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    version: Optional[str] = Field(default=None, alias="Version")
    title: Optional[str] = Field(default=None, alias="Title")
    source: Optional[str] = Field(default=None, alias="Source")
    operational_data: Optional[Dict[str, OpsItemDataValueModel]] = Field(
        default=None, alias="OperationalData"
    )
    category: Optional[str] = Field(default=None, alias="Category")
    severity: Optional[str] = Field(default=None, alias="Severity")
    actual_start_time: Optional[datetime] = Field(default=None, alias="ActualStartTime")
    actual_end_time: Optional[datetime] = Field(default=None, alias="ActualEndTime")
    planned_start_time: Optional[datetime] = Field(
        default=None, alias="PlannedStartTime"
    )
    planned_end_time: Optional[datetime] = Field(default=None, alias="PlannedEndTime")
    ops_item_arn: Optional[str] = Field(default=None, alias="OpsItemArn")


class UpdateOpsItemRequestModel(BaseModel):
    ops_item_id: str = Field(alias="OpsItemId")
    description: Optional[str] = Field(default=None, alias="Description")
    operational_data: Optional[Mapping[str, OpsItemDataValueModel]] = Field(
        default=None, alias="OperationalData"
    )
    operational_data_to_delete: Optional[Sequence[str]] = Field(
        default=None, alias="OperationalDataToDelete"
    )
    notifications: Optional[Sequence[OpsItemNotificationModel]] = Field(
        default=None, alias="Notifications"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    related_ops_items: Optional[Sequence[RelatedOpsItemModel]] = Field(
        default=None, alias="RelatedOpsItems"
    )
    status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "Closed",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Open",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "Resolved",
            "RunbookInProgress",
            "Scheduled",
            "TimedOut",
        ]
    ] = Field(default=None, alias="Status")
    title: Optional[str] = Field(default=None, alias="Title")
    category: Optional[str] = Field(default=None, alias="Category")
    severity: Optional[str] = Field(default=None, alias="Severity")
    actual_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActualStartTime"
    )
    actual_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActualEndTime"
    )
    planned_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="PlannedStartTime"
    )
    planned_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="PlannedEndTime"
    )
    ops_item_arn: Optional[str] = Field(default=None, alias="OpsItemArn")


class CreateOpsMetadataRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    metadata: Optional[Mapping[str, MetadataValueModel]] = Field(
        default=None, alias="Metadata"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetOpsMetadataResultModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    metadata: Dict[str, MetadataValueModel] = Field(alias="Metadata")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOpsMetadataRequestModel(BaseModel):
    ops_metadata_arn: str = Field(alias="OpsMetadataArn")
    metadata_to_update: Optional[Mapping[str, MetadataValueModel]] = Field(
        default=None, alias="MetadataToUpdate"
    )
    keys_to_delete: Optional[Sequence[str]] = Field(default=None, alias="KeysToDelete")


class DescribeActivationsRequestModel(BaseModel):
    filters: Optional[Sequence[DescribeActivationsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeActivationsRequestDescribeActivationsPaginateModel(BaseModel):
    filters: Optional[Sequence[DescribeActivationsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAssociationExecutionTargetsRequestDescribeAssociationExecutionTargetsPaginateModel(
    BaseModel
):
    association_id: str = Field(alias="AssociationId")
    execution_id: str = Field(alias="ExecutionId")
    filters: Optional[Sequence[AssociationExecutionTargetsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAssociationExecutionsRequestDescribeAssociationExecutionsPaginateModel(
    BaseModel
):
    association_id: str = Field(alias="AssociationId")
    filters: Optional[Sequence[AssociationExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAutomationExecutionsRequestDescribeAutomationExecutionsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[AutomationExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEffectiveInstanceAssociationsRequestDescribeEffectiveInstanceAssociationsPaginateModel(
    BaseModel
):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEffectivePatchesForPatchBaselineRequestDescribeEffectivePatchesForPatchBaselinePaginateModel(
    BaseModel
):
    baseline_id: str = Field(alias="BaselineId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstanceAssociationsStatusRequestDescribeInstanceAssociationsStatusPaginateModel(
    BaseModel
):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstancePatchStatesRequestDescribeInstancePatchStatesPaginateModel(
    BaseModel
):
    instance_ids: Sequence[str] = Field(alias="InstanceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInventoryDeletionsRequestDescribeInventoryDeletionsPaginateModel(
    BaseModel
):
    deletion_id: Optional[str] = Field(default=None, alias="DeletionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowsForTargetRequestDescribeMaintenanceWindowsForTargetPaginateModel(
    BaseModel
):
    targets: Sequence[TargetModel] = Field(alias="Targets")
    resource_type: Literal["INSTANCE", "RESOURCE_GROUP"] = Field(alias="ResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePatchPropertiesRequestDescribePatchPropertiesPaginateModel(BaseModel):
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    property: Literal[
        "CLASSIFICATION",
        "MSRC_SEVERITY",
        "PRIORITY",
        "PRODUCT",
        "PRODUCT_FAMILY",
        "SEVERITY",
    ] = Field(alias="Property")
    patch_set: Optional[Literal["APPLICATION", "OS"]] = Field(
        default=None, alias="PatchSet"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInventorySchemaRequestGetInventorySchemaPaginateModel(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    aggregator: Optional[bool] = Field(default=None, alias="Aggregator")
    sub_type: Optional[bool] = Field(default=None, alias="SubType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetParameterHistoryRequestGetParameterHistoryPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourcePoliciesRequestGetResourcePoliciesPaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociationVersionsRequestListAssociationVersionsPaginateModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociationsRequestListAssociationsPaginateModel(BaseModel):
    association_filter_list: Optional[Sequence[AssociationFilterModel]] = Field(
        default=None, alias="AssociationFilterList"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCommandInvocationsRequestListCommandInvocationsPaginateModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    filters: Optional[Sequence[CommandFilterModel]] = Field(
        default=None, alias="Filters"
    )
    details: Optional[bool] = Field(default=None, alias="Details")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCommandsRequestListCommandsPaginateModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    filters: Optional[Sequence[CommandFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComplianceItemsRequestListComplianceItemsPaginateModel(BaseModel):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="ResourceIds")
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComplianceSummariesRequestListComplianceSummariesPaginateModel(BaseModel):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDocumentVersionsRequestListDocumentVersionsPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceComplianceSummariesRequestListResourceComplianceSummariesPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[ComplianceStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceDataSyncRequestListResourceDataSyncPaginateModel(BaseModel):
    sync_type: Optional[str] = Field(default=None, alias="SyncType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAutomationStepExecutionsRequestDescribeAutomationStepExecutionsPaginateModel(
    BaseModel
):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    filters: Optional[Sequence[StepExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    reverse_order: Optional[bool] = Field(default=None, alias="ReverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAutomationStepExecutionsRequestModel(BaseModel):
    automation_execution_id: str = Field(alias="AutomationExecutionId")
    filters: Optional[Sequence[StepExecutionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    reverse_order: Optional[bool] = Field(default=None, alias="ReverseOrder")


class DescribeAvailablePatchesRequestDescribeAvailablePatchesPaginateModel(BaseModel):
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAvailablePatchesRequestModel(BaseModel):
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstancePatchesRequestDescribeInstancePatchesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstancePatchesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeMaintenanceWindowScheduleRequestDescribeMaintenanceWindowSchedulePaginateModel(
    BaseModel
):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    resource_type: Optional[Literal["INSTANCE", "RESOURCE_GROUP"]] = Field(
        default=None, alias="ResourceType"
    )
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowScheduleRequestModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    resource_type: Optional[Literal["INSTANCE", "RESOURCE_GROUP"]] = Field(
        default=None, alias="ResourceType"
    )
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePatchBaselinesRequestDescribePatchBaselinesPaginateModel(BaseModel):
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePatchBaselinesRequestModel(BaseModel):
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePatchGroupsRequestDescribePatchGroupsPaginateModel(BaseModel):
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePatchGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[PatchOrchestratorFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeAvailablePatchesResultModel(BaseModel):
    patches: List[PatchModel] = Field(alias="Patches")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEffectiveInstanceAssociationsResultModel(BaseModel):
    associations: List[InstanceAssociationModel] = Field(alias="Associations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstanceInformationRequestDescribeInstanceInformationPaginateModel(
    BaseModel
):
    instance_information_filter_list: Optional[
        Sequence[InstanceInformationFilterModel]
    ] = Field(default=None, alias="InstanceInformationFilterList")
    filters: Optional[Sequence[InstanceInformationStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstanceInformationRequestModel(BaseModel):
    instance_information_filter_list: Optional[
        Sequence[InstanceInformationFilterModel]
    ] = Field(default=None, alias="InstanceInformationFilterList")
    filters: Optional[Sequence[InstanceInformationStringFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstancePatchStatesForPatchGroupRequestDescribeInstancePatchStatesForPatchGroupPaginateModel(
    BaseModel
):
    patch_group: str = Field(alias="PatchGroup")
    filters: Optional[Sequence[InstancePatchStateFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstancePatchStatesForPatchGroupRequestModel(BaseModel):
    patch_group: str = Field(alias="PatchGroup")
    filters: Optional[Sequence[InstancePatchStateFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeInstancePatchStatesForPatchGroupResultModel(BaseModel):
    instance_patch_states: List[InstancePatchStateModel] = Field(
        alias="InstancePatchStates"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstancePatchStatesResultModel(BaseModel):
    instance_patch_states: List[InstancePatchStateModel] = Field(
        alias="InstancePatchStates"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstancePatchesResultModel(BaseModel):
    patches: List[PatchComplianceDataModel] = Field(alias="Patches")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestDescribeMaintenanceWindowExecutionTaskInvocationsPaginateModel(
    BaseModel
):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_id: str = Field(alias="TaskId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_id: str = Field(alias="TaskId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowExecutionTasksRequestDescribeMaintenanceWindowExecutionTasksPaginateModel(
    BaseModel
):
    window_execution_id: str = Field(alias="WindowExecutionId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowExecutionTasksRequestModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowExecutionsRequestDescribeMaintenanceWindowExecutionsPaginateModel(
    BaseModel
):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowExecutionsRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowTargetsRequestDescribeMaintenanceWindowTargetsPaginateModel(
    BaseModel
):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowTargetsRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowTasksRequestDescribeMaintenanceWindowTasksPaginateModel(
    BaseModel
):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowTasksRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowsRequestDescribeMaintenanceWindowsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMaintenanceWindowsRequestModel(BaseModel):
    filters: Optional[Sequence[MaintenanceWindowFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMaintenanceWindowExecutionTaskInvocationsResultModel(BaseModel):
    window_execution_task_invocation_identities: List[
        MaintenanceWindowExecutionTaskInvocationIdentityModel
    ] = Field(alias="WindowExecutionTaskInvocationIdentities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowExecutionsResultModel(BaseModel):
    window_executions: List[MaintenanceWindowExecutionModel] = Field(
        alias="WindowExecutions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowScheduleResultModel(BaseModel):
    scheduled_window_executions: List[ScheduledWindowExecutionModel] = Field(
        alias="ScheduledWindowExecutions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowsForTargetResultModel(BaseModel):
    window_identities: List[MaintenanceWindowIdentityForTargetModel] = Field(
        alias="WindowIdentities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowsResultModel(BaseModel):
    window_identities: List[MaintenanceWindowIdentityModel] = Field(
        alias="WindowIdentities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOpsItemsRequestDescribeOpsItemsPaginateModel(BaseModel):
    ops_item_filters: Optional[Sequence[OpsItemFilterModel]] = Field(
        default=None, alias="OpsItemFilters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOpsItemsRequestModel(BaseModel):
    ops_item_filters: Optional[Sequence[OpsItemFilterModel]] = Field(
        default=None, alias="OpsItemFilters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetParametersByPathRequestGetParametersByPathPaginateModel(BaseModel):
    path: str = Field(alias="Path")
    recursive: Optional[bool] = Field(default=None, alias="Recursive")
    parameter_filters: Optional[Sequence[ParameterStringFilterModel]] = Field(
        default=None, alias="ParameterFilters"
    )
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetParametersByPathRequestModel(BaseModel):
    path: str = Field(alias="Path")
    recursive: Optional[bool] = Field(default=None, alias="Recursive")
    parameter_filters: Optional[Sequence[ParameterStringFilterModel]] = Field(
        default=None, alias="ParameterFilters"
    )
    with_decryption: Optional[bool] = Field(default=None, alias="WithDecryption")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeParametersRequestDescribeParametersPaginateModel(BaseModel):
    filters: Optional[Sequence[ParametersFilterModel]] = Field(
        default=None, alias="Filters"
    )
    parameter_filters: Optional[Sequence[ParameterStringFilterModel]] = Field(
        default=None, alias="ParameterFilters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeParametersRequestModel(BaseModel):
    filters: Optional[Sequence[ParametersFilterModel]] = Field(
        default=None, alias="Filters"
    )
    parameter_filters: Optional[Sequence[ParameterStringFilterModel]] = Field(
        default=None, alias="ParameterFilters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePatchBaselinesResultModel(BaseModel):
    baseline_identities: List[PatchBaselineIdentityModel] = Field(
        alias="BaselineIdentities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PatchGroupPatchBaselineMappingModel(BaseModel):
    patch_group: Optional[str] = Field(default=None, alias="PatchGroup")
    baseline_identity: Optional[PatchBaselineIdentityModel] = Field(
        default=None, alias="BaselineIdentity"
    )


class DescribeSessionsRequestDescribeSessionsPaginateModel(BaseModel):
    state: Literal["Active", "History"] = Field(alias="State")
    filters: Optional[Sequence[SessionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSessionsRequestModel(BaseModel):
    state: Literal["Active", "History"] = Field(alias="State")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[SessionFilterModel]] = Field(
        default=None, alias="Filters"
    )


class UpdateDocumentDefaultVersionResultModel(BaseModel):
    description: DocumentDefaultVersionDescriptionModel = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentDescriptionModel(BaseModel):
    sha1: Optional[str] = Field(default=None, alias="Sha1")
    hash: Optional[str] = Field(default=None, alias="Hash")
    hash_type: Optional[Literal["Sha1", "Sha256"]] = Field(
        default=None, alias="HashType"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    status: Optional[
        Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
    ] = Field(default=None, alias="Status")
    status_information: Optional[str] = Field(default=None, alias="StatusInformation")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[List[DocumentParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    platform_types: Optional[List[Literal["Linux", "MacOS", "Windows"]]] = Field(
        default=None, alias="PlatformTypes"
    )
    document_type: Optional[
        Literal[
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "Automation",
            "Automation.ChangeTemplate",
            "ChangeCalendar",
            "CloudFormation",
            "Command",
            "ConformancePackTemplate",
            "DeploymentStrategy",
            "Package",
            "Policy",
            "ProblemAnalysis",
            "ProblemAnalysisTemplate",
            "QuickSetup",
            "Session",
        ]
    ] = Field(default=None, alias="DocumentType")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")
    latest_version: Optional[str] = Field(default=None, alias="LatestVersion")
    default_version: Optional[str] = Field(default=None, alias="DefaultVersion")
    document_format: Optional[Literal["JSON", "TEXT", "YAML"]] = Field(
        default=None, alias="DocumentFormat"
    )
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    attachments_information: Optional[List[AttachmentInformationModel]] = Field(
        default=None, alias="AttachmentsInformation"
    )
    requires: Optional[List[DocumentRequiresModel]] = Field(
        default=None, alias="Requires"
    )
    author: Optional[str] = Field(default=None, alias="Author")
    review_information: Optional[List[ReviewInformationModel]] = Field(
        default=None, alias="ReviewInformation"
    )
    approved_version: Optional[str] = Field(default=None, alias="ApprovedVersion")
    pending_review_version: Optional[str] = Field(
        default=None, alias="PendingReviewVersion"
    )
    review_status: Optional[
        Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="ReviewStatus")
    category: Optional[List[str]] = Field(default=None, alias="Category")
    category_enum: Optional[List[str]] = Field(default=None, alias="CategoryEnum")


class ListDocumentsRequestListDocumentsPaginateModel(BaseModel):
    document_filter_list: Optional[Sequence[DocumentFilterModel]] = Field(
        default=None, alias="DocumentFilterList"
    )
    filters: Optional[Sequence[DocumentKeyValuesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDocumentsRequestModel(BaseModel):
    document_filter_list: Optional[Sequence[DocumentFilterModel]] = Field(
        default=None, alias="DocumentFilterList"
    )
    filters: Optional[Sequence[DocumentKeyValuesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DocumentReviewerResponseSourceModel(BaseModel):
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    updated_time: Optional[datetime] = Field(default=None, alias="UpdatedTime")
    review_status: Optional[
        Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="ReviewStatus")
    comment: Optional[List[DocumentReviewCommentSourceModel]] = Field(
        default=None, alias="Comment"
    )
    reviewer: Optional[str] = Field(default=None, alias="Reviewer")


class DocumentReviewsModel(BaseModel):
    action: Literal["Approve", "Reject", "SendForReview", "UpdateReview"] = Field(
        alias="Action"
    )
    comment: Optional[Sequence[DocumentReviewCommentSourceModel]] = Field(
        default=None, alias="Comment"
    )


class ListDocumentVersionsResultModel(BaseModel):
    document_versions: List[DocumentVersionInfoModel] = Field(alias="DocumentVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EffectivePatchModel(BaseModel):
    patch: Optional[PatchModel] = Field(default=None, alias="Patch")
    patch_status: Optional[PatchStatusModel] = Field(default=None, alias="PatchStatus")


class GetCommandInvocationRequestCommandExecutedWaitModel(BaseModel):
    command_id: str = Field(alias="CommandId")
    instance_id: str = Field(alias="InstanceId")
    plugin_name: Optional[str] = Field(default=None, alias="PluginName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class InventoryGroupModel(BaseModel):
    name: str = Field(alias="Name")
    filters: Sequence[InventoryFilterModel] = Field(alias="Filters")


class ListInventoryEntriesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    type_name: str = Field(alias="TypeName")
    filters: Optional[Sequence[InventoryFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetInventoryRequestGetInventoryPaginateModel(BaseModel):
    filters: Optional[Sequence[InventoryFilterModel]] = Field(
        default=None, alias="Filters"
    )
    aggregators: Optional[Sequence[InventoryAggregatorModel]] = Field(
        default=None, alias="Aggregators"
    )
    result_attributes: Optional[Sequence[ResultAttributeModel]] = Field(
        default=None, alias="ResultAttributes"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInventoryRequestModel(BaseModel):
    filters: Optional[Sequence[InventoryFilterModel]] = Field(
        default=None, alias="Filters"
    )
    aggregators: Optional[Sequence[InventoryAggregatorModel]] = Field(
        default=None, alias="Aggregators"
    )
    result_attributes: Optional[Sequence[ResultAttributeModel]] = Field(
        default=None, alias="ResultAttributes"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OpsAggregatorModel(BaseModel):
    aggregator_type: Optional[str] = Field(default=None, alias="AggregatorType")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    values: Optional[Mapping[str, str]] = Field(default=None, alias="Values")
    filters: Optional[Sequence[OpsFilterModel]] = Field(default=None, alias="Filters")
    aggregators: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="Aggregators"
    )


class GetOpsSummaryRequestGetOpsSummaryPaginateModel(BaseModel):
    sync_name: Optional[str] = Field(default=None, alias="SyncName")
    filters: Optional[Sequence[OpsFilterModel]] = Field(default=None, alias="Filters")
    aggregators: Optional[Sequence[OpsAggregatorModel]] = Field(
        default=None, alias="Aggregators"
    )
    result_attributes: Optional[Sequence[OpsResultAttributeModel]] = Field(
        default=None, alias="ResultAttributes"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetOpsSummaryRequestModel(BaseModel):
    sync_name: Optional[str] = Field(default=None, alias="SyncName")
    filters: Optional[Sequence[OpsFilterModel]] = Field(default=None, alias="Filters")
    aggregators: Optional[Sequence[OpsAggregatorModel]] = Field(
        default=None, alias="Aggregators"
    )
    result_attributes: Optional[Sequence[OpsResultAttributeModel]] = Field(
        default=None, alias="ResultAttributes"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetParameterResultModel(BaseModel):
    parameter: ParameterModel = Field(alias="Parameter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetParametersByPathResultModel(BaseModel):
    parameters: List[ParameterModel] = Field(alias="Parameters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetParametersResultModel(BaseModel):
    parameters: List[ParameterModel] = Field(alias="Parameters")
    invalid_parameters: List[str] = Field(alias="InvalidParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    policies: List[GetResourcePoliciesResponseEntryModel] = Field(alias="Policies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceSettingResultModel(BaseModel):
    service_setting: ServiceSettingModel = Field(alias="ServiceSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetServiceSettingResultModel(BaseModel):
    service_setting: ServiceSettingModel = Field(alias="ServiceSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceInformationModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    ping_status: Optional[Literal["ConnectionLost", "Inactive", "Online"]] = Field(
        default=None, alias="PingStatus"
    )
    last_ping_date_time: Optional[datetime] = Field(
        default=None, alias="LastPingDateTime"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")
    is_latest_version: Optional[bool] = Field(default=None, alias="IsLatestVersion")
    platform_type: Optional[Literal["Linux", "MacOS", "Windows"]] = Field(
        default=None, alias="PlatformType"
    )
    platform_name: Optional[str] = Field(default=None, alias="PlatformName")
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    activation_id: Optional[str] = Field(default=None, alias="ActivationId")
    iam_role: Optional[str] = Field(default=None, alias="IamRole")
    registration_date: Optional[datetime] = Field(
        default=None, alias="RegistrationDate"
    )
    resource_type: Optional[
        Literal["Document", "EC2Instance", "ManagedInstance"]
    ] = Field(default=None, alias="ResourceType")
    name: Optional[str] = Field(default=None, alias="Name")
    ip_address: Optional[str] = Field(default=None, alias="IPAddress")
    computer_name: Optional[str] = Field(default=None, alias="ComputerName")
    association_status: Optional[str] = Field(default=None, alias="AssociationStatus")
    last_association_execution_date: Optional[datetime] = Field(
        default=None, alias="LastAssociationExecutionDate"
    )
    last_successful_association_execution_date: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulAssociationExecutionDate"
    )
    association_overview: Optional[InstanceAggregatedAssociationOverviewModel] = Field(
        default=None, alias="AssociationOverview"
    )
    source_id: Optional[str] = Field(default=None, alias="SourceId")
    source_type: Optional[
        Literal["AWS::EC2::Instance", "AWS::IoT::Thing", "AWS::SSM::ManagedInstance"]
    ] = Field(default=None, alias="SourceType")


class InstanceAssociationOutputLocationModel(BaseModel):
    s3_location: Optional[S3OutputLocationModel] = Field(
        default=None, alias="S3Location"
    )


class InstanceAssociationOutputUrlModel(BaseModel):
    s3_output_url: Optional[S3OutputUrlModel] = Field(default=None, alias="S3OutputUrl")


class InventoryDeletionSummaryModel(BaseModel):
    total_count: Optional[int] = Field(default=None, alias="TotalCount")
    remaining_count: Optional[int] = Field(default=None, alias="RemainingCount")
    summary_items: Optional[List[InventoryDeletionSummaryItemModel]] = Field(
        default=None, alias="SummaryItems"
    )


class InventoryItemSchemaModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    attributes: List[InventoryItemAttributeModel] = Field(alias="Attributes")
    version: Optional[str] = Field(default=None, alias="Version")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class PutInventoryRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    items: Sequence[InventoryItemModel] = Field(alias="Items")


class InventoryResultEntityModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    data: Optional[Dict[str, InventoryResultItemModel]] = Field(
        default=None, alias="Data"
    )


class ListOpsItemEventsRequestListOpsItemEventsPaginateModel(BaseModel):
    filters: Optional[Sequence[OpsItemEventFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOpsItemEventsRequestModel(BaseModel):
    filters: Optional[Sequence[OpsItemEventFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOpsItemRelatedItemsRequestListOpsItemRelatedItemsPaginateModel(BaseModel):
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    filters: Optional[Sequence[OpsItemRelatedItemsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOpsItemRelatedItemsRequestModel(BaseModel):
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    filters: Optional[Sequence[OpsItemRelatedItemsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOpsMetadataRequestListOpsMetadataPaginateModel(BaseModel):
    filters: Optional[Sequence[OpsMetadataFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOpsMetadataRequestModel(BaseModel):
    filters: Optional[Sequence[OpsMetadataFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOpsMetadataResultModel(BaseModel):
    ops_metadata_list: List[OpsMetadataModel] = Field(alias="OpsMetadataList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OpsEntityModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    data: Optional[Dict[str, OpsEntityItemModel]] = Field(default=None, alias="Data")


class OpsItemEventSummaryModel(BaseModel):
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    event_id: Optional[str] = Field(default=None, alias="EventId")
    source: Optional[str] = Field(default=None, alias="Source")
    detail_type: Optional[str] = Field(default=None, alias="DetailType")
    detail: Optional[str] = Field(default=None, alias="Detail")
    created_by: Optional[OpsItemIdentityModel] = Field(default=None, alias="CreatedBy")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class OpsItemRelatedItemSummaryModel(BaseModel):
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    association_type: Optional[str] = Field(default=None, alias="AssociationType")
    resource_uri: Optional[str] = Field(default=None, alias="ResourceUri")
    created_by: Optional[OpsItemIdentityModel] = Field(default=None, alias="CreatedBy")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_by: Optional[OpsItemIdentityModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ParameterHistoryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["SecureString", "String", "StringList"]] = Field(
        default=None, alias="Type"
    )
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_user: Optional[str] = Field(default=None, alias="LastModifiedUser")
    description: Optional[str] = Field(default=None, alias="Description")
    value: Optional[str] = Field(default=None, alias="Value")
    allowed_pattern: Optional[str] = Field(default=None, alias="AllowedPattern")
    version: Optional[int] = Field(default=None, alias="Version")
    labels: Optional[List[str]] = Field(default=None, alias="Labels")
    tier: Optional[Literal["Advanced", "Intelligent-Tiering", "Standard"]] = Field(
        default=None, alias="Tier"
    )
    policies: Optional[List[ParameterInlinePolicyModel]] = Field(
        default=None, alias="Policies"
    )
    data_type: Optional[str] = Field(default=None, alias="DataType")


class ParameterMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["SecureString", "String", "StringList"]] = Field(
        default=None, alias="Type"
    )
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_user: Optional[str] = Field(default=None, alias="LastModifiedUser")
    description: Optional[str] = Field(default=None, alias="Description")
    allowed_pattern: Optional[str] = Field(default=None, alias="AllowedPattern")
    version: Optional[int] = Field(default=None, alias="Version")
    tier: Optional[Literal["Advanced", "Intelligent-Tiering", "Standard"]] = Field(
        default=None, alias="Tier"
    )
    policies: Optional[List[ParameterInlinePolicyModel]] = Field(
        default=None, alias="Policies"
    )
    data_type: Optional[str] = Field(default=None, alias="DataType")


class PatchFilterGroupModel(BaseModel):
    patch_filters: Sequence[PatchFilterModel] = Field(alias="PatchFilters")


class ResourceDataSyncAwsOrganizationsSourceModel(BaseModel):
    organization_source_type: str = Field(alias="OrganizationSourceType")
    organizational_units: Optional[
        Sequence[ResourceDataSyncOrganizationalUnitModel]
    ] = Field(default=None, alias="OrganizationalUnits")


class ResourceDataSyncS3DestinationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    sync_format: Literal["JsonSerDe"] = Field(alias="SyncFormat")
    region: str = Field(alias="Region")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    aws_kms_key_arn: Optional[str] = Field(default=None, alias="AWSKMSKeyARN")
    destination_data_sharing: Optional[
        ResourceDataSyncDestinationDataSharingModel
    ] = Field(default=None, alias="DestinationDataSharing")


class SessionModel(BaseModel):
    session_id: Optional[str] = Field(default=None, alias="SessionId")
    target: Optional[str] = Field(default=None, alias="Target")
    status: Optional[
        Literal[
            "Connected",
            "Connecting",
            "Disconnected",
            "Failed",
            "Terminated",
            "Terminating",
        ]
    ] = Field(default=None, alias="Status")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    reason: Optional[str] = Field(default=None, alias="Reason")
    details: Optional[str] = Field(default=None, alias="Details")
    output_url: Optional[SessionManagerOutputUrlModel] = Field(
        default=None, alias="OutputUrl"
    )
    max_session_duration: Optional[str] = Field(
        default=None, alias="MaxSessionDuration"
    )


class DescribeActivationsResultModel(BaseModel):
    activation_list: List[ActivationModel] = Field(alias="ActivationList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociationExecutionModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    status: Optional[str] = Field(default=None, alias="Status")
    detailed_status: Optional[str] = Field(default=None, alias="DetailedStatus")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_execution_date: Optional[datetime] = Field(
        default=None, alias="LastExecutionDate"
    )
    resource_count_by_status: Optional[str] = Field(
        default=None, alias="ResourceCountByStatus"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )


class CommandModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    comment: Optional[str] = Field(default=None, alias="Comment")
    expires_after: Optional[datetime] = Field(default=None, alias="ExpiresAfter")
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    instance_ids: Optional[List[str]] = Field(default=None, alias="InstanceIds")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    requested_date_time: Optional[datetime] = Field(
        default=None, alias="RequestedDateTime"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Cancelling",
            "Failed",
            "InProgress",
            "Pending",
            "Success",
            "TimedOut",
        ]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    output_s3_region: Optional[str] = Field(default=None, alias="OutputS3Region")
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="OutputS3BucketName"
    )
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    target_count: Optional[int] = Field(default=None, alias="TargetCount")
    completed_count: Optional[int] = Field(default=None, alias="CompletedCount")
    error_count: Optional[int] = Field(default=None, alias="ErrorCount")
    delivery_timed_out_count: Optional[int] = Field(
        default=None, alias="DeliveryTimedOutCount"
    )
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    notification_config: Optional[NotificationConfigModel] = Field(
        default=None, alias="NotificationConfig"
    )
    cloud_watch_output_config: Optional[CloudWatchOutputConfigModel] = Field(
        default=None, alias="CloudWatchOutputConfig"
    )
    timeout_seconds: Optional[int] = Field(default=None, alias="TimeoutSeconds")
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )


class GetMaintenanceWindowExecutionTaskResultModel(BaseModel):
    window_execution_id: str = Field(alias="WindowExecutionId")
    task_execution_id: str = Field(alias="TaskExecutionId")
    task_arn: str = Field(alias="TaskArn")
    service_role: str = Field(alias="ServiceRole")
    type: Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"] = Field(
        alias="Type"
    )
    task_parameters: List[
        Dict[str, MaintenanceWindowTaskParameterValueExpressionModel]
    ] = Field(alias="TaskParameters")
    priority: int = Field(alias="Priority")
    max_concurrency: str = Field(alias="MaxConcurrency")
    max_errors: str = Field(alias="MaxErrors")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "SKIPPED_OVERLAPPING",
        "SUCCESS",
        "TIMED_OUT",
    ] = Field(alias="Status")
    status_details: str = Field(alias="StatusDetails")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    alarm_configuration: AlarmConfigurationModel = Field(alias="AlarmConfiguration")
    triggered_alarms: List[AlarmStateInformationModel] = Field(alias="TriggeredAlarms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MaintenanceWindowExecutionTaskIdentityModel(BaseModel):
    window_execution_id: Optional[str] = Field(default=None, alias="WindowExecutionId")
    task_execution_id: Optional[str] = Field(default=None, alias="TaskExecutionId")
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "SKIPPED_OVERLAPPING",
            "SUCCESS",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    task_type: Optional[
        Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
    ] = Field(default=None, alias="TaskType")
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )


class MaintenanceWindowTaskModel(BaseModel):
    window_id: Optional[str] = Field(default=None, alias="WindowId")
    window_task_id: Optional[str] = Field(default=None, alias="WindowTaskId")
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    type: Optional[
        Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
    ] = Field(default=None, alias="Type")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    task_parameters: Optional[
        Dict[str, MaintenanceWindowTaskParameterValueExpressionModel]
    ] = Field(default=None, alias="TaskParameters")
    priority: Optional[int] = Field(default=None, alias="Priority")
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    cutoff_behavior: Optional[Literal["CANCEL_TASK", "CONTINUE_TASK"]] = Field(
        default=None, alias="CutoffBehavior"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class SendCommandRequestModel(BaseModel):
    document_name: str = Field(alias="DocumentName")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    document_hash: Optional[str] = Field(default=None, alias="DocumentHash")
    document_hash_type: Optional[Literal["Sha1", "Sha256"]] = Field(
        default=None, alias="DocumentHashType"
    )
    timeout_seconds: Optional[int] = Field(default=None, alias="TimeoutSeconds")
    comment: Optional[str] = Field(default=None, alias="Comment")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    output_s3_region: Optional[str] = Field(default=None, alias="OutputS3Region")
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="OutputS3BucketName"
    )
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    notification_config: Optional[NotificationConfigModel] = Field(
        default=None, alias="NotificationConfig"
    )
    cloud_watch_output_config: Optional[CloudWatchOutputConfigModel] = Field(
        default=None, alias="CloudWatchOutputConfig"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class TargetLocationModel(BaseModel):
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")
    target_location_max_concurrency: Optional[str] = Field(
        default=None, alias="TargetLocationMaxConcurrency"
    )
    target_location_max_errors: Optional[str] = Field(
        default=None, alias="TargetLocationMaxErrors"
    )
    execution_role_name: Optional[str] = Field(default=None, alias="ExecutionRoleName")
    target_location_alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="TargetLocationAlarmConfiguration"
    )


class ListAssociationsResultModel(BaseModel):
    associations: List[AssociationModel] = Field(alias="Associations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowTargetsResultModel(BaseModel):
    targets: List[MaintenanceWindowTargetModel] = Field(alias="Targets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssociationExecutionTargetsResultModel(BaseModel):
    association_execution_targets: List[AssociationExecutionTargetModel] = Field(
        alias="AssociationExecutionTargets"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCommandInvocationsResultModel(BaseModel):
    command_invocations: List[CommandInvocationModel] = Field(
        alias="CommandInvocations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MaintenanceWindowTaskInvocationParametersModel(BaseModel):
    run_command: Optional[MaintenanceWindowRunCommandParametersModel] = Field(
        default=None, alias="RunCommand"
    )
    automation: Optional[MaintenanceWindowAutomationParametersModel] = Field(
        default=None, alias="Automation"
    )
    step_functions: Optional[MaintenanceWindowStepFunctionsParametersModel] = Field(
        default=None, alias="StepFunctions"
    )
    lambda_: Optional[MaintenanceWindowLambdaParametersModel] = Field(
        default=None, alias="Lambda"
    )


class ListComplianceItemsResultModel(BaseModel):
    compliance_items: List[ComplianceItemModel] = Field(alias="ComplianceItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComplianceSummaryItemModel(BaseModel):
    compliance_type: Optional[str] = Field(default=None, alias="ComplianceType")
    compliant_summary: Optional[CompliantSummaryModel] = Field(
        default=None, alias="CompliantSummary"
    )
    non_compliant_summary: Optional[NonCompliantSummaryModel] = Field(
        default=None, alias="NonCompliantSummary"
    )


class ResourceComplianceSummaryItemModel(BaseModel):
    compliance_type: Optional[str] = Field(default=None, alias="ComplianceType")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    status: Optional[Literal["COMPLIANT", "NON_COMPLIANT"]] = Field(
        default=None, alias="Status"
    )
    overall_severity: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="OverallSeverity")
    execution_summary: Optional[ComplianceExecutionSummaryModel] = Field(
        default=None, alias="ExecutionSummary"
    )
    compliant_summary: Optional[CompliantSummaryModel] = Field(
        default=None, alias="CompliantSummary"
    )
    non_compliant_summary: Optional[NonCompliantSummaryModel] = Field(
        default=None, alias="NonCompliantSummary"
    )


class ListDocumentsResultModel(BaseModel):
    document_identifiers: List[DocumentIdentifierModel] = Field(
        alias="DocumentIdentifiers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOpsItemsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    ops_item_summaries: List[OpsItemSummaryModel] = Field(alias="OpsItemSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOpsItemResponseModel(BaseModel):
    ops_item: OpsItemModel = Field(alias="OpsItem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePatchGroupsResultModel(BaseModel):
    mappings: List[PatchGroupPatchBaselineMappingModel] = Field(alias="Mappings")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDocumentResultModel(BaseModel):
    document_description: DocumentDescriptionModel = Field(alias="DocumentDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDocumentResultModel(BaseModel):
    document: DocumentDescriptionModel = Field(alias="Document")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDocumentResultModel(BaseModel):
    document_description: DocumentDescriptionModel = Field(alias="DocumentDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentMetadataResponseInfoModel(BaseModel):
    reviewer_response: Optional[List[DocumentReviewerResponseSourceModel]] = Field(
        default=None, alias="ReviewerResponse"
    )


class UpdateDocumentMetadataRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document_reviews: DocumentReviewsModel = Field(alias="DocumentReviews")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")


class DescribeEffectivePatchesForPatchBaselineResultModel(BaseModel):
    effective_patches: List[EffectivePatchModel] = Field(alias="EffectivePatches")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InventoryAggregatorModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="Expression")
    aggregators: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="Aggregators"
    )
    groups: Optional[Sequence[InventoryGroupModel]] = Field(
        default=None, alias="Groups"
    )


class DescribeInstanceInformationResultModel(BaseModel):
    instance_information_list: List[InstanceInformationModel] = Field(
        alias="InstanceInformationList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceAssociationStatusInfoModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    name: Optional[str] = Field(default=None, alias="Name")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    execution_date: Optional[datetime] = Field(default=None, alias="ExecutionDate")
    status: Optional[str] = Field(default=None, alias="Status")
    detailed_status: Optional[str] = Field(default=None, alias="DetailedStatus")
    execution_summary: Optional[str] = Field(default=None, alias="ExecutionSummary")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    output_url: Optional[InstanceAssociationOutputUrlModel] = Field(
        default=None, alias="OutputUrl"
    )
    association_name: Optional[str] = Field(default=None, alias="AssociationName")


class DeleteInventoryResultModel(BaseModel):
    deletion_id: str = Field(alias="DeletionId")
    type_name: str = Field(alias="TypeName")
    deletion_summary: InventoryDeletionSummaryModel = Field(alias="DeletionSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InventoryDeletionStatusItemModel(BaseModel):
    deletion_id: Optional[str] = Field(default=None, alias="DeletionId")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    deletion_start_time: Optional[datetime] = Field(
        default=None, alias="DeletionStartTime"
    )
    last_status: Optional[Literal["Complete", "InProgress"]] = Field(
        default=None, alias="LastStatus"
    )
    last_status_message: Optional[str] = Field(default=None, alias="LastStatusMessage")
    deletion_summary: Optional[InventoryDeletionSummaryModel] = Field(
        default=None, alias="DeletionSummary"
    )
    last_status_update_time: Optional[datetime] = Field(
        default=None, alias="LastStatusUpdateTime"
    )


class GetInventorySchemaResultModel(BaseModel):
    schemas: List[InventoryItemSchemaModel] = Field(alias="Schemas")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInventoryResultModel(BaseModel):
    entities: List[InventoryResultEntityModel] = Field(alias="Entities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOpsSummaryResultModel(BaseModel):
    entities: List[OpsEntityModel] = Field(alias="Entities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOpsItemEventsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    summaries: List[OpsItemEventSummaryModel] = Field(alias="Summaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOpsItemRelatedItemsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    summaries: List[OpsItemRelatedItemSummaryModel] = Field(alias="Summaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetParameterHistoryResultModel(BaseModel):
    parameters: List[ParameterHistoryModel] = Field(alias="Parameters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeParametersResultModel(BaseModel):
    parameters: List[ParameterMetadataModel] = Field(alias="Parameters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PatchRuleModel(BaseModel):
    patch_filter_group: PatchFilterGroupModel = Field(alias="PatchFilterGroup")
    compliance_level: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceLevel")
    approve_after_days: Optional[int] = Field(default=None, alias="ApproveAfterDays")
    approve_until_date: Optional[str] = Field(default=None, alias="ApproveUntilDate")
    enable_non_security: Optional[bool] = Field(default=None, alias="EnableNonSecurity")


class ResourceDataSyncSourceModel(BaseModel):
    source_type: str = Field(alias="SourceType")
    source_regions: Sequence[str] = Field(alias="SourceRegions")
    aws_organizations_source: Optional[
        ResourceDataSyncAwsOrganizationsSourceModel
    ] = Field(default=None, alias="AwsOrganizationsSource")
    include_future_regions: Optional[bool] = Field(
        default=None, alias="IncludeFutureRegions"
    )
    enable_all_ops_data_sources: Optional[bool] = Field(
        default=None, alias="EnableAllOpsDataSources"
    )


class ResourceDataSyncSourceWithStateModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    aws_organizations_source: Optional[
        ResourceDataSyncAwsOrganizationsSourceModel
    ] = Field(default=None, alias="AwsOrganizationsSource")
    source_regions: Optional[List[str]] = Field(default=None, alias="SourceRegions")
    include_future_regions: Optional[bool] = Field(
        default=None, alias="IncludeFutureRegions"
    )
    state: Optional[str] = Field(default=None, alias="State")
    enable_all_ops_data_sources: Optional[bool] = Field(
        default=None, alias="EnableAllOpsDataSources"
    )


class DescribeSessionsResponseModel(BaseModel):
    sessions: List[SessionModel] = Field(alias="Sessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssociationExecutionsResultModel(BaseModel):
    association_executions: List[AssociationExecutionModel] = Field(
        alias="AssociationExecutions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCommandsResultModel(BaseModel):
    commands: List[CommandModel] = Field(alias="Commands")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendCommandResultModel(BaseModel):
    command: CommandModel = Field(alias="Command")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowExecutionTasksResultModel(BaseModel):
    window_execution_task_identities: List[
        MaintenanceWindowExecutionTaskIdentityModel
    ] = Field(alias="WindowExecutionTaskIdentities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceWindowTasksResultModel(BaseModel):
    tasks: List[MaintenanceWindowTaskModel] = Field(alias="Tasks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociationDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    date: Optional[datetime] = Field(default=None, alias="Date")
    last_update_association_date: Optional[datetime] = Field(
        default=None, alias="LastUpdateAssociationDate"
    )
    status: Optional[AssociationStatusModel] = Field(default=None, alias="Status")
    overview: Optional[AssociationOverviewModel] = Field(default=None, alias="Overview")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    automation_target_parameter_name: Optional[str] = Field(
        default=None, alias="AutomationTargetParameterName"
    )
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    output_location: Optional[InstanceAssociationOutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )
    last_execution_date: Optional[datetime] = Field(
        default=None, alias="LastExecutionDate"
    )
    last_successful_execution_date: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulExecutionDate"
    )
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    compliance_severity: Optional[
        Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceSeverity")
    sync_compliance: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="SyncCompliance"
    )
    apply_only_at_cron_interval: Optional[bool] = Field(
        default=None, alias="ApplyOnlyAtCronInterval"
    )
    calendar_names: Optional[List[str]] = Field(default=None, alias="CalendarNames")
    target_locations: Optional[List[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )


class AssociationVersionInfoModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    name: Optional[str] = Field(default=None, alias="Name")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    output_location: Optional[InstanceAssociationOutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    compliance_severity: Optional[
        Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceSeverity")
    sync_compliance: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="SyncCompliance"
    )
    apply_only_at_cron_interval: Optional[bool] = Field(
        default=None, alias="ApplyOnlyAtCronInterval"
    )
    calendar_names: Optional[List[str]] = Field(default=None, alias="CalendarNames")
    target_locations: Optional[List[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )


class CreateAssociationBatchRequestEntryModel(BaseModel):
    name: str = Field(alias="Name")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    automation_target_parameter_name: Optional[str] = Field(
        default=None, alias="AutomationTargetParameterName"
    )
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    output_location: Optional[InstanceAssociationOutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    compliance_severity: Optional[
        Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceSeverity")
    sync_compliance: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="SyncCompliance"
    )
    apply_only_at_cron_interval: Optional[bool] = Field(
        default=None, alias="ApplyOnlyAtCronInterval"
    )
    calendar_names: Optional[Sequence[str]] = Field(default=None, alias="CalendarNames")
    target_locations: Optional[Sequence[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[Sequence[Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class CreateAssociationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    output_location: Optional[InstanceAssociationOutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    automation_target_parameter_name: Optional[str] = Field(
        default=None, alias="AutomationTargetParameterName"
    )
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    compliance_severity: Optional[
        Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceSeverity")
    sync_compliance: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="SyncCompliance"
    )
    apply_only_at_cron_interval: Optional[bool] = Field(
        default=None, alias="ApplyOnlyAtCronInterval"
    )
    calendar_names: Optional[Sequence[str]] = Field(default=None, alias="CalendarNames")
    target_locations: Optional[Sequence[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[Sequence[Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class RunbookModel(BaseModel):
    document_name: str = Field(alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    target_parameter_name: Optional[str] = Field(
        default=None, alias="TargetParameterName"
    )
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    target_locations: Optional[List[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )


class StartAutomationExecutionRequestModel(BaseModel):
    document_name: str = Field(alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    mode: Optional[Literal["Auto", "Interactive"]] = Field(default=None, alias="Mode")
    target_parameter_name: Optional[str] = Field(
        default=None, alias="TargetParameterName"
    )
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    target_maps: Optional[Sequence[Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    target_locations: Optional[Sequence[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class StepExecutionModel(BaseModel):
    step_name: Optional[str] = Field(default=None, alias="StepName")
    action: Optional[str] = Field(default=None, alias="Action")
    timeout_seconds: Optional[int] = Field(default=None, alias="TimeoutSeconds")
    on_failure: Optional[str] = Field(default=None, alias="OnFailure")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")
    execution_start_time: Optional[datetime] = Field(
        default=None, alias="ExecutionStartTime"
    )
    execution_end_time: Optional[datetime] = Field(
        default=None, alias="ExecutionEndTime"
    )
    step_status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "RunbookInProgress",
            "Scheduled",
            "Success",
            "TimedOut",
            "Waiting",
        ]
    ] = Field(default=None, alias="StepStatus")
    response_code: Optional[str] = Field(default=None, alias="ResponseCode")
    inputs: Optional[Dict[str, str]] = Field(default=None, alias="Inputs")
    outputs: Optional[Dict[str, List[str]]] = Field(default=None, alias="Outputs")
    response: Optional[str] = Field(default=None, alias="Response")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    step_execution_id: Optional[str] = Field(default=None, alias="StepExecutionId")
    overridden_parameters: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="OverriddenParameters"
    )
    is_end: Optional[bool] = Field(default=None, alias="IsEnd")
    next_step: Optional[str] = Field(default=None, alias="NextStep")
    is_critical: Optional[bool] = Field(default=None, alias="IsCritical")
    valid_next_steps: Optional[List[str]] = Field(default=None, alias="ValidNextSteps")
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    target_location: Optional[TargetLocationModel] = Field(
        default=None, alias="TargetLocation"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )


class UpdateAssociationRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    output_location: Optional[InstanceAssociationOutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    association_name: Optional[str] = Field(default=None, alias="AssociationName")
    association_version: Optional[str] = Field(default=None, alias="AssociationVersion")
    automation_target_parameter_name: Optional[str] = Field(
        default=None, alias="AutomationTargetParameterName"
    )
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    compliance_severity: Optional[
        Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ComplianceSeverity")
    sync_compliance: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="SyncCompliance"
    )
    apply_only_at_cron_interval: Optional[bool] = Field(
        default=None, alias="ApplyOnlyAtCronInterval"
    )
    calendar_names: Optional[Sequence[str]] = Field(default=None, alias="CalendarNames")
    target_locations: Optional[Sequence[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    target_maps: Optional[Sequence[Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class GetMaintenanceWindowTaskResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")
    targets: List[TargetModel] = Field(alias="Targets")
    task_arn: str = Field(alias="TaskArn")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    task_type: Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"] = Field(
        alias="TaskType"
    )
    task_parameters: Dict[
        str, MaintenanceWindowTaskParameterValueExpressionModel
    ] = Field(alias="TaskParameters")
    task_invocation_parameters: MaintenanceWindowTaskInvocationParametersModel = Field(
        alias="TaskInvocationParameters"
    )
    priority: int = Field(alias="Priority")
    max_concurrency: str = Field(alias="MaxConcurrency")
    max_errors: str = Field(alias="MaxErrors")
    logging_info: LoggingInfoModel = Field(alias="LoggingInfo")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    cutoff_behavior: Literal["CANCEL_TASK", "CONTINUE_TASK"] = Field(
        alias="CutoffBehavior"
    )
    alarm_configuration: AlarmConfigurationModel = Field(alias="AlarmConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTaskWithMaintenanceWindowRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    task_arn: str = Field(alias="TaskArn")
    task_type: Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"] = Field(
        alias="TaskType"
    )
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    task_parameters: Optional[
        Mapping[str, MaintenanceWindowTaskParameterValueExpressionModel]
    ] = Field(default=None, alias="TaskParameters")
    task_invocation_parameters: Optional[
        MaintenanceWindowTaskInvocationParametersModel
    ] = Field(default=None, alias="TaskInvocationParameters")
    priority: Optional[int] = Field(default=None, alias="Priority")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    cutoff_behavior: Optional[Literal["CANCEL_TASK", "CONTINUE_TASK"]] = Field(
        default=None, alias="CutoffBehavior"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class UpdateMaintenanceWindowTaskRequestModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    task_parameters: Optional[
        Mapping[str, MaintenanceWindowTaskParameterValueExpressionModel]
    ] = Field(default=None, alias="TaskParameters")
    task_invocation_parameters: Optional[
        MaintenanceWindowTaskInvocationParametersModel
    ] = Field(default=None, alias="TaskInvocationParameters")
    priority: Optional[int] = Field(default=None, alias="Priority")
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    replace: Optional[bool] = Field(default=None, alias="Replace")
    cutoff_behavior: Optional[Literal["CANCEL_TASK", "CONTINUE_TASK"]] = Field(
        default=None, alias="CutoffBehavior"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )


class UpdateMaintenanceWindowTaskResultModel(BaseModel):
    window_id: str = Field(alias="WindowId")
    window_task_id: str = Field(alias="WindowTaskId")
    targets: List[TargetModel] = Field(alias="Targets")
    task_arn: str = Field(alias="TaskArn")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    task_parameters: Dict[
        str, MaintenanceWindowTaskParameterValueExpressionModel
    ] = Field(alias="TaskParameters")
    task_invocation_parameters: MaintenanceWindowTaskInvocationParametersModel = Field(
        alias="TaskInvocationParameters"
    )
    priority: int = Field(alias="Priority")
    max_concurrency: str = Field(alias="MaxConcurrency")
    max_errors: str = Field(alias="MaxErrors")
    logging_info: LoggingInfoModel = Field(alias="LoggingInfo")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    cutoff_behavior: Literal["CANCEL_TASK", "CONTINUE_TASK"] = Field(
        alias="CutoffBehavior"
    )
    alarm_configuration: AlarmConfigurationModel = Field(alias="AlarmConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComplianceSummariesResultModel(BaseModel):
    compliance_summary_items: List[ComplianceSummaryItemModel] = Field(
        alias="ComplianceSummaryItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceComplianceSummariesResultModel(BaseModel):
    resource_compliance_summary_items: List[ResourceComplianceSummaryItemModel] = Field(
        alias="ResourceComplianceSummaryItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDocumentMetadataHistoryResponseModel(BaseModel):
    name: str = Field(alias="Name")
    document_version: str = Field(alias="DocumentVersion")
    author: str = Field(alias="Author")
    metadata: DocumentMetadataResponseInfoModel = Field(alias="Metadata")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstanceAssociationsStatusResultModel(BaseModel):
    instance_association_status_infos: List[InstanceAssociationStatusInfoModel] = Field(
        alias="InstanceAssociationStatusInfos"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInventoryDeletionsResultModel(BaseModel):
    inventory_deletions: List[InventoryDeletionStatusItemModel] = Field(
        alias="InventoryDeletions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PatchRuleGroupModel(BaseModel):
    patch_rules: Sequence[PatchRuleModel] = Field(alias="PatchRules")


class CreateResourceDataSyncRequestModel(BaseModel):
    sync_name: str = Field(alias="SyncName")
    s3_destination: Optional[ResourceDataSyncS3DestinationModel] = Field(
        default=None, alias="S3Destination"
    )
    sync_type: Optional[str] = Field(default=None, alias="SyncType")
    sync_source: Optional[ResourceDataSyncSourceModel] = Field(
        default=None, alias="SyncSource"
    )


class UpdateResourceDataSyncRequestModel(BaseModel):
    sync_name: str = Field(alias="SyncName")
    sync_type: str = Field(alias="SyncType")
    sync_source: ResourceDataSyncSourceModel = Field(alias="SyncSource")


class ResourceDataSyncItemModel(BaseModel):
    sync_name: Optional[str] = Field(default=None, alias="SyncName")
    sync_type: Optional[str] = Field(default=None, alias="SyncType")
    sync_source: Optional[ResourceDataSyncSourceWithStateModel] = Field(
        default=None, alias="SyncSource"
    )
    s3_destination: Optional[ResourceDataSyncS3DestinationModel] = Field(
        default=None, alias="S3Destination"
    )
    last_sync_time: Optional[datetime] = Field(default=None, alias="LastSyncTime")
    last_successful_sync_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulSyncTime"
    )
    sync_last_modified_time: Optional[datetime] = Field(
        default=None, alias="SyncLastModifiedTime"
    )
    last_status: Optional[Literal["Failed", "InProgress", "Successful"]] = Field(
        default=None, alias="LastStatus"
    )
    sync_created_time: Optional[datetime] = Field(default=None, alias="SyncCreatedTime")
    last_sync_status_message: Optional[str] = Field(
        default=None, alias="LastSyncStatusMessage"
    )


class CreateAssociationResultModel(BaseModel):
    association_description: AssociationDescriptionModel = Field(
        alias="AssociationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssociationResultModel(BaseModel):
    association_description: AssociationDescriptionModel = Field(
        alias="AssociationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssociationResultModel(BaseModel):
    association_description: AssociationDescriptionModel = Field(
        alias="AssociationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssociationStatusResultModel(BaseModel):
    association_description: AssociationDescriptionModel = Field(
        alias="AssociationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociationVersionsResultModel(BaseModel):
    association_versions: List[AssociationVersionInfoModel] = Field(
        alias="AssociationVersions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssociationBatchRequestModel(BaseModel):
    entries: Sequence[CreateAssociationBatchRequestEntryModel] = Field(alias="Entries")


class FailedCreateAssociationModel(BaseModel):
    entry: Optional[CreateAssociationBatchRequestEntryModel] = Field(
        default=None, alias="Entry"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    fault: Optional[Literal["Client", "Server", "Unknown"]] = Field(
        default=None, alias="Fault"
    )


class AutomationExecutionMetadataModel(BaseModel):
    automation_execution_id: Optional[str] = Field(
        default=None, alias="AutomationExecutionId"
    )
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    automation_execution_status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "RunbookInProgress",
            "Scheduled",
            "Success",
            "TimedOut",
            "Waiting",
        ]
    ] = Field(default=None, alias="AutomationExecutionStatus")
    execution_start_time: Optional[datetime] = Field(
        default=None, alias="ExecutionStartTime"
    )
    execution_end_time: Optional[datetime] = Field(
        default=None, alias="ExecutionEndTime"
    )
    executed_by: Optional[str] = Field(default=None, alias="ExecutedBy")
    log_file: Optional[str] = Field(default=None, alias="LogFile")
    outputs: Optional[Dict[str, List[str]]] = Field(default=None, alias="Outputs")
    mode: Optional[Literal["Auto", "Interactive"]] = Field(default=None, alias="Mode")
    parent_automation_execution_id: Optional[str] = Field(
        default=None, alias="ParentAutomationExecutionId"
    )
    current_step_name: Optional[str] = Field(default=None, alias="CurrentStepName")
    current_action: Optional[str] = Field(default=None, alias="CurrentAction")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    target_parameter_name: Optional[str] = Field(
        default=None, alias="TargetParameterName"
    )
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    resolved_targets: Optional[ResolvedTargetsModel] = Field(
        default=None, alias="ResolvedTargets"
    )
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    target: Optional[str] = Field(default=None, alias="Target")
    automation_type: Optional[Literal["CrossAccount", "Local"]] = Field(
        default=None, alias="AutomationType"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )
    automation_subtype: Optional[Literal["ChangeRequest"]] = Field(
        default=None, alias="AutomationSubtype"
    )
    scheduled_time: Optional[datetime] = Field(default=None, alias="ScheduledTime")
    runbooks: Optional[List[RunbookModel]] = Field(default=None, alias="Runbooks")
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    change_request_name: Optional[str] = Field(default=None, alias="ChangeRequestName")


class StartChangeRequestExecutionRequestModel(BaseModel):
    document_name: str = Field(alias="DocumentName")
    runbooks: Sequence[RunbookModel] = Field(alias="Runbooks")
    scheduled_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTime"
    )
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Parameters"
    )
    change_request_name: Optional[str] = Field(default=None, alias="ChangeRequestName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    auto_approve: Optional[bool] = Field(default=None, alias="AutoApprove")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    scheduled_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledEndTime"
    )
    change_details: Optional[str] = Field(default=None, alias="ChangeDetails")


class AutomationExecutionModel(BaseModel):
    automation_execution_id: Optional[str] = Field(
        default=None, alias="AutomationExecutionId"
    )
    document_name: Optional[str] = Field(default=None, alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")
    execution_start_time: Optional[datetime] = Field(
        default=None, alias="ExecutionStartTime"
    )
    execution_end_time: Optional[datetime] = Field(
        default=None, alias="ExecutionEndTime"
    )
    automation_execution_status: Optional[
        Literal[
            "Approved",
            "Cancelled",
            "Cancelling",
            "ChangeCalendarOverrideApproved",
            "ChangeCalendarOverrideRejected",
            "CompletedWithFailure",
            "CompletedWithSuccess",
            "Failed",
            "InProgress",
            "Pending",
            "PendingApproval",
            "PendingChangeCalendarOverride",
            "Rejected",
            "RunbookInProgress",
            "Scheduled",
            "Success",
            "TimedOut",
            "Waiting",
        ]
    ] = Field(default=None, alias="AutomationExecutionStatus")
    step_executions: Optional[List[StepExecutionModel]] = Field(
        default=None, alias="StepExecutions"
    )
    step_executions_truncated: Optional[bool] = Field(
        default=None, alias="StepExecutionsTruncated"
    )
    parameters: Optional[Dict[str, List[str]]] = Field(default=None, alias="Parameters")
    outputs: Optional[Dict[str, List[str]]] = Field(default=None, alias="Outputs")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    mode: Optional[Literal["Auto", "Interactive"]] = Field(default=None, alias="Mode")
    parent_automation_execution_id: Optional[str] = Field(
        default=None, alias="ParentAutomationExecutionId"
    )
    executed_by: Optional[str] = Field(default=None, alias="ExecutedBy")
    current_step_name: Optional[str] = Field(default=None, alias="CurrentStepName")
    current_action: Optional[str] = Field(default=None, alias="CurrentAction")
    target_parameter_name: Optional[str] = Field(
        default=None, alias="TargetParameterName"
    )
    targets: Optional[List[TargetModel]] = Field(default=None, alias="Targets")
    target_maps: Optional[List[Dict[str, List[str]]]] = Field(
        default=None, alias="TargetMaps"
    )
    resolved_targets: Optional[ResolvedTargetsModel] = Field(
        default=None, alias="ResolvedTargets"
    )
    max_concurrency: Optional[str] = Field(default=None, alias="MaxConcurrency")
    max_errors: Optional[str] = Field(default=None, alias="MaxErrors")
    target: Optional[str] = Field(default=None, alias="Target")
    target_locations: Optional[List[TargetLocationModel]] = Field(
        default=None, alias="TargetLocations"
    )
    progress_counters: Optional[ProgressCountersModel] = Field(
        default=None, alias="ProgressCounters"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="AlarmConfiguration"
    )
    triggered_alarms: Optional[List[AlarmStateInformationModel]] = Field(
        default=None, alias="TriggeredAlarms"
    )
    automation_subtype: Optional[Literal["ChangeRequest"]] = Field(
        default=None, alias="AutomationSubtype"
    )
    scheduled_time: Optional[datetime] = Field(default=None, alias="ScheduledTime")
    runbooks: Optional[List[RunbookModel]] = Field(default=None, alias="Runbooks")
    ops_item_id: Optional[str] = Field(default=None, alias="OpsItemId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    change_request_name: Optional[str] = Field(default=None, alias="ChangeRequestName")


class DescribeAutomationStepExecutionsResultModel(BaseModel):
    step_executions: List[StepExecutionModel] = Field(alias="StepExecutions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BaselineOverrideModel(BaseModel):
    operating_system: Optional[
        Literal[
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "AMAZON_LINUX_2022",
            "CENTOS",
            "DEBIAN",
            "MACOS",
            "ORACLE_LINUX",
            "RASPBIAN",
            "REDHAT_ENTERPRISE_LINUX",
            "ROCKY_LINUX",
            "SUSE",
            "UBUNTU",
            "WINDOWS",
        ]
    ] = Field(default=None, alias="OperatingSystem")
    global_filters: Optional[PatchFilterGroupModel] = Field(
        default=None, alias="GlobalFilters"
    )
    approval_rules: Optional[PatchRuleGroupModel] = Field(
        default=None, alias="ApprovalRules"
    )
    approved_patches: Optional[Sequence[str]] = Field(
        default=None, alias="ApprovedPatches"
    )
    approved_patches_compliance_level: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ApprovedPatchesComplianceLevel")
    rejected_patches: Optional[Sequence[str]] = Field(
        default=None, alias="RejectedPatches"
    )
    rejected_patches_action: Optional[Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]] = Field(
        default=None, alias="RejectedPatchesAction"
    )
    approved_patches_enable_non_security: Optional[bool] = Field(
        default=None, alias="ApprovedPatchesEnableNonSecurity"
    )
    sources: Optional[Sequence[PatchSourceModel]] = Field(default=None, alias="Sources")


class CreatePatchBaselineRequestModel(BaseModel):
    name: str = Field(alias="Name")
    operating_system: Optional[
        Literal[
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "AMAZON_LINUX_2022",
            "CENTOS",
            "DEBIAN",
            "MACOS",
            "ORACLE_LINUX",
            "RASPBIAN",
            "REDHAT_ENTERPRISE_LINUX",
            "ROCKY_LINUX",
            "SUSE",
            "UBUNTU",
            "WINDOWS",
        ]
    ] = Field(default=None, alias="OperatingSystem")
    global_filters: Optional[PatchFilterGroupModel] = Field(
        default=None, alias="GlobalFilters"
    )
    approval_rules: Optional[PatchRuleGroupModel] = Field(
        default=None, alias="ApprovalRules"
    )
    approved_patches: Optional[Sequence[str]] = Field(
        default=None, alias="ApprovedPatches"
    )
    approved_patches_compliance_level: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ApprovedPatchesComplianceLevel")
    approved_patches_enable_non_security: Optional[bool] = Field(
        default=None, alias="ApprovedPatchesEnableNonSecurity"
    )
    rejected_patches: Optional[Sequence[str]] = Field(
        default=None, alias="RejectedPatches"
    )
    rejected_patches_action: Optional[Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]] = Field(
        default=None, alias="RejectedPatchesAction"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    sources: Optional[Sequence[PatchSourceModel]] = Field(default=None, alias="Sources")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetPatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    name: str = Field(alias="Name")
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    global_filters: PatchFilterGroupModel = Field(alias="GlobalFilters")
    approval_rules: PatchRuleGroupModel = Field(alias="ApprovalRules")
    approved_patches: List[str] = Field(alias="ApprovedPatches")
    approved_patches_compliance_level: Literal[
        "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
    ] = Field(alias="ApprovedPatchesComplianceLevel")
    approved_patches_enable_non_security: bool = Field(
        alias="ApprovedPatchesEnableNonSecurity"
    )
    rejected_patches: List[str] = Field(alias="RejectedPatches")
    rejected_patches_action: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = Field(
        alias="RejectedPatchesAction"
    )
    patch_groups: List[str] = Field(alias="PatchGroups")
    created_date: datetime = Field(alias="CreatedDate")
    modified_date: datetime = Field(alias="ModifiedDate")
    description: str = Field(alias="Description")
    sources: List[PatchSourceModel] = Field(alias="Sources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePatchBaselineRequestModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    name: Optional[str] = Field(default=None, alias="Name")
    global_filters: Optional[PatchFilterGroupModel] = Field(
        default=None, alias="GlobalFilters"
    )
    approval_rules: Optional[PatchRuleGroupModel] = Field(
        default=None, alias="ApprovalRules"
    )
    approved_patches: Optional[Sequence[str]] = Field(
        default=None, alias="ApprovedPatches"
    )
    approved_patches_compliance_level: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
    ] = Field(default=None, alias="ApprovedPatchesComplianceLevel")
    approved_patches_enable_non_security: Optional[bool] = Field(
        default=None, alias="ApprovedPatchesEnableNonSecurity"
    )
    rejected_patches: Optional[Sequence[str]] = Field(
        default=None, alias="RejectedPatches"
    )
    rejected_patches_action: Optional[Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]] = Field(
        default=None, alias="RejectedPatchesAction"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    sources: Optional[Sequence[PatchSourceModel]] = Field(default=None, alias="Sources")
    replace: Optional[bool] = Field(default=None, alias="Replace")


class UpdatePatchBaselineResultModel(BaseModel):
    baseline_id: str = Field(alias="BaselineId")
    name: str = Field(alias="Name")
    operating_system: Literal[
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ] = Field(alias="OperatingSystem")
    global_filters: PatchFilterGroupModel = Field(alias="GlobalFilters")
    approval_rules: PatchRuleGroupModel = Field(alias="ApprovalRules")
    approved_patches: List[str] = Field(alias="ApprovedPatches")
    approved_patches_compliance_level: Literal[
        "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
    ] = Field(alias="ApprovedPatchesComplianceLevel")
    approved_patches_enable_non_security: bool = Field(
        alias="ApprovedPatchesEnableNonSecurity"
    )
    rejected_patches: List[str] = Field(alias="RejectedPatches")
    rejected_patches_action: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = Field(
        alias="RejectedPatchesAction"
    )
    created_date: datetime = Field(alias="CreatedDate")
    modified_date: datetime = Field(alias="ModifiedDate")
    description: str = Field(alias="Description")
    sources: List[PatchSourceModel] = Field(alias="Sources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceDataSyncResultModel(BaseModel):
    resource_data_sync_items: List[ResourceDataSyncItemModel] = Field(
        alias="ResourceDataSyncItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssociationBatchResultModel(BaseModel):
    successful: List[AssociationDescriptionModel] = Field(alias="Successful")
    failed: List[FailedCreateAssociationModel] = Field(alias="Failed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAutomationExecutionsResultModel(BaseModel):
    automation_execution_metadata_list: List[AutomationExecutionMetadataModel] = Field(
        alias="AutomationExecutionMetadataList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAutomationExecutionResultModel(BaseModel):
    automation_execution: AutomationExecutionModel = Field(alias="AutomationExecution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeployablePatchSnapshotForInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    snapshot_id: str = Field(alias="SnapshotId")
    baseline_override: Optional[BaselineOverrideModel] = Field(
        default=None, alias="BaselineOverride"
    )
