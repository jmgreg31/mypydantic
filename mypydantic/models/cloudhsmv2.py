# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BackupRetentionPolicyModel(BaseModel):
    type: Optional[Literal["DAYS"]] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CertificatesModel(BaseModel):
    cluster_csr: Optional[str] = Field(default=None, alias="ClusterCsr")
    hsm_certificate: Optional[str] = Field(default=None, alias="HsmCertificate")
    aws_hardware_certificate: Optional[str] = Field(
        default=None, alias="AwsHardwareCertificate"
    )
    manufacturer_hardware_certificate: Optional[str] = Field(
        default=None, alias="ManufacturerHardwareCertificate"
    )
    cluster_certificate: Optional[str] = Field(default=None, alias="ClusterCertificate")


class HsmModel(BaseModel):
    hsm_id: str = Field(alias="HsmId")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    eni_id: Optional[str] = Field(default=None, alias="EniId")
    eni_ip: Optional[str] = Field(default=None, alias="EniIp")
    state: Optional[
        Literal[
            "ACTIVE", "CREATE_IN_PROGRESS", "DEGRADED", "DELETED", "DELETE_IN_PROGRESS"
        ]
    ] = Field(default=None, alias="State")
    state_message: Optional[str] = Field(default=None, alias="StateMessage")


class DestinationBackupModel(BaseModel):
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    source_backup: Optional[str] = Field(default=None, alias="SourceBackup")
    source_cluster: Optional[str] = Field(default=None, alias="SourceCluster")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateHsmRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    availability_zone: str = Field(alias="AvailabilityZone")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class DeleteBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")


class DeleteClusterRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class DeleteHsmRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    hsm_id: Optional[str] = Field(default=None, alias="HsmId")
    eni_id: Optional[str] = Field(default=None, alias="EniId")
    eni_ip: Optional[str] = Field(default=None, alias="EniIp")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeBackupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Filters"
    )
    sort_ascending: Optional[bool] = Field(default=None, alias="SortAscending")


class DescribeClustersRequestModel(BaseModel):
    filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class InitializeClusterRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    signed_cert: str = Field(alias="SignedCert")
    trust_anchor: str = Field(alias="TrustAnchor")


class ListTagsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ModifyBackupAttributesRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    never_expires: bool = Field(alias="NeverExpires")


class RestoreBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")


class UntagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_key_list: Sequence[str] = Field(alias="TagKeyList")


class ModifyClusterRequestModel(BaseModel):
    backup_retention_policy: BackupRetentionPolicyModel = Field(
        alias="BackupRetentionPolicy"
    )
    cluster_id: str = Field(alias="ClusterId")


class BackupModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    backup_state: Optional[
        Literal["CREATE_IN_PROGRESS", "DELETED", "PENDING_DELETION", "READY"]
    ] = Field(default=None, alias="BackupState")
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    copy_timestamp: Optional[datetime] = Field(default=None, alias="CopyTimestamp")
    never_expires: Optional[bool] = Field(default=None, alias="NeverExpires")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    source_backup: Optional[str] = Field(default=None, alias="SourceBackup")
    source_cluster: Optional[str] = Field(default=None, alias="SourceCluster")
    delete_timestamp: Optional[datetime] = Field(default=None, alias="DeleteTimestamp")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")


class CopyBackupToRegionRequestModel(BaseModel):
    destination_region: str = Field(alias="DestinationRegion")
    backup_id: str = Field(alias="BackupId")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class CreateClusterRequestModel(BaseModel):
    hsm_type: str = Field(alias="HsmType")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    backup_retention_policy: Optional[BackupRetentionPolicyModel] = Field(
        default=None, alias="BackupRetentionPolicy"
    )
    source_backup_id: Optional[str] = Field(default=None, alias="SourceBackupId")
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class TagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_list: Sequence[TagModel] = Field(alias="TagList")


class ClusterModel(BaseModel):
    backup_policy: Optional[Literal["DEFAULT"]] = Field(
        default=None, alias="BackupPolicy"
    )
    backup_retention_policy: Optional[BackupRetentionPolicyModel] = Field(
        default=None, alias="BackupRetentionPolicy"
    )
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    hsms: Optional[List[HsmModel]] = Field(default=None, alias="Hsms")
    hsm_type: Optional[str] = Field(default=None, alias="HsmType")
    pre_co_password: Optional[str] = Field(default=None, alias="PreCoPassword")
    security_group: Optional[str] = Field(default=None, alias="SecurityGroup")
    source_backup_id: Optional[str] = Field(default=None, alias="SourceBackupId")
    state: Optional[
        Literal[
            "ACTIVE",
            "CREATE_IN_PROGRESS",
            "DEGRADED",
            "DELETED",
            "DELETE_IN_PROGRESS",
            "INITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "UNINITIALIZED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="State")
    state_message: Optional[str] = Field(default=None, alias="StateMessage")
    subnet_mapping: Optional[Dict[str, str]] = Field(
        default=None, alias="SubnetMapping"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    certificates: Optional[CertificatesModel] = Field(
        default=None, alias="Certificates"
    )
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")


class CopyBackupToRegionResponseModel(BaseModel):
    destination_backup: DestinationBackupModel = Field(alias="DestinationBackup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHsmResponseModel(BaseModel):
    hsm: HsmModel = Field(alias="Hsm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteHsmResponseModel(BaseModel):
    hsm_id: str = Field(alias="HsmId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitializeClusterResponseModel(BaseModel):
    state: Literal[
        "ACTIVE",
        "CREATE_IN_PROGRESS",
        "DEGRADED",
        "DELETED",
        "DELETE_IN_PROGRESS",
        "INITIALIZED",
        "INITIALIZE_IN_PROGRESS",
        "UNINITIALIZED",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="State")
    state_message: str = Field(alias="StateMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupsRequestDescribeBackupsPaginateModel(BaseModel):
    filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Filters"
    )
    sort_ascending: Optional[bool] = Field(default=None, alias="SortAscending")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeClustersRequestDescribeClustersPaginateModel(BaseModel):
    filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsRequestListTagsPaginateModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DeleteBackupResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupsResponseModel(BaseModel):
    backups: List[BackupModel] = Field(alias="Backups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyBackupAttributesResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreBackupResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClustersResponseModel(BaseModel):
    clusters: List[ClusterModel] = Field(alias="Clusters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
