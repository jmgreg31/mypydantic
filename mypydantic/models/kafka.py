# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchAssociateScramSecretRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    secret_arn_list: Sequence[str] = Field(alias="SecretArnList")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UnprocessedScramSecretModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")


class BatchDisassociateScramSecretRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    secret_arn_list: Sequence[str] = Field(alias="SecretArnList")


class ProvisionedThroughputModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    volume_throughput: Optional[int] = Field(default=None, alias="VolumeThroughput")


class CloudWatchLogsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")


class FirehoseModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    delivery_stream: Optional[str] = Field(default=None, alias="DeliveryStream")


class S3Model(BaseModel):
    enabled: bool = Field(alias="Enabled")
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class BrokerSoftwareInfoModel(BaseModel):
    configuration_arn: Optional[str] = Field(default=None, alias="ConfigurationArn")
    configuration_revision: Optional[int] = Field(
        default=None, alias="ConfigurationRevision"
    )
    kafka_version: Optional[str] = Field(default=None, alias="KafkaVersion")


class TlsModel(BaseModel):
    certificate_authority_arn_list: Optional[Sequence[str]] = Field(
        default=None, alias="CertificateAuthorityArnList"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UnauthenticatedModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class StateInfoModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class ErrorInfoModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_string: Optional[str] = Field(default=None, alias="ErrorString")


class ClusterOperationStepInfoModel(BaseModel):
    step_status: Optional[str] = Field(default=None, alias="StepStatus")


class CompatibleKafkaVersionModel(BaseModel):
    source_version: Optional[str] = Field(default=None, alias="SourceVersion")
    target_versions: Optional[List[str]] = Field(default=None, alias="TargetVersions")


class ConfigurationInfoModel(BaseModel):
    arn: str = Field(alias="Arn")
    revision: int = Field(alias="Revision")


class ConfigurationRevisionModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    revision: int = Field(alias="Revision")
    description: Optional[str] = Field(default=None, alias="Description")


class PublicAccessModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class CreateConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    server_properties: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="ServerProperties"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    kafka_versions: Optional[Sequence[str]] = Field(default=None, alias="KafkaVersions")


class DeleteClusterRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")


class DeleteConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DescribeClusterOperationRequestModel(BaseModel):
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")


class DescribeClusterRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")


class DescribeClusterV2RequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")


class DescribeConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DescribeConfigurationRevisionRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    revision: int = Field(alias="Revision")


class EncryptionAtRestModel(BaseModel):
    data_volume_kms_key_id: str = Field(alias="DataVolumeKMSKeyId")


class EncryptionInTransitModel(BaseModel):
    client_broker: Optional[Literal["PLAINTEXT", "TLS", "TLS_PLAINTEXT"]] = Field(
        default=None, alias="ClientBroker"
    )
    in_cluster: Optional[bool] = Field(default=None, alias="InCluster")


class GetBootstrapBrokersRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")


class GetCompatibleKafkaVersionsRequestModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")


class IamModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class JmxExporterInfoModel(BaseModel):
    enabled_in_broker: bool = Field(alias="EnabledInBroker")


class JmxExporterModel(BaseModel):
    enabled_in_broker: bool = Field(alias="EnabledInBroker")


class KafkaVersionModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")
    status: Optional[Literal["ACTIVE", "DEPRECATED"]] = Field(
        default=None, alias="Status"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListClusterOperationsRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListClustersRequestModel(BaseModel):
    cluster_name_filter: Optional[str] = Field(default=None, alias="ClusterNameFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListClustersV2RequestModel(BaseModel):
    cluster_name_filter: Optional[str] = Field(default=None, alias="ClusterNameFilter")
    cluster_type_filter: Optional[str] = Field(default=None, alias="ClusterTypeFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationRevisionsRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListKafkaVersionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListNodesRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListScramSecretsRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NodeExporterInfoModel(BaseModel):
    enabled_in_broker: bool = Field(alias="EnabledInBroker")


class NodeExporterModel(BaseModel):
    enabled_in_broker: bool = Field(alias="EnabledInBroker")


class ZookeeperNodeInfoModel(BaseModel):
    attached_eniid: Optional[str] = Field(default=None, alias="AttachedENIId")
    client_vpc_ip_address: Optional[str] = Field(
        default=None, alias="ClientVpcIpAddress"
    )
    endpoints: Optional[List[str]] = Field(default=None, alias="Endpoints")
    zookeeper_id: Optional[float] = Field(default=None, alias="ZookeeperId")
    zookeeper_version: Optional[str] = Field(default=None, alias="ZookeeperVersion")


class RebootBrokerRequestModel(BaseModel):
    broker_ids: Sequence[str] = Field(alias="BrokerIds")
    cluster_arn: str = Field(alias="ClusterArn")


class ScramModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class VpcConfigModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateBrokerCountRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    target_number_of_broker_nodes: int = Field(alias="TargetNumberOfBrokerNodes")


class UpdateBrokerTypeRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    target_instance_type: str = Field(alias="TargetInstanceType")


class UpdateConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    server_properties: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="ServerProperties"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateClusterResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_name: str = Field(alias="ClusterName")
    state: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "FAILED",
        "HEALING",
        "MAINTENANCE",
        "REBOOTING_BROKER",
        "UPDATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterV2ResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_name: str = Field(alias="ClusterName")
    state: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "FAILED",
        "HEALING",
        "MAINTENANCE",
        "REBOOTING_BROKER",
        "UPDATING",
    ] = Field(alias="State")
    cluster_type: Literal["PROVISIONED", "SERVERLESS"] = Field(alias="ClusterType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    state: Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "FAILED",
        "HEALING",
        "MAINTENANCE",
        "REBOOTING_BROKER",
        "UPDATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    state: Literal["ACTIVE", "DELETE_FAILED", "DELETING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationRevisionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    revision: int = Field(alias="Revision")
    server_properties: bytes = Field(alias="ServerProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBootstrapBrokersResponseModel(BaseModel):
    bootstrap_broker_string: str = Field(alias="BootstrapBrokerString")
    bootstrap_broker_string_tls: str = Field(alias="BootstrapBrokerStringTls")
    bootstrap_broker_string_sasl_scram: str = Field(
        alias="BootstrapBrokerStringSaslScram"
    )
    bootstrap_broker_string_sasl_iam: str = Field(alias="BootstrapBrokerStringSaslIam")
    bootstrap_broker_string_public_tls: str = Field(
        alias="BootstrapBrokerStringPublicTls"
    )
    bootstrap_broker_string_public_sasl_scram: str = Field(
        alias="BootstrapBrokerStringPublicSaslScram"
    )
    bootstrap_broker_string_public_sasl_iam: str = Field(
        alias="BootstrapBrokerStringPublicSaslIam"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListScramSecretsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    secret_arn_list: List[str] = Field(alias="SecretArnList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootBrokerResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBrokerCountResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBrokerStorageResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBrokerTypeResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterConfigurationResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterKafkaVersionResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMonitoringResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecurityResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStorageResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    cluster_operation_arn: str = Field(alias="ClusterOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchAssociateScramSecretResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    unprocessed_scram_secrets: List[UnprocessedScramSecretModel] = Field(
        alias="UnprocessedScramSecrets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateScramSecretResponseModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    unprocessed_scram_secrets: List[UnprocessedScramSecretModel] = Field(
        alias="UnprocessedScramSecrets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BrokerEBSVolumeInfoModel(BaseModel):
    kafka_broker_node_id: str = Field(alias="KafkaBrokerNodeId")
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    volume_size_gb: Optional[int] = Field(default=None, alias="VolumeSizeGB")


class EBSStorageInfoModel(BaseModel):
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")


class UpdateStorageRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )
    volume_size_gb: Optional[int] = Field(default=None, alias="VolumeSizeGB")


class BrokerLogsModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsModel] = Field(
        default=None, alias="CloudWatchLogs"
    )
    firehose: Optional[FirehoseModel] = Field(default=None, alias="Firehose")
    s3: Optional[S3Model] = Field(default=None, alias="S3")


class BrokerNodeInfoModel(BaseModel):
    attached_eniid: Optional[str] = Field(default=None, alias="AttachedENIId")
    broker_id: Optional[float] = Field(default=None, alias="BrokerId")
    client_subnet: Optional[str] = Field(default=None, alias="ClientSubnet")
    client_vpc_ip_address: Optional[str] = Field(
        default=None, alias="ClientVpcIpAddress"
    )
    current_broker_software_info: Optional[BrokerSoftwareInfoModel] = Field(
        default=None, alias="CurrentBrokerSoftwareInfo"
    )
    endpoints: Optional[List[str]] = Field(default=None, alias="Endpoints")


class ClusterOperationStepModel(BaseModel):
    step_info: Optional[ClusterOperationStepInfoModel] = Field(
        default=None, alias="StepInfo"
    )
    step_name: Optional[str] = Field(default=None, alias="StepName")


class GetCompatibleKafkaVersionsResponseModel(BaseModel):
    compatible_kafka_versions: List[CompatibleKafkaVersionModel] = Field(
        alias="CompatibleKafkaVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterConfigurationRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    configuration_info: ConfigurationInfoModel = Field(alias="ConfigurationInfo")
    current_version: str = Field(alias="CurrentVersion")


class UpdateClusterKafkaVersionRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    target_kafka_version: str = Field(alias="TargetKafkaVersion")
    configuration_info: Optional[ConfigurationInfoModel] = Field(
        default=None, alias="ConfigurationInfo"
    )


class ConfigurationModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    kafka_versions: List[str] = Field(alias="KafkaVersions")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "DELETE_FAILED", "DELETING"] = Field(alias="State")


class CreateConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "DELETE_FAILED", "DELETING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    description: str = Field(alias="Description")
    kafka_versions: List[str] = Field(alias="KafkaVersions")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "DELETE_FAILED", "DELETING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationRevisionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    revisions: List[ConfigurationRevisionModel] = Field(alias="Revisions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectivityInfoModel(BaseModel):
    public_access: Optional[PublicAccessModel] = Field(
        default=None, alias="PublicAccess"
    )


class EncryptionInfoModel(BaseModel):
    encryption_at_rest: Optional[EncryptionAtRestModel] = Field(
        default=None, alias="EncryptionAtRest"
    )
    encryption_in_transit: Optional[EncryptionInTransitModel] = Field(
        default=None, alias="EncryptionInTransit"
    )


class ServerlessSaslModel(BaseModel):
    iam: Optional[IamModel] = Field(default=None, alias="Iam")


class ListKafkaVersionsResponseModel(BaseModel):
    kafka_versions: List[KafkaVersionModel] = Field(alias="KafkaVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClusterOperationsRequestListClusterOperationsPaginateModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersRequestListClustersPaginateModel(BaseModel):
    cluster_name_filter: Optional[str] = Field(default=None, alias="ClusterNameFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersV2RequestListClustersV2PaginateModel(BaseModel):
    cluster_name_filter: Optional[str] = Field(default=None, alias="ClusterNameFilter")
    cluster_type_filter: Optional[str] = Field(default=None, alias="ClusterTypeFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfigurationRevisionsRequestListConfigurationRevisionsPaginateModel(
    BaseModel
):
    arn: str = Field(alias="Arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfigurationsRequestListConfigurationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKafkaVersionsRequestListKafkaVersionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNodesRequestListNodesPaginateModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListScramSecretsRequestListScramSecretsPaginateModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PrometheusInfoModel(BaseModel):
    jmx_exporter: Optional[JmxExporterInfoModel] = Field(
        default=None, alias="JmxExporter"
    )
    node_exporter: Optional[NodeExporterInfoModel] = Field(
        default=None, alias="NodeExporter"
    )


class PrometheusModel(BaseModel):
    jmx_exporter: Optional[JmxExporterModel] = Field(default=None, alias="JmxExporter")
    node_exporter: Optional[NodeExporterModel] = Field(
        default=None, alias="NodeExporter"
    )


class SaslModel(BaseModel):
    scram: Optional[ScramModel] = Field(default=None, alias="Scram")
    iam: Optional[IamModel] = Field(default=None, alias="Iam")


class UpdateBrokerStorageRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    target_broker_ebs_volume_info: Sequence[BrokerEBSVolumeInfoModel] = Field(
        alias="TargetBrokerEBSVolumeInfo"
    )


class StorageInfoModel(BaseModel):
    ebs_storage_info: Optional[EBSStorageInfoModel] = Field(
        default=None, alias="EbsStorageInfo"
    )


class LoggingInfoModel(BaseModel):
    broker_logs: BrokerLogsModel = Field(alias="BrokerLogs")


class NodeInfoModel(BaseModel):
    added_to_cluster_time: Optional[str] = Field(
        default=None, alias="AddedToClusterTime"
    )
    broker_node_info: Optional[BrokerNodeInfoModel] = Field(
        default=None, alias="BrokerNodeInfo"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    node_arn: Optional[str] = Field(default=None, alias="NodeARN")
    node_type: Optional[Literal["BROKER"]] = Field(default=None, alias="NodeType")
    zookeeper_node_info: Optional[ZookeeperNodeInfoModel] = Field(
        default=None, alias="ZookeeperNodeInfo"
    )


class ListConfigurationsResponseModel(BaseModel):
    configurations: List[ConfigurationModel] = Field(alias="Configurations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    connectivity_info: ConnectivityInfoModel = Field(alias="ConnectivityInfo")
    current_version: str = Field(alias="CurrentVersion")


class ServerlessClientAuthenticationModel(BaseModel):
    sasl: Optional[ServerlessSaslModel] = Field(default=None, alias="Sasl")


class OpenMonitoringInfoModel(BaseModel):
    prometheus: PrometheusInfoModel = Field(alias="Prometheus")


class OpenMonitoringModel(BaseModel):
    prometheus: PrometheusModel = Field(alias="Prometheus")


class ClientAuthenticationModel(BaseModel):
    sasl: Optional[SaslModel] = Field(default=None, alias="Sasl")
    tls: Optional[TlsModel] = Field(default=None, alias="Tls")
    unauthenticated: Optional[UnauthenticatedModel] = Field(
        default=None, alias="Unauthenticated"
    )


class BrokerNodeGroupInfoModel(BaseModel):
    client_subnets: Sequence[str] = Field(alias="ClientSubnets")
    instance_type: str = Field(alias="InstanceType")
    broker_azdistribution: Optional[Literal["DEFAULT"]] = Field(
        default=None, alias="BrokerAZDistribution"
    )
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    storage_info: Optional[StorageInfoModel] = Field(default=None, alias="StorageInfo")
    connectivity_info: Optional[ConnectivityInfoModel] = Field(
        default=None, alias="ConnectivityInfo"
    )


class ListNodesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    node_info_list: List[NodeInfoModel] = Field(alias="NodeInfoList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServerlessRequestModel(BaseModel):
    vpc_configs: Sequence[VpcConfigModel] = Field(alias="VpcConfigs")
    client_authentication: Optional[ServerlessClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )


class ServerlessModel(BaseModel):
    vpc_configs: List[VpcConfigModel] = Field(alias="VpcConfigs")
    client_authentication: Optional[ServerlessClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )


class UpdateMonitoringRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringInfoModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")


class MutableClusterInfoModel(BaseModel):
    broker_ebs_volume_info: Optional[List[BrokerEBSVolumeInfoModel]] = Field(
        default=None, alias="BrokerEBSVolumeInfo"
    )
    configuration_info: Optional[ConfigurationInfoModel] = Field(
        default=None, alias="ConfigurationInfo"
    )
    number_of_broker_nodes: Optional[int] = Field(
        default=None, alias="NumberOfBrokerNodes"
    )
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    kafka_version: Optional[str] = Field(default=None, alias="KafkaVersion")
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )
    connectivity_info: Optional[ConnectivityInfoModel] = Field(
        default=None, alias="ConnectivityInfo"
    )
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )


class UpdateSecurityRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    current_version: str = Field(alias="CurrentVersion")
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )


class ClusterInfoModel(BaseModel):
    active_operation_arn: Optional[str] = Field(
        default=None, alias="ActiveOperationArn"
    )
    broker_node_group_info: Optional[BrokerNodeGroupInfoModel] = Field(
        default=None, alias="BrokerNodeGroupInfo"
    )
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    current_broker_software_info: Optional[BrokerSoftwareInfoModel] = Field(
        default=None, alias="CurrentBrokerSoftwareInfo"
    )
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    number_of_broker_nodes: Optional[int] = Field(
        default=None, alias="NumberOfBrokerNodes"
    )
    state: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "DELETING",
            "FAILED",
            "HEALING",
            "MAINTENANCE",
            "REBOOTING_BROKER",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    state_info: Optional[StateInfoModel] = Field(default=None, alias="StateInfo")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    zookeeper_connect_string: Optional[str] = Field(
        default=None, alias="ZookeeperConnectString"
    )
    zookeeper_connect_string_tls: Optional[str] = Field(
        default=None, alias="ZookeeperConnectStringTls"
    )
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )


class CreateClusterRequestModel(BaseModel):
    broker_node_group_info: BrokerNodeGroupInfoModel = Field(
        alias="BrokerNodeGroupInfo"
    )
    cluster_name: str = Field(alias="ClusterName")
    kafka_version: str = Field(alias="KafkaVersion")
    number_of_broker_nodes: int = Field(alias="NumberOfBrokerNodes")
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    configuration_info: Optional[ConfigurationInfoModel] = Field(
        default=None, alias="ConfigurationInfo"
    )
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringInfoModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )


class ProvisionedRequestModel(BaseModel):
    broker_node_group_info: BrokerNodeGroupInfoModel = Field(
        alias="BrokerNodeGroupInfo"
    )
    kafka_version: str = Field(alias="KafkaVersion")
    number_of_broker_nodes: int = Field(alias="NumberOfBrokerNodes")
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    configuration_info: Optional[ConfigurationInfoModel] = Field(
        default=None, alias="ConfigurationInfo"
    )
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringInfoModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )


class ProvisionedModel(BaseModel):
    broker_node_group_info: BrokerNodeGroupInfoModel = Field(
        alias="BrokerNodeGroupInfo"
    )
    number_of_broker_nodes: int = Field(alias="NumberOfBrokerNodes")
    current_broker_software_info: Optional[BrokerSoftwareInfoModel] = Field(
        default=None, alias="CurrentBrokerSoftwareInfo"
    )
    client_authentication: Optional[ClientAuthenticationModel] = Field(
        default=None, alias="ClientAuthentication"
    )
    encryption_info: Optional[EncryptionInfoModel] = Field(
        default=None, alias="EncryptionInfo"
    )
    enhanced_monitoring: Optional[
        Literal[
            "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
        ]
    ] = Field(default=None, alias="EnhancedMonitoring")
    open_monitoring: Optional[OpenMonitoringInfoModel] = Field(
        default=None, alias="OpenMonitoring"
    )
    logging_info: Optional[LoggingInfoModel] = Field(default=None, alias="LoggingInfo")
    zookeeper_connect_string: Optional[str] = Field(
        default=None, alias="ZookeeperConnectString"
    )
    zookeeper_connect_string_tls: Optional[str] = Field(
        default=None, alias="ZookeeperConnectStringTls"
    )
    storage_mode: Optional[Literal["LOCAL", "TIERED"]] = Field(
        default=None, alias="StorageMode"
    )


class ClusterOperationInfoModel(BaseModel):
    client_request_id: Optional[str] = Field(default=None, alias="ClientRequestId")
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    error_info: Optional[ErrorInfoModel] = Field(default=None, alias="ErrorInfo")
    operation_arn: Optional[str] = Field(default=None, alias="OperationArn")
    operation_state: Optional[str] = Field(default=None, alias="OperationState")
    operation_steps: Optional[List[ClusterOperationStepModel]] = Field(
        default=None, alias="OperationSteps"
    )
    operation_type: Optional[str] = Field(default=None, alias="OperationType")
    source_cluster_info: Optional[MutableClusterInfoModel] = Field(
        default=None, alias="SourceClusterInfo"
    )
    target_cluster_info: Optional[MutableClusterInfoModel] = Field(
        default=None, alias="TargetClusterInfo"
    )


class DescribeClusterResponseModel(BaseModel):
    cluster_info: ClusterInfoModel = Field(alias="ClusterInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersResponseModel(BaseModel):
    cluster_info_list: List[ClusterInfoModel] = Field(alias="ClusterInfoList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterV2RequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    provisioned: Optional[ProvisionedRequestModel] = Field(
        default=None, alias="Provisioned"
    )
    serverless: Optional[ServerlessRequestModel] = Field(
        default=None, alias="Serverless"
    )


class ClusterModel(BaseModel):
    active_operation_arn: Optional[str] = Field(
        default=None, alias="ActiveOperationArn"
    )
    cluster_type: Optional[Literal["PROVISIONED", "SERVERLESS"]] = Field(
        default=None, alias="ClusterType"
    )
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")
    state: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "DELETING",
            "FAILED",
            "HEALING",
            "MAINTENANCE",
            "REBOOTING_BROKER",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    state_info: Optional[StateInfoModel] = Field(default=None, alias="StateInfo")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    provisioned: Optional[ProvisionedModel] = Field(default=None, alias="Provisioned")
    serverless: Optional[ServerlessModel] = Field(default=None, alias="Serverless")


class DescribeClusterOperationResponseModel(BaseModel):
    cluster_operation_info: ClusterOperationInfoModel = Field(
        alias="ClusterOperationInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClusterOperationsResponseModel(BaseModel):
    cluster_operation_info_list: List[ClusterOperationInfoModel] = Field(
        alias="ClusterOperationInfoList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClusterV2ResponseModel(BaseModel):
    cluster_info: ClusterModel = Field(alias="ClusterInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersV2ResponseModel(BaseModel):
    cluster_info_list: List[ClusterModel] = Field(alias="ClusterInfoList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
