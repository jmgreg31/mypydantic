# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ArrayValueModel(BaseModel):
    boolean_values: Optional[Sequence[bool]] = Field(
        default=None, alias="booleanValues"
    )
    long_values: Optional[Sequence[int]] = Field(default=None, alias="longValues")
    double_values: Optional[Sequence[float]] = Field(default=None, alias="doubleValues")
    string_values: Optional[Sequence[str]] = Field(default=None, alias="stringValues")
    array_values: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="arrayValues"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BeginTransactionRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    secret_arn: str = Field(alias="secretArn")
    database: Optional[str] = Field(default=None, alias="database")
    schema_: Optional[str] = Field(default=None, alias="schema")


class ColumnMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[int] = Field(default=None, alias="type")
    type_name: Optional[str] = Field(default=None, alias="typeName")
    label: Optional[str] = Field(default=None, alias="label")
    schema_name: Optional[str] = Field(default=None, alias="schemaName")
    table_name: Optional[str] = Field(default=None, alias="tableName")
    is_auto_increment: Optional[bool] = Field(default=None, alias="isAutoIncrement")
    is_signed: Optional[bool] = Field(default=None, alias="isSigned")
    is_currency: Optional[bool] = Field(default=None, alias="isCurrency")
    is_case_sensitive: Optional[bool] = Field(default=None, alias="isCaseSensitive")
    nullable: Optional[int] = Field(default=None, alias="nullable")
    precision: Optional[int] = Field(default=None, alias="precision")
    scale: Optional[int] = Field(default=None, alias="scale")
    array_base_column_type: Optional[int] = Field(
        default=None, alias="arrayBaseColumnType"
    )


class CommitTransactionRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    secret_arn: str = Field(alias="secretArn")
    transaction_id: str = Field(alias="transactionId")


class ExecuteSqlRequestModel(BaseModel):
    db_cluster_or_instance_arn: str = Field(alias="dbClusterOrInstanceArn")
    aws_secret_store_arn: str = Field(alias="awsSecretStoreArn")
    sql_statements: str = Field(alias="sqlStatements")
    database: Optional[str] = Field(default=None, alias="database")
    schema_: Optional[str] = Field(default=None, alias="schema")


class ResultSetOptionsModel(BaseModel):
    decimal_return_type: Optional[Literal["DOUBLE_OR_LONG", "STRING"]] = Field(
        default=None, alias="decimalReturnType"
    )
    long_return_type: Optional[Literal["LONG", "STRING"]] = Field(
        default=None, alias="longReturnType"
    )


class FieldModel(BaseModel):
    is_null: Optional[bool] = Field(default=None, alias="isNull")
    boolean_value: Optional[bool] = Field(default=None, alias="booleanValue")
    long_value: Optional[int] = Field(default=None, alias="longValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    blob_value: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="blobValue"
    )
    array_value: Optional[ArrayValueModel] = Field(default=None, alias="arrayValue")


class RecordModel(BaseModel):
    values: Optional[List[ValueModel]] = Field(default=None, alias="values")


class RollbackTransactionRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    secret_arn: str = Field(alias="secretArn")
    transaction_id: str = Field(alias="transactionId")


class StructValueModel(BaseModel):
    attributes: Optional[List[Dict[str, Any]]] = Field(default=None, alias="attributes")


class ValueModel(BaseModel):
    is_null: Optional[bool] = Field(default=None, alias="isNull")
    bit_value: Optional[bool] = Field(default=None, alias="bitValue")
    big_int_value: Optional[int] = Field(default=None, alias="bigIntValue")
    int_value: Optional[int] = Field(default=None, alias="intValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    real_value: Optional[float] = Field(default=None, alias="realValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    blob_value: Optional[bytes] = Field(default=None, alias="blobValue")
    array_values: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="arrayValues"
    )
    struct_value: Optional[Dict[str, Any]] = Field(default=None, alias="structValue")


class BeginTransactionResponseModel(BaseModel):
    transaction_id: str = Field(alias="transactionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommitTransactionResponseModel(BaseModel):
    transaction_status: str = Field(alias="transactionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RollbackTransactionResponseModel(BaseModel):
    transaction_status: str = Field(alias="transactionStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResultSetMetadataModel(BaseModel):
    column_count: Optional[int] = Field(default=None, alias="columnCount")
    column_metadata: Optional[List[ColumnMetadataModel]] = Field(
        default=None, alias="columnMetadata"
    )


class ExecuteStatementResponseModel(BaseModel):
    records: List[List[FieldModel]] = Field(alias="records")
    column_metadata: List[ColumnMetadataModel] = Field(alias="columnMetadata")
    number_of_records_updated: int = Field(alias="numberOfRecordsUpdated")
    generated_fields: List[FieldModel] = Field(alias="generatedFields")
    formatted_records: str = Field(alias="formattedRecords")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SqlParameterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[FieldModel] = Field(default=None, alias="value")
    type_hint: Optional[
        Literal["DATE", "DECIMAL", "JSON", "TIME", "TIMESTAMP", "UUID"]
    ] = Field(default=None, alias="typeHint")


class UpdateResultModel(BaseModel):
    generated_fields: Optional[List[FieldModel]] = Field(
        default=None, alias="generatedFields"
    )


class ResultFrameModel(BaseModel):
    result_set_metadata: Optional[ResultSetMetadataModel] = Field(
        default=None, alias="resultSetMetadata"
    )
    records: Optional[List[RecordModel]] = Field(default=None, alias="records")


class BatchExecuteStatementRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    secret_arn: str = Field(alias="secretArn")
    sql: str = Field(alias="sql")
    database: Optional[str] = Field(default=None, alias="database")
    schema_: Optional[str] = Field(default=None, alias="schema")
    parameter_sets: Optional[Sequence[Sequence[SqlParameterModel]]] = Field(
        default=None, alias="parameterSets"
    )
    transaction_id: Optional[str] = Field(default=None, alias="transactionId")


class ExecuteStatementRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    secret_arn: str = Field(alias="secretArn")
    sql: str = Field(alias="sql")
    database: Optional[str] = Field(default=None, alias="database")
    schema_: Optional[str] = Field(default=None, alias="schema")
    parameters: Optional[Sequence[SqlParameterModel]] = Field(
        default=None, alias="parameters"
    )
    transaction_id: Optional[str] = Field(default=None, alias="transactionId")
    include_result_metadata: Optional[bool] = Field(
        default=None, alias="includeResultMetadata"
    )
    continue_after_timeout: Optional[bool] = Field(
        default=None, alias="continueAfterTimeout"
    )
    result_set_options: Optional[ResultSetOptionsModel] = Field(
        default=None, alias="resultSetOptions"
    )
    format_records_as: Optional[Literal["JSON", "NONE"]] = Field(
        default=None, alias="formatRecordsAs"
    )


class BatchExecuteStatementResponseModel(BaseModel):
    update_results: List[UpdateResultModel] = Field(alias="updateResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SqlStatementResultModel(BaseModel):
    result_frame: Optional[ResultFrameModel] = Field(default=None, alias="resultFrame")
    number_of_records_updated: Optional[int] = Field(
        default=None, alias="numberOfRecordsUpdated"
    )


class ExecuteSqlResponseModel(BaseModel):
    sql_statement_results: List[SqlStatementResultModel] = Field(
        alias="sqlStatementResults"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
