# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class StepInputModel(BaseModel):
    integer_value: Optional[int] = Field(default=None, alias="integerValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    list_of_strings_value: Optional[Sequence[str]] = Field(
        default=None, alias="listOfStringsValue"
    )
    map_of_string_value: Optional[Mapping[str, str]] = Field(
        default=None, alias="mapOfStringValue"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateWorkflowStepGroupRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    next: Optional[Sequence[str]] = Field(default=None, alias="next")
    previous: Optional[Sequence[str]] = Field(default=None, alias="previous")


class ToolModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    url: Optional[str] = Field(default=None, alias="url")


class DeleteMigrationWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteWorkflowStepGroupRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    id: str = Field(alias="id")


class DeleteWorkflowStepRequestModel(BaseModel):
    id: str = Field(alias="id")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")


class GetMigrationWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetMigrationWorkflowTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class TemplateInputModel(BaseModel):
    input_name: Optional[str] = Field(default=None, alias="inputName")
    data_type: Optional[
        Literal["INTEGER", "STRING", "STRINGLIST", "STRINGMAP"]
    ] = Field(default=None, alias="dataType")
    required: Optional[bool] = Field(default=None, alias="required")


class GetTemplateStepGroupRequestModel(BaseModel):
    template_id: str = Field(alias="templateId")
    id: str = Field(alias="id")


class GetTemplateStepRequestModel(BaseModel):
    id: str = Field(alias="id")
    template_id: str = Field(alias="templateId")
    step_group_id: str = Field(alias="stepGroupId")


class StepOutputModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    data_type: Optional[
        Literal["INTEGER", "STRING", "STRINGLIST", "STRINGMAP"]
    ] = Field(default=None, alias="dataType")
    required: Optional[bool] = Field(default=None, alias="required")


class GetWorkflowStepGroupRequestModel(BaseModel):
    id: str = Field(alias="id")
    workflow_id: str = Field(alias="workflowId")


class GetWorkflowStepRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    step_group_id: str = Field(alias="stepGroupId")
    id: str = Field(alias="id")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListMigrationWorkflowTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    name: Optional[str] = Field(default=None, alias="name")


class TemplateSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")


class ListMigrationWorkflowsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    template_id: Optional[str] = Field(default=None, alias="templateId")
    ads_application_configuration_name: Optional[str] = Field(
        default=None, alias="adsApplicationConfigurationName"
    )
    status: Optional[
        Literal[
            "COMPLETED",
            "CREATING",
            "CREATION_FAILED",
            "DELETED",
            "DELETING",
            "DELETION_FAILED",
            "IN_PROGRESS",
            "NOT_STARTED",
            "PAUSED",
            "PAUSING",
            "PAUSING_FAILED",
            "STARTING",
            "USER_ATTENTION_REQUIRED",
            "WORKFLOW_FAILED",
        ]
    ] = Field(default=None, alias="status")
    name: Optional[str] = Field(default=None, alias="name")


class MigrationWorkflowSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    template_id: Optional[str] = Field(default=None, alias="templateId")
    ads_application_configuration_name: Optional[str] = Field(
        default=None, alias="adsApplicationConfigurationName"
    )
    status: Optional[
        Literal[
            "COMPLETED",
            "CREATING",
            "CREATION_FAILED",
            "DELETED",
            "DELETING",
            "DELETION_FAILED",
            "IN_PROGRESS",
            "NOT_STARTED",
            "PAUSED",
            "PAUSING",
            "PAUSING_FAILED",
            "STARTING",
            "USER_ATTENTION_REQUIRED",
            "WORKFLOW_FAILED",
        ]
    ] = Field(default=None, alias="status")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    completed_steps: Optional[int] = Field(default=None, alias="completedSteps")
    total_steps: Optional[int] = Field(default=None, alias="totalSteps")


class ListPluginsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PluginSummaryModel(BaseModel):
    plugin_id: Optional[str] = Field(default=None, alias="pluginId")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    status: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="status"
    )
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    version: Optional[str] = Field(default=None, alias="version")
    registered_time: Optional[str] = Field(default=None, alias="registeredTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTemplateStepGroupsRequestModel(BaseModel):
    template_id: str = Field(alias="templateId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TemplateStepGroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    previous: Optional[List[str]] = Field(default=None, alias="previous")
    next: Optional[List[str]] = Field(default=None, alias="next")


class ListTemplateStepsRequestModel(BaseModel):
    template_id: str = Field(alias="templateId")
    step_group_id: str = Field(alias="stepGroupId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TemplateStepSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    step_group_id: Optional[str] = Field(default=None, alias="stepGroupId")
    template_id: Optional[str] = Field(default=None, alias="templateId")
    name: Optional[str] = Field(default=None, alias="name")
    step_action_type: Optional[Literal["AUTOMATED", "MANUAL"]] = Field(
        default=None, alias="stepActionType"
    )
    target_type: Optional[Literal["ALL", "NONE", "SINGLE"]] = Field(
        default=None, alias="targetType"
    )
    owner: Optional[Literal["AWS_MANAGED", "CUSTOM"]] = Field(
        default=None, alias="owner"
    )
    previous: Optional[List[str]] = Field(default=None, alias="previous")
    next: Optional[List[str]] = Field(default=None, alias="next")


class ListWorkflowStepGroupsRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class WorkflowStepGroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    owner: Optional[Literal["AWS_MANAGED", "CUSTOM"]] = Field(
        default=None, alias="owner"
    )
    status: Optional[
        Literal[
            "AWAITING_DEPENDENCIES",
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "PAUSED",
            "PAUSING",
            "READY",
            "USER_ATTENTION_REQUIRED",
        ]
    ] = Field(default=None, alias="status")
    previous: Optional[List[str]] = Field(default=None, alias="previous")
    next: Optional[List[str]] = Field(default=None, alias="next")


class ListWorkflowStepsRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    step_group_id: str = Field(alias="stepGroupId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class WorkflowStepSummaryModel(BaseModel):
    step_id: Optional[str] = Field(default=None, alias="stepId")
    name: Optional[str] = Field(default=None, alias="name")
    step_action_type: Optional[Literal["AUTOMATED", "MANUAL"]] = Field(
        default=None, alias="stepActionType"
    )
    owner: Optional[Literal["AWS_MANAGED", "CUSTOM"]] = Field(
        default=None, alias="owner"
    )
    previous: Optional[List[str]] = Field(default=None, alias="previous")
    next: Optional[List[str]] = Field(default=None, alias="next")
    status: Optional[
        Literal[
            "AWAITING_DEPENDENCIES",
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "PAUSED",
            "READY",
            "USER_ATTENTION_REQUIRED",
        ]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    no_of_srv_completed: Optional[int] = Field(default=None, alias="noOfSrvCompleted")
    no_of_srv_failed: Optional[int] = Field(default=None, alias="noOfSrvFailed")
    total_no_of_srv: Optional[int] = Field(default=None, alias="totalNoOfSrv")
    description: Optional[str] = Field(default=None, alias="description")
    script_location: Optional[str] = Field(default=None, alias="scriptLocation")


class PlatformCommandModel(BaseModel):
    linux: Optional[str] = Field(default=None, alias="linux")
    windows: Optional[str] = Field(default=None, alias="windows")


class PlatformScriptKeyModel(BaseModel):
    linux: Optional[str] = Field(default=None, alias="linux")
    windows: Optional[str] = Field(default=None, alias="windows")


class RetryWorkflowStepRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    step_group_id: str = Field(alias="stepGroupId")
    id: str = Field(alias="id")


class StartMigrationWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")


class StopMigrationWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateWorkflowStepGroupRequestModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    next: Optional[Sequence[str]] = Field(default=None, alias="next")
    previous: Optional[Sequence[str]] = Field(default=None, alias="previous")


class WorkflowStepOutputUnionModel(BaseModel):
    integer_value: Optional[int] = Field(default=None, alias="integerValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    list_of_string_value: Optional[Sequence[str]] = Field(
        default=None, alias="listOfStringValue"
    )


class CreateMigrationWorkflowRequestModel(BaseModel):
    name: str = Field(alias="name")
    template_id: str = Field(alias="templateId")
    application_configuration_id: str = Field(alias="applicationConfigurationId")
    input_parameters: Mapping[str, StepInputModel] = Field(alias="inputParameters")
    description: Optional[str] = Field(default=None, alias="description")
    step_targets: Optional[Sequence[str]] = Field(default=None, alias="stepTargets")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateMigrationWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    input_parameters: Optional[Mapping[str, StepInputModel]] = Field(
        default=None, alias="inputParameters"
    )
    step_targets: Optional[Sequence[str]] = Field(default=None, alias="stepTargets")


class CreateMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    template_id: str = Field(alias="templateId")
    ads_application_configuration_id: str = Field(alias="adsApplicationConfigurationId")
    workflow_inputs: Dict[str, StepInputModel] = Field(alias="workflowInputs")
    step_targets: List[str] = Field(alias="stepTargets")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowStepResponseModel(BaseModel):
    id: str = Field(alias="id")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetryWorkflowStepResponseModel(BaseModel):
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    id: str = Field(alias="id")
    status: Literal[
        "AWAITING_DEPENDENCIES",
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "PAUSED",
        "READY",
        "USER_ATTENTION_REQUIRED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    last_start_time: datetime = Field(alias="lastStartTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    last_stop_time: datetime = Field(alias="lastStopTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    template_id: str = Field(alias="templateId")
    ads_application_configuration_id: str = Field(alias="adsApplicationConfigurationId")
    workflow_inputs: Dict[str, StepInputModel] = Field(alias="workflowInputs")
    step_targets: List[str] = Field(alias="stepTargets")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkflowStepResponseModel(BaseModel):
    id: str = Field(alias="id")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowStepGroupResponseModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    id: str = Field(alias="id")
    description: str = Field(alias="description")
    tools: List[ToolModel] = Field(alias="tools")
    next: List[str] = Field(alias="next")
    previous: List[str] = Field(alias="previous")
    creation_time: datetime = Field(alias="creationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMigrationWorkflowResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    template_id: str = Field(alias="templateId")
    ads_application_configuration_id: str = Field(alias="adsApplicationConfigurationId")
    ads_application_name: str = Field(alias="adsApplicationName")
    status: Literal[
        "COMPLETED",
        "CREATING",
        "CREATION_FAILED",
        "DELETED",
        "DELETING",
        "DELETION_FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "PAUSED",
        "PAUSING",
        "PAUSING_FAILED",
        "STARTING",
        "USER_ATTENTION_REQUIRED",
        "WORKFLOW_FAILED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    creation_time: datetime = Field(alias="creationTime")
    last_start_time: datetime = Field(alias="lastStartTime")
    last_stop_time: datetime = Field(alias="lastStopTime")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    end_time: datetime = Field(alias="endTime")
    tools: List[ToolModel] = Field(alias="tools")
    total_steps: int = Field(alias="totalSteps")
    completed_steps: int = Field(alias="completedSteps")
    workflow_inputs: Dict[str, StepInputModel] = Field(alias="workflowInputs")
    tags: Dict[str, str] = Field(alias="tags")
    workflow_bucket: str = Field(alias="workflowBucket")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemplateStepGroupResponseModel(BaseModel):
    template_id: str = Field(alias="templateId")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    status: Literal[
        "AWAITING_DEPENDENCIES",
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "PAUSED",
        "PAUSING",
        "READY",
        "USER_ATTENTION_REQUIRED",
    ] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    tools: List[ToolModel] = Field(alias="tools")
    previous: List[str] = Field(alias="previous")
    next: List[str] = Field(alias="next")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowStepGroupResponseModel(BaseModel):
    id: str = Field(alias="id")
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    status: Literal[
        "AWAITING_DEPENDENCIES",
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "PAUSED",
        "PAUSING",
        "READY",
        "USER_ATTENTION_REQUIRED",
    ] = Field(alias="status")
    owner: Literal["AWS_MANAGED", "CUSTOM"] = Field(alias="owner")
    creation_time: datetime = Field(alias="creationTime")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    end_time: datetime = Field(alias="endTime")
    tools: List[ToolModel] = Field(alias="tools")
    previous: List[str] = Field(alias="previous")
    next: List[str] = Field(alias="next")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkflowStepGroupResponseModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    name: str = Field(alias="name")
    id: str = Field(alias="id")
    description: str = Field(alias="description")
    tools: List[ToolModel] = Field(alias="tools")
    next: List[str] = Field(alias="next")
    previous: List[str] = Field(alias="previous")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMigrationWorkflowTemplateResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    inputs: List[TemplateInputModel] = Field(alias="inputs")
    tools: List[ToolModel] = Field(alias="tools")
    status: Literal["CREATED"] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMigrationWorkflowTemplatesRequestListTemplatesPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMigrationWorkflowsRequestListWorkflowsPaginateModel(BaseModel):
    template_id: Optional[str] = Field(default=None, alias="templateId")
    ads_application_configuration_name: Optional[str] = Field(
        default=None, alias="adsApplicationConfigurationName"
    )
    status: Optional[
        Literal[
            "COMPLETED",
            "CREATING",
            "CREATION_FAILED",
            "DELETED",
            "DELETING",
            "DELETION_FAILED",
            "IN_PROGRESS",
            "NOT_STARTED",
            "PAUSED",
            "PAUSING",
            "PAUSING_FAILED",
            "STARTING",
            "USER_ATTENTION_REQUIRED",
            "WORKFLOW_FAILED",
        ]
    ] = Field(default=None, alias="status")
    name: Optional[str] = Field(default=None, alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPluginsRequestListPluginsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateModel(BaseModel):
    template_id: str = Field(alias="templateId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplateStepsRequestListTemplateStepsPaginateModel(BaseModel):
    template_id: str = Field(alias="templateId")
    step_group_id: str = Field(alias="stepGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkflowStepsRequestListWorkflowStepsPaginateModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    step_group_id: str = Field(alias="stepGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMigrationWorkflowTemplatesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    template_summary: List[TemplateSummaryModel] = Field(alias="templateSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMigrationWorkflowsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    migration_workflow_summary: List[MigrationWorkflowSummaryModel] = Field(
        alias="migrationWorkflowSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPluginsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    plugins: List[PluginSummaryModel] = Field(alias="plugins")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplateStepGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    template_step_group_summary: List[TemplateStepGroupSummaryModel] = Field(
        alias="templateStepGroupSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplateStepsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    template_step_summary_list: List[TemplateStepSummaryModel] = Field(
        alias="templateStepSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkflowStepGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workflow_step_groups_summary: List[WorkflowStepGroupSummaryModel] = Field(
        alias="workflowStepGroupsSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkflowStepsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workflow_steps_summary: List[WorkflowStepSummaryModel] = Field(
        alias="workflowStepsSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StepAutomationConfigurationModel(BaseModel):
    script_location_s3_bucket: Optional[str] = Field(
        default=None, alias="scriptLocationS3Bucket"
    )
    script_location_s3_key: Optional[PlatformScriptKeyModel] = Field(
        default=None, alias="scriptLocationS3Key"
    )
    command: Optional[PlatformCommandModel] = Field(default=None, alias="command")
    run_environment: Optional[Literal["AWS", "ONPREMISE"]] = Field(
        default=None, alias="runEnvironment"
    )
    target_type: Optional[Literal["ALL", "NONE", "SINGLE"]] = Field(
        default=None, alias="targetType"
    )


class WorkflowStepAutomationConfigurationModel(BaseModel):
    script_location_s3_bucket: Optional[str] = Field(
        default=None, alias="scriptLocationS3Bucket"
    )
    script_location_s3_key: Optional[PlatformScriptKeyModel] = Field(
        default=None, alias="scriptLocationS3Key"
    )
    command: Optional[PlatformCommandModel] = Field(default=None, alias="command")
    run_environment: Optional[Literal["AWS", "ONPREMISE"]] = Field(
        default=None, alias="runEnvironment"
    )
    target_type: Optional[Literal["ALL", "NONE", "SINGLE"]] = Field(
        default=None, alias="targetType"
    )


class WorkflowStepOutputModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    data_type: Optional[
        Literal["INTEGER", "STRING", "STRINGLIST", "STRINGMAP"]
    ] = Field(default=None, alias="dataType")
    required: Optional[bool] = Field(default=None, alias="required")
    value: Optional[WorkflowStepOutputUnionModel] = Field(default=None, alias="value")


class GetTemplateStepResponseModel(BaseModel):
    id: str = Field(alias="id")
    step_group_id: str = Field(alias="stepGroupId")
    template_id: str = Field(alias="templateId")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    step_action_type: Literal["AUTOMATED", "MANUAL"] = Field(alias="stepActionType")
    creation_time: str = Field(alias="creationTime")
    previous: List[str] = Field(alias="previous")
    next: List[str] = Field(alias="next")
    outputs: List[StepOutputModel] = Field(alias="outputs")
    step_automation_configuration: StepAutomationConfigurationModel = Field(
        alias="stepAutomationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowStepRequestModel(BaseModel):
    name: str = Field(alias="name")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    step_action_type: Literal["AUTOMATED", "MANUAL"] = Field(alias="stepActionType")
    description: Optional[str] = Field(default=None, alias="description")
    workflow_step_automation_configuration: Optional[
        WorkflowStepAutomationConfigurationModel
    ] = Field(default=None, alias="workflowStepAutomationConfiguration")
    step_target: Optional[Sequence[str]] = Field(default=None, alias="stepTarget")
    outputs: Optional[Sequence[WorkflowStepOutputModel]] = Field(
        default=None, alias="outputs"
    )
    previous: Optional[Sequence[str]] = Field(default=None, alias="previous")
    next: Optional[Sequence[str]] = Field(default=None, alias="next")


class GetWorkflowStepResponseModel(BaseModel):
    name: str = Field(alias="name")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    step_id: str = Field(alias="stepId")
    description: str = Field(alias="description")
    step_action_type: Literal["AUTOMATED", "MANUAL"] = Field(alias="stepActionType")
    owner: Literal["AWS_MANAGED", "CUSTOM"] = Field(alias="owner")
    workflow_step_automation_configuration: WorkflowStepAutomationConfigurationModel = (
        Field(alias="workflowStepAutomationConfiguration")
    )
    step_target: List[str] = Field(alias="stepTarget")
    outputs: List[WorkflowStepOutputModel] = Field(alias="outputs")
    previous: List[str] = Field(alias="previous")
    next: List[str] = Field(alias="next")
    status: Literal[
        "AWAITING_DEPENDENCIES",
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "PAUSED",
        "READY",
        "USER_ATTENTION_REQUIRED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    script_output_location: str = Field(alias="scriptOutputLocation")
    creation_time: datetime = Field(alias="creationTime")
    last_start_time: datetime = Field(alias="lastStartTime")
    end_time: datetime = Field(alias="endTime")
    no_of_srv_completed: int = Field(alias="noOfSrvCompleted")
    no_of_srv_failed: int = Field(alias="noOfSrvFailed")
    total_no_of_srv: int = Field(alias="totalNoOfSrv")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkflowStepRequestModel(BaseModel):
    id: str = Field(alias="id")
    step_group_id: str = Field(alias="stepGroupId")
    workflow_id: str = Field(alias="workflowId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    step_action_type: Optional[Literal["AUTOMATED", "MANUAL"]] = Field(
        default=None, alias="stepActionType"
    )
    workflow_step_automation_configuration: Optional[
        WorkflowStepAutomationConfigurationModel
    ] = Field(default=None, alias="workflowStepAutomationConfiguration")
    step_target: Optional[Sequence[str]] = Field(default=None, alias="stepTarget")
    outputs: Optional[Sequence[WorkflowStepOutputModel]] = Field(
        default=None, alias="outputs"
    )
    previous: Optional[Sequence[str]] = Field(default=None, alias="previous")
    next: Optional[Sequence[str]] = Field(default=None, alias="next")
    status: Optional[
        Literal[
            "AWAITING_DEPENDENCIES",
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "PAUSED",
            "READY",
            "USER_ATTENTION_REQUIRED",
        ]
    ] = Field(default=None, alias="status")
