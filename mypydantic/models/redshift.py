# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptReservedNodeExchangeInputMessageRequestModel(BaseModel):
    reserved_node_id: str = Field(alias="ReservedNodeId")
    target_reserved_node_offering_id: str = Field(alias="TargetReservedNodeOfferingId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AttributeValueTargetModel(BaseModel):
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class AccountWithRestoreAccessModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    account_alias: Optional[str] = Field(default=None, alias="AccountAlias")


class AquaConfigurationModel(BaseModel):
    aqua_status: Optional[Literal["applying", "disabled", "enabled"]] = Field(
        default=None, alias="AquaStatus"
    )
    aqua_configuration_status: Optional[Literal["auto", "disabled", "enabled"]] = Field(
        default=None, alias="AquaConfigurationStatus"
    )


class AssociateDataShareConsumerMessageRequestModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")
    associate_entire_account: Optional[bool] = Field(
        default=None, alias="AssociateEntireAccount"
    )
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerArn")
    consumer_region: Optional[str] = Field(default=None, alias="ConsumerRegion")


class AuthenticationProfileModel(BaseModel):
    authentication_profile_name: Optional[str] = Field(
        default=None, alias="AuthenticationProfileName"
    )
    authentication_profile_content: Optional[str] = Field(
        default=None, alias="AuthenticationProfileContent"
    )


class AuthorizeClusterSecurityGroupIngressMessageRequestModel(BaseModel):
    cluster_security_group_name: str = Field(alias="ClusterSecurityGroupName")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class AuthorizeDataShareMessageRequestModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")
    consumer_identifier: str = Field(alias="ConsumerIdentifier")


class AuthorizeEndpointAccessMessageRequestModel(BaseModel):
    account: str = Field(alias="Account")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    vpc_ids: Optional[Sequence[str]] = Field(default=None, alias="VpcIds")


class AuthorizeSnapshotAccessMessageRequestModel(BaseModel):
    account_with_restore_access: str = Field(alias="AccountWithRestoreAccess")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )


class SupportedPlatformModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class DeleteClusterSnapshotMessageModel(BaseModel):
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )


class SnapshotErrorMessageModel(BaseModel):
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class BatchModifyClusterSnapshotsMessageRequestModel(BaseModel):
    snapshot_identifier_list: Sequence[str] = Field(alias="SnapshotIdentifierList")
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    force: Optional[bool] = Field(default=None, alias="Force")


class CancelResizeMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class ClusterAssociatedToScheduleModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    schedule_association_state: Optional[
        Literal["ACTIVE", "FAILED", "MODIFYING"]
    ] = Field(default=None, alias="ScheduleAssociationState")


class RevisionTargetModel(BaseModel):
    database_revision: Optional[str] = Field(default=None, alias="DatabaseRevision")
    description: Optional[str] = Field(default=None, alias="Description")
    database_revision_release_date: Optional[datetime] = Field(
        default=None, alias="DatabaseRevisionReleaseDate"
    )


class ClusterIamRoleModel(BaseModel):
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    apply_status: Optional[str] = Field(default=None, alias="ApplyStatus")


class ClusterNodeModel(BaseModel):
    node_role: Optional[str] = Field(default=None, alias="NodeRole")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIPAddress")
    public_ip_address: Optional[str] = Field(default=None, alias="PublicIPAddress")


class ParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    description: Optional[str] = Field(default=None, alias="Description")
    source: Optional[str] = Field(default=None, alias="Source")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    apply_type: Optional[Literal["dynamic", "static"]] = Field(
        default=None, alias="ApplyType"
    )
    is_modifiable: Optional[bool] = Field(default=None, alias="IsModifiable")
    minimum_engine_version: Optional[str] = Field(
        default=None, alias="MinimumEngineVersion"
    )


class ClusterParameterStatusModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    parameter_apply_error_description: Optional[str] = Field(
        default=None, alias="ParameterApplyErrorDescription"
    )


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ClusterSecurityGroupMembershipModel(BaseModel):
    cluster_security_group_name: Optional[str] = Field(
        default=None, alias="ClusterSecurityGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class ClusterSnapshotCopyStatusModel(BaseModel):
    destination_region: Optional[str] = Field(default=None, alias="DestinationRegion")
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )


class DataTransferProgressModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    current_rate_in_mega_bytes_per_second: Optional[float] = Field(
        default=None, alias="CurrentRateInMegaBytesPerSecond"
    )
    total_data_in_mega_bytes: Optional[int] = Field(
        default=None, alias="TotalDataInMegaBytes"
    )
    data_transferred_in_mega_bytes: Optional[int] = Field(
        default=None, alias="DataTransferredInMegaBytes"
    )
    estimated_time_to_completion_in_seconds: Optional[int] = Field(
        default=None, alias="EstimatedTimeToCompletionInSeconds"
    )
    elapsed_time_in_seconds: Optional[int] = Field(
        default=None, alias="ElapsedTimeInSeconds"
    )


class DeferredMaintenanceWindowModel(BaseModel):
    defer_maintenance_identifier: Optional[str] = Field(
        default=None, alias="DeferMaintenanceIdentifier"
    )
    defer_maintenance_start_time: Optional[datetime] = Field(
        default=None, alias="DeferMaintenanceStartTime"
    )
    defer_maintenance_end_time: Optional[datetime] = Field(
        default=None, alias="DeferMaintenanceEndTime"
    )


class ElasticIpStatusModel(BaseModel):
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    status: Optional[str] = Field(default=None, alias="Status")


class HsmStatusModel(BaseModel):
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class PendingModifiedValuesModel(BaseModel):
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    encryption_type: Optional[str] = Field(default=None, alias="EncryptionType")


class ReservedNodeExchangeStatusModel(BaseModel):
    reserved_node_exchange_request_id: Optional[str] = Field(
        default=None, alias="ReservedNodeExchangeRequestId"
    )
    status: Optional[
        Literal[
            "FAILED", "IN_PROGRESS", "PENDING", "REQUESTED", "RETRYING", "SUCCEEDED"
        ]
    ] = Field(default=None, alias="Status")
    request_time: Optional[datetime] = Field(default=None, alias="RequestTime")
    source_reserved_node_id: Optional[str] = Field(
        default=None, alias="SourceReservedNodeId"
    )
    source_reserved_node_type: Optional[str] = Field(
        default=None, alias="SourceReservedNodeType"
    )
    source_reserved_node_count: Optional[int] = Field(
        default=None, alias="SourceReservedNodeCount"
    )
    target_reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="TargetReservedNodeOfferingId"
    )
    target_reserved_node_type: Optional[str] = Field(
        default=None, alias="TargetReservedNodeType"
    )
    target_reserved_node_count: Optional[int] = Field(
        default=None, alias="TargetReservedNodeCount"
    )


class ResizeInfoModel(BaseModel):
    resize_type: Optional[str] = Field(default=None, alias="ResizeType")
    allow_cancel_resize: Optional[bool] = Field(default=None, alias="AllowCancelResize")


class RestoreStatusModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    current_restore_rate_in_mega_bytes_per_second: Optional[float] = Field(
        default=None, alias="CurrentRestoreRateInMegaBytesPerSecond"
    )
    snapshot_size_in_mega_bytes: Optional[int] = Field(
        default=None, alias="SnapshotSizeInMegaBytes"
    )
    progress_in_mega_bytes: Optional[int] = Field(
        default=None, alias="ProgressInMegaBytes"
    )
    elapsed_time_in_seconds: Optional[int] = Field(
        default=None, alias="ElapsedTimeInSeconds"
    )
    estimated_time_to_completion_in_seconds: Optional[int] = Field(
        default=None, alias="EstimatedTimeToCompletionInSeconds"
    )


class VpcSecurityGroupMembershipModel(BaseModel):
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="VpcSecurityGroupId"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class ClusterVersionModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    cluster_parameter_group_family: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupFamily"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CopyClusterSnapshotMessageRequestModel(BaseModel):
    source_snapshot_identifier: str = Field(alias="SourceSnapshotIdentifier")
    target_snapshot_identifier: str = Field(alias="TargetSnapshotIdentifier")
    source_snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SourceSnapshotClusterIdentifier"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )


class CreateAuthenticationProfileMessageRequestModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")
    authentication_profile_content: str = Field(alias="AuthenticationProfileContent")


class CreateEndpointAccessMessageRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    subnet_group_name: str = Field(alias="SubnetGroupName")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )


class DataShareAssociationModel(BaseModel):
    consumer_identifier: Optional[str] = Field(default=None, alias="ConsumerIdentifier")
    status: Optional[
        Literal[
            "ACTIVE",
            "AUTHORIZED",
            "AVAILABLE",
            "DEAUTHORIZED",
            "PENDING_AUTHORIZATION",
            "REJECTED",
        ]
    ] = Field(default=None, alias="Status")
    consumer_region: Optional[str] = Field(default=None, alias="ConsumerRegion")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    status_change_date: Optional[datetime] = Field(
        default=None, alias="StatusChangeDate"
    )


class DeauthorizeDataShareMessageRequestModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")
    consumer_identifier: str = Field(alias="ConsumerIdentifier")


class DeleteAuthenticationProfileMessageRequestModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")


class DeleteClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    skip_final_cluster_snapshot: Optional[bool] = Field(
        default=None, alias="SkipFinalClusterSnapshot"
    )
    final_cluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="FinalClusterSnapshotIdentifier"
    )
    final_cluster_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="FinalClusterSnapshotRetentionPeriod"
    )


class DeleteClusterParameterGroupMessageRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")


class DeleteClusterSecurityGroupMessageRequestModel(BaseModel):
    cluster_security_group_name: str = Field(alias="ClusterSecurityGroupName")


class DeleteClusterSnapshotMessageRequestModel(BaseModel):
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )


class DeleteClusterSubnetGroupMessageRequestModel(BaseModel):
    cluster_subnet_group_name: str = Field(alias="ClusterSubnetGroupName")


class DeleteEndpointAccessMessageRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class DeleteEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")


class DeleteHsmClientCertificateMessageRequestModel(BaseModel):
    hsm_client_certificate_identifier: str = Field(
        alias="HsmClientCertificateIdentifier"
    )


class DeleteHsmConfigurationMessageRequestModel(BaseModel):
    hsm_configuration_identifier: str = Field(alias="HsmConfigurationIdentifier")


class DeleteScheduledActionMessageRequestModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")


class DeleteSnapshotCopyGrantMessageRequestModel(BaseModel):
    snapshot_copy_grant_name: str = Field(alias="SnapshotCopyGrantName")


class DeleteSnapshotScheduleMessageRequestModel(BaseModel):
    schedule_identifier: str = Field(alias="ScheduleIdentifier")


class DeleteTagsMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DeleteUsageLimitMessageRequestModel(BaseModel):
    usage_limit_id: str = Field(alias="UsageLimitId")


class DescribeAccountAttributesMessageRequestModel(BaseModel):
    attribute_names: Optional[Sequence[str]] = Field(
        default=None, alias="AttributeNames"
    )


