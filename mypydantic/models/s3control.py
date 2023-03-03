# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AbortIncompleteMultipartUploadModel(BaseModel):
    days_after_initiation: Optional[int] = Field(
        default=None, alias="DaysAfterInitiation"
    )


class VpcConfigurationModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")


class ActivityMetricsModel(BaseModel):
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")


class AdvancedCostOptimizationMetricsModel(BaseModel):
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")


class AdvancedDataProtectionMetricsModel(BaseModel):
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")


class DetailedStatusCodesMetricsModel(BaseModel):
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")


class AsyncErrorDetailsModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")
    resource: Optional[str] = Field(default=None, alias="Resource")
    request_id: Optional[str] = Field(default=None, alias="RequestId")


class DeleteMultiRegionAccessPointInputModel(BaseModel):
    name: str = Field(alias="Name")


class PutMultiRegionAccessPointPolicyInputModel(BaseModel):
    name: str = Field(alias="Name")
    policy: str = Field(alias="Policy")


class AwsLambdaTransformationModel(BaseModel):
    function_arn: str = Field(alias="FunctionArn")
    function_payload: Optional[str] = Field(default=None, alias="FunctionPayload")


class CloudWatchMetricsModel(BaseModel):
    is_enabled: bool = Field(alias="IsEnabled")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PublicAccessBlockConfigurationModel(BaseModel):
    block_public_acls: Optional[bool] = Field(default=None, alias="BlockPublicAcls")
    ignore_public_acls: Optional[bool] = Field(default=None, alias="IgnorePublicAcls")
    block_public_policy: Optional[bool] = Field(default=None, alias="BlockPublicPolicy")
    restrict_public_buckets: Optional[bool] = Field(
        default=None, alias="RestrictPublicBuckets"
    )


class CreateBucketConfigurationModel(BaseModel):
    location_constraint: Optional[
        Literal[
            "EU",
            "ap-northeast-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "cn-north-1",
            "eu-central-1",
            "eu-west-1",
            "sa-east-1",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="LocationConstraint")


class JobReportModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    format: Optional[Literal["Report_CSV_20180820"]] = Field(
        default=None, alias="Format"
    )
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    report_scope: Optional[Literal["AllTasks", "FailedTasksOnly"]] = Field(
        default=None, alias="ReportScope"
    )


class S3TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class RegionModel(BaseModel):
    bucket: str = Field(alias="Bucket")


class DeleteAccessPointForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class DeleteAccessPointPolicyForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class DeleteAccessPointPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class DeleteAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class DeleteBucketLifecycleConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class DeleteBucketPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class DeleteBucketRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class DeleteBucketTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class DeleteJobTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")


class DeletePublicAccessBlockRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class DeleteStorageLensConfigurationRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")


class DeleteStorageLensConfigurationTaggingRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")


class DescribeJobRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")


class DescribeMultiRegionAccessPointOperationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    request_token_arn: str = Field(alias="RequestTokenARN")


class EstablishedMultiRegionAccessPointPolicyModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="Policy")


class ExcludeModel(BaseModel):
    buckets: Optional[List[str]] = Field(default=None, alias="Buckets")
    regions: Optional[List[str]] = Field(default=None, alias="Regions")


class SSEKMSEncryptionModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class GetAccessPointConfigurationForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetAccessPointForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetAccessPointPolicyForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetAccessPointPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetAccessPointPolicyStatusForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class PolicyStatusModel(BaseModel):
    is_public: Optional[bool] = Field(default=None, alias="IsPublic")


class GetAccessPointPolicyStatusRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetBucketLifecycleConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class GetBucketPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class GetBucketRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class GetBucketTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class GetBucketVersioningRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")


class GetJobTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")


class GetMultiRegionAccessPointPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetMultiRegionAccessPointPolicyStatusRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetMultiRegionAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")


class GetMultiRegionAccessPointRoutesRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    mrap: str = Field(alias="Mrap")


class MultiRegionAccessPointRouteModel(BaseModel):
    traffic_dial_percentage: int = Field(alias="TrafficDialPercentage")
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    region: Optional[str] = Field(default=None, alias="Region")


class GetPublicAccessBlockRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class GetStorageLensConfigurationRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")


class GetStorageLensConfigurationTaggingRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")


class StorageLensTagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class IncludeModel(BaseModel):
    buckets: Optional[List[str]] = Field(default=None, alias="Buckets")
    regions: Optional[List[str]] = Field(default=None, alias="Regions")


