# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class LaunchDetailsModel(BaseModel):
    latest_launch_time: Optional[datetime] = Field(
        default=None, alias="latestLaunchTime"
    )
    stack_name: Optional[str] = Field(default=None, alias="stackName")
    stack_id: Optional[str] = Field(default=None, alias="stackId")


class ConnectorModel(BaseModel):
    connector_id: Optional[str] = Field(default=None, alias="connectorId")
    version: Optional[str] = Field(default=None, alias="version")
    status: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="status"
    )
    capability_list: Optional[
        List[
            Literal[
                "HYPERV-MANAGER",
                "SCVMM",
                "SMS_OPTIMIZED",
                "SNAPSHOT_BATCHING",
                "VSPHERE",
            ]
        ]
    ] = Field(default=None, alias="capabilityList")
    vm_manager_name: Optional[str] = Field(default=None, alias="vmManagerName")
    vm_manager_type: Optional[Literal["HYPERV-MANAGER", "SCVMM", "VSPHERE"]] = Field(
        default=None, alias="vmManagerType"
    )
    vm_manager_id: Optional[str] = Field(default=None, alias="vmManagerId")
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    mac_address: Optional[str] = Field(default=None, alias="macAddress")
    associated_on: Optional[datetime] = Field(default=None, alias="associatedOn")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateReplicationJobRequestModel(BaseModel):
    server_id: str = Field(alias="serverId")
    seed_replication_time: Union[datetime, str] = Field(alias="seedReplicationTime")
    frequency: Optional[int] = Field(default=None, alias="frequency")
    run_once: Optional[bool] = Field(default=None, alias="runOnce")
    license_type: Optional[Literal["AWS", "BYOL"]] = Field(
        default=None, alias="licenseType"
    )
    role_name: Optional[str] = Field(default=None, alias="roleName")
    description: Optional[str] = Field(default=None, alias="description")
    number_of_recent_amis_to_keep: Optional[int] = Field(
        default=None, alias="numberOfRecentAmisToKeep"
    )
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class DeleteAppLaunchConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class DeleteAppReplicationConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class DeleteAppRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    force_stop_app_replication: Optional[bool] = Field(
        default=None, alias="forceStopAppReplication"
    )
    force_terminate_app: Optional[bool] = Field(default=None, alias="forceTerminateApp")


class DeleteAppValidationConfigurationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")


class DeleteReplicationJobRequestModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")


class DisassociateConnectorRequestModel(BaseModel):
    connector_id: str = Field(alias="connectorId")


class GenerateChangeSetRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    changeset_format: Optional[Literal["JSON", "YAML"]] = Field(
        default=None, alias="changesetFormat"
    )


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")


class GenerateTemplateRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    template_format: Optional[Literal["JSON", "YAML"]] = Field(
        default=None, alias="templateFormat"
    )


class GetAppLaunchConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class GetAppReplicationConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class GetAppRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class GetAppValidationConfigurationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")


