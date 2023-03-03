# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AffectedEntityModel(BaseModel):
    entity_arn: Optional[str] = Field(default=None, alias="entityArn")
    event_arn: Optional[str] = Field(default=None, alias="eventArn")
    entity_value: Optional[str] = Field(default=None, alias="entityValue")
    entity_url: Optional[str] = Field(default=None, alias="entityUrl")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    status_code: Optional[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]] = Field(
        default=None, alias="statusCode"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DateTimeRangeModel(BaseModel):
    from_: Optional[Union[datetime, str]] = Field(default=None, alias="from")
    to: Optional[Union[datetime, str]] = Field(default=None, alias="to")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAffectedAccountsForOrganizationRequestModel(BaseModel):
    event_arn: str = Field(alias="eventArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EventAccountFilterModel(BaseModel):
    event_arn: str = Field(alias="eventArn")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")


class OrganizationAffectedEntitiesErrorItemModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    event_arn: Optional[str] = Field(default=None, alias="eventArn")
    error_name: Optional[str] = Field(default=None, alias="errorName")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class DescribeEntityAggregatesRequestModel(BaseModel):
    event_arns: Optional[Sequence[str]] = Field(default=None, alias="eventArns")


class EntityAggregateModel(BaseModel):
    event_arn: Optional[str] = Field(default=None, alias="eventArn")
    count: Optional[int] = Field(default=None, alias="count")


class EventAggregateModel(BaseModel):
    aggregate_value: Optional[str] = Field(default=None, alias="aggregateValue")
    count: Optional[int] = Field(default=None, alias="count")


class OrganizationEventDetailsErrorItemModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    event_arn: Optional[str] = Field(default=None, alias="eventArn")
    error_name: Optional[str] = Field(default=None, alias="errorName")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class DescribeEventDetailsRequestModel(BaseModel):
    event_arns: Sequence[str] = Field(alias="eventArns")
    locale: Optional[str] = Field(default=None, alias="locale")


class EventDetailsErrorItemModel(BaseModel):
    event_arn: Optional[str] = Field(default=None, alias="eventArn")
    error_name: Optional[str] = Field(default=None, alias="errorName")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class EventTypeFilterModel(BaseModel):
    event_type_codes: Optional[Sequence[str]] = Field(
        default=None, alias="eventTypeCodes"
    )
    services: Optional[Sequence[str]] = Field(default=None, alias="services")
    event_type_categories: Optional[
        Sequence[
            Literal["accountNotification", "investigation", "issue", "scheduledChange"]
        ]
    ] = Field(default=None, alias="eventTypeCategories")


class EventTypeModel(BaseModel):
    service: Optional[str] = Field(default=None, alias="service")
    code: Optional[str] = Field(default=None, alias="code")
    category: Optional[
        Literal["accountNotification", "investigation", "issue", "scheduledChange"]
    ] = Field(default=None, alias="category")


class OrganizationEventModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    service: Optional[str] = Field(default=None, alias="service")
    event_type_code: Optional[str] = Field(default=None, alias="eventTypeCode")
    event_type_category: Optional[
        Literal["accountNotification", "investigation", "issue", "scheduledChange"]
    ] = Field(default=None, alias="eventTypeCategory")
    event_scope_code: Optional[Literal["ACCOUNT_SPECIFIC", "NONE", "PUBLIC"]] = Field(
        default=None, alias="eventScopeCode"
    )
    region: Optional[str] = Field(default=None, alias="region")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    status_code: Optional[Literal["closed", "open", "upcoming"]] = Field(
        default=None, alias="statusCode"
    )


class EventModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    service: Optional[str] = Field(default=None, alias="service")
    event_type_code: Optional[str] = Field(default=None, alias="eventTypeCode")
    event_type_category: Optional[
        Literal["accountNotification", "investigation", "issue", "scheduledChange"]
    ] = Field(default=None, alias="eventTypeCategory")
    region: Optional[str] = Field(default=None, alias="region")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    status_code: Optional[Literal["closed", "open", "upcoming"]] = Field(
        default=None, alias="statusCode"
    )
    event_scope_code: Optional[Literal["ACCOUNT_SPECIFIC", "NONE", "PUBLIC"]] = Field(
        default=None, alias="eventScopeCode"
    )


class EventDescriptionModel(BaseModel):
    latest_description: Optional[str] = Field(default=None, alias="latestDescription")


class EntityFilterModel(BaseModel):
    event_arns: Sequence[str] = Field(alias="eventArns")
    entity_arns: Optional[Sequence[str]] = Field(default=None, alias="entityArns")
    entity_values: Optional[Sequence[str]] = Field(default=None, alias="entityValues")
    last_updated_times: Optional[Sequence[DateTimeRangeModel]] = Field(
        default=None, alias="lastUpdatedTimes"
    )
    tags: Optional[Sequence[Mapping[str, str]]] = Field(default=None, alias="tags")
    status_codes: Optional[
        Sequence[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]]
    ] = Field(default=None, alias="statusCodes")


class EventFilterModel(BaseModel):
    event_arns: Optional[Sequence[str]] = Field(default=None, alias="eventArns")
    event_type_codes: Optional[Sequence[str]] = Field(
        default=None, alias="eventTypeCodes"
    )
    services: Optional[Sequence[str]] = Field(default=None, alias="services")
    regions: Optional[Sequence[str]] = Field(default=None, alias="regions")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="availabilityZones"
    )
    start_times: Optional[Sequence[DateTimeRangeModel]] = Field(
        default=None, alias="startTimes"
    )
    end_times: Optional[Sequence[DateTimeRangeModel]] = Field(
        default=None, alias="endTimes"
    )
    last_updated_times: Optional[Sequence[DateTimeRangeModel]] = Field(
        default=None, alias="lastUpdatedTimes"
    )
    entity_arns: Optional[Sequence[str]] = Field(default=None, alias="entityArns")
    entity_values: Optional[Sequence[str]] = Field(default=None, alias="entityValues")
    event_type_categories: Optional[
        Sequence[
            Literal["accountNotification", "investigation", "issue", "scheduledChange"]
        ]
    ] = Field(default=None, alias="eventTypeCategories")
    tags: Optional[Sequence[Mapping[str, str]]] = Field(default=None, alias="tags")
    event_status_codes: Optional[
        Sequence[Literal["closed", "open", "upcoming"]]
    ] = Field(default=None, alias="eventStatusCodes")


