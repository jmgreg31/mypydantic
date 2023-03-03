# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class StackConfigurationManagerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class DataSourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    arn: Optional[str] = Field(default=None, alias="Arn")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")


class EnvironmentVariableModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")
    secure: Optional[bool] = Field(default=None, alias="Secure")


class SourceModel(BaseModel):
    type: Optional[Literal["archive", "git", "s3", "svn"]] = Field(
        default=None, alias="Type"
    )
    url: Optional[str] = Field(default=None, alias="Url")
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    ssh_key: Optional[str] = Field(default=None, alias="SshKey")
    revision: Optional[str] = Field(default=None, alias="Revision")


class SslConfigurationModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    private_key: str = Field(alias="PrivateKey")
    chain: Optional[str] = Field(default=None, alias="Chain")


class AssignInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    layer_ids: Sequence[str] = Field(alias="LayerIds")


class AssignVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class AssociateElasticIpRequestModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class AttachElasticLoadBalancerRequestModel(BaseModel):
    elastic_load_balancer_name: str = Field(alias="ElasticLoadBalancerName")
    layer_id: str = Field(alias="LayerId")


class AutoScalingThresholdsModel(BaseModel):
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    thresholds_wait_time: Optional[int] = Field(
        default=None, alias="ThresholdsWaitTime"
    )
    ignore_metrics_time: Optional[int] = Field(default=None, alias="IgnoreMetricsTime")
    cpu_threshold: Optional[float] = Field(default=None, alias="CpuThreshold")
    memory_threshold: Optional[float] = Field(default=None, alias="MemoryThreshold")
    load_threshold: Optional[float] = Field(default=None, alias="LoadThreshold")
    alarms: Optional[List[str]] = Field(default=None, alias="Alarms")


class EbsBlockDeviceModel(BaseModel):
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    iops: Optional[int] = Field(default=None, alias="Iops")
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")
    volume_type: Optional[Literal["gp2", "io1", "standard"]] = Field(
        default=None, alias="VolumeType"
    )
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ChefConfigurationModel(BaseModel):
    manage_berkshelf: Optional[bool] = Field(default=None, alias="ManageBerkshelf")
    berkshelf_version: Optional[str] = Field(default=None, alias="BerkshelfVersion")


class CloudWatchLogsLogStreamModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    datetime_format: Optional[str] = Field(default=None, alias="DatetimeFormat")
    time_zone: Optional[Literal["LOCAL", "UTC"]] = Field(default=None, alias="TimeZone")
    file: Optional[str] = Field(default=None, alias="File")
    file_fingerprint_lines: Optional[str] = Field(
        default=None, alias="FileFingerprintLines"
    )
    multi_line_start_pattern: Optional[str] = Field(
        default=None, alias="MultiLineStartPattern"
    )
    initial_position: Optional[Literal["end_of_file", "start_of_file"]] = Field(
        default=None, alias="InitialPosition"
    )
    encoding: Optional[
        Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_jp",
            "euc_kr",
            "gb18030",
            "gb2312",
            "gbk",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "johab",
            "koi8_r",
            "koi8_u",
            "latin_1",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ]
    ] = Field(default=None, alias="Encoding")
    buffer_duration: Optional[int] = Field(default=None, alias="BufferDuration")
    batch_count: Optional[int] = Field(default=None, alias="BatchCount")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")


