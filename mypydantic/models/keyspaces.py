# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CapacitySpecificationSummaryModel(BaseModel):
    throughput_mode: Literal["PAY_PER_REQUEST", "PROVISIONED"] = Field(
        alias="throughputMode"
    )
    read_capacity_units: Optional[int] = Field(default=None, alias="readCapacityUnits")
    write_capacity_units: Optional[int] = Field(
        default=None, alias="writeCapacityUnits"
    )
    last_update_to_pay_per_request_timestamp: Optional[datetime] = Field(
        default=None, alias="lastUpdateToPayPerRequestTimestamp"
    )


class CapacitySpecificationModel(BaseModel):
    throughput_mode: Literal["PAY_PER_REQUEST", "PROVISIONED"] = Field(
        alias="throughputMode"
    )
    read_capacity_units: Optional[int] = Field(default=None, alias="readCapacityUnits")
    write_capacity_units: Optional[int] = Field(
        default=None, alias="writeCapacityUnits"
    )


class ClusteringKeyModel(BaseModel):
    name: str = Field(alias="name")
    order_by: Literal["ASC", "DESC"] = Field(alias="orderBy")


class ColumnDefinitionModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")


class CommentModel(BaseModel):
    message: str = Field(alias="message")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EncryptionSpecificationModel(BaseModel):
    type: Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY"] = Field(alias="type")
    kms_key_identifier: Optional[str] = Field(default=None, alias="kmsKeyIdentifier")


class PointInTimeRecoveryModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")


class TimeToLiveModel(BaseModel):
    status: Literal["ENABLED"] = Field(alias="status")


class DeleteKeyspaceRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")


class DeleteTableRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")


class GetKeyspaceRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")


class GetTableRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")


class PointInTimeRecoverySummaryModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")
    earliest_restorable_timestamp: Optional[datetime] = Field(
        default=None, alias="earliestRestorableTimestamp"
    )


class KeyspaceSummaryModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    resource_arn: str = Field(alias="resourceArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListKeyspacesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTablesRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class TableSummaryModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")
    resource_arn: str = Field(alias="resourceArn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PartitionKeyModel(BaseModel):
    name: str = Field(alias="name")


class StaticColumnModel(BaseModel):
    name: str = Field(alias="name")


class CreateKeyspaceRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateKeyspaceResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTableResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyspaceResponseModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreTableResponseModel(BaseModel):
    restored_table_arn: str = Field(alias="restoredTableARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreTableRequestModel(BaseModel):
    source_keyspace_name: str = Field(alias="sourceKeyspaceName")
    source_table_name: str = Field(alias="sourceTableName")
    target_keyspace_name: str = Field(alias="targetKeyspaceName")
    target_table_name: str = Field(alias="targetTableName")
    restore_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="restoreTimestamp"
    )
    capacity_specification_override: Optional[CapacitySpecificationModel] = Field(
        default=None, alias="capacitySpecificationOverride"
    )
    encryption_specification_override: Optional[EncryptionSpecificationModel] = Field(
        default=None, alias="encryptionSpecificationOverride"
    )
    point_in_time_recovery_override: Optional[PointInTimeRecoveryModel] = Field(
        default=None, alias="pointInTimeRecoveryOverride"
    )
    tags_override: Optional[Sequence[TagModel]] = Field(
        default=None, alias="tagsOverride"
    )


class UpdateTableRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")
    add_columns: Optional[Sequence[ColumnDefinitionModel]] = Field(
        default=None, alias="addColumns"
    )
    capacity_specification: Optional[CapacitySpecificationModel] = Field(
        default=None, alias="capacitySpecification"
    )
    encryption_specification: Optional[EncryptionSpecificationModel] = Field(
        default=None, alias="encryptionSpecification"
    )
    point_in_time_recovery: Optional[PointInTimeRecoveryModel] = Field(
        default=None, alias="pointInTimeRecovery"
    )
    ttl: Optional[TimeToLiveModel] = Field(default=None, alias="ttl")
    default_time_to_live: Optional[int] = Field(default=None, alias="defaultTimeToLive")


class ListKeyspacesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    keyspaces: List[KeyspaceSummaryModel] = Field(alias="keyspaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKeyspacesRequestListKeyspacesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTablesRequestListTablesPaginateModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTablesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tables: List[TableSummaryModel] = Field(alias="tables")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SchemaDefinitionModel(BaseModel):
    all_columns: Sequence[ColumnDefinitionModel] = Field(alias="allColumns")
    partition_keys: Sequence[PartitionKeyModel] = Field(alias="partitionKeys")
    clustering_keys: Optional[Sequence[ClusteringKeyModel]] = Field(
        default=None, alias="clusteringKeys"
    )
    static_columns: Optional[Sequence[StaticColumnModel]] = Field(
        default=None, alias="staticColumns"
    )


class CreateTableRequestModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")
    schema_definition: SchemaDefinitionModel = Field(alias="schemaDefinition")
    comment: Optional[CommentModel] = Field(default=None, alias="comment")
    capacity_specification: Optional[CapacitySpecificationModel] = Field(
        default=None, alias="capacitySpecification"
    )
    encryption_specification: Optional[EncryptionSpecificationModel] = Field(
        default=None, alias="encryptionSpecification"
    )
    point_in_time_recovery: Optional[PointInTimeRecoveryModel] = Field(
        default=None, alias="pointInTimeRecovery"
    )
    ttl: Optional[TimeToLiveModel] = Field(default=None, alias="ttl")
    default_time_to_live: Optional[int] = Field(default=None, alias="defaultTimeToLive")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetTableResponseModel(BaseModel):
    keyspace_name: str = Field(alias="keyspaceName")
    table_name: str = Field(alias="tableName")
    resource_arn: str = Field(alias="resourceArn")
    creation_timestamp: datetime = Field(alias="creationTimestamp")
    status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETED",
        "DELETING",
        "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
        "RESTORING",
        "UPDATING",
    ] = Field(alias="status")
    schema_definition: SchemaDefinitionModel = Field(alias="schemaDefinition")
    capacity_specification: CapacitySpecificationSummaryModel = Field(
        alias="capacitySpecification"
    )
    encryption_specification: EncryptionSpecificationModel = Field(
        alias="encryptionSpecification"
    )
    point_in_time_recovery: PointInTimeRecoverySummaryModel = Field(
        alias="pointInTimeRecovery"
    )
    ttl: TimeToLiveModel = Field(alias="ttl")
    default_time_to_live: int = Field(alias="defaultTimeToLive")
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
