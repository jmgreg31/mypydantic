# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApiKeyFilterModel(BaseModel):
    key_status: Optional[Literal["Active", "Expired"]] = Field(
        default=None, alias="KeyStatus"
    )


class ApiKeyRestrictionsModel(BaseModel):
    allow_actions: Sequence[str] = Field(alias="AllowActions")
    allow_resources: Sequence[str] = Field(alias="AllowResources")
    allow_referers: Optional[Sequence[str]] = Field(default=None, alias="AllowReferers")


class AssociateTrackerConsumerRequestModel(BaseModel):
    consumer_arn: str = Field(alias="ConsumerArn")
    tracker_name: str = Field(alias="TrackerName")


class BatchItemErrorModel(BaseModel):
    code: Optional[
        Literal[
            "AccessDeniedError",
            "ConflictError",
            "InternalServerError",
            "ResourceNotFoundError",
            "ThrottlingError",
            "ValidationError",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class BatchDeleteDevicePositionHistoryRequestModel(BaseModel):
    device_ids: Sequence[str] = Field(alias="DeviceIds")
    tracker_name: str = Field(alias="TrackerName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDeleteGeofenceRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    geofence_ids: Sequence[str] = Field(alias="GeofenceIds")


class BatchGetDevicePositionRequestModel(BaseModel):
    device_ids: Sequence[str] = Field(alias="DeviceIds")
    tracker_name: str = Field(alias="TrackerName")


class BatchPutGeofenceSuccessModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    geofence_id: str = Field(alias="GeofenceId")
    update_time: datetime = Field(alias="UpdateTime")


class CalculateRouteCarModeOptionsModel(BaseModel):
    avoid_ferries: Optional[bool] = Field(default=None, alias="AvoidFerries")
    avoid_tolls: Optional[bool] = Field(default=None, alias="AvoidTolls")


class CalculateRouteMatrixSummaryModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    distance_unit: Literal["Kilometers", "Miles"] = Field(alias="DistanceUnit")
    error_count: int = Field(alias="ErrorCount")
    route_count: int = Field(alias="RouteCount")


class CalculateRouteSummaryModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    distance: float = Field(alias="Distance")
    distance_unit: Literal["Kilometers", "Miles"] = Field(alias="DistanceUnit")
    duration_seconds: float = Field(alias="DurationSeconds")
    route_bbox: List[float] = Field(alias="RouteBBox")


class TruckDimensionsModel(BaseModel):
    height: Optional[float] = Field(default=None, alias="Height")
    length: Optional[float] = Field(default=None, alias="Length")
    unit: Optional[Literal["Feet", "Meters"]] = Field(default=None, alias="Unit")
    width: Optional[float] = Field(default=None, alias="Width")


class TruckWeightModel(BaseModel):
    total: Optional[float] = Field(default=None, alias="Total")
    unit: Optional[Literal["Kilograms", "Pounds"]] = Field(default=None, alias="Unit")


class CircleModel(BaseModel):
    center: Sequence[float] = Field(alias="Center")
    radius: float = Field(alias="Radius")


class CreateGeofenceCollectionRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class MapConfigurationModel(BaseModel):
    style: str = Field(alias="Style")


class DataSourceConfigurationModel(BaseModel):
    intended_use: Optional[Literal["SingleUse", "Storage"]] = Field(
        default=None, alias="IntendedUse"
    )


class CreateRouteCalculatorRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")
    data_source: str = Field(alias="DataSource")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateTrackerRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    position_filtering: Optional[
        Literal["AccuracyBased", "DistanceBased", "TimeBased"]
    ] = Field(default=None, alias="PositionFiltering")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteGeofenceCollectionRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")


class DeleteKeyRequestModel(BaseModel):
    key_name: str = Field(alias="KeyName")


class DeleteMapRequestModel(BaseModel):
    map_name: str = Field(alias="MapName")


class DeletePlaceIndexRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")


class DeleteRouteCalculatorRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")


class DeleteTrackerRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")


class DescribeGeofenceCollectionRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")


class DescribeKeyRequestModel(BaseModel):
    key_name: str = Field(alias="KeyName")


class DescribeMapRequestModel(BaseModel):
    map_name: str = Field(alias="MapName")


class DescribePlaceIndexRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")


class DescribeRouteCalculatorRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")


class DescribeTrackerRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")


class PositionalAccuracyModel(BaseModel):
    horizontal: float = Field(alias="Horizontal")


class DisassociateTrackerConsumerRequestModel(BaseModel):
    consumer_arn: str = Field(alias="ConsumerArn")
    tracker_name: str = Field(alias="TrackerName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetDevicePositionHistoryRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    tracker_name: str = Field(alias="TrackerName")
    end_time_exclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="EndTimeExclusive"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    start_time_inclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartTimeInclusive"
    )


class GetDevicePositionRequestModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    tracker_name: str = Field(alias="TrackerName")


class GetGeofenceRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    geofence_id: str = Field(alias="GeofenceId")


class GetMapGlyphsRequestModel(BaseModel):
    font_stack: str = Field(alias="FontStack")
    font_unicode_range: str = Field(alias="FontUnicodeRange")
    map_name: str = Field(alias="MapName")
    key: Optional[str] = Field(default=None, alias="Key")


class GetMapSpritesRequestModel(BaseModel):
    file_name: str = Field(alias="FileName")
    map_name: str = Field(alias="MapName")
    key: Optional[str] = Field(default=None, alias="Key")


class GetMapStyleDescriptorRequestModel(BaseModel):
    map_name: str = Field(alias="MapName")
    key: Optional[str] = Field(default=None, alias="Key")


class GetMapTileRequestModel(BaseModel):
    map_name: str = Field(alias="MapName")
    x: str = Field(alias="X")
    y: str = Field(alias="Y")
    z: str = Field(alias="Z")
    key: Optional[str] = Field(default=None, alias="Key")


class GetPlaceRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    place_id: str = Field(alias="PlaceId")
    language: Optional[str] = Field(default=None, alias="Language")


class LegGeometryModel(BaseModel):
    line_string: Optional[List[List[float]]] = Field(default=None, alias="LineString")


class StepModel(BaseModel):
    distance: float = Field(alias="Distance")
    duration_seconds: float = Field(alias="DurationSeconds")
    end_position: List[float] = Field(alias="EndPosition")
    start_position: List[float] = Field(alias="StartPosition")
    geometry_offset: Optional[int] = Field(default=None, alias="GeometryOffset")


class ListDevicePositionsRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGeofenceCollectionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGeofenceCollectionsResponseEntryModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    create_time: datetime = Field(alias="CreateTime")
    description: str = Field(alias="Description")
    update_time: datetime = Field(alias="UpdateTime")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )


class ListGeofencesRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMapsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMapsResponseEntryModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    description: str = Field(alias="Description")
    map_name: str = Field(alias="MapName")
    update_time: datetime = Field(alias="UpdateTime")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class ListPlaceIndexesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPlaceIndexesResponseEntryModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    description: str = Field(alias="Description")
    index_name: str = Field(alias="IndexName")
    update_time: datetime = Field(alias="UpdateTime")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class ListRouteCalculatorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRouteCalculatorsResponseEntryModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    description: str = Field(alias="Description")
    update_time: datetime = Field(alias="UpdateTime")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListTrackerConsumersRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTrackersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTrackersResponseEntryModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    description: str = Field(alias="Description")
    tracker_name: str = Field(alias="TrackerName")
    update_time: datetime = Field(alias="UpdateTime")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )


class PlaceGeometryModel(BaseModel):
    point: Optional[List[float]] = Field(default=None, alias="Point")


class TimeZoneModel(BaseModel):
    name: str = Field(alias="Name")
    offset: Optional[int] = Field(default=None, alias="Offset")


class RouteMatrixEntryErrorModel(BaseModel):
    code: Literal[
        "DeparturePositionNotFound",
        "DestinationPositionNotFound",
        "OtherValidationError",
        "PositionsNotFound",
        "RouteNotFound",
        "RouteTooLong",
    ] = Field(alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class SearchForSuggestionsResultModel(BaseModel):
    text: str = Field(alias="Text")
    place_id: Optional[str] = Field(default=None, alias="PlaceId")


class SearchPlaceIndexForPositionRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    position: Sequence[float] = Field(alias="Position")
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchPlaceIndexForPositionSummaryModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    position: List[float] = Field(alias="Position")
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchPlaceIndexForSuggestionsRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    text: str = Field(alias="Text")
    bias_position: Optional[Sequence[float]] = Field(default=None, alias="BiasPosition")
    filter_bbox: Optional[Sequence[float]] = Field(default=None, alias="FilterBBox")
    filter_countries: Optional[Sequence[str]] = Field(
        default=None, alias="FilterCountries"
    )
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchPlaceIndexForSuggestionsSummaryModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    text: str = Field(alias="Text")
    bias_position: Optional[List[float]] = Field(default=None, alias="BiasPosition")
    filter_bbox: Optional[List[float]] = Field(default=None, alias="FilterBBox")
    filter_countries: Optional[List[str]] = Field(default=None, alias="FilterCountries")
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchPlaceIndexForTextRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    text: str = Field(alias="Text")
    bias_position: Optional[Sequence[float]] = Field(default=None, alias="BiasPosition")
    filter_bbox: Optional[Sequence[float]] = Field(default=None, alias="FilterBBox")
    filter_countries: Optional[Sequence[str]] = Field(
        default=None, alias="FilterCountries"
    )
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchPlaceIndexForTextSummaryModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    text: str = Field(alias="Text")
    bias_position: Optional[List[float]] = Field(default=None, alias="BiasPosition")
    filter_bbox: Optional[List[float]] = Field(default=None, alias="FilterBBox")
    filter_countries: Optional[List[str]] = Field(default=None, alias="FilterCountries")
    language: Optional[str] = Field(default=None, alias="Language")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    result_bbox: Optional[List[float]] = Field(default=None, alias="ResultBBox")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateGeofenceCollectionRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )


class UpdateMapRequestModel(BaseModel):
    map_name: str = Field(alias="MapName")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class UpdateRouteCalculatorRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class UpdateTrackerRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    description: Optional[str] = Field(default=None, alias="Description")
    position_filtering: Optional[
        Literal["AccuracyBased", "DistanceBased", "TimeBased"]
    ] = Field(default=None, alias="PositionFiltering")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    pricing_plan_data_source: Optional[str] = Field(
        default=None, alias="PricingPlanDataSource"
    )


class ListKeysRequestModel(BaseModel):
    filter: Optional[ApiKeyFilterModel] = Field(default=None, alias="Filter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateKeyRequestModel(BaseModel):
    key_name: str = Field(alias="KeyName")
    restrictions: ApiKeyRestrictionsModel = Field(alias="Restrictions")
    description: Optional[str] = Field(default=None, alias="Description")
    expire_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExpireTime"
    )
    no_expiry: Optional[bool] = Field(default=None, alias="NoExpiry")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListKeysResponseEntryModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    expire_time: datetime = Field(alias="ExpireTime")
    key_name: str = Field(alias="KeyName")
    restrictions: ApiKeyRestrictionsModel = Field(alias="Restrictions")
    update_time: datetime = Field(alias="UpdateTime")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateKeyRequestModel(BaseModel):
    key_name: str = Field(alias="KeyName")
    description: Optional[str] = Field(default=None, alias="Description")
    expire_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExpireTime"
    )
    force_update: Optional[bool] = Field(default=None, alias="ForceUpdate")
    no_expiry: Optional[bool] = Field(default=None, alias="NoExpiry")
    restrictions: Optional[ApiKeyRestrictionsModel] = Field(
        default=None, alias="Restrictions"
    )


