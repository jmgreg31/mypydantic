# Model Generated: Thu Mar  2 21:56:22 2023

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


class BatchArrayPropertiesModel(BaseModel):
    size: Optional[int] = Field(default=None, alias="Size")


class BatchEnvironmentVariableModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class BatchResourceRequirementModel(BaseModel):
    type: Literal["GPU", "MEMORY", "VCPU"] = Field(alias="Type")
    value: str = Field(alias="Value")


class BatchJobDependencyModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    type: Optional[Literal["N_TO_N", "SEQUENTIAL"]] = Field(default=None, alias="Type")


class BatchRetryStrategyModel(BaseModel):
    attempts: Optional[int] = Field(default=None, alias="Attempts")


class CapacityProviderStrategyItemModel(BaseModel):
    capacity_provider: str = Field(alias="capacityProvider")
    base: Optional[int] = Field(default=None, alias="base")
    weight: Optional[int] = Field(default=None, alias="weight")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeadLetterConfigModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class DeletePipeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribePipeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class EcsEnvironmentFileModel(BaseModel):
    type: Literal["s3"] = Field(alias="type")
    value: str = Field(alias="value")


class EcsEnvironmentVariableModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class EcsResourceRequirementModel(BaseModel):
    type: Literal["GPU", "InferenceAccelerator"] = Field(alias="type")
    value: str = Field(alias="value")


class EcsEphemeralStorageModel(BaseModel):
    size_in_gi_b: int = Field(alias="sizeInGiB")


class EcsInferenceAcceleratorOverrideModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    device_type: Optional[str] = Field(default=None, alias="deviceType")


class FilterModel(BaseModel):
    pattern: Optional[str] = Field(default=None, alias="Pattern")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListPipesRequestModel(BaseModel):
    current_state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETING",
            "RUNNING",
            "STARTING",
            "START_FAILED",
            "STOPPED",
            "STOPPING",
            "STOP_FAILED",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="CurrentState")
    desired_state: Optional[Literal["RUNNING", "STOPPED"]] = Field(
        default=None, alias="DesiredState"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    source_prefix: Optional[str] = Field(default=None, alias="SourcePrefix")
    target_prefix: Optional[str] = Field(default=None, alias="TargetPrefix")


class PipeModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    current_state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETING",
            "RUNNING",
            "STARTING",
            "START_FAILED",
            "STOPPED",
            "STOPPING",
            "STOP_FAILED",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="CurrentState")
    desired_state: Optional[Literal["RUNNING", "STOPPED"]] = Field(
        default=None, alias="DesiredState"
    )
    enrichment: Optional[str] = Field(default=None, alias="Enrichment")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    source: Optional[str] = Field(default=None, alias="Source")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    target: Optional[str] = Field(default=None, alias="Target")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MQBrokerAccessCredentialsModel(BaseModel):
    basic_auth: Optional[str] = Field(default=None, alias="BasicAuth")


class MSKAccessCredentialsModel(BaseModel):
    client_certificate_tls_auth: Optional[str] = Field(
        default=None, alias="ClientCertificateTlsAuth"
    )
    sasl_scram512_auth: Optional[str] = Field(default=None, alias="SaslScram512Auth")


class PipeEnrichmentHttpParametersModel(BaseModel):
    header_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="HeaderParameters"
    )
    path_parameter_values: Optional[Sequence[str]] = Field(
        default=None, alias="PathParameterValues"
    )
    query_string_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="QueryStringParameters"
    )


class PipeSourceSqsQueueParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class SelfManagedKafkaAccessConfigurationCredentialsModel(BaseModel):
    basic_auth: Optional[str] = Field(default=None, alias="BasicAuth")
    client_certificate_tls_auth: Optional[str] = Field(
        default=None, alias="ClientCertificateTlsAuth"
    )
    sasl_scram256_auth: Optional[str] = Field(default=None, alias="SaslScram256Auth")
    sasl_scram512_auth: Optional[str] = Field(default=None, alias="SaslScram512Auth")


class SelfManagedKafkaAccessConfigurationVpcModel(BaseModel):
    security_group: Optional[Sequence[str]] = Field(default=None, alias="SecurityGroup")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")


