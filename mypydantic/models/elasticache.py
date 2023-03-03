# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AuthenticationModeModel(BaseModel):
    type: Optional[Literal["iam", "no-password-required", "password"]] = Field(
        default=None, alias="Type"
    )
    passwords: Optional[Sequence[str]] = Field(default=None, alias="Passwords")


class AuthenticationModel(BaseModel):
    type: Optional[Literal["iam", "no-password", "password"]] = Field(
        default=None, alias="Type"
    )
    password_count: Optional[int] = Field(default=None, alias="PasswordCount")


class AuthorizeCacheSecurityGroupIngressMessageRequestModel(BaseModel):
    cache_security_group_name: str = Field(alias="CacheSecurityGroupName")
    ec2_security_group_name: str = Field(alias="EC2SecurityGroupName")
    ec2_security_group_owner_id: str = Field(alias="EC2SecurityGroupOwnerId")


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class BatchApplyUpdateActionMessageRequestModel(BaseModel):
    service_update_name: str = Field(alias="ServiceUpdateName")
    replication_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ReplicationGroupIds"
    )
    cache_cluster_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CacheClusterIds"
    )


class BatchStopUpdateActionMessageRequestModel(BaseModel):
    service_update_name: str = Field(alias="ServiceUpdateName")
    replication_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ReplicationGroupIds"
    )
    cache_cluster_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CacheClusterIds"
    )


class CacheParameterGroupStatusModel(BaseModel):
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    cache_node_ids_to_reboot: Optional[List[str]] = Field(
        default=None, alias="CacheNodeIdsToReboot"
    )


class CacheSecurityGroupMembershipModel(BaseModel):
    cache_security_group_name: Optional[str] = Field(
        default=None, alias="CacheSecurityGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")


class NotificationConfigurationModel(BaseModel):
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    topic_status: Optional[str] = Field(default=None, alias="TopicStatus")


class SecurityGroupMembershipModel(BaseModel):
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")
    status: Optional[str] = Field(default=None, alias="Status")


class CacheEngineVersionModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_family: Optional[str] = Field(
        default=None, alias="CacheParameterGroupFamily"
    )
    cache_engine_description: Optional[str] = Field(
        default=None, alias="CacheEngineDescription"
    )
    cache_engine_version_description: Optional[str] = Field(
        default=None, alias="CacheEngineVersionDescription"
    )


class CacheNodeTypeSpecificValueModel(BaseModel):
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    value: Optional[str] = Field(default=None, alias="Value")


class CacheNodeUpdateStatusModel(BaseModel):
    cache_node_id: Optional[str] = Field(default=None, alias="CacheNodeId")
    node_update_status: Optional[
        Literal[
            "complete",
            "in-progress",
            "not-applied",
            "stopped",
            "stopping",
            "waiting-to-start",
        ]
    ] = Field(default=None, alias="NodeUpdateStatus")
    node_deletion_date: Optional[datetime] = Field(
        default=None, alias="NodeDeletionDate"
    )
    node_update_start_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateStartDate"
    )
    node_update_end_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateEndDate"
    )
    node_update_initiated_by: Optional[Literal["customer", "system"]] = Field(
        default=None, alias="NodeUpdateInitiatedBy"
    )
    node_update_initiated_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateInitiatedDate"
    )
    node_update_status_modified_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateStatusModifiedDate"
    )


class ParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    description: Optional[str] = Field(default=None, alias="Description")
    source: Optional[str] = Field(default=None, alias="Source")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    change_type: Optional[Literal["immediate", "requires-reboot"]] = Field(
        default=None, alias="ChangeType"
    )


class CacheParameterGroupModel(BaseModel):
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    cache_parameter_group_family: Optional[str] = Field(
        default=None, alias="CacheParameterGroupFamily"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    is_global: Optional[bool] = Field(default=None, alias="IsGlobal")
    arn: Optional[str] = Field(default=None, alias="ARN")


class EC2SecurityGroupModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class CloudWatchLogsDestinationDetailsModel(BaseModel):
    log_group: Optional[str] = Field(default=None, alias="LogGroup")


class CompleteMigrationMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    force: Optional[bool] = Field(default=None, alias="Force")


class ConfigureShardModel(BaseModel):
    node_group_id: str = Field(alias="NodeGroupId")
    new_replica_count: int = Field(alias="NewReplicaCount")
    preferred_availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredAvailabilityZones"
    )
    preferred_outpost_arns: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredOutpostArns"
    )


class CreateGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id_suffix: str = Field(
        alias="GlobalReplicationGroupIdSuffix"
    )
    primary_replication_group_id: str = Field(alias="PrimaryReplicationGroupId")
    global_replication_group_description: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupDescription"
    )


class NodeGroupConfigurationModel(BaseModel):
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    slots: Optional[str] = Field(default=None, alias="Slots")
    replica_count: Optional[int] = Field(default=None, alias="ReplicaCount")
    primary_availability_zone: Optional[str] = Field(
        default=None, alias="PrimaryAvailabilityZone"
    )
    replica_availability_zones: Optional[List[str]] = Field(
        default=None, alias="ReplicaAvailabilityZones"
    )
    primary_outpost_arn: Optional[str] = Field(default=None, alias="PrimaryOutpostArn")
    replica_outpost_arns: Optional[List[str]] = Field(
        default=None, alias="ReplicaOutpostArns"
    )


class CustomerNodeEndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")


class DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    node_group_count: int = Field(alias="NodeGroupCount")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    global_node_groups_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="GlobalNodeGroupsToRemove"
    )
    global_node_groups_to_retain: Optional[Sequence[str]] = Field(
        default=None, alias="GlobalNodeGroupsToRetain"
    )


class DeleteCacheClusterMessageRequestModel(BaseModel):
    cache_cluster_id: str = Field(alias="CacheClusterId")
    final_snapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalSnapshotIdentifier"
    )


class DeleteCacheParameterGroupMessageRequestModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")


class DeleteCacheSecurityGroupMessageRequestModel(BaseModel):
    cache_security_group_name: str = Field(alias="CacheSecurityGroupName")


class DeleteCacheSubnetGroupMessageRequestModel(BaseModel):
    cache_subnet_group_name: str = Field(alias="CacheSubnetGroupName")


class DeleteGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    retain_primary_replication_group: bool = Field(
        alias="RetainPrimaryReplicationGroup"
    )


class DeleteReplicationGroupMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    retain_primary_cluster: Optional[bool] = Field(
        default=None, alias="RetainPrimaryCluster"
    )
    final_snapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalSnapshotIdentifier"
    )


class DeleteSnapshotMessageRequestModel(BaseModel):
    snapshot_name: str = Field(alias="SnapshotName")


