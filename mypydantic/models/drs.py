# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountID")


class CPUModel(BaseModel):
    cores: Optional[int] = Field(default=None, alias="cores")
    model_name: Optional[str] = Field(default=None, alias="modelName")


class ConversionPropertiesModel(BaseModel):
    data_timestamp: Optional[str] = Field(default=None, alias="dataTimestamp")
    force_uefi: Optional[bool] = Field(default=None, alias="forceUefi")
    root_volume_name: Optional[str] = Field(default=None, alias="rootVolumeName")
    volume_to_conversion_map: Optional[Dict[str, Dict[str, str]]] = Field(
        default=None, alias="volumeToConversionMap"
    )
    volume_to_volume_size: Optional[Dict[str, int]] = Field(
        default=None, alias="volumeToVolumeSize"
    )


class CreateExtendedSourceServerRequestModel(BaseModel):
    source_server_arn: str = Field(alias="sourceServerArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PITPolicyRuleModel(BaseModel):
    interval: int = Field(alias="interval")
    retention_duration: int = Field(alias="retentionDuration")
    units: Literal["DAY", "HOUR", "MINUTE"] = Field(alias="units")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    rule_id: Optional[int] = Field(default=None, alias="ruleID")


class DataReplicationErrorModel(BaseModel):
    error: Optional[
        Literal[
            "AGENT_NOT_SEEN",
            "FAILED_TO_ATTACH_STAGING_DISKS",
            "FAILED_TO_AUTHENTICATE_WITH_SERVICE",
            "FAILED_TO_BOOT_REPLICATION_SERVER",
            "FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER",
            "FAILED_TO_CREATE_SECURITY_GROUP",
            "FAILED_TO_CREATE_STAGING_DISKS",
            "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE",
            "FAILED_TO_LAUNCH_REPLICATION_SERVER",
            "FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT",
            "FAILED_TO_START_DATA_TRANSFER",
            "NOT_CONVERGING",
            "SNAPSHOTS_FAILURE",
            "UNSTABLE_NETWORK",
        ]
    ] = Field(default=None, alias="error")
    raw_error: Optional[str] = Field(default=None, alias="rawError")


class DataReplicationInfoReplicatedDiskModel(BaseModel):
    backlogged_storage_bytes: Optional[int] = Field(
        default=None, alias="backloggedStorageBytes"
    )
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    replicated_storage_bytes: Optional[int] = Field(
        default=None, alias="replicatedStorageBytes"
    )
    rescanned_storage_bytes: Optional[int] = Field(
        default=None, alias="rescannedStorageBytes"
    )
    total_storage_bytes: Optional[int] = Field(default=None, alias="totalStorageBytes")


class DataReplicationInitiationStepModel(BaseModel):
    name: Optional[
        Literal[
            "ATTACH_STAGING_DISKS",
            "AUTHENTICATE_WITH_SERVICE",
            "BOOT_REPLICATION_SERVER",
            "CONNECT_AGENT_TO_REPLICATION_SERVER",
            "CREATE_SECURITY_GROUP",
            "CREATE_STAGING_DISKS",
            "DOWNLOAD_REPLICATION_SOFTWARE",
            "LAUNCH_REPLICATION_SERVER",
            "PAIR_REPLICATION_SERVER_WITH_AGENT",
            "START_DATA_TRANSFER",
            "WAIT",
        ]
    ] = Field(default=None, alias="name")
    status: Optional[
        Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SKIPPED", "SUCCEEDED"]
    ] = Field(default=None, alias="status")


class DeleteJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobID")


class DeleteRecoveryInstanceRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")


class DeleteReplicationConfigurationTemplateRequestModel(BaseModel):
    replication_configuration_template_id: str = Field(
        alias="replicationConfigurationTemplateID"
    )


class DeleteSourceServerRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeJobLogItemsRequestModel(BaseModel):
    job_id: str = Field(alias="jobID")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeJobsRequestFiltersModel(BaseModel):
    from_date: Optional[str] = Field(default=None, alias="fromDate")
    job_ids: Optional[Sequence[str]] = Field(default=None, alias="jobIDs")
    to_date: Optional[str] = Field(default=None, alias="toDate")


class DescribeRecoveryInstancesRequestFiltersModel(BaseModel):
    recovery_instance_ids: Optional[Sequence[str]] = Field(
        default=None, alias="recoveryInstanceIDs"
    )
    source_server_ids: Optional[Sequence[str]] = Field(
        default=None, alias="sourceServerIDs"
    )


class DescribeRecoverySnapshotsRequestFiltersModel(BaseModel):
    from_date_time: Optional[str] = Field(default=None, alias="fromDateTime")
    to_date_time: Optional[str] = Field(default=None, alias="toDateTime")


class RecoverySnapshotModel(BaseModel):
    expected_timestamp: str = Field(alias="expectedTimestamp")
    snapshot_id: str = Field(alias="snapshotID")
    source_server_id: str = Field(alias="sourceServerID")
    ebs_snapshots: Optional[List[str]] = Field(default=None, alias="ebsSnapshots")
    timestamp: Optional[str] = Field(default=None, alias="timestamp")


class DescribeReplicationConfigurationTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    replication_configuration_template_ids: Optional[Sequence[str]] = Field(
        default=None, alias="replicationConfigurationTemplateIDs"
    )


class DescribeSourceServersRequestFiltersModel(BaseModel):
    hardware_id: Optional[str] = Field(default=None, alias="hardwareId")
    source_server_ids: Optional[Sequence[str]] = Field(
        default=None, alias="sourceServerIDs"
    )
    staging_account_ids: Optional[Sequence[str]] = Field(
        default=None, alias="stagingAccountIDs"
    )


class DisconnectRecoveryInstanceRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")


class DisconnectSourceServerRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class DiskModel(BaseModel):
    bytes: Optional[int] = Field(default=None, alias="bytes")
    device_name: Optional[str] = Field(default=None, alias="deviceName")


class GetFailbackReplicationConfigurationRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")


class GetLaunchConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class GetReplicationConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class IdentificationHintsModel(BaseModel):
    aws_instance_id: Optional[str] = Field(default=None, alias="awsInstanceID")
    fqdn: Optional[str] = Field(default=None, alias="fqdn")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    vm_ware_uuid: Optional[str] = Field(default=None, alias="vmWareUuid")


class ParticipatingServerModel(BaseModel):
    launch_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
    ] = Field(default=None, alias="launchStatus")
    recovery_instance_id: Optional[str] = Field(
        default=None, alias="recoveryInstanceID"
    )
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")


