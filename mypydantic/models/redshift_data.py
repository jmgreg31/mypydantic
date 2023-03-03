# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchExecuteStatementInputRequestModel(BaseModel):
    database: str = Field(alias="Database")
    sqls: Sequence[str] = Field(alias="Sqls")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    with_event: Optional[bool] = Field(default=None, alias="WithEvent")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CancelStatementRequestModel(BaseModel):
    id: str = Field(alias="Id")


class ColumnMetadataModel(BaseModel):
    column_default: Optional[str] = Field(default=None, alias="columnDefault")
    is_case_sensitive: Optional[bool] = Field(default=None, alias="isCaseSensitive")
    is_currency: Optional[bool] = Field(default=None, alias="isCurrency")
    is_signed: Optional[bool] = Field(default=None, alias="isSigned")
    label: Optional[str] = Field(default=None, alias="label")
    length: Optional[int] = Field(default=None, alias="length")
    name: Optional[str] = Field(default=None, alias="name")
    nullable: Optional[int] = Field(default=None, alias="nullable")
    precision: Optional[int] = Field(default=None, alias="precision")
    scale: Optional[int] = Field(default=None, alias="scale")
    schema_name: Optional[str] = Field(default=None, alias="schemaName")
    table_name: Optional[str] = Field(default=None, alias="tableName")
    type_name: Optional[str] = Field(default=None, alias="typeName")


class DescribeStatementRequestModel(BaseModel):
    id: str = Field(alias="Id")


class SqlParameterModel(BaseModel):
    name: str = Field(alias="name")
    value: str = Field(alias="value")


