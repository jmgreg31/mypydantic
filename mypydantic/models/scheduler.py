# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AwsVpcConfigurationModel(BaseModel):
    subnets: Sequence[str] = Field(alias="Subnets")
    assign_public_ip: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AssignPublicIp"
    )
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )


class CapacityProviderStrategyItemModel(BaseModel):
    capacity_provider: str = Field(alias="capacityProvider")
    base: Optional[int] = Field(default=None, alias="base")
    weight: Optional[int] = Field(default=None, alias="weight")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FlexibleTimeWindowModel(BaseModel):
    mode: Literal["FLEXIBLE", "OFF"] = Field(alias="Mode")
    maximum_window_in_minutes: Optional[int] = Field(
        default=None, alias="MaximumWindowInMinutes"
    )


class DeadLetterConfigModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class DeleteScheduleGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteScheduleInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class PlacementConstraintModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="expression")
    type: Optional[Literal["distinctInstance", "memberOf"]] = Field(
        default=None, alias="type"
    )


class PlacementStrategyModel(BaseModel):
    field: Optional[str] = Field(default=None, alias="field")
    type: Optional[Literal["binpack", "random", "spread"]] = Field(
        default=None, alias="type"
    )


class EventBridgeParametersModel(BaseModel):
    detail_type: str = Field(alias="DetailType")
    source: str = Field(alias="Source")


class GetScheduleGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetScheduleInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class KinesisParametersModel(BaseModel):
    partition_key: str = Field(alias="PartitionKey")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListScheduleGroupsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ScheduleGroupSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    last_modification_date: Optional[datetime] = Field(
        default=None, alias="LastModificationDate"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "DELETING"]] = Field(default=None, alias="State")


class ListSchedulesInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RetryPolicyModel(BaseModel):
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )


class SageMakerPipelineParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class TargetSummaryModel(BaseModel):
    arn: str = Field(alias="Arn")


class SqsParametersModel(BaseModel):
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class NetworkConfigurationModel(BaseModel):
    awsvpc_configuration: Optional[AwsVpcConfigurationModel] = Field(
        default=None, alias="awsvpcConfiguration"
    )


class CreateScheduleGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateScheduleGroupOutputModel(BaseModel):
    schedule_group_arn: str = Field(alias="ScheduleGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduleOutputModel(BaseModel):
    schedule_arn: str = Field(alias="ScheduleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetScheduleGroupOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_date: datetime = Field(alias="CreationDate")
    last_modification_date: datetime = Field(alias="LastModificationDate")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "DELETING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScheduleOutputModel(BaseModel):
    schedule_arn: str = Field(alias="ScheduleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListScheduleGroupsInputListScheduleGroupsPaginateModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchedulesInputListSchedulesPaginateModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListScheduleGroupsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schedule_groups: List[ScheduleGroupSummaryModel] = Field(alias="ScheduleGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SageMakerPipelineParametersModel(BaseModel):
    pipeline_parameter_list: Optional[
        Sequence[SageMakerPipelineParameterModel]
    ] = Field(default=None, alias="PipelineParameterList")


class ScheduleSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    last_modification_date: Optional[datetime] = Field(
        default=None, alias="LastModificationDate"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    target: Optional[TargetSummaryModel] = Field(default=None, alias="Target")


class EcsParametersModel(BaseModel):
    task_definition_arn: str = Field(alias="TaskDefinitionArn")
    capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="CapacityProviderStrategy")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="EnableECSManagedTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="EnableExecuteCommand"
    )
    group: Optional[str] = Field(default=None, alias="Group")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="LaunchType"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    placement_constraints: Optional[Sequence[PlacementConstraintModel]] = Field(
        default=None, alias="PlacementConstraints"
    )
    placement_strategy: Optional[Sequence[PlacementStrategyModel]] = Field(
        default=None, alias="PlacementStrategy"
    )
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    propagate_tags: Optional[Literal["TASK_DEFINITION"]] = Field(
        default=None, alias="PropagateTags"
    )
    reference_id: Optional[str] = Field(default=None, alias="ReferenceId")
    tags: Optional[Sequence[Mapping[str, str]]] = Field(default=None, alias="Tags")
    task_count: Optional[int] = Field(default=None, alias="TaskCount")


class ListSchedulesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schedules: List[ScheduleSummaryModel] = Field(alias="Schedules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetModel(BaseModel):
    arn: str = Field(alias="Arn")
    role_arn: str = Field(alias="RoleArn")
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    ecs_parameters: Optional[EcsParametersModel] = Field(
        default=None, alias="EcsParameters"
    )
    event_bridge_parameters: Optional[EventBridgeParametersModel] = Field(
        default=None, alias="EventBridgeParameters"
    )
    input: Optional[str] = Field(default=None, alias="Input")
    kinesis_parameters: Optional[KinesisParametersModel] = Field(
        default=None, alias="KinesisParameters"
    )
    retry_policy: Optional[RetryPolicyModel] = Field(default=None, alias="RetryPolicy")
    sage_maker_pipeline_parameters: Optional[SageMakerPipelineParametersModel] = Field(
        default=None, alias="SageMakerPipelineParameters"
    )
    sqs_parameters: Optional[SqsParametersModel] = Field(
        default=None, alias="SqsParameters"
    )


class CreateScheduleInputRequestModel(BaseModel):
    flexible_time_window: FlexibleTimeWindowModel = Field(alias="FlexibleTimeWindow")
    name: str = Field(alias="Name")
    schedule_expression: str = Field(alias="ScheduleExpression")
    target: TargetModel = Field(alias="Target")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    schedule_expression_timezone: Optional[str] = Field(
        default=None, alias="ScheduleExpressionTimezone"
    )
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class GetScheduleOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_date: datetime = Field(alias="CreationDate")
    description: str = Field(alias="Description")
    end_date: datetime = Field(alias="EndDate")
    flexible_time_window: FlexibleTimeWindowModel = Field(alias="FlexibleTimeWindow")
    group_name: str = Field(alias="GroupName")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    last_modification_date: datetime = Field(alias="LastModificationDate")
    name: str = Field(alias="Name")
    schedule_expression: str = Field(alias="ScheduleExpression")
    schedule_expression_timezone: str = Field(alias="ScheduleExpressionTimezone")
    start_date: datetime = Field(alias="StartDate")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    target: TargetModel = Field(alias="Target")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScheduleInputRequestModel(BaseModel):
    flexible_time_window: FlexibleTimeWindowModel = Field(alias="FlexibleTimeWindow")
    name: str = Field(alias="Name")
    schedule_expression: str = Field(alias="ScheduleExpression")
    target: TargetModel = Field(alias="Target")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="EndDate")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    schedule_expression_timezone: Optional[str] = Field(
        default=None, alias="ScheduleExpressionTimezone"
    )
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="StartDate")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
