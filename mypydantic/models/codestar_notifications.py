# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TargetModel(BaseModel):
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    target_address: Optional[str] = Field(default=None, alias="TargetAddress")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteNotificationRuleRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DeleteTargetRequestModel(BaseModel):
    target_address: str = Field(alias="TargetAddress")
    force_unsubscribe_all: Optional[bool] = Field(
        default=None, alias="ForceUnsubscribeAll"
    )


class DescribeNotificationRuleRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class EventTypeSummaryModel(BaseModel):
    event_type_id: Optional[str] = Field(default=None, alias="EventTypeId")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    event_type_name: Optional[str] = Field(default=None, alias="EventTypeName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class TargetSummaryModel(BaseModel):
    target_address: Optional[str] = Field(default=None, alias="TargetAddress")
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    target_status: Optional[
        Literal["ACTIVE", "DEACTIVATED", "INACTIVE", "PENDING", "UNREACHABLE"]
    ] = Field(default=None, alias="TargetStatus")


class ListEventTypesFilterModel(BaseModel):
    name: Literal["RESOURCE_TYPE", "SERVICE_NAME"] = Field(alias="Name")
    value: str = Field(alias="Value")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListNotificationRulesFilterModel(BaseModel):
    name: Literal["CREATED_BY", "EVENT_TYPE_ID", "RESOURCE", "TARGET_ADDRESS"] = Field(
        alias="Name"
    )
    value: str = Field(alias="Value")


class NotificationRuleSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListTagsForResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class ListTargetsFilterModel(BaseModel):
    name: Literal["TARGET_ADDRESS", "TARGET_STATUS", "TARGET_TYPE"] = Field(
        alias="Name"
    )
    value: str = Field(alias="Value")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UnsubscribeRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    target_address: str = Field(alias="TargetAddress")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class CreateNotificationRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_type_ids: Sequence[str] = Field(alias="EventTypeIds")
    resource: str = Field(alias="Resource")
    targets: Sequence[TargetModel] = Field(alias="Targets")
    detail_type: Literal["BASIC", "FULL"] = Field(alias="DetailType")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class SubscribeRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    target: TargetModel = Field(alias="Target")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class UpdateNotificationRuleRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    event_type_ids: Optional[Sequence[str]] = Field(default=None, alias="EventTypeIds")
    targets: Optional[Sequence[TargetModel]] = Field(default=None, alias="Targets")
    detail_type: Optional[Literal["BASIC", "FULL"]] = Field(
        default=None, alias="DetailType"
    )


class CreateNotificationRuleResultModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNotificationRuleResultModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscribeResultModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnsubscribeResultModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventTypesResultModel(BaseModel):
    event_types: List[EventTypeSummaryModel] = Field(alias="EventTypes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNotificationRuleResultModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    event_types: List[EventTypeSummaryModel] = Field(alias="EventTypes")
    resource: str = Field(alias="Resource")
    targets: List[TargetSummaryModel] = Field(alias="Targets")
    detail_type: Literal["BASIC", "FULL"] = Field(alias="DetailType")
    created_by: str = Field(alias="CreatedBy")
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    last_modified_timestamp: datetime = Field(alias="LastModifiedTimestamp")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetsResultModel(BaseModel):
    targets: List[TargetSummaryModel] = Field(alias="Targets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventTypesRequestModel(BaseModel):
    filters: Optional[Sequence[ListEventTypesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEventTypesRequestListEventTypesPaginateModel(BaseModel):
    filters: Optional[Sequence[ListEventTypesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotificationRulesRequestListNotificationRulesPaginateModel(BaseModel):
    filters: Optional[Sequence[ListNotificationRulesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotificationRulesRequestModel(BaseModel):
    filters: Optional[Sequence[ListNotificationRulesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListNotificationRulesResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    notification_rules: List[NotificationRuleSummaryModel] = Field(
        alias="NotificationRules"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetsRequestListTargetsPaginateModel(BaseModel):
    filters: Optional[Sequence[ListTargetsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTargetsRequestModel(BaseModel):
    filters: Optional[Sequence[ListTargetsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
