# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CloudWatchLoggingOptionModel(BaseModel):
    log_stream_arn: str = Field(alias="LogStreamARN")
    role_arn: str = Field(alias="RoleARN")


class CloudWatchLoggingOptionDescriptionModel(BaseModel):
    log_stream_arn: str = Field(alias="LogStreamARN")
    role_arn: str = Field(alias="RoleARN")
    cloud_watch_logging_option_id: Optional[str] = Field(
        default=None, alias="CloudWatchLoggingOptionId"
    )


class ApplicationSummaryModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_arn: str = Field(alias="ApplicationARN")
    application_status: Literal[
        "DELETING", "READY", "RUNNING", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="ApplicationStatus")


class CloudWatchLoggingOptionUpdateModel(BaseModel):
    cloud_watch_logging_option_id: str = Field(alias="CloudWatchLoggingOptionId")
    log_stream_arnupdate: Optional[str] = Field(
        default=None, alias="LogStreamARNUpdate"
    )
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class CSVMappingParametersModel(BaseModel):
    record_row_delimiter: str = Field(alias="RecordRowDelimiter")
    record_column_delimiter: str = Field(alias="RecordColumnDelimiter")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteApplicationCloudWatchLoggingOptionRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    cloud_watch_logging_option_id: str = Field(alias="CloudWatchLoggingOptionId")


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


class DescribeApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")


class DestinationSchemaModel(BaseModel):
    record_format_type: Literal["CSV", "JSON"] = Field(alias="RecordFormatType")


class InputStartingPositionConfigurationModel(BaseModel):
    input_starting_position: Optional[
        Literal["LAST_STOPPED_POINT", "NOW", "TRIM_HORIZON"]
    ] = Field(default=None, alias="InputStartingPosition")


class S3ConfigurationModel(BaseModel):
    role_arn: str = Field(alias="RoleARN")
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")


class InputParallelismModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")


class KinesisFirehoseInputDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisStreamsInputDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class InputLambdaProcessorDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class InputLambdaProcessorModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class InputLambdaProcessorUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class InputParallelismUpdateModel(BaseModel):
    count_update: Optional[int] = Field(default=None, alias="CountUpdate")


class RecordColumnModel(BaseModel):
    name: str = Field(alias="Name")
    sql_type: str = Field(alias="SqlType")
    mapping: Optional[str] = Field(default=None, alias="Mapping")


class KinesisFirehoseInputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class KinesisStreamsInputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class KinesisFirehoseInputUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class KinesisStreamsInputUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class JSONMappingParametersModel(BaseModel):
    record_row_path: str = Field(alias="RecordRowPath")


class KinesisFirehoseOutputDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisFirehoseOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class KinesisFirehoseOutputUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class KinesisStreamsOutputDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class KinesisStreamsOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class KinesisStreamsOutputUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class LambdaOutputDescriptionModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")


class LambdaOutputModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    role_arn: str = Field(alias="RoleARN")


class LambdaOutputUpdateModel(BaseModel):
    resource_arnupdate: Optional[str] = Field(default=None, alias="ResourceARNUpdate")
    role_arnupdate: Optional[str] = Field(default=None, alias="RoleARNUpdate")


class ListApplicationsRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    exclusive_start_application_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartApplicationName"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class S3ReferenceDataSourceDescriptionModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")
    reference_role_arn: str = Field(alias="ReferenceRoleARN")


class S3ReferenceDataSourceModel(BaseModel):
    bucket_arn: str = Field(alias="BucketARN")
    file_key: str = Field(alias="FileKey")
    reference_role_arn: str = Field(alias="ReferenceRoleARN")


class S3ReferenceDataSourceUpdateModel(BaseModel):
    bucket_arnupdate: Optional[str] = Field(default=None, alias="BucketARNUpdate")
    file_key_update: Optional[str] = Field(default=None, alias="FileKeyUpdate")
    reference_role_arnupdate: Optional[str] = Field(
        default=None, alias="ReferenceRoleARNUpdate"
    )


class StopApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AddApplicationCloudWatchLoggingOptionRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    cloud_watch_logging_option: CloudWatchLoggingOptionModel = Field(
        alias="CloudWatchLoggingOption"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateApplicationResponseModel(BaseModel):
    application_summary: ApplicationSummaryModel = Field(alias="ApplicationSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    application_summaries: List[ApplicationSummaryModel] = Field(
        alias="ApplicationSummaries"
    )
    has_more_applications: bool = Field(alias="HasMoreApplications")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InputConfigurationModel(BaseModel):
    id: str = Field(alias="Id")
    input_starting_position_configuration: InputStartingPositionConfigurationModel = (
        Field(alias="InputStartingPositionConfiguration")
    )


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


class StartApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    input_configurations: Sequence[InputConfigurationModel] = Field(
        alias="InputConfigurations"
    )


class AddApplicationInputProcessingConfigurationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    input_id: str = Field(alias="InputId")
    input_processing_configuration: InputProcessingConfigurationModel = Field(
        alias="InputProcessingConfiguration"
    )


class DiscoverInputSchemaRequestModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    role_arn: Optional[str] = Field(default=None, alias="RoleARN")
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


class AddApplicationOutputRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    output: OutputModel = Field(alias="Output")


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


class AddApplicationInputRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    input: InputModel = Field(alias="Input")


class CreateApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_description: Optional[str] = Field(
        default=None, alias="ApplicationDescription"
    )
    inputs: Optional[Sequence[InputModel]] = Field(default=None, alias="Inputs")
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="Outputs")
    cloud_watch_logging_options: Optional[
        Sequence[CloudWatchLoggingOptionModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptions")
    application_code: Optional[str] = Field(default=None, alias="ApplicationCode")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ApplicationDetailModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    application_arn: str = Field(alias="ApplicationARN")
    application_status: Literal[
        "DELETING", "READY", "RUNNING", "STARTING", "STOPPING", "UPDATING"
    ] = Field(alias="ApplicationStatus")
    application_version_id: int = Field(alias="ApplicationVersionId")
    application_description: Optional[str] = Field(
        default=None, alias="ApplicationDescription"
    )
    create_timestamp: Optional[datetime] = Field(default=None, alias="CreateTimestamp")
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )
    input_descriptions: Optional[List[InputDescriptionModel]] = Field(
        default=None, alias="InputDescriptions"
    )
    output_descriptions: Optional[List[OutputDescriptionModel]] = Field(
        default=None, alias="OutputDescriptions"
    )
    reference_data_source_descriptions: Optional[
        List[ReferenceDataSourceDescriptionModel]
    ] = Field(default=None, alias="ReferenceDataSourceDescriptions")
    cloud_watch_logging_option_descriptions: Optional[
        List[CloudWatchLoggingOptionDescriptionModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptionDescriptions")
    application_code: Optional[str] = Field(default=None, alias="ApplicationCode")


class AddApplicationReferenceDataSourceRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    reference_data_source: ReferenceDataSourceModel = Field(alias="ReferenceDataSource")


class ApplicationUpdateModel(BaseModel):
    input_updates: Optional[Sequence[InputUpdateModel]] = Field(
        default=None, alias="InputUpdates"
    )
    application_code_update: Optional[str] = Field(
        default=None, alias="ApplicationCodeUpdate"
    )
    output_updates: Optional[Sequence[OutputUpdateModel]] = Field(
        default=None, alias="OutputUpdates"
    )
    reference_data_source_updates: Optional[
        Sequence[ReferenceDataSourceUpdateModel]
    ] = Field(default=None, alias="ReferenceDataSourceUpdates")
    cloud_watch_logging_option_updates: Optional[
        Sequence[CloudWatchLoggingOptionUpdateModel]
    ] = Field(default=None, alias="CloudWatchLoggingOptionUpdates")


class DescribeApplicationResponseModel(BaseModel):
    application_detail: ApplicationDetailModel = Field(alias="ApplicationDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    current_application_version_id: int = Field(alias="CurrentApplicationVersionId")
    application_update: ApplicationUpdateModel = Field(alias="ApplicationUpdate")
