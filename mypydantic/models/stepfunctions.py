# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActivityFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class ActivityListItemModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")
    name: str = Field(alias="name")
    creation_date: datetime = Field(alias="creationDate")


class ActivityScheduleFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class HistoryEventExecutionDataDetailsModel(BaseModel):
    truncated: Optional[bool] = Field(default=None, alias="truncated")


class ActivityStartedEventDetailsModel(BaseModel):
    worker_name: Optional[str] = Field(default=None, alias="workerName")


class ActivityTimedOutEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class BillingDetailsModel(BaseModel):
    billed_memory_used_in_mb: Optional[int] = Field(
        default=None, alias="billedMemoryUsedInMB"
    )
    billed_duration_in_milliseconds: Optional[int] = Field(
        default=None, alias="billedDurationInMilliseconds"
    )


class CloudWatchEventsExecutionDataDetailsModel(BaseModel):
    included: Optional[bool] = Field(default=None, alias="included")


class CloudWatchLogsLogGroupModel(BaseModel):
    log_group_arn: Optional[str] = Field(default=None, alias="logGroupArn")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TracingConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class DeleteActivityInputRequestModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")


class DeleteStateMachineInputRequestModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")


class DescribeActivityInputRequestModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")


class DescribeExecutionInputRequestModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")


class DescribeMapRunInputRequestModel(BaseModel):
    map_run_arn: str = Field(alias="mapRunArn")


class MapRunExecutionCountsModel(BaseModel):
    pending: int = Field(alias="pending")
    running: int = Field(alias="running")
    succeeded: int = Field(alias="succeeded")
    failed: int = Field(alias="failed")
    timed_out: int = Field(alias="timedOut")
    aborted: int = Field(alias="aborted")
    total: int = Field(alias="total")
    results_written: int = Field(alias="resultsWritten")


class MapRunItemCountsModel(BaseModel):
    pending: int = Field(alias="pending")
    running: int = Field(alias="running")
    succeeded: int = Field(alias="succeeded")
    failed: int = Field(alias="failed")
    timed_out: int = Field(alias="timedOut")
    aborted: int = Field(alias="aborted")
    total: int = Field(alias="total")
    results_written: int = Field(alias="resultsWritten")


class DescribeStateMachineForExecutionInputRequestModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")


class DescribeStateMachineInputRequestModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")


class ExecutionAbortedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class ExecutionFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class ExecutionListItemModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    status: Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"] = Field(
        alias="status"
    )
    start_date: datetime = Field(alias="startDate")
    stop_date: Optional[datetime] = Field(default=None, alias="stopDate")
    map_run_arn: Optional[str] = Field(default=None, alias="mapRunArn")
    item_count: Optional[int] = Field(default=None, alias="itemCount")


class ExecutionTimedOutEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class GetActivityTaskInputRequestModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")
    worker_name: Optional[str] = Field(default=None, alias="workerName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetExecutionHistoryInputRequestModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    include_execution_data: Optional[bool] = Field(
        default=None, alias="includeExecutionData"
    )


class LambdaFunctionFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class LambdaFunctionScheduleFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class LambdaFunctionStartFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class LambdaFunctionTimedOutEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class MapIterationEventDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    index: Optional[int] = Field(default=None, alias="index")


class MapRunFailedEventDetailsModel(BaseModel):
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class MapRunStartedEventDetailsModel(BaseModel):
    map_run_arn: Optional[str] = Field(default=None, alias="mapRunArn")


class MapStateStartedEventDetailsModel(BaseModel):
    length: Optional[int] = Field(default=None, alias="length")


class TaskFailedEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class TaskStartFailedEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class TaskStartedEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")


class TaskSubmitFailedEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class TaskTimedOutEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class TaskCredentialsModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class ListActivitiesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListExecutionsInputRequestModel(BaseModel):
    state_machine_arn: Optional[str] = Field(default=None, alias="stateMachineArn")
    status_filter: Optional[
        Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="statusFilter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    map_run_arn: Optional[str] = Field(default=None, alias="mapRunArn")


class ListMapRunsInputRequestModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MapRunListItemModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    map_run_arn: str = Field(alias="mapRunArn")
    state_machine_arn: str = Field(alias="stateMachineArn")
    start_date: datetime = Field(alias="startDate")
    stop_date: Optional[datetime] = Field(default=None, alias="stopDate")


class ListStateMachinesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StateMachineListItemModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    type: Literal["EXPRESS", "STANDARD"] = Field(alias="type")
    creation_date: datetime = Field(alias="creationDate")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class SendTaskFailureInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class SendTaskHeartbeatInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")


class SendTaskSuccessInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    output: str = Field(alias="output")


class StartExecutionInputRequestModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: Optional[str] = Field(default=None, alias="name")
    input: Optional[str] = Field(default=None, alias="input")
    trace_header: Optional[str] = Field(default=None, alias="traceHeader")


class StartSyncExecutionInputRequestModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: Optional[str] = Field(default=None, alias="name")
    input: Optional[str] = Field(default=None, alias="input")
    trace_header: Optional[str] = Field(default=None, alias="traceHeader")


class StopExecutionInputRequestModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    error: Optional[str] = Field(default=None, alias="error")
    cause: Optional[str] = Field(default=None, alias="cause")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateMapRunInputRequestModel(BaseModel):
    map_run_arn: str = Field(alias="mapRunArn")
    max_concurrency: Optional[int] = Field(default=None, alias="maxConcurrency")
    tolerated_failure_percentage: Optional[float] = Field(
        default=None, alias="toleratedFailurePercentage"
    )
    tolerated_failure_count: Optional[int] = Field(
        default=None, alias="toleratedFailureCount"
    )


class ActivityScheduledEventDetailsModel(BaseModel):
    resource: str = Field(alias="resource")
    input: Optional[str] = Field(default=None, alias="input")
    input_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="inputDetails"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    heartbeat_in_seconds: Optional[int] = Field(
        default=None, alias="heartbeatInSeconds"
    )


class ActivitySucceededEventDetailsModel(BaseModel):
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class ExecutionStartedEventDetailsModel(BaseModel):
    input: Optional[str] = Field(default=None, alias="input")
    input_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="inputDetails"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class ExecutionSucceededEventDetailsModel(BaseModel):
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class LambdaFunctionSucceededEventDetailsModel(BaseModel):
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class StateEnteredEventDetailsModel(BaseModel):
    name: str = Field(alias="name")
    input: Optional[str] = Field(default=None, alias="input")
    input_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="inputDetails"
    )


class StateExitedEventDetailsModel(BaseModel):
    name: str = Field(alias="name")
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class TaskSubmittedEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class TaskSucceededEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    output: Optional[str] = Field(default=None, alias="output")
    output_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="outputDetails"
    )


class LogDestinationModel(BaseModel):
    cloud_watch_logs_log_group: Optional[CloudWatchLogsLogGroupModel] = Field(
        default=None, alias="cloudWatchLogsLogGroup"
    )


class CreateActivityInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateActivityOutputModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")
    creation_date: datetime = Field(alias="creationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStateMachineOutputModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    creation_date: datetime = Field(alias="creationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeActivityOutputModel(BaseModel):
    activity_arn: str = Field(alias="activityArn")
    name: str = Field(alias="name")
    creation_date: datetime = Field(alias="creationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExecutionOutputModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    status: Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"] = Field(
        alias="status"
    )
    start_date: datetime = Field(alias="startDate")
    stop_date: datetime = Field(alias="stopDate")
    input: str = Field(alias="input")
    input_details: CloudWatchEventsExecutionDataDetailsModel = Field(
        alias="inputDetails"
    )
    output: str = Field(alias="output")
    output_details: CloudWatchEventsExecutionDataDetailsModel = Field(
        alias="outputDetails"
    )
    trace_header: str = Field(alias="traceHeader")
    map_run_arn: str = Field(alias="mapRunArn")
    error: str = Field(alias="error")
    cause: str = Field(alias="cause")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetActivityTaskOutputModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    input: str = Field(alias="input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListActivitiesOutputModel(BaseModel):
    activities: List[ActivityListItemModel] = Field(alias="activities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExecutionOutputModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    start_date: datetime = Field(alias="startDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSyncExecutionOutputModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    start_date: datetime = Field(alias="startDate")
    stop_date: datetime = Field(alias="stopDate")
    status: Literal["FAILED", "SUCCEEDED", "TIMED_OUT"] = Field(alias="status")
    error: str = Field(alias="error")
    cause: str = Field(alias="cause")
    input: str = Field(alias="input")
    input_details: CloudWatchEventsExecutionDataDetailsModel = Field(
        alias="inputDetails"
    )
    output: str = Field(alias="output")
    output_details: CloudWatchEventsExecutionDataDetailsModel = Field(
        alias="outputDetails"
    )
    trace_header: str = Field(alias="traceHeader")
    billing_details: BillingDetailsModel = Field(alias="billingDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopExecutionOutputModel(BaseModel):
    stop_date: datetime = Field(alias="stopDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStateMachineOutputModel(BaseModel):
    update_date: datetime = Field(alias="updateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMapRunOutputModel(BaseModel):
    map_run_arn: str = Field(alias="mapRunArn")
    execution_arn: str = Field(alias="executionArn")
    status: Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED"] = Field(alias="status")
    start_date: datetime = Field(alias="startDate")
    stop_date: datetime = Field(alias="stopDate")
    max_concurrency: int = Field(alias="maxConcurrency")
    tolerated_failure_percentage: float = Field(alias="toleratedFailurePercentage")
    tolerated_failure_count: int = Field(alias="toleratedFailureCount")
    item_counts: MapRunItemCountsModel = Field(alias="itemCounts")
    execution_counts: MapRunExecutionCountsModel = Field(alias="executionCounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExecutionsOutputModel(BaseModel):
    executions: List[ExecutionListItemModel] = Field(alias="executions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExecutionHistoryInputGetExecutionHistoryPaginateModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    include_execution_data: Optional[bool] = Field(
        default=None, alias="includeExecutionData"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListActivitiesInputListActivitiesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExecutionsInputListExecutionsPaginateModel(BaseModel):
    state_machine_arn: Optional[str] = Field(default=None, alias="stateMachineArn")
    status_filter: Optional[
        Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"]
    ] = Field(default=None, alias="statusFilter")
    map_run_arn: Optional[str] = Field(default=None, alias="mapRunArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMapRunsInputListMapRunsPaginateModel(BaseModel):
    execution_arn: str = Field(alias="executionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStateMachinesInputListStateMachinesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LambdaFunctionScheduledEventDetailsModel(BaseModel):
    resource: str = Field(alias="resource")
    input: Optional[str] = Field(default=None, alias="input")
    input_details: Optional[HistoryEventExecutionDataDetailsModel] = Field(
        default=None, alias="inputDetails"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    task_credentials: Optional[TaskCredentialsModel] = Field(
        default=None, alias="taskCredentials"
    )


class TaskScheduledEventDetailsModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    resource: str = Field(alias="resource")
    region: str = Field(alias="region")
    parameters: str = Field(alias="parameters")
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    heartbeat_in_seconds: Optional[int] = Field(
        default=None, alias="heartbeatInSeconds"
    )
    task_credentials: Optional[TaskCredentialsModel] = Field(
        default=None, alias="taskCredentials"
    )


class ListMapRunsOutputModel(BaseModel):
    map_runs: List[MapRunListItemModel] = Field(alias="mapRuns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStateMachinesOutputModel(BaseModel):
    state_machines: List[StateMachineListItemModel] = Field(alias="stateMachines")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingConfigurationModel(BaseModel):
    level: Optional[Literal["ALL", "ERROR", "FATAL", "OFF"]] = Field(
        default=None, alias="level"
    )
    include_execution_data: Optional[bool] = Field(
        default=None, alias="includeExecutionData"
    )
    destinations: Optional[Sequence[LogDestinationModel]] = Field(
        default=None, alias="destinations"
    )


class HistoryEventModel(BaseModel):
    timestamp: datetime = Field(alias="timestamp")
    type: Literal[
        "ActivityFailed",
        "ActivityScheduleFailed",
        "ActivityScheduled",
        "ActivityStarted",
        "ActivitySucceeded",
        "ActivityTimedOut",
        "ChoiceStateEntered",
        "ChoiceStateExited",
        "ExecutionAborted",
        "ExecutionFailed",
        "ExecutionStarted",
        "ExecutionSucceeded",
        "ExecutionTimedOut",
        "FailStateEntered",
        "LambdaFunctionFailed",
        "LambdaFunctionScheduleFailed",
        "LambdaFunctionScheduled",
        "LambdaFunctionStartFailed",
        "LambdaFunctionStarted",
        "LambdaFunctionSucceeded",
        "LambdaFunctionTimedOut",
        "MapIterationAborted",
        "MapIterationFailed",
        "MapIterationStarted",
        "MapIterationSucceeded",
        "MapRunAborted",
        "MapRunFailed",
        "MapRunStarted",
        "MapRunSucceeded",
        "MapStateAborted",
        "MapStateEntered",
        "MapStateExited",
        "MapStateFailed",
        "MapStateStarted",
        "MapStateSucceeded",
        "ParallelStateAborted",
        "ParallelStateEntered",
        "ParallelStateExited",
        "ParallelStateFailed",
        "ParallelStateStarted",
        "ParallelStateSucceeded",
        "PassStateEntered",
        "PassStateExited",
        "SucceedStateEntered",
        "SucceedStateExited",
        "TaskFailed",
        "TaskScheduled",
        "TaskStartFailed",
        "TaskStarted",
        "TaskStateAborted",
        "TaskStateEntered",
        "TaskStateExited",
        "TaskSubmitFailed",
        "TaskSubmitted",
        "TaskSucceeded",
        "TaskTimedOut",
        "WaitStateAborted",
        "WaitStateEntered",
        "WaitStateExited",
    ] = Field(alias="type")
    id: int = Field(alias="id")
    previous_event_id: Optional[int] = Field(default=None, alias="previousEventId")
    activity_failed_event_details: Optional[ActivityFailedEventDetailsModel] = Field(
        default=None, alias="activityFailedEventDetails"
    )
    activity_schedule_failed_event_details: Optional[
        ActivityScheduleFailedEventDetailsModel
    ] = Field(default=None, alias="activityScheduleFailedEventDetails")
    activity_scheduled_event_details: Optional[
        ActivityScheduledEventDetailsModel
    ] = Field(default=None, alias="activityScheduledEventDetails")
    activity_started_event_details: Optional[ActivityStartedEventDetailsModel] = Field(
        default=None, alias="activityStartedEventDetails"
    )
    activity_succeeded_event_details: Optional[
        ActivitySucceededEventDetailsModel
    ] = Field(default=None, alias="activitySucceededEventDetails")
    activity_timed_out_event_details: Optional[
        ActivityTimedOutEventDetailsModel
    ] = Field(default=None, alias="activityTimedOutEventDetails")
    task_failed_event_details: Optional[TaskFailedEventDetailsModel] = Field(
        default=None, alias="taskFailedEventDetails"
    )
    task_scheduled_event_details: Optional[TaskScheduledEventDetailsModel] = Field(
        default=None, alias="taskScheduledEventDetails"
    )
    task_start_failed_event_details: Optional[TaskStartFailedEventDetailsModel] = Field(
        default=None, alias="taskStartFailedEventDetails"
    )
    task_started_event_details: Optional[TaskStartedEventDetailsModel] = Field(
        default=None, alias="taskStartedEventDetails"
    )
    task_submit_failed_event_details: Optional[
        TaskSubmitFailedEventDetailsModel
    ] = Field(default=None, alias="taskSubmitFailedEventDetails")
    task_submitted_event_details: Optional[TaskSubmittedEventDetailsModel] = Field(
        default=None, alias="taskSubmittedEventDetails"
    )
    task_succeeded_event_details: Optional[TaskSucceededEventDetailsModel] = Field(
        default=None, alias="taskSucceededEventDetails"
    )
    task_timed_out_event_details: Optional[TaskTimedOutEventDetailsModel] = Field(
        default=None, alias="taskTimedOutEventDetails"
    )
    execution_failed_event_details: Optional[ExecutionFailedEventDetailsModel] = Field(
        default=None, alias="executionFailedEventDetails"
    )
    execution_started_event_details: Optional[
        ExecutionStartedEventDetailsModel
    ] = Field(default=None, alias="executionStartedEventDetails")
    execution_succeeded_event_details: Optional[
        ExecutionSucceededEventDetailsModel
    ] = Field(default=None, alias="executionSucceededEventDetails")
    execution_aborted_event_details: Optional[
        ExecutionAbortedEventDetailsModel
    ] = Field(default=None, alias="executionAbortedEventDetails")
    execution_timed_out_event_details: Optional[
        ExecutionTimedOutEventDetailsModel
    ] = Field(default=None, alias="executionTimedOutEventDetails")
    map_state_started_event_details: Optional[MapStateStartedEventDetailsModel] = Field(
        default=None, alias="mapStateStartedEventDetails"
    )
    map_iteration_started_event_details: Optional[
        MapIterationEventDetailsModel
    ] = Field(default=None, alias="mapIterationStartedEventDetails")
    map_iteration_succeeded_event_details: Optional[
        MapIterationEventDetailsModel
    ] = Field(default=None, alias="mapIterationSucceededEventDetails")
    map_iteration_failed_event_details: Optional[MapIterationEventDetailsModel] = Field(
        default=None, alias="mapIterationFailedEventDetails"
    )
    map_iteration_aborted_event_details: Optional[
        MapIterationEventDetailsModel
    ] = Field(default=None, alias="mapIterationAbortedEventDetails")
    lambda_function_failed_event_details: Optional[
        LambdaFunctionFailedEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionFailedEventDetails")
    lambda_function_schedule_failed_event_details: Optional[
        LambdaFunctionScheduleFailedEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionScheduleFailedEventDetails")
    lambda_function_scheduled_event_details: Optional[
        LambdaFunctionScheduledEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionScheduledEventDetails")
    lambda_function_start_failed_event_details: Optional[
        LambdaFunctionStartFailedEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionStartFailedEventDetails")
    lambda_function_succeeded_event_details: Optional[
        LambdaFunctionSucceededEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionSucceededEventDetails")
    lambda_function_timed_out_event_details: Optional[
        LambdaFunctionTimedOutEventDetailsModel
    ] = Field(default=None, alias="lambdaFunctionTimedOutEventDetails")
    state_entered_event_details: Optional[StateEnteredEventDetailsModel] = Field(
        default=None, alias="stateEnteredEventDetails"
    )
    state_exited_event_details: Optional[StateExitedEventDetailsModel] = Field(
        default=None, alias="stateExitedEventDetails"
    )
    map_run_started_event_details: Optional[MapRunStartedEventDetailsModel] = Field(
        default=None, alias="mapRunStartedEventDetails"
    )
    map_run_failed_event_details: Optional[MapRunFailedEventDetailsModel] = Field(
        default=None, alias="mapRunFailedEventDetails"
    )


class CreateStateMachineInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    definition: str = Field(alias="definition")
    role_arn: str = Field(alias="roleArn")
    type: Optional[Literal["EXPRESS", "STANDARD"]] = Field(default=None, alias="type")
    logging_configuration: Optional[LoggingConfigurationModel] = Field(
        default=None, alias="loggingConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    tracing_configuration: Optional[TracingConfigurationModel] = Field(
        default=None, alias="tracingConfiguration"
    )


class DescribeStateMachineForExecutionOutputModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    definition: str = Field(alias="definition")
    role_arn: str = Field(alias="roleArn")
    update_date: datetime = Field(alias="updateDate")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="loggingConfiguration"
    )
    tracing_configuration: TracingConfigurationModel = Field(
        alias="tracingConfiguration"
    )
    map_run_arn: str = Field(alias="mapRunArn")
    label: str = Field(alias="label")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStateMachineOutputModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    name: str = Field(alias="name")
    status: Literal["ACTIVE", "DELETING"] = Field(alias="status")
    definition: str = Field(alias="definition")
    role_arn: str = Field(alias="roleArn")
    type: Literal["EXPRESS", "STANDARD"] = Field(alias="type")
    creation_date: datetime = Field(alias="creationDate")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="loggingConfiguration"
    )
    tracing_configuration: TracingConfigurationModel = Field(
        alias="tracingConfiguration"
    )
    label: str = Field(alias="label")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStateMachineInputRequestModel(BaseModel):
    state_machine_arn: str = Field(alias="stateMachineArn")
    definition: Optional[str] = Field(default=None, alias="definition")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    logging_configuration: Optional[LoggingConfigurationModel] = Field(
        default=None, alias="loggingConfiguration"
    )
    tracing_configuration: Optional[TracingConfigurationModel] = Field(
        default=None, alias="tracingConfiguration"
    )


class GetExecutionHistoryOutputModel(BaseModel):
    events: List[HistoryEventModel] = Field(alias="events")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
