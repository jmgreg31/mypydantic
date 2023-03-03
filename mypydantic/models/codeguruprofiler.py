# Model Generated: Thu Mar  2 21:56:17 2023

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


class ChannelModel(BaseModel):
    event_publishers: Sequence[Literal["AnomalyDetection"]] = Field(
        alias="eventPublishers"
    )
    uri: str = Field(alias="uri")
    id: Optional[str] = Field(default=None, alias="id")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AgentConfigurationModel(BaseModel):
    period_in_seconds: int = Field(alias="periodInSeconds")
    should_profile: bool = Field(alias="shouldProfile")
    agent_parameters: Optional[
        Dict[
            Literal[
                "MaxStackDepth",
                "MemoryUsageLimitPercent",
                "MinimumTimeForReportingInMilliseconds",
                "ReportingIntervalInMilliseconds",
                "SamplingIntervalInMilliseconds",
            ],
            str,
        ]
    ] = Field(default=None, alias="agentParameters")


class AgentOrchestrationConfigModel(BaseModel):
    profiling_enabled: bool = Field(alias="profilingEnabled")


class AggregatedProfileTimeModel(BaseModel):
    period: Optional[Literal["P1D", "PT1H", "PT5M"]] = Field(
        default=None, alias="period"
    )
    start: Optional[datetime] = Field(default=None, alias="start")


class UserFeedbackModel(BaseModel):
    type: Literal["Negative", "Positive"] = Field(alias="type")


class MetricModel(BaseModel):
    frame_name: str = Field(alias="frameName")
    thread_states: List[str] = Field(alias="threadStates")
    type: Literal["AggregatedRelativeTotalTime"] = Field(alias="type")


class FrameMetricModel(BaseModel):
    frame_name: str = Field(alias="frameName")
    thread_states: Sequence[str] = Field(alias="threadStates")
    type: Literal["AggregatedRelativeTotalTime"] = Field(alias="type")


class TimestampStructureModel(BaseModel):
    value: datetime = Field(alias="value")


class ConfigureAgentRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")
    fleet_instance_id: Optional[str] = Field(default=None, alias="fleetInstanceId")
    metadata: Optional[
        Mapping[
            Literal[
                "AgentId",
                "AwsRequestId",
                "ComputePlatform",
                "ExecutionEnvironment",
                "LambdaFunctionArn",
                "LambdaMemoryLimitInMB",
                "LambdaPreviousExecutionTimeInMilliseconds",
                "LambdaRemainingTimeInMilliseconds",
                "LambdaTimeGapBetweenInvokesInMilliseconds",
            ],
            str,
        ]
    ] = Field(default=None, alias="metadata")


class DeleteProfilingGroupRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")


class DescribeProfilingGroupRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")


class FindingsReportSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    profile_end_time: Optional[datetime] = Field(default=None, alias="profileEndTime")
    profile_start_time: Optional[datetime] = Field(
        default=None, alias="profileStartTime"
    )
    profiling_group_name: Optional[str] = Field(
        default=None, alias="profilingGroupName"
    )
    total_number_of_findings: Optional[int] = Field(
        default=None, alias="totalNumberOfFindings"
    )


class GetFindingsReportAccountSummaryRequestModel(BaseModel):
    daily_reports_only: Optional[bool] = Field(default=None, alias="dailyReportsOnly")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetNotificationConfigurationRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")


class GetPolicyRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")


class GetProfileRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")
    accept: Optional[str] = Field(default=None, alias="accept")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    max_depth: Optional[int] = Field(default=None, alias="maxDepth")
    period: Optional[str] = Field(default=None, alias="period")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")


class GetRecommendationsRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    profiling_group_name: str = Field(alias="profilingGroupName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    locale: Optional[str] = Field(default=None, alias="locale")


class ListFindingsReportsRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    profiling_group_name: str = Field(alias="profilingGroupName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    daily_reports_only: Optional[bool] = Field(default=None, alias="dailyReportsOnly")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListProfileTimesRequestModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    period: Literal["P1D", "PT1H", "PT5M"] = Field(alias="period")
    profiling_group_name: str = Field(alias="profilingGroupName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    order_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="orderBy"
    )


class ProfileTimeModel(BaseModel):
    start: Optional[datetime] = Field(default=None, alias="start")


class ListProfilingGroupsRequestModel(BaseModel):
    include_description: Optional[bool] = Field(
        default=None, alias="includeDescription"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MatchModel(BaseModel):
    frame_address: Optional[str] = Field(default=None, alias="frameAddress")
    target_frames_index: Optional[int] = Field(default=None, alias="targetFramesIndex")
    threshold_breach_value: Optional[float] = Field(
        default=None, alias="thresholdBreachValue"
    )


class PatternModel(BaseModel):
    counters_to_aggregate: Optional[List[str]] = Field(
        default=None, alias="countersToAggregate"
    )
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    resolution_steps: Optional[str] = Field(default=None, alias="resolutionSteps")
    target_frames: Optional[List[List[str]]] = Field(default=None, alias="targetFrames")
    threshold_percent: Optional[float] = Field(default=None, alias="thresholdPercent")


class PostAgentProfileRequestModel(BaseModel):
    agent_profile: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="agentProfile"
    )
    content_type: str = Field(alias="contentType")
    profiling_group_name: str = Field(alias="profilingGroupName")
    profile_token: Optional[str] = Field(default=None, alias="profileToken")


class PutPermissionRequestModel(BaseModel):
    action_group: Literal["agentPermissions"] = Field(alias="actionGroup")
    principals: Sequence[str] = Field(alias="principals")
    profiling_group_name: str = Field(alias="profilingGroupName")
    revision_id: Optional[str] = Field(default=None, alias="revisionId")


class RemoveNotificationChannelRequestModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    profiling_group_name: str = Field(alias="profilingGroupName")


class RemovePermissionRequestModel(BaseModel):
    action_group: Literal["agentPermissions"] = Field(alias="actionGroup")
    profiling_group_name: str = Field(alias="profilingGroupName")
    revision_id: str = Field(alias="revisionId")


class SubmitFeedbackRequestModel(BaseModel):
    anomaly_instance_id: str = Field(alias="anomalyInstanceId")
    profiling_group_name: str = Field(alias="profilingGroupName")
    type: Literal["Negative", "Positive"] = Field(alias="type")
    comment: Optional[str] = Field(default=None, alias="comment")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AddNotificationChannelsRequestModel(BaseModel):
    channels: Sequence[ChannelModel] = Field(alias="channels")
    profiling_group_name: str = Field(alias="profilingGroupName")


class NotificationConfigurationModel(BaseModel):
    channels: Optional[List[ChannelModel]] = Field(default=None, alias="channels")


class GetPolicyResponseModel(BaseModel):
    policy: str = Field(alias="policy")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProfileResponseModel(BaseModel):
    content_encoding: str = Field(alias="contentEncoding")
    content_type: str = Field(alias="contentType")
    profile: Type[StreamingBody] = Field(alias="profile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPermissionResponseModel(BaseModel):
    policy: str = Field(alias="policy")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemovePermissionResponseModel(BaseModel):
    policy: str = Field(alias="policy")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigureAgentResponseModel(BaseModel):
    configuration: AgentConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfilingGroupRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    profiling_group_name: str = Field(alias="profilingGroupName")
    agent_orchestration_config: Optional[AgentOrchestrationConfigModel] = Field(
        default=None, alias="agentOrchestrationConfig"
    )
    compute_platform: Optional[Literal["AWSLambda", "Default"]] = Field(
        default=None, alias="computePlatform"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateProfilingGroupRequestModel(BaseModel):
    agent_orchestration_config: AgentOrchestrationConfigModel = Field(
        alias="agentOrchestrationConfig"
    )
    profiling_group_name: str = Field(alias="profilingGroupName")


class ProfilingStatusModel(BaseModel):
    latest_agent_orchestrated_at: Optional[datetime] = Field(
        default=None, alias="latestAgentOrchestratedAt"
    )
    latest_agent_profile_reported_at: Optional[datetime] = Field(
        default=None, alias="latestAgentProfileReportedAt"
    )
    latest_aggregated_profile: Optional[AggregatedProfileTimeModel] = Field(
        default=None, alias="latestAggregatedProfile"
    )


class AnomalyInstanceModel(BaseModel):
    id: str = Field(alias="id")
    start_time: datetime = Field(alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    user_feedback: Optional[UserFeedbackModel] = Field(
        default=None, alias="userFeedback"
    )


class BatchGetFrameMetricDataRequestModel(BaseModel):
    profiling_group_name: str = Field(alias="profilingGroupName")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    frame_metrics: Optional[Sequence[FrameMetricModel]] = Field(
        default=None, alias="frameMetrics"
    )
    period: Optional[str] = Field(default=None, alias="period")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    target_resolution: Optional[Literal["P1D", "PT1H", "PT5M"]] = Field(
        default=None, alias="targetResolution"
    )


class FrameMetricDatumModel(BaseModel):
    frame_metric: FrameMetricModel = Field(alias="frameMetric")
    values: List[float] = Field(alias="values")


class GetFindingsReportAccountSummaryResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    report_summaries: List[FindingsReportSummaryModel] = Field(alias="reportSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsReportsResponseModel(BaseModel):
    findings_report_summaries: List[FindingsReportSummaryModel] = Field(
        alias="findingsReportSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfileTimesRequestListProfileTimesPaginateModel(BaseModel):
    end_time: Union[datetime, str] = Field(alias="endTime")
    period: Literal["P1D", "PT1H", "PT5M"] = Field(alias="period")
    profiling_group_name: str = Field(alias="profilingGroupName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    order_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="orderBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProfileTimesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    profile_times: List[ProfileTimeModel] = Field(alias="profileTimes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationModel(BaseModel):
    all_matches_count: int = Field(alias="allMatchesCount")
    all_matches_sum: float = Field(alias="allMatchesSum")
    end_time: datetime = Field(alias="endTime")
    pattern: PatternModel = Field(alias="pattern")
    start_time: datetime = Field(alias="startTime")
    top_matches: List[MatchModel] = Field(alias="topMatches")


class AddNotificationChannelsResponseModel(BaseModel):
    notification_configuration: NotificationConfigurationModel = Field(
        alias="notificationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNotificationConfigurationResponseModel(BaseModel):
    notification_configuration: NotificationConfigurationModel = Field(
        alias="notificationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveNotificationChannelResponseModel(BaseModel):
    notification_configuration: NotificationConfigurationModel = Field(
        alias="notificationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProfilingGroupDescriptionModel(BaseModel):
    agent_orchestration_config: Optional[AgentOrchestrationConfigModel] = Field(
        default=None, alias="agentOrchestrationConfig"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    compute_platform: Optional[Literal["AWSLambda", "Default"]] = Field(
        default=None, alias="computePlatform"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    name: Optional[str] = Field(default=None, alias="name")
    profiling_status: Optional[ProfilingStatusModel] = Field(
        default=None, alias="profilingStatus"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class AnomalyModel(BaseModel):
    instances: List[AnomalyInstanceModel] = Field(alias="instances")
    metric: MetricModel = Field(alias="metric")
    reason: str = Field(alias="reason")


class BatchGetFrameMetricDataResponseModel(BaseModel):
    end_time: datetime = Field(alias="endTime")
    end_times: List[TimestampStructureModel] = Field(alias="endTimes")
    frame_metric_data: List[FrameMetricDatumModel] = Field(alias="frameMetricData")
    resolution: Literal["P1D", "PT1H", "PT5M"] = Field(alias="resolution")
    start_time: datetime = Field(alias="startTime")
    unprocessed_end_times: Dict[str, List[TimestampStructureModel]] = Field(
        alias="unprocessedEndTimes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfilingGroupResponseModel(BaseModel):
    profiling_group: ProfilingGroupDescriptionModel = Field(alias="profilingGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProfilingGroupResponseModel(BaseModel):
    profiling_group: ProfilingGroupDescriptionModel = Field(alias="profilingGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfilingGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    profiling_group_names: List[str] = Field(alias="profilingGroupNames")
    profiling_groups: List[ProfilingGroupDescriptionModel] = Field(
        alias="profilingGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProfilingGroupResponseModel(BaseModel):
    profiling_group: ProfilingGroupDescriptionModel = Field(alias="profilingGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationsResponseModel(BaseModel):
    anomalies: List[AnomalyModel] = Field(alias="anomalies")
    profile_end_time: datetime = Field(alias="profileEndTime")
    profile_start_time: datetime = Field(alias="profileStartTime")
    profiling_group_name: str = Field(alias="profilingGroupName")
    recommendations: List[RecommendationModel] = Field(alias="recommendations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
