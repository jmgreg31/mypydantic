# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationComponentModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="ComponentName")
    component_remarks: Optional[str] = Field(default=None, alias="ComponentRemarks")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    os_type: Optional[Literal["LINUX", "WINDOWS"]] = Field(default=None, alias="OsType")
    tier: Optional[
        Literal[
            "ACTIVE_DIRECTORY",
            "CUSTOM",
            "DEFAULT",
            "DOT_NET_CORE",
            "DOT_NET_WEB",
            "DOT_NET_WEB_TIER",
            "DOT_NET_WORKER",
            "JAVA_JMX",
            "MYSQL",
            "ORACLE",
            "POSTGRESQL",
            "SAP_HANA_HIGH_AVAILABILITY",
            "SAP_HANA_MULTI_NODE",
            "SAP_HANA_SINGLE_NODE",
            "SHAREPOINT",
            "SQL_SERVER",
            "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
            "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
        ]
    ] = Field(default=None, alias="Tier")
    monitor: Optional[bool] = Field(default=None, alias="Monitor")
    detected_workload: Optional[
        Dict[
            Literal[
                "ACTIVE_DIRECTORY",
                "CUSTOM",
                "DEFAULT",
                "DOT_NET_CORE",
                "DOT_NET_WEB",
                "DOT_NET_WEB_TIER",
                "DOT_NET_WORKER",
                "JAVA_JMX",
                "MYSQL",
                "ORACLE",
                "POSTGRESQL",
                "SAP_HANA_HIGH_AVAILABILITY",
                "SAP_HANA_MULTI_NODE",
                "SAP_HANA_SINGLE_NODE",
                "SHAREPOINT",
                "SQL_SERVER",
                "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
                "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
            ],
            Dict[str, str],
        ]
    ] = Field(default=None, alias="DetectedWorkload")


class ApplicationInfoModel(BaseModel):
    resource_group_name: Optional[str] = Field(default=None, alias="ResourceGroupName")
    life_cycle: Optional[str] = Field(default=None, alias="LifeCycle")
    ops_item_s_ns_topic_arn: Optional[str] = Field(
        default=None, alias="OpsItemSNSTopicArn"
    )
    ops_center_enabled: Optional[bool] = Field(default=None, alias="OpsCenterEnabled")
    cwemonitor_enabled: Optional[bool] = Field(default=None, alias="CWEMonitorEnabled")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    auto_config_enabled: Optional[bool] = Field(default=None, alias="AutoConfigEnabled")
    discovery_type: Optional[Literal["ACCOUNT_BASED", "RESOURCE_GROUP_BASED"]] = Field(
        default=None, alias="DiscoveryType"
    )


