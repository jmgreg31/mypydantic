# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateDiscovererRequestModel(BaseModel):
    source_arn: str = Field(alias="SourceArn")
    description: Optional[str] = Field(default=None, alias="Description")
    cross_account: Optional[bool] = Field(default=None, alias="CrossAccount")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateRegistryRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateSchemaRequestModel(BaseModel):
    content: str = Field(alias="Content")
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    type: Literal["JSONSchemaDraft4", "OpenApi3"] = Field(alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteDiscovererRequestModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")


class DeleteRegistryRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")


class DeleteResourcePolicyRequestModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")


class DeleteSchemaRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")


class DeleteSchemaVersionRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: str = Field(alias="SchemaVersion")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeCodeBindingRequestModel(BaseModel):
    language: str = Field(alias="Language")
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")


class DescribeDiscovererRequestModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")


class DescribeRegistryRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")


class DescribeSchemaRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")


class DiscovererSummaryModel(BaseModel):
    discoverer_arn: Optional[str] = Field(default=None, alias="DiscovererArn")
    discoverer_id: Optional[str] = Field(default=None, alias="DiscovererId")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    state: Optional[Literal["STARTED", "STOPPED"]] = Field(default=None, alias="State")
    cross_account: Optional[bool] = Field(default=None, alias="CrossAccount")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ExportSchemaRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    type: str = Field(alias="Type")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")


class GetCodeBindingSourceRequestModel(BaseModel):
    language: str = Field(alias="Language")
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")


class GetDiscoveredSchemaRequestModel(BaseModel):
    events: Sequence[str] = Field(alias="Events")
    type: Literal["JSONSchemaDraft4", "OpenApi3"] = Field(alias="Type")


class GetResourcePolicyRequestModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDiscoverersRequestModel(BaseModel):
    discoverer_id_prefix: Optional[str] = Field(
        default=None, alias="DiscovererIdPrefix"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    source_arn_prefix: Optional[str] = Field(default=None, alias="SourceArnPrefix")


class ListRegistriesRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    registry_name_prefix: Optional[str] = Field(
        default=None, alias="RegistryNamePrefix"
    )
    scope: Optional[str] = Field(default=None, alias="Scope")


class RegistrySummaryModel(BaseModel):
    registry_arn: Optional[str] = Field(default=None, alias="RegistryArn")
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListSchemaVersionsRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SchemaVersionSummaryModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")
    type: Optional[Literal["JSONSchemaDraft4", "OpenApi3"]] = Field(
        default=None, alias="Type"
    )


class ListSchemasRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    schema_name_prefix: Optional[str] = Field(default=None, alias="SchemaNamePrefix")


class SchemaSummaryModel(BaseModel):
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    version_count: Optional[int] = Field(default=None, alias="VersionCount")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PutCodeBindingRequestModel(BaseModel):
    language: str = Field(alias="Language")
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")


class PutResourcePolicyRequestModel(BaseModel):
    policy: str = Field(alias="Policy")
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class SearchSchemaVersionSummaryModel(BaseModel):
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")
    type: Optional[Literal["JSONSchemaDraft4", "OpenApi3"]] = Field(
        default=None, alias="Type"
    )


class SearchSchemasRequestModel(BaseModel):
    keywords: str = Field(alias="Keywords")
    registry_name: str = Field(alias="RegistryName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StartDiscovererRequestModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")


class StopDiscovererRequestModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDiscovererRequestModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")
    description: Optional[str] = Field(default=None, alias="Description")
    cross_account: Optional[bool] = Field(default=None, alias="CrossAccount")


class UpdateRegistryRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateSchemaRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    client_token_id: Optional[str] = Field(default=None, alias="ClientTokenId")
    content: Optional[str] = Field(default=None, alias="Content")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["JSONSchemaDraft4", "OpenApi3"]] = Field(
        default=None, alias="Type"
    )


class CreateDiscovererResponseModel(BaseModel):
    description: str = Field(alias="Description")
    discoverer_arn: str = Field(alias="DiscovererArn")
    discoverer_id: str = Field(alias="DiscovererId")
    source_arn: str = Field(alias="SourceArn")
    state: Literal["STARTED", "STOPPED"] = Field(alias="State")
    cross_account: bool = Field(alias="CrossAccount")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRegistryResponseModel(BaseModel):
    description: str = Field(alias="Description")
    registry_arn: str = Field(alias="RegistryArn")
    registry_name: str = Field(alias="RegistryName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSchemaResponseModel(BaseModel):
    description: str = Field(alias="Description")
    last_modified: datetime = Field(alias="LastModified")
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    schema_version: str = Field(alias="SchemaVersion")
    tags: Dict[str, str] = Field(alias="Tags")
    type: str = Field(alias="Type")
    version_created_date: datetime = Field(alias="VersionCreatedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCodeBindingResponseModel(BaseModel):
    creation_date: datetime = Field(alias="CreationDate")
    last_modified: datetime = Field(alias="LastModified")
    schema_version: str = Field(alias="SchemaVersion")
    status: Literal["CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDiscovererResponseModel(BaseModel):
    description: str = Field(alias="Description")
    discoverer_arn: str = Field(alias="DiscovererArn")
    discoverer_id: str = Field(alias="DiscovererId")
    source_arn: str = Field(alias="SourceArn")
    state: Literal["STARTED", "STOPPED"] = Field(alias="State")
    cross_account: bool = Field(alias="CrossAccount")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRegistryResponseModel(BaseModel):
    description: str = Field(alias="Description")
    registry_arn: str = Field(alias="RegistryArn")
    registry_name: str = Field(alias="RegistryName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSchemaResponseModel(BaseModel):
    content: str = Field(alias="Content")
    description: str = Field(alias="Description")
    last_modified: datetime = Field(alias="LastModified")
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    schema_version: str = Field(alias="SchemaVersion")
    tags: Dict[str, str] = Field(alias="Tags")
    type: str = Field(alias="Type")
    version_created_date: datetime = Field(alias="VersionCreatedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportSchemaResponseModel(BaseModel):
    content: str = Field(alias="Content")
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    schema_version: str = Field(alias="SchemaVersion")
    type: str = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCodeBindingSourceResponseModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDiscoveredSchemaResponseModel(BaseModel):
    content: str = Field(alias="Content")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutCodeBindingResponseModel(BaseModel):
    creation_date: datetime = Field(alias="CreationDate")
    last_modified: datetime = Field(alias="LastModified")
    schema_version: str = Field(alias="SchemaVersion")
    status: Literal["CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDiscovererResponseModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")
    state: Literal["STARTED", "STOPPED"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDiscovererResponseModel(BaseModel):
    discoverer_id: str = Field(alias="DiscovererId")
    state: Literal["STARTED", "STOPPED"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDiscovererResponseModel(BaseModel):
    description: str = Field(alias="Description")
    discoverer_arn: str = Field(alias="DiscovererArn")
    discoverer_id: str = Field(alias="DiscovererId")
    source_arn: str = Field(alias="SourceArn")
    state: Literal["STARTED", "STOPPED"] = Field(alias="State")
    cross_account: bool = Field(alias="CrossAccount")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegistryResponseModel(BaseModel):
    description: str = Field(alias="Description")
    registry_arn: str = Field(alias="RegistryArn")
    registry_name: str = Field(alias="RegistryName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSchemaResponseModel(BaseModel):
    description: str = Field(alias="Description")
    last_modified: datetime = Field(alias="LastModified")
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    schema_version: str = Field(alias="SchemaVersion")
    tags: Dict[str, str] = Field(alias="Tags")
    type: str = Field(alias="Type")
    version_created_date: datetime = Field(alias="VersionCreatedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCodeBindingRequestCodeBindingExistsWaitModel(BaseModel):
    language: str = Field(alias="Language")
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    schema_version: Optional[str] = Field(default=None, alias="SchemaVersion")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListDiscoverersResponseModel(BaseModel):
    discoverers: List[DiscovererSummaryModel] = Field(alias="Discoverers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDiscoverersRequestListDiscoverersPaginateModel(BaseModel):
    discoverer_id_prefix: Optional[str] = Field(
        default=None, alias="DiscovererIdPrefix"
    )
    source_arn_prefix: Optional[str] = Field(default=None, alias="SourceArnPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRegistriesRequestListRegistriesPaginateModel(BaseModel):
    registry_name_prefix: Optional[str] = Field(
        default=None, alias="RegistryNamePrefix"
    )
    scope: Optional[str] = Field(default=None, alias="Scope")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemaVersionsRequestListSchemaVersionsPaginateModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name: str = Field(alias="SchemaName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemasRequestListSchemasPaginateModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    schema_name_prefix: Optional[str] = Field(default=None, alias="SchemaNamePrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSchemasRequestSearchSchemasPaginateModel(BaseModel):
    keywords: str = Field(alias="Keywords")
    registry_name: str = Field(alias="RegistryName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRegistriesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    registries: List[RegistrySummaryModel] = Field(alias="Registries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemaVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schema_versions: List[SchemaVersionSummaryModel] = Field(alias="SchemaVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemasResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schemas: List[SchemaSummaryModel] = Field(alias="Schemas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchSchemaSummaryModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    schema_versions: Optional[List[SearchSchemaVersionSummaryModel]] = Field(
        default=None, alias="SchemaVersions"
    )


class SearchSchemasResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schemas: List[SearchSchemaSummaryModel] = Field(alias="Schemas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