class JobFailureModel(BaseModel):
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class JobManifestGeneratorFilterModel(BaseModel):
    eligible_for_replication: Optional[bool] = Field(
        default=None, alias="EligibleForReplication"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    object_replication_statuses: Optional[
        Sequence[Literal["COMPLETED", "FAILED", "NONE", "REPLICA"]]
    ] = Field(default=None, alias="ObjectReplicationStatuses")


class JobManifestLocationModel(BaseModel):
    object_arn: str = Field(alias="ObjectArn")
    etag: str = Field(alias="ETag")
    object_version_id: Optional[str] = Field(default=None, alias="ObjectVersionId")


class JobManifestSpecModel(BaseModel):
    format: Literal[
        "S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"
    ] = Field(alias="Format")
    fields: Optional[Sequence[Literal["Bucket", "Ignore", "Key", "VersionId"]]] = Field(
        default=None, alias="Fields"
    )


class LambdaInvokeOperationModel(BaseModel):
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")


class S3InitiateRestoreObjectOperationModel(BaseModel):
    expiration_in_days: Optional[int] = Field(default=None, alias="ExpirationInDays")
    glacier_job_tier: Optional[Literal["BULK", "STANDARD"]] = Field(
        default=None, alias="GlacierJobTier"
    )


class JobTimersModel(BaseModel):
    elapsed_time_in_active_seconds: Optional[int] = Field(
        default=None, alias="ElapsedTimeInActiveSeconds"
    )


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
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")


class TransitionModel(BaseModel):
    date: Optional[datetime] = Field(default=None, alias="Date")
    days: Optional[int] = Field(default=None, alias="Days")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccessPointsForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ObjectLambdaAccessPointModel(BaseModel):
    name: str = Field(alias="Name")
    object_lambda_access_point_arn: Optional[str] = Field(
        default=None, alias="ObjectLambdaAccessPointArn"
    )


class ListAccessPointsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListJobsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_statuses: Optional[
        Sequence[
            Literal[
                "Active",
                "Cancelled",
                "Cancelling",
                "Complete",
                "Completing",
                "Failed",
                "Failing",
                "New",
                "Paused",
                "Pausing",
                "Preparing",
                "Ready",
                "Suspended",
            ]
        ]
    ] = Field(default=None, alias="JobStatuses")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMultiRegionAccessPointsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRegionalBucketsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")


class RegionalBucketModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    public_access_block_enabled: bool = Field(alias="PublicAccessBlockEnabled")
    creation_date: datetime = Field(alias="CreationDate")
    bucket_arn: Optional[str] = Field(default=None, alias="BucketArn")
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")


class ListStorageLensConfigurationEntryModel(BaseModel):
    id: str = Field(alias="Id")
    storage_lens_arn: str = Field(alias="StorageLensArn")
    home_region: str = Field(alias="HomeRegion")
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")


class ListStorageLensConfigurationsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProposedMultiRegionAccessPointPolicyModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="Policy")


class MultiRegionAccessPointRegionalResponseModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    request_status: Optional[str] = Field(default=None, alias="RequestStatus")


class RegionReportModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    region: Optional[str] = Field(default=None, alias="Region")


class SelectionCriteriaModel(BaseModel):
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    max_depth: Optional[int] = Field(default=None, alias="MaxDepth")
    min_storage_bytes_percentage: Optional[float] = Field(
        default=None, alias="MinStorageBytesPercentage"
    )


class PutAccessPointPolicyForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    policy: str = Field(alias="Policy")


class PutAccessPointPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    policy: str = Field(alias="Policy")


class PutBucketPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")
    policy: str = Field(alias="Policy")
    confirm_remove_self_bucket_access: Optional[bool] = Field(
        default=None, alias="ConfirmRemoveSelfBucketAccess"
    )


class VersioningConfigurationModel(BaseModel):
    mfadelete: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="MFADelete"
    )
    status: Optional[Literal["Enabled", "Suspended"]] = Field(
        default=None, alias="Status"
    )


class S3ObjectOwnerModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="ID")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class S3ObjectMetadataModel(BaseModel):
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    content_disposition: Optional[str] = Field(default=None, alias="ContentDisposition")
    content_encoding: Optional[str] = Field(default=None, alias="ContentEncoding")
    content_language: Optional[str] = Field(default=None, alias="ContentLanguage")
    user_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserMetadata"
    )
    content_length: Optional[int] = Field(default=None, alias="ContentLength")
    content_md5: Optional[str] = Field(default=None, alias="ContentMD5")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    http_expires_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="HttpExpiresDate"
    )
    requester_charged: Optional[bool] = Field(default=None, alias="RequesterCharged")
    s_s_ealgorithm: Optional[Literal["AES256", "KMS"]] = Field(
        default=None, alias="SSEAlgorithm"
    )


class S3GranteeModel(BaseModel):
    type_identifier: Optional[Literal["emailAddress", "id", "uri"]] = Field(
        default=None, alias="TypeIdentifier"
    )
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class S3ObjectLockLegalHoldModel(BaseModel):
    status: Literal["OFF", "ON"] = Field(alias="Status")


