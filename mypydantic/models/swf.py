# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActivityTaskCancelRequestedEventAttributesModel(BaseModel):
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    activity_id: str = Field(alias="activityId")


class ActivityTaskCanceledEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    details: Optional[str] = Field(default=None, alias="details")
    latest_cancel_requested_event_id: Optional[int] = Field(
        default=None, alias="latestCancelRequestedEventId"
    )


class ActivityTaskCompletedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    result: Optional[str] = Field(default=None, alias="result")


class ActivityTaskFailedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class ActivityTypeModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class TaskListModel(BaseModel):
    name: str = Field(alias="name")


class ActivityTaskStartedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    identity: Optional[str] = Field(default=None, alias="identity")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ActivityTaskTimedOutEventAttributesModel(BaseModel):
    timeout_type: Literal[
        "HEARTBEAT", "SCHEDULE_TO_CLOSE", "SCHEDULE_TO_START", "START_TO_CLOSE"
    ] = Field(alias="timeoutType")
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    details: Optional[str] = Field(default=None, alias="details")


class WorkflowExecutionModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    run_id: str = Field(alias="runId")


class CancelTimerDecisionAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")


class CancelTimerFailedEventAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    cause: Literal["OPERATION_NOT_PERMITTED", "TIMER_ID_UNKNOWN"] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class CancelWorkflowExecutionDecisionAttributesModel(BaseModel):
    details: Optional[str] = Field(default=None, alias="details")


class CancelWorkflowExecutionFailedEventAttributesModel(BaseModel):
    cause: Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"] = Field(
        alias="cause"
    )
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class WorkflowTypeModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class CloseStatusFilterModel(BaseModel):
    status: Literal[
        "CANCELED", "COMPLETED", "CONTINUED_AS_NEW", "FAILED", "TERMINATED", "TIMED_OUT"
    ] = Field(alias="status")


class CompleteWorkflowExecutionDecisionAttributesModel(BaseModel):
    result: Optional[str] = Field(default=None, alias="result")


class CompleteWorkflowExecutionFailedEventAttributesModel(BaseModel):
    cause: Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"] = Field(
        alias="cause"
    )
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class ContinueAsNewWorkflowExecutionFailedEventAttributesModel(BaseModel):
    cause: Literal[
        "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "DEFAULT_CHILD_POLICY_UNDEFINED",
        "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_LIST_UNDEFINED",
        "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "OPERATION_NOT_PERMITTED",
        "UNHANDLED_DECISION",
        "WORKFLOW_TYPE_DEPRECATED",
        "WORKFLOW_TYPE_DOES_NOT_EXIST",
    ] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class ExecutionTimeFilterModel(BaseModel):
    oldest_date: Union[datetime, str] = Field(alias="oldestDate")
    latest_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="latestDate"
    )


class TagFilterModel(BaseModel):
    tag: str = Field(alias="tag")


class WorkflowExecutionFilterModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")


class WorkflowTypeFilterModel(BaseModel):
    name: str = Field(alias="name")
    version: Optional[str] = Field(default=None, alias="version")


class DecisionTaskCompletedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    execution_context: Optional[str] = Field(default=None, alias="executionContext")


class DecisionTaskStartedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    identity: Optional[str] = Field(default=None, alias="identity")


class DecisionTaskTimedOutEventAttributesModel(BaseModel):
    timeout_type: Literal["START_TO_CLOSE"] = Field(alias="timeoutType")
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")


class FailWorkflowExecutionDecisionAttributesModel(BaseModel):
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class RecordMarkerDecisionAttributesModel(BaseModel):
    marker_name: str = Field(alias="markerName")
    details: Optional[str] = Field(default=None, alias="details")


class RequestCancelActivityTaskDecisionAttributesModel(BaseModel):
    activity_id: str = Field(alias="activityId")


class RequestCancelExternalWorkflowExecutionDecisionAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    control: Optional[str] = Field(default=None, alias="control")


class ScheduleLambdaFunctionDecisionAttributesModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    control: Optional[str] = Field(default=None, alias="control")
    input: Optional[str] = Field(default=None, alias="input")
    start_to_close_timeout: Optional[str] = Field(
        default=None, alias="startToCloseTimeout"
    )


class SignalExternalWorkflowExecutionDecisionAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    signal_name: str = Field(alias="signalName")
    run_id: Optional[str] = Field(default=None, alias="runId")
    input: Optional[str] = Field(default=None, alias="input")
    control: Optional[str] = Field(default=None, alias="control")


class StartTimerDecisionAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    start_to_fire_timeout: str = Field(alias="startToFireTimeout")
    control: Optional[str] = Field(default=None, alias="control")


class DeprecateDomainInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DescribeDomainInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class DomainConfigurationModel(BaseModel):
    workflow_execution_retention_period_in_days: str = Field(
        alias="workflowExecutionRetentionPeriodInDays"
    )


class DomainInfoModel(BaseModel):
    name: str = Field(alias="name")
    status: Literal["DEPRECATED", "REGISTERED"] = Field(alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    arn: Optional[str] = Field(default=None, alias="arn")


class FailWorkflowExecutionFailedEventAttributesModel(BaseModel):
    cause: Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"] = Field(
        alias="cause"
    )
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class LambdaFunctionCompletedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    result: Optional[str] = Field(default=None, alias="result")


class LambdaFunctionFailedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class LambdaFunctionScheduledEventAttributesModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    control: Optional[str] = Field(default=None, alias="control")
    input: Optional[str] = Field(default=None, alias="input")
    start_to_close_timeout: Optional[str] = Field(
        default=None, alias="startToCloseTimeout"
    )


class LambdaFunctionStartedEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")


