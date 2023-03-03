# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Callable,
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

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AbortIncompleteMultipartUploadModel(BaseModel):
    days_after_initiation: Optional[int] = Field(
        default=None, alias="DaysAfterInitiation"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AbortMultipartUploadRequestMultipartUploadAbortModel(BaseModel):
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class AbortMultipartUploadRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class AccelerateConfigurationModel(BaseModel):
    status: Optional[Literal["Enabled", "Suspended"]] = Field(
        default=None, alias="Status"
    )


class OwnerModel(BaseModel):
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    id: Optional[str] = Field(default=None, alias="ID")


class AccessControlTranslationModel(BaseModel):
    owner: Literal["Destination"] = Field(alias="Owner")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AnalyticsS3BucketDestinationModel(BaseModel):
    format: Literal["CSV"] = Field(alias="Format")
    bucket: str = Field(alias="Bucket")
    bucket_account_id: Optional[str] = Field(default=None, alias="BucketAccountId")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class CopySourceModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class BucketDownloadFileRequestModel(BaseModel):
    key: str = Field(alias="Key")
    filename: str = Field(alias="Filename")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class BucketDownloadFileobjRequestModel(BaseModel):
    key: str = Field(alias="Key")
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class BucketObjectRequestModel(BaseModel):
    key: str = Field(alias="key")


class BucketModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")


class BucketUploadFileRequestModel(BaseModel):
    filename: str = Field(alias="Filename")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class BucketUploadFileobjRequestModel(BaseModel):
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class CORSRuleModel(BaseModel):
    allowed_methods: List[str] = Field(alias="AllowedMethods")
    allowed_origins: List[str] = Field(alias="AllowedOrigins")
    id: Optional[str] = Field(default=None, alias="ID")
    allowed_headers: Optional[List[str]] = Field(default=None, alias="AllowedHeaders")
    expose_headers: Optional[List[str]] = Field(default=None, alias="ExposeHeaders")
    max_age_seconds: Optional[int] = Field(default=None, alias="MaxAgeSeconds")


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
    allow_quoted_record_delimiter: Optional[bool] = Field(
        default=None, alias="AllowQuotedRecordDelimiter"
    )


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


class ChecksumModel(BaseModel):
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")


class ClientDownloadFileRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    filename: str = Field(alias="Filename")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ClientDownloadFileobjRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ClientGeneratePresignedPostRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    fields: Optional[Dict[str, Any]] = Field(default=None, alias="Fields")
    conditions: Optional[List[Any]] = Field(default=None, alias="Conditions")
    expires_in: Optional[int] = Field(default=None, alias="ExpiresIn")


class ClientUploadFileRequestModel(BaseModel):
    filename: str = Field(alias="Filename")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ClientUploadFileobjRequestModel(BaseModel):
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class CloudFunctionConfigurationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    event: Optional[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(default=None, alias="Event")
    events: Optional[
        List[
            Literal[
                "s3:IntelligentTiering",
                "s3:LifecycleExpiration:*",
                "s3:LifecycleExpiration:Delete",
                "s3:LifecycleExpiration:DeleteMarkerCreated",
                "s3:LifecycleTransition",
                "s3:ObjectAcl:Put",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Put",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Completed",
                "s3:ObjectRestore:Delete",
                "s3:ObjectRestore:Post",
                "s3:ObjectTagging:*",
                "s3:ObjectTagging:Delete",
                "s3:ObjectTagging:Put",
                "s3:ReducedRedundancyLostObject",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ]
    ] = Field(default=None, alias="Events")
    cloud_function: Optional[str] = Field(default=None, alias="CloudFunction")
    invocation_role: Optional[str] = Field(default=None, alias="InvocationRole")


class CommonPrefixModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class CompletedPartModel(BaseModel):
    etag: Optional[str] = Field(default=None, alias="ETag")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    part_number: Optional[int] = Field(default=None, alias="PartNumber")


class ConditionModel(BaseModel):
    http_error_code_returned_equals: Optional[str] = Field(
        default=None, alias="HttpErrorCodeReturnedEquals"
    )
    key_prefix_equals: Optional[str] = Field(default=None, alias="KeyPrefixEquals")


class CopyObjectResultModel(BaseModel):
    etag: Optional[str] = Field(default=None, alias="ETag")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")


class CopyObjectRequestObjectCopyFromModel(BaseModel):
    copy_source: str = Field(alias="CopySource")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    copy_source_if_match: Optional[str] = Field(default=None, alias="CopySourceIfMatch")
    copy_source_if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfModifiedSince"
    )
    copy_source_if_none_match: Optional[str] = Field(
        default=None, alias="CopySourceIfNoneMatch"
    )
    copy_source_if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfUnmodifiedSince"
    )
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    metadata_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="MetadataDirective"
    )
    tagging_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="TaggingDirective"
    )
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    copy_source_s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerAlgorithm"
    )
    copy_source_s_s_ecustomer_key: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKey"
    )
    copy_source_s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    expected_source_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedSourceBucketOwner"
    )


class CopyObjectRequestObjectSummaryCopyFromModel(BaseModel):
    copy_source: str = Field(alias="CopySource")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    copy_source_if_match: Optional[str] = Field(default=None, alias="CopySourceIfMatch")
    copy_source_if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfModifiedSince"
    )
    copy_source_if_none_match: Optional[str] = Field(
        default=None, alias="CopySourceIfNoneMatch"
    )
    copy_source_if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfUnmodifiedSince"
    )
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    metadata_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="MetadataDirective"
    )
    tagging_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="TaggingDirective"
    )
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    copy_source_s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerAlgorithm"
    )
    copy_source_s_s_ecustomer_key: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKey"
    )
    copy_source_s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    expected_source_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedSourceBucketOwner"
    )


class CopyPartResultModel(BaseModel):
    etag: Optional[str] = Field(default=None, alias="ETag")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")


class CreateBucketConfigurationModel(BaseModel):
    location_constraint: Optional[
        Literal[
            "EU",
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "ca-central-1",
            "cn-north-1",
            "cn-northwest-1",
            "eu-central-1",
            "eu-north-1",
            "eu-south-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-south-1",
            "sa-east-1",
            "us-east-2",
            "us-gov-east-1",
            "us-gov-west-1",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="LocationConstraint")


class CreateMultipartUploadRequestObjectInitiateMultipartUploadModel(BaseModel):
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadModel(BaseModel):
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class CreateMultipartUploadRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class DefaultRetentionModel(BaseModel):
    mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="Mode"
    )
    days: Optional[int] = Field(default=None, alias="Days")
    years: Optional[int] = Field(default=None, alias="Years")


class DeleteBucketAnalyticsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketCorsRequestBucketCorsDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketCorsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketEncryptionRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketIntelligentTieringConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")


class DeleteBucketInventoryConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketLifecycleRequestBucketLifecycleDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketLifecycleRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketMetricsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketOwnershipControlsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketPolicyRequestBucketPolicyDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketPolicyRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketReplicationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketRequestBucketDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketTaggingRequestBucketTaggingDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketWebsiteRequestBucketWebsiteDeleteModel(BaseModel):
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteBucketWebsiteRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteMarkerReplicationModel(BaseModel):
    status: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="Status"
    )


class DeleteObjectRequestObjectDeleteModel(BaseModel):
    mfa: Optional[str] = Field(default=None, alias="MFA")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteObjectRequestObjectSummaryDeleteModel(BaseModel):
    mfa: Optional[str] = Field(default=None, alias="MFA")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteObjectRequestObjectVersionDeleteModel(BaseModel):
    mfa: Optional[str] = Field(default=None, alias="MFA")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    mfa: Optional[str] = Field(default=None, alias="MFA")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeleteObjectTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class DeletedObjectModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    delete_marker: Optional[bool] = Field(default=None, alias="DeleteMarker")
    delete_marker_version_id: Optional[str] = Field(
        default=None, alias="DeleteMarkerVersionId"
    )


class ErrorModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class DeletePublicAccessBlockRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ObjectIdentifierModel(BaseModel):
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class EncryptionConfigurationModel(BaseModel):
    replica_kms_key_id: Optional[str] = Field(default=None, alias="ReplicaKmsKeyID")


class EncryptionModel(BaseModel):
    encryption_type: Literal["AES256", "aws:kms"] = Field(alias="EncryptionType")
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    kms_context: Optional[str] = Field(default=None, alias="KMSContext")


class ErrorDocumentModel(BaseModel):
    key: str = Field(alias="Key")


class ExistingObjectReplicationModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")


class FilterRuleModel(BaseModel):
    name: Optional[Literal["prefix", "suffix"]] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class GetBucketAccelerateConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketAclRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketAnalyticsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketCorsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketEncryptionRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketIntelligentTieringConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")


class GetBucketInventoryConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketLifecycleConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketLifecycleRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketLocationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketLoggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketMetricsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketNotificationConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketOwnershipControlsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketPolicyRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PolicyStatusModel(BaseModel):
    is_public: Optional[bool] = Field(default=None, alias="IsPublic")


class GetBucketPolicyStatusRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketReplicationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketRequestPaymentRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketVersioningRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class IndexDocumentModel(BaseModel):
    suffix: str = Field(alias="Suffix")


class RedirectAllRequestsToModel(BaseModel):
    host_name: str = Field(alias="HostName")
    protocol: Optional[Literal["http", "https"]] = Field(default=None, alias="Protocol")


class GetBucketWebsiteRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetObjectAclRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ObjectPartModel(BaseModel):
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    size: Optional[int] = Field(default=None, alias="Size")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")


class GetObjectAttributesRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    object_attributes: Sequence[
        Literal["Checksum", "ETag", "ObjectParts", "ObjectSize", "StorageClass"]
    ] = Field(alias="ObjectAttributes")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    max_parts: Optional[int] = Field(default=None, alias="MaxParts")
    part_number_marker: Optional[int] = Field(default=None, alias="PartNumberMarker")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ObjectLockLegalHoldModel(BaseModel):
    status: Optional[Literal["OFF", "ON"]] = Field(default=None, alias="Status")


class GetObjectLegalHoldRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetObjectLockConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetObjectRequestObjectGetModel(BaseModel):
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    response_cache_control: Optional[str] = Field(
        default=None, alias="ResponseCacheControl"
    )
    response_content_disposition: Optional[str] = Field(
        default=None, alias="ResponseContentDisposition"
    )
    response_content_encoding: Optional[str] = Field(
        default=None, alias="ResponseContentEncoding"
    )
    response_content_language: Optional[str] = Field(
        default=None, alias="ResponseContentLanguage"
    )
    response_content_type: Optional[str] = Field(
        default=None, alias="ResponseContentType"
    )
    response_expires: Optional[Union[datetime, str]] = Field(
        default=None, alias="ResponseExpires"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class GetObjectRequestObjectSummaryGetModel(BaseModel):
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    response_cache_control: Optional[str] = Field(
        default=None, alias="ResponseCacheControl"
    )
    response_content_disposition: Optional[str] = Field(
        default=None, alias="ResponseContentDisposition"
    )
    response_content_encoding: Optional[str] = Field(
        default=None, alias="ResponseContentEncoding"
    )
    response_content_language: Optional[str] = Field(
        default=None, alias="ResponseContentLanguage"
    )
    response_content_type: Optional[str] = Field(
        default=None, alias="ResponseContentType"
    )
    response_expires: Optional[Union[datetime, str]] = Field(
        default=None, alias="ResponseExpires"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class GetObjectRequestObjectVersionGetModel(BaseModel):
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    response_cache_control: Optional[str] = Field(
        default=None, alias="ResponseCacheControl"
    )
    response_content_disposition: Optional[str] = Field(
        default=None, alias="ResponseContentDisposition"
    )
    response_content_encoding: Optional[str] = Field(
        default=None, alias="ResponseContentEncoding"
    )
    response_content_language: Optional[str] = Field(
        default=None, alias="ResponseContentLanguage"
    )
    response_content_type: Optional[str] = Field(
        default=None, alias="ResponseContentType"
    )
    response_expires: Optional[Union[datetime, str]] = Field(
        default=None, alias="ResponseExpires"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class GetObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    response_cache_control: Optional[str] = Field(
        default=None, alias="ResponseCacheControl"
    )
    response_content_disposition: Optional[str] = Field(
        default=None, alias="ResponseContentDisposition"
    )
    response_content_encoding: Optional[str] = Field(
        default=None, alias="ResponseContentEncoding"
    )
    response_content_language: Optional[str] = Field(
        default=None, alias="ResponseContentLanguage"
    )
    response_content_type: Optional[str] = Field(
        default=None, alias="ResponseContentType"
    )
    response_expires: Optional[Union[datetime, str]] = Field(
        default=None, alias="ResponseExpires"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class ObjectLockRetentionModel(BaseModel):
    mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="Mode"
    )
    retain_until_date: Optional[datetime] = Field(default=None, alias="RetainUntilDate")


class GetObjectRetentionRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetObjectTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )


class GetObjectTorrentRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PublicAccessBlockConfigurationModel(BaseModel):
    block_public_acls: Optional[bool] = Field(default=None, alias="BlockPublicAcls")
    ignore_public_acls: Optional[bool] = Field(default=None, alias="IgnorePublicAcls")
    block_public_policy: Optional[bool] = Field(default=None, alias="BlockPublicPolicy")
    restrict_public_buckets: Optional[bool] = Field(
        default=None, alias="RestrictPublicBuckets"
    )


class GetPublicAccessBlockRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GlacierJobParametersModel(BaseModel):
    tier: Literal["Bulk", "Expedited", "Standard"] = Field(alias="Tier")


class GranteeModel(BaseModel):
    type: Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"] = Field(
        alias="Type"
    )
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    id: Optional[str] = Field(default=None, alias="ID")
    uri: Optional[str] = Field(default=None, alias="URI")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class HeadBucketRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class HeadObjectRequestObjectVersionHeadModel(BaseModel):
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class HeadObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )


class InitiatorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="ID")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class JSONInputModel(BaseModel):
    type: Optional[Literal["DOCUMENT", "LINES"]] = Field(default=None, alias="Type")


class TieringModel(BaseModel):
    days: int = Field(alias="Days")
    access_tier: Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"] = Field(
        alias="AccessTier"
    )


class InventoryFilterModel(BaseModel):
    prefix: str = Field(alias="Prefix")


class InventoryScheduleModel(BaseModel):
    frequency: Literal["Daily", "Weekly"] = Field(alias="Frequency")


class SSEKMSModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class JSONOutputModel(BaseModel):
    record_delimiter: Optional[str] = Field(default=None, alias="RecordDelimiter")


class LifecycleExpirationModel(BaseModel):
    date: Optional[datetime] = Field(default=None, alias="Date")
    days: Optional[int] = Field(default=None, alias="Days")
    expired_object_delete_marker: Optional[bool] = Field(
        default=None, alias="ExpiredObjectDeleteMarker"
    )


class NoncurrentVersionExpirationModel(BaseModel):
    noncurrent_days: Optional[int] = Field(default=None, alias="NoncurrentDays")
    newer_noncurrent_versions: Optional[int] = Field(
        default=None, alias="NewerNoncurrentVersions"
    )


class NoncurrentVersionTransitionModel(BaseModel):
    noncurrent_days: Optional[int] = Field(default=None, alias="NoncurrentDays")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    newer_noncurrent_versions: Optional[int] = Field(
        default=None, alias="NewerNoncurrentVersions"
    )


class TransitionModel(BaseModel):
    date: Optional[datetime] = Field(default=None, alias="Date")
    days: Optional[int] = Field(default=None, alias="Days")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")


class ListBucketAnalyticsConfigurationsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ListBucketIntelligentTieringConfigurationsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")


class ListBucketInventoryConfigurationsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ListBucketMetricsConfigurationsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListMultipartUploadsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    key_marker: Optional[str] = Field(default=None, alias="KeyMarker")
    max_uploads: Optional[int] = Field(default=None, alias="MaxUploads")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    upload_id_marker: Optional[str] = Field(default=None, alias="UploadIdMarker")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ListObjectVersionsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    key_marker: Optional[str] = Field(default=None, alias="KeyMarker")
    max_keys: Optional[int] = Field(default=None, alias="MaxKeys")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    version_id_marker: Optional[str] = Field(default=None, alias="VersionIdMarker")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ListObjectsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_keys: Optional[int] = Field(default=None, alias="MaxKeys")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ListObjectsV2RequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    max_keys: Optional[int] = Field(default=None, alias="MaxKeys")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")
    fetch_owner: Optional[bool] = Field(default=None, alias="FetchOwner")
    start_after: Optional[str] = Field(default=None, alias="StartAfter")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PartModel(BaseModel):
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    etag: Optional[str] = Field(default=None, alias="ETag")
    size: Optional[int] = Field(default=None, alias="Size")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")


class ListPartsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    max_parts: Optional[int] = Field(default=None, alias="MaxParts")
    part_number_marker: Optional[int] = Field(default=None, alias="PartNumberMarker")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )


class MetadataEntryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ReplicationTimeValueModel(BaseModel):
    minutes: Optional[int] = Field(default=None, alias="Minutes")


class MultipartUploadPartRequestModel(BaseModel):
    part_number: str = Field(alias="part_number")


class QueueConfigurationDeprecatedModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    event: Optional[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(default=None, alias="Event")
    events: Optional[
        List[
            Literal[
                "s3:IntelligentTiering",
                "s3:LifecycleExpiration:*",
                "s3:LifecycleExpiration:Delete",
                "s3:LifecycleExpiration:DeleteMarkerCreated",
                "s3:LifecycleTransition",
                "s3:ObjectAcl:Put",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Put",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Completed",
                "s3:ObjectRestore:Delete",
                "s3:ObjectRestore:Post",
                "s3:ObjectTagging:*",
                "s3:ObjectTagging:Delete",
                "s3:ObjectTagging:Put",
                "s3:ReducedRedundancyLostObject",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ]
    ] = Field(default=None, alias="Events")
    queue: Optional[str] = Field(default=None, alias="Queue")


class TopicConfigurationDeprecatedModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    events: Optional[
        List[
            Literal[
                "s3:IntelligentTiering",
                "s3:LifecycleExpiration:*",
                "s3:LifecycleExpiration:Delete",
                "s3:LifecycleExpiration:DeleteMarkerCreated",
                "s3:LifecycleTransition",
                "s3:ObjectAcl:Put",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Put",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Completed",
                "s3:ObjectRestore:Delete",
                "s3:ObjectRestore:Post",
                "s3:ObjectTagging:*",
                "s3:ObjectTagging:Delete",
                "s3:ObjectTagging:Put",
                "s3:ReducedRedundancyLostObject",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ]
    ] = Field(default=None, alias="Events")
    event: Optional[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(default=None, alias="Event")
    topic: Optional[str] = Field(default=None, alias="Topic")


class ObjectDownloadFileRequestModel(BaseModel):
    filename: str = Field(alias="Filename")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ObjectDownloadFileobjRequestModel(BaseModel):
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ObjectMultipartUploadRequestModel(BaseModel):
    id: str = Field(alias="id")


class ObjectSummaryMultipartUploadRequestModel(BaseModel):
    id: str = Field(alias="id")


class ObjectSummaryVersionRequestModel(BaseModel):
    id: str = Field(alias="id")


class ObjectUploadFileRequestModel(BaseModel):
    filename: str = Field(alias="Filename")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ObjectUploadFileobjRequestModel(BaseModel):
    fileobj: Union[Type[IO[Any]], Type[StreamingBody]] = Field(alias="Fileobj")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ObjectVersionRequestModel(BaseModel):
    id: str = Field(alias="id")


class OwnershipControlsRuleModel(BaseModel):
    object_ownership: Literal[
        "BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"
    ] = Field(alias="ObjectOwnership")


class ProgressModel(BaseModel):
    bytes_scanned: Optional[int] = Field(default=None, alias="BytesScanned")
    bytes_processed: Optional[int] = Field(default=None, alias="BytesProcessed")
    bytes_returned: Optional[int] = Field(default=None, alias="BytesReturned")


class PutBucketPolicyRequestBucketPolicyPutModel(BaseModel):
    policy: str = Field(alias="Policy")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    confirm_remove_self_bucket_access: Optional[bool] = Field(
        default=None, alias="ConfirmRemoveSelfBucketAccess"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketPolicyRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    policy: str = Field(alias="Policy")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    confirm_remove_self_bucket_access: Optional[bool] = Field(
        default=None, alias="ConfirmRemoveSelfBucketAccess"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class RequestPaymentConfigurationModel(BaseModel):
    payer: Literal["BucketOwner", "Requester"] = Field(alias="Payer")


class PutBucketVersioningRequestBucketVersioningEnableModel(BaseModel):
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    mfa: Optional[str] = Field(default=None, alias="MFA")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class VersioningConfigurationModel(BaseModel):
    mfadelete: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="MFADelete"
    )
    status: Optional[Literal["Enabled", "Suspended"]] = Field(
        default=None, alias="Status"
    )


class PutBucketVersioningRequestBucketVersioningSuspendModel(BaseModel):
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    mfa: Optional[str] = Field(default=None, alias="MFA")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectRequestBucketPutObjectModel(BaseModel):
    key: str = Field(alias="Key")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectRequestObjectPutModel(BaseModel):
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectRequestObjectSummaryPutModel(BaseModel):
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class RecordsEventModel(BaseModel):
    payload: Optional[bytes] = Field(default=None, alias="Payload")


class RedirectModel(BaseModel):
    host_name: Optional[str] = Field(default=None, alias="HostName")
    http_redirect_code: Optional[str] = Field(default=None, alias="HttpRedirectCode")
    protocol: Optional[Literal["http", "https"]] = Field(default=None, alias="Protocol")
    replace_key_prefix_with: Optional[str] = Field(
        default=None, alias="ReplaceKeyPrefixWith"
    )
    replace_key_with: Optional[str] = Field(default=None, alias="ReplaceKeyWith")


class ReplicaModificationsModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")


class RequestProgressModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ScanRangeModel(BaseModel):
    start: Optional[int] = Field(default=None, alias="Start")
    end: Optional[int] = Field(default=None, alias="End")


class ServerSideEncryptionByDefaultModel(BaseModel):
    s_s_ealgorithm: Literal["AES256", "aws:kms"] = Field(alias="SSEAlgorithm")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyID")


class ServiceResourceBucketAclRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketCorsRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketLifecycleConfigurationRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketLifecycleRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketLoggingRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketNotificationRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketPolicyRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketRequestPaymentRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketRequestModel(BaseModel):
    name: str = Field(alias="name")


class ServiceResourceBucketTaggingRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketVersioningRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceBucketWebsiteRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")


class ServiceResourceMultipartUploadPartRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    object_key: str = Field(alias="object_key")
    multipart_upload_id: str = Field(alias="multipart_upload_id")
    part_number: str = Field(alias="part_number")


class ServiceResourceMultipartUploadRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    object_key: str = Field(alias="object_key")
    id: str = Field(alias="id")


class ServiceResourceObjectAclRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    object_key: str = Field(alias="object_key")


class ServiceResourceObjectRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    key: str = Field(alias="key")


class ServiceResourceObjectSummaryRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    key: str = Field(alias="key")


class ServiceResourceObjectVersionRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucket_name")
    object_key: str = Field(alias="object_key")
    id: str = Field(alias="id")


class SseKmsEncryptedObjectsModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")


class StatsModel(BaseModel):
    bytes_scanned: Optional[int] = Field(default=None, alias="BytesScanned")
    bytes_processed: Optional[int] = Field(default=None, alias="BytesProcessed")
    bytes_returned: Optional[int] = Field(default=None, alias="BytesReturned")


class UploadPartRequestMultipartUploadPartUploadModel(BaseModel):
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class UploadPartRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    part_number: int = Field(alias="PartNumber")
    upload_id: str = Field(alias="UploadId")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class WriteGetObjectResponseRequestModel(BaseModel):
    request_route: str = Field(alias="RequestRoute")
    request_token: str = Field(alias="RequestToken")
    body: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Body"
    )
    status_code: Optional[int] = Field(default=None, alias="StatusCode")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    accept_ranges: Optional[str] = Field(default=None, alias="AcceptRanges")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_range: Optional[str] = Field(default=None, alias="ContentRange")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    delete_marker: Optional[bool] = Field(default=None, alias="DeleteMarker")
    etag: Optional[str] = Field(default=None, alias="ETag")
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    expiration: Optional[str] = Field(default=None, alias="Expiration")
    last_modified: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModified"
    )
    missing_meta: Optional[int] = Field(default=None, alias="MissingMeta")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    parts_count: Optional[int] = Field(default=None, alias="PartsCount")
    replication_status: Optional[
        Literal["COMPLETE", "FAILED", "PENDING", "REPLICA"]
    ] = Field(default=None, alias="ReplicationStatus")
    request_charged: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestCharged"
    )
    restore: Optional[str] = Field(default=None, alias="Restore")
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    tag_count: Optional[int] = Field(default=None, alias="TagCount")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")


class AbortMultipartUploadOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompleteMultipartUploadOutputModel(BaseModel):
    location: str = Field(alias="Location")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    expiration: str = Field(alias="Expiration")
    etag: str = Field(alias="ETag")
    checksum_crc32: str = Field(alias="ChecksumCRC32")
    checksum_crc32_c: str = Field(alias="ChecksumCRC32C")
    checksum_s_ha1: str = Field(alias="ChecksumSHA1")
    checksum_s_ha256: str = Field(alias="ChecksumSHA256")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    version_id: str = Field(alias="VersionId")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBucketOutputModel(BaseModel):
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMultipartUploadOutputModel(BaseModel):
    abort_date: datetime = Field(alias="AbortDate")
    abort_rule_id: str = Field(alias="AbortRuleId")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: str = Field(alias="SSEKMSEncryptionContext")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    checksum_algorithm: Literal["CRC32", "CRC32C", "SHA1", "SHA256"] = Field(
        alias="ChecksumAlgorithm"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteObjectOutputModel(BaseModel):
    delete_marker: bool = Field(alias="DeleteMarker")
    version_id: str = Field(alias="VersionId")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteObjectTaggingOutputModel(BaseModel):
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ErrorDocumentResponseMetadataModel(BaseModel):
    key: str = Field(alias="Key")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketAccelerateConfigurationOutputModel(BaseModel):
    status: Literal["Enabled", "Suspended"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketLocationOutputModel(BaseModel):
    location_constraint: Literal[
        "EU",
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-north-1",
        "eu-south-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-south-1",
        "sa-east-1",
        "us-east-2",
        "us-gov-east-1",
        "us-gov-west-1",
        "us-west-1",
        "us-west-2",
    ] = Field(alias="LocationConstraint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketPolicyOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketRequestPaymentOutputModel(BaseModel):
    payer: Literal["BucketOwner", "Requester"] = Field(alias="Payer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketVersioningOutputModel(BaseModel):
    status: Literal["Enabled", "Suspended"] = Field(alias="Status")
    mfadelete: Literal["Disabled", "Enabled"] = Field(alias="MFADelete")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectOutputModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    delete_marker: bool = Field(alias="DeleteMarker")
    accept_ranges: str = Field(alias="AcceptRanges")
    expiration: str = Field(alias="Expiration")
    restore: str = Field(alias="Restore")
    last_modified: datetime = Field(alias="LastModified")
    content_length: int = Field(alias="ContentLength")
    etag: str = Field(alias="ETag")
    checksum_crc32: str = Field(alias="ChecksumCRC32")
    checksum_crc32_c: str = Field(alias="ChecksumCRC32C")
    checksum_s_ha1: str = Field(alias="ChecksumSHA1")
    checksum_s_ha256: str = Field(alias="ChecksumSHA256")
    missing_meta: int = Field(alias="MissingMeta")
    version_id: str = Field(alias="VersionId")
    cache_control: str = Field(alias="CacheControl")
    content_disposition: str = Field(alias="ContentDisposition")
    content_encoding: str = Field(alias="ContentEncoding")
    content_language: str = Field(alias="ContentLanguage")
    content_range: str = Field(alias="ContentRange")
    content_type: str = Field(alias="ContentType")
    expires: datetime = Field(alias="Expires")
    website_redirect_location: str = Field(alias="WebsiteRedirectLocation")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    metadata: Dict[str, str] = Field(alias="Metadata")
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    storage_class: Literal[
        "DEEP_ARCHIVE",
        "GLACIER",
        "GLACIER_IR",
        "INTELLIGENT_TIERING",
        "ONEZONE_IA",
        "OUTPOSTS",
        "REDUCED_REDUNDANCY",
        "STANDARD",
        "STANDARD_IA",
    ] = Field(alias="StorageClass")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    replication_status: Literal["COMPLETE", "FAILED", "PENDING", "REPLICA"] = Field(
        alias="ReplicationStatus"
    )
    parts_count: int = Field(alias="PartsCount")
    tag_count: int = Field(alias="TagCount")
    object_lock_mode: Literal["COMPLIANCE", "GOVERNANCE"] = Field(
        alias="ObjectLockMode"
    )
    object_lock_retain_until_date: datetime = Field(alias="ObjectLockRetainUntilDate")
    object_lock_legal_hold_status: Literal["OFF", "ON"] = Field(
        alias="ObjectLockLegalHoldStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectTorrentOutputModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HeadObjectOutputModel(BaseModel):
    delete_marker: bool = Field(alias="DeleteMarker")
    accept_ranges: str = Field(alias="AcceptRanges")
    expiration: str = Field(alias="Expiration")
    restore: str = Field(alias="Restore")
    archive_status: Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"] = Field(
        alias="ArchiveStatus"
    )
    last_modified: datetime = Field(alias="LastModified")
    content_length: int = Field(alias="ContentLength")
    checksum_crc32: str = Field(alias="ChecksumCRC32")
    checksum_crc32_c: str = Field(alias="ChecksumCRC32C")
    checksum_s_ha1: str = Field(alias="ChecksumSHA1")
    checksum_s_ha256: str = Field(alias="ChecksumSHA256")
    etag: str = Field(alias="ETag")
    missing_meta: int = Field(alias="MissingMeta")
    version_id: str = Field(alias="VersionId")
    cache_control: str = Field(alias="CacheControl")
    content_disposition: str = Field(alias="ContentDisposition")
    content_encoding: str = Field(alias="ContentEncoding")
    content_language: str = Field(alias="ContentLanguage")
    content_type: str = Field(alias="ContentType")
    expires: datetime = Field(alias="Expires")
    website_redirect_location: str = Field(alias="WebsiteRedirectLocation")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    metadata: Dict[str, str] = Field(alias="Metadata")
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    storage_class: Literal[
        "DEEP_ARCHIVE",
        "GLACIER",
        "GLACIER_IR",
        "INTELLIGENT_TIERING",
        "ONEZONE_IA",
        "OUTPOSTS",
        "REDUCED_REDUNDANCY",
        "STANDARD",
        "STANDARD_IA",
    ] = Field(alias="StorageClass")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    replication_status: Literal["COMPLETE", "FAILED", "PENDING", "REPLICA"] = Field(
        alias="ReplicationStatus"
    )
    parts_count: int = Field(alias="PartsCount")
    object_lock_mode: Literal["COMPLIANCE", "GOVERNANCE"] = Field(
        alias="ObjectLockMode"
    )
    object_lock_retain_until_date: datetime = Field(alias="ObjectLockRetainUntilDate")
    object_lock_legal_hold_status: Literal["OFF", "ON"] = Field(
        alias="ObjectLockLegalHoldStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IndexDocumentResponseMetadataModel(BaseModel):
    suffix: str = Field(alias="Suffix")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiatorResponseMetadataModel(BaseModel):
    id: str = Field(alias="ID")
    display_name: str = Field(alias="DisplayName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OwnerResponseMetadataModel(BaseModel):
    display_name: str = Field(alias="DisplayName")
    id: str = Field(alias="ID")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectAclOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectLegalHoldOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectLockConfigurationOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectOutputModel(BaseModel):
    expiration: str = Field(alias="Expiration")
    etag: str = Field(alias="ETag")
    checksum_crc32: str = Field(alias="ChecksumCRC32")
    checksum_crc32_c: str = Field(alias="ChecksumCRC32C")
    checksum_s_ha1: str = Field(alias="ChecksumSHA1")
    checksum_s_ha256: str = Field(alias="ChecksumSHA256")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    version_id: str = Field(alias="VersionId")
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: str = Field(alias="SSEKMSEncryptionContext")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectRetentionOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectTaggingOutputModel(BaseModel):
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RedirectAllRequestsToResponseMetadataModel(BaseModel):
    host_name: str = Field(alias="HostName")
    protocol: Literal["http", "https"] = Field(alias="Protocol")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreObjectOutputModel(BaseModel):
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    restore_output_path: str = Field(alias="RestoreOutputPath")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadPartOutputModel(BaseModel):
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    etag: str = Field(alias="ETag")
    checksum_crc32: str = Field(alias="ChecksumCRC32")
    checksum_crc32_c: str = Field(alias="ChecksumCRC32C")
    checksum_s_ha1: str = Field(alias="ChecksumSHA1")
    checksum_s_ha256: str = Field(alias="ChecksumSHA256")
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketAccelerateConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    accelerate_configuration: AccelerateConfigurationModel = Field(
        alias="AccelerateConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class DeleteMarkerEntryModel(BaseModel):
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")
    key: Optional[str] = Field(default=None, alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    is_latest: Optional[bool] = Field(default=None, alias="IsLatest")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")


class ObjectModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    etag: Optional[str] = Field(default=None, alias="ETag")
    checksum_algorithm: Optional[
        List[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]]
    ] = Field(default=None, alias="ChecksumAlgorithm")
    size: Optional[int] = Field(default=None, alias="Size")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")


class ObjectVersionModel(BaseModel):
    etag: Optional[str] = Field(default=None, alias="ETag")
    checksum_algorithm: Optional[
        List[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]]
    ] = Field(default=None, alias="ChecksumAlgorithm")
    size: Optional[int] = Field(default=None, alias="Size")
    storage_class: Optional[Literal["STANDARD"]] = Field(
        default=None, alias="StorageClass"
    )
    key: Optional[str] = Field(default=None, alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    is_latest: Optional[bool] = Field(default=None, alias="IsLatest")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")


class AnalyticsAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class GetBucketTaggingOutputModel(BaseModel):
    tag_set: List[TagModel] = Field(alias="TagSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectTaggingOutputModel(BaseModel):
    version_id: str = Field(alias="VersionId")
    tag_set: List[TagModel] = Field(alias="TagSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IntelligentTieringAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class LifecycleRuleAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    object_size_greater_than: Optional[int] = Field(
        default=None, alias="ObjectSizeGreaterThan"
    )
    object_size_less_than: Optional[int] = Field(
        default=None, alias="ObjectSizeLessThan"
    )


class MetricsAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    access_point_arn: Optional[str] = Field(default=None, alias="AccessPointArn")


class ReplicationRuleAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class TaggingModel(BaseModel):
    tag_set: Sequence[TagModel] = Field(alias="TagSet")


class AnalyticsExportDestinationModel(BaseModel):
    s3_bucket_destination: AnalyticsS3BucketDestinationModel = Field(
        alias="S3BucketDestination"
    )


class BucketCopyRequestModel(BaseModel):
    copy_source: CopySourceModel = Field(alias="CopySource")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    source_client: Optional[BaseClient] = Field(default=None, alias="SourceClient")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class ClientCopyRequestModel(BaseModel):
    copy_source: CopySourceModel = Field(alias="CopySource")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    source_client: Optional[BaseClient] = Field(default=None, alias="SourceClient")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class CopyObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    copy_source: Union[str, CopySourceModel] = Field(alias="CopySource")
    key: str = Field(alias="Key")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    copy_source_if_match: Optional[str] = Field(default=None, alias="CopySourceIfMatch")
    copy_source_if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfModifiedSince"
    )
    copy_source_if_none_match: Optional[str] = Field(
        default=None, alias="CopySourceIfNoneMatch"
    )
    copy_source_if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfUnmodifiedSince"
    )
    expires: Optional[Union[datetime, str]] = Field(default=None, alias="Expires")
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="Metadata")
    metadata_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="MetadataDirective"
    )
    tagging_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="TaggingDirective"
    )
    server_side_encryption: Optional[Literal["AES256", "aws:kms"]] = Field(
        default=None, alias="ServerSideEncryption"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    website_redirect_location: Optional[str] = Field(
        default=None, alias="WebsiteRedirectLocation"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: Optional[str] = Field(
        default=None, alias="SSEKMSEncryptionContext"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    copy_source_s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerAlgorithm"
    )
    copy_source_s_s_ecustomer_key: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKey"
    )
    copy_source_s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    tagging: Optional[str] = Field(default=None, alias="Tagging")
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    expected_source_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedSourceBucketOwner"
    )


class ObjectCopyRequestModel(BaseModel):
    copy_source: CopySourceModel = Field(alias="CopySource")
    extra_args: Optional[Dict[str, Any]] = Field(default=None, alias="ExtraArgs")
    callback: Optional[Callable[..., Any]] = Field(default=None, alias="Callback")
    source_client: Optional[BaseClient] = Field(default=None, alias="SourceClient")
    config: Optional[TransferConfig] = Field(default=None, alias="Config")


class UploadPartCopyRequestMultipartUploadPartCopyFromModel(BaseModel):
    copy_source: Union[str, CopySourceModel] = Field(alias="CopySource")
    copy_source_if_match: Optional[str] = Field(default=None, alias="CopySourceIfMatch")
    copy_source_if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfModifiedSince"
    )
    copy_source_if_none_match: Optional[str] = Field(
        default=None, alias="CopySourceIfNoneMatch"
    )
    copy_source_if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfUnmodifiedSince"
    )
    copy_source_range: Optional[str] = Field(default=None, alias="CopySourceRange")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    copy_source_s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerAlgorithm"
    )
    copy_source_s_s_ecustomer_key: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKey"
    )
    copy_source_s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    expected_source_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedSourceBucketOwner"
    )


class UploadPartCopyRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    copy_source: Union[str, CopySourceModel] = Field(alias="CopySource")
    key: str = Field(alias="Key")
    part_number: int = Field(alias="PartNumber")
    upload_id: str = Field(alias="UploadId")
    copy_source_if_match: Optional[str] = Field(default=None, alias="CopySourceIfMatch")
    copy_source_if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfModifiedSince"
    )
    copy_source_if_none_match: Optional[str] = Field(
        default=None, alias="CopySourceIfNoneMatch"
    )
    copy_source_if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="CopySourceIfUnmodifiedSince"
    )
    copy_source_range: Optional[str] = Field(default=None, alias="CopySourceRange")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    copy_source_s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerAlgorithm"
    )
    copy_source_s_s_ecustomer_key: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKey"
    )
    copy_source_s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="CopySourceSSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    expected_source_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedSourceBucketOwner"
    )


class ListBucketsOutputModel(BaseModel):
    buckets: List[BucketModel] = Field(alias="Buckets")
    owner: OwnerModel = Field(alias="Owner")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CORSConfigurationModel(BaseModel):
    cors_rules: Sequence[CORSRuleModel] = Field(alias="CORSRules")


class GetBucketCorsOutputModel(BaseModel):
    cors_rules: List[CORSRuleModel] = Field(alias="CORSRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompletedMultipartUploadModel(BaseModel):
    parts: Optional[Sequence[CompletedPartModel]] = Field(default=None, alias="Parts")


class CopyObjectOutputModel(BaseModel):
    copy_object_result: CopyObjectResultModel = Field(alias="CopyObjectResult")
    expiration: str = Field(alias="Expiration")
    copy_source_version_id: str = Field(alias="CopySourceVersionId")
    version_id: str = Field(alias="VersionId")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    s_s_ekms_encryption_context: str = Field(alias="SSEKMSEncryptionContext")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadPartCopyOutputModel(BaseModel):
    copy_source_version_id: str = Field(alias="CopySourceVersionId")
    copy_part_result: CopyPartResultModel = Field(alias="CopyPartResult")
    server_side_encryption: Literal["AES256", "aws:kms"] = Field(
        alias="ServerSideEncryption"
    )
    s_s_ecustomer_algorithm: str = Field(alias="SSECustomerAlgorithm")
    s_s_ecustomer_key_md5: str = Field(alias="SSECustomerKeyMD5")
    s_s_ekms_key_id: str = Field(alias="SSEKMSKeyId")
    bucket_key_enabled: bool = Field(alias="BucketKeyEnabled")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBucketRequestBucketCreateModel(BaseModel):
    acl: Optional[
        Literal["authenticated-read", "private", "public-read", "public-read-write"]
    ] = Field(default=None, alias="ACL")
    create_bucket_configuration: Optional[CreateBucketConfigurationModel] = Field(
        default=None, alias="CreateBucketConfiguration"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    object_lock_enabled_for_bucket: Optional[bool] = Field(
        default=None, alias="ObjectLockEnabledForBucket"
    )
    object_ownership: Optional[
        Literal["BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"]
    ] = Field(default=None, alias="ObjectOwnership")


class CreateBucketRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    acl: Optional[
        Literal["authenticated-read", "private", "public-read", "public-read-write"]
    ] = Field(default=None, alias="ACL")
    create_bucket_configuration: Optional[CreateBucketConfigurationModel] = Field(
        default=None, alias="CreateBucketConfiguration"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    object_lock_enabled_for_bucket: Optional[bool] = Field(
        default=None, alias="ObjectLockEnabledForBucket"
    )
    object_ownership: Optional[
        Literal["BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"]
    ] = Field(default=None, alias="ObjectOwnership")


class CreateBucketRequestServiceResourceCreateBucketModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    acl: Optional[
        Literal["authenticated-read", "private", "public-read", "public-read-write"]
    ] = Field(default=None, alias="ACL")
    create_bucket_configuration: Optional[CreateBucketConfigurationModel] = Field(
        default=None, alias="CreateBucketConfiguration"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    object_lock_enabled_for_bucket: Optional[bool] = Field(
        default=None, alias="ObjectLockEnabledForBucket"
    )
    object_ownership: Optional[
        Literal["BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"]
    ] = Field(default=None, alias="ObjectOwnership")


class ObjectLockRuleModel(BaseModel):
    default_retention: Optional[DefaultRetentionModel] = Field(
        default=None, alias="DefaultRetention"
    )


class DeleteObjectsOutputModel(BaseModel):
    deleted: List[DeletedObjectModel] = Field(alias="Deleted")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    errors: List[ErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteModel(BaseModel):
    objects: Sequence[ObjectIdentifierModel] = Field(alias="Objects")
    quiet: Optional[bool] = Field(default=None, alias="Quiet")


class S3KeyFilterModel(BaseModel):
    filter_rules: Optional[List[FilterRuleModel]] = Field(
        default=None, alias="FilterRules"
    )


class GetBucketPolicyStatusOutputModel(BaseModel):
    policy_status: PolicyStatusModel = Field(alias="PolicyStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectAttributesPartsModel(BaseModel):
    total_parts_count: Optional[int] = Field(default=None, alias="TotalPartsCount")
    part_number_marker: Optional[int] = Field(default=None, alias="PartNumberMarker")
    next_part_number_marker: Optional[int] = Field(
        default=None, alias="NextPartNumberMarker"
    )
    max_parts: Optional[int] = Field(default=None, alias="MaxParts")
    is_truncated: Optional[bool] = Field(default=None, alias="IsTruncated")
    parts: Optional[List[ObjectPartModel]] = Field(default=None, alias="Parts")


class GetObjectLegalHoldOutputModel(BaseModel):
    legal_hold: ObjectLockLegalHoldModel = Field(alias="LegalHold")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectLegalHoldRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    legal_hold: Optional[ObjectLockLegalHoldModel] = Field(
        default=None, alias="LegalHold"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetObjectRetentionOutputModel(BaseModel):
    retention: ObjectLockRetentionModel = Field(alias="Retention")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectRetentionRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    retention: Optional[ObjectLockRetentionModel] = Field(
        default=None, alias="Retention"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetPublicAccessBlockOutputModel(BaseModel):
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPublicAccessBlockRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GrantModel(BaseModel):
    grantee: Optional[GranteeModel] = Field(default=None, alias="Grantee")
    permission: Optional[
        Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
    ] = Field(default=None, alias="Permission")


class TargetGrantModel(BaseModel):
    grantee: Optional[GranteeModel] = Field(default=None, alias="Grantee")
    permission: Optional[Literal["FULL_CONTROL", "READ", "WRITE"]] = Field(
        default=None, alias="Permission"
    )


class HeadBucketRequestBucketExistsWaitModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class HeadBucketRequestBucketNotExistsWaitModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class HeadObjectRequestObjectExistsWaitModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class HeadObjectRequestObjectNotExistsWaitModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    if_match: Optional[str] = Field(default=None, alias="IfMatch")
    if_modified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfModifiedSince"
    )
    if_none_match: Optional[str] = Field(default=None, alias="IfNoneMatch")
    if_unmodified_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="IfUnmodifiedSince"
    )
    range: Optional[str] = Field(default=None, alias="Range")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    part_number: Optional[int] = Field(default=None, alias="PartNumber")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_mode: Optional[Literal["ENABLED"]] = Field(
        default=None, alias="ChecksumMode"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class MultipartUploadModel(BaseModel):
    upload_id: Optional[str] = Field(default=None, alias="UploadId")
    key: Optional[str] = Field(default=None, alias="Key")
    initiated: Optional[datetime] = Field(default=None, alias="Initiated")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")
    initiator: Optional[InitiatorModel] = Field(default=None, alias="Initiator")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class InputSerializationModel(BaseModel):
    cs_v: Optional[CSVInputModel] = Field(default=None, alias="CSV")
    compression_type: Optional[Literal["BZIP2", "GZIP", "NONE"]] = Field(
        default=None, alias="CompressionType"
    )
    js_on_: Optional[JSONInputModel] = Field(default=None, alias="JSON")
    parquet: Optional[Mapping[str, Any]] = Field(default=None, alias="Parquet")


class InventoryEncryptionModel(BaseModel):
    s_s_es3: Optional[Dict[str, Any]] = Field(default=None, alias="SSES3")
    s_s_ekms: Optional[SSEKMSModel] = Field(default=None, alias="SSEKMS")


class OutputSerializationModel(BaseModel):
    cs_v: Optional[CSVOutputModel] = Field(default=None, alias="CSV")
    js_on_: Optional[JSONOutputModel] = Field(default=None, alias="JSON")


class RuleModel(BaseModel):
    prefix: str = Field(alias="Prefix")
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    expiration: Optional[LifecycleExpirationModel] = Field(
        default=None, alias="Expiration"
    )
    id: Optional[str] = Field(default=None, alias="ID")
    transition: Optional[TransitionModel] = Field(default=None, alias="Transition")
    noncurrent_version_transition: Optional[NoncurrentVersionTransitionModel] = Field(
        default=None, alias="NoncurrentVersionTransition"
    )
    noncurrent_version_expiration: Optional[NoncurrentVersionExpirationModel] = Field(
        default=None, alias="NoncurrentVersionExpiration"
    )
    abort_incomplete_multipart_upload: Optional[
        AbortIncompleteMultipartUploadModel
    ] = Field(default=None, alias="AbortIncompleteMultipartUpload")


class ListMultipartUploadsRequestListMultipartUploadsPaginateModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectVersionsRequestListObjectVersionsPaginateModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectsRequestListObjectsPaginateModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectsV2RequestListObjectsV2PaginateModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    encoding_type: Optional[Literal["url"]] = Field(default=None, alias="EncodingType")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    fetch_owner: Optional[bool] = Field(default=None, alias="FetchOwner")
    start_after: Optional[str] = Field(default=None, alias="StartAfter")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPartsRequestListPartsPaginateModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPartsOutputModel(BaseModel):
    abort_date: datetime = Field(alias="AbortDate")
    abort_rule_id: str = Field(alias="AbortRuleId")
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    part_number_marker: int = Field(alias="PartNumberMarker")
    next_part_number_marker: int = Field(alias="NextPartNumberMarker")
    max_parts: int = Field(alias="MaxParts")
    is_truncated: bool = Field(alias="IsTruncated")
    parts: List[PartModel] = Field(alias="Parts")
    initiator: InitiatorModel = Field(alias="Initiator")
    owner: OwnerModel = Field(alias="Owner")
    storage_class: Literal[
        "DEEP_ARCHIVE",
        "GLACIER",
        "GLACIER_IR",
        "INTELLIGENT_TIERING",
        "ONEZONE_IA",
        "OUTPOSTS",
        "REDUCED_REDUNDANCY",
        "STANDARD",
        "STANDARD_IA",
    ] = Field(alias="StorageClass")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    checksum_algorithm: Literal["CRC32", "CRC32C", "SHA1", "SHA256"] = Field(
        alias="ChecksumAlgorithm"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricsModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    event_threshold: Optional[ReplicationTimeValueModel] = Field(
        default=None, alias="EventThreshold"
    )


class ReplicationTimeModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    time: ReplicationTimeValueModel = Field(alias="Time")


class NotificationConfigurationDeprecatedResponseMetadataModel(BaseModel):
    topic_configuration: TopicConfigurationDeprecatedModel = Field(
        alias="TopicConfiguration"
    )
    queue_configuration: QueueConfigurationDeprecatedModel = Field(
        alias="QueueConfiguration"
    )
    cloud_function_configuration: CloudFunctionConfigurationModel = Field(
        alias="CloudFunctionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotificationConfigurationDeprecatedModel(BaseModel):
    topic_configuration: Optional[TopicConfigurationDeprecatedModel] = Field(
        default=None, alias="TopicConfiguration"
    )
    queue_configuration: Optional[QueueConfigurationDeprecatedModel] = Field(
        default=None, alias="QueueConfiguration"
    )
    cloud_function_configuration: Optional[CloudFunctionConfigurationModel] = Field(
        default=None, alias="CloudFunctionConfiguration"
    )


class OwnershipControlsModel(BaseModel):
    rules: List[OwnershipControlsRuleModel] = Field(alias="Rules")


class ProgressEventModel(BaseModel):
    details: Optional[ProgressModel] = Field(default=None, alias="Details")


class PutBucketRequestPaymentRequestBucketRequestPaymentPutModel(BaseModel):
    request_payment_configuration: RequestPaymentConfigurationModel = Field(
        alias="RequestPaymentConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketRequestPaymentRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    request_payment_configuration: RequestPaymentConfigurationModel = Field(
        alias="RequestPaymentConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketVersioningRequestBucketVersioningPutModel(BaseModel):
    versioning_configuration: VersioningConfigurationModel = Field(
        alias="VersioningConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    mfa: Optional[str] = Field(default=None, alias="MFA")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketVersioningRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    versioning_configuration: VersioningConfigurationModel = Field(
        alias="VersioningConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    mfa: Optional[str] = Field(default=None, alias="MFA")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class RoutingRuleModel(BaseModel):
    redirect: RedirectModel = Field(alias="Redirect")
    condition: Optional[ConditionModel] = Field(default=None, alias="Condition")


class ServerSideEncryptionRuleModel(BaseModel):
    apply_server_side_encryption_by_default: Optional[
        ServerSideEncryptionByDefaultModel
    ] = Field(default=None, alias="ApplyServerSideEncryptionByDefault")
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")


class SourceSelectionCriteriaModel(BaseModel):
    sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjectsModel] = Field(
        default=None, alias="SseKmsEncryptedObjects"
    )
    replica_modifications: Optional[ReplicaModificationsModel] = Field(
        default=None, alias="ReplicaModifications"
    )


class StatsEventModel(BaseModel):
    details: Optional[StatsModel] = Field(default=None, alias="Details")


class ListObjectsOutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    marker: str = Field(alias="Marker")
    next_marker: str = Field(alias="NextMarker")
    contents: List[ObjectModel] = Field(alias="Contents")
    name: str = Field(alias="Name")
    prefix: str = Field(alias="Prefix")
    delimiter: str = Field(alias="Delimiter")
    max_keys: int = Field(alias="MaxKeys")
    common_prefixes: List[CommonPrefixModel] = Field(alias="CommonPrefixes")
    encoding_type: Literal["url"] = Field(alias="EncodingType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListObjectsV2OutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    contents: List[ObjectModel] = Field(alias="Contents")
    name: str = Field(alias="Name")
    prefix: str = Field(alias="Prefix")
    delimiter: str = Field(alias="Delimiter")
    max_keys: int = Field(alias="MaxKeys")
    common_prefixes: List[CommonPrefixModel] = Field(alias="CommonPrefixes")
    encoding_type: Literal["url"] = Field(alias="EncodingType")
    key_count: int = Field(alias="KeyCount")
    continuation_token: str = Field(alias="ContinuationToken")
    next_continuation_token: str = Field(alias="NextContinuationToken")
    start_after: str = Field(alias="StartAfter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListObjectVersionsOutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    key_marker: str = Field(alias="KeyMarker")
    version_id_marker: str = Field(alias="VersionIdMarker")
    next_key_marker: str = Field(alias="NextKeyMarker")
    next_version_id_marker: str = Field(alias="NextVersionIdMarker")
    versions: List[ObjectVersionModel] = Field(alias="Versions")
    delete_markers: List[DeleteMarkerEntryModel] = Field(alias="DeleteMarkers")
    name: str = Field(alias="Name")
    prefix: str = Field(alias="Prefix")
    delimiter: str = Field(alias="Delimiter")
    max_keys: int = Field(alias="MaxKeys")
    common_prefixes: List[CommonPrefixModel] = Field(alias="CommonPrefixes")
    encoding_type: Literal["url"] = Field(alias="EncodingType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AnalyticsFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    and_: Optional[AnalyticsAndOperatorModel] = Field(default=None, alias="And")


class IntelligentTieringFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    and_: Optional[IntelligentTieringAndOperatorModel] = Field(
        default=None, alias="And"
    )


class LifecycleRuleFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    object_size_greater_than: Optional[int] = Field(
        default=None, alias="ObjectSizeGreaterThan"
    )
    object_size_less_than: Optional[int] = Field(
        default=None, alias="ObjectSizeLessThan"
    )
    and_: Optional[LifecycleRuleAndOperatorModel] = Field(default=None, alias="And")


class MetricsFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    access_point_arn: Optional[str] = Field(default=None, alias="AccessPointArn")
    and_: Optional[MetricsAndOperatorModel] = Field(default=None, alias="And")


class ReplicationRuleFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[TagModel] = Field(default=None, alias="Tag")
    and_: Optional[ReplicationRuleAndOperatorModel] = Field(default=None, alias="And")


class PutBucketTaggingRequestBucketTaggingPutModel(BaseModel):
    tagging: TaggingModel = Field(alias="Tagging")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    tagging: TaggingModel = Field(alias="Tagging")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectTaggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    tagging: TaggingModel = Field(alias="Tagging")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )


class StorageClassAnalysisDataExportModel(BaseModel):
    output_schema_version: Literal["V_1"] = Field(alias="OutputSchemaVersion")
    destination: AnalyticsExportDestinationModel = Field(alias="Destination")


class PutBucketCorsRequestBucketCorsPutModel(BaseModel):
    cors_configuration: CORSConfigurationModel = Field(alias="CORSConfiguration")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketCorsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    cors_configuration: CORSConfigurationModel = Field(alias="CORSConfiguration")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class CompleteMultipartUploadRequestMultipartUploadCompleteModel(BaseModel):
    multipart_upload: Optional[CompletedMultipartUploadModel] = Field(
        default=None, alias="MultipartUpload"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )


class CompleteMultipartUploadRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    upload_id: str = Field(alias="UploadId")
    multipart_upload: Optional[CompletedMultipartUploadModel] = Field(
        default=None, alias="MultipartUpload"
    )
    checksum_crc32: Optional[str] = Field(default=None, alias="ChecksumCRC32")
    checksum_crc32_c: Optional[str] = Field(default=None, alias="ChecksumCRC32C")
    checksum_s_ha1: Optional[str] = Field(default=None, alias="ChecksumSHA1")
    checksum_s_ha256: Optional[str] = Field(default=None, alias="ChecksumSHA256")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )


class ObjectLockConfigurationModel(BaseModel):
    object_lock_enabled: Optional[Literal["Enabled"]] = Field(
        default=None, alias="ObjectLockEnabled"
    )
    rule: Optional[ObjectLockRuleModel] = Field(default=None, alias="Rule")


class DeleteObjectsRequestBucketDeleteObjectsModel(BaseModel):
    delete: DeleteModel = Field(alias="Delete")
    mfa: Optional[str] = Field(default=None, alias="MFA")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class DeleteObjectsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    delete: DeleteModel = Field(alias="Delete")
    mfa: Optional[str] = Field(default=None, alias="MFA")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class NotificationConfigurationFilterModel(BaseModel):
    key: Optional[S3KeyFilterModel] = Field(default=None, alias="Key")


class GetObjectAttributesOutputModel(BaseModel):
    delete_marker: bool = Field(alias="DeleteMarker")
    last_modified: datetime = Field(alias="LastModified")
    version_id: str = Field(alias="VersionId")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    etag: str = Field(alias="ETag")
    checksum: ChecksumModel = Field(alias="Checksum")
    object_parts: GetObjectAttributesPartsModel = Field(alias="ObjectParts")
    storage_class: Literal[
        "DEEP_ARCHIVE",
        "GLACIER",
        "GLACIER_IR",
        "INTELLIGENT_TIERING",
        "ONEZONE_IA",
        "OUTPOSTS",
        "REDUCED_REDUNDANCY",
        "STANDARD",
        "STANDARD_IA",
    ] = Field(alias="StorageClass")
    object_size: int = Field(alias="ObjectSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessControlPolicyModel(BaseModel):
    grants: Optional[Sequence[GrantModel]] = Field(default=None, alias="Grants")
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")


class GetBucketAclOutputModel(BaseModel):
    owner: OwnerModel = Field(alias="Owner")
    grants: List[GrantModel] = Field(alias="Grants")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectAclOutputModel(BaseModel):
    owner: OwnerModel = Field(alias="Owner")
    grants: List[GrantModel] = Field(alias="Grants")
    request_charged: Literal["requester"] = Field(alias="RequestCharged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3LocationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    prefix: str = Field(alias="Prefix")
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
    access_control_list: Optional[Sequence[GrantModel]] = Field(
        default=None, alias="AccessControlList"
    )
    tagging: Optional[TaggingModel] = Field(default=None, alias="Tagging")
    user_metadata: Optional[Sequence[MetadataEntryModel]] = Field(
        default=None, alias="UserMetadata"
    )
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")


class LoggingEnabledResponseMetadataModel(BaseModel):
    target_bucket: str = Field(alias="TargetBucket")
    target_grants: List[TargetGrantModel] = Field(alias="TargetGrants")
    target_prefix: str = Field(alias="TargetPrefix")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingEnabledModel(BaseModel):
    target_bucket: str = Field(alias="TargetBucket")
    target_prefix: str = Field(alias="TargetPrefix")
    target_grants: Optional[List[TargetGrantModel]] = Field(
        default=None, alias="TargetGrants"
    )


class ListMultipartUploadsOutputModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key_marker: str = Field(alias="KeyMarker")
    upload_id_marker: str = Field(alias="UploadIdMarker")
    next_key_marker: str = Field(alias="NextKeyMarker")
    prefix: str = Field(alias="Prefix")
    delimiter: str = Field(alias="Delimiter")
    next_upload_id_marker: str = Field(alias="NextUploadIdMarker")
    max_uploads: int = Field(alias="MaxUploads")
    is_truncated: bool = Field(alias="IsTruncated")
    uploads: List[MultipartUploadModel] = Field(alias="Uploads")
    common_prefixes: List[CommonPrefixModel] = Field(alias="CommonPrefixes")
    encoding_type: Literal["url"] = Field(alias="EncodingType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InventoryS3BucketDestinationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    format: Literal["CSV", "ORC", "Parquet"] = Field(alias="Format")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    encryption: Optional[InventoryEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class SelectObjectContentRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    expression: str = Field(alias="Expression")
    expression_type: Literal["SQL"] = Field(alias="ExpressionType")
    input_serialization: InputSerializationModel = Field(alias="InputSerialization")
    output_serialization: OutputSerializationModel = Field(alias="OutputSerialization")
    s_s_ecustomer_algorithm: Optional[str] = Field(
        default=None, alias="SSECustomerAlgorithm"
    )
    s_s_ecustomer_key: Optional[str] = Field(default=None, alias="SSECustomerKey")
    s_s_ecustomer_key_md5: Optional[str] = Field(
        default=None, alias="SSECustomerKeyMD5"
    )
    request_progress: Optional[RequestProgressModel] = Field(
        default=None, alias="RequestProgress"
    )
    scan_range: Optional[ScanRangeModel] = Field(default=None, alias="ScanRange")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class SelectParametersModel(BaseModel):
    input_serialization: InputSerializationModel = Field(alias="InputSerialization")
    expression_type: Literal["SQL"] = Field(alias="ExpressionType")
    expression: str = Field(alias="Expression")
    output_serialization: OutputSerializationModel = Field(alias="OutputSerialization")


class GetBucketLifecycleOutputModel(BaseModel):
    rules: List[RuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifecycleConfigurationModel(BaseModel):
    rules: Sequence[RuleModel] = Field(alias="Rules")


class DestinationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    account: Optional[str] = Field(default=None, alias="Account")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    access_control_translation: Optional[AccessControlTranslationModel] = Field(
        default=None, alias="AccessControlTranslation"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    replication_time: Optional[ReplicationTimeModel] = Field(
        default=None, alias="ReplicationTime"
    )
    metrics: Optional[MetricsModel] = Field(default=None, alias="Metrics")


class PutBucketNotificationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    notification_configuration: NotificationConfigurationDeprecatedModel = Field(
        alias="NotificationConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketOwnershipControlsOutputModel(BaseModel):
    ownership_controls: OwnershipControlsModel = Field(alias="OwnershipControls")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketOwnershipControlsRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    ownership_controls: OwnershipControlsModel = Field(alias="OwnershipControls")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketWebsiteOutputModel(BaseModel):
    redirect_all_requests_to: RedirectAllRequestsToModel = Field(
        alias="RedirectAllRequestsTo"
    )
    index_document: IndexDocumentModel = Field(alias="IndexDocument")
    error_document: ErrorDocumentModel = Field(alias="ErrorDocument")
    routing_rules: List[RoutingRuleModel] = Field(alias="RoutingRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WebsiteConfigurationModel(BaseModel):
    error_document: Optional[ErrorDocumentModel] = Field(
        default=None, alias="ErrorDocument"
    )
    index_document: Optional[IndexDocumentModel] = Field(
        default=None, alias="IndexDocument"
    )
    redirect_all_requests_to: Optional[RedirectAllRequestsToModel] = Field(
        default=None, alias="RedirectAllRequestsTo"
    )
    routing_rules: Optional[Sequence[RoutingRuleModel]] = Field(
        default=None, alias="RoutingRules"
    )


class ServerSideEncryptionConfigurationModel(BaseModel):
    rules: List[ServerSideEncryptionRuleModel] = Field(alias="Rules")


class SelectObjectContentEventStreamModel(BaseModel):
    records: Optional[RecordsEventModel] = Field(default=None, alias="Records")
    stats: Optional[StatsEventModel] = Field(default=None, alias="Stats")
    progress: Optional[ProgressEventModel] = Field(default=None, alias="Progress")
    cont: Optional[Dict[str, Any]] = Field(default=None, alias="Cont")
    end: Optional[Dict[str, Any]] = Field(default=None, alias="End")


class IntelligentTieringConfigurationModel(BaseModel):
    id: str = Field(alias="Id")
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    tierings: List[TieringModel] = Field(alias="Tierings")
    filter: Optional[IntelligentTieringFilterModel] = Field(
        default=None, alias="Filter"
    )


class LifecycleRuleModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    expiration: Optional[LifecycleExpirationModel] = Field(
        default=None, alias="Expiration"
    )
    id: Optional[str] = Field(default=None, alias="ID")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    filter: Optional[LifecycleRuleFilterModel] = Field(default=None, alias="Filter")
    transitions: Optional[List[TransitionModel]] = Field(
        default=None, alias="Transitions"
    )
    noncurrent_version_transitions: Optional[
        List[NoncurrentVersionTransitionModel]
    ] = Field(default=None, alias="NoncurrentVersionTransitions")
    noncurrent_version_expiration: Optional[NoncurrentVersionExpirationModel] = Field(
        default=None, alias="NoncurrentVersionExpiration"
    )
    abort_incomplete_multipart_upload: Optional[
        AbortIncompleteMultipartUploadModel
    ] = Field(default=None, alias="AbortIncompleteMultipartUpload")


class MetricsConfigurationModel(BaseModel):
    id: str = Field(alias="Id")
    filter: Optional[MetricsFilterModel] = Field(default=None, alias="Filter")


class StorageClassAnalysisModel(BaseModel):
    data_export: Optional[StorageClassAnalysisDataExportModel] = Field(
        default=None, alias="DataExport"
    )


class GetObjectLockConfigurationOutputModel(BaseModel):
    object_lock_configuration: ObjectLockConfigurationModel = Field(
        alias="ObjectLockConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectLockConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    object_lock_configuration: Optional[ObjectLockConfigurationModel] = Field(
        default=None, alias="ObjectLockConfiguration"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    token: Optional[str] = Field(default=None, alias="Token")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class LambdaFunctionConfigurationModel(BaseModel):
    lambda_function_arn: str = Field(alias="LambdaFunctionArn")
    events: List[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(alias="Events")
    id: Optional[str] = Field(default=None, alias="Id")
    filter: Optional[NotificationConfigurationFilterModel] = Field(
        default=None, alias="Filter"
    )


class QueueConfigurationModel(BaseModel):
    queue_arn: str = Field(alias="QueueArn")
    events: List[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(alias="Events")
    id: Optional[str] = Field(default=None, alias="Id")
    filter: Optional[NotificationConfigurationFilterModel] = Field(
        default=None, alias="Filter"
    )


class TopicConfigurationModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    events: List[
        Literal[
            "s3:IntelligentTiering",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:LifecycleTransition",
            "s3:ObjectAcl:Put",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Put",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Completed",
            "s3:ObjectRestore:Delete",
            "s3:ObjectRestore:Post",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Delete",
            "s3:ObjectTagging:Put",
            "s3:ReducedRedundancyLostObject",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ]
    ] = Field(alias="Events")
    id: Optional[str] = Field(default=None, alias="Id")
    filter: Optional[NotificationConfigurationFilterModel] = Field(
        default=None, alias="Filter"
    )


class PutBucketAclRequestBucketAclPutModel(BaseModel):
    acl: Optional[
        Literal["authenticated-read", "private", "public-read", "public-read-write"]
    ] = Field(default=None, alias="ACL")
    access_control_policy: Optional[AccessControlPolicyModel] = Field(
        default=None, alias="AccessControlPolicy"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketAclRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    acl: Optional[
        Literal["authenticated-read", "private", "public-read", "public-read-write"]
    ] = Field(default=None, alias="ACL")
    access_control_policy: Optional[AccessControlPolicyModel] = Field(
        default=None, alias="AccessControlPolicy"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectAclRequestObjectAclPutModel(BaseModel):
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    access_control_policy: Optional[AccessControlPolicyModel] = Field(
        default=None, alias="AccessControlPolicy"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutObjectAclRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="ACL")
    access_control_policy: Optional[AccessControlPolicyModel] = Field(
        default=None, alias="AccessControlPolicy"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    grant_full_control: Optional[str] = Field(default=None, alias="GrantFullControl")
    grant_read: Optional[str] = Field(default=None, alias="GrantRead")
    grant_read_acp: Optional[str] = Field(default=None, alias="GrantReadACP")
    grant_write: Optional[str] = Field(default=None, alias="GrantWrite")
    grant_write_acp: Optional[str] = Field(default=None, alias="GrantWriteACP")
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class OutputLocationModel(BaseModel):
    s3: Optional[S3LocationModel] = Field(default=None, alias="S3")


class BucketLoggingStatusModel(BaseModel):
    logging_enabled: Optional[LoggingEnabledModel] = Field(
        default=None, alias="LoggingEnabled"
    )


class GetBucketLoggingOutputModel(BaseModel):
    logging_enabled: LoggingEnabledModel = Field(alias="LoggingEnabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InventoryDestinationModel(BaseModel):
    s3_bucket_destination: InventoryS3BucketDestinationModel = Field(
        alias="S3BucketDestination"
    )


class PutBucketLifecycleRequestBucketLifecyclePutModel(BaseModel):
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    lifecycle_configuration: Optional[LifecycleConfigurationModel] = Field(
        default=None, alias="LifecycleConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketLifecycleRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    lifecycle_configuration: Optional[LifecycleConfigurationModel] = Field(
        default=None, alias="LifecycleConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class ReplicationRuleModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    destination: DestinationModel = Field(alias="Destination")
    id: Optional[str] = Field(default=None, alias="ID")
    priority: Optional[int] = Field(default=None, alias="Priority")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    filter: Optional[ReplicationRuleFilterModel] = Field(default=None, alias="Filter")
    source_selection_criteria: Optional[SourceSelectionCriteriaModel] = Field(
        default=None, alias="SourceSelectionCriteria"
    )
    existing_object_replication: Optional[ExistingObjectReplicationModel] = Field(
        default=None, alias="ExistingObjectReplication"
    )
    delete_marker_replication: Optional[DeleteMarkerReplicationModel] = Field(
        default=None, alias="DeleteMarkerReplication"
    )


class PutBucketWebsiteRequestBucketWebsitePutModel(BaseModel):
    website_configuration: WebsiteConfigurationModel = Field(
        alias="WebsiteConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketWebsiteRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    website_configuration: WebsiteConfigurationModel = Field(
        alias="WebsiteConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketEncryptionOutputModel(BaseModel):
    server_side_encryption_configuration: ServerSideEncryptionConfigurationModel = (
        Field(alias="ServerSideEncryptionConfiguration")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketEncryptionRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    server_side_encryption_configuration: ServerSideEncryptionConfigurationModel = (
        Field(alias="ServerSideEncryptionConfiguration")
    )
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class SelectObjectContentOutputModel(BaseModel):
    payload: SelectObjectContentEventStreamModel = Field(alias="Payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketIntelligentTieringConfigurationOutputModel(BaseModel):
    intelligent_tiering_configuration: IntelligentTieringConfigurationModel = Field(
        alias="IntelligentTieringConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBucketIntelligentTieringConfigurationsOutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    continuation_token: str = Field(alias="ContinuationToken")
    next_continuation_token: str = Field(alias="NextContinuationToken")
    intelligent_tiering_configuration_list: List[
        IntelligentTieringConfigurationModel
    ] = Field(alias="IntelligentTieringConfigurationList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketIntelligentTieringConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    intelligent_tiering_configuration: IntelligentTieringConfigurationModel = Field(
        alias="IntelligentTieringConfiguration"
    )


class BucketLifecycleConfigurationModel(BaseModel):
    rules: Sequence[LifecycleRuleModel] = Field(alias="Rules")


class GetBucketLifecycleConfigurationOutputModel(BaseModel):
    rules: List[LifecycleRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketMetricsConfigurationOutputModel(BaseModel):
    metrics_configuration: MetricsConfigurationModel = Field(
        alias="MetricsConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBucketMetricsConfigurationsOutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    continuation_token: str = Field(alias="ContinuationToken")
    next_continuation_token: str = Field(alias="NextContinuationToken")
    metrics_configuration_list: List[MetricsConfigurationModel] = Field(
        alias="MetricsConfigurationList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketMetricsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    metrics_configuration: MetricsConfigurationModel = Field(
        alias="MetricsConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class AnalyticsConfigurationModel(BaseModel):
    id: str = Field(alias="Id")
    storage_class_analysis: StorageClassAnalysisModel = Field(
        alias="StorageClassAnalysis"
    )
    filter: Optional[AnalyticsFilterModel] = Field(default=None, alias="Filter")


class NotificationConfigurationResponseMetadataModel(BaseModel):
    topic_configurations: List[TopicConfigurationModel] = Field(
        alias="TopicConfigurations"
    )
    queue_configurations: List[QueueConfigurationModel] = Field(
        alias="QueueConfigurations"
    )
    lambda_function_configurations: List[LambdaFunctionConfigurationModel] = Field(
        alias="LambdaFunctionConfigurations"
    )
    event_bridge_configuration: Dict[str, Any] = Field(alias="EventBridgeConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotificationConfigurationModel(BaseModel):
    topic_configurations: Optional[Sequence[TopicConfigurationModel]] = Field(
        default=None, alias="TopicConfigurations"
    )
    queue_configurations: Optional[Sequence[QueueConfigurationModel]] = Field(
        default=None, alias="QueueConfigurations"
    )
    lambda_function_configurations: Optional[
        Sequence[LambdaFunctionConfigurationModel]
    ] = Field(default=None, alias="LambdaFunctionConfigurations")
    event_bridge_configuration: Optional[Mapping[str, Any]] = Field(
        default=None, alias="EventBridgeConfiguration"
    )


class RestoreRequestModel(BaseModel):
    days: Optional[int] = Field(default=None, alias="Days")
    glacier_job_parameters: Optional[GlacierJobParametersModel] = Field(
        default=None, alias="GlacierJobParameters"
    )
    type: Optional[Literal["SELECT"]] = Field(default=None, alias="Type")
    tier: Optional[Literal["Bulk", "Expedited", "Standard"]] = Field(
        default=None, alias="Tier"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    select_parameters: Optional[SelectParametersModel] = Field(
        default=None, alias="SelectParameters"
    )
    output_location: Optional[OutputLocationModel] = Field(
        default=None, alias="OutputLocation"
    )


class PutBucketLoggingRequestBucketLoggingPutModel(BaseModel):
    bucket_logging_status: BucketLoggingStatusModel = Field(alias="BucketLoggingStatus")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketLoggingRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    bucket_logging_status: BucketLoggingStatusModel = Field(alias="BucketLoggingStatus")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class InventoryConfigurationModel(BaseModel):
    destination: InventoryDestinationModel = Field(alias="Destination")
    is_enabled: bool = Field(alias="IsEnabled")
    id: str = Field(alias="Id")
    included_object_versions: Literal["All", "Current"] = Field(
        alias="IncludedObjectVersions"
    )
    schedule: InventoryScheduleModel = Field(alias="Schedule")
    filter: Optional[InventoryFilterModel] = Field(default=None, alias="Filter")
    optional_fields: Optional[
        List[
            Literal[
                "BucketKeyStatus",
                "ChecksumAlgorithm",
                "ETag",
                "EncryptionStatus",
                "IntelligentTieringAccessTier",
                "IsMultipartUploaded",
                "LastModifiedDate",
                "ObjectLockLegalHoldStatus",
                "ObjectLockMode",
                "ObjectLockRetainUntilDate",
                "ReplicationStatus",
                "Size",
                "StorageClass",
            ]
        ]
    ] = Field(default=None, alias="OptionalFields")


class ReplicationConfigurationModel(BaseModel):
    role: str = Field(alias="Role")
    rules: List[ReplicationRuleModel] = Field(alias="Rules")


class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutModel(
    BaseModel
):
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    lifecycle_configuration: Optional[BucketLifecycleConfigurationModel] = Field(
        default=None, alias="LifecycleConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketLifecycleConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    lifecycle_configuration: Optional[BucketLifecycleConfigurationModel] = Field(
        default=None, alias="LifecycleConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketAnalyticsConfigurationOutputModel(BaseModel):
    analytics_configuration: AnalyticsConfigurationModel = Field(
        alias="AnalyticsConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBucketAnalyticsConfigurationsOutputModel(BaseModel):
    is_truncated: bool = Field(alias="IsTruncated")
    continuation_token: str = Field(alias="ContinuationToken")
    next_continuation_token: str = Field(alias="NextContinuationToken")
    analytics_configuration_list: List[AnalyticsConfigurationModel] = Field(
        alias="AnalyticsConfigurationList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketAnalyticsConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    analytics_configuration: AnalyticsConfigurationModel = Field(
        alias="AnalyticsConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class PutBucketNotificationConfigurationRequestBucketNotificationPutModel(BaseModel):
    notification_configuration: NotificationConfigurationModel = Field(
        alias="NotificationConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    skip_destination_validation: Optional[bool] = Field(
        default=None, alias="SkipDestinationValidation"
    )


class PutBucketNotificationConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    notification_configuration: NotificationConfigurationModel = Field(
        alias="NotificationConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    skip_destination_validation: Optional[bool] = Field(
        default=None, alias="SkipDestinationValidation"
    )


class RestoreObjectRequestObjectRestoreObjectModel(BaseModel):
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    restore_request: Optional[RestoreRequestModel] = Field(
        default=None, alias="RestoreRequest"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class RestoreObjectRequestObjectSummaryRestoreObjectModel(BaseModel):
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    restore_request: Optional[RestoreRequestModel] = Field(
        default=None, alias="RestoreRequest"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class RestoreObjectRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    restore_request: Optional[RestoreRequestModel] = Field(
        default=None, alias="RestoreRequest"
    )
    request_payer: Optional[Literal["requester"]] = Field(
        default=None, alias="RequestPayer"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketInventoryConfigurationOutputModel(BaseModel):
    inventory_configuration: InventoryConfigurationModel = Field(
        alias="InventoryConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBucketInventoryConfigurationsOutputModel(BaseModel):
    continuation_token: str = Field(alias="ContinuationToken")
    inventory_configuration_list: List[InventoryConfigurationModel] = Field(
        alias="InventoryConfigurationList"
    )
    is_truncated: bool = Field(alias="IsTruncated")
    next_continuation_token: str = Field(alias="NextContinuationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketInventoryConfigurationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    id: str = Field(alias="Id")
    inventory_configuration: InventoryConfigurationModel = Field(
        alias="InventoryConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class GetBucketReplicationOutputModel(BaseModel):
    replication_configuration: ReplicationConfigurationModel = Field(
        alias="ReplicationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBucketReplicationRequestModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    replication_configuration: ReplicationConfigurationModel = Field(
        alias="ReplicationConfiguration"
    )
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )
    token: Optional[str] = Field(default=None, alias="Token")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
