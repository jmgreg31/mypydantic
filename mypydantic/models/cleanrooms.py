# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AggregateColumnModel(BaseModel):
    column_names: Sequence[str] = Field(alias="columnNames")
    function: Literal["AVG", "COUNT", "COUNT_DISTINCT", "SUM", "SUM_DISTINCT"] = Field(
        alias="function"
    )


class AggregationConstraintModel(BaseModel):
    column_name: str = Field(alias="columnName")
    minimum: int = Field(alias="minimum")
    type: Literal["COUNT_DISTINCT"] = Field(alias="type")


class AnalysisRuleListModel(BaseModel):
    join_columns: Sequence[str] = Field(alias="joinColumns")
    list_columns: Sequence[str] = Field(alias="listColumns")


class BatchGetSchemaErrorModel(BaseModel):
    name: str = Field(alias="name")
    code: str = Field(alias="code")
    message: str = Field(alias="message")


class BatchGetSchemaInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    names: Sequence[str] = Field(alias="names")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CollaborationSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    creator_account_id: str = Field(alias="creatorAccountId")
    creator_display_name: str = Field(alias="creatorDisplayName")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    member_status: Literal["ACTIVE", "INVITED", "LEFT", "REMOVED"] = Field(
        alias="memberStatus"
    )
    membership_id: Optional[str] = Field(default=None, alias="membershipId")
    membership_arn: Optional[str] = Field(default=None, alias="membershipArn")


class DataEncryptionMetadataModel(BaseModel):
    allow_cleartext: bool = Field(alias="allowCleartext")
    allow_duplicates: bool = Field(alias="allowDuplicates")
    allow_joins_on_columns_with_different_names: bool = Field(
        alias="allowJoinsOnColumnsWithDifferentNames"
    )
    preserve_nulls: bool = Field(alias="preserveNulls")


class ColumnModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")


class ConfiguredTableAssociationSummaryModel(BaseModel):
    configured_table_id: str = Field(alias="configuredTableId")
    membership_id: str = Field(alias="membershipId")
    membership_arn: str = Field(alias="membershipArn")
    name: str = Field(alias="name")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")


class ConfiguredTableAssociationModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    configured_table_id: str = Field(alias="configuredTableId")
    configured_table_arn: str = Field(alias="configuredTableArn")
    membership_id: str = Field(alias="membershipId")
    membership_arn: str = Field(alias="membershipArn")
    role_arn: str = Field(alias="roleArn")
    name: str = Field(alias="name")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    description: Optional[str] = Field(default=None, alias="description")


class ConfiguredTableSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    analysis_rule_types: List[Literal["AGGREGATION", "LIST"]] = Field(
        alias="analysisRuleTypes"
    )
    analysis_method: Literal["DIRECT_QUERY"] = Field(alias="analysisMethod")


class MemberSpecificationModel(BaseModel):
    account_id: str = Field(alias="accountId")
    member_abilities: Sequence[Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]] = Field(
        alias="memberAbilities"
    )
    display_name: str = Field(alias="displayName")


class CreateConfiguredTableAssociationInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    membership_identifier: str = Field(alias="membershipIdentifier")
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    role_arn: str = Field(alias="roleArn")
    description: Optional[str] = Field(default=None, alias="description")


class CreateMembershipInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    query_log_status: Literal["DISABLED", "ENABLED"] = Field(alias="queryLogStatus")


class MembershipModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    collaboration_arn: str = Field(alias="collaborationArn")
    collaboration_id: str = Field(alias="collaborationId")
    collaboration_creator_account_id: str = Field(alias="collaborationCreatorAccountId")
    collaboration_creator_display_name: str = Field(
        alias="collaborationCreatorDisplayName"
    )
    collaboration_name: str = Field(alias="collaborationName")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    status: Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"] = Field(
        alias="status"
    )
    member_abilities: List[Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]] = Field(
        alias="memberAbilities"
    )
    query_log_status: Literal["DISABLED", "ENABLED"] = Field(alias="queryLogStatus")


class DeleteCollaborationInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")


class DeleteConfiguredTableAnalysisRuleInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    analysis_rule_type: Literal["AGGREGATION", "LIST"] = Field(alias="analysisRuleType")


class DeleteConfiguredTableAssociationInputRequestModel(BaseModel):
    configured_table_association_identifier: str = Field(
        alias="configuredTableAssociationIdentifier"
    )
    membership_identifier: str = Field(alias="membershipIdentifier")


class DeleteConfiguredTableInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")


class DeleteMemberInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    account_id: str = Field(alias="accountId")


class DeleteMembershipInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")


class GetCollaborationInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")


class GetConfiguredTableAnalysisRuleInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    analysis_rule_type: Literal["AGGREGATION", "LIST"] = Field(alias="analysisRuleType")


class GetConfiguredTableAssociationInputRequestModel(BaseModel):
    configured_table_association_identifier: str = Field(
        alias="configuredTableAssociationIdentifier"
    )
    membership_identifier: str = Field(alias="membershipIdentifier")


class GetConfiguredTableInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")


class GetMembershipInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")


class GetProtectedQueryInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    protected_query_identifier: str = Field(alias="protectedQueryIdentifier")


class GetSchemaAnalysisRuleInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    name: str = Field(alias="name")
    type: Literal["AGGREGATION", "LIST"] = Field(alias="type")


class GetSchemaInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    name: str = Field(alias="name")


class GlueTableReferenceModel(BaseModel):
    table_name: str = Field(alias="tableName")
    database_name: str = Field(alias="databaseName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListCollaborationsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    member_status: Optional[Literal["ACTIVE", "INVITED"]] = Field(
        default=None, alias="memberStatus"
    )


class ListConfiguredTableAssociationsInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListConfiguredTablesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListMembersInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class MemberSummaryModel(BaseModel):
    account_id: str = Field(alias="accountId")
    status: Literal["ACTIVE", "INVITED", "LEFT", "REMOVED"] = Field(alias="status")
    display_name: str = Field(alias="displayName")
    abilities: List[Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]] = Field(
        alias="abilities"
    )
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    membership_id: Optional[str] = Field(default=None, alias="membershipId")
    membership_arn: Optional[str] = Field(default=None, alias="membershipArn")


class ListMembershipsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    status: Optional[Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"]] = Field(
        default=None, alias="status"
    )


class MembershipSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    collaboration_arn: str = Field(alias="collaborationArn")
    collaboration_id: str = Field(alias="collaborationId")
    collaboration_creator_account_id: str = Field(alias="collaborationCreatorAccountId")
    collaboration_creator_display_name: str = Field(
        alias="collaborationCreatorDisplayName"
    )
    collaboration_name: str = Field(alias="collaborationName")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    status: Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"] = Field(
        alias="status"
    )
    member_abilities: List[Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]] = Field(
        alias="memberAbilities"
    )


class ListProtectedQueriesInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "FAILED",
            "STARTED",
            "SUBMITTED",
            "SUCCESS",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ProtectedQuerySummaryModel(BaseModel):
    id: str = Field(alias="id")
    membership_id: str = Field(alias="membershipId")
    membership_arn: str = Field(alias="membershipArn")
    create_time: datetime = Field(alias="createTime")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "STARTED",
        "SUBMITTED",
        "SUCCESS",
        "TIMED_OUT",
    ] = Field(alias="status")


class ListSchemasInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    schema_type: Optional[Literal["TABLE"]] = Field(default=None, alias="schemaType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SchemaSummaryModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["TABLE"] = Field(alias="type")
    creator_account_id: str = Field(alias="creatorAccountId")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    collaboration_id: str = Field(alias="collaborationId")
    collaboration_arn: str = Field(alias="collaborationArn")
    analysis_rule_types: List[Literal["AGGREGATION", "LIST"]] = Field(
        alias="analysisRuleTypes"
    )
    analysis_method: Optional[Literal["DIRECT_QUERY"]] = Field(
        default=None, alias="analysisMethod"
    )


class ProtectedQueryErrorModel(BaseModel):
    message: str = Field(alias="message")
    code: str = Field(alias="code")


class ProtectedQueryS3OutputConfigurationModel(BaseModel):
    result_format: Literal["CSV", "PARQUET"] = Field(alias="resultFormat")
    bucket: str = Field(alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class ProtectedQueryS3OutputModel(BaseModel):
    location: str = Field(alias="location")


class ProtectedQuerySQLParametersModel(BaseModel):
    query_string: str = Field(alias="queryString")


class ProtectedQueryStatisticsModel(BaseModel):
    total_duration_in_millis: Optional[int] = Field(
        default=None, alias="totalDurationInMillis"
    )


class UpdateCollaborationInputRequestModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateConfiguredTableAssociationInputRequestModel(BaseModel):
    configured_table_association_identifier: str = Field(
        alias="configuredTableAssociationIdentifier"
    )
    membership_identifier: str = Field(alias="membershipIdentifier")
    description: Optional[str] = Field(default=None, alias="description")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class UpdateConfiguredTableInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateMembershipInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    query_log_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="queryLogStatus"
    )


class UpdateProtectedQueryInputRequestModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    protected_query_identifier: str = Field(alias="protectedQueryIdentifier")
    target_status: Literal["CANCELLED"] = Field(alias="targetStatus")


class AnalysisRuleAggregationModel(BaseModel):
    aggregate_columns: Sequence[AggregateColumnModel] = Field(alias="aggregateColumns")
    join_columns: Sequence[str] = Field(alias="joinColumns")
    dimension_columns: Sequence[str] = Field(alias="dimensionColumns")
    scalar_functions: Sequence[
        Literal[
            "ABS",
            "CAST",
            "CEILING",
            "COALESCE",
            "FLOOR",
            "LN",
            "LOG",
            "LOWER",
            "ROUND",
            "RTRIM",
            "SQRT",
            "TRUNC",
            "UPPER",
        ]
    ] = Field(alias="scalarFunctions")
    output_constraints: Sequence[AggregationConstraintModel] = Field(
        alias="outputConstraints"
    )
    join_required: Optional[Literal["QUERY_RUNNER"]] = Field(
        default=None, alias="joinRequired"
    )


class ListCollaborationsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    collaboration_list: List[CollaborationSummaryModel] = Field(
        alias="collaborationList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CollaborationModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    creator_account_id: str = Field(alias="creatorAccountId")
    creator_display_name: str = Field(alias="creatorDisplayName")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    member_status: Literal["ACTIVE", "INVITED", "LEFT", "REMOVED"] = Field(
        alias="memberStatus"
    )
    query_log_status: Literal["DISABLED", "ENABLED"] = Field(alias="queryLogStatus")
    description: Optional[str] = Field(default=None, alias="description")
    membership_id: Optional[str] = Field(default=None, alias="membershipId")
    membership_arn: Optional[str] = Field(default=None, alias="membershipArn")
    data_encryption_metadata: Optional[DataEncryptionMetadataModel] = Field(
        default=None, alias="dataEncryptionMetadata"
    )


class SchemaModel(BaseModel):
    columns: List[ColumnModel] = Field(alias="columns")
    partition_keys: List[ColumnModel] = Field(alias="partitionKeys")
    analysis_rule_types: List[Literal["AGGREGATION", "LIST"]] = Field(
        alias="analysisRuleTypes"
    )
    creator_account_id: str = Field(alias="creatorAccountId")
    name: str = Field(alias="name")
    collaboration_id: str = Field(alias="collaborationId")
    collaboration_arn: str = Field(alias="collaborationArn")
    description: str = Field(alias="description")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    type: Literal["TABLE"] = Field(alias="type")
    analysis_method: Optional[Literal["DIRECT_QUERY"]] = Field(
        default=None, alias="analysisMethod"
    )


class ListConfiguredTableAssociationsOutputModel(BaseModel):
    configured_table_association_summaries: List[
        ConfiguredTableAssociationSummaryModel
    ] = Field(alias="configuredTableAssociationSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConfiguredTableAssociationOutputModel(BaseModel):
    configured_table_association: ConfiguredTableAssociationModel = Field(
        alias="configuredTableAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConfiguredTableAssociationOutputModel(BaseModel):
    configured_table_association: ConfiguredTableAssociationModel = Field(
        alias="configuredTableAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfiguredTableAssociationOutputModel(BaseModel):
    configured_table_association: ConfiguredTableAssociationModel = Field(
        alias="configuredTableAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfiguredTablesOutputModel(BaseModel):
    configured_table_summaries: List[ConfiguredTableSummaryModel] = Field(
        alias="configuredTableSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCollaborationInputRequestModel(BaseModel):
    members: Sequence[MemberSpecificationModel] = Field(alias="members")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    creator_member_abilities: Sequence[
        Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]
    ] = Field(alias="creatorMemberAbilities")
    creator_display_name: str = Field(alias="creatorDisplayName")
    query_log_status: Literal["DISABLED", "ENABLED"] = Field(alias="queryLogStatus")
    data_encryption_metadata: Optional[DataEncryptionMetadataModel] = Field(
        default=None, alias="dataEncryptionMetadata"
    )


class CreateMembershipOutputModel(BaseModel):
    membership: MembershipModel = Field(alias="membership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMembershipOutputModel(BaseModel):
    membership: MembershipModel = Field(alias="membership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMembershipOutputModel(BaseModel):
    membership: MembershipModel = Field(alias="membership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TableReferenceModel(BaseModel):
    glue: Optional[GlueTableReferenceModel] = Field(default=None, alias="glue")


class ListCollaborationsInputListCollaborationsPaginateModel(BaseModel):
    member_status: Optional[Literal["ACTIVE", "INVITED"]] = Field(
        default=None, alias="memberStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateModel(
    BaseModel
):
    membership_identifier: str = Field(alias="membershipIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfiguredTablesInputListConfiguredTablesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersInputListMembersPaginateModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembershipsInputListMembershipsPaginateModel(BaseModel):
    status: Optional[Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"]] = Field(
        default=None, alias="status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProtectedQueriesInputListProtectedQueriesPaginateModel(BaseModel):
    membership_identifier: str = Field(alias="membershipIdentifier")
    status: Optional[
        Literal[
            "CANCELLED",
            "CANCELLING",
            "FAILED",
            "STARTED",
            "SUBMITTED",
            "SUCCESS",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchemasInputListSchemasPaginateModel(BaseModel):
    collaboration_identifier: str = Field(alias="collaborationIdentifier")
    schema_type: Optional[Literal["TABLE"]] = Field(default=None, alias="schemaType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    member_summaries: List[MemberSummaryModel] = Field(alias="memberSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembershipsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    membership_summaries: List[MembershipSummaryModel] = Field(
        alias="membershipSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProtectedQueriesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    protected_queries: List[ProtectedQuerySummaryModel] = Field(
        alias="protectedQueries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSchemasOutputModel(BaseModel):
    schema_summaries: List[SchemaSummaryModel] = Field(alias="schemaSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProtectedQueryOutputConfigurationModel(BaseModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationModel] = Field(
        default=None, alias="s3"
    )


class ProtectedQueryOutputModel(BaseModel):
    s3: Optional[ProtectedQueryS3OutputModel] = Field(default=None, alias="s3")


class AnalysisRulePolicyV1Model(BaseModel):
    list: Optional[AnalysisRuleListModel] = Field(default=None, alias="list")
    aggregation: Optional[AnalysisRuleAggregationModel] = Field(
        default=None, alias="aggregation"
    )


class ConfiguredTableAnalysisRulePolicyV1Model(BaseModel):
    list: Optional[AnalysisRuleListModel] = Field(default=None, alias="list")
    aggregation: Optional[AnalysisRuleAggregationModel] = Field(
        default=None, alias="aggregation"
    )


class CreateCollaborationOutputModel(BaseModel):
    collaboration: CollaborationModel = Field(alias="collaboration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCollaborationOutputModel(BaseModel):
    collaboration: CollaborationModel = Field(alias="collaboration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCollaborationOutputModel(BaseModel):
    collaboration: CollaborationModel = Field(alias="collaboration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetSchemaOutputModel(BaseModel):
    schemas: List[SchemaModel] = Field(alias="schemas")
    errors: List[BatchGetSchemaErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaOutputModel(BaseModel):
    schema_: SchemaModel = Field(alias="schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfiguredTableModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    table_reference: TableReferenceModel = Field(alias="tableReference")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    analysis_rule_types: List[Literal["AGGREGATION", "LIST"]] = Field(
        alias="analysisRuleTypes"
    )
    analysis_method: Literal["DIRECT_QUERY"] = Field(alias="analysisMethod")
    allowed_columns: List[str] = Field(alias="allowedColumns")
    description: Optional[str] = Field(default=None, alias="description")


class CreateConfiguredTableInputRequestModel(BaseModel):
    name: str = Field(alias="name")
    table_reference: TableReferenceModel = Field(alias="tableReference")
    allowed_columns: Sequence[str] = Field(alias="allowedColumns")
    analysis_method: Literal["DIRECT_QUERY"] = Field(alias="analysisMethod")
    description: Optional[str] = Field(default=None, alias="description")


class ProtectedQueryResultConfigurationModel(BaseModel):
    output_configuration: ProtectedQueryOutputConfigurationModel = Field(
        alias="outputConfiguration"
    )


class ProtectedQueryResultModel(BaseModel):
    output: ProtectedQueryOutputModel = Field(alias="output")


class AnalysisRulePolicyModel(BaseModel):
    v1: Optional[AnalysisRulePolicyV1Model] = Field(default=None, alias="v1")


class ConfiguredTableAnalysisRulePolicyModel(BaseModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1Model] = Field(
        default=None, alias="v1"
    )


class CreateConfiguredTableOutputModel(BaseModel):
    configured_table: ConfiguredTableModel = Field(alias="configuredTable")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConfiguredTableOutputModel(BaseModel):
    configured_table: ConfiguredTableModel = Field(alias="configuredTable")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfiguredTableOutputModel(BaseModel):
    configured_table: ConfiguredTableModel = Field(alias="configuredTable")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartProtectedQueryInputRequestModel(BaseModel):
    type: Literal["SQL"] = Field(alias="type")
    membership_identifier: str = Field(alias="membershipIdentifier")
    sql_parameters: ProtectedQuerySQLParametersModel = Field(alias="sqlParameters")
    result_configuration: ProtectedQueryResultConfigurationModel = Field(
        alias="resultConfiguration"
    )


class ProtectedQueryModel(BaseModel):
    id: str = Field(alias="id")
    membership_id: str = Field(alias="membershipId")
    membership_arn: str = Field(alias="membershipArn")
    create_time: datetime = Field(alias="createTime")
    sql_parameters: ProtectedQuerySQLParametersModel = Field(alias="sqlParameters")
    status: Literal[
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "STARTED",
        "SUBMITTED",
        "SUCCESS",
        "TIMED_OUT",
    ] = Field(alias="status")
    result_configuration: ProtectedQueryResultConfigurationModel = Field(
        alias="resultConfiguration"
    )
    statistics: Optional[ProtectedQueryStatisticsModel] = Field(
        default=None, alias="statistics"
    )
    result: Optional[ProtectedQueryResultModel] = Field(default=None, alias="result")
    error: Optional[ProtectedQueryErrorModel] = Field(default=None, alias="error")


class AnalysisRuleModel(BaseModel):
    collaboration_id: str = Field(alias="collaborationId")
    type: Literal["AGGREGATION", "LIST"] = Field(alias="type")
    name: str = Field(alias="name")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")
    policy: AnalysisRulePolicyModel = Field(alias="policy")


class ConfiguredTableAnalysisRuleModel(BaseModel):
    configured_table_id: str = Field(alias="configuredTableId")
    configured_table_arn: str = Field(alias="configuredTableArn")
    policy: ConfiguredTableAnalysisRulePolicyModel = Field(alias="policy")
    type: Literal["AGGREGATION", "LIST"] = Field(alias="type")
    create_time: datetime = Field(alias="createTime")
    update_time: datetime = Field(alias="updateTime")


class CreateConfiguredTableAnalysisRuleInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    analysis_rule_type: Literal["AGGREGATION", "LIST"] = Field(alias="analysisRuleType")
    analysis_rule_policy: ConfiguredTableAnalysisRulePolicyModel = Field(
        alias="analysisRulePolicy"
    )


class UpdateConfiguredTableAnalysisRuleInputRequestModel(BaseModel):
    configured_table_identifier: str = Field(alias="configuredTableIdentifier")
    analysis_rule_type: Literal["AGGREGATION", "LIST"] = Field(alias="analysisRuleType")
    analysis_rule_policy: ConfiguredTableAnalysisRulePolicyModel = Field(
        alias="analysisRulePolicy"
    )


class GetProtectedQueryOutputModel(BaseModel):
    protected_query: ProtectedQueryModel = Field(alias="protectedQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartProtectedQueryOutputModel(BaseModel):
    protected_query: ProtectedQueryModel = Field(alias="protectedQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProtectedQueryOutputModel(BaseModel):
    protected_query: ProtectedQueryModel = Field(alias="protectedQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaAnalysisRuleOutputModel(BaseModel):
    analysis_rule: AnalysisRuleModel = Field(alias="analysisRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConfiguredTableAnalysisRuleOutputModel(BaseModel):
    analysis_rule: ConfiguredTableAnalysisRuleModel = Field(alias="analysisRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConfiguredTableAnalysisRuleOutputModel(BaseModel):
    analysis_rule: ConfiguredTableAnalysisRuleModel = Field(alias="analysisRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConfiguredTableAnalysisRuleOutputModel(BaseModel):
    analysis_rule: ConfiguredTableAnalysisRuleModel = Field(alias="analysisRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
