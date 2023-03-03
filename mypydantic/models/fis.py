# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionParameterModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    required: Optional[bool] = Field(default=None, alias="required")


class ActionTargetModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")


class CreateExperimentTemplateActionInputModel(BaseModel):
    action_id: str = Field(alias="actionId")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")
    targets: Optional[Mapping[str, str]] = Field(default=None, alias="targets")
    start_after: Optional[Sequence[str]] = Field(default=None, alias="startAfter")


class ExperimentTemplateCloudWatchLogsLogConfigurationInputModel(BaseModel):
    log_group_arn: str = Field(alias="logGroupArn")


class ExperimentTemplateS3LogConfigurationInputModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class CreateExperimentTemplateStopConditionInputModel(BaseModel):
    source: str = Field(alias="source")
    value: Optional[str] = Field(default=None, alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ExperimentTemplateTargetInputFilterModel(BaseModel):
    path: str = Field(alias="path")
    values: Sequence[str] = Field(alias="values")


class DeleteExperimentTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class ExperimentActionStateModel(BaseModel):
    status: Optional[
        Literal[
            "cancelled",
            "completed",
            "failed",
            "initiating",
            "pending",
            "running",
            "stopped",
            "stopping",
        ]
    ] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")


class ExperimentCloudWatchLogsLogConfigurationModel(BaseModel):
    log_group_arn: Optional[str] = Field(default=None, alias="logGroupArn")


class ExperimentS3LogConfigurationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class ExperimentStateModel(BaseModel):
    status: Optional[
        Literal[
            "completed",
            "failed",
            "initiating",
            "pending",
            "running",
            "stopped",
            "stopping",
        ]
    ] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")


class ExperimentStopConditionModel(BaseModel):
    source: Optional[str] = Field(default=None, alias="source")
    value: Optional[str] = Field(default=None, alias="value")


class ExperimentTargetFilterModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")
    values: Optional[List[str]] = Field(default=None, alias="values")


class ExperimentTemplateActionModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="actionId")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")
    targets: Optional[Dict[str, str]] = Field(default=None, alias="targets")
    start_after: Optional[List[str]] = Field(default=None, alias="startAfter")


class ExperimentTemplateCloudWatchLogsLogConfigurationModel(BaseModel):
    log_group_arn: Optional[str] = Field(default=None, alias="logGroupArn")


class ExperimentTemplateS3LogConfigurationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class ExperimentTemplateStopConditionModel(BaseModel):
    source: Optional[str] = Field(default=None, alias="source")
    value: Optional[str] = Field(default=None, alias="value")


class ExperimentTemplateSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ExperimentTemplateTargetFilterModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")
    values: Optional[List[str]] = Field(default=None, alias="values")


class GetActionRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetExperimentRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetExperimentTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetTargetResourceTypeRequestModel(BaseModel):
    resource_type: str = Field(alias="resourceType")


class ListActionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListExperimentTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListExperimentsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTargetResourceTypesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TargetResourceTypeSummaryModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    description: Optional[str] = Field(default=None, alias="description")


class StartExperimentRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    experiment_template_id: str = Field(alias="experimentTemplateId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StopExperimentRequestModel(BaseModel):
    id: str = Field(alias="id")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TargetResourceTypeParameterModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    required: Optional[bool] = Field(default=None, alias="required")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="tagKeys")


class UpdateExperimentTemplateActionInputItemModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="actionId")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")
    targets: Optional[Mapping[str, str]] = Field(default=None, alias="targets")
    start_after: Optional[Sequence[str]] = Field(default=None, alias="startAfter")


class UpdateExperimentTemplateStopConditionInputModel(BaseModel):
    source: str = Field(alias="source")
    value: Optional[str] = Field(default=None, alias="value")


class ActionSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    targets: Optional[Dict[str, ActionTargetModel]] = Field(
        default=None, alias="targets"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ActionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Dict[str, ActionParameterModel]] = Field(
        default=None, alias="parameters"
    )
    targets: Optional[Dict[str, ActionTargetModel]] = Field(
        default=None, alias="targets"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateExperimentTemplateLogConfigurationInputModel(BaseModel):
    log_schema_version: int = Field(alias="logSchemaVersion")
    cloud_watch_logs_configuration: Optional[
        ExperimentTemplateCloudWatchLogsLogConfigurationInputModel
    ] = Field(default=None, alias="cloudWatchLogsConfiguration")
    s3_configuration: Optional[ExperimentTemplateS3LogConfigurationInputModel] = Field(
        default=None, alias="s3Configuration"
    )


class UpdateExperimentTemplateLogConfigurationInputModel(BaseModel):
    cloud_watch_logs_configuration: Optional[
        ExperimentTemplateCloudWatchLogsLogConfigurationInputModel
    ] = Field(default=None, alias="cloudWatchLogsConfiguration")
    s3_configuration: Optional[ExperimentTemplateS3LogConfigurationInputModel] = Field(
        default=None, alias="s3Configuration"
    )
    log_schema_version: Optional[int] = Field(default=None, alias="logSchemaVersion")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentTemplateTargetInputModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    selection_mode: str = Field(alias="selectionMode")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    resource_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="resourceTags"
    )
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterModel]] = Field(
        default=None, alias="filters"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class UpdateExperimentTemplateTargetInputModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    selection_mode: str = Field(alias="selectionMode")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    resource_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="resourceTags"
    )
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterModel]] = Field(
        default=None, alias="filters"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class ExperimentActionModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="actionId")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")
    targets: Optional[Dict[str, str]] = Field(default=None, alias="targets")
    start_after: Optional[List[str]] = Field(default=None, alias="startAfter")
    state: Optional[ExperimentActionStateModel] = Field(default=None, alias="state")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")


