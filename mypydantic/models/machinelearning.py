# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchPredictionModel(BaseModel):
    batch_prediction_id: Optional[str] = Field(default=None, alias="BatchPredictionId")
    ml_model_id: Optional[str] = Field(default=None, alias="MLModelId")
    batch_prediction_data_source_id: Optional[str] = Field(
        default=None, alias="BatchPredictionDataSourceId"
    )
    input_data_location_s3: Optional[str] = Field(
        default=None, alias="InputDataLocationS3"
    )
    created_by_iam_user: Optional[str] = Field(default=None, alias="CreatedByIamUser")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
    ] = Field(default=None, alias="Status")
    output_uri: Optional[str] = Field(default=None, alias="OutputUri")
    message: Optional[str] = Field(default=None, alias="Message")
    compute_time: Optional[int] = Field(default=None, alias="ComputeTime")
    finished_at: Optional[datetime] = Field(default=None, alias="FinishedAt")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")
    total_record_count: Optional[int] = Field(default=None, alias="TotalRecordCount")
    invalid_record_count: Optional[int] = Field(
        default=None, alias="InvalidRecordCount"
    )


class CreateBatchPredictionInputRequestModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    ml_model_id: str = Field(alias="MLModelId")
    batch_prediction_data_source_id: str = Field(alias="BatchPredictionDataSourceId")
    output_uri: str = Field(alias="OutputUri")
    batch_prediction_name: Optional[str] = Field(
        default=None, alias="BatchPredictionName"
    )


class S3DataSpecModel(BaseModel):
    data_location_s3: str = Field(alias="DataLocationS3")
    data_rearrangement: Optional[str] = Field(default=None, alias="DataRearrangement")
    data_schema: Optional[str] = Field(default=None, alias="DataSchema")
    data_schema_location_s3: Optional[str] = Field(
        default=None, alias="DataSchemaLocationS3"
    )


class CreateEvaluationInputRequestModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    ml_model_id: str = Field(alias="MLModelId")
    evaluation_data_source_id: str = Field(alias="EvaluationDataSourceId")
    evaluation_name: Optional[str] = Field(default=None, alias="EvaluationName")


class CreateMLModelInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    ml_model_type: Literal["BINARY", "MULTICLASS", "REGRESSION"] = Field(
        alias="MLModelType"
    )
    training_data_source_id: str = Field(alias="TrainingDataSourceId")
    ml_model_name: Optional[str] = Field(default=None, alias="MLModelName")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    recipe: Optional[str] = Field(default=None, alias="Recipe")
    recipe_uri: Optional[str] = Field(default=None, alias="RecipeUri")


class CreateRealtimeEndpointInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")


