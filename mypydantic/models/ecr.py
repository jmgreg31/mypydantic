# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttributeModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class AuthorizationDataModel(BaseModel):
    authorization_token: Optional[str] = Field(default=None, alias="authorizationToken")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    proxy_endpoint: Optional[str] = Field(default=None, alias="proxyEndpoint")


class AwsEcrContainerImageDetailsModel(BaseModel):
    architecture: Optional[str] = Field(default=None, alias="architecture")
    author: Optional[str] = Field(default=None, alias="author")
    image_hash: Optional[str] = Field(default=None, alias="imageHash")
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    platform: Optional[str] = Field(default=None, alias="platform")
    pushed_at: Optional[datetime] = Field(default=None, alias="pushedAt")
    registry: Optional[str] = Field(default=None, alias="registry")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")


class BatchCheckLayerAvailabilityRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    layer_digests: Sequence[str] = Field(alias="layerDigests")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class LayerFailureModel(BaseModel):
    layer_digest: Optional[str] = Field(default=None, alias="layerDigest")
    failure_code: Optional[Literal["InvalidLayerDigest", "MissingLayerDigest"]] = Field(
        default=None, alias="failureCode"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class LayerModel(BaseModel):
    layer_digest: Optional[str] = Field(default=None, alias="layerDigest")
    layer_availability: Optional[Literal["AVAILABLE", "UNAVAILABLE"]] = Field(
        default=None, alias="layerAvailability"
    )
    layer_size: Optional[int] = Field(default=None, alias="layerSize")
    media_type: Optional[str] = Field(default=None, alias="mediaType")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ImageIdentifierModel(BaseModel):
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    image_tag: Optional[str] = Field(default=None, alias="imageTag")


class BatchGetRepositoryScanningConfigurationRequestModel(BaseModel):
    repository_names: Sequence[str] = Field(alias="repositoryNames")


class RepositoryScanningConfigurationFailureModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    failure_code: Optional[Literal["REPOSITORY_NOT_FOUND"]] = Field(
        default=None, alias="failureCode"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class CompleteLayerUploadRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    upload_id: str = Field(alias="uploadId")
    layer_digests: Sequence[str] = Field(alias="layerDigests")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class CreatePullThroughCacheRuleRequestModel(BaseModel):
    ecr_repository_prefix: str = Field(alias="ecrRepositoryPrefix")
    upstream_registry_url: str = Field(alias="upstreamRegistryUrl")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class EncryptionConfigurationModel(BaseModel):
    encryption_type: Literal["AES256", "KMS"] = Field(alias="encryptionType")
    kms_key: Optional[str] = Field(default=None, alias="kmsKey")


class ImageScanningConfigurationModel(BaseModel):
    scan_on_push: Optional[bool] = Field(default=None, alias="scanOnPush")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CvssScoreAdjustmentModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="metric")
    reason: Optional[str] = Field(default=None, alias="reason")


class CvssScoreModel(BaseModel):
    base_score: Optional[float] = Field(default=None, alias="baseScore")
    scoring_vector: Optional[str] = Field(default=None, alias="scoringVector")
    source: Optional[str] = Field(default=None, alias="source")
    version: Optional[str] = Field(default=None, alias="version")


class DeleteLifecyclePolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DeletePullThroughCacheRuleRequestModel(BaseModel):
    ecr_repository_prefix: str = Field(alias="ecrRepositoryPrefix")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DeleteRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DeleteRepositoryRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    force: Optional[bool] = Field(default=None, alias="force")


class ImageReplicationStatusModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="region")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    status: Optional[Literal["COMPLETE", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="status"
    )
    failure_code: Optional[str] = Field(default=None, alias="failureCode")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class ImageScanStatusModel(BaseModel):
    status: Optional[
        Literal[
            "ACTIVE",
            "COMPLETE",
            "FAILED",
            "FINDINGS_UNAVAILABLE",
            "IN_PROGRESS",
            "PENDING",
            "SCAN_ELIGIBILITY_EXPIRED",
            "UNSUPPORTED_IMAGE",
        ]
    ] = Field(default=None, alias="status")
    description: Optional[str] = Field(default=None, alias="description")


class DescribeImagesFilterModel(BaseModel):
    tag_status: Optional[Literal["ANY", "TAGGED", "UNTAGGED"]] = Field(
        default=None, alias="tagStatus"
    )


class DescribePullThroughCacheRulesRequestModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    ecr_repository_prefixes: Optional[Sequence[str]] = Field(
        default=None, alias="ecrRepositoryPrefixes"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PullThroughCacheRuleModel(BaseModel):
    ecr_repository_prefix: Optional[str] = Field(
        default=None, alias="ecrRepositoryPrefix"
    )
    upstream_registry_url: Optional[str] = Field(
        default=None, alias="upstreamRegistryUrl"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DescribeRepositoriesRequestModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_names: Optional[Sequence[str]] = Field(
        default=None, alias="repositoryNames"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetAuthorizationTokenRequestModel(BaseModel):
    registry_ids: Optional[Sequence[str]] = Field(default=None, alias="registryIds")


class GetDownloadUrlForLayerRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    layer_digest: str = Field(alias="layerDigest")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class LifecyclePolicyPreviewFilterModel(BaseModel):
    tag_status: Optional[Literal["ANY", "TAGGED", "UNTAGGED"]] = Field(
        default=None, alias="tagStatus"
    )


class LifecyclePolicyPreviewSummaryModel(BaseModel):
    expiring_image_total_count: Optional[int] = Field(
        default=None, alias="expiringImageTotalCount"
    )


class GetLifecyclePolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class GetRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class ImageScanFindingsSummaryModel(BaseModel):
    image_scan_completed_at: Optional[datetime] = Field(
        default=None, alias="imageScanCompletedAt"
    )
    vulnerability_source_updated_at: Optional[datetime] = Field(
        default=None, alias="vulnerabilitySourceUpdatedAt"
    )
    finding_severity_counts: Optional[
        Dict[
            Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNDEFINED"],
            int,
        ]
    ] = Field(default=None, alias="findingSeverityCounts")


class InitiateLayerUploadRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class LifecyclePolicyRuleActionModel(BaseModel):
    type: Optional[Literal["EXPIRE"]] = Field(default=None, alias="type")


class ListImagesFilterModel(BaseModel):
    tag_status: Optional[Literal["ANY", "TAGGED", "UNTAGGED"]] = Field(
        default=None, alias="tagStatus"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class VulnerablePackageModel(BaseModel):
    arch: Optional[str] = Field(default=None, alias="arch")
    epoch: Optional[int] = Field(default=None, alias="epoch")
    file_path: Optional[str] = Field(default=None, alias="filePath")
    name: Optional[str] = Field(default=None, alias="name")
    package_manager: Optional[str] = Field(default=None, alias="packageManager")
    release: Optional[str] = Field(default=None, alias="release")
    source_layer_hash: Optional[str] = Field(default=None, alias="sourceLayerHash")
    version: Optional[str] = Field(default=None, alias="version")


class PutImageRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_manifest: str = Field(alias="imageManifest")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )
    image_tag: Optional[str] = Field(default=None, alias="imageTag")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")


class PutImageTagMutabilityRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_tag_mutability: Literal["IMMUTABLE", "MUTABLE"] = Field(
        alias="imageTagMutability"
    )
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class PutLifecyclePolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class PutRegistryPolicyRequestModel(BaseModel):
    policy_text: str = Field(alias="policyText")


class RecommendationModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="url")
    text: Optional[str] = Field(default=None, alias="text")


class ScanningRepositoryFilterModel(BaseModel):
    filter: str = Field(alias="filter")
    filter_type: Literal["WILDCARD"] = Field(alias="filterType")


class ReplicationDestinationModel(BaseModel):
    region: str = Field(alias="region")
    registry_id: str = Field(alias="registryId")


class RepositoryFilterModel(BaseModel):
    filter: str = Field(alias="filter")
    filter_type: Literal["PREFIX_MATCH"] = Field(alias="filterType")


class SetRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    force: Optional[bool] = Field(default=None, alias="force")


class StartLifecyclePolicyPreviewRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    lifecycle_policy_text: Optional[str] = Field(
        default=None, alias="lifecyclePolicyText"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UploadLayerPartRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    upload_id: str = Field(alias="uploadId")
    part_first_byte: int = Field(alias="partFirstByte")
    part_last_byte: int = Field(alias="partLastByte")
    layer_part_blob: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="layerPartBlob"
    )
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class ImageScanFindingModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    uri: Optional[str] = Field(default=None, alias="uri")
    severity: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNDEFINED"]
    ] = Field(default=None, alias="severity")
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="attributes")


class ResourceDetailsModel(BaseModel):
    aws_ecr_container_image: Optional[AwsEcrContainerImageDetailsModel] = Field(
        default=None, alias="awsEcrContainerImage"
    )


class BatchCheckLayerAvailabilityResponseModel(BaseModel):
    layers: List[LayerModel] = Field(alias="layers")
    failures: List[LayerFailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompleteLayerUploadResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    upload_id: str = Field(alias="uploadId")
    layer_digest: str = Field(alias="layerDigest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePullThroughCacheRuleResponseModel(BaseModel):
    ecr_repository_prefix: str = Field(alias="ecrRepositoryPrefix")
    upstream_registry_url: str = Field(alias="upstreamRegistryUrl")
    created_at: datetime = Field(alias="createdAt")
    registry_id: str = Field(alias="registryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLifecyclePolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    last_evaluated_at: datetime = Field(alias="lastEvaluatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePullThroughCacheRuleResponseModel(BaseModel):
    ecr_repository_prefix: str = Field(alias="ecrRepositoryPrefix")
    upstream_registry_url: str = Field(alias="upstreamRegistryUrl")
    created_at: datetime = Field(alias="createdAt")
    registry_id: str = Field(alias="registryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRegistryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAuthorizationTokenResponseModel(BaseModel):
    authorization_data: List[AuthorizationDataModel] = Field(alias="authorizationData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDownloadUrlForLayerResponseModel(BaseModel):
    download_url: str = Field(alias="downloadUrl")
    layer_digest: str = Field(alias="layerDigest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLifecyclePolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    last_evaluated_at: datetime = Field(alias="lastEvaluatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegistryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateLayerUploadResponseModel(BaseModel):
    upload_id: str = Field(alias="uploadId")
    part_size: int = Field(alias="partSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutImageTagMutabilityResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    image_tag_mutability: Literal["IMMUTABLE", "MUTABLE"] = Field(
        alias="imageTagMutability"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLifecyclePolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRegistryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetRepositoryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartLifecyclePolicyPreviewResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    status: Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadLayerPartResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    upload_id: str = Field(alias="uploadId")
    last_byte_received: int = Field(alias="lastByteReceived")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteImageRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_ids: Sequence[ImageIdentifierModel] = Field(alias="imageIds")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class BatchGetImageRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_ids: Sequence[ImageIdentifierModel] = Field(alias="imageIds")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    accepted_media_types: Optional[Sequence[str]] = Field(
        default=None, alias="acceptedMediaTypes"
    )


class DescribeImageReplicationStatusRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DescribeImageScanFindingsRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ImageFailureModel(BaseModel):
    image_id: Optional[ImageIdentifierModel] = Field(default=None, alias="imageId")
    failure_code: Optional[
        Literal[
            "ImageNotFound",
            "ImageReferencedByManifestList",
            "ImageTagDoesNotMatchDigest",
            "InvalidImageDigest",
            "InvalidImageTag",
            "KmsError",
            "MissingDigestAndTag",
        ]
    ] = Field(default=None, alias="failureCode")
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class ImageModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    image_id: Optional[ImageIdentifierModel] = Field(default=None, alias="imageId")
    image_manifest: Optional[str] = Field(default=None, alias="imageManifest")
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )


class ListImagesResponseModel(BaseModel):
    image_ids: List[ImageIdentifierModel] = Field(alias="imageIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImageScanRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class PutImageScanningConfigurationRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_scanning_configuration: ImageScanningConfigurationModel = Field(
        alias="imageScanningConfiguration"
    )
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class PutImageScanningConfigurationResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    image_scanning_configuration: ImageScanningConfigurationModel = Field(
        alias="imageScanningConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RepositoryModel(BaseModel):
    repository_arn: Optional[str] = Field(default=None, alias="repositoryArn")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    repository_uri: Optional[str] = Field(default=None, alias="repositoryUri")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    image_tag_mutability: Optional[Literal["IMMUTABLE", "MUTABLE"]] = Field(
        default=None, alias="imageTagMutability"
    )
    image_scanning_configuration: Optional[ImageScanningConfigurationModel] = Field(
        default=None, alias="imageScanningConfiguration"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="encryptionConfiguration"
    )


class CreateRepositoryRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    image_tag_mutability: Optional[Literal["IMMUTABLE", "MUTABLE"]] = Field(
        default=None, alias="imageTagMutability"
    )
    image_scanning_configuration: Optional[ImageScanningConfigurationModel] = Field(
        default=None, alias="imageScanningConfiguration"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="encryptionConfiguration"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CvssScoreDetailsModel(BaseModel):
    adjustments: Optional[List[CvssScoreAdjustmentModel]] = Field(
        default=None, alias="adjustments"
    )
    score: Optional[float] = Field(default=None, alias="score")
    score_source: Optional[str] = Field(default=None, alias="scoreSource")
    scoring_vector: Optional[str] = Field(default=None, alias="scoringVector")
    version: Optional[str] = Field(default=None, alias="version")


class DescribeImageReplicationStatusResponseModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    replication_statuses: List[ImageReplicationStatusModel] = Field(
        alias="replicationStatuses"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateModel(
    BaseModel
):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    ecr_repository_prefixes: Optional[Sequence[str]] = Field(
        default=None, alias="ecrRepositoryPrefixes"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRepositoriesRequestDescribeRepositoriesPaginateModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_names: Optional[Sequence[str]] = Field(
        default=None, alias="repositoryNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeImageScanFindingsRequestImageScanCompleteWaitModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class StartImageScanResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    image_scan_status: ImageScanStatusModel = Field(alias="imageScanStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImagesRequestDescribeImagesPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    filter: Optional[DescribeImagesFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeImagesRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[DescribeImagesFilterModel] = Field(default=None, alias="filter")


class DescribePullThroughCacheRulesResponseModel(BaseModel):
    pull_through_cache_rules: List[PullThroughCacheRuleModel] = Field(
        alias="pullThroughCacheRules"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    filter: Optional[LifecyclePolicyPreviewFilterModel] = Field(
        default=None, alias="filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitModel(
    BaseModel
):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[LifecyclePolicyPreviewFilterModel] = Field(
        default=None, alias="filter"
    )
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetLifecyclePolicyPreviewRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[LifecyclePolicyPreviewFilterModel] = Field(
        default=None, alias="filter"
    )


class ImageDetailModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    image_size_in_bytes: Optional[int] = Field(default=None, alias="imageSizeInBytes")
    image_pushed_at: Optional[datetime] = Field(default=None, alias="imagePushedAt")
    image_scan_status: Optional[ImageScanStatusModel] = Field(
        default=None, alias="imageScanStatus"
    )
    image_scan_findings_summary: Optional[ImageScanFindingsSummaryModel] = Field(
        default=None, alias="imageScanFindingsSummary"
    )
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )
    artifact_media_type: Optional[str] = Field(default=None, alias="artifactMediaType")
    last_recorded_pull_time: Optional[datetime] = Field(
        default=None, alias="lastRecordedPullTime"
    )


class LifecyclePolicyPreviewResultModel(BaseModel):
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    image_pushed_at: Optional[datetime] = Field(default=None, alias="imagePushedAt")
    action: Optional[LifecyclePolicyRuleActionModel] = Field(
        default=None, alias="action"
    )
    applied_rule_priority: Optional[int] = Field(
        default=None, alias="appliedRulePriority"
    )


class ListImagesRequestListImagesPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    filter: Optional[ListImagesFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImagesRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[ListImagesFilterModel] = Field(default=None, alias="filter")


class PackageVulnerabilityDetailsModel(BaseModel):
    cvss: Optional[List[CvssScoreModel]] = Field(default=None, alias="cvss")
    reference_urls: Optional[List[str]] = Field(default=None, alias="referenceUrls")
    related_vulnerabilities: Optional[List[str]] = Field(
        default=None, alias="relatedVulnerabilities"
    )
    source: Optional[str] = Field(default=None, alias="source")
    source_url: Optional[str] = Field(default=None, alias="sourceUrl")
    vendor_created_at: Optional[datetime] = Field(default=None, alias="vendorCreatedAt")
    vendor_severity: Optional[str] = Field(default=None, alias="vendorSeverity")
    vendor_updated_at: Optional[datetime] = Field(default=None, alias="vendorUpdatedAt")
    vulnerability_id: Optional[str] = Field(default=None, alias="vulnerabilityId")
    vulnerable_packages: Optional[List[VulnerablePackageModel]] = Field(
        default=None, alias="vulnerablePackages"
    )


class RemediationModel(BaseModel):
    recommendation: Optional[RecommendationModel] = Field(
        default=None, alias="recommendation"
    )


class RegistryScanningRuleModel(BaseModel):
    scan_frequency: Literal["CONTINUOUS_SCAN", "MANUAL", "SCAN_ON_PUSH"] = Field(
        alias="scanFrequency"
    )
    repository_filters: List[ScanningRepositoryFilterModel] = Field(
        alias="repositoryFilters"
    )


class RepositoryScanningConfigurationModel(BaseModel):
    repository_arn: Optional[str] = Field(default=None, alias="repositoryArn")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    scan_on_push: Optional[bool] = Field(default=None, alias="scanOnPush")
    scan_frequency: Optional[
        Literal["CONTINUOUS_SCAN", "MANUAL", "SCAN_ON_PUSH"]
    ] = Field(default=None, alias="scanFrequency")
    applied_scan_filters: Optional[List[ScanningRepositoryFilterModel]] = Field(
        default=None, alias="appliedScanFilters"
    )


class ReplicationRuleModel(BaseModel):
    destinations: List[ReplicationDestinationModel] = Field(alias="destinations")
    repository_filters: Optional[List[RepositoryFilterModel]] = Field(
        default=None, alias="repositoryFilters"
    )


class ResourceModel(BaseModel):
    details: Optional[ResourceDetailsModel] = Field(default=None, alias="details")
    id: Optional[str] = Field(default=None, alias="id")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[str] = Field(default=None, alias="type")


class BatchDeleteImageResponseModel(BaseModel):
    image_ids: List[ImageIdentifierModel] = Field(alias="imageIds")
    failures: List[ImageFailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetImageResponseModel(BaseModel):
    images: List[ImageModel] = Field(alias="images")
    failures: List[ImageFailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutImageResponseModel(BaseModel):
    image: ImageModel = Field(alias="image")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryResponseModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryResponseModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRepositoriesResponseModel(BaseModel):
    repositories: List[RepositoryModel] = Field(alias="repositories")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScoreDetailsModel(BaseModel):
    cvss: Optional[CvssScoreDetailsModel] = Field(default=None, alias="cvss")


class DescribeImagesResponseModel(BaseModel):
    image_details: List[ImageDetailModel] = Field(alias="imageDetails")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLifecyclePolicyPreviewResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    lifecycle_policy_text: str = Field(alias="lifecyclePolicyText")
    status: Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"] = Field(
        alias="status"
    )
    next_token: str = Field(alias="nextToken")
    preview_results: List[LifecyclePolicyPreviewResultModel] = Field(
        alias="previewResults"
    )
    summary: LifecyclePolicyPreviewSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRegistryScanningConfigurationRequestModel(BaseModel):
    scan_type: Optional[Literal["BASIC", "ENHANCED"]] = Field(
        default=None, alias="scanType"
    )
    rules: Optional[Sequence[RegistryScanningRuleModel]] = Field(
        default=None, alias="rules"
    )


class RegistryScanningConfigurationModel(BaseModel):
    scan_type: Optional[Literal["BASIC", "ENHANCED"]] = Field(
        default=None, alias="scanType"
    )
    rules: Optional[List[RegistryScanningRuleModel]] = Field(
        default=None, alias="rules"
    )


class BatchGetRepositoryScanningConfigurationResponseModel(BaseModel):
    scanning_configurations: List[RepositoryScanningConfigurationModel] = Field(
        alias="scanningConfigurations"
    )
    failures: List[RepositoryScanningConfigurationFailureModel] = Field(
        alias="failures"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationConfigurationModel(BaseModel):
    rules: List[ReplicationRuleModel] = Field(alias="rules")


class EnhancedImageScanFindingModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    description: Optional[str] = Field(default=None, alias="description")
    finding_arn: Optional[str] = Field(default=None, alias="findingArn")
    first_observed_at: Optional[datetime] = Field(default=None, alias="firstObservedAt")
    last_observed_at: Optional[datetime] = Field(default=None, alias="lastObservedAt")
    package_vulnerability_details: Optional[PackageVulnerabilityDetailsModel] = Field(
        default=None, alias="packageVulnerabilityDetails"
    )
    remediation: Optional[RemediationModel] = Field(default=None, alias="remediation")
    resources: Optional[List[ResourceModel]] = Field(default=None, alias="resources")
    score: Optional[float] = Field(default=None, alias="score")
    score_details: Optional[ScoreDetailsModel] = Field(
        default=None, alias="scoreDetails"
    )
    severity: Optional[str] = Field(default=None, alias="severity")
    status: Optional[str] = Field(default=None, alias="status")
    title: Optional[str] = Field(default=None, alias="title")
    type: Optional[str] = Field(default=None, alias="type")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class GetRegistryScanningConfigurationResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    scanning_configuration: RegistryScanningConfigurationModel = Field(
        alias="scanningConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRegistryScanningConfigurationResponseModel(BaseModel):
    registry_scanning_configuration: RegistryScanningConfigurationModel = Field(
        alias="registryScanningConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRegistryResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    replication_configuration: ReplicationConfigurationModel = Field(
        alias="replicationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutReplicationConfigurationRequestModel(BaseModel):
    replication_configuration: ReplicationConfigurationModel = Field(
        alias="replicationConfiguration"
    )


class PutReplicationConfigurationResponseModel(BaseModel):
    replication_configuration: ReplicationConfigurationModel = Field(
        alias="replicationConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageScanFindingsModel(BaseModel):
    image_scan_completed_at: Optional[datetime] = Field(
        default=None, alias="imageScanCompletedAt"
    )
    vulnerability_source_updated_at: Optional[datetime] = Field(
        default=None, alias="vulnerabilitySourceUpdatedAt"
    )
    finding_severity_counts: Optional[
        Dict[
            Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNDEFINED"],
            int,
        ]
    ] = Field(default=None, alias="findingSeverityCounts")
    findings: Optional[List[ImageScanFindingModel]] = Field(
        default=None, alias="findings"
    )
    enhanced_findings: Optional[List[EnhancedImageScanFindingModel]] = Field(
        default=None, alias="enhancedFindings"
    )


class DescribeImageScanFindingsResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    image_id: ImageIdentifierModel = Field(alias="imageId")
    image_scan_status: ImageScanStatusModel = Field(alias="imageScanStatus")
    image_scan_findings: ImageScanFindingsModel = Field(alias="imageScanFindings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
