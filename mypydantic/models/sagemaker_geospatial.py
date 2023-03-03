# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class MultiPolygonGeometryInputModel(BaseModel):
    coordinates: List[List[List[List[float]]]] = Field(alias="Coordinates")


class PolygonGeometryInputModel(BaseModel):
    coordinates: List[List[List[float]]] = Field(alias="Coordinates")


class AssetValueModel(BaseModel):
    href: Optional[str] = Field(default=None, alias="Href")


class CloudRemovalConfigInputModel(BaseModel):
    algorithm_name: Optional[Literal["INTERPOLATION"]] = Field(
        default=None, alias="AlgorithmName"
    )
    interpolation_value: Optional[str] = Field(default=None, alias="InterpolationValue")
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class OperationModel(BaseModel):
    equation: str = Field(alias="Equation")
    name: str = Field(alias="Name")
    output_type: Optional[
        Literal["FLOAT32", "FLOAT64", "INT16", "INT32", "UINT16"]
    ] = Field(default=None, alias="OutputType")


class DeleteEarthObservationJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DeleteVectorEnrichmentJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class EarthObservationJobErrorDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    type: Optional[Literal["CLIENT_ERROR", "SERVER_ERROR"]] = Field(
        default=None, alias="Type"
    )


class EoCloudCoverInputModel(BaseModel):
    lower_bound: float = Field(alias="LowerBound")
    upper_bound: float = Field(alias="UpperBound")


class S3DataInputModel(BaseModel):
    metadata_provider: Literal["PLANET_ORDER"] = Field(alias="MetadataProvider")
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ExportErrorDetailsOutputModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    type: Optional[Literal["CLIENT_ERROR", "SERVER_ERROR"]] = Field(
        default=None, alias="Type"
    )


class ExportS3DataInputModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class VectorEnrichmentJobS3DataModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    type: str = Field(alias="Type")
    maximum: Optional[float] = Field(default=None, alias="Maximum")
    minimum: Optional[float] = Field(default=None, alias="Minimum")


class GeoMosaicConfigInputModel(BaseModel):
    algorithm_name: Optional[
        Literal[
            "AVERAGE",
            "BILINEAR",
            "CUBIC",
            "CUBICSPLINE",
            "LANCZOS",
            "MAX",
            "MED",
            "MIN",
            "MODE",
            "NEAR",
            "Q1",
            "Q3",
            "RMS",
            "SUM",
        ]
    ] = Field(default=None, alias="AlgorithmName")
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class GeometryModel(BaseModel):
    coordinates: List[List[List[float]]] = Field(alias="Coordinates")
    type: str = Field(alias="Type")


class GetEarthObservationJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class OutputBandModel(BaseModel):
    band_name: str = Field(alias="BandName")
    output_data_type: Literal["FLOAT32", "FLOAT64", "INT16", "INT32", "UINT16"] = Field(
        alias="OutputDataType"
    )


class GetRasterDataCollectionInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GetTileInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    image_assets: Sequence[str] = Field(alias="ImageAssets")
    target: Literal["INPUT", "OUTPUT"] = Field(alias="Target")
    x: int = Field(alias="x")
    y: int = Field(alias="y")
    z: int = Field(alias="z")
    image_mask: Optional[bool] = Field(default=None, alias="ImageMask")
    output_data_type: Optional[
        Literal["FLOAT32", "FLOAT64", "INT16", "INT32", "UINT16"]
    ] = Field(default=None, alias="OutputDataType")
    output_format: Optional[str] = Field(default=None, alias="OutputFormat")
    property_filters: Optional[str] = Field(default=None, alias="PropertyFilters")
    time_range_filter: Optional[str] = Field(default=None, alias="TimeRangeFilter")


class GetVectorEnrichmentJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class VectorEnrichmentJobErrorDetailsModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_type: Optional[Literal["CLIENT_ERROR", "SERVER_ERROR"]] = Field(
        default=None, alias="ErrorType"
    )


class VectorEnrichmentJobExportErrorDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    type: Optional[Literal["CLIENT_ERROR", "SERVER_ERROR"]] = Field(
        default=None, alias="Type"
    )


class PropertiesModel(BaseModel):
    eo_cloud_cover: Optional[float] = Field(default=None, alias="EoCloudCover")
    landsat_cloud_cover_land: Optional[float] = Field(
        default=None, alias="LandsatCloudCoverLand"
    )
    platform: Optional[str] = Field(default=None, alias="Platform")
    view_off_nadir: Optional[float] = Field(default=None, alias="ViewOffNadir")
    view_sun_azimuth: Optional[float] = Field(default=None, alias="ViewSunAzimuth")
    view_sun_elevation: Optional[float] = Field(default=None, alias="ViewSunElevation")


