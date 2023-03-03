# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

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


class CreateHapgRequestModel(BaseModel):
    label: str = Field(alias="Label")


class CreateHsmRequestModel(BaseModel):
    subnet_id: str = Field(alias="SubnetId")
    ssh_key: str = Field(alias="SshKey")
    iam_role_arn: str = Field(alias="IamRoleArn")
    subscription_type: Literal["PRODUCTION"] = Field(alias="SubscriptionType")
    eni_ip: Optional[str] = Field(default=None, alias="EniIp")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    syslog_ip: Optional[str] = Field(default=None, alias="SyslogIp")


class CreateLunaClientRequestModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    label: Optional[str] = Field(default=None, alias="Label")


class DeleteHapgRequestModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")


class DeleteHsmRequestModel(BaseModel):
    hsm_arn: str = Field(alias="HsmArn")


class DeleteLunaClientRequestModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")


class DescribeHapgRequestModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")


class DescribeHsmRequestModel(BaseModel):
    hsm_arn: Optional[str] = Field(default=None, alias="HsmArn")
    hsm_serial_number: Optional[str] = Field(default=None, alias="HsmSerialNumber")


class DescribeLunaClientRequestModel(BaseModel):
    client_arn: Optional[str] = Field(default=None, alias="ClientArn")
    certificate_fingerprint: Optional[str] = Field(
        default=None, alias="CertificateFingerprint"
    )


class GetConfigRequestModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")
    client_version: Literal["5.1", "5.3"] = Field(alias="ClientVersion")
    hapg_list: Sequence[str] = Field(alias="HapgList")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListHapgsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHsmsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLunaClientsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ModifyHapgRequestModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")
    label: Optional[str] = Field(default=None, alias="Label")
    partition_serial_list: Optional[Sequence[str]] = Field(
        default=None, alias="PartitionSerialList"
    )


class ModifyHsmRequestModel(BaseModel):
    hsm_arn: str = Field(alias="HsmArn")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    eni_ip: Optional[str] = Field(default=None, alias="EniIp")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    syslog_ip: Optional[str] = Field(default=None, alias="SyslogIp")


class ModifyLunaClientRequestModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")
    certificate: str = Field(alias="Certificate")


class RemoveTagsFromResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_key_list: Sequence[str] = Field(alias="TagKeyList")


class AddTagsToResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_list: Sequence[TagModel] = Field(alias="TagList")


class AddTagsToResourceResponseModel(BaseModel):
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHapgResponseModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHsmResponseModel(BaseModel):
    hsm_arn: str = Field(alias="HsmArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLunaClientResponseModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteHapgResponseModel(BaseModel):
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteHsmResponseModel(BaseModel):
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLunaClientResponseModel(BaseModel):
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHapgResponseModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")
    hapg_serial: str = Field(alias="HapgSerial")
    hsms_last_action_failed: List[str] = Field(alias="HsmsLastActionFailed")
    hsms_pending_deletion: List[str] = Field(alias="HsmsPendingDeletion")
    hsms_pending_registration: List[str] = Field(alias="HsmsPendingRegistration")
    label: str = Field(alias="Label")
    last_modified_timestamp: str = Field(alias="LastModifiedTimestamp")
    partition_serial_list: List[str] = Field(alias="PartitionSerialList")
    state: Literal["DEGRADED", "READY", "UPDATING"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHsmResponseModel(BaseModel):
    hsm_arn: str = Field(alias="HsmArn")
    status: Literal[
        "DEGRADED",
        "PENDING",
        "RUNNING",
        "SUSPENDED",
        "TERMINATED",
        "TERMINATING",
        "UPDATING",
    ] = Field(alias="Status")
    status_details: str = Field(alias="StatusDetails")
    availability_zone: str = Field(alias="AvailabilityZone")
    eni_id: str = Field(alias="EniId")
    eni_ip: str = Field(alias="EniIp")
    subscription_type: Literal["PRODUCTION"] = Field(alias="SubscriptionType")
    subscription_start_date: str = Field(alias="SubscriptionStartDate")
    subscription_end_date: str = Field(alias="SubscriptionEndDate")
    vpc_id: str = Field(alias="VpcId")
    subnet_id: str = Field(alias="SubnetId")
    iam_role_arn: str = Field(alias="IamRoleArn")
    serial_number: str = Field(alias="SerialNumber")
    vendor_name: str = Field(alias="VendorName")
    hsm_type: str = Field(alias="HsmType")
    software_version: str = Field(alias="SoftwareVersion")
    ssh_public_key: str = Field(alias="SshPublicKey")
    ssh_key_last_updated: str = Field(alias="SshKeyLastUpdated")
    server_cert_uri: str = Field(alias="ServerCertUri")
    server_cert_last_updated: str = Field(alias="ServerCertLastUpdated")
    partitions: List[str] = Field(alias="Partitions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLunaClientResponseModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")
    certificate: str = Field(alias="Certificate")
    certificate_fingerprint: str = Field(alias="CertificateFingerprint")
    last_modified_timestamp: str = Field(alias="LastModifiedTimestamp")
    label: str = Field(alias="Label")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConfigResponseModel(BaseModel):
    config_type: str = Field(alias="ConfigType")
    config_file: str = Field(alias="ConfigFile")
    config_cred: str = Field(alias="ConfigCred")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableZonesResponseModel(BaseModel):
    azlist: List[str] = Field(alias="AZList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHapgsResponseModel(BaseModel):
    hapg_list: List[str] = Field(alias="HapgList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHsmsResponseModel(BaseModel):
    hsm_list: List[str] = Field(alias="HsmList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLunaClientsResponseModel(BaseModel):
    client_list: List[str] = Field(alias="ClientList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyHapgResponseModel(BaseModel):
    hapg_arn: str = Field(alias="HapgArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyHsmResponseModel(BaseModel):
    hsm_arn: str = Field(alias="HsmArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyLunaClientResponseModel(BaseModel):
    client_arn: str = Field(alias="ClientArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveTagsFromResourceResponseModel(BaseModel):
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHapgsRequestListHapgsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHsmsRequestListHsmsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLunaClientsRequestListLunaClientsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
