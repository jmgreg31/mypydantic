# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlertManagerDefinitionStatusModel(BaseModel):
    status_code: Literal[
        "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="statusCode")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class CreateAlertManagerDefinitionRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="data")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLoggingConfigurationRequestModel(BaseModel):
    log_group_arn: str = Field(alias="logGroupArn")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class LoggingConfigurationStatusModel(BaseModel):
    status_code: Literal[
        "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="statusCode")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class CreateRuleGroupsNamespaceRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="data")
    name: str = Field(alias="name")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class RuleGroupsNamespaceStatusModel(BaseModel):
    status_code: Literal[
        "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
    ] = Field(alias="statusCode")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class CreateWorkspaceRequestModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="alias")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class WorkspaceStatusModel(BaseModel):
    status_code: Literal[
        "ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATING"
    ] = Field(alias="statusCode")


class DeleteAlertManagerDefinitionRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteLoggingConfigurationRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteRuleGroupsNamespaceRequestModel(BaseModel):
    name: str = Field(alias="name")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DescribeAlertManagerDefinitionRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DescribeLoggingConfigurationRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class DescribeRuleGroupsNamespaceRequestModel(BaseModel):
    name: str = Field(alias="name")
    workspace_id: str = Field(alias="workspaceId")


class DescribeWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRuleGroupsNamespacesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListWorkspacesRequestModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="alias")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PutAlertManagerDefinitionRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="data")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class PutRuleGroupsNamespaceRequestModel(BaseModel):
    data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="data")
    name: str = Field(alias="name")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateLoggingConfigurationRequestModel(BaseModel):
    log_group_arn: str = Field(alias="logGroupArn")
    workspace_id: str = Field(alias="workspaceId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateWorkspaceAliasRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    alias: Optional[str] = Field(default=None, alias="alias")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AlertManagerDefinitionDescriptionModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    data: bytes = Field(alias="data")
    modified_at: datetime = Field(alias="modifiedAt")
    status: AlertManagerDefinitionStatusModel = Field(alias="status")


class CreateAlertManagerDefinitionResponseModel(BaseModel):
    status: AlertManagerDefinitionStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAlertManagerDefinitionResponseModel(BaseModel):
    status: AlertManagerDefinitionStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggingConfigurationResponseModel(BaseModel):
    status: LoggingConfigurationStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingConfigurationMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    log_group_arn: str = Field(alias="logGroupArn")
    modified_at: datetime = Field(alias="modifiedAt")
    status: LoggingConfigurationStatusModel = Field(alias="status")
    workspace: str = Field(alias="workspace")


class UpdateLoggingConfigurationResponseModel(BaseModel):
    status: LoggingConfigurationStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleGroupsNamespaceResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    status: RuleGroupsNamespaceStatusModel = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRuleGroupsNamespaceResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    status: RuleGroupsNamespaceStatusModel = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleGroupsNamespaceDescriptionModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    data: bytes = Field(alias="data")
    modified_at: datetime = Field(alias="modifiedAt")
    name: str = Field(alias="name")
    status: RuleGroupsNamespaceStatusModel = Field(alias="status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class RuleGroupsNamespaceSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    modified_at: datetime = Field(alias="modifiedAt")
    name: str = Field(alias="name")
    status: RuleGroupsNamespaceStatusModel = Field(alias="status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateWorkspaceResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    status: WorkspaceStatusModel = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    workspace_id: str = Field(alias="workspaceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class WorkspaceDescriptionModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    status: WorkspaceStatusModel = Field(alias="status")
    workspace_id: str = Field(alias="workspaceId")
    alias: Optional[str] = Field(default=None, alias="alias")
    prometheus_endpoint: Optional[str] = Field(default=None, alias="prometheusEndpoint")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class WorkspaceSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    status: WorkspaceStatusModel = Field(alias="status")
    workspace_id: str = Field(alias="workspaceId")
    alias: Optional[str] = Field(default=None, alias="alias")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DescribeWorkspaceRequestWorkspaceActiveWaitModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeWorkspaceRequestWorkspaceDeletedWaitModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListRuleGroupsNamespacesRequestListRuleGroupsNamespacesPaginateModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    name: Optional[str] = Field(default=None, alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkspacesRequestListWorkspacesPaginateModel(BaseModel):
    alias: Optional[str] = Field(default=None, alias="alias")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAlertManagerDefinitionResponseModel(BaseModel):
    alert_manager_definition: AlertManagerDefinitionDescriptionModel = Field(
        alias="alertManagerDefinition"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationMetadataModel = Field(
        alias="loggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRuleGroupsNamespaceResponseModel(BaseModel):
    rule_groups_namespace: RuleGroupsNamespaceDescriptionModel = Field(
        alias="ruleGroupsNamespace"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRuleGroupsNamespacesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    rule_groups_namespaces: List[RuleGroupsNamespaceSummaryModel] = Field(
        alias="ruleGroupsNamespaces"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWorkspaceResponseModel(BaseModel):
    workspace: WorkspaceDescriptionModel = Field(alias="workspace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkspacesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    workspaces: List[WorkspaceSummaryModel] = Field(alias="workspaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
