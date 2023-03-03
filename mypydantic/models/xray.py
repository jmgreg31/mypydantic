# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AliasModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    type: Optional[str] = Field(default=None, alias="Type")


class AnnotationValueModel(BaseModel):
    number_value: Optional[float] = Field(default=None, alias="NumberValue")
    boolean_value: Optional[bool] = Field(default=None, alias="BooleanValue")
    string_value: Optional[str] = Field(default=None, alias="StringValue")


class ServiceIdModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    type: Optional[str] = Field(default=None, alias="Type")


class AvailabilityZoneDetailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class BackendConnectionErrorsModel(BaseModel):
    timeout_count: Optional[int] = Field(default=None, alias="TimeoutCount")
    connection_refused_count: Optional[int] = Field(
        default=None, alias="ConnectionRefusedCount"
    )
    http_code4_xxcount: Optional[int] = Field(default=None, alias="HTTPCode4XXCount")
    http_code5_xxcount: Optional[int] = Field(default=None, alias="HTTPCode5XXCount")
    unknown_host_count: Optional[int] = Field(default=None, alias="UnknownHostCount")
    other_count: Optional[int] = Field(default=None, alias="OtherCount")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class BatchGetTracesRequestModel(BaseModel):
    trace_ids: Sequence[str] = Field(alias="TraceIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class InsightsConfigurationModel(BaseModel):
    insights_enabled: Optional[bool] = Field(default=None, alias="InsightsEnabled")
    notifications_enabled: Optional[bool] = Field(
        default=None, alias="NotificationsEnabled"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class SamplingRuleModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    priority: int = Field(alias="Priority")
    fixed_rate: float = Field(alias="FixedRate")
    reservoir_size: int = Field(alias="ReservoirSize")
    service_name: str = Field(alias="ServiceName")
    service_type: str = Field(alias="ServiceType")
    host: str = Field(alias="Host")
    http_method: str = Field(alias="HTTPMethod")
    url_path: str = Field(alias="URLPath")
    version: int = Field(alias="Version")
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    rule_arn: Optional[str] = Field(default=None, alias="RuleARN")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")


class DeleteGroupRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")


class DeleteResourcePolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")


class DeleteSamplingRuleRequestModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    rule_arn: Optional[str] = Field(default=None, alias="RuleARN")


class ErrorStatisticsModel(BaseModel):
    throttle_count: Optional[int] = Field(default=None, alias="ThrottleCount")
    other_count: Optional[int] = Field(default=None, alias="OtherCount")
    total_count: Optional[int] = Field(default=None, alias="TotalCount")


class FaultStatisticsModel(BaseModel):
    other_count: Optional[int] = Field(default=None, alias="OtherCount")
    total_count: Optional[int] = Field(default=None, alias="TotalCount")


class HistogramEntryModel(BaseModel):
    value: Optional[float] = Field(default=None, alias="Value")
    count: Optional[int] = Field(default=None, alias="Count")


class EncryptionConfigModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    status: Optional[Literal["ACTIVE", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    type: Optional[Literal["KMS", "NONE"]] = Field(default=None, alias="Type")


class RootCauseExceptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    message: Optional[str] = Field(default=None, alias="Message")


class ForecastStatisticsModel(BaseModel):
    fault_count_high: Optional[int] = Field(default=None, alias="FaultCountHigh")
    fault_count_low: Optional[int] = Field(default=None, alias="FaultCountLow")


class GetGroupRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")


class GetGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetInsightEventsRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetInsightImpactGraphRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetInsightRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")


class GetInsightSummariesRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    states: Optional[Sequence[Literal["ACTIVE", "CLOSED"]]] = Field(
        default=None, alias="States"
    )
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetSamplingRulesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetSamplingStatisticSummariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SamplingStatisticSummaryModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    request_count: Optional[int] = Field(default=None, alias="RequestCount")
    borrow_count: Optional[int] = Field(default=None, alias="BorrowCount")
    sampled_count: Optional[int] = Field(default=None, alias="SampledCount")


class SamplingStatisticsDocumentModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    client_id: str = Field(alias="ClientID")
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    request_count: int = Field(alias="RequestCount")
    sampled_count: int = Field(alias="SampledCount")
    borrow_count: Optional[int] = Field(default=None, alias="BorrowCount")


class SamplingTargetDocumentModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    fixed_rate: Optional[float] = Field(default=None, alias="FixedRate")
    reservoir_quota: Optional[int] = Field(default=None, alias="ReservoirQuota")
    reservoir_quota_ttl: Optional[datetime] = Field(
        default=None, alias="ReservoirQuotaTTL"
    )
    interval: Optional[int] = Field(default=None, alias="Interval")


class UnprocessedStatisticsModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class GetServiceGraphRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTimeSeriesServiceStatisticsRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    entity_selector_expression: Optional[str] = Field(
        default=None, alias="EntitySelectorExpression"
    )
    period: Optional[int] = Field(default=None, alias="Period")
    forecast_statistics: Optional[bool] = Field(
        default=None, alias="ForecastStatistics"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTraceGraphRequestModel(BaseModel):
    trace_ids: Sequence[str] = Field(alias="TraceIds")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SamplingStrategyModel(BaseModel):
    name: Optional[Literal["FixedRate", "PartialScan"]] = Field(
        default=None, alias="Name"
    )
    value: Optional[float] = Field(default=None, alias="Value")


class HttpModel(BaseModel):
    http_url: Optional[str] = Field(default=None, alias="HttpURL")
    http_status: Optional[int] = Field(default=None, alias="HttpStatus")
    http_method: Optional[str] = Field(default=None, alias="HttpMethod")
    user_agent: Optional[str] = Field(default=None, alias="UserAgent")
    client_ip: Optional[str] = Field(default=None, alias="ClientIp")


class RequestImpactStatisticsModel(BaseModel):
    fault_count: Optional[int] = Field(default=None, alias="FaultCount")
    ok_count: Optional[int] = Field(default=None, alias="OkCount")
    total_count: Optional[int] = Field(default=None, alias="TotalCount")


class InsightImpactGraphEdgeModel(BaseModel):
    reference_id: Optional[int] = Field(default=None, alias="ReferenceId")


class InstanceIdDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class ListResourcePoliciesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResourcePolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_document: Optional[str] = Field(default=None, alias="PolicyDocument")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PutEncryptionConfigRequestModel(BaseModel):
    type: Literal["KMS", "NONE"] = Field(alias="Type")
    key_id: Optional[str] = Field(default=None, alias="KeyId")


class PutResourcePolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")
    bypass_policy_lockout_check: Optional[bool] = Field(
        default=None, alias="BypassPolicyLockoutCheck"
    )


class PutTraceSegmentsRequestModel(BaseModel):
    trace_segment_documents: Sequence[str] = Field(alias="TraceSegmentDocuments")


class UnprocessedTraceSegmentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class ResourceARNDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="ARN")


class ResponseTimeRootCauseEntityModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    coverage: Optional[float] = Field(default=None, alias="Coverage")
    remote: Optional[bool] = Field(default=None, alias="Remote")


class SamplingRuleUpdateModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    rule_arn: Optional[str] = Field(default=None, alias="RuleARN")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    priority: Optional[int] = Field(default=None, alias="Priority")
    fixed_rate: Optional[float] = Field(default=None, alias="FixedRate")
    reservoir_size: Optional[int] = Field(default=None, alias="ReservoirSize")
    host: Optional[str] = Field(default=None, alias="Host")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_type: Optional[str] = Field(default=None, alias="ServiceType")
    http_method: Optional[str] = Field(default=None, alias="HTTPMethod")
    url_path: Optional[str] = Field(default=None, alias="URLPath")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")


class SegmentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    document: Optional[str] = Field(default=None, alias="Document")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AnomalousServiceModel(BaseModel):
    service_id: Optional[ServiceIdModel] = Field(default=None, alias="ServiceId")


class TraceUserModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    service_ids: Optional[List[ServiceIdModel]] = Field(
        default=None, alias="ServiceIds"
    )


class ValueWithServiceIdsModel(BaseModel):
    annotation_value: Optional[AnnotationValueModel] = Field(
        default=None, alias="AnnotationValue"
    )
    service_ids: Optional[List[ServiceIdModel]] = Field(
        default=None, alias="ServiceIds"
    )


class TelemetryRecordModel(BaseModel):
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    segments_received_count: Optional[int] = Field(
        default=None, alias="SegmentsReceivedCount"
    )
    segments_sent_count: Optional[int] = Field(default=None, alias="SegmentsSentCount")
    segments_spillover_count: Optional[int] = Field(
        default=None, alias="SegmentsSpilloverCount"
    )
    segments_rejected_count: Optional[int] = Field(
        default=None, alias="SegmentsRejectedCount"
    )
    backend_connection_errors: Optional[BackendConnectionErrorsModel] = Field(
        default=None, alias="BackendConnectionErrors"
    )


class BatchGetTracesRequestBatchGetTracesPaginateModel(BaseModel):
    trace_ids: Sequence[str] = Field(alias="TraceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetGroupsRequestGetGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSamplingRulesRequestGetSamplingRulesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetServiceGraphRequestGetServiceGraphPaginateModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateModel(
    BaseModel
):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    entity_selector_expression: Optional[str] = Field(
        default=None, alias="EntitySelectorExpression"
    )
    period: Optional[int] = Field(default=None, alias="Period")
    forecast_statistics: Optional[bool] = Field(
        default=None, alias="ForecastStatistics"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTraceGraphRequestGetTraceGraphPaginateModel(BaseModel):
    trace_ids: Sequence[str] = Field(alias="TraceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcePoliciesRequestListResourcePoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GroupSummaryModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    insights_configuration: Optional[InsightsConfigurationModel] = Field(
        default=None, alias="InsightsConfiguration"
    )


class GroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    insights_configuration: Optional[InsightsConfigurationModel] = Field(
        default=None, alias="InsightsConfiguration"
    )


class UpdateGroupRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    insights_configuration: Optional[InsightsConfigurationModel] = Field(
        default=None, alias="InsightsConfiguration"
    )


class CreateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    insights_configuration: Optional[InsightsConfigurationModel] = Field(
        default=None, alias="InsightsConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateSamplingRuleRequestModel(BaseModel):
    sampling_rule: SamplingRuleModel = Field(alias="SamplingRule")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class SamplingRuleRecordModel(BaseModel):
    sampling_rule: Optional[SamplingRuleModel] = Field(
        default=None, alias="SamplingRule"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    modified_at: Optional[datetime] = Field(default=None, alias="ModifiedAt")


class EdgeStatisticsModel(BaseModel):
    ok_count: Optional[int] = Field(default=None, alias="OkCount")
    error_statistics: Optional[ErrorStatisticsModel] = Field(
        default=None, alias="ErrorStatistics"
    )
    fault_statistics: Optional[FaultStatisticsModel] = Field(
        default=None, alias="FaultStatistics"
    )
    total_count: Optional[int] = Field(default=None, alias="TotalCount")
    total_response_time: Optional[float] = Field(
        default=None, alias="TotalResponseTime"
    )


class ServiceStatisticsModel(BaseModel):
    ok_count: Optional[int] = Field(default=None, alias="OkCount")
    error_statistics: Optional[ErrorStatisticsModel] = Field(
        default=None, alias="ErrorStatistics"
    )
    fault_statistics: Optional[FaultStatisticsModel] = Field(
        default=None, alias="FaultStatistics"
    )
    total_count: Optional[int] = Field(default=None, alias="TotalCount")
    total_response_time: Optional[float] = Field(
        default=None, alias="TotalResponseTime"
    )


class GetEncryptionConfigResultModel(BaseModel):
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEncryptionConfigResultModel(BaseModel):
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ErrorRootCauseEntityModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    exceptions: Optional[List[RootCauseExceptionModel]] = Field(
        default=None, alias="Exceptions"
    )
    remote: Optional[bool] = Field(default=None, alias="Remote")


class FaultRootCauseEntityModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    exceptions: Optional[List[RootCauseExceptionModel]] = Field(
        default=None, alias="Exceptions"
    )
    remote: Optional[bool] = Field(default=None, alias="Remote")


class GetSamplingStatisticSummariesResultModel(BaseModel):
    sampling_statistic_summaries: List[SamplingStatisticSummaryModel] = Field(
        alias="SamplingStatisticSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSamplingTargetsRequestModel(BaseModel):
    sampling_statistics_documents: Sequence[SamplingStatisticsDocumentModel] = Field(
        alias="SamplingStatisticsDocuments"
    )


class GetSamplingTargetsResultModel(BaseModel):
    sampling_target_documents: List[SamplingTargetDocumentModel] = Field(
        alias="SamplingTargetDocuments"
    )
    last_rule_modification: datetime = Field(alias="LastRuleModification")
    unprocessed_statistics: List[UnprocessedStatisticsModel] = Field(
        alias="UnprocessedStatistics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTraceSummariesRequestGetTraceSummariesPaginateModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    time_range_type: Optional[Literal["Event", "TraceId"]] = Field(
        default=None, alias="TimeRangeType"
    )
    sampling: Optional[bool] = Field(default=None, alias="Sampling")
    sampling_strategy: Optional[SamplingStrategyModel] = Field(
        default=None, alias="SamplingStrategy"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTraceSummariesRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    time_range_type: Optional[Literal["Event", "TraceId"]] = Field(
        default=None, alias="TimeRangeType"
    )
    sampling: Optional[bool] = Field(default=None, alias="Sampling")
    sampling_strategy: Optional[SamplingStrategyModel] = Field(
        default=None, alias="SamplingStrategy"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class InsightImpactGraphServiceModel(BaseModel):
    reference_id: Optional[int] = Field(default=None, alias="ReferenceId")
    type: Optional[str] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    edges: Optional[List[InsightImpactGraphEdgeModel]] = Field(
        default=None, alias="Edges"
    )


class ListResourcePoliciesResultModel(BaseModel):
    resource_policies: List[ResourcePolicyModel] = Field(alias="ResourcePolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResultModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutTraceSegmentsResultModel(BaseModel):
    unprocessed_trace_segments: List[UnprocessedTraceSegmentModel] = Field(
        alias="UnprocessedTraceSegments"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResponseTimeRootCauseServiceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    type: Optional[str] = Field(default=None, alias="Type")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    entity_path: Optional[List[ResponseTimeRootCauseEntityModel]] = Field(
        default=None, alias="EntityPath"
    )
    inferred: Optional[bool] = Field(default=None, alias="Inferred")


class UpdateSamplingRuleRequestModel(BaseModel):
    sampling_rule_update: SamplingRuleUpdateModel = Field(alias="SamplingRuleUpdate")


class TraceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    duration: Optional[float] = Field(default=None, alias="Duration")
    limit_exceeded: Optional[bool] = Field(default=None, alias="LimitExceeded")
    segments: Optional[List[SegmentModel]] = Field(default=None, alias="Segments")


class InsightEventModel(BaseModel):
    summary: Optional[str] = Field(default=None, alias="Summary")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    client_request_impact_statistics: Optional[RequestImpactStatisticsModel] = Field(
        default=None, alias="ClientRequestImpactStatistics"
    )
    root_cause_service_request_impact_statistics: Optional[
        RequestImpactStatisticsModel
    ] = Field(default=None, alias="RootCauseServiceRequestImpactStatistics")
    top_anomalous_services: Optional[List[AnomalousServiceModel]] = Field(
        default=None, alias="TopAnomalousServices"
    )


class InsightSummaryModel(BaseModel):
    insight_id: Optional[str] = Field(default=None, alias="InsightId")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    root_cause_service_id: Optional[ServiceIdModel] = Field(
        default=None, alias="RootCauseServiceId"
    )
    categories: Optional[List[Literal["FAULT"]]] = Field(
        default=None, alias="Categories"
    )
    state: Optional[Literal["ACTIVE", "CLOSED"]] = Field(default=None, alias="State")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    summary: Optional[str] = Field(default=None, alias="Summary")
    client_request_impact_statistics: Optional[RequestImpactStatisticsModel] = Field(
        default=None, alias="ClientRequestImpactStatistics"
    )
    root_cause_service_request_impact_statistics: Optional[
        RequestImpactStatisticsModel
    ] = Field(default=None, alias="RootCauseServiceRequestImpactStatistics")
    top_anomalous_services: Optional[List[AnomalousServiceModel]] = Field(
        default=None, alias="TopAnomalousServices"
    )
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class InsightModel(BaseModel):
    insight_id: Optional[str] = Field(default=None, alias="InsightId")
    group_arn: Optional[str] = Field(default=None, alias="GroupARN")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    root_cause_service_id: Optional[ServiceIdModel] = Field(
        default=None, alias="RootCauseServiceId"
    )
    categories: Optional[List[Literal["FAULT"]]] = Field(
        default=None, alias="Categories"
    )
    state: Optional[Literal["ACTIVE", "CLOSED"]] = Field(default=None, alias="State")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    summary: Optional[str] = Field(default=None, alias="Summary")
    client_request_impact_statistics: Optional[RequestImpactStatisticsModel] = Field(
        default=None, alias="ClientRequestImpactStatistics"
    )
    root_cause_service_request_impact_statistics: Optional[
        RequestImpactStatisticsModel
    ] = Field(default=None, alias="RootCauseServiceRequestImpactStatistics")
    top_anomalous_services: Optional[List[AnomalousServiceModel]] = Field(
        default=None, alias="TopAnomalousServices"
    )


class PutTelemetryRecordsRequestModel(BaseModel):
    telemetry_records: Sequence[TelemetryRecordModel] = Field(alias="TelemetryRecords")
    ec2_instance_id: Optional[str] = Field(default=None, alias="EC2InstanceId")
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")


class GetGroupsResultModel(BaseModel):
    groups: List[GroupSummaryModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResultModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupResultModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupResultModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSamplingRuleResultModel(BaseModel):
    sampling_rule_record: SamplingRuleRecordModel = Field(alias="SamplingRuleRecord")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSamplingRuleResultModel(BaseModel):
    sampling_rule_record: SamplingRuleRecordModel = Field(alias="SamplingRuleRecord")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSamplingRulesResultModel(BaseModel):
    sampling_rule_records: List[SamplingRuleRecordModel] = Field(
        alias="SamplingRuleRecords"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSamplingRuleResultModel(BaseModel):
    sampling_rule_record: SamplingRuleRecordModel = Field(alias="SamplingRuleRecord")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EdgeModel(BaseModel):
    reference_id: Optional[int] = Field(default=None, alias="ReferenceId")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    summary_statistics: Optional[EdgeStatisticsModel] = Field(
        default=None, alias="SummaryStatistics"
    )
    response_time_histogram: Optional[List[HistogramEntryModel]] = Field(
        default=None, alias="ResponseTimeHistogram"
    )
    aliases: Optional[List[AliasModel]] = Field(default=None, alias="Aliases")
    edge_type: Optional[str] = Field(default=None, alias="EdgeType")
    received_event_age_histogram: Optional[List[HistogramEntryModel]] = Field(
        default=None, alias="ReceivedEventAgeHistogram"
    )


class TimeSeriesServiceStatisticsModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    edge_summary_statistics: Optional[EdgeStatisticsModel] = Field(
        default=None, alias="EdgeSummaryStatistics"
    )
    service_summary_statistics: Optional[ServiceStatisticsModel] = Field(
        default=None, alias="ServiceSummaryStatistics"
    )
    service_forecast_statistics: Optional[ForecastStatisticsModel] = Field(
        default=None, alias="ServiceForecastStatistics"
    )
    response_time_histogram: Optional[List[HistogramEntryModel]] = Field(
        default=None, alias="ResponseTimeHistogram"
    )


class ErrorRootCauseServiceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    type: Optional[str] = Field(default=None, alias="Type")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    entity_path: Optional[List[ErrorRootCauseEntityModel]] = Field(
        default=None, alias="EntityPath"
    )
    inferred: Optional[bool] = Field(default=None, alias="Inferred")


class FaultRootCauseServiceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    type: Optional[str] = Field(default=None, alias="Type")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    entity_path: Optional[List[FaultRootCauseEntityModel]] = Field(
        default=None, alias="EntityPath"
    )
    inferred: Optional[bool] = Field(default=None, alias="Inferred")


class GetInsightImpactGraphResultModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    service_graph_start_time: datetime = Field(alias="ServiceGraphStartTime")
    service_graph_end_time: datetime = Field(alias="ServiceGraphEndTime")
    services: List[InsightImpactGraphServiceModel] = Field(alias="Services")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResponseTimeRootCauseModel(BaseModel):
    services: Optional[List[ResponseTimeRootCauseServiceModel]] = Field(
        default=None, alias="Services"
    )
    client_impacting: Optional[bool] = Field(default=None, alias="ClientImpacting")


class BatchGetTracesResultModel(BaseModel):
    traces: List[TraceModel] = Field(alias="Traces")
    unprocessed_trace_ids: List[str] = Field(alias="UnprocessedTraceIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightEventsResultModel(BaseModel):
    insight_events: List[InsightEventModel] = Field(alias="InsightEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightSummariesResultModel(BaseModel):
    insight_summaries: List[InsightSummaryModel] = Field(alias="InsightSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightResultModel(BaseModel):
    insight: InsightModel = Field(alias="Insight")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServiceModel(BaseModel):
    reference_id: Optional[int] = Field(default=None, alias="ReferenceId")
    name: Optional[str] = Field(default=None, alias="Name")
    names: Optional[List[str]] = Field(default=None, alias="Names")
    root: Optional[bool] = Field(default=None, alias="Root")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    type: Optional[str] = Field(default=None, alias="Type")
    state: Optional[str] = Field(default=None, alias="State")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    edges: Optional[List[EdgeModel]] = Field(default=None, alias="Edges")
    summary_statistics: Optional[ServiceStatisticsModel] = Field(
        default=None, alias="SummaryStatistics"
    )
    duration_histogram: Optional[List[HistogramEntryModel]] = Field(
        default=None, alias="DurationHistogram"
    )
    response_time_histogram: Optional[List[HistogramEntryModel]] = Field(
        default=None, alias="ResponseTimeHistogram"
    )


class GetTimeSeriesServiceStatisticsResultModel(BaseModel):
    time_series_service_statistics: List[TimeSeriesServiceStatisticsModel] = Field(
        alias="TimeSeriesServiceStatistics"
    )
    contains_old_group_versions: bool = Field(alias="ContainsOldGroupVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ErrorRootCauseModel(BaseModel):
    services: Optional[List[ErrorRootCauseServiceModel]] = Field(
        default=None, alias="Services"
    )
    client_impacting: Optional[bool] = Field(default=None, alias="ClientImpacting")


class FaultRootCauseModel(BaseModel):
    services: Optional[List[FaultRootCauseServiceModel]] = Field(
        default=None, alias="Services"
    )
    client_impacting: Optional[bool] = Field(default=None, alias="ClientImpacting")


class GetServiceGraphResultModel(BaseModel):
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    services: List[ServiceModel] = Field(alias="Services")
    contains_old_group_versions: bool = Field(alias="ContainsOldGroupVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTraceGraphResultModel(BaseModel):
    services: List[ServiceModel] = Field(alias="Services")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TraceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    duration: Optional[float] = Field(default=None, alias="Duration")
    response_time: Optional[float] = Field(default=None, alias="ResponseTime")
    has_fault: Optional[bool] = Field(default=None, alias="HasFault")
    has_error: Optional[bool] = Field(default=None, alias="HasError")
    has_throttle: Optional[bool] = Field(default=None, alias="HasThrottle")
    is_partial: Optional[bool] = Field(default=None, alias="IsPartial")
    http: Optional[HttpModel] = Field(default=None, alias="Http")
    annotations: Optional[Dict[str, List[ValueWithServiceIdsModel]]] = Field(
        default=None, alias="Annotations"
    )
    users: Optional[List[TraceUserModel]] = Field(default=None, alias="Users")
    service_ids: Optional[List[ServiceIdModel]] = Field(
        default=None, alias="ServiceIds"
    )
    resource_arns: Optional[List[ResourceARNDetailModel]] = Field(
        default=None, alias="ResourceARNs"
    )
    instance_ids: Optional[List[InstanceIdDetailModel]] = Field(
        default=None, alias="InstanceIds"
    )
    availability_zones: Optional[List[AvailabilityZoneDetailModel]] = Field(
        default=None, alias="AvailabilityZones"
    )
    entry_point: Optional[ServiceIdModel] = Field(default=None, alias="EntryPoint")
    fault_root_causes: Optional[List[FaultRootCauseModel]] = Field(
        default=None, alias="FaultRootCauses"
    )
    error_root_causes: Optional[List[ErrorRootCauseModel]] = Field(
        default=None, alias="ErrorRootCauses"
    )
    response_time_root_causes: Optional[List[ResponseTimeRootCauseModel]] = Field(
        default=None, alias="ResponseTimeRootCauses"
    )
    revision: Optional[int] = Field(default=None, alias="Revision")
    matched_event_time: Optional[datetime] = Field(
        default=None, alias="MatchedEventTime"
    )


class GetTraceSummariesResultModel(BaseModel):
    trace_summaries: List[TraceSummaryModel] = Field(alias="TraceSummaries")
    approximate_time: datetime = Field(alias="ApproximateTime")
    traces_processed_count: int = Field(alias="TracesProcessedCount")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
