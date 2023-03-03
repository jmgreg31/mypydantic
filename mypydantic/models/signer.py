# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddProfilePermissionRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    action: str = Field(alias="action")
    principal: str = Field(alias="principal")
    statement_id: str = Field(alias="statementId")
    profile_version: Optional[str] = Field(default=None, alias="profileVersion")
    revision_id: Optional[str] = Field(default=None, alias="revisionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CancelSigningProfileRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")


class DescribeSigningJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class SigningJobRevocationRecordModel(BaseModel):
    reason: Optional[str] = Field(default=None, alias="reason")
    revoked_at: Optional[datetime] = Field(default=None, alias="revokedAt")
    revoked_by: Optional[str] = Field(default=None, alias="revokedBy")


class SigningMaterialModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")


class S3DestinationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class EncryptionAlgorithmOptionsModel(BaseModel):
    allowed_values: List[Literal["ECDSA", "RSA"]] = Field(alias="allowedValues")
    default_value: Literal["ECDSA", "RSA"] = Field(alias="defaultValue")


class GetSigningPlatformRequestModel(BaseModel):
    platform_id: str = Field(alias="platformId")


class SigningImageFormatModel(BaseModel):
    supported_formats: List[Literal["JSON", "JSONDetached", "JSONEmbedded"]] = Field(
        alias="supportedFormats"
    )
    default_format: Literal["JSON", "JSONDetached", "JSONEmbedded"] = Field(
        alias="defaultFormat"
    )


class GetSigningProfileRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    profile_owner: Optional[str] = Field(default=None, alias="profileOwner")


class SignatureValidityPeriodModel(BaseModel):
    value: Optional[int] = Field(default=None, alias="value")
    type: Optional[Literal["DAYS", "MONTHS", "YEARS"]] = Field(
        default=None, alias="type"
    )


class SigningProfileRevocationRecordModel(BaseModel):
    revocation_effective_from: Optional[datetime] = Field(
        default=None, alias="revocationEffectiveFrom"
    )
    revoked_at: Optional[datetime] = Field(default=None, alias="revokedAt")
    revoked_by: Optional[str] = Field(default=None, alias="revokedBy")


class HashAlgorithmOptionsModel(BaseModel):
    allowed_values: List[Literal["SHA1", "SHA256"]] = Field(alias="allowedValues")
    default_value: Literal["SHA1", "SHA256"] = Field(alias="defaultValue")


class ListProfilePermissionsRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PermissionModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="action")
    principal: Optional[str] = Field(default=None, alias="principal")
    statement_id: Optional[str] = Field(default=None, alias="statementId")
    profile_version: Optional[str] = Field(default=None, alias="profileVersion")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListSigningJobsRequestModel(BaseModel):
    status: Optional[Literal["Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="status"
    )
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    requested_by: Optional[str] = Field(default=None, alias="requestedBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    is_revoked: Optional[bool] = Field(default=None, alias="isRevoked")
    signature_expires_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="signatureExpiresBefore"
    )
    signature_expires_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="signatureExpiresAfter"
    )
    job_invoker: Optional[str] = Field(default=None, alias="jobInvoker")


class ListSigningPlatformsRequestModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="category")
    partner: Optional[str] = Field(default=None, alias="partner")
    target: Optional[str] = Field(default=None, alias="target")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSigningProfilesRequestModel(BaseModel):
    include_canceled: Optional[bool] = Field(default=None, alias="includeCanceled")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    statuses: Optional[Sequence[Literal["Active", "Canceled", "Revoked"]]] = Field(
        default=None, alias="statuses"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class RemoveProfilePermissionRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    revision_id: str = Field(alias="revisionId")
    statement_id: str = Field(alias="statementId")


class RevokeSignatureRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    reason: str = Field(alias="reason")
    job_owner: Optional[str] = Field(default=None, alias="jobOwner")


class RevokeSigningProfileRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    profile_version: str = Field(alias="profileVersion")
    reason: str = Field(alias="reason")
    effective_time: Union[datetime, str] = Field(alias="effectiveTime")


class S3SignedObjectModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    key: Optional[str] = Field(default=None, alias="key")


class S3SourceModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    key: str = Field(alias="key")
    version: str = Field(alias="version")


class SigningConfigurationOverridesModel(BaseModel):
    encryption_algorithm: Optional[Literal["ECDSA", "RSA"]] = Field(
        default=None, alias="encryptionAlgorithm"
    )
    hash_algorithm: Optional[Literal["SHA1", "SHA256"]] = Field(
        default=None, alias="hashAlgorithm"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AddProfilePermissionResponseModel(BaseModel):
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSigningProfileResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    profile_version: str = Field(alias="profileVersion")
    profile_version_arn: str = Field(alias="profileVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveProfilePermissionResponseModel(BaseModel):
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSigningJobResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_owner: str = Field(alias="jobOwner")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSigningJobRequestSuccessfulSigningJobWaitModel(BaseModel):
    job_id: str = Field(alias="jobId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DestinationModel(BaseModel):
    s3: Optional[S3DestinationModel] = Field(default=None, alias="s3")


class SigningProfileModel(BaseModel):
    profile_name: Optional[str] = Field(default=None, alias="profileName")
    profile_version: Optional[str] = Field(default=None, alias="profileVersion")
    profile_version_arn: Optional[str] = Field(default=None, alias="profileVersionArn")
    signing_material: Optional[SigningMaterialModel] = Field(
        default=None, alias="signingMaterial"
    )
    signature_validity_period: Optional[SignatureValidityPeriodModel] = Field(
        default=None, alias="signatureValidityPeriod"
    )
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    platform_display_name: Optional[str] = Field(
        default=None, alias="platformDisplayName"
    )
    signing_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="signingParameters"
    )
    status: Optional[Literal["Active", "Canceled", "Revoked"]] = Field(
        default=None, alias="status"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class SigningConfigurationModel(BaseModel):
    encryption_algorithm_options: EncryptionAlgorithmOptionsModel = Field(
        alias="encryptionAlgorithmOptions"
    )
    hash_algorithm_options: HashAlgorithmOptionsModel = Field(
        alias="hashAlgorithmOptions"
    )


class ListProfilePermissionsResponseModel(BaseModel):
    revision_id: str = Field(alias="revisionId")
    policy_size_bytes: int = Field(alias="policySizeBytes")
    permissions: List[PermissionModel] = Field(alias="permissions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSigningJobsRequestListSigningJobsPaginateModel(BaseModel):
    status: Optional[Literal["Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="status"
    )
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    requested_by: Optional[str] = Field(default=None, alias="requestedBy")
    is_revoked: Optional[bool] = Field(default=None, alias="isRevoked")
    signature_expires_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="signatureExpiresBefore"
    )
    signature_expires_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="signatureExpiresAfter"
    )
    job_invoker: Optional[str] = Field(default=None, alias="jobInvoker")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSigningPlatformsRequestListSigningPlatformsPaginateModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="category")
    partner: Optional[str] = Field(default=None, alias="partner")
    target: Optional[str] = Field(default=None, alias="target")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSigningProfilesRequestListSigningProfilesPaginateModel(BaseModel):
    include_canceled: Optional[bool] = Field(default=None, alias="includeCanceled")
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    statuses: Optional[Sequence[Literal["Active", "Canceled", "Revoked"]]] = Field(
        default=None, alias="statuses"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SignedObjectModel(BaseModel):
    s3: Optional[S3SignedObjectModel] = Field(default=None, alias="s3")


class SourceModel(BaseModel):
    s3: Optional[S3SourceModel] = Field(default=None, alias="s3")


class SigningPlatformOverridesModel(BaseModel):
    signing_configuration: Optional[SigningConfigurationOverridesModel] = Field(
        default=None, alias="signingConfiguration"
    )
    signing_image_format: Optional[
        Literal["JSON", "JSONDetached", "JSONEmbedded"]
    ] = Field(default=None, alias="signingImageFormat")


class ListSigningProfilesResponseModel(BaseModel):
    profiles: List[SigningProfileModel] = Field(alias="profiles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSigningPlatformResponseModel(BaseModel):
    platform_id: str = Field(alias="platformId")
    display_name: str = Field(alias="displayName")
    partner: str = Field(alias="partner")
    target: str = Field(alias="target")
    category: Literal["AWSIoT"] = Field(alias="category")
    signing_configuration: SigningConfigurationModel = Field(
        alias="signingConfiguration"
    )
    signing_image_format: SigningImageFormatModel = Field(alias="signingImageFormat")
    max_size_in_mb: int = Field(alias="maxSizeInMB")
    revocation_supported: bool = Field(alias="revocationSupported")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SigningPlatformModel(BaseModel):
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    partner: Optional[str] = Field(default=None, alias="partner")
    target: Optional[str] = Field(default=None, alias="target")
    category: Optional[Literal["AWSIoT"]] = Field(default=None, alias="category")
    signing_configuration: Optional[SigningConfigurationModel] = Field(
        default=None, alias="signingConfiguration"
    )
    signing_image_format: Optional[SigningImageFormatModel] = Field(
        default=None, alias="signingImageFormat"
    )
    max_size_in_mb: Optional[int] = Field(default=None, alias="maxSizeInMB")
    revocation_supported: Optional[bool] = Field(
        default=None, alias="revocationSupported"
    )


class SigningJobModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    source: Optional[SourceModel] = Field(default=None, alias="source")
    signed_object: Optional[SignedObjectModel] = Field(
        default=None, alias="signedObject"
    )
    signing_material: Optional[SigningMaterialModel] = Field(
        default=None, alias="signingMaterial"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    status: Optional[Literal["Failed", "InProgress", "Succeeded"]] = Field(
        default=None, alias="status"
    )
    is_revoked: Optional[bool] = Field(default=None, alias="isRevoked")
    profile_name: Optional[str] = Field(default=None, alias="profileName")
    profile_version: Optional[str] = Field(default=None, alias="profileVersion")
    platform_id: Optional[str] = Field(default=None, alias="platformId")
    platform_display_name: Optional[str] = Field(
        default=None, alias="platformDisplayName"
    )
    signature_expires_at: Optional[datetime] = Field(
        default=None, alias="signatureExpiresAt"
    )
    job_owner: Optional[str] = Field(default=None, alias="jobOwner")
    job_invoker: Optional[str] = Field(default=None, alias="jobInvoker")


class StartSigningJobRequestModel(BaseModel):
    source: SourceModel = Field(alias="source")
    destination: DestinationModel = Field(alias="destination")
    profile_name: str = Field(alias="profileName")
    client_request_token: str = Field(alias="clientRequestToken")
    profile_owner: Optional[str] = Field(default=None, alias="profileOwner")


class DescribeSigningJobResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    source: SourceModel = Field(alias="source")
    signing_material: SigningMaterialModel = Field(alias="signingMaterial")
    platform_id: str = Field(alias="platformId")
    platform_display_name: str = Field(alias="platformDisplayName")
    profile_name: str = Field(alias="profileName")
    profile_version: str = Field(alias="profileVersion")
    overrides: SigningPlatformOverridesModel = Field(alias="overrides")
    signing_parameters: Dict[str, str] = Field(alias="signingParameters")
    created_at: datetime = Field(alias="createdAt")
    completed_at: datetime = Field(alias="completedAt")
    signature_expires_at: datetime = Field(alias="signatureExpiresAt")
    requested_by: str = Field(alias="requestedBy")
    status: Literal["Failed", "InProgress", "Succeeded"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    revocation_record: SigningJobRevocationRecordModel = Field(alias="revocationRecord")
    signed_object: SignedObjectModel = Field(alias="signedObject")
    job_owner: str = Field(alias="jobOwner")
    job_invoker: str = Field(alias="jobInvoker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSigningProfileResponseModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    profile_version: str = Field(alias="profileVersion")
    profile_version_arn: str = Field(alias="profileVersionArn")
    revocation_record: SigningProfileRevocationRecordModel = Field(
        alias="revocationRecord"
    )
    signing_material: SigningMaterialModel = Field(alias="signingMaterial")
    platform_id: str = Field(alias="platformId")
    platform_display_name: str = Field(alias="platformDisplayName")
    signature_validity_period: SignatureValidityPeriodModel = Field(
        alias="signatureValidityPeriod"
    )
    overrides: SigningPlatformOverridesModel = Field(alias="overrides")
    signing_parameters: Dict[str, str] = Field(alias="signingParameters")
    status: Literal["Active", "Canceled", "Revoked"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    arn: str = Field(alias="arn")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSigningProfileRequestModel(BaseModel):
    profile_name: str = Field(alias="profileName")
    platform_id: str = Field(alias="platformId")
    signing_material: Optional[SigningMaterialModel] = Field(
        default=None, alias="signingMaterial"
    )
    signature_validity_period: Optional[SignatureValidityPeriodModel] = Field(
        default=None, alias="signatureValidityPeriod"
    )
    overrides: Optional[SigningPlatformOverridesModel] = Field(
        default=None, alias="overrides"
    )
    signing_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="signingParameters"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ListSigningPlatformsResponseModel(BaseModel):
    platforms: List[SigningPlatformModel] = Field(alias="platforms")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSigningJobsResponseModel(BaseModel):
    jobs: List[SigningJobModel] = Field(alias="jobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