class LambdaFunctionTimedOutEventAttributesModel(BaseModel):
    scheduled_event_id: int = Field(alias="scheduledEventId")
    started_event_id: int = Field(alias="startedEventId")
    timeout_type: Optional[Literal["START_TO_CLOSE"]] = Field(
        default=None, alias="timeoutType"
    )


class MarkerRecordedEventAttributesModel(BaseModel):
    marker_name: str = Field(alias="markerName")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    details: Optional[str] = Field(default=None, alias="details")


class RecordMarkerFailedEventAttributesModel(BaseModel):
    marker_name: str = Field(alias="markerName")
    cause: Literal["OPERATION_NOT_PERMITTED"] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class RequestCancelActivityTaskFailedEventAttributesModel(BaseModel):
    activity_id: str = Field(alias="activityId")
    cause: Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"] = Field(
        alias="cause"
    )
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class RequestCancelExternalWorkflowExecutionFailedEventAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    cause: Literal[
        "OPERATION_NOT_PERMITTED",
        "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    ] = Field(alias="cause")
    initiated_event_id: int = Field(alias="initiatedEventId")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    control: Optional[str] = Field(default=None, alias="control")


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    control: Optional[str] = Field(default=None, alias="control")


class ScheduleLambdaFunctionFailedEventAttributesModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    cause: Literal[
        "ID_ALREADY_IN_USE",
        "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
        "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
    ] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class SignalExternalWorkflowExecutionFailedEventAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    cause: Literal[
        "OPERATION_NOT_PERMITTED",
        "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    ] = Field(alias="cause")
    initiated_event_id: int = Field(alias="initiatedEventId")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    control: Optional[str] = Field(default=None, alias="control")


class SignalExternalWorkflowExecutionInitiatedEventAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    signal_name: str = Field(alias="signalName")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    input: Optional[str] = Field(default=None, alias="input")
    control: Optional[str] = Field(default=None, alias="control")


class StartLambdaFunctionFailedEventAttributesModel(BaseModel):
    scheduled_event_id: Optional[int] = Field(default=None, alias="scheduledEventId")
    cause: Optional[Literal["ASSUME_ROLE_FAILED"]] = Field(default=None, alias="cause")
    message: Optional[str] = Field(default=None, alias="message")


class StartTimerFailedEventAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    cause: Literal[
        "OPEN_TIMERS_LIMIT_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
        "TIMER_CREATION_RATE_EXCEEDED",
        "TIMER_ID_ALREADY_IN_USE",
    ] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class TimerCanceledEventAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    started_event_id: int = Field(alias="startedEventId")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class TimerFiredEventAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    started_event_id: int = Field(alias="startedEventId")


class TimerStartedEventAttributesModel(BaseModel):
    timer_id: str = Field(alias="timerId")
    start_to_fire_timeout: str = Field(alias="startToFireTimeout")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    control: Optional[str] = Field(default=None, alias="control")


class WorkflowExecutionCanceledEventAttributesModel(BaseModel):
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    details: Optional[str] = Field(default=None, alias="details")


class WorkflowExecutionCompletedEventAttributesModel(BaseModel):
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    result: Optional[str] = Field(default=None, alias="result")


class WorkflowExecutionFailedEventAttributesModel(BaseModel):
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class WorkflowExecutionTerminatedEventAttributesModel(BaseModel):
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")
    cause: Optional[
        Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"]
    ] = Field(default=None, alias="cause")


class WorkflowExecutionTimedOutEventAttributesModel(BaseModel):
    timeout_type: Literal["START_TO_CLOSE"] = Field(alias="timeoutType")
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )


class ListActivityTypesInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    name: Optional[str] = Field(default=None, alias="name")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class ListDomainsInputRequestModel(BaseModel):
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ResourceTagModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ListWorkflowTypesInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    name: Optional[str] = Field(default=None, alias="name")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class RecordActivityTaskHeartbeatInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    details: Optional[str] = Field(default=None, alias="details")


class RequestCancelWorkflowExecutionInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_id: str = Field(alias="workflowId")
    run_id: Optional[str] = Field(default=None, alias="runId")


class RespondActivityTaskCanceledInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    details: Optional[str] = Field(default=None, alias="details")


class RespondActivityTaskCompletedInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    result: Optional[str] = Field(default=None, alias="result")


class RespondActivityTaskFailedInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class SignalWorkflowExecutionInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_id: str = Field(alias="workflowId")
    signal_name: str = Field(alias="signalName")
    run_id: Optional[str] = Field(default=None, alias="runId")
    input: Optional[str] = Field(default=None, alias="input")


class TerminateWorkflowExecutionInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_id: str = Field(alias="workflowId")
    run_id: Optional[str] = Field(default=None, alias="runId")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")
    child_policy: Optional[Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]] = Field(
        default=None, alias="childPolicy"
    )


class UndeprecateDomainInputRequestModel(BaseModel):
    name: str = Field(alias="name")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class WorkflowExecutionOpenCountsModel(BaseModel):
    open_activity_tasks: int = Field(alias="openActivityTasks")
    open_decision_tasks: int = Field(alias="openDecisionTasks")
    open_timers: int = Field(alias="openTimers")
    open_child_workflow_executions: int = Field(alias="openChildWorkflowExecutions")
    open_lambda_functions: Optional[int] = Field(
        default=None, alias="openLambdaFunctions"
    )


class ActivityTypeInfoModel(BaseModel):
    activity_type: ActivityTypeModel = Field(alias="activityType")
    status: Literal["DEPRECATED", "REGISTERED"] = Field(alias="status")
    creation_date: datetime = Field(alias="creationDate")
    description: Optional[str] = Field(default=None, alias="description")
    deprecation_date: Optional[datetime] = Field(default=None, alias="deprecationDate")


class DeprecateActivityTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    activity_type: ActivityTypeModel = Field(alias="activityType")


class DescribeActivityTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    activity_type: ActivityTypeModel = Field(alias="activityType")


class ScheduleActivityTaskFailedEventAttributesModel(BaseModel):
    activity_type: ActivityTypeModel = Field(alias="activityType")
    activity_id: str = Field(alias="activityId")
    cause: Literal[
        "ACTIVITY_CREATION_RATE_EXCEEDED",
        "ACTIVITY_ID_ALREADY_IN_USE",
        "ACTIVITY_TYPE_DEPRECATED",
        "ACTIVITY_TYPE_DOES_NOT_EXIST",
        "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
        "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
        "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_LIST_UNDEFINED",
        "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
    ] = Field(alias="cause")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")


class UndeprecateActivityTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    activity_type: ActivityTypeModel = Field(alias="activityType")


class ActivityTaskScheduledEventAttributesModel(BaseModel):
    activity_type: ActivityTypeModel = Field(alias="activityType")
    activity_id: str = Field(alias="activityId")
    task_list: TaskListModel = Field(alias="taskList")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    input: Optional[str] = Field(default=None, alias="input")
    control: Optional[str] = Field(default=None, alias="control")
    schedule_to_start_timeout: Optional[str] = Field(
        default=None, alias="scheduleToStartTimeout"
    )
    schedule_to_close_timeout: Optional[str] = Field(
        default=None, alias="scheduleToCloseTimeout"
    )
    start_to_close_timeout: Optional[str] = Field(
        default=None, alias="startToCloseTimeout"
    )
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    heartbeat_timeout: Optional[str] = Field(default=None, alias="heartbeatTimeout")


class ActivityTypeConfigurationModel(BaseModel):
    default_task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskStartToCloseTimeout"
    )
    default_task_heartbeat_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskHeartbeatTimeout"
    )
    default_task_list: Optional[TaskListModel] = Field(
        default=None, alias="defaultTaskList"
    )
    default_task_priority: Optional[str] = Field(
        default=None, alias="defaultTaskPriority"
    )
    default_task_schedule_to_start_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskScheduleToStartTimeout"
    )
    default_task_schedule_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskScheduleToCloseTimeout"
    )


class ContinueAsNewWorkflowExecutionDecisionAttributesModel(BaseModel):
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    task_list: Optional[TaskListModel] = Field(default=None, alias="taskList")
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    child_policy: Optional[Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]] = Field(
        default=None, alias="childPolicy"
    )
    tag_list: Optional[Sequence[str]] = Field(default=None, alias="tagList")
    workflow_type_version: Optional[str] = Field(
        default=None, alias="workflowTypeVersion"
    )
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class CountPendingActivityTasksInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    task_list: TaskListModel = Field(alias="taskList")


class CountPendingDecisionTasksInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    task_list: TaskListModel = Field(alias="taskList")


class DecisionTaskScheduledEventAttributesModel(BaseModel):
    task_list: TaskListModel = Field(alias="taskList")
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    start_to_close_timeout: Optional[str] = Field(
        default=None, alias="startToCloseTimeout"
    )


class PollForActivityTaskInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    task_list: TaskListModel = Field(alias="taskList")
    identity: Optional[str] = Field(default=None, alias="identity")


class PollForDecisionTaskInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    task_list: TaskListModel = Field(alias="taskList")
    identity: Optional[str] = Field(default=None, alias="identity")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class RegisterActivityTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    description: Optional[str] = Field(default=None, alias="description")
    default_task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskStartToCloseTimeout"
    )
    default_task_heartbeat_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskHeartbeatTimeout"
    )
    default_task_list: Optional[TaskListModel] = Field(
        default=None, alias="defaultTaskList"
    )
    default_task_priority: Optional[str] = Field(
        default=None, alias="defaultTaskPriority"
    )
    default_task_schedule_to_start_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskScheduleToStartTimeout"
    )
    default_task_schedule_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskScheduleToCloseTimeout"
    )


class RegisterWorkflowTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    description: Optional[str] = Field(default=None, alias="description")
    default_task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskStartToCloseTimeout"
    )
    default_execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultExecutionStartToCloseTimeout"
    )
    default_task_list: Optional[TaskListModel] = Field(
        default=None, alias="defaultTaskList"
    )
    default_task_priority: Optional[str] = Field(
        default=None, alias="defaultTaskPriority"
    )
    default_child_policy: Optional[
        Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]
    ] = Field(default=None, alias="defaultChildPolicy")
    default_lambda_role: Optional[str] = Field(default=None, alias="defaultLambdaRole")


class ScheduleActivityTaskDecisionAttributesModel(BaseModel):
    activity_type: ActivityTypeModel = Field(alias="activityType")
    activity_id: str = Field(alias="activityId")
    control: Optional[str] = Field(default=None, alias="control")
    input: Optional[str] = Field(default=None, alias="input")
    schedule_to_close_timeout: Optional[str] = Field(
        default=None, alias="scheduleToCloseTimeout"
    )
    task_list: Optional[TaskListModel] = Field(default=None, alias="taskList")
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    schedule_to_start_timeout: Optional[str] = Field(
        default=None, alias="scheduleToStartTimeout"
    )
    start_to_close_timeout: Optional[str] = Field(
        default=None, alias="startToCloseTimeout"
    )
    heartbeat_timeout: Optional[str] = Field(default=None, alias="heartbeatTimeout")


