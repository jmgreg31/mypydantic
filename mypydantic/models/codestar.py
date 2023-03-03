# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateTeamMemberRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    user_arn: str = Field(alias="userArn")
    project_role: str = Field(alias="projectRole")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    remote_access_allowed: Optional[bool] = Field(
        default=None, alias="remoteAccessAllowed"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CodeCommitCodeDestinationModel(BaseModel):
    name: str = Field(alias="name")


class GitHubCodeDestinationModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    owner: str = Field(alias="owner")
    private_repository: bool = Field(alias="privateRepository")
    issues_enabled: bool = Field(alias="issuesEnabled")
    token: str = Field(alias="token")
    description: Optional[str] = Field(default=None, alias="description")


class S3LocationModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    bucket_key: Optional[str] = Field(default=None, alias="bucketKey")


class CreateUserProfileRequestModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    display_name: str = Field(alias="displayName")
    email_address: str = Field(alias="emailAddress")
    ssh_public_key: Optional[str] = Field(default=None, alias="sshPublicKey")


class DeleteProjectRequestModel(BaseModel):
    id: str = Field(alias="id")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    delete_stack: Optional[bool] = Field(default=None, alias="deleteStack")


class DeleteUserProfileRequestModel(BaseModel):
    user_arn: str = Field(alias="userArn")


class DescribeProjectRequestModel(BaseModel):
    id: str = Field(alias="id")


class ProjectStatusModel(BaseModel):
    state: str = Field(alias="state")
    reason: Optional[str] = Field(default=None, alias="reason")


class DescribeUserProfileRequestModel(BaseModel):
    user_arn: str = Field(alias="userArn")


class DisassociateTeamMemberRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    user_arn: str = Field(alias="userArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListProjectsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ProjectSummaryModel(BaseModel):
    project_id: Optional[str] = Field(default=None, alias="projectId")
    project_arn: Optional[str] = Field(default=None, alias="projectArn")


class ListResourcesRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ResourceModel(BaseModel):
    id: str = Field(alias="id")


class ListTagsForProjectRequestModel(BaseModel):
    id: str = Field(alias="id")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTeamMembersRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class TeamMemberModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    project_role: str = Field(alias="projectRole")
    remote_access_allowed: Optional[bool] = Field(
        default=None, alias="remoteAccessAllowed"
    )


class ListUserProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class UserProfileSummaryModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="userArn")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")
    ssh_public_key: Optional[str] = Field(default=None, alias="sshPublicKey")


class TagProjectRequestModel(BaseModel):
    id: str = Field(alias="id")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagProjectRequestModel(BaseModel):
    id: str = Field(alias="id")
    tags: Sequence[str] = Field(alias="tags")


class UpdateProjectRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateTeamMemberRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    user_arn: str = Field(alias="userArn")
    project_role: Optional[str] = Field(default=None, alias="projectRole")
    remote_access_allowed: Optional[bool] = Field(
        default=None, alias="remoteAccessAllowed"
    )


class UpdateUserProfileRequestModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")
    ssh_public_key: Optional[str] = Field(default=None, alias="sshPublicKey")


class AssociateTeamMemberResultModel(BaseModel):
    client_request_token: str = Field(alias="clientRequestToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResultModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    client_request_token: str = Field(alias="clientRequestToken")
    project_template_id: str = Field(alias="projectTemplateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserProfileResultModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    display_name: str = Field(alias="displayName")
    email_address: str = Field(alias="emailAddress")
    ssh_public_key: str = Field(alias="sshPublicKey")
    created_timestamp: datetime = Field(alias="createdTimestamp")
    last_modified_timestamp: datetime = Field(alias="lastModifiedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectResultModel(BaseModel):
    stack_id: str = Field(alias="stackId")
    project_arn: str = Field(alias="projectArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteUserProfileResultModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserProfileResultModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    display_name: str = Field(alias="displayName")
    email_address: str = Field(alias="emailAddress")
    ssh_public_key: str = Field(alias="sshPublicKey")
    created_timestamp: datetime = Field(alias="createdTimestamp")
    last_modified_timestamp: datetime = Field(alias="lastModifiedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForProjectResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagProjectResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTeamMemberResultModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    project_role: str = Field(alias="projectRole")
    remote_access_allowed: bool = Field(alias="remoteAccessAllowed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserProfileResultModel(BaseModel):
    user_arn: str = Field(alias="userArn")
    display_name: str = Field(alias="displayName")
    email_address: str = Field(alias="emailAddress")
    ssh_public_key: str = Field(alias="sshPublicKey")
    created_timestamp: datetime = Field(alias="createdTimestamp")
    last_modified_timestamp: datetime = Field(alias="lastModifiedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CodeDestinationModel(BaseModel):
    code_commit: Optional[CodeCommitCodeDestinationModel] = Field(
        default=None, alias="codeCommit"
    )
    git_hub: Optional[GitHubCodeDestinationModel] = Field(default=None, alias="gitHub")


class CodeSourceModel(BaseModel):
    s3: S3LocationModel = Field(alias="s3")


class ToolchainSourceModel(BaseModel):
    s3: S3LocationModel = Field(alias="s3")


class DescribeProjectResultModel(BaseModel):
    name: str = Field(alias="name")
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    client_request_token: str = Field(alias="clientRequestToken")
    created_time_stamp: datetime = Field(alias="createdTimeStamp")
    stack_id: str = Field(alias="stackId")
    project_template_id: str = Field(alias="projectTemplateId")
    status: ProjectStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcesRequestListResourcesPaginateModel(BaseModel):
    project_id: str = Field(alias="projectId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTeamMembersRequestListTeamMembersPaginateModel(BaseModel):
    project_id: str = Field(alias="projectId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserProfilesRequestListUserProfilesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsResultModel(BaseModel):
    projects: List[ProjectSummaryModel] = Field(alias="projects")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesResultModel(BaseModel):
    resources: List[ResourceModel] = Field(alias="resources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTeamMembersResultModel(BaseModel):
    team_members: List[TeamMemberModel] = Field(alias="teamMembers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserProfilesResultModel(BaseModel):
    user_profiles: List[UserProfileSummaryModel] = Field(alias="userProfiles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CodeModel(BaseModel):
    source: CodeSourceModel = Field(alias="source")
    destination: CodeDestinationModel = Field(alias="destination")


class ToolchainModel(BaseModel):
    source: ToolchainSourceModel = Field(alias="source")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    stack_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="stackParameters"
    )


class CreateProjectRequestModel(BaseModel):
    name: str = Field(alias="name")
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    source_code: Optional[Sequence[CodeModel]] = Field(default=None, alias="sourceCode")
    toolchain: Optional[ToolchainModel] = Field(default=None, alias="toolchain")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