class SubStatementDataModel(BaseModel):
    id: str = Field(alias="Id")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    duration: Optional[int] = Field(default=None, alias="Duration")
    error: Optional[str] = Field(default=None, alias="Error")
    has_result_set: Optional[bool] = Field(default=None, alias="HasResultSet")
    query_string: Optional[str] = Field(default=None, alias="QueryString")
    redshift_query_id: Optional[int] = Field(default=None, alias="RedshiftQueryId")
    result_rows: Optional[int] = Field(default=None, alias="ResultRows")
    result_size: Optional[int] = Field(default=None, alias="ResultSize")
    status: Optional[
        Literal["ABORTED", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"]
    ] = Field(default=None, alias="Status")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeTableRequestModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    schema_: Optional[str] = Field(default=None, alias="Schema")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    table: Optional[str] = Field(default=None, alias="Table")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class FieldModel(BaseModel):
    blob_value: Optional[bytes] = Field(default=None, alias="blobValue")
    boolean_value: Optional[bool] = Field(default=None, alias="booleanValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    is_null: Optional[bool] = Field(default=None, alias="isNull")
    long_value: Optional[int] = Field(default=None, alias="longValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")


class GetStatementResultRequestModel(BaseModel):
    id: str = Field(alias="Id")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDatabasesRequestModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class ListSchemasRequestModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    schema_pattern: Optional[str] = Field(default=None, alias="SchemaPattern")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class ListStatementsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    role_level: Optional[bool] = Field(default=None, alias="RoleLevel")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    status: Optional[
        Literal[
            "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
        ]
    ] = Field(default=None, alias="Status")


class ListTablesRequestModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    schema_pattern: Optional[str] = Field(default=None, alias="SchemaPattern")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    table_pattern: Optional[str] = Field(default=None, alias="TablePattern")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class TableMemberModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    schema_: Optional[str] = Field(default=None, alias="schema")
    type: Optional[str] = Field(default=None, alias="type")


class BatchExecuteStatementOutputModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    created_at: datetime = Field(alias="CreatedAt")
    database: str = Field(alias="Database")
    db_user: str = Field(alias="DbUser")
    id: str = Field(alias="Id")
    secret_arn: str = Field(alias="SecretArn")
    workgroup_name: str = Field(alias="WorkgroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelStatementResponseModel(BaseModel):
    status: bool = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteStatementOutputModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    created_at: datetime = Field(alias="CreatedAt")
    database: str = Field(alias="Database")
    db_user: str = Field(alias="DbUser")
    id: str = Field(alias="Id")
    secret_arn: str = Field(alias="SecretArn")
    workgroup_name: str = Field(alias="WorkgroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatabasesResponseModel(BaseModel):
    databases: List[str] = Field(alias="Databases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemasResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    schemas: List[str] = Field(alias="Schemas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableResponseModel(BaseModel):
    column_list: List[ColumnMetadataModel] = Field(alias="ColumnList")
    next_token: str = Field(alias="NextToken")
    table_name: str = Field(alias="TableName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteStatementInputRequestModel(BaseModel):
    database: str = Field(alias="Database")
    sql: str = Field(alias="Sql")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    parameters: Optional[Sequence[SqlParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    with_event: Optional[bool] = Field(default=None, alias="WithEvent")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")


class StatementDataModel(BaseModel):
    id: str = Field(alias="Id")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    is_batch_statement: Optional[bool] = Field(default=None, alias="IsBatchStatement")
    query_parameters: Optional[List[SqlParameterModel]] = Field(
        default=None, alias="QueryParameters"
    )
    query_string: Optional[str] = Field(default=None, alias="QueryString")
    query_strings: Optional[List[str]] = Field(default=None, alias="QueryStrings")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    status: Optional[
        Literal[
            "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
        ]
    ] = Field(default=None, alias="Status")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class DescribeStatementResponseModel(BaseModel):
    cluster_identifier: str = Field(alias="ClusterIdentifier")
    created_at: datetime = Field(alias="CreatedAt")
    database: str = Field(alias="Database")
    db_user: str = Field(alias="DbUser")
    duration: int = Field(alias="Duration")
    error: str = Field(alias="Error")
    has_result_set: bool = Field(alias="HasResultSet")
    id: str = Field(alias="Id")
    query_parameters: List[SqlParameterModel] = Field(alias="QueryParameters")
    query_string: str = Field(alias="QueryString")
    redshift_pid: int = Field(alias="RedshiftPid")
    redshift_query_id: int = Field(alias="RedshiftQueryId")
    result_rows: int = Field(alias="ResultRows")
    result_size: int = Field(alias="ResultSize")
    secret_arn: str = Field(alias="SecretArn")
    status: Literal[
        "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
    ] = Field(alias="Status")
    sub_statements: List[SubStatementDataModel] = Field(alias="SubStatements")
    updated_at: datetime = Field(alias="UpdatedAt")
    workgroup_name: str = Field(alias="WorkgroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableRequestDescribeTablePaginateModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    schema_: Optional[str] = Field(default=None, alias="Schema")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    table: Optional[str] = Field(default=None, alias="Table")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetStatementResultRequestGetStatementResultPaginateModel(BaseModel):
    id: str = Field(alias="Id")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatabasesRequestListDatabasesPaginateModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemasRequestListSchemasPaginateModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    schema_pattern: Optional[str] = Field(default=None, alias="SchemaPattern")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStatementsRequestListStatementsPaginateModel(BaseModel):
    role_level: Optional[bool] = Field(default=None, alias="RoleLevel")
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    status: Optional[
        Literal[
            "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
        ]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTablesRequestListTablesPaginateModel(BaseModel):
    database: str = Field(alias="Database")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    connected_database: Optional[str] = Field(default=None, alias="ConnectedDatabase")
    db_user: Optional[str] = Field(default=None, alias="DbUser")
    schema_pattern: Optional[str] = Field(default=None, alias="SchemaPattern")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    table_pattern: Optional[str] = Field(default=None, alias="TablePattern")
    workgroup_name: Optional[str] = Field(default=None, alias="WorkgroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetStatementResultResponseModel(BaseModel):
    column_metadata: List[ColumnMetadataModel] = Field(alias="ColumnMetadata")
    next_token: str = Field(alias="NextToken")
    records: List[List[FieldModel]] = Field(alias="Records")
    total_num_rows: int = Field(alias="TotalNumRows")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTablesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    tables: List[TableMemberModel] = Field(alias="Tables")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStatementsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    statements: List[StatementDataModel] = Field(alias="Statements")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