class RealtimeEndpointInfoModel(BaseModel):
    peak_requests_per_second: Optional[int] = Field(
        default=None, alias="PeakRequestsPerSecond"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    endpoint_url: Optional[str] = Field(default=None, alias="EndpointUrl")
    endpoint_status: Optional[Literal["FAILED", "NONE", "READY", "UPDATING"]] = Field(
        default=None, alias="EndpointStatus"
    )


class DeleteBatchPredictionInputRequestModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")


class DeleteDataSourceInputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")


class DeleteEvaluationInputRequestModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")


class DeleteMLModelInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")


class DeleteRealtimeEndpointInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")


class DeleteTagsInputRequestModel(BaseModel):
    tag_keys: Sequence[str] = Field(alias="TagKeys")
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeBatchPredictionsInputRequestModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeDataSourcesInputRequestModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt", "DataLocationS3", "IAMUser", "LastUpdatedAt", "Name", "Status"
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeEvaluationsInputRequestModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeMLModelsInputRequestModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "Algorithm",
            "CreatedAt",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelType",
            "Name",
            "RealtimeEndpointStatus",
            "Status",
            "TrainingDataSourceId",
            "TrainingDataURI",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeTagsInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")


class PerformanceMetricsModel(BaseModel):
    properties: Optional[Dict[str, str]] = Field(default=None, alias="Properties")


class GetBatchPredictionInputRequestModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")


class GetDataSourceInputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    verbose: Optional[bool] = Field(default=None, alias="Verbose")


class GetEvaluationInputRequestModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")


class GetMLModelInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    verbose: Optional[bool] = Field(default=None, alias="Verbose")


class PredictInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    record: Mapping[str, str] = Field(alias="Record")
    predict_endpoint: str = Field(alias="PredictEndpoint")


class PredictionModel(BaseModel):
    predicted_label: Optional[str] = Field(default=None, alias="predictedLabel")
    predicted_value: Optional[float] = Field(default=None, alias="predictedValue")
    predicted_scores: Optional[Dict[str, float]] = Field(
        default=None, alias="predictedScores"
    )
    details: Optional[Dict[Literal["Algorithm", "PredictiveModelType"], str]] = Field(
        default=None, alias="details"
    )


class RDSDatabaseCredentialsModel(BaseModel):
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")


class RDSDatabaseModel(BaseModel):
    instance_identifier: str = Field(alias="InstanceIdentifier")
    database_name: str = Field(alias="DatabaseName")


class RedshiftDatabaseCredentialsModel(BaseModel):
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")


class RedshiftDatabaseModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class UpdateBatchPredictionInputRequestModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    batch_prediction_name: str = Field(alias="BatchPredictionName")


class UpdateDataSourceInputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    data_source_name: str = Field(alias="DataSourceName")


class UpdateEvaluationInputRequestModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    evaluation_name: str = Field(alias="EvaluationName")


class UpdateMLModelInputRequestModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    ml_model_name: Optional[str] = Field(default=None, alias="MLModelName")
    score_threshold: Optional[float] = Field(default=None, alias="ScoreThreshold")


class AddTagsInputRequestModel(BaseModel):
    tags: Sequence[TagModel] = Field(alias="Tags")
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")


class AddTagsOutputModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBatchPredictionOutputModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceFromRDSOutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceFromRedshiftOutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceFromS3OutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEvaluationOutputModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMLModelOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBatchPredictionOutputModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDataSourceOutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEvaluationOutputModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMLModelOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTagsOutputModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTagsOutputModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "BatchPrediction", "DataSource", "Evaluation", "MLModel"
    ] = Field(alias="ResourceType")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBatchPredictionOutputModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    ml_model_id: str = Field(alias="MLModelId")
    batch_prediction_data_source_id: str = Field(alias="BatchPredictionDataSourceId")
    input_data_location_s3: str = Field(alias="InputDataLocationS3")
    created_by_iam_user: str = Field(alias="CreatedByIamUser")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    name: str = Field(alias="Name")
    status: Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"] = Field(
        alias="Status"
    )
    output_uri: str = Field(alias="OutputUri")
    log_uri: str = Field(alias="LogUri")
    message: str = Field(alias="Message")
    compute_time: int = Field(alias="ComputeTime")
    finished_at: datetime = Field(alias="FinishedAt")
    started_at: datetime = Field(alias="StartedAt")
    total_record_count: int = Field(alias="TotalRecordCount")
    invalid_record_count: int = Field(alias="InvalidRecordCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBatchPredictionOutputModel(BaseModel):
    batch_prediction_id: str = Field(alias="BatchPredictionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSourceOutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEvaluationOutputModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMLModelOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBatchPredictionsOutputModel(BaseModel):
    results: List[BatchPredictionModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceFromS3InputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    data_spec: S3DataSpecModel = Field(alias="DataSpec")
    data_source_name: Optional[str] = Field(default=None, alias="DataSourceName")
    compute_statistics: Optional[bool] = Field(default=None, alias="ComputeStatistics")


class CreateRealtimeEndpointOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    realtime_endpoint_info: RealtimeEndpointInfoModel = Field(
        alias="RealtimeEndpointInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRealtimeEndpointOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    realtime_endpoint_info: RealtimeEndpointInfoModel = Field(
        alias="RealtimeEndpointInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMLModelOutputModel(BaseModel):
    ml_model_id: str = Field(alias="MLModelId")
    training_data_source_id: str = Field(alias="TrainingDataSourceId")
    created_by_iam_user: str = Field(alias="CreatedByIamUser")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    name: str = Field(alias="Name")
    status: Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"] = Field(
        alias="Status"
    )
    size_in_bytes: int = Field(alias="SizeInBytes")
    endpoint_info: RealtimeEndpointInfoModel = Field(alias="EndpointInfo")
    training_parameters: Dict[str, str] = Field(alias="TrainingParameters")
    input_data_location_s3: str = Field(alias="InputDataLocationS3")
    ml_model_type: Literal["BINARY", "MULTICLASS", "REGRESSION"] = Field(
        alias="MLModelType"
    )
    score_threshold: float = Field(alias="ScoreThreshold")
    score_threshold_last_updated_at: datetime = Field(
        alias="ScoreThresholdLastUpdatedAt"
    )
    log_uri: str = Field(alias="LogUri")
    message: str = Field(alias="Message")
    compute_time: int = Field(alias="ComputeTime")
    finished_at: datetime = Field(alias="FinishedAt")
    started_at: datetime = Field(alias="StartedAt")
    recipe: str = Field(alias="Recipe")
    schema_: str = Field(alias="Schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MLModelModel(BaseModel):
    ml_model_id: Optional[str] = Field(default=None, alias="MLModelId")
    training_data_source_id: Optional[str] = Field(
        default=None, alias="TrainingDataSourceId"
    )
    created_by_iam_user: Optional[str] = Field(default=None, alias="CreatedByIamUser")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
    ] = Field(default=None, alias="Status")
    size_in_bytes: Optional[int] = Field(default=None, alias="SizeInBytes")
    endpoint_info: Optional[RealtimeEndpointInfoModel] = Field(
        default=None, alias="EndpointInfo"
    )
    training_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="TrainingParameters"
    )
    input_data_location_s3: Optional[str] = Field(
        default=None, alias="InputDataLocationS3"
    )
    algorithm: Optional[Literal["sgd"]] = Field(default=None, alias="Algorithm")
    ml_model_type: Optional[Literal["BINARY", "MULTICLASS", "REGRESSION"]] = Field(
        default=None, alias="MLModelType"
    )
    score_threshold: Optional[float] = Field(default=None, alias="ScoreThreshold")
    score_threshold_last_updated_at: Optional[datetime] = Field(
        default=None, alias="ScoreThresholdLastUpdatedAt"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    compute_time: Optional[int] = Field(default=None, alias="ComputeTime")
    finished_at: Optional[datetime] = Field(default=None, alias="FinishedAt")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")


class DescribeBatchPredictionsInputBatchPredictionAvailableWaitModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDataSourcesInputDataSourceAvailableWaitModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt", "DataLocationS3", "IAMUser", "LastUpdatedAt", "Name", "Status"
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEvaluationsInputEvaluationAvailableWaitModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeMLModelsInputMLModelAvailableWaitModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "Algorithm",
            "CreatedAt",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelType",
            "Name",
            "RealtimeEndpointStatus",
            "Status",
            "TrainingDataSourceId",
            "TrainingDataURI",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBatchPredictionsInputDescribeBatchPredictionsPaginateModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDataSourcesInputDescribeDataSourcesPaginateModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt", "DataLocationS3", "IAMUser", "LastUpdatedAt", "Name", "Status"
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEvaluationsInputDescribeEvaluationsPaginateModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "CreatedAt",
            "DataSourceId",
            "DataURI",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelId",
            "Name",
            "Status",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMLModelsInputDescribeMLModelsPaginateModel(BaseModel):
    filter_variable: Optional[
        Literal[
            "Algorithm",
            "CreatedAt",
            "IAMUser",
            "LastUpdatedAt",
            "MLModelType",
            "Name",
            "RealtimeEndpointStatus",
            "Status",
            "TrainingDataSourceId",
            "TrainingDataURI",
        ]
    ] = Field(default=None, alias="FilterVariable")
    eq: Optional[str] = Field(default=None, alias="EQ")
    gt: Optional[str] = Field(default=None, alias="GT")
    l_t: Optional[str] = Field(default=None, alias="LT")
    ge: Optional[str] = Field(default=None, alias="GE")
    l_e: Optional[str] = Field(default=None, alias="LE")
    ne: Optional[str] = Field(default=None, alias="NE")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    sort_order: Optional[Literal["asc", "dsc"]] = Field(default=None, alias="SortOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class EvaluationModel(BaseModel):
    evaluation_id: Optional[str] = Field(default=None, alias="EvaluationId")
    ml_model_id: Optional[str] = Field(default=None, alias="MLModelId")
    evaluation_data_source_id: Optional[str] = Field(
        default=None, alias="EvaluationDataSourceId"
    )
    input_data_location_s3: Optional[str] = Field(
        default=None, alias="InputDataLocationS3"
    )
    created_by_iam_user: Optional[str] = Field(default=None, alias="CreatedByIamUser")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
    ] = Field(default=None, alias="Status")
    performance_metrics: Optional[PerformanceMetricsModel] = Field(
        default=None, alias="PerformanceMetrics"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    compute_time: Optional[int] = Field(default=None, alias="ComputeTime")
    finished_at: Optional[datetime] = Field(default=None, alias="FinishedAt")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")


class GetEvaluationOutputModel(BaseModel):
    evaluation_id: str = Field(alias="EvaluationId")
    ml_model_id: str = Field(alias="MLModelId")
    evaluation_data_source_id: str = Field(alias="EvaluationDataSourceId")
    input_data_location_s3: str = Field(alias="InputDataLocationS3")
    created_by_iam_user: str = Field(alias="CreatedByIamUser")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    name: str = Field(alias="Name")
    status: Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"] = Field(
        alias="Status"
    )
    performance_metrics: PerformanceMetricsModel = Field(alias="PerformanceMetrics")
    log_uri: str = Field(alias="LogUri")
    message: str = Field(alias="Message")
    compute_time: int = Field(alias="ComputeTime")
    finished_at: datetime = Field(alias="FinishedAt")
    started_at: datetime = Field(alias="StartedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PredictOutputModel(BaseModel):
    prediction: PredictionModel = Field(alias="Prediction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RDSDataSpecModel(BaseModel):
    database_information: RDSDatabaseModel = Field(alias="DatabaseInformation")
    select_sql_query: str = Field(alias="SelectSqlQuery")
    database_credentials: RDSDatabaseCredentialsModel = Field(
        alias="DatabaseCredentials"
    )
    s3_staging_location: str = Field(alias="S3StagingLocation")
    resource_role: str = Field(alias="ResourceRole")
    service_role: str = Field(alias="ServiceRole")
    subnet_id: str = Field(alias="SubnetId")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    data_rearrangement: Optional[str] = Field(default=None, alias="DataRearrangement")
    data_schema: Optional[str] = Field(default=None, alias="DataSchema")
    data_schema_uri: Optional[str] = Field(default=None, alias="DataSchemaUri")


class RDSMetadataModel(BaseModel):
    database: Optional[RDSDatabaseModel] = Field(default=None, alias="Database")
    database_user_name: Optional[str] = Field(default=None, alias="DatabaseUserName")
    select_sql_query: Optional[str] = Field(default=None, alias="SelectSqlQuery")
    resource_role: Optional[str] = Field(default=None, alias="ResourceRole")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    data_pipeline_id: Optional[str] = Field(default=None, alias="DataPipelineId")


class RedshiftDataSpecModel(BaseModel):
    database_information: RedshiftDatabaseModel = Field(alias="DatabaseInformation")
    select_sql_query: str = Field(alias="SelectSqlQuery")
    database_credentials: RedshiftDatabaseCredentialsModel = Field(
        alias="DatabaseCredentials"
    )
    s3_staging_location: str = Field(alias="S3StagingLocation")
    data_rearrangement: Optional[str] = Field(default=None, alias="DataRearrangement")
    data_schema: Optional[str] = Field(default=None, alias="DataSchema")
    data_schema_uri: Optional[str] = Field(default=None, alias="DataSchemaUri")


class RedshiftMetadataModel(BaseModel):
    redshift_database: Optional[RedshiftDatabaseModel] = Field(
        default=None, alias="RedshiftDatabase"
    )
    database_user_name: Optional[str] = Field(default=None, alias="DatabaseUserName")
    select_sql_query: Optional[str] = Field(default=None, alias="SelectSqlQuery")


class DescribeMLModelsOutputModel(BaseModel):
    results: List[MLModelModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEvaluationsOutputModel(BaseModel):
    results: List[EvaluationModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceFromRDSInputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    rds_data: RDSDataSpecModel = Field(alias="RDSData")
    role_arn: str = Field(alias="RoleARN")
    data_source_name: Optional[str] = Field(default=None, alias="DataSourceName")
    compute_statistics: Optional[bool] = Field(default=None, alias="ComputeStatistics")


class CreateDataSourceFromRedshiftInputRequestModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    data_spec: RedshiftDataSpecModel = Field(alias="DataSpec")
    role_arn: str = Field(alias="RoleARN")
    data_source_name: Optional[str] = Field(default=None, alias="DataSourceName")
    compute_statistics: Optional[bool] = Field(default=None, alias="ComputeStatistics")


class DataSourceModel(BaseModel):
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    data_location_s3: Optional[str] = Field(default=None, alias="DataLocationS3")
    data_rearrangement: Optional[str] = Field(default=None, alias="DataRearrangement")
    created_by_iam_user: Optional[str] = Field(default=None, alias="CreatedByIamUser")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    data_size_in_bytes: Optional[int] = Field(default=None, alias="DataSizeInBytes")
    number_of_files: Optional[int] = Field(default=None, alias="NumberOfFiles")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    redshift_metadata: Optional[RedshiftMetadataModel] = Field(
        default=None, alias="RedshiftMetadata"
    )
    rds_metadata: Optional[RDSMetadataModel] = Field(default=None, alias="RDSMetadata")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    compute_statistics: Optional[bool] = Field(default=None, alias="ComputeStatistics")
    compute_time: Optional[int] = Field(default=None, alias="ComputeTime")
    finished_at: Optional[datetime] = Field(default=None, alias="FinishedAt")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")


class GetDataSourceOutputModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    data_location_s3: str = Field(alias="DataLocationS3")
    data_rearrangement: str = Field(alias="DataRearrangement")
    created_by_iam_user: str = Field(alias="CreatedByIamUser")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    data_size_in_bytes: int = Field(alias="DataSizeInBytes")
    number_of_files: int = Field(alias="NumberOfFiles")
    name: str = Field(alias="Name")
    status: Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"] = Field(
        alias="Status"
    )
    log_uri: str = Field(alias="LogUri")
    message: str = Field(alias="Message")
    redshift_metadata: RedshiftMetadataModel = Field(alias="RedshiftMetadata")
    rds_metadata: RDSMetadataModel = Field(alias="RDSMetadata")
    role_arn: str = Field(alias="RoleARN")
    compute_statistics: bool = Field(alias="ComputeStatistics")
    compute_time: int = Field(alias="ComputeTime")
    finished_at: datetime = Field(alias="FinishedAt")
    started_at: datetime = Field(alias="StartedAt")
    data_source_schema: str = Field(alias="DataSourceSchema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSourcesOutputModel(BaseModel):
    results: List[DataSourceModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