class WorkflowExecutionConfigurationModel(BaseModel):
    task_start_to_close_timeout: str = Field(alias="taskStartToCloseTimeout")
    execution_start_to_close_timeout: str = Field(alias="executionStartToCloseTimeout")
    task_list: TaskListModel = Field(alias="taskList")
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class WorkflowTypeConfigurationModel(BaseModel):
    default_task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultTaskStartToCloseTimeout"
    )
    default_execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="defaultExecutionStartToCloseTimeout"
    )
    default_task_list: Optional[TaskListModel] = Field(
        default=None, alias="defaultTaskList"
    )
    default_task_priority: Optional[str] = Field(
        default=None, alias="defaultTaskPriority"
    )
    default_child_policy: Optional[
        Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]
    ] = Field(default=None, alias="defaultChildPolicy")
    default_lambda_role: Optional[str] = Field(default=None, alias="defaultLambdaRole")


class ActivityTaskStatusModel(BaseModel):
    cancel_requested: bool = Field(alias="cancelRequested")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PendingTaskCountModel(BaseModel):
    count: int = Field(alias="count")
    truncated: bool = Field(alias="truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunModel(BaseModel):
    run_id: str = Field(alias="runId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkflowExecutionCountModel(BaseModel):
    count: int = Field(alias="count")
    truncated: bool = Field(alias="truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivityTaskModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    activity_id: str = Field(alias="activityId")
    started_event_id: int = Field(alias="startedEventId")
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    activity_type: ActivityTypeModel = Field(alias="activityType")
    input: str = Field(alias="input")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkflowExecutionInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    execution: WorkflowExecutionModel = Field(alias="execution")


class ExternalWorkflowExecutionCancelRequestedEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    initiated_event_id: int = Field(alias="initiatedEventId")


class ExternalWorkflowExecutionSignaledEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    initiated_event_id: int = Field(alias="initiatedEventId")


class GetWorkflowExecutionHistoryInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    execution: WorkflowExecutionModel = Field(alias="execution")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class WorkflowExecutionCancelRequestedEventAttributesModel(BaseModel):
    external_workflow_execution: Optional[WorkflowExecutionModel] = Field(
        default=None, alias="externalWorkflowExecution"
    )
    external_initiated_event_id: Optional[int] = Field(
        default=None, alias="externalInitiatedEventId"
    )
    cause: Optional[Literal["CHILD_POLICY_APPLIED"]] = Field(
        default=None, alias="cause"
    )


class WorkflowExecutionSignaledEventAttributesModel(BaseModel):
    signal_name: str = Field(alias="signalName")
    input: Optional[str] = Field(default=None, alias="input")
    external_workflow_execution: Optional[WorkflowExecutionModel] = Field(
        default=None, alias="externalWorkflowExecution"
    )
    external_initiated_event_id: Optional[int] = Field(
        default=None, alias="externalInitiatedEventId"
    )


class ChildWorkflowExecutionCanceledEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    initiated_event_id: int = Field(alias="initiatedEventId")
    started_event_id: int = Field(alias="startedEventId")
    details: Optional[str] = Field(default=None, alias="details")


class ChildWorkflowExecutionCompletedEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    initiated_event_id: int = Field(alias="initiatedEventId")
    started_event_id: int = Field(alias="startedEventId")
    result: Optional[str] = Field(default=None, alias="result")


class ChildWorkflowExecutionFailedEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    initiated_event_id: int = Field(alias="initiatedEventId")
    started_event_id: int = Field(alias="startedEventId")
    reason: Optional[str] = Field(default=None, alias="reason")
    details: Optional[str] = Field(default=None, alias="details")


class ChildWorkflowExecutionStartedEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    initiated_event_id: int = Field(alias="initiatedEventId")


class ChildWorkflowExecutionTerminatedEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    initiated_event_id: int = Field(alias="initiatedEventId")
    started_event_id: int = Field(alias="startedEventId")


class ChildWorkflowExecutionTimedOutEventAttributesModel(BaseModel):
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    timeout_type: Literal["START_TO_CLOSE"] = Field(alias="timeoutType")
    initiated_event_id: int = Field(alias="initiatedEventId")
    started_event_id: int = Field(alias="startedEventId")


class DeprecateWorkflowTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")


class DescribeWorkflowTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")


class StartChildWorkflowExecutionDecisionAttributesModel(BaseModel):
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    workflow_id: str = Field(alias="workflowId")
    control: Optional[str] = Field(default=None, alias="control")
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    task_list: Optional[TaskListModel] = Field(default=None, alias="taskList")
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    child_policy: Optional[Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]] = Field(
        default=None, alias="childPolicy"
    )
    tag_list: Optional[Sequence[str]] = Field(default=None, alias="tagList")
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class StartChildWorkflowExecutionFailedEventAttributesModel(BaseModel):
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    cause: Literal[
        "CHILD_CREATION_RATE_EXCEEDED",
        "DEFAULT_CHILD_POLICY_UNDEFINED",
        "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_LIST_UNDEFINED",
        "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "OPEN_CHILDREN_LIMIT_EXCEEDED",
        "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
        "WORKFLOW_ALREADY_RUNNING",
        "WORKFLOW_TYPE_DEPRECATED",
        "WORKFLOW_TYPE_DOES_NOT_EXIST",
    ] = Field(alias="cause")
    workflow_id: str = Field(alias="workflowId")
    initiated_event_id: int = Field(alias="initiatedEventId")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    control: Optional[str] = Field(default=None, alias="control")


class StartChildWorkflowExecutionInitiatedEventAttributesModel(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    task_list: TaskListModel = Field(alias="taskList")
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )
    control: Optional[str] = Field(default=None, alias="control")
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    tag_list: Optional[List[str]] = Field(default=None, alias="tagList")
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class StartWorkflowExecutionInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_id: str = Field(alias="workflowId")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    task_list: Optional[TaskListModel] = Field(default=None, alias="taskList")
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    tag_list: Optional[Sequence[str]] = Field(default=None, alias="tagList")
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    child_policy: Optional[Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]] = Field(
        default=None, alias="childPolicy"
    )
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class UndeprecateWorkflowTypeInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")


class WorkflowExecutionContinuedAsNewEventAttributesModel(BaseModel):
    decision_task_completed_event_id: int = Field(alias="decisionTaskCompletedEventId")
    new_execution_run_id: str = Field(alias="newExecutionRunId")
    task_list: TaskListModel = Field(alias="taskList")
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    tag_list: Optional[List[str]] = Field(default=None, alias="tagList")
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class WorkflowExecutionInfoModel(BaseModel):
    execution: WorkflowExecutionModel = Field(alias="execution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    start_timestamp: datetime = Field(alias="startTimestamp")
    execution_status: Literal["CLOSED", "OPEN"] = Field(alias="executionStatus")
    close_timestamp: Optional[datetime] = Field(default=None, alias="closeTimestamp")
    close_status: Optional[
        Literal[
            "CANCELED",
            "COMPLETED",
            "CONTINUED_AS_NEW",
            "FAILED",
            "TERMINATED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="closeStatus")
    parent: Optional[WorkflowExecutionModel] = Field(default=None, alias="parent")
    tag_list: Optional[List[str]] = Field(default=None, alias="tagList")
    cancel_requested: Optional[bool] = Field(default=None, alias="cancelRequested")


class WorkflowExecutionStartedEventAttributesModel(BaseModel):
    child_policy: Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"] = Field(
        alias="childPolicy"
    )
    task_list: TaskListModel = Field(alias="taskList")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    input: Optional[str] = Field(default=None, alias="input")
    execution_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="executionStartToCloseTimeout"
    )
    task_start_to_close_timeout: Optional[str] = Field(
        default=None, alias="taskStartToCloseTimeout"
    )
    task_priority: Optional[str] = Field(default=None, alias="taskPriority")
    tag_list: Optional[List[str]] = Field(default=None, alias="tagList")
    continued_execution_run_id: Optional[str] = Field(
        default=None, alias="continuedExecutionRunId"
    )
    parent_workflow_execution: Optional[WorkflowExecutionModel] = Field(
        default=None, alias="parentWorkflowExecution"
    )
    parent_initiated_event_id: Optional[int] = Field(
        default=None, alias="parentInitiatedEventId"
    )
    lambda_role: Optional[str] = Field(default=None, alias="lambdaRole")


class WorkflowTypeInfoModel(BaseModel):
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    status: Literal["DEPRECATED", "REGISTERED"] = Field(alias="status")
    creation_date: datetime = Field(alias="creationDate")
    description: Optional[str] = Field(default=None, alias="description")
    deprecation_date: Optional[datetime] = Field(default=None, alias="deprecationDate")


class CountClosedWorkflowExecutionsInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    start_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="startTimeFilter"
    )
    close_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="closeTimeFilter"
    )
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    close_status_filter: Optional[CloseStatusFilterModel] = Field(
        default=None, alias="closeStatusFilter"
    )


class CountOpenWorkflowExecutionsInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    start_time_filter: ExecutionTimeFilterModel = Field(alias="startTimeFilter")
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )


class ListClosedWorkflowExecutionsInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    start_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="startTimeFilter"
    )
    close_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="closeTimeFilter"
    )
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )
    close_status_filter: Optional[CloseStatusFilterModel] = Field(
        default=None, alias="closeStatusFilter"
    )
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class ListOpenWorkflowExecutionsInputRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    start_time_filter: ExecutionTimeFilterModel = Field(alias="startTimeFilter")
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")
    maximum_page_size: Optional[int] = Field(default=None, alias="maximumPageSize")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )


class DomainDetailModel(BaseModel):
    domain_info: DomainInfoModel = Field(alias="domainInfo")
    configuration: DomainConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainInfosModel(BaseModel):
    domain_infos: List[DomainInfoModel] = Field(alias="domainInfos")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowExecutionHistoryInputGetWorkflowExecutionHistoryPaginateModel(
    BaseModel
):
    domain: str = Field(alias="domain")
    execution: WorkflowExecutionModel = Field(alias="execution")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListActivityTypesInputListActivityTypesPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    name: Optional[str] = Field(default=None, alias="name")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClosedWorkflowExecutionsInputListClosedWorkflowExecutionsPaginateModel(
    BaseModel
):
    domain: str = Field(alias="domain")
    start_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="startTimeFilter"
    )
    close_time_filter: Optional[ExecutionTimeFilterModel] = Field(
        default=None, alias="closeTimeFilter"
    )
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )
    close_status_filter: Optional[CloseStatusFilterModel] = Field(
        default=None, alias="closeStatusFilter"
    )
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainsInputListDomainsPaginateModel(BaseModel):
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOpenWorkflowExecutionsInputListOpenWorkflowExecutionsPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    start_time_filter: ExecutionTimeFilterModel = Field(alias="startTimeFilter")
    type_filter: Optional[WorkflowTypeFilterModel] = Field(
        default=None, alias="typeFilter"
    )
    tag_filter: Optional[TagFilterModel] = Field(default=None, alias="tagFilter")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    execution_filter: Optional[WorkflowExecutionFilterModel] = Field(
        default=None, alias="executionFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkflowTypesInputListWorkflowTypesPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    registration_status: Literal["DEPRECATED", "REGISTERED"] = Field(
        alias="registrationStatus"
    )
    name: Optional[str] = Field(default=None, alias="name")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PollForDecisionTaskInputPollForDecisionTaskPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    task_list: TaskListModel = Field(alias="taskList")
    identity: Optional[str] = Field(default=None, alias="identity")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[ResourceTagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDomainInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    workflow_execution_retention_period_in_days: str = Field(
        alias="workflowExecutionRetentionPeriodInDays"
    )
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[ResourceTagModel]] = Field(default=None, alias="tags")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[ResourceTagModel] = Field(alias="tags")


