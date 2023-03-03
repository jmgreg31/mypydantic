# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ConfigParameterModel(BaseModel):
    parameter_key: Optional[str] = Field(default=None, alias="parameterKey")
    parameter_value: Optional[str] = Field(default=None, alias="parameterValue")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SnapshotModel(BaseModel):
    accounts_with_provisioned_restore_access: Optional[List[str]] = Field(
        default=None, alias="accountsWithProvisionedRestoreAccess"
    )
    accounts_with_restore_access: Optional[List[str]] = Field(
        default=None, alias="accountsWithRestoreAccess"
    )
    actual_incremental_backup_size_in_mega_bytes: Optional[float] = Field(
        default=None, alias="actualIncrementalBackupSizeInMegaBytes"
    )
    admin_username: Optional[str] = Field(default=None, alias="adminUsername")
    backup_progress_in_mega_bytes: Optional[float] = Field(
        default=None, alias="backupProgressInMegaBytes"
    )
    current_backup_rate_in_mega_bytes_per_second: Optional[float] = Field(
        default=None, alias="currentBackupRateInMegaBytesPerSecond"
    )
    elapsed_time_in_seconds: Optional[int] = Field(
        default=None, alias="elapsedTimeInSeconds"
    )
    estimated_seconds_to_completion: Optional[int] = Field(
        default=None, alias="estimatedSecondsToCompletion"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    snapshot_arn: Optional[str] = Field(default=None, alias="snapshotArn")
    snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="snapshotCreateTime"
    )
    snapshot_name: Optional[str] = Field(default=None, alias="snapshotName")
    snapshot_remaining_days: Optional[int] = Field(
        default=None, alias="snapshotRemainingDays"
    )
    snapshot_retention_period: Optional[int] = Field(
        default=None, alias="snapshotRetentionPeriod"
    )
    snapshot_retention_start_time: Optional[datetime] = Field(
        default=None, alias="snapshotRetentionStartTime"
    )
    status: Optional[
        Literal["AVAILABLE", "CANCELLED", "COPYING", "CREATING", "DELETED", "FAILED"]
    ] = Field(default=None, alias="status")
    total_backup_size_in_mega_bytes: Optional[float] = Field(
        default=None, alias="totalBackupSizeInMegaBytes"
    )


class CreateEndpointAccessRequestModel(BaseModel):
    endpoint_name: str = Field(alias="endpointName")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    workgroup_name: str = Field(alias="workgroupName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcSecurityGroupIds"
    )


class NamespaceModel(BaseModel):
    admin_username: Optional[str] = Field(default=None, alias="adminUsername")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    db_name: Optional[str] = Field(default=None, alias="dbName")
    default_iam_role_arn: Optional[str] = Field(default=None, alias="defaultIamRoleArn")
    iam_roles: Optional[List[str]] = Field(default=None, alias="iamRoles")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    log_exports: Optional[
        List[Literal["connectionlog", "useractivitylog", "userlog"]]
    ] = Field(default=None, alias="logExports")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    status: Optional[Literal["AVAILABLE", "DELETING", "MODIFYING"]] = Field(
        default=None, alias="status"
    )


class CreateUsageLimitRequestModel(BaseModel):
    amount: int = Field(alias="amount")
    resource_arn: str = Field(alias="resourceArn")
    usage_type: Literal["cross-region-datasharing", "serverless-compute"] = Field(
        alias="usageType"
    )
    breach_action: Optional[Literal["deactivate", "emit-metric", "log"]] = Field(
        default=None, alias="breachAction"
    )
    period: Optional[Literal["daily", "monthly", "weekly"]] = Field(
        default=None, alias="period"
    )


class UsageLimitModel(BaseModel):
    amount: Optional[int] = Field(default=None, alias="amount")
    breach_action: Optional[Literal["deactivate", "emit-metric", "log"]] = Field(
        default=None, alias="breachAction"
    )
    period: Optional[Literal["daily", "monthly", "weekly"]] = Field(
        default=None, alias="period"
    )
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    usage_limit_arn: Optional[str] = Field(default=None, alias="usageLimitArn")
    usage_limit_id: Optional[str] = Field(default=None, alias="usageLimitId")
    usage_type: Optional[
        Literal["cross-region-datasharing", "serverless-compute"]
    ] = Field(default=None, alias="usageType")


class DeleteEndpointAccessRequestModel(BaseModel):
    endpoint_name: str = Field(alias="endpointName")


class DeleteNamespaceRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    final_snapshot_name: Optional[str] = Field(default=None, alias="finalSnapshotName")
    final_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="finalSnapshotRetentionPeriod"
    )


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class DeleteSnapshotRequestModel(BaseModel):
    snapshot_name: str = Field(alias="snapshotName")


class DeleteUsageLimitRequestModel(BaseModel):
    usage_limit_id: str = Field(alias="usageLimitId")


class DeleteWorkgroupRequestModel(BaseModel):
    workgroup_name: str = Field(alias="workgroupName")


class VpcSecurityGroupMembershipModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="status")
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="vpcSecurityGroupId"
    )


class GetCredentialsRequestModel(BaseModel):
    workgroup_name: str = Field(alias="workgroupName")
    db_name: Optional[str] = Field(default=None, alias="dbName")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")


class GetEndpointAccessRequestModel(BaseModel):
    endpoint_name: str = Field(alias="endpointName")


class GetNamespaceRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")


class GetRecoveryPointRequestModel(BaseModel):
    recovery_point_id: str = Field(alias="recoveryPointId")


class RecoveryPointModel(BaseModel):
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    recovery_point_create_time: Optional[datetime] = Field(
        default=None, alias="recoveryPointCreateTime"
    )
    recovery_point_id: Optional[str] = Field(default=None, alias="recoveryPointId")
    total_size_in_mega_bytes: Optional[float] = Field(
        default=None, alias="totalSizeInMegaBytes"
    )
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class GetResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ResourcePolicyModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="policy")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")


class GetSnapshotRequestModel(BaseModel):
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    snapshot_arn: Optional[str] = Field(default=None, alias="snapshotArn")
    snapshot_name: Optional[str] = Field(default=None, alias="snapshotName")


class GetTableRestoreStatusRequestModel(BaseModel):
    table_restore_request_id: str = Field(alias="tableRestoreRequestId")


class TableRestoreStatusModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    new_table_name: Optional[str] = Field(default=None, alias="newTableName")
    progress_in_mega_bytes: Optional[int] = Field(
        default=None, alias="progressInMegaBytes"
    )
    request_time: Optional[datetime] = Field(default=None, alias="requestTime")
    snapshot_name: Optional[str] = Field(default=None, alias="snapshotName")
    source_database_name: Optional[str] = Field(
        default=None, alias="sourceDatabaseName"
    )
    source_schema_name: Optional[str] = Field(default=None, alias="sourceSchemaName")
    source_table_name: Optional[str] = Field(default=None, alias="sourceTableName")
    status: Optional[str] = Field(default=None, alias="status")
    table_restore_request_id: Optional[str] = Field(
        default=None, alias="tableRestoreRequestId"
    )
    target_database_name: Optional[str] = Field(
        default=None, alias="targetDatabaseName"
    )
    target_schema_name: Optional[str] = Field(default=None, alias="targetSchemaName")
    total_data_in_mega_bytes: Optional[int] = Field(
        default=None, alias="totalDataInMegaBytes"
    )
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class GetUsageLimitRequestModel(BaseModel):
    usage_limit_id: str = Field(alias="usageLimitId")


