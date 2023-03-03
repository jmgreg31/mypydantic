# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchDeleteWorldsRequestModel(BaseModel):
    worlds: Sequence[str] = Field(alias="worlds")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDescribeSimulationJobRequestModel(BaseModel):
    jobs: Sequence[str] = Field(alias="jobs")


class BatchPolicyModel(BaseModel):
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    max_concurrency: Optional[int] = Field(default=None, alias="maxConcurrency")


class CancelDeploymentJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class CancelSimulationJobBatchRequestModel(BaseModel):
    batch: str = Field(alias="batch")


class CancelSimulationJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class CancelWorldExportJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class CancelWorldGenerationJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class ComputeResponseModel(BaseModel):
    simulation_unit_limit: Optional[int] = Field(
        default=None, alias="simulationUnitLimit"
    )
    compute_type: Optional[Literal["CPU", "GPU_AND_CPU"]] = Field(
        default=None, alias="computeType"
    )
    gpu_unit_limit: Optional[int] = Field(default=None, alias="gpuUnitLimit")


class ComputeModel(BaseModel):
    simulation_unit_limit: Optional[int] = Field(
        default=None, alias="simulationUnitLimit"
    )
    compute_type: Optional[Literal["CPU", "GPU_AND_CPU"]] = Field(
        default=None, alias="computeType"
    )
    gpu_unit_limit: Optional[int] = Field(default=None, alias="gpuUnitLimit")


class CreateFleetRequestModel(BaseModel):
    name: str = Field(alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class EnvironmentModel(BaseModel):
    uri: Optional[str] = Field(default=None, alias="uri")


class RobotSoftwareSuiteModel(BaseModel):
    name: Optional[Literal["General", "ROS", "ROS2"]] = Field(
        default=None, alias="name"
    )
    version: Optional[Literal["Dashing", "Foxy", "Kinetic", "Melodic"]] = Field(
        default=None, alias="version"
    )


class SourceConfigModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="s3Key")
    architecture: Optional[Literal["ARM64", "ARMHF", "X86_64"]] = Field(
        default=None, alias="architecture"
    )


class SourceModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="s3Key")
    etag: Optional[str] = Field(default=None, alias="etag")
    architecture: Optional[Literal["ARM64", "ARMHF", "X86_64"]] = Field(
        default=None, alias="architecture"
    )


class CreateRobotApplicationVersionRequestModel(BaseModel):
    application: str = Field(alias="application")
    current_revision_id: Optional[str] = Field(default=None, alias="currentRevisionId")
    s3_etags: Optional[Sequence[str]] = Field(default=None, alias="s3Etags")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")


class CreateRobotRequestModel(BaseModel):
    name: str = Field(alias="name")
    architecture: Literal["ARM64", "ARMHF", "X86_64"] = Field(alias="architecture")
    greengrass_group_id: str = Field(alias="greengrassGroupId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class RenderingEngineModel(BaseModel):
    name: Optional[Literal["OGRE"]] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")


class SimulationSoftwareSuiteModel(BaseModel):
    name: Optional[Literal["Gazebo", "RosbagPlay", "SimulationRuntime"]] = Field(
        default=None, alias="name"
    )
    version: Optional[str] = Field(default=None, alias="version")


class CreateSimulationApplicationVersionRequestModel(BaseModel):
    application: str = Field(alias="application")
    current_revision_id: Optional[str] = Field(default=None, alias="currentRevisionId")
    s3_etags: Optional[Sequence[str]] = Field(default=None, alias="s3Etags")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")


class DataSourceConfigModel(BaseModel):
    name: str = Field(alias="name")
    s3_bucket: str = Field(alias="s3Bucket")
    s3_keys: Sequence[str] = Field(alias="s3Keys")
    type: Optional[Literal["Archive", "File", "Prefix"]] = Field(
        default=None, alias="type"
    )
    destination: Optional[str] = Field(default=None, alias="destination")


class LoggingConfigModel(BaseModel):
    record_all_ros_topics: Optional[bool] = Field(
        default=None, alias="recordAllRosTopics"
    )


class OutputLocationModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_prefix: Optional[str] = Field(default=None, alias="s3Prefix")


class VPCConfigModel(BaseModel):
    subnets: Sequence[str] = Field(alias="subnets")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroups"
    )
    assign_public_ip: Optional[bool] = Field(default=None, alias="assignPublicIp")


class VPCConfigResponseModel(BaseModel):
    subnets: Optional[List[str]] = Field(default=None, alias="subnets")
    security_groups: Optional[List[str]] = Field(default=None, alias="securityGroups")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    assign_public_ip: Optional[bool] = Field(default=None, alias="assignPublicIp")


class WorldCountModel(BaseModel):
    floorplan_count: Optional[int] = Field(default=None, alias="floorplanCount")
    interior_count_per_floorplan: Optional[int] = Field(
        default=None, alias="interiorCountPerFloorplan"
    )


class TemplateLocationModel(BaseModel):
    s3_bucket: str = Field(alias="s3Bucket")
    s3_key: str = Field(alias="s3Key")


class S3KeyOutputModel(BaseModel):
    s3_key: Optional[str] = Field(default=None, alias="s3Key")
    etag: Optional[str] = Field(default=None, alias="etag")


class DeleteFleetRequestModel(BaseModel):
    fleet: str = Field(alias="fleet")


class DeleteRobotApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")


class DeleteRobotRequestModel(BaseModel):
    robot: str = Field(alias="robot")


class DeleteSimulationApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")


class DeleteWorldTemplateRequestModel(BaseModel):
    template: str = Field(alias="template")


class DeploymentLaunchConfigModel(BaseModel):
    package_name: str = Field(alias="packageName")
    launch_file: str = Field(alias="launchFile")
    pre_launch_file: Optional[str] = Field(default=None, alias="preLaunchFile")
    post_launch_file: Optional[str] = Field(default=None, alias="postLaunchFile")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )


class S3ObjectModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")
    etag: Optional[str] = Field(default=None, alias="etag")


class DeregisterRobotRequestModel(BaseModel):
    fleet: str = Field(alias="fleet")
    robot: str = Field(alias="robot")


class DescribeDeploymentJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class DescribeFleetRequestModel(BaseModel):
    fleet: str = Field(alias="fleet")


class RobotModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    fleet_arn: Optional[str] = Field(default=None, alias="fleetArn")
    status: Optional[
        Literal[
            "Available",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
            "PendingNewDeployment",
            "Registered",
        ]
    ] = Field(default=None, alias="status")
    green_grass_group_id: Optional[str] = Field(default=None, alias="greenGrassGroupId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    architecture: Optional[Literal["ARM64", "ARMHF", "X86_64"]] = Field(
        default=None, alias="architecture"
    )
    last_deployment_job: Optional[str] = Field(default=None, alias="lastDeploymentJob")
    last_deployment_time: Optional[datetime] = Field(
        default=None, alias="lastDeploymentTime"
    )


class DescribeRobotApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")


class DescribeRobotRequestModel(BaseModel):
    robot: str = Field(alias="robot")


class DescribeSimulationApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")


class DescribeSimulationJobBatchRequestModel(BaseModel):
    batch: str = Field(alias="batch")


class SimulationJobSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[
        Literal[
            "Canceled",
            "Completed",
            "Failed",
            "Pending",
            "Preparing",
            "Restarting",
            "Running",
            "RunningFailed",
            "Terminated",
            "Terminating",
        ]
    ] = Field(default=None, alias="status")
    simulation_application_names: Optional[List[str]] = Field(
        default=None, alias="simulationApplicationNames"
    )
    robot_application_names: Optional[List[str]] = Field(
        default=None, alias="robotApplicationNames"
    )
    data_source_names: Optional[List[str]] = Field(
        default=None, alias="dataSourceNames"
    )
    compute_type: Optional[Literal["CPU", "GPU_AND_CPU"]] = Field(
        default=None, alias="computeType"
    )


class DescribeSimulationJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class NetworkInterfaceModel(BaseModel):
    network_interface_id: Optional[str] = Field(
        default=None, alias="networkInterfaceId"
    )
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")
    public_ip_address: Optional[str] = Field(default=None, alias="publicIpAddress")


class DescribeWorldExportJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class DescribeWorldGenerationJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class DescribeWorldRequestModel(BaseModel):
    world: str = Field(alias="world")


class DescribeWorldTemplateRequestModel(BaseModel):
    template: str = Field(alias="template")


class WorldFailureModel(BaseModel):
    failure_code: Optional[
        Literal[
            "AllWorldGenerationFailed",
            "InternalServiceError",
            "InvalidInput",
            "LimitExceeded",
            "RequestThrottled",
            "ResourceNotFound",
        ]
    ] = Field(default=None, alias="failureCode")
    sample_failure_reason: Optional[str] = Field(
        default=None, alias="sampleFailureReason"
    )
    failure_count: Optional[int] = Field(default=None, alias="failureCount")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class FleetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_deployment_status: Optional[
        Literal["Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"]
    ] = Field(default=None, alias="lastDeploymentStatus")
    last_deployment_job: Optional[str] = Field(default=None, alias="lastDeploymentJob")
    last_deployment_time: Optional[datetime] = Field(
        default=None, alias="lastDeploymentTime"
    )