class ActivityTypeInfosModel(BaseModel):
    type_infos: List[ActivityTypeInfoModel] = Field(alias="typeInfos")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivityTypeDetailModel(BaseModel):
    type_info: ActivityTypeInfoModel = Field(alias="typeInfo")
    configuration: ActivityTypeConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecisionModel(BaseModel):
    decision_type: Literal[
        "CancelTimer",
        "CancelWorkflowExecution",
        "CompleteWorkflowExecution",
        "ContinueAsNewWorkflowExecution",
        "FailWorkflowExecution",
        "RecordMarker",
        "RequestCancelActivityTask",
        "RequestCancelExternalWorkflowExecution",
        "ScheduleActivityTask",
        "ScheduleLambdaFunction",
        "SignalExternalWorkflowExecution",
        "StartChildWorkflowExecution",
        "StartTimer",
    ] = Field(alias="decisionType")
    schedule_activity_task_decision_attributes: Optional[
        ScheduleActivityTaskDecisionAttributesModel
    ] = Field(default=None, alias="scheduleActivityTaskDecisionAttributes")
    request_cancel_activity_task_decision_attributes: Optional[
        RequestCancelActivityTaskDecisionAttributesModel
    ] = Field(default=None, alias="requestCancelActivityTaskDecisionAttributes")
    complete_workflow_execution_decision_attributes: Optional[
        CompleteWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="completeWorkflowExecutionDecisionAttributes")
    fail_workflow_execution_decision_attributes: Optional[
        FailWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="failWorkflowExecutionDecisionAttributes")
    cancel_workflow_execution_decision_attributes: Optional[
        CancelWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="cancelWorkflowExecutionDecisionAttributes")
    continue_as_new_workflow_execution_decision_attributes: Optional[
        ContinueAsNewWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="continueAsNewWorkflowExecutionDecisionAttributes")
    record_marker_decision_attributes: Optional[
        RecordMarkerDecisionAttributesModel
    ] = Field(default=None, alias="recordMarkerDecisionAttributes")
    start_timer_decision_attributes: Optional[
        StartTimerDecisionAttributesModel
    ] = Field(default=None, alias="startTimerDecisionAttributes")
    cancel_timer_decision_attributes: Optional[
        CancelTimerDecisionAttributesModel
    ] = Field(default=None, alias="cancelTimerDecisionAttributes")
    signal_external_workflow_execution_decision_attributes: Optional[
        SignalExternalWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="signalExternalWorkflowExecutionDecisionAttributes")
    request_cancel_external_workflow_execution_decision_attributes: Optional[
        RequestCancelExternalWorkflowExecutionDecisionAttributesModel
    ] = Field(
        default=None, alias="requestCancelExternalWorkflowExecutionDecisionAttributes"
    )
    start_child_workflow_execution_decision_attributes: Optional[
        StartChildWorkflowExecutionDecisionAttributesModel
    ] = Field(default=None, alias="startChildWorkflowExecutionDecisionAttributes")
    schedule_lambda_function_decision_attributes: Optional[
        ScheduleLambdaFunctionDecisionAttributesModel
    ] = Field(default=None, alias="scheduleLambdaFunctionDecisionAttributes")


