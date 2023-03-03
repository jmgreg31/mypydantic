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


class CloudWatchLoggingOptionModel(BaseModel):
    log_stream_arn: str = Field(alias="LogStreamARN")


class CloudWatchLoggingOptionDescriptionModel(BaseModel):
    log_stream_arn: str = Field(alias="LogStreamARN")
    cloud_watch_logging_option_id: Optional[str] = Field(
        default=None, alias="CloudWatchLoggingOptionId"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class VpcConfigurationModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")


class VpcConfigurationDescriptionModel(BaseModel):
    vpc_configuration_id: str = Field(alias="VpcConfigurationId")
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")


class ApplicationSnapshotConfigurationDescriptionModel(BaseModel):
    snapshots_enabled: bool = Field(alias="SnapshotsEnabled")


class ApplicationSnapshotConfigurationModel(BaseModel):
    snapshots_enabled: bool = Field(alias="SnapshotsEnabled")


class ApplicationSnapshotConfigurationUpdateModel(BaseModel):
    snapshots_enabled_update: bool = Field(alias="SnapshotsEnabledUpdate")


class VpcConfigurationUpdateModel(BaseModel):
    vpc_configuration_id: str = Field(alias="VpcConfigurationId")
    subnet_id_updates: Optional[Sequence[str]] = Field(
        default=None, alias="SubnetIdUpdates"
    )
    security_group_id_updates: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIdUpdates"
    )


class ApplicationMaintenanceConfigurationDescriptionModel(BaseModel):
    application_maintenance_window_start_time: str = Field(
        alias="ApplicationMaintenanceWindowStartTime"
    )
    application_maintenance_window_end_time: str = Field(
        alias="ApplicationMaintenanceWindowEndTime"
    )


class ApplicationMaintenanceConfigurationUpdateModel(BaseModel):
    application_maintenance_window_start_time_update: str = Field(
        alias="ApplicationMaintenanceWindowStartTimeUpdate"
    )


class ApplicationRestoreConfigurationModel(BaseModel):
    application_restore_type: Literal[
        "RESTORE_FROM_CUSTOM_SNAPSHOT",
        "RESTORE_FROM_LATEST_SNAPSHOT",
        "SKIP_RESTORE_FROM_SNAPSHOT",
    ] = Field(alias="ApplicationRestoreType")
    snapshot_name: Optional[str] = Field(default=None, alias="SnapshotName")


class ApplicationSummaryModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_arn: str = Field(alias="ApplicationARN")
    application_status: Literal[
        "AUTOSCALING",
        "DELETING",
        "FORCE_STOPPING",
        "MAINTENANCE",
        "READY",
        "ROLLED_BACK",
        "ROLLING_BACK",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATING",
    ] = Field(alias="ApplicationStatus")
    application_version_id: int = Field(alias="ApplicationVersionId")
    runtime_environment: Literal[
        "FLINK-1_11",
        "FLINK-1_13",
        "FLINK-1_15",
        "FLINK-1_6",
        "FLINK-1_8",
        "SQL-1_0",
        "ZEPPELIN-FLINK-1_0",
        "ZEPPELIN-FLINK-2_0",
    ] = Field(alias="RuntimeEnvironment")
    application_mode: Optional[Literal["INTERACTIVE", "STREAMING"]] = Field(
        default=None, alias="ApplicationMode"
    )


class ApplicationVersionSummaryModel(BaseModel):
    application_version_id: int = Field(alias="ApplicationVersionId")
    application_status: Literal[
        "AUTOSCALING",
        "DELETING",
        "FORCE_STOPPING",
        "MAINTENANCE",
        "READY",
        "ROLLED_BACK",
        "ROLLING_BACK",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATING",
    ] = Field(alias="ApplicationStatus")


class CSVMappingParametersModel(BaseModel):
    record_row_delimiter: str = Field(alias="RecordRowDelimiter")
    record_column_delimiter: str = Field(alias="RecordColumnDelimiter")


class GlueDataCatalogConfigurationDescriptionModel(BaseModel):
    database_arn: str = Field(alias="DatabaseARN")


class GlueDataCatalogConfigurationModel(BaseModel):
    database_arn: str = Field(alias="DatabaseARN")


class GlueDataCatalogConfigurationUpdateModel(BaseModel):
    database_arnupdate: str = Field(alias="DatabaseARNUpdate")


class CheckpointConfigurationDescriptionModel(BaseModel):
    configuration_type: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationType"
    )
    checkpointing_enabled: Optional[bool] = Field(
        default=None, alias="CheckpointingEnabled"
    )
    checkpoint_interval: Optional[int] = Field(default=None, alias="CheckpointInterval")
    min_pause_between_checkpoints: Optional[int] = Field(
        default=None, alias="MinPauseBetweenCheckpoints"
    )


class CheckpointConfigurationModel(BaseModel):
    configuration_type: Literal["CUSTOM", "DEFAULT"] = Field(alias="ConfigurationType")
    checkpointing_enabled: Optional[bool] = Field(
        default=None, alias="CheckpointingEnabled"
    )
    checkpoint_interval: Optional[int] = Field(default=None, alias="CheckpointInterval")
    min_pause_between_checkpoints: Optional[int] = Field(
        default=None, alias="MinPauseBetweenCheckpoints"
    )


class CheckpointConfigurationUpdateModel(BaseModel):
    configuration_type_update: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationTypeUpdate"
    )
    checkpointing_enabled_update: Optional[bool] = Field(
        default=None, alias="CheckpointingEnabledUpdate"
    )
    checkpoint_interval_update: Optional[int] = Field(
        default=None, alias="CheckpointIntervalUpdate"
    )
    min_pause_between_checkpoints_update: Optional[int] = Field(
        default=None, alias="MinPauseBetweenCheckpointsUpdate"
    )


class CloudWatchLoggingOptionUpdateModel(BaseModel):
    cloud_watch_logging_option_id: str = Field(alias="CloudWatchLoggingOptionId")
    log_stream_arnupdate: Optional[str] = Field(
        default=None, alias="LogStreamARNUpdate"
    )


class S3ApplicationCodeLocationDescriptionModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")
    object_version: Optional[str] = Field(default=None, alias="ObjectVersion")


class S3ContentLocationModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")
    object_version: Optional[str] = Field(default=None, alias="ObjectVersion")


class S3ContentLocationUpdateModel(BaseModel):
    bucket_arnupdate: Optional[str] = Field(default=None, alias="BucketARNUpdate")
    file_key_update: Optional[str] = Field(default=None, alias="FileKeyUpdate")
    object_version_update: Optional[str] = Field(
        default=None, alias="ObjectVersionUpdate"
    )


class CreateApplicationPresignedUrlRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    url_type: Literal["FLINK_DASHBOARD_URL", "ZEPPELIN_UI_URL"] = Field(alias="UrlType")
    session_expiration_duration_in_seconds: Optional[int] = Field(
        default=None, alias="SessionExpirationDurationInSeconds"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CreateApplicationSnapshotRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    snapshot_name: str = Field(alias="SnapshotName")


class MavenReferenceModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    artifact_id: str = Field(alias="ArtifactId")
    version: str = Field(alias="Version")


class DeleteApplicationCloudWatchLoggingOptionRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    cloud_watch_logging_option_id: str = Field(alias="CloudWatchLoggingOptionId")
    current_application_version_id: Optional[int] = Field(
        default=None, alias="CurrentApplicationVersionId"
    )
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")


class DeleteApplicationInputProcessingConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    input_id: str = Field(alias="InputId")


class DeleteApplicationOutputRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    output_id: str = Field(alias="OutputId")


class DeleteApplicationReferenceDataSourceRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    reference_id: str = Field(alias="ReferenceId")


class DeleteApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    create_timestamp: Union[datetime, str] = Field(alias="CreateTimestamp")


class DeleteApplicationSnapshotRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    snapshot_name: str = Field(alias="SnapshotName")
    snapshot_creation_timestamp: Union[datetime, str] = Field(
        alias="SnapshotCreationTimestamp"
    )


class DeleteApplicationVpcConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    vpc_configuration_id: str = Field(alias="VpcConfigurationId")
    current_application_version_id: Optional[int] = Field(
        default=None, alias="CurrentApplicationVersionId"
    )
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")


class S3ContentBaseLocationDescriptionModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    base_path: Optional[str] = Field(default=None, alias="BasePath")


class S3ContentBaseLocationModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    base_path: Optional[str] = Field(default=None, alias="BasePath")


class S3ContentBaseLocationUpdateModel(BaseModel):
    bucket_arnupdate: Optional[str] = Field(default=None, alias="BucketARNUpdate")
    base_path_update: Optional[str] = Field(default=None, alias="BasePathUpdate")


class DescribeApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    include_additional_details: Optional[bool] = Field(
        default=None, alias="IncludeAdditionalDetails"
    )


class DescribeApplicationSnapshotRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    snapshot_name: str = Field(alias="SnapshotName")


class SnapshotDetailsModel(BaseModel):
    snapshot_name: str = Field(alias="SnapshotName")
    snapshot_status: Literal["CREATING", "DELETING", "FAILED", "READY"] = Field(
        alias="SnapshotStatus"
    )
    application_version_id: int = Field(alias="ApplicationVersionId")
    snapshot_creation_timestamp: Optional[datetime] = Field(
        default=None, alias="SnapshotCreationTimestamp"
    )


class DescribeApplicationVersionRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_version_id: int = Field(alias="ApplicationVersionId")


class DestinationSchemaModel(BaseModel):
    record_format_type: Literal["CSV", "JSON"] = Field(alias="RecordFormatType")


class InputStartingPositionConfigurationModel(BaseModel):
    input_starting_position: Optional[
        Literal["LAST_STOPPED_POINT", "NOW", "TRIM_HORIZON"]
    ] = Field(default=None, alias="InputStartingPosition")


class S3ConfigurationModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")


class PropertyGroupModel(BaseModel):
    property_group_id: str = Field(alias="PropertyGroupId")
    property_map: Mapping[str, str] = Field(alias="PropertyMap")


class MonitoringConfigurationDescriptionModel(BaseModel):
    configuration_type: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationType"
    )
    metrics_level: Optional[
        Literal["APPLICATION", "OPERATOR", "PARALLELISM", "TASK"]
    ] = Field(default=None, alias="MetricsLevel")
    log_level: Optional[Literal["DEBUG", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="LogLevel"
    )


class ParallelismConfigurationDescriptionModel(BaseModel):
    configuration_type: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationType"
    )
    parallelism: Optional[int] = Field(default=None, alias="Parallelism")
    parallelism_per_kp_u: Optional[int] = Field(default=None, alias="ParallelismPerKPU")
    current_parallelism: Optional[int] = Field(default=None, alias="CurrentParallelism")
    auto_scaling_enabled: Optional[bool] = Field(
        default=None, alias="AutoScalingEnabled"
    )