class GetAppValidationOutputRequestModel(BaseModel):
    app_id: str = Field(alias="appId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetConnectorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetReplicationJobsRequestModel(BaseModel):
    replication_job_id: Optional[str] = Field(default=None, alias="replicationJobId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetReplicationRunsRequestModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class VmServerAddressModel(BaseModel):
    vm_manager_id: Optional[str] = Field(default=None, alias="vmManagerId")
    vm_id: Optional[str] = Field(default=None, alias="vmId")


class ImportAppCatalogRequestModel(BaseModel):
    role_name: Optional[str] = Field(default=None, alias="roleName")


class LaunchAppRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class ListAppsRequestModel(BaseModel):
    app_ids: Optional[Sequence[str]] = Field(default=None, alias="appIds")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class NotificationContextModel(BaseModel):
    validation_id: Optional[str] = Field(default=None, alias="validationId")
    status: Optional[
        Literal["FAILED", "IN_PROGRESS", "PENDING", "READY_FOR_VALIDATION", "SUCCEEDED"]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ReplicationRunStageDetailsModel(BaseModel):
    stage: Optional[str] = Field(default=None, alias="stage")
    stage_progress: Optional[str] = Field(default=None, alias="stageProgress")


class ServerReplicationParametersModel(BaseModel):
    seed_time: Optional[datetime] = Field(default=None, alias="seedTime")
    frequency: Optional[int] = Field(default=None, alias="frequency")
    run_once: Optional[bool] = Field(default=None, alias="runOnce")
    license_type: Optional[Literal["AWS", "BYOL"]] = Field(
        default=None, alias="licenseType"
    )
    number_of_recent_amis_to_keep: Optional[int] = Field(
        default=None, alias="numberOfRecentAmisToKeep"
    )
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class StartAppReplicationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class StartOnDemandAppReplicationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    description: Optional[str] = Field(default=None, alias="description")


class StartOnDemandReplicationRunRequestModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")
    description: Optional[str] = Field(default=None, alias="description")


class StopAppReplicationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class TerminateAppRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")


class UpdateReplicationJobRequestModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")
    frequency: Optional[int] = Field(default=None, alias="frequency")
    next_replication_run_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="nextReplicationRunStartTime"
    )
    license_type: Optional[Literal["AWS", "BYOL"]] = Field(
        default=None, alias="licenseType"
    )
    role_name: Optional[str] = Field(default=None, alias="roleName")
    description: Optional[str] = Field(default=None, alias="description")
    number_of_recent_amis_to_keep: Optional[int] = Field(
        default=None, alias="numberOfRecentAmisToKeep"
    )
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class AppSummaryModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    imported_app_id: Optional[str] = Field(default=None, alias="importedAppId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[
        Literal[
            "ACTIVE", "CREATING", "DELETED", "DELETE_FAILED", "DELETING", "UPDATING"
        ]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    replication_configuration_status: Optional[
        Literal["CONFIGURED", "NOT_CONFIGURED"]
    ] = Field(default=None, alias="replicationConfigurationStatus")
    replication_status: Optional[
        Literal[
            "CONFIGURATION_INVALID",
            "CONFIGURATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "PARTIALLY_REPLICATED",
            "READY_FOR_CONFIGURATION",
            "READY_FOR_REPLICATION",
            "REPLICATED",
            "REPLICATION_FAILED",
            "REPLICATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_STOPPED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "VALIDATION_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="replicationStatus")
    replication_status_message: Optional[str] = Field(
        default=None, alias="replicationStatusMessage"
    )
    latest_replication_time: Optional[datetime] = Field(
        default=None, alias="latestReplicationTime"
    )
    launch_configuration_status: Optional[
        Literal["CONFIGURED", "NOT_CONFIGURED"]
    ] = Field(default=None, alias="launchConfigurationStatus")
    launch_status: Optional[
        Literal[
            "CONFIGURATION_INVALID",
            "CONFIGURATION_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "LAUNCH_FAILED",
            "LAUNCH_IN_PROGRESS",
            "LAUNCH_PENDING",
            "PARTIALLY_LAUNCHED",
            "READY_FOR_CONFIGURATION",
            "READY_FOR_LAUNCH",
            "TERMINATED",
            "TERMINATE_FAILED",
            "TERMINATE_IN_PROGRESS",
            "VALIDATION_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="launchStatus")
    launch_status_message: Optional[str] = Field(
        default=None, alias="launchStatusMessage"
    )
    launch_details: Optional[LaunchDetailsModel] = Field(
        default=None, alias="launchDetails"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_modified: Optional[datetime] = Field(default=None, alias="lastModified")
    role_name: Optional[str] = Field(default=None, alias="roleName")
    total_server_groups: Optional[int] = Field(default=None, alias="totalServerGroups")
    total_servers: Optional[int] = Field(default=None, alias="totalServers")


class CreateReplicationJobResponseModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectorsResponseModel(BaseModel):
    connector_list: List[ConnectorModel] = Field(alias="connectorList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartOnDemandReplicationRunResponseModel(BaseModel):
    replication_run_id: str = Field(alias="replicationRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateChangeSetResponseModel(BaseModel):
    s3_location: S3LocationModel = Field(alias="s3Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateTemplateResponseModel(BaseModel):
    s3_location: S3LocationModel = Field(alias="s3Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SSMOutputModel(BaseModel):
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")


class SourceModel(BaseModel):
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")


class UserDataModel(BaseModel):
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")


class GetConnectorsRequestGetConnectorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReplicationJobsRequestGetReplicationJobsPaginateModel(BaseModel):
    replication_job_id: Optional[str] = Field(default=None, alias="replicationJobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReplicationRunsRequestGetReplicationRunsPaginateModel(BaseModel):
    replication_job_id: str = Field(alias="replicationJobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAppsRequestListAppsPaginateModel(BaseModel):
    app_ids: Optional[Sequence[str]] = Field(default=None, alias="appIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetServersRequestGetServersPaginateModel(BaseModel):
    vm_server_address_list: Optional[Sequence[VmServerAddressModel]] = Field(
        default=None, alias="vmServerAddressList"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetServersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    vm_server_address_list: Optional[Sequence[VmServerAddressModel]] = Field(
        default=None, alias="vmServerAddressList"
    )


class VmServerModel(BaseModel):
    vm_server_address: Optional[VmServerAddressModel] = Field(
        default=None, alias="vmServerAddress"
    )
    vm_name: Optional[str] = Field(default=None, alias="vmName")
    vm_manager_name: Optional[str] = Field(default=None, alias="vmManagerName")
    vm_manager_type: Optional[Literal["HYPERV-MANAGER", "SCVMM", "VSPHERE"]] = Field(
        default=None, alias="vmManagerType"
    )
    vm_path: Optional[str] = Field(default=None, alias="vmPath")


class NotifyAppValidationOutputRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    notification_context: Optional[NotificationContextModel] = Field(
        default=None, alias="notificationContext"
    )


class ReplicationRunModel(BaseModel):
    replication_run_id: Optional[str] = Field(default=None, alias="replicationRunId")
    state: Optional[
        Literal[
            "ACTIVE", "COMPLETED", "DELETED", "DELETING", "FAILED", "MISSED", "PENDING"
        ]
    ] = Field(default=None, alias="state")
    type: Optional[Literal["AUTOMATIC", "ON_DEMAND"]] = Field(
        default=None, alias="type"
    )
    stage_details: Optional[ReplicationRunStageDetailsModel] = Field(
        default=None, alias="stageDetails"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    ami_id: Optional[str] = Field(default=None, alias="amiId")
    scheduled_start_time: Optional[datetime] = Field(
        default=None, alias="scheduledStartTime"
    )
    completed_time: Optional[datetime] = Field(default=None, alias="completedTime")
    description: Optional[str] = Field(default=None, alias="description")
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class ListAppsResponseModel(BaseModel):
    apps: List[AppSummaryModel] = Field(alias="apps")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AppValidationOutputModel(BaseModel):
    ssm_output: Optional[SSMOutputModel] = Field(default=None, alias="ssmOutput")


class SSMValidationParametersModel(BaseModel):
    source: Optional[SourceModel] = Field(default=None, alias="source")
    instance_id: Optional[str] = Field(default=None, alias="instanceId")
    script_type: Optional[Literal["POWERSHELL_SCRIPT", "SHELL_SCRIPT"]] = Field(
        default=None, alias="scriptType"
    )
    command: Optional[str] = Field(default=None, alias="command")
    execution_timeout_seconds: Optional[int] = Field(
        default=None, alias="executionTimeoutSeconds"
    )
    output_s3_bucket_name: Optional[str] = Field(
        default=None, alias="outputS3BucketName"
    )


class UserDataValidationParametersModel(BaseModel):
    source: Optional[SourceModel] = Field(default=None, alias="source")
    script_type: Optional[Literal["POWERSHELL_SCRIPT", "SHELL_SCRIPT"]] = Field(
        default=None, alias="scriptType"
    )


class ServerModel(BaseModel):
    server_id: Optional[str] = Field(default=None, alias="serverId")
    server_type: Optional[Literal["VIRTUAL_MACHINE"]] = Field(
        default=None, alias="serverType"
    )
    vm_server: Optional[VmServerModel] = Field(default=None, alias="vmServer")
    replication_job_id: Optional[str] = Field(default=None, alias="replicationJobId")
    replication_job_terminated: Optional[bool] = Field(
        default=None, alias="replicationJobTerminated"
    )


class ReplicationJobModel(BaseModel):
    replication_job_id: Optional[str] = Field(default=None, alias="replicationJobId")
    server_id: Optional[str] = Field(default=None, alias="serverId")
    server_type: Optional[Literal["VIRTUAL_MACHINE"]] = Field(
        default=None, alias="serverType"
    )
    vm_server: Optional[VmServerModel] = Field(default=None, alias="vmServer")
    seed_replication_time: Optional[datetime] = Field(
        default=None, alias="seedReplicationTime"
    )
    frequency: Optional[int] = Field(default=None, alias="frequency")
    run_once: Optional[bool] = Field(default=None, alias="runOnce")
    next_replication_run_start_time: Optional[datetime] = Field(
        default=None, alias="nextReplicationRunStartTime"
    )
    license_type: Optional[Literal["AWS", "BYOL"]] = Field(
        default=None, alias="licenseType"
    )
    role_name: Optional[str] = Field(default=None, alias="roleName")
    latest_ami_id: Optional[str] = Field(default=None, alias="latestAmiId")
    state: Optional[
        Literal[
            "ACTIVE",
            "COMPLETED",
            "DELETED",
            "DELETING",
            "FAILED",
            "FAILING",
            "PAUSED_ON_FAILURE",
            "PENDING",
        ]
    ] = Field(default=None, alias="state")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    description: Optional[str] = Field(default=None, alias="description")
    number_of_recent_amis_to_keep: Optional[int] = Field(
        default=None, alias="numberOfRecentAmisToKeep"
    )
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    replication_run_list: Optional[List[ReplicationRunModel]] = Field(
        default=None, alias="replicationRunList"
    )


class AppValidationConfigurationModel(BaseModel):
    validation_id: Optional[str] = Field(default=None, alias="validationId")
    name: Optional[str] = Field(default=None, alias="name")
    app_validation_strategy: Optional[Literal["SSM"]] = Field(
        default=None, alias="appValidationStrategy"
    )
    ssm_validation_parameters: Optional[SSMValidationParametersModel] = Field(
        default=None, alias="ssmValidationParameters"
    )


class GetServersResponseModel(BaseModel):
    last_modified_on: datetime = Field(alias="lastModifiedOn")
    server_catalog_status: Literal[
        "AVAILABLE", "DELETED", "EXPIRED", "IMPORTING", "NOT_IMPORTED"
    ] = Field(alias="serverCatalogStatus")
    server_list: List[ServerModel] = Field(alias="serverList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServerGroupModel(BaseModel):
    server_group_id: Optional[str] = Field(default=None, alias="serverGroupId")
    name: Optional[str] = Field(default=None, alias="name")
    server_list: Optional[Sequence[ServerModel]] = Field(
        default=None, alias="serverList"
    )


class ServerLaunchConfigurationModel(BaseModel):
    server: Optional[ServerModel] = Field(default=None, alias="server")
    logical_id: Optional[str] = Field(default=None, alias="logicalId")
    vpc: Optional[str] = Field(default=None, alias="vpc")
    subnet: Optional[str] = Field(default=None, alias="subnet")
    security_group: Optional[str] = Field(default=None, alias="securityGroup")
    ec2_key_name: Optional[str] = Field(default=None, alias="ec2KeyName")
    user_data: Optional[UserDataModel] = Field(default=None, alias="userData")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="associatePublicIpAddress"
    )
    iam_instance_profile_name: Optional[str] = Field(
        default=None, alias="iamInstanceProfileName"
    )
    configure_script: Optional[S3LocationModel] = Field(
        default=None, alias="configureScript"
    )
    configure_script_type: Optional[
        Literal["POWERSHELL_SCRIPT", "SHELL_SCRIPT"]
    ] = Field(default=None, alias="configureScriptType")


class ServerReplicationConfigurationModel(BaseModel):
    server: Optional[ServerModel] = Field(default=None, alias="server")
    server_replication_parameters: Optional[ServerReplicationParametersModel] = Field(
        default=None, alias="serverReplicationParameters"
    )


class ServerValidationConfigurationModel(BaseModel):
    server: Optional[ServerModel] = Field(default=None, alias="server")
    validation_id: Optional[str] = Field(default=None, alias="validationId")
    name: Optional[str] = Field(default=None, alias="name")
    server_validation_strategy: Optional[Literal["USERDATA"]] = Field(
        default=None, alias="serverValidationStrategy"
    )
    user_data_validation_parameters: Optional[
        UserDataValidationParametersModel
    ] = Field(default=None, alias="userDataValidationParameters")


class ServerValidationOutputModel(BaseModel):
    server: Optional[ServerModel] = Field(default=None, alias="server")


class GetReplicationJobsResponseModel(BaseModel):
    replication_job_list: List[ReplicationJobModel] = Field(alias="replicationJobList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReplicationRunsResponseModel(BaseModel):
    replication_job: ReplicationJobModel = Field(alias="replicationJob")
    replication_run_list: List[ReplicationRunModel] = Field(alias="replicationRunList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    role_name: Optional[str] = Field(default=None, alias="roleName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    server_groups: Optional[Sequence[ServerGroupModel]] = Field(
        default=None, alias="serverGroups"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateAppResponseModel(BaseModel):
    app_summary: AppSummaryModel = Field(alias="appSummary")
    server_groups: List[ServerGroupModel] = Field(alias="serverGroups")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppResponseModel(BaseModel):
    app_summary: AppSummaryModel = Field(alias="appSummary")
    server_groups: List[ServerGroupModel] = Field(alias="serverGroups")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    role_name: Optional[str] = Field(default=None, alias="roleName")
    server_groups: Optional[Sequence[ServerGroupModel]] = Field(
        default=None, alias="serverGroups"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateAppResponseModel(BaseModel):
    app_summary: AppSummaryModel = Field(alias="appSummary")
    server_groups: List[ServerGroupModel] = Field(alias="serverGroups")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServerGroupLaunchConfigurationModel(BaseModel):
    server_group_id: Optional[str] = Field(default=None, alias="serverGroupId")
    launch_order: Optional[int] = Field(default=None, alias="launchOrder")
    server_launch_configurations: Optional[
        List[ServerLaunchConfigurationModel]
    ] = Field(default=None, alias="serverLaunchConfigurations")


class ServerGroupReplicationConfigurationModel(BaseModel):
    server_group_id: Optional[str] = Field(default=None, alias="serverGroupId")
    server_replication_configurations: Optional[
        List[ServerReplicationConfigurationModel]
    ] = Field(default=None, alias="serverReplicationConfigurations")


class ServerGroupValidationConfigurationModel(BaseModel):
    server_group_id: Optional[str] = Field(default=None, alias="serverGroupId")
    server_validation_configurations: Optional[
        List[ServerValidationConfigurationModel]
    ] = Field(default=None, alias="serverValidationConfigurations")


class ValidationOutputModel(BaseModel):
    validation_id: Optional[str] = Field(default=None, alias="validationId")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[
        Literal["FAILED", "IN_PROGRESS", "PENDING", "READY_FOR_VALIDATION", "SUCCEEDED"]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    latest_validation_time: Optional[datetime] = Field(
        default=None, alias="latestValidationTime"
    )
    app_validation_output: Optional[AppValidationOutputModel] = Field(
        default=None, alias="appValidationOutput"
    )
    server_validation_output: Optional[ServerValidationOutputModel] = Field(
        default=None, alias="serverValidationOutput"
    )


class GetAppLaunchConfigurationResponseModel(BaseModel):
    app_id: str = Field(alias="appId")
    role_name: str = Field(alias="roleName")
    auto_launch: bool = Field(alias="autoLaunch")
    server_group_launch_configurations: List[
        ServerGroupLaunchConfigurationModel
    ] = Field(alias="serverGroupLaunchConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppLaunchConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    role_name: Optional[str] = Field(default=None, alias="roleName")
    auto_launch: Optional[bool] = Field(default=None, alias="autoLaunch")
    server_group_launch_configurations: Optional[
        Sequence[ServerGroupLaunchConfigurationModel]
    ] = Field(default=None, alias="serverGroupLaunchConfigurations")


class GetAppReplicationConfigurationResponseModel(BaseModel):
    server_group_replication_configurations: List[
        ServerGroupReplicationConfigurationModel
    ] = Field(alias="serverGroupReplicationConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppReplicationConfigurationRequestModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="appId")
    server_group_replication_configurations: Optional[
        Sequence[ServerGroupReplicationConfigurationModel]
    ] = Field(default=None, alias="serverGroupReplicationConfigurations")


class GetAppValidationConfigurationResponseModel(BaseModel):
    app_validation_configurations: List[AppValidationConfigurationModel] = Field(
        alias="appValidationConfigurations"
    )
    server_group_validation_configurations: List[
        ServerGroupValidationConfigurationModel
    ] = Field(alias="serverGroupValidationConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppValidationConfigurationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    app_validation_configurations: Optional[
        Sequence[AppValidationConfigurationModel]
    ] = Field(default=None, alias="appValidationConfigurations")
    server_group_validation_configurations: Optional[
        Sequence[ServerGroupValidationConfigurationModel]
    ] = Field(default=None, alias="serverGroupValidationConfigurations")


class GetAppValidationOutputResponseModel(BaseModel):
    validation_output_list: List[ValidationOutputModel] = Field(
        alias="validationOutputList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
