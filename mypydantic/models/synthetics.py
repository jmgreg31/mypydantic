# Model Generated: Thu Mar  2 21:56:24 2023

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


class S3EncryptionConfigModel(BaseModel):
    encryption_mode: Optional[Literal["SSE_KMS", "SSE_S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class AssociateResourceRequestModel(BaseModel):
    group_identifier: str = Field(alias="GroupIdentifier")
    resource_arn: str = Field(alias="ResourceArn")


class BaseScreenshotModel(BaseModel):
    screenshot_name: str = Field(alias="ScreenshotName")
    ignore_coordinates: Optional[List[str]] = Field(
        default=None, alias="IgnoreCoordinates"
    )


class CanaryCodeInputModel(BaseModel):
    handler: str = Field(alias="Handler")
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_version: Optional[str] = Field(default=None, alias="S3Version")
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )


class CanaryCodeOutputModel(BaseModel):
    source_location_arn: Optional[str] = Field(default=None, alias="SourceLocationArn")
    handler: Optional[str] = Field(default=None, alias="Handler")


class CanaryRunConfigInputModel(BaseModel):
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")
    memory_in_mb: Optional[int] = Field(default=None, alias="MemoryInMB")
    active_tracing: Optional[bool] = Field(default=None, alias="ActiveTracing")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="EnvironmentVariables"
    )


class CanaryRunConfigOutputModel(BaseModel):
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")
    memory_in_mb: Optional[int] = Field(default=None, alias="MemoryInMB")
    active_tracing: Optional[bool] = Field(default=None, alias="ActiveTracing")


class CanaryRunStatusModel(BaseModel):
    state: Optional[Literal["FAILED", "PASSED", "RUNNING"]] = Field(
        default=None, alias="State"
    )
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    state_reason_code: Optional[Literal["CANARY_FAILURE", "EXECUTION_FAILURE"]] = Field(
        default=None, alias="StateReasonCode"
    )


class CanaryRunTimelineModel(BaseModel):
    started: Optional[datetime] = Field(default=None, alias="Started")
    completed: Optional[datetime] = Field(default=None, alias="Completed")


class CanaryScheduleInputModel(BaseModel):
    expression: str = Field(alias="Expression")
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class CanaryScheduleOutputModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="Expression")
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class CanaryStatusModel(BaseModel):
    state: Optional[
        Literal[
            "CREATING",
            "DELETING",
            "ERROR",
            "READY",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    state_reason_code: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "CREATE_PENDING",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "INVALID_PERMISSIONS",
            "ROLLBACK_COMPLETE",
            "ROLLBACK_FAILED",
            "SYNC_DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_PENDING",
        ]
    ] = Field(default=None, alias="StateReasonCode")


class CanaryTimelineModel(BaseModel):
    created: Optional[datetime] = Field(default=None, alias="Created")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    last_started: Optional[datetime] = Field(default=None, alias="LastStarted")
    last_stopped: Optional[datetime] = Field(default=None, alias="LastStopped")


class VpcConfigOutputModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class VpcConfigInputModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class DeleteCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    delete_lambda: Optional[bool] = Field(default=None, alias="DeleteLambda")


class DeleteGroupRequestModel(BaseModel):
    group_identifier: str = Field(alias="GroupIdentifier")


class DescribeCanariesLastRunRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")


class DescribeCanariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")


class DescribeRuntimeVersionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RuntimeVersionModel(BaseModel):
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    description: Optional[str] = Field(default=None, alias="Description")
    release_date: Optional[datetime] = Field(default=None, alias="ReleaseDate")
    deprecation_date: Optional[datetime] = Field(default=None, alias="DeprecationDate")


class DisassociateResourceRequestModel(BaseModel):
    group_identifier: str = Field(alias="GroupIdentifier")
    resource_arn: str = Field(alias="ResourceArn")


class GetCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetCanaryRunsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetGroupRequestModel(BaseModel):
    group_identifier: str = Field(alias="GroupIdentifier")


class GroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListAssociatedGroupsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGroupResourcesRequestModel(BaseModel):
    group_identifier: str = Field(alias="GroupIdentifier")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class StartCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StopCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ArtifactConfigInputModel(BaseModel):
    s3_encryption: Optional[S3EncryptionConfigModel] = Field(
        default=None, alias="S3Encryption"
    )


class ArtifactConfigOutputModel(BaseModel):
    s3_encryption: Optional[S3EncryptionConfigModel] = Field(
        default=None, alias="S3Encryption"
    )


class VisualReferenceInputModel(BaseModel):
    base_canary_run_id: str = Field(alias="BaseCanaryRunId")
    base_screenshots: Optional[Sequence[BaseScreenshotModel]] = Field(
        default=None, alias="BaseScreenshots"
    )


class VisualReferenceOutputModel(BaseModel):
    base_screenshots: Optional[List[BaseScreenshotModel]] = Field(
        default=None, alias="BaseScreenshots"
    )
    base_canary_run_id: Optional[str] = Field(default=None, alias="BaseCanaryRunId")


class CanaryRunModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[CanaryRunStatusModel] = Field(default=None, alias="Status")
    timeline: Optional[CanaryRunTimelineModel] = Field(default=None, alias="Timeline")
    artifact_s3_location: Optional[str] = Field(
        default=None, alias="ArtifactS3Location"
    )


class ListGroupResourcesResponseModel(BaseModel):
    resources: List[str] = Field(alias="Resources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRuntimeVersionsResponseModel(BaseModel):
    runtime_versions: List[RuntimeVersionModel] = Field(alias="RuntimeVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedGroupsResponseModel(BaseModel):
    groups: List[GroupSummaryModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupSummaryModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    code: CanaryCodeInputModel = Field(alias="Code")
    artifact_s3_location: str = Field(alias="ArtifactS3Location")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    schedule: CanaryScheduleInputModel = Field(alias="Schedule")
    runtime_version: str = Field(alias="RuntimeVersion")
    run_config: Optional[CanaryRunConfigInputModel] = Field(
        default=None, alias="RunConfig"
    )
    success_retention_period_in_days: Optional[int] = Field(
        default=None, alias="SuccessRetentionPeriodInDays"
    )
    failure_retention_period_in_days: Optional[int] = Field(
        default=None, alias="FailureRetentionPeriodInDays"
    )
    vpc_config: Optional[VpcConfigInputModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    artifact_config: Optional[ArtifactConfigInputModel] = Field(
        default=None, alias="ArtifactConfig"
    )


class UpdateCanaryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    code: Optional[CanaryCodeInputModel] = Field(default=None, alias="Code")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    runtime_version: Optional[str] = Field(default=None, alias="RuntimeVersion")
    schedule: Optional[CanaryScheduleInputModel] = Field(default=None, alias="Schedule")
    run_config: Optional[CanaryRunConfigInputModel] = Field(
        default=None, alias="RunConfig"
    )
    success_retention_period_in_days: Optional[int] = Field(
        default=None, alias="SuccessRetentionPeriodInDays"
    )
    failure_retention_period_in_days: Optional[int] = Field(
        default=None, alias="FailureRetentionPeriodInDays"
    )
    vpc_config: Optional[VpcConfigInputModel] = Field(default=None, alias="VpcConfig")
    visual_reference: Optional[VisualReferenceInputModel] = Field(
        default=None, alias="VisualReference"
    )
    artifact_s3_location: Optional[str] = Field(
        default=None, alias="ArtifactS3Location"
    )
    artifact_config: Optional[ArtifactConfigInputModel] = Field(
        default=None, alias="ArtifactConfig"
    )


class CanaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    code: Optional[CanaryCodeOutputModel] = Field(default=None, alias="Code")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    schedule: Optional[CanaryScheduleOutputModel] = Field(
        default=None, alias="Schedule"
    )
    run_config: Optional[CanaryRunConfigOutputModel] = Field(
        default=None, alias="RunConfig"
    )
    success_retention_period_in_days: Optional[int] = Field(
        default=None, alias="SuccessRetentionPeriodInDays"
    )
    failure_retention_period_in_days: Optional[int] = Field(
        default=None, alias="FailureRetentionPeriodInDays"
    )
    status: Optional[CanaryStatusModel] = Field(default=None, alias="Status")
    timeline: Optional[CanaryTimelineModel] = Field(default=None, alias="Timeline")
    artifact_s3_location: Optional[str] = Field(
        default=None, alias="ArtifactS3Location"
    )
    engine_arn: Optional[str] = Field(default=None, alias="EngineArn")
    runtime_version: Optional[str] = Field(default=None, alias="RuntimeVersion")
    vpc_config: Optional[VpcConfigOutputModel] = Field(default=None, alias="VpcConfig")
    visual_reference: Optional[VisualReferenceOutputModel] = Field(
        default=None, alias="VisualReference"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    artifact_config: Optional[ArtifactConfigOutputModel] = Field(
        default=None, alias="ArtifactConfig"
    )


class CanaryLastRunModel(BaseModel):
    canary_name: Optional[str] = Field(default=None, alias="CanaryName")
    last_run: Optional[CanaryRunModel] = Field(default=None, alias="LastRun")


class GetCanaryRunsResponseModel(BaseModel):
    canary_runs: List[CanaryRunModel] = Field(alias="CanaryRuns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCanaryResponseModel(BaseModel):
    canary: CanaryModel = Field(alias="Canary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCanariesResponseModel(BaseModel):
    canaries: List[CanaryModel] = Field(alias="Canaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCanaryResponseModel(BaseModel):
    canary: CanaryModel = Field(alias="Canary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCanariesLastRunResponseModel(BaseModel):
    canaries_last_run: List[CanaryLastRunModel] = Field(alias="CanariesLastRun")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
