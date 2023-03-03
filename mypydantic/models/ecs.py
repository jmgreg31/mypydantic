# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttachmentStateChangeModel(BaseModel):
    attachment_arn: str = Field(alias="attachmentArn")
    status: str = Field(alias="status")


class KeyValuePairModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class AttributeModel(BaseModel):
    name: str = Field(alias="name")
    value: Optional[str] = Field(default=None, alias="value")
    target_type: Optional[Literal["container-instance"]] = Field(
        default=None, alias="targetType"
    )
    target_id: Optional[str] = Field(default=None, alias="targetId")


class ManagedScalingModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )
    target_capacity: Optional[int] = Field(default=None, alias="targetCapacity")
    minimum_scaling_step_size: Optional[int] = Field(
        default=None, alias="minimumScalingStepSize"
    )
    maximum_scaling_step_size: Optional[int] = Field(
        default=None, alias="maximumScalingStepSize"
    )
    instance_warmup_period: Optional[int] = Field(
        default=None, alias="instanceWarmupPeriod"
    )


class AwsVpcConfigurationModel(BaseModel):
    subnets: Sequence[str] = Field(alias="subnets")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroups"
    )
    assign_public_ip: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="assignPublicIp"
    )


class CapacityProviderStrategyItemModel(BaseModel):
    capacity_provider: str = Field(alias="capacityProvider")
    weight: Optional[int] = Field(default=None, alias="weight")
    base: Optional[int] = Field(default=None, alias="base")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ClusterServiceConnectDefaultsRequestModel(BaseModel):
    namespace: str = Field(alias="namespace")


class ClusterServiceConnectDefaultsModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="namespace")


class ClusterSettingModel(BaseModel):
    name: Optional[Literal["containerInsights"]] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class ContainerDependencyModel(BaseModel):
    container_name: str = Field(alias="containerName")
    condition: Literal["COMPLETE", "HEALTHY", "START", "SUCCESS"] = Field(
        alias="condition"
    )


class EnvironmentFileModel(BaseModel):
    value: str = Field(alias="value")
    type: Literal["s3"] = Field(alias="type")


class FirelensConfigurationModel(BaseModel):
    type: Literal["fluentbit", "fluentd"] = Field(alias="type")
    options: Optional[Dict[str, str]] = Field(default=None, alias="options")


class HealthCheckModel(BaseModel):
    command: List[str] = Field(alias="command")
    interval: Optional[int] = Field(default=None, alias="interval")
    timeout: Optional[int] = Field(default=None, alias="timeout")
    retries: Optional[int] = Field(default=None, alias="retries")
    start_period: Optional[int] = Field(default=None, alias="startPeriod")


class HostEntryModel(BaseModel):
    hostname: str = Field(alias="hostname")
    ip_address: str = Field(alias="ipAddress")


class MountPointModel(BaseModel):
    source_volume: Optional[str] = Field(default=None, alias="sourceVolume")
    container_path: Optional[str] = Field(default=None, alias="containerPath")
    read_only: Optional[bool] = Field(default=None, alias="readOnly")


class PortMappingModel(BaseModel):
    container_port: Optional[int] = Field(default=None, alias="containerPort")
    host_port: Optional[int] = Field(default=None, alias="hostPort")
    protocol: Optional[Literal["tcp", "udp"]] = Field(default=None, alias="protocol")
    name: Optional[str] = Field(default=None, alias="name")
    app_protocol: Optional[Literal["grpc", "http", "http2"]] = Field(
        default=None, alias="appProtocol"
    )
    container_port_range: Optional[str] = Field(
        default=None, alias="containerPortRange"
    )


class RepositoryCredentialsModel(BaseModel):
    credentials_parameter: str = Field(alias="credentialsParameter")


class ResourceRequirementModel(BaseModel):
    value: str = Field(alias="value")
    type: Literal["GPU", "InferenceAccelerator"] = Field(alias="type")


class SecretModel(BaseModel):
    name: str = Field(alias="name")
    value_from: str = Field(alias="valueFrom")


class SystemControlModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="namespace")
    value: Optional[str] = Field(default=None, alias="value")


class UlimitModel(BaseModel):
    name: Literal[
        "core",
        "cpu",
        "data",
        "fsize",
        "locks",
        "memlock",
        "msgqueue",
        "nice",
        "nofile",
        "nproc",
        "rss",
        "rtprio",
        "rttime",
        "sigpending",
        "stack",
    ] = Field(alias="name")
    soft_limit: int = Field(alias="softLimit")
    hard_limit: int = Field(alias="hardLimit")


class VolumeFromModel(BaseModel):
    source_container: Optional[str] = Field(default=None, alias="sourceContainer")
    read_only: Optional[bool] = Field(default=None, alias="readOnly")


class InstanceHealthCheckResultModel(BaseModel):
    type: Optional[Literal["CONTAINER_RUNTIME"]] = Field(default=None, alias="type")
    status: Optional[
        Literal["IMPAIRED", "INITIALIZING", "INSUFFICIENT_DATA", "OK"]
    ] = Field(default=None, alias="status")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")
    last_status_change: Optional[datetime] = Field(
        default=None, alias="lastStatusChange"
    )


class ResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    long_value: Optional[int] = Field(default=None, alias="longValue")
    integer_value: Optional[int] = Field(default=None, alias="integerValue")
    string_set_value: Optional[List[str]] = Field(default=None, alias="stringSetValue")


class VersionInfoModel(BaseModel):
    agent_version: Optional[str] = Field(default=None, alias="agentVersion")
    agent_hash: Optional[str] = Field(default=None, alias="agentHash")
    docker_version: Optional[str] = Field(default=None, alias="dockerVersion")


class NetworkBindingModel(BaseModel):
    bind_ip: Optional[str] = Field(default=None, alias="bindIP")
    container_port: Optional[int] = Field(default=None, alias="containerPort")
    host_port: Optional[int] = Field(default=None, alias="hostPort")
    protocol: Optional[Literal["tcp", "udp"]] = Field(default=None, alias="protocol")
    container_port_range: Optional[str] = Field(
        default=None, alias="containerPortRange"
    )
    host_port_range: Optional[str] = Field(default=None, alias="hostPortRange")


class ManagedAgentModel(BaseModel):
    last_started_at: Optional[datetime] = Field(default=None, alias="lastStartedAt")
    name: Optional[Literal["ExecuteCommandAgent"]] = Field(default=None, alias="name")
    reason: Optional[str] = Field(default=None, alias="reason")
    last_status: Optional[str] = Field(default=None, alias="lastStatus")


class NetworkInterfaceModel(BaseModel):
    attachment_id: Optional[str] = Field(default=None, alias="attachmentId")
    private_ipv4_address: Optional[str] = Field(
        default=None, alias="privateIpv4Address"
    )
    ipv6_address: Optional[str] = Field(default=None, alias="ipv6Address")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeploymentControllerModel(BaseModel):
    type: Literal["CODE_DEPLOY", "ECS", "EXTERNAL"] = Field(alias="type")


class LoadBalancerModel(BaseModel):
    target_group_arn: Optional[str] = Field(default=None, alias="targetGroupArn")
    load_balancer_name: Optional[str] = Field(default=None, alias="loadBalancerName")
    container_name: Optional[str] = Field(default=None, alias="containerName")
    container_port: Optional[int] = Field(default=None, alias="containerPort")


class PlacementConstraintModel(BaseModel):
    type: Optional[Literal["distinctInstance", "memberOf"]] = Field(
        default=None, alias="type"
    )
    expression: Optional[str] = Field(default=None, alias="expression")


class PlacementStrategyModel(BaseModel):
    type: Optional[Literal["binpack", "random", "spread"]] = Field(
        default=None, alias="type"
    )
    field: Optional[str] = Field(default=None, alias="field")


class ServiceRegistryModel(BaseModel):
    registry_arn: Optional[str] = Field(default=None, alias="registryArn")
    port: Optional[int] = Field(default=None, alias="port")
    container_name: Optional[str] = Field(default=None, alias="containerName")
    container_port: Optional[int] = Field(default=None, alias="containerPort")