class DescribeAuthenticationProfilesMessageRequestModel(BaseModel):
    authentication_profile_name: Optional[str] = Field(
        default=None, alias="AuthenticationProfileName"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeClusterDbRevisionsMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeClusterParameterGroupsMessageRequestModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeClusterParametersMessageRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeClusterSecurityGroupsMessageRequestModel(BaseModel):
    cluster_security_group_name: Optional[str] = Field(
        default=None, alias="ClusterSecurityGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class SnapshotSortingEntityModel(BaseModel):
    attribute: Literal["CREATE_TIME", "SOURCE_TYPE", "TOTAL_SIZE"] = Field(
        alias="Attribute"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="SortOrder"
    )


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeClusterSubnetGroupsMessageRequestModel(BaseModel):
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeClusterTracksMessageRequestModel(BaseModel):
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeClusterVersionsMessageRequestModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    cluster_parameter_group_family: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupFamily"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeClustersMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeDataSharesForConsumerMessageRequestModel(BaseModel):
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerArn")
    status: Optional[Literal["ACTIVE", "AVAILABLE"]] = Field(
        default=None, alias="Status"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDataSharesForProducerMessageRequestModel(BaseModel):
    producer_arn: Optional[str] = Field(default=None, alias="ProducerArn")
    status: Optional[
        Literal[
            "ACTIVE", "AUTHORIZED", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"
        ]
    ] = Field(default=None, alias="Status")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDataSharesMessageRequestModel(BaseModel):
    data_share_arn: Optional[str] = Field(default=None, alias="DataShareArn")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDefaultClusterParametersMessageRequestModel(BaseModel):
    parameter_group_family: str = Field(alias="ParameterGroupFamily")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEndpointAccessMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEndpointAuthorizationMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    account: Optional[str] = Field(default=None, alias="Account")
    grantee: Optional[bool] = Field(default=None, alias="Grantee")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventCategoriesMessageRequestModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")


class DescribeEventSubscriptionsMessageRequestModel(BaseModel):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeEventsMessageRequestModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeHsmClientCertificatesMessageRequestModel(BaseModel):
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeHsmConfigurationsMessageRequestModel(BaseModel):
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeLoggingStatusMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class NodeConfigurationOptionsFilterModel(BaseModel):
    name: Optional[
        Literal["EstimatedDiskUtilizationPercent", "Mode", "NodeType", "NumberOfNodes"]
    ] = Field(default=None, alias="Name")
    operator: Optional[Literal["between", "eq", "ge", "gt", "in", "le", "lt"]] = Field(
        default=None, alias="Operator"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DescribeOrderableClusterOptionsMessageRequestModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribePartnersInputMessageRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    partner_name: Optional[str] = Field(default=None, alias="PartnerName")


class PartnerIntegrationInfoModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    partner_name: Optional[str] = Field(default=None, alias="PartnerName")
    status: Optional[
        Literal["Active", "ConnectionFailure", "Inactive", "RuntimeFailure"]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class DescribeReservedNodeExchangeStatusInputMessageRequestModel(BaseModel):
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    reserved_node_exchange_request_id: Optional[str] = Field(
        default=None, alias="ReservedNodeExchangeRequestId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReservedNodeOfferingsMessageRequestModel(BaseModel):
    reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodeOfferingId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReservedNodesMessageRequestModel(BaseModel):
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeResizeMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class ScheduledActionFilterModel(BaseModel):
    name: Literal["cluster-identifier", "iam-role"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class DescribeSnapshotCopyGrantsMessageRequestModel(BaseModel):
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeSnapshotSchedulesMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    schedule_identifier: Optional[str] = Field(default=None, alias="ScheduleIdentifier")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeTableRestoreStatusMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    table_restore_request_id: Optional[str] = Field(
        default=None, alias="TableRestoreRequestId"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeTagsMessageRequestModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DescribeUsageLimitsMessageRequestModel(BaseModel):
    usage_limit_id: Optional[str] = Field(default=None, alias="UsageLimitId")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    feature_type: Optional[
        Literal["concurrency-scaling", "cross-region-datasharing", "spectrum"]
    ] = Field(default=None, alias="FeatureType")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")


class DisableLoggingMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class DisableSnapshotCopyMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class DisassociateDataShareConsumerMessageRequestModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")
    disassociate_entire_account: Optional[bool] = Field(
        default=None, alias="DisassociateEntireAccount"
    )
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerArn")
    consumer_region: Optional[str] = Field(default=None, alias="ConsumerRegion")


class EnableLoggingMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    log_destination_type: Optional[Literal["cloudwatch", "s3"]] = Field(
        default=None, alias="LogDestinationType"
    )
    log_exports: Optional[Sequence[str]] = Field(default=None, alias="LogExports")


class EnableSnapshotCopyMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    destination_region: str = Field(alias="DestinationRegion")
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )


class EndpointAuthorizationModel(BaseModel):
    grantor: Optional[str] = Field(default=None, alias="Grantor")
    grantee: Optional[str] = Field(default=None, alias="Grantee")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    authorize_time: Optional[datetime] = Field(default=None, alias="AuthorizeTime")
    cluster_status: Optional[str] = Field(default=None, alias="ClusterStatus")
    status: Optional[Literal["Authorized", "Revoking"]] = Field(
        default=None, alias="Status"
    )
    allowed_all_vp_cs: Optional[bool] = Field(default=None, alias="AllowedAllVPCs")
    allowed_vp_cs: Optional[List[str]] = Field(default=None, alias="AllowedVPCs")
    endpoint_count: Optional[int] = Field(default=None, alias="EndpointCount")


class EventInfoMapModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")
    event_description: Optional[str] = Field(default=None, alias="EventDescription")
    severity: Optional[str] = Field(default=None, alias="Severity")


class EventModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")
    severity: Optional[str] = Field(default=None, alias="Severity")
    date: Optional[datetime] = Field(default=None, alias="Date")
    event_id: Optional[str] = Field(default=None, alias="EventId")


class GetClusterCredentialsMessageRequestModel(BaseModel):
    db_user: str = Field(alias="DbUser")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    db_name: Optional[str] = Field(default=None, alias="DbName")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    auto_create: Optional[bool] = Field(default=None, alias="AutoCreate")
    db_groups: Optional[Sequence[str]] = Field(default=None, alias="DbGroups")


class GetClusterCredentialsWithIAMMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    db_name: Optional[str] = Field(default=None, alias="DbName")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")


class GetReservedNodeExchangeConfigurationOptionsInputMessageRequestModel(BaseModel):
    action_type: Literal["resize-cluster", "restore-cluster"] = Field(
        alias="ActionType"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GetReservedNodeExchangeOfferingsInputMessageRequestModel(BaseModel):
    reserved_node_id: str = Field(alias="ReservedNodeId")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ModifyAquaInputMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    aqua_configuration_status: Optional[Literal["auto", "disabled", "enabled"]] = Field(
        default=None, alias="AquaConfigurationStatus"
    )


class ModifyAuthenticationProfileMessageRequestModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")
    authentication_profile_content: str = Field(alias="AuthenticationProfileContent")


class ModifyClusterDbRevisionMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    revision_target: str = Field(alias="RevisionTarget")


class ModifyClusterIamRolesMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    add_iam_roles: Optional[Sequence[str]] = Field(default=None, alias="AddIamRoles")
    remove_iam_roles: Optional[Sequence[str]] = Field(
        default=None, alias="RemoveIamRoles"
    )
    default_iam_role_arn: Optional[str] = Field(default=None, alias="DefaultIamRoleArn")


class ModifyClusterMaintenanceMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    defer_maintenance: Optional[bool] = Field(default=None, alias="DeferMaintenance")
    defer_maintenance_identifier: Optional[str] = Field(
        default=None, alias="DeferMaintenanceIdentifier"
    )
    defer_maintenance_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DeferMaintenanceStartTime"
    )
    defer_maintenance_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DeferMaintenanceEndTime"
    )
    defer_maintenance_duration: Optional[int] = Field(
        default=None, alias="DeferMaintenanceDuration"
    )


class ModifyClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    cluster_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="ClusterSecurityGroups"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    cluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupName"
    )
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    allow_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowVersionUpgrade"
    )
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    new_cluster_identifier: Optional[str] = Field(
        default=None, alias="NewClusterIdentifier"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    availability_zone_relocation: Optional[bool] = Field(
        default=None, alias="AvailabilityZoneRelocation"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    port: Optional[int] = Field(default=None, alias="Port")


class ModifyClusterSnapshotMessageRequestModel(BaseModel):
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    force: Optional[bool] = Field(default=None, alias="Force")


class ModifyClusterSnapshotScheduleMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    schedule_identifier: Optional[str] = Field(default=None, alias="ScheduleIdentifier")
    disassociate_schedule: Optional[bool] = Field(
        default=None, alias="DisassociateSchedule"
    )


class ModifyClusterSubnetGroupMessageRequestModel(BaseModel):
    cluster_subnet_group_name: str = Field(alias="ClusterSubnetGroupName")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    description: Optional[str] = Field(default=None, alias="Description")


class ModifyEndpointAccessMessageRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )


class ModifyEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_ids: Optional[Sequence[str]] = Field(default=None, alias="SourceIds")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    severity: Optional[str] = Field(default=None, alias="Severity")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ModifySnapshotCopyRetentionPeriodMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    retention_period: int = Field(alias="RetentionPeriod")
    manual: Optional[bool] = Field(default=None, alias="Manual")


class ModifySnapshotScheduleMessageRequestModel(BaseModel):
    schedule_identifier: str = Field(alias="ScheduleIdentifier")
    schedule_definitions: Sequence[str] = Field(alias="ScheduleDefinitions")


class ModifyUsageLimitMessageRequestModel(BaseModel):
    usage_limit_id: str = Field(alias="UsageLimitId")
    amount: Optional[int] = Field(default=None, alias="Amount")
    breach_action: Optional[Literal["disable", "emit-metric", "log"]] = Field(
        default=None, alias="BreachAction"
    )


class NetworkInterfaceModel(BaseModel):
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")


class NodeConfigurationOptionModel(BaseModel):
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    estimated_disk_utilization_percent: Optional[float] = Field(
        default=None, alias="EstimatedDiskUtilizationPercent"
    )
    mode: Optional[Literal["high-performance", "standard"]] = Field(
        default=None, alias="Mode"
    )


class PartnerIntegrationInputMessageRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    database_name: str = Field(alias="DatabaseName")
    partner_name: str = Field(alias="PartnerName")


class PauseClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class PauseClusterMessageModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class PurchaseReservedNodeOfferingMessageRequestModel(BaseModel):
    reserved_node_offering_id: str = Field(alias="ReservedNodeOfferingId")
    node_count: Optional[int] = Field(default=None, alias="NodeCount")


class RebootClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class RejectDataShareMessageRequestModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")


class ResizeClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    classic: Optional[bool] = Field(default=None, alias="Classic")
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    target_reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="TargetReservedNodeOfferingId"
    )


class ResizeClusterMessageModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    classic: Optional[bool] = Field(default=None, alias="Classic")
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    target_reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="TargetReservedNodeOfferingId"
    )


class RestoreFromClusterSnapshotMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    allow_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowVersionUpgrade"
    )
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    cluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupName"
    )
    cluster_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="ClusterSecurityGroups"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    additional_info: Optional[str] = Field(default=None, alias="AdditionalInfo")
    iam_roles: Optional[Sequence[str]] = Field(default=None, alias="IamRoles")
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    snapshot_schedule_identifier: Optional[str] = Field(
        default=None, alias="SnapshotScheduleIdentifier"
    )
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    availability_zone_relocation: Optional[bool] = Field(
        default=None, alias="AvailabilityZoneRelocation"
    )
    aqua_configuration_status: Optional[Literal["auto", "disabled", "enabled"]] = Field(
        default=None, alias="AquaConfigurationStatus"
    )
    default_iam_role_arn: Optional[str] = Field(default=None, alias="DefaultIamRoleArn")
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    target_reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="TargetReservedNodeOfferingId"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")


class RestoreTableFromClusterSnapshotMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    source_database_name: str = Field(alias="SourceDatabaseName")
    source_table_name: str = Field(alias="SourceTableName")
    new_table_name: str = Field(alias="NewTableName")
    source_schema_name: Optional[str] = Field(default=None, alias="SourceSchemaName")
    target_database_name: Optional[str] = Field(
        default=None, alias="TargetDatabaseName"
    )
    target_schema_name: Optional[str] = Field(default=None, alias="TargetSchemaName")
    enable_case_sensitive_identifier: Optional[bool] = Field(
        default=None, alias="EnableCaseSensitiveIdentifier"
    )


class TableRestoreStatusModel(BaseModel):
    table_restore_request_id: Optional[str] = Field(
        default=None, alias="TableRestoreRequestId"
    )
    status: Optional[
        Literal["CANCELED", "FAILED", "IN_PROGRESS", "PENDING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    request_time: Optional[datetime] = Field(default=None, alias="RequestTime")
    progress_in_mega_bytes: Optional[int] = Field(
        default=None, alias="ProgressInMegaBytes"
    )
    total_data_in_mega_bytes: Optional[int] = Field(
        default=None, alias="TotalDataInMegaBytes"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    source_database_name: Optional[str] = Field(
        default=None, alias="SourceDatabaseName"
    )
    source_schema_name: Optional[str] = Field(default=None, alias="SourceSchemaName")
    source_table_name: Optional[str] = Field(default=None, alias="SourceTableName")
    target_database_name: Optional[str] = Field(
        default=None, alias="TargetDatabaseName"
    )
    target_schema_name: Optional[str] = Field(default=None, alias="TargetSchemaName")
    new_table_name: Optional[str] = Field(default=None, alias="NewTableName")


class ResumeClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class ResumeClusterMessageModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class RevokeClusterSecurityGroupIngressMessageRequestModel(BaseModel):
    cluster_security_group_name: str = Field(alias="ClusterSecurityGroupName")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )


class RevokeEndpointAccessMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    account: Optional[str] = Field(default=None, alias="Account")
    vpc_ids: Optional[Sequence[str]] = Field(default=None, alias="VpcIds")
    force: Optional[bool] = Field(default=None, alias="Force")


class RevokeSnapshotAccessMessageRequestModel(BaseModel):
    account_with_restore_access: str = Field(alias="AccountWithRestoreAccess")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_cluster_identifier: Optional[str] = Field(
        default=None, alias="SnapshotClusterIdentifier"
    )


class RotateEncryptionKeyMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")


class SupportedOperationModel(BaseModel):
    operation_name: Optional[str] = Field(default=None, alias="OperationName")


class UpdatePartnerStatusInputMessageRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    database_name: str = Field(alias="DatabaseName")
    partner_name: str = Field(alias="PartnerName")
    status: Literal[
        "Active", "ConnectionFailure", "Inactive", "RuntimeFailure"
    ] = Field(alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ClusterCredentialsModel(BaseModel):
    db_user: str = Field(alias="DbUser")
    db_password: str = Field(alias="DbPassword")
    expiration: datetime = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterExtendedCredentialsModel(BaseModel):
    db_user: str = Field(alias="DbUser")
    db_password: str = Field(alias="DbPassword")
    expiration: datetime = Field(alias="Expiration")
    next_refresh_time: datetime = Field(alias="NextRefreshTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterParameterGroupNameMessageModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    parameter_group_status: str = Field(alias="ParameterGroupStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAuthenticationProfileResultModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")
    authentication_profile_content: str = Field(alias="AuthenticationProfileContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomerStorageMessageModel(BaseModel):
    total_backup_size_in_mega_bytes: float = Field(alias="TotalBackupSizeInMegaBytes")
    total_provisioned_storage_in_mega_bytes: float = Field(
        alias="TotalProvisionedStorageInMegaBytes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAuthenticationProfileResultModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointAuthorizationResponseMetadataModel(BaseModel):
    grantor: str = Field(alias="Grantor")
    grantee: str = Field(alias="Grantee")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    authorize_time: datetime = Field(alias="AuthorizeTime")
    cluster_status: str = Field(alias="ClusterStatus")
    status: Literal["Authorized", "Revoking"] = Field(alias="Status")
    allowed_all_vp_cs: bool = Field(alias="AllowedAllVPCs")
    allowed_vp_cs: List[str] = Field(alias="AllowedVPCs")
    endpoint_count: int = Field(alias="EndpointCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingStatusModel(BaseModel):
    logging_enabled: bool = Field(alias="LoggingEnabled")
    bucket_name: str = Field(alias="BucketName")
    s3_key_prefix: str = Field(alias="S3KeyPrefix")
    last_successful_delivery_time: datetime = Field(alias="LastSuccessfulDeliveryTime")
    last_failure_time: datetime = Field(alias="LastFailureTime")
    last_failure_message: str = Field(alias="LastFailureMessage")
    log_destination_type: Literal["cloudwatch", "s3"] = Field(
        alias="LogDestinationType"
    )
    log_exports: List[str] = Field(alias="LogExports")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyAuthenticationProfileResultModel(BaseModel):
    authentication_profile_name: str = Field(alias="AuthenticationProfileName")
    authentication_profile_content: str = Field(alias="AuthenticationProfileContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PartnerIntegrationOutputMessageModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    partner_name: str = Field(alias="PartnerName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResizeProgressMessageModel(BaseModel):
    target_node_type: str = Field(alias="TargetNodeType")
    target_number_of_nodes: int = Field(alias="TargetNumberOfNodes")
    target_cluster_type: str = Field(alias="TargetClusterType")
    status: str = Field(alias="Status")
    import_tables_completed: List[str] = Field(alias="ImportTablesCompleted")
    import_tables_in_progress: List[str] = Field(alias="ImportTablesInProgress")
    import_tables_not_started: List[str] = Field(alias="ImportTablesNotStarted")
    avg_resize_rate_in_mega_bytes_per_second: float = Field(
        alias="AvgResizeRateInMegaBytesPerSecond"
    )
    total_resize_data_in_mega_bytes: int = Field(alias="TotalResizeDataInMegaBytes")
    progress_in_mega_bytes: int = Field(alias="ProgressInMegaBytes")
    elapsed_time_in_seconds: int = Field(alias="ElapsedTimeInSeconds")
    estimated_time_to_completion_in_seconds: int = Field(
        alias="EstimatedTimeToCompletionInSeconds"
    )
    resize_type: str = Field(alias="ResizeType")
    message: str = Field(alias="Message")
    target_encryption_type: str = Field(alias="TargetEncryptionType")
    data_transfer_progress_percent: float = Field(alias="DataTransferProgressPercent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccountAttributeModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_values: Optional[List[AttributeValueTargetModel]] = Field(
        default=None, alias="AttributeValues"
    )


class ModifyAquaOutputMessageModel(BaseModel):
    aqua_configuration: AquaConfigurationModel = Field(alias="AquaConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAuthenticationProfilesResultModel(BaseModel):
    authentication_profiles: List[AuthenticationProfileModel] = Field(
        alias="AuthenticationProfiles"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    supported_platforms: Optional[List[SupportedPlatformModel]] = Field(
        default=None, alias="SupportedPlatforms"
    )


class BatchDeleteClusterSnapshotsRequestModel(BaseModel):
    identifiers: Sequence[DeleteClusterSnapshotMessageModel] = Field(
        alias="Identifiers"
    )


class BatchDeleteClusterSnapshotsResultModel(BaseModel):
    resources: List[str] = Field(alias="Resources")
    errors: List[SnapshotErrorMessageModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchModifyClusterSnapshotsOutputMessageModel(BaseModel):
    resources: List[str] = Field(alias="Resources")
    errors: List[SnapshotErrorMessageModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterDbRevisionModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    current_database_revision: Optional[str] = Field(
        default=None, alias="CurrentDatabaseRevision"
    )
    database_revision_release_date: Optional[datetime] = Field(
        default=None, alias="DatabaseRevisionReleaseDate"
    )
    revision_targets: Optional[List[RevisionTargetModel]] = Field(
        default=None, alias="RevisionTargets"
    )


class ClusterParameterGroupDetailsModel(BaseModel):
    parameters: List[ParameterModel] = Field(alias="Parameters")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefaultClusterParametersModel(BaseModel):
    parameter_group_family: Optional[str] = Field(
        default=None, alias="ParameterGroupFamily"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    parameters: Optional[List[ParameterModel]] = Field(default=None, alias="Parameters")


class ModifyClusterParameterGroupMessageRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    parameters: Sequence[ParameterModel] = Field(alias="Parameters")


class ResetClusterParameterGroupMessageRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    reset_all_parameters: Optional[bool] = Field(
        default=None, alias="ResetAllParameters"
    )
    parameters: Optional[Sequence[ParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class ClusterParameterGroupStatusModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    cluster_parameter_status_list: Optional[List[ClusterParameterStatusModel]] = Field(
        default=None, alias="ClusterParameterStatusList"
    )


class ClusterParameterGroupModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    parameter_group_family: Optional[str] = Field(
        default=None, alias="ParameterGroupFamily"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateClusterMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    node_type: str = Field(alias="NodeType")
    master_username: str = Field(alias="MasterUsername")
    master_user_password: str = Field(alias="MasterUserPassword")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    cluster_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="ClusterSecurityGroups"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    cluster_parameter_group_name: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupName"
    )
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    allow_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowVersionUpgrade"
    )
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    additional_info: Optional[str] = Field(default=None, alias="AdditionalInfo")
    iam_roles: Optional[Sequence[str]] = Field(default=None, alias="IamRoles")
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    snapshot_schedule_identifier: Optional[str] = Field(
        default=None, alias="SnapshotScheduleIdentifier"
    )
    availability_zone_relocation: Optional[bool] = Field(
        default=None, alias="AvailabilityZoneRelocation"
    )
    aqua_configuration_status: Optional[Literal["auto", "disabled", "enabled"]] = Field(
        default=None, alias="AquaConfigurationStatus"
    )
    default_iam_role_arn: Optional[str] = Field(default=None, alias="DefaultIamRoleArn")
    load_sample_data: Optional[str] = Field(default=None, alias="LoadSampleData")


class CreateClusterParameterGroupMessageRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    parameter_group_family: str = Field(alias="ParameterGroupFamily")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateClusterSecurityGroupMessageRequestModel(BaseModel):
    cluster_security_group_name: str = Field(alias="ClusterSecurityGroupName")
    description: str = Field(alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateClusterSnapshotMessageRequestModel(BaseModel):
    snapshot_identifier: str = Field(alias="SnapshotIdentifier")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateClusterSubnetGroupMessageRequestModel(BaseModel):
    cluster_subnet_group_name: str = Field(alias="ClusterSubnetGroupName")
    description: str = Field(alias="Description")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_ids: Optional[Sequence[str]] = Field(default=None, alias="SourceIds")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    severity: Optional[str] = Field(default=None, alias="Severity")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateHsmClientCertificateMessageRequestModel(BaseModel):
    hsm_client_certificate_identifier: str = Field(
        alias="HsmClientCertificateIdentifier"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateHsmConfigurationMessageRequestModel(BaseModel):
    hsm_configuration_identifier: str = Field(alias="HsmConfigurationIdentifier")
    description: str = Field(alias="Description")
    hsm_ip_address: str = Field(alias="HsmIpAddress")
    hsm_partition_name: str = Field(alias="HsmPartitionName")
    hsm_partition_password: str = Field(alias="HsmPartitionPassword")
    hsm_server_public_certificate: str = Field(alias="HsmServerPublicCertificate")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotCopyGrantMessageRequestModel(BaseModel):
    snapshot_copy_grant_name: str = Field(alias="SnapshotCopyGrantName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotScheduleMessageRequestModel(BaseModel):
    schedule_definitions: Optional[Sequence[str]] = Field(
        default=None, alias="ScheduleDefinitions"
    )
    schedule_identifier: Optional[str] = Field(default=None, alias="ScheduleIdentifier")
    schedule_description: Optional[str] = Field(
        default=None, alias="ScheduleDescription"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    next_invocations: Optional[int] = Field(default=None, alias="NextInvocations")


class CreateTagsMessageRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateUsageLimitMessageRequestModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    feature_type: Literal[
        "concurrency-scaling", "cross-region-datasharing", "spectrum"
    ] = Field(alias="FeatureType")
    limit_type: Literal["data-scanned", "time"] = Field(alias="LimitType")
    amount: int = Field(alias="Amount")
    period: Optional[Literal["daily", "monthly", "weekly"]] = Field(
        default=None, alias="Period"
    )
    breach_action: Optional[Literal["disable", "emit-metric", "log"]] = Field(
        default=None, alias="BreachAction"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class EC2SecurityGroupModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupName"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="EC2SecurityGroupOwnerId"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class EventSubscriptionModel(BaseModel):
    customer_aws_id: Optional[str] = Field(default=None, alias="CustomerAwsId")
    cust_subscription_id: Optional[str] = Field(
        default=None, alias="CustSubscriptionId"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    status: Optional[str] = Field(default=None, alias="Status")
    subscription_creation_time: Optional[datetime] = Field(
        default=None, alias="SubscriptionCreationTime"
    )
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_ids_list: Optional[List[str]] = Field(default=None, alias="SourceIdsList")
    event_categories_list: Optional[List[str]] = Field(
        default=None, alias="EventCategoriesList"
    )
    severity: Optional[str] = Field(default=None, alias="Severity")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class HsmClientCertificateModel(BaseModel):
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_client_certificate_public_key: Optional[str] = Field(
        default=None, alias="HsmClientCertificatePublicKey"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class HsmConfigurationModel(BaseModel):
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    hsm_ip_address: Optional[str] = Field(default=None, alias="HsmIpAddress")
    hsm_partition_name: Optional[str] = Field(default=None, alias="HsmPartitionName")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class IPRangeModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    cidrip: Optional[str] = Field(default=None, alias="CIDRIP")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class SnapshotCopyGrantModel(BaseModel):
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class SnapshotScheduleResponseMetadataModel(BaseModel):
    schedule_definitions: List[str] = Field(alias="ScheduleDefinitions")
    schedule_identifier: str = Field(alias="ScheduleIdentifier")
    schedule_description: str = Field(alias="ScheduleDescription")
    tags: List[TagModel] = Field(alias="Tags")
    next_invocations: List[datetime] = Field(alias="NextInvocations")
    associated_cluster_count: int = Field(alias="AssociatedClusterCount")
    associated_clusters: List[ClusterAssociatedToScheduleModel] = Field(
        alias="AssociatedClusters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SnapshotScheduleModel(BaseModel):
    schedule_definitions: Optional[List[str]] = Field(
        default=None, alias="ScheduleDefinitions"
    )
    schedule_identifier: Optional[str] = Field(default=None, alias="ScheduleIdentifier")
    schedule_description: Optional[str] = Field(
        default=None, alias="ScheduleDescription"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    next_invocations: Optional[List[datetime]] = Field(
        default=None, alias="NextInvocations"
    )
    associated_cluster_count: Optional[int] = Field(
        default=None, alias="AssociatedClusterCount"
    )
    associated_clusters: Optional[List[ClusterAssociatedToScheduleModel]] = Field(
        default=None, alias="AssociatedClusters"
    )


class SnapshotModel(BaseModel):
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_create_time: Optional[datetime] = Field(
        default=None, alias="SnapshotCreateTime"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    cluster_create_time: Optional[datetime] = Field(
        default=None, alias="ClusterCreateTime"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    engine_full_version: Optional[str] = Field(default=None, alias="EngineFullVersion")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    encrypted_with_hs_m: Optional[bool] = Field(default=None, alias="EncryptedWithHSM")
    accounts_with_restore_access: Optional[List[AccountWithRestoreAccessModel]] = Field(
        default=None, alias="AccountsWithRestoreAccess"
    )
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    total_backup_size_in_mega_bytes: Optional[float] = Field(
        default=None, alias="TotalBackupSizeInMegaBytes"
    )
    actual_incremental_backup_size_in_mega_bytes: Optional[float] = Field(
        default=None, alias="ActualIncrementalBackupSizeInMegaBytes"
    )
    backup_progress_in_mega_bytes: Optional[float] = Field(
        default=None, alias="BackupProgressInMegaBytes"
    )
    current_backup_rate_in_mega_bytes_per_second: Optional[float] = Field(
        default=None, alias="CurrentBackupRateInMegaBytesPerSecond"
    )
    estimated_seconds_to_completion: Optional[int] = Field(
        default=None, alias="EstimatedSecondsToCompletion"
    )
    elapsed_time_in_seconds: Optional[int] = Field(
        default=None, alias="ElapsedTimeInSeconds"
    )
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    restorable_node_types: Optional[List[str]] = Field(
        default=None, alias="RestorableNodeTypes"
    )
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    manual_snapshot_remaining_days: Optional[int] = Field(
        default=None, alias="ManualSnapshotRemainingDays"
    )
    snapshot_retention_start_time: Optional[datetime] = Field(
        default=None, alias="SnapshotRetentionStartTime"
    )


class TaggedResourceModel(BaseModel):
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class UsageLimitResponseMetadataModel(BaseModel):
    usage_limit_id: str = Field(alias="UsageLimitId")
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    feature_type: Literal[
        "concurrency-scaling", "cross-region-datasharing", "spectrum"
    ] = Field(alias="FeatureType")
    limit_type: Literal["data-scanned", "time"] = Field(alias="LimitType")
    amount: int = Field(alias="Amount")
    period: Literal["daily", "monthly", "weekly"] = Field(alias="Period")
    breach_action: Literal["disable", "emit-metric", "log"] = Field(
        alias="BreachAction"
    )
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsageLimitModel(BaseModel):
    usage_limit_id: Optional[str] = Field(default=None, alias="UsageLimitId")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    feature_type: Optional[
        Literal["concurrency-scaling", "cross-region-datasharing", "spectrum"]
    ] = Field(default=None, alias="FeatureType")
    limit_type: Optional[Literal["data-scanned", "time"]] = Field(
        default=None, alias="LimitType"
    )
    amount: Optional[int] = Field(default=None, alias="Amount")
    period: Optional[Literal["daily", "monthly", "weekly"]] = Field(
        default=None, alias="Period"
    )
    breach_action: Optional[Literal["disable", "emit-metric", "log"]] = Field(
        default=None, alias="BreachAction"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribeReservedNodeExchangeStatusOutputMessageModel(BaseModel):
    reserved_node_exchange_status_details: List[
        ReservedNodeExchangeStatusModel
    ] = Field(alias="ReservedNodeExchangeStatusDetails")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterVersionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cluster_versions: List[ClusterVersionModel] = Field(alias="ClusterVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataShareResponseMetadataModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")
    producer_arn: str = Field(alias="ProducerArn")
    allow_publicly_accessible_consumers: bool = Field(
        alias="AllowPubliclyAccessibleConsumers"
    )
    data_share_associations: List[DataShareAssociationModel] = Field(
        alias="DataShareAssociations"
    )
    managed_by: str = Field(alias="ManagedBy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataShareModel(BaseModel):
    data_share_arn: Optional[str] = Field(default=None, alias="DataShareArn")
    producer_arn: Optional[str] = Field(default=None, alias="ProducerArn")
    allow_publicly_accessible_consumers: Optional[bool] = Field(
        default=None, alias="AllowPubliclyAccessibleConsumers"
    )
    data_share_associations: Optional[List[DataShareAssociationModel]] = Field(
        default=None, alias="DataShareAssociations"
    )
    managed_by: Optional[str] = Field(default=None, alias="ManagedBy")


class DescribeClusterDbRevisionsMessageDescribeClusterDbRevisionsPaginateModel(
    BaseModel
):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterParameterGroupsMessageDescribeClusterParameterGroupsPaginateModel(
    BaseModel
):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterParametersMessageDescribeClusterParametersPaginateModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterSecurityGroupsMessageDescribeClusterSecurityGroupsPaginateModel(
    BaseModel
):
    cluster_security_group_name: Optional[str] = Field(
        default=None, alias="ClusterSecurityGroupName"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterSubnetGroupsMessageDescribeClusterSubnetGroupsPaginateModel(
    BaseModel
):
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterTracksMessageDescribeClusterTracksPaginateModel(BaseModel):
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterVersionsMessageDescribeClusterVersionsPaginateModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    cluster_parameter_group_family: Optional[str] = Field(
        default=None, alias="ClusterParameterGroupFamily"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClustersMessageDescribeClustersPaginateModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDataSharesForConsumerMessageDescribeDataSharesForConsumerPaginateModel(
    BaseModel
):
    consumer_arn: Optional[str] = Field(default=None, alias="ConsumerArn")
    status: Optional[Literal["ACTIVE", "AVAILABLE"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDataSharesForProducerMessageDescribeDataSharesForProducerPaginateModel(
    BaseModel
):
    producer_arn: Optional[str] = Field(default=None, alias="ProducerArn")
    status: Optional[
        Literal[
            "ACTIVE", "AUTHORIZED", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"
        ]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDataSharesMessageDescribeDataSharesPaginateModel(BaseModel):
    data_share_arn: Optional[str] = Field(default=None, alias="DataShareArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDefaultClusterParametersMessageDescribeDefaultClusterParametersPaginateModel(
    BaseModel
):
    parameter_group_family: str = Field(alias="ParameterGroupFamily")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEndpointAccessMessageDescribeEndpointAccessPaginateModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEndpointAuthorizationMessageDescribeEndpointAuthorizationPaginateModel(
    BaseModel
):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    account: Optional[str] = Field(default=None, alias="Account")
    grantee: Optional[bool] = Field(default=None, alias="Grantee")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateModel(
    BaseModel
):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsMessageDescribeEventsPaginateModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[
        Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeHsmClientCertificatesMessageDescribeHsmClientCertificatesPaginateModel(
    BaseModel
):
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeHsmConfigurationsMessageDescribeHsmConfigurationsPaginateModel(BaseModel):
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrderableClusterOptionsMessageDescribeOrderableClusterOptionsPaginateModel(
    BaseModel
):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedNodeExchangeStatusInputMessageDescribeReservedNodeExchangeStatusPaginateModel(
    BaseModel
):
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    reserved_node_exchange_request_id: Optional[str] = Field(
        default=None, alias="ReservedNodeExchangeRequestId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedNodeOfferingsMessageDescribeReservedNodeOfferingsPaginateModel(
    BaseModel
):
    reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodeOfferingId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedNodesMessageDescribeReservedNodesPaginateModel(BaseModel):
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotCopyGrantsMessageDescribeSnapshotCopyGrantsPaginateModel(
    BaseModel
):
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSnapshotSchedulesMessageDescribeSnapshotSchedulesPaginateModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    schedule_identifier: Optional[str] = Field(default=None, alias="ScheduleIdentifier")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTableRestoreStatusMessageDescribeTableRestoreStatusPaginateModel(
    BaseModel
):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    table_restore_request_id: Optional[str] = Field(
        default=None, alias="TableRestoreRequestId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTagsMessageDescribeTagsPaginateModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUsageLimitsMessageDescribeUsageLimitsPaginateModel(BaseModel):
    usage_limit_id: Optional[str] = Field(default=None, alias="UsageLimitId")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    feature_type: Optional[
        Literal["concurrency-scaling", "cross-region-datasharing", "spectrum"]
    ] = Field(default=None, alias="FeatureType")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReservedNodeExchangeConfigurationOptionsInputMessageGetReservedNodeExchangeConfigurationOptionsPaginateModel(
    BaseModel
):
    action_type: Literal["resize-cluster", "restore-cluster"] = Field(
        alias="ActionType"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReservedNodeExchangeOfferingsInputMessageGetReservedNodeExchangeOfferingsPaginateModel(
    BaseModel
):
    reserved_node_id: str = Field(alias="ReservedNodeId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterSnapshotsMessageDescribeClusterSnapshotsPaginateModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    cluster_exists: Optional[bool] = Field(default=None, alias="ClusterExists")
    sorting_entities: Optional[Sequence[SnapshotSortingEntityModel]] = Field(
        default=None, alias="SortingEntities"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClusterSnapshotsMessageRequestModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    cluster_exists: Optional[bool] = Field(default=None, alias="ClusterExists")
    sorting_entities: Optional[Sequence[SnapshotSortingEntityModel]] = Field(
        default=None, alias="SortingEntities"
    )


class DescribeClusterSnapshotsMessageSnapshotAvailableWaitModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    cluster_exists: Optional[bool] = Field(default=None, alias="ClusterExists")
    sorting_entities: Optional[Sequence[SnapshotSortingEntityModel]] = Field(
        default=None, alias="SortingEntities"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClustersMessageClusterAvailableWaitModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClustersMessageClusterDeletedWaitModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClustersMessageClusterRestoredWaitModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="TagValues")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNodeConfigurationOptionsMessageDescribeNodeConfigurationOptionsPaginateModel(
    BaseModel
):
    action_type: Literal[
        "recommend-node-config", "resize-cluster", "restore-cluster"
    ] = Field(alias="ActionType")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    filters: Optional[Sequence[NodeConfigurationOptionsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeNodeConfigurationOptionsMessageRequestModel(BaseModel):
    action_type: Literal[
        "recommend-node-config", "resize-cluster", "restore-cluster"
    ] = Field(alias="ActionType")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    snapshot_identifier: Optional[str] = Field(default=None, alias="SnapshotIdentifier")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    filters: Optional[Sequence[NodeConfigurationOptionsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribePartnersOutputMessageModel(BaseModel):
    partner_integration_info_list: List[PartnerIntegrationInfoModel] = Field(
        alias="PartnerIntegrationInfoList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScheduledActionsMessageDescribeScheduledActionsPaginateModel(BaseModel):
    scheduled_action_name: Optional[str] = Field(
        default=None, alias="ScheduledActionName"
    )
    target_action_type: Optional[
        Literal["PauseCluster", "ResizeCluster", "ResumeCluster"]
    ] = Field(default=None, alias="TargetActionType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    active: Optional[bool] = Field(default=None, alias="Active")
    filters: Optional[Sequence[ScheduledActionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScheduledActionsMessageRequestModel(BaseModel):
    scheduled_action_name: Optional[str] = Field(
        default=None, alias="ScheduledActionName"
    )
    target_action_type: Optional[
        Literal["PauseCluster", "ResizeCluster", "ResumeCluster"]
    ] = Field(default=None, alias="TargetActionType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    active: Optional[bool] = Field(default=None, alias="Active")
    filters: Optional[Sequence[ScheduledActionFilterModel]] = Field(
        default=None, alias="Filters"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class EndpointAuthorizationListModel(BaseModel):
    endpoint_authorization_list: List[EndpointAuthorizationModel] = Field(
        alias="EndpointAuthorizationList"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventCategoriesMapModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    events: Optional[List[EventInfoMapModel]] = Field(default=None, alias="Events")


class EventsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VpcEndpointModel(BaseModel):
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="NetworkInterfaces"
    )


class NodeConfigurationOptionsMessageModel(BaseModel):
    node_configuration_option_list: List[NodeConfigurationOptionModel] = Field(
        alias="NodeConfigurationOptionList"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedNodeOfferingModel(BaseModel):
    reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodeOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )
    reserved_node_offering_type: Optional[Literal["Regular", "Upgradable"]] = Field(
        default=None, alias="ReservedNodeOfferingType"
    )


class ReservedNodeModel(BaseModel):
    reserved_node_id: Optional[str] = Field(default=None, alias="ReservedNodeId")
    reserved_node_offering_id: Optional[str] = Field(
        default=None, alias="ReservedNodeOfferingId"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    node_count: Optional[int] = Field(default=None, alias="NodeCount")
    state: Optional[str] = Field(default=None, alias="State")
    offering_type: Optional[str] = Field(default=None, alias="OfferingType")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )
    reserved_node_offering_type: Optional[Literal["Regular", "Upgradable"]] = Field(
        default=None, alias="ReservedNodeOfferingType"
    )


class RestoreTableFromClusterSnapshotResultModel(BaseModel):
    table_restore_status: TableRestoreStatusModel = Field(alias="TableRestoreStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TableRestoreStatusMessageModel(BaseModel):
    table_restore_status_details: List[TableRestoreStatusModel] = Field(
        alias="TableRestoreStatusDetails"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduledActionTypeModel(BaseModel):
    resize_cluster: Optional[ResizeClusterMessageModel] = Field(
        default=None, alias="ResizeCluster"
    )
    pause_cluster: Optional[PauseClusterMessageModel] = Field(
        default=None, alias="PauseCluster"
    )
    resume_cluster: Optional[ResumeClusterMessageModel] = Field(
        default=None, alias="ResumeCluster"
    )


class UpdateTargetModel(BaseModel):
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    database_version: Optional[str] = Field(default=None, alias="DatabaseVersion")
    supported_operations: Optional[List[SupportedOperationModel]] = Field(
        default=None, alias="SupportedOperations"
    )


class AccountAttributeListModel(BaseModel):
    account_attributes: List[AccountAttributeModel] = Field(alias="AccountAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrderableClusterOptionModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    availability_zones: Optional[List[AvailabilityZoneModel]] = Field(
        default=None, alias="AvailabilityZones"
    )


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_status: Optional[str] = Field(default=None, alias="SubnetStatus")


class ClusterDbRevisionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cluster_db_revisions: List[ClusterDbRevisionModel] = Field(
        alias="ClusterDbRevisions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDefaultClusterParametersResultModel(BaseModel):
    default_cluster_parameters: DefaultClusterParametersModel = Field(
        alias="DefaultClusterParameters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterParameterGroupsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    parameter_groups: List[ClusterParameterGroupModel] = Field(alias="ParameterGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterParameterGroupResultModel(BaseModel):
    cluster_parameter_group: ClusterParameterGroupModel = Field(
        alias="ClusterParameterGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventSubscriptionResultModel(BaseModel):
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


class CreateHsmClientCertificateResultModel(BaseModel):
    hsm_client_certificate: HsmClientCertificateModel = Field(
        alias="HsmClientCertificate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HsmClientCertificateMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    hsm_client_certificates: List[HsmClientCertificateModel] = Field(
        alias="HsmClientCertificates"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHsmConfigurationResultModel(BaseModel):
    hsm_configuration: HsmConfigurationModel = Field(alias="HsmConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HsmConfigurationMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    hsm_configurations: List[HsmConfigurationModel] = Field(alias="HsmConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterSecurityGroupModel(BaseModel):
    cluster_security_group_name: Optional[str] = Field(
        default=None, alias="ClusterSecurityGroupName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    ec2_security_groups: Optional[List[EC2SecurityGroupModel]] = Field(
        default=None, alias="EC2SecurityGroups"
    )
    ip_ranges: Optional[List[IPRangeModel]] = Field(default=None, alias="IPRanges")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotCopyGrantResultModel(BaseModel):
    snapshot_copy_grant: SnapshotCopyGrantModel = Field(alias="SnapshotCopyGrant")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SnapshotCopyGrantMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    snapshot_copy_grants: List[SnapshotCopyGrantModel] = Field(
        alias="SnapshotCopyGrants"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotSchedulesOutputMessageModel(BaseModel):
    snapshot_schedules: List[SnapshotScheduleModel] = Field(alias="SnapshotSchedules")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizeSnapshotAccessResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyClusterSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterSnapshotResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeSnapshotAccessResultModel(BaseModel):
    snapshot: SnapshotModel = Field(alias="Snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SnapshotMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    snapshots: List[SnapshotModel] = Field(alias="Snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaggedResourceListMessageModel(BaseModel):
    tagged_resources: List[TaggedResourceModel] = Field(alias="TaggedResources")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsageLimitListModel(BaseModel):
    usage_limits: List[UsageLimitModel] = Field(alias="UsageLimits")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSharesForConsumerResultModel(BaseModel):
    data_shares: List[DataShareModel] = Field(alias="DataShares")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSharesForProducerResultModel(BaseModel):
    data_shares: List[DataShareModel] = Field(alias="DataShares")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSharesResultModel(BaseModel):
    data_shares: List[DataShareModel] = Field(alias="DataShares")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventCategoriesMessageModel(BaseModel):
    event_categories_map_list: List[EventCategoriesMapModel] = Field(
        alias="EventCategoriesMapList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointAccessResponseMetadataModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    resource_owner: str = Field(alias="ResourceOwner")
    subnet_group_name: str = Field(alias="SubnetGroupName")
    endpoint_status: str = Field(alias="EndpointStatus")
    endpoint_name: str = Field(alias="EndpointName")
    endpoint_create_time: datetime = Field(alias="EndpointCreateTime")
    port: int = Field(alias="Port")
    address: str = Field(alias="Address")
    vpc_security_groups: List[VpcSecurityGroupMembershipModel] = Field(
        alias="VpcSecurityGroups"
    )
    vpc_endpoint: VpcEndpointModel = Field(alias="VpcEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointAccessModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    resource_owner: Optional[str] = Field(default=None, alias="ResourceOwner")
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    endpoint_status: Optional[str] = Field(default=None, alias="EndpointStatus")
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    endpoint_create_time: Optional[datetime] = Field(
        default=None, alias="EndpointCreateTime"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    address: Optional[str] = Field(default=None, alias="Address")
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="VpcSecurityGroups"
    )
    vpc_endpoint: Optional[VpcEndpointModel] = Field(default=None, alias="VpcEndpoint")


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")
    vpc_endpoints: Optional[List[VpcEndpointModel]] = Field(
        default=None, alias="VpcEndpoints"
    )


class GetReservedNodeExchangeOfferingsOutputMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_node_offerings: List[ReservedNodeOfferingModel] = Field(
        alias="ReservedNodeOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedNodeOfferingsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_node_offerings: List[ReservedNodeOfferingModel] = Field(
        alias="ReservedNodeOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptReservedNodeExchangeOutputMessageModel(BaseModel):
    exchanged_reserved_node: ReservedNodeModel = Field(alias="ExchangedReservedNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseReservedNodeOfferingResultModel(BaseModel):
    reserved_node: ReservedNodeModel = Field(alias="ReservedNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservedNodeConfigurationOptionModel(BaseModel):
    source_reserved_node: Optional[ReservedNodeModel] = Field(
        default=None, alias="SourceReservedNode"
    )
    target_reserved_node_count: Optional[int] = Field(
        default=None, alias="TargetReservedNodeCount"
    )
    target_reserved_node_offering: Optional[ReservedNodeOfferingModel] = Field(
        default=None, alias="TargetReservedNodeOffering"
    )


class ReservedNodesMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_nodes: List[ReservedNodeModel] = Field(alias="ReservedNodes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduledActionMessageRequestModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    target_action: ScheduledActionTypeModel = Field(alias="TargetAction")
    schedule: str = Field(alias="Schedule")
    iam_role: str = Field(alias="IamRole")
    scheduled_action_description: Optional[str] = Field(
        default=None, alias="ScheduledActionDescription"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    enable: Optional[bool] = Field(default=None, alias="Enable")


class ModifyScheduledActionMessageRequestModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    target_action: Optional[ScheduledActionTypeModel] = Field(
        default=None, alias="TargetAction"
    )
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    iam_role: Optional[str] = Field(default=None, alias="IamRole")
    scheduled_action_description: Optional[str] = Field(
        default=None, alias="ScheduledActionDescription"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    enable: Optional[bool] = Field(default=None, alias="Enable")


class ScheduledActionResponseMetadataModel(BaseModel):
    scheduled_action_name: str = Field(alias="ScheduledActionName")
    target_action: ScheduledActionTypeModel = Field(alias="TargetAction")
    schedule: str = Field(alias="Schedule")
    iam_role: str = Field(alias="IamRole")
    scheduled_action_description: str = Field(alias="ScheduledActionDescription")
    state: Literal["ACTIVE", "DISABLED"] = Field(alias="State")
    next_invocations: List[datetime] = Field(alias="NextInvocations")
    start_time: datetime = Field(alias="StartTime")
    end_time: datetime = Field(alias="EndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduledActionModel(BaseModel):
    scheduled_action_name: Optional[str] = Field(
        default=None, alias="ScheduledActionName"
    )
    target_action: Optional[ScheduledActionTypeModel] = Field(
        default=None, alias="TargetAction"
    )
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    iam_role: Optional[str] = Field(default=None, alias="IamRole")
    scheduled_action_description: Optional[str] = Field(
        default=None, alias="ScheduledActionDescription"
    )
    state: Optional[Literal["ACTIVE", "DISABLED"]] = Field(default=None, alias="State")
    next_invocations: Optional[List[datetime]] = Field(
        default=None, alias="NextInvocations"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class MaintenanceTrackModel(BaseModel):
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    database_version: Optional[str] = Field(default=None, alias="DatabaseVersion")
    update_targets: Optional[List[UpdateTargetModel]] = Field(
        default=None, alias="UpdateTargets"
    )


class OrderableClusterOptionsMessageModel(BaseModel):
    orderable_cluster_options: List[OrderableClusterOptionModel] = Field(
        alias="OrderableClusterOptions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterSubnetGroupModel(BaseModel):
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_group_status: Optional[str] = Field(default=None, alias="SubnetGroupStatus")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class AuthorizeClusterSecurityGroupIngressResultModel(BaseModel):
    cluster_security_group: ClusterSecurityGroupModel = Field(
        alias="ClusterSecurityGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterSecurityGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cluster_security_groups: List[ClusterSecurityGroupModel] = Field(
        alias="ClusterSecurityGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterSecurityGroupResultModel(BaseModel):
    cluster_security_group: ClusterSecurityGroupModel = Field(
        alias="ClusterSecurityGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeClusterSecurityGroupIngressResultModel(BaseModel):
    cluster_security_group: ClusterSecurityGroupModel = Field(
        alias="ClusterSecurityGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EndpointAccessListModel(BaseModel):
    endpoint_access_list: List[EndpointAccessModel] = Field(alias="EndpointAccessList")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterModel(BaseModel):
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    cluster_status: Optional[str] = Field(default=None, alias="ClusterStatus")
    cluster_availability_status: Optional[str] = Field(
        default=None, alias="ClusterAvailabilityStatus"
    )
    modify_status: Optional[str] = Field(default=None, alias="ModifyStatus")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")
    cluster_create_time: Optional[datetime] = Field(
        default=None, alias="ClusterCreateTime"
    )
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    cluster_security_groups: Optional[
        List[ClusterSecurityGroupMembershipModel]
    ] = Field(default=None, alias="ClusterSecurityGroups")
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="VpcSecurityGroups"
    )
    cluster_parameter_groups: Optional[List[ClusterParameterGroupStatusModel]] = Field(
        default=None, alias="ClusterParameterGroups"
    )
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    pending_modified_values: Optional[PendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    allow_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowVersionUpgrade"
    )
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    restore_status: Optional[RestoreStatusModel] = Field(
        default=None, alias="RestoreStatus"
    )
    data_transfer_progress: Optional[DataTransferProgressModel] = Field(
        default=None, alias="DataTransferProgress"
    )
    hsm_status: Optional[HsmStatusModel] = Field(default=None, alias="HsmStatus")
    cluster_snapshot_copy_status: Optional[ClusterSnapshotCopyStatusModel] = Field(
        default=None, alias="ClusterSnapshotCopyStatus"
    )
    cluster_public_key: Optional[str] = Field(default=None, alias="ClusterPublicKey")
    cluster_nodes: Optional[List[ClusterNodeModel]] = Field(
        default=None, alias="ClusterNodes"
    )
    elastic_ip_status: Optional[ElasticIpStatusModel] = Field(
        default=None, alias="ElasticIpStatus"
    )
    cluster_revision_number: Optional[str] = Field(
        default=None, alias="ClusterRevisionNumber"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    iam_roles: Optional[List[ClusterIamRoleModel]] = Field(
        default=None, alias="IamRoles"
    )
    pending_actions: Optional[List[str]] = Field(default=None, alias="PendingActions")
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    elastic_resize_number_of_node_options: Optional[str] = Field(
        default=None, alias="ElasticResizeNumberOfNodeOptions"
    )
    deferred_maintenance_windows: Optional[
        List[DeferredMaintenanceWindowModel]
    ] = Field(default=None, alias="DeferredMaintenanceWindows")
    snapshot_schedule_identifier: Optional[str] = Field(
        default=None, alias="SnapshotScheduleIdentifier"
    )
    snapshot_schedule_state: Optional[Literal["ACTIVE", "FAILED", "MODIFYING"]] = Field(
        default=None, alias="SnapshotScheduleState"
    )
    expected_next_snapshot_schedule_time: Optional[datetime] = Field(
        default=None, alias="ExpectedNextSnapshotScheduleTime"
    )
    expected_next_snapshot_schedule_time_status: Optional[str] = Field(
        default=None, alias="ExpectedNextSnapshotScheduleTimeStatus"
    )
    next_maintenance_window_start_time: Optional[datetime] = Field(
        default=None, alias="NextMaintenanceWindowStartTime"
    )
    resize_info: Optional[ResizeInfoModel] = Field(default=None, alias="ResizeInfo")
    availability_zone_relocation_status: Optional[str] = Field(
        default=None, alias="AvailabilityZoneRelocationStatus"
    )
    cluster_namespace_arn: Optional[str] = Field(
        default=None, alias="ClusterNamespaceArn"
    )
    total_storage_capacity_in_mega_bytes: Optional[int] = Field(
        default=None, alias="TotalStorageCapacityInMegaBytes"
    )
    aqua_configuration: Optional[AquaConfigurationModel] = Field(
        default=None, alias="AquaConfiguration"
    )
    default_iam_role_arn: Optional[str] = Field(default=None, alias="DefaultIamRoleArn")
    reserved_node_exchange_status: Optional[ReservedNodeExchangeStatusModel] = Field(
        default=None, alias="ReservedNodeExchangeStatus"
    )


class GetReservedNodeExchangeConfigurationOptionsOutputMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    reserved_node_configuration_option_list: List[
        ReservedNodeConfigurationOptionModel
    ] = Field(alias="ReservedNodeConfigurationOptionList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduledActionsMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    scheduled_actions: List[ScheduledActionModel] = Field(alias="ScheduledActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrackListMessageModel(BaseModel):
    maintenance_tracks: List[MaintenanceTrackModel] = Field(alias="MaintenanceTracks")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterSubnetGroupMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    cluster_subnet_groups: List[ClusterSubnetGroupModel] = Field(
        alias="ClusterSubnetGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterSubnetGroupResultModel(BaseModel):
    cluster_subnet_group: ClusterSubnetGroupModel = Field(alias="ClusterSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterSubnetGroupResultModel(BaseModel):
    cluster_subnet_group: ClusterSubnetGroupModel = Field(alias="ClusterSubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClustersMessageModel(BaseModel):
    marker: str = Field(alias="Marker")
    clusters: List[ClusterModel] = Field(alias="Clusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableSnapshotCopyResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableSnapshotCopyResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterDbRevisionResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterIamRolesResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterMaintenanceResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifySnapshotCopyRetentionPeriodResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PauseClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResizeClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreFromClusterSnapshotResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResumeClusterResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateEncryptionKeyResultModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
