# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteHumanLoopRequestModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")


class DescribeHumanLoopRequestModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")


class HumanLoopOutputModel(BaseModel):
    output_s3_uri: str = Field(alias="OutputS3Uri")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class HumanLoopDataAttributesModel(BaseModel):
    content_classifiers: Sequence[
        Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
    ] = Field(alias="ContentClassifiers")


class HumanLoopInputModel(BaseModel):
    input_content: str = Field(alias="InputContent")


class HumanLoopSummaryModel(BaseModel):
    human_loop_name: Optional[str] = Field(default=None, alias="HumanLoopName")
    human_loop_status: Optional[
        Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
    ] = Field(default=None, alias="HumanLoopStatus")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    flow_definition_arn: Optional[str] = Field(default=None, alias="FlowDefinitionArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListHumanLoopsRequestModel(BaseModel):
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StopHumanLoopRequestModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")


class DescribeHumanLoopResponseModel(BaseModel):
    creation_time: datetime = Field(alias="CreationTime")
    failure_reason: str = Field(alias="FailureReason")
    failure_code: str = Field(alias="FailureCode")
    human_loop_status: Literal[
        "Completed", "Failed", "InProgress", "Stopped", "Stopping"
    ] = Field(alias="HumanLoopStatus")
    human_loop_name: str = Field(alias="HumanLoopName")
    human_loop_arn: str = Field(alias="HumanLoopArn")
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    human_loop_output: HumanLoopOutputModel = Field(alias="HumanLoopOutput")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartHumanLoopResponseModel(BaseModel):
    human_loop_arn: str = Field(alias="HumanLoopArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartHumanLoopRequestModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    human_loop_input: HumanLoopInputModel = Field(alias="HumanLoopInput")
    data_attributes: Optional[HumanLoopDataAttributesModel] = Field(
        default=None, alias="DataAttributes"
    )


class ListHumanLoopsResponseModel(BaseModel):
    human_loop_summaries: List[HumanLoopSummaryModel] = Field(
        alias="HumanLoopSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHumanLoopsRequestListHumanLoopsPaginateModel(BaseModel):
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    sort_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
