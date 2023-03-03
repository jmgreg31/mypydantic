# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AppMonitorConfigurationModel(BaseModel):
    allow_cookies: Optional[bool] = Field(default=None, alias="AllowCookies")
    enable_xray: Optional[bool] = Field(default=None, alias="EnableXRay")
    excluded_pages: Optional[Sequence[str]] = Field(default=None, alias="ExcludedPages")
    favorite_pages: Optional[Sequence[str]] = Field(default=None, alias="FavoritePages")
    guest_role_arn: Optional[str] = Field(default=None, alias="GuestRoleArn")
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    included_pages: Optional[Sequence[str]] = Field(default=None, alias="IncludedPages")
    session_sample_rate: Optional[float] = Field(
        default=None, alias="SessionSampleRate"
    )
    telemetries: Optional[Sequence[Literal["errors", "http", "performance"]]] = Field(
        default=None, alias="Telemetries"
    )


class AppMonitorDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")


class AppMonitorSummaryModel(BaseModel):
    created: Optional[str] = Field(default=None, alias="Created")
    id: Optional[str] = Field(default=None, alias="Id")
    last_modified: Optional[str] = Field(default=None, alias="LastModified")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "CREATED", "DELETING"]] = Field(
        default=None, alias="State"
    )


class CustomEventsModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class MetricDefinitionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    dimension_keys: Optional[Mapping[str, str]] = Field(
        default=None, alias="DimensionKeys"
    )
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    unit_label: Optional[str] = Field(default=None, alias="UnitLabel")
    value_key: Optional[str] = Field(default=None, alias="ValueKey")


class MetricDefinitionModel(BaseModel):
    metric_definition_id: str = Field(alias="MetricDefinitionId")
    name: str = Field(alias="Name")
    dimension_keys: Optional[Dict[str, str]] = Field(
        default=None, alias="DimensionKeys"
    )
    event_pattern: Optional[str] = Field(default=None, alias="EventPattern")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    unit_label: Optional[str] = Field(default=None, alias="UnitLabel")
    value_key: Optional[str] = Field(default=None, alias="ValueKey")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDeleteRumMetricDefinitionsErrorModel(BaseModel):
    error_code: str = Field(alias="ErrorCode")
    error_message: str = Field(alias="ErrorMessage")
    metric_definition_id: str = Field(alias="MetricDefinitionId")


class BatchDeleteRumMetricDefinitionsRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    metric_definition_ids: Sequence[str] = Field(alias="MetricDefinitionIds")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class BatchGetRumMetricDefinitionsRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CwLogModel(BaseModel):
    cw_log_enabled: Optional[bool] = Field(default=None, alias="CwLogEnabled")
    cw_log_group: Optional[str] = Field(default=None, alias="CwLogGroup")


class DeleteAppMonitorRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteRumMetricsDestinationRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class QueryFilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class TimeRangeModel(BaseModel):
    after: int = Field(alias="After")
    before: Optional[int] = Field(default=None, alias="Before")


class GetAppMonitorRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ListAppMonitorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRumMetricsDestinationsRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MetricDestinationSummaryModel(BaseModel):
    destination: Optional[Literal["CloudWatch", "Evidently"]] = Field(
        default=None, alias="Destination"
    )
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RumEventModel(BaseModel):
    details: str = Field(alias="details")
    id: str = Field(alias="id")
    timestamp: Union[datetime, str] = Field(alias="timestamp")
    type: str = Field(alias="type")
    metadata: Optional[str] = Field(default=None, alias="metadata")


class UserDetailsModel(BaseModel):
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    user_id: Optional[str] = Field(default=None, alias="userId")


class PutRumMetricsDestinationRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class CreateAppMonitorRequestModel(BaseModel):
    domain: str = Field(alias="Domain")
    name: str = Field(alias="Name")
    app_monitor_configuration: Optional[AppMonitorConfigurationModel] = Field(
        default=None, alias="AppMonitorConfiguration"
    )
    custom_events: Optional[CustomEventsModel] = Field(
        default=None, alias="CustomEvents"
    )
    cw_log_enabled: Optional[bool] = Field(default=None, alias="CwLogEnabled")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateAppMonitorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    app_monitor_configuration: Optional[AppMonitorConfigurationModel] = Field(
        default=None, alias="AppMonitorConfiguration"
    )
    custom_events: Optional[CustomEventsModel] = Field(
        default=None, alias="CustomEvents"
    )
    cw_log_enabled: Optional[bool] = Field(default=None, alias="CwLogEnabled")
    domain: Optional[str] = Field(default=None, alias="Domain")


