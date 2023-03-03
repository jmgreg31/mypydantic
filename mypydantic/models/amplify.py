# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AutoBranchCreationConfigModel(BaseModel):
    stage: Optional[
        Literal["BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"]
    ] = Field(default=None, alias="stage")
    framework: Optional[str] = Field(default=None, alias="framework")
    enable_auto_build: Optional[bool] = Field(default=None, alias="enableAutoBuild")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    enable_basic_auth: Optional[bool] = Field(default=None, alias="enableBasicAuth")
    enable_performance_mode: Optional[bool] = Field(
        default=None, alias="enablePerformanceMode"
    )
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    enable_pull_request_preview: Optional[bool] = Field(
        default=None, alias="enablePullRequestPreview"
    )
    pull_request_environment_name: Optional[str] = Field(
        default=None, alias="pullRequestEnvironmentName"
    )


class CustomRuleModel(BaseModel):
    source: str = Field(alias="source")
    target: str = Field(alias="target")
    status: Optional[str] = Field(default=None, alias="status")
    condition: Optional[str] = Field(default=None, alias="condition")


class ProductionBranchModel(BaseModel):
    last_deploy_time: Optional[datetime] = Field(default=None, alias="lastDeployTime")
    status: Optional[str] = Field(default=None, alias="status")
    thumbnail_url: Optional[str] = Field(default=None, alias="thumbnailUrl")
    branch_name: Optional[str] = Field(default=None, alias="branchName")


class ArtifactModel(BaseModel):
    artifact_file_name: str = Field(alias="artifactFileName")
    artifact_id: str = Field(alias="artifactId")


class BackendEnvironmentModel(BaseModel):
    backend_environment_arn: str = Field(alias="backendEnvironmentArn")
    environment_name: str = Field(alias="environmentName")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    stack_name: Optional[str] = Field(default=None, alias="stackName")
    deployment_artifacts: Optional[str] = Field(
        default=None, alias="deploymentArtifacts"
    )


