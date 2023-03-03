# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelJournalKinesisStreamRequestModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    stream_id: str = Field(alias="StreamId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLedgerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    permissions_mode: Literal["ALLOW_ALL", "STANDARD"] = Field(alias="PermissionsMode")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")


class DeleteLedgerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeJournalKinesisStreamRequestModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    stream_id: str = Field(alias="StreamId")


class DescribeJournalS3ExportRequestModel(BaseModel):
    name: str = Field(alias="Name")
    export_id: str = Field(alias="ExportId")


class DescribeLedgerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class LedgerEncryptionDescriptionModel(BaseModel):
    kms_key_arn: str = Field(alias="KmsKeyArn")
    encryption_status: Literal["ENABLED", "KMS_KEY_INACCESSIBLE", "UPDATING"] = Field(
        alias="EncryptionStatus"
    )
    inaccessible_kms_key_date_time: Optional[datetime] = Field(
        default=None, alias="InaccessibleKmsKeyDateTime"
    )


class ValueHolderModel(BaseModel):
    ion_text: Optional[str] = Field(default=None, alias="IonText")


class GetDigestRequestModel(BaseModel):
    name: str = Field(alias="Name")


class KinesisConfigurationModel(BaseModel):
    stream_arn: str = Field(alias="StreamArn")
    aggregation_enabled: Optional[bool] = Field(
        default=None, alias="AggregationEnabled"
    )


class LedgerSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]] = Field(
        default=None, alias="State"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )


class ListJournalKinesisStreamsForLedgerRequestModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJournalS3ExportsForLedgerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJournalS3ExportsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLedgersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class S3EncryptionConfigurationModel(BaseModel):
    object_encryption_type: Literal["NO_ENCRYPTION", "SSE_KMS", "SSE_S3"] = Field(
        alias="ObjectEncryptionType"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateLedgerPermissionsModeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    permissions_mode: Literal["ALLOW_ALL", "STANDARD"] = Field(alias="PermissionsMode")


class UpdateLedgerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")


class CancelJournalKinesisStreamResponseModel(BaseModel):
    stream_id: str = Field(alias="StreamId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLedgerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    permissions_mode: Literal["ALLOW_ALL", "STANDARD"] = Field(alias="PermissionsMode")
    deletion_protection: bool = Field(alias="DeletionProtection")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportJournalToS3ResponseModel(BaseModel):
    export_id: str = Field(alias="ExportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamJournalToKinesisResponseModel(BaseModel):
    stream_id: str = Field(alias="StreamId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLedgerPermissionsModeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    permissions_mode: Literal["ALLOW_ALL", "STANDARD"] = Field(alias="PermissionsMode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLedgerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    permissions_mode: Literal["ALLOW_ALL", "STANDARD"] = Field(alias="PermissionsMode")
    deletion_protection: bool = Field(alias="DeletionProtection")
    encryption_description: LedgerEncryptionDescriptionModel = Field(
        alias="EncryptionDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLedgerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    deletion_protection: bool = Field(alias="DeletionProtection")
    encryption_description: LedgerEncryptionDescriptionModel = Field(
        alias="EncryptionDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlockRequestModel(BaseModel):
    name: str = Field(alias="Name")
    block_address: ValueHolderModel = Field(alias="BlockAddress")
    digest_tip_address: Optional[ValueHolderModel] = Field(
        default=None, alias="DigestTipAddress"
    )


class GetBlockResponseModel(BaseModel):
    block: ValueHolderModel = Field(alias="Block")
    proof: ValueHolderModel = Field(alias="Proof")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDigestResponseModel(BaseModel):
    digest: bytes = Field(alias="Digest")
    digest_tip_address: ValueHolderModel = Field(alias="DigestTipAddress")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRevisionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    block_address: ValueHolderModel = Field(alias="BlockAddress")
    document_id: str = Field(alias="DocumentId")
    digest_tip_address: Optional[ValueHolderModel] = Field(
        default=None, alias="DigestTipAddress"
    )


class GetRevisionResponseModel(BaseModel):
    proof: ValueHolderModel = Field(alias="Proof")
    revision: ValueHolderModel = Field(alias="Revision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JournalKinesisStreamDescriptionModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    role_arn: str = Field(alias="RoleArn")
    stream_id: str = Field(alias="StreamId")
    status: Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "IMPAIRED"] = Field(
        alias="Status"
    )
    kinesis_configuration: KinesisConfigurationModel = Field(
        alias="KinesisConfiguration"
    )
    stream_name: str = Field(alias="StreamName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    inclusive_start_time: Optional[datetime] = Field(
        default=None, alias="InclusiveStartTime"
    )
    exclusive_end_time: Optional[datetime] = Field(
        default=None, alias="ExclusiveEndTime"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    error_cause: Optional[
        Literal["IAM_PERMISSION_REVOKED", "KINESIS_STREAM_NOT_FOUND"]
    ] = Field(default=None, alias="ErrorCause")


class StreamJournalToKinesisRequestModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    role_arn: str = Field(alias="RoleArn")
    inclusive_start_time: Union[datetime, str] = Field(alias="InclusiveStartTime")
    kinesis_configuration: KinesisConfigurationModel = Field(
        alias="KinesisConfiguration"
    )
    stream_name: str = Field(alias="StreamName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    exclusive_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExclusiveEndTime"
    )


class ListLedgersResponseModel(BaseModel):
    ledgers: List[LedgerSummaryModel] = Field(alias="Ledgers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3ExportConfigurationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    prefix: str = Field(alias="Prefix")
    encryption_configuration: S3EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )


class DescribeJournalKinesisStreamResponseModel(BaseModel):
    stream: JournalKinesisStreamDescriptionModel = Field(alias="Stream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJournalKinesisStreamsForLedgerResponseModel(BaseModel):
    streams: List[JournalKinesisStreamDescriptionModel] = Field(alias="Streams")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportJournalToS3RequestModel(BaseModel):
    name: str = Field(alias="Name")
    inclusive_start_time: Union[datetime, str] = Field(alias="InclusiveStartTime")
    exclusive_end_time: Union[datetime, str] = Field(alias="ExclusiveEndTime")
    s3_export_configuration: S3ExportConfigurationModel = Field(
        alias="S3ExportConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    output_format: Optional[Literal["ION_BINARY", "ION_TEXT", "JSON"]] = Field(
        default=None, alias="OutputFormat"
    )


class JournalS3ExportDescriptionModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")
    export_id: str = Field(alias="ExportId")
    export_creation_time: datetime = Field(alias="ExportCreationTime")
    status: Literal["CANCELLED", "COMPLETED", "IN_PROGRESS"] = Field(alias="Status")
    inclusive_start_time: datetime = Field(alias="InclusiveStartTime")
    exclusive_end_time: datetime = Field(alias="ExclusiveEndTime")
    s3_export_configuration: S3ExportConfigurationModel = Field(
        alias="S3ExportConfiguration"
    )
    role_arn: str = Field(alias="RoleArn")
    output_format: Optional[Literal["ION_BINARY", "ION_TEXT", "JSON"]] = Field(
        default=None, alias="OutputFormat"
    )


class DescribeJournalS3ExportResponseModel(BaseModel):
    export_description: JournalS3ExportDescriptionModel = Field(
        alias="ExportDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJournalS3ExportsForLedgerResponseModel(BaseModel):
    journal_s3_exports: List[JournalS3ExportDescriptionModel] = Field(
        alias="JournalS3Exports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJournalS3ExportsResponseModel(BaseModel):
    journal_s3_exports: List[JournalS3ExportDescriptionModel] = Field(
        alias="JournalS3Exports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
