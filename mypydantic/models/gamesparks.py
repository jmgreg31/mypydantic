# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ConnectionModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    id: Optional[str] = Field(default=None, alias="Id")


class CreateGameRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GameDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "DELETING"]] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateSnapshotRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateStageRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    role: str = Field(alias="Role")
    stage_name: str = Field(alias="StageName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class StageDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    game_key: Optional[str] = Field(default=None, alias="GameKey")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")
    name: Optional[str] = Field(default=None, alias="Name")
    role: Optional[str] = Field(default=None, alias="Role")
    state: Optional[Literal["ACTIVE", "DELETING"]] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DeleteGameRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")


class DeleteStageRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")


class DeploymentResultModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    result_code: Optional[
        Literal["INVALID_ROLE_FAILURE", "SUCCESS", "UNSPECIFIED_FAILURE"]
    ] = Field(default=None, alias="ResultCode")


class DisconnectPlayerRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    player_id: str = Field(alias="PlayerId")
    stage_name: str = Field(alias="StageName")


class ExportSnapshotRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")


class ExtensionDetailsModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class ExtensionVersionDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    schema_: Optional[str] = Field(default=None, alias="Schema")
    version: Optional[str] = Field(default=None, alias="Version")


class SectionModel(BaseModel):
    attributes: Optional[Dict[str, Any]] = Field(default=None, alias="Attributes")
    name: Optional[str] = Field(default=None, alias="Name")
    size: Optional[int] = Field(default=None, alias="Size")


class GameSummaryModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "DELETING"]] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GeneratedCodeJobDetailsModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")
    generated_code_job_id: Optional[str] = Field(
        default=None, alias="GeneratedCodeJobId"
    )
    s3_url: Optional[str] = Field(default=None, alias="S3Url")
    status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]] = Field(
        default=None, alias="Status"
    )


class GeneratorModel(BaseModel):
    game_sdk_version: Optional[str] = Field(default=None, alias="GameSdkVersion")
    language: Optional[str] = Field(default=None, alias="Language")
    target_platform: Optional[str] = Field(default=None, alias="TargetPlatform")


class GetExtensionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    namespace: str = Field(alias="Namespace")


class GetExtensionVersionRequestModel(BaseModel):
    extension_version: str = Field(alias="ExtensionVersion")
    name: str = Field(alias="Name")
    namespace: str = Field(alias="Namespace")


class GetGameConfigurationRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    sections: Optional[Sequence[str]] = Field(default=None, alias="Sections")


class GetGameRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")


class GetGeneratedCodeJobRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    job_id: str = Field(alias="JobId")
    snapshot_id: str = Field(alias="SnapshotId")


class GetPlayerConnectionStatusRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    player_id: str = Field(alias="PlayerId")
    stage_name: str = Field(alias="StageName")


class GetSnapshotRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")
    sections: Optional[Sequence[str]] = Field(default=None, alias="Sections")


class GetStageDeploymentRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")


class GetStageRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")


class ImportGameConfigurationSourceModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="File")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListExtensionVersionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    namespace: str = Field(alias="Namespace")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExtensionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGamesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGeneratedCodeJobsRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSnapshotsRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SnapshotSummaryModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    id: Optional[str] = Field(default=None, alias="Id")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")


class ListStageDeploymentsRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListStagesRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StageSummaryModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    game_key: Optional[str] = Field(default=None, alias="GameKey")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "DELETING"]] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class SectionModificationModel(BaseModel):
    operation: Literal["ADD", "REMOVE", "REPLACE"] = Field(alias="Operation")
    path: str = Field(alias="Path")
    section: str = Field(alias="Section")
    value: Optional[Mapping[str, Any]] = Field(default=None, alias="Value")


class StartStageDeploymentRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")
    stage_name: str = Field(alias="StageName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateGameRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateSnapshotRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateStageRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")
    description: Optional[str] = Field(default=None, alias="Description")
    role: Optional[str] = Field(default=None, alias="Role")


