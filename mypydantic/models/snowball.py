# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressModel(BaseModel):
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    name: Optional[str] = Field(default=None, alias="Name")
    company: Optional[str] = Field(default=None, alias="Company")
    street1: Optional[str] = Field(default=None, alias="Street1")
    street2: Optional[str] = Field(default=None, alias="Street2")
    street3: Optional[str] = Field(default=None, alias="Street3")
    city: Optional[str] = Field(default=None, alias="City")
    state_or_province: Optional[str] = Field(default=None, alias="StateOrProvince")
    prefecture_or_district: Optional[str] = Field(
        default=None, alias="PrefectureOrDistrict"
    )
    landmark: Optional[str] = Field(default=None, alias="Landmark")
    country: Optional[str] = Field(default=None, alias="Country")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    is_restricted: Optional[bool] = Field(default=None, alias="IsRestricted")


class CancelClusterRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class CancelJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class ClusterListEntryModel(BaseModel):
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    cluster_state: Optional[
        Literal["AwaitingQuorum", "Cancelled", "Complete", "InUse", "Pending"]
    ] = Field(default=None, alias="ClusterState")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    description: Optional[str] = Field(default=None, alias="Description")


class NotificationModel(BaseModel):
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicARN")
    job_states_to_notify: Optional[
        Sequence[
            Literal[
                "Cancelled",
                "Complete",
                "InProgress",
                "InTransitToAWS",
                "InTransitToCustomer",
                "Listing",
                "New",
                "Pending",
                "PreparingAppliance",
                "PreparingShipment",
                "WithAWS",
                "WithAWSSortingFacility",
                "WithCustomer",
            ]
        ]
    ] = Field(default=None, alias="JobStatesToNotify")
    notify_all: Optional[bool] = Field(default=None, alias="NotifyAll")


class CompatibleImageModel(BaseModel):
    ami_id: Optional[str] = Field(default=None, alias="AmiId")
    name: Optional[str] = Field(default=None, alias="Name")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLongTermPricingRequestModel(BaseModel):
    long_term_pricing_type: Literal["OneYear", "ThreeYear"] = Field(
        alias="LongTermPricingType"
    )
    is_long_term_pricing_auto_renew: Optional[bool] = Field(
        default=None, alias="IsLongTermPricingAutoRenew"
    )
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")


class CreateReturnShippingLabelRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")


class DataTransferModel(BaseModel):
    bytes_transferred: Optional[int] = Field(default=None, alias="BytesTransferred")
    objects_transferred: Optional[int] = Field(default=None, alias="ObjectsTransferred")
    total_bytes: Optional[int] = Field(default=None, alias="TotalBytes")
    total_objects: Optional[int] = Field(default=None, alias="TotalObjects")


class ServiceVersionModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")


