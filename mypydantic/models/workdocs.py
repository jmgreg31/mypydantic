# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AbortDocumentVersionUploadRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class ActivateUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UserMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    username: Optional[str] = Field(default=None, alias="Username")
    given_name: Optional[str] = Field(default=None, alias="GivenName")
    surname: Optional[str] = Field(default=None, alias="Surname")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")


class NotificationOptionsModel(BaseModel):
    send_email: Optional[bool] = Field(default=None, alias="SendEmail")
    email_message: Optional[str] = Field(default=None, alias="EmailMessage")


class SharePrincipalModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"] = Field(
        alias="Type"
    )
    role: Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"] = Field(alias="Role")


class ShareResultModel(BaseModel):
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    invitee_principal_id: Optional[str] = Field(
        default=None, alias="InviteePrincipalId"
    )
    role: Optional[Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]] = Field(
        default=None, alias="Role"
    )
    status: Optional[Literal["FAILURE", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    share_id: Optional[str] = Field(default=None, alias="ShareId")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class CreateCommentRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    text: str = Field(alias="Text")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    parent_id: Optional[str] = Field(default=None, alias="ParentId")
    thread_id: Optional[str] = Field(default=None, alias="ThreadId")
    visibility: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Visibility"
    )
    notify_collaborators: Optional[bool] = Field(
        default=None, alias="NotifyCollaborators"
    )


class CreateCustomMetadataRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    custom_metadata: Mapping[str, str] = Field(alias="CustomMetadata")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class CreateFolderRequestModel(BaseModel):
    parent_folder_id: str = Field(alias="ParentFolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class FolderMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    creator_id: Optional[str] = Field(default=None, alias="CreatorId")
    parent_folder_id: Optional[str] = Field(default=None, alias="ParentFolderId")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    modified_timestamp: Optional[datetime] = Field(
        default=None, alias="ModifiedTimestamp"
    )
    resource_state: Optional[
        Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
    ] = Field(default=None, alias="ResourceState")
    signature: Optional[str] = Field(default=None, alias="Signature")
    labels: Optional[List[str]] = Field(default=None, alias="Labels")
    size: Optional[int] = Field(default=None, alias="Size")
    latest_version_size: Optional[int] = Field(default=None, alias="LatestVersionSize")


class CreateLabelsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    labels: Sequence[str] = Field(alias="Labels")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class CreateNotificationSubscriptionRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    endpoint: str = Field(alias="Endpoint")
    protocol: Literal["HTTPS", "SQS"] = Field(alias="Protocol")
    subscription_type: Literal["ALL"] = Field(alias="SubscriptionType")


class SubscriptionModel(BaseModel):
    subscription_id: Optional[str] = Field(default=None, alias="SubscriptionId")
    end_point: Optional[str] = Field(default=None, alias="EndPoint")
    protocol: Optional[Literal["HTTPS", "SQS"]] = Field(default=None, alias="Protocol")


class StorageRuleTypeModel(BaseModel):
    storage_allocated_in_bytes: Optional[int] = Field(
        default=None, alias="StorageAllocatedInBytes"
    )
    storage_type: Optional[Literal["QUOTA", "UNLIMITED"]] = Field(
        default=None, alias="StorageType"
    )


class DeactivateUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteCommentRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    comment_id: str = Field(alias="CommentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteCustomMetadataRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    keys: Optional[Sequence[str]] = Field(default=None, alias="Keys")
    delete_all: Optional[bool] = Field(default=None, alias="DeleteAll")


class DeleteDocumentRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteDocumentVersionRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    delete_prior_versions: bool = Field(alias="DeletePriorVersions")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteFolderContentsRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteFolderRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class DeleteLabelsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    labels: Optional[Sequence[str]] = Field(default=None, alias="Labels")
    delete_all: Optional[bool] = Field(default=None, alias="DeleteAll")


class DeleteNotificationSubscriptionRequestModel(BaseModel):
    subscription_id: str = Field(alias="SubscriptionId")
    organization_id: str = Field(alias="OrganizationId")


class DeleteUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeActivitiesRequestModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    activity_types: Optional[str] = Field(default=None, alias="ActivityTypes")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    include_indirect_activities: Optional[bool] = Field(
        default=None, alias="IncludeIndirectActivities"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeCommentsRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeDocumentVersionsRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")
    include: Optional[str] = Field(default=None, alias="Include")
    fields: Optional[str] = Field(default=None, alias="Fields")


class DocumentVersionMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    size: Optional[int] = Field(default=None, alias="Size")
    signature: Optional[str] = Field(default=None, alias="Signature")
    status: Optional[Literal["ACTIVE", "INITIALIZED"]] = Field(
        default=None, alias="Status"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    modified_timestamp: Optional[datetime] = Field(
        default=None, alias="ModifiedTimestamp"
    )
    content_created_timestamp: Optional[datetime] = Field(
        default=None, alias="ContentCreatedTimestamp"
    )
    content_modified_timestamp: Optional[datetime] = Field(
        default=None, alias="ContentModifiedTimestamp"
    )
    creator_id: Optional[str] = Field(default=None, alias="CreatorId")
    thumbnail: Optional[Dict[Literal["LARGE", "SMALL", "SMALL_HQ"], str]] = Field(
        default=None, alias="Thumbnail"
    )
    source: Optional[Dict[Literal["ORIGINAL", "WITH_COMMENTS"], str]] = Field(
        default=None, alias="Source"
    )


class DescribeFolderContentsRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    sort: Optional[Literal["DATE", "NAME"]] = Field(default=None, alias="Sort")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")
    type: Optional[Literal["ALL", "DOCUMENT", "FOLDER"]] = Field(
        default=None, alias="Type"
    )
    include: Optional[str] = Field(default=None, alias="Include")


class DescribeGroupsRequestModel(BaseModel):
    search_query: str = Field(alias="SearchQuery")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class GroupMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class DescribeNotificationSubscriptionsRequestModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeResourcePermissionsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeRootFoldersRequestModel(BaseModel):
    authentication_token: str = Field(alias="AuthenticationToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeUsersRequestModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    user_ids: Optional[str] = Field(default=None, alias="UserIds")
    query: Optional[str] = Field(default=None, alias="Query")
    include: Optional[Literal["ACTIVE_PENDING", "ALL"]] = Field(
        default=None, alias="Include"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    sort: Optional[
        Literal[
            "FULL_NAME", "STORAGE_LIMIT", "STORAGE_USED", "USER_NAME", "USER_STATUS"
        ]
    ] = Field(default=None, alias="Sort")
    marker: Optional[str] = Field(default=None, alias="Marker")
    limit: Optional[int] = Field(default=None, alias="Limit")
    fields: Optional[str] = Field(default=None, alias="Fields")


class GetCurrentUserRequestModel(BaseModel):
    authentication_token: str = Field(alias="AuthenticationToken")


class GetDocumentPathRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    fields: Optional[str] = Field(default=None, alias="Fields")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GetDocumentRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    include_custom_metadata: Optional[bool] = Field(
        default=None, alias="IncludeCustomMetadata"
    )


class GetDocumentVersionRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    fields: Optional[str] = Field(default=None, alias="Fields")
    include_custom_metadata: Optional[bool] = Field(
        default=None, alias="IncludeCustomMetadata"
    )


class GetFolderPathRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    fields: Optional[str] = Field(default=None, alias="Fields")
    marker: Optional[str] = Field(default=None, alias="Marker")


class GetFolderRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    include_custom_metadata: Optional[bool] = Field(
        default=None, alias="IncludeCustomMetadata"
    )


class GetResourcesRequestModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    user_id: Optional[str] = Field(default=None, alias="UserId")
    collection_type: Optional[Literal["SHARED_WITH_ME"]] = Field(
        default=None, alias="CollectionType"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class InitiateDocumentVersionUploadRequestModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    content_created_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="ContentCreatedTimestamp"
    )
    content_modified_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="ContentModifiedTimestamp"
    )
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    document_size_in_bytes: Optional[int] = Field(
        default=None, alias="DocumentSizeInBytes"
    )
    parent_folder_id: Optional[str] = Field(default=None, alias="ParentFolderId")


class UploadMetadataModel(BaseModel):
    upload_url: Optional[str] = Field(default=None, alias="UploadUrl")
    signed_headers: Optional[Dict[str, str]] = Field(
        default=None, alias="SignedHeaders"
    )


class PermissionInfoModel(BaseModel):
    role: Optional[Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]] = Field(
        default=None, alias="Role"
    )
    type: Optional[Literal["DIRECT", "INHERITED"]] = Field(default=None, alias="Type")


class RemoveAllResourcePermissionsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class RemoveResourcePermissionRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    principal_id: str = Field(alias="PrincipalId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    principal_type: Optional[
        Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"]
    ] = Field(default=None, alias="PrincipalType")


class ResourcePathComponentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class RestoreDocumentVersionsRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class UpdateDocumentRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    parent_folder_id: Optional[str] = Field(default=None, alias="ParentFolderId")
    resource_state: Optional[
        Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
    ] = Field(default=None, alias="ResourceState")


class UpdateDocumentVersionRequestModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    version_status: Optional[Literal["ACTIVE"]] = Field(
        default=None, alias="VersionStatus"
    )


class UpdateFolderRequestModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    parent_folder_id: Optional[str] = Field(default=None, alias="ParentFolderId")
    resource_state: Optional[
        Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
    ] = Field(default=None, alias="ResourceState")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceMetadataModel(BaseModel):
    type: Optional[Literal["DOCUMENT", "FOLDER"]] = Field(default=None, alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    original_name: Optional[str] = Field(default=None, alias="OriginalName")
    id: Optional[str] = Field(default=None, alias="Id")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    owner: Optional[UserMetadataModel] = Field(default=None, alias="Owner")
    parent_id: Optional[str] = Field(default=None, alias="ParentId")


class AddResourcePermissionsRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    principals: Sequence[SharePrincipalModel] = Field(alias="Principals")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    notification_options: Optional[NotificationOptionsModel] = Field(
        default=None, alias="NotificationOptions"
    )


class AddResourcePermissionsResponseModel(BaseModel):
    share_results: List[ShareResultModel] = Field(alias="ShareResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFolderResponseModel(BaseModel):
    metadata: FolderMetadataModel = Field(alias="Metadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRootFoldersResponseModel(BaseModel):
    folders: List[FolderMetadataModel] = Field(alias="Folders")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFolderResponseModel(BaseModel):
    metadata: FolderMetadataModel = Field(alias="Metadata")
    custom_metadata: Dict[str, str] = Field(alias="CustomMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNotificationSubscriptionResponseModel(BaseModel):
    subscription: SubscriptionModel = Field(alias="Subscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNotificationSubscriptionsResponseModel(BaseModel):
    subscriptions: List[SubscriptionModel] = Field(alias="Subscriptions")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserRequestModel(BaseModel):
    username: str = Field(alias="Username")
    given_name: str = Field(alias="GivenName")
    surname: str = Field(alias="Surname")
    password: str = Field(alias="Password")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    time_zone_id: Optional[str] = Field(default=None, alias="TimeZoneId")
    storage_rule: Optional[StorageRuleTypeModel] = Field(
        default=None, alias="StorageRule"
    )
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )


class UpdateUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    given_name: Optional[str] = Field(default=None, alias="GivenName")
    surname: Optional[str] = Field(default=None, alias="Surname")
    type: Optional[
        Literal["ADMIN", "MINIMALUSER", "POWERUSER", "USER", "WORKSPACESUSER"]
    ] = Field(default=None, alias="Type")
    storage_rule: Optional[StorageRuleTypeModel] = Field(
        default=None, alias="StorageRule"
    )
    time_zone_id: Optional[str] = Field(default=None, alias="TimeZoneId")
    locale: Optional[
        Literal[
            "de",
            "default",
            "en",
            "es",
            "fr",
            "ja",
            "ko",
            "pt_BR",
            "ru",
            "zh_CN",
            "zh_TW",
        ]
    ] = Field(default=None, alias="Locale")
    grant_poweruser_privileges: Optional[Literal["FALSE", "TRUE"]] = Field(
        default=None, alias="GrantPoweruserPrivileges"
    )


class UserStorageMetadataModel(BaseModel):
    storage_utilized_in_bytes: Optional[int] = Field(
        default=None, alias="StorageUtilizedInBytes"
    )
    storage_rule: Optional[StorageRuleTypeModel] = Field(
        default=None, alias="StorageRule"
    )


class DescribeActivitiesRequestDescribeActivitiesPaginateModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    activity_types: Optional[str] = Field(default=None, alias="ActivityTypes")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    include_indirect_activities: Optional[bool] = Field(
        default=None, alias="IncludeIndirectActivities"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCommentsRequestDescribeCommentsPaginateModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    version_id: str = Field(alias="VersionId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    include: Optional[str] = Field(default=None, alias="Include")
    fields: Optional[str] = Field(default=None, alias="Fields")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFolderContentsRequestDescribeFolderContentsPaginateModel(BaseModel):
    folder_id: str = Field(alias="FolderId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    sort: Optional[Literal["DATE", "NAME"]] = Field(default=None, alias="Sort")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    type: Optional[Literal["ALL", "DOCUMENT", "FOLDER"]] = Field(
        default=None, alias="Type"
    )
    include: Optional[str] = Field(default=None, alias="Include")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGroupsRequestDescribeGroupsPaginateModel(BaseModel):
    search_query: str = Field(alias="SearchQuery")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeNotificationSubscriptionsRequestDescribeNotificationSubscriptionsPaginateModel(
    BaseModel
):
    organization_id: str = Field(alias="OrganizationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateModel(
    BaseModel
):
    resource_id: str = Field(alias="ResourceId")
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRootFoldersRequestDescribeRootFoldersPaginateModel(BaseModel):
    authentication_token: str = Field(alias="AuthenticationToken")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUsersRequestDescribeUsersPaginateModel(BaseModel):
    authentication_token: Optional[str] = Field(
        default=None, alias="AuthenticationToken"
    )
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    user_ids: Optional[str] = Field(default=None, alias="UserIds")
    query: Optional[str] = Field(default=None, alias="Query")
    include: Optional[Literal["ACTIVE_PENDING", "ALL"]] = Field(
        default=None, alias="Include"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    sort: Optional[
        Literal[
            "FULL_NAME", "STORAGE_LIMIT", "STORAGE_USED", "USER_NAME", "USER_STATUS"
        ]
    ] = Field(default=None, alias="Sort")
    fields: Optional[str] = Field(default=None, alias="Fields")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeDocumentVersionsResponseModel(BaseModel):
    document_versions: List[DocumentVersionMetadataModel] = Field(
        alias="DocumentVersions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    creator_id: Optional[str] = Field(default=None, alias="CreatorId")
    parent_folder_id: Optional[str] = Field(default=None, alias="ParentFolderId")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    modified_timestamp: Optional[datetime] = Field(
        default=None, alias="ModifiedTimestamp"
    )
    latest_version_metadata: Optional[DocumentVersionMetadataModel] = Field(
        default=None, alias="LatestVersionMetadata"
    )
    resource_state: Optional[
        Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
    ] = Field(default=None, alias="ResourceState")
    labels: Optional[List[str]] = Field(default=None, alias="Labels")


class GetDocumentVersionResponseModel(BaseModel):
    metadata: DocumentVersionMetadataModel = Field(alias="Metadata")
    custom_metadata: Dict[str, str] = Field(alias="CustomMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupsResponseModel(BaseModel):
    groups: List[GroupMetadataModel] = Field(alias="Groups")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParticipantsModel(BaseModel):
    users: Optional[List[UserMetadataModel]] = Field(default=None, alias="Users")
    groups: Optional[List[GroupMetadataModel]] = Field(default=None, alias="Groups")


class PrincipalModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[
        Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"]
    ] = Field(default=None, alias="Type")
    roles: Optional[List[PermissionInfoModel]] = Field(default=None, alias="Roles")


class ResourcePathModel(BaseModel):
    components: Optional[List[ResourcePathComponentModel]] = Field(
        default=None, alias="Components"
    )


class UserModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    username: Optional[str] = Field(default=None, alias="Username")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    given_name: Optional[str] = Field(default=None, alias="GivenName")
    surname: Optional[str] = Field(default=None, alias="Surname")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    root_folder_id: Optional[str] = Field(default=None, alias="RootFolderId")
    recycle_bin_folder_id: Optional[str] = Field(
        default=None, alias="RecycleBinFolderId"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    type: Optional[
        Literal["ADMIN", "MINIMALUSER", "POWERUSER", "USER", "WORKSPACESUSER"]
    ] = Field(default=None, alias="Type")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    modified_timestamp: Optional[datetime] = Field(
        default=None, alias="ModifiedTimestamp"
    )
    time_zone_id: Optional[str] = Field(default=None, alias="TimeZoneId")
    locale: Optional[
        Literal[
            "de",
            "default",
            "en",
            "es",
            "fr",
            "ja",
            "ko",
            "pt_BR",
            "ru",
            "zh_CN",
            "zh_TW",
        ]
    ] = Field(default=None, alias="Locale")
    storage: Optional[UserStorageMetadataModel] = Field(default=None, alias="Storage")


class DescribeFolderContentsResponseModel(BaseModel):
    folders: List[FolderMetadataModel] = Field(alias="Folders")
    documents: List[DocumentMetadataModel] = Field(alias="Documents")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDocumentResponseModel(BaseModel):
    metadata: DocumentMetadataModel = Field(alias="Metadata")
    custom_metadata: Dict[str, str] = Field(alias="CustomMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcesResponseModel(BaseModel):
    folders: List[FolderMetadataModel] = Field(alias="Folders")
    documents: List[DocumentMetadataModel] = Field(alias="Documents")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InitiateDocumentVersionUploadResponseModel(BaseModel):
    metadata: DocumentMetadataModel = Field(alias="Metadata")
    upload_metadata: UploadMetadataModel = Field(alias="UploadMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePermissionsResponseModel(BaseModel):
    principals: List[PrincipalModel] = Field(alias="Principals")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDocumentPathResponseModel(BaseModel):
    path: ResourcePathModel = Field(alias="Path")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFolderPathResponseModel(BaseModel):
    path: ResourcePathModel = Field(alias="Path")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommentMetadataModel(BaseModel):
    comment_id: Optional[str] = Field(default=None, alias="CommentId")
    contributor: Optional[UserModel] = Field(default=None, alias="Contributor")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    comment_status: Optional[Literal["DELETED", "DRAFT", "PUBLISHED"]] = Field(
        default=None, alias="CommentStatus"
    )
    recipient_id: Optional[str] = Field(default=None, alias="RecipientId")


class CommentModel(BaseModel):
    comment_id: str = Field(alias="CommentId")
    parent_id: Optional[str] = Field(default=None, alias="ParentId")
    thread_id: Optional[str] = Field(default=None, alias="ThreadId")
    text: Optional[str] = Field(default=None, alias="Text")
    contributor: Optional[UserModel] = Field(default=None, alias="Contributor")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    status: Optional[Literal["DELETED", "DRAFT", "PUBLISHED"]] = Field(
        default=None, alias="Status"
    )
    visibility: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="Visibility"
    )
    recipient_id: Optional[str] = Field(default=None, alias="RecipientId")


class CreateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    total_number_of_users: int = Field(alias="TotalNumberOfUsers")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCurrentUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActivityModel(BaseModel):
    type: Optional[
        Literal[
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_MOVED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RENAMED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_VIEWED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_MOVED",
            "FOLDER_RECYCLED",
            "FOLDER_RENAMED",
            "FOLDER_RESTORED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_UNSHARED",
        ]
    ] = Field(default=None, alias="Type")
    time_stamp: Optional[datetime] = Field(default=None, alias="TimeStamp")
    is_indirect_activity: Optional[bool] = Field(
        default=None, alias="IsIndirectActivity"
    )
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    initiator: Optional[UserMetadataModel] = Field(default=None, alias="Initiator")
    participants: Optional[ParticipantsModel] = Field(
        default=None, alias="Participants"
    )
    resource_metadata: Optional[ResourceMetadataModel] = Field(
        default=None, alias="ResourceMetadata"
    )
    original_parent: Optional[ResourceMetadataModel] = Field(
        default=None, alias="OriginalParent"
    )
    comment_metadata: Optional[CommentMetadataModel] = Field(
        default=None, alias="CommentMetadata"
    )


class CreateCommentResponseModel(BaseModel):
    comment: CommentModel = Field(alias="Comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCommentsResponseModel(BaseModel):
    comments: List[CommentModel] = Field(alias="Comments")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeActivitiesResponseModel(BaseModel):
    user_activities: List[ActivityModel] = Field(alias="UserActivities")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
