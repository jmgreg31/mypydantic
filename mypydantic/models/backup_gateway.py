# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateGatewayToServerInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    server_arn: str = Field(alias="ServerArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BandwidthRateLimitIntervalModel(BaseModel):
    days_of_week: List[int] = Field(alias="DaysOfWeek")
    end_hour_of_day: int = Field(alias="EndHourOfDay")
    end_minute_of_hour: int = Field(alias="EndMinuteOfHour")
    start_hour_of_day: int = Field(alias="StartHourOfDay")
    start_minute_of_hour: int = Field(alias="StartMinuteOfHour")
    average_upload_rate_limit_in_bits_per_sec: Optional[int] = Field(
        default=None, alias="AverageUploadRateLimitInBitsPerSec"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class DeleteHypervisorInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")


class DisassociateGatewayFromServerInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class MaintenanceStartTimeModel(BaseModel):
    hour_of_day: int = Field(alias="HourOfDay")
    minute_of_hour: int = Field(alias="MinuteOfHour")
    day_of_month: Optional[int] = Field(default=None, alias="DayOfMonth")
    day_of_week: Optional[int] = Field(default=None, alias="DayOfWeek")


class GatewayModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayArn")
    gateway_display_name: Optional[str] = Field(
        default=None, alias="GatewayDisplayName"
    )
    gateway_type: Optional[Literal["BACKUP_VM"]] = Field(
        default=None, alias="GatewayType"
    )
    hypervisor_id: Optional[str] = Field(default=None, alias="HypervisorId")
    last_seen_time: Optional[datetime] = Field(default=None, alias="LastSeenTime")


class GetBandwidthRateLimitScheduleInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class GetGatewayInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class GetHypervisorInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")


class HypervisorDetailsModel(BaseModel):
    host: Optional[str] = Field(default=None, alias="Host")
    hypervisor_arn: Optional[str] = Field(default=None, alias="HypervisorArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    last_successful_metadata_sync_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulMetadataSyncTime"
    )
    latest_metadata_sync_status: Optional[
        Literal["CREATED", "FAILED", "PARTIALLY_FAILED", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="LatestMetadataSyncStatus")
    latest_metadata_sync_status_message: Optional[str] = Field(
        default=None, alias="LatestMetadataSyncStatusMessage"
    )
    log_group_arn: Optional[str] = Field(default=None, alias="LogGroupArn")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ERROR", "OFFLINE", "ONLINE", "PENDING"]] = Field(
        default=None, alias="State"
    )


class GetHypervisorPropertyMappingsInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")


class VmwareToAwsTagMappingModel(BaseModel):
    aws_tag_key: str = Field(alias="AwsTagKey")
    aws_tag_value: str = Field(alias="AwsTagValue")
    vmware_category: str = Field(alias="VmwareCategory")
    vmware_tag_name: str = Field(alias="VmwareTagName")


class GetVirtualMachineInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class HypervisorModel(BaseModel):
    host: Optional[str] = Field(default=None, alias="Host")
    hypervisor_arn: Optional[str] = Field(default=None, alias="HypervisorArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ERROR", "OFFLINE", "ONLINE", "PENDING"]] = Field(
        default=None, alias="State"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListGatewaysInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHypervisorsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListVirtualMachinesInputRequestModel(BaseModel):
    hypervisor_arn: Optional[str] = Field(default=None, alias="HypervisorArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VirtualMachineModel(BaseModel):
    host_name: Optional[str] = Field(default=None, alias="HostName")
    hypervisor_id: Optional[str] = Field(default=None, alias="HypervisorId")
    last_backup_date: Optional[datetime] = Field(default=None, alias="LastBackupDate")
    name: Optional[str] = Field(default=None, alias="Name")
    path: Optional[str] = Field(default=None, alias="Path")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class PutMaintenanceStartTimeInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    hour_of_day: int = Field(alias="HourOfDay")
    minute_of_hour: int = Field(alias="MinuteOfHour")
    day_of_month: Optional[int] = Field(default=None, alias="DayOfMonth")
    day_of_week: Optional[int] = Field(default=None, alias="DayOfWeek")


class StartVirtualMachinesMetadataSyncInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")


class TestHypervisorConfigurationInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    host: str = Field(alias="Host")
    password: Optional[str] = Field(default=None, alias="Password")
    username: Optional[str] = Field(default=None, alias="Username")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateGatewayInformationInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    gateway_display_name: Optional[str] = Field(
        default=None, alias="GatewayDisplayName"
    )


class UpdateGatewaySoftwareNowInputRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class UpdateHypervisorInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    host: Optional[str] = Field(default=None, alias="Host")
    log_group_arn: Optional[str] = Field(default=None, alias="LogGroupArn")
    name: Optional[str] = Field(default=None, alias="Name")
    password: Optional[str] = Field(default=None, alias="Password")
    username: Optional[str] = Field(default=None, alias="Username")


class VmwareTagModel(BaseModel):
    vmware_category: Optional[str] = Field(default=None, alias="VmwareCategory")
    vmware_tag_description: Optional[str] = Field(
        default=None, alias="VmwareTagDescription"
    )
    vmware_tag_name: Optional[str] = Field(default=None, alias="VmwareTagName")


class AssociateGatewayToServerOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGatewayOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteHypervisorOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateGatewayFromServerOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportHypervisorConfigurationOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBandwidthRateLimitScheduleOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutHypervisorPropertyMappingsOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMaintenanceStartTimeOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartVirtualMachinesMetadataSyncOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewayInformationOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewaySoftwareNowOutputModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHypervisorOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBandwidthRateLimitScheduleOutputModel(BaseModel):
    bandwidth_rate_limit_intervals: List[BandwidthRateLimitIntervalModel] = Field(
        alias="BandwidthRateLimitIntervals"
    )
    gateway_arn: str = Field(alias="GatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBandwidthRateLimitScheduleInputRequestModel(BaseModel):
    bandwidth_rate_limit_intervals: Sequence[BandwidthRateLimitIntervalModel] = Field(
        alias="BandwidthRateLimitIntervals"
    )
    gateway_arn: str = Field(alias="GatewayArn")


class CreateGatewayInputRequestModel(BaseModel):
    activation_key: str = Field(alias="ActivationKey")
    gateway_display_name: str = Field(alias="GatewayDisplayName")
    gateway_type: Literal["BACKUP_VM"] = Field(alias="GatewayType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ImportHypervisorConfigurationInputRequestModel(BaseModel):
    host: str = Field(alias="Host")
    name: str = Field(alias="Name")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    password: Optional[str] = Field(default=None, alias="Password")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    username: Optional[str] = Field(default=None, alias="Username")


class ListTagsForResourceOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class GatewayDetailsModel(BaseModel):
    gateway_arn: Optional[str] = Field(default=None, alias="GatewayArn")
    gateway_display_name: Optional[str] = Field(
        default=None, alias="GatewayDisplayName"
    )
    gateway_type: Optional[Literal["BACKUP_VM"]] = Field(
        default=None, alias="GatewayType"
    )
    hypervisor_id: Optional[str] = Field(default=None, alias="HypervisorId")
    last_seen_time: Optional[datetime] = Field(default=None, alias="LastSeenTime")
    maintenance_start_time: Optional[MaintenanceStartTimeModel] = Field(
        default=None, alias="MaintenanceStartTime"
    )
    next_update_availability_time: Optional[datetime] = Field(
        default=None, alias="NextUpdateAvailabilityTime"
    )
    vpc_endpoint: Optional[str] = Field(default=None, alias="VpcEndpoint")


class ListGatewaysOutputModel(BaseModel):
    gateways: List[GatewayModel] = Field(alias="Gateways")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHypervisorOutputModel(BaseModel):
    hypervisor: HypervisorDetailsModel = Field(alias="Hypervisor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHypervisorPropertyMappingsOutputModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    iam_role_arn: str = Field(alias="IamRoleArn")
    vmware_to_aws_tag_mappings: List[VmwareToAwsTagMappingModel] = Field(
        alias="VmwareToAwsTagMappings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutHypervisorPropertyMappingsInputRequestModel(BaseModel):
    hypervisor_arn: str = Field(alias="HypervisorArn")
    iam_role_arn: str = Field(alias="IamRoleArn")
    vmware_to_aws_tag_mappings: Sequence[VmwareToAwsTagMappingModel] = Field(
        alias="VmwareToAwsTagMappings"
    )


class ListHypervisorsOutputModel(BaseModel):
    hypervisors: List[HypervisorModel] = Field(alias="Hypervisors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGatewaysInputListGatewaysPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHypervisorsInputListHypervisorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualMachinesInputListVirtualMachinesPaginateModel(BaseModel):
    hypervisor_arn: Optional[str] = Field(default=None, alias="HypervisorArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualMachinesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    virtual_machines: List[VirtualMachineModel] = Field(alias="VirtualMachines")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualMachineDetailsModel(BaseModel):
    host_name: Optional[str] = Field(default=None, alias="HostName")
    hypervisor_id: Optional[str] = Field(default=None, alias="HypervisorId")
    last_backup_date: Optional[datetime] = Field(default=None, alias="LastBackupDate")
    name: Optional[str] = Field(default=None, alias="Name")
    path: Optional[str] = Field(default=None, alias="Path")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    vmware_tags: Optional[List[VmwareTagModel]] = Field(
        default=None, alias="VmwareTags"
    )


class GetGatewayOutputModel(BaseModel):
    gateway: GatewayDetailsModel = Field(alias="Gateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVirtualMachineOutputModel(BaseModel):
    virtual_machine: VirtualMachineDetailsModel = Field(alias="VirtualMachine")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
