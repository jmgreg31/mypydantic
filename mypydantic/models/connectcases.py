# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class FieldIdentifierModel(BaseModel):
    id: str = Field(alias="id")


class FieldErrorModel(BaseModel):
    error_code: str = Field(alias="errorCode")
    id: str = Field(alias="id")
    message: Optional[str] = Field(default=None, alias="message")


class GetFieldResponseModel(BaseModel):
    field_arn: str = Field(alias="fieldArn")
    field_id: str = Field(alias="fieldId")
    name: str = Field(alias="name")
    namespace: Literal["Custom", "System"] = Field(alias="namespace")
    type: Literal["Boolean", "DateTime", "Number", "SingleSelect", "Text"] = Field(
        alias="type"
    )
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FieldOptionModel(BaseModel):
    active: bool = Field(alias="active")
    name: str = Field(alias="name")
    value: str = Field(alias="value")


class FieldOptionErrorModel(BaseModel):
    error_code: str = Field(alias="errorCode")
    message: str = Field(alias="message")
    value: str = Field(alias="value")


class CaseSummaryModel(BaseModel):
    case_id: str = Field(alias="caseId")
    template_id: str = Field(alias="templateId")


class CommentContentModel(BaseModel):
    body: str = Field(alias="body")
    content_type: Literal["Text/Plain"] = Field(alias="contentType")


class ContactContentModel(BaseModel):
    channel: str = Field(alias="channel")
    connected_to_system_time: datetime = Field(alias="connectedToSystemTime")
    contact_arn: str = Field(alias="contactArn")


class ContactFilterModel(BaseModel):
    channel: Optional[Sequence[str]] = Field(default=None, alias="channel")
    contact_arn: Optional[str] = Field(default=None, alias="contactArn")


class ContactModel(BaseModel):
    contact_arn: str = Field(alias="contactArn")


class CreateDomainRequestModel(BaseModel):
    name: str = Field(alias="name")


class CreateFieldRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    name: str = Field(alias="name")
    type: Literal["Boolean", "DateTime", "Number", "SingleSelect", "Text"] = Field(
        alias="type"
    )
    description: Optional[str] = Field(default=None, alias="description")


class LayoutConfigurationModel(BaseModel):
    default_layout: Optional[str] = Field(default=None, alias="defaultLayout")


class RequiredFieldModel(BaseModel):
    field_id: str = Field(alias="fieldId")


class DeleteDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")


class DomainSummaryModel(BaseModel):
    domain_arn: str = Field(alias="domainArn")
    domain_id: str = Field(alias="domainId")
    name: str = Field(alias="name")


class RelatedItemEventIncludedDataModel(BaseModel):
    include_content: bool = Field(alias="includeContent")


class FieldItemModel(BaseModel):
    id: str = Field(alias="id")


class FieldSummaryModel(BaseModel):
    field_arn: str = Field(alias="fieldArn")
    field_id: str = Field(alias="fieldId")
    name: str = Field(alias="name")
    namespace: Literal["Custom", "System"] = Field(alias="namespace")
    type: Literal["Boolean", "DateTime", "Number", "SingleSelect", "Text"] = Field(
        alias="type"
    )


class FieldValueUnionModel(BaseModel):
    boolean_value: Optional[bool] = Field(default=None, alias="booleanValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")


class GetCaseEventConfigurationRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")


class GetDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")


class GetLayoutRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    layout_id: str = Field(alias="layoutId")


class GetTemplateRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    template_id: str = Field(alias="templateId")


class LayoutSummaryModel(BaseModel):
    layout_arn: str = Field(alias="layoutArn")
    layout_id: str = Field(alias="layoutId")
    name: str = Field(alias="name")