class TemporalStatisticsConfigInputModel(BaseModel):
    statistics: List[Literal["MEAN", "MEDIAN", "STANDARD_DEVIATION"]] = Field(
        alias="Statistics"
    )
    group_by: Optional[Literal["ALL", "YEARLY"]] = Field(default=None, alias="GroupBy")
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class ZonalStatisticsConfigInputModel(BaseModel):
    statistics: List[
        Literal["MAX", "MEAN", "MEDIAN", "MIN", "STANDARD_DEVIATION", "SUM"]
    ] = Field(alias="Statistics")
    zone_s3_path: str = Field(alias="ZoneS3Path")
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class LandsatCloudCoverLandInputModel(BaseModel):
    lower_bound: float = Field(alias="LowerBound")
    upper_bound: float = Field(alias="UpperBound")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEarthObservationJobInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[
        Literal[
            "COMPLETED",
            "DELETED",
            "DELETING",
            "FAILED",
            "INITIALIZING",
            "IN_PROGRESS",
            "STOPPED",
            "STOPPING",
        ]
    ] = Field(default=None, alias="StatusEquals")


class ListEarthObservationJobOutputConfigModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    name: str = Field(alias="Name")
    operation_type: str = Field(alias="OperationType")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListRasterDataCollectionsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListVectorEnrichmentJobInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[str] = Field(default=None, alias="StatusEquals")


class ListVectorEnrichmentJobOutputConfigModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    type: Literal["MAP_MATCHING", "REVERSE_GEOCODING"] = Field(alias="Type")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class MapMatchingConfigModel(BaseModel):
    id_attribute_name: str = Field(alias="IdAttributeName")
    timestamp_attribute_name: str = Field(alias="TimestampAttributeName")
    xattribute_name: str = Field(alias="XAttributeName")
    yattribute_name: str = Field(alias="YAttributeName")


class UserDefinedModel(BaseModel):
    unit: Literal["METERS"] = Field(alias="Unit")
    value: float = Field(alias="Value")


class PlatformInputModel(BaseModel):
    value: str = Field(alias="Value")
    comparison_operator: Optional[
        Literal["EQUALS", "NOT_EQUALS", "STARTS_WITH"]
    ] = Field(default=None, alias="ComparisonOperator")


class ViewOffNadirInputModel(BaseModel):
    lower_bound: float = Field(alias="LowerBound")
    upper_bound: float = Field(alias="UpperBound")


class ViewSunAzimuthInputModel(BaseModel):
    lower_bound: float = Field(alias="LowerBound")
    upper_bound: float = Field(alias="UpperBound")


class ViewSunElevationInputModel(BaseModel):
    lower_bound: float = Field(alias="LowerBound")
    upper_bound: float = Field(alias="UpperBound")


class TimeRangeFilterInputModel(BaseModel):
    end_time: datetime = Field(alias="EndTime")
    start_time: datetime = Field(alias="StartTime")


class ReverseGeocodingConfigModel(BaseModel):
    xattribute_name: str = Field(alias="XAttributeName")
    yattribute_name: str = Field(alias="YAttributeName")


class StopEarthObservationJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class StopVectorEnrichmentJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AreaOfInterestGeometryModel(BaseModel):
    multi_polygon_geometry: Optional[MultiPolygonGeometryInputModel] = Field(
        default=None, alias="MultiPolygonGeometry"
    )
    polygon_geometry: Optional[PolygonGeometryInputModel] = Field(
        default=None, alias="PolygonGeometry"
    )


class CustomIndicesInputModel(BaseModel):
    operations: Optional[List[OperationModel]] = Field(default=None, alias="Operations")


class EojDataSourceConfigInputModel(BaseModel):
    s3_data: Optional[S3DataInputModel] = Field(default=None, alias="S3Data")


