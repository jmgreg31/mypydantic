# Model Generated: Thu Mar  2 21:56:21 2023

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


class ActivateReadSetFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")


class ActivateReadSetJobItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")


class ActivateReadSetSourceItemModel(BaseModel):
    read_set_id: str = Field(alias="readSetId")
    status: Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class AnnotationImportItemDetailModel(BaseModel):
    job_status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="jobStatus")
    source: str = Field(alias="source")


class AnnotationImportItemSourceModel(BaseModel):
    source: str = Field(alias="source")


class AnnotationImportJobItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    destination_name: str = Field(alias="destinationName")
    id: str = Field(alias="id")
    role_arn: str = Field(alias="roleArn")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    update_time: datetime = Field(alias="updateTime")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")
    run_left_normalization: Optional[bool] = Field(
        default=None, alias="runLeftNormalization"
    )


class ReferenceItemModel(BaseModel):
    reference_arn: Optional[str] = Field(default=None, alias="referenceArn")


class SseConfigModel(BaseModel):
    type: Literal["KMS"] = Field(alias="type")
    key_arn: Optional[str] = Field(default=None, alias="keyArn")


class BatchDeleteReadSetRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")
    sequence_store_id: str = Field(alias="sequenceStoreId")


class ReadSetBatchErrorModel(BaseModel):
    code: str = Field(alias="code")
    id: str = Field(alias="id")
    message: str = Field(alias="message")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CancelAnnotationImportRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class CancelRunRequestModel(BaseModel):
    id: str = Field(alias="id")


class CancelVariantImportRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class CreateRunGroupRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    max_cpus: Optional[int] = Field(default=None, alias="maxCpus")
    max_duration: Optional[int] = Field(default=None, alias="maxDuration")
    max_runs: Optional[int] = Field(default=None, alias="maxRuns")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class WorkflowParameterModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    optional: Optional[bool] = Field(default=None, alias="optional")


class DeleteAnnotationStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    force: Optional[bool] = Field(default=None, alias="force")


class DeleteReferenceRequestModel(BaseModel):
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")


class DeleteReferenceStoreRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteRunGroupRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteRunRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteSequenceStoreRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteVariantStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    force: Optional[bool] = Field(default=None, alias="force")


class DeleteWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")


class ExportReadSetDetailModel(BaseModel):
    id: str = Field(alias="id")
    status: Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ExportReadSetFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")


class ExportReadSetJobDetailModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    destination: str = Field(alias="destination")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")


class ExportReadSetModel(BaseModel):
    read_set_id: str = Field(alias="readSetId")


class FileInformationModel(BaseModel):
    content_length: Optional[int] = Field(default=None, alias="contentLength")
    part_size: Optional[int] = Field(default=None, alias="partSize")
    total_parts: Optional[int] = Field(default=None, alias="totalParts")


class VcfOptionsModel(BaseModel):
    ignore_filter_field: Optional[bool] = Field(default=None, alias="ignoreFilterField")
    ignore_qual_field: Optional[bool] = Field(default=None, alias="ignoreQualField")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetAnnotationImportRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class GetAnnotationStoreRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetReadSetActivationJobRequestModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")


class GetReadSetExportJobRequestModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")


class GetReadSetImportJobRequestModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")


class GetReadSetMetadataRequestModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")


class SequenceInformationModel(BaseModel):
    alignment: Optional[str] = Field(default=None, alias="alignment")
    generated_from: Optional[str] = Field(default=None, alias="generatedFrom")
    total_base_count: Optional[int] = Field(default=None, alias="totalBaseCount")
    total_read_count: Optional[int] = Field(default=None, alias="totalReadCount")


class GetReadSetRequestModel(BaseModel):
    id: str = Field(alias="id")
    part_number: int = Field(alias="partNumber")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    file: Optional[Literal["INDEX", "SOURCE1", "SOURCE2"]] = Field(
        default=None, alias="file"
    )


class GetReferenceImportJobRequestModel(BaseModel):
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")