class S3RetentionModel(BaseModel):
    retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="RetainUntilDate"
    )
    mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="Mode"
    )


class SSEKMSModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class StorageLensAwsOrgModel(BaseModel):
    arn: str = Field(alias="Arn")


class UpdateJobPriorityRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")
    priority: int = Field(alias="Priority")


class UpdateJobStatusRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")
    requested_job_status: Literal["Cancelled", "Ready"] = Field(
        alias="RequestedJobStatus"
    )
    status_update_reason: Optional[str] = Field(
        default=None, alias="StatusUpdateReason"
    )


class AccessPointModel(BaseModel):
    name: str = Field(alias="Name")
    network_origin: Literal["Internet", "VPC"] = Field(alias="NetworkOrigin")
    bucket: str = Field(alias="Bucket")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    access_point_arn: Optional[str] = Field(default=None, alias="AccessPointArn")
    alias: Optional[str] = Field(default=None, alias="Alias")
    bucket_account_id: Optional[str] = Field(default=None, alias="BucketAccountId")


class DeleteMultiRegionAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    client_token: str = Field(alias="ClientToken")
    details: DeleteMultiRegionAccessPointInputModel = Field(alias="Details")


class PutMultiRegionAccessPointPolicyRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    client_token: str = Field(alias="ClientToken")
    details: PutMultiRegionAccessPointPolicyInputModel = Field(alias="Details")


class ObjectLambdaContentTransformationModel(BaseModel):
    aws_lambda: Optional[AwsLambdaTransformationModel] = Field(
        default=None, alias="AwsLambda"
    )


