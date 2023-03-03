# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AgentListEntryModel(BaseModel):
    agent_arn: Optional[str] = Field(default=None, alias="AgentArn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["OFFLINE", "ONLINE"]] = Field(default=None, alias="Status")


class CancelTaskExecutionRequestModel(BaseModel):
    task_execution_arn: str = Field(alias="TaskExecutionArn")


class TagListEntryModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class Ec2ConfigModel(BaseModel):
    subnet_arn: str = Field(alias="SubnetArn")
    security_group_arns: Sequence[str] = Field(alias="SecurityGroupArns")


class HdfsNameNodeModel(BaseModel):
    hostname: str = Field(alias="Hostname")
    port: int = Field(alias="Port")


class QopConfigurationModel(BaseModel):
    rpc_protection: Optional[
        Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
    ] = Field(default=None, alias="RpcProtection")
    data_transfer_protection: Optional[
        Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
    ] = Field(default=None, alias="DataTransferProtection")


class NfsMountOptionsModel(BaseModel):
    version: Optional[Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]] = Field(
        default=None, alias="Version"
    )


class OnPremConfigModel(BaseModel):
    agent_arns: Sequence[str] = Field(alias="AgentArns")


class S3ConfigModel(BaseModel):
    bucket_access_role_arn: str = Field(alias="BucketAccessRoleArn")


class SmbMountOptionsModel(BaseModel):
    version: Optional[Literal["AUTOMATIC", "SMB1", "SMB2", "SMB2_0", "SMB3"]] = Field(
        default=None, alias="Version"
    )


class FilterRuleModel(BaseModel):
    filter_type: Optional[Literal["SIMPLE_PATTERN"]] = Field(
        default=None, alias="FilterType"
    )
    value: Optional[str] = Field(default=None, alias="Value")


class OptionsModel(BaseModel):
    verify_mode: Optional[
        Literal["NONE", "ONLY_FILES_TRANSFERRED", "POINT_IN_TIME_CONSISTENT"]
    ] = Field(default=None, alias="VerifyMode")
    overwrite_mode: Optional[Literal["ALWAYS", "NEVER"]] = Field(
        default=None, alias="OverwriteMode"
    )
    atime: Optional[Literal["BEST_EFFORT", "NONE"]] = Field(default=None, alias="Atime")
    mtime: Optional[Literal["NONE", "PRESERVE"]] = Field(default=None, alias="Mtime")
    uid: Optional[Literal["BOTH", "INT_VALUE", "NAME", "NONE"]] = Field(
        default=None, alias="Uid"
    )
    gid: Optional[Literal["BOTH", "INT_VALUE", "NAME", "NONE"]] = Field(
        default=None, alias="Gid"
    )
    preserve_deleted_files: Optional[Literal["PRESERVE", "REMOVE"]] = Field(
        default=None, alias="PreserveDeletedFiles"
    )
    preserve_devices: Optional[Literal["NONE", "PRESERVE"]] = Field(
        default=None, alias="PreserveDevices"
    )
    posix_permissions: Optional[Literal["NONE", "PRESERVE"]] = Field(
        default=None, alias="PosixPermissions"
    )
    bytes_per_second: Optional[int] = Field(default=None, alias="BytesPerSecond")
    task_queueing: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TaskQueueing"
    )
    log_level: Optional[Literal["BASIC", "OFF", "TRANSFER"]] = Field(
        default=None, alias="LogLevel"
    )
    transfer_mode: Optional[Literal["ALL", "CHANGED"]] = Field(
        default=None, alias="TransferMode"
    )
    security_descriptor_copy_flags: Optional[
        Literal["NONE", "OWNER_DACL", "OWNER_DACL_SACL"]
    ] = Field(default=None, alias="SecurityDescriptorCopyFlags")
    object_tags: Optional[Literal["NONE", "PRESERVE"]] = Field(
        default=None, alias="ObjectTags"
    )


class TaskScheduleModel(BaseModel):
    schedule_expression: str = Field(alias="ScheduleExpression")


class DeleteAgentRequestModel(BaseModel):
    agent_arn: str = Field(alias="AgentArn")


class DeleteLocationRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DeleteTaskRequestModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")


class DescribeAgentRequestModel(BaseModel):
    agent_arn: str = Field(alias="AgentArn")


class PrivateLinkConfigModel(BaseModel):
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    private_link_endpoint: Optional[str] = Field(
        default=None, alias="PrivateLinkEndpoint"
    )
    subnet_arns: Optional[List[str]] = Field(default=None, alias="SubnetArns")
    security_group_arns: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupArns"
    )


class DescribeLocationEfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationFsxLustreRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationFsxOntapRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationFsxOpenZfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationFsxWindowsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationHdfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationNfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationObjectStorageRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationS3RequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeLocationSmbRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")


class DescribeTaskExecutionRequestModel(BaseModel):
    task_execution_arn: str = Field(alias="TaskExecutionArn")


class TaskExecutionResultDetailModel(BaseModel):
    prepare_duration: Optional[int] = Field(default=None, alias="PrepareDuration")
    prepare_status: Optional[Literal["ERROR", "PENDING", "SUCCESS"]] = Field(
        default=None, alias="PrepareStatus"
    )
    total_duration: Optional[int] = Field(default=None, alias="TotalDuration")
    transfer_duration: Optional[int] = Field(default=None, alias="TransferDuration")
    transfer_status: Optional[Literal["ERROR", "PENDING", "SUCCESS"]] = Field(
        default=None, alias="TransferStatus"
    )
    verify_duration: Optional[int] = Field(default=None, alias="VerifyDuration")
    verify_status: Optional[Literal["ERROR", "PENDING", "SUCCESS"]] = Field(
        default=None, alias="VerifyStatus"
    )
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_detail: Optional[str] = Field(default=None, alias="ErrorDetail")


class DescribeTaskRequestModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAgentsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LocationFilterModel(BaseModel):
    name: Literal["CreationTime", "LocationType", "LocationUri"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal[
        "BeginsWith",
        "Contains",
        "Equals",
        "GreaterThan",
        "GreaterThanOrEqual",
        "In",
        "LessThan",
        "LessThanOrEqual",
        "NotContains",
        "NotEquals",
    ] = Field(alias="Operator")


class LocationListEntryModel(BaseModel):
    location_arn: Optional[str] = Field(default=None, alias="LocationArn")
    location_uri: Optional[str] = Field(default=None, alias="LocationUri")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTaskExecutionsRequestModel(BaseModel):
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TaskExecutionListEntryModel(BaseModel):
    task_execution_arn: Optional[str] = Field(default=None, alias="TaskExecutionArn")
    status: Optional[
        Literal[
            "ERROR",
            "LAUNCHING",
            "PREPARING",
            "QUEUED",
            "SUCCESS",
            "TRANSFERRING",
            "VERIFYING",
        ]
    ] = Field(default=None, alias="Status")


class TaskFilterModel(BaseModel):
    name: Literal["CreationTime", "LocationId"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")
    operator: Literal[
        "BeginsWith",
        "Contains",
        "Equals",
        "GreaterThan",
        "GreaterThanOrEqual",
        "In",
        "LessThan",
        "LessThanOrEqual",
        "NotContains",
        "NotEquals",
    ] = Field(alias="Operator")


class TaskListEntryModel(BaseModel):
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    status: Optional[
        Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"]
    ] = Field(default=None, alias="Status")
    name: Optional[str] = Field(default=None, alias="Name")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    keys: Sequence[str] = Field(alias="Keys")


class UpdateAgentRequestModel(BaseModel):
    agent_arn: str = Field(alias="AgentArn")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateLocationObjectStorageRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    server_port: Optional[int] = Field(default=None, alias="ServerPort")
    server_protocol: Optional[Literal["HTTP", "HTTPS"]] = Field(
        default=None, alias="ServerProtocol"
    )
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    access_key: Optional[str] = Field(default=None, alias="AccessKey")
    secret_key: Optional[str] = Field(default=None, alias="SecretKey")
    agent_arns: Optional[Sequence[str]] = Field(default=None, alias="AgentArns")
    server_certificate: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="ServerCertificate")


class CreateAgentRequestModel(BaseModel):
    activation_key: str = Field(alias="ActivationKey")
    agent_name: Optional[str] = Field(default=None, alias="AgentName")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    subnet_arns: Optional[Sequence[str]] = Field(default=None, alias="SubnetArns")
    security_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupArns"
    )


