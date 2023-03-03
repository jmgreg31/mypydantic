# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class FailedBatchItemModel(BaseModel):
    id: str = Field(alias="id")
    error_message: str = Field(alias="errorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDeleteTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    row_ids: Sequence[str] = Field(alias="rowIds")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class UpsertRowsResultModel(BaseModel):
    row_ids: List[str] = Field(alias="rowIds")
    upsert_action: Literal["APPENDED", "UPDATED"] = Field(alias="upsertAction")


class CellInputModel(BaseModel):
    fact: Optional[str] = Field(default=None, alias="fact")
    facts: Optional[Sequence[str]] = Field(default=None, alias="facts")


class CellModel(BaseModel):
    formula: Optional[str] = Field(default=None, alias="formula")
    format: Optional[
        Literal[
            "ACCOUNTING",
            "AUTO",
            "CONTACT",
            "CURRENCY",
            "DATE",
            "DATE_TIME",
            "NUMBER",
            "PERCENTAGE",
            "ROWLINK",
            "ROWSET",
            "TEXT",
            "TIME",
        ]
    ] = Field(default=None, alias="format")
    raw_value: Optional[str] = Field(default=None, alias="rawValue")
    formatted_value: Optional[str] = Field(default=None, alias="formattedValue")
    formatted_values: Optional[List[str]] = Field(default=None, alias="formattedValues")


class ColumnMetadataModel(BaseModel):
    name: str = Field(alias="name")
    format: Literal[
        "ACCOUNTING",
        "AUTO",
        "CONTACT",
        "CURRENCY",
        "DATE",
        "DATE_TIME",
        "NUMBER",
        "PERCENTAGE",
        "ROWLINK",
        "ROWSET",
        "TEXT",
        "TIME",
    ] = Field(alias="format")


class DataItemModel(BaseModel):
    override_format: Optional[
        Literal[
            "ACCOUNTING",
            "AUTO",
            "CONTACT",
            "CURRENCY",
            "DATE",
            "DATE_TIME",
            "NUMBER",
            "PERCENTAGE",
            "ROWLINK",
            "ROWSET",
            "TEXT",
            "TIME",
        ]
    ] = Field(default=None, alias="overrideFormat")
    raw_value: Optional[str] = Field(default=None, alias="rawValue")
    formatted_value: Optional[str] = Field(default=None, alias="formattedValue")


class DelimitedTextImportOptionsModel(BaseModel):
    delimiter: str = Field(alias="delimiter")
    has_header_row: Optional[bool] = Field(default=None, alias="hasHeaderRow")
    ignore_empty_rows: Optional[bool] = Field(default=None, alias="ignoreEmptyRows")
    data_character_encoding: Optional[
        Literal["ISO-8859-1", "US-ASCII", "UTF-16", "UTF-16BE", "UTF-16LE", "UTF-8"]
    ] = Field(default=None, alias="dataCharacterEncoding")


class DescribeTableDataImportJobRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    job_id: str = Field(alias="jobId")


class SourceDataColumnPropertiesModel(BaseModel):
    column_index: Optional[int] = Field(default=None, alias="columnIndex")


class FilterModel(BaseModel):
    formula: str = Field(alias="formula")
    context_row_id: Optional[str] = Field(default=None, alias="contextRowId")


class VariableValueModel(BaseModel):
    raw_value: str = Field(alias="rawValue")


class ImportDataSourceConfigModel(BaseModel):
    data_source_url: Optional[str] = Field(default=None, alias="dataSourceUrl")


class ImportJobSubmitterModel(BaseModel):
    email: Optional[str] = Field(default=None, alias="email")
    user_arn: Optional[str] = Field(default=None, alias="userArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListTableColumnsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TableColumnModel(BaseModel):
    table_column_id: Optional[str] = Field(default=None, alias="tableColumnId")
    table_column_name: Optional[str] = Field(default=None, alias="tableColumnName")
    format: Optional[
        Literal[
            "ACCOUNTING",
            "AUTO",
            "CONTACT",
            "CURRENCY",
            "DATE",
            "DATE_TIME",
            "NUMBER",
            "PERCENTAGE",
            "ROWLINK",
            "ROWSET",
            "TEXT",
            "TIME",
        ]
    ] = Field(default=None, alias="format")


class ListTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    row_ids: Optional[Sequence[str]] = Field(default=None, alias="rowIds")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTablesRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TableModel(BaseModel):
    table_id: Optional[str] = Field(default=None, alias="tableId")
    table_name: Optional[str] = Field(default=None, alias="tableName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchCreateTableRowsResultModel(BaseModel):
    workbook_cursor: int = Field(alias="workbookCursor")
    created_rows: Dict[str, str] = Field(alias="createdRows")
    failed_batch_items: List[FailedBatchItemModel] = Field(alias="failedBatchItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteTableRowsResultModel(BaseModel):
    workbook_cursor: int = Field(alias="workbookCursor")
    failed_batch_items: List[FailedBatchItemModel] = Field(alias="failedBatchItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateTableRowsResultModel(BaseModel):
    workbook_cursor: int = Field(alias="workbookCursor")
    failed_batch_items: List[FailedBatchItemModel] = Field(alias="failedBatchItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvokeScreenAutomationResultModel(BaseModel):
    workbook_cursor: int = Field(alias="workbookCursor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTableDataImportJobResultModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"] = Field(
        alias="jobStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpsertTableRowsResultModel(BaseModel):
    rows: Dict[str, UpsertRowsResultModel] = Field(alias="rows")
    workbook_cursor: int = Field(alias="workbookCursor")
    failed_batch_items: List[FailedBatchItemModel] = Field(alias="failedBatchItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRowDataModel(BaseModel):
    batch_item_id: str = Field(alias="batchItemId")
    cells_to_create: Mapping[str, CellInputModel] = Field(alias="cellsToCreate")


class UpdateRowDataModel(BaseModel):
    row_id: str = Field(alias="rowId")
    cells_to_update: Mapping[str, CellInputModel] = Field(alias="cellsToUpdate")


class TableRowModel(BaseModel):
    row_id: str = Field(alias="rowId")
    cells: List[CellModel] = Field(alias="cells")


class ResultRowModel(BaseModel):
    data_items: List[DataItemModel] = Field(alias="dataItems")
    row_id: Optional[str] = Field(default=None, alias="rowId")


class DestinationOptionsModel(BaseModel):
    column_map: Optional[Dict[str, SourceDataColumnPropertiesModel]] = Field(
        default=None, alias="columnMap"
    )


class QueryTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    filter_formula: FilterModel = Field(alias="filterFormula")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UpsertRowDataModel(BaseModel):
    batch_item_id: str = Field(alias="batchItemId")
    filter: FilterModel = Field(alias="filter")
    cells_to_update: Mapping[str, CellInputModel] = Field(alias="cellsToUpdate")


class GetScreenDataRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    app_id: str = Field(alias="appId")
    screen_id: str = Field(alias="screenId")
    variables: Optional[Mapping[str, VariableValueModel]] = Field(
        default=None, alias="variables"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class InvokeScreenAutomationRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    app_id: str = Field(alias="appId")
    screen_id: str = Field(alias="screenId")
    screen_automation_id: str = Field(alias="screenAutomationId")
    variables: Optional[Mapping[str, VariableValueModel]] = Field(
        default=None, alias="variables"
    )
    row_id: Optional[str] = Field(default=None, alias="rowId")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class ImportDataSourceModel(BaseModel):
    data_source_config: ImportDataSourceConfigModel = Field(alias="dataSourceConfig")


class ListTableColumnsRequestListTableColumnsPaginateModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTableRowsRequestListTableRowsPaginateModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    row_ids: Optional[Sequence[str]] = Field(default=None, alias="rowIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTablesRequestListTablesPaginateModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class QueryTableRowsRequestQueryTableRowsPaginateModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    filter_formula: FilterModel = Field(alias="filterFormula")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTableColumnsResultModel(BaseModel):
    table_columns: List[TableColumnModel] = Field(alias="tableColumns")
    next_token: str = Field(alias="nextToken")
    workbook_cursor: int = Field(alias="workbookCursor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTablesResultModel(BaseModel):
    tables: List[TableModel] = Field(alias="tables")
    next_token: str = Field(alias="nextToken")
    workbook_cursor: int = Field(alias="workbookCursor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    rows_to_create: Sequence[CreateRowDataModel] = Field(alias="rowsToCreate")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class BatchUpdateTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    rows_to_update: Sequence[UpdateRowDataModel] = Field(alias="rowsToUpdate")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class ListTableRowsResultModel(BaseModel):
    column_ids: List[str] = Field(alias="columnIds")
    rows: List[TableRowModel] = Field(alias="rows")
    row_ids_not_found: List[str] = Field(alias="rowIdsNotFound")
    next_token: str = Field(alias="nextToken")
    workbook_cursor: int = Field(alias="workbookCursor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryTableRowsResultModel(BaseModel):
    column_ids: List[str] = Field(alias="columnIds")
    rows: List[TableRowModel] = Field(alias="rows")
    next_token: str = Field(alias="nextToken")
    workbook_cursor: int = Field(alias="workbookCursor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResultSetModel(BaseModel):
    headers: List[ColumnMetadataModel] = Field(alias="headers")
    rows: List[ResultRowModel] = Field(alias="rows")


class ImportOptionsModel(BaseModel):
    destination_options: Optional[DestinationOptionsModel] = Field(
        default=None, alias="destinationOptions"
    )
    delimited_text_options: Optional[DelimitedTextImportOptionsModel] = Field(
        default=None, alias="delimitedTextOptions"
    )


class BatchUpsertTableRowsRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    table_id: str = Field(alias="tableId")
    rows_to_upsert: Sequence[UpsertRowDataModel] = Field(alias="rowsToUpsert")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class GetScreenDataResultModel(BaseModel):
    results: Dict[str, ResultSetModel] = Field(alias="results")
    workbook_cursor: int = Field(alias="workbookCursor")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTableDataImportJobRequestModel(BaseModel):
    workbook_id: str = Field(alias="workbookId")
    data_source: ImportDataSourceModel = Field(alias="dataSource")
    data_format: Literal["DELIMITED_TEXT"] = Field(alias="dataFormat")
    destination_table_id: str = Field(alias="destinationTableId")
    import_options: ImportOptionsModel = Field(alias="importOptions")
    client_request_token: str = Field(alias="clientRequestToken")


class TableDataImportJobMetadataModel(BaseModel):
    submitter: ImportJobSubmitterModel = Field(alias="submitter")
    submit_time: datetime = Field(alias="submitTime")
    import_options: ImportOptionsModel = Field(alias="importOptions")
    data_source: ImportDataSourceModel = Field(alias="dataSource")


class DescribeTableDataImportJobResultModel(BaseModel):
    job_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"] = Field(
        alias="jobStatus"
    )
    message: str = Field(alias="message")
    job_metadata: TableDataImportJobMetadataModel = Field(alias="jobMetadata")
    error_code: Literal[
        "ACCESS_DENIED",
        "FILE_EMPTY_ERROR",
        "FILE_NOT_FOUND_ERROR",
        "FILE_PARSING_ERROR",
        "FILE_SIZE_LIMIT_ERROR",
        "INVALID_FILE_TYPE_ERROR",
        "INVALID_IMPORT_OPTIONS_ERROR",
        "INVALID_TABLE_COLUMN_ID_ERROR",
        "INVALID_TABLE_ID_ERROR",
        "INVALID_URL_ERROR",
        "RESOURCE_NOT_FOUND_ERROR",
        "SYSTEM_LIMIT_ERROR",
        "TABLE_NOT_FOUND_ERROR",
        "UNKNOWN_ERROR",
    ] = Field(alias="errorCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
