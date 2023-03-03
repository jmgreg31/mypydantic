# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class LambdaConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    lambda_arn: str = Field(alias="LambdaArn")


class SNSConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    sns_format: Optional[Literal["JSON", "LONG_TEXT", "SHORT_TEXT"]] = Field(
        default=None, alias="SnsFormat"
    )


class ActivateAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class DimensionFilterModel(BaseModel):
    dimension_name: Optional[str] = Field(default=None, alias="DimensionName")
    dimension_value_list: Optional[Sequence[str]] = Field(
        default=None, alias="DimensionValueList"
    )


class AlertSummaryModel(BaseModel):
    alert_arn: Optional[str] = Field(default=None, alias="AlertArn")
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    alert_name: Optional[str] = Field(default=None, alias="AlertName")
    alert_sensitivity_threshold: Optional[int] = Field(
        default=None, alias="AlertSensitivityThreshold"
    )
    alert_type: Optional[Literal["LAMBDA", "SNS"]] = Field(
        default=None, alias="AlertType"
    )
    alert_status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="AlertStatus"
    )
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class AnomalyDetectorConfigSummaryModel(BaseModel):
    anomaly_detector_frequency: Optional[
        Literal["P1D", "PT10M", "PT1H", "PT5M"]
    ] = Field(default=None, alias="AnomalyDetectorFrequency")


class AnomalyDetectorConfigModel(BaseModel):
    anomaly_detector_frequency: Optional[
        Literal["P1D", "PT10M", "PT1H", "PT5M"]
    ] = Field(default=None, alias="AnomalyDetectorFrequency")


class AnomalyDetectorSummaryModel(BaseModel):
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    anomaly_detector_name: Optional[str] = Field(
        default=None, alias="AnomalyDetectorName"
    )
    anomaly_detector_description: Optional[str] = Field(
        default=None, alias="AnomalyDetectorDescription"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "BACK_TEST_ACTIVATING",
            "BACK_TEST_ACTIVE",
            "BACK_TEST_COMPLETE",
            "DEACTIVATED",
            "DEACTIVATING",
            "DELETING",
            "FAILED",
            "INACTIVE",
            "LEARNING",
        ]
    ] = Field(default=None, alias="Status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ItemizedMetricStatsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    occurrence_count: Optional[int] = Field(default=None, alias="OccurrenceCount")


class AnomalyGroupSummaryModel(BaseModel):
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    end_time: Optional[str] = Field(default=None, alias="EndTime")
    anomaly_group_id: Optional[str] = Field(default=None, alias="AnomalyGroupId")
    anomaly_group_score: Optional[float] = Field(
        default=None, alias="AnomalyGroupScore"
    )
    primary_metric_name: Optional[str] = Field(default=None, alias="PrimaryMetricName")


class AnomalyGroupTimeSeriesFeedbackModel(BaseModel):
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    time_series_id: str = Field(alias="TimeSeriesId")
    is_anomaly: bool = Field(alias="IsAnomaly")


class AnomalyGroupTimeSeriesModel(BaseModel):
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    time_series_id: Optional[str] = Field(default=None, alias="TimeSeriesId")


class AppFlowConfigModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    flow_name: Optional[str] = Field(default=None, alias="FlowName")


class BackTestConfigurationModel(BaseModel):
    run_back_test_mode: bool = Field(alias="RunBackTestMode")


class AttributeValueModel(BaseModel):
    s: Optional[str] = Field(default=None, alias="S")
    n: Optional[str] = Field(default=None, alias="N")
    b: Optional[str] = Field(default=None, alias="B")
    s_s: Optional[List[str]] = Field(default=None, alias="SS")
    ns: Optional[List[str]] = Field(default=None, alias="NS")
    bs: Optional[List[str]] = Field(default=None, alias="BS")


class AutoDetectionS3SourceConfigModel(BaseModel):
    templated_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="TemplatedPathList"
    )
    historical_data_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="HistoricalDataPathList"
    )


class BackTestAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class MetricModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    aggregation_function: Literal["AVG", "SUM"] = Field(alias="AggregationFunction")
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class TimestampColumnModel(BaseModel):
    column_name: Optional[str] = Field(default=None, alias="ColumnName")
    column_format: Optional[str] = Field(default=None, alias="ColumnFormat")


class CsvFormatDescriptorModel(BaseModel):
    file_compression: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="FileCompression"
    )
    charset: Optional[str] = Field(default=None, alias="Charset")
    contains_header: Optional[bool] = Field(default=None, alias="ContainsHeader")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    header_list: Optional[Sequence[str]] = Field(default=None, alias="HeaderList")
    quote_symbol: Optional[str] = Field(default=None, alias="QuoteSymbol")


class DataQualityMetricModel(BaseModel):
    metric_type: Optional[
        Literal[
            "BACKTEST_INFERENCE_DATA_END_TIME_STAMP",
            "BACKTEST_INFERENCE_DATA_START_TIME_STAMP",
            "BACKTEST_TRAINING_DATA_END_TIME_STAMP",
            "BACKTEST_TRAINING_DATA_START_TIME_STAMP",
            "COLUMN_COMPLETENESS",
            "DIMENSION_UNIQUENESS",
            "INVALID_ROWS_COMPLIANCE",
            "ROWS_PARTIAL_COMPLIANCE",
            "ROWS_PROCESSED",
            "TIME_SERIES_COUNT",
        ]
    ] = Field(default=None, alias="MetricType")
    metric_description: Optional[str] = Field(default=None, alias="MetricDescription")
    related_column_name: Optional[str] = Field(default=None, alias="RelatedColumnName")
    metric_value: Optional[float] = Field(default=None, alias="MetricValue")


class DeactivateAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class DeleteAlertRequestModel(BaseModel):
    alert_arn: str = Field(alias="AlertArn")


class DeleteAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class DescribeAlertRequestModel(BaseModel):
    alert_arn: str = Field(alias="AlertArn")


class DescribeAnomalyDetectionExecutionsRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    timestamp: Optional[str] = Field(default=None, alias="Timestamp")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ExecutionStatusModel(BaseModel):
    timestamp: Optional[str] = Field(default=None, alias="Timestamp")
    status: Optional[
        Literal["COMPLETED", "FAILED", "FAILED_TO_SCHEDULE", "IN_PROGRESS", "PENDING"]
    ] = Field(default=None, alias="Status")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class DescribeAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class DescribeMetricSetRequestModel(BaseModel):
    metric_set_arn: str = Field(alias="MetricSetArn")


class DimensionValueContributionModel(BaseModel):
    dimension_value: Optional[str] = Field(default=None, alias="DimensionValue")
    contribution_score: Optional[float] = Field(default=None, alias="ContributionScore")


class DimensionNameValueModel(BaseModel):
    dimension_name: str = Field(alias="DimensionName")
    dimension_value: str = Field(alias="DimensionValue")


class JsonFormatDescriptorModel(BaseModel):
    file_compression: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="FileCompression"
    )
    charset: Optional[str] = Field(default=None, alias="Charset")


class FilterModel(BaseModel):
    dimension_value: Optional[str] = Field(default=None, alias="DimensionValue")
    filter_operation: Optional[Literal["EQUALS"]] = Field(
        default=None, alias="FilterOperation"
    )


class GetAnomalyGroupRequestModel(BaseModel):
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")


class GetDataQualityMetricsRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    metric_set_arn: Optional[str] = Field(default=None, alias="MetricSetArn")


class TimeSeriesFeedbackModel(BaseModel):
    time_series_id: Optional[str] = Field(default=None, alias="TimeSeriesId")
    is_anomaly: Optional[bool] = Field(default=None, alias="IsAnomaly")


class InterMetricImpactDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    anomaly_group_id: Optional[str] = Field(default=None, alias="AnomalyGroupId")
    relationship_type: Optional[
        Literal["CAUSE_OF_INPUT_ANOMALY_GROUP", "EFFECT_OF_INPUT_ANOMALY_GROUP"]
    ] = Field(default=None, alias="RelationshipType")
    contribution_percentage: Optional[float] = Field(
        default=None, alias="ContributionPercentage"
    )


