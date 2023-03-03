# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AuthorizationDataModel(BaseModel):
    authorization_token: Optional[str] = Field(default=None, alias="authorizationToken")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")


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


class CompleteLayerUploadRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    upload_id: str = Field(alias="uploadId")
    layer_digests: Sequence[str] = Field(alias="layerDigests")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class RepositoryCatalogDataInputModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    architectures: Optional[Sequence[str]] = Field(default=None, alias="architectures")
    operating_systems: Optional[Sequence[str]] = Field(
        default=None, alias="operatingSystems"
    )
    logo_image_blob: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="logoImageBlob")
    about_text: Optional[str] = Field(default=None, alias="aboutText")
    usage_text: Optional[str] = Field(default=None, alias="usageText")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class RepositoryCatalogDataModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    architectures: Optional[List[str]] = Field(default=None, alias="architectures")
    operating_systems: Optional[List[str]] = Field(
        default=None, alias="operatingSystems"
    )
    logo_url: Optional[str] = Field(default=None, alias="logoUrl")
    about_text: Optional[str] = Field(default=None, alias="aboutText")
    usage_text: Optional[str] = Field(default=None, alias="usageText")
    marketplace_certified: Optional[bool] = Field(
        default=None, alias="marketplaceCertified"
    )


class RepositoryModel(BaseModel):
    repository_arn: Optional[str] = Field(default=None, alias="repositoryArn")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    repository_uri: Optional[str] = Field(default=None, alias="repositoryUri")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class DeleteRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class DeleteRepositoryRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    force: Optional[bool] = Field(default=None, alias="force")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeImageTagsRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ImageDetailModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    image_size_in_bytes: Optional[int] = Field(default=None, alias="imageSizeInBytes")
    image_pushed_at: Optional[datetime] = Field(default=None, alias="imagePushedAt")
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )
    artifact_media_type: Optional[str] = Field(default=None, alias="artifactMediaType")


class DescribeRegistriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeRepositoriesRequestModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    repository_names: Optional[Sequence[str]] = Field(
        default=None, alias="repositoryNames"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RegistryCatalogDataModel(BaseModel):
    display_name: Optional[str] = Field(default=None, alias="displayName")


class GetRepositoryCatalogDataRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class GetRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class ReferencedImageDetailModel(BaseModel):
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")
    image_size_in_bytes: Optional[int] = Field(default=None, alias="imageSizeInBytes")
    image_pushed_at: Optional[datetime] = Field(default=None, alias="imagePushedAt")
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )
    artifact_media_type: Optional[str] = Field(default=None, alias="artifactMediaType")


class InitiateLayerUploadRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PutImageRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    image_manifest: str = Field(alias="imageManifest")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_manifest_media_type: Optional[str] = Field(
        default=None, alias="imageManifestMediaType"
    )
    image_tag: Optional[str] = Field(default=None, alias="imageTag")
    image_digest: Optional[str] = Field(default=None, alias="imageDigest")


class PutRegistryCatalogDataRequestModel(BaseModel):
    display_name: Optional[str] = Field(default=None, alias="displayName")


class RegistryAliasModel(BaseModel):
    name: str = Field(alias="name")
    status: Literal["ACTIVE", "PENDING", "REJECTED"] = Field(alias="status")
    primary_registry_alias: bool = Field(alias="primaryRegistryAlias")
    default_registry_alias: bool = Field(alias="defaultRegistryAlias")


class SetRepositoryPolicyRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    force: Optional[bool] = Field(default=None, alias="force")


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


class DeleteRepositoryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAuthorizationTokenResponseModel(BaseModel):
    authorization_data: AuthorizationDataModel = Field(alias="authorizationData")
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


class SetRepositoryPolicyResponseModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    repository_name: str = Field(alias="repositoryName")
    policy_text: str = Field(alias="policyText")
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


class DescribeImagesRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
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


class PutRepositoryCatalogDataRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    catalog_data: RepositoryCatalogDataInputModel = Field(alias="catalogData")
    registry_id: Optional[str] = Field(default=None, alias="registryId")


class CreateRepositoryRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    catalog_data: Optional[RepositoryCatalogDataInputModel] = Field(
        default=None, alias="catalogData"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class GetRepositoryCatalogDataResponseModel(BaseModel):
    catalog_data: RepositoryCatalogDataModel = Field(alias="catalogData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRepositoryCatalogDataResponseModel(BaseModel):
    catalog_data: RepositoryCatalogDataModel = Field(alias="catalogData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryResponseModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    catalog_data: RepositoryCatalogDataModel = Field(alias="catalogData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryResponseModel(BaseModel):
    repository: RepositoryModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRepositoriesResponseModel(BaseModel):
    repositories: List[RepositoryModel] = Field(alias="repositories")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageTagsRequestDescribeImageTagsPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeImagesRequestDescribeImagesPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    registry_id: Optional[str] = Field(default=None, alias="registryId")
    image_ids: Optional[Sequence[ImageIdentifierModel]] = Field(
        default=None, alias="imageIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRegistriesRequestDescribeRegistriesPaginateModel(BaseModel):
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


class DescribeImagesResponseModel(BaseModel):
    image_details: List[ImageDetailModel] = Field(alias="imageDetails")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegistryCatalogDataResponseModel(BaseModel):
    registry_catalog_data: RegistryCatalogDataModel = Field(alias="registryCatalogData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRegistryCatalogDataResponseModel(BaseModel):
    registry_catalog_data: RegistryCatalogDataModel = Field(alias="registryCatalogData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageTagDetailModel(BaseModel):
    image_tag: Optional[str] = Field(default=None, alias="imageTag")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    image_detail: Optional[ReferencedImageDetailModel] = Field(
        default=None, alias="imageDetail"
    )


class RegistryModel(BaseModel):
    registry_id: str = Field(alias="registryId")
    registry_arn: str = Field(alias="registryArn")
    registry_uri: str = Field(alias="registryUri")
    verified: bool = Field(alias="verified")
    aliases: List[RegistryAliasModel] = Field(alias="aliases")


class BatchDeleteImageResponseModel(BaseModel):
    image_ids: List[ImageIdentifierModel] = Field(alias="imageIds")
    failures: List[ImageFailureModel] = Field(alias="failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutImageResponseModel(BaseModel):
    image: ImageModel = Field(alias="image")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageTagsResponseModel(BaseModel):
    image_tag_details: List[ImageTagDetailModel] = Field(alias="imageTagDetails")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRegistriesResponseModel(BaseModel):
    registries: List[RegistryModel] = Field(alias="registries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
