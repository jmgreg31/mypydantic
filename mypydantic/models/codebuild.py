# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchDeleteBuildsInputRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")


class BuildNotDeletedModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    status_code: Optional[str] = Field(default=None, alias="statusCode")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetBuildBatchesInputRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")


class BatchGetBuildsInputRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")


class BatchGetProjectsInputRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="names")


class BatchGetReportGroupsInputRequestModel(BaseModel):
    report_group_arns: Sequence[str] = Field(alias="reportGroupArns")


class BatchGetReportsInputRequestModel(BaseModel):
    report_arns: Sequence[str] = Field(alias="reportArns")


class BatchRestrictionsModel(BaseModel):
    maximum_builds_allowed: Optional[int] = Field(
        default=None, alias="maximumBuildsAllowed"
    )
    compute_types_allowed: Optional[List[str]] = Field(
        default=None, alias="computeTypesAllowed"
    )


class BuildArtifactsModel(BaseModel):
    location: Optional[str] = Field(default=None, alias="location")
    sha256sum: Optional[str] = Field(default=None, alias="sha256sum")
    md5sum: Optional[str] = Field(default=None, alias="md5sum")
    override_artifact_name: Optional[bool] = Field(
        default=None, alias="overrideArtifactName"
    )
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="encryptionDisabled"
    )
    artifact_identifier: Optional[str] = Field(default=None, alias="artifactIdentifier")
    bucket_owner_access: Optional[Literal["FULL", "NONE", "READ_ONLY"]] = Field(
        default=None, alias="bucketOwnerAccess"
    )


class BuildBatchFilterModel(BaseModel):
    status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="status")


class PhaseContextModel(BaseModel):
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    message: Optional[str] = Field(default=None, alias="message")


class ProjectCacheModel(BaseModel):
    type: Literal["LOCAL", "NO_CACHE", "S3"] = Field(alias="type")
    location: Optional[str] = Field(default=None, alias="location")
    modes: Optional[
        List[
            Literal[
                "LOCAL_CUSTOM_CACHE", "LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE"
            ]
        ]
    ] = Field(default=None, alias="modes")


class ProjectFileSystemLocationModel(BaseModel):
    type: Optional[Literal["EFS"]] = Field(default=None, alias="type")
    location: Optional[str] = Field(default=None, alias="location")
    mount_point: Optional[str] = Field(default=None, alias="mountPoint")
    identifier: Optional[str] = Field(default=None, alias="identifier")
    mount_options: Optional[str] = Field(default=None, alias="mountOptions")


class ProjectSourceVersionModel(BaseModel):
    source_identifier: str = Field(alias="sourceIdentifier")
    source_version: str = Field(alias="sourceVersion")


class VpcConfigModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    subnets: Optional[List[str]] = Field(default=None, alias="subnets")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )


class BuildStatusConfigModel(BaseModel):
    context: Optional[str] = Field(default=None, alias="context")
    target_url: Optional[str] = Field(default=None, alias="targetUrl")


class ResolvedArtifactModel(BaseModel):
    type: Optional[Literal["CODEPIPELINE", "NO_ARTIFACTS", "S3"]] = Field(
        default=None, alias="type"
    )
    location: Optional[str] = Field(default=None, alias="location")
    identifier: Optional[str] = Field(default=None, alias="identifier")


class DebugSessionModel(BaseModel):
    session_enabled: Optional[bool] = Field(default=None, alias="sessionEnabled")
    session_target: Optional[str] = Field(default=None, alias="sessionTarget")


class ExportedEnvironmentVariableModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class NetworkInterfaceModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    network_interface_id: Optional[str] = Field(
        default=None, alias="networkInterfaceId"
    )


class CloudWatchLogsConfigModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")
    group_name: Optional[str] = Field(default=None, alias="groupName")
    stream_name: Optional[str] = Field(default=None, alias="streamName")


class CodeCoverageReportSummaryModel(BaseModel):
    line_coverage_percentage: Optional[float] = Field(
        default=None, alias="lineCoveragePercentage"
    )
    lines_covered: Optional[int] = Field(default=None, alias="linesCovered")
    lines_missed: Optional[int] = Field(default=None, alias="linesMissed")
    branch_coverage_percentage: Optional[float] = Field(
        default=None, alias="branchCoveragePercentage"
    )
    branches_covered: Optional[int] = Field(default=None, alias="branchesCovered")
    branches_missed: Optional[int] = Field(default=None, alias="branchesMissed")


class CodeCoverageModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    report_arn: Optional[str] = Field(default=None, alias="reportARN")
    file_path: Optional[str] = Field(default=None, alias="filePath")
    line_coverage_percentage: Optional[float] = Field(
        default=None, alias="lineCoveragePercentage"
    )
    lines_covered: Optional[int] = Field(default=None, alias="linesCovered")
    lines_missed: Optional[int] = Field(default=None, alias="linesMissed")
    branch_coverage_percentage: Optional[float] = Field(
        default=None, alias="branchCoveragePercentage"
    )
    branches_covered: Optional[int] = Field(default=None, alias="branchesCovered")
    branches_missed: Optional[int] = Field(default=None, alias="branchesMissed")
    expired: Optional[datetime] = Field(default=None, alias="expired")


