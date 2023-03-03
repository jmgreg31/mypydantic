# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DataPointModel(BaseModel):
    timestamp: datetime = Field(alias="Timestamp")
    value: float = Field(alias="Value")


class DimensionGroupModel(BaseModel):
    group: str = Field(alias="Group")
    dimensions: Optional[Sequence[str]] = Field(default=None, alias="Dimensions")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DimensionKeyDescriptionModel(BaseModel):
    dimensions: Optional[Dict[str, str]] = Field(default=None, alias="Dimensions")
    total: Optional[float] = Field(default=None, alias="Total")
    additional_metrics: Optional[Dict[str, float]] = Field(
        default=None, alias="AdditionalMetrics"
    )
    partitions: Optional[List[float]] = Field(default=None, alias="Partitions")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ResponsePartitionKeyModel(BaseModel):
    dimensions: Dict[str, str] = Field(alias="Dimensions")


class DimensionDetailModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")


class DimensionKeyDetailModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    dimension: Optional[str] = Field(default=None, alias="Dimension")
    status: Optional[Literal["AVAILABLE", "PROCESSING", "UNAVAILABLE"]] = Field(
        default=None, alias="Status"
    )


class FeatureMetadataModel(BaseModel):
    status: Optional[
        Literal[
            "DISABLED",
            "DISABLED_PENDING_REBOOT",
            "ENABLED",
            "ENABLED_PENDING_REBOOT",
            "UNKNOWN",
            "UNSUPPORTED",
        ]
    ] = Field(default=None, alias="Status")


class GetDimensionKeyDetailsRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")
    group: str = Field(alias="Group")
    group_identifier: str = Field(alias="GroupIdentifier")
    requested_dimensions: Optional[Sequence[str]] = Field(
        default=None, alias="RequestedDimensions"
    )


class GetResourceMetadataRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")


class ListAvailableResourceDimensionsRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")
    metrics: Sequence[str] = Field(alias="Metrics")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAvailableResourceMetricsRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")
    metric_types: Sequence[str] = Field(alias="MetricTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResponseResourceMetricModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")
    description: Optional[str] = Field(default=None, alias="Description")
    unit: Optional[str] = Field(default=None, alias="Unit")


class ResponseResourceMetricKeyModel(BaseModel):
    metric: str = Field(alias="Metric")
    dimensions: Optional[Dict[str, str]] = Field(default=None, alias="Dimensions")


class DescribeDimensionKeysRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    metric: str = Field(alias="Metric")
    group_by: DimensionGroupModel = Field(alias="GroupBy")
    period_in_seconds: Optional[int] = Field(default=None, alias="PeriodInSeconds")
    additional_metrics: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalMetrics"
    )
    partition_by: Optional[DimensionGroupModel] = Field(
        default=None, alias="PartitionBy"
    )
    filter: Optional[Mapping[str, str]] = Field(default=None, alias="Filter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MetricQueryModel(BaseModel):
    metric: str = Field(alias="Metric")
    group_by: Optional[DimensionGroupModel] = Field(default=None, alias="GroupBy")
    filter: Optional[Mapping[str, str]] = Field(default=None, alias="Filter")


class DescribeDimensionKeysResponseModel(BaseModel):
    aligned_start_time: datetime = Field(alias="AlignedStartTime")
    aligned_end_time: datetime = Field(alias="AlignedEndTime")
    partition_keys: List[ResponsePartitionKeyModel] = Field(alias="PartitionKeys")
    keys: List[DimensionKeyDescriptionModel] = Field(alias="Keys")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DimensionGroupDetailModel(BaseModel):
    group: Optional[str] = Field(default=None, alias="Group")
    dimensions: Optional[List[DimensionDetailModel]] = Field(
        default=None, alias="Dimensions"
    )


class GetDimensionKeyDetailsResponseModel(BaseModel):
    dimensions: List[DimensionKeyDetailModel] = Field(alias="Dimensions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceMetadataResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    features: Dict[str, FeatureMetadataModel] = Field(alias="Features")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableResourceMetricsResponseModel(BaseModel):
    metrics: List[ResponseResourceMetricModel] = Field(alias="Metrics")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricKeyDataPointsModel(BaseModel):
    key: Optional[ResponseResourceMetricKeyModel] = Field(default=None, alias="Key")
    data_points: Optional[List[DataPointModel]] = Field(
        default=None, alias="DataPoints"
    )


class GetResourceMetricsRequestModel(BaseModel):
    service_type: Literal["DOCDB", "RDS"] = Field(alias="ServiceType")
    identifier: str = Field(alias="Identifier")
    metric_queries: Sequence[MetricQueryModel] = Field(alias="MetricQueries")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    period_in_seconds: Optional[int] = Field(default=None, alias="PeriodInSeconds")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MetricDimensionGroupsModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")
    groups: Optional[List[DimensionGroupDetailModel]] = Field(
        default=None, alias="Groups"
    )


class GetResourceMetricsResponseModel(BaseModel):
    aligned_start_time: datetime = Field(alias="AlignedStartTime")
    aligned_end_time: datetime = Field(alias="AlignedEndTime")
    identifier: str = Field(alias="Identifier")
    metric_list: List[MetricKeyDataPointsModel] = Field(alias="MetricList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableResourceDimensionsResponseModel(BaseModel):
    metric_dimensions: List[MetricDimensionGroupsModel] = Field(
        alias="MetricDimensions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
