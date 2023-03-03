# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountSettingsModel(BaseModel):
    group_lifecycle_events_desired_status: Optional[
        Literal["ACTIVE", "INACTIVE"]
    ] = Field(default=None, alias="GroupLifecycleEventsDesiredStatus")
    group_lifecycle_events_status: Optional[
        Literal["ACTIVE", "ERROR", "INACTIVE", "IN_PROGRESS"]
    ] = Field(default=None, alias="GroupLifecycleEventsStatus")
    group_lifecycle_events_status_message: Optional[str] = Field(
        default=None, alias="GroupLifecycleEventsStatusMessage"
    )


class ResourceQueryModel(BaseModel):
    type: Literal["CLOUDFORMATION_STACK_1_0", "TAG_FILTERS_1_0"] = Field(alias="Type")
    query: str = Field(alias="Query")


class GroupModel(BaseModel):
    group_arn: str = Field(alias="GroupArn")
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteGroupInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")


class FailedResourceModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")


class GetGroupConfigurationInputRequestModel(BaseModel):
    group: Optional[str] = Field(default=None, alias="Group")


class GetGroupInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")


class GetGroupQueryInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")


class GetTagsInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GroupConfigurationParameterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class GroupFilterModel(BaseModel):
    name: Literal["configuration-type", "resource-type"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class GroupIdentifierModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_arn: Optional[str] = Field(default=None, alias="GroupArn")


class GroupResourcesInputRequestModel(BaseModel):
    group: str = Field(alias="Group")
    resource_arns: Sequence[str] = Field(alias="ResourceArns")


class PendingResourceModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ResourceFilterModel(BaseModel):
    name: Literal["resource-type"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class ResourceIdentifierModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class ResourceStatusModel(BaseModel):
    name: Optional[Literal["PENDING"]] = Field(default=None, alias="Name")


class QueryErrorModel(BaseModel):
    error_code: Optional[
        Literal[
            "CLOUDFORMATION_STACK_INACTIVE",
            "CLOUDFORMATION_STACK_NOT_EXISTING",
            "CLOUDFORMATION_STACK_UNASSUMABLE_ROLE",
        ]
    ] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class TagInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UngroupResourcesInputRequestModel(BaseModel):
    group: str = Field(alias="Group")
    resource_arns: Sequence[str] = Field(alias="ResourceArns")


class UntagInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    keys: Sequence[str] = Field(alias="Keys")


class UpdateAccountSettingsInputRequestModel(BaseModel):
    group_lifecycle_events_desired_status: Optional[
        Literal["ACTIVE", "INACTIVE"]
    ] = Field(default=None, alias="GroupLifecycleEventsDesiredStatus")


class UpdateGroupInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")
    description: Optional[str] = Field(default=None, alias="Description")


class GroupQueryModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    resource_query: ResourceQueryModel = Field(alias="ResourceQuery")


class SearchResourcesInputRequestModel(BaseModel):
    resource_query: ResourceQueryModel = Field(alias="ResourceQuery")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateGroupQueryInputRequestModel(BaseModel):
    resource_query: ResourceQueryModel = Field(alias="ResourceQuery")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")


class DeleteGroupOutputModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSettingsOutputModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="AccountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupOutputModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagsOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    keys: List[str] = Field(alias="Keys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountSettingsOutputModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="AccountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupOutputModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GroupConfigurationItemModel(BaseModel):
    type: str = Field(alias="Type")
    parameters: Optional[Sequence[GroupConfigurationParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class ListGroupsInputRequestModel(BaseModel):
    filters: Optional[Sequence[GroupFilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGroupsOutputModel(BaseModel):
    group_identifiers: List[GroupIdentifierModel] = Field(alias="GroupIdentifiers")
    groups: List[GroupModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GroupResourcesOutputModel(BaseModel):
    succeeded: List[str] = Field(alias="Succeeded")
    failed: List[FailedResourceModel] = Field(alias="Failed")
    pending: List[PendingResourceModel] = Field(alias="Pending")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UngroupResourcesOutputModel(BaseModel):
    succeeded: List[str] = Field(alias="Succeeded")
    failed: List[FailedResourceModel] = Field(alias="Failed")
    pending: List[PendingResourceModel] = Field(alias="Pending")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsInputListGroupsPaginateModel(BaseModel):
    filters: Optional[Sequence[GroupFilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchResourcesInputSearchResourcesPaginateModel(BaseModel):
    resource_query: ResourceQueryModel = Field(alias="ResourceQuery")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupResourcesInputListGroupResourcesPaginateModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")
    filters: Optional[Sequence[ResourceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupResourcesInputRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group: Optional[str] = Field(default=None, alias="Group")
    filters: Optional[Sequence[ResourceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGroupResourcesItemModel(BaseModel):
    identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="Identifier"
    )
    status: Optional[ResourceStatusModel] = Field(default=None, alias="Status")


class SearchResourcesOutputModel(BaseModel):
    resource_identifiers: List[ResourceIdentifierModel] = Field(
        alias="ResourceIdentifiers"
    )
    next_token: str = Field(alias="NextToken")
    query_errors: List[QueryErrorModel] = Field(alias="QueryErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupQueryOutputModel(BaseModel):
    group_query: GroupQueryModel = Field(alias="GroupQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupQueryOutputModel(BaseModel):
    group_query: GroupQueryModel = Field(alias="GroupQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    resource_query: Optional[ResourceQueryModel] = Field(
        default=None, alias="ResourceQuery"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    configuration: Optional[Sequence[GroupConfigurationItemModel]] = Field(
        default=None, alias="Configuration"
    )


class GroupConfigurationModel(BaseModel):
    configuration: Optional[List[GroupConfigurationItemModel]] = Field(
        default=None, alias="Configuration"
    )
    proposed_configuration: Optional[List[GroupConfigurationItemModel]] = Field(
        default=None, alias="ProposedConfiguration"
    )
    status: Optional[Literal["UPDATE_COMPLETE", "UPDATE_FAILED", "UPDATING"]] = Field(
        default=None, alias="Status"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class PutGroupConfigurationInputRequestModel(BaseModel):
    group: Optional[str] = Field(default=None, alias="Group")
    configuration: Optional[Sequence[GroupConfigurationItemModel]] = Field(
        default=None, alias="Configuration"
    )


class ListGroupResourcesOutputModel(BaseModel):
    resources: List[ListGroupResourcesItemModel] = Field(alias="Resources")
    resource_identifiers: List[ResourceIdentifierModel] = Field(
        alias="ResourceIdentifiers"
    )
    next_token: str = Field(alias="NextToken")
    query_errors: List[QueryErrorModel] = Field(alias="QueryErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupOutputModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    resource_query: ResourceQueryModel = Field(alias="ResourceQuery")
    tags: Dict[str, str] = Field(alias="Tags")
    group_configuration: GroupConfigurationModel = Field(alias="GroupConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupConfigurationOutputModel(BaseModel):
    group_configuration: GroupConfigurationModel = Field(alias="GroupConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
