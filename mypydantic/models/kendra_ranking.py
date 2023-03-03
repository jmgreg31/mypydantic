# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CapacityUnitsConfigurationModel(BaseModel):
    rescore_capacity_units: int = Field(alias="RescoreCapacityUnits")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteRescoreExecutionPlanRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribeRescoreExecutionPlanRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DocumentModel(BaseModel):
    id: str = Field(alias="Id")
    original_score: float = Field(alias="OriginalScore")
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    title: Optional[str] = Field(default=None, alias="Title")
    body: Optional[str] = Field(default=None, alias="Body")
    tokenized_title: Optional[Sequence[str]] = Field(
        default=None, alias="TokenizedTitle"
    )
    tokenized_body: Optional[Sequence[str]] = Field(default=None, alias="TokenizedBody")


class ListRescoreExecutionPlansRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RescoreExecutionPlanSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class RescoreResultItemModel(BaseModel):
    document_id: Optional[str] = Field(default=None, alias="DocumentId")
    score: Optional[float] = Field(default=None, alias="Score")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateRescoreExecutionPlanRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    capacity_units: Optional[CapacityUnitsConfigurationModel] = Field(
        default=None, alias="CapacityUnits"
    )


class CreateRescoreExecutionPlanRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    capacity_units: Optional[CapacityUnitsConfigurationModel] = Field(
        default=None, alias="CapacityUnits"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateRescoreExecutionPlanResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRescoreExecutionPlanResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    capacity_units: CapacityUnitsConfigurationModel = Field(alias="CapacityUnits")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    error_message: str = Field(alias="ErrorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RescoreRequestModel(BaseModel):
    rescore_execution_plan_id: str = Field(alias="RescoreExecutionPlanId")
    search_query: str = Field(alias="SearchQuery")
    documents: Sequence[DocumentModel] = Field(alias="Documents")


class ListRescoreExecutionPlansResponseModel(BaseModel):
    summary_items: List[RescoreExecutionPlanSummaryModel] = Field(alias="SummaryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RescoreResultModel(BaseModel):
    rescore_id: str = Field(alias="RescoreId")
    result_items: List[RescoreResultItemModel] = Field(alias="ResultItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