class LicensingModel(BaseModel):
    os_byol: Optional[bool] = Field(default=None, alias="osByol")


class LifeCycleLastLaunchInitiatedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")
    job_id: Optional[str] = Field(default=None, alias="jobID")
    type: Optional[Literal["DRILL", "RECOVERY"]] = Field(default=None, alias="type")


class ListExtensibleSourceServersRequestModel(BaseModel):
    staging_account_id: str = Field(alias="stagingAccountID")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StagingSourceServerModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListStagingAccountsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class NetworkInterfaceModel(BaseModel):
    ips: Optional[List[str]] = Field(default=None, alias="ips")
    is_primary: Optional[bool] = Field(default=None, alias="isPrimary")
    mac_address: Optional[str] = Field(default=None, alias="macAddress")


class OSModel(BaseModel):
    full_string: Optional[str] = Field(default=None, alias="fullString")


class RecoveryInstanceDataReplicationErrorModel(BaseModel):
    error: Optional[
        Literal[
            "AGENT_NOT_SEEN",
            "FAILBACK_CLIENT_NOT_SEEN",
            "FAILED_GETTING_REPLICATION_STATE",
            "FAILED_TO_ATTACH_STAGING_DISKS",
            "FAILED_TO_AUTHENTICATE_WITH_SERVICE",
            "FAILED_TO_BOOT_REPLICATION_SERVER",
            "FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE",
            "FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER",
            "FAILED_TO_CREATE_SECURITY_GROUP",
            "FAILED_TO_CREATE_STAGING_DISKS",
            "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE",
            "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT",
            "FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION",
            "FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION",
            "FAILED_TO_LAUNCH_REPLICATION_SERVER",
            "FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE",
            "FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT",
            "FAILED_TO_START_DATA_TRANSFER",
            "NOT_CONVERGING",
            "SNAPSHOTS_FAILURE",
            "UNSTABLE_NETWORK",
        ]
    ] = Field(default=None, alias="error")
    raw_error: Optional[str] = Field(default=None, alias="rawError")


class RecoveryInstanceDataReplicationInfoReplicatedDiskModel(BaseModel):
    backlogged_storage_bytes: Optional[int] = Field(
        default=None, alias="backloggedStorageBytes"
    )
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    replicated_storage_bytes: Optional[int] = Field(
        default=None, alias="replicatedStorageBytes"
    )
    rescanned_storage_bytes: Optional[int] = Field(
        default=None, alias="rescannedStorageBytes"
    )
    total_storage_bytes: Optional[int] = Field(default=None, alias="totalStorageBytes")


