# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteObjectRequestModel(BaseModel):
    path: str = Field(alias="Path")


class DescribeObjectRequestModel(BaseModel):
    path: str = Field(alias="Path")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetObjectRequestModel(BaseModel):
    path: str = Field(alias="Path")
    range: Optional[str] = Field(default=None, alias="Range")


class ItemModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["FOLDER", "OBJECT"]] = Field(default=None, alias="Type")
    etag: Optional[str] = Field(default=None, alias="ETag")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    content_length: Optional[int] = Field(default=None, alias="ContentLength")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListItemsRequestModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PutObjectRequestModel(BaseModel):
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Body")
    path: str = Field(alias="Path")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    cache_control: Optional[str] = Field(default=None, alias="CacheControl")
    storage_class: Optional[Literal["TEMPORAL"]] = Field(
        default=None, alias="StorageClass"
    )
    upload_availability: Optional[Literal["STANDARD", "STREAMING"]] = Field(
        default=None, alias="UploadAvailability"
    )


class DescribeObjectResponseModel(BaseModel):
    etag: str = Field(alias="ETag")
    content_type: str = Field(alias="ContentType")
    content_length: int = Field(alias="ContentLength")
    cache_control: str = Field(alias="CacheControl")
    last_modified: datetime = Field(alias="LastModified")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectResponseModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="Body")
    cache_control: str = Field(alias="CacheControl")
    content_range: str = Field(alias="ContentRange")
    content_length: int = Field(alias="ContentLength")
    content_type: str = Field(alias="ContentType")
    etag: str = Field(alias="ETag")
    last_modified: datetime = Field(alias="LastModified")
    status_code: int = Field(alias="StatusCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutObjectResponseModel(BaseModel):
    content_s_ha256: str = Field(alias="ContentSHA256")
    etag: str = Field(alias="ETag")
    storage_class: Literal["TEMPORAL"] = Field(alias="StorageClass")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListItemsResponseModel(BaseModel):
    items: List[ItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListItemsRequestListItemsPaginateModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
