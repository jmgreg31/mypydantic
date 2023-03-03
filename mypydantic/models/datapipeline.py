# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ParameterValueModel(BaseModel):
    id: str = Field(alias="id")
    string_value: str = Field(alias="stringValue")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeactivatePipelineInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    cancel_active: Optional[bool] = Field(default=None, alias="cancelActive")


class DeletePipelineInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeObjectsInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    object_ids: Sequence[str] = Field(alias="objectIds")
    evaluate_expressions: Optional[bool] = Field(
        default=None, alias="evaluateExpressions"
    )
    marker: Optional[str] = Field(default=None, alias="marker")


class DescribePipelinesInputRequestModel(BaseModel):
    pipeline_ids: Sequence[str] = Field(alias="pipelineIds")


class EvaluateExpressionInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    object_id: str = Field(alias="objectId")
    expression: str = Field(alias="expression")


class FieldModel(BaseModel):
    key: str = Field(alias="key")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    ref_value: Optional[str] = Field(default=None, alias="refValue")


class GetPipelineDefinitionInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    version: Optional[str] = Field(default=None, alias="version")


class InstanceIdentityModel(BaseModel):
    document: Optional[str] = Field(default=None, alias="document")
    signature: Optional[str] = Field(default=None, alias="signature")


class ListPipelinesInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="marker")


class PipelineIdNameModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class OperatorModel(BaseModel):
    type: Optional[Literal["BETWEEN", "EQ", "GE", "LE", "REF_EQ"]] = Field(
        default=None, alias="type"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ParameterAttributeModel(BaseModel):
    key: str = Field(alias="key")
    string_value: str = Field(alias="stringValue")


class ValidationErrorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    errors: Optional[List[str]] = Field(default=None, alias="errors")


class ValidationWarningModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    warnings: Optional[List[str]] = Field(default=None, alias="warnings")


class RemoveTagsInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class ReportTaskRunnerHeartbeatInputRequestModel(BaseModel):
    taskrunner_id: str = Field(alias="taskrunnerId")
    worker_group: Optional[str] = Field(default=None, alias="workerGroup")
    hostname: Optional[str] = Field(default=None, alias="hostname")


class SetStatusInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    object_ids: Sequence[str] = Field(alias="objectIds")
    status: str = Field(alias="status")


class SetTaskStatusInputRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    task_status: Literal["FAILED", "FALSE", "FINISHED"] = Field(alias="taskStatus")
    error_id: Optional[str] = Field(default=None, alias="errorId")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    error_stack_trace: Optional[str] = Field(default=None, alias="errorStackTrace")


class ActivatePipelineInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    parameter_values: Optional[Sequence[ParameterValueModel]] = Field(
        default=None, alias="parameterValues"
    )
    start_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="startTimestamp"
    )


class AddTagsInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreatePipelineInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    unique_id: str = Field(alias="uniqueId")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreatePipelineOutputModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluateExpressionOutputModel(BaseModel):
    evaluated_expression: str = Field(alias="evaluatedExpression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryObjectsOutputModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    marker: str = Field(alias="marker")
    has_more_results: bool = Field(alias="hasMoreResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReportTaskProgressOutputModel(BaseModel):
    canceled: bool = Field(alias="canceled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReportTaskRunnerHeartbeatOutputModel(BaseModel):
    terminate: bool = Field(alias="terminate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeObjectsInputDescribeObjectsPaginateModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    object_ids: Sequence[str] = Field(alias="objectIds")
    evaluate_expressions: Optional[bool] = Field(
        default=None, alias="evaluateExpressions"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesInputListPipelinesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PipelineDescriptionModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    name: str = Field(alias="name")
    fields: List[FieldModel] = Field(alias="fields")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class PipelineObjectModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    fields: List[FieldModel] = Field(alias="fields")


class ReportTaskProgressInputRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    fields: Optional[Sequence[FieldModel]] = Field(default=None, alias="fields")


class PollForTaskInputRequestModel(BaseModel):
    worker_group: str = Field(alias="workerGroup")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    instance_identity: Optional[InstanceIdentityModel] = Field(
        default=None, alias="instanceIdentity"
    )


class ListPipelinesOutputModel(BaseModel):
    pipeline_id_list: List[PipelineIdNameModel] = Field(alias="pipelineIdList")
    marker: str = Field(alias="marker")
    has_more_results: bool = Field(alias="hasMoreResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SelectorModel(BaseModel):
    field_name: Optional[str] = Field(default=None, alias="fieldName")
    operator: Optional[OperatorModel] = Field(default=None, alias="operator")


class ParameterObjectModel(BaseModel):
    id: str = Field(alias="id")
    attributes: List[ParameterAttributeModel] = Field(alias="attributes")


class PutPipelineDefinitionOutputModel(BaseModel):
    validation_errors: List[ValidationErrorModel] = Field(alias="validationErrors")
    validation_warnings: List[ValidationWarningModel] = Field(
        alias="validationWarnings"
    )
    errored: bool = Field(alias="errored")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidatePipelineDefinitionOutputModel(BaseModel):
    validation_errors: List[ValidationErrorModel] = Field(alias="validationErrors")
    validation_warnings: List[ValidationWarningModel] = Field(
        alias="validationWarnings"
    )
    errored: bool = Field(alias="errored")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePipelinesOutputModel(BaseModel):
    pipeline_description_list: List[PipelineDescriptionModel] = Field(
        alias="pipelineDescriptionList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeObjectsOutputModel(BaseModel):
    pipeline_objects: List[PipelineObjectModel] = Field(alias="pipelineObjects")
    marker: str = Field(alias="marker")
    has_more_results: bool = Field(alias="hasMoreResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaskObjectModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    pipeline_id: Optional[str] = Field(default=None, alias="pipelineId")
    attempt_id: Optional[str] = Field(default=None, alias="attemptId")
    objects: Optional[Dict[str, PipelineObjectModel]] = Field(
        default=None, alias="objects"
    )


class QueryModel(BaseModel):
    selectors: Optional[Sequence[SelectorModel]] = Field(
        default=None, alias="selectors"
    )


class GetPipelineDefinitionOutputModel(BaseModel):
    pipeline_objects: List[PipelineObjectModel] = Field(alias="pipelineObjects")
    parameter_objects: List[ParameterObjectModel] = Field(alias="parameterObjects")
    parameter_values: List[ParameterValueModel] = Field(alias="parameterValues")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPipelineDefinitionInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    pipeline_objects: Sequence[PipelineObjectModel] = Field(alias="pipelineObjects")
    parameter_objects: Optional[Sequence[ParameterObjectModel]] = Field(
        default=None, alias="parameterObjects"
    )
    parameter_values: Optional[Sequence[ParameterValueModel]] = Field(
        default=None, alias="parameterValues"
    )


class ValidatePipelineDefinitionInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    pipeline_objects: Sequence[PipelineObjectModel] = Field(alias="pipelineObjects")
    parameter_objects: Optional[Sequence[ParameterObjectModel]] = Field(
        default=None, alias="parameterObjects"
    )
    parameter_values: Optional[Sequence[ParameterValueModel]] = Field(
        default=None, alias="parameterValues"
    )


class PollForTaskOutputModel(BaseModel):
    task_object: TaskObjectModel = Field(alias="taskObject")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryObjectsInputQueryObjectsPaginateModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    sphere: str = Field(alias="sphere")
    query: Optional[QueryModel] = Field(default=None, alias="query")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class QueryObjectsInputRequestModel(BaseModel):
    pipeline_id: str = Field(alias="pipelineId")
    sphere: str = Field(alias="sphere")
    query: Optional[QueryModel] = Field(default=None, alias="query")
    marker: Optional[str] = Field(default=None, alias="marker")
    limit: Optional[int] = Field(default=None, alias="limit")
