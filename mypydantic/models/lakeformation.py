# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class LFTagPairModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_values: Sequence[str] = Field(alias="TagValues")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddObjectInputModel(BaseModel):
    uri: str = Field(alias="Uri")
    etag: str = Field(alias="ETag")
    size: int = Field(alias="Size")
    partition_values: Optional[Sequence[str]] = Field(
        default=None, alias="PartitionValues"
    )


class AssumeDecoratedRoleWithSAMLRequestModel(BaseModel):
    s_aml_assertion: str = Field(alias="SAMLAssertion")
    role_arn: str = Field(alias="RoleArn")
    principal_arn: str = Field(alias="PrincipalArn")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")


class AuditContextModel(BaseModel):
    additional_audit_context: Optional[str] = Field(
        default=None, alias="AdditionalAuditContext"
    )


class ErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class DataLakePrincipalModel(BaseModel):
    data_lake_principal_identifier: Optional[str] = Field(
        default=None, alias="DataLakePrincipalIdentifier"
    )


class CancelTransactionRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")


class ColumnWildcardModel(BaseModel):
    excluded_column_names: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedColumnNames"
    )


class CommitTransactionRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")


class CreateLFTagRequestModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_values: Sequence[str] = Field(alias="TagValues")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DataCellsFilterResourceModel(BaseModel):
    table_catalog_id: Optional[str] = Field(default=None, alias="TableCatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    name: Optional[str] = Field(default=None, alias="Name")


class RowFilterModel(BaseModel):
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    all_rows_wildcard: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AllRowsWildcard"
    )


class DataLocationResourceModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DatabaseResourceModel(BaseModel):
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteDataCellsFilterRequestModel(BaseModel):
    table_catalog_id: Optional[str] = Field(default=None, alias="TableCatalogId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    name: Optional[str] = Field(default=None, alias="Name")


class DeleteLFTagRequestModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DeleteObjectInputModel(BaseModel):
    uri: str = Field(alias="Uri")
    etag: Optional[str] = Field(default=None, alias="ETag")
    partition_values: Optional[Sequence[str]] = Field(
        default=None, alias="PartitionValues"
    )


class VirtualObjectModel(BaseModel):
    uri: str = Field(alias="Uri")
    etag: Optional[str] = Field(default=None, alias="ETag")


class DeregisterResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DescribeResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ResourceInfoModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")


class DescribeTransactionRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")


class TransactionDescriptionModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    transaction_status: Optional[
        Literal["ABORTED", "ACTIVE", "COMMITTED", "COMMIT_IN_PROGRESS"]
    ] = Field(default=None, alias="TransactionStatus")
    transaction_start_time: Optional[datetime] = Field(
        default=None, alias="TransactionStartTime"
    )
    transaction_end_time: Optional[datetime] = Field(
        default=None, alias="TransactionEndTime"
    )


class DetailsMapModel(BaseModel):
    resource_share: Optional[List[str]] = Field(default=None, alias="ResourceShare")


class ExecutionStatisticsModel(BaseModel):
    average_execution_time_millis: Optional[int] = Field(
        default=None, alias="AverageExecutionTimeMillis"
    )
    data_scanned_bytes: Optional[int] = Field(default=None, alias="DataScannedBytes")
    work_units_executed_count: Optional[int] = Field(
        default=None, alias="WorkUnitsExecutedCount"
    )


class ExtendTransactionRequestModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class FilterConditionModel(BaseModel):
    field: Optional[Literal["LAST_MODIFIED", "RESOURCE_ARN", "ROLE_ARN"]] = Field(
        default=None, alias="Field"
    )
    comparison_operator: Optional[
        Literal[
            "BEGINS_WITH",
            "BETWEEN",
            "CONTAINS",
            "EQ",
            "GE",
            "GT",
            "IN",
            "LE",
            "LT",
            "NE",
            "NOT_CONTAINS",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    string_value_list: Optional[Sequence[str]] = Field(
        default=None, alias="StringValueList"
    )


class GetDataLakeSettingsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetEffectivePermissionsForPathRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetLFTagRequestModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetQueryStateRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")


class GetQueryStatisticsRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")


class PlanningStatisticsModel(BaseModel):
    estimated_data_to_scan_bytes: Optional[int] = Field(
        default=None, alias="EstimatedDataToScanBytes"
    )
    planning_time_millis: Optional[int] = Field(
        default=None, alias="PlanningTimeMillis"
    )
    queue_time_millis: Optional[int] = Field(default=None, alias="QueueTimeMillis")
    work_units_generated_count: Optional[int] = Field(
        default=None, alias="WorkUnitsGeneratedCount"
    )


class GetTableObjectsRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )
    partition_predicate: Optional[str] = Field(default=None, alias="PartitionPredicate")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PartitionValueListModel(BaseModel):
    values: Sequence[str] = Field(alias="Values")


class GetWorkUnitResultsRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    work_unit_id: int = Field(alias="WorkUnitId")
    work_unit_token: str = Field(alias="WorkUnitToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetWorkUnitsRequestModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")


class WorkUnitRangeModel(BaseModel):
    work_unit_id_max: int = Field(alias="WorkUnitIdMax")
    work_unit_id_min: int = Field(alias="WorkUnitIdMin")
    work_unit_token: str = Field(alias="WorkUnitToken")


class LFTagKeyResourceModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_values: Sequence[str] = Field(alias="TagValues")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class LFTagModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_values: Sequence[str] = Field(alias="TagValues")


class TableResourceModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    name: Optional[str] = Field(default=None, alias="Name")
    table_wildcard: Optional[Mapping[str, Any]] = Field(
        default=None, alias="TableWildcard"
    )


class ListLFTagsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    resource_share_type: Optional[Literal["ALL", "FOREIGN"]] = Field(
        default=None, alias="ResourceShareType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTableStorageOptimizersRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    storage_optimizer_type: Optional[
        Literal["ALL", "COMPACTION", "GARBAGE_COLLECTION"]
    ] = Field(default=None, alias="StorageOptimizerType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StorageOptimizerModel(BaseModel):
    storage_optimizer_type: Optional[
        Literal["ALL", "COMPACTION", "GARBAGE_COLLECTION"]
    ] = Field(default=None, alias="StorageOptimizerType")
    config: Optional[Dict[str, str]] = Field(default=None, alias="Config")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    warnings: Optional[str] = Field(default=None, alias="Warnings")
    last_run_details: Optional[str] = Field(default=None, alias="LastRunDetails")


class ListTransactionsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    status_filter: Optional[
        Literal["ABORTED", "ACTIVE", "ALL", "COMMITTED", "COMPLETED"]
    ] = Field(default=None, alias="StatusFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TableObjectModel(BaseModel):
    uri: Optional[str] = Field(default=None, alias="Uri")
    etag: Optional[str] = Field(default=None, alias="ETag")
    size: Optional[int] = Field(default=None, alias="Size")


class QueryPlanningContextModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    query_as_of_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryAsOfTime"
    )
    query_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="QueryParameters"
    )
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class RegisterResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    use_service_linked_role: Optional[bool] = Field(
        default=None, alias="UseServiceLinkedRole"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class StartTransactionRequestModel(BaseModel):
    transaction_type: Optional[Literal["READ_AND_WRITE", "READ_ONLY"]] = Field(
        default=None, alias="TransactionType"
    )


class UpdateLFTagRequestModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    tag_values_to_delete: Optional[Sequence[str]] = Field(
        default=None, alias="TagValuesToDelete"
    )
    tag_values_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="TagValuesToAdd"
    )


class UpdateResourceRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    resource_arn: str = Field(alias="ResourceArn")


class UpdateTableStorageOptimizerRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    storage_optimizer_config: Mapping[
        Literal["ALL", "COMPACTION", "GARBAGE_COLLECTION"], Mapping[str, str]
    ] = Field(alias="StorageOptimizerConfig")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class ColumnLFTagModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    l_ftags: Optional[List[LFTagPairModel]] = Field(default=None, alias="LFTags")


class AssumeDecoratedRoleWithSAMLResponseModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    secret_access_key: str = Field(alias="SecretAccessKey")
    session_token: str = Field(alias="SessionToken")
    expiration: datetime = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommitTransactionResponseModel(BaseModel):
    transaction_status: Literal[
        "ABORTED", "ACTIVE", "COMMITTED", "COMMIT_IN_PROGRESS"
    ] = Field(alias="TransactionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLFTagResponseModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    tag_key: str = Field(alias="TagKey")
    tag_values: List[str] = Field(alias="TagValues")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryStateResponseModel(BaseModel):
    error: str = Field(alias="Error")
    state: Literal[
        "ERROR", "EXPIRED", "FINISHED", "PENDING", "WORKUNITS_AVAILABLE"
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemporaryGluePartitionCredentialsResponseModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    secret_access_key: str = Field(alias="SecretAccessKey")
    session_token: str = Field(alias="SessionToken")
    expiration: datetime = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemporaryGlueTableCredentialsResponseModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    secret_access_key: str = Field(alias="SecretAccessKey")
    session_token: str = Field(alias="SessionToken")
    expiration: datetime = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkUnitResultsResponseModel(BaseModel):
    result_stream: Type[StreamingBody] = Field(alias="ResultStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLFTagsResponseModel(BaseModel):
    l_ftags: List[LFTagPairModel] = Field(alias="LFTags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartQueryPlanningResponseModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTransactionResponseModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableStorageOptimizerResponseModel(BaseModel):
    result: str = Field(alias="Result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemporaryGlueTableCredentialsRequestModel(BaseModel):
    table_arn: str = Field(alias="TableArn")
    supported_permission_types: Sequence[
        Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
    ] = Field(alias="SupportedPermissionTypes")
    permissions: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    audit_context: Optional[AuditContextModel] = Field(
        default=None, alias="AuditContext"
    )


class LFTagErrorModel(BaseModel):
    l_ftag: Optional[LFTagPairModel] = Field(default=None, alias="LFTag")
    error: Optional[ErrorDetailModel] = Field(default=None, alias="Error")


class PrincipalPermissionsModel(BaseModel):
    principal: Optional[DataLakePrincipalModel] = Field(default=None, alias="Principal")
    permissions: Optional[
        List[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")


class TableWithColumnsResourceModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    name: str = Field(alias="Name")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    column_names: Optional[Sequence[str]] = Field(default=None, alias="ColumnNames")
    column_wildcard: Optional[ColumnWildcardModel] = Field(
        default=None, alias="ColumnWildcard"
    )


class DataCellsFilterModel(BaseModel):
    table_catalog_id: str = Field(alias="TableCatalogId")
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    name: str = Field(alias="Name")
    row_filter: Optional[RowFilterModel] = Field(default=None, alias="RowFilter")
    column_names: Optional[Sequence[str]] = Field(default=None, alias="ColumnNames")
    column_wildcard: Optional[ColumnWildcardModel] = Field(
        default=None, alias="ColumnWildcard"
    )


class TaggedDatabaseModel(BaseModel):
    database: Optional[DatabaseResourceModel] = Field(default=None, alias="Database")
    l_ftags: Optional[List[LFTagPairModel]] = Field(default=None, alias="LFTags")


class WriteOperationModel(BaseModel):
    add_object: Optional[AddObjectInputModel] = Field(default=None, alias="AddObject")
    delete_object: Optional[DeleteObjectInputModel] = Field(
        default=None, alias="DeleteObject"
    )


class DeleteObjectsOnCancelRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    transaction_id: str = Field(alias="TransactionId")
    objects: Sequence[VirtualObjectModel] = Field(alias="Objects")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class DescribeResourceResponseModel(BaseModel):
    resource_info: ResourceInfoModel = Field(alias="ResourceInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesResponseModel(BaseModel):
    resource_info_list: List[ResourceInfoModel] = Field(alias="ResourceInfoList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTransactionResponseModel(BaseModel):
    transaction_description: TransactionDescriptionModel = Field(
        alias="TransactionDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTransactionsResponseModel(BaseModel):
    transactions: List[TransactionDescriptionModel] = Field(alias="Transactions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesRequestModel(BaseModel):
    filter_condition_list: Optional[Sequence[FilterConditionModel]] = Field(
        default=None, alias="FilterConditionList"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetQueryStatisticsResponseModel(BaseModel):
    execution_statistics: ExecutionStatisticsModel = Field(alias="ExecutionStatistics")
    planning_statistics: PlanningStatisticsModel = Field(alias="PlanningStatistics")
    query_submission_time: datetime = Field(alias="QuerySubmissionTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTemporaryGluePartitionCredentialsRequestModel(BaseModel):
    table_arn: str = Field(alias="TableArn")
    partition: PartitionValueListModel = Field(alias="Partition")
    supported_permission_types: Sequence[
        Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
    ] = Field(alias="SupportedPermissionTypes")
    permissions: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    audit_context: Optional[AuditContextModel] = Field(
        default=None, alias="AuditContext"
    )


class GetWorkUnitsRequestGetWorkUnitsPaginateModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLFTagsRequestListLFTagsPaginateModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    resource_share_type: Optional[Literal["ALL", "FOREIGN"]] = Field(
        default=None, alias="ResourceShareType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetWorkUnitsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    query_id: str = Field(alias="QueryId")
    work_unit_ranges: List[WorkUnitRangeModel] = Field(alias="WorkUnitRanges")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LFTagPolicyResourceModel(BaseModel):
    resource_type: Literal["DATABASE", "TABLE"] = Field(alias="ResourceType")
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class SearchDatabasesByLFTagsRequestModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchTablesByLFTagsRequestModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataCellsFilterRequestListDataCellsFilterPaginateModel(BaseModel):
    table: Optional[TableResourceModel] = Field(default=None, alias="Table")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataCellsFilterRequestModel(BaseModel):
    table: Optional[TableResourceModel] = Field(default=None, alias="Table")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTableStorageOptimizersResponseModel(BaseModel):
    storage_optimizer_list: List[StorageOptimizerModel] = Field(
        alias="StorageOptimizerList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PartitionObjectsModel(BaseModel):
    partition_values: Optional[List[str]] = Field(default=None, alias="PartitionValues")
    objects: Optional[List[TableObjectModel]] = Field(default=None, alias="Objects")


class StartQueryPlanningRequestModel(BaseModel):
    query_planning_context: QueryPlanningContextModel = Field(
        alias="QueryPlanningContext"
    )
    query_string: str = Field(alias="QueryString")


class GetResourceLFTagsResponseModel(BaseModel):
    l_ftag_on_database: List[LFTagPairModel] = Field(alias="LFTagOnDatabase")
    l_ftags_on_table: List[LFTagPairModel] = Field(alias="LFTagsOnTable")
    l_ftags_on_columns: List[ColumnLFTagModel] = Field(alias="LFTagsOnColumns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaggedTableModel(BaseModel):
    table: Optional[TableResourceModel] = Field(default=None, alias="Table")
    l_ftag_on_database: Optional[List[LFTagPairModel]] = Field(
        default=None, alias="LFTagOnDatabase"
    )
    l_ftags_on_table: Optional[List[LFTagPairModel]] = Field(
        default=None, alias="LFTagsOnTable"
    )
    l_ftags_on_columns: Optional[List[ColumnLFTagModel]] = Field(
        default=None, alias="LFTagsOnColumns"
    )


class AddLFTagsToResourceResponseModel(BaseModel):
    failures: List[LFTagErrorModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveLFTagsFromResourceResponseModel(BaseModel):
    failures: List[LFTagErrorModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataLakeSettingsModel(BaseModel):
    data_lake_admins: Optional[List[DataLakePrincipalModel]] = Field(
        default=None, alias="DataLakeAdmins"
    )
    create_database_default_permissions: Optional[
        List[PrincipalPermissionsModel]
    ] = Field(default=None, alias="CreateDatabaseDefaultPermissions")
    create_table_default_permissions: Optional[List[PrincipalPermissionsModel]] = Field(
        default=None, alias="CreateTableDefaultPermissions"
    )
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")
    trusted_resource_owners: Optional[List[str]] = Field(
        default=None, alias="TrustedResourceOwners"
    )
    allow_external_data_filtering: Optional[bool] = Field(
        default=None, alias="AllowExternalDataFiltering"
    )
    external_data_filtering_allow_list: Optional[List[DataLakePrincipalModel]] = Field(
        default=None, alias="ExternalDataFilteringAllowList"
    )
    authorized_session_tag_value_list: Optional[List[str]] = Field(
        default=None, alias="AuthorizedSessionTagValueList"
    )


class CreateDataCellsFilterRequestModel(BaseModel):
    table_data: DataCellsFilterModel = Field(alias="TableData")


class ListDataCellsFilterResponseModel(BaseModel):
    data_cells_filters: List[DataCellsFilterModel] = Field(alias="DataCellsFilters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchDatabasesByLFTagsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    database_list: List[TaggedDatabaseModel] = Field(alias="DatabaseList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableObjectsRequestModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    write_operations: Sequence[WriteOperationModel] = Field(alias="WriteOperations")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class ResourceModel(BaseModel):
    catalog: Optional[Mapping[str, Any]] = Field(default=None, alias="Catalog")
    database: Optional[DatabaseResourceModel] = Field(default=None, alias="Database")
    table: Optional[TableResourceModel] = Field(default=None, alias="Table")
    table_with_columns: Optional[TableWithColumnsResourceModel] = Field(
        default=None, alias="TableWithColumns"
    )
    data_location: Optional[DataLocationResourceModel] = Field(
        default=None, alias="DataLocation"
    )
    data_cells_filter: Optional[DataCellsFilterResourceModel] = Field(
        default=None, alias="DataCellsFilter"
    )
    l_ftag: Optional[LFTagKeyResourceModel] = Field(default=None, alias="LFTag")
    l_ftag_policy: Optional[LFTagPolicyResourceModel] = Field(
        default=None, alias="LFTagPolicy"
    )


class GetTableObjectsResponseModel(BaseModel):
    objects: List[PartitionObjectsModel] = Field(alias="Objects")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchTablesByLFTagsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    table_list: List[TaggedTableModel] = Field(alias="TableList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataLakeSettingsResponseModel(BaseModel):
    data_lake_settings: DataLakeSettingsModel = Field(alias="DataLakeSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDataLakeSettingsRequestModel(BaseModel):
    data_lake_settings: DataLakeSettingsModel = Field(alias="DataLakeSettings")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class AddLFTagsToResourceRequestModel(BaseModel):
    resource: ResourceModel = Field(alias="Resource")
    l_ftags: Sequence[LFTagPairModel] = Field(alias="LFTags")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchPermissionsRequestEntryModel(BaseModel):
    id: str = Field(alias="Id")
    principal: Optional[DataLakePrincipalModel] = Field(default=None, alias="Principal")
    resource: Optional[ResourceModel] = Field(default=None, alias="Resource")
    permissions: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")
    permissions_with_grant_option: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="PermissionsWithGrantOption")


class GetResourceLFTagsRequestModel(BaseModel):
    resource: ResourceModel = Field(alias="Resource")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    show_assigned_l_ftags: Optional[bool] = Field(
        default=None, alias="ShowAssignedLFTags"
    )


class GrantPermissionsRequestModel(BaseModel):
    principal: DataLakePrincipalModel = Field(alias="Principal")
    resource: ResourceModel = Field(alias="Resource")
    permissions: Sequence[
        Literal[
            "ALL",
            "ALTER",
            "ASSOCIATE",
            "CREATE_DATABASE",
            "CREATE_TABLE",
            "CREATE_TAG",
            "DATA_LOCATION_ACCESS",
            "DELETE",
            "DESCRIBE",
            "DROP",
            "INSERT",
            "SELECT",
        ]
    ] = Field(alias="Permissions")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    permissions_with_grant_option: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="PermissionsWithGrantOption")


class ListPermissionsRequestModel(BaseModel):
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    principal: Optional[DataLakePrincipalModel] = Field(default=None, alias="Principal")
    resource_type: Optional[
        Literal[
            "CATALOG",
            "DATABASE",
            "DATA_LOCATION",
            "LF_TAG",
            "LF_TAG_POLICY",
            "LF_TAG_POLICY_DATABASE",
            "LF_TAG_POLICY_TABLE",
            "TABLE",
        ]
    ] = Field(default=None, alias="ResourceType")
    resource: Optional[ResourceModel] = Field(default=None, alias="Resource")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    include_related: Optional[str] = Field(default=None, alias="IncludeRelated")


class PrincipalResourcePermissionsModel(BaseModel):
    principal: Optional[DataLakePrincipalModel] = Field(default=None, alias="Principal")
    resource: Optional[ResourceModel] = Field(default=None, alias="Resource")
    permissions: Optional[
        List[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="Permissions")
    permissions_with_grant_option: Optional[
        List[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="PermissionsWithGrantOption")
    additional_details: Optional[DetailsMapModel] = Field(
        default=None, alias="AdditionalDetails"
    )


class RemoveLFTagsFromResourceRequestModel(BaseModel):
    resource: ResourceModel = Field(alias="Resource")
    l_ftags: Sequence[LFTagPairModel] = Field(alias="LFTags")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class RevokePermissionsRequestModel(BaseModel):
    principal: DataLakePrincipalModel = Field(alias="Principal")
    resource: ResourceModel = Field(alias="Resource")
    permissions: Sequence[
        Literal[
            "ALL",
            "ALTER",
            "ASSOCIATE",
            "CREATE_DATABASE",
            "CREATE_TABLE",
            "CREATE_TAG",
            "DATA_LOCATION_ACCESS",
            "DELETE",
            "DESCRIBE",
            "DROP",
            "INSERT",
            "SELECT",
        ]
    ] = Field(alias="Permissions")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")
    permissions_with_grant_option: Optional[
        Sequence[
            Literal[
                "ALL",
                "ALTER",
                "ASSOCIATE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "CREATE_TAG",
                "DATA_LOCATION_ACCESS",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT",
                "SELECT",
            ]
        ]
    ] = Field(default=None, alias="PermissionsWithGrantOption")


class BatchGrantPermissionsRequestModel(BaseModel):
    entries: Sequence[BatchPermissionsRequestEntryModel] = Field(alias="Entries")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class BatchPermissionsFailureEntryModel(BaseModel):
    request_entry: Optional[BatchPermissionsRequestEntryModel] = Field(
        default=None, alias="RequestEntry"
    )
    error: Optional[ErrorDetailModel] = Field(default=None, alias="Error")


class BatchRevokePermissionsRequestModel(BaseModel):
    entries: Sequence[BatchPermissionsRequestEntryModel] = Field(alias="Entries")
    catalog_id: Optional[str] = Field(default=None, alias="CatalogId")


class GetEffectivePermissionsForPathResponseModel(BaseModel):
    permissions: List[PrincipalResourcePermissionsModel] = Field(alias="Permissions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionsResponseModel(BaseModel):
    principal_resource_permissions: List[PrincipalResourcePermissionsModel] = Field(
        alias="PrincipalResourcePermissions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGrantPermissionsResponseModel(BaseModel):
    failures: List[BatchPermissionsFailureEntryModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchRevokePermissionsResponseModel(BaseModel):
    failures: List[BatchPermissionsFailureEntryModel] = Field(alias="Failures")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
