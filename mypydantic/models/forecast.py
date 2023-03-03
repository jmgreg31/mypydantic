# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    operation: Literal["ADD", "DIVIDE", "MULTIPLY", "SUBTRACT"] = Field(
        alias="Operation"
    )
    value: float = Field(alias="Value")


class AdditionalDatasetModel(BaseModel):
    name: str = Field(alias="Name")
    configuration: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Configuration"
    )


class AttributeConfigModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    transformations: Mapping[str, str] = Field(alias="Transformations")


class BaselineMetricModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[float] = Field(default=None, alias="Value")


class CategoricalParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class ContinuousParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    max_value: float = Field(alias="MaxValue")
    min_value: float = Field(alias="MinValue")
    scaling_type: Optional[
        Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
    ] = Field(default=None, alias="ScalingType")


class EncryptionConfigModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    kms_key_arn: str = Field(alias="KMSKeyArn")


class MonitorConfigModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class TimeAlignmentBoundaryModel(BaseModel):
    month: Optional[
        Literal[
            "APRIL",
            "AUGUST",
            "DECEMBER",
            "FEBRUARY",
            "JANUARY",
            "JULY",
            "JUNE",
            "MARCH",
            "MAY",
            "NOVEMBER",
            "OCTOBER",
            "SEPTEMBER",
        ]
    ] = Field(default=None, alias="Month")
    day_of_month: Optional[int] = Field(default=None, alias="DayOfMonth")
    day_of_week: Optional[
        Literal[
            "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
        ]
    ] = Field(default=None, alias="DayOfWeek")
    hour: Optional[int] = Field(default=None, alias="Hour")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ExplainabilityConfigModel(BaseModel):
    time_series_granularity: Literal["ALL", "SPECIFIC"] = Field(
        alias="TimeSeriesGranularity"
    )
    time_point_granularity: Literal["ALL", "SPECIFIC"] = Field(
        alias="TimePointGranularity"
    )


class EvaluationParametersModel(BaseModel):
    number_of_backtest_windows: Optional[int] = Field(
        default=None, alias="NumberOfBacktestWindows"
    )
    back_test_window_offset: Optional[int] = Field(
        default=None, alias="BackTestWindowOffset"
    )


class S3ConfigModel(BaseModel):
    path: str = Field(alias="Path")
    role_arn: str = Field(alias="RoleArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")


class DatasetGroupSummaryModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="DatasetGroupArn")
    dataset_group_name: Optional[str] = Field(default=None, alias="DatasetGroupName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class DatasetSummaryModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    dataset_type: Optional[
        Literal["ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"]
    ] = Field(default=None, alias="DatasetType")
    domain: Optional[
        Literal[
            "CUSTOM",
            "EC2_CAPACITY",
            "INVENTORY_PLANNING",
            "METRICS",
            "RETAIL",
            "WEB_TRAFFIC",
            "WORK_FORCE",
        ]
    ] = Field(default=None, alias="Domain")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class DeleteDatasetGroupRequestModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")


class DeleteDatasetImportJobRequestModel(BaseModel):
    dataset_import_job_arn: str = Field(alias="DatasetImportJobArn")


class DeleteDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")


class DeleteExplainabilityExportRequestModel(BaseModel):
    explainability_export_arn: str = Field(alias="ExplainabilityExportArn")


class DeleteExplainabilityRequestModel(BaseModel):
    explainability_arn: str = Field(alias="ExplainabilityArn")


class DeleteForecastExportJobRequestModel(BaseModel):
    forecast_export_job_arn: str = Field(alias="ForecastExportJobArn")


class DeleteForecastRequestModel(BaseModel):
    forecast_arn: str = Field(alias="ForecastArn")


class DeleteMonitorRequestModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")


class DeletePredictorBacktestExportJobRequestModel(BaseModel):
    predictor_backtest_export_job_arn: str = Field(
        alias="PredictorBacktestExportJobArn"
    )


class DeletePredictorRequestModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")


class DeleteResourceTreeRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteWhatIfAnalysisRequestModel(BaseModel):
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")


class DeleteWhatIfForecastExportRequestModel(BaseModel):
    what_if_forecast_export_arn: str = Field(alias="WhatIfForecastExportArn")


class DeleteWhatIfForecastRequestModel(BaseModel):
    what_if_forecast_arn: str = Field(alias="WhatIfForecastArn")


class DescribeAutoPredictorRequestModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")


class ExplainabilityInfoModel(BaseModel):
    explainability_arn: Optional[str] = Field(default=None, alias="ExplainabilityArn")
    status: Optional[str] = Field(default=None, alias="Status")


class MonitorInfoModel(BaseModel):
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    status: Optional[str] = Field(default=None, alias="Status")


class ReferencePredictorSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    state: Optional[Literal["Active", "Deleted"]] = Field(default=None, alias="State")


class DescribeDatasetGroupRequestModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")


class DescribeDatasetImportJobRequestModel(BaseModel):
    dataset_import_job_arn: str = Field(alias="DatasetImportJobArn")


class StatisticsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    count_distinct: Optional[int] = Field(default=None, alias="CountDistinct")
    count_null: Optional[int] = Field(default=None, alias="CountNull")
    count_nan: Optional[int] = Field(default=None, alias="CountNan")
    min: Optional[str] = Field(default=None, alias="Min")
    max: Optional[str] = Field(default=None, alias="Max")
    avg: Optional[float] = Field(default=None, alias="Avg")
    stddev: Optional[float] = Field(default=None, alias="Stddev")
    count_long: Optional[int] = Field(default=None, alias="CountLong")
    count_distinct_long: Optional[int] = Field(default=None, alias="CountDistinctLong")
    count_null_long: Optional[int] = Field(default=None, alias="CountNullLong")
    count_nan_long: Optional[int] = Field(default=None, alias="CountNanLong")


class DescribeDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")


class DescribeExplainabilityExportRequestModel(BaseModel):
    explainability_export_arn: str = Field(alias="ExplainabilityExportArn")


class DescribeExplainabilityRequestModel(BaseModel):
    explainability_arn: str = Field(alias="ExplainabilityArn")


class DescribeForecastExportJobRequestModel(BaseModel):
    forecast_export_job_arn: str = Field(alias="ForecastExportJobArn")


class DescribeForecastRequestModel(BaseModel):
    forecast_arn: str = Field(alias="ForecastArn")


class DescribeMonitorRequestModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")


class DescribePredictorBacktestExportJobRequestModel(BaseModel):
    predictor_backtest_export_job_arn: str = Field(
        alias="PredictorBacktestExportJobArn"
    )


class DescribePredictorRequestModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")


class DescribeWhatIfAnalysisRequestModel(BaseModel):
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")


class DescribeWhatIfForecastExportRequestModel(BaseModel):
    what_if_forecast_export_arn: str = Field(alias="WhatIfForecastExportArn")


class DescribeWhatIfForecastRequestModel(BaseModel):
    what_if_forecast_arn: str = Field(alias="WhatIfForecastArn")


class ErrorMetricModel(BaseModel):
    forecast_type: Optional[str] = Field(default=None, alias="ForecastType")
    wap_e: Optional[float] = Field(default=None, alias="WAPE")
    rms_e: Optional[float] = Field(default=None, alias="RMSE")
    mas_e: Optional[float] = Field(default=None, alias="MASE")
    map_e: Optional[float] = Field(default=None, alias="MAPE")


class FeaturizationMethodModel(BaseModel):
    featurization_method_name: Literal["filling"] = Field(
        alias="FeaturizationMethodName"
    )
    featurization_method_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="FeaturizationMethodParameters"
    )


class FilterModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")
    condition: Literal["IS", "IS_NOT"] = Field(alias="Condition")


class ForecastSummaryModel(BaseModel):
    forecast_arn: Optional[str] = Field(default=None, alias="ForecastArn")
    forecast_name: Optional[str] = Field(default=None, alias="ForecastName")
    predictor_arn: Optional[str] = Field(default=None, alias="PredictorArn")
    created_using_auto_predictor: Optional[bool] = Field(
        default=None, alias="CreatedUsingAutoPredictor"
    )
    dataset_group_arn: Optional[str] = Field(default=None, alias="DatasetGroupArn")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class GetAccuracyMetricsRequestModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")


class SupplementaryFeatureModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class IntegerParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    max_value: int = Field(alias="MaxValue")
    min_value: int = Field(alias="MinValue")
    scaling_type: Optional[
        Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
    ] = Field(default=None, alias="ScalingType")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDatasetGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDatasetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MonitorSummaryModel(BaseModel):
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    monitor_name: Optional[str] = Field(default=None, alias="MonitorName")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    status: Optional[str] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class WhatIfAnalysisSummaryModel(BaseModel):
    what_if_analysis_arn: Optional[str] = Field(default=None, alias="WhatIfAnalysisArn")
    what_if_analysis_name: Optional[str] = Field(
        default=None, alias="WhatIfAnalysisName"
    )
    forecast_arn: Optional[str] = Field(default=None, alias="ForecastArn")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class WhatIfForecastSummaryModel(BaseModel):
    what_if_forecast_arn: Optional[str] = Field(default=None, alias="WhatIfForecastArn")
    what_if_forecast_name: Optional[str] = Field(
        default=None, alias="WhatIfForecastName"
    )
    what_if_analysis_arn: Optional[str] = Field(default=None, alias="WhatIfAnalysisArn")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class MetricResultModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    metric_value: Optional[float] = Field(default=None, alias="MetricValue")


class WeightedQuantileLossModel(BaseModel):
    quantile: Optional[float] = Field(default=None, alias="Quantile")
    loss_value: Optional[float] = Field(default=None, alias="LossValue")


class MonitorDataSourceModel(BaseModel):
    dataset_import_job_arn: Optional[str] = Field(
        default=None, alias="DatasetImportJobArn"
    )
    forecast_arn: Optional[str] = Field(default=None, alias="ForecastArn")
    predictor_arn: Optional[str] = Field(default=None, alias="PredictorArn")


class PredictorEventModel(BaseModel):
    detail: Optional[str] = Field(default=None, alias="Detail")
    datetime: Optional[datetime] = Field(default=None, alias="Datetime")