class ScaleModel(BaseModel):
    value: Optional[float] = Field(default=None, alias="value")
    unit: Optional[Literal["PERCENT"]] = Field(default=None, alias="unit")


class DeleteAccountSettingRequestModel(BaseModel):
    name: Literal[
        "awsvpcTrunking",
        "containerInsights",
        "containerInstanceLongArnFormat",
        "serviceLongArnFormat",
        "taskLongArnFormat",
    ] = Field(alias="name")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")


class SettingModel(BaseModel):
    name: Optional[
        Literal[
            "awsvpcTrunking",
            "containerInsights",
            "containerInstanceLongArnFormat",
            "serviceLongArnFormat",
            "taskLongArnFormat",
        ]
    ] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")


class DeleteCapacityProviderRequestModel(BaseModel):
    capacity_provider: str = Field(alias="capacityProvider")


class DeleteClusterRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")


class DeleteServiceRequestModel(BaseModel):
    service: str = Field(alias="service")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    force: Optional[bool] = Field(default=None, alias="force")


class DeleteTaskDefinitionsRequestModel(BaseModel):
    task_definitions: Sequence[str] = Field(alias="taskDefinitions")


class FailureModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    reason: Optional[str] = Field(default=None, alias="reason")
    detail: Optional[str] = Field(default=None, alias="detail")


class DeleteTaskSetRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    service: str = Field(alias="service")
    task_set: str = Field(alias="taskSet")
    force: Optional[bool] = Field(default=None, alias="force")


class DeploymentAlarmsModel(BaseModel):
    alarm_names: Sequence[str] = Field(alias="alarmNames")
    enable: bool = Field(alias="enable")
    rollback: bool = Field(alias="rollback")


class DeploymentCircuitBreakerModel(BaseModel):
    enable: bool = Field(alias="enable")
    rollback: bool = Field(alias="rollback")


class ServiceConnectServiceResourceModel(BaseModel):
    discovery_name: Optional[str] = Field(default=None, alias="discoveryName")
    discovery_arn: Optional[str] = Field(default=None, alias="discoveryArn")


class DeregisterContainerInstanceRequestModel(BaseModel):
    container_instance: str = Field(alias="containerInstance")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    force: Optional[bool] = Field(default=None, alias="force")


class DeregisterTaskDefinitionRequestModel(BaseModel):
    task_definition: str = Field(alias="taskDefinition")


class DescribeCapacityProvidersRequestModel(BaseModel):
    capacity_providers: Optional[Sequence[str]] = Field(
        default=None, alias="capacityProviders"
    )
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeClustersRequestModel(BaseModel):
    clusters: Optional[Sequence[str]] = Field(default=None, alias="clusters")
    include: Optional[
        Sequence[
            Literal["ATTACHMENTS", "CONFIGURATIONS", "SETTINGS", "STATISTICS", "TAGS"]
        ]
    ] = Field(default=None, alias="include")


class DescribeContainerInstancesRequestModel(BaseModel):
    container_instances: Sequence[str] = Field(alias="containerInstances")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["CONTAINER_INSTANCE_HEALTH", "TAGS"]]] = Field(
        default=None, alias="include"
    )


class DescribeServicesRequestModel(BaseModel):
    services: Sequence[str] = Field(alias="services")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeTaskDefinitionRequestModel(BaseModel):
    task_definition: str = Field(alias="taskDefinition")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")


class DescribeTaskSetsRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    service: str = Field(alias="service")
    task_sets: Optional[Sequence[str]] = Field(default=None, alias="taskSets")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")


class DescribeTasksRequestModel(BaseModel):
    tasks: Sequence[str] = Field(alias="tasks")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")


class DeviceModel(BaseModel):
    host_path: str = Field(alias="hostPath")
    container_path: Optional[str] = Field(default=None, alias="containerPath")
    permissions: Optional[List[Literal["mknod", "read", "write"]]] = Field(
        default=None, alias="permissions"
    )


class DiscoverPollEndpointRequestModel(BaseModel):
    container_instance: Optional[str] = Field(default=None, alias="containerInstance")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class DockerVolumeConfigurationModel(BaseModel):
    scope: Optional[Literal["shared", "task"]] = Field(default=None, alias="scope")
    autoprovision: Optional[bool] = Field(default=None, alias="autoprovision")
    driver: Optional[str] = Field(default=None, alias="driver")
    driver_opts: Optional[Dict[str, str]] = Field(default=None, alias="driverOpts")
    labels: Optional[Dict[str, str]] = Field(default=None, alias="labels")


class EFSAuthorizationConfigModel(BaseModel):
    access_point_id: Optional[str] = Field(default=None, alias="accessPointId")
    iam: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="iam")


class EphemeralStorageModel(BaseModel):
    size_in_gi_b: int = Field(alias="sizeInGiB")


class ExecuteCommandLogConfigurationModel(BaseModel):
    cloud_watch_log_group_name: Optional[str] = Field(
        default=None, alias="cloudWatchLogGroupName"
    )
    cloud_watch_encryption_enabled: Optional[bool] = Field(
        default=None, alias="cloudWatchEncryptionEnabled"
    )
    s3_bucket_name: Optional[str] = Field(default=None, alias="s3BucketName")
    s3_encryption_enabled: Optional[bool] = Field(
        default=None, alias="s3EncryptionEnabled"
    )
    s3_key_prefix: Optional[str] = Field(default=None, alias="s3KeyPrefix")


class ExecuteCommandRequestModel(BaseModel):
    command: str = Field(alias="command")
    interactive: bool = Field(alias="interactive")
    task: str = Field(alias="task")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    container: Optional[str] = Field(default=None, alias="container")


class SessionModel(BaseModel):
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    stream_url: Optional[str] = Field(default=None, alias="streamUrl")
    token_value: Optional[str] = Field(default=None, alias="tokenValue")


class FSxWindowsFileServerAuthorizationConfigModel(BaseModel):
    credentials_parameter: str = Field(alias="credentialsParameter")
    domain: str = Field(alias="domain")


class GetTaskProtectionRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    tasks: Optional[Sequence[str]] = Field(default=None, alias="tasks")


class ProtectedTaskModel(BaseModel):
    task_arn: Optional[str] = Field(default=None, alias="taskArn")
    protection_enabled: Optional[bool] = Field(default=None, alias="protectionEnabled")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")


class HostVolumePropertiesModel(BaseModel):
    source_path: Optional[str] = Field(default=None, alias="sourcePath")


class InferenceAcceleratorOverrideModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    device_type: Optional[str] = Field(default=None, alias="deviceType")


class InferenceAcceleratorModel(BaseModel):
    device_name: str = Field(alias="deviceName")
    device_type: str = Field(alias="deviceType")


class KernelCapabilitiesModel(BaseModel):
    add: Optional[List[str]] = Field(default=None, alias="add")
    drop: Optional[List[str]] = Field(default=None, alias="drop")


class TmpfsModel(BaseModel):
    container_path: str = Field(alias="containerPath")
    size: int = Field(alias="size")
    mount_options: Optional[List[str]] = Field(default=None, alias="mountOptions")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccountSettingsRequestModel(BaseModel):
    name: Optional[
        Literal[
            "awsvpcTrunking",
            "containerInsights",
            "containerInstanceLongArnFormat",
            "serviceLongArnFormat",
            "taskLongArnFormat",
        ]
    ] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")
    effective_settings: Optional[bool] = Field(default=None, alias="effectiveSettings")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAttributesRequestModel(BaseModel):
    target_type: Literal["container-instance"] = Field(alias="targetType")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    attribute_value: Optional[str] = Field(default=None, alias="attributeValue")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListClustersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListContainerInstancesRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    filter: Optional[str] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    status: Optional[
        Literal[
            "ACTIVE", "DEREGISTERING", "DRAINING", "REGISTERING", "REGISTRATION_FAILED"
        ]
    ] = Field(default=None, alias="status")


