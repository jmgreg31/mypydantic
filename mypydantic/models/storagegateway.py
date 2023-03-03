# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddCacheInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: Sequence[str] = Field(alias="DiskIds")


class AddUploadBufferInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: Sequence[str] = Field(alias="DiskIds")


class AddWorkingStorageInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: Sequence[str] = Field(alias="DiskIds")


class AssignTapePoolInputRequestModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    pool_id: str = Field(alias="PoolId")
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )


class CacheAttributesModel(BaseModel):
    cache_stale_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="CacheStaleTimeoutInSeconds"
    )


class EndpointNetworkConfigurationModel(BaseModel):
    ip_addresses: Optional[Sequence[str]] = Field(default=None, alias="IpAddresses")


class AttachVolumeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    volume_arn: str = Field(alias="VolumeARN")
    network_interface_id: str = Field(alias="NetworkInterfaceId")
    target_name: Optional[str] = Field(default=None, alias="TargetName")
    disk_id: Optional[str] = Field(default=None, alias="DiskId")


class AutomaticTapeCreationRuleModel(BaseModel):
    tape_barcode_prefix: str = Field(alias="TapeBarcodePrefix")
    pool_id: str = Field(alias="PoolId")
    tape_size_in_bytes: int = Field(alias="TapeSizeInBytes")
    minimum_num_tapes: int = Field(alias="MinimumNumTapes")
    worm: Optional[bool] = Field(default=None, alias="Worm")


class BandwidthRateLimitIntervalModel(BaseModel):
    start_hour_of_day: int = Field(alias="StartHourOfDay")
    start_minute_of_hour: int = Field(alias="StartMinuteOfHour")
    end_hour_of_day: int = Field(alias="EndHourOfDay")
    end_minute_of_hour: int = Field(alias="EndMinuteOfHour")
    days_of_week: List[int] = Field(alias="DaysOfWeek")
    average_upload_rate_limit_in_bits_per_sec: Optional[int] = Field(
        default=None, alias="AverageUploadRateLimitInBitsPerSec"
    )
    average_download_rate_limit_in_bits_per_sec: Optional[int] = Field(
        default=None, alias="AverageDownloadRateLimitInBitsPerSec"
    )


class VolumeiSCSIAttributesModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetARN")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    network_interface_port: Optional[int] = Field(
        default=None, alias="NetworkInterfacePort"
    )
    lun_number: Optional[int] = Field(default=None, alias="LunNumber")
    chap_enabled: Optional[bool] = Field(default=None, alias="ChapEnabled")


class CancelArchivalInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_arn: str = Field(alias="TapeARN")


class CancelRetrievalInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_arn: str = Field(alias="TapeARN")


class ChapInfoModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetARN")
    secret_to_authenticate_initiator: Optional[str] = Field(
        default=None, alias="SecretToAuthenticateInitiator"
    )
    initiator_name: Optional[str] = Field(default=None, alias="InitiatorName")
    secret_to_authenticate_target: Optional[str] = Field(
        default=None, alias="SecretToAuthenticateTarget"
    )


class NFSFileShareDefaultsModel(BaseModel):
    file_mode: Optional[str] = Field(default=None, alias="FileMode")
    directory_mode: Optional[str] = Field(default=None, alias="DirectoryMode")
    group_id: Optional[int] = Field(default=None, alias="GroupId")
    owner_id: Optional[int] = Field(default=None, alias="OwnerId")


class DeleteAutomaticTapeCreationPolicyInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DeleteBandwidthRateLimitInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    bandwidth_type: str = Field(alias="BandwidthType")


class DeleteChapCredentialsInputRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetARN")
    initiator_name: str = Field(alias="InitiatorName")


class DeleteFileShareInputRequestModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    force_delete: Optional[bool] = Field(default=None, alias="ForceDelete")


class DeleteGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DeleteSnapshotScheduleInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")


class DeleteTapeArchiveInputRequestModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )


class DeleteTapeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_arn: str = Field(alias="TapeARN")
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )


class DeleteTapePoolInputRequestModel(BaseModel):
    pool_arn: str = Field(alias="PoolARN")


class DeleteVolumeInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")


class DescribeAvailabilityMonitorTestInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeBandwidthRateLimitInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeBandwidthRateLimitScheduleInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeCacheInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeCachediSCSIVolumesInputRequestModel(BaseModel):
    volume_arns: Sequence[str] = Field(alias="VolumeARNs")


class DescribeChapCredentialsInputRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetARN")


class DescribeFileSystemAssociationsInputRequestModel(BaseModel):
    file_system_association_arnlist: Sequence[str] = Field(
        alias="FileSystemAssociationARNList"
    )


class DescribeGatewayInformationInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class NetworkInterfaceModel(BaseModel):
    ipv4_address: Optional[str] = Field(default=None, alias="Ipv4Address")
    mac_address: Optional[str] = Field(default=None, alias="MacAddress")
    ipv6_address: Optional[str] = Field(default=None, alias="Ipv6Address")


class DescribeMaintenanceStartTimeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeNFSFileSharesInputRequestModel(BaseModel):
    file_share_arnlist: Sequence[str] = Field(alias="FileShareARNList")


class DescribeSMBFileSharesInputRequestModel(BaseModel):
    file_share_arnlist: Sequence[str] = Field(alias="FileShareARNList")


class DescribeSMBSettingsInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class SMBLocalGroupsModel(BaseModel):
    gateway_admins: Optional[List[str]] = Field(default=None, alias="GatewayAdmins")


class DescribeSnapshotScheduleInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")


class DescribeStorediSCSIVolumesInputRequestModel(BaseModel):
    volume_arns: Sequence[str] = Field(alias="VolumeARNs")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeTapeArchivesInputRequestModel(BaseModel):
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class TapeArchiveModel(BaseModel):
    tape_arn: Optional[str] = Field(default=None, alias="TapeARN")
    tape_barcode: Optional[str] = Field(default=None, alias="TapeBarcode")
    tape_created_date: Optional[datetime] = Field(default=None, alias="TapeCreatedDate")
    tape_size_in_bytes: Optional[int] = Field(default=None, alias="TapeSizeInBytes")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    retrieved_to: Optional[str] = Field(default=None, alias="RetrievedTo")
    tape_status: Optional[str] = Field(default=None, alias="TapeStatus")
    tape_used_in_bytes: Optional[int] = Field(default=None, alias="TapeUsedInBytes")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    worm: Optional[bool] = Field(default=None, alias="Worm")
    retention_start_date: Optional[datetime] = Field(
        default=None, alias="RetentionStartDate"
    )
    pool_entry_date: Optional[datetime] = Field(default=None, alias="PoolEntryDate")


class DescribeTapeRecoveryPointsInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class TapeRecoveryPointInfoModel(BaseModel):
    tape_arn: Optional[str] = Field(default=None, alias="TapeARN")
    tape_recovery_point_time: Optional[datetime] = Field(
        default=None, alias="TapeRecoveryPointTime"
    )
    tape_size_in_bytes: Optional[int] = Field(default=None, alias="TapeSizeInBytes")
    tape_status: Optional[str] = Field(default=None, alias="TapeStatus")


class DescribeTapesInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class TapeModel(BaseModel):
    tape_arn: Optional[str] = Field(default=None, alias="TapeARN")
    tape_barcode: Optional[str] = Field(default=None, alias="TapeBarcode")
    tape_created_date: Optional[datetime] = Field(default=None, alias="TapeCreatedDate")
    tape_size_in_bytes: Optional[int] = Field(default=None, alias="TapeSizeInBytes")
    tape_status: Optional[str] = Field(default=None, alias="TapeStatus")
    vtl_device: Optional[str] = Field(default=None, alias="VTLDevice")
    progress: Optional[float] = Field(default=None, alias="Progress")
    tape_used_in_bytes: Optional[int] = Field(default=None, alias="TapeUsedInBytes")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    worm: Optional[bool] = Field(default=None, alias="Worm")
    retention_start_date: Optional[datetime] = Field(
        default=None, alias="RetentionStartDate"
    )
    pool_entry_date: Optional[datetime] = Field(default=None, alias="PoolEntryDate")


class DescribeUploadBufferInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeVTLDevicesInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    vtl_device_arns: Optional[Sequence[str]] = Field(
        default=None, alias="VTLDeviceARNs"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeWorkingStorageInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DetachVolumeInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    force_detach: Optional[bool] = Field(default=None, alias="ForceDetach")


class DeviceiSCSIAttributesModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetARN")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    network_interface_port: Optional[int] = Field(
        default=None, alias="NetworkInterfacePort"
    )
    chap_enabled: Optional[bool] = Field(default=None, alias="ChapEnabled")


class DisableGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class DisassociateFileSystemInputRequestModel(BaseModel):
    file_system_association_arn: str = Field(alias="FileSystemAssociationARN")
    force_delete: Optional[bool] = Field(default=None, alias="ForceDelete")


class DiskModel(BaseModel):
    disk_id: Optional[str] = Field(default=None, alias="DiskId")
    disk_path: Optional[str] = Field(default=None, alias="DiskPath")
    disk_node: Optional[str] = Field(default=None, alias="DiskNode")
    disk_status: Optional[str] = Field(default=None, alias="DiskStatus")
    disk_size_in_bytes: Optional[int] = Field(default=None, alias="DiskSizeInBytes")
    disk_allocation_type: Optional[str] = Field(
        default=None, alias="DiskAllocationType"
    )
    disk_allocation_resource: Optional[str] = Field(
        default=None, alias="DiskAllocationResource"
    )
    disk_attribute_list: Optional[List[str]] = Field(
        default=None, alias="DiskAttributeList"
    )


class FileShareInfoModel(BaseModel):
    file_share_type: Optional[Literal["NFS", "SMB"]] = Field(
        default=None, alias="FileShareType"
    )
    file_share_arn: Optional[str] = Field(default=None, alias="FileShareARN")
    file_share_id: Optional[str] = Field(default=None, alias="FileShareId")
    file_share_status: Optional[str] = Field(default=None, alias="FileShareStatus")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")


class FileSystemAssociationStatusDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")


class FileSystemAssociationSummaryModel(BaseModel):
    file_system_association_id: Optional[str] = Field(
        default=None, alias="FileSystemAssociationId"
    )
    file_system_association_arn: Optional[str] = Field(
        default=None, alias="FileSystemAssociationARN"
    )
    file_system_association_status: Optional[str] = Field(
        default=None, alias="FileSystemAssociationStatus"
    )
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")