class BranchModel(BaseModel):
    branch_arn: str = Field(alias="branchArn")
    branch_name: str = Field(alias="branchName")
    description: str = Field(alias="description")
    stage: Literal[
        "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"
    ] = Field(alias="stage")
    display_name: str = Field(alias="displayName")
    enable_notification: bool = Field(alias="enableNotification")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    environment_variables: Dict[str, str] = Field(alias="environmentVariables")
    enable_auto_build: bool = Field(alias="enableAutoBuild")
    custom_domains: List[str] = Field(alias="customDomains")
    framework: str = Field(alias="framework")
    active_job_id: str = Field(alias="activeJobId")
    total_number_of_jobs: str = Field(alias="totalNumberOfJobs")
    enable_basic_auth: bool = Field(alias="enableBasicAuth")
    ttl: str = Field(alias="ttl")
    enable_pull_request_preview: bool = Field(alias="enablePullRequestPreview")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    enable_performance_mode: Optional[bool] = Field(
        default=None, alias="enablePerformanceMode"
    )
    thumbnail_url: Optional[str] = Field(default=None, alias="thumbnailUrl")
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    associated_resources: Optional[List[str]] = Field(
        default=None, alias="associatedResources"
    )
    pull_request_environment_name: Optional[str] = Field(
        default=None, alias="pullRequestEnvironmentName"
    )
    destination_branch: Optional[str] = Field(default=None, alias="destinationBranch")
    source_branch: Optional[str] = Field(default=None, alias="sourceBranch")
    backend_environment_arn: Optional[str] = Field(
        default=None, alias="backendEnvironmentArn"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateBackendEnvironmentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    stack_name: Optional[str] = Field(default=None, alias="stackName")
    deployment_artifacts: Optional[str] = Field(
        default=None, alias="deploymentArtifacts"
    )


class CreateBranchRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")
    stage: Optional[
        Literal["BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"]
    ] = Field(default=None, alias="stage")
    framework: Optional[str] = Field(default=None, alias="framework")
    enable_notification: Optional[bool] = Field(
        default=None, alias="enableNotification"
    )
    enable_auto_build: Optional[bool] = Field(default=None, alias="enableAutoBuild")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    enable_basic_auth: Optional[bool] = Field(default=None, alias="enableBasicAuth")
    enable_performance_mode: Optional[bool] = Field(
        default=None, alias="enablePerformanceMode"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    ttl: Optional[str] = Field(default=None, alias="ttl")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    enable_pull_request_preview: Optional[bool] = Field(
        default=None, alias="enablePullRequestPreview"
    )
    pull_request_environment_name: Optional[str] = Field(
        default=None, alias="pullRequestEnvironmentName"
    )
    backend_environment_arn: Optional[str] = Field(
        default=None, alias="backendEnvironmentArn"
    )


class CreateDeploymentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    file_map: Optional[Mapping[str, str]] = Field(default=None, alias="fileMap")


class SubDomainSettingModel(BaseModel):
    prefix: str = Field(alias="prefix")
    branch_name: str = Field(alias="branchName")


class CreateWebhookRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")


class WebhookModel(BaseModel):
    webhook_arn: str = Field(alias="webhookArn")
    webhook_id: str = Field(alias="webhookId")
    webhook_url: str = Field(alias="webhookUrl")
    branch_name: str = Field(alias="branchName")
    description: str = Field(alias="description")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")


class DeleteAppRequestModel(BaseModel):
    app_id: str = Field(alias="appId")


class DeleteBackendEnvironmentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")


class DeleteBranchRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")


class DeleteDomainAssociationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    domain_name: str = Field(alias="domainName")


class DeleteJobRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_id: str = Field(alias="jobId")


class JobSummaryModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    commit_id: str = Field(alias="commitId")
    commit_message: str = Field(alias="commitMessage")
    commit_time: datetime = Field(alias="commitTime")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "PENDING",
        "PROVISIONING",
        "RUNNING",
        "SUCCEED",
    ] = Field(alias="status")
    job_type: Literal["MANUAL", "RELEASE", "RETRY", "WEB_HOOK"] = Field(alias="jobType")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")


class DeleteWebhookRequestModel(BaseModel):
    webhook_id: str = Field(alias="webhookId")


class GenerateAccessLogsRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    app_id: str = Field(alias="appId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")


class GetAppRequestModel(BaseModel):
    app_id: str = Field(alias="appId")


class GetArtifactUrlRequestModel(BaseModel):
    artifact_id: str = Field(alias="artifactId")


class GetBackendEnvironmentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")


class GetBranchRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")


class GetDomainAssociationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    domain_name: str = Field(alias="domainName")


class GetJobRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_id: str = Field(alias="jobId")


class GetWebhookRequestModel(BaseModel):
    webhook_id: str = Field(alias="webhookId")


class StepModel(BaseModel):
    step_name: str = Field(alias="stepName")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "PENDING",
        "PROVISIONING",
        "RUNNING",
        "SUCCEED",
    ] = Field(alias="status")
    end_time: datetime = Field(alias="endTime")
    log_url: Optional[str] = Field(default=None, alias="logUrl")
    artifacts_url: Optional[str] = Field(default=None, alias="artifactsUrl")
    test_artifacts_url: Optional[str] = Field(default=None, alias="testArtifactsUrl")
    test_config_url: Optional[str] = Field(default=None, alias="testConfigUrl")
    screenshots: Optional[Dict[str, str]] = Field(default=None, alias="screenshots")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    context: Optional[str] = Field(default=None, alias="context")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAppsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListArtifactsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_id: str = Field(alias="jobId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListBackendEnvironmentsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: Optional[str] = Field(default=None, alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListBranchesRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDomainAssociationsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListJobsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListWebhooksRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class StartDeploymentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    source_url: Optional[str] = Field(default=None, alias="sourceUrl")


class StartJobRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_type: Literal["MANUAL", "RELEASE", "RETRY", "WEB_HOOK"] = Field(alias="jobType")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    job_reason: Optional[str] = Field(default=None, alias="jobReason")
    commit_id: Optional[str] = Field(default=None, alias="commitId")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    commit_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="commitTime"
    )


class StopJobRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    job_id: str = Field(alias="jobId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateBranchRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")
    framework: Optional[str] = Field(default=None, alias="framework")
    stage: Optional[
        Literal["BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"]
    ] = Field(default=None, alias="stage")
    enable_notification: Optional[bool] = Field(
        default=None, alias="enableNotification"
    )
    enable_auto_build: Optional[bool] = Field(default=None, alias="enableAutoBuild")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    enable_basic_auth: Optional[bool] = Field(default=None, alias="enableBasicAuth")
    enable_performance_mode: Optional[bool] = Field(
        default=None, alias="enablePerformanceMode"
    )
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    ttl: Optional[str] = Field(default=None, alias="ttl")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    enable_pull_request_preview: Optional[bool] = Field(
        default=None, alias="enablePullRequestPreview"
    )
    pull_request_environment_name: Optional[str] = Field(
        default=None, alias="pullRequestEnvironmentName"
    )
    backend_environment_arn: Optional[str] = Field(
        default=None, alias="backendEnvironmentArn"
    )


class UpdateWebhookRequestModel(BaseModel):
    webhook_id: str = Field(alias="webhookId")
    branch_name: Optional[str] = Field(default=None, alias="branchName")
    description: Optional[str] = Field(default=None, alias="description")


class CreateAppRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    repository: Optional[str] = Field(default=None, alias="repository")
    platform: Optional[Literal["WEB", "WEB_COMPUTE", "WEB_DYNAMIC"]] = Field(
        default=None, alias="platform"
    )
    iam_service_role_arn: Optional[str] = Field(default=None, alias="iamServiceRoleArn")
    oauth_token: Optional[str] = Field(default=None, alias="oauthToken")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    enable_branch_auto_build: Optional[bool] = Field(
        default=None, alias="enableBranchAutoBuild"
    )
    enable_branch_auto_deletion: Optional[bool] = Field(
        default=None, alias="enableBranchAutoDeletion"
    )
    enable_basic_auth: Optional[bool] = Field(default=None, alias="enableBasicAuth")
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    custom_rules: Optional[Sequence[CustomRuleModel]] = Field(
        default=None, alias="customRules"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    custom_headers: Optional[str] = Field(default=None, alias="customHeaders")
    enable_auto_branch_creation: Optional[bool] = Field(
        default=None, alias="enableAutoBranchCreation"
    )
    auto_branch_creation_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="autoBranchCreationPatterns"
    )
    auto_branch_creation_config: Optional[AutoBranchCreationConfigModel] = Field(
        default=None, alias="autoBranchCreationConfig"
    )


class UpdateAppRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    platform: Optional[Literal["WEB", "WEB_COMPUTE", "WEB_DYNAMIC"]] = Field(
        default=None, alias="platform"
    )
    iam_service_role_arn: Optional[str] = Field(default=None, alias="iamServiceRoleArn")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    enable_branch_auto_build: Optional[bool] = Field(
        default=None, alias="enableBranchAutoBuild"
    )
    enable_branch_auto_deletion: Optional[bool] = Field(
        default=None, alias="enableBranchAutoDeletion"
    )
    enable_basic_auth: Optional[bool] = Field(default=None, alias="enableBasicAuth")
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    custom_rules: Optional[Sequence[CustomRuleModel]] = Field(
        default=None, alias="customRules"
    )
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    custom_headers: Optional[str] = Field(default=None, alias="customHeaders")
    enable_auto_branch_creation: Optional[bool] = Field(
        default=None, alias="enableAutoBranchCreation"
    )
    auto_branch_creation_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="autoBranchCreationPatterns"
    )
    auto_branch_creation_config: Optional[AutoBranchCreationConfigModel] = Field(
        default=None, alias="autoBranchCreationConfig"
    )
    repository: Optional[str] = Field(default=None, alias="repository")
    oauth_token: Optional[str] = Field(default=None, alias="oauthToken")
    access_token: Optional[str] = Field(default=None, alias="accessToken")


