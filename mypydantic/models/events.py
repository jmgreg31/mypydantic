# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActivateEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ApiDestinationModel(BaseModel):
    api_destination_arn: Optional[str] = Field(default=None, alias="ApiDestinationArn")
    name: Optional[str] = Field(default=None, alias="Name")
    api_destination_state: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="ApiDestinationState"
    )
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    invocation_endpoint: Optional[str] = Field(default=None, alias="InvocationEndpoint")
    http_method: Optional[
        Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(default=None, alias="HttpMethod")
    invocation_rate_limit_per_second: Optional[int] = Field(
        default=None, alias="InvocationRateLimitPerSecond"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ArchiveModel(BaseModel):
    archive_name: Optional[str] = Field(default=None, alias="ArchiveName")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DISABLED",
            "ENABLED",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")
    size_bytes: Optional[int] = Field(default=None, alias="SizeBytes")
    event_count: Optional[int] = Field(default=None, alias="EventCount")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class AwsVpcConfigurationModel(BaseModel):
    subnets: List[str] = Field(alias="Subnets")
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    assign_public_ip: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AssignPublicIp"
    )


class BatchArrayPropertiesModel(BaseModel):
    size: Optional[int] = Field(default=None, alias="Size")


class BatchRetryStrategyModel(BaseModel):
    attempts: Optional[int] = Field(default=None, alias="Attempts")


class CancelReplayRequestModel(BaseModel):
    replay_name: str = Field(alias="ReplayName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CapacityProviderStrategyItemModel(BaseModel):
    capacity_provider: str = Field(alias="capacityProvider")
    weight: Optional[int] = Field(default=None, alias="weight")
    base: Optional[int] = Field(default=None, alias="base")


class ConditionModel(BaseModel):
    type: str = Field(alias="Type")
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ConnectionApiKeyAuthResponseParametersModel(BaseModel):
    api_key_name: Optional[str] = Field(default=None, alias="ApiKeyName")


class ConnectionBasicAuthResponseParametersModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")


class ConnectionBodyParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    is_value_secret: Optional[bool] = Field(default=None, alias="IsValueSecret")


class ConnectionHeaderParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    is_value_secret: Optional[bool] = Field(default=None, alias="IsValueSecret")


class ConnectionQueryStringParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    is_value_secret: Optional[bool] = Field(default=None, alias="IsValueSecret")


class ConnectionOAuthClientResponseParametersModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientID")


class ConnectionModel(BaseModel):
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    name: Optional[str] = Field(default=None, alias="Name")
    connection_state: Optional[
        Literal[
            "AUTHORIZED",
            "AUTHORIZING",
            "CREATING",
            "DEAUTHORIZED",
            "DEAUTHORIZING",
            "DELETING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ConnectionState")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    authorization_type: Optional[
        Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"]
    ] = Field(default=None, alias="AuthorizationType")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    last_authorized_time: Optional[datetime] = Field(
        default=None, alias="LastAuthorizedTime"
    )


class CreateApiDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    connection_arn: str = Field(alias="ConnectionArn")
    invocation_endpoint: str = Field(alias="InvocationEndpoint")
    http_method: Literal[
        "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
    ] = Field(alias="HttpMethod")
    description: Optional[str] = Field(default=None, alias="Description")
    invocation_rate_limit_per_second: Optional[int] = Field(
        default=None, alias="InvocationRateLimitPerSecond"
    )


class CreateArchiveRequestModel(BaseModel):
    archive_name: str = Field(alias="ArchiveName")
    event_source_arn: str = Field(alias="EventSourceArn")
    description: Optional[str] = Field(default=None, alias="Description")
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class CreateConnectionApiKeyAuthRequestParametersModel(BaseModel):
    api_key_name: str = Field(alias="ApiKeyName")
    api_key_value: str = Field(alias="ApiKeyValue")


class CreateConnectionBasicAuthRequestParametersModel(BaseModel):
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")


class CreateConnectionOAuthClientRequestParametersModel(BaseModel):
    client_id: str = Field(alias="ClientID")
    client_secret: str = Field(alias="ClientSecret")


class EndpointEventBusModel(BaseModel):
    event_bus_arn: str = Field(alias="EventBusArn")


class ReplicationConfigModel(BaseModel):
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreatePartnerEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    account: str = Field(alias="Account")


class DeactivateEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeadLetterConfigModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class DeauthorizeConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteApiDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteArchiveRequestModel(BaseModel):
    archive_name: str = Field(alias="ArchiveName")


class DeleteConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteEndpointRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteEventBusRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeletePartnerEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    account: str = Field(alias="Account")


class DeleteRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    force: Optional[bool] = Field(default=None, alias="Force")


class DescribeApiDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeArchiveRequestModel(BaseModel):
    archive_name: str = Field(alias="ArchiveName")


class DescribeConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeEndpointRequestModel(BaseModel):
    name: str = Field(alias="Name")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")


class DescribeEventBusRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class DescribeEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribePartnerEventSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeReplayRequestModel(BaseModel):
    replay_name: str = Field(alias="ReplayName")


class ReplayDestinationModel(BaseModel):
    arn: str = Field(alias="Arn")
    filter_arns: Optional[List[str]] = Field(default=None, alias="FilterArns")


class DescribeRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class DisableRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class PlacementConstraintModel(BaseModel):
    type: Optional[Literal["distinctInstance", "memberOf"]] = Field(
        default=None, alias="type"
    )
    expression: Optional[str] = Field(default=None, alias="expression")


class PlacementStrategyModel(BaseModel):
    type: Optional[Literal["binpack", "random", "spread"]] = Field(
        default=None, alias="type"
    )
    field: Optional[str] = Field(default=None, alias="field")


class EnableRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class EventBusModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    policy: Optional[str] = Field(default=None, alias="Policy")


class EventSourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "DELETED", "PENDING"]] = Field(
        default=None, alias="State"
    )


class PrimaryModel(BaseModel):
    health_check: str = Field(alias="HealthCheck")


class SecondaryModel(BaseModel):
    route: str = Field(alias="Route")


class HttpParametersModel(BaseModel):
    path_parameter_values: Optional[List[str]] = Field(
        default=None, alias="PathParameterValues"
    )
    header_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="HeaderParameters"
    )
    query_string_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="QueryStringParameters"
    )