class GatewayInfoModel(BaseModel):
    gateway_id: Optional[str] = Field(default=None, alias="GatewayId")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    gateway_type: Optional[str] = Field(default=None, alias="GatewayType")
    gateway_operational_state: Optional[str] = Field(
        default=None, alias="GatewayOperationalState"
    )
    gateway_name: Optional[str] = Field(default=None, alias="GatewayName")
    ec2_instance_id: Optional[str] = Field(default=None, alias="Ec2InstanceId")
    ec2_instance_region: Optional[str] = Field(default=None, alias="Ec2InstanceRegion")
    host_environment: Optional[
        Literal["EC2", "HYPER-V", "KVM", "OTHER", "SNOWBALL", "VMWARE"]
    ] = Field(default=None, alias="HostEnvironment")
    host_environment_id: Optional[str] = Field(default=None, alias="HostEnvironmentId")


class JoinDomainInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    domain_name: str = Field(alias="DomainName")
    user_name: str = Field(alias="UserName")
    password: str = Field(alias="Password")
    organizational_unit: Optional[str] = Field(default=None, alias="OrganizationalUnit")
    domain_controllers: Optional[Sequence[str]] = Field(
        default=None, alias="DomainControllers"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")


class ListAutomaticTapeCreationPoliciesInputRequestModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")


class ListFileSharesInputRequestModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListFileSystemAssociationsInputRequestModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListGatewaysInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListLocalDisksInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListTapePoolsInputRequestModel(BaseModel):
    pool_arns: Optional[Sequence[str]] = Field(default=None, alias="PoolARNs")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class PoolInfoModel(BaseModel):
    pool_arn: Optional[str] = Field(default=None, alias="PoolARN")
    pool_name: Optional[str] = Field(default=None, alias="PoolName")
    storage_class: Optional[Literal["DEEP_ARCHIVE", "GLACIER"]] = Field(
        default=None, alias="StorageClass"
    )
    retention_lock_type: Optional[Literal["COMPLIANCE", "GOVERNANCE", "NONE"]] = Field(
        default=None, alias="RetentionLockType"
    )
    retention_lock_time_in_days: Optional[int] = Field(
        default=None, alias="RetentionLockTimeInDays"
    )
    pool_status: Optional[Literal["ACTIVE", "DELETED"]] = Field(
        default=None, alias="PoolStatus"
    )


class ListTapesInputRequestModel(BaseModel):
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class TapeInfoModel(BaseModel):
    tape_arn: Optional[str] = Field(default=None, alias="TapeARN")
    tape_barcode: Optional[str] = Field(default=None, alias="TapeBarcode")
    tape_size_in_bytes: Optional[int] = Field(default=None, alias="TapeSizeInBytes")
    tape_status: Optional[str] = Field(default=None, alias="TapeStatus")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    retention_start_date: Optional[datetime] = Field(
        default=None, alias="RetentionStartDate"
    )
    pool_entry_date: Optional[datetime] = Field(default=None, alias="PoolEntryDate")


class ListVolumeInitiatorsInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")


class ListVolumeRecoveryPointsInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class VolumeRecoveryPointInfoModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="VolumeARN")
    volume_size_in_bytes: Optional[int] = Field(default=None, alias="VolumeSizeInBytes")
    volume_usage_in_bytes: Optional[int] = Field(
        default=None, alias="VolumeUsageInBytes"
    )
    volume_recovery_point_time: Optional[str] = Field(
        default=None, alias="VolumeRecoveryPointTime"
    )


class ListVolumesInputRequestModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class VolumeInfoModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="VolumeARN")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    gateway_id: Optional[str] = Field(default=None, alias="GatewayId")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    volume_size_in_bytes: Optional[int] = Field(default=None, alias="VolumeSizeInBytes")
    volume_attachment_status: Optional[str] = Field(
        default=None, alias="VolumeAttachmentStatus"
    )


class NotifyWhenUploadedInputRequestModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")


class RefreshCacheInputRequestModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    folder_list: Optional[Sequence[str]] = Field(default=None, alias="FolderList")
    recursive: Optional[bool] = Field(default=None, alias="Recursive")


class RemoveTagsFromResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ResetCacheInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class RetrieveTapeArchiveInputRequestModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    gateway_arn: str = Field(alias="GatewayARN")


class RetrieveTapeRecoveryPointInputRequestModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    gateway_arn: str = Field(alias="GatewayARN")


class SetLocalConsolePasswordInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    local_console_password: str = Field(alias="LocalConsolePassword")


class SetSMBGuestPasswordInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    password: str = Field(alias="Password")


class ShutdownGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class StartAvailabilityMonitorTestInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class StartGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class UpdateBandwidthRateLimitInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    average_upload_rate_limit_in_bits_per_sec: Optional[int] = Field(
        default=None, alias="AverageUploadRateLimitInBitsPerSec"
    )
    average_download_rate_limit_in_bits_per_sec: Optional[int] = Field(
        default=None, alias="AverageDownloadRateLimitInBitsPerSec"
    )


class UpdateChapCredentialsInputRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetARN")
    secret_to_authenticate_initiator: str = Field(alias="SecretToAuthenticateInitiator")
    initiator_name: str = Field(alias="InitiatorName")
    secret_to_authenticate_target: Optional[str] = Field(
        default=None, alias="SecretToAuthenticateTarget"
    )


class UpdateGatewayInformationInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    gateway_name: Optional[str] = Field(default=None, alias="GatewayName")
    gateway_timezone: Optional[str] = Field(default=None, alias="GatewayTimezone")
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupARN"
    )
    gateway_capacity: Optional[Literal["Large", "Medium", "Small"]] = Field(
        default=None, alias="GatewayCapacity"
    )


class UpdateGatewaySoftwareNowInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")


class UpdateMaintenanceStartTimeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    hour_of_day: int = Field(alias="HourOfDay")
    minute_of_hour: int = Field(alias="MinuteOfHour")
    day_of_week: Optional[int] = Field(default=None, alias="DayOfWeek")
    day_of_month: Optional[int] = Field(default=None, alias="DayOfMonth")


class UpdateSMBFileShareVisibilityInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    file_shares_visible: bool = Field(alias="FileSharesVisible")


class UpdateSMBSecurityStrategyInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    s_mbsecurity_strategy: Literal[
        "ClientSpecified", "MandatoryEncryption", "MandatorySigning"
    ] = Field(alias="SMBSecurityStrategy")


class UpdateVTLDeviceTypeInputRequestModel(BaseModel):
    vtl_device_arn: str = Field(alias="VTLDeviceARN")
    device_type: str = Field(alias="DeviceType")