class PipeTargetCloudWatchLogsParametersModel(BaseModel):
    log_stream_name: Optional[str] = Field(default=None, alias="LogStreamName")
    timestamp: Optional[str] = Field(default=None, alias="Timestamp")


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


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PipeTargetEventBridgeEventBusParametersModel(BaseModel):
    detail_type: Optional[str] = Field(default=None, alias="DetailType")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")
    source: Optional[str] = Field(default=None, alias="Source")
    time: Optional[str] = Field(default=None, alias="Time")


class PipeTargetHttpParametersModel(BaseModel):
    header_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="HeaderParameters"
    )
    path_parameter_values: Optional[Sequence[str]] = Field(
        default=None, alias="PathParameterValues"
    )
    query_string_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="QueryStringParameters"
    )


class PipeTargetKinesisStreamParametersModel(BaseModel):
    partition_key: str = Field(alias="PartitionKey")


class PipeTargetLambdaFunctionParametersModel(BaseModel):
    invocation_type: Optional[Literal["FIRE_AND_FORGET", "REQUEST_RESPONSE"]] = Field(
        default=None, alias="InvocationType"
    )


class PipeTargetRedshiftDataParametersModel(BaseModel):
    database: str = Field(alias="Database")
    sqls: Sequence[str] = Field(alias="Sqls")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    secret_manager_arn: Optional[str] = Field(default=None, alias="SecretManagerArn")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    with_event: Optional[bool] = Field(default=None, alias="WithEvent")


class PipeTargetSqsQueueParametersModel(BaseModel):
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class PipeTargetStateMachineParametersModel(BaseModel):
    invocation_type: Optional[Literal["FIRE_AND_FORGET", "REQUEST_RESPONSE"]] = Field(
        default=None, alias="InvocationType"
    )


class SageMakerPipelineParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class StartPipeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StopPipeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdatePipeSourceSqsQueueParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class NetworkConfigurationModel(BaseModel):
    awsvpc_configuration: Optional[AwsVpcConfigurationModel] = Field(
        default=None, alias="awsvpcConfiguration"
    )


class BatchContainerOverridesModel(BaseModel):
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    environment: Optional[Sequence[BatchEnvironmentVariableModel]] = Field(
        default=None, alias="Environment"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    resource_requirements: Optional[Sequence[BatchResourceRequirementModel]] = Field(
        default=None, alias="ResourceRequirements"
    )


class CreatePipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    desired_state: Literal["RUNNING", "STOPPED"] = Field(alias="DesiredState")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    desired_state: Literal["DELETED", "RUNNING", "STOPPED"] = Field(
        alias="DesiredState"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    desired_state: Literal["RUNNING", "STOPPED"] = Field(alias="DesiredState")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopPipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    desired_state: Literal["RUNNING", "STOPPED"] = Field(alias="DesiredState")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    desired_state: Literal["RUNNING", "STOPPED"] = Field(alias="DesiredState")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PipeSourceDynamoDBStreamParametersModel(BaseModel):
    starting_position: Literal["LATEST", "TRIM_HORIZON"] = Field(
        alias="StartingPosition"
    )
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    on_partial_batch_item_failure: Optional[Literal["AUTOMATIC_BISECT"]] = Field(
        default=None, alias="OnPartialBatchItemFailure"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )


class PipeSourceKinesisStreamParametersModel(BaseModel):
    starting_position: Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"] = Field(
        alias="StartingPosition"
    )
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    on_partial_batch_item_failure: Optional[Literal["AUTOMATIC_BISECT"]] = Field(
        default=None, alias="OnPartialBatchItemFailure"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )
    starting_position_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartingPositionTimestamp"
    )


class UpdatePipeSourceDynamoDBStreamParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    on_partial_batch_item_failure: Optional[Literal["AUTOMATIC_BISECT"]] = Field(
        default=None, alias="OnPartialBatchItemFailure"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )


class UpdatePipeSourceKinesisStreamParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    on_partial_batch_item_failure: Optional[Literal["AUTOMATIC_BISECT"]] = Field(
        default=None, alias="OnPartialBatchItemFailure"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )


