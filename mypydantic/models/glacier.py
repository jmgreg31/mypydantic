# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

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


class AbortMultipartUploadInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    upload_id: str = Field(alias="uploadId")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class AbortVaultLockInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class AccountVaultRequestModel(BaseModel):
    name: str = Field(alias="name")


class AddTagsToVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CSVInputModel(BaseModel):
    file_header_info: Optional[Literal["IGNORE", "NONE", "USE"]] = Field(
        default=None, alias="FileHeaderInfo"
    )
    comments: Optional[str] = Field(default=None, alias="Comments")
    quote_escape_character: Optional[str] = Field(
        default=None, alias="QuoteEscapeCharacter"
    )
    record_delimiter: Optional[str] = Field(default=None, alias="RecordDelimiter")
    field_delimiter: Optional[str] = Field(default=None, alias="FieldDelimiter")
    quote_character: Optional[str] = Field(default=None, alias="QuoteCharacter")


class CSVOutputModel(BaseModel):
    quote_fields: Optional[Literal["ALWAYS", "ASNEEDED"]] = Field(
        default=None, alias="QuoteFields"
    )
    quote_escape_character: Optional[str] = Field(
        default=None, alias="QuoteEscapeCharacter"
    )
    record_delimiter: Optional[str] = Field(default=None, alias="RecordDelimiter")
    field_delimiter: Optional[str] = Field(default=None, alias="FieldDelimiter")
    quote_character: Optional[str] = Field(default=None, alias="QuoteCharacter")


class CompleteMultipartUploadInputMultipartUploadCompleteModel(BaseModel):
    archive_size: Optional[str] = Field(default=None, alias="archiveSize")
    checksum: Optional[str] = Field(default=None, alias="checksum")


class CompleteMultipartUploadInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    upload_id: str = Field(alias="uploadId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    archive_size: Optional[str] = Field(default=None, alias="archiveSize")
    checksum: Optional[str] = Field(default=None, alias="checksum")


class CompleteVaultLockInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    lock_id: str = Field(alias="lockId")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class CreateVaultInputAccountCreateVaultModel(BaseModel):
    vault_name: str = Field(alias="vaultName")


class CreateVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class CreateVaultInputServiceResourceCreateVaultModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DataRetrievalRuleModel(BaseModel):
    strategy: Optional[str] = Field(default=None, alias="Strategy")
    bytes_per_hour: Optional[int] = Field(default=None, alias="BytesPerHour")


class DeleteArchiveInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    archive_id: str = Field(alias="archiveId")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DeleteVaultAccessPolicyInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DeleteVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DeleteVaultNotificationsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DescribeJobInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    job_id: str = Field(alias="jobId")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class DescribeVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeVaultOutputModel(BaseModel):
    vault_arn: Optional[str] = Field(default=None, alias="VaultARN")
    vault_name: Optional[str] = Field(default=None, alias="VaultName")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    last_inventory_date: Optional[str] = Field(default=None, alias="LastInventoryDate")
    number_of_archives: Optional[int] = Field(default=None, alias="NumberOfArchives")
    size_in_bytes: Optional[int] = Field(default=None, alias="SizeInBytes")


class EncryptionModel(BaseModel):
    encryption_type: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="EncryptionType"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    kms_context: Optional[str] = Field(default=None, alias="KMSContext")


class GetDataRetrievalPolicyInputRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")


class GetJobOutputInputJobGetOutputModel(BaseModel):
    range: Optional[str] = Field(default=None, alias="range")


class GetJobOutputInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    job_id: str = Field(alias="jobId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    range: Optional[str] = Field(default=None, alias="range")


class GetVaultAccessPolicyInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class VaultAccessPolicyModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="Policy")


class GetVaultLockInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class GetVaultNotificationsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class VaultNotificationConfigModel(BaseModel):
    s_ns_topic: Optional[str] = Field(default=None, alias="SNSTopic")
    events: Optional[List[str]] = Field(default=None, alias="Events")


class InventoryRetrievalJobDescriptionModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    limit: Optional[str] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GranteeModel(BaseModel):
    type: Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"] = Field(
        alias="Type"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    uri: Optional[str] = Field(default=None, alias="URI")
    id: Optional[str] = Field(default=None, alias="ID")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")


class InitiateMultipartUploadInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    archive_description: Optional[str] = Field(default=None, alias="archiveDescription")
    part_size: Optional[str] = Field(default=None, alias="partSize")


class InitiateMultipartUploadInputVaultInitiateMultipartUploadModel(BaseModel):
    archive_description: Optional[str] = Field(default=None, alias="archiveDescription")
    part_size: Optional[str] = Field(default=None, alias="partSize")


class VaultLockPolicyModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="Policy")


