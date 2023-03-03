# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddRoleToDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class AddSourceIdentifierToSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    source_identifier: str = Field(alias="SourceIdentifier")


class EventSubscriptionModel(BaseModel):
    customer_aws_id: Optional[str] = Field(default=None, alias="CustomerAwsId")
    cust_subscription_id: Optional[str] = Field(
        default=None, alias="CustSubscriptionId"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    status: Optional[str] = Field(default=None, alias="Status")
    subscription_creation_time: Optional[str] = Field(
        default=None, alias="SubscriptionCreationTime"
    )
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_ids_list: Optional[List[str]] = Field(default=None, alias="SourceIdsList")
    event_categories_list: Optional[List[str]] = Field(
        default=None, alias="EventCategoriesList"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    event_subscription_arn: Optional[str] = Field(
        default=None, alias="EventSubscriptionArn"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ApplyPendingMaintenanceActionMessageRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    apply_action: str = Field(alias="ApplyAction")
    opt_in_type: str = Field(alias="OptInType")


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class CharacterSetModel(BaseModel):
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    character_set_description: Optional[str] = Field(
        default=None, alias="CharacterSetDescription"
    )


class CloudwatchLogsExportConfigurationModel(BaseModel):
    enable_log_types: Optional[Sequence[str]] = Field(
        default=None, alias="EnableLogTypes"
    )
    disable_log_types: Optional[Sequence[str]] = Field(
        default=None, alias="DisableLogTypes"
    )


class DBClusterParameterGroupModel(BaseModel):
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    dbcluster_parameter_group_arn: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupArn"
    )


class DBClusterSnapshotModel(BaseModel):
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    dbcluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotIdentifier"
    )
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="SnapshotCreateTime"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    cluster_create_time: Optional[datetime] = Field(
        default=None, alias="ClusterCreateTime"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    percent_progress: Optional[int] = Field(default=None, alias="PercentProgress")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    dbcluster_snapshot_arn: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotArn"
    )
    source_dbcluster_snapshot_arn: Optional[str] = Field(
        default=None, alias="SourceDBClusterSnapshotArn"
    )
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )


class DBParameterGroupModel(BaseModel):
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    dbparameter_group_arn: Optional[str] = Field(
        default=None, alias="DBParameterGroupArn"
    )


class ServerlessV2ScalingConfigurationModel(BaseModel):
    min_capacity: Optional[float] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")


class CreateGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")
    source_dbcluster_identifier: Optional[str] = Field(
        default=None, alias="SourceDBClusterIdentifier"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")


class DBClusterEndpointModel(BaseModel):
    dbcluster_endpoint_identifier: Optional[str] = Field(
        default=None, alias="DBClusterEndpointIdentifier"
    )
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_endpoint_resource_identifier: Optional[str] = Field(
        default=None, alias="DBClusterEndpointResourceIdentifier"
    )
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    status: Optional[str] = Field(default=None, alias="Status")
    endpoint_type: Optional[str] = Field(default=None, alias="EndpointType")
    custom_endpoint_type: Optional[str] = Field(
        default=None, alias="CustomEndpointType"
    )
    static_members: Optional[List[str]] = Field(default=None, alias="StaticMembers")
    excluded_members: Optional[List[str]] = Field(default=None, alias="ExcludedMembers")
    dbcluster_endpoint_arn: Optional[str] = Field(
        default=None, alias="DBClusterEndpointArn"
    )


class DBClusterMemberModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    is_cluster_writer: Optional[bool] = Field(default=None, alias="IsClusterWriter")
    dbcluster_parameter_group_status: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupStatus"
    )
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")


class DBClusterOptionGroupStatusModel(BaseModel):
    dbcluster_option_group_name: Optional[str] = Field(
        default=None, alias="DBClusterOptionGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class ParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    description: Optional[str] = Field(default=None, alias="Description")
    source: Optional[str] = Field(default=None, alias="Source")
    apply_type: Optional[str] = Field(default=None, alias="ApplyType")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )
    apply_method: Optional[Literal["immediate", "pending-reboot"]] = Field(
        default=None, alias="ApplyMethod"
    )


class DBClusterRoleModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    status: Optional[str] = Field(default=None, alias="Status")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class DBClusterSnapshotAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_values: Optional[List[str]] = Field(default=None, alias="AttributeValues")


