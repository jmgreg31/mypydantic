# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlternateSoftwareMetadataModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")


class ReportedRuntimeContextStateModel(BaseModel):
    desired_state: Literal["REMOVED", "RUNNING", "STOPPED"] = Field(
        alias="DesiredState"
    )
    device_reported_status: Literal[
        "INSTALL_ERROR",
        "INSTALL_IN_PROGRESS",
        "LAUNCHED",
        "LAUNCH_ERROR",
        "REMOVAL_FAILED",
        "REMOVAL_IN_PROGRESS",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "STOP_ERROR",
    ] = Field(alias="DeviceReportedStatus")
    device_reported_time: datetime = Field(alias="DeviceReportedTime")
    runtime_context_name: str = Field(alias="RuntimeContextName")


class ManifestOverridesPayloadModel(BaseModel):
    payload_data: Optional[str] = Field(default=None, alias="PayloadData")


class ManifestPayloadModel(BaseModel):
    payload_data: Optional[str] = Field(default=None, alias="PayloadData")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class JobModel(BaseModel):
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    job_id: Optional[str] = Field(default=None, alias="JobId")


class JobResourceTagsModel(BaseModel):
    resource_type: Literal["PACKAGE"] = Field(alias="ResourceType")
    tags: Mapping[str, str] = Field(alias="Tags")