class ListServicesByNamespaceRequestModel(BaseModel):
    namespace: str = Field(alias="namespace")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListServicesRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    scheduling_strategy: Optional[Literal["DAEMON", "REPLICA"]] = Field(
        default=None, alias="schedulingStrategy"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTaskDefinitionFamiliesRequestModel(BaseModel):
    family_prefix: Optional[str] = Field(default=None, alias="familyPrefix")
    status: Optional[Literal["ACTIVE", "ALL", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTaskDefinitionsRequestModel(BaseModel):
    family_prefix: Optional[str] = Field(default=None, alias="familyPrefix")
    status: Optional[Literal["ACTIVE", "DELETE_IN_PROGRESS", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTasksRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    container_instance: Optional[str] = Field(default=None, alias="containerInstance")
    family: Optional[str] = Field(default=None, alias="family")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    desired_status: Optional[Literal["PENDING", "RUNNING", "STOPPED"]] = Field(
        default=None, alias="desiredStatus"
    )
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )


class ManagedAgentStateChangeModel(BaseModel):
    container_name: str = Field(alias="containerName")
    managed_agent_name: Literal["ExecuteCommandAgent"] = Field(alias="managedAgentName")
    status: str = Field(alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")


class PlatformDeviceModel(BaseModel):
    id: str = Field(alias="id")
    type: Literal["GPU"] = Field(alias="type")


class PutAccountSettingDefaultRequestModel(BaseModel):
    name: Literal[
        "awsvpcTrunking",
        "containerInsights",
        "containerInstanceLongArnFormat",
        "serviceLongArnFormat",
        "taskLongArnFormat",
    ] = Field(alias="name")
    value: str = Field(alias="value")


class PutAccountSettingRequestModel(BaseModel):
    name: Literal[
        "awsvpcTrunking",
        "containerInsights",
        "containerInstanceLongArnFormat",
        "serviceLongArnFormat",
        "taskLongArnFormat",
    ] = Field(alias="name")
    value: str = Field(alias="value")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")


class RuntimePlatformModel(BaseModel):
    cpu_architecture: Optional[Literal["ARM64", "X86_64"]] = Field(
        default=None, alias="cpuArchitecture"
    )
    operating_system_family: Optional[
        Literal[
            "LINUX",
            "WINDOWS_SERVER_2004_CORE",
            "WINDOWS_SERVER_2016_FULL",
            "WINDOWS_SERVER_2019_CORE",
            "WINDOWS_SERVER_2019_FULL",
            "WINDOWS_SERVER_2022_CORE",
            "WINDOWS_SERVER_2022_FULL",
            "WINDOWS_SERVER_20H2_CORE",
        ]
    ] = Field(default=None, alias="operatingSystemFamily")


class TaskDefinitionPlacementConstraintModel(BaseModel):
    type: Optional[Literal["memberOf"]] = Field(default=None, alias="type")
    expression: Optional[str] = Field(default=None, alias="expression")


class ServiceConnectClientAliasModel(BaseModel):
    port: int = Field(alias="port")
    dns_name: Optional[str] = Field(default=None, alias="dnsName")


class ServiceEventModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    message: Optional[str] = Field(default=None, alias="message")


class StopTaskRequestModel(BaseModel):
    task: str = Field(alias="task")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    reason: Optional[str] = Field(default=None, alias="reason")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateContainerAgentRequestModel(BaseModel):
    container_instance: str = Field(alias="containerInstance")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class UpdateContainerInstancesStateRequestModel(BaseModel):
    container_instances: Sequence[str] = Field(alias="containerInstances")
    status: Literal[
        "ACTIVE", "DEREGISTERING", "DRAINING", "REGISTERING", "REGISTRATION_FAILED"
    ] = Field(alias="status")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class UpdateServicePrimaryTaskSetRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    service: str = Field(alias="service")
    primary_task_set: str = Field(alias="primaryTaskSet")


class UpdateTaskProtectionRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    tasks: Sequence[str] = Field(alias="tasks")
    protection_enabled: bool = Field(alias="protectionEnabled")
    expires_in_minutes: Optional[int] = Field(default=None, alias="expiresInMinutes")


class SubmitAttachmentStateChangesRequestModel(BaseModel):
    attachments: Sequence[AttachmentStateChangeModel] = Field(alias="attachments")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class AttachmentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[str] = Field(default=None, alias="type")
    status: Optional[str] = Field(default=None, alias="status")
    details: Optional[List[KeyValuePairModel]] = Field(default=None, alias="details")


class ProxyConfigurationModel(BaseModel):
    container_name: str = Field(alias="containerName")
    type: Optional[Literal["APPMESH"]] = Field(default=None, alias="type")
    properties: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="properties"
    )


class DeleteAttributesRequestModel(BaseModel):
    attributes: Sequence[AttributeModel] = Field(alias="attributes")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class PutAttributesRequestModel(BaseModel):
    attributes: Sequence[AttributeModel] = Field(alias="attributes")
    cluster: Optional[str] = Field(default=None, alias="cluster")


class AutoScalingGroupProviderModel(BaseModel):
    auto_scaling_group_arn: str = Field(alias="autoScalingGroupArn")
    managed_scaling: Optional[ManagedScalingModel] = Field(
        default=None, alias="managedScaling"
    )
    managed_termination_protection: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="managedTerminationProtection"
    )


class AutoScalingGroupProviderUpdateModel(BaseModel):
    managed_scaling: Optional[ManagedScalingModel] = Field(
        default=None, alias="managedScaling"
    )
    managed_termination_protection: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="managedTerminationProtection"
    )


class NetworkConfigurationModel(BaseModel):
    awsvpc_configuration: Optional[AwsVpcConfigurationModel] = Field(
        default=None, alias="awsvpcConfiguration"
    )


class PutClusterCapacityProvidersRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    capacity_providers: Sequence[str] = Field(alias="capacityProviders")
    default_capacity_provider_strategy: Sequence[
        CapacityProviderStrategyItemModel
    ] = Field(alias="defaultCapacityProviderStrategy")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class UpdateClusterSettingsRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    settings: Sequence[ClusterSettingModel] = Field(alias="settings")


class ContainerOverrideModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    command: Optional[List[str]] = Field(default=None, alias="command")
    environment: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="environment"
    )
    environment_files: Optional[List[EnvironmentFileModel]] = Field(
        default=None, alias="environmentFiles"
    )
    cpu: Optional[int] = Field(default=None, alias="cpu")
    memory: Optional[int] = Field(default=None, alias="memory")
    memory_reservation: Optional[int] = Field(default=None, alias="memoryReservation")
    resource_requirements: Optional[List[ResourceRequirementModel]] = Field(
        default=None, alias="resourceRequirements"
    )


class LogConfigurationModel(BaseModel):
    log_driver: Literal[
        "awsfirelens",
        "awslogs",
        "fluentd",
        "gelf",
        "journald",
        "json-file",
        "splunk",
        "syslog",
    ] = Field(alias="logDriver")
    options: Optional[Mapping[str, str]] = Field(default=None, alias="options")
    secret_options: Optional[Sequence[SecretModel]] = Field(
        default=None, alias="secretOptions"
    )


class ContainerInstanceHealthStatusModel(BaseModel):
    overall_status: Optional[
        Literal["IMPAIRED", "INITIALIZING", "INSUFFICIENT_DATA", "OK"]
    ] = Field(default=None, alias="overallStatus")
    details: Optional[List[InstanceHealthCheckResultModel]] = Field(
        default=None, alias="details"
    )


class ContainerStateChangeModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="containerName")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    runtime_id: Optional[str] = Field(default=None, alias="runtimeId")
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    network_bindings: Optional[Sequence[NetworkBindingModel]] = Field(
        default=None, alias="networkBindings"
    )
    reason: Optional[str] = Field(default=None, alias="reason")
    status: Optional[str] = Field(default=None, alias="status")


class SubmitContainerStateChangeRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    task: Optional[str] = Field(default=None, alias="task")
    container_name: Optional[str] = Field(default=None, alias="containerName")
    runtime_id: Optional[str] = Field(default=None, alias="runtimeId")
    status: Optional[str] = Field(default=None, alias="status")
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")
    network_bindings: Optional[Sequence[NetworkBindingModel]] = Field(
        default=None, alias="networkBindings"
    )


class ContainerModel(BaseModel):
    container_arn: Optional[str] = Field(default=None, alias="containerArn")
    task_arn: Optional[str] = Field(default=None, alias="taskArn")
    name: Optional[str] = Field(default=None, alias="name")
    image: Optional[str] = Field(default=None, alias="image")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    runtime_id: Optional[str] = Field(default=None, alias="runtimeId")
    last_status: Optional[str] = Field(default=None, alias="lastStatus")
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")
    network_bindings: Optional[List[NetworkBindingModel]] = Field(
        default=None, alias="networkBindings"
    )
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    health_status: Optional[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        default=None, alias="healthStatus"
    )
    managed_agents: Optional[List[ManagedAgentModel]] = Field(
        default=None, alias="managedAgents"
    )
    cpu: Optional[str] = Field(default=None, alias="cpu")
    memory: Optional[str] = Field(default=None, alias="memory")
    memory_reservation: Optional[str] = Field(default=None, alias="memoryReservation")
    gpu_ids: Optional[List[str]] = Field(default=None, alias="gpuIds")


