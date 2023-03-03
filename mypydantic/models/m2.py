# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlternateKeyModel(BaseModel):
    length: int = Field(alias="length")
    offset: int = Field(alias="offset")
    allow_duplicates: Optional[bool] = Field(default=None, alias="allowDuplicates")
    name: Optional[str] = Field(default=None, alias="name")


class ApplicationSummaryModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")
    creation_time: datetime = Field(alias="creationTime")
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    name: str = Field(alias="name")
    status: Literal[
        "Available",
        "Created",
        "Creating",
        "Deleting",
        "Deleting From Environment",
        "Failed",
        "Ready",
        "Running",
        "Starting",
        "Stopped",
        "Stopping",
    ] = Field(alias="status")
    deployment_status: Optional[Literal["Deployed", "Deploying"]] = Field(
        default=None, alias="deploymentStatus"
    )
    description: Optional[str] = Field(default=None, alias="description")
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    last_start_time: Optional[datetime] = Field(default=None, alias="lastStartTime")
    version_status: Optional[Literal["Available", "Creating", "Failed"]] = Field(
        default=None, alias="versionStatus"
    )


class ApplicationVersionSummaryModel(BaseModel):
    application_version: int = Field(alias="applicationVersion")
    creation_time: datetime = Field(alias="creationTime")
    status: Literal["Available", "Creating", "Failed"] = Field(alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class FileBatchJobDefinitionModel(BaseModel):
    file_name: str = Field(alias="fileName")
    folder_path: Optional[str] = Field(default=None, alias="folderPath")


class ScriptBatchJobDefinitionModel(BaseModel):
    script_name: str = Field(alias="scriptName")


class FileBatchJobIdentifierModel(BaseModel):
    file_name: str = Field(alias="fileName")
    folder_path: Optional[str] = Field(default=None, alias="folderPath")


class ScriptBatchJobIdentifierModel(BaseModel):
    script_name: str = Field(alias="scriptName")


class CancelBatchJobExecutionRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    execution_id: str = Field(alias="executionId")


class DefinitionModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    s3_location: Optional[str] = Field(default=None, alias="s3Location")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateDeploymentRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")
    environment_id: str = Field(alias="environmentId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class HighAvailabilityConfigModel(BaseModel):
    desired_capacity: int = Field(alias="desiredCapacity")


class ExternalLocationModel(BaseModel):
    s3_location: Optional[str] = Field(default=None, alias="s3Location")


class DataSetImportSummaryModel(BaseModel):
    failed: int = Field(alias="failed")
    in_progress: int = Field(alias="inProgress")
    pending: int = Field(alias="pending")
    succeeded: int = Field(alias="succeeded")
    total: int = Field(alias="total")


class DataSetSummaryModel(BaseModel):
    data_set_name: str = Field(alias="dataSetName")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    data_set_org: Optional[str] = Field(default=None, alias="dataSetOrg")
    format: Optional[str] = Field(default=None, alias="format")
    last_referenced_time: Optional[datetime] = Field(
        default=None, alias="lastReferencedTime"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")


class RecordLengthModel(BaseModel):
    max: int = Field(alias="max")
    min: int = Field(alias="min")


class GdgDetailAttributesModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="limit")
    roll_disposition: Optional[str] = Field(default=None, alias="rollDisposition")


class GdgAttributesModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="limit")
    roll_disposition: Optional[str] = Field(default=None, alias="rollDisposition")


class DeleteApplicationFromEnvironmentRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    environment_id: str = Field(alias="environmentId")


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class DeleteEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class DeployedVersionSummaryModel(BaseModel):
    application_version: int = Field(alias="applicationVersion")
    status: Literal["Deploying", "Failed", "Succeeded"] = Field(alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class DeploymentSummaryModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")
    creation_time: datetime = Field(alias="creationTime")
    deployment_id: str = Field(alias="deploymentId")
    environment_id: str = Field(alias="environmentId")
    status: Literal["Deploying", "Failed", "Succeeded"] = Field(alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class EfsStorageConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="fileSystemId")
    mount_point: str = Field(alias="mountPoint")


class EngineVersionsSummaryModel(BaseModel):
    engine_type: str = Field(alias="engineType")
    engine_version: str = Field(alias="engineVersion")


class EnvironmentSummaryModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    engine_version: str = Field(alias="engineVersion")
    environment_arn: str = Field(alias="environmentArn")
    environment_id: str = Field(alias="environmentId")
    instance_type: str = Field(alias="instanceType")
    name: str = Field(alias="name")
    status: Literal["Available", "Creating", "Deleting", "Failed", "Updating"] = Field(
        alias="status"
    )


class FsxStorageConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="fileSystemId")
    mount_point: str = Field(alias="mountPoint")


class GetApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class LogGroupSummaryModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    log_type: str = Field(alias="logType")


class GetApplicationVersionRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")


class GetBatchJobExecutionRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    execution_id: str = Field(alias="executionId")


class GetDataSetDetailsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    data_set_name: str = Field(alias="dataSetName")


class GetDataSetImportTaskRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    task_id: str = Field(alias="taskId")


class GetDeploymentRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    deployment_id: str = Field(alias="deploymentId")


class GetEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationVersionsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListApplicationsRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    names: Optional[Sequence[str]] = Field(default=None, alias="names")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBatchJobDefinitionsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class ListBatchJobExecutionsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    execution_ids: Optional[Sequence[str]] = Field(default=None, alias="executionIds")
    job_name: Optional[str] = Field(default=None, alias="jobName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="startedAfter"
    )
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="startedBefore"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Cancelling",
            "Dispatching",
            "Failed",
            "Holding",
            "Running",
            "Submitting",
            "Succeeded",
            "Succeeded With Warning",
        ]
    ] = Field(default=None, alias="status")


class ListDataSetImportHistoryRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDataSetsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class ListDeploymentsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEngineVersionsRequestModel(BaseModel):
    engine_type: Optional[Literal["bluage", "microfocus"]] = Field(
        default=None, alias="engineType"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEnvironmentsRequestModel(BaseModel):
    engine_type: Optional[Literal["bluage", "microfocus"]] = Field(
        default=None, alias="engineType"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    names: Optional[Sequence[str]] = Field(default=None, alias="names")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MaintenanceScheduleModel(BaseModel):
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")


class PrimaryKeyModel(BaseModel):
    length: int = Field(alias="length")
    offset: int = Field(alias="offset")
    name: Optional[str] = Field(default=None, alias="name")


class StartApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class StopApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    force_stop: Optional[bool] = Field(default=None, alias="forceStop")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    apply_during_maintenance_window: Optional[bool] = Field(
        default=None, alias="applyDuringMaintenanceWindow"
    )
    desired_capacity: Optional[int] = Field(default=None, alias="desiredCapacity")
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )


class BatchJobDefinitionModel(BaseModel):
    file_batch_job_definition: Optional[FileBatchJobDefinitionModel] = Field(
        default=None, alias="fileBatchJobDefinition"
    )
    script_batch_job_definition: Optional[ScriptBatchJobDefinitionModel] = Field(
        default=None, alias="scriptBatchJobDefinition"
    )


class BatchJobIdentifierModel(BaseModel):
    file_batch_job_identifier: Optional[FileBatchJobIdentifierModel] = Field(
        default=None, alias="fileBatchJobIdentifier"
    )
    script_batch_job_identifier: Optional[ScriptBatchJobIdentifierModel] = Field(
        default=None, alias="scriptBatchJobIdentifier"
    )


class CreateApplicationRequestModel(BaseModel):
    definition: DefinitionModel = Field(alias="definition")
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    current_application_version: int = Field(alias="currentApplicationVersion")
    definition: Optional[DefinitionModel] = Field(default=None, alias="definition")
    description: Optional[str] = Field(default=None, alias="description")


class CreateApplicationResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSetImportTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResponseModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentResponseModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationVersionResponseModel(BaseModel):
    application_version: int = Field(alias="applicationVersion")
    creation_time: datetime = Field(alias="creationTime")
    definition_content: str = Field(alias="definitionContent")
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    status: Literal["Available", "Creating", "Failed"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_version: int = Field(alias="applicationVersion")
    creation_time: datetime = Field(alias="creationTime")
    deployment_id: str = Field(alias="deploymentId")
    environment_id: str = Field(alias="environmentId")
    status: Literal["Deploying", "Failed", "Succeeded"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationVersionsResponseModel(BaseModel):
    application_versions: List[ApplicationVersionSummaryModel] = Field(
        alias="applicationVersions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    applications: List[ApplicationSummaryModel] = Field(alias="applications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBatchJobResponseModel(BaseModel):
    execution_id: str = Field(alias="executionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application_version: int = Field(alias="applicationVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentResponseModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSetImportTaskModel(BaseModel):
    status: Literal["Completed", "Creating", "Running"] = Field(alias="status")
    summary: DataSetImportSummaryModel = Field(alias="summary")
    task_id: str = Field(alias="taskId")


class GetDataSetImportTaskResponseModel(BaseModel):
    status: Literal["Completed", "Creating", "Running"] = Field(alias="status")
    summary: DataSetImportSummaryModel = Field(alias="summary")
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataSetsResponseModel(BaseModel):
    data_sets: List[DataSetSummaryModel] = Field(alias="dataSets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentsResponseModel(BaseModel):
    deployments: List[DeploymentSummaryModel] = Field(alias="deployments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEngineVersionsResponseModel(BaseModel):
    engine_versions: List[EngineVersionsSummaryModel] = Field(alias="engineVersions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsResponseModel(BaseModel):
    environments: List[EnvironmentSummaryModel] = Field(alias="environments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StorageConfigurationModel(BaseModel):
    efs: Optional[EfsStorageConfigurationModel] = Field(default=None, alias="efs")
    fsx: Optional[FsxStorageConfigurationModel] = Field(default=None, alias="fsx")


class GetApplicationResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    application_id: str = Field(alias="applicationId")
    creation_time: datetime = Field(alias="creationTime")
    deployed_version: DeployedVersionSummaryModel = Field(alias="deployedVersion")
    description: str = Field(alias="description")
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    environment_id: str = Field(alias="environmentId")
    kms_key_id: str = Field(alias="kmsKeyId")
    last_start_time: datetime = Field(alias="lastStartTime")
    latest_version: ApplicationVersionSummaryModel = Field(alias="latestVersion")
    listener_arns: List[str] = Field(alias="listenerArns")
    listener_ports: List[int] = Field(alias="listenerPorts")
    load_balancer_dns_name: str = Field(alias="loadBalancerDnsName")
    log_groups: List[LogGroupSummaryModel] = Field(alias="logGroups")
    name: str = Field(alias="name")
    status: Literal[
        "Available",
        "Created",
        "Creating",
        "Deleting",
        "Deleting From Environment",
        "Failed",
        "Ready",
        "Running",
        "Starting",
        "Stopped",
        "Stopping",
    ] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    tags: Dict[str, str] = Field(alias="tags")
    target_group_arns: List[str] = Field(alias="targetGroupArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationVersionsRequestListApplicationVersionsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    names: Optional[Sequence[str]] = Field(default=None, alias="names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBatchJobDefinitionsRequestListBatchJobDefinitionsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBatchJobExecutionsRequestListBatchJobExecutionsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    execution_ids: Optional[Sequence[str]] = Field(default=None, alias="executionIds")
    job_name: Optional[str] = Field(default=None, alias="jobName")
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="startedAfter"
    )
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="startedBefore"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Cancelling",
            "Dispatching",
            "Failed",
            "Holding",
            "Running",
            "Submitting",
            "Succeeded",
            "Succeeded With Warning",
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSetImportHistoryRequestListDataSetImportHistoryPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSetsRequestListDataSetsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentsRequestListDeploymentsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEngineVersionsRequestListEngineVersionsPaginateModel(BaseModel):
    engine_type: Optional[Literal["bluage", "microfocus"]] = Field(
        default=None, alias="engineType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentsRequestListEnvironmentsPaginateModel(BaseModel):
    engine_type: Optional[Literal["bluage", "microfocus"]] = Field(
        default=None, alias="engineType"
    )
    names: Optional[Sequence[str]] = Field(default=None, alias="names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PendingMaintenanceModel(BaseModel):
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    schedule: Optional[MaintenanceScheduleModel] = Field(default=None, alias="schedule")


class VsamAttributesModel(BaseModel):
    format: str = Field(alias="format")
    alternate_keys: Optional[Sequence[AlternateKeyModel]] = Field(
        default=None, alias="alternateKeys"
    )
    compressed: Optional[bool] = Field(default=None, alias="compressed")
    encoding: Optional[str] = Field(default=None, alias="encoding")
    primary_key: Optional[PrimaryKeyModel] = Field(default=None, alias="primaryKey")


class VsamDetailAttributesModel(BaseModel):
    alternate_keys: Optional[List[AlternateKeyModel]] = Field(
        default=None, alias="alternateKeys"
    )
    cache_at_startup: Optional[bool] = Field(default=None, alias="cacheAtStartup")
    compressed: Optional[bool] = Field(default=None, alias="compressed")
    encoding: Optional[str] = Field(default=None, alias="encoding")
    primary_key: Optional[PrimaryKeyModel] = Field(default=None, alias="primaryKey")
    record_format: Optional[str] = Field(default=None, alias="recordFormat")


class ListBatchJobDefinitionsResponseModel(BaseModel):
    batch_job_definitions: List[BatchJobDefinitionModel] = Field(
        alias="batchJobDefinitions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchJobExecutionSummaryModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    execution_id: str = Field(alias="executionId")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "Cancelled",
        "Cancelling",
        "Dispatching",
        "Failed",
        "Holding",
        "Running",
        "Submitting",
        "Succeeded",
        "Succeeded With Warning",
    ] = Field(alias="status")
    batch_job_identifier: Optional[BatchJobIdentifierModel] = Field(
        default=None, alias="batchJobIdentifier"
    )
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    job_name: Optional[str] = Field(default=None, alias="jobName")
    job_type: Optional[Literal["JES2", "JES3", "VSE"]] = Field(
        default=None, alias="jobType"
    )
    return_code: Optional[str] = Field(default=None, alias="returnCode")


class GetBatchJobExecutionResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    batch_job_identifier: BatchJobIdentifierModel = Field(alias="batchJobIdentifier")
    end_time: datetime = Field(alias="endTime")
    execution_id: str = Field(alias="executionId")
    job_id: str = Field(alias="jobId")
    job_name: str = Field(alias="jobName")
    job_type: Literal["JES2", "JES3", "VSE"] = Field(alias="jobType")
    job_user: str = Field(alias="jobUser")
    return_code: str = Field(alias="returnCode")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "Cancelled",
        "Cancelling",
        "Dispatching",
        "Failed",
        "Holding",
        "Running",
        "Submitting",
        "Succeeded",
        "Succeeded With Warning",
    ] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBatchJobRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    batch_job_identifier: BatchJobIdentifierModel = Field(alias="batchJobIdentifier")
    job_params: Optional[Mapping[str, str]] = Field(default=None, alias="jobParams")


class ListDataSetImportHistoryResponseModel(BaseModel):
    data_set_import_tasks: List[DataSetImportTaskModel] = Field(
        alias="dataSetImportTasks"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentRequestModel(BaseModel):
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    instance_type: str = Field(alias="instanceType")
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    high_availability_config: Optional[HighAvailabilityConfigModel] = Field(
        default=None, alias="highAvailabilityConfig"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    storage_configurations: Optional[Sequence[StorageConfigurationModel]] = Field(
        default=None, alias="storageConfigurations"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetEnvironmentResponseModel(BaseModel):
    actual_capacity: int = Field(alias="actualCapacity")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    engine_type: Literal["bluage", "microfocus"] = Field(alias="engineType")
    engine_version: str = Field(alias="engineVersion")
    environment_arn: str = Field(alias="environmentArn")
    environment_id: str = Field(alias="environmentId")
    high_availability_config: HighAvailabilityConfigModel = Field(
        alias="highAvailabilityConfig"
    )
    instance_type: str = Field(alias="instanceType")
    kms_key_id: str = Field(alias="kmsKeyId")
    load_balancer_arn: str = Field(alias="loadBalancerArn")
    name: str = Field(alias="name")
    pending_maintenance: PendingMaintenanceModel = Field(alias="pendingMaintenance")
    preferred_maintenance_window: str = Field(alias="preferredMaintenanceWindow")
    publicly_accessible: bool = Field(alias="publiclyAccessible")
    security_group_ids: List[str] = Field(alias="securityGroupIds")
    status: Literal["Available", "Creating", "Deleting", "Failed", "Updating"] = Field(
        alias="status"
    )
    status_reason: str = Field(alias="statusReason")
    storage_configurations: List[StorageConfigurationModel] = Field(
        alias="storageConfigurations"
    )
    subnet_ids: List[str] = Field(alias="subnetIds")
    tags: Dict[str, str] = Field(alias="tags")
    vpc_id: str = Field(alias="vpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasetOrgAttributesModel(BaseModel):
    gdg: Optional[GdgAttributesModel] = Field(default=None, alias="gdg")
    vsam: Optional[VsamAttributesModel] = Field(default=None, alias="vsam")


class DatasetDetailOrgAttributesModel(BaseModel):
    gdg: Optional[GdgDetailAttributesModel] = Field(default=None, alias="gdg")
    vsam: Optional[VsamDetailAttributesModel] = Field(default=None, alias="vsam")


class ListBatchJobExecutionsResponseModel(BaseModel):
    batch_job_executions: List[BatchJobExecutionSummaryModel] = Field(
        alias="batchJobExecutions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSetModel(BaseModel):
    dataset_name: str = Field(alias="datasetName")
    dataset_org: DatasetOrgAttributesModel = Field(alias="datasetOrg")
    record_length: RecordLengthModel = Field(alias="recordLength")
    relative_path: Optional[str] = Field(default=None, alias="relativePath")
    storage_type: Optional[str] = Field(default=None, alias="storageType")


class GetDataSetDetailsResponseModel(BaseModel):
    blocksize: int = Field(alias="blocksize")
    creation_time: datetime = Field(alias="creationTime")
    data_set_name: str = Field(alias="dataSetName")
    data_set_org: DatasetDetailOrgAttributesModel = Field(alias="dataSetOrg")
    last_referenced_time: datetime = Field(alias="lastReferencedTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    location: str = Field(alias="location")
    record_length: int = Field(alias="recordLength")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSetImportItemModel(BaseModel):
    data_set: DataSetModel = Field(alias="dataSet")
    external_location: ExternalLocationModel = Field(alias="externalLocation")


class DataSetImportConfigModel(BaseModel):
    data_sets: Optional[Sequence[DataSetImportItemModel]] = Field(
        default=None, alias="dataSets"
    )
    s3_location: Optional[str] = Field(default=None, alias="s3Location")


class CreateDataSetImportTaskRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    import_config: DataSetImportConfigModel = Field(alias="importConfig")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
