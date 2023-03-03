# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AvailabilityMeasurementModel(BaseModel):
    experience_score: Optional[float] = Field(default=None, alias="ExperienceScore")
    percent_of_total_traffic_impacted: Optional[float] = Field(
        default=None, alias="PercentOfTotalTrafficImpacted"
    )
    percent_of_client_location_impacted: Optional[float] = Field(
        default=None, alias="PercentOfClientLocationImpacted"
    )


class CreateMonitorInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    max_city_networks_to_monitor: int = Field(alias="MaxCityNetworksToMonitor")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteMonitorInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")


class GetHealthEventInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    event_id: str = Field(alias="EventId")


class GetMonitorInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListHealthEventsInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    event_status: Optional[Literal["ACTIVE", "RESOLVED"]] = Field(
        default=None, alias="EventStatus"
    )


class ListMonitorsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    monitor_status: Optional[str] = Field(default=None, alias="MonitorStatus")


class MonitorModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    monitor_arn: str = Field(alias="MonitorArn")
    status: Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"] = Field(alias="Status")
    processing_status: Optional[
        Literal[
            "COLLECTING_DATA",
            "FAULT_ACCESS_CLOUDWATCH",
            "FAULT_SERVICE",
            "INACTIVE",
            "INSUFFICIENT_DATA",
            "OK",
        ]
    ] = Field(default=None, alias="ProcessingStatus")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NetworkModel(BaseModel):
    as_name: str = Field(alias="ASName")
    as_number: int = Field(alias="ASNumber")


class RoundTripTimeModel(BaseModel):
    p50: Optional[float] = Field(default=None, alias="P50")
    p90: Optional[float] = Field(default=None, alias="P90")
    p95: Optional[float] = Field(default=None, alias="P95")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateMonitorInputRequestModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    resources_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="ResourcesToAdd"
    )
    resources_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="ResourcesToRemove"
    )
    status: Optional[Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    max_city_networks_to_monitor: Optional[int] = Field(
        default=None, alias="MaxCityNetworksToMonitor"
    )


class CreateMonitorOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    status: Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMonitorOutputModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    monitor_arn: str = Field(alias="MonitorArn")
    resources: List[str] = Field(alias="Resources")
    status: Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"] = Field(alias="Status")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    processing_status: Literal[
        "COLLECTING_DATA",
        "FAULT_ACCESS_CLOUDWATCH",
        "FAULT_SERVICE",
        "INACTIVE",
        "INSUFFICIENT_DATA",
        "OK",
    ] = Field(alias="ProcessingStatus")
    processing_status_info: str = Field(alias="ProcessingStatusInfo")
    tags: Dict[str, str] = Field(alias="Tags")
    max_city_networks_to_monitor: int = Field(alias="MaxCityNetworksToMonitor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMonitorOutputModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    status: Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHealthEventsInputListHealthEventsPaginateModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    event_status: Optional[Literal["ACTIVE", "RESOLVED"]] = Field(
        default=None, alias="EventStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitorsInputListMonitorsPaginateModel(BaseModel):
    monitor_status: Optional[str] = Field(default=None, alias="MonitorStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMonitorsOutputModel(BaseModel):
    monitors: List[MonitorModel] = Field(alias="Monitors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkImpairmentModel(BaseModel):
    networks: List[NetworkModel] = Field(alias="Networks")
    as_path: List[NetworkModel] = Field(alias="AsPath")
    network_event_type: Literal["AWS", "Internet"] = Field(alias="NetworkEventType")


class PerformanceMeasurementModel(BaseModel):
    experience_score: Optional[float] = Field(default=None, alias="ExperienceScore")
    percent_of_total_traffic_impacted: Optional[float] = Field(
        default=None, alias="PercentOfTotalTrafficImpacted"
    )
    percent_of_client_location_impacted: Optional[float] = Field(
        default=None, alias="PercentOfClientLocationImpacted"
    )
    round_trip_time: Optional[RoundTripTimeModel] = Field(
        default=None, alias="RoundTripTime"
    )


class InternetHealthModel(BaseModel):
    availability: Optional[AvailabilityMeasurementModel] = Field(
        default=None, alias="Availability"
    )
    performance: Optional[PerformanceMeasurementModel] = Field(
        default=None, alias="Performance"
    )


class ImpactedLocationModel(BaseModel):
    as_name: str = Field(alias="ASName")
    as_number: int = Field(alias="ASNumber")
    country: str = Field(alias="Country")
    status: Literal["ACTIVE", "RESOLVED"] = Field(alias="Status")
    subdivision: Optional[str] = Field(default=None, alias="Subdivision")
    metro: Optional[str] = Field(default=None, alias="Metro")
    city: Optional[str] = Field(default=None, alias="City")
    latitude: Optional[float] = Field(default=None, alias="Latitude")
    longitude: Optional[float] = Field(default=None, alias="Longitude")
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    subdivision_code: Optional[str] = Field(default=None, alias="SubdivisionCode")
    service_location: Optional[str] = Field(default=None, alias="ServiceLocation")
    caused_by: Optional[NetworkImpairmentModel] = Field(default=None, alias="CausedBy")
    internet_health: Optional[InternetHealthModel] = Field(
        default=None, alias="InternetHealth"
    )


class GetHealthEventOutputModel(BaseModel):
    event_arn: str = Field(alias="EventArn")
    event_id: str = Field(alias="EventId")
    started_at: datetime = Field(alias="StartedAt")
    ended_at: datetime = Field(alias="EndedAt")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    impacted_locations: List[ImpactedLocationModel] = Field(alias="ImpactedLocations")
    status: Literal["ACTIVE", "RESOLVED"] = Field(alias="Status")
    percent_of_total_traffic_impacted: float = Field(
        alias="PercentOfTotalTrafficImpacted"
    )
    impact_type: Literal["AVAILABILITY", "PERFORMANCE"] = Field(alias="ImpactType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HealthEventModel(BaseModel):
    event_arn: str = Field(alias="EventArn")
    event_id: str = Field(alias="EventId")
    started_at: datetime = Field(alias="StartedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    impacted_locations: List[ImpactedLocationModel] = Field(alias="ImpactedLocations")
    status: Literal["ACTIVE", "RESOLVED"] = Field(alias="Status")
    impact_type: Literal["AVAILABILITY", "PERFORMANCE"] = Field(alias="ImpactType")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    percent_of_total_traffic_impacted: Optional[float] = Field(
        default=None, alias="PercentOfTotalTrafficImpacted"
    )


class ListHealthEventsOutputModel(BaseModel):
    health_events: List[HealthEventModel] = Field(alias="HealthEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
