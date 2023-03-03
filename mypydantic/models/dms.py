# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountQuotaModel(BaseModel):
    account_quota_name: Optional[str] = Field(default=None, alias="AccountQuotaName")
    used: Optional[int] = Field(default=None, alias="Used")
    max: Optional[int] = Field(default=None, alias="Max")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class ApplyPendingMaintenanceActionMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    apply_action: str = Field(alias="ApplyAction")
    opt_in_type: str = Field(alias="OptInType")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class CancelReplicationTaskAssessmentRunMessageRequestModel(BaseModel):
    replication_task_assessment_run_arn: str = Field(
        alias="ReplicationTaskAssessmentRunArn"
    )


class CertificateModel(BaseModel):
    certificate_identifier: Optional[str] = Field(
        default=None, alias="CertificateIdentifier"
    )
    certificate_creation_date: Optional[datetime] = Field(
        default=None, alias="CertificateCreationDate"
    )
    certificate_pem: Optional[str] = Field(default=None, alias="CertificatePem")
    certificate_wallet: Optional[bytes] = Field(default=None, alias="CertificateWallet")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    certificate_owner: Optional[str] = Field(default=None, alias="CertificateOwner")
    valid_from_date: Optional[datetime] = Field(default=None, alias="ValidFromDate")
    valid_to_date: Optional[datetime] = Field(default=None, alias="ValidToDate")
    signing_algorithm: Optional[str] = Field(default=None, alias="SigningAlgorithm")
    key_length: Optional[int] = Field(default=None, alias="KeyLength")


class CollectorHealthCheckModel(BaseModel):
    collector_status: Optional[Literal["ACTIVE", "UNREGISTERED"]] = Field(
        default=None, alias="CollectorStatus"
    )
    local_collector_s3_access: Optional[bool] = Field(
        default=None, alias="LocalCollectorS3Access"
    )
    web_collector_s3_access: Optional[bool] = Field(
        default=None, alias="WebCollectorS3Access"
    )
    web_collector_granted_role_based_access: Optional[bool] = Field(
        default=None, alias="WebCollectorGrantedRoleBasedAccess"
    )


class InventoryDataModel(BaseModel):
    number_of_databases: Optional[int] = Field(default=None, alias="NumberOfDatabases")
    number_of_schemas: Optional[int] = Field(default=None, alias="NumberOfSchemas")


class CollectorShortInfoResponseModel(BaseModel):
    collector_referenced_id: Optional[str] = Field(
        default=None, alias="CollectorReferencedId"
    )
    collector_name: Optional[str] = Field(default=None, alias="CollectorName")


class ConnectionModel(BaseModel):
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    status: Optional[str] = Field(default=None, alias="Status")
    last_failure_message: Optional[str] = Field(
        default=None, alias="LastFailureMessage"
    )
    endpoint_identifier: Optional[str] = Field(default=None, alias="EndpointIdentifier")
    replication_instance_identifier: Optional[str] = Field(
        default=None, alias="ReplicationInstanceIdentifier"
    )


class DmsTransferSettingsModel(BaseModel):
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")


class DocDbSettingsModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    port: Optional[int] = Field(default=None, alias="Port")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    nesting_level: Optional[Literal["none", "one"]] = Field(
        default=None, alias="NestingLevel"
    )
    extract_doc_id: Optional[bool] = Field(default=None, alias="ExtractDocId")
    docs_to_investigate: Optional[int] = Field(default=None, alias="DocsToInvestigate")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class DynamoDbSettingsModel(BaseModel):
    service_access_role_arn: str = Field(alias="ServiceAccessRoleArn")


class ElasticsearchSettingsModel(BaseModel):
    service_access_role_arn: str = Field(alias="ServiceAccessRoleArn")
    endpoint_uri: str = Field(alias="EndpointUri")
    full_load_error_percentage: Optional[int] = Field(
        default=None, alias="FullLoadErrorPercentage"
    )
    error_retry_duration: Optional[int] = Field(
        default=None, alias="ErrorRetryDuration"
    )
    use_new_mapping_type: Optional[bool] = Field(
        default=None, alias="UseNewMappingType"
    )


class GcpMySQLSettingsModel(BaseModel):
    after_connect_script: Optional[str] = Field(
        default=None, alias="AfterConnectScript"
    )
    clean_source_metadata_on_mismatch: Optional[bool] = Field(
        default=None, alias="CleanSourceMetadataOnMismatch"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    events_poll_interval: Optional[int] = Field(
        default=None, alias="EventsPollInterval"
    )
    target_db_type: Optional[
        Literal["multiple-databases", "specific-database"]
    ] = Field(default=None, alias="TargetDbType")
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    parallel_load_threads: Optional[int] = Field(
        default=None, alias="ParallelLoadThreads"
    )
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    server_timezone: Optional[str] = Field(default=None, alias="ServerTimezone")
    username: Optional[str] = Field(default=None, alias="Username")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class IBMDb2SettingsModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    set_data_capture_changes: Optional[bool] = Field(
        default=None, alias="SetDataCaptureChanges"
    )
    current_lsn: Optional[str] = Field(default=None, alias="CurrentLsn")
    max_kbytes_per_read: Optional[int] = Field(default=None, alias="MaxKBytesPerRead")
    username: Optional[str] = Field(default=None, alias="Username")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class KafkaSettingsModel(BaseModel):
    broker: Optional[str] = Field(default=None, alias="Broker")
    topic: Optional[str] = Field(default=None, alias="Topic")
    message_format: Optional[Literal["json", "json-unformatted"]] = Field(
        default=None, alias="MessageFormat"
    )
    include_transaction_details: Optional[bool] = Field(
        default=None, alias="IncludeTransactionDetails"
    )
    include_partition_value: Optional[bool] = Field(
        default=None, alias="IncludePartitionValue"
    )
    partition_include_schema_table: Optional[bool] = Field(
        default=None, alias="PartitionIncludeSchemaTable"
    )
    include_table_alter_operations: Optional[bool] = Field(
        default=None, alias="IncludeTableAlterOperations"
    )
    include_control_details: Optional[bool] = Field(
        default=None, alias="IncludeControlDetails"
    )
    message_max_bytes: Optional[int] = Field(default=None, alias="MessageMaxBytes")
    include_null_and_empty: Optional[bool] = Field(
        default=None, alias="IncludeNullAndEmpty"
    )
    security_protocol: Optional[
        Literal["plaintext", "sasl-ssl", "ssl-authentication", "ssl-encryption"]
    ] = Field(default=None, alias="SecurityProtocol")
    ssl_client_certificate_arn: Optional[str] = Field(
        default=None, alias="SslClientCertificateArn"
    )
    ssl_client_key_arn: Optional[str] = Field(default=None, alias="SslClientKeyArn")
    ssl_client_key_password: Optional[str] = Field(
        default=None, alias="SslClientKeyPassword"
    )
    ssl_ca_certificate_arn: Optional[str] = Field(
        default=None, alias="SslCaCertificateArn"
    )
    sasl_username: Optional[str] = Field(default=None, alias="SaslUsername")
    sasl_password: Optional[str] = Field(default=None, alias="SaslPassword")
    no_hex_prefix: Optional[bool] = Field(default=None, alias="NoHexPrefix")


class KinesisSettingsModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamArn")
    message_format: Optional[Literal["json", "json-unformatted"]] = Field(
        default=None, alias="MessageFormat"
    )
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    include_transaction_details: Optional[bool] = Field(
        default=None, alias="IncludeTransactionDetails"
    )
    include_partition_value: Optional[bool] = Field(
        default=None, alias="IncludePartitionValue"
    )
    partition_include_schema_table: Optional[bool] = Field(
        default=None, alias="PartitionIncludeSchemaTable"
    )
    include_table_alter_operations: Optional[bool] = Field(
        default=None, alias="IncludeTableAlterOperations"
    )
    include_control_details: Optional[bool] = Field(
        default=None, alias="IncludeControlDetails"
    )
    include_null_and_empty: Optional[bool] = Field(
        default=None, alias="IncludeNullAndEmpty"
    )
    no_hex_prefix: Optional[bool] = Field(default=None, alias="NoHexPrefix")


class MicrosoftSQLServerSettingsModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="Port")
    bcp_packet_size: Optional[int] = Field(default=None, alias="BcpPacketSize")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    control_tables_file_group: Optional[str] = Field(
        default=None, alias="ControlTablesFileGroup"
    )
    password: Optional[str] = Field(default=None, alias="Password")
    query_single_always_on_node: Optional[bool] = Field(
        default=None, alias="QuerySingleAlwaysOnNode"
    )
    read_backup_only: Optional[bool] = Field(default=None, alias="ReadBackupOnly")
    safeguard_policy: Optional[
        Literal[
            "exclusive-automatic-truncation",
            "rely-on-sql-server-replication-agent",
            "shared-automatic-truncation",
        ]
    ] = Field(default=None, alias="SafeguardPolicy")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    username: Optional[str] = Field(default=None, alias="Username")
    use_bcp_full_load: Optional[bool] = Field(default=None, alias="UseBcpFullLoad")
    use_third_party_backup_device: Optional[bool] = Field(
        default=None, alias="UseThirdPartyBackupDevice"
    )
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )
    trim_space_in_char: Optional[bool] = Field(default=None, alias="TrimSpaceInChar")


class MongoDbSettingsModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    port: Optional[int] = Field(default=None, alias="Port")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    auth_type: Optional[Literal["no", "password"]] = Field(
        default=None, alias="AuthType"
    )
    auth_mechanism: Optional[Literal["default", "mongodb_cr", "scram_sha_1"]] = Field(
        default=None, alias="AuthMechanism"
    )
    nesting_level: Optional[Literal["none", "one"]] = Field(
        default=None, alias="NestingLevel"
    )
    extract_doc_id: Optional[str] = Field(default=None, alias="ExtractDocId")
    docs_to_investigate: Optional[str] = Field(default=None, alias="DocsToInvestigate")
    auth_source: Optional[str] = Field(default=None, alias="AuthSource")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class MySQLSettingsModel(BaseModel):
    after_connect_script: Optional[str] = Field(
        default=None, alias="AfterConnectScript"
    )
    clean_source_metadata_on_mismatch: Optional[bool] = Field(
        default=None, alias="CleanSourceMetadataOnMismatch"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    events_poll_interval: Optional[int] = Field(
        default=None, alias="EventsPollInterval"
    )
    target_db_type: Optional[
        Literal["multiple-databases", "specific-database"]
    ] = Field(default=None, alias="TargetDbType")
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    parallel_load_threads: Optional[int] = Field(
        default=None, alias="ParallelLoadThreads"
    )
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    server_timezone: Optional[str] = Field(default=None, alias="ServerTimezone")
    username: Optional[str] = Field(default=None, alias="Username")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class NeptuneSettingsModel(BaseModel):
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_bucket_folder: str = Field(alias="S3BucketFolder")
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    error_retry_duration: Optional[int] = Field(
        default=None, alias="ErrorRetryDuration"
    )
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    max_retry_count: Optional[int] = Field(default=None, alias="MaxRetryCount")
    iam_auth_enabled: Optional[bool] = Field(default=None, alias="IamAuthEnabled")


class OracleSettingsModel(BaseModel):
    add_supplemental_logging: Optional[bool] = Field(
        default=None, alias="AddSupplementalLogging"
    )
    archived_log_dest_id: Optional[int] = Field(default=None, alias="ArchivedLogDestId")
    additional_archived_log_dest_id: Optional[int] = Field(
        default=None, alias="AdditionalArchivedLogDestId"
    )
    extra_archived_log_dest_ids: Optional[Sequence[int]] = Field(
        default=None, alias="ExtraArchivedLogDestIds"
    )
    allow_select_nested_tables: Optional[bool] = Field(
        default=None, alias="AllowSelectNestedTables"
    )
    parallel_asm_read_threads: Optional[int] = Field(
        default=None, alias="ParallelAsmReadThreads"
    )
    read_ahead_blocks: Optional[int] = Field(default=None, alias="ReadAheadBlocks")
    access_alternate_directly: Optional[bool] = Field(
        default=None, alias="AccessAlternateDirectly"
    )
    use_alternate_folder_for_online: Optional[bool] = Field(
        default=None, alias="UseAlternateFolderForOnline"
    )
    oracle_path_prefix: Optional[str] = Field(default=None, alias="OraclePathPrefix")
    use_path_prefix: Optional[str] = Field(default=None, alias="UsePathPrefix")
    replace_path_prefix: Optional[bool] = Field(default=None, alias="ReplacePathPrefix")
    enable_homogenous_tablespace: Optional[bool] = Field(
        default=None, alias="EnableHomogenousTablespace"
    )
    direct_path_no_log: Optional[bool] = Field(default=None, alias="DirectPathNoLog")
    archived_logs_only: Optional[bool] = Field(default=None, alias="ArchivedLogsOnly")
    asm_password: Optional[str] = Field(default=None, alias="AsmPassword")
    asm_server: Optional[str] = Field(default=None, alias="AsmServer")
    asm_user: Optional[str] = Field(default=None, alias="AsmUser")
    char_length_semantics: Optional[Literal["byte", "char", "default"]] = Field(
        default=None, alias="CharLengthSemantics"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    direct_path_parallel_load: Optional[bool] = Field(
        default=None, alias="DirectPathParallelLoad"
    )
    fail_tasks_on_lob_truncation: Optional[bool] = Field(
        default=None, alias="FailTasksOnLobTruncation"
    )
    number_datatype_scale: Optional[int] = Field(
        default=None, alias="NumberDatatypeScale"
    )
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    read_table_space_name: Optional[bool] = Field(
        default=None, alias="ReadTableSpaceName"
    )
    retry_interval: Optional[int] = Field(default=None, alias="RetryInterval")
    security_db_encryption: Optional[str] = Field(
        default=None, alias="SecurityDbEncryption"
    )
    security_db_encryption_name: Optional[str] = Field(
        default=None, alias="SecurityDbEncryptionName"
    )
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    spatial_data_option_to_geo_json_function_name: Optional[str] = Field(
        default=None, alias="SpatialDataOptionToGeoJsonFunctionName"
    )
    standby_delay_time: Optional[int] = Field(default=None, alias="StandbyDelayTime")
    username: Optional[str] = Field(default=None, alias="Username")
    use_bfile: Optional[bool] = Field(default=None, alias="UseBFile")
    use_direct_path_full_load: Optional[bool] = Field(
        default=None, alias="UseDirectPathFullLoad"
    )
    use_logminer_reader: Optional[bool] = Field(default=None, alias="UseLogminerReader")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )
    secrets_manager_oracle_asm_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerOracleAsmAccessRoleArn"
    )
    secrets_manager_oracle_asm_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerOracleAsmSecretId"
    )
    trim_space_in_char: Optional[bool] = Field(default=None, alias="TrimSpaceInChar")


class PostgreSQLSettingsModel(BaseModel):
    after_connect_script: Optional[str] = Field(
        default=None, alias="AfterConnectScript"
    )
    capture_ddls: Optional[bool] = Field(default=None, alias="CaptureDdls")
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    ddl_artifacts_schema: Optional[str] = Field(
        default=None, alias="DdlArtifactsSchema"
    )
    execute_timeout: Optional[int] = Field(default=None, alias="ExecuteTimeout")
    fail_tasks_on_lob_truncation: Optional[bool] = Field(
        default=None, alias="FailTasksOnLobTruncation"
    )
    heartbeat_enable: Optional[bool] = Field(default=None, alias="HeartbeatEnable")
    heartbeat_schema: Optional[str] = Field(default=None, alias="HeartbeatSchema")
    heartbeat_frequency: Optional[int] = Field(default=None, alias="HeartbeatFrequency")
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    username: Optional[str] = Field(default=None, alias="Username")
    slot_name: Optional[str] = Field(default=None, alias="SlotName")
    plugin_name: Optional[
        Literal["no-preference", "pglogical", "test-decoding"]
    ] = Field(default=None, alias="PluginName")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )
    trim_space_in_char: Optional[bool] = Field(default=None, alias="TrimSpaceInChar")


class RedisSettingsModel(BaseModel):
    server_name: str = Field(alias="ServerName")
    port: int = Field(alias="Port")
    ssl_security_protocol: Optional[Literal["plaintext", "ssl-encryption"]] = Field(
        default=None, alias="SslSecurityProtocol"
    )
    auth_type: Optional[Literal["auth-role", "auth-token", "none"]] = Field(
        default=None, alias="AuthType"
    )
    auth_user_name: Optional[str] = Field(default=None, alias="AuthUserName")
    auth_password: Optional[str] = Field(default=None, alias="AuthPassword")
    ssl_ca_certificate_arn: Optional[str] = Field(
        default=None, alias="SslCaCertificateArn"
    )