class MonitoringConfigurationModel(BaseModel):
    configuration_type: Literal["CUSTOM", "DEFAULT"] = Field(alias="ConfigurationType")
    metrics_level: Optional[
        Literal["APPLICATION", "OPERATOR", "PARALLELISM", "TASK"]
    ] = Field(default=None, alias="MetricsLevel")
    log_level: Optional[Literal["DEBUG", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="LogLevel"
    )


class ParallelismConfigurationModel(BaseModel):
    configuration_type: Literal["CUSTOM", "DEFAULT"] = Field(alias="ConfigurationType")
    parallelism: Optional[int] = Field(default=None, alias="Parallelism")
    parallelism_per_kp_u: Optional[int] = Field(default=None, alias="ParallelismPerKPU")
    auto_scaling_enabled: Optional[bool] = Field(
        default=None, alias="AutoScalingEnabled"
    )


class MonitoringConfigurationUpdateModel(BaseModel):
    configuration_type_update: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationTypeUpdate"
    )
    metrics_level_update: Optional[
        Literal["APPLICATION", "OPERATOR", "PARALLELISM", "TASK"]
    ] = Field(default=None, alias="MetricsLevelUpdate")
    log_level_update: Optional[Literal["DEBUG", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="LogLevelUpdate"
    )


class ParallelismConfigurationUpdateModel(BaseModel):
    configuration_type_update: Optional[Literal["CUSTOM", "DEFAULT"]] = Field(
        default=None, alias="ConfigurationTypeUpdate"
    )
    parallelism_update: Optional[int] = Field(default=None, alias="ParallelismUpdate")
    parallelism_per_kp_uupdate: Optional[int] = Field(
        default=None, alias="ParallelismPerKPUUpdate"
    )
    auto_scaling_enabled_update: Optional[bool] = Field(
        default=None, alias="AutoScalingEnabledUpdate"
    )


class FlinkRunConfigurationModel(BaseModel):
    allow_non_restored_state: Optional[bool] = Field(
        default=None, alias="AllowNonRestoredState"
    )


class InputParallelismModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")


class KinesisFirehoseInputDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisStreamsInputDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class InputLambdaProcessorDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class InputLambdaProcessorModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class InputLambdaProcessorUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class InputParallelismUpdateModel(BaseModel):
    count_update: int = Field(alias="CountUpdate")


class RecordColumnModel(BaseModel):
    name: str = Field(alias="Name")
    sql_type: str = Field(alias="SqlType")
    mapping: Optional[str] = Field(default=None, alias="Mapping")


class KinesisFirehoseInputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class KinesisStreamsInputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class KinesisFirehoseInputUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class KinesisStreamsInputUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class JSONMappingParametersModel(BaseModel):
    record_row_path: str = Field(alias="RecordRowPath")


class KinesisFirehoseOutputDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisFirehoseOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class KinesisFirehoseOutputUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class KinesisStreamsOutputDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisStreamsOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class KinesisStreamsOutputUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class LambdaOutputDescriptionModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class LambdaOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class LambdaOutputUpdateModel(BaseModel):
    resource_arnupdate: str = Field(alias="ResourceARNUpdate")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationSnapshotsRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListApplicationVersionsRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListApplicationsRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class S3ReferenceDataSourceDescriptionModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")
    reference_role_arn: Optional[str] = Field(default=None, alias="ReferenceRoleARN")


class S3ReferenceDataSourceModel(BaseModel):
    bucket_arn: Optional[str] = Field(default=None, alias="BucketARN")
    file_key: Optional[str] = Field(default=None, alias="FileKey")


class S3ReferenceDataSourceUpdateModel(BaseModel):
    bucket_arnupdate: Optional[str] = Field(default=None, alias="BucketARNUpdate")
    file_key_update: Optional[str] = Field(default=None, alias="FileKeyUpdate")


class RollbackApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")


class StopApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    force: Optional[bool] = Field(default=None, alias="Force")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ZeppelinMonitoringConfigurationDescriptionModel(BaseModel):
    log_level: Optional[Literal["DEBUG", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="LogLevel"
    )


class ZeppelinMonitoringConfigurationModel(BaseModel):
    log_level: Literal["DEBUG", "ERROR", "INFO", "WARN"] = Field(alias="LogLevel")


class ZeppelinMonitoringConfigurationUpdateModel(BaseModel):
    log_level_update: Literal["DEBUG", "ERROR", "INFO", "WARN"] = Field(
        alias="LogLevelUpdate"
    )


class AddApplicationCloudWatchLoggingOptionRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    cloud_watch_logging_option: CloudWatchLoggingOptionModel = Field(
        alias="CloudWatchLoggingOption"
    )
    current_application_version_id: Optional[int] = Field(
        default=None, alias="CurrentApplicationVersionId"
    )
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")


class AddApplicationCloudWatchLoggingOptionResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    cloud_watch_logging_option_descriptions: List[
        CloudWatchLoggingOptionDescriptionModel
    ] = Field(alias="CloudWatchLoggingOptionDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationPresignedUrlResponseModel(BaseModel):
    authorized_url: str = Field(alias="AuthorizedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationCloudWatchLoggingOptionResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    cloud_watch_logging_option_descriptions: List[
        CloudWatchLoggingOptionDescriptionModel
    ] = Field(alias="CloudWatchLoggingOptionDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationInputProcessingConfigurationResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationOutputResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationReferenceDataSourceResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationVpcConfigurationResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddApplicationVpcConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    vpc_configuration: VpcConfigurationModel = Field(alias="VpcConfiguration")
    current_application_version_id: Optional[int] = Field(
        default=None, alias="CurrentApplicationVersionId"
    )
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")


class AddApplicationVpcConfigurationResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    vpc_configuration_description: VpcConfigurationDescriptionModel = Field(
        alias="VpcConfigurationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationMaintenanceConfigurationResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_maintenance_configuration_description: ApplicationMaintenanceConfigurationDescriptionModel = Field(
        alias="ApplicationMaintenanceConfigurationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationMaintenanceConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_maintenance_configuration_update: ApplicationMaintenanceConfigurationUpdateModel = Field(
        alias="ApplicationMaintenanceConfigurationUpdate"
    )


class ListApplicationsResponseModel(BaseModel):
    application_summaries: List[ApplicationSummaryModel] = Field(
        alias="ApplicationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationVersionsResponseModel(BaseModel):
    application_version_summaries: List[ApplicationVersionSummaryModel] = Field(
        alias="ApplicationVersionSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CatalogConfigurationDescriptionModel(BaseModel):
    glue_data_catalog_configuration_description: GlueDataCatalogConfigurationDescriptionModel = Field(
        alias="GlueDataCatalogConfigurationDescription"
    )


class CatalogConfigurationModel(BaseModel):
    glue_data_catalog_configuration: GlueDataCatalogConfigurationModel = Field(
        alias="GlueDataCatalogConfiguration"
    )


class CatalogConfigurationUpdateModel(BaseModel):
    glue_data_catalog_configuration_update: GlueDataCatalogConfigurationUpdateModel = (
        Field(alias="GlueDataCatalogConfigurationUpdate")
    )


class CodeContentDescriptionModel(BaseModel):
    text_content: Optional[str] = Field(default=None, alias="TextContent")
    code_md5: Optional[str] = Field(default=None, alias="CodeMD5")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    s3_application_code_location_description: Optional[
        S3ApplicationCodeLocationDescriptionModel
    ] = Field(default=None, alias="S3ApplicationCodeLocationDescription")


class CodeContentModel(BaseModel):
    text_content: Optional[str] = Field(default=None, alias="TextContent")
    zip_file_content: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="ZipFileContent")
    s3_content_location: Optional[S3ContentLocationModel] = Field(
        default=None, alias="S3ContentLocation"
    )


class CodeContentUpdateModel(BaseModel):
    text_content_update: Optional[str] = Field(default=None, alias="TextContentUpdate")
    zip_file_content_update: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="ZipFileContentUpdate")
    s3_content_location_update: Optional[S3ContentLocationUpdateModel] = Field(
        default=None, alias="S3ContentLocationUpdate"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CustomArtifactConfigurationDescriptionModel(BaseModel):
    artifact_type: Optional[Literal["DEPENDENCY_JAR", "UDF"]] = Field(
        default=None, alias="ArtifactType"
    )
    s3_content_location_description: Optional[S3ContentLocationModel] = Field(
        default=None, alias="S3ContentLocationDescription"
    )
    maven_reference_description: Optional[MavenReferenceModel] = Field(
        default=None, alias="MavenReferenceDescription"
    )


class CustomArtifactConfigurationModel(BaseModel):
    artifact_type: Literal["DEPENDENCY_JAR", "UDF"] = Field(alias="ArtifactType")
    s3_content_location: Optional[S3ContentLocationModel] = Field(
        default=None, alias="S3ContentLocation"
    )
    maven_reference: Optional[MavenReferenceModel] = Field(
        default=None, alias="MavenReference"
    )


class DeployAsApplicationConfigurationDescriptionModel(BaseModel):
    s3_content_location_description: S3ContentBaseLocationDescriptionModel = Field(
        alias="S3ContentLocationDescription"
    )


class DeployAsApplicationConfigurationModel(BaseModel):
    s3_content_location: S3ContentBaseLocationModel = Field(alias="S3ContentLocation")


class DeployAsApplicationConfigurationUpdateModel(BaseModel):
    s3_content_location_update: Optional[S3ContentBaseLocationUpdateModel] = Field(
        default=None, alias="S3ContentLocationUpdate"
    )


class DescribeApplicationSnapshotResponseModel(BaseModel):
    snapshot_details: SnapshotDetailsModel = Field(alias="SnapshotDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationSnapshotsResponseModel(BaseModel):
    snapshot_summaries: List[SnapshotDetailsModel] = Field(alias="SnapshotSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SqlRunConfigurationModel(BaseModel):
    input_id: str = Field(alias="InputId")
    input_starting_position_configuration: InputStartingPositionConfigurationModel = (
        Field(alias="InputStartingPositionConfiguration")
    )


class EnvironmentPropertiesModel(BaseModel):
    property_groups: Sequence[PropertyGroupModel] = Field(alias="PropertyGroups")


class EnvironmentPropertyDescriptionsModel(BaseModel):
    property_group_descriptions: Optional[List[PropertyGroupModel]] = Field(
        default=None, alias="PropertyGroupDescriptions"
    )


class EnvironmentPropertyUpdatesModel(BaseModel):
    property_groups: Sequence[PropertyGroupModel] = Field(alias="PropertyGroups")


class FlinkApplicationConfigurationDescriptionModel(BaseModel):
    checkpoint_configuration_description: Optional[
        CheckpointConfigurationDescriptionModel
    ] = Field(default=None, alias="CheckpointConfigurationDescription")
    monitoring_configuration_description: Optional[
        MonitoringConfigurationDescriptionModel
    ] = Field(default=None, alias="MonitoringConfigurationDescription")
    parallelism_configuration_description: Optional[
        ParallelismConfigurationDescriptionModel
    ] = Field(default=None, alias="ParallelismConfigurationDescription")
    job_plan_description: Optional[str] = Field(
        default=None, alias="JobPlanDescription"
    )


class FlinkApplicationConfigurationModel(BaseModel):
    checkpoint_configuration: Optional[CheckpointConfigurationModel] = Field(
        default=None, alias="CheckpointConfiguration"
    )
    monitoring_configuration: Optional[MonitoringConfigurationModel] = Field(
        default=None, alias="MonitoringConfiguration"
    )
    parallelism_configuration: Optional[ParallelismConfigurationModel] = Field(
        default=None, alias="ParallelismConfiguration"
    )


class FlinkApplicationConfigurationUpdateModel(BaseModel):
    checkpoint_configuration_update: Optional[
        CheckpointConfigurationUpdateModel
    ] = Field(default=None, alias="CheckpointConfigurationUpdate")
    monitoring_configuration_update: Optional[
        MonitoringConfigurationUpdateModel
    ] = Field(default=None, alias="MonitoringConfigurationUpdate")
    parallelism_configuration_update: Optional[
        ParallelismConfigurationUpdateModel
    ] = Field(default=None, alias="ParallelismConfigurationUpdate")


class RunConfigurationDescriptionModel(BaseModel):
    application_restore_configuration_description: Optional[
        ApplicationRestoreConfigurationModel
    ] = Field(default=None, alias="ApplicationRestoreConfigurationDescription")
    flink_run_configuration_description: Optional[FlinkRunConfigurationModel] = Field(
        default=None, alias="FlinkRunConfigurationDescription"
    )


class RunConfigurationUpdateModel(BaseModel):
    flink_run_configuration: Optional[FlinkRunConfigurationModel] = Field(
        default=None, alias="FlinkRunConfiguration"
    )
    application_restore_configuration: Optional[
        ApplicationRestoreConfigurationModel
    ] = Field(default=None, alias="ApplicationRestoreConfiguration")


class InputProcessingConfigurationDescriptionModel(BaseModel):
    input_lambda_processor_description: Optional[
        InputLambdaProcessorDescriptionModel
    ] = Field(default=None, alias="InputLambdaProcessorDescription")


class InputProcessingConfigurationModel(BaseModel):
    input_lambda_processor: InputLambdaProcessorModel = Field(
        alias="InputLambdaProcessor"
    )


class InputProcessingConfigurationUpdateModel(BaseModel):
    input_lambda_processor_update: InputLambdaProcessorUpdateModel = Field(
        alias="InputLambdaProcessorUpdate"
    )


class MappingParametersModel(BaseModel):
    js_onmapping_parameters: Optional[JSONMappingParametersModel] = Field(
        default=None, alias="JSONMappingParameters"
    )
    cs_vmapping_parameters: Optional[CSVMappingParametersModel] = Field(
        default=None, alias="CSVMappingParameters"
    )


class OutputDescriptionModel(BaseModel):
    output_id: Optional[str] = Field(default=None, alias="OutputId")
    name: Optional[str] = Field(default=None, alias="Name")
    kinesis_streams_output_description: Optional[
        KinesisStreamsOutputDescriptionModel
    ] = Field(default=None, alias="KinesisStreamsOutputDescription")
    kinesis_firehose_output_description: Optional[
        KinesisFirehoseOutputDescriptionModel
    ] = Field(default=None, alias="KinesisFirehoseOutputDescription")
    lambda_output_description: Optional[LambdaOutputDescriptionModel] = Field(
        default=None, alias="LambdaOutputDescription"
    )
    destination_schema: Optional[DestinationSchemaModel] = Field(
        default=None, alias="DestinationSchema"
    )


class OutputModel(BaseModel):
    name: str = Field(alias="Name")
    destination_schema: DestinationSchemaModel = Field(alias="DestinationSchema")
    kinesis_streams_output: Optional[KinesisStreamsOutputModel] = Field(
        default=None, alias="KinesisStreamsOutput"
    )
    kinesis_firehose_output: Optional[KinesisFirehoseOutputModel] = Field(
        default=None, alias="KinesisFirehoseOutput"
    )
    lambda_output: Optional[LambdaOutputModel] = Field(
        default=None, alias="LambdaOutput"
    )


class OutputUpdateModel(BaseModel):
    output_id: str = Field(alias="OutputId")
    name_update: Optional[str] = Field(default=None, alias="NameUpdate")
    kinesis_streams_output_update: Optional[KinesisStreamsOutputUpdateModel] = Field(
        default=None, alias="KinesisStreamsOutputUpdate"
    )
    kinesis_firehose_output_update: Optional[KinesisFirehoseOutputUpdateModel] = Field(
        default=None, alias="KinesisFirehoseOutputUpdate"
    )
    lambda_output_update: Optional[LambdaOutputUpdateModel] = Field(
        default=None, alias="LambdaOutputUpdate"
    )
    destination_schema_update: Optional[DestinationSchemaModel] = Field(
        default=None, alias="DestinationSchemaUpdate"
    )


class ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ApplicationCodeConfigurationDescriptionModel(BaseModel):
    code_content_type: Literal["PLAINTEXT", "ZIPFILE"] = Field(alias="CodeContentType")
    code_content_description: Optional[CodeContentDescriptionModel] = Field(
        default=None, alias="CodeContentDescription"
    )


class ApplicationCodeConfigurationModel(BaseModel):
    code_content_type: Literal["PLAINTEXT", "ZIPFILE"] = Field(alias="CodeContentType")
    code_content: Optional[CodeContentModel] = Field(default=None, alias="CodeContent")


class ApplicationCodeConfigurationUpdateModel(BaseModel):
    code_content_type_update: Optional[Literal["PLAINTEXT", "ZIPFILE"]] = Field(
        default=None, alias="CodeContentTypeUpdate"
    )
    code_content_update: Optional[CodeContentUpdateModel] = Field(
        default=None, alias="CodeContentUpdate"
    )


class ZeppelinApplicationConfigurationDescriptionModel(BaseModel):
    monitoring_configuration_description: ZeppelinMonitoringConfigurationDescriptionModel = Field(
        alias="MonitoringConfigurationDescription"
    )
    catalog_configuration_description: Optional[
        CatalogConfigurationDescriptionModel
    ] = Field(default=None, alias="CatalogConfigurationDescription")
    deploy_as_application_configuration_description: Optional[
        DeployAsApplicationConfigurationDescriptionModel
    ] = Field(default=None, alias="DeployAsApplicationConfigurationDescription")
    custom_artifacts_configuration_description: Optional[
        List[CustomArtifactConfigurationDescriptionModel]
    ] = Field(default=None, alias="CustomArtifactsConfigurationDescription")


class ZeppelinApplicationConfigurationModel(BaseModel):
    monitoring_configuration: Optional[ZeppelinMonitoringConfigurationModel] = Field(
        default=None, alias="MonitoringConfiguration"
    )
    catalog_configuration: Optional[CatalogConfigurationModel] = Field(
        default=None, alias="CatalogConfiguration"
    )
    deploy_as_application_configuration: Optional[
        DeployAsApplicationConfigurationModel
    ] = Field(default=None, alias="DeployAsApplicationConfiguration")
    custom_artifacts_configuration: Optional[
        Sequence[CustomArtifactConfigurationModel]
    ] = Field(default=None, alias="CustomArtifactsConfiguration")


class ZeppelinApplicationConfigurationUpdateModel(BaseModel):
    monitoring_configuration_update: Optional[
        ZeppelinMonitoringConfigurationUpdateModel
    ] = Field(default=None, alias="MonitoringConfigurationUpdate")
    catalog_configuration_update: Optional[CatalogConfigurationUpdateModel] = Field(
        default=None, alias="CatalogConfigurationUpdate"
    )
    deploy_as_application_configuration_update: Optional[
        DeployAsApplicationConfigurationUpdateModel
    ] = Field(default=None, alias="DeployAsApplicationConfigurationUpdate")
    custom_artifacts_configuration_update: Optional[
        Sequence[CustomArtifactConfigurationModel]
    ] = Field(default=None, alias="CustomArtifactsConfigurationUpdate")


class RunConfigurationModel(BaseModel):
    flink_run_configuration: Optional[FlinkRunConfigurationModel] = Field(
        default=None, alias="FlinkRunConfiguration"
    )
    sql_run_configurations: Optional[Sequence[SqlRunConfigurationModel]] = Field(
        default=None, alias="SqlRunConfigurations"
    )
    application_restore_configuration: Optional[
        ApplicationRestoreConfigurationModel
    ] = Field(default=None, alias="ApplicationRestoreConfiguration")


class AddApplicationInputProcessingConfigurationResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    input_id: str = Field(alias="InputId")
    input_processing_configuration_description: InputProcessingConfigurationDescriptionModel = Field(
        alias="InputProcessingConfigurationDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddApplicationInputProcessingConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    input_id: str = Field(alias="InputId")
    input_processing_configuration: InputProcessingConfigurationModel = Field(
        alias="InputProcessingConfiguration"
    )


class DiscoverInputSchemaRequestModel(BaseModel):
    service_execution_role: str = Field(alias="ServiceExecutionRole")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    input_starting_position_configuration: Optional[
        InputStartingPositionConfigurationModel
    ] = Field(default=None, alias="InputStartingPositionConfiguration")
    s3_configuration: Optional[S3ConfigurationModel] = Field(
        default=None, alias="S3Configuration"
    )
    input_processing_configuration: Optional[InputProcessingConfigurationModel] = Field(
        default=None, alias="InputProcessingConfiguration"
    )


class RecordFormatModel(BaseModel):
    record_format_type: Literal["CSV", "JSON"] = Field(alias="RecordFormatType")
    mapping_parameters: Optional[MappingParametersModel] = Field(
        default=None, alias="MappingParameters"
    )


class AddApplicationOutputResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    output_descriptions: List[OutputDescriptionModel] = Field(
        alias="OutputDescriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddApplicationOutputRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    output: OutputModel = Field(alias="Output")


class StartApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    run_configuration: Optional[RunConfigurationModel] = Field(
        default=None, alias="RunConfiguration"
    )


class InputSchemaUpdateModel(BaseModel):
    record_format_update: Optional[RecordFormatModel] = Field(
        default=None, alias="RecordFormatUpdate"
    )
    record_encoding_update: Optional[str] = Field(
        default=None, alias="RecordEncodingUpdate"
    )
    record_column_updates: Optional[Sequence[RecordColumnModel]] = Field(
        default=None, alias="RecordColumnUpdates"
    )


class SourceSchemaModel(BaseModel):
    record_format: RecordFormatModel = Field(alias="RecordFormat")
    record_columns: Sequence[RecordColumnModel] = Field(alias="RecordColumns")
    record_encoding: Optional[str] = Field(default=None, alias="RecordEncoding")


class InputUpdateModel(BaseModel):
    input_id: str = Field(alias="InputId")
    name_prefix_update: Optional[str] = Field(default=None, alias="NamePrefixUpdate")
    input_processing_configuration_update: Optional[
        InputProcessingConfigurationUpdateModel
    ] = Field(default=None, alias="InputProcessingConfigurationUpdate")
    kinesis_streams_input_update: Optional[KinesisStreamsInputUpdateModel] = Field(
        default=None, alias="KinesisStreamsInputUpdate"
    )
    kinesis_firehose_input_update: Optional[KinesisFirehoseInputUpdateModel] = Field(
        default=None, alias="KinesisFirehoseInputUpdate"
    )
    input_schema_update: Optional[InputSchemaUpdateModel] = Field(
        default=None, alias="InputSchemaUpdate"
    )
    input_parallelism_update: Optional[InputParallelismUpdateModel] = Field(
        default=None, alias="InputParallelismUpdate"
    )


class DiscoverInputSchemaResponseModel(BaseModel):
    input_schema: SourceSchemaModel = Field(alias="InputSchema")
    parsed_input_records: List[List[str]] = Field(alias="ParsedInputRecords")
    processed_input_records: List[str] = Field(alias="ProcessedInputRecords")
    raw_input_records: List[str] = Field(alias="RawInputRecords")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputDescriptionModel(BaseModel):
    input_id: Optional[str] = Field(default=None, alias="InputId")
    name_prefix: Optional[str] = Field(default=None, alias="NamePrefix")
    in_app_stream_names: Optional[List[str]] = Field(
        default=None, alias="InAppStreamNames"
    )
    input_processing_configuration_description: Optional[
        InputProcessingConfigurationDescriptionModel
    ] = Field(default=None, alias="InputProcessingConfigurationDescription")
    kinesis_streams_input_description: Optional[
        KinesisStreamsInputDescriptionModel
    ] = Field(default=None, alias="KinesisStreamsInputDescription")
    kinesis_firehose_input_description: Optional[
        KinesisFirehoseInputDescriptionModel
    ] = Field(default=None, alias="KinesisFirehoseInputDescription")
    input_schema: Optional[SourceSchemaModel] = Field(default=None, alias="InputSchema")
    input_parallelism: Optional[InputParallelismModel] = Field(
        default=None, alias="InputParallelism"
    )
    input_starting_position_configuration: Optional[
        InputStartingPositionConfigurationModel
    ] = Field(default=None, alias="InputStartingPositionConfiguration")


class InputModel(BaseModel):
    name_prefix: str = Field(alias="NamePrefix")
    input_schema: SourceSchemaModel = Field(alias="InputSchema")
    input_processing_configuration: Optional[InputProcessingConfigurationModel] = Field(
        default=None, alias="InputProcessingConfiguration"
    )
    kinesis_streams_input: Optional[KinesisStreamsInputModel] = Field(
        default=None, alias="KinesisStreamsInput"
    )
    kinesis_firehose_input: Optional[KinesisFirehoseInputModel] = Field(
        default=None, alias="KinesisFirehoseInput"
    )
    input_parallelism: Optional[InputParallelismModel] = Field(
        default=None, alias="InputParallelism"
    )


class ReferenceDataSourceDescriptionModel(BaseModel):
    reference_id: str = Field(alias="ReferenceId")
    table_name: str = Field(alias="TableName")
    s3_reference_data_source_description: S3ReferenceDataSourceDescriptionModel = Field(
        alias="S3ReferenceDataSourceDescription"
    )
    reference_schema: Optional[SourceSchemaModel] = Field(
        default=None, alias="ReferenceSchema"
    )


class ReferenceDataSourceModel(BaseModel):
    table_name: str = Field(alias="TableName")
    reference_schema: SourceSchemaModel = Field(alias="ReferenceSchema")
    s3_reference_data_source: Optional[S3ReferenceDataSourceModel] = Field(
        default=None, alias="S3ReferenceDataSource"
    )


class ReferenceDataSourceUpdateModel(BaseModel):
    reference_id: str = Field(alias="ReferenceId")
    table_name_update: Optional[str] = Field(default=None, alias="TableNameUpdate")
    s3_reference_data_source_update: Optional[S3ReferenceDataSourceUpdateModel] = Field(
        default=None, alias="S3ReferenceDataSourceUpdate"
    )
    reference_schema_update: Optional[SourceSchemaModel] = Field(
        default=None, alias="ReferenceSchemaUpdate"
    )


class AddApplicationInputResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    input_descriptions: List[InputDescriptionModel] = Field(alias="InputDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddApplicationInputRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    input: InputModel = Field(alias="Input")


class AddApplicationReferenceDataSourceResponseModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_version_id: int = Field(alias="ApplicationVersionId")
    reference_data_source_descriptions: List[
        ReferenceDataSourceDescriptionModel
    ] = Field(alias="ReferenceDataSourceDescriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SqlApplicationConfigurationDescriptionModel(BaseModel):
    input_descriptions: Optional[List[InputDescriptionModel]] = Field(
        default=None, alias="InputDescriptions"
    )
    output_descriptions: Optional[List[OutputDescriptionModel]] = Field(
        default=None, alias="OutputDescriptions"
    )
    reference_data_source_descriptions: Optional[
        List[ReferenceDataSourceDescriptionModel]
    ] = Field(default=None, alias="ReferenceDataSourceDescriptions")


class AddApplicationReferenceDataSourceRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    reference_data_source: ReferenceDataSourceModel = Field(alias="ReferenceDataSource")


class SqlApplicationConfigurationModel(BaseModel):
    inputs: Optional[Sequence[InputModel]] = Field(default=None, alias="Inputs")
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="Outputs")
    reference_data_sources: Optional[Sequence[ReferenceDataSourceModel]] = Field(
        default=None, alias="ReferenceDataSources"
    )


class SqlApplicationConfigurationUpdateModel(BaseModel):
    input_updates: Optional[Sequence[InputUpdateModel]] = Field(
        default=None, alias="InputUpdates"
    )
    output_updates: Optional[Sequence[OutputUpdateModel]] = Field(
        default=None, alias="OutputUpdates"
    )
    reference_data_source_updates: Optional[
        Sequence[ReferenceDataSourceUpdateModel]
    ] = Field(default=None, alias="ReferenceDataSourceUpdates")


class ApplicationConfigurationDescriptionModel(BaseModel):
    sql_application_configuration_description: Optional[
        SqlApplicationConfigurationDescriptionModel
    ] = Field(default=None, alias="SqlApplicationConfigurationDescription")
    application_code_configuration_description: Optional[
        ApplicationCodeConfigurationDescriptionModel
    ] = Field(default=None, alias="ApplicationCodeConfigurationDescription")
    run_configuration_description: Optional[RunConfigurationDescriptionModel] = Field(
        default=None, alias="RunConfigurationDescription"
    )
    flink_application_configuration_description: Optional[
        FlinkApplicationConfigurationDescriptionModel
    ] = Field(default=None, alias="FlinkApplicationConfigurationDescription")
    environment_property_descriptions: Optional[
        EnvironmentPropertyDescriptionsModel
    ] = Field(default=None, alias="EnvironmentPropertyDescriptions")
    application_snapshot_configuration_description: Optional[
        ApplicationSnapshotConfigurationDescriptionModel
    ] = Field(default=None, alias="ApplicationSnapshotConfigurationDescription")
    vpc_configuration_descriptions: Optional[
        List[VpcConfigurationDescriptionModel]
    ] = Field(default=None, alias="VpcConfigurationDescriptions")
    zeppelin_application_configuration_description: Optional[
        ZeppelinApplicationConfigurationDescriptionModel
    ] = Field(default=None, alias="ZeppelinApplicationConfigurationDescription")


class ApplicationConfigurationModel(BaseModel):
    sql_application_configuration: Optional[SqlApplicationConfigurationModel] = Field(
        default=None, alias="SqlApplicationConfiguration"
    )
    flink_application_configuration: Optional[
        FlinkApplicationConfigurationModel
    ] = Field(default=None, alias="FlinkApplicationConfiguration")
    environment_properties: Optional[EnvironmentPropertiesModel] = Field(
        default=None, alias="EnvironmentProperties"
    )
    application_code_configuration: Optional[ApplicationCodeConfigurationModel] = Field(
        default=None, alias="ApplicationCodeConfiguration"
    )
    application_snapshot_configuration: Optional[
        ApplicationSnapshotConfigurationModel
    ] = Field(default=None, alias="ApplicationSnapshotConfiguration")
    vpc_configurations: Optional[Sequence[VpcConfigurationModel]] = Field(
        default=None, alias="VpcConfigurations"
    )
    zeppelin_application_configuration: Optional[
        ZeppelinApplicationConfigurationModel
    ] = Field(default=None, alias="ZeppelinApplicationConfiguration")


class ApplicationConfigurationUpdateModel(BaseModel):
    sql_application_configuration_update: Optional[
        SqlApplicationConfigurationUpdateModel
    ] = Field(default=None, alias="SqlApplicationConfigurationUpdate")
    application_code_configuration_update: Optional[
        ApplicationCodeConfigurationUpdateModel
    ] = Field(default=None, alias="ApplicationCodeConfigurationUpdate")
    flink_application_configuration_update: Optional[
        FlinkApplicationConfigurationUpdateModel
    ] = Field(default=None, alias="FlinkApplicationConfigurationUpdate")
    environment_property_updates: Optional[EnvironmentPropertyUpdatesModel] = Field(
        default=None, alias="EnvironmentPropertyUpdates"
    )
    application_snapshot_configuration_update: Optional[
        ApplicationSnapshotConfigurationUpdateModel
    ] = Field(default=None, alias="ApplicationSnapshotConfigurationUpdate")
    vpc_configuration_updates: Optional[Sequence[VpcConfigurationUpdateModel]] = Field(
        default=None, alias="VpcConfigurationUpdates"
    )
    zeppelin_application_configuration_update: Optional[
        ZeppelinApplicationConfigurationUpdateModel
    ] = Field(default=None, alias="ZeppelinApplicationConfigurationUpdate")


class ApplicationDetailModel(BaseModel):
    application_arn: str = Field(alias="ApplicationARN")
    application_name: str = Field(alias="ApplicationName")
    runtime_environment: Literal[
        "FLINK-1_11",
        "FLINK-1_13",
        "FLINK-1_15",
        "FLINK-1_6",
        "FLINK-1_8",
        "SQL-1_0",
        "ZEPPELIN-FLINK-1_0",
        "ZEPPELIN-FLINK-2_0",
    ] = Field(alias="RuntimeEnvironment")
    application_status: Literal[
        "AUTOSCALING",
        "DELETING",
        "FORCE_STOPPING",
        "MAINTENANCE",
        "READY",
        "ROLLED_BACK",
        "ROLLING_BACK",
        "RUNNING",
        "STARTING",
        "STOPPING",
        "UPDATING",
    ] = Field(alias="ApplicationStatus")
    application_version_id: int = Field(alias="ApplicationVersionId")
    application_description: Optional[str] = Field(
        default=None, alias="ApplicationDescription"
    )
    service_execution_role: Optional[str] = Field(
        default=None, alias="ServiceExecutionRole"
    )
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )
    application_configuration_description: Optional[
        ApplicationConfigurationDescriptionModel
    ] = Field(default=None, alias="ApplicationConfigurationDescription")
    cloud_watch_logging_option_descriptions: Optional[
        List[CloudWatchLoggingOptionDescriptionModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptionDescriptions")
    application_maintenance_configuration_description: Optional[
        ApplicationMaintenanceConfigurationDescriptionModel
    ] = Field(default=None, alias="ApplicationMaintenanceConfigurationDescription")
    application_version_updated_from: Optional[int] = Field(
        default=None, alias="ApplicationVersionUpdatedFrom"
    )
    application_version_rolled_back_from: Optional[int] = Field(
        default=None, alias="ApplicationVersionRolledBackFrom"
    )
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")
    application_version_rolled_back_to: Optional[int] = Field(
        default=None, alias="ApplicationVersionRolledBackTo"
    )
    application_mode: Optional[Literal["INTERACTIVE", "STREAMING"]] = Field(
        default=None, alias="ApplicationMode"
    )


class CreateApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    runtime_environment: Literal[
        "FLINK-1_11",
        "FLINK-1_13",
        "FLINK-1_15",
        "FLINK-1_6",
        "FLINK-1_8",
        "SQL-1_0",
        "ZEPPELIN-FLINK-1_0",
        "ZEPPELIN-FLINK-2_0",
    ] = Field(alias="RuntimeEnvironment")
    service_execution_role: str = Field(alias="ServiceExecutionRole")
    application_description: Optional[str] = Field(
        default=None, alias="ApplicationDescription"
    )
    application_configuration: Optional[ApplicationConfigurationModel] = Field(
        default=None, alias="ApplicationConfiguration"
    )
    cloud_watch_logging_options: Optional[
        Sequence[CloudWatchLoggingOptionModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptions")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    application_mode: Optional[Literal["INTERACTIVE", "STREAMING"]] = Field(
        default=None, alias="ApplicationMode"
    )


class UpdateApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: Optional[int] = Field(
        default=None, alias="CurrentApplicationVersionId"
    )
    application_configuration_update: Optional[
        ApplicationConfigurationUpdateModel
    ] = Field(default=None, alias="ApplicationConfigurationUpdate")
    service_execution_role_update: Optional[str] = Field(
        default=None, alias="ServiceExecutionRoleUpdate"
    )
    run_configuration_update: Optional[RunConfigurationUpdateModel] = Field(
        default=None, alias="RunConfigurationUpdate"
    )
    cloud_watch_logging_option_updates: Optional[
        Sequence[CloudWatchLoggingOptionUpdateModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptionUpdates")
    conditional_token: Optional[str] = Field(default=None, alias="ConditionalToken")


class CreateApplicationResponseModel(BaseModel):
    application_detail: ApplicationDetailModel = Field(alias="ApplicationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationResponseModel(BaseModel):
    application_detail: ApplicationDetailModel = Field(alias="ApplicationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationVersionResponseModel(BaseModel):
    application_version_detail: ApplicationDetailModel = Field(
        alias="ApplicationVersionDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackApplicationResponseModel(BaseModel):
    application_detail: ApplicationDetailModel = Field(alias="ApplicationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application_detail: ApplicationDetailModel = Field(alias="ApplicationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
