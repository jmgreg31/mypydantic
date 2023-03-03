# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttributeValueModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeServicesRequestModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    format_version: Optional[str] = Field(default=None, alias="FormatVersion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ServiceModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    attribute_names: Optional[List[str]] = Field(default=None, alias="AttributeNames")


class FilterModel(BaseModel):
    type: Literal["TERM_MATCH"] = Field(alias="Type")
    field: str = Field(alias="Field")
    value: str = Field(alias="Value")


class GetAttributeValuesRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    attribute_name: str = Field(alias="AttributeName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetPriceListFileUrlRequestModel(BaseModel):
    price_list_arn: str = Field(alias="PriceListArn")
    file_format: str = Field(alias="FileFormat")


class ListPriceListsRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    effective_date: Union[datetime, str] = Field(alias="EffectiveDate")
    currency_code: str = Field(alias="CurrencyCode")
    region_code: Optional[str] = Field(default=None, alias="RegionCode")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PriceListModel(BaseModel):
    price_list_arn: Optional[str] = Field(default=None, alias="PriceListArn")
    region_code: Optional[str] = Field(default=None, alias="RegionCode")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    file_formats: Optional[List[str]] = Field(default=None, alias="FileFormats")


class DescribeServicesRequestDescribeServicesPaginateModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    format_version: Optional[str] = Field(default=None, alias="FormatVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAttributeValuesRequestGetAttributeValuesPaginateModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    attribute_name: str = Field(alias="AttributeName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPriceListsRequestListPriceListsPaginateModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    effective_date: Union[datetime, str] = Field(alias="EffectiveDate")
    currency_code: str = Field(alias="CurrencyCode")
    region_code: Optional[str] = Field(default=None, alias="RegionCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAttributeValuesResponseModel(BaseModel):
    attribute_values: List[AttributeValueModel] = Field(alias="AttributeValues")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPriceListFileUrlResponseModel(BaseModel):
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProductsResponseModel(BaseModel):
    format_version: str = Field(alias="FormatVersion")
    price_list: List[str] = Field(alias="PriceList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServicesResponseModel(BaseModel):
    services: List[ServiceModel] = Field(alias="Services")
    format_version: str = Field(alias="FormatVersion")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProductsRequestGetProductsPaginateModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    format_version: Optional[str] = Field(default=None, alias="FormatVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetProductsRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    format_version: Optional[str] = Field(default=None, alias="FormatVersion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPriceListsResponseModel(BaseModel):
    price_lists: List[PriceListModel] = Field(alias="PriceLists")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
