# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateCliTokenRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class NetworkConfigurationModel(BaseModel):
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class CreateWebLoginTokenRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class GetEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class UpdateErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEnvironmentsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ModuleLoggingConfigurationInputModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    log_level: Literal["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"] = Field(
        alias="LogLevel"
    )


class ModuleLoggingConfigurationModel(BaseModel):
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupArn"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    log_level: Optional[
        Literal["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"]
    ] = Field(default=None, alias="LogLevel")


class StatisticSetModel(BaseModel):
    maximum: Optional[float] = Field(default=None, alias="Maximum")
    minimum: Optional[float] = Field(default=None, alias="Minimum")
    sample_count: Optional[int] = Field(default=None, alias="SampleCount")
    sum: Optional[float] = Field(default=None, alias="Sum")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateNetworkConfigurationInputModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")


class CreateCliTokenResponseModel(BaseModel):
    cli_token: str = Field(alias="CliToken")
    web_server_hostname: str = Field(alias="WebServerHostname")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWebLoginTokenResponseModel(BaseModel):
    web_server_hostname: str = Field(alias="WebServerHostname")
    web_token: str = Field(alias="WebToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsOutputModel(BaseModel):
    environments: List[str] = Field(alias="Environments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LastUpdateModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    error: Optional[UpdateErrorModel] = Field(default=None, alias="Error")
    source: Optional[str] = Field(default=None, alias="Source")
    status: Optional[Literal["FAILED", "PENDING", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class ListEnvironmentsInputListEnvironmentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LoggingConfigurationInputModel(BaseModel):
    dag_processing_logs: Optional[ModuleLoggingConfigurationInputModel] = Field(
        default=None, alias="DagProcessingLogs"
    )
    scheduler_logs: Optional[ModuleLoggingConfigurationInputModel] = Field(
        default=None, alias="SchedulerLogs"
    )
    task_logs: Optional[ModuleLoggingConfigurationInputModel] = Field(
        default=None, alias="TaskLogs"
    )
    webserver_logs: Optional[ModuleLoggingConfigurationInputModel] = Field(
        default=None, alias="WebserverLogs"
    )
    worker_logs: Optional[ModuleLoggingConfigurationInputModel] = Field(
        default=None, alias="WorkerLogs"
    )


class LoggingConfigurationModel(BaseModel):
    dag_processing_logs: Optional[ModuleLoggingConfigurationModel] = Field(
        default=None, alias="DagProcessingLogs"
    )
    scheduler_logs: Optional[ModuleLoggingConfigurationModel] = Field(
        default=None, alias="SchedulerLogs"
    )
    task_logs: Optional[ModuleLoggingConfigurationModel] = Field(
        default=None, alias="TaskLogs"
    )
    webserver_logs: Optional[ModuleLoggingConfigurationModel] = Field(
        default=None, alias="WebserverLogs"
    )
    worker_logs: Optional[ModuleLoggingConfigurationModel] = Field(
        default=None, alias="WorkerLogs"
    )


class MetricDatumModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    statistic_values: Optional[StatisticSetModel] = Field(
        default=None, alias="StatisticValues"
    )
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="Unit")
    value: Optional[float] = Field(default=None, alias="Value")


class CreateEnvironmentInputRequestModel(BaseModel):
    dag_s3_path: str = Field(alias="DagS3Path")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    name: str = Field(alias="Name")
    network_configuration: NetworkConfigurationModel = Field(
        alias="NetworkConfiguration"
    )
    source_bucket_arn: str = Field(alias="SourceBucketArn")
    airflow_configuration_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="AirflowConfigurationOptions"
    )
    airflow_version: Optional[str] = Field(default=None, alias="AirflowVersion")
    environment_class: Optional[str] = Field(default=None, alias="EnvironmentClass")
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")
    logging_configuration: Optional[LoggingConfigurationInputModel] = Field(
        default=None, alias="LoggingConfiguration"
    )
    max_workers: Optional[int] = Field(default=None, alias="MaxWorkers")
    min_workers: Optional[int] = Field(default=None, alias="MinWorkers")
    plugins_s3_object_version: Optional[str] = Field(
        default=None, alias="PluginsS3ObjectVersion"
    )
    plugins_s3_path: Optional[str] = Field(default=None, alias="PluginsS3Path")
    requirements_s3_object_version: Optional[str] = Field(
        default=None, alias="RequirementsS3ObjectVersion"
    )
    requirements_s3_path: Optional[str] = Field(
        default=None, alias="RequirementsS3Path"
    )
    schedulers: Optional[int] = Field(default=None, alias="Schedulers")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    webserver_access_mode: Optional[Literal["PRIVATE_ONLY", "PUBLIC_ONLY"]] = Field(
        default=None, alias="WebserverAccessMode"
    )
    weekly_maintenance_window_start: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceWindowStart"
    )


class UpdateEnvironmentInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    airflow_configuration_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="AirflowConfigurationOptions"
    )
    airflow_version: Optional[str] = Field(default=None, alias="AirflowVersion")
    dag_s3_path: Optional[str] = Field(default=None, alias="DagS3Path")
    environment_class: Optional[str] = Field(default=None, alias="EnvironmentClass")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    logging_configuration: Optional[LoggingConfigurationInputModel] = Field(
        default=None, alias="LoggingConfiguration"
    )
    max_workers: Optional[int] = Field(default=None, alias="MaxWorkers")
    min_workers: Optional[int] = Field(default=None, alias="MinWorkers")
    network_configuration: Optional[UpdateNetworkConfigurationInputModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    plugins_s3_object_version: Optional[str] = Field(
        default=None, alias="PluginsS3ObjectVersion"
    )
    plugins_s3_path: Optional[str] = Field(default=None, alias="PluginsS3Path")
    requirements_s3_object_version: Optional[str] = Field(
        default=None, alias="RequirementsS3ObjectVersion"
    )
    requirements_s3_path: Optional[str] = Field(
        default=None, alias="RequirementsS3Path"
    )
    schedulers: Optional[int] = Field(default=None, alias="Schedulers")
    source_bucket_arn: Optional[str] = Field(default=None, alias="SourceBucketArn")
    webserver_access_mode: Optional[Literal["PRIVATE_ONLY", "PUBLIC_ONLY"]] = Field(
        default=None, alias="WebserverAccessMode"
    )
    weekly_maintenance_window_start: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceWindowStart"
    )


