# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountInsightHealthModel(BaseModel):
    open_proactive_insights: Optional[int] = Field(
        default=None, alias="OpenProactiveInsights"
    )
    open_reactive_insights: Optional[int] = Field(
        default=None, alias="OpenReactiveInsights"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AmazonCodeGuruProfilerIntegrationModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class AnomalyReportedTimeRangeModel(BaseModel):
    open_time: datetime = Field(alias="OpenTime")
    close_time: Optional[datetime] = Field(default=None, alias="CloseTime")


class AnomalyResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")


class AnomalySourceMetadataModel(BaseModel):
    source: Optional[str] = Field(default=None, alias="Source")
    source_resource_name: Optional[str] = Field(
        default=None, alias="SourceResourceName"
    )
    source_resource_type: Optional[str] = Field(
        default=None, alias="SourceResourceType"
    )


class AnomalyTimeRangeModel(BaseModel):
    start_time: datetime = Field(alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class CloudFormationCollectionFilterModel(BaseModel):
    stack_names: Optional[List[str]] = Field(default=None, alias="StackNames")


class CloudFormationCollectionModel(BaseModel):
    stack_names: Optional[List[str]] = Field(default=None, alias="StackNames")


class CloudFormationCostEstimationResourceCollectionFilterModel(BaseModel):
    stack_names: Optional[List[str]] = Field(default=None, alias="StackNames")


class InsightHealthModel(BaseModel):
    open_proactive_insights: Optional[int] = Field(
        default=None, alias="OpenProactiveInsights"
    )
    open_reactive_insights: Optional[int] = Field(
        default=None, alias="OpenReactiveInsights"
    )
    mean_time_to_recover_in_milliseconds: Optional[int] = Field(
        default=None, alias="MeanTimeToRecoverInMilliseconds"
    )


class TimestampMetricValuePairModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    metric_value: Optional[float] = Field(default=None, alias="MetricValue")


class CloudWatchMetricsDimensionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class TagCostEstimationResourceCollectionFilterModel(BaseModel):
    app_boundary_key: str = Field(alias="AppBoundaryKey")
    tag_values: List[str] = Field(alias="TagValues")


class CostEstimationTimeRangeModel(BaseModel):
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class DeleteInsightRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeAccountOverviewRequestModel(BaseModel):
    from_time: Union[datetime, str] = Field(alias="FromTime")
    to_time: Optional[Union[datetime, str]] = Field(default=None, alias="ToTime")


class DescribeAnomalyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class DescribeFeedbackRequestModel(BaseModel):
    insight_id: Optional[str] = Field(default=None, alias="InsightId")


class InsightFeedbackModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    feedback: Optional[
        Literal[
            "ALERT_TOO_SENSITIVE",
            "DATA_INCORRECT",
            "DATA_NOISY_ANOMALY",
            "RECOMMENDATION_USEFUL",
            "VALID_COLLECTION",
        ]
    ] = Field(default=None, alias="Feedback")


class DescribeInsightRequestModel(BaseModel):
    id: str = Field(alias="Id")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class DescribeOrganizationHealthRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )


class DescribeOrganizationOverviewRequestModel(BaseModel):
    from_time: Union[datetime, str] = Field(alias="FromTime")
    to_time: Optional[Union[datetime, str]] = Field(default=None, alias="ToTime")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeOrganizationResourceCollectionHealthRequestModel(BaseModel):
    organization_resource_collection_type: Literal[
        "AWS_ACCOUNT", "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="OrganizationResourceCollectionType")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeResourceCollectionHealthRequestModel(BaseModel):
    resource_collection_type: Literal[
        "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="ResourceCollectionType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EndTimeRangeModel(BaseModel):
    from_time: Optional[Union[datetime, str]] = Field(default=None, alias="FromTime")
    to_time: Optional[Union[datetime, str]] = Field(default=None, alias="ToTime")


class EventResourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")


class EventTimeRangeModel(BaseModel):
    from_time: Union[datetime, str] = Field(alias="FromTime")
    to_time: Union[datetime, str] = Field(alias="ToTime")


class GetCostEstimationRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ServiceResourceCostModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    state: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(default=None, alias="State")
    count: Optional[int] = Field(default=None, alias="Count")
    unit_cost: Optional[float] = Field(default=None, alias="UnitCost")
    cost: Optional[float] = Field(default=None, alias="Cost")


class GetResourceCollectionRequestModel(BaseModel):
    resource_collection_type: Literal[
        "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="ResourceCollectionType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class InsightTimeRangeModel(BaseModel):
    start_time: datetime = Field(alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class ServiceCollectionModel(BaseModel):
    service_names: Optional[
        Sequence[
            Literal[
                "API_GATEWAY",
                "APPLICATION_ELB",
                "AUTO_SCALING_GROUP",
                "CLOUD_FRONT",
                "DYNAMO_DB",
                "EC2",
                "ECS",
                "EKS",
                "ELASTIC_BEANSTALK",
                "ELASTI_CACHE",
                "ELB",
                "ES",
                "KINESIS",
                "LAMBDA",
                "NAT_GATEWAY",
                "NETWORK_ELB",
                "RDS",
                "REDSHIFT",
                "ROUTE_53",
                "S3",
                "SAGE_MAKER",
                "SNS",
                "SQS",
                "STEP_FUNCTIONS",
                "SWF",
            ]
        ]
    ] = Field(default=None, alias="ServiceNames")


class StartTimeRangeModel(BaseModel):
    from_time: Optional[Union[datetime, str]] = Field(default=None, alias="FromTime")
    to_time: Optional[Union[datetime, str]] = Field(default=None, alias="ToTime")


class ListAnomalousLogGroupsRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInsightsOngoingStatusFilterModel(BaseModel):
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")


class ListMonitoredResourcesFiltersModel(BaseModel):
    resource_permission: Literal["FULL_PERMISSION", "MISSING_PERMISSION"] = Field(
        alias="ResourcePermission"
    )
    resource_type_filters: Sequence[
        Literal[
            "CLOUDFRONT_DISTRIBUTION",
            "DYNAMODB_TABLE",
            "EC2_NAT_GATEWAY",
            "ECS_CLUSTER",
            "ECS_SERVICE",
            "EKS_CLUSTER",
            "ELASTICACHE_CACHE_CLUSTER",
            "ELASTICSEARCH_DOMAIN",
            "ELASTIC_BEANSTALK_ENVIRONMENT",
            "ELASTIC_LOAD_BALANCER_LOAD_BALANCER",
            "ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER",
            "ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP",
            "KINESIS_STREAM",
            "LAMBDA_FUNCTION",
            "LOG_GROUPS",
            "OPEN_SEARCH_SERVICE_DOMAIN",
            "RDS_DB_CLUSTER",
            "RDS_DB_INSTANCE",
            "REDSHIFT_CLUSTER",
            "ROUTE53_HEALTH_CHECK",
            "ROUTE53_HOSTED_ZONE",
            "S3_BUCKET",
            "SAGEMAKER_ENDPOINT",
            "SNS_TOPIC",
            "SQS_QUEUE",
            "STEP_FUNCTIONS_ACTIVITY",
            "STEP_FUNCTIONS_STATE_MACHINE",
        ]
    ] = Field(alias="ResourceTypeFilters")


class ListNotificationChannelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRecommendationsRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    locale: Optional[
        Literal[
            "DE_DE",
            "EN_GB",
            "EN_US",
            "ES_ES",
            "FR_FR",
            "IT_IT",
            "JA_JP",
            "KO_KR",
            "PT_BR",
            "ZH_CN",
            "ZH_TW",
        ]
    ] = Field(default=None, alias="Locale")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class LogAnomalyClassModel(BaseModel):
    log_stream_name: Optional[str] = Field(default=None, alias="LogStreamName")
    log_anomaly_type: Optional[
        Literal[
            "BLOCK_FORMAT",
            "FORMAT",
            "HTTP_CODE",
            "KEYWORD",
            "KEYWORD_TOKEN",
            "NEW_FIELD_NAME",
            "NUMERICAL_NAN",
            "NUMERICAL_POINT",
        ]
    ] = Field(default=None, alias="LogAnomalyType")
    log_anomaly_token: Optional[str] = Field(default=None, alias="LogAnomalyToken")
    log_event_id: Optional[str] = Field(default=None, alias="LogEventId")
    explanation: Optional[str] = Field(default=None, alias="Explanation")
    number_of_log_lines_occurrences: Optional[int] = Field(
        default=None, alias="NumberOfLogLinesOccurrences"
    )
    log_event_timestamp: Optional[datetime] = Field(
        default=None, alias="LogEventTimestamp"
    )


class LogsAnomalyDetectionIntegrationConfigModel(BaseModel):
    opt_in_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptInStatus"
    )


class LogsAnomalyDetectionIntegrationModel(BaseModel):
    opt_in_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptInStatus"
    )


class NotificationFilterConfigModel(BaseModel):
    severities: Optional[Sequence[Literal["HIGH", "LOW", "MEDIUM"]]] = Field(
        default=None, alias="Severities"
    )
    message_types: Optional[
        Sequence[
            Literal[
                "CLOSED_INSIGHT",
                "NEW_ASSOCIATION",
                "NEW_INSIGHT",
                "NEW_RECOMMENDATION",
                "SEVERITY_UPGRADED",
            ]
        ]
    ] = Field(default=None, alias="MessageTypes")


class SnsChannelConfigModel(BaseModel):
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class OpsCenterIntegrationConfigModel(BaseModel):
    opt_in_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptInStatus"
    )


class OpsCenterIntegrationModel(BaseModel):
    opt_in_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OptInStatus"
    )


class PerformanceInsightsMetricDimensionGroupModel(BaseModel):
    group: Optional[str] = Field(default=None, alias="Group")
    dimensions: Optional[List[str]] = Field(default=None, alias="Dimensions")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PerformanceInsightsStatModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[float] = Field(default=None, alias="Value")


class PerformanceInsightsReferenceScalarModel(BaseModel):
    value: Optional[float] = Field(default=None, alias="Value")


class PredictionTimeRangeModel(BaseModel):
    start_time: datetime = Field(alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class RecommendationRelatedAnomalyResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")


class RecommendationRelatedCloudWatchMetricsSourceDetailModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class RecommendationRelatedEventResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")


class RemoveNotificationChannelRequestModel(BaseModel):
    id: str = Field(alias="Id")


class TagCollectionFilterModel(BaseModel):
    app_boundary_key: str = Field(alias="AppBoundaryKey")
    tag_values: List[str] = Field(alias="TagValues")


class TagCollectionModel(BaseModel):
    app_boundary_key: str = Field(alias="AppBoundaryKey")
    tag_values: List[str] = Field(alias="TagValues")


class ServiceInsightHealthModel(BaseModel):
    open_proactive_insights: Optional[int] = Field(
        default=None, alias="OpenProactiveInsights"
    )
    open_reactive_insights: Optional[int] = Field(
        default=None, alias="OpenReactiveInsights"
    )


class UpdateCloudFormationCollectionFilterModel(BaseModel):
    stack_names: Optional[Sequence[str]] = Field(default=None, alias="StackNames")


class UpdateTagCollectionFilterModel(BaseModel):
    app_boundary_key: str = Field(alias="AppBoundaryKey")
    tag_values: Sequence[str] = Field(alias="TagValues")


class AccountHealthModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    insight: Optional[AccountInsightHealthModel] = Field(default=None, alias="Insight")


class AddNotificationChannelResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountHealthResponseModel(BaseModel):
    open_reactive_insights: int = Field(alias="OpenReactiveInsights")
    open_proactive_insights: int = Field(alias="OpenProactiveInsights")
    metrics_analyzed: int = Field(alias="MetricsAnalyzed")
    resource_hours: int = Field(alias="ResourceHours")
    analyzed_resource_count: int = Field(alias="AnalyzedResourceCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountOverviewResponseModel(BaseModel):
    reactive_insights: int = Field(alias="ReactiveInsights")
    proactive_insights: int = Field(alias="ProactiveInsights")
    mean_time_to_recover_in_milliseconds: int = Field(
        alias="MeanTimeToRecoverInMilliseconds"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationHealthResponseModel(BaseModel):
    open_reactive_insights: int = Field(alias="OpenReactiveInsights")
    open_proactive_insights: int = Field(alias="OpenProactiveInsights")
    metrics_analyzed: int = Field(alias="MetricsAnalyzed")
    resource_hours: int = Field(alias="ResourceHours")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationOverviewResponseModel(BaseModel):
    reactive_insights: int = Field(alias="ReactiveInsights")
    proactive_insights: int = Field(alias="ProactiveInsights")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventSourcesConfigModel(BaseModel):
    amazon_code_guru_profiler: Optional[AmazonCodeGuruProfilerIntegrationModel] = Field(
        default=None, alias="AmazonCodeGuruProfiler"
    )


class CloudFormationHealthModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    insight: Optional[InsightHealthModel] = Field(default=None, alias="Insight")
    analyzed_resource_count: Optional[int] = Field(
        default=None, alias="AnalyzedResourceCount"
    )


class TagHealthModel(BaseModel):
    app_boundary_key: Optional[str] = Field(default=None, alias="AppBoundaryKey")
    tag_value: Optional[str] = Field(default=None, alias="TagValue")
    insight: Optional[InsightHealthModel] = Field(default=None, alias="Insight")
    analyzed_resource_count: Optional[int] = Field(
        default=None, alias="AnalyzedResourceCount"
    )


class CloudWatchMetricsDataSummaryModel(BaseModel):
    timestamp_metric_value_pair_list: Optional[
        List[TimestampMetricValuePairModel]
    ] = Field(default=None, alias="TimestampMetricValuePairList")
    status_code: Optional[Literal["Complete", "InternalError", "PartialData"]] = Field(
        default=None, alias="StatusCode"
    )


class CostEstimationResourceCollectionFilterModel(BaseModel):
    cloud_formation: Optional[
        CloudFormationCostEstimationResourceCollectionFilterModel
    ] = Field(default=None, alias="CloudFormation")
    tags: Optional[List[TagCostEstimationResourceCollectionFilterModel]] = Field(
        default=None, alias="Tags"
    )


class DescribeFeedbackResponseModel(BaseModel):
    insight_feedback: InsightFeedbackModel = Field(alias="InsightFeedback")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutFeedbackRequestModel(BaseModel):
    insight_feedback: Optional[InsightFeedbackModel] = Field(
        default=None, alias="InsightFeedback"
    )


class DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateModel(
    BaseModel
):
    organization_resource_collection_type: Literal[
        "AWS_ACCOUNT", "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="OrganizationResourceCollectionType")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateModel(
    BaseModel
):
    resource_collection_type: Literal[
        "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="ResourceCollectionType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCostEstimationRequestGetCostEstimationPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceCollectionRequestGetResourceCollectionPaginateModel(BaseModel):
    resource_collection_type: Literal[
        "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
    ] = Field(alias="ResourceCollectionType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotificationChannelsRequestListNotificationChannelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecommendationsRequestListRecommendationsPaginateModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    locale: Optional[
        Literal[
            "DE_DE",
            "EN_GB",
            "EN_US",
            "ES_ES",
            "FR_FR",
            "IT_IT",
            "JA_JP",
            "KO_KR",
            "PT_BR",
            "ZH_CN",
            "ZH_TW",
        ]
    ] = Field(default=None, alias="Locale")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInsightsClosedStatusFilterModel(BaseModel):
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    end_time_range: EndTimeRangeModel = Field(alias="EndTimeRange")


class ListAnomaliesForInsightFiltersModel(BaseModel):
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )


class ListInsightsAnyStatusFilterModel(BaseModel):
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    start_time_range: StartTimeRangeModel = Field(alias="StartTimeRange")


class ListMonitoredResourcesRequestListMonitoredResourcesPaginateModel(BaseModel):
    filters: Optional[ListMonitoredResourcesFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitoredResourcesRequestModel(BaseModel):
    filters: Optional[ListMonitoredResourcesFiltersModel] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LogAnomalyShowcaseModel(BaseModel):
    log_anomaly_classes: Optional[List[LogAnomalyClassModel]] = Field(
        default=None, alias="LogAnomalyClasses"
    )


class NotificationChannelConfigModel(BaseModel):
    sns: SnsChannelConfigModel = Field(alias="Sns")
    filters: Optional[NotificationFilterConfigModel] = Field(
        default=None, alias="Filters"
    )


class UpdateServiceIntegrationConfigModel(BaseModel):
    ops_center: Optional[OpsCenterIntegrationConfigModel] = Field(
        default=None, alias="OpsCenter"
    )
    logs_anomaly_detection: Optional[
        LogsAnomalyDetectionIntegrationConfigModel
    ] = Field(default=None, alias="LogsAnomalyDetection")


class ServiceIntegrationConfigModel(BaseModel):
    ops_center: Optional[OpsCenterIntegrationModel] = Field(
        default=None, alias="OpsCenter"
    )
    logs_anomaly_detection: Optional[LogsAnomalyDetectionIntegrationModel] = Field(
        default=None, alias="LogsAnomalyDetection"
    )


class PerformanceInsightsMetricQueryModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")
    group_by: Optional[PerformanceInsightsMetricDimensionGroupModel] = Field(
        default=None, alias="GroupBy"
    )
    filter: Optional[Dict[str, str]] = Field(default=None, alias="Filter")


class RecommendationRelatedAnomalySourceDetailModel(BaseModel):
    cloud_watch_metrics: Optional[
        List[RecommendationRelatedCloudWatchMetricsSourceDetailModel]
    ] = Field(default=None, alias="CloudWatchMetrics")


class RecommendationRelatedEventModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    resources: Optional[List[RecommendationRelatedEventResourceModel]] = Field(
        default=None, alias="Resources"
    )


class ResourceCollectionFilterModel(BaseModel):
    cloud_formation: Optional[CloudFormationCollectionFilterModel] = Field(
        default=None, alias="CloudFormation"
    )
    tags: Optional[List[TagCollectionFilterModel]] = Field(default=None, alias="Tags")


class ResourceCollectionModel(BaseModel):
    cloud_formation: Optional[CloudFormationCollectionModel] = Field(
        default=None, alias="CloudFormation"
    )
    tags: Optional[List[TagCollectionModel]] = Field(default=None, alias="Tags")


class ServiceHealthModel(BaseModel):
    service_name: Optional[
        Literal[
            "API_GATEWAY",
            "APPLICATION_ELB",
            "AUTO_SCALING_GROUP",
            "CLOUD_FRONT",
            "DYNAMO_DB",
            "EC2",
            "ECS",
            "EKS",
            "ELASTIC_BEANSTALK",
            "ELASTI_CACHE",
            "ELB",
            "ES",
            "KINESIS",
            "LAMBDA",
            "NAT_GATEWAY",
            "NETWORK_ELB",
            "RDS",
            "REDSHIFT",
            "ROUTE_53",
            "S3",
            "SAGE_MAKER",
            "SNS",
            "SQS",
            "STEP_FUNCTIONS",
            "SWF",
        ]
    ] = Field(default=None, alias="ServiceName")
    insight: Optional[ServiceInsightHealthModel] = Field(default=None, alias="Insight")
    analyzed_resource_count: Optional[int] = Field(
        default=None, alias="AnalyzedResourceCount"
    )


class UpdateResourceCollectionFilterModel(BaseModel):
    cloud_formation: Optional[UpdateCloudFormationCollectionFilterModel] = Field(
        default=None, alias="CloudFormation"
    )
    tags: Optional[Sequence[UpdateTagCollectionFilterModel]] = Field(
        default=None, alias="Tags"
    )


class DescribeEventSourcesConfigResponseModel(BaseModel):
    event_sources: EventSourcesConfigModel = Field(alias="EventSources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEventSourcesConfigRequestModel(BaseModel):
    event_sources: Optional[EventSourcesConfigModel] = Field(
        default=None, alias="EventSources"
    )


class CloudWatchMetricsDetailModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    dimensions: Optional[List[CloudWatchMetricsDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    stat: Optional[
        Literal[
            "Average", "Maximum", "Minimum", "SampleCount", "Sum", "p50", "p90", "p99"
        ]
    ] = Field(default=None, alias="Stat")
    unit: Optional[str] = Field(default=None, alias="Unit")
    period: Optional[int] = Field(default=None, alias="Period")
    metric_data_summary: Optional[CloudWatchMetricsDataSummaryModel] = Field(
        default=None, alias="MetricDataSummary"
    )


class GetCostEstimationResponseModel(BaseModel):
    resource_collection: CostEstimationResourceCollectionFilterModel = Field(
        alias="ResourceCollection"
    )
    status: Literal["COMPLETED", "ONGOING"] = Field(alias="Status")
    costs: List[ServiceResourceCostModel] = Field(alias="Costs")
    time_range: CostEstimationTimeRangeModel = Field(alias="TimeRange")
    total_cost: float = Field(alias="TotalCost")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCostEstimationRequestModel(BaseModel):
    resource_collection: CostEstimationResourceCollectionFilterModel = Field(
        alias="ResourceCollection"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    start_time_range: Optional[StartTimeRangeModel] = Field(
        default=None, alias="StartTimeRange"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    filters: Optional[ListAnomaliesForInsightFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnomaliesForInsightRequestModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    start_time_range: Optional[StartTimeRangeModel] = Field(
        default=None, alias="StartTimeRange"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    filters: Optional[ListAnomaliesForInsightFiltersModel] = Field(
        default=None, alias="Filters"
    )


class ListInsightsStatusFilterModel(BaseModel):
    ongoing: Optional[ListInsightsOngoingStatusFilterModel] = Field(
        default=None, alias="Ongoing"
    )
    closed: Optional[ListInsightsClosedStatusFilterModel] = Field(
        default=None, alias="Closed"
    )
    any: Optional[ListInsightsAnyStatusFilterModel] = Field(default=None, alias="Any")


class AnomalousLogGroupModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    impact_start_time: Optional[datetime] = Field(default=None, alias="ImpactStartTime")
    impact_end_time: Optional[datetime] = Field(default=None, alias="ImpactEndTime")
    number_of_log_lines_scanned: Optional[int] = Field(
        default=None, alias="NumberOfLogLinesScanned"
    )
    log_anomaly_showcases: Optional[List[LogAnomalyShowcaseModel]] = Field(
        default=None, alias="LogAnomalyShowcases"
    )


class AddNotificationChannelRequestModel(BaseModel):
    config: NotificationChannelConfigModel = Field(alias="Config")


class NotificationChannelModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    config: Optional[NotificationChannelConfigModel] = Field(
        default=None, alias="Config"
    )


class UpdateServiceIntegrationRequestModel(BaseModel):
    service_integration: UpdateServiceIntegrationConfigModel = Field(
        alias="ServiceIntegration"
    )


class DescribeServiceIntegrationResponseModel(BaseModel):
    service_integration: ServiceIntegrationConfigModel = Field(
        alias="ServiceIntegration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PerformanceInsightsReferenceMetricModel(BaseModel):
    metric_query: Optional[PerformanceInsightsMetricQueryModel] = Field(
        default=None, alias="MetricQuery"
    )


class RecommendationRelatedAnomalyModel(BaseModel):
    resources: Optional[List[RecommendationRelatedAnomalyResourceModel]] = Field(
        default=None, alias="Resources"
    )
    source_details: Optional[
        List[RecommendationRelatedAnomalySourceDetailModel]
    ] = Field(default=None, alias="SourceDetails")
    anomaly_id: Optional[str] = Field(default=None, alias="AnomalyId")


class GetResourceCollectionResponseModel(BaseModel):
    resource_collection: ResourceCollectionFilterModel = Field(
        alias="ResourceCollection"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventModel(BaseModel):
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    time: Optional[datetime] = Field(default=None, alias="Time")
    event_source: Optional[str] = Field(default=None, alias="EventSource")
    name: Optional[str] = Field(default=None, alias="Name")
    data_source: Optional[Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]] = Field(
        default=None, alias="DataSource"
    )
    event_class: Optional[
        Literal[
            "CONFIG_CHANGE",
            "DEPLOYMENT",
            "INFRASTRUCTURE",
            "SCHEMA_CHANGE",
            "SECURITY_CHANGE",
        ]
    ] = Field(default=None, alias="EventClass")
    resources: Optional[List[EventResourceModel]] = Field(
        default=None, alias="Resources"
    )


class ListEventsFiltersModel(BaseModel):
    insight_id: Optional[str] = Field(default=None, alias="InsightId")
    event_time_range: Optional[EventTimeRangeModel] = Field(
        default=None, alias="EventTimeRange"
    )
    event_class: Optional[
        Literal[
            "CONFIG_CHANGE",
            "DEPLOYMENT",
            "INFRASTRUCTURE",
            "SCHEMA_CHANGE",
            "SECURITY_CHANGE",
        ]
    ] = Field(default=None, alias="EventClass")
    event_source: Optional[str] = Field(default=None, alias="EventSource")
    data_source: Optional[Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]] = Field(
        default=None, alias="DataSource"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )


class MonitoredResourceIdentifierModel(BaseModel):
    monitored_resource_name: Optional[str] = Field(
        default=None, alias="MonitoredResourceName"
    )
    type: Optional[str] = Field(default=None, alias="Type")
    resource_permission: Optional[
        Literal["FULL_PERMISSION", "MISSING_PERMISSION"]
    ] = Field(default=None, alias="ResourcePermission")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )


class ProactiveInsightSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="PredictionTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )
    associated_resource_arns: Optional[List[str]] = Field(
        default=None, alias="AssociatedResourceArns"
    )


class ProactiveInsightModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="PredictionTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    ssm_ops_item_id: Optional[str] = Field(default=None, alias="SsmOpsItemId")
    description: Optional[str] = Field(default=None, alias="Description")


class ProactiveOrganizationInsightSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="PredictionTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )


class ReactiveInsightSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )
    associated_resource_arns: Optional[List[str]] = Field(
        default=None, alias="AssociatedResourceArns"
    )


class ReactiveInsightModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    ssm_ops_item_id: Optional[str] = Field(default=None, alias="SsmOpsItemId")
    description: Optional[str] = Field(default=None, alias="Description")


class ReactiveOrganizationInsightSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    organizational_unit_id: Optional[str] = Field(
        default=None, alias="OrganizationalUnitId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    insight_time_range: Optional[InsightTimeRangeModel] = Field(
        default=None, alias="InsightTimeRange"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )


class SearchInsightsFiltersModel(BaseModel):
    severities: Optional[Sequence[Literal["HIGH", "LOW", "MEDIUM"]]] = Field(
        default=None, alias="Severities"
    )
    statuses: Optional[Sequence[Literal["CLOSED", "ONGOING"]]] = Field(
        default=None, alias="Statuses"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )


class SearchOrganizationInsightsFiltersModel(BaseModel):
    severities: Optional[Sequence[Literal["HIGH", "LOW", "MEDIUM"]]] = Field(
        default=None, alias="Severities"
    )
    statuses: Optional[Sequence[Literal["CLOSED", "ONGOING"]]] = Field(
        default=None, alias="Statuses"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    service_collection: Optional[ServiceCollectionModel] = Field(
        default=None, alias="ServiceCollection"
    )


class DescribeOrganizationResourceCollectionHealthResponseModel(BaseModel):
    cloud_formation: List[CloudFormationHealthModel] = Field(alias="CloudFormation")
    service: List[ServiceHealthModel] = Field(alias="Service")
    account: List[AccountHealthModel] = Field(alias="Account")
    next_token: str = Field(alias="NextToken")
    tags: List[TagHealthModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourceCollectionHealthResponseModel(BaseModel):
    cloud_formation: List[CloudFormationHealthModel] = Field(alias="CloudFormation")
    service: List[ServiceHealthModel] = Field(alias="Service")
    next_token: str = Field(alias="NextToken")
    tags: List[TagHealthModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceCollectionRequestModel(BaseModel):
    action: Literal["ADD", "REMOVE"] = Field(alias="Action")
    resource_collection: UpdateResourceCollectionFilterModel = Field(
        alias="ResourceCollection"
    )


class ListInsightsRequestListInsightsPaginateModel(BaseModel):
    status_filter: ListInsightsStatusFilterModel = Field(alias="StatusFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInsightsRequestModel(BaseModel):
    status_filter: ListInsightsStatusFilterModel = Field(alias="StatusFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOrganizationInsightsRequestListOrganizationInsightsPaginateModel(BaseModel):
    status_filter: ListInsightsStatusFilterModel = Field(alias="StatusFilter")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationInsightsRequestModel(BaseModel):
    status_filter: ListInsightsStatusFilterModel = Field(alias="StatusFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    organizational_unit_ids: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAnomalousLogGroupsResponseModel(BaseModel):
    insight_id: str = Field(alias="InsightId")
    anomalous_log_groups: List[AnomalousLogGroupModel] = Field(
        alias="AnomalousLogGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotificationChannelsResponseModel(BaseModel):
    channels: List[NotificationChannelModel] = Field(alias="Channels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PerformanceInsightsReferenceComparisonValuesModel(BaseModel):
    reference_scalar: Optional[PerformanceInsightsReferenceScalarModel] = Field(
        default=None, alias="ReferenceScalar"
    )
    reference_metric: Optional[PerformanceInsightsReferenceMetricModel] = Field(
        default=None, alias="ReferenceMetric"
    )


class RecommendationModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    link: Optional[str] = Field(default=None, alias="Link")
    name: Optional[str] = Field(default=None, alias="Name")
    reason: Optional[str] = Field(default=None, alias="Reason")
    related_events: Optional[List[RecommendationRelatedEventModel]] = Field(
        default=None, alias="RelatedEvents"
    )
    related_anomalies: Optional[List[RecommendationRelatedAnomalyModel]] = Field(
        default=None, alias="RelatedAnomalies"
    )
    category: Optional[str] = Field(default=None, alias="Category")


class ListEventsResponseModel(BaseModel):
    events: List[EventModel] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventsRequestListEventsPaginateModel(BaseModel):
    filters: ListEventsFiltersModel = Field(alias="Filters")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventsRequestModel(BaseModel):
    filters: ListEventsFiltersModel = Field(alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class ListMonitoredResourcesResponseModel(BaseModel):
    monitored_resource_identifiers: List[MonitoredResourceIdentifierModel] = Field(
        alias="MonitoredResourceIdentifiers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInsightsResponseModel(BaseModel):
    proactive_insights: List[ProactiveInsightSummaryModel] = Field(
        alias="ProactiveInsights"
    )
    reactive_insights: List[ReactiveInsightSummaryModel] = Field(
        alias="ReactiveInsights"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchInsightsResponseModel(BaseModel):
    proactive_insights: List[ProactiveInsightSummaryModel] = Field(
        alias="ProactiveInsights"
    )
    reactive_insights: List[ReactiveInsightSummaryModel] = Field(
        alias="ReactiveInsights"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchOrganizationInsightsResponseModel(BaseModel):
    proactive_insights: List[ProactiveInsightSummaryModel] = Field(
        alias="ProactiveInsights"
    )
    reactive_insights: List[ReactiveInsightSummaryModel] = Field(
        alias="ReactiveInsights"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInsightResponseModel(BaseModel):
    proactive_insight: ProactiveInsightModel = Field(alias="ProactiveInsight")
    reactive_insight: ReactiveInsightModel = Field(alias="ReactiveInsight")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationInsightsResponseModel(BaseModel):
    proactive_insights: List[ProactiveOrganizationInsightSummaryModel] = Field(
        alias="ProactiveInsights"
    )
    reactive_insights: List[ReactiveOrganizationInsightSummaryModel] = Field(
        alias="ReactiveInsights"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchInsightsRequestModel(BaseModel):
    start_time_range: StartTimeRangeModel = Field(alias="StartTimeRange")
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    filters: Optional[SearchInsightsFiltersModel] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SearchInsightsRequestSearchInsightsPaginateModel(BaseModel):
    start_time_range: StartTimeRangeModel = Field(alias="StartTimeRange")
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    filters: Optional[SearchInsightsFiltersModel] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchOrganizationInsightsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")
    start_time_range: StartTimeRangeModel = Field(alias="StartTimeRange")
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    filters: Optional[SearchOrganizationInsightsFiltersModel] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateModel(
    BaseModel
):
    account_ids: Sequence[str] = Field(alias="AccountIds")
    start_time_range: StartTimeRangeModel = Field(alias="StartTimeRange")
    type: Literal["PROACTIVE", "REACTIVE"] = Field(alias="Type")
    filters: Optional[SearchOrganizationInsightsFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PerformanceInsightsReferenceDataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    comparison_values: Optional[
        PerformanceInsightsReferenceComparisonValuesModel
    ] = Field(default=None, alias="ComparisonValues")


class ListRecommendationsResponseModel(BaseModel):
    recommendations: List[RecommendationModel] = Field(alias="Recommendations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PerformanceInsightsMetricsDetailModel(BaseModel):
    metric_display_name: Optional[str] = Field(default=None, alias="MetricDisplayName")
    unit: Optional[str] = Field(default=None, alias="Unit")
    metric_query: Optional[PerformanceInsightsMetricQueryModel] = Field(
        default=None, alias="MetricQuery"
    )
    reference_data: Optional[List[PerformanceInsightsReferenceDataModel]] = Field(
        default=None, alias="ReferenceData"
    )
    stats_at_anomaly: Optional[List[PerformanceInsightsStatModel]] = Field(
        default=None, alias="StatsAtAnomaly"
    )
    stats_at_baseline: Optional[List[PerformanceInsightsStatModel]] = Field(
        default=None, alias="StatsAtBaseline"
    )


class AnomalySourceDetailsModel(BaseModel):
    cloud_watch_metrics: Optional[List[CloudWatchMetricsDetailModel]] = Field(
        default=None, alias="CloudWatchMetrics"
    )
    performance_insights_metrics: Optional[
        List[PerformanceInsightsMetricsDetailModel]
    ] = Field(default=None, alias="PerformanceInsightsMetrics")


class ProactiveAnomalySummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    update_time: Optional[datetime] = Field(default=None, alias="UpdateTime")
    anomaly_time_range: Optional[AnomalyTimeRangeModel] = Field(
        default=None, alias="AnomalyTimeRange"
    )
    anomaly_reported_time_range: Optional[AnomalyReportedTimeRangeModel] = Field(
        default=None, alias="AnomalyReportedTimeRange"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="PredictionTimeRange"
    )
    source_details: Optional[AnomalySourceDetailsModel] = Field(
        default=None, alias="SourceDetails"
    )
    associated_insight_id: Optional[str] = Field(
        default=None, alias="AssociatedInsightId"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    limit: Optional[float] = Field(default=None, alias="Limit")
    source_metadata: Optional[AnomalySourceMetadataModel] = Field(
        default=None, alias="SourceMetadata"
    )
    anomaly_resources: Optional[List[AnomalyResourceModel]] = Field(
        default=None, alias="AnomalyResources"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ProactiveAnomalyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    update_time: Optional[datetime] = Field(default=None, alias="UpdateTime")
    anomaly_time_range: Optional[AnomalyTimeRangeModel] = Field(
        default=None, alias="AnomalyTimeRange"
    )
    anomaly_reported_time_range: Optional[AnomalyReportedTimeRangeModel] = Field(
        default=None, alias="AnomalyReportedTimeRange"
    )
    prediction_time_range: Optional[PredictionTimeRangeModel] = Field(
        default=None, alias="PredictionTimeRange"
    )
    source_details: Optional[AnomalySourceDetailsModel] = Field(
        default=None, alias="SourceDetails"
    )
    associated_insight_id: Optional[str] = Field(
        default=None, alias="AssociatedInsightId"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    limit: Optional[float] = Field(default=None, alias="Limit")
    source_metadata: Optional[AnomalySourceMetadataModel] = Field(
        default=None, alias="SourceMetadata"
    )
    anomaly_resources: Optional[List[AnomalyResourceModel]] = Field(
        default=None, alias="AnomalyResources"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ReactiveAnomalySummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    anomaly_time_range: Optional[AnomalyTimeRangeModel] = Field(
        default=None, alias="AnomalyTimeRange"
    )
    anomaly_reported_time_range: Optional[AnomalyReportedTimeRangeModel] = Field(
        default=None, alias="AnomalyReportedTimeRange"
    )
    source_details: Optional[AnomalySourceDetailsModel] = Field(
        default=None, alias="SourceDetails"
    )
    associated_insight_id: Optional[str] = Field(
        default=None, alias="AssociatedInsightId"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    type: Optional[Literal["CAUSAL", "CONTEXTUAL"]] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    causal_anomaly_id: Optional[str] = Field(default=None, alias="CausalAnomalyId")
    anomaly_resources: Optional[List[AnomalyResourceModel]] = Field(
        default=None, alias="AnomalyResources"
    )


class ReactiveAnomalyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )
    status: Optional[Literal["CLOSED", "ONGOING"]] = Field(default=None, alias="Status")
    anomaly_time_range: Optional[AnomalyTimeRangeModel] = Field(
        default=None, alias="AnomalyTimeRange"
    )
    anomaly_reported_time_range: Optional[AnomalyReportedTimeRangeModel] = Field(
        default=None, alias="AnomalyReportedTimeRange"
    )
    source_details: Optional[AnomalySourceDetailsModel] = Field(
        default=None, alias="SourceDetails"
    )
    associated_insight_id: Optional[str] = Field(
        default=None, alias="AssociatedInsightId"
    )
    resource_collection: Optional[ResourceCollectionModel] = Field(
        default=None, alias="ResourceCollection"
    )
    type: Optional[Literal["CAUSAL", "CONTEXTUAL"]] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    causal_anomaly_id: Optional[str] = Field(default=None, alias="CausalAnomalyId")
    anomaly_resources: Optional[List[AnomalyResourceModel]] = Field(
        default=None, alias="AnomalyResources"
    )


class ListAnomaliesForInsightResponseModel(BaseModel):
    proactive_anomalies: List[ProactiveAnomalySummaryModel] = Field(
        alias="ProactiveAnomalies"
    )
    reactive_anomalies: List[ReactiveAnomalySummaryModel] = Field(
        alias="ReactiveAnomalies"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAnomalyResponseModel(BaseModel):
    proactive_anomaly: ProactiveAnomalyModel = Field(alias="ProactiveAnomaly")
    reactive_anomaly: ReactiveAnomalyModel = Field(alias="ReactiveAnomaly")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