class ExperimentLogConfigurationModel(BaseModel):
    cloud_watch_logs_configuration: Optional[
        ExperimentCloudWatchLogsLogConfigurationModel
    ] = Field(default=None, alias="cloudWatchLogsConfiguration")
    s3_configuration: Optional[ExperimentS3LogConfigurationModel] = Field(
        default=None, alias="s3Configuration"
    )
    log_schema_version: Optional[int] = Field(default=None, alias="logSchemaVersion")


class ExperimentSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    experiment_template_id: Optional[str] = Field(
        default=None, alias="experimentTemplateId"
    )
    state: Optional[ExperimentStateModel] = Field(default=None, alias="state")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ExperimentTargetModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_arns: Optional[List[str]] = Field(default=None, alias="resourceArns")
    resource_tags: Optional[Dict[str, str]] = Field(default=None, alias="resourceTags")
    filters: Optional[List[ExperimentTargetFilterModel]] = Field(
        default=None, alias="filters"
    )
    selection_mode: Optional[str] = Field(default=None, alias="selectionMode")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")


class ExperimentTemplateLogConfigurationModel(BaseModel):
    cloud_watch_logs_configuration: Optional[
        ExperimentTemplateCloudWatchLogsLogConfigurationModel
    ] = Field(default=None, alias="cloudWatchLogsConfiguration")
    s3_configuration: Optional[ExperimentTemplateS3LogConfigurationModel] = Field(
        default=None, alias="s3Configuration"
    )
    log_schema_version: Optional[int] = Field(default=None, alias="logSchemaVersion")


class ListExperimentTemplatesResponseModel(BaseModel):
    experiment_templates: List[ExperimentTemplateSummaryModel] = Field(
        alias="experimentTemplates"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExperimentTemplateTargetModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_arns: Optional[List[str]] = Field(default=None, alias="resourceArns")
    resource_tags: Optional[Dict[str, str]] = Field(default=None, alias="resourceTags")
    filters: Optional[List[ExperimentTemplateTargetFilterModel]] = Field(
        default=None, alias="filters"
    )
    selection_mode: Optional[str] = Field(default=None, alias="selectionMode")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")


class ListTargetResourceTypesResponseModel(BaseModel):
    target_resource_types: List[TargetResourceTypeSummaryModel] = Field(
        alias="targetResourceTypes"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetResourceTypeModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    description: Optional[str] = Field(default=None, alias="description")
    parameters: Optional[Dict[str, TargetResourceTypeParameterModel]] = Field(
        default=None, alias="parameters"
    )


class ListActionsResponseModel(BaseModel):
    actions: List[ActionSummaryModel] = Field(alias="actions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetActionResponseModel(BaseModel):
    action: ActionModel = Field(alias="action")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentTemplateRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    description: str = Field(alias="description")
    stop_conditions: Sequence[CreateExperimentTemplateStopConditionInputModel] = Field(
        alias="stopConditions"
    )
    actions: Mapping[str, CreateExperimentTemplateActionInputModel] = Field(
        alias="actions"
    )
    role_arn: str = Field(alias="roleArn")
    targets: Optional[Mapping[str, CreateExperimentTemplateTargetInputModel]] = Field(
        default=None, alias="targets"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    log_configuration: Optional[
        CreateExperimentTemplateLogConfigurationInputModel
    ] = Field(default=None, alias="logConfiguration")


class UpdateExperimentTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    stop_conditions: Optional[
        Sequence[UpdateExperimentTemplateStopConditionInputModel]
    ] = Field(default=None, alias="stopConditions")
    targets: Optional[Mapping[str, UpdateExperimentTemplateTargetInputModel]] = Field(
        default=None, alias="targets"
    )
    actions: Optional[
        Mapping[str, UpdateExperimentTemplateActionInputItemModel]
    ] = Field(default=None, alias="actions")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    log_configuration: Optional[
        UpdateExperimentTemplateLogConfigurationInputModel
    ] = Field(default=None, alias="logConfiguration")


class ListExperimentsResponseModel(BaseModel):
    experiments: List[ExperimentSummaryModel] = Field(alias="experiments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExperimentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    experiment_template_id: Optional[str] = Field(
        default=None, alias="experimentTemplateId"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    state: Optional[ExperimentStateModel] = Field(default=None, alias="state")
    targets: Optional[Dict[str, ExperimentTargetModel]] = Field(
        default=None, alias="targets"
    )
    actions: Optional[Dict[str, ExperimentActionModel]] = Field(
        default=None, alias="actions"
    )
    stop_conditions: Optional[List[ExperimentStopConditionModel]] = Field(
        default=None, alias="stopConditions"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    log_configuration: Optional[ExperimentLogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )


class ExperimentTemplateModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    targets: Optional[Dict[str, ExperimentTemplateTargetModel]] = Field(
        default=None, alias="targets"
    )
    actions: Optional[Dict[str, ExperimentTemplateActionModel]] = Field(
        default=None, alias="actions"
    )
    stop_conditions: Optional[List[ExperimentTemplateStopConditionModel]] = Field(
        default=None, alias="stopConditions"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    log_configuration: Optional[ExperimentTemplateLogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )


class GetTargetResourceTypeResponseModel(BaseModel):
    target_resource_type: TargetResourceTypeModel = Field(alias="targetResourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentTemplateResponseModel(BaseModel):
    experiment_template: ExperimentTemplateModel = Field(alias="experimentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteExperimentTemplateResponseModel(BaseModel):
    experiment_template: ExperimentTemplateModel = Field(alias="experimentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExperimentTemplateResponseModel(BaseModel):
    experiment_template: ExperimentTemplateModel = Field(alias="experimentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateExperimentTemplateResponseModel(BaseModel):
    experiment_template: ExperimentTemplateModel = Field(alias="experimentTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
