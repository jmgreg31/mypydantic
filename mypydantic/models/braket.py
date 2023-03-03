# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ContainerImageModel(BaseModel):
    uri: str = Field(alias="uri")


class ScriptModeConfigModel(BaseModel):
    entry_point: str = Field(alias="entryPoint")
    s3_uri: str = Field(alias="s3Uri")
    compression_type: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="compressionType"
    )


class CancelJobRequestModel(BaseModel):
    job_arn: str = Field(alias="jobArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CancelQuantumTaskRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    quantum_task_arn: str = Field(alias="quantumTaskArn")


class DeviceConfigModel(BaseModel):
    device: str = Field(alias="device")


class InstanceConfigModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5n.18xlarge",
        "ml.c5n.2xlarge",
        "ml.c5n.4xlarge",
        "ml.c5n.9xlarge",
        "ml.c5n.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.p4d.24xlarge",
    ] = Field(alias="instanceType")
    volume_size_in_gb: int = Field(alias="volumeSizeInGb")
    instance_count: Optional[int] = Field(default=None, alias="instanceCount")


class JobCheckpointConfigModel(BaseModel):
    s3_uri: str = Field(alias="s3Uri")
    local_path: Optional[str] = Field(default=None, alias="localPath")


class JobOutputDataConfigModel(BaseModel):
    s3_path: str = Field(alias="s3Path")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class JobStoppingConditionModel(BaseModel):
    max_runtime_in_seconds: Optional[int] = Field(
        default=None, alias="maxRuntimeInSeconds"
    )


class CreateQuantumTaskRequestModel(BaseModel):
    action: str = Field(alias="action")
    client_token: str = Field(alias="clientToken")
    device_arn: str = Field(alias="deviceArn")
    output_s3_bucket: str = Field(alias="outputS3Bucket")
    output_s3_key_prefix: str = Field(alias="outputS3KeyPrefix")
    shots: int = Field(alias="shots")
    device_parameters: Optional[str] = Field(default=None, alias="deviceParameters")
    job_token: Optional[str] = Field(default=None, alias="jobToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class S3DataSourceModel(BaseModel):
    s3_uri: str = Field(alias="s3Uri")


class DeviceSummaryModel(BaseModel):
    device_arn: str = Field(alias="deviceArn")
    device_name: str = Field(alias="deviceName")
    device_status: Literal["OFFLINE", "ONLINE", "RETIRED"] = Field(alias="deviceStatus")
    device_type: Literal["QPU", "SIMULATOR"] = Field(alias="deviceType")
    provider_name: str = Field(alias="providerName")


class GetDeviceRequestModel(BaseModel):
    device_arn: str = Field(alias="deviceArn")


class GetJobRequestModel(BaseModel):
    job_arn: str = Field(alias="jobArn")


class JobEventDetailsModel(BaseModel):
    event_type: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "DEPRIORITIZED_DUE_TO_INACTIVITY",
            "DOWNLOADING_DATA",
            "FAILED",
            "MAX_RUNTIME_EXCEEDED",
            "QUEUED_FOR_EXECUTION",
            "RUNNING",
            "STARTING_INSTANCE",
            "UPLOADING_RESULTS",
            "WAITING_FOR_PRIORITY",
        ]
    ] = Field(default=None, alias="eventType")
    message: Optional[str] = Field(default=None, alias="message")
    time_of_event: Optional[datetime] = Field(default=None, alias="timeOfEvent")


class GetQuantumTaskRequestModel(BaseModel):
    quantum_task_arn: str = Field(alias="quantumTaskArn")


class JobSummaryModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    device: str = Field(alias="device")
    job_arn: str = Field(alias="jobArn")
    job_name: str = Field(alias="jobName")
    status: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "QUEUED", "RUNNING"
    ] = Field(alias="status")
    ended_at: Optional[datetime] = Field(default=None, alias="endedAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class QuantumTaskSummaryModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    device_arn: str = Field(alias="deviceArn")
    output_s3_bucket: str = Field(alias="outputS3Bucket")
    output_s3_directory: str = Field(alias="outputS3Directory")
    quantum_task_arn: str = Field(alias="quantumTaskArn")
    shots: int = Field(alias="shots")
    status: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "CREATED", "FAILED", "QUEUED", "RUNNING"
    ] = Field(alias="status")
    ended_at: Optional[datetime] = Field(default=None, alias="endedAt")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class SearchDevicesFilterModel(BaseModel):
    name: str = Field(alias="name")
    values: Sequence[str] = Field(alias="values")


class SearchJobsFilterModel(BaseModel):
    name: str = Field(alias="name")
    operator: Literal["BETWEEN", "CONTAINS", "EQUAL", "GT", "GTE", "LT", "LTE"] = Field(
        alias="operator"
    )
    values: Sequence[str] = Field(alias="values")


class SearchQuantumTasksFilterModel(BaseModel):
    name: str = Field(alias="name")
    operator: Literal["BETWEEN", "EQUAL", "GT", "GTE", "LT", "LTE"] = Field(
        alias="operator"
    )
    values: Sequence[str] = Field(alias="values")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AlgorithmSpecificationModel(BaseModel):
    container_image: Optional[ContainerImageModel] = Field(
        default=None, alias="containerImage"
    )
    script_mode_config: Optional[ScriptModeConfigModel] = Field(
        default=None, alias="scriptModeConfig"
    )


