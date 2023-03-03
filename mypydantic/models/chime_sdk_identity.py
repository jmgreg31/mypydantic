# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class IdentityModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ChannelRetentionSettingsModel(BaseModel):
    retention_days: Optional[int] = Field(default=None, alias="RetentionDays")


class AppInstanceSummaryModel(BaseModel):
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class AppInstanceModel(BaseModel):
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    name: Optional[str] = Field(default=None, alias="Name")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class EndpointStateModel(BaseModel):
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias="Status")
    status_reason: Optional[
        Literal["INVALID_DEVICE_TOKEN", "INVALID_PINPOINT_ARN"]
    ] = Field(default=None, alias="StatusReason")


class EndpointAttributesModel(BaseModel):
    device_token: str = Field(alias="DeviceToken")
    voip_device_token: Optional[str] = Field(default=None, alias="VoipDeviceToken")


class AppInstanceUserSummaryModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")


class AppInstanceUserModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class CreateAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DeleteAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DeleteAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")


class DeregisterAppInstanceUserEndpointRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    endpoint_id: str = Field(alias="EndpointId")


class DescribeAppInstanceAdminRequestModel(BaseModel):
    app_instance_admin_arn: str = Field(alias="AppInstanceAdminArn")
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DescribeAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class DescribeAppInstanceUserEndpointRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    endpoint_id: str = Field(alias="EndpointId")


class DescribeAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")


class GetAppInstanceRetentionSettingsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")


class ListAppInstanceAdminsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppInstanceUserEndpointsRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppInstanceUsersRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAppInstancesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAppInstanceRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    name: str = Field(alias="Name")
    metadata: str = Field(alias="Metadata")


class UpdateAppInstanceUserEndpointRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    endpoint_id: str = Field(alias="EndpointId")
    name: Optional[str] = Field(default=None, alias="Name")
    allow_messages: Optional[Literal["ALL", "NONE"]] = Field(
        default=None, alias="AllowMessages"
    )


class UpdateAppInstanceUserRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    name: str = Field(alias="Name")
    metadata: str = Field(alias="Metadata")


class AppInstanceAdminSummaryModel(BaseModel):
    admin: Optional[IdentityModel] = Field(default=None, alias="Admin")


class AppInstanceAdminModel(BaseModel):
    admin: Optional[IdentityModel] = Field(default=None, alias="Admin")
    app_instance_arn: Optional[str] = Field(default=None, alias="AppInstanceArn")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )


class AppInstanceRetentionSettingsModel(BaseModel):
    channel_retention_settings: Optional[ChannelRetentionSettingsModel] = Field(
        default=None, alias="ChannelRetentionSettings"
    )


class AppInstanceUserEndpointSummaryModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["APNS", "APNS_SANDBOX", "GCM"]] = Field(
        default=None, alias="Type"
    )
    allow_messages: Optional[Literal["ALL", "NONE"]] = Field(
        default=None, alias="AllowMessages"
    )
    endpoint_state: Optional[EndpointStateModel] = Field(
        default=None, alias="EndpointState"
    )


class AppInstanceUserEndpointModel(BaseModel):
    app_instance_user_arn: Optional[str] = Field(
        default=None, alias="AppInstanceUserArn"
    )
    endpoint_id: Optional[str] = Field(default=None, alias="EndpointId")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["APNS", "APNS_SANDBOX", "GCM"]] = Field(
        default=None, alias="Type"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    endpoint_attributes: Optional[EndpointAttributesModel] = Field(
        default=None, alias="EndpointAttributes"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    allow_messages: Optional[Literal["ALL", "NONE"]] = Field(
        default=None, alias="AllowMessages"
    )
    endpoint_state: Optional[EndpointStateModel] = Field(
        default=None, alias="EndpointState"
    )


class RegisterAppInstanceUserEndpointRequestModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    type: Literal["APNS", "APNS_SANDBOX", "GCM"] = Field(alias="Type")
    resource_arn: str = Field(alias="ResourceArn")
    endpoint_attributes: EndpointAttributesModel = Field(alias="EndpointAttributes")
    client_request_token: str = Field(alias="ClientRequestToken")
    name: Optional[str] = Field(default=None, alias="Name")
    allow_messages: Optional[Literal["ALL", "NONE"]] = Field(
        default=None, alias="AllowMessages"
    )


class CreateAppInstanceAdminResponseModel(BaseModel):
    app_instance_admin: IdentityModel = Field(alias="AppInstanceAdmin")
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceUserResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceResponseModel(BaseModel):
    app_instance: AppInstanceModel = Field(alias="AppInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceUserResponseModel(BaseModel):
    app_instance_user: AppInstanceUserModel = Field(alias="AppInstanceUser")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstanceUsersResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_users: List[AppInstanceUserSummaryModel] = Field(
        alias="AppInstanceUsers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstancesResponseModel(BaseModel):
    app_instances: List[AppInstanceSummaryModel] = Field(alias="AppInstances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterAppInstanceUserEndpointResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    endpoint_id: str = Field(alias="EndpointId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppInstanceResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppInstanceUserEndpointResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    endpoint_id: str = Field(alias="EndpointId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppInstanceUserResponseModel(BaseModel):
    app_instance_user_arn: str = Field(alias="AppInstanceUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppInstanceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateAppInstanceUserRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_user_id: str = Field(alias="AppInstanceUserId")
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListAppInstanceAdminsResponseModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_admins: List[AppInstanceAdminSummaryModel] = Field(
        alias="AppInstanceAdmins"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceAdminResponseModel(BaseModel):
    app_instance_admin: AppInstanceAdminModel = Field(alias="AppInstanceAdmin")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppInstanceRetentionSettingsResponseModel(BaseModel):
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAppInstanceRetentionSettingsRequestModel(BaseModel):
    app_instance_arn: str = Field(alias="AppInstanceArn")
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )


class PutAppInstanceRetentionSettingsResponseModel(BaseModel):
    app_instance_retention_settings: AppInstanceRetentionSettingsModel = Field(
        alias="AppInstanceRetentionSettings"
    )
    initiate_deletion_timestamp: datetime = Field(alias="InitiateDeletionTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInstanceUserEndpointsResponseModel(BaseModel):
    app_instance_user_endpoints: List[AppInstanceUserEndpointSummaryModel] = Field(
        alias="AppInstanceUserEndpoints"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppInstanceUserEndpointResponseModel(BaseModel):
    app_instance_user_endpoint: AppInstanceUserEndpointModel = Field(
        alias="AppInstanceUserEndpoint"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