class ServerlessV2ScalingConfigurationInfoModel(BaseModel):
    min_capacity: Optional[float] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")


class VpcSecurityGroupMembershipModel(BaseModel):
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="VpcSecurityGroupId"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class TimezoneModel(BaseModel):
    timezone_name: Optional[str] = Field(default=None, alias="TimezoneName")


class UpgradeTargetModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    auto_upgrade: Optional[bool] = Field(default=None, alias="AutoUpgrade")
    is_major_version_upgrade: Optional[bool] = Field(
        default=None, alias="IsMajorVersionUpgrade"
    )
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )


class DBInstanceStatusInfoModel(BaseModel):
    status_type: Optional[str] = Field(default=None, alias="StatusType")
    normal: Optional[bool] = Field(default=None, alias="Normal")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")


class DBParameterGroupStatusModel(BaseModel):
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )


class DBSecurityGroupMembershipModel(BaseModel):
    dbsecurity_group_name: Optional[str] = Field(
        default=None, alias="DBSecurityGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class DomainMembershipModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    status: Optional[str] = Field(default=None, alias="Status")
    fqdn: Optional[str] = Field(default=None, alias="FQDN")
    iamrole_name: Optional[str] = Field(default=None, alias="IAMRoleName")


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")


class OptionGroupMembershipModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    status: Optional[str] = Field(default=None, alias="Status")


class DeleteDBClusterEndpointMessageRequestModel(BaseModel):
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")


class DeleteDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    skip_final_snapshot: Optional[bool] = Field(default=None, alias="SkipFinalSnapshot")
    final_dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalDBSnapshotIdentifier"
    )


class DeleteDBClusterParameterGroupMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")


class DeleteDBClusterSnapshotMessageRequestModel(BaseModel):
    dbcluster_snapshot_identifier: str = Field(alias="DBClusterSnapshotIdentifier")


class DeleteDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    skip_final_snapshot: Optional[bool] = Field(default=None, alias="SkipFinalSnapshot")
    final_dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalDBSnapshotIdentifier"
    )


class DeleteDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")


class DeleteDBSubnetGroupMessageRequestModel(BaseModel):
    dbsubnet_group_name: str = Field(alias="DBSubnetGroupName")


class DeleteEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")


class DeleteGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeDBClusterSnapshotAttributesMessageRequestModel(BaseModel):
    dbcluster_snapshot_identifier: str = Field(alias="DBClusterSnapshotIdentifier")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeGlobalClustersMessageRequestModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeValidDBInstanceModificationsMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")


class DoubleRangeModel(BaseModel):
    from_: Optional[float] = Field(default=None, alias="From")
    to: Optional[float] = Field(default=None, alias="To")


class EventCategoriesMapModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")


class EventModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
        ]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")
    date: Optional[datetime] = Field(default=None, alias="Date")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")


class FailoverDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    target_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="TargetDBInstanceIdentifier"
    )


class FailoverGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")
    target_db_cluster_identifier: str = Field(alias="TargetDbClusterIdentifier")


class GlobalClusterMemberModel(BaseModel):
    dbcluster_arn: Optional[str] = Field(default=None, alias="DBClusterArn")
    readers: Optional[List[str]] = Field(default=None, alias="Readers")
    is_writer: Optional[bool] = Field(default=None, alias="IsWriter")


class ModifyDBClusterEndpointMessageRequestModel(BaseModel):
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")
    endpoint_type: Optional[str] = Field(default=None, alias="EndpointType")
    static_members: Optional[Sequence[str]] = Field(default=None, alias="StaticMembers")
    excluded_members: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedMembers"
    )


class ModifyDBClusterSnapshotAttributeMessageRequestModel(BaseModel):
    dbcluster_snapshot_identifier: str = Field(alias="DBClusterSnapshotIdentifier")
    attribute_name: str = Field(alias="AttributeName")
    values_to_add: Optional[Sequence[str]] = Field(default=None, alias="ValuesToAdd")
    values_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="ValuesToRemove"
    )


class ModifyDBSubnetGroupMessageRequestModel(BaseModel):
    dbsubnet_group_name: str = Field(alias="DBSubnetGroupName")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    dbsubnet_group_description: Optional[str] = Field(
        default=None, alias="DBSubnetGroupDescription"
    )


class ModifyEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ModifyGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")
    new_global_cluster_identifier: Optional[str] = Field(
        default=None, alias="NewGlobalClusterIdentifier"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    allow_major_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowMajorVersionUpgrade"
    )


class PendingCloudwatchLogsExportsModel(BaseModel):
    log_types_to_enable: Optional[List[str]] = Field(
        default=None, alias="LogTypesToEnable"
    )
    log_types_to_disable: Optional[List[str]] = Field(
        default=None, alias="LogTypesToDisable"
    )


class PendingMaintenanceActionModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="Action")
    auto_applied_after_date: Optional[datetime] = Field(
        default=None, alias="AutoAppliedAfterDate"
    )
    forced_apply_date: Optional[datetime] = Field(default=None, alias="ForcedApplyDate")
    opt_in_status: Optional[str] = Field(default=None, alias="OptInStatus")
    current_apply_date: Optional[datetime] = Field(
        default=None, alias="CurrentApplyDate"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class PromoteReadReplicaDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class RangeModel(BaseModel):
    from_: Optional[int] = Field(default=None, alias="From")
    to: Optional[int] = Field(default=None, alias="To")
    step: Optional[int] = Field(default=None, alias="Step")


class RebootDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    force_failover: Optional[bool] = Field(default=None, alias="ForceFailover")


class RemoveFromGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")
    db_cluster_identifier: str = Field(alias="DbClusterIdentifier")


class RemoveRoleFromDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class RemoveSourceIdentifierFromSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    source_identifier: str = Field(alias="SourceIdentifier")


class RemoveTagsFromResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class StartDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class StopDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class AddSourceIdentifierToSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBClusterEndpointOutputModel(BaseModel):
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    dbcluster_endpoint_resource_identifier: str = Field(
        alias="DBClusterEndpointResourceIdentifier"
    )
    endpoint: str = Field(alias="Endpoint")
    status: str = Field(alias="Status")
    endpoint_type: str = Field(alias="EndpointType")
    custom_endpoint_type: str = Field(alias="CustomEndpointType")
    static_members: List[str] = Field(alias="StaticMembers")
    excluded_members: List[str] = Field(alias="ExcludedMembers")
    dbcluster_endpoint_arn: str = Field(alias="DBClusterEndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterParameterGroupNameMessageModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBParameterGroupNameMessageModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBClusterEndpointOutputModel(BaseModel):
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    dbcluster_endpoint_resource_identifier: str = Field(
        alias="DBClusterEndpointResourceIdentifier"
    )
    endpoint: str = Field(alias="Endpoint")
    status: str = Field(alias="Status")
    endpoint_type: str = Field(alias="EndpointType")
    custom_endpoint_type: str = Field(alias="CustomEndpointType")
    static_members: List[str] = Field(alias="StaticMembers")
    excluded_members: List[str] = Field(alias="ExcludedMembers")
    dbcluster_endpoint_arn: str = Field(alias="DBClusterEndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventSubscriptionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    event_subscriptions_list: List[EventSubscriptionModel] = Field(
        alias="EventSubscriptionsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBClusterEndpointOutputModel(BaseModel):
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    dbcluster_endpoint_resource_identifier: str = Field(
        alias="DBClusterEndpointResourceIdentifier"
    )
    endpoint: str = Field(alias="Endpoint")
    status: str = Field(alias="Status")
    endpoint_type: str = Field(alias="EndpointType")
    custom_endpoint_type: str = Field(alias="CustomEndpointType")
    static_members: List[str] = Field(alias="StaticMembers")
    excluded_members: List[str] = Field(alias="ExcludedMembers")
    dbcluster_endpoint_arn: str = Field(alias="DBClusterEndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyEventSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveSourceIdentifierFromSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsToResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CopyDBClusterParameterGroupMessageRequestModel(BaseModel):
    source_dbcluster_parameter_group_identifier: str = Field(
        alias="SourceDBClusterParameterGroupIdentifier"
    )
    target_dbcluster_parameter_group_identifier: str = Field(
        alias="TargetDBClusterParameterGroupIdentifier"
    )
    target_dbcluster_parameter_group_description: str = Field(
        alias="TargetDBClusterParameterGroupDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CopyDBClusterSnapshotMessageRequestModel(BaseModel):
    source_dbcluster_snapshot_identifier: str = Field(
        alias="SourceDBClusterSnapshotIdentifier"
    )
    target_dbcluster_snapshot_identifier: str = Field(
        alias="TargetDBClusterSnapshotIdentifier"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    copy_tags: Optional[bool] = Field(default=None, alias="CopyTags")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")


class CopyDBParameterGroupMessageRequestModel(BaseModel):
    source_dbparameter_group_identifier: str = Field(
        alias="SourceDBParameterGroupIdentifier"
    )
    target_dbparameter_group_identifier: str = Field(
        alias="TargetDBParameterGroupIdentifier"
    )
    target_dbparameter_group_description: str = Field(
        alias="TargetDBParameterGroupDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBClusterEndpointMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    dbcluster_endpoint_identifier: str = Field(alias="DBClusterEndpointIdentifier")
    endpoint_type: str = Field(alias="EndpointType")
    static_members: Optional[Sequence[str]] = Field(default=None, alias="StaticMembers")
    excluded_members: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedMembers"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBClusterParameterGroupMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBClusterSnapshotMessageRequestModel(BaseModel):
    dbcluster_snapshot_identifier: str = Field(alias="DBClusterSnapshotIdentifier")
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    dbinstance_class: str = Field(alias="DBInstanceClass")
    engine: str = Field(alias="Engine")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    dbsecurity_groups: Optional[Sequence[str]] = Field(
        default=None, alias="DBSecurityGroups"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    tde_credential_password: Optional[str] = Field(
        default=None, alias="TdeCredentialPassword"
    )
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    domain: Optional[str] = Field(default=None, alias="Domain")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )


class CreateDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBSubnetGroupMessageRequestModel(BaseModel):
    dbsubnet_group_name: str = Field(alias="DBSubnetGroupName")
    dbsubnet_group_description: str = Field(alias="DBSubnetGroupDescription")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    source_ids: Optional[Sequence[str]] = Field(default=None, alias="SourceIds")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagListMessageModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrderableDBInstanceOptionModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    availability_zones: Optional[List[AvailabilityZoneModel]] = Field(
        default=None, alias="AvailabilityZones"
    )
    multi_azcapable: Optional[bool] = Field(default=None, alias="MultiAZCapable")
    read_replica_capable: Optional[bool] = Field(
        default=None, alias="ReadReplicaCapable"
    )
    vpc: Optional[bool] = Field(default=None, alias="Vpc")
    supports_storage_encryption: Optional[bool] = Field(
        default=None, alias="SupportsStorageEncryption"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    supports_iops: Optional[bool] = Field(default=None, alias="SupportsIops")
    supports_enhanced_monitoring: Optional[bool] = Field(
        default=None, alias="SupportsEnhancedMonitoring"
    )
    supports_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="SupportsIAMDatabaseAuthentication"
    )
    supports_performance_insights: Optional[bool] = Field(
        default=None, alias="SupportsPerformanceInsights"
    )
    min_storage_size: Optional[int] = Field(default=None, alias="MinStorageSize")
    max_storage_size: Optional[int] = Field(default=None, alias="MaxStorageSize")
    min_iops_per_db_instance: Optional[int] = Field(
        default=None, alias="MinIopsPerDbInstance"
    )
    max_iops_per_db_instance: Optional[int] = Field(
        default=None, alias="MaxIopsPerDbInstance"
    )
    min_iops_per_gib: Optional[float] = Field(default=None, alias="MinIopsPerGib")
    max_iops_per_gib: Optional[float] = Field(default=None, alias="MaxIopsPerGib")
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_status: Optional[str] = Field(default=None, alias="SubnetStatus")


class ModifyDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    dbsecurity_groups: Optional[Sequence[str]] = Field(
        default=None, alias="DBSecurityGroups"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    allow_major_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowMajorVersionUpgrade"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    new_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="NewDBInstanceIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    tde_credential_password: Optional[str] = Field(
        default=None, alias="TdeCredentialPassword"
    )
    cacertificate_identifier: Optional[str] = Field(
        default=None, alias="CACertificateIdentifier"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    dbport_number: Optional[int] = Field(default=None, alias="DBPortNumber")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    cloudwatch_logs_export_configuration: Optional[
        CloudwatchLogsExportConfigurationModel
    ] = Field(default=None, alias="CloudwatchLogsExportConfiguration")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )


class CopyDBClusterParameterGroupResultModel(BaseModel):
    dbcluster_parameter_group: DBClusterParameterGroupModel = Field(
        alias="DBClusterParameterGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBClusterParameterGroupResultModel(BaseModel):
    dbcluster_parameter_group: DBClusterParameterGroupModel = Field(
        alias="DBClusterParameterGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterParameterGroupsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbcluster_parameter_groups: List[DBClusterParameterGroupModel] = Field(
        alias="DBClusterParameterGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyDBClusterSnapshotResultModel(BaseModel):
    dbcluster_snapshot: DBClusterSnapshotModel = Field(alias="DBClusterSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBClusterSnapshotResultModel(BaseModel):
    dbcluster_snapshot: DBClusterSnapshotModel = Field(alias="DBClusterSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterSnapshotMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbcluster_snapshots: List[DBClusterSnapshotModel] = Field(
        alias="DBClusterSnapshots"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBClusterSnapshotResultModel(BaseModel):
    dbcluster_snapshot: DBClusterSnapshotModel = Field(alias="DBClusterSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyDBParameterGroupResultModel(BaseModel):
    dbparameter_group: DBParameterGroupModel = Field(alias="DBParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBParameterGroupResultModel(BaseModel):
    dbparameter_group: DBParameterGroupModel = Field(alias="DBParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBParameterGroupsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbparameter_groups: List[DBParameterGroupModel] = Field(alias="DBParameterGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    engine: str = Field(alias="Engine")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    port: Optional[int] = Field(default=None, alias="Port")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    replication_source_identifier: Optional[str] = Field(
        default=None, alias="ReplicationSourceIdentifier"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")


class ModifyDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    new_dbcluster_identifier: Optional[str] = Field(
        default=None, alias="NewDBClusterIdentifier"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    cloudwatch_logs_export_configuration: Optional[
        CloudwatchLogsExportConfigurationModel
    ] = Field(default=None, alias="CloudwatchLogsExportConfiguration")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    allow_major_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowMajorVersionUpgrade"
    )
    dbinstance_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBInstanceParameterGroupName"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")


class RestoreDBClusterFromSnapshotMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    engine: str = Field(alias="Engine")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    port: Optional[int] = Field(default=None, alias="Port")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")


class RestoreDBClusterToPointInTimeMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    source_dbcluster_identifier: str = Field(alias="SourceDBClusterIdentifier")
    restore_type: Optional[str] = Field(default=None, alias="RestoreType")
    restore_to_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="RestoreToTime"
    )
    use_latest_restorable_time: Optional[bool] = Field(
        default=None, alias="UseLatestRestorableTime"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")


class DBClusterEndpointMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbcluster_endpoints: List[DBClusterEndpointModel] = Field(
        alias="DBClusterEndpoints"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterParameterGroupDetailsModel(BaseModel):
    parameters: List[ParameterModel] = Field(alias="Parameters")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBParameterGroupDetailsModel(BaseModel):
    parameters: List[ParameterModel] = Field(alias="Parameters")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EngineDefaultsModel(BaseModel):
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    parameters: Optional[List[ParameterModel]] = Field(default=None, alias="Parameters")


class ModifyDBClusterParameterGroupMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    parameters: Sequence[ParameterModel] = Field(alias="Parameters")


class ModifyDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    parameters: Sequence[ParameterModel] = Field(alias="Parameters")


class ResetDBClusterParameterGroupMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    reset_all_parameters: Optional[bool] = Field(
        default=None, alias="ResetAllParameters"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class ResetDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    reset_all_parameters: Optional[bool] = Field(
        default=None, alias="ResetAllParameters"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class DBClusterSnapshotAttributesResultModel(BaseModel):
    dbcluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotIdentifier"
    )
    dbcluster_snapshot_attributes: Optional[
        List[DBClusterSnapshotAttributeModel]
    ] = Field(default=None, alias="DBClusterSnapshotAttributes")


class DBClusterModel(BaseModel):
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_parameter_group: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroup"
    )
    dbsubnet_group: Optional[str] = Field(default=None, alias="DBSubnetGroup")
    status: Optional[str] = Field(default=None, alias="Status")
    percent_progress: Optional[str] = Field(default=None, alias="PercentProgress")
    earliest_restorable_time: Optional[datetime] = Field(
        default=None, alias="EarliestRestorableTime"
    )
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    reader_endpoint: Optional[str] = Field(default=None, alias="ReaderEndpoint")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    latest_restorable_time: Optional[datetime] = Field(
        default=None, alias="LatestRestorableTime"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    dbcluster_option_group_memberships: Optional[
        List[DBClusterOptionGroupStatusModel]
    ] = Field(default=None, alias="DBClusterOptionGroupMemberships")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    replication_source_identifier: Optional[str] = Field(
        default=None, alias="ReplicationSourceIdentifier"
    )
    read_replica_identifiers: Optional[List[str]] = Field(
        default=None, alias="ReadReplicaIdentifiers"
    )
    dbcluster_members: Optional[List[DBClusterMemberModel]] = Field(
        default=None, alias="DBClusterMembers"
    )
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="VpcSecurityGroups"
    )
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    db_cluster_resource_id: Optional[str] = Field(
        default=None, alias="DbClusterResourceId"
    )
    dbcluster_arn: Optional[str] = Field(default=None, alias="DBClusterArn")
    associated_roles: Optional[List[DBClusterRoleModel]] = Field(
        default=None, alias="AssociatedRoles"
    )
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    clone_group_id: Optional[str] = Field(default=None, alias="CloneGroupId")
    cluster_create_time: Optional[datetime] = Field(
        default=None, alias="ClusterCreateTime"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    enabled_cloudwatch_logs_exports: Optional[List[str]] = Field(
        default=None, alias="EnabledCloudwatchLogsExports"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    cross_account_clone: Optional[bool] = Field(default=None, alias="CrossAccountClone")
    automatic_restart_time: Optional[datetime] = Field(
        default=None, alias="AutomaticRestartTime"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationInfoModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")


class DBEngineVersionModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    dbengine_description: Optional[str] = Field(
        default=None, alias="DBEngineDescription"
    )
    dbengine_version_description: Optional[str] = Field(
        default=None, alias="DBEngineVersionDescription"
    )
    default_character_set: Optional[CharacterSetModel] = Field(
        default=None, alias="DefaultCharacterSet"
    )
    supported_character_sets: Optional[List[CharacterSetModel]] = Field(
        default=None, alias="SupportedCharacterSets"
    )
    valid_upgrade_target: Optional[List[UpgradeTargetModel]] = Field(
        default=None, alias="ValidUpgradeTarget"
    )
    supported_timezones: Optional[List[TimezoneModel]] = Field(
        default=None, alias="SupportedTimezones"
    )
    exportable_log_types: Optional[List[str]] = Field(
        default=None, alias="ExportableLogTypes"
    )
    supports_log_exports_to_cloudwatch_logs: Optional[bool] = Field(
        default=None, alias="SupportsLogExportsToCloudwatchLogs"
    )
    supports_read_replica: Optional[bool] = Field(
        default=None, alias="SupportsReadReplica"
    )
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )


class DescribeDBClusterEndpointsMessageRequestModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_endpoint_identifier: Optional[str] = Field(
        default=None, alias="DBClusterEndpointIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBClusterParameterGroupsMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBClusterParametersMessageRequestModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBClusterSnapshotsMessageRequestModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")


class DescribeDBClustersMessageRequestModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBEngineVersionsMessageRequestModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")
    list_supported_character_sets: Optional[bool] = Field(
        default=None, alias="ListSupportedCharacterSets"
    )
    list_supported_timezones: Optional[bool] = Field(
        default=None, alias="ListSupportedTimezones"
    )


class DescribeDBInstancesMessageRequestModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBParameterGroupsMessageRequestModel(BaseModel):
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBParametersMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBSubnetGroupsMessageRequestModel(BaseModel):
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEngineDefaultClusterParametersMessageRequestModel(BaseModel):
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEngineDefaultParametersMessageRequestModel(BaseModel):
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventCategoriesMessageRequestModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeEventSubscriptionsMessageRequestModel(BaseModel):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventsMessageRequestModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeOrderableDBInstanceOptionsMessageRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    vpc: Optional[bool] = Field(default=None, alias="Vpc")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribePendingMaintenanceActionsMessageRequestModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class ListTagsForResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateModel(
    BaseModel
):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_endpoint_identifier: Optional[str] = Field(
        default=None, alias="DBClusterEndpointIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateModel(
    BaseModel
):
    dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="DBClusterParameterGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateModel(
    BaseModel
):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateModel(
    BaseModel
):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbcluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClustersMessageDescribeDBClustersPaginateModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbparameter_group_family: Optional[str] = Field(
        default=None, alias="DBParameterGroupFamily"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    default_only: Optional[bool] = Field(default=None, alias="DefaultOnly")
    list_supported_character_sets: Optional[bool] = Field(
        default=None, alias="ListSupportedCharacterSets"
    )
    list_supported_timezones: Optional[bool] = Field(
        default=None, alias="ListSupportedTimezones"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBInstancesMessageDescribeDBInstancesPaginateModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateModel(BaseModel):
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBParametersMessageDescribeDBParametersPaginateModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateModel(BaseModel):
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateModel(
    BaseModel
):
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateModel(
    BaseModel
):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsMessageDescribeEventsPaginateModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateModel(
    BaseModel
):
    engine: str = Field(alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    vpc: Optional[bool] = Field(default=None, alias="Vpc")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateModel(
    BaseModel
):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBInstancesMessageDBInstanceAvailableWaitModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBInstancesMessageDBInstanceDeletedWaitModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class EventCategoriesMessageModel(BaseModel):
    event_categories_map_list: List[EventCategoriesMapModel] = Field(
        alias="EventCategoriesMapList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlobalClusterModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    global_cluster_resource_id: Optional[str] = Field(
        default=None, alias="GlobalClusterResourceId"
    )
    global_cluster_arn: Optional[str] = Field(default=None, alias="GlobalClusterArn")
    status: Optional[str] = Field(default=None, alias="Status")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    global_cluster_members: Optional[List[GlobalClusterMemberModel]] = Field(
        default=None, alias="GlobalClusterMembers"
    )


class PendingModifiedValuesModel(BaseModel):
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    cacertificate_identifier: Optional[str] = Field(
        default=None, alias="CACertificateIdentifier"
    )
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    pending_cloudwatch_logs_exports: Optional[
        PendingCloudwatchLogsExportsModel
    ] = Field(default=None, alias="PendingCloudwatchLogsExports")


class ResourcePendingMaintenanceActionsModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    pending_maintenance_action_details: Optional[
        List[PendingMaintenanceActionModel]
    ] = Field(default=None, alias="PendingMaintenanceActionDetails")


class ValidStorageOptionsModel(BaseModel):
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    storage_size: Optional[List[RangeModel]] = Field(default=None, alias="StorageSize")
    provisioned_iops: Optional[List[RangeModel]] = Field(
        default=None, alias="ProvisionedIops"
    )
    iops_to_storage_ratio: Optional[List[DoubleRangeModel]] = Field(
        default=None, alias="IopsToStorageRatio"
    )


class OrderableDBInstanceOptionsMessageModel(BaseModel):
    orderable_dbinstance_options: List[OrderableDBInstanceOptionModel] = Field(
        alias="OrderableDBInstanceOptions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBSubnetGroupModel(BaseModel):
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    dbsubnet_group_description: Optional[str] = Field(
        default=None, alias="DBSubnetGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_group_status: Optional[str] = Field(default=None, alias="SubnetGroupStatus")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    dbsubnet_group_arn: Optional[str] = Field(default=None, alias="DBSubnetGroupArn")


class DescribeEngineDefaultClusterParametersResultModel(BaseModel):
    engine_defaults: EngineDefaultsModel = Field(alias="EngineDefaults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEngineDefaultParametersResultModel(BaseModel):
    engine_defaults: EngineDefaultsModel = Field(alias="EngineDefaults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDBClusterSnapshotAttributesResultModel(BaseModel):
    dbcluster_snapshot_attributes_result: DBClusterSnapshotAttributesResultModel = (
        Field(alias="DBClusterSnapshotAttributesResult")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBClusterSnapshotAttributeResultModel(BaseModel):
    dbcluster_snapshot_attributes_result: DBClusterSnapshotAttributesResultModel = (
        Field(alias="DBClusterSnapshotAttributesResult")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbclusters: List[DBClusterModel] = Field(alias="DBClusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailoverDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PromoteReadReplicaDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBClusterFromSnapshotResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBClusterToPointInTimeResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBEngineVersionMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbengine_versions: List[DBEngineVersionModel] = Field(alias="DBEngineVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGlobalClusterResultModel(BaseModel):
    global_cluster: GlobalClusterModel = Field(alias="GlobalCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGlobalClusterResultModel(BaseModel):
    global_cluster: GlobalClusterModel = Field(alias="GlobalCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailoverGlobalClusterResultModel(BaseModel):
    global_cluster: GlobalClusterModel = Field(alias="GlobalCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlobalClustersMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    global_clusters: List[GlobalClusterModel] = Field(alias="GlobalClusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyGlobalClusterResultModel(BaseModel):
    global_cluster: GlobalClusterModel = Field(alias="GlobalCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveFromGlobalClusterResultModel(BaseModel):
    global_cluster: GlobalClusterModel = Field(alias="GlobalCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplyPendingMaintenanceActionResultModel(BaseModel):
    resource_pending_maintenance_actions: ResourcePendingMaintenanceActionsModel = (
        Field(alias="ResourcePendingMaintenanceActions")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PendingMaintenanceActionsMessageModel(BaseModel):
    pending_maintenance_actions: List[ResourcePendingMaintenanceActionsModel] = Field(
        alias="PendingMaintenanceActions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidDBInstanceModificationsMessageModel(BaseModel):
    storage: Optional[List[ValidStorageOptionsModel]] = Field(
        default=None, alias="Storage"
    )


class CreateDBSubnetGroupResultModel(BaseModel):
    dbsubnet_group: DBSubnetGroupModel = Field(alias="DBSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBInstanceModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    engine: Optional[str] = Field(default=None, alias="Engine")
    dbinstance_status: Optional[str] = Field(default=None, alias="DBInstanceStatus")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    instance_create_time: Optional[datetime] = Field(
        default=None, alias="InstanceCreateTime"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    dbsecurity_groups: Optional[List[DBSecurityGroupMembershipModel]] = Field(
        default=None, alias="DBSecurityGroups"
    )
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="VpcSecurityGroups"
    )
    dbparameter_groups: Optional[List[DBParameterGroupStatusModel]] = Field(
        default=None, alias="DBParameterGroups"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    dbsubnet_group: Optional[DBSubnetGroupModel] = Field(
        default=None, alias="DBSubnetGroup"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    pending_modified_values: Optional[PendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    latest_restorable_time: Optional[datetime] = Field(
        default=None, alias="LatestRestorableTime"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    read_replica_source_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="ReadReplicaSourceDBInstanceIdentifier"
    )
    read_replica_dbinstance_identifiers: Optional[List[str]] = Field(
        default=None, alias="ReadReplicaDBInstanceIdentifiers"
    )
    read_replica_dbcluster_identifiers: Optional[List[str]] = Field(
        default=None, alias="ReadReplicaDBClusterIdentifiers"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_memberships: Optional[List[OptionGroupMembershipModel]] = Field(
        default=None, alias="OptionGroupMemberships"
    )
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    secondary_availability_zone: Optional[str] = Field(
        default=None, alias="SecondaryAvailabilityZone"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    status_infos: Optional[List[DBInstanceStatusInfoModel]] = Field(
        default=None, alias="StatusInfos"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    db_instance_port: Optional[int] = Field(default=None, alias="DbInstancePort")
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    cacertificate_identifier: Optional[str] = Field(
        default=None, alias="CACertificateIdentifier"
    )
    domain_memberships: Optional[List[DomainMembershipModel]] = Field(
        default=None, alias="DomainMemberships"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    enhanced_monitoring_resource_arn: Optional[str] = Field(
        default=None, alias="EnhancedMonitoringResourceArn"
    )
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")
    dbinstance_arn: Optional[str] = Field(default=None, alias="DBInstanceArn")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    performance_insights_enabled: Optional[bool] = Field(
        default=None, alias="PerformanceInsightsEnabled"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    enabled_cloudwatch_logs_exports: Optional[List[str]] = Field(
        default=None, alias="EnabledCloudwatchLogsExports"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )


class DBSubnetGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbsubnet_groups: List[DBSubnetGroupModel] = Field(alias="DBSubnetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBSubnetGroupResultModel(BaseModel):
    dbsubnet_group: DBSubnetGroupModel = Field(alias="DBSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeValidDBInstanceModificationsResultModel(BaseModel):
    valid_dbinstance_modifications_message: ValidDBInstanceModificationsMessageModel = (
        Field(alias="ValidDBInstanceModificationsMessage")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBInstanceMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbinstances: List[DBInstanceModel] = Field(alias="DBInstances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