class CreatePackageRequestModel(BaseModel):
    package_name: str = Field(alias="PackageName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class StorageLocationModel(BaseModel):
    binary_prefix_location: str = Field(alias="BinaryPrefixLocation")
    bucket: str = Field(alias="Bucket")
    generated_prefix_location: str = Field(alias="GeneratedPrefixLocation")
    manifest_prefix_location: str = Field(alias="ManifestPrefixLocation")
    repo_prefix_location: str = Field(alias="RepoPrefixLocation")


class DeleteDeviceRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class DeletePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageId")
    force_delete: Optional[bool] = Field(default=None, alias="ForceDelete")


class DeregisterPackageVersionRequestModel(BaseModel):
    package_id: str = Field(alias="PackageId")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    updated_latest_patch_version: Optional[str] = Field(
        default=None, alias="UpdatedLatestPatchVersion"
    )


class DescribeApplicationInstanceDetailsRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")


class DescribeApplicationInstanceRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")


class DescribeDeviceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeDeviceRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")


class LatestDeviceJobModel(BaseModel):
    image_version: Optional[str] = Field(default=None, alias="ImageVersion")
    job_type: Optional[Literal["OTA", "REBOOT"]] = Field(default=None, alias="JobType")
    status: Optional[
        Literal[
            "COMPLETED",
            "DOWNLOADING",
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "REBOOTING",
            "VERIFYING",
        ]
    ] = Field(default=None, alias="Status")


class DescribeNodeFromTemplateJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeNodeRequestModel(BaseModel):
    node_id: str = Field(alias="NodeId")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")


class DescribePackageImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageId")


class DescribePackageVersionRequestModel(BaseModel):
    package_id: str = Field(alias="PackageId")
    package_version: str = Field(alias="PackageVersion")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    patch_version: Optional[str] = Field(default=None, alias="PatchVersion")


class OTAJobConfigModel(BaseModel):
    image_version: str = Field(alias="ImageVersion")
    allow_major_version_update: Optional[bool] = Field(
        default=None, alias="AllowMajorVersionUpdate"
    )


class DeviceJobModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_type: Optional[Literal["OTA", "REBOOT"]] = Field(default=None, alias="JobType")


class StaticIpConnectionInfoModel(BaseModel):
    default_gateway: str = Field(alias="DefaultGateway")
    dns: List[str] = Field(alias="Dns")
    ip_address: str = Field(alias="IpAddress")
    mask: str = Field(alias="Mask")


class EthernetStatusModel(BaseModel):
    connection_status: Optional[
        Literal["CONNECTED", "CONNECTING", "NOT_CONNECTED"]
    ] = Field(default=None, alias="ConnectionStatus")
    hw_address: Optional[str] = Field(default=None, alias="HwAddress")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class ListApplicationInstanceDependenciesRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PackageObjectModel(BaseModel):
    name: str = Field(alias="Name")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")


class ListApplicationInstanceNodeInstancesRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NodeInstanceModel(BaseModel):
    current_status: Literal["ERROR", "NOT_AVAILABLE", "PAUSED", "RUNNING"] = Field(
        alias="CurrentStatus"
    )
    node_instance_id: str = Field(alias="NodeInstanceId")
    node_id: Optional[str] = Field(default=None, alias="NodeId")
    node_name: Optional[str] = Field(default=None, alias="NodeName")
    package_name: Optional[str] = Field(default=None, alias="PackageName")
    package_patch_version: Optional[str] = Field(
        default=None, alias="PackagePatchVersion"
    )
    package_version: Optional[str] = Field(default=None, alias="PackageVersion")


class ListApplicationInstancesRequestModel(BaseModel):
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    status_filter: Optional[
        Literal[
            "DEPLOYMENT_ERROR",
            "DEPLOYMENT_FAILED",
            "DEPLOYMENT_SUCCEEDED",
            "PROCESSING_DEPLOYMENT",
            "PROCESSING_REMOVAL",
            "REMOVAL_FAILED",
            "REMOVAL_SUCCEEDED",
        ]
    ] = Field(default=None, alias="StatusFilter")


class ListDevicesJobsRequestModel(BaseModel):
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDevicesRequestModel(BaseModel):
    device_aggregated_status_filter: Optional[
        Literal[
            "AWAITING_PROVISIONING",
            "DELETING",
            "ERROR",
            "FAILED",
            "LEASE_EXPIRED",
            "OFFLINE",
            "ONLINE",
            "PENDING",
            "REBOOTING",
            "UPDATE_NEEDED",
        ]
    ] = Field(default=None, alias="DeviceAggregatedStatusFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_filter: Optional[str] = Field(default=None, alias="NameFilter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[
        Literal["CREATED_TIME", "DEVICE_AGGREGATED_STATUS", "DEVICE_ID", "NAME"]
    ] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListNodeFromTemplateJobsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NodeFromTemplateJobModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    node_name: Optional[str] = Field(default=None, alias="NodeName")
    status: Optional[Literal["FAILED", "PENDING", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    template_type: Optional[Literal["RTSP_CAMERA_STREAM"]] = Field(
        default=None, alias="TemplateType"
    )


class ListNodesRequestModel(BaseModel):
    category: Optional[
        Literal["BUSINESS_LOGIC", "MEDIA_SINK", "MEDIA_SOURCE", "ML_MODEL"]
    ] = Field(default=None, alias="Category")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    package_name: Optional[str] = Field(default=None, alias="PackageName")
    package_version: Optional[str] = Field(default=None, alias="PackageVersion")
    patch_version: Optional[str] = Field(default=None, alias="PatchVersion")


class NodeModel(BaseModel):
    category: Literal[
        "BUSINESS_LOGIC", "MEDIA_SINK", "MEDIA_SOURCE", "ML_MODEL"
    ] = Field(alias="Category")
    created_time: datetime = Field(alias="CreatedTime")
    name: str = Field(alias="Name")
    node_id: str = Field(alias="NodeId")
    package_id: str = Field(alias="PackageId")
    package_name: str = Field(alias="PackageName")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    package_arn: Optional[str] = Field(default=None, alias="PackageArn")


class ListPackageImportJobsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PackageImportJobModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_type: Optional[
        Literal["MARKETPLACE_NODE_PACKAGE_VERSION", "NODE_PACKAGE_VERSION"]
    ] = Field(default=None, alias="JobType")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    status: Optional[Literal["FAILED", "PENDING", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ListPackagesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PackageListItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    package_id: Optional[str] = Field(default=None, alias="PackageId")
    package_name: Optional[str] = Field(default=None, alias="PackageName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NtpPayloadModel(BaseModel):
    ntp_servers: List[str] = Field(alias="NtpServers")


class NtpStatusModel(BaseModel):
    connection_status: Optional[
        Literal["CONNECTED", "CONNECTING", "NOT_CONNECTED"]
    ] = Field(default=None, alias="ConnectionStatus")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    ntp_server_name: Optional[str] = Field(default=None, alias="NtpServerName")


class NodeInputPortModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    description: Optional[str] = Field(default=None, alias="Description")
    max_connections: Optional[int] = Field(default=None, alias="MaxConnections")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["BOOLEAN", "FLOAT32", "INT32", "MEDIA", "STRING"]] = Field(
        default=None, alias="Type"
    )


class NodeOutputPortModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["BOOLEAN", "FLOAT32", "INT32", "MEDIA", "STRING"]] = Field(
        default=None, alias="Type"
    )


class NodeSignalModel(BaseModel):
    node_instance_id: str = Field(alias="NodeInstanceId")
    signal: Literal["PAUSE", "RESUME"] = Field(alias="Signal")


class OutPutS3LocationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    object_key: str = Field(alias="ObjectKey")


class PackageVersionOutputConfigModel(BaseModel):
    package_name: str = Field(alias="PackageName")
    package_version: str = Field(alias="PackageVersion")
    mark_latest: Optional[bool] = Field(default=None, alias="MarkLatest")


class S3LocationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    object_key: str = Field(alias="ObjectKey")
    region: Optional[str] = Field(default=None, alias="Region")


class RegisterPackageVersionRequestModel(BaseModel):
    package_id: str = Field(alias="PackageId")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")
    mark_latest: Optional[bool] = Field(default=None, alias="MarkLatest")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")


class RemoveApplicationInstanceRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDeviceMetadataRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    description: Optional[str] = Field(default=None, alias="Description")


class ApplicationInstanceModel(BaseModel):
    application_instance_id: Optional[str] = Field(
        default=None, alias="ApplicationInstanceId"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    default_runtime_context_device: Optional[str] = Field(
        default=None, alias="DefaultRuntimeContextDevice"
    )
    default_runtime_context_device_name: Optional[str] = Field(
        default=None, alias="DefaultRuntimeContextDeviceName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    health_status: Optional[Literal["ERROR", "NOT_AVAILABLE", "RUNNING"]] = Field(
        default=None, alias="HealthStatus"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    runtime_context_states: Optional[List[ReportedRuntimeContextStateModel]] = Field(
        default=None, alias="RuntimeContextStates"
    )
    status: Optional[
        Literal[
            "DEPLOYMENT_ERROR",
            "DEPLOYMENT_FAILED",
            "DEPLOYMENT_IN_PROGRESS",
            "DEPLOYMENT_PENDING",
            "DEPLOYMENT_REQUESTED",
            "DEPLOYMENT_SUCCEEDED",
            "REMOVAL_FAILED",
            "REMOVAL_IN_PROGRESS",
            "REMOVAL_PENDING",
            "REMOVAL_REQUESTED",
            "REMOVAL_SUCCEEDED",
        ]
    ] = Field(default=None, alias="Status")
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class CreateApplicationInstanceRequestModel(BaseModel):
    default_runtime_context_device: str = Field(alias="DefaultRuntimeContextDevice")
    manifest_payload: ManifestPayloadModel = Field(alias="ManifestPayload")
    application_instance_id_to_replace: Optional[str] = Field(
        default=None, alias="ApplicationInstanceIdToReplace"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    manifest_overrides_payload: Optional[ManifestOverridesPayloadModel] = Field(
        default=None, alias="ManifestOverridesPayload"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    runtime_role_arn: Optional[str] = Field(default=None, alias="RuntimeRoleArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateApplicationInstanceResponseModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNodeFromTemplateJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePackageImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDeviceResponseModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationInstanceDetailsResponseModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    application_instance_id_to_replace: str = Field(
        alias="ApplicationInstanceIdToReplace"
    )
    created_time: datetime = Field(alias="CreatedTime")
    default_runtime_context_device: str = Field(alias="DefaultRuntimeContextDevice")
    description: str = Field(alias="Description")
    manifest_overrides_payload: ManifestOverridesPayloadModel = Field(
        alias="ManifestOverridesPayload"
    )
    manifest_payload: ManifestPayloadModel = Field(alias="ManifestPayload")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationInstanceResponseModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    application_instance_id_to_replace: str = Field(
        alias="ApplicationInstanceIdToReplace"
    )
    arn: str = Field(alias="Arn")
    created_time: datetime = Field(alias="CreatedTime")
    default_runtime_context_device: str = Field(alias="DefaultRuntimeContextDevice")
    default_runtime_context_device_name: str = Field(
        alias="DefaultRuntimeContextDeviceName"
    )
    description: str = Field(alias="Description")
    health_status: Literal["ERROR", "NOT_AVAILABLE", "RUNNING"] = Field(
        alias="HealthStatus"
    )
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    runtime_context_states: List[ReportedRuntimeContextStateModel] = Field(
        alias="RuntimeContextStates"
    )
    runtime_role_arn: str = Field(alias="RuntimeRoleArn")
    status: Literal[
        "DEPLOYMENT_ERROR",
        "DEPLOYMENT_FAILED",
        "DEPLOYMENT_IN_PROGRESS",
        "DEPLOYMENT_PENDING",
        "DEPLOYMENT_REQUESTED",
        "DEPLOYMENT_SUCCEEDED",
        "REMOVAL_FAILED",
        "REMOVAL_IN_PROGRESS",
        "REMOVAL_PENDING",
        "REMOVAL_REQUESTED",
        "REMOVAL_SUCCEEDED",
    ] = Field(alias="Status")
    status_description: str = Field(alias="StatusDescription")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDeviceJobResponseModel(BaseModel):
    created_time: datetime = Field(alias="CreatedTime")
    device_arn: str = Field(alias="DeviceArn")
    device_id: str = Field(alias="DeviceId")
    device_name: str = Field(alias="DeviceName")
    device_type: Literal[
        "PANORAMA_APPLIANCE", "PANORAMA_APPLIANCE_DEVELOPER_KIT"
    ] = Field(alias="DeviceType")
    image_version: str = Field(alias="ImageVersion")
    job_id: str = Field(alias="JobId")
    job_type: Literal["OTA", "REBOOT"] = Field(alias="JobType")
    status: Literal[
        "COMPLETED",
        "DOWNLOADING",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "REBOOTING",
        "VERIFYING",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackageVersionResponseModel(BaseModel):
    is_latest_patch: bool = Field(alias="IsLatestPatch")
    owner_account: str = Field(alias="OwnerAccount")
    package_arn: str = Field(alias="PackageArn")
    package_id: str = Field(alias="PackageId")
    package_name: str = Field(alias="PackageName")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")
    registered_time: datetime = Field(alias="RegisteredTime")
    status: Literal[
        "DELETING", "FAILED", "REGISTER_COMPLETED", "REGISTER_PENDING"
    ] = Field(alias="Status")
    status_description: str = Field(alias="StatusDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionDeviceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    certificates: bytes = Field(alias="Certificates")
    device_id: str = Field(alias="DeviceId")
    iot_thing_name: str = Field(alias="IotThingName")
    status: Literal[
        "AWAITING_PROVISIONING", "DELETING", "ERROR", "FAILED", "PENDING", "SUCCEEDED"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SignalApplicationInstanceNodeInstancesResponseModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeviceMetadataResponseModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobForDevicesResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNodeFromTemplateJobRequestModel(BaseModel):
    node_name: str = Field(alias="NodeName")
    output_package_name: str = Field(alias="OutputPackageName")
    output_package_version: str = Field(alias="OutputPackageVersion")
    template_parameters: Mapping[str, str] = Field(alias="TemplateParameters")
    template_type: Literal["RTSP_CAMERA_STREAM"] = Field(alias="TemplateType")
    job_tags: Optional[Sequence[JobResourceTagsModel]] = Field(
        default=None, alias="JobTags"
    )
    node_description: Optional[str] = Field(default=None, alias="NodeDescription")


class DescribeNodeFromTemplateJobResponseModel(BaseModel):
    created_time: datetime = Field(alias="CreatedTime")
    job_id: str = Field(alias="JobId")
    job_tags: List[JobResourceTagsModel] = Field(alias="JobTags")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    node_description: str = Field(alias="NodeDescription")
    node_name: str = Field(alias="NodeName")
    output_package_name: str = Field(alias="OutputPackageName")
    output_package_version: str = Field(alias="OutputPackageVersion")
    status: Literal["FAILED", "PENDING", "SUCCEEDED"] = Field(alias="Status")
    status_message: str = Field(alias="StatusMessage")
    template_parameters: Dict[str, str] = Field(alias="TemplateParameters")
    template_type: Literal["RTSP_CAMERA_STREAM"] = Field(alias="TemplateType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePackageResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    package_id: str = Field(alias="PackageId")
    storage_location: StorageLocationModel = Field(alias="StorageLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackageResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_time: datetime = Field(alias="CreatedTime")
    package_id: str = Field(alias="PackageId")
    package_name: str = Field(alias="PackageName")
    read_access_principal_arns: List[str] = Field(alias="ReadAccessPrincipalArns")
    storage_location: StorageLocationModel = Field(alias="StorageLocation")
    tags: Dict[str, str] = Field(alias="Tags")
    write_access_principal_arns: List[str] = Field(alias="WriteAccessPrincipalArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceModel(BaseModel):
    brand: Optional[Literal["AWS_PANORAMA", "LENOVO"]] = Field(
        default=None, alias="Brand"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    current_software: Optional[str] = Field(default=None, alias="CurrentSoftware")
    description: Optional[str] = Field(default=None, alias="Description")
    device_aggregated_status: Optional[
        Literal[
            "AWAITING_PROVISIONING",
            "DELETING",
            "ERROR",
            "FAILED",
            "LEASE_EXPIRED",
            "OFFLINE",
            "ONLINE",
            "PENDING",
            "REBOOTING",
            "UPDATE_NEEDED",
        ]
    ] = Field(default=None, alias="DeviceAggregatedStatus")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    latest_device_job: Optional[LatestDeviceJobModel] = Field(
        default=None, alias="LatestDeviceJob"
    )
    lease_expiration_time: Optional[datetime] = Field(
        default=None, alias="LeaseExpirationTime"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    provisioning_status: Optional[
        Literal[
            "AWAITING_PROVISIONING",
            "DELETING",
            "ERROR",
            "FAILED",
            "PENDING",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="ProvisioningStatus")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    type: Optional[
        Literal["PANORAMA_APPLIANCE", "PANORAMA_APPLIANCE_DEVELOPER_KIT"]
    ] = Field(default=None, alias="Type")


class DeviceJobConfigModel(BaseModel):
    otajob_config: Optional[OTAJobConfigModel] = Field(
        default=None, alias="OTAJobConfig"
    )


class ListDevicesJobsResponseModel(BaseModel):
    device_jobs: List[DeviceJobModel] = Field(alias="DeviceJobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EthernetPayloadModel(BaseModel):
    connection_type: Literal["DHCP", "STATIC_IP"] = Field(alias="ConnectionType")
    static_ip_connection_info: Optional[StaticIpConnectionInfoModel] = Field(
        default=None, alias="StaticIpConnectionInfo"
    )


class ListApplicationInstanceDependenciesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    package_objects: List[PackageObjectModel] = Field(alias="PackageObjects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationInstanceNodeInstancesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    node_instances: List[NodeInstanceModel] = Field(alias="NodeInstances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNodeFromTemplateJobsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    node_from_template_jobs: List[NodeFromTemplateJobModel] = Field(
        alias="NodeFromTemplateJobs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNodesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    nodes: List[NodeModel] = Field(alias="Nodes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackageImportJobsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    package_import_jobs: List[PackageImportJobModel] = Field(alias="PackageImportJobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackagesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    packages: List[PackageListItemModel] = Field(alias="Packages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkStatusModel(BaseModel):
    ethernet0_status: Optional[EthernetStatusModel] = Field(
        default=None, alias="Ethernet0Status"
    )
    ethernet1_status: Optional[EthernetStatusModel] = Field(
        default=None, alias="Ethernet1Status"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    ntp_status: Optional[NtpStatusModel] = Field(default=None, alias="NtpStatus")


class NodeInterfaceModel(BaseModel):
    inputs: List[NodeInputPortModel] = Field(alias="Inputs")
    outputs: List[NodeOutputPortModel] = Field(alias="Outputs")


class SignalApplicationInstanceNodeInstancesRequestModel(BaseModel):
    application_instance_id: str = Field(alias="ApplicationInstanceId")
    node_signals: Sequence[NodeSignalModel] = Field(alias="NodeSignals")


class PackageImportJobOutputModel(BaseModel):
    output_s3_location: OutPutS3LocationModel = Field(alias="OutputS3Location")
    package_id: str = Field(alias="PackageId")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")


class PackageImportJobOutputConfigModel(BaseModel):
    package_version_output_config: Optional[PackageVersionOutputConfigModel] = Field(
        default=None, alias="PackageVersionOutputConfig"
    )


class PackageVersionInputConfigModel(BaseModel):
    s3_location: S3LocationModel = Field(alias="S3Location")


class ListApplicationInstancesResponseModel(BaseModel):
    application_instances: List[ApplicationInstanceModel] = Field(
        alias="ApplicationInstances"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesResponseModel(BaseModel):
    devices: List[DeviceModel] = Field(alias="Devices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobForDevicesRequestModel(BaseModel):
    device_ids: Sequence[str] = Field(alias="DeviceIds")
    job_type: Literal["OTA", "REBOOT"] = Field(alias="JobType")
    device_job_config: Optional[DeviceJobConfigModel] = Field(
        default=None, alias="DeviceJobConfig"
    )


class NetworkPayloadModel(BaseModel):
    ethernet0: Optional[EthernetPayloadModel] = Field(default=None, alias="Ethernet0")
    ethernet1: Optional[EthernetPayloadModel] = Field(default=None, alias="Ethernet1")
    ntp: Optional[NtpPayloadModel] = Field(default=None, alias="Ntp")


class DescribeNodeResponseModel(BaseModel):
    asset_name: str = Field(alias="AssetName")
    category: Literal[
        "BUSINESS_LOGIC", "MEDIA_SINK", "MEDIA_SOURCE", "ML_MODEL"
    ] = Field(alias="Category")
    created_time: datetime = Field(alias="CreatedTime")
    description: str = Field(alias="Description")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    node_id: str = Field(alias="NodeId")
    node_interface: NodeInterfaceModel = Field(alias="NodeInterface")
    owner_account: str = Field(alias="OwnerAccount")
    package_arn: str = Field(alias="PackageArn")
    package_id: str = Field(alias="PackageId")
    package_name: str = Field(alias="PackageName")
    package_version: str = Field(alias="PackageVersion")
    patch_version: str = Field(alias="PatchVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PackageImportJobInputConfigModel(BaseModel):
    package_version_input_config: Optional[PackageVersionInputConfigModel] = Field(
        default=None, alias="PackageVersionInputConfig"
    )


class DescribeDeviceResponseModel(BaseModel):
    alternate_softwares: List[AlternateSoftwareMetadataModel] = Field(
        alias="AlternateSoftwares"
    )
    arn: str = Field(alias="Arn")
    brand: Literal["AWS_PANORAMA", "LENOVO"] = Field(alias="Brand")
    created_time: datetime = Field(alias="CreatedTime")
    current_networking_status: NetworkStatusModel = Field(
        alias="CurrentNetworkingStatus"
    )
    current_software: str = Field(alias="CurrentSoftware")
    description: str = Field(alias="Description")
    device_aggregated_status: Literal[
        "AWAITING_PROVISIONING",
        "DELETING",
        "ERROR",
        "FAILED",
        "LEASE_EXPIRED",
        "OFFLINE",
        "ONLINE",
        "PENDING",
        "REBOOTING",
        "UPDATE_NEEDED",
    ] = Field(alias="DeviceAggregatedStatus")
    device_connection_status: Literal[
        "AWAITING_CREDENTIALS", "ERROR", "NOT_AVAILABLE", "OFFLINE", "ONLINE"
    ] = Field(alias="DeviceConnectionStatus")
    device_id: str = Field(alias="DeviceId")
    latest_alternate_software: str = Field(alias="LatestAlternateSoftware")
    latest_device_job: LatestDeviceJobModel = Field(alias="LatestDeviceJob")
    latest_software: str = Field(alias="LatestSoftware")
    lease_expiration_time: datetime = Field(alias="LeaseExpirationTime")
    name: str = Field(alias="Name")
    networking_configuration: NetworkPayloadModel = Field(
        alias="NetworkingConfiguration"
    )
    provisioning_status: Literal[
        "AWAITING_PROVISIONING", "DELETING", "ERROR", "FAILED", "PENDING", "SUCCEEDED"
    ] = Field(alias="ProvisioningStatus")
    serial_number: str = Field(alias="SerialNumber")
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal["PANORAMA_APPLIANCE", "PANORAMA_APPLIANCE_DEVELOPER_KIT"] = Field(
        alias="Type"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionDeviceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    networking_configuration: Optional[NetworkPayloadModel] = Field(
        default=None, alias="NetworkingConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreatePackageImportJobRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    input_config: PackageImportJobInputConfigModel = Field(alias="InputConfig")
    job_type: Literal[
        "MARKETPLACE_NODE_PACKAGE_VERSION", "NODE_PACKAGE_VERSION"
    ] = Field(alias="JobType")
    output_config: PackageImportJobOutputConfigModel = Field(alias="OutputConfig")
    job_tags: Optional[Sequence[JobResourceTagsModel]] = Field(
        default=None, alias="JobTags"
    )


class DescribePackageImportJobResponseModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    created_time: datetime = Field(alias="CreatedTime")
    input_config: PackageImportJobInputConfigModel = Field(alias="InputConfig")
    job_id: str = Field(alias="JobId")
    job_tags: List[JobResourceTagsModel] = Field(alias="JobTags")
    job_type: Literal[
        "MARKETPLACE_NODE_PACKAGE_VERSION", "NODE_PACKAGE_VERSION"
    ] = Field(alias="JobType")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    output: PackageImportJobOutputModel = Field(alias="Output")
    output_config: PackageImportJobOutputConfigModel = Field(alias="OutputConfig")
    status: Literal["FAILED", "PENDING", "SUCCEEDED"] = Field(alias="Status")
    status_message: str = Field(alias="StatusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
