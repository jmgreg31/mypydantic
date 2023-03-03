# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountInfoModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    account_name: Optional[str] = Field(default=None, alias="accountName")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetRoleCredentialsRequestModel(BaseModel):
    role_name: str = Field(alias="roleName")
    account_id: str = Field(alias="accountId")
    access_token: str = Field(alias="accessToken")


class RoleCredentialsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    secret_access_key: Optional[str] = Field(default=None, alias="secretAccessKey")
    session_token: Optional[str] = Field(default=None, alias="sessionToken")
    expiration: Optional[int] = Field(default=None, alias="expiration")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccountRolesRequestModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    account_id: str = Field(alias="accountId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RoleInfoModel(BaseModel):
    role_name: Optional[str] = Field(default=None, alias="roleName")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ListAccountsRequestModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class LogoutRequestModel(BaseModel):
    access_token: str = Field(alias="accessToken")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    account_list: List[AccountInfoModel] = Field(alias="accountList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoleCredentialsResponseModel(BaseModel):
    role_credentials: RoleCredentialsModel = Field(alias="roleCredentials")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountRolesRequestListAccountRolesPaginateModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    account_id: str = Field(alias="accountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountsRequestListAccountsPaginateModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountRolesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    role_list: List[RoleInfoModel] = Field(alias="roleList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
