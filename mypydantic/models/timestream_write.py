# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchLoadProgressReportModel(BaseModel):
    records_processed: Optional[int] = Field(default=None, alias="RecordsProcessed")
    records_ingested: Optional[int] = Field(default=None, alias="RecordsIngested")
    parse_failures: Optional[int] = Field(default=None, alias="ParseFailures")
    record_ingestion_failures: Optional[int] = Field(
        default=None, alias="RecordIngestionFailures"
    )
    file_failures: Optional[int] = Field(default=None, alias="FileFailures")
    bytes_metered: Optional[int] = Field(default=None, alias="BytesMetered")


class BatchLoadTaskModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="TaskId")
    task_status: Optional[
        Literal[
            "CREATED",
            "FAILED",
            "IN_PROGRESS",
            "PENDING_RESUME",
            "PROGRESS_STOPPED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="TaskStatus")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    resumable_until: Optional[datetime] = Field(default=None, alias="ResumableUntil")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DatabaseModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_count: Optional[int] = Field(default=None, alias="TableCount")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class RetentionPropertiesModel(BaseModel):
    memory_store_retention_period_in_hours: int = Field(
        alias="MemoryStoreRetentionPeriodInHours"
    )
    magnetic_store_retention_period_in_days: int = Field(
        alias="MagneticStoreRetentionPeriodInDays"
    )


class CsvConfigurationModel(BaseModel):
    column_separator: Optional[str] = Field(default=None, alias="ColumnSeparator")
    escape_char: Optional[str] = Field(default=None, alias="EscapeChar")
    quote_char: Optional[str] = Field(default=None, alias="QuoteChar")
    null_value: Optional[str] = Field(default=None, alias="NullValue")
    trim_white_space: Optional[bool] = Field(default=None, alias="TrimWhiteSpace")


class DataModelS3ConfigurationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    object_key: Optional[str] = Field(default=None, alias="ObjectKey")


class DimensionMappingModel(BaseModel):
    source_column: Optional[str] = Field(default=None, alias="SourceColumn")
    destination_column: Optional[str] = Field(default=None, alias="DestinationColumn")


class DataSourceS3ConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    object_key_prefix: Optional[str] = Field(default=None, alias="ObjectKeyPrefix")


class DeleteDatabaseRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")


class DeleteTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")


class DescribeBatchLoadTaskRequestModel(BaseModel):
    task_id: str = Field(alias="TaskId")


class DescribeDatabaseRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")


class EndpointModel(BaseModel):
    address: str = Field(alias="Address")
    cache_period_in_minutes: int = Field(alias="CachePeriodInMinutes")


class DescribeTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")


class DimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    dimension_value_type: Optional[Literal["VARCHAR"]] = Field(
        default=None, alias="DimensionValueType"
    )


class ListBatchLoadTasksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    task_status: Optional[
        Literal[
            "CREATED",
            "FAILED",
            "IN_PROGRESS",
            "PENDING_RESUME",
            "PROGRESS_STOPPED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="TaskStatus")


class ListDatabasesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTablesRequestModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class S3ConfigurationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    object_key_prefix: Optional[str] = Field(default=None, alias="ObjectKeyPrefix")
    encryption_option: Optional[Literal["SSE_KMS", "SSE_S3"]] = Field(
        default=None, alias="EncryptionOption"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class MeasureValueModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    type: Literal[
        "BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "TIMESTAMP", "VARCHAR"
    ] = Field(alias="Type")


class MultiMeasureAttributeMappingModel(BaseModel):
    source_column: str = Field(alias="SourceColumn")
    target_multi_measure_attribute_name: Optional[str] = Field(
        default=None, alias="TargetMultiMeasureAttributeName"
    )
    measure_value_type: Optional[
        Literal["BIGINT", "BOOLEAN", "DOUBLE", "TIMESTAMP", "VARCHAR"]
    ] = Field(default=None, alias="MeasureValueType")


class RecordsIngestedModel(BaseModel):
    total: Optional[int] = Field(default=None, alias="Total")
    memory_store: Optional[int] = Field(default=None, alias="MemoryStore")
    magnetic_store: Optional[int] = Field(default=None, alias="MagneticStore")


class ReportS3ConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    object_key_prefix: Optional[str] = Field(default=None, alias="ObjectKeyPrefix")
    encryption_option: Optional[Literal["SSE_KMS", "SSE_S3"]] = Field(
        default=None, alias="EncryptionOption"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ResumeBatchLoadTaskRequestModel(BaseModel):
    task_id: str = Field(alias="TaskId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDatabaseRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    kms_key_id: str = Field(alias="KmsKeyId")


class CreateBatchLoadTaskResponseModel(BaseModel):
    task_id: str = Field(alias="TaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBatchLoadTasksResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    batch_load_tasks: List[BatchLoadTaskModel] = Field(alias="BatchLoadTasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatabaseRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateDatabaseResponseModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatabaseResponseModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatabasesResponseModel(BaseModel):
    databases: List[DatabaseModel] = Field(alias="Databases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatabaseResponseModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSourceConfigurationModel(BaseModel):
    data_source_s3_configuration: DataSourceS3ConfigurationModel = Field(
        alias="DataSourceS3Configuration"
    )
    data_format: Literal["CSV"] = Field(alias="DataFormat")
    csv_configuration: Optional[CsvConfigurationModel] = Field(
        default=None, alias="CsvConfiguration"
    )


class DescribeEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MagneticStoreRejectedDataLocationModel(BaseModel):
    s3_configuration: Optional[S3ConfigurationModel] = Field(
        default=None, alias="S3Configuration"
    )


class RecordModel(BaseModel):
    dimensions: Optional[Sequence[DimensionModel]] = Field(
        default=None, alias="Dimensions"
    )
    measure_name: Optional[str] = Field(default=None, alias="MeasureName")
    measure_value: Optional[str] = Field(default=None, alias="MeasureValue")
    measure_value_type: Optional[
        Literal["BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "TIMESTAMP", "VARCHAR"]
    ] = Field(default=None, alias="MeasureValueType")
    time: Optional[str] = Field(default=None, alias="Time")
    time_unit: Optional[
        Literal["MICROSECONDS", "MILLISECONDS", "NANOSECONDS", "SECONDS"]
    ] = Field(default=None, alias="TimeUnit")
    version: Optional[int] = Field(default=None, alias="Version")
    measure_values: Optional[Sequence[MeasureValueModel]] = Field(
        default=None, alias="MeasureValues"
    )


class MixedMeasureMappingModel(BaseModel):
    measure_value_type: Literal[
        "BIGINT", "BOOLEAN", "DOUBLE", "MULTI", "TIMESTAMP", "VARCHAR"
    ] = Field(alias="MeasureValueType")
    measure_name: Optional[str] = Field(default=None, alias="MeasureName")
    source_column: Optional[str] = Field(default=None, alias="SourceColumn")
    target_measure_name: Optional[str] = Field(default=None, alias="TargetMeasureName")
    multi_measure_attribute_mappings: Optional[
        Sequence[MultiMeasureAttributeMappingModel]
    ] = Field(default=None, alias="MultiMeasureAttributeMappings")


class MultiMeasureMappingsModel(BaseModel):
    multi_measure_attribute_mappings: Sequence[
        MultiMeasureAttributeMappingModel
    ] = Field(alias="MultiMeasureAttributeMappings")
    target_multi_measure_name: Optional[str] = Field(
        default=None, alias="TargetMultiMeasureName"
    )


class WriteRecordsResponseModel(BaseModel):
    records_ingested: RecordsIngestedModel = Field(alias="RecordsIngested")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReportConfigurationModel(BaseModel):
    report_s3_configuration: Optional[ReportS3ConfigurationModel] = Field(
        default=None, alias="ReportS3Configuration"
    )


class MagneticStoreWritePropertiesModel(BaseModel):
    enable_magnetic_store_writes: bool = Field(alias="EnableMagneticStoreWrites")
    magnetic_store_rejected_data_location: Optional[
        MagneticStoreRejectedDataLocationModel
    ] = Field(default=None, alias="MagneticStoreRejectedDataLocation")


class WriteRecordsRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    records: Sequence[RecordModel] = Field(alias="Records")
    common_attributes: Optional[RecordModel] = Field(
        default=None, alias="CommonAttributes"
    )


class DataModelModel(BaseModel):
    dimension_mappings: Sequence[DimensionMappingModel] = Field(
        alias="DimensionMappings"
    )
    time_column: Optional[str] = Field(default=None, alias="TimeColumn")
    time_unit: Optional[
        Literal["MICROSECONDS", "MILLISECONDS", "NANOSECONDS", "SECONDS"]
    ] = Field(default=None, alias="TimeUnit")
    multi_measure_mappings: Optional[MultiMeasureMappingsModel] = Field(
        default=None, alias="MultiMeasureMappings"
    )
    mixed_measure_mappings: Optional[Sequence[MixedMeasureMappingModel]] = Field(
        default=None, alias="MixedMeasureMappings"
    )
    measure_name_column: Optional[str] = Field(default=None, alias="MeasureNameColumn")


class CreateTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    retention_properties: Optional[RetentionPropertiesModel] = Field(
        default=None, alias="RetentionProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    magnetic_store_write_properties: Optional[
        MagneticStoreWritePropertiesModel
    ] = Field(default=None, alias="MagneticStoreWriteProperties")


class TableModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_status: Optional[Literal["ACTIVE", "DELETING", "RESTORING"]] = Field(
        default=None, alias="TableStatus"
    )
    retention_properties: Optional[RetentionPropertiesModel] = Field(
        default=None, alias="RetentionProperties"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    magnetic_store_write_properties: Optional[
        MagneticStoreWritePropertiesModel
    ] = Field(default=None, alias="MagneticStoreWriteProperties")


class UpdateTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    retention_properties: Optional[RetentionPropertiesModel] = Field(
        default=None, alias="RetentionProperties"
    )
    magnetic_store_write_properties: Optional[
        MagneticStoreWritePropertiesModel
    ] = Field(default=None, alias="MagneticStoreWriteProperties")


class DataModelConfigurationModel(BaseModel):
    data_model: Optional[DataModelModel] = Field(default=None, alias="DataModel")
    data_model_s3_configuration: Optional[DataModelS3ConfigurationModel] = Field(
        default=None, alias="DataModelS3Configuration"
    )


class CreateTableResponseModel(BaseModel):
    table: TableModel = Field(alias="Table")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableResponseModel(BaseModel):
    table: TableModel = Field(alias="Table")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTablesResponseModel(BaseModel):
    tables: List[TableModel] = Field(alias="Tables")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableResponseModel(BaseModel):
    table: TableModel = Field(alias="Table")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchLoadTaskDescriptionModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="TaskId")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    data_source_configuration: Optional[DataSourceConfigurationModel] = Field(
        default=None, alias="DataSourceConfiguration"
    )
    progress_report: Optional[BatchLoadProgressReportModel] = Field(
        default=None, alias="ProgressReport"
    )
    report_configuration: Optional[ReportConfigurationModel] = Field(
        default=None, alias="ReportConfiguration"
    )
    data_model_configuration: Optional[DataModelConfigurationModel] = Field(
        default=None, alias="DataModelConfiguration"
    )
    target_database_name: Optional[str] = Field(
        default=None, alias="TargetDatabaseName"
    )
    target_table_name: Optional[str] = Field(default=None, alias="TargetTableName")
    task_status: Optional[
        Literal[
            "CREATED",
            "FAILED",
            "IN_PROGRESS",
            "PENDING_RESUME",
            "PROGRESS_STOPPED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="TaskStatus")
    record_version: Optional[int] = Field(default=None, alias="RecordVersion")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    resumable_until: Optional[datetime] = Field(default=None, alias="ResumableUntil")


class CreateBatchLoadTaskRequestModel(BaseModel):
    data_source_configuration: DataSourceConfigurationModel = Field(
        alias="DataSourceConfiguration"
    )
    report_configuration: ReportConfigurationModel = Field(alias="ReportConfiguration")
    target_database_name: str = Field(alias="TargetDatabaseName")
    target_table_name: str = Field(alias="TargetTableName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    data_model_configuration: Optional[DataModelConfigurationModel] = Field(
        default=None, alias="DataModelConfiguration"
    )
    record_version: Optional[int] = Field(default=None, alias="RecordVersion")


class DescribeBatchLoadTaskResponseModel(BaseModel):
    batch_load_task_description: BatchLoadTaskDescriptionModel = Field(
        alias="BatchLoadTaskDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