class InventoryRetrievalJobInputModel(BaseModel):
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    limit: Optional[str] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListJobsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    limit: Optional[str] = Field(default=None, alias="limit")
    marker: Optional[str] = Field(default=None, alias="marker")
    statuscode: Optional[str] = Field(default=None, alias="statuscode")
    completed: Optional[str] = Field(default=None, alias="completed")


class ListMultipartUploadsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    marker: Optional[str] = Field(default=None, alias="marker")
    limit: Optional[str] = Field(default=None, alias="limit")


class UploadListElementModel(BaseModel):
    multipart_upload_id: Optional[str] = Field(default=None, alias="MultipartUploadId")
    vault_arn: Optional[str] = Field(default=None, alias="VaultARN")
    archive_description: Optional[str] = Field(default=None, alias="ArchiveDescription")
    part_size_in_bytes: Optional[int] = Field(default=None, alias="PartSizeInBytes")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")


class ListPartsInputMultipartUploadPartsModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="marker")
    limit: Optional[str] = Field(default=None, alias="limit")


class ListPartsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    upload_id: str = Field(alias="uploadId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    marker: Optional[str] = Field(default=None, alias="marker")
    limit: Optional[str] = Field(default=None, alias="limit")


class PartListElementModel(BaseModel):
    range_in_bytes: Optional[str] = Field(default=None, alias="RangeInBytes")
    s_ha256_tree_hash: Optional[str] = Field(default=None, alias="SHA256TreeHash")


class ListProvisionedCapacityInputRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ProvisionedCapacityDescriptionModel(BaseModel):
    capacity_id: Optional[str] = Field(default=None, alias="CapacityId")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    expiration_date: Optional[str] = Field(default=None, alias="ExpirationDate")


class ListTagsForVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ListVaultsInputRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    marker: Optional[str] = Field(default=None, alias="marker")
    limit: Optional[str] = Field(default=None, alias="limit")


class PurchaseProvisionedCapacityInputRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")


class RemoveTagsFromVaultInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")


class ServiceResourceAccountRequestModel(BaseModel):
    id: str = Field(alias="id")


class ServiceResourceArchiveRequestModel(BaseModel):
    account_id: str = Field(alias="account_id")
    vault_name: str = Field(alias="vault_name")
    id: str = Field(alias="id")


class ServiceResourceJobRequestModel(BaseModel):
    account_id: str = Field(alias="account_id")
    vault_name: str = Field(alias="vault_name")
    id: str = Field(alias="id")


class ServiceResourceMultipartUploadRequestModel(BaseModel):
    account_id: str = Field(alias="account_id")
    vault_name: str = Field(alias="vault_name")
    id: str = Field(alias="id")


class ServiceResourceNotificationRequestModel(BaseModel):
    account_id: str = Field(alias="account_id")
    vault_name: str = Field(alias="vault_name")


class ServiceResourceVaultRequestModel(BaseModel):
    account_id: str = Field(alias="account_id")
    name: str = Field(alias="name")


class UploadArchiveInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    archive_description: Optional[str] = Field(default=None, alias="archiveDescription")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="body"
    )


class UploadArchiveInputVaultUploadArchiveModel(BaseModel):
    archive_description: Optional[str] = Field(default=None, alias="archiveDescription")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="body"
    )


