# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class MetricDimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DatapointModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    value: Optional[float] = Field(default=None, alias="Value")


class DeleteScalingPlanRequestModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeScalingPlanResourcesRequestModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetScalingPlanResourceForecastDataRequestModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    service_namespace: Literal["autoscaling", "dynamodb", "ec2", "ecs", "rds"] = Field(
        alias="ServiceNamespace"
    )
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "autoscaling:autoScalingGroup:DesiredCapacity",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "rds:cluster:ReadReplicaCount",
    ] = Field(alias="ScalableDimension")
    forecast_data_type: Literal[
        "CapacityForecast",
        "LoadForecast",
        "ScheduledActionMaxCapacity",
        "ScheduledActionMinCapacity",
    ] = Field(alias="ForecastDataType")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class PredefinedLoadMetricSpecificationModel(BaseModel):
    predefined_load_metric_type: Literal[
        "ALBTargetGroupRequestCount",
        "ASGTotalCPUUtilization",
        "ASGTotalNetworkIn",
        "ASGTotalNetworkOut",
    ] = Field(alias="PredefinedLoadMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class PredefinedScalingMetricSpecificationModel(BaseModel):
    predefined_scaling_metric_type: Literal[
        "ALBRequestCountPerTarget",
        "ASGAverageCPUUtilization",
        "ASGAverageNetworkIn",
        "ASGAverageNetworkOut",
        "DynamoDBReadCapacityUtilization",
        "DynamoDBWriteCapacityUtilization",
        "EC2SpotFleetRequestAverageCPUUtilization",
        "EC2SpotFleetRequestAverageNetworkIn",
        "EC2SpotFleetRequestAverageNetworkOut",
        "ECSServiceAverageCPUUtilization",
        "ECSServiceAverageMemoryUtilization",
        "RDSReaderAverageCPUUtilization",
        "RDSReaderAverageDatabaseConnections",
    ] = Field(alias="PredefinedScalingMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class ApplicationSourceModel(BaseModel):
    cloud_formation_stack_arn: Optional[str] = Field(
        default=None, alias="CloudFormationStackARN"
    )
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="TagFilters"
    )


class CreateScalingPlanResponseModel(BaseModel):
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomizedLoadMetricSpecificationModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    namespace: str = Field(alias="Namespace")
    statistic: Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"] = Field(
        alias="Statistic"
    )
    dimensions: Optional[Sequence[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    unit: Optional[str] = Field(default=None, alias="Unit")


class CustomizedScalingMetricSpecificationModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    namespace: str = Field(alias="Namespace")
    statistic: Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"] = Field(
        alias="Statistic"
    )
    dimensions: Optional[Sequence[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    unit: Optional[str] = Field(default=None, alias="Unit")


class GetScalingPlanResourceForecastDataResponseModel(BaseModel):
    datapoints: List[DatapointModel] = Field(alias="Datapoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateModel(
    BaseModel
):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingPlansRequestDescribeScalingPlansPaginateModel(BaseModel):
    scaling_plan_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScalingPlanNames"
    )
    scaling_plan_version: Optional[int] = Field(
        default=None, alias="ScalingPlanVersion"
    )
    application_sources: Optional[Sequence[ApplicationSourceModel]] = Field(
        default=None, alias="ApplicationSources"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingPlansRequestModel(BaseModel):
    scaling_plan_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScalingPlanNames"
    )
    scaling_plan_version: Optional[int] = Field(
        default=None, alias="ScalingPlanVersion"
    )
    application_sources: Optional[Sequence[ApplicationSourceModel]] = Field(
        default=None, alias="ApplicationSources"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TargetTrackingConfigurationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    predefined_scaling_metric_specification: Optional[
        PredefinedScalingMetricSpecificationModel
    ] = Field(default=None, alias="PredefinedScalingMetricSpecification")
    customized_scaling_metric_specification: Optional[
        CustomizedScalingMetricSpecificationModel
    ] = Field(default=None, alias="CustomizedScalingMetricSpecification")
    disable_scale_in: Optional[bool] = Field(default=None, alias="DisableScaleIn")
    scale_out_cooldown: Optional[int] = Field(default=None, alias="ScaleOutCooldown")
    scale_in_cooldown: Optional[int] = Field(default=None, alias="ScaleInCooldown")
    estimated_instance_warmup: Optional[int] = Field(
        default=None, alias="EstimatedInstanceWarmup"
    )


class ScalingInstructionModel(BaseModel):
    service_namespace: Literal["autoscaling", "dynamodb", "ec2", "ecs", "rds"] = Field(
        alias="ServiceNamespace"
    )
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "autoscaling:autoScalingGroup:DesiredCapacity",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "rds:cluster:ReadReplicaCount",
    ] = Field(alias="ScalableDimension")
    min_capacity: int = Field(alias="MinCapacity")
    max_capacity: int = Field(alias="MaxCapacity")
    target_tracking_configurations: Sequence[TargetTrackingConfigurationModel] = Field(
        alias="TargetTrackingConfigurations"
    )
    predefined_load_metric_specification: Optional[
        PredefinedLoadMetricSpecificationModel
    ] = Field(default=None, alias="PredefinedLoadMetricSpecification")
    customized_load_metric_specification: Optional[
        CustomizedLoadMetricSpecificationModel
    ] = Field(default=None, alias="CustomizedLoadMetricSpecification")
    scheduled_action_buffer_time: Optional[int] = Field(
        default=None, alias="ScheduledActionBufferTime"
    )
    predictive_scaling_max_capacity_behavior: Optional[
        Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityAboveForecastCapacity",
            "SetMaxCapacityToForecastCapacity",
        ]
    ] = Field(default=None, alias="PredictiveScalingMaxCapacityBehavior")
    predictive_scaling_max_capacity_buffer: Optional[int] = Field(
        default=None, alias="PredictiveScalingMaxCapacityBuffer"
    )
    predictive_scaling_mode: Optional[
        Literal["ForecastAndScale", "ForecastOnly"]
    ] = Field(default=None, alias="PredictiveScalingMode")
    scaling_policy_update_behavior: Optional[
        Literal["KeepExternalPolicies", "ReplaceExternalPolicies"]
    ] = Field(default=None, alias="ScalingPolicyUpdateBehavior")
    disable_dynamic_scaling: Optional[bool] = Field(
        default=None, alias="DisableDynamicScaling"
    )


class ScalingPolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    policy_type: Literal["TargetTrackingScaling"] = Field(alias="PolicyType")
    target_tracking_configuration: Optional[TargetTrackingConfigurationModel] = Field(
        default=None, alias="TargetTrackingConfiguration"
    )


class CreateScalingPlanRequestModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    application_source: ApplicationSourceModel = Field(alias="ApplicationSource")
    scaling_instructions: Sequence[ScalingInstructionModel] = Field(
        alias="ScalingInstructions"
    )


class ScalingPlanModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    application_source: ApplicationSourceModel = Field(alias="ApplicationSource")
    scaling_instructions: List[ScalingInstructionModel] = Field(
        alias="ScalingInstructions"
    )
    status_code: Literal[
        "Active",
        "ActiveWithProblems",
        "CreationFailed",
        "CreationInProgress",
        "DeletionFailed",
        "DeletionInProgress",
        "UpdateFailed",
        "UpdateInProgress",
    ] = Field(alias="StatusCode")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    status_start_time: Optional[datetime] = Field(default=None, alias="StatusStartTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class UpdateScalingPlanRequestModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    application_source: Optional[ApplicationSourceModel] = Field(
        default=None, alias="ApplicationSource"
    )
    scaling_instructions: Optional[Sequence[ScalingInstructionModel]] = Field(
        default=None, alias="ScalingInstructions"
    )


class ScalingPlanResourceModel(BaseModel):
    scaling_plan_name: str = Field(alias="ScalingPlanName")
    scaling_plan_version: int = Field(alias="ScalingPlanVersion")
    service_namespace: Literal["autoscaling", "dynamodb", "ec2", "ecs", "rds"] = Field(
        alias="ServiceNamespace"
    )
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "autoscaling:autoScalingGroup:DesiredCapacity",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "rds:cluster:ReadReplicaCount",
    ] = Field(alias="ScalableDimension")
    scaling_status_code: Literal["Active", "Inactive", "PartiallyActive"] = Field(
        alias="ScalingStatusCode"
    )
    scaling_policies: Optional[List[ScalingPolicyModel]] = Field(
        default=None, alias="ScalingPolicies"
    )
    scaling_status_message: Optional[str] = Field(
        default=None, alias="ScalingStatusMessage"
    )


class DescribeScalingPlansResponseModel(BaseModel):
    scaling_plans: List[ScalingPlanModel] = Field(alias="ScalingPlans")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScalingPlanResourcesResponseModel(BaseModel):
    scaling_plan_resources: List[ScalingPlanResourceModel] = Field(
        alias="ScalingPlanResources"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