class GetWorkgroupRequestModel(BaseModel):
    workgroup_name: str = Field(alias="workgroupName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEndpointAccessRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class ListNamespacesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRecoveryPointsRequestModel(BaseModel):
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")


class ListSnapshotsRequestModel(BaseModel):
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")


class ListTableRestoreStatusRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListUsageLimitsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    usage_type: Optional[
        Literal["cross-region-datasharing", "serverless-compute"]
    ] = Field(default=None, alias="usageType")


class ListWorkgroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class NetworkInterfaceModel(BaseModel):
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    network_interface_id: Optional[str] = Field(
        default=None, alias="networkInterfaceId"
    )
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")


class PutResourcePolicyRequestModel(BaseModel):
    policy: str = Field(alias="policy")
    resource_arn: str = Field(alias="resourceArn")


class RestoreFromRecoveryPointRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    recovery_point_id: str = Field(alias="recoveryPointId")
    workgroup_name: str = Field(alias="workgroupName")


class RestoreFromSnapshotRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    workgroup_name: str = Field(alias="workgroupName")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    snapshot_arn: Optional[str] = Field(default=None, alias="snapshotArn")
    snapshot_name: Optional[str] = Field(default=None, alias="snapshotName")


class RestoreTableFromSnapshotRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    new_table_name: str = Field(alias="newTableName")
    snapshot_name: str = Field(alias="snapshotName")
    source_database_name: str = Field(alias="sourceDatabaseName")
    source_table_name: str = Field(alias="sourceTableName")
    workgroup_name: str = Field(alias="workgroupName")
    activate_case_sensitive_identifier: Optional[bool] = Field(
        default=None, alias="activateCaseSensitiveIdentifier"
    )
    source_schema_name: Optional[str] = Field(default=None, alias="sourceSchemaName")
    target_database_name: Optional[str] = Field(
        default=None, alias="targetDatabaseName"
    )
    target_schema_name: Optional[str] = Field(default=None, alias="targetSchemaName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateEndpointAccessRequestModel(BaseModel):
    endpoint_name: str = Field(alias="endpointName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcSecurityGroupIds"
    )


class UpdateNamespaceRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    admin_user_password: Optional[str] = Field(default=None, alias="adminUserPassword")
    admin_username: Optional[str] = Field(default=None, alias="adminUsername")
    default_iam_role_arn: Optional[str] = Field(default=None, alias="defaultIamRoleArn")
    iam_roles: Optional[Sequence[str]] = Field(default=None, alias="iamRoles")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    log_exports: Optional[
        Sequence[Literal["connectionlog", "useractivitylog", "userlog"]]
    ] = Field(default=None, alias="logExports")


class UpdateSnapshotRequestModel(BaseModel):
    snapshot_name: str = Field(alias="snapshotName")
    retention_period: Optional[int] = Field(default=None, alias="retentionPeriod")


class UpdateUsageLimitRequestModel(BaseModel):
    usage_limit_id: str = Field(alias="usageLimitId")
    amount: Optional[int] = Field(default=None, alias="amount")
    breach_action: Optional[Literal["deactivate", "emit-metric", "log"]] = Field(
        default=None, alias="breachAction"
    )


class UpdateWorkgroupRequestModel(BaseModel):
    workgroup_name: str = Field(alias="workgroupName")
    base_capacity: Optional[int] = Field(default=None, alias="baseCapacity")
    config_parameters: Optional[Sequence[ConfigParameterModel]] = Field(
        default=None, alias="configParameters"
    )
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="enhancedVpcRouting"
    )
    port: Optional[int] = Field(default=None, alias="port")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")


class ConvertRecoveryPointToSnapshotRequestModel(BaseModel):
    recovery_point_id: str = Field(alias="recoveryPointId")
    snapshot_name: str = Field(alias="snapshotName")
    retention_period: Optional[int] = Field(default=None, alias="retentionPeriod")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateNamespaceRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    admin_user_password: Optional[str] = Field(default=None, alias="adminUserPassword")
    admin_username: Optional[str] = Field(default=None, alias="adminUsername")
    db_name: Optional[str] = Field(default=None, alias="dbName")
    default_iam_role_arn: Optional[str] = Field(default=None, alias="defaultIamRoleArn")
    iam_roles: Optional[Sequence[str]] = Field(default=None, alias="iamRoles")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    log_exports: Optional[
        Sequence[Literal["connectionlog", "useractivitylog", "userlog"]]
    ] = Field(default=None, alias="logExports")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateSnapshotRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    snapshot_name: str = Field(alias="snapshotName")
    retention_period: Optional[int] = Field(default=None, alias="retentionPeriod")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateWorkgroupRequestModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    workgroup_name: str = Field(alias="workgroupName")
    base_capacity: Optional[int] = Field(default=None, alias="baseCapacity")
    config_parameters: Optional[Sequence[ConfigParameterModel]] = Field(
        default=None, alias="configParameters"
    )
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="enhancedVpcRouting"
    )
    port: Optional[int] = Field(default=None, alias="port")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class GetCredentialsResponseModel(BaseModel):
    db_password: str = Field(alias="dbPassword")
    db_user: str = Field(alias="dbUser")
    expiration: datetime = Field(alias="expiration")
    next_refresh_time: datetime = Field(alias="nextRefreshTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConvertRecoveryPointToSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSnapshotsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    snapshots: List[SnapshotModel] = Field(alias="snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNamespaceResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNamespaceResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNamespaceResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNamespacesResponseModel(BaseModel):
    namespaces: List[NamespaceModel] = Field(alias="namespaces")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreFromRecoveryPointResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    recovery_point_id: str = Field(alias="recoveryPointId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreFromSnapshotResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    owner_account: str = Field(alias="ownerAccount")
    snapshot_name: str = Field(alias="snapshotName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNamespaceResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="namespace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUsageLimitResponseModel(BaseModel):
    usage_limit: UsageLimitModel = Field(alias="usageLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteUsageLimitResponseModel(BaseModel):
    usage_limit: UsageLimitModel = Field(alias="usageLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUsageLimitResponseModel(BaseModel):
    usage_limit: UsageLimitModel = Field(alias="usageLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsageLimitsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    usage_limits: List[UsageLimitModel] = Field(alias="usageLimits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUsageLimitResponseModel(BaseModel):
    usage_limit: UsageLimitModel = Field(alias="usageLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecoveryPointResponseModel(BaseModel):
    recovery_point: RecoveryPointModel = Field(alias="recoveryPoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecoveryPointsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    recovery_points: List[RecoveryPointModel] = Field(alias="recoveryPoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="resourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="resourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTableRestoreStatusResponseModel(BaseModel):
    table_restore_status: TableRestoreStatusModel = Field(alias="tableRestoreStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTableRestoreStatusResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    table_restore_statuses: List[TableRestoreStatusModel] = Field(
        alias="tableRestoreStatuses"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreTableFromSnapshotResponseModel(BaseModel):
    table_restore_status: TableRestoreStatusModel = Field(alias="tableRestoreStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointAccessRequestListEndpointAccessPaginateModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNamespacesRequestListNamespacesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecoveryPointsRequestListRecoveryPointsPaginateModel(BaseModel):
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSnapshotsRequestListSnapshotsPaginateModel(BaseModel):
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    namespace_arn: Optional[str] = Field(default=None, alias="namespaceArn")
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    owner_account: Optional[str] = Field(default=None, alias="ownerAccount")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTableRestoreStatusRequestListTableRestoreStatusPaginateModel(BaseModel):
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsageLimitsRequestListUsageLimitsPaginateModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    usage_type: Optional[
        Literal["cross-region-datasharing", "serverless-compute"]
    ] = Field(default=None, alias="usageType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkgroupsRequestListWorkgroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class VpcEndpointModel(BaseModel):
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="vpcEndpointId")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class EndpointAccessModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="address")
    endpoint_arn: Optional[str] = Field(default=None, alias="endpointArn")
    endpoint_create_time: Optional[datetime] = Field(
        default=None, alias="endpointCreateTime"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="endpointName")
    endpoint_status: Optional[str] = Field(default=None, alias="endpointStatus")
    port: Optional[int] = Field(default=None, alias="port")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    vpc_endpoint: Optional[VpcEndpointModel] = Field(default=None, alias="vpcEndpoint")
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="vpcSecurityGroups"
    )
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="address")
    port: Optional[int] = Field(default=None, alias="port")
    vpc_endpoints: Optional[List[VpcEndpointModel]] = Field(
        default=None, alias="vpcEndpoints"
    )


class CreateEndpointAccessResponseModel(BaseModel):
    endpoint: EndpointAccessModel = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEndpointAccessResponseModel(BaseModel):
    endpoint: EndpointAccessModel = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEndpointAccessResponseModel(BaseModel):
    endpoint: EndpointAccessModel = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointAccessResponseModel(BaseModel):
    endpoints: List[EndpointAccessModel] = Field(alias="endpoints")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointAccessResponseModel(BaseModel):
    endpoint: EndpointAccessModel = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkgroupModel(BaseModel):
    base_capacity: Optional[int] = Field(default=None, alias="baseCapacity")
    config_parameters: Optional[List[ConfigParameterModel]] = Field(
        default=None, alias="configParameters"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    endpoint: Optional[EndpointModel] = Field(default=None, alias="endpoint")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="enhancedVpcRouting"
    )
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")
    port: Optional[int] = Field(default=None, alias="port")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    status: Optional[Literal["AVAILABLE", "CREATING", "DELETING", "MODIFYING"]] = Field(
        default=None, alias="status"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    workgroup_arn: Optional[str] = Field(default=None, alias="workgroupArn")
    workgroup_id: Optional[str] = Field(default=None, alias="workgroupId")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")


class CreateWorkgroupResponseModel(BaseModel):
    workgroup: WorkgroupModel = Field(alias="workgroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWorkgroupResponseModel(BaseModel):
    workgroup: WorkgroupModel = Field(alias="workgroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkgroupResponseModel(BaseModel):
    workgroup: WorkgroupModel = Field(alias="workgroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkgroupsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workgroups: List[WorkgroupModel] = Field(alias="workgroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkgroupResponseModel(BaseModel):
    workgroup: WorkgroupModel = Field(alias="workgroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