class RecoveryInstanceDataReplicationInitiationStepModel(BaseModel):
    name: Optional[
        Literal[
            "ATTACH_STAGING_DISKS",
            "AUTHENTICATE_WITH_SERVICE",
            "BOOT_REPLICATION_SERVER",
            "COMPLETE_VOLUME_MAPPING",
            "CONFIGURE_REPLICATION_SOFTWARE",
            "CONNECT_AGENT_TO_REPLICATION_SERVER",
            "CREATE_SECURITY_GROUP",
            "CREATE_STAGING_DISKS",
            "DOWNLOAD_REPLICATION_SOFTWARE",
            "DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT",
            "ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION",
            "ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION",
            "LAUNCH_REPLICATION_SERVER",
            "LINK_FAILBACK_CLIENT_WITH_RECOVERY_INSTANCE",
            "PAIR_AGENT_WITH_REPLICATION_SOFTWARE",
            "PAIR_REPLICATION_SERVER_WITH_AGENT",
            "START_DATA_TRANSFER",
            "WAIT",
        ]
    ] = Field(default=None, alias="name")
    status: Optional[
        Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SKIPPED", "SUCCEEDED"]
    ] = Field(default=None, alias="status")


class RecoveryInstanceDiskModel(BaseModel):
    bytes: Optional[int] = Field(default=None, alias="bytes")
    ebs_volume_id: Optional[str] = Field(default=None, alias="ebsVolumeID")
    internal_device_name: Optional[str] = Field(
        default=None, alias="internalDeviceName"
    )


class RecoveryInstanceFailbackModel(BaseModel):
    agent_last_seen_by_service_date_time: Optional[str] = Field(
        default=None, alias="agentLastSeenByServiceDateTime"
    )
    elapsed_replication_duration: Optional[str] = Field(
        default=None, alias="elapsedReplicationDuration"
    )
    failback_client_id: Optional[str] = Field(default=None, alias="failbackClientID")
    failback_client_last_seen_by_service_date_time: Optional[str] = Field(
        default=None, alias="failbackClientLastSeenByServiceDateTime"
    )
    failback_initiation_time: Optional[str] = Field(
        default=None, alias="failbackInitiationTime"
    )
    failback_job_id: Optional[str] = Field(default=None, alias="failbackJobID")
    failback_launch_type: Optional[Literal["DRILL", "RECOVERY"]] = Field(
        default=None, alias="failbackLaunchType"
    )
    failback_to_original_server: Optional[bool] = Field(
        default=None, alias="failbackToOriginalServer"
    )
    first_byte_date_time: Optional[str] = Field(default=None, alias="firstByteDateTime")
    state: Optional[
        Literal[
            "FAILBACK_COMPLETED",
            "FAILBACK_ERROR",
            "FAILBACK_IN_PROGRESS",
            "FAILBACK_LAUNCH_STATE_NOT_AVAILABLE",
            "FAILBACK_NOT_READY_FOR_LAUNCH",
            "FAILBACK_NOT_STARTED",
            "FAILBACK_READY_FOR_LAUNCH",
        ]
    ] = Field(default=None, alias="state")


class ReplicationConfigurationReplicatedDiskModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    iops: Optional[int] = Field(default=None, alias="iops")
    is_boot_disk: Optional[bool] = Field(default=None, alias="isBootDisk")
    optimized_staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "IO1", "SC1", "ST1", "STANDARD"]
    ] = Field(default=None, alias="optimizedStagingDiskType")
    staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "IO1", "SC1", "ST1", "STANDARD"]
    ] = Field(default=None, alias="stagingDiskType")
    throughput: Optional[int] = Field(default=None, alias="throughput")


class RetryDataReplicationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class ReverseReplicationRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")


class SourceCloudPropertiesModel(BaseModel):
    origin_account_id: Optional[str] = Field(default=None, alias="originAccountID")
    origin_availability_zone: Optional[str] = Field(
        default=None, alias="originAvailabilityZone"
    )
    origin_region: Optional[str] = Field(default=None, alias="originRegion")


class StagingAreaModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    staging_account_id: Optional[str] = Field(default=None, alias="stagingAccountID")
    staging_source_server_arn: Optional[str] = Field(
        default=None, alias="stagingSourceServerArn"
    )
    status: Optional[Literal["EXTENDED", "EXTENSION_ERROR", "NOT_EXTENDED"]] = Field(
        default=None, alias="status"
    )


class StartFailbackLaunchRequestModel(BaseModel):
    recovery_instance_ids: Sequence[str] = Field(alias="recoveryInstanceIDs")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StartRecoveryRequestSourceServerModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    recovery_snapshot_id: Optional[str] = Field(
        default=None, alias="recoverySnapshotID"
    )


class StartReplicationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class StopFailbackRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")


class StopReplicationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TerminateRecoveryInstancesRequestModel(BaseModel):
    recovery_instance_ids: Sequence[str] = Field(alias="recoveryInstanceIDs")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateFailbackReplicationConfigurationRequestModel(BaseModel):
    recovery_instance_id: str = Field(alias="recoveryInstanceID")
    bandwidth_throttling: Optional[int] = Field(
        default=None, alias="bandwidthThrottling"
    )
    name: Optional[str] = Field(default=None, alias="name")
    use_private_ip: Optional[bool] = Field(default=None, alias="usePrivateIP")


class JobLogEventDataModel(BaseModel):
    conversion_properties: Optional[ConversionPropertiesModel] = Field(
        default=None, alias="conversionProperties"
    )
    conversion_server_id: Optional[str] = Field(
        default=None, alias="conversionServerID"
    )
    raw_error: Optional[str] = Field(default=None, alias="rawError")
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")
    target_instance_id: Optional[str] = Field(default=None, alias="targetInstanceID")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFailbackReplicationConfigurationResponseModel(BaseModel):
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    name: str = Field(alias="name")
    recovery_instance_id: str = Field(alias="recoveryInstanceID")
    use_private_ip: bool = Field(alias="usePrivateIP")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStagingAccountsResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="accounts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReverseReplicationResponseModel(BaseModel):
    reversed_direction_source_server_arn: str = Field(
        alias="reversedDirectionSourceServerArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReplicationConfigurationTemplateRequestModel(BaseModel):
    associate_default_security_group: bool = Field(
        alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    create_public_ip: bool = Field(alias="createPublicIP")
    data_plane_routing: Literal["PRIVATE_IP", "PUBLIC_IP"] = Field(
        alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Literal["AUTO", "GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
    pit_policy: Sequence[PITPolicyRuleModel] = Field(alias="pitPolicy")
    replication_server_instance_type: str = Field(alias="replicationServerInstanceType")
    replication_servers_security_groups_ids: Sequence[str] = Field(
        alias="replicationServersSecurityGroupsIDs"
    )
    staging_area_subnet_id: str = Field(alias="stagingAreaSubnetId")
    staging_area_tags: Mapping[str, str] = Field(alias="stagingAreaTags")
    use_dedicated_replication_server: bool = Field(
        alias="useDedicatedReplicationServer"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ReplicationConfigurationTemplateResponseMetadataModel(BaseModel):
    arn: str = Field(alias="arn")
    associate_default_security_group: bool = Field(
        alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    create_public_ip: bool = Field(alias="createPublicIP")
    data_plane_routing: Literal["PRIVATE_IP", "PUBLIC_IP"] = Field(
        alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Literal["AUTO", "GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
    ebs_encryption_key_arn: str = Field(alias="ebsEncryptionKeyArn")
    pit_policy: List[PITPolicyRuleModel] = Field(alias="pitPolicy")
    replication_configuration_template_id: str = Field(
        alias="replicationConfigurationTemplateID"
    )
    replication_server_instance_type: str = Field(alias="replicationServerInstanceType")
    replication_servers_security_groups_ids: List[str] = Field(
        alias="replicationServersSecurityGroupsIDs"
    )
    staging_area_subnet_id: str = Field(alias="stagingAreaSubnetId")
    staging_area_tags: Dict[str, str] = Field(alias="stagingAreaTags")
    tags: Dict[str, str] = Field(alias="tags")
    use_dedicated_replication_server: bool = Field(
        alias="useDedicatedReplicationServer"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationConfigurationTemplateModel(BaseModel):
    replication_configuration_template_id: str = Field(
        alias="replicationConfigurationTemplateID"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    associate_default_security_group: Optional[bool] = Field(
        default=None, alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: Optional[int] = Field(
        default=None, alias="bandwidthThrottling"
    )
    create_public_ip: Optional[bool] = Field(default=None, alias="createPublicIP")
    data_plane_routing: Optional[Literal["PRIVATE_IP", "PUBLIC_IP"]] = Field(
        default=None, alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "ST1"]
    ] = Field(default=None, alias="defaultLargeStagingDiskType")
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
    )
    pit_policy: Optional[List[PITPolicyRuleModel]] = Field(
        default=None, alias="pitPolicy"
    )
    replication_server_instance_type: Optional[str] = Field(
        default=None, alias="replicationServerInstanceType"
    )
    replication_servers_security_groups_ids: Optional[List[str]] = Field(
        default=None, alias="replicationServersSecurityGroupsIDs"
    )
    staging_area_subnet_id: Optional[str] = Field(
        default=None, alias="stagingAreaSubnetId"
    )
    staging_area_tags: Optional[Dict[str, str]] = Field(
        default=None, alias="stagingAreaTags"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    use_dedicated_replication_server: Optional[bool] = Field(
        default=None, alias="useDedicatedReplicationServer"
    )


class UpdateReplicationConfigurationTemplateRequestModel(BaseModel):
    replication_configuration_template_id: str = Field(
        alias="replicationConfigurationTemplateID"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    associate_default_security_group: Optional[bool] = Field(
        default=None, alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: Optional[int] = Field(
        default=None, alias="bandwidthThrottling"
    )
    create_public_ip: Optional[bool] = Field(default=None, alias="createPublicIP")
    data_plane_routing: Optional[Literal["PRIVATE_IP", "PUBLIC_IP"]] = Field(
        default=None, alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "ST1"]
    ] = Field(default=None, alias="defaultLargeStagingDiskType")
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
    )
    pit_policy: Optional[Sequence[PITPolicyRuleModel]] = Field(
        default=None, alias="pitPolicy"
    )
    replication_server_instance_type: Optional[str] = Field(
        default=None, alias="replicationServerInstanceType"
    )
    replication_servers_security_groups_ids: Optional[Sequence[str]] = Field(
        default=None, alias="replicationServersSecurityGroupsIDs"
    )
    staging_area_subnet_id: Optional[str] = Field(
        default=None, alias="stagingAreaSubnetId"
    )
    staging_area_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="stagingAreaTags"
    )
    use_dedicated_replication_server: Optional[bool] = Field(
        default=None, alias="useDedicatedReplicationServer"
    )


class DataReplicationInitiationModel(BaseModel):
    next_attempt_date_time: Optional[str] = Field(
        default=None, alias="nextAttemptDateTime"
    )
    start_date_time: Optional[str] = Field(default=None, alias="startDateTime")
    steps: Optional[List[DataReplicationInitiationStepModel]] = Field(
        default=None, alias="steps"
    )


class DescribeJobLogItemsRequestDescribeJobLogItemsPaginateModel(BaseModel):
    job_id: str = Field(alias="jobID")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateModel(
    BaseModel
):
    replication_configuration_template_ids: Optional[Sequence[str]] = Field(
        default=None, alias="replicationConfigurationTemplateIDs"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExtensibleSourceServersRequestListExtensibleSourceServersPaginateModel(
    BaseModel
):
    staging_account_id: str = Field(alias="stagingAccountID")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStagingAccountsRequestListStagingAccountsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeJobsRequestDescribeJobsPaginateModel(BaseModel):
    filters: Optional[DescribeJobsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeJobsRequestModel(BaseModel):
    filters: Optional[DescribeJobsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeRecoveryInstancesRequestDescribeRecoveryInstancesPaginateModel(BaseModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRecoveryInstancesRequestModel(BaseModel):
    filters: Optional[DescribeRecoveryInstancesRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeRecoverySnapshotsRequestDescribeRecoverySnapshotsPaginateModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    order: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="order")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRecoverySnapshotsRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    filters: Optional[DescribeRecoverySnapshotsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    order: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="order")


class DescribeRecoverySnapshotsResponseModel(BaseModel):
    items: List[RecoverySnapshotModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSourceServersRequestDescribeSourceServersPaginateModel(BaseModel):
    filters: Optional[DescribeSourceServersRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSourceServersRequestModel(BaseModel):
    filters: Optional[DescribeSourceServersRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class JobModel(BaseModel):
    job_id: str = Field(alias="jobID")
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_date_time: Optional[str] = Field(default=None, alias="creationDateTime")
    end_date_time: Optional[str] = Field(default=None, alias="endDateTime")
    initiated_by: Optional[
        Literal[
            "DIAGNOSTIC",
            "FAILBACK",
            "START_DRILL",
            "START_RECOVERY",
            "TARGET_ACCOUNT",
            "TERMINATE_RECOVERY_INSTANCES",
        ]
    ] = Field(default=None, alias="initiatedBy")
    participating_servers: Optional[List[ParticipatingServerModel]] = Field(
        default=None, alias="participatingServers"
    )
    status: Optional[Literal["COMPLETED", "PENDING", "STARTED"]] = Field(
        default=None, alias="status"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[Literal["CREATE_CONVERTED_SNAPSHOT", "LAUNCH", "TERMINATE"]] = Field(
        default=None, alias="type"
    )


class LaunchConfigurationModel(BaseModel):
    copy_private_ip: bool = Field(alias="copyPrivateIp")
    copy_tags: bool = Field(alias="copyTags")
    ec2_launch_template_id: str = Field(alias="ec2LaunchTemplateID")
    launch_disposition: Literal["STARTED", "STOPPED"] = Field(alias="launchDisposition")
    licensing: LicensingModel = Field(alias="licensing")
    name: str = Field(alias="name")
    source_server_id: str = Field(alias="sourceServerID")
    target_instance_type_right_sizing_method: Literal["BASIC", "NONE"] = Field(
        alias="targetInstanceTypeRightSizingMethod"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLaunchConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    copy_private_ip: Optional[bool] = Field(default=None, alias="copyPrivateIp")
    copy_tags: Optional[bool] = Field(default=None, alias="copyTags")
    launch_disposition: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="launchDisposition"
    )
    licensing: Optional[LicensingModel] = Field(default=None, alias="licensing")
    name: Optional[str] = Field(default=None, alias="name")
    target_instance_type_right_sizing_method: Optional[
        Literal["BASIC", "NONE"]
    ] = Field(default=None, alias="targetInstanceTypeRightSizingMethod")


class LifeCycleLastLaunchModel(BaseModel):
    initiated: Optional[LifeCycleLastLaunchInitiatedModel] = Field(
        default=None, alias="initiated"
    )
    status: Optional[
        Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
    ] = Field(default=None, alias="status")


class ListExtensibleSourceServersResponseModel(BaseModel):
    items: List[StagingSourceServerModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourcePropertiesModel(BaseModel):
    cpus: Optional[List[CPUModel]] = Field(default=None, alias="cpus")
    disks: Optional[List[DiskModel]] = Field(default=None, alias="disks")
    identification_hints: Optional[IdentificationHintsModel] = Field(
        default=None, alias="identificationHints"
    )
    last_updated_date_time: Optional[str] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    os: Optional[OSModel] = Field(default=None, alias="os")
    ram_bytes: Optional[int] = Field(default=None, alias="ramBytes")
    recommended_instance_type: Optional[str] = Field(
        default=None, alias="recommendedInstanceType"
    )


class RecoveryInstanceDataReplicationInitiationModel(BaseModel):
    start_date_time: Optional[str] = Field(default=None, alias="startDateTime")
    steps: Optional[List[RecoveryInstanceDataReplicationInitiationStepModel]] = Field(
        default=None, alias="steps"
    )


class RecoveryInstancePropertiesModel(BaseModel):
    cpus: Optional[List[CPUModel]] = Field(default=None, alias="cpus")
    disks: Optional[List[RecoveryInstanceDiskModel]] = Field(
        default=None, alias="disks"
    )
    identification_hints: Optional[IdentificationHintsModel] = Field(
        default=None, alias="identificationHints"
    )
    last_updated_date_time: Optional[str] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    os: Optional[OSModel] = Field(default=None, alias="os")
    ram_bytes: Optional[int] = Field(default=None, alias="ramBytes")


class ReplicationConfigurationModel(BaseModel):
    associate_default_security_group: bool = Field(
        alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    create_public_ip: bool = Field(alias="createPublicIP")
    data_plane_routing: Literal["PRIVATE_IP", "PUBLIC_IP"] = Field(
        alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Literal["AUTO", "GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
    ebs_encryption_key_arn: str = Field(alias="ebsEncryptionKeyArn")
    name: str = Field(alias="name")
    pit_policy: List[PITPolicyRuleModel] = Field(alias="pitPolicy")
    replicated_disks: List[ReplicationConfigurationReplicatedDiskModel] = Field(
        alias="replicatedDisks"
    )
    replication_server_instance_type: str = Field(alias="replicationServerInstanceType")
    replication_servers_security_groups_ids: List[str] = Field(
        alias="replicationServersSecurityGroupsIDs"
    )
    source_server_id: str = Field(alias="sourceServerID")
    staging_area_subnet_id: str = Field(alias="stagingAreaSubnetId")
    staging_area_tags: Dict[str, str] = Field(alias="stagingAreaTags")
    use_dedicated_replication_server: bool = Field(
        alias="useDedicatedReplicationServer"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReplicationConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    associate_default_security_group: Optional[bool] = Field(
        default=None, alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: Optional[int] = Field(
        default=None, alias="bandwidthThrottling"
    )
    create_public_ip: Optional[bool] = Field(default=None, alias="createPublicIP")
    data_plane_routing: Optional[Literal["PRIVATE_IP", "PUBLIC_IP"]] = Field(
        default=None, alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "ST1"]
    ] = Field(default=None, alias="defaultLargeStagingDiskType")
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
    )
    name: Optional[str] = Field(default=None, alias="name")
    pit_policy: Optional[Sequence[PITPolicyRuleModel]] = Field(
        default=None, alias="pitPolicy"
    )
    replicated_disks: Optional[
        Sequence[ReplicationConfigurationReplicatedDiskModel]
    ] = Field(default=None, alias="replicatedDisks")
    replication_server_instance_type: Optional[str] = Field(
        default=None, alias="replicationServerInstanceType"
    )
    replication_servers_security_groups_ids: Optional[Sequence[str]] = Field(
        default=None, alias="replicationServersSecurityGroupsIDs"
    )
    staging_area_subnet_id: Optional[str] = Field(
        default=None, alias="stagingAreaSubnetId"
    )
    staging_area_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="stagingAreaTags"
    )
    use_dedicated_replication_server: Optional[bool] = Field(
        default=None, alias="useDedicatedReplicationServer"
    )


class StartRecoveryRequestModel(BaseModel):
    source_servers: Sequence[StartRecoveryRequestSourceServerModel] = Field(
        alias="sourceServers"
    )
    is_drill: Optional[bool] = Field(default=None, alias="isDrill")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class JobLogModel(BaseModel):
    event: Optional[
        Literal[
            "CLEANUP_END",
            "CLEANUP_FAIL",
            "CLEANUP_START",
            "CONVERSION_END",
            "CONVERSION_FAIL",
            "CONVERSION_START",
            "JOB_CANCEL",
            "JOB_END",
            "JOB_START",
            "LAUNCH_FAILED",
            "LAUNCH_START",
            "SERVER_SKIPPED",
            "SNAPSHOT_END",
            "SNAPSHOT_FAIL",
            "SNAPSHOT_START",
            "USING_PREVIOUS_SNAPSHOT",
            "USING_PREVIOUS_SNAPSHOT_FAILED",
        ]
    ] = Field(default=None, alias="event")
    event_data: Optional[JobLogEventDataModel] = Field(default=None, alias="eventData")
    log_date_time: Optional[str] = Field(default=None, alias="logDateTime")


class DescribeReplicationConfigurationTemplatesResponseModel(BaseModel):
    items: List[ReplicationConfigurationTemplateModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataReplicationInfoModel(BaseModel):
    data_replication_error: Optional[DataReplicationErrorModel] = Field(
        default=None, alias="dataReplicationError"
    )
    data_replication_initiation: Optional[DataReplicationInitiationModel] = Field(
        default=None, alias="dataReplicationInitiation"
    )
    data_replication_state: Optional[
        Literal[
            "BACKLOG",
            "CONTINUOUS",
            "CREATING_SNAPSHOT",
            "DISCONNECTED",
            "INITIAL_SYNC",
            "INITIATING",
            "PAUSED",
            "RESCAN",
            "STALLED",
            "STOPPED",
        ]
    ] = Field(default=None, alias="dataReplicationState")
    eta_date_time: Optional[str] = Field(default=None, alias="etaDateTime")
    lag_duration: Optional[str] = Field(default=None, alias="lagDuration")
    replicated_disks: Optional[List[DataReplicationInfoReplicatedDiskModel]] = Field(
        default=None, alias="replicatedDisks"
    )
    staging_availability_zone: Optional[str] = Field(
        default=None, alias="stagingAvailabilityZone"
    )


class DescribeJobsResponseModel(BaseModel):
    items: List[JobModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFailbackLaunchResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRecoveryResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateRecoveryInstancesResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifeCycleModel(BaseModel):
    added_to_service_date_time: Optional[str] = Field(
        default=None, alias="addedToServiceDateTime"
    )
    elapsed_replication_duration: Optional[str] = Field(
        default=None, alias="elapsedReplicationDuration"
    )
    first_byte_date_time: Optional[str] = Field(default=None, alias="firstByteDateTime")
    last_launch: Optional[LifeCycleLastLaunchModel] = Field(
        default=None, alias="lastLaunch"
    )
    last_seen_by_service_date_time: Optional[str] = Field(
        default=None, alias="lastSeenByServiceDateTime"
    )


class RecoveryInstanceDataReplicationInfoModel(BaseModel):
    data_replication_error: Optional[RecoveryInstanceDataReplicationErrorModel] = Field(
        default=None, alias="dataReplicationError"
    )
    data_replication_initiation: Optional[
        RecoveryInstanceDataReplicationInitiationModel
    ] = Field(default=None, alias="dataReplicationInitiation")
    data_replication_state: Optional[
        Literal[
            "BACKLOG",
            "CONTINUOUS",
            "CREATING_SNAPSHOT",
            "DISCONNECTED",
            "INITIAL_SYNC",
            "INITIATING",
            "NOT_STARTED",
            "PAUSED",
            "REPLICATION_STATE_NOT_AVAILABLE",
            "RESCAN",
            "STALLED",
            "STOPPED",
        ]
    ] = Field(default=None, alias="dataReplicationState")
    eta_date_time: Optional[str] = Field(default=None, alias="etaDateTime")
    lag_duration: Optional[str] = Field(default=None, alias="lagDuration")
    replicated_disks: Optional[
        List[RecoveryInstanceDataReplicationInfoReplicatedDiskModel]
    ] = Field(default=None, alias="replicatedDisks")
    staging_availability_zone: Optional[str] = Field(
        default=None, alias="stagingAvailabilityZone"
    )


class DescribeJobLogItemsResponseModel(BaseModel):
    items: List[JobLogModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceServerResponseMetadataModel(BaseModel):
    arn: str = Field(alias="arn")
    data_replication_info: DataReplicationInfoModel = Field(alias="dataReplicationInfo")
    last_launch_result: Literal[
        "FAILED", "NOT_STARTED", "PENDING", "SUCCEEDED"
    ] = Field(alias="lastLaunchResult")
    life_cycle: LifeCycleModel = Field(alias="lifeCycle")
    recovery_instance_id: str = Field(alias="recoveryInstanceId")
    replication_direction: Literal["FAILBACK", "FAILOVER"] = Field(
        alias="replicationDirection"
    )
    reversed_direction_source_server_arn: str = Field(
        alias="reversedDirectionSourceServerArn"
    )
    source_cloud_properties: SourceCloudPropertiesModel = Field(
        alias="sourceCloudProperties"
    )
    source_properties: SourcePropertiesModel = Field(alias="sourceProperties")
    source_server_id: str = Field(alias="sourceServerID")
    staging_area: StagingAreaModel = Field(alias="stagingArea")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceServerModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    data_replication_info: Optional[DataReplicationInfoModel] = Field(
        default=None, alias="dataReplicationInfo"
    )
    last_launch_result: Optional[
        Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCEEDED"]
    ] = Field(default=None, alias="lastLaunchResult")
    life_cycle: Optional[LifeCycleModel] = Field(default=None, alias="lifeCycle")
    recovery_instance_id: Optional[str] = Field(
        default=None, alias="recoveryInstanceId"
    )
    replication_direction: Optional[Literal["FAILBACK", "FAILOVER"]] = Field(
        default=None, alias="replicationDirection"
    )
    reversed_direction_source_server_arn: Optional[str] = Field(
        default=None, alias="reversedDirectionSourceServerArn"
    )
    source_cloud_properties: Optional[SourceCloudPropertiesModel] = Field(
        default=None, alias="sourceCloudProperties"
    )
    source_properties: Optional[SourcePropertiesModel] = Field(
        default=None, alias="sourceProperties"
    )
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")
    staging_area: Optional[StagingAreaModel] = Field(default=None, alias="stagingArea")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class RecoveryInstanceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    data_replication_info: Optional[RecoveryInstanceDataReplicationInfoModel] = Field(
        default=None, alias="dataReplicationInfo"
    )
    ec2_instance_id: Optional[str] = Field(default=None, alias="ec2InstanceID")
    ec2_instance_state: Optional[
        Literal[
            "NOT_FOUND",
            "PENDING",
            "RUNNING",
            "SHUTTING-DOWN",
            "STOPPED",
            "STOPPING",
            "TERMINATED",
        ]
    ] = Field(default=None, alias="ec2InstanceState")
    failback: Optional[RecoveryInstanceFailbackModel] = Field(
        default=None, alias="failback"
    )
    is_drill: Optional[bool] = Field(default=None, alias="isDrill")
    job_id: Optional[str] = Field(default=None, alias="jobID")
    origin_availability_zone: Optional[str] = Field(
        default=None, alias="originAvailabilityZone"
    )
    origin_environment: Optional[Literal["AWS", "ON_PREMISES"]] = Field(
        default=None, alias="originEnvironment"
    )
    point_in_time_snapshot_date_time: Optional[str] = Field(
        default=None, alias="pointInTimeSnapshotDateTime"
    )
    recovery_instance_id: Optional[str] = Field(
        default=None, alias="recoveryInstanceID"
    )
    recovery_instance_properties: Optional[RecoveryInstancePropertiesModel] = Field(
        default=None, alias="recoveryInstanceProperties"
    )
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateExtendedSourceServerResponseModel(BaseModel):
    source_server: SourceServerModel = Field(alias="sourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSourceServersResponseModel(BaseModel):
    items: List[SourceServerModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplicationResponseModel(BaseModel):
    source_server: SourceServerModel = Field(alias="sourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopReplicationResponseModel(BaseModel):
    source_server: SourceServerModel = Field(alias="sourceServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRecoveryInstancesResponseModel(BaseModel):
    items: List[RecoveryInstanceModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