class CancelJobResponseModel(BaseModel):
    cancellation_status: Literal["CANCELLED", "CANCELLING"] = Field(
        alias="cancellationStatus"
    )
    job_arn: str = Field(alias="jobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelQuantumTaskResponseModel(BaseModel):
    cancellation_status: Literal["CANCELLED", "CANCELLING"] = Field(
        alias="cancellationStatus"
    )
    quantum_task_arn: str = Field(alias="quantumTaskArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQuantumTaskResponseModel(BaseModel):
    quantum_task_arn: str = Field(alias="quantumTaskArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceResponseModel(BaseModel):
    device_arn: str = Field(alias="deviceArn")
    device_capabilities: str = Field(alias="deviceCapabilities")
    device_name: str = Field(alias="deviceName")
    device_status: Literal["OFFLINE", "ONLINE", "RETIRED"] = Field(alias="deviceStatus")
    device_type: Literal["QPU", "SIMULATOR"] = Field(alias="deviceType")
    provider_name: str = Field(alias="providerName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQuantumTaskResponseModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    device_arn: str = Field(alias="deviceArn")
    device_parameters: str = Field(alias="deviceParameters")
    ended_at: datetime = Field(alias="endedAt")
    failure_reason: str = Field(alias="failureReason")
    job_arn: str = Field(alias="jobArn")
    output_s3_bucket: str = Field(alias="outputS3Bucket")
    output_s3_directory: str = Field(alias="outputS3Directory")
    quantum_task_arn: str = Field(alias="quantumTaskArn")
    shots: int = Field(alias="shots")
    status: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "CREATED", "FAILED", "QUEUED", "RUNNING"
    ] = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSourceModel(BaseModel):
    s3_data_source: S3DataSourceModel = Field(alias="s3DataSource")


class SearchDevicesResponseModel(BaseModel):
    devices: List[DeviceSummaryModel] = Field(alias="devices")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchJobsResponseModel(BaseModel):
    jobs: List[JobSummaryModel] = Field(alias="jobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchQuantumTasksResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    quantum_tasks: List[QuantumTaskSummaryModel] = Field(alias="quantumTasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchDevicesRequestModel(BaseModel):
    filters: Sequence[SearchDevicesFilterModel] = Field(alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchDevicesRequestSearchDevicesPaginateModel(BaseModel):
    filters: Sequence[SearchDevicesFilterModel] = Field(alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchJobsRequestModel(BaseModel):
    filters: Sequence[SearchJobsFilterModel] = Field(alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchJobsRequestSearchJobsPaginateModel(BaseModel):
    filters: Sequence[SearchJobsFilterModel] = Field(alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchQuantumTasksRequestModel(BaseModel):
    filters: Sequence[SearchQuantumTasksFilterModel] = Field(alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchQuantumTasksRequestSearchQuantumTasksPaginateModel(BaseModel):
    filters: Sequence[SearchQuantumTasksFilterModel] = Field(alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class InputFileConfigModel(BaseModel):
    channel_name: str = Field(alias="channelName")
    data_source: DataSourceModel = Field(alias="dataSource")
    content_type: Optional[str] = Field(default=None, alias="contentType")


class CreateJobRequestModel(BaseModel):
    algorithm_specification: AlgorithmSpecificationModel = Field(
        alias="algorithmSpecification"
    )
    client_token: str = Field(alias="clientToken")
    device_config: DeviceConfigModel = Field(alias="deviceConfig")
    instance_config: InstanceConfigModel = Field(alias="instanceConfig")
    job_name: str = Field(alias="jobName")
    output_data_config: JobOutputDataConfigModel = Field(alias="outputDataConfig")
    role_arn: str = Field(alias="roleArn")
    checkpoint_config: Optional[JobCheckpointConfigModel] = Field(
        default=None, alias="checkpointConfig"
    )
    hyper_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="hyperParameters"
    )
    input_data_config: Optional[Sequence[InputFileConfigModel]] = Field(
        default=None, alias="inputDataConfig"
    )
    stopping_condition: Optional[JobStoppingConditionModel] = Field(
        default=None, alias="stoppingCondition"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetJobResponseModel(BaseModel):
    algorithm_specification: AlgorithmSpecificationModel = Field(
        alias="algorithmSpecification"
    )
    billable_duration: int = Field(alias="billableDuration")
    checkpoint_config: JobCheckpointConfigModel = Field(alias="checkpointConfig")
    created_at: datetime = Field(alias="createdAt")
    device_config: DeviceConfigModel = Field(alias="deviceConfig")
    ended_at: datetime = Field(alias="endedAt")
    events: List[JobEventDetailsModel] = Field(alias="events")
    failure_reason: str = Field(alias="failureReason")
    hyper_parameters: Dict[str, str] = Field(alias="hyperParameters")
    input_data_config: List[InputFileConfigModel] = Field(alias="inputDataConfig")
    instance_config: InstanceConfigModel = Field(alias="instanceConfig")
    job_arn: str = Field(alias="jobArn")
    job_name: str = Field(alias="jobName")
    output_data_config: JobOutputDataConfigModel = Field(alias="outputDataConfig")
    role_arn: str = Field(alias="roleArn")
    started_at: datetime = Field(alias="startedAt")
    status: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "QUEUED", "RUNNING"
    ] = Field(alias="status")
    stopping_condition: JobStoppingConditionModel = Field(alias="stoppingCondition")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
