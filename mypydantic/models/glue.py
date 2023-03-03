# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class NotificationPropertyModel(BaseModel):
    notify_delay_after: Optional[int] = Field(default=None, alias="NotifyDelayAfter")


class AggregateOperationModel(BaseModel):
    column: List[str] = Field(alias="Column")
    agg_func: Literal[
        "avg",
        "count",
        "countDistinct",
        "first",
        "kurtosis",
        "last",
        "max",
        "min",
        "skewness",
        "stddev_pop",
        "stddev_samp",
        "sum",
        "sumDistinct",
        "var_pop",
        "var_samp",
    ] = Field(alias="AggFunc")


class ApplyMappingModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    mapping: List[MappingModel] = Field(alias="Mapping")


class AuditContextModel(BaseModel):
    additional_audit_context: Optional[str] = Field(
        default=None, alias="AdditionalAuditContext"
    )
    requested_columns: Optional[Sequence[str]] = Field(
        default=None, alias="RequestedColumns"
    )
    all_columns_requested: Optional[bool] = Field(
        default=None, alias="AllColumnsRequested"
    )


class PartitionValueListModel(BaseModel):
    values: Sequence[str] = Field(alias="Values")


class BasicCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDeleteConnectionRequestModel(BaseModel):
    connection_name_list: Sequence[str] = Field(alias="ConnectionNameList")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class ErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchDeleteTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    tables_to_delete: Sequence[str] = Field(alias="TablesToDelete")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class BatchDeleteTableVersionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    version_ids: Sequence[str] = Field(alias="VersionIds")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchGetBlueprintsRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")
    include_blueprint: Optional[bool] = Field(default=None, alias="IncludeBlueprint")
    include_parameter_spec: Optional[bool] = Field(
        default=None, alias="IncludeParameterSpec"
    )


class BatchGetCrawlersRequestModel(BaseModel):
    crawler_names: Sequence[str] = Field(alias="CrawlerNames")


class BatchGetCustomEntityTypesRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")


class CustomEntityTypeModel(BaseModel):
    name: str = Field(alias="Name")
    regex_string: str = Field(alias="RegexString")
    context_words: Optional[List[str]] = Field(default=None, alias="ContextWords")


class BatchGetDataQualityResultRequestModel(BaseModel):
    result_ids: Sequence[str] = Field(alias="ResultIds")


class BatchGetDevEndpointsRequestModel(BaseModel):
    dev_endpoint_names: Sequence[str] = Field(alias="DevEndpointNames")


class DevEndpointModel(BaseModel):
    endpoint_name: Optional[str] = Field(default=None, alias="EndpointName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    yarn_endpoint_address: Optional[str] = Field(
        default=None, alias="YarnEndpointAddress"
    )
    private_address: Optional[str] = Field(default=None, alias="PrivateAddress")
    zeppelin_remote_spark_interpreter_port: Optional[int] = Field(
        default=None, alias="ZeppelinRemoteSparkInterpreterPort"
    )
    public_address: Optional[str] = Field(default=None, alias="PublicAddress")
    status: Optional[str] = Field(default=None, alias="Status")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    extra_python_libs_s3_path: Optional[str] = Field(
        default=None, alias="ExtraPythonLibsS3Path"
    )
    extra_jars_s3_path: Optional[str] = Field(default=None, alias="ExtraJarsS3Path")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    last_update_status: Optional[str] = Field(default=None, alias="LastUpdateStatus")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_modified_timestamp: Optional[datetime] = Field(
        default=None, alias="LastModifiedTimestamp"
    )
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    public_keys: Optional[List[str]] = Field(default=None, alias="PublicKeys")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    arguments: Optional[Dict[str, str]] = Field(default=None, alias="Arguments")


class BatchGetJobsRequestModel(BaseModel):
    job_names: Sequence[str] = Field(alias="JobNames")


class BatchGetTriggersRequestModel(BaseModel):
    trigger_names: Sequence[str] = Field(alias="TriggerNames")


class BatchGetWorkflowsRequestModel(BaseModel):
    names: Sequence[str] = Field(alias="Names")
    include_graph: Optional[bool] = Field(default=None, alias="IncludeGraph")


class BatchStopJobRunRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_run_ids: Sequence[str] = Field(alias="JobRunIds")


class BatchStopJobRunSuccessfulSubmissionModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")


class BinaryColumnStatisticsDataModel(BaseModel):
    maximum_length: int = Field(alias="MaximumLength")
    average_length: float = Field(alias="AverageLength")
    number_of_nulls: int = Field(alias="NumberOfNulls")


class BlueprintDetailsModel(BaseModel):
    blueprint_name: Optional[str] = Field(default=None, alias="BlueprintName")
    run_id: Optional[str] = Field(default=None, alias="RunId")