class DeleteAttributesResponseModel(BaseModel):
    attributes: List[AttributeModel] = Field(alias="attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DiscoverPollEndpointResponseModel(BaseModel):
    endpoint: str = Field(alias="endpoint")
    telemetry_endpoint: str = Field(alias="telemetryEndpoint")
    service_connect_endpoint: str = Field(alias="serviceConnectEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttributesResponseModel(BaseModel):
    attributes: List[AttributeModel] = Field(alias="attributes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersResponseModel(BaseModel):
    cluster_arns: List[str] = Field(alias="clusterArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContainerInstancesResponseModel(BaseModel):
    container_instance_arns: List[str] = Field(alias="containerInstanceArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesByNamespaceResponseModel(BaseModel):
    service_arns: List[str] = Field(alias="serviceArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesResponseModel(BaseModel):
    service_arns: List[str] = Field(alias="serviceArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTaskDefinitionFamiliesResponseModel(BaseModel):
    families: List[str] = Field(alias="families")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTaskDefinitionsResponseModel(BaseModel):
    task_definition_arns: List[str] = Field(alias="taskDefinitionArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTasksResponseModel(BaseModel):
    task_arns: List[str] = Field(alias="taskArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAttributesResponseModel(BaseModel):
    attributes: List[AttributeModel] = Field(alias="attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitAttachmentStateChangesResponseModel(BaseModel):
    acknowledgment: str = Field(alias="acknowledgment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitContainerStateChangeResponseModel(BaseModel):
    acknowledgment: str = Field(alias="acknowledgment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitTaskStateChangeResponseModel(BaseModel):
    acknowledgment: str = Field(alias="acknowledgment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTaskSetRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    service: str = Field(alias="service")
    task_set: str = Field(alias="taskSet")
    scale: ScaleModel = Field(alias="scale")


class DeleteAccountSettingResponseModel(BaseModel):
    setting: SettingModel = Field(alias="setting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountSettingsResponseModel(BaseModel):
    settings: List[SettingModel] = Field(alias="settings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccountSettingDefaultResponseModel(BaseModel):
    setting: SettingModel = Field(alias="setting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccountSettingResponseModel(BaseModel):
    setting: SettingModel = Field(alias="setting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentConfigurationModel(BaseModel):
    deployment_circuit_breaker: Optional[DeploymentCircuitBreakerModel] = Field(
        default=None, alias="deploymentCircuitBreaker"
    )
    maximum_percent: Optional[int] = Field(default=None, alias="maximumPercent")
    minimum_healthy_percent: Optional[int] = Field(
        default=None, alias="minimumHealthyPercent"
    )
    alarms: Optional[DeploymentAlarmsModel] = Field(default=None, alias="alarms")


class DescribeServicesRequestServicesInactiveWaitModel(BaseModel):
    services: Sequence[str] = Field(alias="services")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeServicesRequestServicesStableWaitModel(BaseModel):
    services: Sequence[str] = Field(alias="services")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTasksRequestTasksRunningWaitModel(BaseModel):
    tasks: Sequence[str] = Field(alias="tasks")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTasksRequestTasksStoppedWaitModel(BaseModel):
    tasks: Sequence[str] = Field(alias="tasks")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    include: Optional[Sequence[Literal["TAGS"]]] = Field(default=None, alias="include")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class EFSVolumeConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="fileSystemId")
    root_directory: Optional[str] = Field(default=None, alias="rootDirectory")
    transit_encryption: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="transitEncryption"
    )
    transit_encryption_port: Optional[int] = Field(
        default=None, alias="transitEncryptionPort"
    )
    authorization_config: Optional[EFSAuthorizationConfigModel] = Field(
        default=None, alias="authorizationConfig"
    )


class ExecuteCommandConfigurationModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    logging: Optional[Literal["DEFAULT", "NONE", "OVERRIDE"]] = Field(
        default=None, alias="logging"
    )
    log_configuration: Optional[ExecuteCommandLogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )


class ExecuteCommandResponseModel(BaseModel):
    cluster_arn: str = Field(alias="clusterArn")
    container_arn: str = Field(alias="containerArn")
    container_name: str = Field(alias="containerName")
    interactive: bool = Field(alias="interactive")
    session: SessionModel = Field(alias="session")
    task_arn: str = Field(alias="taskArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FSxWindowsFileServerVolumeConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="fileSystemId")
    root_directory: str = Field(alias="rootDirectory")
    authorization_config: FSxWindowsFileServerAuthorizationConfigModel = Field(
        alias="authorizationConfig"
    )


class GetTaskProtectionResponseModel(BaseModel):
    protected_tasks: List[ProtectedTaskModel] = Field(alias="protectedTasks")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTaskProtectionResponseModel(BaseModel):
    protected_tasks: List[ProtectedTaskModel] = Field(alias="protectedTasks")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LinuxParametersModel(BaseModel):
    capabilities: Optional[KernelCapabilitiesModel] = Field(
        default=None, alias="capabilities"
    )
    devices: Optional[List[DeviceModel]] = Field(default=None, alias="devices")
    init_process_enabled: Optional[bool] = Field(
        default=None, alias="initProcessEnabled"
    )
    shared_memory_size: Optional[int] = Field(default=None, alias="sharedMemorySize")
    tmpfs: Optional[List[TmpfsModel]] = Field(default=None, alias="tmpfs")
    max_swap: Optional[int] = Field(default=None, alias="maxSwap")
    swappiness: Optional[int] = Field(default=None, alias="swappiness")


class ListAccountSettingsRequestListAccountSettingsPaginateModel(BaseModel):
    name: Optional[
        Literal[
            "awsvpcTrunking",
            "containerInsights",
            "containerInstanceLongArnFormat",
            "serviceLongArnFormat",
            "taskLongArnFormat",
        ]
    ] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")
    effective_settings: Optional[bool] = Field(default=None, alias="effectiveSettings")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttributesRequestListAttributesPaginateModel(BaseModel):
    target_type: Literal["container-instance"] = Field(alias="targetType")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    attribute_value: Optional[str] = Field(default=None, alias="attributeValue")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersRequestListClustersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContainerInstancesRequestListContainerInstancesPaginateModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    filter: Optional[str] = Field(default=None, alias="filter")
    status: Optional[
        Literal[
            "ACTIVE", "DEREGISTERING", "DRAINING", "REGISTERING", "REGISTRATION_FAILED"
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesByNamespaceRequestListServicesByNamespacePaginateModel(BaseModel):
    namespace: str = Field(alias="namespace")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesRequestListServicesPaginateModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    scheduling_strategy: Optional[Literal["DAEMON", "REPLICA"]] = Field(
        default=None, alias="schedulingStrategy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateModel(
    BaseModel
):
    family_prefix: Optional[str] = Field(default=None, alias="familyPrefix")
    status: Optional[Literal["ACTIVE", "ALL", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTaskDefinitionsRequestListTaskDefinitionsPaginateModel(BaseModel):
    family_prefix: Optional[str] = Field(default=None, alias="familyPrefix")
    status: Optional[Literal["ACTIVE", "DELETE_IN_PROGRESS", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTasksRequestListTasksPaginateModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    container_instance: Optional[str] = Field(default=None, alias="containerInstance")
    family: Optional[str] = Field(default=None, alias="family")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    desired_status: Optional[Literal["PENDING", "RUNNING", "STOPPED"]] = Field(
        default=None, alias="desiredStatus"
    )
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RegisterContainerInstanceRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    instance_identity_document: Optional[str] = Field(
        default=None, alias="instanceIdentityDocument"
    )
    instance_identity_document_signature: Optional[str] = Field(
        default=None, alias="instanceIdentityDocumentSignature"
    )
    total_resources: Optional[Sequence[ResourceModel]] = Field(
        default=None, alias="totalResources"
    )
    version_info: Optional[VersionInfoModel] = Field(default=None, alias="versionInfo")
    container_instance_arn: Optional[str] = Field(
        default=None, alias="containerInstanceArn"
    )
    attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="attributes"
    )
    platform_devices: Optional[Sequence[PlatformDeviceModel]] = Field(
        default=None, alias="platformDevices"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ServiceConnectServiceModel(BaseModel):
    port_name: str = Field(alias="portName")
    discovery_name: Optional[str] = Field(default=None, alias="discoveryName")
    client_aliases: Optional[Sequence[ServiceConnectClientAliasModel]] = Field(
        default=None, alias="clientAliases"
    )
    ingress_port_override: Optional[int] = Field(
        default=None, alias="ingressPortOverride"
    )


class CapacityProviderModel(BaseModel):
    capacity_provider_arn: Optional[str] = Field(
        default=None, alias="capacityProviderArn"
    )
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    auto_scaling_group_provider: Optional[AutoScalingGroupProviderModel] = Field(
        default=None, alias="autoScalingGroupProvider"
    )
    update_status: Optional[
        Literal[
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="updateStatus")
    update_status_reason: Optional[str] = Field(
        default=None, alias="updateStatusReason"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class CreateCapacityProviderRequestModel(BaseModel):
    name: str = Field(alias="name")
    auto_scaling_group_provider: AutoScalingGroupProviderModel = Field(
        alias="autoScalingGroupProvider"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateCapacityProviderRequestModel(BaseModel):
    name: str = Field(alias="name")
    auto_scaling_group_provider: AutoScalingGroupProviderUpdateModel = Field(
        alias="autoScalingGroupProvider"
    )


class CreateTaskSetRequestModel(BaseModel):
    service: str = Field(alias="service")
    cluster: str = Field(alias="cluster")
    task_definition: str = Field(alias="taskDefinition")
    external_id: Optional[str] = Field(default=None, alias="externalId")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    load_balancers: Optional[Sequence[LoadBalancerModel]] = Field(
        default=None, alias="loadBalancers"
    )
    service_registries: Optional[Sequence[ServiceRegistryModel]] = Field(
        default=None, alias="serviceRegistries"
    )
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    scale: Optional[ScaleModel] = Field(default=None, alias="scale")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TaskSetModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    task_set_arn: Optional[str] = Field(default=None, alias="taskSetArn")
    service_arn: Optional[str] = Field(default=None, alias="serviceArn")
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    external_id: Optional[str] = Field(default=None, alias="externalId")
    status: Optional[str] = Field(default=None, alias="status")
    task_definition: Optional[str] = Field(default=None, alias="taskDefinition")
    computed_desired_count: Optional[int] = Field(
        default=None, alias="computedDesiredCount"
    )
    pending_count: Optional[int] = Field(default=None, alias="pendingCount")
    running_count: Optional[int] = Field(default=None, alias="runningCount")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    capacity_provider_strategy: Optional[
        List[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    platform_family: Optional[str] = Field(default=None, alias="platformFamily")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    load_balancers: Optional[List[LoadBalancerModel]] = Field(
        default=None, alias="loadBalancers"
    )
    service_registries: Optional[List[ServiceRegistryModel]] = Field(
        default=None, alias="serviceRegistries"
    )
    scale: Optional[ScaleModel] = Field(default=None, alias="scale")
    stability_status: Optional[Literal["STABILIZING", "STEADY_STATE"]] = Field(
        default=None, alias="stabilityStatus"
    )
    stability_status_at: Optional[datetime] = Field(
        default=None, alias="stabilityStatusAt"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class TaskOverrideModel(BaseModel):
    container_overrides: Optional[List[ContainerOverrideModel]] = Field(
        default=None, alias="containerOverrides"
    )
    cpu: Optional[str] = Field(default=None, alias="cpu")
    inference_accelerator_overrides: Optional[
        List[InferenceAcceleratorOverrideModel]
    ] = Field(default=None, alias="inferenceAcceleratorOverrides")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    memory: Optional[str] = Field(default=None, alias="memory")
    task_role_arn: Optional[str] = Field(default=None, alias="taskRoleArn")
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="ephemeralStorage"
    )


class ContainerInstanceModel(BaseModel):
    container_instance_arn: Optional[str] = Field(
        default=None, alias="containerInstanceArn"
    )
    ec2_instance_id: Optional[str] = Field(default=None, alias="ec2InstanceId")
    capacity_provider_name: Optional[str] = Field(
        default=None, alias="capacityProviderName"
    )
    version: Optional[int] = Field(default=None, alias="version")
    version_info: Optional[VersionInfoModel] = Field(default=None, alias="versionInfo")
    remaining_resources: Optional[List[ResourceModel]] = Field(
        default=None, alias="remainingResources"
    )
    registered_resources: Optional[List[ResourceModel]] = Field(
        default=None, alias="registeredResources"
    )
    status: Optional[str] = Field(default=None, alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    agent_connected: Optional[bool] = Field(default=None, alias="agentConnected")
    running_tasks_count: Optional[int] = Field(default=None, alias="runningTasksCount")
    pending_tasks_count: Optional[int] = Field(default=None, alias="pendingTasksCount")
    agent_update_status: Optional[
        Literal["FAILED", "PENDING", "STAGED", "STAGING", "UPDATED", "UPDATING"]
    ] = Field(default=None, alias="agentUpdateStatus")
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="attributes")
    registered_at: Optional[datetime] = Field(default=None, alias="registeredAt")
    attachments: Optional[List[AttachmentModel]] = Field(
        default=None, alias="attachments"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    health_status: Optional[ContainerInstanceHealthStatusModel] = Field(
        default=None, alias="healthStatus"
    )


class SubmitTaskStateChangeRequestModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    task: Optional[str] = Field(default=None, alias="task")
    status: Optional[str] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")
    containers: Optional[Sequence[ContainerStateChangeModel]] = Field(
        default=None, alias="containers"
    )
    attachments: Optional[Sequence[AttachmentStateChangeModel]] = Field(
        default=None, alias="attachments"
    )
    managed_agents: Optional[Sequence[ManagedAgentStateChangeModel]] = Field(
        default=None, alias="managedAgents"
    )
    pull_started_at: Optional[Union[datetime, str]] = Field(
        default=None, alias="pullStartedAt"
    )
    pull_stopped_at: Optional[Union[datetime, str]] = Field(
        default=None, alias="pullStoppedAt"
    )
    execution_stopped_at: Optional[Union[datetime, str]] = Field(
        default=None, alias="executionStoppedAt"
    )


class ClusterConfigurationModel(BaseModel):
    execute_command_configuration: Optional[ExecuteCommandConfigurationModel] = Field(
        default=None, alias="executeCommandConfiguration"
    )


class VolumeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    host: Optional[HostVolumePropertiesModel] = Field(default=None, alias="host")
    docker_volume_configuration: Optional[DockerVolumeConfigurationModel] = Field(
        default=None, alias="dockerVolumeConfiguration"
    )
    efs_volume_configuration: Optional[EFSVolumeConfigurationModel] = Field(
        default=None, alias="efsVolumeConfiguration"
    )
    fsx_windows_file_server_volume_configuration: Optional[
        FSxWindowsFileServerVolumeConfigurationModel
    ] = Field(default=None, alias="fsxWindowsFileServerVolumeConfiguration")


class ContainerDefinitionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    image: Optional[str] = Field(default=None, alias="image")
    repository_credentials: Optional[RepositoryCredentialsModel] = Field(
        default=None, alias="repositoryCredentials"
    )
    cpu: Optional[int] = Field(default=None, alias="cpu")
    memory: Optional[int] = Field(default=None, alias="memory")
    memory_reservation: Optional[int] = Field(default=None, alias="memoryReservation")
    links: Optional[List[str]] = Field(default=None, alias="links")
    port_mappings: Optional[List[PortMappingModel]] = Field(
        default=None, alias="portMappings"
    )
    essential: Optional[bool] = Field(default=None, alias="essential")
    entry_point: Optional[List[str]] = Field(default=None, alias="entryPoint")
    command: Optional[List[str]] = Field(default=None, alias="command")
    environment: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="environment"
    )
    environment_files: Optional[List[EnvironmentFileModel]] = Field(
        default=None, alias="environmentFiles"
    )
    mount_points: Optional[List[MountPointModel]] = Field(
        default=None, alias="mountPoints"
    )
    volumes_from: Optional[List[VolumeFromModel]] = Field(
        default=None, alias="volumesFrom"
    )
    linux_parameters: Optional[LinuxParametersModel] = Field(
        default=None, alias="linuxParameters"
    )
    secrets: Optional[List[SecretModel]] = Field(default=None, alias="secrets")
    depends_on: Optional[List[ContainerDependencyModel]] = Field(
        default=None, alias="dependsOn"
    )
    start_timeout: Optional[int] = Field(default=None, alias="startTimeout")
    stop_timeout: Optional[int] = Field(default=None, alias="stopTimeout")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    user: Optional[str] = Field(default=None, alias="user")
    working_directory: Optional[str] = Field(default=None, alias="workingDirectory")
    disable_networking: Optional[bool] = Field(default=None, alias="disableNetworking")
    privileged: Optional[bool] = Field(default=None, alias="privileged")
    readonly_root_filesystem: Optional[bool] = Field(
        default=None, alias="readonlyRootFilesystem"
    )
    dns_servers: Optional[List[str]] = Field(default=None, alias="dnsServers")
    dns_search_domains: Optional[List[str]] = Field(
        default=None, alias="dnsSearchDomains"
    )
    extra_hosts: Optional[List[HostEntryModel]] = Field(
        default=None, alias="extraHosts"
    )
    docker_security_options: Optional[List[str]] = Field(
        default=None, alias="dockerSecurityOptions"
    )
    interactive: Optional[bool] = Field(default=None, alias="interactive")
    pseudo_terminal: Optional[bool] = Field(default=None, alias="pseudoTerminal")
    docker_labels: Optional[Dict[str, str]] = Field(default=None, alias="dockerLabels")
    ulimits: Optional[List[UlimitModel]] = Field(default=None, alias="ulimits")
    log_configuration: Optional[LogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )
    health_check: Optional[HealthCheckModel] = Field(default=None, alias="healthCheck")
    system_controls: Optional[List[SystemControlModel]] = Field(
        default=None, alias="systemControls"
    )
    resource_requirements: Optional[List[ResourceRequirementModel]] = Field(
        default=None, alias="resourceRequirements"
    )
    firelens_configuration: Optional[FirelensConfigurationModel] = Field(
        default=None, alias="firelensConfiguration"
    )


class ServiceConnectConfigurationModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    services: Optional[Sequence[ServiceConnectServiceModel]] = Field(
        default=None, alias="services"
    )
    log_configuration: Optional[LogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )


class CreateCapacityProviderResponseModel(BaseModel):
    capacity_provider: CapacityProviderModel = Field(alias="capacityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCapacityProviderResponseModel(BaseModel):
    capacity_provider: CapacityProviderModel = Field(alias="capacityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCapacityProvidersResponseModel(BaseModel):
    capacity_providers: List[CapacityProviderModel] = Field(alias="capacityProviders")
    failures: List[FailureModel] = Field(alias="failures")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCapacityProviderResponseModel(BaseModel):
    capacity_provider: CapacityProviderModel = Field(alias="capacityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskSetResponseModel(BaseModel):
    task_set: TaskSetModel = Field(alias="taskSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTaskSetResponseModel(BaseModel):
    task_set: TaskSetModel = Field(alias="taskSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTaskSetsResponseModel(BaseModel):
    task_sets: List[TaskSetModel] = Field(alias="taskSets")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServicePrimaryTaskSetResponseModel(BaseModel):
    task_set: TaskSetModel = Field(alias="taskSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTaskSetResponseModel(BaseModel):
    task_set: TaskSetModel = Field(alias="taskSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunTaskRequestModel(BaseModel):
    task_definition: str = Field(alias="taskDefinition")
    capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    count: Optional[int] = Field(default=None, alias="count")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="enableECSManagedTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )
    group: Optional[str] = Field(default=None, alias="group")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    overrides: Optional[TaskOverrideModel] = Field(default=None, alias="overrides")
    placement_constraints: Optional[Sequence[PlacementConstraintModel]] = Field(
        default=None, alias="placementConstraints"
    )
    placement_strategy: Optional[Sequence[PlacementStrategyModel]] = Field(
        default=None, alias="placementStrategy"
    )
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    propagate_tags: Optional[Literal["NONE", "SERVICE", "TASK_DEFINITION"]] = Field(
        default=None, alias="propagateTags"
    )
    reference_id: Optional[str] = Field(default=None, alias="referenceId")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class StartTaskRequestModel(BaseModel):
    container_instances: Sequence[str] = Field(alias="containerInstances")
    task_definition: str = Field(alias="taskDefinition")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="enableECSManagedTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )
    group: Optional[str] = Field(default=None, alias="group")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    overrides: Optional[TaskOverrideModel] = Field(default=None, alias="overrides")
    propagate_tags: Optional[Literal["NONE", "SERVICE", "TASK_DEFINITION"]] = Field(
        default=None, alias="propagateTags"
    )
    reference_id: Optional[str] = Field(default=None, alias="referenceId")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TaskModel(BaseModel):
    attachments: Optional[List[AttachmentModel]] = Field(
        default=None, alias="attachments"
    )
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="attributes")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    capacity_provider_name: Optional[str] = Field(
        default=None, alias="capacityProviderName"
    )
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    connectivity: Optional[Literal["CONNECTED", "DISCONNECTED"]] = Field(
        default=None, alias="connectivity"
    )
    connectivity_at: Optional[datetime] = Field(default=None, alias="connectivityAt")
    container_instance_arn: Optional[str] = Field(
        default=None, alias="containerInstanceArn"
    )
    containers: Optional[List[ContainerModel]] = Field(default=None, alias="containers")
    cpu: Optional[str] = Field(default=None, alias="cpu")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    desired_status: Optional[str] = Field(default=None, alias="desiredStatus")
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )
    execution_stopped_at: Optional[datetime] = Field(
        default=None, alias="executionStoppedAt"
    )
    group: Optional[str] = Field(default=None, alias="group")
    health_status: Optional[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        default=None, alias="healthStatus"
    )
    inference_accelerators: Optional[List[InferenceAcceleratorModel]] = Field(
        default=None, alias="inferenceAccelerators"
    )
    last_status: Optional[str] = Field(default=None, alias="lastStatus")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    memory: Optional[str] = Field(default=None, alias="memory")
    overrides: Optional[TaskOverrideModel] = Field(default=None, alias="overrides")
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    platform_family: Optional[str] = Field(default=None, alias="platformFamily")
    pull_started_at: Optional[datetime] = Field(default=None, alias="pullStartedAt")
    pull_stopped_at: Optional[datetime] = Field(default=None, alias="pullStoppedAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    stop_code: Optional[
        Literal[
            "EssentialContainerExited",
            "ServiceSchedulerInitiated",
            "SpotInterruption",
            "TaskFailedToStart",
            "TerminationNotice",
            "UserInitiated",
        ]
    ] = Field(default=None, alias="stopCode")
    stopped_at: Optional[datetime] = Field(default=None, alias="stoppedAt")
    stopped_reason: Optional[str] = Field(default=None, alias="stoppedReason")
    stopping_at: Optional[datetime] = Field(default=None, alias="stoppingAt")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    task_arn: Optional[str] = Field(default=None, alias="taskArn")
    task_definition_arn: Optional[str] = Field(default=None, alias="taskDefinitionArn")
    version: Optional[int] = Field(default=None, alias="version")
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="ephemeralStorage"
    )


class DeregisterContainerInstanceResponseModel(BaseModel):
    container_instance: ContainerInstanceModel = Field(alias="containerInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContainerInstancesResponseModel(BaseModel):
    container_instances: List[ContainerInstanceModel] = Field(
        alias="containerInstances"
    )
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterContainerInstanceResponseModel(BaseModel):
    container_instance: ContainerInstanceModel = Field(alias="containerInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContainerAgentResponseModel(BaseModel):
    container_instance: ContainerInstanceModel = Field(alias="containerInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContainerInstancesStateResponseModel(BaseModel):
    container_instances: List[ContainerInstanceModel] = Field(
        alias="containerInstances"
    )
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    configuration: Optional[ClusterConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    status: Optional[str] = Field(default=None, alias="status")
    registered_container_instances_count: Optional[int] = Field(
        default=None, alias="registeredContainerInstancesCount"
    )
    running_tasks_count: Optional[int] = Field(default=None, alias="runningTasksCount")
    pending_tasks_count: Optional[int] = Field(default=None, alias="pendingTasksCount")
    active_services_count: Optional[int] = Field(
        default=None, alias="activeServicesCount"
    )
    statistics: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="statistics"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    settings: Optional[List[ClusterSettingModel]] = Field(
        default=None, alias="settings"
    )
    capacity_providers: Optional[List[str]] = Field(
        default=None, alias="capacityProviders"
    )
    default_capacity_provider_strategy: Optional[
        List[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="defaultCapacityProviderStrategy")
    attachments: Optional[List[AttachmentModel]] = Field(
        default=None, alias="attachments"
    )
    attachments_status: Optional[str] = Field(default=None, alias="attachmentsStatus")
    service_connect_defaults: Optional[ClusterServiceConnectDefaultsModel] = Field(
        default=None, alias="serviceConnectDefaults"
    )


class CreateClusterRequestModel(BaseModel):
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    settings: Optional[Sequence[ClusterSettingModel]] = Field(
        default=None, alias="settings"
    )
    configuration: Optional[ClusterConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    capacity_providers: Optional[Sequence[str]] = Field(
        default=None, alias="capacityProviders"
    )
    default_capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="defaultCapacityProviderStrategy")
    service_connect_defaults: Optional[
        ClusterServiceConnectDefaultsRequestModel
    ] = Field(default=None, alias="serviceConnectDefaults")


class UpdateClusterRequestModel(BaseModel):
    cluster: str = Field(alias="cluster")
    settings: Optional[Sequence[ClusterSettingModel]] = Field(
        default=None, alias="settings"
    )
    configuration: Optional[ClusterConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    service_connect_defaults: Optional[
        ClusterServiceConnectDefaultsRequestModel
    ] = Field(default=None, alias="serviceConnectDefaults")


class RegisterTaskDefinitionRequestModel(BaseModel):
    family: str = Field(alias="family")
    container_definitions: Sequence[ContainerDefinitionModel] = Field(
        alias="containerDefinitions"
    )
    task_role_arn: Optional[str] = Field(default=None, alias="taskRoleArn")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    network_mode: Optional[Literal["awsvpc", "bridge", "host", "none"]] = Field(
        default=None, alias="networkMode"
    )
    volumes: Optional[Sequence[VolumeModel]] = Field(default=None, alias="volumes")
    placement_constraints: Optional[
        Sequence[TaskDefinitionPlacementConstraintModel]
    ] = Field(default=None, alias="placementConstraints")
    requires_compatibilities: Optional[
        Sequence[Literal["EC2", "EXTERNAL", "FARGATE"]]
    ] = Field(default=None, alias="requiresCompatibilities")
    cpu: Optional[str] = Field(default=None, alias="cpu")
    memory: Optional[str] = Field(default=None, alias="memory")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    pid_mode: Optional[Literal["host", "task"]] = Field(default=None, alias="pidMode")
    ipc_mode: Optional[Literal["host", "none", "task"]] = Field(
        default=None, alias="ipcMode"
    )
    proxy_configuration: Optional[ProxyConfigurationModel] = Field(
        default=None, alias="proxyConfiguration"
    )
    inference_accelerators: Optional[Sequence[InferenceAcceleratorModel]] = Field(
        default=None, alias="inferenceAccelerators"
    )
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="ephemeralStorage"
    )
    runtime_platform: Optional[RuntimePlatformModel] = Field(
        default=None, alias="runtimePlatform"
    )


class TaskDefinitionModel(BaseModel):
    task_definition_arn: Optional[str] = Field(default=None, alias="taskDefinitionArn")
    container_definitions: Optional[List[ContainerDefinitionModel]] = Field(
        default=None, alias="containerDefinitions"
    )
    family: Optional[str] = Field(default=None, alias="family")
    task_role_arn: Optional[str] = Field(default=None, alias="taskRoleArn")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    network_mode: Optional[Literal["awsvpc", "bridge", "host", "none"]] = Field(
        default=None, alias="networkMode"
    )
    revision: Optional[int] = Field(default=None, alias="revision")
    volumes: Optional[List[VolumeModel]] = Field(default=None, alias="volumes")
    status: Optional[Literal["ACTIVE", "DELETE_IN_PROGRESS", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    requires_attributes: Optional[List[AttributeModel]] = Field(
        default=None, alias="requiresAttributes"
    )
    placement_constraints: Optional[
        List[TaskDefinitionPlacementConstraintModel]
    ] = Field(default=None, alias="placementConstraints")
    compatibilities: Optional[List[Literal["EC2", "EXTERNAL", "FARGATE"]]] = Field(
        default=None, alias="compatibilities"
    )
    runtime_platform: Optional[RuntimePlatformModel] = Field(
        default=None, alias="runtimePlatform"
    )
    requires_compatibilities: Optional[
        List[Literal["EC2", "EXTERNAL", "FARGATE"]]
    ] = Field(default=None, alias="requiresCompatibilities")
    cpu: Optional[str] = Field(default=None, alias="cpu")
    memory: Optional[str] = Field(default=None, alias="memory")
    inference_accelerators: Optional[List[InferenceAcceleratorModel]] = Field(
        default=None, alias="inferenceAccelerators"
    )
    pid_mode: Optional[Literal["host", "task"]] = Field(default=None, alias="pidMode")
    ipc_mode: Optional[Literal["host", "none", "task"]] = Field(
        default=None, alias="ipcMode"
    )
    proxy_configuration: Optional[ProxyConfigurationModel] = Field(
        default=None, alias="proxyConfiguration"
    )
    registered_at: Optional[datetime] = Field(default=None, alias="registeredAt")
    deregistered_at: Optional[datetime] = Field(default=None, alias="deregisteredAt")
    registered_by: Optional[str] = Field(default=None, alias="registeredBy")
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="ephemeralStorage"
    )


class CreateServiceRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    task_definition: Optional[str] = Field(default=None, alias="taskDefinition")
    load_balancers: Optional[Sequence[LoadBalancerModel]] = Field(
        default=None, alias="loadBalancers"
    )
    service_registries: Optional[Sequence[ServiceRegistryModel]] = Field(
        default=None, alias="serviceRegistries"
    )
    desired_count: Optional[int] = Field(default=None, alias="desiredCount")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    role: Optional[str] = Field(default=None, alias="role")
    deployment_configuration: Optional[DeploymentConfigurationModel] = Field(
        default=None, alias="deploymentConfiguration"
    )
    placement_constraints: Optional[Sequence[PlacementConstraintModel]] = Field(
        default=None, alias="placementConstraints"
    )
    placement_strategy: Optional[Sequence[PlacementStrategyModel]] = Field(
        default=None, alias="placementStrategy"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    health_check_grace_period_seconds: Optional[int] = Field(
        default=None, alias="healthCheckGracePeriodSeconds"
    )
    scheduling_strategy: Optional[Literal["DAEMON", "REPLICA"]] = Field(
        default=None, alias="schedulingStrategy"
    )
    deployment_controller: Optional[DeploymentControllerModel] = Field(
        default=None, alias="deploymentController"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="enableECSManagedTags"
    )
    propagate_tags: Optional[Literal["NONE", "SERVICE", "TASK_DEFINITION"]] = Field(
        default=None, alias="propagateTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )
    service_connect_configuration: Optional[ServiceConnectConfigurationModel] = Field(
        default=None, alias="serviceConnectConfiguration"
    )


class DeploymentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    status: Optional[str] = Field(default=None, alias="status")
    task_definition: Optional[str] = Field(default=None, alias="taskDefinition")
    desired_count: Optional[int] = Field(default=None, alias="desiredCount")
    pending_count: Optional[int] = Field(default=None, alias="pendingCount")
    running_count: Optional[int] = Field(default=None, alias="runningCount")
    failed_tasks: Optional[int] = Field(default=None, alias="failedTasks")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    capacity_provider_strategy: Optional[
        List[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    platform_family: Optional[str] = Field(default=None, alias="platformFamily")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    rollout_state: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="rolloutState"
    )
    rollout_state_reason: Optional[str] = Field(
        default=None, alias="rolloutStateReason"
    )
    service_connect_configuration: Optional[ServiceConnectConfigurationModel] = Field(
        default=None, alias="serviceConnectConfiguration"
    )
    service_connect_resources: Optional[
        List[ServiceConnectServiceResourceModel]
    ] = Field(default=None, alias="serviceConnectResources")


class UpdateServiceRequestModel(BaseModel):
    service: str = Field(alias="service")
    cluster: Optional[str] = Field(default=None, alias="cluster")
    desired_count: Optional[int] = Field(default=None, alias="desiredCount")
    task_definition: Optional[str] = Field(default=None, alias="taskDefinition")
    capacity_provider_strategy: Optional[
        Sequence[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    deployment_configuration: Optional[DeploymentConfigurationModel] = Field(
        default=None, alias="deploymentConfiguration"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    placement_constraints: Optional[Sequence[PlacementConstraintModel]] = Field(
        default=None, alias="placementConstraints"
    )
    placement_strategy: Optional[Sequence[PlacementStrategyModel]] = Field(
        default=None, alias="placementStrategy"
    )
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    force_new_deployment: Optional[bool] = Field(
        default=None, alias="forceNewDeployment"
    )
    health_check_grace_period_seconds: Optional[int] = Field(
        default=None, alias="healthCheckGracePeriodSeconds"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="enableECSManagedTags"
    )
    load_balancers: Optional[Sequence[LoadBalancerModel]] = Field(
        default=None, alias="loadBalancers"
    )
    propagate_tags: Optional[Literal["NONE", "SERVICE", "TASK_DEFINITION"]] = Field(
        default=None, alias="propagateTags"
    )
    service_registries: Optional[Sequence[ServiceRegistryModel]] = Field(
        default=None, alias="serviceRegistries"
    )
    service_connect_configuration: Optional[ServiceConnectConfigurationModel] = Field(
        default=None, alias="serviceConnectConfiguration"
    )


class DescribeTasksResponseModel(BaseModel):
    tasks: List[TaskModel] = Field(alias="tasks")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunTaskResponseModel(BaseModel):
    tasks: List[TaskModel] = Field(alias="tasks")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTaskResponseModel(BaseModel):
    tasks: List[TaskModel] = Field(alias="tasks")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopTaskResponseModel(BaseModel):
    task: TaskModel = Field(alias="task")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClustersResponseModel(BaseModel):
    clusters: List[ClusterModel] = Field(alias="clusters")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutClusterCapacityProvidersResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterSettingsResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTaskDefinitionsResponseModel(BaseModel):
    task_definitions: List[TaskDefinitionModel] = Field(alias="taskDefinitions")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterTaskDefinitionResponseModel(BaseModel):
    task_definition: TaskDefinitionModel = Field(alias="taskDefinition")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTaskDefinitionResponseModel(BaseModel):
    task_definition: TaskDefinitionModel = Field(alias="taskDefinition")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterTaskDefinitionResponseModel(BaseModel):
    task_definition: TaskDefinitionModel = Field(alias="taskDefinition")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServiceModel(BaseModel):
    service_arn: Optional[str] = Field(default=None, alias="serviceArn")
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    cluster_arn: Optional[str] = Field(default=None, alias="clusterArn")
    load_balancers: Optional[List[LoadBalancerModel]] = Field(
        default=None, alias="loadBalancers"
    )
    service_registries: Optional[List[ServiceRegistryModel]] = Field(
        default=None, alias="serviceRegistries"
    )
    status: Optional[str] = Field(default=None, alias="status")
    desired_count: Optional[int] = Field(default=None, alias="desiredCount")
    running_count: Optional[int] = Field(default=None, alias="runningCount")
    pending_count: Optional[int] = Field(default=None, alias="pendingCount")
    launch_type: Optional[Literal["EC2", "EXTERNAL", "FARGATE"]] = Field(
        default=None, alias="launchType"
    )
    capacity_provider_strategy: Optional[
        List[CapacityProviderStrategyItemModel]
    ] = Field(default=None, alias="capacityProviderStrategy")
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    platform_family: Optional[str] = Field(default=None, alias="platformFamily")
    task_definition: Optional[str] = Field(default=None, alias="taskDefinition")
    deployment_configuration: Optional[DeploymentConfigurationModel] = Field(
        default=None, alias="deploymentConfiguration"
    )
    task_sets: Optional[List[TaskSetModel]] = Field(default=None, alias="taskSets")
    deployments: Optional[List[DeploymentModel]] = Field(
        default=None, alias="deployments"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    events: Optional[List[ServiceEventModel]] = Field(default=None, alias="events")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    placement_constraints: Optional[List[PlacementConstraintModel]] = Field(
        default=None, alias="placementConstraints"
    )
    placement_strategy: Optional[List[PlacementStrategyModel]] = Field(
        default=None, alias="placementStrategy"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    health_check_grace_period_seconds: Optional[int] = Field(
        default=None, alias="healthCheckGracePeriodSeconds"
    )
    scheduling_strategy: Optional[Literal["DAEMON", "REPLICA"]] = Field(
        default=None, alias="schedulingStrategy"
    )
    deployment_controller: Optional[DeploymentControllerModel] = Field(
        default=None, alias="deploymentController"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="enableECSManagedTags"
    )
    propagate_tags: Optional[Literal["NONE", "SERVICE", "TASK_DEFINITION"]] = Field(
        default=None, alias="propagateTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="enableExecuteCommand"
    )


class CreateServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServicesResponseModel(BaseModel):
    services: List[ServiceModel] = Field(alias="services")
    failures: List[FailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