class ListAlertsRequestModel(BaseModel):
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAnomalyDetectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAnomalyGroupRelatedMetricsRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    relationship_type_filter: Optional[
        Literal["CAUSE_OF_INPUT_ANOMALY_GROUP", "EFFECT_OF_INPUT_ANOMALY_GROUP"]
    ] = Field(default=None, alias="RelationshipTypeFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAnomalyGroupSummariesRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    sensitivity_threshold: int = Field(alias="SensitivityThreshold")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAnomalyGroupTimeSeriesRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    metric_name: str = Field(alias="MetricName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMetricSetsRequestModel(BaseModel):
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MetricSetSummaryModel(BaseModel):
    metric_set_arn: Optional[str] = Field(default=None, alias="MetricSetArn")
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    metric_set_description: Optional[str] = Field(
        default=None, alias="MetricSetDescription"
    )
    metric_set_name: Optional[str] = Field(default=None, alias="MetricSetName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class VpcConfigurationModel(BaseModel):
    subnet_id_list: Sequence[str] = Field(alias="SubnetIdList")
    security_group_id_list: Sequence[str] = Field(alias="SecurityGroupIdList")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ActionModel(BaseModel):
    s_ns_configuration: Optional[SNSConfigurationModel] = Field(
        default=None, alias="SNSConfiguration"
    )
    lambda_configuration: Optional[LambdaConfigurationModel] = Field(
        default=None, alias="LambdaConfiguration"
    )


class AlertFiltersModel(BaseModel):
    metric_list: Optional[Sequence[str]] = Field(default=None, alias="MetricList")
    dimension_filter_list: Optional[Sequence[DimensionFilterModel]] = Field(
        default=None, alias="DimensionFilterList"
    )


class CreateAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_name: str = Field(alias="AnomalyDetectorName")
    anomaly_detector_config: AnomalyDetectorConfigModel = Field(
        alias="AnomalyDetectorConfig"
    )
    anomaly_detector_description: Optional[str] = Field(
        default=None, alias="AnomalyDetectorDescription"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateAnomalyDetectorRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    anomaly_detector_description: Optional[str] = Field(
        default=None, alias="AnomalyDetectorDescription"
    )
    anomaly_detector_config: Optional[AnomalyDetectorConfigModel] = Field(
        default=None, alias="AnomalyDetectorConfig"
    )


class AnomalyGroupStatisticsModel(BaseModel):
    evaluation_start_date: Optional[str] = Field(
        default=None, alias="EvaluationStartDate"
    )
    total_count: Optional[int] = Field(default=None, alias="TotalCount")
    itemized_metric_stats_list: Optional[List[ItemizedMetricStatsModel]] = Field(
        default=None, alias="ItemizedMetricStatsList"
    )


class PutFeedbackRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    anomaly_group_time_series_feedback: AnomalyGroupTimeSeriesFeedbackModel = Field(
        alias="AnomalyGroupTimeSeriesFeedback"
    )


class GetFeedbackRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    anomaly_group_time_series_feedback: AnomalyGroupTimeSeriesModel = Field(
        alias="AnomalyGroupTimeSeriesFeedback"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class AthenaSourceConfigModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    data_catalog: Optional[str] = Field(default=None, alias="DataCatalog")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    work_group_name: Optional[str] = Field(default=None, alias="WorkGroupName")
    s3_results_path: Optional[str] = Field(default=None, alias="S3ResultsPath")
    back_test_configuration: Optional[BackTestConfigurationModel] = Field(
        default=None, alias="BackTestConfiguration"
    )


class CloudWatchConfigModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    back_test_configuration: Optional[BackTestConfigurationModel] = Field(
        default=None, alias="BackTestConfiguration"
    )


class DetectedFieldModel(BaseModel):
    value: Optional[AttributeValueModel] = Field(default=None, alias="Value")
    confidence: Optional[Literal["HIGH", "LOW", "NONE"]] = Field(
        default=None, alias="Confidence"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class AutoDetectionMetricSourceModel(BaseModel):
    s3_source_config: Optional[AutoDetectionS3SourceConfigModel] = Field(
        default=None, alias="S3SourceConfig"
    )


class CreateAlertResponseModel(BaseModel):
    alert_arn: str = Field(alias="AlertArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnomalyDetectorResponseModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMetricSetResponseModel(BaseModel):
    metric_set_arn: str = Field(alias="MetricSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAnomalyDetectorResponseModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    anomaly_detector_name: str = Field(alias="AnomalyDetectorName")
    anomaly_detector_description: str = Field(alias="AnomalyDetectorDescription")
    anomaly_detector_config: AnomalyDetectorConfigSummaryModel = Field(
        alias="AnomalyDetectorConfig"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    status: Literal[
        "ACTIVATING",
        "ACTIVE",
        "BACK_TEST_ACTIVATING",
        "BACK_TEST_ACTIVE",
        "BACK_TEST_COMPLETE",
        "DEACTIVATED",
        "DEACTIVATING",
        "DELETING",
        "FAILED",
        "INACTIVE",
        "LEARNING",
    ] = Field(alias="Status")
    failure_reason: str = Field(alias="FailureReason")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    failure_type: Literal[
        "ACTIVATION_FAILURE",
        "BACK_TEST_ACTIVATION_FAILURE",
        "DEACTIVATION_FAILURE",
        "DELETION_FAILURE",
    ] = Field(alias="FailureType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSampleDataResponseModel(BaseModel):
    header_values: List[str] = Field(alias="HeaderValues")
    sample_rows: List[List[str]] = Field(alias="SampleRows")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAlertsResponseModel(BaseModel):
    alert_summary_list: List[AlertSummaryModel] = Field(alias="AlertSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnomalyDetectorsResponseModel(BaseModel):
    anomaly_detector_summary_list: List[AnomalyDetectorSummaryModel] = Field(
        alias="AnomalyDetectorSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAlertResponseModel(BaseModel):
    alert_arn: str = Field(alias="AlertArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnomalyDetectorResponseModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMetricSetResponseModel(BaseModel):
    metric_set_arn: str = Field(alias="MetricSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricSetDataQualityMetricModel(BaseModel):
    metric_set_arn: Optional[str] = Field(default=None, alias="MetricSetArn")
    data_quality_metric_list: Optional[List[DataQualityMetricModel]] = Field(
        default=None, alias="DataQualityMetricList"
    )


class DescribeAnomalyDetectionExecutionsResponseModel(BaseModel):
    execution_list: List[ExecutionStatusModel] = Field(alias="ExecutionList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DimensionContributionModel(BaseModel):
    dimension_name: Optional[str] = Field(default=None, alias="DimensionName")
    dimension_value_contribution_list: Optional[
        List[DimensionValueContributionModel]
    ] = Field(default=None, alias="DimensionValueContributionList")


class TimeSeriesModel(BaseModel):
    time_series_id: str = Field(alias="TimeSeriesId")
    dimension_list: List[DimensionNameValueModel] = Field(alias="DimensionList")
    metric_value_list: List[float] = Field(alias="MetricValueList")


class FileFormatDescriptorModel(BaseModel):
    csv_format_descriptor: Optional[CsvFormatDescriptorModel] = Field(
        default=None, alias="CsvFormatDescriptor"
    )
    json_format_descriptor: Optional[JsonFormatDescriptorModel] = Field(
        default=None, alias="JsonFormatDescriptor"
    )


class MetricSetDimensionFilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    filter_list: Optional[Sequence[FilterModel]] = Field(
        default=None, alias="FilterList"
    )


class GetFeedbackResponseModel(BaseModel):
    anomaly_group_time_series_feedback: List[TimeSeriesFeedbackModel] = Field(
        alias="AnomalyGroupTimeSeriesFeedback"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnomalyGroupRelatedMetricsResponseModel(BaseModel):
    inter_metric_impact_list: List[InterMetricImpactDetailsModel] = Field(
        alias="InterMetricImpactList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMetricSetsResponseModel(BaseModel):
    metric_set_summary_list: List[MetricSetSummaryModel] = Field(
        alias="MetricSetSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RDSSourceConfigModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    database_host: Optional[str] = Field(default=None, alias="DatabaseHost")
    database_port: Optional[int] = Field(default=None, alias="DatabasePort")
    secret_manager_arn: Optional[str] = Field(default=None, alias="SecretManagerArn")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class RedshiftSourceConfigModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    database_host: Optional[str] = Field(default=None, alias="DatabaseHost")
    database_port: Optional[int] = Field(default=None, alias="DatabasePort")
    secret_manager_arn: Optional[str] = Field(default=None, alias="SecretManagerArn")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class AlertModel(BaseModel):
    action: Optional[ActionModel] = Field(default=None, alias="Action")
    alert_description: Optional[str] = Field(default=None, alias="AlertDescription")
    alert_arn: Optional[str] = Field(default=None, alias="AlertArn")
    anomaly_detector_arn: Optional[str] = Field(
        default=None, alias="AnomalyDetectorArn"
    )
    alert_name: Optional[str] = Field(default=None, alias="AlertName")
    alert_sensitivity_threshold: Optional[int] = Field(
        default=None, alias="AlertSensitivityThreshold"
    )
    alert_type: Optional[Literal["LAMBDA", "SNS"]] = Field(
        default=None, alias="AlertType"
    )
    alert_status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="AlertStatus"
    )
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="LastModificationTime"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    alert_filters: Optional[AlertFiltersModel] = Field(
        default=None, alias="AlertFilters"
    )


class CreateAlertRequestModel(BaseModel):
    alert_name: str = Field(alias="AlertName")
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    action: ActionModel = Field(alias="Action")
    alert_sensitivity_threshold: Optional[int] = Field(
        default=None, alias="AlertSensitivityThreshold"
    )
    alert_description: Optional[str] = Field(default=None, alias="AlertDescription")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    alert_filters: Optional[AlertFiltersModel] = Field(
        default=None, alias="AlertFilters"
    )


class UpdateAlertRequestModel(BaseModel):
    alert_arn: str = Field(alias="AlertArn")
    alert_description: Optional[str] = Field(default=None, alias="AlertDescription")
    alert_sensitivity_threshold: Optional[int] = Field(
        default=None, alias="AlertSensitivityThreshold"
    )
    action: Optional[ActionModel] = Field(default=None, alias="Action")
    alert_filters: Optional[AlertFiltersModel] = Field(
        default=None, alias="AlertFilters"
    )


class ListAnomalyGroupSummariesResponseModel(BaseModel):
    anomaly_group_summary_list: List[AnomalyGroupSummaryModel] = Field(
        alias="AnomalyGroupSummaryList"
    )
    anomaly_group_statistics: AnomalyGroupStatisticsModel = Field(
        alias="AnomalyGroupStatistics"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectedCsvFormatDescriptorModel(BaseModel):
    file_compression: Optional[DetectedFieldModel] = Field(
        default=None, alias="FileCompression"
    )
    charset: Optional[DetectedFieldModel] = Field(default=None, alias="Charset")
    contains_header: Optional[DetectedFieldModel] = Field(
        default=None, alias="ContainsHeader"
    )
    delimiter: Optional[DetectedFieldModel] = Field(default=None, alias="Delimiter")
    header_list: Optional[DetectedFieldModel] = Field(default=None, alias="HeaderList")
    quote_symbol: Optional[DetectedFieldModel] = Field(
        default=None, alias="QuoteSymbol"
    )


class DetectedJsonFormatDescriptorModel(BaseModel):
    file_compression: Optional[DetectedFieldModel] = Field(
        default=None, alias="FileCompression"
    )
    charset: Optional[DetectedFieldModel] = Field(default=None, alias="Charset")


class DetectMetricSetConfigRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    auto_detection_metric_source: AutoDetectionMetricSourceModel = Field(
        alias="AutoDetectionMetricSource"
    )


class AnomalyDetectorDataQualityMetricModel(BaseModel):
    start_timestamp: Optional[datetime] = Field(default=None, alias="StartTimestamp")
    metric_set_data_quality_metric_list: Optional[
        List[MetricSetDataQualityMetricModel]
    ] = Field(default=None, alias="MetricSetDataQualityMetricList")


class ContributionMatrixModel(BaseModel):
    dimension_contribution_list: Optional[List[DimensionContributionModel]] = Field(
        default=None, alias="DimensionContributionList"
    )


class ListAnomalyGroupTimeSeriesResponseModel(BaseModel):
    anomaly_group_id: str = Field(alias="AnomalyGroupId")
    metric_name: str = Field(alias="MetricName")
    timestamp_list: List[str] = Field(alias="TimestampList")
    next_token: str = Field(alias="NextToken")
    time_series_list: List[TimeSeriesModel] = Field(alias="TimeSeriesList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3SourceConfigModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    templated_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="TemplatedPathList"
    )
    historical_data_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="HistoricalDataPathList"
    )
    file_format_descriptor: Optional[FileFormatDescriptorModel] = Field(
        default=None, alias="FileFormatDescriptor"
    )


class SampleDataS3SourceConfigModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    file_format_descriptor: FileFormatDescriptorModel = Field(
        alias="FileFormatDescriptor"
    )
    templated_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="TemplatedPathList"
    )
    historical_data_path_list: Optional[Sequence[str]] = Field(
        default=None, alias="HistoricalDataPathList"
    )


class DescribeAlertResponseModel(BaseModel):
    alert: AlertModel = Field(alias="Alert")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectedFileFormatDescriptorModel(BaseModel):
    csv_format_descriptor: Optional[DetectedCsvFormatDescriptorModel] = Field(
        default=None, alias="CsvFormatDescriptor"
    )
    json_format_descriptor: Optional[DetectedJsonFormatDescriptorModel] = Field(
        default=None, alias="JsonFormatDescriptor"
    )


class GetDataQualityMetricsResponseModel(BaseModel):
    anomaly_detector_data_quality_metric_list: List[
        AnomalyDetectorDataQualityMetricModel
    ] = Field(alias="AnomalyDetectorDataQualityMetricList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricLevelImpactModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    num_time_series: Optional[int] = Field(default=None, alias="NumTimeSeries")
    contribution_matrix: Optional[ContributionMatrixModel] = Field(
        default=None, alias="ContributionMatrix"
    )


class MetricSourceModel(BaseModel):
    s3_source_config: Optional[S3SourceConfigModel] = Field(
        default=None, alias="S3SourceConfig"
    )
    app_flow_config: Optional[AppFlowConfigModel] = Field(
        default=None, alias="AppFlowConfig"
    )
    cloud_watch_config: Optional[CloudWatchConfigModel] = Field(
        default=None, alias="CloudWatchConfig"
    )
    rds_source_config: Optional[RDSSourceConfigModel] = Field(
        default=None, alias="RDSSourceConfig"
    )
    redshift_source_config: Optional[RedshiftSourceConfigModel] = Field(
        default=None, alias="RedshiftSourceConfig"
    )
    athena_source_config: Optional[AthenaSourceConfigModel] = Field(
        default=None, alias="AthenaSourceConfig"
    )


class GetSampleDataRequestModel(BaseModel):
    s3_source_config: Optional[SampleDataS3SourceConfigModel] = Field(
        default=None, alias="S3SourceConfig"
    )


class DetectedS3SourceConfigModel(BaseModel):
    file_format_descriptor: Optional[DetectedFileFormatDescriptorModel] = Field(
        default=None, alias="FileFormatDescriptor"
    )


class AnomalyGroupModel(BaseModel):
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    end_time: Optional[str] = Field(default=None, alias="EndTime")
    anomaly_group_id: Optional[str] = Field(default=None, alias="AnomalyGroupId")
    anomaly_group_score: Optional[float] = Field(
        default=None, alias="AnomalyGroupScore"
    )
    primary_metric_name: Optional[str] = Field(default=None, alias="PrimaryMetricName")
    metric_level_impact_list: Optional[List[MetricLevelImpactModel]] = Field(
        default=None, alias="MetricLevelImpactList"
    )


class CreateMetricSetRequestModel(BaseModel):
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    metric_set_name: str = Field(alias="MetricSetName")
    metric_list: Sequence[MetricModel] = Field(alias="MetricList")
    metric_source: MetricSourceModel = Field(alias="MetricSource")
    metric_set_description: Optional[str] = Field(
        default=None, alias="MetricSetDescription"
    )
    offset: Optional[int] = Field(default=None, alias="Offset")
    timestamp_column: Optional[TimestampColumnModel] = Field(
        default=None, alias="TimestampColumn"
    )
    dimension_list: Optional[Sequence[str]] = Field(default=None, alias="DimensionList")
    metric_set_frequency: Optional[Literal["P1D", "PT10M", "PT1H", "PT5M"]] = Field(
        default=None, alias="MetricSetFrequency"
    )
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    dimension_filter_list: Optional[Sequence[MetricSetDimensionFilterModel]] = Field(
        default=None, alias="DimensionFilterList"
    )


class DescribeMetricSetResponseModel(BaseModel):
    metric_set_arn: str = Field(alias="MetricSetArn")
    anomaly_detector_arn: str = Field(alias="AnomalyDetectorArn")
    metric_set_name: str = Field(alias="MetricSetName")
    metric_set_description: str = Field(alias="MetricSetDescription")
    creation_time: datetime = Field(alias="CreationTime")
    last_modification_time: datetime = Field(alias="LastModificationTime")
    offset: int = Field(alias="Offset")
    metric_list: List[MetricModel] = Field(alias="MetricList")
    timestamp_column: TimestampColumnModel = Field(alias="TimestampColumn")
    dimension_list: List[str] = Field(alias="DimensionList")
    metric_set_frequency: Literal["P1D", "PT10M", "PT1H", "PT5M"] = Field(
        alias="MetricSetFrequency"
    )
    timezone: str = Field(alias="Timezone")
    metric_source: MetricSourceModel = Field(alias="MetricSource")
    dimension_filter_list: List[MetricSetDimensionFilterModel] = Field(
        alias="DimensionFilterList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMetricSetRequestModel(BaseModel):
    metric_set_arn: str = Field(alias="MetricSetArn")
    metric_set_description: Optional[str] = Field(
        default=None, alias="MetricSetDescription"
    )
    metric_list: Optional[Sequence[MetricModel]] = Field(
        default=None, alias="MetricList"
    )
    offset: Optional[int] = Field(default=None, alias="Offset")
    timestamp_column: Optional[TimestampColumnModel] = Field(
        default=None, alias="TimestampColumn"
    )
    dimension_list: Optional[Sequence[str]] = Field(default=None, alias="DimensionList")
    metric_set_frequency: Optional[Literal["P1D", "PT10M", "PT1H", "PT5M"]] = Field(
        default=None, alias="MetricSetFrequency"
    )
    metric_source: Optional[MetricSourceModel] = Field(
        default=None, alias="MetricSource"
    )
    dimension_filter_list: Optional[Sequence[MetricSetDimensionFilterModel]] = Field(
        default=None, alias="DimensionFilterList"
    )


class DetectedMetricSourceModel(BaseModel):
    s3_source_config: Optional[DetectedS3SourceConfigModel] = Field(
        default=None, alias="S3SourceConfig"
    )


class GetAnomalyGroupResponseModel(BaseModel):
    anomaly_group: AnomalyGroupModel = Field(alias="AnomalyGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectedMetricSetConfigModel(BaseModel):
    offset: Optional[DetectedFieldModel] = Field(default=None, alias="Offset")
    metric_set_frequency: Optional[DetectedFieldModel] = Field(
        default=None, alias="MetricSetFrequency"
    )
    metric_source: Optional[DetectedMetricSourceModel] = Field(
        default=None, alias="MetricSource"
    )


class DetectMetricSetConfigResponseModel(BaseModel):
    detected_metric_set_config: DetectedMetricSetConfigModel = Field(
        alias="DetectedMetricSetConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
