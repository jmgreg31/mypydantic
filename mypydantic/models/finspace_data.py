# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateUserToPermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    user_id: str = Field(alias="userId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AwsCredentialsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    secret_access_key: Optional[str] = Field(default=None, alias="secretAccessKey")
    session_token: Optional[str] = Field(default=None, alias="sessionToken")
    expiration: Optional[int] = Field(default=None, alias="expiration")


class ChangesetErrorInfoModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    error_category: Optional[
        Literal[
            "ACCESS_DENIED",
            "CANCELLED",
            "INTERNAL_SERVICE_EXCEPTION",
            "RESOURCE_NOT_FOUND",
            "SERVICE_QUOTA_EXCEEDED",
            "THROTTLING",
            "USER_RECOVERABLE",
            "VALIDATION",
        ]
    ] = Field(default=None, alias="errorCategory")


class ColumnDefinitionModel(BaseModel):
    data_type: Optional[
        Literal[
            "BIGINT",
            "BINARY",
            "BOOLEAN",
            "CHAR",
            "DATE",
            "DATETIME",
            "DOUBLE",
            "FLOAT",
            "INTEGER",
            "SMALLINT",
            "STRING",
            "TINYINT",
        ]
    ] = Field(default=None, alias="dataType")
    column_name: Optional[str] = Field(default=None, alias="columnName")
    column_description: Optional[str] = Field(default=None, alias="columnDescription")


class CreateChangesetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    change_type: Literal["APPEND", "MODIFY", "REPLACE"] = Field(alias="changeType")
    source_params: Mapping[str, str] = Field(alias="sourceParams")
    format_params: Mapping[str, str] = Field(alias="formatParams")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DataViewDestinationTypeParamsModel(BaseModel):
    destination_type: str = Field(alias="destinationType")
    s3_destination_export_file_format: Optional[
        Literal["DELIMITED_TEXT", "PARQUET"]
    ] = Field(default=None, alias="s3DestinationExportFileFormat")
    s3_destination_export_file_format_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="s3DestinationExportFileFormatOptions"
    )


class DatasetOwnerInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    phone_number: Optional[str] = Field(default=None, alias="phoneNumber")
    email: Optional[str] = Field(default=None, alias="email")