class OrganizationEventFilterModel(BaseModel):
    event_type_codes: Optional[Sequence[str]] = Field(
        default=None, alias="eventTypeCodes"
    )
    aws_account_ids: Optional[Sequence[str]] = Field(
        default=None, alias="awsAccountIds"
    )
    services: Optional[Sequence[str]] = Field(default=None, alias="services")
    regions: Optional[Sequence[str]] = Field(default=None, alias="regions")
    start_time: Optional[DateTimeRangeModel] = Field(default=None, alias="startTime")
    end_time: Optional[DateTimeRangeModel] = Field(default=None, alias="endTime")
    last_updated_time: Optional[DateTimeRangeModel] = Field(
        default=None, alias="lastUpdatedTime"
    )
    entity_arns: Optional[Sequence[str]] = Field(default=None, alias="entityArns")
    entity_values: Optional[Sequence[str]] = Field(default=None, alias="entityValues")
    event_type_categories: Optional[
        Sequence[
            Literal["accountNotification", "investigation", "issue", "scheduledChange"]
        ]
    ] = Field(default=None, alias="eventTypeCategories")
    event_status_codes: Optional[
        Sequence[Literal["closed", "open", "upcoming"]]
    ] = Field(default=None, alias="eventStatusCodes")


class DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateModel(
    BaseModel
):
    event_arn: str = Field(alias="eventArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAffectedAccountsForOrganizationResponseModel(BaseModel):
    affected_accounts: List[str] = Field(alias="affectedAccounts")
    event_scope_code: Literal["ACCOUNT_SPECIFIC", "NONE", "PUBLIC"] = Field(
        alias="eventScopeCode"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAffectedEntitiesResponseModel(BaseModel):
    entities: List[AffectedEntityModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHealthServiceStatusForOrganizationResponseModel(BaseModel):
    health_service_access_status_for_organization: str = Field(
        alias="healthServiceAccessStatusForOrganization"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateModel(
    BaseModel
):
    organization_entity_filters: Sequence[EventAccountFilterModel] = Field(
        alias="organizationEntityFilters"
    )
    locale: Optional[str] = Field(default=None, alias="locale")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAffectedEntitiesForOrganizationRequestModel(BaseModel):
    organization_entity_filters: Sequence[EventAccountFilterModel] = Field(
        alias="organizationEntityFilters"
    )
    locale: Optional[str] = Field(default=None, alias="locale")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeEventDetailsForOrganizationRequestModel(BaseModel):
    organization_event_detail_filters: Sequence[EventAccountFilterModel] = Field(
        alias="organizationEventDetailFilters"
    )
    locale: Optional[str] = Field(default=None, alias="locale")


class DescribeAffectedEntitiesForOrganizationResponseModel(BaseModel):
    entities: List[AffectedEntityModel] = Field(alias="entities")
    failed_set: List[OrganizationAffectedEntitiesErrorItemModel] = Field(
        alias="failedSet"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEntityAggregatesResponseModel(BaseModel):
    entity_aggregates: List[EntityAggregateModel] = Field(alias="entityAggregates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventAggregatesResponseModel(BaseModel):
    event_aggregates: List[EventAggregateModel] = Field(alias="eventAggregates")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventTypesRequestDescribeEventTypesPaginateModel(BaseModel):
    filter: Optional[EventTypeFilterModel] = Field(default=None, alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventTypesRequestModel(BaseModel):
    filter: Optional[EventTypeFilterModel] = Field(default=None, alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeEventTypesResponseModel(BaseModel):
    event_types: List[EventTypeModel] = Field(alias="eventTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventsForOrganizationResponseModel(BaseModel):
    events: List[OrganizationEventModel] = Field(alias="events")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventsResponseModel(BaseModel):
    events: List[EventModel] = Field(alias="events")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventDetailsModel(BaseModel):
    event: Optional[EventModel] = Field(default=None, alias="event")
    event_description: Optional[EventDescriptionModel] = Field(
        default=None, alias="eventDescription"
    )
    event_metadata: Optional[Dict[str, str]] = Field(
        default=None, alias="eventMetadata"
    )


class OrganizationEventDetailsModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    event: Optional[EventModel] = Field(default=None, alias="event")
    event_description: Optional[EventDescriptionModel] = Field(
        default=None, alias="eventDescription"
    )
    event_metadata: Optional[Dict[str, str]] = Field(
        default=None, alias="eventMetadata"
    )


class DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateModel(BaseModel):
    filter: EntityFilterModel = Field(alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAffectedEntitiesRequestModel(BaseModel):
    filter: EntityFilterModel = Field(alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeEventAggregatesRequestDescribeEventAggregatesPaginateModel(BaseModel):
    aggregate_field: Literal["eventTypeCategory"] = Field(alias="aggregateField")
    filter: Optional[EventFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventAggregatesRequestModel(BaseModel):
    aggregate_field: Literal["eventTypeCategory"] = Field(alias="aggregateField")
    filter: Optional[EventFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeEventsRequestDescribeEventsPaginateModel(BaseModel):
    filter: Optional[EventFilterModel] = Field(default=None, alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsRequestModel(BaseModel):
    filter: Optional[EventFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    locale: Optional[str] = Field(default=None, alias="locale")


class DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateModel(
    BaseModel
):
    filter: Optional[OrganizationEventFilterModel] = Field(default=None, alias="filter")
    locale: Optional[str] = Field(default=None, alias="locale")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsForOrganizationRequestModel(BaseModel):
    filter: Optional[OrganizationEventFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    locale: Optional[str] = Field(default=None, alias="locale")


class DescribeEventDetailsResponseModel(BaseModel):
    successful_set: List[EventDetailsModel] = Field(alias="successfulSet")
    failed_set: List[EventDetailsErrorItemModel] = Field(alias="failedSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventDetailsForOrganizationResponseModel(BaseModel):
    successful_set: List[OrganizationEventDetailsModel] = Field(alias="successfulSet")
    failed_set: List[OrganizationEventDetailsErrorItemModel] = Field(alias="failedSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