class InputTransformerModel(BaseModel):
    input_template: str = Field(alias="InputTemplate")
    input_paths_map: Optional[Dict[str, str]] = Field(
        default=None, alias="InputPathsMap"
    )


class KinesisParametersModel(BaseModel):
    partition_key_path: str = Field(alias="PartitionKeyPath")


class ListApiDestinationsRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListArchivesRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATING",
            "DISABLED",
            "ENABLED",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListConnectionsRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    connection_state: Optional[
        Literal[
            "AUTHORIZED",
            "AUTHORIZING",
            "CREATING",
            "DEAUTHORIZED",
            "DEAUTHORIZING",
            "DELETING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ConnectionState")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListEndpointsRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEventBusesRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListEventSourcesRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListPartnerEventSourceAccountsRequestModel(BaseModel):
    event_source_name: str = Field(alias="EventSourceName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PartnerEventSourceAccountModel(BaseModel):
    account: Optional[str] = Field(default=None, alias="Account")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")
    state: Optional[Literal["ACTIVE", "DELETED", "PENDING"]] = Field(
        default=None, alias="State"
    )


class ListPartnerEventSourcesRequestModel(BaseModel):
    name_prefix: str = Field(alias="NamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PartnerEventSourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListReplaysRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    state: Optional[
        Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"]
    ] = Field(default=None, alias="State")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ReplayModel(BaseModel):
    replay_name: Optional[str] = Field(default=None, alias="ReplayName")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    state: Optional[
        Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    event_start_time: Optional[datetime] = Field(default=None, alias="EventStartTime")
    event_end_time: Optional[datetime] = Field(default=None, alias="EventEndTime")
    event_last_replayed_time: Optional[datetime] = Field(
        default=None, alias="EventLastReplayedTime"
    )
    replay_start_time: Optional[datetime] = Field(default=None, alias="ReplayStartTime")
    replay_end_time: Optional[datetime] = Field(default=None, alias="ReplayEndTime")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRuleNamesByTargetRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListRulesRequestModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class RuleModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    managed_by: Optional[str] = Field(default=None, alias="ManagedBy")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class ListTargetsByRuleRequestModel(BaseModel):
    rule: str = Field(alias="Rule")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PutEventsRequestEntryModel(BaseModel):
    time: Optional[Union[datetime, str]] = Field(default=None, alias="Time")
    source: Optional[str] = Field(default=None, alias="Source")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")
    detail_type: Optional[str] = Field(default=None, alias="DetailType")
    detail: Optional[str] = Field(default=None, alias="Detail")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    trace_header: Optional[str] = Field(default=None, alias="TraceHeader")


class PutEventsResultEntryModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class PutPartnerEventsRequestEntryModel(BaseModel):
    time: Optional[Union[datetime, str]] = Field(default=None, alias="Time")
    source: Optional[str] = Field(default=None, alias="Source")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")
    detail_type: Optional[str] = Field(default=None, alias="DetailType")
    detail: Optional[str] = Field(default=None, alias="Detail")


class PutPartnerEventsResultEntryModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class PutTargetsResultEntryModel(BaseModel):
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class RedshiftDataParametersModel(BaseModel):
    database: str = Field(alias="Database")
    sql: str = Field(alias="Sql")
    secret_manager_arn: Optional[str] = Field(default=None, alias="SecretManagerArn")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    with_event: Optional[bool] = Field(default=None, alias="WithEvent")


class RemovePermissionRequestModel(BaseModel):
    statement_id: Optional[str] = Field(default=None, alias="StatementId")
    remove_all_permissions: Optional[bool] = Field(
        default=None, alias="RemoveAllPermissions"
    )
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class RemoveTargetsRequestModel(BaseModel):
    rule: str = Field(alias="Rule")
    ids: Sequence[str] = Field(alias="Ids")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    force: Optional[bool] = Field(default=None, alias="Force")


class RemoveTargetsResultEntryModel(BaseModel):
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class RetryPolicyModel(BaseModel):
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )


class RunCommandTargetModel(BaseModel):
    key: str = Field(alias="Key")
    values: List[str] = Field(alias="Values")


class SageMakerPipelineParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class SqsParametersModel(BaseModel):
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class TestEventPatternRequestModel(BaseModel):
    event_pattern: str = Field(alias="EventPattern")
    event: str = Field(alias="Event")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateApiDestinationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    invocation_endpoint: Optional[str] = Field(default=None, alias="InvocationEndpoint")
    http_method: Optional[
        Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(default=None, alias="HttpMethod")
    invocation_rate_limit_per_second: Optional[int] = Field(
        default=None, alias="InvocationRateLimitPerSecond"
    )


class UpdateArchiveRequestModel(BaseModel):
    archive_name: str = Field(alias="ArchiveName")
    description: Optional[str] = Field(default=None, alias="Description")
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class UpdateConnectionApiKeyAuthRequestParametersModel(BaseModel):
    api_key_name: Optional[str] = Field(default=None, alias="ApiKeyName")
    api_key_value: Optional[str] = Field(default=None, alias="ApiKeyValue")


class UpdateConnectionBasicAuthRequestParametersModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")


class UpdateConnectionOAuthClientRequestParametersModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientID")
    client_secret: Optional[str] = Field(default=None, alias="ClientSecret")


class NetworkConfigurationModel(BaseModel):
    awsvpc_configuration: Optional[AwsVpcConfigurationModel] = Field(
        default=None, alias="awsvpcConfiguration"
    )


class BatchParametersModel(BaseModel):
    job_definition: str = Field(alias="JobDefinition")
    job_name: str = Field(alias="JobName")
    array_properties: Optional[BatchArrayPropertiesModel] = Field(
        default=None, alias="ArrayProperties"
    )
    retry_strategy: Optional[BatchRetryStrategyModel] = Field(
        default=None, alias="RetryStrategy"
    )


class CancelReplayResponseModel(BaseModel):
    replay_arn: str = Field(alias="ReplayArn")
    state: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApiDestinationResponseModel(BaseModel):
    api_destination_arn: str = Field(alias="ApiDestinationArn")
    api_destination_state: Literal["ACTIVE", "INACTIVE"] = Field(
        alias="ApiDestinationState"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateArchiveResponseModel(BaseModel):
    archive_arn: str = Field(alias="ArchiveArn")
    state: Literal[
        "CREATE_FAILED", "CREATING", "DISABLED", "ENABLED", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectionResponseModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    connection_state: Literal[
        "AUTHORIZED",
        "AUTHORIZING",
        "CREATING",
        "DEAUTHORIZED",
        "DEAUTHORIZING",
        "DELETING",
        "UPDATING",
    ] = Field(alias="ConnectionState")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventBusResponseModel(BaseModel):
    event_bus_arn: str = Field(alias="EventBusArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePartnerEventSourceResponseModel(BaseModel):
    event_source_arn: str = Field(alias="EventSourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeauthorizeConnectionResponseModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    connection_state: Literal[
        "AUTHORIZED",
        "AUTHORIZING",
        "CREATING",
        "DEAUTHORIZED",
        "DEAUTHORIZING",
        "DELETING",
        "UPDATING",
    ] = Field(alias="ConnectionState")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_authorized_time: datetime = Field(alias="LastAuthorizedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConnectionResponseModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    connection_state: Literal[
        "AUTHORIZED",
        "AUTHORIZING",
        "CREATING",
        "DEAUTHORIZED",
        "DEAUTHORIZING",
        "DELETING",
        "UPDATING",
    ] = Field(alias="ConnectionState")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_authorized_time: datetime = Field(alias="LastAuthorizedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApiDestinationResponseModel(BaseModel):
    api_destination_arn: str = Field(alias="ApiDestinationArn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    api_destination_state: Literal["ACTIVE", "INACTIVE"] = Field(
        alias="ApiDestinationState"
    )
    connection_arn: str = Field(alias="ConnectionArn")
    invocation_endpoint: str = Field(alias="InvocationEndpoint")
    http_method: Literal[
        "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
    ] = Field(alias="HttpMethod")
    invocation_rate_limit_per_second: int = Field(alias="InvocationRateLimitPerSecond")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeArchiveResponseModel(BaseModel):
    archive_arn: str = Field(alias="ArchiveArn")
    archive_name: str = Field(alias="ArchiveName")
    event_source_arn: str = Field(alias="EventSourceArn")
    description: str = Field(alias="Description")
    event_pattern: str = Field(alias="EventPattern")
    state: Literal[
        "CREATE_FAILED", "CREATING", "DISABLED", "ENABLED", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    retention_days: int = Field(alias="RetentionDays")
    size_bytes: int = Field(alias="SizeBytes")
    event_count: int = Field(alias="EventCount")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventBusResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_by: str = Field(alias="CreatedBy")
    creation_time: datetime = Field(alias="CreationTime")
    expiration_time: datetime = Field(alias="ExpirationTime")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "DELETED", "PENDING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePartnerEventSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRuleResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    event_pattern: str = Field(alias="EventPattern")
    schedule_expression: str = Field(alias="ScheduleExpression")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    description: str = Field(alias="Description")
    role_arn: str = Field(alias="RoleArn")
    managed_by: str = Field(alias="ManagedBy")
    event_bus_name: str = Field(alias="EventBusName")
    created_by: str = Field(alias="CreatedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApiDestinationsResponseModel(BaseModel):
    api_destinations: List[ApiDestinationModel] = Field(alias="ApiDestinations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListArchivesResponseModel(BaseModel):
    archives: List[ArchiveModel] = Field(alias="Archives")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRuleNamesByTargetResponseModel(BaseModel):
    rule_names: List[str] = Field(alias="RuleNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRuleResponseModel(BaseModel):
    rule_arn: str = Field(alias="RuleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplayResponseModel(BaseModel):
    replay_arn: str = Field(alias="ReplayArn")
    state: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    replay_start_time: datetime = Field(alias="ReplayStartTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestEventPatternResponseModel(BaseModel):
    result: bool = Field(alias="Result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApiDestinationResponseModel(BaseModel):
    api_destination_arn: str = Field(alias="ApiDestinationArn")
    api_destination_state: Literal["ACTIVE", "INACTIVE"] = Field(
        alias="ApiDestinationState"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateArchiveResponseModel(BaseModel):
    archive_arn: str = Field(alias="ArchiveArn")
    state: Literal[
        "CREATE_FAILED", "CREATING", "DISABLED", "ENABLED", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectionResponseModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    connection_state: Literal[
        "AUTHORIZED",
        "AUTHORIZING",
        "CREATING",
        "DEAUTHORIZED",
        "DEAUTHORIZING",
        "DELETING",
        "UPDATING",
    ] = Field(alias="ConnectionState")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_authorized_time: datetime = Field(alias="LastAuthorizedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPermissionRequestModel(BaseModel):
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    action: Optional[str] = Field(default=None, alias="Action")
    principal: Optional[str] = Field(default=None, alias="Principal")
    statement_id: Optional[str] = Field(default=None, alias="StatementId")
    condition: Optional[ConditionModel] = Field(default=None, alias="Condition")
    policy: Optional[str] = Field(default=None, alias="Policy")


class ConnectionHttpParametersModel(BaseModel):
    header_parameters: Optional[Sequence[ConnectionHeaderParameterModel]] = Field(
        default=None, alias="HeaderParameters"
    )
    query_string_parameters: Optional[
        Sequence[ConnectionQueryStringParameterModel]
    ] = Field(default=None, alias="QueryStringParameters")
    body_parameters: Optional[Sequence[ConnectionBodyParameterModel]] = Field(
        default=None, alias="BodyParameters"
    )


class ListConnectionsResponseModel(BaseModel):
    connections: List[ConnectionModel] = Field(alias="Connections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventBusRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_source_name: Optional[str] = Field(default=None, alias="EventSourceName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DescribeReplayResponseModel(BaseModel):
    replay_name: str = Field(alias="ReplayName")
    replay_arn: str = Field(alias="ReplayArn")
    description: str = Field(alias="Description")
    state: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "RUNNING", "STARTING"
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    event_source_arn: str = Field(alias="EventSourceArn")
    destination: ReplayDestinationModel = Field(alias="Destination")
    event_start_time: datetime = Field(alias="EventStartTime")
    event_end_time: datetime = Field(alias="EventEndTime")
    event_last_replayed_time: datetime = Field(alias="EventLastReplayedTime")
    replay_start_time: datetime = Field(alias="ReplayStartTime")
    replay_end_time: datetime = Field(alias="ReplayEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplayRequestModel(BaseModel):
    replay_name: str = Field(alias="ReplayName")
    event_source_arn: str = Field(alias="EventSourceArn")
    event_start_time: Union[datetime, str] = Field(alias="EventStartTime")
    event_end_time: Union[datetime, str] = Field(alias="EventEndTime")
    destination: ReplayDestinationModel = Field(alias="Destination")
    description: Optional[str] = Field(default=None, alias="Description")


class ListEventBusesResponseModel(BaseModel):
    event_buses: List[EventBusModel] = Field(alias="EventBuses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventSourcesResponseModel(BaseModel):
    event_sources: List[EventSourceModel] = Field(alias="EventSources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailoverConfigModel(BaseModel):
    primary: PrimaryModel = Field(alias="Primary")
    secondary: SecondaryModel = Field(alias="Secondary")


class ListPartnerEventSourceAccountsResponseModel(BaseModel):
    partner_event_source_accounts: List[PartnerEventSourceAccountModel] = Field(
        alias="PartnerEventSourceAccounts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPartnerEventSourcesResponseModel(BaseModel):
    partner_event_sources: List[PartnerEventSourceModel] = Field(
        alias="PartnerEventSources"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReplaysResponseModel(BaseModel):
    replays: List[ReplayModel] = Field(alias="Replays")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesRequestListRulesPaginateModel(BaseModel):
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTargetsByRuleRequestListTargetsByRulePaginateModel(BaseModel):
    rule: str = Field(alias="Rule")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesResponseModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutEventsRequestModel(BaseModel):
    entries: Sequence[PutEventsRequestEntryModel] = Field(alias="Entries")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")


class PutEventsResponseModel(BaseModel):
    failed_entry_count: int = Field(alias="FailedEntryCount")
    entries: List[PutEventsResultEntryModel] = Field(alias="Entries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPartnerEventsRequestModel(BaseModel):
    entries: Sequence[PutPartnerEventsRequestEntryModel] = Field(alias="Entries")


class PutPartnerEventsResponseModel(BaseModel):
    failed_entry_count: int = Field(alias="FailedEntryCount")
    entries: List[PutPartnerEventsResultEntryModel] = Field(alias="Entries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutTargetsResponseModel(BaseModel):
    failed_entry_count: int = Field(alias="FailedEntryCount")
    failed_entries: List[PutTargetsResultEntryModel] = Field(alias="FailedEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveTargetsResponseModel(BaseModel):
    failed_entry_count: int = Field(alias="FailedEntryCount")
    failed_entries: List[RemoveTargetsResultEntryModel] = Field(alias="FailedEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunCommandParametersModel(BaseModel):
    run_command_targets: List[RunCommandTargetModel] = Field(alias="RunCommandTargets")


class SageMakerPipelineParametersModel(BaseModel):
    pipeline_parameter_list: Optional[List[SageMakerPipelineParameterModel]] = Field(
        default=None, alias="PipelineParameterList"
    )


class EcsParametersModel(BaseModel):
    task_definition_arn: str = Field(alias="TaskDefinitionArn")
    task_count: Optional[int] = Field(default=None, alias="TaskCount")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="LaunchType"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    group: Optional[str] = Field(default=None, alias="Group")
    capacity_provider_strategy: Optional[
        List[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="CapacityProviderStrategy")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="EnableECSManagedTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="EnableExecuteCommand"
    )
    placement_constraints: Optional[List[PlacementConstraintModel]] = Field(
        default=None, alias="PlacementConstraints"
    )
    placement_strategy: Optional[List[PlacementStrategyModel]] = Field(
        default=None, alias="PlacementStrategy"
    )
    propagate_tags: Optional[Literal["TASK_DEFINITION"]] = Field(
        default=None, alias="PropagateTags"
    )
    reference_id: Optional[str] = Field(default=None, alias="ReferenceId")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ConnectionOAuthResponseParametersModel(BaseModel):
    client_parameters: Optional[ConnectionOAuthClientResponseParametersModel] = Field(
        default=None, alias="ClientParameters"
    )
    authorization_endpoint: Optional[str] = Field(
        default=None, alias="AuthorizationEndpoint"
    )
    http_method: Optional[Literal["GET", "POST", "PUT"]] = Field(
        default=None, alias="HttpMethod"
    )
    oauth_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="OAuthHttpParameters"
    )


class CreateConnectionOAuthRequestParametersModel(BaseModel):
    client_parameters: CreateConnectionOAuthClientRequestParametersModel = Field(
        alias="ClientParameters"
    )
    authorization_endpoint: str = Field(alias="AuthorizationEndpoint")
    http_method: Literal["GET", "POST", "PUT"] = Field(alias="HttpMethod")
    oauth_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="OAuthHttpParameters"
    )


class UpdateConnectionOAuthRequestParametersModel(BaseModel):
    client_parameters: Optional[
        UpdateConnectionOAuthClientRequestParametersModel
    ] = Field(default=None, alias="ClientParameters")
    authorization_endpoint: Optional[str] = Field(
        default=None, alias="AuthorizationEndpoint"
    )
    http_method: Optional[Literal["GET", "POST", "PUT"]] = Field(
        default=None, alias="HttpMethod"
    )
    oauth_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="OAuthHttpParameters"
    )


class RoutingConfigModel(BaseModel):
    failover_config: FailoverConfigModel = Field(alias="FailoverConfig")


class TargetModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    input: Optional[str] = Field(default=None, alias="Input")
    input_path: Optional[str] = Field(default=None, alias="InputPath")
    input_transformer: Optional[InputTransformerModel] = Field(
        default=None, alias="InputTransformer"
    )
    kinesis_parameters: Optional[KinesisParametersModel] = Field(
        default=None, alias="KinesisParameters"
    )
    run_command_parameters: Optional[RunCommandParametersModel] = Field(
        default=None, alias="RunCommandParameters"
    )
    ecs_parameters: Optional[EcsParametersModel] = Field(
        default=None, alias="EcsParameters"
    )
    batch_parameters: Optional[BatchParametersModel] = Field(
        default=None, alias="BatchParameters"
    )
    sqs_parameters: Optional[SqsParametersModel] = Field(
        default=None, alias="SqsParameters"
    )
    http_parameters: Optional[HttpParametersModel] = Field(
        default=None, alias="HttpParameters"
    )
    redshift_data_parameters: Optional[RedshiftDataParametersModel] = Field(
        default=None, alias="RedshiftDataParameters"
    )
    sage_maker_pipeline_parameters: Optional[SageMakerPipelineParametersModel] = Field(
        default=None, alias="SageMakerPipelineParameters"
    )
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    retry_policy: Optional[RetryPolicyModel] = Field(default=None, alias="RetryPolicy")


class ConnectionAuthResponseParametersModel(BaseModel):
    basic_auth_parameters: Optional[ConnectionBasicAuthResponseParametersModel] = Field(
        default=None, alias="BasicAuthParameters"
    )
    oauth_parameters: Optional[ConnectionOAuthResponseParametersModel] = Field(
        default=None, alias="OAuthParameters"
    )
    api_key_auth_parameters: Optional[
        ConnectionApiKeyAuthResponseParametersModel
    ] = Field(default=None, alias="ApiKeyAuthParameters")
    invocation_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="InvocationHttpParameters"
    )


class CreateConnectionAuthRequestParametersModel(BaseModel):
    basic_auth_parameters: Optional[
        CreateConnectionBasicAuthRequestParametersModel
    ] = Field(default=None, alias="BasicAuthParameters")
    oauth_parameters: Optional[CreateConnectionOAuthRequestParametersModel] = Field(
        default=None, alias="OAuthParameters"
    )
    api_key_auth_parameters: Optional[
        CreateConnectionApiKeyAuthRequestParametersModel
    ] = Field(default=None, alias="ApiKeyAuthParameters")
    invocation_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="InvocationHttpParameters"
    )


class UpdateConnectionAuthRequestParametersModel(BaseModel):
    basic_auth_parameters: Optional[
        UpdateConnectionBasicAuthRequestParametersModel
    ] = Field(default=None, alias="BasicAuthParameters")
    oauth_parameters: Optional[UpdateConnectionOAuthRequestParametersModel] = Field(
        default=None, alias="OAuthParameters"
    )
    api_key_auth_parameters: Optional[
        UpdateConnectionApiKeyAuthRequestParametersModel
    ] = Field(default=None, alias="ApiKeyAuthParameters")
    invocation_http_parameters: Optional[ConnectionHttpParametersModel] = Field(
        default=None, alias="InvocationHttpParameters"
    )


class CreateEndpointRequestModel(BaseModel):
    name: str = Field(alias="Name")
    routing_config: RoutingConfigModel = Field(alias="RoutingConfig")
    event_buses: Sequence[EndpointEventBusModel] = Field(alias="EventBuses")
    description: Optional[str] = Field(default=None, alias="Description")
    replication_config: Optional[ReplicationConfigModel] = Field(
        default=None, alias="ReplicationConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class CreateEndpointResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    routing_config: RoutingConfigModel = Field(alias="RoutingConfig")
    replication_config: ReplicationConfigModel = Field(alias="ReplicationConfig")
    event_buses: List[EndpointEventBusModel] = Field(alias="EventBuses")
    role_arn: str = Field(alias="RoleArn")
    state: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    arn: str = Field(alias="Arn")
    routing_config: RoutingConfigModel = Field(alias="RoutingConfig")
    replication_config: ReplicationConfigModel = Field(alias="ReplicationConfig")
    event_buses: List[EndpointEventBusModel] = Field(alias="EventBuses")
    role_arn: str = Field(alias="RoleArn")
    endpoint_id: str = Field(alias="EndpointId")
    endpoint_url: str = Field(alias="EndpointUrl")
    state: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    arn: Optional[str] = Field(default=None, alias="Arn")
    routing_config: Optional[RoutingConfigModel] = Field(
        default=None, alias="RoutingConfig"
    )
    replication_config: Optional[ReplicationConfigModel] = Field(
        default=None, alias="ReplicationConfig"
    )
    event_buses: Optional[List[EndpointEventBusModel]] = Field(
        default=None, alias="EventBuses"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    endpoint_url: Optional[str] = Field(default=None, alias="EndpointUrl")
    state: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DELETE_FAILED",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class UpdateEndpointRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[RoutingConfigModel] = Field(
        default=None, alias="RoutingConfig"
    )
    replication_config: Optional[ReplicationConfigModel] = Field(
        default=None, alias="ReplicationConfig"
    )
    event_buses: Optional[Sequence[EndpointEventBusModel]] = Field(
        default=None, alias="EventBuses"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class UpdateEndpointResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    routing_config: RoutingConfigModel = Field(alias="RoutingConfig")
    replication_config: ReplicationConfigModel = Field(alias="ReplicationConfig")
    event_buses: List[EndpointEventBusModel] = Field(alias="EventBuses")
    role_arn: str = Field(alias="RoleArn")
    endpoint_id: str = Field(alias="EndpointId")
    endpoint_url: str = Field(alias="EndpointUrl")
    state: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "UPDATE_FAILED",
        "UPDATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetsByRuleResponseModel(BaseModel):
    targets: List[TargetModel] = Field(alias="Targets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutTargetsRequestModel(BaseModel):
    rule: str = Field(alias="Rule")
    targets: Sequence[TargetModel] = Field(alias="Targets")
    event_bus_name: Optional[str] = Field(default=None, alias="EventBusName")


class DescribeConnectionResponseModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    connection_state: Literal[
        "AUTHORIZED",
        "AUTHORIZING",
        "CREATING",
        "DEAUTHORIZED",
        "DEAUTHORIZING",
        "DELETING",
        "UPDATING",
    ] = Field(alias="ConnectionState")
    state_reason: str = Field(alias="StateReason")
    authorization_type: Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"] = Field(
        alias="AuthorizationType"
    )
    secret_arn: str = Field(alias="SecretArn")
    auth_parameters: ConnectionAuthResponseParametersModel = Field(
        alias="AuthParameters"
    )
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    last_authorized_time: datetime = Field(alias="LastAuthorizedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    authorization_type: Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"] = Field(
        alias="AuthorizationType"
    )
    auth_parameters: CreateConnectionAuthRequestParametersModel = Field(
        alias="AuthParameters"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    authorization_type: Optional[
        Literal["API_KEY", "BASIC", "OAUTH_CLIENT_CREDENTIALS"]
    ] = Field(default=None, alias="AuthorizationType")
    auth_parameters: Optional[UpdateConnectionAuthRequestParametersModel] = Field(
        default=None, alias="AuthParameters"
    )


class ListEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
