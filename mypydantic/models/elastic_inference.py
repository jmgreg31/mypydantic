# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceleratorTypeOfferingModel(BaseModel):
    accelerator_type: Optional[str] = Field(default=None, alias="acceleratorType")
    location_type: Optional[
        Literal["availability-zone", "availability-zone-id", "region"]
    ] = Field(default=None, alias="locationType")
    location: Optional[str] = Field(default=None, alias="location")


class KeyValuePairModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[int] = Field(default=None, alias="value")


class MemoryInfoModel(BaseModel):
    size_in_mi_b: Optional[int] = Field(default=None, alias="sizeInMiB")


class DescribeAcceleratorOfferingsRequestModel(BaseModel):
    location_type: Literal[
        "availability-zone", "availability-zone-id", "region"
    ] = Field(alias="locationType")
    accelerator_types: Optional[Sequence[str]] = Field(
        default=None, alias="acceleratorTypes"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ElasticInferenceAcceleratorHealthModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="status")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AcceleratorTypeModel(BaseModel):
    accelerator_type_name: Optional[str] = Field(
        default=None, alias="acceleratorTypeName"
    )
    memory_info: Optional[MemoryInfoModel] = Field(default=None, alias="memoryInfo")
    throughput_info: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="throughputInfo"
    )


class DescribeAcceleratorOfferingsResponseModel(BaseModel):
    accelerator_type_offerings: List[AcceleratorTypeOfferingModel] = Field(
        alias="acceleratorTypeOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAcceleratorsRequestModel(BaseModel):
    accelerator_ids: Optional[Sequence[str]] = Field(
        default=None, alias="acceleratorIds"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeAcceleratorsRequestDescribeAcceleratorsPaginateModel(BaseModel):
    accelerator_ids: Optional[Sequence[str]] = Field(
        default=None, alias="acceleratorIds"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ElasticInferenceAcceleratorModel(BaseModel):
    accelerator_health: Optional[ElasticInferenceAcceleratorHealthModel] = Field(
        default=None, alias="acceleratorHealth"
    )
    accelerator_type: Optional[str] = Field(default=None, alias="acceleratorType")
    accelerator_id: Optional[str] = Field(default=None, alias="acceleratorId")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    attached_resource: Optional[str] = Field(default=None, alias="attachedResource")


class DescribeAcceleratorTypesResponseModel(BaseModel):
    accelerator_types: List[AcceleratorTypeModel] = Field(alias="acceleratorTypes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAcceleratorsResponseModel(BaseModel):
    accelerator_set: List[ElasticInferenceAcceleratorModel] = Field(
        alias="acceleratorSet"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