class GetWorldTemplateBodyRequestModel(BaseModel):
    template: Optional[str] = Field(default=None, alias="template")
    generation_job: Optional[str] = Field(default=None, alias="generationJob")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class SimulationJobBatchSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    status: Optional[
        Literal[
            "Canceled",
            "Canceling",
            "Completed",
            "Completing",
            "Failed",
            "InProgress",
            "Pending",
            "TimedOut",
            "TimingOut",
        ]
    ] = Field(default=None, alias="status")
    failed_request_count: Optional[int] = Field(
        default=None, alias="failedRequestCount"
    )
    pending_request_count: Optional[int] = Field(
        default=None, alias="pendingRequestCount"
    )
    created_request_count: Optional[int] = Field(
        default=None, alias="createdRequestCount"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListWorldTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class TemplateSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")


class WorldSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    generation_job: Optional[str] = Field(default=None, alias="generationJob")
    template: Optional[str] = Field(default=None, alias="template")


class PortMappingModel(BaseModel):
    job_port: int = Field(alias="jobPort")
    application_port: int = Field(alias="applicationPort")
    enable_on_public_ip: Optional[bool] = Field(default=None, alias="enableOnPublicIp")


class ProgressDetailModel(BaseModel):
    current_progress: Optional[
        Literal[
            "DownloadingExtracting",
            "ExecutingDownloadCondition",
            "ExecutingPostLaunch",
            "ExecutingPreLaunch",
            "Finished",
            "Launching",
            "Validating",
        ]
    ] = Field(default=None, alias="currentProgress")
    percent_done: Optional[float] = Field(default=None, alias="percentDone")
    estimated_time_remaining_seconds: Optional[int] = Field(
        default=None, alias="estimatedTimeRemainingSeconds"
    )
    target_resource: Optional[str] = Field(default=None, alias="targetResource")


class RegisterRobotRequestModel(BaseModel):
    fleet: str = Field(alias="fleet")
    robot: str = Field(alias="robot")


class RestartSimulationJobRequestModel(BaseModel):
    job: str = Field(alias="job")


class ToolModel(BaseModel):
    name: str = Field(alias="name")
    command: str = Field(alias="command")
    stream_ui: Optional[bool] = Field(default=None, alias="streamUI")
    stream_output_to_cloud_watch: Optional[bool] = Field(
        default=None, alias="streamOutputToCloudWatch"
    )
    exit_behavior: Optional[Literal["FAIL", "RESTART"]] = Field(
        default=None, alias="exitBehavior"
    )


class UploadConfigurationModel(BaseModel):
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    upload_behavior: Literal[
        "UPLOAD_ON_TERMINATE", "UPLOAD_ROLLING_AUTO_REMOVE"
    ] = Field(alias="uploadBehavior")


class WorldConfigModel(BaseModel):
    world: Optional[str] = Field(default=None, alias="world")


class SyncDeploymentJobRequestModel(BaseModel):
    client_request_token: str = Field(alias="clientRequestToken")
    fleet: str = Field(alias="fleet")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchDeleteWorldsResponseModel(BaseModel):
    unprocessed_worlds: List[str] = Field(alias="unprocessedWorlds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    created_at: datetime = Field(alias="createdAt")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRobotResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    created_at: datetime = Field(alias="createdAt")
    greengrass_group_id: str = Field(alias="greengrassGroupId")
    architecture: Literal["ARM64", "ARMHF", "X86_64"] = Field(alias="architecture")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorldTemplateResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    client_request_token: str = Field(alias="clientRequestToken")
    created_at: datetime = Field(alias="createdAt")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterRobotResponseModel(BaseModel):
    fleet: str = Field(alias="fleet")
    robot: str = Field(alias="robot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRobotResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    fleet_arn: str = Field(alias="fleetArn")
    status: Literal[
        "Available",
        "Deploying",
        "Failed",
        "InSync",
        "NoResponse",
        "PendingNewDeployment",
        "Registered",
    ] = Field(alias="status")
    greengrass_group_id: str = Field(alias="greengrassGroupId")
    created_at: datetime = Field(alias="createdAt")
    architecture: Literal["ARM64", "ARMHF", "X86_64"] = Field(alias="architecture")
    last_deployment_job: str = Field(alias="lastDeploymentJob")
    last_deployment_time: datetime = Field(alias="lastDeploymentTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorldResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    generation_job: str = Field(alias="generationJob")
    template: str = Field(alias="template")
    created_at: datetime = Field(alias="createdAt")
    tags: Dict[str, str] = Field(alias="tags")
    world_description_body: str = Field(alias="worldDescriptionBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorldTemplateResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    client_request_token: str = Field(alias="clientRequestToken")
    name: str = Field(alias="name")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    tags: Dict[str, str] = Field(alias="tags")
    version: str = Field(alias="version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorldTemplateBodyResponseModel(BaseModel):
    template_body: str = Field(alias="templateBody")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterRobotResponseModel(BaseModel):
    fleet: str = Field(alias="fleet")
    robot: str = Field(alias="robot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorldTemplateResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RobotApplicationSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    version: Optional[str] = Field(default=None, alias="version")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    robot_software_suite: Optional[RobotSoftwareSuiteModel] = Field(
        default=None, alias="robotSoftwareSuite"
    )


class CreateRobotApplicationRequestModel(BaseModel):
    name: str = Field(alias="name")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    sources: Optional[Sequence[SourceConfigModel]] = Field(
        default=None, alias="sources"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    environment: Optional[EnvironmentModel] = Field(default=None, alias="environment")


class UpdateRobotApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    sources: Optional[Sequence[SourceConfigModel]] = Field(
        default=None, alias="sources"
    )
    current_revision_id: Optional[str] = Field(default=None, alias="currentRevisionId")
    environment: Optional[EnvironmentModel] = Field(default=None, alias="environment")


class CreateRobotApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    tags: Dict[str, str] = Field(alias="tags")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRobotApplicationVersionResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRobotApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    revision_id: str = Field(alias="revisionId")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    tags: Dict[str, str] = Field(alias="tags")
    environment: EnvironmentModel = Field(alias="environment")
    image_digest: str = Field(alias="imageDigest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRobotApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSimulationApplicationRequestModel(BaseModel):
    name: str = Field(alias="name")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    sources: Optional[Sequence[SourceConfigModel]] = Field(
        default=None, alias="sources"
    )
    rendering_engine: Optional[RenderingEngineModel] = Field(
        default=None, alias="renderingEngine"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    environment: Optional[EnvironmentModel] = Field(default=None, alias="environment")


class CreateSimulationApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    rendering_engine: RenderingEngineModel = Field(alias="renderingEngine")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    tags: Dict[str, str] = Field(alias="tags")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSimulationApplicationVersionResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    rendering_engine: RenderingEngineModel = Field(alias="renderingEngine")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSimulationApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    rendering_engine: RenderingEngineModel = Field(alias="renderingEngine")
    revision_id: str = Field(alias="revisionId")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    tags: Dict[str, str] = Field(alias="tags")
    environment: EnvironmentModel = Field(alias="environment")
    image_digest: str = Field(alias="imageDigest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SimulationApplicationSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    version: Optional[str] = Field(default=None, alias="version")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    robot_software_suite: Optional[RobotSoftwareSuiteModel] = Field(
        default=None, alias="robotSoftwareSuite"
    )
    simulation_software_suite: Optional[SimulationSoftwareSuiteModel] = Field(
        default=None, alias="simulationSoftwareSuite"
    )


class UpdateSimulationApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    sources: Optional[Sequence[SourceConfigModel]] = Field(
        default=None, alias="sources"
    )
    rendering_engine: Optional[RenderingEngineModel] = Field(
        default=None, alias="renderingEngine"
    )
    current_revision_id: Optional[str] = Field(default=None, alias="currentRevisionId")
    environment: Optional[EnvironmentModel] = Field(default=None, alias="environment")


class UpdateSimulationApplicationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    sources: List[SourceModel] = Field(alias="sources")
    simulation_software_suite: SimulationSoftwareSuiteModel = Field(
        alias="simulationSoftwareSuite"
    )
    robot_software_suite: RobotSoftwareSuiteModel = Field(alias="robotSoftwareSuite")
    rendering_engine: RenderingEngineModel = Field(alias="renderingEngine")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    revision_id: str = Field(alias="revisionId")
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorldExportJobRequestModel(BaseModel):
    worlds: Sequence[str] = Field(alias="worlds")
    output_location: OutputLocationModel = Field(alias="outputLocation")
    iam_role: str = Field(alias="iamRole")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateWorldExportJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled", "Canceling", "Completed", "Failed", "Pending", "Running"
    ] = Field(alias="status")
    created_at: datetime = Field(alias="createdAt")
    failure_code: Literal[
        "AccessDenied",
        "InternalServiceError",
        "InvalidInput",
        "LimitExceeded",
        "RequestThrottled",
        "ResourceNotFound",
    ] = Field(alias="failureCode")
    client_request_token: str = Field(alias="clientRequestToken")
    output_location: OutputLocationModel = Field(alias="outputLocation")
    iam_role: str = Field(alias="iamRole")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorldExportJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled", "Canceling", "Completed", "Failed", "Pending", "Running"
    ] = Field(alias="status")
    created_at: datetime = Field(alias="createdAt")
    failure_code: Literal[
        "AccessDenied",
        "InternalServiceError",
        "InvalidInput",
        "LimitExceeded",
        "RequestThrottled",
        "ResourceNotFound",
    ] = Field(alias="failureCode")
    failure_reason: str = Field(alias="failureReason")
    client_request_token: str = Field(alias="clientRequestToken")
    worlds: List[str] = Field(alias="worlds")
    output_location: OutputLocationModel = Field(alias="outputLocation")
    iam_role: str = Field(alias="iamRole")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorldExportJobSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[
        Literal["Canceled", "Canceling", "Completed", "Failed", "Pending", "Running"]
    ] = Field(default=None, alias="status")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    worlds: Optional[List[str]] = Field(default=None, alias="worlds")
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="outputLocation"
    )


class CreateWorldGenerationJobRequestModel(BaseModel):
    template: str = Field(alias="template")
    world_count: WorldCountModel = Field(alias="worldCount")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    world_tags: Optional[Mapping[str, str]] = Field(default=None, alias="worldTags")


class CreateWorldGenerationJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled",
        "Canceling",
        "Completed",
        "Failed",
        "PartialFailed",
        "Pending",
        "Running",
    ] = Field(alias="status")
    created_at: datetime = Field(alias="createdAt")
    failure_code: Literal[
        "AllWorldGenerationFailed",
        "InternalServiceError",
        "InvalidInput",
        "LimitExceeded",
        "RequestThrottled",
        "ResourceNotFound",
    ] = Field(alias="failureCode")
    client_request_token: str = Field(alias="clientRequestToken")
    template: str = Field(alias="template")
    world_count: WorldCountModel = Field(alias="worldCount")
    tags: Dict[str, str] = Field(alias="tags")
    world_tags: Dict[str, str] = Field(alias="worldTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorldGenerationJobSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    template: Optional[str] = Field(default=None, alias="template")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    status: Optional[
        Literal[
            "Canceled",
            "Canceling",
            "Completed",
            "Failed",
            "PartialFailed",
            "Pending",
            "Running",
        ]
    ] = Field(default=None, alias="status")
    world_count: Optional[WorldCountModel] = Field(default=None, alias="worldCount")
    succeeded_world_count: Optional[int] = Field(
        default=None, alias="succeededWorldCount"
    )
    failed_world_count: Optional[int] = Field(default=None, alias="failedWorldCount")


class CreateWorldTemplateRequestModel(BaseModel):
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    name: Optional[str] = Field(default=None, alias="name")
    template_body: Optional[str] = Field(default=None, alias="templateBody")
    template_location: Optional[TemplateLocationModel] = Field(
        default=None, alias="templateLocation"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateWorldTemplateRequestModel(BaseModel):
    template: str = Field(alias="template")
    name: Optional[str] = Field(default=None, alias="name")
    template_body: Optional[str] = Field(default=None, alias="templateBody")
    template_location: Optional[TemplateLocationModel] = Field(
        default=None, alias="templateLocation"
    )


class DataSourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_keys: Optional[List[S3KeyOutputModel]] = Field(default=None, alias="s3Keys")
    type: Optional[Literal["Archive", "File", "Prefix"]] = Field(
        default=None, alias="type"
    )
    destination: Optional[str] = Field(default=None, alias="destination")


class DeploymentApplicationConfigModel(BaseModel):
    application: str = Field(alias="application")
    application_version: str = Field(alias="applicationVersion")
    launch_config: DeploymentLaunchConfigModel = Field(alias="launchConfig")


class DeploymentConfigModel(BaseModel):
    concurrent_deployment_percentage: Optional[int] = Field(
        default=None, alias="concurrentDeploymentPercentage"
    )
    failure_threshold_percentage: Optional[int] = Field(
        default=None, alias="failureThresholdPercentage"
    )
    robot_deployment_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="robotDeploymentTimeoutInSeconds"
    )
    download_condition_file: Optional[S3ObjectModel] = Field(
        default=None, alias="downloadConditionFile"
    )


class DescribeFleetResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    robots: List[RobotModel] = Field(alias="robots")
    created_at: datetime = Field(alias="createdAt")
    last_deployment_status: Literal[
        "Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"
    ] = Field(alias="lastDeploymentStatus")
    last_deployment_job: str = Field(alias="lastDeploymentJob")
    last_deployment_time: datetime = Field(alias="lastDeploymentTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRobotsResponseModel(BaseModel):
    robots: List[RobotModel] = Field(alias="robots")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSimulationJobsResponseModel(BaseModel):
    simulation_job_summaries: List[SimulationJobSummaryModel] = Field(
        alias="simulationJobSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailureSummaryModel(BaseModel):
    total_failure_count: Optional[int] = Field(default=None, alias="totalFailureCount")
    failures: Optional[List[WorldFailureModel]] = Field(default=None, alias="failures")


class ListDeploymentJobsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFleetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListRobotApplicationsRequestModel(BaseModel):
    version_qualifier: Optional[str] = Field(default=None, alias="versionQualifier")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListRobotsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListSimulationApplicationsRequestModel(BaseModel):
    version_qualifier: Optional[str] = Field(default=None, alias="versionQualifier")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListSimulationJobBatchesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListSimulationJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListWorldExportJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListWorldGenerationJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListWorldsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")


class ListFleetsResponseModel(BaseModel):
    fleet_details: List[FleetModel] = Field(alias="fleetDetails")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentJobsRequestListDeploymentJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFleetsRequestListFleetsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRobotApplicationsRequestListRobotApplicationsPaginateModel(BaseModel):
    version_qualifier: Optional[str] = Field(default=None, alias="versionQualifier")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRobotsRequestListRobotsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSimulationApplicationsRequestListSimulationApplicationsPaginateModel(
    BaseModel
):
    version_qualifier: Optional[str] = Field(default=None, alias="versionQualifier")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSimulationJobsRequestListSimulationJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorldExportJobsRequestListWorldExportJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorldTemplatesRequestListWorldTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorldsRequestListWorldsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSimulationJobBatchesResponseModel(BaseModel):
    simulation_job_batch_summaries: List[SimulationJobBatchSummaryModel] = Field(
        alias="simulationJobBatchSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorldTemplatesResponseModel(BaseModel):
    template_summaries: List[TemplateSummaryModel] = Field(alias="templateSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorldsResponseModel(BaseModel):
    world_summaries: List[WorldSummaryModel] = Field(alias="worldSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PortForwardingConfigModel(BaseModel):
    port_mappings: Optional[List[PortMappingModel]] = Field(
        default=None, alias="portMappings"
    )


class RobotDeploymentModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    deployment_start_time: Optional[datetime] = Field(
        default=None, alias="deploymentStartTime"
    )
    deployment_finish_time: Optional[datetime] = Field(
        default=None, alias="deploymentFinishTime"
    )
    status: Optional[
        Literal[
            "Available",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
            "PendingNewDeployment",
            "Registered",
        ]
    ] = Field(default=None, alias="status")
    progress_detail: Optional[ProgressDetailModel] = Field(
        default=None, alias="progressDetail"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    failure_code: Optional[
        Literal[
            "BadLambdaAssociated",
            "BadPermissionError",
            "DeploymentFleetDoesNotExist",
            "DownloadConditionFailed",
            "EnvironmentSetupError",
            "EtagMismatch",
            "ExtractingBundleFailure",
            "FailureThresholdBreached",
            "FleetDeploymentTimeout",
            "GreengrassDeploymentFailed",
            "GreengrassGroupVersionDoesNotExist",
            "InternalServerError",
            "InvalidGreengrassGroup",
            "LambdaDeleted",
            "MissingRobotApplicationArchitecture",
            "MissingRobotArchitecture",
            "MissingRobotDeploymentResource",
            "PostLaunchFileFailure",
            "PreLaunchFileFailure",
            "ResourceNotFound",
            "RobotAgentConnectionTimeout",
            "RobotApplicationDoesNotExist",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
        ]
    ] = Field(default=None, alias="failureCode")


class ListRobotApplicationsResponseModel(BaseModel):
    robot_application_summaries: List[RobotApplicationSummaryModel] = Field(
        alias="robotApplicationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSimulationApplicationsResponseModel(BaseModel):
    simulation_application_summaries: List[SimulationApplicationSummaryModel] = Field(
        alias="simulationApplicationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorldExportJobsResponseModel(BaseModel):
    world_export_job_summaries: List[WorldExportJobSummaryModel] = Field(
        alias="worldExportJobSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorldGenerationJobsResponseModel(BaseModel):
    world_generation_job_summaries: List[WorldGenerationJobSummaryModel] = Field(
        alias="worldGenerationJobSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentJobRequestModel(BaseModel):
    client_request_token: str = Field(alias="clientRequestToken")
    fleet: str = Field(alias="fleet")
    deployment_application_configs: Sequence[DeploymentApplicationConfigModel] = Field(
        alias="deploymentApplicationConfigs"
    )
    deployment_config: Optional[DeploymentConfigModel] = Field(
        default=None, alias="deploymentConfig"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateDeploymentJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    fleet: str = Field(alias="fleet")
    status: Literal[
        "Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"
    ] = Field(alias="status")
    deployment_application_configs: List[DeploymentApplicationConfigModel] = Field(
        alias="deploymentApplicationConfigs"
    )
    failure_reason: str = Field(alias="failureReason")
    failure_code: Literal[
        "BadLambdaAssociated",
        "BadPermissionError",
        "DeploymentFleetDoesNotExist",
        "DownloadConditionFailed",
        "EnvironmentSetupError",
        "EtagMismatch",
        "ExtractingBundleFailure",
        "FailureThresholdBreached",
        "FleetDeploymentTimeout",
        "GreengrassDeploymentFailed",
        "GreengrassGroupVersionDoesNotExist",
        "InternalServerError",
        "InvalidGreengrassGroup",
        "LambdaDeleted",
        "MissingRobotApplicationArchitecture",
        "MissingRobotArchitecture",
        "MissingRobotDeploymentResource",
        "PostLaunchFileFailure",
        "PreLaunchFileFailure",
        "ResourceNotFound",
        "RobotAgentConnectionTimeout",
        "RobotApplicationDoesNotExist",
        "RobotDeploymentAborted",
        "RobotDeploymentNoResponse",
    ] = Field(alias="failureCode")
    created_at: datetime = Field(alias="createdAt")
    deployment_config: DeploymentConfigModel = Field(alias="deploymentConfig")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentJobModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    fleet: Optional[str] = Field(default=None, alias="fleet")
    status: Optional[
        Literal["Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"]
    ] = Field(default=None, alias="status")
    deployment_application_configs: Optional[
        List[DeploymentApplicationConfigModel]
    ] = Field(default=None, alias="deploymentApplicationConfigs")
    deployment_config: Optional[DeploymentConfigModel] = Field(
        default=None, alias="deploymentConfig"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    failure_code: Optional[
        Literal[
            "BadLambdaAssociated",
            "BadPermissionError",
            "DeploymentFleetDoesNotExist",
            "DownloadConditionFailed",
            "EnvironmentSetupError",
            "EtagMismatch",
            "ExtractingBundleFailure",
            "FailureThresholdBreached",
            "FleetDeploymentTimeout",
            "GreengrassDeploymentFailed",
            "GreengrassGroupVersionDoesNotExist",
            "InternalServerError",
            "InvalidGreengrassGroup",
            "LambdaDeleted",
            "MissingRobotApplicationArchitecture",
            "MissingRobotArchitecture",
            "MissingRobotDeploymentResource",
            "PostLaunchFileFailure",
            "PreLaunchFileFailure",
            "ResourceNotFound",
            "RobotAgentConnectionTimeout",
            "RobotApplicationDoesNotExist",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
        ]
    ] = Field(default=None, alias="failureCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class SyncDeploymentJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    fleet: str = Field(alias="fleet")
    status: Literal[
        "Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"
    ] = Field(alias="status")
    deployment_config: DeploymentConfigModel = Field(alias="deploymentConfig")
    deployment_application_configs: List[DeploymentApplicationConfigModel] = Field(
        alias="deploymentApplicationConfigs"
    )
    failure_reason: str = Field(alias="failureReason")
    failure_code: Literal[
        "BadLambdaAssociated",
        "BadPermissionError",
        "DeploymentFleetDoesNotExist",
        "DownloadConditionFailed",
        "EnvironmentSetupError",
        "EtagMismatch",
        "ExtractingBundleFailure",
        "FailureThresholdBreached",
        "FleetDeploymentTimeout",
        "GreengrassDeploymentFailed",
        "GreengrassGroupVersionDoesNotExist",
        "InternalServerError",
        "InvalidGreengrassGroup",
        "LambdaDeleted",
        "MissingRobotApplicationArchitecture",
        "MissingRobotArchitecture",
        "MissingRobotDeploymentResource",
        "PostLaunchFileFailure",
        "PreLaunchFileFailure",
        "ResourceNotFound",
        "RobotAgentConnectionTimeout",
        "RobotApplicationDoesNotExist",
        "RobotDeploymentAborted",
        "RobotDeploymentNoResponse",
    ] = Field(alias="failureCode")
    created_at: datetime = Field(alias="createdAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FinishedWorldsSummaryModel(BaseModel):
    finished_count: Optional[int] = Field(default=None, alias="finishedCount")
    succeeded_worlds: Optional[List[str]] = Field(default=None, alias="succeededWorlds")
    failure_summary: Optional[FailureSummaryModel] = Field(
        default=None, alias="failureSummary"
    )


class LaunchConfigModel(BaseModel):
    package_name: Optional[str] = Field(default=None, alias="packageName")
    launch_file: Optional[str] = Field(default=None, alias="launchFile")
    environment_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    port_forwarding_config: Optional[PortForwardingConfigModel] = Field(
        default=None, alias="portForwardingConfig"
    )
    stream_ui: Optional[bool] = Field(default=None, alias="streamUI")
    command: Optional[List[str]] = Field(default=None, alias="command")


class DescribeDeploymentJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    fleet: str = Field(alias="fleet")
    status: Literal[
        "Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"
    ] = Field(alias="status")
    deployment_config: DeploymentConfigModel = Field(alias="deploymentConfig")
    deployment_application_configs: List[DeploymentApplicationConfigModel] = Field(
        alias="deploymentApplicationConfigs"
    )
    failure_reason: str = Field(alias="failureReason")
    failure_code: Literal[
        "BadLambdaAssociated",
        "BadPermissionError",
        "DeploymentFleetDoesNotExist",
        "DownloadConditionFailed",
        "EnvironmentSetupError",
        "EtagMismatch",
        "ExtractingBundleFailure",
        "FailureThresholdBreached",
        "FleetDeploymentTimeout",
        "GreengrassDeploymentFailed",
        "GreengrassGroupVersionDoesNotExist",
        "InternalServerError",
        "InvalidGreengrassGroup",
        "LambdaDeleted",
        "MissingRobotApplicationArchitecture",
        "MissingRobotArchitecture",
        "MissingRobotDeploymentResource",
        "PostLaunchFileFailure",
        "PreLaunchFileFailure",
        "ResourceNotFound",
        "RobotAgentConnectionTimeout",
        "RobotApplicationDoesNotExist",
        "RobotDeploymentAborted",
        "RobotDeploymentNoResponse",
    ] = Field(alias="failureCode")
    created_at: datetime = Field(alias="createdAt")
    robot_deployment_summary: List[RobotDeploymentModel] = Field(
        alias="robotDeploymentSummary"
    )
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentJobsResponseModel(BaseModel):
    deployment_jobs: List[DeploymentJobModel] = Field(alias="deploymentJobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorldGenerationJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled",
        "Canceling",
        "Completed",
        "Failed",
        "PartialFailed",
        "Pending",
        "Running",
    ] = Field(alias="status")
    created_at: datetime = Field(alias="createdAt")
    failure_code: Literal[
        "AllWorldGenerationFailed",
        "InternalServiceError",
        "InvalidInput",
        "LimitExceeded",
        "RequestThrottled",
        "ResourceNotFound",
    ] = Field(alias="failureCode")
    failure_reason: str = Field(alias="failureReason")
    client_request_token: str = Field(alias="clientRequestToken")
    template: str = Field(alias="template")
    world_count: WorldCountModel = Field(alias="worldCount")
    finished_worlds_summary: FinishedWorldsSummaryModel = Field(
        alias="finishedWorldsSummary"
    )
    tags: Dict[str, str] = Field(alias="tags")
    world_tags: Dict[str, str] = Field(alias="worldTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RobotApplicationConfigModel(BaseModel):
    application: str = Field(alias="application")
    launch_config: LaunchConfigModel = Field(alias="launchConfig")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")
    upload_configurations: Optional[List[UploadConfigurationModel]] = Field(
        default=None, alias="uploadConfigurations"
    )
    use_default_upload_configurations: Optional[bool] = Field(
        default=None, alias="useDefaultUploadConfigurations"
    )
    tools: Optional[List[ToolModel]] = Field(default=None, alias="tools")
    use_default_tools: Optional[bool] = Field(default=None, alias="useDefaultTools")


class SimulationApplicationConfigModel(BaseModel):
    application: str = Field(alias="application")
    launch_config: LaunchConfigModel = Field(alias="launchConfig")
    application_version: Optional[str] = Field(default=None, alias="applicationVersion")
    upload_configurations: Optional[List[UploadConfigurationModel]] = Field(
        default=None, alias="uploadConfigurations"
    )
    world_configs: Optional[List[WorldConfigModel]] = Field(
        default=None, alias="worldConfigs"
    )
    use_default_upload_configurations: Optional[bool] = Field(
        default=None, alias="useDefaultUploadConfigurations"
    )
    tools: Optional[List[ToolModel]] = Field(default=None, alias="tools")
    use_default_tools: Optional[bool] = Field(default=None, alias="useDefaultTools")


class CreateSimulationJobRequestModel(BaseModel):
    max_job_duration_in_seconds: int = Field(alias="maxJobDurationInSeconds")
    iam_role: str = Field(alias="iamRole")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="outputLocation"
    )
    logging_config: Optional[LoggingConfigModel] = Field(
        default=None, alias="loggingConfig"
    )
    failure_behavior: Optional[Literal["Continue", "Fail"]] = Field(
        default=None, alias="failureBehavior"
    )
    robot_applications: Optional[Sequence[RobotApplicationConfigModel]] = Field(
        default=None, alias="robotApplications"
    )
    simulation_applications: Optional[
        Sequence[SimulationApplicationConfigModel]
    ] = Field(default=None, alias="simulationApplications")
    data_sources: Optional[Sequence[DataSourceConfigModel]] = Field(
        default=None, alias="dataSources"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    vpc_config: Optional[VPCConfigModel] = Field(default=None, alias="vpcConfig")
    compute: Optional[ComputeModel] = Field(default=None, alias="compute")


class CreateSimulationJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled",
        "Completed",
        "Failed",
        "Pending",
        "Preparing",
        "Restarting",
        "Running",
        "RunningFailed",
        "Terminated",
        "Terminating",
    ] = Field(alias="status")
    last_started_at: datetime = Field(alias="lastStartedAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    failure_behavior: Literal["Continue", "Fail"] = Field(alias="failureBehavior")
    failure_code: Literal[
        "BadPermissionsCloudwatchLogs",
        "BadPermissionsRobotApplication",
        "BadPermissionsS3Object",
        "BadPermissionsS3Output",
        "BadPermissionsSimulationApplication",
        "BadPermissionsUserCredentials",
        "BatchCanceled",
        "BatchTimedOut",
        "ENILimitExceeded",
        "InternalServiceError",
        "InvalidBundleRobotApplication",
        "InvalidBundleSimulationApplication",
        "InvalidInput",
        "InvalidS3Resource",
        "LimitExceeded",
        "MismatchedEtag",
        "RequestThrottled",
        "ResourceNotFound",
        "RobotApplicationCrash",
        "RobotApplicationHealthCheckFailure",
        "RobotApplicationVersionMismatchedEtag",
        "SimulationApplicationCrash",
        "SimulationApplicationHealthCheckFailure",
        "SimulationApplicationVersionMismatchedEtag",
        "SubnetIpLimitExceeded",
        "ThrottlingError",
        "UploadContentMismatchError",
        "WrongRegionRobotApplication",
        "WrongRegionS3Bucket",
        "WrongRegionS3Output",
        "WrongRegionSimulationApplication",
    ] = Field(alias="failureCode")
    client_request_token: str = Field(alias="clientRequestToken")
    output_location: OutputLocationModel = Field(alias="outputLocation")
    logging_config: LoggingConfigModel = Field(alias="loggingConfig")
    max_job_duration_in_seconds: int = Field(alias="maxJobDurationInSeconds")
    simulation_time_millis: int = Field(alias="simulationTimeMillis")
    iam_role: str = Field(alias="iamRole")
    robot_applications: List[RobotApplicationConfigModel] = Field(
        alias="robotApplications"
    )
    simulation_applications: List[SimulationApplicationConfigModel] = Field(
        alias="simulationApplications"
    )
    data_sources: List[DataSourceModel] = Field(alias="dataSources")
    tags: Dict[str, str] = Field(alias="tags")
    vpc_config: VPCConfigResponseModel = Field(alias="vpcConfig")
    compute: ComputeResponseModel = Field(alias="compute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSimulationJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    status: Literal[
        "Canceled",
        "Completed",
        "Failed",
        "Pending",
        "Preparing",
        "Restarting",
        "Running",
        "RunningFailed",
        "Terminated",
        "Terminating",
    ] = Field(alias="status")
    last_started_at: datetime = Field(alias="lastStartedAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    failure_behavior: Literal["Continue", "Fail"] = Field(alias="failureBehavior")
    failure_code: Literal[
        "BadPermissionsCloudwatchLogs",
        "BadPermissionsRobotApplication",
        "BadPermissionsS3Object",
        "BadPermissionsS3Output",
        "BadPermissionsSimulationApplication",
        "BadPermissionsUserCredentials",
        "BatchCanceled",
        "BatchTimedOut",
        "ENILimitExceeded",
        "InternalServiceError",
        "InvalidBundleRobotApplication",
        "InvalidBundleSimulationApplication",
        "InvalidInput",
        "InvalidS3Resource",
        "LimitExceeded",
        "MismatchedEtag",
        "RequestThrottled",
        "ResourceNotFound",
        "RobotApplicationCrash",
        "RobotApplicationHealthCheckFailure",
        "RobotApplicationVersionMismatchedEtag",
        "SimulationApplicationCrash",
        "SimulationApplicationHealthCheckFailure",
        "SimulationApplicationVersionMismatchedEtag",
        "SubnetIpLimitExceeded",
        "ThrottlingError",
        "UploadContentMismatchError",
        "WrongRegionRobotApplication",
        "WrongRegionS3Bucket",
        "WrongRegionS3Output",
        "WrongRegionSimulationApplication",
    ] = Field(alias="failureCode")
    failure_reason: str = Field(alias="failureReason")
    client_request_token: str = Field(alias="clientRequestToken")
    output_location: OutputLocationModel = Field(alias="outputLocation")
    logging_config: LoggingConfigModel = Field(alias="loggingConfig")
    max_job_duration_in_seconds: int = Field(alias="maxJobDurationInSeconds")
    simulation_time_millis: int = Field(alias="simulationTimeMillis")
    iam_role: str = Field(alias="iamRole")
    robot_applications: List[RobotApplicationConfigModel] = Field(
        alias="robotApplications"
    )
    simulation_applications: List[SimulationApplicationConfigModel] = Field(
        alias="simulationApplications"
    )
    data_sources: List[DataSourceModel] = Field(alias="dataSources")
    tags: Dict[str, str] = Field(alias="tags")
    vpc_config: VPCConfigResponseModel = Field(alias="vpcConfig")
    network_interface: NetworkInterfaceModel = Field(alias="networkInterface")
    compute: ComputeResponseModel = Field(alias="compute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SimulationJobRequestModel(BaseModel):
    max_job_duration_in_seconds: int = Field(alias="maxJobDurationInSeconds")
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="outputLocation"
    )
    logging_config: Optional[LoggingConfigModel] = Field(
        default=None, alias="loggingConfig"
    )
    iam_role: Optional[str] = Field(default=None, alias="iamRole")
    failure_behavior: Optional[Literal["Continue", "Fail"]] = Field(
        default=None, alias="failureBehavior"
    )
    use_default_applications: Optional[bool] = Field(
        default=None, alias="useDefaultApplications"
    )
    robot_applications: Optional[List[RobotApplicationConfigModel]] = Field(
        default=None, alias="robotApplications"
    )
    simulation_applications: Optional[List[SimulationApplicationConfigModel]] = Field(
        default=None, alias="simulationApplications"
    )
    data_sources: Optional[List[DataSourceConfigModel]] = Field(
        default=None, alias="dataSources"
    )
    vpc_config: Optional[VPCConfigModel] = Field(default=None, alias="vpcConfig")
    compute: Optional[ComputeModel] = Field(default=None, alias="compute")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class SimulationJobModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[
        Literal[
            "Canceled",
            "Completed",
            "Failed",
            "Pending",
            "Preparing",
            "Restarting",
            "Running",
            "RunningFailed",
            "Terminated",
            "Terminating",
        ]
    ] = Field(default=None, alias="status")
    last_started_at: Optional[datetime] = Field(default=None, alias="lastStartedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    failure_behavior: Optional[Literal["Continue", "Fail"]] = Field(
        default=None, alias="failureBehavior"
    )
    failure_code: Optional[
        Literal[
            "BadPermissionsCloudwatchLogs",
            "BadPermissionsRobotApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsSimulationApplication",
            "BadPermissionsUserCredentials",
            "BatchCanceled",
            "BatchTimedOut",
            "ENILimitExceeded",
            "InternalServiceError",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidInput",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RequestThrottled",
            "ResourceNotFound",
            "RobotApplicationCrash",
            "RobotApplicationHealthCheckFailure",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationCrash",
            "SimulationApplicationHealthCheckFailure",
            "SimulationApplicationVersionMismatchedEtag",
            "SubnetIpLimitExceeded",
            "ThrottlingError",
            "UploadContentMismatchError",
            "WrongRegionRobotApplication",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionSimulationApplication",
        ]
    ] = Field(default=None, alias="failureCode")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="outputLocation"
    )
    logging_config: Optional[LoggingConfigModel] = Field(
        default=None, alias="loggingConfig"
    )
    max_job_duration_in_seconds: Optional[int] = Field(
        default=None, alias="maxJobDurationInSeconds"
    )
    simulation_time_millis: Optional[int] = Field(
        default=None, alias="simulationTimeMillis"
    )
    iam_role: Optional[str] = Field(default=None, alias="iamRole")
    robot_applications: Optional[List[RobotApplicationConfigModel]] = Field(
        default=None, alias="robotApplications"
    )
    simulation_applications: Optional[List[SimulationApplicationConfigModel]] = Field(
        default=None, alias="simulationApplications"
    )
    data_sources: Optional[List[DataSourceModel]] = Field(
        default=None, alias="dataSources"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    vpc_config: Optional[VPCConfigResponseModel] = Field(
        default=None, alias="vpcConfig"
    )
    network_interface: Optional[NetworkInterfaceModel] = Field(
        default=None, alias="networkInterface"
    )
    compute: Optional[ComputeResponseModel] = Field(default=None, alias="compute")


class FailedCreateSimulationJobRequestModel(BaseModel):
    request: Optional[SimulationJobRequestModel] = Field(default=None, alias="request")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    failure_code: Optional[
        Literal[
            "BadPermissionsCloudwatchLogs",
            "BadPermissionsRobotApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsSimulationApplication",
            "BadPermissionsUserCredentials",
            "BatchCanceled",
            "BatchTimedOut",
            "ENILimitExceeded",
            "InternalServiceError",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidInput",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RequestThrottled",
            "ResourceNotFound",
            "RobotApplicationCrash",
            "RobotApplicationHealthCheckFailure",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationCrash",
            "SimulationApplicationHealthCheckFailure",
            "SimulationApplicationVersionMismatchedEtag",
            "SubnetIpLimitExceeded",
            "ThrottlingError",
            "UploadContentMismatchError",
            "WrongRegionRobotApplication",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionSimulationApplication",
        ]
    ] = Field(default=None, alias="failureCode")
    failed_at: Optional[datetime] = Field(default=None, alias="failedAt")


class StartSimulationJobBatchRequestModel(BaseModel):
    create_simulation_job_requests: Sequence[SimulationJobRequestModel] = Field(
        alias="createSimulationJobRequests"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    batch_policy: Optional[BatchPolicyModel] = Field(default=None, alias="batchPolicy")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class BatchDescribeSimulationJobResponseModel(BaseModel):
    jobs: List[SimulationJobModel] = Field(alias="jobs")
    unprocessed_jobs: List[str] = Field(alias="unprocessedJobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSimulationJobBatchResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled",
        "Canceling",
        "Completed",
        "Completing",
        "Failed",
        "InProgress",
        "Pending",
        "TimedOut",
        "TimingOut",
    ] = Field(alias="status")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    created_at: datetime = Field(alias="createdAt")
    client_request_token: str = Field(alias="clientRequestToken")
    batch_policy: BatchPolicyModel = Field(alias="batchPolicy")
    failure_code: Literal["InternalServiceError"] = Field(alias="failureCode")
    failure_reason: str = Field(alias="failureReason")
    failed_requests: List[FailedCreateSimulationJobRequestModel] = Field(
        alias="failedRequests"
    )
    pending_requests: List[SimulationJobRequestModel] = Field(alias="pendingRequests")
    created_requests: List[SimulationJobSummaryModel] = Field(alias="createdRequests")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSimulationJobBatchResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal[
        "Canceled",
        "Canceling",
        "Completed",
        "Completing",
        "Failed",
        "InProgress",
        "Pending",
        "TimedOut",
        "TimingOut",
    ] = Field(alias="status")
    created_at: datetime = Field(alias="createdAt")
    client_request_token: str = Field(alias="clientRequestToken")
    batch_policy: BatchPolicyModel = Field(alias="batchPolicy")
    failure_code: Literal["InternalServiceError"] = Field(alias="failureCode")
    failure_reason: str = Field(alias="failureReason")
    failed_requests: List[FailedCreateSimulationJobRequestModel] = Field(
        alias="failedRequests"
    )
    pending_requests: List[SimulationJobRequestModel] = Field(alias="pendingRequests")
    created_requests: List[SimulationJobSummaryModel] = Field(alias="createdRequests")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
