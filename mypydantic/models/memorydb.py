# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ACLPendingChangesModel(BaseModel):
    user_names_to_remove: Optional[List[str]] = Field(
        default=None, alias="UserNamesToRemove"
    )
    user_names_to_add: Optional[List[str]] = Field(default=None, alias="UserNamesToAdd")


class ACLsUpdateStatusModel(BaseModel):
    acl_to_apply: Optional[str] = Field(default=None, alias="ACLToApply")


class AuthenticationModeModel(BaseModel):
    type: Optional[Literal["password"]] = Field(default=None, alias="Type")
    passwords: Optional[Sequence[str]] = Field(default=None, alias="Passwords")


class AuthenticationModel(BaseModel):
    type: Optional[Literal["no-password", "password"]] = Field(
        default=None, alias="Type"
    )
    password_count: Optional[int] = Field(default=None, alias="PasswordCount")


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class ServiceUpdateRequestModel(BaseModel):
    service_update_name_to_apply: Optional[str] = Field(
        default=None, alias="ServiceUpdateNameToApply"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UnprocessedClusterModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    error_type: Optional[str] = Field(default=None, alias="ErrorType")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class PendingModifiedServiceUpdateModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    status: Optional[
        Literal["available", "complete", "in-progress", "scheduled"]
    ] = Field(default=None, alias="Status")


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")


class SecurityGroupMembershipModel(BaseModel):
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")
    status: Optional[str] = Field(default=None, alias="Status")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ParameterGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    family: Optional[str] = Field(default=None, alias="Family")
    description: Optional[str] = Field(default=None, alias="Description")
    arn: Optional[str] = Field(default=None, alias="ARN")


class DeleteACLRequestModel(BaseModel):
    acl_name: str = Field(alias="ACLName")


class DeleteClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    final_snapshot_name: Optional[str] = Field(default=None, alias="FinalSnapshotName")


class DeleteParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")


class DeleteSnapshotRequestModel(BaseModel):
    snapshot_name: str = Field(alias="SnapshotName")


class DeleteSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")


class DeleteUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeACLsRequestModel(BaseModel):
    acl_name: Optional[str] = Field(default=None, alias="ACLName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeClustersRequestModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    show_shard_details: Optional[bool] = Field(default=None, alias="ShowShardDetails")


class DescribeEngineVersionsRequestModel(BaseModel):
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    parameter_group_family: Optional[str] = Field(
        default=None, alias="ParameterGroupFamily"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")


class EngineVersionInfoModel(BaseModel):
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    engine_patch_version: Optional[str] = Field(
        default=None, alias="EnginePatchVersion"
    )
    parameter_group_family: Optional[str] = Field(
        default=None, alias="ParameterGroupFamily"
    )


class DescribeEventsRequestModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["acl", "cluster", "node", "parameter-group", "subnet-group", "user"]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EventModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["acl", "cluster", "node", "parameter-group", "subnet-group", "user"]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    date: Optional[datetime] = Field(default=None, alias="Date")


class DescribeParameterGroupsRequestModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeParametersRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ParameterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")
    description: Optional[str] = Field(default=None, alias="Description")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )


class DescribeReservedNodesOfferingsRequestModel(BaseModel):
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeReservedNodesRequestModel(BaseModel):
    reservation_id: Optional[str] = Field(default=None, alias="ReservationId")
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeServiceUpdatesRequestModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    cluster_names: Optional[Sequence[str]] = Field(default=None, alias="ClusterNames")
    status: Optional[
        Sequence[Literal["available", "complete", "in-progress", "scheduled"]]
    ] = Field(default=None, alias="Status")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ServiceUpdateModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    release_date: Optional[datetime] = Field(default=None, alias="ReleaseDate")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal["available", "complete", "in-progress", "scheduled"]
    ] = Field(default=None, alias="Status")
    type: Optional[Literal["security-update"]] = Field(default=None, alias="Type")
    nodes_updated: Optional[str] = Field(default=None, alias="NodesUpdated")
    auto_update_start_date: Optional[datetime] = Field(
        default=None, alias="AutoUpdateStartDate"
    )


class DescribeSnapshotsRequestModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    source: Optional[str] = Field(default=None, alias="Source")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    show_detail: Optional[bool] = Field(default=None, alias="ShowDetail")


class DescribeSubnetGroupsRequestModel(BaseModel):
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class FailoverShardRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    shard_name: str = Field(alias="ShardName")


class ListAllowedNodeTypeUpdatesRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")


class ListTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ParameterNameValueModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class ReplicaConfigurationRequestModel(BaseModel):
    replica_count: Optional[int] = Field(default=None, alias="ReplicaCount")


class ResetParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    all_parameters: Optional[bool] = Field(default=None, alias="AllParameters")
    parameter_names: Optional[Sequence[str]] = Field(
        default=None, alias="ParameterNames"
    )


class SlotMigrationModel(BaseModel):
    progress_percentage: Optional[float] = Field(
        default=None, alias="ProgressPercentage"
    )


class ShardConfigurationRequestModel(BaseModel):
    shard_count: Optional[int] = Field(default=None, alias="ShardCount")


class ShardConfigurationModel(BaseModel):
    slots: Optional[str] = Field(default=None, alias="Slots")
    replica_count: Optional[int] = Field(default=None, alias="ReplicaCount")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateACLRequestModel(BaseModel):
    acl_name: str = Field(alias="ACLName")
    user_names_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="UserNamesToAdd"
    )
    user_names_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="UserNamesToRemove"
    )


class UpdateSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class ACLModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    user_names: Optional[List[str]] = Field(default=None, alias="UserNames")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    pending_changes: Optional[ACLPendingChangesModel] = Field(
        default=None, alias="PendingChanges"
    )
    clusters: Optional[List[str]] = Field(default=None, alias="Clusters")
    arn: Optional[str] = Field(default=None, alias="ARN")


class UpdateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_mode: Optional[AuthenticationModeModel] = Field(
        default=None, alias="AuthenticationMode"
    )
    access_string: Optional[str] = Field(default=None, alias="AccessString")


class UserModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    access_string: Optional[str] = Field(default=None, alias="AccessString")
    acl_names: Optional[List[str]] = Field(default=None, alias="ACLNames")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    authentication: Optional[AuthenticationModel] = Field(
        default=None, alias="Authentication"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class SubnetModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="AvailabilityZone"
    )


class BatchUpdateClusterRequestModel(BaseModel):
    cluster_names: Sequence[str] = Field(alias="ClusterNames")
    service_update: Optional[ServiceUpdateRequestModel] = Field(
        default=None, alias="ServiceUpdate"
    )


class ListAllowedNodeTypeUpdatesResponseModel(BaseModel):
    scale_up_node_types: List[str] = Field(alias="ScaleUpNodeTypes")
    scale_down_node_types: List[str] = Field(alias="ScaleDownNodeTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")


class CopySnapshotRequestModel(BaseModel):
    source_snapshot_name: str = Field(alias="SourceSnapshotName")
    target_snapshot_name: str = Field(alias="TargetSnapshotName")
    target_bucket: Optional[str] = Field(default=None, alias="TargetBucket")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateACLRequestModel(BaseModel):
    acl_name: str = Field(alias="ACLName")
    user_names: Optional[Sequence[str]] = Field(default=None, alias="UserNames")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    node_type: str = Field(alias="NodeType")
    acl_name: str = Field(alias="ACLName")
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    num_shards: Optional[int] = Field(default=None, alias="NumShards")
    num_replicas_per_shard: Optional[int] = Field(
        default=None, alias="NumReplicasPerShard"
    )
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    maintenance_window: Optional[str] = Field(default=None, alias="MaintenanceWindow")
    port: Optional[int] = Field(default=None, alias="Port")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    tl_s_enabled: Optional[bool] = Field(default=None, alias="TLSEnabled")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    snapshot_arns: Optional[Sequence[str]] = Field(default=None, alias="SnapshotArns")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    data_tiering: Optional[bool] = Field(default=None, alias="DataTiering")


class CreateParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    family: str = Field(alias="Family")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    snapshot_name: str = Field(alias="SnapshotName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_mode: AuthenticationModeModel = Field(alias="AuthenticationMode")
    access_string: str = Field(alias="AccessString")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseReservedNodesOfferingRequestModel(BaseModel):
    reserved_nodes_offering_id: str = Field(alias="ReservedNodesOfferingId")
    reservation_id: Optional[str] = Field(default=None, alias="ReservationId")
    node_count: Optional[int] = Field(default=None, alias="NodeCount")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class TagResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeParameterGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    parameter_groups: List[ParameterGroupModel] = Field(alias="ParameterGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeACLsRequestDescribeACLsPaginateModel(BaseModel):
    acl_name: Optional[str] = Field(default=None, alias="ACLName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClustersRequestDescribeClustersPaginateModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    show_shard_details: Optional[bool] = Field(default=None, alias="ShowShardDetails")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEngineVersionsRequestDescribeEngineVersionsPaginateModel(BaseModel):
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    parameter_group_family: Optional[str] = Field(
        default=None, alias="ParameterGroupFamily"
    )
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsRequestDescribeEventsPaginateModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["acl", "cluster", "node", "parameter-group", "subnet-group", "user"]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeParametersRequestDescribeParametersPaginateModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateModel(
    BaseModel
):
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedNodesRequestDescribeReservedNodesPaginateModel(BaseModel):
    reservation_id: Optional[str] = Field(default=None, alias="ReservationId")
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    cluster_names: Optional[Sequence[str]] = Field(default=None, alias="ClusterNames")
    status: Optional[
        Sequence[Literal["available", "complete", "in-progress", "scheduled"]]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotsRequestDescribeSnapshotsPaginateModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    source: Optional[str] = Field(default=None, alias="Source")
    show_detail: Optional[bool] = Field(default=None, alias="ShowDetail")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateModel(BaseModel):
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEngineVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    engine_versions: List[EngineVersionInfoModel] = Field(alias="EngineVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeParametersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    parameters: List[ParameterModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServiceUpdatesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    service_updates: List[ServiceUpdateModel] = Field(alias="ServiceUpdates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUsersRequestDescribeUsersPaginateModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUsersRequestModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    parameter_name_values: Sequence[ParameterNameValueModel] = Field(
        alias="ParameterNameValues"
    )


class ReservedNodeModel(BaseModel):
    reservation_id: Optional[str] = Field(default=None, alias="ReservationId")
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    node_count: Optional[int] = Field(default=None, alias="NodeCount")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    state: Optional[str] = Field(default=None, alias="State")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class ReservedNodesOfferingModel(BaseModel):
    reserved_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodesOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )


class ReshardingStatusModel(BaseModel):
    slot_migration: Optional[SlotMigrationModel] = Field(
        default=None, alias="SlotMigration"
    )


class UpdateClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    description: Optional[str] = Field(default=None, alias="Description")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    maintenance_window: Optional[str] = Field(default=None, alias="MaintenanceWindow")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    sns_topic_status: Optional[str] = Field(default=None, alias="SnsTopicStatus")
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    replica_configuration: Optional[ReplicaConfigurationRequestModel] = Field(
        default=None, alias="ReplicaConfiguration"
    )
    shard_configuration: Optional[ShardConfigurationRequestModel] = Field(
        default=None, alias="ShardConfiguration"
    )
    acl_name: Optional[str] = Field(default=None, alias="ACLName")


class ShardDetailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    configuration: Optional[ShardConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    size: Optional[str] = Field(default=None, alias="Size")
    snapshot_creation_time: Optional[datetime] = Field(
        default=None, alias="SnapshotCreationTime"
    )


class CreateACLResponseModel(BaseModel):
    acl: ACLModel = Field(alias="ACL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteACLResponseModel(BaseModel):
    acl: ACLModel = Field(alias="ACL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeACLsResponseModel(BaseModel):
    acls: List[ACLModel] = Field(alias="ACLs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateACLResponseModel(BaseModel):
    acl: ACLModel = Field(alias="ACL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubnetGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    arn: Optional[str] = Field(default=None, alias="ARN")


class ShardModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    slots: Optional[str] = Field(default=None, alias="Slots")
    nodes: Optional[List[NodeModel]] = Field(default=None, alias="Nodes")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")


class DescribeReservedNodesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_nodes: List[ReservedNodeModel] = Field(alias="ReservedNodes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseReservedNodesOfferingResponseModel(BaseModel):
    reserved_node: ReservedNodeModel = Field(alias="ReservedNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservedNodesOfferingsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_nodes_offerings: List[ReservedNodesOfferingModel] = Field(
        alias="ReservedNodesOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterPendingUpdatesModel(BaseModel):
    resharding: Optional[ReshardingStatusModel] = Field(
        default=None, alias="Resharding"
    )
    acls: Optional[ACLsUpdateStatusModel] = Field(default=None, alias="ACLs")
    service_updates: Optional[List[PendingModifiedServiceUpdateModel]] = Field(
        default=None, alias="ServiceUpdates"
    )


class ClusterConfigurationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    maintenance_window: Optional[str] = Field(default=None, alias="MaintenanceWindow")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    port: Optional[int] = Field(default=None, alias="Port")
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    num_shards: Optional[int] = Field(default=None, alias="NumShards")
    shards: Optional[List[ShardDetailModel]] = Field(default=None, alias="Shards")


class CreateSubnetGroupResponseModel(BaseModel):
    subnet_group: SubnetGroupModel = Field(alias="SubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSubnetGroupResponseModel(BaseModel):
    subnet_group: SubnetGroupModel = Field(alias="SubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSubnetGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    subnet_groups: List[SubnetGroupModel] = Field(alias="SubnetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubnetGroupResponseModel(BaseModel):
    subnet_group: SubnetGroupModel = Field(alias="SubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[str] = Field(default=None, alias="Status")
    pending_updates: Optional[ClusterPendingUpdatesModel] = Field(
        default=None, alias="PendingUpdates"
    )
    number_of_shards: Optional[int] = Field(default=None, alias="NumberOfShards")
    shards: Optional[List[ShardModel]] = Field(default=None, alias="Shards")
    availability_mode: Optional[Literal["multiaz", "singleaz"]] = Field(
        default=None, alias="AvailabilityMode"
    )
    cluster_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ClusterEndpoint"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    engine_patch_version: Optional[str] = Field(
        default=None, alias="EnginePatchVersion"
    )
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    parameter_group_status: Optional[str] = Field(
        default=None, alias="ParameterGroupStatus"
    )
    security_groups: Optional[List[SecurityGroupMembershipModel]] = Field(
        default=None, alias="SecurityGroups"
    )
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    tl_s_enabled: Optional[bool] = Field(default=None, alias="TLSEnabled")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    arn: Optional[str] = Field(default=None, alias="ARN")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    sns_topic_status: Optional[str] = Field(default=None, alias="SnsTopicStatus")
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    maintenance_window: Optional[str] = Field(default=None, alias="MaintenanceWindow")
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    acl_name: Optional[str] = Field(default=None, alias="ACLName")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    data_tiering: Optional[Literal["false", "true"]] = Field(
        default=None, alias="DataTiering"
    )


class SnapshotModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    source: Optional[str] = Field(default=None, alias="Source")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    arn: Optional[str] = Field(default=None, alias="ARN")
    cluster_configuration: Optional[ClusterConfigurationModel] = Field(
        default=None, alias="ClusterConfiguration"
    )
    data_tiering: Optional[Literal["false", "true"]] = Field(
        default=None, alias="DataTiering"
    )


class BatchUpdateClusterResponseModel(BaseModel):
    processed_clusters: List[ClusterModel] = Field(alias="ProcessedClusters")
    unprocessed_clusters: List[UnprocessedClusterModel] = Field(
        alias="UnprocessedClusters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClustersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    clusters: List[ClusterModel] = Field(alias="Clusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailoverShardResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopySnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotResponseModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    snapshots: List[SnapshotModel] = Field(alias="Snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
