# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class EvaluationRequestModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    feature: str = Field(alias="feature")
    evaluation_context: Optional[str] = Field(default=None, alias="evaluationContext")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CloudWatchLogsDestinationConfigModel(BaseModel):
    log_group: Optional[str] = Field(default=None, alias="logGroup")


class CloudWatchLogsDestinationModel(BaseModel):
    log_group: Optional[str] = Field(default=None, alias="logGroup")


class OnlineAbConfigModel(BaseModel):
    control_treatment_name: Optional[str] = Field(
        default=None, alias="controlTreatmentName"
    )
    treatment_weights: Optional[Mapping[str, int]] = Field(
        default=None, alias="treatmentWeights"
    )


class TreatmentConfigModel(BaseModel):
    feature: str = Field(alias="feature")
    name: str = Field(alias="name")
    variation: str = Field(alias="variation")
    description: Optional[str] = Field(default=None, alias="description")


class LaunchGroupConfigModel(BaseModel):
    feature: str = Field(alias="feature")
    name: str = Field(alias="name")
    variation: str = Field(alias="variation")
    description: Optional[str] = Field(default=None, alias="description")


class ProjectAppConfigResourceConfigModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="applicationId")
    environment_id: Optional[str] = Field(default=None, alias="environmentId")


class CreateSegmentRequestModel(BaseModel):
    name: str = Field(alias="name")
    pattern: str = Field(alias="pattern")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class SegmentModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    pattern: str = Field(alias="pattern")
    description: Optional[str] = Field(default=None, alias="description")
    experiment_count: Optional[int] = Field(default=None, alias="experimentCount")
    launch_count: Optional[int] = Field(default=None, alias="launchCount")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DeleteExperimentRequestModel(BaseModel):
    experiment: str = Field(alias="experiment")
    project: str = Field(alias="project")


class DeleteFeatureRequestModel(BaseModel):
    feature: str = Field(alias="feature")
    project: str = Field(alias="project")


class DeleteLaunchRequestModel(BaseModel):
    launch: str = Field(alias="launch")
    project: str = Field(alias="project")


class DeleteProjectRequestModel(BaseModel):
    project: str = Field(alias="project")


class DeleteSegmentRequestModel(BaseModel):
    segment: str = Field(alias="segment")


class EvaluateFeatureRequestModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    feature: str = Field(alias="feature")
    project: str = Field(alias="project")
    evaluation_context: Optional[str] = Field(default=None, alias="evaluationContext")


