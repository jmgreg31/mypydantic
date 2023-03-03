# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateEnvironmentMembershipRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    user_arn: str = Field(alias="userArn")
    permissions: Literal["read-only", "read-write"] = Field(alias="permissions")


class EnvironmentMemberModel(BaseModel):
    permissions: Literal["owner", "read-only", "read-write"] = Field(
        alias="permissions"
    )
    user_id: str = Field(alias="userId")
    user_arn: str = Field(alias="userArn")
    environment_id: str = Field(alias="environmentId")
    last_access: Optional[datetime] = Field(default=None, alias="lastAccess")


class DeleteEnvironmentMembershipRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    user_arn: str = Field(alias="userArn")


class DeleteEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeEnvironmentMembershipsRequestModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="userArn")
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    permissions: Optional[
        Sequence[Literal["owner", "read-only", "read-write"]]
    ] = Field(default=None, alias="permissions")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeEnvironmentStatusRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class DescribeEnvironmentsRequestModel(BaseModel):
    environment_ids: Sequence[str] = Field(alias="environmentIds")


class EnvironmentLifecycleModel(BaseModel):
    status: Optional[
        Literal["CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
    ] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")
    failure_resource: Optional[str] = Field(default=None, alias="failureResource")


class ListEnvironmentsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateEnvironmentMembershipRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    user_arn: str = Field(alias="userArn")
    permissions: Literal["read-only", "read-write"] = Field(alias="permissions")


class UpdateEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    managed_credentials_action: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="managedCredentialsAction"
    )


class CreateEnvironmentEC2RequestModel(BaseModel):
    name: str = Field(alias="name")
    instance_type: str = Field(alias="instanceType")
    description: Optional[str] = Field(default=None, alias="description")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    image_id: Optional[str] = Field(default=None, alias="imageId")
    automatic_stop_time_minutes: Optional[int] = Field(
        default=None, alias="automaticStopTimeMinutes"
    )
    owner_arn: Optional[str] = Field(default=None, alias="ownerArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    connection_type: Optional[Literal["CONNECT_SSH", "CONNECT_SSM"]] = Field(
        default=None, alias="connectionType"
    )
    dry_run: Optional[bool] = Field(default=None, alias="dryRun")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateEnvironmentEC2ResultModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEnvironmentStatusResultModel(BaseModel):
    status: Literal[
        "connecting", "creating", "deleting", "error", "ready", "stopped", "stopping"
    ] = Field(alias="status")
    message: str = Field(alias="message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsResultModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    environment_ids: List[str] = Field(alias="environmentIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentMembershipResultModel(BaseModel):
    membership: EnvironmentMemberModel = Field(alias="membership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEnvironmentMembershipsResultModel(BaseModel):
    memberships: List[EnvironmentMemberModel] = Field(alias="memberships")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentMembershipResultModel(BaseModel):
    membership: EnvironmentMemberModel = Field(alias="membership")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateModel(
    BaseModel
):
    user_arn: Optional[str] = Field(default=None, alias="userArn")
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    permissions: Optional[
        Sequence[Literal["owner", "read-only", "read-write"]]
    ] = Field(default=None, alias="permissions")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentsRequestListEnvironmentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class EnvironmentModel(BaseModel):
    type: Literal["ec2", "ssh"] = Field(alias="type")
    arn: str = Field(alias="arn")
    owner_arn: str = Field(alias="ownerArn")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    connection_type: Optional[Literal["CONNECT_SSH", "CONNECT_SSM"]] = Field(
        default=None, alias="connectionType"
    )
    lifecycle: Optional[EnvironmentLifecycleModel] = Field(
        default=None, alias="lifecycle"
    )
    managed_credentials_status: Optional[
        Literal[
            "DISABLED_BY_COLLABORATOR",
            "DISABLED_BY_DEFAULT",
            "DISABLED_BY_OWNER",
            "ENABLED_BY_OWNER",
            "ENABLED_ON_CREATE",
            "FAILED_REMOVAL_BY_COLLABORATOR",
            "FAILED_REMOVAL_BY_OWNER",
            "PENDING_REMOVAL_BY_COLLABORATOR",
            "PENDING_REMOVAL_BY_OWNER",
            "PENDING_START_REMOVAL_BY_COLLABORATOR",
            "PENDING_START_REMOVAL_BY_OWNER",
        ]
    ] = Field(default=None, alias="managedCredentialsStatus")


class DescribeEnvironmentsResultModel(BaseModel):
    environments: List[EnvironmentModel] = Field(alias="environments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
