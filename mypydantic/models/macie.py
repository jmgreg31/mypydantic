# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateMemberAccountRequestModel(BaseModel):
    member_account_id: str = Field(alias="memberAccountId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ClassificationTypeModel(BaseModel):
    one_time: Literal["FULL", "NONE"] = Field(alias="oneTime")
    continuous: Literal["FULL"] = Field(alias="continuous")


class ClassificationTypeUpdateModel(BaseModel):
    one_time: Optional[Literal["FULL", "NONE"]] = Field(default=None, alias="oneTime")
    continuous: Optional[Literal["FULL"]] = Field(default=None, alias="continuous")


class DisassociateMemberAccountRequestModel(BaseModel):
    member_account_id: str = Field(alias="memberAccountId")


class S3ResourceModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListMemberAccountsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class MemberAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ListS3ResourcesRequestModel(BaseModel):
    member_account_id: Optional[str] = Field(default=None, alias="memberAccountId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3ResourceClassificationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    classification_type: ClassificationTypeModel = Field(alias="classificationType")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class S3ResourceClassificationUpdateModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    classification_type_update: ClassificationTypeUpdateModel = Field(
        alias="classificationTypeUpdate"
    )
    prefix: Optional[str] = Field(default=None, alias="prefix")


class DisassociateS3ResourcesRequestModel(BaseModel):
    associated_s3_resources: Sequence[S3ResourceModel] = Field(
        alias="associatedS3Resources"
    )
    member_account_id: Optional[str] = Field(default=None, alias="memberAccountId")


class FailedS3ResourceModel(BaseModel):
    failed_item: Optional[S3ResourceModel] = Field(default=None, alias="failedItem")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class ListMemberAccountsRequestListMemberAccountsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListS3ResourcesRequestListS3ResourcesPaginateModel(BaseModel):
    member_account_id: Optional[str] = Field(default=None, alias="memberAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMemberAccountsResultModel(BaseModel):
    member_accounts: List[MemberAccountModel] = Field(alias="memberAccounts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateS3ResourcesRequestModel(BaseModel):
    s3_resources: Sequence[S3ResourceClassificationModel] = Field(alias="s3Resources")
    member_account_id: Optional[str] = Field(default=None, alias="memberAccountId")


class ListS3ResourcesResultModel(BaseModel):
    s3_resources: List[S3ResourceClassificationModel] = Field(alias="s3Resources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateS3ResourcesRequestModel(BaseModel):
    s3_resources_update: Sequence[S3ResourceClassificationUpdateModel] = Field(
        alias="s3ResourcesUpdate"
    )
    member_account_id: Optional[str] = Field(default=None, alias="memberAccountId")


class AssociateS3ResourcesResultModel(BaseModel):
    failed_s3_resources: List[FailedS3ResourceModel] = Field(alias="failedS3Resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateS3ResourcesResultModel(BaseModel):
    failed_s3_resources: List[FailedS3ResourceModel] = Field(alias="failedS3Resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateS3ResourcesResultModel(BaseModel):
    failed_s3_resources: List[FailedS3ResourceModel] = Field(alias="failedS3Resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
