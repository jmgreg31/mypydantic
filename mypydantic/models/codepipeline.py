# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AWSSessionCredentialsModel(BaseModel):
    access_key_id: str = Field(alias="accessKeyId")
    secret_access_key: str = Field(alias="secretAccessKey")
    session_token: str = Field(alias="sessionToken")


class AcknowledgeJobInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    nonce: str = Field(alias="nonce")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AcknowledgeThirdPartyJobInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    nonce: str = Field(alias="nonce")
    client_token: str = Field(alias="clientToken")


class ActionConfigurationPropertyModel(BaseModel):
    name: str = Field(alias="name")
    required: bool = Field(alias="required")
    key: bool = Field(alias="key")
    secret: bool = Field(alias="secret")
    queryable: Optional[bool] = Field(default=None, alias="queryable")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["Boolean", "Number", "String"]] = Field(
        default=None, alias="type"
    )


class ActionConfigurationModel(BaseModel):
    configuration: Optional[Dict[str, str]] = Field(default=None, alias="configuration")


class ActionContextModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    action_execution_id: Optional[str] = Field(default=None, alias="actionExecutionId")


class ActionTypeIdModel(BaseModel):
    category: Literal[
        "Approval", "Build", "Deploy", "Invoke", "Source", "Test"
    ] = Field(alias="category")
    owner: Literal["AWS", "Custom", "ThirdParty"] = Field(alias="owner")
    provider: str = Field(alias="provider")
    version: str = Field(alias="version")


class InputArtifactModel(BaseModel):
    name: str = Field(alias="name")


class OutputArtifactModel(BaseModel):
    name: str = Field(alias="name")


class ActionExecutionFilterModel(BaseModel):
    pipeline_execution_id: Optional[str] = Field(
        default=None, alias="pipelineExecutionId"
    )


class ActionExecutionResultModel(BaseModel):
    external_execution_id: Optional[str] = Field(
        default=None, alias="externalExecutionId"
    )
    external_execution_summary: Optional[str] = Field(
        default=None, alias="externalExecutionSummary"
    )
    external_execution_url: Optional[str] = Field(
        default=None, alias="externalExecutionUrl"
    )


class ErrorDetailsModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class ActionRevisionModel(BaseModel):
    revision_id: str = Field(alias="revisionId")
    revision_change_id: str = Field(alias="revisionChangeId")
    created: datetime = Field(alias="created")


class ActionTypeArtifactDetailsModel(BaseModel):
    minimum_count: int = Field(alias="minimumCount")
    maximum_count: int = Field(alias="maximumCount")


class ActionTypeIdentifierModel(BaseModel):
    category: Literal[
        "Approval", "Build", "Deploy", "Invoke", "Source", "Test"
    ] = Field(alias="category")
    owner: str = Field(alias="owner")
    provider: str = Field(alias="provider")
    version: str = Field(alias="version")


class ActionTypePermissionsModel(BaseModel):
    allowed_accounts: List[str] = Field(alias="allowedAccounts")


class ActionTypePropertyModel(BaseModel):
    name: str = Field(alias="name")
    optional: bool = Field(alias="optional")
    key: bool = Field(alias="key")
    no_echo: bool = Field(alias="noEcho")
    queryable: Optional[bool] = Field(default=None, alias="queryable")
    description: Optional[str] = Field(default=None, alias="description")


class ActionTypeUrlsModel(BaseModel):
    configuration_url: Optional[str] = Field(default=None, alias="configurationUrl")
    entity_url_template: Optional[str] = Field(default=None, alias="entityUrlTemplate")
    execution_url_template: Optional[str] = Field(
        default=None, alias="executionUrlTemplate"
    )
    revision_url_template: Optional[str] = Field(
        default=None, alias="revisionUrlTemplate"
    )


class ActionTypeSettingsModel(BaseModel):
    third_party_configuration_url: Optional[str] = Field(
        default=None, alias="thirdPartyConfigurationUrl"
    )
    entity_url_template: Optional[str] = Field(default=None, alias="entityUrlTemplate")
    execution_url_template: Optional[str] = Field(
        default=None, alias="executionUrlTemplate"
    )
    revision_url_template: Optional[str] = Field(
        default=None, alias="revisionUrlTemplate"
    )


class ArtifactDetailsModel(BaseModel):
    minimum_count: int = Field(alias="minimumCount")
    maximum_count: int = Field(alias="maximumCount")