class DescribeAddressRequestModel(BaseModel):
    address_id: str = Field(alias="AddressId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAddressesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeClusterRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class DescribeJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeReturnShippingLabelRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class EKSOnDeviceServiceConfigurationModel(BaseModel):
    kubernetes_version: Optional[str] = Field(default=None, alias="KubernetesVersion")
    eks_anywhere_version: Optional[str] = Field(
        default=None, alias="EKSAnywhereVersion"
    )


class Ec2AmiResourceModel(BaseModel):
    ami_id: str = Field(alias="AmiId")
    snowball_ami_id: Optional[str] = Field(default=None, alias="SnowballAmiId")


class EventTriggerDefinitionModel(BaseModel):
    event_resource_arn: Optional[str] = Field(default=None, alias="EventResourceARN")


class GetJobManifestRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class GetJobUnlockCodeRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class GetSoftwareUpdatesRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class INDTaxDocumentsModel(BaseModel):
    gs_tin: Optional[str] = Field(default=None, alias="GSTIN")


class JobListEntryModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_state: Optional[
        Literal[
            "Cancelled",
            "Complete",
            "InProgress",
            "InTransitToAWS",
            "InTransitToCustomer",
            "Listing",
            "New",
            "Pending",
            "PreparingAppliance",
            "PreparingShipment",
            "WithAWS",
            "WithAWSSortingFacility",
            "WithCustomer",
        ]
    ] = Field(default=None, alias="JobState")
    is_master: Optional[bool] = Field(default=None, alias="IsMaster")
    job_type: Optional[Literal["EXPORT", "IMPORT", "LOCAL_USE"]] = Field(
        default=None, alias="JobType"
    )
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    description: Optional[str] = Field(default=None, alias="Description")


class JobLogsModel(BaseModel):
    job_completion_report_uri: Optional[str] = Field(
        default=None, alias="JobCompletionReportURI"
    )
    job_success_log_uri: Optional[str] = Field(default=None, alias="JobSuccessLogURI")
    job_failure_log_uri: Optional[str] = Field(default=None, alias="JobFailureLogURI")


class KeyRangeModel(BaseModel):
    begin_marker: Optional[str] = Field(default=None, alias="BeginMarker")
    end_marker: Optional[str] = Field(default=None, alias="EndMarker")


class ListClusterJobsRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListClustersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCompatibleImagesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJobsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLongTermPricingRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LongTermPricingListEntryModel(BaseModel):
    long_term_pricing_id: Optional[str] = Field(default=None, alias="LongTermPricingId")
    long_term_pricing_end_date: Optional[datetime] = Field(
        default=None, alias="LongTermPricingEndDate"
    )
    long_term_pricing_start_date: Optional[datetime] = Field(
        default=None, alias="LongTermPricingStartDate"
    )
    long_term_pricing_type: Optional[Literal["OneYear", "ThreeYear"]] = Field(
        default=None, alias="LongTermPricingType"
    )
    current_active_job: Optional[str] = Field(default=None, alias="CurrentActiveJob")
    replacement_job: Optional[str] = Field(default=None, alias="ReplacementJob")
    is_long_term_pricing_auto_renew: Optional[bool] = Field(
        default=None, alias="IsLongTermPricingAutoRenew"
    )
    long_term_pricing_status: Optional[str] = Field(
        default=None, alias="LongTermPricingStatus"
    )
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")
    job_ids: Optional[List[str]] = Field(default=None, alias="JobIds")


class NFSOnDeviceServiceConfigurationModel(BaseModel):
    storage_limit: Optional[int] = Field(default=None, alias="StorageLimit")
    storage_unit: Optional[Literal["TB"]] = Field(default=None, alias="StorageUnit")


class TGWOnDeviceServiceConfigurationModel(BaseModel):
    storage_limit: Optional[int] = Field(default=None, alias="StorageLimit")
    storage_unit: Optional[Literal["TB"]] = Field(default=None, alias="StorageUnit")


class TargetOnDeviceServiceModel(BaseModel):
    service_name: Optional[
        Literal["NFS_ON_DEVICE_SERVICE", "S3_ON_DEVICE_SERVICE"]
    ] = Field(default=None, alias="ServiceName")
    transfer_option: Optional[Literal["EXPORT", "IMPORT", "LOCAL_USE"]] = Field(
        default=None, alias="TransferOption"
    )


class ShipmentModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    tracking_number: Optional[str] = Field(default=None, alias="TrackingNumber")


class WirelessConnectionModel(BaseModel):
    is_wifi_enabled: Optional[bool] = Field(default=None, alias="IsWifiEnabled")


class UpdateJobShipmentStateRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    shipment_state: Literal["RECEIVED", "RETURNED"] = Field(alias="ShipmentState")


class UpdateLongTermPricingRequestModel(BaseModel):
    long_term_pricing_id: str = Field(alias="LongTermPricingId")
    replacement_job: Optional[str] = Field(default=None, alias="ReplacementJob")
    is_long_term_pricing_auto_renew: Optional[bool] = Field(
        default=None, alias="IsLongTermPricingAutoRenew"
    )


class CreateAddressRequestModel(BaseModel):
    address: AddressModel = Field(alias="Address")


class CreateAddressResultModel(BaseModel):
    address_id: str = Field(alias="AddressId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResultModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobResultModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLongTermPricingResultModel(BaseModel):
    long_term_pricing_id: str = Field(alias="LongTermPricingId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReturnShippingLabelResultModel(BaseModel):
    status: Literal["Failed", "InProgress", "Succeeded", "TimedOut"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAddressResultModel(BaseModel):
    address: AddressModel = Field(alias="Address")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAddressesResultModel(BaseModel):
    addresses: List[AddressModel] = Field(alias="Addresses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReturnShippingLabelResultModel(BaseModel):
    status: Literal["Failed", "InProgress", "Succeeded", "TimedOut"] = Field(
        alias="Status"
    )
    expiration_date: datetime = Field(alias="ExpirationDate")
    return_shipping_label_uri: str = Field(alias="ReturnShippingLabelURI")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobManifestResultModel(BaseModel):
    manifest_uri: str = Field(alias="ManifestURI")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobUnlockCodeResultModel(BaseModel):
    unlock_code: str = Field(alias="UnlockCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnowballUsageResultModel(BaseModel):
    snowball_limit: int = Field(alias="SnowballLimit")
    snowballs_in_use: int = Field(alias="SnowballsInUse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSoftwareUpdatesResultModel(BaseModel):
    updates_uri: str = Field(alias="UpdatesURI")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersResultModel(BaseModel):
    cluster_list_entries: List[ClusterListEntryModel] = Field(
        alias="ClusterListEntries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCompatibleImagesResultModel(BaseModel):
    compatible_images: List[CompatibleImageModel] = Field(alias="CompatibleImages")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DependentServiceModel(BaseModel):
    service_name: Optional[Literal["EKS_ANYWHERE", "KUBERNETES"]] = Field(
        default=None, alias="ServiceName"
    )
    service_version: Optional[ServiceVersionModel] = Field(
        default=None, alias="ServiceVersion"
    )


class DescribeAddressesRequestDescribeAddressesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClusterJobsRequestListClusterJobsPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersRequestListClustersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCompatibleImagesRequestListCompatibleImagesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLongTermPricingRequestListLongTermPricingPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LambdaResourceModel(BaseModel):
    lambda_arn: Optional[str] = Field(default=None, alias="LambdaArn")
    event_triggers: Optional[Sequence[EventTriggerDefinitionModel]] = Field(
        default=None, alias="EventTriggers"
    )


class TaxDocumentsModel(BaseModel):
    ind: Optional[INDTaxDocumentsModel] = Field(default=None, alias="IND")


class ListClusterJobsResultModel(BaseModel):
    job_list_entries: List[JobListEntryModel] = Field(alias="JobListEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResultModel(BaseModel):
    job_list_entries: List[JobListEntryModel] = Field(alias="JobListEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLongTermPricingResultModel(BaseModel):
    long_term_pricing_entries: List[LongTermPricingListEntryModel] = Field(
        alias="LongTermPricingEntries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OnDeviceServiceConfigurationModel(BaseModel):
    nfs_on_device_service: Optional[NFSOnDeviceServiceConfigurationModel] = Field(
        default=None, alias="NFSOnDeviceService"
    )
    tgwon_device_service: Optional[TGWOnDeviceServiceConfigurationModel] = Field(
        default=None, alias="TGWOnDeviceService"
    )
    eks_on_device_service: Optional[EKSOnDeviceServiceConfigurationModel] = Field(
        default=None, alias="EKSOnDeviceService"
    )


class S3ResourceModel(BaseModel):
    bucket_arn: Optional[str] = Field(default=None, alias="BucketArn")
    key_range: Optional[KeyRangeModel] = Field(default=None, alias="KeyRange")
    target_on_device_services: Optional[Sequence[TargetOnDeviceServiceModel]] = Field(
        default=None, alias="TargetOnDeviceServices"
    )


class ShippingDetailsModel(BaseModel):
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")
    inbound_shipment: Optional[ShipmentModel] = Field(
        default=None, alias="InboundShipment"
    )
    outbound_shipment: Optional[ShipmentModel] = Field(
        default=None, alias="OutboundShipment"
    )


class SnowconeDeviceConfigurationModel(BaseModel):
    wireless_connection: Optional[WirelessConnectionModel] = Field(
        default=None, alias="WirelessConnection"
    )


class ListServiceVersionsRequestModel(BaseModel):
    service_name: Literal["EKS_ANYWHERE", "KUBERNETES"] = Field(alias="ServiceName")
    dependent_services: Optional[Sequence[DependentServiceModel]] = Field(
        default=None, alias="DependentServices"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListServiceVersionsResultModel(BaseModel):
    service_versions: List[ServiceVersionModel] = Field(alias="ServiceVersions")
    service_name: Literal["EKS_ANYWHERE", "KUBERNETES"] = Field(alias="ServiceName")
    dependent_services: List[DependentServiceModel] = Field(alias="DependentServices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobResourceModel(BaseModel):
    s3_resources: Optional[Sequence[S3ResourceModel]] = Field(
        default=None, alias="S3Resources"
    )
    lambda_resources: Optional[Sequence[LambdaResourceModel]] = Field(
        default=None, alias="LambdaResources"
    )
    ec2_ami_resources: Optional[Sequence[Ec2AmiResourceModel]] = Field(
        default=None, alias="Ec2AmiResources"
    )


class DeviceConfigurationModel(BaseModel):
    snowcone_device_configuration: Optional[SnowconeDeviceConfigurationModel] = Field(
        default=None, alias="SnowconeDeviceConfiguration"
    )


class ClusterMetadataModel(BaseModel):
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    cluster_state: Optional[
        Literal["AwaitingQuorum", "Cancelled", "Complete", "InUse", "Pending"]
    ] = Field(default=None, alias="ClusterState")
    job_type: Optional[Literal["EXPORT", "IMPORT", "LOCAL_USE"]] = Field(
        default=None, alias="JobType"
    )
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    resources: Optional[JobResourceModel] = Field(default=None, alias="Resources")
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )
    tax_documents: Optional[TaxDocumentsModel] = Field(
        default=None, alias="TaxDocuments"
    )
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")


class CreateClusterRequestModel(BaseModel):
    job_type: Literal["EXPORT", "IMPORT", "LOCAL_USE"] = Field(alias="JobType")
    resources: JobResourceModel = Field(alias="Resources")
    address_id: str = Field(alias="AddressId")
    role_arn: str = Field(alias="RoleARN")
    snowball_type: Literal[
        "EDGE",
        "EDGE_C",
        "EDGE_CG",
        "EDGE_S",
        "SNC1_HDD",
        "SNC1_SSD",
        "STANDARD",
        "V3_5C",
    ] = Field(alias="SnowballType")
    shipping_option: Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"] = Field(
        alias="ShippingOption"
    )
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyARN")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )
    tax_documents: Optional[TaxDocumentsModel] = Field(
        default=None, alias="TaxDocuments"
    )
    remote_management: Optional[
        Literal["INSTALLED_AUTOSTART", "INSTALLED_ONLY"]
    ] = Field(default=None, alias="RemoteManagement")


class UpdateClusterRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    description: Optional[str] = Field(default=None, alias="Description")
    resources: Optional[JobResourceModel] = Field(default=None, alias="Resources")
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )


class UpdateJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    resources: Optional[JobResourceModel] = Field(default=None, alias="Resources")
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")
    description: Optional[str] = Field(default=None, alias="Description")
    snowball_capacity_preference: Optional[
        Literal["NoPreference", "T100", "T14", "T32", "T42", "T50", "T8", "T80", "T98"]
    ] = Field(default=None, alias="SnowballCapacityPreference")
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )


class CreateJobRequestModel(BaseModel):
    job_type: Optional[Literal["EXPORT", "IMPORT", "LOCAL_USE"]] = Field(
        default=None, alias="JobType"
    )
    resources: Optional[JobResourceModel] = Field(default=None, alias="Resources")
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")
    description: Optional[str] = Field(default=None, alias="Description")
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    snowball_capacity_preference: Optional[
        Literal["NoPreference", "T100", "T14", "T32", "T42", "T50", "T8", "T80", "T98"]
    ] = Field(default=None, alias="SnowballCapacityPreference")
    shipping_option: Optional[
        Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
    ] = Field(default=None, alias="ShippingOption")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )
    tax_documents: Optional[TaxDocumentsModel] = Field(
        default=None, alias="TaxDocuments"
    )
    device_configuration: Optional[DeviceConfigurationModel] = Field(
        default=None, alias="DeviceConfiguration"
    )
    remote_management: Optional[
        Literal["INSTALLED_AUTOSTART", "INSTALLED_ONLY"]
    ] = Field(default=None, alias="RemoteManagement")
    long_term_pricing_id: Optional[str] = Field(default=None, alias="LongTermPricingId")


class JobMetadataModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_state: Optional[
        Literal[
            "Cancelled",
            "Complete",
            "InProgress",
            "InTransitToAWS",
            "InTransitToCustomer",
            "Listing",
            "New",
            "Pending",
            "PreparingAppliance",
            "PreparingShipment",
            "WithAWS",
            "WithAWSSortingFacility",
            "WithCustomer",
        ]
    ] = Field(default=None, alias="JobState")
    job_type: Optional[Literal["EXPORT", "IMPORT", "LOCAL_USE"]] = Field(
        default=None, alias="JobType"
    )
    snowball_type: Optional[
        Literal[
            "EDGE",
            "EDGE_C",
            "EDGE_CG",
            "EDGE_S",
            "SNC1_HDD",
            "SNC1_SSD",
            "STANDARD",
            "V3_5C",
        ]
    ] = Field(default=None, alias="SnowballType")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    resources: Optional[JobResourceModel] = Field(default=None, alias="Resources")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    address_id: Optional[str] = Field(default=None, alias="AddressId")
    shipping_details: Optional[ShippingDetailsModel] = Field(
        default=None, alias="ShippingDetails"
    )
    snowball_capacity_preference: Optional[
        Literal["NoPreference", "T100", "T14", "T32", "T42", "T50", "T8", "T80", "T98"]
    ] = Field(default=None, alias="SnowballCapacityPreference")
    notification: Optional[NotificationModel] = Field(
        default=None, alias="Notification"
    )
    data_transfer_progress: Optional[DataTransferModel] = Field(
        default=None, alias="DataTransferProgress"
    )
    job_log_info: Optional[JobLogsModel] = Field(default=None, alias="JobLogInfo")
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    forwarding_address_id: Optional[str] = Field(
        default=None, alias="ForwardingAddressId"
    )
    tax_documents: Optional[TaxDocumentsModel] = Field(
        default=None, alias="TaxDocuments"
    )
    device_configuration: Optional[DeviceConfigurationModel] = Field(
        default=None, alias="DeviceConfiguration"
    )
    remote_management: Optional[
        Literal["INSTALLED_AUTOSTART", "INSTALLED_ONLY"]
    ] = Field(default=None, alias="RemoteManagement")
    long_term_pricing_id: Optional[str] = Field(default=None, alias="LongTermPricingId")
    on_device_service_configuration: Optional[
        OnDeviceServiceConfigurationModel
    ] = Field(default=None, alias="OnDeviceServiceConfiguration")


class DescribeClusterResultModel(BaseModel):
    cluster_metadata: ClusterMetadataModel = Field(alias="ClusterMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeJobResultModel(BaseModel):
    job_metadata: JobMetadataModel = Field(alias="JobMetadata")
    sub_job_metadata: List[JobMetadataModel] = Field(alias="SubJobMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
