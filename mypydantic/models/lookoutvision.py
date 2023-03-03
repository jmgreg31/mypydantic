# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class PixelAnomalyModel(BaseModel):
    total_percentage_area: Optional[float] = Field(
        default=None, alias="TotalPercentageArea"
    )
    color: Optional[str] = Field(default=None, alias="Color")


class DatasetMetadataModel(BaseModel):
    dataset_type: Optional[str] = Field(default=None, alias="DatasetType")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateProjectRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ProjectMetadataModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="ProjectArn")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )


class DatasetImageStatsModel(BaseModel):
    total: Optional[int] = Field(default=None, alias="Total")
    labeled: Optional[int] = Field(default=None, alias="Labeled")
    normal: Optional[int] = Field(default=None, alias="Normal")
    anomaly: Optional[int] = Field(default=None, alias="Anomaly")


class InputS3ObjectModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class DeleteDatasetRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteModelRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteProjectRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribeDatasetRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")


class DescribeModelPackagingJobRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    job_name: str = Field(alias="JobName")


class DescribeModelRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")


class DescribeProjectRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")


class DetectAnomaliesRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Body")
    content_type: str = Field(alias="ContentType")


class ImageSourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class S3LocationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class TargetPlatformModel(BaseModel):
    os: Literal["LINUX"] = Field(alias="Os")
    arch: Literal["ARM64", "X86_64"] = Field(alias="Arch")
    accelerator: Optional[Literal["NVIDIA"]] = Field(default=None, alias="Accelerator")


class GreengrassOutputDetailsModel(BaseModel):
    component_version_arn: Optional[str] = Field(
        default=None, alias="ComponentVersionArn"
    )
    component_name: Optional[str] = Field(default=None, alias="ComponentName")
    component_version: Optional[str] = Field(default=None, alias="ComponentVersion")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDatasetEntriesRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")
    labeled: Optional[bool] = Field(default=None, alias="Labeled")
    anomaly_class: Optional[str] = Field(default=None, alias="AnomalyClass")
    before_creation_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="BeforeCreationDate"
    )
    after_creation_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="AfterCreationDate"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    source_ref_contains: Optional[str] = Field(default=None, alias="SourceRefContains")


class ListModelPackagingJobsRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ModelPackagingJobMetadataModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    model_packaging_job_description: Optional[str] = Field(
        default=None, alias="ModelPackagingJobDescription"
    )
    model_packaging_method: Optional[str] = Field(
        default=None, alias="ModelPackagingMethod"
    )
    status: Optional[Literal["CREATED", "FAILED", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class ListModelsRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListProjectsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ModelPerformanceModel(BaseModel):
    f1_score: Optional[float] = Field(default=None, alias="F1Score")
    recall: Optional[float] = Field(default=None, alias="Recall")
    precision: Optional[float] = Field(default=None, alias="Precision")


class OutputS3ObjectModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")


class StartModelRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")
    min_inference_units: int = Field(alias="MinInferenceUnits")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    max_inference_units: Optional[int] = Field(default=None, alias="MaxInferenceUnits")


class StopModelRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDatasetEntriesRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")
    changes: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Changes"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class AnomalyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    pixel_anomaly: Optional[PixelAnomalyModel] = Field(
        default=None, alias="PixelAnomaly"
    )


class ProjectDescriptionModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="ProjectArn")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    datasets: Optional[List[DatasetMetadataModel]] = Field(
        default=None, alias="Datasets"
    )


