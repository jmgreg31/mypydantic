# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelChangeSetRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    change_set_id: str = Field(alias="ChangeSetId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ChangeSetSummaryListItemModel(BaseModel):
    change_set_id: Optional[str] = Field(default=None, alias="ChangeSetId")
    change_set_arn: Optional[str] = Field(default=None, alias="ChangeSetArn")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    end_time: Optional[str] = Field(default=None, alias="EndTime")
    status: Optional[
        Literal["APPLYING", "CANCELLED", "FAILED", "PREPARING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    entity_id_list: Optional[List[str]] = Field(default=None, alias="EntityIdList")
    failure_code: Optional[Literal["CLIENT_ERROR", "SERVER_FAULT"]] = Field(
        default=None, alias="FailureCode"
    )


class EntityModel(BaseModel):
    type: str = Field(alias="Type")
    identifier: Optional[str] = Field(default=None, alias="Identifier")


class ErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DescribeChangeSetRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    change_set_id: str = Field(alias="ChangeSetId")


class DescribeEntityRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    entity_id: str = Field(alias="EntityId")


class EntitySummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    entity_type: Optional[str] = Field(default=None, alias="EntityType")
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    entity_arn: Optional[str] = Field(default=None, alias="EntityArn")
    last_modified_date: Optional[str] = Field(default=None, alias="LastModifiedDate")
    visibility: Optional[str] = Field(default=None, alias="Visibility")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value_list: Optional[Sequence[str]] = Field(default=None, alias="ValueList")


class SortModel(BaseModel):
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class CancelChangeSetResponseModel(BaseModel):
    change_set_id: str = Field(alias="ChangeSetId")
    change_set_arn: str = Field(alias="ChangeSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEntityResponseModel(BaseModel):
    entity_type: str = Field(alias="EntityType")
    entity_identifier: str = Field(alias="EntityIdentifier")
    entity_arn: str = Field(alias="EntityArn")
    last_modified_date: str = Field(alias="LastModifiedDate")
    details: str = Field(alias="Details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartChangeSetResponseModel(BaseModel):
    change_set_id: str = Field(alias="ChangeSetId")
    change_set_arn: str = Field(alias="ChangeSetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChangeSetsResponseModel(BaseModel):
    change_set_summary_list: List[ChangeSetSummaryListItemModel] = Field(
        alias="ChangeSetSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeSummaryModel(BaseModel):
    change_type: Optional[str] = Field(default=None, alias="ChangeType")
    entity: Optional[EntityModel] = Field(default=None, alias="Entity")
    details: Optional[str] = Field(default=None, alias="Details")
    error_detail_list: Optional[List[ErrorDetailModel]] = Field(
        default=None, alias="ErrorDetailList"
    )
    change_name: Optional[str] = Field(default=None, alias="ChangeName")


class ChangeModel(BaseModel):
    change_type: str = Field(alias="ChangeType")
    entity: EntityModel = Field(alias="Entity")
    details: str = Field(alias="Details")
    entity_tags: Optional[Sequence[TagModel]] = Field(default=None, alias="EntityTags")
    change_name: Optional[str] = Field(default=None, alias="ChangeName")


class ListTagsForResourceResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListEntitiesResponseModel(BaseModel):
    entity_summary_list: List[EntitySummaryModel] = Field(alias="EntitySummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChangeSetsRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    filter_list: Optional[Sequence[FilterModel]] = Field(
        default=None, alias="FilterList"
    )
    sort: Optional[SortModel] = Field(default=None, alias="Sort")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEntitiesRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    entity_type: str = Field(alias="EntityType")
    filter_list: Optional[Sequence[FilterModel]] = Field(
        default=None, alias="FilterList"
    )
    sort: Optional[SortModel] = Field(default=None, alias="Sort")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeChangeSetResponseModel(BaseModel):
    change_set_id: str = Field(alias="ChangeSetId")
    change_set_arn: str = Field(alias="ChangeSetArn")
    change_set_name: str = Field(alias="ChangeSetName")
    start_time: str = Field(alias="StartTime")
    end_time: str = Field(alias="EndTime")
    status: Literal[
        "APPLYING", "CANCELLED", "FAILED", "PREPARING", "SUCCEEDED"
    ] = Field(alias="Status")
    failure_code: Literal["CLIENT_ERROR", "SERVER_FAULT"] = Field(alias="FailureCode")
    failure_description: str = Field(alias="FailureDescription")
    change_set: List[ChangeSummaryModel] = Field(alias="ChangeSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartChangeSetRequestModel(BaseModel):
    catalog: str = Field(alias="Catalog")
    change_set: Sequence[ChangeModel] = Field(alias="ChangeSet")
    change_set_name: Optional[str] = Field(default=None, alias="ChangeSetName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    change_set_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="ChangeSetTags"
    )
