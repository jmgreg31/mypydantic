# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlgorithmImageModel(BaseModel):
    docker_uri: str = Field(alias="dockerURI")
    name: Optional[str] = Field(default=None, alias="name")


class AutoMLConfigModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    recipe_list: Optional[Sequence[str]] = Field(default=None, alias="recipeList")


class AutoMLResultModel(BaseModel):
    best_recipe_arn: Optional[str] = Field(default=None, alias="bestRecipeArn")


class BatchInferenceJobConfigModel(BaseModel):
    item_exploration_config: Optional[Mapping[str, str]] = Field(
        default=None, alias="itemExplorationConfig"
    )


class S3DataConfigModel(BaseModel):
    path: str = Field(alias="path")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class BatchInferenceJobSummaryModel(BaseModel):
    batch_inference_job_arn: Optional[str] = Field(
        default=None, alias="batchInferenceJobArn"
    )
    job_name: Optional[str] = Field(default=None, alias="jobName")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )


class BatchSegmentJobSummaryModel(BaseModel):
    batch_segment_job_arn: Optional[str] = Field(
        default=None, alias="batchSegmentJobArn"
    )
    job_name: Optional[str] = Field(default=None, alias="jobName")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )


class CampaignConfigModel(BaseModel):
    item_exploration_config: Optional[Mapping[str, str]] = Field(
        default=None, alias="itemExplorationConfig"
    )


class CampaignSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    campaign_arn: Optional[str] = Field(default=None, alias="campaignArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class CategoricalHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ContinuousHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    min_value: Optional[float] = Field(default=None, alias="minValue")
    max_value: Optional[float] = Field(default=None, alias="maxValue")


class TagModel(BaseModel):
    tag_key: str = Field(alias="tagKey")
    tag_value: str = Field(alias="tagValue")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DataSourceModel(BaseModel):
    data_location: Optional[str] = Field(default=None, alias="dataLocation")


class MetricAttributeModel(BaseModel):
    event_type: str = Field(alias="eventType")
    metric_name: str = Field(alias="metricName")
    expression: str = Field(alias="expression")


class RecommenderConfigModel(BaseModel):
    item_exploration_config: Optional[Mapping[str, str]] = Field(
        default=None, alias="itemExplorationConfig"
    )
    min_recommendation_requests_per_second: Optional[int] = Field(
        default=None, alias="minRecommendationRequestsPerSecond"
    )


class CreateSchemaRequestModel(BaseModel):
    name: str = Field(alias="name")
    schema_: str = Field(alias="schema")
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class DatasetExportJobSummaryModel(BaseModel):
    dataset_export_job_arn: Optional[str] = Field(
        default=None, alias="datasetExportJobArn"
    )
    job_name: Optional[str] = Field(default=None, alias="jobName")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class DatasetGroupSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class DatasetGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    status: Optional[str] = Field(default=None, alias="status")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class DatasetImportJobSummaryModel(BaseModel):
    dataset_import_job_arn: Optional[str] = Field(
        default=None, alias="datasetImportJobArn"
    )
    job_name: Optional[str] = Field(default=None, alias="jobName")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    import_mode: Optional[Literal["FULL", "INCREMENTAL"]] = Field(
        default=None, alias="importMode"
    )


class DatasetSchemaSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    schema_arn: Optional[str] = Field(default=None, alias="schemaArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class DatasetSchemaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    schema_arn: Optional[str] = Field(default=None, alias="schemaArn")
    schema_: Optional[str] = Field(default=None, alias="schema")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class DatasetSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    dataset_type: Optional[str] = Field(default=None, alias="datasetType")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class DatasetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    dataset_type: Optional[str] = Field(default=None, alias="datasetType")
    schema_arn: Optional[str] = Field(default=None, alias="schemaArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class DefaultCategoricalHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[List[str]] = Field(default=None, alias="values")
    is_tunable: Optional[bool] = Field(default=None, alias="isTunable")


class DefaultContinuousHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    min_value: Optional[float] = Field(default=None, alias="minValue")
    max_value: Optional[float] = Field(default=None, alias="maxValue")
    is_tunable: Optional[bool] = Field(default=None, alias="isTunable")


class DefaultIntegerHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    min_value: Optional[int] = Field(default=None, alias="minValue")
    max_value: Optional[int] = Field(default=None, alias="maxValue")
    is_tunable: Optional[bool] = Field(default=None, alias="isTunable")


class DeleteCampaignRequestModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")


class DeleteDatasetGroupRequestModel(BaseModel):
    dataset_group_arn: str = Field(alias="datasetGroupArn")


class DeleteDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="datasetArn")


class DeleteEventTrackerRequestModel(BaseModel):
    event_tracker_arn: str = Field(alias="eventTrackerArn")


class DeleteFilterRequestModel(BaseModel):
    filter_arn: str = Field(alias="filterArn")


class DeleteMetricAttributionRequestModel(BaseModel):
    metric_attribution_arn: str = Field(alias="metricAttributionArn")


class DeleteRecommenderRequestModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")


class DeleteSchemaRequestModel(BaseModel):
    schema_arn: str = Field(alias="schemaArn")


class DeleteSolutionRequestModel(BaseModel):
    solution_arn: str = Field(alias="solutionArn")


class DescribeAlgorithmRequestModel(BaseModel):
    algorithm_arn: str = Field(alias="algorithmArn")


class DescribeBatchInferenceJobRequestModel(BaseModel):
    batch_inference_job_arn: str = Field(alias="batchInferenceJobArn")


class DescribeBatchSegmentJobRequestModel(BaseModel):
    batch_segment_job_arn: str = Field(alias="batchSegmentJobArn")


class DescribeCampaignRequestModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")


class DescribeDatasetExportJobRequestModel(BaseModel):
    dataset_export_job_arn: str = Field(alias="datasetExportJobArn")


class DescribeDatasetGroupRequestModel(BaseModel):
    dataset_group_arn: str = Field(alias="datasetGroupArn")


class DescribeDatasetImportJobRequestModel(BaseModel):
    dataset_import_job_arn: str = Field(alias="datasetImportJobArn")


class DescribeDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="datasetArn")


class DescribeEventTrackerRequestModel(BaseModel):
    event_tracker_arn: str = Field(alias="eventTrackerArn")


class EventTrackerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    event_tracker_arn: Optional[str] = Field(default=None, alias="eventTrackerArn")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    tracking_id: Optional[str] = Field(default=None, alias="trackingId")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class DescribeFeatureTransformationRequestModel(BaseModel):
    feature_transformation_arn: str = Field(alias="featureTransformationArn")


class FeatureTransformationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    feature_transformation_arn: Optional[str] = Field(
        default=None, alias="featureTransformationArn"
    )
    default_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="defaultParameters"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    status: Optional[str] = Field(default=None, alias="status")


class DescribeFilterRequestModel(BaseModel):
    filter_arn: str = Field(alias="filterArn")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    filter_expression: Optional[str] = Field(default=None, alias="filterExpression")
    status: Optional[str] = Field(default=None, alias="status")


class DescribeMetricAttributionRequestModel(BaseModel):
    metric_attribution_arn: str = Field(alias="metricAttributionArn")


class DescribeRecipeRequestModel(BaseModel):
    recipe_arn: str = Field(alias="recipeArn")


class RecipeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    algorithm_arn: Optional[str] = Field(default=None, alias="algorithmArn")
    feature_transformation_arn: Optional[str] = Field(
        default=None, alias="featureTransformationArn"
    )
    status: Optional[str] = Field(default=None, alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    recipe_type: Optional[str] = Field(default=None, alias="recipeType")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class DescribeRecommenderRequestModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")


class DescribeSchemaRequestModel(BaseModel):
    schema_arn: str = Field(alias="schemaArn")


class DescribeSolutionRequestModel(BaseModel):
    solution_arn: str = Field(alias="solutionArn")


class DescribeSolutionVersionRequestModel(BaseModel):
    solution_version_arn: str = Field(alias="solutionVersionArn")


class EventTrackerSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    event_tracker_arn: Optional[str] = Field(default=None, alias="eventTrackerArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class FilterSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    status: Optional[str] = Field(default=None, alias="status")


class GetSolutionMetricsRequestModel(BaseModel):
    solution_version_arn: str = Field(alias="solutionVersionArn")


class HPOObjectiveModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    metric_regex: Optional[str] = Field(default=None, alias="metricRegex")


class HPOResourceConfigModel(BaseModel):
    max_number_of_training_jobs: Optional[str] = Field(
        default=None, alias="maxNumberOfTrainingJobs"
    )
    max_parallel_training_jobs: Optional[str] = Field(
        default=None, alias="maxParallelTrainingJobs"
    )


class IntegerHyperParameterRangeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    min_value: Optional[int] = Field(default=None, alias="minValue")
    max_value: Optional[int] = Field(default=None, alias="maxValue")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBatchInferenceJobsRequestModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListBatchSegmentJobsRequestModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListCampaignsRequestModel(BaseModel):
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetExportJobsRequestModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetImportJobsRequestModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetsRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListEventTrackersRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFiltersRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListMetricAttributionMetricsRequestModel(BaseModel):
    metric_attribution_arn: Optional[str] = Field(
        default=None, alias="metricAttributionArn"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListMetricAttributionsRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class MetricAttributionSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    metric_attribution_arn: Optional[str] = Field(
        default=None, alias="metricAttributionArn"
    )
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class ListRecipesRequestModel(BaseModel):
    recipe_provider: Optional[Literal["SERVICE"]] = Field(
        default=None, alias="recipeProvider"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class RecipeSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )


class ListRecommendersRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListSchemasRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListSolutionVersionsRequestModel(BaseModel):
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SolutionVersionSummaryModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class ListSolutionsRequestModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SolutionSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class OptimizationObjectiveModel(BaseModel):
    item_attribute: Optional[str] = Field(default=None, alias="itemAttribute")
    objective_sensitivity: Optional[Literal["HIGH", "LOW", "MEDIUM", "OFF"]] = Field(
        default=None, alias="objectiveSensitivity"
    )


class TunedHPOParamsModel(BaseModel):
    algorithm_hyper_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="algorithmHyperParameters"
    )


class StartRecommenderRequestModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")


class StopRecommenderRequestModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")


class StopSolutionVersionCreationRequestModel(BaseModel):
    solution_version_arn: str = Field(alias="solutionVersionArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchInferenceJobInputModel(BaseModel):
    s3_data_source: S3DataConfigModel = Field(alias="s3DataSource")


class BatchInferenceJobOutputModel(BaseModel):
    s3_data_destination: S3DataConfigModel = Field(alias="s3DataDestination")


class BatchSegmentJobInputModel(BaseModel):
    s3_data_source: S3DataConfigModel = Field(alias="s3DataSource")


class BatchSegmentJobOutputModel(BaseModel):
    s3_data_destination: S3DataConfigModel = Field(alias="s3DataDestination")


class DatasetExportJobOutputModel(BaseModel):
    s3_data_destination: S3DataConfigModel = Field(alias="s3DataDestination")


class MetricAttributionOutputModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    s3_data_destination: Optional[S3DataConfigModel] = Field(
        default=None, alias="s3DataDestination"
    )


class CampaignUpdateSummaryModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    min_provisioned_tp_s: Optional[int] = Field(default=None, alias="minProvisionedTPS")
    campaign_config: Optional[CampaignConfigModel] = Field(
        default=None, alias="campaignConfig"
    )
    status: Optional[str] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class UpdateCampaignRequestModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    min_provisioned_tp_s: Optional[int] = Field(default=None, alias="minProvisionedTPS")
    campaign_config: Optional[CampaignConfigModel] = Field(
        default=None, alias="campaignConfig"
    )


class CreateCampaignRequestModel(BaseModel):
    name: str = Field(alias="name")
    solution_version_arn: str = Field(alias="solutionVersionArn")
    min_provisioned_tp_s: Optional[int] = Field(default=None, alias="minProvisionedTPS")
    campaign_config: Optional[CampaignConfigModel] = Field(
        default=None, alias="campaignConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDatasetGroupRequestModel(BaseModel):
    name: str = Field(alias="name")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDatasetRequestModel(BaseModel):
    name: str = Field(alias="name")
    schema_arn: str = Field(alias="schemaArn")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    dataset_type: str = Field(alias="datasetType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateEventTrackerRequestModel(BaseModel):
    name: str = Field(alias="name")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateFilterRequestModel(BaseModel):
    name: str = Field(alias="name")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    filter_expression: str = Field(alias="filterExpression")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateSolutionVersionRequestModel(BaseModel):
    solution_arn: str = Field(alias="solutionArn")
    name: Optional[str] = Field(default=None, alias="name")
    training_mode: Optional[Literal["FULL", "UPDATE"]] = Field(
        default=None, alias="trainingMode"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateBatchInferenceJobResponseModel(BaseModel):
    batch_inference_job_arn: str = Field(alias="batchInferenceJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBatchSegmentJobResponseModel(BaseModel):
    batch_segment_job_arn: str = Field(alias="batchSegmentJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCampaignResponseModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetExportJobResponseModel(BaseModel):
    dataset_export_job_arn: str = Field(alias="datasetExportJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetGroupResponseModel(BaseModel):
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    domain: Literal["ECOMMERCE", "VIDEO_ON_DEMAND"] = Field(alias="domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetImportJobResponseModel(BaseModel):
    dataset_import_job_arn: str = Field(alias="datasetImportJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    dataset_arn: str = Field(alias="datasetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventTrackerResponseModel(BaseModel):
    event_tracker_arn: str = Field(alias="eventTrackerArn")
    tracking_id: str = Field(alias="trackingId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFilterResponseModel(BaseModel):
    filter_arn: str = Field(alias="filterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMetricAttributionResponseModel(BaseModel):
    metric_attribution_arn: str = Field(alias="metricAttributionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecommenderResponseModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="schemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSolutionResponseModel(BaseModel):
    solution_arn: str = Field(alias="solutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSolutionVersionResponseModel(BaseModel):
    solution_version_arn: str = Field(alias="solutionVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolutionMetricsResponseModel(BaseModel):
    solution_version_arn: str = Field(alias="solutionVersionArn")
    metrics: Dict[str, float] = Field(alias="metrics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBatchInferenceJobsResponseModel(BaseModel):
    batch_inference_jobs: List[BatchInferenceJobSummaryModel] = Field(
        alias="batchInferenceJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBatchSegmentJobsResponseModel(BaseModel):
    batch_segment_jobs: List[BatchSegmentJobSummaryModel] = Field(
        alias="batchSegmentJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCampaignsResponseModel(BaseModel):
    campaigns: List[CampaignSummaryModel] = Field(alias="campaigns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRecommenderResponseModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopRecommenderResponseModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCampaignResponseModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMetricAttributionResponseModel(BaseModel):
    metric_attribution_arn: str = Field(alias="metricAttributionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecommenderResponseModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetImportJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    dataset_arn: str = Field(alias="datasetArn")
    data_source: DataSourceModel = Field(alias="dataSource")
    role_arn: str = Field(alias="roleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    import_mode: Optional[Literal["FULL", "INCREMENTAL"]] = Field(
        default=None, alias="importMode"
    )
    publish_attribution_metrics_to_s3: Optional[bool] = Field(
        default=None, alias="publishAttributionMetricsToS3"
    )


class DatasetImportJobModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="jobName")
    dataset_import_job_arn: Optional[str] = Field(
        default=None, alias="datasetImportJobArn"
    )
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    data_source: Optional[DataSourceModel] = Field(default=None, alias="dataSource")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    import_mode: Optional[Literal["FULL", "INCREMENTAL"]] = Field(
        default=None, alias="importMode"
    )
    publish_attribution_metrics_to_s3: Optional[bool] = Field(
        default=None, alias="publishAttributionMetricsToS3"
    )


class ListMetricAttributionMetricsResponseModel(BaseModel):
    metrics: List[MetricAttributeModel] = Field(alias="metrics")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecommenderRequestModel(BaseModel):
    name: str = Field(alias="name")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    recipe_arn: str = Field(alias="recipeArn")
    recommender_config: Optional[RecommenderConfigModel] = Field(
        default=None, alias="recommenderConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class RecommenderSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    recommender_arn: Optional[str] = Field(default=None, alias="recommenderArn")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    recommender_config: Optional[RecommenderConfigModel] = Field(
        default=None, alias="recommenderConfig"
    )
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class RecommenderUpdateSummaryModel(BaseModel):
    recommender_config: Optional[RecommenderConfigModel] = Field(
        default=None, alias="recommenderConfig"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    status: Optional[str] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class UpdateRecommenderRequestModel(BaseModel):
    recommender_arn: str = Field(alias="recommenderArn")
    recommender_config: RecommenderConfigModel = Field(alias="recommenderConfig")


class ListDatasetExportJobsResponseModel(BaseModel):
    dataset_export_jobs: List[DatasetExportJobSummaryModel] = Field(
        alias="datasetExportJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetGroupsResponseModel(BaseModel):
    dataset_groups: List[DatasetGroupSummaryModel] = Field(alias="datasetGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetGroupResponseModel(BaseModel):
    dataset_group: DatasetGroupModel = Field(alias="datasetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetImportJobsResponseModel(BaseModel):
    dataset_import_jobs: List[DatasetImportJobSummaryModel] = Field(
        alias="datasetImportJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemasResponseModel(BaseModel):
    schemas: List[DatasetSchemaSummaryModel] = Field(alias="schemas")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSchemaResponseModel(BaseModel):
    schema_: DatasetSchemaModel = Field(alias="schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    datasets: List[DatasetSummaryModel] = Field(alias="datasets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetResponseModel(BaseModel):
    dataset: DatasetModel = Field(alias="dataset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefaultHyperParameterRangesModel(BaseModel):
    integer_hyper_parameter_ranges: Optional[
        List[DefaultIntegerHyperParameterRangeModel]
    ] = Field(default=None, alias="integerHyperParameterRanges")
    continuous_hyper_parameter_ranges: Optional[
        List[DefaultContinuousHyperParameterRangeModel]
    ] = Field(default=None, alias="continuousHyperParameterRanges")
    categorical_hyper_parameter_ranges: Optional[
        List[DefaultCategoricalHyperParameterRangeModel]
    ] = Field(default=None, alias="categoricalHyperParameterRanges")


class DescribeEventTrackerResponseModel(BaseModel):
    event_tracker: EventTrackerModel = Field(alias="eventTracker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFeatureTransformationResponseModel(BaseModel):
    feature_transformation: FeatureTransformationModel = Field(
        alias="featureTransformation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFilterResponseModel(BaseModel):
    filter: FilterModel = Field(alias="filter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRecipeResponseModel(BaseModel):
    recipe: RecipeModel = Field(alias="recipe")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventTrackersResponseModel(BaseModel):
    event_trackers: List[EventTrackerSummaryModel] = Field(alias="eventTrackers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFiltersResponseModel(BaseModel):
    filters: List[FilterSummaryModel] = Field(alias="Filters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HyperParameterRangesModel(BaseModel):
    integer_hyper_parameter_ranges: Optional[
        Sequence[IntegerHyperParameterRangeModel]
    ] = Field(default=None, alias="integerHyperParameterRanges")
    continuous_hyper_parameter_ranges: Optional[
        Sequence[ContinuousHyperParameterRangeModel]
    ] = Field(default=None, alias="continuousHyperParameterRanges")
    categorical_hyper_parameter_ranges: Optional[
        Sequence[CategoricalHyperParameterRangeModel]
    ] = Field(default=None, alias="categoricalHyperParameterRanges")


class ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateModel(BaseModel):
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCampaignsRequestListCampaignsPaginateModel(BaseModel):
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetExportJobsRequestListDatasetExportJobsPaginateModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetGroupsRequestListDatasetGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetImportJobsRequestListDatasetImportJobsPaginateModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetsRequestListDatasetsPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventTrackersRequestListEventTrackersPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFiltersRequestListFiltersPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateModel(
    BaseModel
):
    metric_attribution_arn: Optional[str] = Field(
        default=None, alias="metricAttributionArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMetricAttributionsRequestListMetricAttributionsPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecipesRequestListRecipesPaginateModel(BaseModel):
    recipe_provider: Optional[Literal["SERVICE"]] = Field(
        default=None, alias="recipeProvider"
    )
    domain: Optional[Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]] = Field(
        default=None, alias="domain"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecommendersRequestListRecommendersPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemasRequestListSchemasPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolutionVersionsRequestListSolutionVersionsPaginateModel(BaseModel):
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolutionsRequestListSolutionsPaginateModel(BaseModel):
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMetricAttributionsResponseModel(BaseModel):
    metric_attributions: List[MetricAttributionSummaryModel] = Field(
        alias="metricAttributions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecipesResponseModel(BaseModel):
    recipes: List[RecipeSummaryModel] = Field(alias="recipes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolutionVersionsResponseModel(BaseModel):
    solution_versions: List[SolutionVersionSummaryModel] = Field(
        alias="solutionVersions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolutionsResponseModel(BaseModel):
    solutions: List[SolutionSummaryModel] = Field(alias="solutions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchInferenceJobModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="jobName")
    batch_inference_job_arn: Optional[str] = Field(
        default=None, alias="batchInferenceJobArn"
    )
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    num_results: Optional[int] = Field(default=None, alias="numResults")
    job_input: Optional[BatchInferenceJobInputModel] = Field(
        default=None, alias="jobInput"
    )
    job_output: Optional[BatchInferenceJobOutputModel] = Field(
        default=None, alias="jobOutput"
    )
    batch_inference_job_config: Optional[BatchInferenceJobConfigModel] = Field(
        default=None, alias="batchInferenceJobConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class CreateBatchInferenceJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    solution_version_arn: str = Field(alias="solutionVersionArn")
    job_input: BatchInferenceJobInputModel = Field(alias="jobInput")
    job_output: BatchInferenceJobOutputModel = Field(alias="jobOutput")
    role_arn: str = Field(alias="roleArn")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    num_results: Optional[int] = Field(default=None, alias="numResults")
    batch_inference_job_config: Optional[BatchInferenceJobConfigModel] = Field(
        default=None, alias="batchInferenceJobConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class BatchSegmentJobModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="jobName")
    batch_segment_job_arn: Optional[str] = Field(
        default=None, alias="batchSegmentJobArn"
    )
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    num_results: Optional[int] = Field(default=None, alias="numResults")
    job_input: Optional[BatchSegmentJobInputModel] = Field(
        default=None, alias="jobInput"
    )
    job_output: Optional[BatchSegmentJobOutputModel] = Field(
        default=None, alias="jobOutput"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class CreateBatchSegmentJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    solution_version_arn: str = Field(alias="solutionVersionArn")
    job_input: BatchSegmentJobInputModel = Field(alias="jobInput")
    job_output: BatchSegmentJobOutputModel = Field(alias="jobOutput")
    role_arn: str = Field(alias="roleArn")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    num_results: Optional[int] = Field(default=None, alias="numResults")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDatasetExportJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    dataset_arn: str = Field(alias="datasetArn")
    role_arn: str = Field(alias="roleArn")
    job_output: DatasetExportJobOutputModel = Field(alias="jobOutput")
    ingestion_mode: Optional[Literal["ALL", "BULK", "PUT"]] = Field(
        default=None, alias="ingestionMode"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DatasetExportJobModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="jobName")
    dataset_export_job_arn: Optional[str] = Field(
        default=None, alias="datasetExportJobArn"
    )
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    ingestion_mode: Optional[Literal["ALL", "BULK", "PUT"]] = Field(
        default=None, alias="ingestionMode"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    status: Optional[str] = Field(default=None, alias="status")
    job_output: Optional[DatasetExportJobOutputModel] = Field(
        default=None, alias="jobOutput"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class CreateMetricAttributionRequestModel(BaseModel):
    name: str = Field(alias="name")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    metrics: Sequence[MetricAttributeModel] = Field(alias="metrics")
    metrics_output_config: MetricAttributionOutputModel = Field(
        alias="metricsOutputConfig"
    )


class MetricAttributionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    metric_attribution_arn: Optional[str] = Field(
        default=None, alias="metricAttributionArn"
    )
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    metrics_output_config: Optional[MetricAttributionOutputModel] = Field(
        default=None, alias="metricsOutputConfig"
    )
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class UpdateMetricAttributionRequestModel(BaseModel):
    add_metrics: Optional[Sequence[MetricAttributeModel]] = Field(
        default=None, alias="addMetrics"
    )
    remove_metrics: Optional[Sequence[str]] = Field(default=None, alias="removeMetrics")
    metrics_output_config: Optional[MetricAttributionOutputModel] = Field(
        default=None, alias="metricsOutputConfig"
    )
    metric_attribution_arn: Optional[str] = Field(
        default=None, alias="metricAttributionArn"
    )


class CampaignModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    campaign_arn: Optional[str] = Field(default=None, alias="campaignArn")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    min_provisioned_tp_s: Optional[int] = Field(default=None, alias="minProvisionedTPS")
    campaign_config: Optional[CampaignConfigModel] = Field(
        default=None, alias="campaignConfig"
    )
    status: Optional[str] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    latest_campaign_update: Optional[CampaignUpdateSummaryModel] = Field(
        default=None, alias="latestCampaignUpdate"
    )


class DescribeDatasetImportJobResponseModel(BaseModel):
    dataset_import_job: DatasetImportJobModel = Field(alias="datasetImportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecommendersResponseModel(BaseModel):
    recommenders: List[RecommenderSummaryModel] = Field(alias="recommenders")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommenderModel(BaseModel):
    recommender_arn: Optional[str] = Field(default=None, alias="recommenderArn")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    name: Optional[str] = Field(default=None, alias="name")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    recommender_config: Optional[RecommenderConfigModel] = Field(
        default=None, alias="recommenderConfig"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    status: Optional[str] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    latest_recommender_update: Optional[RecommenderUpdateSummaryModel] = Field(
        default=None, alias="latestRecommenderUpdate"
    )
    model_metrics: Optional[Dict[str, float]] = Field(
        default=None, alias="modelMetrics"
    )


class AlgorithmModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    algorithm_arn: Optional[str] = Field(default=None, alias="algorithmArn")
    algorithm_image: Optional[AlgorithmImageModel] = Field(
        default=None, alias="algorithmImage"
    )
    default_hyper_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="defaultHyperParameters"
    )
    default_hyper_parameter_ranges: Optional[DefaultHyperParameterRangesModel] = Field(
        default=None, alias="defaultHyperParameterRanges"
    )
    default_resource_config: Optional[Dict[str, str]] = Field(
        default=None, alias="defaultResourceConfig"
    )
    training_input_mode: Optional[str] = Field(default=None, alias="trainingInputMode")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class HPOConfigModel(BaseModel):
    hpo_objective: Optional[HPOObjectiveModel] = Field(
        default=None, alias="hpoObjective"
    )
    hpo_resource_config: Optional[HPOResourceConfigModel] = Field(
        default=None, alias="hpoResourceConfig"
    )
    algorithm_hyper_parameter_ranges: Optional[HyperParameterRangesModel] = Field(
        default=None, alias="algorithmHyperParameterRanges"
    )


class DescribeBatchInferenceJobResponseModel(BaseModel):
    batch_inference_job: BatchInferenceJobModel = Field(alias="batchInferenceJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBatchSegmentJobResponseModel(BaseModel):
    batch_segment_job: BatchSegmentJobModel = Field(alias="batchSegmentJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetExportJobResponseModel(BaseModel):
    dataset_export_job: DatasetExportJobModel = Field(alias="datasetExportJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMetricAttributionResponseModel(BaseModel):
    metric_attribution: MetricAttributionModel = Field(alias="metricAttribution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCampaignResponseModel(BaseModel):
    campaign: CampaignModel = Field(alias="campaign")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRecommenderResponseModel(BaseModel):
    recommender: RecommenderModel = Field(alias="recommender")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAlgorithmResponseModel(BaseModel):
    algorithm: AlgorithmModel = Field(alias="algorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SolutionConfigModel(BaseModel):
    event_value_threshold: Optional[str] = Field(
        default=None, alias="eventValueThreshold"
    )
    hpo_config: Optional[HPOConfigModel] = Field(default=None, alias="hpoConfig")
    algorithm_hyper_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="algorithmHyperParameters"
    )
    feature_transformation_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="featureTransformationParameters"
    )
    auto_ml_config: Optional[AutoMLConfigModel] = Field(
        default=None, alias="autoMLConfig"
    )
    optimization_objective: Optional[OptimizationObjectiveModel] = Field(
        default=None, alias="optimizationObjective"
    )


class CreateSolutionRequestModel(BaseModel):
    name: str = Field(alias="name")
    dataset_group_arn: str = Field(alias="datasetGroupArn")
    perform_hp_o: Optional[bool] = Field(default=None, alias="performHPO")
    perform_auto_ml: Optional[bool] = Field(default=None, alias="performAutoML")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    event_type: Optional[str] = Field(default=None, alias="eventType")
    solution_config: Optional[SolutionConfigModel] = Field(
        default=None, alias="solutionConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class SolutionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    perform_hp_o: Optional[bool] = Field(default=None, alias="performHPO")
    perform_auto_ml: Optional[bool] = Field(default=None, alias="performAutoML")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    event_type: Optional[str] = Field(default=None, alias="eventType")
    solution_config: Optional[SolutionConfigModel] = Field(
        default=None, alias="solutionConfig"
    )
    auto_ml_result: Optional[AutoMLResultModel] = Field(
        default=None, alias="autoMLResult"
    )
    status: Optional[str] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    latest_solution_version: Optional[SolutionVersionSummaryModel] = Field(
        default=None, alias="latestSolutionVersion"
    )


class SolutionVersionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    solution_version_arn: Optional[str] = Field(
        default=None, alias="solutionVersionArn"
    )
    solution_arn: Optional[str] = Field(default=None, alias="solutionArn")
    perform_hp_o: Optional[bool] = Field(default=None, alias="performHPO")
    perform_auto_ml: Optional[bool] = Field(default=None, alias="performAutoML")
    recipe_arn: Optional[str] = Field(default=None, alias="recipeArn")
    event_type: Optional[str] = Field(default=None, alias="eventType")
    dataset_group_arn: Optional[str] = Field(default=None, alias="datasetGroupArn")
    solution_config: Optional[SolutionConfigModel] = Field(
        default=None, alias="solutionConfig"
    )
    training_hours: Optional[float] = Field(default=None, alias="trainingHours")
    training_mode: Optional[Literal["FULL", "UPDATE"]] = Field(
        default=None, alias="trainingMode"
    )
    tuned_hp_oparams: Optional[TunedHPOParamsModel] = Field(
        default=None, alias="tunedHPOParams"
    )
    status: Optional[str] = Field(default=None, alias="status")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class DescribeSolutionResponseModel(BaseModel):
    solution: SolutionModel = Field(alias="solution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSolutionVersionResponseModel(BaseModel):
    solution_version: SolutionVersionModel = Field(alias="solutionVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
