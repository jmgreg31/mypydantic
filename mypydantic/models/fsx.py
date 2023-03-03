# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActiveDirectoryBackupAttributesModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    active_directory_id: Optional[str] = Field(default=None, alias="ActiveDirectoryId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")


class AdministrativeActionFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class AliasModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    lifecycle: Optional[
        Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
    ] = Field(default=None, alias="Lifecycle")


class AssociateFileSystemAliasesRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    aliases: Sequence[str] = Field(alias="Aliases")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AutoExportPolicyModel(BaseModel):
    events: Optional[Sequence[Literal["CHANGED", "DELETED", "NEW"]]] = Field(
        default=None, alias="Events"
    )


class AutoImportPolicyModel(BaseModel):
    events: Optional[Sequence[Literal["CHANGED", "DELETED", "NEW"]]] = Field(
        default=None, alias="Events"
    )


class BackupFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CancelDataRepositoryTaskRequestModel(BaseModel):
    task_id: str = Field(alias="TaskId")


class CompletionReportModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    path: Optional[str] = Field(default=None, alias="Path")
    format: Optional[Literal["REPORT_CSV_20191124"]] = Field(
        default=None, alias="Format"
    )
    scope: Optional[Literal["FAILED_FILES_ONLY"]] = Field(default=None, alias="Scope")


class FileCacheLustreMetadataConfigurationModel(BaseModel):
    storage_capacity: int = Field(alias="StorageCapacity")


class LustreLogCreateConfigurationModel(BaseModel):
    level: Literal["DISABLED", "ERROR_ONLY", "WARN_ERROR", "WARN_ONLY"] = Field(
        alias="Level"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")


class LustreRootSquashConfigurationModel(BaseModel):
    root_squash: Optional[str] = Field(default=None, alias="RootSquash")
    no_squash_nids: Optional[List[str]] = Field(default=None, alias="NoSquashNids")


class DiskIopsConfigurationModel(BaseModel):
    mode: Optional[Literal["AUTOMATIC", "USER_PROVISIONED"]] = Field(
        default=None, alias="Mode"
    )
    iops: Optional[int] = Field(default=None, alias="Iops")


class SelfManagedActiveDirectoryConfigurationModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    user_name: str = Field(alias="UserName")
    password: str = Field(alias="Password")
    dns_ips: Sequence[str] = Field(alias="DnsIps")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="OrganizationalUnitDistinguishedName"
    )
    file_system_administrators_group: Optional[str] = Field(
        default=None, alias="FileSystemAdministratorsGroup"
    )


class WindowsAuditLogCreateConfigurationModel(BaseModel):
    file_access_audit_log_level: Literal[
        "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
    ] = Field(alias="FileAccessAuditLogLevel")
    file_share_access_audit_log_level: Literal[
        "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
    ] = Field(alias="FileShareAccessAuditLogLevel")
    audit_log_destination: Optional[str] = Field(
        default=None, alias="AuditLogDestination"
    )


class TieringPolicyModel(BaseModel):
    cooling_period: Optional[int] = Field(default=None, alias="CoolingPeriod")
    name: Optional[Literal["ALL", "AUTO", "NONE", "SNAPSHOT_ONLY"]] = Field(
        default=None, alias="Name"
    )


class CreateOpenZFSOriginSnapshotConfigurationModel(BaseModel):
    snapshot_arn: str = Field(alias="SnapshotARN")
    copy_strategy: Literal["CLONE", "FULL_COPY"] = Field(alias="CopyStrategy")


class OpenZFSUserOrGroupQuotaModel(BaseModel):
    type: Literal["GROUP", "USER"] = Field(alias="Type")
    id: int = Field(alias="Id")
    storage_capacity_quota_gi_b: int = Field(alias="StorageCapacityQuotaGiB")


class DataRepositoryFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class DataRepositoryTaskFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class DataRepositoryTaskFilterModel(BaseModel):
    name: Optional[
        Literal[
            "data-repository-association-id",
            "file-cache-id",
            "file-system-id",
            "task-lifecycle",
        ]
    ] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DataRepositoryTaskStatusModel(BaseModel):
    total_count: Optional[int] = Field(default=None, alias="TotalCount")
    succeeded_count: Optional[int] = Field(default=None, alias="SucceededCount")
    failed_count: Optional[int] = Field(default=None, alias="FailedCount")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    released_capacity: Optional[int] = Field(default=None, alias="ReleasedCapacity")


class DeleteBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteDataRepositoryAssociationRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    delete_data_in_file_system: Optional[bool] = Field(
        default=None, alias="DeleteDataInFileSystem"
    )


