# Model Generated: Thu Mar  2 21:56:19 2023

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


class AmazonOpenSearchServerlessBufferingHintsModel(BaseModel):
    interval_in_seconds: Optional[int] = Field(default=None, alias="IntervalInSeconds")
    size_in_mbs: Optional[int] = Field(default=None, alias="SizeInMBs")


class AmazonOpenSearchServerlessRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class CloudWatchLoggingOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    log_stream_name: Optional[str] = Field(default=None, alias="LogStreamName")


class VpcConfigurationModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    role_arn: str = Field(alias="RoleARN")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")


class VpcConfigurationDescriptionModel(BaseModel):
    subnet_ids: List[str] = Field(alias="SubnetIds")
    role_arn: str = Field(alias="RoleARN")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    vpc_id: str = Field(alias="VpcId")


class AmazonopensearchserviceBufferingHintsModel(BaseModel):
    interval_in_seconds: Optional[int] = Field(default=None, alias="IntervalInSeconds")
    size_in_mbs: Optional[int] = Field(default=None, alias="SizeInMBs")


class AmazonopensearchserviceRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class BufferingHintsModel(BaseModel):
    size_in_mbs: Optional[int] = Field(default=None, alias="SizeInMBs")
    interval_in_seconds: Optional[int] = Field(default=None, alias="IntervalInSeconds")


class CopyCommandModel(BaseModel):
    data_table_name: str = Field(alias="DataTableName")
    data_table_columns: Optional[str] = Field(default=None, alias="DataTableColumns")
    copy_options: Optional[str] = Field(default=None, alias="CopyOptions")


class DeliveryStreamEncryptionConfigurationInputModel(BaseModel):
    key_type: Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"] = Field(alias="KeyType")
    key_arn: Optional[str] = Field(default=None, alias="KeyARN")


class KinesisStreamSourceConfigurationModel(BaseModel):
    kinesis_stream_arn: str = Field(alias="KinesisStreamARN")
    role_arn: str = Field(alias="RoleARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SchemaConfigurationModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    region: Optional[str] = Field(default=None, alias="Region")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class DeleteDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    allow_force_delete: Optional[bool] = Field(default=None, alias="AllowForceDelete")


class FailureDescriptionModel(BaseModel):
    type: Literal[
        "CREATE_ENI_FAILED",
        "CREATE_KMS_GRANT_FAILED",
        "DELETE_ENI_FAILED",
        "DISABLED_KMS_KEY",
        "ENI_ACCESS_DENIED",
        "INVALID_KMS_KEY",
        "KMS_ACCESS_DENIED",
        "KMS_KEY_NOT_FOUND",
        "KMS_OPT_IN_REQUIRED",
        "RETIRE_KMS_GRANT_FAILED",
        "SECURITY_GROUP_ACCESS_DENIED",
        "SECURITY_GROUP_NOT_FOUND",
        "SUBNET_ACCESS_DENIED",
        "SUBNET_NOT_FOUND",
        "UNKNOWN_ERROR",
    ] = Field(alias="Type")
    details: str = Field(alias="Details")


class DescribeDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_destination_id: Optional[str] = Field(
        default=None, alias="ExclusiveStartDestinationId"
    )


class HiveJsonSerDeModel(BaseModel):
    timestamp_formats: Optional[Sequence[str]] = Field(
        default=None, alias="TimestampFormats"
    )


class OpenXJsonSerDeModel(BaseModel):
    convert_dots_in_json_keys_to_underscores: Optional[bool] = Field(
        default=None, alias="ConvertDotsInJsonKeysToUnderscores"
    )
    case_insensitive: Optional[bool] = Field(default=None, alias="CaseInsensitive")
    column_to_json_key_mappings: Optional[Mapping[str, str]] = Field(
        default=None, alias="ColumnToJsonKeyMappings"
    )


class RetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class ElasticsearchBufferingHintsModel(BaseModel):
    interval_in_seconds: Optional[int] = Field(default=None, alias="IntervalInSeconds")
    size_in_mbs: Optional[int] = Field(default=None, alias="SizeInMBs")


class ElasticsearchRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class KMSEncryptionConfigModel(BaseModel):
    aws_kms_key_arn: str = Field(alias="AWSKMSKeyARN")


class HttpEndpointBufferingHintsModel(BaseModel):
    size_in_mbs: Optional[int] = Field(default=None, alias="SizeInMBs")
    interval_in_seconds: Optional[int] = Field(default=None, alias="IntervalInSeconds")


class HttpEndpointCommonAttributeModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: str = Field(alias="AttributeValue")


class HttpEndpointConfigurationModel(BaseModel):
    url: str = Field(alias="Url")
    name: Optional[str] = Field(default=None, alias="Name")
    access_key: Optional[str] = Field(default=None, alias="AccessKey")


class HttpEndpointDescriptionModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    name: Optional[str] = Field(default=None, alias="Name")


class HttpEndpointRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class KinesisStreamSourceDescriptionModel(BaseModel):
    kinesis_stream_arn: Optional[str] = Field(default=None, alias="KinesisStreamARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    delivery_start_timestamp: Optional[datetime] = Field(
        default=None, alias="DeliveryStartTimestamp"
    )


class ListDeliveryStreamsInputRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    delivery_stream_type: Optional[
        Literal["DirectPut", "KinesisStreamAsSource"]
    ] = Field(default=None, alias="DeliveryStreamType")
    exclusive_start_delivery_stream_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartDeliveryStreamName"
    )


class ListTagsForDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    exclusive_start_tag_key: Optional[str] = Field(
        default=None, alias="ExclusiveStartTagKey"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")


class OrcSerDeModel(BaseModel):
    stripe_size_bytes: Optional[int] = Field(default=None, alias="StripeSizeBytes")
    block_size_bytes: Optional[int] = Field(default=None, alias="BlockSizeBytes")
    row_index_stride: Optional[int] = Field(default=None, alias="RowIndexStride")
    enable_padding: Optional[bool] = Field(default=None, alias="EnablePadding")
    padding_tolerance: Optional[float] = Field(default=None, alias="PaddingTolerance")
    compression: Optional[Literal["NONE", "SNAPPY", "ZLIB"]] = Field(
        default=None, alias="Compression"
    )
    bloom_filter_columns: Optional[Sequence[str]] = Field(
        default=None, alias="BloomFilterColumns"
    )
    bloom_filter_false_positive_probability: Optional[float] = Field(
        default=None, alias="BloomFilterFalsePositiveProbability"
    )
    dictionary_key_threshold: Optional[float] = Field(
        default=None, alias="DictionaryKeyThreshold"
    )
    format_version: Optional[Literal["V0_11", "V0_12"]] = Field(
        default=None, alias="FormatVersion"
    )


class ParquetSerDeModel(BaseModel):
    block_size_bytes: Optional[int] = Field(default=None, alias="BlockSizeBytes")
    page_size_bytes: Optional[int] = Field(default=None, alias="PageSizeBytes")
    compression: Optional[Literal["GZIP", "SNAPPY", "UNCOMPRESSED"]] = Field(
        default=None, alias="Compression"
    )
    enable_dictionary_compression: Optional[bool] = Field(
        default=None, alias="EnableDictionaryCompression"
    )
    max_padding_bytes: Optional[int] = Field(default=None, alias="MaxPaddingBytes")
    writer_version: Optional[Literal["V1", "V2"]] = Field(
        default=None, alias="WriterVersion"
    )


class ProcessorParameterModel(BaseModel):
    parameter_name: Literal[
        "BufferIntervalInSeconds",
        "BufferSizeInMBs",
        "Delimiter",
        "JsonParsingEngine",
        "LambdaArn",
        "MetadataExtractionQuery",
        "NumberOfRetries",
        "RoleArn",
        "SubRecordType",
    ] = Field(alias="ParameterName")
    parameter_value: str = Field(alias="ParameterValue")


class RecordModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Data")


class PutRecordBatchResponseEntryModel(BaseModel):
    record_id: Optional[str] = Field(default=None, alias="RecordId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class RedshiftRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class SplunkRetryOptionsModel(BaseModel):
    duration_in_seconds: Optional[int] = Field(default=None, alias="DurationInSeconds")


class StopDeliveryStreamEncryptionInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")


class UntagDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class StartDeliveryStreamEncryptionInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    delivery_stream_encryption_configuration_input: Optional[
        DeliveryStreamEncryptionConfigurationInputModel
    ] = Field(default=None, alias="DeliveryStreamEncryptionConfigurationInput")


class TagDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateDeliveryStreamOutputModel(BaseModel):
    delivery_stream_arn: str = Field(alias="DeliveryStreamARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeliveryStreamsOutputModel(BaseModel):
    delivery_stream_names: List[str] = Field(alias="DeliveryStreamNames")
    has_more_delivery_streams: bool = Field(alias="HasMoreDeliveryStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForDeliveryStreamOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    has_more_tags: bool = Field(alias="HasMoreTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRecordOutputModel(BaseModel):
    record_id: str = Field(alias="RecordId")
    encrypted: bool = Field(alias="Encrypted")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeliveryStreamEncryptionConfigurationModel(BaseModel):
    key_arn: Optional[str] = Field(default=None, alias="KeyARN")
    key_type: Optional[Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]] = Field(
        default=None, alias="KeyType"
    )
    status: Optional[
        Literal[
            "DISABLED",
            "DISABLING",
            "DISABLING_FAILED",
            "ENABLED",
            "ENABLING",
            "ENABLING_FAILED",
        ]
    ] = Field(default=None, alias="Status")
    failure_description: Optional[FailureDescriptionModel] = Field(
        default=None, alias="FailureDescription"
    )


class DeserializerModel(BaseModel):
    open_xjson_ser_de: Optional[OpenXJsonSerDeModel] = Field(
        default=None, alias="OpenXJsonSerDe"
    )
    hive_json_ser_de: Optional[HiveJsonSerDeModel] = Field(
        default=None, alias="HiveJsonSerDe"
    )


class DynamicPartitioningConfigurationModel(BaseModel):
    retry_options: Optional[RetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class EncryptionConfigurationModel(BaseModel):
    no_encryption_config: Optional[Literal["NoEncryption"]] = Field(
        default=None, alias="NoEncryptionConfig"
    )
    kms_encryption_config: Optional[KMSEncryptionConfigModel] = Field(
        default=None, alias="KMSEncryptionConfig"
    )


class HttpEndpointRequestConfigurationModel(BaseModel):
    content_encoding: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="ContentEncoding"
    )
    common_attributes: Optional[Sequence[HttpEndpointCommonAttributeModel]] = Field(
        default=None, alias="CommonAttributes"
    )


class SourceDescriptionModel(BaseModel):
    kinesis_stream_source_description: Optional[
        KinesisStreamSourceDescriptionModel
    ] = Field(default=None, alias="KinesisStreamSourceDescription")


class SerializerModel(BaseModel):
    parquet_ser_de: Optional[ParquetSerDeModel] = Field(
        default=None, alias="ParquetSerDe"
    )
    orc_ser_de: Optional[OrcSerDeModel] = Field(default=None, alias="OrcSerDe")


class ProcessorModel(BaseModel):
    type: Literal[
        "AppendDelimiterToRecord", "Lambda", "MetadataExtraction", "RecordDeAggregation"
    ] = Field(alias="Type")
    parameters: Optional[Sequence[ProcessorParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class PutRecordBatchInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    records: Sequence[RecordModel] = Field(alias="Records")


class PutRecordInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    record: RecordModel = Field(alias="Record")


class PutRecordBatchOutputModel(BaseModel):
    failed_put_count: int = Field(alias="FailedPutCount")
    encrypted: bool = Field(alias="Encrypted")
    request_responses: List[PutRecordBatchResponseEntryModel] = Field(
        alias="RequestResponses"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputFormatConfigurationModel(BaseModel):
    deserializer: Optional[DeserializerModel] = Field(
        default=None, alias="Deserializer"
    )


class S3DestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    bucket_arn: str = Field(alias="BucketARN")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    buffering_hints: Optional[BufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    compression_format: Optional[
        Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
    ] = Field(default=None, alias="CompressionFormat")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class S3DestinationDescriptionModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    bucket_arn: str = Field(alias="BucketARN")
    buffering_hints: BufferingHintsModel = Field(alias="BufferingHints")
    compression_format: Literal[
        "GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"
    ] = Field(alias="CompressionFormat")
    encryption_configuration: EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class S3DestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    bucket_arn: Optional[str] = Field(default=None, alias="BucketARN")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    buffering_hints: Optional[BufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    compression_format: Optional[
        Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
    ] = Field(default=None, alias="CompressionFormat")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class OutputFormatConfigurationModel(BaseModel):
    serializer: Optional[SerializerModel] = Field(default=None, alias="Serializer")


class ProcessingConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    processors: Optional[Sequence[ProcessorModel]] = Field(
        default=None, alias="Processors"
    )


class DataFormatConversionConfigurationModel(BaseModel):
    schema_configuration: Optional[SchemaConfigurationModel] = Field(
        default=None, alias="SchemaConfiguration"
    )
    input_format_configuration: Optional[InputFormatConfigurationModel] = Field(
        default=None, alias="InputFormatConfiguration"
    )
    output_format_configuration: Optional[OutputFormatConfigurationModel] = Field(
        default=None, alias="OutputFormatConfiguration"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AmazonOpenSearchServerlessDestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    index_name: str = Field(alias="IndexName")
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    collection_endpoint: Optional[str] = Field(default=None, alias="CollectionEndpoint")
    buffering_hints: Optional[AmazonOpenSearchServerlessBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonOpenSearchServerlessRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class AmazonOpenSearchServerlessDestinationDescriptionModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    collection_endpoint: Optional[str] = Field(default=None, alias="CollectionEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    buffering_hints: Optional[AmazonOpenSearchServerlessBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonOpenSearchServerlessRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration_description: Optional[VpcConfigurationDescriptionModel] = Field(
        default=None, alias="VpcConfigurationDescription"
    )


class AmazonOpenSearchServerlessDestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    collection_endpoint: Optional[str] = Field(default=None, alias="CollectionEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    buffering_hints: Optional[AmazonOpenSearchServerlessBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonOpenSearchServerlessRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class AmazonopensearchserviceDestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    index_name: str = Field(alias="IndexName")
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[AmazonopensearchserviceBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonopensearchserviceRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class AmazonopensearchserviceDestinationDescriptionModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[AmazonopensearchserviceBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonopensearchserviceRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration_description: Optional[VpcConfigurationDescriptionModel] = Field(
        default=None, alias="VpcConfigurationDescription"
    )


class AmazonopensearchserviceDestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[AmazonopensearchserviceBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[AmazonopensearchserviceRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class ElasticsearchDestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    index_name: str = Field(alias="IndexName")
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[ElasticsearchBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[ElasticsearchRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class ElasticsearchDestinationDescriptionModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[ElasticsearchBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[ElasticsearchRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllDocuments", "FailedDocumentsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    vpc_configuration_description: Optional[VpcConfigurationDescriptionModel] = Field(
        default=None, alias="VpcConfigurationDescription"
    )


class ElasticsearchDestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    domain_arn: Optional[str] = Field(default=None, alias="DomainARN")
    cluster_endpoint: Optional[str] = Field(default=None, alias="ClusterEndpoint")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    index_rotation_period: Optional[
        Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
    ] = Field(default=None, alias="IndexRotationPeriod")
    buffering_hints: Optional[ElasticsearchBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    retry_options: Optional[ElasticsearchRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class HttpEndpointDestinationConfigurationModel(BaseModel):
    endpoint_configuration: HttpEndpointConfigurationModel = Field(
        alias="EndpointConfiguration"
    )
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    buffering_hints: Optional[HttpEndpointBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    request_configuration: Optional[HttpEndpointRequestConfigurationModel] = Field(
        default=None, alias="RequestConfiguration"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    retry_options: Optional[HttpEndpointRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllData", "FailedDataOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )


class HttpEndpointDestinationDescriptionModel(BaseModel):
    endpoint_configuration: Optional[HttpEndpointDescriptionModel] = Field(
        default=None, alias="EndpointConfiguration"
    )
    buffering_hints: Optional[HttpEndpointBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    request_configuration: Optional[HttpEndpointRequestConfigurationModel] = Field(
        default=None, alias="RequestConfiguration"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    retry_options: Optional[HttpEndpointRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllData", "FailedDataOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )


class HttpEndpointDestinationUpdateModel(BaseModel):
    endpoint_configuration: Optional[HttpEndpointConfigurationModel] = Field(
        default=None, alias="EndpointConfiguration"
    )
    buffering_hints: Optional[HttpEndpointBufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    request_configuration: Optional[HttpEndpointRequestConfigurationModel] = Field(
        default=None, alias="RequestConfiguration"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    retry_options: Optional[HttpEndpointRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllData", "FailedDataOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )


class RedshiftDestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    cluster_jdbcurl: str = Field(alias="ClusterJDBCURL")
    copy_command: CopyCommandModel = Field(alias="CopyCommand")
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    retry_options: Optional[RedshiftRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_configuration: Optional[S3DestinationConfigurationModel] = Field(
        default=None, alias="S3BackupConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class RedshiftDestinationDescriptionModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    cluster_jdbcurl: str = Field(alias="ClusterJDBCURL")
    copy_command: CopyCommandModel = Field(alias="CopyCommand")
    username: str = Field(alias="Username")
    s3_destination_description: S3DestinationDescriptionModel = Field(
        alias="S3DestinationDescription"
    )
    retry_options: Optional[RedshiftRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3BackupDescription"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class RedshiftDestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    cluster_jdbcurl: Optional[str] = Field(default=None, alias="ClusterJDBCURL")
    copy_command: Optional[CopyCommandModel] = Field(default=None, alias="CopyCommand")
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")
    retry_options: Optional[RedshiftRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3BackupUpdate"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class SplunkDestinationConfigurationModel(BaseModel):
    hecendpoint: str = Field(alias="HECEndpoint")
    hecendpoint_type: Literal["Event", "Raw"] = Field(alias="HECEndpointType")
    hectoken: str = Field(alias="HECToken")
    s3_configuration: S3DestinationConfigurationModel = Field(alias="S3Configuration")
    hecacknowledgment_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="HECAcknowledgmentTimeoutInSeconds"
    )
    retry_options: Optional[SplunkRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllEvents", "FailedEventsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class SplunkDestinationDescriptionModel(BaseModel):
    hecendpoint: Optional[str] = Field(default=None, alias="HECEndpoint")
    hecendpoint_type: Optional[Literal["Event", "Raw"]] = Field(
        default=None, alias="HECEndpointType"
    )
    hectoken: Optional[str] = Field(default=None, alias="HECToken")
    hecacknowledgment_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="HECAcknowledgmentTimeoutInSeconds"
    )
    retry_options: Optional[SplunkRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllEvents", "FailedEventsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class SplunkDestinationUpdateModel(BaseModel):
    hecendpoint: Optional[str] = Field(default=None, alias="HECEndpoint")
    hecendpoint_type: Optional[Literal["Event", "Raw"]] = Field(
        default=None, alias="HECEndpointType"
    )
    hectoken: Optional[str] = Field(default=None, alias="HECToken")
    hecacknowledgment_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="HECAcknowledgmentTimeoutInSeconds"
    )
    retry_options: Optional[SplunkRetryOptionsModel] = Field(
        default=None, alias="RetryOptions"
    )
    s3_backup_mode: Optional[Literal["AllEvents", "FailedEventsOnly"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3Update"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )


class ExtendedS3DestinationConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    bucket_arn: str = Field(alias="BucketARN")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    buffering_hints: Optional[BufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    compression_format: Optional[
        Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
    ] = Field(default=None, alias="CompressionFormat")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_configuration: Optional[S3DestinationConfigurationModel] = Field(
        default=None, alias="S3BackupConfiguration"
    )
    data_format_conversion_configuration: Optional[
        DataFormatConversionConfigurationModel
    ] = Field(default=None, alias="DataFormatConversionConfiguration")
    dynamic_partitioning_configuration: Optional[
        DynamicPartitioningConfigurationModel
    ] = Field(default=None, alias="DynamicPartitioningConfiguration")


class ExtendedS3DestinationDescriptionModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    bucket_arn: str = Field(alias="BucketARN")
    buffering_hints: BufferingHintsModel = Field(alias="BufferingHints")
    compression_format: Literal[
        "GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"
    ] = Field(alias="CompressionFormat")
    encryption_configuration: EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3BackupDescription"
    )
    data_format_conversion_configuration: Optional[
        DataFormatConversionConfigurationModel
    ] = Field(default=None, alias="DataFormatConversionConfiguration")
    dynamic_partitioning_configuration: Optional[
        DynamicPartitioningConfigurationModel
    ] = Field(default=None, alias="DynamicPartitioningConfiguration")


class ExtendedS3DestinationUpdateModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
    bucket_arn: Optional[str] = Field(default=None, alias="BucketARN")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    error_output_prefix: Optional[str] = Field(default=None, alias="ErrorOutputPrefix")
    buffering_hints: Optional[BufferingHintsModel] = Field(
        default=None, alias="BufferingHints"
    )
    compression_format: Optional[
        Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
    ] = Field(default=None, alias="CompressionFormat")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    cloud_watch_logging_options: Optional[CloudWatchLoggingOptionsModel] = Field(
        default=None, alias="CloudWatchLoggingOptions"
    )
    processing_configuration: Optional[ProcessingConfigurationModel] = Field(
        default=None, alias="ProcessingConfiguration"
    )
    s3_backup_mode: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="S3BackupMode"
    )
    s3_backup_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3BackupUpdate"
    )
    data_format_conversion_configuration: Optional[
        DataFormatConversionConfigurationModel
    ] = Field(default=None, alias="DataFormatConversionConfiguration")
    dynamic_partitioning_configuration: Optional[
        DynamicPartitioningConfigurationModel
    ] = Field(default=None, alias="DynamicPartitioningConfiguration")


class CreateDeliveryStreamInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    delivery_stream_type: Optional[
        Literal["DirectPut", "KinesisStreamAsSource"]
    ] = Field(default=None, alias="DeliveryStreamType")
    kinesis_stream_source_configuration: Optional[
        KinesisStreamSourceConfigurationModel
    ] = Field(default=None, alias="KinesisStreamSourceConfiguration")
    delivery_stream_encryption_configuration_input: Optional[
        DeliveryStreamEncryptionConfigurationInputModel
    ] = Field(default=None, alias="DeliveryStreamEncryptionConfigurationInput")
    s3_destination_configuration: Optional[S3DestinationConfigurationModel] = Field(
        default=None, alias="S3DestinationConfiguration"
    )
    extended_s3_destination_configuration: Optional[
        ExtendedS3DestinationConfigurationModel
    ] = Field(default=None, alias="ExtendedS3DestinationConfiguration")
    redshift_destination_configuration: Optional[
        RedshiftDestinationConfigurationModel
    ] = Field(default=None, alias="RedshiftDestinationConfiguration")
    elasticsearch_destination_configuration: Optional[
        ElasticsearchDestinationConfigurationModel
    ] = Field(default=None, alias="ElasticsearchDestinationConfiguration")
    amazonopensearchservice_destination_configuration: Optional[
        AmazonopensearchserviceDestinationConfigurationModel
    ] = Field(default=None, alias="AmazonopensearchserviceDestinationConfiguration")
    splunk_destination_configuration: Optional[
        SplunkDestinationConfigurationModel
    ] = Field(default=None, alias="SplunkDestinationConfiguration")
    http_endpoint_destination_configuration: Optional[
        HttpEndpointDestinationConfigurationModel
    ] = Field(default=None, alias="HttpEndpointDestinationConfiguration")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    amazon_open_search_serverless_destination_configuration: Optional[
        AmazonOpenSearchServerlessDestinationConfigurationModel
    ] = Field(default=None, alias="AmazonOpenSearchServerlessDestinationConfiguration")


class DestinationDescriptionModel(BaseModel):
    destination_id: str = Field(alias="DestinationId")
    s3_destination_description: Optional[S3DestinationDescriptionModel] = Field(
        default=None, alias="S3DestinationDescription"
    )
    extended_s3_destination_description: Optional[
        ExtendedS3DestinationDescriptionModel
    ] = Field(default=None, alias="ExtendedS3DestinationDescription")
    redshift_destination_description: Optional[
        RedshiftDestinationDescriptionModel
    ] = Field(default=None, alias="RedshiftDestinationDescription")
    elasticsearch_destination_description: Optional[
        ElasticsearchDestinationDescriptionModel
    ] = Field(default=None, alias="ElasticsearchDestinationDescription")
    amazonopensearchservice_destination_description: Optional[
        AmazonopensearchserviceDestinationDescriptionModel
    ] = Field(default=None, alias="AmazonopensearchserviceDestinationDescription")
    splunk_destination_description: Optional[SplunkDestinationDescriptionModel] = Field(
        default=None, alias="SplunkDestinationDescription"
    )
    http_endpoint_destination_description: Optional[
        HttpEndpointDestinationDescriptionModel
    ] = Field(default=None, alias="HttpEndpointDestinationDescription")
    amazon_open_search_serverless_destination_description: Optional[
        AmazonOpenSearchServerlessDestinationDescriptionModel
    ] = Field(default=None, alias="AmazonOpenSearchServerlessDestinationDescription")


class UpdateDestinationInputRequestModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    current_delivery_stream_version_id: str = Field(
        alias="CurrentDeliveryStreamVersionId"
    )
    destination_id: str = Field(alias="DestinationId")
    s3_destination_update: Optional[S3DestinationUpdateModel] = Field(
        default=None, alias="S3DestinationUpdate"
    )
    extended_s3_destination_update: Optional[ExtendedS3DestinationUpdateModel] = Field(
        default=None, alias="ExtendedS3DestinationUpdate"
    )
    redshift_destination_update: Optional[RedshiftDestinationUpdateModel] = Field(
        default=None, alias="RedshiftDestinationUpdate"
    )
    elasticsearch_destination_update: Optional[
        ElasticsearchDestinationUpdateModel
    ] = Field(default=None, alias="ElasticsearchDestinationUpdate")
    amazonopensearchservice_destination_update: Optional[
        AmazonopensearchserviceDestinationUpdateModel
    ] = Field(default=None, alias="AmazonopensearchserviceDestinationUpdate")
    splunk_destination_update: Optional[SplunkDestinationUpdateModel] = Field(
        default=None, alias="SplunkDestinationUpdate"
    )
    http_endpoint_destination_update: Optional[
        HttpEndpointDestinationUpdateModel
    ] = Field(default=None, alias="HttpEndpointDestinationUpdate")
    amazon_open_search_serverless_destination_update: Optional[
        AmazonOpenSearchServerlessDestinationUpdateModel
    ] = Field(default=None, alias="AmazonOpenSearchServerlessDestinationUpdate")


class DeliveryStreamDescriptionModel(BaseModel):
    delivery_stream_name: str = Field(alias="DeliveryStreamName")
    delivery_stream_arn: str = Field(alias="DeliveryStreamARN")
    delivery_stream_status: Literal[
        "ACTIVE", "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED"
    ] = Field(alias="DeliveryStreamStatus")
    delivery_stream_type: Literal["DirectPut", "KinesisStreamAsSource"] = Field(
        alias="DeliveryStreamType"
    )
    version_id: str = Field(alias="VersionId")
    destinations: List[DestinationDescriptionModel] = Field(alias="Destinations")
    has_more_destinations: bool = Field(alias="HasMoreDestinations")
    failure_description: Optional[FailureDescriptionModel] = Field(
        default=None, alias="FailureDescription"
    )
    delivery_stream_encryption_configuration: Optional[
        DeliveryStreamEncryptionConfigurationModel
    ] = Field(default=None, alias="DeliveryStreamEncryptionConfiguration")
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )
    source: Optional[SourceDescriptionModel] = Field(default=None, alias="Source")


class DescribeDeliveryStreamOutputModel(BaseModel):
    delivery_stream_description: DeliveryStreamDescriptionModel = Field(
        alias="DeliveryStreamDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