class DeleteUserGroupMessageRequestModel(BaseModel):
    user_group_id: str = Field(alias="UserGroupId")


class DeleteUserMessageRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeCacheClustersMessageRequestModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    show_cache_node_info: Optional[bool] = Field(
        default=None, alias="ShowCacheNodeInfo"
    )
    show_cache_clusters_not_in_replication_groups: Optional[bool] = Field(
        default=None, alias="ShowCacheClustersNotInReplicationGroups"
    )


class DescribeCacheEngineVersionsMessageRequestModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_family: Optional[str] = Field(
        default=None, alias="CacheParameterGroupFamily"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")


class DescribeCacheParameterGroupsMessageRequestModel(BaseModel):
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeCacheParametersMessageRequestModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeCacheSecurityGroupsMessageRequestModel(BaseModel):
    cache_security_group_name: Optional[str] = Field(
        default=None, alias="CacheSecurityGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeCacheSubnetGroupsMessageRequestModel(BaseModel):
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEngineDefaultParametersMessageRequestModel(BaseModel):
    cache_parameter_group_family: str = Field(alias="CacheParameterGroupFamily")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventsMessageRequestModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
            "user",
            "user-group",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeGlobalReplicationGroupsMessageRequestModel(BaseModel):
    global_replication_group_id: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    show_member_info: Optional[bool] = Field(default=None, alias="ShowMemberInfo")


class DescribeReplicationGroupsMessageRequestModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReservedCacheNodesMessageRequestModel(BaseModel):
    reserved_cache_node_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodeId"
    )
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReservedCacheNodesOfferingsMessageRequestModel(BaseModel):
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeServiceUpdatesMessageRequestModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    service_update_status: Optional[
        Sequence[Literal["available", "cancelled", "expired"]]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeSnapshotsMessageRequestModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    snapshot_source: Optional[str] = Field(default=None, alias="SnapshotSource")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    show_node_group_config: Optional[bool] = Field(
        default=None, alias="ShowNodeGroupConfig"
    )


class TimeRangeFilterModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")


class DescribeUserGroupsMessageRequestModel(BaseModel):
    user_group_id: Optional[str] = Field(default=None, alias="UserGroupId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class KinesisFirehoseDestinationDetailsModel(BaseModel):
    delivery_stream: Optional[str] = Field(default=None, alias="DeliveryStream")


class DisassociateGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    replication_group_id: str = Field(alias="ReplicationGroupId")
    replication_group_region: str = Field(alias="ReplicationGroupRegion")


class EventModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
            "user",
            "user-group",
        ]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    date: Optional[datetime] = Field(default=None, alias="Date")


class FailoverGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    primary_region: str = Field(alias="PrimaryRegion")
    primary_replication_group_id: str = Field(alias="PrimaryReplicationGroupId")


class GlobalNodeGroupModel(BaseModel):
    global_node_group_id: Optional[str] = Field(default=None, alias="GlobalNodeGroupId")
    slots: Optional[str] = Field(default=None, alias="Slots")


class GlobalReplicationGroupInfoModel(BaseModel):
    global_replication_group_id: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupId"
    )
    global_replication_group_member_role: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupMemberRole"
    )


class GlobalReplicationGroupMemberModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    replication_group_region: Optional[str] = Field(
        default=None, alias="ReplicationGroupRegion"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    automatic_failover: Optional[
        Literal["disabled", "disabling", "enabled", "enabling"]
    ] = Field(default=None, alias="AutomaticFailover")
    status: Optional[str] = Field(default=None, alias="Status")


class ListAllowedNodeTypeModificationsMessageRequestModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )


class ListTagsForResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")


class ParameterNameValueModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")


class ModifyCacheSubnetGroupMessageRequestModel(BaseModel):
    cache_subnet_group_name: str = Field(alias="CacheSubnetGroupName")
    cache_subnet_group_description: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupDescription"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class ModifyGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    global_replication_group_description: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupDescription"
    )
    automatic_failover_enabled: Optional[bool] = Field(
        default=None, alias="AutomaticFailoverEnabled"
    )


class ReshardingConfigurationModel(BaseModel):
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    preferred_availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredAvailabilityZones"
    )


class ModifyUserGroupMessageRequestModel(BaseModel):
    user_group_id: str = Field(alias="UserGroupId")
    user_ids_to_add: Optional[Sequence[str]] = Field(default=None, alias="UserIdsToAdd")
    user_ids_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="UserIdsToRemove"
    )


class NodeGroupMemberUpdateStatusModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    cache_node_id: Optional[str] = Field(default=None, alias="CacheNodeId")
    node_update_status: Optional[
        Literal[
            "complete",
            "in-progress",
            "not-applied",
            "stopped",
            "stopping",
            "waiting-to-start",
        ]
    ] = Field(default=None, alias="NodeUpdateStatus")
    node_deletion_date: Optional[datetime] = Field(
        default=None, alias="NodeDeletionDate"
    )
    node_update_start_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateStartDate"
    )
    node_update_end_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateEndDate"
    )
    node_update_initiated_by: Optional[Literal["customer", "system"]] = Field(
        default=None, alias="NodeUpdateInitiatedBy"
    )
    node_update_initiated_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateInitiatedDate"
    )
    node_update_status_modified_date: Optional[datetime] = Field(
        default=None, alias="NodeUpdateStatusModifiedDate"
    )


class ProcessedUpdateActionModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    update_action_status: Optional[
        Literal[
            "complete",
            "in-progress",
            "not-applicable",
            "not-applied",
            "scheduled",
            "scheduling",
            "stopped",
            "stopping",
            "waiting-to-start",
        ]
    ] = Field(default=None, alias="UpdateActionStatus")


class RebalanceSlotsInGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    apply_immediately: bool = Field(alias="ApplyImmediately")


class RebootCacheClusterMessageRequestModel(BaseModel):
    cache_cluster_id: str = Field(alias="CacheClusterId")
    cache_node_ids_to_reboot: Sequence[str] = Field(alias="CacheNodeIdsToReboot")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class RemoveTagsFromResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UserGroupsUpdateStatusModel(BaseModel):
    user_group_ids_to_add: Optional[List[str]] = Field(
        default=None, alias="UserGroupIdsToAdd"
    )
    user_group_ids_to_remove: Optional[List[str]] = Field(
        default=None, alias="UserGroupIdsToRemove"
    )


class SlotMigrationModel(BaseModel):
    progress_percentage: Optional[float] = Field(
        default=None, alias="ProgressPercentage"
    )


class RevokeCacheSecurityGroupIngressMessageRequestModel(BaseModel):
    cache_security_group_name: str = Field(alias="CacheSecurityGroupName")
    ec2_security_group_name: str = Field(alias="EC2SecurityGroupName")
    ec2_security_group_owner_id: str = Field(alias="EC2SecurityGroupOwnerId")


class ServiceUpdateModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    service_update_release_date: Optional[datetime] = Field(
        default=None, alias="ServiceUpdateReleaseDate"
    )
    service_update_end_date: Optional[datetime] = Field(
        default=None, alias="ServiceUpdateEndDate"
    )
    service_update_severity: Optional[
        Literal["critical", "important", "low", "medium"]
    ] = Field(default=None, alias="ServiceUpdateSeverity")
    service_update_recommended_apply_by_date: Optional[datetime] = Field(
        default=None, alias="ServiceUpdateRecommendedApplyByDate"
    )
    service_update_status: Optional[
        Literal["available", "cancelled", "expired"]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    service_update_description: Optional[str] = Field(
        default=None, alias="ServiceUpdateDescription"
    )
    service_update_type: Optional[Literal["security-update"]] = Field(
        default=None, alias="ServiceUpdateType"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_update_after_recommended_apply_by_date: Optional[bool] = Field(
        default=None, alias="AutoUpdateAfterRecommendedApplyByDate"
    )
    estimated_update_time: Optional[str] = Field(
        default=None, alias="EstimatedUpdateTime"
    )


class SubnetOutpostModel(BaseModel):
    subnet_outpost_arn: Optional[str] = Field(default=None, alias="SubnetOutpostArn")


class TestFailoverMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    node_group_id: str = Field(alias="NodeGroupId")


class UnprocessedUpdateActionModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    error_type: Optional[str] = Field(default=None, alias="ErrorType")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class UserGroupPendingChangesModel(BaseModel):
    user_ids_to_remove: Optional[List[str]] = Field(
        default=None, alias="UserIdsToRemove"
    )
    user_ids_to_add: Optional[List[str]] = Field(default=None, alias="UserIdsToAdd")


class AddTagsToResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CopySnapshotMessageRequestModel(BaseModel):
    source_snapshot_name: str = Field(alias="SourceSnapshotName")
    target_snapshot_name: str = Field(alias="TargetSnapshotName")
    target_bucket: Optional[str] = Field(default=None, alias="TargetBucket")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCacheParameterGroupMessageRequestModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    cache_parameter_group_family: str = Field(alias="CacheParameterGroupFamily")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCacheSecurityGroupMessageRequestModel(BaseModel):
    cache_security_group_name: str = Field(alias="CacheSecurityGroupName")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCacheSubnetGroupMessageRequestModel(BaseModel):
    cache_subnet_group_name: str = Field(alias="CacheSubnetGroupName")
    cache_subnet_group_description: str = Field(alias="CacheSubnetGroupDescription")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotMessageRequestModel(BaseModel):
    snapshot_name: str = Field(alias="SnapshotName")
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserGroupMessageRequestModel(BaseModel):
    user_group_id: str = Field(alias="UserGroupId")
    engine: str = Field(alias="Engine")
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="UserIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PurchaseReservedCacheNodesOfferingMessageRequestModel(BaseModel):
    reserved_cache_nodes_offering_id: str = Field(alias="ReservedCacheNodesOfferingId")
    reserved_cache_node_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodeId"
    )
    cache_node_count: Optional[int] = Field(default=None, alias="CacheNodeCount")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class AllowedNodeTypeModificationsMessageModel(BaseModel):
    scale_up_modifications: List[str] = Field(alias="ScaleUpModifications")
    scale_down_modifications: List[str] = Field(alias="ScaleDownModifications")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheParameterGroupNameMessageModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagListMessageModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserMessageRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    user_name: str = Field(alias="UserName")
    engine: str = Field(alias="Engine")
    access_string: str = Field(alias="AccessString")
    passwords: Optional[Sequence[str]] = Field(default=None, alias="Passwords")
    no_password_required: Optional[bool] = Field(
        default=None, alias="NoPasswordRequired"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    authentication_mode: Optional[AuthenticationModeModel] = Field(
        default=None, alias="AuthenticationMode"
    )


class ModifyUserMessageRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    access_string: Optional[str] = Field(default=None, alias="AccessString")
    append_access_string: Optional[str] = Field(
        default=None, alias="AppendAccessString"
    )
    passwords: Optional[Sequence[str]] = Field(default=None, alias="Passwords")
    no_password_required: Optional[bool] = Field(
        default=None, alias="NoPasswordRequired"
    )
    authentication_mode: Optional[AuthenticationModeModel] = Field(
        default=None, alias="AuthenticationMode"
    )


class UserResponseMetadataModel(BaseModel):
    user_id: str = Field(alias="UserId")
    user_name: str = Field(alias="UserName")
    status: str = Field(alias="Status")
    engine: str = Field(alias="Engine")
    minimum_engine_version: str = Field(alias="MinimumEngineVersion")
    access_string: str = Field(alias="AccessString")
    user_group_ids: List[str] = Field(alias="UserGroupIds")
    authentication: AuthenticationModel = Field(alias="Authentication")
    arn: str = Field(alias="ARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="UserId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    status: Optional[str] = Field(default=None, alias="Status")
    engine: Optional[str] = Field(default=None, alias="Engine")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    access_string: Optional[str] = Field(default=None, alias="AccessString")
    user_group_ids: Optional[List[str]] = Field(default=None, alias="UserGroupIds")
    authentication: Optional[AuthenticationModel] = Field(
        default=None, alias="Authentication"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class CacheNodeModel(BaseModel):
    cache_node_id: Optional[str] = Field(default=None, alias="CacheNodeId")
    cache_node_status: Optional[str] = Field(default=None, alias="CacheNodeStatus")
    cache_node_create_time: Optional[datetime] = Field(
        default=None, alias="CacheNodeCreateTime"
    )
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")
    parameter_group_status: Optional[str] = Field(
        default=None, alias="ParameterGroupStatus"
    )
    source_cache_node_id: Optional[str] = Field(default=None, alias="SourceCacheNodeId")
    customer_availability_zone: Optional[str] = Field(
        default=None, alias="CustomerAvailabilityZone"
    )
    customer_outpost_arn: Optional[str] = Field(
        default=None, alias="CustomerOutpostArn"
    )


class NodeGroupMemberModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    cache_node_id: Optional[str] = Field(default=None, alias="CacheNodeId")
    read_endpoint: Optional[EndpointModel] = Field(default=None, alias="ReadEndpoint")
    preferred_availability_zone: Optional[str] = Field(
        default=None, alias="PreferredAvailabilityZone"
    )
    preferred_outpost_arn: Optional[str] = Field(
        default=None, alias="PreferredOutpostArn"
    )
    current_role: Optional[str] = Field(default=None, alias="CurrentRole")


class CacheEngineVersionMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cache_engine_versions: List[CacheEngineVersionModel] = Field(
        alias="CacheEngineVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheNodeTypeSpecificParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    description: Optional[str] = Field(default=None, alias="Description")
    source: Optional[str] = Field(default=None, alias="Source")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    cache_node_type_specific_values: Optional[
        List[CacheNodeTypeSpecificValueModel]
    ] = Field(default=None, alias="CacheNodeTypeSpecificValues")
    change_type: Optional[Literal["immediate", "requires-reboot"]] = Field(
        default=None, alias="ChangeType"
    )


class CacheParameterGroupsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cache_parameter_groups: List[CacheParameterGroupModel] = Field(
        alias="CacheParameterGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCacheParameterGroupResultModel(BaseModel):
    cache_parameter_group: CacheParameterGroupModel = Field(alias="CacheParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheSecurityGroupModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    cache_security_group_name: Optional[str] = Field(
        default=None, alias="CacheSecurityGroupName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    ec2_security_groups: Optional[List[EC2SecurityGroupModel]] = Field(
        default=None, alias="EC2SecurityGroups"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class DecreaseReplicaCountMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    new_replica_count: Optional[int] = Field(default=None, alias="NewReplicaCount")
    replica_configuration: Optional[Sequence[ConfigureShardModel]] = Field(
        default=None, alias="ReplicaConfiguration"
    )
    replicas_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="ReplicasToRemove"
    )


class IncreaseReplicaCountMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    new_replica_count: Optional[int] = Field(default=None, alias="NewReplicaCount")
    replica_configuration: Optional[Sequence[ConfigureShardModel]] = Field(
        default=None, alias="ReplicaConfiguration"
    )


class NodeSnapshotModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    cache_node_id: Optional[str] = Field(default=None, alias="CacheNodeId")
    node_group_configuration: Optional[NodeGroupConfigurationModel] = Field(
        default=None, alias="NodeGroupConfiguration"
    )
    cache_size: Optional[str] = Field(default=None, alias="CacheSize")
    cache_node_create_time: Optional[datetime] = Field(
        default=None, alias="CacheNodeCreateTime"
    )
    snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="SnapshotCreateTime"
    )


class StartMigrationMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    customer_node_endpoint_list: Sequence[CustomerNodeEndpointModel] = Field(
        alias="CustomerNodeEndpointList"
    )


class DescribeCacheClustersMessageCacheClusterAvailableWaitModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    show_cache_node_info: Optional[bool] = Field(
        default=None, alias="ShowCacheNodeInfo"
    )
    show_cache_clusters_not_in_replication_groups: Optional[bool] = Field(
        default=None, alias="ShowCacheClustersNotInReplicationGroups"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeCacheClustersMessageCacheClusterDeletedWaitModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    show_cache_node_info: Optional[bool] = Field(
        default=None, alias="ShowCacheNodeInfo"
    )
    show_cache_clusters_not_in_replication_groups: Optional[bool] = Field(
        default=None, alias="ShowCacheClustersNotInReplicationGroups"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationGroupsMessageReplicationGroupAvailableWaitModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationGroupsMessageReplicationGroupDeletedWaitModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeCacheClustersMessageDescribeCacheClustersPaginateModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    show_cache_node_info: Optional[bool] = Field(
        default=None, alias="ShowCacheNodeInfo"
    )
    show_cache_clusters_not_in_replication_groups: Optional[bool] = Field(
        default=None, alias="ShowCacheClustersNotInReplicationGroups"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateModel(
    BaseModel
):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_family: Optional[str] = Field(
        default=None, alias="CacheParameterGroupFamily"
    )
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateModel(
    BaseModel
):
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCacheParametersMessageDescribeCacheParametersPaginateModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateModel(
    BaseModel
):
    cache_security_group_name: Optional[str] = Field(
        default=None, alias="CacheSecurityGroupName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateModel(BaseModel):
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateModel(
    BaseModel
):
    cache_parameter_group_family: str = Field(alias="CacheParameterGroupFamily")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsMessageDescribeEventsPaginateModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
            "user",
            "user-group",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateModel(
    BaseModel
):
    global_replication_group_id: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupId"
    )
    show_member_info: Optional[bool] = Field(default=None, alias="ShowMemberInfo")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateModel(
    BaseModel
):
    reserved_cache_node_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodeId"
    )
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateModel(
    BaseModel
):
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    service_update_status: Optional[
        Sequence[Literal["available", "cancelled", "expired"]]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotsMessageDescribeSnapshotsPaginateModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    snapshot_source: Optional[str] = Field(default=None, alias="SnapshotSource")
    show_node_group_config: Optional[bool] = Field(
        default=None, alias="ShowNodeGroupConfig"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUserGroupsMessageDescribeUserGroupsPaginateModel(BaseModel):
    user_group_id: Optional[str] = Field(default=None, alias="UserGroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUpdateActionsMessageDescribeUpdateActionsPaginateModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    replication_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ReplicationGroupIds"
    )
    cache_cluster_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CacheClusterIds"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    service_update_status: Optional[
        Sequence[Literal["available", "cancelled", "expired"]]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    service_update_time_range: Optional[TimeRangeFilterModel] = Field(
        default=None, alias="ServiceUpdateTimeRange"
    )
    update_action_status: Optional[
        Sequence[
            Literal[
                "complete",
                "in-progress",
                "not-applicable",
                "not-applied",
                "scheduled",
                "scheduling",
                "stopped",
                "stopping",
                "waiting-to-start",
            ]
        ]
    ] = Field(default=None, alias="UpdateActionStatus")
    show_node_level_update_status: Optional[bool] = Field(
        default=None, alias="ShowNodeLevelUpdateStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUpdateActionsMessageRequestModel(BaseModel):
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    replication_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ReplicationGroupIds"
    )
    cache_cluster_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CacheClusterIds"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    service_update_status: Optional[
        Sequence[Literal["available", "cancelled", "expired"]]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    service_update_time_range: Optional[TimeRangeFilterModel] = Field(
        default=None, alias="ServiceUpdateTimeRange"
    )
    update_action_status: Optional[
        Sequence[
            Literal[
                "complete",
                "in-progress",
                "not-applicable",
                "not-applied",
                "scheduled",
                "scheduling",
                "stopped",
                "stopping",
                "waiting-to-start",
            ]
        ]
    ] = Field(default=None, alias="UpdateActionStatus")
    show_node_level_update_status: Optional[bool] = Field(
        default=None, alias="ShowNodeLevelUpdateStatus"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeUsersMessageDescribeUsersPaginateModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUsersMessageRequestModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DestinationDetailsModel(BaseModel):
    cloud_watch_logs_details: Optional[CloudWatchLogsDestinationDetailsModel] = Field(
        default=None, alias="CloudWatchLogsDetails"
    )
    kinesis_firehose_details: Optional[KinesisFirehoseDestinationDetailsModel] = Field(
        default=None, alias="KinesisFirehoseDetails"
    )


class EventsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlobalReplicationGroupModel(BaseModel):
    global_replication_group_id: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupId"
    )
    global_replication_group_description: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupDescription"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    members: Optional[List[GlobalReplicationGroupMemberModel]] = Field(
        default=None, alias="Members"
    )
    cluster_enabled: Optional[bool] = Field(default=None, alias="ClusterEnabled")
    global_node_groups: Optional[List[GlobalNodeGroupModel]] = Field(
        default=None, alias="GlobalNodeGroups"
    )
    auth_token_enabled: Optional[bool] = Field(default=None, alias="AuthTokenEnabled")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="AtRestEncryptionEnabled"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class ModifyCacheParameterGroupMessageRequestModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    parameter_name_values: Sequence[ParameterNameValueModel] = Field(
        alias="ParameterNameValues"
    )


class ResetCacheParameterGroupMessageRequestModel(BaseModel):
    cache_parameter_group_name: str = Field(alias="CacheParameterGroupName")
    reset_all_parameters: Optional[bool] = Field(
        default=None, alias="ResetAllParameters"
    )
    parameter_name_values: Optional[Sequence[ParameterNameValueModel]] = Field(
        default=None, alias="ParameterNameValues"
    )


class ModifyReplicationGroupShardConfigurationMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    node_group_count: int = Field(alias="NodeGroupCount")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    resharding_configuration: Optional[Sequence[ReshardingConfigurationModel]] = Field(
        default=None, alias="ReshardingConfiguration"
    )
    node_groups_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="NodeGroupsToRemove"
    )
    node_groups_to_retain: Optional[Sequence[str]] = Field(
        default=None, alias="NodeGroupsToRetain"
    )


class RegionalConfigurationModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    replication_group_region: str = Field(alias="ReplicationGroupRegion")
    resharding_configuration: Sequence[ReshardingConfigurationModel] = Field(
        alias="ReshardingConfiguration"
    )


class NodeGroupUpdateStatusModel(BaseModel):
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    node_group_member_update_status: Optional[
        List[NodeGroupMemberUpdateStatusModel]
    ] = Field(default=None, alias="NodeGroupMemberUpdateStatus")


class ReservedCacheNodeModel(BaseModel):
    reserved_cache_node_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodeId"
    )
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    cache_node_count: Optional[int] = Field(default=None, alias="CacheNodeCount")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    state: Optional[str] = Field(default=None, alias="State")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )
    reservation_arn: Optional[str] = Field(default=None, alias="ReservationARN")


class ReservedCacheNodesOfferingModel(BaseModel):
    reserved_cache_nodes_offering_id: Optional[str] = Field(
        default=None, alias="ReservedCacheNodesOfferingId"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )


class ReshardingStatusModel(BaseModel):
    slot_migration: Optional[SlotMigrationModel] = Field(
        default=None, alias="SlotMigration"
    )


class ServiceUpdatesMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    service_updates: List[ServiceUpdateModel] = Field(alias="ServiceUpdates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_outpost: Optional[SubnetOutpostModel] = Field(
        default=None, alias="SubnetOutpost"
    )
    supported_network_types: Optional[
        List[Literal["dual_stack", "ipv4", "ipv6"]]
    ] = Field(default=None, alias="SupportedNetworkTypes")


class UpdateActionResultsMessageModel(BaseModel):
    processed_update_actions: List[ProcessedUpdateActionModel] = Field(
        alias="ProcessedUpdateActions"
    )
    unprocessed_update_actions: List[UnprocessedUpdateActionModel] = Field(
        alias="UnprocessedUpdateActions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserGroupResponseMetadataModel(BaseModel):
    user_group_id: str = Field(alias="UserGroupId")
    status: str = Field(alias="Status")
    engine: str = Field(alias="Engine")
    user_ids: List[str] = Field(alias="UserIds")
    minimum_engine_version: str = Field(alias="MinimumEngineVersion")
    pending_changes: UserGroupPendingChangesModel = Field(alias="PendingChanges")
    replication_groups: List[str] = Field(alias="ReplicationGroups")
    arn: str = Field(alias="ARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserGroupModel(BaseModel):
    user_group_id: Optional[str] = Field(default=None, alias="UserGroupId")
    status: Optional[str] = Field(default=None, alias="Status")
    engine: Optional[str] = Field(default=None, alias="Engine")
    user_ids: Optional[List[str]] = Field(default=None, alias="UserIds")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    pending_changes: Optional[UserGroupPendingChangesModel] = Field(
        default=None, alias="PendingChanges"
    )
    replication_groups: Optional[List[str]] = Field(
        default=None, alias="ReplicationGroups"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")


class DescribeUsersResultModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodeGroupModel(BaseModel):
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    status: Optional[str] = Field(default=None, alias="Status")
    primary_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="PrimaryEndpoint"
    )
    reader_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ReaderEndpoint"
    )
    slots: Optional[str] = Field(default=None, alias="Slots")
    node_group_members: Optional[List[NodeGroupMemberModel]] = Field(
        default=None, alias="NodeGroupMembers"
    )


class CacheParameterGroupDetailsModel(BaseModel):
    marker: str = Field(alias="Marker")
    parameters: List[ParameterModel] = Field(alias="Parameters")
    cache_node_type_specific_parameters: List[
        CacheNodeTypeSpecificParameterModel
    ] = Field(alias="CacheNodeTypeSpecificParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EngineDefaultsModel(BaseModel):
    cache_parameter_group_family: Optional[str] = Field(
        default=None, alias="CacheParameterGroupFamily"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    parameters: Optional[List[ParameterModel]] = Field(default=None, alias="Parameters")
    cache_node_type_specific_parameters: Optional[
        List[CacheNodeTypeSpecificParameterModel]
    ] = Field(default=None, alias="CacheNodeTypeSpecificParameters")


class AuthorizeCacheSecurityGroupIngressResultModel(BaseModel):
    cache_security_group: CacheSecurityGroupModel = Field(alias="CacheSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheSecurityGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cache_security_groups: List[CacheSecurityGroupModel] = Field(
        alias="CacheSecurityGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCacheSecurityGroupResultModel(BaseModel):
    cache_security_group: CacheSecurityGroupModel = Field(alias="CacheSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeCacheSecurityGroupIngressResultModel(BaseModel):
    cache_security_group: CacheSecurityGroupModel = Field(alias="CacheSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SnapshotModel(BaseModel):
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    replication_group_description: Optional[str] = Field(
        default=None, alias="ReplicationGroupDescription"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    snapshot_status: Optional[str] = Field(default=None, alias="SnapshotStatus")
    snapshot_source: Optional[str] = Field(default=None, alias="SnapshotSource")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    num_cache_nodes: Optional[int] = Field(default=None, alias="NumCacheNodes")
    preferred_availability_zone: Optional[str] = Field(
        default=None, alias="PreferredAvailabilityZone"
    )
    preferred_outpost_arn: Optional[str] = Field(
        default=None, alias="PreferredOutpostArn"
    )
    cache_cluster_create_time: Optional[datetime] = Field(
        default=None, alias="CacheClusterCreateTime"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    port: Optional[int] = Field(default=None, alias="Port")
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    num_node_groups: Optional[int] = Field(default=None, alias="NumNodeGroups")
    automatic_failover: Optional[
        Literal["disabled", "disabling", "enabled", "enabling"]
    ] = Field(default=None, alias="AutomaticFailover")
    node_snapshots: Optional[List[NodeSnapshotModel]] = Field(
        default=None, alias="NodeSnapshots"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    arn: Optional[str] = Field(default=None, alias="ARN")
    data_tiering: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="DataTiering"
    )


class LogDeliveryConfigurationRequestModel(BaseModel):
    log_type: Optional[Literal["engine-log", "slow-log"]] = Field(
        default=None, alias="LogType"
    )
    destination_type: Optional[Literal["cloudwatch-logs", "kinesis-firehose"]] = Field(
        default=None, alias="DestinationType"
    )
    destination_details: Optional[DestinationDetailsModel] = Field(
        default=None, alias="DestinationDetails"
    )
    log_format: Optional[Literal["json", "text"]] = Field(
        default=None, alias="LogFormat"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class LogDeliveryConfigurationModel(BaseModel):
    log_type: Optional[Literal["engine-log", "slow-log"]] = Field(
        default=None, alias="LogType"
    )
    destination_type: Optional[Literal["cloudwatch-logs", "kinesis-firehose"]] = Field(
        default=None, alias="DestinationType"
    )
    destination_details: Optional[DestinationDetailsModel] = Field(
        default=None, alias="DestinationDetails"
    )
    log_format: Optional[Literal["json", "text"]] = Field(
        default=None, alias="LogFormat"
    )
    status: Optional[
        Literal["active", "disabling", "enabling", "error", "modifying"]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")


class PendingLogDeliveryConfigurationModel(BaseModel):
    log_type: Optional[Literal["engine-log", "slow-log"]] = Field(
        default=None, alias="LogType"
    )
    destination_type: Optional[Literal["cloudwatch-logs", "kinesis-firehose"]] = Field(
        default=None, alias="DestinationType"
    )
    destination_details: Optional[DestinationDetailsModel] = Field(
        default=None, alias="DestinationDetails"
    )
    log_format: Optional[Literal["json", "text"]] = Field(
        default=None, alias="LogFormat"
    )


class CreateGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecreaseNodeGroupsInGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGlobalReplicationGroupsResultModel(BaseModel):
    marker: str = Field(alias="Marker")
    global_replication_groups: List[GlobalReplicationGroupModel] = Field(
        alias="GlobalReplicationGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailoverGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IncreaseNodeGroupsInGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebalanceSlotsInGlobalReplicationGroupResultModel(BaseModel):
    global_replication_group: GlobalReplicationGroupModel = Field(
        alias="GlobalReplicationGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestModel(BaseModel):
    global_replication_group_id: str = Field(alias="GlobalReplicationGroupId")
    node_group_count: int = Field(alias="NodeGroupCount")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    regional_configurations: Optional[Sequence[RegionalConfigurationModel]] = Field(
        default=None, alias="RegionalConfigurations"
    )


class UpdateActionModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    service_update_name: Optional[str] = Field(default=None, alias="ServiceUpdateName")
    service_update_release_date: Optional[datetime] = Field(
        default=None, alias="ServiceUpdateReleaseDate"
    )
    service_update_severity: Optional[
        Literal["critical", "important", "low", "medium"]
    ] = Field(default=None, alias="ServiceUpdateSeverity")
    service_update_status: Optional[
        Literal["available", "cancelled", "expired"]
    ] = Field(default=None, alias="ServiceUpdateStatus")
    service_update_recommended_apply_by_date: Optional[datetime] = Field(
        default=None, alias="ServiceUpdateRecommendedApplyByDate"
    )
    service_update_type: Optional[Literal["security-update"]] = Field(
        default=None, alias="ServiceUpdateType"
    )
    update_action_available_date: Optional[datetime] = Field(
        default=None, alias="UpdateActionAvailableDate"
    )
    update_action_status: Optional[
        Literal[
            "complete",
            "in-progress",
            "not-applicable",
            "not-applied",
            "scheduled",
            "scheduling",
            "stopped",
            "stopping",
            "waiting-to-start",
        ]
    ] = Field(default=None, alias="UpdateActionStatus")
    nodes_updated: Optional[str] = Field(default=None, alias="NodesUpdated")
    update_action_status_modified_date: Optional[datetime] = Field(
        default=None, alias="UpdateActionStatusModifiedDate"
    )
    sla_met: Optional[Literal["n/a", "no", "yes"]] = Field(default=None, alias="SlaMet")
    node_group_update_status: Optional[List[NodeGroupUpdateStatusModel]] = Field(
        default=None, alias="NodeGroupUpdateStatus"
    )
    cache_node_update_status: Optional[List[CacheNodeUpdateStatusModel]] = Field(
        default=None, alias="CacheNodeUpdateStatus"
    )
    estimated_update_time: Optional[str] = Field(
        default=None, alias="EstimatedUpdateTime"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")


class PurchaseReservedCacheNodesOfferingResultModel(BaseModel):
    reserved_cache_node: ReservedCacheNodeModel = Field(alias="ReservedCacheNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedCacheNodeMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_cache_nodes: List[ReservedCacheNodeModel] = Field(
        alias="ReservedCacheNodes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedCacheNodesOfferingMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_cache_nodes_offerings: List[ReservedCacheNodesOfferingModel] = Field(
        alias="ReservedCacheNodesOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheSubnetGroupModel(BaseModel):
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    cache_subnet_group_description: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    arn: Optional[str] = Field(default=None, alias="ARN")
    supported_network_types: Optional[
        List[Literal["dual_stack", "ipv4", "ipv6"]]
    ] = Field(default=None, alias="SupportedNetworkTypes")


class DescribeUserGroupsResultModel(BaseModel):
    user_groups: List[UserGroupModel] = Field(alias="UserGroups")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEngineDefaultParametersResultModel(BaseModel):
    engine_defaults: EngineDefaultsModel = Field(alias="EngineDefaults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopySnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotsListMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    snapshots: List[SnapshotModel] = Field(alias="Snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCacheClusterMessageRequestModel(BaseModel):
    cache_cluster_id: str = Field(alias="CacheClusterId")
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    azmode: Optional[Literal["cross-az", "single-az"]] = Field(
        default=None, alias="AZMode"
    )
    preferred_availability_zone: Optional[str] = Field(
        default=None, alias="PreferredAvailabilityZone"
    )
    preferred_availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredAvailabilityZones"
    )
    num_cache_nodes: Optional[int] = Field(default=None, alias="NumCacheNodes")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    cache_security_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="CacheSecurityGroupNames"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    snapshot_arns: Optional[Sequence[str]] = Field(default=None, alias="SnapshotArns")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")
    outpost_mode: Optional[Literal["cross-outpost", "single-outpost"]] = Field(
        default=None, alias="OutpostMode"
    )
    preferred_outpost_arn: Optional[str] = Field(
        default=None, alias="PreferredOutpostArn"
    )
    preferred_outpost_arns: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredOutpostArns"
    )
    log_delivery_configurations: Optional[
        Sequence[LogDeliveryConfigurationRequestModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    network_type: Optional[Literal["dual_stack", "ipv4", "ipv6"]] = Field(
        default=None, alias="NetworkType"
    )
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )


class CreateReplicationGroupMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    replication_group_description: str = Field(alias="ReplicationGroupDescription")
    global_replication_group_id: Optional[str] = Field(
        default=None, alias="GlobalReplicationGroupId"
    )
    primary_cluster_id: Optional[str] = Field(default=None, alias="PrimaryClusterId")
    automatic_failover_enabled: Optional[bool] = Field(
        default=None, alias="AutomaticFailoverEnabled"
    )
    multi_azenabled: Optional[bool] = Field(default=None, alias="MultiAZEnabled")
    num_cache_clusters: Optional[int] = Field(default=None, alias="NumCacheClusters")
    preferred_cache_cluster_azs: Optional[Sequence[str]] = Field(
        default=None, alias="PreferredCacheClusterAZs"
    )
    num_node_groups: Optional[int] = Field(default=None, alias="NumNodeGroups")
    replicas_per_node_group: Optional[int] = Field(
        default=None, alias="ReplicasPerNodeGroup"
    )
    node_group_configuration: Optional[Sequence[NodeGroupConfigurationModel]] = Field(
        default=None, alias="NodeGroupConfiguration"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    cache_security_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="CacheSecurityGroupNames"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    snapshot_arns: Optional[Sequence[str]] = Field(default=None, alias="SnapshotArns")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="AtRestEncryptionEnabled"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    user_group_ids: Optional[Sequence[str]] = Field(default=None, alias="UserGroupIds")
    log_delivery_configurations: Optional[
        Sequence[LogDeliveryConfigurationRequestModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    data_tiering_enabled: Optional[bool] = Field(
        default=None, alias="DataTieringEnabled"
    )
    network_type: Optional[Literal["dual_stack", "ipv4", "ipv6"]] = Field(
        default=None, alias="NetworkType"
    )
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class ModifyCacheClusterMessageRequestModel(BaseModel):
    cache_cluster_id: str = Field(alias="CacheClusterId")
    num_cache_nodes: Optional[int] = Field(default=None, alias="NumCacheNodes")
    cache_node_ids_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="CacheNodeIdsToRemove"
    )
    azmode: Optional[Literal["cross-az", "single-az"]] = Field(
        default=None, alias="AZMode"
    )
    new_availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="NewAvailabilityZones"
    )
    cache_security_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="CacheSecurityGroupNames"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    notification_topic_status: Optional[str] = Field(
        default=None, alias="NotificationTopicStatus"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")
    auth_token_update_strategy: Optional[Literal["DELETE", "ROTATE", "SET"]] = Field(
        default=None, alias="AuthTokenUpdateStrategy"
    )
    log_delivery_configurations: Optional[
        Sequence[LogDeliveryConfigurationRequestModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )


class ModifyReplicationGroupMessageRequestModel(BaseModel):
    replication_group_id: str = Field(alias="ReplicationGroupId")
    replication_group_description: Optional[str] = Field(
        default=None, alias="ReplicationGroupDescription"
    )
    primary_cluster_id: Optional[str] = Field(default=None, alias="PrimaryClusterId")
    snapshotting_cluster_id: Optional[str] = Field(
        default=None, alias="SnapshottingClusterId"
    )
    automatic_failover_enabled: Optional[bool] = Field(
        default=None, alias="AutomaticFailoverEnabled"
    )
    multi_azenabled: Optional[bool] = Field(default=None, alias="MultiAZEnabled")
    node_group_id: Optional[str] = Field(default=None, alias="NodeGroupId")
    cache_security_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="CacheSecurityGroupNames"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    cache_parameter_group_name: Optional[str] = Field(
        default=None, alias="CacheParameterGroupName"
    )
    notification_topic_status: Optional[str] = Field(
        default=None, alias="NotificationTopicStatus"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")
    auth_token_update_strategy: Optional[Literal["DELETE", "ROTATE", "SET"]] = Field(
        default=None, alias="AuthTokenUpdateStrategy"
    )
    user_group_ids_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="UserGroupIdsToAdd"
    )
    user_group_ids_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="UserGroupIdsToRemove"
    )
    remove_user_groups: Optional[bool] = Field(default=None, alias="RemoveUserGroups")
    log_delivery_configurations: Optional[
        Sequence[LogDeliveryConfigurationRequestModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class PendingModifiedValuesModel(BaseModel):
    num_cache_nodes: Optional[int] = Field(default=None, alias="NumCacheNodes")
    cache_node_ids_to_remove: Optional[List[str]] = Field(
        default=None, alias="CacheNodeIdsToRemove"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    auth_token_status: Optional[Literal["ROTATING", "SETTING"]] = Field(
        default=None, alias="AuthTokenStatus"
    )
    log_delivery_configurations: Optional[
        List[PendingLogDeliveryConfigurationModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class ReplicationGroupPendingModifiedValuesModel(BaseModel):
    primary_cluster_id: Optional[str] = Field(default=None, alias="PrimaryClusterId")
    automatic_failover_status: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="AutomaticFailoverStatus"
    )
    resharding: Optional[ReshardingStatusModel] = Field(
        default=None, alias="Resharding"
    )
    auth_token_status: Optional[Literal["ROTATING", "SETTING"]] = Field(
        default=None, alias="AuthTokenStatus"
    )
    user_groups: Optional[UserGroupsUpdateStatusModel] = Field(
        default=None, alias="UserGroups"
    )
    log_delivery_configurations: Optional[
        List[PendingLogDeliveryConfigurationModel]
    ] = Field(default=None, alias="LogDeliveryConfigurations")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class UpdateActionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    update_actions: List[UpdateActionModel] = Field(alias="UpdateActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheSubnetGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cache_subnet_groups: List[CacheSubnetGroupModel] = Field(alias="CacheSubnetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCacheSubnetGroupResultModel(BaseModel):
    cache_subnet_group: CacheSubnetGroupModel = Field(alias="CacheSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyCacheSubnetGroupResultModel(BaseModel):
    cache_subnet_group: CacheSubnetGroupModel = Field(alias="CacheSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheClusterModel(BaseModel):
    cache_cluster_id: Optional[str] = Field(default=None, alias="CacheClusterId")
    configuration_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ConfigurationEndpoint"
    )
    client_download_landing_page: Optional[str] = Field(
        default=None, alias="ClientDownloadLandingPage"
    )
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cache_cluster_status: Optional[str] = Field(
        default=None, alias="CacheClusterStatus"
    )
    num_cache_nodes: Optional[int] = Field(default=None, alias="NumCacheNodes")
    preferred_availability_zone: Optional[str] = Field(
        default=None, alias="PreferredAvailabilityZone"
    )
    preferred_outpost_arn: Optional[str] = Field(
        default=None, alias="PreferredOutpostArn"
    )
    cache_cluster_create_time: Optional[datetime] = Field(
        default=None, alias="CacheClusterCreateTime"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    pending_modified_values: Optional[PendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )
    cache_security_groups: Optional[List[CacheSecurityGroupMembershipModel]] = Field(
        default=None, alias="CacheSecurityGroups"
    )
    cache_parameter_group: Optional[CacheParameterGroupStatusModel] = Field(
        default=None, alias="CacheParameterGroup"
    )
    cache_subnet_group_name: Optional[str] = Field(
        default=None, alias="CacheSubnetGroupName"
    )
    cache_nodes: Optional[List[CacheNodeModel]] = Field(
        default=None, alias="CacheNodes"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    security_groups: Optional[List[SecurityGroupMembershipModel]] = Field(
        default=None, alias="SecurityGroups"
    )
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    auth_token_enabled: Optional[bool] = Field(default=None, alias="AuthTokenEnabled")
    auth_token_last_modified_date: Optional[datetime] = Field(
        default=None, alias="AuthTokenLastModifiedDate"
    )
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="AtRestEncryptionEnabled"
    )
    arn: Optional[str] = Field(default=None, alias="ARN")
    replication_group_log_delivery_enabled: Optional[bool] = Field(
        default=None, alias="ReplicationGroupLogDeliveryEnabled"
    )
    log_delivery_configurations: Optional[List[LogDeliveryConfigurationModel]] = Field(
        default=None, alias="LogDeliveryConfigurations"
    )
    network_type: Optional[Literal["dual_stack", "ipv4", "ipv6"]] = Field(
        default=None, alias="NetworkType"
    )
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class ReplicationGroupModel(BaseModel):
    replication_group_id: Optional[str] = Field(
        default=None, alias="ReplicationGroupId"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    global_replication_group_info: Optional[GlobalReplicationGroupInfoModel] = Field(
        default=None, alias="GlobalReplicationGroupInfo"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    pending_modified_values: Optional[
        ReplicationGroupPendingModifiedValuesModel
    ] = Field(default=None, alias="PendingModifiedValues")
    member_clusters: Optional[List[str]] = Field(default=None, alias="MemberClusters")
    node_groups: Optional[List[NodeGroupModel]] = Field(
        default=None, alias="NodeGroups"
    )
    snapshotting_cluster_id: Optional[str] = Field(
        default=None, alias="SnapshottingClusterId"
    )
    automatic_failover: Optional[
        Literal["disabled", "disabling", "enabled", "enabling"]
    ] = Field(default=None, alias="AutomaticFailover")
    multi_az: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="MultiAZ"
    )
    configuration_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ConfigurationEndpoint"
    )
    snapshot_retention_limit: Optional[int] = Field(
        default=None, alias="SnapshotRetentionLimit"
    )
    snapshot_window: Optional[str] = Field(default=None, alias="SnapshotWindow")
    cluster_enabled: Optional[bool] = Field(default=None, alias="ClusterEnabled")
    cache_node_type: Optional[str] = Field(default=None, alias="CacheNodeType")
    auth_token_enabled: Optional[bool] = Field(default=None, alias="AuthTokenEnabled")
    auth_token_last_modified_date: Optional[datetime] = Field(
        default=None, alias="AuthTokenLastModifiedDate"
    )
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="TransitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="AtRestEncryptionEnabled"
    )
    member_clusters_outpost_arns: Optional[List[str]] = Field(
        default=None, alias="MemberClustersOutpostArns"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    arn: Optional[str] = Field(default=None, alias="ARN")
    user_group_ids: Optional[List[str]] = Field(default=None, alias="UserGroupIds")
    log_delivery_configurations: Optional[List[LogDeliveryConfigurationModel]] = Field(
        default=None, alias="LogDeliveryConfigurations"
    )
    replication_group_create_time: Optional[datetime] = Field(
        default=None, alias="ReplicationGroupCreateTime"
    )
    data_tiering: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="DataTiering"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    network_type: Optional[Literal["dual_stack", "ipv4", "ipv6"]] = Field(
        default=None, alias="NetworkType"
    )
    ip_discovery: Optional[Literal["ipv4", "ipv6"]] = Field(
        default=None, alias="IpDiscovery"
    )
    transit_encryption_mode: Optional[Literal["preferred", "required"]] = Field(
        default=None, alias="TransitEncryptionMode"
    )


class CacheClusterMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cache_clusters: List[CacheClusterModel] = Field(alias="CacheClusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCacheClusterResultModel(BaseModel):
    cache_cluster: CacheClusterModel = Field(alias="CacheCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCacheClusterResultModel(BaseModel):
    cache_cluster: CacheClusterModel = Field(alias="CacheCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyCacheClusterResultModel(BaseModel):
    cache_cluster: CacheClusterModel = Field(alias="CacheCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootCacheClusterResultModel(BaseModel):
    cache_cluster: CacheClusterModel = Field(alias="CacheCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompleteMigrationResponseModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReplicationGroupResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecreaseReplicaCountResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteReplicationGroupResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IncreaseReplicaCountResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReplicationGroupResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReplicationGroupShardConfigurationResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_groups: List[ReplicationGroupModel] = Field(alias="ReplicationGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMigrationResponseModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestFailoverResultModel(BaseModel):
    replication_group: ReplicationGroupModel = Field(alias="ReplicationGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
