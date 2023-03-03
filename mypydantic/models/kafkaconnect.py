# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class VpcDescriptionModel(BaseModel):
    security_groups: Optional[List[str]] = Field(default=None, alias="securityGroups")
    subnets: Optional[List[str]] = Field(default=None, alias="subnets")


class VpcModel(BaseModel):
    subnets: Sequence[str] = Field(alias="subnets")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroups"
    )


class ScaleInPolicyDescriptionModel(BaseModel):
    cpu_utilization_percentage: Optional[int] = Field(
        default=None, alias="cpuUtilizationPercentage"
    )


class ScaleOutPolicyDescriptionModel(BaseModel):
    cpu_utilization_percentage: Optional[int] = Field(
        default=None, alias="cpuUtilizationPercentage"
    )


class ScaleInPolicyModel(BaseModel):
    cpu_utilization_percentage: int = Field(alias="cpuUtilizationPercentage")


class ScaleOutPolicyModel(BaseModel):
    cpu_utilization_percentage: int = Field(alias="cpuUtilizationPercentage")


class ScaleInPolicyUpdateModel(BaseModel):
    cpu_utilization_percentage: int = Field(alias="cpuUtilizationPercentage")


class ScaleOutPolicyUpdateModel(BaseModel):
    cpu_utilization_percentage: int = Field(alias="cpuUtilizationPercentage")


class ProvisionedCapacityDescriptionModel(BaseModel):
    mcu_count: Optional[int] = Field(default=None, alias="mcuCount")
    worker_count: Optional[int] = Field(default=None, alias="workerCount")


class ProvisionedCapacityModel(BaseModel):
    mcu_count: int = Field(alias="mcuCount")
    worker_count: int = Field(alias="workerCount")


class ProvisionedCapacityUpdateModel(BaseModel):
    mcu_count: int = Field(alias="mcuCount")
    worker_count: int = Field(alias="workerCount")


class CloudWatchLogsLogDeliveryDescriptionModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    log_group: Optional[str] = Field(default=None, alias="logGroup")


class CloudWatchLogsLogDeliveryModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    log_group: Optional[str] = Field(default=None, alias="logGroup")


class KafkaClusterClientAuthenticationDescriptionModel(BaseModel):
    authentication_type: Optional[Literal["IAM", "NONE"]] = Field(
        default=None, alias="authenticationType"
    )


class KafkaClusterEncryptionInTransitDescriptionModel(BaseModel):
    encryption_type: Optional[Literal["PLAINTEXT", "TLS"]] = Field(
        default=None, alias="encryptionType"
    )


class WorkerConfigurationDescriptionModel(BaseModel):
    revision: Optional[int] = Field(default=None, alias="revision")
    worker_configuration_arn: Optional[str] = Field(
        default=None, alias="workerConfigurationArn"
    )


class KafkaClusterClientAuthenticationModel(BaseModel):
    authentication_type: Literal["IAM", "NONE"] = Field(alias="authenticationType")


class KafkaClusterEncryptionInTransitModel(BaseModel):
    encryption_type: Literal["PLAINTEXT", "TLS"] = Field(alias="encryptionType")


