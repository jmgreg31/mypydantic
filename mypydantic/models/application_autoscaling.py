# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlarmModel(BaseModel):
    alarm_name: str = Field(alias="AlarmName")
    alarm_arn: str = Field(alias="AlarmARN")


class MetricDimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DeleteScalingPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")


class DeleteScheduledActionRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")


class DeregisterScalableTargetRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeScalableTargetsRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="ResourceIds")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeScalingActivitiesRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    include_not_scaled_activities: Optional[bool] = Field(
        default=None, alias="IncludeNotScaledActivities"
    )


class DescribeScalingPoliciesRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeScheduledActionsRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    scheduled_action_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScheduledActionNames"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NotScaledReasonModel(BaseModel):
    code: str = Field(alias="Code")
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    min_capacity: Optional[int] = Field(default=None, alias="MinCapacity")
    current_capacity: Optional[int] = Field(default=None, alias="CurrentCapacity")


class PredefinedMetricSpecificationModel(BaseModel):
    predefined_metric_type: Literal[
        "ALBRequestCountPerTarget",
        "AppStreamAverageCapacityUtilization",
        "CassandraReadCapacityUtilization",
        "CassandraWriteCapacityUtilization",
        "ComprehendInferenceUtilization",
        "DynamoDBReadCapacityUtilization",
        "DynamoDBWriteCapacityUtilization",
        "EC2SpotFleetRequestAverageCPUUtilization",
        "EC2SpotFleetRequestAverageNetworkIn",
        "EC2SpotFleetRequestAverageNetworkOut",
        "ECSServiceAverageCPUUtilization",
        "ECSServiceAverageMemoryUtilization",
        "ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage",
        "ElastiCachePrimaryEngineCPUUtilization",
        "ElastiCacheReplicaEngineCPUUtilization",
        "KafkaBrokerStorageUtilization",
        "LambdaProvisionedConcurrencyUtilization",
        "NeptuneReaderAverageCPUUtilization",
        "RDSReaderAverageCPUUtilization",
        "RDSReaderAverageDatabaseConnections",
        "SageMakerVariantInvocationsPerInstance",
    ] = Field(alias="PredefinedMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class ScalableTargetActionModel(BaseModel):
    min_capacity: Optional[int] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")


class SuspendedStateModel(BaseModel):
    dynamic_scaling_in_suspended: Optional[bool] = Field(
        default=None, alias="DynamicScalingInSuspended"
    )
    dynamic_scaling_out_suspended: Optional[bool] = Field(
        default=None, alias="DynamicScalingOutSuspended"
    )
    scheduled_scaling_suspended: Optional[bool] = Field(
        default=None, alias="ScheduledScalingSuspended"
    )


class StepAdjustmentModel(BaseModel):
    scaling_adjustment: int = Field(alias="ScalingAdjustment")
    metric_interval_lower_bound: Optional[float] = Field(
        default=None, alias="MetricIntervalLowerBound"
    )
    metric_interval_upper_bound: Optional[float] = Field(
        default=None, alias="MetricIntervalUpperBound"
    )


class CustomizedMetricSpecificationModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    namespace: str = Field(alias="Namespace")
    statistic: Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"] = Field(
        alias="Statistic"
    )
    dimensions: Optional[List[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    unit: Optional[str] = Field(default=None, alias="Unit")


class DescribeScalableTargetsRequestDescribeScalableTargetsPaginateModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="ResourceIds")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    include_not_scaled_activities: Optional[bool] = Field(
        default=None, alias="IncludeNotScaledActivities"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScheduledActionsRequestDescribeScheduledActionsPaginateModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    scheduled_action_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScheduledActionNames"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PutScalingPolicyResponseModel(BaseModel):
    policy_arn: str = Field(alias="PolicyARN")
    alarms: List[AlarmModel] = Field(alias="Alarms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScalingActivityModel(BaseModel):
    activity_id: str = Field(alias="ActivityId")
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    description: str = Field(alias="Description")
    cause: str = Field(alias="Cause")
    start_time: datetime = Field(alias="StartTime")
    status_code: Literal[
        "Failed", "InProgress", "Overridden", "Pending", "Successful", "Unfulfilled"
    ] = Field(alias="StatusCode")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    details: Optional[str] = Field(default=None, alias="Details")
    not_scaled_reasons: Optional[List[NotScaledReasonModel]] = Field(
        default=None, alias="NotScaledReasons"
    )


class PutScheduledActionRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    scalable_target_action: Optional[ScalableTargetActionModel] = Field(
        default=None, alias="ScalableTargetAction"
    )


class ScheduledActionModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    scheduled_action_arn: str = Field(alias="ScheduledActionARN")
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    schedule: str = Field(alias="Schedule")
    resource_id: str = Field(alias="ResourceId")
    creation_time: datetime = Field(alias="CreationTime")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    scalable_dimension: Optional[
        Literal[
            "appstream:fleet:DesiredCapacity",
            "cassandra:table:ReadCapacityUnits",
            "cassandra:table:WriteCapacityUnits",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
            "custom-resource:ResourceType:Property",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "ec2:spot-fleet-request:TargetCapacity",
            "ecs:service:DesiredCount",
            "elasticache:replication-group:NodeGroups",
            "elasticache:replication-group:Replicas",
            "elasticmapreduce:instancegroup:InstanceCount",
            "kafka:broker-storage:VolumeSize",
            "lambda:function:ProvisionedConcurrency",
            "neptune:cluster:ReadReplicaCount",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
        ]
    ] = Field(default=None, alias="ScalableDimension")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    scalable_target_action: Optional[ScalableTargetActionModel] = Field(
        default=None, alias="ScalableTargetAction"
    )


class RegisterScalableTargetRequestModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    min_capacity: Optional[int] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    suspended_state: Optional[SuspendedStateModel] = Field(
        default=None, alias="SuspendedState"
    )


class ScalableTargetModel(BaseModel):
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    min_capacity: int = Field(alias="MinCapacity")
    max_capacity: int = Field(alias="MaxCapacity")
    role_arn: str = Field(alias="RoleARN")
    creation_time: datetime = Field(alias="CreationTime")
    suspended_state: Optional[SuspendedStateModel] = Field(
        default=None, alias="SuspendedState"
    )


class StepScalingPolicyConfigurationModel(BaseModel):
    adjustment_type: Optional[
        Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
    ] = Field(default=None, alias="AdjustmentType")
    step_adjustments: Optional[List[StepAdjustmentModel]] = Field(
        default=None, alias="StepAdjustments"
    )
    min_adjustment_magnitude: Optional[int] = Field(
        default=None, alias="MinAdjustmentMagnitude"
    )
    cooldown: Optional[int] = Field(default=None, alias="Cooldown")
    metric_aggregation_type: Optional[Literal["Average", "Maximum", "Minimum"]] = Field(
        default=None, alias="MetricAggregationType"
    )


class TargetTrackingScalingPolicyConfigurationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    predefined_metric_specification: Optional[
        PredefinedMetricSpecificationModel
    ] = Field(default=None, alias="PredefinedMetricSpecification")
    customized_metric_specification: Optional[
        CustomizedMetricSpecificationModel
    ] = Field(default=None, alias="CustomizedMetricSpecification")
    scale_out_cooldown: Optional[int] = Field(default=None, alias="ScaleOutCooldown")
    scale_in_cooldown: Optional[int] = Field(default=None, alias="ScaleInCooldown")
    disable_scale_in: Optional[bool] = Field(default=None, alias="DisableScaleIn")


class DescribeScalingActivitiesResponseModel(BaseModel):
    scaling_activities: List[ScalingActivityModel] = Field(alias="ScalingActivities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScheduledActionsResponseModel(BaseModel):
    scheduled_actions: List[ScheduledActionModel] = Field(alias="ScheduledActions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScalableTargetsResponseModel(BaseModel):
    scalable_targets: List[ScalableTargetModel] = Field(alias="ScalableTargets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutScalingPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    policy_type: Optional[Literal["StepScaling", "TargetTrackingScaling"]] = Field(
        default=None, alias="PolicyType"
    )
    step_scaling_policy_configuration: Optional[
        StepScalingPolicyConfigurationModel
    ] = Field(default=None, alias="StepScalingPolicyConfiguration")
    target_tracking_scaling_policy_configuration: Optional[
        TargetTrackingScalingPolicyConfigurationModel
    ] = Field(default=None, alias="TargetTrackingScalingPolicyConfiguration")


class ScalingPolicyModel(BaseModel):
    policy_arn: str = Field(alias="PolicyARN")
    policy_name: str = Field(alias="PolicyName")
    service_namespace: Literal[
        "appstream",
        "cassandra",
        "comprehend",
        "custom-resource",
        "dynamodb",
        "ec2",
        "ecs",
        "elasticache",
        "elasticmapreduce",
        "kafka",
        "lambda",
        "neptune",
        "rds",
        "sagemaker",
    ] = Field(alias="ServiceNamespace")
    resource_id: str = Field(alias="ResourceId")
    scalable_dimension: Literal[
        "appstream:fleet:DesiredCapacity",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "custom-resource:ResourceType:Property",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "ec2:spot-fleet-request:TargetCapacity",
        "ecs:service:DesiredCount",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "elasticmapreduce:instancegroup:InstanceCount",
        "kafka:broker-storage:VolumeSize",
        "lambda:function:ProvisionedConcurrency",
        "neptune:cluster:ReadReplicaCount",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
    ] = Field(alias="ScalableDimension")
    policy_type: Literal["StepScaling", "TargetTrackingScaling"] = Field(
        alias="PolicyType"
    )
    creation_time: datetime = Field(alias="CreationTime")
    step_scaling_policy_configuration: Optional[
        StepScalingPolicyConfigurationModel
    ] = Field(default=None, alias="StepScalingPolicyConfiguration")
    target_tracking_scaling_policy_configuration: Optional[
        TargetTrackingScalingPolicyConfigurationModel
    ] = Field(default=None, alias="TargetTrackingScalingPolicyConfiguration")
    alarms: Optional[List[AlarmModel]] = Field(default=None, alias="Alarms")


class DescribeScalingPoliciesResponseModel(BaseModel):
    scaling_policies: List[ScalingPolicyModel] = Field(alias="ScalingPolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
