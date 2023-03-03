# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class EndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")
    url: Optional[str] = Field(default=None, alias="URL")


class NotificationConfigurationModel(BaseModel):
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    topic_status: Optional[str] = Field(default=None, alias="TopicStatus")


class ParameterGroupStatusModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    node_ids_to_reboot: Optional[List[str]] = Field(
        default=None, alias="NodeIdsToReboot"
    )


class SSEDescriptionModel(BaseModel):
    status: Optional[Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]] = Field(
        default=None, alias="Status"
    )


class SecurityGroupMembershipModel(BaseModel):
    security_group_identifier: Optional[str] = Field(
        default=None, alias="SecurityGroupIdentifier"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class SSESpecificationModel(BaseModel):
    enabled: bool = Field(alias="Enabled")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    description: Optional[str] = Field(default=None, alias="Description")


class ParameterGroupModel(BaseModel):
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    description: Optional[str] = Field(default=None, alias="Description")


class DecreaseReplicationFactorRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    new_replication_factor: int = Field(alias="NewReplicationFactor")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    node_ids_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="NodeIdsToRemove"
    )


class DeleteClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")


class DeleteParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")


class DeleteSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeClustersRequestModel(BaseModel):
    cluster_names: Optional[Sequence[str]] = Field(default=None, alias="ClusterNames")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeDefaultParametersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeEventsRequestModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EventModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"]
    ] = Field(default=None, alias="SourceType")
    message: Optional[str] = Field(default=None, alias="Message")
    date: Optional[datetime] = Field(default=None, alias="Date")


class DescribeParameterGroupsRequestModel(BaseModel):
    parameter_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="ParameterGroupNames"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeParametersRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeSubnetGroupsRequestModel(BaseModel):
    subnet_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="SubnetGroupNames"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class IncreaseReplicationFactorRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    new_replication_factor: int = Field(alias="NewReplicationFactor")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )


class ListTagsRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NodeTypeSpecificValueModel(BaseModel):
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    value: Optional[str] = Field(default=None, alias="Value")


class ParameterNameValueModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")


class RebootNodeRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    node_id: str = Field(alias="NodeId")


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[str] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )


class UntagResourceRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    description: Optional[str] = Field(default=None, alias="Description")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    notification_topic_status: Optional[str] = Field(
        default=None, alias="NotificationTopicStatus"
    )
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class UpdateSubnetGroupRequestModel(BaseModel):
    subnet_group_name: str = Field(alias="SubnetGroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class NodeModel(BaseModel):
    node_id: Optional[str] = Field(default=None, alias="NodeId")
    endpoint: Optional[EndpointModel] = Field(default=None, alias="Endpoint")
    node_create_time: Optional[datetime] = Field(default=None, alias="NodeCreateTime")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    node_status: Optional[str] = Field(default=None, alias="NodeStatus")
    parameter_group_status: Optional[str] = Field(
        default=None, alias="ParameterGroupStatus"
    )


class CreateClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    node_type: str = Field(alias="NodeType")
    replication_factor: int = Field(alias="ReplicationFactor")
    iam_role_arn: str = Field(alias="IamRoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    notification_topic_arn: Optional[str] = Field(
        default=None, alias="NotificationTopicArn"
    )
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    s_s_especification: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecification"
    )
    cluster_endpoint_encryption_type: Optional[Literal["NONE", "TLS"]] = Field(
        default=None, alias="ClusterEndpointEncryptionType"
    )


class TagResourceRequestModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DeleteParameterGroupResponseModel(BaseModel):
    deletion_message: str = Field(alias="DeletionMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSubnetGroupResponseModel(BaseModel):
    deletion_message: str = Field(alias="DeletionMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeParameterGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    parameter_groups: List[ParameterGroupModel] = Field(alias="ParameterGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateParameterGroupResponseModel(BaseModel):
    parameter_group: ParameterGroupModel = Field(alias="ParameterGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClustersRequestDescribeClustersPaginateModel(BaseModel):
    cluster_names: Optional[Sequence[str]] = Field(default=None, alias="ClusterNames")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDefaultParametersRequestDescribeDefaultParametersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsRequestDescribeEventsPaginateModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_type: Optional[
        Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"]
    ] = Field(default=None, alias="SourceType")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateModel(BaseModel):
    parameter_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="ParameterGroupNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeParametersRequestDescribeParametersPaginateModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    source: Optional[str] = Field(default=None, alias="Source")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateModel(BaseModel):
    subnet_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="SubnetGroupNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsRequestListTagsPaginateModel(BaseModel):
    resource_name: str = Field(alias="ResourceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParameterModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_type: Optional[Literal["DEFAULT", "NODE_TYPE_SPECIFIC"]] = Field(
        default=None, alias="ParameterType"
    )
    parameter_value: Optional[str] = Field(default=None, alias="ParameterValue")
    node_type_specific_values: Optional[List[NodeTypeSpecificValueModel]] = Field(
        default=None, alias="NodeTypeSpecificValues"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    source: Optional[str] = Field(default=None, alias="Source")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    allowed_values: Optional[str] = Field(default=None, alias="AllowedValues")
    is_modifiable: Optional[Literal["CONDITIONAL", "FALSE", "TRUE"]] = Field(
        default=None, alias="IsModifiable"
    )
    change_type: Optional[Literal["IMMEDIATE", "REQUIRES_REBOOT"]] = Field(
        default=None, alias="ChangeType"
    )


class UpdateParameterGroupRequestModel(BaseModel):
    parameter_group_name: str = Field(alias="ParameterGroupName")
    parameter_name_values: Sequence[ParameterNameValueModel] = Field(
        alias="ParameterNameValues"
    )


class SubnetGroupModel(BaseModel):
    subnet_group_name: Optional[str] = Field(default=None, alias="SubnetGroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")


class ClusterModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    description: Optional[str] = Field(default=None, alias="Description")
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    total_nodes: Optional[int] = Field(default=None, alias="TotalNodes")
    active_nodes: Optional[int] = Field(default=None, alias="ActiveNodes")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    status: Optional[str] = Field(default=None, alias="Status")
    cluster_discovery_endpoint: Optional[EndpointModel] = Field(
        default=None, alias="ClusterDiscoveryEndpoint"
    )
    node_ids_to_remove: Optional[List[str]] = Field(
        default=None, alias="NodeIdsToRemove"
    )
    nodes: Optional[List[NodeModel]] = Field(default=None, alias="Nodes")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    notification_configuration: Optional[NotificationConfigurationModel] = Field(
        default=None, alias="NotificationConfiguration"
    )
    subnet_group: Optional[str] = Field(default=None, alias="SubnetGroup")
    security_groups: Optional[List[SecurityGroupMembershipModel]] = Field(
        default=None, alias="SecurityGroups"
    )
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    parameter_group: Optional[ParameterGroupStatusModel] = Field(
        default=None, alias="ParameterGroup"
    )
    s_s_edescription: Optional[SSEDescriptionModel] = Field(
        default=None, alias="SSEDescription"
    )
    cluster_endpoint_encryption_type: Optional[Literal["NONE", "TLS"]] = Field(
        default=None, alias="ClusterEndpointEncryptionType"
    )


class DescribeDefaultParametersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    parameters: List[ParameterModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeParametersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    parameters: List[ParameterModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubnetGroupResponseModel(BaseModel):
    subnet_group: SubnetGroupModel = Field(alias="SubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSubnetGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    subnet_groups: List[SubnetGroupModel] = Field(alias="SubnetGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubnetGroupResponseModel(BaseModel):
    subnet_group: SubnetGroupModel = Field(alias="SubnetGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecreaseReplicationFactorResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClustersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    clusters: List[ClusterModel] = Field(alias="Clusters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IncreaseReplicationFactorResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootNodeResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