class ImportReferenceSourceItemModel(BaseModel):
    status: Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="status"
    )
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    source_file: Optional[str] = Field(default=None, alias="sourceFile")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class GetReferenceMetadataRequestModel(BaseModel):
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")


class GetReferenceRequestModel(BaseModel):
    id: str = Field(alias="id")
    part_number: int = Field(alias="partNumber")
    reference_store_id: str = Field(alias="referenceStoreId")
    file: Optional[Literal["INDEX", "SOURCE"]] = Field(default=None, alias="file")
    range: Optional[str] = Field(default=None, alias="range")


class GetReferenceStoreRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetRunGroupRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetRunRequestModel(BaseModel):
    id: str = Field(alias="id")
    export: Optional[Sequence[Literal["DEFINITION"]]] = Field(
        default=None, alias="export"
    )


class GetRunTaskRequestModel(BaseModel):
    id: str = Field(alias="id")
    task_id: str = Field(alias="taskId")


class GetSequenceStoreRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetVariantImportRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class VariantImportItemDetailModel(BaseModel):
    job_status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="jobStatus")
    source: str = Field(alias="source")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class GetVariantStoreRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")
    export: Optional[Sequence[Literal["DEFINITION"]]] = Field(
        default=None, alias="export"
    )
    type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(default=None, alias="type")


class ImportReadSetFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")


class ImportReadSetJobItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    role_arn: str = Field(alias="roleArn")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")


class SourceFilesModel(BaseModel):
    source1: str = Field(alias="source1")
    source2: Optional[str] = Field(default=None, alias="source2")


class ImportReferenceFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")


class ImportReferenceJobItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")
    role_arn: str = Field(alias="roleArn")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")


class ListAnnotationImportJobsFilterModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")
    store_name: Optional[str] = Field(default=None, alias="storeName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAnnotationStoresFilterModel(BaseModel):
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="status")


class ReadSetFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    name: Optional[str] = Field(default=None, alias="name")
    reference_arn: Optional[str] = Field(default=None, alias="referenceArn")
    status: Optional[
        Literal["ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING"]
    ] = Field(default=None, alias="status")


class ReferenceStoreFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    name: Optional[str] = Field(default=None, alias="name")


class ReferenceFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    md5: Optional[str] = Field(default=None, alias="md5")
    name: Optional[str] = Field(default=None, alias="name")


class ReferenceListItemModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    md5: str = Field(alias="md5")
    reference_store_id: str = Field(alias="referenceStoreId")
    update_time: datetime = Field(alias="updateTime")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "DELETED", "DELETING"]] = Field(
        default=None, alias="status"
    )


class ListRunGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    starting_token: Optional[str] = Field(default=None, alias="startingToken")


class RunGroupListItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    id: Optional[str] = Field(default=None, alias="id")
    max_cpus: Optional[int] = Field(default=None, alias="maxCpus")
    max_duration: Optional[int] = Field(default=None, alias="maxDuration")
    max_runs: Optional[int] = Field(default=None, alias="maxRuns")
    name: Optional[str] = Field(default=None, alias="name")


class ListRunTasksRequestModel(BaseModel):
    id: str = Field(alias="id")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    starting_token: Optional[str] = Field(default=None, alias="startingToken")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PENDING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")


class TaskListItemModel(BaseModel):
    cpus: Optional[int] = Field(default=None, alias="cpus")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    memory: Optional[int] = Field(default=None, alias="memory")
    name: Optional[str] = Field(default=None, alias="name")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PENDING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    stop_time: Optional[datetime] = Field(default=None, alias="stopTime")
    task_id: Optional[str] = Field(default=None, alias="taskId")


class ListRunsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    run_group_id: Optional[str] = Field(default=None, alias="runGroupId")
    starting_token: Optional[str] = Field(default=None, alias="startingToken")


class RunListItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    priority: Optional[int] = Field(default=None, alias="priority")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "DELETED",
            "FAILED",
            "PENDING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    stop_time: Optional[datetime] = Field(default=None, alias="stopTime")
    storage_capacity: Optional[int] = Field(default=None, alias="storageCapacity")
    workflow_id: Optional[str] = Field(default=None, alias="workflowId")


class SequenceStoreFilterModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    name: Optional[str] = Field(default=None, alias="name")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListVariantImportJobsFilterModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "IN_PROGRESS",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="status")
    store_name: Optional[str] = Field(default=None, alias="storeName")


class VariantImportJobItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    destination_name: str = Field(alias="destinationName")
    id: str = Field(alias="id")
    role_arn: str = Field(alias="roleArn")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    update_time: datetime = Field(alias="updateTime")
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")
    run_left_normalization: Optional[bool] = Field(
        default=None, alias="runLeftNormalization"
    )


class ListVariantStoresFilterModel(BaseModel):
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="status")


class ListWorkflowsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    starting_token: Optional[str] = Field(default=None, alias="startingToken")
    type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(default=None, alias="type")


class WorkflowListItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    digest: Optional[str] = Field(default=None, alias="digest")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]
    ] = Field(default=None, alias="status")
    type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(default=None, alias="type")


class ReadOptionsModel(BaseModel):
    comment: Optional[str] = Field(default=None, alias="comment")
    encoding: Optional[str] = Field(default=None, alias="encoding")
    escape: Optional[str] = Field(default=None, alias="escape")
    escape_quotes: Optional[bool] = Field(default=None, alias="escapeQuotes")
    header: Optional[bool] = Field(default=None, alias="header")
    line_sep: Optional[str] = Field(default=None, alias="lineSep")
    quote: Optional[str] = Field(default=None, alias="quote")
    quote_all: Optional[bool] = Field(default=None, alias="quoteAll")
    sep: Optional[str] = Field(default=None, alias="sep")


class StartReadSetActivationJobSourceItemModel(BaseModel):
    read_set_id: str = Field(alias="readSetId")


