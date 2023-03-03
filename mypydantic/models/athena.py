# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AclConfigurationModel(BaseModel):
    s3_acl_option: Literal["BUCKET_OWNER_FULL_CONTROL"] = Field(alias="S3AclOption")


class ApplicationDPUSizesModel(BaseModel):
    application_runtime_id: Optional[str] = Field(
        default=None, alias="ApplicationRuntimeId"
    )
    supported_dp_usizes: Optional[List[int]] = Field(
        default=None, alias="SupportedDPUSizes"
    )


class AthenaErrorModel(BaseModel):
    error_category: Optional[int] = Field(default=None, alias="ErrorCategory")
    error_type: Optional[int] = Field(default=None, alias="ErrorType")
    retryable: Optional[bool] = Field(default=None, alias="Retryable")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchGetNamedQueryInputRequestModel(BaseModel):
    named_query_ids: Sequence[str] = Field(alias="NamedQueryIds")


class NamedQueryModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    query_string: str = Field(alias="QueryString")
    description: Optional[str] = Field(default=None, alias="Description")
    named_query_id: Optional[str] = Field(default=None, alias="NamedQueryId")
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UnprocessedNamedQueryIdModel(BaseModel):
    named_query_id: Optional[str] = Field(default=None, alias="NamedQueryId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchGetPreparedStatementInputRequestModel(BaseModel):
    prepared_statement_names: Sequence[str] = Field(alias="PreparedStatementNames")
    work_group: str = Field(alias="WorkGroup")


class PreparedStatementModel(BaseModel):
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    query_statement: Optional[str] = Field(default=None, alias="QueryStatement")
    work_group_name: Optional[str] = Field(default=None, alias="WorkGroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class UnprocessedPreparedStatementNameModel(BaseModel):
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchGetQueryExecutionInputRequestModel(BaseModel):
    query_execution_ids: Sequence[str] = Field(alias="QueryExecutionIds")


class UnprocessedQueryExecutionIdModel(BaseModel):
    query_execution_id: Optional[str] = Field(default=None, alias="QueryExecutionId")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class CalculationConfigurationModel(BaseModel):
    code_block: Optional[str] = Field(default=None, alias="CodeBlock")


class CalculationResultModel(BaseModel):
    std_out_s3_uri: Optional[str] = Field(default=None, alias="StdOutS3Uri")
    std_error_s3_uri: Optional[str] = Field(default=None, alias="StdErrorS3Uri")
    result_s3_uri: Optional[str] = Field(default=None, alias="ResultS3Uri")
    result_type: Optional[str] = Field(default=None, alias="ResultType")


class CalculationStatisticsModel(BaseModel):
    dpu_execution_in_millis: Optional[int] = Field(
        default=None, alias="DpuExecutionInMillis"
    )
    progress: Optional[str] = Field(default=None, alias="Progress")


class CalculationStatusModel(BaseModel):
    submission_date_time: Optional[datetime] = Field(
        default=None, alias="SubmissionDateTime"
    )
    completion_date_time: Optional[datetime] = Field(
        default=None, alias="CompletionDateTime"
    )
    state: Optional[
        Literal[
            "CANCELED",
            "CANCELING",
            "COMPLETED",
            "CREATED",
            "CREATING",
            "FAILED",
            "QUEUED",
            "RUNNING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[str] = Field(default=None, alias="StateChangeReason")


class ColumnInfoModel(BaseModel):
    name: str = Field(alias="Name")
    type: str = Field(alias="Type")
    catalog_name: Optional[str] = Field(default=None, alias="CatalogName")
    schema_name: Optional[str] = Field(default=None, alias="SchemaName")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    label: Optional[str] = Field(default=None, alias="Label")
    precision: Optional[int] = Field(default=None, alias="Precision")
    scale: Optional[int] = Field(default=None, alias="Scale")
    nullable: Optional[Literal["NOT_NULL", "NULLABLE", "UNKNOWN"]] = Field(
        default=None, alias="Nullable"
    )
    case_sensitive: Optional[bool] = Field(default=None, alias="CaseSensitive")


class ColumnModel(BaseModel):
    name: str = Field(alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    comment: Optional[str] = Field(default=None, alias="Comment")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CreateNamedQueryInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    database: str = Field(alias="Database")
    query_string: str = Field(alias="QueryString")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")


class CreateNotebookInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class CreatePreparedStatementInputRequestModel(BaseModel):
    statement_name: str = Field(alias="StatementName")
    work_group: str = Field(alias="WorkGroup")
    query_statement: str = Field(alias="QueryStatement")
    description: Optional[str] = Field(default=None, alias="Description")


class CreatePresignedNotebookUrlRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class CustomerContentEncryptionConfigurationModel(BaseModel):
    kms_key: str = Field(alias="KmsKey")


class DataCatalogSummaryModel(BaseModel):
    catalog_name: Optional[str] = Field(default=None, alias="CatalogName")
    type: Optional[Literal["GLUE", "HIVE", "LAMBDA"]] = Field(
        default=None, alias="Type"
    )


class DataCatalogModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["GLUE", "HIVE", "LAMBDA"] = Field(alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")


class DatabaseModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")


class DatumModel(BaseModel):
    var_char_value: Optional[str] = Field(default=None, alias="VarCharValue")


class DeleteDataCatalogInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteNamedQueryInputRequestModel(BaseModel):
    named_query_id: str = Field(alias="NamedQueryId")


class DeleteNotebookInputRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")


class DeletePreparedStatementInputRequestModel(BaseModel):
    statement_name: str = Field(alias="StatementName")
    work_group: str = Field(alias="WorkGroup")


class DeleteWorkGroupInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    recursive_delete_option: Optional[bool] = Field(
        default=None, alias="RecursiveDeleteOption"
    )


class EncryptionConfigurationModel(BaseModel):
    encryption_option: Literal["CSE_KMS", "SSE_KMS", "SSE_S3"] = Field(
        alias="EncryptionOption"
    )
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")


class EngineConfigurationModel(BaseModel):
    max_concurrent_dpus: int = Field(alias="MaxConcurrentDpus")
    coordinator_dpu_size: Optional[int] = Field(
        default=None, alias="CoordinatorDpuSize"
    )
    default_executor_dpu_size: Optional[int] = Field(
        default=None, alias="DefaultExecutorDpuSize"
    )
    additional_configs: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalConfigs"
    )


class EngineVersionModel(BaseModel):
    selected_engine_version: Optional[str] = Field(
        default=None, alias="SelectedEngineVersion"
    )
    effective_engine_version: Optional[str] = Field(
        default=None, alias="EffectiveEngineVersion"
    )


class ExecutorsSummaryModel(BaseModel):
    executor_id: str = Field(alias="ExecutorId")
    executor_type: Optional[Literal["COORDINATOR", "GATEWAY", "WORKER"]] = Field(
        default=None, alias="ExecutorType"
    )
    start_date_time: Optional[int] = Field(default=None, alias="StartDateTime")
    termination_date_time: Optional[int] = Field(
        default=None, alias="TerminationDateTime"
    )
    executor_state: Optional[
        Literal[
            "CREATED", "CREATING", "FAILED", "REGISTERED", "TERMINATED", "TERMINATING"
        ]
    ] = Field(default=None, alias="ExecutorState")
    executor_size: Optional[int] = Field(default=None, alias="ExecutorSize")


class ExportNotebookInputRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")


class NotebookMetadataModel(BaseModel):
    notebook_id: Optional[str] = Field(default=None, alias="NotebookId")
    name: Optional[str] = Field(default=None, alias="Name")
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    type: Optional[Literal["IPYNB"]] = Field(default=None, alias="Type")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class FilterDefinitionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class GetCalculationExecutionCodeRequestModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")


class GetCalculationExecutionRequestModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")


class GetCalculationExecutionStatusRequestModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")


class GetDataCatalogInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetDatabaseInputRequestModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    database_name: str = Field(alias="DatabaseName")


class GetNamedQueryInputRequestModel(BaseModel):
    named_query_id: str = Field(alias="NamedQueryId")


class GetNotebookMetadataInputRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")


class GetPreparedStatementInputRequestModel(BaseModel):
    statement_name: str = Field(alias="StatementName")
    work_group: str = Field(alias="WorkGroup")


class GetQueryExecutionInputRequestModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetQueryResultsInputRequestModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetQueryRuntimeStatisticsInputRequestModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")


class GetSessionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class SessionStatisticsModel(BaseModel):
    dpu_execution_in_millis: Optional[int] = Field(
        default=None, alias="DpuExecutionInMillis"
    )


class SessionStatusModel(BaseModel):
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    last_modified_date_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedDateTime"
    )
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")
    idle_since_date_time: Optional[datetime] = Field(
        default=None, alias="IdleSinceDateTime"
    )
    state: Optional[
        Literal[
            "BUSY",
            "CREATED",
            "CREATING",
            "DEGRADED",
            "FAILED",
            "IDLE",
            "TERMINATED",
            "TERMINATING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[str] = Field(default=None, alias="StateChangeReason")


class GetSessionStatusRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class GetTableMetadataInputRequestModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")


class GetWorkGroupInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")


class ImportNotebookInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    name: str = Field(alias="Name")
    payload: str = Field(alias="Payload")
    type: Literal["IPYNB"] = Field(alias="Type")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ListApplicationDPUSizesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCalculationExecutionsRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    state_filter: Optional[
        Literal[
            "CANCELED",
            "CANCELING",
            "COMPLETED",
            "CREATED",
            "CREATING",
            "FAILED",
            "QUEUED",
            "RUNNING",
        ]
    ] = Field(default=None, alias="StateFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDataCatalogsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDatabasesInputRequestModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEngineVersionsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListExecutorsRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    executor_state_filter: Optional[
        Literal[
            "CREATED", "CREATING", "FAILED", "REGISTERED", "TERMINATED", "TERMINATING"
        ]
    ] = Field(default=None, alias="ExecutorStateFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListNamedQueriesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")


class ListNotebookSessionsRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NotebookSessionSummaryModel(BaseModel):
    session_id: Optional[str] = Field(default=None, alias="SessionId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class ListPreparedStatementsInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PreparedStatementSummaryModel(BaseModel):
    statement_name: Optional[str] = Field(default=None, alias="StatementName")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class ListQueryExecutionsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")


class ListSessionsRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    state_filter: Optional[
        Literal[
            "BUSY",
            "CREATED",
            "CREATING",
            "DEGRADED",
            "FAILED",
            "IDLE",
            "TERMINATED",
            "TERMINATING",
        ]
    ] = Field(default=None, alias="StateFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTableMetadataInputRequestModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    database_name: str = Field(alias="DatabaseName")
    expression: Optional[str] = Field(default=None, alias="Expression")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListWorkGroupsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class QueryExecutionContextModel(BaseModel):
    database: Optional[str] = Field(default=None, alias="Database")
    catalog: Optional[str] = Field(default=None, alias="Catalog")


class ResultReuseInformationModel(BaseModel):
    reused_previous_result: bool = Field(alias="ReusedPreviousResult")


class QueryRuntimeStatisticsRowsModel(BaseModel):
    input_rows: Optional[int] = Field(default=None, alias="InputRows")
    input_bytes: Optional[int] = Field(default=None, alias="InputBytes")
    output_bytes: Optional[int] = Field(default=None, alias="OutputBytes")
    output_rows: Optional[int] = Field(default=None, alias="OutputRows")


class QueryRuntimeStatisticsTimelineModel(BaseModel):
    query_queue_time_in_millis: Optional[int] = Field(
        default=None, alias="QueryQueueTimeInMillis"
    )
    query_planning_time_in_millis: Optional[int] = Field(
        default=None, alias="QueryPlanningTimeInMillis"
    )
    engine_execution_time_in_millis: Optional[int] = Field(
        default=None, alias="EngineExecutionTimeInMillis"
    )
    service_processing_time_in_millis: Optional[int] = Field(
        default=None, alias="ServiceProcessingTimeInMillis"
    )
    total_execution_time_in_millis: Optional[int] = Field(
        default=None, alias="TotalExecutionTimeInMillis"
    )


class QueryStagePlanNodeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    children: Optional[List[Dict[str, Any]]] = Field(default=None, alias="Children")
    remote_sources: Optional[List[str]] = Field(default=None, alias="RemoteSources")


class QueryStageModel(BaseModel):
    stage_id: Optional[int] = Field(default=None, alias="StageId")
    state: Optional[str] = Field(default=None, alias="State")
    output_bytes: Optional[int] = Field(default=None, alias="OutputBytes")
    output_rows: Optional[int] = Field(default=None, alias="OutputRows")
    input_bytes: Optional[int] = Field(default=None, alias="InputBytes")
    input_rows: Optional[int] = Field(default=None, alias="InputRows")
    execution_time: Optional[int] = Field(default=None, alias="ExecutionTime")
    query_stage_plan: Optional[QueryStagePlanNodeModel] = Field(
        default=None, alias="QueryStagePlan"
    )
    sub_stages: Optional[List[Dict[str, Any]]] = Field(default=None, alias="SubStages")


class ResultReuseByAgeConfigurationModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    max_age_in_minutes: Optional[int] = Field(default=None, alias="MaxAgeInMinutes")


class StopCalculationExecutionRequestModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")


class StopQueryExecutionInputRequestModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")


class TerminateSessionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDataCatalogInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["GLUE", "HIVE", "LAMBDA"] = Field(alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class UpdateNamedQueryInputRequestModel(BaseModel):
    named_query_id: str = Field(alias="NamedQueryId")
    name: str = Field(alias="Name")
    query_string: str = Field(alias="QueryString")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateNotebookInputRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")
    payload: str = Field(alias="Payload")
    type: Literal["IPYNB"] = Field(alias="Type")
    session_id: Optional[str] = Field(default=None, alias="SessionId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class UpdateNotebookMetadataInputRequestModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class UpdatePreparedStatementInputRequestModel(BaseModel):
    statement_name: str = Field(alias="StatementName")
    work_group: str = Field(alias="WorkGroup")
    query_statement: str = Field(alias="QueryStatement")
    description: Optional[str] = Field(default=None, alias="Description")


class QueryExecutionStatusModel(BaseModel):
    state: Optional[
        Literal["CANCELLED", "FAILED", "QUEUED", "RUNNING", "SUCCEEDED"]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[str] = Field(default=None, alias="StateChangeReason")
    submission_date_time: Optional[datetime] = Field(
        default=None, alias="SubmissionDateTime"
    )
    completion_date_time: Optional[datetime] = Field(
        default=None, alias="CompletionDateTime"
    )
    athena_error: Optional[AthenaErrorModel] = Field(default=None, alias="AthenaError")


class CreateNamedQueryOutputModel(BaseModel):
    named_query_id: str = Field(alias="NamedQueryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNotebookOutputModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePresignedNotebookUrlResponseModel(BaseModel):
    notebook_url: str = Field(alias="NotebookUrl")
    auth_token: str = Field(alias="AuthToken")
    auth_token_expiration_time: int = Field(alias="AuthTokenExpirationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCalculationExecutionCodeResponseModel(BaseModel):
    code_block: str = Field(alias="CodeBlock")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNamedQueryOutputModel(BaseModel):
    named_query: NamedQueryModel = Field(alias="NamedQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportNotebookOutputModel(BaseModel):
    notebook_id: str = Field(alias="NotebookId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationDPUSizesOutputModel(BaseModel):
    application_dp_usizes: List[ApplicationDPUSizesModel] = Field(
        alias="ApplicationDPUSizes"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNamedQueriesOutputModel(BaseModel):
    named_query_ids: List[str] = Field(alias="NamedQueryIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueryExecutionsOutputModel(BaseModel):
    query_execution_ids: List[str] = Field(alias="QueryExecutionIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCalculationExecutionResponseModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")
    state: Literal[
        "CANCELED",
        "CANCELING",
        "COMPLETED",
        "CREATED",
        "CREATING",
        "FAILED",
        "QUEUED",
        "RUNNING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartQueryExecutionOutputModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSessionResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    state: Literal[
        "BUSY",
        "CREATED",
        "CREATING",
        "DEGRADED",
        "FAILED",
        "IDLE",
        "TERMINATED",
        "TERMINATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopCalculationExecutionResponseModel(BaseModel):
    state: Literal[
        "CANCELED",
        "CANCELING",
        "COMPLETED",
        "CREATED",
        "CREATING",
        "FAILED",
        "QUEUED",
        "RUNNING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateSessionResponseModel(BaseModel):
    state: Literal[
        "BUSY",
        "CREATED",
        "CREATING",
        "DEGRADED",
        "FAILED",
        "IDLE",
        "TERMINATED",
        "TERMINATING",
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetNamedQueryOutputModel(BaseModel):
    named_queries: List[NamedQueryModel] = Field(alias="NamedQueries")
    unprocessed_named_query_ids: List[UnprocessedNamedQueryIdModel] = Field(
        alias="UnprocessedNamedQueryIds"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPreparedStatementOutputModel(BaseModel):
    prepared_statement: PreparedStatementModel = Field(alias="PreparedStatement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetPreparedStatementOutputModel(BaseModel):
    prepared_statements: List[PreparedStatementModel] = Field(
        alias="PreparedStatements"
    )
    unprocessed_prepared_statement_names: List[
        UnprocessedPreparedStatementNameModel
    ] = Field(alias="UnprocessedPreparedStatementNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCalculationExecutionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    description: Optional[str] = Field(default=None, alias="Description")
    calculation_configuration: Optional[CalculationConfigurationModel] = Field(
        default=None, alias="CalculationConfiguration"
    )
    code_block: Optional[str] = Field(default=None, alias="CodeBlock")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class CalculationSummaryModel(BaseModel):
    calculation_execution_id: Optional[str] = Field(
        default=None, alias="CalculationExecutionId"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[CalculationStatusModel] = Field(default=None, alias="Status")


class GetCalculationExecutionResponseModel(BaseModel):
    calculation_execution_id: str = Field(alias="CalculationExecutionId")
    session_id: str = Field(alias="SessionId")
    description: str = Field(alias="Description")
    working_directory: str = Field(alias="WorkingDirectory")
    status: CalculationStatusModel = Field(alias="Status")
    statistics: CalculationStatisticsModel = Field(alias="Statistics")
    result: CalculationResultModel = Field(alias="Result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCalculationExecutionStatusResponseModel(BaseModel):
    status: CalculationStatusModel = Field(alias="Status")
    statistics: CalculationStatisticsModel = Field(alias="Statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResultSetMetadataModel(BaseModel):
    column_info: Optional[List[ColumnInfoModel]] = Field(
        default=None, alias="ColumnInfo"
    )


class TableMetadataModel(BaseModel):
    name: str = Field(alias="Name")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    last_access_time: Optional[datetime] = Field(default=None, alias="LastAccessTime")
    table_type: Optional[str] = Field(default=None, alias="TableType")
    columns: Optional[List[ColumnModel]] = Field(default=None, alias="Columns")
    partition_keys: Optional[List[ColumnModel]] = Field(
        default=None, alias="PartitionKeys"
    )
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")


class CreateDataCatalogInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["GLUE", "HIVE", "LAMBDA"] = Field(alias="Type")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListDataCatalogsOutputModel(BaseModel):
    data_catalogs_summary: List[DataCatalogSummaryModel] = Field(
        alias="DataCatalogsSummary"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataCatalogOutputModel(BaseModel):
    data_catalog: DataCatalogModel = Field(alias="DataCatalog")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDatabaseOutputModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatabasesOutputModel(BaseModel):
    database_list: List[DatabaseModel] = Field(alias="DatabaseList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RowModel(BaseModel):
    data: Optional[List[DatumModel]] = Field(default=None, alias="Data")


class ResultConfigurationModel(BaseModel):
    output_location: Optional[str] = Field(default=None, alias="OutputLocation")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    acl_configuration: Optional[AclConfigurationModel] = Field(
        default=None, alias="AclConfiguration"
    )


class ResultConfigurationUpdatesModel(BaseModel):
    output_location: Optional[str] = Field(default=None, alias="OutputLocation")
    remove_output_location: Optional[bool] = Field(
        default=None, alias="RemoveOutputLocation"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    remove_encryption_configuration: Optional[bool] = Field(
        default=None, alias="RemoveEncryptionConfiguration"
    )
    expected_bucket_owner: Optional[str] = Field(
        default=None, alias="ExpectedBucketOwner"
    )
    remove_expected_bucket_owner: Optional[bool] = Field(
        default=None, alias="RemoveExpectedBucketOwner"
    )
    acl_configuration: Optional[AclConfigurationModel] = Field(
        default=None, alias="AclConfiguration"
    )
    remove_acl_configuration: Optional[bool] = Field(
        default=None, alias="RemoveAclConfiguration"
    )


class SessionConfigurationModel(BaseModel):
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")
    idle_timeout_seconds: Optional[int] = Field(
        default=None, alias="IdleTimeoutSeconds"
    )
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )


class StartSessionRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    engine_configuration: EngineConfigurationModel = Field(alias="EngineConfiguration")
    description: Optional[str] = Field(default=None, alias="Description")
    notebook_version: Optional[str] = Field(default=None, alias="NotebookVersion")
    session_idle_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="SessionIdleTimeoutInMinutes"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ListEngineVersionsOutputModel(BaseModel):
    engine_versions: List[EngineVersionModel] = Field(alias="EngineVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkGroupSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    engine_version: Optional[EngineVersionModel] = Field(
        default=None, alias="EngineVersion"
    )


class ListExecutorsResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    next_token: str = Field(alias="NextToken")
    executors_summary: List[ExecutorsSummaryModel] = Field(alias="ExecutorsSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportNotebookOutputModel(BaseModel):
    notebook_metadata: NotebookMetadataModel = Field(alias="NotebookMetadata")
    payload: str = Field(alias="Payload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNotebookMetadataOutputModel(BaseModel):
    notebook_metadata: NotebookMetadataModel = Field(alias="NotebookMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotebookMetadataOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    notebook_metadata_list: List[NotebookMetadataModel] = Field(
        alias="NotebookMetadataList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotebookMetadataInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    filters: Optional[FilterDefinitionModel] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetQueryResultsInputGetQueryResultsPaginateModel(BaseModel):
    query_execution_id: str = Field(alias="QueryExecutionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataCatalogsInputListDataCatalogsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatabasesInputListDatabasesPaginateModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNamedQueriesInputListNamedQueriesPaginateModel(BaseModel):
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueryExecutionsInputListQueryExecutionsPaginateModel(BaseModel):
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTableMetadataInputListTableMetadataPaginateModel(BaseModel):
    catalog_name: str = Field(alias="CatalogName")
    database_name: str = Field(alias="DatabaseName")
    expression: Optional[str] = Field(default=None, alias="Expression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceInputListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSessionStatusResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    status: SessionStatusModel = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SessionSummaryModel(BaseModel):
    session_id: Optional[str] = Field(default=None, alias="SessionId")
    description: Optional[str] = Field(default=None, alias="Description")
    engine_version: Optional[EngineVersionModel] = Field(
        default=None, alias="EngineVersion"
    )
    notebook_version: Optional[str] = Field(default=None, alias="NotebookVersion")
    status: Optional[SessionStatusModel] = Field(default=None, alias="Status")


class ListNotebookSessionsResponseModel(BaseModel):
    notebook_sessions_list: List[NotebookSessionSummaryModel] = Field(
        alias="NotebookSessionsList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPreparedStatementsOutputModel(BaseModel):
    prepared_statements: List[PreparedStatementSummaryModel] = Field(
        alias="PreparedStatements"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryExecutionStatisticsModel(BaseModel):
    engine_execution_time_in_millis: Optional[int] = Field(
        default=None, alias="EngineExecutionTimeInMillis"
    )
    data_scanned_in_bytes: Optional[int] = Field(
        default=None, alias="DataScannedInBytes"
    )
    data_manifest_location: Optional[str] = Field(
        default=None, alias="DataManifestLocation"
    )
    total_execution_time_in_millis: Optional[int] = Field(
        default=None, alias="TotalExecutionTimeInMillis"
    )
    query_queue_time_in_millis: Optional[int] = Field(
        default=None, alias="QueryQueueTimeInMillis"
    )
    query_planning_time_in_millis: Optional[int] = Field(
        default=None, alias="QueryPlanningTimeInMillis"
    )
    service_processing_time_in_millis: Optional[int] = Field(
        default=None, alias="ServiceProcessingTimeInMillis"
    )
    result_reuse_information: Optional[ResultReuseInformationModel] = Field(
        default=None, alias="ResultReuseInformation"
    )


class QueryRuntimeStatisticsModel(BaseModel):
    timeline: Optional[QueryRuntimeStatisticsTimelineModel] = Field(
        default=None, alias="Timeline"
    )
    rows: Optional[QueryRuntimeStatisticsRowsModel] = Field(default=None, alias="Rows")
    output_stage: Optional[QueryStageModel] = Field(default=None, alias="OutputStage")


class ResultReuseConfigurationModel(BaseModel):
    result_reuse_by_age_configuration: Optional[
        ResultReuseByAgeConfigurationModel
    ] = Field(default=None, alias="ResultReuseByAgeConfiguration")


class ListCalculationExecutionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    calculations: List[CalculationSummaryModel] = Field(alias="Calculations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTableMetadataOutputModel(BaseModel):
    table_metadata: TableMetadataModel = Field(alias="TableMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTableMetadataOutputModel(BaseModel):
    table_metadata_list: List[TableMetadataModel] = Field(alias="TableMetadataList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResultSetModel(BaseModel):
    rows: Optional[List[RowModel]] = Field(default=None, alias="Rows")
    result_set_metadata: Optional[ResultSetMetadataModel] = Field(
        default=None, alias="ResultSetMetadata"
    )


class WorkGroupConfigurationModel(BaseModel):
    result_configuration: Optional[ResultConfigurationModel] = Field(
        default=None, alias="ResultConfiguration"
    )
    enforce_work_group_configuration: Optional[bool] = Field(
        default=None, alias="EnforceWorkGroupConfiguration"
    )
    publish_cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="PublishCloudWatchMetricsEnabled"
    )
    bytes_scanned_cutoff_per_query: Optional[int] = Field(
        default=None, alias="BytesScannedCutoffPerQuery"
    )
    requester_pays_enabled: Optional[bool] = Field(
        default=None, alias="RequesterPaysEnabled"
    )
    engine_version: Optional[EngineVersionModel] = Field(
        default=None, alias="EngineVersion"
    )
    additional_configuration: Optional[str] = Field(
        default=None, alias="AdditionalConfiguration"
    )
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    customer_content_encryption_configuration: Optional[
        CustomerContentEncryptionConfigurationModel
    ] = Field(default=None, alias="CustomerContentEncryptionConfiguration")


class WorkGroupConfigurationUpdatesModel(BaseModel):
    enforce_work_group_configuration: Optional[bool] = Field(
        default=None, alias="EnforceWorkGroupConfiguration"
    )
    result_configuration_updates: Optional[ResultConfigurationUpdatesModel] = Field(
        default=None, alias="ResultConfigurationUpdates"
    )
    publish_cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="PublishCloudWatchMetricsEnabled"
    )
    bytes_scanned_cutoff_per_query: Optional[int] = Field(
        default=None, alias="BytesScannedCutoffPerQuery"
    )
    remove_bytes_scanned_cutoff_per_query: Optional[bool] = Field(
        default=None, alias="RemoveBytesScannedCutoffPerQuery"
    )
    requester_pays_enabled: Optional[bool] = Field(
        default=None, alias="RequesterPaysEnabled"
    )
    engine_version: Optional[EngineVersionModel] = Field(
        default=None, alias="EngineVersion"
    )
    remove_customer_content_encryption_configuration: Optional[bool] = Field(
        default=None, alias="RemoveCustomerContentEncryptionConfiguration"
    )
    additional_configuration: Optional[str] = Field(
        default=None, alias="AdditionalConfiguration"
    )
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    customer_content_encryption_configuration: Optional[
        CustomerContentEncryptionConfigurationModel
    ] = Field(default=None, alias="CustomerContentEncryptionConfiguration")


class GetSessionResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    description: str = Field(alias="Description")
    work_group: str = Field(alias="WorkGroup")
    engine_version: str = Field(alias="EngineVersion")
    engine_configuration: EngineConfigurationModel = Field(alias="EngineConfiguration")
    notebook_version: str = Field(alias="NotebookVersion")
    session_configuration: SessionConfigurationModel = Field(
        alias="SessionConfiguration"
    )
    status: SessionStatusModel = Field(alias="Status")
    statistics: SessionStatisticsModel = Field(alias="Statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkGroupsOutputModel(BaseModel):
    work_groups: List[WorkGroupSummaryModel] = Field(alias="WorkGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSessionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    sessions: List[SessionSummaryModel] = Field(alias="Sessions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryRuntimeStatisticsOutputModel(BaseModel):
    query_runtime_statistics: QueryRuntimeStatisticsModel = Field(
        alias="QueryRuntimeStatistics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryExecutionModel(BaseModel):
    query_execution_id: Optional[str] = Field(default=None, alias="QueryExecutionId")
    query: Optional[str] = Field(default=None, alias="Query")
    statement_type: Optional[Literal["DDL", "DML", "UTILITY"]] = Field(
        default=None, alias="StatementType"
    )
    result_configuration: Optional[ResultConfigurationModel] = Field(
        default=None, alias="ResultConfiguration"
    )
    result_reuse_configuration: Optional[ResultReuseConfigurationModel] = Field(
        default=None, alias="ResultReuseConfiguration"
    )
    query_execution_context: Optional[QueryExecutionContextModel] = Field(
        default=None, alias="QueryExecutionContext"
    )
    status: Optional[QueryExecutionStatusModel] = Field(default=None, alias="Status")
    statistics: Optional[QueryExecutionStatisticsModel] = Field(
        default=None, alias="Statistics"
    )
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    engine_version: Optional[EngineVersionModel] = Field(
        default=None, alias="EngineVersion"
    )
    execution_parameters: Optional[List[str]] = Field(
        default=None, alias="ExecutionParameters"
    )


class StartQueryExecutionInputRequestModel(BaseModel):
    query_string: str = Field(alias="QueryString")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    query_execution_context: Optional[QueryExecutionContextModel] = Field(
        default=None, alias="QueryExecutionContext"
    )
    result_configuration: Optional[ResultConfigurationModel] = Field(
        default=None, alias="ResultConfiguration"
    )
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    execution_parameters: Optional[Sequence[str]] = Field(
        default=None, alias="ExecutionParameters"
    )
    result_reuse_configuration: Optional[ResultReuseConfigurationModel] = Field(
        default=None, alias="ResultReuseConfiguration"
    )


class GetQueryResultsOutputModel(BaseModel):
    update_count: int = Field(alias="UpdateCount")
    result_set: ResultSetModel = Field(alias="ResultSet")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    configuration: Optional[WorkGroupConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class WorkGroupModel(BaseModel):
    name: str = Field(alias="Name")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    configuration: Optional[WorkGroupConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class UpdateWorkGroupInputRequestModel(BaseModel):
    work_group: str = Field(alias="WorkGroup")
    description: Optional[str] = Field(default=None, alias="Description")
    configuration_updates: Optional[WorkGroupConfigurationUpdatesModel] = Field(
        default=None, alias="ConfigurationUpdates"
    )
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")


class BatchGetQueryExecutionOutputModel(BaseModel):
    query_executions: List[QueryExecutionModel] = Field(alias="QueryExecutions")
    unprocessed_query_execution_ids: List[UnprocessedQueryExecutionIdModel] = Field(
        alias="UnprocessedQueryExecutionIds"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryExecutionOutputModel(BaseModel):
    query_execution: QueryExecutionModel = Field(alias="QueryExecution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkGroupOutputModel(BaseModel):
    work_group: WorkGroupModel = Field(alias="WorkGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