class VariableValueModel(BaseModel):
    bool_value: Optional[bool] = Field(default=None, alias="boolValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    long_value: Optional[int] = Field(default=None, alias="longValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")


class EvaluationRuleModel(BaseModel):
    type: str = Field(alias="type")
    name: Optional[str] = Field(default=None, alias="name")


class EventModel(BaseModel):
    data: str = Field(alias="data")
    timestamp: Union[datetime, str] = Field(alias="timestamp")
    type: Literal["aws.evidently.custom", "aws.evidently.evaluation"] = Field(
        alias="type"
    )


class ExperimentExecutionModel(BaseModel):
    ended_time: Optional[datetime] = Field(default=None, alias="endedTime")
    started_time: Optional[datetime] = Field(default=None, alias="startedTime")


class ExperimentReportModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    report_name: Optional[Literal["BayesianInference"]] = Field(
        default=None, alias="reportName"
    )
    treatment_name: Optional[str] = Field(default=None, alias="treatmentName")


class ExperimentResultsDataModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    result_stat: Optional[
        Literal[
            "ConfidenceIntervalLowerBound",
            "ConfidenceIntervalUpperBound",
            "Mean",
            "PValue",
            "TreatmentEffect",
        ]
    ] = Field(default=None, alias="resultStat")
    treatment_name: Optional[str] = Field(default=None, alias="treatmentName")
    values: Optional[List[float]] = Field(default=None, alias="values")


class ExperimentScheduleModel(BaseModel):
    analysis_complete_time: Optional[datetime] = Field(
        default=None, alias="analysisCompleteTime"
    )


class OnlineAbDefinitionModel(BaseModel):
    control_treatment_name: Optional[str] = Field(
        default=None, alias="controlTreatmentName"
    )
    treatment_weights: Optional[Dict[str, int]] = Field(
        default=None, alias="treatmentWeights"
    )


class TreatmentModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    feature_variations: Optional[Dict[str, str]] = Field(
        default=None, alias="featureVariations"
    )


class GetExperimentRequestModel(BaseModel):
    experiment: str = Field(alias="experiment")
    project: str = Field(alias="project")


class GetExperimentResultsRequestModel(BaseModel):
    experiment: str = Field(alias="experiment")
    metric_names: Sequence[str] = Field(alias="metricNames")
    project: str = Field(alias="project")
    treatment_names: Sequence[str] = Field(alias="treatmentNames")
    base_stat: Optional[Literal["Mean"]] = Field(default=None, alias="baseStat")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    period: Optional[int] = Field(default=None, alias="period")
    report_names: Optional[Sequence[Literal["BayesianInference"]]] = Field(
        default=None, alias="reportNames"
    )
    result_stats: Optional[
        Sequence[Literal["BaseStat", "ConfidenceInterval", "PValue", "TreatmentEffect"]]
    ] = Field(default=None, alias="resultStats")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")


class GetFeatureRequestModel(BaseModel):
    feature: str = Field(alias="feature")
    project: str = Field(alias="project")


class GetLaunchRequestModel(BaseModel):
    launch: str = Field(alias="launch")
    project: str = Field(alias="project")


class GetProjectRequestModel(BaseModel):
    project: str = Field(alias="project")


class GetSegmentRequestModel(BaseModel):
    segment: str = Field(alias="segment")


class LaunchExecutionModel(BaseModel):
    ended_time: Optional[datetime] = Field(default=None, alias="endedTime")
    started_time: Optional[datetime] = Field(default=None, alias="startedTime")


class LaunchGroupModel(BaseModel):
    feature_variations: Dict[str, str] = Field(alias="featureVariations")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListExperimentsRequestModel(BaseModel):
    project: str = Field(alias="project")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    status: Optional[
        Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
    ] = Field(default=None, alias="status")


class ListFeaturesRequestModel(BaseModel):
    project: str = Field(alias="project")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListLaunchesRequestModel(BaseModel):
    project: str = Field(alias="project")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    status: Optional[
        Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
    ] = Field(default=None, alias="status")


class ListProjectsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ProjectSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["AVAILABLE", "UPDATING"] = Field(alias="status")
    active_experiment_count: Optional[int] = Field(
        default=None, alias="activeExperimentCount"
    )
    active_launch_count: Optional[int] = Field(default=None, alias="activeLaunchCount")
    description: Optional[str] = Field(default=None, alias="description")
    experiment_count: Optional[int] = Field(default=None, alias="experimentCount")
    feature_count: Optional[int] = Field(default=None, alias="featureCount")
    launch_count: Optional[int] = Field(default=None, alias="launchCount")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListSegmentReferencesRequestModel(BaseModel):
    segment: str = Field(alias="segment")
    type: Literal["EXPERIMENT", "LAUNCH"] = Field(alias="type")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RefResourceModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    arn: Optional[str] = Field(default=None, alias="arn")
    end_time: Optional[str] = Field(default=None, alias="endTime")
    last_updated_on: Optional[str] = Field(default=None, alias="lastUpdatedOn")
    start_time: Optional[str] = Field(default=None, alias="startTime")
    status: Optional[str] = Field(default=None, alias="status")


class ListSegmentsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MetricDefinitionConfigModel(BaseModel):
    entity_id_key: str = Field(alias="entityIdKey")
    name: str = Field(alias="name")
    value_key: str = Field(alias="valueKey")
    event_pattern: Optional[str] = Field(default=None, alias="eventPattern")
    unit_label: Optional[str] = Field(default=None, alias="unitLabel")


class MetricDefinitionModel(BaseModel):
    entity_id_key: Optional[str] = Field(default=None, alias="entityIdKey")
    event_pattern: Optional[str] = Field(default=None, alias="eventPattern")
    name: Optional[str] = Field(default=None, alias="name")
    unit_label: Optional[str] = Field(default=None, alias="unitLabel")
    value_key: Optional[str] = Field(default=None, alias="valueKey")


class ProjectAppConfigResourceModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    configuration_profile_id: str = Field(alias="configurationProfileId")
    environment_id: str = Field(alias="environmentId")


class S3DestinationConfigModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class S3DestinationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class PutProjectEventsResultEntryModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    event_id: Optional[str] = Field(default=None, alias="eventId")


class SegmentOverrideModel(BaseModel):
    evaluation_order: int = Field(alias="evaluationOrder")
    segment: str = Field(alias="segment")
    weights: Mapping[str, int] = Field(alias="weights")


class StartExperimentRequestModel(BaseModel):
    analysis_complete_time: Union[datetime, str] = Field(alias="analysisCompleteTime")
    experiment: str = Field(alias="experiment")
    project: str = Field(alias="project")


class StartLaunchRequestModel(BaseModel):
    launch: str = Field(alias="launch")
    project: str = Field(alias="project")


class StopExperimentRequestModel(BaseModel):
    experiment: str = Field(alias="experiment")
    project: str = Field(alias="project")
    desired_state: Optional[Literal["CANCELLED", "COMPLETED"]] = Field(
        default=None, alias="desiredState"
    )
    reason: Optional[str] = Field(default=None, alias="reason")


class StopLaunchRequestModel(BaseModel):
    launch: str = Field(alias="launch")
    project: str = Field(alias="project")
    desired_state: Optional[Literal["CANCELLED", "COMPLETED"]] = Field(
        default=None, alias="desiredState"
    )
    reason: Optional[str] = Field(default=None, alias="reason")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TestSegmentPatternRequestModel(BaseModel):
    pattern: str = Field(alias="pattern")
    payload: str = Field(alias="payload")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchEvaluateFeatureRequestModel(BaseModel):
    project: str = Field(alias="project")
    requests: Sequence[EvaluationRequestModel] = Field(alias="requests")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExperimentResponseModel(BaseModel):
    started_time: datetime = Field(alias="startedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopExperimentResponseModel(BaseModel):
    ended_time: datetime = Field(alias="endedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopLaunchResponseModel(BaseModel):
    ended_time: datetime = Field(alias="endedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestSegmentPatternResponseModel(BaseModel):
    match: bool = Field(alias="match")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectRequestModel(BaseModel):
    project: str = Field(alias="project")
    app_config_resource: Optional[ProjectAppConfigResourceConfigModel] = Field(
        default=None, alias="appConfigResource"
    )
    description: Optional[str] = Field(default=None, alias="description")


class CreateSegmentResponseModel(BaseModel):
    segment: SegmentModel = Field(alias="segment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentResponseModel(BaseModel):
    segment: SegmentModel = Field(alias="segment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSegmentsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    segments: List[SegmentModel] = Field(alias="segments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluateFeatureResponseModel(BaseModel):
    details: str = Field(alias="details")
    reason: str = Field(alias="reason")
    value: VariableValueModel = Field(alias="value")
    variation: str = Field(alias="variation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluationResultModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    feature: str = Field(alias="feature")
    details: Optional[str] = Field(default=None, alias="details")
    project: Optional[str] = Field(default=None, alias="project")
    reason: Optional[str] = Field(default=None, alias="reason")
    value: Optional[VariableValueModel] = Field(default=None, alias="value")
    variation: Optional[str] = Field(default=None, alias="variation")


class VariationConfigModel(BaseModel):
    name: str = Field(alias="name")
    value: VariableValueModel = Field(alias="value")


class VariationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[VariableValueModel] = Field(default=None, alias="value")


class FeatureSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    evaluation_strategy: Literal["ALL_RULES", "DEFAULT_VARIATION"] = Field(
        alias="evaluationStrategy"
    )
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["AVAILABLE", "UPDATING"] = Field(alias="status")
    default_variation: Optional[str] = Field(default=None, alias="defaultVariation")
    evaluation_rules: Optional[List[EvaluationRuleModel]] = Field(
        default=None, alias="evaluationRules"
    )
    project: Optional[str] = Field(default=None, alias="project")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class PutProjectEventsRequestModel(BaseModel):
    events: Sequence[EventModel] = Field(alias="events")
    project: str = Field(alias="project")


class GetExperimentResultsResponseModel(BaseModel):
    details: str = Field(alias="details")
    reports: List[ExperimentReportModel] = Field(alias="reports")
    results_data: List[ExperimentResultsDataModel] = Field(alias="resultsData")
    timestamps: List[datetime] = Field(alias="timestamps")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExperimentsRequestListExperimentsPaginateModel(BaseModel):
    project: str = Field(alias="project")
    status: Optional[
        Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFeaturesRequestListFeaturesPaginateModel(BaseModel):
    project: str = Field(alias="project")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLaunchesRequestListLaunchesPaginateModel(BaseModel):
    project: str = Field(alias="project")
    status: Optional[
        Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSegmentReferencesRequestListSegmentReferencesPaginateModel(BaseModel):
    segment: str = Field(alias="segment")
    type: Literal["EXPERIMENT", "LAUNCH"] = Field(alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSegmentsRequestListSegmentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    projects: List[ProjectSummaryModel] = Field(alias="projects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSegmentReferencesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    referenced_by: List[RefResourceModel] = Field(alias="referencedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricGoalConfigModel(BaseModel):
    metric_definition: MetricDefinitionConfigModel = Field(alias="metricDefinition")
    desired_change: Optional[Literal["DECREASE", "INCREASE"]] = Field(
        default=None, alias="desiredChange"
    )


class MetricMonitorConfigModel(BaseModel):
    metric_definition: MetricDefinitionConfigModel = Field(alias="metricDefinition")


class MetricGoalModel(BaseModel):
    metric_definition: MetricDefinitionModel = Field(alias="metricDefinition")
    desired_change: Optional[Literal["DECREASE", "INCREASE"]] = Field(
        default=None, alias="desiredChange"
    )


class MetricMonitorModel(BaseModel):
    metric_definition: MetricDefinitionModel = Field(alias="metricDefinition")


class ProjectDataDeliveryConfigModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsDestinationConfigModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    s3_destination: Optional[S3DestinationConfigModel] = Field(
        default=None, alias="s3Destination"
    )


class UpdateProjectDataDeliveryRequestModel(BaseModel):
    project: str = Field(alias="project")
    cloud_watch_logs: Optional[CloudWatchLogsDestinationConfigModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    s3_destination: Optional[S3DestinationConfigModel] = Field(
        default=None, alias="s3Destination"
    )


class ProjectDataDeliveryModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    s3_destination: Optional[S3DestinationModel] = Field(
        default=None, alias="s3Destination"
    )


class PutProjectEventsResponseModel(BaseModel):
    event_results: List[PutProjectEventsResultEntryModel] = Field(alias="eventResults")
    failed_event_count: int = Field(alias="failedEventCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduledSplitConfigModel(BaseModel):
    group_weights: Mapping[str, int] = Field(alias="groupWeights")
    start_time: Union[datetime, str] = Field(alias="startTime")
    segment_overrides: Optional[Sequence[SegmentOverrideModel]] = Field(
        default=None, alias="segmentOverrides"
    )


class ScheduledSplitModel(BaseModel):
    start_time: datetime = Field(alias="startTime")
    group_weights: Optional[Dict[str, int]] = Field(default=None, alias="groupWeights")
    segment_overrides: Optional[List[SegmentOverrideModel]] = Field(
        default=None, alias="segmentOverrides"
    )


class BatchEvaluateFeatureResponseModel(BaseModel):
    results: List[EvaluationResultModel] = Field(alias="results")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFeatureRequestModel(BaseModel):
    name: str = Field(alias="name")
    project: str = Field(alias="project")
    variations: Sequence[VariationConfigModel] = Field(alias="variations")
    default_variation: Optional[str] = Field(default=None, alias="defaultVariation")
    description: Optional[str] = Field(default=None, alias="description")
    entity_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="entityOverrides"
    )
    evaluation_strategy: Optional[Literal["ALL_RULES", "DEFAULT_VARIATION"]] = Field(
        default=None, alias="evaluationStrategy"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateFeatureRequestModel(BaseModel):
    feature: str = Field(alias="feature")
    project: str = Field(alias="project")
    add_or_update_variations: Optional[Sequence[VariationConfigModel]] = Field(
        default=None, alias="addOrUpdateVariations"
    )
    default_variation: Optional[str] = Field(default=None, alias="defaultVariation")
    description: Optional[str] = Field(default=None, alias="description")
    entity_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="entityOverrides"
    )
    evaluation_strategy: Optional[Literal["ALL_RULES", "DEFAULT_VARIATION"]] = Field(
        default=None, alias="evaluationStrategy"
    )
    remove_variations: Optional[Sequence[str]] = Field(
        default=None, alias="removeVariations"
    )


class FeatureModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    evaluation_strategy: Literal["ALL_RULES", "DEFAULT_VARIATION"] = Field(
        alias="evaluationStrategy"
    )
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["AVAILABLE", "UPDATING"] = Field(alias="status")
    value_type: Literal["BOOLEAN", "DOUBLE", "LONG", "STRING"] = Field(
        alias="valueType"
    )
    variations: List[VariationModel] = Field(alias="variations")
    default_variation: Optional[str] = Field(default=None, alias="defaultVariation")
    description: Optional[str] = Field(default=None, alias="description")
    entity_overrides: Optional[Dict[str, str]] = Field(
        default=None, alias="entityOverrides"
    )
    evaluation_rules: Optional[List[EvaluationRuleModel]] = Field(
        default=None, alias="evaluationRules"
    )
    project: Optional[str] = Field(default=None, alias="project")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListFeaturesResponseModel(BaseModel):
    features: List[FeatureSummaryModel] = Field(alias="features")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentRequestModel(BaseModel):
    metric_goals: Sequence[MetricGoalConfigModel] = Field(alias="metricGoals")
    name: str = Field(alias="name")
    project: str = Field(alias="project")
    treatments: Sequence[TreatmentConfigModel] = Field(alias="treatments")
    description: Optional[str] = Field(default=None, alias="description")
    online_ab_config: Optional[OnlineAbConfigModel] = Field(
        default=None, alias="onlineAbConfig"
    )
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    sampling_rate: Optional[int] = Field(default=None, alias="samplingRate")
    segment: Optional[str] = Field(default=None, alias="segment")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateExperimentRequestModel(BaseModel):
    experiment: str = Field(alias="experiment")
    project: str = Field(alias="project")
    description: Optional[str] = Field(default=None, alias="description")
    metric_goals: Optional[Sequence[MetricGoalConfigModel]] = Field(
        default=None, alias="metricGoals"
    )
    online_ab_config: Optional[OnlineAbConfigModel] = Field(
        default=None, alias="onlineAbConfig"
    )
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    remove_segment: Optional[bool] = Field(default=None, alias="removeSegment")
    sampling_rate: Optional[int] = Field(default=None, alias="samplingRate")
    segment: Optional[str] = Field(default=None, alias="segment")
    treatments: Optional[Sequence[TreatmentConfigModel]] = Field(
        default=None, alias="treatments"
    )


class ExperimentModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"] = Field(
        alias="status"
    )
    type: Literal["aws.evidently.onlineab"] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    execution: Optional[ExperimentExecutionModel] = Field(
        default=None, alias="execution"
    )
    metric_goals: Optional[List[MetricGoalModel]] = Field(
        default=None, alias="metricGoals"
    )
    online_ab_definition: Optional[OnlineAbDefinitionModel] = Field(
        default=None, alias="onlineAbDefinition"
    )
    project: Optional[str] = Field(default=None, alias="project")
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    sampling_rate: Optional[int] = Field(default=None, alias="samplingRate")
    schedule: Optional[ExperimentScheduleModel] = Field(default=None, alias="schedule")
    segment: Optional[str] = Field(default=None, alias="segment")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    treatments: Optional[List[TreatmentModel]] = Field(default=None, alias="treatments")


class CreateProjectRequestModel(BaseModel):
    name: str = Field(alias="name")
    app_config_resource: Optional[ProjectAppConfigResourceConfigModel] = Field(
        default=None, alias="appConfigResource"
    )
    data_delivery: Optional[ProjectDataDeliveryConfigModel] = Field(
        default=None, alias="dataDelivery"
    )
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ProjectModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["AVAILABLE", "UPDATING"] = Field(alias="status")
    active_experiment_count: Optional[int] = Field(
        default=None, alias="activeExperimentCount"
    )
    active_launch_count: Optional[int] = Field(default=None, alias="activeLaunchCount")
    app_config_resource: Optional[ProjectAppConfigResourceModel] = Field(
        default=None, alias="appConfigResource"
    )
    data_delivery: Optional[ProjectDataDeliveryModel] = Field(
        default=None, alias="dataDelivery"
    )
    description: Optional[str] = Field(default=None, alias="description")
    experiment_count: Optional[int] = Field(default=None, alias="experimentCount")
    feature_count: Optional[int] = Field(default=None, alias="featureCount")
    launch_count: Optional[int] = Field(default=None, alias="launchCount")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ScheduledSplitsLaunchConfigModel(BaseModel):
    steps: Sequence[ScheduledSplitConfigModel] = Field(alias="steps")


class ScheduledSplitsLaunchDefinitionModel(BaseModel):
    steps: Optional[List[ScheduledSplitModel]] = Field(default=None, alias="steps")


class CreateFeatureResponseModel(BaseModel):
    feature: FeatureModel = Field(alias="feature")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFeatureResponseModel(BaseModel):
    feature: FeatureModel = Field(alias="feature")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFeatureResponseModel(BaseModel):
    feature: FeatureModel = Field(alias="feature")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExperimentsResponseModel(BaseModel):
    experiments: List[ExperimentModel] = Field(alias="experiments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateExperimentResponseModel(BaseModel):
    experiment: ExperimentModel = Field(alias="experiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResponseModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProjectResponseModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectDataDeliveryResponseModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectResponseModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLaunchRequestModel(BaseModel):
    groups: Sequence[LaunchGroupConfigModel] = Field(alias="groups")
    name: str = Field(alias="name")
    project: str = Field(alias="project")
    description: Optional[str] = Field(default=None, alias="description")
    metric_monitors: Optional[Sequence[MetricMonitorConfigModel]] = Field(
        default=None, alias="metricMonitors"
    )
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    scheduled_splits_config: Optional[ScheduledSplitsLaunchConfigModel] = Field(
        default=None, alias="scheduledSplitsConfig"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateLaunchRequestModel(BaseModel):
    launch: str = Field(alias="launch")
    project: str = Field(alias="project")
    description: Optional[str] = Field(default=None, alias="description")
    groups: Optional[Sequence[LaunchGroupConfigModel]] = Field(
        default=None, alias="groups"
    )
    metric_monitors: Optional[Sequence[MetricMonitorConfigModel]] = Field(
        default=None, alias="metricMonitors"
    )
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    scheduled_splits_config: Optional[ScheduledSplitsLaunchConfigModel] = Field(
        default=None, alias="scheduledSplitsConfig"
    )


class LaunchModel(BaseModel):
    arn: str = Field(alias="arn")
    created_time: datetime = Field(alias="createdTime")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    name: str = Field(alias="name")
    status: Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"] = Field(
        alias="status"
    )
    type: Literal["aws.evidently.splits"] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    execution: Optional[LaunchExecutionModel] = Field(default=None, alias="execution")
    groups: Optional[List[LaunchGroupModel]] = Field(default=None, alias="groups")
    metric_monitors: Optional[List[MetricMonitorModel]] = Field(
        default=None, alias="metricMonitors"
    )
    project: Optional[str] = Field(default=None, alias="project")
    randomization_salt: Optional[str] = Field(default=None, alias="randomizationSalt")
    scheduled_splits_definition: Optional[ScheduledSplitsLaunchDefinitionModel] = Field(
        default=None, alias="scheduledSplitsDefinition"
    )
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateLaunchResponseModel(BaseModel):
    launch: LaunchModel = Field(alias="launch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLaunchResponseModel(BaseModel):
    launch: LaunchModel = Field(alias="launch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLaunchesResponseModel(BaseModel):
    launches: List[LaunchModel] = Field(alias="launches")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartLaunchResponseModel(BaseModel):
    launch: LaunchModel = Field(alias="launch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLaunchResponseModel(BaseModel):
    launch: LaunchModel = Field(alias="launch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
