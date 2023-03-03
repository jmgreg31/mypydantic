# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionSourceModel(BaseModel):
    source_uri: str = Field(alias="SourceUri")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_id: Optional[str] = Field(default=None, alias="SourceId")


class AddAssociationRequestModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    destination_arn: str = Field(alias="DestinationArn")
    association_type: Optional[
        Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
    ] = Field(default=None, alias="AssociationType")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AgentVersionModel(BaseModel):
    version: str = Field(alias="Version")
    agent_count: int = Field(alias="AgentCount")


class AlarmModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")


class MetricDefinitionModel(BaseModel):
    name: str = Field(alias="Name")
    regex: str = Field(alias="Regex")


class AlgorithmStatusItemModel(BaseModel):
    name: str = Field(alias="Name")
    status: Literal["Completed", "Failed", "InProgress", "NotStarted"] = Field(
        alias="Status"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class AlgorithmSummaryModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")
    algorithm_arn: str = Field(alias="AlgorithmArn")
    creation_time: datetime = Field(alias="CreationTime")
    algorithm_status: Literal[
        "Completed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="AlgorithmStatus")
    algorithm_description: Optional[str] = Field(
        default=None, alias="AlgorithmDescription"
    )


class AnnotationConsolidationConfigModel(BaseModel):
    annotation_consolidation_lambda_arn: str = Field(
        alias="AnnotationConsolidationLambdaArn"
    )


class AppDetailsModel(BaseModel):
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    app_type: Optional[
        Literal[
            "JupyterServer",
            "KernelGateway",
            "RSessionGateway",
            "RStudioServerPro",
            "TensorBoard",
        ]
    ] = Field(default=None, alias="AppType")
    app_name: Optional[str] = Field(default=None, alias="AppName")
    status: Optional[
        Literal["Deleted", "Deleting", "Failed", "InService", "Pending"]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    space_name: Optional[str] = Field(default=None, alias="SpaceName")


class AppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    container_entrypoint: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerEntrypoint"
    )
    container_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerArguments"
    )


class ArtifactSourceTypeModel(BaseModel):
    source_id_type: Literal["Custom", "MD5Hash", "S3ETag", "S3Version"] = Field(
        alias="SourceIdType"
    )
    value: str = Field(alias="Value")


class AssociateTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    trial_name: str = Field(alias="TrialName")


class UserContextModel(BaseModel):
    user_profile_arn: Optional[str] = Field(default=None, alias="UserProfileArn")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")


class AsyncInferenceClientConfigModel(BaseModel):
    max_concurrent_invocations_per_instance: Optional[int] = Field(
        default=None, alias="MaxConcurrentInvocationsPerInstance"
    )


class AsyncInferenceNotificationConfigModel(BaseModel):
    success_topic: Optional[str] = Field(default=None, alias="SuccessTopic")
    error_topic: Optional[str] = Field(default=None, alias="ErrorTopic")


class AthenaDatasetDefinitionModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    database: str = Field(alias="Database")
    query_string: str = Field(alias="QueryString")
    output_s3_uri: str = Field(alias="OutputS3Uri")
    output_format: Literal["AVRO", "JSON", "ORC", "PARQUET", "TEXTFILE"] = Field(
        alias="OutputFormat"
    )
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    output_compression: Optional[Literal["GZIP", "SNAPPY", "ZLIB"]] = Field(
        default=None, alias="OutputCompression"
    )


class AutoMLAlgorithmConfigModel(BaseModel):
    auto_ml_algorithms: Sequence[
        Literal[
            "catboost",
            "extra-trees",
            "fastai",
            "lightgbm",
            "linear-learner",
            "mlp",
            "nn-torch",
            "randomforest",
            "xgboost",
        ]
    ] = Field(alias="AutoMLAlgorithms")


class AutoMLCandidateStepModel(BaseModel):
    candidate_step_type: Literal[
        "AWS::SageMaker::ProcessingJob",
        "AWS::SageMaker::TrainingJob",
        "AWS::SageMaker::TransformJob",
    ] = Field(alias="CandidateStepType")
    candidate_step_arn: str = Field(alias="CandidateStepArn")
    candidate_step_name: str = Field(alias="CandidateStepName")


class AutoMLContainerDefinitionModel(BaseModel):
    image: str = Field(alias="Image")
    model_data_url: str = Field(alias="ModelDataUrl")
    environment: Optional[Dict[str, str]] = Field(default=None, alias="Environment")


class FinalAutoMLJobObjectiveMetricModel(BaseModel):
    metric_name: Literal[
        "AUC",
        "Accuracy",
        "BalancedAccuracy",
        "F1",
        "F1macro",
        "MAE",
        "MSE",
        "Precision",
        "PrecisionMacro",
        "R2",
        "RMSE",
        "Recall",
        "RecallMacro",
    ] = Field(alias="MetricName")
    value: float = Field(alias="Value")
    type: Optional[Literal["Maximize", "Minimize"]] = Field(default=None, alias="Type")
    standard_metric_name: Optional[
        Literal[
            "AUC",
            "Accuracy",
            "BalancedAccuracy",
            "F1",
            "F1macro",
            "MAE",
            "MSE",
            "Precision",
            "PrecisionMacro",
            "R2",
            "RMSE",
            "Recall",
            "RecallMacro",
        ]
    ] = Field(default=None, alias="StandardMetricName")


class AutoMLS3DataSourceModel(BaseModel):
    s3_data_type: Literal["ManifestFile", "S3Prefix"] = Field(alias="S3DataType")
    s3_uri: str = Field(alias="S3Uri")


class AutoMLDataSplitConfigModel(BaseModel):
    validation_fraction: Optional[float] = Field(
        default=None, alias="ValidationFraction"
    )


class AutoMLJobArtifactsModel(BaseModel):
    candidate_definition_notebook_location: Optional[str] = Field(
        default=None, alias="CandidateDefinitionNotebookLocation"
    )
    data_exploration_notebook_location: Optional[str] = Field(
        default=None, alias="DataExplorationNotebookLocation"
    )


class AutoMLJobCompletionCriteriaModel(BaseModel):
    max_candidates: Optional[int] = Field(default=None, alias="MaxCandidates")
    max_runtime_per_training_job_in_seconds: Optional[int] = Field(
        default=None, alias="MaxRuntimePerTrainingJobInSeconds"
    )
    max_auto_ml_job_runtime_in_seconds: Optional[int] = Field(
        default=None, alias="MaxAutoMLJobRuntimeInSeconds"
    )


class AutoMLJobObjectiveModel(BaseModel):
    metric_name: Literal[
        "AUC",
        "Accuracy",
        "BalancedAccuracy",
        "F1",
        "F1macro",
        "MAE",
        "MSE",
        "Precision",
        "PrecisionMacro",
        "R2",
        "RMSE",
        "Recall",
        "RecallMacro",
    ] = Field(alias="MetricName")


class AutoMLJobStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class AutoMLPartialFailureReasonModel(BaseModel):
    partial_failure_message: Optional[str] = Field(
        default=None, alias="PartialFailureMessage"
    )


class AutoMLOutputDataConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class VpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    subnets: Sequence[str] = Field(alias="Subnets")


class BatchDataCaptureConfigModel(BaseModel):
    destination_s3_uri: str = Field(alias="DestinationS3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    generate_inference_id: Optional[bool] = Field(
        default=None, alias="GenerateInferenceId"
    )


class BatchDescribeModelPackageErrorModel(BaseModel):
    error_code: str = Field(alias="ErrorCode")
    error_response: str = Field(alias="ErrorResponse")


class BatchDescribeModelPackageInputRequestModel(BaseModel):
    model_package_arn_list: Sequence[str] = Field(alias="ModelPackageArnList")


class BestObjectiveNotImprovingModel(BaseModel):
    max_number_of_training_jobs_not_improving: Optional[int] = Field(
        default=None, alias="MaxNumberOfTrainingJobsNotImproving"
    )


class MetricsSourceModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    s3_uri: str = Field(alias="S3Uri")
    content_digest: Optional[str] = Field(default=None, alias="ContentDigest")


class CacheHitResultModel(BaseModel):
    source_pipeline_execution_arn: Optional[str] = Field(
        default=None, alias="SourcePipelineExecutionArn"
    )


class OutputParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class CandidateArtifactLocationsModel(BaseModel):
    explainability: str = Field(alias="Explainability")
    model_insights: Optional[str] = Field(default=None, alias="ModelInsights")


class MetricDatumModel(BaseModel):
    metric_name: Optional[
        Literal[
            "AUC",
            "Accuracy",
            "BalancedAccuracy",
            "F1",
            "F1macro",
            "MAE",
            "MSE",
            "Precision",
            "PrecisionMacro",
            "R2",
            "RMSE",
            "Recall",
            "RecallMacro",
        ]
    ] = Field(default=None, alias="MetricName")
    value: Optional[float] = Field(default=None, alias="Value")
    set: Optional[Literal["Test", "Train", "Validation"]] = Field(
        default=None, alias="Set"
    )
    standard_metric_name: Optional[
        Literal[
            "AUC",
            "Accuracy",
            "BalancedAccuracy",
            "F1",
            "F1macro",
            "InferenceLatency",
            "LogLoss",
            "MAE",
            "MSE",
            "Precision",
            "PrecisionMacro",
            "R2",
            "RMSE",
            "Recall",
            "RecallMacro",
        ]
    ] = Field(default=None, alias="StandardMetricName")


class TimeSeriesForecastingSettingsModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    amazon_forecast_role_arn: Optional[str] = Field(
        default=None, alias="AmazonForecastRoleArn"
    )


class CapacitySizeModel(BaseModel):
    type: Literal["CAPACITY_PERCENT", "INSTANCE_COUNT"] = Field(alias="Type")
    value: int = Field(alias="Value")


class CaptureContentTypeHeaderModel(BaseModel):
    csv_content_types: Optional[Sequence[str]] = Field(
        default=None, alias="CsvContentTypes"
    )
    json_content_types: Optional[Sequence[str]] = Field(
        default=None, alias="JsonContentTypes"
    )


class CaptureOptionModel(BaseModel):
    capture_mode: Literal["Input", "Output"] = Field(alias="CaptureMode")


class CategoricalParameterRangeSpecificationModel(BaseModel):
    values: Sequence[str] = Field(alias="Values")


class CategoricalParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class CategoricalParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: Sequence[str] = Field(alias="Value")


class ChannelSpecificationModel(BaseModel):
    name: str = Field(alias="Name")
    supported_content_types: Sequence[str] = Field(alias="SupportedContentTypes")
    supported_input_modes: Sequence[Literal["FastFile", "File", "Pipe"]] = Field(
        alias="SupportedInputModes"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    is_required: Optional[bool] = Field(default=None, alias="IsRequired")
    supported_compression_types: Optional[Sequence[Literal["Gzip", "None"]]] = Field(
        default=None, alias="SupportedCompressionTypes"
    )


class ShuffleConfigModel(BaseModel):
    seed: int = Field(alias="Seed")


class CheckpointConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")


class ClarifyCheckStepMetadataModel(BaseModel):
    check_type: Optional[str] = Field(default=None, alias="CheckType")
    baseline_used_for_drift_check_constraints: Optional[str] = Field(
        default=None, alias="BaselineUsedForDriftCheckConstraints"
    )
    calculated_baseline_constraints: Optional[str] = Field(
        default=None, alias="CalculatedBaselineConstraints"
    )
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    violation_report: Optional[str] = Field(default=None, alias="ViolationReport")
    check_job_arn: Optional[str] = Field(default=None, alias="CheckJobArn")
    skip_check: Optional[bool] = Field(default=None, alias="SkipCheck")
    register_new_baseline: Optional[bool] = Field(
        default=None, alias="RegisterNewBaseline"
    )


class ClarifyInferenceConfigModel(BaseModel):
    features_attribute: Optional[str] = Field(default=None, alias="FeaturesAttribute")
    content_template: Optional[str] = Field(default=None, alias="ContentTemplate")
    max_record_count: Optional[int] = Field(default=None, alias="MaxRecordCount")
    max_payload_in_mb: Optional[int] = Field(default=None, alias="MaxPayloadInMB")
    probability_index: Optional[int] = Field(default=None, alias="ProbabilityIndex")
    label_index: Optional[int] = Field(default=None, alias="LabelIndex")
    probability_attribute: Optional[str] = Field(
        default=None, alias="ProbabilityAttribute"
    )
    label_attribute: Optional[str] = Field(default=None, alias="LabelAttribute")
    label_headers: Optional[Sequence[str]] = Field(default=None, alias="LabelHeaders")
    feature_headers: Optional[Sequence[str]] = Field(
        default=None, alias="FeatureHeaders"
    )
    feature_types: Optional[
        Sequence[Literal["categorical", "numerical", "text"]]
    ] = Field(default=None, alias="FeatureTypes")


class ClarifyShapBaselineConfigModel(BaseModel):
    mime_type: Optional[str] = Field(default=None, alias="MimeType")
    shap_baseline: Optional[str] = Field(default=None, alias="ShapBaseline")
    shap_baseline_uri: Optional[str] = Field(default=None, alias="ShapBaselineUri")


class ClarifyTextConfigModel(BaseModel):
    language: Literal[
        "af",
        "ar",
        "bg",
        "bn",
        "ca",
        "cs",
        "da",
        "de",
        "el",
        "en",
        "es",
        "et",
        "eu",
        "fa",
        "fi",
        "fr",
        "ga",
        "gu",
        "he",
        "hi",
        "hr",
        "hu",
        "hy",
        "id",
        "is",
        "it",
        "kn",
        "ky",
        "lb",
        "lij",
        "lt",
        "lv",
        "mk",
        "ml",
        "mr",
        "nb",
        "ne",
        "nl",
        "pl",
        "pt",
        "ro",
        "ru",
        "sa",
        "si",
        "sk",
        "sl",
        "sq",
        "sr",
        "sv",
        "ta",
        "te",
        "tl",
        "tn",
        "tr",
        "tt",
        "uk",
        "ur",
        "xx",
        "yo",
        "zh",
    ] = Field(alias="Language")
    granularity: Literal["paragraph", "sentence", "token"] = Field(alias="Granularity")


class GitConfigModel(BaseModel):
    repository_url: str = Field(alias="RepositoryUrl")
    branch: Optional[str] = Field(default=None, alias="Branch")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")


class CodeRepositoryModel(BaseModel):
    repository_url: str = Field(alias="RepositoryUrl")


class CognitoConfigModel(BaseModel):
    user_pool: str = Field(alias="UserPool")
    client_id: str = Field(alias="ClientId")


class CognitoMemberDefinitionModel(BaseModel):
    user_pool: str = Field(alias="UserPool")
    user_group: str = Field(alias="UserGroup")
    client_id: str = Field(alias="ClientId")


class CollectionConfigurationModel(BaseModel):
    collection_name: Optional[str] = Field(default=None, alias="CollectionName")
    collection_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="CollectionParameters"
    )


class CompilationJobSummaryModel(BaseModel):
    compilation_job_name: str = Field(alias="CompilationJobName")
    compilation_job_arn: str = Field(alias="CompilationJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    compilation_job_status: Literal[
        "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
    ] = Field(alias="CompilationJobStatus")
    compilation_start_time: Optional[datetime] = Field(
        default=None, alias="CompilationStartTime"
    )
    compilation_end_time: Optional[datetime] = Field(
        default=None, alias="CompilationEndTime"
    )
    compilation_target_device: Optional[
        Literal[
            "aisage",
            "amba_cv2",
            "amba_cv22",
            "amba_cv25",
            "coreml",
            "deeplens",
            "imx8mplus",
            "imx8qm",
            "jacinto_tda4vm",
            "jetson_nano",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_xavier",
            "lambda",
            "ml_c4",
            "ml_c5",
            "ml_eia2",
            "ml_g4dn",
            "ml_inf1",
            "ml_m4",
            "ml_m5",
            "ml_p2",
            "ml_p3",
            "qcs603",
            "qcs605",
            "rasp3b",
            "rk3288",
            "rk3399",
            "sbe_c",
            "sitara_am57x",
            "x86_win32",
            "x86_win64",
        ]
    ] = Field(default=None, alias="CompilationTargetDevice")
    compilation_target_platform_os: Optional[Literal["ANDROID", "LINUX"]] = Field(
        default=None, alias="CompilationTargetPlatformOs"
    )
    compilation_target_platform_arch: Optional[
        Literal["ARM64", "ARM_EABI", "ARM_EABIHF", "X86", "X86_64"]
    ] = Field(default=None, alias="CompilationTargetPlatformArch")
    compilation_target_platform_accelerator: Optional[
        Literal["INTEL_GRAPHICS", "MALI", "NNA", "NVIDIA"]
    ] = Field(default=None, alias="CompilationTargetPlatformAccelerator")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ConditionStepMetadataModel(BaseModel):
    outcome: Optional[Literal["False", "True"]] = Field(default=None, alias="Outcome")


class MultiModelConfigModel(BaseModel):
    model_cache_setting: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="ModelCacheSetting"
    )


class ContextSourceModel(BaseModel):
    source_uri: str = Field(alias="SourceUri")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_id: Optional[str] = Field(default=None, alias="SourceId")


class ContinuousParameterRangeSpecificationModel(BaseModel):
    min_value: str = Field(alias="MinValue")
    max_value: str = Field(alias="MaxValue")


class ContinuousParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    min_value: str = Field(alias="MinValue")
    max_value: str = Field(alias="MaxValue")
    scaling_type: Optional[
        Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
    ] = Field(default=None, alias="ScalingType")


class ConvergenceDetectedModel(BaseModel):
    complete_on_convergence: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="CompleteOnConvergence"
    )


class MetadataPropertiesModel(BaseModel):
    commit_id: Optional[str] = Field(default=None, alias="CommitId")
    repository: Optional[str] = Field(default=None, alias="Repository")
    generated_by: Optional[str] = Field(default=None, alias="GeneratedBy")
    project_id: Optional[str] = Field(default=None, alias="ProjectId")


class ResourceSpecModel(BaseModel):
    sage_maker_image_arn: Optional[str] = Field(default=None, alias="SageMakerImageArn")
    sage_maker_image_version_arn: Optional[str] = Field(
        default=None, alias="SageMakerImageVersionArn"
    )
    instance_type: Optional[
        Literal[
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.16xlarge",
            "ml.m5d.24xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.8xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.t3.2xlarge",
            "ml.t3.large",
            "ml.t3.medium",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.xlarge",
            "system",
        ]
    ] = Field(default=None, alias="InstanceType")
    lifecycle_config_arn: Optional[str] = Field(
        default=None, alias="LifecycleConfigArn"
    )


class ModelDeployConfigModel(BaseModel):
    auto_generate_endpoint_name: Optional[bool] = Field(
        default=None, alias="AutoGenerateEndpointName"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")


class InputConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    data_input_config: str = Field(alias="DataInputConfig")
    framework: Literal[
        "DARKNET",
        "KERAS",
        "MXNET",
        "ONNX",
        "PYTORCH",
        "SKLEARN",
        "TENSORFLOW",
        "TFLITE",
        "XGBOOST",
    ] = Field(alias="Framework")
    framework_version: Optional[str] = Field(default=None, alias="FrameworkVersion")


class NeoVpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    subnets: Sequence[str] = Field(alias="Subnets")


class StoppingConditionModel(BaseModel):
    max_runtime_in_seconds: Optional[int] = Field(
        default=None, alias="MaxRuntimeInSeconds"
    )
    max_wait_time_in_seconds: Optional[int] = Field(
        default=None, alias="MaxWaitTimeInSeconds"
    )


class DataQualityAppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    container_entrypoint: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerEntrypoint"
    )
    container_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerArguments"
    )
    record_preprocessor_source_uri: Optional[str] = Field(
        default=None, alias="RecordPreprocessorSourceUri"
    )
    post_analytics_processor_source_uri: Optional[str] = Field(
        default=None, alias="PostAnalyticsProcessorSourceUri"
    )
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class MonitoringStoppingConditionModel(BaseModel):
    max_runtime_in_seconds: int = Field(alias="MaxRuntimeInSeconds")


class EdgeOutputConfigModel(BaseModel):
    s3_output_location: str = Field(alias="S3OutputLocation")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    preset_deployment_type: Optional[Literal["GreengrassV2Component"]] = Field(
        default=None, alias="PresetDeploymentType"
    )
    preset_deployment_config: Optional[str] = Field(
        default=None, alias="PresetDeploymentConfig"
    )


class EdgeDeploymentModelConfigModel(BaseModel):
    model_handle: str = Field(alias="ModelHandle")
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")


class FeatureDefinitionModel(BaseModel):
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")
    feature_type: Optional[Literal["Fractional", "Integral", "String"]] = Field(
        default=None, alias="FeatureType"
    )


class FlowDefinitionOutputConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class HumanLoopRequestSourceModel(BaseModel):
    aws_managed_human_loop_request_source: Literal[
        "AWS/Rekognition/DetectModerationLabels/Image/V3",
        "AWS/Textract/AnalyzeDocument/Forms/V1",
    ] = Field(alias="AwsManagedHumanLoopRequestSource")


class HubS3StorageConfigModel(BaseModel):
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")


class UiTemplateModel(BaseModel):
    content: str = Field(alias="Content")


class CreateImageVersionRequestModel(BaseModel):
    base_image: str = Field(alias="BaseImage")
    client_token: str = Field(alias="ClientToken")
    image_name: str = Field(alias="ImageName")
    aliases: Optional[Sequence[str]] = Field(default=None, alias="Aliases")
    vendor_guidance: Optional[
        Literal["ARCHIVED", "NOT_PROVIDED", "STABLE", "TO_BE_ARCHIVED"]
    ] = Field(default=None, alias="VendorGuidance")
    job_type: Optional[Literal["INFERENCE", "NOTEBOOK_KERNEL", "TRAINING"]] = Field(
        default=None, alias="JobType"
    )
    ml_framework: Optional[str] = Field(default=None, alias="MLFramework")
    programming_lang: Optional[str] = Field(default=None, alias="ProgrammingLang")
    processor: Optional[Literal["CPU", "GPU"]] = Field(default=None, alias="Processor")
    horovod: Optional[bool] = Field(default=None, alias="Horovod")
    release_notes: Optional[str] = Field(default=None, alias="ReleaseNotes")


class InferenceExperimentScheduleModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")


class LabelingJobOutputConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")


class LabelingJobStoppingConditionsModel(BaseModel):
    max_human_labeled_object_count: Optional[int] = Field(
        default=None, alias="MaxHumanLabeledObjectCount"
    )
    max_percentage_of_input_dataset_labeled: Optional[int] = Field(
        default=None, alias="MaxPercentageOfInputDatasetLabeled"
    )


class ModelBiasAppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    config_uri: str = Field(alias="ConfigUri")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class ModelCardExportOutputConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")


class ModelCardSecurityConfigModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ModelExplainabilityAppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    config_uri: str = Field(alias="ConfigUri")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class InferenceExecutionConfigModel(BaseModel):
    mode: Literal["Direct", "Serial"] = Field(alias="Mode")


class ModelQualityAppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    container_entrypoint: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerEntrypoint"
    )
    container_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerArguments"
    )
    record_preprocessor_source_uri: Optional[str] = Field(
        default=None, alias="RecordPreprocessorSourceUri"
    )
    post_analytics_processor_source_uri: Optional[str] = Field(
        default=None, alias="PostAnalyticsProcessorSourceUri"
    )
    problem_type: Optional[
        Literal["BinaryClassification", "MulticlassClassification", "Regression"]
    ] = Field(default=None, alias="ProblemType")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class InstanceMetadataServiceConfigurationModel(BaseModel):
    minimum_instance_metadata_service_version: str = Field(
        alias="MinimumInstanceMetadataServiceVersion"
    )


class NotebookInstanceLifecycleHookModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="Content")


class ParallelismConfigurationModel(BaseModel):
    max_parallel_execution_steps: int = Field(alias="MaxParallelExecutionSteps")


class PipelineDefinitionS3LocationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    object_key: str = Field(alias="ObjectKey")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class CreatePresignedDomainUrlRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")
    session_expiration_duration_in_seconds: Optional[int] = Field(
        default=None, alias="SessionExpirationDurationInSeconds"
    )
    expires_in_seconds: Optional[int] = Field(default=None, alias="ExpiresInSeconds")
    space_name: Optional[str] = Field(default=None, alias="SpaceName")


class CreatePresignedNotebookInstanceUrlInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    session_expiration_duration_in_seconds: Optional[int] = Field(
        default=None, alias="SessionExpirationDurationInSeconds"
    )


class ExperimentConfigModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    trial_component_display_name: Optional[str] = Field(
        default=None, alias="TrialComponentDisplayName"
    )
    run_name: Optional[str] = Field(default=None, alias="RunName")


class ProcessingStoppingConditionModel(BaseModel):
    max_runtime_in_seconds: int = Field(alias="MaxRuntimeInSeconds")


class DebugRuleConfigurationModel(BaseModel):
    rule_configuration_name: str = Field(alias="RuleConfigurationName")
    rule_evaluator_image: str = Field(alias="RuleEvaluatorImage")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.t3.2xlarge",
            "ml.t3.large",
            "ml.t3.medium",
            "ml.t3.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    rule_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuleParameters"
    )


class OutputDataConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ProfilerConfigModel(BaseModel):
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")
    profiling_interval_in_milliseconds: Optional[int] = Field(
        default=None, alias="ProfilingIntervalInMilliseconds"
    )
    profiling_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="ProfilingParameters"
    )
    disable_profiler: Optional[bool] = Field(default=None, alias="DisableProfiler")


class ProfilerRuleConfigurationModel(BaseModel):
    rule_configuration_name: str = Field(alias="RuleConfigurationName")
    rule_evaluator_image: str = Field(alias="RuleEvaluatorImage")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.t3.2xlarge",
            "ml.t3.large",
            "ml.t3.medium",
            "ml.t3.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    rule_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuleParameters"
    )


class RetryStrategyModel(BaseModel):
    maximum_retry_attempts: int = Field(alias="MaximumRetryAttempts")


class TensorBoardOutputConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")


class DataProcessingModel(BaseModel):
    input_filter: Optional[str] = Field(default=None, alias="InputFilter")
    output_filter: Optional[str] = Field(default=None, alias="OutputFilter")
    join_source: Optional[Literal["Input", "None"]] = Field(
        default=None, alias="JoinSource"
    )


class ModelClientConfigModel(BaseModel):
    invocations_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="InvocationsTimeoutInSeconds"
    )
    invocations_max_retries: Optional[int] = Field(
        default=None, alias="InvocationsMaxRetries"
    )


class TransformOutputModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    accept: Optional[str] = Field(default=None, alias="Accept")
    assemble_with: Optional[Literal["Line", "None"]] = Field(
        default=None, alias="AssembleWith"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class TransformResourcesModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
    ] = Field(alias="InstanceType")
    instance_count: int = Field(alias="InstanceCount")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")


class TrialComponentArtifactModel(BaseModel):
    value: str = Field(alias="Value")
    media_type: Optional[str] = Field(default=None, alias="MediaType")


class TrialComponentParameterValueModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    number_value: Optional[float] = Field(default=None, alias="NumberValue")


class TrialComponentStatusModel(BaseModel):
    primary_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="PrimaryStatus")
    message: Optional[str] = Field(default=None, alias="Message")


class OidcConfigModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    client_secret: str = Field(alias="ClientSecret")
    issuer: str = Field(alias="Issuer")
    authorization_endpoint: str = Field(alias="AuthorizationEndpoint")
    token_endpoint: str = Field(alias="TokenEndpoint")
    user_info_endpoint: str = Field(alias="UserInfoEndpoint")
    logout_endpoint: str = Field(alias="LogoutEndpoint")
    jwks_uri: str = Field(alias="JwksUri")


class SourceIpConfigModel(BaseModel):
    cidrs: Sequence[str] = Field(alias="Cidrs")


class WorkforceVpcConfigRequestModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")


class NotificationConfigurationModel(BaseModel):
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )


class CustomImageModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    app_image_config_name: str = Field(alias="AppImageConfigName")
    image_version_number: Optional[int] = Field(
        default=None, alias="ImageVersionNumber"
    )


class DataCaptureConfigSummaryModel(BaseModel):
    enable_capture: bool = Field(alias="EnableCapture")
    capture_status: Literal["Started", "Stopped"] = Field(alias="CaptureStatus")
    current_sampling_percentage: int = Field(alias="CurrentSamplingPercentage")
    destination_s3_uri: str = Field(alias="DestinationS3Uri")
    kms_key_id: str = Field(alias="KmsKeyId")


class DataCatalogConfigModel(BaseModel):
    table_name: str = Field(alias="TableName")
    catalog: str = Field(alias="Catalog")
    database: str = Field(alias="Database")


class MonitoringConstraintsResourceModel(BaseModel):
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")


class MonitoringStatisticsResourceModel(BaseModel):
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")


class EndpointInputModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    local_path: str = Field(alias="LocalPath")
    s3_input_mode: Optional[Literal["File", "Pipe"]] = Field(
        default=None, alias="S3InputMode"
    )
    s3_data_distribution_type: Optional[
        Literal["FullyReplicated", "ShardedByS3Key"]
    ] = Field(default=None, alias="S3DataDistributionType")
    features_attribute: Optional[str] = Field(default=None, alias="FeaturesAttribute")
    inference_attribute: Optional[str] = Field(default=None, alias="InferenceAttribute")
    probability_attribute: Optional[str] = Field(
        default=None, alias="ProbabilityAttribute"
    )
    probability_threshold_attribute: Optional[float] = Field(
        default=None, alias="ProbabilityThresholdAttribute"
    )
    start_time_offset: Optional[str] = Field(default=None, alias="StartTimeOffset")
    end_time_offset: Optional[str] = Field(default=None, alias="EndTimeOffset")


class FileSystemDataSourceModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    file_system_access_mode: Literal["ro", "rw"] = Field(alias="FileSystemAccessMode")
    file_system_type: Literal["EFS", "FSxLustre"] = Field(alias="FileSystemType")
    directory_path: str = Field(alias="DirectoryPath")


class S3DataSourceModel(BaseModel):
    s3_data_type: Literal["AugmentedManifestFile", "ManifestFile", "S3Prefix"] = Field(
        alias="S3DataType"
    )
    s3_uri: str = Field(alias="S3Uri")
    s3_data_distribution_type: Optional[
        Literal["FullyReplicated", "ShardedByS3Key"]
    ] = Field(default=None, alias="S3DataDistributionType")
    attribute_names: Optional[Sequence[str]] = Field(
        default=None, alias="AttributeNames"
    )
    instance_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="InstanceGroupNames"
    )


class RedshiftDatasetDefinitionModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    database: str = Field(alias="Database")
    db_user: str = Field(alias="DbUser")
    query_string: str = Field(alias="QueryString")
    cluster_role_arn: str = Field(alias="ClusterRoleArn")
    output_s3_uri: str = Field(alias="OutputS3Uri")
    output_format: Literal["CSV", "PARQUET"] = Field(alias="OutputFormat")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    output_compression: Optional[
        Literal["BZIP2", "GZIP", "None", "SNAPPY", "ZSTD"]
    ] = Field(default=None, alias="OutputCompression")


class DebugRuleEvaluationStatusModel(BaseModel):
    rule_configuration_name: Optional[str] = Field(
        default=None, alias="RuleConfigurationName"
    )
    rule_evaluation_job_arn: Optional[str] = Field(
        default=None, alias="RuleEvaluationJobArn"
    )
    rule_evaluation_status: Optional[
        Literal[
            "Error", "InProgress", "IssuesFound", "NoIssuesFound", "Stopped", "Stopping"
        ]
    ] = Field(default=None, alias="RuleEvaluationStatus")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class DeleteActionRequestModel(BaseModel):
    action_name: str = Field(alias="ActionName")


class DeleteAlgorithmInputRequestModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")


class DeleteAppImageConfigRequestModel(BaseModel):
    app_image_config_name: str = Field(alias="AppImageConfigName")


class DeleteAppRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    app_type: Literal[
        "JupyterServer",
        "KernelGateway",
        "RSessionGateway",
        "RStudioServerPro",
        "TensorBoard",
    ] = Field(alias="AppType")
    app_name: str = Field(alias="AppName")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    space_name: Optional[str] = Field(default=None, alias="SpaceName")


class DeleteAssociationRequestModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    destination_arn: str = Field(alias="DestinationArn")


class DeleteCodeRepositoryInputRequestModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")


class DeleteContextRequestModel(BaseModel):
    context_name: str = Field(alias="ContextName")


class DeleteDataQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DeleteDeviceFleetRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")


class RetentionPolicyModel(BaseModel):
    home_efs_file_system: Optional[Literal["Delete", "Retain"]] = Field(
        default=None, alias="HomeEfsFileSystem"
    )


class DeleteEdgeDeploymentPlanRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")


class DeleteEdgeDeploymentStageRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")


class DeleteEndpointConfigInputRequestModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")


class DeleteEndpointInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class DeleteExperimentRequestModel(BaseModel):
    experiment_name: str = Field(alias="ExperimentName")


class DeleteFeatureGroupRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")


class DeleteFlowDefinitionRequestModel(BaseModel):
    flow_definition_name: str = Field(alias="FlowDefinitionName")


class DeleteHubContentRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    hub_content_name: str = Field(alias="HubContentName")
    hub_content_version: str = Field(alias="HubContentVersion")


class DeleteHubRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")


class DeleteHumanTaskUiRequestModel(BaseModel):
    human_task_ui_name: str = Field(alias="HumanTaskUiName")


class DeleteImageRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")


class DeleteImageVersionRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    version: Optional[int] = Field(default=None, alias="Version")
    alias: Optional[str] = Field(default=None, alias="Alias")


class DeleteInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteModelBiasJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DeleteModelCardRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")


class DeleteModelExplainabilityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DeleteModelInputRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class DeleteModelPackageGroupInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")


class DeleteModelPackageGroupPolicyInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")


class DeleteModelPackageInputRequestModel(BaseModel):
    model_package_name: str = Field(alias="ModelPackageName")


class DeleteModelQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DeleteMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")


class DeleteNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")


class DeleteNotebookInstanceLifecycleConfigInputRequestModel(BaseModel):
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )


class DeletePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    client_request_token: str = Field(alias="ClientRequestToken")


class DeleteProjectInputRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")


class DeleteSpaceRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    space_name: str = Field(alias="SpaceName")


class DeleteStudioLifecycleConfigRequestModel(BaseModel):
    studio_lifecycle_config_name: str = Field(alias="StudioLifecycleConfigName")


class DeleteTagsInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DeleteTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")


class DeleteTrialRequestModel(BaseModel):
    trial_name: str = Field(alias="TrialName")


class DeleteUserProfileRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")


class DeleteWorkforceRequestModel(BaseModel):
    workforce_name: str = Field(alias="WorkforceName")


class DeleteWorkteamRequestModel(BaseModel):
    workteam_name: str = Field(alias="WorkteamName")


class DeployedImageModel(BaseModel):
    specified_image: Optional[str] = Field(default=None, alias="SpecifiedImage")
    resolved_image: Optional[str] = Field(default=None, alias="ResolvedImage")
    resolution_time: Optional[datetime] = Field(default=None, alias="ResolutionTime")


class DeviceSelectionConfigModel(BaseModel):
    device_subset_type: Literal["NAMECONTAINS", "PERCENTAGE", "SELECTION"] = Field(
        alias="DeviceSubsetType"
    )
    percentage: Optional[int] = Field(default=None, alias="Percentage")
    device_names: Optional[Sequence[str]] = Field(default=None, alias="DeviceNames")
    device_name_contains: Optional[str] = Field(
        default=None, alias="DeviceNameContains"
    )


class EdgeDeploymentConfigModel(BaseModel):
    failure_handling_policy: Literal["DO_NOTHING", "ROLLBACK_ON_FAILURE"] = Field(
        alias="FailureHandlingPolicy"
    )


class EdgeDeploymentStatusModel(BaseModel):
    stage_status: Literal[
        "CREATING",
        "DEPLOYED",
        "FAILED",
        "INPROGRESS",
        "READYTODEPLOY",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="StageStatus")
    edge_deployment_success_in_stage: int = Field(alias="EdgeDeploymentSuccessInStage")
    edge_deployment_pending_in_stage: int = Field(alias="EdgeDeploymentPendingInStage")
    edge_deployment_failed_in_stage: int = Field(alias="EdgeDeploymentFailedInStage")
    edge_deployment_status_message: Optional[str] = Field(
        default=None, alias="EdgeDeploymentStatusMessage"
    )
    edge_deployment_stage_start_time: Optional[datetime] = Field(
        default=None, alias="EdgeDeploymentStageStartTime"
    )


class DeregisterDevicesRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    device_names: Sequence[str] = Field(alias="DeviceNames")


class DescribeActionRequestModel(BaseModel):
    action_name: str = Field(alias="ActionName")


class DescribeAlgorithmInputRequestModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")


class DescribeAppImageConfigRequestModel(BaseModel):
    app_image_config_name: str = Field(alias="AppImageConfigName")


class DescribeAppRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    app_type: Literal[
        "JupyterServer",
        "KernelGateway",
        "RSessionGateway",
        "RStudioServerPro",
        "TensorBoard",
    ] = Field(alias="AppType")
    app_name: str = Field(alias="AppName")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    space_name: Optional[str] = Field(default=None, alias="SpaceName")


class DescribeArtifactRequestModel(BaseModel):
    artifact_arn: str = Field(alias="ArtifactArn")


class DescribeAutoMLJobRequestModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")


class ModelDeployResultModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")


class DescribeCodeRepositoryInputRequestModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")


class DescribeCompilationJobRequestModel(BaseModel):
    compilation_job_name: str = Field(alias="CompilationJobName")


class ModelArtifactsModel(BaseModel):
    s3_model_artifacts: str = Field(alias="S3ModelArtifacts")


class ModelDigestsModel(BaseModel):
    artifact_digest: Optional[str] = Field(default=None, alias="ArtifactDigest")


class DescribeContextRequestModel(BaseModel):
    context_name: str = Field(alias="ContextName")


class DescribeDataQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DescribeDeviceFleetRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")


class DescribeDeviceRequestModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EdgeModelModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    model_version: str = Field(alias="ModelVersion")
    latest_sample_time: Optional[datetime] = Field(
        default=None, alias="LatestSampleTime"
    )
    latest_inference: Optional[datetime] = Field(default=None, alias="LatestInference")


class DescribeDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")


class DescribeEdgeDeploymentPlanRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeEdgePackagingJobRequestModel(BaseModel):
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")


class EdgePresetDeploymentOutputModel(BaseModel):
    type: Literal["GreengrassV2Component"] = Field(alias="Type")
    artifact: Optional[str] = Field(default=None, alias="Artifact")
    status: Optional[Literal["COMPLETED", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class DescribeEndpointConfigInputRequestModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeEndpointInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class DescribeExperimentRequestModel(BaseModel):
    experiment_name: str = Field(alias="ExperimentName")


class ExperimentSourceModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")


class DescribeFeatureGroupRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LastUpdateStatusModel(BaseModel):
    status: Literal["Failed", "InProgress", "Successful"] = Field(alias="Status")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class OfflineStoreStatusModel(BaseModel):
    status: Literal["Active", "Blocked", "Disabled"] = Field(alias="Status")
    blocked_reason: Optional[str] = Field(default=None, alias="BlockedReason")


class DescribeFeatureMetadataRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    feature_name: str = Field(alias="FeatureName")


class FeatureParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class DescribeFlowDefinitionRequestModel(BaseModel):
    flow_definition_name: str = Field(alias="FlowDefinitionName")


class DescribeHubContentRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    hub_content_name: str = Field(alias="HubContentName")
    hub_content_version: Optional[str] = Field(default=None, alias="HubContentVersion")


class HubContentDependencyModel(BaseModel):
    dependency_origin_path: Optional[str] = Field(
        default=None, alias="DependencyOriginPath"
    )
    dependency_copy_path: Optional[str] = Field(
        default=None, alias="DependencyCopyPath"
    )


class DescribeHubRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")


class DescribeHumanTaskUiRequestModel(BaseModel):
    human_task_ui_name: str = Field(alias="HumanTaskUiName")


class UiTemplateInfoModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    content_sha256: Optional[str] = Field(default=None, alias="ContentSha256")


class DescribeHyperParameterTuningJobRequestModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")


class HyperParameterTuningJobCompletionDetailsModel(BaseModel):
    number_of_training_jobs_objective_not_improving: Optional[int] = Field(
        default=None, alias="NumberOfTrainingJobsObjectiveNotImproving"
    )
    convergence_detected_time: Optional[datetime] = Field(
        default=None, alias="ConvergenceDetectedTime"
    )


class HyperParameterTuningJobConsumedResourcesModel(BaseModel):
    runtime_in_seconds: Optional[int] = Field(default=None, alias="RuntimeInSeconds")


class ObjectiveStatusCountersModel(BaseModel):
    succeeded: Optional[int] = Field(default=None, alias="Succeeded")
    pending: Optional[int] = Field(default=None, alias="Pending")
    failed: Optional[int] = Field(default=None, alias="Failed")


class TrainingJobStatusCountersModel(BaseModel):
    completed: Optional[int] = Field(default=None, alias="Completed")
    in_progress: Optional[int] = Field(default=None, alias="InProgress")
    retryable_error: Optional[int] = Field(default=None, alias="RetryableError")
    non_retryable_error: Optional[int] = Field(default=None, alias="NonRetryableError")
    stopped: Optional[int] = Field(default=None, alias="Stopped")


class DescribeImageRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")


class DescribeImageVersionRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    version: Optional[int] = Field(default=None, alias="Version")
    alias: Optional[str] = Field(default=None, alias="Alias")


class DescribeInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")


class EndpointMetadataModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_config_name: Optional[str] = Field(
        default=None, alias="EndpointConfigName"
    )
    endpoint_status: Optional[
        Literal[
            "Creating",
            "Deleting",
            "Failed",
            "InService",
            "OutOfService",
            "RollingBack",
            "SystemUpdating",
            "Updating",
        ]
    ] = Field(default=None, alias="EndpointStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class DescribeInferenceRecommendationsJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")


class DescribeLabelingJobRequestModel(BaseModel):
    labeling_job_name: str = Field(alias="LabelingJobName")


class LabelCountersModel(BaseModel):
    total_labeled: Optional[int] = Field(default=None, alias="TotalLabeled")
    human_labeled: Optional[int] = Field(default=None, alias="HumanLabeled")
    machine_labeled: Optional[int] = Field(default=None, alias="MachineLabeled")
    failed_non_retryable_error: Optional[int] = Field(
        default=None, alias="FailedNonRetryableError"
    )
    unlabeled: Optional[int] = Field(default=None, alias="Unlabeled")


class LabelingJobOutputModel(BaseModel):
    output_dataset_s3_uri: str = Field(alias="OutputDatasetS3Uri")
    final_active_learning_model_arn: Optional[str] = Field(
        default=None, alias="FinalActiveLearningModelArn"
    )


class DescribeLineageGroupRequestModel(BaseModel):
    lineage_group_name: str = Field(alias="LineageGroupName")


class DescribeModelBiasJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DescribeModelCardExportJobRequestModel(BaseModel):
    model_card_export_job_arn: str = Field(alias="ModelCardExportJobArn")


class ModelCardExportArtifactsModel(BaseModel):
    s3_export_artifacts: str = Field(alias="S3ExportArtifacts")


class DescribeModelCardRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")


class DescribeModelExplainabilityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DescribeModelInputRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class DescribeModelPackageGroupInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")


class DescribeModelPackageInputRequestModel(BaseModel):
    model_package_name: str = Field(alias="ModelPackageName")


class DescribeModelQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")


class DescribeMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")


class MonitoringExecutionSummaryModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    scheduled_time: datetime = Field(alias="ScheduledTime")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    monitoring_execution_status: Literal[
        "Completed",
        "CompletedWithViolations",
        "Failed",
        "InProgress",
        "Pending",
        "Stopped",
        "Stopping",
    ] = Field(alias="MonitoringExecutionStatus")
    processing_job_arn: Optional[str] = Field(default=None, alias="ProcessingJobArn")
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringType")


class DescribeNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")


class DescribeNotebookInstanceLifecycleConfigInputRequestModel(BaseModel):
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )


class DescribePipelineDefinitionForExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")


class DescribePipelineExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")


class PipelineExperimentConfigModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_name: Optional[str] = Field(default=None, alias="TrialName")


class DescribePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")


class DescribeProcessingJobRequestModel(BaseModel):
    processing_job_name: str = Field(alias="ProcessingJobName")


class DescribeProjectInputRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")


class ServiceCatalogProvisionedProductDetailsModel(BaseModel):
    provisioned_product_id: Optional[str] = Field(
        default=None, alias="ProvisionedProductId"
    )
    provisioned_product_status_message: Optional[str] = Field(
        default=None, alias="ProvisionedProductStatusMessage"
    )


class DescribeSpaceRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    space_name: str = Field(alias="SpaceName")


class DescribeStudioLifecycleConfigRequestModel(BaseModel):
    studio_lifecycle_config_name: str = Field(alias="StudioLifecycleConfigName")


class DescribeSubscribedWorkteamRequestModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")


class SubscribedWorkteamModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")
    marketplace_title: Optional[str] = Field(default=None, alias="MarketplaceTitle")
    seller_name: Optional[str] = Field(default=None, alias="SellerName")
    marketplace_description: Optional[str] = Field(
        default=None, alias="MarketplaceDescription"
    )
    listing_id: Optional[str] = Field(default=None, alias="ListingId")


class DescribeTrainingJobRequestModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")


class MetricDataModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    value: Optional[float] = Field(default=None, alias="Value")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class ProfilerRuleEvaluationStatusModel(BaseModel):
    rule_configuration_name: Optional[str] = Field(
        default=None, alias="RuleConfigurationName"
    )
    rule_evaluation_job_arn: Optional[str] = Field(
        default=None, alias="RuleEvaluationJobArn"
    )
    rule_evaluation_status: Optional[
        Literal[
            "Error", "InProgress", "IssuesFound", "NoIssuesFound", "Stopped", "Stopping"
        ]
    ] = Field(default=None, alias="RuleEvaluationStatus")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class SecondaryStatusTransitionModel(BaseModel):
    status: Literal[
        "Completed",
        "Downloading",
        "DownloadingTrainingImage",
        "Failed",
        "Interrupted",
        "LaunchingMLInstances",
        "MaxRuntimeExceeded",
        "MaxWaitTimeExceeded",
        "PreparingTrainingStack",
        "Restarting",
        "Starting",
        "Stopped",
        "Stopping",
        "Training",
        "Updating",
        "Uploading",
    ] = Field(alias="Status")
    start_time: datetime = Field(alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class WarmPoolStatusModel(BaseModel):
    status: Literal["Available", "InUse", "Reused", "Terminated"] = Field(
        alias="Status"
    )
    resource_retained_billable_time_in_seconds: Optional[int] = Field(
        default=None, alias="ResourceRetainedBillableTimeInSeconds"
    )
    reused_by_job: Optional[str] = Field(default=None, alias="ReusedByJob")


class DescribeTransformJobRequestModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")


class DescribeTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")


class TrialComponentMetricSummaryModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    time_stamp: Optional[datetime] = Field(default=None, alias="TimeStamp")
    max: Optional[float] = Field(default=None, alias="Max")
    min: Optional[float] = Field(default=None, alias="Min")
    last: Optional[float] = Field(default=None, alias="Last")
    count: Optional[int] = Field(default=None, alias="Count")
    avg: Optional[float] = Field(default=None, alias="Avg")
    std_dev: Optional[float] = Field(default=None, alias="StdDev")


class TrialComponentSourceModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")


class DescribeTrialRequestModel(BaseModel):
    trial_name: str = Field(alias="TrialName")


class TrialSourceModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")


class DescribeUserProfileRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")


class DescribeWorkforceRequestModel(BaseModel):
    workforce_name: str = Field(alias="WorkforceName")


class DescribeWorkteamRequestModel(BaseModel):
    workteam_name: str = Field(alias="WorkteamName")


class DesiredWeightAndCapacityModel(BaseModel):
    variant_name: str = Field(alias="VariantName")
    desired_weight: Optional[float] = Field(default=None, alias="DesiredWeight")
    desired_instance_count: Optional[int] = Field(
        default=None, alias="DesiredInstanceCount"
    )


class DeviceDeploymentSummaryModel(BaseModel):
    edge_deployment_plan_arn: str = Field(alias="EdgeDeploymentPlanArn")
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")
    device_name: str = Field(alias="DeviceName")
    device_arn: str = Field(alias="DeviceArn")
    deployed_stage_name: Optional[str] = Field(default=None, alias="DeployedStageName")
    device_fleet_name: Optional[str] = Field(default=None, alias="DeviceFleetName")
    device_deployment_status: Optional[
        Literal[
            "DEPLOYED", "FAILED", "INPROGRESS", "READYTODEPLOY", "STOPPED", "STOPPING"
        ]
    ] = Field(default=None, alias="DeviceDeploymentStatus")
    device_deployment_status_message: Optional[str] = Field(
        default=None, alias="DeviceDeploymentStatusMessage"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    deployment_start_time: Optional[datetime] = Field(
        default=None, alias="DeploymentStartTime"
    )


class DeviceFleetSummaryModel(BaseModel):
    device_fleet_arn: str = Field(alias="DeviceFleetArn")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class DeviceStatsModel(BaseModel):
    connected_device_count: int = Field(alias="ConnectedDeviceCount")
    registered_device_count: int = Field(alias="RegisteredDeviceCount")


class EdgeModelSummaryModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    model_version: str = Field(alias="ModelVersion")


class DeviceModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    description: Optional[str] = Field(default=None, alias="Description")
    iot_thing_name: Optional[str] = Field(default=None, alias="IotThingName")


class DisassociateTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    trial_name: str = Field(alias="TrialName")


class DomainDetailsModel(BaseModel):
    domain_arn: Optional[str] = Field(default=None, alias="DomainArn")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    status: Optional[
        Literal[
            "Delete_Failed",
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Update_Failed",
            "Updating",
        ]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    url: Optional[str] = Field(default=None, alias="Url")


class FileSourceModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    content_digest: Optional[str] = Field(default=None, alias="ContentDigest")


class EMRStepMetadataModel(BaseModel):
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    step_id: Optional[str] = Field(default=None, alias="StepId")
    step_name: Optional[str] = Field(default=None, alias="StepName")
    log_file_path: Optional[str] = Field(default=None, alias="LogFilePath")


class EdgeDeploymentPlanSummaryModel(BaseModel):
    edge_deployment_plan_arn: str = Field(alias="EdgeDeploymentPlanArn")
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    edge_deployment_success: int = Field(alias="EdgeDeploymentSuccess")
    edge_deployment_pending: int = Field(alias="EdgeDeploymentPending")
    edge_deployment_failed: int = Field(alias="EdgeDeploymentFailed")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class EdgeModelStatModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    model_version: str = Field(alias="ModelVersion")
    offline_device_count: int = Field(alias="OfflineDeviceCount")
    connected_device_count: int = Field(alias="ConnectedDeviceCount")
    active_device_count: int = Field(alias="ActiveDeviceCount")
    sampling_device_count: int = Field(alias="SamplingDeviceCount")


class EdgePackagingJobSummaryModel(BaseModel):
    edge_packaging_job_arn: str = Field(alias="EdgePackagingJobArn")
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")
    edge_packaging_job_status: Literal[
        "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
    ] = Field(alias="EdgePackagingJobStatus")
    compilation_job_name: Optional[str] = Field(
        default=None, alias="CompilationJobName"
    )
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class EdgeModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    association_type: Optional[
        Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
    ] = Field(default=None, alias="AssociationType")


class EndpointConfigSummaryModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    endpoint_config_arn: str = Field(alias="EndpointConfigArn")
    creation_time: datetime = Field(alias="CreationTime")


class EndpointInfoModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class EndpointOutputConfigurationModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    variant_name: str = Field(alias="VariantName")
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.large",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.large",
        "ml.c5.xlarge",
        "ml.c5d.18xlarge",
        "ml.c5d.2xlarge",
        "ml.c5d.4xlarge",
        "ml.c5d.9xlarge",
        "ml.c5d.large",
        "ml.c5d.xlarge",
        "ml.c6g.12xlarge",
        "ml.c6g.16xlarge",
        "ml.c6g.2xlarge",
        "ml.c6g.4xlarge",
        "ml.c6g.8xlarge",
        "ml.c6g.large",
        "ml.c6g.xlarge",
        "ml.c6gd.12xlarge",
        "ml.c6gd.16xlarge",
        "ml.c6gd.2xlarge",
        "ml.c6gd.4xlarge",
        "ml.c6gd.8xlarge",
        "ml.c6gd.large",
        "ml.c6gd.xlarge",
        "ml.c6gn.12xlarge",
        "ml.c6gn.16xlarge",
        "ml.c6gn.2xlarge",
        "ml.c6gn.4xlarge",
        "ml.c6gn.8xlarge",
        "ml.c6gn.large",
        "ml.c6gn.xlarge",
        "ml.c6i.12xlarge",
        "ml.c6i.16xlarge",
        "ml.c6i.24xlarge",
        "ml.c6i.2xlarge",
        "ml.c6i.32xlarge",
        "ml.c6i.4xlarge",
        "ml.c6i.8xlarge",
        "ml.c6i.large",
        "ml.c6i.xlarge",
        "ml.c7g.12xlarge",
        "ml.c7g.16xlarge",
        "ml.c7g.2xlarge",
        "ml.c7g.4xlarge",
        "ml.c7g.8xlarge",
        "ml.c7g.large",
        "ml.c7g.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.inf1.24xlarge",
        "ml.inf1.2xlarge",
        "ml.inf1.6xlarge",
        "ml.inf1.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.m5d.12xlarge",
        "ml.m5d.24xlarge",
        "ml.m5d.2xlarge",
        "ml.m5d.4xlarge",
        "ml.m5d.large",
        "ml.m5d.xlarge",
        "ml.m6g.12xlarge",
        "ml.m6g.16xlarge",
        "ml.m6g.2xlarge",
        "ml.m6g.4xlarge",
        "ml.m6g.8xlarge",
        "ml.m6g.large",
        "ml.m6g.xlarge",
        "ml.m6gd.12xlarge",
        "ml.m6gd.16xlarge",
        "ml.m6gd.2xlarge",
        "ml.m6gd.4xlarge",
        "ml.m6gd.8xlarge",
        "ml.m6gd.large",
        "ml.m6gd.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p4d.24xlarge",
        "ml.p4de.24xlarge",
        "ml.r5.12xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.r5d.12xlarge",
        "ml.r5d.24xlarge",
        "ml.r5d.2xlarge",
        "ml.r5d.4xlarge",
        "ml.r5d.large",
        "ml.r5d.xlarge",
        "ml.r6g.12xlarge",
        "ml.r6g.16xlarge",
        "ml.r6g.2xlarge",
        "ml.r6g.4xlarge",
        "ml.r6g.8xlarge",
        "ml.r6g.large",
        "ml.r6g.xlarge",
        "ml.r6gd.12xlarge",
        "ml.r6gd.16xlarge",
        "ml.r6gd.2xlarge",
        "ml.r6gd.4xlarge",
        "ml.r6gd.8xlarge",
        "ml.r6gd.large",
        "ml.r6gd.xlarge",
        "ml.t2.2xlarge",
        "ml.t2.large",
        "ml.t2.medium",
        "ml.t2.xlarge",
    ] = Field(alias="InstanceType")
    initial_instance_count: int = Field(alias="InitialInstanceCount")


class InferenceMetricsModel(BaseModel):
    max_invocations: int = Field(alias="MaxInvocations")
    model_latency: int = Field(alias="ModelLatency")


class EndpointSummaryModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_arn: str = Field(alias="EndpointArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    endpoint_status: Literal[
        "Creating",
        "Deleting",
        "Failed",
        "InService",
        "OutOfService",
        "RollingBack",
        "SystemUpdating",
        "Updating",
    ] = Field(alias="EndpointStatus")


class EnvironmentParameterModel(BaseModel):
    key: str = Field(alias="Key")
    value_type: str = Field(alias="ValueType")
    value: str = Field(alias="Value")


class FailStepMetadataModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class FileSystemConfigModel(BaseModel):
    mount_path: Optional[str] = Field(default=None, alias="MountPath")
    default_uid: Optional[int] = Field(default=None, alias="DefaultUid")
    default_gid: Optional[int] = Field(default=None, alias="DefaultGid")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    operator: Optional[
        Literal[
            "Contains",
            "Equals",
            "Exists",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "In",
            "LessThan",
            "LessThanOrEqualTo",
            "NotEquals",
            "NotExists",
        ]
    ] = Field(default=None, alias="Operator")
    value: Optional[str] = Field(default=None, alias="Value")


class FinalHyperParameterTuningJobObjectiveMetricModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    value: float = Field(alias="Value")
    type: Optional[Literal["Maximize", "Minimize"]] = Field(default=None, alias="Type")


class FlowDefinitionSummaryModel(BaseModel):
    flow_definition_name: str = Field(alias="FlowDefinitionName")
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    flow_definition_status: Literal[
        "Active", "Deleting", "Failed", "Initializing"
    ] = Field(alias="FlowDefinitionStatus")
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class GetDeviceFleetReportRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")


class GetLineageGroupPolicyRequestModel(BaseModel):
    lineage_group_name: str = Field(alias="LineageGroupName")


class GetModelPackageGroupPolicyInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")


class PropertyNameSuggestionModel(BaseModel):
    property_name: Optional[str] = Field(default=None, alias="PropertyName")


class GitConfigForUpdateModel(BaseModel):
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")


class HubContentInfoModel(BaseModel):
    hub_content_name: str = Field(alias="HubContentName")
    hub_content_arn: str = Field(alias="HubContentArn")
    hub_content_version: str = Field(alias="HubContentVersion")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    document_schema_version: str = Field(alias="DocumentSchemaVersion")
    hub_content_status: Literal[
        "Available", "DeleteFailed", "Deleting", "ImportFailed", "Importing"
    ] = Field(alias="HubContentStatus")
    creation_time: datetime = Field(alias="CreationTime")
    hub_content_display_name: Optional[str] = Field(
        default=None, alias="HubContentDisplayName"
    )
    hub_content_description: Optional[str] = Field(
        default=None, alias="HubContentDescription"
    )
    hub_content_search_keywords: Optional[List[str]] = Field(
        default=None, alias="HubContentSearchKeywords"
    )


class HubInfoModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_arn: str = Field(alias="HubArn")
    hub_status: Literal[
        "CreateFailed",
        "Creating",
        "DeleteFailed",
        "Deleting",
        "InService",
        "UpdateFailed",
        "Updating",
    ] = Field(alias="HubStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    hub_display_name: Optional[str] = Field(default=None, alias="HubDisplayName")
    hub_description: Optional[str] = Field(default=None, alias="HubDescription")
    hub_search_keywords: Optional[List[str]] = Field(
        default=None, alias="HubSearchKeywords"
    )


class HumanLoopActivationConditionsConfigModel(BaseModel):
    human_loop_activation_conditions: str = Field(alias="HumanLoopActivationConditions")


class UiConfigModel(BaseModel):
    ui_template_s3_uri: Optional[str] = Field(default=None, alias="UiTemplateS3Uri")
    human_task_ui_arn: Optional[str] = Field(default=None, alias="HumanTaskUiArn")


class HumanTaskUiSummaryModel(BaseModel):
    human_task_ui_name: str = Field(alias="HumanTaskUiName")
    human_task_ui_arn: str = Field(alias="HumanTaskUiArn")
    creation_time: datetime = Field(alias="CreationTime")


class HyperParameterTuningJobObjectiveModel(BaseModel):
    type: Literal["Maximize", "Minimize"] = Field(alias="Type")
    metric_name: str = Field(alias="MetricName")


class HyperParameterTuningInstanceConfigModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5n.18xlarge",
        "ml.c5n.2xlarge",
        "ml.c5n.4xlarge",
        "ml.c5n.9xlarge",
        "ml.c5n.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.p4d.24xlarge",
        "ml.trn1.2xlarge",
        "ml.trn1.32xlarge",
    ] = Field(alias="InstanceType")
    instance_count: int = Field(alias="InstanceCount")
    volume_size_in_gb: int = Field(alias="VolumeSizeInGB")


class ResourceLimitsModel(BaseModel):
    max_parallel_training_jobs: int = Field(alias="MaxParallelTrainingJobs")
    max_number_of_training_jobs: Optional[int] = Field(
        default=None, alias="MaxNumberOfTrainingJobs"
    )
    max_runtime_in_seconds: Optional[int] = Field(
        default=None, alias="MaxRuntimeInSeconds"
    )


class HyperbandStrategyConfigModel(BaseModel):
    min_resource: Optional[int] = Field(default=None, alias="MinResource")
    max_resource: Optional[int] = Field(default=None, alias="MaxResource")


class ParentHyperParameterTuningJobModel(BaseModel):
    hyper_parameter_tuning_job_name: Optional[str] = Field(
        default=None, alias="HyperParameterTuningJobName"
    )


class RepositoryAuthConfigModel(BaseModel):
    repository_credentials_provider_arn: str = Field(
        alias="RepositoryCredentialsProviderArn"
    )


class ImageModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    image_arn: str = Field(alias="ImageArn")
    image_name: str = Field(alias="ImageName")
    image_status: Literal[
        "CREATED",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="ImageStatus")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class ImageVersionModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    image_arn: str = Field(alias="ImageArn")
    image_version_arn: str = Field(alias="ImageVersionArn")
    image_version_status: Literal[
        "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
    ] = Field(alias="ImageVersionStatus")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    version: int = Field(alias="Version")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class RecommendationMetricsModel(BaseModel):
    cost_per_hour: float = Field(alias="CostPerHour")
    cost_per_inference: float = Field(alias="CostPerInference")
    max_invocations: int = Field(alias="MaxInvocations")
    model_latency: int = Field(alias="ModelLatency")
    cpu_utilization: Optional[float] = Field(default=None, alias="CpuUtilization")
    memory_utilization: Optional[float] = Field(default=None, alias="MemoryUtilization")


class InferenceRecommendationsJobModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_description: str = Field(alias="JobDescription")
    job_type: Literal["Advanced", "Default"] = Field(alias="JobType")
    job_arn: str = Field(alias="JobArn")
    status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"
    ] = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    role_arn: str = Field(alias="RoleArn")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class InstanceGroupModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5n.18xlarge",
        "ml.c5n.2xlarge",
        "ml.c5n.4xlarge",
        "ml.c5n.9xlarge",
        "ml.c5n.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.p4d.24xlarge",
        "ml.trn1.2xlarge",
        "ml.trn1.32xlarge",
    ] = Field(alias="InstanceType")
    instance_count: int = Field(alias="InstanceCount")
    instance_group_name: str = Field(alias="InstanceGroupName")


class IntegerParameterRangeSpecificationModel(BaseModel):
    min_value: str = Field(alias="MinValue")
    max_value: str = Field(alias="MaxValue")


class IntegerParameterRangeModel(BaseModel):
    name: str = Field(alias="Name")
    min_value: str = Field(alias="MinValue")
    max_value: str = Field(alias="MaxValue")
    scaling_type: Optional[
        Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
    ] = Field(default=None, alias="ScalingType")


class KernelSpecModel(BaseModel):
    name: str = Field(alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class LabelCountersForWorkteamModel(BaseModel):
    human_labeled: Optional[int] = Field(default=None, alias="HumanLabeled")
    pending_human: Optional[int] = Field(default=None, alias="PendingHuman")
    total: Optional[int] = Field(default=None, alias="Total")


class LabelingJobDataAttributesModel(BaseModel):
    content_classifiers: Optional[
        Sequence[
            Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
        ]
    ] = Field(default=None, alias="ContentClassifiers")


class LabelingJobS3DataSourceModel(BaseModel):
    manifest_s3_uri: str = Field(alias="ManifestS3Uri")


class LabelingJobSnsDataSourceModel(BaseModel):
    sns_topic_arn: str = Field(alias="SnsTopicArn")


class LineageGroupSummaryModel(BaseModel):
    lineage_group_arn: Optional[str] = Field(default=None, alias="LineageGroupArn")
    lineage_group_name: Optional[str] = Field(default=None, alias="LineageGroupName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListActionsRequestModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    action_type: Optional[str] = Field(default=None, alias="ActionType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAlgorithmsInputRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListAliasesRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    alias: Optional[str] = Field(default=None, alias="Alias")
    version: Optional[int] = Field(default=None, alias="Version")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppImageConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeBefore"
    )
    modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeAfter"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListAppsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    user_profile_name_equals: Optional[str] = Field(
        default=None, alias="UserProfileNameEquals"
    )
    space_name_equals: Optional[str] = Field(default=None, alias="SpaceNameEquals")


class ListArtifactsRequestModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    artifact_type: Optional[str] = Field(default=None, alias="ArtifactType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAssociationsRequestModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    destination_type: Optional[str] = Field(default=None, alias="DestinationType")
    association_type: Optional[
        Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
    ] = Field(default=None, alias="AssociationType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[
        Literal[
            "CreationTime",
            "DestinationArn",
            "DestinationType",
            "SourceArn",
            "SourceType",
        ]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAutoMLJobsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCandidatesForAutoMLJobRequestModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    candidate_name_equals: Optional[str] = Field(
        default=None, alias="CandidateNameEquals"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[
        Literal["CreationTime", "FinalObjectiveMetricValue", "Status"]
    ] = Field(default=None, alias="SortBy")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCodeRepositoriesInputRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListCompilationJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListContextsRequestModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    context_type: Optional[str] = Field(default=None, alias="ContextType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataQualityJobDefinitionsRequestModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class MonitoringJobDefinitionSummaryModel(BaseModel):
    monitoring_job_definition_name: str = Field(alias="MonitoringJobDefinitionName")
    monitoring_job_definition_arn: str = Field(alias="MonitoringJobDefinitionArn")
    creation_time: datetime = Field(alias="CreationTime")
    endpoint_name: str = Field(alias="EndpointName")


class ListDeviceFleetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListDevicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    latest_heartbeat_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LatestHeartbeatAfter"
    )
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    device_fleet_name: Optional[str] = Field(default=None, alias="DeviceFleetName")


class ListDomainsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEdgeDeploymentPlansRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    device_fleet_name_contains: Optional[str] = Field(
        default=None, alias="DeviceFleetNameContains"
    )
    sort_by: Optional[
        Literal["CREATION_TIME", "DEVICE_FLEET_NAME", "LAST_MODIFIED_TIME", "NAME"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListEdgePackagingJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_name_contains: Optional[str] = Field(default=None, alias="ModelNameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[
        Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "MODEL_NAME", "NAME", "STATUS"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListEndpointConfigsInputRequestModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class ListEndpointsInputRequestModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Creating",
            "Deleting",
            "Failed",
            "InService",
            "OutOfService",
            "RollingBack",
            "SystemUpdating",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")


class ListExperimentsRequestModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFeatureGroupsRequestModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    feature_group_status_equals: Optional[
        Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
    ] = Field(default=None, alias="FeatureGroupStatusEquals")
    offline_store_status_equals: Optional[
        Literal["Active", "Blocked", "Disabled"]
    ] = Field(default=None, alias="OfflineStoreStatusEquals")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[
        Literal["CreationTime", "FeatureGroupStatus", "Name", "OfflineStoreStatus"]
    ] = Field(default=None, alias="SortBy")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFlowDefinitionsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListHubContentVersionsRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    hub_content_name: str = Field(alias="HubContentName")
    min_version: Optional[str] = Field(default=None, alias="MinVersion")
    max_schema_version: Optional[str] = Field(default=None, alias="MaxSchemaVersion")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    sort_by: Optional[
        Literal["CreationTime", "HubContentName", "HubContentStatus"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHubContentsRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    max_schema_version: Optional[str] = Field(default=None, alias="MaxSchemaVersion")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    sort_by: Optional[
        Literal["CreationTime", "HubContentName", "HubContentStatus"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHubsRequestModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    sort_by: Optional[
        Literal["AccountIdOwner", "CreationTime", "HubName", "HubStatus"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHumanTaskUisRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListHyperParameterTuningJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")


class ListImageVersionsRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[
        Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListImagesRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[
        Literal["CREATION_TIME", "IMAGE_NAME", "LAST_MODIFIED_TIME"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListInferenceExperimentsRequestModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    type: Optional[Literal["ShadowMode"]] = Field(default=None, alias="Type")
    status_equals: Optional[
        Literal[
            "Cancelled",
            "Completed",
            "Created",
            "Creating",
            "Running",
            "Starting",
            "Stopping",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInferenceRecommendationsJobStepsRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="Status")
    step_type: Optional[Literal["BENCHMARK"]] = Field(default=None, alias="StepType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInferenceRecommendationsJobsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLabelingJobsForWorkteamRequestModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    job_reference_code_contains: Optional[str] = Field(
        default=None, alias="JobReferenceCodeContains"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListLabelingJobsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[
        Literal[
            "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
        ]
    ] = Field(default=None, alias="StatusEquals")


class ListLineageGroupsRequestModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListModelBiasJobDefinitionsRequestModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class ListModelCardExportJobsRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    model_card_export_job_name_contains: Optional[str] = Field(
        default=None, alias="ModelCardExportJobNameContains"
    )
    status_equals: Optional[Literal["Completed", "Failed", "InProgress"]] = Field(
        default=None, alias="StatusEquals"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ModelCardExportJobSummaryModel(BaseModel):
    model_card_export_job_name: str = Field(alias="ModelCardExportJobName")
    model_card_export_job_arn: str = Field(alias="ModelCardExportJobArn")
    status: Literal["Completed", "Failed", "InProgress"] = Field(alias="Status")
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: int = Field(alias="ModelCardVersion")
    created_at: datetime = Field(alias="CreatedAt")
    last_modified_at: datetime = Field(alias="LastModifiedAt")


class ListModelCardVersionsRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["Version"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ModelCardVersionSummaryModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_arn: str = Field(alias="ModelCardArn")
    model_card_status: Literal[
        "Approved", "Archived", "Draft", "PendingReview"
    ] = Field(alias="ModelCardStatus")
    model_card_version: int = Field(alias="ModelCardVersion")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListModelCardsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ModelCardSummaryModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_arn: str = Field(alias="ModelCardArn")
    model_card_status: Literal[
        "Approved", "Archived", "Draft", "PendingReview"
    ] = Field(alias="ModelCardStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListModelExplainabilityJobDefinitionsRequestModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class ModelMetadataSummaryModel(BaseModel):
    domain: str = Field(alias="Domain")
    framework: str = Field(alias="Framework")
    task: str = Field(alias="Task")
    model: str = Field(alias="Model")
    framework_version: str = Field(alias="FrameworkVersion")


class ListModelPackageGroupsInputRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ModelPackageGroupSummaryModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    model_package_group_arn: str = Field(alias="ModelPackageGroupArn")
    creation_time: datetime = Field(alias="CreationTime")
    model_package_group_status: Literal[
        "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="ModelPackageGroupStatus")
    model_package_group_description: Optional[str] = Field(
        default=None, alias="ModelPackageGroupDescription"
    )


class ListModelPackagesInputRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_type: Optional[Literal["Both", "Unversioned", "Versioned"]] = Field(
        default=None, alias="ModelPackageType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ModelPackageSummaryModel(BaseModel):
    model_package_name: str = Field(alias="ModelPackageName")
    model_package_arn: str = Field(alias="ModelPackageArn")
    creation_time: datetime = Field(alias="CreationTime")
    model_package_status: Literal[
        "Completed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="ModelPackageStatus")
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_version: Optional[int] = Field(
        default=None, alias="ModelPackageVersion"
    )
    model_package_description: Optional[str] = Field(
        default=None, alias="ModelPackageDescription"
    )
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")


class ListModelQualityJobDefinitionsRequestModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class ListModelsInputRequestModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class ModelSummaryModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    model_arn: str = Field(alias="ModelArn")
    creation_time: datetime = Field(alias="CreationTime")


class ListMonitoringAlertHistoryRequestModel(BaseModel):
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    monitoring_alert_name: Optional[str] = Field(
        default=None, alias="MonitoringAlertName"
    )
    sort_by: Optional[Literal["CreationTime", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    status_equals: Optional[Literal["InAlert", "OK"]] = Field(
        default=None, alias="StatusEquals"
    )


class MonitoringAlertHistorySummaryModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_alert_name: str = Field(alias="MonitoringAlertName")
    creation_time: datetime = Field(alias="CreationTime")
    alert_status: Literal["InAlert", "OK"] = Field(alias="AlertStatus")


class ListMonitoringAlertsRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMonitoringExecutionsRequestModel(BaseModel):
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "ScheduledTime", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    scheduled_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTimeBefore"
    )
    scheduled_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Completed",
            "CompletedWithViolations",
            "Failed",
            "InProgress",
            "Pending",
            "Stopped",
            "Stopping",
        ]
    ] = Field(default=None, alias="StatusEquals")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type_equals: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringTypeEquals")


class ListMonitoringSchedulesRequestModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal["Failed", "Pending", "Scheduled", "Stopped"]
    ] = Field(default=None, alias="StatusEquals")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type_equals: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringTypeEquals")


class MonitoringScheduleSummaryModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    monitoring_schedule_status: Literal[
        "Failed", "Pending", "Scheduled", "Stopped"
    ] = Field(alias="MonitoringScheduleStatus")
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringType")


class ListNotebookInstanceLifecycleConfigsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )


class NotebookInstanceLifecycleConfigSummaryModel(BaseModel):
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )
    notebook_instance_lifecycle_config_arn: str = Field(
        alias="NotebookInstanceLifecycleConfigArn"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListNotebookInstancesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Stopped",
            "Stopping",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")
    notebook_instance_lifecycle_config_name_contains: Optional[str] = Field(
        default=None, alias="NotebookInstanceLifecycleConfigNameContains"
    )
    default_code_repository_contains: Optional[str] = Field(
        default=None, alias="DefaultCodeRepositoryContains"
    )
    additional_code_repository_equals: Optional[str] = Field(
        default=None, alias="AdditionalCodeRepositoryEquals"
    )


class NotebookInstanceSummaryModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    notebook_instance_arn: str = Field(alias="NotebookInstanceArn")
    notebook_instance_status: Optional[
        Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Stopped",
            "Stopping",
            "Updating",
        ]
    ] = Field(default=None, alias="NotebookInstanceStatus")
    url: Optional[str] = Field(default=None, alias="Url")
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.c5d.18xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.16xlarge",
            "ml.m5d.24xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.8xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.t2.2xlarge",
            "ml.t2.large",
            "ml.t2.medium",
            "ml.t2.xlarge",
            "ml.t3.2xlarge",
            "ml.t3.large",
            "ml.t3.medium",
            "ml.t3.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    notebook_instance_lifecycle_config_name: Optional[str] = Field(
        default=None, alias="NotebookInstanceLifecycleConfigName"
    )
    default_code_repository: Optional[str] = Field(
        default=None, alias="DefaultCodeRepository"
    )
    additional_code_repositories: Optional[List[str]] = Field(
        default=None, alias="AdditionalCodeRepositories"
    )


class ListPipelineExecutionStepsRequestModel(BaseModel):
    pipeline_execution_arn: Optional[str] = Field(
        default=None, alias="PipelineExecutionArn"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListPipelineExecutionsRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "PipelineExecutionArn"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PipelineExecutionSummaryModel(BaseModel):
    pipeline_execution_arn: Optional[str] = Field(
        default=None, alias="PipelineExecutionArn"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    pipeline_execution_status: Optional[
        Literal["Executing", "Failed", "Stopped", "Stopping", "Succeeded"]
    ] = Field(default=None, alias="PipelineExecutionStatus")
    pipeline_execution_description: Optional[str] = Field(
        default=None, alias="PipelineExecutionDescription"
    )
    pipeline_execution_display_name: Optional[str] = Field(
        default=None, alias="PipelineExecutionDisplayName"
    )
    pipeline_execution_failure_reason: Optional[str] = Field(
        default=None, alias="PipelineExecutionFailureReason"
    )


class ListPipelineParametersForExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class ListPipelinesRequestModel(BaseModel):
    pipeline_name_prefix: Optional[str] = Field(
        default=None, alias="PipelineNamePrefix"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PipelineSummaryModel(BaseModel):
    pipeline_arn: Optional[str] = Field(default=None, alias="PipelineArn")
    pipeline_name: Optional[str] = Field(default=None, alias="PipelineName")
    pipeline_display_name: Optional[str] = Field(
        default=None, alias="PipelineDisplayName"
    )
    pipeline_description: Optional[str] = Field(
        default=None, alias="PipelineDescription"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_execution_time: Optional[datetime] = Field(
        default=None, alias="LastExecutionTime"
    )


class ListProcessingJobsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ProcessingJobSummaryModel(BaseModel):
    processing_job_name: str = Field(alias="ProcessingJobName")
    processing_job_arn: str = Field(alias="ProcessingJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    processing_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="ProcessingJobStatus")
    processing_end_time: Optional[datetime] = Field(
        default=None, alias="ProcessingEndTime"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    exit_message: Optional[str] = Field(default=None, alias="ExitMessage")


class ListProjectsInputRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ProjectSummaryModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    project_arn: str = Field(alias="ProjectArn")
    project_id: str = Field(alias="ProjectId")
    creation_time: datetime = Field(alias="CreationTime")
    project_status: Literal[
        "CreateCompleted",
        "CreateFailed",
        "CreateInProgress",
        "DeleteCompleted",
        "DeleteFailed",
        "DeleteInProgress",
        "Pending",
        "UpdateCompleted",
        "UpdateFailed",
        "UpdateInProgress",
    ] = Field(alias="ProjectStatus")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")


class ListSpacesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime"]] = Field(
        default=None, alias="SortBy"
    )
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    space_name_contains: Optional[str] = Field(default=None, alias="SpaceNameContains")


class SpaceDetailsModel(BaseModel):
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    space_name: Optional[str] = Field(default=None, alias="SpaceName")
    status: Optional[
        Literal[
            "Delete_Failed",
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Update_Failed",
            "Updating",
        ]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListStageDevicesRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    exclude_devices_deployed_in_other_stage: Optional[bool] = Field(
        default=None, alias="ExcludeDevicesDeployedInOtherStage"
    )


class ListStudioLifecycleConfigsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    app_type_equals: Optional[Literal["JupyterServer", "KernelGateway"]] = Field(
        default=None, alias="AppTypeEquals"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeBefore"
    )
    modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeAfter"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class StudioLifecycleConfigDetailsModel(BaseModel):
    studio_lifecycle_config_arn: Optional[str] = Field(
        default=None, alias="StudioLifecycleConfigArn"
    )
    studio_lifecycle_config_name: Optional[str] = Field(
        default=None, alias="StudioLifecycleConfigName"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    studio_lifecycle_config_app_type: Optional[
        Literal["JupyterServer", "KernelGateway"]
    ] = Field(default=None, alias="StudioLifecycleConfigAppType")


class ListSubscribedWorkteamsRequestModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTrainingJobsForHyperParameterTuningJobRequestModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[
        Literal["CreationTime", "FinalObjectiveMetricValue", "Name", "Status"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )


class ListTrainingJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    warm_pool_status_equals: Optional[
        Literal["Available", "InUse", "Reused", "Terminated"]
    ] = Field(default=None, alias="WarmPoolStatusEquals")


class ListTransformJobsRequestModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TransformJobSummaryModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")
    transform_job_arn: str = Field(alias="TransformJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    transform_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="TransformJobStatus")
    transform_end_time: Optional[datetime] = Field(
        default=None, alias="TransformEndTime"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class ListTrialComponentsRequestModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTrialsRequestModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_component_name: Optional[str] = Field(
        default=None, alias="TrialComponentName"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListUserProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime"]] = Field(
        default=None, alias="SortBy"
    )
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    user_profile_name_contains: Optional[str] = Field(
        default=None, alias="UserProfileNameContains"
    )


class UserProfileDetailsModel(BaseModel):
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    status: Optional[
        Literal[
            "Delete_Failed",
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Update_Failed",
            "Updating",
        ]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListWorkforcesRequestModel(BaseModel):
    sort_by: Optional[Literal["CreateDate", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListWorkteamsRequestModel(BaseModel):
    sort_by: Optional[Literal["CreateDate", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OidcMemberDefinitionModel(BaseModel):
    groups: Sequence[str] = Field(alias="Groups")


class MonitoringGroundTruthS3InputModel(BaseModel):
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")


class ModelDashboardEndpointModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_arn: str = Field(alias="EndpointArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    endpoint_status: Literal[
        "Creating",
        "Deleting",
        "Failed",
        "InService",
        "OutOfService",
        "RollingBack",
        "SystemUpdating",
        "Updating",
    ] = Field(alias="EndpointStatus")


class ModelDashboardIndicatorActionModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class RealTimeInferenceConfigModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5d.18xlarge",
        "ml.c5d.2xlarge",
        "ml.c5d.4xlarge",
        "ml.c5d.9xlarge",
        "ml.c5d.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.xlarge",
        "ml.m5d.12xlarge",
        "ml.m5d.16xlarge",
        "ml.m5d.24xlarge",
        "ml.m5d.2xlarge",
        "ml.m5d.4xlarge",
        "ml.m5d.8xlarge",
        "ml.m5d.large",
        "ml.m5d.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.r5.12xlarge",
        "ml.r5.16xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.8xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.t2.2xlarge",
        "ml.t2.large",
        "ml.t2.medium",
        "ml.t2.xlarge",
        "ml.t3.2xlarge",
        "ml.t3.large",
        "ml.t3.medium",
        "ml.t3.xlarge",
    ] = Field(alias="InstanceType")
    instance_count: int = Field(alias="InstanceCount")


class ModelInputModel(BaseModel):
    data_input_config: str = Field(alias="DataInputConfig")


class ModelLatencyThresholdModel(BaseModel):
    percentile: Optional[str] = Field(default=None, alias="Percentile")
    value_in_milliseconds: Optional[int] = Field(
        default=None, alias="ValueInMilliseconds"
    )


class ModelMetadataFilterModel(BaseModel):
    name: Literal["Domain", "Framework", "FrameworkVersion", "Task"] = Field(
        alias="Name"
    )
    value: str = Field(alias="Value")


class ModelPackageStatusItemModel(BaseModel):
    name: str = Field(alias="Name")
    status: Literal["Completed", "Failed", "InProgress", "NotStarted"] = Field(
        alias="Status"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class ModelStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class MonitoringAppSpecificationModel(BaseModel):
    image_uri: str = Field(alias="ImageUri")
    container_entrypoint: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerEntrypoint"
    )
    container_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerArguments"
    )
    record_preprocessor_source_uri: Optional[str] = Field(
        default=None, alias="RecordPreprocessorSourceUri"
    )
    post_analytics_processor_source_uri: Optional[str] = Field(
        default=None, alias="PostAnalyticsProcessorSourceUri"
    )


class MonitoringClusterConfigModel(BaseModel):
    instance_count: int = Field(alias="InstanceCount")
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.r5.12xlarge",
        "ml.r5.16xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.8xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.t3.2xlarge",
        "ml.t3.large",
        "ml.t3.medium",
        "ml.t3.xlarge",
    ] = Field(alias="InstanceType")
    volume_size_in_gb: int = Field(alias="VolumeSizeInGB")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")


class MonitoringCsvDatasetFormatModel(BaseModel):
    header: Optional[bool] = Field(default=None, alias="Header")


class MonitoringJsonDatasetFormatModel(BaseModel):
    line: Optional[bool] = Field(default=None, alias="Line")


class MonitoringS3OutputModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    local_path: str = Field(alias="LocalPath")
    s3_upload_mode: Optional[Literal["Continuous", "EndOfJob"]] = Field(
        default=None, alias="S3UploadMode"
    )


class ScheduleConfigModel(BaseModel):
    schedule_expression: str = Field(alias="ScheduleExpression")


class S3StorageConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    resolved_output_s3_uri: Optional[str] = Field(
        default=None, alias="ResolvedOutputS3Uri"
    )


class OidcConfigForResponseModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    issuer: Optional[str] = Field(default=None, alias="Issuer")
    authorization_endpoint: Optional[str] = Field(
        default=None, alias="AuthorizationEndpoint"
    )
    token_endpoint: Optional[str] = Field(default=None, alias="TokenEndpoint")
    user_info_endpoint: Optional[str] = Field(default=None, alias="UserInfoEndpoint")
    logout_endpoint: Optional[str] = Field(default=None, alias="LogoutEndpoint")
    jwks_uri: Optional[str] = Field(default=None, alias="JwksUri")


class OnlineStoreSecurityConfigModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class TargetPlatformModel(BaseModel):
    os: Literal["ANDROID", "LINUX"] = Field(alias="Os")
    arch: Literal["ARM64", "ARM_EABI", "ARM_EABIHF", "X86", "X86_64"] = Field(
        alias="Arch"
    )
    accelerator: Optional[Literal["INTEL_GRAPHICS", "MALI", "NNA", "NVIDIA"]] = Field(
        default=None, alias="Accelerator"
    )


class ParentModel(BaseModel):
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")


class ProductionVariantServerlessConfigModel(BaseModel):
    memory_size_in_mb: int = Field(alias="MemorySizeInMB")
    max_concurrency: int = Field(alias="MaxConcurrency")


class ProductionVariantStatusModel(BaseModel):
    status: Literal[
        "ActivatingTraffic", "Baking", "Creating", "Deleting", "Updating"
    ] = Field(alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")


class PhaseModel(BaseModel):
    initial_number_of_users: Optional[int] = Field(
        default=None, alias="InitialNumberOfUsers"
    )
    spawn_rate: Optional[int] = Field(default=None, alias="SpawnRate")
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class ProcessingJobStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class QualityCheckStepMetadataModel(BaseModel):
    check_type: Optional[str] = Field(default=None, alias="CheckType")
    baseline_used_for_drift_check_statistics: Optional[str] = Field(
        default=None, alias="BaselineUsedForDriftCheckStatistics"
    )
    baseline_used_for_drift_check_constraints: Optional[str] = Field(
        default=None, alias="BaselineUsedForDriftCheckConstraints"
    )
    calculated_baseline_statistics: Optional[str] = Field(
        default=None, alias="CalculatedBaselineStatistics"
    )
    calculated_baseline_constraints: Optional[str] = Field(
        default=None, alias="CalculatedBaselineConstraints"
    )
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    violation_report: Optional[str] = Field(default=None, alias="ViolationReport")
    check_job_arn: Optional[str] = Field(default=None, alias="CheckJobArn")
    skip_check: Optional[bool] = Field(default=None, alias="SkipCheck")
    register_new_baseline: Optional[bool] = Field(
        default=None, alias="RegisterNewBaseline"
    )


class RegisterModelStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class TrainingJobStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class TransformJobStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class TuningJobStepMetaDataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class ProcessingClusterConfigModel(BaseModel):
    instance_count: int = Field(alias="InstanceCount")
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.r5.12xlarge",
        "ml.r5.16xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.8xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.t3.2xlarge",
        "ml.t3.large",
        "ml.t3.medium",
        "ml.t3.xlarge",
    ] = Field(alias="InstanceType")
    volume_size_in_gb: int = Field(alias="VolumeSizeInGB")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")


class ProcessingFeatureStoreOutputModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")


class ProcessingS3InputModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    s3_data_type: Literal["ManifestFile", "S3Prefix"] = Field(alias="S3DataType")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")
    s3_input_mode: Optional[Literal["File", "Pipe"]] = Field(
        default=None, alias="S3InputMode"
    )
    s3_data_distribution_type: Optional[
        Literal["FullyReplicated", "ShardedByS3Key"]
    ] = Field(default=None, alias="S3DataDistributionType")
    s3_compression_type: Optional[Literal["Gzip", "None"]] = Field(
        default=None, alias="S3CompressionType"
    )


class ProcessingS3OutputModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    local_path: str = Field(alias="LocalPath")
    s3_upload_mode: Literal["Continuous", "EndOfJob"] = Field(alias="S3UploadMode")


class ProductionVariantCoreDumpConfigModel(BaseModel):
    destination_s3_uri: str = Field(alias="DestinationS3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ProfilerConfigForUpdateModel(BaseModel):
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")
    profiling_interval_in_milliseconds: Optional[int] = Field(
        default=None, alias="ProfilingIntervalInMilliseconds"
    )
    profiling_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="ProfilingParameters"
    )
    disable_profiler: Optional[bool] = Field(default=None, alias="DisableProfiler")


class PropertyNameQueryModel(BaseModel):
    property_name_hint: str = Field(alias="PropertyNameHint")


class ProvisioningParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class USDModel(BaseModel):
    dollars: Optional[int] = Field(default=None, alias="Dollars")
    cents: Optional[int] = Field(default=None, alias="Cents")
    tenth_fractions_of_acent: Optional[int] = Field(
        default=None, alias="TenthFractionsOfACent"
    )


class PutModelPackageGroupPolicyInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    resource_policy: str = Field(alias="ResourcePolicy")


class QueryFiltersModel(BaseModel):
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")
    lineage_types: Optional[
        Sequence[Literal["Action", "Artifact", "Context", "TrialComponent"]]
    ] = Field(default=None, alias="LineageTypes")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    modified_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedBefore"
    )
    modified_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedAfter"
    )
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")


class VertexModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    type: Optional[str] = Field(default=None, alias="Type")
    lineage_type: Optional[
        Literal["Action", "Artifact", "Context", "TrialComponent"]
    ] = Field(default=None, alias="LineageType")


class RStudioServerProAppSettingsModel(BaseModel):
    access_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AccessStatus"
    )
    user_group: Optional[Literal["R_STUDIO_ADMIN", "R_STUDIO_USER"]] = Field(
        default=None, alias="UserGroup"
    )


class RecommendationJobCompiledOutputConfigModel(BaseModel):
    s3_output_uri: Optional[str] = Field(default=None, alias="S3OutputUri")


class RecommendationJobPayloadConfigModel(BaseModel):
    sample_payload_url: Optional[str] = Field(default=None, alias="SamplePayloadUrl")
    supported_content_types: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedContentTypes"
    )


class RecommendationJobResourceLimitModel(BaseModel):
    max_number_of_tests: Optional[int] = Field(default=None, alias="MaxNumberOfTests")
    max_parallel_of_tests: Optional[int] = Field(
        default=None, alias="MaxParallelOfTests"
    )


class RecommendationJobVpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    subnets: Sequence[str] = Field(alias="Subnets")


class RenderableTaskModel(BaseModel):
    input: str = Field(alias="Input")


class RenderingErrorModel(BaseModel):
    code: str = Field(alias="Code")
    message: str = Field(alias="Message")


class ResourceConfigForUpdateModel(BaseModel):
    keep_alive_period_in_seconds: int = Field(alias="KeepAlivePeriodInSeconds")


class SearchRequestModel(BaseModel):
    resource: Literal[
        "Endpoint",
        "Experiment",
        "ExperimentTrial",
        "ExperimentTrialComponent",
        "FeatureGroup",
        "FeatureMetadata",
        "HyperParameterTuningJob",
        "Model",
        "ModelCard",
        "ModelPackage",
        "ModelPackageGroup",
        "Pipeline",
        "PipelineExecution",
        "Project",
        "TrainingJob",
    ] = Field(alias="Resource")
    search_expression: Optional[SearchExpressionModel] = Field(
        default=None, alias="SearchExpression"
    )
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SendPipelineExecutionStepFailureRequestModel(BaseModel):
    callback_token: str = Field(alias="CallbackToken")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ShadowModelVariantConfigModel(BaseModel):
    shadow_model_variant_name: str = Field(alias="ShadowModelVariantName")
    sampling_percentage: int = Field(alias="SamplingPercentage")


class SharingSettingsModel(BaseModel):
    notebook_output_option: Optional[Literal["Allowed", "Disabled"]] = Field(
        default=None, alias="NotebookOutputOption"
    )
    s3_output_path: Optional[str] = Field(default=None, alias="S3OutputPath")
    s3_kms_key_id: Optional[str] = Field(default=None, alias="S3KmsKeyId")


class SourceAlgorithmModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")
    model_data_url: Optional[str] = Field(default=None, alias="ModelDataUrl")


class StartEdgeDeploymentStageRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")


class StartInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")


class StartNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")


class StopAutoMLJobRequestModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")


class StopCompilationJobRequestModel(BaseModel):
    compilation_job_name: str = Field(alias="CompilationJobName")


class StopEdgeDeploymentStageRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")


class StopEdgePackagingJobRequestModel(BaseModel):
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")


class StopHyperParameterTuningJobRequestModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")


class StopInferenceRecommendationsJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")


class StopLabelingJobRequestModel(BaseModel):
    labeling_job_name: str = Field(alias="LabelingJobName")


class StopMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")


class StopNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")


class StopPipelineExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    client_request_token: str = Field(alias="ClientRequestToken")


class StopProcessingJobRequestModel(BaseModel):
    processing_job_name: str = Field(alias="ProcessingJobName")


class StopTrainingJobRequestModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")


class StopTransformJobRequestModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")


class TrainingRepositoryAuthConfigModel(BaseModel):
    training_repository_credentials_provider_arn: str = Field(
        alias="TrainingRepositoryCredentialsProviderArn"
    )


class TransformS3DataSourceModel(BaseModel):
    s3_data_type: Literal["AugmentedManifestFile", "ManifestFile", "S3Prefix"] = Field(
        alias="S3DataType"
    )
    s3_uri: str = Field(alias="S3Uri")


class UpdateActionRequestModel(BaseModel):
    action_name: str = Field(alias="ActionName")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
    ] = Field(default=None, alias="Status")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    properties_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="PropertiesToRemove"
    )


class UpdateArtifactRequestModel(BaseModel):
    artifact_arn: str = Field(alias="ArtifactArn")
    artifact_name: Optional[str] = Field(default=None, alias="ArtifactName")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    properties_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="PropertiesToRemove"
    )


class UpdateContextRequestModel(BaseModel):
    context_name: str = Field(alias="ContextName")
    description: Optional[str] = Field(default=None, alias="Description")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    properties_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="PropertiesToRemove"
    )


class VariantPropertyModel(BaseModel):
    variant_property_type: Literal[
        "DataCaptureConfig", "DesiredInstanceCount", "DesiredWeight"
    ] = Field(alias="VariantPropertyType")


class UpdateExperimentRequestModel(BaseModel):
    experiment_name: str = Field(alias="ExperimentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateHubRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_description: Optional[str] = Field(default=None, alias="HubDescription")
    hub_display_name: Optional[str] = Field(default=None, alias="HubDisplayName")
    hub_search_keywords: Optional[Sequence[str]] = Field(
        default=None, alias="HubSearchKeywords"
    )


class UpdateImageRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    delete_properties: Optional[Sequence[str]] = Field(
        default=None, alias="DeleteProperties"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class UpdateImageVersionRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    alias: Optional[str] = Field(default=None, alias="Alias")
    version: Optional[int] = Field(default=None, alias="Version")
    aliases_to_add: Optional[Sequence[str]] = Field(default=None, alias="AliasesToAdd")
    aliases_to_delete: Optional[Sequence[str]] = Field(
        default=None, alias="AliasesToDelete"
    )
    vendor_guidance: Optional[
        Literal["ARCHIVED", "NOT_PROVIDED", "STABLE", "TO_BE_ARCHIVED"]
    ] = Field(default=None, alias="VendorGuidance")
    job_type: Optional[Literal["INFERENCE", "NOTEBOOK_KERNEL", "TRAINING"]] = Field(
        default=None, alias="JobType"
    )
    ml_framework: Optional[str] = Field(default=None, alias="MLFramework")
    programming_lang: Optional[str] = Field(default=None, alias="ProgrammingLang")
    processor: Optional[Literal["CPU", "GPU"]] = Field(default=None, alias="Processor")
    horovod: Optional[bool] = Field(default=None, alias="Horovod")
    release_notes: Optional[str] = Field(default=None, alias="ReleaseNotes")


class UpdateModelCardRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    content: Optional[str] = Field(default=None, alias="Content")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")


class UpdateMonitoringAlertRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_alert_name: str = Field(alias="MonitoringAlertName")
    datapoints_to_alert: int = Field(alias="DatapointsToAlert")
    evaluation_period: int = Field(alias="EvaluationPeriod")


class UpdateTrialRequestModel(BaseModel):
    trial_name: str = Field(alias="TrialName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class WorkforceVpcConfigResponseModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnets: List[str] = Field(alias="Subnets")
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")


class ActionSummaryModel(BaseModel):
    action_arn: Optional[str] = Field(default=None, alias="ActionArn")
    action_name: Optional[str] = Field(default=None, alias="ActionName")
    source: Optional[ActionSourceModel] = Field(default=None, alias="Source")
    action_type: Optional[str] = Field(default=None, alias="ActionType")
    status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class AddAssociationResponseModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    destination_arn: str = Field(alias="DestinationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateTrialComponentResponseModel(BaseModel):
    trial_component_arn: str = Field(alias="TrialComponentArn")
    trial_arn: str = Field(alias="TrialArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateActionResponseModel(BaseModel):
    action_arn: str = Field(alias="ActionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAlgorithmOutputModel(BaseModel):
    algorithm_arn: str = Field(alias="AlgorithmArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppImageConfigResponseModel(BaseModel):
    app_image_config_arn: str = Field(alias="AppImageConfigArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppResponseModel(BaseModel):
    app_arn: str = Field(alias="AppArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateArtifactResponseModel(BaseModel):
    artifact_arn: str = Field(alias="ArtifactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAutoMLJobResponseModel(BaseModel):
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCodeRepositoryOutputModel(BaseModel):
    code_repository_arn: str = Field(alias="CodeRepositoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCompilationJobResponseModel(BaseModel):
    compilation_job_arn: str = Field(alias="CompilationJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContextResponseModel(BaseModel):
    context_arn: str = Field(alias="ContextArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataQualityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainResponseModel(BaseModel):
    domain_arn: str = Field(alias="DomainArn")
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEdgeDeploymentPlanResponseModel(BaseModel):
    edge_deployment_plan_arn: str = Field(alias="EdgeDeploymentPlanArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointConfigOutputModel(BaseModel):
    endpoint_config_arn: str = Field(alias="EndpointConfigArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointOutputModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentResponseModel(BaseModel):
    experiment_arn: str = Field(alias="ExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFeatureGroupResponseModel(BaseModel):
    feature_group_arn: str = Field(alias="FeatureGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFlowDefinitionResponseModel(BaseModel):
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHubResponseModel(BaseModel):
    hub_arn: str = Field(alias="HubArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHumanTaskUiResponseModel(BaseModel):
    human_task_ui_arn: str = Field(alias="HumanTaskUiArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHyperParameterTuningJobResponseModel(BaseModel):
    hyper_parameter_tuning_job_arn: str = Field(alias="HyperParameterTuningJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageResponseModel(BaseModel):
    image_arn: str = Field(alias="ImageArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageVersionResponseModel(BaseModel):
    image_version_arn: str = Field(alias="ImageVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInferenceExperimentResponseModel(BaseModel):
    inference_experiment_arn: str = Field(alias="InferenceExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInferenceRecommendationsJobResponseModel(BaseModel):
    job_arn: str = Field(alias="JobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLabelingJobResponseModel(BaseModel):
    labeling_job_arn: str = Field(alias="LabelingJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelBiasJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelCardExportJobResponseModel(BaseModel):
    model_card_export_job_arn: str = Field(alias="ModelCardExportJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelCardResponseModel(BaseModel):
    model_card_arn: str = Field(alias="ModelCardArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelExplainabilityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelOutputModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelPackageGroupOutputModel(BaseModel):
    model_package_group_arn: str = Field(alias="ModelPackageGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelPackageOutputModel(BaseModel):
    model_package_arn: str = Field(alias="ModelPackageArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelQualityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMonitoringScheduleResponseModel(BaseModel):
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNotebookInstanceLifecycleConfigOutputModel(BaseModel):
    notebook_instance_lifecycle_config_arn: str = Field(
        alias="NotebookInstanceLifecycleConfigArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNotebookInstanceOutputModel(BaseModel):
    notebook_instance_arn: str = Field(alias="NotebookInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePipelineResponseModel(BaseModel):
    pipeline_arn: str = Field(alias="PipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePresignedDomainUrlResponseModel(BaseModel):
    authorized_url: str = Field(alias="AuthorizedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePresignedNotebookInstanceUrlOutputModel(BaseModel):
    authorized_url: str = Field(alias="AuthorizedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProcessingJobResponseModel(BaseModel):
    processing_job_arn: str = Field(alias="ProcessingJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectOutputModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    project_id: str = Field(alias="ProjectId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSpaceResponseModel(BaseModel):
    space_arn: str = Field(alias="SpaceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStudioLifecycleConfigResponseModel(BaseModel):
    studio_lifecycle_config_arn: str = Field(alias="StudioLifecycleConfigArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrainingJobResponseModel(BaseModel):
    training_job_arn: str = Field(alias="TrainingJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTransformJobResponseModel(BaseModel):
    transform_job_arn: str = Field(alias="TransformJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrialComponentResponseModel(BaseModel):
    trial_component_arn: str = Field(alias="TrialComponentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrialResponseModel(BaseModel):
    trial_arn: str = Field(alias="TrialArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserProfileResponseModel(BaseModel):
    user_profile_arn: str = Field(alias="UserProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkforceResponseModel(BaseModel):
    workforce_arn: str = Field(alias="WorkforceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkteamResponseModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteActionResponseModel(BaseModel):
    action_arn: str = Field(alias="ActionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteArtifactResponseModel(BaseModel):
    artifact_arn: str = Field(alias="ArtifactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAssociationResponseModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    destination_arn: str = Field(alias="DestinationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteContextResponseModel(BaseModel):
    context_arn: str = Field(alias="ContextArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteExperimentResponseModel(BaseModel):
    experiment_arn: str = Field(alias="ExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInferenceExperimentResponseModel(BaseModel):
    inference_experiment_arn: str = Field(alias="InferenceExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePipelineResponseModel(BaseModel):
    pipeline_arn: str = Field(alias="PipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTrialComponentResponseModel(BaseModel):
    trial_component_arn: str = Field(alias="TrialComponentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTrialResponseModel(BaseModel):
    trial_arn: str = Field(alias="TrialArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWorkteamResponseModel(BaseModel):
    success: bool = Field(alias="Success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageResponseModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    display_name: str = Field(alias="DisplayName")
    failure_reason: str = Field(alias="FailureReason")
    image_arn: str = Field(alias="ImageArn")
    image_name: str = Field(alias="ImageName")
    image_status: Literal[
        "CREATED",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="ImageStatus")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    role_arn: str = Field(alias="RoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageVersionResponseModel(BaseModel):
    base_image: str = Field(alias="BaseImage")
    container_image: str = Field(alias="ContainerImage")
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: str = Field(alias="FailureReason")
    image_arn: str = Field(alias="ImageArn")
    image_version_arn: str = Field(alias="ImageVersionArn")
    image_version_status: Literal[
        "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
    ] = Field(alias="ImageVersionStatus")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    version: int = Field(alias="Version")
    vendor_guidance: Literal[
        "ARCHIVED", "NOT_PROVIDED", "STABLE", "TO_BE_ARCHIVED"
    ] = Field(alias="VendorGuidance")
    job_type: Literal["INFERENCE", "NOTEBOOK_KERNEL", "TRAINING"] = Field(
        alias="JobType"
    )
    ml_framework: str = Field(alias="MLFramework")
    programming_lang: str = Field(alias="ProgrammingLang")
    processor: Literal["CPU", "GPU"] = Field(alias="Processor")
    horovod: bool = Field(alias="Horovod")
    release_notes: str = Field(alias="ReleaseNotes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePipelineDefinitionForExecutionResponseModel(BaseModel):
    pipeline_definition: str = Field(alias="PipelineDefinition")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStudioLifecycleConfigResponseModel(BaseModel):
    studio_lifecycle_config_arn: str = Field(alias="StudioLifecycleConfigArn")
    studio_lifecycle_config_name: str = Field(alias="StudioLifecycleConfigName")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    studio_lifecycle_config_content: str = Field(alias="StudioLifecycleConfigContent")
    studio_lifecycle_config_app_type: Literal["JupyterServer", "KernelGateway"] = Field(
        alias="StudioLifecycleConfigAppType"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateTrialComponentResponseModel(BaseModel):
    trial_component_arn: str = Field(alias="TrialComponentArn")
    trial_arn: str = Field(alias="TrialArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLineageGroupPolicyResponseModel(BaseModel):
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    resource_policy: str = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelPackageGroupPolicyOutputModel(BaseModel):
    resource_policy: str = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSagemakerServicecatalogPortfolioStatusOutputModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportHubContentResponseModel(BaseModel):
    hub_arn: str = Field(alias="HubArn")
    hub_content_arn: str = Field(alias="HubContentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesResponseModel(BaseModel):
    sage_maker_image_version_aliases: List[str] = Field(
        alias="SageMakerImageVersionAliases"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutModelPackageGroupPolicyOutputModel(BaseModel):
    model_package_group_arn: str = Field(alias="ModelPackageGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetryPipelineExecutionResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendPipelineExecutionStepFailureResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendPipelineExecutionStepSuccessResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartInferenceExperimentResponseModel(BaseModel):
    inference_experiment_arn: str = Field(alias="InferenceExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPipelineExecutionResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopInferenceExperimentResponseModel(BaseModel):
    inference_experiment_arn: str = Field(alias="InferenceExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopPipelineExecutionResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateActionResponseModel(BaseModel):
    action_arn: str = Field(alias="ActionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppImageConfigResponseModel(BaseModel):
    app_image_config_arn: str = Field(alias="AppImageConfigArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateArtifactResponseModel(BaseModel):
    artifact_arn: str = Field(alias="ArtifactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCodeRepositoryOutputModel(BaseModel):
    code_repository_arn: str = Field(alias="CodeRepositoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContextResponseModel(BaseModel):
    context_arn: str = Field(alias="ContextArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainResponseModel(BaseModel):
    domain_arn: str = Field(alias="DomainArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointOutputModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointWeightsAndCapacitiesOutputModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateExperimentResponseModel(BaseModel):
    experiment_arn: str = Field(alias="ExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFeatureGroupResponseModel(BaseModel):
    feature_group_arn: str = Field(alias="FeatureGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHubResponseModel(BaseModel):
    hub_arn: str = Field(alias="HubArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateImageResponseModel(BaseModel):
    image_arn: str = Field(alias="ImageArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateImageVersionResponseModel(BaseModel):
    image_version_arn: str = Field(alias="ImageVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInferenceExperimentResponseModel(BaseModel):
    inference_experiment_arn: str = Field(alias="InferenceExperimentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelCardResponseModel(BaseModel):
    model_card_arn: str = Field(alias="ModelCardArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelPackageOutputModel(BaseModel):
    model_package_arn: str = Field(alias="ModelPackageArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMonitoringAlertResponseModel(BaseModel):
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    monitoring_alert_name: str = Field(alias="MonitoringAlertName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMonitoringScheduleResponseModel(BaseModel):
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineExecutionResponseModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipelineResponseModel(BaseModel):
    pipeline_arn: str = Field(alias="PipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectOutputModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSpaceResponseModel(BaseModel):
    space_arn: str = Field(alias="SpaceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrainingJobResponseModel(BaseModel):
    training_job_arn: str = Field(alias="TrainingJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrialComponentResponseModel(BaseModel):
    trial_component_arn: str = Field(alias="TrialComponentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrialResponseModel(BaseModel):
    trial_arn: str = Field(alias="TrialArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserProfileResponseModel(BaseModel):
    user_profile_arn: str = Field(alias="UserProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class AddTagsOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperimentRequestModel(BaseModel):
    experiment_name: str = Field(alias="ExperimentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateImageRequestModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    role_arn: str = Field(alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateModelPackageGroupInputRequestModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    model_package_group_description: Optional[str] = Field(
        default=None, alias="ModelPackageGroupDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateStudioLifecycleConfigRequestModel(BaseModel):
    studio_lifecycle_config_name: str = Field(alias="StudioLifecycleConfigName")
    studio_lifecycle_config_content: str = Field(alias="StudioLifecycleConfigContent")
    studio_lifecycle_config_app_type: Literal["JupyterServer", "KernelGateway"] = Field(
        alias="StudioLifecycleConfigAppType"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ImportHubContentRequestModel(BaseModel):
    hub_content_name: str = Field(alias="HubContentName")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    document_schema_version: str = Field(alias="DocumentSchemaVersion")
    hub_name: str = Field(alias="HubName")
    hub_content_document: str = Field(alias="HubContentDocument")
    hub_content_version: Optional[str] = Field(default=None, alias="HubContentVersion")
    hub_content_display_name: Optional[str] = Field(
        default=None, alias="HubContentDisplayName"
    )
    hub_content_description: Optional[str] = Field(
        default=None, alias="HubContentDescription"
    )
    hub_content_markdown: Optional[str] = Field(
        default=None, alias="HubContentMarkdown"
    )
    hub_content_search_keywords: Optional[Sequence[str]] = Field(
        default=None, alias="HubContentSearchKeywords"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoRollbackConfigModel(BaseModel):
    alarms: Optional[Sequence[AlarmModel]] = Field(default=None, alias="Alarms")


class HyperParameterAlgorithmSpecificationModel(BaseModel):
    training_input_mode: Literal["FastFile", "File", "Pipe"] = Field(
        alias="TrainingInputMode"
    )
    training_image: Optional[str] = Field(default=None, alias="TrainingImage")
    algorithm_name: Optional[str] = Field(default=None, alias="AlgorithmName")
    metric_definitions: Optional[Sequence[MetricDefinitionModel]] = Field(
        default=None, alias="MetricDefinitions"
    )


class AlgorithmStatusDetailsModel(BaseModel):
    validation_statuses: Optional[List[AlgorithmStatusItemModel]] = Field(
        default=None, alias="ValidationStatuses"
    )
    image_scan_statuses: Optional[List[AlgorithmStatusItemModel]] = Field(
        default=None, alias="ImageScanStatuses"
    )


class ListAlgorithmsOutputModel(BaseModel):
    algorithm_summary_list: List[AlgorithmSummaryModel] = Field(
        alias="AlgorithmSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppsResponseModel(BaseModel):
    apps: List[AppDetailsModel] = Field(alias="Apps")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ArtifactSourceModel(BaseModel):
    source_uri: str = Field(alias="SourceUri")
    source_types: Optional[Sequence[ArtifactSourceTypeModel]] = Field(
        default=None, alias="SourceTypes"
    )


class AssociationSummaryModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    destination_type: Optional[str] = Field(default=None, alias="DestinationType")
    association_type: Optional[
        Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
    ] = Field(default=None, alias="AssociationType")
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    destination_name: Optional[str] = Field(default=None, alias="DestinationName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")


class DescribeLineageGroupResponseModel(BaseModel):
    lineage_group_name: str = Field(alias="LineageGroupName")
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    display_name: str = Field(alias="DisplayName")
    description: str = Field(alias="Description")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeModelPackageGroupOutputModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    model_package_group_arn: str = Field(alias="ModelPackageGroupArn")
    model_package_group_description: str = Field(alias="ModelPackageGroupDescription")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    model_package_group_status: Literal[
        "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="ModelPackageGroupStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelPackageGroupModel(BaseModel):
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_group_arn: Optional[str] = Field(
        default=None, alias="ModelPackageGroupArn"
    )
    model_package_group_description: Optional[str] = Field(
        default=None, alias="ModelPackageGroupDescription"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    model_package_group_status: Optional[
        Literal[
            "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
        ]
    ] = Field(default=None, alias="ModelPackageGroupStatus")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class AsyncInferenceOutputConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    notification_config: Optional[AsyncInferenceNotificationConfigModel] = Field(
        default=None, alias="NotificationConfig"
    )


class AutoMLCandidateGenerationConfigModel(BaseModel):
    feature_specification_s3_uri: Optional[str] = Field(
        default=None, alias="FeatureSpecificationS3Uri"
    )
    algorithms_config: Optional[Sequence[AutoMLAlgorithmConfigModel]] = Field(
        default=None, alias="AlgorithmsConfig"
    )


class AutoMLDataSourceModel(BaseModel):
    s3_data_source: AutoMLS3DataSourceModel = Field(alias="S3DataSource")


class ResolvedAttributesModel(BaseModel):
    auto_ml_job_objective: Optional[AutoMLJobObjectiveModel] = Field(
        default=None, alias="AutoMLJobObjective"
    )
    problem_type: Optional[
        Literal["BinaryClassification", "MulticlassClassification", "Regression"]
    ] = Field(default=None, alias="ProblemType")
    completion_criteria: Optional[AutoMLJobCompletionCriteriaModel] = Field(
        default=None, alias="CompletionCriteria"
    )


class AutoMLJobSummaryModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    auto_ml_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="AutoMLJobStatus")
    auto_ml_job_secondary_status: Literal[
        "AnalyzingData",
        "CandidateDefinitionsGenerated",
        "Completed",
        "DeployingModel",
        "ExplainabilityError",
        "Failed",
        "FeatureEngineering",
        "GeneratingExplainabilityReport",
        "GeneratingModelInsightsReport",
        "MaxAutoMLJobRuntimeReached",
        "MaxCandidatesReached",
        "ModelDeploymentError",
        "ModelInsightsError",
        "ModelTuning",
        "Starting",
        "Stopped",
        "Stopping",
    ] = Field(alias="AutoMLJobSecondaryStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    partial_failure_reasons: Optional[List[AutoMLPartialFailureReasonModel]] = Field(
        default=None, alias="PartialFailureReasons"
    )


class AutoMLSecurityConfigModel(BaseModel):
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class LabelingJobResourceConfigModel(BaseModel):
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class MonitoringNetworkConfigModel(BaseModel):
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class NetworkConfigModel(BaseModel):
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class BiasModel(BaseModel):
    report: Optional[MetricsSourceModel] = Field(default=None, alias="Report")
    pre_training_report: Optional[MetricsSourceModel] = Field(
        default=None, alias="PreTrainingReport"
    )
    post_training_report: Optional[MetricsSourceModel] = Field(
        default=None, alias="PostTrainingReport"
    )


class DriftCheckModelDataQualityModel(BaseModel):
    statistics: Optional[MetricsSourceModel] = Field(default=None, alias="Statistics")
    constraints: Optional[MetricsSourceModel] = Field(default=None, alias="Constraints")


class DriftCheckModelQualityModel(BaseModel):
    statistics: Optional[MetricsSourceModel] = Field(default=None, alias="Statistics")
    constraints: Optional[MetricsSourceModel] = Field(default=None, alias="Constraints")


class ExplainabilityModel(BaseModel):
    report: Optional[MetricsSourceModel] = Field(default=None, alias="Report")


class ModelDataQualityModel(BaseModel):
    statistics: Optional[MetricsSourceModel] = Field(default=None, alias="Statistics")
    constraints: Optional[MetricsSourceModel] = Field(default=None, alias="Constraints")


class ModelQualityModel(BaseModel):
    statistics: Optional[MetricsSourceModel] = Field(default=None, alias="Statistics")
    constraints: Optional[MetricsSourceModel] = Field(default=None, alias="Constraints")


class CallbackStepMetadataModel(BaseModel):
    callback_token: Optional[str] = Field(default=None, alias="CallbackToken")
    sqs_queue_url: Optional[str] = Field(default=None, alias="SqsQueueUrl")
    output_parameters: Optional[List[OutputParameterModel]] = Field(
        default=None, alias="OutputParameters"
    )


class LambdaStepMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    output_parameters: Optional[List[OutputParameterModel]] = Field(
        default=None, alias="OutputParameters"
    )


class SendPipelineExecutionStepSuccessRequestModel(BaseModel):
    callback_token: str = Field(alias="CallbackToken")
    output_parameters: Optional[Sequence[OutputParameterModel]] = Field(
        default=None, alias="OutputParameters"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class CandidatePropertiesModel(BaseModel):
    candidate_artifact_locations: Optional[CandidateArtifactLocationsModel] = Field(
        default=None, alias="CandidateArtifactLocations"
    )
    candidate_metrics: Optional[List[MetricDatumModel]] = Field(
        default=None, alias="CandidateMetrics"
    )


class CanvasAppSettingsModel(BaseModel):
    time_series_forecasting_settings: Optional[
        TimeSeriesForecastingSettingsModel
    ] = Field(default=None, alias="TimeSeriesForecastingSettings")


class TrafficRoutingConfigModel(BaseModel):
    type: Literal["ALL_AT_ONCE", "CANARY", "LINEAR"] = Field(alias="Type")
    wait_interval_in_seconds: int = Field(alias="WaitIntervalInSeconds")
    canary_size: Optional[CapacitySizeModel] = Field(default=None, alias="CanarySize")
    linear_step_size: Optional[CapacitySizeModel] = Field(
        default=None, alias="LinearStepSize"
    )


class InferenceExperimentDataStorageConfigModel(BaseModel):
    destination: str = Field(alias="Destination")
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")
    content_type: Optional[CaptureContentTypeHeaderModel] = Field(
        default=None, alias="ContentType"
    )


class DataCaptureConfigModel(BaseModel):
    initial_sampling_percentage: int = Field(alias="InitialSamplingPercentage")
    destination_s3_uri: str = Field(alias="DestinationS3Uri")
    capture_options: Sequence[CaptureOptionModel] = Field(alias="CaptureOptions")
    enable_capture: Optional[bool] = Field(default=None, alias="EnableCapture")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    capture_content_type_header: Optional[CaptureContentTypeHeaderModel] = Field(
        default=None, alias="CaptureContentTypeHeader"
    )


class EnvironmentParameterRangesModel(BaseModel):
    categorical_parameter_ranges: Optional[Sequence[CategoricalParameterModel]] = Field(
        default=None, alias="CategoricalParameterRanges"
    )


class ClarifyShapConfigModel(BaseModel):
    shap_baseline_config: ClarifyShapBaselineConfigModel = Field(
        alias="ShapBaselineConfig"
    )
    number_of_samples: Optional[int] = Field(default=None, alias="NumberOfSamples")
    use_logit: Optional[bool] = Field(default=None, alias="UseLogit")
    seed: Optional[int] = Field(default=None, alias="Seed")
    text_config: Optional[ClarifyTextConfigModel] = Field(
        default=None, alias="TextConfig"
    )


class CodeRepositorySummaryModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")
    code_repository_arn: str = Field(alias="CodeRepositoryArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    git_config: Optional[GitConfigModel] = Field(default=None, alias="GitConfig")


class CreateCodeRepositoryInputRequestModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")
    git_config: GitConfigModel = Field(alias="GitConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeCodeRepositoryOutputModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")
    code_repository_arn: str = Field(alias="CodeRepositoryArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    git_config: GitConfigModel = Field(alias="GitConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DebugHookConfigModel(BaseModel):
    s3_output_path: str = Field(alias="S3OutputPath")
    local_path: Optional[str] = Field(default=None, alias="LocalPath")
    hook_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="HookParameters"
    )
    collection_configurations: Optional[Sequence[CollectionConfigurationModel]] = Field(
        default=None, alias="CollectionConfigurations"
    )


class ListCompilationJobsResponseModel(BaseModel):
    compilation_job_summaries: List[CompilationJobSummaryModel] = Field(
        alias="CompilationJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContextSummaryModel(BaseModel):
    context_arn: Optional[str] = Field(default=None, alias="ContextArn")
    context_name: Optional[str] = Field(default=None, alias="ContextName")
    source: Optional[ContextSourceModel] = Field(default=None, alias="Source")
    context_type: Optional[str] = Field(default=None, alias="ContextType")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class CreateContextRequestModel(BaseModel):
    context_name: str = Field(alias="ContextName")
    source: ContextSourceModel = Field(alias="Source")
    context_type: str = Field(alias="ContextType")
    description: Optional[str] = Field(default=None, alias="Description")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeContextResponseModel(BaseModel):
    context_name: str = Field(alias="ContextName")
    context_arn: str = Field(alias="ContextArn")
    source: ContextSourceModel = Field(alias="Source")
    context_type: str = Field(alias="ContextType")
    description: str = Field(alias="Description")
    properties: Dict[str, str] = Field(alias="Properties")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TuningJobCompletionCriteriaModel(BaseModel):
    target_objective_metric_value: Optional[float] = Field(
        default=None, alias="TargetObjectiveMetricValue"
    )
    best_objective_not_improving: Optional[BestObjectiveNotImprovingModel] = Field(
        default=None, alias="BestObjectiveNotImproving"
    )
    convergence_detected: Optional[ConvergenceDetectedModel] = Field(
        default=None, alias="ConvergenceDetected"
    )


class CreateActionRequestModel(BaseModel):
    action_name: str = Field(alias="ActionName")
    source: ActionSourceModel = Field(alias="Source")
    action_type: str = Field(alias="ActionType")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
    ] = Field(default=None, alias="Status")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTrialRequestModel(BaseModel):
    trial_name: str = Field(alias="TrialName")
    experiment_name: str = Field(alias="ExperimentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeActionResponseModel(BaseModel):
    action_name: str = Field(alias="ActionName")
    action_arn: str = Field(alias="ActionArn")
    source: ActionSourceModel = Field(alias="Source")
    action_type: str = Field(alias="ActionType")
    description: str = Field(alias="Description")
    status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"
    ] = Field(alias="Status")
    properties: Dict[str, str] = Field(alias="Properties")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    metadata_properties: MetadataPropertiesModel = Field(alias="MetadataProperties")
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    app_type: Literal[
        "JupyterServer",
        "KernelGateway",
        "RSessionGateway",
        "RStudioServerPro",
        "TensorBoard",
    ] = Field(alias="AppType")
    app_name: str = Field(alias="AppName")
    user_profile_name: Optional[str] = Field(default=None, alias="UserProfileName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="ResourceSpec"
    )
    space_name: Optional[str] = Field(default=None, alias="SpaceName")


class DescribeAppResponseModel(BaseModel):
    app_arn: str = Field(alias="AppArn")
    app_type: Literal[
        "JupyterServer",
        "KernelGateway",
        "RSessionGateway",
        "RStudioServerPro",
        "TensorBoard",
    ] = Field(alias="AppType")
    app_name: str = Field(alias="AppName")
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")
    status: Literal["Deleted", "Deleting", "Failed", "InService", "Pending"] = Field(
        alias="Status"
    )
    last_health_check_timestamp: datetime = Field(alias="LastHealthCheckTimestamp")
    last_user_activity_timestamp: datetime = Field(alias="LastUserActivityTimestamp")
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: str = Field(alias="FailureReason")
    resource_spec: ResourceSpecModel = Field(alias="ResourceSpec")
    space_name: str = Field(alias="SpaceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JupyterServerAppSettingsModel(BaseModel):
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )
    lifecycle_config_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LifecycleConfigArns"
    )
    code_repositories: Optional[Sequence[CodeRepositoryModel]] = Field(
        default=None, alias="CodeRepositories"
    )


class RStudioServerProDomainSettingsForUpdateModel(BaseModel):
    domain_execution_role_arn: str = Field(alias="DomainExecutionRoleArn")
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )
    rstudio_connect_url: Optional[str] = Field(default=None, alias="RStudioConnectUrl")
    rstudio_package_manager_url: Optional[str] = Field(
        default=None, alias="RStudioPackageManagerUrl"
    )


class RStudioServerProDomainSettingsModel(BaseModel):
    domain_execution_role_arn: str = Field(alias="DomainExecutionRoleArn")
    rstudio_connect_url: Optional[str] = Field(default=None, alias="RStudioConnectUrl")
    rstudio_package_manager_url: Optional[str] = Field(
        default=None, alias="RStudioPackageManagerUrl"
    )
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )


class TensorBoardAppSettingsModel(BaseModel):
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )


class CreateDeviceFleetRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    enable_iot_role_alias: Optional[bool] = Field(
        default=None, alias="EnableIotRoleAlias"
    )


class CreateEdgePackagingJobRequestModel(BaseModel):
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")
    compilation_job_name: str = Field(alias="CompilationJobName")
    model_name: str = Field(alias="ModelName")
    model_version: str = Field(alias="ModelVersion")
    role_arn: str = Field(alias="RoleArn")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    resource_key: Optional[str] = Field(default=None, alias="ResourceKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeDeviceFleetResponseModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    device_fleet_arn: str = Field(alias="DeviceFleetArn")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    description: str = Field(alias="Description")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    role_arn: str = Field(alias="RoleArn")
    iot_role_alias: str = Field(alias="IotRoleAlias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeviceFleetRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    enable_iot_role_alias: Optional[bool] = Field(
        default=None, alias="EnableIotRoleAlias"
    )


class UpdateFeatureGroupRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    feature_additions: Optional[Sequence[FeatureDefinitionModel]] = Field(
        default=None, alias="FeatureAdditions"
    )


class CreateHubRequestModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_description: str = Field(alias="HubDescription")
    hub_display_name: Optional[str] = Field(default=None, alias="HubDisplayName")
    hub_search_keywords: Optional[Sequence[str]] = Field(
        default=None, alias="HubSearchKeywords"
    )
    s3_storage_config: Optional[HubS3StorageConfigModel] = Field(
        default=None, alias="S3StorageConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeHubResponseModel(BaseModel):
    hub_name: str = Field(alias="HubName")
    hub_arn: str = Field(alias="HubArn")
    hub_display_name: str = Field(alias="HubDisplayName")
    hub_description: str = Field(alias="HubDescription")
    hub_search_keywords: List[str] = Field(alias="HubSearchKeywords")
    s3_storage_config: HubS3StorageConfigModel = Field(alias="S3StorageConfig")
    hub_status: Literal[
        "CreateFailed",
        "Creating",
        "DeleteFailed",
        "Deleting",
        "InService",
        "UpdateFailed",
        "Updating",
    ] = Field(alias="HubStatus")
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHumanTaskUiRequestModel(BaseModel):
    human_task_ui_name: str = Field(alias="HumanTaskUiName")
    ui_template: UiTemplateModel = Field(alias="UiTemplate")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class InferenceExperimentSummaryModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["ShadowMode"] = Field(alias="Type")
    status: Literal[
        "Cancelled",
        "Completed",
        "Created",
        "Creating",
        "Running",
        "Starting",
        "Stopping",
        "Updating",
    ] = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    schedule: Optional[InferenceExperimentScheduleModel] = Field(
        default=None, alias="Schedule"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    description: Optional[str] = Field(default=None, alias="Description")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class CreateModelCardExportJobRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_export_job_name: str = Field(alias="ModelCardExportJobName")
    output_config: ModelCardExportOutputConfigModel = Field(alias="OutputConfig")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")


class CreateModelCardRequestModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    content: str = Field(alias="Content")
    model_card_status: Literal[
        "Approved", "Archived", "Draft", "PendingReview"
    ] = Field(alias="ModelCardStatus")
    security_config: Optional[ModelCardSecurityConfigModel] = Field(
        default=None, alias="SecurityConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeModelCardResponseModel(BaseModel):
    model_card_arn: str = Field(alias="ModelCardArn")
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: int = Field(alias="ModelCardVersion")
    content: str = Field(alias="Content")
    model_card_status: Literal[
        "Approved", "Archived", "Draft", "PendingReview"
    ] = Field(alias="ModelCardStatus")
    security_config: ModelCardSecurityConfigModel = Field(alias="SecurityConfig")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    model_card_processing_status: Literal[
        "ContentDeleted",
        "DeleteCompleted",
        "DeleteFailed",
        "DeleteInProgress",
        "DeletePending",
        "ExportJobsDeleted",
    ] = Field(alias="ModelCardProcessingStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelCardModel(BaseModel):
    model_card_arn: Optional[str] = Field(default=None, alias="ModelCardArn")
    model_card_name: Optional[str] = Field(default=None, alias="ModelCardName")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")
    content: Optional[str] = Field(default=None, alias="Content")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    security_config: Optional[ModelCardSecurityConfigModel] = Field(
        default=None, alias="SecurityConfig"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    model_id: Optional[str] = Field(default=None, alias="ModelId")
    risk_rating: Optional[str] = Field(default=None, alias="RiskRating")


class ModelDashboardModelCardModel(BaseModel):
    model_card_arn: Optional[str] = Field(default=None, alias="ModelCardArn")
    model_card_name: Optional[str] = Field(default=None, alias="ModelCardName")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    security_config: Optional[ModelCardSecurityConfigModel] = Field(
        default=None, alias="SecurityConfig"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    model_id: Optional[str] = Field(default=None, alias="ModelId")
    risk_rating: Optional[str] = Field(default=None, alias="RiskRating")


class CreateNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5d.18xlarge",
        "ml.c5d.2xlarge",
        "ml.c5d.4xlarge",
        "ml.c5d.9xlarge",
        "ml.c5d.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.xlarge",
        "ml.m5d.12xlarge",
        "ml.m5d.16xlarge",
        "ml.m5d.24xlarge",
        "ml.m5d.2xlarge",
        "ml.m5d.4xlarge",
        "ml.m5d.8xlarge",
        "ml.m5d.large",
        "ml.m5d.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.r5.12xlarge",
        "ml.r5.16xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.8xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.t2.2xlarge",
        "ml.t2.large",
        "ml.t2.medium",
        "ml.t2.xlarge",
        "ml.t3.2xlarge",
        "ml.t3.large",
        "ml.t3.medium",
        "ml.t3.xlarge",
    ] = Field(alias="InstanceType")
    role_arn: str = Field(alias="RoleArn")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    lifecycle_config_name: Optional[str] = Field(
        default=None, alias="LifecycleConfigName"
    )
    direct_internet_access: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="DirectInternetAccess"
    )
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    accelerator_types: Optional[
        Sequence[
            Literal[
                "ml.eia1.large",
                "ml.eia1.medium",
                "ml.eia1.xlarge",
                "ml.eia2.large",
                "ml.eia2.medium",
                "ml.eia2.xlarge",
            ]
        ]
    ] = Field(default=None, alias="AcceleratorTypes")
    default_code_repository: Optional[str] = Field(
        default=None, alias="DefaultCodeRepository"
    )
    additional_code_repositories: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalCodeRepositories"
    )
    root_access: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="RootAccess"
    )
    platform_identifier: Optional[str] = Field(default=None, alias="PlatformIdentifier")
    instance_metadata_service_configuration: Optional[
        InstanceMetadataServiceConfigurationModel
    ] = Field(default=None, alias="InstanceMetadataServiceConfiguration")


class DescribeNotebookInstanceOutputModel(BaseModel):
    notebook_instance_arn: str = Field(alias="NotebookInstanceArn")
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    notebook_instance_status: Literal[
        "Deleting", "Failed", "InService", "Pending", "Stopped", "Stopping", "Updating"
    ] = Field(alias="NotebookInstanceStatus")
    failure_reason: str = Field(alias="FailureReason")
    url: str = Field(alias="Url")
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.xlarge",
        "ml.c5d.18xlarge",
        "ml.c5d.2xlarge",
        "ml.c5d.4xlarge",
        "ml.c5d.9xlarge",
        "ml.c5d.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.xlarge",
        "ml.m5d.12xlarge",
        "ml.m5d.16xlarge",
        "ml.m5d.24xlarge",
        "ml.m5d.2xlarge",
        "ml.m5d.4xlarge",
        "ml.m5d.8xlarge",
        "ml.m5d.large",
        "ml.m5d.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p3dn.24xlarge",
        "ml.r5.12xlarge",
        "ml.r5.16xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.8xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.t2.2xlarge",
        "ml.t2.large",
        "ml.t2.medium",
        "ml.t2.xlarge",
        "ml.t3.2xlarge",
        "ml.t3.large",
        "ml.t3.medium",
        "ml.t3.xlarge",
    ] = Field(alias="InstanceType")
    subnet_id: str = Field(alias="SubnetId")
    security_groups: List[str] = Field(alias="SecurityGroups")
    role_arn: str = Field(alias="RoleArn")
    kms_key_id: str = Field(alias="KmsKeyId")
    network_interface_id: str = Field(alias="NetworkInterfaceId")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    creation_time: datetime = Field(alias="CreationTime")
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )
    direct_internet_access: Literal["Disabled", "Enabled"] = Field(
        alias="DirectInternetAccess"
    )
    volume_size_in_gb: int = Field(alias="VolumeSizeInGB")
    accelerator_types: List[
        Literal[
            "ml.eia1.large",
            "ml.eia1.medium",
            "ml.eia1.xlarge",
            "ml.eia2.large",
            "ml.eia2.medium",
            "ml.eia2.xlarge",
        ]
    ] = Field(alias="AcceleratorTypes")
    default_code_repository: str = Field(alias="DefaultCodeRepository")
    additional_code_repositories: List[str] = Field(alias="AdditionalCodeRepositories")
    root_access: Literal["Disabled", "Enabled"] = Field(alias="RootAccess")
    platform_identifier: str = Field(alias="PlatformIdentifier")
    instance_metadata_service_configuration: InstanceMetadataServiceConfigurationModel = Field(
        alias="InstanceMetadataServiceConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNotebookInstanceInputRequestModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.c5d.18xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.16xlarge",
            "ml.m5d.24xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.8xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.t2.2xlarge",
            "ml.t2.large",
            "ml.t2.medium",
            "ml.t2.xlarge",
            "ml.t3.2xlarge",
            "ml.t3.large",
            "ml.t3.medium",
            "ml.t3.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    lifecycle_config_name: Optional[str] = Field(
        default=None, alias="LifecycleConfigName"
    )
    disassociate_lifecycle_config: Optional[bool] = Field(
        default=None, alias="DisassociateLifecycleConfig"
    )
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    default_code_repository: Optional[str] = Field(
        default=None, alias="DefaultCodeRepository"
    )
    additional_code_repositories: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalCodeRepositories"
    )
    accelerator_types: Optional[
        Sequence[
            Literal[
                "ml.eia1.large",
                "ml.eia1.medium",
                "ml.eia1.xlarge",
                "ml.eia2.large",
                "ml.eia2.medium",
                "ml.eia2.xlarge",
            ]
        ]
    ] = Field(default=None, alias="AcceleratorTypes")
    disassociate_accelerator_types: Optional[bool] = Field(
        default=None, alias="DisassociateAcceleratorTypes"
    )
    disassociate_default_code_repository: Optional[bool] = Field(
        default=None, alias="DisassociateDefaultCodeRepository"
    )
    disassociate_additional_code_repositories: Optional[bool] = Field(
        default=None, alias="DisassociateAdditionalCodeRepositories"
    )
    root_access: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="RootAccess"
    )
    instance_metadata_service_configuration: Optional[
        InstanceMetadataServiceConfigurationModel
    ] = Field(default=None, alias="InstanceMetadataServiceConfiguration")


class CreateNotebookInstanceLifecycleConfigInputRequestModel(BaseModel):
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )
    on_create: Optional[Sequence[NotebookInstanceLifecycleHookModel]] = Field(
        default=None, alias="OnCreate"
    )
    on_start: Optional[Sequence[NotebookInstanceLifecycleHookModel]] = Field(
        default=None, alias="OnStart"
    )


class DescribeNotebookInstanceLifecycleConfigOutputModel(BaseModel):
    notebook_instance_lifecycle_config_arn: str = Field(
        alias="NotebookInstanceLifecycleConfigArn"
    )
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )
    on_create: List[NotebookInstanceLifecycleHookModel] = Field(alias="OnCreate")
    on_start: List[NotebookInstanceLifecycleHookModel] = Field(alias="OnStart")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNotebookInstanceLifecycleConfigInputRequestModel(BaseModel):
    notebook_instance_lifecycle_config_name: str = Field(
        alias="NotebookInstanceLifecycleConfigName"
    )
    on_create: Optional[Sequence[NotebookInstanceLifecycleHookModel]] = Field(
        default=None, alias="OnCreate"
    )
    on_start: Optional[Sequence[NotebookInstanceLifecycleHookModel]] = Field(
        default=None, alias="OnStart"
    )


class DescribePipelineResponseModel(BaseModel):
    pipeline_arn: str = Field(alias="PipelineArn")
    pipeline_name: str = Field(alias="PipelineName")
    pipeline_display_name: str = Field(alias="PipelineDisplayName")
    pipeline_definition: str = Field(alias="PipelineDefinition")
    pipeline_description: str = Field(alias="PipelineDescription")
    role_arn: str = Field(alias="RoleArn")
    pipeline_status: Literal["Active"] = Field(alias="PipelineStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_run_time: datetime = Field(alias="LastRunTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    parallelism_configuration: ParallelismConfigurationModel = Field(
        alias="ParallelismConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PipelineModel(BaseModel):
    pipeline_arn: Optional[str] = Field(default=None, alias="PipelineArn")
    pipeline_name: Optional[str] = Field(default=None, alias="PipelineName")
    pipeline_display_name: Optional[str] = Field(
        default=None, alias="PipelineDisplayName"
    )
    pipeline_description: Optional[str] = Field(
        default=None, alias="PipelineDescription"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    pipeline_status: Optional[Literal["Active"]] = Field(
        default=None, alias="PipelineStatus"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_run_time: Optional[datetime] = Field(default=None, alias="LastRunTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class RetryPipelineExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    client_request_token: str = Field(alias="ClientRequestToken")
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class UpdatePipelineExecutionRequestModel(BaseModel):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    pipeline_execution_description: Optional[str] = Field(
        default=None, alias="PipelineExecutionDescription"
    )
    pipeline_execution_display_name: Optional[str] = Field(
        default=None, alias="PipelineExecutionDisplayName"
    )
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class CreatePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    client_request_token: str = Field(alias="ClientRequestToken")
    role_arn: str = Field(alias="RoleArn")
    pipeline_display_name: Optional[str] = Field(
        default=None, alias="PipelineDisplayName"
    )
    pipeline_definition: Optional[str] = Field(default=None, alias="PipelineDefinition")
    pipeline_definition_s3_location: Optional[
        PipelineDefinitionS3LocationModel
    ] = Field(default=None, alias="PipelineDefinitionS3Location")
    pipeline_description: Optional[str] = Field(
        default=None, alias="PipelineDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class UpdatePipelineRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    pipeline_display_name: Optional[str] = Field(
        default=None, alias="PipelineDisplayName"
    )
    pipeline_definition: Optional[str] = Field(default=None, alias="PipelineDefinition")
    pipeline_definition_s3_location: Optional[
        PipelineDefinitionS3LocationModel
    ] = Field(default=None, alias="PipelineDefinitionS3Location")
    pipeline_description: Optional[str] = Field(
        default=None, alias="PipelineDescription"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class CreateTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    status: Optional[TrialComponentStatusModel] = Field(default=None, alias="Status")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    parameters: Optional[Mapping[str, TrialComponentParameterValueModel]] = Field(
        default=None, alias="Parameters"
    )
    input_artifacts: Optional[Mapping[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="InputArtifacts"
    )
    output_artifacts: Optional[Mapping[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="OutputArtifacts"
    )
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateTrialComponentRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    status: Optional[TrialComponentStatusModel] = Field(default=None, alias="Status")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    parameters: Optional[Mapping[str, TrialComponentParameterValueModel]] = Field(
        default=None, alias="Parameters"
    )
    parameters_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="ParametersToRemove"
    )
    input_artifacts: Optional[Mapping[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="InputArtifacts"
    )
    input_artifacts_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="InputArtifactsToRemove"
    )
    output_artifacts: Optional[Mapping[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="OutputArtifacts"
    )
    output_artifacts_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="OutputArtifactsToRemove"
    )


class CreateWorkforceRequestModel(BaseModel):
    workforce_name: str = Field(alias="WorkforceName")
    cognito_config: Optional[CognitoConfigModel] = Field(
        default=None, alias="CognitoConfig"
    )
    oidc_config: Optional[OidcConfigModel] = Field(default=None, alias="OidcConfig")
    source_ip_config: Optional[SourceIpConfigModel] = Field(
        default=None, alias="SourceIpConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    workforce_vpc_config: Optional[WorkforceVpcConfigRequestModel] = Field(
        default=None, alias="WorkforceVpcConfig"
    )


class UpdateWorkforceRequestModel(BaseModel):
    workforce_name: str = Field(alias="WorkforceName")
    source_ip_config: Optional[SourceIpConfigModel] = Field(
        default=None, alias="SourceIpConfig"
    )
    oidc_config: Optional[OidcConfigModel] = Field(default=None, alias="OidcConfig")
    workforce_vpc_config: Optional[WorkforceVpcConfigRequestModel] = Field(
        default=None, alias="WorkforceVpcConfig"
    )


class KernelGatewayAppSettingsModel(BaseModel):
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )
    custom_images: Optional[Sequence[CustomImageModel]] = Field(
        default=None, alias="CustomImages"
    )
    lifecycle_config_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LifecycleConfigArns"
    )


class RSessionAppSettingsModel(BaseModel):
    default_resource_spec: Optional[ResourceSpecModel] = Field(
        default=None, alias="DefaultResourceSpec"
    )
    custom_images: Optional[Sequence[CustomImageModel]] = Field(
        default=None, alias="CustomImages"
    )


class ModelBiasBaselineConfigModel(BaseModel):
    baselining_job_name: Optional[str] = Field(default=None, alias="BaseliningJobName")
    constraints_resource: Optional[MonitoringConstraintsResourceModel] = Field(
        default=None, alias="ConstraintsResource"
    )


class ModelExplainabilityBaselineConfigModel(BaseModel):
    baselining_job_name: Optional[str] = Field(default=None, alias="BaseliningJobName")
    constraints_resource: Optional[MonitoringConstraintsResourceModel] = Field(
        default=None, alias="ConstraintsResource"
    )


class ModelQualityBaselineConfigModel(BaseModel):
    baselining_job_name: Optional[str] = Field(default=None, alias="BaseliningJobName")
    constraints_resource: Optional[MonitoringConstraintsResourceModel] = Field(
        default=None, alias="ConstraintsResource"
    )


class DataQualityBaselineConfigModel(BaseModel):
    baselining_job_name: Optional[str] = Field(default=None, alias="BaseliningJobName")
    constraints_resource: Optional[MonitoringConstraintsResourceModel] = Field(
        default=None, alias="ConstraintsResource"
    )
    statistics_resource: Optional[MonitoringStatisticsResourceModel] = Field(
        default=None, alias="StatisticsResource"
    )


class MonitoringBaselineConfigModel(BaseModel):
    baselining_job_name: Optional[str] = Field(default=None, alias="BaseliningJobName")
    constraints_resource: Optional[MonitoringConstraintsResourceModel] = Field(
        default=None, alias="ConstraintsResource"
    )
    statistics_resource: Optional[MonitoringStatisticsResourceModel] = Field(
        default=None, alias="StatisticsResource"
    )


class DataSourceModel(BaseModel):
    s3_data_source: Optional[S3DataSourceModel] = Field(
        default=None, alias="S3DataSource"
    )
    file_system_data_source: Optional[FileSystemDataSourceModel] = Field(
        default=None, alias="FileSystemDataSource"
    )


class DatasetDefinitionModel(BaseModel):
    athena_dataset_definition: Optional[AthenaDatasetDefinitionModel] = Field(
        default=None, alias="AthenaDatasetDefinition"
    )
    redshift_dataset_definition: Optional[RedshiftDatasetDefinitionModel] = Field(
        default=None, alias="RedshiftDatasetDefinition"
    )
    local_path: Optional[str] = Field(default=None, alias="LocalPath")
    data_distribution_type: Optional[
        Literal["FullyReplicated", "ShardedByS3Key"]
    ] = Field(default=None, alias="DataDistributionType")
    input_mode: Optional[Literal["File", "Pipe"]] = Field(
        default=None, alias="InputMode"
    )


class DeleteDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    retention_policy: Optional[RetentionPolicyModel] = Field(
        default=None, alias="RetentionPolicy"
    )


class DeploymentStageModel(BaseModel):
    stage_name: str = Field(alias="StageName")
    device_selection_config: DeviceSelectionConfigModel = Field(
        alias="DeviceSelectionConfig"
    )
    deployment_config: Optional[EdgeDeploymentConfigModel] = Field(
        default=None, alias="DeploymentConfig"
    )


class DeploymentStageStatusSummaryModel(BaseModel):
    stage_name: str = Field(alias="StageName")
    device_selection_config: DeviceSelectionConfigModel = Field(
        alias="DeviceSelectionConfig"
    )
    deployment_config: EdgeDeploymentConfigModel = Field(alias="DeploymentConfig")
    deployment_status: EdgeDeploymentStatusModel = Field(alias="DeploymentStatus")


class DescribeDeviceResponseModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    device_name: str = Field(alias="DeviceName")
    description: str = Field(alias="Description")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    iot_thing_name: str = Field(alias="IotThingName")
    registration_time: datetime = Field(alias="RegistrationTime")
    latest_heartbeat: datetime = Field(alias="LatestHeartbeat")
    models: List[EdgeModelModel] = Field(alias="Models")
    max_models: int = Field(alias="MaxModels")
    next_token: str = Field(alias="NextToken")
    agent_version: str = Field(alias="AgentVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEdgePackagingJobResponseModel(BaseModel):
    edge_packaging_job_arn: str = Field(alias="EdgePackagingJobArn")
    edge_packaging_job_name: str = Field(alias="EdgePackagingJobName")
    compilation_job_name: str = Field(alias="CompilationJobName")
    model_name: str = Field(alias="ModelName")
    model_version: str = Field(alias="ModelVersion")
    role_arn: str = Field(alias="RoleArn")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    resource_key: str = Field(alias="ResourceKey")
    edge_packaging_job_status: Literal[
        "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
    ] = Field(alias="EdgePackagingJobStatus")
    edge_packaging_job_status_message: str = Field(
        alias="EdgePackagingJobStatusMessage"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    model_artifact: str = Field(alias="ModelArtifact")
    model_signature: str = Field(alias="ModelSignature")
    preset_deployment_output: EdgePresetDeploymentOutputModel = Field(
        alias="PresetDeploymentOutput"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointInputEndpointDeletedWaitModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndpointInputEndpointInServiceWaitModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImageRequestImageCreatedWaitModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImageRequestImageDeletedWaitModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImageRequestImageUpdatedWaitModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImageVersionRequestImageVersionCreatedWaitModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    version: Optional[int] = Field(default=None, alias="Version")
    alias: Optional[str] = Field(default=None, alias="Alias")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImageVersionRequestImageVersionDeletedWaitModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    version: Optional[int] = Field(default=None, alias="Version")
    alias: Optional[str] = Field(default=None, alias="Alias")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNotebookInstanceInputNotebookInstanceDeletedWaitModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNotebookInstanceInputNotebookInstanceInServiceWaitModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNotebookInstanceInputNotebookInstanceStoppedWaitModel(BaseModel):
    notebook_instance_name: str = Field(alias="NotebookInstanceName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitModel(BaseModel):
    processing_job_name: str = Field(alias="ProcessingJobName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTransformJobRequestTransformJobCompletedOrStoppedWaitModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeExperimentResponseModel(BaseModel):
    experiment_name: str = Field(alias="ExperimentName")
    experiment_arn: str = Field(alias="ExperimentArn")
    display_name: str = Field(alias="DisplayName")
    source: ExperimentSourceModel = Field(alias="Source")
    description: str = Field(alias="Description")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExperimentSummaryModel(BaseModel):
    experiment_arn: Optional[str] = Field(default=None, alias="ExperimentArn")
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    experiment_source: Optional[ExperimentSourceModel] = Field(
        default=None, alias="ExperimentSource"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ExperimentModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    experiment_arn: Optional[str] = Field(default=None, alias="ExperimentArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    source: Optional[ExperimentSourceModel] = Field(default=None, alias="Source")
    description: Optional[str] = Field(default=None, alias="Description")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class FeatureGroupSummaryModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    feature_group_arn: str = Field(alias="FeatureGroupArn")
    creation_time: datetime = Field(alias="CreationTime")
    feature_group_status: Optional[
        Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
    ] = Field(default=None, alias="FeatureGroupStatus")
    offline_store_status: Optional[OfflineStoreStatusModel] = Field(
        default=None, alias="OfflineStoreStatus"
    )


class DescribeFeatureMetadataResponseModel(BaseModel):
    feature_group_arn: str = Field(alias="FeatureGroupArn")
    feature_group_name: str = Field(alias="FeatureGroupName")
    feature_name: str = Field(alias="FeatureName")
    feature_type: Literal["Fractional", "Integral", "String"] = Field(
        alias="FeatureType"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    description: str = Field(alias="Description")
    parameters: List[FeatureParameterModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FeatureMetadataModel(BaseModel):
    feature_group_arn: Optional[str] = Field(default=None, alias="FeatureGroupArn")
    feature_group_name: Optional[str] = Field(default=None, alias="FeatureGroupName")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")
    feature_type: Optional[Literal["Fractional", "Integral", "String"]] = Field(
        default=None, alias="FeatureType"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[List[FeatureParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class UpdateFeatureMetadataRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    feature_name: str = Field(alias="FeatureName")
    description: Optional[str] = Field(default=None, alias="Description")
    parameter_additions: Optional[Sequence[FeatureParameterModel]] = Field(
        default=None, alias="ParameterAdditions"
    )
    parameter_removals: Optional[Sequence[str]] = Field(
        default=None, alias="ParameterRemovals"
    )


class DescribeHubContentResponseModel(BaseModel):
    hub_content_name: str = Field(alias="HubContentName")
    hub_content_arn: str = Field(alias="HubContentArn")
    hub_content_version: str = Field(alias="HubContentVersion")
    hub_content_type: Literal["Model", "Notebook"] = Field(alias="HubContentType")
    document_schema_version: str = Field(alias="DocumentSchemaVersion")
    hub_name: str = Field(alias="HubName")
    hub_arn: str = Field(alias="HubArn")
    hub_content_display_name: str = Field(alias="HubContentDisplayName")
    hub_content_description: str = Field(alias="HubContentDescription")
    hub_content_markdown: str = Field(alias="HubContentMarkdown")
    hub_content_document: str = Field(alias="HubContentDocument")
    hub_content_search_keywords: List[str] = Field(alias="HubContentSearchKeywords")
    hub_content_dependencies: List[HubContentDependencyModel] = Field(
        alias="HubContentDependencies"
    )
    hub_content_status: Literal[
        "Available", "DeleteFailed", "Deleting", "ImportFailed", "Importing"
    ] = Field(alias="HubContentStatus")
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHumanTaskUiResponseModel(BaseModel):
    human_task_ui_arn: str = Field(alias="HumanTaskUiArn")
    human_task_ui_name: str = Field(alias="HumanTaskUiName")
    human_task_ui_status: Literal["Active", "Deleting"] = Field(
        alias="HumanTaskUiStatus"
    )
    creation_time: datetime = Field(alias="CreationTime")
    ui_template: UiTemplateInfoModel = Field(alias="UiTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeModelCardExportJobResponseModel(BaseModel):
    model_card_export_job_name: str = Field(alias="ModelCardExportJobName")
    model_card_export_job_arn: str = Field(alias="ModelCardExportJobArn")
    status: Literal["Completed", "Failed", "InProgress"] = Field(alias="Status")
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: int = Field(alias="ModelCardVersion")
    output_config: ModelCardExportOutputConfigModel = Field(alias="OutputConfig")
    created_at: datetime = Field(alias="CreatedAt")
    last_modified_at: datetime = Field(alias="LastModifiedAt")
    failure_reason: str = Field(alias="FailureReason")
    export_artifacts: ModelCardExportArtifactsModel = Field(alias="ExportArtifacts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMonitoringExecutionsResponseModel(BaseModel):
    monitoring_execution_summaries: List[MonitoringExecutionSummaryModel] = Field(
        alias="MonitoringExecutionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePipelineExecutionResponseModel(BaseModel):
    pipeline_arn: str = Field(alias="PipelineArn")
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    pipeline_execution_display_name: str = Field(alias="PipelineExecutionDisplayName")
    pipeline_execution_status: Literal[
        "Executing", "Failed", "Stopped", "Stopping", "Succeeded"
    ] = Field(alias="PipelineExecutionStatus")
    pipeline_execution_description: str = Field(alias="PipelineExecutionDescription")
    pipeline_experiment_config: PipelineExperimentConfigModel = Field(
        alias="PipelineExperimentConfig"
    )
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    parallelism_configuration: ParallelismConfigurationModel = Field(
        alias="ParallelismConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSubscribedWorkteamResponseModel(BaseModel):
    subscribed_workteam: SubscribedWorkteamModel = Field(alias="SubscribedWorkteam")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscribedWorkteamsResponseModel(BaseModel):
    subscribed_workteams: List[SubscribedWorkteamModel] = Field(
        alias="SubscribedWorkteams"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrainingJobSummaryModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    training_job_arn: str = Field(alias="TrainingJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    training_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="TrainingJobStatus")
    training_end_time: Optional[datetime] = Field(default=None, alias="TrainingEndTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    warm_pool_status: Optional[WarmPoolStatusModel] = Field(
        default=None, alias="WarmPoolStatus"
    )


class DescribeTrialComponentResponseModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    trial_component_arn: str = Field(alias="TrialComponentArn")
    display_name: str = Field(alias="DisplayName")
    source: TrialComponentSourceModel = Field(alias="Source")
    status: TrialComponentStatusModel = Field(alias="Status")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    parameters: Dict[str, TrialComponentParameterValueModel] = Field(alias="Parameters")
    input_artifacts: Dict[str, TrialComponentArtifactModel] = Field(
        alias="InputArtifacts"
    )
    output_artifacts: Dict[str, TrialComponentArtifactModel] = Field(
        alias="OutputArtifacts"
    )
    metadata_properties: MetadataPropertiesModel = Field(alias="MetadataProperties")
    metrics: List[TrialComponentMetricSummaryModel] = Field(alias="Metrics")
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    sources: List[TrialComponentSourceModel] = Field(alias="Sources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrialComponentSimpleSummaryModel(BaseModel):
    trial_component_name: Optional[str] = Field(
        default=None, alias="TrialComponentName"
    )
    trial_component_arn: Optional[str] = Field(default=None, alias="TrialComponentArn")
    trial_component_source: Optional[TrialComponentSourceModel] = Field(
        default=None, alias="TrialComponentSource"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")


class TrialComponentSummaryModel(BaseModel):
    trial_component_name: Optional[str] = Field(
        default=None, alias="TrialComponentName"
    )
    trial_component_arn: Optional[str] = Field(default=None, alias="TrialComponentArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    trial_component_source: Optional[TrialComponentSourceModel] = Field(
        default=None, alias="TrialComponentSource"
    )
    status: Optional[TrialComponentStatusModel] = Field(default=None, alias="Status")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )


class DescribeTrialResponseModel(BaseModel):
    trial_name: str = Field(alias="TrialName")
    trial_arn: str = Field(alias="TrialArn")
    display_name: str = Field(alias="DisplayName")
    experiment_name: str = Field(alias="ExperimentName")
    source: TrialSourceModel = Field(alias="Source")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    metadata_properties: MetadataPropertiesModel = Field(alias="MetadataProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrialSummaryModel(BaseModel):
    trial_arn: Optional[str] = Field(default=None, alias="TrialArn")
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    trial_source: Optional[TrialSourceModel] = Field(default=None, alias="TrialSource")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class UpdateEndpointWeightsAndCapacitiesInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    desired_weights_and_capacities: Sequence[DesiredWeightAndCapacityModel] = Field(
        alias="DesiredWeightsAndCapacities"
    )


class ListStageDevicesResponseModel(BaseModel):
    device_deployment_summaries: List[DeviceDeploymentSummaryModel] = Field(
        alias="DeviceDeploymentSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceFleetsResponseModel(BaseModel):
    device_fleet_summaries: List[DeviceFleetSummaryModel] = Field(
        alias="DeviceFleetSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceSummaryModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    device_arn: str = Field(alias="DeviceArn")
    description: Optional[str] = Field(default=None, alias="Description")
    device_fleet_name: Optional[str] = Field(default=None, alias="DeviceFleetName")
    iot_thing_name: Optional[str] = Field(default=None, alias="IotThingName")
    registration_time: Optional[datetime] = Field(
        default=None, alias="RegistrationTime"
    )
    latest_heartbeat: Optional[datetime] = Field(default=None, alias="LatestHeartbeat")
    models: Optional[List[EdgeModelSummaryModel]] = Field(default=None, alias="Models")
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class RegisterDevicesRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    devices: Sequence[DeviceModel] = Field(alias="Devices")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateDevicesRequestModel(BaseModel):
    device_fleet_name: str = Field(alias="DeviceFleetName")
    devices: Sequence[DeviceModel] = Field(alias="Devices")


class ListDomainsResponseModel(BaseModel):
    domains: List[DomainDetailsModel] = Field(alias="Domains")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DriftCheckBiasModel(BaseModel):
    config_file: Optional[FileSourceModel] = Field(default=None, alias="ConfigFile")
    pre_training_constraints: Optional[MetricsSourceModel] = Field(
        default=None, alias="PreTrainingConstraints"
    )
    post_training_constraints: Optional[MetricsSourceModel] = Field(
        default=None, alias="PostTrainingConstraints"
    )


class DriftCheckExplainabilityModel(BaseModel):
    constraints: Optional[MetricsSourceModel] = Field(default=None, alias="Constraints")
    config_file: Optional[FileSourceModel] = Field(default=None, alias="ConfigFile")


class ListEdgeDeploymentPlansResponseModel(BaseModel):
    edge_deployment_plan_summaries: List[EdgeDeploymentPlanSummaryModel] = Field(
        alias="EdgeDeploymentPlanSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceFleetReportResponseModel(BaseModel):
    device_fleet_arn: str = Field(alias="DeviceFleetArn")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    output_config: EdgeOutputConfigModel = Field(alias="OutputConfig")
    description: str = Field(alias="Description")
    report_generated: datetime = Field(alias="ReportGenerated")
    device_stats: DeviceStatsModel = Field(alias="DeviceStats")
    agent_versions: List[AgentVersionModel] = Field(alias="AgentVersions")
    model_stats: List[EdgeModelStatModel] = Field(alias="ModelStats")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEdgePackagingJobsResponseModel(BaseModel):
    edge_packaging_job_summaries: List[EdgePackagingJobSummaryModel] = Field(
        alias="EdgePackagingJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointConfigsOutputModel(BaseModel):
    endpoint_configs: List[EndpointConfigSummaryModel] = Field(alias="EndpointConfigs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointPerformanceModel(BaseModel):
    metrics: InferenceMetricsModel = Field(alias="Metrics")
    endpoint_info: EndpointInfoModel = Field(alias="EndpointInfo")


class ListEndpointsOutputModel(BaseModel):
    endpoints: List[EndpointSummaryModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelConfigurationModel(BaseModel):
    inference_specification_name: Optional[str] = Field(
        default=None, alias="InferenceSpecificationName"
    )
    environment_parameters: Optional[List[EnvironmentParameterModel]] = Field(
        default=None, alias="EnvironmentParameters"
    )
    compilation_job_name: Optional[str] = Field(
        default=None, alias="CompilationJobName"
    )


class NestedFiltersModel(BaseModel):
    nested_property_name: str = Field(alias="NestedPropertyName")
    filters: Sequence[FilterModel] = Field(alias="Filters")


class HyperParameterTrainingJobSummaryModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    training_job_arn: str = Field(alias="TrainingJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    training_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="TrainingJobStatus")
    tuned_hyper_parameters: Dict[str, str] = Field(alias="TunedHyperParameters")
    training_job_definition_name: Optional[str] = Field(
        default=None, alias="TrainingJobDefinitionName"
    )
    tuning_job_name: Optional[str] = Field(default=None, alias="TuningJobName")
    training_start_time: Optional[datetime] = Field(
        default=None, alias="TrainingStartTime"
    )
    training_end_time: Optional[datetime] = Field(default=None, alias="TrainingEndTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    final_hyper_parameter_tuning_job_objective_metric: Optional[
        FinalHyperParameterTuningJobObjectiveMetricModel
    ] = Field(default=None, alias="FinalHyperParameterTuningJobObjectiveMetric")
    objective_status: Optional[Literal["Failed", "Pending", "Succeeded"]] = Field(
        default=None, alias="ObjectiveStatus"
    )


class ListFlowDefinitionsResponseModel(BaseModel):
    flow_definition_summaries: List[FlowDefinitionSummaryModel] = Field(
        alias="FlowDefinitionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSearchSuggestionsResponseModel(BaseModel):
    property_name_suggestions: List[PropertyNameSuggestionModel] = Field(
        alias="PropertyNameSuggestions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCodeRepositoryInputRequestModel(BaseModel):
    code_repository_name: str = Field(alias="CodeRepositoryName")
    git_config: Optional[GitConfigForUpdateModel] = Field(
        default=None, alias="GitConfig"
    )


class ListHubContentVersionsResponseModel(BaseModel):
    hub_content_summaries: List[HubContentInfoModel] = Field(
        alias="HubContentSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHubContentsResponseModel(BaseModel):
    hub_content_summaries: List[HubContentInfoModel] = Field(
        alias="HubContentSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHubsResponseModel(BaseModel):
    hub_summaries: List[HubInfoModel] = Field(alias="HubSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HumanLoopActivationConfigModel(BaseModel):
    human_loop_activation_conditions_config: HumanLoopActivationConditionsConfigModel = Field(
        alias="HumanLoopActivationConditionsConfig"
    )


class ListHumanTaskUisResponseModel(BaseModel):
    human_task_ui_summaries: List[HumanTaskUiSummaryModel] = Field(
        alias="HumanTaskUiSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HyperParameterTuningResourceConfigModel(BaseModel):
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.c5n.18xlarge",
            "ml.c5n.2xlarge",
            "ml.c5n.4xlarge",
            "ml.c5n.9xlarge",
            "ml.c5n.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.p4d.24xlarge",
            "ml.trn1.2xlarge",
            "ml.trn1.32xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    allocation_strategy: Optional[Literal["Prioritized"]] = Field(
        default=None, alias="AllocationStrategy"
    )
    instance_configs: Optional[
        Sequence[HyperParameterTuningInstanceConfigModel]
    ] = Field(default=None, alias="InstanceConfigs")


class HyperParameterTuningJobSummaryModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")
    hyper_parameter_tuning_job_arn: str = Field(alias="HyperParameterTuningJobArn")
    hyper_parameter_tuning_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="HyperParameterTuningJobStatus")
    strategy: Literal["Bayesian", "Grid", "Hyperband", "Random"] = Field(
        alias="Strategy"
    )
    creation_time: datetime = Field(alias="CreationTime")
    training_job_status_counters: TrainingJobStatusCountersModel = Field(
        alias="TrainingJobStatusCounters"
    )
    objective_status_counters: ObjectiveStatusCountersModel = Field(
        alias="ObjectiveStatusCounters"
    )
    hyper_parameter_tuning_end_time: Optional[datetime] = Field(
        default=None, alias="HyperParameterTuningEndTime"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    resource_limits: Optional[ResourceLimitsModel] = Field(
        default=None, alias="ResourceLimits"
    )


class HyperParameterTuningJobStrategyConfigModel(BaseModel):
    hyperband_strategy_config: Optional[HyperbandStrategyConfigModel] = Field(
        default=None, alias="HyperbandStrategyConfig"
    )


class HyperParameterTuningJobWarmStartConfigModel(BaseModel):
    parent_hyper_parameter_tuning_jobs: Sequence[
        ParentHyperParameterTuningJobModel
    ] = Field(alias="ParentHyperParameterTuningJobs")
    warm_start_type: Literal["IdenticalDataAndAlgorithm", "TransferLearning"] = Field(
        alias="WarmStartType"
    )


class ImageConfigModel(BaseModel):
    repository_access_mode: Literal["Platform", "Vpc"] = Field(
        alias="RepositoryAccessMode"
    )
    repository_auth_config: Optional[RepositoryAuthConfigModel] = Field(
        default=None, alias="RepositoryAuthConfig"
    )


class ListImagesResponseModel(BaseModel):
    images: List[ImageModel] = Field(alias="Images")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImageVersionsResponseModel(BaseModel):
    image_versions: List[ImageVersionModel] = Field(alias="ImageVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInferenceRecommendationsJobsResponseModel(BaseModel):
    inference_recommendations_jobs: List[InferenceRecommendationsJobModel] = Field(
        alias="InferenceRecommendationsJobs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceConfigModel(BaseModel):
    volume_size_in_gb: int = Field(alias="VolumeSizeInGB")
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.c5n.18xlarge",
            "ml.c5n.2xlarge",
            "ml.c5n.4xlarge",
            "ml.c5n.9xlarge",
            "ml.c5n.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.p4d.24xlarge",
            "ml.trn1.2xlarge",
            "ml.trn1.32xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    instance_groups: Optional[Sequence[InstanceGroupModel]] = Field(
        default=None, alias="InstanceGroups"
    )
    keep_alive_period_in_seconds: Optional[int] = Field(
        default=None, alias="KeepAlivePeriodInSeconds"
    )


class ParameterRangeModel(BaseModel):
    integer_parameter_range_specification: Optional[
        IntegerParameterRangeSpecificationModel
    ] = Field(default=None, alias="IntegerParameterRangeSpecification")
    continuous_parameter_range_specification: Optional[
        ContinuousParameterRangeSpecificationModel
    ] = Field(default=None, alias="ContinuousParameterRangeSpecification")
    categorical_parameter_range_specification: Optional[
        CategoricalParameterRangeSpecificationModel
    ] = Field(default=None, alias="CategoricalParameterRangeSpecification")


class ParameterRangesModel(BaseModel):
    integer_parameter_ranges: Optional[Sequence[IntegerParameterRangeModel]] = Field(
        default=None, alias="IntegerParameterRanges"
    )
    continuous_parameter_ranges: Optional[
        Sequence[ContinuousParameterRangeModel]
    ] = Field(default=None, alias="ContinuousParameterRanges")
    categorical_parameter_ranges: Optional[
        Sequence[CategoricalParameterRangeModel]
    ] = Field(default=None, alias="CategoricalParameterRanges")


class KernelGatewayImageConfigModel(BaseModel):
    kernel_specs: Sequence[KernelSpecModel] = Field(alias="KernelSpecs")
    file_system_config: Optional[FileSystemConfigModel] = Field(
        default=None, alias="FileSystemConfig"
    )


class LabelingJobForWorkteamSummaryModel(BaseModel):
    job_reference_code: str = Field(alias="JobReferenceCode")
    work_requester_account_id: str = Field(alias="WorkRequesterAccountId")
    creation_time: datetime = Field(alias="CreationTime")
    labeling_job_name: Optional[str] = Field(default=None, alias="LabelingJobName")
    label_counters: Optional[LabelCountersForWorkteamModel] = Field(
        default=None, alias="LabelCounters"
    )
    number_of_human_workers_per_data_object: Optional[int] = Field(
        default=None, alias="NumberOfHumanWorkersPerDataObject"
    )


class LabelingJobDataSourceModel(BaseModel):
    s3_data_source: Optional[LabelingJobS3DataSourceModel] = Field(
        default=None, alias="S3DataSource"
    )
    sns_data_source: Optional[LabelingJobSnsDataSourceModel] = Field(
        default=None, alias="SnsDataSource"
    )


class ListLineageGroupsResponseModel(BaseModel):
    lineage_group_summaries: List[LineageGroupSummaryModel] = Field(
        alias="LineageGroupSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListActionsRequestListActionsPaginateModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    action_type: Optional[str] = Field(default=None, alias="ActionType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAlgorithmsInputListAlgorithmsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAliasesRequestListAliasesPaginateModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    alias: Optional[str] = Field(default=None, alias="Alias")
    version: Optional[int] = Field(default=None, alias="Version")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAppImageConfigsRequestListAppImageConfigsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeBefore"
    )
    modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeAfter"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAppsRequestListAppsPaginateModel(BaseModel):
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    user_profile_name_equals: Optional[str] = Field(
        default=None, alias="UserProfileNameEquals"
    )
    space_name_equals: Optional[str] = Field(default=None, alias="SpaceNameEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListArtifactsRequestListArtifactsPaginateModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    artifact_type: Optional[str] = Field(default=None, alias="ArtifactType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociationsRequestListAssociationsPaginateModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    destination_type: Optional[str] = Field(default=None, alias="DestinationType")
    association_type: Optional[
        Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
    ] = Field(default=None, alias="AssociationType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[
        Literal[
            "CreationTime",
            "DestinationArn",
            "DestinationType",
            "SourceArn",
            "SourceType",
        ]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAutoMLJobsRequestListAutoMLJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateModel(
    BaseModel
):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    candidate_name_equals: Optional[str] = Field(
        default=None, alias="CandidateNameEquals"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[
        Literal["CreationTime", "FinalObjectiveMetricValue", "Status"]
    ] = Field(default=None, alias="SortBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCodeRepositoriesInputListCodeRepositoriesPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCompilationJobsRequestListCompilationJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContextsRequestListContextsPaginateModel(BaseModel):
    source_uri: Optional[str] = Field(default=None, alias="SourceUri")
    context_type: Optional[str] = Field(default=None, alias="ContextType")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateModel(
    BaseModel
):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceFleetsRequestListDeviceFleetsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "NAME"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicesRequestListDevicesPaginateModel(BaseModel):
    latest_heartbeat_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LatestHeartbeatAfter"
    )
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    device_fleet_name: Optional[str] = Field(default=None, alias="DeviceFleetName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainsRequestListDomainsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    device_fleet_name_contains: Optional[str] = Field(
        default=None, alias="DeviceFleetNameContains"
    )
    sort_by: Optional[
        Literal["CREATION_TIME", "DEVICE_FLEET_NAME", "LAST_MODIFIED_TIME", "NAME"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_name_contains: Optional[str] = Field(default=None, alias="ModelNameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[
        Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "MODEL_NAME", "NAME", "STATUS"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEndpointConfigsInputListEndpointConfigsPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEndpointsInputListEndpointsPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Creating",
            "Deleting",
            "Failed",
            "InService",
            "OutOfService",
            "RollingBack",
            "SystemUpdating",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExperimentsRequestListExperimentsPaginateModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFeatureGroupsRequestListFeatureGroupsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    feature_group_status_equals: Optional[
        Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
    ] = Field(default=None, alias="FeatureGroupStatusEquals")
    offline_store_status_equals: Optional[
        Literal["Active", "Blocked", "Disabled"]
    ] = Field(default=None, alias="OfflineStoreStatusEquals")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[
        Literal["CreationTime", "FeatureGroupStatus", "Name", "OfflineStoreStatus"]
    ] = Field(default=None, alias="SortBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFlowDefinitionsRequestListFlowDefinitionsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHumanTaskUisRequestListHumanTaskUisPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateModel(
    BaseModel
):
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImageVersionsRequestListImageVersionsPaginateModel(BaseModel):
    image_name: str = Field(alias="ImageName")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    sort_by: Optional[
        Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImagesRequestListImagesPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[
        Literal["CREATION_TIME", "IMAGE_NAME", "LAST_MODIFIED_TIME"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInferenceExperimentsRequestListInferenceExperimentsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    type: Optional[Literal["ShadowMode"]] = Field(default=None, alias="Type")
    status_equals: Optional[
        Literal[
            "Cancelled",
            "Completed",
            "Created",
            "Creating",
            "Running",
            "Starting",
            "Stopping",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateModel(
    BaseModel
):
    job_name: str = Field(alias="JobName")
    status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="Status")
    step_type: Optional[Literal["BENCHMARK"]] = Field(default=None, alias="StepType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateModel(
    BaseModel
):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateModel(
    BaseModel
):
    workteam_arn: str = Field(alias="WorkteamArn")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    job_reference_code_contains: Optional[str] = Field(
        default=None, alias="JobReferenceCodeContains"
    )
    sort_by: Optional[Literal["CreationTime"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLabelingJobsRequestListLabelingJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[
        Literal[
            "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
        ]
    ] = Field(default=None, alias="StatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLineageGroupsRequestListLineageGroupsPaginateModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateModel(
    BaseModel
):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelCardExportJobsRequestListModelCardExportJobsPaginateModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    model_card_version: Optional[int] = Field(default=None, alias="ModelCardVersion")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    model_card_export_job_name_contains: Optional[str] = Field(
        default=None, alias="ModelCardExportJobNameContains"
    )
    status_equals: Optional[Literal["Completed", "Failed", "InProgress"]] = Field(
        default=None, alias="StatusEquals"
    )
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelCardVersionsRequestListModelCardVersionsPaginateModel(BaseModel):
    model_card_name: str = Field(alias="ModelCardName")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    sort_by: Optional[Literal["Version"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelCardsRequestListModelCardsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_card_status: Optional[
        Literal["Approved", "Archived", "Draft", "PendingReview"]
    ] = Field(default=None, alias="ModelCardStatus")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateModel(
    BaseModel
):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelPackageGroupsInputListModelPackageGroupsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelPackagesInputListModelPackagesPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_type: Optional[Literal["Both", "Unversioned", "Versioned"]] = Field(
        default=None, alias="ModelPackageType"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateModel(
    BaseModel
):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelsInputListModelsPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateModel(
    BaseModel
):
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    monitoring_alert_name: Optional[str] = Field(
        default=None, alias="MonitoringAlertName"
    )
    sort_by: Optional[Literal["CreationTime", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    status_equals: Optional[Literal["InAlert", "OK"]] = Field(
        default=None, alias="StatusEquals"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitoringAlertsRequestListMonitoringAlertsPaginateModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateModel(BaseModel):
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "ScheduledTime", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    scheduled_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTimeBefore"
    )
    scheduled_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Completed",
            "CompletedWithViolations",
            "Failed",
            "InProgress",
            "Pending",
            "Stopped",
            "Stopping",
        ]
    ] = Field(default=None, alias="StatusEquals")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type_equals: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringTypeEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal["Failed", "Pending", "Scheduled", "Stopped"]
    ] = Field(default=None, alias="StatusEquals")
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type_equals: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringTypeEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateModel(
    BaseModel
):
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotebookInstancesInputListNotebookInstancesPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    status_equals: Optional[
        Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Stopped",
            "Stopping",
            "Updating",
        ]
    ] = Field(default=None, alias="StatusEquals")
    notebook_instance_lifecycle_config_name_contains: Optional[str] = Field(
        default=None, alias="NotebookInstanceLifecycleConfigNameContains"
    )
    default_code_repository_contains: Optional[str] = Field(
        default=None, alias="DefaultCodeRepositoryContains"
    )
    additional_code_repository_equals: Optional[str] = Field(
        default=None, alias="AdditionalCodeRepositoryEquals"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateModel(
    BaseModel
):
    pipeline_execution_arn: Optional[str] = Field(
        default=None, alias="PipelineExecutionArn"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelineExecutionsRequestListPipelineExecutionsPaginateModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "PipelineExecutionArn"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateModel(
    BaseModel
):
    pipeline_execution_arn: str = Field(alias="PipelineExecutionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipelinesRequestListPipelinesPaginateModel(BaseModel):
    pipeline_name_prefix: Optional[str] = Field(
        default=None, alias="PipelineNamePrefix"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProcessingJobsRequestListProcessingJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpacesRequestListSpacesPaginateModel(BaseModel):
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime"]] = Field(
        default=None, alias="SortBy"
    )
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    space_name_contains: Optional[str] = Field(default=None, alias="SpaceNameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStageDevicesRequestListStageDevicesPaginateModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stage_name: str = Field(alias="StageName")
    exclude_devices_deployed_in_other_stage: Optional[bool] = Field(
        default=None, alias="ExcludeDevicesDeployedInOtherStage"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateModel(
    BaseModel
):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    app_type_equals: Optional[Literal["JupyterServer", "KernelGateway"]] = Field(
        default=None, alias="AppTypeEquals"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeBefore"
    )
    modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedTimeAfter"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsInputListTagsPaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateModel(
    BaseModel
):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[
        Literal["CreationTime", "FinalObjectiveMetricValue", "Name", "Status"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrainingJobsRequestListTrainingJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    warm_pool_status_equals: Optional[
        Literal["Available", "InUse", "Reused", "Terminated"]
    ] = Field(default=None, alias="WarmPoolStatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTransformJobsRequestListTransformJobsPaginateModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    last_modified_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeAfter"
    )
    last_modified_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedTimeBefore"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    status_equals: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="StatusEquals")
    sort_by: Optional[Literal["CreationTime", "Name", "Status"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrialComponentsRequestListTrialComponentsPaginateModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrialsRequestListTrialsPaginateModel(BaseModel):
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    trial_component_name: Optional[str] = Field(
        default=None, alias="TrialComponentName"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    sort_by: Optional[Literal["CreationTime", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserProfilesRequestListUserProfilesPaginateModel(BaseModel):
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["CreationTime", "LastModifiedTime"]] = Field(
        default=None, alias="SortBy"
    )
    domain_id_equals: Optional[str] = Field(default=None, alias="DomainIdEquals")
    user_profile_name_contains: Optional[str] = Field(
        default=None, alias="UserProfileNameContains"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkforcesRequestListWorkforcesPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreateDate", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkteamsRequestListWorkteamsPaginateModel(BaseModel):
    sort_by: Optional[Literal["CreateDate", "Name"]] = Field(
        default=None, alias="SortBy"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchRequestSearchPaginateModel(BaseModel):
    resource: Literal[
        "Endpoint",
        "Experiment",
        "ExperimentTrial",
        "ExperimentTrialComponent",
        "FeatureGroup",
        "FeatureMetadata",
        "HyperParameterTuningJob",
        "Model",
        "ModelCard",
        "ModelPackage",
        "ModelPackageGroup",
        "Pipeline",
        "PipelineExecution",
        "Project",
        "TrainingJob",
    ] = Field(alias="Resource")
    search_expression: Optional[SearchExpressionModel] = Field(
        default=None, alias="SearchExpression"
    )
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataQualityJobDefinitionsResponseModel(BaseModel):
    job_definition_summaries: List[MonitoringJobDefinitionSummaryModel] = Field(
        alias="JobDefinitionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelBiasJobDefinitionsResponseModel(BaseModel):
    job_definition_summaries: List[MonitoringJobDefinitionSummaryModel] = Field(
        alias="JobDefinitionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelExplainabilityJobDefinitionsResponseModel(BaseModel):
    job_definition_summaries: List[MonitoringJobDefinitionSummaryModel] = Field(
        alias="JobDefinitionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelQualityJobDefinitionsResponseModel(BaseModel):
    job_definition_summaries: List[MonitoringJobDefinitionSummaryModel] = Field(
        alias="JobDefinitionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelCardExportJobsResponseModel(BaseModel):
    model_card_export_job_summaries: List[ModelCardExportJobSummaryModel] = Field(
        alias="ModelCardExportJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelCardVersionsResponseModel(BaseModel):
    model_card_version_summary_list: List[ModelCardVersionSummaryModel] = Field(
        alias="ModelCardVersionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelCardsResponseModel(BaseModel):
    model_card_summaries: List[ModelCardSummaryModel] = Field(
        alias="ModelCardSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelMetadataResponseModel(BaseModel):
    model_metadata_summaries: List[ModelMetadataSummaryModel] = Field(
        alias="ModelMetadataSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelPackageGroupsOutputModel(BaseModel):
    model_package_group_summary_list: List[ModelPackageGroupSummaryModel] = Field(
        alias="ModelPackageGroupSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelPackagesOutputModel(BaseModel):
    model_package_summary_list: List[ModelPackageSummaryModel] = Field(
        alias="ModelPackageSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelsOutputModel(BaseModel):
    models: List[ModelSummaryModel] = Field(alias="Models")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMonitoringAlertHistoryResponseModel(BaseModel):
    monitoring_alert_history: List[MonitoringAlertHistorySummaryModel] = Field(
        alias="MonitoringAlertHistory"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMonitoringSchedulesResponseModel(BaseModel):
    monitoring_schedule_summaries: List[MonitoringScheduleSummaryModel] = Field(
        alias="MonitoringScheduleSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotebookInstanceLifecycleConfigsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    notebook_instance_lifecycle_configs: List[
        NotebookInstanceLifecycleConfigSummaryModel
    ] = Field(alias="NotebookInstanceLifecycleConfigs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotebookInstancesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    notebook_instances: List[NotebookInstanceSummaryModel] = Field(
        alias="NotebookInstances"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPipelineExecutionsResponseModel(BaseModel):
    pipeline_execution_summaries: List[PipelineExecutionSummaryModel] = Field(
        alias="PipelineExecutionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPipelineParametersForExecutionResponseModel(BaseModel):
    pipeline_parameters: List[ParameterModel] = Field(alias="PipelineParameters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PipelineExecutionModel(BaseModel):
    pipeline_arn: Optional[str] = Field(default=None, alias="PipelineArn")
    pipeline_execution_arn: Optional[str] = Field(
        default=None, alias="PipelineExecutionArn"
    )
    pipeline_execution_display_name: Optional[str] = Field(
        default=None, alias="PipelineExecutionDisplayName"
    )
    pipeline_execution_status: Optional[
        Literal["Executing", "Failed", "Stopped", "Stopping", "Succeeded"]
    ] = Field(default=None, alias="PipelineExecutionStatus")
    pipeline_execution_description: Optional[str] = Field(
        default=None, alias="PipelineExecutionDescription"
    )
    pipeline_experiment_config: Optional[PipelineExperimentConfigModel] = Field(
        default=None, alias="PipelineExperimentConfig"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )
    pipeline_parameters: Optional[List[ParameterModel]] = Field(
        default=None, alias="PipelineParameters"
    )


class StartPipelineExecutionRequestModel(BaseModel):
    pipeline_name: str = Field(alias="PipelineName")
    client_request_token: str = Field(alias="ClientRequestToken")
    pipeline_execution_display_name: Optional[str] = Field(
        default=None, alias="PipelineExecutionDisplayName"
    )
    pipeline_parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="PipelineParameters"
    )
    pipeline_execution_description: Optional[str] = Field(
        default=None, alias="PipelineExecutionDescription"
    )
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class ListPipelinesResponseModel(BaseModel):
    pipeline_summaries: List[PipelineSummaryModel] = Field(alias="PipelineSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProcessingJobsResponseModel(BaseModel):
    processing_job_summaries: List[ProcessingJobSummaryModel] = Field(
        alias="ProcessingJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsOutputModel(BaseModel):
    project_summary_list: List[ProjectSummaryModel] = Field(alias="ProjectSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSpacesResponseModel(BaseModel):
    spaces: List[SpaceDetailsModel] = Field(alias="Spaces")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudioLifecycleConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    studio_lifecycle_configs: List[StudioLifecycleConfigDetailsModel] = Field(
        alias="StudioLifecycleConfigs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTransformJobsResponseModel(BaseModel):
    transform_job_summaries: List[TransformJobSummaryModel] = Field(
        alias="TransformJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserProfilesResponseModel(BaseModel):
    user_profiles: List[UserProfileDetailsModel] = Field(alias="UserProfiles")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MemberDefinitionModel(BaseModel):
    cognito_member_definition: Optional[CognitoMemberDefinitionModel] = Field(
        default=None, alias="CognitoMemberDefinition"
    )
    oidc_member_definition: Optional[OidcMemberDefinitionModel] = Field(
        default=None, alias="OidcMemberDefinition"
    )


class MonitoringAlertActionsModel(BaseModel):
    model_dashboard_indicator: Optional[ModelDashboardIndicatorActionModel] = Field(
        default=None, alias="ModelDashboardIndicator"
    )


class ModelInfrastructureConfigModel(BaseModel):
    infrastructure_type: Literal["RealTimeInference"] = Field(
        alias="InfrastructureType"
    )
    real_time_inference_config: RealTimeInferenceConfigModel = Field(
        alias="RealTimeInferenceConfig"
    )


class ModelPackageContainerDefinitionModel(BaseModel):
    image: str = Field(alias="Image")
    container_hostname: Optional[str] = Field(default=None, alias="ContainerHostname")
    image_digest: Optional[str] = Field(default=None, alias="ImageDigest")
    model_data_url: Optional[str] = Field(default=None, alias="ModelDataUrl")
    product_id: Optional[str] = Field(default=None, alias="ProductId")
    environment: Optional[Dict[str, str]] = Field(default=None, alias="Environment")
    model_input: Optional[ModelInputModel] = Field(default=None, alias="ModelInput")
    framework: Optional[str] = Field(default=None, alias="Framework")
    framework_version: Optional[str] = Field(default=None, alias="FrameworkVersion")
    nearest_model_name: Optional[str] = Field(default=None, alias="NearestModelName")


class RecommendationJobStoppingConditionsModel(BaseModel):
    max_invocations: Optional[int] = Field(default=None, alias="MaxInvocations")
    model_latency_thresholds: Optional[Sequence[ModelLatencyThresholdModel]] = Field(
        default=None, alias="ModelLatencyThresholds"
    )


class ModelMetadataSearchExpressionModel(BaseModel):
    filters: Optional[Sequence[ModelMetadataFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ModelPackageStatusDetailsModel(BaseModel):
    validation_statuses: List[ModelPackageStatusItemModel] = Field(
        alias="ValidationStatuses"
    )
    image_scan_statuses: Optional[List[ModelPackageStatusItemModel]] = Field(
        default=None, alias="ImageScanStatuses"
    )


class MonitoringResourcesModel(BaseModel):
    cluster_config: MonitoringClusterConfigModel = Field(alias="ClusterConfig")


class MonitoringDatasetFormatModel(BaseModel):
    csv: Optional[MonitoringCsvDatasetFormatModel] = Field(default=None, alias="Csv")
    json_: Optional[MonitoringJsonDatasetFormatModel] = Field(
        default=None, alias="Json"
    )
    parquet: Optional[Mapping[str, Any]] = Field(default=None, alias="Parquet")


class MonitoringOutputModel(BaseModel):
    s3_output: MonitoringS3OutputModel = Field(alias="S3Output")


class OfflineStoreConfigModel(BaseModel):
    s3_storage_config: S3StorageConfigModel = Field(alias="S3StorageConfig")
    disable_glue_table_creation: Optional[bool] = Field(
        default=None, alias="DisableGlueTableCreation"
    )
    data_catalog_config: Optional[DataCatalogConfigModel] = Field(
        default=None, alias="DataCatalogConfig"
    )
    table_format: Optional[Literal["Glue", "Iceberg"]] = Field(
        default=None, alias="TableFormat"
    )


class OnlineStoreConfigModel(BaseModel):
    security_config: Optional[OnlineStoreSecurityConfigModel] = Field(
        default=None, alias="SecurityConfig"
    )
    enable_online_store: Optional[bool] = Field(default=None, alias="EnableOnlineStore")


class OutputConfigModel(BaseModel):
    s3_output_location: str = Field(alias="S3OutputLocation")
    target_device: Optional[
        Literal[
            "aisage",
            "amba_cv2",
            "amba_cv22",
            "amba_cv25",
            "coreml",
            "deeplens",
            "imx8mplus",
            "imx8qm",
            "jacinto_tda4vm",
            "jetson_nano",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_xavier",
            "lambda",
            "ml_c4",
            "ml_c5",
            "ml_eia2",
            "ml_g4dn",
            "ml_inf1",
            "ml_m4",
            "ml_m5",
            "ml_p2",
            "ml_p3",
            "qcs603",
            "qcs605",
            "rasp3b",
            "rk3288",
            "rk3399",
            "sbe_c",
            "sitara_am57x",
            "x86_win32",
            "x86_win64",
        ]
    ] = Field(default=None, alias="TargetDevice")
    target_platform: Optional[TargetPlatformModel] = Field(
        default=None, alias="TargetPlatform"
    )
    compiler_options: Optional[str] = Field(default=None, alias="CompilerOptions")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class PendingProductionVariantSummaryModel(BaseModel):
    variant_name: str = Field(alias="VariantName")
    deployed_images: Optional[List[DeployedImageModel]] = Field(
        default=None, alias="DeployedImages"
    )
    current_weight: Optional[float] = Field(default=None, alias="CurrentWeight")
    desired_weight: Optional[float] = Field(default=None, alias="DesiredWeight")
    current_instance_count: Optional[int] = Field(
        default=None, alias="CurrentInstanceCount"
    )
    desired_instance_count: Optional[int] = Field(
        default=None, alias="DesiredInstanceCount"
    )
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5d.18xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c6g.12xlarge",
            "ml.c6g.16xlarge",
            "ml.c6g.2xlarge",
            "ml.c6g.4xlarge",
            "ml.c6g.8xlarge",
            "ml.c6g.large",
            "ml.c6g.xlarge",
            "ml.c6gd.12xlarge",
            "ml.c6gd.16xlarge",
            "ml.c6gd.2xlarge",
            "ml.c6gd.4xlarge",
            "ml.c6gd.8xlarge",
            "ml.c6gd.large",
            "ml.c6gd.xlarge",
            "ml.c6gn.12xlarge",
            "ml.c6gn.16xlarge",
            "ml.c6gn.2xlarge",
            "ml.c6gn.4xlarge",
            "ml.c6gn.8xlarge",
            "ml.c6gn.large",
            "ml.c6gn.xlarge",
            "ml.c6i.12xlarge",
            "ml.c6i.16xlarge",
            "ml.c6i.24xlarge",
            "ml.c6i.2xlarge",
            "ml.c6i.32xlarge",
            "ml.c6i.4xlarge",
            "ml.c6i.8xlarge",
            "ml.c6i.large",
            "ml.c6i.xlarge",
            "ml.c7g.12xlarge",
            "ml.c7g.16xlarge",
            "ml.c7g.2xlarge",
            "ml.c7g.4xlarge",
            "ml.c7g.8xlarge",
            "ml.c7g.large",
            "ml.c7g.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.inf1.24xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m6g.12xlarge",
            "ml.m6g.16xlarge",
            "ml.m6g.2xlarge",
            "ml.m6g.4xlarge",
            "ml.m6g.8xlarge",
            "ml.m6g.large",
            "ml.m6g.xlarge",
            "ml.m6gd.12xlarge",
            "ml.m6gd.16xlarge",
            "ml.m6gd.2xlarge",
            "ml.m6gd.4xlarge",
            "ml.m6gd.8xlarge",
            "ml.m6gd.large",
            "ml.m6gd.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p4d.24xlarge",
            "ml.p4de.24xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r6g.12xlarge",
            "ml.r6g.16xlarge",
            "ml.r6g.2xlarge",
            "ml.r6g.4xlarge",
            "ml.r6g.8xlarge",
            "ml.r6g.large",
            "ml.r6g.xlarge",
            "ml.r6gd.12xlarge",
            "ml.r6gd.16xlarge",
            "ml.r6gd.2xlarge",
            "ml.r6gd.4xlarge",
            "ml.r6gd.8xlarge",
            "ml.r6gd.large",
            "ml.r6gd.xlarge",
            "ml.t2.2xlarge",
            "ml.t2.large",
            "ml.t2.medium",
            "ml.t2.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    accelerator_type: Optional[
        Literal[
            "ml.eia1.large",
            "ml.eia1.medium",
            "ml.eia1.xlarge",
            "ml.eia2.large",
            "ml.eia2.medium",
            "ml.eia2.xlarge",
        ]
    ] = Field(default=None, alias="AcceleratorType")
    variant_status: Optional[List[ProductionVariantStatusModel]] = Field(
        default=None, alias="VariantStatus"
    )
    current_serverless_config: Optional[ProductionVariantServerlessConfigModel] = Field(
        default=None, alias="CurrentServerlessConfig"
    )
    desired_serverless_config: Optional[ProductionVariantServerlessConfigModel] = Field(
        default=None, alias="DesiredServerlessConfig"
    )


class ProductionVariantSummaryModel(BaseModel):
    variant_name: str = Field(alias="VariantName")
    deployed_images: Optional[List[DeployedImageModel]] = Field(
        default=None, alias="DeployedImages"
    )
    current_weight: Optional[float] = Field(default=None, alias="CurrentWeight")
    desired_weight: Optional[float] = Field(default=None, alias="DesiredWeight")
    current_instance_count: Optional[int] = Field(
        default=None, alias="CurrentInstanceCount"
    )
    desired_instance_count: Optional[int] = Field(
        default=None, alias="DesiredInstanceCount"
    )
    variant_status: Optional[List[ProductionVariantStatusModel]] = Field(
        default=None, alias="VariantStatus"
    )
    current_serverless_config: Optional[ProductionVariantServerlessConfigModel] = Field(
        default=None, alias="CurrentServerlessConfig"
    )
    desired_serverless_config: Optional[ProductionVariantServerlessConfigModel] = Field(
        default=None, alias="DesiredServerlessConfig"
    )


class TrafficPatternModel(BaseModel):
    traffic_type: Optional[Literal["PHASES"]] = Field(default=None, alias="TrafficType")
    phases: Optional[Sequence[PhaseModel]] = Field(default=None, alias="Phases")


class ProcessingResourcesModel(BaseModel):
    cluster_config: ProcessingClusterConfigModel = Field(alias="ClusterConfig")


class ProcessingOutputModel(BaseModel):
    output_name: str = Field(alias="OutputName")
    s3_output: Optional[ProcessingS3OutputModel] = Field(default=None, alias="S3Output")
    feature_store_output: Optional[ProcessingFeatureStoreOutputModel] = Field(
        default=None, alias="FeatureStoreOutput"
    )
    app_managed: Optional[bool] = Field(default=None, alias="AppManaged")


class ProductionVariantModel(BaseModel):
    variant_name: str = Field(alias="VariantName")
    model_name: str = Field(alias="ModelName")
    initial_instance_count: Optional[int] = Field(
        default=None, alias="InitialInstanceCount"
    )
    instance_type: Optional[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5d.18xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c6g.12xlarge",
            "ml.c6g.16xlarge",
            "ml.c6g.2xlarge",
            "ml.c6g.4xlarge",
            "ml.c6g.8xlarge",
            "ml.c6g.large",
            "ml.c6g.xlarge",
            "ml.c6gd.12xlarge",
            "ml.c6gd.16xlarge",
            "ml.c6gd.2xlarge",
            "ml.c6gd.4xlarge",
            "ml.c6gd.8xlarge",
            "ml.c6gd.large",
            "ml.c6gd.xlarge",
            "ml.c6gn.12xlarge",
            "ml.c6gn.16xlarge",
            "ml.c6gn.2xlarge",
            "ml.c6gn.4xlarge",
            "ml.c6gn.8xlarge",
            "ml.c6gn.large",
            "ml.c6gn.xlarge",
            "ml.c6i.12xlarge",
            "ml.c6i.16xlarge",
            "ml.c6i.24xlarge",
            "ml.c6i.2xlarge",
            "ml.c6i.32xlarge",
            "ml.c6i.4xlarge",
            "ml.c6i.8xlarge",
            "ml.c6i.large",
            "ml.c6i.xlarge",
            "ml.c7g.12xlarge",
            "ml.c7g.16xlarge",
            "ml.c7g.2xlarge",
            "ml.c7g.4xlarge",
            "ml.c7g.8xlarge",
            "ml.c7g.large",
            "ml.c7g.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.inf1.24xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m6g.12xlarge",
            "ml.m6g.16xlarge",
            "ml.m6g.2xlarge",
            "ml.m6g.4xlarge",
            "ml.m6g.8xlarge",
            "ml.m6g.large",
            "ml.m6g.xlarge",
            "ml.m6gd.12xlarge",
            "ml.m6gd.16xlarge",
            "ml.m6gd.2xlarge",
            "ml.m6gd.4xlarge",
            "ml.m6gd.8xlarge",
            "ml.m6gd.large",
            "ml.m6gd.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p4d.24xlarge",
            "ml.p4de.24xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r6g.12xlarge",
            "ml.r6g.16xlarge",
            "ml.r6g.2xlarge",
            "ml.r6g.4xlarge",
            "ml.r6g.8xlarge",
            "ml.r6g.large",
            "ml.r6g.xlarge",
            "ml.r6gd.12xlarge",
            "ml.r6gd.16xlarge",
            "ml.r6gd.2xlarge",
            "ml.r6gd.4xlarge",
            "ml.r6gd.8xlarge",
            "ml.r6gd.large",
            "ml.r6gd.xlarge",
            "ml.t2.2xlarge",
            "ml.t2.large",
            "ml.t2.medium",
            "ml.t2.xlarge",
        ]
    ] = Field(default=None, alias="InstanceType")
    initial_variant_weight: Optional[float] = Field(
        default=None, alias="InitialVariantWeight"
    )
    accelerator_type: Optional[
        Literal[
            "ml.eia1.large",
            "ml.eia1.medium",
            "ml.eia1.xlarge",
            "ml.eia2.large",
            "ml.eia2.medium",
            "ml.eia2.xlarge",
        ]
    ] = Field(default=None, alias="AcceleratorType")
    core_dump_config: Optional[ProductionVariantCoreDumpConfigModel] = Field(
        default=None, alias="CoreDumpConfig"
    )
    serverless_config: Optional[ProductionVariantServerlessConfigModel] = Field(
        default=None, alias="ServerlessConfig"
    )
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    model_data_download_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="ModelDataDownloadTimeoutInSeconds"
    )
    container_startup_health_check_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="ContainerStartupHealthCheckTimeoutInSeconds"
    )


class SuggestionQueryModel(BaseModel):
    property_name_query: Optional[PropertyNameQueryModel] = Field(
        default=None, alias="PropertyNameQuery"
    )


class ServiceCatalogProvisioningDetailsModel(BaseModel):
    product_id: str = Field(alias="ProductId")
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    path_id: Optional[str] = Field(default=None, alias="PathId")
    provisioning_parameters: Optional[Sequence[ProvisioningParameterModel]] = Field(
        default=None, alias="ProvisioningParameters"
    )


class ServiceCatalogProvisioningUpdateDetailsModel(BaseModel):
    provisioning_artifact_id: Optional[str] = Field(
        default=None, alias="ProvisioningArtifactId"
    )
    provisioning_parameters: Optional[Sequence[ProvisioningParameterModel]] = Field(
        default=None, alias="ProvisioningParameters"
    )


class PublicWorkforceTaskPriceModel(BaseModel):
    amount_in_usd: Optional[USDModel] = Field(default=None, alias="AmountInUsd")


class QueryLineageRequestModel(BaseModel):
    start_arns: Optional[Sequence[str]] = Field(default=None, alias="StartArns")
    direction: Optional[Literal["Ascendants", "Both", "Descendants"]] = Field(
        default=None, alias="Direction"
    )
    include_edges: Optional[bool] = Field(default=None, alias="IncludeEdges")
    filters: Optional[QueryFiltersModel] = Field(default=None, alias="Filters")
    max_depth: Optional[int] = Field(default=None, alias="MaxDepth")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class QueryLineageResponseModel(BaseModel):
    vertices: List[VertexModel] = Field(alias="Vertices")
    edges: List[EdgeModel] = Field(alias="Edges")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationJobOutputConfigModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    compiled_output_config: Optional[
        RecommendationJobCompiledOutputConfigModel
    ] = Field(default=None, alias="CompiledOutputConfig")


class RecommendationJobContainerConfigModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    task: Optional[str] = Field(default=None, alias="Task")
    framework: Optional[str] = Field(default=None, alias="Framework")
    framework_version: Optional[str] = Field(default=None, alias="FrameworkVersion")
    payload_config: Optional[RecommendationJobPayloadConfigModel] = Field(
        default=None, alias="PayloadConfig"
    )
    nearest_model_name: Optional[str] = Field(default=None, alias="NearestModelName")
    supported_instance_types: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedInstanceTypes"
    )
    data_input_config: Optional[str] = Field(default=None, alias="DataInputConfig")


class RenderUiTemplateRequestModel(BaseModel):
    task: RenderableTaskModel = Field(alias="Task")
    role_arn: str = Field(alias="RoleArn")
    ui_template: Optional[UiTemplateModel] = Field(default=None, alias="UiTemplate")
    human_task_ui_arn: Optional[str] = Field(default=None, alias="HumanTaskUiArn")


class RenderUiTemplateResponseModel(BaseModel):
    rendered_content: str = Field(alias="RenderedContent")
    errors: List[RenderingErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrainingJobRequestModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    profiler_config: Optional[ProfilerConfigForUpdateModel] = Field(
        default=None, alias="ProfilerConfig"
    )
    profiler_rule_configurations: Optional[
        Sequence[ProfilerRuleConfigurationModel]
    ] = Field(default=None, alias="ProfilerRuleConfigurations")
    resource_config: Optional[ResourceConfigForUpdateModel] = Field(
        default=None, alias="ResourceConfig"
    )


class ShadowModeConfigModel(BaseModel):
    source_model_variant_name: str = Field(alias="SourceModelVariantName")
    shadow_model_variants: Sequence[ShadowModelVariantConfigModel] = Field(
        alias="ShadowModelVariants"
    )


class SourceAlgorithmSpecificationModel(BaseModel):
    source_algorithms: Sequence[SourceAlgorithmModel] = Field(alias="SourceAlgorithms")


class TrainingImageConfigModel(BaseModel):
    training_repository_access_mode: Literal["Platform", "Vpc"] = Field(
        alias="TrainingRepositoryAccessMode"
    )
    training_repository_auth_config: Optional[
        TrainingRepositoryAuthConfigModel
    ] = Field(default=None, alias="TrainingRepositoryAuthConfig")


class TransformDataSourceModel(BaseModel):
    s3_data_source: TransformS3DataSourceModel = Field(alias="S3DataSource")


class WorkforceModel(BaseModel):
    workforce_name: str = Field(alias="WorkforceName")
    workforce_arn: str = Field(alias="WorkforceArn")
    last_updated_date: Optional[datetime] = Field(default=None, alias="LastUpdatedDate")
    source_ip_config: Optional[SourceIpConfigModel] = Field(
        default=None, alias="SourceIpConfig"
    )
    sub_domain: Optional[str] = Field(default=None, alias="SubDomain")
    cognito_config: Optional[CognitoConfigModel] = Field(
        default=None, alias="CognitoConfig"
    )
    oidc_config: Optional[OidcConfigForResponseModel] = Field(
        default=None, alias="OidcConfig"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    workforce_vpc_config: Optional[WorkforceVpcConfigResponseModel] = Field(
        default=None, alias="WorkforceVpcConfig"
    )
    status: Optional[
        Literal["Active", "Deleting", "Failed", "Initializing", "Updating"]
    ] = Field(default=None, alias="Status")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class ListActionsResponseModel(BaseModel):
    action_summaries: List[ActionSummaryModel] = Field(alias="ActionSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ArtifactSummaryModel(BaseModel):
    artifact_arn: Optional[str] = Field(default=None, alias="ArtifactArn")
    artifact_name: Optional[str] = Field(default=None, alias="ArtifactName")
    source: Optional[ArtifactSourceModel] = Field(default=None, alias="Source")
    artifact_type: Optional[str] = Field(default=None, alias="ArtifactType")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class CreateArtifactRequestModel(BaseModel):
    source: ArtifactSourceModel = Field(alias="Source")
    artifact_type: str = Field(alias="ArtifactType")
    artifact_name: Optional[str] = Field(default=None, alias="ArtifactName")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DeleteArtifactRequestModel(BaseModel):
    artifact_arn: Optional[str] = Field(default=None, alias="ArtifactArn")
    source: Optional[ArtifactSourceModel] = Field(default=None, alias="Source")


class DescribeArtifactResponseModel(BaseModel):
    artifact_name: str = Field(alias="ArtifactName")
    artifact_arn: str = Field(alias="ArtifactArn")
    source: ArtifactSourceModel = Field(alias="Source")
    artifact_type: str = Field(alias="ArtifactType")
    properties: Dict[str, str] = Field(alias="Properties")
    creation_time: datetime = Field(alias="CreationTime")
    created_by: UserContextModel = Field(alias="CreatedBy")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    metadata_properties: MetadataPropertiesModel = Field(alias="MetadataProperties")
    lineage_group_arn: str = Field(alias="LineageGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociationsResponseModel(BaseModel):
    association_summaries: List[AssociationSummaryModel] = Field(
        alias="AssociationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AsyncInferenceConfigModel(BaseModel):
    output_config: AsyncInferenceOutputConfigModel = Field(alias="OutputConfig")
    client_config: Optional[AsyncInferenceClientConfigModel] = Field(
        default=None, alias="ClientConfig"
    )


class AutoMLChannelModel(BaseModel):
    data_source: AutoMLDataSourceModel = Field(alias="DataSource")
    target_attribute_name: str = Field(alias="TargetAttributeName")
    compression_type: Optional[Literal["Gzip", "None"]] = Field(
        default=None, alias="CompressionType"
    )
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    channel_type: Optional[Literal["training", "validation"]] = Field(
        default=None, alias="ChannelType"
    )


class ListAutoMLJobsResponseModel(BaseModel):
    auto_ml_job_summaries: List[AutoMLJobSummaryModel] = Field(
        alias="AutoMLJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoMLJobConfigModel(BaseModel):
    completion_criteria: Optional[AutoMLJobCompletionCriteriaModel] = Field(
        default=None, alias="CompletionCriteria"
    )
    security_config: Optional[AutoMLSecurityConfigModel] = Field(
        default=None, alias="SecurityConfig"
    )
    data_split_config: Optional[AutoMLDataSplitConfigModel] = Field(
        default=None, alias="DataSplitConfig"
    )
    candidate_generation_config: Optional[AutoMLCandidateGenerationConfigModel] = Field(
        default=None, alias="CandidateGenerationConfig"
    )
    mode: Optional[Literal["AUTO", "ENSEMBLING", "HYPERPARAMETER_TUNING"]] = Field(
        default=None, alias="Mode"
    )


class LabelingJobAlgorithmsConfigModel(BaseModel):
    labeling_job_algorithm_specification_arn: str = Field(
        alias="LabelingJobAlgorithmSpecificationArn"
    )
    initial_active_learning_model_arn: Optional[str] = Field(
        default=None, alias="InitialActiveLearningModelArn"
    )
    labeling_job_resource_config: Optional[LabelingJobResourceConfigModel] = Field(
        default=None, alias="LabelingJobResourceConfig"
    )


class ModelMetricsModel(BaseModel):
    model_quality: Optional[ModelQualityModel] = Field(
        default=None, alias="ModelQuality"
    )
    model_data_quality: Optional[ModelDataQualityModel] = Field(
        default=None, alias="ModelDataQuality"
    )
    bias: Optional[BiasModel] = Field(default=None, alias="Bias")
    explainability: Optional[ExplainabilityModel] = Field(
        default=None, alias="Explainability"
    )


class PipelineExecutionStepMetadataModel(BaseModel):
    training_job: Optional[TrainingJobStepMetadataModel] = Field(
        default=None, alias="TrainingJob"
    )
    processing_job: Optional[ProcessingJobStepMetadataModel] = Field(
        default=None, alias="ProcessingJob"
    )
    transform_job: Optional[TransformJobStepMetadataModel] = Field(
        default=None, alias="TransformJob"
    )
    tuning_job: Optional[TuningJobStepMetaDataModel] = Field(
        default=None, alias="TuningJob"
    )
    model: Optional[ModelStepMetadataModel] = Field(default=None, alias="Model")
    register_model: Optional[RegisterModelStepMetadataModel] = Field(
        default=None, alias="RegisterModel"
    )
    condition: Optional[ConditionStepMetadataModel] = Field(
        default=None, alias="Condition"
    )
    callback: Optional[CallbackStepMetadataModel] = Field(
        default=None, alias="Callback"
    )
    lambda_: Optional[LambdaStepMetadataModel] = Field(default=None, alias="Lambda")
    quality_check: Optional[QualityCheckStepMetadataModel] = Field(
        default=None, alias="QualityCheck"
    )
    clarify_check: Optional[ClarifyCheckStepMetadataModel] = Field(
        default=None, alias="ClarifyCheck"
    )
    emr: Optional[EMRStepMetadataModel] = Field(default=None, alias="EMR")
    fail: Optional[FailStepMetadataModel] = Field(default=None, alias="Fail")
    auto_ml_job: Optional[AutoMLJobStepMetadataModel] = Field(
        default=None, alias="AutoMLJob"
    )


class AutoMLCandidateModel(BaseModel):
    candidate_name: str = Field(alias="CandidateName")
    objective_status: Literal["Failed", "Pending", "Succeeded"] = Field(
        alias="ObjectiveStatus"
    )
    candidate_steps: List[AutoMLCandidateStepModel] = Field(alias="CandidateSteps")
    candidate_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="CandidateStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    final_auto_ml_job_objective_metric: Optional[
        FinalAutoMLJobObjectiveMetricModel
    ] = Field(default=None, alias="FinalAutoMLJobObjectiveMetric")
    inference_containers: Optional[List[AutoMLContainerDefinitionModel]] = Field(
        default=None, alias="InferenceContainers"
    )
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    candidate_properties: Optional[CandidatePropertiesModel] = Field(
        default=None, alias="CandidateProperties"
    )


class BlueGreenUpdatePolicyModel(BaseModel):
    traffic_routing_configuration: TrafficRoutingConfigModel = Field(
        alias="TrafficRoutingConfiguration"
    )
    termination_wait_in_seconds: Optional[int] = Field(
        default=None, alias="TerminationWaitInSeconds"
    )
    maximum_execution_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumExecutionTimeoutInSeconds"
    )


class EndpointInputConfigurationModel(BaseModel):
    instance_type: Literal[
        "ml.c4.2xlarge",
        "ml.c4.4xlarge",
        "ml.c4.8xlarge",
        "ml.c4.large",
        "ml.c4.xlarge",
        "ml.c5.18xlarge",
        "ml.c5.2xlarge",
        "ml.c5.4xlarge",
        "ml.c5.9xlarge",
        "ml.c5.large",
        "ml.c5.xlarge",
        "ml.c5d.18xlarge",
        "ml.c5d.2xlarge",
        "ml.c5d.4xlarge",
        "ml.c5d.9xlarge",
        "ml.c5d.large",
        "ml.c5d.xlarge",
        "ml.c6g.12xlarge",
        "ml.c6g.16xlarge",
        "ml.c6g.2xlarge",
        "ml.c6g.4xlarge",
        "ml.c6g.8xlarge",
        "ml.c6g.large",
        "ml.c6g.xlarge",
        "ml.c6gd.12xlarge",
        "ml.c6gd.16xlarge",
        "ml.c6gd.2xlarge",
        "ml.c6gd.4xlarge",
        "ml.c6gd.8xlarge",
        "ml.c6gd.large",
        "ml.c6gd.xlarge",
        "ml.c6gn.12xlarge",
        "ml.c6gn.16xlarge",
        "ml.c6gn.2xlarge",
        "ml.c6gn.4xlarge",
        "ml.c6gn.8xlarge",
        "ml.c6gn.large",
        "ml.c6gn.xlarge",
        "ml.c6i.12xlarge",
        "ml.c6i.16xlarge",
        "ml.c6i.24xlarge",
        "ml.c6i.2xlarge",
        "ml.c6i.32xlarge",
        "ml.c6i.4xlarge",
        "ml.c6i.8xlarge",
        "ml.c6i.large",
        "ml.c6i.xlarge",
        "ml.c7g.12xlarge",
        "ml.c7g.16xlarge",
        "ml.c7g.2xlarge",
        "ml.c7g.4xlarge",
        "ml.c7g.8xlarge",
        "ml.c7g.large",
        "ml.c7g.xlarge",
        "ml.g4dn.12xlarge",
        "ml.g4dn.16xlarge",
        "ml.g4dn.2xlarge",
        "ml.g4dn.4xlarge",
        "ml.g4dn.8xlarge",
        "ml.g4dn.xlarge",
        "ml.g5.12xlarge",
        "ml.g5.16xlarge",
        "ml.g5.24xlarge",
        "ml.g5.2xlarge",
        "ml.g5.48xlarge",
        "ml.g5.4xlarge",
        "ml.g5.8xlarge",
        "ml.g5.xlarge",
        "ml.inf1.24xlarge",
        "ml.inf1.2xlarge",
        "ml.inf1.6xlarge",
        "ml.inf1.xlarge",
        "ml.m4.10xlarge",
        "ml.m4.16xlarge",
        "ml.m4.2xlarge",
        "ml.m4.4xlarge",
        "ml.m4.xlarge",
        "ml.m5.12xlarge",
        "ml.m5.24xlarge",
        "ml.m5.2xlarge",
        "ml.m5.4xlarge",
        "ml.m5.large",
        "ml.m5.xlarge",
        "ml.m5d.12xlarge",
        "ml.m5d.24xlarge",
        "ml.m5d.2xlarge",
        "ml.m5d.4xlarge",
        "ml.m5d.large",
        "ml.m5d.xlarge",
        "ml.m6g.12xlarge",
        "ml.m6g.16xlarge",
        "ml.m6g.2xlarge",
        "ml.m6g.4xlarge",
        "ml.m6g.8xlarge",
        "ml.m6g.large",
        "ml.m6g.xlarge",
        "ml.m6gd.12xlarge",
        "ml.m6gd.16xlarge",
        "ml.m6gd.2xlarge",
        "ml.m6gd.4xlarge",
        "ml.m6gd.8xlarge",
        "ml.m6gd.large",
        "ml.m6gd.xlarge",
        "ml.p2.16xlarge",
        "ml.p2.8xlarge",
        "ml.p2.xlarge",
        "ml.p3.16xlarge",
        "ml.p3.2xlarge",
        "ml.p3.8xlarge",
        "ml.p4d.24xlarge",
        "ml.p4de.24xlarge",
        "ml.r5.12xlarge",
        "ml.r5.24xlarge",
        "ml.r5.2xlarge",
        "ml.r5.4xlarge",
        "ml.r5.large",
        "ml.r5.xlarge",
        "ml.r5d.12xlarge",
        "ml.r5d.24xlarge",
        "ml.r5d.2xlarge",
        "ml.r5d.4xlarge",
        "ml.r5d.large",
        "ml.r5d.xlarge",
        "ml.r6g.12xlarge",
        "ml.r6g.16xlarge",
        "ml.r6g.2xlarge",
        "ml.r6g.4xlarge",
        "ml.r6g.8xlarge",
        "ml.r6g.large",
        "ml.r6g.xlarge",
        "ml.r6gd.12xlarge",
        "ml.r6gd.16xlarge",
        "ml.r6gd.2xlarge",
        "ml.r6gd.4xlarge",
        "ml.r6gd.8xlarge",
        "ml.r6gd.large",
        "ml.r6gd.xlarge",
        "ml.t2.2xlarge",
        "ml.t2.large",
        "ml.t2.medium",
        "ml.t2.xlarge",
    ] = Field(alias="InstanceType")
    inference_specification_name: Optional[str] = Field(
        default=None, alias="InferenceSpecificationName"
    )
    environment_parameter_ranges: Optional[EnvironmentParameterRangesModel] = Field(
        default=None, alias="EnvironmentParameterRanges"
    )


class ClarifyExplainerConfigModel(BaseModel):
    shap_config: ClarifyShapConfigModel = Field(alias="ShapConfig")
    enable_explanations: Optional[str] = Field(default=None, alias="EnableExplanations")
    inference_config: Optional[ClarifyInferenceConfigModel] = Field(
        default=None, alias="InferenceConfig"
    )


class ListCodeRepositoriesOutputModel(BaseModel):
    code_repository_summary_list: List[CodeRepositorySummaryModel] = Field(
        alias="CodeRepositorySummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContextsResponseModel(BaseModel):
    context_summaries: List[ContextSummaryModel] = Field(alias="ContextSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainSettingsForUpdateModel(BaseModel):
    rstudio_server_pro_domain_settings_for_update: Optional[
        RStudioServerProDomainSettingsForUpdateModel
    ] = Field(default=None, alias="RStudioServerProDomainSettingsForUpdate")
    execution_role_identity_config: Optional[
        Literal["DISABLED", "USER_PROFILE_NAME"]
    ] = Field(default=None, alias="ExecutionRoleIdentityConfig")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class DomainSettingsModel(BaseModel):
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    rstudio_server_pro_domain_settings: Optional[
        RStudioServerProDomainSettingsModel
    ] = Field(default=None, alias="RStudioServerProDomainSettings")
    execution_role_identity_config: Optional[
        Literal["DISABLED", "USER_PROFILE_NAME"]
    ] = Field(default=None, alias="ExecutionRoleIdentityConfig")


class ListInferenceExperimentsResponseModel(BaseModel):
    inference_experiments: List[InferenceExperimentSummaryModel] = Field(
        alias="InferenceExperiments"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefaultSpaceSettingsModel(BaseModel):
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    jupyter_server_app_settings: Optional[JupyterServerAppSettingsModel] = Field(
        default=None, alias="JupyterServerAppSettings"
    )
    kernel_gateway_app_settings: Optional[KernelGatewayAppSettingsModel] = Field(
        default=None, alias="KernelGatewayAppSettings"
    )


class SpaceSettingsModel(BaseModel):
    jupyter_server_app_settings: Optional[JupyterServerAppSettingsModel] = Field(
        default=None, alias="JupyterServerAppSettings"
    )
    kernel_gateway_app_settings: Optional[KernelGatewayAppSettingsModel] = Field(
        default=None, alias="KernelGatewayAppSettings"
    )


class UserSettingsModel(BaseModel):
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    sharing_settings: Optional[SharingSettingsModel] = Field(
        default=None, alias="SharingSettings"
    )
    jupyter_server_app_settings: Optional[JupyterServerAppSettingsModel] = Field(
        default=None, alias="JupyterServerAppSettings"
    )
    kernel_gateway_app_settings: Optional[KernelGatewayAppSettingsModel] = Field(
        default=None, alias="KernelGatewayAppSettings"
    )
    tensor_board_app_settings: Optional[TensorBoardAppSettingsModel] = Field(
        default=None, alias="TensorBoardAppSettings"
    )
    rstudio_server_pro_app_settings: Optional[RStudioServerProAppSettingsModel] = Field(
        default=None, alias="RStudioServerProAppSettings"
    )
    rsession_app_settings: Optional[RSessionAppSettingsModel] = Field(
        default=None, alias="RSessionAppSettings"
    )
    canvas_app_settings: Optional[CanvasAppSettingsModel] = Field(
        default=None, alias="CanvasAppSettings"
    )


class ChannelModel(BaseModel):
    channel_name: str = Field(alias="ChannelName")
    data_source: DataSourceModel = Field(alias="DataSource")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    compression_type: Optional[Literal["Gzip", "None"]] = Field(
        default=None, alias="CompressionType"
    )
    record_wrapper_type: Optional[Literal["None", "RecordIO"]] = Field(
        default=None, alias="RecordWrapperType"
    )
    input_mode: Optional[Literal["FastFile", "File", "Pipe"]] = Field(
        default=None, alias="InputMode"
    )
    shuffle_config: Optional[ShuffleConfigModel] = Field(
        default=None, alias="ShuffleConfig"
    )


class ProcessingInputModel(BaseModel):
    input_name: str = Field(alias="InputName")
    app_managed: Optional[bool] = Field(default=None, alias="AppManaged")
    s3_input: Optional[ProcessingS3InputModel] = Field(default=None, alias="S3Input")
    dataset_definition: Optional[DatasetDefinitionModel] = Field(
        default=None, alias="DatasetDefinition"
    )


class CreateEdgeDeploymentPlanRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    model_configs: Sequence[EdgeDeploymentModelConfigModel] = Field(
        alias="ModelConfigs"
    )
    device_fleet_name: str = Field(alias="DeviceFleetName")
    stages: Optional[Sequence[DeploymentStageModel]] = Field(
        default=None, alias="Stages"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateEdgeDeploymentStageRequestModel(BaseModel):
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    stages: Sequence[DeploymentStageModel] = Field(alias="Stages")


class DescribeEdgeDeploymentPlanResponseModel(BaseModel):
    edge_deployment_plan_arn: str = Field(alias="EdgeDeploymentPlanArn")
    edge_deployment_plan_name: str = Field(alias="EdgeDeploymentPlanName")
    model_configs: List[EdgeDeploymentModelConfigModel] = Field(alias="ModelConfigs")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    edge_deployment_success: int = Field(alias="EdgeDeploymentSuccess")
    edge_deployment_pending: int = Field(alias="EdgeDeploymentPending")
    edge_deployment_failed: int = Field(alias="EdgeDeploymentFailed")
    stages: List[DeploymentStageStatusSummaryModel] = Field(alias="Stages")
    next_token: str = Field(alias="NextToken")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExperimentsResponseModel(BaseModel):
    experiment_summaries: List[ExperimentSummaryModel] = Field(
        alias="ExperimentSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFeatureGroupsResponseModel(BaseModel):
    feature_group_summaries: List[FeatureGroupSummaryModel] = Field(
        alias="FeatureGroupSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrainingJobsResponseModel(BaseModel):
    training_job_summaries: List[TrainingJobSummaryModel] = Field(
        alias="TrainingJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrialModel(BaseModel):
    trial_name: Optional[str] = Field(default=None, alias="TrialName")
    trial_arn: Optional[str] = Field(default=None, alias="TrialArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    experiment_name: Optional[str] = Field(default=None, alias="ExperimentName")
    source: Optional[TrialSourceModel] = Field(default=None, alias="Source")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    trial_component_summaries: Optional[List[TrialComponentSimpleSummaryModel]] = Field(
        default=None, alias="TrialComponentSummaries"
    )


class ListTrialComponentsResponseModel(BaseModel):
    trial_component_summaries: List[TrialComponentSummaryModel] = Field(
        alias="TrialComponentSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrialsResponseModel(BaseModel):
    trial_summaries: List[TrialSummaryModel] = Field(alias="TrialSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesResponseModel(BaseModel):
    device_summaries: List[DeviceSummaryModel] = Field(alias="DeviceSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DriftCheckBaselinesModel(BaseModel):
    bias: Optional[DriftCheckBiasModel] = Field(default=None, alias="Bias")
    explainability: Optional[DriftCheckExplainabilityModel] = Field(
        default=None, alias="Explainability"
    )
    model_quality: Optional[DriftCheckModelQualityModel] = Field(
        default=None, alias="ModelQuality"
    )
    model_data_quality: Optional[DriftCheckModelDataQualityModel] = Field(
        default=None, alias="ModelDataQuality"
    )


class InferenceRecommendationModel(BaseModel):
    metrics: RecommendationMetricsModel = Field(alias="Metrics")
    endpoint_configuration: EndpointOutputConfigurationModel = Field(
        alias="EndpointConfiguration"
    )
    model_configuration: ModelConfigurationModel = Field(alias="ModelConfiguration")
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")


class RecommendationJobInferenceBenchmarkModel(BaseModel):
    model_configuration: ModelConfigurationModel = Field(alias="ModelConfiguration")
    metrics: Optional[RecommendationMetricsModel] = Field(default=None, alias="Metrics")
    endpoint_configuration: Optional[EndpointOutputConfigurationModel] = Field(
        default=None, alias="EndpointConfiguration"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class SearchExpressionModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    nested_filters: Optional[Sequence[NestedFiltersModel]] = Field(
        default=None, alias="NestedFilters"
    )
    sub_expressions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="SubExpressions"
    )
    operator: Optional[Literal["And", "Or"]] = Field(default=None, alias="Operator")


class ListTrainingJobsForHyperParameterTuningJobResponseModel(BaseModel):
    training_job_summaries: List[HyperParameterTrainingJobSummaryModel] = Field(
        alias="TrainingJobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHyperParameterTuningJobsResponseModel(BaseModel):
    hyper_parameter_tuning_job_summaries: List[
        HyperParameterTuningJobSummaryModel
    ] = Field(alias="HyperParameterTuningJobSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerDefinitionModel(BaseModel):
    container_hostname: Optional[str] = Field(default=None, alias="ContainerHostname")
    image: Optional[str] = Field(default=None, alias="Image")
    image_config: Optional[ImageConfigModel] = Field(default=None, alias="ImageConfig")
    mode: Optional[Literal["MultiModel", "SingleModel"]] = Field(
        default=None, alias="Mode"
    )
    model_data_url: Optional[str] = Field(default=None, alias="ModelDataUrl")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")
    model_package_name: Optional[str] = Field(default=None, alias="ModelPackageName")
    inference_specification_name: Optional[str] = Field(
        default=None, alias="InferenceSpecificationName"
    )
    multi_model_config: Optional[MultiModelConfigModel] = Field(
        default=None, alias="MultiModelConfig"
    )


class HyperParameterSpecificationModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["Categorical", "Continuous", "FreeText", "Integer"] = Field(
        alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    range: Optional[ParameterRangeModel] = Field(default=None, alias="Range")
    is_tunable: Optional[bool] = Field(default=None, alias="IsTunable")
    is_required: Optional[bool] = Field(default=None, alias="IsRequired")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class HyperParameterTuningJobConfigModel(BaseModel):
    strategy: Literal["Bayesian", "Grid", "Hyperband", "Random"] = Field(
        alias="Strategy"
    )
    resource_limits: ResourceLimitsModel = Field(alias="ResourceLimits")
    strategy_config: Optional[HyperParameterTuningJobStrategyConfigModel] = Field(
        default=None, alias="StrategyConfig"
    )
    hyper_parameter_tuning_job_objective: Optional[
        HyperParameterTuningJobObjectiveModel
    ] = Field(default=None, alias="HyperParameterTuningJobObjective")
    parameter_ranges: Optional[ParameterRangesModel] = Field(
        default=None, alias="ParameterRanges"
    )
    training_job_early_stopping_type: Optional[Literal["Auto", "Off"]] = Field(
        default=None, alias="TrainingJobEarlyStoppingType"
    )
    tuning_job_completion_criteria: Optional[TuningJobCompletionCriteriaModel] = Field(
        default=None, alias="TuningJobCompletionCriteria"
    )
    random_seed: Optional[int] = Field(default=None, alias="RandomSeed")


class AppImageConfigDetailsModel(BaseModel):
    app_image_config_arn: Optional[str] = Field(default=None, alias="AppImageConfigArn")
    app_image_config_name: Optional[str] = Field(
        default=None, alias="AppImageConfigName"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    kernel_gateway_image_config: Optional[KernelGatewayImageConfigModel] = Field(
        default=None, alias="KernelGatewayImageConfig"
    )


class CreateAppImageConfigRequestModel(BaseModel):
    app_image_config_name: str = Field(alias="AppImageConfigName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kernel_gateway_image_config: Optional[KernelGatewayImageConfigModel] = Field(
        default=None, alias="KernelGatewayImageConfig"
    )


class DescribeAppImageConfigResponseModel(BaseModel):
    app_image_config_arn: str = Field(alias="AppImageConfigArn")
    app_image_config_name: str = Field(alias="AppImageConfigName")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    kernel_gateway_image_config: KernelGatewayImageConfigModel = Field(
        alias="KernelGatewayImageConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppImageConfigRequestModel(BaseModel):
    app_image_config_name: str = Field(alias="AppImageConfigName")
    kernel_gateway_image_config: Optional[KernelGatewayImageConfigModel] = Field(
        default=None, alias="KernelGatewayImageConfig"
    )


class ListLabelingJobsForWorkteamResponseModel(BaseModel):
    labeling_job_summary_list: List[LabelingJobForWorkteamSummaryModel] = Field(
        alias="LabelingJobSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LabelingJobInputConfigModel(BaseModel):
    data_source: LabelingJobDataSourceModel = Field(alias="DataSource")
    data_attributes: Optional[LabelingJobDataAttributesModel] = Field(
        default=None, alias="DataAttributes"
    )


class CreateWorkteamRequestModel(BaseModel):
    workteam_name: str = Field(alias="WorkteamName")
    member_definitions: Sequence[MemberDefinitionModel] = Field(
        alias="MemberDefinitions"
    )
    description: str = Field(alias="Description")
    workforce_name: Optional[str] = Field(default=None, alias="WorkforceName")
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateWorkteamRequestModel(BaseModel):
    workteam_name: str = Field(alias="WorkteamName")
    member_definitions: Optional[Sequence[MemberDefinitionModel]] = Field(
        default=None, alias="MemberDefinitions"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )


class WorkteamModel(BaseModel):
    workteam_name: str = Field(alias="WorkteamName")
    member_definitions: List[MemberDefinitionModel] = Field(alias="MemberDefinitions")
    workteam_arn: str = Field(alias="WorkteamArn")
    description: str = Field(alias="Description")
    workforce_arn: Optional[str] = Field(default=None, alias="WorkforceArn")
    product_listing_ids: Optional[List[str]] = Field(
        default=None, alias="ProductListingIds"
    )
    sub_domain: Optional[str] = Field(default=None, alias="SubDomain")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    last_updated_date: Optional[datetime] = Field(default=None, alias="LastUpdatedDate")
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )


class MonitoringAlertSummaryModel(BaseModel):
    monitoring_alert_name: str = Field(alias="MonitoringAlertName")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    alert_status: Literal["InAlert", "OK"] = Field(alias="AlertStatus")
    datapoints_to_alert: int = Field(alias="DatapointsToAlert")
    evaluation_period: int = Field(alias="EvaluationPeriod")
    actions: MonitoringAlertActionsModel = Field(alias="Actions")


class ModelVariantConfigSummaryModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    variant_name: str = Field(alias="VariantName")
    infrastructure_config: ModelInfrastructureConfigModel = Field(
        alias="InfrastructureConfig"
    )
    status: Literal["Creating", "Deleted", "Deleting", "InService", "Updating"] = Field(
        alias="Status"
    )


class ModelVariantConfigModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    variant_name: str = Field(alias="VariantName")
    infrastructure_config: ModelInfrastructureConfigModel = Field(
        alias="InfrastructureConfig"
    )


class AdditionalInferenceSpecificationDefinitionModel(BaseModel):
    name: str = Field(alias="Name")
    containers: Sequence[ModelPackageContainerDefinitionModel] = Field(
        alias="Containers"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    supported_transform_instance_types: Optional[
        Sequence[
            Literal[
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.c4.xlarge",
                "ml.c5.18xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.p2.16xlarge",
                "ml.p2.8xlarge",
                "ml.p2.xlarge",
                "ml.p3.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
            ]
        ]
    ] = Field(default=None, alias="SupportedTransformInstanceTypes")
    supported_realtime_inference_instance_types: Optional[
        Sequence[
            Literal[
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c5.18xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5d.18xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c6g.12xlarge",
                "ml.c6g.16xlarge",
                "ml.c6g.2xlarge",
                "ml.c6g.4xlarge",
                "ml.c6g.8xlarge",
                "ml.c6g.large",
                "ml.c6g.xlarge",
                "ml.c6gd.12xlarge",
                "ml.c6gd.16xlarge",
                "ml.c6gd.2xlarge",
                "ml.c6gd.4xlarge",
                "ml.c6gd.8xlarge",
                "ml.c6gd.large",
                "ml.c6gd.xlarge",
                "ml.c6gn.12xlarge",
                "ml.c6gn.16xlarge",
                "ml.c6gn.2xlarge",
                "ml.c6gn.4xlarge",
                "ml.c6gn.8xlarge",
                "ml.c6gn.large",
                "ml.c6gn.xlarge",
                "ml.c6i.12xlarge",
                "ml.c6i.16xlarge",
                "ml.c6i.24xlarge",
                "ml.c6i.2xlarge",
                "ml.c6i.32xlarge",
                "ml.c6i.4xlarge",
                "ml.c6i.8xlarge",
                "ml.c6i.large",
                "ml.c6i.xlarge",
                "ml.c7g.12xlarge",
                "ml.c7g.16xlarge",
                "ml.c7g.2xlarge",
                "ml.c7g.4xlarge",
                "ml.c7g.8xlarge",
                "ml.c7g.large",
                "ml.c7g.xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.xlarge",
                "ml.g5.12xlarge",
                "ml.g5.16xlarge",
                "ml.g5.24xlarge",
                "ml.g5.2xlarge",
                "ml.g5.48xlarge",
                "ml.g5.4xlarge",
                "ml.g5.8xlarge",
                "ml.g5.xlarge",
                "ml.inf1.24xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m6g.12xlarge",
                "ml.m6g.16xlarge",
                "ml.m6g.2xlarge",
                "ml.m6g.4xlarge",
                "ml.m6g.8xlarge",
                "ml.m6g.large",
                "ml.m6g.xlarge",
                "ml.m6gd.12xlarge",
                "ml.m6gd.16xlarge",
                "ml.m6gd.2xlarge",
                "ml.m6gd.4xlarge",
                "ml.m6gd.8xlarge",
                "ml.m6gd.large",
                "ml.m6gd.xlarge",
                "ml.p2.16xlarge",
                "ml.p2.8xlarge",
                "ml.p2.xlarge",
                "ml.p3.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p4d.24xlarge",
                "ml.p4de.24xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r6g.12xlarge",
                "ml.r6g.16xlarge",
                "ml.r6g.2xlarge",
                "ml.r6g.4xlarge",
                "ml.r6g.8xlarge",
                "ml.r6g.large",
                "ml.r6g.xlarge",
                "ml.r6gd.12xlarge",
                "ml.r6gd.16xlarge",
                "ml.r6gd.2xlarge",
                "ml.r6gd.4xlarge",
                "ml.r6gd.8xlarge",
                "ml.r6gd.large",
                "ml.r6gd.xlarge",
                "ml.t2.2xlarge",
                "ml.t2.large",
                "ml.t2.medium",
                "ml.t2.xlarge",
            ]
        ]
    ] = Field(default=None, alias="SupportedRealtimeInferenceInstanceTypes")
    supported_content_types: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedContentTypes"
    )
    supported_response_mimetypes: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedResponseMIMETypes"
    )


class InferenceSpecificationModel(BaseModel):
    containers: List[ModelPackageContainerDefinitionModel] = Field(alias="Containers")
    supported_content_types: List[str] = Field(alias="SupportedContentTypes")
    supported_response_mimetypes: List[str] = Field(alias="SupportedResponseMIMETypes")
    supported_transform_instance_types: Optional[
        List[
            Literal[
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.c4.xlarge",
                "ml.c5.18xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.p2.16xlarge",
                "ml.p2.8xlarge",
                "ml.p2.xlarge",
                "ml.p3.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
            ]
        ]
    ] = Field(default=None, alias="SupportedTransformInstanceTypes")
    supported_realtime_inference_instance_types: Optional[
        List[
            Literal[
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c5.18xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5d.18xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c6g.12xlarge",
                "ml.c6g.16xlarge",
                "ml.c6g.2xlarge",
                "ml.c6g.4xlarge",
                "ml.c6g.8xlarge",
                "ml.c6g.large",
                "ml.c6g.xlarge",
                "ml.c6gd.12xlarge",
                "ml.c6gd.16xlarge",
                "ml.c6gd.2xlarge",
                "ml.c6gd.4xlarge",
                "ml.c6gd.8xlarge",
                "ml.c6gd.large",
                "ml.c6gd.xlarge",
                "ml.c6gn.12xlarge",
                "ml.c6gn.16xlarge",
                "ml.c6gn.2xlarge",
                "ml.c6gn.4xlarge",
                "ml.c6gn.8xlarge",
                "ml.c6gn.large",
                "ml.c6gn.xlarge",
                "ml.c6i.12xlarge",
                "ml.c6i.16xlarge",
                "ml.c6i.24xlarge",
                "ml.c6i.2xlarge",
                "ml.c6i.32xlarge",
                "ml.c6i.4xlarge",
                "ml.c6i.8xlarge",
                "ml.c6i.large",
                "ml.c6i.xlarge",
                "ml.c7g.12xlarge",
                "ml.c7g.16xlarge",
                "ml.c7g.2xlarge",
                "ml.c7g.4xlarge",
                "ml.c7g.8xlarge",
                "ml.c7g.large",
                "ml.c7g.xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.xlarge",
                "ml.g5.12xlarge",
                "ml.g5.16xlarge",
                "ml.g5.24xlarge",
                "ml.g5.2xlarge",
                "ml.g5.48xlarge",
                "ml.g5.4xlarge",
                "ml.g5.8xlarge",
                "ml.g5.xlarge",
                "ml.inf1.24xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m6g.12xlarge",
                "ml.m6g.16xlarge",
                "ml.m6g.2xlarge",
                "ml.m6g.4xlarge",
                "ml.m6g.8xlarge",
                "ml.m6g.large",
                "ml.m6g.xlarge",
                "ml.m6gd.12xlarge",
                "ml.m6gd.16xlarge",
                "ml.m6gd.2xlarge",
                "ml.m6gd.4xlarge",
                "ml.m6gd.8xlarge",
                "ml.m6gd.large",
                "ml.m6gd.xlarge",
                "ml.p2.16xlarge",
                "ml.p2.8xlarge",
                "ml.p2.xlarge",
                "ml.p3.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p4d.24xlarge",
                "ml.p4de.24xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r6g.12xlarge",
                "ml.r6g.16xlarge",
                "ml.r6g.2xlarge",
                "ml.r6g.4xlarge",
                "ml.r6g.8xlarge",
                "ml.r6g.large",
                "ml.r6g.xlarge",
                "ml.r6gd.12xlarge",
                "ml.r6gd.16xlarge",
                "ml.r6gd.2xlarge",
                "ml.r6gd.4xlarge",
                "ml.r6gd.8xlarge",
                "ml.r6gd.large",
                "ml.r6gd.xlarge",
                "ml.t2.2xlarge",
                "ml.t2.large",
                "ml.t2.medium",
                "ml.t2.xlarge",
            ]
        ]
    ] = Field(default=None, alias="SupportedRealtimeInferenceInstanceTypes")


class ListModelMetadataRequestListModelMetadataPaginateModel(BaseModel):
    search_expression: Optional[ModelMetadataSearchExpressionModel] = Field(
        default=None, alias="SearchExpression"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelMetadataRequestModel(BaseModel):
    search_expression: Optional[ModelMetadataSearchExpressionModel] = Field(
        default=None, alias="SearchExpression"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchTransformInputModel(BaseModel):
    data_captured_destination_s3_uri: str = Field(alias="DataCapturedDestinationS3Uri")
    dataset_format: MonitoringDatasetFormatModel = Field(alias="DatasetFormat")
    local_path: str = Field(alias="LocalPath")
    s3_input_mode: Optional[Literal["File", "Pipe"]] = Field(
        default=None, alias="S3InputMode"
    )
    s3_data_distribution_type: Optional[
        Literal["FullyReplicated", "ShardedByS3Key"]
    ] = Field(default=None, alias="S3DataDistributionType")
    features_attribute: Optional[str] = Field(default=None, alias="FeaturesAttribute")
    inference_attribute: Optional[str] = Field(default=None, alias="InferenceAttribute")
    probability_attribute: Optional[str] = Field(
        default=None, alias="ProbabilityAttribute"
    )
    probability_threshold_attribute: Optional[float] = Field(
        default=None, alias="ProbabilityThresholdAttribute"
    )
    start_time_offset: Optional[str] = Field(default=None, alias="StartTimeOffset")
    end_time_offset: Optional[str] = Field(default=None, alias="EndTimeOffset")


class MonitoringOutputConfigModel(BaseModel):
    monitoring_outputs: Sequence[MonitoringOutputModel] = Field(
        alias="MonitoringOutputs"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class CreateFeatureGroupRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_feature_name: str = Field(alias="RecordIdentifierFeatureName")
    event_time_feature_name: str = Field(alias="EventTimeFeatureName")
    feature_definitions: Sequence[FeatureDefinitionModel] = Field(
        alias="FeatureDefinitions"
    )
    online_store_config: Optional[OnlineStoreConfigModel] = Field(
        default=None, alias="OnlineStoreConfig"
    )
    offline_store_config: Optional[OfflineStoreConfigModel] = Field(
        default=None, alias="OfflineStoreConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeFeatureGroupResponseModel(BaseModel):
    feature_group_arn: str = Field(alias="FeatureGroupArn")
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_feature_name: str = Field(alias="RecordIdentifierFeatureName")
    event_time_feature_name: str = Field(alias="EventTimeFeatureName")
    feature_definitions: List[FeatureDefinitionModel] = Field(
        alias="FeatureDefinitions"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    online_store_config: OnlineStoreConfigModel = Field(alias="OnlineStoreConfig")
    offline_store_config: OfflineStoreConfigModel = Field(alias="OfflineStoreConfig")
    role_arn: str = Field(alias="RoleArn")
    feature_group_status: Literal[
        "CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"
    ] = Field(alias="FeatureGroupStatus")
    offline_store_status: OfflineStoreStatusModel = Field(alias="OfflineStoreStatus")
    last_update_status: LastUpdateStatusModel = Field(alias="LastUpdateStatus")
    failure_reason: str = Field(alias="FailureReason")
    description: str = Field(alias="Description")
    next_token: str = Field(alias="NextToken")
    online_store_total_size_bytes: int = Field(alias="OnlineStoreTotalSizeBytes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FeatureGroupModel(BaseModel):
    feature_group_arn: Optional[str] = Field(default=None, alias="FeatureGroupArn")
    feature_group_name: Optional[str] = Field(default=None, alias="FeatureGroupName")
    record_identifier_feature_name: Optional[str] = Field(
        default=None, alias="RecordIdentifierFeatureName"
    )
    event_time_feature_name: Optional[str] = Field(
        default=None, alias="EventTimeFeatureName"
    )
    feature_definitions: Optional[List[FeatureDefinitionModel]] = Field(
        default=None, alias="FeatureDefinitions"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    online_store_config: Optional[OnlineStoreConfigModel] = Field(
        default=None, alias="OnlineStoreConfig"
    )
    offline_store_config: Optional[OfflineStoreConfigModel] = Field(
        default=None, alias="OfflineStoreConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    feature_group_status: Optional[
        Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
    ] = Field(default=None, alias="FeatureGroupStatus")
    offline_store_status: Optional[OfflineStoreStatusModel] = Field(
        default=None, alias="OfflineStoreStatus"
    )
    last_update_status: Optional[LastUpdateStatusModel] = Field(
        default=None, alias="LastUpdateStatus"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateCompilationJobRequestModel(BaseModel):
    compilation_job_name: str = Field(alias="CompilationJobName")
    role_arn: str = Field(alias="RoleArn")
    output_config: OutputConfigModel = Field(alias="OutputConfig")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    model_package_version_arn: Optional[str] = Field(
        default=None, alias="ModelPackageVersionArn"
    )
    input_config: Optional[InputConfigModel] = Field(default=None, alias="InputConfig")
    vpc_config: Optional[NeoVpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeCompilationJobResponseModel(BaseModel):
    compilation_job_name: str = Field(alias="CompilationJobName")
    compilation_job_arn: str = Field(alias="CompilationJobArn")
    compilation_job_status: Literal[
        "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
    ] = Field(alias="CompilationJobStatus")
    compilation_start_time: datetime = Field(alias="CompilationStartTime")
    compilation_end_time: datetime = Field(alias="CompilationEndTime")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    inference_image: str = Field(alias="InferenceImage")
    model_package_version_arn: str = Field(alias="ModelPackageVersionArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    model_artifacts: ModelArtifactsModel = Field(alias="ModelArtifacts")
    model_digests: ModelDigestsModel = Field(alias="ModelDigests")
    role_arn: str = Field(alias="RoleArn")
    input_config: InputConfigModel = Field(alias="InputConfig")
    output_config: OutputConfigModel = Field(alias="OutputConfig")
    vpc_config: NeoVpcConfigModel = Field(alias="VpcConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PendingDeploymentSummaryModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    production_variants: Optional[List[PendingProductionVariantSummaryModel]] = Field(
        default=None, alias="ProductionVariants"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    shadow_production_variants: Optional[
        List[PendingProductionVariantSummaryModel]
    ] = Field(default=None, alias="ShadowProductionVariants")


class ProcessingOutputConfigModel(BaseModel):
    outputs: Sequence[ProcessingOutputModel] = Field(alias="Outputs")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class GetSearchSuggestionsRequestModel(BaseModel):
    resource: Literal[
        "Endpoint",
        "Experiment",
        "ExperimentTrial",
        "ExperimentTrialComponent",
        "FeatureGroup",
        "FeatureMetadata",
        "HyperParameterTuningJob",
        "Model",
        "ModelCard",
        "ModelPackage",
        "ModelPackageGroup",
        "Pipeline",
        "PipelineExecution",
        "Project",
        "TrainingJob",
    ] = Field(alias="Resource")
    suggestion_query: Optional[SuggestionQueryModel] = Field(
        default=None, alias="SuggestionQuery"
    )


class CreateProjectInputRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    service_catalog_provisioning_details: ServiceCatalogProvisioningDetailsModel = (
        Field(alias="ServiceCatalogProvisioningDetails")
    )
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeProjectOutputModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    project_name: str = Field(alias="ProjectName")
    project_id: str = Field(alias="ProjectId")
    project_description: str = Field(alias="ProjectDescription")
    service_catalog_provisioning_details: ServiceCatalogProvisioningDetailsModel = (
        Field(alias="ServiceCatalogProvisioningDetails")
    )
    service_catalog_provisioned_product_details: ServiceCatalogProvisionedProductDetailsModel = Field(
        alias="ServiceCatalogProvisionedProductDetails"
    )
    project_status: Literal[
        "CreateCompleted",
        "CreateFailed",
        "CreateInProgress",
        "DeleteCompleted",
        "DeleteFailed",
        "DeleteInProgress",
        "Pending",
        "UpdateCompleted",
        "UpdateFailed",
        "UpdateInProgress",
    ] = Field(alias="ProjectStatus")
    created_by: UserContextModel = Field(alias="CreatedBy")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProjectModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="ProjectArn")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    project_id: Optional[str] = Field(default=None, alias="ProjectId")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    service_catalog_provisioning_details: Optional[
        ServiceCatalogProvisioningDetailsModel
    ] = Field(default=None, alias="ServiceCatalogProvisioningDetails")
    service_catalog_provisioned_product_details: Optional[
        ServiceCatalogProvisionedProductDetailsModel
    ] = Field(default=None, alias="ServiceCatalogProvisionedProductDetails")
    project_status: Optional[
        Literal[
            "CreateCompleted",
            "CreateFailed",
            "CreateInProgress",
            "DeleteCompleted",
            "DeleteFailed",
            "DeleteInProgress",
            "Pending",
            "UpdateCompleted",
            "UpdateFailed",
            "UpdateInProgress",
        ]
    ] = Field(default=None, alias="ProjectStatus")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )


class UpdateProjectInputRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    service_catalog_provisioning_update_details: Optional[
        ServiceCatalogProvisioningUpdateDetailsModel
    ] = Field(default=None, alias="ServiceCatalogProvisioningUpdateDetails")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class HumanLoopConfigModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")
    human_task_ui_arn: str = Field(alias="HumanTaskUiArn")
    task_title: str = Field(alias="TaskTitle")
    task_description: str = Field(alias="TaskDescription")
    task_count: int = Field(alias="TaskCount")
    task_availability_lifetime_in_seconds: Optional[int] = Field(
        default=None, alias="TaskAvailabilityLifetimeInSeconds"
    )
    task_time_limit_in_seconds: Optional[int] = Field(
        default=None, alias="TaskTimeLimitInSeconds"
    )
    task_keywords: Optional[Sequence[str]] = Field(default=None, alias="TaskKeywords")
    public_workforce_task_price: Optional[PublicWorkforceTaskPriceModel] = Field(
        default=None, alias="PublicWorkforceTaskPrice"
    )


class HumanTaskConfigModel(BaseModel):
    workteam_arn: str = Field(alias="WorkteamArn")
    ui_config: UiConfigModel = Field(alias="UiConfig")
    pre_human_task_lambda_arn: str = Field(alias="PreHumanTaskLambdaArn")
    task_title: str = Field(alias="TaskTitle")
    task_description: str = Field(alias="TaskDescription")
    number_of_human_workers_per_data_object: int = Field(
        alias="NumberOfHumanWorkersPerDataObject"
    )
    task_time_limit_in_seconds: int = Field(alias="TaskTimeLimitInSeconds")
    annotation_consolidation_config: AnnotationConsolidationConfigModel = Field(
        alias="AnnotationConsolidationConfig"
    )
    task_keywords: Optional[Sequence[str]] = Field(default=None, alias="TaskKeywords")
    task_availability_lifetime_in_seconds: Optional[int] = Field(
        default=None, alias="TaskAvailabilityLifetimeInSeconds"
    )
    max_concurrent_task_count: Optional[int] = Field(
        default=None, alias="MaxConcurrentTaskCount"
    )
    public_workforce_task_price: Optional[PublicWorkforceTaskPriceModel] = Field(
        default=None, alias="PublicWorkforceTaskPrice"
    )


class AlgorithmSpecificationModel(BaseModel):
    training_input_mode: Literal["FastFile", "File", "Pipe"] = Field(
        alias="TrainingInputMode"
    )
    training_image: Optional[str] = Field(default=None, alias="TrainingImage")
    algorithm_name: Optional[str] = Field(default=None, alias="AlgorithmName")
    metric_definitions: Optional[Sequence[MetricDefinitionModel]] = Field(
        default=None, alias="MetricDefinitions"
    )
    enable_sage_maker_metrics_time_series: Optional[bool] = Field(
        default=None, alias="EnableSageMakerMetricsTimeSeries"
    )
    container_entrypoint: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerEntrypoint"
    )
    container_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="ContainerArguments"
    )
    training_image_config: Optional[TrainingImageConfigModel] = Field(
        default=None, alias="TrainingImageConfig"
    )


class TransformInputModel(BaseModel):
    data_source: TransformDataSourceModel = Field(alias="DataSource")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    compression_type: Optional[Literal["Gzip", "None"]] = Field(
        default=None, alias="CompressionType"
    )
    split_type: Optional[Literal["Line", "None", "RecordIO", "TFRecord"]] = Field(
        default=None, alias="SplitType"
    )


class DescribeWorkforceResponseModel(BaseModel):
    workforce: WorkforceModel = Field(alias="Workforce")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkforcesResponseModel(BaseModel):
    workforces: List[WorkforceModel] = Field(alias="Workforces")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkforceResponseModel(BaseModel):
    workforce: WorkforceModel = Field(alias="Workforce")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListArtifactsResponseModel(BaseModel):
    artifact_summaries: List[ArtifactSummaryModel] = Field(alias="ArtifactSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAutoMLJobRequestModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")
    input_data_config: Sequence[AutoMLChannelModel] = Field(alias="InputDataConfig")
    output_data_config: AutoMLOutputDataConfigModel = Field(alias="OutputDataConfig")
    role_arn: str = Field(alias="RoleArn")
    problem_type: Optional[
        Literal["BinaryClassification", "MulticlassClassification", "Regression"]
    ] = Field(default=None, alias="ProblemType")
    auto_ml_job_objective: Optional[AutoMLJobObjectiveModel] = Field(
        default=None, alias="AutoMLJobObjective"
    )
    auto_ml_job_config: Optional[AutoMLJobConfigModel] = Field(
        default=None, alias="AutoMLJobConfig"
    )
    generate_candidate_definitions_only: Optional[bool] = Field(
        default=None, alias="GenerateCandidateDefinitionsOnly"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    model_deploy_config: Optional[ModelDeployConfigModel] = Field(
        default=None, alias="ModelDeployConfig"
    )


class PipelineExecutionStepModel(BaseModel):
    step_name: Optional[str] = Field(default=None, alias="StepName")
    step_display_name: Optional[str] = Field(default=None, alias="StepDisplayName")
    step_description: Optional[str] = Field(default=None, alias="StepDescription")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    step_status: Optional[
        Literal["Executing", "Failed", "Starting", "Stopped", "Stopping", "Succeeded"]
    ] = Field(default=None, alias="StepStatus")
    cache_hit_result: Optional[CacheHitResultModel] = Field(
        default=None, alias="CacheHitResult"
    )
    attempt_count: Optional[int] = Field(default=None, alias="AttemptCount")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    metadata: Optional[PipelineExecutionStepMetadataModel] = Field(
        default=None, alias="Metadata"
    )


class DescribeAutoMLJobResponseModel(BaseModel):
    auto_ml_job_name: str = Field(alias="AutoMLJobName")
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    input_data_config: List[AutoMLChannelModel] = Field(alias="InputDataConfig")
    output_data_config: AutoMLOutputDataConfigModel = Field(alias="OutputDataConfig")
    role_arn: str = Field(alias="RoleArn")
    auto_ml_job_objective: AutoMLJobObjectiveModel = Field(alias="AutoMLJobObjective")
    problem_type: Literal[
        "BinaryClassification", "MulticlassClassification", "Regression"
    ] = Field(alias="ProblemType")
    auto_ml_job_config: AutoMLJobConfigModel = Field(alias="AutoMLJobConfig")
    creation_time: datetime = Field(alias="CreationTime")
    end_time: datetime = Field(alias="EndTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    partial_failure_reasons: List[AutoMLPartialFailureReasonModel] = Field(
        alias="PartialFailureReasons"
    )
    best_candidate: AutoMLCandidateModel = Field(alias="BestCandidate")
    auto_ml_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="AutoMLJobStatus")
    auto_ml_job_secondary_status: Literal[
        "AnalyzingData",
        "CandidateDefinitionsGenerated",
        "Completed",
        "DeployingModel",
        "ExplainabilityError",
        "Failed",
        "FeatureEngineering",
        "GeneratingExplainabilityReport",
        "GeneratingModelInsightsReport",
        "MaxAutoMLJobRuntimeReached",
        "MaxCandidatesReached",
        "ModelDeploymentError",
        "ModelInsightsError",
        "ModelTuning",
        "Starting",
        "Stopped",
        "Stopping",
    ] = Field(alias="AutoMLJobSecondaryStatus")
    generate_candidate_definitions_only: bool = Field(
        alias="GenerateCandidateDefinitionsOnly"
    )
    auto_ml_job_artifacts: AutoMLJobArtifactsModel = Field(alias="AutoMLJobArtifacts")
    resolved_attributes: ResolvedAttributesModel = Field(alias="ResolvedAttributes")
    model_deploy_config: ModelDeployConfigModel = Field(alias="ModelDeployConfig")
    model_deploy_result: ModelDeployResultModel = Field(alias="ModelDeployResult")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCandidatesForAutoMLJobResponseModel(BaseModel):
    candidates: List[AutoMLCandidateModel] = Field(alias="Candidates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentConfigModel(BaseModel):
    blue_green_update_policy: BlueGreenUpdatePolicyModel = Field(
        alias="BlueGreenUpdatePolicy"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigModel] = Field(
        default=None, alias="AutoRollbackConfiguration"
    )


class RecommendationJobInputConfigModel(BaseModel):
    model_package_version_arn: Optional[str] = Field(
        default=None, alias="ModelPackageVersionArn"
    )
    job_duration_in_seconds: Optional[int] = Field(
        default=None, alias="JobDurationInSeconds"
    )
    traffic_pattern: Optional[TrafficPatternModel] = Field(
        default=None, alias="TrafficPattern"
    )
    resource_limit: Optional[RecommendationJobResourceLimitModel] = Field(
        default=None, alias="ResourceLimit"
    )
    endpoint_configurations: Optional[
        Sequence[EndpointInputConfigurationModel]
    ] = Field(default=None, alias="EndpointConfigurations")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    container_config: Optional[RecommendationJobContainerConfigModel] = Field(
        default=None, alias="ContainerConfig"
    )
    endpoints: Optional[Sequence[EndpointInfoModel]] = Field(
        default=None, alias="Endpoints"
    )
    vpc_config: Optional[RecommendationJobVpcConfigModel] = Field(
        default=None, alias="VpcConfig"
    )
    model_name: Optional[str] = Field(default=None, alias="ModelName")


class ExplainerConfigModel(BaseModel):
    clarify_explainer_config: Optional[ClarifyExplainerConfigModel] = Field(
        default=None, alias="ClarifyExplainerConfig"
    )


class CreateSpaceRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    space_name: str = Field(alias="SpaceName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    space_settings: Optional[SpaceSettingsModel] = Field(
        default=None, alias="SpaceSettings"
    )


class DescribeSpaceResponseModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    space_arn: str = Field(alias="SpaceArn")
    space_name: str = Field(alias="SpaceName")
    home_efs_file_system_uid: str = Field(alias="HomeEfsFileSystemUid")
    status: Literal[
        "Delete_Failed",
        "Deleting",
        "Failed",
        "InService",
        "Pending",
        "Update_Failed",
        "Updating",
    ] = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: str = Field(alias="FailureReason")
    space_settings: SpaceSettingsModel = Field(alias="SpaceSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSpaceRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    space_name: str = Field(alias="SpaceName")
    space_settings: Optional[SpaceSettingsModel] = Field(
        default=None, alias="SpaceSettings"
    )


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    auth_mode: Literal["IAM", "SSO"] = Field(alias="AuthMode")
    default_user_settings: UserSettingsModel = Field(alias="DefaultUserSettings")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    vpc_id: str = Field(alias="VpcId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    app_network_access_type: Optional[Literal["PublicInternetOnly", "VpcOnly"]] = Field(
        default=None, alias="AppNetworkAccessType"
    )
    home_efs_file_system_kms_key_id: Optional[str] = Field(
        default=None, alias="HomeEfsFileSystemKmsKeyId"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    app_security_group_management: Optional[Literal["Customer", "Service"]] = Field(
        default=None, alias="AppSecurityGroupManagement"
    )
    domain_settings: Optional[DomainSettingsModel] = Field(
        default=None, alias="DomainSettings"
    )
    default_space_settings: Optional[DefaultSpaceSettingsModel] = Field(
        default=None, alias="DefaultSpaceSettings"
    )


class CreateUserProfileRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")
    single_sign_on_user_identifier: Optional[str] = Field(
        default=None, alias="SingleSignOnUserIdentifier"
    )
    single_sign_on_user_value: Optional[str] = Field(
        default=None, alias="SingleSignOnUserValue"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    user_settings: Optional[UserSettingsModel] = Field(
        default=None, alias="UserSettings"
    )


class DescribeDomainResponseModel(BaseModel):
    domain_arn: str = Field(alias="DomainArn")
    domain_id: str = Field(alias="DomainId")
    domain_name: str = Field(alias="DomainName")
    home_efs_file_system_id: str = Field(alias="HomeEfsFileSystemId")
    single_sign_on_managed_application_instance_id: str = Field(
        alias="SingleSignOnManagedApplicationInstanceId"
    )
    status: Literal[
        "Delete_Failed",
        "Deleting",
        "Failed",
        "InService",
        "Pending",
        "Update_Failed",
        "Updating",
    ] = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    auth_mode: Literal["IAM", "SSO"] = Field(alias="AuthMode")
    default_user_settings: UserSettingsModel = Field(alias="DefaultUserSettings")
    app_network_access_type: Literal["PublicInternetOnly", "VpcOnly"] = Field(
        alias="AppNetworkAccessType"
    )
    home_efs_file_system_kms_key_id: str = Field(alias="HomeEfsFileSystemKmsKeyId")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    url: str = Field(alias="Url")
    vpc_id: str = Field(alias="VpcId")
    kms_key_id: str = Field(alias="KmsKeyId")
    domain_settings: DomainSettingsModel = Field(alias="DomainSettings")
    app_security_group_management: Literal["Customer", "Service"] = Field(
        alias="AppSecurityGroupManagement"
    )
    security_group_id_for_domain_boundary: str = Field(
        alias="SecurityGroupIdForDomainBoundary"
    )
    default_space_settings: DefaultSpaceSettingsModel = Field(
        alias="DefaultSpaceSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserProfileResponseModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_arn: str = Field(alias="UserProfileArn")
    user_profile_name: str = Field(alias="UserProfileName")
    home_efs_file_system_uid: str = Field(alias="HomeEfsFileSystemUid")
    status: Literal[
        "Delete_Failed",
        "Deleting",
        "Failed",
        "InService",
        "Pending",
        "Update_Failed",
        "Updating",
    ] = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: str = Field(alias="FailureReason")
    single_sign_on_user_identifier: str = Field(alias="SingleSignOnUserIdentifier")
    single_sign_on_user_value: str = Field(alias="SingleSignOnUserValue")
    user_settings: UserSettingsModel = Field(alias="UserSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    default_user_settings: Optional[UserSettingsModel] = Field(
        default=None, alias="DefaultUserSettings"
    )
    domain_settings_for_update: Optional[DomainSettingsForUpdateModel] = Field(
        default=None, alias="DomainSettingsForUpdate"
    )
    default_space_settings: Optional[DefaultSpaceSettingsModel] = Field(
        default=None, alias="DefaultSpaceSettings"
    )
    app_security_group_management: Optional[Literal["Customer", "Service"]] = Field(
        default=None, alias="AppSecurityGroupManagement"
    )


class UpdateUserProfileRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    user_profile_name: str = Field(alias="UserProfileName")
    user_settings: Optional[UserSettingsModel] = Field(
        default=None, alias="UserSettings"
    )


class HyperParameterTrainingJobDefinitionModel(BaseModel):
    algorithm_specification: HyperParameterAlgorithmSpecificationModel = Field(
        alias="AlgorithmSpecification"
    )
    role_arn: str = Field(alias="RoleArn")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    definition_name: Optional[str] = Field(default=None, alias="DefinitionName")
    tuning_objective: Optional[HyperParameterTuningJobObjectiveModel] = Field(
        default=None, alias="TuningObjective"
    )
    hyper_parameter_ranges: Optional[ParameterRangesModel] = Field(
        default=None, alias="HyperParameterRanges"
    )
    static_hyper_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="StaticHyperParameters"
    )
    input_data_config: Optional[Sequence[ChannelModel]] = Field(
        default=None, alias="InputDataConfig"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    resource_config: Optional[ResourceConfigModel] = Field(
        default=None, alias="ResourceConfig"
    )
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    enable_managed_spot_training: Optional[bool] = Field(
        default=None, alias="EnableManagedSpotTraining"
    )
    checkpoint_config: Optional[CheckpointConfigModel] = Field(
        default=None, alias="CheckpointConfig"
    )
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="RetryStrategy"
    )
    hyper_parameter_tuning_resource_config: Optional[
        HyperParameterTuningResourceConfigModel
    ] = Field(default=None, alias="HyperParameterTuningResourceConfig")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class TrainingJobDefinitionModel(BaseModel):
    training_input_mode: Literal["FastFile", "File", "Pipe"] = Field(
        alias="TrainingInputMode"
    )
    input_data_config: Sequence[ChannelModel] = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    resource_config: ResourceConfigModel = Field(alias="ResourceConfig")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    hyper_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="HyperParameters"
    )


class InferenceRecommendationsJobStepModel(BaseModel):
    step_type: Literal["BENCHMARK"] = Field(alias="StepType")
    job_name: str = Field(alias="JobName")
    status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"
    ] = Field(alias="Status")
    inference_benchmark: Optional[RecommendationJobInferenceBenchmarkModel] = Field(
        default=None, alias="InferenceBenchmark"
    )


class CreateModelInputRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    primary_container: Optional[ContainerDefinitionModel] = Field(
        default=None, alias="PrimaryContainer"
    )
    containers: Optional[Sequence[ContainerDefinitionModel]] = Field(
        default=None, alias="Containers"
    )
    inference_execution_config: Optional[InferenceExecutionConfigModel] = Field(
        default=None, alias="InferenceExecutionConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )


class DescribeModelOutputModel(BaseModel):
    model_name: str = Field(alias="ModelName")
    primary_container: ContainerDefinitionModel = Field(alias="PrimaryContainer")
    containers: List[ContainerDefinitionModel] = Field(alias="Containers")
    inference_execution_config: InferenceExecutionConfigModel = Field(
        alias="InferenceExecutionConfig"
    )
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    vpc_config: VpcConfigModel = Field(alias="VpcConfig")
    creation_time: datetime = Field(alias="CreationTime")
    model_arn: str = Field(alias="ModelArn")
    enable_network_isolation: bool = Field(alias="EnableNetworkIsolation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    primary_container: Optional[ContainerDefinitionModel] = Field(
        default=None, alias="PrimaryContainer"
    )
    containers: Optional[List[ContainerDefinitionModel]] = Field(
        default=None, alias="Containers"
    )
    inference_execution_config: Optional[InferenceExecutionConfigModel] = Field(
        default=None, alias="InferenceExecutionConfig"
    )
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class TrainingSpecificationModel(BaseModel):
    training_image: str = Field(alias="TrainingImage")
    supported_training_instance_types: Sequence[
        Literal[
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c4.xlarge",
            "ml.c5.18xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.xlarge",
            "ml.c5n.18xlarge",
            "ml.c5n.2xlarge",
            "ml.c5n.4xlarge",
            "ml.c5n.9xlarge",
            "ml.c5n.xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.xlarge",
            "ml.g5.12xlarge",
            "ml.g5.16xlarge",
            "ml.g5.24xlarge",
            "ml.g5.2xlarge",
            "ml.g5.48xlarge",
            "ml.g5.4xlarge",
            "ml.g5.8xlarge",
            "ml.g5.xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.p2.16xlarge",
            "ml.p2.8xlarge",
            "ml.p2.xlarge",
            "ml.p3.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3dn.24xlarge",
            "ml.p4d.24xlarge",
            "ml.trn1.2xlarge",
            "ml.trn1.32xlarge",
        ]
    ] = Field(alias="SupportedTrainingInstanceTypes")
    training_channels: Sequence[ChannelSpecificationModel] = Field(
        alias="TrainingChannels"
    )
    training_image_digest: Optional[str] = Field(
        default=None, alias="TrainingImageDigest"
    )
    supported_hyper_parameters: Optional[
        Sequence[HyperParameterSpecificationModel]
    ] = Field(default=None, alias="SupportedHyperParameters")
    supports_distributed_training: Optional[bool] = Field(
        default=None, alias="SupportsDistributedTraining"
    )
    metric_definitions: Optional[Sequence[MetricDefinitionModel]] = Field(
        default=None, alias="MetricDefinitions"
    )
    supported_tuning_job_objective_metrics: Optional[
        Sequence[HyperParameterTuningJobObjectiveModel]
    ] = Field(default=None, alias="SupportedTuningJobObjectiveMetrics")


class ListAppImageConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    app_image_configs: List[AppImageConfigDetailsModel] = Field(alias="AppImageConfigs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LabelingJobSummaryModel(BaseModel):
    labeling_job_name: str = Field(alias="LabelingJobName")
    labeling_job_arn: str = Field(alias="LabelingJobArn")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    labeling_job_status: Literal[
        "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
    ] = Field(alias="LabelingJobStatus")
    label_counters: LabelCountersModel = Field(alias="LabelCounters")
    workteam_arn: str = Field(alias="WorkteamArn")
    pre_human_task_lambda_arn: str = Field(alias="PreHumanTaskLambdaArn")
    annotation_consolidation_lambda_arn: Optional[str] = Field(
        default=None, alias="AnnotationConsolidationLambdaArn"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    labeling_job_output: Optional[LabelingJobOutputModel] = Field(
        default=None, alias="LabelingJobOutput"
    )
    input_config: Optional[LabelingJobInputConfigModel] = Field(
        default=None, alias="InputConfig"
    )


class DescribeWorkteamResponseModel(BaseModel):
    workteam: WorkteamModel = Field(alias="Workteam")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkteamsResponseModel(BaseModel):
    workteams: List[WorkteamModel] = Field(alias="Workteams")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkteamResponseModel(BaseModel):
    workteam: WorkteamModel = Field(alias="Workteam")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMonitoringAlertsResponseModel(BaseModel):
    monitoring_alert_summaries: List[MonitoringAlertSummaryModel] = Field(
        alias="MonitoringAlertSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInferenceExperimentResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    type: Literal["ShadowMode"] = Field(alias="Type")
    schedule: InferenceExperimentScheduleModel = Field(alias="Schedule")
    status: Literal[
        "Cancelled",
        "Completed",
        "Created",
        "Creating",
        "Running",
        "Starting",
        "Stopping",
        "Updating",
    ] = Field(alias="Status")
    status_reason: str = Field(alias="StatusReason")
    description: str = Field(alias="Description")
    creation_time: datetime = Field(alias="CreationTime")
    completion_time: datetime = Field(alias="CompletionTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    role_arn: str = Field(alias="RoleArn")
    endpoint_metadata: EndpointMetadataModel = Field(alias="EndpointMetadata")
    model_variants: List[ModelVariantConfigSummaryModel] = Field(alias="ModelVariants")
    data_storage_config: InferenceExperimentDataStorageConfigModel = Field(
        alias="DataStorageConfig"
    )
    shadow_mode_config: ShadowModeConfigModel = Field(alias="ShadowModeConfig")
    kms_key: str = Field(alias="KmsKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["ShadowMode"] = Field(alias="Type")
    role_arn: str = Field(alias="RoleArn")
    endpoint_name: str = Field(alias="EndpointName")
    model_variants: Sequence[ModelVariantConfigModel] = Field(alias="ModelVariants")
    shadow_mode_config: ShadowModeConfigModel = Field(alias="ShadowModeConfig")
    schedule: Optional[InferenceExperimentScheduleModel] = Field(
        default=None, alias="Schedule"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    data_storage_config: Optional[InferenceExperimentDataStorageConfigModel] = Field(
        default=None, alias="DataStorageConfig"
    )
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StopInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    model_variant_actions: Mapping[str, Literal["Promote", "Remove", "Retain"]] = Field(
        alias="ModelVariantActions"
    )
    desired_model_variants: Optional[Sequence[ModelVariantConfigModel]] = Field(
        default=None, alias="DesiredModelVariants"
    )
    desired_state: Optional[Literal["Cancelled", "Completed"]] = Field(
        default=None, alias="DesiredState"
    )
    reason: Optional[str] = Field(default=None, alias="Reason")


class UpdateInferenceExperimentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    schedule: Optional[InferenceExperimentScheduleModel] = Field(
        default=None, alias="Schedule"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    model_variants: Optional[Sequence[ModelVariantConfigModel]] = Field(
        default=None, alias="ModelVariants"
    )
    data_storage_config: Optional[InferenceExperimentDataStorageConfigModel] = Field(
        default=None, alias="DataStorageConfig"
    )
    shadow_mode_config: Optional[ShadowModeConfigModel] = Field(
        default=None, alias="ShadowModeConfig"
    )


class UpdateModelPackageInputRequestModel(BaseModel):
    model_package_arn: str = Field(alias="ModelPackageArn")
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")
    approval_description: Optional[str] = Field(
        default=None, alias="ApprovalDescription"
    )
    customer_metadata_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="CustomerMetadataProperties"
    )
    customer_metadata_properties_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="CustomerMetadataPropertiesToRemove"
    )
    additional_inference_specifications_to_add: Optional[
        Sequence[AdditionalInferenceSpecificationDefinitionModel]
    ] = Field(default=None, alias="AdditionalInferenceSpecificationsToAdd")


class BatchDescribeModelPackageSummaryModel(BaseModel):
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    model_package_arn: str = Field(alias="ModelPackageArn")
    creation_time: datetime = Field(alias="CreationTime")
    inference_specification: InferenceSpecificationModel = Field(
        alias="InferenceSpecification"
    )
    model_package_status: Literal[
        "Completed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="ModelPackageStatus")
    model_package_version: Optional[int] = Field(
        default=None, alias="ModelPackageVersion"
    )
    model_package_description: Optional[str] = Field(
        default=None, alias="ModelPackageDescription"
    )
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")


class DataQualityJobInputModel(BaseModel):
    endpoint_input: Optional[EndpointInputModel] = Field(
        default=None, alias="EndpointInput"
    )
    batch_transform_input: Optional[BatchTransformInputModel] = Field(
        default=None, alias="BatchTransformInput"
    )


class ModelBiasJobInputModel(BaseModel):
    ground_truth_s3_input: MonitoringGroundTruthS3InputModel = Field(
        alias="GroundTruthS3Input"
    )
    endpoint_input: Optional[EndpointInputModel] = Field(
        default=None, alias="EndpointInput"
    )
    batch_transform_input: Optional[BatchTransformInputModel] = Field(
        default=None, alias="BatchTransformInput"
    )


class ModelExplainabilityJobInputModel(BaseModel):
    endpoint_input: Optional[EndpointInputModel] = Field(
        default=None, alias="EndpointInput"
    )
    batch_transform_input: Optional[BatchTransformInputModel] = Field(
        default=None, alias="BatchTransformInput"
    )


class ModelQualityJobInputModel(BaseModel):
    ground_truth_s3_input: MonitoringGroundTruthS3InputModel = Field(
        alias="GroundTruthS3Input"
    )
    endpoint_input: Optional[EndpointInputModel] = Field(
        default=None, alias="EndpointInput"
    )
    batch_transform_input: Optional[BatchTransformInputModel] = Field(
        default=None, alias="BatchTransformInput"
    )


class MonitoringInputModel(BaseModel):
    endpoint_input: Optional[EndpointInputModel] = Field(
        default=None, alias="EndpointInput"
    )
    batch_transform_input: Optional[BatchTransformInputModel] = Field(
        default=None, alias="BatchTransformInput"
    )


class CreateProcessingJobRequestModel(BaseModel):
    processing_job_name: str = Field(alias="ProcessingJobName")
    processing_resources: ProcessingResourcesModel = Field(alias="ProcessingResources")
    app_specification: AppSpecificationModel = Field(alias="AppSpecification")
    role_arn: str = Field(alias="RoleArn")
    processing_inputs: Optional[Sequence[ProcessingInputModel]] = Field(
        default=None, alias="ProcessingInputs"
    )
    processing_output_config: Optional[ProcessingOutputConfigModel] = Field(
        default=None, alias="ProcessingOutputConfig"
    )
    stopping_condition: Optional[ProcessingStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")
    network_config: Optional[NetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )


class DescribeProcessingJobResponseModel(BaseModel):
    processing_inputs: List[ProcessingInputModel] = Field(alias="ProcessingInputs")
    processing_output_config: ProcessingOutputConfigModel = Field(
        alias="ProcessingOutputConfig"
    )
    processing_job_name: str = Field(alias="ProcessingJobName")
    processing_resources: ProcessingResourcesModel = Field(alias="ProcessingResources")
    stopping_condition: ProcessingStoppingConditionModel = Field(
        alias="StoppingCondition"
    )
    app_specification: AppSpecificationModel = Field(alias="AppSpecification")
    environment: Dict[str, str] = Field(alias="Environment")
    network_config: NetworkConfigModel = Field(alias="NetworkConfig")
    role_arn: str = Field(alias="RoleArn")
    experiment_config: ExperimentConfigModel = Field(alias="ExperimentConfig")
    processing_job_arn: str = Field(alias="ProcessingJobArn")
    processing_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="ProcessingJobStatus")
    exit_message: str = Field(alias="ExitMessage")
    failure_reason: str = Field(alias="FailureReason")
    processing_end_time: datetime = Field(alias="ProcessingEndTime")
    processing_start_time: datetime = Field(alias="ProcessingStartTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    creation_time: datetime = Field(alias="CreationTime")
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    training_job_arn: str = Field(alias="TrainingJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProcessingJobModel(BaseModel):
    processing_inputs: Optional[List[ProcessingInputModel]] = Field(
        default=None, alias="ProcessingInputs"
    )
    processing_output_config: Optional[ProcessingOutputConfigModel] = Field(
        default=None, alias="ProcessingOutputConfig"
    )
    processing_job_name: Optional[str] = Field(default=None, alias="ProcessingJobName")
    processing_resources: Optional[ProcessingResourcesModel] = Field(
        default=None, alias="ProcessingResources"
    )
    stopping_condition: Optional[ProcessingStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    app_specification: Optional[AppSpecificationModel] = Field(
        default=None, alias="AppSpecification"
    )
    environment: Optional[Dict[str, str]] = Field(default=None, alias="Environment")
    network_config: Optional[NetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )
    processing_job_arn: Optional[str] = Field(default=None, alias="ProcessingJobArn")
    processing_job_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="ProcessingJobStatus")
    exit_message: Optional[str] = Field(default=None, alias="ExitMessage")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    processing_end_time: Optional[datetime] = Field(
        default=None, alias="ProcessingEndTime"
    )
    processing_start_time: Optional[datetime] = Field(
        default=None, alias="ProcessingStartTime"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    monitoring_schedule_arn: Optional[str] = Field(
        default=None, alias="MonitoringScheduleArn"
    )
    auto_ml_job_arn: Optional[str] = Field(default=None, alias="AutoMLJobArn")
    training_job_arn: Optional[str] = Field(default=None, alias="TrainingJobArn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateFlowDefinitionRequestModel(BaseModel):
    flow_definition_name: str = Field(alias="FlowDefinitionName")
    human_loop_config: HumanLoopConfigModel = Field(alias="HumanLoopConfig")
    output_config: FlowDefinitionOutputConfigModel = Field(alias="OutputConfig")
    role_arn: str = Field(alias="RoleArn")
    human_loop_request_source: Optional[HumanLoopRequestSourceModel] = Field(
        default=None, alias="HumanLoopRequestSource"
    )
    human_loop_activation_config: Optional[HumanLoopActivationConfigModel] = Field(
        default=None, alias="HumanLoopActivationConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeFlowDefinitionResponseModel(BaseModel):
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    flow_definition_name: str = Field(alias="FlowDefinitionName")
    flow_definition_status: Literal[
        "Active", "Deleting", "Failed", "Initializing"
    ] = Field(alias="FlowDefinitionStatus")
    creation_time: datetime = Field(alias="CreationTime")
    human_loop_request_source: HumanLoopRequestSourceModel = Field(
        alias="HumanLoopRequestSource"
    )
    human_loop_activation_config: HumanLoopActivationConfigModel = Field(
        alias="HumanLoopActivationConfig"
    )
    human_loop_config: HumanLoopConfigModel = Field(alias="HumanLoopConfig")
    output_config: FlowDefinitionOutputConfigModel = Field(alias="OutputConfig")
    role_arn: str = Field(alias="RoleArn")
    failure_reason: str = Field(alias="FailureReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLabelingJobRequestModel(BaseModel):
    labeling_job_name: str = Field(alias="LabelingJobName")
    label_attribute_name: str = Field(alias="LabelAttributeName")
    input_config: LabelingJobInputConfigModel = Field(alias="InputConfig")
    output_config: LabelingJobOutputConfigModel = Field(alias="OutputConfig")
    role_arn: str = Field(alias="RoleArn")
    human_task_config: HumanTaskConfigModel = Field(alias="HumanTaskConfig")
    label_category_config_s3_uri: Optional[str] = Field(
        default=None, alias="LabelCategoryConfigS3Uri"
    )
    stopping_conditions: Optional[LabelingJobStoppingConditionsModel] = Field(
        default=None, alias="StoppingConditions"
    )
    labeling_job_algorithms_config: Optional[LabelingJobAlgorithmsConfigModel] = Field(
        default=None, alias="LabelingJobAlgorithmsConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeLabelingJobResponseModel(BaseModel):
    labeling_job_status: Literal[
        "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
    ] = Field(alias="LabelingJobStatus")
    label_counters: LabelCountersModel = Field(alias="LabelCounters")
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    job_reference_code: str = Field(alias="JobReferenceCode")
    labeling_job_name: str = Field(alias="LabelingJobName")
    labeling_job_arn: str = Field(alias="LabelingJobArn")
    label_attribute_name: str = Field(alias="LabelAttributeName")
    input_config: LabelingJobInputConfigModel = Field(alias="InputConfig")
    output_config: LabelingJobOutputConfigModel = Field(alias="OutputConfig")
    role_arn: str = Field(alias="RoleArn")
    label_category_config_s3_uri: str = Field(alias="LabelCategoryConfigS3Uri")
    stopping_conditions: LabelingJobStoppingConditionsModel = Field(
        alias="StoppingConditions"
    )
    labeling_job_algorithms_config: LabelingJobAlgorithmsConfigModel = Field(
        alias="LabelingJobAlgorithmsConfig"
    )
    human_task_config: HumanTaskConfigModel = Field(alias="HumanTaskConfig")
    tags: List[TagModel] = Field(alias="Tags")
    labeling_job_output: LabelingJobOutputModel = Field(alias="LabelingJobOutput")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrainingJobRequestModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    algorithm_specification: AlgorithmSpecificationModel = Field(
        alias="AlgorithmSpecification"
    )
    role_arn: str = Field(alias="RoleArn")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    resource_config: ResourceConfigModel = Field(alias="ResourceConfig")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    hyper_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="HyperParameters"
    )
    input_data_config: Optional[Sequence[ChannelModel]] = Field(
        default=None, alias="InputDataConfig"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    enable_managed_spot_training: Optional[bool] = Field(
        default=None, alias="EnableManagedSpotTraining"
    )
    checkpoint_config: Optional[CheckpointConfigModel] = Field(
        default=None, alias="CheckpointConfig"
    )
    debug_hook_config: Optional[DebugHookConfigModel] = Field(
        default=None, alias="DebugHookConfig"
    )
    debug_rule_configurations: Optional[Sequence[DebugRuleConfigurationModel]] = Field(
        default=None, alias="DebugRuleConfigurations"
    )
    tensor_board_output_config: Optional[TensorBoardOutputConfigModel] = Field(
        default=None, alias="TensorBoardOutputConfig"
    )
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )
    profiler_config: Optional[ProfilerConfigModel] = Field(
        default=None, alias="ProfilerConfig"
    )
    profiler_rule_configurations: Optional[
        Sequence[ProfilerRuleConfigurationModel]
    ] = Field(default=None, alias="ProfilerRuleConfigurations")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="RetryStrategy"
    )


class DescribeTrainingJobResponseModel(BaseModel):
    training_job_name: str = Field(alias="TrainingJobName")
    training_job_arn: str = Field(alias="TrainingJobArn")
    tuning_job_arn: str = Field(alias="TuningJobArn")
    labeling_job_arn: str = Field(alias="LabelingJobArn")
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    model_artifacts: ModelArtifactsModel = Field(alias="ModelArtifacts")
    training_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="TrainingJobStatus")
    secondary_status: Literal[
        "Completed",
        "Downloading",
        "DownloadingTrainingImage",
        "Failed",
        "Interrupted",
        "LaunchingMLInstances",
        "MaxRuntimeExceeded",
        "MaxWaitTimeExceeded",
        "PreparingTrainingStack",
        "Restarting",
        "Starting",
        "Stopped",
        "Stopping",
        "Training",
        "Updating",
        "Uploading",
    ] = Field(alias="SecondaryStatus")
    failure_reason: str = Field(alias="FailureReason")
    hyper_parameters: Dict[str, str] = Field(alias="HyperParameters")
    algorithm_specification: AlgorithmSpecificationModel = Field(
        alias="AlgorithmSpecification"
    )
    role_arn: str = Field(alias="RoleArn")
    input_data_config: List[ChannelModel] = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    resource_config: ResourceConfigModel = Field(alias="ResourceConfig")
    vpc_config: VpcConfigModel = Field(alias="VpcConfig")
    stopping_condition: StoppingConditionModel = Field(alias="StoppingCondition")
    creation_time: datetime = Field(alias="CreationTime")
    training_start_time: datetime = Field(alias="TrainingStartTime")
    training_end_time: datetime = Field(alias="TrainingEndTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    secondary_status_transitions: List[SecondaryStatusTransitionModel] = Field(
        alias="SecondaryStatusTransitions"
    )
    final_metric_data_list: List[MetricDataModel] = Field(alias="FinalMetricDataList")
    enable_network_isolation: bool = Field(alias="EnableNetworkIsolation")
    enable_inter_container_traffic_encryption: bool = Field(
        alias="EnableInterContainerTrafficEncryption"
    )
    enable_managed_spot_training: bool = Field(alias="EnableManagedSpotTraining")
    checkpoint_config: CheckpointConfigModel = Field(alias="CheckpointConfig")
    training_time_in_seconds: int = Field(alias="TrainingTimeInSeconds")
    billable_time_in_seconds: int = Field(alias="BillableTimeInSeconds")
    debug_hook_config: DebugHookConfigModel = Field(alias="DebugHookConfig")
    experiment_config: ExperimentConfigModel = Field(alias="ExperimentConfig")
    debug_rule_configurations: List[DebugRuleConfigurationModel] = Field(
        alias="DebugRuleConfigurations"
    )
    tensor_board_output_config: TensorBoardOutputConfigModel = Field(
        alias="TensorBoardOutputConfig"
    )
    debug_rule_evaluation_statuses: List[DebugRuleEvaluationStatusModel] = Field(
        alias="DebugRuleEvaluationStatuses"
    )
    profiler_config: ProfilerConfigModel = Field(alias="ProfilerConfig")
    profiler_rule_configurations: List[ProfilerRuleConfigurationModel] = Field(
        alias="ProfilerRuleConfigurations"
    )
    profiler_rule_evaluation_statuses: List[ProfilerRuleEvaluationStatusModel] = Field(
        alias="ProfilerRuleEvaluationStatuses"
    )
    profiling_status: Literal["Disabled", "Enabled"] = Field(alias="ProfilingStatus")
    retry_strategy: RetryStrategyModel = Field(alias="RetryStrategy")
    environment: Dict[str, str] = Field(alias="Environment")
    warm_pool_status: WarmPoolStatusModel = Field(alias="WarmPoolStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrainingJobModel(BaseModel):
    training_job_name: Optional[str] = Field(default=None, alias="TrainingJobName")
    training_job_arn: Optional[str] = Field(default=None, alias="TrainingJobArn")
    tuning_job_arn: Optional[str] = Field(default=None, alias="TuningJobArn")
    labeling_job_arn: Optional[str] = Field(default=None, alias="LabelingJobArn")
    auto_ml_job_arn: Optional[str] = Field(default=None, alias="AutoMLJobArn")
    model_artifacts: Optional[ModelArtifactsModel] = Field(
        default=None, alias="ModelArtifacts"
    )
    training_job_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="TrainingJobStatus")
    secondary_status: Optional[
        Literal[
            "Completed",
            "Downloading",
            "DownloadingTrainingImage",
            "Failed",
            "Interrupted",
            "LaunchingMLInstances",
            "MaxRuntimeExceeded",
            "MaxWaitTimeExceeded",
            "PreparingTrainingStack",
            "Restarting",
            "Starting",
            "Stopped",
            "Stopping",
            "Training",
            "Updating",
            "Uploading",
        ]
    ] = Field(default=None, alias="SecondaryStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    hyper_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="HyperParameters"
    )
    algorithm_specification: Optional[AlgorithmSpecificationModel] = Field(
        default=None, alias="AlgorithmSpecification"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    input_data_config: Optional[List[ChannelModel]] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    resource_config: Optional[ResourceConfigModel] = Field(
        default=None, alias="ResourceConfig"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    stopping_condition: Optional[StoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    training_start_time: Optional[datetime] = Field(
        default=None, alias="TrainingStartTime"
    )
    training_end_time: Optional[datetime] = Field(default=None, alias="TrainingEndTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    secondary_status_transitions: Optional[
        List[SecondaryStatusTransitionModel]
    ] = Field(default=None, alias="SecondaryStatusTransitions")
    final_metric_data_list: Optional[List[MetricDataModel]] = Field(
        default=None, alias="FinalMetricDataList"
    )
    enable_network_isolation: Optional[bool] = Field(
        default=None, alias="EnableNetworkIsolation"
    )
    enable_inter_container_traffic_encryption: Optional[bool] = Field(
        default=None, alias="EnableInterContainerTrafficEncryption"
    )
    enable_managed_spot_training: Optional[bool] = Field(
        default=None, alias="EnableManagedSpotTraining"
    )
    checkpoint_config: Optional[CheckpointConfigModel] = Field(
        default=None, alias="CheckpointConfig"
    )
    training_time_in_seconds: Optional[int] = Field(
        default=None, alias="TrainingTimeInSeconds"
    )
    billable_time_in_seconds: Optional[int] = Field(
        default=None, alias="BillableTimeInSeconds"
    )
    debug_hook_config: Optional[DebugHookConfigModel] = Field(
        default=None, alias="DebugHookConfig"
    )
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )
    debug_rule_configurations: Optional[List[DebugRuleConfigurationModel]] = Field(
        default=None, alias="DebugRuleConfigurations"
    )
    tensor_board_output_config: Optional[TensorBoardOutputConfigModel] = Field(
        default=None, alias="TensorBoardOutputConfig"
    )
    debug_rule_evaluation_statuses: Optional[
        List[DebugRuleEvaluationStatusModel]
    ] = Field(default=None, alias="DebugRuleEvaluationStatuses")
    environment: Optional[Dict[str, str]] = Field(default=None, alias="Environment")
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="RetryStrategy"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateTransformJobRequestModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")
    model_name: str = Field(alias="ModelName")
    transform_input: TransformInputModel = Field(alias="TransformInput")
    transform_output: TransformOutputModel = Field(alias="TransformOutput")
    transform_resources: TransformResourcesModel = Field(alias="TransformResources")
    max_concurrent_transforms: Optional[int] = Field(
        default=None, alias="MaxConcurrentTransforms"
    )
    model_client_config: Optional[ModelClientConfigModel] = Field(
        default=None, alias="ModelClientConfig"
    )
    max_payload_in_mb: Optional[int] = Field(default=None, alias="MaxPayloadInMB")
    batch_strategy: Optional[Literal["MultiRecord", "SingleRecord"]] = Field(
        default=None, alias="BatchStrategy"
    )
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")
    data_capture_config: Optional[BatchDataCaptureConfigModel] = Field(
        default=None, alias="DataCaptureConfig"
    )
    data_processing: Optional[DataProcessingModel] = Field(
        default=None, alias="DataProcessing"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )


class DescribeTransformJobResponseModel(BaseModel):
    transform_job_name: str = Field(alias="TransformJobName")
    transform_job_arn: str = Field(alias="TransformJobArn")
    transform_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="TransformJobStatus")
    failure_reason: str = Field(alias="FailureReason")
    model_name: str = Field(alias="ModelName")
    max_concurrent_transforms: int = Field(alias="MaxConcurrentTransforms")
    model_client_config: ModelClientConfigModel = Field(alias="ModelClientConfig")
    max_payload_in_mb: int = Field(alias="MaxPayloadInMB")
    batch_strategy: Literal["MultiRecord", "SingleRecord"] = Field(
        alias="BatchStrategy"
    )
    environment: Dict[str, str] = Field(alias="Environment")
    transform_input: TransformInputModel = Field(alias="TransformInput")
    transform_output: TransformOutputModel = Field(alias="TransformOutput")
    data_capture_config: BatchDataCaptureConfigModel = Field(alias="DataCaptureConfig")
    transform_resources: TransformResourcesModel = Field(alias="TransformResources")
    creation_time: datetime = Field(alias="CreationTime")
    transform_start_time: datetime = Field(alias="TransformStartTime")
    transform_end_time: datetime = Field(alias="TransformEndTime")
    labeling_job_arn: str = Field(alias="LabelingJobArn")
    auto_ml_job_arn: str = Field(alias="AutoMLJobArn")
    data_processing: DataProcessingModel = Field(alias="DataProcessing")
    experiment_config: ExperimentConfigModel = Field(alias="ExperimentConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransformJobDefinitionModel(BaseModel):
    transform_input: TransformInputModel = Field(alias="TransformInput")
    transform_output: TransformOutputModel = Field(alias="TransformOutput")
    transform_resources: TransformResourcesModel = Field(alias="TransformResources")
    max_concurrent_transforms: Optional[int] = Field(
        default=None, alias="MaxConcurrentTransforms"
    )
    max_payload_in_mb: Optional[int] = Field(default=None, alias="MaxPayloadInMB")
    batch_strategy: Optional[Literal["MultiRecord", "SingleRecord"]] = Field(
        default=None, alias="BatchStrategy"
    )
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")


class TransformJobModel(BaseModel):
    transform_job_name: Optional[str] = Field(default=None, alias="TransformJobName")
    transform_job_arn: Optional[str] = Field(default=None, alias="TransformJobArn")
    transform_job_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="TransformJobStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    max_concurrent_transforms: Optional[int] = Field(
        default=None, alias="MaxConcurrentTransforms"
    )
    model_client_config: Optional[ModelClientConfigModel] = Field(
        default=None, alias="ModelClientConfig"
    )
    max_payload_in_mb: Optional[int] = Field(default=None, alias="MaxPayloadInMB")
    batch_strategy: Optional[Literal["MultiRecord", "SingleRecord"]] = Field(
        default=None, alias="BatchStrategy"
    )
    environment: Optional[Dict[str, str]] = Field(default=None, alias="Environment")
    transform_input: Optional[TransformInputModel] = Field(
        default=None, alias="TransformInput"
    )
    transform_output: Optional[TransformOutputModel] = Field(
        default=None, alias="TransformOutput"
    )
    transform_resources: Optional[TransformResourcesModel] = Field(
        default=None, alias="TransformResources"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    transform_start_time: Optional[datetime] = Field(
        default=None, alias="TransformStartTime"
    )
    transform_end_time: Optional[datetime] = Field(
        default=None, alias="TransformEndTime"
    )
    labeling_job_arn: Optional[str] = Field(default=None, alias="LabelingJobArn")
    auto_ml_job_arn: Optional[str] = Field(default=None, alias="AutoMLJobArn")
    data_processing: Optional[DataProcessingModel] = Field(
        default=None, alias="DataProcessing"
    )
    experiment_config: Optional[ExperimentConfigModel] = Field(
        default=None, alias="ExperimentConfig"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListPipelineExecutionStepsResponseModel(BaseModel):
    pipeline_execution_steps: List[PipelineExecutionStepModel] = Field(
        alias="PipelineExecutionSteps"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    deployment_config: Optional[DeploymentConfigModel] = Field(
        default=None, alias="DeploymentConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateEndpointInputRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    retain_all_variant_properties: Optional[bool] = Field(
        default=None, alias="RetainAllVariantProperties"
    )
    exclude_retained_variant_properties: Optional[
        Sequence[VariantPropertyModel]
    ] = Field(default=None, alias="ExcludeRetainedVariantProperties")
    deployment_config: Optional[DeploymentConfigModel] = Field(
        default=None, alias="DeploymentConfig"
    )
    retain_deployment_config: Optional[bool] = Field(
        default=None, alias="RetainDeploymentConfig"
    )


class CreateInferenceRecommendationsJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_type: Literal["Advanced", "Default"] = Field(alias="JobType")
    role_arn: str = Field(alias="RoleArn")
    input_config: RecommendationJobInputConfigModel = Field(alias="InputConfig")
    job_description: Optional[str] = Field(default=None, alias="JobDescription")
    stopping_conditions: Optional[RecommendationJobStoppingConditionsModel] = Field(
        default=None, alias="StoppingConditions"
    )
    output_config: Optional[RecommendationJobOutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeInferenceRecommendationsJobResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_description: str = Field(alias="JobDescription")
    job_type: Literal["Advanced", "Default"] = Field(alias="JobType")
    job_arn: str = Field(alias="JobArn")
    role_arn: str = Field(alias="RoleArn")
    status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "STOPPED", "STOPPING"
    ] = Field(alias="Status")
    creation_time: datetime = Field(alias="CreationTime")
    completion_time: datetime = Field(alias="CompletionTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    input_config: RecommendationJobInputConfigModel = Field(alias="InputConfig")
    stopping_conditions: RecommendationJobStoppingConditionsModel = Field(
        alias="StoppingConditions"
    )
    inference_recommendations: List[InferenceRecommendationModel] = Field(
        alias="InferenceRecommendations"
    )
    endpoint_performances: List[EndpointPerformanceModel] = Field(
        alias="EndpointPerformances"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointConfigInputRequestModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    production_variants: Sequence[ProductionVariantModel] = Field(
        alias="ProductionVariants"
    )
    data_capture_config: Optional[DataCaptureConfigModel] = Field(
        default=None, alias="DataCaptureConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    async_inference_config: Optional[AsyncInferenceConfigModel] = Field(
        default=None, alias="AsyncInferenceConfig"
    )
    explainer_config: Optional[ExplainerConfigModel] = Field(
        default=None, alias="ExplainerConfig"
    )
    shadow_production_variants: Optional[Sequence[ProductionVariantModel]] = Field(
        default=None, alias="ShadowProductionVariants"
    )


class DescribeEndpointConfigOutputModel(BaseModel):
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    endpoint_config_arn: str = Field(alias="EndpointConfigArn")
    production_variants: List[ProductionVariantModel] = Field(
        alias="ProductionVariants"
    )
    data_capture_config: DataCaptureConfigModel = Field(alias="DataCaptureConfig")
    kms_key_id: str = Field(alias="KmsKeyId")
    creation_time: datetime = Field(alias="CreationTime")
    async_inference_config: AsyncInferenceConfigModel = Field(
        alias="AsyncInferenceConfig"
    )
    explainer_config: ExplainerConfigModel = Field(alias="ExplainerConfig")
    shadow_production_variants: List[ProductionVariantModel] = Field(
        alias="ShadowProductionVariants"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointOutputModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_arn: str = Field(alias="EndpointArn")
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    production_variants: List[ProductionVariantSummaryModel] = Field(
        alias="ProductionVariants"
    )
    data_capture_config: DataCaptureConfigSummaryModel = Field(
        alias="DataCaptureConfig"
    )
    endpoint_status: Literal[
        "Creating",
        "Deleting",
        "Failed",
        "InService",
        "OutOfService",
        "RollingBack",
        "SystemUpdating",
        "Updating",
    ] = Field(alias="EndpointStatus")
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_deployment_config: DeploymentConfigModel = Field(alias="LastDeploymentConfig")
    async_inference_config: AsyncInferenceConfigModel = Field(
        alias="AsyncInferenceConfig"
    )
    pending_deployment_summary: PendingDeploymentSummaryModel = Field(
        alias="PendingDeploymentSummary"
    )
    explainer_config: ExplainerConfigModel = Field(alias="ExplainerConfig")
    shadow_production_variants: List[ProductionVariantSummaryModel] = Field(
        alias="ShadowProductionVariants"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHyperParameterTuningJobRequestModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")
    hyper_parameter_tuning_job_config: HyperParameterTuningJobConfigModel = Field(
        alias="HyperParameterTuningJobConfig"
    )
    training_job_definition: Optional[HyperParameterTrainingJobDefinitionModel] = Field(
        default=None, alias="TrainingJobDefinition"
    )
    training_job_definitions: Optional[
        Sequence[HyperParameterTrainingJobDefinitionModel]
    ] = Field(default=None, alias="TrainingJobDefinitions")
    warm_start_config: Optional[HyperParameterTuningJobWarmStartConfigModel] = Field(
        default=None, alias="WarmStartConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeHyperParameterTuningJobResponseModel(BaseModel):
    hyper_parameter_tuning_job_name: str = Field(alias="HyperParameterTuningJobName")
    hyper_parameter_tuning_job_arn: str = Field(alias="HyperParameterTuningJobArn")
    hyper_parameter_tuning_job_config: HyperParameterTuningJobConfigModel = Field(
        alias="HyperParameterTuningJobConfig"
    )
    training_job_definition: HyperParameterTrainingJobDefinitionModel = Field(
        alias="TrainingJobDefinition"
    )
    training_job_definitions: List[HyperParameterTrainingJobDefinitionModel] = Field(
        alias="TrainingJobDefinitions"
    )
    hyper_parameter_tuning_job_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="HyperParameterTuningJobStatus")
    creation_time: datetime = Field(alias="CreationTime")
    hyper_parameter_tuning_end_time: datetime = Field(
        alias="HyperParameterTuningEndTime"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    training_job_status_counters: TrainingJobStatusCountersModel = Field(
        alias="TrainingJobStatusCounters"
    )
    objective_status_counters: ObjectiveStatusCountersModel = Field(
        alias="ObjectiveStatusCounters"
    )
    best_training_job: HyperParameterTrainingJobSummaryModel = Field(
        alias="BestTrainingJob"
    )
    overall_best_training_job: HyperParameterTrainingJobSummaryModel = Field(
        alias="OverallBestTrainingJob"
    )
    warm_start_config: HyperParameterTuningJobWarmStartConfigModel = Field(
        alias="WarmStartConfig"
    )
    failure_reason: str = Field(alias="FailureReason")
    tuning_job_completion_details: HyperParameterTuningJobCompletionDetailsModel = (
        Field(alias="TuningJobCompletionDetails")
    )
    consumed_resources: HyperParameterTuningJobConsumedResourcesModel = Field(
        alias="ConsumedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HyperParameterTuningJobSearchEntityModel(BaseModel):
    hyper_parameter_tuning_job_name: Optional[str] = Field(
        default=None, alias="HyperParameterTuningJobName"
    )
    hyper_parameter_tuning_job_arn: Optional[str] = Field(
        default=None, alias="HyperParameterTuningJobArn"
    )
    hyper_parameter_tuning_job_config: Optional[
        HyperParameterTuningJobConfigModel
    ] = Field(default=None, alias="HyperParameterTuningJobConfig")
    training_job_definition: Optional[HyperParameterTrainingJobDefinitionModel] = Field(
        default=None, alias="TrainingJobDefinition"
    )
    training_job_definitions: Optional[
        List[HyperParameterTrainingJobDefinitionModel]
    ] = Field(default=None, alias="TrainingJobDefinitions")
    hyper_parameter_tuning_job_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="HyperParameterTuningJobStatus")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    hyper_parameter_tuning_end_time: Optional[datetime] = Field(
        default=None, alias="HyperParameterTuningEndTime"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    training_job_status_counters: Optional[TrainingJobStatusCountersModel] = Field(
        default=None, alias="TrainingJobStatusCounters"
    )
    objective_status_counters: Optional[ObjectiveStatusCountersModel] = Field(
        default=None, alias="ObjectiveStatusCounters"
    )
    best_training_job: Optional[HyperParameterTrainingJobSummaryModel] = Field(
        default=None, alias="BestTrainingJob"
    )
    overall_best_training_job: Optional[HyperParameterTrainingJobSummaryModel] = Field(
        default=None, alias="OverallBestTrainingJob"
    )
    warm_start_config: Optional[HyperParameterTuningJobWarmStartConfigModel] = Field(
        default=None, alias="WarmStartConfig"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    tuning_job_completion_details: Optional[
        HyperParameterTuningJobCompletionDetailsModel
    ] = Field(default=None, alias="TuningJobCompletionDetails")
    consumed_resources: Optional[HyperParameterTuningJobConsumedResourcesModel] = Field(
        default=None, alias="ConsumedResources"
    )


class ListInferenceRecommendationsJobStepsResponseModel(BaseModel):
    steps: List[InferenceRecommendationsJobStepModel] = Field(alias="Steps")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLabelingJobsResponseModel(BaseModel):
    labeling_job_summary_list: List[LabelingJobSummaryModel] = Field(
        alias="LabelingJobSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDescribeModelPackageOutputModel(BaseModel):
    model_package_summaries: Dict[str, BatchDescribeModelPackageSummaryModel] = Field(
        alias="ModelPackageSummaries"
    )
    batch_describe_model_package_error_map: Dict[
        str, BatchDescribeModelPackageErrorModel
    ] = Field(alias="BatchDescribeModelPackageErrorMap")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")
    data_quality_app_specification: DataQualityAppSpecificationModel = Field(
        alias="DataQualityAppSpecification"
    )
    data_quality_job_input: DataQualityJobInputModel = Field(
        alias="DataQualityJobInput"
    )
    data_quality_job_output_config: MonitoringOutputConfigModel = Field(
        alias="DataQualityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    role_arn: str = Field(alias="RoleArn")
    data_quality_baseline_config: Optional[DataQualityBaselineConfigModel] = Field(
        default=None, alias="DataQualityBaselineConfig"
    )
    network_config: Optional[MonitoringNetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    stopping_condition: Optional[MonitoringStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeDataQualityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    job_definition_name: str = Field(alias="JobDefinitionName")
    creation_time: datetime = Field(alias="CreationTime")
    data_quality_baseline_config: DataQualityBaselineConfigModel = Field(
        alias="DataQualityBaselineConfig"
    )
    data_quality_app_specification: DataQualityAppSpecificationModel = Field(
        alias="DataQualityAppSpecification"
    )
    data_quality_job_input: DataQualityJobInputModel = Field(
        alias="DataQualityJobInput"
    )
    data_quality_job_output_config: MonitoringOutputConfigModel = Field(
        alias="DataQualityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    network_config: MonitoringNetworkConfigModel = Field(alias="NetworkConfig")
    role_arn: str = Field(alias="RoleArn")
    stopping_condition: MonitoringStoppingConditionModel = Field(
        alias="StoppingCondition"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelBiasJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")
    model_bias_app_specification: ModelBiasAppSpecificationModel = Field(
        alias="ModelBiasAppSpecification"
    )
    model_bias_job_input: ModelBiasJobInputModel = Field(alias="ModelBiasJobInput")
    model_bias_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelBiasJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    role_arn: str = Field(alias="RoleArn")
    model_bias_baseline_config: Optional[ModelBiasBaselineConfigModel] = Field(
        default=None, alias="ModelBiasBaselineConfig"
    )
    network_config: Optional[MonitoringNetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    stopping_condition: Optional[MonitoringStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeModelBiasJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    job_definition_name: str = Field(alias="JobDefinitionName")
    creation_time: datetime = Field(alias="CreationTime")
    model_bias_baseline_config: ModelBiasBaselineConfigModel = Field(
        alias="ModelBiasBaselineConfig"
    )
    model_bias_app_specification: ModelBiasAppSpecificationModel = Field(
        alias="ModelBiasAppSpecification"
    )
    model_bias_job_input: ModelBiasJobInputModel = Field(alias="ModelBiasJobInput")
    model_bias_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelBiasJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    network_config: MonitoringNetworkConfigModel = Field(alias="NetworkConfig")
    role_arn: str = Field(alias="RoleArn")
    stopping_condition: MonitoringStoppingConditionModel = Field(
        alias="StoppingCondition"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelExplainabilityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")
    model_explainability_app_specification: ModelExplainabilityAppSpecificationModel = (
        Field(alias="ModelExplainabilityAppSpecification")
    )
    model_explainability_job_input: ModelExplainabilityJobInputModel = Field(
        alias="ModelExplainabilityJobInput"
    )
    model_explainability_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelExplainabilityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    role_arn: str = Field(alias="RoleArn")
    model_explainability_baseline_config: Optional[
        ModelExplainabilityBaselineConfigModel
    ] = Field(default=None, alias="ModelExplainabilityBaselineConfig")
    network_config: Optional[MonitoringNetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    stopping_condition: Optional[MonitoringStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeModelExplainabilityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    job_definition_name: str = Field(alias="JobDefinitionName")
    creation_time: datetime = Field(alias="CreationTime")
    model_explainability_baseline_config: ModelExplainabilityBaselineConfigModel = (
        Field(alias="ModelExplainabilityBaselineConfig")
    )
    model_explainability_app_specification: ModelExplainabilityAppSpecificationModel = (
        Field(alias="ModelExplainabilityAppSpecification")
    )
    model_explainability_job_input: ModelExplainabilityJobInputModel = Field(
        alias="ModelExplainabilityJobInput"
    )
    model_explainability_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelExplainabilityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    network_config: MonitoringNetworkConfigModel = Field(alias="NetworkConfig")
    role_arn: str = Field(alias="RoleArn")
    stopping_condition: MonitoringStoppingConditionModel = Field(
        alias="StoppingCondition"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelQualityJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="JobDefinitionName")
    model_quality_app_specification: ModelQualityAppSpecificationModel = Field(
        alias="ModelQualityAppSpecification"
    )
    model_quality_job_input: ModelQualityJobInputModel = Field(
        alias="ModelQualityJobInput"
    )
    model_quality_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelQualityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    role_arn: str = Field(alias="RoleArn")
    model_quality_baseline_config: Optional[ModelQualityBaselineConfigModel] = Field(
        default=None, alias="ModelQualityBaselineConfig"
    )
    network_config: Optional[MonitoringNetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )
    stopping_condition: Optional[MonitoringStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeModelQualityJobDefinitionResponseModel(BaseModel):
    job_definition_arn: str = Field(alias="JobDefinitionArn")
    job_definition_name: str = Field(alias="JobDefinitionName")
    creation_time: datetime = Field(alias="CreationTime")
    model_quality_baseline_config: ModelQualityBaselineConfigModel = Field(
        alias="ModelQualityBaselineConfig"
    )
    model_quality_app_specification: ModelQualityAppSpecificationModel = Field(
        alias="ModelQualityAppSpecification"
    )
    model_quality_job_input: ModelQualityJobInputModel = Field(
        alias="ModelQualityJobInput"
    )
    model_quality_job_output_config: MonitoringOutputConfigModel = Field(
        alias="ModelQualityJobOutputConfig"
    )
    job_resources: MonitoringResourcesModel = Field(alias="JobResources")
    network_config: MonitoringNetworkConfigModel = Field(alias="NetworkConfig")
    role_arn: str = Field(alias="RoleArn")
    stopping_condition: MonitoringStoppingConditionModel = Field(
        alias="StoppingCondition"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MonitoringJobDefinitionModel(BaseModel):
    monitoring_inputs: Sequence[MonitoringInputModel] = Field(alias="MonitoringInputs")
    monitoring_output_config: MonitoringOutputConfigModel = Field(
        alias="MonitoringOutputConfig"
    )
    monitoring_resources: MonitoringResourcesModel = Field(alias="MonitoringResources")
    monitoring_app_specification: MonitoringAppSpecificationModel = Field(
        alias="MonitoringAppSpecification"
    )
    role_arn: str = Field(alias="RoleArn")
    baseline_config: Optional[MonitoringBaselineConfigModel] = Field(
        default=None, alias="BaselineConfig"
    )
    stopping_condition: Optional[MonitoringStoppingConditionModel] = Field(
        default=None, alias="StoppingCondition"
    )
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="Environment")
    network_config: Optional[NetworkConfigModel] = Field(
        default=None, alias="NetworkConfig"
    )


class AlgorithmValidationProfileModel(BaseModel):
    profile_name: str = Field(alias="ProfileName")
    training_job_definition: TrainingJobDefinitionModel = Field(
        alias="TrainingJobDefinition"
    )
    transform_job_definition: Optional[TransformJobDefinitionModel] = Field(
        default=None, alias="TransformJobDefinition"
    )


class ModelPackageValidationProfileModel(BaseModel):
    profile_name: str = Field(alias="ProfileName")
    transform_job_definition: TransformJobDefinitionModel = Field(
        alias="TransformJobDefinition"
    )


class TrialComponentSourceDetailModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    training_job: Optional[TrainingJobModel] = Field(default=None, alias="TrainingJob")
    processing_job: Optional[ProcessingJobModel] = Field(
        default=None, alias="ProcessingJob"
    )
    transform_job: Optional[TransformJobModel] = Field(
        default=None, alias="TransformJob"
    )


class MonitoringScheduleConfigModel(BaseModel):
    schedule_config: Optional[ScheduleConfigModel] = Field(
        default=None, alias="ScheduleConfig"
    )
    monitoring_job_definition: Optional[MonitoringJobDefinitionModel] = Field(
        default=None, alias="MonitoringJobDefinition"
    )
    monitoring_job_definition_name: Optional[str] = Field(
        default=None, alias="MonitoringJobDefinitionName"
    )
    monitoring_type: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringType")


class AlgorithmValidationSpecificationModel(BaseModel):
    validation_role: str = Field(alias="ValidationRole")
    validation_profiles: Sequence[AlgorithmValidationProfileModel] = Field(
        alias="ValidationProfiles"
    )


class ModelPackageValidationSpecificationModel(BaseModel):
    validation_role: str = Field(alias="ValidationRole")
    validation_profiles: Sequence[ModelPackageValidationProfileModel] = Field(
        alias="ValidationProfiles"
    )


class TrialComponentModel(BaseModel):
    trial_component_name: Optional[str] = Field(
        default=None, alias="TrialComponentName"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    trial_component_arn: Optional[str] = Field(default=None, alias="TrialComponentArn")
    source: Optional[TrialComponentSourceModel] = Field(default=None, alias="Source")
    status: Optional[TrialComponentStatusModel] = Field(default=None, alias="Status")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    parameters: Optional[Dict[str, TrialComponentParameterValueModel]] = Field(
        default=None, alias="Parameters"
    )
    input_artifacts: Optional[Dict[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="InputArtifacts"
    )
    output_artifacts: Optional[Dict[str, TrialComponentArtifactModel]] = Field(
        default=None, alias="OutputArtifacts"
    )
    metrics: Optional[List[TrialComponentMetricSummaryModel]] = Field(
        default=None, alias="Metrics"
    )
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    source_detail: Optional[TrialComponentSourceDetailModel] = Field(
        default=None, alias="SourceDetail"
    )
    lineage_group_arn: Optional[str] = Field(default=None, alias="LineageGroupArn")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    parents: Optional[List[ParentModel]] = Field(default=None, alias="Parents")
    run_name: Optional[str] = Field(default=None, alias="RunName")


class CreateMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_schedule_config: MonitoringScheduleConfigModel = Field(
        alias="MonitoringScheduleConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeMonitoringScheduleResponseModel(BaseModel):
    monitoring_schedule_arn: str = Field(alias="MonitoringScheduleArn")
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_schedule_status: Literal[
        "Failed", "Pending", "Scheduled", "Stopped"
    ] = Field(alias="MonitoringScheduleStatus")
    monitoring_type: Literal[
        "DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"
    ] = Field(alias="MonitoringType")
    failure_reason: str = Field(alias="FailureReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    monitoring_schedule_config: MonitoringScheduleConfigModel = Field(
        alias="MonitoringScheduleConfig"
    )
    endpoint_name: str = Field(alias="EndpointName")
    last_monitoring_execution_summary: MonitoringExecutionSummaryModel = Field(
        alias="LastMonitoringExecutionSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelDashboardMonitoringScheduleModel(BaseModel):
    monitoring_schedule_arn: Optional[str] = Field(
        default=None, alias="MonitoringScheduleArn"
    )
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    monitoring_schedule_status: Optional[
        Literal["Failed", "Pending", "Scheduled", "Stopped"]
    ] = Field(default=None, alias="MonitoringScheduleStatus")
    monitoring_type: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringType")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    monitoring_schedule_config: Optional[MonitoringScheduleConfigModel] = Field(
        default=None, alias="MonitoringScheduleConfig"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    monitoring_alert_summaries: Optional[List[MonitoringAlertSummaryModel]] = Field(
        default=None, alias="MonitoringAlertSummaries"
    )
    last_monitoring_execution_summary: Optional[
        MonitoringExecutionSummaryModel
    ] = Field(default=None, alias="LastMonitoringExecutionSummary")


class MonitoringScheduleModel(BaseModel):
    monitoring_schedule_arn: Optional[str] = Field(
        default=None, alias="MonitoringScheduleArn"
    )
    monitoring_schedule_name: Optional[str] = Field(
        default=None, alias="MonitoringScheduleName"
    )
    monitoring_schedule_status: Optional[
        Literal["Failed", "Pending", "Scheduled", "Stopped"]
    ] = Field(default=None, alias="MonitoringScheduleStatus")
    monitoring_type: Optional[
        Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
    ] = Field(default=None, alias="MonitoringType")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    monitoring_schedule_config: Optional[MonitoringScheduleConfigModel] = Field(
        default=None, alias="MonitoringScheduleConfig"
    )
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    last_monitoring_execution_summary: Optional[
        MonitoringExecutionSummaryModel
    ] = Field(default=None, alias="LastMonitoringExecutionSummary")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class UpdateMonitoringScheduleRequestModel(BaseModel):
    monitoring_schedule_name: str = Field(alias="MonitoringScheduleName")
    monitoring_schedule_config: MonitoringScheduleConfigModel = Field(
        alias="MonitoringScheduleConfig"
    )


class CreateAlgorithmInputRequestModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")
    training_specification: TrainingSpecificationModel = Field(
        alias="TrainingSpecification"
    )
    algorithm_description: Optional[str] = Field(
        default=None, alias="AlgorithmDescription"
    )
    inference_specification: Optional[InferenceSpecificationModel] = Field(
        default=None, alias="InferenceSpecification"
    )
    validation_specification: Optional[AlgorithmValidationSpecificationModel] = Field(
        default=None, alias="ValidationSpecification"
    )
    certify_for_marketplace: Optional[bool] = Field(
        default=None, alias="CertifyForMarketplace"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeAlgorithmOutputModel(BaseModel):
    algorithm_name: str = Field(alias="AlgorithmName")
    algorithm_arn: str = Field(alias="AlgorithmArn")
    algorithm_description: str = Field(alias="AlgorithmDescription")
    creation_time: datetime = Field(alias="CreationTime")
    training_specification: TrainingSpecificationModel = Field(
        alias="TrainingSpecification"
    )
    inference_specification: InferenceSpecificationModel = Field(
        alias="InferenceSpecification"
    )
    validation_specification: AlgorithmValidationSpecificationModel = Field(
        alias="ValidationSpecification"
    )
    algorithm_status: Literal[
        "Completed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="AlgorithmStatus")
    algorithm_status_details: AlgorithmStatusDetailsModel = Field(
        alias="AlgorithmStatusDetails"
    )
    product_id: str = Field(alias="ProductId")
    certify_for_marketplace: bool = Field(alias="CertifyForMarketplace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelPackageInputRequestModel(BaseModel):
    model_package_name: Optional[str] = Field(default=None, alias="ModelPackageName")
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_description: Optional[str] = Field(
        default=None, alias="ModelPackageDescription"
    )
    inference_specification: Optional[InferenceSpecificationModel] = Field(
        default=None, alias="InferenceSpecification"
    )
    validation_specification: Optional[
        ModelPackageValidationSpecificationModel
    ] = Field(default=None, alias="ValidationSpecification")
    source_algorithm_specification: Optional[SourceAlgorithmSpecificationModel] = Field(
        default=None, alias="SourceAlgorithmSpecification"
    )
    certify_for_marketplace: Optional[bool] = Field(
        default=None, alias="CertifyForMarketplace"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    model_metrics: Optional[ModelMetricsModel] = Field(
        default=None, alias="ModelMetrics"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    customer_metadata_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="CustomerMetadataProperties"
    )
    drift_check_baselines: Optional[DriftCheckBaselinesModel] = Field(
        default=None, alias="DriftCheckBaselines"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    task: Optional[str] = Field(default=None, alias="Task")
    sample_payload_url: Optional[str] = Field(default=None, alias="SamplePayloadUrl")
    additional_inference_specifications: Optional[
        Sequence[AdditionalInferenceSpecificationDefinitionModel]
    ] = Field(default=None, alias="AdditionalInferenceSpecifications")


class DescribeModelPackageOutputModel(BaseModel):
    model_package_name: str = Field(alias="ModelPackageName")
    model_package_group_name: str = Field(alias="ModelPackageGroupName")
    model_package_version: int = Field(alias="ModelPackageVersion")
    model_package_arn: str = Field(alias="ModelPackageArn")
    model_package_description: str = Field(alias="ModelPackageDescription")
    creation_time: datetime = Field(alias="CreationTime")
    inference_specification: InferenceSpecificationModel = Field(
        alias="InferenceSpecification"
    )
    source_algorithm_specification: SourceAlgorithmSpecificationModel = Field(
        alias="SourceAlgorithmSpecification"
    )
    validation_specification: ModelPackageValidationSpecificationModel = Field(
        alias="ValidationSpecification"
    )
    model_package_status: Literal[
        "Completed", "Deleting", "Failed", "InProgress", "Pending"
    ] = Field(alias="ModelPackageStatus")
    model_package_status_details: ModelPackageStatusDetailsModel = Field(
        alias="ModelPackageStatusDetails"
    )
    certify_for_marketplace: bool = Field(alias="CertifyForMarketplace")
    model_approval_status: Literal[
        "Approved", "PendingManualApproval", "Rejected"
    ] = Field(alias="ModelApprovalStatus")
    created_by: UserContextModel = Field(alias="CreatedBy")
    metadata_properties: MetadataPropertiesModel = Field(alias="MetadataProperties")
    model_metrics: ModelMetricsModel = Field(alias="ModelMetrics")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_modified_by: UserContextModel = Field(alias="LastModifiedBy")
    approval_description: str = Field(alias="ApprovalDescription")
    customer_metadata_properties: Dict[str, str] = Field(
        alias="CustomerMetadataProperties"
    )
    drift_check_baselines: DriftCheckBaselinesModel = Field(alias="DriftCheckBaselines")
    domain: str = Field(alias="Domain")
    task: str = Field(alias="Task")
    sample_payload_url: str = Field(alias="SamplePayloadUrl")
    additional_inference_specifications: List[
        AdditionalInferenceSpecificationDefinitionModel
    ] = Field(alias="AdditionalInferenceSpecifications")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelPackageModel(BaseModel):
    model_package_name: Optional[str] = Field(default=None, alias="ModelPackageName")
    model_package_group_name: Optional[str] = Field(
        default=None, alias="ModelPackageGroupName"
    )
    model_package_version: Optional[int] = Field(
        default=None, alias="ModelPackageVersion"
    )
    model_package_arn: Optional[str] = Field(default=None, alias="ModelPackageArn")
    model_package_description: Optional[str] = Field(
        default=None, alias="ModelPackageDescription"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    inference_specification: Optional[InferenceSpecificationModel] = Field(
        default=None, alias="InferenceSpecification"
    )
    source_algorithm_specification: Optional[SourceAlgorithmSpecificationModel] = Field(
        default=None, alias="SourceAlgorithmSpecification"
    )
    validation_specification: Optional[
        ModelPackageValidationSpecificationModel
    ] = Field(default=None, alias="ValidationSpecification")
    model_package_status: Optional[
        Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
    ] = Field(default=None, alias="ModelPackageStatus")
    model_package_status_details: Optional[ModelPackageStatusDetailsModel] = Field(
        default=None, alias="ModelPackageStatusDetails"
    )
    certify_for_marketplace: Optional[bool] = Field(
        default=None, alias="CertifyForMarketplace"
    )
    model_approval_status: Optional[
        Literal["Approved", "PendingManualApproval", "Rejected"]
    ] = Field(default=None, alias="ModelApprovalStatus")
    created_by: Optional[UserContextModel] = Field(default=None, alias="CreatedBy")
    metadata_properties: Optional[MetadataPropertiesModel] = Field(
        default=None, alias="MetadataProperties"
    )
    model_metrics: Optional[ModelMetricsModel] = Field(
        default=None, alias="ModelMetrics"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_modified_by: Optional[UserContextModel] = Field(
        default=None, alias="LastModifiedBy"
    )
    approval_description: Optional[str] = Field(
        default=None, alias="ApprovalDescription"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    task: Optional[str] = Field(default=None, alias="Task")
    sample_payload_url: Optional[str] = Field(default=None, alias="SamplePayloadUrl")
    additional_inference_specifications: Optional[
        List[AdditionalInferenceSpecificationDefinitionModel]
    ] = Field(default=None, alias="AdditionalInferenceSpecifications")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    customer_metadata_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="CustomerMetadataProperties"
    )
    drift_check_baselines: Optional[DriftCheckBaselinesModel] = Field(
        default=None, alias="DriftCheckBaselines"
    )


class ModelDashboardModelModel(BaseModel):
    model: Optional[ModelModel] = Field(default=None, alias="Model")
    endpoints: Optional[List[ModelDashboardEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )
    last_batch_transform_job: Optional[TransformJobModel] = Field(
        default=None, alias="LastBatchTransformJob"
    )
    monitoring_schedules: Optional[List[ModelDashboardMonitoringScheduleModel]] = Field(
        default=None, alias="MonitoringSchedules"
    )
    model_card: Optional[ModelDashboardModelCardModel] = Field(
        default=None, alias="ModelCard"
    )


class EndpointModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_arn: str = Field(alias="EndpointArn")
    endpoint_config_name: str = Field(alias="EndpointConfigName")
    endpoint_status: Literal[
        "Creating",
        "Deleting",
        "Failed",
        "InService",
        "OutOfService",
        "RollingBack",
        "SystemUpdating",
        "Updating",
    ] = Field(alias="EndpointStatus")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    production_variants: Optional[List[ProductionVariantSummaryModel]] = Field(
        default=None, alias="ProductionVariants"
    )
    data_capture_config: Optional[DataCaptureConfigSummaryModel] = Field(
        default=None, alias="DataCaptureConfig"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    monitoring_schedules: Optional[List[MonitoringScheduleModel]] = Field(
        default=None, alias="MonitoringSchedules"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    shadow_production_variants: Optional[List[ProductionVariantSummaryModel]] = Field(
        default=None, alias="ShadowProductionVariants"
    )


class SearchRecordModel(BaseModel):
    training_job: Optional[TrainingJobModel] = Field(default=None, alias="TrainingJob")
    experiment: Optional[ExperimentModel] = Field(default=None, alias="Experiment")
    trial: Optional[TrialModel] = Field(default=None, alias="Trial")
    trial_component: Optional[TrialComponentModel] = Field(
        default=None, alias="TrialComponent"
    )
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")
    model_package: Optional[ModelPackageModel] = Field(
        default=None, alias="ModelPackage"
    )
    model_package_group: Optional[ModelPackageGroupModel] = Field(
        default=None, alias="ModelPackageGroup"
    )
    pipeline: Optional[PipelineModel] = Field(default=None, alias="Pipeline")
    pipeline_execution: Optional[PipelineExecutionModel] = Field(
        default=None, alias="PipelineExecution"
    )
    feature_group: Optional[FeatureGroupModel] = Field(
        default=None, alias="FeatureGroup"
    )
    project: Optional[ProjectModel] = Field(default=None, alias="Project")
    feature_metadata: Optional[FeatureMetadataModel] = Field(
        default=None, alias="FeatureMetadata"
    )
    hyper_parameter_tuning_job: Optional[
        HyperParameterTuningJobSearchEntityModel
    ] = Field(default=None, alias="HyperParameterTuningJob")
    model: Optional[ModelDashboardModelModel] = Field(default=None, alias="Model")
    model_card: Optional[ModelCardModel] = Field(default=None, alias="ModelCard")


class SearchResponseModel(BaseModel):
    results: List[SearchRecordModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
