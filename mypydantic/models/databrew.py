# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AllowedStatisticsModel(BaseModel):
    statistics: Sequence[str] = Field(alias="Statistics")


class BatchDeleteRecipeVersionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_versions: Sequence[str] = Field(alias="RecipeVersions")


class RecipeVersionErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ColumnSelectorModel(BaseModel):
    regex: Optional[str] = Field(default=None, alias="Regex")
    name: Optional[str] = Field(default=None, alias="Name")


class ConditionExpressionModel(BaseModel):
    condition: str = Field(alias="Condition")
    target_column: str = Field(alias="TargetColumn")
    value: Optional[str] = Field(default=None, alias="Value")


class JobSampleModel(BaseModel):
    mode: Optional[Literal["CUSTOM_ROWS", "FULL_DATASET"]] = Field(
        default=None, alias="Mode"
    )
    size: Optional[int] = Field(default=None, alias="Size")


class S3LocationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: Optional[str] = Field(default=None, alias="Key")
    bucket_owner: Optional[str] = Field(default=None, alias="BucketOwner")


class ValidationConfigurationModel(BaseModel):
    ruleset_arn: str = Field(alias="RulesetArn")
    validation_mode: Optional[Literal["CHECK_ALL"]] = Field(
        default=None, alias="ValidationMode"
    )


class SampleModel(BaseModel):
    type: Literal["FIRST_N", "LAST_N", "RANDOM"] = Field(alias="Type")
    size: Optional[int] = Field(default=None, alias="Size")


class RecipeReferenceModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")


class CreateScheduleRequestModel(BaseModel):
    cron_expression: str = Field(alias="CronExpression")
    name: str = Field(alias="Name")
    job_names: Optional[Sequence[str]] = Field(default=None, alias="JobNames")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CsvOptionsModel(BaseModel):
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    header_row: Optional[bool] = Field(default=None, alias="HeaderRow")


class CsvOutputOptionsModel(BaseModel):
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")


class DatetimeOptionsModel(BaseModel):
    format: str = Field(alias="Format")
    timezone_offset: Optional[str] = Field(default=None, alias="TimezoneOffset")
    locale_code: Optional[str] = Field(default=None, alias="LocaleCode")


class FilterExpressionModel(BaseModel):
    expression: str = Field(alias="Expression")
    values_map: Mapping[str, str] = Field(alias="ValuesMap")


class DeleteDatasetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteJobRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteProjectRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteRecipeVersionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_version: str = Field(alias="RecipeVersion")


class DeleteRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteScheduleRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeDatasetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeJobRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeJobRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")


class DescribeProjectRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeRecipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")


class DescribeRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeScheduleRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ExcelOptionsModel(BaseModel):
    sheet_names: Optional[Sequence[str]] = Field(default=None, alias="SheetNames")
    sheet_indexes: Optional[Sequence[int]] = Field(default=None, alias="SheetIndexes")
    header_row: Optional[bool] = Field(default=None, alias="HeaderRow")


class FilesLimitModel(BaseModel):
    max_files: int = Field(alias="MaxFiles")
    ordered_by: Optional[Literal["LAST_MODIFIED_DATE"]] = Field(
        default=None, alias="OrderedBy"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )


class JsonOptionsModel(BaseModel):
    multi_line: Optional[bool] = Field(default=None, alias="MultiLine")


class MetadataModel(BaseModel):
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDatasetsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJobRunsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJobsRequestModel(BaseModel):
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")


class ListProjectsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRecipeVersionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRecipesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")


class ListRulesetsRequestModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RulesetItemModel(BaseModel):
    name: str = Field(alias="Name")
    target_arn: str = Field(alias="TargetArn")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    description: Optional[str] = Field(default=None, alias="Description")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    rule_count: Optional[int] = Field(default=None, alias="RuleCount")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListSchedulesRequestModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ScheduleModel(BaseModel):
    name: str = Field(alias="Name")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    job_names: Optional[List[str]] = Field(default=None, alias="JobNames")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    cron_expression: Optional[str] = Field(default=None, alias="CronExpression")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PublishRecipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class RecipeActionModel(BaseModel):
    operation: str = Field(alias="Operation")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class ThresholdModel(BaseModel):
    value: float = Field(alias="Value")
    type: Optional[
        Literal[
            "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ]
    ] = Field(default=None, alias="Type")
    unit: Optional[Literal["COUNT", "PERCENTAGE"]] = Field(default=None, alias="Unit")


class ViewFrameModel(BaseModel):
    start_column_index: int = Field(alias="StartColumnIndex")
    column_range: Optional[int] = Field(default=None, alias="ColumnRange")
    hidden_columns: Optional[Sequence[str]] = Field(default=None, alias="HiddenColumns")
    start_row_index: Optional[int] = Field(default=None, alias="StartRowIndex")
    row_range: Optional[int] = Field(default=None, alias="RowRange")
    analytics: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="Analytics"
    )


class StartJobRunRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartProjectSessionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    assume_control: Optional[bool] = Field(default=None, alias="AssumeControl")


class StatisticOverrideModel(BaseModel):
    statistic: str = Field(alias="Statistic")
    parameters: Mapping[str, str] = Field(alias="Parameters")