class UploadMultipartPartInputMultipartUploadUploadPartModel(BaseModel):
    checksum: Optional[str] = Field(default=None, alias="checksum")
    range: Optional[str] = Field(default=None, alias="range")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="body"
    )


class UploadMultipartPartInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    upload_id: str = Field(alias="uploadId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    range: Optional[str] = Field(default=None, alias="range")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="body"
    )


class VaultArchiveRequestModel(BaseModel):
    id: str = Field(alias="id")


class VaultJobRequestModel(BaseModel):
    id: str = Field(alias="id")


class VaultMultipartUploadRequestModel(BaseModel):
    id: str = Field(alias="id")


class ArchiveCreationOutputModel(BaseModel):
    location: str = Field(alias="location")
    checksum: str = Field(alias="checksum")
    archive_id: str = Field(alias="archiveId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVaultOutputModel(BaseModel):
    location: str = Field(alias="location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVaultOutputResponseMetadataModel(BaseModel):
    vault_arn: str = Field(alias="VaultARN")
    vault_name: str = Field(alias="VaultName")
    creation_date: str = Field(alias="CreationDate")
    last_inventory_date: str = Field(alias="LastInventoryDate")
    number_of_archives: int = Field(alias="NumberOfArchives")
    size_in_bytes: int = Field(alias="SizeInBytes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobOutputOutputModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="body")
    checksum: str = Field(alias="checksum")
    status: int = Field(alias="status")
    content_range: str = Field(alias="contentRange")
    accept_ranges: str = Field(alias="acceptRanges")
    content_type: str = Field(alias="contentType")
    archive_description: str = Field(alias="archiveDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVaultLockOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    state: str = Field(alias="State")
    expiration_date: str = Field(alias="ExpirationDate")
    creation_date: str = Field(alias="CreationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateJobOutputModel(BaseModel):
    location: str = Field(alias="location")
    job_id: str = Field(alias="jobId")
    job_output_path: str = Field(alias="jobOutputPath")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateMultipartUploadOutputModel(BaseModel):
    location: str = Field(alias="location")
    upload_id: str = Field(alias="uploadId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateVaultLockOutputModel(BaseModel):
    lock_id: str = Field(alias="lockId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InventoryRetrievalJobDescriptionResponseMetadataModel(BaseModel):
    format: str = Field(alias="Format")
    start_date: str = Field(alias="StartDate")
    end_date: str = Field(alias="EndDate")
    limit: str = Field(alias="Limit")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForVaultOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseProvisionedCapacityOutputModel(BaseModel):
    capacity_id: str = Field(alias="capacityId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadMultipartPartOutputModel(BaseModel):
    checksum: str = Field(alias="checksum")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputSerializationModel(BaseModel):
    csv: Optional[CSVInputModel] = Field(default=None, alias="csv")


class OutputSerializationModel(BaseModel):
    csv: Optional[CSVOutputModel] = Field(default=None, alias="csv")


class DataRetrievalPolicyModel(BaseModel):
    rules: Optional[List[DataRetrievalRuleModel]] = Field(default=None, alias="Rules")


class DescribeVaultInputVaultExistsWaitModel(BaseModel):
    account_id: str = Field(alias="accountId")
    vault_name: str = Field(alias="vaultName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeVaultInputVaultNotExistsWaitModel(BaseModel):
    account_id: str = Field(alias="accountId")
    vault_name: str = Field(alias="vaultName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListVaultsOutputModel(BaseModel):
    vault_list: List[DescribeVaultOutputModel] = Field(alias="VaultList")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVaultAccessPolicyOutputModel(BaseModel):
    policy: VaultAccessPolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetVaultAccessPolicyInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    policy: Optional[VaultAccessPolicyModel] = Field(default=None, alias="policy")


class GetVaultNotificationsOutputModel(BaseModel):
    vault_notification_config: VaultNotificationConfigModel = Field(
        alias="vaultNotificationConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetVaultNotificationsInputNotificationSetModel(BaseModel):
    vault_notification_config: Optional[VaultNotificationConfigModel] = Field(
        default=None, alias="vaultNotificationConfig"
    )


class SetVaultNotificationsInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    vault_notification_config: Optional[VaultNotificationConfigModel] = Field(
        default=None, alias="vaultNotificationConfig"
    )


class GrantModel(BaseModel):
    grantee: Optional[GranteeModel] = Field(default=None, alias="Grantee")
    permission: Optional[
        Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
    ] = Field(default=None, alias="Permission")


class InitiateVaultLockInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    policy: Optional[VaultLockPolicyModel] = Field(default=None, alias="policy")


class ListJobsInputListJobsPaginateModel(BaseModel):
    account_id: str = Field(alias="accountId")
    vault_name: str = Field(alias="vaultName")
    statuscode: Optional[str] = Field(default=None, alias="statuscode")
    completed: Optional[str] = Field(default=None, alias="completed")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMultipartUploadsInputListMultipartUploadsPaginateModel(BaseModel):
    account_id: str = Field(alias="accountId")
    vault_name: str = Field(alias="vaultName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPartsInputListPartsPaginateModel(BaseModel):
    account_id: str = Field(alias="accountId")
    vault_name: str = Field(alias="vaultName")
    upload_id: str = Field(alias="uploadId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVaultsInputListVaultsPaginateModel(BaseModel):
    account_id: str = Field(alias="accountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMultipartUploadsOutputModel(BaseModel):
    uploads_list: List[UploadListElementModel] = Field(alias="UploadsList")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPartsOutputModel(BaseModel):
    multipart_upload_id: str = Field(alias="MultipartUploadId")
    vault_arn: str = Field(alias="VaultARN")
    archive_description: str = Field(alias="ArchiveDescription")
    part_size_in_bytes: int = Field(alias="PartSizeInBytes")
    creation_date: str = Field(alias="CreationDate")
    parts: List[PartListElementModel] = Field(alias="Parts")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisionedCapacityOutputModel(BaseModel):
    provisioned_capacity_list: List[ProvisionedCapacityDescriptionModel] = Field(
        alias="ProvisionedCapacityList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SelectParametersResponseMetadataModel(BaseModel):
    input_serialization: InputSerializationModel = Field(alias="InputSerialization")
    expression_type: Literal["SQL"] = Field(alias="ExpressionType")
    expression: str = Field(alias="Expression")
    output_serialization: OutputSerializationModel = Field(alias="OutputSerialization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SelectParametersModel(BaseModel):
    input_serialization: Optional[InputSerializationModel] = Field(
        default=None, alias="InputSerialization"
    )
    expression_type: Optional[Literal["SQL"]] = Field(
        default=None, alias="ExpressionType"
    )
    expression: Optional[str] = Field(default=None, alias="Expression")
    output_serialization: Optional[OutputSerializationModel] = Field(
        default=None, alias="OutputSerialization"
    )


class GetDataRetrievalPolicyOutputModel(BaseModel):
    policy: DataRetrievalPolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetDataRetrievalPolicyInputRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    policy: Optional[DataRetrievalPolicyModel] = Field(default=None, alias="Policy")


class S3LocationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    encryption: Optional[EncryptionModel] = Field(default=None, alias="Encryption")
    canned_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="CannedACL")
    access_control_list: Optional[List[GrantModel]] = Field(
        default=None, alias="AccessControlList"
    )
    tagging: Optional[Dict[str, str]] = Field(default=None, alias="Tagging")
    user_metadata: Optional[Dict[str, str]] = Field(default=None, alias="UserMetadata")
    storage_class: Optional[
        Literal["REDUCED_REDUNDANCY", "STANDARD", "STANDARD_IA"]
    ] = Field(default=None, alias="StorageClass")


class OutputLocationResponseMetadataModel(BaseModel):
    s3: S3LocationModel = Field(alias="S3")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OutputLocationModel(BaseModel):
    s3: Optional[S3LocationModel] = Field(default=None, alias="S3")


class GlacierJobDescriptionResponseMetadataModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_description: str = Field(alias="JobDescription")
    action: Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"] = Field(
        alias="Action"
    )
    archive_id: str = Field(alias="ArchiveId")
    vault_arn: str = Field(alias="VaultARN")
    creation_date: str = Field(alias="CreationDate")
    completed: bool = Field(alias="Completed")
    status_code: Literal["Failed", "InProgress", "Succeeded"] = Field(
        alias="StatusCode"
    )
    status_message: str = Field(alias="StatusMessage")
    archive_size_in_bytes: int = Field(alias="ArchiveSizeInBytes")
    inventory_size_in_bytes: int = Field(alias="InventorySizeInBytes")
    s_ns_topic: str = Field(alias="SNSTopic")
    completion_date: str = Field(alias="CompletionDate")
    s_ha256_tree_hash: str = Field(alias="SHA256TreeHash")
    archive_s_ha256_tree_hash: str = Field(alias="ArchiveSHA256TreeHash")
    retrieval_byte_range: str = Field(alias="RetrievalByteRange")
    tier: str = Field(alias="Tier")
    inventory_retrieval_parameters: InventoryRetrievalJobDescriptionModel = Field(
        alias="InventoryRetrievalParameters"
    )
    job_output_path: str = Field(alias="JobOutputPath")
    select_parameters: SelectParametersModel = Field(alias="SelectParameters")
    output_location: OutputLocationModel = Field(alias="OutputLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlacierJobDescriptionModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_description: Optional[str] = Field(default=None, alias="JobDescription")
    action: Optional[
        Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"]
    ] = Field(default=None, alias="Action")
    archive_id: Optional[str] = Field(default=None, alias="ArchiveId")
    vault_arn: Optional[str] = Field(default=None, alias="VaultARN")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    completed: Optional[bool] = Field(default=None, alias="Completed")
    status_code: Optional[Literal["Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="StatusCode"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    archive_size_in_bytes: Optional[int] = Field(
        default=None, alias="ArchiveSizeInBytes"
    )
    inventory_size_in_bytes: Optional[int] = Field(
        default=None, alias="InventorySizeInBytes"
    )
    s_ns_topic: Optional[str] = Field(default=None, alias="SNSTopic")
    completion_date: Optional[str] = Field(default=None, alias="CompletionDate")
    s_ha256_tree_hash: Optional[str] = Field(default=None, alias="SHA256TreeHash")
    archive_s_ha256_tree_hash: Optional[str] = Field(
        default=None, alias="ArchiveSHA256TreeHash"
    )
    retrieval_byte_range: Optional[str] = Field(
        default=None, alias="RetrievalByteRange"
    )
    tier: Optional[str] = Field(default=None, alias="Tier")
    inventory_retrieval_parameters: Optional[
        InventoryRetrievalJobDescriptionModel
    ] = Field(default=None, alias="InventoryRetrievalParameters")
    job_output_path: Optional[str] = Field(default=None, alias="JobOutputPath")
    select_parameters: Optional[SelectParametersModel] = Field(
        default=None, alias="SelectParameters"
    )
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )


class JobParametersModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    type: Optional[str] = Field(default=None, alias="Type")
    archive_id: Optional[str] = Field(default=None, alias="ArchiveId")
    description: Optional[str] = Field(default=None, alias="Description")
    s_ns_topic: Optional[str] = Field(default=None, alias="SNSTopic")
    retrieval_byte_range: Optional[str] = Field(
        default=None, alias="RetrievalByteRange"
    )
    tier: Optional[str] = Field(default=None, alias="Tier")
    inventory_retrieval_parameters: Optional[InventoryRetrievalJobInputModel] = Field(
        default=None, alias="InventoryRetrievalParameters"
    )
    select_parameters: Optional[SelectParametersModel] = Field(
        default=None, alias="SelectParameters"
    )
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )


class ListJobsOutputModel(BaseModel):
    job_list: List[GlacierJobDescriptionModel] = Field(alias="JobList")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateJobInputRequestModel(BaseModel):
    vault_name: str = Field(alias="vaultName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    job_parameters: Optional[JobParametersModel] = Field(
        default=None, alias="jobParameters"
    )
