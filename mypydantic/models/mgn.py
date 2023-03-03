# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationAggregatedStatusModel(BaseModel):
    health_status: Optional[Literal["ERROR", "HEALTHY", "LAGGING"]] = Field(
        default=None, alias="healthStatus"
    )
    last_update_date_time: Optional[str] = Field(
        default=None, alias="lastUpdateDateTime"
    )
    progress_status: Optional[
        Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="progressStatus")
    total_source_servers: Optional[int] = Field(
        default=None, alias="totalSourceServers"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ArchiveApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")


class ArchiveWaveRequestModel(BaseModel):
    wave_id: str = Field(alias="waveID")


class AssociateApplicationsRequestModel(BaseModel):
    application_ids: Sequence[str] = Field(alias="applicationIDs")
    wave_id: str = Field(alias="waveID")


class AssociateSourceServersRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")
    source_server_ids: Sequence[str] = Field(alias="sourceServerIDs")


class CPUModel(BaseModel):
    cores: Optional[int] = Field(default=None, alias="cores")
    model_name: Optional[str] = Field(default=None, alias="modelName")


class ChangeServerLifeCycleStateSourceServerLifecycleModel(BaseModel):
    state: Literal["CUTOVER", "READY_FOR_CUTOVER", "READY_FOR_TEST"] = Field(
        alias="state"
    )


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class LaunchTemplateDiskConfModel(BaseModel):
    iops: Optional[int] = Field(default=None, alias="iops")
    throughput: Optional[int] = Field(default=None, alias="throughput")
    volume_type: Optional[
        Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
    ] = Field(default=None, alias="volumeType")


class LicensingModel(BaseModel):
    os_byol: Optional[bool] = Field(default=None, alias="osByol")


class CreateReplicationConfigurationTemplateRequestModel(BaseModel):
    associate_default_security_group: bool = Field(
        alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    create_public_ip: bool = Field(alias="createPublicIP")
    data_plane_routing: Literal["PRIVATE_IP", "PUBLIC_IP"] = Field(
        alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Literal["GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
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


class CreateWaveRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


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
            "LAST_SNAPSHOT_JOB_FAILED",
            "NOT_CONVERGING",
            "SNAPSHOTS_FAILURE",
            "UNSTABLE_NETWORK",
            "UNSUPPORTED_VM_CONFIGURATION",
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


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")


class DeleteJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobID")


class DeleteLaunchConfigurationTemplateRequestModel(BaseModel):
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")


class DeleteReplicationConfigurationTemplateRequestModel(BaseModel):
    replication_configuration_template_id: str = Field(
        alias="replicationConfigurationTemplateID"
    )


class DeleteSourceServerRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class DeleteVcenterClientRequestModel(BaseModel):
    vcenter_client_id: str = Field(alias="vcenterClientID")


class DeleteWaveRequestModel(BaseModel):
    wave_id: str = Field(alias="waveID")


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


class DescribeLaunchConfigurationTemplatesRequestModel(BaseModel):
    launch_configuration_template_ids: Optional[Sequence[str]] = Field(
        default=None, alias="launchConfigurationTemplateIDs"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeReplicationConfigurationTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    replication_configuration_template_ids: Optional[Sequence[str]] = Field(
        default=None, alias="replicationConfigurationTemplateIDs"
    )


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
    default_large_staging_disk_type: Optional[Literal["GP2", "GP3", "ST1"]] = Field(
        default=None, alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
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


class DescribeSourceServersRequestFiltersModel(BaseModel):
    application_ids: Optional[Sequence[str]] = Field(
        default=None, alias="applicationIDs"
    )
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    life_cycle_states: Optional[
        Sequence[
            Literal[
                "CUTOVER",
                "CUTTING_OVER",
                "DISCONNECTED",
                "DISCOVERED",
                "NOT_READY",
                "READY_FOR_CUTOVER",
                "READY_FOR_TEST",
                "STOPPED",
                "TESTING",
            ]
        ]
    ] = Field(default=None, alias="lifeCycleStates")
    replication_types: Optional[
        Sequence[Literal["AGENT_BASED", "SNAPSHOT_SHIPPING"]]
    ] = Field(default=None, alias="replicationTypes")
    source_server_ids: Optional[Sequence[str]] = Field(
        default=None, alias="sourceServerIDs"
    )


class DescribeVcenterClientsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VcenterClientModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    datacenter_name: Optional[str] = Field(default=None, alias="datacenterName")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    last_seen_datetime: Optional[str] = Field(default=None, alias="lastSeenDatetime")
    source_server_tags: Optional[Dict[str, str]] = Field(
        default=None, alias="sourceServerTags"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    vcenter_client_id: Optional[str] = Field(default=None, alias="vcenterClientID")
    vcenter_uuid: Optional[str] = Field(default=None, alias="vcenterUUID")


class DisassociateApplicationsRequestModel(BaseModel):
    application_ids: Sequence[str] = Field(alias="applicationIDs")
    wave_id: str = Field(alias="waveID")


class DisassociateSourceServersRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")
    source_server_ids: Sequence[str] = Field(alias="sourceServerIDs")


class DisconnectFromServiceRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class DiskModel(BaseModel):
    bytes: Optional[int] = Field(default=None, alias="bytes")
    device_name: Optional[str] = Field(default=None, alias="deviceName")


class FinalizeCutoverRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class GetLaunchConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class GetReplicationConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class IdentificationHintsModel(BaseModel):
    aws_instance_id: Optional[str] = Field(default=None, alias="awsInstanceID")
    fqdn: Optional[str] = Field(default=None, alias="fqdn")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    vm_path: Optional[str] = Field(default=None, alias="vmPath")
    vm_ware_uuid: Optional[str] = Field(default=None, alias="vmWareUuid")


class JobLogEventDataModel(BaseModel):
    conversion_server_id: Optional[str] = Field(
        default=None, alias="conversionServerID"
    )
    raw_error: Optional[str] = Field(default=None, alias="rawError")
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")
    target_instance_id: Optional[str] = Field(default=None, alias="targetInstanceID")


class LaunchedInstanceModel(BaseModel):
    ec2_instance_id: Optional[str] = Field(default=None, alias="ec2InstanceID")
    first_boot: Optional[Literal["STOPPED", "SUCCEEDED", "UNKNOWN", "WAITING"]] = Field(
        default=None, alias="firstBoot"
    )
    job_id: Optional[str] = Field(default=None, alias="jobID")


class LifeCycleLastCutoverFinalizedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")


class LifeCycleLastCutoverInitiatedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")
    job_id: Optional[str] = Field(default=None, alias="jobID")


class LifeCycleLastCutoverRevertedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")


class LifeCycleLastTestFinalizedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")


class LifeCycleLastTestInitiatedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")
    job_id: Optional[str] = Field(default=None, alias="jobID")


class LifeCycleLastTestRevertedModel(BaseModel):
    api_call_date_time: Optional[str] = Field(default=None, alias="apiCallDateTime")


class ListApplicationsRequestFiltersModel(BaseModel):
    application_ids: Optional[Sequence[str]] = Field(
        default=None, alias="applicationIDs"
    )
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    wave_ids: Optional[Sequence[str]] = Field(default=None, alias="waveIDs")


class SourceServerActionsRequestFiltersModel(BaseModel):
    action_ids: Optional[Sequence[str]] = Field(default=None, alias="actionIDs")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TemplateActionsRequestFiltersModel(BaseModel):
    action_ids: Optional[Sequence[str]] = Field(default=None, alias="actionIDs")


class ListWavesRequestFiltersModel(BaseModel):
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    wave_ids: Optional[Sequence[str]] = Field(default=None, alias="waveIDs")


class MarkAsArchivedRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class NetworkInterfaceModel(BaseModel):
    ips: Optional[List[str]] = Field(default=None, alias="ips")
    is_primary: Optional[bool] = Field(default=None, alias="isPrimary")
    mac_address: Optional[str] = Field(default=None, alias="macAddress")


class OSModel(BaseModel):
    full_string: Optional[str] = Field(default=None, alias="fullString")


class SsmParameterStoreParameterModel(BaseModel):
    parameter_name: str = Field(alias="parameterName")
    parameter_type: Literal["STRING"] = Field(alias="parameterType")


class RemoveSourceServerActionRequestModel(BaseModel):
    action_id: str = Field(alias="actionID")
    source_server_id: str = Field(alias="sourceServerID")


class RemoveTemplateActionRequestModel(BaseModel):
    action_id: str = Field(alias="actionID")
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")


class ReplicationConfigurationReplicatedDiskModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    iops: Optional[int] = Field(default=None, alias="iops")
    is_boot_disk: Optional[bool] = Field(default=None, alias="isBootDisk")
    staging_disk_type: Optional[
        Literal["AUTO", "GP2", "GP3", "IO1", "IO2", "SC1", "ST1", "STANDARD"]
    ] = Field(default=None, alias="stagingDiskType")
    throughput: Optional[int] = Field(default=None, alias="throughput")


class RetryDataReplicationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class StartCutoverRequestModel(BaseModel):
    source_server_ids: Sequence[str] = Field(alias="sourceServerIDs")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StartReplicationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")


class StartTestRequestModel(BaseModel):
    source_server_ids: Sequence[str] = Field(alias="sourceServerIDs")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TerminateTargetInstancesRequestModel(BaseModel):
    source_server_ids: Sequence[str] = Field(alias="sourceServerIDs")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UnarchiveApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")


class UnarchiveWaveRequestModel(BaseModel):
    wave_id: str = Field(alias="waveID")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationID")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")


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
    default_large_staging_disk_type: Optional[Literal["GP2", "GP3", "ST1"]] = Field(
        default=None, alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
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


class UpdateSourceServerReplicationTypeRequestModel(BaseModel):
    replication_type: Literal["AGENT_BASED", "SNAPSHOT_SHIPPING"] = Field(
        alias="replicationType"
    )
    source_server_id: str = Field(alias="sourceServerID")


class UpdateWaveRequestModel(BaseModel):
    wave_id: str = Field(alias="waveID")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")


class WaveAggregatedStatusModel(BaseModel):
    health_status: Optional[Literal["ERROR", "HEALTHY", "LAGGING"]] = Field(
        default=None, alias="healthStatus"
    )
    last_update_date_time: Optional[str] = Field(
        default=None, alias="lastUpdateDateTime"
    )
    progress_status: Optional[
        Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="progressStatus")
    replication_started_date_time: Optional[str] = Field(
        default=None, alias="replicationStartedDateTime"
    )
    total_applications: Optional[int] = Field(default=None, alias="totalApplications")


class ApplicationModel(BaseModel):
    application_aggregated_status: Optional[ApplicationAggregatedStatusModel] = Field(
        default=None, alias="applicationAggregatedStatus"
    )
    application_id: Optional[str] = Field(default=None, alias="applicationID")
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_date_time: Optional[str] = Field(default=None, alias="creationDateTime")
    description: Optional[str] = Field(default=None, alias="description")
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    last_modified_date_time: Optional[str] = Field(
        default=None, alias="lastModifiedDateTime"
    )
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    wave_id: Optional[str] = Field(default=None, alias="waveID")


class ApplicationResponseMetadataModel(BaseModel):
    application_aggregated_status: ApplicationAggregatedStatusModel = Field(
        alias="applicationAggregatedStatus"
    )
    application_id: str = Field(alias="applicationID")
    arn: str = Field(alias="arn")
    creation_date_time: str = Field(alias="creationDateTime")
    description: str = Field(alias="description")
    is_archived: bool = Field(alias="isArchived")
    last_modified_date_time: str = Field(alias="lastModifiedDateTime")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    wave_id: str = Field(alias="waveID")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
    default_large_staging_disk_type: Literal["GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
    ebs_encryption_key_arn: str = Field(alias="ebsEncryptionKeyArn")
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


class ChangeServerLifeCycleStateRequestModel(BaseModel):
    life_cycle: ChangeServerLifeCycleStateSourceServerLifecycleModel = Field(
        alias="lifeCycle"
    )
    source_server_id: str = Field(alias="sourceServerID")


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


class DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateModel(
    BaseModel
):
    launch_configuration_template_ids: Optional[Sequence[str]] = Field(
        default=None, alias="launchConfigurationTemplateIDs"
    )
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


class DescribeVcenterClientsRequestDescribeVcenterClientsPaginateModel(BaseModel):
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


class DescribeReplicationConfigurationTemplatesResponseModel(BaseModel):
    items: List[ReplicationConfigurationTemplateModel] = Field(alias="items")
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


class DescribeVcenterClientsResponseModel(BaseModel):
    items: List[VcenterClientModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
        ]
    ] = Field(default=None, alias="event")
    event_data: Optional[JobLogEventDataModel] = Field(default=None, alias="eventData")
    log_date_time: Optional[str] = Field(default=None, alias="logDateTime")


class LifeCycleLastCutoverModel(BaseModel):
    finalized: Optional[LifeCycleLastCutoverFinalizedModel] = Field(
        default=None, alias="finalized"
    )
    initiated: Optional[LifeCycleLastCutoverInitiatedModel] = Field(
        default=None, alias="initiated"
    )
    reverted: Optional[LifeCycleLastCutoverRevertedModel] = Field(
        default=None, alias="reverted"
    )


class LifeCycleLastTestModel(BaseModel):
    finalized: Optional[LifeCycleLastTestFinalizedModel] = Field(
        default=None, alias="finalized"
    )
    initiated: Optional[LifeCycleLastTestInitiatedModel] = Field(
        default=None, alias="initiated"
    )
    reverted: Optional[LifeCycleLastTestRevertedModel] = Field(
        default=None, alias="reverted"
    )


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    filters: Optional[ListApplicationsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationsRequestModel(BaseModel):
    filters: Optional[ListApplicationsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSourceServerActionsRequestListSourceServerActionsPaginateModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    filters: Optional[SourceServerActionsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSourceServerActionsRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    filters: Optional[SourceServerActionsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTemplateActionsRequestListTemplateActionsPaginateModel(BaseModel):
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    filters: Optional[TemplateActionsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplateActionsRequestModel(BaseModel):
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    filters: Optional[TemplateActionsRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListWavesRequestListWavesPaginateModel(BaseModel):
    filters: Optional[ListWavesRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWavesRequestModel(BaseModel):
    filters: Optional[ListWavesRequestFiltersModel] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


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


class PutSourceServerActionRequestModel(BaseModel):
    action_id: str = Field(alias="actionID")
    action_name: str = Field(alias="actionName")
    document_identifier: str = Field(alias="documentIdentifier")
    order: int = Field(alias="order")
    source_server_id: str = Field(alias="sourceServerID")
    active: Optional[bool] = Field(default=None, alias="active")
    document_version: Optional[str] = Field(default=None, alias="documentVersion")
    must_succeed_for_cutover: Optional[bool] = Field(
        default=None, alias="mustSucceedForCutover"
    )
    parameters: Optional[
        Mapping[str, Sequence[SsmParameterStoreParameterModel]]
    ] = Field(default=None, alias="parameters")
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")


class PutTemplateActionRequestModel(BaseModel):
    action_id: str = Field(alias="actionID")
    action_name: str = Field(alias="actionName")
    document_identifier: str = Field(alias="documentIdentifier")
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    order: int = Field(alias="order")
    active: Optional[bool] = Field(default=None, alias="active")
    document_version: Optional[str] = Field(default=None, alias="documentVersion")
    must_succeed_for_cutover: Optional[bool] = Field(
        default=None, alias="mustSucceedForCutover"
    )
    operating_system: Optional[str] = Field(default=None, alias="operatingSystem")
    parameters: Optional[
        Mapping[str, Sequence[SsmParameterStoreParameterModel]]
    ] = Field(default=None, alias="parameters")
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")


class SourceServerActionDocumentResponseMetadataModel(BaseModel):
    action_id: str = Field(alias="actionID")
    action_name: str = Field(alias="actionName")
    active: bool = Field(alias="active")
    document_identifier: str = Field(alias="documentIdentifier")
    document_version: str = Field(alias="documentVersion")
    must_succeed_for_cutover: bool = Field(alias="mustSucceedForCutover")
    order: int = Field(alias="order")
    parameters: Dict[str, List[SsmParameterStoreParameterModel]] = Field(
        alias="parameters"
    )
    timeout_seconds: int = Field(alias="timeoutSeconds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceServerActionDocumentModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="actionID")
    action_name: Optional[str] = Field(default=None, alias="actionName")
    active: Optional[bool] = Field(default=None, alias="active")
    document_identifier: Optional[str] = Field(default=None, alias="documentIdentifier")
    document_version: Optional[str] = Field(default=None, alias="documentVersion")
    must_succeed_for_cutover: Optional[bool] = Field(
        default=None, alias="mustSucceedForCutover"
    )
    order: Optional[int] = Field(default=None, alias="order")
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterModel]]] = Field(
        default=None, alias="parameters"
    )
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")


class SsmDocumentModel(BaseModel):
    action_name: str = Field(alias="actionName")
    ssm_document_name: str = Field(alias="ssmDocumentName")
    must_succeed_for_cutover: Optional[bool] = Field(
        default=None, alias="mustSucceedForCutover"
    )
    parameters: Optional[
        Mapping[str, Sequence[SsmParameterStoreParameterModel]]
    ] = Field(default=None, alias="parameters")
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")


class TemplateActionDocumentResponseMetadataModel(BaseModel):
    action_id: str = Field(alias="actionID")
    action_name: str = Field(alias="actionName")
    active: bool = Field(alias="active")
    document_identifier: str = Field(alias="documentIdentifier")
    document_version: str = Field(alias="documentVersion")
    must_succeed_for_cutover: bool = Field(alias="mustSucceedForCutover")
    operating_system: str = Field(alias="operatingSystem")
    order: int = Field(alias="order")
    parameters: Dict[str, List[SsmParameterStoreParameterModel]] = Field(
        alias="parameters"
    )
    timeout_seconds: int = Field(alias="timeoutSeconds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TemplateActionDocumentModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="actionID")
    action_name: Optional[str] = Field(default=None, alias="actionName")
    active: Optional[bool] = Field(default=None, alias="active")
    document_identifier: Optional[str] = Field(default=None, alias="documentIdentifier")
    document_version: Optional[str] = Field(default=None, alias="documentVersion")
    must_succeed_for_cutover: Optional[bool] = Field(
        default=None, alias="mustSucceedForCutover"
    )
    operating_system: Optional[str] = Field(default=None, alias="operatingSystem")
    order: Optional[int] = Field(default=None, alias="order")
    parameters: Optional[Dict[str, List[SsmParameterStoreParameterModel]]] = Field(
        default=None, alias="parameters"
    )
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")


class ReplicationConfigurationModel(BaseModel):
    associate_default_security_group: bool = Field(
        alias="associateDefaultSecurityGroup"
    )
    bandwidth_throttling: int = Field(alias="bandwidthThrottling")
    create_public_ip: bool = Field(alias="createPublicIP")
    data_plane_routing: Literal["PRIVATE_IP", "PUBLIC_IP"] = Field(
        alias="dataPlaneRouting"
    )
    default_large_staging_disk_type: Literal["GP2", "GP3", "ST1"] = Field(
        alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Literal["CUSTOM", "DEFAULT"] = Field(alias="ebsEncryption")
    ebs_encryption_key_arn: str = Field(alias="ebsEncryptionKeyArn")
    name: str = Field(alias="name")
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
    default_large_staging_disk_type: Optional[Literal["GP2", "GP3", "ST1"]] = Field(
        default=None, alias="defaultLargeStagingDiskType"
    )
    ebs_encryption: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ebsEncryption"
    )
    ebs_encryption_key_arn: Optional[str] = Field(
        default=None, alias="ebsEncryptionKeyArn"
    )
    name: Optional[str] = Field(default=None, alias="name")
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


class WaveResponseMetadataModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_date_time: str = Field(alias="creationDateTime")
    description: str = Field(alias="description")
    is_archived: bool = Field(alias="isArchived")
    last_modified_date_time: str = Field(alias="lastModifiedDateTime")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    wave_aggregated_status: WaveAggregatedStatusModel = Field(
        alias="waveAggregatedStatus"
    )
    wave_id: str = Field(alias="waveID")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WaveModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_date_time: Optional[str] = Field(default=None, alias="creationDateTime")
    description: Optional[str] = Field(default=None, alias="description")
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    last_modified_date_time: Optional[str] = Field(
        default=None, alias="lastModifiedDateTime"
    )
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    wave_aggregated_status: Optional[WaveAggregatedStatusModel] = Field(
        default=None, alias="waveAggregatedStatus"
    )
    wave_id: Optional[str] = Field(default=None, alias="waveID")


class ListApplicationsResponseModel(BaseModel):
    items: List[ApplicationModel] = Field(alias="items")
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
            "PENDING_SNAPSHOT_SHIPPING",
            "RESCAN",
            "SHIPPING_SNAPSHOT",
            "STALLED",
            "STOPPED",
        ]
    ] = Field(default=None, alias="dataReplicationState")
    eta_date_time: Optional[str] = Field(default=None, alias="etaDateTime")
    lag_duration: Optional[str] = Field(default=None, alias="lagDuration")
    last_snapshot_date_time: Optional[str] = Field(
        default=None, alias="lastSnapshotDateTime"
    )
    replicated_disks: Optional[List[DataReplicationInfoReplicatedDiskModel]] = Field(
        default=None, alias="replicatedDisks"
    )


class DescribeJobLogItemsResponseModel(BaseModel):
    items: List[JobLogModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifeCycleModel(BaseModel):
    added_to_service_date_time: Optional[str] = Field(
        default=None, alias="addedToServiceDateTime"
    )
    elapsed_replication_duration: Optional[str] = Field(
        default=None, alias="elapsedReplicationDuration"
    )
    first_byte_date_time: Optional[str] = Field(default=None, alias="firstByteDateTime")
    last_cutover: Optional[LifeCycleLastCutoverModel] = Field(
        default=None, alias="lastCutover"
    )
    last_seen_by_service_date_time: Optional[str] = Field(
        default=None, alias="lastSeenByServiceDateTime"
    )
    last_test: Optional[LifeCycleLastTestModel] = Field(default=None, alias="lastTest")
    state: Optional[
        Literal[
            "CUTOVER",
            "CUTTING_OVER",
            "DISCONNECTED",
            "DISCOVERED",
            "NOT_READY",
            "READY_FOR_CUTOVER",
            "READY_FOR_TEST",
            "STOPPED",
            "TESTING",
        ]
    ] = Field(default=None, alias="state")


class ListSourceServerActionsResponseModel(BaseModel):
    items: List[SourceServerActionDocumentModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobPostLaunchActionsLaunchStatusModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="executionID")
    execution_status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="executionStatus"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    ssm_document: Optional[SsmDocumentModel] = Field(default=None, alias="ssmDocument")
    ssm_document_type: Optional[Literal["AUTOMATION", "COMMAND"]] = Field(
        default=None, alias="ssmDocumentType"
    )


class PostLaunchActionsModel(BaseModel):
    cloud_watch_log_group_name: Optional[str] = Field(
        default=None, alias="cloudWatchLogGroupName"
    )
    deployment: Optional[
        Literal["CUTOVER_ONLY", "TEST_AND_CUTOVER", "TEST_ONLY"]
    ] = Field(default=None, alias="deployment")
    s3_log_bucket: Optional[str] = Field(default=None, alias="s3LogBucket")
    s3_output_key_prefix: Optional[str] = Field(default=None, alias="s3OutputKeyPrefix")
    ssm_documents: Optional[Sequence[SsmDocumentModel]] = Field(
        default=None, alias="ssmDocuments"
    )


class ListTemplateActionsResponseModel(BaseModel):
    items: List[TemplateActionDocumentModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWavesResponseModel(BaseModel):
    items: List[WaveModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceServerResponseMetadataModel(BaseModel):
    application_id: str = Field(alias="applicationID")
    arn: str = Field(alias="arn")
    data_replication_info: DataReplicationInfoModel = Field(alias="dataReplicationInfo")
    is_archived: bool = Field(alias="isArchived")
    launched_instance: LaunchedInstanceModel = Field(alias="launchedInstance")
    life_cycle: LifeCycleModel = Field(alias="lifeCycle")
    replication_type: Literal["AGENT_BASED", "SNAPSHOT_SHIPPING"] = Field(
        alias="replicationType"
    )
    source_properties: SourcePropertiesModel = Field(alias="sourceProperties")
    source_server_id: str = Field(alias="sourceServerID")
    tags: Dict[str, str] = Field(alias="tags")
    vcenter_client_id: str = Field(alias="vcenterClientID")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceServerModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="applicationID")
    arn: Optional[str] = Field(default=None, alias="arn")
    data_replication_info: Optional[DataReplicationInfoModel] = Field(
        default=None, alias="dataReplicationInfo"
    )
    is_archived: Optional[bool] = Field(default=None, alias="isArchived")
    launched_instance: Optional[LaunchedInstanceModel] = Field(
        default=None, alias="launchedInstance"
    )
    life_cycle: Optional[LifeCycleModel] = Field(default=None, alias="lifeCycle")
    replication_type: Optional[Literal["AGENT_BASED", "SNAPSHOT_SHIPPING"]] = Field(
        default=None, alias="replicationType"
    )
    source_properties: Optional[SourcePropertiesModel] = Field(
        default=None, alias="sourceProperties"
    )
    source_server_id: Optional[str] = Field(default=None, alias="sourceServerID")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    vcenter_client_id: Optional[str] = Field(default=None, alias="vcenterClientID")


class PostLaunchActionsStatusModel(BaseModel):
    post_launch_actions_launch_status_list: Optional[
        List[JobPostLaunchActionsLaunchStatusModel]
    ] = Field(default=None, alias="postLaunchActionsLaunchStatusList")
    ssm_agent_discovery_datetime: Optional[str] = Field(
        default=None, alias="ssmAgentDiscoveryDatetime"
    )


class CreateLaunchConfigurationTemplateRequestModel(BaseModel):
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="associatePublicIpAddress"
    )
    boot_mode: Optional[Literal["LEGACY_BIOS", "UEFI"]] = Field(
        default=None, alias="bootMode"
    )
    copy_private_ip: Optional[bool] = Field(default=None, alias="copyPrivateIp")
    copy_tags: Optional[bool] = Field(default=None, alias="copyTags")
    enable_map_auto_tagging: Optional[bool] = Field(
        default=None, alias="enableMapAutoTagging"
    )
    large_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="largeVolumeConf"
    )
    launch_disposition: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="launchDisposition"
    )
    licensing: Optional[LicensingModel] = Field(default=None, alias="licensing")
    map_auto_tagging_mpe_id: Optional[str] = Field(
        default=None, alias="mapAutoTaggingMpeID"
    )
    post_launch_actions: Optional[PostLaunchActionsModel] = Field(
        default=None, alias="postLaunchActions"
    )
    small_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="smallVolumeConf"
    )
    small_volume_max_size: Optional[int] = Field(
        default=None, alias="smallVolumeMaxSize"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    target_instance_type_right_sizing_method: Optional[
        Literal["BASIC", "NONE"]
    ] = Field(default=None, alias="targetInstanceTypeRightSizingMethod")


class LaunchConfigurationTemplateResponseMetadataModel(BaseModel):
    arn: str = Field(alias="arn")
    associate_public_ip_address: bool = Field(alias="associatePublicIpAddress")
    boot_mode: Literal["LEGACY_BIOS", "UEFI"] = Field(alias="bootMode")
    copy_private_ip: bool = Field(alias="copyPrivateIp")
    copy_tags: bool = Field(alias="copyTags")
    ec2_launch_template_id: str = Field(alias="ec2LaunchTemplateID")
    enable_map_auto_tagging: bool = Field(alias="enableMapAutoTagging")
    large_volume_conf: LaunchTemplateDiskConfModel = Field(alias="largeVolumeConf")
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    launch_disposition: Literal["STARTED", "STOPPED"] = Field(alias="launchDisposition")
    licensing: LicensingModel = Field(alias="licensing")
    map_auto_tagging_mpe_id: str = Field(alias="mapAutoTaggingMpeID")
    post_launch_actions: PostLaunchActionsModel = Field(alias="postLaunchActions")
    small_volume_conf: LaunchTemplateDiskConfModel = Field(alias="smallVolumeConf")
    small_volume_max_size: int = Field(alias="smallVolumeMaxSize")
    tags: Dict[str, str] = Field(alias="tags")
    target_instance_type_right_sizing_method: Literal["BASIC", "NONE"] = Field(
        alias="targetInstanceTypeRightSizingMethod"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LaunchConfigurationTemplateModel(BaseModel):
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    arn: Optional[str] = Field(default=None, alias="arn")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="associatePublicIpAddress"
    )
    boot_mode: Optional[Literal["LEGACY_BIOS", "UEFI"]] = Field(
        default=None, alias="bootMode"
    )
    copy_private_ip: Optional[bool] = Field(default=None, alias="copyPrivateIp")
    copy_tags: Optional[bool] = Field(default=None, alias="copyTags")
    ec2_launch_template_id: Optional[str] = Field(
        default=None, alias="ec2LaunchTemplateID"
    )
    enable_map_auto_tagging: Optional[bool] = Field(
        default=None, alias="enableMapAutoTagging"
    )
    large_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="largeVolumeConf"
    )
    launch_disposition: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="launchDisposition"
    )
    licensing: Optional[LicensingModel] = Field(default=None, alias="licensing")
    map_auto_tagging_mpe_id: Optional[str] = Field(
        default=None, alias="mapAutoTaggingMpeID"
    )
    post_launch_actions: Optional[PostLaunchActionsModel] = Field(
        default=None, alias="postLaunchActions"
    )
    small_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="smallVolumeConf"
    )
    small_volume_max_size: Optional[int] = Field(
        default=None, alias="smallVolumeMaxSize"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    target_instance_type_right_sizing_method: Optional[
        Literal["BASIC", "NONE"]
    ] = Field(default=None, alias="targetInstanceTypeRightSizingMethod")


class LaunchConfigurationModel(BaseModel):
    boot_mode: Literal["LEGACY_BIOS", "UEFI"] = Field(alias="bootMode")
    copy_private_ip: bool = Field(alias="copyPrivateIp")
    copy_tags: bool = Field(alias="copyTags")
    ec2_launch_template_id: str = Field(alias="ec2LaunchTemplateID")
    enable_map_auto_tagging: bool = Field(alias="enableMapAutoTagging")
    launch_disposition: Literal["STARTED", "STOPPED"] = Field(alias="launchDisposition")
    licensing: LicensingModel = Field(alias="licensing")
    map_auto_tagging_mpe_id: str = Field(alias="mapAutoTaggingMpeID")
    name: str = Field(alias="name")
    post_launch_actions: PostLaunchActionsModel = Field(alias="postLaunchActions")
    source_server_id: str = Field(alias="sourceServerID")
    target_instance_type_right_sizing_method: Literal["BASIC", "NONE"] = Field(
        alias="targetInstanceTypeRightSizingMethod"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLaunchConfigurationRequestModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    boot_mode: Optional[Literal["LEGACY_BIOS", "UEFI"]] = Field(
        default=None, alias="bootMode"
    )
    copy_private_ip: Optional[bool] = Field(default=None, alias="copyPrivateIp")
    copy_tags: Optional[bool] = Field(default=None, alias="copyTags")
    enable_map_auto_tagging: Optional[bool] = Field(
        default=None, alias="enableMapAutoTagging"
    )
    launch_disposition: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="launchDisposition"
    )
    licensing: Optional[LicensingModel] = Field(default=None, alias="licensing")
    map_auto_tagging_mpe_id: Optional[str] = Field(
        default=None, alias="mapAutoTaggingMpeID"
    )
    name: Optional[str] = Field(default=None, alias="name")
    post_launch_actions: Optional[PostLaunchActionsModel] = Field(
        default=None, alias="postLaunchActions"
    )
    target_instance_type_right_sizing_method: Optional[
        Literal["BASIC", "NONE"]
    ] = Field(default=None, alias="targetInstanceTypeRightSizingMethod")


class UpdateLaunchConfigurationTemplateRequestModel(BaseModel):
    launch_configuration_template_id: str = Field(alias="launchConfigurationTemplateID")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="associatePublicIpAddress"
    )
    boot_mode: Optional[Literal["LEGACY_BIOS", "UEFI"]] = Field(
        default=None, alias="bootMode"
    )
    copy_private_ip: Optional[bool] = Field(default=None, alias="copyPrivateIp")
    copy_tags: Optional[bool] = Field(default=None, alias="copyTags")
    enable_map_auto_tagging: Optional[bool] = Field(
        default=None, alias="enableMapAutoTagging"
    )
    large_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="largeVolumeConf"
    )
    launch_disposition: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="launchDisposition"
    )
    licensing: Optional[LicensingModel] = Field(default=None, alias="licensing")
    map_auto_tagging_mpe_id: Optional[str] = Field(
        default=None, alias="mapAutoTaggingMpeID"
    )
    post_launch_actions: Optional[PostLaunchActionsModel] = Field(
        default=None, alias="postLaunchActions"
    )
    small_volume_conf: Optional[LaunchTemplateDiskConfModel] = Field(
        default=None, alias="smallVolumeConf"
    )
    small_volume_max_size: Optional[int] = Field(
        default=None, alias="smallVolumeMaxSize"
    )
    target_instance_type_right_sizing_method: Optional[
        Literal["BASIC", "NONE"]
    ] = Field(default=None, alias="targetInstanceTypeRightSizingMethod")


class DescribeSourceServersResponseModel(BaseModel):
    items: List[SourceServerModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParticipatingServerModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerID")
    launch_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
    ] = Field(default=None, alias="launchStatus")
    launched_ec2_instance_id: Optional[str] = Field(
        default=None, alias="launchedEc2InstanceID"
    )
    post_launch_actions_status: Optional[PostLaunchActionsStatusModel] = Field(
        default=None, alias="postLaunchActionsStatus"
    )


class DescribeLaunchConfigurationTemplatesResponseModel(BaseModel):
    items: List[LaunchConfigurationTemplateModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobModel(BaseModel):
    job_id: str = Field(alias="jobID")
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_date_time: Optional[str] = Field(default=None, alias="creationDateTime")
    end_date_time: Optional[str] = Field(default=None, alias="endDateTime")
    initiated_by: Optional[
        Literal["DIAGNOSTIC", "START_CUTOVER", "START_TEST", "TERMINATE"]
    ] = Field(default=None, alias="initiatedBy")
    participating_servers: Optional[List[ParticipatingServerModel]] = Field(
        default=None, alias="participatingServers"
    )
    status: Optional[Literal["COMPLETED", "PENDING", "STARTED"]] = Field(
        default=None, alias="status"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[Literal["LAUNCH", "TERMINATE"]] = Field(default=None, alias="type")


class DescribeJobsResponseModel(BaseModel):
    items: List[JobModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCutoverResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTestResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateTargetInstancesResponseModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