class TestWindowSummaryModel(BaseModel):
    test_window_start: Optional[datetime] = Field(default=None, alias="TestWindowStart")
    test_window_end: Optional[datetime] = Field(default=None, alias="TestWindowEnd")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")


class ResumeResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class SchemaAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_type: Optional[
        Literal["float", "geolocation", "integer", "string", "timestamp"]
    ] = Field(default=None, alias="AttributeType")


class StopResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TimeSeriesConditionModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: str = Field(alias="AttributeValue")
    condition: Literal["EQUALS", "GREATER_THAN", "LESS_THAN", "NOT_EQUALS"] = Field(
        alias="Condition"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDatasetGroupRequestModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    dataset_arns: Sequence[str] = Field(alias="DatasetArns")


class DataConfigModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    attribute_configs: Optional[Sequence[AttributeConfigModel]] = Field(
        default=None, alias="AttributeConfigs"
    )
    additional_datasets: Optional[Sequence[AdditionalDatasetModel]] = Field(
        default=None, alias="AdditionalDatasets"
    )


class PredictorBaselineModel(BaseModel):
    baseline_metrics: Optional[List[BaselineMetricModel]] = Field(
        default=None, alias="BaselineMetrics"
    )


class CreateDatasetGroupRequestModel(BaseModel):
    dataset_group_name: str = Field(alias="DatasetGroupName")
    domain: Literal[
        "CUSTOM",
        "EC2_CAPACITY",
        "INVENTORY_PLANNING",
        "METRICS",
        "RETAIL",
        "WEB_TRAFFIC",
        "WORK_FORCE",
    ] = Field(alias="Domain")
    dataset_arns: Optional[Sequence[str]] = Field(default=None, alias="DatasetArns")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateMonitorRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateAutoPredictorResponseModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetGroupResponseModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetImportJobResponseModel(BaseModel):
    dataset_import_job_arn: str = Field(alias="DatasetImportJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExplainabilityExportResponseModel(BaseModel):
    explainability_export_arn: str = Field(alias="ExplainabilityExportArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExplainabilityResponseModel(BaseModel):
    explainability_arn: str = Field(alias="ExplainabilityArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateForecastExportJobResponseModel(BaseModel):
    forecast_export_job_arn: str = Field(alias="ForecastExportJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateForecastResponseModel(BaseModel):
    forecast_arn: str = Field(alias="ForecastArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMonitorResponseModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePredictorBacktestExportJobResponseModel(BaseModel):
    predictor_backtest_export_job_arn: str = Field(
        alias="PredictorBacktestExportJobArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePredictorResponseModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWhatIfAnalysisResponseModel(BaseModel):
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWhatIfForecastExportResponseModel(BaseModel):
    what_if_forecast_export_arn: str = Field(alias="WhatIfForecastExportArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWhatIfForecastResponseModel(BaseModel):
    what_if_forecast_arn: str = Field(alias="WhatIfForecastArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetGroupResponseModel(BaseModel):
    dataset_group_name: str = Field(alias="DatasetGroupName")
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    dataset_arns: List[str] = Field(alias="DatasetArns")
    domain: Literal[
        "CUSTOM",
        "EC2_CAPACITY",
        "INVENTORY_PLANNING",
        "METRICS",
        "RETAIL",
        "WEB_TRAFFIC",
        "WORK_FORCE",
    ] = Field(alias="Domain")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExplainabilitySummaryModel(BaseModel):
    explainability_arn: Optional[str] = Field(default=None, alias="ExplainabilityArn")
    explainability_name: Optional[str] = Field(default=None, alias="ExplainabilityName")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    explainability_config: Optional[ExplainabilityConfigModel] = Field(
        default=None, alias="ExplainabilityConfig"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class DataDestinationModel(BaseModel):
    s3_config: S3ConfigModel = Field(alias="S3Config")


class DataSourceModel(BaseModel):
    s3_config: S3ConfigModel = Field(alias="S3Config")


class ListDatasetGroupsResponseModel(BaseModel):
    dataset_groups: List[DatasetGroupSummaryModel] = Field(alias="DatasetGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    datasets: List[DatasetSummaryModel] = Field(alias="Datasets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PredictorSummaryModel(BaseModel):
    predictor_arn: Optional[str] = Field(default=None, alias="PredictorArn")
    predictor_name: Optional[str] = Field(default=None, alias="PredictorName")
    dataset_group_arn: Optional[str] = Field(default=None, alias="DatasetGroupArn")
    is_auto_predictor: Optional[bool] = Field(default=None, alias="IsAutoPredictor")
    reference_predictor_summary: Optional[ReferencePredictorSummaryModel] = Field(
        default=None, alias="ReferencePredictorSummary"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class FeaturizationModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    featurization_pipeline: Optional[Sequence[FeaturizationMethodModel]] = Field(
        default=None, alias="FeaturizationPipeline"
    )


class ListDatasetImportJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListExplainabilitiesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListExplainabilityExportsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListForecastExportJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListForecastsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListMonitorEvaluationsRequestModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListMonitorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListPredictorBacktestExportJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListPredictorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListWhatIfAnalysesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListWhatIfForecastExportsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListWhatIfForecastsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListForecastsResponseModel(BaseModel):
    forecasts: List[ForecastSummaryModel] = Field(alias="Forecasts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputDataConfigModel(BaseModel):
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    supplementary_features: Optional[Sequence[SupplementaryFeatureModel]] = Field(
        default=None, alias="SupplementaryFeatures"
    )


class ParameterRangesModel(BaseModel):
    categorical_parameter_ranges: Optional[
        Sequence[CategoricalParameterRangeModel]
    ] = Field(default=None, alias="CategoricalParameterRanges")
    continuous_parameter_ranges: Optional[
        Sequence[ContinuousParameterRangeModel]
    ] = Field(default=None, alias="ContinuousParameterRanges")
    integer_parameter_ranges: Optional[Sequence[IntegerParameterRangeModel]] = Field(
        default=None, alias="IntegerParameterRanges"
    )


class ListDatasetGroupsRequestListDatasetGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetImportJobsRequestListDatasetImportJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetsRequestListDatasetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExplainabilitiesRequestListExplainabilitiesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExplainabilityExportsRequestListExplainabilityExportsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListForecastExportJobsRequestListForecastExportJobsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListForecastsRequestListForecastsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitorsRequestListMonitorsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPredictorsRequestListPredictorsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWhatIfForecastsRequestListWhatIfForecastsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitorsResponseModel(BaseModel):
    monitors: List[MonitorSummaryModel] = Field(alias="Monitors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWhatIfAnalysesResponseModel(BaseModel):
    what_if_analyses: List[WhatIfAnalysisSummaryModel] = Field(alias="WhatIfAnalyses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWhatIfForecastsResponseModel(BaseModel):
    what_if_forecasts: List[WhatIfForecastSummaryModel] = Field(alias="WhatIfForecasts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricsModel(BaseModel):
    rms_e: Optional[float] = Field(default=None, alias="RMSE")
    weighted_quantile_losses: Optional[List[WeightedQuantileLossModel]] = Field(
        default=None, alias="WeightedQuantileLosses"
    )
    error_metrics: Optional[List[ErrorMetricModel]] = Field(
        default=None, alias="ErrorMetrics"
    )
    average_weighted_quantile_loss: Optional[float] = Field(
        default=None, alias="AverageWeightedQuantileLoss"
    )


class PredictorMonitorEvaluationModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    evaluation_time: Optional[datetime] = Field(default=None, alias="EvaluationTime")
    evaluation_state: Optional[str] = Field(default=None, alias="EvaluationState")
    window_start_datetime: Optional[datetime] = Field(
        default=None, alias="WindowStartDatetime"
    )
    window_end_datetime: Optional[datetime] = Field(
        default=None, alias="WindowEndDatetime"
    )
    predictor_event: Optional[PredictorEventModel] = Field(
        default=None, alias="PredictorEvent"
    )
    monitor_data_source: Optional[MonitorDataSourceModel] = Field(
        default=None, alias="MonitorDataSource"
    )
    metric_results: Optional[List[MetricResultModel]] = Field(
        default=None, alias="MetricResults"
    )
    num_items_evaluated: Optional[int] = Field(default=None, alias="NumItemsEvaluated")
    message: Optional[str] = Field(default=None, alias="Message")


class PredictorExecutionModel(BaseModel):
    algorithm_arn: Optional[str] = Field(default=None, alias="AlgorithmArn")
    test_windows: Optional[List[TestWindowSummaryModel]] = Field(
        default=None, alias="TestWindows"
    )


class SchemaModel(BaseModel):
    attributes: Optional[Sequence[SchemaAttributeModel]] = Field(
        default=None, alias="Attributes"
    )


class TimeSeriesTransformationModel(BaseModel):
    action: Optional[ActionModel] = Field(default=None, alias="Action")
    time_series_conditions: Optional[Sequence[TimeSeriesConditionModel]] = Field(
        default=None, alias="TimeSeriesConditions"
    )


class CreateAutoPredictorRequestModel(BaseModel):
    predictor_name: str = Field(alias="PredictorName")
    forecast_horizon: Optional[int] = Field(default=None, alias="ForecastHorizon")
    forecast_types: Optional[Sequence[str]] = Field(default=None, alias="ForecastTypes")
    forecast_dimensions: Optional[Sequence[str]] = Field(
        default=None, alias="ForecastDimensions"
    )
    forecast_frequency: Optional[str] = Field(default=None, alias="ForecastFrequency")
    data_config: Optional[DataConfigModel] = Field(default=None, alias="DataConfig")
    encryption_config: Optional[EncryptionConfigModel] = Field(
        default=None, alias="EncryptionConfig"
    )
    reference_predictor_arn: Optional[str] = Field(
        default=None, alias="ReferencePredictorArn"
    )
    optimization_metric: Optional[
        Literal["AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"]
    ] = Field(default=None, alias="OptimizationMetric")
    explain_predictor: Optional[bool] = Field(default=None, alias="ExplainPredictor")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    monitor_config: Optional[MonitorConfigModel] = Field(
        default=None, alias="MonitorConfig"
    )
    time_alignment_boundary: Optional[TimeAlignmentBoundaryModel] = Field(
        default=None, alias="TimeAlignmentBoundary"
    )


class DescribeAutoPredictorResponseModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")
    predictor_name: str = Field(alias="PredictorName")
    forecast_horizon: int = Field(alias="ForecastHorizon")
    forecast_types: List[str] = Field(alias="ForecastTypes")
    forecast_frequency: str = Field(alias="ForecastFrequency")
    forecast_dimensions: List[str] = Field(alias="ForecastDimensions")
    dataset_import_job_arns: List[str] = Field(alias="DatasetImportJobArns")
    data_config: DataConfigModel = Field(alias="DataConfig")
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")
    reference_predictor_summary: ReferencePredictorSummaryModel = Field(
        alias="ReferencePredictorSummary"
    )
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    optimization_metric: Literal[
        "AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"
    ] = Field(alias="OptimizationMetric")
    explainability_info: ExplainabilityInfoModel = Field(alias="ExplainabilityInfo")
    monitor_info: MonitorInfoModel = Field(alias="MonitorInfo")
    time_alignment_boundary: TimeAlignmentBoundaryModel = Field(
        alias="TimeAlignmentBoundary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BaselineModel(BaseModel):
    predictor_baseline: Optional[PredictorBaselineModel] = Field(
        default=None, alias="PredictorBaseline"
    )


class ListExplainabilitiesResponseModel(BaseModel):
    explainabilities: List[ExplainabilitySummaryModel] = Field(alias="Explainabilities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExplainabilityExportRequestModel(BaseModel):
    explainability_export_name: str = Field(alias="ExplainabilityExportName")
    explainability_arn: str = Field(alias="ExplainabilityArn")
    destination: DataDestinationModel = Field(alias="Destination")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    format: Optional[str] = Field(default=None, alias="Format")


class CreateForecastExportJobRequestModel(BaseModel):
    forecast_export_job_name: str = Field(alias="ForecastExportJobName")
    forecast_arn: str = Field(alias="ForecastArn")
    destination: DataDestinationModel = Field(alias="Destination")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    format: Optional[str] = Field(default=None, alias="Format")


class CreatePredictorBacktestExportJobRequestModel(BaseModel):
    predictor_backtest_export_job_name: str = Field(
        alias="PredictorBacktestExportJobName"
    )
    predictor_arn: str = Field(alias="PredictorArn")
    destination: DataDestinationModel = Field(alias="Destination")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    format: Optional[str] = Field(default=None, alias="Format")


class CreateWhatIfForecastExportRequestModel(BaseModel):
    what_if_forecast_export_name: str = Field(alias="WhatIfForecastExportName")
    what_if_forecast_arns: Sequence[str] = Field(alias="WhatIfForecastArns")
    destination: DataDestinationModel = Field(alias="Destination")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    format: Optional[str] = Field(default=None, alias="Format")


class DescribeExplainabilityExportResponseModel(BaseModel):
    explainability_export_arn: str = Field(alias="ExplainabilityExportArn")
    explainability_export_name: str = Field(alias="ExplainabilityExportName")
    explainability_arn: str = Field(alias="ExplainabilityArn")
    destination: DataDestinationModel = Field(alias="Destination")
    message: str = Field(alias="Message")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    format: str = Field(alias="Format")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeForecastExportJobResponseModel(BaseModel):
    forecast_export_job_arn: str = Field(alias="ForecastExportJobArn")
    forecast_export_job_name: str = Field(alias="ForecastExportJobName")
    forecast_arn: str = Field(alias="ForecastArn")
    destination: DataDestinationModel = Field(alias="Destination")
    message: str = Field(alias="Message")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    format: str = Field(alias="Format")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePredictorBacktestExportJobResponseModel(BaseModel):
    predictor_backtest_export_job_arn: str = Field(
        alias="PredictorBacktestExportJobArn"
    )
    predictor_backtest_export_job_name: str = Field(
        alias="PredictorBacktestExportJobName"
    )
    predictor_arn: str = Field(alias="PredictorArn")
    destination: DataDestinationModel = Field(alias="Destination")
    message: str = Field(alias="Message")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    format: str = Field(alias="Format")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWhatIfForecastExportResponseModel(BaseModel):
    what_if_forecast_export_arn: str = Field(alias="WhatIfForecastExportArn")
    what_if_forecast_export_name: str = Field(alias="WhatIfForecastExportName")
    what_if_forecast_arns: List[str] = Field(alias="WhatIfForecastArns")
    destination: DataDestinationModel = Field(alias="Destination")
    message: str = Field(alias="Message")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    last_modification_time: datetime = Field(alias="LastModificationTime")
    format: str = Field(alias="Format")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExplainabilityExportSummaryModel(BaseModel):
    explainability_export_arn: Optional[str] = Field(
        default=None, alias="ExplainabilityExportArn"
    )
    explainability_export_name: Optional[str] = Field(
        default=None, alias="ExplainabilityExportName"
    )
    destination: Optional[DataDestinationModel] = Field(
        default=None, alias="Destination"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class ForecastExportJobSummaryModel(BaseModel):
    forecast_export_job_arn: Optional[str] = Field(
        default=None, alias="ForecastExportJobArn"
    )
    forecast_export_job_name: Optional[str] = Field(
        default=None, alias="ForecastExportJobName"
    )
    destination: Optional[DataDestinationModel] = Field(
        default=None, alias="Destination"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class PredictorBacktestExportJobSummaryModel(BaseModel):
    predictor_backtest_export_job_arn: Optional[str] = Field(
        default=None, alias="PredictorBacktestExportJobArn"
    )
    predictor_backtest_export_job_name: Optional[str] = Field(
        default=None, alias="PredictorBacktestExportJobName"
    )
    destination: Optional[DataDestinationModel] = Field(
        default=None, alias="Destination"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class WhatIfForecastExportSummaryModel(BaseModel):
    what_if_forecast_export_arn: Optional[str] = Field(
        default=None, alias="WhatIfForecastExportArn"
    )
    what_if_forecast_arns: Optional[List[str]] = Field(
        default=None, alias="WhatIfForecastArns"
    )
    what_if_forecast_export_name: Optional[str] = Field(
        default=None, alias="WhatIfForecastExportName"
    )
    destination: Optional[DataDestinationModel] = Field(
        default=None, alias="Destination"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )


class CreateDatasetImportJobRequestModel(BaseModel):
    dataset_import_job_name: str = Field(alias="DatasetImportJobName")
    dataset_arn: str = Field(alias="DatasetArn")
    data_source: DataSourceModel = Field(alias="DataSource")
    timestamp_format: Optional[str] = Field(default=None, alias="TimestampFormat")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")
    use_geolocation_for_time_zone: Optional[bool] = Field(
        default=None, alias="UseGeolocationForTimeZone"
    )
    geolocation_format: Optional[str] = Field(default=None, alias="GeolocationFormat")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    format: Optional[str] = Field(default=None, alias="Format")
    import_mode: Optional[Literal["FULL", "INCREMENTAL"]] = Field(
        default=None, alias="ImportMode"
    )


class DatasetImportJobSummaryModel(BaseModel):
    dataset_import_job_arn: Optional[str] = Field(
        default=None, alias="DatasetImportJobArn"
    )
    dataset_import_job_name: Optional[str] = Field(
        default=None, alias="DatasetImportJobName"
    )
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )
    import_mode: Optional[Literal["FULL", "INCREMENTAL"]] = Field(
        default=None, alias="ImportMode"
    )


class DescribeDatasetImportJobResponseModel(BaseModel):
    dataset_import_job_name: str = Field(alias="DatasetImportJobName")
    dataset_import_job_arn: str = Field(alias="DatasetImportJobArn")
    dataset_arn: str = Field(alias="DatasetArn")
    timestamp_format: str = Field(alias="TimestampFormat")
    time_zone: str = Field(alias="TimeZone")
    use_geolocation_for_time_zone: bool = Field(alias="UseGeolocationForTimeZone")
    geolocation_format: str = Field(alias="GeolocationFormat")
    data_source: DataSourceModel = Field(alias="DataSource")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    field_statistics: Dict[str, StatisticsModel] = Field(alias="FieldStatistics")
    data_size: float = Field(alias="DataSize")
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    format: str = Field(alias="Format")
    import_mode: Literal["FULL", "INCREMENTAL"] = Field(alias="ImportMode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPredictorsResponseModel(BaseModel):
    predictors: List[PredictorSummaryModel] = Field(alias="Predictors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FeaturizationConfigModel(BaseModel):
    forecast_frequency: str = Field(alias="ForecastFrequency")
    forecast_dimensions: Optional[Sequence[str]] = Field(
        default=None, alias="ForecastDimensions"
    )
    featurizations: Optional[Sequence[FeaturizationModel]] = Field(
        default=None, alias="Featurizations"
    )


class HyperParameterTuningJobConfigModel(BaseModel):
    parameter_ranges: Optional[ParameterRangesModel] = Field(
        default=None, alias="ParameterRanges"
    )


class WindowSummaryModel(BaseModel):
    test_window_start: Optional[datetime] = Field(default=None, alias="TestWindowStart")
    test_window_end: Optional[datetime] = Field(default=None, alias="TestWindowEnd")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    evaluation_type: Optional[Literal["COMPUTED", "SUMMARY"]] = Field(
        default=None, alias="EvaluationType"
    )
    metrics: Optional[MetricsModel] = Field(default=None, alias="Metrics")


class ListMonitorEvaluationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    predictor_monitor_evaluations: List[PredictorMonitorEvaluationModel] = Field(
        alias="PredictorMonitorEvaluations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PredictorExecutionDetailsModel(BaseModel):
    predictor_executions: Optional[List[PredictorExecutionModel]] = Field(
        default=None, alias="PredictorExecutions"
    )


class CreateDatasetRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    domain: Literal[
        "CUSTOM",
        "EC2_CAPACITY",
        "INVENTORY_PLANNING",
        "METRICS",
        "RETAIL",
        "WEB_TRAFFIC",
        "WORK_FORCE",
    ] = Field(alias="Domain")
    dataset_type: Literal[
        "ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"
    ] = Field(alias="DatasetType")
    schema_: SchemaModel = Field(alias="Schema")
    data_frequency: Optional[str] = Field(default=None, alias="DataFrequency")
    encryption_config: Optional[EncryptionConfigModel] = Field(
        default=None, alias="EncryptionConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateExplainabilityRequestModel(BaseModel):
    explainability_name: str = Field(alias="ExplainabilityName")
    resource_arn: str = Field(alias="ResourceArn")
    explainability_config: ExplainabilityConfigModel = Field(
        alias="ExplainabilityConfig"
    )
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    schema_: Optional[SchemaModel] = Field(default=None, alias="Schema")
    enable_visualization: Optional[bool] = Field(
        default=None, alias="EnableVisualization"
    )
    start_date_time: Optional[str] = Field(default=None, alias="StartDateTime")
    end_date_time: Optional[str] = Field(default=None, alias="EndDateTime")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeDatasetResponseModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    dataset_name: str = Field(alias="DatasetName")
    domain: Literal[
        "CUSTOM",
        "EC2_CAPACITY",
        "INVENTORY_PLANNING",
        "METRICS",
        "RETAIL",
        "WEB_TRAFFIC",
        "WORK_FORCE",
    ] = Field(alias="Domain")
    dataset_type: Literal[
        "ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"
    ] = Field(alias="DatasetType")
    data_frequency: str = Field(alias="DataFrequency")
    schema_: SchemaModel = Field(alias="Schema")
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExplainabilityResponseModel(BaseModel):
    explainability_arn: str = Field(alias="ExplainabilityArn")
    explainability_name: str = Field(alias="ExplainabilityName")
    resource_arn: str = Field(alias="ResourceArn")
    explainability_config: ExplainabilityConfigModel = Field(
        alias="ExplainabilityConfig"
    )
    enable_visualization: bool = Field(alias="EnableVisualization")
    data_source: DataSourceModel = Field(alias="DataSource")
    schema_: SchemaModel = Field(alias="Schema")
    start_date_time: str = Field(alias="StartDateTime")
    end_date_time: str = Field(alias="EndDateTime")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    message: str = Field(alias="Message")
    status: str = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TimeSeriesIdentifiersModel(BaseModel):
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    schema_: Optional[SchemaModel] = Field(default=None, alias="Schema")
    format: Optional[str] = Field(default=None, alias="Format")


class TimeSeriesReplacementsDataSourceModel(BaseModel):
    s3_config: S3ConfigModel = Field(alias="S3Config")
    schema_: SchemaModel = Field(alias="Schema")
    format: Optional[str] = Field(default=None, alias="Format")
    timestamp_format: Optional[str] = Field(default=None, alias="TimestampFormat")


class DescribeMonitorResponseModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    monitor_arn: str = Field(alias="MonitorArn")
    resource_arn: str = Field(alias="ResourceArn")
    status: str = Field(alias="Status")
    last_evaluation_time: datetime = Field(alias="LastEvaluationTime")
    last_evaluation_state: str = Field(alias="LastEvaluationState")
    baseline: BaselineModel = Field(alias="Baseline")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    estimated_evaluation_time_remaining_in_minutes: int = Field(
        alias="EstimatedEvaluationTimeRemainingInMinutes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExplainabilityExportsResponseModel(BaseModel):
    explainability_exports: List[ExplainabilityExportSummaryModel] = Field(
        alias="ExplainabilityExports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListForecastExportJobsResponseModel(BaseModel):
    forecast_export_jobs: List[ForecastExportJobSummaryModel] = Field(
        alias="ForecastExportJobs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPredictorBacktestExportJobsResponseModel(BaseModel):
    predictor_backtest_export_jobs: List[
        PredictorBacktestExportJobSummaryModel
    ] = Field(alias="PredictorBacktestExportJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWhatIfForecastExportsResponseModel(BaseModel):
    what_if_forecast_exports: List[WhatIfForecastExportSummaryModel] = Field(
        alias="WhatIfForecastExports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetImportJobsResponseModel(BaseModel):
    dataset_import_jobs: List[DatasetImportJobSummaryModel] = Field(
        alias="DatasetImportJobs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePredictorRequestModel(BaseModel):
    predictor_name: str = Field(alias="PredictorName")
    forecast_horizon: int = Field(alias="ForecastHorizon")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    featurization_config: FeaturizationConfigModel = Field(alias="FeaturizationConfig")
    algorithm_arn: Optional[str] = Field(default=None, alias="AlgorithmArn")
    forecast_types: Optional[Sequence[str]] = Field(default=None, alias="ForecastTypes")
    perform_auto_ml: Optional[bool] = Field(default=None, alias="PerformAutoML")
    auto_ml_override_strategy: Optional[
        Literal["AccuracyOptimized", "LatencyOptimized"]
    ] = Field(default=None, alias="AutoMLOverrideStrategy")
    perform_hp_o: Optional[bool] = Field(default=None, alias="PerformHPO")
    training_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="TrainingParameters"
    )
    evaluation_parameters: Optional[EvaluationParametersModel] = Field(
        default=None, alias="EvaluationParameters"
    )
    hp_oconfig: Optional[HyperParameterTuningJobConfigModel] = Field(
        default=None, alias="HPOConfig"
    )
    encryption_config: Optional[EncryptionConfigModel] = Field(
        default=None, alias="EncryptionConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    optimization_metric: Optional[
        Literal["AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"]
    ] = Field(default=None, alias="OptimizationMetric")


class EvaluationResultModel(BaseModel):
    algorithm_arn: Optional[str] = Field(default=None, alias="AlgorithmArn")
    test_windows: Optional[List[WindowSummaryModel]] = Field(
        default=None, alias="TestWindows"
    )


class DescribePredictorResponseModel(BaseModel):
    predictor_arn: str = Field(alias="PredictorArn")
    predictor_name: str = Field(alias="PredictorName")
    algorithm_arn: str = Field(alias="AlgorithmArn")
    auto_ml_algorithm_arns: List[str] = Field(alias="AutoMLAlgorithmArns")
    forecast_horizon: int = Field(alias="ForecastHorizon")
    forecast_types: List[str] = Field(alias="ForecastTypes")
    perform_auto_ml: bool = Field(alias="PerformAutoML")
    auto_ml_override_strategy: Literal["AccuracyOptimized", "LatencyOptimized"] = Field(
        alias="AutoMLOverrideStrategy"
    )
    perform_hp_o: bool = Field(alias="PerformHPO")
    training_parameters: Dict[str, str] = Field(alias="TrainingParameters")
    evaluation_parameters: EvaluationParametersModel = Field(
        alias="EvaluationParameters"
    )
    hp_oconfig: HyperParameterTuningJobConfigModel = Field(alias="HPOConfig")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    featurization_config: FeaturizationConfigModel = Field(alias="FeaturizationConfig")
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")
    predictor_execution_details: PredictorExecutionDetailsModel = Field(
        alias="PredictorExecutionDetails"
    )
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    is_auto_predictor: bool = Field(alias="IsAutoPredictor")
    dataset_import_job_arns: List[str] = Field(alias="DatasetImportJobArns")
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    optimization_metric: Literal[
        "AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"
    ] = Field(alias="OptimizationMetric")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TimeSeriesSelectorModel(BaseModel):
    time_series_identifiers: Optional[TimeSeriesIdentifiersModel] = Field(
        default=None, alias="TimeSeriesIdentifiers"
    )


class CreateWhatIfForecastRequestModel(BaseModel):
    what_if_forecast_name: str = Field(alias="WhatIfForecastName")
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")
    time_series_transformations: Optional[
        Sequence[TimeSeriesTransformationModel]
    ] = Field(default=None, alias="TimeSeriesTransformations")
    time_series_replacements_data_source: Optional[
        TimeSeriesReplacementsDataSourceModel
    ] = Field(default=None, alias="TimeSeriesReplacementsDataSource")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeWhatIfForecastResponseModel(BaseModel):
    what_if_forecast_name: str = Field(alias="WhatIfForecastName")
    what_if_forecast_arn: str = Field(alias="WhatIfForecastArn")
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    time_series_transformations: List[TimeSeriesTransformationModel] = Field(
        alias="TimeSeriesTransformations"
    )
    time_series_replacements_data_source: TimeSeriesReplacementsDataSourceModel = Field(
        alias="TimeSeriesReplacementsDataSource"
    )
    forecast_types: List[str] = Field(alias="ForecastTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccuracyMetricsResponseModel(BaseModel):
    predictor_evaluation_results: List[EvaluationResultModel] = Field(
        alias="PredictorEvaluationResults"
    )
    is_auto_predictor: bool = Field(alias="IsAutoPredictor")
    auto_ml_override_strategy: Literal["AccuracyOptimized", "LatencyOptimized"] = Field(
        alias="AutoMLOverrideStrategy"
    )
    optimization_metric: Literal[
        "AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"
    ] = Field(alias="OptimizationMetric")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateForecastRequestModel(BaseModel):
    forecast_name: str = Field(alias="ForecastName")
    predictor_arn: str = Field(alias="PredictorArn")
    forecast_types: Optional[Sequence[str]] = Field(default=None, alias="ForecastTypes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    time_series_selector: Optional[TimeSeriesSelectorModel] = Field(
        default=None, alias="TimeSeriesSelector"
    )


class CreateWhatIfAnalysisRequestModel(BaseModel):
    what_if_analysis_name: str = Field(alias="WhatIfAnalysisName")
    forecast_arn: str = Field(alias="ForecastArn")
    time_series_selector: Optional[TimeSeriesSelectorModel] = Field(
        default=None, alias="TimeSeriesSelector"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeForecastResponseModel(BaseModel):
    forecast_arn: str = Field(alias="ForecastArn")
    forecast_name: str = Field(alias="ForecastName")
    forecast_types: List[str] = Field(alias="ForecastTypes")
    predictor_arn: str = Field(alias="PredictorArn")
    dataset_group_arn: str = Field(alias="DatasetGroupArn")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    time_series_selector: TimeSeriesSelectorModel = Field(alias="TimeSeriesSelector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWhatIfAnalysisResponseModel(BaseModel):
    what_if_analysis_name: str = Field(alias="WhatIfAnalysisName")
    what_if_analysis_arn: str = Field(alias="WhatIfAnalysisArn")
    forecast_arn: str = Field(alias="ForecastArn")
    estimated_time_remaining_in_minutes: int = Field(
        alias="EstimatedTimeRemainingInMinutes"
    )
    status: str = Field(alias="Status")
    message: str = Field(alias="Message")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    time_series_selector: TimeSeriesSelectorModel = Field(alias="TimeSeriesSelector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