class ActivateGatewayInputRequestModel(BaseModel):
    activation_key: str = Field(alias="ActivationKey")
    gateway_name: str = Field(alias="GatewayName")
    gateway_timezone: str = Field(alias="GatewayTimezone")
    gateway_region: str = Field(alias="GatewayRegion")
    gateway_type: Optional[str] = Field(default=None, alias="GatewayType")
    tape_drive_type: Optional[str] = Field(default=None, alias="TapeDriveType")
    medium_changer_type: Optional[str] = Field(default=None, alias="MediumChangerType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class AddTagsToResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateCachediSCSIVolumeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    volume_size_in_bytes: int = Field(alias="VolumeSizeInBytes")
    target_name: str = Field(alias="TargetName")
    network_interface_id: str = Field(alias="NetworkInterfaceId")
    client_token: str = Field(alias="ClientToken")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    source_volume_arn: Optional[str] = Field(default=None, alias="SourceVolumeARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotFromVolumeRecoveryPointInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    snapshot_description: str = Field(alias="SnapshotDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSnapshotInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    snapshot_description: str = Field(alias="SnapshotDescription")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateStorediSCSIVolumeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_id: str = Field(alias="DiskId")
    preserve_existing_data: bool = Field(alias="PreserveExistingData")
    target_name: str = Field(alias="TargetName")
    network_interface_id: str = Field(alias="NetworkInterfaceId")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTapePoolInputRequestModel(BaseModel):
    pool_name: str = Field(alias="PoolName")
    storage_class: Literal["DEEP_ARCHIVE", "GLACIER"] = Field(alias="StorageClass")
    retention_lock_type: Optional[Literal["COMPLIANCE", "GOVERNANCE", "NONE"]] = Field(
        default=None, alias="RetentionLockType"
    )
    retention_lock_time_in_days: Optional[int] = Field(
        default=None, alias="RetentionLockTimeInDays"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTapeWithBarcodeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_size_in_bytes: int = Field(alias="TapeSizeInBytes")
    tape_barcode: str = Field(alias="TapeBarcode")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    worm: Optional[bool] = Field(default=None, alias="Worm")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateTapesInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_size_in_bytes: int = Field(alias="TapeSizeInBytes")
    client_token: str = Field(alias="ClientToken")
    num_tapes_to_create: int = Field(alias="NumTapesToCreate")
    tape_barcode_prefix: str = Field(alias="TapeBarcodePrefix")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    worm: Optional[bool] = Field(default=None, alias="Worm")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateSnapshotScheduleInputRequestModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    start_at: int = Field(alias="StartAt")
    recurrence_in_hours: int = Field(alias="RecurrenceInHours")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ActivateGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddCacheOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsToResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddUploadBufferOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddWorkingStorageOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssignTapePoolOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateFileSystemOutputModel(BaseModel):
    file_system_association_arn: str = Field(alias="FileSystemAssociationARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachVolumeOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    target_arn: str = Field(alias="TargetARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelArchivalOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelRetrievalOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCachediSCSIVolumeOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    target_arn: str = Field(alias="TargetARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNFSFileShareOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSMBFileShareOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotFromVolumeRecoveryPointOutputModel(BaseModel):
    snapshot_id: str = Field(alias="SnapshotId")
    volume_arn: str = Field(alias="VolumeARN")
    volume_recovery_point_time: str = Field(alias="VolumeRecoveryPointTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSnapshotOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    snapshot_id: str = Field(alias="SnapshotId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStorediSCSIVolumeOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    volume_size_in_bytes: int = Field(alias="VolumeSizeInBytes")
    target_arn: str = Field(alias="TargetARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTapePoolOutputModel(BaseModel):
    pool_arn: str = Field(alias="PoolARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTapeWithBarcodeOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTapesOutputModel(BaseModel):
    tape_arns: List[str] = Field(alias="TapeARNs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAutomaticTapeCreationPolicyOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBandwidthRateLimitOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteChapCredentialsOutputModel(BaseModel):
    target_arn: str = Field(alias="TargetARN")
    initiator_name: str = Field(alias="InitiatorName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFileShareOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSnapshotScheduleOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTapeArchiveOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTapeOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTapePoolOutputModel(BaseModel):
    pool_arn: str = Field(alias="PoolARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVolumeOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAvailabilityMonitorTestOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    status: Literal["COMPLETE", "FAILED", "PENDING"] = Field(alias="Status")
    start_time: datetime = Field(alias="StartTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBandwidthRateLimitOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    average_upload_rate_limit_in_bits_per_sec: int = Field(
        alias="AverageUploadRateLimitInBitsPerSec"
    )
    average_download_rate_limit_in_bits_per_sec: int = Field(
        alias="AverageDownloadRateLimitInBitsPerSec"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCacheOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: List[str] = Field(alias="DiskIds")
    cache_allocated_in_bytes: int = Field(alias="CacheAllocatedInBytes")
    cache_used_percentage: float = Field(alias="CacheUsedPercentage")
    cache_dirty_percentage: float = Field(alias="CacheDirtyPercentage")
    cache_hit_percentage: float = Field(alias="CacheHitPercentage")
    cache_miss_percentage: float = Field(alias="CacheMissPercentage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMaintenanceStartTimeOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    hour_of_day: int = Field(alias="HourOfDay")
    minute_of_hour: int = Field(alias="MinuteOfHour")
    day_of_week: int = Field(alias="DayOfWeek")
    day_of_month: int = Field(alias="DayOfMonth")
    timezone: str = Field(alias="Timezone")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSnapshotScheduleOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    start_at: int = Field(alias="StartAt")
    recurrence_in_hours: int = Field(alias="RecurrenceInHours")
    description: str = Field(alias="Description")
    timezone: str = Field(alias="Timezone")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUploadBufferOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: List[str] = Field(alias="DiskIds")
    upload_buffer_used_in_bytes: int = Field(alias="UploadBufferUsedInBytes")
    upload_buffer_allocated_in_bytes: int = Field(alias="UploadBufferAllocatedInBytes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkingStorageOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disk_ids: List[str] = Field(alias="DiskIds")
    working_storage_used_in_bytes: int = Field(alias="WorkingStorageUsedInBytes")
    working_storage_allocated_in_bytes: int = Field(
        alias="WorkingStorageAllocatedInBytes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachVolumeOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateFileSystemOutputModel(BaseModel):
    file_system_association_arn: str = Field(alias="FileSystemAssociationARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JoinDomainOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    active_directory_status: Literal[
        "ACCESS_DENIED",
        "DETACHED",
        "JOINED",
        "JOINING",
        "NETWORK_ERROR",
        "TIMEOUT",
        "UNKNOWN_ERROR",
    ] = Field(alias="ActiveDirectoryStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    marker: str = Field(alias="Marker")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVolumeInitiatorsOutputModel(BaseModel):
    initiators: List[str] = Field(alias="Initiators")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotifyWhenUploadedOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    notification_id: str = Field(alias="NotificationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RefreshCacheOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    notification_id: str = Field(alias="NotificationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveTagsFromResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetCacheOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetrieveTapeArchiveOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetrieveTapeRecoveryPointOutputModel(BaseModel):
    tape_arn: str = Field(alias="TapeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetLocalConsolePasswordOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetSMBGuestPasswordOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ShutdownGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAvailabilityMonitorTestOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAutomaticTapeCreationPolicyOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBandwidthRateLimitOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBandwidthRateLimitScheduleOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChapCredentialsOutputModel(BaseModel):
    target_arn: str = Field(alias="TargetARN")
    initiator_name: str = Field(alias="InitiatorName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFileSystemAssociationOutputModel(BaseModel):
    file_system_association_arn: str = Field(alias="FileSystemAssociationARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewayInformationOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    gateway_name: str = Field(alias="GatewayName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewaySoftwareNowOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMaintenanceStartTimeOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNFSFileShareOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSMBFileShareOutputModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSMBFileShareVisibilityOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSMBLocalGroupsOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSMBSecurityStrategyOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSnapshotScheduleOutputModel(BaseModel):
    volume_arn: str = Field(alias="VolumeARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVTLDeviceTypeOutputModel(BaseModel):
    vtl_device_arn: str = Field(alias="VTLDeviceARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSMBFileShareInputRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    gateway_arn: str = Field(alias="GatewayARN")
    role: str = Field(alias="Role")
    location_arn: str = Field(alias="LocationARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    s_mbacl_enabled: Optional[bool] = Field(default=None, alias="SMBACLEnabled")
    access_based_enumeration: Optional[bool] = Field(
        default=None, alias="AccessBasedEnumeration"
    )
    admin_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="AdminUserList"
    )
    valid_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="ValidUserList"
    )
    invalid_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="InvalidUserList"
    )
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    authentication: Optional[str] = Field(default=None, alias="Authentication")
    case_sensitivity: Optional[Literal["CaseSensitive", "ClientSpecified"]] = Field(
        default=None, alias="CaseSensitivity"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    vp_cendpoint_dns_name: Optional[str] = Field(
        default=None, alias="VPCEndpointDNSName"
    )
    bucket_region: Optional[str] = Field(default=None, alias="BucketRegion")
    oplocks_enabled: Optional[bool] = Field(default=None, alias="OplocksEnabled")


class SMBFileShareInfoModel(BaseModel):
    file_share_arn: Optional[str] = Field(default=None, alias="FileShareARN")
    file_share_id: Optional[str] = Field(default=None, alias="FileShareId")
    file_share_status: Optional[str] = Field(default=None, alias="FileShareStatus")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    path: Optional[str] = Field(default=None, alias="Path")
    role: Optional[str] = Field(default=None, alias="Role")
    location_arn: Optional[str] = Field(default=None, alias="LocationARN")
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    s_mbacl_enabled: Optional[bool] = Field(default=None, alias="SMBACLEnabled")
    access_based_enumeration: Optional[bool] = Field(
        default=None, alias="AccessBasedEnumeration"
    )
    admin_user_list: Optional[List[str]] = Field(default=None, alias="AdminUserList")
    valid_user_list: Optional[List[str]] = Field(default=None, alias="ValidUserList")
    invalid_user_list: Optional[List[str]] = Field(
        default=None, alias="InvalidUserList"
    )
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    authentication: Optional[str] = Field(default=None, alias="Authentication")
    case_sensitivity: Optional[Literal["CaseSensitive", "ClientSpecified"]] = Field(
        default=None, alias="CaseSensitivity"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    vp_cendpoint_dns_name: Optional[str] = Field(
        default=None, alias="VPCEndpointDNSName"
    )
    bucket_region: Optional[str] = Field(default=None, alias="BucketRegion")
    oplocks_enabled: Optional[bool] = Field(default=None, alias="OplocksEnabled")


class UpdateFileSystemAssociationInputRequestModel(BaseModel):
    file_system_association_arn: str = Field(alias="FileSystemAssociationARN")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    password: Optional[str] = Field(default=None, alias="Password")
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )


class UpdateSMBFileShareInputRequestModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    s_mbacl_enabled: Optional[bool] = Field(default=None, alias="SMBACLEnabled")
    access_based_enumeration: Optional[bool] = Field(
        default=None, alias="AccessBasedEnumeration"
    )
    admin_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="AdminUserList"
    )
    valid_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="ValidUserList"
    )
    invalid_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="InvalidUserList"
    )
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    case_sensitivity: Optional[Literal["CaseSensitive", "ClientSpecified"]] = Field(
        default=None, alias="CaseSensitivity"
    )
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    oplocks_enabled: Optional[bool] = Field(default=None, alias="OplocksEnabled")


class AssociateFileSystemInputRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    password: str = Field(alias="Password")
    client_token: str = Field(alias="ClientToken")
    gateway_arn: str = Field(alias="GatewayARN")
    location_arn: str = Field(alias="LocationARN")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    endpoint_network_configuration: Optional[EndpointNetworkConfigurationModel] = Field(
        default=None, alias="EndpointNetworkConfiguration"
    )


class AutomaticTapeCreationPolicyInfoModel(BaseModel):
    automatic_tape_creation_rules: Optional[
        List[AutomaticTapeCreationRuleModel]
    ] = Field(default=None, alias="AutomaticTapeCreationRules")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")


class UpdateAutomaticTapeCreationPolicyInputRequestModel(BaseModel):
    automatic_tape_creation_rules: Sequence[AutomaticTapeCreationRuleModel] = Field(
        alias="AutomaticTapeCreationRules"
    )
    gateway_arn: str = Field(alias="GatewayARN")


class DescribeBandwidthRateLimitScheduleOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    bandwidth_rate_limit_intervals: List[BandwidthRateLimitIntervalModel] = Field(
        alias="BandwidthRateLimitIntervals"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBandwidthRateLimitScheduleInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    bandwidth_rate_limit_intervals: Sequence[BandwidthRateLimitIntervalModel] = Field(
        alias="BandwidthRateLimitIntervals"
    )


class CachediSCSIVolumeModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="VolumeARN")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    volume_status: Optional[str] = Field(default=None, alias="VolumeStatus")
    volume_attachment_status: Optional[str] = Field(
        default=None, alias="VolumeAttachmentStatus"
    )
    volume_size_in_bytes: Optional[int] = Field(default=None, alias="VolumeSizeInBytes")
    volume_progress: Optional[float] = Field(default=None, alias="VolumeProgress")
    source_snapshot_id: Optional[str] = Field(default=None, alias="SourceSnapshotId")
    volumei_s_cs_iattributes: Optional[VolumeiSCSIAttributesModel] = Field(
        default=None, alias="VolumeiSCSIAttributes"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    volume_used_in_bytes: Optional[int] = Field(default=None, alias="VolumeUsedInBytes")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    target_name: Optional[str] = Field(default=None, alias="TargetName")


class StorediSCSIVolumeModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="VolumeARN")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    volume_status: Optional[str] = Field(default=None, alias="VolumeStatus")
    volume_attachment_status: Optional[str] = Field(
        default=None, alias="VolumeAttachmentStatus"
    )
    volume_size_in_bytes: Optional[int] = Field(default=None, alias="VolumeSizeInBytes")
    volume_progress: Optional[float] = Field(default=None, alias="VolumeProgress")
    volume_disk_id: Optional[str] = Field(default=None, alias="VolumeDiskId")
    source_snapshot_id: Optional[str] = Field(default=None, alias="SourceSnapshotId")
    preserved_existing_data: Optional[bool] = Field(
        default=None, alias="PreservedExistingData"
    )
    volumei_s_cs_iattributes: Optional[VolumeiSCSIAttributesModel] = Field(
        default=None, alias="VolumeiSCSIAttributes"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    volume_used_in_bytes: Optional[int] = Field(default=None, alias="VolumeUsedInBytes")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    target_name: Optional[str] = Field(default=None, alias="TargetName")


class DescribeChapCredentialsOutputModel(BaseModel):
    chap_credentials: List[ChapInfoModel] = Field(alias="ChapCredentials")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNFSFileShareInputRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    gateway_arn: str = Field(alias="GatewayARN")
    role: str = Field(alias="Role")
    location_arn: str = Field(alias="LocationARN")
    nfs_file_share_defaults: Optional[NFSFileShareDefaultsModel] = Field(
        default=None, alias="NFSFileShareDefaults"
    )
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    client_list: Optional[Sequence[str]] = Field(default=None, alias="ClientList")
    squash: Optional[str] = Field(default=None, alias="Squash")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    vp_cendpoint_dns_name: Optional[str] = Field(
        default=None, alias="VPCEndpointDNSName"
    )
    bucket_region: Optional[str] = Field(default=None, alias="BucketRegion")
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )


class NFSFileShareInfoModel(BaseModel):
    nfs_file_share_defaults: Optional[NFSFileShareDefaultsModel] = Field(
        default=None, alias="NFSFileShareDefaults"
    )
    file_share_arn: Optional[str] = Field(default=None, alias="FileShareARN")
    file_share_id: Optional[str] = Field(default=None, alias="FileShareId")
    file_share_status: Optional[str] = Field(default=None, alias="FileShareStatus")
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    path: Optional[str] = Field(default=None, alias="Path")
    role: Optional[str] = Field(default=None, alias="Role")
    location_arn: Optional[str] = Field(default=None, alias="LocationARN")
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    client_list: Optional[List[str]] = Field(default=None, alias="ClientList")
    squash: Optional[str] = Field(default=None, alias="Squash")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    vp_cendpoint_dns_name: Optional[str] = Field(
        default=None, alias="VPCEndpointDNSName"
    )
    bucket_region: Optional[str] = Field(default=None, alias="BucketRegion")
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )


class UpdateNFSFileShareInputRequestModel(BaseModel):
    file_share_arn: str = Field(alias="FileShareARN")
    kms_encrypted: Optional[bool] = Field(default=None, alias="KMSEncrypted")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    nfs_file_share_defaults: Optional[NFSFileShareDefaultsModel] = Field(
        default=None, alias="NFSFileShareDefaults"
    )
    default_storage_class: Optional[str] = Field(
        default=None, alias="DefaultStorageClass"
    )
    object_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ObjectACL")
    client_list: Optional[Sequence[str]] = Field(default=None, alias="ClientList")
    squash: Optional[str] = Field(default=None, alias="Squash")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    guess_mimetype_enabled: Optional[bool] = Field(
        default=None, alias="GuessMIMETypeEnabled"
    )
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    file_share_name: Optional[str] = Field(default=None, alias="FileShareName")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    notification_policy: Optional[str] = Field(default=None, alias="NotificationPolicy")
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )


class DescribeGatewayInformationOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    gateway_id: str = Field(alias="GatewayId")
    gateway_name: str = Field(alias="GatewayName")
    gateway_timezone: str = Field(alias="GatewayTimezone")
    gateway_state: str = Field(alias="GatewayState")
    gateway_network_interfaces: List[NetworkInterfaceModel] = Field(
        alias="GatewayNetworkInterfaces"
    )
    gateway_type: str = Field(alias="GatewayType")
    next_update_availability_date: str = Field(alias="NextUpdateAvailabilityDate")
    last_software_update: str = Field(alias="LastSoftwareUpdate")
    ec2_instance_id: str = Field(alias="Ec2InstanceId")
    ec2_instance_region: str = Field(alias="Ec2InstanceRegion")
    tags: List[TagModel] = Field(alias="Tags")
    vp_cendpoint: str = Field(alias="VPCEndpoint")
    cloud_watch_log_group_arn: str = Field(alias="CloudWatchLogGroupARN")
    host_environment: Literal[
        "EC2", "HYPER-V", "KVM", "OTHER", "SNOWBALL", "VMWARE"
    ] = Field(alias="HostEnvironment")
    endpoint_type: str = Field(alias="EndpointType")
    software_updates_end_date: str = Field(alias="SoftwareUpdatesEndDate")
    deprecation_date: str = Field(alias="DeprecationDate")
    gateway_capacity: Literal["Large", "Medium", "Small"] = Field(
        alias="GatewayCapacity"
    )
    supported_gateway_capacities: List[Literal["Large", "Medium", "Small"]] = Field(
        alias="SupportedGatewayCapacities"
    )
    host_environment_id: str = Field(alias="HostEnvironmentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSMBSettingsOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    domain_name: str = Field(alias="DomainName")
    active_directory_status: Literal[
        "ACCESS_DENIED",
        "DETACHED",
        "JOINED",
        "JOINING",
        "NETWORK_ERROR",
        "TIMEOUT",
        "UNKNOWN_ERROR",
    ] = Field(alias="ActiveDirectoryStatus")
    s_mbguest_password_set: bool = Field(alias="SMBGuestPasswordSet")
    s_mbsecurity_strategy: Literal[
        "ClientSpecified", "MandatoryEncryption", "MandatorySigning"
    ] = Field(alias="SMBSecurityStrategy")
    file_shares_visible: bool = Field(alias="FileSharesVisible")
    s_mblocal_groups: SMBLocalGroupsModel = Field(alias="SMBLocalGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSMBLocalGroupsInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    s_mblocal_groups: SMBLocalGroupsModel = Field(alias="SMBLocalGroups")


class DescribeTapeArchivesInputDescribeTapeArchivesPaginateModel(BaseModel):
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTapesInputDescribeTapesPaginateModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeVTLDevicesInputDescribeVTLDevicesPaginateModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    vtl_device_arns: Optional[Sequence[str]] = Field(
        default=None, alias="VTLDeviceARNs"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFileSharesInputListFileSharesPaginateModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFileSystemAssociationsInputListFileSystemAssociationsPaginateModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGatewaysInputListGatewaysPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceInputListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTapePoolsInputListTapePoolsPaginateModel(BaseModel):
    pool_arns: Optional[Sequence[str]] = Field(default=None, alias="PoolARNs")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTapesInputListTapesPaginateModel(BaseModel):
    tape_arns: Optional[Sequence[str]] = Field(default=None, alias="TapeARNs")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVolumesInputListVolumesPaginateModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTapeArchivesOutputModel(BaseModel):
    tape_archives: List[TapeArchiveModel] = Field(alias="TapeArchives")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTapeRecoveryPointsOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    tape_recovery_point_infos: List[TapeRecoveryPointInfoModel] = Field(
        alias="TapeRecoveryPointInfos"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTapesOutputModel(BaseModel):
    tapes: List[TapeModel] = Field(alias="Tapes")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VTLDeviceModel(BaseModel):
    vtl_device_arn: Optional[str] = Field(default=None, alias="VTLDeviceARN")
    vtl_device_type: Optional[str] = Field(default=None, alias="VTLDeviceType")
    vtl_device_vendor: Optional[str] = Field(default=None, alias="VTLDeviceVendor")
    vtl_device_product_identifier: Optional[str] = Field(
        default=None, alias="VTLDeviceProductIdentifier"
    )
    devicei_s_cs_iattributes: Optional[DeviceiSCSIAttributesModel] = Field(
        default=None, alias="DeviceiSCSIAttributes"
    )


class ListLocalDisksOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    disks: List[DiskModel] = Field(alias="Disks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFileSharesOutputModel(BaseModel):
    marker: str = Field(alias="Marker")
    next_marker: str = Field(alias="NextMarker")
    file_share_info_list: List[FileShareInfoModel] = Field(alias="FileShareInfoList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FileSystemAssociationInfoModel(BaseModel):
    file_system_association_arn: Optional[str] = Field(
        default=None, alias="FileSystemAssociationARN"
    )
    location_arn: Optional[str] = Field(default=None, alias="LocationARN")
    file_system_association_status: Optional[str] = Field(
        default=None, alias="FileSystemAssociationStatus"
    )
    audit_destination_arn: Optional[str] = Field(
        default=None, alias="AuditDestinationARN"
    )
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    cache_attributes: Optional[CacheAttributesModel] = Field(
        default=None, alias="CacheAttributes"
    )
    endpoint_network_configuration: Optional[EndpointNetworkConfigurationModel] = Field(
        default=None, alias="EndpointNetworkConfiguration"
    )
    file_system_association_status_details: Optional[
        List[FileSystemAssociationStatusDetailModel]
    ] = Field(default=None, alias="FileSystemAssociationStatusDetails")


class ListFileSystemAssociationsOutputModel(BaseModel):
    marker: str = Field(alias="Marker")
    next_marker: str = Field(alias="NextMarker")
    file_system_association_summary_list: List[
        FileSystemAssociationSummaryModel
    ] = Field(alias="FileSystemAssociationSummaryList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGatewaysOutputModel(BaseModel):
    gateways: List[GatewayInfoModel] = Field(alias="Gateways")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTapePoolsOutputModel(BaseModel):
    pool_infos: List[PoolInfoModel] = Field(alias="PoolInfos")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTapesOutputModel(BaseModel):
    tape_infos: List[TapeInfoModel] = Field(alias="TapeInfos")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVolumeRecoveryPointsOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    volume_recovery_point_infos: List[VolumeRecoveryPointInfoModel] = Field(
        alias="VolumeRecoveryPointInfos"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVolumesOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    marker: str = Field(alias="Marker")
    volume_infos: List[VolumeInfoModel] = Field(alias="VolumeInfos")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSMBFileSharesOutputModel(BaseModel):
    s_mbfile_share_info_list: List[SMBFileShareInfoModel] = Field(
        alias="SMBFileShareInfoList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAutomaticTapeCreationPoliciesOutputModel(BaseModel):
    automatic_tape_creation_policy_infos: List[
        AutomaticTapeCreationPolicyInfoModel
    ] = Field(alias="AutomaticTapeCreationPolicyInfos")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCachediSCSIVolumesOutputModel(BaseModel):
    cachedi_s_cs_ivolumes: List[CachediSCSIVolumeModel] = Field(
        alias="CachediSCSIVolumes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStorediSCSIVolumesOutputModel(BaseModel):
    storedi_s_cs_ivolumes: List[StorediSCSIVolumeModel] = Field(
        alias="StorediSCSIVolumes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNFSFileSharesOutputModel(BaseModel):
    nfs_file_share_info_list: List[NFSFileShareInfoModel] = Field(
        alias="NFSFileShareInfoList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVTLDevicesOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayARN")
    vtl_devices: List[VTLDeviceModel] = Field(alias="VTLDevices")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFileSystemAssociationsOutputModel(BaseModel):
    file_system_association_info_list: List[FileSystemAssociationInfoModel] = Field(
        alias="FileSystemAssociationInfoList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
