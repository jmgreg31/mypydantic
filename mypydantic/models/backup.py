# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AdvancedBackupSettingModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    backup_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="BackupOptions"
    )


class RecoveryPointCreatorModel(BaseModel):
    backup_plan_id: Optional[str] = Field(default=None, alias="BackupPlanId")
    backup_plan_arn: Optional[str] = Field(default=None, alias="BackupPlanArn")
    backup_plan_version: Optional[str] = Field(default=None, alias="BackupPlanVersion")
    backup_rule_id: Optional[str] = Field(default=None, alias="BackupRuleId")


class BackupPlanTemplatesListMemberModel(BaseModel):
    backup_plan_template_id: Optional[str] = Field(
        default=None, alias="BackupPlanTemplateId"
    )
    backup_plan_template_name: Optional[str] = Field(
        default=None, alias="BackupPlanTemplateName"
    )


class LifecycleModel(BaseModel):
    move_to_cold_storage_after_days: Optional[int] = Field(
        default=None, alias="MoveToColdStorageAfterDays"
    )
    delete_after_days: Optional[int] = Field(default=None, alias="DeleteAfterDays")


class ConditionModel(BaseModel):
    condition_type: Literal["STRINGEQUALS"] = Field(alias="ConditionType")
    condition_key: str = Field(alias="ConditionKey")
    condition_value: str = Field(alias="ConditionValue")


class BackupSelectionsListMemberModel(BaseModel):
    selection_id: Optional[str] = Field(default=None, alias="SelectionId")
    selection_name: Optional[str] = Field(default=None, alias="SelectionName")
    backup_plan_id: Optional[str] = Field(default=None, alias="BackupPlanId")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")


class BackupVaultListMemberModel(BaseModel):
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    backup_vault_arn: Optional[str] = Field(default=None, alias="BackupVaultArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    number_of_recovery_points: Optional[int] = Field(
        default=None, alias="NumberOfRecoveryPoints"
    )
    locked: Optional[bool] = Field(default=None, alias="Locked")
    min_retention_days: Optional[int] = Field(default=None, alias="MinRetentionDays")
    max_retention_days: Optional[int] = Field(default=None, alias="MaxRetentionDays")
    lock_date: Optional[datetime] = Field(default=None, alias="LockDate")


class CalculatedLifecycleModel(BaseModel):
    move_to_cold_storage_at: Optional[datetime] = Field(
        default=None, alias="MoveToColdStorageAt"
    )
    delete_at: Optional[datetime] = Field(default=None, alias="DeleteAt")


class CancelLegalHoldInputRequestModel(BaseModel):
    legal_hold_id: str = Field(alias="LegalHoldId")
    cancel_description: str = Field(alias="CancelDescription")
    retain_record_in_days: Optional[int] = Field(
        default=None, alias="RetainRecordInDays"
    )


class ConditionParameterModel(BaseModel):
    condition_key: Optional[str] = Field(default=None, alias="ConditionKey")
    condition_value: Optional[str] = Field(default=None, alias="ConditionValue")


class ControlInputParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")


class ControlScopeModel(BaseModel):
    compliance_resource_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ComplianceResourceIds"
    )
    compliance_resource_types: Optional[Sequence[str]] = Field(
        default=None, alias="ComplianceResourceTypes"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateBackupVaultInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="BackupVaultTags"
    )
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class ReportDeliveryChannelModel(BaseModel):
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    formats: Optional[Sequence[str]] = Field(default=None, alias="Formats")


class ReportSettingModel(BaseModel):
    report_template: str = Field(alias="ReportTemplate")
    framework_arns: Optional[Sequence[str]] = Field(default=None, alias="FrameworkArns")
    number_of_frameworks: Optional[int] = Field(
        default=None, alias="NumberOfFrameworks"
    )
    accounts: Optional[Sequence[str]] = Field(default=None, alias="Accounts")
    organization_units: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationUnits"
    )
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")


class DateRangeModel(BaseModel):
    from_date: Union[datetime, str] = Field(alias="FromDate")
    to_date: Union[datetime, str] = Field(alias="ToDate")


class DeleteBackupPlanInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")


class DeleteBackupSelectionInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    selection_id: str = Field(alias="SelectionId")


class DeleteBackupVaultAccessPolicyInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class DeleteBackupVaultInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class DeleteBackupVaultLockConfigurationInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class DeleteBackupVaultNotificationsInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class DeleteFrameworkInputRequestModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")


class DeleteRecoveryPointInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")


class DeleteReportPlanInputRequestModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")


class DescribeBackupJobInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")


class DescribeBackupVaultInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class DescribeCopyJobInputRequestModel(BaseModel):
    copy_job_id: str = Field(alias="CopyJobId")


class DescribeFrameworkInputRequestModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")


class DescribeProtectedResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DescribeRecoveryPointInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")


class DescribeReportJobInputRequestModel(BaseModel):
    report_job_id: str = Field(alias="ReportJobId")


class DescribeReportPlanInputRequestModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")


class DescribeRestoreJobInputRequestModel(BaseModel):
    restore_job_id: str = Field(alias="RestoreJobId")


class DisassociateRecoveryPointFromParentInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")


class DisassociateRecoveryPointInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")


class ExportBackupPlanTemplateInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")


