# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationCredentialModel(BaseModel):
    database_name: str = Field(alias="DatabaseName")
    credential_type: Literal["ADMIN"] = Field(alias="CredentialType")
    secret_id: str = Field(alias="SecretId")


class ApplicationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["HANA"]] = Field(default=None, alias="Type")
    arn: Optional[str] = Field(default=None, alias="Arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ApplicationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["HANA"]] = Field(default=None, alias="Type")
    arn: Optional[str] = Field(default=None, alias="Arn")
    app_registry_arn: Optional[str] = Field(default=None, alias="AppRegistryArn")
    status: Optional[
        Literal[
            "ACTIVATED",
            "DELETING",
            "FAILED",
            "REGISTERING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "UNKNOWN",
        ]
    ] = Field(default=None, alias="Status")
    components: Optional[List[str]] = Field(default=None, alias="Components")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ComponentSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    component_type: Optional[Literal["HANA"]] = Field(
        default=None, alias="ComponentType"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class HostModel(BaseModel):
    host_name: Optional[str] = Field(default=None, alias="HostName")
    host_role: Optional[Literal["LEADER", "STANDBY", "UNKNOWN", "WORKER"]] = Field(
        default=None, alias="HostRole"
    )
    host_ip: Optional[str] = Field(default=None, alias="HostIp")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class DatabaseSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_type: Optional[Literal["SYSTEM", "TENANT"]] = Field(
        default=None, alias="DatabaseType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DeleteResourcePermissionInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    action_type: Optional[Literal["RESTORE"]] = Field(default=None, alias="ActionType")
    source_resource_arn: Optional[str] = Field(default=None, alias="SourceResourceArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeregisterApplicationInputRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class FilterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")
    operator: Literal["Equals", "GreaterThanOrEquals", "LessThanOrEquals"] = Field(
        alias="Operator"
    )


class GetApplicationInputRequestModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")
    app_registry_arn: Optional[str] = Field(default=None, alias="AppRegistryArn")


class GetComponentInputRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    component_id: str = Field(alias="ComponentId")


class GetDatabaseInputRequestModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_arn: Optional[str] = Field(default=None, alias="DatabaseArn")


class GetOperationInputRequestModel(BaseModel):
    operation_id: str = Field(alias="OperationId")


class OperationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[str] = Field(default=None, alias="Type")
    status: Optional[Literal["ERROR", "INPROGRESS", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    properties: Optional[Dict[str, str]] = Field(default=None, alias="Properties")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class GetResourcePermissionInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    action_type: Optional[Literal["RESTORE"]] = Field(default=None, alias="ActionType")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListComponentsInputRequestModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDatabasesInputRequestModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PutResourcePermissionInputRequestModel(BaseModel):
    action_type: Literal["RESTORE"] = Field(alias="ActionType")
    source_resource_arn: str = Field(alias="SourceResourceArn")
    resource_arn: str = Field(alias="ResourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class DatabaseModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    credentials: Optional[List[ApplicationCredentialModel]] = Field(
        default=None, alias="Credentials"
    )
    database_id: Optional[str] = Field(default=None, alias="DatabaseId")
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    database_type: Optional[Literal["SYSTEM", "TENANT"]] = Field(
        default=None, alias="DatabaseType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    status: Optional[
        Literal["RUNNING", "STARTING", "STOPPED", "UNKNOWN", "WARNING"]
    ] = Field(default=None, alias="Status")
    primary_host: Optional[str] = Field(default=None, alias="PrimaryHost")
    s_ql_port: Optional[int] = Field(default=None, alias="SQLPort")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")


class RegisterApplicationInputRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    application_type: Literal["HANA"] = Field(alias="ApplicationType")
    instances: Sequence[str] = Field(alias="Instances")
    credentials: Sequence[ApplicationCredentialModel] = Field(alias="Credentials")
    sap_instance_number: Optional[str] = Field(default=None, alias="SapInstanceNumber")
    sid: Optional[str] = Field(default=None, alias="Sid")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateApplicationSettingsInputRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    credentials_to_add_or_update: Optional[
        Sequence[ApplicationCredentialModel]
    ] = Field(default=None, alias="CredentialsToAddOrUpdate")
    credentials_to_remove: Optional[Sequence[ApplicationCredentialModel]] = Field(
        default=None, alias="CredentialsToRemove"
    )


class ComponentModel(BaseModel):
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_type: Optional[Literal["HANA"]] = Field(
        default=None, alias="ComponentType"
    )
    status: Optional[Literal["ACTIVATED"]] = Field(default=None, alias="Status")
    databases: Optional[List[str]] = Field(default=None, alias="Databases")
    hosts: Optional[List[HostModel]] = Field(default=None, alias="Hosts")
    primary_host: Optional[str] = Field(default=None, alias="PrimaryHost")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")


class DeleteResourcePermissionOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationOutputModel(BaseModel):
    application: ApplicationModel = Field(alias="Application")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePermissionOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsOutputModel(BaseModel):
    applications: List[ApplicationSummaryModel] = Field(alias="Applications")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComponentsOutputModel(BaseModel):
    components: List[ComponentSummaryModel] = Field(alias="Components")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatabasesOutputModel(BaseModel):
    databases: List[DatabaseSummaryModel] = Field(alias="Databases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePermissionOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterApplicationOutputModel(BaseModel):
    application: ApplicationModel = Field(alias="Application")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationSettingsOutputModel(BaseModel):
    message: str = Field(alias="Message")
    operation_ids: List[str] = Field(alias="OperationIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOperationsInputRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class GetOperationOutputModel(BaseModel):
    operation: OperationModel = Field(alias="Operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOperationsOutputModel(BaseModel):
    operations: List[OperationModel] = Field(alias="Operations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsInputListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentsInputListComponentsPaginateModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatabasesInputListDatabasesPaginateModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOperationsInputListOperationsPaginateModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDatabaseOutputModel(BaseModel):
    database: DatabaseModel = Field(alias="Database")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentOutputModel(BaseModel):
    component: ComponentModel = Field(alias="Component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
