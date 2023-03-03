# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlarmHistoryItemModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_type: Optional[Literal["CompositeAlarm", "MetricAlarm"]] = Field(
        default=None, alias="AlarmType"
    )
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    history_item_type: Optional[
        Literal["Action", "ConfigurationUpdate", "StateUpdate"]
    ] = Field(default=None, alias="HistoryItemType")
    history_summary: Optional[str] = Field(default=None, alias="HistorySummary")
    history_data: Optional[str] = Field(default=None, alias="HistoryData")


class RangeModel(BaseModel):
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")


class DimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class CompositeAlarmModel(BaseModel):
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    alarm_actions: Optional[List[str]] = Field(default=None, alias="AlarmActions")
    alarm_arn: Optional[str] = Field(default=None, alias="AlarmArn")
    alarm_configuration_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="AlarmConfigurationUpdatedTimestamp"
    )
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_rule: Optional[str] = Field(default=None, alias="AlarmRule")
    insufficient_data_actions: Optional[List[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    okactions: Optional[List[str]] = Field(default=None, alias="OKActions")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    state_reason_data: Optional[str] = Field(default=None, alias="StateReasonData")
    state_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="StateUpdatedTimestamp"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    state_transitioned_timestamp: Optional[datetime] = Field(
        default=None, alias="StateTransitionedTimestamp"
    )
    actions_suppressed_by: Optional[
        Literal["Alarm", "ExtensionPeriod", "WaitPeriod"]
    ] = Field(default=None, alias="ActionsSuppressedBy")
    actions_suppressed_reason: Optional[str] = Field(
        default=None, alias="ActionsSuppressedReason"
    )
    actions_suppressor: Optional[str] = Field(default=None, alias="ActionsSuppressor")
    actions_suppressor_wait_period: Optional[int] = Field(
        default=None, alias="ActionsSuppressorWaitPeriod"
    )
    actions_suppressor_extension_period: Optional[int] = Field(
        default=None, alias="ActionsSuppressorExtensionPeriod"
    )


class DashboardEntryModel(BaseModel):
    dashboard_name: Optional[str] = Field(default=None, alias="DashboardName")
    dashboard_arn: Optional[str] = Field(default=None, alias="DashboardArn")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    size: Optional[int] = Field(default=None, alias="Size")


class DashboardValidationMessageModel(BaseModel):
    data_path: Optional[str] = Field(default=None, alias="DataPath")
    message: Optional[str] = Field(default=None, alias="Message")


class DatapointModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    sample_count: Optional[float] = Field(default=None, alias="SampleCount")
    average: Optional[float] = Field(default=None, alias="Average")
    sum: Optional[float] = Field(default=None, alias="Sum")
    minimum: Optional[float] = Field(default=None, alias="Minimum")
    maximum: Optional[float] = Field(default=None, alias="Maximum")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    extended_statistics: Optional[Dict[str, float]] = Field(
        default=None, alias="ExtendedStatistics"
    )


class DeleteAlarmsInputRequestModel(BaseModel):
    alarm_names: Sequence[str] = Field(alias="AlarmNames")


class DeleteDashboardsInputRequestModel(BaseModel):
    dashboard_names: Sequence[str] = Field(alias="DashboardNames")


class DeleteInsightRulesInputRequestModel(BaseModel):
    rule_names: Sequence[str] = Field(alias="RuleNames")


class PartialFailureModel(BaseModel):
    failure_resource: Optional[str] = Field(default=None, alias="FailureResource")
    exception_type: Optional[str] = Field(default=None, alias="ExceptionType")
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_description: Optional[str] = Field(default=None, alias="FailureDescription")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteMetricStreamInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeAlarmHistoryInputAlarmDescribeHistoryModel(BaseModel):
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    history_item_type: Optional[
        Literal["Action", "ConfigurationUpdate", "StateUpdate"]
    ] = Field(default=None, alias="HistoryItemType")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    scan_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="ScanBy"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAlarmHistoryInputRequestModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    history_item_type: Optional[
        Literal["Action", "ConfigurationUpdate", "StateUpdate"]
    ] = Field(default=None, alias="HistoryItemType")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    scan_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="ScanBy"
    )


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeAlarmsInputRequestModel(BaseModel):
    alarm_names: Optional[Sequence[str]] = Field(default=None, alias="AlarmNames")
    alarm_name_prefix: Optional[str] = Field(default=None, alias="AlarmNamePrefix")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    children_of_alarm_name: Optional[str] = Field(
        default=None, alias="ChildrenOfAlarmName"
    )
    parents_of_alarm_name: Optional[str] = Field(
        default=None, alias="ParentsOfAlarmName"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    action_prefix: Optional[str] = Field(default=None, alias="ActionPrefix")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInsightRulesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class InsightRuleModel(BaseModel):
    name: str = Field(alias="Name")
    state: str = Field(alias="State")
    schema_: str = Field(alias="Schema")
    definition: str = Field(alias="Definition")
    managed_rule: Optional[bool] = Field(default=None, alias="ManagedRule")


class DimensionFilterModel(BaseModel):
    name: str = Field(alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class DisableAlarmActionsInputRequestModel(BaseModel):
    alarm_names: Sequence[str] = Field(alias="AlarmNames")


class DisableInsightRulesInputRequestModel(BaseModel):
    rule_names: Sequence[str] = Field(alias="RuleNames")


class EnableAlarmActionsInputRequestModel(BaseModel):
    alarm_names: Sequence[str] = Field(alias="AlarmNames")


class EnableInsightRulesInputRequestModel(BaseModel):
    rule_names: Sequence[str] = Field(alias="RuleNames")


class GetDashboardInputRequestModel(BaseModel):
    dashboard_name: str = Field(alias="DashboardName")


class GetInsightRuleReportInputRequestModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    period: int = Field(alias="Period")
    max_contributor_count: Optional[int] = Field(
        default=None, alias="MaxContributorCount"
    )
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")
    order_by: Optional[str] = Field(default=None, alias="OrderBy")


class InsightRuleMetricDatapointModel(BaseModel):
    timestamp: datetime = Field(alias="Timestamp")
    unique_contributors: Optional[float] = Field(
        default=None, alias="UniqueContributors"
    )
    max_contributor_value: Optional[float] = Field(
        default=None, alias="MaxContributorValue"
    )
    sample_count: Optional[float] = Field(default=None, alias="SampleCount")
    average: Optional[float] = Field(default=None, alias="Average")
    sum: Optional[float] = Field(default=None, alias="Sum")
    minimum: Optional[float] = Field(default=None, alias="Minimum")
    maximum: Optional[float] = Field(default=None, alias="Maximum")


class LabelOptionsModel(BaseModel):
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class MessageDataModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    value: Optional[str] = Field(default=None, alias="Value")


class GetMetricStreamInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class MetricStreamFilterModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class GetMetricWidgetImageInputRequestModel(BaseModel):
    metric_widget: str = Field(alias="MetricWidget")
    output_format: Optional[str] = Field(default=None, alias="OutputFormat")


class InsightRuleContributorDatapointModel(BaseModel):
    timestamp: datetime = Field(alias="Timestamp")
    approximate_value: float = Field(alias="ApproximateValue")


class ListDashboardsInputRequestModel(BaseModel):
    dashboard_name_prefix: Optional[str] = Field(
        default=None, alias="DashboardNamePrefix"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListManagedInsightRulesInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMetricStreamsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MetricStreamEntryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    last_update_date: Optional[datetime] = Field(default=None, alias="LastUpdateDate")
    name: Optional[str] = Field(default=None, alias="Name")
    firehose_arn: Optional[str] = Field(default=None, alias="FirehoseArn")
    state: Optional[str] = Field(default=None, alias="State")
    output_format: Optional[Literal["json", "opentelemetry0.7"]] = Field(
        default=None, alias="OutputFormat"
    )


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ManagedRuleStateModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    state: str = Field(alias="State")


class StatisticSetModel(BaseModel):
    sample_count: float = Field(alias="SampleCount")
    sum: float = Field(alias="Sum")
    minimum: float = Field(alias="Minimum")
    maximum: float = Field(alias="Maximum")


class MetricStreamStatisticsMetricModel(BaseModel):
    namespace: str = Field(alias="Namespace")
    metric_name: str = Field(alias="MetricName")


class PutDashboardInputRequestModel(BaseModel):
    dashboard_name: str = Field(alias="DashboardName")
    dashboard_body: str = Field(alias="DashboardBody")


class ServiceResourceAlarmRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceMetricRequestModel(BaseModel):
    namespace: str = Field(alias="namespace")
    name: str = Field(alias="name")


class SetAlarmStateInputAlarmSetStateModel(BaseModel):
    state_value: Literal["ALARM", "INSUFFICIENT_DATA", "OK"] = Field(alias="StateValue")
    state_reason: str = Field(alias="StateReason")
    state_reason_data: Optional[str] = Field(default=None, alias="StateReasonData")


class SetAlarmStateInputRequestModel(BaseModel):
    alarm_name: str = Field(alias="AlarmName")
    state_value: Literal["ALARM", "INSUFFICIENT_DATA", "OK"] = Field(alias="StateValue")
    state_reason: str = Field(alias="StateReason")
    state_reason_data: Optional[str] = Field(default=None, alias="StateReasonData")


class StartMetricStreamsInputRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")


class StopMetricStreamsInputRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AnomalyDetectorConfigurationModel(BaseModel):
    excluded_time_ranges: Optional[List[RangeModel]] = Field(
        default=None, alias="ExcludedTimeRanges"
    )
    metric_timezone: Optional[str] = Field(default=None, alias="MetricTimezone")


class DescribeAlarmsForMetricInputRequestModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    namespace: str = Field(alias="Namespace")
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="Statistic")
    extended_statistic: Optional[str] = Field(default=None, alias="ExtendedStatistic")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    period: Optional[int] = Field(default=None, alias="Period")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")


class DescribeAnomalyDetectorsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    anomaly_detector_types: Optional[
        Sequence[Literal["METRIC_MATH", "SINGLE_METRIC"]]
    ] = Field(default=None, alias="AnomalyDetectorTypes")


class GetMetricStatisticsInputMetricGetStatisticsModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    period: int = Field(alias="Period")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    statistics: Optional[
        Sequence[Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]]
    ] = Field(default=None, alias="Statistics")
    extended_statistics: Optional[Sequence[str]] = Field(
        default=None, alias="ExtendedStatistics"
    )
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")


class GetMetricStatisticsInputRequestModel(BaseModel):
    namespace: str = Field(alias="Namespace")
    metric_name: str = Field(alias="MetricName")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    period: int = Field(alias="Period")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    statistics: Optional[
        Sequence[Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]]
    ] = Field(default=None, alias="Statistics")
    extended_statistics: Optional[Sequence[str]] = Field(
        default=None, alias="ExtendedStatistics"
    )
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")


class MetricModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )


class SingleMetricAnomalyDetectorModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    stat: Optional[str] = Field(default=None, alias="Stat")


class DeleteInsightRulesOutputModel(BaseModel):
    failures: List[PartialFailureModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAlarmHistoryOutputModel(BaseModel):
    alarm_history_items: List[AlarmHistoryItemModel] = Field(alias="AlarmHistoryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableInsightRulesOutputModel(BaseModel):
    failures: List[PartialFailureModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableInsightRulesOutputModel(BaseModel):
    failures: List[PartialFailureModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDashboardOutputModel(BaseModel):
    dashboard_arn: str = Field(alias="DashboardArn")
    dashboard_body: str = Field(alias="DashboardBody")
    dashboard_name: str = Field(alias="DashboardName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMetricStatisticsOutputModel(BaseModel):
    label: str = Field(alias="Label")
    datapoints: List[DatapointModel] = Field(alias="Datapoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMetricWidgetImageOutputModel(BaseModel):
    metric_widget_image: bytes = Field(alias="MetricWidgetImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDashboardsOutputModel(BaseModel):
    dashboard_entries: List[DashboardEntryModel] = Field(alias="DashboardEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDashboardOutputModel(BaseModel):
    dashboard_validation_messages: List[DashboardValidationMessageModel] = Field(
        alias="DashboardValidationMessages"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutManagedInsightRulesOutputModel(BaseModel):
    failures: List[PartialFailureModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMetricStreamOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    history_item_type: Optional[
        Literal["Action", "ConfigurationUpdate", "StateUpdate"]
    ] = Field(default=None, alias="HistoryItemType")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    scan_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="ScanBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAlarmsInputDescribeAlarmsPaginateModel(BaseModel):
    alarm_names: Optional[Sequence[str]] = Field(default=None, alias="AlarmNames")
    alarm_name_prefix: Optional[str] = Field(default=None, alias="AlarmNamePrefix")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    children_of_alarm_name: Optional[str] = Field(
        default=None, alias="ChildrenOfAlarmName"
    )
    parents_of_alarm_name: Optional[str] = Field(
        default=None, alias="ParentsOfAlarmName"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    action_prefix: Optional[str] = Field(default=None, alias="ActionPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    anomaly_detector_types: Optional[
        Sequence[Literal["METRIC_MATH", "SINGLE_METRIC"]]
    ] = Field(default=None, alias="AnomalyDetectorTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDashboardsInputListDashboardsPaginateModel(BaseModel):
    dashboard_name_prefix: Optional[str] = Field(
        default=None, alias="DashboardNamePrefix"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAlarmsInputAlarmExistsWaitModel(BaseModel):
    alarm_names: Optional[Sequence[str]] = Field(default=None, alias="AlarmNames")
    alarm_name_prefix: Optional[str] = Field(default=None, alias="AlarmNamePrefix")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    children_of_alarm_name: Optional[str] = Field(
        default=None, alias="ChildrenOfAlarmName"
    )
    parents_of_alarm_name: Optional[str] = Field(
        default=None, alias="ParentsOfAlarmName"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    action_prefix: Optional[str] = Field(default=None, alias="ActionPrefix")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAlarmsInputCompositeAlarmExistsWaitModel(BaseModel):
    alarm_names: Optional[Sequence[str]] = Field(default=None, alias="AlarmNames")
    alarm_name_prefix: Optional[str] = Field(default=None, alias="AlarmNamePrefix")
    alarm_types: Optional[Sequence[Literal["CompositeAlarm", "MetricAlarm"]]] = Field(
        default=None, alias="AlarmTypes"
    )
    children_of_alarm_name: Optional[str] = Field(
        default=None, alias="ChildrenOfAlarmName"
    )
    parents_of_alarm_name: Optional[str] = Field(
        default=None, alias="ParentsOfAlarmName"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    action_prefix: Optional[str] = Field(default=None, alias="ActionPrefix")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInsightRulesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    insight_rules: List[InsightRuleModel] = Field(alias="InsightRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMetricsInputListMetricsPaginateModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionFilterModel]] = Field(
        default=None, alias="Dimensions"
    )
    recently_active: Optional[Literal["PT3H"]] = Field(
        default=None, alias="RecentlyActive"
    )
    include_linked_accounts: Optional[bool] = Field(
        default=None, alias="IncludeLinkedAccounts"
    )
    owning_account: Optional[str] = Field(default=None, alias="OwningAccount")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMetricsInputRequestModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionFilterModel]] = Field(
        default=None, alias="Dimensions"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    recently_active: Optional[Literal["PT3H"]] = Field(
        default=None, alias="RecentlyActive"
    )
    include_linked_accounts: Optional[bool] = Field(
        default=None, alias="IncludeLinkedAccounts"
    )
    owning_account: Optional[str] = Field(default=None, alias="OwningAccount")


class MetricDataResultModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    label: Optional[str] = Field(default=None, alias="Label")
    timestamps: Optional[List[datetime]] = Field(default=None, alias="Timestamps")
    values: Optional[List[float]] = Field(default=None, alias="Values")
    status_code: Optional[
        Literal["Complete", "Forbidden", "InternalError", "PartialData"]
    ] = Field(default=None, alias="StatusCode")
    messages: Optional[List[MessageDataModel]] = Field(default=None, alias="Messages")


class InsightRuleContributorModel(BaseModel):
    keys: List[str] = Field(alias="Keys")
    approximate_aggregate_value: float = Field(alias="ApproximateAggregateValue")
    datapoints: List[InsightRuleContributorDatapointModel] = Field(alias="Datapoints")


class ListMetricStreamsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    entries: List[MetricStreamEntryModel] = Field(alias="Entries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ManagedRuleModel(BaseModel):
    template_name: str = Field(alias="TemplateName")
    resource_arn: str = Field(alias="ResourceARN")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PutCompositeAlarmInputRequestModel(BaseModel):
    alarm_name: str = Field(alias="AlarmName")
    alarm_rule: str = Field(alias="AlarmRule")
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    alarm_actions: Optional[Sequence[str]] = Field(default=None, alias="AlarmActions")
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    insufficient_data_actions: Optional[Sequence[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    okactions: Optional[Sequence[str]] = Field(default=None, alias="OKActions")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    actions_suppressor: Optional[str] = Field(default=None, alias="ActionsSuppressor")
    actions_suppressor_wait_period: Optional[int] = Field(
        default=None, alias="ActionsSuppressorWaitPeriod"
    )
    actions_suppressor_extension_period: Optional[int] = Field(
        default=None, alias="ActionsSuppressorExtensionPeriod"
    )


class PutInsightRuleInputRequestModel(BaseModel):
    rule_name: str = Field(alias="RuleName")
    rule_definition: str = Field(alias="RuleDefinition")
    rule_state: Optional[str] = Field(default=None, alias="RuleState")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ManagedRuleDescriptionModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    rule_state: Optional[ManagedRuleStateModel] = Field(default=None, alias="RuleState")


class MetricDatumModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")
    value: Optional[float] = Field(default=None, alias="Value")
    statistic_values: Optional[StatisticSetModel] = Field(
        default=None, alias="StatisticValues"
    )
    values: Optional[Sequence[float]] = Field(default=None, alias="Values")
    counts: Optional[Sequence[float]] = Field(default=None, alias="Counts")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    storage_resolution: Optional[int] = Field(default=None, alias="StorageResolution")


class MetricStreamStatisticsConfigurationModel(BaseModel):
    include_metrics: List[MetricStreamStatisticsMetricModel] = Field(
        alias="IncludeMetrics"
    )
    additional_statistics: List[str] = Field(alias="AdditionalStatistics")


class ListMetricsOutputModel(BaseModel):
    metrics: List[MetricModel] = Field(alias="Metrics")
    next_token: str = Field(alias="NextToken")
    owning_accounts: List[str] = Field(alias="OwningAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricStatModel(BaseModel):
    metric: MetricModel = Field(alias="Metric")
    period: int = Field(alias="Period")
    stat: str = Field(alias="Stat")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")


class GetMetricDataOutputModel(BaseModel):
    metric_data_results: List[MetricDataResultModel] = Field(alias="MetricDataResults")
    next_token: str = Field(alias="NextToken")
    messages: List[MessageDataModel] = Field(alias="Messages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightRuleReportOutputModel(BaseModel):
    key_labels: List[str] = Field(alias="KeyLabels")
    aggregation_statistic: str = Field(alias="AggregationStatistic")
    aggregate_value: float = Field(alias="AggregateValue")
    approximate_unique_count: int = Field(alias="ApproximateUniqueCount")
    contributors: List[InsightRuleContributorModel] = Field(alias="Contributors")
    metric_datapoints: List[InsightRuleMetricDatapointModel] = Field(
        alias="MetricDatapoints"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutManagedInsightRulesInputRequestModel(BaseModel):
    managed_rules: Sequence[ManagedRuleModel] = Field(alias="ManagedRules")


class ListManagedInsightRulesOutputModel(BaseModel):
    managed_rules: List[ManagedRuleDescriptionModel] = Field(alias="ManagedRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMetricDataInputRequestModel(BaseModel):
    namespace: str = Field(alias="Namespace")
    metric_data: Sequence[MetricDatumModel] = Field(alias="MetricData")


class GetMetricStreamOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    include_filters: List[MetricStreamFilterModel] = Field(alias="IncludeFilters")
    exclude_filters: List[MetricStreamFilterModel] = Field(alias="ExcludeFilters")
    firehose_arn: str = Field(alias="FirehoseArn")
    role_arn: str = Field(alias="RoleArn")
    state: str = Field(alias="State")
    creation_date: datetime = Field(alias="CreationDate")
    last_update_date: datetime = Field(alias="LastUpdateDate")
    output_format: Literal["json", "opentelemetry0.7"] = Field(alias="OutputFormat")
    statistics_configurations: List[MetricStreamStatisticsConfigurationModel] = Field(
        alias="StatisticsConfigurations"
    )
    include_linked_accounts_metrics: bool = Field(alias="IncludeLinkedAccountsMetrics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMetricStreamInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    firehose_arn: str = Field(alias="FirehoseArn")
    role_arn: str = Field(alias="RoleArn")
    output_format: Literal["json", "opentelemetry0.7"] = Field(alias="OutputFormat")
    include_filters: Optional[Sequence[MetricStreamFilterModel]] = Field(
        default=None, alias="IncludeFilters"
    )
    exclude_filters: Optional[Sequence[MetricStreamFilterModel]] = Field(
        default=None, alias="ExcludeFilters"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    statistics_configurations: Optional[
        Sequence[MetricStreamStatisticsConfigurationModel]
    ] = Field(default=None, alias="StatisticsConfigurations")
    include_linked_accounts_metrics: Optional[bool] = Field(
        default=None, alias="IncludeLinkedAccountsMetrics"
    )


class MetricDataQueryModel(BaseModel):
    id: str = Field(alias="Id")
    metric_stat: Optional[MetricStatModel] = Field(default=None, alias="MetricStat")
    expression: Optional[str] = Field(default=None, alias="Expression")
    label: Optional[str] = Field(default=None, alias="Label")
    return_data: Optional[bool] = Field(default=None, alias="ReturnData")
    period: Optional[int] = Field(default=None, alias="Period")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class GetMetricDataInputGetMetricDataPaginateModel(BaseModel):
    metric_data_queries: Sequence[MetricDataQueryModel] = Field(
        alias="MetricDataQueries"
    )
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    scan_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="ScanBy"
    )
    label_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="LabelOptions"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetMetricDataInputRequestModel(BaseModel):
    metric_data_queries: Sequence[MetricDataQueryModel] = Field(
        alias="MetricDataQueries"
    )
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    scan_by: Optional[Literal["TimestampAscending", "TimestampDescending"]] = Field(
        default=None, alias="ScanBy"
    )
    max_datapoints: Optional[int] = Field(default=None, alias="MaxDatapoints")
    label_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="LabelOptions"
    )


class MetricAlarmModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_arn: Optional[str] = Field(default=None, alias="AlarmArn")
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    alarm_configuration_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="AlarmConfigurationUpdatedTimestamp"
    )
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    okactions: Optional[List[str]] = Field(default=None, alias="OKActions")
    alarm_actions: Optional[List[str]] = Field(default=None, alias="AlarmActions")
    insufficient_data_actions: Optional[List[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    state_value: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="StateValue"
    )
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    state_reason_data: Optional[str] = Field(default=None, alias="StateReasonData")
    state_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="StateUpdatedTimestamp"
    )
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="Statistic")
    extended_statistic: Optional[str] = Field(default=None, alias="ExtendedStatistic")
    dimensions: Optional[List[DimensionModel]] = Field(default=None, alias="Dimensions")
    period: Optional[int] = Field(default=None, alias="Period")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    evaluation_periods: Optional[int] = Field(default=None, alias="EvaluationPeriods")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="DatapointsToAlarm")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    comparison_operator: Optional[
        Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "GreaterThanUpperThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanThreshold",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    treat_missing_data: Optional[str] = Field(default=None, alias="TreatMissingData")
    evaluate_low_sample_count_percentile: Optional[str] = Field(
        default=None, alias="EvaluateLowSampleCountPercentile"
    )
    metrics: Optional[List[MetricDataQueryModel]] = Field(default=None, alias="Metrics")
    threshold_metric_id: Optional[str] = Field(default=None, alias="ThresholdMetricId")
    evaluation_state: Optional[Literal["PARTIAL_DATA"]] = Field(
        default=None, alias="EvaluationState"
    )
    state_transitioned_timestamp: Optional[datetime] = Field(
        default=None, alias="StateTransitionedTimestamp"
    )


class MetricMathAnomalyDetectorModel(BaseModel):
    metric_data_queries: Optional[Sequence[MetricDataQueryModel]] = Field(
        default=None, alias="MetricDataQueries"
    )


class PutMetricAlarmInputMetricPutAlarmModel(BaseModel):
    alarm_name: str = Field(alias="AlarmName")
    evaluation_periods: int = Field(alias="EvaluationPeriods")
    comparison_operator: Literal[
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "GreaterThanUpperThreshold",
        "LessThanLowerOrGreaterThanUpperThreshold",
        "LessThanLowerThreshold",
        "LessThanOrEqualToThreshold",
        "LessThanThreshold",
    ] = Field(alias="ComparisonOperator")
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    okactions: Optional[Sequence[str]] = Field(default=None, alias="OKActions")
    alarm_actions: Optional[Sequence[str]] = Field(default=None, alias="AlarmActions")
    insufficient_data_actions: Optional[Sequence[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="Statistic")
    extended_statistic: Optional[str] = Field(default=None, alias="ExtendedStatistic")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    period: Optional[int] = Field(default=None, alias="Period")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="DatapointsToAlarm")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    treat_missing_data: Optional[str] = Field(default=None, alias="TreatMissingData")
    evaluate_low_sample_count_percentile: Optional[str] = Field(
        default=None, alias="EvaluateLowSampleCountPercentile"
    )
    metrics: Optional[Sequence[MetricDataQueryModel]] = Field(
        default=None, alias="Metrics"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    threshold_metric_id: Optional[str] = Field(default=None, alias="ThresholdMetricId")


class PutMetricAlarmInputRequestModel(BaseModel):
    alarm_name: str = Field(alias="AlarmName")
    evaluation_periods: int = Field(alias="EvaluationPeriods")
    comparison_operator: Literal[
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "GreaterThanUpperThreshold",
        "LessThanLowerOrGreaterThanUpperThreshold",
        "LessThanLowerThreshold",
        "LessThanOrEqualToThreshold",
        "LessThanThreshold",
    ] = Field(alias="ComparisonOperator")
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    okactions: Optional[Sequence[str]] = Field(default=None, alias="OKActions")
    alarm_actions: Optional[Sequence[str]] = Field(default=None, alias="AlarmActions")
    insufficient_data_actions: Optional[Sequence[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="Statistic")
    extended_statistic: Optional[str] = Field(default=None, alias="ExtendedStatistic")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    period: Optional[int] = Field(default=None, alias="Period")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="DatapointsToAlarm")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    treat_missing_data: Optional[str] = Field(default=None, alias="TreatMissingData")
    evaluate_low_sample_count_percentile: Optional[str] = Field(
        default=None, alias="EvaluateLowSampleCountPercentile"
    )
    metrics: Optional[Sequence[MetricDataQueryModel]] = Field(
        default=None, alias="Metrics"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    threshold_metric_id: Optional[str] = Field(default=None, alias="ThresholdMetricId")


class DescribeAlarmsForMetricOutputModel(BaseModel):
    metric_alarms: List[MetricAlarmModel] = Field(alias="MetricAlarms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAlarmsOutputModel(BaseModel):
    composite_alarms: List[CompositeAlarmModel] = Field(alias="CompositeAlarms")
    metric_alarms: List[MetricAlarmModel] = Field(alias="MetricAlarms")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AnomalyDetectorModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[List[DimensionModel]] = Field(default=None, alias="Dimensions")
    stat: Optional[str] = Field(default=None, alias="Stat")
    configuration: Optional[AnomalyDetectorConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    state_value: Optional[
        Literal["PENDING_TRAINING", "TRAINED", "TRAINED_INSUFFICIENT_DATA"]
    ] = Field(default=None, alias="StateValue")
    single_metric_anomaly_detector: Optional[SingleMetricAnomalyDetectorModel] = Field(
        default=None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: Optional[MetricMathAnomalyDetectorModel] = Field(
        default=None, alias="MetricMathAnomalyDetector"
    )


class DeleteAnomalyDetectorInputRequestModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    stat: Optional[str] = Field(default=None, alias="Stat")
    single_metric_anomaly_detector: Optional[SingleMetricAnomalyDetectorModel] = Field(
        default=None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: Optional[MetricMathAnomalyDetectorModel] = Field(
        default=None, alias="MetricMathAnomalyDetector"
    )


class PutAnomalyDetectorInputRequestModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    stat: Optional[str] = Field(default=None, alias="Stat")
    configuration: Optional[AnomalyDetectorConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    single_metric_anomaly_detector: Optional[SingleMetricAnomalyDetectorModel] = Field(
        default=None, alias="SingleMetricAnomalyDetector"
    )
    metric_math_anomaly_detector: Optional[MetricMathAnomalyDetectorModel] = Field(
        default=None, alias="MetricMathAnomalyDetector"
    )


class DescribeAnomalyDetectorsOutputModel(BaseModel):
    anomaly_detectors: List[AnomalyDetectorModel] = Field(alias="AnomalyDetectors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