class CreateLocationFsxLustreRequestModel(BaseModel):
    fsx_filesystem_arn: str = Field(alias="FsxFilesystemArn")
    security_group_arns: Sequence[str] = Field(alias="SecurityGroupArns")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class CreateLocationFsxWindowsRequestModel(BaseModel):
    fsx_filesystem_arn: str = Field(alias="FsxFilesystemArn")
    security_group_arns: Sequence[str] = Field(alias="SecurityGroupArns")
    user: str = Field(alias="User")
    password: str = Field(alias="Password")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")
    domain: Optional[str] = Field(default=None, alias="Domain")


class CreateLocationObjectStorageRequestModel(BaseModel):
    server_hostname: str = Field(alias="ServerHostname")
    bucket_name: str = Field(alias="BucketName")
    agent_arns: Sequence[str] = Field(alias="AgentArns")
    server_port: Optional[int] = Field(default=None, alias="ServerPort")
    server_protocol: Optional[Literal["HTTP", "HTTPS"]] = Field(
        default=None, alias="ServerProtocol"
    )
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    access_key: Optional[str] = Field(default=None, alias="AccessKey")
    secret_key: Optional[str] = Field(default=None, alias="SecretKey")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")
    server_certificate: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="ServerCertificate")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagListEntryModel] = Field(alias="Tags")


