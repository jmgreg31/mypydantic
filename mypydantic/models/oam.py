# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateLinkInputRequestModel(BaseModel):
    label_template: str = Field(alias="LabelTemplate")
    resource_types: Sequence[
        Literal["AWS::CloudWatch::Metric", "AWS::Logs::LogGroup", "AWS::XRay::Trace"]
    ] = Field(alias="ResourceTypes")
    sink_identifier: str = Field(alias="SinkIdentifier")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateSinkInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteLinkInputRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class DeleteSinkInputRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetLinkInputRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetSinkInputRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetSinkPolicyInputRequestModel(BaseModel):
    sink_identifier: str = Field(alias="SinkIdentifier")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAttachedLinksInputRequestModel(BaseModel):
    sink_identifier: str = Field(alias="SinkIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAttachedLinksItemModel(BaseModel):
    label: Optional[str] = Field(default=None, alias="Label")
    link_arn: Optional[str] = Field(default=None, alias="LinkArn")
    resource_types: Optional[List[str]] = Field(default=None, alias="ResourceTypes")


class ListLinksInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLinksItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    label: Optional[str] = Field(default=None, alias="Label")
    resource_types: Optional[List[str]] = Field(default=None, alias="ResourceTypes")
    sink_arn: Optional[str] = Field(default=None, alias="SinkArn")


class ListSinksInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSinksItemModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PutSinkPolicyInputRequestModel(BaseModel):
    sink_identifier: str = Field(alias="SinkIdentifier")
    policy: str = Field(alias="Policy")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateLinkInputRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    resource_types: Sequence[
        Literal["AWS::CloudWatch::Metric", "AWS::Logs::LogGroup", "AWS::XRay::Trace"]
    ] = Field(alias="ResourceTypes")


class CreateLinkOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    label: str = Field(alias="Label")
    label_template: str = Field(alias="LabelTemplate")
    resource_types: List[str] = Field(alias="ResourceTypes")
    sink_arn: str = Field(alias="SinkArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSinkOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLinkOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    label: str = Field(alias="Label")
    label_template: str = Field(alias="LabelTemplate")
    resource_types: List[str] = Field(alias="ResourceTypes")
    sink_arn: str = Field(alias="SinkArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSinkOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSinkPolicyOutputModel(BaseModel):
    sink_arn: str = Field(alias="SinkArn")
    sink_id: str = Field(alias="SinkId")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSinkPolicyOutputModel(BaseModel):
    sink_arn: str = Field(alias="SinkArn")
    sink_id: str = Field(alias="SinkId")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLinkOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    label: str = Field(alias="Label")
    label_template: str = Field(alias="LabelTemplate")
    resource_types: List[str] = Field(alias="ResourceTypes")
    sink_arn: str = Field(alias="SinkArn")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachedLinksInputListAttachedLinksPaginateModel(BaseModel):
    sink_identifier: str = Field(alias="SinkIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLinksInputListLinksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSinksInputListSinksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedLinksOutputModel(BaseModel):
    items: List[ListAttachedLinksItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLinksOutputModel(BaseModel):
    items: List[ListLinksItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSinksOutputModel(BaseModel):
    items: List[ListSinksItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