class CreatePermissionGroupRequestModel(BaseModel):
    name: str = Field(alias="name")
    application_permissions: Sequence[
        Literal[
            "AccessNotebooks",
            "CreateDataset",
            "GetTemporaryCredentials",
            "ManageAttributeSets",
            "ManageClusters",
            "ManageUsersAndGroups",
            "ViewAuditData",
        ]
    ] = Field(alias="applicationPermissions")
    description: Optional[str] = Field(default=None, alias="description")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CreateUserRequestModel(BaseModel):
    email_address: str = Field(alias="emailAddress")
    type: Literal["APP_USER", "SUPER_USER"] = Field(alias="type")
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    api_access: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ApiAccess"
    )
    api_access_principal_arn: Optional[str] = Field(
        default=None, alias="apiAccessPrincipalArn"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CredentialsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    secret_access_key: Optional[str] = Field(default=None, alias="secretAccessKey")
    session_token: Optional[str] = Field(default=None, alias="sessionToken")


class DataViewErrorInfoModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    error_category: Optional[
        Literal[
            "ACCESS_DENIED",
            "CANCELLED",
            "INTERNAL_SERVICE_EXCEPTION",
            "RESOURCE_NOT_FOUND",
            "SERVICE_QUOTA_EXCEEDED",
            "THROTTLING",
            "USER_RECOVERABLE",
            "VALIDATION",
        ]
    ] = Field(default=None, alias="errorCategory")


class DeleteDatasetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeletePermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DisableUserRequestModel(BaseModel):
    user_id: str = Field(alias="userId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DisassociateUserFromPermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    user_id: str = Field(alias="userId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class EnableUserRequestModel(BaseModel):
    user_id: str = Field(alias="userId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetChangesetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    changeset_id: str = Field(alias="changesetId")


class GetDataViewRequestModel(BaseModel):
    data_view_id: str = Field(alias="dataViewId")
    dataset_id: str = Field(alias="datasetId")


class GetDatasetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")


class GetExternalDataViewAccessDetailsRequestModel(BaseModel):
    data_view_id: str = Field(alias="dataViewId")
    dataset_id: str = Field(alias="datasetId")


class S3LocationModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")


class GetPermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")


class PermissionGroupModel(BaseModel):
    permission_group_id: Optional[str] = Field(default=None, alias="permissionGroupId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    application_permissions: Optional[
        List[
            Literal[
                "AccessNotebooks",
                "CreateDataset",
                "GetTemporaryCredentials",
                "ManageAttributeSets",
                "ManageClusters",
                "ManageUsersAndGroups",
                "ViewAuditData",
            ]
        ]
    ] = Field(default=None, alias="applicationPermissions")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    last_modified_time: Optional[int] = Field(default=None, alias="lastModifiedTime")
    membership_status: Optional[
        Literal["ADDITION_IN_PROGRESS", "ADDITION_SUCCESS", "REMOVAL_IN_PROGRESS"]
    ] = Field(default=None, alias="membershipStatus")


class GetProgrammaticAccessCredentialsRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    duration_in_minutes: Optional[int] = Field(default=None, alias="durationInMinutes")


class GetUserRequestModel(BaseModel):
    user_id: str = Field(alias="userId")


class GetWorkingLocationRequestModel(BaseModel):
    location_type: Optional[Literal["INGESTION", "SAGEMAKER"]] = Field(
        default=None, alias="locationType"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListChangesetsRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDataViewsRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDatasetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListPermissionGroupsByUserRequestModel(BaseModel):
    user_id: str = Field(alias="userId")
    max_results: int = Field(alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PermissionGroupByUserModel(BaseModel):
    permission_group_id: Optional[str] = Field(default=None, alias="permissionGroupId")
    name: Optional[str] = Field(default=None, alias="name")
    membership_status: Optional[
        Literal["ADDITION_IN_PROGRESS", "ADDITION_SUCCESS", "REMOVAL_IN_PROGRESS"]
    ] = Field(default=None, alias="membershipStatus")


class ListPermissionGroupsRequestModel(BaseModel):
    max_results: int = Field(alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListUsersByPermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    max_results: int = Field(alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UserByPermissionGroupModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="userId")
    status: Optional[Literal["CREATING", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")
    type: Optional[Literal["APP_USER", "SUPER_USER"]] = Field(
        default=None, alias="type"
    )
    api_access: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="apiAccess"
    )
    api_access_principal_arn: Optional[str] = Field(
        default=None, alias="apiAccessPrincipalArn"
    )
    membership_status: Optional[
        Literal["ADDITION_IN_PROGRESS", "ADDITION_SUCCESS", "REMOVAL_IN_PROGRESS"]
    ] = Field(default=None, alias="membershipStatus")


class ListUsersRequestModel(BaseModel):
    max_results: int = Field(alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UserModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="userId")
    status: Optional[Literal["CREATING", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")
    type: Optional[Literal["APP_USER", "SUPER_USER"]] = Field(
        default=None, alias="type"
    )
    api_access: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="apiAccess"
    )
    api_access_principal_arn: Optional[str] = Field(
        default=None, alias="apiAccessPrincipalArn"
    )
    create_time: Optional[int] = Field(default=None, alias="createTime")
    last_enabled_time: Optional[int] = Field(default=None, alias="lastEnabledTime")
    last_disabled_time: Optional[int] = Field(default=None, alias="lastDisabledTime")
    last_modified_time: Optional[int] = Field(default=None, alias="lastModifiedTime")
    last_login_time: Optional[int] = Field(default=None, alias="lastLoginTime")


class ResourcePermissionModel(BaseModel):
    permission: Optional[str] = Field(default=None, alias="permission")


class ResetUserPasswordRequestModel(BaseModel):
    user_id: str = Field(alias="userId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateChangesetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    changeset_id: str = Field(alias="changesetId")
    source_params: Mapping[str, str] = Field(alias="sourceParams")
    format_params: Mapping[str, str] = Field(alias="formatParams")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdatePermissionGroupRequestModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    application_permissions: Optional[
        Sequence[
            Literal[
                "AccessNotebooks",
                "CreateDataset",
                "GetTemporaryCredentials",
                "ManageAttributeSets",
                "ManageClusters",
                "ManageUsersAndGroups",
                "ViewAuditData",
            ]
        ]
    ] = Field(default=None, alias="applicationPermissions")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateUserRequestModel(BaseModel):
    user_id: str = Field(alias="userId")
    type: Optional[Literal["APP_USER", "SUPER_USER"]] = Field(
        default=None, alias="type"
    )
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    api_access: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="apiAccess"
    )
    api_access_principal_arn: Optional[str] = Field(
        default=None, alias="apiAccessPrincipalArn"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AssociateUserToPermissionGroupResponseModel(BaseModel):
    status_code: int = Field(alias="statusCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateChangesetResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    changeset_id: str = Field(alias="changesetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataViewResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    data_view_id: str = Field(alias="dataViewId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePermissionGroupResponseModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDatasetResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePermissionGroupResponseModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableUserResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateUserFromPermissionGroupResponseModel(BaseModel):
    status_code: int = Field(alias="statusCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableUserResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    status: Literal["CREATING", "DISABLED", "ENABLED"] = Field(alias="status")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email_address: str = Field(alias="emailAddress")
    type: Literal["APP_USER", "SUPER_USER"] = Field(alias="type")
    api_access: Literal["DISABLED", "ENABLED"] = Field(alias="apiAccess")
    api_access_principal_arn: str = Field(alias="apiAccessPrincipalArn")
    create_time: int = Field(alias="createTime")
    last_enabled_time: int = Field(alias="lastEnabledTime")
    last_disabled_time: int = Field(alias="lastDisabledTime")
    last_modified_time: int = Field(alias="lastModifiedTime")
    last_login_time: int = Field(alias="lastLoginTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkingLocationResponseModel(BaseModel):
    s3_uri: str = Field(alias="s3Uri")
    s3_path: str = Field(alias="s3Path")
    s3_bucket: str = Field(alias="s3Bucket")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetUserPasswordResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    temporary_password: str = Field(alias="temporaryPassword")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateChangesetResponseModel(BaseModel):
    changeset_id: str = Field(alias="changesetId")
    dataset_id: str = Field(alias="datasetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatasetResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePermissionGroupResponseModel(BaseModel):
    permission_group_id: str = Field(alias="permissionGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    user_id: str = Field(alias="userId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangesetSummaryModel(BaseModel):
    changeset_id: Optional[str] = Field(default=None, alias="changesetId")
    changeset_arn: Optional[str] = Field(default=None, alias="changesetArn")
    dataset_id: Optional[str] = Field(default=None, alias="datasetId")
    change_type: Optional[Literal["APPEND", "MODIFY", "REPLACE"]] = Field(
        default=None, alias="changeType"
    )
    source_params: Optional[Dict[str, str]] = Field(default=None, alias="sourceParams")
    format_params: Optional[Dict[str, str]] = Field(default=None, alias="formatParams")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    status: Optional[
        Literal["FAILED", "PENDING", "RUNNING", "STOP_REQUESTED", "SUCCESS"]
    ] = Field(default=None, alias="status")
    error_info: Optional[ChangesetErrorInfoModel] = Field(
        default=None, alias="errorInfo"
    )
    active_until_timestamp: Optional[int] = Field(
        default=None, alias="activeUntilTimestamp"
    )
    active_from_timestamp: Optional[int] = Field(
        default=None, alias="activeFromTimestamp"
    )
    updates_changeset_id: Optional[str] = Field(
        default=None, alias="updatesChangesetId"
    )
    updated_by_changeset_id: Optional[str] = Field(
        default=None, alias="updatedByChangesetId"
    )


class GetChangesetResponseModel(BaseModel):
    changeset_id: str = Field(alias="changesetId")
    changeset_arn: str = Field(alias="changesetArn")
    dataset_id: str = Field(alias="datasetId")
    change_type: Literal["APPEND", "MODIFY", "REPLACE"] = Field(alias="changeType")
    source_params: Dict[str, str] = Field(alias="sourceParams")
    format_params: Dict[str, str] = Field(alias="formatParams")
    create_time: int = Field(alias="createTime")
    status: Literal[
        "FAILED", "PENDING", "RUNNING", "STOP_REQUESTED", "SUCCESS"
    ] = Field(alias="status")
    error_info: ChangesetErrorInfoModel = Field(alias="errorInfo")
    active_until_timestamp: int = Field(alias="activeUntilTimestamp")
    active_from_timestamp: int = Field(alias="activeFromTimestamp")
    updates_changeset_id: str = Field(alias="updatesChangesetId")
    updated_by_changeset_id: str = Field(alias="updatedByChangesetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SchemaDefinitionModel(BaseModel):
    columns: Optional[Sequence[ColumnDefinitionModel]] = Field(
        default=None, alias="columns"
    )
    primary_key_columns: Optional[Sequence[str]] = Field(
        default=None, alias="primaryKeyColumns"
    )


class CreateDataViewRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    destination_type_params: DataViewDestinationTypeParamsModel = Field(
        alias="destinationTypeParams"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    auto_update: Optional[bool] = Field(default=None, alias="autoUpdate")
    sort_columns: Optional[Sequence[str]] = Field(default=None, alias="sortColumns")
    partition_columns: Optional[Sequence[str]] = Field(
        default=None, alias="partitionColumns"
    )
    as_of_timestamp: Optional[int] = Field(default=None, alias="asOfTimestamp")


class GetProgrammaticAccessCredentialsResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="credentials")
    duration_in_minutes: int = Field(alias="durationInMinutes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataViewSummaryModel(BaseModel):
    data_view_id: Optional[str] = Field(default=None, alias="dataViewId")
    data_view_arn: Optional[str] = Field(default=None, alias="dataViewArn")
    dataset_id: Optional[str] = Field(default=None, alias="datasetId")
    as_of_timestamp: Optional[int] = Field(default=None, alias="asOfTimestamp")
    partition_columns: Optional[List[str]] = Field(
        default=None, alias="partitionColumns"
    )
    sort_columns: Optional[List[str]] = Field(default=None, alias="sortColumns")
    status: Optional[
        Literal[
            "CANCELLED",
            "FAILED",
            "FAILED_CLEANUP_FAILED",
            "PENDING",
            "RUNNING",
            "STARTING",
            "SUCCESS",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="status")
    error_info: Optional[DataViewErrorInfoModel] = Field(
        default=None, alias="errorInfo"
    )
    destination_type_properties: Optional[DataViewDestinationTypeParamsModel] = Field(
        default=None, alias="destinationTypeProperties"
    )
    auto_update: Optional[bool] = Field(default=None, alias="autoUpdate")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    last_modified_time: Optional[int] = Field(default=None, alias="lastModifiedTime")


class GetDataViewResponseModel(BaseModel):
    auto_update: bool = Field(alias="autoUpdate")
    partition_columns: List[str] = Field(alias="partitionColumns")
    dataset_id: str = Field(alias="datasetId")
    as_of_timestamp: int = Field(alias="asOfTimestamp")
    error_info: DataViewErrorInfoModel = Field(alias="errorInfo")
    last_modified_time: int = Field(alias="lastModifiedTime")
    create_time: int = Field(alias="createTime")
    sort_columns: List[str] = Field(alias="sortColumns")
    data_view_id: str = Field(alias="dataViewId")
    data_view_arn: str = Field(alias="dataViewArn")
    destination_type_params: DataViewDestinationTypeParamsModel = Field(
        alias="destinationTypeParams"
    )
    status: Literal[
        "CANCELLED",
        "FAILED",
        "FAILED_CLEANUP_FAILED",
        "PENDING",
        "RUNNING",
        "STARTING",
        "SUCCESS",
        "TIMEOUT",
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExternalDataViewAccessDetailsResponseModel(BaseModel):
    credentials: AwsCredentialsModel = Field(alias="credentials")
    s3_location: S3LocationModel = Field(alias="s3Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPermissionGroupResponseModel(BaseModel):
    permission_group: PermissionGroupModel = Field(alias="permissionGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionGroupsResponseModel(BaseModel):
    permission_groups: List[PermissionGroupModel] = Field(alias="permissionGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChangesetsRequestListChangesetsPaginateModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataViewsRequestListDataViewsPaginateModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetsRequestListDatasetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionGroupsRequestListPermissionGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionGroupsByUserResponseModel(BaseModel):
    permission_groups: List[PermissionGroupByUserModel] = Field(
        alias="permissionGroups"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersByPermissionGroupResponseModel(BaseModel):
    users: List[UserByPermissionGroupModel] = Field(alias="users")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="users")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PermissionGroupParamsModel(BaseModel):
    permission_group_id: Optional[str] = Field(default=None, alias="permissionGroupId")
    dataset_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="datasetPermissions"
    )


class ListChangesetsResponseModel(BaseModel):
    changesets: List[ChangesetSummaryModel] = Field(alias="changesets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SchemaUnionModel(BaseModel):
    tabular_schema_config: Optional[SchemaDefinitionModel] = Field(
        default=None, alias="tabularSchemaConfig"
    )


class ListDataViewsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    data_views: List[DataViewSummaryModel] = Field(alias="dataViews")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetRequestModel(BaseModel):
    dataset_title: str = Field(alias="datasetTitle")
    kind: Literal["NON_TABULAR", "TABULAR"] = Field(alias="kind")
    permission_group_params: PermissionGroupParamsModel = Field(
        alias="permissionGroupParams"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    dataset_description: Optional[str] = Field(default=None, alias="datasetDescription")
    owner_info: Optional[DatasetOwnerInfoModel] = Field(default=None, alias="ownerInfo")
    alias: Optional[str] = Field(default=None, alias="alias")
    schema_definition: Optional[SchemaUnionModel] = Field(
        default=None, alias="schemaDefinition"
    )


class DatasetModel(BaseModel):
    dataset_id: Optional[str] = Field(default=None, alias="datasetId")
    dataset_arn: Optional[str] = Field(default=None, alias="datasetArn")
    dataset_title: Optional[str] = Field(default=None, alias="datasetTitle")
    kind: Optional[Literal["NON_TABULAR", "TABULAR"]] = Field(
        default=None, alias="kind"
    )
    dataset_description: Optional[str] = Field(default=None, alias="datasetDescription")
    owner_info: Optional[DatasetOwnerInfoModel] = Field(default=None, alias="ownerInfo")
    create_time: Optional[int] = Field(default=None, alias="createTime")
    last_modified_time: Optional[int] = Field(default=None, alias="lastModifiedTime")
    schema_definition: Optional[SchemaUnionModel] = Field(
        default=None, alias="schemaDefinition"
    )
    alias: Optional[str] = Field(default=None, alias="alias")


class GetDatasetResponseModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    dataset_arn: str = Field(alias="datasetArn")
    dataset_title: str = Field(alias="datasetTitle")
    kind: Literal["NON_TABULAR", "TABULAR"] = Field(alias="kind")
    dataset_description: str = Field(alias="datasetDescription")
    create_time: int = Field(alias="createTime")
    last_modified_time: int = Field(alias="lastModifiedTime")
    schema_definition: SchemaUnionModel = Field(alias="schemaDefinition")
    alias: str = Field(alias="alias")
    status: Literal["FAILED", "PENDING", "RUNNING", "SUCCESS"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDatasetRequestModel(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    dataset_title: str = Field(alias="datasetTitle")
    kind: Literal["NON_TABULAR", "TABULAR"] = Field(alias="kind")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    dataset_description: Optional[str] = Field(default=None, alias="datasetDescription")
    alias: Optional[str] = Field(default=None, alias="alias")
    schema_definition: Optional[SchemaUnionModel] = Field(
        default=None, alias="schemaDefinition"
    )


class ListDatasetsResponseModel(BaseModel):
    datasets: List[DatasetModel] = Field(alias="datasets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
