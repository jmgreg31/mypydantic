# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountQuotaModel(BaseModel):
    account_quota_name: Optional[str] = Field(default=None, alias="AccountQuotaName")
    used: Optional[int] = Field(default=None, alias="Used")
    max: Optional[int] = Field(default=None, alias="Max")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddRoleToDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class AddRoleToDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: str = Field(alias="FeatureName")


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


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ApplyPendingMaintenanceActionMessageRequestModel(BaseModel):
    resource_identifier: str = Field(alias="ResourceIdentifier")
    apply_action: str = Field(alias="ApplyAction")
    opt_in_type: str = Field(alias="OptInType")


class AuthorizeDBSecurityGroupIngressMessageRequestModel(BaseModel):
    dbsecurity_group_name: str = Field(alias="DBSecurityGroupName")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupId"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class AvailableProcessorFeatureModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")


class BacktrackDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    backtrack_to: Union[datetime, str] = Field(alias="BacktrackTo")
    force: Optional[bool] = Field(default=None, alias="Force")
    use_earliest_time_on_point_in_time_unavailable: Optional[bool] = Field(
        default=None, alias="UseEarliestTimeOnPointInTimeUnavailable"
    )


class BlueGreenDeploymentTaskModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")


class SwitchoverDetailModel(BaseModel):
    source_member: Optional[str] = Field(default=None, alias="SourceMember")
    target_member: Optional[str] = Field(default=None, alias="TargetMember")
    status: Optional[str] = Field(default=None, alias="Status")


class CancelExportTaskMessageRequestModel(BaseModel):
    export_task_identifier: str = Field(alias="ExportTaskIdentifier")


class CertificateDetailsModel(BaseModel):
    caidentifier: Optional[str] = Field(default=None, alias="CAIdentifier")
    valid_till: Optional[datetime] = Field(default=None, alias="ValidTill")


class CertificateModel(BaseModel):
    certificate_identifier: Optional[str] = Field(
        default=None, alias="CertificateIdentifier"
    )
    certificate_type: Optional[str] = Field(default=None, alias="CertificateType")
    thumbprint: Optional[str] = Field(default=None, alias="Thumbprint")
    valid_from: Optional[datetime] = Field(default=None, alias="ValidFrom")
    valid_till: Optional[datetime] = Field(default=None, alias="ValidTill")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    customer_override: Optional[bool] = Field(default=None, alias="CustomerOverride")
    customer_override_valid_till: Optional[datetime] = Field(
        default=None, alias="CustomerOverrideValidTill"
    )


class CharacterSetModel(BaseModel):
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    character_set_description: Optional[str] = Field(
        default=None, alias="CharacterSetDescription"
    )


class ClientGenerateDbAuthTokenRequestModel(BaseModel):
    dbhostname: str = Field(alias="DBHostname")
    port: int = Field(alias="Port")
    dbusername: str = Field(alias="DBUsername")
    region: Optional[str] = Field(default=None, alias="Region")


class CloudwatchLogsExportConfigurationModel(BaseModel):
    enable_log_types: Optional[Sequence[str]] = Field(
        default=None, alias="EnableLogTypes"
    )
    disable_log_types: Optional[Sequence[str]] = Field(
        default=None, alias="DisableLogTypes"
    )


class PendingCloudwatchLogsExportsModel(BaseModel):
    log_types_to_enable: Optional[List[str]] = Field(
        default=None, alias="LogTypesToEnable"
    )
    log_types_to_disable: Optional[List[str]] = Field(
        default=None, alias="LogTypesToDisable"
    )


class ConnectionPoolConfigurationInfoModel(BaseModel):
    max_connections_percent: Optional[int] = Field(
        default=None, alias="MaxConnectionsPercent"
    )
    max_idle_connections_percent: Optional[int] = Field(
        default=None, alias="MaxIdleConnectionsPercent"
    )
    connection_borrow_timeout: Optional[int] = Field(
        default=None, alias="ConnectionBorrowTimeout"
    )
    session_pinning_filters: Optional[List[str]] = Field(
        default=None, alias="SessionPinningFilters"
    )
    init_query: Optional[str] = Field(default=None, alias="InitQuery")


class ConnectionPoolConfigurationModel(BaseModel):
    max_connections_percent: Optional[int] = Field(
        default=None, alias="MaxConnectionsPercent"
    )
    max_idle_connections_percent: Optional[int] = Field(
        default=None, alias="MaxIdleConnectionsPercent"
    )
    connection_borrow_timeout: Optional[int] = Field(
        default=None, alias="ConnectionBorrowTimeout"
    )
    session_pinning_filters: Optional[Sequence[str]] = Field(
        default=None, alias="SessionPinningFilters"
    )
    init_query: Optional[str] = Field(default=None, alias="InitQuery")


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


class ScalingConfigurationModel(BaseModel):
    min_capacity: Optional[int] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    auto_pause: Optional[bool] = Field(default=None, alias="AutoPause")
    seconds_until_auto_pause: Optional[int] = Field(
        default=None, alias="SecondsUntilAutoPause"
    )
    timeout_action: Optional[str] = Field(default=None, alias="TimeoutAction")
    seconds_before_timeout: Optional[int] = Field(
        default=None, alias="SecondsBeforeTimeout"
    )


class ServerlessV2ScalingConfigurationModel(BaseModel):
    min_capacity: Optional[float] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")


class ProcessorFeatureModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class DBProxyEndpointModel(BaseModel):
    dbproxy_endpoint_name: Optional[str] = Field(
        default=None, alias="DBProxyEndpointName"
    )
    dbproxy_endpoint_arn: Optional[str] = Field(
        default=None, alias="DBProxyEndpointArn"
    )
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    status: Optional[
        Literal[
            "available",
            "creating",
            "deleting",
            "incompatible-network",
            "insufficient-resource-limits",
            "modifying",
        ]
    ] = Field(default=None, alias="Status")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_security_group_ids: Optional[List[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    vpc_subnet_ids: Optional[List[str]] = Field(default=None, alias="VpcSubnetIds")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    target_role: Optional[Literal["READ_ONLY", "READ_WRITE"]] = Field(
        default=None, alias="TargetRole"
    )
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")


class UserAuthConfigModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    auth_scheme: Optional[Literal["SECRETS"]] = Field(default=None, alias="AuthScheme")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    iamauth: Optional[Literal["DISABLED", "ENABLED", "REQUIRED"]] = Field(
        default=None, alias="IAMAuth"
    )
    client_password_auth_type: Optional[
        Literal[
            "MYSQL_NATIVE_PASSWORD",
            "POSTGRES_MD5",
            "POSTGRES_SCRAM_SHA_256",
            "SQL_SERVER_AUTHENTICATION",
        ]
    ] = Field(default=None, alias="ClientPasswordAuthType")


class CreateGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    source_dbcluster_identifier: Optional[str] = Field(
        default=None, alias="SourceDBClusterIdentifier"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")


class CustomDBEngineVersionAMIModel(BaseModel):
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    status: Optional[str] = Field(default=None, alias="Status")


class DBClusterBacktrackModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    backtrack_identifier: Optional[str] = Field(
        default=None, alias="BacktrackIdentifier"
    )
    backtrack_to: Optional[datetime] = Field(default=None, alias="BacktrackTo")
    backtracked_from: Optional[datetime] = Field(default=None, alias="BacktrackedFrom")
    backtrack_request_creation_time: Optional[datetime] = Field(
        default=None, alias="BacktrackRequestCreationTime"
    )
    status: Optional[str] = Field(default=None, alias="Status")


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
    supported_engine_modes: Optional[List[str]] = Field(
        default=None, alias="SupportedEngineModes"
    )


class DBClusterRoleModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    status: Optional[str] = Field(default=None, alias="Status")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class DBClusterSnapshotAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_values: Optional[List[str]] = Field(default=None, alias="AttributeValues")


class DomainMembershipModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    status: Optional[str] = Field(default=None, alias="Status")
    fqdn: Optional[str] = Field(default=None, alias="FQDN")
    iamrole_name: Optional[str] = Field(default=None, alias="IAMRoleName")


class MasterUserSecretModel(BaseModel):
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    secret_status: Optional[str] = Field(default=None, alias="SecretStatus")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ScalingConfigurationInfoModel(BaseModel):
    min_capacity: Optional[int] = Field(default=None, alias="MinCapacity")
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    auto_pause: Optional[bool] = Field(default=None, alias="AutoPause")
    seconds_until_auto_pause: Optional[int] = Field(
        default=None, alias="SecondsUntilAutoPause"
    )
    timeout_action: Optional[str] = Field(default=None, alias="TimeoutAction")
    seconds_before_timeout: Optional[int] = Field(
        default=None, alias="SecondsBeforeTimeout"
    )


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
    supported_engine_modes: Optional[List[str]] = Field(
        default=None, alias="SupportedEngineModes"
    )
    supports_parallel_query: Optional[bool] = Field(
        default=None, alias="SupportsParallelQuery"
    )
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )
    supports_babelfish: Optional[bool] = Field(default=None, alias="SupportsBabelfish")


class DBInstanceAutomatedBackupsReplicationModel(BaseModel):
    dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="DBInstanceAutomatedBackupsArn"
    )


class RestoreWindowModel(BaseModel):
    earliest_time: Optional[datetime] = Field(default=None, alias="EarliestTime")
    latest_time: Optional[datetime] = Field(default=None, alias="LatestTime")


class DBInstanceRoleModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")
    status: Optional[str] = Field(default=None, alias="Status")


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


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")


class OptionGroupMembershipModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    status: Optional[str] = Field(default=None, alias="Status")


class TargetHealthModel(BaseModel):
    state: Optional[Literal["AVAILABLE", "REGISTERING", "UNAVAILABLE"]] = Field(
        default=None, alias="State"
    )
    reason: Optional[
        Literal[
            "AUTH_FAILURE",
            "CONNECTION_FAILED",
            "INVALID_REPLICATION_STATE",
            "PENDING_PROXY_CAPACITY",
            "UNREACHABLE",
        ]
    ] = Field(default=None, alias="Reason")
    description: Optional[str] = Field(default=None, alias="Description")


class UserAuthConfigInfoModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    auth_scheme: Optional[Literal["SECRETS"]] = Field(default=None, alias="AuthScheme")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    iamauth: Optional[Literal["DISABLED", "ENABLED", "REQUIRED"]] = Field(
        default=None, alias="IAMAuth"
    )
    client_password_auth_type: Optional[
        Literal[
            "MYSQL_NATIVE_PASSWORD",
            "POSTGRES_MD5",
            "POSTGRES_SCRAM_SHA_256",
            "SQL_SERVER_AUTHENTICATION",
        ]
    ] = Field(default=None, alias="ClientPasswordAuthType")


class EC2SecurityGroupModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupId"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class IPRangeModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")


class DBSnapshotAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_values: Optional[List[str]] = Field(default=None, alias="AttributeValues")


class DeleteBlueGreenDeploymentRequestModel(BaseModel):
    blue_green_deployment_identifier: str = Field(alias="BlueGreenDeploymentIdentifier")
    delete_target: Optional[bool] = Field(default=None, alias="DeleteTarget")


class DeleteCustomDBEngineVersionMessageRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: str = Field(alias="EngineVersion")


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


class DeleteDBInstanceAutomatedBackupMessageRequestModel(BaseModel):
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="DBInstanceAutomatedBackupsArn"
    )


class DeleteDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    skip_final_snapshot: Optional[bool] = Field(default=None, alias="SkipFinalSnapshot")
    final_dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalDBSnapshotIdentifier"
    )
    delete_automated_backups: Optional[bool] = Field(
        default=None, alias="DeleteAutomatedBackups"
    )


class DeleteDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")


class DeleteDBProxyEndpointRequestModel(BaseModel):
    dbproxy_endpoint_name: str = Field(alias="DBProxyEndpointName")


class DeleteDBProxyRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")


class DeleteDBSecurityGroupMessageRequestModel(BaseModel):
    dbsecurity_group_name: str = Field(alias="DBSecurityGroupName")


class DeleteDBSnapshotMessageRequestModel(BaseModel):
    dbsnapshot_identifier: str = Field(alias="DBSnapshotIdentifier")


class DeleteDBSubnetGroupMessageRequestModel(BaseModel):
    dbsubnet_group_name: str = Field(alias="DBSubnetGroupName")


class DeleteEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")


class DeleteGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")


class DeleteOptionGroupMessageRequestModel(BaseModel):
    option_group_name: str = Field(alias="OptionGroupName")


class DeregisterDBProxyTargetsRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    dbinstance_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="DBInstanceIdentifiers"
    )
    dbcluster_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="DBClusterIdentifiers"
    )


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


class DescribeDBLogFilesDetailsModel(BaseModel):
    log_file_name: Optional[str] = Field(default=None, alias="LogFileName")
    last_written: Optional[int] = Field(default=None, alias="LastWritten")
    size: Optional[int] = Field(default=None, alias="Size")


class DescribeDBSnapshotAttributesMessageRequestModel(BaseModel):
    dbsnapshot_identifier: str = Field(alias="DBSnapshotIdentifier")


class DescribeValidDBInstanceModificationsMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")


class DoubleRangeModel(BaseModel):
    from_: Optional[float] = Field(default=None, alias="From")
    to: Optional[float] = Field(default=None, alias="To")


class DownloadDBLogFilePortionMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    log_file_name: str = Field(alias="LogFileName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    number_of_lines: Optional[int] = Field(default=None, alias="NumberOfLines")


class EventCategoriesMapModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")


class EventModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "blue-green-deployment",
            "custom-engine-version",
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-proxy",
            "db-security-group",
            "db-snapshot",
        ]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")
    date: Optional[datetime] = Field(default=None, alias="Date")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")


class ExportTaskModel(BaseModel):
    export_task_identifier: Optional[str] = Field(
        default=None, alias="ExportTaskIdentifier"
    )
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    export_only: Optional[List[str]] = Field(default=None, alias="ExportOnly")
    snapshot_time: Optional[datetime] = Field(default=None, alias="SnapshotTime")
    task_start_time: Optional[datetime] = Field(default=None, alias="TaskStartTime")
    task_end_time: Optional[datetime] = Field(default=None, alias="TaskEndTime")
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    status: Optional[str] = Field(default=None, alias="Status")
    percent_progress: Optional[int] = Field(default=None, alias="PercentProgress")
    total_extracted_data_in_gb: Optional[int] = Field(
        default=None, alias="TotalExtractedDataInGB"
    )
    failure_cause: Optional[str] = Field(default=None, alias="FailureCause")
    warning_message: Optional[str] = Field(default=None, alias="WarningMessage")
    source_type: Optional[Literal["CLUSTER", "SNAPSHOT"]] = Field(
        default=None, alias="SourceType"
    )


class FailoverDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    target_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="TargetDBInstanceIdentifier"
    )


class FailoverGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: str = Field(alias="GlobalClusterIdentifier")
    target_db_cluster_identifier: str = Field(alias="TargetDbClusterIdentifier")


class FailoverStateModel(BaseModel):
    status: Optional[Literal["cancelling", "failing-over", "pending"]] = Field(
        default=None, alias="Status"
    )
    from_db_cluster_arn: Optional[str] = Field(default=None, alias="FromDbClusterArn")
    to_db_cluster_arn: Optional[str] = Field(default=None, alias="ToDbClusterArn")


class GlobalClusterMemberModel(BaseModel):
    dbcluster_arn: Optional[str] = Field(default=None, alias="DBClusterArn")
    readers: Optional[List[str]] = Field(default=None, alias="Readers")
    is_writer: Optional[bool] = Field(default=None, alias="IsWriter")
    global_write_forwarding_status: Optional[
        Literal["disabled", "disabling", "enabled", "enabling", "unknown"]
    ] = Field(default=None, alias="GlobalWriteForwardingStatus")


class MinimumEngineVersionPerAllowedValueModel(BaseModel):
    allowed_value: Optional[str] = Field(default=None, alias="AllowedValue")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )


class ModifyActivityStreamRequestModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    audit_policy_state: Optional[Literal["locked", "unlocked"]] = Field(
        default=None, alias="AuditPolicyState"
    )


class ModifyCertificatesMessageRequestModel(BaseModel):
    certificate_identifier: Optional[str] = Field(
        default=None, alias="CertificateIdentifier"
    )
    remove_customer_override: Optional[bool] = Field(
        default=None, alias="RemoveCustomerOverride"
    )


class ModifyCurrentDBClusterCapacityMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    seconds_before_timeout: Optional[int] = Field(
        default=None, alias="SecondsBeforeTimeout"
    )
    timeout_action: Optional[str] = Field(default=None, alias="TimeoutAction")


class ModifyCustomDBEngineVersionMessageRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: str = Field(alias="EngineVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal["available", "inactive", "inactive-except-restore"]
    ] = Field(default=None, alias="Status")


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


class ModifyDBProxyEndpointRequestModel(BaseModel):
    dbproxy_endpoint_name: str = Field(alias="DBProxyEndpointName")
    new_dbproxy_endpoint_name: Optional[str] = Field(
        default=None, alias="NewDBProxyEndpointName"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )


class ModifyDBSnapshotAttributeMessageRequestModel(BaseModel):
    dbsnapshot_identifier: str = Field(alias="DBSnapshotIdentifier")
    attribute_name: str = Field(alias="AttributeName")
    values_to_add: Optional[Sequence[str]] = Field(default=None, alias="ValuesToAdd")
    values_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="ValuesToRemove"
    )


class ModifyDBSnapshotMessageRequestModel(BaseModel):
    dbsnapshot_identifier: str = Field(alias="DBSnapshotIdentifier")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")


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
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
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


class OptionSettingModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    description: Optional[str] = Field(default=None, alias="Description")
    apply_type: Optional[str] = Field(default=None, alias="ApplyType")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    is_collection: Optional[bool] = Field(default=None, alias="IsCollection")


class OptionVersionModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")


class OutpostModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


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


class PromoteReadReplicaMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )


class RangeModel(BaseModel):
    from_: Optional[int] = Field(default=None, alias="From")
    to: Optional[int] = Field(default=None, alias="To")
    step: Optional[int] = Field(default=None, alias="Step")


class RebootDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class RebootDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    force_failover: Optional[bool] = Field(default=None, alias="ForceFailover")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class RegisterDBProxyTargetsRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    dbinstance_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="DBInstanceIdentifiers"
    )
    dbcluster_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="DBClusterIdentifiers"
    )


class RemoveFromGlobalClusterMessageRequestModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    db_cluster_identifier: Optional[str] = Field(
        default=None, alias="DbClusterIdentifier"
    )


class RemoveRoleFromDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")


class RemoveRoleFromDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    role_arn: str = Field(alias="RoleArn")
    feature_name: str = Field(alias="FeatureName")


class RemoveSourceIdentifierFromSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    source_identifier: str = Field(alias="SourceIdentifier")


class RemoveTagsFromResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class RevokeDBSecurityGroupIngressMessageRequestModel(BaseModel):
    dbsecurity_group_name: str = Field(alias="DBSecurityGroupName")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupId"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class SourceRegionModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    status: Optional[str] = Field(default=None, alias="Status")
    supports_dbinstance_automated_backups_replication: Optional[bool] = Field(
        default=None, alias="SupportsDBInstanceAutomatedBackupsReplication"
    )


class StartActivityStreamRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    mode: Literal["async", "sync"] = Field(alias="Mode")
    kms_key_id: str = Field(alias="KmsKeyId")
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    engine_native_audit_fields_included: Optional[bool] = Field(
        default=None, alias="EngineNativeAuditFieldsIncluded"
    )


class StartDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class StartDBInstanceAutomatedBackupsReplicationMessageRequestModel(BaseModel):
    source_dbinstance_arn: str = Field(alias="SourceDBInstanceArn")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")


class StartDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")


class StartExportTaskMessageRequestModel(BaseModel):
    export_task_identifier: str = Field(alias="ExportTaskIdentifier")
    source_arn: str = Field(alias="SourceArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    iam_role_arn: str = Field(alias="IamRoleArn")
    kms_key_id: str = Field(alias="KmsKeyId")
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    export_only: Optional[Sequence[str]] = Field(default=None, alias="ExportOnly")


class StopActivityStreamRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")


class StopDBClusterMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")


class StopDBInstanceAutomatedBackupsReplicationMessageRequestModel(BaseModel):
    source_dbinstance_arn: str = Field(alias="SourceDBInstanceArn")


class StopDBInstanceMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )


class SwitchoverBlueGreenDeploymentRequestModel(BaseModel):
    blue_green_deployment_identifier: str = Field(alias="BlueGreenDeploymentIdentifier")
    switchover_timeout: Optional[int] = Field(default=None, alias="SwitchoverTimeout")


class SwitchoverReadReplicaMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")


