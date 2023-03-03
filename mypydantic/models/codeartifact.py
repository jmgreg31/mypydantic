# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssetSummaryModel(BaseModel):
    name: str = Field(alias="name")
    size: Optional[int] = Field(default=None, alias="size")
    hashes: Optional[Dict[Literal["MD5", "SHA-1", "SHA-256", "SHA-512"], str]] = Field(
        default=None, alias="hashes"
    )


class AssociateExternalConnectionRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    external_connection: str = Field(alias="externalConnection")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CopyPackageVersionsRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    source_repository: str = Field(alias="sourceRepository")
    destination_repository: str = Field(alias="destinationRepository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    versions: Optional[Sequence[str]] = Field(default=None, alias="versions")
    version_revisions: Optional[Mapping[str, str]] = Field(
        default=None, alias="versionRevisions"
    )
    allow_overwrite: Optional[bool] = Field(default=None, alias="allowOverwrite")
    include_from_upstream: Optional[bool] = Field(
        default=None, alias="includeFromUpstream"
    )


class PackageVersionErrorModel(BaseModel):
    error_code: Optional[
        Literal[
            "ALREADY_EXISTS",
            "MISMATCHED_REVISION",
            "MISMATCHED_STATUS",
            "NOT_ALLOWED",
            "NOT_FOUND",
            "SKIPPED",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class SuccessfulPackageVersionInfoModel(BaseModel):
    revision: Optional[str] = Field(default=None, alias="revision")
    status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="status")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class DomainDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    owner: Optional[str] = Field(default=None, alias="owner")
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[Literal["Active", "Deleted"]] = Field(default=None, alias="status")
    created_time: Optional[datetime] = Field(default=None, alias="createdTime")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    repository_count: Optional[int] = Field(default=None, alias="repositoryCount")
    asset_size_bytes: Optional[int] = Field(default=None, alias="assetSizeBytes")
    s3_bucket_arn: Optional[str] = Field(default=None, alias="s3BucketArn")


class UpstreamRepositoryModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")


class DeleteDomainPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    policy_revision: Optional[str] = Field(default=None, alias="policyRevision")


class ResourcePolicyModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    revision: Optional[str] = Field(default=None, alias="revision")
    document: Optional[str] = Field(default=None, alias="document")


class DeleteDomainRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class DeletePackageRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class DeletePackageVersionsRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    versions: Sequence[str] = Field(alias="versions")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    expected_status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="expectedStatus")


class DeleteRepositoryPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    policy_revision: Optional[str] = Field(default=None, alias="policyRevision")


class DeleteRepositoryRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class DescribeDomainRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class DescribePackageRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class DescribePackageVersionRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class DescribeRepositoryRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class DisassociateExternalConnectionRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    external_connection: str = Field(alias="externalConnection")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class DisposePackageVersionsRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    versions: Sequence[str] = Field(alias="versions")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    version_revisions: Optional[Mapping[str, str]] = Field(
        default=None, alias="versionRevisions"
    )
    expected_status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="expectedStatus")


class DomainEntryPointModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    external_connection_name: Optional[str] = Field(
        default=None, alias="externalConnectionName"
    )


class DomainSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    owner: Optional[str] = Field(default=None, alias="owner")
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[Literal["Active", "Deleted"]] = Field(default=None, alias="status")
    created_time: Optional[datetime] = Field(default=None, alias="createdTime")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")


class GetAuthorizationTokenRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")


class GetDomainPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class GetPackageVersionAssetRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    asset: str = Field(alias="asset")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package_version_revision: Optional[str] = Field(
        default=None, alias="packageVersionRevision"
    )


class GetPackageVersionReadmeRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class GetRepositoryEndpointRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class GetRepositoryPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")


class LicenseInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    url: Optional[str] = Field(default=None, alias="url")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDomainsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPackageVersionAssetsRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPackageVersionDependenciesRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PackageDependencyModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package: Optional[str] = Field(default=None, alias="package")
    dependency_type: Optional[str] = Field(default=None, alias="dependencyType")
    version_requirement: Optional[str] = Field(default=None, alias="versionRequirement")


class ListPackageVersionsRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="status")
    sort_by: Optional[Literal["PUBLISHED_TIME"]] = Field(default=None, alias="sortBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    origin_type: Optional[Literal["EXTERNAL", "INTERNAL", "UNKNOWN"]] = Field(
        default=None, alias="originType"
    )


class ListPackagesRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="format"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package_prefix: Optional[str] = Field(default=None, alias="packagePrefix")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    publish: Optional[Literal["ALLOW", "BLOCK"]] = Field(default=None, alias="publish")
    upstream: Optional[Literal["ALLOW", "BLOCK"]] = Field(
        default=None, alias="upstream"
    )


class ListRepositoriesInDomainRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    administrator_account: Optional[str] = Field(
        default=None, alias="administratorAccount"
    )
    repository_prefix: Optional[str] = Field(default=None, alias="repositoryPrefix")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RepositorySummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    administrator_account: Optional[str] = Field(
        default=None, alias="administratorAccount"
    )
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")


class ListRepositoriesRequestModel(BaseModel):
    repository_prefix: Optional[str] = Field(default=None, alias="repositoryPrefix")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PackageOriginRestrictionsModel(BaseModel):
    publish: Literal["ALLOW", "BLOCK"] = Field(alias="publish")
    upstream: Literal["ALLOW", "BLOCK"] = Field(alias="upstream")


class PutDomainPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    policy_document: str = Field(alias="policyDocument")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    policy_revision: Optional[str] = Field(default=None, alias="policyRevision")


class PutRepositoryPermissionsPolicyRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    policy_document: str = Field(alias="policyDocument")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    policy_revision: Optional[str] = Field(default=None, alias="policyRevision")


class RepositoryExternalConnectionInfoModel(BaseModel):
    external_connection_name: Optional[str] = Field(
        default=None, alias="externalConnectionName"
    )
    package_format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="packageFormat"
    )
    status: Optional[Literal["Available"]] = Field(default=None, alias="status")


class UpstreamRepositoryInfoModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdatePackageVersionsStatusRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    versions: Sequence[str] = Field(alias="versions")
    target_status: Literal[
        "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
    ] = Field(alias="targetStatus")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    version_revisions: Optional[Mapping[str, str]] = Field(
        default=None, alias="versionRevisions"
    )
    expected_status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="expectedStatus")


