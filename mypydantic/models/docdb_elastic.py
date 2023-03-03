# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ClusterInListModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")
    cluster_name: str = Field(alias="clusterName")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "INACCESSIBLE_ENCRYPTION_CREDS",
        "INVALID_SECURITY_GROUP_ID",
        "INVALID_SUBNET_ID",
        "IP_ADDRESS_LIMIT_EXCEEDED",
        "UPDATING",
        "VPC_ENDPOINT_LIMIT_EXCEEDED",
    ] = Field(alias="status")


class ClusterSnapshotInListModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")
    snapshot_arn: str = Field(alias="snapshotArn")
    snapshot_creation_time: str = Field(alias="snapshotCreationTime")
    snapshot_name: str = Field(alias="snapshotName")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "INACCESSIBLE_ENCRYPTION_CREDS",
        "INVALID_SECURITY_GROUP_ID",
        "INVALID_SUBNET_ID",
        "IP_ADDRESS_LIMIT_EXCEEDED",
        "UPDATING",
        "VPC_ENDPOINT_LIMIT_EXCEEDED",
    ] = Field(alias="status")


class ClusterSnapshotModel(BaseModel):
    admin_user_name: str = Field(alias="adminUserName")
    cluster_arn: str = Field(alias="clusterArn")
    cluster_creation_time: str = Field(alias="clusterCreationTime")
    kms_key_id: str = Field(alias="kmsKeyId")
    snapshot_arn: str = Field(alias="snapshotArn")
    snapshot_creation_time: str = Field(alias="snapshotCreationTime")
    snapshot_name: str = Field(alias="snapshotName")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "INACCESSIBLE_ENCRYPTION_CREDS",
        "INVALID_SECURITY_GROUP_ID",
        "INVALID_SUBNET_ID",
        "IP_ADDRESS_LIMIT_EXCEEDED",
        "UPDATING",
        "VPC_ENDPOINT_LIMIT_EXCEEDED",
    ] = Field(alias="status")
    subnet_ids: List[str] = Field(alias="subnetIds")
    vpc_security_group_ids: List[str] = Field(alias="vpcSecurityGroupIds")


class ClusterModel(BaseModel):
    admin_user_name: str = Field(alias="adminUserName")
    auth_type: Literal["PLAIN_TEXT", "SECRET_ARN"] = Field(alias="authType")
    cluster_arn: str = Field(alias="clusterArn")
    cluster_endpoint: str = Field(alias="clusterEndpoint")
    cluster_name: str = Field(alias="clusterName")
    create_time: str = Field(alias="createTime")
    kms_key_id: str = Field(alias="kmsKeyId")
    preferred_maintenance_window: str = Field(alias="preferredMaintenanceWindow")
    shard_capacity: int = Field(alias="shardCapacity")
    shard_count: int = Field(alias="shardCount")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "INACCESSIBLE_ENCRYPTION_CREDS",
        "INVALID_SECURITY_GROUP_ID",
        "INVALID_SUBNET_ID",
        "IP_ADDRESS_LIMIT_EXCEEDED",
        "UPDATING",
        "VPC_ENDPOINT_LIMIT_EXCEEDED",
    ] = Field(alias="status")
    subnet_ids: List[str] = Field(alias="subnetIds")
    vpc_security_group_ids: List[str] = Field(alias="vpcSecurityGroupIds")


class CreateClusterInputRequestModel(BaseModel):
    admin_user_name: str = Field(alias="adminUserName")
    admin_user_password: str = Field(alias="adminUserPassword")
    auth_type: Literal["PLAIN_TEXT", "SECRET_ARN"] = Field(alias="authType")
    cluster_name: str = Field(alias="clusterName")
    shard_capacity: int = Field(alias="shardCapacity")
    shard_count: int = Field(alias="shardCount")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcSecurityGroupIds"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateClusterSnapshotInputRequestModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")
    snapshot_name: str = Field(alias="snapshotName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteClusterInputRequestModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")


class DeleteClusterSnapshotInputRequestModel(BaseModel):
    snapshot_arn: str = Field(alias="snapshotArn")


class GetClusterInputRequestModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")


class GetClusterSnapshotInputRequestModel(BaseModel):
    snapshot_arn: str = Field(alias="snapshotArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListClusterSnapshotsInputRequestModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListClustersInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class RestoreClusterFromSnapshotInputRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    snapshot_arn: str = Field(alias="snapshotArn")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcSecurityGroupIds"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateClusterInputRequestModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")
    admin_user_password: Optional[str] = Field(default=None, alias="adminUserPassword")
    auth_type: Optional[Literal["PLAIN_TEXT", "SECRET_ARN"]] = Field(
        default=None, alias="authType"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    shard_capacity: Optional[int] = Field(default=None, alias="shardCapacity")
    shard_count: Optional[int] = Field(default=None, alias="shardCount")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcSecurityGroupIds"
    )


class CreateClusterOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterSnapshotOutputModel(BaseModel):
    snapshot: ClusterSnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterSnapshotOutputModel(BaseModel):
    snapshot: ClusterSnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetClusterOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetClusterSnapshotOutputModel(BaseModel):
    snapshot: ClusterSnapshotModel = Field(alias="snapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClusterSnapshotsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    snapshots: List[ClusterSnapshotInListModel] = Field(alias="snapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersOutputModel(BaseModel):
    clusters: List[ClusterInListModel] = Field(alias="clusters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreClusterFromSnapshotOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClusterSnapshotsInputListClusterSnapshotsPaginateModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersInputListClustersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
