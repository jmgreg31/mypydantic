# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ControlOperationModel(BaseModel):
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    operation_type: Optional[Literal["DISABLE_CONTROL", "ENABLE_CONTROL"]] = Field(
        default=None, alias="operationType"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class DisableControlInputRequestModel(BaseModel):
    control_identifier: str = Field(alias="controlIdentifier")
    target_identifier: str = Field(alias="targetIdentifier")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EnableControlInputRequestModel(BaseModel):
    control_identifier: str = Field(alias="controlIdentifier")
    target_identifier: str = Field(alias="targetIdentifier")


class EnabledControlSummaryModel(BaseModel):
    control_identifier: Optional[str] = Field(default=None, alias="controlIdentifier")


class GetControlOperationInputRequestModel(BaseModel):
    operation_identifier: str = Field(alias="operationIdentifier")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEnabledControlsInputRequestModel(BaseModel):
    target_identifier: str = Field(alias="targetIdentifier")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DisableControlOutputModel(BaseModel):
    operation_identifier: str = Field(alias="operationIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableControlOutputModel(BaseModel):
    operation_identifier: str = Field(alias="operationIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetControlOperationOutputModel(BaseModel):
    control_operation: ControlOperationModel = Field(alias="controlOperation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnabledControlsOutputModel(BaseModel):
    enabled_controls: List[EnabledControlSummaryModel] = Field(alias="enabledControls")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnabledControlsInputListEnabledControlsPaginateModel(BaseModel):
    target_identifier: str = Field(alias="targetIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