class CreateAccessPointForObjectLambdaResultModel(BaseModel):
    object_lambda_access_point_arn: str = Field(alias="ObjectLambdaAccessPointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPointResultModel(BaseModel):
    access_point_arn: str = Field(alias="AccessPointArn")
    alias: str = Field(alias="Alias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBucketResultModel(BaseModel):
    location: str = Field(alias="Location")
    bucket_arn: str = Field(alias="BucketArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobResultModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMultiRegionAccessPointResultModel(BaseModel):
    request_token_arn: str = Field(alias="RequestTokenARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMultiRegionAccessPointResultModel(BaseModel):
    request_token_arn: str = Field(alias="RequestTokenARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessPointPolicyForObjectLambdaResultModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessPointPolicyResultModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketPolicyResultModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketResultModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    public_access_block_enabled: bool = Field(alias="PublicAccessBlockEnabled")
    creation_date: datetime = Field(alias="CreationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketVersioningResultModel(BaseModel):
    status: Literal["Enabled", "Suspended"] = Field(alias="Status")
    mfadelete: Literal["Disabled", "Enabled"] = Field(alias="MFADelete")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMultiRegionAccessPointPolicyResultModel(BaseModel):
    request_token_arn: str = Field(alias="RequestTokenARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobPriorityResultModel(BaseModel):
    job_id: str = Field(alias="JobId")
    priority: int = Field(alias="Priority")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobStatusResultModel(BaseModel):
    job_id: str = Field(alias="JobId")
    status: Literal[
        "Active",
        "Cancelled",
        "Cancelling",
        "Complete",
        "Completing",
        "Failed",
        "Failing",
        "New",
        "Paused",
        "Pausing",
        "Preparing",
        "Ready",
        "Suspended",
    ] = Field(alias="Status")
    status_update_reason: str = Field(alias="StatusUpdateReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    bucket: str = Field(alias="Bucket")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    public_access_block_configuration: Optional[
        PublicAccessBlockConfigurationModel
    ] = Field(default=None, alias="PublicAccessBlockConfiguration")
    bucket_account_id: Optional[str] = Field(default=None, alias="BucketAccountId")


class GetAccessPointForObjectLambdaResultModel(BaseModel):
    name: str = Field(alias="Name")
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    creation_date: datetime = Field(alias="CreationDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessPointResultModel(BaseModel):
    name: str = Field(alias="Name")
    bucket: str = Field(alias="Bucket")
    network_origin: Literal["Internet", "VPC"] = Field(alias="NetworkOrigin")
    vpc_configuration: VpcConfigurationModel = Field(alias="VpcConfiguration")
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    creation_date: datetime = Field(alias="CreationDate")
    alias: str = Field(alias="Alias")
    access_point_arn: str = Field(alias="AccessPointArn")
    endpoints: Dict[str, str] = Field(alias="Endpoints")
    bucket_account_id: str = Field(alias="BucketAccountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPublicAccessBlockOutputModel(BaseModel):
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPublicAccessBlockRequestModel(BaseModel):
    public_access_block_configuration: PublicAccessBlockConfigurationModel = Field(
        alias="PublicAccessBlockConfiguration"
    )
    account_id: str = Field(alias="AccountId")


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
    outpost_id: Optional[str] = Field(default=None, alias="OutpostId")


class GetBucketTaggingResultModel(BaseModel):
    tag_set: List[S3TagModel] = Field(alias="TagSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobTaggingResultModel(BaseModel):
    tags: List[S3TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifecycleRuleAndOperatorModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tags: Optional[List[S3TagModel]] = Field(default=None, alias="Tags")
    object_size_greater_than: Optional[int] = Field(
        default=None, alias="ObjectSizeGreaterThan"
    )
    object_size_less_than: Optional[int] = Field(
        default=None, alias="ObjectSizeLessThan"
    )


class PutJobTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    job_id: str = Field(alias="JobId")
    tags: Sequence[S3TagModel] = Field(alias="Tags")


class S3SetObjectTaggingOperationModel(BaseModel):
    tag_set: Optional[Sequence[S3TagModel]] = Field(default=None, alias="TagSet")


class TaggingModel(BaseModel):
    tag_set: Sequence[S3TagModel] = Field(alias="TagSet")


class CreateMultiRegionAccessPointInputModel(BaseModel):
    name: str = Field(alias="Name")
    regions: Sequence[RegionModel] = Field(alias="Regions")
    public_access_block: Optional[PublicAccessBlockConfigurationModel] = Field(
        default=None, alias="PublicAccessBlock"
    )


class GeneratedManifestEncryptionModel(BaseModel):
    s_s_es3: Optional[Mapping[str, Any]] = Field(default=None, alias="SSES3")
    s_s_ekms: Optional[SSEKMSEncryptionModel] = Field(default=None, alias="SSEKMS")


class GetAccessPointPolicyStatusForObjectLambdaResultModel(BaseModel):
    policy_status: PolicyStatusModel = Field(alias="PolicyStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessPointPolicyStatusResultModel(BaseModel):
    policy_status: PolicyStatusModel = Field(alias="PolicyStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMultiRegionAccessPointPolicyStatusResultModel(BaseModel):
    established: PolicyStatusModel = Field(alias="Established")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMultiRegionAccessPointRoutesResultModel(BaseModel):
    mrap: str = Field(alias="Mrap")
    routes: List[MultiRegionAccessPointRouteModel] = Field(alias="Routes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitMultiRegionAccessPointRoutesRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    mrap: str = Field(alias="Mrap")
    route_updates: Sequence[MultiRegionAccessPointRouteModel] = Field(
        alias="RouteUpdates"
    )


class GetStorageLensConfigurationTaggingResultModel(BaseModel):
    tags: List[StorageLensTagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutStorageLensConfigurationTaggingRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")
    tags: Sequence[StorageLensTagModel] = Field(alias="Tags")


class S3GeneratedManifestDescriptorModel(BaseModel):
    format: Optional[Literal["S3InventoryReport_CSV_20211130"]] = Field(
        default=None, alias="Format"
    )
    location: Optional[JobManifestLocationModel] = Field(default=None, alias="Location")


class JobManifestModel(BaseModel):
    spec: JobManifestSpecModel = Field(alias="Spec")
    location: JobManifestLocationModel = Field(alias="Location")


class JobProgressSummaryModel(BaseModel):
    total_number_of_tasks: Optional[int] = Field(
        default=None, alias="TotalNumberOfTasks"
    )
    number_of_tasks_succeeded: Optional[int] = Field(
        default=None, alias="NumberOfTasksSucceeded"
    )
    number_of_tasks_failed: Optional[int] = Field(
        default=None, alias="NumberOfTasksFailed"
    )
    timers: Optional[JobTimersModel] = Field(default=None, alias="Timers")


class ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccessPointsForObjectLambdaResultModel(BaseModel):
    object_lambda_access_point_list: List[ObjectLambdaAccessPointModel] = Field(
        alias="ObjectLambdaAccessPointList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRegionalBucketsResultModel(BaseModel):
    regional_bucket_list: List[RegionalBucketModel] = Field(alias="RegionalBucketList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStorageLensConfigurationsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    storage_lens_configuration_list: List[
        ListStorageLensConfigurationEntryModel
    ] = Field(alias="StorageLensConfigurationList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MultiRegionAccessPointPolicyDocumentModel(BaseModel):
    established: Optional[EstablishedMultiRegionAccessPointPolicyModel] = Field(
        default=None, alias="Established"
    )
    proposed: Optional[ProposedMultiRegionAccessPointPolicyModel] = Field(
        default=None, alias="Proposed"
    )


class MultiRegionAccessPointsAsyncResponseModel(BaseModel):
    regions: Optional[List[MultiRegionAccessPointRegionalResponseModel]] = Field(
        default=None, alias="Regions"
    )


class MultiRegionAccessPointReportModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    alias: Optional[str] = Field(default=None, alias="Alias")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    public_access_block: Optional[PublicAccessBlockConfigurationModel] = Field(
        default=None, alias="PublicAccessBlock"
    )
    status: Optional[
        Literal[
            "CREATING",
            "DELETING",
            "INCONSISTENT_ACROSS_REGIONS",
            "PARTIALLY_CREATED",
            "PARTIALLY_DELETED",
            "READY",
        ]
    ] = Field(default=None, alias="Status")
    regions: Optional[List[RegionReportModel]] = Field(default=None, alias="Regions")


class PrefixLevelStorageMetricsModel(BaseModel):
    is_enabled: Optional[bool] = Field(default=None, alias="IsEnabled")
    selection_criteria: Optional[SelectionCriteriaModel] = Field(
        default=None, alias="SelectionCriteria"
    )


class PutBucketVersioningRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")
    versioning_configuration: VersioningConfigurationModel = Field(
        alias="VersioningConfiguration"
    )
    mfa: Optional[str] = Field(default=None, alias="MFA")


class S3GrantModel(BaseModel):
    grantee: Optional[S3GranteeModel] = Field(default=None, alias="Grantee")
    permission: Optional[
        Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
    ] = Field(default=None, alias="Permission")


class S3SetObjectLegalHoldOperationModel(BaseModel):
    legal_hold: S3ObjectLockLegalHoldModel = Field(alias="LegalHold")


class S3SetObjectRetentionOperationModel(BaseModel):
    retention: S3RetentionModel = Field(alias="Retention")
    bypass_governance_retention: Optional[bool] = Field(
        default=None, alias="BypassGovernanceRetention"
    )


class StorageLensDataExportEncryptionModel(BaseModel):
    s_s_es3: Optional[Dict[str, Any]] = Field(default=None, alias="SSES3")
    s_s_ekms: Optional[SSEKMSModel] = Field(default=None, alias="SSEKMS")


class ListAccessPointsResultModel(BaseModel):
    access_point_list: List[AccessPointModel] = Field(alias="AccessPointList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ObjectLambdaTransformationConfigurationModel(BaseModel):
    actions: Sequence[
        Literal["GetObject", "HeadObject", "ListObjects", "ListObjectsV2"]
    ] = Field(alias="Actions")
    content_transformation: ObjectLambdaContentTransformationModel = Field(
        alias="ContentTransformation"
    )


class LifecycleRuleFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[S3TagModel] = Field(default=None, alias="Tag")
    and_: Optional[LifecycleRuleAndOperatorModel] = Field(default=None, alias="And")
    object_size_greater_than: Optional[int] = Field(
        default=None, alias="ObjectSizeGreaterThan"
    )
    object_size_less_than: Optional[int] = Field(
        default=None, alias="ObjectSizeLessThan"
    )


class PutBucketTaggingRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")
    tagging: TaggingModel = Field(alias="Tagging")


class AsyncRequestParametersModel(BaseModel):
    create_multi_region_access_point_request: Optional[
        CreateMultiRegionAccessPointInputModel
    ] = Field(default=None, alias="CreateMultiRegionAccessPointRequest")
    delete_multi_region_access_point_request: Optional[
        DeleteMultiRegionAccessPointInputModel
    ] = Field(default=None, alias="DeleteMultiRegionAccessPointRequest")
    put_multi_region_access_point_policy_request: Optional[
        PutMultiRegionAccessPointPolicyInputModel
    ] = Field(default=None, alias="PutMultiRegionAccessPointPolicyRequest")


class CreateMultiRegionAccessPointRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    client_token: str = Field(alias="ClientToken")
    details: CreateMultiRegionAccessPointInputModel = Field(alias="Details")


class S3ManifestOutputLocationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    manifest_format: Literal["S3InventoryReport_CSV_20211130"] = Field(
        alias="ManifestFormat"
    )
    expected_manifest_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedManifestBucketOwner"
    )
    manifest_prefix: Optional[str] = Field(default=None, alias="ManifestPrefix")
    manifest_encryption: Optional[GeneratedManifestEncryptionModel] = Field(
        default=None, alias="ManifestEncryption"
    )


class JobListDescriptorModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    description: Optional[str] = Field(default=None, alias="Description")
    operation: Optional[
        Literal[
            "LambdaInvoke",
            "S3DeleteObjectTagging",
            "S3InitiateRestoreObject",
            "S3PutObjectAcl",
            "S3PutObjectCopy",
            "S3PutObjectLegalHold",
            "S3PutObjectRetention",
            "S3PutObjectTagging",
            "S3ReplicateObject",
        ]
    ] = Field(default=None, alias="Operation")
    priority: Optional[int] = Field(default=None, alias="Priority")
    status: Optional[
        Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ]
    ] = Field(default=None, alias="Status")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    termination_date: Optional[datetime] = Field(default=None, alias="TerminationDate")
    progress_summary: Optional[JobProgressSummaryModel] = Field(
        default=None, alias="ProgressSummary"
    )


class GetMultiRegionAccessPointPolicyResultModel(BaseModel):
    policy: MultiRegionAccessPointPolicyDocumentModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AsyncResponseDetailsModel(BaseModel):
    multi_region_access_point_details: Optional[
        MultiRegionAccessPointsAsyncResponseModel
    ] = Field(default=None, alias="MultiRegionAccessPointDetails")
    error_details: Optional[AsyncErrorDetailsModel] = Field(
        default=None, alias="ErrorDetails"
    )


class GetMultiRegionAccessPointResultModel(BaseModel):
    access_point: MultiRegionAccessPointReportModel = Field(alias="AccessPoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMultiRegionAccessPointsResultModel(BaseModel):
    access_points: List[MultiRegionAccessPointReportModel] = Field(alias="AccessPoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PrefixLevelModel(BaseModel):
    storage_metrics: PrefixLevelStorageMetricsModel = Field(alias="StorageMetrics")


class S3AccessControlListModel(BaseModel):
    owner: S3ObjectOwnerModel = Field(alias="Owner")
    grants: Optional[Sequence[S3GrantModel]] = Field(default=None, alias="Grants")


class S3CopyObjectOperationModel(BaseModel):
    target_resource: Optional[str] = Field(default=None, alias="TargetResource")
    canned_access_control_list: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="CannedAccessControlList")
    access_control_grants: Optional[Sequence[S3GrantModel]] = Field(
        default=None, alias="AccessControlGrants"
    )
    metadata_directive: Optional[Literal["COPY", "REPLACE"]] = Field(
        default=None, alias="MetadataDirective"
    )
    modified_since_constraint: Optional[Union[datetime, str]] = Field(
        default=None, alias="ModifiedSinceConstraint"
    )
    new_object_metadata: Optional[S3ObjectMetadataModel] = Field(
        default=None, alias="NewObjectMetadata"
    )
    new_object_tagging: Optional[Sequence[S3TagModel]] = Field(
        default=None, alias="NewObjectTagging"
    )
    redirect_location: Optional[str] = Field(default=None, alias="RedirectLocation")
    requester_pays: Optional[bool] = Field(default=None, alias="RequesterPays")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="StorageClass")
    un_modified_since_constraint: Optional[Union[datetime, str]] = Field(
        default=None, alias="UnModifiedSinceConstraint"
    )
    s_s_eaws_kms_key_id: Optional[str] = Field(default=None, alias="SSEAwsKmsKeyId")
    target_key_prefix: Optional[str] = Field(default=None, alias="TargetKeyPrefix")
    object_lock_legal_hold_status: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="ObjectLockLegalHoldStatus"
    )
    object_lock_mode: Optional[Literal["COMPLIANCE", "GOVERNANCE"]] = Field(
        default=None, alias="ObjectLockMode"
    )
    object_lock_retain_until_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ObjectLockRetainUntilDate"
    )
    bucket_key_enabled: Optional[bool] = Field(default=None, alias="BucketKeyEnabled")
    checksum_algorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256"]] = Field(
        default=None, alias="ChecksumAlgorithm"
    )


class S3BucketDestinationModel(BaseModel):
    format: Literal["CSV", "Parquet"] = Field(alias="Format")
    output_schema_version: Literal["V_1"] = Field(alias="OutputSchemaVersion")
    account_id: str = Field(alias="AccountId")
    arn: str = Field(alias="Arn")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    encryption: Optional[StorageLensDataExportEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class ObjectLambdaConfigurationModel(BaseModel):
    supporting_access_point: str = Field(alias="SupportingAccessPoint")
    transformation_configurations: Sequence[
        ObjectLambdaTransformationConfigurationModel
    ] = Field(alias="TransformationConfigurations")
    cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchMetricsEnabled"
    )
    allowed_features: Optional[
        Sequence[
            Literal[
                "GetObject-PartNumber",
                "GetObject-Range",
                "HeadObject-PartNumber",
                "HeadObject-Range",
            ]
        ]
    ] = Field(default=None, alias="AllowedFeatures")


class LifecycleRuleModel(BaseModel):
    status: Literal["Disabled", "Enabled"] = Field(alias="Status")
    expiration: Optional[LifecycleExpirationModel] = Field(
        default=None, alias="Expiration"
    )
    id: Optional[str] = Field(default=None, alias="ID")
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


class S3JobManifestGeneratorModel(BaseModel):
    source_bucket: str = Field(alias="SourceBucket")
    enable_manifest_output: bool = Field(alias="EnableManifestOutput")
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    manifest_output_location: Optional[S3ManifestOutputLocationModel] = Field(
        default=None, alias="ManifestOutputLocation"
    )
    filter: Optional[JobManifestGeneratorFilterModel] = Field(
        default=None, alias="Filter"
    )


class ListJobsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    jobs: List[JobListDescriptorModel] = Field(alias="Jobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AsyncOperationModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    operation: Optional[
        Literal[
            "CreateMultiRegionAccessPoint",
            "DeleteMultiRegionAccessPoint",
            "PutMultiRegionAccessPointPolicy",
        ]
    ] = Field(default=None, alias="Operation")
    request_token_arn: Optional[str] = Field(default=None, alias="RequestTokenARN")
    request_parameters: Optional[AsyncRequestParametersModel] = Field(
        default=None, alias="RequestParameters"
    )
    request_status: Optional[str] = Field(default=None, alias="RequestStatus")
    response_details: Optional[AsyncResponseDetailsModel] = Field(
        default=None, alias="ResponseDetails"
    )


class BucketLevelModel(BaseModel):
    activity_metrics: Optional[ActivityMetricsModel] = Field(
        default=None, alias="ActivityMetrics"
    )
    prefix_level: Optional[PrefixLevelModel] = Field(default=None, alias="PrefixLevel")
    advanced_cost_optimization_metrics: Optional[
        AdvancedCostOptimizationMetricsModel
    ] = Field(default=None, alias="AdvancedCostOptimizationMetrics")
    advanced_data_protection_metrics: Optional[
        AdvancedDataProtectionMetricsModel
    ] = Field(default=None, alias="AdvancedDataProtectionMetrics")
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetricsModel] = Field(
        default=None, alias="DetailedStatusCodesMetrics"
    )


class S3AccessControlPolicyModel(BaseModel):
    access_control_list: Optional[S3AccessControlListModel] = Field(
        default=None, alias="AccessControlList"
    )
    canned_access_control_list: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="CannedAccessControlList")


class StorageLensDataExportModel(BaseModel):
    s3_bucket_destination: Optional[S3BucketDestinationModel] = Field(
        default=None, alias="S3BucketDestination"
    )
    cloud_watch_metrics: Optional[CloudWatchMetricsModel] = Field(
        default=None, alias="CloudWatchMetrics"
    )


class CreateAccessPointForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    configuration: ObjectLambdaConfigurationModel = Field(alias="Configuration")


class GetAccessPointConfigurationForObjectLambdaResultModel(BaseModel):
    configuration: ObjectLambdaConfigurationModel = Field(alias="Configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccessPointConfigurationForObjectLambdaRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    name: str = Field(alias="Name")
    configuration: ObjectLambdaConfigurationModel = Field(alias="Configuration")


class GetBucketLifecycleConfigurationResultModel(BaseModel):
    rules: List[LifecycleRuleModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LifecycleConfigurationModel(BaseModel):
    rules: Optional[Sequence[LifecycleRuleModel]] = Field(default=None, alias="Rules")


class JobManifestGeneratorModel(BaseModel):
    s3_job_manifest_generator: Optional[S3JobManifestGeneratorModel] = Field(
        default=None, alias="S3JobManifestGenerator"
    )


class DescribeMultiRegionAccessPointOperationResultModel(BaseModel):
    async_operation: AsyncOperationModel = Field(alias="AsyncOperation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccountLevelModel(BaseModel):
    bucket_level: BucketLevelModel = Field(alias="BucketLevel")
    activity_metrics: Optional[ActivityMetricsModel] = Field(
        default=None, alias="ActivityMetrics"
    )
    advanced_cost_optimization_metrics: Optional[
        AdvancedCostOptimizationMetricsModel
    ] = Field(default=None, alias="AdvancedCostOptimizationMetrics")
    advanced_data_protection_metrics: Optional[
        AdvancedDataProtectionMetricsModel
    ] = Field(default=None, alias="AdvancedDataProtectionMetrics")
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetricsModel] = Field(
        default=None, alias="DetailedStatusCodesMetrics"
    )


class S3SetObjectAclOperationModel(BaseModel):
    access_control_policy: Optional[S3AccessControlPolicyModel] = Field(
        default=None, alias="AccessControlPolicy"
    )


class PutBucketLifecycleConfigurationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    bucket: str = Field(alias="Bucket")
    lifecycle_configuration: Optional[LifecycleConfigurationModel] = Field(
        default=None, alias="LifecycleConfiguration"
    )


class StorageLensConfigurationModel(BaseModel):
    id: str = Field(alias="Id")
    account_level: AccountLevelModel = Field(alias="AccountLevel")
    is_enabled: bool = Field(alias="IsEnabled")
    include: Optional[IncludeModel] = Field(default=None, alias="Include")
    exclude: Optional[ExcludeModel] = Field(default=None, alias="Exclude")
    data_export: Optional[StorageLensDataExportModel] = Field(
        default=None, alias="DataExport"
    )
    aws_org: Optional[StorageLensAwsOrgModel] = Field(default=None, alias="AwsOrg")
    storage_lens_arn: Optional[str] = Field(default=None, alias="StorageLensArn")


class JobOperationModel(BaseModel):
    lambda_invoke: Optional[LambdaInvokeOperationModel] = Field(
        default=None, alias="LambdaInvoke"
    )
    s3_put_object_copy: Optional[S3CopyObjectOperationModel] = Field(
        default=None, alias="S3PutObjectCopy"
    )
    s3_put_object_acl: Optional[S3SetObjectAclOperationModel] = Field(
        default=None, alias="S3PutObjectAcl"
    )
    s3_put_object_tagging: Optional[S3SetObjectTaggingOperationModel] = Field(
        default=None, alias="S3PutObjectTagging"
    )
    s3_delete_object_tagging: Optional[Mapping[str, Any]] = Field(
        default=None, alias="S3DeleteObjectTagging"
    )
    s3_initiate_restore_object: Optional[S3InitiateRestoreObjectOperationModel] = Field(
        default=None, alias="S3InitiateRestoreObject"
    )
    s3_put_object_legal_hold: Optional[S3SetObjectLegalHoldOperationModel] = Field(
        default=None, alias="S3PutObjectLegalHold"
    )
    s3_put_object_retention: Optional[S3SetObjectRetentionOperationModel] = Field(
        default=None, alias="S3PutObjectRetention"
    )
    s3_replicate_object: Optional[Mapping[str, Any]] = Field(
        default=None, alias="S3ReplicateObject"
    )


class GetStorageLensConfigurationResultModel(BaseModel):
    storage_lens_configuration: StorageLensConfigurationModel = Field(
        alias="StorageLensConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutStorageLensConfigurationRequestModel(BaseModel):
    config_id: str = Field(alias="ConfigId")
    account_id: str = Field(alias="AccountId")
    storage_lens_configuration: StorageLensConfigurationModel = Field(
        alias="StorageLensConfiguration"
    )
    tags: Optional[Sequence[StorageLensTagModel]] = Field(default=None, alias="Tags")


class CreateJobRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    operation: JobOperationModel = Field(alias="Operation")
    report: JobReportModel = Field(alias="Report")
    client_request_token: str = Field(alias="ClientRequestToken")
    priority: int = Field(alias="Priority")
    role_arn: str = Field(alias="RoleArn")
    confirmation_required: Optional[bool] = Field(
        default=None, alias="ConfirmationRequired"
    )
    manifest: Optional[JobManifestModel] = Field(default=None, alias="Manifest")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[S3TagModel]] = Field(default=None, alias="Tags")
    manifest_generator: Optional[JobManifestGeneratorModel] = Field(
        default=None, alias="ManifestGenerator"
    )


class JobDescriptorModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    confirmation_required: Optional[bool] = Field(
        default=None, alias="ConfirmationRequired"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    status: Optional[
        Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ]
    ] = Field(default=None, alias="Status")
    manifest: Optional[JobManifestModel] = Field(default=None, alias="Manifest")
    operation: Optional[JobOperationModel] = Field(default=None, alias="Operation")
    priority: Optional[int] = Field(default=None, alias="Priority")
    progress_summary: Optional[JobProgressSummaryModel] = Field(
        default=None, alias="ProgressSummary"
    )
    status_update_reason: Optional[str] = Field(
        default=None, alias="StatusUpdateReason"
    )
    failure_reasons: Optional[List[JobFailureModel]] = Field(
        default=None, alias="FailureReasons"
    )
    report: Optional[JobReportModel] = Field(default=None, alias="Report")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    termination_date: Optional[datetime] = Field(default=None, alias="TerminationDate")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    suspended_date: Optional[datetime] = Field(default=None, alias="SuspendedDate")
    suspended_cause: Optional[str] = Field(default=None, alias="SuspendedCause")
    manifest_generator: Optional[JobManifestGeneratorModel] = Field(
        default=None, alias="ManifestGenerator"
    )
    generated_manifest_descriptor: Optional[S3GeneratedManifestDescriptorModel] = Field(
        default=None, alias="GeneratedManifestDescriptor"
    )


class DescribeJobResultModel(BaseModel):
    job: JobDescriptorModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