class ApprovalResultModel(BaseModel):
    summary: str = Field(alias="summary")
    status: Literal["Approved", "Rejected"] = Field(alias="status")


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")


class S3ArtifactLocationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    object_key: str = Field(alias="objectKey")


class ArtifactRevisionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    revision_change_identifier: Optional[str] = Field(
        default=None, alias="revisionChangeIdentifier"
    )
    revision_summary: Optional[str] = Field(default=None, alias="revisionSummary")
    created: Optional[datetime] = Field(default=None, alias="created")
    revision_url: Optional[str] = Field(default=None, alias="revisionUrl")


class EncryptionKeyModel(BaseModel):
    id: str = Field(alias="id")
    type: Literal["KMS"] = Field(alias="type")


class BlockerDeclarationModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["Schedule"] = Field(alias="type")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class CurrentRevisionModel(BaseModel):
    revision: str = Field(alias="revision")
    change_identifier: str = Field(alias="changeIdentifier")
    created: Optional[Union[datetime, str]] = Field(default=None, alias="created")
    revision_summary: Optional[str] = Field(default=None, alias="revisionSummary")


class DeleteCustomActionTypeInputRequestModel(BaseModel):
    category: Literal[
        "Approval", "Build", "Deploy", "Invoke", "Source", "Test"
    ] = Field(alias="category")
    provider: str = Field(alias="provider")
    version: str = Field(alias="version")


class DeletePipelineInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteWebhookInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeregisterWebhookWithThirdPartyInputRequestModel(BaseModel):
    webhook_name: Optional[str] = Field(default=None, alias="webhookName")


class DisableStageTransitionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    stage_name: str = Field(alias="stageName")
    transition_type: Literal["Inbound", "Outbound"] = Field(alias="transitionType")
    reason: str = Field(alias="reason")


class EnableStageTransitionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    stage_name: str = Field(alias="stageName")
    transition_type: Literal["Inbound", "Outbound"] = Field(alias="transitionType")


class ExecutionDetailsModel(BaseModel):
    summary: Optional[str] = Field(default=None, alias="summary")
    external_execution_id: Optional[str] = Field(
        default=None, alias="externalExecutionId"
    )
    percent_complete: Optional[int] = Field(default=None, alias="percentComplete")


class ExecutionTriggerModel(BaseModel):
    trigger_type: Optional[
        Literal[
            "CloudWatchEvent",
            "CreatePipeline",
            "PollForSourceChanges",
            "PutActionRevision",
            "StartPipelineExecution",
            "Webhook",
        ]
    ] = Field(default=None, alias="triggerType")
    trigger_detail: Optional[str] = Field(default=None, alias="triggerDetail")


class JobWorkerExecutorConfigurationModel(BaseModel):
    polling_accounts: Optional[List[str]] = Field(default=None, alias="pollingAccounts")
    polling_service_principals: Optional[List[str]] = Field(
        default=None, alias="pollingServicePrincipals"
    )


class LambdaExecutorConfigurationModel(BaseModel):
    lambda_function_arn: str = Field(alias="lambdaFunctionArn")


class FailureDetailsModel(BaseModel):
    type: Literal[
        "ConfigurationError",
        "JobFailed",
        "PermissionError",
        "RevisionOutOfSync",
        "RevisionUnavailable",
        "SystemUnavailable",
    ] = Field(alias="type")
    message: str = Field(alias="message")
    external_execution_id: Optional[str] = Field(
        default=None, alias="externalExecutionId"
    )


class GetActionTypeInputRequestModel(BaseModel):
    category: Literal[
        "Approval", "Build", "Deploy", "Invoke", "Source", "Test"
    ] = Field(alias="category")
    owner: str = Field(alias="owner")
    provider: str = Field(alias="provider")
    version: str = Field(alias="version")


class GetJobDetailsInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class GetPipelineExecutionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")


class GetPipelineInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: Optional[int] = Field(default=None, alias="version")


class PipelineMetadataModel(BaseModel):
    pipeline_arn: Optional[str] = Field(default=None, alias="pipelineArn")
    created: Optional[datetime] = Field(default=None, alias="created")
    updated: Optional[datetime] = Field(default=None, alias="updated")


class GetPipelineStateInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetThirdPartyJobDetailsInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    client_token: str = Field(alias="clientToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListActionTypesInputRequestModel(BaseModel):
    action_owner_filter: Optional[Literal["AWS", "Custom", "ThirdParty"]] = Field(
        default=None, alias="actionOwnerFilter"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    region_filter: Optional[str] = Field(default=None, alias="regionFilter")


class ListPipelineExecutionsInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPipelinesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PipelineSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[int] = Field(default=None, alias="version")
    created: Optional[datetime] = Field(default=None, alias="created")
    updated: Optional[datetime] = Field(default=None, alias="updated")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListWebhooksInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StageContextModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class SourceRevisionModel(BaseModel):
    action_name: str = Field(alias="actionName")
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    revision_summary: Optional[str] = Field(default=None, alias="revisionSummary")
    revision_url: Optional[str] = Field(default=None, alias="revisionUrl")


class StopExecutionTriggerModel(BaseModel):
    reason: Optional[str] = Field(default=None, alias="reason")


class ThirdPartyJobModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="clientId")
    job_id: Optional[str] = Field(default=None, alias="jobId")


class RegisterWebhookWithThirdPartyInputRequestModel(BaseModel):
    webhook_name: Optional[str] = Field(default=None, alias="webhookName")


class RetryStageExecutionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    stage_name: str = Field(alias="stageName")
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    retry_mode: Literal["FAILED_ACTIONS"] = Field(alias="retryMode")


class StageExecutionModel(BaseModel):
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    status: Literal[
        "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded"
    ] = Field(alias="status")


class TransitionStateModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    last_changed_by: Optional[str] = Field(default=None, alias="lastChangedBy")
    last_changed_at: Optional[datetime] = Field(default=None, alias="lastChangedAt")
    disabled_reason: Optional[str] = Field(default=None, alias="disabledReason")


class StartPipelineExecutionInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class StopPipelineExecutionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    abandon: Optional[bool] = Field(default=None, alias="abandon")
    reason: Optional[str] = Field(default=None, alias="reason")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class WebhookAuthConfigurationModel(BaseModel):
    allowed_ip_range: Optional[str] = Field(default=None, alias="AllowedIPRange")
    secret_token: Optional[str] = Field(default=None, alias="SecretToken")


class WebhookFilterRuleModel(BaseModel):
    json_path: str = Field(alias="jsonPath")
    match_equals: Optional[str] = Field(default=None, alias="matchEquals")


class AcknowledgeJobOutputModel(BaseModel):
    status: Literal[
        "Created",
        "Dispatched",
        "Failed",
        "InProgress",
        "Queued",
        "Succeeded",
        "TimedOut",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcknowledgeThirdPartyJobOutputModel(BaseModel):
    status: Literal[
        "Created",
        "Dispatched",
        "Failed",
        "InProgress",
        "Queued",
        "Succeeded",
        "TimedOut",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutActionRevisionOutputModel(BaseModel):
    new_revision: bool = Field(alias="newRevision")
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutApprovalResultOutputModel(BaseModel):
    approved_at: datetime = Field(alias="approvedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetryStageExecutionOutputModel(BaseModel):
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPipelineExecutionOutputModel(BaseModel):
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopPipelineExecutionOutputModel(BaseModel):
    pipeline_execution_id: str = Field(alias="pipelineExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PollForJobsInputRequestModel(BaseModel):
    action_type_id: ActionTypeIdModel = Field(alias="actionTypeId")
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    query_param: Optional[Mapping[str, str]] = Field(default=None, alias="queryParam")


class PollForThirdPartyJobsInputRequestModel(BaseModel):
    action_type_id: ActionTypeIdModel = Field(alias="actionTypeId")
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")


class ActionDeclarationModel(BaseModel):
    name: str = Field(alias="name")
    action_type_id: ActionTypeIdModel = Field(alias="actionTypeId")
    run_order: Optional[int] = Field(default=None, alias="runOrder")
    configuration: Optional[Mapping[str, str]] = Field(
        default=None, alias="configuration"
    )
    output_artifacts: Optional[Sequence[OutputArtifactModel]] = Field(
        default=None, alias="outputArtifacts"
    )
    input_artifacts: Optional[Sequence[InputArtifactModel]] = Field(
        default=None, alias="inputArtifacts"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    region: Optional[str] = Field(default=None, alias="region")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class ListActionExecutionsInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    filter: Optional[ActionExecutionFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ActionExecutionModel(BaseModel):
    action_execution_id: Optional[str] = Field(default=None, alias="actionExecutionId")
    status: Optional[Literal["Abandoned", "Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="status"
    )
    summary: Optional[str] = Field(default=None, alias="summary")
    last_status_change: Optional[datetime] = Field(
        default=None, alias="lastStatusChange"
    )
    token: Optional[str] = Field(default=None, alias="token")
    last_updated_by: Optional[str] = Field(default=None, alias="lastUpdatedBy")
    external_execution_id: Optional[str] = Field(
        default=None, alias="externalExecutionId"
    )
    external_execution_url: Optional[str] = Field(
        default=None, alias="externalExecutionUrl"
    )
    percent_complete: Optional[int] = Field(default=None, alias="percentComplete")
    error_details: Optional[ErrorDetailsModel] = Field(
        default=None, alias="errorDetails"
    )


class PutActionRevisionInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    stage_name: str = Field(alias="stageName")
    action_name: str = Field(alias="actionName")
    action_revision: ActionRevisionModel = Field(alias="actionRevision")


class ActionTypeModel(BaseModel):
    id: ActionTypeIdModel = Field(alias="id")
    input_artifact_details: ArtifactDetailsModel = Field(alias="inputArtifactDetails")
    output_artifact_details: ArtifactDetailsModel = Field(alias="outputArtifactDetails")
    settings: Optional[ActionTypeSettingsModel] = Field(default=None, alias="settings")
    action_configuration_properties: Optional[
        List[ActionConfigurationPropertyModel]
    ] = Field(default=None, alias="actionConfigurationProperties")


class PutApprovalResultInputRequestModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    stage_name: str = Field(alias="stageName")
    action_name: str = Field(alias="actionName")
    result: ApprovalResultModel = Field(alias="result")
    token: str = Field(alias="token")


class ArtifactDetailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    s3location: Optional[S3LocationModel] = Field(default=None, alias="s3location")


class ArtifactLocationModel(BaseModel):
    type: Optional[Literal["S3"]] = Field(default=None, alias="type")
    s3_location: Optional[S3ArtifactLocationModel] = Field(
        default=None, alias="s3Location"
    )


class PipelineExecutionModel(BaseModel):
    pipeline_name: Optional[str] = Field(default=None, alias="pipelineName")
    pipeline_version: Optional[int] = Field(default=None, alias="pipelineVersion")
    pipeline_execution_id: Optional[str] = Field(
        default=None, alias="pipelineExecutionId"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Failed",
            "InProgress",
            "Stopped",
            "Stopping",
            "Succeeded",
            "Superseded",
        ]
    ] = Field(default=None, alias="status")
    status_summary: Optional[str] = Field(default=None, alias="statusSummary")
    artifact_revisions: Optional[List[ArtifactRevisionModel]] = Field(
        default=None, alias="artifactRevisions"
    )


class ArtifactStoreModel(BaseModel):
    type: Literal["S3"] = Field(alias="type")
    location: str = Field(alias="location")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="encryptionKey"
    )


class CreateCustomActionTypeInputRequestModel(BaseModel):
    category: Literal[
        "Approval", "Build", "Deploy", "Invoke", "Source", "Test"
    ] = Field(alias="category")
    provider: str = Field(alias="provider")
    version: str = Field(alias="version")
    input_artifact_details: ArtifactDetailsModel = Field(alias="inputArtifactDetails")
    output_artifact_details: ArtifactDetailsModel = Field(alias="outputArtifactDetails")
    settings: Optional[ActionTypeSettingsModel] = Field(default=None, alias="settings")
    configuration_properties: Optional[
        Sequence[ActionConfigurationPropertyModel]
    ] = Field(default=None, alias="configurationProperties")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class PutJobSuccessResultInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    current_revision: Optional[CurrentRevisionModel] = Field(
        default=None, alias="currentRevision"
    )
    continuation_token: Optional[str] = Field(default=None, alias="continuationToken")
    execution_details: Optional[ExecutionDetailsModel] = Field(
        default=None, alias="executionDetails"
    )
    output_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="outputVariables"
    )


class PutThirdPartyJobSuccessResultInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    client_token: str = Field(alias="clientToken")
    current_revision: Optional[CurrentRevisionModel] = Field(
        default=None, alias="currentRevision"
    )
    continuation_token: Optional[str] = Field(default=None, alias="continuationToken")
    execution_details: Optional[ExecutionDetailsModel] = Field(
        default=None, alias="executionDetails"
    )


class ExecutorConfigurationModel(BaseModel):
    lambda_executor_configuration: Optional[LambdaExecutorConfigurationModel] = Field(
        default=None, alias="lambdaExecutorConfiguration"
    )
    job_worker_executor_configuration: Optional[
        JobWorkerExecutorConfigurationModel
    ] = Field(default=None, alias="jobWorkerExecutorConfiguration")


class PutJobFailureResultInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    failure_details: FailureDetailsModel = Field(alias="failureDetails")


class PutThirdPartyJobFailureResultInputRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    client_token: str = Field(alias="clientToken")
    failure_details: FailureDetailsModel = Field(alias="failureDetails")


class ListActionExecutionsInputListActionExecutionsPaginateModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    filter: Optional[ActionExecutionFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListActionTypesInputListActionTypesPaginateModel(BaseModel):
    action_owner_filter: Optional[Literal["AWS", "Custom", "ThirdParty"]] = Field(
        default=None, alias="actionOwnerFilter"
    )
    region_filter: Optional[str] = Field(default=None, alias="regionFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelineExecutionsInputListPipelineExecutionsPaginateModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesInputListPipelinesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceInputListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWebhooksInputListWebhooksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesOutputModel(BaseModel):
    pipelines: List[PipelineSummaryModel] = Field(alias="pipelines")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PipelineContextModel(BaseModel):
    pipeline_name: Optional[str] = Field(default=None, alias="pipelineName")
    stage: Optional[StageContextModel] = Field(default=None, alias="stage")
    action: Optional[ActionContextModel] = Field(default=None, alias="action")
    pipeline_arn: Optional[str] = Field(default=None, alias="pipelineArn")
    pipeline_execution_id: Optional[str] = Field(
        default=None, alias="pipelineExecutionId"
    )


class PipelineExecutionSummaryModel(BaseModel):
    pipeline_execution_id: Optional[str] = Field(
        default=None, alias="pipelineExecutionId"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Failed",
            "InProgress",
            "Stopped",
            "Stopping",
            "Succeeded",
            "Superseded",
        ]
    ] = Field(default=None, alias="status")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    source_revisions: Optional[List[SourceRevisionModel]] = Field(
        default=None, alias="sourceRevisions"
    )
    trigger: Optional[ExecutionTriggerModel] = Field(default=None, alias="trigger")
    stop_trigger: Optional[StopExecutionTriggerModel] = Field(
        default=None, alias="stopTrigger"
    )


class PollForThirdPartyJobsOutputModel(BaseModel):
    jobs: List[ThirdPartyJobModel] = Field(alias="jobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WebhookDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    target_pipeline: str = Field(alias="targetPipeline")
    target_action: str = Field(alias="targetAction")
    filters: List[WebhookFilterRuleModel] = Field(alias="filters")
    authentication: Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"] = Field(
        alias="authentication"
    )
    authentication_configuration: WebhookAuthConfigurationModel = Field(
        alias="authenticationConfiguration"
    )


class StageDeclarationModel(BaseModel):
    name: str = Field(alias="name")
    actions: Sequence[ActionDeclarationModel] = Field(alias="actions")
    blockers: Optional[Sequence[BlockerDeclarationModel]] = Field(
        default=None, alias="blockers"
    )


class ActionStateModel(BaseModel):
    action_name: Optional[str] = Field(default=None, alias="actionName")
    current_revision: Optional[ActionRevisionModel] = Field(
        default=None, alias="currentRevision"
    )
    latest_execution: Optional[ActionExecutionModel] = Field(
        default=None, alias="latestExecution"
    )
    entity_url: Optional[str] = Field(default=None, alias="entityUrl")
    revision_url: Optional[str] = Field(default=None, alias="revisionUrl")


class CreateCustomActionTypeOutputModel(BaseModel):
    action_type: ActionTypeModel = Field(alias="actionType")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListActionTypesOutputModel(BaseModel):
    action_types: List[ActionTypeModel] = Field(alias="actionTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionExecutionInputModel(BaseModel):
    action_type_id: Optional[ActionTypeIdModel] = Field(
        default=None, alias="actionTypeId"
    )
    configuration: Optional[Dict[str, str]] = Field(default=None, alias="configuration")
    resolved_configuration: Optional[Dict[str, str]] = Field(
        default=None, alias="resolvedConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    region: Optional[str] = Field(default=None, alias="region")
    input_artifacts: Optional[List[ArtifactDetailModel]] = Field(
        default=None, alias="inputArtifacts"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")


class ActionExecutionOutputModel(BaseModel):
    output_artifacts: Optional[List[ArtifactDetailModel]] = Field(
        default=None, alias="outputArtifacts"
    )
    execution_result: Optional[ActionExecutionResultModel] = Field(
        default=None, alias="executionResult"
    )
    output_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="outputVariables"
    )


class ArtifactModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    revision: Optional[str] = Field(default=None, alias="revision")
    location: Optional[ArtifactLocationModel] = Field(default=None, alias="location")


class GetPipelineExecutionOutputModel(BaseModel):
    pipeline_execution: PipelineExecutionModel = Field(alias="pipelineExecution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionTypeExecutorModel(BaseModel):
    configuration: ExecutorConfigurationModel = Field(alias="configuration")
    type: Literal["JobWorker", "Lambda"] = Field(alias="type")
    policy_statements_template: Optional[str] = Field(
        default=None, alias="policyStatementsTemplate"
    )
    job_timeout: Optional[int] = Field(default=None, alias="jobTimeout")


class ListPipelineExecutionsOutputModel(BaseModel):
    pipeline_execution_summaries: List[PipelineExecutionSummaryModel] = Field(
        alias="pipelineExecutionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebhookItemModel(BaseModel):
    definition: WebhookDefinitionModel = Field(alias="definition")
    url: str = Field(alias="url")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    last_triggered: Optional[datetime] = Field(default=None, alias="lastTriggered")
    arn: Optional[str] = Field(default=None, alias="arn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class PutWebhookInputRequestModel(BaseModel):
    webhook: WebhookDefinitionModel = Field(alias="webhook")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PipelineDeclarationModel(BaseModel):
    name: str = Field(alias="name")
    role_arn: str = Field(alias="roleArn")
    stages: Sequence[StageDeclarationModel] = Field(alias="stages")
    artifact_store: Optional[ArtifactStoreModel] = Field(
        default=None, alias="artifactStore"
    )
    artifact_stores: Optional[Mapping[str, ArtifactStoreModel]] = Field(
        default=None, alias="artifactStores"
    )
    version: Optional[int] = Field(default=None, alias="version")


class StageStateModel(BaseModel):
    stage_name: Optional[str] = Field(default=None, alias="stageName")
    inbound_execution: Optional[StageExecutionModel] = Field(
        default=None, alias="inboundExecution"
    )
    inbound_transition_state: Optional[TransitionStateModel] = Field(
        default=None, alias="inboundTransitionState"
    )
    action_states: Optional[List[ActionStateModel]] = Field(
        default=None, alias="actionStates"
    )
    latest_execution: Optional[StageExecutionModel] = Field(
        default=None, alias="latestExecution"
    )


class ActionExecutionDetailModel(BaseModel):
    pipeline_execution_id: Optional[str] = Field(
        default=None, alias="pipelineExecutionId"
    )
    action_execution_id: Optional[str] = Field(default=None, alias="actionExecutionId")
    pipeline_version: Optional[int] = Field(default=None, alias="pipelineVersion")
    stage_name: Optional[str] = Field(default=None, alias="stageName")
    action_name: Optional[str] = Field(default=None, alias="actionName")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    status: Optional[Literal["Abandoned", "Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="status"
    )
    input: Optional[ActionExecutionInputModel] = Field(default=None, alias="input")
    output: Optional[ActionExecutionOutputModel] = Field(default=None, alias="output")


class JobDataModel(BaseModel):
    action_type_id: Optional[ActionTypeIdModel] = Field(
        default=None, alias="actionTypeId"
    )
    action_configuration: Optional[ActionConfigurationModel] = Field(
        default=None, alias="actionConfiguration"
    )
    pipeline_context: Optional[PipelineContextModel] = Field(
        default=None, alias="pipelineContext"
    )
    input_artifacts: Optional[List[ArtifactModel]] = Field(
        default=None, alias="inputArtifacts"
    )
    output_artifacts: Optional[List[ArtifactModel]] = Field(
        default=None, alias="outputArtifacts"
    )
    artifact_credentials: Optional[AWSSessionCredentialsModel] = Field(
        default=None, alias="artifactCredentials"
    )
    continuation_token: Optional[str] = Field(default=None, alias="continuationToken")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="encryptionKey"
    )


class ThirdPartyJobDataModel(BaseModel):
    action_type_id: Optional[ActionTypeIdModel] = Field(
        default=None, alias="actionTypeId"
    )
    action_configuration: Optional[ActionConfigurationModel] = Field(
        default=None, alias="actionConfiguration"
    )
    pipeline_context: Optional[PipelineContextModel] = Field(
        default=None, alias="pipelineContext"
    )
    input_artifacts: Optional[List[ArtifactModel]] = Field(
        default=None, alias="inputArtifacts"
    )
    output_artifacts: Optional[List[ArtifactModel]] = Field(
        default=None, alias="outputArtifacts"
    )
    artifact_credentials: Optional[AWSSessionCredentialsModel] = Field(
        default=None, alias="artifactCredentials"
    )
    continuation_token: Optional[str] = Field(default=None, alias="continuationToken")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="encryptionKey"
    )


class ActionTypeDeclarationModel(BaseModel):
    executor: ActionTypeExecutorModel = Field(alias="executor")
    id: ActionTypeIdentifierModel = Field(alias="id")
    input_artifact_details: ActionTypeArtifactDetailsModel = Field(
        alias="inputArtifactDetails"
    )
    output_artifact_details: ActionTypeArtifactDetailsModel = Field(
        alias="outputArtifactDetails"
    )
    description: Optional[str] = Field(default=None, alias="description")
    permissions: Optional[ActionTypePermissionsModel] = Field(
        default=None, alias="permissions"
    )
    properties: Optional[List[ActionTypePropertyModel]] = Field(
        default=None, alias="properties"
    )
    urls: Optional[ActionTypeUrlsModel] = Field(default=None, alias="urls")


class ListWebhooksOutputModel(BaseModel):
    webhooks: List[ListWebhookItemModel] = Field(alias="webhooks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutWebhookOutputModel(BaseModel):
    webhook: ListWebhookItemModel = Field(alias="webhook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePipelineInputRequestModel(BaseModel):
    pipeline: PipelineDeclarationModel = Field(alias="pipeline")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreatePipelineOutputModel(BaseModel):
    pipeline: PipelineDeclarationModel = Field(alias="pipeline")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPipelineOutputModel(BaseModel):
    pipeline: PipelineDeclarationModel = Field(alias="pipeline")
    metadata: PipelineMetadataModel = Field(alias="metadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineInputRequestModel(BaseModel):
    pipeline: PipelineDeclarationModel = Field(alias="pipeline")


class UpdatePipelineOutputModel(BaseModel):
    pipeline: PipelineDeclarationModel = Field(alias="pipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPipelineStateOutputModel(BaseModel):
    pipeline_name: str = Field(alias="pipelineName")
    pipeline_version: int = Field(alias="pipelineVersion")
    stage_states: List[StageStateModel] = Field(alias="stageStates")
    created: datetime = Field(alias="created")
    updated: datetime = Field(alias="updated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListActionExecutionsOutputModel(BaseModel):
    action_execution_details: List[ActionExecutionDetailModel] = Field(
        alias="actionExecutionDetails"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    data: Optional[JobDataModel] = Field(default=None, alias="data")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class JobModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    data: Optional[JobDataModel] = Field(default=None, alias="data")
    nonce: Optional[str] = Field(default=None, alias="nonce")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ThirdPartyJobDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    data: Optional[ThirdPartyJobDataModel] = Field(default=None, alias="data")
    nonce: Optional[str] = Field(default=None, alias="nonce")


class GetActionTypeOutputModel(BaseModel):
    action_type: ActionTypeDeclarationModel = Field(alias="actionType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateActionTypeInputRequestModel(BaseModel):
    action_type: ActionTypeDeclarationModel = Field(alias="actionType")


class GetJobDetailsOutputModel(BaseModel):
    job_details: JobDetailsModel = Field(alias="jobDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PollForJobsOutputModel(BaseModel):
    jobs: List[JobModel] = Field(alias="jobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetThirdPartyJobDetailsOutputModel(BaseModel):
    job_details: ThirdPartyJobDetailsModel = Field(alias="jobDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