class GetTileOutputModel(BaseModel):
    binary_file: Type[StreamingBody] = Field(alias="BinaryFile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportErrorDetailsModel(BaseModel):
    export_results: Optional[ExportErrorDetailsOutputModel] = Field(
        default=None, alias="ExportResults"
    )
    export_source_images: Optional[ExportErrorDetailsOutputModel] = Field(
        default=None, alias="ExportSourceImages"
    )


class OutputConfigInputModel(BaseModel):
    s3_data: ExportS3DataInputModel = Field(alias="S3Data")


class ExportVectorEnrichmentJobOutputConfigModel(BaseModel):
    s3_data: VectorEnrichmentJobS3DataModel = Field(alias="S3Data")


class VectorEnrichmentJobDataSourceConfigInputModel(BaseModel):
    s3_data: Optional[VectorEnrichmentJobS3DataModel] = Field(
        default=None, alias="S3Data"
    )


class GetRasterDataCollectionOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    description_page_url: str = Field(alias="DescriptionPageUrl")
    image_source_bands: List[str] = Field(alias="ImageSourceBands")
    name: str = Field(alias="Name")
    supported_filters: List[FilterModel] = Field(alias="SupportedFilters")
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal["PREMIUM", "PUBLIC", "USER"] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RasterDataCollectionMetadataModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    supported_filters: List[FilterModel] = Field(alias="SupportedFilters")
    type: Literal["PREMIUM", "PUBLIC", "USER"] = Field(alias="Type")
    description_page_url: Optional[str] = Field(
        default=None, alias="DescriptionPageUrl"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ItemSourceModel(BaseModel):
    date_time: datetime = Field(alias="DateTime")
    geometry: GeometryModel = Field(alias="Geometry")
    id: str = Field(alias="Id")
    assets: Optional[Dict[str, AssetValueModel]] = Field(default=None, alias="Assets")
    properties: Optional[PropertiesModel] = Field(default=None, alias="Properties")


class ListEarthObservationJobInputListEarthObservationJobsPaginateModel(BaseModel):
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[
        Literal[
            "COMPLETED",
            "DELETED",
            "DELETING",
            "FAILED",
            "INITIALIZING",
            "IN_PROGRESS",
            "STOPPED",
            "STOPPING",
        ]
    ] = Field(default=None, alias="StatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRasterDataCollectionsInputListRasterDataCollectionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateModel(BaseModel):
    sort_by: Optional[str] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    status_equals: Optional[str] = Field(default=None, alias="StatusEquals")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEarthObservationJobOutputModel(BaseModel):
    earth_observation_job_summaries: List[
        ListEarthObservationJobOutputConfigModel
    ] = Field(alias="EarthObservationJobSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVectorEnrichmentJobOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    vector_enrichment_job_summaries: List[
        ListVectorEnrichmentJobOutputConfigModel
    ] = Field(alias="VectorEnrichmentJobSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OutputResolutionResamplingInputModel(BaseModel):
    user_defined: UserDefinedModel = Field(alias="UserDefined")


class OutputResolutionStackInputModel(BaseModel):
    predefined: Optional[Literal["AVERAGE", "HIGHEST", "LOWEST"]] = Field(
        default=None, alias="Predefined"
    )
    user_defined: Optional[UserDefinedModel] = Field(default=None, alias="UserDefined")


class PropertyModel(BaseModel):
    eo_cloud_cover: Optional[EoCloudCoverInputModel] = Field(
        default=None, alias="EoCloudCover"
    )
    landsat_cloud_cover_land: Optional[LandsatCloudCoverLandInputModel] = Field(
        default=None, alias="LandsatCloudCoverLand"
    )
    platform: Optional[PlatformInputModel] = Field(default=None, alias="Platform")
    view_off_nadir: Optional[ViewOffNadirInputModel] = Field(
        default=None, alias="ViewOffNadir"
    )
    view_sun_azimuth: Optional[ViewSunAzimuthInputModel] = Field(
        default=None, alias="ViewSunAzimuth"
    )
    view_sun_elevation: Optional[ViewSunElevationInputModel] = Field(
        default=None, alias="ViewSunElevation"
    )


class VectorEnrichmentJobConfigModel(BaseModel):
    map_matching_config: Optional[MapMatchingConfigModel] = Field(
        default=None, alias="MapMatchingConfig"
    )
    reverse_geocoding_config: Optional[ReverseGeocodingConfigModel] = Field(
        default=None, alias="ReverseGeocodingConfig"
    )


class AreaOfInterestModel(BaseModel):
    area_of_interest_geometry: Optional[AreaOfInterestGeometryModel] = Field(
        default=None, alias="AreaOfInterestGeometry"
    )


class BandMathConfigInputModel(BaseModel):
    custom_indices: Optional[CustomIndicesInputModel] = Field(
        default=None, alias="CustomIndices"
    )
    predefined_indices: Optional[List[str]] = Field(
        default=None, alias="PredefinedIndices"
    )


class ExportEarthObservationJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    output_config: OutputConfigInputModel = Field(alias="OutputConfig")
    export_source_images: Optional[bool] = Field(
        default=None, alias="ExportSourceImages"
    )


class ExportEarthObservationJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    export_source_images: bool = Field(alias="ExportSourceImages")
    export_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="ExportStatus"
    )
    output_config: OutputConfigInputModel = Field(alias="OutputConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportVectorEnrichmentJobInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    output_config: ExportVectorEnrichmentJobOutputConfigModel = Field(
        alias="OutputConfig"
    )


class ExportVectorEnrichmentJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    export_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="ExportStatus"
    )
    output_config: ExportVectorEnrichmentJobOutputConfigModel = Field(
        alias="OutputConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VectorEnrichmentJobInputConfigModel(BaseModel):
    data_source_config: VectorEnrichmentJobDataSourceConfigInputModel = Field(
        alias="DataSourceConfig"
    )
    document_type: Literal["CSV"] = Field(alias="DocumentType")


class ListRasterDataCollectionsOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    raster_data_collection_summaries: List[RasterDataCollectionMetadataModel] = Field(
        alias="RasterDataCollectionSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchRasterDataCollectionOutputModel(BaseModel):
    approximate_result_count: int = Field(alias="ApproximateResultCount")
    items: List[ItemSourceModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResamplingConfigInputModel(BaseModel):
    output_resolution: OutputResolutionResamplingInputModel = Field(
        alias="OutputResolution"
    )
    algorithm_name: Optional[
        Literal[
            "AVERAGE",
            "BILINEAR",
            "CUBIC",
            "CUBICSPLINE",
            "LANCZOS",
            "MAX",
            "MED",
            "MIN",
            "MODE",
            "NEAR",
            "Q1",
            "Q3",
            "RMS",
            "SUM",
        ]
    ] = Field(default=None, alias="AlgorithmName")
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class StackConfigInputModel(BaseModel):
    output_resolution: Optional[OutputResolutionStackInputModel] = Field(
        default=None, alias="OutputResolution"
    )
    target_bands: Optional[List[str]] = Field(default=None, alias="TargetBands")


class PropertyFilterModel(BaseModel):
    property: PropertyModel = Field(alias="Property")


class GetVectorEnrichmentJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    error_details: VectorEnrichmentJobErrorDetailsModel = Field(alias="ErrorDetails")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    export_error_details: VectorEnrichmentJobExportErrorDetailsModel = Field(
        alias="ExportErrorDetails"
    )
    export_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="ExportStatus"
    )
    input_config: VectorEnrichmentJobInputConfigModel = Field(alias="InputConfig")
    job_config: VectorEnrichmentJobConfigModel = Field(alias="JobConfig")
    kms_key_id: str = Field(alias="KmsKeyId")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal["MAP_MATCHING", "REVERSE_GEOCODING"] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartVectorEnrichmentJobInputRequestModel(BaseModel):
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    input_config: VectorEnrichmentJobInputConfigModel = Field(alias="InputConfig")
    job_config: VectorEnrichmentJobConfigModel = Field(alias="JobConfig")
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class StartVectorEnrichmentJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    input_config: VectorEnrichmentJobInputConfigModel = Field(alias="InputConfig")
    job_config: VectorEnrichmentJobConfigModel = Field(alias="JobConfig")
    kms_key_id: str = Field(alias="KmsKeyId")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    type: Literal["MAP_MATCHING", "REVERSE_GEOCODING"] = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobConfigInputModel(BaseModel):
    band_math_config: Optional[BandMathConfigInputModel] = Field(
        default=None, alias="BandMathConfig"
    )
    cloud_masking_config: Optional[Dict[str, Any]] = Field(
        default=None, alias="CloudMaskingConfig"
    )
    cloud_removal_config: Optional[CloudRemovalConfigInputModel] = Field(
        default=None, alias="CloudRemovalConfig"
    )
    geo_mosaic_config: Optional[GeoMosaicConfigInputModel] = Field(
        default=None, alias="GeoMosaicConfig"
    )
    land_cover_segmentation_config: Optional[Dict[str, Any]] = Field(
        default=None, alias="LandCoverSegmentationConfig"
    )
    resampling_config: Optional[ResamplingConfigInputModel] = Field(
        default=None, alias="ResamplingConfig"
    )
    stack_config: Optional[StackConfigInputModel] = Field(
        default=None, alias="StackConfig"
    )
    temporal_statistics_config: Optional[TemporalStatisticsConfigInputModel] = Field(
        default=None, alias="TemporalStatisticsConfig"
    )
    zonal_statistics_config: Optional[ZonalStatisticsConfigInputModel] = Field(
        default=None, alias="ZonalStatisticsConfig"
    )


class PropertyFiltersModel(BaseModel):
    logical_operator: Optional[Literal["AND"]] = Field(
        default=None, alias="LogicalOperator"
    )
    properties: Optional[List[PropertyFilterModel]] = Field(
        default=None, alias="Properties"
    )


class RasterDataCollectionQueryInputModel(BaseModel):
    raster_data_collection_arn: str = Field(alias="RasterDataCollectionArn")
    time_range_filter: TimeRangeFilterInputModel = Field(alias="TimeRangeFilter")
    area_of_interest: Optional[AreaOfInterestModel] = Field(
        default=None, alias="AreaOfInterest"
    )
    property_filters: Optional[PropertyFiltersModel] = Field(
        default=None, alias="PropertyFilters"
    )


class RasterDataCollectionQueryOutputModel(BaseModel):
    raster_data_collection_arn: str = Field(alias="RasterDataCollectionArn")
    raster_data_collection_name: str = Field(alias="RasterDataCollectionName")
    time_range_filter: TimeRangeFilterInputModel = Field(alias="TimeRangeFilter")
    area_of_interest: Optional[AreaOfInterestModel] = Field(
        default=None, alias="AreaOfInterest"
    )
    property_filters: Optional[PropertyFiltersModel] = Field(
        default=None, alias="PropertyFilters"
    )


class RasterDataCollectionQueryWithBandFilterInputModel(BaseModel):
    time_range_filter: TimeRangeFilterInputModel = Field(alias="TimeRangeFilter")
    area_of_interest: Optional[AreaOfInterestModel] = Field(
        default=None, alias="AreaOfInterest"
    )
    band_filter: Optional[Sequence[str]] = Field(default=None, alias="BandFilter")
    property_filters: Optional[PropertyFiltersModel] = Field(
        default=None, alias="PropertyFilters"
    )


class InputConfigInputModel(BaseModel):
    data_source_config: Optional[EojDataSourceConfigInputModel] = Field(
        default=None, alias="DataSourceConfig"
    )
    previous_earth_observation_job_arn: Optional[str] = Field(
        default=None, alias="PreviousEarthObservationJobArn"
    )
    raster_data_collection_query: Optional[RasterDataCollectionQueryInputModel] = Field(
        default=None, alias="RasterDataCollectionQuery"
    )


class InputConfigOutputModel(BaseModel):
    data_source_config: Optional[EojDataSourceConfigInputModel] = Field(
        default=None, alias="DataSourceConfig"
    )
    previous_earth_observation_job_arn: Optional[str] = Field(
        default=None, alias="PreviousEarthObservationJobArn"
    )
    raster_data_collection_query: Optional[
        RasterDataCollectionQueryOutputModel
    ] = Field(default=None, alias="RasterDataCollectionQuery")


class SearchRasterDataCollectionInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    raster_data_collection_query: RasterDataCollectionQueryWithBandFilterInputModel = (
        Field(alias="RasterDataCollectionQuery")
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StartEarthObservationJobInputRequestModel(BaseModel):
    input_config: InputConfigInputModel = Field(alias="InputConfig")
    job_config: JobConfigInputModel = Field(alias="JobConfig")
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GetEarthObservationJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    error_details: EarthObservationJobErrorDetailsModel = Field(alias="ErrorDetails")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    export_error_details: ExportErrorDetailsModel = Field(alias="ExportErrorDetails")
    export_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="ExportStatus"
    )
    input_config: InputConfigOutputModel = Field(alias="InputConfig")
    job_config: JobConfigInputModel = Field(alias="JobConfig")
    kms_key_id: str = Field(alias="KmsKeyId")
    name: str = Field(alias="Name")
    output_bands: List[OutputBandModel] = Field(alias="OutputBands")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartEarthObservationJobOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_time: datetime = Field(alias="CreationTime")
    duration_in_seconds: int = Field(alias="DurationInSeconds")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    input_config: InputConfigOutputModel = Field(alias="InputConfig")
    job_config: JobConfigInputModel = Field(alias="JobConfig")
    kms_key_id: str = Field(alias="KmsKeyId")
    name: str = Field(alias="Name")
    status: Literal[
        "COMPLETED",
        "DELETED",
        "DELETING",
        "FAILED",
        "INITIALIZING",
        "IN_PROGRESS",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