class StartReferenceImportJobSourceItemModel(BaseModel):
    name: str = Field(alias="name")
    source_file: str = Field(alias="sourceFile")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StartRunRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    role_arn: str = Field(alias="roleArn")
    log_level: Optional[Literal["ALL", "ERROR", "FATAL", "OFF"]] = Field(
        default=None, alias="logLevel"
    )
    name: Optional[str] = Field(default=None, alias="name")
    output_uri: Optional[str] = Field(default=None, alias="outputUri")
    parameters: Optional[Mapping[str, Any]] = Field(default=None, alias="parameters")
    priority: Optional[int] = Field(default=None, alias="priority")
    run_group_id: Optional[str] = Field(default=None, alias="runGroupId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    storage_capacity: Optional[int] = Field(default=None, alias="storageCapacity")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    workflow_id: Optional[str] = Field(default=None, alias="workflowId")
    workflow_type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(
        default=None, alias="workflowType"
    )


class VariantImportItemSourceModel(BaseModel):
    source: str = Field(alias="source")


class TsvStoreOptionsModel(BaseModel):
    annotation_type: Optional[
        Literal[
            "CHR_POS",
            "CHR_POS_REF_ALT",
            "CHR_START_END_ONE_BASE",
            "CHR_START_END_REF_ALT_ONE_BASE",
            "CHR_START_END_REF_ALT_ZERO_BASE",
            "CHR_START_END_ZERO_BASE",
            "GENERIC",
        ]
    ] = Field(default=None, alias="annotationType")
    format_to_header: Optional[
        Mapping[Literal["ALT", "CHR", "END", "POS", "REF", "START"], str]
    ] = Field(default=None, alias="formatToHeader")
    schema_: Optional[
        Sequence[
            Mapping[str, Literal["BOOLEAN", "DOUBLE", "FLOAT", "INT", "LONG", "STRING"]]
        ]
    ] = Field(default=None, alias="schema")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAnnotationStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateRunGroupRequestModel(BaseModel):
    id: str = Field(alias="id")
    max_cpus: Optional[int] = Field(default=None, alias="maxCpus")
    max_duration: Optional[int] = Field(default=None, alias="maxDuration")
    max_runs: Optional[int] = Field(default=None, alias="maxRuns")
    name: Optional[str] = Field(default=None, alias="name")


class UpdateVariantStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateWorkflowRequestModel(BaseModel):
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")


class ListReadSetActivationJobsRequestModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ActivateReadSetFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class AnnotationStoreItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    store_arn: str = Field(alias="storeArn")
    store_format: Literal["GFF", "TSV", "VCF"] = Field(alias="storeFormat")
    store_size_bytes: int = Field(alias="storeSizeBytes")
    update_time: datetime = Field(alias="updateTime")


class CreateReferenceStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateSequenceStoreRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateVariantStoreRequestModel(BaseModel):
    reference: ReferenceItemModel = Field(alias="reference")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ReferenceStoreDetailModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")


class SequenceStoreDetailModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")


class VariantStoreItemModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    store_arn: str = Field(alias="storeArn")
    store_size_bytes: int = Field(alias="storeSizeBytes")
    update_time: datetime = Field(alias="updateTime")


class BatchDeleteReadSetResponseModel(BaseModel):
    errors: List[ReadSetBatchErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReferenceStoreResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRunGroupResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSequenceStoreResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVariantStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    status: Literal[
        "ACTIVE", "CREATING", "DELETED", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAnnotationStoreResponseModel(BaseModel):
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVariantStoreResponseModel(BaseModel):
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadSetActivationJobResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    sources: List[ActivateReadSetSourceItemModel] = Field(alias="sources")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadSetResponseModel(BaseModel):
    payload: Type[StreamingBody] = Field(alias="payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReferenceResponseModel(BaseModel):
    payload: Type[StreamingBody] = Field(alias="payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReferenceStoreResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRunGroupResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    max_cpus: int = Field(alias="maxCpus")
    max_duration: int = Field(alias="maxDuration")
    max_runs: int = Field(alias="maxRuns")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRunResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    definition: str = Field(alias="definition")
    digest: str = Field(alias="digest")
    id: str = Field(alias="id")
    log_level: Literal["ALL", "ERROR", "FATAL", "OFF"] = Field(alias="logLevel")
    name: str = Field(alias="name")
    output_uri: str = Field(alias="outputUri")
    parameters: Dict[str, Any] = Field(alias="parameters")
    priority: int = Field(alias="priority")
    resource_digests: Dict[str, str] = Field(alias="resourceDigests")
    role_arn: str = Field(alias="roleArn")
    run_group_id: str = Field(alias="runGroupId")
    run_id: str = Field(alias="runId")
    start_time: datetime = Field(alias="startTime")
    started_by: str = Field(alias="startedBy")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "DELETED",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    stop_time: datetime = Field(alias="stopTime")
    storage_capacity: int = Field(alias="storageCapacity")
    tags: Dict[str, str] = Field(alias="tags")
    workflow_id: str = Field(alias="workflowId")
    workflow_type: Literal["PRIVATE", "SERVICE"] = Field(alias="workflowType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRunTaskResponseModel(BaseModel):
    cpus: int = Field(alias="cpus")
    creation_time: datetime = Field(alias="creationTime")
    log_stream: str = Field(alias="logStream")
    memory: int = Field(alias="memory")
    name: str = Field(alias="name")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    stop_time: datetime = Field(alias="stopTime")
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSequenceStoreResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVariantStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    store_arn: str = Field(alias="storeArn")
    store_size_bytes: int = Field(alias="storeSizeBytes")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnnotationImportJobsResponseModel(BaseModel):
    annotation_import_jobs: List[AnnotationImportJobItemModel] = Field(
        alias="annotationImportJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReadSetActivationJobsResponseModel(BaseModel):
    activation_jobs: List[ActivateReadSetJobItemModel] = Field(alias="activationJobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAnnotationImportResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReadSetActivationJobResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReadSetExportJobResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    destination: str = Field(alias="destination")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReadSetImportJobResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    role_arn: str = Field(alias="roleArn")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReferenceImportJobResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")
    role_arn: str = Field(alias="roleArn")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRunResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "DELETED",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPING",
    ] = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartVariantImportResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVariantStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    definition_uri: Optional[str] = Field(default=None, alias="definitionUri")
    definition_zip: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="definitionZip")
    description: Optional[str] = Field(default=None, alias="description")
    engine: Optional[Literal["NEXTFLOW", "WDL"]] = Field(default=None, alias="engine")
    main: Optional[str] = Field(default=None, alias="main")
    name: Optional[str] = Field(default=None, alias="name")
    parameter_template: Optional[Mapping[str, WorkflowParameterModel]] = Field(
        default=None, alias="parameterTemplate"
    )
    storage_capacity: Optional[int] = Field(default=None, alias="storageCapacity")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetWorkflowResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    definition: str = Field(alias="definition")
    description: str = Field(alias="description")
    digest: str = Field(alias="digest")
    engine: Literal["NEXTFLOW", "WDL"] = Field(alias="engine")
    id: str = Field(alias="id")
    main: str = Field(alias="main")
    name: str = Field(alias="name")
    parameter_template: Dict[str, WorkflowParameterModel] = Field(
        alias="parameterTemplate"
    )
    status: Literal[
        "ACTIVE", "CREATING", "DELETED", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    storage_capacity: int = Field(alias="storageCapacity")
    tags: Dict[str, str] = Field(alias="tags")
    type: Literal["PRIVATE", "SERVICE"] = Field(alias="type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadSetExportJobResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    destination: str = Field(alias="destination")
    id: str = Field(alias="id")
    read_sets: List[ExportReadSetDetailModel] = Field(alias="readSets")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReadSetExportJobsRequestModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ExportReadSetFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReadSetExportJobsResponseModel(BaseModel):
    export_jobs: List[ExportReadSetJobDetailModel] = Field(alias="exportJobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReadSetExportJobRequestModel(BaseModel):
    destination: str = Field(alias="destination")
    role_arn: str = Field(alias="roleArn")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    sources: Sequence[ExportReadSetModel] = Field(alias="sources")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ReadSetFilesModel(BaseModel):
    index: Optional[FileInformationModel] = Field(default=None, alias="index")
    source1: Optional[FileInformationModel] = Field(default=None, alias="source1")
    source2: Optional[FileInformationModel] = Field(default=None, alias="source2")


class ReferenceFilesModel(BaseModel):
    index: Optional[FileInformationModel] = Field(default=None, alias="index")
    source: Optional[FileInformationModel] = Field(default=None, alias="source")


class GetAnnotationImportRequestAnnotationImportJobCreatedWaitModel(BaseModel):
    job_id: str = Field(alias="jobId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetAnnotationStoreRequestAnnotationStoreCreatedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetAnnotationStoreRequestAnnotationStoreDeletedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetReadSetExportJobRequestReadSetExportJobCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetReadSetImportJobRequestReadSetImportJobCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetReferenceImportJobRequestReferenceImportJobCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetRunRequestRunCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    export: Optional[Sequence[Literal["DEFINITION"]]] = Field(
        default=None, alias="export"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetRunRequestRunRunningWaitModel(BaseModel):
    id: str = Field(alias="id")
    export: Optional[Sequence[Literal["DEFINITION"]]] = Field(
        default=None, alias="export"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetRunTaskRequestTaskCompletedWaitModel(BaseModel):
    id: str = Field(alias="id")
    task_id: str = Field(alias="taskId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetRunTaskRequestTaskRunningWaitModel(BaseModel):
    id: str = Field(alias="id")
    task_id: str = Field(alias="taskId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetVariantImportRequestVariantImportJobCreatedWaitModel(BaseModel):
    job_id: str = Field(alias="jobId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetVariantStoreRequestVariantStoreCreatedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetVariantStoreRequestVariantStoreDeletedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetWorkflowRequestWorkflowActiveWaitModel(BaseModel):
    id: str = Field(alias="id")
    export: Optional[Sequence[Literal["DEFINITION"]]] = Field(
        default=None, alias="export"
    )
    type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(default=None, alias="type")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ReadSetListItemModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    file_type: Literal["BAM", "CRAM", "FASTQ"] = Field(alias="fileType")
    id: str = Field(alias="id")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal["ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING"] = Field(
        alias="status"
    )
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    reference_arn: Optional[str] = Field(default=None, alias="referenceArn")
    sample_id: Optional[str] = Field(default=None, alias="sampleId")
    sequence_information: Optional[SequenceInformationModel] = Field(
        default=None, alias="sequenceInformation"
    )
    subject_id: Optional[str] = Field(default=None, alias="subjectId")


class GetReferenceImportJobResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    reference_store_id: str = Field(alias="referenceStoreId")
    role_arn: str = Field(alias="roleArn")
    sources: List[ImportReferenceSourceItemModel] = Field(alias="sources")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVariantImportResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    destination_name: str = Field(alias="destinationName")
    id: str = Field(alias="id")
    items: List[VariantImportItemDetailModel] = Field(alias="items")
    role_arn: str = Field(alias="roleArn")
    run_left_normalization: bool = Field(alias="runLeftNormalization")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReadSetImportJobsRequestModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ImportReadSetFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReadSetImportJobsResponseModel(BaseModel):
    import_jobs: List[ImportReadSetJobItemModel] = Field(alias="importJobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportReadSetSourceItemModel(BaseModel):
    sample_id: str = Field(alias="sampleId")
    source_file_type: Literal["BAM", "CRAM", "FASTQ"] = Field(alias="sourceFileType")
    source_files: SourceFilesModel = Field(alias="sourceFiles")
    status: Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="status"
    )
    subject_id: str = Field(alias="subjectId")
    description: Optional[str] = Field(default=None, alias="description")
    generated_from: Optional[str] = Field(default=None, alias="generatedFrom")
    name: Optional[str] = Field(default=None, alias="name")
    reference_arn: Optional[str] = Field(default=None, alias="referenceArn")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class StartReadSetImportJobSourceItemModel(BaseModel):
    reference_arn: str = Field(alias="referenceArn")
    sample_id: str = Field(alias="sampleId")
    source_file_type: Literal["BAM", "CRAM", "FASTQ"] = Field(alias="sourceFileType")
    source_files: SourceFilesModel = Field(alias="sourceFiles")
    subject_id: str = Field(alias="subjectId")
    description: Optional[str] = Field(default=None, alias="description")
    generated_from: Optional[str] = Field(default=None, alias="generatedFrom")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ListReferenceImportJobsRequestModel(BaseModel):
    reference_store_id: str = Field(alias="referenceStoreId")
    filter: Optional[ImportReferenceFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReferenceImportJobsResponseModel(BaseModel):
    import_jobs: List[ImportReferenceJobItemModel] = Field(alias="importJobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnnotationImportJobsRequestModel(BaseModel):
    filter: Optional[ListAnnotationImportJobsFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateModel(BaseModel):
    filter: Optional[ListAnnotationImportJobsFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ActivateReadSetFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReadSetExportJobsRequestListReadSetExportJobsPaginateModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ExportReadSetFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReadSetImportJobsRequestListReadSetImportJobsPaginateModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ImportReadSetFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReferenceImportJobsRequestListReferenceImportJobsPaginateModel(BaseModel):
    reference_store_id: str = Field(alias="referenceStoreId")
    filter: Optional[ImportReferenceFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRunGroupsRequestListRunGroupsPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRunTasksRequestListRunTasksPaginateModel(BaseModel):
    id: str = Field(alias="id")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PENDING",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRunsRequestListRunsPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    run_group_id: Optional[str] = Field(default=None, alias="runGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkflowsRequestListWorkflowsPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["PRIVATE", "SERVICE"]] = Field(default=None, alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnnotationStoresRequestListAnnotationStoresPaginateModel(BaseModel):
    filter: Optional[ListAnnotationStoresFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnnotationStoresRequestModel(BaseModel):
    filter: Optional[ListAnnotationStoresFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReadSetsRequestListReadSetsPaginateModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ReadSetFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReadSetsRequestModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    filter: Optional[ReadSetFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReferenceStoresRequestListReferenceStoresPaginateModel(BaseModel):
    filter: Optional[ReferenceStoreFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReferenceStoresRequestModel(BaseModel):
    filter: Optional[ReferenceStoreFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReferencesRequestListReferencesPaginateModel(BaseModel):
    reference_store_id: str = Field(alias="referenceStoreId")
    filter: Optional[ReferenceFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReferencesRequestModel(BaseModel):
    reference_store_id: str = Field(alias="referenceStoreId")
    filter: Optional[ReferenceFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReferencesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    references: List[ReferenceListItemModel] = Field(alias="references")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRunGroupsResponseModel(BaseModel):
    items: List[RunGroupListItemModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRunTasksResponseModel(BaseModel):
    items: List[TaskListItemModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRunsResponseModel(BaseModel):
    items: List[RunListItemModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSequenceStoresRequestListSequenceStoresPaginateModel(BaseModel):
    filter: Optional[SequenceStoreFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSequenceStoresRequestModel(BaseModel):
    filter: Optional[SequenceStoreFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListVariantImportJobsRequestListVariantImportJobsPaginateModel(BaseModel):
    filter: Optional[ListVariantImportJobsFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVariantImportJobsRequestModel(BaseModel):
    filter: Optional[ListVariantImportJobsFilterModel] = Field(
        default=None, alias="filter"
    )
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListVariantImportJobsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    variant_import_jobs: List[VariantImportJobItemModel] = Field(
        alias="variantImportJobs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVariantStoresRequestListVariantStoresPaginateModel(BaseModel):
    filter: Optional[ListVariantStoresFilterModel] = Field(default=None, alias="filter")
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVariantStoresRequestModel(BaseModel):
    filter: Optional[ListVariantStoresFilterModel] = Field(default=None, alias="filter")
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListWorkflowsResponseModel(BaseModel):
    items: List[WorkflowListItemModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TsvOptionsModel(BaseModel):
    read_options: Optional[ReadOptionsModel] = Field(default=None, alias="readOptions")


class StartReadSetActivationJobRequestModel(BaseModel):
    sequence_store_id: str = Field(alias="sequenceStoreId")
    sources: Sequence[StartReadSetActivationJobSourceItemModel] = Field(alias="sources")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StartReferenceImportJobRequestModel(BaseModel):
    reference_store_id: str = Field(alias="referenceStoreId")
    role_arn: str = Field(alias="roleArn")
    sources: Sequence[StartReferenceImportJobSourceItemModel] = Field(alias="sources")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StartVariantImportRequestModel(BaseModel):
    destination_name: str = Field(alias="destinationName")
    items: Sequence[VariantImportItemSourceModel] = Field(alias="items")
    role_arn: str = Field(alias="roleArn")
    run_left_normalization: Optional[bool] = Field(
        default=None, alias="runLeftNormalization"
    )


class StoreOptionsModel(BaseModel):
    tsv_store_options: Optional[TsvStoreOptionsModel] = Field(
        default=None, alias="tsvStoreOptions"
    )


class ListAnnotationStoresResponseModel(BaseModel):
    annotation_stores: List[AnnotationStoreItemModel] = Field(alias="annotationStores")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReferenceStoresResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    reference_stores: List[ReferenceStoreDetailModel] = Field(alias="referenceStores")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSequenceStoresResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sequence_stores: List[SequenceStoreDetailModel] = Field(alias="sequenceStores")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVariantStoresResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    variant_stores: List[VariantStoreItemModel] = Field(alias="variantStores")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadSetMetadataResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    file_type: Literal["BAM", "CRAM", "FASTQ"] = Field(alias="fileType")
    files: ReadSetFilesModel = Field(alias="files")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference_arn: str = Field(alias="referenceArn")
    sample_id: str = Field(alias="sampleId")
    sequence_information: SequenceInformationModel = Field(alias="sequenceInformation")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    status: Literal["ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING"] = Field(
        alias="status"
    )
    subject_id: str = Field(alias="subjectId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReferenceMetadataResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    files: ReferenceFilesModel = Field(alias="files")
    id: str = Field(alias="id")
    md5: str = Field(alias="md5")
    name: str = Field(alias="name")
    reference_store_id: str = Field(alias="referenceStoreId")
    status: Literal["ACTIVE", "DELETED", "DELETING"] = Field(alias="status")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReadSetsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    read_sets: List[ReadSetListItemModel] = Field(alias="readSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadSetImportJobResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    role_arn: str = Field(alias="roleArn")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    sources: List[ImportReadSetSourceItemModel] = Field(alias="sources")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReadSetImportJobRequestModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    sequence_store_id: str = Field(alias="sequenceStoreId")
    sources: Sequence[StartReadSetImportJobSourceItemModel] = Field(alias="sources")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class FormatOptionsModel(BaseModel):
    tsv_options: Optional[TsvOptionsModel] = Field(default=None, alias="tsvOptions")
    vcf_options: Optional[VcfOptionsModel] = Field(default=None, alias="vcfOptions")


class CreateAnnotationStoreRequestModel(BaseModel):
    store_format: Literal["GFF", "TSV", "VCF"] = Field(alias="storeFormat")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    reference: Optional[ReferenceItemModel] = Field(default=None, alias="reference")
    sse_config: Optional[SseConfigModel] = Field(default=None, alias="sseConfig")
    store_options: Optional[StoreOptionsModel] = Field(
        default=None, alias="storeOptions"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateAnnotationStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    store_format: Literal["GFF", "TSV", "VCF"] = Field(alias="storeFormat")
    store_options: StoreOptionsModel = Field(alias="storeOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnnotationStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    sse_config: SseConfigModel = Field(alias="sseConfig")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    store_arn: str = Field(alias="storeArn")
    store_format: Literal["GFF", "TSV", "VCF"] = Field(alias="storeFormat")
    store_options: StoreOptionsModel = Field(alias="storeOptions")
    store_size_bytes: int = Field(alias="storeSizeBytes")
    tags: Dict[str, str] = Field(alias="tags")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnnotationStoreResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    reference: ReferenceItemModel = Field(alias="reference")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    store_format: Literal["GFF", "TSV", "VCF"] = Field(alias="storeFormat")
    store_options: StoreOptionsModel = Field(alias="storeOptions")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnnotationImportResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    creation_time: datetime = Field(alias="creationTime")
    destination_name: str = Field(alias="destinationName")
    format_options: FormatOptionsModel = Field(alias="formatOptions")
    id: str = Field(alias="id")
    items: List[AnnotationImportItemDetailModel] = Field(alias="items")
    role_arn: str = Field(alias="roleArn")
    run_left_normalization: bool = Field(alias="runLeftNormalization")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "IN_PROGRESS",
        "SUBMITTED",
    ] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    update_time: datetime = Field(alias="updateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAnnotationImportRequestModel(BaseModel):
    destination_name: str = Field(alias="destinationName")
    items: Sequence[AnnotationImportItemSourceModel] = Field(alias="items")
    role_arn: str = Field(alias="roleArn")
    format_options: Optional[FormatOptionsModel] = Field(
        default=None, alias="formatOptions"
    )
    run_left_normalization: Optional[bool] = Field(
        default=None, alias="runLeftNormalization"
    )