class ProjectArtifactsModel(BaseModel):
    type: Literal["CODEPIPELINE", "NO_ARTIFACTS", "S3"] = Field(alias="type")
    location: Optional[str] = Field(default=None, alias="location")
    path: Optional[str] = Field(default=None, alias="path")
    namespace_type: Optional[Literal["BUILD_ID", "NONE"]] = Field(
        default=None, alias="namespaceType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    packaging: Optional[Literal["NONE", "ZIP"]] = Field(default=None, alias="packaging")
    override_artifact_name: Optional[bool] = Field(
        default=None, alias="overrideArtifactName"
    )
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="encryptionDisabled"
    )
    artifact_identifier: Optional[str] = Field(default=None, alias="artifactIdentifier")
    bucket_owner_access: Optional[Literal["FULL", "NONE", "READ_ONLY"]] = Field(
        default=None, alias="bucketOwnerAccess"
    )


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class WebhookFilterModel(BaseModel):
    type: Literal[
        "ACTOR_ACCOUNT_ID",
        "BASE_REF",
        "COMMIT_MESSAGE",
        "EVENT",
        "FILE_PATH",
        "HEAD_REF",
    ] = Field(alias="type")
    pattern: str = Field(alias="pattern")
    exclude_matched_pattern: Optional[bool] = Field(
        default=None, alias="excludeMatchedPattern"
    )


class DeleteBuildBatchInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteProjectInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteReportGroupInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    delete_reports: Optional[bool] = Field(default=None, alias="deleteReports")


class DeleteReportInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteResourcePolicyInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class DeleteSourceCredentialsInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteWebhookInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeCodeCoveragesInputRequestModel(BaseModel):
    report_arn: str = Field(alias="reportArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["FILE_PATH", "LINE_COVERAGE_PERCENTAGE"]] = Field(
        default=None, alias="sortBy"
    )
    min_line_coverage_percentage: Optional[float] = Field(
        default=None, alias="minLineCoveragePercentage"
    )
    max_line_coverage_percentage: Optional[float] = Field(
        default=None, alias="maxLineCoveragePercentage"
    )


class TestCaseFilterModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="status")
    keyword: Optional[str] = Field(default=None, alias="keyword")


class TestCaseModel(BaseModel):
    report_arn: Optional[str] = Field(default=None, alias="reportArn")
    test_raw_data_path: Optional[str] = Field(default=None, alias="testRawDataPath")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[str] = Field(default=None, alias="status")
    duration_in_nano_seconds: Optional[int] = Field(
        default=None, alias="durationInNanoSeconds"
    )
    message: Optional[str] = Field(default=None, alias="message")
    expired: Optional[datetime] = Field(default=None, alias="expired")


class EnvironmentImageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    versions: Optional[List[str]] = Field(default=None, alias="versions")


class EnvironmentVariableModel(BaseModel):
    name: str = Field(alias="name")
    value: str = Field(alias="value")
    type: Optional[Literal["PARAMETER_STORE", "PLAINTEXT", "SECRETS_MANAGER"]] = Field(
        default=None, alias="type"
    )


class GetReportGroupTrendInputRequestModel(BaseModel):
    report_group_arn: str = Field(alias="reportGroupArn")
    trend_field: Literal[
        "BRANCHES_COVERED",
        "BRANCHES_MISSED",
        "BRANCH_COVERAGE",
        "DURATION",
        "LINES_COVERED",
        "LINES_MISSED",
        "LINE_COVERAGE",
        "PASS_RATE",
        "TOTAL",
    ] = Field(alias="trendField")
    num_of_reports: Optional[int] = Field(default=None, alias="numOfReports")


class ReportGroupTrendStatsModel(BaseModel):
    average: Optional[str] = Field(default=None, alias="average")
    max: Optional[str] = Field(default=None, alias="max")
    min: Optional[str] = Field(default=None, alias="min")


class ReportWithRawDataModel(BaseModel):
    report_arn: Optional[str] = Field(default=None, alias="reportArn")
    data: Optional[str] = Field(default=None, alias="data")


class GetResourcePolicyInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class GitSubmodulesConfigModel(BaseModel):
    fetch_submodules: bool = Field(alias="fetchSubmodules")


class ImportSourceCredentialsInputRequestModel(BaseModel):
    token: str = Field(alias="token")
    server_type: Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"] = Field(
        alias="serverType"
    )
    auth_type: Literal["BASIC_AUTH", "OAUTH", "PERSONAL_ACCESS_TOKEN"] = Field(
        alias="authType"
    )
    username: Optional[str] = Field(default=None, alias="username")
    should_overwrite: Optional[bool] = Field(default=None, alias="shouldOverwrite")


class InvalidateProjectCacheInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")


class ListBuildsForProjectInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBuildsInputRequestModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListProjectsInputRequestModel(BaseModel):
    sort_by: Optional[Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReportGroupsInputRequestModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="sortBy"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ReportFilterModel(BaseModel):
    status: Optional[
        Literal["DELETING", "FAILED", "GENERATING", "INCOMPLETE", "SUCCEEDED"]
    ] = Field(default=None, alias="status")


class ListSharedProjectsInputRequestModel(BaseModel):
    sort_by: Optional[Literal["ARN", "MODIFIED_TIME"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSharedReportGroupsInputRequestModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["ARN", "MODIFIED_TIME"]] = Field(
        default=None, alias="sortBy"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SourceCredentialsInfoModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    server_type: Optional[Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"]] = Field(
        default=None, alias="serverType"
    )
    auth_type: Optional[
        Literal["BASIC_AUTH", "OAUTH", "PERSONAL_ACCESS_TOKEN"]
    ] = Field(default=None, alias="authType")


class S3LogsConfigModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")
    location: Optional[str] = Field(default=None, alias="location")
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="encryptionDisabled"
    )
    bucket_owner_access: Optional[Literal["FULL", "NONE", "READ_ONLY"]] = Field(
        default=None, alias="bucketOwnerAccess"
    )


class ProjectBadgeModel(BaseModel):
    badge_enabled: Optional[bool] = Field(default=None, alias="badgeEnabled")
    badge_request_url: Optional[str] = Field(default=None, alias="badgeRequestUrl")


class RegistryCredentialModel(BaseModel):
    credential: str = Field(alias="credential")
    credential_provider: Literal["SECRETS_MANAGER"] = Field(alias="credentialProvider")


class SourceAuthModel(BaseModel):
    type: Literal["OAUTH"] = Field(alias="type")
    resource: Optional[str] = Field(default=None, alias="resource")


class PutResourcePolicyInputRequestModel(BaseModel):
    policy: str = Field(alias="policy")
    resource_arn: str = Field(alias="resourceArn")


class S3ReportExportConfigModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    bucket_owner: Optional[str] = Field(default=None, alias="bucketOwner")
    path: Optional[str] = Field(default=None, alias="path")
    packaging: Optional[Literal["NONE", "ZIP"]] = Field(default=None, alias="packaging")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="encryptionDisabled"
    )


class TestReportSummaryModel(BaseModel):
    total: int = Field(alias="total")
    status_counts: Dict[str, int] = Field(alias="statusCounts")
    duration_in_nano_seconds: int = Field(alias="durationInNanoSeconds")


class RetryBuildBatchInputRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    idempotency_token: Optional[str] = Field(default=None, alias="idempotencyToken")
    retry_type: Optional[Literal["RETRY_ALL_BUILDS", "RETRY_FAILED_BUILDS"]] = Field(
        default=None, alias="retryType"
    )


class RetryBuildInputRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    idempotency_token: Optional[str] = Field(default=None, alias="idempotencyToken")


class StopBuildBatchInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class StopBuildInputRequestModel(BaseModel):
    id: str = Field(alias="id")


class UpdateProjectVisibilityInputRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    project_visibility: Literal["PRIVATE", "PUBLIC_READ"] = Field(
        alias="projectVisibility"
    )
    resource_access_role: Optional[str] = Field(
        default=None, alias="resourceAccessRole"
    )


class BatchDeleteBuildsOutputModel(BaseModel):
    builds_deleted: List[str] = Field(alias="buildsDeleted")
    builds_not_deleted: List[BuildNotDeletedModel] = Field(alias="buildsNotDeleted")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBuildBatchOutputModel(BaseModel):
    status_code: str = Field(alias="statusCode")
    builds_deleted: List[str] = Field(alias="buildsDeleted")
    builds_not_deleted: List[BuildNotDeletedModel] = Field(alias="buildsNotDeleted")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSourceCredentialsOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyOutputModel(BaseModel):
    policy: str = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportSourceCredentialsOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuildBatchesForProjectOutputModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuildBatchesOutputModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuildsForProjectOutputModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuildsOutputModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    projects: List[str] = Field(alias="projects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportGroupsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    report_groups: List[str] = Field(alias="reportGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportsForReportGroupOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    reports: List[str] = Field(alias="reports")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    reports: List[str] = Field(alias="reports")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSharedProjectsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    projects: List[str] = Field(alias="projects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSharedReportGroupsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    report_groups: List[str] = Field(alias="reportGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyOutputModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectVisibilityOutputModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    public_project_alias: str = Field(alias="publicProjectAlias")
    project_visibility: Literal["PRIVATE", "PUBLIC_READ"] = Field(
        alias="projectVisibility"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProjectBuildBatchConfigModel(BaseModel):
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    combine_artifacts: Optional[bool] = Field(default=None, alias="combineArtifacts")
    restrictions: Optional[BatchRestrictionsModel] = Field(
        default=None, alias="restrictions"
    )
    timeout_in_mins: Optional[int] = Field(default=None, alias="timeoutInMins")
    batch_report_mode: Optional[
        Literal["REPORT_AGGREGATED_BATCH", "REPORT_INDIVIDUAL_BUILDS"]
    ] = Field(default=None, alias="batchReportMode")


class ListBuildBatchesForProjectInputRequestModel(BaseModel):
    project_name: Optional[str] = Field(default=None, alias="projectName")
    filter: Optional[BuildBatchFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBuildBatchesInputRequestModel(BaseModel):
    filter: Optional[BuildBatchFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class BuildBatchPhaseModel(BaseModel):
    phase_type: Optional[
        Literal[
            "COMBINE_ARTIFACTS",
            "DOWNLOAD_BATCHSPEC",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "SUBMITTED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="phaseType")
    phase_status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="phaseStatus")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    duration_in_seconds: Optional[int] = Field(default=None, alias="durationInSeconds")
    contexts: Optional[List[PhaseContextModel]] = Field(default=None, alias="contexts")


class BuildPhaseModel(BaseModel):
    phase_type: Optional[
        Literal[
            "BUILD",
            "COMPLETED",
            "DOWNLOAD_SOURCE",
            "FINALIZING",
            "INSTALL",
            "POST_BUILD",
            "PRE_BUILD",
            "PROVISIONING",
            "QUEUED",
            "SUBMITTED",
            "UPLOAD_ARTIFACTS",
        ]
    ] = Field(default=None, alias="phaseType")
    phase_status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="phaseStatus")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    duration_in_seconds: Optional[int] = Field(default=None, alias="durationInSeconds")
    contexts: Optional[List[PhaseContextModel]] = Field(default=None, alias="contexts")


class BuildSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    requested_on: Optional[datetime] = Field(default=None, alias="requestedOn")
    build_status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="buildStatus")
    primary_artifact: Optional[ResolvedArtifactModel] = Field(
        default=None, alias="primaryArtifact"
    )
    secondary_artifacts: Optional[List[ResolvedArtifactModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )


class DescribeCodeCoveragesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    code_coverages: List[CodeCoverageModel] = Field(alias="codeCoverages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWebhookInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    branch_filter: Optional[str] = Field(default=None, alias="branchFilter")
    filter_groups: Optional[Sequence[Sequence[WebhookFilterModel]]] = Field(
        default=None, alias="filterGroups"
    )
    build_type: Optional[Literal["BUILD", "BUILD_BATCH"]] = Field(
        default=None, alias="buildType"
    )


class UpdateWebhookInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    branch_filter: Optional[str] = Field(default=None, alias="branchFilter")
    rotate_secret: Optional[bool] = Field(default=None, alias="rotateSecret")
    filter_groups: Optional[Sequence[Sequence[WebhookFilterModel]]] = Field(
        default=None, alias="filterGroups"
    )
    build_type: Optional[Literal["BUILD", "BUILD_BATCH"]] = Field(
        default=None, alias="buildType"
    )


class WebhookModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="url")
    payload_url: Optional[str] = Field(default=None, alias="payloadUrl")
    secret: Optional[str] = Field(default=None, alias="secret")
    branch_filter: Optional[str] = Field(default=None, alias="branchFilter")
    filter_groups: Optional[List[List[WebhookFilterModel]]] = Field(
        default=None, alias="filterGroups"
    )
    build_type: Optional[Literal["BUILD", "BUILD_BATCH"]] = Field(
        default=None, alias="buildType"
    )
    last_modified_secret: Optional[datetime] = Field(
        default=None, alias="lastModifiedSecret"
    )


class DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateModel(BaseModel):
    report_arn: str = Field(alias="reportArn")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["FILE_PATH", "LINE_COVERAGE_PERCENTAGE"]] = Field(
        default=None, alias="sortBy"
    )
    min_line_coverage_percentage: Optional[float] = Field(
        default=None, alias="minLineCoveragePercentage"
    )
    max_line_coverage_percentage: Optional[float] = Field(
        default=None, alias="maxLineCoveragePercentage"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateModel(BaseModel):
    project_name: Optional[str] = Field(default=None, alias="projectName")
    filter: Optional[BuildBatchFilterModel] = Field(default=None, alias="filter")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBuildBatchesInputListBuildBatchesPaginateModel(BaseModel):
    filter: Optional[BuildBatchFilterModel] = Field(default=None, alias="filter")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBuildsForProjectInputListBuildsForProjectPaginateModel(BaseModel):
    project_name: str = Field(alias="projectName")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBuildsInputListBuildsPaginateModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsInputListProjectsPaginateModel(BaseModel):
    sort_by: Optional[Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReportGroupsInputListReportGroupsPaginateModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="sortBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSharedProjectsInputListSharedProjectsPaginateModel(BaseModel):
    sort_by: Optional[Literal["ARN", "MODIFIED_TIME"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSharedReportGroupsInputListSharedReportGroupsPaginateModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    sort_by: Optional[Literal["ARN", "MODIFIED_TIME"]] = Field(
        default=None, alias="sortBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTestCasesInputDescribeTestCasesPaginateModel(BaseModel):
    report_arn: str = Field(alias="reportArn")
    filter: Optional[TestCaseFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTestCasesInputRequestModel(BaseModel):
    report_arn: str = Field(alias="reportArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[TestCaseFilterModel] = Field(default=None, alias="filter")


class DescribeTestCasesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    test_cases: List[TestCaseModel] = Field(alias="testCases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentLanguageModel(BaseModel):
    language: Optional[
        Literal[
            "ANDROID",
            "BASE",
            "DOCKER",
            "DOTNET",
            "GOLANG",
            "JAVA",
            "NODE_JS",
            "PHP",
            "PYTHON",
            "RUBY",
        ]
    ] = Field(default=None, alias="language")
    images: Optional[List[EnvironmentImageModel]] = Field(default=None, alias="images")


class GetReportGroupTrendOutputModel(BaseModel):
    stats: ReportGroupTrendStatsModel = Field(alias="stats")
    raw_data: List[ReportWithRawDataModel] = Field(alias="rawData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReportsForReportGroupInputListReportsForReportGroupPaginateModel(BaseModel):
    report_group_arn: str = Field(alias="reportGroupArn")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    filter: Optional[ReportFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReportsForReportGroupInputRequestModel(BaseModel):
    report_group_arn: str = Field(alias="reportGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[ReportFilterModel] = Field(default=None, alias="filter")


class ListReportsInputListReportsPaginateModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    filter: Optional[ReportFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReportsInputRequestModel(BaseModel):
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[ReportFilterModel] = Field(default=None, alias="filter")


class ListSourceCredentialsOutputModel(BaseModel):
    source_credentials_infos: List[SourceCredentialsInfoModel] = Field(
        alias="sourceCredentialsInfos"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LogsConfigModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsConfigModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    s3_logs: Optional[S3LogsConfigModel] = Field(default=None, alias="s3Logs")


class LogsLocationModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="groupName")
    stream_name: Optional[str] = Field(default=None, alias="streamName")
    deep_link: Optional[str] = Field(default=None, alias="deepLink")
    s3_deep_link: Optional[str] = Field(default=None, alias="s3DeepLink")
    cloud_watch_logs_arn: Optional[str] = Field(default=None, alias="cloudWatchLogsArn")
    s3_logs_arn: Optional[str] = Field(default=None, alias="s3LogsArn")
    cloud_watch_logs: Optional[CloudWatchLogsConfigModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    s3_logs: Optional[S3LogsConfigModel] = Field(default=None, alias="s3Logs")


class ProjectEnvironmentModel(BaseModel):
    type: Literal[
        "ARM_CONTAINER",
        "LINUX_CONTAINER",
        "LINUX_GPU_CONTAINER",
        "WINDOWS_CONTAINER",
        "WINDOWS_SERVER_2019_CONTAINER",
    ] = Field(alias="type")
    image: str = Field(alias="image")
    compute_type: Literal[
        "BUILD_GENERAL1_2XLARGE",
        "BUILD_GENERAL1_LARGE",
        "BUILD_GENERAL1_MEDIUM",
        "BUILD_GENERAL1_SMALL",
    ] = Field(alias="computeType")
    environment_variables: Optional[List[EnvironmentVariableModel]] = Field(
        default=None, alias="environmentVariables"
    )
    privileged_mode: Optional[bool] = Field(default=None, alias="privilegedMode")
    certificate: Optional[str] = Field(default=None, alias="certificate")
    registry_credential: Optional[RegistryCredentialModel] = Field(
        default=None, alias="registryCredential"
    )
    image_pull_credentials_type: Optional[Literal["CODEBUILD", "SERVICE_ROLE"]] = Field(
        default=None, alias="imagePullCredentialsType"
    )


class ProjectSourceModel(BaseModel):
    type: Literal[
        "BITBUCKET",
        "CODECOMMIT",
        "CODEPIPELINE",
        "GITHUB",
        "GITHUB_ENTERPRISE",
        "NO_SOURCE",
        "S3",
    ] = Field(alias="type")
    location: Optional[str] = Field(default=None, alias="location")
    git_clone_depth: Optional[int] = Field(default=None, alias="gitCloneDepth")
    git_submodules_config: Optional[GitSubmodulesConfigModel] = Field(
        default=None, alias="gitSubmodulesConfig"
    )
    buildspec: Optional[str] = Field(default=None, alias="buildspec")
    auth: Optional[SourceAuthModel] = Field(default=None, alias="auth")
    report_build_status: Optional[bool] = Field(default=None, alias="reportBuildStatus")
    build_status_config: Optional[BuildStatusConfigModel] = Field(
        default=None, alias="buildStatusConfig"
    )
    insecure_ssl: Optional[bool] = Field(default=None, alias="insecureSsl")
    source_identifier: Optional[str] = Field(default=None, alias="sourceIdentifier")


class ReportExportConfigModel(BaseModel):
    export_config_type: Optional[Literal["NO_EXPORT", "S3"]] = Field(
        default=None, alias="exportConfigType"
    )
    s3_destination: Optional[S3ReportExportConfigModel] = Field(
        default=None, alias="s3Destination"
    )


class BuildGroupModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="identifier")
    depends_on: Optional[List[str]] = Field(default=None, alias="dependsOn")
    ignore_failure: Optional[bool] = Field(default=None, alias="ignoreFailure")
    current_build_summary: Optional[BuildSummaryModel] = Field(
        default=None, alias="currentBuildSummary"
    )
    prior_build_summary_list: Optional[List[BuildSummaryModel]] = Field(
        default=None, alias="priorBuildSummaryList"
    )


class CreateWebhookOutputModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWebhookOutputModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentPlatformModel(BaseModel):
    platform: Optional[
        Literal["AMAZON_LINUX", "DEBIAN", "UBUNTU", "WINDOWS_SERVER"]
    ] = Field(default=None, alias="platform")
    languages: Optional[List[EnvironmentLanguageModel]] = Field(
        default=None, alias="languages"
    )


class BuildModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    build_number: Optional[int] = Field(default=None, alias="buildNumber")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    current_phase: Optional[str] = Field(default=None, alias="currentPhase")
    build_status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="buildStatus")
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    resolved_source_version: Optional[str] = Field(
        default=None, alias="resolvedSourceVersion"
    )
    project_name: Optional[str] = Field(default=None, alias="projectName")
    phases: Optional[List[BuildPhaseModel]] = Field(default=None, alias="phases")
    source: Optional[ProjectSourceModel] = Field(default=None, alias="source")
    secondary_sources: Optional[List[ProjectSourceModel]] = Field(
        default=None, alias="secondarySources"
    )
    secondary_source_versions: Optional[List[ProjectSourceVersionModel]] = Field(
        default=None, alias="secondarySourceVersions"
    )
    artifacts: Optional[BuildArtifactsModel] = Field(default=None, alias="artifacts")
    secondary_artifacts: Optional[List[BuildArtifactsModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )
    cache: Optional[ProjectCacheModel] = Field(default=None, alias="cache")
    environment: Optional[ProjectEnvironmentModel] = Field(
        default=None, alias="environment"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    logs: Optional[LogsLocationModel] = Field(default=None, alias="logs")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="timeoutInMinutes")
    queued_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutes"
    )
    build_complete: Optional[bool] = Field(default=None, alias="buildComplete")
    initiator: Optional[str] = Field(default=None, alias="initiator")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")
    network_interface: Optional[NetworkInterfaceModel] = Field(
        default=None, alias="networkInterface"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    exported_environment_variables: Optional[
        List[ExportedEnvironmentVariableModel]
    ] = Field(default=None, alias="exportedEnvironmentVariables")
    report_arns: Optional[List[str]] = Field(default=None, alias="reportArns")
    file_system_locations: Optional[List[ProjectFileSystemLocationModel]] = Field(
        default=None, alias="fileSystemLocations"
    )
    debug_session: Optional[DebugSessionModel] = Field(
        default=None, alias="debugSession"
    )
    build_batch_arn: Optional[str] = Field(default=None, alias="buildBatchArn")


class CreateProjectInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    source: ProjectSourceModel = Field(alias="source")
    artifacts: ProjectArtifactsModel = Field(alias="artifacts")
    environment: ProjectEnvironmentModel = Field(alias="environment")
    service_role: str = Field(alias="serviceRole")
    description: Optional[str] = Field(default=None, alias="description")
    secondary_sources: Optional[Sequence[ProjectSourceModel]] = Field(
        default=None, alias="secondarySources"
    )
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    secondary_source_versions: Optional[Sequence[ProjectSourceVersionModel]] = Field(
        default=None, alias="secondarySourceVersions"
    )
    secondary_artifacts: Optional[Sequence[ProjectArtifactsModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )
    cache: Optional[ProjectCacheModel] = Field(default=None, alias="cache")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="timeoutInMinutes")
    queued_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutes"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")
    badge_enabled: Optional[bool] = Field(default=None, alias="badgeEnabled")
    logs_config: Optional[LogsConfigModel] = Field(default=None, alias="logsConfig")
    file_system_locations: Optional[Sequence[ProjectFileSystemLocationModel]] = Field(
        default=None, alias="fileSystemLocations"
    )
    build_batch_config: Optional[ProjectBuildBatchConfigModel] = Field(
        default=None, alias="buildBatchConfig"
    )
    concurrent_build_limit: Optional[int] = Field(
        default=None, alias="concurrentBuildLimit"
    )


class ProjectModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")
    source: Optional[ProjectSourceModel] = Field(default=None, alias="source")
    secondary_sources: Optional[List[ProjectSourceModel]] = Field(
        default=None, alias="secondarySources"
    )
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    secondary_source_versions: Optional[List[ProjectSourceVersionModel]] = Field(
        default=None, alias="secondarySourceVersions"
    )
    artifacts: Optional[ProjectArtifactsModel] = Field(default=None, alias="artifacts")
    secondary_artifacts: Optional[List[ProjectArtifactsModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )
    cache: Optional[ProjectCacheModel] = Field(default=None, alias="cache")
    environment: Optional[ProjectEnvironmentModel] = Field(
        default=None, alias="environment"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="timeoutInMinutes")
    queued_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutes"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    created: Optional[datetime] = Field(default=None, alias="created")
    last_modified: Optional[datetime] = Field(default=None, alias="lastModified")
    webhook: Optional[WebhookModel] = Field(default=None, alias="webhook")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")
    badge: Optional[ProjectBadgeModel] = Field(default=None, alias="badge")
    logs_config: Optional[LogsConfigModel] = Field(default=None, alias="logsConfig")
    file_system_locations: Optional[List[ProjectFileSystemLocationModel]] = Field(
        default=None, alias="fileSystemLocations"
    )
    build_batch_config: Optional[ProjectBuildBatchConfigModel] = Field(
        default=None, alias="buildBatchConfig"
    )
    concurrent_build_limit: Optional[int] = Field(
        default=None, alias="concurrentBuildLimit"
    )
    project_visibility: Optional[Literal["PRIVATE", "PUBLIC_READ"]] = Field(
        default=None, alias="projectVisibility"
    )
    public_project_alias: Optional[str] = Field(
        default=None, alias="publicProjectAlias"
    )
    resource_access_role: Optional[str] = Field(
        default=None, alias="resourceAccessRole"
    )


class StartBuildBatchInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    secondary_sources_override: Optional[Sequence[ProjectSourceModel]] = Field(
        default=None, alias="secondarySourcesOverride"
    )
    secondary_sources_version_override: Optional[
        Sequence[ProjectSourceVersionModel]
    ] = Field(default=None, alias="secondarySourcesVersionOverride")
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    artifacts_override: Optional[ProjectArtifactsModel] = Field(
        default=None, alias="artifactsOverride"
    )
    secondary_artifacts_override: Optional[Sequence[ProjectArtifactsModel]] = Field(
        default=None, alias="secondaryArtifactsOverride"
    )
    environment_variables_override: Optional[
        Sequence[EnvironmentVariableModel]
    ] = Field(default=None, alias="environmentVariablesOverride")
    source_type_override: Optional[
        Literal[
            "BITBUCKET",
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
            "S3",
        ]
    ] = Field(default=None, alias="sourceTypeOverride")
    source_location_override: Optional[str] = Field(
        default=None, alias="sourceLocationOverride"
    )
    source_auth_override: Optional[SourceAuthModel] = Field(
        default=None, alias="sourceAuthOverride"
    )
    git_clone_depth_override: Optional[int] = Field(
        default=None, alias="gitCloneDepthOverride"
    )
    git_submodules_config_override: Optional[GitSubmodulesConfigModel] = Field(
        default=None, alias="gitSubmodulesConfigOverride"
    )
    buildspec_override: Optional[str] = Field(default=None, alias="buildspecOverride")
    insecure_ssl_override: Optional[bool] = Field(
        default=None, alias="insecureSslOverride"
    )
    report_build_batch_status_override: Optional[bool] = Field(
        default=None, alias="reportBuildBatchStatusOverride"
    )
    environment_type_override: Optional[
        Literal[
            "ARM_CONTAINER",
            "LINUX_CONTAINER",
            "LINUX_GPU_CONTAINER",
            "WINDOWS_CONTAINER",
            "WINDOWS_SERVER_2019_CONTAINER",
        ]
    ] = Field(default=None, alias="environmentTypeOverride")
    image_override: Optional[str] = Field(default=None, alias="imageOverride")
    compute_type_override: Optional[
        Literal[
            "BUILD_GENERAL1_2XLARGE",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_SMALL",
        ]
    ] = Field(default=None, alias="computeTypeOverride")
    certificate_override: Optional[str] = Field(
        default=None, alias="certificateOverride"
    )
    cache_override: Optional[ProjectCacheModel] = Field(
        default=None, alias="cacheOverride"
    )
    service_role_override: Optional[str] = Field(
        default=None, alias="serviceRoleOverride"
    )
    privileged_mode_override: Optional[bool] = Field(
        default=None, alias="privilegedModeOverride"
    )
    build_timeout_in_minutes_override: Optional[int] = Field(
        default=None, alias="buildTimeoutInMinutesOverride"
    )
    queued_timeout_in_minutes_override: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutesOverride"
    )
    encryption_key_override: Optional[str] = Field(
        default=None, alias="encryptionKeyOverride"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="idempotencyToken")
    logs_config_override: Optional[LogsConfigModel] = Field(
        default=None, alias="logsConfigOverride"
    )
    registry_credential_override: Optional[RegistryCredentialModel] = Field(
        default=None, alias="registryCredentialOverride"
    )
    image_pull_credentials_type_override: Optional[
        Literal["CODEBUILD", "SERVICE_ROLE"]
    ] = Field(default=None, alias="imagePullCredentialsTypeOverride")
    build_batch_config_override: Optional[ProjectBuildBatchConfigModel] = Field(
        default=None, alias="buildBatchConfigOverride"
    )
    debug_session_enabled: Optional[bool] = Field(
        default=None, alias="debugSessionEnabled"
    )


class StartBuildInputRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    secondary_sources_override: Optional[Sequence[ProjectSourceModel]] = Field(
        default=None, alias="secondarySourcesOverride"
    )
    secondary_sources_version_override: Optional[
        Sequence[ProjectSourceVersionModel]
    ] = Field(default=None, alias="secondarySourcesVersionOverride")
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    artifacts_override: Optional[ProjectArtifactsModel] = Field(
        default=None, alias="artifactsOverride"
    )
    secondary_artifacts_override: Optional[Sequence[ProjectArtifactsModel]] = Field(
        default=None, alias="secondaryArtifactsOverride"
    )
    environment_variables_override: Optional[
        Sequence[EnvironmentVariableModel]
    ] = Field(default=None, alias="environmentVariablesOverride")
    source_type_override: Optional[
        Literal[
            "BITBUCKET",
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
            "S3",
        ]
    ] = Field(default=None, alias="sourceTypeOverride")
    source_location_override: Optional[str] = Field(
        default=None, alias="sourceLocationOverride"
    )
    source_auth_override: Optional[SourceAuthModel] = Field(
        default=None, alias="sourceAuthOverride"
    )
    git_clone_depth_override: Optional[int] = Field(
        default=None, alias="gitCloneDepthOverride"
    )
    git_submodules_config_override: Optional[GitSubmodulesConfigModel] = Field(
        default=None, alias="gitSubmodulesConfigOverride"
    )
    buildspec_override: Optional[str] = Field(default=None, alias="buildspecOverride")
    insecure_ssl_override: Optional[bool] = Field(
        default=None, alias="insecureSslOverride"
    )
    report_build_status_override: Optional[bool] = Field(
        default=None, alias="reportBuildStatusOverride"
    )
    build_status_config_override: Optional[BuildStatusConfigModel] = Field(
        default=None, alias="buildStatusConfigOverride"
    )
    environment_type_override: Optional[
        Literal[
            "ARM_CONTAINER",
            "LINUX_CONTAINER",
            "LINUX_GPU_CONTAINER",
            "WINDOWS_CONTAINER",
            "WINDOWS_SERVER_2019_CONTAINER",
        ]
    ] = Field(default=None, alias="environmentTypeOverride")
    image_override: Optional[str] = Field(default=None, alias="imageOverride")
    compute_type_override: Optional[
        Literal[
            "BUILD_GENERAL1_2XLARGE",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_SMALL",
        ]
    ] = Field(default=None, alias="computeTypeOverride")
    certificate_override: Optional[str] = Field(
        default=None, alias="certificateOverride"
    )
    cache_override: Optional[ProjectCacheModel] = Field(
        default=None, alias="cacheOverride"
    )
    service_role_override: Optional[str] = Field(
        default=None, alias="serviceRoleOverride"
    )
    privileged_mode_override: Optional[bool] = Field(
        default=None, alias="privilegedModeOverride"
    )
    timeout_in_minutes_override: Optional[int] = Field(
        default=None, alias="timeoutInMinutesOverride"
    )
    queued_timeout_in_minutes_override: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutesOverride"
    )
    encryption_key_override: Optional[str] = Field(
        default=None, alias="encryptionKeyOverride"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="idempotencyToken")
    logs_config_override: Optional[LogsConfigModel] = Field(
        default=None, alias="logsConfigOverride"
    )
    registry_credential_override: Optional[RegistryCredentialModel] = Field(
        default=None, alias="registryCredentialOverride"
    )
    image_pull_credentials_type_override: Optional[
        Literal["CODEBUILD", "SERVICE_ROLE"]
    ] = Field(default=None, alias="imagePullCredentialsTypeOverride")
    debug_session_enabled: Optional[bool] = Field(
        default=None, alias="debugSessionEnabled"
    )


class UpdateProjectInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    source: Optional[ProjectSourceModel] = Field(default=None, alias="source")
    secondary_sources: Optional[Sequence[ProjectSourceModel]] = Field(
        default=None, alias="secondarySources"
    )
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    secondary_source_versions: Optional[Sequence[ProjectSourceVersionModel]] = Field(
        default=None, alias="secondarySourceVersions"
    )
    artifacts: Optional[ProjectArtifactsModel] = Field(default=None, alias="artifacts")
    secondary_artifacts: Optional[Sequence[ProjectArtifactsModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )
    cache: Optional[ProjectCacheModel] = Field(default=None, alias="cache")
    environment: Optional[ProjectEnvironmentModel] = Field(
        default=None, alias="environment"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="timeoutInMinutes")
    queued_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutes"
    )
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")
    badge_enabled: Optional[bool] = Field(default=None, alias="badgeEnabled")
    logs_config: Optional[LogsConfigModel] = Field(default=None, alias="logsConfig")
    file_system_locations: Optional[Sequence[ProjectFileSystemLocationModel]] = Field(
        default=None, alias="fileSystemLocations"
    )
    build_batch_config: Optional[ProjectBuildBatchConfigModel] = Field(
        default=None, alias="buildBatchConfig"
    )
    concurrent_build_limit: Optional[int] = Field(
        default=None, alias="concurrentBuildLimit"
    )


class CreateReportGroupInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["CODE_COVERAGE", "TEST"] = Field(alias="type")
    export_config: ReportExportConfigModel = Field(alias="exportConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ReportGroupModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["CODE_COVERAGE", "TEST"]] = Field(default=None, alias="type")
    export_config: Optional[ReportExportConfigModel] = Field(
        default=None, alias="exportConfig"
    )
    created: Optional[datetime] = Field(default=None, alias="created")
    last_modified: Optional[datetime] = Field(default=None, alias="lastModified")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    status: Optional[Literal["ACTIVE", "DELETING"]] = Field(
        default=None, alias="status"
    )


class ReportModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[Literal["CODE_COVERAGE", "TEST"]] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    report_group_arn: Optional[str] = Field(default=None, alias="reportGroupArn")
    execution_id: Optional[str] = Field(default=None, alias="executionId")
    status: Optional[
        Literal["DELETING", "FAILED", "GENERATING", "INCOMPLETE", "SUCCEEDED"]
    ] = Field(default=None, alias="status")
    created: Optional[datetime] = Field(default=None, alias="created")
    expired: Optional[datetime] = Field(default=None, alias="expired")
    export_config: Optional[ReportExportConfigModel] = Field(
        default=None, alias="exportConfig"
    )
    truncated: Optional[bool] = Field(default=None, alias="truncated")
    test_summary: Optional[TestReportSummaryModel] = Field(
        default=None, alias="testSummary"
    )
    code_coverage_summary: Optional[CodeCoverageReportSummaryModel] = Field(
        default=None, alias="codeCoverageSummary"
    )


class UpdateReportGroupInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    export_config: Optional[ReportExportConfigModel] = Field(
        default=None, alias="exportConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class BuildBatchModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    current_phase: Optional[str] = Field(default=None, alias="currentPhase")
    build_batch_status: Optional[
        Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="buildBatchStatus")
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    resolved_source_version: Optional[str] = Field(
        default=None, alias="resolvedSourceVersion"
    )
    project_name: Optional[str] = Field(default=None, alias="projectName")
    phases: Optional[List[BuildBatchPhaseModel]] = Field(default=None, alias="phases")
    source: Optional[ProjectSourceModel] = Field(default=None, alias="source")
    secondary_sources: Optional[List[ProjectSourceModel]] = Field(
        default=None, alias="secondarySources"
    )
    secondary_source_versions: Optional[List[ProjectSourceVersionModel]] = Field(
        default=None, alias="secondarySourceVersions"
    )
    artifacts: Optional[BuildArtifactsModel] = Field(default=None, alias="artifacts")
    secondary_artifacts: Optional[List[BuildArtifactsModel]] = Field(
        default=None, alias="secondaryArtifacts"
    )
    cache: Optional[ProjectCacheModel] = Field(default=None, alias="cache")
    environment: Optional[ProjectEnvironmentModel] = Field(
        default=None, alias="environment"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    log_config: Optional[LogsConfigModel] = Field(default=None, alias="logConfig")
    build_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="buildTimeoutInMinutes"
    )
    queued_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="queuedTimeoutInMinutes"
    )
    complete: Optional[bool] = Field(default=None, alias="complete")
    initiator: Optional[str] = Field(default=None, alias="initiator")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    build_batch_number: Optional[int] = Field(default=None, alias="buildBatchNumber")
    file_system_locations: Optional[List[ProjectFileSystemLocationModel]] = Field(
        default=None, alias="fileSystemLocations"
    )
    build_batch_config: Optional[ProjectBuildBatchConfigModel] = Field(
        default=None, alias="buildBatchConfig"
    )
    build_groups: Optional[List[BuildGroupModel]] = Field(
        default=None, alias="buildGroups"
    )
    debug_session_enabled: Optional[bool] = Field(
        default=None, alias="debugSessionEnabled"
    )


class ListCuratedEnvironmentImagesOutputModel(BaseModel):
    platforms: List[EnvironmentPlatformModel] = Field(alias="platforms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetBuildsOutputModel(BaseModel):
    builds: List[BuildModel] = Field(alias="builds")
    builds_not_found: List[str] = Field(alias="buildsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetryBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="build")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="build")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="build")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetProjectsOutputModel(BaseModel):
    projects: List[ProjectModel] = Field(alias="projects")
    projects_not_found: List[str] = Field(alias="projectsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectOutputModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectOutputModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetReportGroupsOutputModel(BaseModel):
    report_groups: List[ReportGroupModel] = Field(alias="reportGroups")
    report_groups_not_found: List[str] = Field(alias="reportGroupsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReportGroupOutputModel(BaseModel):
    report_group: ReportGroupModel = Field(alias="reportGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReportGroupOutputModel(BaseModel):
    report_group: ReportGroupModel = Field(alias="reportGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetReportsOutputModel(BaseModel):
    reports: List[ReportModel] = Field(alias="reports")
    reports_not_found: List[str] = Field(alias="reportsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetBuildBatchesOutputModel(BaseModel):
    build_batches: List[BuildBatchModel] = Field(alias="buildBatches")
    build_batches_not_found: List[str] = Field(alias="buildBatchesNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetryBuildBatchOutputModel(BaseModel):
    build_batch: BuildBatchModel = Field(alias="buildBatch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBuildBatchOutputModel(BaseModel):
    build_batch: BuildBatchModel = Field(alias="buildBatch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopBuildBatchOutputModel(BaseModel):
    build_batch: BuildBatchModel = Field(alias="buildBatch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
