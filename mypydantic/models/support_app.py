# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateSlackChannelConfigurationRequestModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    channel_role_arn: str = Field(alias="channelRoleArn")
    notify_on_case_severity: Literal["all", "high", "none"] = Field(
        alias="notifyOnCaseSeverity"
    )
    team_id: str = Field(alias="teamId")
    channel_name: Optional[str] = Field(default=None, alias="channelName")
    notify_on_add_correspondence_to_case: Optional[bool] = Field(
        default=None, alias="notifyOnAddCorrespondenceToCase"
    )
    notify_on_create_or_reopen_case: Optional[bool] = Field(
        default=None, alias="notifyOnCreateOrReopenCase"
    )
    notify_on_resolve_case: Optional[bool] = Field(
        default=None, alias="notifyOnResolveCase"
    )


class DeleteSlackChannelConfigurationRequestModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    team_id: str = Field(alias="teamId")


class DeleteSlackWorkspaceConfigurationRequestModel(BaseModel):
    team_id: str = Field(alias="teamId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ListSlackChannelConfigurationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SlackChannelConfigurationModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    team_id: str = Field(alias="teamId")
    channel_name: Optional[str] = Field(default=None, alias="channelName")
    channel_role_arn: Optional[str] = Field(default=None, alias="channelRoleArn")
    notify_on_add_correspondence_to_case: Optional[bool] = Field(
        default=None, alias="notifyOnAddCorrespondenceToCase"
    )
    notify_on_case_severity: Optional[Literal["all", "high", "none"]] = Field(
        default=None, alias="notifyOnCaseSeverity"
    )
    notify_on_create_or_reopen_case: Optional[bool] = Field(
        default=None, alias="notifyOnCreateOrReopenCase"
    )
    notify_on_resolve_case: Optional[bool] = Field(
        default=None, alias="notifyOnResolveCase"
    )


class ListSlackWorkspaceConfigurationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SlackWorkspaceConfigurationModel(BaseModel):
    team_id: str = Field(alias="teamId")
    allow_organization_member_account: Optional[bool] = Field(
        default=None, alias="allowOrganizationMemberAccount"
    )
    team_name: Optional[str] = Field(default=None, alias="teamName")


class PutAccountAliasRequestModel(BaseModel):
    account_alias: str = Field(alias="accountAlias")


class RegisterSlackWorkspaceForOrganizationRequestModel(BaseModel):
    team_id: str = Field(alias="teamId")


class UpdateSlackChannelConfigurationRequestModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    team_id: str = Field(alias="teamId")
    channel_name: Optional[str] = Field(default=None, alias="channelName")
    channel_role_arn: Optional[str] = Field(default=None, alias="channelRoleArn")
    notify_on_add_correspondence_to_case: Optional[bool] = Field(
        default=None, alias="notifyOnAddCorrespondenceToCase"
    )
    notify_on_case_severity: Optional[Literal["all", "high", "none"]] = Field(
        default=None, alias="notifyOnCaseSeverity"
    )
    notify_on_create_or_reopen_case: Optional[bool] = Field(
        default=None, alias="notifyOnCreateOrReopenCase"
    )
    notify_on_resolve_case: Optional[bool] = Field(
        default=None, alias="notifyOnResolveCase"
    )


class GetAccountAliasResultModel(BaseModel):
    account_alias: str = Field(alias="accountAlias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterSlackWorkspaceForOrganizationResultModel(BaseModel):
    account_type: Literal["management", "member"] = Field(alias="accountType")
    team_id: str = Field(alias="teamId")
    team_name: str = Field(alias="teamName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSlackChannelConfigurationResultModel(BaseModel):
    channel_id: str = Field(alias="channelId")
    channel_name: str = Field(alias="channelName")
    channel_role_arn: str = Field(alias="channelRoleArn")
    notify_on_add_correspondence_to_case: bool = Field(
        alias="notifyOnAddCorrespondenceToCase"
    )
    notify_on_case_severity: Literal["all", "high", "none"] = Field(
        alias="notifyOnCaseSeverity"
    )
    notify_on_create_or_reopen_case: bool = Field(alias="notifyOnCreateOrReopenCase")
    notify_on_resolve_case: bool = Field(alias="notifyOnResolveCase")
    team_id: str = Field(alias="teamId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSlackChannelConfigurationsResultModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    slack_channel_configurations: List[SlackChannelConfigurationModel] = Field(
        alias="slackChannelConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSlackWorkspaceConfigurationsResultModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    slack_workspace_configurations: List[SlackWorkspaceConfigurationModel] = Field(
        alias="slackWorkspaceConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