class ListCasesForContactRequestModel(BaseModel):
    contact_arn: str = Field(alias="contactArn")
    domain_id: str = Field(alias="domainId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDomainsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListFieldOptionsRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    field_id: str = Field(alias="fieldId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ListFieldsRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListLayoutsRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ListTemplatesRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    status: Optional[Sequence[Literal["Active", "Inactive"]]] = Field(
        default=None, alias="status"
    )


class TemplateSummaryModel(BaseModel):
    name: str = Field(alias="name")
    status: Literal["Active", "Inactive"] = Field(alias="status")
    template_arn: str = Field(alias="templateArn")
    template_id: str = Field(alias="templateId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class SortModel(BaseModel):
    field_id: str = Field(alias="fieldId")
    sort_order: Literal["Asc", "Desc"] = Field(alias="sortOrder")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateFieldRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    field_id: str = Field(alias="fieldId")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")


class BatchGetFieldRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    fields: Sequence[FieldIdentifierModel] = Field(alias="fields")


class CaseEventIncludedDataModel(BaseModel):
    fields: List[FieldIdentifierModel] = Field(alias="fields")


class GetCaseRequestModel(BaseModel):
    case_id: str = Field(alias="caseId")
    domain_id: str = Field(alias="domainId")
    fields: Sequence[FieldIdentifierModel] = Field(alias="fields")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class BatchGetFieldResponseModel(BaseModel):
    errors: List[FieldErrorModel] = Field(alias="errors")
    fields: List[GetFieldResponseModel] = Field(alias="fields")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCaseResponseModel(BaseModel):
    case_arn: str = Field(alias="caseArn")
    case_id: str = Field(alias="caseId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainResponseModel(BaseModel):
    domain_arn: str = Field(alias="domainArn")
    domain_id: str = Field(alias="domainId")
    domain_status: Literal["Active", "CreationFailed", "CreationInProgress"] = Field(
        alias="domainStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFieldResponseModel(BaseModel):
    field_arn: str = Field(alias="fieldArn")
    field_id: str = Field(alias="fieldId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLayoutResponseModel(BaseModel):
    layout_arn: str = Field(alias="layoutArn")
    layout_id: str = Field(alias="layoutId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRelatedItemResponseModel(BaseModel):
    related_item_arn: str = Field(alias="relatedItemArn")
    related_item_id: str = Field(alias="relatedItemId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTemplateResponseModel(BaseModel):
    template_arn: str = Field(alias="templateArn")
    template_id: str = Field(alias="templateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainResponseModel(BaseModel):
    created_time: datetime = Field(alias="createdTime")
    domain_arn: str = Field(alias="domainArn")
    domain_id: str = Field(alias="domainId")
    domain_status: Literal["Active", "CreationFailed", "CreationInProgress"] = Field(
        alias="domainStatus"
    )
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutFieldOptionsRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    field_id: str = Field(alias="fieldId")
    options: Sequence[FieldOptionModel] = Field(alias="options")


class ListFieldOptionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    options: List[FieldOptionModel] = Field(alias="options")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutFieldOptionsResponseModel(BaseModel):
    errors: List[FieldOptionErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCasesForContactResponseModel(BaseModel):
    cases: List[CaseSummaryModel] = Field(alias="cases")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RelatedItemContentModel(BaseModel):
    comment: Optional[CommentContentModel] = Field(default=None, alias="comment")
    contact: Optional[ContactContentModel] = Field(default=None, alias="contact")


class RelatedItemTypeFilterModel(BaseModel):
    comment: Optional[Mapping[str, Any]] = Field(default=None, alias="comment")
    contact: Optional[ContactFilterModel] = Field(default=None, alias="contact")


class RelatedItemInputContentModel(BaseModel):
    comment: Optional[CommentContentModel] = Field(default=None, alias="comment")
    contact: Optional[ContactModel] = Field(default=None, alias="contact")


class CreateTemplateRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    layout_configuration: Optional[LayoutConfigurationModel] = Field(
        default=None, alias="layoutConfiguration"
    )
    required_fields: Optional[Sequence[RequiredFieldModel]] = Field(
        default=None, alias="requiredFields"
    )
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="status"
    )


class GetTemplateResponseModel(BaseModel):
    description: str = Field(alias="description")
    layout_configuration: LayoutConfigurationModel = Field(alias="layoutConfiguration")
    name: str = Field(alias="name")
    required_fields: List[RequiredFieldModel] = Field(alias="requiredFields")
    status: Literal["Active", "Inactive"] = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    template_arn: str = Field(alias="templateArn")
    template_id: str = Field(alias="templateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    template_id: str = Field(alias="templateId")
    description: Optional[str] = Field(default=None, alias="description")
    layout_configuration: Optional[LayoutConfigurationModel] = Field(
        default=None, alias="layoutConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="name")
    required_fields: Optional[Sequence[RequiredFieldModel]] = Field(
        default=None, alias="requiredFields"
    )
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="status"
    )


class ListDomainsResponseModel(BaseModel):
    domains: List[DomainSummaryModel] = Field(alias="domains")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FieldGroupModel(BaseModel):
    fields: Sequence[FieldItemModel] = Field(alias="fields")
    name: Optional[str] = Field(default=None, alias="name")


class ListFieldsResponseModel(BaseModel):
    fields: List[FieldSummaryModel] = Field(alias="fields")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FieldValueModel(BaseModel):
    id: str = Field(alias="id")
    value: FieldValueUnionModel = Field(alias="value")


class ListLayoutsResponseModel(BaseModel):
    layouts: List[LayoutSummaryModel] = Field(alias="layouts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplatesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    templates: List[TemplateSummaryModel] = Field(alias="templates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchCasesRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    fields: Optional[Sequence[FieldIdentifierModel]] = Field(
        default=None, alias="fields"
    )
    filter: Optional[CaseFilterModel] = Field(default=None, alias="filter")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    search_term: Optional[str] = Field(default=None, alias="searchTerm")
    sorts: Optional[Sequence[SortModel]] = Field(default=None, alias="sorts")


class SearchCasesRequestSearchCasesPaginateModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    fields: Optional[Sequence[FieldIdentifierModel]] = Field(
        default=None, alias="fields"
    )
    filter: Optional[CaseFilterModel] = Field(default=None, alias="filter")
    search_term: Optional[str] = Field(default=None, alias="searchTerm")
    sorts: Optional[Sequence[SortModel]] = Field(default=None, alias="sorts")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class EventIncludedDataModel(BaseModel):
    case_data: Optional[CaseEventIncludedDataModel] = Field(
        default=None, alias="caseData"
    )
    related_item_data: Optional[RelatedItemEventIncludedDataModel] = Field(
        default=None, alias="relatedItemData"
    )


class SearchRelatedItemsResponseItemModel(BaseModel):
    association_time: datetime = Field(alias="associationTime")
    content: RelatedItemContentModel = Field(alias="content")
    related_item_id: str = Field(alias="relatedItemId")
    type: Literal["Comment", "Contact"] = Field(alias="type")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class SearchRelatedItemsRequestModel(BaseModel):
    case_id: str = Field(alias="caseId")
    domain_id: str = Field(alias="domainId")
    filters: Optional[Sequence[RelatedItemTypeFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchRelatedItemsRequestSearchRelatedItemsPaginateModel(BaseModel):
    case_id: str = Field(alias="caseId")
    domain_id: str = Field(alias="domainId")
    filters: Optional[Sequence[RelatedItemTypeFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class CreateRelatedItemRequestModel(BaseModel):
    case_id: str = Field(alias="caseId")
    content: RelatedItemInputContentModel = Field(alias="content")
    domain_id: str = Field(alias="domainId")
    type: Literal["Comment", "Contact"] = Field(alias="type")


class SectionModel(BaseModel):
    field_group: Optional[FieldGroupModel] = Field(default=None, alias="fieldGroup")


class CreateCaseRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    fields: Sequence[FieldValueModel] = Field(alias="fields")
    template_id: str = Field(alias="templateId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class FieldFilterModel(BaseModel):
    contains: Optional[FieldValueModel] = Field(default=None, alias="contains")
    equal_to: Optional[FieldValueModel] = Field(default=None, alias="equalTo")
    greater_than: Optional[FieldValueModel] = Field(default=None, alias="greaterThan")
    greater_than_or_equal_to: Optional[FieldValueModel] = Field(
        default=None, alias="greaterThanOrEqualTo"
    )
    less_than: Optional[FieldValueModel] = Field(default=None, alias="lessThan")
    less_than_or_equal_to: Optional[FieldValueModel] = Field(
        default=None, alias="lessThanOrEqualTo"
    )


class GetCaseResponseModel(BaseModel):
    fields: List[FieldValueModel] = Field(alias="fields")
    next_token: str = Field(alias="nextToken")
    tags: Dict[str, str] = Field(alias="tags")
    template_id: str = Field(alias="templateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchCasesResponseItemModel(BaseModel):
    case_id: str = Field(alias="caseId")
    fields: List[FieldValueModel] = Field(alias="fields")
    template_id: str = Field(alias="templateId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateCaseRequestModel(BaseModel):
    case_id: str = Field(alias="caseId")
    domain_id: str = Field(alias="domainId")
    fields: Sequence[FieldValueModel] = Field(alias="fields")


class EventBridgeConfigurationModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    included_data: Optional[EventIncludedDataModel] = Field(
        default=None, alias="includedData"
    )


class SearchRelatedItemsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    related_items: List[SearchRelatedItemsResponseItemModel] = Field(
        alias="relatedItems"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LayoutSectionsModel(BaseModel):
    sections: Optional[Sequence[SectionModel]] = Field(default=None, alias="sections")


class CaseFilterModel(BaseModel):
    and_all: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="andAll")
    field: Optional[FieldFilterModel] = Field(default=None, alias="field")
    not_: Optional[Dict[str, Any]] = Field(default=None, alias="not")


class SearchCasesResponseModel(BaseModel):
    cases: List[SearchCasesResponseItemModel] = Field(alias="cases")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCaseEventConfigurationResponseModel(BaseModel):
    event_bridge: EventBridgeConfigurationModel = Field(alias="eventBridge")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutCaseEventConfigurationRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    event_bridge: EventBridgeConfigurationModel = Field(alias="eventBridge")


class BasicLayoutModel(BaseModel):
    more_info: Optional[LayoutSectionsModel] = Field(default=None, alias="moreInfo")
    top_panel: Optional[LayoutSectionsModel] = Field(default=None, alias="topPanel")


class LayoutContentModel(BaseModel):
    basic: Optional[BasicLayoutModel] = Field(default=None, alias="basic")


class CreateLayoutRequestModel(BaseModel):
    content: LayoutContentModel = Field(alias="content")
    domain_id: str = Field(alias="domainId")
    name: str = Field(alias="name")


class GetLayoutResponseModel(BaseModel):
    content: LayoutContentModel = Field(alias="content")
    layout_arn: str = Field(alias="layoutArn")
    layout_id: str = Field(alias="layoutId")
    name: str = Field(alias="name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLayoutRequestModel(BaseModel):
    domain_id: str = Field(alias="domainId")
    layout_id: str = Field(alias="layoutId")
    content: Optional[LayoutContentModel] = Field(default=None, alias="content")
    name: Optional[str] = Field(default=None, alias="name")