class BatchCreateRumMetricDefinitionsErrorModel(BaseModel):
    error_code: str = Field(alias="ErrorCode")
    error_message: str = Field(alias="ErrorMessage")
    metric_definition: MetricDefinitionRequestModel = Field(alias="MetricDefinition")


class BatchCreateRumMetricDefinitionsRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    metric_definitions: Sequence[MetricDefinitionRequestModel] = Field(
        alias="MetricDefinitions"
    )
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class UpdateRumMetricDefinitionRequestModel(BaseModel):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    metric_definition: MetricDefinitionRequestModel = Field(alias="MetricDefinition")
    metric_definition_id: str = Field(alias="MetricDefinitionId")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class BatchGetRumMetricDefinitionsResponseModel(BaseModel):
    metric_definitions: List[MetricDefinitionModel] = Field(alias="MetricDefinitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppMonitorResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppMonitorDataResponseModel(BaseModel):
    events: List[str] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppMonitorsResponseModel(BaseModel):
    app_monitor_summaries: List[AppMonitorSummaryModel] = Field(
        alias="AppMonitorSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteRumMetricDefinitionsResponseModel(BaseModel):
    errors: List[BatchDeleteRumMetricDefinitionsErrorModel] = Field(alias="Errors")
    metric_definition_ids: List[str] = Field(alias="MetricDefinitionIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateModel(
    BaseModel
):
    app_monitor_name: str = Field(alias="AppMonitorName")
    destination: Literal["CloudWatch", "Evidently"] = Field(alias="Destination")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAppMonitorsRequestListAppMonitorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateModel(
    BaseModel
):
    app_monitor_name: str = Field(alias="AppMonitorName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DataStorageModel(BaseModel):
    cw_log: Optional[CwLogModel] = Field(default=None, alias="CwLog")


class GetAppMonitorDataRequestGetAppMonitorDataPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    time_range: TimeRangeModel = Field(alias="TimeRange")
    filters: Optional[Sequence[QueryFilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAppMonitorDataRequestModel(BaseModel):
    name: str = Field(alias="Name")
    time_range: TimeRangeModel = Field(alias="TimeRange")
    filters: Optional[Sequence[QueryFilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRumMetricsDestinationsResponseModel(BaseModel):
    destinations: List[MetricDestinationSummaryModel] = Field(alias="Destinations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRumEventsRequestModel(BaseModel):
    app_monitor_details: AppMonitorDetailsModel = Field(alias="AppMonitorDetails")
    batch_id: str = Field(alias="BatchId")
    id: str = Field(alias="Id")
    rum_events: Sequence[RumEventModel] = Field(alias="RumEvents")
    user_details: UserDetailsModel = Field(alias="UserDetails")


class BatchCreateRumMetricDefinitionsResponseModel(BaseModel):
    errors: List[BatchCreateRumMetricDefinitionsErrorModel] = Field(alias="Errors")
    metric_definitions: List[MetricDefinitionModel] = Field(alias="MetricDefinitions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AppMonitorModel(BaseModel):
    app_monitor_configuration: Optional[AppMonitorConfigurationModel] = Field(
        default=None, alias="AppMonitorConfiguration"
    )
    created: Optional[str] = Field(default=None, alias="Created")
    custom_events: Optional[CustomEventsModel] = Field(
        default=None, alias="CustomEvents"
    )
    data_storage: Optional[DataStorageModel] = Field(default=None, alias="DataStorage")
    domain: Optional[str] = Field(default=None, alias="Domain")
    id: Optional[str] = Field(default=None, alias="Id")
    last_modified: Optional[str] = Field(default=None, alias="LastModified")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "CREATED", "DELETING"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetAppMonitorResponseModel(BaseModel):
    app_monitor: AppMonitorModel = Field(alias="AppMonitor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