class RedshiftSettingsModel(BaseModel):
    accept_any_date: Optional[bool] = Field(default=None, alias="AcceptAnyDate")
    after_connect_script: Optional[str] = Field(
        default=None, alias="AfterConnectScript"
    )
    bucket_folder: Optional[str] = Field(default=None, alias="BucketFolder")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    case_sensitive_names: Optional[bool] = Field(
        default=None, alias="CaseSensitiveNames"
    )
    comp_update: Optional[bool] = Field(default=None, alias="CompUpdate")
    connection_timeout: Optional[int] = Field(default=None, alias="ConnectionTimeout")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    date_format: Optional[str] = Field(default=None, alias="DateFormat")
    empty_as_null: Optional[bool] = Field(default=None, alias="EmptyAsNull")
    encryption_mode: Optional[Literal["sse-kms", "sse-s3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    explicit_ids: Optional[bool] = Field(default=None, alias="ExplicitIds")
    file_transfer_upload_streams: Optional[int] = Field(
        default=None, alias="FileTransferUploadStreams"
    )
    load_timeout: Optional[int] = Field(default=None, alias="LoadTimeout")
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    remove_quotes: Optional[bool] = Field(default=None, alias="RemoveQuotes")
    replace_invalid_chars: Optional[str] = Field(
        default=None, alias="ReplaceInvalidChars"
    )
    replace_chars: Optional[str] = Field(default=None, alias="ReplaceChars")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    server_side_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="ServerSideEncryptionKmsKeyId"
    )
    time_format: Optional[str] = Field(default=None, alias="TimeFormat")
    trim_blanks: Optional[bool] = Field(default=None, alias="TrimBlanks")
    truncate_columns: Optional[bool] = Field(default=None, alias="TruncateColumns")
    username: Optional[str] = Field(default=None, alias="Username")
    write_buffer_size: Optional[int] = Field(default=None, alias="WriteBufferSize")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class S3SettingsModel(BaseModel):
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    external_table_definition: Optional[str] = Field(
        default=None, alias="ExternalTableDefinition"
    )
    csv_row_delimiter: Optional[str] = Field(default=None, alias="CsvRowDelimiter")
    csv_delimiter: Optional[str] = Field(default=None, alias="CsvDelimiter")
    bucket_folder: Optional[str] = Field(default=None, alias="BucketFolder")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    compression_type: Optional[Literal["gzip", "none"]] = Field(
        default=None, alias="CompressionType"
    )
    encryption_mode: Optional[Literal["sse-kms", "sse-s3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    server_side_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="ServerSideEncryptionKmsKeyId"
    )
    data_format: Optional[Literal["csv", "parquet"]] = Field(
        default=None, alias="DataFormat"
    )
    encoding_type: Optional[
        Literal["plain", "plain-dictionary", "rle-dictionary"]
    ] = Field(default=None, alias="EncodingType")
    dict_page_size_limit: Optional[int] = Field(default=None, alias="DictPageSizeLimit")
    row_group_length: Optional[int] = Field(default=None, alias="RowGroupLength")
    data_page_size: Optional[int] = Field(default=None, alias="DataPageSize")
    parquet_version: Optional[Literal["parquet-1-0", "parquet-2-0"]] = Field(
        default=None, alias="ParquetVersion"
    )
    enable_statistics: Optional[bool] = Field(default=None, alias="EnableStatistics")
    include_op_for_full_load: Optional[bool] = Field(
        default=None, alias="IncludeOpForFullLoad"
    )
    cdc_inserts_only: Optional[bool] = Field(default=None, alias="CdcInsertsOnly")
    timestamp_column_name: Optional[str] = Field(
        default=None, alias="TimestampColumnName"
    )
    parquet_timestamp_in_millisecond: Optional[bool] = Field(
        default=None, alias="ParquetTimestampInMillisecond"
    )
    cdc_inserts_and_updates: Optional[bool] = Field(
        default=None, alias="CdcInsertsAndUpdates"
    )
    date_partition_enabled: Optional[bool] = Field(
        default=None, alias="DatePartitionEnabled"
    )
    date_partition_sequence: Optional[
        Literal["DDMMYYYY", "MMYYYYDD", "YYYYMM", "YYYYMMDD", "YYYYMMDDHH"]
    ] = Field(default=None, alias="DatePartitionSequence")
    date_partition_delimiter: Optional[
        Literal["DASH", "NONE", "SLASH", "UNDERSCORE"]
    ] = Field(default=None, alias="DatePartitionDelimiter")
    use_csv_no_sup_value: Optional[bool] = Field(default=None, alias="UseCsvNoSupValue")
    csv_no_sup_value: Optional[str] = Field(default=None, alias="CsvNoSupValue")
    preserve_transactions: Optional[bool] = Field(
        default=None, alias="PreserveTransactions"
    )
    cdc_path: Optional[str] = Field(default=None, alias="CdcPath")
    use_task_start_time_for_full_load_timestamp: Optional[bool] = Field(
        default=None, alias="UseTaskStartTimeForFullLoadTimestamp"
    )
    canned_acl_for_objects: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "none",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="CannedAclForObjects")
    add_column_name: Optional[bool] = Field(default=None, alias="AddColumnName")
    cdc_max_batch_interval: Optional[int] = Field(
        default=None, alias="CdcMaxBatchInterval"
    )
    cdc_min_file_size: Optional[int] = Field(default=None, alias="CdcMinFileSize")
    csv_null_value: Optional[str] = Field(default=None, alias="CsvNullValue")
    ignore_header_rows: Optional[int] = Field(default=None, alias="IgnoreHeaderRows")
    max_file_size: Optional[int] = Field(default=None, alias="MaxFileSize")
    rfc4180: Optional[bool] = Field(default=None, alias="Rfc4180")
    date_partition_timezone: Optional[str] = Field(
        default=None, alias="DatePartitionTimezone"
    )
    add_trailing_padding_character: Optional[bool] = Field(
        default=None, alias="AddTrailingPaddingCharacter"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )


class SybaseSettingsModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    password: Optional[str] = Field(default=None, alias="Password")
    port: Optional[int] = Field(default=None, alias="Port")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    username: Optional[str] = Field(default=None, alias="Username")
    secrets_manager_access_role_arn: Optional[str] = Field(
        default=None, alias="SecretsManagerAccessRoleArn"
    )
    secrets_manager_secret_id: Optional[str] = Field(
        default=None, alias="SecretsManagerSecretId"
    )


class EventSubscriptionModel(BaseModel):
    customer_aws_id: Optional[str] = Field(default=None, alias="CustomerAwsId")
    cust_subscription_id: Optional[str] = Field(
        default=None, alias="CustSubscriptionId"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    status: Optional[str] = Field(default=None, alias="Status")
    subscription_creation_time: Optional[str] = Field(
        default=None, alias="SubscriptionCreationTime"
    )
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    source_ids_list: Optional[List[str]] = Field(default=None, alias="SourceIdsList")
    event_categories_list: Optional[List[str]] = Field(
        default=None, alias="EventCategoriesList"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class CreateFleetAdvisorCollectorRequestModel(BaseModel):
    collector_name: str = Field(alias="CollectorName")
    service_access_role_arn: str = Field(alias="ServiceAccessRoleArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    description: Optional[str] = Field(default=None, alias="Description")


class DatabaseInstanceSoftwareDetailsResponseModel(BaseModel):
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    engine_edition: Optional[str] = Field(default=None, alias="EngineEdition")
    service_pack: Optional[str] = Field(default=None, alias="ServicePack")
    support_level: Optional[str] = Field(default=None, alias="SupportLevel")
    os_architecture: Optional[int] = Field(default=None, alias="OsArchitecture")
    tooltip: Optional[str] = Field(default=None, alias="Tooltip")


class ServerShortInfoResponseModel(BaseModel):
    server_id: Optional[str] = Field(default=None, alias="ServerId")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    server_name: Optional[str] = Field(default=None, alias="ServerName")


class DatabaseShortInfoResponseModel(BaseModel):
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    database_ip_address: Optional[str] = Field(default=None, alias="DatabaseIpAddress")
    database_engine: Optional[str] = Field(default=None, alias="DatabaseEngine")


class DeleteCertificateMessageRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class DeleteCollectorRequestModel(BaseModel):
    collector_referenced_id: str = Field(alias="CollectorReferencedId")


class DeleteConnectionMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")


class DeleteEndpointMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class DeleteEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")


class DeleteFleetAdvisorDatabasesRequestModel(BaseModel):
    database_ids: Sequence[str] = Field(alias="DatabaseIds")


class DeleteReplicationInstanceMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")


class DeleteReplicationSubnetGroupMessageRequestModel(BaseModel):
    replication_subnet_group_identifier: str = Field(
        alias="ReplicationSubnetGroupIdentifier"
    )


class DeleteReplicationTaskAssessmentRunMessageRequestModel(BaseModel):
    replication_task_assessment_run_arn: str = Field(
        alias="ReplicationTaskAssessmentRunArn"
    )


class DeleteReplicationTaskMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")


class DescribeApplicableIndividualAssessmentsMessageRequestModel(BaseModel):
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    source_engine_name: Optional[str] = Field(default=None, alias="SourceEngineName")
    target_engine_name: Optional[str] = Field(default=None, alias="TargetEngineName")
    migration_type: Optional[Literal["cdc", "full-load", "full-load-and-cdc"]] = Field(
        default=None, alias="MigrationType"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeEndpointSettingsMessageRequestModel(BaseModel):
    engine_name: str = Field(alias="EngineName")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class EndpointSettingModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["boolean", "enum", "integer", "string"]] = Field(
        default=None, alias="Type"
    )
    enum_values: Optional[List[str]] = Field(default=None, alias="EnumValues")
    sensitive: Optional[bool] = Field(default=None, alias="Sensitive")
    units: Optional[str] = Field(default=None, alias="Units")
    applicability: Optional[str] = Field(default=None, alias="Applicability")
    int_value_min: Optional[int] = Field(default=None, alias="IntValueMin")
    int_value_max: Optional[int] = Field(default=None, alias="IntValueMax")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class SupportedEndpointTypeModel(BaseModel):
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    supports_cdc: Optional[bool] = Field(default=None, alias="SupportsCDC")
    endpoint_type: Optional[Literal["source", "target"]] = Field(
        default=None, alias="EndpointType"
    )
    replication_instance_engine_minimum_version: Optional[str] = Field(
        default=None, alias="ReplicationInstanceEngineMinimumVersion"
    )
    engine_display_name: Optional[str] = Field(default=None, alias="EngineDisplayName")


class EventCategoryGroupModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")


class EventModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[Literal["replication-instance"]] = Field(
        default=None, alias="SourceType"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    event_categories: Optional[List[str]] = Field(default=None, alias="EventCategories")
    date: Optional[datetime] = Field(default=None, alias="Date")


class DescribeFleetAdvisorLsaAnalysisRequestModel(BaseModel):
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class FleetAdvisorLsaAnalysisResponseModel(BaseModel):
    lsa_analysis_id: Optional[str] = Field(default=None, alias="LsaAnalysisId")
    status: Optional[str] = Field(default=None, alias="Status")


class FleetAdvisorSchemaObjectResponseModel(BaseModel):
    schema_id: Optional[str] = Field(default=None, alias="SchemaId")
    object_type: Optional[str] = Field(default=None, alias="ObjectType")
    number_of_objects: Optional[int] = Field(default=None, alias="NumberOfObjects")
    code_line_count: Optional[int] = Field(default=None, alias="CodeLineCount")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")


class DescribeOrderableReplicationInstancesMessageRequestModel(BaseModel):
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class OrderableReplicationInstanceModel(BaseModel):
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    replication_instance_class: Optional[str] = Field(
        default=None, alias="ReplicationInstanceClass"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    min_allocated_storage: Optional[int] = Field(
        default=None, alias="MinAllocatedStorage"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )
    default_allocated_storage: Optional[int] = Field(
        default=None, alias="DefaultAllocatedStorage"
    )
    included_allocated_storage: Optional[int] = Field(
        default=None, alias="IncludedAllocatedStorage"
    )
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    release_status: Optional[Literal["beta"]] = Field(
        default=None, alias="ReleaseStatus"
    )


class DescribeRefreshSchemasStatusMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class RefreshSchemasStatusModel(BaseModel):
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    status: Optional[Literal["failed", "refreshing", "successful"]] = Field(
        default=None, alias="Status"
    )
    last_refresh_date: Optional[datetime] = Field(default=None, alias="LastRefreshDate")
    last_failure_message: Optional[str] = Field(
        default=None, alias="LastFailureMessage"
    )


class DescribeReplicationInstanceTaskLogsMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ReplicationInstanceTaskLogModel(BaseModel):
    replication_task_name: Optional[str] = Field(
        default=None, alias="ReplicationTaskName"
    )
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    replication_instance_task_log_size: Optional[int] = Field(
        default=None, alias="ReplicationInstanceTaskLogSize"
    )


class DescribeReplicationTaskAssessmentResultsMessageRequestModel(BaseModel):
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ReplicationTaskAssessmentResultModel(BaseModel):
    replication_task_identifier: Optional[str] = Field(
        default=None, alias="ReplicationTaskIdentifier"
    )
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    replication_task_last_assessment_date: Optional[datetime] = Field(
        default=None, alias="ReplicationTaskLastAssessmentDate"
    )
    assessment_status: Optional[str] = Field(default=None, alias="AssessmentStatus")
    assessment_results_file: Optional[str] = Field(
        default=None, alias="AssessmentResultsFile"
    )
    assessment_results: Optional[str] = Field(default=None, alias="AssessmentResults")
    s3_object_url: Optional[str] = Field(default=None, alias="S3ObjectUrl")


class ReplicationTaskIndividualAssessmentModel(BaseModel):
    replication_task_individual_assessment_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskIndividualAssessmentArn"
    )
    replication_task_assessment_run_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskAssessmentRunArn"
    )
    individual_assessment_name: Optional[str] = Field(
        default=None, alias="IndividualAssessmentName"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    replication_task_individual_assessment_start_date: Optional[datetime] = Field(
        default=None, alias="ReplicationTaskIndividualAssessmentStartDate"
    )


class DescribeSchemasMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class TableStatisticsModel(BaseModel):
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    inserts: Optional[int] = Field(default=None, alias="Inserts")
    deletes: Optional[int] = Field(default=None, alias="Deletes")
    updates: Optional[int] = Field(default=None, alias="Updates")
    ddls: Optional[int] = Field(default=None, alias="Ddls")
    applied_inserts: Optional[int] = Field(default=None, alias="AppliedInserts")
    applied_deletes: Optional[int] = Field(default=None, alias="AppliedDeletes")
    applied_updates: Optional[int] = Field(default=None, alias="AppliedUpdates")
    applied_ddls: Optional[int] = Field(default=None, alias="AppliedDdls")
    full_load_rows: Optional[int] = Field(default=None, alias="FullLoadRows")
    full_load_condtnl_chk_failed_rows: Optional[int] = Field(
        default=None, alias="FullLoadCondtnlChkFailedRows"
    )
    full_load_error_rows: Optional[int] = Field(default=None, alias="FullLoadErrorRows")
    full_load_start_time: Optional[datetime] = Field(
        default=None, alias="FullLoadStartTime"
    )
    full_load_end_time: Optional[datetime] = Field(
        default=None, alias="FullLoadEndTime"
    )
    full_load_reloaded: Optional[bool] = Field(default=None, alias="FullLoadReloaded")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    table_state: Optional[str] = Field(default=None, alias="TableState")
    validation_pending_records: Optional[int] = Field(
        default=None, alias="ValidationPendingRecords"
    )
    validation_failed_records: Optional[int] = Field(
        default=None, alias="ValidationFailedRecords"
    )
    validation_suspended_records: Optional[int] = Field(
        default=None, alias="ValidationSuspendedRecords"
    )
    validation_state: Optional[str] = Field(default=None, alias="ValidationState")
    validation_state_details: Optional[str] = Field(
        default=None, alias="ValidationStateDetails"
    )


class ListTagsForResourceMessageRequestModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_arn_list: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceArnList"
    )


class ModifyEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ModifyReplicationInstanceMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    apply_immediately: Optional[bool] = Field(default=None, alias="ApplyImmediately")
    replication_instance_class: Optional[str] = Field(
        default=None, alias="ReplicationInstanceClass"
    )
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    allow_major_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowMajorVersionUpgrade"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    replication_instance_identifier: Optional[str] = Field(
        default=None, alias="ReplicationInstanceIdentifier"
    )
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


class ModifyReplicationSubnetGroupMessageRequestModel(BaseModel):
    replication_subnet_group_identifier: str = Field(
        alias="ReplicationSubnetGroupIdentifier"
    )
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    replication_subnet_group_description: Optional[str] = Field(
        default=None, alias="ReplicationSubnetGroupDescription"
    )


class ModifyReplicationTaskMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    replication_task_identifier: Optional[str] = Field(
        default=None, alias="ReplicationTaskIdentifier"
    )
    migration_type: Optional[Literal["cdc", "full-load", "full-load-and-cdc"]] = Field(
        default=None, alias="MigrationType"
    )
    table_mappings: Optional[str] = Field(default=None, alias="TableMappings")
    replication_task_settings: Optional[str] = Field(
        default=None, alias="ReplicationTaskSettings"
    )
    cdc_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="CdcStartTime"
    )
    cdc_start_position: Optional[str] = Field(default=None, alias="CdcStartPosition")
    cdc_stop_position: Optional[str] = Field(default=None, alias="CdcStopPosition")
    task_data: Optional[str] = Field(default=None, alias="TaskData")


class MoveReplicationTaskMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    target_replication_instance_arn: str = Field(alias="TargetReplicationInstanceArn")


class PendingMaintenanceActionModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="Action")
    auto_applied_after_date: Optional[datetime] = Field(
        default=None, alias="AutoAppliedAfterDate"
    )
    forced_apply_date: Optional[datetime] = Field(default=None, alias="ForcedApplyDate")
    opt_in_status: Optional[str] = Field(default=None, alias="OptInStatus")
    current_apply_date: Optional[datetime] = Field(
        default=None, alias="CurrentApplyDate"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class RebootReplicationInstanceMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    force_failover: Optional[bool] = Field(default=None, alias="ForceFailover")
    force_planned_failover: Optional[bool] = Field(
        default=None, alias="ForcePlannedFailover"
    )


class RefreshSchemasMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")


class TableToReloadModel(BaseModel):
    schema_name: str = Field(alias="SchemaName")
    table_name: str = Field(alias="TableName")


class RemoveTagsFromResourceMessageRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ReplicationPendingModifiedValuesModel(BaseModel):
    replication_instance_class: Optional[str] = Field(
        default=None, alias="ReplicationInstanceClass"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


class VpcSecurityGroupMembershipModel(BaseModel):
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="VpcSecurityGroupId"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class ReplicationTaskAssessmentRunProgressModel(BaseModel):
    individual_assessment_count: Optional[int] = Field(
        default=None, alias="IndividualAssessmentCount"
    )
    individual_assessment_completed_count: Optional[int] = Field(
        default=None, alias="IndividualAssessmentCompletedCount"
    )


class ReplicationTaskStatsModel(BaseModel):
    full_load_progress_percent: Optional[int] = Field(
        default=None, alias="FullLoadProgressPercent"
    )
    elapsed_time_millis: Optional[int] = Field(default=None, alias="ElapsedTimeMillis")
    tables_loaded: Optional[int] = Field(default=None, alias="TablesLoaded")
    tables_loading: Optional[int] = Field(default=None, alias="TablesLoading")
    tables_queued: Optional[int] = Field(default=None, alias="TablesQueued")
    tables_errored: Optional[int] = Field(default=None, alias="TablesErrored")
    fresh_start_date: Optional[datetime] = Field(default=None, alias="FreshStartDate")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    stop_date: Optional[datetime] = Field(default=None, alias="StopDate")
    full_load_start_date: Optional[datetime] = Field(
        default=None, alias="FullLoadStartDate"
    )
    full_load_finish_date: Optional[datetime] = Field(
        default=None, alias="FullLoadFinishDate"
    )


class SchemaShortInfoResponseModel(BaseModel):
    schema_id: Optional[str] = Field(default=None, alias="SchemaId")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    database_ip_address: Optional[str] = Field(default=None, alias="DatabaseIpAddress")


class StartReplicationTaskAssessmentMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")


class StartReplicationTaskAssessmentRunMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    service_access_role_arn: str = Field(alias="ServiceAccessRoleArn")
    result_location_bucket: str = Field(alias="ResultLocationBucket")
    assessment_run_name: str = Field(alias="AssessmentRunName")
    result_location_folder: Optional[str] = Field(
        default=None, alias="ResultLocationFolder"
    )
    result_encryption_mode: Optional[str] = Field(
        default=None, alias="ResultEncryptionMode"
    )
    result_kms_key_arn: Optional[str] = Field(default=None, alias="ResultKmsKeyArn")
    include_only: Optional[Sequence[str]] = Field(default=None, alias="IncludeOnly")
    exclude: Optional[Sequence[str]] = Field(default=None, alias="Exclude")


class StartReplicationTaskMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    start_replication_task_type: Literal[
        "reload-target", "resume-processing", "start-replication"
    ] = Field(alias="StartReplicationTaskType")
    cdc_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="CdcStartTime"
    )
    cdc_start_position: Optional[str] = Field(default=None, alias="CdcStartPosition")
    cdc_stop_position: Optional[str] = Field(default=None, alias="CdcStopPosition")


class StopReplicationTaskMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")


class TestConnectionMessageRequestModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    endpoint_arn: str = Field(alias="EndpointArn")


class UpdateSubscriptionsToEventBridgeMessageRequestModel(BaseModel):
    force_move: Optional[bool] = Field(default=None, alias="ForceMove")


class AddTagsToResourceMessageRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateEventSubscriptionMessageRequestModel(BaseModel):
    subscription_name: str = Field(alias="SubscriptionName")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    source_ids: Optional[Sequence[str]] = Field(default=None, alias="SourceIds")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateReplicationInstanceMessageRequestModel(BaseModel):
    replication_instance_identifier: str = Field(alias="ReplicationInstanceIdentifier")
    replication_instance_class: str = Field(alias="ReplicationInstanceClass")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    vpc_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="VpcSecurityGroupIds"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    replication_subnet_group_identifier: Optional[str] = Field(
        default=None, alias="ReplicationSubnetGroupIdentifier"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    dns_name_servers: Optional[str] = Field(default=None, alias="DnsNameServers")
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


class CreateReplicationSubnetGroupMessageRequestModel(BaseModel):
    replication_subnet_group_identifier: str = Field(
        alias="ReplicationSubnetGroupIdentifier"
    )
    replication_subnet_group_description: str = Field(
        alias="ReplicationSubnetGroupDescription"
    )
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateReplicationTaskMessageRequestModel(BaseModel):
    replication_task_identifier: str = Field(alias="ReplicationTaskIdentifier")
    source_endpoint_arn: str = Field(alias="SourceEndpointArn")
    target_endpoint_arn: str = Field(alias="TargetEndpointArn")
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    migration_type: Literal["cdc", "full-load", "full-load-and-cdc"] = Field(
        alias="MigrationType"
    )
    table_mappings: str = Field(alias="TableMappings")
    replication_task_settings: Optional[str] = Field(
        default=None, alias="ReplicationTaskSettings"
    )
    cdc_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="CdcStartTime"
    )
    cdc_start_position: Optional[str] = Field(default=None, alias="CdcStartPosition")
    cdc_stop_position: Optional[str] = Field(default=None, alias="CdcStopPosition")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    task_data: Optional[str] = Field(default=None, alias="TaskData")
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")


class ImportCertificateMessageRequestModel(BaseModel):
    certificate_identifier: str = Field(alias="CertificateIdentifier")
    certificate_pem: Optional[str] = Field(default=None, alias="CertificatePem")
    certificate_wallet: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="CertificateWallet")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateFleetAdvisorCollectorResponseModel(BaseModel):
    collector_referenced_id: str = Field(alias="CollectorReferencedId")
    collector_name: str = Field(alias="CollectorName")
    description: str = Field(alias="Description")
    service_access_role_arn: str = Field(alias="ServiceAccessRoleArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFleetAdvisorDatabasesResponseModel(BaseModel):
    database_ids: List[str] = Field(alias="DatabaseIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAttributesResponseModel(BaseModel):
    account_quotas: List[AccountQuotaModel] = Field(alias="AccountQuotas")
    unique_account_identifier: str = Field(alias="UniqueAccountIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicableIndividualAssessmentsResponseModel(BaseModel):
    individual_assessment_names: List[str] = Field(alias="IndividualAssessmentNames")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSchemasResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    schemas: List[str] = Field(alias="Schemas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReloadTablesResponseModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunFleetAdvisorLsaAnalysisResponseModel(BaseModel):
    lsa_analysis_id: str = Field(alias="LsaAnalysisId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubscriptionsToEventBridgeResponseModel(BaseModel):
    result: str = Field(alias="Result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[AvailabilityZoneModel] = Field(
        default=None, alias="SubnetAvailabilityZone"
    )
    subnet_status: Optional[str] = Field(default=None, alias="SubnetStatus")


class DeleteCertificateResponseModel(BaseModel):
    certificate: CertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCertificatesResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    certificates: List[CertificateModel] = Field(alias="Certificates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportCertificateResponseModel(BaseModel):
    certificate: CertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CollectorResponseModel(BaseModel):
    collector_referenced_id: Optional[str] = Field(
        default=None, alias="CollectorReferencedId"
    )
    collector_name: Optional[str] = Field(default=None, alias="CollectorName")
    collector_version: Optional[str] = Field(default=None, alias="CollectorVersion")
    version_status: Optional[Literal["OUTDATED", "UNSUPPORTED", "UP_TO_DATE"]] = Field(
        default=None, alias="VersionStatus"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    collector_health_check: Optional[CollectorHealthCheckModel] = Field(
        default=None, alias="CollectorHealthCheck"
    )
    last_data_received: Optional[str] = Field(default=None, alias="LastDataReceived")
    registered_date: Optional[str] = Field(default=None, alias="RegisteredDate")
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    modified_date: Optional[str] = Field(default=None, alias="ModifiedDate")
    inventory_data: Optional[InventoryDataModel] = Field(
        default=None, alias="InventoryData"
    )


class DeleteConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectionsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    connections: List[ConnectionModel] = Field(alias="Connections")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointMessageRequestModel(BaseModel):
    endpoint_identifier: str = Field(alias="EndpointIdentifier")
    endpoint_type: Literal["source", "target"] = Field(alias="EndpointType")
    engine_name: str = Field(alias="EngineName")
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    port: Optional[int] = Field(default=None, alias="Port")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    extra_connection_attributes: Optional[str] = Field(
        default=None, alias="ExtraConnectionAttributes"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    ssl_mode: Optional[Literal["none", "require", "verify-ca", "verify-full"]] = Field(
        default=None, alias="SslMode"
    )
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    external_table_definition: Optional[str] = Field(
        default=None, alias="ExternalTableDefinition"
    )
    dynamo_db_settings: Optional[DynamoDbSettingsModel] = Field(
        default=None, alias="DynamoDbSettings"
    )
    s3_settings: Optional[S3SettingsModel] = Field(default=None, alias="S3Settings")
    dms_transfer_settings: Optional[DmsTransferSettingsModel] = Field(
        default=None, alias="DmsTransferSettings"
    )
    mongo_db_settings: Optional[MongoDbSettingsModel] = Field(
        default=None, alias="MongoDbSettings"
    )
    kinesis_settings: Optional[KinesisSettingsModel] = Field(
        default=None, alias="KinesisSettings"
    )
    kafka_settings: Optional[KafkaSettingsModel] = Field(
        default=None, alias="KafkaSettings"
    )
    elasticsearch_settings: Optional[ElasticsearchSettingsModel] = Field(
        default=None, alias="ElasticsearchSettings"
    )
    neptune_settings: Optional[NeptuneSettingsModel] = Field(
        default=None, alias="NeptuneSettings"
    )
    redshift_settings: Optional[RedshiftSettingsModel] = Field(
        default=None, alias="RedshiftSettings"
    )
    postgre_s_ql_settings: Optional[PostgreSQLSettingsModel] = Field(
        default=None, alias="PostgreSQLSettings"
    )
    my_s_ql_settings: Optional[MySQLSettingsModel] = Field(
        default=None, alias="MySQLSettings"
    )
    oracle_settings: Optional[OracleSettingsModel] = Field(
        default=None, alias="OracleSettings"
    )
    sybase_settings: Optional[SybaseSettingsModel] = Field(
        default=None, alias="SybaseSettings"
    )
    microsoft_s_ql_server_settings: Optional[MicrosoftSQLServerSettingsModel] = Field(
        default=None, alias="MicrosoftSQLServerSettings"
    )
    ibmdb2_settings: Optional[IBMDb2SettingsModel] = Field(
        default=None, alias="IBMDb2Settings"
    )
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    doc_db_settings: Optional[DocDbSettingsModel] = Field(
        default=None, alias="DocDbSettings"
    )
    redis_settings: Optional[RedisSettingsModel] = Field(
        default=None, alias="RedisSettings"
    )
    gcp_my_s_ql_settings: Optional[GcpMySQLSettingsModel] = Field(
        default=None, alias="GcpMySQLSettings"
    )


class EndpointModel(BaseModel):
    endpoint_identifier: Optional[str] = Field(default=None, alias="EndpointIdentifier")
    endpoint_type: Optional[Literal["source", "target"]] = Field(
        default=None, alias="EndpointType"
    )
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    engine_display_name: Optional[str] = Field(default=None, alias="EngineDisplayName")
    username: Optional[str] = Field(default=None, alias="Username")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    port: Optional[int] = Field(default=None, alias="Port")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    extra_connection_attributes: Optional[str] = Field(
        default=None, alias="ExtraConnectionAttributes"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    ssl_mode: Optional[Literal["none", "require", "verify-ca", "verify-full"]] = Field(
        default=None, alias="SslMode"
    )
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    external_table_definition: Optional[str] = Field(
        default=None, alias="ExternalTableDefinition"
    )
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    dynamo_db_settings: Optional[DynamoDbSettingsModel] = Field(
        default=None, alias="DynamoDbSettings"
    )
    s3_settings: Optional[S3SettingsModel] = Field(default=None, alias="S3Settings")
    dms_transfer_settings: Optional[DmsTransferSettingsModel] = Field(
        default=None, alias="DmsTransferSettings"
    )
    mongo_db_settings: Optional[MongoDbSettingsModel] = Field(
        default=None, alias="MongoDbSettings"
    )
    kinesis_settings: Optional[KinesisSettingsModel] = Field(
        default=None, alias="KinesisSettings"
    )
    kafka_settings: Optional[KafkaSettingsModel] = Field(
        default=None, alias="KafkaSettings"
    )
    elasticsearch_settings: Optional[ElasticsearchSettingsModel] = Field(
        default=None, alias="ElasticsearchSettings"
    )
    neptune_settings: Optional[NeptuneSettingsModel] = Field(
        default=None, alias="NeptuneSettings"
    )
    redshift_settings: Optional[RedshiftSettingsModel] = Field(
        default=None, alias="RedshiftSettings"
    )
    postgre_s_ql_settings: Optional[PostgreSQLSettingsModel] = Field(
        default=None, alias="PostgreSQLSettings"
    )
    my_s_ql_settings: Optional[MySQLSettingsModel] = Field(
        default=None, alias="MySQLSettings"
    )
    oracle_settings: Optional[OracleSettingsModel] = Field(
        default=None, alias="OracleSettings"
    )
    sybase_settings: Optional[SybaseSettingsModel] = Field(
        default=None, alias="SybaseSettings"
    )
    microsoft_s_ql_server_settings: Optional[MicrosoftSQLServerSettingsModel] = Field(
        default=None, alias="MicrosoftSQLServerSettings"
    )
    ibmdb2_settings: Optional[IBMDb2SettingsModel] = Field(
        default=None, alias="IBMDb2Settings"
    )
    doc_db_settings: Optional[DocDbSettingsModel] = Field(
        default=None, alias="DocDbSettings"
    )
    redis_settings: Optional[RedisSettingsModel] = Field(
        default=None, alias="RedisSettings"
    )
    gcp_my_s_ql_settings: Optional[GcpMySQLSettingsModel] = Field(
        default=None, alias="GcpMySQLSettings"
    )


class ModifyEndpointMessageRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    endpoint_identifier: Optional[str] = Field(default=None, alias="EndpointIdentifier")
    endpoint_type: Optional[Literal["source", "target"]] = Field(
        default=None, alias="EndpointType"
    )
    engine_name: Optional[str] = Field(default=None, alias="EngineName")
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    server_name: Optional[str] = Field(default=None, alias="ServerName")
    port: Optional[int] = Field(default=None, alias="Port")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    extra_connection_attributes: Optional[str] = Field(
        default=None, alias="ExtraConnectionAttributes"
    )
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    ssl_mode: Optional[Literal["none", "require", "verify-ca", "verify-full"]] = Field(
        default=None, alias="SslMode"
    )
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    external_table_definition: Optional[str] = Field(
        default=None, alias="ExternalTableDefinition"
    )
    dynamo_db_settings: Optional[DynamoDbSettingsModel] = Field(
        default=None, alias="DynamoDbSettings"
    )
    s3_settings: Optional[S3SettingsModel] = Field(default=None, alias="S3Settings")
    dms_transfer_settings: Optional[DmsTransferSettingsModel] = Field(
        default=None, alias="DmsTransferSettings"
    )
    mongo_db_settings: Optional[MongoDbSettingsModel] = Field(
        default=None, alias="MongoDbSettings"
    )
    kinesis_settings: Optional[KinesisSettingsModel] = Field(
        default=None, alias="KinesisSettings"
    )
    kafka_settings: Optional[KafkaSettingsModel] = Field(
        default=None, alias="KafkaSettings"
    )
    elasticsearch_settings: Optional[ElasticsearchSettingsModel] = Field(
        default=None, alias="ElasticsearchSettings"
    )
    neptune_settings: Optional[NeptuneSettingsModel] = Field(
        default=None, alias="NeptuneSettings"
    )
    redshift_settings: Optional[RedshiftSettingsModel] = Field(
        default=None, alias="RedshiftSettings"
    )
    postgre_s_ql_settings: Optional[PostgreSQLSettingsModel] = Field(
        default=None, alias="PostgreSQLSettings"
    )
    my_s_ql_settings: Optional[MySQLSettingsModel] = Field(
        default=None, alias="MySQLSettings"
    )
    oracle_settings: Optional[OracleSettingsModel] = Field(
        default=None, alias="OracleSettings"
    )
    sybase_settings: Optional[SybaseSettingsModel] = Field(
        default=None, alias="SybaseSettings"
    )
    microsoft_s_ql_server_settings: Optional[MicrosoftSQLServerSettingsModel] = Field(
        default=None, alias="MicrosoftSQLServerSettings"
    )
    ibmdb2_settings: Optional[IBMDb2SettingsModel] = Field(
        default=None, alias="IBMDb2Settings"
    )
    doc_db_settings: Optional[DocDbSettingsModel] = Field(
        default=None, alias="DocDbSettings"
    )
    redis_settings: Optional[RedisSettingsModel] = Field(
        default=None, alias="RedisSettings"
    )
    exact_settings: Optional[bool] = Field(default=None, alias="ExactSettings")
    gcp_my_s_ql_settings: Optional[GcpMySQLSettingsModel] = Field(
        default=None, alias="GcpMySQLSettings"
    )


class CreateEventSubscriptionResponseModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventSubscriptionResponseModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventSubscriptionsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    event_subscriptions_list: List[EventSubscriptionModel] = Field(
        alias="EventSubscriptionsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyEventSubscriptionResponseModel(BaseModel):
    event_subscription: EventSubscriptionModel = Field(alias="EventSubscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatabaseResponseModel(BaseModel):
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    number_of_schemas: Optional[int] = Field(default=None, alias="NumberOfSchemas")
    server: Optional[ServerShortInfoResponseModel] = Field(default=None, alias="Server")
    software_details: Optional[DatabaseInstanceSoftwareDetailsResponseModel] = Field(
        default=None, alias="SoftwareDetails"
    )
    collectors: Optional[List[CollectorShortInfoResponseModel]] = Field(
        default=None, alias="Collectors"
    )


class DescribeCertificatesMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeConnectionsMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEndpointTypesMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEndpointsMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventCategoriesMessageRequestModel(BaseModel):
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeEventSubscriptionsMessageRequestModel(BaseModel):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeEventsMessageRequestModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[Literal["replication-instance"]] = Field(
        default=None, alias="SourceType"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeFleetAdvisorCollectorsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetAdvisorDatabasesRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetAdvisorSchemaObjectSummaryRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetAdvisorSchemasRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePendingMaintenanceActionsMessageRequestModel(BaseModel):
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")


class DescribeReplicationInstancesMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReplicationSubnetGroupsMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReplicationTaskAssessmentRunsMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReplicationTaskIndividualAssessmentsMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeReplicationTasksMessageRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")


class DescribeTableStatisticsMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class DescribeCertificatesMessageDescribeCertificatesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConnectionsMessageDescribeConnectionsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEndpointTypesMessageDescribeEndpointTypesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEndpointsMessageDescribeEndpointsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateModel(
    BaseModel
):
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsMessageDescribeEventsPaginateModel(BaseModel):
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_type: Optional[Literal["replication-instance"]] = Field(
        default=None, alias="SourceType"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    event_categories: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategories"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrderableReplicationInstancesMessageDescribeOrderableReplicationInstancesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationInstancesMessageDescribeReplicationInstancesPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationSubnetGroupsMessageDescribeReplicationSubnetGroupsPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationTaskAssessmentResultsMessageDescribeReplicationTaskAssessmentResultsPaginateModel(
    BaseModel
):
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReplicationTasksMessageDescribeReplicationTasksPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSchemasMessageDescribeSchemasPaginateModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTableStatisticsMessageDescribeTableStatisticsPaginateModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConnectionsMessageTestConnectionSucceedsWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndpointsMessageEndpointDeletedWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationInstancesMessageReplicationInstanceAvailableWaitModel(
    BaseModel
):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationInstancesMessageReplicationInstanceDeletedWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationTasksMessageReplicationTaskDeletedWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationTasksMessageReplicationTaskReadyWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationTasksMessageReplicationTaskRunningWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReplicationTasksMessageReplicationTaskStoppedWaitModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    marker: Optional[str] = Field(default=None, alias="Marker")
    without_settings: Optional[bool] = Field(default=None, alias="WithoutSettings")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEndpointSettingsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    endpoint_settings: List[EndpointSettingModel] = Field(alias="EndpointSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointTypesResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    supported_endpoint_types: List[SupportedEndpointTypeModel] = Field(
        alias="SupportedEndpointTypes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventCategoriesResponseModel(BaseModel):
    event_category_group_list: List[EventCategoryGroupModel] = Field(
        alias="EventCategoryGroupList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    events: List[EventModel] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAdvisorLsaAnalysisResponseModel(BaseModel):
    analysis: List[FleetAdvisorLsaAnalysisResponseModel] = Field(alias="Analysis")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAdvisorSchemaObjectSummaryResponseModel(BaseModel):
    fleet_advisor_schema_objects: List[FleetAdvisorSchemaObjectResponseModel] = Field(
        alias="FleetAdvisorSchemaObjects"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrderableReplicationInstancesResponseModel(BaseModel):
    orderable_replication_instances: List[OrderableReplicationInstanceModel] = Field(
        alias="OrderableReplicationInstances"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRefreshSchemasStatusResponseModel(BaseModel):
    refresh_schemas_status: RefreshSchemasStatusModel = Field(
        alias="RefreshSchemasStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RefreshSchemasResponseModel(BaseModel):
    refresh_schemas_status: RefreshSchemasStatusModel = Field(
        alias="RefreshSchemasStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationInstanceTaskLogsResponseModel(BaseModel):
    replication_instance_arn: str = Field(alias="ReplicationInstanceArn")
    replication_instance_task_logs: List[ReplicationInstanceTaskLogModel] = Field(
        alias="ReplicationInstanceTaskLogs"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationTaskAssessmentResultsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    bucket_name: str = Field(alias="BucketName")
    replication_task_assessment_results: List[
        ReplicationTaskAssessmentResultModel
    ] = Field(alias="ReplicationTaskAssessmentResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationTaskIndividualAssessmentsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_task_individual_assessments: List[
        ReplicationTaskIndividualAssessmentModel
    ] = Field(alias="ReplicationTaskIndividualAssessments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableStatisticsResponseModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    table_statistics: List[TableStatisticsModel] = Field(alias="TableStatistics")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourcePendingMaintenanceActionsModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    pending_maintenance_action_details: Optional[
        List[PendingMaintenanceActionModel]
    ] = Field(default=None, alias="PendingMaintenanceActionDetails")


class ReloadTablesMessageRequestModel(BaseModel):
    replication_task_arn: str = Field(alias="ReplicationTaskArn")
    tables_to_reload: Sequence[TableToReloadModel] = Field(alias="TablesToReload")
    reload_option: Optional[Literal["data-reload", "validate-only"]] = Field(
        default=None, alias="ReloadOption"
    )


class ReplicationTaskAssessmentRunModel(BaseModel):
    replication_task_assessment_run_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskAssessmentRunArn"
    )
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    replication_task_assessment_run_creation_date: Optional[datetime] = Field(
        default=None, alias="ReplicationTaskAssessmentRunCreationDate"
    )
    assessment_progress: Optional[ReplicationTaskAssessmentRunProgressModel] = Field(
        default=None, alias="AssessmentProgress"
    )
    last_failure_message: Optional[str] = Field(
        default=None, alias="LastFailureMessage"
    )
    service_access_role_arn: Optional[str] = Field(
        default=None, alias="ServiceAccessRoleArn"
    )
    result_location_bucket: Optional[str] = Field(
        default=None, alias="ResultLocationBucket"
    )
    result_location_folder: Optional[str] = Field(
        default=None, alias="ResultLocationFolder"
    )
    result_encryption_mode: Optional[str] = Field(
        default=None, alias="ResultEncryptionMode"
    )
    result_kms_key_arn: Optional[str] = Field(default=None, alias="ResultKmsKeyArn")
    assessment_run_name: Optional[str] = Field(default=None, alias="AssessmentRunName")


class ReplicationTaskModel(BaseModel):
    replication_task_identifier: Optional[str] = Field(
        default=None, alias="ReplicationTaskIdentifier"
    )
    source_endpoint_arn: Optional[str] = Field(default=None, alias="SourceEndpointArn")
    target_endpoint_arn: Optional[str] = Field(default=None, alias="TargetEndpointArn")
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    migration_type: Optional[Literal["cdc", "full-load", "full-load-and-cdc"]] = Field(
        default=None, alias="MigrationType"
    )
    table_mappings: Optional[str] = Field(default=None, alias="TableMappings")
    replication_task_settings: Optional[str] = Field(
        default=None, alias="ReplicationTaskSettings"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    last_failure_message: Optional[str] = Field(
        default=None, alias="LastFailureMessage"
    )
    stop_reason: Optional[str] = Field(default=None, alias="StopReason")
    replication_task_creation_date: Optional[datetime] = Field(
        default=None, alias="ReplicationTaskCreationDate"
    )
    replication_task_start_date: Optional[datetime] = Field(
        default=None, alias="ReplicationTaskStartDate"
    )
    cdc_start_position: Optional[str] = Field(default=None, alias="CdcStartPosition")
    cdc_stop_position: Optional[str] = Field(default=None, alias="CdcStopPosition")
    recovery_checkpoint: Optional[str] = Field(default=None, alias="RecoveryCheckpoint")
    replication_task_arn: Optional[str] = Field(
        default=None, alias="ReplicationTaskArn"
    )
    replication_task_stats: Optional[ReplicationTaskStatsModel] = Field(
        default=None, alias="ReplicationTaskStats"
    )
    task_data: Optional[str] = Field(default=None, alias="TaskData")
    target_replication_instance_arn: Optional[str] = Field(
        default=None, alias="TargetReplicationInstanceArn"
    )


class SchemaResponseModel(BaseModel):
    code_line_count: Optional[int] = Field(default=None, alias="CodeLineCount")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    complexity: Optional[str] = Field(default=None, alias="Complexity")
    server: Optional[ServerShortInfoResponseModel] = Field(default=None, alias="Server")
    database_instance: Optional[DatabaseShortInfoResponseModel] = Field(
        default=None, alias="DatabaseInstance"
    )
    schema_id: Optional[str] = Field(default=None, alias="SchemaId")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    original_schema: Optional[SchemaShortInfoResponseModel] = Field(
        default=None, alias="OriginalSchema"
    )
    similarity: Optional[float] = Field(default=None, alias="Similarity")


class ReplicationSubnetGroupModel(BaseModel):
    replication_subnet_group_identifier: Optional[str] = Field(
        default=None, alias="ReplicationSubnetGroupIdentifier"
    )
    replication_subnet_group_description: Optional[str] = Field(
        default=None, alias="ReplicationSubnetGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_group_status: Optional[str] = Field(default=None, alias="SubnetGroupStatus")
    subnets: Optional[List[SubnetModel]] = Field(default=None, alias="Subnets")
    supported_network_types: Optional[List[str]] = Field(
        default=None, alias="SupportedNetworkTypes"
    )


class DescribeFleetAdvisorCollectorsResponseModel(BaseModel):
    collectors: List[CollectorResponseModel] = Field(alias="Collectors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointResponseModel(BaseModel):
    endpoint: EndpointModel = Field(alias="Endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEndpointResponseModel(BaseModel):
    endpoint: EndpointModel = Field(alias="Endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyEndpointResponseModel(BaseModel):
    endpoint: EndpointModel = Field(alias="Endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAdvisorDatabasesResponseModel(BaseModel):
    databases: List[DatabaseResponseModel] = Field(alias="Databases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplyPendingMaintenanceActionResponseModel(BaseModel):
    resource_pending_maintenance_actions: ResourcePendingMaintenanceActionsModel = (
        Field(alias="ResourcePendingMaintenanceActions")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePendingMaintenanceActionsResponseModel(BaseModel):
    pending_maintenance_actions: List[ResourcePendingMaintenanceActionsModel] = Field(
        alias="PendingMaintenanceActions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelReplicationTaskAssessmentRunResponseModel(BaseModel):
    replication_task_assessment_run: ReplicationTaskAssessmentRunModel = Field(
        alias="ReplicationTaskAssessmentRun"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteReplicationTaskAssessmentRunResponseModel(BaseModel):
    replication_task_assessment_run: ReplicationTaskAssessmentRunModel = Field(
        alias="ReplicationTaskAssessmentRun"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationTaskAssessmentRunsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_task_assessment_runs: List[ReplicationTaskAssessmentRunModel] = Field(
        alias="ReplicationTaskAssessmentRuns"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplicationTaskAssessmentRunResponseModel(BaseModel):
    replication_task_assessment_run: ReplicationTaskAssessmentRunModel = Field(
        alias="ReplicationTaskAssessmentRun"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationTasksResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_tasks: List[ReplicationTaskModel] = Field(alias="ReplicationTasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MoveReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplicationTaskAssessmentResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopReplicationTaskResponseModel(BaseModel):
    replication_task: ReplicationTaskModel = Field(alias="ReplicationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAdvisorSchemasResponseModel(BaseModel):
    fleet_advisor_schemas: List[SchemaResponseModel] = Field(
        alias="FleetAdvisorSchemas"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReplicationSubnetGroupResponseModel(BaseModel):
    replication_subnet_group: ReplicationSubnetGroupModel = Field(
        alias="ReplicationSubnetGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationSubnetGroupsResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_subnet_groups: List[ReplicationSubnetGroupModel] = Field(
        alias="ReplicationSubnetGroups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReplicationSubnetGroupResponseModel(BaseModel):
    replication_subnet_group: ReplicationSubnetGroupModel = Field(
        alias="ReplicationSubnetGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicationInstanceModel(BaseModel):
    replication_instance_identifier: Optional[str] = Field(
        default=None, alias="ReplicationInstanceIdentifier"
    )
    replication_instance_class: Optional[str] = Field(
        default=None, alias="ReplicationInstanceClass"
    )
    replication_instance_status: Optional[str] = Field(
        default=None, alias="ReplicationInstanceStatus"
    )
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    instance_create_time: Optional[datetime] = Field(
        default=None, alias="InstanceCreateTime"
    )
    vpc_security_groups: Optional[List[VpcSecurityGroupMembershipModel]] = Field(
        default=None, alias="VpcSecurityGroups"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    replication_subnet_group: Optional[ReplicationSubnetGroupModel] = Field(
        default=None, alias="ReplicationSubnetGroup"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    pending_modified_values: Optional[ReplicationPendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    replication_instance_arn: Optional[str] = Field(
        default=None, alias="ReplicationInstanceArn"
    )
    replication_instance_public_ip_address: Optional[str] = Field(
        default=None, alias="ReplicationInstancePublicIpAddress"
    )
    replication_instance_private_ip_address: Optional[str] = Field(
        default=None, alias="ReplicationInstancePrivateIpAddress"
    )
    replication_instance_public_ip_addresses: Optional[List[str]] = Field(
        default=None, alias="ReplicationInstancePublicIpAddresses"
    )
    replication_instance_private_ip_addresses: Optional[List[str]] = Field(
        default=None, alias="ReplicationInstancePrivateIpAddresses"
    )
    replication_instance_ipv6_addresses: Optional[List[str]] = Field(
        default=None, alias="ReplicationInstanceIpv6Addresses"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    secondary_availability_zone: Optional[str] = Field(
        default=None, alias="SecondaryAvailabilityZone"
    )
    free_until: Optional[datetime] = Field(default=None, alias="FreeUntil")
    dns_name_servers: Optional[str] = Field(default=None, alias="DnsNameServers")
    network_type: Optional[str] = Field(default=None, alias="NetworkType")


class CreateReplicationInstanceResponseModel(BaseModel):
    replication_instance: ReplicationInstanceModel = Field(alias="ReplicationInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteReplicationInstanceResponseModel(BaseModel):
    replication_instance: ReplicationInstanceModel = Field(alias="ReplicationInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReplicationInstancesResponseModel(BaseModel):
    marker: str = Field(alias="Marker")
    replication_instances: List[ReplicationInstanceModel] = Field(
        alias="ReplicationInstances"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReplicationInstanceResponseModel(BaseModel):
    replication_instance: ReplicationInstanceModel = Field(alias="ReplicationInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootReplicationInstanceResponseModel(BaseModel):
    replication_instance: ReplicationInstanceModel = Field(alias="ReplicationInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
