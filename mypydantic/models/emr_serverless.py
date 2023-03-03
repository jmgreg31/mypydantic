# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    release_label: str = Field(alias="releaseLabel")
    type: str = Field(alias="type")
    state: Literal[
        "CREATED",
        "CREATING",
        "STARTED",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "TERMINATED",
    ] = Field(alias="state")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    name: Optional[str] = Field(default=None, alias="name")
    state_details: Optional[str] = Field(default=None, alias="stateDetails")
    architecture: Optional[Literal["ARM64", "X86_64"]] = Field(
        default=None, alias="architecture"
    )


class AutoStartConfigModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class AutoStopConfigModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    idle_timeout_minutes: Optional[int] = Field(
        default=None, alias="idleTimeoutMinutes"
    )


class ImageConfigurationModel(BaseModel):
    image_uri: str = Field(alias="imageUri")
    resolved_image_digest: Optional[str] = Field(
        default=None, alias="resolvedImageDigest"
    )


class MaximumAllowedResourcesModel(BaseModel):
    cpu: str = Field(alias="cpu")
    memory: str = Field(alias="memory")
    disk: Optional[str] = Field(default=None, alias="disk")


class NetworkConfigurationModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )


class CancelJobRunRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConfigurationModel(BaseModel):
    classification: str = Field(alias="classification")
    properties: Optional[Dict[str, str]] = Field(default=None, alias="properties")
    configurations: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="configurations"
    )


class ImageConfigurationInputModel(BaseModel):
    image_uri: Optional[str] = Field(default=None, alias="imageUri")


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class GetApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class GetDashboardForJobRunRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")


class GetJobRunRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")


class HiveModel(BaseModel):
    query: str = Field(alias="query")
    init_query_file: Optional[str] = Field(default=None, alias="initQueryFile")
    parameters: Optional[str] = Field(default=None, alias="parameters")


class WorkerResourceConfigModel(BaseModel):
    cpu: str = Field(alias="cpu")
    memory: str = Field(alias="memory")
    disk: Optional[str] = Field(default=None, alias="disk")


class SparkSubmitModel(BaseModel):
    entry_point: str = Field(alias="entryPoint")
    entry_point_arguments: Optional[List[str]] = Field(
        default=None, alias="entryPointArguments"
    )
    spark_submit_parameters: Optional[str] = Field(
        default=None, alias="sparkSubmitParameters"
    )


class JobRunSummaryModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    created_by: str = Field(alias="createdBy")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    execution_role: str = Field(alias="executionRole")
    state: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "SCHEDULED",
        "SUBMITTED",
        "SUCCESS",
    ] = Field(alias="state")
    state_details: str = Field(alias="stateDetails")
    release_label: str = Field(alias="releaseLabel")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")


class TotalResourceUtilizationModel(BaseModel):
    vcp_uhour: Optional[float] = Field(default=None, alias="vCPUHour")
    memory_gbhour: Optional[float] = Field(default=None, alias="memoryGBHour")
    storage_gbhour: Optional[float] = Field(default=None, alias="storageGBHour")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    states: Optional[
        Sequence[
            Literal[
                "CREATED",
                "CREATING",
                "STARTED",
                "STARTING",
                "STOPPED",
                "STOPPING",
                "TERMINATED",
            ]
        ]
    ] = Field(default=None, alias="states")


class ListJobRunsRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    created_at_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAtAfter"
    )
    created_at_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAtBefore"
    )
    states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCELLING",
                "FAILED",
                "PENDING",
                "RUNNING",
                "SCHEDULED",
                "SUBMITTED",
                "SUCCESS",
            ]
        ]
    ] = Field(default=None, alias="states")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ManagedPersistenceMonitoringConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    encryption_key_arn: Optional[str] = Field(default=None, alias="encryptionKeyArn")


class S3MonitoringConfigurationModel(BaseModel):
    log_uri: Optional[str] = Field(default=None, alias="logUri")
    encryption_key_arn: Optional[str] = Field(default=None, alias="encryptionKeyArn")


class StartApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class StopApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class WorkerTypeSpecificationModel(BaseModel):
    image_configuration: Optional[ImageConfigurationModel] = Field(
        default=None, alias="imageConfiguration"
    )


class CancelJobRunResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDashboardForJobRunResponseModel(BaseModel):
    url: str = Field(alias="url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    applications: List[ApplicationSummaryModel] = Field(alias="applications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartJobRunResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkerTypeSpecificationInputModel(BaseModel):
    image_configuration: Optional[ImageConfigurationInputModel] = Field(
        default=None, alias="imageConfiguration"
    )


class InitialCapacityConfigModel(BaseModel):
    worker_count: int = Field(alias="workerCount")
    worker_configuration: Optional[WorkerResourceConfigModel] = Field(
        default=None, alias="workerConfiguration"
    )


class JobDriverModel(BaseModel):
    spark_submit: Optional[SparkSubmitModel] = Field(default=None, alias="sparkSubmit")
    hive: Optional[HiveModel] = Field(default=None, alias="hive")


class ListJobRunsResponseModel(BaseModel):
    job_runs: List[JobRunSummaryModel] = Field(alias="jobRuns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    states: Optional[
        Sequence[
            Literal[
                "CREATED",
                "CREATING",
                "STARTED",
                "STARTING",
                "STOPPED",
                "STOPPING",
                "TERMINATED",
            ]
        ]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobRunsRequestListJobRunsPaginateModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    created_at_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAtAfter"
    )
    created_at_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAtBefore"
    )
    states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCELLING",
                "FAILED",
                "PENDING",
                "RUNNING",
                "SCHEDULED",
                "SUBMITTED",
                "SUCCESS",
            ]
        ]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MonitoringConfigurationModel(BaseModel):
    s3_monitoring_configuration: Optional[S3MonitoringConfigurationModel] = Field(
        default=None, alias="s3MonitoringConfiguration"
    )
    managed_persistence_monitoring_configuration: Optional[
        ManagedPersistenceMonitoringConfigurationModel
    ] = Field(default=None, alias="managedPersistenceMonitoringConfiguration")


class ApplicationModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    arn: str = Field(alias="arn")
    release_label: str = Field(alias="releaseLabel")
    type: str = Field(alias="type")
    state: Literal[
        "CREATED",
        "CREATING",
        "STARTED",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "TERMINATED",
    ] = Field(alias="state")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    name: Optional[str] = Field(default=None, alias="name")
    state_details: Optional[str] = Field(default=None, alias="stateDetails")
    initial_capacity: Optional[Dict[str, InitialCapacityConfigModel]] = Field(
        default=None, alias="initialCapacity"
    )
    maximum_capacity: Optional[MaximumAllowedResourcesModel] = Field(
        default=None, alias="maximumCapacity"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    auto_start_configuration: Optional[AutoStartConfigModel] = Field(
        default=None, alias="autoStartConfiguration"
    )
    auto_stop_configuration: Optional[AutoStopConfigModel] = Field(
        default=None, alias="autoStopConfiguration"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    architecture: Optional[Literal["ARM64", "X86_64"]] = Field(
        default=None, alias="architecture"
    )
    image_configuration: Optional[ImageConfigurationModel] = Field(
        default=None, alias="imageConfiguration"
    )
    worker_type_specifications: Optional[
        Dict[str, WorkerTypeSpecificationModel]
    ] = Field(default=None, alias="workerTypeSpecifications")


class CreateApplicationRequestModel(BaseModel):
    release_label: str = Field(alias="releaseLabel")
    type: str = Field(alias="type")
    client_token: str = Field(alias="clientToken")
    name: Optional[str] = Field(default=None, alias="name")
    initial_capacity: Optional[Mapping[str, InitialCapacityConfigModel]] = Field(
        default=None, alias="initialCapacity"
    )
    maximum_capacity: Optional[MaximumAllowedResourcesModel] = Field(
        default=None, alias="maximumCapacity"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    auto_start_configuration: Optional[AutoStartConfigModel] = Field(
        default=None, alias="autoStartConfiguration"
    )
    auto_stop_configuration: Optional[AutoStopConfigModel] = Field(
        default=None, alias="autoStopConfiguration"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    architecture: Optional[Literal["ARM64", "X86_64"]] = Field(
        default=None, alias="architecture"
    )
    image_configuration: Optional[ImageConfigurationInputModel] = Field(
        default=None, alias="imageConfiguration"
    )
    worker_type_specifications: Optional[
        Mapping[str, WorkerTypeSpecificationInputModel]
    ] = Field(default=None, alias="workerTypeSpecifications")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    client_token: str = Field(alias="clientToken")
    initial_capacity: Optional[Mapping[str, InitialCapacityConfigModel]] = Field(
        default=None, alias="initialCapacity"
    )
    maximum_capacity: Optional[MaximumAllowedResourcesModel] = Field(
        default=None, alias="maximumCapacity"
    )
    auto_start_configuration: Optional[AutoStartConfigModel] = Field(
        default=None, alias="autoStartConfiguration"
    )
    auto_stop_configuration: Optional[AutoStopConfigModel] = Field(
        default=None, alias="autoStopConfiguration"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    architecture: Optional[Literal["ARM64", "X86_64"]] = Field(
        default=None, alias="architecture"
    )
    image_configuration: Optional[ImageConfigurationInputModel] = Field(
        default=None, alias="imageConfiguration"
    )
    worker_type_specifications: Optional[
        Mapping[str, WorkerTypeSpecificationInputModel]
    ] = Field(default=None, alias="workerTypeSpecifications")


class ConfigurationOverridesModel(BaseModel):
    application_configuration: Optional[List[ConfigurationModel]] = Field(
        default=None, alias="applicationConfiguration"
    )
    monitoring_configuration: Optional[MonitoringConfigurationModel] = Field(
        default=None, alias="monitoringConfiguration"
    )


class GetApplicationResponseModel(BaseModel):
    application: ApplicationModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application: ApplicationModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobRunModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    job_run_id: str = Field(alias="jobRunId")
    arn: str = Field(alias="arn")
    created_by: str = Field(alias="createdBy")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    execution_role: str = Field(alias="executionRole")
    state: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "SCHEDULED",
        "SUBMITTED",
        "SUCCESS",
    ] = Field(alias="state")
    state_details: str = Field(alias="stateDetails")
    release_label: str = Field(alias="releaseLabel")
    job_driver: JobDriverModel = Field(alias="jobDriver")
    name: Optional[str] = Field(default=None, alias="name")
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    total_resource_utilization: Optional[TotalResourceUtilizationModel] = Field(
        default=None, alias="totalResourceUtilization"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    total_execution_duration_seconds: Optional[int] = Field(
        default=None, alias="totalExecutionDurationSeconds"
    )


class StartJobRunRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    client_token: str = Field(alias="clientToken")
    execution_role_arn: str = Field(alias="executionRoleArn")
    job_driver: Optional[JobDriverModel] = Field(default=None, alias="jobDriver")
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    execution_timeout_minutes: Optional[int] = Field(
        default=None, alias="executionTimeoutMinutes"
    )
    name: Optional[str] = Field(default=None, alias="name")


class GetJobRunResponseModel(BaseModel):
    job_run: JobRunModel = Field(alias="jobRun")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
