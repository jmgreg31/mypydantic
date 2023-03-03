# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceleratorCountRequestModel(BaseModel):
    min: Optional[int] = Field(default=None, alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class AcceleratorTotalMemoryMiBRequestModel(BaseModel):
    min: Optional[int] = Field(default=None, alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class ActivityModel(BaseModel):
    activity_id: str = Field(alias="ActivityId")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    cause: str = Field(alias="Cause")
    start_time: datetime = Field(alias="StartTime")
    status_code: Literal[
        "Cancelled",
        "Failed",
        "InProgress",
        "MidLifecycleAction",
        "PendingSpotBidPlacement",
        "PreInService",
        "Successful",
        "WaitingForELBConnectionDraining",
        "WaitingForInstanceId",
        "WaitingForInstanceWarmup",
        "WaitingForSpotInstanceId",
        "WaitingForSpotInstanceRequestId",
    ] = Field(alias="StatusCode")
    description: Optional[str] = Field(default=None, alias="Description")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    progress: Optional[int] = Field(default=None, alias="Progress")
    details: Optional[str] = Field(default=None, alias="Details")
    auto_scaling_group_state: Optional[str] = Field(
        default=None, alias="AutoScalingGroupState"
    )
    auto_scaling_group_arn: Optional[str] = Field(
        default=None, alias="AutoScalingGroupARN"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AdjustmentTypeModel(BaseModel):
    adjustment_type: Optional[str] = Field(default=None, alias="AdjustmentType")


class AlarmModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    alarm_arn: Optional[str] = Field(default=None, alias="AlarmARN")


class AttachInstancesQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class AttachLoadBalancerTargetGroupsTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    target_group_arns: Sequence[str] = Field(alias="TargetGroupARNs")


class AttachLoadBalancersTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    load_balancer_names: Sequence[str] = Field(alias="LoadBalancerNames")


class TrafficSourceIdentifierModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class EnabledMetricModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")
    granularity: Optional[str] = Field(default=None, alias="Granularity")


class LaunchTemplateSpecificationModel(BaseModel):
    launch_template_id: Optional[str] = Field(default=None, alias="LaunchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="LaunchTemplateName"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class SuspendedProcessModel(BaseModel):
    process_name: Optional[str] = Field(default=None, alias="ProcessName")
    suspension_reason: Optional[str] = Field(default=None, alias="SuspensionReason")


class TagDescriptionModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    propagate_at_launch: Optional[bool] = Field(default=None, alias="PropagateAtLaunch")


class BaselineEbsBandwidthMbpsRequestModel(BaseModel):
    min: Optional[int] = Field(default=None, alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class FailedScheduledUpdateGroupActionRequestModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchDeleteScheduledActionTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    scheduled_action_names: Sequence[str] = Field(alias="ScheduledActionNames")


class ScheduledUpdateGroupActionRequestModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    recurrence: Optional[str] = Field(default=None, alias="Recurrence")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    desired_capacity: Optional[int] = Field(default=None, alias="DesiredCapacity")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")


class EbsModel(BaseModel):
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    iops: Optional[int] = Field(default=None, alias="Iops")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    throughput: Optional[int] = Field(default=None, alias="Throughput")


class CancelInstanceRefreshTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")


class CapacityForecastModel(BaseModel):
    timestamps: List[datetime] = Field(alias="Timestamps")
    values: List[float] = Field(alias="Values")


class CompleteLifecycleActionTypeRequestModel(BaseModel):
    lifecycle_hook_name: str = Field(alias="LifecycleHookName")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    lifecycle_action_result: str = Field(alias="LifecycleActionResult")
    lifecycle_action_token: Optional[str] = Field(
        default=None, alias="LifecycleActionToken"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class LifecycleHookSpecificationModel(BaseModel):
    lifecycle_hook_name: str = Field(alias="LifecycleHookName")
    lifecycle_transition: str = Field(alias="LifecycleTransition")
    notification_metadata: Optional[str] = Field(
        default=None, alias="NotificationMetadata"
    )
    heartbeat_timeout: Optional[int] = Field(default=None, alias="HeartbeatTimeout")
    default_result: Optional[str] = Field(default=None, alias="DefaultResult")
    notification_target_arn: Optional[str] = Field(
        default=None, alias="NotificationTargetARN"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    value: Optional[str] = Field(default=None, alias="Value")
    propagate_at_launch: Optional[bool] = Field(default=None, alias="PropagateAtLaunch")


class InstanceMetadataOptionsModel(BaseModel):
    http_tokens: Optional[Literal["optional", "required"]] = Field(
        default=None, alias="HttpTokens"
    )
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="HttpPutResponseHopLimit"
    )
    http_endpoint: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="HttpEndpoint"
    )


class InstanceMonitoringModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class MetricDimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DeleteAutoScalingGroupTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    force_delete: Optional[bool] = Field(default=None, alias="ForceDelete")


class DeleteLifecycleHookTypeRequestModel(BaseModel):
    lifecycle_hook_name: str = Field(alias="LifecycleHookName")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")


class DeleteNotificationConfigurationTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    topic_arn: str = Field(alias="TopicARN")


class DeletePolicyTypeRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )


class DeleteScheduledActionTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    scheduled_action_name: str = Field(alias="ScheduledActionName")


class DeleteWarmPoolTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    force_delete: Optional[bool] = Field(default=None, alias="ForceDelete")


class DescribeAutoScalingInstancesTypeRequestModel(BaseModel):
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstanceRefreshesTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    instance_refresh_ids: Optional[Sequence[str]] = Field(
        default=None, alias="InstanceRefreshIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class LifecycleHookModel(BaseModel):
    lifecycle_hook_name: Optional[str] = Field(default=None, alias="LifecycleHookName")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    lifecycle_transition: Optional[str] = Field(
        default=None, alias="LifecycleTransition"
    )
    notification_target_arn: Optional[str] = Field(
        default=None, alias="NotificationTargetARN"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    notification_metadata: Optional[str] = Field(
        default=None, alias="NotificationMetadata"
    )
    heartbeat_timeout: Optional[int] = Field(default=None, alias="HeartbeatTimeout")
    global_timeout: Optional[int] = Field(default=None, alias="GlobalTimeout")
    default_result: Optional[str] = Field(default=None, alias="DefaultResult")


class DescribeLifecycleHooksTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    lifecycle_hook_names: Optional[Sequence[str]] = Field(
        default=None, alias="LifecycleHookNames"
    )


class DescribeLoadBalancerTargetGroupsRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class LoadBalancerTargetGroupStateModel(BaseModel):
    load_balancer_target_group_arn: Optional[str] = Field(
        default=None, alias="LoadBalancerTargetGroupARN"
    )
    state: Optional[str] = Field(default=None, alias="State")


class DescribeLoadBalancersRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class LoadBalancerStateModel(BaseModel):
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    state: Optional[str] = Field(default=None, alias="State")


class MetricCollectionTypeModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")


class MetricGranularityTypeModel(BaseModel):
    granularity: Optional[str] = Field(default=None, alias="Granularity")


class NotificationConfigurationModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    topic_arn: Optional[str] = Field(default=None, alias="TopicARN")
    notification_type: Optional[str] = Field(default=None, alias="NotificationType")


class DescribeNotificationConfigurationsTypeRequestModel(BaseModel):
    auto_scaling_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="AutoScalingGroupNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribePoliciesTypeRequestModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")
    policy_types: Optional[Sequence[str]] = Field(default=None, alias="PolicyTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeScalingActivitiesTypeRequestModel(BaseModel):
    activity_ids: Optional[Sequence[str]] = Field(default=None, alias="ActivityIds")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    include_deleted_groups: Optional[bool] = Field(
        default=None, alias="IncludeDeletedGroups"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeScheduledActionsTypeRequestModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    scheduled_action_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScheduledActionNames"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeTrafficSourcesRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    traffic_source_type: str = Field(alias="TrafficSourceType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class TrafficSourceStateModel(BaseModel):
    traffic_source: Optional[str] = Field(default=None, alias="TrafficSource")
    state: Optional[str] = Field(default=None, alias="State")


class DescribeWarmPoolTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DetachInstancesQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    should_decrement_desired_capacity: bool = Field(
        alias="ShouldDecrementDesiredCapacity"
    )
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class DetachLoadBalancerTargetGroupsTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    target_group_arns: Sequence[str] = Field(alias="TargetGroupARNs")


class DetachLoadBalancersTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    load_balancer_names: Sequence[str] = Field(alias="LoadBalancerNames")


class DisableMetricsCollectionQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")


class EnableMetricsCollectionQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    granularity: str = Field(alias="Granularity")
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")


class EnterStandbyQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    should_decrement_desired_capacity: bool = Field(
        alias="ShouldDecrementDesiredCapacity"
    )
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class ExecutePolicyTypeRequestModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    honor_cooldown: Optional[bool] = Field(default=None, alias="HonorCooldown")
    metric_value: Optional[float] = Field(default=None, alias="MetricValue")
    breach_threshold: Optional[float] = Field(default=None, alias="BreachThreshold")


class ExitStandbyQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class GetPredictiveScalingForecastTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    policy_name: str = Field(alias="PolicyName")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class InstanceRefreshLivePoolProgressModel(BaseModel):
    percentage_complete: Optional[int] = Field(default=None, alias="PercentageComplete")
    instances_to_update: Optional[int] = Field(default=None, alias="InstancesToUpdate")


class InstanceRefreshWarmPoolProgressModel(BaseModel):
    percentage_complete: Optional[int] = Field(default=None, alias="PercentageComplete")
    instances_to_update: Optional[int] = Field(default=None, alias="InstancesToUpdate")


class RefreshPreferencesModel(BaseModel):
    min_healthy_percentage: Optional[int] = Field(
        default=None, alias="MinHealthyPercentage"
    )
    instance_warmup: Optional[int] = Field(default=None, alias="InstanceWarmup")
    checkpoint_percentages: Optional[List[int]] = Field(
        default=None, alias="CheckpointPercentages"
    )
    checkpoint_delay: Optional[int] = Field(default=None, alias="CheckpointDelay")
    skip_matching: Optional[bool] = Field(default=None, alias="SkipMatching")
    auto_rollback: Optional[bool] = Field(default=None, alias="AutoRollback")
    scale_in_protected_instances: Optional[
        Literal["Ignore", "Refresh", "Wait"]
    ] = Field(default=None, alias="ScaleInProtectedInstances")
    standby_instances: Optional[Literal["Ignore", "Terminate", "Wait"]] = Field(
        default=None, alias="StandbyInstances"
    )


class MemoryGiBPerVCpuRequestModel(BaseModel):
    min: Optional[float] = Field(default=None, alias="Min")
    max: Optional[float] = Field(default=None, alias="Max")


class MemoryMiBRequestModel(BaseModel):
    min: int = Field(alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class NetworkBandwidthGbpsRequestModel(BaseModel):
    min: Optional[float] = Field(default=None, alias="Min")
    max: Optional[float] = Field(default=None, alias="Max")


class NetworkInterfaceCountRequestModel(BaseModel):
    min: Optional[int] = Field(default=None, alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class TotalLocalStorageGBRequestModel(BaseModel):
    min: Optional[float] = Field(default=None, alias="Min")
    max: Optional[float] = Field(default=None, alias="Max")


class VCpuCountRequestModel(BaseModel):
    min: int = Field(alias="Min")
    max: Optional[int] = Field(default=None, alias="Max")


class InstanceReusePolicyModel(BaseModel):
    reuse_on_scale_in: Optional[bool] = Field(default=None, alias="ReuseOnScaleIn")


class InstancesDistributionModel(BaseModel):
    on_demand_allocation_strategy: Optional[str] = Field(
        default=None, alias="OnDemandAllocationStrategy"
    )
    on_demand_base_capacity: Optional[int] = Field(
        default=None, alias="OnDemandBaseCapacity"
    )
    on_demand_percentage_above_base_capacity: Optional[int] = Field(
        default=None, alias="OnDemandPercentageAboveBaseCapacity"
    )
    spot_allocation_strategy: Optional[str] = Field(
        default=None, alias="SpotAllocationStrategy"
    )
    spot_instance_pools: Optional[int] = Field(default=None, alias="SpotInstancePools")
    spot_max_price: Optional[str] = Field(default=None, alias="SpotMaxPrice")


class LaunchConfigurationNameTypeRequestModel(BaseModel):
    launch_configuration_name: str = Field(alias="LaunchConfigurationName")


class LaunchConfigurationNamesTypeRequestModel(BaseModel):
    launch_configuration_names: Optional[Sequence[str]] = Field(
        default=None, alias="LaunchConfigurationNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class PredefinedMetricSpecificationModel(BaseModel):
    predefined_metric_type: Literal[
        "ALBRequestCountPerTarget",
        "ASGAverageCPUUtilization",
        "ASGAverageNetworkIn",
        "ASGAverageNetworkOut",
    ] = Field(alias="PredefinedMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class PredictiveScalingPredefinedLoadMetricModel(BaseModel):
    predefined_metric_type: Literal[
        "ALBTargetGroupRequestCount",
        "ASGTotalCPUUtilization",
        "ASGTotalNetworkIn",
        "ASGTotalNetworkOut",
    ] = Field(alias="PredefinedMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class PredictiveScalingPredefinedMetricPairModel(BaseModel):
    predefined_metric_type: Literal[
        "ALBRequestCount", "ASGCPUUtilization", "ASGNetworkIn", "ASGNetworkOut"
    ] = Field(alias="PredefinedMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class PredictiveScalingPredefinedScalingMetricModel(BaseModel):
    predefined_metric_type: Literal[
        "ALBRequestCountPerTarget",
        "ASGAverageCPUUtilization",
        "ASGAverageNetworkIn",
        "ASGAverageNetworkOut",
    ] = Field(alias="PredefinedMetricType")
    resource_label: Optional[str] = Field(default=None, alias="ResourceLabel")


class ProcessTypeModel(BaseModel):
    process_name: str = Field(alias="ProcessName")


class PutLifecycleHookTypeRequestModel(BaseModel):
    lifecycle_hook_name: str = Field(alias="LifecycleHookName")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    lifecycle_transition: Optional[str] = Field(
        default=None, alias="LifecycleTransition"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    notification_target_arn: Optional[str] = Field(
        default=None, alias="NotificationTargetARN"
    )
    notification_metadata: Optional[str] = Field(
        default=None, alias="NotificationMetadata"
    )
    heartbeat_timeout: Optional[int] = Field(default=None, alias="HeartbeatTimeout")
    default_result: Optional[str] = Field(default=None, alias="DefaultResult")


class PutNotificationConfigurationTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    topic_arn: str = Field(alias="TopicARN")
    notification_types: Sequence[str] = Field(alias="NotificationTypes")


class StepAdjustmentModel(BaseModel):
    scaling_adjustment: int = Field(alias="ScalingAdjustment")
    metric_interval_lower_bound: Optional[float] = Field(
        default=None, alias="MetricIntervalLowerBound"
    )
    metric_interval_upper_bound: Optional[float] = Field(
        default=None, alias="MetricIntervalUpperBound"
    )


class PutScheduledUpdateGroupActionTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    time: Optional[Union[datetime, str]] = Field(default=None, alias="Time")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    recurrence: Optional[str] = Field(default=None, alias="Recurrence")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    desired_capacity: Optional[int] = Field(default=None, alias="DesiredCapacity")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")


class RecordLifecycleActionHeartbeatTypeRequestModel(BaseModel):
    lifecycle_hook_name: str = Field(alias="LifecycleHookName")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    lifecycle_action_token: Optional[str] = Field(
        default=None, alias="LifecycleActionToken"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class RollbackInstanceRefreshTypeRequestModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )


class ScalingProcessQueryRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    scaling_processes: Optional[Sequence[str]] = Field(
        default=None, alias="ScalingProcesses"
    )


class ScheduledUpdateGroupActionModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    scheduled_action_name: Optional[str] = Field(
        default=None, alias="ScheduledActionName"
    )
    scheduled_action_arn: Optional[str] = Field(
        default=None, alias="ScheduledActionARN"
    )
    time: Optional[datetime] = Field(default=None, alias="Time")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    recurrence: Optional[str] = Field(default=None, alias="Recurrence")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    desired_capacity: Optional[int] = Field(default=None, alias="DesiredCapacity")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")


class SetDesiredCapacityTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    desired_capacity: int = Field(alias="DesiredCapacity")
    honor_cooldown: Optional[bool] = Field(default=None, alias="HonorCooldown")


class SetInstanceHealthQueryRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    health_status: str = Field(alias="HealthStatus")
    should_respect_grace_period: Optional[bool] = Field(
        default=None, alias="ShouldRespectGracePeriod"
    )


class SetInstanceProtectionQueryRequestModel(BaseModel):
    instance_ids: Sequence[str] = Field(alias="InstanceIds")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    protected_from_scale_in: bool = Field(alias="ProtectedFromScaleIn")


class TerminateInstanceInAutoScalingGroupTypeRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    should_decrement_desired_capacity: bool = Field(
        alias="ShouldDecrementDesiredCapacity"
    )


class ActivitiesTypeModel(BaseModel):
    activities: List[ActivityModel] = Field(alias="Activities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivityTypeModel(BaseModel):
    activity: ActivityModel = Field(alias="Activity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelInstanceRefreshAnswerModel(BaseModel):
    instance_refresh_id: str = Field(alias="InstanceRefreshId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountLimitsAnswerModel(BaseModel):
    max_number_of_auto_scaling_groups: int = Field(alias="MaxNumberOfAutoScalingGroups")
    max_number_of_launch_configurations: int = Field(
        alias="MaxNumberOfLaunchConfigurations"
    )
    number_of_auto_scaling_groups: int = Field(alias="NumberOfAutoScalingGroups")
    number_of_launch_configurations: int = Field(alias="NumberOfLaunchConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAutoScalingNotificationTypesAnswerModel(BaseModel):
    auto_scaling_notification_types: List[str] = Field(
        alias="AutoScalingNotificationTypes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLifecycleHookTypesAnswerModel(BaseModel):
    lifecycle_hook_types: List[str] = Field(alias="LifecycleHookTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTerminationPolicyTypesAnswerModel(BaseModel):
    termination_policy_types: List[str] = Field(alias="TerminationPolicyTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachInstancesAnswerModel(BaseModel):
    activities: List[ActivityModel] = Field(alias="Activities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnterStandbyAnswerModel(BaseModel):
    activities: List[ActivityModel] = Field(alias="Activities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExitStandbyAnswerModel(BaseModel):
    activities: List[ActivityModel] = Field(alias="Activities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackInstanceRefreshAnswerModel(BaseModel):
    instance_refresh_id: str = Field(alias="InstanceRefreshId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartInstanceRefreshAnswerModel(BaseModel):
    instance_refresh_id: str = Field(alias="InstanceRefreshId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAdjustmentTypesAnswerModel(BaseModel):
    adjustment_types: List[AdjustmentTypeModel] = Field(alias="AdjustmentTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyARNTypeModel(BaseModel):
    policy_arn: str = Field(alias="PolicyARN")
    alarms: List[AlarmModel] = Field(alias="Alarms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachTrafficSourcesTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    traffic_sources: Sequence[TrafficSourceIdentifierModel] = Field(
        alias="TrafficSources"
    )


class DetachTrafficSourcesTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    traffic_sources: Sequence[TrafficSourceIdentifierModel] = Field(
        alias="TrafficSources"
    )


class AutoScalingGroupNamesTypeRequestModel(BaseModel):
    auto_scaling_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="AutoScalingGroupNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeTagsTypeRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateModel(BaseModel):
    auto_scaling_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="AutoScalingGroupNames"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateModel(
    BaseModel
):
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateModel(
    BaseModel
):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeLoadBalancersRequestDescribeLoadBalancersPaginateModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateModel(
    BaseModel
):
    auto_scaling_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="AutoScalingGroupNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePoliciesTypeDescribePoliciesPaginateModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")
    policy_types: Optional[Sequence[str]] = Field(default=None, alias="PolicyTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateModel(BaseModel):
    activity_ids: Optional[Sequence[str]] = Field(default=None, alias="ActivityIds")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    include_deleted_groups: Optional[bool] = Field(
        default=None, alias="IncludeDeletedGroups"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScheduledActionsTypeDescribeScheduledActionsPaginateModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    scheduled_action_names: Optional[Sequence[str]] = Field(
        default=None, alias="ScheduledActionNames"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTagsTypeDescribeTagsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateModel(BaseModel):
    launch_configuration_names: Optional[Sequence[str]] = Field(
        default=None, alias="LaunchConfigurationNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class AutoScalingInstanceDetailsModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    availability_zone: str = Field(alias="AvailabilityZone")
    lifecycle_state: str = Field(alias="LifecycleState")
    health_status: str = Field(alias="HealthStatus")
    protected_from_scale_in: bool = Field(alias="ProtectedFromScaleIn")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    weighted_capacity: Optional[str] = Field(default=None, alias="WeightedCapacity")


class InstanceModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    availability_zone: str = Field(alias="AvailabilityZone")
    lifecycle_state: Literal[
        "Detached",
        "Detaching",
        "EnteringStandby",
        "InService",
        "Pending",
        "Pending:Proceed",
        "Pending:Wait",
        "Quarantined",
        "Standby",
        "Terminated",
        "Terminating",
        "Terminating:Proceed",
        "Terminating:Wait",
        "Warmed:Hibernated",
        "Warmed:Pending",
        "Warmed:Pending:Proceed",
        "Warmed:Pending:Wait",
        "Warmed:Running",
        "Warmed:Stopped",
        "Warmed:Terminated",
        "Warmed:Terminating",
        "Warmed:Terminating:Proceed",
        "Warmed:Terminating:Wait",
    ] = Field(alias="LifecycleState")
    health_status: str = Field(alias="HealthStatus")
    protected_from_scale_in: bool = Field(alias="ProtectedFromScaleIn")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    weighted_capacity: Optional[str] = Field(default=None, alias="WeightedCapacity")


class TagsTypeModel(BaseModel):
    tags: List[TagDescriptionModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteScheduledActionAnswerModel(BaseModel):
    failed_scheduled_actions: List[
        FailedScheduledUpdateGroupActionRequestModel
    ] = Field(alias="FailedScheduledActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutScheduledUpdateGroupActionAnswerModel(BaseModel):
    failed_scheduled_update_group_actions: List[
        FailedScheduledUpdateGroupActionRequestModel
    ] = Field(alias="FailedScheduledUpdateGroupActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutScheduledUpdateGroupActionTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    scheduled_update_group_actions: Sequence[
        ScheduledUpdateGroupActionRequestModel
    ] = Field(alias="ScheduledUpdateGroupActions")


class BlockDeviceMappingModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    virtual_name: Optional[str] = Field(default=None, alias="VirtualName")
    ebs: Optional[EbsModel] = Field(default=None, alias="Ebs")
    no_device: Optional[bool] = Field(default=None, alias="NoDevice")


class CreateOrUpdateTagsTypeRequestModel(BaseModel):
    tags: Sequence[TagModel] = Field(alias="Tags")


class DeleteTagsTypeRequestModel(BaseModel):
    tags: Sequence[TagModel] = Field(alias="Tags")


class MetricModel(BaseModel):
    namespace: str = Field(alias="Namespace")
    metric_name: str = Field(alias="MetricName")
    dimensions: Optional[List[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )


class DescribeLifecycleHooksAnswerModel(BaseModel):
    lifecycle_hooks: List[LifecycleHookModel] = Field(alias="LifecycleHooks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancerTargetGroupsResponseModel(BaseModel):
    load_balancer_target_groups: List[LoadBalancerTargetGroupStateModel] = Field(
        alias="LoadBalancerTargetGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBalancersResponseModel(BaseModel):
    load_balancers: List[LoadBalancerStateModel] = Field(alias="LoadBalancers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMetricCollectionTypesAnswerModel(BaseModel):
    metrics: List[MetricCollectionTypeModel] = Field(alias="Metrics")
    granularities: List[MetricGranularityTypeModel] = Field(alias="Granularities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNotificationConfigurationsAnswerModel(BaseModel):
    notification_configurations: List[NotificationConfigurationModel] = Field(
        alias="NotificationConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrafficSourcesResponseModel(BaseModel):
    traffic_sources: List[TrafficSourceStateModel] = Field(alias="TrafficSources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceRefreshProgressDetailsModel(BaseModel):
    live_pool_progress: Optional[InstanceRefreshLivePoolProgressModel] = Field(
        default=None, alias="LivePoolProgress"
    )
    warm_pool_progress: Optional[InstanceRefreshWarmPoolProgressModel] = Field(
        default=None, alias="WarmPoolProgress"
    )


class InstanceRequirementsModel(BaseModel):
    vcpu_count: VCpuCountRequestModel = Field(alias="VCpuCount")
    memory_mi_b: MemoryMiBRequestModel = Field(alias="MemoryMiB")
    cpu_manufacturers: Optional[
        Sequence[Literal["amazon-web-services", "amd", "intel"]]
    ] = Field(default=None, alias="CpuManufacturers")
    memory_gi_bper_vcpu: Optional[MemoryGiBPerVCpuRequestModel] = Field(
        default=None, alias="MemoryGiBPerVCpu"
    )
    excluded_instance_types: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedInstanceTypes"
    )
    instance_generations: Optional[Sequence[Literal["current", "previous"]]] = Field(
        default=None, alias="InstanceGenerations"
    )
    spot_max_price_percentage_over_lowest_price: Optional[int] = Field(
        default=None, alias="SpotMaxPricePercentageOverLowestPrice"
    )
    on_demand_max_price_percentage_over_lowest_price: Optional[int] = Field(
        default=None, alias="OnDemandMaxPricePercentageOverLowestPrice"
    )
    bare_metal: Optional[Literal["excluded", "included", "required"]] = Field(
        default=None, alias="BareMetal"
    )
    burstable_performance: Optional[
        Literal["excluded", "included", "required"]
    ] = Field(default=None, alias="BurstablePerformance")
    require_hibernate_support: Optional[bool] = Field(
        default=None, alias="RequireHibernateSupport"
    )
    network_interface_count: Optional[NetworkInterfaceCountRequestModel] = Field(
        default=None, alias="NetworkInterfaceCount"
    )
    local_storage: Optional[Literal["excluded", "included", "required"]] = Field(
        default=None, alias="LocalStorage"
    )
    local_storage_types: Optional[Sequence[Literal["hdd", "ssd"]]] = Field(
        default=None, alias="LocalStorageTypes"
    )
    total_local_storage_gb: Optional[TotalLocalStorageGBRequestModel] = Field(
        default=None, alias="TotalLocalStorageGB"
    )
    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbpsRequestModel] = Field(
        default=None, alias="BaselineEbsBandwidthMbps"
    )
    accelerator_types: Optional[Sequence[Literal["fpga", "gpu", "inference"]]] = Field(
        default=None, alias="AcceleratorTypes"
    )
    accelerator_count: Optional[AcceleratorCountRequestModel] = Field(
        default=None, alias="AcceleratorCount"
    )
    accelerator_manufacturers: Optional[
        Sequence[Literal["amazon-web-services", "amd", "nvidia", "xilinx"]]
    ] = Field(default=None, alias="AcceleratorManufacturers")
    accelerator_names: Optional[
        Sequence[Literal["a100", "k80", "m60", "radeon-pro-v520", "t4", "v100", "vu9p"]]
    ] = Field(default=None, alias="AcceleratorNames")
    accelerator_total_memory_mi_b: Optional[
        AcceleratorTotalMemoryMiBRequestModel
    ] = Field(default=None, alias="AcceleratorTotalMemoryMiB")
    network_bandwidth_gbps: Optional[NetworkBandwidthGbpsRequestModel] = Field(
        default=None, alias="NetworkBandwidthGbps"
    )
    allowed_instance_types: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedInstanceTypes"
    )


class PutWarmPoolTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    max_group_prepared_capacity: Optional[int] = Field(
        default=None, alias="MaxGroupPreparedCapacity"
    )
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    pool_state: Optional[Literal["Hibernated", "Running", "Stopped"]] = Field(
        default=None, alias="PoolState"
    )
    instance_reuse_policy: Optional[InstanceReusePolicyModel] = Field(
        default=None, alias="InstanceReusePolicy"
    )


class WarmPoolConfigurationModel(BaseModel):
    max_group_prepared_capacity: Optional[int] = Field(
        default=None, alias="MaxGroupPreparedCapacity"
    )
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    pool_state: Optional[Literal["Hibernated", "Running", "Stopped"]] = Field(
        default=None, alias="PoolState"
    )
    status: Optional[Literal["PendingDelete"]] = Field(default=None, alias="Status")
    instance_reuse_policy: Optional[InstanceReusePolicyModel] = Field(
        default=None, alias="InstanceReusePolicy"
    )


class ProcessesTypeModel(BaseModel):
    processes: List[ProcessTypeModel] = Field(alias="Processes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduledActionsTypeModel(BaseModel):
    scheduled_update_group_actions: List[ScheduledUpdateGroupActionModel] = Field(
        alias="ScheduledUpdateGroupActions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoScalingInstancesTypeModel(BaseModel):
    auto_scaling_instances: List[AutoScalingInstanceDetailsModel] = Field(
        alias="AutoScalingInstances"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLaunchConfigurationTypeRequestModel(BaseModel):
    launch_configuration_name: str = Field(alias="LaunchConfigurationName")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    classic_link_vp_cid: Optional[str] = Field(default=None, alias="ClassicLinkVPCId")
    classic_link_vp_csecurity_groups: Optional[Sequence[str]] = Field(
        default=None, alias="ClassicLinkVPCSecurityGroups"
    )
    user_data: Optional[str] = Field(default=None, alias="UserData")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    kernel_id: Optional[str] = Field(default=None, alias="KernelId")
    ramdisk_id: Optional[str] = Field(default=None, alias="RamdiskId")
    block_device_mappings: Optional[Sequence[BlockDeviceMappingModel]] = Field(
        default=None, alias="BlockDeviceMappings"
    )
    instance_monitoring: Optional[InstanceMonitoringModel] = Field(
        default=None, alias="InstanceMonitoring"
    )
    spot_price: Optional[str] = Field(default=None, alias="SpotPrice")
    iam_instance_profile: Optional[str] = Field(
        default=None, alias="IamInstanceProfile"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    placement_tenancy: Optional[str] = Field(default=None, alias="PlacementTenancy")
    metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="MetadataOptions"
    )


class LaunchConfigurationModel(BaseModel):
    launch_configuration_name: str = Field(alias="LaunchConfigurationName")
    image_id: str = Field(alias="ImageId")
    instance_type: str = Field(alias="InstanceType")
    created_time: datetime = Field(alias="CreatedTime")
    launch_configuration_arn: Optional[str] = Field(
        default=None, alias="LaunchConfigurationARN"
    )
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    classic_link_vp_cid: Optional[str] = Field(default=None, alias="ClassicLinkVPCId")
    classic_link_vp_csecurity_groups: Optional[List[str]] = Field(
        default=None, alias="ClassicLinkVPCSecurityGroups"
    )
    user_data: Optional[str] = Field(default=None, alias="UserData")
    kernel_id: Optional[str] = Field(default=None, alias="KernelId")
    ramdisk_id: Optional[str] = Field(default=None, alias="RamdiskId")
    block_device_mappings: Optional[List[BlockDeviceMappingModel]] = Field(
        default=None, alias="BlockDeviceMappings"
    )
    instance_monitoring: Optional[InstanceMonitoringModel] = Field(
        default=None, alias="InstanceMonitoring"
    )
    spot_price: Optional[str] = Field(default=None, alias="SpotPrice")
    iam_instance_profile: Optional[str] = Field(
        default=None, alias="IamInstanceProfile"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    placement_tenancy: Optional[str] = Field(default=None, alias="PlacementTenancy")
    metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="MetadataOptions"
    )


class MetricStatModel(BaseModel):
    metric: MetricModel = Field(alias="Metric")
    stat: str = Field(alias="Stat")
    unit: Optional[str] = Field(default=None, alias="Unit")


class TargetTrackingMetricStatModel(BaseModel):
    metric: MetricModel = Field(alias="Metric")
    stat: str = Field(alias="Stat")
    unit: Optional[str] = Field(default=None, alias="Unit")


class RollbackDetailsModel(BaseModel):
    rollback_reason: Optional[str] = Field(default=None, alias="RollbackReason")
    rollback_start_time: Optional[datetime] = Field(
        default=None, alias="RollbackStartTime"
    )
    percentage_complete_on_rollback: Optional[int] = Field(
        default=None, alias="PercentageCompleteOnRollback"
    )
    instances_to_update_on_rollback: Optional[int] = Field(
        default=None, alias="InstancesToUpdateOnRollback"
    )
    progress_details_on_rollback: Optional[InstanceRefreshProgressDetailsModel] = Field(
        default=None, alias="ProgressDetailsOnRollback"
    )


class LaunchTemplateOverridesModel(BaseModel):
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    weighted_capacity: Optional[str] = Field(default=None, alias="WeightedCapacity")
    launch_template_specification: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplateSpecification"
    )
    instance_requirements: Optional[InstanceRequirementsModel] = Field(
        default=None, alias="InstanceRequirements"
    )


class DescribeWarmPoolAnswerModel(BaseModel):
    warm_pool_configuration: WarmPoolConfigurationModel = Field(
        alias="WarmPoolConfiguration"
    )
    instances: List[InstanceModel] = Field(alias="Instances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LaunchConfigurationsTypeModel(BaseModel):
    launch_configurations: List[LaunchConfigurationModel] = Field(
        alias="LaunchConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricDataQueryModel(BaseModel):
    id: str = Field(alias="Id")
    expression: Optional[str] = Field(default=None, alias="Expression")
    metric_stat: Optional[MetricStatModel] = Field(default=None, alias="MetricStat")
    label: Optional[str] = Field(default=None, alias="Label")
    return_data: Optional[bool] = Field(default=None, alias="ReturnData")


class TargetTrackingMetricDataQueryModel(BaseModel):
    id: str = Field(alias="Id")
    expression: Optional[str] = Field(default=None, alias="Expression")
    metric_stat: Optional[TargetTrackingMetricStatModel] = Field(
        default=None, alias="MetricStat"
    )
    label: Optional[str] = Field(default=None, alias="Label")
    return_data: Optional[bool] = Field(default=None, alias="ReturnData")


class LaunchTemplateModel(BaseModel):
    launch_template_specification: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplateSpecification"
    )
    overrides: Optional[Sequence[LaunchTemplateOverridesModel]] = Field(
        default=None, alias="Overrides"
    )


class PredictiveScalingCustomizedCapacityMetricModel(BaseModel):
    metric_data_queries: List[MetricDataQueryModel] = Field(alias="MetricDataQueries")


class PredictiveScalingCustomizedLoadMetricModel(BaseModel):
    metric_data_queries: List[MetricDataQueryModel] = Field(alias="MetricDataQueries")


class PredictiveScalingCustomizedScalingMetricModel(BaseModel):
    metric_data_queries: List[MetricDataQueryModel] = Field(alias="MetricDataQueries")


class CustomizedMetricSpecificationModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    dimensions: Optional[List[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="Statistic")
    unit: Optional[str] = Field(default=None, alias="Unit")
    metrics: Optional[List[TargetTrackingMetricDataQueryModel]] = Field(
        default=None, alias="Metrics"
    )


class MixedInstancesPolicyModel(BaseModel):
    launch_template: Optional[LaunchTemplateModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    instances_distribution: Optional[InstancesDistributionModel] = Field(
        default=None, alias="InstancesDistribution"
    )


class PredictiveScalingMetricSpecificationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    predefined_metric_pair_specification: Optional[
        PredictiveScalingPredefinedMetricPairModel
    ] = Field(default=None, alias="PredefinedMetricPairSpecification")
    predefined_scaling_metric_specification: Optional[
        PredictiveScalingPredefinedScalingMetricModel
    ] = Field(default=None, alias="PredefinedScalingMetricSpecification")
    predefined_load_metric_specification: Optional[
        PredictiveScalingPredefinedLoadMetricModel
    ] = Field(default=None, alias="PredefinedLoadMetricSpecification")
    customized_scaling_metric_specification: Optional[
        PredictiveScalingCustomizedScalingMetricModel
    ] = Field(default=None, alias="CustomizedScalingMetricSpecification")
    customized_load_metric_specification: Optional[
        PredictiveScalingCustomizedLoadMetricModel
    ] = Field(default=None, alias="CustomizedLoadMetricSpecification")
    customized_capacity_metric_specification: Optional[
        PredictiveScalingCustomizedCapacityMetricModel
    ] = Field(default=None, alias="CustomizedCapacityMetricSpecification")


class TargetTrackingConfigurationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    predefined_metric_specification: Optional[
        PredefinedMetricSpecificationModel
    ] = Field(default=None, alias="PredefinedMetricSpecification")
    customized_metric_specification: Optional[
        CustomizedMetricSpecificationModel
    ] = Field(default=None, alias="CustomizedMetricSpecification")
    disable_scale_in: Optional[bool] = Field(default=None, alias="DisableScaleIn")


class AutoScalingGroupModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    min_size: int = Field(alias="MinSize")
    max_size: int = Field(alias="MaxSize")
    desired_capacity: int = Field(alias="DesiredCapacity")
    default_cooldown: int = Field(alias="DefaultCooldown")
    availability_zones: List[str] = Field(alias="AvailabilityZones")
    health_check_type: str = Field(alias="HealthCheckType")
    created_time: datetime = Field(alias="CreatedTime")
    auto_scaling_group_arn: Optional[str] = Field(
        default=None, alias="AutoScalingGroupARN"
    )
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    mixed_instances_policy: Optional[MixedInstancesPolicyModel] = Field(
        default=None, alias="MixedInstancesPolicy"
    )
    predicted_capacity: Optional[int] = Field(default=None, alias="PredictedCapacity")
    load_balancer_names: Optional[List[str]] = Field(
        default=None, alias="LoadBalancerNames"
    )
    target_group_arns: Optional[List[str]] = Field(
        default=None, alias="TargetGroupARNs"
    )
    health_check_grace_period: Optional[int] = Field(
        default=None, alias="HealthCheckGracePeriod"
    )
    instances: Optional[List[InstanceModel]] = Field(default=None, alias="Instances")
    suspended_processes: Optional[List[SuspendedProcessModel]] = Field(
        default=None, alias="SuspendedProcesses"
    )
    placement_group: Optional[str] = Field(default=None, alias="PlacementGroup")
    vp_czone_identifier: Optional[str] = Field(default=None, alias="VPCZoneIdentifier")
    enabled_metrics: Optional[List[EnabledMetricModel]] = Field(
        default=None, alias="EnabledMetrics"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    tags: Optional[List[TagDescriptionModel]] = Field(default=None, alias="Tags")
    termination_policies: Optional[List[str]] = Field(
        default=None, alias="TerminationPolicies"
    )
    new_instances_protected_from_scale_in: Optional[bool] = Field(
        default=None, alias="NewInstancesProtectedFromScaleIn"
    )
    service_linked_role_arn: Optional[str] = Field(
        default=None, alias="ServiceLinkedRoleARN"
    )
    max_instance_lifetime: Optional[int] = Field(
        default=None, alias="MaxInstanceLifetime"
    )
    capacity_rebalance: Optional[bool] = Field(default=None, alias="CapacityRebalance")
    warm_pool_configuration: Optional[WarmPoolConfigurationModel] = Field(
        default=None, alias="WarmPoolConfiguration"
    )
    warm_pool_size: Optional[int] = Field(default=None, alias="WarmPoolSize")
    context: Optional[str] = Field(default=None, alias="Context")
    desired_capacity_type: Optional[str] = Field(
        default=None, alias="DesiredCapacityType"
    )
    default_instance_warmup: Optional[int] = Field(
        default=None, alias="DefaultInstanceWarmup"
    )
    traffic_sources: Optional[List[TrafficSourceIdentifierModel]] = Field(
        default=None, alias="TrafficSources"
    )


class CreateAutoScalingGroupTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    min_size: int = Field(alias="MinSize")
    max_size: int = Field(alias="MaxSize")
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    mixed_instances_policy: Optional[MixedInstancesPolicyModel] = Field(
        default=None, alias="MixedInstancesPolicy"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    desired_capacity: Optional[int] = Field(default=None, alias="DesiredCapacity")
    default_cooldown: Optional[int] = Field(default=None, alias="DefaultCooldown")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    load_balancer_names: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerNames"
    )
    target_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="TargetGroupARNs"
    )
    health_check_type: Optional[str] = Field(default=None, alias="HealthCheckType")
    health_check_grace_period: Optional[int] = Field(
        default=None, alias="HealthCheckGracePeriod"
    )
    placement_group: Optional[str] = Field(default=None, alias="PlacementGroup")
    vp_czone_identifier: Optional[str] = Field(default=None, alias="VPCZoneIdentifier")
    termination_policies: Optional[Sequence[str]] = Field(
        default=None, alias="TerminationPolicies"
    )
    new_instances_protected_from_scale_in: Optional[bool] = Field(
        default=None, alias="NewInstancesProtectedFromScaleIn"
    )
    capacity_rebalance: Optional[bool] = Field(default=None, alias="CapacityRebalance")
    lifecycle_hook_specification_list: Optional[
        Sequence[LifecycleHookSpecificationModel]
    ] = Field(default=None, alias="LifecycleHookSpecificationList")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    service_linked_role_arn: Optional[str] = Field(
        default=None, alias="ServiceLinkedRoleARN"
    )
    max_instance_lifetime: Optional[int] = Field(
        default=None, alias="MaxInstanceLifetime"
    )
    context: Optional[str] = Field(default=None, alias="Context")
    desired_capacity_type: Optional[str] = Field(
        default=None, alias="DesiredCapacityType"
    )
    default_instance_warmup: Optional[int] = Field(
        default=None, alias="DefaultInstanceWarmup"
    )
    traffic_sources: Optional[Sequence[TrafficSourceIdentifierModel]] = Field(
        default=None, alias="TrafficSources"
    )


class DesiredConfigurationModel(BaseModel):
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    mixed_instances_policy: Optional[MixedInstancesPolicyModel] = Field(
        default=None, alias="MixedInstancesPolicy"
    )


class UpdateAutoScalingGroupTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="LaunchTemplate"
    )
    mixed_instances_policy: Optional[MixedInstancesPolicyModel] = Field(
        default=None, alias="MixedInstancesPolicy"
    )
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    desired_capacity: Optional[int] = Field(default=None, alias="DesiredCapacity")
    default_cooldown: Optional[int] = Field(default=None, alias="DefaultCooldown")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    health_check_type: Optional[str] = Field(default=None, alias="HealthCheckType")
    health_check_grace_period: Optional[int] = Field(
        default=None, alias="HealthCheckGracePeriod"
    )
    placement_group: Optional[str] = Field(default=None, alias="PlacementGroup")
    vp_czone_identifier: Optional[str] = Field(default=None, alias="VPCZoneIdentifier")
    termination_policies: Optional[Sequence[str]] = Field(
        default=None, alias="TerminationPolicies"
    )
    new_instances_protected_from_scale_in: Optional[bool] = Field(
        default=None, alias="NewInstancesProtectedFromScaleIn"
    )
    service_linked_role_arn: Optional[str] = Field(
        default=None, alias="ServiceLinkedRoleARN"
    )
    max_instance_lifetime: Optional[int] = Field(
        default=None, alias="MaxInstanceLifetime"
    )
    capacity_rebalance: Optional[bool] = Field(default=None, alias="CapacityRebalance")
    context: Optional[str] = Field(default=None, alias="Context")
    desired_capacity_type: Optional[str] = Field(
        default=None, alias="DesiredCapacityType"
    )
    default_instance_warmup: Optional[int] = Field(
        default=None, alias="DefaultInstanceWarmup"
    )


class LoadForecastModel(BaseModel):
    timestamps: List[datetime] = Field(alias="Timestamps")
    values: List[float] = Field(alias="Values")
    metric_specification: PredictiveScalingMetricSpecificationModel = Field(
        alias="MetricSpecification"
    )


class PredictiveScalingConfigurationModel(BaseModel):
    metric_specifications: List[PredictiveScalingMetricSpecificationModel] = Field(
        alias="MetricSpecifications"
    )
    mode: Optional[Literal["ForecastAndScale", "ForecastOnly"]] = Field(
        default=None, alias="Mode"
    )
    scheduling_buffer_time: Optional[int] = Field(
        default=None, alias="SchedulingBufferTime"
    )
    max_capacity_breach_behavior: Optional[
        Literal["HonorMaxCapacity", "IncreaseMaxCapacity"]
    ] = Field(default=None, alias="MaxCapacityBreachBehavior")
    max_capacity_buffer: Optional[int] = Field(default=None, alias="MaxCapacityBuffer")


class AutoScalingGroupsTypeModel(BaseModel):
    auto_scaling_groups: List[AutoScalingGroupModel] = Field(alias="AutoScalingGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceRefreshModel(BaseModel):
    instance_refresh_id: Optional[str] = Field(default=None, alias="InstanceRefreshId")
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    status: Optional[
        Literal[
            "Cancelled",
            "Cancelling",
            "Failed",
            "InProgress",
            "Pending",
            "RollbackFailed",
            "RollbackInProgress",
            "RollbackSuccessful",
            "Successful",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    percentage_complete: Optional[int] = Field(default=None, alias="PercentageComplete")
    instances_to_update: Optional[int] = Field(default=None, alias="InstancesToUpdate")
    progress_details: Optional[InstanceRefreshProgressDetailsModel] = Field(
        default=None, alias="ProgressDetails"
    )
    preferences: Optional[RefreshPreferencesModel] = Field(
        default=None, alias="Preferences"
    )
    desired_configuration: Optional[DesiredConfigurationModel] = Field(
        default=None, alias="DesiredConfiguration"
    )
    rollback_details: Optional[RollbackDetailsModel] = Field(
        default=None, alias="RollbackDetails"
    )


class StartInstanceRefreshTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    strategy: Optional[Literal["Rolling"]] = Field(default=None, alias="Strategy")
    desired_configuration: Optional[DesiredConfigurationModel] = Field(
        default=None, alias="DesiredConfiguration"
    )
    preferences: Optional[RefreshPreferencesModel] = Field(
        default=None, alias="Preferences"
    )


class GetPredictiveScalingForecastAnswerModel(BaseModel):
    load_forecast: List[LoadForecastModel] = Field(alias="LoadForecast")
    capacity_forecast: CapacityForecastModel = Field(alias="CapacityForecast")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutScalingPolicyTypeRequestModel(BaseModel):
    auto_scaling_group_name: str = Field(alias="AutoScalingGroupName")
    policy_name: str = Field(alias="PolicyName")
    policy_type: Optional[str] = Field(default=None, alias="PolicyType")
    adjustment_type: Optional[str] = Field(default=None, alias="AdjustmentType")
    min_adjustment_step: Optional[int] = Field(default=None, alias="MinAdjustmentStep")
    min_adjustment_magnitude: Optional[int] = Field(
        default=None, alias="MinAdjustmentMagnitude"
    )
    scaling_adjustment: Optional[int] = Field(default=None, alias="ScalingAdjustment")
    cooldown: Optional[int] = Field(default=None, alias="Cooldown")
    metric_aggregation_type: Optional[str] = Field(
        default=None, alias="MetricAggregationType"
    )
    step_adjustments: Optional[Sequence[StepAdjustmentModel]] = Field(
        default=None, alias="StepAdjustments"
    )
    estimated_instance_warmup: Optional[int] = Field(
        default=None, alias="EstimatedInstanceWarmup"
    )
    target_tracking_configuration: Optional[TargetTrackingConfigurationModel] = Field(
        default=None, alias="TargetTrackingConfiguration"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    predictive_scaling_configuration: Optional[
        PredictiveScalingConfigurationModel
    ] = Field(default=None, alias="PredictiveScalingConfiguration")


class ScalingPolicyModel(BaseModel):
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="AutoScalingGroupName"
    )
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyARN")
    policy_type: Optional[str] = Field(default=None, alias="PolicyType")
    adjustment_type: Optional[str] = Field(default=None, alias="AdjustmentType")
    min_adjustment_step: Optional[int] = Field(default=None, alias="MinAdjustmentStep")
    min_adjustment_magnitude: Optional[int] = Field(
        default=None, alias="MinAdjustmentMagnitude"
    )
    scaling_adjustment: Optional[int] = Field(default=None, alias="ScalingAdjustment")
    cooldown: Optional[int] = Field(default=None, alias="Cooldown")
    step_adjustments: Optional[List[StepAdjustmentModel]] = Field(
        default=None, alias="StepAdjustments"
    )
    metric_aggregation_type: Optional[str] = Field(
        default=None, alias="MetricAggregationType"
    )
    estimated_instance_warmup: Optional[int] = Field(
        default=None, alias="EstimatedInstanceWarmup"
    )
    alarms: Optional[List[AlarmModel]] = Field(default=None, alias="Alarms")
    target_tracking_configuration: Optional[TargetTrackingConfigurationModel] = Field(
        default=None, alias="TargetTrackingConfiguration"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    predictive_scaling_configuration: Optional[
        PredictiveScalingConfigurationModel
    ] = Field(default=None, alias="PredictiveScalingConfiguration")


class DescribeInstanceRefreshesAnswerModel(BaseModel):
    instance_refreshes: List[InstanceRefreshModel] = Field(alias="InstanceRefreshes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PoliciesTypeModel(BaseModel):
    scaling_policies: List[ScalingPolicyModel] = Field(alias="ScalingPolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