class BlueprintRunModel(BaseModel):
    blueprint_name: Optional[str] = Field(default=None, alias="BlueprintName")
    run_id: Optional[str] = Field(default=None, alias="RunId")
    workflow_name: Optional[str] = Field(default=None, alias="WorkflowName")
    state: Optional[Literal["FAILED", "ROLLING_BACK", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="State"
    )
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    rollback_error_message: Optional[str] = Field(
        default=None, alias="RollbackErrorMessage"
    )
    parameters: Optional[str] = Field(default=None, alias="Parameters")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class LastActiveDefinitionModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    parameter_spec: Optional[str] = Field(default=None, alias="ParameterSpec")
    blueprint_location: Optional[str] = Field(default=None, alias="BlueprintLocation")
    blueprint_service_location: Optional[str] = Field(
        default=None, alias="BlueprintServiceLocation"
    )


class BooleanColumnStatisticsDataModel(BaseModel):
    number_of_trues: int = Field(alias="NumberOfTrues")
    number_of_falses: int = Field(alias="NumberOfFalses")
    number_of_nulls: int = Field(alias="NumberOfNulls")


class CancelDataQualityRuleRecommendationRunRequestModel(BaseModel):
    run_id: str = Field(alias="RunId")


class CancelDataQualityRulesetEvaluationRunRequestModel(BaseModel):
    run_id: str = Field(alias="RunId")


class CancelMLTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    task_run_id: str = Field(alias="TaskRunId")


class CancelStatementRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    id: int = Field(alias="Id")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class CatalogEntryModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")


class CatalogImportStatusModel(BaseModel):
    import_completed: Optional[bool] = Field(default=None, alias="ImportCompleted")
    import_time: Optional[datetime] = Field(default=None, alias="ImportTime")
    imported_by: Optional[str] = Field(default=None, alias="ImportedBy")


class KafkaStreamingSourceOptionsModel(BaseModel):
    bootstrap_servers: Optional[str] = Field(default=None, alias="BootstrapServers")
    security_protocol: Optional[str] = Field(default=None, alias="SecurityProtocol")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    topic_name: Optional[str] = Field(default=None, alias="TopicName")
    assign: Optional[str] = Field(default=None, alias="Assign")
    subscribe_pattern: Optional[str] = Field(default=None, alias="SubscribePattern")
    classification: Optional[str] = Field(default=None, alias="Classification")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    starting_offsets: Optional[str] = Field(default=None, alias="StartingOffsets")
    ending_offsets: Optional[str] = Field(default=None, alias="EndingOffsets")
    poll_timeout_ms: Optional[int] = Field(default=None, alias="PollTimeoutMs")
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    retry_interval_ms: Optional[int] = Field(default=None, alias="RetryIntervalMs")
    max_offsets_per_trigger: Optional[int] = Field(
        default=None, alias="MaxOffsetsPerTrigger"
    )
    min_partitions: Optional[int] = Field(default=None, alias="MinPartitions")
    include_headers: Optional[bool] = Field(default=None, alias="IncludeHeaders")
    add_record_timestamp: Optional[str] = Field(
        default=None, alias="AddRecordTimestamp"
    )
    emit_consumer_lag_metrics: Optional[str] = Field(
        default=None, alias="EmitConsumerLagMetrics"
    )


class StreamingDataPreviewOptionsModel(BaseModel):
    polling_time: Optional[int] = Field(default=None, alias="PollingTime")
    record_polling_limit: Optional[int] = Field(
        default=None, alias="RecordPollingLimit"
    )


class KinesisStreamingSourceOptionsModel(BaseModel):
    endpoint_url: Optional[str] = Field(default=None, alias="EndpointUrl")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    classification: Optional[str] = Field(default=None, alias="Classification")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    starting_position: Optional[Literal["earliest", "latest", "trim_horizon"]] = Field(
        default=None, alias="StartingPosition"
    )
    max_fetch_time_in_ms: Optional[int] = Field(default=None, alias="MaxFetchTimeInMs")
    max_fetch_records_per_shard: Optional[int] = Field(
        default=None, alias="MaxFetchRecordsPerShard"
    )
    max_record_per_read: Optional[int] = Field(default=None, alias="MaxRecordPerRead")
    add_idle_time_between_reads: Optional[bool] = Field(
        default=None, alias="AddIdleTimeBetweenReads"
    )
    idle_time_between_reads_in_ms: Optional[int] = Field(
        default=None, alias="IdleTimeBetweenReadsInMs"
    )
    describe_shard_interval: Optional[int] = Field(
        default=None, alias="DescribeShardInterval"
    )
    num_retries: Optional[int] = Field(default=None, alias="NumRetries")
    retry_interval_ms: Optional[int] = Field(default=None, alias="RetryIntervalMs")
    max_retry_interval_ms: Optional[int] = Field(
        default=None, alias="MaxRetryIntervalMs"
    )
    avoid_empty_batches: Optional[bool] = Field(default=None, alias="AvoidEmptyBatches")
    stream_arn: Optional[str] = Field(default=None, alias="StreamArn")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    role_session_name: Optional[str] = Field(default=None, alias="RoleSessionName")
    add_record_timestamp: Optional[str] = Field(
        default=None, alias="AddRecordTimestamp"
    )
    emit_consumer_lag_metrics: Optional[str] = Field(
        default=None, alias="EmitConsumerLagMetrics"
    )


class CatalogSchemaChangePolicyModel(BaseModel):
    enable_update_catalog: Optional[bool] = Field(
        default=None, alias="EnableUpdateCatalog"
    )
    update_behavior: Optional[Literal["LOG", "UPDATE_IN_DATABASE"]] = Field(
        default=None, alias="UpdateBehavior"
    )


class CatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class CatalogTargetModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    tables: List[str] = Field(alias="Tables")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    event_queue_arn: Optional[str] = Field(default=None, alias="EventQueueArn")
    dlq_event_queue_arn: Optional[str] = Field(default=None, alias="DlqEventQueueArn")


class CheckSchemaVersionValidityInputRequestModel(BaseModel):
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    schema_definition: str = Field(alias="SchemaDefinition")


class CsvClassifierModel(BaseModel):
    name: str = Field(alias="Name")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    version: Optional[int] = Field(default=None, alias="Version")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    quote_symbol: Optional[str] = Field(default=None, alias="QuoteSymbol")
    contains_header: Optional[Literal["ABSENT", "PRESENT", "UNKNOWN"]] = Field(
        default=None, alias="ContainsHeader"
    )
    header: Optional[List[str]] = Field(default=None, alias="Header")
    disable_value_trimming: Optional[bool] = Field(
        default=None, alias="DisableValueTrimming"
    )
    allow_single_column: Optional[bool] = Field(default=None, alias="AllowSingleColumn")
    custom_datatype_configured: Optional[bool] = Field(
        default=None, alias="CustomDatatypeConfigured"
    )
    custom_datatypes: Optional[List[str]] = Field(default=None, alias="CustomDatatypes")


class GrokClassifierModel(BaseModel):
    name: str = Field(alias="Name")
    classification: str = Field(alias="Classification")
    grok_pattern: str = Field(alias="GrokPattern")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    version: Optional[int] = Field(default=None, alias="Version")
    custom_patterns: Optional[str] = Field(default=None, alias="CustomPatterns")


class JsonClassifierModel(BaseModel):
    name: str = Field(alias="Name")
    json_path: str = Field(alias="JsonPath")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    version: Optional[int] = Field(default=None, alias="Version")


class XMLClassifierModel(BaseModel):
    name: str = Field(alias="Name")
    classification: str = Field(alias="Classification")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    version: Optional[int] = Field(default=None, alias="Version")
    row_tag: Optional[str] = Field(default=None, alias="RowTag")


class CloudWatchEncryptionModel(BaseModel):
    cloud_watch_encryption_mode: Optional[Literal["DISABLED", "SSE-KMS"]] = Field(
        default=None, alias="CloudWatchEncryptionMode"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class DirectJDBCSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    connection_name: str = Field(alias="ConnectionName")
    connection_type: Literal[
        "mysql", "oracle", "postgresql", "redshift", "sqlserver"
    ] = Field(alias="ConnectionType")
    redshift_tmp_dir: Optional[str] = Field(default=None, alias="RedshiftTmpDir")


class DropDuplicatesModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    columns: Optional[List[List[str]]] = Field(default=None, alias="Columns")


class DropFieldsModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    paths: List[List[str]] = Field(alias="Paths")


class DynamoDBCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class FillMissingValuesModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    imputed_path: str = Field(alias="ImputedPath")
    filled_path: Optional[str] = Field(default=None, alias="FilledPath")


class MergeModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    source: str = Field(alias="Source")
    primary_keys: List[List[str]] = Field(alias="PrimaryKeys")


class MicrosoftSQLServerCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class MicrosoftSQLServerCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class MySQLCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class MySQLCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class OracleSQLCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class OracleSQLCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class PIIDetectionModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    pii_type: Literal["ColumnAudit", "ColumnMasking", "RowAudit", "RowMasking"] = Field(
        alias="PiiType"
    )
    entity_types_to_detect: List[str] = Field(alias="EntityTypesToDetect")
    output_column_name: Optional[str] = Field(default=None, alias="OutputColumnName")
    sample_fraction: Optional[float] = Field(default=None, alias="SampleFraction")
    threshold_fraction: Optional[float] = Field(default=None, alias="ThresholdFraction")
    mask_value: Optional[str] = Field(default=None, alias="MaskValue")


class PostgreSQLCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class PostgreSQLCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class RedshiftSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    redshift_tmp_dir: Optional[str] = Field(default=None, alias="RedshiftTmpDir")
    tmp_dir_iamrole: Optional[str] = Field(default=None, alias="TmpDirIAMRole")


class RelationalCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")


class RenameFieldModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    source_path: List[str] = Field(alias="SourcePath")
    target_path: List[str] = Field(alias="TargetPath")


class SelectFieldsModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    paths: List[List[str]] = Field(alias="Paths")


class SelectFromCollectionModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    index: int = Field(alias="Index")


class SpigotModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    path: str = Field(alias="Path")
    topk: Optional[int] = Field(default=None, alias="Topk")
    prob: Optional[float] = Field(default=None, alias="Prob")


class SplitFieldsModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    paths: List[List[str]] = Field(alias="Paths")


class UnionModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    union_type: Literal["ALL", "DISTINCT"] = Field(alias="UnionType")


class CodeGenEdgeModel(BaseModel):
    source: str = Field(alias="Source")
    target: str = Field(alias="Target")
    target_parameter: Optional[str] = Field(default=None, alias="TargetParameter")


class CodeGenNodeArgModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    param: Optional[bool] = Field(default=None, alias="Param")


class ColumnImportanceModel(BaseModel):
    column_name: Optional[str] = Field(default=None, alias="ColumnName")
    importance: Optional[float] = Field(default=None, alias="Importance")


class ColumnRowFilterModel(BaseModel):
    column_name: Optional[str] = Field(default=None, alias="ColumnName")
    row_filter_expression: Optional[str] = Field(
        default=None, alias="RowFilterExpression"
    )


class DateColumnStatisticsDataModel(BaseModel):
    number_of_nulls: int = Field(alias="NumberOfNulls")
    number_of_distinct_values: int = Field(alias="NumberOfDistinctValues")
    minimum_value: Optional[datetime] = Field(default=None, alias="MinimumValue")
    maximum_value: Optional[datetime] = Field(default=None, alias="MaximumValue")


class DoubleColumnStatisticsDataModel(BaseModel):
    number_of_nulls: int = Field(alias="NumberOfNulls")
    number_of_distinct_values: int = Field(alias="NumberOfDistinctValues")
    minimum_value: Optional[float] = Field(default=None, alias="MinimumValue")
    maximum_value: Optional[float] = Field(default=None, alias="MaximumValue")


class LongColumnStatisticsDataModel(BaseModel):
    number_of_nulls: int = Field(alias="NumberOfNulls")
    number_of_distinct_values: int = Field(alias="NumberOfDistinctValues")
    minimum_value: Optional[int] = Field(default=None, alias="MinimumValue")
    maximum_value: Optional[int] = Field(default=None, alias="MaximumValue")


class StringColumnStatisticsDataModel(BaseModel):
    maximum_length: int = Field(alias="MaximumLength")
    average_length: float = Field(alias="AverageLength")
    number_of_nulls: int = Field(alias="NumberOfNulls")
    number_of_distinct_values: int = Field(alias="NumberOfDistinctValues")


class ColumnModel(BaseModel):
    name: str = Field(alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    comment: Optional[str] = Field(default=None, alias="Comment")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class ConditionModel(BaseModel):
    logical_operator: Optional[Literal["EQUALS"]] = Field(
        default=None, alias="LogicalOperator"
    )
    job_name: Optional[str] = Field(default=None, alias="JobName")
    state: Optional[
        Literal[
            "ERROR",
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
            "WAITING",
        ]
    ] = Field(default=None, alias="State")
    crawler_name: Optional[str] = Field(default=None, alias="CrawlerName")
    crawl_state: Optional[
        Literal["CANCELLED", "CANCELLING", "ERROR", "FAILED", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="CrawlState")


class ConfusionMatrixModel(BaseModel):
    num_true_positives: Optional[int] = Field(default=None, alias="NumTruePositives")
    num_false_positives: Optional[int] = Field(default=None, alias="NumFalsePositives")
    num_true_negatives: Optional[int] = Field(default=None, alias="NumTrueNegatives")
    num_false_negatives: Optional[int] = Field(default=None, alias="NumFalseNegatives")


class PhysicalConnectionRequirementsModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    security_group_id_list: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIdList"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")


class ConnectionPasswordEncryptionModel(BaseModel):
    return_connection_password_encrypted: bool = Field(
        alias="ReturnConnectionPasswordEncrypted"
    )
    aws_kms_key_id: Optional[str] = Field(default=None, alias="AwsKmsKeyId")


class ConnectionsListModel(BaseModel):
    connections: Optional[List[str]] = Field(default=None, alias="Connections")


class CrawlModel(BaseModel):
    state: Optional[
        Literal["CANCELLED", "CANCELLING", "ERROR", "FAILED", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="State")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")
    log_stream: Optional[str] = Field(default=None, alias="LogStream")


class CrawlerHistoryModel(BaseModel):
    crawl_id: Optional[str] = Field(default=None, alias="CrawlId")
    state: Optional[Literal["COMPLETED", "FAILED", "RUNNING", "STOPPED"]] = Field(
        default=None, alias="State"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    summary: Optional[str] = Field(default=None, alias="Summary")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")
    log_stream: Optional[str] = Field(default=None, alias="LogStream")
    message_prefix: Optional[str] = Field(default=None, alias="MessagePrefix")
    dp_uhour: Optional[float] = Field(default=None, alias="DPUHour")


class CrawlerMetricsModel(BaseModel):
    crawler_name: Optional[str] = Field(default=None, alias="CrawlerName")
    time_left_seconds: Optional[float] = Field(default=None, alias="TimeLeftSeconds")
    still_estimating: Optional[bool] = Field(default=None, alias="StillEstimating")
    last_runtime_seconds: Optional[float] = Field(
        default=None, alias="LastRuntimeSeconds"
    )
    median_runtime_seconds: Optional[float] = Field(
        default=None, alias="MedianRuntimeSeconds"
    )
    tables_created: Optional[int] = Field(default=None, alias="TablesCreated")
    tables_updated: Optional[int] = Field(default=None, alias="TablesUpdated")
    tables_deleted: Optional[int] = Field(default=None, alias="TablesDeleted")


class DeltaTargetModel(BaseModel):
    delta_tables: Optional[List[str]] = Field(default=None, alias="DeltaTables")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    write_manifest: Optional[bool] = Field(default=None, alias="WriteManifest")
    create_native_delta_table: Optional[bool] = Field(
        default=None, alias="CreateNativeDeltaTable"
    )


class DynamoDBTargetModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    scan_all: Optional[bool] = Field(default=None, alias="scanAll")
    scan_rate: Optional[float] = Field(default=None, alias="scanRate")


class JdbcTargetModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    path: Optional[str] = Field(default=None, alias="Path")
    exclusions: Optional[List[str]] = Field(default=None, alias="Exclusions")
    enable_additional_metadata: Optional[List[Literal["COMMENTS", "RAWTYPES"]]] = Field(
        default=None, alias="EnableAdditionalMetadata"
    )


class MongoDBTargetModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    path: Optional[str] = Field(default=None, alias="Path")
    scan_all: Optional[bool] = Field(default=None, alias="ScanAll")


class S3TargetModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    exclusions: Optional[List[str]] = Field(default=None, alias="Exclusions")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    sample_size: Optional[int] = Field(default=None, alias="SampleSize")
    event_queue_arn: Optional[str] = Field(default=None, alias="EventQueueArn")
    dlq_event_queue_arn: Optional[str] = Field(default=None, alias="DlqEventQueueArn")


class LakeFormationConfigurationModel(BaseModel):
    use_lake_formation_credentials: Optional[bool] = Field(
        default=None, alias="UseLakeFormationCredentials"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class LastCrawlInfoModel(BaseModel):
    status: Optional[Literal["CANCELLED", "FAILED", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    log_group: Optional[str] = Field(default=None, alias="LogGroup")
    log_stream: Optional[str] = Field(default=None, alias="LogStream")
    message_prefix: Optional[str] = Field(default=None, alias="MessagePrefix")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")


class LineageConfigurationModel(BaseModel):
    crawler_lineage_settings: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="CrawlerLineageSettings"
    )


class RecrawlPolicyModel(BaseModel):
    recrawl_behavior: Optional[
        Literal["CRAWL_EVENT_MODE", "CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
    ] = Field(default=None, alias="RecrawlBehavior")


class ScheduleModel(BaseModel):
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    state: Optional[Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]] = Field(
        default=None, alias="State"
    )


class SchemaChangePolicyModel(BaseModel):
    update_behavior: Optional[Literal["LOG", "UPDATE_IN_DATABASE"]] = Field(
        default=None, alias="UpdateBehavior"
    )
    delete_behavior: Optional[
        Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
    ] = Field(default=None, alias="DeleteBehavior")


class CrawlsFilterModel(BaseModel):
    field_name: Optional[
        Literal["CRAWL_ID", "DPU_HOUR", "END_TIME", "START_TIME", "STATE"]
    ] = Field(default=None, alias="FieldName")
    filter_operator: Optional[Literal["EQ", "GE", "GT", "LE", "LT", "NE"]] = Field(
        default=None, alias="FilterOperator"
    )
    field_value: Optional[str] = Field(default=None, alias="FieldValue")


class CreateBlueprintRequestModel(BaseModel):
    name: str = Field(alias="Name")
    blueprint_location: str = Field(alias="BlueprintLocation")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateCsvClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    quote_symbol: Optional[str] = Field(default=None, alias="QuoteSymbol")
    contains_header: Optional[Literal["ABSENT", "PRESENT", "UNKNOWN"]] = Field(
        default=None, alias="ContainsHeader"
    )
    header: Optional[Sequence[str]] = Field(default=None, alias="Header")
    disable_value_trimming: Optional[bool] = Field(
        default=None, alias="DisableValueTrimming"
    )
    allow_single_column: Optional[bool] = Field(default=None, alias="AllowSingleColumn")
    custom_datatype_configured: Optional[bool] = Field(
        default=None, alias="CustomDatatypeConfigured"
    )
    custom_datatypes: Optional[Sequence[str]] = Field(
        default=None, alias="CustomDatatypes"
    )


class CreateGrokClassifierRequestModel(BaseModel):
    classification: str = Field(alias="Classification")
    name: str = Field(alias="Name")
    grok_pattern: str = Field(alias="GrokPattern")
    custom_patterns: Optional[str] = Field(default=None, alias="CustomPatterns")


class CreateJsonClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    json_path: str = Field(alias="JsonPath")


class CreateXMLClassifierRequestModel(BaseModel):
    classification: str = Field(alias="Classification")
    name: str = Field(alias="Name")
    row_tag: Optional[str] = Field(default=None, alias="RowTag")


class CreateCustomEntityTypeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    regex_string: str = Field(alias="RegexString")
    context_words: Optional[Sequence[str]] = Field(default=None, alias="ContextWords")


class DataQualityTargetTableModel(BaseModel):
    table_name: str = Field(alias="TableName")
    database_name: str = Field(alias="DatabaseName")


class CreateDevEndpointRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    role_arn: str = Field(alias="RoleArn")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    public_keys: Optional[Sequence[str]] = Field(default=None, alias="PublicKeys")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    extra_python_libs_s3_path: Optional[str] = Field(
        default=None, alias="ExtraPythonLibsS3Path"
    )
    extra_jars_s3_path: Optional[str] = Field(default=None, alias="ExtraJarsS3Path")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    arguments: Optional[Mapping[str, str]] = Field(default=None, alias="Arguments")


class ExecutionPropertyModel(BaseModel):
    max_concurrent_runs: Optional[int] = Field(default=None, alias="MaxConcurrentRuns")


class JobCommandModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    script_location: Optional[str] = Field(default=None, alias="ScriptLocation")
    python_version: Optional[str] = Field(default=None, alias="PythonVersion")


class SourceControlDetailsModel(BaseModel):
    provider: Optional[Literal["AWS_CODE_COMMIT", "GITHUB"]] = Field(
        default=None, alias="Provider"
    )
    repository: Optional[str] = Field(default=None, alias="Repository")
    owner: Optional[str] = Field(default=None, alias="Owner")
    branch: Optional[str] = Field(default=None, alias="Branch")
    folder: Optional[str] = Field(default=None, alias="Folder")
    last_commit_id: Optional[str] = Field(default=None, alias="LastCommitId")
    auth_strategy: Optional[
        Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
    ] = Field(default=None, alias="AuthStrategy")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")


class GlueTableModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )


class PartitionIndexModel(BaseModel):
    keys: Sequence[str] = Field(alias="Keys")
    index_name: str = Field(alias="IndexName")


class CreateRegistryInputRequestModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class RegistryIdModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    registry_arn: Optional[str] = Field(default=None, alias="RegistryArn")


class SessionCommandModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    python_version: Optional[str] = Field(default=None, alias="PythonVersion")


class EventBatchingConditionModel(BaseModel):
    batch_size: int = Field(alias="BatchSize")
    batch_window: Optional[int] = Field(default=None, alias="BatchWindow")


class CreateWorkflowRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    default_run_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="DefaultRunProperties"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    max_concurrent_runs: Optional[int] = Field(default=None, alias="MaxConcurrentRuns")


class DQResultsPublishingOptionsModel(BaseModel):
    evaluation_context: Optional[str] = Field(default=None, alias="EvaluationContext")
    results_s3_prefix: Optional[str] = Field(default=None, alias="ResultsS3Prefix")
    cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchMetricsEnabled"
    )
    results_publishing_enabled: Optional[bool] = Field(
        default=None, alias="ResultsPublishingEnabled"
    )


class DQStopJobOnFailureOptionsModel(BaseModel):
    stop_job_on_failure_timing: Optional[Literal["AfterDataLoad", "Immediate"]] = Field(
        default=None, alias="StopJobOnFailureTiming"
    )


class EncryptionAtRestModel(BaseModel):
    catalog_encryption_mode: Literal["DISABLED", "SSE-KMS"] = Field(
        alias="CatalogEncryptionMode"
    )
    sse_aws_kms_key_id: Optional[str] = Field(default=None, alias="SseAwsKmsKeyId")


class DataLakePrincipalModel(BaseModel):
    data_lake_principal_identifier: Optional[str] = Field(
        default=None, alias="DataLakePrincipalIdentifier"
    )


class DataQualityEvaluationRunAdditionalRunOptionsModel(BaseModel):
    cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchMetricsEnabled"
    )
    results_s3_prefix: Optional[str] = Field(default=None, alias="ResultsS3Prefix")


class DataQualityRuleResultModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    evaluation_message: Optional[str] = Field(default=None, alias="EvaluationMessage")
    result: Optional[Literal["ERROR", "FAIL", "PASS"]] = Field(
        default=None, alias="Result"
    )


class DatabaseIdentifierModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")


class DatatypeModel(BaseModel):
    id: str = Field(alias="Id")
    label: str = Field(alias="Label")


class DecimalNumberModel(BaseModel):
    unscaled_value: bytes = Field(alias="UnscaledValue")
    scale: int = Field(alias="Scale")


class DeleteBlueprintRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteColumnStatisticsForPartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    column_name: str = Field(alias="ColumnName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteColumnStatisticsForTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    column_name: str = Field(alias="ColumnName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteConnectionRequestModel(BaseModel):
    connection_name: str = Field(alias="ConnectionName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteCustomEntityTypeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteDataQualityRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteDatabaseRequestModel(BaseModel):
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteDevEndpointRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class DeleteJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")


class DeleteMLTransformRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")


class DeletePartitionIndexRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    index_name: str = Field(alias="IndexName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeletePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteResourcePolicyRequestModel(BaseModel):
    policy_hash_condition: Optional[str] = Field(
        default=None, alias="PolicyHashCondition"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class SchemaIdModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")


class DeleteSecurityConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class DeleteTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class DeleteTableVersionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    version_id: str = Field(alias="VersionId")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteUserDefinedFunctionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    function_name: str = Field(alias="FunctionName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteWorkflowRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DevEndpointCustomLibrariesModel(BaseModel):
    extra_python_libs_s3_path: Optional[str] = Field(
        default=None, alias="ExtraPythonLibsS3Path"
    )
    extra_jars_s3_path: Optional[str] = Field(default=None, alias="ExtraJarsS3Path")


class DirectSchemaChangePolicyModel(BaseModel):
    enable_update_catalog: Optional[bool] = Field(
        default=None, alias="EnableUpdateCatalog"
    )
    update_behavior: Optional[Literal["LOG", "UPDATE_IN_DATABASE"]] = Field(
        default=None, alias="UpdateBehavior"
    )
    table: Optional[str] = Field(default=None, alias="Table")
    database: Optional[str] = Field(default=None, alias="Database")


class NullCheckBoxListModel(BaseModel):
    is_empty: Optional[bool] = Field(default=None, alias="IsEmpty")
    is_null_string: Optional[bool] = Field(default=None, alias="IsNullString")
    is_neg_one: Optional[bool] = Field(default=None, alias="IsNegOne")


class TransformConfigParameterModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["bool", "complex", "float", "int", "list", "null", "str"] = Field(
        alias="Type"
    )
    validation_rule: Optional[str] = Field(default=None, alias="ValidationRule")
    validation_message: Optional[str] = Field(default=None, alias="ValidationMessage")
    value: Optional[List[str]] = Field(default=None, alias="Value")
    list_type: Optional[
        Literal["bool", "complex", "float", "int", "list", "null", "str"]
    ] = Field(default=None, alias="ListType")
    is_optional: Optional[bool] = Field(default=None, alias="IsOptional")


class EdgeModel(BaseModel):
    source_id: Optional[str] = Field(default=None, alias="SourceId")
    destination_id: Optional[str] = Field(default=None, alias="DestinationId")


class JobBookmarksEncryptionModel(BaseModel):
    job_bookmarks_encryption_mode: Optional[Literal["CSE-KMS", "DISABLED"]] = Field(
        default=None, alias="JobBookmarksEncryptionMode"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class S3EncryptionModel(BaseModel):
    s3_encryption_mode: Optional[Literal["DISABLED", "SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="S3EncryptionMode"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class ErrorDetailsModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ExportLabelsTaskRunPropertiesModel(BaseModel):
    output_s3_path: Optional[str] = Field(default=None, alias="OutputS3Path")


class FilterValueModel(BaseModel):
    type: Literal["COLUMNEXTRACTED", "CONSTANT"] = Field(alias="Type")
    value: List[str] = Field(alias="Value")


class FindMatchesParametersModel(BaseModel):
    primary_key_column_name: Optional[str] = Field(
        default=None, alias="PrimaryKeyColumnName"
    )
    precision_recall_tradeoff: Optional[float] = Field(
        default=None, alias="PrecisionRecallTradeoff"
    )
    accuracy_cost_tradeoff: Optional[float] = Field(
        default=None, alias="AccuracyCostTradeoff"
    )
    enforce_provided_labels: Optional[bool] = Field(
        default=None, alias="EnforceProvidedLabels"
    )


class FindMatchesTaskRunPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")


class GetBlueprintRequestModel(BaseModel):
    name: str = Field(alias="Name")
    include_blueprint: Optional[bool] = Field(default=None, alias="IncludeBlueprint")
    include_parameter_spec: Optional[bool] = Field(
        default=None, alias="IncludeParameterSpec"
    )


class GetBlueprintRunRequestModel(BaseModel):
    blueprint_name: str = Field(alias="BlueprintName")
    run_id: str = Field(alias="RunId")


class GetBlueprintRunsRequestModel(BaseModel):
    blueprint_name: str = Field(alias="BlueprintName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetCatalogImportStatusRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetClassifiersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetColumnStatisticsForPartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    column_names: Sequence[str] = Field(alias="ColumnNames")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetColumnStatisticsForTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    column_names: Sequence[str] = Field(alias="ColumnNames")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    hide_password: Optional[bool] = Field(default=None, alias="HidePassword")


class GetConnectionsFilterModel(BaseModel):
    match_criteria: Optional[Sequence[str]] = Field(default=None, alias="MatchCriteria")
    connection_type: Optional[
        Literal["CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SFTP"]
    ] = Field(default=None, alias="ConnectionType")


class GetCrawlerMetricsRequestModel(BaseModel):
    crawler_name_list: Optional[Sequence[str]] = Field(
        default=None, alias="CrawlerNameList"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetCrawlersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCustomEntityTypeRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetDataCatalogEncryptionSettingsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetDataQualityResultRequestModel(BaseModel):
    result_id: str = Field(alias="ResultId")


class GetDataQualityRuleRecommendationRunRequestModel(BaseModel):
    run_id: str = Field(alias="RunId")


class GetDataQualityRulesetEvaluationRunRequestModel(BaseModel):
    run_id: str = Field(alias="RunId")


class GetDataQualityRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetDatabaseRequestModel(BaseModel):
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetDatabasesRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    resource_share_type: Optional[Literal["ALL", "FOREIGN"]] = Field(
        default=None, alias="ResourceShareType"
    )


class GetDataflowGraphRequestModel(BaseModel):
    python_script: Optional[str] = Field(default=None, alias="PythonScript")


class GetDevEndpointRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")


class GetDevEndpointsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetJobBookmarkRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    run_id: Optional[str] = Field(default=None, alias="RunId")


class JobBookmarkEntryModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    version: Optional[int] = Field(default=None, alias="Version")
    run: Optional[int] = Field(default=None, alias="Run")
    attempt: Optional[int] = Field(default=None, alias="Attempt")
    previous_run_id: Optional[str] = Field(default=None, alias="PreviousRunId")
    run_id: Optional[str] = Field(default=None, alias="RunId")
    job_bookmark: Optional[str] = Field(default=None, alias="JobBookmark")


class GetJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")


class GetJobRunRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    run_id: str = Field(alias="RunId")
    predecessors_included: Optional[bool] = Field(
        default=None, alias="PredecessorsIncluded"
    )


class GetJobRunsRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetMLTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    task_run_id: str = Field(alias="TaskRunId")


class TaskRunFilterCriteriaModel(BaseModel):
    task_run_type: Optional[
        Literal[
            "EVALUATION",
            "EXPORT_LABELS",
            "FIND_MATCHES",
            "IMPORT_LABELS",
            "LABELING_SET_GENERATION",
        ]
    ] = Field(default=None, alias="TaskRunType")
    status: Optional[
        Literal[
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="Status")
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedBefore"
    )
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedAfter"
    )


class TaskRunSortCriteriaModel(BaseModel):
    column: Literal["STARTED", "STATUS", "TASK_RUN_TYPE"] = Field(alias="Column")
    sort_direction: Literal["ASCENDING", "DESCENDING"] = Field(alias="SortDirection")


class GetMLTransformRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")


class SchemaColumnModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    data_type: Optional[str] = Field(default=None, alias="DataType")


class TransformSortCriteriaModel(BaseModel):
    column: Literal[
        "CREATED", "LAST_MODIFIED", "NAME", "STATUS", "TRANSFORM_TYPE"
    ] = Field(alias="Column")
    sort_direction: Literal["ASCENDING", "DESCENDING"] = Field(alias="SortDirection")


class MappingEntryModel(BaseModel):
    source_table: Optional[str] = Field(default=None, alias="SourceTable")
    source_path: Optional[str] = Field(default=None, alias="SourcePath")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    target_table: Optional[str] = Field(default=None, alias="TargetTable")
    target_path: Optional[str] = Field(default=None, alias="TargetPath")
    target_type: Optional[str] = Field(default=None, alias="TargetType")


class GetPartitionIndexesRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetPartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class SegmentModel(BaseModel):
    segment_number: int = Field(alias="SegmentNumber")
    total_segments: int = Field(alias="TotalSegments")


class GetResourcePoliciesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GluePolicyModel(BaseModel):
    policy_in_json: Optional[str] = Field(default=None, alias="PolicyInJson")
    policy_hash: Optional[str] = Field(default=None, alias="PolicyHash")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    update_time: Optional[datetime] = Field(default=None, alias="UpdateTime")


class GetResourcePolicyRequestModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class SchemaVersionNumberModel(BaseModel):
    latest_version: Optional[bool] = Field(default=None, alias="LatestVersion")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class GetSecurityConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetSecurityConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class GetStatementRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    id: int = Field(alias="Id")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class GetTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )


class GetTableVersionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class GetTableVersionsRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetTablesRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    expression: Optional[str] = Field(default=None, alias="Expression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )


class GetTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetTriggersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    dependent_job_name: Optional[str] = Field(default=None, alias="DependentJobName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetUserDefinedFunctionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    function_name: str = Field(alias="FunctionName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetUserDefinedFunctionsRequestModel(BaseModel):
    pattern: str = Field(alias="Pattern")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetWorkflowRequestModel(BaseModel):
    name: str = Field(alias="Name")
    include_graph: Optional[bool] = Field(default=None, alias="IncludeGraph")


class GetWorkflowRunPropertiesRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")


class GetWorkflowRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")
    include_graph: Optional[bool] = Field(default=None, alias="IncludeGraph")


class GetWorkflowRunsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    include_graph: Optional[bool] = Field(default=None, alias="IncludeGraph")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GlueStudioSchemaColumnModel(BaseModel):
    name: str = Field(alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")


class S3SourceAdditionalOptionsModel(BaseModel):
    bounded_size: Optional[int] = Field(default=None, alias="BoundedSize")
    bounded_files: Optional[int] = Field(default=None, alias="BoundedFiles")


class ImportCatalogToGlueRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class ImportLabelsTaskRunPropertiesModel(BaseModel):
    input_s3_path: Optional[str] = Field(default=None, alias="InputS3Path")
    replace: Optional[bool] = Field(default=None, alias="Replace")


class JDBCConnectorOptionsModel(BaseModel):
    filter_predicate: Optional[str] = Field(default=None, alias="FilterPredicate")
    partition_column: Optional[str] = Field(default=None, alias="PartitionColumn")
    lower_bound: Optional[int] = Field(default=None, alias="LowerBound")
    upper_bound: Optional[int] = Field(default=None, alias="UpperBound")
    num_partitions: Optional[int] = Field(default=None, alias="NumPartitions")
    job_bookmark_keys: Optional[List[str]] = Field(
        default=None, alias="JobBookmarkKeys"
    )
    job_bookmark_keys_sort_order: Optional[str] = Field(
        default=None, alias="JobBookmarkKeysSortOrder"
    )
    data_type_mapping: Optional[
        Dict[
            Literal[
                "ARRAY",
                "BIGINT",
                "BINARY",
                "BIT",
                "BLOB",
                "BOOLEAN",
                "CHAR",
                "CLOB",
                "DATALINK",
                "DATE",
                "DECIMAL",
                "DISTINCT",
                "DOUBLE",
                "FLOAT",
                "INTEGER",
                "JAVA_OBJECT",
                "LONGNVARCHAR",
                "LONGVARBINARY",
                "LONGVARCHAR",
                "NCHAR",
                "NCLOB",
                "NULL",
                "NUMERIC",
                "NVARCHAR",
                "OTHER",
                "REAL",
                "REF",
                "REF_CURSOR",
                "ROWID",
                "SMALLINT",
                "SQLXML",
                "STRUCT",
                "TIME",
                "TIMESTAMP",
                "TIMESTAMP_WITH_TIMEZONE",
                "TIME_WITH_TIMEZONE",
                "TINYINT",
                "VARBINARY",
                "VARCHAR",
            ],
            Literal[
                "BIGDECIMAL",
                "BYTE",
                "DATE",
                "DOUBLE",
                "FLOAT",
                "INT",
                "LONG",
                "SHORT",
                "STRING",
                "TIMESTAMP",
            ],
        ]
    ] = Field(default=None, alias="DataTypeMapping")


class PredecessorModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    run_id: Optional[str] = Field(default=None, alias="RunId")


class JoinColumnModel(BaseModel):
    from_: str = Field(alias="From")
    keys: List[List[str]] = Field(alias="Keys")


class KeySchemaElementModel(BaseModel):
    name: str = Field(alias="Name")
    type: str = Field(alias="Type")


class LabelingSetGenerationTaskRunPropertiesModel(BaseModel):
    output_s3_path: Optional[str] = Field(default=None, alias="OutputS3Path")


class ListBlueprintsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListCrawlersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListCustomEntityTypesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDevEndpointsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListJobsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListRegistriesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RegistryListItemModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    registry_arn: Optional[str] = Field(default=None, alias="RegistryArn")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["AVAILABLE", "DELETING"]] = Field(
        default=None, alias="Status"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    updated_time: Optional[str] = Field(default=None, alias="UpdatedTime")


class SchemaVersionListItemModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    status: Optional[Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")


class SchemaListItemModel(BaseModel):
    registry_name: Optional[str] = Field(default=None, alias="RegistryName")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    description: Optional[str] = Field(default=None, alias="Description")
    schema_status: Optional[Literal["AVAILABLE", "DELETING", "PENDING"]] = Field(
        default=None, alias="SchemaStatus"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    updated_time: Optional[str] = Field(default=None, alias="UpdatedTime")


class ListSessionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class ListStatementsRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTriggersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    dependent_job_name: Optional[str] = Field(default=None, alias="DependentJobName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListWorkflowsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MLUserDataEncryptionModel(BaseModel):
    ml_user_data_encryption_mode: Literal["DISABLED", "SSE-KMS"] = Field(
        alias="MlUserDataEncryptionMode"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class MappingModel(BaseModel):
    to_key: Optional[str] = Field(default=None, alias="ToKey")
    from_path: Optional[List[str]] = Field(default=None, alias="FromPath")
    from_type: Optional[str] = Field(default=None, alias="FromType")
    to_type: Optional[str] = Field(default=None, alias="ToType")
    dropped: Optional[bool] = Field(default=None, alias="Dropped")
    children: Optional[List[Dict[str, Any]]] = Field(default=None, alias="Children")


class OtherMetadataValueListItemModel(BaseModel):
    metadata_value: Optional[str] = Field(default=None, alias="MetadataValue")
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")


class MetadataKeyValuePairModel(BaseModel):
    metadata_key: Optional[str] = Field(default=None, alias="MetadataKey")
    metadata_value: Optional[str] = Field(default=None, alias="MetadataValue")


class OrderModel(BaseModel):
    column: str = Field(alias="Column")
    sort_order: int = Field(alias="SortOrder")


class PropertyPredicateModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    comparator: Optional[
        Literal[
            "EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_EQUALS",
            "LESS_THAN",
            "LESS_THAN_EQUALS",
        ]
    ] = Field(default=None, alias="Comparator")


class PutResourcePolicyRequestModel(BaseModel):
    policy_in_json: str = Field(alias="PolicyInJson")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    policy_hash_condition: Optional[str] = Field(
        default=None, alias="PolicyHashCondition"
    )
    policy_exists_condition: Optional[
        Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
    ] = Field(default=None, alias="PolicyExistsCondition")
    enable_hybrid: Optional[Literal["FALSE", "TRUE"]] = Field(
        default=None, alias="EnableHybrid"
    )


class PutWorkflowRunPropertiesRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")
    run_properties: Mapping[str, str] = Field(alias="RunProperties")


class UpsertRedshiftTargetOptionsModel(BaseModel):
    table_location: Optional[str] = Field(default=None, alias="TableLocation")
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    upsert_keys: Optional[List[str]] = Field(default=None, alias="UpsertKeys")


class ResetJobBookmarkRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    run_id: Optional[str] = Field(default=None, alias="RunId")


class ResourceUriModel(BaseModel):
    resource_type: Optional[Literal["ARCHIVE", "FILE", "JAR"]] = Field(
        default=None, alias="ResourceType"
    )
    uri: Optional[str] = Field(default=None, alias="Uri")


class ResumeWorkflowRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")
    node_ids: Sequence[str] = Field(alias="NodeIds")


class RunStatementRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    code: str = Field(alias="Code")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class S3DirectSourceAdditionalOptionsModel(BaseModel):
    bounded_size: Optional[int] = Field(default=None, alias="BoundedSize")
    bounded_files: Optional[int] = Field(default=None, alias="BoundedFiles")
    enable_sample_path: Optional[bool] = Field(default=None, alias="EnableSamplePath")
    sample_path: Optional[str] = Field(default=None, alias="SamplePath")


class SortCriterionModel(BaseModel):
    field_name: Optional[str] = Field(default=None, alias="FieldName")
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="Sort")


class SerDeInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    serialization_library: Optional[str] = Field(
        default=None, alias="SerializationLibrary"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class SkewedInfoModel(BaseModel):
    skewed_column_names: Optional[Sequence[str]] = Field(
        default=None, alias="SkewedColumnNames"
    )
    skewed_column_values: Optional[Sequence[str]] = Field(
        default=None, alias="SkewedColumnValues"
    )
    skewed_column_value_location_maps: Optional[Mapping[str, str]] = Field(
        default=None, alias="SkewedColumnValueLocationMaps"
    )


class SqlAliasModel(BaseModel):
    from_: str = Field(alias="From")
    alias: str = Field(alias="Alias")


class StartBlueprintRunRequestModel(BaseModel):
    blueprint_name: str = Field(alias="BlueprintName")
    role_arn: str = Field(alias="RoleArn")
    parameters: Optional[str] = Field(default=None, alias="Parameters")


class StartCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartCrawlerScheduleRequestModel(BaseModel):
    crawler_name: str = Field(alias="CrawlerName")


class StartExportLabelsTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    output_s3_path: str = Field(alias="OutputS3Path")


class StartImportLabelsTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    input_s3_path: str = Field(alias="InputS3Path")
    replace_all_labels: Optional[bool] = Field(default=None, alias="ReplaceAllLabels")


class StartMLEvaluationTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")


class StartMLLabelingSetGenerationTaskRunRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    output_s3_path: str = Field(alias="OutputS3Path")


class StartTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartWorkflowRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="RunProperties"
    )


class StartingEventBatchConditionModel(BaseModel):
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    batch_window: Optional[int] = Field(default=None, alias="BatchWindow")


class StatementOutputDataModel(BaseModel):
    text_plain: Optional[str] = Field(default=None, alias="TextPlain")


class StopCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StopCrawlerScheduleRequestModel(BaseModel):
    crawler_name: str = Field(alias="CrawlerName")


class StopSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class StopTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StopWorkflowRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")


class TableIdentifierModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    name: Optional[str] = Field(default=None, alias="Name")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags_to_add: Mapping[str, str] = Field(alias="TagsToAdd")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags_to_remove: Sequence[str] = Field(alias="TagsToRemove")


class UpdateBlueprintRequestModel(BaseModel):
    name: str = Field(alias="Name")
    blueprint_location: str = Field(alias="BlueprintLocation")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateCsvClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    quote_symbol: Optional[str] = Field(default=None, alias="QuoteSymbol")
    contains_header: Optional[Literal["ABSENT", "PRESENT", "UNKNOWN"]] = Field(
        default=None, alias="ContainsHeader"
    )
    header: Optional[Sequence[str]] = Field(default=None, alias="Header")
    disable_value_trimming: Optional[bool] = Field(
        default=None, alias="DisableValueTrimming"
    )
    allow_single_column: Optional[bool] = Field(default=None, alias="AllowSingleColumn")
    custom_datatype_configured: Optional[bool] = Field(
        default=None, alias="CustomDatatypeConfigured"
    )
    custom_datatypes: Optional[Sequence[str]] = Field(
        default=None, alias="CustomDatatypes"
    )


class UpdateGrokClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    classification: Optional[str] = Field(default=None, alias="Classification")
    grok_pattern: Optional[str] = Field(default=None, alias="GrokPattern")
    custom_patterns: Optional[str] = Field(default=None, alias="CustomPatterns")


class UpdateJsonClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    json_path: Optional[str] = Field(default=None, alias="JsonPath")


class UpdateXMLClassifierRequestModel(BaseModel):
    name: str = Field(alias="Name")
    classification: Optional[str] = Field(default=None, alias="Classification")
    row_tag: Optional[str] = Field(default=None, alias="RowTag")


class UpdateCrawlerScheduleRequestModel(BaseModel):
    crawler_name: str = Field(alias="CrawlerName")
    schedule: Optional[str] = Field(default=None, alias="Schedule")


class UpdateDataQualityRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    updated_name: Optional[str] = Field(default=None, alias="UpdatedName")
    description: Optional[str] = Field(default=None, alias="Description")
    ruleset: Optional[str] = Field(default=None, alias="Ruleset")


class UpdateJobFromSourceControlRequestModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    provider: Optional[Literal["AWS_CODE_COMMIT", "GITHUB"]] = Field(
        default=None, alias="Provider"
    )
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    repository_owner: Optional[str] = Field(default=None, alias="RepositoryOwner")
    branch_name: Optional[str] = Field(default=None, alias="BranchName")
    folder: Optional[str] = Field(default=None, alias="Folder")
    commit_id: Optional[str] = Field(default=None, alias="CommitId")
    auth_strategy: Optional[
        Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
    ] = Field(default=None, alias="AuthStrategy")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")


class UpdateSourceControlFromJobRequestModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    provider: Optional[Literal["AWS_CODE_COMMIT", "GITHUB"]] = Field(
        default=None, alias="Provider"
    )
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    repository_owner: Optional[str] = Field(default=None, alias="RepositoryOwner")
    branch_name: Optional[str] = Field(default=None, alias="BranchName")
    folder: Optional[str] = Field(default=None, alias="Folder")
    commit_id: Optional[str] = Field(default=None, alias="CommitId")
    auth_strategy: Optional[
        Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
    ] = Field(default=None, alias="AuthStrategy")
    auth_token: Optional[str] = Field(default=None, alias="AuthToken")


class UpdateWorkflowRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    default_run_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="DefaultRunProperties"
    )
    max_concurrent_runs: Optional[int] = Field(default=None, alias="MaxConcurrentRuns")


class WorkflowRunStatisticsModel(BaseModel):
    total_actions: Optional[int] = Field(default=None, alias="TotalActions")
    timeout_actions: Optional[int] = Field(default=None, alias="TimeoutActions")
    failed_actions: Optional[int] = Field(default=None, alias="FailedActions")
    stopped_actions: Optional[int] = Field(default=None, alias="StoppedActions")
    succeeded_actions: Optional[int] = Field(default=None, alias="SucceededActions")
    running_actions: Optional[int] = Field(default=None, alias="RunningActions")
    errored_actions: Optional[int] = Field(default=None, alias="ErroredActions")
    waiting_actions: Optional[int] = Field(default=None, alias="WaitingActions")


class ActionModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    arguments: Optional[Dict[str, str]] = Field(default=None, alias="Arguments")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    crawler_name: Optional[str] = Field(default=None, alias="CrawlerName")


class StartJobRunRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")
    arguments: Optional[Mapping[str, str]] = Field(default=None, alias="Arguments")
    allocated_capacity: Optional[int] = Field(default=None, alias="AllocatedCapacity")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    execution_class: Optional[Literal["FLEX", "STANDARD"]] = Field(
        default=None, alias="ExecutionClass"
    )


class AggregateModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    groups: List[List[str]] = Field(alias="Groups")
    aggs: List[AggregateOperationModel] = Field(alias="Aggs")


class GetUnfilteredPartitionMetadataRequestModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    supported_permission_types: Sequence[
        Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
    ] = Field(alias="SupportedPermissionTypes")
    audit_context: Optional[AuditContextModel] = Field(
        default=None, alias="AuditContext"
    )


class GetUnfilteredTableMetadataRequestModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    database_name: str = Field(alias="DatabaseName")
    name: str = Field(alias="Name")
    supported_permission_types: Sequence[
        Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
    ] = Field(alias="SupportedPermissionTypes")
    audit_context: Optional[AuditContextModel] = Field(
        default=None, alias="AuditContext"
    )


class BackfillErrorModel(BaseModel):
    code: Optional[
        Literal[
            "ENCRYPTED_PARTITION_ERROR",
            "INTERNAL_ERROR",
            "INVALID_PARTITION_TYPE_DATA_ERROR",
            "MISSING_PARTITION_VALUE_ERROR",
            "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    partitions: Optional[List[PartitionValueListModel]] = Field(
        default=None, alias="Partitions"
    )


class BatchDeletePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partitions_to_delete: Sequence[PartitionValueListModel] = Field(
        alias="PartitionsToDelete"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchGetPartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partitions_to_get: Sequence[PartitionValueListModel] = Field(
        alias="PartitionsToGet"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class CancelMLTaskRunResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    task_run_id: str = Field(alias="TaskRunId")
    status: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckSchemaVersionValidityResponseModel(BaseModel):
    valid: bool = Field(alias="Valid")
    error: str = Field(alias="Error")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBlueprintResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomEntityTypeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataQualityRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDevEndpointResponseModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    status: str = Field(alias="Status")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_id: str = Field(alias="SubnetId")
    role_arn: str = Field(alias="RoleArn")
    yarn_endpoint_address: str = Field(alias="YarnEndpointAddress")
    zeppelin_remote_spark_interpreter_port: int = Field(
        alias="ZeppelinRemoteSparkInterpreterPort"
    )
    number_of_nodes: int = Field(alias="NumberOfNodes")
    worker_type: Literal["G.025X", "G.1X", "G.2X", "Standard"] = Field(
        alias="WorkerType"
    )
    glue_version: str = Field(alias="GlueVersion")
    number_of_workers: int = Field(alias="NumberOfWorkers")
    availability_zone: str = Field(alias="AvailabilityZone")
    vpc_id: str = Field(alias="VpcId")
    extra_python_libs_s3_path: str = Field(alias="ExtraPythonLibsS3Path")
    extra_jars_s3_path: str = Field(alias="ExtraJarsS3Path")
    failure_reason: str = Field(alias="FailureReason")
    security_configuration: str = Field(alias="SecurityConfiguration")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    arguments: Dict[str, str] = Field(alias="Arguments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMLTransformResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRegistryResponseModel(BaseModel):
    registry_arn: str = Field(alias="RegistryArn")
    registry_name: str = Field(alias="RegistryName")
    description: str = Field(alias="Description")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSchemaResponseModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    registry_arn: str = Field(alias="RegistryArn")
    schema_name: str = Field(alias="SchemaName")
    schema_arn: str = Field(alias="SchemaArn")
    description: str = Field(alias="Description")
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    compatibility: Literal[
        "BACKWARD",
        "BACKWARD_ALL",
        "DISABLED",
        "FORWARD",
        "FORWARD_ALL",
        "FULL",
        "FULL_ALL",
        "NONE",
    ] = Field(alias="Compatibility")
    schema_checkpoint: int = Field(alias="SchemaCheckpoint")
    latest_schema_version: int = Field(alias="LatestSchemaVersion")
    next_schema_version: int = Field(alias="NextSchemaVersion")
    schema_status: Literal["AVAILABLE", "DELETING", "PENDING"] = Field(
        alias="SchemaStatus"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    schema_version_id: str = Field(alias="SchemaVersionId")
    schema_version_status: Literal[
        "AVAILABLE", "DELETING", "FAILURE", "PENDING"
    ] = Field(alias="SchemaVersionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScriptResponseModel(BaseModel):
    python_script: str = Field(alias="PythonScript")
    scala_code: str = Field(alias="ScalaCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSecurityConfigurationResponseModel(BaseModel):
    name: str = Field(alias="Name")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTriggerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBlueprintResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCustomEntityTypeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteJobResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMLTransformResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRegistryResponseModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    registry_arn: str = Field(alias="RegistryArn")
    status: Literal["AVAILABLE", "DELETING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    status: Literal["AVAILABLE", "DELETING", "PENDING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSessionResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTriggerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWorkflowResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCustomEntityTypeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    regex_string: str = Field(alias="RegexString")
    context_words: List[str] = Field(alias="ContextWords")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPlanResponseModel(BaseModel):
    python_script: str = Field(alias="PythonScript")
    scala_code: str = Field(alias="ScalaCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegistryResponseModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    registry_arn: str = Field(alias="RegistryArn")
    description: str = Field(alias="Description")
    status: Literal["AVAILABLE", "DELETING"] = Field(alias="Status")
    created_time: str = Field(alias="CreatedTime")
    updated_time: str = Field(alias="UpdatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    policy_in_json: str = Field(alias="PolicyInJson")
    policy_hash: str = Field(alias="PolicyHash")
    create_time: datetime = Field(alias="CreateTime")
    update_time: datetime = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaByDefinitionResponseModel(BaseModel):
    schema_version_id: str = Field(alias="SchemaVersionId")
    schema_arn: str = Field(alias="SchemaArn")
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    status: Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"] = Field(
        alias="Status"
    )
    created_time: str = Field(alias="CreatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaResponseModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    registry_arn: str = Field(alias="RegistryArn")
    schema_name: str = Field(alias="SchemaName")
    schema_arn: str = Field(alias="SchemaArn")
    description: str = Field(alias="Description")
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    compatibility: Literal[
        "BACKWARD",
        "BACKWARD_ALL",
        "DISABLED",
        "FORWARD",
        "FORWARD_ALL",
        "FULL",
        "FULL_ALL",
        "NONE",
    ] = Field(alias="Compatibility")
    schema_checkpoint: int = Field(alias="SchemaCheckpoint")
    latest_schema_version: int = Field(alias="LatestSchemaVersion")
    next_schema_version: int = Field(alias="NextSchemaVersion")
    schema_status: Literal["AVAILABLE", "DELETING", "PENDING"] = Field(
        alias="SchemaStatus"
    )
    created_time: str = Field(alias="CreatedTime")
    updated_time: str = Field(alias="UpdatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaVersionResponseModel(BaseModel):
    schema_version_id: str = Field(alias="SchemaVersionId")
    schema_definition: str = Field(alias="SchemaDefinition")
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    schema_arn: str = Field(alias="SchemaArn")
    version_number: int = Field(alias="VersionNumber")
    status: Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"] = Field(
        alias="Status"
    )
    created_time: str = Field(alias="CreatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaVersionsDiffResponseModel(BaseModel):
    diff: str = Field(alias="Diff")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagsResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowRunPropertiesResponseModel(BaseModel):
    run_properties: Dict[str, str] = Field(alias="RunProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBlueprintsResponseModel(BaseModel):
    blueprints: List[str] = Field(alias="Blueprints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCrawlersResponseModel(BaseModel):
    crawler_names: List[str] = Field(alias="CrawlerNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevEndpointsResponseModel(BaseModel):
    dev_endpoint_names: List[str] = Field(alias="DevEndpointNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResponseModel(BaseModel):
    job_names: List[str] = Field(alias="JobNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMLTransformsResponseModel(BaseModel):
    transform_ids: List[str] = Field(alias="TransformIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTriggersResponseModel(BaseModel):
    trigger_names: List[str] = Field(alias="TriggerNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkflowsResponseModel(BaseModel):
    workflows: List[str] = Field(alias="Workflows")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    policy_hash: str = Field(alias="PolicyHash")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSchemaVersionMetadataResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    registry_name: str = Field(alias="RegistryName")
    latest_version: bool = Field(alias="LatestVersion")
    version_number: int = Field(alias="VersionNumber")
    schema_version_id: str = Field(alias="SchemaVersionId")
    metadata_key: str = Field(alias="MetadataKey")
    metadata_value: str = Field(alias="MetadataValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterSchemaVersionResponseModel(BaseModel):
    schema_version_id: str = Field(alias="SchemaVersionId")
    version_number: int = Field(alias="VersionNumber")
    status: Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveSchemaVersionMetadataResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    registry_name: str = Field(alias="RegistryName")
    latest_version: bool = Field(alias="LatestVersion")
    version_number: int = Field(alias="VersionNumber")
    schema_version_id: str = Field(alias="SchemaVersionId")
    metadata_key: str = Field(alias="MetadataKey")
    metadata_value: str = Field(alias="MetadataValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResumeWorkflowRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    node_ids: List[str] = Field(alias="NodeIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunStatementResponseModel(BaseModel):
    id: int = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBlueprintRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataQualityRuleRecommendationRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataQualityRulesetEvaluationRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExportLabelsTaskRunResponseModel(BaseModel):
    task_run_id: str = Field(alias="TaskRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportLabelsTaskRunResponseModel(BaseModel):
    task_run_id: str = Field(alias="TaskRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartJobRunResponseModel(BaseModel):
    job_run_id: str = Field(alias="JobRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMLEvaluationTaskRunResponseModel(BaseModel):
    task_run_id: str = Field(alias="TaskRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMLLabelingSetGenerationTaskRunResponseModel(BaseModel):
    task_run_id: str = Field(alias="TaskRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTriggerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartWorkflowRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopSessionResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopTriggerResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBlueprintResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataQualityRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    ruleset: str = Field(alias="Ruleset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobFromSourceControlResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMLTransformResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegistryResponseModel(BaseModel):
    registry_name: str = Field(alias="RegistryName")
    registry_arn: str = Field(alias="RegistryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    schema_name: str = Field(alias="SchemaName")
    registry_name: str = Field(alias="RegistryName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSourceControlFromJobResponseModel(BaseModel):
    job_name: str = Field(alias="JobName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkflowResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteConnectionResponseModel(BaseModel):
    succeeded: List[str] = Field(alias="Succeeded")
    errors: Dict[str, ErrorDetailModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchStopJobRunErrorModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")
    error_detail: Optional[ErrorDetailModel] = Field(default=None, alias="ErrorDetail")


class BatchUpdatePartitionFailureEntryModel(BaseModel):
    partition_value_list: Optional[List[str]] = Field(
        default=None, alias="PartitionValueList"
    )
    error_detail: Optional[ErrorDetailModel] = Field(default=None, alias="ErrorDetail")


class ColumnErrorModel(BaseModel):
    column_name: Optional[str] = Field(default=None, alias="ColumnName")
    error: Optional[ErrorDetailModel] = Field(default=None, alias="Error")


class PartitionErrorModel(BaseModel):
    partition_values: Optional[List[str]] = Field(default=None, alias="PartitionValues")
    error_detail: Optional[ErrorDetailModel] = Field(default=None, alias="ErrorDetail")


class TableErrorModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    error_detail: Optional[ErrorDetailModel] = Field(default=None, alias="ErrorDetail")


class TableVersionErrorModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    error_detail: Optional[ErrorDetailModel] = Field(default=None, alias="ErrorDetail")


class BatchGetCustomEntityTypesResponseModel(BaseModel):
    custom_entity_types: List[CustomEntityTypeModel] = Field(alias="CustomEntityTypes")
    custom_entity_types_not_found: List[str] = Field(alias="CustomEntityTypesNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomEntityTypesResponseModel(BaseModel):
    custom_entity_types: List[CustomEntityTypeModel] = Field(alias="CustomEntityTypes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetDevEndpointsResponseModel(BaseModel):
    dev_endpoints: List[DevEndpointModel] = Field(alias="DevEndpoints")
    dev_endpoints_not_found: List[str] = Field(alias="DevEndpointsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevEndpointResponseModel(BaseModel):
    dev_endpoint: DevEndpointModel = Field(alias="DevEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevEndpointsResponseModel(BaseModel):
    dev_endpoints: List[DevEndpointModel] = Field(alias="DevEndpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlueprintRunResponseModel(BaseModel):
    blueprint_run: BlueprintRunModel = Field(alias="BlueprintRun")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlueprintRunsResponseModel(BaseModel):
    blueprint_runs: List[BlueprintRunModel] = Field(alias="BlueprintRuns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BlueprintModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    parameter_spec: Optional[str] = Field(default=None, alias="ParameterSpec")
    blueprint_location: Optional[str] = Field(default=None, alias="BlueprintLocation")
    blueprint_service_location: Optional[str] = Field(
        default=None, alias="BlueprintServiceLocation"
    )
    status: Optional[Literal["ACTIVE", "CREATING", "FAILED", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_active_definition: Optional[LastActiveDefinitionModel] = Field(
        default=None, alias="LastActiveDefinition"
    )


class GetCatalogImportStatusResponseModel(BaseModel):
    import_status: CatalogImportStatusModel = Field(alias="ImportStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CatalogKafkaSourceModel(BaseModel):
    name: str = Field(alias="Name")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    window_size: Optional[int] = Field(default=None, alias="WindowSize")
    detect_schema: Optional[bool] = Field(default=None, alias="DetectSchema")
    streaming_options: Optional[KafkaStreamingSourceOptionsModel] = Field(
        default=None, alias="StreamingOptions"
    )
    data_preview_options: Optional[StreamingDataPreviewOptionsModel] = Field(
        default=None, alias="DataPreviewOptions"
    )


class DirectKafkaSourceModel(BaseModel):
    name: str = Field(alias="Name")
    streaming_options: Optional[KafkaStreamingSourceOptionsModel] = Field(
        default=None, alias="StreamingOptions"
    )
    window_size: Optional[int] = Field(default=None, alias="WindowSize")
    detect_schema: Optional[bool] = Field(default=None, alias="DetectSchema")
    data_preview_options: Optional[StreamingDataPreviewOptionsModel] = Field(
        default=None, alias="DataPreviewOptions"
    )


class CatalogKinesisSourceModel(BaseModel):
    name: str = Field(alias="Name")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    window_size: Optional[int] = Field(default=None, alias="WindowSize")
    detect_schema: Optional[bool] = Field(default=None, alias="DetectSchema")
    streaming_options: Optional[KinesisStreamingSourceOptionsModel] = Field(
        default=None, alias="StreamingOptions"
    )
    data_preview_options: Optional[StreamingDataPreviewOptionsModel] = Field(
        default=None, alias="DataPreviewOptions"
    )


class DirectKinesisSourceModel(BaseModel):
    name: str = Field(alias="Name")
    window_size: Optional[int] = Field(default=None, alias="WindowSize")
    detect_schema: Optional[bool] = Field(default=None, alias="DetectSchema")
    streaming_options: Optional[KinesisStreamingSourceOptionsModel] = Field(
        default=None, alias="StreamingOptions"
    )
    data_preview_options: Optional[StreamingDataPreviewOptionsModel] = Field(
        default=None, alias="DataPreviewOptions"
    )


class GovernedCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    schema_change_policy: Optional[CatalogSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3CatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    schema_change_policy: Optional[CatalogSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3DeltaCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )
    schema_change_policy: Optional[CatalogSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3HudiCatalogTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    table: str = Field(alias="Table")
    database: str = Field(alias="Database")
    additional_options: Dict[str, str] = Field(alias="AdditionalOptions")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    schema_change_policy: Optional[CatalogSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class ClassifierModel(BaseModel):
    grok_classifier: Optional[GrokClassifierModel] = Field(
        default=None, alias="GrokClassifier"
    )
    xml_classifier: Optional[XMLClassifierModel] = Field(
        default=None, alias="XMLClassifier"
    )
    json_classifier: Optional[JsonClassifierModel] = Field(
        default=None, alias="JsonClassifier"
    )
    csv_classifier: Optional[CsvClassifierModel] = Field(
        default=None, alias="CsvClassifier"
    )


class CodeGenNodeModel(BaseModel):
    id: str = Field(alias="Id")
    node_type: str = Field(alias="NodeType")
    args: Sequence[CodeGenNodeArgModel] = Field(alias="Args")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")


class LocationModel(BaseModel):
    jdbc: Optional[Sequence[CodeGenNodeArgModel]] = Field(default=None, alias="Jdbc")
    s3: Optional[Sequence[CodeGenNodeArgModel]] = Field(default=None, alias="S3")
    dynamo_db: Optional[Sequence[CodeGenNodeArgModel]] = Field(
        default=None, alias="DynamoDB"
    )


class PredicateModel(BaseModel):
    logical: Optional[Literal["AND", "ANY"]] = Field(default=None, alias="Logical")
    conditions: Optional[List[ConditionModel]] = Field(default=None, alias="Conditions")


class FindMatchesMetricsModel(BaseModel):
    area_under_p_rcurve: Optional[float] = Field(default=None, alias="AreaUnderPRCurve")
    precision: Optional[float] = Field(default=None, alias="Precision")
    recall: Optional[float] = Field(default=None, alias="Recall")
    f1: Optional[float] = Field(default=None, alias="F1")
    confusion_matrix: Optional[ConfusionMatrixModel] = Field(
        default=None, alias="ConfusionMatrix"
    )
    column_importances: Optional[List[ColumnImportanceModel]] = Field(
        default=None, alias="ColumnImportances"
    )


class ConnectionInputModel(BaseModel):
    name: str = Field(alias="Name")
    connection_type: Literal[
        "CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SFTP"
    ] = Field(alias="ConnectionType")
    connection_properties: Mapping[
        Literal[
            "CONFIG_FILES",
            "CONNECTION_URL",
            "CONNECTOR_CLASS_NAME",
            "CONNECTOR_TYPE",
            "CONNECTOR_URL",
            "CUSTOM_JDBC_CERT",
            "CUSTOM_JDBC_CERT_STRING",
            "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
            "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
            "ENCRYPTED_PASSWORD",
            "HOST",
            "INSTANCE_ID",
            "JDBC_CONNECTION_URL",
            "JDBC_DRIVER_CLASS_NAME",
            "JDBC_DRIVER_JAR_URI",
            "JDBC_ENFORCE_SSL",
            "JDBC_ENGINE",
            "JDBC_ENGINE_VERSION",
            "KAFKA_BOOTSTRAP_SERVERS",
            "KAFKA_CLIENT_KEYSTORE",
            "KAFKA_CLIENT_KEYSTORE_PASSWORD",
            "KAFKA_CLIENT_KEY_PASSWORD",
            "KAFKA_CUSTOM_CERT",
            "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
            "KAFKA_SSL_ENABLED",
            "PASSWORD",
            "PORT",
            "SECRET_ID",
            "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
            "USERNAME",
        ],
        str,
    ] = Field(alias="ConnectionProperties")
    description: Optional[str] = Field(default=None, alias="Description")
    match_criteria: Optional[Sequence[str]] = Field(default=None, alias="MatchCriteria")
    physical_connection_requirements: Optional[
        PhysicalConnectionRequirementsModel
    ] = Field(default=None, alias="PhysicalConnectionRequirements")


class ConnectionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    connection_type: Optional[
        Literal["CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SFTP"]
    ] = Field(default=None, alias="ConnectionType")
    match_criteria: Optional[List[str]] = Field(default=None, alias="MatchCriteria")
    connection_properties: Optional[
        Dict[
            Literal[
                "CONFIG_FILES",
                "CONNECTION_URL",
                "CONNECTOR_CLASS_NAME",
                "CONNECTOR_TYPE",
                "CONNECTOR_URL",
                "CUSTOM_JDBC_CERT",
                "CUSTOM_JDBC_CERT_STRING",
                "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
                "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
                "ENCRYPTED_PASSWORD",
                "HOST",
                "INSTANCE_ID",
                "JDBC_CONNECTION_URL",
                "JDBC_DRIVER_CLASS_NAME",
                "JDBC_DRIVER_JAR_URI",
                "JDBC_ENFORCE_SSL",
                "JDBC_ENGINE",
                "JDBC_ENGINE_VERSION",
                "KAFKA_BOOTSTRAP_SERVERS",
                "KAFKA_CLIENT_KEYSTORE",
                "KAFKA_CLIENT_KEYSTORE_PASSWORD",
                "KAFKA_CLIENT_KEY_PASSWORD",
                "KAFKA_CUSTOM_CERT",
                "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
                "KAFKA_SSL_ENABLED",
                "PASSWORD",
                "PORT",
                "SECRET_ID",
                "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
                "USERNAME",
            ],
            str,
        ]
    ] = Field(default=None, alias="ConnectionProperties")
    physical_connection_requirements: Optional[
        PhysicalConnectionRequirementsModel
    ] = Field(default=None, alias="PhysicalConnectionRequirements")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    last_updated_by: Optional[str] = Field(default=None, alias="LastUpdatedBy")


class CrawlerNodeDetailsModel(BaseModel):
    crawls: Optional[List[CrawlModel]] = Field(default=None, alias="Crawls")


class ListCrawlsResponseModel(BaseModel):
    crawls: List[CrawlerHistoryModel] = Field(alias="Crawls")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCrawlerMetricsResponseModel(BaseModel):
    crawler_metrics_list: List[CrawlerMetricsModel] = Field(alias="CrawlerMetricsList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CrawlerTargetsModel(BaseModel):
    s3_targets: Optional[List[S3TargetModel]] = Field(default=None, alias="S3Targets")
    jdbc_targets: Optional[List[JdbcTargetModel]] = Field(
        default=None, alias="JdbcTargets"
    )
    mongo_dbtargets: Optional[List[MongoDBTargetModel]] = Field(
        default=None, alias="MongoDBTargets"
    )
    dynamo_dbtargets: Optional[List[DynamoDBTargetModel]] = Field(
        default=None, alias="DynamoDBTargets"
    )
    catalog_targets: Optional[List[CatalogTargetModel]] = Field(
        default=None, alias="CatalogTargets"
    )
    delta_targets: Optional[List[DeltaTargetModel]] = Field(
        default=None, alias="DeltaTargets"
    )


class ListCrawlsRequestModel(BaseModel):
    crawler_name: str = Field(alias="CrawlerName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[CrawlsFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateClassifierRequestModel(BaseModel):
    grok_classifier: Optional[CreateGrokClassifierRequestModel] = Field(
        default=None, alias="GrokClassifier"
    )
    xml_classifier: Optional[CreateXMLClassifierRequestModel] = Field(
        default=None, alias="XMLClassifier"
    )
    json_classifier: Optional[CreateJsonClassifierRequestModel] = Field(
        default=None, alias="JsonClassifier"
    )
    csv_classifier: Optional[CreateCsvClassifierRequestModel] = Field(
        default=None, alias="CsvClassifier"
    )


class CreateDataQualityRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    ruleset: str = Field(alias="Ruleset")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    target_table: Optional[DataQualityTargetTableModel] = Field(
        default=None, alias="TargetTable"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DataQualityRulesetFilterCriteriaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    last_modified_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedBefore"
    )
    last_modified_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedAfter"
    )
    target_table: Optional[DataQualityTargetTableModel] = Field(
        default=None, alias="TargetTable"
    )


class DataQualityRulesetListDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    target_table: Optional[DataQualityTargetTableModel] = Field(
        default=None, alias="TargetTable"
    )
    recommendation_run_id: Optional[str] = Field(
        default=None, alias="RecommendationRunId"
    )
    rule_count: Optional[int] = Field(default=None, alias="RuleCount")


class GetDataQualityRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    ruleset: str = Field(alias="Ruleset")
    target_table: DataQualityTargetTableModel = Field(alias="TargetTable")
    created_on: datetime = Field(alias="CreatedOn")
    last_modified_on: datetime = Field(alias="LastModifiedOn")
    recommendation_run_id: str = Field(alias="RecommendationRunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSourceModel(BaseModel):
    glue_table: GlueTableModel = Field(alias="GlueTable")


class CreatePartitionIndexRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_index: PartitionIndexModel = Field(alias="PartitionIndex")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class CreateSchemaInputRequestModel(BaseModel):
    schema_name: str = Field(alias="SchemaName")
    data_format: Literal["AVRO", "JSON", "PROTOBUF"] = Field(alias="DataFormat")
    registry_id: Optional[RegistryIdModel] = Field(default=None, alias="RegistryId")
    compatibility: Optional[
        Literal[
            "BACKWARD",
            "BACKWARD_ALL",
            "DISABLED",
            "FORWARD",
            "FORWARD_ALL",
            "FULL",
            "FULL_ALL",
            "NONE",
        ]
    ] = Field(default=None, alias="Compatibility")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    schema_definition: Optional[str] = Field(default=None, alias="SchemaDefinition")


class DeleteRegistryInputRequestModel(BaseModel):
    registry_id: RegistryIdModel = Field(alias="RegistryId")


class GetRegistryInputRequestModel(BaseModel):
    registry_id: RegistryIdModel = Field(alias="RegistryId")


class ListSchemasInputRequestModel(BaseModel):
    registry_id: Optional[RegistryIdModel] = Field(default=None, alias="RegistryId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateRegistryInputRequestModel(BaseModel):
    registry_id: RegistryIdModel = Field(alias="RegistryId")
    description: str = Field(alias="Description")


class CreateSessionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    role: str = Field(alias="Role")
    command: SessionCommandModel = Field(alias="Command")
    description: Optional[str] = Field(default=None, alias="Description")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    idle_timeout: Optional[int] = Field(default=None, alias="IdleTimeout")
    default_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="DefaultArguments"
    )
    connections: Optional[ConnectionsListModel] = Field(
        default=None, alias="Connections"
    )
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    request_origin: Optional[str] = Field(default=None, alias="RequestOrigin")


class SessionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    status: Optional[
        Literal["FAILED", "PROVISIONING", "READY", "STOPPED", "STOPPING", "TIMEOUT"]
    ] = Field(default=None, alias="Status")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    description: Optional[str] = Field(default=None, alias="Description")
    role: Optional[str] = Field(default=None, alias="Role")
    command: Optional[SessionCommandModel] = Field(default=None, alias="Command")
    default_arguments: Optional[Dict[str, str]] = Field(
        default=None, alias="DefaultArguments"
    )
    connections: Optional[ConnectionsListModel] = Field(
        default=None, alias="Connections"
    )
    progress: Optional[float] = Field(default=None, alias="Progress")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")


class EvaluateDataQualityModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    ruleset: str = Field(alias="Ruleset")
    output: Optional[Literal["EvaluationResults", "PrimaryInput"]] = Field(
        default=None, alias="Output"
    )
    publishing_options: Optional[DQResultsPublishingOptionsModel] = Field(
        default=None, alias="PublishingOptions"
    )
    stop_job_on_failure_options: Optional[DQStopJobOnFailureOptionsModel] = Field(
        default=None, alias="StopJobOnFailureOptions"
    )


class DataCatalogEncryptionSettingsModel(BaseModel):
    encryption_at_rest: Optional[EncryptionAtRestModel] = Field(
        default=None, alias="EncryptionAtRest"
    )
    connection_password_encryption: Optional[ConnectionPasswordEncryptionModel] = Field(
        default=None, alias="ConnectionPasswordEncryption"
    )


class PrincipalPermissionsModel(BaseModel):
    principal: Optional[DataLakePrincipalModel] = Field(default=None, alias="Principal")
    permissions: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")


class NullValueFieldModel(BaseModel):
    value: str = Field(alias="Value")
    datatype: DatatypeModel = Field(alias="Datatype")


class DecimalColumnStatisticsDataModel(BaseModel):
    number_of_nulls: int = Field(alias="NumberOfNulls")
    number_of_distinct_values: int = Field(alias="NumberOfDistinctValues")
    minimum_value: Optional[DecimalNumberModel] = Field(
        default=None, alias="MinimumValue"
    )
    maximum_value: Optional[DecimalNumberModel] = Field(
        default=None, alias="MaximumValue"
    )


class DeleteSchemaInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")


class DeleteSchemaVersionsInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    versions: str = Field(alias="Versions")


class GetSchemaByDefinitionInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    schema_definition: str = Field(alias="SchemaDefinition")


class GetSchemaInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")


class ListSchemaVersionsInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RegisterSchemaVersionInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    schema_definition: str = Field(alias="SchemaDefinition")


class SchemaReferenceModel(BaseModel):
    schema_id: Optional[SchemaIdModel] = Field(default=None, alias="SchemaId")
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")
    schema_version_number: Optional[int] = Field(
        default=None, alias="SchemaVersionNumber"
    )


class UpdateDevEndpointRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    add_public_keys: Optional[Sequence[str]] = Field(
        default=None, alias="AddPublicKeys"
    )
    delete_public_keys: Optional[Sequence[str]] = Field(
        default=None, alias="DeletePublicKeys"
    )
    custom_libraries: Optional[DevEndpointCustomLibrariesModel] = Field(
        default=None, alias="CustomLibraries"
    )
    update_etl_libraries: Optional[bool] = Field(
        default=None, alias="UpdateEtlLibraries"
    )
    delete_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="DeleteArguments"
    )
    add_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="AddArguments"
    )


class S3DeltaDirectTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    path: str = Field(alias="Path")
    compression: Literal["snappy", "uncompressed"] = Field(alias="Compression")
    format: Literal["avro", "csv", "delta", "hudi", "json", "orc", "parquet"] = Field(
        alias="Format"
    )
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )
    schema_change_policy: Optional[DirectSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3DirectTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    path: str = Field(alias="Path")
    format: Literal["avro", "csv", "delta", "hudi", "json", "orc", "parquet"] = Field(
        alias="Format"
    )
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    compression: Optional[str] = Field(default=None, alias="Compression")
    schema_change_policy: Optional[DirectSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3GlueParquetTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    path: str = Field(alias="Path")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    compression: Optional[
        Literal["gzip", "lzo", "none", "snappy", "uncompressed"]
    ] = Field(default=None, alias="Compression")
    schema_change_policy: Optional[DirectSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class S3HudiDirectTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    path: str = Field(alias="Path")
    compression: Literal["gzip", "lzo", "snappy", "uncompressed"] = Field(
        alias="Compression"
    )
    format: Literal["avro", "csv", "delta", "hudi", "json", "orc", "parquet"] = Field(
        alias="Format"
    )
    additional_options: Dict[str, str] = Field(alias="AdditionalOptions")
    partition_keys: Optional[List[List[str]]] = Field(
        default=None, alias="PartitionKeys"
    )
    schema_change_policy: Optional[DirectSchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )


class DynamicTransformModel(BaseModel):
    name: str = Field(alias="Name")
    transform_name: str = Field(alias="TransformName")
    inputs: List[str] = Field(alias="Inputs")
    function_name: str = Field(alias="FunctionName")
    path: str = Field(alias="Path")
    parameters: Optional[List[TransformConfigParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class EncryptionConfigurationModel(BaseModel):
    s3_encryption: Optional[Sequence[S3EncryptionModel]] = Field(
        default=None, alias="S3Encryption"
    )
    cloud_watch_encryption: Optional[CloudWatchEncryptionModel] = Field(
        default=None, alias="CloudWatchEncryption"
    )
    job_bookmarks_encryption: Optional[JobBookmarksEncryptionModel] = Field(
        default=None, alias="JobBookmarksEncryption"
    )


class SchemaVersionErrorItemModel(BaseModel):
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    error_details: Optional[ErrorDetailsModel] = Field(
        default=None, alias="ErrorDetails"
    )


class FilterExpressionModel(BaseModel):
    operation: Literal["EQ", "GT", "GTE", "ISNULL", "LT", "LTE", "REGEX"] = Field(
        alias="Operation"
    )
    values: List[FilterValueModel] = Field(alias="Values")
    negated: Optional[bool] = Field(default=None, alias="Negated")


class TransformParametersModel(BaseModel):
    transform_type: Literal["FIND_MATCHES"] = Field(alias="TransformType")
    find_matches_parameters: Optional[FindMatchesParametersModel] = Field(
        default=None, alias="FindMatchesParameters"
    )


class GetClassifiersRequestGetClassifiersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCrawlerMetricsRequestGetCrawlerMetricsPaginateModel(BaseModel):
    crawler_name_list: Optional[Sequence[str]] = Field(
        default=None, alias="CrawlerNameList"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCrawlersRequestGetCrawlersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDatabasesRequestGetDatabasesPaginateModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    resource_share_type: Optional[Literal["ALL", "FOREIGN"]] = Field(
        default=None, alias="ResourceShareType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDevEndpointsRequestGetDevEndpointsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetJobRunsRequestGetJobRunsPaginateModel(BaseModel):
    job_name: str = Field(alias="JobName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetJobsRequestGetJobsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetPartitionIndexesRequestGetPartitionIndexesPaginateModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourcePoliciesRequestGetResourcePoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTableVersionsRequestGetTableVersionsPaginateModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTablesRequestGetTablesPaginateModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    expression: Optional[str] = Field(default=None, alias="Expression")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTriggersRequestGetTriggersPaginateModel(BaseModel):
    dependent_job_name: Optional[str] = Field(default=None, alias="DependentJobName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateModel(BaseModel):
    pattern: str = Field(alias="Pattern")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRegistriesInputListRegistriesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemaVersionsInputListSchemaVersionsPaginateModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemasInputListSchemasPaginateModel(BaseModel):
    registry_id: Optional[RegistryIdModel] = Field(default=None, alias="RegistryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetConnectionsRequestGetConnectionsPaginateModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    filter: Optional[GetConnectionsFilterModel] = Field(default=None, alias="Filter")
    hide_password: Optional[bool] = Field(default=None, alias="HidePassword")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetConnectionsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    filter: Optional[GetConnectionsFilterModel] = Field(default=None, alias="Filter")
    hide_password: Optional[bool] = Field(default=None, alias="HidePassword")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetJobBookmarkResponseModel(BaseModel):
    job_bookmark_entry: JobBookmarkEntryModel = Field(alias="JobBookmarkEntry")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetJobBookmarkResponseModel(BaseModel):
    job_bookmark_entry: JobBookmarkEntryModel = Field(alias="JobBookmarkEntry")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMLTaskRunsRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filter: Optional[TaskRunFilterCriteriaModel] = Field(default=None, alias="Filter")
    sort: Optional[TaskRunSortCriteriaModel] = Field(default=None, alias="Sort")


class TransformFilterCriteriaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    transform_type: Optional[Literal["FIND_MATCHES"]] = Field(
        default=None, alias="TransformType"
    )
    status: Optional[Literal["DELETING", "NOT_READY", "READY"]] = Field(
        default=None, alias="Status"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    last_modified_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedBefore"
    )
    last_modified_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastModifiedAfter"
    )
    schema_: Optional[Sequence[SchemaColumnModel]] = Field(default=None, alias="Schema")


class GetMappingResponseModel(BaseModel):
    mapping: List[MappingEntryModel] = Field(alias="Mapping")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPartitionsRequestGetPartitionsPaginateModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    expression: Optional[str] = Field(default=None, alias="Expression")
    segment: Optional[SegmentModel] = Field(default=None, alias="Segment")
    exclude_column_schema: Optional[bool] = Field(
        default=None, alias="ExcludeColumnSchema"
    )
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetPartitionsRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    expression: Optional[str] = Field(default=None, alias="Expression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    segment: Optional[SegmentModel] = Field(default=None, alias="Segment")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    exclude_column_schema: Optional[bool] = Field(
        default=None, alias="ExcludeColumnSchema"
    )
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )


class GetUnfilteredPartitionsMetadataRequestModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    supported_permission_types: Sequence[
        Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
    ] = Field(alias="SupportedPermissionTypes")
    expression: Optional[str] = Field(default=None, alias="Expression")
    audit_context: Optional[AuditContextModel] = Field(
        default=None, alias="AuditContext"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    segment: Optional[SegmentModel] = Field(default=None, alias="Segment")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetResourcePoliciesResponseModel(BaseModel):
    get_resource_policies_response_list: List[GluePolicyModel] = Field(
        alias="GetResourcePoliciesResponseList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaVersionInputRequestModel(BaseModel):
    schema_id: Optional[SchemaIdModel] = Field(default=None, alias="SchemaId")
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")
    schema_version_number: Optional[SchemaVersionNumberModel] = Field(
        default=None, alias="SchemaVersionNumber"
    )


class GetSchemaVersionsDiffInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    first_schema_version_number: SchemaVersionNumberModel = Field(
        alias="FirstSchemaVersionNumber"
    )
    second_schema_version_number: SchemaVersionNumberModel = Field(
        alias="SecondSchemaVersionNumber"
    )
    schema_diff_type: Literal["SYNTAX_DIFF"] = Field(alias="SchemaDiffType")


class UpdateSchemaInputRequestModel(BaseModel):
    schema_id: SchemaIdModel = Field(alias="SchemaId")
    schema_version_number: Optional[SchemaVersionNumberModel] = Field(
        default=None, alias="SchemaVersionNumber"
    )
    compatibility: Optional[
        Literal[
            "BACKWARD",
            "BACKWARD_ALL",
            "DISABLED",
            "FORWARD",
            "FORWARD_ALL",
            "FULL",
            "FULL_ALL",
            "NONE",
        ]
    ] = Field(default=None, alias="Compatibility")
    description: Optional[str] = Field(default=None, alias="Description")


class GlueSchemaModel(BaseModel):
    columns: Optional[List[GlueStudioSchemaColumnModel]] = Field(
        default=None, alias="Columns"
    )


class GovernedCatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    partition_predicate: Optional[str] = Field(default=None, alias="PartitionPredicate")
    additional_options: Optional[S3SourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )


class S3CatalogSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    partition_predicate: Optional[str] = Field(default=None, alias="PartitionPredicate")
    additional_options: Optional[S3SourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )


class JobRunModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    attempt: Optional[int] = Field(default=None, alias="Attempt")
    previous_run_id: Optional[str] = Field(default=None, alias="PreviousRunId")
    trigger_name: Optional[str] = Field(default=None, alias="TriggerName")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    job_run_state: Optional[
        Literal[
            "ERROR",
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
            "WAITING",
        ]
    ] = Field(default=None, alias="JobRunState")
    arguments: Optional[Dict[str, str]] = Field(default=None, alias="Arguments")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    predecessor_runs: Optional[List[PredecessorModel]] = Field(
        default=None, alias="PredecessorRuns"
    )
    allocated_capacity: Optional[int] = Field(default=None, alias="AllocatedCapacity")
    execution_time: Optional[int] = Field(default=None, alias="ExecutionTime")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    dp_useconds: Optional[float] = Field(default=None, alias="DPUSeconds")
    execution_class: Optional[Literal["FLEX", "STANDARD"]] = Field(
        default=None, alias="ExecutionClass"
    )


class JoinModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    join_type: Literal[
        "equijoin", "left", "leftanti", "leftsemi", "outer", "right"
    ] = Field(alias="JoinType")
    columns: List[JoinColumnModel] = Field(alias="Columns")


class TaskRunPropertiesModel(BaseModel):
    task_type: Optional[
        Literal[
            "EVALUATION",
            "EXPORT_LABELS",
            "FIND_MATCHES",
            "IMPORT_LABELS",
            "LABELING_SET_GENERATION",
        ]
    ] = Field(default=None, alias="TaskType")
    import_labels_task_run_properties: Optional[
        ImportLabelsTaskRunPropertiesModel
    ] = Field(default=None, alias="ImportLabelsTaskRunProperties")
    export_labels_task_run_properties: Optional[
        ExportLabelsTaskRunPropertiesModel
    ] = Field(default=None, alias="ExportLabelsTaskRunProperties")
    labeling_set_generation_task_run_properties: Optional[
        LabelingSetGenerationTaskRunPropertiesModel
    ] = Field(default=None, alias="LabelingSetGenerationTaskRunProperties")
    find_matches_task_run_properties: Optional[
        FindMatchesTaskRunPropertiesModel
    ] = Field(default=None, alias="FindMatchesTaskRunProperties")


class ListRegistriesResponseModel(BaseModel):
    registries: List[RegistryListItemModel] = Field(alias="Registries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemaVersionsResponseModel(BaseModel):
    schemas: List[SchemaVersionListItemModel] = Field(alias="Schemas")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemasResponseModel(BaseModel):
    schemas: List[SchemaListItemModel] = Field(alias="Schemas")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransformEncryptionModel(BaseModel):
    ml_user_data_encryption: Optional[MLUserDataEncryptionModel] = Field(
        default=None, alias="MlUserDataEncryption"
    )
    task_run_security_configuration_name: Optional[str] = Field(
        default=None, alias="TaskRunSecurityConfigurationName"
    )


class MetadataInfoModel(BaseModel):
    metadata_value: Optional[str] = Field(default=None, alias="MetadataValue")
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    other_metadata_value_list: Optional[List[OtherMetadataValueListItemModel]] = Field(
        default=None, alias="OtherMetadataValueList"
    )


class PutSchemaVersionMetadataInputRequestModel(BaseModel):
    metadata_key_value: MetadataKeyValuePairModel = Field(alias="MetadataKeyValue")
    schema_id: Optional[SchemaIdModel] = Field(default=None, alias="SchemaId")
    schema_version_number: Optional[SchemaVersionNumberModel] = Field(
        default=None, alias="SchemaVersionNumber"
    )
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")


class QuerySchemaVersionMetadataInputRequestModel(BaseModel):
    schema_id: Optional[SchemaIdModel] = Field(default=None, alias="SchemaId")
    schema_version_number: Optional[SchemaVersionNumberModel] = Field(
        default=None, alias="SchemaVersionNumber"
    )
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")
    metadata_list: Optional[Sequence[MetadataKeyValuePairModel]] = Field(
        default=None, alias="MetadataList"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RemoveSchemaVersionMetadataInputRequestModel(BaseModel):
    metadata_key_value: MetadataKeyValuePairModel = Field(alias="MetadataKeyValue")
    schema_id: Optional[SchemaIdModel] = Field(default=None, alias="SchemaId")
    schema_version_number: Optional[SchemaVersionNumberModel] = Field(
        default=None, alias="SchemaVersionNumber"
    )
    schema_version_id: Optional[str] = Field(default=None, alias="SchemaVersionId")


class RedshiftTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    redshift_tmp_dir: Optional[str] = Field(default=None, alias="RedshiftTmpDir")
    tmp_dir_iamrole: Optional[str] = Field(default=None, alias="TmpDirIAMRole")
    upsert_redshift_options: Optional[UpsertRedshiftTargetOptionsModel] = Field(
        default=None, alias="UpsertRedshiftOptions"
    )


class UserDefinedFunctionInputModel(BaseModel):
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    class_name: Optional[str] = Field(default=None, alias="ClassName")
    owner_name: Optional[str] = Field(default=None, alias="OwnerName")
    owner_type: Optional[Literal["GROUP", "ROLE", "USER"]] = Field(
        default=None, alias="OwnerType"
    )
    resource_uris: Optional[Sequence[ResourceUriModel]] = Field(
        default=None, alias="ResourceUris"
    )


class UserDefinedFunctionModel(BaseModel):
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    class_name: Optional[str] = Field(default=None, alias="ClassName")
    owner_name: Optional[str] = Field(default=None, alias="OwnerName")
    owner_type: Optional[Literal["GROUP", "ROLE", "USER"]] = Field(
        default=None, alias="OwnerType"
    )
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    resource_uris: Optional[List[ResourceUriModel]] = Field(
        default=None, alias="ResourceUris"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class SearchTablesRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[PropertyPredicateModel]] = Field(
        default=None, alias="Filters"
    )
    search_text: Optional[str] = Field(default=None, alias="SearchText")
    sort_criteria: Optional[Sequence[SortCriterionModel]] = Field(
        default=None, alias="SortCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    resource_share_type: Optional[Literal["ALL", "FOREIGN"]] = Field(
        default=None, alias="ResourceShareType"
    )


class StatementOutputModel(BaseModel):
    data: Optional[StatementOutputDataModel] = Field(default=None, alias="Data")
    execution_count: Optional[int] = Field(default=None, alias="ExecutionCount")
    status: Optional[
        Literal["AVAILABLE", "CANCELLED", "CANCELLING", "ERROR", "RUNNING", "WAITING"]
    ] = Field(default=None, alias="Status")
    error_name: Optional[str] = Field(default=None, alias="ErrorName")
    error_value: Optional[str] = Field(default=None, alias="ErrorValue")
    traceback: Optional[List[str]] = Field(default=None, alias="Traceback")


class UpdateClassifierRequestModel(BaseModel):
    grok_classifier: Optional[UpdateGrokClassifierRequestModel] = Field(
        default=None, alias="GrokClassifier"
    )
    xml_classifier: Optional[UpdateXMLClassifierRequestModel] = Field(
        default=None, alias="XMLClassifier"
    )
    json_classifier: Optional[UpdateJsonClassifierRequestModel] = Field(
        default=None, alias="JsonClassifier"
    )
    csv_classifier: Optional[UpdateCsvClassifierRequestModel] = Field(
        default=None, alias="CsvClassifier"
    )


class PartitionIndexDescriptorModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    keys: List[KeySchemaElementModel] = Field(alias="Keys")
    index_status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(
        alias="IndexStatus"
    )
    backfill_errors: Optional[List[BackfillErrorModel]] = Field(
        default=None, alias="BackfillErrors"
    )


class BatchStopJobRunResponseModel(BaseModel):
    successful_submissions: List[BatchStopJobRunSuccessfulSubmissionModel] = Field(
        alias="SuccessfulSubmissions"
    )
    errors: List[BatchStopJobRunErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePartitionResponseModel(BaseModel):
    errors: List[BatchUpdatePartitionFailureEntryModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreatePartitionResponseModel(BaseModel):
    errors: List[PartitionErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeletePartitionResponseModel(BaseModel):
    errors: List[PartitionErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteTableResponseModel(BaseModel):
    errors: List[TableErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteTableVersionResponseModel(BaseModel):
    errors: List[TableVersionErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetBlueprintsResponseModel(BaseModel):
    blueprints: List[BlueprintModel] = Field(alias="Blueprints")
    missing_blueprints: List[str] = Field(alias="MissingBlueprints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlueprintResponseModel(BaseModel):
    blueprint: BlueprintModel = Field(alias="Blueprint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetClassifierResponseModel(BaseModel):
    classifier: ClassifierModel = Field(alias="Classifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetClassifiersResponseModel(BaseModel):
    classifiers: List[ClassifierModel] = Field(alias="Classifiers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScriptRequestModel(BaseModel):
    dag_nodes: Optional[Sequence[CodeGenNodeModel]] = Field(
        default=None, alias="DagNodes"
    )
    dag_edges: Optional[Sequence[CodeGenEdgeModel]] = Field(
        default=None, alias="DagEdges"
    )
    language: Optional[Literal["PYTHON", "SCALA"]] = Field(
        default=None, alias="Language"
    )


class GetDataflowGraphResponseModel(BaseModel):
    dag_nodes: List[CodeGenNodeModel] = Field(alias="DagNodes")
    dag_edges: List[CodeGenEdgeModel] = Field(alias="DagEdges")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMappingRequestModel(BaseModel):
    source: CatalogEntryModel = Field(alias="Source")
    sinks: Optional[Sequence[CatalogEntryModel]] = Field(default=None, alias="Sinks")
    location: Optional[LocationModel] = Field(default=None, alias="Location")


class GetPlanRequestModel(BaseModel):
    mapping: Sequence[MappingEntryModel] = Field(alias="Mapping")
    source: CatalogEntryModel = Field(alias="Source")
    sinks: Optional[Sequence[CatalogEntryModel]] = Field(default=None, alias="Sinks")
    location: Optional[LocationModel] = Field(default=None, alias="Location")
    language: Optional[Literal["PYTHON", "SCALA"]] = Field(
        default=None, alias="Language"
    )
    additional_plan_options_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="AdditionalPlanOptionsMap"
    )


class CreateTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["CONDITIONAL", "EVENT", "ON_DEMAND", "SCHEDULED"] = Field(
        alias="Type"
    )
    actions: Sequence[ActionModel] = Field(alias="Actions")
    workflow_name: Optional[str] = Field(default=None, alias="WorkflowName")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    predicate: Optional[PredicateModel] = Field(default=None, alias="Predicate")
    description: Optional[str] = Field(default=None, alias="Description")
    start_on_creation: Optional[bool] = Field(default=None, alias="StartOnCreation")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    event_batching_condition: Optional[EventBatchingConditionModel] = Field(
        default=None, alias="EventBatchingCondition"
    )


class TriggerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    workflow_name: Optional[str] = Field(default=None, alias="WorkflowName")
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["CONDITIONAL", "EVENT", "ON_DEMAND", "SCHEDULED"]] = Field(
        default=None, alias="Type"
    )
    state: Optional[
        Literal[
            "ACTIVATED",
            "ACTIVATING",
            "CREATED",
            "CREATING",
            "DEACTIVATED",
            "DEACTIVATING",
            "DELETING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    actions: Optional[List[ActionModel]] = Field(default=None, alias="Actions")
    predicate: Optional[PredicateModel] = Field(default=None, alias="Predicate")
    event_batching_condition: Optional[EventBatchingConditionModel] = Field(
        default=None, alias="EventBatchingCondition"
    )


class TriggerUpdateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="Actions")
    predicate: Optional[PredicateModel] = Field(default=None, alias="Predicate")
    event_batching_condition: Optional[EventBatchingConditionModel] = Field(
        default=None, alias="EventBatchingCondition"
    )


class EvaluationMetricsModel(BaseModel):
    transform_type: Literal["FIND_MATCHES"] = Field(alias="TransformType")
    find_matches_metrics: Optional[FindMatchesMetricsModel] = Field(
        default=None, alias="FindMatchesMetrics"
    )


class CreateConnectionRequestModel(BaseModel):
    connection_input: ConnectionInputModel = Field(alias="ConnectionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateConnectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    connection_input: ConnectionInputModel = Field(alias="ConnectionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectionsResponseModel(BaseModel):
    connection_list: List[ConnectionModel] = Field(alias="ConnectionList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CrawlerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    role: Optional[str] = Field(default=None, alias="Role")
    targets: Optional[CrawlerTargetsModel] = Field(default=None, alias="Targets")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    description: Optional[str] = Field(default=None, alias="Description")
    classifiers: Optional[List[str]] = Field(default=None, alias="Classifiers")
    recrawl_policy: Optional[RecrawlPolicyModel] = Field(
        default=None, alias="RecrawlPolicy"
    )
    schema_change_policy: Optional[SchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )
    lineage_configuration: Optional[LineageConfigurationModel] = Field(
        default=None, alias="LineageConfiguration"
    )
    state: Optional[Literal["READY", "RUNNING", "STOPPING"]] = Field(
        default=None, alias="State"
    )
    table_prefix: Optional[str] = Field(default=None, alias="TablePrefix")
    schedule: Optional[ScheduleModel] = Field(default=None, alias="Schedule")
    crawl_elapsed_time: Optional[int] = Field(default=None, alias="CrawlElapsedTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    last_crawl: Optional[LastCrawlInfoModel] = Field(default=None, alias="LastCrawl")
    version: Optional[int] = Field(default=None, alias="Version")
    configuration: Optional[str] = Field(default=None, alias="Configuration")
    crawler_security_configuration: Optional[str] = Field(
        default=None, alias="CrawlerSecurityConfiguration"
    )
    lake_formation_configuration: Optional[LakeFormationConfigurationModel] = Field(
        default=None, alias="LakeFormationConfiguration"
    )


class CreateCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role: str = Field(alias="Role")
    targets: CrawlerTargetsModel = Field(alias="Targets")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    description: Optional[str] = Field(default=None, alias="Description")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    classifiers: Optional[Sequence[str]] = Field(default=None, alias="Classifiers")
    table_prefix: Optional[str] = Field(default=None, alias="TablePrefix")
    schema_change_policy: Optional[SchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )
    recrawl_policy: Optional[RecrawlPolicyModel] = Field(
        default=None, alias="RecrawlPolicy"
    )
    lineage_configuration: Optional[LineageConfigurationModel] = Field(
        default=None, alias="LineageConfiguration"
    )
    lake_formation_configuration: Optional[LakeFormationConfigurationModel] = Field(
        default=None, alias="LakeFormationConfiguration"
    )
    configuration: Optional[str] = Field(default=None, alias="Configuration")
    crawler_security_configuration: Optional[str] = Field(
        default=None, alias="CrawlerSecurityConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateCrawlerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role: Optional[str] = Field(default=None, alias="Role")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    description: Optional[str] = Field(default=None, alias="Description")
    targets: Optional[CrawlerTargetsModel] = Field(default=None, alias="Targets")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    classifiers: Optional[Sequence[str]] = Field(default=None, alias="Classifiers")
    table_prefix: Optional[str] = Field(default=None, alias="TablePrefix")
    schema_change_policy: Optional[SchemaChangePolicyModel] = Field(
        default=None, alias="SchemaChangePolicy"
    )
    recrawl_policy: Optional[RecrawlPolicyModel] = Field(
        default=None, alias="RecrawlPolicy"
    )
    lineage_configuration: Optional[LineageConfigurationModel] = Field(
        default=None, alias="LineageConfiguration"
    )
    lake_formation_configuration: Optional[LakeFormationConfigurationModel] = Field(
        default=None, alias="LakeFormationConfiguration"
    )
    configuration: Optional[str] = Field(default=None, alias="Configuration")
    crawler_security_configuration: Optional[str] = Field(
        default=None, alias="CrawlerSecurityConfiguration"
    )


class ListDataQualityRulesetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filter: Optional[DataQualityRulesetFilterCriteriaModel] = Field(
        default=None, alias="Filter"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ListDataQualityRulesetsResponseModel(BaseModel):
    rulesets: List[DataQualityRulesetListDetailsModel] = Field(alias="Rulesets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataQualityResultDescriptionModel(BaseModel):
    result_id: Optional[str] = Field(default=None, alias="ResultId")
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")


class DataQualityResultFilterCriteriaModel(BaseModel):
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedAfter"
    )
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedBefore"
    )


class DataQualityResultModel(BaseModel):
    result_id: Optional[str] = Field(default=None, alias="ResultId")
    score: Optional[float] = Field(default=None, alias="Score")
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")
    ruleset_name: Optional[str] = Field(default=None, alias="RulesetName")
    evaluation_context: Optional[str] = Field(default=None, alias="EvaluationContext")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_run_id: Optional[str] = Field(default=None, alias="JobRunId")
    ruleset_evaluation_run_id: Optional[str] = Field(
        default=None, alias="RulesetEvaluationRunId"
    )
    rule_results: Optional[List[DataQualityRuleResultModel]] = Field(
        default=None, alias="RuleResults"
    )


class DataQualityRuleRecommendationRunDescriptionModel(BaseModel):
    run_id: Optional[str] = Field(default=None, alias="RunId")
    status: Optional[
        Literal[
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="Status")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")


class DataQualityRuleRecommendationRunFilterModel(BaseModel):
    data_source: DataSourceModel = Field(alias="DataSource")
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedBefore"
    )
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedAfter"
    )


class DataQualityRulesetEvaluationRunDescriptionModel(BaseModel):
    run_id: Optional[str] = Field(default=None, alias="RunId")
    status: Optional[
        Literal[
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="Status")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    data_source: Optional[DataSourceModel] = Field(default=None, alias="DataSource")


class DataQualityRulesetEvaluationRunFilterModel(BaseModel):
    data_source: DataSourceModel = Field(alias="DataSource")
    started_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedBefore"
    )
    started_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartedAfter"
    )


class GetDataQualityResultResponseModel(BaseModel):
    result_id: str = Field(alias="ResultId")
    score: float = Field(alias="Score")
    data_source: DataSourceModel = Field(alias="DataSource")
    ruleset_name: str = Field(alias="RulesetName")
    evaluation_context: str = Field(alias="EvaluationContext")
    started_on: datetime = Field(alias="StartedOn")
    completed_on: datetime = Field(alias="CompletedOn")
    job_name: str = Field(alias="JobName")
    job_run_id: str = Field(alias="JobRunId")
    ruleset_evaluation_run_id: str = Field(alias="RulesetEvaluationRunId")
    rule_results: List[DataQualityRuleResultModel] = Field(alias="RuleResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataQualityRuleRecommendationRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    data_source: DataSourceModel = Field(alias="DataSource")
    role: str = Field(alias="Role")
    number_of_workers: int = Field(alias="NumberOfWorkers")
    timeout: int = Field(alias="Timeout")
    status: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
    ] = Field(alias="Status")
    error_string: str = Field(alias="ErrorString")
    started_on: datetime = Field(alias="StartedOn")
    last_modified_on: datetime = Field(alias="LastModifiedOn")
    completed_on: datetime = Field(alias="CompletedOn")
    execution_time: int = Field(alias="ExecutionTime")
    recommended_ruleset: str = Field(alias="RecommendedRuleset")
    created_ruleset_name: str = Field(alias="CreatedRulesetName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataQualityRulesetEvaluationRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    data_source: DataSourceModel = Field(alias="DataSource")
    role: str = Field(alias="Role")
    number_of_workers: int = Field(alias="NumberOfWorkers")
    timeout: int = Field(alias="Timeout")
    additional_run_options: DataQualityEvaluationRunAdditionalRunOptionsModel = Field(
        alias="AdditionalRunOptions"
    )
    status: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
    ] = Field(alias="Status")
    error_string: str = Field(alias="ErrorString")
    started_on: datetime = Field(alias="StartedOn")
    last_modified_on: datetime = Field(alias="LastModifiedOn")
    completed_on: datetime = Field(alias="CompletedOn")
    execution_time: int = Field(alias="ExecutionTime")
    ruleset_names: List[str] = Field(alias="RulesetNames")
    result_ids: List[str] = Field(alias="ResultIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataQualityRuleRecommendationRunRequestModel(BaseModel):
    data_source: DataSourceModel = Field(alias="DataSource")
    role: str = Field(alias="Role")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    created_ruleset_name: Optional[str] = Field(
        default=None, alias="CreatedRulesetName"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class StartDataQualityRulesetEvaluationRunRequestModel(BaseModel):
    data_source: DataSourceModel = Field(alias="DataSource")
    role: str = Field(alias="Role")
    ruleset_names: Sequence[str] = Field(alias="RulesetNames")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    additional_run_options: Optional[
        DataQualityEvaluationRunAdditionalRunOptionsModel
    ] = Field(default=None, alias="AdditionalRunOptions")


class CreateSessionResponseModel(BaseModel):
    session: SessionModel = Field(alias="Session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSessionResponseModel(BaseModel):
    session: SessionModel = Field(alias="Session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSessionsResponseModel(BaseModel):
    ids: List[str] = Field(alias="Ids")
    sessions: List[SessionModel] = Field(alias="Sessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataCatalogEncryptionSettingsResponseModel(BaseModel):
    data_catalog_encryption_settings: DataCatalogEncryptionSettingsModel = Field(
        alias="DataCatalogEncryptionSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDataCatalogEncryptionSettingsRequestModel(BaseModel):
    data_catalog_encryption_settings: DataCatalogEncryptionSettingsModel = Field(
        alias="DataCatalogEncryptionSettings"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DatabaseInputModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    location_uri: Optional[str] = Field(default=None, alias="LocationUri")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    create_table_default_permissions: Optional[
        Sequence[PrincipalPermissionsModel]
    ] = Field(default=None, alias="CreateTableDefaultPermissions")
    target_database: Optional[DatabaseIdentifierModel] = Field(
        default=None, alias="TargetDatabase"
    )


class DatabaseModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    location_uri: Optional[str] = Field(default=None, alias="LocationUri")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    create_table_default_permissions: Optional[List[PrincipalPermissionsModel]] = Field(
        default=None, alias="CreateTableDefaultPermissions"
    )
    target_database: Optional[DatabaseIdentifierModel] = Field(
        default=None, alias="TargetDatabase"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DropNullFieldsModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    null_check_box_list: Optional[NullCheckBoxListModel] = Field(
        default=None, alias="NullCheckBoxList"
    )
    null_text_list: Optional[List[NullValueFieldModel]] = Field(
        default=None, alias="NullTextList"
    )


class ColumnStatisticsDataModel(BaseModel):
    type: Literal[
        "BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING"
    ] = Field(alias="Type")
    boolean_column_statistics_data: Optional[BooleanColumnStatisticsDataModel] = Field(
        default=None, alias="BooleanColumnStatisticsData"
    )
    date_column_statistics_data: Optional[DateColumnStatisticsDataModel] = Field(
        default=None, alias="DateColumnStatisticsData"
    )
    decimal_column_statistics_data: Optional[DecimalColumnStatisticsDataModel] = Field(
        default=None, alias="DecimalColumnStatisticsData"
    )
    double_column_statistics_data: Optional[DoubleColumnStatisticsDataModel] = Field(
        default=None, alias="DoubleColumnStatisticsData"
    )
    long_column_statistics_data: Optional[LongColumnStatisticsDataModel] = Field(
        default=None, alias="LongColumnStatisticsData"
    )
    string_column_statistics_data: Optional[StringColumnStatisticsDataModel] = Field(
        default=None, alias="StringColumnStatisticsData"
    )
    binary_column_statistics_data: Optional[BinaryColumnStatisticsDataModel] = Field(
        default=None, alias="BinaryColumnStatisticsData"
    )


class StorageDescriptorModel(BaseModel):
    columns: Optional[Sequence[ColumnModel]] = Field(default=None, alias="Columns")
    location: Optional[str] = Field(default=None, alias="Location")
    additional_locations: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalLocations"
    )
    input_format: Optional[str] = Field(default=None, alias="InputFormat")
    output_format: Optional[str] = Field(default=None, alias="OutputFormat")
    compressed: Optional[bool] = Field(default=None, alias="Compressed")
    number_of_buckets: Optional[int] = Field(default=None, alias="NumberOfBuckets")
    serde_info: Optional[SerDeInfoModel] = Field(default=None, alias="SerdeInfo")
    bucket_columns: Optional[Sequence[str]] = Field(default=None, alias="BucketColumns")
    sort_columns: Optional[Sequence[OrderModel]] = Field(
        default=None, alias="SortColumns"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    skewed_info: Optional[SkewedInfoModel] = Field(default=None, alias="SkewedInfo")
    stored_as_sub_directories: Optional[bool] = Field(
        default=None, alias="StoredAsSubDirectories"
    )
    schema_reference: Optional[SchemaReferenceModel] = Field(
        default=None, alias="SchemaReference"
    )


class CreateSecurityConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    encryption_configuration: EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )


class SecurityConfigurationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    created_time_stamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimeStamp"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class DeleteSchemaVersionsResponseModel(BaseModel):
    schema_version_errors: List[SchemaVersionErrorItemModel] = Field(
        alias="SchemaVersionErrors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    logical_operator: Literal["AND", "OR"] = Field(alias="LogicalOperator")
    filters: List[FilterExpressionModel] = Field(alias="Filters")


class UpdateMLTransformRequestModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[TransformParametersModel] = Field(
        default=None, alias="Parameters"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")


class GetMLTransformsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filter: Optional[TransformFilterCriteriaModel] = Field(default=None, alias="Filter")
    sort: Optional[TransformSortCriteriaModel] = Field(default=None, alias="Sort")


class ListMLTransformsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filter: Optional[TransformFilterCriteriaModel] = Field(default=None, alias="Filter")
    sort: Optional[TransformSortCriteriaModel] = Field(default=None, alias="Sort")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class AthenaConnectorSourceModel(BaseModel):
    name: str = Field(alias="Name")
    connection_name: str = Field(alias="ConnectionName")
    connector_name: str = Field(alias="ConnectorName")
    connection_type: str = Field(alias="ConnectionType")
    schema_name: str = Field(alias="SchemaName")
    connection_table: Optional[str] = Field(default=None, alias="ConnectionTable")
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class CatalogDeltaSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    additional_delta_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalDeltaOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class CatalogHudiSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    additional_hudi_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalHudiOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class CustomCodeModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    code: str = Field(alias="Code")
    class_name: str = Field(alias="ClassName")
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class JDBCConnectorSourceModel(BaseModel):
    name: str = Field(alias="Name")
    connection_name: str = Field(alias="ConnectionName")
    connector_name: str = Field(alias="ConnectorName")
    connection_type: str = Field(alias="ConnectionType")
    additional_options: Optional[JDBCConnectorOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    connection_table: Optional[str] = Field(default=None, alias="ConnectionTable")
    query: Optional[str] = Field(default=None, alias="Query")
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class JDBCConnectorTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    connection_name: str = Field(alias="ConnectionName")
    connection_table: str = Field(alias="ConnectionTable")
    connector_name: str = Field(alias="ConnectorName")
    connection_type: str = Field(alias="ConnectionType")
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3CatalogDeltaSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    additional_delta_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalDeltaOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3CatalogHudiSourceModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    table: str = Field(alias="Table")
    additional_hudi_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalHudiOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3CsvSourceModel(BaseModel):
    name: str = Field(alias="Name")
    paths: List[str] = Field(alias="Paths")
    separator: Literal["comma", "ctrla", "pipe", "semicolon", "tab"] = Field(
        alias="Separator"
    )
    quote_char: Literal["disabled", "quillemet", "quote", "single_quote"] = Field(
        alias="QuoteChar"
    )
    compression_type: Optional[Literal["bzip2", "gzip"]] = Field(
        default=None, alias="CompressionType"
    )
    exclusions: Optional[List[str]] = Field(default=None, alias="Exclusions")
    group_size: Optional[str] = Field(default=None, alias="GroupSize")
    group_files: Optional[str] = Field(default=None, alias="GroupFiles")
    recurse: Optional[bool] = Field(default=None, alias="Recurse")
    max_band: Optional[int] = Field(default=None, alias="MaxBand")
    max_files_in_band: Optional[int] = Field(default=None, alias="MaxFilesInBand")
    additional_options: Optional[S3DirectSourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    escaper: Optional[str] = Field(default=None, alias="Escaper")
    multiline: Optional[bool] = Field(default=None, alias="Multiline")
    with_header: Optional[bool] = Field(default=None, alias="WithHeader")
    write_header: Optional[bool] = Field(default=None, alias="WriteHeader")
    skip_first: Optional[bool] = Field(default=None, alias="SkipFirst")
    optimize_performance: Optional[bool] = Field(
        default=None, alias="OptimizePerformance"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3DeltaSourceModel(BaseModel):
    name: str = Field(alias="Name")
    paths: List[str] = Field(alias="Paths")
    additional_delta_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalDeltaOptions"
    )
    additional_options: Optional[S3DirectSourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3HudiSourceModel(BaseModel):
    name: str = Field(alias="Name")
    paths: List[str] = Field(alias="Paths")
    additional_hudi_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalHudiOptions"
    )
    additional_options: Optional[S3DirectSourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3JsonSourceModel(BaseModel):
    name: str = Field(alias="Name")
    paths: List[str] = Field(alias="Paths")
    compression_type: Optional[Literal["bzip2", "gzip"]] = Field(
        default=None, alias="CompressionType"
    )
    exclusions: Optional[List[str]] = Field(default=None, alias="Exclusions")
    group_size: Optional[str] = Field(default=None, alias="GroupSize")
    group_files: Optional[str] = Field(default=None, alias="GroupFiles")
    recurse: Optional[bool] = Field(default=None, alias="Recurse")
    max_band: Optional[int] = Field(default=None, alias="MaxBand")
    max_files_in_band: Optional[int] = Field(default=None, alias="MaxFilesInBand")
    additional_options: Optional[S3DirectSourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    json_path: Optional[str] = Field(default=None, alias="JsonPath")
    multiline: Optional[bool] = Field(default=None, alias="Multiline")
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class S3ParquetSourceModel(BaseModel):
    name: str = Field(alias="Name")
    paths: List[str] = Field(alias="Paths")
    compression_type: Optional[
        Literal["gzip", "lzo", "none", "snappy", "uncompressed"]
    ] = Field(default=None, alias="CompressionType")
    exclusions: Optional[List[str]] = Field(default=None, alias="Exclusions")
    group_size: Optional[str] = Field(default=None, alias="GroupSize")
    group_files: Optional[str] = Field(default=None, alias="GroupFiles")
    recurse: Optional[bool] = Field(default=None, alias="Recurse")
    max_band: Optional[int] = Field(default=None, alias="MaxBand")
    max_files_in_band: Optional[int] = Field(default=None, alias="MaxFilesInBand")
    additional_options: Optional[S3DirectSourceAdditionalOptionsModel] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class SparkConnectorSourceModel(BaseModel):
    name: str = Field(alias="Name")
    connection_name: str = Field(alias="ConnectionName")
    connector_name: str = Field(alias="ConnectorName")
    connection_type: str = Field(alias="ConnectionType")
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class SparkConnectorTargetModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    connection_name: str = Field(alias="ConnectionName")
    connector_name: str = Field(alias="ConnectorName")
    connection_type: str = Field(alias="ConnectionType")
    additional_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalOptions"
    )
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class SparkSQLModel(BaseModel):
    name: str = Field(alias="Name")
    inputs: List[str] = Field(alias="Inputs")
    sql_query: str = Field(alias="SqlQuery")
    sql_aliases: List[SqlAliasModel] = Field(alias="SqlAliases")
    output_schemas: Optional[List[GlueSchemaModel]] = Field(
        default=None, alias="OutputSchemas"
    )


class GetJobRunResponseModel(BaseModel):
    job_run: JobRunModel = Field(alias="JobRun")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobRunsResponseModel(BaseModel):
    job_runs: List[JobRunModel] = Field(alias="JobRuns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobNodeDetailsModel(BaseModel):
    job_runs: Optional[List[JobRunModel]] = Field(default=None, alias="JobRuns")


class GetMLTaskRunResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    task_run_id: str = Field(alias="TaskRunId")
    status: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
    ] = Field(alias="Status")
    log_group_name: str = Field(alias="LogGroupName")
    properties: TaskRunPropertiesModel = Field(alias="Properties")
    error_string: str = Field(alias="ErrorString")
    started_on: datetime = Field(alias="StartedOn")
    last_modified_on: datetime = Field(alias="LastModifiedOn")
    completed_on: datetime = Field(alias="CompletedOn")
    execution_time: int = Field(alias="ExecutionTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaskRunModel(BaseModel):
    transform_id: Optional[str] = Field(default=None, alias="TransformId")
    task_run_id: Optional[str] = Field(default=None, alias="TaskRunId")
    status: Optional[
        Literal[
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="Status")
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    properties: Optional[TaskRunPropertiesModel] = Field(
        default=None, alias="Properties"
    )
    error_string: Optional[str] = Field(default=None, alias="ErrorString")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    execution_time: Optional[int] = Field(default=None, alias="ExecutionTime")


class CreateMLTransformRequestModel(BaseModel):
    name: str = Field(alias="Name")
    input_record_tables: Sequence[GlueTableModel] = Field(alias="InputRecordTables")
    parameters: TransformParametersModel = Field(alias="Parameters")
    role: str = Field(alias="Role")
    description: Optional[str] = Field(default=None, alias="Description")
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    transform_encryption: Optional[TransformEncryptionModel] = Field(
        default=None, alias="TransformEncryption"
    )


class QuerySchemaVersionMetadataResponseModel(BaseModel):
    metadata_info_map: Dict[str, MetadataInfoModel] = Field(alias="MetadataInfoMap")
    schema_version_id: str = Field(alias="SchemaVersionId")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserDefinedFunctionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    function_input: UserDefinedFunctionInputModel = Field(alias="FunctionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class UpdateUserDefinedFunctionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    function_name: str = Field(alias="FunctionName")
    function_input: UserDefinedFunctionInputModel = Field(alias="FunctionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetUserDefinedFunctionResponseModel(BaseModel):
    user_defined_function: UserDefinedFunctionModel = Field(alias="UserDefinedFunction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserDefinedFunctionsResponseModel(BaseModel):
    user_defined_functions: List[UserDefinedFunctionModel] = Field(
        alias="UserDefinedFunctions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StatementModel(BaseModel):
    id: Optional[int] = Field(default=None, alias="Id")
    code: Optional[str] = Field(default=None, alias="Code")
    state: Optional[
        Literal["AVAILABLE", "CANCELLED", "CANCELLING", "ERROR", "RUNNING", "WAITING"]
    ] = Field(default=None, alias="State")
    output: Optional[StatementOutputModel] = Field(default=None, alias="Output")
    progress: Optional[float] = Field(default=None, alias="Progress")
    started_on: Optional[int] = Field(default=None, alias="StartedOn")
    completed_on: Optional[int] = Field(default=None, alias="CompletedOn")


class GetPartitionIndexesResponseModel(BaseModel):
    partition_index_descriptor_list: List[PartitionIndexDescriptorModel] = Field(
        alias="PartitionIndexDescriptorList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetTriggersResponseModel(BaseModel):
    triggers: List[TriggerModel] = Field(alias="Triggers")
    triggers_not_found: List[str] = Field(alias="TriggersNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTriggerResponseModel(BaseModel):
    trigger: TriggerModel = Field(alias="Trigger")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTriggersResponseModel(BaseModel):
    triggers: List[TriggerModel] = Field(alias="Triggers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TriggerNodeDetailsModel(BaseModel):
    trigger: Optional[TriggerModel] = Field(default=None, alias="Trigger")


class UpdateTriggerResponseModel(BaseModel):
    trigger: TriggerModel = Field(alias="Trigger")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTriggerRequestModel(BaseModel):
    name: str = Field(alias="Name")
    trigger_update: TriggerUpdateModel = Field(alias="TriggerUpdate")


class GetMLTransformResponseModel(BaseModel):
    transform_id: str = Field(alias="TransformId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    status: Literal["DELETING", "NOT_READY", "READY"] = Field(alias="Status")
    created_on: datetime = Field(alias="CreatedOn")
    last_modified_on: datetime = Field(alias="LastModifiedOn")
    input_record_tables: List[GlueTableModel] = Field(alias="InputRecordTables")
    parameters: TransformParametersModel = Field(alias="Parameters")
    evaluation_metrics: EvaluationMetricsModel = Field(alias="EvaluationMetrics")
    label_count: int = Field(alias="LabelCount")
    schema_: List[SchemaColumnModel] = Field(alias="Schema")
    role: str = Field(alias="Role")
    glue_version: str = Field(alias="GlueVersion")
    max_capacity: float = Field(alias="MaxCapacity")
    worker_type: Literal["G.025X", "G.1X", "G.2X", "Standard"] = Field(
        alias="WorkerType"
    )
    number_of_workers: int = Field(alias="NumberOfWorkers")
    timeout: int = Field(alias="Timeout")
    max_retries: int = Field(alias="MaxRetries")
    transform_encryption: TransformEncryptionModel = Field(alias="TransformEncryption")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MLTransformModel(BaseModel):
    transform_id: Optional[str] = Field(default=None, alias="TransformId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["DELETING", "NOT_READY", "READY"]] = Field(
        default=None, alias="Status"
    )
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    input_record_tables: Optional[List[GlueTableModel]] = Field(
        default=None, alias="InputRecordTables"
    )
    parameters: Optional[TransformParametersModel] = Field(
        default=None, alias="Parameters"
    )
    evaluation_metrics: Optional[EvaluationMetricsModel] = Field(
        default=None, alias="EvaluationMetrics"
    )
    label_count: Optional[int] = Field(default=None, alias="LabelCount")
    schema_: Optional[List[SchemaColumnModel]] = Field(default=None, alias="Schema")
    role: Optional[str] = Field(default=None, alias="Role")
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    transform_encryption: Optional[TransformEncryptionModel] = Field(
        default=None, alias="TransformEncryption"
    )


class BatchGetCrawlersResponseModel(BaseModel):
    crawlers: List[CrawlerModel] = Field(alias="Crawlers")
    crawlers_not_found: List[str] = Field(alias="CrawlersNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCrawlerResponseModel(BaseModel):
    crawler: CrawlerModel = Field(alias="Crawler")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCrawlersResponseModel(BaseModel):
    crawlers: List[CrawlerModel] = Field(alias="Crawlers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataQualityResultsResponseModel(BaseModel):
    results: List[DataQualityResultDescriptionModel] = Field(alias="Results")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataQualityResultsRequestModel(BaseModel):
    filter: Optional[DataQualityResultFilterCriteriaModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchGetDataQualityResultResponseModel(BaseModel):
    results: List[DataQualityResultModel] = Field(alias="Results")
    results_not_found: List[str] = Field(alias="ResultsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataQualityRuleRecommendationRunsResponseModel(BaseModel):
    runs: List[DataQualityRuleRecommendationRunDescriptionModel] = Field(alias="Runs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataQualityRuleRecommendationRunsRequestModel(BaseModel):
    filter: Optional[DataQualityRuleRecommendationRunFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataQualityRulesetEvaluationRunsResponseModel(BaseModel):
    runs: List[DataQualityRulesetEvaluationRunDescriptionModel] = Field(alias="Runs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataQualityRulesetEvaluationRunsRequestModel(BaseModel):
    filter: Optional[DataQualityRulesetEvaluationRunFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class CreateDatabaseRequestModel(BaseModel):
    database_input: DatabaseInputModel = Field(alias="DatabaseInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateDatabaseRequestModel(BaseModel):
    name: str = Field(alias="Name")
    database_input: DatabaseInputModel = Field(alias="DatabaseInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetDatabaseResponseModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDatabasesResponseModel(BaseModel):
    database_list: List[DatabaseModel] = Field(alias="DatabaseList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ColumnStatisticsModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    column_type: str = Field(alias="ColumnType")
    analyzed_time: datetime = Field(alias="AnalyzedTime")
    statistics_data: ColumnStatisticsDataModel = Field(alias="StatisticsData")


class PartitionInputModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    last_access_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAccessTime"
    )
    storage_descriptor: Optional[StorageDescriptorModel] = Field(
        default=None, alias="StorageDescriptor"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    last_analyzed_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAnalyzedTime"
    )


class PartitionModel(BaseModel):
    values: Optional[List[str]] = Field(default=None, alias="Values")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_access_time: Optional[datetime] = Field(default=None, alias="LastAccessTime")
    storage_descriptor: Optional[StorageDescriptorModel] = Field(
        default=None, alias="StorageDescriptor"
    )
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")
    last_analyzed_time: Optional[datetime] = Field(
        default=None, alias="LastAnalyzedTime"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class TableInputModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    owner: Optional[str] = Field(default=None, alias="Owner")
    last_access_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAccessTime"
    )
    last_analyzed_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAnalyzedTime"
    )
    retention: Optional[int] = Field(default=None, alias="Retention")
    storage_descriptor: Optional[StorageDescriptorModel] = Field(
        default=None, alias="StorageDescriptor"
    )
    partition_keys: Optional[Sequence[ColumnModel]] = Field(
        default=None, alias="PartitionKeys"
    )
    view_original_text: Optional[str] = Field(default=None, alias="ViewOriginalText")
    view_expanded_text: Optional[str] = Field(default=None, alias="ViewExpandedText")
    table_type: Optional[str] = Field(default=None, alias="TableType")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    target_table: Optional[TableIdentifierModel] = Field(
        default=None, alias="TargetTable"
    )


class TableModel(BaseModel):
    name: str = Field(alias="Name")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    description: Optional[str] = Field(default=None, alias="Description")
    owner: Optional[str] = Field(default=None, alias="Owner")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    update_time: Optional[datetime] = Field(default=None, alias="UpdateTime")
    last_access_time: Optional[datetime] = Field(default=None, alias="LastAccessTime")
    last_analyzed_time: Optional[datetime] = Field(
        default=None, alias="LastAnalyzedTime"
    )
    retention: Optional[int] = Field(default=None, alias="Retention")
    storage_descriptor: Optional[StorageDescriptorModel] = Field(
        default=None, alias="StorageDescriptor"
    )
    partition_keys: Optional[List[ColumnModel]] = Field(
        default=None, alias="PartitionKeys"
    )
    view_original_text: Optional[str] = Field(default=None, alias="ViewOriginalText")
    view_expanded_text: Optional[str] = Field(default=None, alias="ViewExpandedText")
    table_type: Optional[str] = Field(default=None, alias="TableType")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    is_registered_with_lake_formation: Optional[bool] = Field(
        default=None, alias="IsRegisteredWithLakeFormation"
    )
    target_table: Optional[TableIdentifierModel] = Field(
        default=None, alias="TargetTable"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class GetSecurityConfigurationResponseModel(BaseModel):
    security_configuration: SecurityConfigurationModel = Field(
        alias="SecurityConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSecurityConfigurationsResponseModel(BaseModel):
    security_configurations: List[SecurityConfigurationModel] = Field(
        alias="SecurityConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CodeGenConfigurationNodeModel(BaseModel):
    athena_connector_source: Optional[AthenaConnectorSourceModel] = Field(
        default=None, alias="AthenaConnectorSource"
    )
    jdbcconnector_source: Optional[JDBCConnectorSourceModel] = Field(
        default=None, alias="JDBCConnectorSource"
    )
    spark_connector_source: Optional[SparkConnectorSourceModel] = Field(
        default=None, alias="SparkConnectorSource"
    )
    catalog_source: Optional[CatalogSourceModel] = Field(
        default=None, alias="CatalogSource"
    )
    redshift_source: Optional[RedshiftSourceModel] = Field(
        default=None, alias="RedshiftSource"
    )
    s3_catalog_source: Optional[S3CatalogSourceModel] = Field(
        default=None, alias="S3CatalogSource"
    )
    s3_csv_source: Optional[S3CsvSourceModel] = Field(default=None, alias="S3CsvSource")
    s3_json_source: Optional[S3JsonSourceModel] = Field(
        default=None, alias="S3JsonSource"
    )
    s3_parquet_source: Optional[S3ParquetSourceModel] = Field(
        default=None, alias="S3ParquetSource"
    )
    relational_catalog_source: Optional[RelationalCatalogSourceModel] = Field(
        default=None, alias="RelationalCatalogSource"
    )
    dynamo_dbcatalog_source: Optional[DynamoDBCatalogSourceModel] = Field(
        default=None, alias="DynamoDBCatalogSource"
    )
    jdbcconnector_target: Optional[JDBCConnectorTargetModel] = Field(
        default=None, alias="JDBCConnectorTarget"
    )
    spark_connector_target: Optional[SparkConnectorTargetModel] = Field(
        default=None, alias="SparkConnectorTarget"
    )
    catalog_target: Optional[BasicCatalogTargetModel] = Field(
        default=None, alias="CatalogTarget"
    )
    redshift_target: Optional[RedshiftTargetModel] = Field(
        default=None, alias="RedshiftTarget"
    )
    s3_catalog_target: Optional[S3CatalogTargetModel] = Field(
        default=None, alias="S3CatalogTarget"
    )
    s3_glue_parquet_target: Optional[S3GlueParquetTargetModel] = Field(
        default=None, alias="S3GlueParquetTarget"
    )
    s3_direct_target: Optional[S3DirectTargetModel] = Field(
        default=None, alias="S3DirectTarget"
    )
    apply_mapping: Optional[ApplyMappingModel] = Field(
        default=None, alias="ApplyMapping"
    )
    select_fields: Optional[SelectFieldsModel] = Field(
        default=None, alias="SelectFields"
    )
    drop_fields: Optional[DropFieldsModel] = Field(default=None, alias="DropFields")
    rename_field: Optional[RenameFieldModel] = Field(default=None, alias="RenameField")
    spigot: Optional[SpigotModel] = Field(default=None, alias="Spigot")
    join: Optional[JoinModel] = Field(default=None, alias="Join")
    split_fields: Optional[SplitFieldsModel] = Field(default=None, alias="SplitFields")
    select_from_collection: Optional[SelectFromCollectionModel] = Field(
        default=None, alias="SelectFromCollection"
    )
    fill_missing_values: Optional[FillMissingValuesModel] = Field(
        default=None, alias="FillMissingValues"
    )
    filter: Optional[FilterModel] = Field(default=None, alias="Filter")
    custom_code: Optional[CustomCodeModel] = Field(default=None, alias="CustomCode")
    spark_s_ql: Optional[SparkSQLModel] = Field(default=None, alias="SparkSQL")
    direct_kinesis_source: Optional[DirectKinesisSourceModel] = Field(
        default=None, alias="DirectKinesisSource"
    )
    direct_kafka_source: Optional[DirectKafkaSourceModel] = Field(
        default=None, alias="DirectKafkaSource"
    )
    catalog_kinesis_source: Optional[CatalogKinesisSourceModel] = Field(
        default=None, alias="CatalogKinesisSource"
    )
    catalog_kafka_source: Optional[CatalogKafkaSourceModel] = Field(
        default=None, alias="CatalogKafkaSource"
    )
    drop_null_fields: Optional[DropNullFieldsModel] = Field(
        default=None, alias="DropNullFields"
    )
    merge: Optional[MergeModel] = Field(default=None, alias="Merge")
    union: Optional[UnionModel] = Field(default=None, alias="Union")
    p_iidetection: Optional[PIIDetectionModel] = Field(
        default=None, alias="PIIDetection"
    )
    aggregate: Optional[AggregateModel] = Field(default=None, alias="Aggregate")
    drop_duplicates: Optional[DropDuplicatesModel] = Field(
        default=None, alias="DropDuplicates"
    )
    governed_catalog_target: Optional[GovernedCatalogTargetModel] = Field(
        default=None, alias="GovernedCatalogTarget"
    )
    governed_catalog_source: Optional[GovernedCatalogSourceModel] = Field(
        default=None, alias="GovernedCatalogSource"
    )
    microsoft_s_ql_server_catalog_source: Optional[
        MicrosoftSQLServerCatalogSourceModel
    ] = Field(default=None, alias="MicrosoftSQLServerCatalogSource")
    my_s_ql_catalog_source: Optional[MySQLCatalogSourceModel] = Field(
        default=None, alias="MySQLCatalogSource"
    )
    oracle_s_ql_catalog_source: Optional[OracleSQLCatalogSourceModel] = Field(
        default=None, alias="OracleSQLCatalogSource"
    )
    postgre_s_ql_catalog_source: Optional[PostgreSQLCatalogSourceModel] = Field(
        default=None, alias="PostgreSQLCatalogSource"
    )
    microsoft_s_ql_server_catalog_target: Optional[
        MicrosoftSQLServerCatalogTargetModel
    ] = Field(default=None, alias="MicrosoftSQLServerCatalogTarget")
    my_s_ql_catalog_target: Optional[MySQLCatalogTargetModel] = Field(
        default=None, alias="MySQLCatalogTarget"
    )
    oracle_s_ql_catalog_target: Optional[OracleSQLCatalogTargetModel] = Field(
        default=None, alias="OracleSQLCatalogTarget"
    )
    postgre_s_ql_catalog_target: Optional[PostgreSQLCatalogTargetModel] = Field(
        default=None, alias="PostgreSQLCatalogTarget"
    )
    dynamic_transform: Optional[DynamicTransformModel] = Field(
        default=None, alias="DynamicTransform"
    )
    evaluate_data_quality: Optional[EvaluateDataQualityModel] = Field(
        default=None, alias="EvaluateDataQuality"
    )
    s3_catalog_hudi_source: Optional[S3CatalogHudiSourceModel] = Field(
        default=None, alias="S3CatalogHudiSource"
    )
    catalog_hudi_source: Optional[CatalogHudiSourceModel] = Field(
        default=None, alias="CatalogHudiSource"
    )
    s3_hudi_source: Optional[S3HudiSourceModel] = Field(
        default=None, alias="S3HudiSource"
    )
    s3_hudi_catalog_target: Optional[S3HudiCatalogTargetModel] = Field(
        default=None, alias="S3HudiCatalogTarget"
    )
    s3_hudi_direct_target: Optional[S3HudiDirectTargetModel] = Field(
        default=None, alias="S3HudiDirectTarget"
    )
    direct_jdbcsource: Optional[DirectJDBCSourceModel] = Field(
        default=None, alias="DirectJDBCSource"
    )
    s3_catalog_delta_source: Optional[S3CatalogDeltaSourceModel] = Field(
        default=None, alias="S3CatalogDeltaSource"
    )
    catalog_delta_source: Optional[CatalogDeltaSourceModel] = Field(
        default=None, alias="CatalogDeltaSource"
    )
    s3_delta_source: Optional[S3DeltaSourceModel] = Field(
        default=None, alias="S3DeltaSource"
    )
    s3_delta_catalog_target: Optional[S3DeltaCatalogTargetModel] = Field(
        default=None, alias="S3DeltaCatalogTarget"
    )
    s3_delta_direct_target: Optional[S3DeltaDirectTargetModel] = Field(
        default=None, alias="S3DeltaDirectTarget"
    )


class GetMLTaskRunsResponseModel(BaseModel):
    task_runs: List[TaskRunModel] = Field(alias="TaskRuns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStatementResponseModel(BaseModel):
    statement: StatementModel = Field(alias="Statement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStatementsResponseModel(BaseModel):
    statements: List[StatementModel] = Field(alias="Statements")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodeModel(BaseModel):
    type: Optional[Literal["CRAWLER", "JOB", "TRIGGER"]] = Field(
        default=None, alias="Type"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    unique_id: Optional[str] = Field(default=None, alias="UniqueId")
    trigger_details: Optional[TriggerNodeDetailsModel] = Field(
        default=None, alias="TriggerDetails"
    )
    job_details: Optional[JobNodeDetailsModel] = Field(default=None, alias="JobDetails")
    crawler_details: Optional[CrawlerNodeDetailsModel] = Field(
        default=None, alias="CrawlerDetails"
    )


class GetMLTransformsResponseModel(BaseModel):
    transforms: List[MLTransformModel] = Field(alias="Transforms")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ColumnStatisticsErrorModel(BaseModel):
    column_statistics: Optional[ColumnStatisticsModel] = Field(
        default=None, alias="ColumnStatistics"
    )
    error: Optional[ErrorDetailModel] = Field(default=None, alias="Error")


class GetColumnStatisticsForPartitionResponseModel(BaseModel):
    column_statistics_list: List[ColumnStatisticsModel] = Field(
        alias="ColumnStatisticsList"
    )
    errors: List[ColumnErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetColumnStatisticsForTableResponseModel(BaseModel):
    column_statistics_list: List[ColumnStatisticsModel] = Field(
        alias="ColumnStatisticsList"
    )
    errors: List[ColumnErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateColumnStatisticsForPartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_values: Sequence[str] = Field(alias="PartitionValues")
    column_statistics_list: Sequence[ColumnStatisticsModel] = Field(
        alias="ColumnStatisticsList"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class UpdateColumnStatisticsForTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    column_statistics_list: Sequence[ColumnStatisticsModel] = Field(
        alias="ColumnStatisticsList"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchCreatePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_input_list: Sequence[PartitionInputModel] = Field(
        alias="PartitionInputList"
    )
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchUpdatePartitionRequestEntryModel(BaseModel):
    partition_value_list: Sequence[str] = Field(alias="PartitionValueList")
    partition_input: PartitionInputModel = Field(alias="PartitionInput")


class CreatePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_input: PartitionInputModel = Field(alias="PartitionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class UpdatePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    partition_value_list: Sequence[str] = Field(alias="PartitionValueList")
    partition_input: PartitionInputModel = Field(alias="PartitionInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchGetPartitionResponseModel(BaseModel):
    partitions: List[PartitionModel] = Field(alias="Partitions")
    unprocessed_keys: List[PartitionValueListModel] = Field(alias="UnprocessedKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPartitionResponseModel(BaseModel):
    partition: PartitionModel = Field(alias="Partition")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPartitionsResponseModel(BaseModel):
    partitions: List[PartitionModel] = Field(alias="Partitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUnfilteredPartitionMetadataResponseModel(BaseModel):
    partition: PartitionModel = Field(alias="Partition")
    authorized_columns: List[str] = Field(alias="AuthorizedColumns")
    is_registered_with_lake_formation: bool = Field(
        alias="IsRegisteredWithLakeFormation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnfilteredPartitionModel(BaseModel):
    partition: Optional[PartitionModel] = Field(default=None, alias="Partition")
    authorized_columns: Optional[List[str]] = Field(
        default=None, alias="AuthorizedColumns"
    )
    is_registered_with_lake_formation: Optional[bool] = Field(
        default=None, alias="IsRegisteredWithLakeFormation"
    )


class CreateTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_input: TableInputModel = Field(alias="TableInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    partition_indexes: Optional[Sequence[PartitionIndexModel]] = Field(
        default=None, alias="PartitionIndexes"
    )
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class UpdateTableRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_input: TableInputModel = Field(alias="TableInput")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    skip_archive: Optional[bool] = Field(default=None, alias="SkipArchive")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class GetTableResponseModel(BaseModel):
    table: TableModel = Field(alias="Table")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTablesResponseModel(BaseModel):
    table_list: List[TableModel] = Field(alias="TableList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUnfilteredTableMetadataResponseModel(BaseModel):
    table: TableModel = Field(alias="Table")
    authorized_columns: List[str] = Field(alias="AuthorizedColumns")
    is_registered_with_lake_formation: bool = Field(
        alias="IsRegisteredWithLakeFormation"
    )
    cell_filters: List[ColumnRowFilterModel] = Field(alias="CellFilters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchTablesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    table_list: List[TableModel] = Field(alias="TableList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TableVersionModel(BaseModel):
    table: Optional[TableModel] = Field(default=None, alias="Table")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class CreateJobRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role: str = Field(alias="Role")
    command: JobCommandModel = Field(alias="Command")
    description: Optional[str] = Field(default=None, alias="Description")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    execution_property: Optional[ExecutionPropertyModel] = Field(
        default=None, alias="ExecutionProperty"
    )
    default_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="DefaultArguments"
    )
    non_overridable_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="NonOverridableArguments"
    )
    connections: Optional[ConnectionsListModel] = Field(
        default=None, alias="Connections"
    )
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    allocated_capacity: Optional[int] = Field(default=None, alias="AllocatedCapacity")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    code_gen_configuration_nodes: Optional[
        Mapping[str, CodeGenConfigurationNodeModel]
    ] = Field(default=None, alias="CodeGenConfigurationNodes")
    execution_class: Optional[Literal["FLEX", "STANDARD"]] = Field(
        default=None, alias="ExecutionClass"
    )
    source_control_details: Optional[SourceControlDetailsModel] = Field(
        default=None, alias="SourceControlDetails"
    )


class JobModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    role: Optional[str] = Field(default=None, alias="Role")
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    execution_property: Optional[ExecutionPropertyModel] = Field(
        default=None, alias="ExecutionProperty"
    )
    command: Optional[JobCommandModel] = Field(default=None, alias="Command")
    default_arguments: Optional[Dict[str, str]] = Field(
        default=None, alias="DefaultArguments"
    )
    non_overridable_arguments: Optional[Dict[str, str]] = Field(
        default=None, alias="NonOverridableArguments"
    )
    connections: Optional[ConnectionsListModel] = Field(
        default=None, alias="Connections"
    )
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    allocated_capacity: Optional[int] = Field(default=None, alias="AllocatedCapacity")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    code_gen_configuration_nodes: Optional[
        Dict[str, CodeGenConfigurationNodeModel]
    ] = Field(default=None, alias="CodeGenConfigurationNodes")
    execution_class: Optional[Literal["FLEX", "STANDARD"]] = Field(
        default=None, alias="ExecutionClass"
    )
    source_control_details: Optional[SourceControlDetailsModel] = Field(
        default=None, alias="SourceControlDetails"
    )


class JobUpdateModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    role: Optional[str] = Field(default=None, alias="Role")
    execution_property: Optional[ExecutionPropertyModel] = Field(
        default=None, alias="ExecutionProperty"
    )
    command: Optional[JobCommandModel] = Field(default=None, alias="Command")
    default_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="DefaultArguments"
    )
    non_overridable_arguments: Optional[Mapping[str, str]] = Field(
        default=None, alias="NonOverridableArguments"
    )
    connections: Optional[ConnectionsListModel] = Field(
        default=None, alias="Connections"
    )
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    allocated_capacity: Optional[int] = Field(default=None, alias="AllocatedCapacity")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    max_capacity: Optional[float] = Field(default=None, alias="MaxCapacity")
    worker_type: Optional[Literal["G.025X", "G.1X", "G.2X", "Standard"]] = Field(
        default=None, alias="WorkerType"
    )
    number_of_workers: Optional[int] = Field(default=None, alias="NumberOfWorkers")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    notification_property: Optional[NotificationPropertyModel] = Field(
        default=None, alias="NotificationProperty"
    )
    glue_version: Optional[str] = Field(default=None, alias="GlueVersion")
    code_gen_configuration_nodes: Optional[
        Mapping[str, CodeGenConfigurationNodeModel]
    ] = Field(default=None, alias="CodeGenConfigurationNodes")
    execution_class: Optional[Literal["FLEX", "STANDARD"]] = Field(
        default=None, alias="ExecutionClass"
    )
    source_control_details: Optional[SourceControlDetailsModel] = Field(
        default=None, alias="SourceControlDetails"
    )


class WorkflowGraphModel(BaseModel):
    nodes: Optional[List[NodeModel]] = Field(default=None, alias="Nodes")
    edges: Optional[List[EdgeModel]] = Field(default=None, alias="Edges")


class UpdateColumnStatisticsForPartitionResponseModel(BaseModel):
    errors: List[ColumnStatisticsErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateColumnStatisticsForTableResponseModel(BaseModel):
    errors: List[ColumnStatisticsErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePartitionRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    entries: Sequence[BatchUpdatePartitionRequestEntryModel] = Field(alias="Entries")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetUnfilteredPartitionsMetadataResponseModel(BaseModel):
    unfiltered_partitions: List[UnfilteredPartitionModel] = Field(
        alias="UnfilteredPartitions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTableVersionResponseModel(BaseModel):
    table_version: TableVersionModel = Field(alias="TableVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTableVersionsResponseModel(BaseModel):
    table_versions: List[TableVersionModel] = Field(alias="TableVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetJobsResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    jobs_not_found: List[str] = Field(alias="JobsNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobResponseModel(BaseModel):
    job: JobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobsResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobRequestModel(BaseModel):
    job_name: str = Field(alias="JobName")
    job_update: JobUpdateModel = Field(alias="JobUpdate")


class WorkflowRunModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    workflow_run_id: Optional[str] = Field(default=None, alias="WorkflowRunId")
    previous_run_id: Optional[str] = Field(default=None, alias="PreviousRunId")
    workflow_run_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="WorkflowRunProperties"
    )
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    status: Optional[
        Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
    ] = Field(default=None, alias="Status")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    statistics: Optional[WorkflowRunStatisticsModel] = Field(
        default=None, alias="Statistics"
    )
    graph: Optional[WorkflowGraphModel] = Field(default=None, alias="Graph")
    starting_event_batch_condition: Optional[StartingEventBatchConditionModel] = Field(
        default=None, alias="StartingEventBatchCondition"
    )


class GetWorkflowRunResponseModel(BaseModel):
    run: WorkflowRunModel = Field(alias="Run")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowRunsResponseModel(BaseModel):
    runs: List[WorkflowRunModel] = Field(alias="Runs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkflowModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    default_run_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="DefaultRunProperties"
    )
    created_on: Optional[datetime] = Field(default=None, alias="CreatedOn")
    last_modified_on: Optional[datetime] = Field(default=None, alias="LastModifiedOn")
    last_run: Optional[WorkflowRunModel] = Field(default=None, alias="LastRun")
    graph: Optional[WorkflowGraphModel] = Field(default=None, alias="Graph")
    max_concurrent_runs: Optional[int] = Field(default=None, alias="MaxConcurrentRuns")
    blueprint_details: Optional[BlueprintDetailsModel] = Field(
        default=None, alias="BlueprintDetails"
    )


class BatchGetWorkflowsResponseModel(BaseModel):
    workflows: List[WorkflowModel] = Field(alias="Workflows")
    missing_workflows: List[str] = Field(alias="MissingWorkflows")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowResponseModel(BaseModel):
    workflow: WorkflowModel = Field(alias="Workflow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