class DeleteFileCacheRequestModel(BaseModel):
    file_cache_id: str = Field(alias="FileCacheId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteSnapshotRequestModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteStorageVirtualMachineRequestModel(BaseModel):
    storage_virtual_machine_id: str = Field(alias="StorageVirtualMachineId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class DeleteVolumeOpenZFSConfigurationModel(BaseModel):
    options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = Field(
        default=None, alias="Options"
    )


class FilterModel(BaseModel):
    name: Optional[
        Literal[
            "backup-type",
            "data-repository-type",
            "file-cache-id",
            "file-cache-type",
            "file-system-id",
            "file-system-type",
            "volume-id",
        ]
    ] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeFileCachesRequestModel(BaseModel):
    file_cache_ids: Optional[Sequence[str]] = Field(default=None, alias="FileCacheIds")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFileSystemAliasesRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFileSystemsRequestModel(BaseModel):
    file_system_ids: Optional[Sequence[str]] = Field(
        default=None, alias="FileSystemIds"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SnapshotFilterModel(BaseModel):
    name: Optional[Literal["file-system-id", "volume-id"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class StorageVirtualMachineFilterModel(BaseModel):
    name: Optional[Literal["file-system-id"]] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class VolumeFilterModel(BaseModel):
    name: Optional[Literal["file-system-id", "storage-virtual-machine-id"]] = Field(
        default=None, alias="Name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DisassociateFileSystemAliasesRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    aliases: Sequence[str] = Field(alias="Aliases")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class FileCacheFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class FileCacheNFSConfigurationModel(BaseModel):
    version: Literal["NFS3"] = Field(alias="Version")
    dns_ips: Optional[Sequence[str]] = Field(default=None, alias="DnsIps")


class LustreLogConfigurationModel(BaseModel):
    level: Literal["DISABLED", "ERROR_ONLY", "WARN_ERROR", "WARN_ONLY"] = Field(
        alias="Level"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")


class FileSystemEndpointModel(BaseModel):
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    ip_addresses: Optional[List[str]] = Field(default=None, alias="IpAddresses")


class FileSystemFailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class LifecycleTransitionReasonModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OpenZFSClientConfigurationModel(BaseModel):
    clients: str = Field(alias="Clients")
    options: List[str] = Field(alias="Options")


class OpenZFSOriginSnapshotConfigurationModel(BaseModel):
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotARN")
    copy_strategy: Optional[Literal["CLONE", "FULL_COPY"]] = Field(
        default=None, alias="CopyStrategy"
    )


class ReleaseFileSystemNfsV3LocksRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class RestoreVolumeFromSnapshotRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    snapshot_id: str = Field(alias="SnapshotId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    options: Optional[
        Sequence[Literal["DELETE_CLONED_VOLUMES", "DELETE_INTERMEDIATE_SNAPSHOTS"]]
    ] = Field(default=None, alias="Options")


class SelfManagedActiveDirectoryAttributesModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="OrganizationalUnitDistinguishedName"
    )
    file_system_administrators_group: Optional[str] = Field(
        default=None, alias="FileSystemAdministratorsGroup"
    )
    user_name: Optional[str] = Field(default=None, alias="UserName")
    dns_ips: Optional[List[str]] = Field(default=None, alias="DnsIps")


class SelfManagedActiveDirectoryConfigurationUpdatesModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    password: Optional[str] = Field(default=None, alias="Password")
    dns_ips: Optional[Sequence[str]] = Field(default=None, alias="DnsIps")


class SvmEndpointModel(BaseModel):
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    ip_addresses: Optional[List[str]] = Field(default=None, alias="IpAddresses")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFileCacheLustreConfigurationModel(BaseModel):
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )


class UpdateSnapshotRequestModel(BaseModel):
    name: str = Field(alias="Name")
    snapshot_id: str = Field(alias="SnapshotId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class WindowsAuditLogConfigurationModel(BaseModel):
    file_access_audit_log_level: Literal[
        "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
    ] = Field(alias="FileAccessAuditLogLevel")
    file_share_access_audit_log_level: Literal[
        "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
    ] = Field(alias="FileShareAccessAuditLogLevel")
    audit_log_destination: Optional[str] = Field(
        default=None, alias="AuditLogDestination"
    )


class AssociateFileSystemAliasesResponseModel(BaseModel):
    aliases: List[AliasModel] = Field(alias="Aliases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelDataRepositoryTaskResponseModel(BaseModel):
    lifecycle: Literal[
        "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
    ] = Field(alias="Lifecycle")
    task_id: str = Field(alias="TaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileSystemFromBackupResponseModel(BaseModel):
    file_system: FileSystemModel = Field(alias="FileSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileSystemResponseModel(BaseModel):
    file_system: FileSystemModel = Field(alias="FileSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackupResponseModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    lifecycle: Literal[
        "AVAILABLE",
        "COPYING",
        "CREATING",
        "DELETED",
        "FAILED",
        "PENDING",
        "TRANSFERRING",
    ] = Field(alias="Lifecycle")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDataRepositoryAssociationResponseModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    lifecycle: Literal[
        "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
    ] = Field(alias="Lifecycle")
    delete_data_in_file_system: bool = Field(alias="DeleteDataInFileSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFileCacheResponseModel(BaseModel):
    file_cache_id: str = Field(alias="FileCacheId")
    lifecycle: Literal[
        "AVAILABLE", "CREATING", "DELETING", "FAILED", "UPDATING"
    ] = Field(alias="Lifecycle")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotResponseModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    lifecycle: Literal["AVAILABLE", "CREATING", "DELETING", "PENDING"] = Field(
        alias="Lifecycle"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStorageVirtualMachineResponseModel(BaseModel):
    storage_virtual_machine_id: str = Field(alias="StorageVirtualMachineId")
    lifecycle: Literal[
        "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
    ] = Field(alias="Lifecycle")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileSystemAliasesResponseModel(BaseModel):
    aliases: List[AliasModel] = Field(alias="Aliases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileSystemsResponseModel(BaseModel):
    file_systems: List[FileSystemModel] = Field(alias="FileSystems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateFileSystemAliasesResponseModel(BaseModel):
    aliases: List[AliasModel] = Field(alias="Aliases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReleaseFileSystemNfsV3LocksResponseModel(BaseModel):
    file_system: FileSystemModel = Field(alias="FileSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreVolumeFromSnapshotResponseModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    lifecycle: Literal[
        "AVAILABLE",
        "CREATED",
        "CREATING",
        "DELETING",
        "FAILED",
        "MISCONFIGURED",
        "PENDING",
    ] = Field(alias="Lifecycle")
    administrative_actions: List[AdministrativeActionModel] = Field(
        alias="AdministrativeActions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFileSystemResponseModel(BaseModel):
    file_system: FileSystemModel = Field(alias="FileSystem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NFSDataRepositoryConfigurationModel(BaseModel):
    version: Literal["NFS3"] = Field(alias="Version")
    dns_ips: Optional[List[str]] = Field(default=None, alias="DnsIps")
    auto_export_policy: Optional[AutoExportPolicyModel] = Field(
        default=None, alias="AutoExportPolicy"
    )


class S3DataRepositoryConfigurationModel(BaseModel):
    auto_import_policy: Optional[AutoImportPolicyModel] = Field(
        default=None, alias="AutoImportPolicy"
    )
    auto_export_policy: Optional[AutoExportPolicyModel] = Field(
        default=None, alias="AutoExportPolicy"
    )


class CopyBackupRequestModel(BaseModel):
    source_backup_id: str = Field(alias="SourceBackupId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    copy_tags: Optional[bool] = Field(default=None, alias="CopyTags")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateBackupRequestModel(BaseModel):
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")


class CreateSnapshotRequestModel(BaseModel):
    name: str = Field(alias="Name")
    volume_id: str = Field(alias="VolumeId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DeleteFileSystemLustreConfigurationModel(BaseModel):
    skip_final_backup: Optional[bool] = Field(default=None, alias="SkipFinalBackup")
    final_backup_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteFileSystemLustreResponseModel(BaseModel):
    final_backup_id: Optional[str] = Field(default=None, alias="FinalBackupId")
    final_backup_tags: Optional[List[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteFileSystemOpenZFSConfigurationModel(BaseModel):
    skip_final_backup: Optional[bool] = Field(default=None, alias="SkipFinalBackup")
    final_backup_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )
    options: Optional[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]] = Field(
        default=None, alias="Options"
    )


class DeleteFileSystemOpenZFSResponseModel(BaseModel):
    final_backup_id: Optional[str] = Field(default=None, alias="FinalBackupId")
    final_backup_tags: Optional[List[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteFileSystemWindowsConfigurationModel(BaseModel):
    skip_final_backup: Optional[bool] = Field(default=None, alias="SkipFinalBackup")
    final_backup_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteFileSystemWindowsResponseModel(BaseModel):
    final_backup_id: Optional[str] = Field(default=None, alias="FinalBackupId")
    final_backup_tags: Optional[List[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteVolumeOntapConfigurationModel(BaseModel):
    skip_final_backup: Optional[bool] = Field(default=None, alias="SkipFinalBackup")
    final_backup_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class DeleteVolumeOntapResponseModel(BaseModel):
    final_backup_id: Optional[str] = Field(default=None, alias="FinalBackupId")
    final_backup_tags: Optional[List[TagModel]] = Field(
        default=None, alias="FinalBackupTags"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateDataRepositoryTaskRequestModel(BaseModel):
    type: Literal[
        "AUTO_RELEASE_DATA",
        "EXPORT_TO_REPOSITORY",
        "IMPORT_METADATA_FROM_REPOSITORY",
        "RELEASE_DATA_FROM_FILESYSTEM",
    ] = Field(alias="Type")
    file_system_id: str = Field(alias="FileSystemId")
    report: CompletionReportModel = Field(alias="Report")
    paths: Optional[Sequence[str]] = Field(default=None, alias="Paths")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    capacity_to_release: Optional[int] = Field(default=None, alias="CapacityToRelease")


class CreateFileCacheLustreConfigurationModel(BaseModel):
    per_unit_storage_throughput: int = Field(alias="PerUnitStorageThroughput")
    deployment_type: Literal["CACHE_1"] = Field(alias="DeploymentType")
    metadata_configuration: FileCacheLustreMetadataConfigurationModel = Field(
        alias="MetadataConfiguration"
    )
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )


class CreateFileSystemLustreConfigurationModel(BaseModel):
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    import_path: Optional[str] = Field(default=None, alias="ImportPath")
    export_path: Optional[str] = Field(default=None, alias="ExportPath")
    imported_file_chunk_size: Optional[int] = Field(
        default=None, alias="ImportedFileChunkSize"
    )
    deployment_type: Optional[
        Literal["PERSISTENT_1", "PERSISTENT_2", "SCRATCH_1", "SCRATCH_2"]
    ] = Field(default=None, alias="DeploymentType")
    auto_import_policy: Optional[
        Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
    ] = Field(default=None, alias="AutoImportPolicy")
    per_unit_storage_throughput: Optional[int] = Field(
        default=None, alias="PerUnitStorageThroughput"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    drive_cache_type: Optional[Literal["NONE", "READ"]] = Field(
        default=None, alias="DriveCacheType"
    )
    data_compression_type: Optional[Literal["LZ4", "NONE"]] = Field(
        default=None, alias="DataCompressionType"
    )
    log_configuration: Optional[LustreLogCreateConfigurationModel] = Field(
        default=None, alias="LogConfiguration"
    )
    root_squash_configuration: Optional[LustreRootSquashConfigurationModel] = Field(
        default=None, alias="RootSquashConfiguration"
    )


class UpdateFileSystemLustreConfigurationModel(BaseModel):
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    auto_import_policy: Optional[
        Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
    ] = Field(default=None, alias="AutoImportPolicy")
    data_compression_type: Optional[Literal["LZ4", "NONE"]] = Field(
        default=None, alias="DataCompressionType"
    )
    log_configuration: Optional[LustreLogCreateConfigurationModel] = Field(
        default=None, alias="LogConfiguration"
    )
    root_squash_configuration: Optional[LustreRootSquashConfigurationModel] = Field(
        default=None, alias="RootSquashConfiguration"
    )


class CreateFileSystemOntapConfigurationModel(BaseModel):
    deployment_type: Literal["MULTI_AZ_1", "SINGLE_AZ_1"] = Field(
        alias="DeploymentType"
    )
    throughput_capacity: int = Field(alias="ThroughputCapacity")
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    endpoint_ip_address_range: Optional[str] = Field(
        default=None, alias="EndpointIpAddressRange"
    )
    fsx_admin_password: Optional[str] = Field(default=None, alias="FsxAdminPassword")
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )
    preferred_subnet_id: Optional[str] = Field(default=None, alias="PreferredSubnetId")
    route_table_ids: Optional[Sequence[str]] = Field(
        default=None, alias="RouteTableIds"
    )
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )


class OpenZFSFileSystemConfigurationModel(BaseModel):
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    copy_tags_to_volumes: Optional[bool] = Field(
        default=None, alias="CopyTagsToVolumes"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    deployment_type: Optional[Literal["SINGLE_AZ_1", "SINGLE_AZ_2"]] = Field(
        default=None, alias="DeploymentType"
    )
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )
    root_volume_id: Optional[str] = Field(default=None, alias="RootVolumeId")


class UpdateFileSystemOntapConfigurationModel(BaseModel):
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    fsx_admin_password: Optional[str] = Field(default=None, alias="FsxAdminPassword")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    add_route_table_ids: Optional[Sequence[str]] = Field(
        default=None, alias="AddRouteTableIds"
    )
    remove_route_table_ids: Optional[Sequence[str]] = Field(
        default=None, alias="RemoveRouteTableIds"
    )


class UpdateFileSystemOpenZFSConfigurationModel(BaseModel):
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    copy_tags_to_volumes: Optional[bool] = Field(
        default=None, alias="CopyTagsToVolumes"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )


class CreateSvmActiveDirectoryConfigurationModel(BaseModel):
    net_bios_name: str = Field(alias="NetBiosName")
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryConfigurationModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")


class CreateFileSystemWindowsConfigurationModel(BaseModel):
    throughput_capacity: int = Field(alias="ThroughputCapacity")
    active_directory_id: Optional[str] = Field(default=None, alias="ActiveDirectoryId")
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryConfigurationModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")
    deployment_type: Optional[
        Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
    ] = Field(default=None, alias="DeploymentType")
    preferred_subnet_id: Optional[str] = Field(default=None, alias="PreferredSubnetId")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    aliases: Optional[Sequence[str]] = Field(default=None, alias="Aliases")
    audit_log_configuration: Optional[WindowsAuditLogCreateConfigurationModel] = Field(
        default=None, alias="AuditLogConfiguration"
    )


class CreateOntapVolumeConfigurationModel(BaseModel):
    size_in_megabytes: int = Field(alias="SizeInMegabytes")
    storage_virtual_machine_id: str = Field(alias="StorageVirtualMachineId")
    junction_path: Optional[str] = Field(default=None, alias="JunctionPath")
    security_style: Optional[Literal["MIXED", "NTFS", "UNIX"]] = Field(
        default=None, alias="SecurityStyle"
    )
    storage_efficiency_enabled: Optional[bool] = Field(
        default=None, alias="StorageEfficiencyEnabled"
    )
    tiering_policy: Optional[TieringPolicyModel] = Field(
        default=None, alias="TieringPolicy"
    )
    ontap_volume_type: Optional[Literal["DP", "RW"]] = Field(
        default=None, alias="OntapVolumeType"
    )
    snapshot_policy: Optional[str] = Field(default=None, alias="SnapshotPolicy")
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )


class OntapVolumeConfigurationModel(BaseModel):
    flex_cache_endpoint_type: Optional[Literal["CACHE", "NONE", "ORIGIN"]] = Field(
        default=None, alias="FlexCacheEndpointType"
    )
    junction_path: Optional[str] = Field(default=None, alias="JunctionPath")
    security_style: Optional[Literal["MIXED", "NTFS", "UNIX"]] = Field(
        default=None, alias="SecurityStyle"
    )
    size_in_megabytes: Optional[int] = Field(default=None, alias="SizeInMegabytes")
    storage_efficiency_enabled: Optional[bool] = Field(
        default=None, alias="StorageEfficiencyEnabled"
    )
    storage_virtual_machine_id: Optional[str] = Field(
        default=None, alias="StorageVirtualMachineId"
    )
    storage_virtual_machine_root: Optional[bool] = Field(
        default=None, alias="StorageVirtualMachineRoot"
    )
    tiering_policy: Optional[TieringPolicyModel] = Field(
        default=None, alias="TieringPolicy"
    )
    uuid: Optional[str] = Field(default=None, alias="UUID")
    ontap_volume_type: Optional[Literal["DP", "LS", "RW"]] = Field(
        default=None, alias="OntapVolumeType"
    )
    snapshot_policy: Optional[str] = Field(default=None, alias="SnapshotPolicy")
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )


class UpdateOntapVolumeConfigurationModel(BaseModel):
    junction_path: Optional[str] = Field(default=None, alias="JunctionPath")
    security_style: Optional[Literal["MIXED", "NTFS", "UNIX"]] = Field(
        default=None, alias="SecurityStyle"
    )
    size_in_megabytes: Optional[int] = Field(default=None, alias="SizeInMegabytes")
    storage_efficiency_enabled: Optional[bool] = Field(
        default=None, alias="StorageEfficiencyEnabled"
    )
    tiering_policy: Optional[TieringPolicyModel] = Field(
        default=None, alias="TieringPolicy"
    )
    snapshot_policy: Optional[str] = Field(default=None, alias="SnapshotPolicy")
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )


class DataRepositoryConfigurationModel(BaseModel):
    lifecycle: Optional[
        Literal[
            "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
        ]
    ] = Field(default=None, alias="Lifecycle")
    import_path: Optional[str] = Field(default=None, alias="ImportPath")
    export_path: Optional[str] = Field(default=None, alias="ExportPath")
    imported_file_chunk_size: Optional[int] = Field(
        default=None, alias="ImportedFileChunkSize"
    )
    auto_import_policy: Optional[
        Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
    ] = Field(default=None, alias="AutoImportPolicy")
    failure_details: Optional[DataRepositoryFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )


class DescribeDataRepositoryTasksRequestModel(BaseModel):
    task_ids: Optional[Sequence[str]] = Field(default=None, alias="TaskIds")
    filters: Optional[Sequence[DataRepositoryTaskFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DataRepositoryTaskModel(BaseModel):
    task_id: str = Field(alias="TaskId")
    lifecycle: Literal[
        "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
    ] = Field(alias="Lifecycle")
    type: Literal[
        "AUTO_RELEASE_DATA",
        "EXPORT_TO_REPOSITORY",
        "IMPORT_METADATA_FROM_REPOSITORY",
        "RELEASE_DATA_FROM_FILESYSTEM",
    ] = Field(alias="Type")
    creation_time: datetime = Field(alias="CreationTime")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    paths: Optional[List[str]] = Field(default=None, alias="Paths")
    failure_details: Optional[DataRepositoryTaskFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    status: Optional[DataRepositoryTaskStatusModel] = Field(
        default=None, alias="Status"
    )
    report: Optional[CompletionReportModel] = Field(default=None, alias="Report")
    capacity_to_release: Optional[int] = Field(default=None, alias="CapacityToRelease")
    file_cache_id: Optional[str] = Field(default=None, alias="FileCacheId")


class DescribeBackupsRequestModel(BaseModel):
    backup_ids: Optional[Sequence[str]] = Field(default=None, alias="BackupIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeDataRepositoryAssociationsRequestModel(BaseModel):
    association_ids: Optional[Sequence[str]] = Field(
        default=None, alias="AssociationIds"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBackupsRequestDescribeBackupsPaginateModel(BaseModel):
    backup_ids: Optional[Sequence[str]] = Field(default=None, alias="BackupIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFileSystemsRequestDescribeFileSystemsPaginateModel(BaseModel):
    file_system_ids: Optional[Sequence[str]] = Field(
        default=None, alias="FileSystemIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotsRequestModel(BaseModel):
    snapshot_ids: Optional[Sequence[str]] = Field(default=None, alias="SnapshotIds")
    filters: Optional[Sequence[SnapshotFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeStorageVirtualMachinesRequestDescribeStorageVirtualMachinesPaginateModel(
    BaseModel
):
    storage_virtual_machine_ids: Optional[Sequence[str]] = Field(
        default=None, alias="StorageVirtualMachineIds"
    )
    filters: Optional[Sequence[StorageVirtualMachineFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStorageVirtualMachinesRequestModel(BaseModel):
    storage_virtual_machine_ids: Optional[Sequence[str]] = Field(
        default=None, alias="StorageVirtualMachineIds"
    )
    filters: Optional[Sequence[StorageVirtualMachineFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeVolumesRequestDescribeVolumesPaginateModel(BaseModel):
    volume_ids: Optional[Sequence[str]] = Field(default=None, alias="VolumeIds")
    filters: Optional[Sequence[VolumeFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeVolumesRequestModel(BaseModel):
    volume_ids: Optional[Sequence[str]] = Field(default=None, alias="VolumeIds")
    filters: Optional[Sequence[VolumeFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class FileCacheDataRepositoryAssociationModel(BaseModel):
    file_cache_path: str = Field(alias="FileCachePath")
    data_repository_path: str = Field(alias="DataRepositoryPath")
    data_repository_subdirectories: Optional[Sequence[str]] = Field(
        default=None, alias="DataRepositorySubdirectories"
    )
    nfs: Optional[FileCacheNFSConfigurationModel] = Field(default=None, alias="NFS")


class FileCacheLustreConfigurationModel(BaseModel):
    per_unit_storage_throughput: Optional[int] = Field(
        default=None, alias="PerUnitStorageThroughput"
    )
    deployment_type: Optional[Literal["CACHE_1"]] = Field(
        default=None, alias="DeploymentType"
    )
    mount_name: Optional[str] = Field(default=None, alias="MountName")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    metadata_configuration: Optional[FileCacheLustreMetadataConfigurationModel] = Field(
        default=None, alias="MetadataConfiguration"
    )
    log_configuration: Optional[LustreLogConfigurationModel] = Field(
        default=None, alias="LogConfiguration"
    )


class FileSystemEndpointsModel(BaseModel):
    intercluster: Optional[FileSystemEndpointModel] = Field(
        default=None, alias="Intercluster"
    )
    management: Optional[FileSystemEndpointModel] = Field(
        default=None, alias="Management"
    )


class SnapshotModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    name: Optional[str] = Field(default=None, alias="Name")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    lifecycle: Optional[
        Literal["AVAILABLE", "CREATING", "DELETING", "PENDING"]
    ] = Field(default=None, alias="Lifecycle")
    lifecycle_transition_reason: Optional[LifecycleTransitionReasonModel] = Field(
        default=None, alias="LifecycleTransitionReason"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    administrative_actions: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="AdministrativeActions"
    )


class OpenZFSNfsExportModel(BaseModel):
    client_configurations: List[OpenZFSClientConfigurationModel] = Field(
        alias="ClientConfigurations"
    )


class SvmActiveDirectoryConfigurationModel(BaseModel):
    net_bios_name: Optional[str] = Field(default=None, alias="NetBiosName")
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryAttributesModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")


class UpdateFileSystemWindowsConfigurationModel(BaseModel):
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryConfigurationUpdatesModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")
    audit_log_configuration: Optional[WindowsAuditLogCreateConfigurationModel] = Field(
        default=None, alias="AuditLogConfiguration"
    )


class UpdateSvmActiveDirectoryConfigurationModel(BaseModel):
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryConfigurationUpdatesModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")


class SvmEndpointsModel(BaseModel):
    iscsi: Optional[SvmEndpointModel] = Field(default=None, alias="Iscsi")
    management: Optional[SvmEndpointModel] = Field(default=None, alias="Management")
    nfs: Optional[SvmEndpointModel] = Field(default=None, alias="Nfs")
    smb: Optional[SvmEndpointModel] = Field(default=None, alias="Smb")


class UpdateFileCacheRequestModel(BaseModel):
    file_cache_id: str = Field(alias="FileCacheId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    lustre_configuration: Optional[UpdateFileCacheLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )


class WindowsFileSystemConfigurationModel(BaseModel):
    active_directory_id: Optional[str] = Field(default=None, alias="ActiveDirectoryId")
    self_managed_active_directory_configuration: Optional[
        SelfManagedActiveDirectoryAttributesModel
    ] = Field(default=None, alias="SelfManagedActiveDirectoryConfiguration")
    deployment_type: Optional[
        Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
    ] = Field(default=None, alias="DeploymentType")
    remote_administration_endpoint: Optional[str] = Field(
        default=None, alias="RemoteAdministrationEndpoint"
    )
    preferred_subnet_id: Optional[str] = Field(default=None, alias="PreferredSubnetId")
    preferred_file_server_ip: Optional[str] = Field(
        default=None, alias="PreferredFileServerIp"
    )
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    maintenance_operations_in_progress: Optional[
        List[Literal["BACKING_UP", "PATCHING"]]
    ] = Field(default=None, alias="MaintenanceOperationsInProgress")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    aliases: Optional[List[AliasModel]] = Field(default=None, alias="Aliases")
    audit_log_configuration: Optional[WindowsAuditLogConfigurationModel] = Field(
        default=None, alias="AuditLogConfiguration"
    )


class CreateDataRepositoryAssociationRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    data_repository_path: str = Field(alias="DataRepositoryPath")
    file_system_path: Optional[str] = Field(default=None, alias="FileSystemPath")
    batch_import_meta_data_on_create: Optional[bool] = Field(
        default=None, alias="BatchImportMetaDataOnCreate"
    )
    imported_file_chunk_size: Optional[int] = Field(
        default=None, alias="ImportedFileChunkSize"
    )
    s3: Optional[S3DataRepositoryConfigurationModel] = Field(default=None, alias="S3")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DataRepositoryAssociationModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    lifecycle: Optional[
        Literal[
            "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
        ]
    ] = Field(default=None, alias="Lifecycle")
    failure_details: Optional[DataRepositoryFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    file_system_path: Optional[str] = Field(default=None, alias="FileSystemPath")
    data_repository_path: Optional[str] = Field(
        default=None, alias="DataRepositoryPath"
    )
    batch_import_meta_data_on_create: Optional[bool] = Field(
        default=None, alias="BatchImportMetaDataOnCreate"
    )
    imported_file_chunk_size: Optional[int] = Field(
        default=None, alias="ImportedFileChunkSize"
    )
    s3: Optional[S3DataRepositoryConfigurationModel] = Field(default=None, alias="S3")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    file_cache_id: Optional[str] = Field(default=None, alias="FileCacheId")
    file_cache_path: Optional[str] = Field(default=None, alias="FileCachePath")
    data_repository_subdirectories: Optional[List[str]] = Field(
        default=None, alias="DataRepositorySubdirectories"
    )
    nfs: Optional[NFSDataRepositoryConfigurationModel] = Field(
        default=None, alias="NFS"
    )


class UpdateDataRepositoryAssociationRequestModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    imported_file_chunk_size: Optional[int] = Field(
        default=None, alias="ImportedFileChunkSize"
    )
    s3: Optional[S3DataRepositoryConfigurationModel] = Field(default=None, alias="S3")


class DeleteFileSystemRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    windows_configuration: Optional[DeleteFileSystemWindowsConfigurationModel] = Field(
        default=None, alias="WindowsConfiguration"
    )
    lustre_configuration: Optional[DeleteFileSystemLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    open_zfs_configuration: Optional[DeleteFileSystemOpenZFSConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class DeleteFileSystemResponseModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    lifecycle: Literal[
        "AVAILABLE",
        "CREATING",
        "DELETING",
        "FAILED",
        "MISCONFIGURED",
        "MISCONFIGURED_UNAVAILABLE",
        "UPDATING",
    ] = Field(alias="Lifecycle")
    windows_response: DeleteFileSystemWindowsResponseModel = Field(
        alias="WindowsResponse"
    )
    lustre_response: DeleteFileSystemLustreResponseModel = Field(alias="LustreResponse")
    open_zfs_response: DeleteFileSystemOpenZFSResponseModel = Field(
        alias="OpenZFSResponse"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    ontap_configuration: Optional[DeleteVolumeOntapConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    open_zfs_configuration: Optional[DeleteVolumeOpenZFSConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class DeleteVolumeResponseModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    lifecycle: Literal[
        "AVAILABLE",
        "CREATED",
        "CREATING",
        "DELETING",
        "FAILED",
        "MISCONFIGURED",
        "PENDING",
    ] = Field(alias="Lifecycle")
    ontap_response: DeleteVolumeOntapResponseModel = Field(alias="OntapResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStorageVirtualMachineRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    name: str = Field(alias="Name")
    active_directory_configuration: Optional[
        CreateSvmActiveDirectoryConfigurationModel
    ] = Field(default=None, alias="ActiveDirectoryConfiguration")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    svm_admin_password: Optional[str] = Field(default=None, alias="SvmAdminPassword")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    root_volume_security_style: Optional[Literal["MIXED", "NTFS", "UNIX"]] = Field(
        default=None, alias="RootVolumeSecurityStyle"
    )


class CreateVolumeFromBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    ontap_configuration: Optional[CreateOntapVolumeConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class LustreFileSystemConfigurationModel(BaseModel):
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    data_repository_configuration: Optional[DataRepositoryConfigurationModel] = Field(
        default=None, alias="DataRepositoryConfiguration"
    )
    deployment_type: Optional[
        Literal["PERSISTENT_1", "PERSISTENT_2", "SCRATCH_1", "SCRATCH_2"]
    ] = Field(default=None, alias="DeploymentType")
    per_unit_storage_throughput: Optional[int] = Field(
        default=None, alias="PerUnitStorageThroughput"
    )
    mount_name: Optional[str] = Field(default=None, alias="MountName")
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    drive_cache_type: Optional[Literal["NONE", "READ"]] = Field(
        default=None, alias="DriveCacheType"
    )
    data_compression_type: Optional[Literal["LZ4", "NONE"]] = Field(
        default=None, alias="DataCompressionType"
    )
    log_configuration: Optional[LustreLogConfigurationModel] = Field(
        default=None, alias="LogConfiguration"
    )
    root_squash_configuration: Optional[LustreRootSquashConfigurationModel] = Field(
        default=None, alias="RootSquashConfiguration"
    )


class CreateDataRepositoryTaskResponseModel(BaseModel):
    data_repository_task: DataRepositoryTaskModel = Field(alias="DataRepositoryTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataRepositoryTasksResponseModel(BaseModel):
    data_repository_tasks: List[DataRepositoryTaskModel] = Field(
        alias="DataRepositoryTasks"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileCacheRequestModel(BaseModel):
    file_cache_type: Literal["LUSTRE"] = Field(alias="FileCacheType")
    file_cache_type_version: str = Field(alias="FileCacheTypeVersion")
    storage_capacity: int = Field(alias="StorageCapacity")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    copy_tags_to_data_repository_associations: Optional[bool] = Field(
        default=None, alias="CopyTagsToDataRepositoryAssociations"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    lustre_configuration: Optional[CreateFileCacheLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    data_repository_associations: Optional[
        Sequence[FileCacheDataRepositoryAssociationModel]
    ] = Field(default=None, alias="DataRepositoryAssociations")


class FileCacheCreatingModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    file_cache_id: Optional[str] = Field(default=None, alias="FileCacheId")
    file_cache_type: Optional[Literal["LUSTRE"]] = Field(
        default=None, alias="FileCacheType"
    )
    file_cache_type_version: Optional[str] = Field(
        default=None, alias="FileCacheTypeVersion"
    )
    lifecycle: Optional[
        Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Lifecycle")
    failure_details: Optional[FileCacheFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="StorageCapacity")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    network_interface_ids: Optional[List[str]] = Field(
        default=None, alias="NetworkInterfaceIds"
    )
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    copy_tags_to_data_repository_associations: Optional[bool] = Field(
        default=None, alias="CopyTagsToDataRepositoryAssociations"
    )
    lustre_configuration: Optional[FileCacheLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    data_repository_association_ids: Optional[List[str]] = Field(
        default=None, alias="DataRepositoryAssociationIds"
    )


class FileCacheModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    file_cache_id: Optional[str] = Field(default=None, alias="FileCacheId")
    file_cache_type: Optional[Literal["LUSTRE"]] = Field(
        default=None, alias="FileCacheType"
    )
    file_cache_type_version: Optional[str] = Field(
        default=None, alias="FileCacheTypeVersion"
    )
    lifecycle: Optional[
        Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Lifecycle")
    failure_details: Optional[FileCacheFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="StorageCapacity")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    network_interface_ids: Optional[List[str]] = Field(
        default=None, alias="NetworkInterfaceIds"
    )
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    lustre_configuration: Optional[FileCacheLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    data_repository_association_ids: Optional[List[str]] = Field(
        default=None, alias="DataRepositoryAssociationIds"
    )


class OntapFileSystemConfigurationModel(BaseModel):
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    deployment_type: Optional[Literal["MULTI_AZ_1", "SINGLE_AZ_1"]] = Field(
        default=None, alias="DeploymentType"
    )
    endpoint_ip_address_range: Optional[str] = Field(
        default=None, alias="EndpointIpAddressRange"
    )
    endpoints: Optional[FileSystemEndpointsModel] = Field(
        default=None, alias="Endpoints"
    )
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )
    preferred_subnet_id: Optional[str] = Field(default=None, alias="PreferredSubnetId")
    route_table_ids: Optional[List[str]] = Field(default=None, alias="RouteTableIds")
    throughput_capacity: Optional[int] = Field(default=None, alias="ThroughputCapacity")
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )


class CreateSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotsResponseModel(BaseModel):
    snapshots: List[SnapshotModel] = Field(alias="Snapshots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOpenZFSVolumeConfigurationModel(BaseModel):
    parent_volume_id: str = Field(alias="ParentVolumeId")
    storage_capacity_reservation_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityReservationGiB"
    )
    storage_capacity_quota_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityQuotaGiB"
    )
    record_size_ki_b: Optional[int] = Field(default=None, alias="RecordSizeKiB")
    data_compression_type: Optional[Literal["LZ4", "NONE", "ZSTD"]] = Field(
        default=None, alias="DataCompressionType"
    )
    copy_tags_to_snapshots: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshots"
    )
    origin_snapshot: Optional[CreateOpenZFSOriginSnapshotConfigurationModel] = Field(
        default=None, alias="OriginSnapshot"
    )
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    nfs_exports: Optional[Sequence[OpenZFSNfsExportModel]] = Field(
        default=None, alias="NfsExports"
    )
    user_and_group_quotas: Optional[Sequence[OpenZFSUserOrGroupQuotaModel]] = Field(
        default=None, alias="UserAndGroupQuotas"
    )


class OpenZFSCreateRootVolumeConfigurationModel(BaseModel):
    record_size_ki_b: Optional[int] = Field(default=None, alias="RecordSizeKiB")
    data_compression_type: Optional[Literal["LZ4", "NONE", "ZSTD"]] = Field(
        default=None, alias="DataCompressionType"
    )
    nfs_exports: Optional[Sequence[OpenZFSNfsExportModel]] = Field(
        default=None, alias="NfsExports"
    )
    user_and_group_quotas: Optional[Sequence[OpenZFSUserOrGroupQuotaModel]] = Field(
        default=None, alias="UserAndGroupQuotas"
    )
    copy_tags_to_snapshots: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshots"
    )
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")


class OpenZFSVolumeConfigurationModel(BaseModel):
    parent_volume_id: Optional[str] = Field(default=None, alias="ParentVolumeId")
    volume_path: Optional[str] = Field(default=None, alias="VolumePath")
    storage_capacity_reservation_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityReservationGiB"
    )
    storage_capacity_quota_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityQuotaGiB"
    )
    record_size_ki_b: Optional[int] = Field(default=None, alias="RecordSizeKiB")
    data_compression_type: Optional[Literal["LZ4", "NONE", "ZSTD"]] = Field(
        default=None, alias="DataCompressionType"
    )
    copy_tags_to_snapshots: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshots"
    )
    origin_snapshot: Optional[OpenZFSOriginSnapshotConfigurationModel] = Field(
        default=None, alias="OriginSnapshot"
    )
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    nfs_exports: Optional[List[OpenZFSNfsExportModel]] = Field(
        default=None, alias="NfsExports"
    )
    user_and_group_quotas: Optional[List[OpenZFSUserOrGroupQuotaModel]] = Field(
        default=None, alias="UserAndGroupQuotas"
    )
    restore_to_snapshot: Optional[str] = Field(default=None, alias="RestoreToSnapshot")
    delete_intermediate_snaphots: Optional[bool] = Field(
        default=None, alias="DeleteIntermediateSnaphots"
    )
    delete_cloned_volumes: Optional[bool] = Field(
        default=None, alias="DeleteClonedVolumes"
    )


class UpdateOpenZFSVolumeConfigurationModel(BaseModel):
    storage_capacity_reservation_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityReservationGiB"
    )
    storage_capacity_quota_gi_b: Optional[int] = Field(
        default=None, alias="StorageCapacityQuotaGiB"
    )
    record_size_ki_b: Optional[int] = Field(default=None, alias="RecordSizeKiB")
    data_compression_type: Optional[Literal["LZ4", "NONE", "ZSTD"]] = Field(
        default=None, alias="DataCompressionType"
    )
    nfs_exports: Optional[Sequence[OpenZFSNfsExportModel]] = Field(
        default=None, alias="NfsExports"
    )
    user_and_group_quotas: Optional[Sequence[OpenZFSUserOrGroupQuotaModel]] = Field(
        default=None, alias="UserAndGroupQuotas"
    )
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")


class UpdateFileSystemRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="StorageCapacity")
    windows_configuration: Optional[UpdateFileSystemWindowsConfigurationModel] = Field(
        default=None, alias="WindowsConfiguration"
    )
    lustre_configuration: Optional[UpdateFileSystemLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    ontap_configuration: Optional[UpdateFileSystemOntapConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    open_zfs_configuration: Optional[UpdateFileSystemOpenZFSConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class UpdateStorageVirtualMachineRequestModel(BaseModel):
    storage_virtual_machine_id: str = Field(alias="StorageVirtualMachineId")
    active_directory_configuration: Optional[
        UpdateSvmActiveDirectoryConfigurationModel
    ] = Field(default=None, alias="ActiveDirectoryConfiguration")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    svm_admin_password: Optional[str] = Field(default=None, alias="SvmAdminPassword")


class StorageVirtualMachineModel(BaseModel):
    active_directory_configuration: Optional[
        SvmActiveDirectoryConfigurationModel
    ] = Field(default=None, alias="ActiveDirectoryConfiguration")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    endpoints: Optional[SvmEndpointsModel] = Field(default=None, alias="Endpoints")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    lifecycle: Optional[
        Literal["CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"]
    ] = Field(default=None, alias="Lifecycle")
    name: Optional[str] = Field(default=None, alias="Name")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    storage_virtual_machine_id: Optional[str] = Field(
        default=None, alias="StorageVirtualMachineId"
    )
    subtype: Optional[
        Literal["DEFAULT", "DP_DESTINATION", "SYNC_DESTINATION", "SYNC_SOURCE"]
    ] = Field(default=None, alias="Subtype")
    uuid: Optional[str] = Field(default=None, alias="UUID")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    lifecycle_transition_reason: Optional[LifecycleTransitionReasonModel] = Field(
        default=None, alias="LifecycleTransitionReason"
    )
    root_volume_security_style: Optional[Literal["MIXED", "NTFS", "UNIX"]] = Field(
        default=None, alias="RootVolumeSecurityStyle"
    )


class CreateDataRepositoryAssociationResponseModel(BaseModel):
    association: DataRepositoryAssociationModel = Field(alias="Association")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataRepositoryAssociationsResponseModel(BaseModel):
    associations: List[DataRepositoryAssociationModel] = Field(alias="Associations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataRepositoryAssociationResponseModel(BaseModel):
    association: DataRepositoryAssociationModel = Field(alias="Association")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileCacheResponseModel(BaseModel):
    file_cache: FileCacheCreatingModel = Field(alias="FileCache")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileCachesResponseModel(BaseModel):
    file_caches: List[FileCacheModel] = Field(alias="FileCaches")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFileCacheResponseModel(BaseModel):
    file_cache: FileCacheModel = Field(alias="FileCache")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FileSystemModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    file_system_type: Optional[
        Literal["LUSTRE", "ONTAP", "OPENZFS", "WINDOWS"]
    ] = Field(default=None, alias="FileSystemType")
    lifecycle: Optional[
        Literal[
            "AVAILABLE",
            "CREATING",
            "DELETING",
            "FAILED",
            "MISCONFIGURED",
            "MISCONFIGURED_UNAVAILABLE",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Lifecycle")
    failure_details: Optional[FileSystemFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="StorageCapacity")
    storage_type: Optional[Literal["HDD", "SSD"]] = Field(
        default=None, alias="StorageType"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    network_interface_ids: Optional[List[str]] = Field(
        default=None, alias="NetworkInterfaceIds"
    )
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    windows_configuration: Optional[WindowsFileSystemConfigurationModel] = Field(
        default=None, alias="WindowsConfiguration"
    )
    lustre_configuration: Optional[LustreFileSystemConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    administrative_actions: Optional[List[AdministrativeActionModel]] = Field(
        default=None, alias="AdministrativeActions"
    )
    ontap_configuration: Optional[OntapFileSystemConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    file_system_type_version: Optional[str] = Field(
        default=None, alias="FileSystemTypeVersion"
    )
    open_zfs_configuration: Optional[OpenZFSFileSystemConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class CreateVolumeRequestModel(BaseModel):
    volume_type: Literal["ONTAP", "OPENZFS"] = Field(alias="VolumeType")
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    ontap_configuration: Optional[CreateOntapVolumeConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    open_zfs_configuration: Optional[CreateOpenZFSVolumeConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class CreateFileSystemOpenZFSConfigurationModel(BaseModel):
    deployment_type: Literal["SINGLE_AZ_1", "SINGLE_AZ_2"] = Field(
        alias="DeploymentType"
    )
    throughput_capacity: int = Field(alias="ThroughputCapacity")
    automatic_backup_retention_days: Optional[int] = Field(
        default=None, alias="AutomaticBackupRetentionDays"
    )
    copy_tags_to_backups: Optional[bool] = Field(
        default=None, alias="CopyTagsToBackups"
    )
    copy_tags_to_volumes: Optional[bool] = Field(
        default=None, alias="CopyTagsToVolumes"
    )
    daily_automatic_backup_start_time: Optional[str] = Field(
        default=None, alias="DailyAutomaticBackupStartTime"
    )
    weekly_maintenance_start_time: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceStartTime"
    )
    disk_iops_configuration: Optional[DiskIopsConfigurationModel] = Field(
        default=None, alias="DiskIopsConfiguration"
    )
    root_volume_configuration: Optional[
        OpenZFSCreateRootVolumeConfigurationModel
    ] = Field(default=None, alias="RootVolumeConfiguration")


class VolumeModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    lifecycle: Optional[
        Literal[
            "AVAILABLE",
            "CREATED",
            "CREATING",
            "DELETING",
            "FAILED",
            "MISCONFIGURED",
            "PENDING",
        ]
    ] = Field(default=None, alias="Lifecycle")
    name: Optional[str] = Field(default=None, alias="Name")
    ontap_configuration: Optional[OntapVolumeConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    volume_type: Optional[Literal["ONTAP", "OPENZFS"]] = Field(
        default=None, alias="VolumeType"
    )
    lifecycle_transition_reason: Optional[LifecycleTransitionReasonModel] = Field(
        default=None, alias="LifecycleTransitionReason"
    )
    administrative_actions: Optional[List[AdministrativeActionModel]] = Field(
        default=None, alias="AdministrativeActions"
    )
    open_zfs_configuration: Optional[OpenZFSVolumeConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class UpdateVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    ontap_configuration: Optional[UpdateOntapVolumeConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    open_zfs_configuration: Optional[UpdateOpenZFSVolumeConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class CreateStorageVirtualMachineResponseModel(BaseModel):
    storage_virtual_machine: StorageVirtualMachineModel = Field(
        alias="StorageVirtualMachine"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStorageVirtualMachinesResponseModel(BaseModel):
    storage_virtual_machines: List[StorageVirtualMachineModel] = Field(
        alias="StorageVirtualMachines"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStorageVirtualMachineResponseModel(BaseModel):
    storage_virtual_machine: StorageVirtualMachineModel = Field(
        alias="StorageVirtualMachine"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileSystemFromBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    windows_configuration: Optional[CreateFileSystemWindowsConfigurationModel] = Field(
        default=None, alias="WindowsConfiguration"
    )
    lustre_configuration: Optional[CreateFileSystemLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    storage_type: Optional[Literal["HDD", "SSD"]] = Field(
        default=None, alias="StorageType"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    file_system_type_version: Optional[str] = Field(
        default=None, alias="FileSystemTypeVersion"
    )
    open_zfs_configuration: Optional[CreateFileSystemOpenZFSConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="StorageCapacity")


class CreateFileSystemRequestModel(BaseModel):
    file_system_type: Literal["LUSTRE", "ONTAP", "OPENZFS", "WINDOWS"] = Field(
        alias="FileSystemType"
    )
    storage_capacity: int = Field(alias="StorageCapacity")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    storage_type: Optional[Literal["HDD", "SSD"]] = Field(
        default=None, alias="StorageType"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    windows_configuration: Optional[CreateFileSystemWindowsConfigurationModel] = Field(
        default=None, alias="WindowsConfiguration"
    )
    lustre_configuration: Optional[CreateFileSystemLustreConfigurationModel] = Field(
        default=None, alias="LustreConfiguration"
    )
    ontap_configuration: Optional[CreateFileSystemOntapConfigurationModel] = Field(
        default=None, alias="OntapConfiguration"
    )
    file_system_type_version: Optional[str] = Field(
        default=None, alias="FileSystemTypeVersion"
    )
    open_zfs_configuration: Optional[CreateFileSystemOpenZFSConfigurationModel] = Field(
        default=None, alias="OpenZFSConfiguration"
    )


class AdministrativeActionModel(BaseModel):
    administrative_action_type: Optional[
        Literal[
            "FILE_SYSTEM_ALIAS_ASSOCIATION",
            "FILE_SYSTEM_ALIAS_DISASSOCIATION",
            "FILE_SYSTEM_UPDATE",
            "RELEASE_NFS_V3_LOCKS",
            "SNAPSHOT_UPDATE",
            "STORAGE_OPTIMIZATION",
            "VOLUME_RESTORE",
            "VOLUME_UPDATE",
        ]
    ] = Field(default=None, alias="AdministrativeActionType")
    progress_percent: Optional[int] = Field(default=None, alias="ProgressPercent")
    request_time: Optional[datetime] = Field(default=None, alias="RequestTime")
    status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "UPDATED_OPTIMIZING"]
    ] = Field(default=None, alias="Status")
    target_file_system_values: Optional[Dict[str, Any]] = Field(
        default=None, alias="TargetFileSystemValues"
    )
    failure_details: Optional[AdministrativeActionFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    target_volume_values: Optional[Dict[str, Any]] = Field(
        default=None, alias="TargetVolumeValues"
    )
    target_snapshot_values: Optional[Dict[str, Any]] = Field(
        default=None, alias="TargetSnapshotValues"
    )


class BackupModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    lifecycle: Literal[
        "AVAILABLE",
        "COPYING",
        "CREATING",
        "DELETED",
        "FAILED",
        "PENDING",
        "TRANSFERRING",
    ] = Field(alias="Lifecycle")
    type: Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"] = Field(alias="Type")
    creation_time: datetime = Field(alias="CreationTime")
    file_system: FileSystemModel = Field(alias="FileSystem")
    failure_details: Optional[BackupFailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    progress_percent: Optional[int] = Field(default=None, alias="ProgressPercent")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    directory_information: Optional[ActiveDirectoryBackupAttributesModel] = Field(
        default=None, alias="DirectoryInformation"
    )
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    source_backup_id: Optional[str] = Field(default=None, alias="SourceBackupId")
    source_backup_region: Optional[str] = Field(
        default=None, alias="SourceBackupRegion"
    )
    resource_type: Optional[Literal["FILE_SYSTEM", "VOLUME"]] = Field(
        default=None, alias="ResourceType"
    )
    volume: Optional[VolumeModel] = Field(default=None, alias="Volume")


class CreateVolumeFromBackupResponseModel(BaseModel):
    volume: VolumeModel = Field(alias="Volume")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVolumeResponseModel(BaseModel):
    volume: VolumeModel = Field(alias="Volume")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVolumesResponseModel(BaseModel):
    volumes: List[VolumeModel] = Field(alias="Volumes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVolumeResponseModel(BaseModel):
    volume: VolumeModel = Field(alias="Volume")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyBackupResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupsResponseModel(BaseModel):
    backups: List[BackupModel] = Field(alias="Backups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
