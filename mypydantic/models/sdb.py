# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttributeModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    alternate_name_encoding: Optional[str] = Field(
        default=None, alias="AlternateNameEncoding"
    )
    alternate_value_encoding: Optional[str] = Field(
        default=None, alias="AlternateValueEncoding"
    )


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class UpdateConditionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")
    exists: Optional[bool] = Field(default=None, alias="Exists")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DomainMetadataRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetAttributesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    item_name: str = Field(alias="ItemName")
    attribute_names: Optional[Sequence[str]] = Field(
        default=None, alias="AttributeNames"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDomainsRequestModel(BaseModel):
    max_number_of_domains: Optional[int] = Field(
        default=None, alias="MaxNumberOfDomains"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ReplaceableAttributeModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    replace: Optional[bool] = Field(default=None, alias="Replace")


class SelectRequestModel(BaseModel):
    select_expression: str = Field(alias="SelectExpression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")


class DeletableItemModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="Attributes"
    )


class ItemModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: List[AttributeModel] = Field(alias="Attributes")
    alternate_name_encoding: Optional[str] = Field(
        default=None, alias="AlternateNameEncoding"
    )


class DeleteAttributesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    item_name: str = Field(alias="ItemName")
    attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    expected: Optional[UpdateConditionModel] = Field(default=None, alias="Expected")


class DomainMetadataResultModel(BaseModel):
    item_count: int = Field(alias="ItemCount")
    item_names_size_bytes: int = Field(alias="ItemNamesSizeBytes")
    attribute_name_count: int = Field(alias="AttributeNameCount")
    attribute_names_size_bytes: int = Field(alias="AttributeNamesSizeBytes")
    attribute_value_count: int = Field(alias="AttributeValueCount")
    attribute_values_size_bytes: int = Field(alias="AttributeValuesSizeBytes")
    timestamp: int = Field(alias="Timestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAttributesResultModel(BaseModel):
    attributes: List[AttributeModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsResultModel(BaseModel):
    domain_names: List[str] = Field(alias="DomainNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsRequestListDomainsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SelectRequestSelectPaginateModel(BaseModel):
    select_expression: str = Field(alias="SelectExpression")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PutAttributesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    item_name: str = Field(alias="ItemName")
    attributes: Sequence[ReplaceableAttributeModel] = Field(alias="Attributes")
    expected: Optional[UpdateConditionModel] = Field(default=None, alias="Expected")


class ReplaceableItemModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: Sequence[ReplaceableAttributeModel] = Field(alias="Attributes")


class BatchDeleteAttributesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    items: Sequence[DeletableItemModel] = Field(alias="Items")


class SelectResultModel(BaseModel):
    items: List[ItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutAttributesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    items: Sequence[ReplaceableItemModel] = Field(alias="Items")