class CommandModel(BaseModel):
    command_id: Optional[str] = Field(default=None, alias="CommandId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    acknowledged_at: Optional[str] = Field(default=None, alias="AcknowledgedAt")
    completed_at: Optional[str] = Field(default=None, alias="CompletedAt")
    status: Optional[str] = Field(default=None, alias="Status")
    exit_code: Optional[int] = Field(default=None, alias="ExitCode")
    log_url: Optional[str] = Field(default=None, alias="LogUrl")
    type: Optional[str] = Field(default=None, alias="Type")


class DeploymentCommandModel(BaseModel):
    name: Literal[
        "configure",
        "deploy",
        "execute_recipes",
        "install_dependencies",
        "restart",
        "rollback",
        "setup",
        "start",
        "stop",
        "undeploy",
        "update_custom_cookbooks",
        "update_dependencies",
    ] = Field(alias="Name")
    args: Optional[Mapping[str, Sequence[str]]] = Field(default=None, alias="Args")


class RecipesModel(BaseModel):
    setup: Optional[Sequence[str]] = Field(default=None, alias="Setup")
    configure: Optional[Sequence[str]] = Field(default=None, alias="Configure")
    deploy: Optional[Sequence[str]] = Field(default=None, alias="Deploy")
    undeploy: Optional[Sequence[str]] = Field(default=None, alias="Undeploy")
    shutdown: Optional[Sequence[str]] = Field(default=None, alias="Shutdown")


class VolumeConfigurationModel(BaseModel):
    mount_point: str = Field(alias="MountPoint")
    number_of_disks: int = Field(alias="NumberOfDisks")
    size: int = Field(alias="Size")
    raid_level: Optional[int] = Field(default=None, alias="RaidLevel")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")


class CreateUserProfileRequestModel(BaseModel):
    iam_user_arn: str = Field(alias="IamUserArn")
    ssh_username: Optional[str] = Field(default=None, alias="SshUsername")
    ssh_public_key: Optional[str] = Field(default=None, alias="SshPublicKey")
    allow_self_management: Optional[bool] = Field(
        default=None, alias="AllowSelfManagement"
    )


class DeleteAppRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")


class DeleteInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    delete_elastic_ip: Optional[bool] = Field(default=None, alias="DeleteElasticIp")
    delete_volumes: Optional[bool] = Field(default=None, alias="DeleteVolumes")


class DeleteLayerRequestModel(BaseModel):
    layer_id: str = Field(alias="LayerId")


class DeleteStackRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")


class DeleteUserProfileRequestModel(BaseModel):
    iam_user_arn: str = Field(alias="IamUserArn")


class DeregisterEcsClusterRequestModel(BaseModel):
    ecs_cluster_arn: str = Field(alias="EcsClusterArn")


class DeregisterElasticIpRequestModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")


class DeregisterInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class DeregisterRdsDbInstanceRequestModel(BaseModel):
    rds_db_instance_arn: str = Field(alias="RdsDbInstanceArn")


class DeregisterVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeAppsRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    app_ids: Optional[Sequence[str]] = Field(default=None, alias="AppIds")


class DescribeCommandsRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    command_ids: Optional[Sequence[str]] = Field(default=None, alias="CommandIds")


class DescribeDeploymentsRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    app_id: Optional[str] = Field(default=None, alias="AppId")
    deployment_ids: Optional[Sequence[str]] = Field(default=None, alias="DeploymentIds")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeEcsClustersRequestModel(BaseModel):
    ecs_cluster_arns: Optional[Sequence[str]] = Field(
        default=None, alias="EcsClusterArns"
    )
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class EcsClusterModel(BaseModel):
    ecs_cluster_arn: Optional[str] = Field(default=None, alias="EcsClusterArn")
    ecs_cluster_name: Optional[str] = Field(default=None, alias="EcsClusterName")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    registered_at: Optional[str] = Field(default=None, alias="RegisteredAt")


class DescribeElasticIpsRequestModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    ips: Optional[Sequence[str]] = Field(default=None, alias="Ips")


class ElasticIpModel(BaseModel):
    ip: Optional[str] = Field(default=None, alias="Ip")
    name: Optional[str] = Field(default=None, alias="Name")
    domain: Optional[str] = Field(default=None, alias="Domain")
    region: Optional[str] = Field(default=None, alias="Region")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class DescribeElasticLoadBalancersRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_ids: Optional[Sequence[str]] = Field(default=None, alias="LayerIds")


class ElasticLoadBalancerModel(BaseModel):
    elastic_load_balancer_name: Optional[str] = Field(
        default=None, alias="ElasticLoadBalancerName"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    ec2_instance_ids: Optional[List[str]] = Field(default=None, alias="Ec2InstanceIds")


class DescribeInstancesRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")


class DescribeLayersRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_ids: Optional[Sequence[str]] = Field(default=None, alias="LayerIds")


class DescribeLoadBasedAutoScalingRequestModel(BaseModel):
    layer_ids: Sequence[str] = Field(alias="LayerIds")


class SelfUserProfileModel(BaseModel):
    iam_user_arn: Optional[str] = Field(default=None, alias="IamUserArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ssh_username: Optional[str] = Field(default=None, alias="SshUsername")
    ssh_public_key: Optional[str] = Field(default=None, alias="SshPublicKey")


class DescribePermissionsRequestModel(BaseModel):
    iam_user_arn: Optional[str] = Field(default=None, alias="IamUserArn")
    stack_id: Optional[str] = Field(default=None, alias="StackId")


class PermissionModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    iam_user_arn: Optional[str] = Field(default=None, alias="IamUserArn")
    allow_ssh: Optional[bool] = Field(default=None, alias="AllowSsh")
    allow_sudo: Optional[bool] = Field(default=None, alias="AllowSudo")
    level: Optional[str] = Field(default=None, alias="Level")


class DescribeRaidArraysRequestModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    raid_array_ids: Optional[Sequence[str]] = Field(default=None, alias="RaidArrayIds")


class RaidArrayModel(BaseModel):
    raid_array_id: Optional[str] = Field(default=None, alias="RaidArrayId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    name: Optional[str] = Field(default=None, alias="Name")
    raid_level: Optional[int] = Field(default=None, alias="RaidLevel")
    number_of_disks: Optional[int] = Field(default=None, alias="NumberOfDisks")
    size: Optional[int] = Field(default=None, alias="Size")
    device: Optional[str] = Field(default=None, alias="Device")
    mount_point: Optional[str] = Field(default=None, alias="MountPoint")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    iops: Optional[int] = Field(default=None, alias="Iops")


class DescribeRdsDbInstancesRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    rds_db_instance_arns: Optional[Sequence[str]] = Field(
        default=None, alias="RdsDbInstanceArns"
    )


class RdsDbInstanceModel(BaseModel):
    rds_db_instance_arn: Optional[str] = Field(default=None, alias="RdsDbInstanceArn")
    db_instance_identifier: Optional[str] = Field(
        default=None, alias="DbInstanceIdentifier"
    )
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    db_password: Optional[str] = Field(default=None, alias="DbPassword")
    region: Optional[str] = Field(default=None, alias="Region")
    address: Optional[str] = Field(default=None, alias="Address")
    engine: Optional[str] = Field(default=None, alias="Engine")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    missing_on_rds: Optional[bool] = Field(default=None, alias="MissingOnRds")


class DescribeServiceErrorsRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    service_error_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ServiceErrorIds"
    )


class ServiceErrorModel(BaseModel):
    service_error_id: Optional[str] = Field(default=None, alias="ServiceErrorId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    type: Optional[str] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")


class DescribeStackProvisioningParametersRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")


class DescribeStackSummaryRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")


class DescribeStacksRequestModel(BaseModel):
    stack_ids: Optional[Sequence[str]] = Field(default=None, alias="StackIds")


class DescribeTimeBasedAutoScalingRequestModel(BaseModel):
    instance_ids: Sequence[str] = Field(alias="InstanceIds")


class DescribeUserProfilesRequestModel(BaseModel):
    iam_user_arns: Optional[Sequence[str]] = Field(default=None, alias="IamUserArns")


class UserProfileModel(BaseModel):
    iam_user_arn: Optional[str] = Field(default=None, alias="IamUserArn")
    name: Optional[str] = Field(default=None, alias="Name")
    ssh_username: Optional[str] = Field(default=None, alias="SshUsername")
    ssh_public_key: Optional[str] = Field(default=None, alias="SshPublicKey")
    allow_self_management: Optional[bool] = Field(
        default=None, alias="AllowSelfManagement"
    )


class DescribeVolumesRequestModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    raid_array_id: Optional[str] = Field(default=None, alias="RaidArrayId")
    volume_ids: Optional[Sequence[str]] = Field(default=None, alias="VolumeIds")


class VolumeModel(BaseModel):
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    ec2_volume_id: Optional[str] = Field(default=None, alias="Ec2VolumeId")
    name: Optional[str] = Field(default=None, alias="Name")
    raid_array_id: Optional[str] = Field(default=None, alias="RaidArrayId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    status: Optional[str] = Field(default=None, alias="Status")
    size: Optional[int] = Field(default=None, alias="Size")
    device: Optional[str] = Field(default=None, alias="Device")
    mount_point: Optional[str] = Field(default=None, alias="MountPoint")
    region: Optional[str] = Field(default=None, alias="Region")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")


class DetachElasticLoadBalancerRequestModel(BaseModel):
    elastic_load_balancer_name: str = Field(alias="ElasticLoadBalancerName")
    layer_id: str = Field(alias="LayerId")


class DisassociateElasticIpRequestModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")


class GetHostnameSuggestionRequestModel(BaseModel):
    layer_id: str = Field(alias="LayerId")


class GrantAccessRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    valid_for_in_minutes: Optional[int] = Field(default=None, alias="ValidForInMinutes")


class TemporaryCredentialModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    valid_for_in_minutes: Optional[int] = Field(default=None, alias="ValidForInMinutes")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class InstanceIdentityModel(BaseModel):
    document: Optional[str] = Field(default=None, alias="Document")
    signature: Optional[str] = Field(default=None, alias="Signature")


class ReportedOsModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class InstancesCountModel(BaseModel):
    assigning: Optional[int] = Field(default=None, alias="Assigning")
    booting: Optional[int] = Field(default=None, alias="Booting")
    connection_lost: Optional[int] = Field(default=None, alias="ConnectionLost")
    deregistering: Optional[int] = Field(default=None, alias="Deregistering")
    online: Optional[int] = Field(default=None, alias="Online")
    pending: Optional[int] = Field(default=None, alias="Pending")
    rebooting: Optional[int] = Field(default=None, alias="Rebooting")
    registered: Optional[int] = Field(default=None, alias="Registered")
    registering: Optional[int] = Field(default=None, alias="Registering")
    requested: Optional[int] = Field(default=None, alias="Requested")
    running_setup: Optional[int] = Field(default=None, alias="RunningSetup")
    setup_failed: Optional[int] = Field(default=None, alias="SetupFailed")
    shutting_down: Optional[int] = Field(default=None, alias="ShuttingDown")
    start_failed: Optional[int] = Field(default=None, alias="StartFailed")
    stop_failed: Optional[int] = Field(default=None, alias="StopFailed")
    stopped: Optional[int] = Field(default=None, alias="Stopped")
    stopping: Optional[int] = Field(default=None, alias="Stopping")
    terminated: Optional[int] = Field(default=None, alias="Terminated")
    terminating: Optional[int] = Field(default=None, alias="Terminating")
    unassigning: Optional[int] = Field(default=None, alias="Unassigning")


class ShutdownEventConfigurationModel(BaseModel):
    execution_timeout: Optional[int] = Field(default=None, alias="ExecutionTimeout")
    delay_until_elb_connections_drained: Optional[bool] = Field(
        default=None, alias="DelayUntilElbConnectionsDrained"
    )


class ListTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OperatingSystemConfigurationManagerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class RebootInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class RegisterEcsClusterRequestModel(BaseModel):
    ecs_cluster_arn: str = Field(alias="EcsClusterArn")
    stack_id: str = Field(alias="StackId")


class RegisterElasticIpRequestModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")
    stack_id: str = Field(alias="StackId")


class RegisterRdsDbInstanceRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    rds_db_instance_arn: str = Field(alias="RdsDbInstanceArn")
    db_user: str = Field(alias="DbUser")
    db_password: str = Field(alias="DbPassword")


class RegisterVolumeRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    ec2_volume_id: Optional[str] = Field(default=None, alias="Ec2VolumeId")


class ServiceResourceLayerRequestModel(BaseModel):
    id: str = Field(alias="id")


class ServiceResourceStackRequestModel(BaseModel):
    id: str = Field(alias="id")


class ServiceResourceStackSummaryRequestModel(BaseModel):
    stack_id: str = Field(alias="stack_id")


class SetPermissionRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    iam_user_arn: str = Field(alias="IamUserArn")
    allow_ssh: Optional[bool] = Field(default=None, alias="AllowSsh")
    allow_sudo: Optional[bool] = Field(default=None, alias="AllowSudo")
    level: Optional[str] = Field(default=None, alias="Level")


class WeeklyAutoScalingScheduleModel(BaseModel):
    monday: Optional[Dict[str, str]] = Field(default=None, alias="Monday")
    tuesday: Optional[Dict[str, str]] = Field(default=None, alias="Tuesday")
    wednesday: Optional[Dict[str, str]] = Field(default=None, alias="Wednesday")
    thursday: Optional[Dict[str, str]] = Field(default=None, alias="Thursday")
    friday: Optional[Dict[str, str]] = Field(default=None, alias="Friday")
    saturday: Optional[Dict[str, str]] = Field(default=None, alias="Saturday")
    sunday: Optional[Dict[str, str]] = Field(default=None, alias="Sunday")


class StartInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class StartStackRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")


class StopInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    force: Optional[bool] = Field(default=None, alias="Force")


class StopStackRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UnassignInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class UnassignVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateElasticIpRequestModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    layer_ids: Optional[Sequence[str]] = Field(default=None, alias="LayerIds")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    auto_scaling_type: Optional[Literal["load", "timer"]] = Field(
        default=None, alias="AutoScalingType"
    )
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    os: Optional[str] = Field(default=None, alias="Os")
    ami_id: Optional[str] = Field(default=None, alias="AmiId")
    ssh_key_name: Optional[str] = Field(default=None, alias="SshKeyName")
    architecture: Optional[Literal["i386", "x86_64"]] = Field(
        default=None, alias="Architecture"
    )
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class UpdateMyUserProfileRequestModel(BaseModel):
    ssh_public_key: Optional[str] = Field(default=None, alias="SshPublicKey")


class UpdateRdsDbInstanceRequestModel(BaseModel):
    rds_db_instance_arn: str = Field(alias="RdsDbInstanceArn")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    db_password: Optional[str] = Field(default=None, alias="DbPassword")


class UpdateUserProfileRequestModel(BaseModel):
    iam_user_arn: str = Field(alias="IamUserArn")
    ssh_username: Optional[str] = Field(default=None, alias="SshUsername")
    ssh_public_key: Optional[str] = Field(default=None, alias="SshPublicKey")
    allow_self_management: Optional[bool] = Field(
        default=None, alias="AllowSelfManagement"
    )


class UpdateVolumeRequestModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    name: Optional[str] = Field(default=None, alias="Name")
    mount_point: Optional[str] = Field(default=None, alias="MountPoint")


class AgentVersionModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )


class DescribeAgentVersionsRequestModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )


class AppModel(BaseModel):
    app_id: Optional[str] = Field(default=None, alias="AppId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    shortname: Optional[str] = Field(default=None, alias="Shortname")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    data_sources: Optional[List[DataSourceModel]] = Field(
        default=None, alias="DataSources"
    )
    type: Optional[
        Literal["aws-flow-ruby", "java", "nodejs", "other", "php", "rails", "static"]
    ] = Field(default=None, alias="Type")
    app_source: Optional[SourceModel] = Field(default=None, alias="AppSource")
    domains: Optional[List[str]] = Field(default=None, alias="Domains")
    enable_ssl: Optional[bool] = Field(default=None, alias="EnableSsl")
    ssl_configuration: Optional[SslConfigurationModel] = Field(
        default=None, alias="SslConfiguration"
    )
    attributes: Optional[
        Dict[
            Literal[
                "AutoBundleOnDeploy", "AwsFlowRubySettings", "DocumentRoot", "RailsEnv"
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    environment: Optional[List[EnvironmentVariableModel]] = Field(
        default=None, alias="Environment"
    )


class CreateAppRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    name: str = Field(alias="Name")
    type: Literal[
        "aws-flow-ruby", "java", "nodejs", "other", "php", "rails", "static"
    ] = Field(alias="Type")
    shortname: Optional[str] = Field(default=None, alias="Shortname")
    description: Optional[str] = Field(default=None, alias="Description")
    data_sources: Optional[Sequence[DataSourceModel]] = Field(
        default=None, alias="DataSources"
    )
    app_source: Optional[SourceModel] = Field(default=None, alias="AppSource")
    domains: Optional[Sequence[str]] = Field(default=None, alias="Domains")
    enable_ssl: Optional[bool] = Field(default=None, alias="EnableSsl")
    ssl_configuration: Optional[SslConfigurationModel] = Field(
        default=None, alias="SslConfiguration"
    )
    attributes: Optional[
        Mapping[
            Literal[
                "AutoBundleOnDeploy", "AwsFlowRubySettings", "DocumentRoot", "RailsEnv"
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    environment: Optional[Sequence[EnvironmentVariableModel]] = Field(
        default=None, alias="Environment"
    )


class UpdateAppRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    data_sources: Optional[Sequence[DataSourceModel]] = Field(
        default=None, alias="DataSources"
    )
    type: Optional[
        Literal["aws-flow-ruby", "java", "nodejs", "other", "php", "rails", "static"]
    ] = Field(default=None, alias="Type")
    app_source: Optional[SourceModel] = Field(default=None, alias="AppSource")
    domains: Optional[Sequence[str]] = Field(default=None, alias="Domains")
    enable_ssl: Optional[bool] = Field(default=None, alias="EnableSsl")
    ssl_configuration: Optional[SslConfigurationModel] = Field(
        default=None, alias="SslConfiguration"
    )
    attributes: Optional[
        Mapping[
            Literal[
                "AutoBundleOnDeploy", "AwsFlowRubySettings", "DocumentRoot", "RailsEnv"
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    environment: Optional[Sequence[EnvironmentVariableModel]] = Field(
        default=None, alias="Environment"
    )


class LoadBasedAutoScalingConfigurationModel(BaseModel):
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    enable: Optional[bool] = Field(default=None, alias="Enable")
    up_scaling: Optional[AutoScalingThresholdsModel] = Field(
        default=None, alias="UpScaling"
    )
    down_scaling: Optional[AutoScalingThresholdsModel] = Field(
        default=None, alias="DownScaling"
    )


class SetLoadBasedAutoScalingRequestModel(BaseModel):
    layer_id: str = Field(alias="LayerId")
    enable: Optional[bool] = Field(default=None, alias="Enable")
    up_scaling: Optional[AutoScalingThresholdsModel] = Field(
        default=None, alias="UpScaling"
    )
    down_scaling: Optional[AutoScalingThresholdsModel] = Field(
        default=None, alias="DownScaling"
    )


class BlockDeviceMappingModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    no_device: Optional[str] = Field(default=None, alias="NoDevice")
    virtual_name: Optional[str] = Field(default=None, alias="VirtualName")
    ebs: Optional[EbsBlockDeviceModel] = Field(default=None, alias="Ebs")


class ChefConfigurationResponseMetadataModel(BaseModel):
    manage_berkshelf: bool = Field(alias="ManageBerkshelf")
    berkshelf_version: str = Field(alias="BerkshelfVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloneStackResultModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppResultModel(BaseModel):
    app_id: str = Field(alias="AppId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResultModel(BaseModel):
    deployment_id: str = Field(alias="DeploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceResultModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLayerResultModel(BaseModel):
    layer_id: str = Field(alias="LayerId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStackResultModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserProfileResultModel(BaseModel):
    iam_user_arn: str = Field(alias="IamUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackProvisioningParametersResultModel(BaseModel):
    agent_installer_url: str = Field(alias="AgentInstallerUrl")
    parameters: Dict[str, str] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHostnameSuggestionResultModel(BaseModel):
    layer_id: str = Field(alias="LayerId")
    hostname: str = Field(alias="Hostname")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstancesCountResponseMetadataModel(BaseModel):
    assigning: int = Field(alias="Assigning")
    booting: int = Field(alias="Booting")
    connection_lost: int = Field(alias="ConnectionLost")
    deregistering: int = Field(alias="Deregistering")
    online: int = Field(alias="Online")
    pending: int = Field(alias="Pending")
    rebooting: int = Field(alias="Rebooting")
    registered: int = Field(alias="Registered")
    registering: int = Field(alias="Registering")
    requested: int = Field(alias="Requested")
    running_setup: int = Field(alias="RunningSetup")
    setup_failed: int = Field(alias="SetupFailed")
    shutting_down: int = Field(alias="ShuttingDown")
    start_failed: int = Field(alias="StartFailed")
    stop_failed: int = Field(alias="StopFailed")
    stopped: int = Field(alias="Stopped")
    stopping: int = Field(alias="Stopping")
    terminated: int = Field(alias="Terminated")
    terminating: int = Field(alias="Terminating")
    unassigning: int = Field(alias="Unassigning")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecipesResponseMetadataModel(BaseModel):
    setup: List[str] = Field(alias="Setup")
    configure: List[str] = Field(alias="Configure")
    deploy: List[str] = Field(alias="Deploy")
    undeploy: List[str] = Field(alias="Undeploy")
    shutdown: List[str] = Field(alias="Shutdown")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterEcsClusterResultModel(BaseModel):
    ecs_cluster_arn: str = Field(alias="EcsClusterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterElasticIpResultModel(BaseModel):
    elastic_ip: str = Field(alias="ElasticIp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterInstanceResultModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterVolumeResultModel(BaseModel):
    volume_id: str = Field(alias="VolumeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceResponseMetadataModel(BaseModel):
    type: Literal["archive", "git", "s3", "svn"] = Field(alias="Type")
    url: str = Field(alias="Url")
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")
    ssh_key: str = Field(alias="SshKey")
    revision: str = Field(alias="Revision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StackConfigurationManagerResponseMetadataModel(BaseModel):
    name: str = Field(alias="Name")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloneStackRequestModel(BaseModel):
    source_stack_id: str = Field(alias="SourceStackId")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    name: Optional[str] = Field(default=None, alias="Name")
    region: Optional[str] = Field(default=None, alias="Region")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    attributes: Optional[Mapping[Literal["Color"], str]] = Field(
        default=None, alias="Attributes"
    )
    default_instance_profile_arn: Optional[str] = Field(
        default=None, alias="DefaultInstanceProfileArn"
    )
    default_os: Optional[str] = Field(default=None, alias="DefaultOs")
    hostname_theme: Optional[str] = Field(default=None, alias="HostnameTheme")
    default_availability_zone: Optional[str] = Field(
        default=None, alias="DefaultAvailabilityZone"
    )
    default_subnet_id: Optional[str] = Field(default=None, alias="DefaultSubnetId")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )
    chef_configuration: Optional[ChefConfigurationModel] = Field(
        default=None, alias="ChefConfiguration"
    )
    use_custom_cookbooks: Optional[bool] = Field(
        default=None, alias="UseCustomCookbooks"
    )
    use_opsworks_security_groups: Optional[bool] = Field(
        default=None, alias="UseOpsworksSecurityGroups"
    )
    custom_cookbooks_source: Optional[SourceModel] = Field(
        default=None, alias="CustomCookbooksSource"
    )
    default_ssh_key_name: Optional[str] = Field(default=None, alias="DefaultSshKeyName")
    clone_permissions: Optional[bool] = Field(default=None, alias="ClonePermissions")
    clone_app_ids: Optional[Sequence[str]] = Field(default=None, alias="CloneAppIds")
    default_root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="DefaultRootDeviceType"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class CreateStackRequestModel(BaseModel):
    name: str = Field(alias="Name")
    region: str = Field(alias="Region")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    default_instance_profile_arn: str = Field(alias="DefaultInstanceProfileArn")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    attributes: Optional[Mapping[Literal["Color"], str]] = Field(
        default=None, alias="Attributes"
    )
    default_os: Optional[str] = Field(default=None, alias="DefaultOs")
    hostname_theme: Optional[str] = Field(default=None, alias="HostnameTheme")
    default_availability_zone: Optional[str] = Field(
        default=None, alias="DefaultAvailabilityZone"
    )
    default_subnet_id: Optional[str] = Field(default=None, alias="DefaultSubnetId")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )
    chef_configuration: Optional[ChefConfigurationModel] = Field(
        default=None, alias="ChefConfiguration"
    )
    use_custom_cookbooks: Optional[bool] = Field(
        default=None, alias="UseCustomCookbooks"
    )
    use_opsworks_security_groups: Optional[bool] = Field(
        default=None, alias="UseOpsworksSecurityGroups"
    )
    custom_cookbooks_source: Optional[SourceModel] = Field(
        default=None, alias="CustomCookbooksSource"
    )
    default_ssh_key_name: Optional[str] = Field(default=None, alias="DefaultSshKeyName")
    default_root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="DefaultRootDeviceType"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class CreateStackRequestServiceResourceCreateStackModel(BaseModel):
    name: str = Field(alias="Name")
    region: str = Field(alias="Region")
    service_role_arn: str = Field(alias="ServiceRoleArn")
    default_instance_profile_arn: str = Field(alias="DefaultInstanceProfileArn")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    attributes: Optional[Mapping[Literal["Color"], str]] = Field(
        default=None, alias="Attributes"
    )
    default_os: Optional[str] = Field(default=None, alias="DefaultOs")
    hostname_theme: Optional[str] = Field(default=None, alias="HostnameTheme")
    default_availability_zone: Optional[str] = Field(
        default=None, alias="DefaultAvailabilityZone"
    )
    default_subnet_id: Optional[str] = Field(default=None, alias="DefaultSubnetId")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )
    chef_configuration: Optional[ChefConfigurationModel] = Field(
        default=None, alias="ChefConfiguration"
    )
    use_custom_cookbooks: Optional[bool] = Field(
        default=None, alias="UseCustomCookbooks"
    )
    use_opsworks_security_groups: Optional[bool] = Field(
        default=None, alias="UseOpsworksSecurityGroups"
    )
    custom_cookbooks_source: Optional[SourceModel] = Field(
        default=None, alias="CustomCookbooksSource"
    )
    default_ssh_key_name: Optional[str] = Field(default=None, alias="DefaultSshKeyName")
    default_root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="DefaultRootDeviceType"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class StackModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    region: Optional[str] = Field(default=None, alias="Region")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    attributes: Optional[Dict[Literal["Color"], str]] = Field(
        default=None, alias="Attributes"
    )
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    default_instance_profile_arn: Optional[str] = Field(
        default=None, alias="DefaultInstanceProfileArn"
    )
    default_os: Optional[str] = Field(default=None, alias="DefaultOs")
    hostname_theme: Optional[str] = Field(default=None, alias="HostnameTheme")
    default_availability_zone: Optional[str] = Field(
        default=None, alias="DefaultAvailabilityZone"
    )
    default_subnet_id: Optional[str] = Field(default=None, alias="DefaultSubnetId")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )
    chef_configuration: Optional[ChefConfigurationModel] = Field(
        default=None, alias="ChefConfiguration"
    )
    use_custom_cookbooks: Optional[bool] = Field(
        default=None, alias="UseCustomCookbooks"
    )
    use_opsworks_security_groups: Optional[bool] = Field(
        default=None, alias="UseOpsworksSecurityGroups"
    )
    custom_cookbooks_source: Optional[SourceModel] = Field(
        default=None, alias="CustomCookbooksSource"
    )
    default_ssh_key_name: Optional[str] = Field(default=None, alias="DefaultSshKeyName")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    default_root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="DefaultRootDeviceType"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class UpdateStackRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    name: Optional[str] = Field(default=None, alias="Name")
    attributes: Optional[Mapping[Literal["Color"], str]] = Field(
        default=None, alias="Attributes"
    )
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    default_instance_profile_arn: Optional[str] = Field(
        default=None, alias="DefaultInstanceProfileArn"
    )
    default_os: Optional[str] = Field(default=None, alias="DefaultOs")
    hostname_theme: Optional[str] = Field(default=None, alias="HostnameTheme")
    default_availability_zone: Optional[str] = Field(
        default=None, alias="DefaultAvailabilityZone"
    )
    default_subnet_id: Optional[str] = Field(default=None, alias="DefaultSubnetId")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    configuration_manager: Optional[StackConfigurationManagerModel] = Field(
        default=None, alias="ConfigurationManager"
    )
    chef_configuration: Optional[ChefConfigurationModel] = Field(
        default=None, alias="ChefConfiguration"
    )
    use_custom_cookbooks: Optional[bool] = Field(
        default=None, alias="UseCustomCookbooks"
    )
    custom_cookbooks_source: Optional[SourceModel] = Field(
        default=None, alias="CustomCookbooksSource"
    )
    default_ssh_key_name: Optional[str] = Field(default=None, alias="DefaultSshKeyName")
    default_root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="DefaultRootDeviceType"
    )
    use_opsworks_security_groups: Optional[bool] = Field(
        default=None, alias="UseOpsworksSecurityGroups"
    )
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")


class CloudWatchLogsConfigurationResponseMetadataModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    log_streams: List[CloudWatchLogsLogStreamModel] = Field(alias="LogStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloudWatchLogsConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    log_streams: Optional[Sequence[CloudWatchLogsLogStreamModel]] = Field(
        default=None, alias="LogStreams"
    )


class DescribeCommandsResultModel(BaseModel):
    commands: List[CommandModel] = Field(alias="Commands")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    command: DeploymentCommandModel = Field(alias="Command")
    app_id: Optional[str] = Field(default=None, alias="AppId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    layer_ids: Optional[Sequence[str]] = Field(default=None, alias="LayerIds")
    comment: Optional[str] = Field(default=None, alias="Comment")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")


class DeploymentModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    app_id: Optional[str] = Field(default=None, alias="AppId")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    completed_at: Optional[str] = Field(default=None, alias="CompletedAt")
    duration: Optional[int] = Field(default=None, alias="Duration")
    iam_user_arn: Optional[str] = Field(default=None, alias="IamUserArn")
    comment: Optional[str] = Field(default=None, alias="Comment")
    command: Optional[DeploymentCommandModel] = Field(default=None, alias="Command")
    status: Optional[str] = Field(default=None, alias="Status")
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    instance_ids: Optional[List[str]] = Field(default=None, alias="InstanceIds")


class DescribeAppsRequestAppExistsWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    app_ids: Optional[Sequence[str]] = Field(default=None, alias="AppIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeDeploymentsRequestDeploymentSuccessfulWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    app_id: Optional[str] = Field(default=None, alias="AppId")
    deployment_ids: Optional[Sequence[str]] = Field(default=None, alias="DeploymentIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInstancesRequestInstanceOnlineWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInstancesRequestInstanceRegisteredWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInstancesRequestInstanceStoppedWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeInstancesRequestInstanceTerminatedWaitModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEcsClustersRequestDescribeEcsClustersPaginateModel(BaseModel):
    ecs_cluster_arns: Optional[Sequence[str]] = Field(
        default=None, alias="EcsClusterArns"
    )
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEcsClustersResultModel(BaseModel):
    ecs_clusters: List[EcsClusterModel] = Field(alias="EcsClusters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeElasticIpsResultModel(BaseModel):
    elastic_ips: List[ElasticIpModel] = Field(alias="ElasticIps")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeElasticLoadBalancersResultModel(BaseModel):
    elastic_load_balancers: List[ElasticLoadBalancerModel] = Field(
        alias="ElasticLoadBalancers"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMyUserProfileResultModel(BaseModel):
    user_profile: SelfUserProfileModel = Field(alias="UserProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePermissionsResultModel(BaseModel):
    permissions: List[PermissionModel] = Field(alias="Permissions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRaidArraysResultModel(BaseModel):
    raid_arrays: List[RaidArrayModel] = Field(alias="RaidArrays")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRdsDbInstancesResultModel(BaseModel):
    rds_db_instances: List[RdsDbInstanceModel] = Field(alias="RdsDbInstances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServiceErrorsResultModel(BaseModel):
    service_errors: List[ServiceErrorModel] = Field(alias="ServiceErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserProfilesResultModel(BaseModel):
    user_profiles: List[UserProfileModel] = Field(alias="UserProfiles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVolumesResultModel(BaseModel):
    volumes: List[VolumeModel] = Field(alias="Volumes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GrantAccessResultModel(BaseModel):
    temporary_credential: TemporaryCredentialModel = Field(alias="TemporaryCredential")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterInstanceRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    public_ip: Optional[str] = Field(default=None, alias="PublicIp")
    private_ip: Optional[str] = Field(default=None, alias="PrivateIp")
    rsa_public_key: Optional[str] = Field(default=None, alias="RsaPublicKey")
    rsa_public_key_fingerprint: Optional[str] = Field(
        default=None, alias="RsaPublicKeyFingerprint"
    )
    instance_identity: Optional[InstanceIdentityModel] = Field(
        default=None, alias="InstanceIdentity"
    )


class StackSummaryModel(BaseModel):
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    layers_count: Optional[int] = Field(default=None, alias="LayersCount")
    apps_count: Optional[int] = Field(default=None, alias="AppsCount")
    instances_count: Optional[InstancesCountModel] = Field(
        default=None, alias="InstancesCount"
    )


class LifecycleEventConfigurationResponseMetadataModel(BaseModel):
    shutdown: ShutdownEventConfigurationModel = Field(alias="Shutdown")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifecycleEventConfigurationModel(BaseModel):
    shutdown: Optional[ShutdownEventConfigurationModel] = Field(
        default=None, alias="Shutdown"
    )


class OperatingSystemModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[str] = Field(default=None, alias="Type")
    configuration_managers: Optional[
        List[OperatingSystemConfigurationManagerModel]
    ] = Field(default=None, alias="ConfigurationManagers")
    reported_name: Optional[str] = Field(default=None, alias="ReportedName")
    reported_version: Optional[str] = Field(default=None, alias="ReportedVersion")
    supported: Optional[bool] = Field(default=None, alias="Supported")


class SetTimeBasedAutoScalingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    auto_scaling_schedule: Optional[WeeklyAutoScalingScheduleModel] = Field(
        default=None, alias="AutoScalingSchedule"
    )


class TimeBasedAutoScalingConfigurationModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    auto_scaling_schedule: Optional[WeeklyAutoScalingScheduleModel] = Field(
        default=None, alias="AutoScalingSchedule"
    )


class DescribeAgentVersionsResultModel(BaseModel):
    agent_versions: List[AgentVersionModel] = Field(alias="AgentVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppsResultModel(BaseModel):
    apps: List[AppModel] = Field(alias="Apps")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoadBasedAutoScalingResultModel(BaseModel):
    load_based_auto_scaling_configurations: List[
        LoadBasedAutoScalingConfigurationModel
    ] = Field(alias="LoadBasedAutoScalingConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    layer_ids: Sequence[str] = Field(alias="LayerIds")
    instance_type: str = Field(alias="InstanceType")
    auto_scaling_type: Optional[Literal["load", "timer"]] = Field(
        default=None, alias="AutoScalingType"
    )
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    os: Optional[str] = Field(default=None, alias="Os")
    ami_id: Optional[str] = Field(default=None, alias="AmiId")
    ssh_key_name: Optional[str] = Field(default=None, alias="SshKeyName")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    virtualization_type: Optional[str] = Field(default=None, alias="VirtualizationType")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    architecture: Optional[Literal["i386", "x86_64"]] = Field(
        default=None, alias="Architecture"
    )
    root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="RootDeviceType"
    )
    block_device_mappings: Optional[Sequence[BlockDeviceMappingModel]] = Field(
        default=None, alias="BlockDeviceMappings"
    )
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")
    tenancy: Optional[str] = Field(default=None, alias="Tenancy")


class InstanceModel(BaseModel):
    agent_version: Optional[str] = Field(default=None, alias="AgentVersion")
    ami_id: Optional[str] = Field(default=None, alias="AmiId")
    architecture: Optional[Literal["i386", "x86_64"]] = Field(
        default=None, alias="Architecture"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    auto_scaling_type: Optional[Literal["load", "timer"]] = Field(
        default=None, alias="AutoScalingType"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    block_device_mappings: Optional[List[BlockDeviceMappingModel]] = Field(
        default=None, alias="BlockDeviceMappings"
    )
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    ec2_instance_id: Optional[str] = Field(default=None, alias="Ec2InstanceId")
    ecs_cluster_arn: Optional[str] = Field(default=None, alias="EcsClusterArn")
    ecs_container_instance_arn: Optional[str] = Field(
        default=None, alias="EcsContainerInstanceArn"
    )
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    infrastructure_class: Optional[str] = Field(
        default=None, alias="InfrastructureClass"
    )
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_profile_arn: Optional[str] = Field(
        default=None, alias="InstanceProfileArn"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    last_service_error_id: Optional[str] = Field(
        default=None, alias="LastServiceErrorId"
    )
    layer_ids: Optional[List[str]] = Field(default=None, alias="LayerIds")
    os: Optional[str] = Field(default=None, alias="Os")
    platform: Optional[str] = Field(default=None, alias="Platform")
    private_dns: Optional[str] = Field(default=None, alias="PrivateDns")
    private_ip: Optional[str] = Field(default=None, alias="PrivateIp")
    public_dns: Optional[str] = Field(default=None, alias="PublicDns")
    public_ip: Optional[str] = Field(default=None, alias="PublicIp")
    registered_by: Optional[str] = Field(default=None, alias="RegisteredBy")
    reported_agent_version: Optional[str] = Field(
        default=None, alias="ReportedAgentVersion"
    )
    reported_os: Optional[ReportedOsModel] = Field(default=None, alias="ReportedOs")
    root_device_type: Optional[Literal["ebs", "instance-store"]] = Field(
        default=None, alias="RootDeviceType"
    )
    root_device_volume_id: Optional[str] = Field(
        default=None, alias="RootDeviceVolumeId"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    ssh_host_dsa_key_fingerprint: Optional[str] = Field(
        default=None, alias="SshHostDsaKeyFingerprint"
    )
    ssh_host_rsa_key_fingerprint: Optional[str] = Field(
        default=None, alias="SshHostRsaKeyFingerprint"
    )
    ssh_key_name: Optional[str] = Field(default=None, alias="SshKeyName")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    status: Optional[str] = Field(default=None, alias="Status")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    tenancy: Optional[str] = Field(default=None, alias="Tenancy")
    virtualization_type: Optional[Literal["hvm", "paravirtual"]] = Field(
        default=None, alias="VirtualizationType"
    )


class DescribeStacksResultModel(BaseModel):
    stacks: List[StackModel] = Field(alias="Stacks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDeploymentsResultModel(BaseModel):
    deployments: List[DeploymentModel] = Field(alias="Deployments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStackSummaryResultModel(BaseModel):
    stack_summary: StackSummaryModel = Field(alias="StackSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLayerRequestModel(BaseModel):
    stack_id: str = Field(alias="StackId")
    type: Literal[
        "aws-flow-ruby",
        "custom",
        "db-master",
        "ecs-cluster",
        "java-app",
        "lb",
        "memcached",
        "monitoring-master",
        "nodejs-app",
        "php-app",
        "rails-app",
        "web",
    ] = Field(alias="Type")
    name: str = Field(alias="Name")
    shortname: str = Field(alias="Shortname")
    attributes: Optional[
        Mapping[
            Literal[
                "BundlerVersion",
                "EcsClusterArn",
                "EnableHaproxyStats",
                "GangliaPassword",
                "GangliaUrl",
                "GangliaUser",
                "HaproxyHealthCheckMethod",
                "HaproxyHealthCheckUrl",
                "HaproxyStatsPassword",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "JavaAppServer",
                "JavaAppServerVersion",
                "Jvm",
                "JvmOptions",
                "JvmVersion",
                "ManageBundler",
                "MemcachedMemory",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "NodejsVersion",
                "PassengerVersion",
                "RailsStack",
                "RubyVersion",
                "RubygemsVersion",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfigurationModel] = Field(
        default=None, alias="CloudWatchLogsConfiguration"
    )
    custom_instance_profile_arn: Optional[str] = Field(
        default=None, alias="CustomInstanceProfileArn"
    )
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    custom_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CustomSecurityGroupIds"
    )
    packages: Optional[Sequence[str]] = Field(default=None, alias="Packages")
    volume_configurations: Optional[Sequence[VolumeConfigurationModel]] = Field(
        default=None, alias="VolumeConfigurations"
    )
    enable_auto_healing: Optional[bool] = Field(default=None, alias="EnableAutoHealing")
    auto_assign_elastic_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignElasticIps"
    )
    auto_assign_public_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignPublicIps"
    )
    custom_recipes: Optional[RecipesModel] = Field(default=None, alias="CustomRecipes")
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    use_ebs_optimized_instances: Optional[bool] = Field(
        default=None, alias="UseEbsOptimizedInstances"
    )
    lifecycle_event_configuration: Optional[LifecycleEventConfigurationModel] = Field(
        default=None, alias="LifecycleEventConfiguration"
    )


class CreateLayerRequestStackCreateLayerModel(BaseModel):
    type: Literal[
        "aws-flow-ruby",
        "custom",
        "db-master",
        "ecs-cluster",
        "java-app",
        "lb",
        "memcached",
        "monitoring-master",
        "nodejs-app",
        "php-app",
        "rails-app",
        "web",
    ] = Field(alias="Type")
    name: str = Field(alias="Name")
    shortname: str = Field(alias="Shortname")
    attributes: Optional[
        Mapping[
            Literal[
                "BundlerVersion",
                "EcsClusterArn",
                "EnableHaproxyStats",
                "GangliaPassword",
                "GangliaUrl",
                "GangliaUser",
                "HaproxyHealthCheckMethod",
                "HaproxyHealthCheckUrl",
                "HaproxyStatsPassword",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "JavaAppServer",
                "JavaAppServerVersion",
                "Jvm",
                "JvmOptions",
                "JvmVersion",
                "ManageBundler",
                "MemcachedMemory",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "NodejsVersion",
                "PassengerVersion",
                "RailsStack",
                "RubyVersion",
                "RubygemsVersion",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfigurationModel] = Field(
        default=None, alias="CloudWatchLogsConfiguration"
    )
    custom_instance_profile_arn: Optional[str] = Field(
        default=None, alias="CustomInstanceProfileArn"
    )
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    custom_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CustomSecurityGroupIds"
    )
    packages: Optional[Sequence[str]] = Field(default=None, alias="Packages")
    volume_configurations: Optional[Sequence[VolumeConfigurationModel]] = Field(
        default=None, alias="VolumeConfigurations"
    )
    enable_auto_healing: Optional[bool] = Field(default=None, alias="EnableAutoHealing")
    auto_assign_elastic_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignElasticIps"
    )
    auto_assign_public_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignPublicIps"
    )
    custom_recipes: Optional[RecipesModel] = Field(default=None, alias="CustomRecipes")
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    use_ebs_optimized_instances: Optional[bool] = Field(
        default=None, alias="UseEbsOptimizedInstances"
    )
    lifecycle_event_configuration: Optional[LifecycleEventConfigurationModel] = Field(
        default=None, alias="LifecycleEventConfiguration"
    )


class LayerModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    layer_id: Optional[str] = Field(default=None, alias="LayerId")
    type: Optional[
        Literal[
            "aws-flow-ruby",
            "custom",
            "db-master",
            "ecs-cluster",
            "java-app",
            "lb",
            "memcached",
            "monitoring-master",
            "nodejs-app",
            "php-app",
            "rails-app",
            "web",
        ]
    ] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    shortname: Optional[str] = Field(default=None, alias="Shortname")
    attributes: Optional[
        Dict[
            Literal[
                "BundlerVersion",
                "EcsClusterArn",
                "EnableHaproxyStats",
                "GangliaPassword",
                "GangliaUrl",
                "GangliaUser",
                "HaproxyHealthCheckMethod",
                "HaproxyHealthCheckUrl",
                "HaproxyStatsPassword",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "JavaAppServer",
                "JavaAppServerVersion",
                "Jvm",
                "JvmOptions",
                "JvmVersion",
                "ManageBundler",
                "MemcachedMemory",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "NodejsVersion",
                "PassengerVersion",
                "RailsStack",
                "RubyVersion",
                "RubygemsVersion",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfigurationModel] = Field(
        default=None, alias="CloudWatchLogsConfiguration"
    )
    custom_instance_profile_arn: Optional[str] = Field(
        default=None, alias="CustomInstanceProfileArn"
    )
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    custom_security_group_ids: Optional[List[str]] = Field(
        default=None, alias="CustomSecurityGroupIds"
    )
    default_security_group_names: Optional[List[str]] = Field(
        default=None, alias="DefaultSecurityGroupNames"
    )
    packages: Optional[List[str]] = Field(default=None, alias="Packages")
    volume_configurations: Optional[List[VolumeConfigurationModel]] = Field(
        default=None, alias="VolumeConfigurations"
    )
    enable_auto_healing: Optional[bool] = Field(default=None, alias="EnableAutoHealing")
    auto_assign_elastic_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignElasticIps"
    )
    auto_assign_public_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignPublicIps"
    )
    default_recipes: Optional[RecipesModel] = Field(
        default=None, alias="DefaultRecipes"
    )
    custom_recipes: Optional[RecipesModel] = Field(default=None, alias="CustomRecipes")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    use_ebs_optimized_instances: Optional[bool] = Field(
        default=None, alias="UseEbsOptimizedInstances"
    )
    lifecycle_event_configuration: Optional[LifecycleEventConfigurationModel] = Field(
        default=None, alias="LifecycleEventConfiguration"
    )


class UpdateLayerRequestModel(BaseModel):
    layer_id: str = Field(alias="LayerId")
    name: Optional[str] = Field(default=None, alias="Name")
    shortname: Optional[str] = Field(default=None, alias="Shortname")
    attributes: Optional[
        Mapping[
            Literal[
                "BundlerVersion",
                "EcsClusterArn",
                "EnableHaproxyStats",
                "GangliaPassword",
                "GangliaUrl",
                "GangliaUser",
                "HaproxyHealthCheckMethod",
                "HaproxyHealthCheckUrl",
                "HaproxyStatsPassword",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "JavaAppServer",
                "JavaAppServerVersion",
                "Jvm",
                "JvmOptions",
                "JvmVersion",
                "ManageBundler",
                "MemcachedMemory",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "NodejsVersion",
                "PassengerVersion",
                "RailsStack",
                "RubyVersion",
                "RubygemsVersion",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfigurationModel] = Field(
        default=None, alias="CloudWatchLogsConfiguration"
    )
    custom_instance_profile_arn: Optional[str] = Field(
        default=None, alias="CustomInstanceProfileArn"
    )
    custom_json: Optional[str] = Field(default=None, alias="CustomJson")
    custom_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CustomSecurityGroupIds"
    )
    packages: Optional[Sequence[str]] = Field(default=None, alias="Packages")
    volume_configurations: Optional[Sequence[VolumeConfigurationModel]] = Field(
        default=None, alias="VolumeConfigurations"
    )
    enable_auto_healing: Optional[bool] = Field(default=None, alias="EnableAutoHealing")
    auto_assign_elastic_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignElasticIps"
    )
    auto_assign_public_ips: Optional[bool] = Field(
        default=None, alias="AutoAssignPublicIps"
    )
    custom_recipes: Optional[RecipesModel] = Field(default=None, alias="CustomRecipes")
    install_updates_on_boot: Optional[bool] = Field(
        default=None, alias="InstallUpdatesOnBoot"
    )
    use_ebs_optimized_instances: Optional[bool] = Field(
        default=None, alias="UseEbsOptimizedInstances"
    )
    lifecycle_event_configuration: Optional[LifecycleEventConfigurationModel] = Field(
        default=None, alias="LifecycleEventConfiguration"
    )


class DescribeOperatingSystemsResponseModel(BaseModel):
    operating_systems: List[OperatingSystemModel] = Field(alias="OperatingSystems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTimeBasedAutoScalingResultModel(BaseModel):
    time_based_auto_scaling_configurations: List[
        TimeBasedAutoScalingConfigurationModel
    ] = Field(alias="TimeBasedAutoScalingConfigurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstancesResultModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLayersResultModel(BaseModel):
    layers: List[LayerModel] = Field(alias="Layers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