class EcsContainerOverrideModel(BaseModel):
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    cpu: Optional[int] = Field(default=None, alias="Cpu")
    environment: Optional[Sequence[EcsEnvironmentVariableModel]] = Field(
        default=None, alias="Environment"
    )
    environment_files: Optional[Sequence[EcsEnvironmentFileModel]] = Field(
        default=None, alias="EnvironmentFiles"
    )
    memory: Optional[int] = Field(default=None, alias="Memory")
    memory_reservation: Optional[int] = Field(default=None, alias="MemoryReservation")
    name: Optional[str] = Field(default=None, alias="Name")
    resource_requirements: Optional[Sequence[EcsResourceRequirementModel]] = Field(
        default=None, alias="ResourceRequirements"
    )


class FilterCriteriaModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListPipesRequestListPipesPaginateModel(BaseModel):
    current_state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DELETING",
            "RUNNING",
            "STARTING",
            "START_FAILED",
            "STOPPED",
            "STOPPING",
            "STOP_FAILED",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="CurrentState")
    desired_state: Optional[Literal["RUNNING", "STOPPED"]] = Field(
        default=None, alias="DesiredState"
    )
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    source_prefix: Optional[str] = Field(default=None, alias="SourcePrefix")
    target_prefix: Optional[str] = Field(default=None, alias="TargetPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPipesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    pipes: List[PipeModel] = Field(alias="Pipes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PipeSourceActiveMQBrokerParametersModel(BaseModel):
    credentials: MQBrokerAccessCredentialsModel = Field(alias="Credentials")
    queue_name: str = Field(alias="QueueName")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class PipeSourceRabbitMQBrokerParametersModel(BaseModel):
    credentials: MQBrokerAccessCredentialsModel = Field(alias="Credentials")
    queue_name: str = Field(alias="QueueName")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    virtual_host: Optional[str] = Field(default=None, alias="VirtualHost")


class UpdatePipeSourceActiveMQBrokerParametersModel(BaseModel):
    credentials: MQBrokerAccessCredentialsModel = Field(alias="Credentials")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class UpdatePipeSourceRabbitMQBrokerParametersModel(BaseModel):
    credentials: MQBrokerAccessCredentialsModel = Field(alias="Credentials")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class PipeSourceManagedStreamingKafkaParametersModel(BaseModel):
    topic_name: str = Field(alias="TopicName")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupID")
    credentials: Optional[MSKAccessCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    starting_position: Optional[Literal["LATEST", "TRIM_HORIZON"]] = Field(
        default=None, alias="StartingPosition"
    )


class UpdatePipeSourceManagedStreamingKafkaParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    credentials: Optional[MSKAccessCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )


class PipeEnrichmentParametersModel(BaseModel):
    http_parameters: Optional[PipeEnrichmentHttpParametersModel] = Field(
        default=None, alias="HttpParameters"
    )
    input_template: Optional[str] = Field(default=None, alias="InputTemplate")


class PipeSourceSelfManagedKafkaParametersModel(BaseModel):
    topic_name: str = Field(alias="TopicName")
    additional_bootstrap_servers: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalBootstrapServers"
    )
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupID")
    credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    server_root_ca_certificate: Optional[str] = Field(
        default=None, alias="ServerRootCaCertificate"
    )
    starting_position: Optional[Literal["LATEST", "TRIM_HORIZON"]] = Field(
        default=None, alias="StartingPosition"
    )
    vpc: Optional[SelfManagedKafkaAccessConfigurationVpcModel] = Field(
        default=None, alias="Vpc"
    )


class UpdatePipeSourceSelfManagedKafkaParametersModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    credentials: Optional[SelfManagedKafkaAccessConfigurationCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    server_root_ca_certificate: Optional[str] = Field(
        default=None, alias="ServerRootCaCertificate"
    )
    vpc: Optional[SelfManagedKafkaAccessConfigurationVpcModel] = Field(
        default=None, alias="Vpc"
    )


class PipeTargetSageMakerPipelineParametersModel(BaseModel):
    pipeline_parameter_list: Optional[
        Sequence[SageMakerPipelineParameterModel]
    ] = Field(default=None, alias="PipelineParameterList")


class PipeTargetBatchJobParametersModel(BaseModel):
    job_definition: str = Field(alias="JobDefinition")
    job_name: str = Field(alias="JobName")
    array_properties: Optional[BatchArrayPropertiesModel] = Field(
        default=None, alias="ArrayProperties"
    )
    container_overrides: Optional[BatchContainerOverridesModel] = Field(
        default=None, alias="ContainerOverrides"
    )
    depends_on: Optional[Sequence[BatchJobDependencyModel]] = Field(
        default=None, alias="DependsOn"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    retry_strategy: Optional[BatchRetryStrategyModel] = Field(
        default=None, alias="RetryStrategy"
    )


class EcsTaskOverrideModel(BaseModel):
    container_overrides: Optional[Sequence[EcsContainerOverrideModel]] = Field(
        default=None, alias="ContainerOverrides"
    )
    cpu: Optional[str] = Field(default=None, alias="Cpu")
    ephemeral_storage: Optional[EcsEphemeralStorageModel] = Field(
        default=None, alias="EphemeralStorage"
    )
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    inference_accelerator_overrides: Optional[
        Sequence[EcsInferenceAcceleratorOverrideModel]
    ] = Field(default=None, alias="InferenceAcceleratorOverrides")
    memory: Optional[str] = Field(default=None, alias="Memory")
    task_role_arn: Optional[str] = Field(default=None, alias="TaskRoleArn")


class PipeSourceParametersModel(BaseModel):
    active_mqbroker_parameters: Optional[
        PipeSourceActiveMQBrokerParametersModel
    ] = Field(default=None, alias="ActiveMQBrokerParameters")
    dynamo_dbstream_parameters: Optional[
        PipeSourceDynamoDBStreamParametersModel
    ] = Field(default=None, alias="DynamoDBStreamParameters")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="FilterCriteria"
    )
    kinesis_stream_parameters: Optional[PipeSourceKinesisStreamParametersModel] = Field(
        default=None, alias="KinesisStreamParameters"
    )
    managed_streaming_kafka_parameters: Optional[
        PipeSourceManagedStreamingKafkaParametersModel
    ] = Field(default=None, alias="ManagedStreamingKafkaParameters")
    rabbit_mqbroker_parameters: Optional[
        PipeSourceRabbitMQBrokerParametersModel
    ] = Field(default=None, alias="RabbitMQBrokerParameters")
    self_managed_kafka_parameters: Optional[
        PipeSourceSelfManagedKafkaParametersModel
    ] = Field(default=None, alias="SelfManagedKafkaParameters")
    sqs_queue_parameters: Optional[PipeSourceSqsQueueParametersModel] = Field(
        default=None, alias="SqsQueueParameters"
    )


class UpdatePipeSourceParametersModel(BaseModel):
    active_mqbroker_parameters: Optional[
        UpdatePipeSourceActiveMQBrokerParametersModel
    ] = Field(default=None, alias="ActiveMQBrokerParameters")
    dynamo_dbstream_parameters: Optional[
        UpdatePipeSourceDynamoDBStreamParametersModel
    ] = Field(default=None, alias="DynamoDBStreamParameters")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="FilterCriteria"
    )
    kinesis_stream_parameters: Optional[
        UpdatePipeSourceKinesisStreamParametersModel
    ] = Field(default=None, alias="KinesisStreamParameters")
    managed_streaming_kafka_parameters: Optional[
        UpdatePipeSourceManagedStreamingKafkaParametersModel
    ] = Field(default=None, alias="ManagedStreamingKafkaParameters")
    rabbit_mqbroker_parameters: Optional[
        UpdatePipeSourceRabbitMQBrokerParametersModel
    ] = Field(default=None, alias="RabbitMQBrokerParameters")
    self_managed_kafka_parameters: Optional[
        UpdatePipeSourceSelfManagedKafkaParametersModel
    ] = Field(default=None, alias="SelfManagedKafkaParameters")
    sqs_queue_parameters: Optional[UpdatePipeSourceSqsQueueParametersModel] = Field(
        default=None, alias="SqsQueueParameters"
    )


class PipeTargetEcsTaskParametersModel(BaseModel):
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
    overrides: Optional[EcsTaskOverrideModel] = Field(default=None, alias="Overrides")
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
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    task_count: Optional[int] = Field(default=None, alias="TaskCount")


class PipeTargetParametersModel(BaseModel):
    batch_job_parameters: Optional[PipeTargetBatchJobParametersModel] = Field(
        default=None, alias="BatchJobParameters"
    )
    cloud_watch_logs_parameters: Optional[
        PipeTargetCloudWatchLogsParametersModel
    ] = Field(default=None, alias="CloudWatchLogsParameters")
    ecs_task_parameters: Optional[PipeTargetEcsTaskParametersModel] = Field(
        default=None, alias="EcsTaskParameters"
    )
    event_bridge_event_bus_parameters: Optional[
        PipeTargetEventBridgeEventBusParametersModel
    ] = Field(default=None, alias="EventBridgeEventBusParameters")
    http_parameters: Optional[PipeTargetHttpParametersModel] = Field(
        default=None, alias="HttpParameters"
    )
    input_template: Optional[str] = Field(default=None, alias="InputTemplate")
    kinesis_stream_parameters: Optional[PipeTargetKinesisStreamParametersModel] = Field(
        default=None, alias="KinesisStreamParameters"
    )
    lambda_function_parameters: Optional[
        PipeTargetLambdaFunctionParametersModel
    ] = Field(default=None, alias="LambdaFunctionParameters")
    redshift_data_parameters: Optional[PipeTargetRedshiftDataParametersModel] = Field(
        default=None, alias="RedshiftDataParameters"
    )
    sage_maker_pipeline_parameters: Optional[
        PipeTargetSageMakerPipelineParametersModel
    ] = Field(default=None, alias="SageMakerPipelineParameters")
    sqs_queue_parameters: Optional[PipeTargetSqsQueueParametersModel] = Field(
        default=None, alias="SqsQueueParameters"
    )
    step_function_state_machine_parameters: Optional[
        PipeTargetStateMachineParametersModel
    ] = Field(default=None, alias="StepFunctionStateMachineParameters")


class CreatePipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    source: str = Field(alias="Source")
    target: str = Field(alias="Target")
    description: Optional[str] = Field(default=None, alias="Description")
    desired_state: Optional[Literal["RUNNING", "STOPPED"]] = Field(
        default=None, alias="DesiredState"
    )
    enrichment: Optional[str] = Field(default=None, alias="Enrichment")
    enrichment_parameters: Optional[PipeEnrichmentParametersModel] = Field(
        default=None, alias="EnrichmentParameters"
    )
    source_parameters: Optional[PipeSourceParametersModel] = Field(
        default=None, alias="SourceParameters"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    target_parameters: Optional[PipeTargetParametersModel] = Field(
        default=None, alias="TargetParameters"
    )


class DescribePipeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    current_state: Literal[
        "CREATE_FAILED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "START_FAILED",
        "STOPPED",
        "STOPPING",
        "STOP_FAILED",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="CurrentState")
    description: str = Field(alias="Description")
    desired_state: Literal["DELETED", "RUNNING", "STOPPED"] = Field(
        alias="DesiredState"
    )
    enrichment: str = Field(alias="Enrichment")
    enrichment_parameters: PipeEnrichmentParametersModel = Field(
        alias="EnrichmentParameters"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    source: str = Field(alias="Source")
    source_parameters: PipeSourceParametersModel = Field(alias="SourceParameters")
    state_reason: str = Field(alias="StateReason")
    tags: Dict[str, str] = Field(alias="Tags")
    target: str = Field(alias="Target")
    target_parameters: PipeTargetParametersModel = Field(alias="TargetParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    desired_state: Optional[Literal["RUNNING", "STOPPED"]] = Field(
        default=None, alias="DesiredState"
    )
    enrichment: Optional[str] = Field(default=None, alias="Enrichment")
    enrichment_parameters: Optional[PipeEnrichmentParametersModel] = Field(
        default=None, alias="EnrichmentParameters"
    )
    source_parameters: Optional[UpdatePipeSourceParametersModel] = Field(
        default=None, alias="SourceParameters"
    )
    target: Optional[str] = Field(default=None, alias="Target")
    target_parameters: Optional[PipeTargetParametersModel] = Field(
        default=None, alias="TargetParameters"
    )
