# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationSummaryModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_name: str = Field(alias="applicationName")
    application_url: str = Field(alias="applicationUrl")
    application_description: Optional[str] = Field(
        default=None, alias="applicationDescription"
    )
    application_creation_date: Optional[int] = Field(
        default=None, alias="applicationCreationDate"
    )
    application_last_update_date: Optional[int] = Field(
        default=None, alias="applicationLastUpdateDate"
    )
    application_state: Optional[
        Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
    ] = Field(default=None, alias="applicationState")


class CreateApplicationRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    role_arn: str = Field(alias="roleArn")
    application_description: Optional[str] = Field(
        default=None, alias="applicationDescription"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DescribeApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    application_description: Optional[str] = Field(
        default=None, alias="applicationDescription"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CreateApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_arn: str = Field(alias="applicationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    application_arn: str = Field(alias="applicationArn")
    application_name: str = Field(alias="applicationName")
    application_description: str = Field(alias="applicationDescription")
    application_url: str = Field(alias="applicationUrl")
    application_state: Literal[
        "ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
    ] = Field(alias="applicationState")
    application_creation_date: int = Field(alias="applicationCreationDate")
    application_last_update_date: int = Field(alias="applicationLastUpdateDate")
    role_arn: str = Field(alias="roleArn")
    sso_client_id: str = Field(alias="ssoClientId")
    error_message: str = Field(alias="errorMessage")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    application_summaries: List[ApplicationSummaryModel] = Field(
        alias="applicationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