class EnvironmentModel(BaseModel):
    airflow_configuration_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AirflowConfigurationOptions"
    )
    airflow_version: Optional[str] = Field(default=None, alias="AirflowVersion")
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    dag_s3_path: Optional[str] = Field(default=None, alias="DagS3Path")
    environment_class: Optional[str] = Field(default=None, alias="EnvironmentClass")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")
    last_update: Optional[LastUpdateModel] = Field(default=None, alias="LastUpdate")
    logging_configuration: Optional[LoggingConfigurationModel] = Field(
        default=None, alias="LoggingConfiguration"
    )
    max_workers: Optional[int] = Field(default=None, alias="MaxWorkers")
    min_workers: Optional[int] = Field(default=None, alias="MinWorkers")
    name: Optional[str] = Field(default=None, alias="Name")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    plugins_s3_object_version: Optional[str] = Field(
        default=None, alias="PluginsS3ObjectVersion"
    )
    plugins_s3_path: Optional[str] = Field(default=None, alias="PluginsS3Path")
    requirements_s3_object_version: Optional[str] = Field(
        default=None, alias="RequirementsS3ObjectVersion"
    )
    requirements_s3_path: Optional[str] = Field(
        default=None, alias="RequirementsS3Path"
    )
    schedulers: Optional[int] = Field(default=None, alias="Schedulers")
    service_role_arn: Optional[str] = Field(default=None, alias="ServiceRoleArn")
    source_bucket_arn: Optional[str] = Field(default=None, alias="SourceBucketArn")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "UNAVAILABLE",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    webserver_access_mode: Optional[Literal["PRIVATE_ONLY", "PUBLIC_ONLY"]] = Field(
        default=None, alias="WebserverAccessMode"
    )
    webserver_url: Optional[str] = Field(default=None, alias="WebserverUrl")
    weekly_maintenance_window_start: Optional[str] = Field(
        default=None, alias="WeeklyMaintenanceWindowStart"
    )


class PublishMetricsInputRequestModel(BaseModel):
    environment_name: str = Field(alias="EnvironmentName")
    metric_data: Sequence[MetricDatumModel] = Field(alias="MetricData")


class GetEnvironmentOutputModel(BaseModel):
    environment: EnvironmentModel = Field(alias="Environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