class StopJobRunRequestModel(BaseModel):
    name: str = Field(alias="Name")
    run_id: str = Field(alias="RunId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateScheduleRequestModel(BaseModel):
    cron_expression: str = Field(alias="CronExpression")
    name: str = Field(alias="Name")
    job_names: Optional[Sequence[str]] = Field(default=None, alias="JobNames")


class EntityDetectorConfigurationModel(BaseModel):
    entity_types: Sequence[str] = Field(alias="EntityTypes")
    allowed_statistics: Optional[Sequence[AllowedStatisticsModel]] = Field(
        default=None, alias="AllowedStatistics"
    )


class BatchDeleteRecipeVersionResponseModel(BaseModel):
    name: str = Field(alias="Name")
    errors: List[RecipeVersionErrorDetailModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfileJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecipeJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecipeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduleResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDatasetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRecipeVersionResponseModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_version: str = Field(alias="RecipeVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteScheduleResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScheduleResponseModel(BaseModel):
    create_date: datetime = Field(alias="CreateDate")
    created_by: str = Field(alias="CreatedBy")
    job_names: List[str] = Field(alias="JobNames")
    last_modified_by: str = Field(alias="LastModifiedBy")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    resource_arn: str = Field(alias="ResourceArn")
    cron_expression: str = Field(alias="CronExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishRecipeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendProjectSessionActionResponseModel(BaseModel):
    result: str = Field(alias="Result")
    name: str = Field(alias="Name")
    action_id: int = Field(alias="ActionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartJobRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartProjectSessionResponseModel(BaseModel):
    name: str = Field(alias="Name")
    client_session_id: str = Field(alias="ClientSessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopJobRunResponseModel(BaseModel):
    run_id: str = Field(alias="RunId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatasetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProfileJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectResponseModel(BaseModel):
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecipeJobResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecipeResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScheduleResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataCatalogInputDefinitionModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    temp_directory: Optional[S3LocationModel] = Field(
        default=None, alias="TempDirectory"
    )


class DatabaseInputDefinitionModel(BaseModel):
    glue_connection_name: str = Field(alias="GlueConnectionName")
    database_table_name: Optional[str] = Field(default=None, alias="DatabaseTableName")
    temp_directory: Optional[S3LocationModel] = Field(
        default=None, alias="TempDirectory"
    )
    query_string: Optional[str] = Field(default=None, alias="QueryString")


class DatabaseTableOutputOptionsModel(BaseModel):
    table_name: str = Field(alias="TableName")
    temp_directory: Optional[S3LocationModel] = Field(
        default=None, alias="TempDirectory"
    )


class S3TableOutputOptionsModel(BaseModel):
    location: S3LocationModel = Field(alias="Location")


class CreateProjectRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    name: str = Field(alias="Name")
    recipe_name: str = Field(alias="RecipeName")
    role_arn: str = Field(alias="RoleArn")
    sample: Optional[SampleModel] = Field(default=None, alias="Sample")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DescribeProjectResponseModel(BaseModel):
    create_date: datetime = Field(alias="CreateDate")
    created_by: str = Field(alias="CreatedBy")
    dataset_name: str = Field(alias="DatasetName")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    last_modified_by: str = Field(alias="LastModifiedBy")
    name: str = Field(alias="Name")
    recipe_name: str = Field(alias="RecipeName")
    resource_arn: str = Field(alias="ResourceArn")
    sample: SampleModel = Field(alias="Sample")
    role_arn: str = Field(alias="RoleArn")
    tags: Dict[str, str] = Field(alias="Tags")
    session_status: Literal[
        "ASSIGNED",
        "FAILED",
        "INITIALIZING",
        "PROVISIONING",
        "READY",
        "RECYCLING",
        "ROTATING",
        "TERMINATED",
        "TERMINATING",
        "UPDATING",
    ] = Field(alias="SessionStatus")
    opened_by: str = Field(alias="OpenedBy")
    open_date: datetime = Field(alias="OpenDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProjectModel(BaseModel):
    name: str = Field(alias="Name")
    recipe_name: str = Field(alias="RecipeName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    sample: Optional[SampleModel] = Field(default=None, alias="Sample")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    opened_by: Optional[str] = Field(default=None, alias="OpenedBy")
    open_date: Optional[datetime] = Field(default=None, alias="OpenDate")


class UpdateProjectRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    name: str = Field(alias="Name")
    sample: Optional[SampleModel] = Field(default=None, alias="Sample")


class OutputFormatOptionsModel(BaseModel):
    csv: Optional[CsvOutputOptionsModel] = Field(default=None, alias="Csv")


class DatasetParameterModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["Datetime", "Number", "String"] = Field(alias="Type")
    datetime_options: Optional[DatetimeOptionsModel] = Field(
        default=None, alias="DatetimeOptions"
    )
    create_column: Optional[bool] = Field(default=None, alias="CreateColumn")
    filter: Optional[FilterExpressionModel] = Field(default=None, alias="Filter")


class FormatOptionsModel(BaseModel):
    json_: Optional[JsonOptionsModel] = Field(default=None, alias="Json")
    excel: Optional[ExcelOptionsModel] = Field(default=None, alias="Excel")
    csv: Optional[CsvOptionsModel] = Field(default=None, alias="Csv")


class ListDatasetsRequestListDatasetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobRunsRequestListJobRunsPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecipeVersionsRequestListRecipeVersionsPaginateModel(BaseModel):
    name: str = Field(alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecipesRequestListRecipesPaginateModel(BaseModel):
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesetsRequestListRulesetsPaginateModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchedulesRequestListSchedulesPaginateModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesetsResponseModel(BaseModel):
    rulesets: List[RulesetItemModel] = Field(alias="Rulesets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchedulesResponseModel(BaseModel):
    schedules: List[ScheduleModel] = Field(alias="Schedules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecipeStepModel(BaseModel):
    action: RecipeActionModel = Field(alias="Action")
    condition_expressions: Optional[Sequence[ConditionExpressionModel]] = Field(
        default=None, alias="ConditionExpressions"
    )


class RuleModel(BaseModel):
    name: str = Field(alias="Name")
    check_expression: str = Field(alias="CheckExpression")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    substitution_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="SubstitutionMap"
    )
    threshold: Optional[ThresholdModel] = Field(default=None, alias="Threshold")
    column_selectors: Optional[Sequence[ColumnSelectorModel]] = Field(
        default=None, alias="ColumnSelectors"
    )


class StatisticsConfigurationModel(BaseModel):
    included_statistics: Optional[Sequence[str]] = Field(
        default=None, alias="IncludedStatistics"
    )
    overrides: Optional[Sequence[StatisticOverrideModel]] = Field(
        default=None, alias="Overrides"
    )


class InputModel(BaseModel):
    s3_input_definition: Optional[S3LocationModel] = Field(
        default=None, alias="S3InputDefinition"
    )
    data_catalog_input_definition: Optional[DataCatalogInputDefinitionModel] = Field(
        default=None, alias="DataCatalogInputDefinition"
    )
    database_input_definition: Optional[DatabaseInputDefinitionModel] = Field(
        default=None, alias="DatabaseInputDefinition"
    )
    metadata: Optional[MetadataModel] = Field(default=None, alias="Metadata")


class DatabaseOutputModel(BaseModel):
    glue_connection_name: str = Field(alias="GlueConnectionName")
    database_options: DatabaseTableOutputOptionsModel = Field(alias="DatabaseOptions")
    database_output_mode: Optional[Literal["NEW_TABLE"]] = Field(
        default=None, alias="DatabaseOutputMode"
    )


class DataCatalogOutputModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    s3_options: Optional[S3TableOutputOptionsModel] = Field(
        default=None, alias="S3Options"
    )
    database_options: Optional[DatabaseTableOutputOptionsModel] = Field(
        default=None, alias="DatabaseOptions"
    )
    overwrite: Optional[bool] = Field(default=None, alias="Overwrite")


class ListProjectsResponseModel(BaseModel):
    projects: List[ProjectModel] = Field(alias="Projects")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OutputModel(BaseModel):
    location: S3LocationModel = Field(alias="Location")
    compression_format: Optional[
        Literal[
            "BROTLI", "BZIP2", "DEFLATE", "GZIP", "LZ4", "LZO", "SNAPPY", "ZLIB", "ZSTD"
        ]
    ] = Field(default=None, alias="CompressionFormat")
    format: Optional[
        Literal[
            "AVRO",
            "CSV",
            "GLUEPARQUET",
            "JSON",
            "ORC",
            "PARQUET",
            "TABLEAUHYPER",
            "XML",
        ]
    ] = Field(default=None, alias="Format")
    partition_columns: Optional[Sequence[str]] = Field(
        default=None, alias="PartitionColumns"
    )
    overwrite: Optional[bool] = Field(default=None, alias="Overwrite")
    format_options: Optional[OutputFormatOptionsModel] = Field(
        default=None, alias="FormatOptions"
    )
    max_output_files: Optional[int] = Field(default=None, alias="MaxOutputFiles")


class PathOptionsModel(BaseModel):
    last_modified_date_condition: Optional[FilterExpressionModel] = Field(
        default=None, alias="LastModifiedDateCondition"
    )
    files_limit: Optional[FilesLimitModel] = Field(default=None, alias="FilesLimit")
    parameters: Optional[Mapping[str, DatasetParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class CreateRecipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    steps: Sequence[RecipeStepModel] = Field(alias="Steps")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DescribeRecipeResponseModel(BaseModel):
    created_by: str = Field(alias="CreatedBy")
    create_date: datetime = Field(alias="CreateDate")
    last_modified_by: str = Field(alias="LastModifiedBy")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    project_name: str = Field(alias="ProjectName")
    published_by: str = Field(alias="PublishedBy")
    published_date: datetime = Field(alias="PublishedDate")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    steps: List[RecipeStepModel] = Field(alias="Steps")
    tags: Dict[str, str] = Field(alias="Tags")
    resource_arn: str = Field(alias="ResourceArn")
    recipe_version: str = Field(alias="RecipeVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecipeModel(BaseModel):
    name: str = Field(alias="Name")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    published_by: Optional[str] = Field(default=None, alias="PublishedBy")
    published_date: Optional[datetime] = Field(default=None, alias="PublishedDate")
    description: Optional[str] = Field(default=None, alias="Description")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    steps: Optional[List[RecipeStepModel]] = Field(default=None, alias="Steps")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    recipe_version: Optional[str] = Field(default=None, alias="RecipeVersion")


class SendProjectSessionActionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    preview: Optional[bool] = Field(default=None, alias="Preview")
    recipe_step: Optional[RecipeStepModel] = Field(default=None, alias="RecipeStep")
    step_index: Optional[int] = Field(default=None, alias="StepIndex")
    client_session_id: Optional[str] = Field(default=None, alias="ClientSessionId")
    view_frame: Optional[ViewFrameModel] = Field(default=None, alias="ViewFrame")


class UpdateRecipeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    steps: Optional[Sequence[RecipeStepModel]] = Field(default=None, alias="Steps")


class CreateRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    target_arn: str = Field(alias="TargetArn")
    rules: Sequence[RuleModel] = Field(alias="Rules")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DescribeRulesetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    target_arn: str = Field(alias="TargetArn")
    rules: List[RuleModel] = Field(alias="Rules")
    create_date: datetime = Field(alias="CreateDate")
    created_by: str = Field(alias="CreatedBy")
    last_modified_by: str = Field(alias="LastModifiedBy")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    resource_arn: str = Field(alias="ResourceArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRulesetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    rules: Sequence[RuleModel] = Field(alias="Rules")
    description: Optional[str] = Field(default=None, alias="Description")


class ColumnStatisticsConfigurationModel(BaseModel):
    statistics: StatisticsConfigurationModel = Field(alias="Statistics")
    selectors: Optional[Sequence[ColumnSelectorModel]] = Field(
        default=None, alias="Selectors"
    )


class CreateRecipeJobRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    encryption_mode: Optional[Literal["SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="Outputs")
    data_catalog_outputs: Optional[Sequence[DataCatalogOutputModel]] = Field(
        default=None, alias="DataCatalogOutputs"
    )
    database_outputs: Optional[Sequence[DatabaseOutputModel]] = Field(
        default=None, alias="DatabaseOutputs"
    )
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    recipe_reference: Optional[RecipeReferenceModel] = Field(
        default=None, alias="RecipeReference"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class JobRunModel(BaseModel):
    attempt: Optional[int] = Field(default=None, alias="Attempt")
    completed_on: Optional[datetime] = Field(default=None, alias="CompletedOn")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    execution_time: Optional[int] = Field(default=None, alias="ExecutionTime")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    run_id: Optional[str] = Field(default=None, alias="RunId")
    state: Optional[
        Literal[
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "SUCCEEDED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="State")
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")
    outputs: Optional[List[OutputModel]] = Field(default=None, alias="Outputs")
    data_catalog_outputs: Optional[List[DataCatalogOutputModel]] = Field(
        default=None, alias="DataCatalogOutputs"
    )
    database_outputs: Optional[List[DatabaseOutputModel]] = Field(
        default=None, alias="DatabaseOutputs"
    )
    recipe_reference: Optional[RecipeReferenceModel] = Field(
        default=None, alias="RecipeReference"
    )
    started_by: Optional[str] = Field(default=None, alias="StartedBy")
    started_on: Optional[datetime] = Field(default=None, alias="StartedOn")
    job_sample: Optional[JobSampleModel] = Field(default=None, alias="JobSample")
    validation_configurations: Optional[List[ValidationConfigurationModel]] = Field(
        default=None, alias="ValidationConfigurations"
    )


class JobModel(BaseModel):
    name: str = Field(alias="Name")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    encryption_mode: Optional[Literal["SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    type: Optional[Literal["PROFILE", "RECIPE"]] = Field(default=None, alias="Type")
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    outputs: Optional[List[OutputModel]] = Field(default=None, alias="Outputs")
    data_catalog_outputs: Optional[List[DataCatalogOutputModel]] = Field(
        default=None, alias="DataCatalogOutputs"
    )
    database_outputs: Optional[List[DatabaseOutputModel]] = Field(
        default=None, alias="DatabaseOutputs"
    )
    project_name: Optional[str] = Field(default=None, alias="ProjectName")
    recipe_reference: Optional[RecipeReferenceModel] = Field(
        default=None, alias="RecipeReference"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    job_sample: Optional[JobSampleModel] = Field(default=None, alias="JobSample")
    validation_configurations: Optional[List[ValidationConfigurationModel]] = Field(
        default=None, alias="ValidationConfigurations"
    )


class UpdateRecipeJobRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    encryption_mode: Optional[Literal["SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="Outputs")
    data_catalog_outputs: Optional[Sequence[DataCatalogOutputModel]] = Field(
        default=None, alias="DataCatalogOutputs"
    )
    database_outputs: Optional[Sequence[DatabaseOutputModel]] = Field(
        default=None, alias="DatabaseOutputs"
    )
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class CreateDatasetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    input: InputModel = Field(alias="Input")
    format: Optional[Literal["CSV", "EXCEL", "JSON", "ORC", "PARQUET"]] = Field(
        default=None, alias="Format"
    )
    format_options: Optional[FormatOptionsModel] = Field(
        default=None, alias="FormatOptions"
    )
    path_options: Optional[PathOptionsModel] = Field(default=None, alias="PathOptions")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DatasetModel(BaseModel):
    name: str = Field(alias="Name")
    input: InputModel = Field(alias="Input")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    format: Optional[Literal["CSV", "EXCEL", "JSON", "ORC", "PARQUET"]] = Field(
        default=None, alias="Format"
    )
    format_options: Optional[FormatOptionsModel] = Field(
        default=None, alias="FormatOptions"
    )
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    source: Optional[Literal["DATA-CATALOG", "DATABASE", "S3"]] = Field(
        default=None, alias="Source"
    )
    path_options: Optional[PathOptionsModel] = Field(default=None, alias="PathOptions")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class DescribeDatasetResponseModel(BaseModel):
    created_by: str = Field(alias="CreatedBy")
    create_date: datetime = Field(alias="CreateDate")
    name: str = Field(alias="Name")
    format: Literal["CSV", "EXCEL", "JSON", "ORC", "PARQUET"] = Field(alias="Format")
    format_options: FormatOptionsModel = Field(alias="FormatOptions")
    input: InputModel = Field(alias="Input")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    last_modified_by: str = Field(alias="LastModifiedBy")
    source: Literal["DATA-CATALOG", "DATABASE", "S3"] = Field(alias="Source")
    path_options: PathOptionsModel = Field(alias="PathOptions")
    tags: Dict[str, str] = Field(alias="Tags")
    resource_arn: str = Field(alias="ResourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatasetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    input: InputModel = Field(alias="Input")
    format: Optional[Literal["CSV", "EXCEL", "JSON", "ORC", "PARQUET"]] = Field(
        default=None, alias="Format"
    )
    format_options: Optional[FormatOptionsModel] = Field(
        default=None, alias="FormatOptions"
    )
    path_options: Optional[PathOptionsModel] = Field(default=None, alias="PathOptions")


class ListRecipeVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    recipes: List[RecipeModel] = Field(alias="Recipes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecipesResponseModel(BaseModel):
    recipes: List[RecipeModel] = Field(alias="Recipes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProfileConfigurationModel(BaseModel):
    dataset_statistics_configuration: Optional[StatisticsConfigurationModel] = Field(
        default=None, alias="DatasetStatisticsConfiguration"
    )
    profile_columns: Optional[Sequence[ColumnSelectorModel]] = Field(
        default=None, alias="ProfileColumns"
    )
    column_statistics_configurations: Optional[
        Sequence[ColumnStatisticsConfigurationModel]
    ] = Field(default=None, alias="ColumnStatisticsConfigurations")
    entity_detector_configuration: Optional[EntityDetectorConfigurationModel] = Field(
        default=None, alias="EntityDetectorConfiguration"
    )


class ListJobRunsResponseModel(BaseModel):
    job_runs: List[JobRunModel] = Field(alias="JobRuns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    datasets: List[DatasetModel] = Field(alias="Datasets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfileJobRequestModel(BaseModel):
    dataset_name: str = Field(alias="DatasetName")
    name: str = Field(alias="Name")
    output_location: S3LocationModel = Field(alias="OutputLocation")
    role_arn: str = Field(alias="RoleArn")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    encryption_mode: Optional[Literal["SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    configuration: Optional[ProfileConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    validation_configurations: Optional[Sequence[ValidationConfigurationModel]] = Field(
        default=None, alias="ValidationConfigurations"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    job_sample: Optional[JobSampleModel] = Field(default=None, alias="JobSample")


class DescribeJobResponseModel(BaseModel):
    create_date: datetime = Field(alias="CreateDate")
    created_by: str = Field(alias="CreatedBy")
    dataset_name: str = Field(alias="DatasetName")
    encryption_key_arn: str = Field(alias="EncryptionKeyArn")
    encryption_mode: Literal["SSE-KMS", "SSE-S3"] = Field(alias="EncryptionMode")
    name: str = Field(alias="Name")
    type: Literal["PROFILE", "RECIPE"] = Field(alias="Type")
    last_modified_by: str = Field(alias="LastModifiedBy")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    log_subscription: Literal["DISABLE", "ENABLE"] = Field(alias="LogSubscription")
    max_capacity: int = Field(alias="MaxCapacity")
    max_retries: int = Field(alias="MaxRetries")
    outputs: List[OutputModel] = Field(alias="Outputs")
    data_catalog_outputs: List[DataCatalogOutputModel] = Field(
        alias="DataCatalogOutputs"
    )
    database_outputs: List[DatabaseOutputModel] = Field(alias="DatabaseOutputs")
    project_name: str = Field(alias="ProjectName")
    profile_configuration: ProfileConfigurationModel = Field(
        alias="ProfileConfiguration"
    )
    validation_configurations: List[ValidationConfigurationModel] = Field(
        alias="ValidationConfigurations"
    )
    recipe_reference: RecipeReferenceModel = Field(alias="RecipeReference")
    resource_arn: str = Field(alias="ResourceArn")
    role_arn: str = Field(alias="RoleArn")
    tags: Dict[str, str] = Field(alias="Tags")
    timeout: int = Field(alias="Timeout")
    job_sample: JobSampleModel = Field(alias="JobSample")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeJobRunResponseModel(BaseModel):
    attempt: int = Field(alias="Attempt")
    completed_on: datetime = Field(alias="CompletedOn")
    dataset_name: str = Field(alias="DatasetName")
    error_message: str = Field(alias="ErrorMessage")
    execution_time: int = Field(alias="ExecutionTime")
    job_name: str = Field(alias="JobName")
    profile_configuration: ProfileConfigurationModel = Field(
        alias="ProfileConfiguration"
    )
    validation_configurations: List[ValidationConfigurationModel] = Field(
        alias="ValidationConfigurations"
    )
    run_id: str = Field(alias="RunId")
    state: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
    ] = Field(alias="State")
    log_subscription: Literal["DISABLE", "ENABLE"] = Field(alias="LogSubscription")
    log_group_name: str = Field(alias="LogGroupName")
    outputs: List[OutputModel] = Field(alias="Outputs")
    data_catalog_outputs: List[DataCatalogOutputModel] = Field(
        alias="DataCatalogOutputs"
    )
    database_outputs: List[DatabaseOutputModel] = Field(alias="DatabaseOutputs")
    recipe_reference: RecipeReferenceModel = Field(alias="RecipeReference")
    started_by: str = Field(alias="StartedBy")
    started_on: datetime = Field(alias="StartedOn")
    job_sample: JobSampleModel = Field(alias="JobSample")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProfileJobRequestModel(BaseModel):
    name: str = Field(alias="Name")
    output_location: S3LocationModel = Field(alias="OutputLocation")
    role_arn: str = Field(alias="RoleArn")
    configuration: Optional[ProfileConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    encryption_mode: Optional[Literal["SSE-KMS", "SSE-S3"]] = Field(
        default=None, alias="EncryptionMode"
    )
    log_subscription: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="LogSubscription"
    )
    max_capacity: Optional[int] = Field(default=None, alias="MaxCapacity")
    max_retries: Optional[int] = Field(default=None, alias="MaxRetries")
    validation_configurations: Optional[Sequence[ValidationConfigurationModel]] = Field(
        default=None, alias="ValidationConfigurations"
    )
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    job_sample: Optional[JobSampleModel] = Field(default=None, alias="JobSample")
