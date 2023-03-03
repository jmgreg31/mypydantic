# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountAttributeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    maximum: Optional[int] = Field(default=None, alias="Maximum")
    used: Optional[int] = Field(default=None, alias="Used")


class EngineAttributeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BackupModel(BaseModel):
    backup_arn: Optional[str] = Field(default=None, alias="BackupArn")
    backup_id: Optional[str] = Field(default=None, alias="BackupId")
    backup_type: Optional[Literal["AUTOMATED", "MANUAL"]] = Field(
        default=None, alias="BackupType"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_model: Optional[str] = Field(default=None, alias="EngineModel")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    instance_profile_arn: Optional[str] = Field(
        default=None, alias="InstanceProfileArn"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    key_pair: Optional[str] = Field(default=None, alias="KeyPair")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    s3_data_size: Optional[int] = Field(default=None, alias="S3DataSize")
    s3_data_url: Optional[str] = Field(default=None, alias="S3DataUrl")
    s3_log_url: Optional[str] = Field(default=None, alias="S3LogUrl")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    status: Optional[Literal["DELETING", "FAILED", "IN_PROGRESS", "OK"]] = Field(
        default=None, alias="Status"
    )
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    tools_version: Optional[str] = Field(default=None, alias="ToolsVersion")
    user_arn: Optional[str] = Field(default=None, alias="UserArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")


class DeleteServerRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeBackupsRequestModel(BaseModel):
    backup_id: Optional[str] = Field(default=None, alias="BackupId")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeEventsRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ServerEventModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    message: Optional[str] = Field(default=None, alias="Message")
    log_url: Optional[str] = Field(default=None, alias="LogUrl")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeNodeAssociationStatusRequestModel(BaseModel):
    node_association_status_token: str = Field(alias="NodeAssociationStatusToken")
    server_name: str = Field(alias="ServerName")


class DescribeServersRequestModel(BaseModel):
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RestoreServerRequestModel(BaseModel):
    backup_id: str = Field(alias="BackupId")
    server_name: str = Field(alias="ServerName")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    key_pair: Optional[str] = Field(default=None, alias="KeyPair")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateServerEngineAttributesRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class UpdateServerRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    disable_automated_backup: Optional[bool] = Field(
        default=None, alias="DisableAutomatedBackup"
    )
    backup_retention_count: Optional[int] = Field(
        default=None, alias="BackupRetentionCount"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )


class AssociateNodeRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    node_name: str = Field(alias="NodeName")
    engine_attributes: Sequence[EngineAttributeModel] = Field(alias="EngineAttributes")


class DisassociateNodeRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    node_name: str = Field(alias="NodeName")
    engine_attributes: Optional[Sequence[EngineAttributeModel]] = Field(
        default=None, alias="EngineAttributes"
    )


class ExportServerEngineAttributeRequestModel(BaseModel):
    export_attribute_name: str = Field(alias="ExportAttributeName")
    server_name: str = Field(alias="ServerName")
    input_attributes: Optional[Sequence[EngineAttributeModel]] = Field(
        default=None, alias="InputAttributes"
    )


class ServerModel(BaseModel):
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    backup_retention_count: Optional[int] = Field(
        default=None, alias="BackupRetentionCount"
    )
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    cloud_formation_stack_arn: Optional[str] = Field(
        default=None, alias="CloudFormationStackArn"
    )
    custom_domain: Optional[str] = Field(default=None, alias="CustomDomain")
    disable_automated_backup: Optional[bool] = Field(
        default=None, alias="DisableAutomatedBackup"
    )
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_model: Optional[str] = Field(default=None, alias="EngineModel")
    engine_attributes: Optional[List[EngineAttributeModel]] = Field(
        default=None, alias="EngineAttributes"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    instance_profile_arn: Optional[str] = Field(
        default=None, alias="InstanceProfileArn"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    key_pair: Optional[str] = Field(default=None, alias="KeyPair")
    maintenance_status: Optional[Literal["FAILED", "SUCCESS"]] = Field(
        default=None, alias="MaintenanceStatus"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    status: Optional[
        Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "FAILED",
            "HEALTHY",
            "MODIFYING",
            "RESTORING",
            "RUNNING",
            "SETUP",
            "TERMINATED",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    server_arn: Optional[str] = Field(default=None, alias="ServerArn")


class StartMaintenanceRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    engine_attributes: Optional[Sequence[EngineAttributeModel]] = Field(
        default=None, alias="EngineAttributes"
    )


class AssociateNodeResponseModel(BaseModel):
    node_association_status_token: str = Field(alias="NodeAssociationStatusToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAttributesResponseModel(BaseModel):
    attributes: List[AccountAttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNodeAssociationStatusResponseModel(BaseModel):
    node_association_status: Literal["FAILED", "IN_PROGRESS", "SUCCESS"] = Field(
        alias="NodeAssociationStatus"
    )
    engine_attributes: List[EngineAttributeModel] = Field(alias="EngineAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateNodeResponseModel(BaseModel):
    node_association_status_token: str = Field(alias="NodeAssociationStatusToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportServerEngineAttributeResponseModel(BaseModel):
    engine_attribute: EngineAttributeModel = Field(alias="EngineAttribute")
    server_name: str = Field(alias="ServerName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupResponseModel(BaseModel):
    backup: BackupModel = Field(alias="Backup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupsResponseModel(BaseModel):
    backups: List[BackupModel] = Field(alias="Backups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackupRequestModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateServerRequestModel(BaseModel):
    engine: str = Field(alias="Engine")
    server_name: str = Field(alias="ServerName")
    instance_profile_arn: str = Field(alias="InstanceProfileArn")
    instance_type: str = Field(alias="InstanceType")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    custom_domain: Optional[str] = Field(default=None, alias="CustomDomain")
    custom_certificate: Optional[str] = Field(default=None, alias="CustomCertificate")
    custom_private_key: Optional[str] = Field(default=None, alias="CustomPrivateKey")
    disable_automated_backup: Optional[bool] = Field(
        default=None, alias="DisableAutomatedBackup"
    )
    engine_model: Optional[str] = Field(default=None, alias="EngineModel")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    engine_attributes: Optional[Sequence[EngineAttributeModel]] = Field(
        default=None, alias="EngineAttributes"
    )
    backup_retention_count: Optional[int] = Field(
        default=None, alias="BackupRetentionCount"
    )
    key_pair: Optional[str] = Field(default=None, alias="KeyPair")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    backup_id: Optional[str] = Field(default=None, alias="BackupId")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DescribeBackupsRequestDescribeBackupsPaginateModel(BaseModel):
    backup_id: Optional[str] = Field(default=None, alias="BackupId")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsRequestDescribeEventsPaginateModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeServersRequestDescribeServersPaginateModel(BaseModel):
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsResponseModel(BaseModel):
    server_events: List[ServerEventModel] = Field(alias="ServerEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNodeAssociationStatusRequestNodeAssociatedWaitModel(BaseModel):
    node_association_status_token: str = Field(alias="NodeAssociationStatusToken")
    server_name: str = Field(alias="ServerName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class CreateServerResponseModel(BaseModel):
    server: ServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServersResponseModel(BaseModel):
    servers: List[ServerModel] = Field(alias="Servers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreServerResponseModel(BaseModel):
    server: ServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMaintenanceResponseModel(BaseModel):
    server: ServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServerEngineAttributesResponseModel(BaseModel):
    server: ServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServerResponseModel(BaseModel):
    server: ServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
