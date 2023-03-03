# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class EntitlementValueModel(BaseModel):
    integer_value: Optional[int] = Field(default=None, alias="IntegerValue")
    double_value: Optional[float] = Field(default=None, alias="DoubleValue")
    boolean_value: Optional[bool] = Field(default=None, alias="BooleanValue")
    string_value: Optional[str] = Field(default=None, alias="StringValue")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetEntitlementsRequestModel(BaseModel):
    product_code: str = Field(alias="ProductCode")
    filter: Optional[
        Mapping[Literal["CUSTOMER_IDENTIFIER", "DIMENSION"], Sequence[str]]
    ] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EntitlementModel(BaseModel):
    product_code: Optional[str] = Field(default=None, alias="ProductCode")
    dimension: Optional[str] = Field(default=None, alias="Dimension")
    customer_identifier: Optional[str] = Field(default=None, alias="CustomerIdentifier")
    value: Optional[EntitlementValueModel] = Field(default=None, alias="Value")
    expiration_date: Optional[datetime] = Field(default=None, alias="ExpirationDate")


class GetEntitlementsRequestGetEntitlementsPaginateModel(BaseModel):
    product_code: str = Field(alias="ProductCode")
    filter: Optional[
        Mapping[Literal["CUSTOMER_IDENTIFIER", "DIMENSION"], Sequence[str]]
    ] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetEntitlementsResultModel(BaseModel):
    entitlements: List[EntitlementModel] = Field(alias="Entitlements")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