class CreateGameResultModel(BaseModel):
    game: GameDetailsModel = Field(alias="Game")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisconnectPlayerResultModel(BaseModel):
    disconnect_failures: List[str] = Field(alias="DisconnectFailures")
    disconnect_successes: List[str] = Field(alias="DisconnectSuccesses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportSnapshotResultModel(BaseModel):
    s3_url: str = Field(alias="S3Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGameResultModel(BaseModel):
    game: GameDetailsModel = Field(alias="Game")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPlayerConnectionStatusResultModel(BaseModel):
    connections: List[ConnectionModel] = Field(alias="Connections")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartGeneratedCodeJobResultModel(BaseModel):
    generated_code_job_id: str = Field(alias="GeneratedCodeJobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameResultModel(BaseModel):
    game: GameDetailsModel = Field(alias="Game")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStageResultModel(BaseModel):
    stage: StageDetailsModel = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStageResultModel(BaseModel):
    stage: StageDetailsModel = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStageResultModel(BaseModel):
    stage: StageDetailsModel = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StageDeploymentDetailsModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    deployment_action: Optional[Literal["DEPLOY", "UNDEPLOY"]] = Field(
        default=None, alias="DeploymentAction"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    deployment_result: Optional[DeploymentResultModel] = Field(
        default=None, alias="DeploymentResult"
    )
    deployment_state: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
    ] = Field(default=None, alias="DeploymentState")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")


class StageDeploymentSummaryModel(BaseModel):
    deployment_action: Optional[Literal["DEPLOY", "UNDEPLOY"]] = Field(
        default=None, alias="DeploymentAction"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    deployment_result: Optional[DeploymentResultModel] = Field(
        default=None, alias="DeploymentResult"
    )
    deployment_state: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
    ] = Field(default=None, alias="DeploymentState")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")


class GetExtensionResultModel(BaseModel):
    extension: ExtensionDetailsModel = Field(alias="Extension")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExtensionsResultModel(BaseModel):
    extensions: List[ExtensionDetailsModel] = Field(alias="Extensions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExtensionVersionResultModel(BaseModel):
    extension_version: ExtensionVersionDetailsModel = Field(alias="ExtensionVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExtensionVersionsResultModel(BaseModel):
    extension_versions: List[ExtensionVersionDetailsModel] = Field(
        alias="ExtensionVersions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GameConfigurationDetailsModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    sections: Optional[Dict[str, SectionModel]] = Field(default=None, alias="Sections")


class SnapshotDetailsModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    id: Optional[str] = Field(default=None, alias="Id")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    sections: Optional[Dict[str, SectionModel]] = Field(default=None, alias="Sections")


class ListGamesResultModel(BaseModel):
    games: List[GameSummaryModel] = Field(alias="Games")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGeneratedCodeJobResultModel(BaseModel):
    generated_code_job: GeneratedCodeJobDetailsModel = Field(alias="GeneratedCodeJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGeneratedCodeJobsResultModel(BaseModel):
    generated_code_jobs: List[GeneratedCodeJobDetailsModel] = Field(
        alias="GeneratedCodeJobs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartGeneratedCodeJobRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    generator: GeneratorModel = Field(alias="Generator")
    snapshot_id: str = Field(alias="SnapshotId")


class ImportGameConfigurationRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    import_source: ImportGameConfigurationSourceModel = Field(alias="ImportSource")


class ListExtensionVersionsRequestListExtensionVersionsPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    namespace: str = Field(alias="Namespace")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExtensionsRequestListExtensionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGamesRequestListGamesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGeneratedCodeJobsRequestListGeneratedCodeJobsPaginateModel(BaseModel):
    game_name: str = Field(alias="GameName")
    snapshot_id: str = Field(alias="SnapshotId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSnapshotsRequestListSnapshotsPaginateModel(BaseModel):
    game_name: str = Field(alias="GameName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStageDeploymentsRequestListStageDeploymentsPaginateModel(BaseModel):
    game_name: str = Field(alias="GameName")
    stage_name: str = Field(alias="StageName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStagesRequestListStagesPaginateModel(BaseModel):
    game_name: str = Field(alias="GameName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSnapshotsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    snapshots: List[SnapshotSummaryModel] = Field(alias="Snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStagesResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    stages: List[StageSummaryModel] = Field(alias="Stages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameConfigurationRequestModel(BaseModel):
    game_name: str = Field(alias="GameName")
    modifications: Sequence[SectionModificationModel] = Field(alias="Modifications")


class GetStageDeploymentResultModel(BaseModel):
    stage_deployment: StageDeploymentDetailsModel = Field(alias="StageDeployment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartStageDeploymentResultModel(BaseModel):
    stage_deployment: StageDeploymentDetailsModel = Field(alias="StageDeployment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStageDeploymentsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    stage_deployments: List[StageDeploymentSummaryModel] = Field(
        alias="StageDeployments"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGameConfigurationResultModel(BaseModel):
    game_configuration: GameConfigurationDetailsModel = Field(alias="GameConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportGameConfigurationResultModel(BaseModel):
    game_configuration: GameConfigurationDetailsModel = Field(alias="GameConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameConfigurationResultModel(BaseModel):
    game_configuration: GameConfigurationDetailsModel = Field(alias="GameConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotResultModel(BaseModel):
    snapshot: SnapshotDetailsModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnapshotResultModel(BaseModel):
    snapshot: SnapshotDetailsModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSnapshotResultModel(BaseModel):
    snapshot: SnapshotDetailsModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