class CreateAgentResponseModel(BaseModel):
    agent_arn: str = Field(alias="AgentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationEfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationFsxLustreResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationFsxOntapResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationFsxOpenZfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationFsxWindowsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationHdfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationNfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationObjectStorageResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationS3ResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationSmbResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskResponseModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLocationFsxLustreResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    security_group_arns: List[str] = Field(alias="SecurityGroupArns")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLocationFsxWindowsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    security_group_arns: List[str] = Field(alias="SecurityGroupArns")
    creation_time: datetime = Field(alias="CreationTime")
    user: str = Field(alias="User")
    domain: str = Field(alias="Domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLocationObjectStorageResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    access_key: str = Field(alias="AccessKey")
    server_port: int = Field(alias="ServerPort")
    server_protocol: Literal["HTTP", "HTTPS"] = Field(alias="ServerProtocol")
    agent_arns: List[str] = Field(alias="AgentArns")
    creation_time: datetime = Field(alias="CreationTime")
    server_certificate: bytes = Field(alias="ServerCertificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAgentsResponseModel(BaseModel):
    agents: List[AgentListEntryModel] = Field(alias="Agents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagListEntryModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTaskExecutionResponseModel(BaseModel):
    task_execution_arn: str = Field(alias="TaskExecutionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationEfsRequestModel(BaseModel):
    efs_filesystem_arn: str = Field(alias="EfsFilesystemArn")
    ec2_config: Ec2ConfigModel = Field(alias="Ec2Config")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")
    access_point_arn: Optional[str] = Field(default=None, alias="AccessPointArn")
    file_system_access_role_arn: Optional[str] = Field(
        default=None, alias="FileSystemAccessRoleArn"
    )
    in_transit_encryption: Optional[Literal["NONE", "TLS1_2"]] = Field(
        default=None, alias="InTransitEncryption"
    )


class DescribeLocationEfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    ec2_config: Ec2ConfigModel = Field(alias="Ec2Config")
    creation_time: datetime = Field(alias="CreationTime")
    access_point_arn: str = Field(alias="AccessPointArn")
    file_system_access_role_arn: str = Field(alias="FileSystemAccessRoleArn")
    in_transit_encryption: Literal["NONE", "TLS1_2"] = Field(
        alias="InTransitEncryption"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationHdfsRequestModel(BaseModel):
    name_nodes: Sequence[HdfsNameNodeModel] = Field(alias="NameNodes")
    authentication_type: Literal["KERBEROS", "SIMPLE"] = Field(
        alias="AuthenticationType"
    )
    agent_arns: Sequence[str] = Field(alias="AgentArns")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    block_size: Optional[int] = Field(default=None, alias="BlockSize")
    replication_factor: Optional[int] = Field(default=None, alias="ReplicationFactor")
    kms_key_provider_uri: Optional[str] = Field(default=None, alias="KmsKeyProviderUri")
    qop_configuration: Optional[QopConfigurationModel] = Field(
        default=None, alias="QopConfiguration"
    )
    simple_user: Optional[str] = Field(default=None, alias="SimpleUser")
    kerberos_principal: Optional[str] = Field(default=None, alias="KerberosPrincipal")
    kerberos_keytab: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="KerberosKeytab")
    kerberos_krb5_conf: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="KerberosKrb5Conf")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class DescribeLocationHdfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    name_nodes: List[HdfsNameNodeModel] = Field(alias="NameNodes")
    block_size: int = Field(alias="BlockSize")
    replication_factor: int = Field(alias="ReplicationFactor")
    kms_key_provider_uri: str = Field(alias="KmsKeyProviderUri")
    qop_configuration: QopConfigurationModel = Field(alias="QopConfiguration")
    authentication_type: Literal["KERBEROS", "SIMPLE"] = Field(
        alias="AuthenticationType"
    )
    simple_user: str = Field(alias="SimpleUser")
    kerberos_principal: str = Field(alias="KerberosPrincipal")
    agent_arns: List[str] = Field(alias="AgentArns")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLocationHdfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    name_nodes: Optional[Sequence[HdfsNameNodeModel]] = Field(
        default=None, alias="NameNodes"
    )
    block_size: Optional[int] = Field(default=None, alias="BlockSize")
    replication_factor: Optional[int] = Field(default=None, alias="ReplicationFactor")
    kms_key_provider_uri: Optional[str] = Field(default=None, alias="KmsKeyProviderUri")
    qop_configuration: Optional[QopConfigurationModel] = Field(
        default=None, alias="QopConfiguration"
    )
    authentication_type: Optional[Literal["KERBEROS", "SIMPLE"]] = Field(
        default=None, alias="AuthenticationType"
    )
    simple_user: Optional[str] = Field(default=None, alias="SimpleUser")
    kerberos_principal: Optional[str] = Field(default=None, alias="KerberosPrincipal")
    kerberos_keytab: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="KerberosKeytab")
    kerberos_krb5_conf: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="KerberosKrb5Conf")
    agent_arns: Optional[Sequence[str]] = Field(default=None, alias="AgentArns")


class FsxProtocolNfsModel(BaseModel):
    mount_options: Optional[NfsMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )


class CreateLocationNfsRequestModel(BaseModel):
    subdirectory: str = Field(alias="Subdirectory")
    server_hostname: str = Field(alias="ServerHostname")
    on_prem_config: OnPremConfigModel = Field(alias="OnPremConfig")
    mount_options: Optional[NfsMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class DescribeLocationNfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    on_prem_config: OnPremConfigModel = Field(alias="OnPremConfig")
    mount_options: NfsMountOptionsModel = Field(alias="MountOptions")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLocationNfsRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    on_prem_config: Optional[OnPremConfigModel] = Field(
        default=None, alias="OnPremConfig"
    )
    mount_options: Optional[NfsMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )


class CreateLocationS3RequestModel(BaseModel):
    s3_bucket_arn: str = Field(alias="S3BucketArn")
    s3_config: S3ConfigModel = Field(alias="S3Config")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    s3_storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_INSTANT_RETRIEVAL",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="S3StorageClass")
    agent_arns: Optional[Sequence[str]] = Field(default=None, alias="AgentArns")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class DescribeLocationS3ResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    s3_storage_class: Literal[
        "DEEP_ARCHIVE",
        "GLACIER",
        "GLACIER_INSTANT_RETRIEVAL",
        "INTELLIGENT_TIERING",
        "ONEZONE_IA",
        "OUTPOSTS",
        "STANDARD",
        "STANDARD_IA",
    ] = Field(alias="S3StorageClass")
    s3_config: S3ConfigModel = Field(alias="S3Config")
    agent_arns: List[str] = Field(alias="AgentArns")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLocationSmbRequestModel(BaseModel):
    subdirectory: str = Field(alias="Subdirectory")
    server_hostname: str = Field(alias="ServerHostname")
    user: str = Field(alias="User")
    password: str = Field(alias="Password")
    agent_arns: Sequence[str] = Field(alias="AgentArns")
    domain: Optional[str] = Field(default=None, alias="Domain")
    mount_options: Optional[SmbMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class DescribeLocationSmbResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    agent_arns: List[str] = Field(alias="AgentArns")
    user: str = Field(alias="User")
    domain: str = Field(alias="Domain")
    mount_options: SmbMountOptionsModel = Field(alias="MountOptions")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FsxProtocolSmbModel(BaseModel):
    password: str = Field(alias="Password")
    user: str = Field(alias="User")
    domain: Optional[str] = Field(default=None, alias="Domain")
    mount_options: Optional[SmbMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )


class UpdateLocationSmbRequestModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    user: Optional[str] = Field(default=None, alias="User")
    domain: Optional[str] = Field(default=None, alias="Domain")
    password: Optional[str] = Field(default=None, alias="Password")
    agent_arns: Optional[Sequence[str]] = Field(default=None, alias="AgentArns")
    mount_options: Optional[SmbMountOptionsModel] = Field(
        default=None, alias="MountOptions"
    )


class StartTaskExecutionRequestModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")
    override_options: Optional[OptionsModel] = Field(
        default=None, alias="OverrideOptions"
    )
    includes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Includes"
    )
    excludes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Excludes"
    )
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class UpdateTaskExecutionRequestModel(BaseModel):
    task_execution_arn: str = Field(alias="TaskExecutionArn")
    options: OptionsModel = Field(alias="Options")


class CreateTaskRequestModel(BaseModel):
    source_location_arn: str = Field(alias="SourceLocationArn")
    destination_location_arn: str = Field(alias="DestinationLocationArn")
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    options: Optional[OptionsModel] = Field(default=None, alias="Options")
    excludes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Excludes"
    )
    schedule: Optional[TaskScheduleModel] = Field(default=None, alias="Schedule")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")
    includes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Includes"
    )


class DescribeTaskResponseModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")
    status: Literal[
        "AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"
    ] = Field(alias="Status")
    name: str = Field(alias="Name")
    current_task_execution_arn: str = Field(alias="CurrentTaskExecutionArn")
    source_location_arn: str = Field(alias="SourceLocationArn")
    destination_location_arn: str = Field(alias="DestinationLocationArn")
    cloud_watch_log_group_arn: str = Field(alias="CloudWatchLogGroupArn")
    source_network_interface_arns: List[str] = Field(alias="SourceNetworkInterfaceArns")
    destination_network_interface_arns: List[str] = Field(
        alias="DestinationNetworkInterfaceArns"
    )
    options: OptionsModel = Field(alias="Options")
    excludes: List[FilterRuleModel] = Field(alias="Excludes")
    schedule: TaskScheduleModel = Field(alias="Schedule")
    error_code: str = Field(alias="ErrorCode")
    error_detail: str = Field(alias="ErrorDetail")
    creation_time: datetime = Field(alias="CreationTime")
    includes: List[FilterRuleModel] = Field(alias="Includes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTaskRequestModel(BaseModel):
    task_arn: str = Field(alias="TaskArn")
    options: Optional[OptionsModel] = Field(default=None, alias="Options")
    excludes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Excludes"
    )
    schedule: Optional[TaskScheduleModel] = Field(default=None, alias="Schedule")
    name: Optional[str] = Field(default=None, alias="Name")
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupArn"
    )
    includes: Optional[Sequence[FilterRuleModel]] = Field(
        default=None, alias="Includes"
    )


