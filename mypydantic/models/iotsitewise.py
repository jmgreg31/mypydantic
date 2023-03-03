# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AggregatesModel(BaseModel):
    average: Optional[float] = Field(default=None, alias="average")
    count: Optional[float] = Field(default=None, alias="count")
    maximum: Optional[float] = Field(default=None, alias="maximum")
    minimum: Optional[float] = Field(default=None, alias="minimum")
    sum: Optional[float] = Field(default=None, alias="sum")
    standard_deviation: Optional[float] = Field(default=None, alias="standardDeviation")


class AlarmsModel(BaseModel):
    alarm_role_arn: str = Field(alias="alarmRoleArn")
    notification_lambda_arn: Optional[str] = Field(
        default=None, alias="notificationLambdaArn"
    )


class AssetErrorDetailsModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    code: Literal["INTERNAL_FAILURE"] = Field(alias="code")
    message: str = Field(alias="message")


class AssetHierarchyInfoModel(BaseModel):
    parent_asset_id: Optional[str] = Field(default=None, alias="parentAssetId")
    child_asset_id: Optional[str] = Field(default=None, alias="childAssetId")


class AssetHierarchyModel(BaseModel):
    name: str = Field(alias="name")
    id: Optional[str] = Field(default=None, alias="id")


class AssetModelHierarchyDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    child_asset_model_id: str = Field(alias="childAssetModelId")


class AssetModelHierarchyModel(BaseModel):
    name: str = Field(alias="name")
    child_asset_model_id: str = Field(alias="childAssetModelId")
    id: Optional[str] = Field(default=None, alias="id")


class PropertyNotificationModel(BaseModel):
    topic: str = Field(alias="topic")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="state")


class TimeInNanosModel(BaseModel):
    time_in_seconds: int = Field(alias="timeInSeconds")
    offset_in_nanos: Optional[int] = Field(default=None, alias="offsetInNanos")


class VariantModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    integer_value: Optional[int] = Field(default=None, alias="integerValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    boolean_value: Optional[bool] = Field(default=None, alias="booleanValue")


class AssociateAssetsRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    hierarchy_id: str = Field(alias="hierarchyId")
    child_asset_id: str = Field(alias="childAssetId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AssociateTimeSeriesToAssetPropertyRequestModel(BaseModel):
    alias: str = Field(alias="alias")
    asset_id: str = Field(alias="assetId")
    property_id: str = Field(alias="propertyId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AttributeModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="defaultValue")


class BatchAssociateProjectAssetsRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    asset_ids: Sequence[str] = Field(alias="assetIds")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDisassociateProjectAssetsRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    asset_ids: Sequence[str] = Field(alias="assetIds")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class BatchGetAssetPropertyAggregatesEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    aggregate_types: Sequence[
        Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
    ] = Field(alias="aggregateTypes")
    resolution: str = Field(alias="resolution")
    start_date: Union[datetime, str] = Field(alias="startDate")
    end_date: Union[datetime, str] = Field(alias="endDate")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )


class BatchGetAssetPropertyAggregatesErrorEntryModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    entry_id: str = Field(alias="entryId")


class BatchGetAssetPropertyAggregatesErrorInfoModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_timestamp: datetime = Field(alias="errorTimestamp")


class BatchGetAssetPropertyValueEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")


class BatchGetAssetPropertyValueErrorEntryModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    entry_id: str = Field(alias="entryId")


class BatchGetAssetPropertyValueErrorInfoModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_timestamp: datetime = Field(alias="errorTimestamp")


class BatchGetAssetPropertyValueHistoryEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="startDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="endDate")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )


class BatchGetAssetPropertyValueHistoryErrorEntryModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    entry_id: str = Field(alias="entryId")


class BatchGetAssetPropertyValueHistoryErrorInfoModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
    ] = Field(alias="errorCode")
    error_timestamp: datetime = Field(alias="errorTimestamp")


class ConfigurationErrorDetailsModel(BaseModel):
    code: Literal["INTERNAL_FAILURE", "VALIDATION_ERROR"] = Field(alias="code")
    message: str = Field(alias="message")


class CreateAssetRequestModel(BaseModel):
    asset_name: str = Field(alias="assetName")
    asset_model_id: str = Field(alias="assetModelId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    asset_description: Optional[str] = Field(default=None, alias="assetDescription")


class ErrorReportLocationModel(BaseModel):
    bucket: str = Field(alias="bucket")
    prefix: str = Field(alias="prefix")


class FileModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")
    version_id: Optional[str] = Field(default=None, alias="versionId")


class CreateDashboardRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    dashboard_name: str = Field(alias="dashboardName")
    dashboard_definition: str = Field(alias="dashboardDefinition")
    dashboard_description: Optional[str] = Field(
        default=None, alias="dashboardDescription"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ImageFileModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="data")
    type: Literal["PNG"] = Field(alias="type")


class CreateProjectRequestModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    project_name: str = Field(alias="projectName")
    project_description: Optional[str] = Field(default=None, alias="projectDescription")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CsvModel(BaseModel):
    column_names: Optional[
        Sequence[
            Literal[
                "ALIAS",
                "ASSET_ID",
                "DATA_TYPE",
                "PROPERTY_ID",
                "QUALITY",
                "TIMESTAMP_NANO_OFFSET",
                "TIMESTAMP_SECONDS",
                "VALUE",
            ]
        ]
    ] = Field(default=None, alias="columnNames")


class CustomerManagedS3StorageModel(BaseModel):
    s3_resource_arn: str = Field(alias="s3ResourceArn")
    role_arn: str = Field(alias="roleArn")


class DashboardSummaryModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_update_date: Optional[datetime] = Field(default=None, alias="lastUpdateDate")


class DeleteAccessPolicyRequestModel(BaseModel):
    access_policy_id: str = Field(alias="accessPolicyId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteAssetModelRequestModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteDashboardRequestModel(BaseModel):
    dashboard_id: str = Field(alias="dashboardId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteGatewayRequestModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")


class DeletePortalRequestModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteTimeSeriesRequestModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="alias")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DescribeAccessPolicyRequestModel(BaseModel):
    access_policy_id: str = Field(alias="accessPolicyId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeAssetModelRequestModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")


class DescribeAssetPropertyRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    property_id: str = Field(alias="propertyId")


class DescribeAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")


class DescribeBulkImportJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class DescribeDashboardRequestModel(BaseModel):
    dashboard_id: str = Field(alias="dashboardId")


class DescribeGatewayCapabilityConfigurationRequestModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    capability_namespace: str = Field(alias="capabilityNamespace")


class DescribeGatewayRequestModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")


class GatewayCapabilitySummaryModel(BaseModel):
    capability_namespace: str = Field(alias="capabilityNamespace")
    capability_sync_status: Literal[
        "IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED", "UNKNOWN"
    ] = Field(alias="capabilitySyncStatus")


class LoggingOptionsModel(BaseModel):
    level: Literal["ERROR", "INFO", "OFF"] = Field(alias="level")


class DescribePortalRequestModel(BaseModel):
    portal_id: str = Field(alias="portalId")


class ImageLocationModel(BaseModel):
    id: str = Field(alias="id")
    url: str = Field(alias="url")


class DescribeProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")


class RetentionPeriodModel(BaseModel):
    number_of_days: Optional[int] = Field(default=None, alias="numberOfDays")
    unlimited: Optional[bool] = Field(default=None, alias="unlimited")


class DescribeTimeSeriesRequestModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="alias")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")


class DetailedErrorModel(BaseModel):
    code: Literal[
        "INCOMPATIBLE_COMPUTE_LOCATION", "INCOMPATIBLE_FORWARDING_CONFIGURATION"
    ] = Field(alias="code")
    message: str = Field(alias="message")


class DisassociateAssetsRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    hierarchy_id: str = Field(alias="hierarchyId")
    child_asset_id: str = Field(alias="childAssetId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DisassociateTimeSeriesFromAssetPropertyRequestModel(BaseModel):
    alias: str = Field(alias="alias")
    asset_id: str = Field(alias="assetId")
    property_id: str = Field(alias="propertyId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class VariableValueModel(BaseModel):
    property_id: str = Field(alias="propertyId")
    hierarchy_id: Optional[str] = Field(default=None, alias="hierarchyId")


class ForwardingConfigModel(BaseModel):
    state: Literal["DISABLED", "ENABLED"] = Field(alias="state")


class GreengrassModel(BaseModel):
    group_arn: str = Field(alias="groupArn")


class GreengrassV2Model(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetAssetPropertyAggregatesRequestModel(BaseModel):
    aggregate_types: Sequence[
        Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
    ] = Field(alias="aggregateTypes")
    resolution: str = Field(alias="resolution")
    start_date: Union[datetime, str] = Field(alias="startDate")
    end_date: Union[datetime, str] = Field(alias="endDate")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetAssetPropertyValueHistoryRequestModel(BaseModel):
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="startDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="endDate")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetAssetPropertyValueRequestModel(BaseModel):
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")


class GetInterpolatedAssetPropertyValuesRequestModel(BaseModel):
    start_time_in_seconds: int = Field(alias="startTimeInSeconds")
    end_time_in_seconds: int = Field(alias="endTimeInSeconds")
    quality: Literal["BAD", "GOOD", "UNCERTAIN"] = Field(alias="quality")
    interval_in_seconds: int = Field(alias="intervalInSeconds")
    type: str = Field(alias="type")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    start_time_offset_in_nanos: Optional[int] = Field(
        default=None, alias="startTimeOffsetInNanos"
    )
    end_time_offset_in_nanos: Optional[int] = Field(
        default=None, alias="endTimeOffsetInNanos"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    interval_window_in_seconds: Optional[int] = Field(
        default=None, alias="intervalWindowInSeconds"
    )


class GroupIdentityModel(BaseModel):
    id: str = Field(alias="id")


class IAMRoleIdentityModel(BaseModel):
    arn: str = Field(alias="arn")


class IAMUserIdentityModel(BaseModel):
    arn: str = Field(alias="arn")


class UserIdentityModel(BaseModel):
    id: str = Field(alias="id")


class JobSummaryModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "PENDING",
        "RUNNING",
    ] = Field(alias="status")


class ListAccessPoliciesRequestModel(BaseModel):
    identity_type: Optional[Literal["GROUP", "IAM", "USER"]] = Field(
        default=None, alias="identityType"
    )
    identity_id: Optional[str] = Field(default=None, alias="identityId")
    resource_type: Optional[Literal["PORTAL", "PROJECT"]] = Field(
        default=None, alias="resourceType"
    )
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    iam_arn: Optional[str] = Field(default=None, alias="iamArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssetModelPropertiesRequestModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[Literal["ALL", "BASE"]] = Field(default=None, alias="filter")


class ListAssetModelsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssetPropertiesRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[Literal["ALL", "BASE"]] = Field(default=None, alias="filter")


class ListAssetRelationshipsRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    traversal_type: Literal["PATH_TO_ROOT"] = Field(alias="traversalType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    asset_model_id: Optional[str] = Field(default=None, alias="assetModelId")
    filter: Optional[Literal["ALL", "TOP_LEVEL"]] = Field(default=None, alias="filter")


class ListAssociatedAssetsRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    hierarchy_id: Optional[str] = Field(default=None, alias="hierarchyId")
    traversal_direction: Optional[Literal["CHILD", "PARENT"]] = Field(
        default=None, alias="traversalDirection"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListBulkImportJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filter: Optional[
        Literal[
            "ALL",
            "CANCELLED",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="filter")


class ListDashboardsRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListGatewaysRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListPortalsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListProjectAssetsRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListProjectsRequestModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ProjectSummaryModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_update_date: Optional[datetime] = Field(default=None, alias="lastUpdateDate")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTimeSeriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    alias_prefix: Optional[str] = Field(default=None, alias="aliasPrefix")
    time_series_type: Optional[Literal["ASSOCIATED", "DISASSOCIATED"]] = Field(
        default=None, alias="timeSeriesType"
    )


class TimeSeriesSummaryModel(BaseModel):
    time_series_id: str = Field(alias="timeSeriesId")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    time_series_creation_date: datetime = Field(alias="timeSeriesCreationDate")
    time_series_last_update_date: datetime = Field(alias="timeSeriesLastUpdateDate")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    alias: Optional[str] = Field(default=None, alias="alias")
    data_type_spec: Optional[str] = Field(default=None, alias="dataTypeSpec")


class MetricProcessingConfigModel(BaseModel):
    compute_location: Literal["CLOUD", "EDGE"] = Field(alias="computeLocation")


class TumblingWindowModel(BaseModel):
    interval: str = Field(alias="interval")
    offset: Optional[str] = Field(default=None, alias="offset")


class MonitorErrorDetailsModel(BaseModel):
    code: Optional[
        Literal["INTERNAL_FAILURE", "LIMIT_EXCEEDED", "VALIDATION_ERROR"]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class PortalResourceModel(BaseModel):
    id: str = Field(alias="id")


class ProjectResourceModel(BaseModel):
    id: str = Field(alias="id")


class PutDefaultEncryptionConfigurationRequestModel(BaseModel):
    encryption_type: Literal[
        "KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"
    ] = Field(alias="encryptionType")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAssetPropertyRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    property_id: str = Field(alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    property_notification_state: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="propertyNotificationState"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    property_unit: Optional[str] = Field(default=None, alias="propertyUnit")


class UpdateAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    asset_name: str = Field(alias="assetName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    asset_description: Optional[str] = Field(default=None, alias="assetDescription")


class UpdateDashboardRequestModel(BaseModel):
    dashboard_id: str = Field(alias="dashboardId")
    dashboard_name: str = Field(alias="dashboardName")
    dashboard_definition: str = Field(alias="dashboardDefinition")
    dashboard_description: Optional[str] = Field(
        default=None, alias="dashboardDescription"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateGatewayCapabilityConfigurationRequestModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    capability_namespace: str = Field(alias="capabilityNamespace")
    capability_configuration: str = Field(alias="capabilityConfiguration")


class UpdateGatewayRequestModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    gateway_name: str = Field(alias="gatewayName")


class UpdateProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    project_name: str = Field(alias="projectName")
    project_description: Optional[str] = Field(default=None, alias="projectDescription")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AggregatedValueModel(BaseModel):
    timestamp: datetime = Field(alias="timestamp")
    value: AggregatesModel = Field(alias="value")
    quality: Optional[Literal["BAD", "GOOD", "UNCERTAIN"]] = Field(
        default=None, alias="quality"
    )


class AssetRelationshipSummaryModel(BaseModel):
    relationship_type: Literal["HIERARCHY"] = Field(alias="relationshipType")
    hierarchy_info: Optional[AssetHierarchyInfoModel] = Field(
        default=None, alias="hierarchyInfo"
    )


class AssetPropertySummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    alias: Optional[str] = Field(default=None, alias="alias")
    unit: Optional[str] = Field(default=None, alias="unit")
    notification: Optional[PropertyNotificationModel] = Field(
        default=None, alias="notification"
    )
    asset_composite_model_id: Optional[str] = Field(
        default=None, alias="assetCompositeModelId"
    )


class AssetPropertyModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    alias: Optional[str] = Field(default=None, alias="alias")
    notification: Optional[PropertyNotificationModel] = Field(
        default=None, alias="notification"
    )
    data_type_spec: Optional[str] = Field(default=None, alias="dataTypeSpec")
    unit: Optional[str] = Field(default=None, alias="unit")


class BatchPutAssetPropertyErrorModel(BaseModel):
    error_code: Literal[
        "AccessDeniedException",
        "ConflictingOperationException",
        "InternalFailureException",
        "InvalidRequestException",
        "LimitExceededException",
        "ResourceNotFoundException",
        "ServiceUnavailableException",
        "ThrottlingException",
        "TimestampOutOfRangeException",
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    timestamps: List[TimeInNanosModel] = Field(alias="timestamps")


class AssetPropertyValueModel(BaseModel):
    value: VariantModel = Field(alias="value")
    timestamp: TimeInNanosModel = Field(alias="timestamp")
    quality: Optional[Literal["BAD", "GOOD", "UNCERTAIN"]] = Field(
        default=None, alias="quality"
    )


class InterpolatedAssetPropertyValueModel(BaseModel):
    timestamp: TimeInNanosModel = Field(alias="timestamp")
    value: VariantModel = Field(alias="value")


class BatchAssociateProjectAssetsResponseModel(BaseModel):
    errors: List[AssetErrorDetailsModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateProjectAssetsResponseModel(BaseModel):
    errors: List[AssetErrorDetailsModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPolicyResponseModel(BaseModel):
    access_policy_id: str = Field(alias="accessPolicyId")
    access_policy_arn: str = Field(alias="accessPolicyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBulkImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_name: str = Field(alias="jobName")
    job_status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "PENDING",
        "RUNNING",
    ] = Field(alias="jobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDashboardResponseModel(BaseModel):
    dashboard_id: str = Field(alias="dashboardId")
    dashboard_arn: str = Field(alias="dashboardArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGatewayResponseModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    gateway_arn: str = Field(alias="gatewayArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResponseModel(BaseModel):
    project_id: str = Field(alias="projectId")
    project_arn: str = Field(alias="projectArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDashboardResponseModel(BaseModel):
    dashboard_id: str = Field(alias="dashboardId")
    dashboard_arn: str = Field(alias="dashboardArn")
    dashboard_name: str = Field(alias="dashboardName")
    project_id: str = Field(alias="projectId")
    dashboard_description: str = Field(alias="dashboardDescription")
    dashboard_definition: str = Field(alias="dashboardDefinition")
    dashboard_creation_date: datetime = Field(alias="dashboardCreationDate")
    dashboard_last_update_date: datetime = Field(alias="dashboardLastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGatewayCapabilityConfigurationResponseModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    capability_namespace: str = Field(alias="capabilityNamespace")
    capability_configuration: str = Field(alias="capabilityConfiguration")
    capability_sync_status: Literal[
        "IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED", "UNKNOWN"
    ] = Field(alias="capabilitySyncStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProjectResponseModel(BaseModel):
    project_id: str = Field(alias="projectId")
    project_arn: str = Field(alias="projectArn")
    project_name: str = Field(alias="projectName")
    portal_id: str = Field(alias="portalId")
    project_description: str = Field(alias="projectDescription")
    project_creation_date: datetime = Field(alias="projectCreationDate")
    project_last_update_date: datetime = Field(alias="projectLastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTimeSeriesResponseModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    property_id: str = Field(alias="propertyId")
    alias: str = Field(alias="alias")
    time_series_id: str = Field(alias="timeSeriesId")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    data_type_spec: str = Field(alias="dataTypeSpec")
    time_series_creation_date: datetime = Field(alias="timeSeriesCreationDate")
    time_series_last_update_date: datetime = Field(alias="timeSeriesLastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectAssetsResponseModel(BaseModel):
    asset_ids: List[str] = Field(alias="assetIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewayCapabilityConfigurationResponseModel(BaseModel):
    capability_namespace: str = Field(alias="capabilityNamespace")
    capability_sync_status: Literal[
        "IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED", "UNKNOWN"
    ] = Field(alias="capabilitySyncStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetAssetPropertyAggregatesRequestModel(BaseModel):
    entries: Sequence[BatchGetAssetPropertyAggregatesEntryModel] = Field(
        alias="entries"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class BatchGetAssetPropertyAggregatesSkippedEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    completion_status: Literal["ERROR", "SUCCESS"] = Field(alias="completionStatus")
    error_info: Optional[BatchGetAssetPropertyAggregatesErrorInfoModel] = Field(
        default=None, alias="errorInfo"
    )


class BatchGetAssetPropertyValueRequestModel(BaseModel):
    entries: Sequence[BatchGetAssetPropertyValueEntryModel] = Field(alias="entries")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class BatchGetAssetPropertyValueSkippedEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    completion_status: Literal["ERROR", "SUCCESS"] = Field(alias="completionStatus")
    error_info: Optional[BatchGetAssetPropertyValueErrorInfoModel] = Field(
        default=None, alias="errorInfo"
    )


class BatchGetAssetPropertyValueHistoryRequestModel(BaseModel):
    entries: Sequence[BatchGetAssetPropertyValueHistoryEntryModel] = Field(
        alias="entries"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class BatchGetAssetPropertyValueHistorySkippedEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    completion_status: Literal["ERROR", "SUCCESS"] = Field(alias="completionStatus")
    error_info: Optional[BatchGetAssetPropertyValueHistoryErrorInfoModel] = Field(
        default=None, alias="errorInfo"
    )


class ConfigurationStatusModel(BaseModel):
    state: Literal["ACTIVE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"] = Field(
        alias="state"
    )
    error: Optional[ConfigurationErrorDetailsModel] = Field(default=None, alias="error")


class CreatePortalRequestModel(BaseModel):
    portal_name: str = Field(alias="portalName")
    portal_contact_email: str = Field(alias="portalContactEmail")
    role_arn: str = Field(alias="roleArn")
    portal_description: Optional[str] = Field(default=None, alias="portalDescription")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    portal_logo_image_file: Optional[ImageFileModel] = Field(
        default=None, alias="portalLogoImageFile"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    portal_auth_mode: Optional[Literal["IAM", "SSO"]] = Field(
        default=None, alias="portalAuthMode"
    )
    notification_sender_email: Optional[str] = Field(
        default=None, alias="notificationSenderEmail"
    )
    alarms: Optional[AlarmsModel] = Field(default=None, alias="alarms")


class ImageModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    file: Optional[ImageFileModel] = Field(default=None, alias="file")


class FileFormatModel(BaseModel):
    csv: Optional[CsvModel] = Field(default=None, alias="csv")


class MultiLayerStorageModel(BaseModel):
    customer_managed_s3_storage: CustomerManagedS3StorageModel = Field(
        alias="customerManagedS3Storage"
    )


class ListDashboardsResponseModel(BaseModel):
    dashboard_summaries: List[DashboardSummaryModel] = Field(alias="dashboardSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssetModelRequestAssetModelActiveWaitModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAssetModelRequestAssetModelNotExistsWaitModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAssetRequestAssetActiveWaitModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAssetRequestAssetNotExistsWaitModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    exclude_properties: Optional[bool] = Field(default=None, alias="excludeProperties")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribePortalRequestPortalActiveWaitModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribePortalRequestPortalNotExistsWaitModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeLoggingOptionsResponseModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingOptionsRequestModel(BaseModel):
    logging_options: LoggingOptionsModel = Field(alias="loggingOptions")


class ErrorDetailsModel(BaseModel):
    code: Literal["INTERNAL_FAILURE", "VALIDATION_ERROR"] = Field(alias="code")
    message: str = Field(alias="message")
    details: Optional[List[DetailedErrorModel]] = Field(default=None, alias="details")


class ExpressionVariableModel(BaseModel):
    name: str = Field(alias="name")
    value: VariableValueModel = Field(alias="value")


class MeasurementProcessingConfigModel(BaseModel):
    forwarding_config: ForwardingConfigModel = Field(alias="forwardingConfig")


class TransformProcessingConfigModel(BaseModel):
    compute_location: Literal["CLOUD", "EDGE"] = Field(alias="computeLocation")
    forwarding_config: Optional[ForwardingConfigModel] = Field(
        default=None, alias="forwardingConfig"
    )


class GatewayPlatformModel(BaseModel):
    greengrass: Optional[GreengrassModel] = Field(default=None, alias="greengrass")
    greengrass_v2: Optional[GreengrassV2Model] = Field(
        default=None, alias="greengrassV2"
    )


class GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateModel(
    BaseModel
):
    aggregate_types: Sequence[
        Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
    ] = Field(alias="aggregateTypes")
    resolution: str = Field(alias="resolution")
    start_date: Union[datetime, str] = Field(alias="startDate")
    end_date: Union[datetime, str] = Field(alias="endDate")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateModel(
    BaseModel
):
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    start_date: Optional[Union[datetime, str]] = Field(default=None, alias="startDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="endDate")
    qualities: Optional[Sequence[Literal["BAD", "GOOD", "UNCERTAIN"]]] = Field(
        default=None, alias="qualities"
    )
    time_ordering: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="timeOrdering"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateModel(
    BaseModel
):
    start_time_in_seconds: int = Field(alias="startTimeInSeconds")
    end_time_in_seconds: int = Field(alias="endTimeInSeconds")
    quality: Literal["BAD", "GOOD", "UNCERTAIN"] = Field(alias="quality")
    interval_in_seconds: int = Field(alias="intervalInSeconds")
    type: str = Field(alias="type")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")
    start_time_offset_in_nanos: Optional[int] = Field(
        default=None, alias="startTimeOffsetInNanos"
    )
    end_time_offset_in_nanos: Optional[int] = Field(
        default=None, alias="endTimeOffsetInNanos"
    )
    interval_window_in_seconds: Optional[int] = Field(
        default=None, alias="intervalWindowInSeconds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccessPoliciesRequestListAccessPoliciesPaginateModel(BaseModel):
    identity_type: Optional[Literal["GROUP", "IAM", "USER"]] = Field(
        default=None, alias="identityType"
    )
    identity_id: Optional[str] = Field(default=None, alias="identityId")
    resource_type: Optional[Literal["PORTAL", "PROJECT"]] = Field(
        default=None, alias="resourceType"
    )
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    iam_arn: Optional[str] = Field(default=None, alias="iamArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    filter: Optional[Literal["ALL", "BASE"]] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssetModelsRequestListAssetModelsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssetPropertiesRequestListAssetPropertiesPaginateModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    filter: Optional[Literal["ALL", "BASE"]] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssetRelationshipsRequestListAssetRelationshipsPaginateModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    traversal_type: Literal["PATH_TO_ROOT"] = Field(alias="traversalType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssetsRequestListAssetsPaginateModel(BaseModel):
    asset_model_id: Optional[str] = Field(default=None, alias="assetModelId")
    filter: Optional[Literal["ALL", "TOP_LEVEL"]] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociatedAssetsRequestListAssociatedAssetsPaginateModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    hierarchy_id: Optional[str] = Field(default=None, alias="hierarchyId")
    traversal_direction: Optional[Literal["CHILD", "PARENT"]] = Field(
        default=None, alias="traversalDirection"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBulkImportJobsRequestListBulkImportJobsPaginateModel(BaseModel):
    filter: Optional[
        Literal[
            "ALL",
            "CANCELLED",
            "COMPLETED",
            "COMPLETED_WITH_FAILURES",
            "FAILED",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDashboardsRequestListDashboardsPaginateModel(BaseModel):
    project_id: str = Field(alias="projectId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGatewaysRequestListGatewaysPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPortalsRequestListPortalsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectAssetsRequestListProjectAssetsPaginateModel(BaseModel):
    project_id: str = Field(alias="projectId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTimeSeriesRequestListTimeSeriesPaginateModel(BaseModel):
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    alias_prefix: Optional[str] = Field(default=None, alias="aliasPrefix")
    time_series_type: Optional[Literal["ASSOCIATED", "DISASSOCIATED"]] = Field(
        default=None, alias="timeSeriesType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class IdentityModel(BaseModel):
    user: Optional[UserIdentityModel] = Field(default=None, alias="user")
    group: Optional[GroupIdentityModel] = Field(default=None, alias="group")
    iam_user: Optional[IAMUserIdentityModel] = Field(default=None, alias="iamUser")
    iam_role: Optional[IAMRoleIdentityModel] = Field(default=None, alias="iamRole")


class ListBulkImportJobsResponseModel(BaseModel):
    job_summaries: List[JobSummaryModel] = Field(alias="jobSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsResponseModel(BaseModel):
    project_summaries: List[ProjectSummaryModel] = Field(alias="projectSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTimeSeriesResponseModel(BaseModel):
    time_series_summaries: List[TimeSeriesSummaryModel] = Field(
        alias="TimeSeriesSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricWindowModel(BaseModel):
    tumbling: Optional[TumblingWindowModel] = Field(default=None, alias="tumbling")


class PortalStatusModel(BaseModel):
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="state"
    )
    error: Optional[MonitorErrorDetailsModel] = Field(default=None, alias="error")


class ResourceModel(BaseModel):
    portal: Optional[PortalResourceModel] = Field(default=None, alias="portal")
    project: Optional[ProjectResourceModel] = Field(default=None, alias="project")


class BatchGetAssetPropertyAggregatesSuccessEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    aggregated_values: List[AggregatedValueModel] = Field(alias="aggregatedValues")


class GetAssetPropertyAggregatesResponseModel(BaseModel):
    aggregated_values: List[AggregatedValueModel] = Field(alias="aggregatedValues")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetRelationshipsResponseModel(BaseModel):
    asset_relationship_summaries: List[AssetRelationshipSummaryModel] = Field(
        alias="assetRelationshipSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetPropertiesResponseModel(BaseModel):
    asset_property_summaries: List[AssetPropertySummaryModel] = Field(
        alias="assetPropertySummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetCompositeModelModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    properties: List[AssetPropertyModel] = Field(alias="properties")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")


class BatchPutAssetPropertyErrorEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    errors: List[BatchPutAssetPropertyErrorModel] = Field(alias="errors")


class BatchGetAssetPropertyValueHistorySuccessEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    asset_property_value_history: List[AssetPropertyValueModel] = Field(
        alias="assetPropertyValueHistory"
    )


class BatchGetAssetPropertyValueSuccessEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    asset_property_value: Optional[AssetPropertyValueModel] = Field(
        default=None, alias="assetPropertyValue"
    )


class GetAssetPropertyValueHistoryResponseModel(BaseModel):
    asset_property_value_history: List[AssetPropertyValueModel] = Field(
        alias="assetPropertyValueHistory"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssetPropertyValueResponseModel(BaseModel):
    property_value: AssetPropertyValueModel = Field(alias="propertyValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAssetPropertyValueEntryModel(BaseModel):
    entry_id: str = Field(alias="entryId")
    property_values: Sequence[AssetPropertyValueModel] = Field(alias="propertyValues")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")


class GetInterpolatedAssetPropertyValuesResponseModel(BaseModel):
    interpolated_asset_property_values: List[
        InterpolatedAssetPropertyValueModel
    ] = Field(alias="interpolatedAssetPropertyValues")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDefaultEncryptionConfigurationResponseModel(BaseModel):
    encryption_type: Literal[
        "KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"
    ] = Field(alias="encryptionType")
    kms_key_arn: str = Field(alias="kmsKeyArn")
    configuration_status: ConfigurationStatusModel = Field(alias="configurationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDefaultEncryptionConfigurationResponseModel(BaseModel):
    encryption_type: Literal[
        "KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"
    ] = Field(alias="encryptionType")
    kms_key_arn: str = Field(alias="kmsKeyArn")
    configuration_status: ConfigurationStatusModel = Field(alias="configurationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePortalRequestModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    portal_name: str = Field(alias="portalName")
    portal_contact_email: str = Field(alias="portalContactEmail")
    role_arn: str = Field(alias="roleArn")
    portal_description: Optional[str] = Field(default=None, alias="portalDescription")
    portal_logo_image: Optional[ImageModel] = Field(
        default=None, alias="portalLogoImage"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    notification_sender_email: Optional[str] = Field(
        default=None, alias="notificationSenderEmail"
    )
    alarms: Optional[AlarmsModel] = Field(default=None, alias="alarms")


class JobConfigurationModel(BaseModel):
    file_format: FileFormatModel = Field(alias="fileFormat")


class DescribeStorageConfigurationResponseModel(BaseModel):
    storage_type: Literal["MULTI_LAYER_STORAGE", "SITEWISE_DEFAULT_STORAGE"] = Field(
        alias="storageType"
    )
    multi_layer_storage: MultiLayerStorageModel = Field(alias="multiLayerStorage")
    disassociated_data_storage: Literal["DISABLED", "ENABLED"] = Field(
        alias="disassociatedDataStorage"
    )
    retention_period: RetentionPeriodModel = Field(alias="retentionPeriod")
    configuration_status: ConfigurationStatusModel = Field(alias="configurationStatus")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutStorageConfigurationRequestModel(BaseModel):
    storage_type: Literal["MULTI_LAYER_STORAGE", "SITEWISE_DEFAULT_STORAGE"] = Field(
        alias="storageType"
    )
    multi_layer_storage: Optional[MultiLayerStorageModel] = Field(
        default=None, alias="multiLayerStorage"
    )
    disassociated_data_storage: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="disassociatedDataStorage"
    )
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="retentionPeriod"
    )


class PutStorageConfigurationResponseModel(BaseModel):
    storage_type: Literal["MULTI_LAYER_STORAGE", "SITEWISE_DEFAULT_STORAGE"] = Field(
        alias="storageType"
    )
    multi_layer_storage: MultiLayerStorageModel = Field(alias="multiLayerStorage")
    disassociated_data_storage: Literal["DISABLED", "ENABLED"] = Field(
        alias="disassociatedDataStorage"
    )
    retention_period: RetentionPeriodModel = Field(alias="retentionPeriod")
    configuration_status: ConfigurationStatusModel = Field(alias="configurationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetModelStatusModel(BaseModel):
    state: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "PROPAGATING", "UPDATING"
    ] = Field(alias="state")
    error: Optional[ErrorDetailsModel] = Field(default=None, alias="error")


class AssetStatusModel(BaseModel):
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="state"
    )
    error: Optional[ErrorDetailsModel] = Field(default=None, alias="error")


class MeasurementModel(BaseModel):
    processing_config: Optional[MeasurementProcessingConfigModel] = Field(
        default=None, alias="processingConfig"
    )


class TransformModel(BaseModel):
    expression: str = Field(alias="expression")
    variables: Sequence[ExpressionVariableModel] = Field(alias="variables")
    processing_config: Optional[TransformProcessingConfigModel] = Field(
        default=None, alias="processingConfig"
    )


class CreateGatewayRequestModel(BaseModel):
    gateway_name: str = Field(alias="gatewayName")
    gateway_platform: GatewayPlatformModel = Field(alias="gatewayPlatform")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DescribeGatewayResponseModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    gateway_name: str = Field(alias="gatewayName")
    gateway_arn: str = Field(alias="gatewayArn")
    gateway_platform: GatewayPlatformModel = Field(alias="gatewayPlatform")
    gateway_capability_summaries: List[GatewayCapabilitySummaryModel] = Field(
        alias="gatewayCapabilitySummaries"
    )
    creation_date: datetime = Field(alias="creationDate")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GatewaySummaryModel(BaseModel):
    gateway_id: str = Field(alias="gatewayId")
    gateway_name: str = Field(alias="gatewayName")
    creation_date: datetime = Field(alias="creationDate")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    gateway_platform: Optional[GatewayPlatformModel] = Field(
        default=None, alias="gatewayPlatform"
    )
    gateway_capability_summaries: Optional[List[GatewayCapabilitySummaryModel]] = Field(
        default=None, alias="gatewayCapabilitySummaries"
    )


class MetricModel(BaseModel):
    expression: str = Field(alias="expression")
    variables: Sequence[ExpressionVariableModel] = Field(alias="variables")
    window: MetricWindowModel = Field(alias="window")
    processing_config: Optional[MetricProcessingConfigModel] = Field(
        default=None, alias="processingConfig"
    )


class CreatePortalResponseModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    portal_arn: str = Field(alias="portalArn")
    portal_start_url: str = Field(alias="portalStartUrl")
    portal_status: PortalStatusModel = Field(alias="portalStatus")
    sso_application_id: str = Field(alias="ssoApplicationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePortalResponseModel(BaseModel):
    portal_status: PortalStatusModel = Field(alias="portalStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePortalResponseModel(BaseModel):
    portal_id: str = Field(alias="portalId")
    portal_arn: str = Field(alias="portalArn")
    portal_name: str = Field(alias="portalName")
    portal_description: str = Field(alias="portalDescription")
    portal_client_id: str = Field(alias="portalClientId")
    portal_start_url: str = Field(alias="portalStartUrl")
    portal_contact_email: str = Field(alias="portalContactEmail")
    portal_status: PortalStatusModel = Field(alias="portalStatus")
    portal_creation_date: datetime = Field(alias="portalCreationDate")
    portal_last_update_date: datetime = Field(alias="portalLastUpdateDate")
    portal_logo_image_location: ImageLocationModel = Field(
        alias="portalLogoImageLocation"
    )
    role_arn: str = Field(alias="roleArn")
    portal_auth_mode: Literal["IAM", "SSO"] = Field(alias="portalAuthMode")
    notification_sender_email: str = Field(alias="notificationSenderEmail")
    alarms: AlarmsModel = Field(alias="alarms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PortalSummaryModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    start_url: str = Field(alias="startUrl")
    status: PortalStatusModel = Field(alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_update_date: Optional[datetime] = Field(default=None, alias="lastUpdateDate")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class UpdatePortalResponseModel(BaseModel):
    portal_status: PortalStatusModel = Field(alias="portalStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessPolicySummaryModel(BaseModel):
    id: str = Field(alias="id")
    identity: IdentityModel = Field(alias="identity")
    resource: ResourceModel = Field(alias="resource")
    permission: Literal["ADMINISTRATOR", "VIEWER"] = Field(alias="permission")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_update_date: Optional[datetime] = Field(default=None, alias="lastUpdateDate")


class CreateAccessPolicyRequestModel(BaseModel):
    access_policy_identity: IdentityModel = Field(alias="accessPolicyIdentity")
    access_policy_resource: ResourceModel = Field(alias="accessPolicyResource")
    access_policy_permission: Literal["ADMINISTRATOR", "VIEWER"] = Field(
        alias="accessPolicyPermission"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DescribeAccessPolicyResponseModel(BaseModel):
    access_policy_id: str = Field(alias="accessPolicyId")
    access_policy_arn: str = Field(alias="accessPolicyArn")
    access_policy_identity: IdentityModel = Field(alias="accessPolicyIdentity")
    access_policy_resource: ResourceModel = Field(alias="accessPolicyResource")
    access_policy_permission: Literal["ADMINISTRATOR", "VIEWER"] = Field(
        alias="accessPolicyPermission"
    )
    access_policy_creation_date: datetime = Field(alias="accessPolicyCreationDate")
    access_policy_last_update_date: datetime = Field(alias="accessPolicyLastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccessPolicyRequestModel(BaseModel):
    access_policy_id: str = Field(alias="accessPolicyId")
    access_policy_identity: IdentityModel = Field(alias="accessPolicyIdentity")
    access_policy_resource: ResourceModel = Field(alias="accessPolicyResource")
    access_policy_permission: Literal["ADMINISTRATOR", "VIEWER"] = Field(
        alias="accessPolicyPermission"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class BatchGetAssetPropertyAggregatesResponseModel(BaseModel):
    error_entries: List[BatchGetAssetPropertyAggregatesErrorEntryModel] = Field(
        alias="errorEntries"
    )
    success_entries: List[BatchGetAssetPropertyAggregatesSuccessEntryModel] = Field(
        alias="successEntries"
    )
    skipped_entries: List[BatchGetAssetPropertyAggregatesSkippedEntryModel] = Field(
        alias="skippedEntries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutAssetPropertyValueResponseModel(BaseModel):
    error_entries: List[BatchPutAssetPropertyErrorEntryModel] = Field(
        alias="errorEntries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetAssetPropertyValueHistoryResponseModel(BaseModel):
    error_entries: List[BatchGetAssetPropertyValueHistoryErrorEntryModel] = Field(
        alias="errorEntries"
    )
    success_entries: List[BatchGetAssetPropertyValueHistorySuccessEntryModel] = Field(
        alias="successEntries"
    )
    skipped_entries: List[BatchGetAssetPropertyValueHistorySkippedEntryModel] = Field(
        alias="skippedEntries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetAssetPropertyValueResponseModel(BaseModel):
    error_entries: List[BatchGetAssetPropertyValueErrorEntryModel] = Field(
        alias="errorEntries"
    )
    success_entries: List[BatchGetAssetPropertyValueSuccessEntryModel] = Field(
        alias="successEntries"
    )
    skipped_entries: List[BatchGetAssetPropertyValueSkippedEntryModel] = Field(
        alias="skippedEntries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutAssetPropertyValueRequestModel(BaseModel):
    entries: Sequence[PutAssetPropertyValueEntryModel] = Field(alias="entries")


class CreateBulkImportJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    job_role_arn: str = Field(alias="jobRoleArn")
    files: Sequence[FileModel] = Field(alias="files")
    error_report_location: ErrorReportLocationModel = Field(alias="errorReportLocation")
    job_configuration: JobConfigurationModel = Field(alias="jobConfiguration")


class DescribeBulkImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_name: str = Field(alias="jobName")
    job_status: Literal[
        "CANCELLED",
        "COMPLETED",
        "COMPLETED_WITH_FAILURES",
        "FAILED",
        "PENDING",
        "RUNNING",
    ] = Field(alias="jobStatus")
    job_role_arn: str = Field(alias="jobRoleArn")
    files: List[FileModel] = Field(alias="files")
    error_report_location: ErrorReportLocationModel = Field(alias="errorReportLocation")
    job_configuration: JobConfigurationModel = Field(alias="jobConfiguration")
    job_creation_date: datetime = Field(alias="jobCreationDate")
    job_last_update_date: datetime = Field(alias="jobLastUpdateDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetModelSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    creation_date: datetime = Field(alias="creationDate")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    status: AssetModelStatusModel = Field(alias="status")


class CreateAssetModelResponseModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    asset_model_arn: str = Field(alias="assetModelArn")
    asset_model_status: AssetModelStatusModel = Field(alias="assetModelStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAssetModelResponseModel(BaseModel):
    asset_model_status: AssetModelStatusModel = Field(alias="assetModelStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssetModelResponseModel(BaseModel):
    asset_model_status: AssetModelStatusModel = Field(alias="assetModelStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    asset_model_id: str = Field(alias="assetModelId")
    creation_date: datetime = Field(alias="creationDate")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    status: AssetStatusModel = Field(alias="status")
    hierarchies: List[AssetHierarchyModel] = Field(alias="hierarchies")
    description: Optional[str] = Field(default=None, alias="description")


class AssociatedAssetsSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    asset_model_id: str = Field(alias="assetModelId")
    creation_date: datetime = Field(alias="creationDate")
    last_update_date: datetime = Field(alias="lastUpdateDate")
    status: AssetStatusModel = Field(alias="status")
    hierarchies: List[AssetHierarchyModel] = Field(alias="hierarchies")
    description: Optional[str] = Field(default=None, alias="description")


class CreateAssetResponseModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    asset_arn: str = Field(alias="assetArn")
    asset_status: AssetStatusModel = Field(alias="assetStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAssetResponseModel(BaseModel):
    asset_status: AssetStatusModel = Field(alias="assetStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAssetResponseModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    asset_arn: str = Field(alias="assetArn")
    asset_name: str = Field(alias="assetName")
    asset_model_id: str = Field(alias="assetModelId")
    asset_properties: List[AssetPropertyModel] = Field(alias="assetProperties")
    asset_hierarchies: List[AssetHierarchyModel] = Field(alias="assetHierarchies")
    asset_composite_models: List[AssetCompositeModelModel] = Field(
        alias="assetCompositeModels"
    )
    asset_creation_date: datetime = Field(alias="assetCreationDate")
    asset_last_update_date: datetime = Field(alias="assetLastUpdateDate")
    asset_status: AssetStatusModel = Field(alias="assetStatus")
    asset_description: str = Field(alias="assetDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssetResponseModel(BaseModel):
    asset_status: AssetStatusModel = Field(alias="assetStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGatewaysResponseModel(BaseModel):
    gateway_summaries: List[GatewaySummaryModel] = Field(alias="gatewaySummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PropertyTypeModel(BaseModel):
    attribute: Optional[AttributeModel] = Field(default=None, alias="attribute")
    measurement: Optional[MeasurementModel] = Field(default=None, alias="measurement")
    transform: Optional[TransformModel] = Field(default=None, alias="transform")
    metric: Optional[MetricModel] = Field(default=None, alias="metric")


class ListPortalsResponseModel(BaseModel):
    portal_summaries: List[PortalSummaryModel] = Field(alias="portalSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessPoliciesResponseModel(BaseModel):
    access_policy_summaries: List[AccessPolicySummaryModel] = Field(
        alias="accessPolicySummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetModelsResponseModel(BaseModel):
    asset_model_summaries: List[AssetModelSummaryModel] = Field(
        alias="assetModelSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssetsResponseModel(BaseModel):
    asset_summaries: List[AssetSummaryModel] = Field(alias="assetSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedAssetsResponseModel(BaseModel):
    asset_summaries: List[AssociatedAssetsSummaryModel] = Field(alias="assetSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetModelPropertyDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    type: PropertyTypeModel = Field(alias="type")
    data_type_spec: Optional[str] = Field(default=None, alias="dataTypeSpec")
    unit: Optional[str] = Field(default=None, alias="unit")


class AssetModelPropertySummaryModel(BaseModel):
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    type: PropertyTypeModel = Field(alias="type")
    id: Optional[str] = Field(default=None, alias="id")
    data_type_spec: Optional[str] = Field(default=None, alias="dataTypeSpec")
    unit: Optional[str] = Field(default=None, alias="unit")
    asset_model_composite_model_id: Optional[str] = Field(
        default=None, alias="assetModelCompositeModelId"
    )


class AssetModelPropertyModel(BaseModel):
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    type: PropertyTypeModel = Field(alias="type")
    id: Optional[str] = Field(default=None, alias="id")
    data_type_spec: Optional[str] = Field(default=None, alias="dataTypeSpec")
    unit: Optional[str] = Field(default=None, alias="unit")


class PropertyModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    data_type: Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"] = Field(
        alias="dataType"
    )
    alias: Optional[str] = Field(default=None, alias="alias")
    notification: Optional[PropertyNotificationModel] = Field(
        default=None, alias="notification"
    )
    unit: Optional[str] = Field(default=None, alias="unit")
    type: Optional[PropertyTypeModel] = Field(default=None, alias="type")


class AssetModelCompositeModelDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    properties: Optional[Sequence[AssetModelPropertyDefinitionModel]] = Field(
        default=None, alias="properties"
    )


class ListAssetModelPropertiesResponseModel(BaseModel):
    asset_model_property_summaries: List[AssetModelPropertySummaryModel] = Field(
        alias="assetModelPropertySummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetModelCompositeModelModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    properties: Optional[List[AssetModelPropertyModel]] = Field(
        default=None, alias="properties"
    )
    id: Optional[str] = Field(default=None, alias="id")


class CompositeModelPropertyModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    asset_property: PropertyModel = Field(alias="assetProperty")
    id: Optional[str] = Field(default=None, alias="id")


class CreateAssetModelRequestModel(BaseModel):
    asset_model_name: str = Field(alias="assetModelName")
    asset_model_description: Optional[str] = Field(
        default=None, alias="assetModelDescription"
    )
    asset_model_properties: Optional[
        Sequence[AssetModelPropertyDefinitionModel]
    ] = Field(default=None, alias="assetModelProperties")
    asset_model_hierarchies: Optional[
        Sequence[AssetModelHierarchyDefinitionModel]
    ] = Field(default=None, alias="assetModelHierarchies")
    asset_model_composite_models: Optional[
        Sequence[AssetModelCompositeModelDefinitionModel]
    ] = Field(default=None, alias="assetModelCompositeModels")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DescribeAssetModelResponseModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    asset_model_arn: str = Field(alias="assetModelArn")
    asset_model_name: str = Field(alias="assetModelName")
    asset_model_description: str = Field(alias="assetModelDescription")
    asset_model_properties: List[AssetModelPropertyModel] = Field(
        alias="assetModelProperties"
    )
    asset_model_hierarchies: List[AssetModelHierarchyModel] = Field(
        alias="assetModelHierarchies"
    )
    asset_model_composite_models: List[AssetModelCompositeModelModel] = Field(
        alias="assetModelCompositeModels"
    )
    asset_model_creation_date: datetime = Field(alias="assetModelCreationDate")
    asset_model_last_update_date: datetime = Field(alias="assetModelLastUpdateDate")
    asset_model_status: AssetModelStatusModel = Field(alias="assetModelStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssetModelRequestModel(BaseModel):
    asset_model_id: str = Field(alias="assetModelId")
    asset_model_name: str = Field(alias="assetModelName")
    asset_model_description: Optional[str] = Field(
        default=None, alias="assetModelDescription"
    )
    asset_model_properties: Optional[Sequence[AssetModelPropertyModel]] = Field(
        default=None, alias="assetModelProperties"
    )
    asset_model_hierarchies: Optional[Sequence[AssetModelHierarchyModel]] = Field(
        default=None, alias="assetModelHierarchies"
    )
    asset_model_composite_models: Optional[
        Sequence[AssetModelCompositeModelModel]
    ] = Field(default=None, alias="assetModelCompositeModels")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DescribeAssetPropertyResponseModel(BaseModel):
    asset_id: str = Field(alias="assetId")
    asset_name: str = Field(alias="assetName")
    asset_model_id: str = Field(alias="assetModelId")
    asset_property: PropertyModel = Field(alias="assetProperty")
    composite_model: CompositeModelPropertyModel = Field(alias="compositeModel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