class WorkflowExecutionDetailModel(BaseModel):
    execution_info: WorkflowExecutionInfoModel = Field(alias="executionInfo")
    execution_configuration: WorkflowExecutionConfigurationModel = Field(
        alias="executionConfiguration"
    )
    open_counts: WorkflowExecutionOpenCountsModel = Field(alias="openCounts")
    latest_activity_task_timestamp: datetime = Field(
        alias="latestActivityTaskTimestamp"
    )
    latest_execution_context: str = Field(alias="latestExecutionContext")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkflowExecutionInfosModel(BaseModel):
    execution_infos: List[WorkflowExecutionInfoModel] = Field(alias="executionInfos")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HistoryEventModel(BaseModel):
    event_timestamp: datetime = Field(alias="eventTimestamp")
    event_type: Literal[
        "ActivityTaskCancelRequested",
        "ActivityTaskCanceled",
        "ActivityTaskCompleted",
        "ActivityTaskFailed",
        "ActivityTaskScheduled",
        "ActivityTaskStarted",
        "ActivityTaskTimedOut",
        "CancelTimerFailed",
        "CancelWorkflowExecutionFailed",
        "ChildWorkflowExecutionCanceled",
        "ChildWorkflowExecutionCompleted",
        "ChildWorkflowExecutionFailed",
        "ChildWorkflowExecutionStarted",
        "ChildWorkflowExecutionTerminated",
        "ChildWorkflowExecutionTimedOut",
        "CompleteWorkflowExecutionFailed",
        "ContinueAsNewWorkflowExecutionFailed",
        "DecisionTaskCompleted",
        "DecisionTaskScheduled",
        "DecisionTaskStarted",
        "DecisionTaskTimedOut",
        "ExternalWorkflowExecutionCancelRequested",
        "ExternalWorkflowExecutionSignaled",
        "FailWorkflowExecutionFailed",
        "LambdaFunctionCompleted",
        "LambdaFunctionFailed",
        "LambdaFunctionScheduled",
        "LambdaFunctionStarted",
        "LambdaFunctionTimedOut",
        "MarkerRecorded",
        "RecordMarkerFailed",
        "RequestCancelActivityTaskFailed",
        "RequestCancelExternalWorkflowExecutionFailed",
        "RequestCancelExternalWorkflowExecutionInitiated",
        "ScheduleActivityTaskFailed",
        "ScheduleLambdaFunctionFailed",
        "SignalExternalWorkflowExecutionFailed",
        "SignalExternalWorkflowExecutionInitiated",
        "StartChildWorkflowExecutionFailed",
        "StartChildWorkflowExecutionInitiated",
        "StartLambdaFunctionFailed",
        "StartTimerFailed",
        "TimerCanceled",
        "TimerFired",
        "TimerStarted",
        "WorkflowExecutionCancelRequested",
        "WorkflowExecutionCanceled",
        "WorkflowExecutionCompleted",
        "WorkflowExecutionContinuedAsNew",
        "WorkflowExecutionFailed",
        "WorkflowExecutionSignaled",
        "WorkflowExecutionStarted",
        "WorkflowExecutionTerminated",
        "WorkflowExecutionTimedOut",
    ] = Field(alias="eventType")
    event_id: int = Field(alias="eventId")
    workflow_execution_started_event_attributes: Optional[
        WorkflowExecutionStartedEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionStartedEventAttributes")
    workflow_execution_completed_event_attributes: Optional[
        WorkflowExecutionCompletedEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionCompletedEventAttributes")
    complete_workflow_execution_failed_event_attributes: Optional[
        CompleteWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="completeWorkflowExecutionFailedEventAttributes")
    workflow_execution_failed_event_attributes: Optional[
        WorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionFailedEventAttributes")
    fail_workflow_execution_failed_event_attributes: Optional[
        FailWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="failWorkflowExecutionFailedEventAttributes")
    workflow_execution_timed_out_event_attributes: Optional[
        WorkflowExecutionTimedOutEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionTimedOutEventAttributes")
    workflow_execution_canceled_event_attributes: Optional[
        WorkflowExecutionCanceledEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionCanceledEventAttributes")
    cancel_workflow_execution_failed_event_attributes: Optional[
        CancelWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="cancelWorkflowExecutionFailedEventAttributes")
    workflow_execution_continued_as_new_event_attributes: Optional[
        WorkflowExecutionContinuedAsNewEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionContinuedAsNewEventAttributes")
    continue_as_new_workflow_execution_failed_event_attributes: Optional[
        ContinueAsNewWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="continueAsNewWorkflowExecutionFailedEventAttributes")
    workflow_execution_terminated_event_attributes: Optional[
        WorkflowExecutionTerminatedEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionTerminatedEventAttributes")
    workflow_execution_cancel_requested_event_attributes: Optional[
        WorkflowExecutionCancelRequestedEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionCancelRequestedEventAttributes")
    decision_task_scheduled_event_attributes: Optional[
        DecisionTaskScheduledEventAttributesModel
    ] = Field(default=None, alias="decisionTaskScheduledEventAttributes")
    decision_task_started_event_attributes: Optional[
        DecisionTaskStartedEventAttributesModel
    ] = Field(default=None, alias="decisionTaskStartedEventAttributes")
    decision_task_completed_event_attributes: Optional[
        DecisionTaskCompletedEventAttributesModel
    ] = Field(default=None, alias="decisionTaskCompletedEventAttributes")
    decision_task_timed_out_event_attributes: Optional[
        DecisionTaskTimedOutEventAttributesModel
    ] = Field(default=None, alias="decisionTaskTimedOutEventAttributes")
    activity_task_scheduled_event_attributes: Optional[
        ActivityTaskScheduledEventAttributesModel
    ] = Field(default=None, alias="activityTaskScheduledEventAttributes")
    activity_task_started_event_attributes: Optional[
        ActivityTaskStartedEventAttributesModel
    ] = Field(default=None, alias="activityTaskStartedEventAttributes")
    activity_task_completed_event_attributes: Optional[
        ActivityTaskCompletedEventAttributesModel
    ] = Field(default=None, alias="activityTaskCompletedEventAttributes")
    activity_task_failed_event_attributes: Optional[
        ActivityTaskFailedEventAttributesModel
    ] = Field(default=None, alias="activityTaskFailedEventAttributes")
    activity_task_timed_out_event_attributes: Optional[
        ActivityTaskTimedOutEventAttributesModel
    ] = Field(default=None, alias="activityTaskTimedOutEventAttributes")
    activity_task_canceled_event_attributes: Optional[
        ActivityTaskCanceledEventAttributesModel
    ] = Field(default=None, alias="activityTaskCanceledEventAttributes")
    activity_task_cancel_requested_event_attributes: Optional[
        ActivityTaskCancelRequestedEventAttributesModel
    ] = Field(default=None, alias="activityTaskCancelRequestedEventAttributes")
    workflow_execution_signaled_event_attributes: Optional[
        WorkflowExecutionSignaledEventAttributesModel
    ] = Field(default=None, alias="workflowExecutionSignaledEventAttributes")
    marker_recorded_event_attributes: Optional[
        MarkerRecordedEventAttributesModel
    ] = Field(default=None, alias="markerRecordedEventAttributes")
    record_marker_failed_event_attributes: Optional[
        RecordMarkerFailedEventAttributesModel
    ] = Field(default=None, alias="recordMarkerFailedEventAttributes")
    timer_started_event_attributes: Optional[TimerStartedEventAttributesModel] = Field(
        default=None, alias="timerStartedEventAttributes"
    )
    timer_fired_event_attributes: Optional[TimerFiredEventAttributesModel] = Field(
        default=None, alias="timerFiredEventAttributes"
    )
    timer_canceled_event_attributes: Optional[
        TimerCanceledEventAttributesModel
    ] = Field(default=None, alias="timerCanceledEventAttributes")
    start_child_workflow_execution_initiated_event_attributes: Optional[
        StartChildWorkflowExecutionInitiatedEventAttributesModel
    ] = Field(default=None, alias="startChildWorkflowExecutionInitiatedEventAttributes")
    child_workflow_execution_started_event_attributes: Optional[
        ChildWorkflowExecutionStartedEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionStartedEventAttributes")
    child_workflow_execution_completed_event_attributes: Optional[
        ChildWorkflowExecutionCompletedEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionCompletedEventAttributes")
    child_workflow_execution_failed_event_attributes: Optional[
        ChildWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionFailedEventAttributes")
    child_workflow_execution_timed_out_event_attributes: Optional[
        ChildWorkflowExecutionTimedOutEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionTimedOutEventAttributes")
    child_workflow_execution_canceled_event_attributes: Optional[
        ChildWorkflowExecutionCanceledEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionCanceledEventAttributes")
    child_workflow_execution_terminated_event_attributes: Optional[
        ChildWorkflowExecutionTerminatedEventAttributesModel
    ] = Field(default=None, alias="childWorkflowExecutionTerminatedEventAttributes")
    signal_external_workflow_execution_initiated_event_attributes: Optional[
        SignalExternalWorkflowExecutionInitiatedEventAttributesModel
    ] = Field(
        default=None, alias="signalExternalWorkflowExecutionInitiatedEventAttributes"
    )
    external_workflow_execution_signaled_event_attributes: Optional[
        ExternalWorkflowExecutionSignaledEventAttributesModel
    ] = Field(default=None, alias="externalWorkflowExecutionSignaledEventAttributes")
    signal_external_workflow_execution_failed_event_attributes: Optional[
        SignalExternalWorkflowExecutionFailedEventAttributesModel
    ] = Field(
        default=None, alias="signalExternalWorkflowExecutionFailedEventAttributes"
    )
    external_workflow_execution_cancel_requested_event_attributes: Optional[
        ExternalWorkflowExecutionCancelRequestedEventAttributesModel
    ] = Field(
        default=None, alias="externalWorkflowExecutionCancelRequestedEventAttributes"
    )
    request_cancel_external_workflow_execution_initiated_event_attributes: Optional[
        RequestCancelExternalWorkflowExecutionInitiatedEventAttributesModel
    ] = Field(
        default=None,
        alias="requestCancelExternalWorkflowExecutionInitiatedEventAttributes",
    )
    request_cancel_external_workflow_execution_failed_event_attributes: Optional[
        RequestCancelExternalWorkflowExecutionFailedEventAttributesModel
    ] = Field(
        default=None,
        alias="requestCancelExternalWorkflowExecutionFailedEventAttributes",
    )
    schedule_activity_task_failed_event_attributes: Optional[
        ScheduleActivityTaskFailedEventAttributesModel
    ] = Field(default=None, alias="scheduleActivityTaskFailedEventAttributes")
    request_cancel_activity_task_failed_event_attributes: Optional[
        RequestCancelActivityTaskFailedEventAttributesModel
    ] = Field(default=None, alias="requestCancelActivityTaskFailedEventAttributes")
    start_timer_failed_event_attributes: Optional[
        StartTimerFailedEventAttributesModel
    ] = Field(default=None, alias="startTimerFailedEventAttributes")
    cancel_timer_failed_event_attributes: Optional[
        CancelTimerFailedEventAttributesModel
    ] = Field(default=None, alias="cancelTimerFailedEventAttributes")
    start_child_workflow_execution_failed_event_attributes: Optional[
        StartChildWorkflowExecutionFailedEventAttributesModel
    ] = Field(default=None, alias="startChildWorkflowExecutionFailedEventAttributes")
    lambda_function_scheduled_event_attributes: Optional[
        LambdaFunctionScheduledEventAttributesModel
    ] = Field(default=None, alias="lambdaFunctionScheduledEventAttributes")
    lambda_function_started_event_attributes: Optional[
        LambdaFunctionStartedEventAttributesModel
    ] = Field(default=None, alias="lambdaFunctionStartedEventAttributes")
    lambda_function_completed_event_attributes: Optional[
        LambdaFunctionCompletedEventAttributesModel
    ] = Field(default=None, alias="lambdaFunctionCompletedEventAttributes")
    lambda_function_failed_event_attributes: Optional[
        LambdaFunctionFailedEventAttributesModel
    ] = Field(default=None, alias="lambdaFunctionFailedEventAttributes")
    lambda_function_timed_out_event_attributes: Optional[
        LambdaFunctionTimedOutEventAttributesModel
    ] = Field(default=None, alias="lambdaFunctionTimedOutEventAttributes")
    schedule_lambda_function_failed_event_attributes: Optional[
        ScheduleLambdaFunctionFailedEventAttributesModel
    ] = Field(default=None, alias="scheduleLambdaFunctionFailedEventAttributes")
    start_lambda_function_failed_event_attributes: Optional[
        StartLambdaFunctionFailedEventAttributesModel
    ] = Field(default=None, alias="startLambdaFunctionFailedEventAttributes")


class WorkflowTypeDetailModel(BaseModel):
    type_info: WorkflowTypeInfoModel = Field(alias="typeInfo")
    configuration: WorkflowTypeConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkflowTypeInfosModel(BaseModel):
    type_infos: List[WorkflowTypeInfoModel] = Field(alias="typeInfos")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RespondDecisionTaskCompletedInputRequestModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    decisions: Optional[Sequence[DecisionModel]] = Field(
        default=None, alias="decisions"
    )
    execution_context: Optional[str] = Field(default=None, alias="executionContext")


class DecisionTaskModel(BaseModel):
    task_token: str = Field(alias="taskToken")
    started_event_id: int = Field(alias="startedEventId")
    workflow_execution: WorkflowExecutionModel = Field(alias="workflowExecution")
    workflow_type: WorkflowTypeModel = Field(alias="workflowType")
    events: List[HistoryEventModel] = Field(alias="events")
    next_page_token: str = Field(alias="nextPageToken")
    previous_started_event_id: int = Field(alias="previousStartedEventId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HistoryModel(BaseModel):
    events: List[HistoryEventModel] = Field(alias="events")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
