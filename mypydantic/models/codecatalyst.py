# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessTokenSummaryModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    expires_time: Optional[datetime] = Field(default=None, alias="expiresTime")


class CreateAccessTokenRequestModel(BaseModel):
    name: str = Field(alias="name")
    expires_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="expiresTime"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class IdeConfigurationModel(BaseModel):
    runtime: Optional[str] = Field(default=None, alias="runtime")
    name: Optional[str] = Field(default=None, alias="name")


class PersistentStorageConfigurationModel(BaseModel):
    size_in_gi_b: int = Field(alias="sizeInGiB")


class RepositoryInputModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: Optional[str] = Field(default=None, alias="branchName")


class CreateProjectRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    display_name: str = Field(alias="displayName")
    description: Optional[str] = Field(default=None, alias="description")


class CreateSourceRepositoryBranchRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    source_repository_name: str = Field(alias="sourceRepositoryName")
    name: str = Field(alias="name")
    head_commit_id: Optional[str] = Field(default=None, alias="headCommitId")


class DeleteAccessTokenRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")


class DevEnvironmentAccessDetailsModel(BaseModel):
    stream_url: str = Field(alias="streamUrl")
    token_value: str = Field(alias="tokenValue")


class DevEnvironmentRepositorySummaryModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: Optional[str] = Field(default=None, alias="branchName")


class ExecuteCommandSessionConfigurationModel(BaseModel):
    command: str = Field(alias="command")
    arguments: Optional[Sequence[str]] = Field(default=None, alias="arguments")


class IdeModel(BaseModel):
    runtime: Optional[str] = Field(default=None, alias="runtime")
    name: Optional[str] = Field(default=None, alias="name")


class PersistentStorageModel(BaseModel):
    size_in_gi_b: int = Field(alias="sizeInGiB")


class EmailAddressModel(BaseModel):
    email: Optional[str] = Field(default=None, alias="email")
    verified: Optional[bool] = Field(default=None, alias="verified")


class EventPayloadModel(BaseModel):
    content_type: Optional[str] = Field(default=None, alias="contentType")
    data: Optional[str] = Field(default=None, alias="data")


class ProjectInformationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    project_id: Optional[str] = Field(default=None, alias="projectId")


class UserIdentityModel(BaseModel):
    user_type: Literal["AWS_ACCOUNT", "UNKNOWN", "USER"] = Field(alias="userType")
    principal_id: str = Field(alias="principalId")
    user_name: Optional[str] = Field(default=None, alias="userName")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")


class FilterModel(BaseModel):
    key: str = Field(alias="key")
    values: Sequence[str] = Field(alias="values")
    comparison_operator: Optional[str] = Field(default=None, alias="comparisonOperator")


class GetDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")


class GetProjectRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    name: str = Field(alias="name")


class GetSourceRepositoryCloneUrlsRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    source_repository_name: str = Field(alias="sourceRepositoryName")


class GetSpaceRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetSubscriptionRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")


class GetUserDetailsRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    user_name: Optional[str] = Field(default=None, alias="userName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccessTokensRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEventLogsRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    event_name: Optional[str] = Field(default=None, alias="eventName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ProjectListFilterModel(BaseModel):
    key: Literal["hasAccessTo"] = Field(alias="key")
    values: Sequence[str] = Field(alias="values")
    comparison_operator: Optional[Literal["EQ", "GE", "GT", "LE", "LT"]] = Field(
        default=None, alias="comparisonOperator"
    )


class ProjectSummaryModel(BaseModel):
    name: str = Field(alias="name")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    description: Optional[str] = Field(default=None, alias="description")


class ListSourceRepositoriesItemModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    created_time: datetime = Field(alias="createdTime")
    description: Optional[str] = Field(default=None, alias="description")


class ListSourceRepositoriesRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListSourceRepositoryBranchesItemModel(BaseModel):
    ref: Optional[str] = Field(default=None, alias="ref")
    name: Optional[str] = Field(default=None, alias="name")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    head_commit_id: Optional[str] = Field(default=None, alias="headCommitId")


class ListSourceRepositoryBranchesRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    source_repository_name: str = Field(alias="sourceRepositoryName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListSpacesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SpaceSummaryModel(BaseModel):
    name: str = Field(alias="name")
    region_name: str = Field(alias="regionName")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    description: Optional[str] = Field(default=None, alias="description")


class StopDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")


class StopDevEnvironmentSessionRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    session_id: str = Field(alias="sessionId")


class CreateAccessTokenResponseModel(BaseModel):
    secret: str = Field(alias="secret")
    name: str = Field(alias="name")
    expires_time: datetime = Field(alias="expiresTime")
    access_token_id: str = Field(alias="accessTokenId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDevEnvironmentResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    name: str = Field(alias="name")
    display_name: str = Field(alias="displayName")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSourceRepositoryBranchResponseModel(BaseModel):
    ref: str = Field(alias="ref")
    name: str = Field(alias="name")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    head_commit_id: str = Field(alias="headCommitId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDevEnvironmentResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProjectResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    name: str = Field(alias="name")
    display_name: str = Field(alias="displayName")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSourceRepositoryCloneUrlsResponseModel(BaseModel):
    https: str = Field(alias="https")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSpaceResponseModel(BaseModel):
    name: str = Field(alias="name")
    region_name: str = Field(alias="regionName")
    display_name: str = Field(alias="displayName")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSubscriptionResponseModel(BaseModel):
    subscription_type: str = Field(alias="subscriptionType")
    aws_account_name: str = Field(alias="awsAccountName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessTokensResponseModel(BaseModel):
    items: List[AccessTokenSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDevEnvironmentResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    status: Literal[
        "DELETED",
        "DELETING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDevEnvironmentResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    status: Literal[
        "DELETED",
        "DELETING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDevEnvironmentSessionResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    session_id: str = Field(alias="sessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifySessionResponseModel(BaseModel):
    identity: str = Field(alias="identity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    ides: Optional[Sequence[IdeConfigurationModel]] = Field(default=None, alias="ides")
    instance_type: Optional[
        Literal[
            "dev.standard1.large",
            "dev.standard1.medium",
            "dev.standard1.small",
            "dev.standard1.xlarge",
        ]
    ] = Field(default=None, alias="instanceType")
    inactivity_timeout_minutes: Optional[int] = Field(
        default=None, alias="inactivityTimeoutMinutes"
    )


class UpdateDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    alias: Optional[str] = Field(default=None, alias="alias")
    ides: Optional[Sequence[IdeConfigurationModel]] = Field(default=None, alias="ides")
    instance_type: Optional[
        Literal[
            "dev.standard1.large",
            "dev.standard1.medium",
            "dev.standard1.small",
            "dev.standard1.xlarge",
        ]
    ] = Field(default=None, alias="instanceType")
    inactivity_timeout_minutes: Optional[int] = Field(
        default=None, alias="inactivityTimeoutMinutes"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateDevEnvironmentResponseModel(BaseModel):
    id: str = Field(alias="id")
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    alias: str = Field(alias="alias")
    ides: List[IdeConfigurationModel] = Field(alias="ides")
    instance_type: Literal[
        "dev.standard1.large",
        "dev.standard1.medium",
        "dev.standard1.small",
        "dev.standard1.xlarge",
    ] = Field(alias="instanceType")
    inactivity_timeout_minutes: int = Field(alias="inactivityTimeoutMinutes")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDevEnvironmentRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    instance_type: Literal[
        "dev.standard1.large",
        "dev.standard1.medium",
        "dev.standard1.small",
        "dev.standard1.xlarge",
    ] = Field(alias="instanceType")
    persistent_storage: PersistentStorageConfigurationModel = Field(
        alias="persistentStorage"
    )
    repositories: Optional[Sequence[RepositoryInputModel]] = Field(
        default=None, alias="repositories"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    alias: Optional[str] = Field(default=None, alias="alias")
    ides: Optional[Sequence[IdeConfigurationModel]] = Field(default=None, alias="ides")
    inactivity_timeout_minutes: Optional[int] = Field(
        default=None, alias="inactivityTimeoutMinutes"
    )


class StartDevEnvironmentSessionResponseModel(BaseModel):
    access_details: DevEnvironmentAccessDetailsModel = Field(alias="accessDetails")
    session_id: str = Field(alias="sessionId")
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DevEnvironmentSessionConfigurationModel(BaseModel):
    session_type: Literal["SSH", "SSM"] = Field(alias="sessionType")
    execute_command_session_configuration: Optional[
        ExecuteCommandSessionConfigurationModel
    ] = Field(default=None, alias="executeCommandSessionConfiguration")


class DevEnvironmentSummaryModel(BaseModel):
    id: str = Field(alias="id")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    creator_id: str = Field(alias="creatorId")
    status: Literal[
        "DELETED",
        "DELETING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="status")
    repositories: List[DevEnvironmentRepositorySummaryModel] = Field(
        alias="repositories"
    )
    instance_type: Literal[
        "dev.standard1.large",
        "dev.standard1.medium",
        "dev.standard1.small",
        "dev.standard1.xlarge",
    ] = Field(alias="instanceType")
    inactivity_timeout_minutes: int = Field(alias="inactivityTimeoutMinutes")
    persistent_storage: PersistentStorageModel = Field(alias="persistentStorage")
    space_name: Optional[str] = Field(default=None, alias="spaceName")
    project_name: Optional[str] = Field(default=None, alias="projectName")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    alias: Optional[str] = Field(default=None, alias="alias")
    ides: Optional[List[IdeModel]] = Field(default=None, alias="ides")


class GetDevEnvironmentResponseModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    last_updated_time: datetime = Field(alias="lastUpdatedTime")
    creator_id: str = Field(alias="creatorId")
    status: Literal[
        "DELETED",
        "DELETING",
        "FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    repositories: List[DevEnvironmentRepositorySummaryModel] = Field(
        alias="repositories"
    )
    alias: str = Field(alias="alias")
    ides: List[IdeModel] = Field(alias="ides")
    instance_type: Literal[
        "dev.standard1.large",
        "dev.standard1.medium",
        "dev.standard1.small",
        "dev.standard1.xlarge",
    ] = Field(alias="instanceType")
    inactivity_timeout_minutes: int = Field(alias="inactivityTimeoutMinutes")
    persistent_storage: PersistentStorageModel = Field(alias="persistentStorage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserDetailsResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    user_name: str = Field(alias="userName")
    display_name: str = Field(alias="displayName")
    primary_email: EmailAddressModel = Field(alias="primaryEmail")
    version: str = Field(alias="version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventLogEntryModel(BaseModel):
    id: str = Field(alias="id")
    event_name: str = Field(alias="eventName")
    event_type: str = Field(alias="eventType")
    event_category: str = Field(alias="eventCategory")
    event_source: str = Field(alias="eventSource")
    event_time: datetime = Field(alias="eventTime")
    operation_type: Literal["MUTATION", "READONLY"] = Field(alias="operationType")
    user_identity: UserIdentityModel = Field(alias="userIdentity")
    project_information: Optional[ProjectInformationModel] = Field(
        default=None, alias="projectInformation"
    )
    request_id: Optional[str] = Field(default=None, alias="requestId")
    request_payload: Optional[EventPayloadModel] = Field(
        default=None, alias="requestPayload"
    )
    response_payload: Optional[EventPayloadModel] = Field(
        default=None, alias="responsePayload"
    )
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    source_ip_address: Optional[str] = Field(default=None, alias="sourceIpAddress")
    user_agent: Optional[str] = Field(default=None, alias="userAgent")


class ListDevEnvironmentsRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAccessTokensRequestListAccessTokensPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevEnvironmentsRequestListDevEnvironmentsPaginateModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventLogsRequestListEventLogsPaginateModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    event_name: Optional[str] = Field(default=None, alias="eventName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSourceRepositoriesRequestListSourceRepositoriesPaginateModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateModel(
    BaseModel
):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    source_repository_name: str = Field(alias="sourceRepositoryName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpacesRequestListSpacesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    filters: Optional[Sequence[ProjectListFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[ProjectListFilterModel]] = Field(
        default=None, alias="filters"
    )


class ListProjectsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    items: List[ProjectSummaryModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSourceRepositoriesResponseModel(BaseModel):
    items: List[ListSourceRepositoriesItemModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSourceRepositoryBranchesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    items: List[ListSourceRepositoryBranchesItemModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSpacesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    items: List[SpaceSummaryModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDevEnvironmentSessionRequestModel(BaseModel):
    space_name: str = Field(alias="spaceName")
    project_name: str = Field(alias="projectName")
    id: str = Field(alias="id")
    session_configuration: DevEnvironmentSessionConfigurationModel = Field(
        alias="sessionConfiguration"
    )


class ListDevEnvironmentsResponseModel(BaseModel):
    items: List[DevEnvironmentSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventLogsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    items: List[EventLogEntryModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