class FrameworkModel(BaseModel):
    framework_name: Optional[str] = Field(default=None, alias="FrameworkName")
    framework_arn: Optional[str] = Field(default=None, alias="FrameworkArn")
    framework_description: Optional[str] = Field(
        default=None, alias="FrameworkDescription"
    )
    number_of_controls: Optional[int] = Field(default=None, alias="NumberOfControls")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    deployment_status: Optional[str] = Field(default=None, alias="DeploymentStatus")


class GetBackupPlanFromJSONInputRequestModel(BaseModel):
    backup_plan_template_json: str = Field(alias="BackupPlanTemplateJson")


class GetBackupPlanFromTemplateInputRequestModel(BaseModel):
    backup_plan_template_id: str = Field(alias="BackupPlanTemplateId")


class GetBackupPlanInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class GetBackupSelectionInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    selection_id: str = Field(alias="SelectionId")


class GetBackupVaultAccessPolicyInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class GetBackupVaultNotificationsInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")


class GetLegalHoldInputRequestModel(BaseModel):
    legal_hold_id: str = Field(alias="LegalHoldId")


class GetRecoveryPointRestoreMetadataInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")


class LegalHoldModel(BaseModel):
    title: Optional[str] = Field(default=None, alias="Title")
    status: Optional[Literal["ACTIVE", "CANCELED", "CANCELING", "CREATING"]] = Field(
        default=None, alias="Status"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    legal_hold_id: Optional[str] = Field(default=None, alias="LegalHoldId")
    legal_hold_arn: Optional[str] = Field(default=None, alias="LegalHoldArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    cancellation_date: Optional[datetime] = Field(
        default=None, alias="CancellationDate"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBackupJobsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_state: Optional[
        Literal[
            "ABORTED",
            "ABORTING",
            "COMPLETED",
            "CREATED",
            "EXPIRED",
            "FAILED",
            "PARTIAL",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="ByState")
    by_backup_vault_name: Optional[str] = Field(default=None, alias="ByBackupVaultName")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_parent_job_id: Optional[str] = Field(default=None, alias="ByParentJobId")


class ListBackupPlanTemplatesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListBackupPlanVersionsInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListBackupPlansInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")


class ListBackupSelectionsInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListBackupVaultsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCopyJobsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_state: Optional[
        Literal["COMPLETED", "CREATED", "FAILED", "PARTIAL", "RUNNING"]
    ] = Field(default=None, alias="ByState")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_destination_vault_arn: Optional[str] = Field(
        default=None, alias="ByDestinationVaultArn"
    )
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )
    by_parent_job_id: Optional[str] = Field(default=None, alias="ByParentJobId")


class ListFrameworksInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLegalHoldsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListProtectedResourcesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ProtectedResourceModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    last_backup_time: Optional[datetime] = Field(default=None, alias="LastBackupTime")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class ListRecoveryPointsByBackupVaultInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_backup_plan_id: Optional[str] = Field(default=None, alias="ByBackupPlanId")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_parent_recovery_point_arn: Optional[str] = Field(
        default=None, alias="ByParentRecoveryPointArn"
    )


class ListRecoveryPointsByLegalHoldInputRequestModel(BaseModel):
    legal_hold_id: str = Field(alias="LegalHoldId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RecoveryPointMemberModel(BaseModel):
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")


class ListRecoveryPointsByResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RecoveryPointByResourceModel(BaseModel):
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    status: Optional[Literal["COMPLETED", "DELETING", "EXPIRED", "PARTIAL"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    backup_size_bytes: Optional[int] = Field(default=None, alias="BackupSizeBytes")
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    is_parent: Optional[bool] = Field(default=None, alias="IsParent")
    parent_recovery_point_arn: Optional[str] = Field(
        default=None, alias="ParentRecoveryPointArn"
    )
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class ListReportJobsInputRequestModel(BaseModel):
    by_report_plan_name: Optional[str] = Field(default=None, alias="ByReportPlanName")
    by_creation_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreationBefore"
    )
    by_creation_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreationAfter"
    )
    by_status: Optional[str] = Field(default=None, alias="ByStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListReportPlansInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRestoreJobsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_status: Optional[
        Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    ] = Field(default=None, alias="ByStatus")
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )


class RestoreJobsListMemberModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    restore_job_id: Optional[str] = Field(default=None, alias="RestoreJobId")
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    completion_date: Optional[datetime] = Field(default=None, alias="CompletionDate")
    status: Optional[
        Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    percent_done: Optional[str] = Field(default=None, alias="PercentDone")
    backup_size_in_bytes: Optional[int] = Field(default=None, alias="BackupSizeInBytes")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    expected_completion_time_minutes: Optional[int] = Field(
        default=None, alias="ExpectedCompletionTimeMinutes"
    )
    created_resource_arn: Optional[str] = Field(
        default=None, alias="CreatedResourceArn"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class ListTagsInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PutBackupVaultAccessPolicyInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    policy: Optional[str] = Field(default=None, alias="Policy")


class PutBackupVaultLockConfigurationInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    min_retention_days: Optional[int] = Field(default=None, alias="MinRetentionDays")
    max_retention_days: Optional[int] = Field(default=None, alias="MaxRetentionDays")
    changeable_for_days: Optional[int] = Field(default=None, alias="ChangeableForDays")


class PutBackupVaultNotificationsInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    s_ns_topic_arn: str = Field(alias="SNSTopicArn")
    backup_vault_events: Sequence[
        Literal[
            "BACKUP_JOB_COMPLETED",
            "BACKUP_JOB_EXPIRED",
            "BACKUP_JOB_FAILED",
            "BACKUP_JOB_STARTED",
            "BACKUP_JOB_SUCCESSFUL",
            "BACKUP_PLAN_CREATED",
            "BACKUP_PLAN_MODIFIED",
            "COPY_JOB_FAILED",
            "COPY_JOB_STARTED",
            "COPY_JOB_SUCCESSFUL",
            "RECOVERY_POINT_MODIFIED",
            "RESTORE_JOB_COMPLETED",
            "RESTORE_JOB_FAILED",
            "RESTORE_JOB_STARTED",
            "RESTORE_JOB_SUCCESSFUL",
            "S3_BACKUP_OBJECT_FAILED",
            "S3_RESTORE_OBJECT_FAILED",
        ]
    ] = Field(alias="BackupVaultEvents")


class ReportDestinationModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_keys: Optional[List[str]] = Field(default=None, alias="S3Keys")


class StartReportJobInputRequestModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class StartRestoreJobInputRequestModel(BaseModel):
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    metadata: Mapping[str, str] = Field(alias="Metadata")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class StopBackupJobInputRequestModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_key_list: Sequence[str] = Field(alias="TagKeyList")


class UpdateGlobalSettingsInputRequestModel(BaseModel):
    global_settings: Optional[Mapping[str, str]] = Field(
        default=None, alias="GlobalSettings"
    )


class UpdateRegionSettingsInputRequestModel(BaseModel):
    resource_type_opt_in_preference: Optional[Mapping[str, bool]] = Field(
        default=None, alias="ResourceTypeOptInPreference"
    )
    resource_type_management_preference: Optional[Mapping[str, bool]] = Field(
        default=None, alias="ResourceTypeManagementPreference"
    )


class BackupPlansListMemberModel(BaseModel):
    backup_plan_arn: Optional[str] = Field(default=None, alias="BackupPlanArn")
    backup_plan_id: Optional[str] = Field(default=None, alias="BackupPlanId")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    deletion_date: Optional[datetime] = Field(default=None, alias="DeletionDate")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    backup_plan_name: Optional[str] = Field(default=None, alias="BackupPlanName")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    last_execution_date: Optional[datetime] = Field(
        default=None, alias="LastExecutionDate"
    )
    advanced_backup_settings: Optional[List[AdvancedBackupSettingModel]] = Field(
        default=None, alias="AdvancedBackupSettings"
    )


class BackupJobModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    backup_job_id: Optional[str] = Field(default=None, alias="BackupJobId")
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    backup_vault_arn: Optional[str] = Field(default=None, alias="BackupVaultArn")
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    completion_date: Optional[datetime] = Field(default=None, alias="CompletionDate")
    state: Optional[
        Literal[
            "ABORTED",
            "ABORTING",
            "COMPLETED",
            "CREATED",
            "EXPIRED",
            "FAILED",
            "PARTIAL",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="State")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    percent_done: Optional[str] = Field(default=None, alias="PercentDone")
    backup_size_in_bytes: Optional[int] = Field(default=None, alias="BackupSizeInBytes")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    created_by: Optional[RecoveryPointCreatorModel] = Field(
        default=None, alias="CreatedBy"
    )
    expected_completion_date: Optional[datetime] = Field(
        default=None, alias="ExpectedCompletionDate"
    )
    start_by: Optional[datetime] = Field(default=None, alias="StartBy")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    bytes_transferred: Optional[int] = Field(default=None, alias="BytesTransferred")
    backup_options: Optional[Dict[str, str]] = Field(
        default=None, alias="BackupOptions"
    )
    backup_type: Optional[str] = Field(default=None, alias="BackupType")
    parent_job_id: Optional[str] = Field(default=None, alias="ParentJobId")
    is_parent: Optional[bool] = Field(default=None, alias="IsParent")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class CopyJobModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    copy_job_id: Optional[str] = Field(default=None, alias="CopyJobId")
    source_backup_vault_arn: Optional[str] = Field(
        default=None, alias="SourceBackupVaultArn"
    )
    source_recovery_point_arn: Optional[str] = Field(
        default=None, alias="SourceRecoveryPointArn"
    )
    destination_backup_vault_arn: Optional[str] = Field(
        default=None, alias="DestinationBackupVaultArn"
    )
    destination_recovery_point_arn: Optional[str] = Field(
        default=None, alias="DestinationRecoveryPointArn"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    completion_date: Optional[datetime] = Field(default=None, alias="CompletionDate")
    state: Optional[
        Literal["COMPLETED", "CREATED", "FAILED", "PARTIAL", "RUNNING"]
    ] = Field(default=None, alias="State")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    backup_size_in_bytes: Optional[int] = Field(default=None, alias="BackupSizeInBytes")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    created_by: Optional[RecoveryPointCreatorModel] = Field(
        default=None, alias="CreatedBy"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    parent_job_id: Optional[str] = Field(default=None, alias="ParentJobId")
    is_parent: Optional[bool] = Field(default=None, alias="IsParent")
    composite_member_identifier: Optional[str] = Field(
        default=None, alias="CompositeMemberIdentifier"
    )
    number_of_child_jobs: Optional[int] = Field(default=None, alias="NumberOfChildJobs")
    child_jobs_in_state: Optional[
        Dict[Literal["COMPLETED", "CREATED", "FAILED", "PARTIAL", "RUNNING"], int]
    ] = Field(default=None, alias="ChildJobsInState")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class CopyActionModel(BaseModel):
    destination_backup_vault_arn: str = Field(alias="DestinationBackupVaultArn")
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")


class StartBackupJobInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    resource_arn: str = Field(alias="ResourceArn")
    iam_role_arn: str = Field(alias="IamRoleArn")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    start_window_minutes: Optional[int] = Field(
        default=None, alias="StartWindowMinutes"
    )
    complete_window_minutes: Optional[int] = Field(
        default=None, alias="CompleteWindowMinutes"
    )
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")
    recovery_point_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="RecoveryPointTags"
    )
    backup_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="BackupOptions"
    )


class StartCopyJobInputRequestModel(BaseModel):
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    source_backup_vault_name: str = Field(alias="SourceBackupVaultName")
    destination_backup_vault_arn: str = Field(alias="DestinationBackupVaultArn")
    iam_role_arn: str = Field(alias="IamRoleArn")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")


class UpdateRecoveryPointLifecycleInputRequestModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")


class RecoveryPointByBackupVaultModel(BaseModel):
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    backup_vault_arn: Optional[str] = Field(default=None, alias="BackupVaultArn")
    source_backup_vault_arn: Optional[str] = Field(
        default=None, alias="SourceBackupVaultArn"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    created_by: Optional[RecoveryPointCreatorModel] = Field(
        default=None, alias="CreatedBy"
    )
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    status: Optional[Literal["COMPLETED", "DELETING", "EXPIRED", "PARTIAL"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    completion_date: Optional[datetime] = Field(default=None, alias="CompletionDate")
    backup_size_in_bytes: Optional[int] = Field(default=None, alias="BackupSizeInBytes")
    calculated_lifecycle: Optional[CalculatedLifecycleModel] = Field(
        default=None, alias="CalculatedLifecycle"
    )
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    is_encrypted: Optional[bool] = Field(default=None, alias="IsEncrypted")
    last_restore_time: Optional[datetime] = Field(default=None, alias="LastRestoreTime")
    parent_recovery_point_arn: Optional[str] = Field(
        default=None, alias="ParentRecoveryPointArn"
    )
    composite_member_identifier: Optional[str] = Field(
        default=None, alias="CompositeMemberIdentifier"
    )
    is_parent: Optional[bool] = Field(default=None, alias="IsParent")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class ConditionsModel(BaseModel):
    string_equals: Optional[Sequence[ConditionParameterModel]] = Field(
        default=None, alias="StringEquals"
    )
    string_not_equals: Optional[Sequence[ConditionParameterModel]] = Field(
        default=None, alias="StringNotEquals"
    )
    string_like: Optional[Sequence[ConditionParameterModel]] = Field(
        default=None, alias="StringLike"
    )
    string_not_like: Optional[Sequence[ConditionParameterModel]] = Field(
        default=None, alias="StringNotLike"
    )


class FrameworkControlModel(BaseModel):
    control_name: str = Field(alias="ControlName")
    control_input_parameters: Optional[Sequence[ControlInputParameterModel]] = Field(
        default=None, alias="ControlInputParameters"
    )
    control_scope: Optional[ControlScopeModel] = Field(
        default=None, alias="ControlScope"
    )


class CreateBackupPlanOutputModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_plan_arn: str = Field(alias="BackupPlanArn")
    creation_date: datetime = Field(alias="CreationDate")
    version_id: str = Field(alias="VersionId")
    advanced_backup_settings: List[AdvancedBackupSettingModel] = Field(
        alias="AdvancedBackupSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupSelectionOutputModel(BaseModel):
    selection_id: str = Field(alias="SelectionId")
    backup_plan_id: str = Field(alias="BackupPlanId")
    creation_date: datetime = Field(alias="CreationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupVaultOutputModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    creation_date: datetime = Field(alias="CreationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFrameworkOutputModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")
    framework_arn: str = Field(alias="FrameworkArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReportPlanOutputModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")
    report_plan_arn: str = Field(alias="ReportPlanArn")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackupPlanOutputModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_plan_arn: str = Field(alias="BackupPlanArn")
    deletion_date: datetime = Field(alias="DeletionDate")
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupJobOutputModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    backup_job_id: str = Field(alias="BackupJobId")
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    resource_arn: str = Field(alias="ResourceArn")
    creation_date: datetime = Field(alias="CreationDate")
    completion_date: datetime = Field(alias="CompletionDate")
    state: Literal[
        "ABORTED",
        "ABORTING",
        "COMPLETED",
        "CREATED",
        "EXPIRED",
        "FAILED",
        "PARTIAL",
        "PENDING",
        "RUNNING",
    ] = Field(alias="State")
    status_message: str = Field(alias="StatusMessage")
    percent_done: str = Field(alias="PercentDone")
    backup_size_in_bytes: int = Field(alias="BackupSizeInBytes")
    iam_role_arn: str = Field(alias="IamRoleArn")
    created_by: RecoveryPointCreatorModel = Field(alias="CreatedBy")
    resource_type: str = Field(alias="ResourceType")
    bytes_transferred: int = Field(alias="BytesTransferred")
    expected_completion_date: datetime = Field(alias="ExpectedCompletionDate")
    start_by: datetime = Field(alias="StartBy")
    backup_options: Dict[str, str] = Field(alias="BackupOptions")
    backup_type: str = Field(alias="BackupType")
    parent_job_id: str = Field(alias="ParentJobId")
    is_parent: bool = Field(alias="IsParent")
    number_of_child_jobs: int = Field(alias="NumberOfChildJobs")
    child_jobs_in_state: Dict[
        Literal[
            "ABORTED",
            "ABORTING",
            "COMPLETED",
            "CREATED",
            "EXPIRED",
            "FAILED",
            "PARTIAL",
            "PENDING",
            "RUNNING",
        ],
        int,
    ] = Field(alias="ChildJobsInState")
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupVaultOutputModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    encryption_key_arn: str = Field(alias="EncryptionKeyArn")
    creation_date: datetime = Field(alias="CreationDate")
    creator_request_id: str = Field(alias="CreatorRequestId")
    number_of_recovery_points: int = Field(alias="NumberOfRecoveryPoints")
    locked: bool = Field(alias="Locked")
    min_retention_days: int = Field(alias="MinRetentionDays")
    max_retention_days: int = Field(alias="MaxRetentionDays")
    lock_date: datetime = Field(alias="LockDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGlobalSettingsOutputModel(BaseModel):
    global_settings: Dict[str, str] = Field(alias="GlobalSettings")
    last_update_time: datetime = Field(alias="LastUpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProtectedResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_type: str = Field(alias="ResourceType")
    last_backup_time: datetime = Field(alias="LastBackupTime")
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRecoveryPointOutputModel(BaseModel):
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    source_backup_vault_arn: str = Field(alias="SourceBackupVaultArn")
    resource_arn: str = Field(alias="ResourceArn")
    resource_type: str = Field(alias="ResourceType")
    created_by: RecoveryPointCreatorModel = Field(alias="CreatedBy")
    iam_role_arn: str = Field(alias="IamRoleArn")
    status: Literal["COMPLETED", "DELETING", "EXPIRED", "PARTIAL"] = Field(
        alias="Status"
    )
    status_message: str = Field(alias="StatusMessage")
    creation_date: datetime = Field(alias="CreationDate")
    completion_date: datetime = Field(alias="CompletionDate")
    backup_size_in_bytes: int = Field(alias="BackupSizeInBytes")
    calculated_lifecycle: CalculatedLifecycleModel = Field(alias="CalculatedLifecycle")
    lifecycle: LifecycleModel = Field(alias="Lifecycle")
    encryption_key_arn: str = Field(alias="EncryptionKeyArn")
    is_encrypted: bool = Field(alias="IsEncrypted")
    storage_class: Literal["COLD", "DELETED", "WARM"] = Field(alias="StorageClass")
    last_restore_time: datetime = Field(alias="LastRestoreTime")
    parent_recovery_point_arn: str = Field(alias="ParentRecoveryPointArn")
    composite_member_identifier: str = Field(alias="CompositeMemberIdentifier")
    is_parent: bool = Field(alias="IsParent")
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRegionSettingsOutputModel(BaseModel):
    resource_type_opt_in_preference: Dict[str, bool] = Field(
        alias="ResourceTypeOptInPreference"
    )
    resource_type_management_preference: Dict[str, bool] = Field(
        alias="ResourceTypeManagementPreference"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRestoreJobOutputModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    restore_job_id: str = Field(alias="RestoreJobId")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    creation_date: datetime = Field(alias="CreationDate")
    completion_date: datetime = Field(alias="CompletionDate")
    status: Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"] = Field(
        alias="Status"
    )
    status_message: str = Field(alias="StatusMessage")
    percent_done: str = Field(alias="PercentDone")
    backup_size_in_bytes: int = Field(alias="BackupSizeInBytes")
    iam_role_arn: str = Field(alias="IamRoleArn")
    expected_completion_time_minutes: int = Field(alias="ExpectedCompletionTimeMinutes")
    created_resource_arn: str = Field(alias="CreatedResourceArn")
    resource_type: str = Field(alias="ResourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportBackupPlanTemplateOutputModel(BaseModel):
    backup_plan_template_json: str = Field(alias="BackupPlanTemplateJson")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackupVaultAccessPolicyOutputModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackupVaultNotificationsOutputModel(BaseModel):
    backup_vault_name: str = Field(alias="BackupVaultName")
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    s_ns_topic_arn: str = Field(alias="SNSTopicArn")
    backup_vault_events: List[
        Literal[
            "BACKUP_JOB_COMPLETED",
            "BACKUP_JOB_EXPIRED",
            "BACKUP_JOB_FAILED",
            "BACKUP_JOB_STARTED",
            "BACKUP_JOB_SUCCESSFUL",
            "BACKUP_PLAN_CREATED",
            "BACKUP_PLAN_MODIFIED",
            "COPY_JOB_FAILED",
            "COPY_JOB_STARTED",
            "COPY_JOB_SUCCESSFUL",
            "RECOVERY_POINT_MODIFIED",
            "RESTORE_JOB_COMPLETED",
            "RESTORE_JOB_FAILED",
            "RESTORE_JOB_STARTED",
            "RESTORE_JOB_SUCCESSFUL",
            "S3_BACKUP_OBJECT_FAILED",
            "S3_RESTORE_OBJECT_FAILED",
        ]
    ] = Field(alias="BackupVaultEvents")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecoveryPointRestoreMetadataOutputModel(BaseModel):
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    restore_metadata: Dict[str, str] = Field(alias="RestoreMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSupportedResourceTypesOutputModel(BaseModel):
    resource_types: List[str] = Field(alias="ResourceTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupPlanTemplatesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    backup_plan_templates_list: List[BackupPlanTemplatesListMemberModel] = Field(
        alias="BackupPlanTemplatesList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupSelectionsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    backup_selections_list: List[BackupSelectionsListMemberModel] = Field(
        alias="BackupSelectionsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupVaultsOutputModel(BaseModel):
    backup_vault_list: List[BackupVaultListMemberModel] = Field(alias="BackupVaultList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBackupJobOutputModel(BaseModel):
    backup_job_id: str = Field(alias="BackupJobId")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    creation_date: datetime = Field(alias="CreationDate")
    is_parent: bool = Field(alias="IsParent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCopyJobOutputModel(BaseModel):
    copy_job_id: str = Field(alias="CopyJobId")
    creation_date: datetime = Field(alias="CreationDate")
    is_parent: bool = Field(alias="IsParent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReportJobOutputModel(BaseModel):
    report_job_id: str = Field(alias="ReportJobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRestoreJobOutputModel(BaseModel):
    restore_job_id: str = Field(alias="RestoreJobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackupPlanOutputModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_plan_arn: str = Field(alias="BackupPlanArn")
    creation_date: datetime = Field(alias="CreationDate")
    version_id: str = Field(alias="VersionId")
    advanced_backup_settings: List[AdvancedBackupSettingModel] = Field(
        alias="AdvancedBackupSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFrameworkOutputModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")
    framework_arn: str = Field(alias="FrameworkArn")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecoveryPointLifecycleOutputModel(BaseModel):
    backup_vault_arn: str = Field(alias="BackupVaultArn")
    recovery_point_arn: str = Field(alias="RecoveryPointArn")
    lifecycle: LifecycleModel = Field(alias="Lifecycle")
    calculated_lifecycle: CalculatedLifecycleModel = Field(alias="CalculatedLifecycle")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReportPlanOutputModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")
    report_plan_arn: str = Field(alias="ReportPlanArn")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReportPlanInputRequestModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")
    report_delivery_channel: ReportDeliveryChannelModel = Field(
        alias="ReportDeliveryChannel"
    )
    report_setting: ReportSettingModel = Field(alias="ReportSetting")
    report_plan_description: Optional[str] = Field(
        default=None, alias="ReportPlanDescription"
    )
    report_plan_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="ReportPlanTags"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class ReportPlanModel(BaseModel):
    report_plan_arn: Optional[str] = Field(default=None, alias="ReportPlanArn")
    report_plan_name: Optional[str] = Field(default=None, alias="ReportPlanName")
    report_plan_description: Optional[str] = Field(
        default=None, alias="ReportPlanDescription"
    )
    report_setting: Optional[ReportSettingModel] = Field(
        default=None, alias="ReportSetting"
    )
    report_delivery_channel: Optional[ReportDeliveryChannelModel] = Field(
        default=None, alias="ReportDeliveryChannel"
    )
    deployment_status: Optional[str] = Field(default=None, alias="DeploymentStatus")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_attempted_execution_time: Optional[datetime] = Field(
        default=None, alias="LastAttemptedExecutionTime"
    )
    last_successful_execution_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulExecutionTime"
    )


class UpdateReportPlanInputRequestModel(BaseModel):
    report_plan_name: str = Field(alias="ReportPlanName")
    report_plan_description: Optional[str] = Field(
        default=None, alias="ReportPlanDescription"
    )
    report_delivery_channel: Optional[ReportDeliveryChannelModel] = Field(
        default=None, alias="ReportDeliveryChannel"
    )
    report_setting: Optional[ReportSettingModel] = Field(
        default=None, alias="ReportSetting"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class RecoveryPointSelectionModel(BaseModel):
    vault_names: Optional[Sequence[str]] = Field(default=None, alias="VaultNames")
    resource_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceIdentifiers"
    )
    date_range: Optional[DateRangeModel] = Field(default=None, alias="DateRange")


class ListFrameworksOutputModel(BaseModel):
    frameworks: List[FrameworkModel] = Field(alias="Frameworks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLegalHoldsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    legal_holds: List[LegalHoldModel] = Field(alias="LegalHolds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupJobsInputListBackupJobsPaginateModel(BaseModel):
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_state: Optional[
        Literal[
            "ABORTED",
            "ABORTING",
            "COMPLETED",
            "CREATED",
            "EXPIRED",
            "FAILED",
            "PARTIAL",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="ByState")
    by_backup_vault_name: Optional[str] = Field(default=None, alias="ByBackupVaultName")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_parent_job_id: Optional[str] = Field(default=None, alias="ByParentJobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBackupPlanVersionsInputListBackupPlanVersionsPaginateModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBackupPlansInputListBackupPlansPaginateModel(BaseModel):
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBackupSelectionsInputListBackupSelectionsPaginateModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBackupVaultsInputListBackupVaultsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCopyJobsInputListCopyJobsPaginateModel(BaseModel):
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_state: Optional[
        Literal["COMPLETED", "CREATED", "FAILED", "PARTIAL", "RUNNING"]
    ] = Field(default=None, alias="ByState")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_destination_vault_arn: Optional[str] = Field(
        default=None, alias="ByDestinationVaultArn"
    )
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )
    by_parent_job_id: Optional[str] = Field(default=None, alias="ByParentJobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLegalHoldsInputListLegalHoldsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProtectedResourcesInputListProtectedResourcesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateModel(
    BaseModel
):
    backup_vault_name: str = Field(alias="BackupVaultName")
    by_resource_arn: Optional[str] = Field(default=None, alias="ByResourceArn")
    by_resource_type: Optional[str] = Field(default=None, alias="ByResourceType")
    by_backup_plan_id: Optional[str] = Field(default=None, alias="ByBackupPlanId")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_parent_recovery_point_arn: Optional[str] = Field(
        default=None, alias="ByParentRecoveryPointArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateModel(
    BaseModel
):
    legal_hold_id: str = Field(alias="LegalHoldId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateModel(
    BaseModel
):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRestoreJobsInputListRestoreJobsPaginateModel(BaseModel):
    by_account_id: Optional[str] = Field(default=None, alias="ByAccountId")
    by_created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedBefore"
    )
    by_created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCreatedAfter"
    )
    by_status: Optional[
        Literal["ABORTED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    ] = Field(default=None, alias="ByStatus")
    by_complete_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteBefore"
    )
    by_complete_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ByCompleteAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProtectedResourcesOutputModel(BaseModel):
    results: List[ProtectedResourceModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecoveryPointsByLegalHoldOutputModel(BaseModel):
    recovery_points: List[RecoveryPointMemberModel] = Field(alias="RecoveryPoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecoveryPointsByResourceOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    recovery_points: List[RecoveryPointByResourceModel] = Field(alias="RecoveryPoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRestoreJobsOutputModel(BaseModel):
    restore_jobs: List[RestoreJobsListMemberModel] = Field(alias="RestoreJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReportJobModel(BaseModel):
    report_job_id: Optional[str] = Field(default=None, alias="ReportJobId")
    report_plan_arn: Optional[str] = Field(default=None, alias="ReportPlanArn")
    report_template: Optional[str] = Field(default=None, alias="ReportTemplate")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    status: Optional[str] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    report_destination: Optional[ReportDestinationModel] = Field(
        default=None, alias="ReportDestination"
    )


class ListBackupPlanVersionsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    backup_plan_versions_list: List[BackupPlansListMemberModel] = Field(
        alias="BackupPlanVersionsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupPlansOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    backup_plans_list: List[BackupPlansListMemberModel] = Field(alias="BackupPlansList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupJobsOutputModel(BaseModel):
    backup_jobs: List[BackupJobModel] = Field(alias="BackupJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCopyJobOutputModel(BaseModel):
    copy_job: CopyJobModel = Field(alias="CopyJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCopyJobsOutputModel(BaseModel):
    copy_jobs: List[CopyJobModel] = Field(alias="CopyJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BackupRuleInputModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    target_backup_vault_name: str = Field(alias="TargetBackupVaultName")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    start_window_minutes: Optional[int] = Field(
        default=None, alias="StartWindowMinutes"
    )
    completion_window_minutes: Optional[int] = Field(
        default=None, alias="CompletionWindowMinutes"
    )
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")
    recovery_point_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="RecoveryPointTags"
    )
    copy_actions: Optional[Sequence[CopyActionModel]] = Field(
        default=None, alias="CopyActions"
    )
    enable_continuous_backup: Optional[bool] = Field(
        default=None, alias="EnableContinuousBackup"
    )


class BackupRuleModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    target_backup_vault_name: str = Field(alias="TargetBackupVaultName")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    start_window_minutes: Optional[int] = Field(
        default=None, alias="StartWindowMinutes"
    )
    completion_window_minutes: Optional[int] = Field(
        default=None, alias="CompletionWindowMinutes"
    )
    lifecycle: Optional[LifecycleModel] = Field(default=None, alias="Lifecycle")
    recovery_point_tags: Optional[Dict[str, str]] = Field(
        default=None, alias="RecoveryPointTags"
    )
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    copy_actions: Optional[List[CopyActionModel]] = Field(
        default=None, alias="CopyActions"
    )
    enable_continuous_backup: Optional[bool] = Field(
        default=None, alias="EnableContinuousBackup"
    )


class ListRecoveryPointsByBackupVaultOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    recovery_points: List[RecoveryPointByBackupVaultModel] = Field(
        alias="RecoveryPoints"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BackupSelectionModel(BaseModel):
    selection_name: str = Field(alias="SelectionName")
    iam_role_arn: str = Field(alias="IamRoleArn")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")
    list_of_tags: Optional[Sequence[ConditionModel]] = Field(
        default=None, alias="ListOfTags"
    )
    not_resources: Optional[Sequence[str]] = Field(default=None, alias="NotResources")
    conditions: Optional[ConditionsModel] = Field(default=None, alias="Conditions")


class CreateFrameworkInputRequestModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")
    framework_controls: Sequence[FrameworkControlModel] = Field(
        alias="FrameworkControls"
    )
    framework_description: Optional[str] = Field(
        default=None, alias="FrameworkDescription"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    framework_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="FrameworkTags"
    )


class DescribeFrameworkOutputModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")
    framework_arn: str = Field(alias="FrameworkArn")
    framework_description: str = Field(alias="FrameworkDescription")
    framework_controls: List[FrameworkControlModel] = Field(alias="FrameworkControls")
    creation_time: datetime = Field(alias="CreationTime")
    deployment_status: str = Field(alias="DeploymentStatus")
    framework_status: str = Field(alias="FrameworkStatus")
    idempotency_token: str = Field(alias="IdempotencyToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFrameworkInputRequestModel(BaseModel):
    framework_name: str = Field(alias="FrameworkName")
    framework_description: Optional[str] = Field(
        default=None, alias="FrameworkDescription"
    )
    framework_controls: Optional[Sequence[FrameworkControlModel]] = Field(
        default=None, alias="FrameworkControls"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class DescribeReportPlanOutputModel(BaseModel):
    report_plan: ReportPlanModel = Field(alias="ReportPlan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportPlansOutputModel(BaseModel):
    report_plans: List[ReportPlanModel] = Field(alias="ReportPlans")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLegalHoldInputRequestModel(BaseModel):
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    recovery_point_selection: Optional[RecoveryPointSelectionModel] = Field(
        default=None, alias="RecoveryPointSelection"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateLegalHoldOutputModel(BaseModel):
    title: str = Field(alias="Title")
    status: Literal["ACTIVE", "CANCELED", "CANCELING", "CREATING"] = Field(
        alias="Status"
    )
    description: str = Field(alias="Description")
    legal_hold_id: str = Field(alias="LegalHoldId")
    legal_hold_arn: str = Field(alias="LegalHoldArn")
    creation_date: datetime = Field(alias="CreationDate")
    recovery_point_selection: RecoveryPointSelectionModel = Field(
        alias="RecoveryPointSelection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLegalHoldOutputModel(BaseModel):
    title: str = Field(alias="Title")
    status: Literal["ACTIVE", "CANCELED", "CANCELING", "CREATING"] = Field(
        alias="Status"
    )
    description: str = Field(alias="Description")
    cancel_description: str = Field(alias="CancelDescription")
    legal_hold_id: str = Field(alias="LegalHoldId")
    legal_hold_arn: str = Field(alias="LegalHoldArn")
    creation_date: datetime = Field(alias="CreationDate")
    cancellation_date: datetime = Field(alias="CancellationDate")
    retain_record_until: datetime = Field(alias="RetainRecordUntil")
    recovery_point_selection: RecoveryPointSelectionModel = Field(
        alias="RecoveryPointSelection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReportJobOutputModel(BaseModel):
    report_job: ReportJobModel = Field(alias="ReportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportJobsOutputModel(BaseModel):
    report_jobs: List[ReportJobModel] = Field(alias="ReportJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BackupPlanInputModel(BaseModel):
    backup_plan_name: str = Field(alias="BackupPlanName")
    rules: Sequence[BackupRuleInputModel] = Field(alias="Rules")
    advanced_backup_settings: Optional[Sequence[AdvancedBackupSettingModel]] = Field(
        default=None, alias="AdvancedBackupSettings"
    )


class BackupPlanModel(BaseModel):
    backup_plan_name: str = Field(alias="BackupPlanName")
    rules: List[BackupRuleModel] = Field(alias="Rules")
    advanced_backup_settings: Optional[List[AdvancedBackupSettingModel]] = Field(
        default=None, alias="AdvancedBackupSettings"
    )


class CreateBackupSelectionInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_selection: BackupSelectionModel = Field(alias="BackupSelection")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class GetBackupSelectionOutputModel(BaseModel):
    backup_selection: BackupSelectionModel = Field(alias="BackupSelection")
    selection_id: str = Field(alias="SelectionId")
    backup_plan_id: str = Field(alias="BackupPlanId")
    creation_date: datetime = Field(alias="CreationDate")
    creator_request_id: str = Field(alias="CreatorRequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupPlanInputRequestModel(BaseModel):
    backup_plan: BackupPlanInputModel = Field(alias="BackupPlan")
    backup_plan_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="BackupPlanTags"
    )
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class UpdateBackupPlanInputRequestModel(BaseModel):
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_plan: BackupPlanInputModel = Field(alias="BackupPlan")


class GetBackupPlanFromJSONOutputModel(BaseModel):
    backup_plan: BackupPlanModel = Field(alias="BackupPlan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackupPlanFromTemplateOutputModel(BaseModel):
    backup_plan_document: BackupPlanModel = Field(alias="BackupPlanDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackupPlanOutputModel(BaseModel):
    backup_plan: BackupPlanModel = Field(alias="BackupPlan")
    backup_plan_id: str = Field(alias="BackupPlanId")
    backup_plan_arn: str = Field(alias="BackupPlanArn")
    version_id: str = Field(alias="VersionId")
    creator_request_id: str = Field(alias="CreatorRequestId")
    creation_date: datetime = Field(alias="CreationDate")
    deletion_date: datetime = Field(alias="DeletionDate")
    last_execution_date: datetime = Field(alias="LastExecutionDate")
    advanced_backup_settings: List[AdvancedBackupSettingModel] = Field(
        alias="AdvancedBackupSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