class AppModel(BaseModel):
    app_id: str = Field(alias="appId")
    app_arn: str = Field(alias="appArn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    repository: str = Field(alias="repository")
    platform: Literal["WEB", "WEB_COMPUTE", "WEB_DYNAMIC"] = Field(alias="platform")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    environment_variables: Dict[str, str] = Field(alias="environmentVariables")
    default_domain: str = Field(alias="defaultDomain")
    enable_branch_auto_build: bool = Field(alias="enableBranchAutoBuild")
    enable_basic_auth: bool = Field(alias="enableBasicAuth")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    iam_service_role_arn: Optional[str] = Field(default=None, alias="iamServiceRoleArn")
    enable_branch_auto_deletion: Optional[bool] = Field(
        default=None, alias="enableBranchAutoDeletion"
    )
    basic_auth_credentials: Optional[str] = Field(
        default=None, alias="basicAuthCredentials"
    )
    custom_rules: Optional[List[CustomRuleModel]] = Field(
        default=None, alias="customRules"
    )
    production_branch: Optional[ProductionBranchModel] = Field(
        default=None, alias="productionBranch"
    )
    build_spec: Optional[str] = Field(default=None, alias="buildSpec")
    custom_headers: Optional[str] = Field(default=None, alias="customHeaders")
    enable_auto_branch_creation: Optional[bool] = Field(
        default=None, alias="enableAutoBranchCreation"
    )
    auto_branch_creation_patterns: Optional[List[str]] = Field(
        default=None, alias="autoBranchCreationPatterns"
    )
    auto_branch_creation_config: Optional[AutoBranchCreationConfigModel] = Field(
        default=None, alias="autoBranchCreationConfig"
    )
    repository_clone_method: Optional[Literal["SIGV4", "SSH", "TOKEN"]] = Field(
        default=None, alias="repositoryCloneMethod"
    )


class CreateBackendEnvironmentResultModel(BaseModel):
    backend_environment: BackendEnvironmentModel = Field(alias="backendEnvironment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBranchResultModel(BaseModel):
    branch: BranchModel = Field(alias="branch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResultModel(BaseModel):
    job_id: str = Field(alias="jobId")
    file_upload_urls: Dict[str, str] = Field(alias="fileUploadUrls")
    zip_upload_url: str = Field(alias="zipUploadUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackendEnvironmentResultModel(BaseModel):
    backend_environment: BackendEnvironmentModel = Field(alias="backendEnvironment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBranchResultModel(BaseModel):
    branch: BranchModel = Field(alias="branch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateAccessLogsResultModel(BaseModel):
    log_url: str = Field(alias="logUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetArtifactUrlResultModel(BaseModel):
    artifact_id: str = Field(alias="artifactId")
    artifact_url: str = Field(alias="artifactUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackendEnvironmentResultModel(BaseModel):
    backend_environment: BackendEnvironmentModel = Field(alias="backendEnvironment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBranchResultModel(BaseModel):
    branch: BranchModel = Field(alias="branch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListArtifactsResultModel(BaseModel):
    artifacts: List[ArtifactModel] = Field(alias="artifacts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackendEnvironmentsResultModel(BaseModel):
    backend_environments: List[BackendEnvironmentModel] = Field(
        alias="backendEnvironments"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBranchesResultModel(BaseModel):
    branches: List[BranchModel] = Field(alias="branches")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBranchResultModel(BaseModel):
    branch: BranchModel = Field(alias="branch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainAssociationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    domain_name: str = Field(alias="domainName")
    sub_domain_settings: Sequence[SubDomainSettingModel] = Field(
        alias="subDomainSettings"
    )
    enable_auto_sub_domain: Optional[bool] = Field(
        default=None, alias="enableAutoSubDomain"
    )
    auto_sub_domain_creation_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="autoSubDomainCreationPatterns"
    )
    auto_sub_domain_iamrole: Optional[str] = Field(
        default=None, alias="autoSubDomainIAMRole"
    )


class SubDomainModel(BaseModel):
    sub_domain_setting: SubDomainSettingModel = Field(alias="subDomainSetting")
    verified: bool = Field(alias="verified")
    dns_record: str = Field(alias="dnsRecord")


class UpdateDomainAssociationRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    domain_name: str = Field(alias="domainName")
    enable_auto_sub_domain: Optional[bool] = Field(
        default=None, alias="enableAutoSubDomain"
    )
    sub_domain_settings: Optional[Sequence[SubDomainSettingModel]] = Field(
        default=None, alias="subDomainSettings"
    )
    auto_sub_domain_creation_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="autoSubDomainCreationPatterns"
    )
    auto_sub_domain_iamrole: Optional[str] = Field(
        default=None, alias="autoSubDomainIAMRole"
    )


class CreateWebhookResultModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWebhookResultModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWebhookResultModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebhooksResultModel(BaseModel):
    webhooks: List[WebhookModel] = Field(alias="webhooks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWebhookResultModel(BaseModel):
    webhook: WebhookModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteJobResultModel(BaseModel):
    job_summary: JobSummaryModel = Field(alias="jobSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResultModel(BaseModel):
    job_summaries: List[JobSummaryModel] = Field(alias="jobSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDeploymentResultModel(BaseModel):
    job_summary: JobSummaryModel = Field(alias="jobSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartJobResultModel(BaseModel):
    job_summary: JobSummaryModel = Field(alias="jobSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopJobResultModel(BaseModel):
    job_summary: JobSummaryModel = Field(alias="jobSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobModel(BaseModel):
    summary: JobSummaryModel = Field(alias="summary")
    steps: List[StepModel] = Field(alias="steps")


class ListAppsRequestListAppsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBranchesRequestListBranchesPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainAssociationsRequestListDomainAssociationsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    branch_name: str = Field(alias="branchName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class CreateAppResultModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppResultModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppResultModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppsResultModel(BaseModel):
    apps: List[AppModel] = Field(alias="apps")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppResultModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainAssociationModel(BaseModel):
    domain_association_arn: str = Field(alias="domainAssociationArn")
    domain_name: str = Field(alias="domainName")
    enable_auto_sub_domain: bool = Field(alias="enableAutoSubDomain")
    domain_status: Literal[
        "AVAILABLE",
        "CREATING",
        "FAILED",
        "IN_PROGRESS",
        "PENDING_DEPLOYMENT",
        "PENDING_VERIFICATION",
        "REQUESTING_CERTIFICATE",
        "UPDATING",
    ] = Field(alias="domainStatus")
    status_reason: str = Field(alias="statusReason")
    sub_domains: List[SubDomainModel] = Field(alias="subDomains")
    auto_sub_domain_creation_patterns: Optional[List[str]] = Field(
        default=None, alias="autoSubDomainCreationPatterns"
    )
    auto_sub_domain_iamrole: Optional[str] = Field(
        default=None, alias="autoSubDomainIAMRole"
    )
    certificate_verification_dns_record: Optional[str] = Field(
        default=None, alias="certificateVerificationDNSRecord"
    )


class GetJobResultModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainAssociationResultModel(BaseModel):
    domain_association: DomainAssociationModel = Field(alias="domainAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainAssociationResultModel(BaseModel):
    domain_association: DomainAssociationModel = Field(alias="domainAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainAssociationResultModel(BaseModel):
    domain_association: DomainAssociationModel = Field(alias="domainAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainAssociationsResultModel(BaseModel):
    domain_associations: List[DomainAssociationModel] = Field(
        alias="domainAssociations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainAssociationResultModel(BaseModel):
    domain_association: DomainAssociationModel = Field(alias="domainAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
