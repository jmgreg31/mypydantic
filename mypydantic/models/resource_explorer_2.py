# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateDefaultViewInputRequestModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetViewErrorModel(BaseModel):
    error_message: str = Field(alias="ErrorMessage")
    view_arn: str = Field(alias="ViewArn")


class BatchGetViewInputRequestModel(BaseModel):
    view_arns: Optional[Sequence[str]] = Field(default=None, alias="ViewArns")


class CreateIndexInputRequestModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class IncludedPropertyModel(BaseModel):
    name: str = Field(alias="Name")


class SearchFilterModel(BaseModel):
    filter_string: str = Field(alias="FilterString")


class DeleteIndexInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DeleteViewInputRequestModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")


class GetViewInputRequestModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")


class IndexModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    region: Optional[str] = Field(default=None, alias="Region")
    type: Optional[Literal["AGGREGATOR", "LOCAL"]] = Field(default=None, alias="Type")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListIndexesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")
    type: Optional[Literal["AGGREGATOR", "LOCAL"]] = Field(default=None, alias="Type")


class ListSupportedResourceTypesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SupportedResourceTypeModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    service: Optional[str] = Field(default=None, alias="Service")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListViewsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResourceCountModel(BaseModel):
    complete: Optional[bool] = Field(default=None, alias="Complete")
    total_resources: Optional[int] = Field(default=None, alias="TotalResources")


class ResourcePropertyModel(BaseModel):
    data: Optional[Dict[str, Any]] = Field(default=None, alias="Data")
    last_reported_at: Optional[datetime] = Field(default=None, alias="LastReportedAt")
    name: Optional[str] = Field(default=None, alias="Name")


class SearchInputRequestModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    view_arn: Optional[str] = Field(default=None, alias="ViewArn")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateIndexTypeInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    type: Literal["AGGREGATOR", "LOCAL"] = Field(alias="Type")


class AssociateDefaultViewOutputModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIndexOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "UPDATING"] = Field(
        alias="State"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIndexOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "UPDATING"] = Field(
        alias="State"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteViewOutputModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDefaultViewOutputModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIndexOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    replicating_from: List[str] = Field(alias="ReplicatingFrom")
    replicating_to: List[str] = Field(alias="ReplicatingTo")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "UPDATING"] = Field(
        alias="State"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal["AGGREGATOR", "LOCAL"] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListViewsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    views: List[str] = Field(alias="Views")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIndexTypeOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    state: Literal["ACTIVE", "CREATING", "DELETED", "DELETING", "UPDATING"] = Field(
        alias="State"
    )
    type: Literal["AGGREGATOR", "LOCAL"] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateViewInputRequestModel(BaseModel):
    view_name: str = Field(alias="ViewName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    filters: Optional[SearchFilterModel] = Field(default=None, alias="Filters")
    included_properties: Optional[Sequence[IncludedPropertyModel]] = Field(
        default=None, alias="IncludedProperties"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateViewInputRequestModel(BaseModel):
    view_arn: str = Field(alias="ViewArn")
    filters: Optional[SearchFilterModel] = Field(default=None, alias="Filters")
    included_properties: Optional[Sequence[IncludedPropertyModel]] = Field(
        default=None, alias="IncludedProperties"
    )


class ViewModel(BaseModel):
    filters: Optional[SearchFilterModel] = Field(default=None, alias="Filters")
    included_properties: Optional[List[IncludedPropertyModel]] = Field(
        default=None, alias="IncludedProperties"
    )
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    owner: Optional[str] = Field(default=None, alias="Owner")
    scope: Optional[str] = Field(default=None, alias="Scope")
    view_arn: Optional[str] = Field(default=None, alias="ViewArn")


class ListIndexesOutputModel(BaseModel):
    indexes: List[IndexModel] = Field(alias="Indexes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIndexesInputListIndexesPaginateModel(BaseModel):
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")
    type: Optional[Literal["AGGREGATOR", "LOCAL"]] = Field(default=None, alias="Type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSupportedResourceTypesInputListSupportedResourceTypesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListViewsInputListViewsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchInputSearchPaginateModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    view_arn: Optional[str] = Field(default=None, alias="ViewArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSupportedResourceTypesOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    resource_types: List[SupportedResourceTypeModel] = Field(alias="ResourceTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    last_reported_at: Optional[datetime] = Field(default=None, alias="LastReportedAt")
    owning_account_id: Optional[str] = Field(default=None, alias="OwningAccountId")
    properties: Optional[List[ResourcePropertyModel]] = Field(
        default=None, alias="Properties"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    service: Optional[str] = Field(default=None, alias="Service")


class BatchGetViewOutputModel(BaseModel):
    errors: List[BatchGetViewErrorModel] = Field(alias="Errors")
    views: List[ViewModel] = Field(alias="Views")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateViewOutputModel(BaseModel):
    view: ViewModel = Field(alias="View")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetViewOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    view: ViewModel = Field(alias="View")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateViewOutputModel(BaseModel):
    view: ViewModel = Field(alias="View")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchOutputModel(BaseModel):
    count: ResourceCountModel = Field(alias="Count")
    next_token: str = Field(alias="NextToken")
    resources: List[ResourceModel] = Field(alias="Resources")
    view_arn: str = Field(alias="ViewArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
