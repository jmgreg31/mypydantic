# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class PosixUserModel(BaseModel):
    uid: int = Field(alias="Uid")
    gid: int = Field(alias="Gid")
    secondary_gids: Optional[Sequence[int]] = Field(default=None, alias="SecondaryGids")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class BackupPolicyModel(BaseModel):
    status: Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"] = Field(
        alias="Status"
    )


class CreateMountTargetRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    subnet_id: str = Field(alias="SubnetId")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )


class DestinationToCreateModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    availability_zone_name: Optional[str] = Field(
        default=None, alias="AvailabilityZoneName"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class CreationInfoModel(BaseModel):
    owner_uid: int = Field(alias="OwnerUid")
    owner_gid: int = Field(alias="OwnerGid")
    permissions: str = Field(alias="Permissions")


class DeleteAccessPointRequestModel(BaseModel):
    access_point_id: str = Field(alias="AccessPointId")


class DeleteFileSystemPolicyRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")


class DeleteFileSystemRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")


class DeleteMountTargetRequestModel(BaseModel):
    mount_target_id: str = Field(alias="MountTargetId")


class DeleteReplicationConfigurationRequestModel(BaseModel):
    source_file_system_id: str = Field(alias="SourceFileSystemId")


class DeleteTagsRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DescribeAccessPointsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")


class DescribeAccountPreferencesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResourceIdPreferenceModel(BaseModel):
    resource_id_type: Optional[Literal["LONG_ID", "SHORT_ID"]] = Field(
        default=None, alias="ResourceIdType"
    )
    resources: Optional[List[Literal["FILE_SYSTEM", "MOUNT_TARGET"]]] = Field(
        default=None, alias="Resources"
    )


class DescribeBackupPolicyRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")


class DescribeFileSystemPolicyRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeFileSystemsRequestModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")
    creation_token: Optional[str] = Field(default=None, alias="CreationToken")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")


class DescribeLifecycleConfigurationRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")


class DescribeMountTargetSecurityGroupsRequestModel(BaseModel):
    mount_target_id: str = Field(alias="MountTargetId")


class DescribeMountTargetsRequestModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    mount_target_id: Optional[str] = Field(default=None, alias="MountTargetId")
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")


class MountTargetDescriptionModel(BaseModel):
    mount_target_id: str = Field(alias="MountTargetId")
    file_system_id: str = Field(alias="FileSystemId")
    subnet_id: str = Field(alias="SubnetId")
    life_cycle_state: Literal[
        "available", "creating", "deleted", "deleting", "error", "updating"
    ] = Field(alias="LifeCycleState")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    availability_zone_id: Optional[str] = Field(
        default=None, alias="AvailabilityZoneId"
    )
    availability_zone_name: Optional[str] = Field(
        default=None, alias="AvailabilityZoneName"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class DescribeReplicationConfigurationsRequestModel(BaseModel):
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeTagsRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DestinationModel(BaseModel):
    status: Literal["DELETING", "ENABLED", "ENABLING", "ERROR"] = Field(alias="Status")
    file_system_id: str = Field(alias="FileSystemId")
    region: str = Field(alias="Region")
    last_replicated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastReplicatedTimestamp"
    )


class FileSystemSizeModel(BaseModel):
    value: int = Field(alias="Value")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    value_in_ia: Optional[int] = Field(default=None, alias="ValueInIA")
    value_in_standard: Optional[int] = Field(default=None, alias="ValueInStandard")


class LifecyclePolicyModel(BaseModel):
    transition_to_ia: Optional[
        Literal[
            "AFTER_14_DAYS",
            "AFTER_1_DAY",
            "AFTER_30_DAYS",
            "AFTER_60_DAYS",
            "AFTER_7_DAYS",
            "AFTER_90_DAYS",
        ]
    ] = Field(default=None, alias="TransitionToIA")
    transition_to_primary_storage_class: Optional[Literal["AFTER_1_ACCESS"]] = Field(
        default=None, alias="TransitionToPrimaryStorageClass"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ModifyMountTargetSecurityGroupsRequestModel(BaseModel):
    mount_target_id: str = Field(alias="MountTargetId")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )


class PutAccountPreferencesRequestModel(BaseModel):
    resource_id_type: Literal["LONG_ID", "SHORT_ID"] = Field(alias="ResourceIdType")


class PutFileSystemPolicyRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    policy: str = Field(alias="Policy")
    bypass_policy_lockout_safety_check: Optional[bool] = Field(
        default=None, alias="BypassPolicyLockoutSafetyCheck"
    )


class UntagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFileSystemRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    throughput_mode: Optional[Literal["bursting", "elastic", "provisioned"]] = Field(
        default=None, alias="ThroughputMode"
    )
    provisioned_throughput_in_mibps: Optional[float] = Field(
        default=None, alias="ProvisionedThroughputInMibps"
    )


class DescribeMountTargetSecurityGroupsResponseModel(BaseModel):
    security_groups: List[str] = Field(alias="SecurityGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FileSystemPolicyDescriptionModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MountTargetDescriptionResponseMetadataModel(BaseModel):
    owner_id: str = Field(alias="OwnerId")
    mount_target_id: str = Field(alias="MountTargetId")
    file_system_id: str = Field(alias="FileSystemId")
    subnet_id: str = Field(alias="SubnetId")
    life_cycle_state: Literal[
        "available", "creating", "deleted", "deleting", "error", "updating"
    ] = Field(alias="LifeCycleState")
    ip_address: str = Field(alias="IpAddress")
    network_interface_id: str = Field(alias="NetworkInterfaceId")
    availability_zone_id: str = Field(alias="AvailabilityZoneId")
    availability_zone_name: str = Field(alias="AvailabilityZoneName")
    vpc_id: str = Field(alias="VpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFileSystemRequestModel(BaseModel):
    creation_token: str = Field(alias="CreationToken")
    performance_mode: Optional[Literal["generalPurpose", "maxIO"]] = Field(
        default=None, alias="PerformanceMode"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    throughput_mode: Optional[Literal["bursting", "elastic", "provisioned"]] = Field(
        default=None, alias="ThroughputMode"
    )
    provisioned_throughput_in_mibps: Optional[float] = Field(
        default=None, alias="ProvisionedThroughputInMibps"
    )
    availability_zone_name: Optional[str] = Field(
        default=None, alias="AvailabilityZoneName"
    )
    backup: Optional[bool] = Field(default=None, alias="Backup")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTagsRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DescribeTagsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    tags: List[TagModel] = Field(alias="Tags")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class BackupPolicyDescriptionModel(BaseModel):
    backup_policy: BackupPolicyModel = Field(alias="BackupPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBackupPolicyRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    backup_policy: BackupPolicyModel = Field(alias="BackupPolicy")


class CreateReplicationConfigurationRequestModel(BaseModel):
    source_file_system_id: str = Field(alias="SourceFileSystemId")
    destinations: Sequence[DestinationToCreateModel] = Field(alias="Destinations")


class RootDirectoryModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    creation_info: Optional[CreationInfoModel] = Field(
        default=None, alias="CreationInfo"
    )


class DescribeAccountPreferencesResponseModel(BaseModel):
    resource_id_preference: ResourceIdPreferenceModel = Field(
        alias="ResourceIdPreference"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccountPreferencesResponseModel(BaseModel):
    resource_id_preference: ResourceIdPreferenceModel = Field(
        alias="ResourceIdPreference"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileSystemsRequestDescribeFileSystemsPaginateModel(BaseModel):
    creation_token: Optional[str] = Field(default=None, alias="CreationToken")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMountTargetsRequestDescribeMountTargetsPaginateModel(BaseModel):
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    mount_target_id: Optional[str] = Field(default=None, alias="MountTargetId")
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTagsRequestDescribeTagsPaginateModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMountTargetsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    mount_targets: List[MountTargetDescriptionModel] = Field(alias="MountTargets")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationConfigurationDescriptionResponseMetadataModel(BaseModel):
    source_file_system_id: str = Field(alias="SourceFileSystemId")
    source_file_system_region: str = Field(alias="SourceFileSystemRegion")
    source_file_system_arn: str = Field(alias="SourceFileSystemArn")
    original_source_file_system_arn: str = Field(alias="OriginalSourceFileSystemArn")
    creation_time: datetime = Field(alias="CreationTime")
    destinations: List[DestinationModel] = Field(alias="Destinations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationConfigurationDescriptionModel(BaseModel):
    source_file_system_id: str = Field(alias="SourceFileSystemId")
    source_file_system_region: str = Field(alias="SourceFileSystemRegion")
    source_file_system_arn: str = Field(alias="SourceFileSystemArn")
    original_source_file_system_arn: str = Field(alias="OriginalSourceFileSystemArn")
    creation_time: datetime = Field(alias="CreationTime")
    destinations: List[DestinationModel] = Field(alias="Destinations")


class FileSystemDescriptionResponseMetadataModel(BaseModel):
    owner_id: str = Field(alias="OwnerId")
    creation_token: str = Field(alias="CreationToken")
    file_system_id: str = Field(alias="FileSystemId")
    file_system_arn: str = Field(alias="FileSystemArn")
    creation_time: datetime = Field(alias="CreationTime")
    life_cycle_state: Literal[
        "available", "creating", "deleted", "deleting", "error", "updating"
    ] = Field(alias="LifeCycleState")
    name: str = Field(alias="Name")
    number_of_mount_targets: int = Field(alias="NumberOfMountTargets")
    size_in_bytes: FileSystemSizeModel = Field(alias="SizeInBytes")
    performance_mode: Literal["generalPurpose", "maxIO"] = Field(
        alias="PerformanceMode"
    )
    encrypted: bool = Field(alias="Encrypted")
    kms_key_id: str = Field(alias="KmsKeyId")
    throughput_mode: Literal["bursting", "elastic", "provisioned"] = Field(
        alias="ThroughputMode"
    )
    provisioned_throughput_in_mibps: float = Field(alias="ProvisionedThroughputInMibps")
    availability_zone_name: str = Field(alias="AvailabilityZoneName")
    availability_zone_id: str = Field(alias="AvailabilityZoneId")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FileSystemDescriptionModel(BaseModel):
    owner_id: str = Field(alias="OwnerId")
    creation_token: str = Field(alias="CreationToken")
    file_system_id: str = Field(alias="FileSystemId")
    creation_time: datetime = Field(alias="CreationTime")
    life_cycle_state: Literal[
        "available", "creating", "deleted", "deleting", "error", "updating"
    ] = Field(alias="LifeCycleState")
    number_of_mount_targets: int = Field(alias="NumberOfMountTargets")
    size_in_bytes: FileSystemSizeModel = Field(alias="SizeInBytes")
    performance_mode: Literal["generalPurpose", "maxIO"] = Field(
        alias="PerformanceMode"
    )
    tags: List[TagModel] = Field(alias="Tags")
    file_system_arn: Optional[str] = Field(default=None, alias="FileSystemArn")
    name: Optional[str] = Field(default=None, alias="Name")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    throughput_mode: Optional[Literal["bursting", "elastic", "provisioned"]] = Field(
        default=None, alias="ThroughputMode"
    )
    provisioned_throughput_in_mibps: Optional[float] = Field(
        default=None, alias="ProvisionedThroughputInMibps"
    )
    availability_zone_name: Optional[str] = Field(
        default=None, alias="AvailabilityZoneName"
    )
    availability_zone_id: Optional[str] = Field(
        default=None, alias="AvailabilityZoneId"
    )


class LifecycleConfigurationDescriptionModel(BaseModel):
    lifecycle_policies: List[LifecyclePolicyModel] = Field(alias="LifecyclePolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLifecycleConfigurationRequestModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    lifecycle_policies: Sequence[LifecyclePolicyModel] = Field(
        alias="LifecyclePolicies"
    )


class AccessPointDescriptionResponseMetadataModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    name: str = Field(alias="Name")
    tags: List[TagModel] = Field(alias="Tags")
    access_point_id: str = Field(alias="AccessPointId")
    access_point_arn: str = Field(alias="AccessPointArn")
    file_system_id: str = Field(alias="FileSystemId")
    posix_user: PosixUserModel = Field(alias="PosixUser")
    root_directory: RootDirectoryModel = Field(alias="RootDirectory")
    owner_id: str = Field(alias="OwnerId")
    life_cycle_state: Literal[
        "available", "creating", "deleted", "deleting", "error", "updating"
    ] = Field(alias="LifeCycleState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessPointDescriptionModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")
    access_point_arn: Optional[str] = Field(default=None, alias="AccessPointArn")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    posix_user: Optional[PosixUserModel] = Field(default=None, alias="PosixUser")
    root_directory: Optional[RootDirectoryModel] = Field(
        default=None, alias="RootDirectory"
    )
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    life_cycle_state: Optional[
        Literal["available", "creating", "deleted", "deleting", "error", "updating"]
    ] = Field(default=None, alias="LifeCycleState")


class CreateAccessPointRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    file_system_id: str = Field(alias="FileSystemId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    posix_user: Optional[PosixUserModel] = Field(default=None, alias="PosixUser")
    root_directory: Optional[RootDirectoryModel] = Field(
        default=None, alias="RootDirectory"
    )


class DescribeReplicationConfigurationsResponseModel(BaseModel):
    replications: List[ReplicationConfigurationDescriptionModel] = Field(
        alias="Replications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileSystemsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    file_systems: List[FileSystemDescriptionModel] = Field(alias="FileSystems")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccessPointsResponseModel(BaseModel):
    access_points: List[AccessPointDescriptionModel] = Field(alias="AccessPoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