class WorkerConfigurationModel(BaseModel):
    revision: int = Field(alias="revision")
    worker_configuration_arn: str = Field(alias="workerConfigurationArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateWorkerConfigurationRequestModel(BaseModel):
    name: str = Field(alias="name")
    properties_file_content: str = Field(alias="propertiesFileContent")
    description: Optional[str] = Field(default=None, alias="description")


class WorkerConfigurationRevisionSummaryModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    description: Optional[str] = Field(default=None, alias="description")
    revision: Optional[int] = Field(default=None, alias="revision")


class CustomPluginDescriptionModel(BaseModel):
    custom_plugin_arn: Optional[str] = Field(default=None, alias="customPluginArn")
    revision: Optional[int] = Field(default=None, alias="revision")


class CustomPluginFileDescriptionModel(BaseModel):
    file_md5: Optional[str] = Field(default=None, alias="fileMd5")
    file_size: Optional[int] = Field(default=None, alias="fileSize")


class S3LocationDescriptionModel(BaseModel):
    bucket_arn: Optional[str] = Field(default=None, alias="bucketArn")
    file_key: Optional[str] = Field(default=None, alias="fileKey")
    object_version: Optional[str] = Field(default=None, alias="objectVersion")


class S3LocationModel(BaseModel):
    bucket_arn: str = Field(alias="bucketArn")
    file_key: str = Field(alias="fileKey")
    object_version: Optional[str] = Field(default=None, alias="objectVersion")


class CustomPluginModel(BaseModel):
    custom_plugin_arn: str = Field(alias="customPluginArn")
    revision: int = Field(alias="revision")


class DeleteConnectorRequestModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    current_version: Optional[str] = Field(default=None, alias="currentVersion")


class DeleteCustomPluginRequestModel(BaseModel):
    custom_plugin_arn: str = Field(alias="customPluginArn")


class DescribeConnectorRequestModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")


class StateDescriptionModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class DescribeCustomPluginRequestModel(BaseModel):
    custom_plugin_arn: str = Field(alias="customPluginArn")


class DescribeWorkerConfigurationRequestModel(BaseModel):
    worker_configuration_arn: str = Field(alias="workerConfigurationArn")


class WorkerConfigurationRevisionDescriptionModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    description: Optional[str] = Field(default=None, alias="description")
    properties_file_content: Optional[str] = Field(
        default=None, alias="propertiesFileContent"
    )
    revision: Optional[int] = Field(default=None, alias="revision")


class FirehoseLogDeliveryDescriptionModel(BaseModel):
    delivery_stream: Optional[str] = Field(default=None, alias="deliveryStream")
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class FirehoseLogDeliveryModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    delivery_stream: Optional[str] = Field(default=None, alias="deliveryStream")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListConnectorsRequestModel(BaseModel):
    connector_name_prefix: Optional[str] = Field(
        default=None, alias="connectorNamePrefix"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCustomPluginsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListWorkerConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class S3LogDeliveryDescriptionModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class S3LogDeliveryModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    bucket: Optional[str] = Field(default=None, alias="bucket")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class ApacheKafkaClusterDescriptionModel(BaseModel):
    bootstrap_servers: Optional[str] = Field(default=None, alias="bootstrapServers")
    vpc: Optional[VpcDescriptionModel] = Field(default=None, alias="vpc")


class ApacheKafkaClusterModel(BaseModel):
    bootstrap_servers: str = Field(alias="bootstrapServers")
    vpc: VpcModel = Field(alias="vpc")


class AutoScalingDescriptionModel(BaseModel):
    max_worker_count: Optional[int] = Field(default=None, alias="maxWorkerCount")
    mcu_count: Optional[int] = Field(default=None, alias="mcuCount")
    min_worker_count: Optional[int] = Field(default=None, alias="minWorkerCount")
    scale_in_policy: Optional[ScaleInPolicyDescriptionModel] = Field(
        default=None, alias="scaleInPolicy"
    )
    scale_out_policy: Optional[ScaleOutPolicyDescriptionModel] = Field(
        default=None, alias="scaleOutPolicy"
    )


class AutoScalingModel(BaseModel):
    max_worker_count: int = Field(alias="maxWorkerCount")
    mcu_count: int = Field(alias="mcuCount")
    min_worker_count: int = Field(alias="minWorkerCount")
    scale_in_policy: Optional[ScaleInPolicyModel] = Field(
        default=None, alias="scaleInPolicy"
    )
    scale_out_policy: Optional[ScaleOutPolicyModel] = Field(
        default=None, alias="scaleOutPolicy"
    )


class AutoScalingUpdateModel(BaseModel):
    max_worker_count: int = Field(alias="maxWorkerCount")
    mcu_count: int = Field(alias="mcuCount")
    min_worker_count: int = Field(alias="minWorkerCount")
    scale_in_policy: ScaleInPolicyUpdateModel = Field(alias="scaleInPolicy")
    scale_out_policy: ScaleOutPolicyUpdateModel = Field(alias="scaleOutPolicy")


class CreateConnectorResponseModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    connector_name: str = Field(alias="connectorName")
    connector_state: Literal[
        "CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"
    ] = Field(alias="connectorState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomPluginResponseModel(BaseModel):
    custom_plugin_arn: str = Field(alias="customPluginArn")
    custom_plugin_state: Literal[
        "ACTIVE", "CREATE_FAILED", "CREATING", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="customPluginState")
    name: str = Field(alias="name")
    revision: int = Field(alias="revision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConnectorResponseModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    connector_state: Literal[
        "CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"
    ] = Field(alias="connectorState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCustomPluginResponseModel(BaseModel):
    custom_plugin_arn: str = Field(alias="customPluginArn")
    custom_plugin_state: Literal[
        "ACTIVE", "CREATE_FAILED", "CREATING", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="customPluginState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectorResponseModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    connector_state: Literal[
        "CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"
    ] = Field(alias="connectorState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkerConfigurationResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    latest_revision: WorkerConfigurationRevisionSummaryModel = Field(
        alias="latestRevision"
    )
    name: str = Field(alias="name")
    worker_configuration_arn: str = Field(alias="workerConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkerConfigurationSummaryModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    description: Optional[str] = Field(default=None, alias="description")
    latest_revision: Optional[WorkerConfigurationRevisionSummaryModel] = Field(
        default=None, alias="latestRevision"
    )
    name: Optional[str] = Field(default=None, alias="name")
    worker_configuration_arn: Optional[str] = Field(
        default=None, alias="workerConfigurationArn"
    )


class PluginDescriptionModel(BaseModel):
    custom_plugin: Optional[CustomPluginDescriptionModel] = Field(
        default=None, alias="customPlugin"
    )


class CustomPluginLocationDescriptionModel(BaseModel):
    s3_location: Optional[S3LocationDescriptionModel] = Field(
        default=None, alias="s3Location"
    )


class CustomPluginLocationModel(BaseModel):
    s3_location: S3LocationModel = Field(alias="s3Location")


class PluginModel(BaseModel):
    custom_plugin: CustomPluginModel = Field(alias="customPlugin")


class DescribeWorkerConfigurationResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    description: str = Field(alias="description")
    latest_revision: WorkerConfigurationRevisionDescriptionModel = Field(
        alias="latestRevision"
    )
    name: str = Field(alias="name")
    worker_configuration_arn: str = Field(alias="workerConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectorsRequestListConnectorsPaginateModel(BaseModel):
    connector_name_prefix: Optional[str] = Field(
        default=None, alias="connectorNamePrefix"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomPluginsRequestListCustomPluginsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class WorkerLogDeliveryDescriptionModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsLogDeliveryDescriptionModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    firehose: Optional[FirehoseLogDeliveryDescriptionModel] = Field(
        default=None, alias="firehose"
    )
    s3: Optional[S3LogDeliveryDescriptionModel] = Field(default=None, alias="s3")


class WorkerLogDeliveryModel(BaseModel):
    cloud_watch_logs: Optional[CloudWatchLogsLogDeliveryModel] = Field(
        default=None, alias="cloudWatchLogs"
    )
    firehose: Optional[FirehoseLogDeliveryModel] = Field(default=None, alias="firehose")
    s3: Optional[S3LogDeliveryModel] = Field(default=None, alias="s3")


class KafkaClusterDescriptionModel(BaseModel):
    apache_kafka_cluster: Optional[ApacheKafkaClusterDescriptionModel] = Field(
        default=None, alias="apacheKafkaCluster"
    )


class KafkaClusterModel(BaseModel):
    apache_kafka_cluster: ApacheKafkaClusterModel = Field(alias="apacheKafkaCluster")


class CapacityDescriptionModel(BaseModel):
    auto_scaling: Optional[AutoScalingDescriptionModel] = Field(
        default=None, alias="autoScaling"
    )
    provisioned_capacity: Optional[ProvisionedCapacityDescriptionModel] = Field(
        default=None, alias="provisionedCapacity"
    )


class CapacityModel(BaseModel):
    auto_scaling: Optional[AutoScalingModel] = Field(default=None, alias="autoScaling")
    provisioned_capacity: Optional[ProvisionedCapacityModel] = Field(
        default=None, alias="provisionedCapacity"
    )


class CapacityUpdateModel(BaseModel):
    auto_scaling: Optional[AutoScalingUpdateModel] = Field(
        default=None, alias="autoScaling"
    )
    provisioned_capacity: Optional[ProvisionedCapacityUpdateModel] = Field(
        default=None, alias="provisionedCapacity"
    )


class ListWorkerConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    worker_configurations: List[WorkerConfigurationSummaryModel] = Field(
        alias="workerConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomPluginRevisionSummaryModel(BaseModel):
    content_type: Optional[Literal["JAR", "ZIP"]] = Field(
        default=None, alias="contentType"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    description: Optional[str] = Field(default=None, alias="description")
    file_description: Optional[CustomPluginFileDescriptionModel] = Field(
        default=None, alias="fileDescription"
    )
    location: Optional[CustomPluginLocationDescriptionModel] = Field(
        default=None, alias="location"
    )
    revision: Optional[int] = Field(default=None, alias="revision")


class CreateCustomPluginRequestModel(BaseModel):
    content_type: Literal["JAR", "ZIP"] = Field(alias="contentType")
    location: CustomPluginLocationModel = Field(alias="location")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class LogDeliveryDescriptionModel(BaseModel):
    worker_log_delivery: Optional[WorkerLogDeliveryDescriptionModel] = Field(
        default=None, alias="workerLogDelivery"
    )


class LogDeliveryModel(BaseModel):
    worker_log_delivery: WorkerLogDeliveryModel = Field(alias="workerLogDelivery")


class UpdateConnectorRequestModel(BaseModel):
    capacity: CapacityUpdateModel = Field(alias="capacity")
    connector_arn: str = Field(alias="connectorArn")
    current_version: str = Field(alias="currentVersion")


class CustomPluginSummaryModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    custom_plugin_arn: Optional[str] = Field(default=None, alias="customPluginArn")
    custom_plugin_state: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="customPluginState")
    description: Optional[str] = Field(default=None, alias="description")
    latest_revision: Optional[CustomPluginRevisionSummaryModel] = Field(
        default=None, alias="latestRevision"
    )
    name: Optional[str] = Field(default=None, alias="name")


class DescribeCustomPluginResponseModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    custom_plugin_arn: str = Field(alias="customPluginArn")
    custom_plugin_state: Literal[
        "ACTIVE", "CREATE_FAILED", "CREATING", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="customPluginState")
    description: str = Field(alias="description")
    latest_revision: CustomPluginRevisionSummaryModel = Field(alias="latestRevision")
    name: str = Field(alias="name")
    state_description: StateDescriptionModel = Field(alias="stateDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectorSummaryModel(BaseModel):
    capacity: Optional[CapacityDescriptionModel] = Field(default=None, alias="capacity")
    connector_arn: Optional[str] = Field(default=None, alias="connectorArn")
    connector_description: Optional[str] = Field(
        default=None, alias="connectorDescription"
    )
    connector_name: Optional[str] = Field(default=None, alias="connectorName")
    connector_state: Optional[
        Literal["CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"]
    ] = Field(default=None, alias="connectorState")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    current_version: Optional[str] = Field(default=None, alias="currentVersion")
    kafka_cluster: Optional[KafkaClusterDescriptionModel] = Field(
        default=None, alias="kafkaCluster"
    )
    kafka_cluster_client_authentication: Optional[
        KafkaClusterClientAuthenticationDescriptionModel
    ] = Field(default=None, alias="kafkaClusterClientAuthentication")
    kafka_cluster_encryption_in_transit: Optional[
        KafkaClusterEncryptionInTransitDescriptionModel
    ] = Field(default=None, alias="kafkaClusterEncryptionInTransit")
    kafka_connect_version: Optional[str] = Field(
        default=None, alias="kafkaConnectVersion"
    )
    log_delivery: Optional[LogDeliveryDescriptionModel] = Field(
        default=None, alias="logDelivery"
    )
    plugins: Optional[List[PluginDescriptionModel]] = Field(
        default=None, alias="plugins"
    )
    service_execution_role_arn: Optional[str] = Field(
        default=None, alias="serviceExecutionRoleArn"
    )
    worker_configuration: Optional[WorkerConfigurationDescriptionModel] = Field(
        default=None, alias="workerConfiguration"
    )


class DescribeConnectorResponseModel(BaseModel):
    capacity: CapacityDescriptionModel = Field(alias="capacity")
    connector_arn: str = Field(alias="connectorArn")
    connector_configuration: Dict[str, str] = Field(alias="connectorConfiguration")
    connector_description: str = Field(alias="connectorDescription")
    connector_name: str = Field(alias="connectorName")
    connector_state: Literal[
        "CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"
    ] = Field(alias="connectorState")
    creation_time: datetime = Field(alias="creationTime")
    current_version: str = Field(alias="currentVersion")
    kafka_cluster: KafkaClusterDescriptionModel = Field(alias="kafkaCluster")
    kafka_cluster_client_authentication: KafkaClusterClientAuthenticationDescriptionModel = Field(
        alias="kafkaClusterClientAuthentication"
    )
    kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransitDescriptionModel = Field(
        alias="kafkaClusterEncryptionInTransit"
    )
    kafka_connect_version: str = Field(alias="kafkaConnectVersion")
    log_delivery: LogDeliveryDescriptionModel = Field(alias="logDelivery")
    plugins: List[PluginDescriptionModel] = Field(alias="plugins")
    service_execution_role_arn: str = Field(alias="serviceExecutionRoleArn")
    state_description: StateDescriptionModel = Field(alias="stateDescription")
    worker_configuration: WorkerConfigurationDescriptionModel = Field(
        alias="workerConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectorRequestModel(BaseModel):
    capacity: CapacityModel = Field(alias="capacity")
    connector_configuration: Mapping[str, str] = Field(alias="connectorConfiguration")
    connector_name: str = Field(alias="connectorName")
    kafka_cluster: KafkaClusterModel = Field(alias="kafkaCluster")
    kafka_cluster_client_authentication: KafkaClusterClientAuthenticationModel = Field(
        alias="kafkaClusterClientAuthentication"
    )
    kafka_cluster_encryption_in_transit: KafkaClusterEncryptionInTransitModel = Field(
        alias="kafkaClusterEncryptionInTransit"
    )
    kafka_connect_version: str = Field(alias="kafkaConnectVersion")
    plugins: Sequence[PluginModel] = Field(alias="plugins")
    service_execution_role_arn: str = Field(alias="serviceExecutionRoleArn")
    connector_description: Optional[str] = Field(
        default=None, alias="connectorDescription"
    )
    log_delivery: Optional[LogDeliveryModel] = Field(default=None, alias="logDelivery")
    worker_configuration: Optional[WorkerConfigurationModel] = Field(
        default=None, alias="workerConfiguration"
    )


class ListCustomPluginsResponseModel(BaseModel):
    custom_plugins: List[CustomPluginSummaryModel] = Field(alias="customPlugins")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectorsResponseModel(BaseModel):
    connectors: List[ConnectorSummaryModel] = Field(alias="connectors")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