class CreateDatasetResponseModel(BaseModel):
    dataset_metadata: DatasetMetadataModel = Field(alias="DatasetMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteModelResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectResponseModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetEntriesResponseModel(BaseModel):
    dataset_entries: List[str] = Field(alias="DatasetEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartModelPackagingJobResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartModelResponseModel(BaseModel):
    status: Literal[
        "HOSTED",
        "HOSTING_FAILED",
        "STARTING_HOSTING",
        "STOPPING_HOSTING",
        "SYSTEM_UPDATING",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopModelResponseModel(BaseModel):
    status: Literal[
        "HOSTED",
        "HOSTING_FAILED",
        "STARTING_HOSTING",
        "STOPPING_HOSTING",
        "SYSTEM_UPDATING",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatasetEntriesResponseModel(BaseModel):
    status: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED_ROLLBACK_COMPLETE",
        "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateProjectResponseModel(BaseModel):
    project_metadata: ProjectMetadataModel = Field(alias="ProjectMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsResponseModel(BaseModel):
    projects: List[ProjectMetadataModel] = Field(alias="Projects")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasetDescriptionModel(BaseModel):
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    dataset_type: Optional[str] = Field(default=None, alias="DatasetType")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    image_stats: Optional[DatasetImageStatsModel] = Field(
        default=None, alias="ImageStats"
    )


class DatasetGroundTruthManifestModel(BaseModel):
    s3_object: Optional[InputS3ObjectModel] = Field(default=None, alias="S3Object")


class OutputConfigModel(BaseModel):
    s3_location: S3LocationModel = Field(alias="S3Location")


class GreengrassConfigurationModel(BaseModel):
    s3_output_location: S3LocationModel = Field(alias="S3OutputLocation")
    component_name: str = Field(alias="ComponentName")
    compiler_options: Optional[str] = Field(default=None, alias="CompilerOptions")
    target_device: Optional[Literal["jetson_xavier"]] = Field(
        default=None, alias="TargetDevice"
    )
    target_platform: Optional[TargetPlatformModel] = Field(
        default=None, alias="TargetPlatform"
    )
    component_version: Optional[str] = Field(default=None, alias="ComponentVersion")
    component_description: Optional[str] = Field(
        default=None, alias="ComponentDescription"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ModelPackagingOutputDetailsModel(BaseModel):
    greengrass: Optional[GreengrassOutputDetailsModel] = Field(
        default=None, alias="Greengrass"
    )


class ListDatasetEntriesRequestListDatasetEntriesPaginateModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")
    labeled: Optional[bool] = Field(default=None, alias="Labeled")
    anomaly_class: Optional[str] = Field(default=None, alias="AnomalyClass")
    before_creation_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="BeforeCreationDate"
    )
    after_creation_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="AfterCreationDate"
    )
    source_ref_contains: Optional[str] = Field(default=None, alias="SourceRefContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelPackagingJobsRequestListModelPackagingJobsPaginateModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelsRequestListModelsPaginateModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelPackagingJobsResponseModel(BaseModel):
    model_packaging_jobs: List[ModelPackagingJobMetadataModel] = Field(
        alias="ModelPackagingJobs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelMetadataModel(BaseModel):
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal[
            "DELETING",
            "HOSTED",
            "HOSTING_FAILED",
            "STARTING_HOSTING",
            "STOPPING_HOSTING",
            "SYSTEM_UPDATING",
            "TRAINED",
            "TRAINING",
            "TRAINING_FAILED",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    performance: Optional[ModelPerformanceModel] = Field(
        default=None, alias="Performance"
    )


class DetectAnomalyResultModel(BaseModel):
    source: Optional[ImageSourceModel] = Field(default=None, alias="Source")
    is_anomalous: Optional[bool] = Field(default=None, alias="IsAnomalous")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    anomalies: Optional[List[AnomalyModel]] = Field(default=None, alias="Anomalies")
    anomaly_mask: Optional[bytes] = Field(default=None, alias="AnomalyMask")


class DescribeProjectResponseModel(BaseModel):
    project_description: ProjectDescriptionModel = Field(alias="ProjectDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetResponseModel(BaseModel):
    dataset_description: DatasetDescriptionModel = Field(alias="DatasetDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasetSourceModel(BaseModel):
    ground_truth_manifest: Optional[DatasetGroundTruthManifestModel] = Field(
        default=None, alias="GroundTruthManifest"
    )


class CreateModelRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    output_config: OutputConfigModel = Field(alias="OutputConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ModelDescriptionModel(BaseModel):
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal[
            "DELETING",
            "HOSTED",
            "HOSTING_FAILED",
            "STARTING_HOSTING",
            "STOPPING_HOSTING",
            "SYSTEM_UPDATING",
            "TRAINED",
            "TRAINING",
            "TRAINING_FAILED",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    performance: Optional[ModelPerformanceModel] = Field(
        default=None, alias="Performance"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    evaluation_manifest: Optional[OutputS3ObjectModel] = Field(
        default=None, alias="EvaluationManifest"
    )
    evaluation_result: Optional[OutputS3ObjectModel] = Field(
        default=None, alias="EvaluationResult"
    )
    evaluation_end_timestamp: Optional[datetime] = Field(
        default=None, alias="EvaluationEndTimestamp"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    min_inference_units: Optional[int] = Field(default=None, alias="MinInferenceUnits")
    max_inference_units: Optional[int] = Field(default=None, alias="MaxInferenceUnits")


class ModelPackagingConfigurationModel(BaseModel):
    greengrass: GreengrassConfigurationModel = Field(alias="Greengrass")


class CreateModelResponseModel(BaseModel):
    model_metadata: ModelMetadataModel = Field(alias="ModelMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelsResponseModel(BaseModel):
    models: List[ModelMetadataModel] = Field(alias="Models")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectAnomaliesResponseModel(BaseModel):
    detect_anomaly_result: DetectAnomalyResultModel = Field(alias="DetectAnomalyResult")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    dataset_type: str = Field(alias="DatasetType")
    dataset_source: Optional[DatasetSourceModel] = Field(
        default=None, alias="DatasetSource"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribeModelResponseModel(BaseModel):
    model_description: ModelDescriptionModel = Field(alias="ModelDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelPackagingDescriptionModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    model_packaging_configuration: Optional[ModelPackagingConfigurationModel] = Field(
        default=None, alias="ModelPackagingConfiguration"
    )
    model_packaging_job_description: Optional[str] = Field(
        default=None, alias="ModelPackagingJobDescription"
    )
    model_packaging_method: Optional[str] = Field(
        default=None, alias="ModelPackagingMethod"
    )
    model_packaging_output_details: Optional[ModelPackagingOutputDetailsModel] = Field(
        default=None, alias="ModelPackagingOutputDetails"
    )
    status: Optional[Literal["CREATED", "FAILED", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class StartModelPackagingJobRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    model_version: str = Field(alias="ModelVersion")
    configuration: ModelPackagingConfigurationModel = Field(alias="Configuration")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribeModelPackagingJobResponseModel(BaseModel):
    model_packaging_description: ModelPackagingDescriptionModel = Field(
        alias="ModelPackagingDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