class GetAuthorizationTokenResultModel(BaseModel):
    authorization_token: str = Field(alias="authorizationToken")
    expiration: datetime = Field(alias="expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPackageVersionAssetResultModel(BaseModel):
    asset: Type[StreamingBody] = Field(alias="asset")
    asset_name: str = Field(alias="assetName")
    package_version: str = Field(alias="packageVersion")
    package_version_revision: str = Field(alias="packageVersionRevision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPackageVersionReadmeResultModel(BaseModel):
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    namespace: str = Field(alias="namespace")
    package: str = Field(alias="package")
    version: str = Field(alias="version")
    version_revision: str = Field(alias="versionRevision")
    readme: str = Field(alias="readme")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryEndpointResultModel(BaseModel):
    repository_endpoint: str = Field(alias="repositoryEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackageVersionAssetsResultModel(BaseModel):
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    namespace: str = Field(alias="namespace")
    package: str = Field(alias="package")
    version: str = Field(alias="version")
    version_revision: str = Field(alias="versionRevision")
    next_token: str = Field(alias="nextToken")
    assets: List[AssetSummaryModel] = Field(alias="assets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyPackageVersionsResultModel(BaseModel):
    successful_versions: Dict[str, SuccessfulPackageVersionInfoModel] = Field(
        alias="successfulVersions"
    )
    failed_versions: Dict[str, PackageVersionErrorModel] = Field(alias="failedVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePackageVersionsResultModel(BaseModel):
    successful_versions: Dict[str, SuccessfulPackageVersionInfoModel] = Field(
        alias="successfulVersions"
    )
    failed_versions: Dict[str, PackageVersionErrorModel] = Field(alias="failedVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisposePackageVersionsResultModel(BaseModel):
    successful_versions: Dict[str, SuccessfulPackageVersionInfoModel] = Field(
        alias="successfulVersions"
    )
    failed_versions: Dict[str, PackageVersionErrorModel] = Field(alias="failedVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePackageVersionsStatusResultModel(BaseModel):
    successful_versions: Dict[str, SuccessfulPackageVersionInfoModel] = Field(
        alias="successfulVersions"
    )
    failed_versions: Dict[str, PackageVersionErrorModel] = Field(alias="failedVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceResultModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateDomainResultModel(BaseModel):
    domain: DomainDescriptionModel = Field(alias="domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResultModel(BaseModel):
    domain: DomainDescriptionModel = Field(alias="domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainResultModel(BaseModel):
    domain: DomainDescriptionModel = Field(alias="domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    description: Optional[str] = Field(default=None, alias="description")
    upstreams: Optional[Sequence[UpstreamRepositoryModel]] = Field(
        default=None, alias="upstreams"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateRepositoryRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    description: Optional[str] = Field(default=None, alias="description")
    upstreams: Optional[Sequence[UpstreamRepositoryModel]] = Field(
        default=None, alias="upstreams"
    )


class DeleteDomainPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDomainPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRepositoryPermissionsPolicyResultModel(BaseModel):
    policy: ResourcePolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PackageVersionOriginModel(BaseModel):
    domain_entry_point: Optional[DomainEntryPointModel] = Field(
        default=None, alias="domainEntryPoint"
    )
    origin_type: Optional[Literal["EXTERNAL", "INTERNAL", "UNKNOWN"]] = Field(
        default=None, alias="originType"
    )


class ListDomainsResultModel(BaseModel):
    domains: List[DomainSummaryModel] = Field(alias="domains")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsRequestListDomainsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    package_version: str = Field(alias="packageVersion")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackageVersionsRequestListPackageVersionsPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="status")
    sort_by: Optional[Literal["PUBLISHED_TIME"]] = Field(default=None, alias="sortBy")
    origin_type: Optional[Literal["EXTERNAL", "INTERNAL", "UNKNOWN"]] = Field(
        default=None, alias="originType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackagesRequestListPackagesPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="format"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package_prefix: Optional[str] = Field(default=None, alias="packagePrefix")
    publish: Optional[Literal["ALLOW", "BLOCK"]] = Field(default=None, alias="publish")
    upstream: Optional[Literal["ALLOW", "BLOCK"]] = Field(
        default=None, alias="upstream"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateModel(BaseModel):
    domain: str = Field(alias="domain")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    administrator_account: Optional[str] = Field(
        default=None, alias="administratorAccount"
    )
    repository_prefix: Optional[str] = Field(default=None, alias="repositoryPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositoriesRequestListRepositoriesPaginateModel(BaseModel):
    repository_prefix: Optional[str] = Field(default=None, alias="repositoryPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPackageVersionDependenciesResultModel(BaseModel):
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    namespace: str = Field(alias="namespace")
    package: str = Field(alias="package")
    version: str = Field(alias="version")
    version_revision: str = Field(alias="versionRevision")
    next_token: str = Field(alias="nextToken")
    dependencies: List[PackageDependencyModel] = Field(alias="dependencies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositoriesInDomainResultModel(BaseModel):
    repositories: List[RepositorySummaryModel] = Field(alias="repositories")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositoriesResultModel(BaseModel):
    repositories: List[RepositorySummaryModel] = Field(alias="repositories")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PackageOriginConfigurationModel(BaseModel):
    restrictions: Optional[PackageOriginRestrictionsModel] = Field(
        default=None, alias="restrictions"
    )


class PutPackageOriginConfigurationRequestModel(BaseModel):
    domain: str = Field(alias="domain")
    repository: str = Field(alias="repository")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    package: str = Field(alias="package")
    restrictions: PackageOriginRestrictionsModel = Field(alias="restrictions")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    namespace: Optional[str] = Field(default=None, alias="namespace")


class RepositoryDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    administrator_account: Optional[str] = Field(
        default=None, alias="administratorAccount"
    )
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    domain_owner: Optional[str] = Field(default=None, alias="domainOwner")
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")
    upstreams: Optional[List[UpstreamRepositoryInfoModel]] = Field(
        default=None, alias="upstreams"
    )
    external_connections: Optional[List[RepositoryExternalConnectionInfoModel]] = Field(
        default=None, alias="externalConnections"
    )


class PackageVersionDescriptionModel(BaseModel):
    format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="format"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package_name: Optional[str] = Field(default=None, alias="packageName")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    version: Optional[str] = Field(default=None, alias="version")
    summary: Optional[str] = Field(default=None, alias="summary")
    home_page: Optional[str] = Field(default=None, alias="homePage")
    source_code_repository: Optional[str] = Field(
        default=None, alias="sourceCodeRepository"
    )
    published_time: Optional[datetime] = Field(default=None, alias="publishedTime")
    licenses: Optional[List[LicenseInfoModel]] = Field(default=None, alias="licenses")
    revision: Optional[str] = Field(default=None, alias="revision")
    status: Optional[
        Literal[
            "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
        ]
    ] = Field(default=None, alias="status")
    origin: Optional[PackageVersionOriginModel] = Field(default=None, alias="origin")


class PackageVersionSummaryModel(BaseModel):
    version: str = Field(alias="version")
    status: Literal[
        "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
    ] = Field(alias="status")
    revision: Optional[str] = Field(default=None, alias="revision")
    origin: Optional[PackageVersionOriginModel] = Field(default=None, alias="origin")


class PackageDescriptionModel(BaseModel):
    format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="format"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")
    name: Optional[str] = Field(default=None, alias="name")
    origin_configuration: Optional[PackageOriginConfigurationModel] = Field(
        default=None, alias="originConfiguration"
    )


class PackageSummaryModel(BaseModel):
    format: Optional[Literal["maven", "npm", "nuget", "pypi"]] = Field(
        default=None, alias="format"
    )
    namespace: Optional[str] = Field(default=None, alias="namespace")
    package: Optional[str] = Field(default=None, alias="package")
    origin_configuration: Optional[PackageOriginConfigurationModel] = Field(
        default=None, alias="originConfiguration"
    )


class PutPackageOriginConfigurationResultModel(BaseModel):
    origin_configuration: PackageOriginConfigurationModel = Field(
        alias="originConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateExternalConnectionResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRepositoryResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateExternalConnectionResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRepositoryResultModel(BaseModel):
    repository: RepositoryDescriptionModel = Field(alias="repository")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackageVersionResultModel(BaseModel):
    package_version: PackageVersionDescriptionModel = Field(alias="packageVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackageVersionsResultModel(BaseModel):
    default_display_version: str = Field(alias="defaultDisplayVersion")
    format: Literal["maven", "npm", "nuget", "pypi"] = Field(alias="format")
    namespace: str = Field(alias="namespace")
    package: str = Field(alias="package")
    versions: List[PackageVersionSummaryModel] = Field(alias="versions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackageResultModel(BaseModel):
    package: PackageDescriptionModel = Field(alias="package")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePackageResultModel(BaseModel):
    deleted_package: PackageSummaryModel = Field(alias="deletedPackage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackagesResultModel(BaseModel):
    packages: List[PackageSummaryModel] = Field(alias="packages")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