class AccountAttributesMessageModel(BaseModel):
    account_quotas: List[AccountQuotaModel] = Field(alias="AccountQuotas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterBacktrackResponseMetadataModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    backtrack_identifier: str = Field(alias="BacktrackIdentifier")
    backtrack_to: datetime = Field(alias="BacktrackTo")
    backtracked_from: datetime = Field(alias="BacktrackedFrom")
    backtrack_request_creation_time: datetime = Field(
        alias="BacktrackRequestCreationTime"
    )
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterCapacityInfoModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    pending_capacity: int = Field(alias="PendingCapacity")
    current_capacity: int = Field(alias="CurrentCapacity")
    seconds_before_timeout: int = Field(alias="SecondsBeforeTimeout")
    timeout_action: str = Field(alias="TimeoutAction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBClusterEndpointResponseMetadataModel(BaseModel):
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


class DBClusterParameterGroupNameMessageModel(BaseModel):
    dbcluster_parameter_group_name: str = Field(alias="DBClusterParameterGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBParameterGroupNameMessageModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DownloadDBLogFilePortionDetailsModel(BaseModel):
    log_file_data: str = Field(alias="LogFileData")
    marker: str = Field(alias="Marker")
    additional_data_pending: bool = Field(alias="AdditionalDataPending")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportTaskResponseMetadataModel(BaseModel):
    export_task_identifier: str = Field(alias="ExportTaskIdentifier")
    source_arn: str = Field(alias="SourceArn")
    export_only: List[str] = Field(alias="ExportOnly")
    snapshot_time: datetime = Field(alias="SnapshotTime")
    task_start_time: datetime = Field(alias="TaskStartTime")
    task_end_time: datetime = Field(alias="TaskEndTime")
    s3_bucket: str = Field(alias="S3Bucket")
    s3_prefix: str = Field(alias="S3Prefix")
    iam_role_arn: str = Field(alias="IamRoleArn")
    kms_key_id: str = Field(alias="KmsKeyId")
    status: str = Field(alias="Status")
    percent_progress: int = Field(alias="PercentProgress")
    total_extracted_data_in_gb: int = Field(alias="TotalExtractedDataInGB")
    failure_cause: str = Field(alias="FailureCause")
    warning_message: str = Field(alias="WarningMessage")
    source_type: Literal["CLUSTER", "SNAPSHOT"] = Field(alias="SourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyActivityStreamResponseModel(BaseModel):
    kms_key_id: str = Field(alias="KmsKeyId")
    kinesis_stream_name: str = Field(alias="KinesisStreamName")
    status: Literal["started", "starting", "stopped", "stopping"] = Field(
        alias="Status"
    )
    mode: Literal["async", "sync"] = Field(alias="Mode")
    engine_native_audit_fields_included: bool = Field(
        alias="EngineNativeAuditFieldsIncluded"
    )
    policy_status: Literal[
        "locked", "locking-policy", "unlocked", "unlocking-policy"
    ] = Field(alias="PolicyStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartActivityStreamResponseModel(BaseModel):
    kms_key_id: str = Field(alias="KmsKeyId")
    kinesis_stream_name: str = Field(alias="KinesisStreamName")
    status: Literal["started", "starting", "stopped", "stopping"] = Field(
        alias="Status"
    )
    mode: Literal["async", "sync"] = Field(alias="Mode")
    apply_immediately: bool = Field(alias="ApplyImmediately")
    engine_native_audit_fields_included: bool = Field(
        alias="EngineNativeAuditFieldsIncluded"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopActivityStreamResponseModel(BaseModel):
    kms_key_id: str = Field(alias="KmsKeyId")
    kinesis_stream_name: str = Field(alias="KinesisStreamName")
    status: Literal["started", "starting", "stopped", "stopping"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddSourceIdentifierToSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventSubscriptionResultModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventSubscriptionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    event_subscriptions_list: List[EventSubscriptionModel] = Field(
        alias="EventSubscriptionsList"
    )
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


class CopyDBSnapshotMessageRequestModel(BaseModel):
    source_dbsnapshot_identifier: str = Field(alias="SourceDBSnapshotIdentifier")
    target_dbsnapshot_identifier: str = Field(alias="TargetDBSnapshotIdentifier")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    copy_tags: Optional[bool] = Field(default=None, alias="CopyTags")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    target_custom_availability_zone: Optional[str] = Field(
        default=None, alias="TargetCustomAvailabilityZone"
    )
    copy_option_group: Optional[bool] = Field(default=None, alias="CopyOptionGroup")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")


class CopyOptionGroupMessageRequestModel(BaseModel):
    source_option_group_identifier: str = Field(alias="SourceOptionGroupIdentifier")
    target_option_group_identifier: str = Field(alias="TargetOptionGroupIdentifier")
    target_option_group_description: str = Field(alias="TargetOptionGroupDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateBlueGreenDeploymentRequestModel(BaseModel):
    blue_green_deployment_name: str = Field(alias="BlueGreenDeploymentName")
    source: str = Field(alias="Source")
    target_engine_version: Optional[str] = Field(
        default=None, alias="TargetEngineVersion"
    )
    target_dbparameter_group_name: Optional[str] = Field(
        default=None, alias="TargetDBParameterGroupName"
    )
    target_dbcluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="TargetDBClusterParameterGroupName"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateCustomDBEngineVersionMessageRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: str = Field(alias="EngineVersion")
    database_installation_files_s3_bucket_name: Optional[str] = Field(
        default=None, alias="DatabaseInstallationFilesS3BucketName"
    )
    database_installation_files_s3_prefix: Optional[str] = Field(
        default=None, alias="DatabaseInstallationFilesS3Prefix"
    )
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    description: Optional[str] = Field(default=None, alias="Description")
    manifest: Optional[str] = Field(default=None, alias="Manifest")
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


class CreateDBParameterGroupMessageRequestModel(BaseModel):
    dbparameter_group_name: str = Field(alias="DBParameterGroupName")
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBProxyEndpointRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    dbproxy_endpoint_name: str = Field(alias="DBProxyEndpointName")
    vpc_subnet_ids: Sequence[str] = Field(alias="VpcSubnetIds")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    target_role: Optional[Literal["READ_ONLY", "READ_WRITE"]] = Field(
        default=None, alias="TargetRole"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBSecurityGroupMessageRequestModel(BaseModel):
    dbsecurity_group_name: str = Field(alias="DBSecurityGroupName")
    dbsecurity_group_description: str = Field(alias="DBSecurityGroupDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateDBSnapshotMessageRequestModel(BaseModel):
    dbsnapshot_identifier: str = Field(alias="DBSnapshotIdentifier")
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
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


class CreateOptionGroupMessageRequestModel(BaseModel):
    option_group_name: str = Field(alias="OptionGroupName")
    engine_name: str = Field(alias="EngineName")
    major_engine_version: str = Field(alias="MajorEngineVersion")
    option_group_description: str = Field(alias="OptionGroupDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


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
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
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
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")
    dbsystem_id: Optional[str] = Field(default=None, alias="DBSystemId")


class PurchaseReservedDBInstancesOfferingMessageRequestModel(BaseModel):
    reserved_dbinstances_offering_id: str = Field(alias="ReservedDBInstancesOfferingId")
    reserved_dbinstance_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstanceId"
    )
    dbinstance_count: Optional[int] = Field(default=None, alias="DBInstanceCount")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagListMessageModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrderableDBInstanceOptionModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    availability_zone_group: Optional[str] = Field(
        default=None, alias="AvailabilityZoneGroup"
    )
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
    available_processor_features: Optional[
        List[AvailableProcessorFeatureModel]
    ] = Field(default=None, alias="AvailableProcessorFeatures")
    supported_engine_modes: Optional[List[str]] = Field(
        default=None, alias="SupportedEngineModes"
    )
    supports_storage_autoscaling: Optional[bool] = Field(
        default=None, alias="SupportsStorageAutoscaling"
    )
    supports_kerberos_authentication: Optional[bool] = Field(
        default=None, alias="SupportsKerberosAuthentication"
    )
    outpost_capable: Optional[bool] = Field(default=None, alias="OutpostCapable")
    supported_activity_stream_modes: Optional[List[str]] = Field(
        default=None, alias="SupportedActivityStreamModes"
    )
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )
    supports_clusters: Optional[bool] = Field(default=None, alias="SupportsClusters")
    supported_network_types: Optional[List[str]] = Field(
        default=None, alias="SupportedNetworkTypes"
    )
    supports_storage_throughput: Optional[bool] = Field(
        default=None, alias="SupportsStorageThroughput"
    )
    min_storage_throughput_per_db_instance: Optional[int] = Field(
        default=None, alias="MinStorageThroughputPerDbInstance"
    )
    max_storage_throughput_per_db_instance: Optional[int] = Field(
        default=None, alias="MaxStorageThroughputPerDbInstance"
    )
    min_storage_throughput_per_iops: Optional[float] = Field(
        default=None, alias="MinStorageThroughputPerIops"
    )
    max_storage_throughput_per_iops: Optional[float] = Field(
        default=None, alias="MaxStorageThroughputPerIops"
    )


class BlueGreenDeploymentModel(BaseModel):
    blue_green_deployment_identifier: Optional[str] = Field(
        default=None, alias="BlueGreenDeploymentIdentifier"
    )
    blue_green_deployment_name: Optional[str] = Field(
        default=None, alias="BlueGreenDeploymentName"
    )
    source: Optional[str] = Field(default=None, alias="Source")
    target: Optional[str] = Field(default=None, alias="Target")
    switchover_details: Optional[List[SwitchoverDetailModel]] = Field(
        default=None, alias="SwitchoverDetails"
    )
    tasks: Optional[List[BlueGreenDeploymentTaskModel]] = Field(
        default=None, alias="Tasks"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    status_details: Optional[str] = Field(default=None, alias="StatusDetails")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    delete_time: Optional[datetime] = Field(default=None, alias="DeleteTime")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")


class CertificateMessageModel(BaseModel):
    certificates: List[CertificateModel] = Field(alias="Certificates")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyCertificatesResultModel(BaseModel):
    certificate: CertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterPendingModifiedValuesModel(BaseModel):
    pending_cloudwatch_logs_exports: Optional[
        PendingCloudwatchLogsExportsModel
    ] = Field(default=None, alias="PendingCloudwatchLogsExports")
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    iops: Optional[int] = Field(default=None, alias="Iops")


class DBProxyTargetGroupModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    target_group_arn: Optional[str] = Field(default=None, alias="TargetGroupArn")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")
    status: Optional[str] = Field(default=None, alias="Status")
    connection_pool_config: Optional[ConnectionPoolConfigurationInfoModel] = Field(
        default=None, alias="ConnectionPoolConfig"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    updated_date: Optional[datetime] = Field(default=None, alias="UpdatedDate")


class ModifyDBProxyTargetGroupRequestModel(BaseModel):
    target_group_name: str = Field(alias="TargetGroupName")
    dbproxy_name: str = Field(alias="DBProxyName")
    connection_pool_config: Optional[ConnectionPoolConfigurationModel] = Field(
        default=None, alias="ConnectionPoolConfig"
    )
    new_name: Optional[str] = Field(default=None, alias="NewName")


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
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
    scaling_configuration: Optional[ScalingConfigurationModel] = Field(
        default=None, alias="ScalingConfiguration"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    enable_http_endpoint: Optional[bool] = Field(
        default=None, alias="EnableHttpEndpoint"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    enable_global_write_forwarding: Optional[bool] = Field(
        default=None, alias="EnableGlobalWriteForwarding"
    )
    dbcluster_instance_class: Optional[str] = Field(
        default=None, alias="DBClusterInstanceClass"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    dbsystem_id: Optional[str] = Field(default=None, alias="DBSystemId")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
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
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
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
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    scaling_configuration: Optional[ScalingConfigurationModel] = Field(
        default=None, alias="ScalingConfiguration"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    enable_http_endpoint: Optional[bool] = Field(
        default=None, alias="EnableHttpEndpoint"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    enable_global_write_forwarding: Optional[bool] = Field(
        default=None, alias="EnableGlobalWriteForwarding"
    )
    dbcluster_instance_class: Optional[str] = Field(
        default=None, alias="DBClusterInstanceClass"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    rotate_master_user_password: Optional[bool] = Field(
        default=None, alias="RotateMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
    )


class RestoreDBClusterFromS3MessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    engine: str = Field(alias="Engine")
    master_username: str = Field(alias="MasterUsername")
    source_engine: str = Field(alias="SourceEngine")
    source_engine_version: str = Field(alias="SourceEngineVersion")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_ingestion_role_arn: str = Field(alias="S3IngestionRoleArn")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
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
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
    )


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
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
    scaling_configuration: Optional[ScalingConfigurationModel] = Field(
        default=None, alias="ScalingConfiguration"
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
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    dbcluster_instance_class: Optional[str] = Field(
        default=None, alias="DBClusterInstanceClass"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


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
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
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
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    scaling_configuration: Optional[ScalingConfigurationModel] = Field(
        default=None, alias="ScalingConfiguration"
    )
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
    dbcluster_instance_class: Optional[str] = Field(
        default=None, alias="DBClusterInstanceClass"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    iops: Optional[int] = Field(default=None, alias="Iops")
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


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
    nchar_character_set_name: Optional[str] = Field(
        default=None, alias="NcharCharacterSetName"
    )
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
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    enable_customer_owned_ip: Optional[bool] = Field(
        default=None, alias="EnableCustomerOwnedIp"
    )
    custom_iam_instance_profile: Optional[str] = Field(
        default=None, alias="CustomIamInstanceProfile"
    )
    backup_target: Optional[str] = Field(default=None, alias="BackupTarget")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
    )
    cacertificate_identifier: Optional[str] = Field(
        default=None, alias="CACertificateIdentifier"
    )


class CreateDBInstanceReadReplicaMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    source_dbinstance_identifier: str = Field(alias="SourceDBInstanceIdentifier")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    port: Optional[int] = Field(default=None, alias="Port")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    pre_signed_url: Optional[str] = Field(default=None, alias="PreSignedUrl")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    use_default_processor_features: Optional[bool] = Field(
        default=None, alias="UseDefaultProcessorFeatures"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    replica_mode: Optional[Literal["mounted", "open-read-only"]] = Field(
        default=None, alias="ReplicaMode"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    custom_iam_instance_profile: Optional[str] = Field(
        default=None, alias="CustomIamInstanceProfile"
    )
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    enable_customer_owned_ip: Optional[bool] = Field(
        default=None, alias="EnableCustomerOwnedIp"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")


class DBSnapshotModel(BaseModel):
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="SnapshotCreateTime"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    instance_create_time: Optional[datetime] = Field(
        default=None, alias="InstanceCreateTime"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    percent_progress: Optional[int] = Field(default=None, alias="PercentProgress")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    source_dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="SourceDBSnapshotIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    dbsnapshot_arn: Optional[str] = Field(default=None, alias="DBSnapshotArn")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    processor_features: Optional[List[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")
    original_snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="OriginalSnapshotCreateTime"
    )
    snapshot_database_time: Optional[datetime] = Field(
        default=None, alias="SnapshotDatabaseTime"
    )
    snapshot_target: Optional[str] = Field(default=None, alias="SnapshotTarget")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")


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
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    cloudwatch_logs_export_configuration: Optional[
        CloudwatchLogsExportConfigurationModel
    ] = Field(default=None, alias="CloudwatchLogsExportConfiguration")
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    use_default_processor_features: Optional[bool] = Field(
        default=None, alias="UseDefaultProcessorFeatures"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    certificate_rotation_restart: Optional[bool] = Field(
        default=None, alias="CertificateRotationRestart"
    )
    replica_mode: Optional[Literal["mounted", "open-read-only"]] = Field(
        default=None, alias="ReplicaMode"
    )
    enable_customer_owned_ip: Optional[bool] = Field(
        default=None, alias="EnableCustomerOwnedIp"
    )
    aws_backup_recovery_point_arn: Optional[str] = Field(
        default=None, alias="AwsBackupRecoveryPointArn"
    )
    automation_mode: Optional[Literal["all-paused", "full"]] = Field(
        default=None, alias="AutomationMode"
    )
    resume_full_automation_mode_minutes: Optional[int] = Field(
        default=None, alias="ResumeFullAutomationModeMinutes"
    )
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    rotate_master_user_password: Optional[bool] = Field(
        default=None, alias="RotateMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
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
    processor_features: Optional[List[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    automation_mode: Optional[Literal["all-paused", "full"]] = Field(
        default=None, alias="AutomationMode"
    )
    resume_full_automation_mode_time: Optional[datetime] = Field(
        default=None, alias="ResumeFullAutomationModeTime"
    )
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")


class RestoreDBInstanceFromDBSnapshotMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    engine: Optional[str] = Field(default=None, alias="Engine")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    tde_credential_password: Optional[str] = Field(
        default=None, alias="TdeCredentialPassword"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    use_default_processor_features: Optional[bool] = Field(
        default=None, alias="UseDefaultProcessorFeatures"
    )
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    enable_customer_owned_ip: Optional[bool] = Field(
        default=None, alias="EnableCustomerOwnedIp"
    )
    custom_iam_instance_profile: Optional[str] = Field(
        default=None, alias="CustomIamInstanceProfile"
    )
    backup_target: Optional[str] = Field(default=None, alias="BackupTarget")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    dbcluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DBClusterSnapshotIdentifier"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")


class RestoreDBInstanceFromS3MessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    dbinstance_class: str = Field(alias="DBInstanceClass")
    engine: str = Field(alias="Engine")
    source_engine: str = Field(alias="SourceEngine")
    source_engine_version: str = Field(alias="SourceEngineVersion")
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_ingestion_role_arn: str = Field(alias="S3IngestionRoleArn")
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
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    enable_performance_insights: Optional[bool] = Field(
        default=None, alias="EnablePerformanceInsights"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    use_default_processor_features: Optional[bool] = Field(
        default=None, alias="UseDefaultProcessorFeatures"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    manage_master_user_password: Optional[bool] = Field(
        default=None, alias="ManageMasterUserPassword"
    )
    master_user_secret_kms_key_id: Optional[str] = Field(
        default=None, alias="MasterUserSecretKmsKeyId"
    )


class RestoreDBInstanceToPointInTimeMessageRequestModel(BaseModel):
    target_dbinstance_identifier: str = Field(alias="TargetDBInstanceIdentifier")
    source_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="SourceDBInstanceIdentifier"
    )
    restore_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="RestoreTime"
    )
    use_latest_restorable_time: Optional[bool] = Field(
        default=None, alias="UseLatestRestorableTime"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    engine: Optional[str] = Field(default=None, alias="Engine")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    tde_credential_password: Optional[str] = Field(
        default=None, alias="TdeCredentialPassword"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    domain: Optional[str] = Field(default=None, alias="Domain")
    domain_iamrole_name: Optional[str] = Field(default=None, alias="DomainIAMRoleName")
    enable_iamdatabase_authentication: Optional[bool] = Field(
        default=None, alias="EnableIAMDatabaseAuthentication"
    )
    enable_cloudwatch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnableCloudwatchLogsExports"
    )
    processor_features: Optional[Sequence[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    use_default_processor_features: Optional[bool] = Field(
        default=None, alias="UseDefaultProcessorFeatures"
    )
    dbparameter_group_name: Optional[str] = Field(
        default=None, alias="DBParameterGroupName"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    source_dbi_resource_id: Optional[str] = Field(
        default=None, alias="SourceDbiResourceId"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    source_dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="SourceDBInstanceAutomatedBackupsArn"
    )
    enable_customer_owned_ip: Optional[bool] = Field(
        default=None, alias="EnableCustomerOwnedIp"
    )
    custom_iam_instance_profile: Optional[str] = Field(
        default=None, alias="CustomIamInstanceProfile"
    )
    backup_target: Optional[str] = Field(default=None, alias="BackupTarget")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")


class CreateDBProxyEndpointResponseModel(BaseModel):
    dbproxy_endpoint: DBProxyEndpointModel = Field(alias="DBProxyEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBProxyEndpointResponseModel(BaseModel):
    dbproxy_endpoint: DBProxyEndpointModel = Field(alias="DBProxyEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDBProxyEndpointsResponseModel(BaseModel):
    dbproxy_endpoints: List[DBProxyEndpointModel] = Field(alias="DBProxyEndpoints")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBProxyEndpointResponseModel(BaseModel):
    dbproxy_endpoint: DBProxyEndpointModel = Field(alias="DBProxyEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBProxyRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    engine_family: Literal["MYSQL", "POSTGRESQL", "SQLSERVER"] = Field(
        alias="EngineFamily"
    )
    auth: Sequence[UserAuthConfigModel] = Field(alias="Auth")
    role_arn: str = Field(alias="RoleArn")
    vpc_subnet_ids: Sequence[str] = Field(alias="VpcSubnetIds")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    require_tl_s: Optional[bool] = Field(default=None, alias="RequireTLS")
    idle_client_timeout: Optional[int] = Field(default=None, alias="IdleClientTimeout")
    debug_logging: Optional[bool] = Field(default=None, alias="DebugLogging")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ModifyDBProxyRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    new_dbproxy_name: Optional[str] = Field(default=None, alias="NewDBProxyName")
    auth: Optional[Sequence[UserAuthConfigModel]] = Field(default=None, alias="Auth")
    require_tl_s: Optional[bool] = Field(default=None, alias="RequireTLS")
    idle_client_timeout: Optional[int] = Field(default=None, alias="IdleClientTimeout")
    debug_logging: Optional[bool] = Field(default=None, alias="DebugLogging")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )


class DBClusterBacktrackMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbcluster_backtracks: List[DBClusterBacktrackModel] = Field(
        alias="DBClusterBacktracks"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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


class DBEngineVersionResponseMetadataModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: str = Field(alias="EngineVersion")
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
    dbengine_description: str = Field(alias="DBEngineDescription")
    dbengine_version_description: str = Field(alias="DBEngineVersionDescription")
    default_character_set: CharacterSetModel = Field(alias="DefaultCharacterSet")
    image: CustomDBEngineVersionAMIModel = Field(alias="Image")
    dbengine_media_type: str = Field(alias="DBEngineMediaType")
    supported_character_sets: List[CharacterSetModel] = Field(
        alias="SupportedCharacterSets"
    )
    supported_nchar_character_sets: List[CharacterSetModel] = Field(
        alias="SupportedNcharCharacterSets"
    )
    valid_upgrade_target: List[UpgradeTargetModel] = Field(alias="ValidUpgradeTarget")
    supported_timezones: List[TimezoneModel] = Field(alias="SupportedTimezones")
    exportable_log_types: List[str] = Field(alias="ExportableLogTypes")
    supports_log_exports_to_cloudwatch_logs: bool = Field(
        alias="SupportsLogExportsToCloudwatchLogs"
    )
    supports_read_replica: bool = Field(alias="SupportsReadReplica")
    supported_engine_modes: List[str] = Field(alias="SupportedEngineModes")
    supported_feature_names: List[str] = Field(alias="SupportedFeatureNames")
    status: str = Field(alias="Status")
    supports_parallel_query: bool = Field(alias="SupportsParallelQuery")
    supports_global_databases: bool = Field(alias="SupportsGlobalDatabases")
    major_engine_version: str = Field(alias="MajorEngineVersion")
    database_installation_files_s3_bucket_name: str = Field(
        alias="DatabaseInstallationFilesS3BucketName"
    )
    database_installation_files_s3_prefix: str = Field(
        alias="DatabaseInstallationFilesS3Prefix"
    )
    dbengine_version_arn: str = Field(alias="DBEngineVersionArn")
    kms_key_id: str = Field(alias="KMSKeyId")
    create_time: datetime = Field(alias="CreateTime")
    tag_list: List[TagModel] = Field(alias="TagList")
    supports_babelfish: bool = Field(alias="SupportsBabelfish")
    custom_dbengine_version_manifest: str = Field(alias="CustomDBEngineVersionManifest")
    supports_certificate_rotation_without_restart: bool = Field(
        alias="SupportsCertificateRotationWithoutRestart"
    )
    supported_cacertificate_identifiers: List[str] = Field(
        alias="SupportedCACertificateIdentifiers"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
    image: Optional[CustomDBEngineVersionAMIModel] = Field(default=None, alias="Image")
    dbengine_media_type: Optional[str] = Field(default=None, alias="DBEngineMediaType")
    supported_character_sets: Optional[List[CharacterSetModel]] = Field(
        default=None, alias="SupportedCharacterSets"
    )
    supported_nchar_character_sets: Optional[List[CharacterSetModel]] = Field(
        default=None, alias="SupportedNcharCharacterSets"
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
    supported_engine_modes: Optional[List[str]] = Field(
        default=None, alias="SupportedEngineModes"
    )
    supported_feature_names: Optional[List[str]] = Field(
        default=None, alias="SupportedFeatureNames"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    supports_parallel_query: Optional[bool] = Field(
        default=None, alias="SupportsParallelQuery"
    )
    supports_global_databases: Optional[bool] = Field(
        default=None, alias="SupportsGlobalDatabases"
    )
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )
    database_installation_files_s3_bucket_name: Optional[str] = Field(
        default=None, alias="DatabaseInstallationFilesS3BucketName"
    )
    database_installation_files_s3_prefix: Optional[str] = Field(
        default=None, alias="DatabaseInstallationFilesS3Prefix"
    )
    dbengine_version_arn: Optional[str] = Field(
        default=None, alias="DBEngineVersionArn"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")
    supports_babelfish: Optional[bool] = Field(default=None, alias="SupportsBabelfish")
    custom_dbengine_version_manifest: Optional[str] = Field(
        default=None, alias="CustomDBEngineVersionManifest"
    )
    supports_certificate_rotation_without_restart: Optional[bool] = Field(
        default=None, alias="SupportsCertificateRotationWithoutRestart"
    )
    supported_cacertificate_identifiers: Optional[List[str]] = Field(
        default=None, alias="SupportedCACertificateIdentifiers"
    )


class DBInstanceAutomatedBackupModel(BaseModel):
    dbinstance_arn: Optional[str] = Field(default=None, alias="DBInstanceArn")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    region: Optional[str] = Field(default=None, alias="Region")
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    restore_window: Optional[RestoreWindowModel] = Field(
        default=None, alias="RestoreWindow"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    instance_create_time: Optional[datetime] = Field(
        default=None, alias="InstanceCreateTime"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="DBInstanceAutomatedBackupsArn"
    )
    dbinstance_automated_backups_replications: Optional[
        List[DBInstanceAutomatedBackupsReplicationModel]
    ] = Field(default=None, alias="DBInstanceAutomatedBackupsReplications")
    backup_target: Optional[str] = Field(default=None, alias="BackupTarget")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")


class DBProxyTargetModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    tracked_cluster_id: Optional[str] = Field(default=None, alias="TrackedClusterId")
    rds_resource_id: Optional[str] = Field(default=None, alias="RdsResourceId")
    port: Optional[int] = Field(default=None, alias="Port")
    type: Optional[
        Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"]
    ] = Field(default=None, alias="Type")
    role: Optional[Literal["READ_ONLY", "READ_WRITE", "UNKNOWN"]] = Field(
        default=None, alias="Role"
    )
    target_health: Optional[TargetHealthModel] = Field(
        default=None, alias="TargetHealth"
    )


class DBProxyModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    dbproxy_arn: Optional[str] = Field(default=None, alias="DBProxyArn")
    status: Optional[
        Literal[
            "available",
            "creating",
            "deleting",
            "incompatible-network",
            "insufficient-resource-limits",
            "modifying",
            "reactivating",
            "suspended",
            "suspending",
        ]
    ] = Field(default=None, alias="Status")
    engine_family: Optional[str] = Field(default=None, alias="EngineFamily")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_security_group_ids: Optional[List[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    vpc_subnet_ids: Optional[List[str]] = Field(default=None, alias="VpcSubnetIds")
    auth: Optional[List[UserAuthConfigInfoModel]] = Field(default=None, alias="Auth")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    require_tl_s: Optional[bool] = Field(default=None, alias="RequireTLS")
    idle_client_timeout: Optional[int] = Field(default=None, alias="IdleClientTimeout")
    debug_logging: Optional[bool] = Field(default=None, alias="DebugLogging")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    updated_date: Optional[datetime] = Field(default=None, alias="UpdatedDate")


class DBSecurityGroupModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    dbsecurity_group_name: Optional[str] = Field(
        default=None, alias="DBSecurityGroupName"
    )
    dbsecurity_group_description: Optional[str] = Field(
        default=None, alias="DBSecurityGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    ec2_security_groups: Optional[List[EC2SecurityGroupModel]] = Field(
        default=None, alias="EC2SecurityGroups"
    )
    ip_ranges: Optional[List[IPRangeModel]] = Field(default=None, alias="IPRanges")
    dbsecurity_group_arn: Optional[str] = Field(
        default=None, alias="DBSecurityGroupArn"
    )


class DBSnapshotAttributesResultModel(BaseModel):
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    dbsnapshot_attributes: Optional[List[DBSnapshotAttributeModel]] = Field(
        default=None, alias="DBSnapshotAttributes"
    )


class DescribeBlueGreenDeploymentsRequestModel(BaseModel):
    blue_green_deployment_identifier: Optional[str] = Field(
        default=None, alias="BlueGreenDeploymentIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeCertificatesMessageRequestModel(BaseModel):
    certificate_identifier: Optional[str] = Field(
        default=None, alias="CertificateIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBClusterBacktracksMessageRequestModel(BaseModel):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    backtrack_identifier: Optional[str] = Field(
        default=None, alias="BacktrackIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


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
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")


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
    include_all: Optional[bool] = Field(default=None, alias="IncludeAll")


class DescribeDBInstanceAutomatedBackupsMessageRequestModel(BaseModel):
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="DBInstanceAutomatedBackupsArn"
    )


class DescribeDBInstancesMessageRequestModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBLogFilesMessageRequestModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    filename_contains: Optional[str] = Field(default=None, alias="FilenameContains")
    file_last_written: Optional[int] = Field(default=None, alias="FileLastWritten")
    file_size: Optional[int] = Field(default=None, alias="FileSize")
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


class DescribeDBProxiesRequestModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeDBProxyEndpointsRequestModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    dbproxy_endpoint_name: Optional[str] = Field(
        default=None, alias="DBProxyEndpointName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeDBProxyTargetGroupsRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeDBProxyTargetsRequestModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeDBSecurityGroupsMessageRequestModel(BaseModel):
    dbsecurity_group_name: Optional[str] = Field(
        default=None, alias="DBSecurityGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDBSnapshotsMessageRequestModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")


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
            "blue-green-deployment",
            "custom-engine-version",
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-proxy",
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


class DescribeExportTasksMessageRequestModel(BaseModel):
    export_task_identifier: Optional[str] = Field(
        default=None, alias="ExportTaskIdentifier"
    )
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    source_type: Optional[Literal["CLUSTER", "SNAPSHOT"]] = Field(
        default=None, alias="SourceType"
    )


class DescribeGlobalClustersMessageRequestModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeOptionGroupOptionsMessageRequestModel(BaseModel):
    engine_name: str = Field(alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeOptionGroupsMessageRequestModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )


class DescribeOrderableDBInstanceOptionsMessageRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    availability_zone_group: Optional[str] = Field(
        default=None, alias="AvailabilityZoneGroup"
    )
    vpc: Optional[bool] = Field(default=None, alias="Vpc")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribePendingMaintenanceActionsMessageRequestModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeReservedDBInstancesMessageRequestModel(BaseModel):
    reserved_dbinstance_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstanceId"
    )
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    lease_id: Optional[str] = Field(default=None, alias="LeaseId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReservedDBInstancesOfferingsMessageRequestModel(BaseModel):
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeSourceRegionsMessageRequestModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListTagsForResourceMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeBlueGreenDeploymentsRequestDescribeBlueGreenDeploymentsPaginateModel(
    BaseModel
):
    blue_green_deployment_identifier: Optional[str] = Field(
        default=None, alias="BlueGreenDeploymentIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCertificatesMessageDescribeCertificatesPaginateModel(BaseModel):
    certificate_identifier: Optional[str] = Field(
        default=None, alias="CertificateIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClusterBacktracksMessageDescribeDBClusterBacktracksPaginateModel(
    BaseModel
):
    dbcluster_identifier: str = Field(alias="DBClusterIdentifier")
    backtrack_identifier: Optional[str] = Field(
        default=None, alias="BacktrackIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


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
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
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
    include_all: Optional[bool] = Field(default=None, alias="IncludeAll")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBInstanceAutomatedBackupsMessageDescribeDBInstanceAutomatedBackupsPaginateModel(
    BaseModel
):
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    dbinstance_automated_backups_arn: Optional[str] = Field(
        default=None, alias="DBInstanceAutomatedBackupsArn"
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


class DescribeDBLogFilesMessageDescribeDBLogFilesPaginateModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    filename_contains: Optional[str] = Field(default=None, alias="FilenameContains")
    file_last_written: Optional[int] = Field(default=None, alias="FileLastWritten")
    file_size: Optional[int] = Field(default=None, alias="FileSize")
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


class DescribeDBProxiesRequestDescribeDBProxiesPaginateModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBProxyEndpointsRequestDescribeDBProxyEndpointsPaginateModel(BaseModel):
    dbproxy_name: Optional[str] = Field(default=None, alias="DBProxyName")
    dbproxy_endpoint_name: Optional[str] = Field(
        default=None, alias="DBProxyEndpointName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBProxyTargetGroupsRequestDescribeDBProxyTargetGroupsPaginateModel(
    BaseModel
):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBProxyTargetsRequestDescribeDBProxyTargetsPaginateModel(BaseModel):
    dbproxy_name: str = Field(alias="DBProxyName")
    target_group_name: Optional[str] = Field(default=None, alias="TargetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBSecurityGroupsMessageDescribeDBSecurityGroupsPaginateModel(BaseModel):
    dbsecurity_group_name: Optional[str] = Field(
        default=None, alias="DBSecurityGroupName"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBSnapshotsMessageDescribeDBSnapshotsPaginateModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateModel(BaseModel):
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEngineDefaultClusterParametersMessageDescribeEngineDefaultClusterParametersPaginateModel(
    BaseModel
):
    dbparameter_group_family: str = Field(alias="DBParameterGroupFamily")
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
            "blue-green-deployment",
            "custom-engine-version",
            "db-cluster",
            "db-cluster-snapshot",
            "db-instance",
            "db-parameter-group",
            "db-proxy",
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


class DescribeExportTasksMessageDescribeExportTasksPaginateModel(BaseModel):
    export_task_identifier: Optional[str] = Field(
        default=None, alias="ExportTaskIdentifier"
    )
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    source_type: Optional[Literal["CLUSTER", "SNAPSHOT"]] = Field(
        default=None, alias="SourceType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateModel(BaseModel):
    global_cluster_identifier: Optional[str] = Field(
        default=None, alias="GlobalClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOptionGroupOptionsMessageDescribeOptionGroupOptionsPaginateModel(
    BaseModel
):
    engine_name: str = Field(alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOptionGroupsMessageDescribeOptionGroupsPaginateModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
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
    availability_zone_group: Optional[str] = Field(
        default=None, alias="AvailabilityZoneGroup"
    )
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


class DescribeReservedDBInstancesMessageDescribeReservedDBInstancesPaginateModel(
    BaseModel
):
    reserved_dbinstance_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstanceId"
    )
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    lease_id: Optional[str] = Field(default=None, alias="LeaseId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedDBInstancesOfferingsMessageDescribeReservedDBInstancesOfferingsPaginateModel(
    BaseModel
):
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    duration: Optional[str] = Field(default=None, alias="Duration")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSourceRegionsMessageDescribeSourceRegionsPaginateModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DownloadDBLogFilePortionMessageDownloadDBLogFilePortionPaginateModel(BaseModel):
    dbinstance_identifier: str = Field(alias="DBInstanceIdentifier")
    log_file_name: str = Field(alias="LogFileName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDBClusterSnapshotsMessageDBClusterSnapshotAvailableWaitModel(BaseModel):
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
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBClusterSnapshotsMessageDBClusterSnapshotDeletedWaitModel(BaseModel):
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
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBClustersMessageDBClusterAvailableWaitModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBClustersMessageDBClusterDeletedWaitModel(BaseModel):
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
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


class DescribeDBSnapshotsMessageDBSnapshotAvailableWaitModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBSnapshotsMessageDBSnapshotCompletedWaitModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBSnapshotsMessageDBSnapshotDeletedWaitModel(BaseModel):
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbsnapshot_identifier: Optional[str] = Field(
        default=None, alias="DBSnapshotIdentifier"
    )
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    include_shared: Optional[bool] = Field(default=None, alias="IncludeShared")
    include_public: Optional[bool] = Field(default=None, alias="IncludePublic")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDBLogFilesResponseModel(BaseModel):
    describe_dblog_files: List[DescribeDBLogFilesDetailsModel] = Field(
        alias="DescribeDBLogFiles"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventCategoriesMessageModel(BaseModel):
    event_categories_map_list: List[EventCategoriesMapModel] = Field(
        alias="EventCategoriesMapList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportTasksMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    export_tasks: List[ExportTaskModel] = Field(alias="ExportTasks")
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
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    global_cluster_members: Optional[List[GlobalClusterMemberModel]] = Field(
        default=None, alias="GlobalClusterMembers"
    )
    failover_state: Optional[FailoverStateModel] = Field(
        default=None, alias="FailoverState"
    )


class OptionGroupOptionSettingModel(BaseModel):
    setting_name: Optional[str] = Field(default=None, alias="SettingName")
    setting_description: Optional[str] = Field(default=None, alias="SettingDescription")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    apply_type: Optional[str] = Field(default=None, alias="ApplyType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    is_required: Optional[bool] = Field(default=None, alias="IsRequired")
    minimum_engine_version_per_allowed_value: Optional[
        List[MinimumEngineVersionPerAllowedValueModel]
    ] = Field(default=None, alias="MinimumEngineVersionPerAllowedValue")


class OptionConfigurationModel(BaseModel):
    option_name: str = Field(alias="OptionName")
    port: Optional[int] = Field(default=None, alias="Port")
    option_version: Optional[str] = Field(default=None, alias="OptionVersion")
    dbsecurity_group_memberships: Optional[Sequence[str]] = Field(
        default=None, alias="DBSecurityGroupMemberships"
    )
    vpc_security_group_memberships: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupMemberships"
    )
    option_settings: Optional[Sequence[OptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )


class OptionModel(BaseModel):
    option_name: Optional[str] = Field(default=None, alias="OptionName")
    option_description: Optional[str] = Field(default=None, alias="OptionDescription")
    persistent: Optional[bool] = Field(default=None, alias="Persistent")
    permanent: Optional[bool] = Field(default=None, alias="Permanent")
    port: Optional[int] = Field(default=None, alias="Port")
    option_version: Optional[str] = Field(default=None, alias="OptionVersion")
    option_settings: Optional[List[OptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    dbsecurity_group_memberships: Optional[
        List[DBSecurityGroupMembershipModel]
    ] = Field(default=None, alias="DBSecurityGroupMemberships")
    vpc_security_group_memberships: Optional[
        List[VpcSecurityGroupMembershipModel]
    ] = Field(default=None, alias="VpcSecurityGroupMemberships")


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_outpost: Optional[OutpostModel] = Field(default=None, alias="SubnetOutpost")
    subnet_status: Optional[str] = Field(default=None, alias="SubnetStatus")


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
    supports_storage_autoscaling: Optional[bool] = Field(
        default=None, alias="SupportsStorageAutoscaling"
    )
    provisioned_storage_throughput: Optional[List[RangeModel]] = Field(
        default=None, alias="ProvisionedStorageThroughput"
    )
    storage_throughput_to_iops_ratio: Optional[List[DoubleRangeModel]] = Field(
        default=None, alias="StorageThroughputToIopsRatio"
    )


class ReservedDBInstanceModel(BaseModel):
    reserved_dbinstance_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstanceId"
    )
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    dbinstance_count: Optional[int] = Field(default=None, alias="DBInstanceCount")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    state: Optional[str] = Field(default=None, alias="State")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )
    reserved_dbinstance_arn: Optional[str] = Field(
        default=None, alias="ReservedDBInstanceArn"
    )
    lease_id: Optional[str] = Field(default=None, alias="LeaseId")


class ReservedDBInstancesOfferingModel(BaseModel):
    reserved_dbinstances_offering_id: Optional[str] = Field(
        default=None, alias="ReservedDBInstancesOfferingId"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )


class SourceRegionMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    source_regions: List[SourceRegionModel] = Field(alias="SourceRegions")
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


class OrderableDBInstanceOptionsMessageModel(BaseModel):
    orderable_dbinstance_options: List[OrderableDBInstanceOptionModel] = Field(
        alias="OrderableDBInstanceOptions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBlueGreenDeploymentResponseModel(BaseModel):
    blue_green_deployment: BlueGreenDeploymentModel = Field(alias="BlueGreenDeployment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBlueGreenDeploymentResponseModel(BaseModel):
    blue_green_deployment: BlueGreenDeploymentModel = Field(alias="BlueGreenDeployment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBlueGreenDeploymentsResponseModel(BaseModel):
    blue_green_deployments: List[BlueGreenDeploymentModel] = Field(
        alias="BlueGreenDeployments"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SwitchoverBlueGreenDeploymentResponseModel(BaseModel):
    blue_green_deployment: BlueGreenDeploymentModel = Field(alias="BlueGreenDeployment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
    automatic_restart_time: Optional[datetime] = Field(
        default=None, alias="AutomaticRestartTime"
    )
    percent_progress: Optional[str] = Field(default=None, alias="PercentProgress")
    earliest_restorable_time: Optional[datetime] = Field(
        default=None, alias="EarliestRestorableTime"
    )
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    reader_endpoint: Optional[str] = Field(default=None, alias="ReaderEndpoint")
    custom_endpoints: Optional[List[str]] = Field(default=None, alias="CustomEndpoints")
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
    earliest_backtrack_time: Optional[datetime] = Field(
        default=None, alias="EarliestBacktrackTime"
    )
    backtrack_window: Optional[int] = Field(default=None, alias="BacktrackWindow")
    backtrack_consumed_change_records: Optional[int] = Field(
        default=None, alias="BacktrackConsumedChangeRecords"
    )
    enabled_cloudwatch_logs_exports: Optional[List[str]] = Field(
        default=None, alias="EnabledCloudwatchLogsExports"
    )
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
    scaling_configuration_info: Optional[ScalingConfigurationInfoModel] = Field(
        default=None, alias="ScalingConfigurationInfo"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    http_endpoint_enabled: Optional[bool] = Field(
        default=None, alias="HttpEndpointEnabled"
    )
    activity_stream_mode: Optional[Literal["async", "sync"]] = Field(
        default=None, alias="ActivityStreamMode"
    )
    activity_stream_status: Optional[
        Literal["started", "starting", "stopped", "stopping"]
    ] = Field(default=None, alias="ActivityStreamStatus")
    activity_stream_kms_key_id: Optional[str] = Field(
        default=None, alias="ActivityStreamKmsKeyId"
    )
    activity_stream_kinesis_stream_name: Optional[str] = Field(
        default=None, alias="ActivityStreamKinesisStreamName"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    cross_account_clone: Optional[bool] = Field(default=None, alias="CrossAccountClone")
    domain_memberships: Optional[List[DomainMembershipModel]] = Field(
        default=None, alias="DomainMemberships"
    )
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")
    global_write_forwarding_status: Optional[
        Literal["disabled", "disabling", "enabled", "enabling", "unknown"]
    ] = Field(default=None, alias="GlobalWriteForwardingStatus")
    global_write_forwarding_requested: Optional[bool] = Field(
        default=None, alias="GlobalWriteForwardingRequested"
    )
    pending_modified_values: Optional[ClusterPendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    dbcluster_instance_class: Optional[str] = Field(
        default=None, alias="DBClusterInstanceClass"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    performance_insights_enabled: Optional[bool] = Field(
        default=None, alias="PerformanceInsightsEnabled"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKMSKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    serverless_v2_scaling_configuration: Optional[
        ServerlessV2ScalingConfigurationInfoModel
    ] = Field(default=None, alias="ServerlessV2ScalingConfiguration")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    dbsystem_id: Optional[str] = Field(default=None, alias="DBSystemId")
    master_user_secret: Optional[MasterUserSecretModel] = Field(
        default=None, alias="MasterUserSecret"
    )


class DescribeDBProxyTargetGroupsResponseModel(BaseModel):
    target_groups: List[DBProxyTargetGroupModel] = Field(alias="TargetGroups")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBProxyTargetGroupResponseModel(BaseModel):
    dbproxy_target_group: DBProxyTargetGroupModel = Field(alias="DBProxyTargetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyDBSnapshotResultModel(BaseModel):
    dbsnapshot: DBSnapshotModel = Field(alias="DBSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBSnapshotResultModel(BaseModel):
    dbsnapshot: DBSnapshotModel = Field(alias="DBSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBSnapshotMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbsnapshots: List[DBSnapshotModel] = Field(alias="DBSnapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBSnapshotResultModel(BaseModel):
    dbsnapshot: DBSnapshotModel = Field(alias="DBSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBSnapshotResultModel(BaseModel):
    dbsnapshot: DBSnapshotModel = Field(alias="DBSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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


class DBEngineVersionMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbengine_versions: List[DBEngineVersionModel] = Field(alias="DBEngineVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBInstanceAutomatedBackupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbinstance_automated_backups: List[DBInstanceAutomatedBackupModel] = Field(
        alias="DBInstanceAutomatedBackups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBInstanceAutomatedBackupResultModel(BaseModel):
    dbinstance_automated_backup: DBInstanceAutomatedBackupModel = Field(
        alias="DBInstanceAutomatedBackup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDBInstanceAutomatedBackupsReplicationResultModel(BaseModel):
    dbinstance_automated_backup: DBInstanceAutomatedBackupModel = Field(
        alias="DBInstanceAutomatedBackup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDBInstanceAutomatedBackupsReplicationResultModel(BaseModel):
    dbinstance_automated_backup: DBInstanceAutomatedBackupModel = Field(
        alias="DBInstanceAutomatedBackup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDBProxyTargetsResponseModel(BaseModel):
    targets: List[DBProxyTargetModel] = Field(alias="Targets")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDBProxyTargetsResponseModel(BaseModel):
    dbproxy_targets: List[DBProxyTargetModel] = Field(alias="DBProxyTargets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBProxyResponseModel(BaseModel):
    dbproxy: DBProxyModel = Field(alias="DBProxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDBProxyResponseModel(BaseModel):
    dbproxy: DBProxyModel = Field(alias="DBProxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDBProxiesResponseModel(BaseModel):
    dbproxies: List[DBProxyModel] = Field(alias="DBProxies")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBProxyResponseModel(BaseModel):
    dbproxy: DBProxyModel = Field(alias="DBProxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizeDBSecurityGroupIngressResultModel(BaseModel):
    dbsecurity_group: DBSecurityGroupModel = Field(alias="DBSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDBSecurityGroupResultModel(BaseModel):
    dbsecurity_group: DBSecurityGroupModel = Field(alias="DBSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DBSecurityGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    dbsecurity_groups: List[DBSecurityGroupModel] = Field(alias="DBSecurityGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeDBSecurityGroupIngressResultModel(BaseModel):
    dbsecurity_group: DBSecurityGroupModel = Field(alias="DBSecurityGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDBSnapshotAttributesResultModel(BaseModel):
    dbsnapshot_attributes_result: DBSnapshotAttributesResultModel = Field(
        alias="DBSnapshotAttributesResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyDBSnapshotAttributeResultModel(BaseModel):
    dbsnapshot_attributes_result: DBSnapshotAttributesResultModel = Field(
        alias="DBSnapshotAttributesResult"
    )
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


class OptionGroupOptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )
    minimum_required_minor_engine_version: Optional[str] = Field(
        default=None, alias="MinimumRequiredMinorEngineVersion"
    )
    port_required: Optional[bool] = Field(default=None, alias="PortRequired")
    default_port: Optional[int] = Field(default=None, alias="DefaultPort")
    options_depended_on: Optional[List[str]] = Field(
        default=None, alias="OptionsDependedOn"
    )
    options_conflicts_with: Optional[List[str]] = Field(
        default=None, alias="OptionsConflictsWith"
    )
    persistent: Optional[bool] = Field(default=None, alias="Persistent")
    permanent: Optional[bool] = Field(default=None, alias="Permanent")
    requires_auto_minor_engine_version_upgrade: Optional[bool] = Field(
        default=None, alias="RequiresAutoMinorEngineVersionUpgrade"
    )
    vpc_only: Optional[bool] = Field(default=None, alias="VpcOnly")
    supports_option_version_downgrade: Optional[bool] = Field(
        default=None, alias="SupportsOptionVersionDowngrade"
    )
    option_group_option_settings: Optional[List[OptionGroupOptionSettingModel]] = Field(
        default=None, alias="OptionGroupOptionSettings"
    )
    option_group_option_versions: Optional[List[OptionVersionModel]] = Field(
        default=None, alias="OptionGroupOptionVersions"
    )
    copyable_cross_account: Optional[bool] = Field(
        default=None, alias="CopyableCrossAccount"
    )


class ModifyOptionGroupMessageRequestModel(BaseModel):
    option_group_name: str = Field(alias="OptionGroupName")
    options_to_include: Optional[Sequence[OptionConfigurationModel]] = Field(
        default=None, alias="OptionsToInclude"
    )
    options_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="OptionsToRemove"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")


class OptionGroupModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    option_group_description: Optional[str] = Field(
        default=None, alias="OptionGroupDescription"
    )
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    major_engine_version: Optional[str] = Field(
        default=None, alias="MajorEngineVersion"
    )
    options: Optional[List[OptionModel]] = Field(default=None, alias="Options")
    allows_vpc_and_non_vpc_instance_memberships: Optional[bool] = Field(
        default=None, alias="AllowsVpcAndNonVpcInstanceMemberships"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    option_group_arn: Optional[str] = Field(default=None, alias="OptionGroupArn")
    source_option_group: Optional[str] = Field(default=None, alias="SourceOptionGroup")
    source_account_id: Optional[str] = Field(default=None, alias="SourceAccountId")
    copy_timestamp: Optional[datetime] = Field(default=None, alias="CopyTimestamp")


class DBSubnetGroupModel(BaseModel):
    dbsubnet_group_name: Optional[str] = Field(default=None, alias="DBSubnetGroupName")
    dbsubnet_group_description: Optional[str] = Field(
        default=None, alias="DBSubnetGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_group_status: Optional[str] = Field(default=None, alias="SubnetGroupStatus")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    dbsubnet_group_arn: Optional[str] = Field(default=None, alias="DBSubnetGroupArn")
    supported_network_types: Optional[List[str]] = Field(
        default=None, alias="SupportedNetworkTypes"
    )


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
    valid_processor_features: Optional[List[AvailableProcessorFeatureModel]] = Field(
        default=None, alias="ValidProcessorFeatures"
    )


class PurchaseReservedDBInstancesOfferingResultModel(BaseModel):
    reserved_dbinstance: ReservedDBInstanceModel = Field(alias="ReservedDBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedDBInstanceMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_dbinstances: List[ReservedDBInstanceModel] = Field(
        alias="ReservedDBInstances"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedDBInstancesOfferingMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_dbinstances_offerings: List[ReservedDBInstancesOfferingModel] = Field(
        alias="ReservedDBInstancesOfferings"
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


class RebootDBClusterResultModel(BaseModel):
    dbcluster: DBClusterModel = Field(alias="DBCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBClusterFromS3ResultModel(BaseModel):
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


class OptionGroupOptionsMessageModel(BaseModel):
    option_group_options: List[OptionGroupOptionModel] = Field(
        alias="OptionGroupOptions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyOptionGroupResultModel(BaseModel):
    option_group: OptionGroupModel = Field(alias="OptionGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOptionGroupResultModel(BaseModel):
    option_group: OptionGroupModel = Field(alias="OptionGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyOptionGroupResultModel(BaseModel):
    option_group: OptionGroupModel = Field(alias="OptionGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OptionGroupsModel(BaseModel):
    option_groups_list: List[OptionGroupModel] = Field(alias="OptionGroupsList")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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
    automatic_restart_time: Optional[datetime] = Field(
        default=None, alias="AutomaticRestartTime"
    )
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
    replica_mode: Optional[Literal["mounted", "open-read-only"]] = Field(
        default=None, alias="ReplicaMode"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_memberships: Optional[List[OptionGroupMembershipModel]] = Field(
        default=None, alias="OptionGroupMemberships"
    )
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    nchar_character_set_name: Optional[str] = Field(
        default=None, alias="NcharCharacterSetName"
    )
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
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    enabled_cloudwatch_logs_exports: Optional[List[str]] = Field(
        default=None, alias="EnabledCloudwatchLogsExports"
    )
    processor_features: Optional[List[ProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    associated_roles: Optional[List[DBInstanceRoleModel]] = Field(
        default=None, alias="AssociatedRoles"
    )
    listener_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ListenerEndpoint"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")
    dbinstance_automated_backups_replications: Optional[
        List[DBInstanceAutomatedBackupsReplicationModel]
    ] = Field(default=None, alias="DBInstanceAutomatedBackupsReplications")
    customer_owned_ip_enabled: Optional[bool] = Field(
        default=None, alias="CustomerOwnedIpEnabled"
    )
    aws_backup_recovery_point_arn: Optional[str] = Field(
        default=None, alias="AwsBackupRecoveryPointArn"
    )
    activity_stream_status: Optional[
        Literal["started", "starting", "stopped", "stopping"]
    ] = Field(default=None, alias="ActivityStreamStatus")
    activity_stream_kms_key_id: Optional[str] = Field(
        default=None, alias="ActivityStreamKmsKeyId"
    )
    activity_stream_kinesis_stream_name: Optional[str] = Field(
        default=None, alias="ActivityStreamKinesisStreamName"
    )
    activity_stream_mode: Optional[Literal["async", "sync"]] = Field(
        default=None, alias="ActivityStreamMode"
    )
    activity_stream_engine_native_audit_fields_included: Optional[bool] = Field(
        default=None, alias="ActivityStreamEngineNativeAuditFieldsIncluded"
    )
    automation_mode: Optional[Literal["all-paused", "full"]] = Field(
        default=None, alias="AutomationMode"
    )
    resume_full_automation_mode_time: Optional[datetime] = Field(
        default=None, alias="ResumeFullAutomationModeTime"
    )
    custom_iam_instance_profile: Optional[str] = Field(
        default=None, alias="CustomIamInstanceProfile"
    )
    backup_target: Optional[str] = Field(default=None, alias="BackupTarget")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")
    activity_stream_policy_status: Optional[
        Literal["locked", "locking-policy", "unlocked", "unlocking-policy"]
    ] = Field(default=None, alias="ActivityStreamPolicyStatus")
    storage_throughput: Optional[int] = Field(default=None, alias="StorageThroughput")
    dbsystem_id: Optional[str] = Field(default=None, alias="DBSystemId")
    master_user_secret: Optional[MasterUserSecretModel] = Field(
        default=None, alias="MasterUserSecret"
    )
    certificate_details: Optional[CertificateDetailsModel] = Field(
        default=None, alias="CertificateDetails"
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


class CreateDBInstanceReadReplicaResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
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


class PromoteReadReplicaResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBInstanceFromDBSnapshotResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBInstanceFromS3ResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreDBInstanceToPointInTimeResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDBInstanceResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SwitchoverReadReplicaResultModel(BaseModel):
    dbinstance: DBInstanceModel = Field(alias="DBInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