class BatchDeleteDevicePositionHistoryErrorModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    error: BatchItemErrorModel = Field(alias="Error")


class BatchDeleteGeofenceErrorModel(BaseModel):
    error: BatchItemErrorModel = Field(alias="Error")
    geofence_id: str = Field(alias="GeofenceId")


class BatchEvaluateGeofencesErrorModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    error: BatchItemErrorModel = Field(alias="Error")
    sample_time: datetime = Field(alias="SampleTime")


class BatchGetDevicePositionErrorModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    error: BatchItemErrorModel = Field(alias="Error")


class BatchPutGeofenceErrorModel(BaseModel):
    error: BatchItemErrorModel = Field(alias="Error")
    geofence_id: str = Field(alias="GeofenceId")


class BatchUpdateDevicePositionErrorModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    error: BatchItemErrorModel = Field(alias="Error")
    sample_time: datetime = Field(alias="SampleTime")


class CreateGeofenceCollectionResponseModel(BaseModel):
    collection_arn: str = Field(alias="CollectionArn")
    collection_name: str = Field(alias="CollectionName")
    create_time: datetime = Field(alias="CreateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateKeyResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    key: str = Field(alias="Key")
    key_arn: str = Field(alias="KeyArn")
    key_name: str = Field(alias="KeyName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMapResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    map_arn: str = Field(alias="MapArn")
    map_name: str = Field(alias="MapName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePlaceIndexResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    index_arn: str = Field(alias="IndexArn")
    index_name: str = Field(alias="IndexName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRouteCalculatorResponseModel(BaseModel):
    calculator_arn: str = Field(alias="CalculatorArn")
    calculator_name: str = Field(alias="CalculatorName")
    create_time: datetime = Field(alias="CreateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrackerResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    tracker_arn: str = Field(alias="TrackerArn")
    tracker_name: str = Field(alias="TrackerName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGeofenceCollectionResponseModel(BaseModel):
    collection_arn: str = Field(alias="CollectionArn")
    collection_name: str = Field(alias="CollectionName")
    create_time: datetime = Field(alias="CreateTime")
    description: str = Field(alias="Description")
    kms_key_id: str = Field(alias="KmsKeyId")
    pricing_plan: Literal[
        "MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"
    ] = Field(alias="PricingPlan")
    pricing_plan_data_source: str = Field(alias="PricingPlanDataSource")
    tags: Dict[str, str] = Field(alias="Tags")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeKeyResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    description: str = Field(alias="Description")
    expire_time: datetime = Field(alias="ExpireTime")
    key: str = Field(alias="Key")
    key_arn: str = Field(alias="KeyArn")
    key_name: str = Field(alias="KeyName")
    restrictions: ApiKeyRestrictionsModel = Field(alias="Restrictions")
    tags: Dict[str, str] = Field(alias="Tags")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRouteCalculatorResponseModel(BaseModel):
    calculator_arn: str = Field(alias="CalculatorArn")
    calculator_name: str = Field(alias="CalculatorName")
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    description: str = Field(alias="Description")
    pricing_plan: Literal[
        "MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"
    ] = Field(alias="PricingPlan")
    tags: Dict[str, str] = Field(alias="Tags")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrackerResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    description: str = Field(alias="Description")
    kms_key_id: str = Field(alias="KmsKeyId")
    position_filtering: Literal["AccuracyBased", "DistanceBased", "TimeBased"] = Field(
        alias="PositionFiltering"
    )
    pricing_plan: Literal[
        "MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"
    ] = Field(alias="PricingPlan")
    pricing_plan_data_source: str = Field(alias="PricingPlanDataSource")
    tags: Dict[str, str] = Field(alias="Tags")
    tracker_arn: str = Field(alias="TrackerArn")
    tracker_name: str = Field(alias="TrackerName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMapGlyphsResponseModel(BaseModel):
    blob: Type[StreamingBody] = Field(alias="Blob")
    cache_control: str = Field(alias="CacheControl")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMapSpritesResponseModel(BaseModel):
    blob: Type[StreamingBody] = Field(alias="Blob")
    cache_control: str = Field(alias="CacheControl")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMapStyleDescriptorResponseModel(BaseModel):
    blob: Type[StreamingBody] = Field(alias="Blob")
    cache_control: str = Field(alias="CacheControl")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMapTileResponseModel(BaseModel):
    blob: Type[StreamingBody] = Field(alias="Blob")
    cache_control: str = Field(alias="CacheControl")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrackerConsumersResponseModel(BaseModel):
    consumer_arns: List[str] = Field(alias="ConsumerArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutGeofenceResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    geofence_id: str = Field(alias="GeofenceId")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGeofenceCollectionResponseModel(BaseModel):
    collection_arn: str = Field(alias="CollectionArn")
    collection_name: str = Field(alias="CollectionName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateKeyResponseModel(BaseModel):
    key_arn: str = Field(alias="KeyArn")
    key_name: str = Field(alias="KeyName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMapResponseModel(BaseModel):
    map_arn: str = Field(alias="MapArn")
    map_name: str = Field(alias="MapName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePlaceIndexResponseModel(BaseModel):
    index_arn: str = Field(alias="IndexArn")
    index_name: str = Field(alias="IndexName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRouteCalculatorResponseModel(BaseModel):
    calculator_arn: str = Field(alias="CalculatorArn")
    calculator_name: str = Field(alias="CalculatorName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrackerResponseModel(BaseModel):
    tracker_arn: str = Field(alias="TrackerArn")
    tracker_name: str = Field(alias="TrackerName")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CalculateRouteTruckModeOptionsModel(BaseModel):
    avoid_ferries: Optional[bool] = Field(default=None, alias="AvoidFerries")
    avoid_tolls: Optional[bool] = Field(default=None, alias="AvoidTolls")
    dimensions: Optional[TruckDimensionsModel] = Field(default=None, alias="Dimensions")
    weight: Optional[TruckWeightModel] = Field(default=None, alias="Weight")


class GeofenceGeometryModel(BaseModel):
    circle: Optional[CircleModel] = Field(default=None, alias="Circle")
    polygon: Optional[Sequence[Sequence[Sequence[float]]]] = Field(
        default=None, alias="Polygon"
    )


class CreateMapRequestModel(BaseModel):
    configuration: MapConfigurationModel = Field(alias="Configuration")
    map_name: str = Field(alias="MapName")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DescribeMapResponseModel(BaseModel):
    configuration: MapConfigurationModel = Field(alias="Configuration")
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    description: str = Field(alias="Description")
    map_arn: str = Field(alias="MapArn")
    map_name: str = Field(alias="MapName")
    pricing_plan: Literal[
        "MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"
    ] = Field(alias="PricingPlan")
    tags: Dict[str, str] = Field(alias="Tags")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePlaceIndexRequestModel(BaseModel):
    data_source: str = Field(alias="DataSource")
    index_name: str = Field(alias="IndexName")
    data_source_configuration: Optional[DataSourceConfigurationModel] = Field(
        default=None, alias="DataSourceConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DescribePlaceIndexResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    data_source: str = Field(alias="DataSource")
    data_source_configuration: DataSourceConfigurationModel = Field(
        alias="DataSourceConfiguration"
    )
    description: str = Field(alias="Description")
    index_arn: str = Field(alias="IndexArn")
    index_name: str = Field(alias="IndexName")
    pricing_plan: Literal[
        "MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"
    ] = Field(alias="PricingPlan")
    tags: Dict[str, str] = Field(alias="Tags")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePlaceIndexRequestModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    data_source_configuration: Optional[DataSourceConfigurationModel] = Field(
        default=None, alias="DataSourceConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[
        Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
    ] = Field(default=None, alias="PricingPlan")


class DevicePositionModel(BaseModel):
    position: List[float] = Field(alias="Position")
    received_time: datetime = Field(alias="ReceivedTime")
    sample_time: datetime = Field(alias="SampleTime")
    accuracy: Optional[PositionalAccuracyModel] = Field(default=None, alias="Accuracy")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    position_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="PositionProperties"
    )


class DevicePositionUpdateModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    position: Sequence[float] = Field(alias="Position")
    sample_time: Union[datetime, str] = Field(alias="SampleTime")
    accuracy: Optional[PositionalAccuracyModel] = Field(default=None, alias="Accuracy")
    position_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="PositionProperties"
    )


class GetDevicePositionResponseModel(BaseModel):
    accuracy: PositionalAccuracyModel = Field(alias="Accuracy")
    device_id: str = Field(alias="DeviceId")
    position: List[float] = Field(alias="Position")
    position_properties: Dict[str, str] = Field(alias="PositionProperties")
    received_time: datetime = Field(alias="ReceivedTime")
    sample_time: datetime = Field(alias="SampleTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicePositionsResponseEntryModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    position: List[float] = Field(alias="Position")
    sample_time: datetime = Field(alias="SampleTime")
    accuracy: Optional[PositionalAccuracyModel] = Field(default=None, alias="Accuracy")
    position_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="PositionProperties"
    )


class GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    tracker_name: str = Field(alias="TrackerName")
    end_time_exclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="EndTimeExclusive"
    )
    start_time_inclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartTimeInclusive"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicePositionsRequestListDevicePositionsPaginateModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGeofencesRequestListGeofencesPaginateModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKeysRequestListKeysPaginateModel(BaseModel):
    filter: Optional[ApiKeyFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMapsRequestListMapsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlaceIndexesRequestListPlaceIndexesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRouteCalculatorsRequestListRouteCalculatorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrackerConsumersRequestListTrackerConsumersPaginateModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrackersRequestListTrackersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LegModel(BaseModel):
    distance: float = Field(alias="Distance")
    duration_seconds: float = Field(alias="DurationSeconds")
    end_position: List[float] = Field(alias="EndPosition")
    start_position: List[float] = Field(alias="StartPosition")
    steps: List[StepModel] = Field(alias="Steps")
    geometry: Optional[LegGeometryModel] = Field(default=None, alias="Geometry")


class ListGeofenceCollectionsResponseModel(BaseModel):
    entries: List[ListGeofenceCollectionsResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMapsResponseModel(BaseModel):
    entries: List[ListMapsResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlaceIndexesResponseModel(BaseModel):
    entries: List[ListPlaceIndexesResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRouteCalculatorsResponseModel(BaseModel):
    entries: List[ListRouteCalculatorsResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrackersResponseModel(BaseModel):
    entries: List[ListTrackersResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PlaceModel(BaseModel):
    geometry: PlaceGeometryModel = Field(alias="Geometry")
    address_number: Optional[str] = Field(default=None, alias="AddressNumber")
    country: Optional[str] = Field(default=None, alias="Country")
    interpolated: Optional[bool] = Field(default=None, alias="Interpolated")
    label: Optional[str] = Field(default=None, alias="Label")
    municipality: Optional[str] = Field(default=None, alias="Municipality")
    neighborhood: Optional[str] = Field(default=None, alias="Neighborhood")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")
    region: Optional[str] = Field(default=None, alias="Region")
    street: Optional[str] = Field(default=None, alias="Street")
    sub_region: Optional[str] = Field(default=None, alias="SubRegion")
    time_zone: Optional[TimeZoneModel] = Field(default=None, alias="TimeZone")
    unit_number: Optional[str] = Field(default=None, alias="UnitNumber")
    unit_type: Optional[str] = Field(default=None, alias="UnitType")


class RouteMatrixEntryModel(BaseModel):
    distance: Optional[float] = Field(default=None, alias="Distance")
    duration_seconds: Optional[float] = Field(default=None, alias="DurationSeconds")
    error: Optional[RouteMatrixEntryErrorModel] = Field(default=None, alias="Error")


class SearchPlaceIndexForSuggestionsResponseModel(BaseModel):
    results: List[SearchForSuggestionsResultModel] = Field(alias="Results")
    summary: SearchPlaceIndexForSuggestionsSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKeysResponseModel(BaseModel):
    entries: List[ListKeysResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteDevicePositionHistoryResponseModel(BaseModel):
    errors: List[BatchDeleteDevicePositionHistoryErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteGeofenceResponseModel(BaseModel):
    errors: List[BatchDeleteGeofenceErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchEvaluateGeofencesResponseModel(BaseModel):
    errors: List[BatchEvaluateGeofencesErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutGeofenceResponseModel(BaseModel):
    errors: List[BatchPutGeofenceErrorModel] = Field(alias="Errors")
    successes: List[BatchPutGeofenceSuccessModel] = Field(alias="Successes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateDevicePositionResponseModel(BaseModel):
    errors: List[BatchUpdateDevicePositionErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CalculateRouteMatrixRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")
    departure_positions: Sequence[Sequence[float]] = Field(alias="DeparturePositions")
    destination_positions: Sequence[Sequence[float]] = Field(
        alias="DestinationPositions"
    )
    car_mode_options: Optional[CalculateRouteCarModeOptionsModel] = Field(
        default=None, alias="CarModeOptions"
    )
    depart_now: Optional[bool] = Field(default=None, alias="DepartNow")
    departure_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DepartureTime"
    )
    distance_unit: Optional[Literal["Kilometers", "Miles"]] = Field(
        default=None, alias="DistanceUnit"
    )
    travel_mode: Optional[
        Literal["Bicycle", "Car", "Motorcycle", "Truck", "Walking"]
    ] = Field(default=None, alias="TravelMode")
    truck_mode_options: Optional[CalculateRouteTruckModeOptionsModel] = Field(
        default=None, alias="TruckModeOptions"
    )


class CalculateRouteRequestModel(BaseModel):
    calculator_name: str = Field(alias="CalculatorName")
    departure_position: Sequence[float] = Field(alias="DeparturePosition")
    destination_position: Sequence[float] = Field(alias="DestinationPosition")
    car_mode_options: Optional[CalculateRouteCarModeOptionsModel] = Field(
        default=None, alias="CarModeOptions"
    )
    depart_now: Optional[bool] = Field(default=None, alias="DepartNow")
    departure_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DepartureTime"
    )
    distance_unit: Optional[Literal["Kilometers", "Miles"]] = Field(
        default=None, alias="DistanceUnit"
    )
    include_leg_geometry: Optional[bool] = Field(
        default=None, alias="IncludeLegGeometry"
    )
    travel_mode: Optional[
        Literal["Bicycle", "Car", "Motorcycle", "Truck", "Walking"]
    ] = Field(default=None, alias="TravelMode")
    truck_mode_options: Optional[CalculateRouteTruckModeOptionsModel] = Field(
        default=None, alias="TruckModeOptions"
    )
    waypoint_positions: Optional[Sequence[Sequence[float]]] = Field(
        default=None, alias="WaypointPositions"
    )


class BatchPutGeofenceRequestEntryModel(BaseModel):
    geofence_id: str = Field(alias="GeofenceId")
    geometry: GeofenceGeometryModel = Field(alias="Geometry")


class GetGeofenceResponseModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    geofence_id: str = Field(alias="GeofenceId")
    geometry: GeofenceGeometryModel = Field(alias="Geometry")
    status: str = Field(alias="Status")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGeofenceResponseEntryModel(BaseModel):
    create_time: datetime = Field(alias="CreateTime")
    geofence_id: str = Field(alias="GeofenceId")
    geometry: GeofenceGeometryModel = Field(alias="Geometry")
    status: str = Field(alias="Status")
    update_time: datetime = Field(alias="UpdateTime")


class PutGeofenceRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    geofence_id: str = Field(alias="GeofenceId")
    geometry: GeofenceGeometryModel = Field(alias="Geometry")


class BatchGetDevicePositionResponseModel(BaseModel):
    device_positions: List[DevicePositionModel] = Field(alias="DevicePositions")
    errors: List[BatchGetDevicePositionErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevicePositionHistoryResponseModel(BaseModel):
    device_positions: List[DevicePositionModel] = Field(alias="DevicePositions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchEvaluateGeofencesRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    device_position_updates: Sequence[DevicePositionUpdateModel] = Field(
        alias="DevicePositionUpdates"
    )


class BatchUpdateDevicePositionRequestModel(BaseModel):
    tracker_name: str = Field(alias="TrackerName")
    updates: Sequence[DevicePositionUpdateModel] = Field(alias="Updates")


class ListDevicePositionsResponseModel(BaseModel):
    entries: List[ListDevicePositionsResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CalculateRouteResponseModel(BaseModel):
    legs: List[LegModel] = Field(alias="Legs")
    summary: CalculateRouteSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPlaceResponseModel(BaseModel):
    place: PlaceModel = Field(alias="Place")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchForPositionResultModel(BaseModel):
    distance: float = Field(alias="Distance")
    place: PlaceModel = Field(alias="Place")
    place_id: Optional[str] = Field(default=None, alias="PlaceId")


class SearchForTextResultModel(BaseModel):
    place: PlaceModel = Field(alias="Place")
    distance: Optional[float] = Field(default=None, alias="Distance")
    place_id: Optional[str] = Field(default=None, alias="PlaceId")
    relevance: Optional[float] = Field(default=None, alias="Relevance")


class CalculateRouteMatrixResponseModel(BaseModel):
    route_matrix: List[List[RouteMatrixEntryModel]] = Field(alias="RouteMatrix")
    snapped_departure_positions: List[List[float]] = Field(
        alias="SnappedDeparturePositions"
    )
    snapped_destination_positions: List[List[float]] = Field(
        alias="SnappedDestinationPositions"
    )
    summary: CalculateRouteMatrixSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutGeofenceRequestModel(BaseModel):
    collection_name: str = Field(alias="CollectionName")
    entries: Sequence[BatchPutGeofenceRequestEntryModel] = Field(alias="Entries")


class ListGeofencesResponseModel(BaseModel):
    entries: List[ListGeofenceResponseEntryModel] = Field(alias="Entries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchPlaceIndexForPositionResponseModel(BaseModel):
    results: List[SearchForPositionResultModel] = Field(alias="Results")
    summary: SearchPlaceIndexForPositionSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchPlaceIndexForTextResponseModel(BaseModel):
    results: List[SearchForTextResultModel] = Field(alias="Results")
    summary: SearchPlaceIndexForTextSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
