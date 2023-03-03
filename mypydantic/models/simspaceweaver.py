# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CloudWatchLogsLogGroupModel(BaseModel):
    log_group_arn: Optional[str] = Field(default=None, alias="LogGroupArn")


class DeleteAppInputRequestModel(BaseModel):
    app: str = Field(alias="App")
    domain: str = Field(alias="Domain")
    simulation: str = Field(alias="Simulation")


class DeleteSimulationInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")


class DescribeAppInputRequestModel(BaseModel):
    app: str = Field(alias="App")
    domain: str = Field(alias="Domain")
    simulation: str = Field(alias="Simulation")


class LaunchOverridesModel(BaseModel):
    launch_commands: Optional[List[str]] = Field(default=None, alias="LaunchCommands")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeSimulationInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")


class S3LocationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    object_key: Optional[str] = Field(default=None, alias="ObjectKey")


class DomainModel(BaseModel):
    lifecycle: Optional[
        Literal["ByRequest", "BySpatialSubdivision", "PerWorker", "Unknown"]
    ] = Field(default=None, alias="Lifecycle")
    name: Optional[str] = Field(default=None, alias="Name")


class ListAppsInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")
    domain: Optional[str] = Field(default=None, alias="Domain")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SimulationAppMetadataModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    name: Optional[str] = Field(default=None, alias="Name")
    simulation: Optional[str] = Field(default=None, alias="Simulation")
    status: Optional[
        Literal["ERROR", "STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"]
    ] = Field(default=None, alias="Status")
    target_status: Optional[Literal["STARTED", "STOPPED", "UNKNOWN"]] = Field(
        default=None, alias="TargetStatus"
    )


class ListSimulationsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SimulationMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "DELETED",
            "DELETING",
            "FAILED",
            "STARTED",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "UNKNOWN",
        ]
    ] = Field(default=None, alias="Status")
    target_status: Optional[
        Literal["DELETED", "STARTED", "STOPPED", "UNKNOWN"]
    ] = Field(default=None, alias="TargetStatus")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class SimulationClockModel(BaseModel):
    status: Optional[
        Literal["STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"]
    ] = Field(default=None, alias="Status")
    target_status: Optional[Literal["STARTED", "STOPPED", "UNKNOWN"]] = Field(
        default=None, alias="TargetStatus"
    )


class SimulationAppPortMappingModel(BaseModel):
    actual: Optional[int] = Field(default=None, alias="Actual")
    declared: Optional[int] = Field(default=None, alias="Declared")


class StartClockInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")


class StopAppInputRequestModel(BaseModel):
    app: str = Field(alias="App")
    domain: str = Field(alias="Domain")
    simulation: str = Field(alias="Simulation")


class StopClockInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")


class StopSimulationInputRequestModel(BaseModel):
    simulation: str = Field(alias="Simulation")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class LogDestinationModel(BaseModel):
    cloud_watch_logs_log_group: Optional[CloudWatchLogsLogGroupModel] = Field(
        default=None, alias="CloudWatchLogsLogGroup"
    )


class StartAppInputRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    name: str = Field(alias="Name")
    simulation: str = Field(alias="Simulation")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    launch_overrides: Optional[LaunchOverridesModel] = Field(
        default=None, alias="LaunchOverrides"
    )


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAppOutputModel(BaseModel):
    domain: str = Field(alias="Domain")
    name: str = Field(alias="Name")
    simulation: str = Field(alias="Simulation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSimulationOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    execution_id: str = Field(alias="ExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSimulationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    schema_s3_location: S3LocationModel = Field(alias="SchemaS3Location")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    maximum_duration: Optional[str] = Field(default=None, alias="MaximumDuration")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListAppsOutputModel(BaseModel):
    apps: List[SimulationAppMetadataModel] = Field(alias="Apps")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSimulationsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    simulations: List[SimulationMetadataModel] = Field(alias="Simulations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LiveSimulationStateModel(BaseModel):
    clocks: Optional[List[SimulationClockModel]] = Field(default=None, alias="Clocks")
    domains: Optional[List[DomainModel]] = Field(default=None, alias="Domains")


class SimulationAppEndpointInfoModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    ingress_port_mappings: Optional[List[SimulationAppPortMappingModel]] = Field(
        default=None, alias="IngressPortMappings"
    )


class LoggingConfigurationModel(BaseModel):
    destinations: Optional[List[LogDestinationModel]] = Field(
        default=None, alias="Destinations"
    )


class DescribeAppOutputModel(BaseModel):
    description: str = Field(alias="Description")
    domain: str = Field(alias="Domain")
    endpoint_info: SimulationAppEndpointInfoModel = Field(alias="EndpointInfo")
    launch_overrides: LaunchOverridesModel = Field(alias="LaunchOverrides")
    name: str = Field(alias="Name")
    simulation: str = Field(alias="Simulation")
    status: Literal[
        "ERROR", "STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"
    ] = Field(alias="Status")
    target_status: Literal["STARTED", "STOPPED", "UNKNOWN"] = Field(
        alias="TargetStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSimulationOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    execution_id: str = Field(alias="ExecutionId")
    live_simulation_state: LiveSimulationStateModel = Field(alias="LiveSimulationState")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    maximum_duration: str = Field(alias="MaximumDuration")
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    schema_error: str = Field(alias="SchemaError")
    schema_s3_location: S3LocationModel = Field(alias="SchemaS3Location")
    status: Literal[
        "DELETED",
        "DELETING",
        "FAILED",
        "STARTED",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "UNKNOWN",
    ] = Field(alias="Status")
    target_status: Literal["DELETED", "STARTED", "STOPPED", "UNKNOWN"] = Field(
        alias="TargetStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
