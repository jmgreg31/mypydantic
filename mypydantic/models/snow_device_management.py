# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelTaskInputRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CapacityModel(BaseModel):
    available: Optional[int] = Field(default=None, alias="available")
    name: Optional[str] = Field(default=None, alias="name")
    total: Optional[int] = Field(default=None, alias="total")
    unit: Optional[str] = Field(default=None, alias="unit")
    used: Optional[int] = Field(default=None, alias="used")


class CommandModel(BaseModel):
    reboot: Optional[Mapping[str, Any]] = Field(default=None, alias="reboot")
    unlock: Optional[Mapping[str, Any]] = Field(default=None, alias="unlock")


class CpuOptionsModel(BaseModel):
    core_count: Optional[int] = Field(default=None, alias="coreCount")
    threads_per_core: Optional[int] = Field(default=None, alias="threadsPerCore")


class DescribeDeviceEc2InputRequestModel(BaseModel):
    instance_ids: Sequence[str] = Field(alias="instanceIds")
    managed_device_id: str = Field(alias="managedDeviceId")


class DescribeDeviceInputRequestModel(BaseModel):
    managed_device_id: str = Field(alias="managedDeviceId")


class PhysicalNetworkInterfaceModel(BaseModel):
    default_gateway: Optional[str] = Field(default=None, alias="defaultGateway")
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    ip_address_assignment: Optional[Literal["DHCP", "STATIC"]] = Field(
        default=None, alias="ipAddressAssignment"
    )
    mac_address: Optional[str] = Field(default=None, alias="macAddress")
    netmask: Optional[str] = Field(default=None, alias="netmask")
    physical_connector_type: Optional[
        Literal["QSFP", "RJ45", "RJ45_2", "SFP_PLUS", "WIFI"]
    ] = Field(default=None, alias="physicalConnectorType")
    physical_network_interface_id: Optional[str] = Field(
        default=None, alias="physicalNetworkInterfaceId"
    )


class SoftwareInformationModel(BaseModel):
    install_state: Optional[str] = Field(default=None, alias="installState")
    installed_version: Optional[str] = Field(default=None, alias="installedVersion")
    installing_version: Optional[str] = Field(default=None, alias="installingVersion")


class DescribeExecutionInputRequestModel(BaseModel):
    managed_device_id: str = Field(alias="managedDeviceId")
    task_id: str = Field(alias="taskId")


class DescribeTaskInputRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class DeviceSummaryModel(BaseModel):
    associated_with_job: Optional[str] = Field(default=None, alias="associatedWithJob")
    managed_device_arn: Optional[str] = Field(default=None, alias="managedDeviceArn")
    managed_device_id: Optional[str] = Field(default=None, alias="managedDeviceId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class EbsInstanceBlockDeviceModel(BaseModel):
    attach_time: Optional[datetime] = Field(default=None, alias="attachTime")
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="deleteOnTermination"
    )
    status: Optional[Literal["ATTACHED", "ATTACHING", "DETACHED", "DETACHING"]] = Field(
        default=None, alias="status"
    )
    volume_id: Optional[str] = Field(default=None, alias="volumeId")


class ExecutionSummaryModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="executionId")
    managed_device_id: Optional[str] = Field(default=None, alias="managedDeviceId")
    state: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="state")
    task_id: Optional[str] = Field(default=None, alias="taskId")


class InstanceStateModel(BaseModel):
    code: Optional[int] = Field(default=None, alias="code")
    name: Optional[
        Literal[
            "PENDING", "RUNNING", "SHUTTING_DOWN", "STOPPED", "STOPPING", "TERMINATED"
        ]
    ] = Field(default=None, alias="name")


class SecurityGroupIdentifierModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="groupId")
    group_name: Optional[str] = Field(default=None, alias="groupName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDeviceResourcesInputRequestModel(BaseModel):
    managed_device_id: str = Field(alias="managedDeviceId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    type: Optional[str] = Field(default=None, alias="type")


class ResourceSummaryModel(BaseModel):
    resource_type: str = Field(alias="resourceType")
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")


class ListDevicesInputRequestModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListExecutionsInputRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    state: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="state")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTasksInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    state: Optional[Literal["CANCELED", "COMPLETED", "IN_PROGRESS"]] = Field(
        default=None, alias="state"
    )


class TaskSummaryModel(BaseModel):
    task_id: str = Field(alias="taskId")
    state: Optional[Literal["CANCELED", "COMPLETED", "IN_PROGRESS"]] = Field(
        default=None, alias="state"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    task_arn: Optional[str] = Field(default=None, alias="taskArn")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CancelTaskOutputModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskOutputModel(BaseModel):
    task_arn: str = Field(alias="taskArn")
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExecutionOutputModel(BaseModel):
    execution_id: str = Field(alias="executionId")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    managed_device_id: str = Field(alias="managedDeviceId")
    started_at: datetime = Field(alias="startedAt")
    state: Literal[
        "CANCELED",
        "FAILED",
        "IN_PROGRESS",
        "QUEUED",
        "REJECTED",
        "SUCCEEDED",
        "TIMED_OUT",
    ] = Field(alias="state")
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTaskOutputModel(BaseModel):
    completed_at: datetime = Field(alias="completedAt")
    created_at: datetime = Field(alias="createdAt")
    description: str = Field(alias="description")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    state: Literal["CANCELED", "COMPLETED", "IN_PROGRESS"] = Field(alias="state")
    tags: Dict[str, str] = Field(alias="tags")
    targets: List[str] = Field(alias="targets")
    task_arn: str = Field(alias="taskArn")
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskInputRequestModel(BaseModel):
    command: CommandModel = Field(alias="command")
    targets: Sequence[str] = Field(alias="targets")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DescribeDeviceOutputModel(BaseModel):
    associated_with_job: str = Field(alias="associatedWithJob")
    device_capacities: List[CapacityModel] = Field(alias="deviceCapacities")
    device_state: Literal["LOCKED", "UNLOCKED", "UNLOCKING"] = Field(
        alias="deviceState"
    )
    device_type: str = Field(alias="deviceType")
    last_reached_out_at: datetime = Field(alias="lastReachedOutAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    managed_device_arn: str = Field(alias="managedDeviceArn")
    managed_device_id: str = Field(alias="managedDeviceId")
    physical_network_interfaces: List[PhysicalNetworkInterfaceModel] = Field(
        alias="physicalNetworkInterfaces"
    )
    software: SoftwareInformationModel = Field(alias="software")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesOutputModel(BaseModel):
    devices: List[DeviceSummaryModel] = Field(alias="devices")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceBlockDeviceMappingModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    ebs: Optional[EbsInstanceBlockDeviceModel] = Field(default=None, alias="ebs")


class ListExecutionsOutputModel(BaseModel):
    executions: List[ExecutionSummaryModel] = Field(alias="executions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceResourcesInputListDeviceResourcesPaginateModel(BaseModel):
    managed_device_id: str = Field(alias="managedDeviceId")
    type: Optional[str] = Field(default=None, alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicesInputListDevicesPaginateModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExecutionsInputListExecutionsPaginateModel(BaseModel):
    task_id: str = Field(alias="taskId")
    state: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="state")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTasksInputListTasksPaginateModel(BaseModel):
    state: Optional[Literal["CANCELED", "COMPLETED", "IN_PROGRESS"]] = Field(
        default=None, alias="state"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceResourcesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resources: List[ResourceSummaryModel] = Field(alias="resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTasksOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tasks: List[TaskSummaryModel] = Field(alias="tasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceModel(BaseModel):
    ami_launch_index: Optional[int] = Field(default=None, alias="amiLaunchIndex")
    block_device_mappings: Optional[List[InstanceBlockDeviceMappingModel]] = Field(
        default=None, alias="blockDeviceMappings"
    )
    cpu_options: Optional[CpuOptionsModel] = Field(default=None, alias="cpuOptions")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    image_id: Optional[str] = Field(default=None, alias="imageId")
    instance_id: Optional[str] = Field(default=None, alias="instanceId")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")
    public_ip_address: Optional[str] = Field(default=None, alias="publicIpAddress")
    root_device_name: Optional[str] = Field(default=None, alias="rootDeviceName")
    security_groups: Optional[List[SecurityGroupIdentifierModel]] = Field(
        default=None, alias="securityGroups"
    )
    state: Optional[InstanceStateModel] = Field(default=None, alias="state")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class InstanceSummaryModel(BaseModel):
    instance: Optional[InstanceModel] = Field(default=None, alias="instance")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class DescribeDeviceEc2OutputModel(BaseModel):
    instances: List[InstanceSummaryModel] = Field(alias="instances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