class DescribeAgentResponseModel(BaseModel):
    agent_arn: str = Field(alias="AgentArn")
    name: str = Field(alias="Name")
    status: Literal["OFFLINE", "ONLINE"] = Field(alias="Status")
    last_connection_time: datetime = Field(alias="LastConnectionTime")
    creation_time: datetime = Field(alias="CreationTime")
    endpoint_type: Literal["FIPS", "PRIVATE_LINK", "PUBLIC"] = Field(
        alias="EndpointType"
    )
    private_link_config: PrivateLinkConfigModel = Field(alias="PrivateLinkConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTaskExecutionResponseModel(BaseModel):
    task_execution_arn: str = Field(alias="TaskExecutionArn")
    status: Literal[
        "ERROR",
        "LAUNCHING",
        "PREPARING",
        "QUEUED",
        "SUCCESS",
        "TRANSFERRING",
        "VERIFYING",
    ] = Field(alias="Status")
    options: OptionsModel = Field(alias="Options")
    excludes: List[FilterRuleModel] = Field(alias="Excludes")
    includes: List[FilterRuleModel] = Field(alias="Includes")
    start_time: datetime = Field(alias="StartTime")
    estimated_files_to_transfer: int = Field(alias="EstimatedFilesToTransfer")
    estimated_bytes_to_transfer: int = Field(alias="EstimatedBytesToTransfer")
    files_transferred: int = Field(alias="FilesTransferred")
    bytes_written: int = Field(alias="BytesWritten")
    bytes_transferred: int = Field(alias="BytesTransferred")
    result: TaskExecutionResultDetailModel = Field(alias="Result")
    bytes_compressed: int = Field(alias="BytesCompressed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAgentsRequestListAgentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTaskExecutionsRequestListTaskExecutionsPaginateModel(BaseModel):
    task_arn: Optional[str] = Field(default=None, alias="TaskArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLocationsRequestListLocationsPaginateModel(BaseModel):
    filters: Optional[Sequence[LocationFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLocationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[LocationFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ListLocationsResponseModel(BaseModel):
    locations: List[LocationListEntryModel] = Field(alias="Locations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTaskExecutionsResponseModel(BaseModel):
    task_executions: List[TaskExecutionListEntryModel] = Field(alias="TaskExecutions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTasksRequestListTasksPaginateModel(BaseModel):
    filters: Optional[Sequence[TaskFilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTasksRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[TaskFilterModel]] = Field(default=None, alias="Filters")


class ListTasksResponseModel(BaseModel):
    tasks: List[TaskListEntryModel] = Field(alias="Tasks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FsxProtocolModel(BaseModel):
    nfs: Optional[FsxProtocolNfsModel] = Field(default=None, alias="NFS")
    s_mb: Optional[FsxProtocolSmbModel] = Field(default=None, alias="SMB")


class CreateLocationFsxOntapRequestModel(BaseModel):
    protocol: FsxProtocolModel = Field(alias="Protocol")
    security_group_arns: Sequence[str] = Field(alias="SecurityGroupArns")
    storage_virtual_machine_arn: str = Field(alias="StorageVirtualMachineArn")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class CreateLocationFsxOpenZfsRequestModel(BaseModel):
    fsx_filesystem_arn: str = Field(alias="FsxFilesystemArn")
    protocol: FsxProtocolModel = Field(alias="Protocol")
    security_group_arns: Sequence[str] = Field(alias="SecurityGroupArns")
    subdirectory: Optional[str] = Field(default=None, alias="Subdirectory")
    tags: Optional[Sequence[TagListEntryModel]] = Field(default=None, alias="Tags")


class DescribeLocationFsxOntapResponseModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    protocol: FsxProtocolModel = Field(alias="Protocol")
    security_group_arns: List[str] = Field(alias="SecurityGroupArns")
    storage_virtual_machine_arn: str = Field(alias="StorageVirtualMachineArn")
    fsx_filesystem_arn: str = Field(alias="FsxFilesystemArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLocationFsxOpenZfsResponseModel(BaseModel):
    location_arn: str = Field(alias="LocationArn")
    location_uri: str = Field(alias="LocationUri")
    security_group_arns: List[str] = Field(alias="SecurityGroupArns")
    protocol: FsxProtocolModel = Field(alias="Protocol")
    creation_time: datetime = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
