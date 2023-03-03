# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CartesianCoordinatesModel(BaseModel):
    x: float = Field(alias="x")
    y: float = Field(alias="y")
    z: Optional[float] = Field(default=None, alias="z")


class CreateDestinationRequestModel(BaseModel):
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    state: Optional[Literal["DECOMMISSIONED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateSiteRequestModel(BaseModel):
    name: str = Field(alias="name")
    country_code: str = Field(alias="countryCode")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class CreateWorkerFleetRequestModel(BaseModel):
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class OrientationModel(BaseModel):
    degrees: Optional[float] = Field(default=None, alias="degrees")


class VendorPropertiesModel(BaseModel):
    vendor_worker_id: str = Field(alias="vendorWorkerId")
    vendor_worker_ip_address: Optional[str] = Field(
        default=None, alias="vendorWorkerIpAddress"
    )
    vendor_additional_transient_properties: Optional[str] = Field(
        default=None, alias="vendorAdditionalTransientProperties"
    )
    vendor_additional_fixed_properties: Optional[str] = Field(
        default=None, alias="vendorAdditionalFixedProperties"
    )


class DeleteDestinationRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteSiteRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteWorkerFleetRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteWorkerRequestModel(BaseModel):
    id: str = Field(alias="id")


class DestinationModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    state: Literal["DECOMMISSIONED", "DISABLED", "ENABLED"] = Field(alias="state")
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class GetDestinationRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetSiteRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetWorkerFleetRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetWorkerRequestModel(BaseModel):
    id: str = Field(alias="id")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDestinationsRequestModel(BaseModel):
    site: str = Field(alias="site")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    state: Optional[Literal["DECOMMISSIONED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )


class ListSitesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SiteModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    country_code: str = Field(alias="countryCode")
    created_at: datetime = Field(alias="createdAt")


class ListWorkerFleetsRequestModel(BaseModel):
    site: str = Field(alias="site")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class WorkerFleetModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class ListWorkersRequestModel(BaseModel):
    site: str = Field(alias="site")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    fleet: Optional[str] = Field(default=None, alias="fleet")


class UpdateDestinationRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    state: Optional[Literal["DECOMMISSIONED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class UpdateSiteRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    country_code: Optional[str] = Field(default=None, alias="countryCode")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateWorkerFleetRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )


class PositionCoordinatesModel(BaseModel):
    cartesian_coordinates: Optional[CartesianCoordinatesModel] = Field(
        default=None, alias="cartesianCoordinates"
    )


class CreateDestinationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    state: Literal["DECOMMISSIONED", "DISABLED", "ENABLED"] = Field(alias="state")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSiteResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkerFleetResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkerResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    site: str = Field(alias="site")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDestinationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    state: Literal["DECOMMISSIONED", "DISABLED", "ENABLED"] = Field(alias="state")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSiteResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    country_code: str = Field(alias="countryCode")
    description: str = Field(alias="description")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkerFleetResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDestinationResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    updated_at: datetime = Field(alias="updatedAt")
    state: Literal["DECOMMISSIONED", "DISABLED", "ENABLED"] = Field(alias="state")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSiteResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    country_code: str = Field(alias="countryCode")
    description: str = Field(alias="description")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkerFleetResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    updated_at: datetime = Field(alias="updatedAt")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDestinationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    destinations: List[DestinationModel] = Field(alias="destinations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDestinationsRequestListDestinationsPaginateModel(BaseModel):
    site: str = Field(alias="site")
    state: Optional[Literal["DECOMMISSIONED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSitesRequestListSitesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkerFleetsRequestListWorkerFleetsPaginateModel(BaseModel):
    site: str = Field(alias="site")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkersRequestListWorkersPaginateModel(BaseModel):
    site: str = Field(alias="site")
    fleet: Optional[str] = Field(default=None, alias="fleet")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSitesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sites: List[SiteModel] = Field(alias="sites")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkerFleetsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    worker_fleets: List[WorkerFleetModel] = Field(alias="workerFleets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkerRequestModel(BaseModel):
    name: str = Field(alias="name")
    fleet: str = Field(alias="fleet")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    additional_transient_properties: Optional[str] = Field(
        default=None, alias="additionalTransientProperties"
    )
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )
    vendor_properties: Optional[VendorPropertiesModel] = Field(
        default=None, alias="vendorProperties"
    )
    position: Optional[PositionCoordinatesModel] = Field(default=None, alias="position")
    orientation: Optional[OrientationModel] = Field(default=None, alias="orientation")


class GetWorkerResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    fleet: str = Field(alias="fleet")
    site: str = Field(alias="site")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    name: str = Field(alias="name")
    additional_transient_properties: str = Field(alias="additionalTransientProperties")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    vendor_properties: VendorPropertiesModel = Field(alias="vendorProperties")
    position: PositionCoordinatesModel = Field(alias="position")
    orientation: OrientationModel = Field(alias="orientation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkerRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    additional_transient_properties: Optional[str] = Field(
        default=None, alias="additionalTransientProperties"
    )
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )
    vendor_properties: Optional[VendorPropertiesModel] = Field(
        default=None, alias="vendorProperties"
    )
    position: Optional[PositionCoordinatesModel] = Field(default=None, alias="position")
    orientation: Optional[OrientationModel] = Field(default=None, alias="orientation")


class UpdateWorkerResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    fleet: str = Field(alias="fleet")
    updated_at: datetime = Field(alias="updatedAt")
    name: str = Field(alias="name")
    additional_transient_properties: str = Field(alias="additionalTransientProperties")
    additional_fixed_properties: str = Field(alias="additionalFixedProperties")
    orientation: OrientationModel = Field(alias="orientation")
    vendor_properties: VendorPropertiesModel = Field(alias="vendorProperties")
    position: PositionCoordinatesModel = Field(alias="position")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkerModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    fleet: str = Field(alias="fleet")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    name: str = Field(alias="name")
    site: str = Field(alias="site")
    additional_transient_properties: Optional[str] = Field(
        default=None, alias="additionalTransientProperties"
    )
    additional_fixed_properties: Optional[str] = Field(
        default=None, alias="additionalFixedProperties"
    )
    vendor_properties: Optional[VendorPropertiesModel] = Field(
        default=None, alias="vendorProperties"
    )
    position: Optional[PositionCoordinatesModel] = Field(default=None, alias="position")
    orientation: Optional[OrientationModel] = Field(default=None, alias="orientation")


class ListWorkersResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workers: List[WorkerModel] = Field(alias="workers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