class ConfigurationEventModel(BaseModel):
    monitored_resource_arn: Optional[str] = Field(
        default=None, alias="MonitoredResourceARN"
    )
    event_status: Optional[Literal["ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="EventStatus"
    )
    event_resource_type: Optional[
        Literal[
            "CLOUDFORMATION", "CLOUDWATCH_ALARM", "CLOUDWATCH_LOG", "SSM_ASSOCIATION"
        ]
    ] = Field(default=None, alias="EventResourceType")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    event_detail: Optional[str] = Field(default=None, alias="EventDetail")
    event_resource_name: Optional[str] = Field(default=None, alias="EventResourceName")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateComponentRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")
    resource_list: Sequence[str] = Field(alias="ResourceList")


class CreateLogPatternRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    pattern_set_name: str = Field(alias="PatternSetName")
    pattern_name: str = Field(alias="PatternName")
    pattern: str = Field(alias="Pattern")
    rank: int = Field(alias="Rank")


class LogPatternModel(BaseModel):
    pattern_set_name: Optional[str] = Field(default=None, alias="PatternSetName")
    pattern_name: Optional[str] = Field(default=None, alias="PatternName")
    pattern: Optional[str] = Field(default=None, alias="Pattern")
    rank: Optional[int] = Field(default=None, alias="Rank")


class DeleteApplicationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")


class DeleteComponentRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")


class DeleteLogPatternRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    pattern_set_name: str = Field(alias="PatternSetName")
    pattern_name: str = Field(alias="PatternName")


class DescribeApplicationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")


class DescribeComponentConfigurationRecommendationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")
    tier: Literal[
        "ACTIVE_DIRECTORY",
        "CUSTOM",
        "DEFAULT",
        "DOT_NET_CORE",
        "DOT_NET_WEB",
        "DOT_NET_WEB_TIER",
        "DOT_NET_WORKER",
        "JAVA_JMX",
        "MYSQL",
        "ORACLE",
        "POSTGRESQL",
        "SAP_HANA_HIGH_AVAILABILITY",
        "SAP_HANA_MULTI_NODE",
        "SAP_HANA_SINGLE_NODE",
        "SHAREPOINT",
        "SQL_SERVER",
        "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
        "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
    ] = Field(alias="Tier")


class DescribeComponentConfigurationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")


class DescribeComponentRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")


class DescribeLogPatternRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    pattern_set_name: str = Field(alias="PatternSetName")
    pattern_name: str = Field(alias="PatternName")


class DescribeObservationRequestModel(BaseModel):
    observation_id: str = Field(alias="ObservationId")


class ObservationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_arn: Optional[str] = Field(default=None, alias="SourceARN")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")
    line_time: Optional[datetime] = Field(default=None, alias="LineTime")
    log_text: Optional[str] = Field(default=None, alias="LogText")
    log_filter: Optional[Literal["ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="LogFilter"
    )
    metric_namespace: Optional[str] = Field(default=None, alias="MetricNamespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    unit: Optional[str] = Field(default=None, alias="Unit")
    value: Optional[float] = Field(default=None, alias="Value")
    cloud_watch_event_id: Optional[str] = Field(default=None, alias="CloudWatchEventId")
    cloud_watch_event_source: Optional[
        Literal["CODE_DEPLOY", "EC2", "HEALTH", "RDS"]
    ] = Field(default=None, alias="CloudWatchEventSource")
    cloud_watch_event_detail_type: Optional[str] = Field(
        default=None, alias="CloudWatchEventDetailType"
    )
    health_event_arn: Optional[str] = Field(default=None, alias="HealthEventArn")
    health_service: Optional[str] = Field(default=None, alias="HealthService")
    health_event_type_code: Optional[str] = Field(
        default=None, alias="HealthEventTypeCode"
    )
    health_event_type_category: Optional[str] = Field(
        default=None, alias="HealthEventTypeCategory"
    )
    health_event_description: Optional[str] = Field(
        default=None, alias="HealthEventDescription"
    )
    code_deploy_deployment_id: Optional[str] = Field(
        default=None, alias="CodeDeployDeploymentId"
    )
    code_deploy_deployment_group: Optional[str] = Field(
        default=None, alias="CodeDeployDeploymentGroup"
    )
    code_deploy_state: Optional[str] = Field(default=None, alias="CodeDeployState")
    code_deploy_application: Optional[str] = Field(
        default=None, alias="CodeDeployApplication"
    )
    code_deploy_instance_group_id: Optional[str] = Field(
        default=None, alias="CodeDeployInstanceGroupId"
    )
    ec2_state: Optional[str] = Field(default=None, alias="Ec2State")
    rds_event_categories: Optional[str] = Field(
        default=None, alias="RdsEventCategories"
    )
    rds_event_message: Optional[str] = Field(default=None, alias="RdsEventMessage")
    s3_event_name: Optional[str] = Field(default=None, alias="S3EventName")
    states_execution_arn: Optional[str] = Field(
        default=None, alias="StatesExecutionArn"
    )
    states_arn: Optional[str] = Field(default=None, alias="StatesArn")
    states_status: Optional[str] = Field(default=None, alias="StatesStatus")
    states_input: Optional[str] = Field(default=None, alias="StatesInput")
    ebs_event: Optional[str] = Field(default=None, alias="EbsEvent")
    ebs_result: Optional[str] = Field(default=None, alias="EbsResult")
    ebs_cause: Optional[str] = Field(default=None, alias="EbsCause")
    ebs_request_id: Optional[str] = Field(default=None, alias="EbsRequestId")
    xray_fault_percent: Optional[int] = Field(default=None, alias="XRayFaultPercent")
    xray_throttle_percent: Optional[int] = Field(
        default=None, alias="XRayThrottlePercent"
    )
    xray_error_percent: Optional[int] = Field(default=None, alias="XRayErrorPercent")
    xray_request_count: Optional[int] = Field(default=None, alias="XRayRequestCount")
    xray_request_average_latency: Optional[int] = Field(
        default=None, alias="XRayRequestAverageLatency"
    )
    xray_node_name: Optional[str] = Field(default=None, alias="XRayNodeName")
    xray_node_type: Optional[str] = Field(default=None, alias="XRayNodeType")


class DescribeProblemObservationsRequestModel(BaseModel):
    problem_id: str = Field(alias="ProblemId")


class DescribeProblemRequestModel(BaseModel):
    problem_id: str = Field(alias="ProblemId")


class ProblemModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    title: Optional[str] = Field(default=None, alias="Title")
    insights: Optional[str] = Field(default=None, alias="Insights")
    status: Optional[Literal["IGNORE", "PENDING", "RECURRING", "RESOLVED"]] = Field(
        default=None, alias="Status"
    )
    affected_resource: Optional[str] = Field(default=None, alias="AffectedResource")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    severity_level: Optional[Literal["High", "Informative", "Low", "Medium"]] = Field(
        default=None, alias="SeverityLevel"
    )
    resource_group_name: Optional[str] = Field(default=None, alias="ResourceGroupName")
    feedback: Optional[
        Dict[
            Literal["INSIGHTS_FEEDBACK"],
            Literal["NOT_SPECIFIED", "NOT_USEFUL", "USEFUL"],
        ]
    ] = Field(default=None, alias="Feedback")
    recurring_count: Optional[int] = Field(default=None, alias="RecurringCount")
    last_recurrence_time: Optional[datetime] = Field(
        default=None, alias="LastRecurrenceTime"
    )


class ListApplicationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListComponentsRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationHistoryRequestModel(BaseModel):
    resource_group_name: Optional[str] = Field(default=None, alias="ResourceGroupName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    event_status: Optional[Literal["ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="EventStatus"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLogPatternSetsRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLogPatternsRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    pattern_set_name: Optional[str] = Field(default=None, alias="PatternSetName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListProblemsRequestModel(BaseModel):
    resource_group_name: Optional[str] = Field(default=None, alias="ResourceGroupName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    component_name: Optional[str] = Field(default=None, alias="ComponentName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateApplicationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    ops_center_enabled: Optional[bool] = Field(default=None, alias="OpsCenterEnabled")
    cwemonitor_enabled: Optional[bool] = Field(default=None, alias="CWEMonitorEnabled")
    ops_item_s_ns_topic_arn: Optional[str] = Field(
        default=None, alias="OpsItemSNSTopicArn"
    )
    remove_s_ns_topic: Optional[bool] = Field(default=None, alias="RemoveSNSTopic")
    auto_config_enabled: Optional[bool] = Field(default=None, alias="AutoConfigEnabled")


class UpdateComponentConfigurationRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")
    monitor: Optional[bool] = Field(default=None, alias="Monitor")
    tier: Optional[
        Literal[
            "ACTIVE_DIRECTORY",
            "CUSTOM",
            "DEFAULT",
            "DOT_NET_CORE",
            "DOT_NET_WEB",
            "DOT_NET_WEB_TIER",
            "DOT_NET_WORKER",
            "JAVA_JMX",
            "MYSQL",
            "ORACLE",
            "POSTGRESQL",
            "SAP_HANA_HIGH_AVAILABILITY",
            "SAP_HANA_MULTI_NODE",
            "SAP_HANA_SINGLE_NODE",
            "SHAREPOINT",
            "SQL_SERVER",
            "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
            "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
        ]
    ] = Field(default=None, alias="Tier")
    component_configuration: Optional[str] = Field(
        default=None, alias="ComponentConfiguration"
    )
    auto_config_enabled: Optional[bool] = Field(default=None, alias="AutoConfigEnabled")


class UpdateComponentRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    component_name: str = Field(alias="ComponentName")
    new_component_name: Optional[str] = Field(default=None, alias="NewComponentName")
    resource_list: Optional[Sequence[str]] = Field(default=None, alias="ResourceList")


class UpdateLogPatternRequestModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    pattern_set_name: str = Field(alias="PatternSetName")
    pattern_name: str = Field(alias="PatternName")
    pattern: Optional[str] = Field(default=None, alias="Pattern")
    rank: Optional[int] = Field(default=None, alias="Rank")


class CreateApplicationRequestModel(BaseModel):
    resource_group_name: Optional[str] = Field(default=None, alias="ResourceGroupName")
    ops_center_enabled: Optional[bool] = Field(default=None, alias="OpsCenterEnabled")
    cwemonitor_enabled: Optional[bool] = Field(default=None, alias="CWEMonitorEnabled")
    ops_item_s_ns_topic_arn: Optional[str] = Field(
        default=None, alias="OpsItemSNSTopicArn"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    auto_config_enabled: Optional[bool] = Field(default=None, alias="AutoConfigEnabled")
    auto_create: Optional[bool] = Field(default=None, alias="AutoCreate")
    grouping_type: Optional[Literal["ACCOUNT_BASED"]] = Field(
        default=None, alias="GroupingType"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateApplicationResponseModel(BaseModel):
    application_info: ApplicationInfoModel = Field(alias="ApplicationInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationResponseModel(BaseModel):
    application_info: ApplicationInfoModel = Field(alias="ApplicationInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComponentConfigurationRecommendationResponseModel(BaseModel):
    component_configuration: str = Field(alias="ComponentConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComponentConfigurationResponseModel(BaseModel):
    monitor: bool = Field(alias="Monitor")
    tier: Literal[
        "ACTIVE_DIRECTORY",
        "CUSTOM",
        "DEFAULT",
        "DOT_NET_CORE",
        "DOT_NET_WEB",
        "DOT_NET_WEB_TIER",
        "DOT_NET_WORKER",
        "JAVA_JMX",
        "MYSQL",
        "ORACLE",
        "POSTGRESQL",
        "SAP_HANA_HIGH_AVAILABILITY",
        "SAP_HANA_MULTI_NODE",
        "SAP_HANA_SINGLE_NODE",
        "SHAREPOINT",
        "SQL_SERVER",
        "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
        "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
    ] = Field(alias="Tier")
    component_configuration: str = Field(alias="ComponentConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComponentResponseModel(BaseModel):
    application_component: ApplicationComponentModel = Field(
        alias="ApplicationComponent"
    )
    resource_list: List[str] = Field(alias="ResourceList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    application_info_list: List[ApplicationInfoModel] = Field(
        alias="ApplicationInfoList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComponentsResponseModel(BaseModel):
    application_component_list: List[ApplicationComponentModel] = Field(
        alias="ApplicationComponentList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationHistoryResponseModel(BaseModel):
    event_list: List[ConfigurationEventModel] = Field(alias="EventList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLogPatternSetsResponseModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    log_pattern_sets: List[str] = Field(alias="LogPatternSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application_info: ApplicationInfoModel = Field(alias="ApplicationInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLogPatternResponseModel(BaseModel):
    log_pattern: LogPatternModel = Field(alias="LogPattern")
    resource_group_name: str = Field(alias="ResourceGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLogPatternResponseModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    log_pattern: LogPatternModel = Field(alias="LogPattern")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLogPatternsResponseModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    log_patterns: List[LogPatternModel] = Field(alias="LogPatterns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLogPatternResponseModel(BaseModel):
    resource_group_name: str = Field(alias="ResourceGroupName")
    log_pattern: LogPatternModel = Field(alias="LogPattern")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeObservationResponseModel(BaseModel):
    observation: ObservationModel = Field(alias="Observation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RelatedObservationsModel(BaseModel):
    observation_list: Optional[List[ObservationModel]] = Field(
        default=None, alias="ObservationList"
    )


class DescribeProblemResponseModel(BaseModel):
    problem: ProblemModel = Field(alias="Problem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProblemsResponseModel(BaseModel):
    problem_list: List[ProblemModel] = Field(alias="ProblemList")
    next_token: str = Field(alias="NextToken")
    resource_group_name: str = Field(alias="ResourceGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProblemObservationsResponseModel(BaseModel):
    related_observations: RelatedObservationsModel = Field(alias="RelatedObservations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
