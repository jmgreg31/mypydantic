# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelZonalShiftRequestModel(BaseModel):
    zonal_shift_id: str = Field(alias="zonalShiftId")


class GetManagedResourceRequestModel(BaseModel):
    resource_identifier: str = Field(alias="resourceIdentifier")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ZonalShiftInResourceModel(BaseModel):
    applied_status: Literal["APPLIED", "NOT_APPLIED"] = Field(alias="appliedStatus")
    away_from: str = Field(alias="awayFrom")
    comment: str = Field(alias="comment")
    expiry_time: datetime = Field(alias="expiryTime")
    resource_identifier: str = Field(alias="resourceIdentifier")
    start_time: datetime = Field(alias="startTime")
    zonal_shift_id: str = Field(alias="zonalShiftId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListManagedResourcesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ManagedResourceSummaryModel(BaseModel):
    availability_zones: List[str] = Field(alias="availabilityZones")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")


class ListZonalShiftsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    status: Optional[Literal["ACTIVE", "CANCELED", "EXPIRED"]] = Field(
        default=None, alias="status"
    )


class ZonalShiftSummaryModel(BaseModel):
    away_from: str = Field(alias="awayFrom")
    comment: str = Field(alias="comment")
    expiry_time: datetime = Field(alias="expiryTime")
    resource_identifier: str = Field(alias="resourceIdentifier")
    start_time: datetime = Field(alias="startTime")
    status: Literal["ACTIVE", "CANCELED", "EXPIRED"] = Field(alias="status")
    zonal_shift_id: str = Field(alias="zonalShiftId")


class StartZonalShiftRequestModel(BaseModel):
    away_from: str = Field(alias="awayFrom")
    comment: str = Field(alias="comment")
    expires_in: str = Field(alias="expiresIn")
    resource_identifier: str = Field(alias="resourceIdentifier")


class UpdateZonalShiftRequestModel(BaseModel):
    zonal_shift_id: str = Field(alias="zonalShiftId")
    comment: Optional[str] = Field(default=None, alias="comment")
    expires_in: Optional[str] = Field(default=None, alias="expiresIn")


class ZonalShiftModel(BaseModel):
    away_from: str = Field(alias="awayFrom")
    comment: str = Field(alias="comment")
    expiry_time: datetime = Field(alias="expiryTime")
    resource_identifier: str = Field(alias="resourceIdentifier")
    start_time: datetime = Field(alias="startTime")
    status: Literal["ACTIVE", "CANCELED", "EXPIRED"] = Field(alias="status")
    zonal_shift_id: str = Field(alias="zonalShiftId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetManagedResourceResponseModel(BaseModel):
    applied_weights: Dict[str, float] = Field(alias="appliedWeights")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    zonal_shifts: List[ZonalShiftInResourceModel] = Field(alias="zonalShifts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedResourcesRequestListManagedResourcesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListZonalShiftsRequestListZonalShiftsPaginateModel(BaseModel):
    status: Optional[Literal["ACTIVE", "CANCELED", "EXPIRED"]] = Field(
        default=None, alias="status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListManagedResourcesResponseModel(BaseModel):
    items: List[ManagedResourceSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListZonalShiftsResponseModel(BaseModel):
    items: List[ZonalShiftSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
