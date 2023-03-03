# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GetRoutingControlStateRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRoutingControlsRequestModel(BaseModel):
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RoutingControlModel(BaseModel):
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")
    control_panel_name: Optional[str] = Field(default=None, alias="ControlPanelName")
    routing_control_arn: Optional[str] = Field(default=None, alias="RoutingControlArn")
    routing_control_name: Optional[str] = Field(
        default=None, alias="RoutingControlName"
    )
    routing_control_state: Optional[Literal["Off", "On"]] = Field(
        default=None, alias="RoutingControlState"
    )


class UpdateRoutingControlStateEntryModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    routing_control_state: Literal["Off", "On"] = Field(alias="RoutingControlState")


class UpdateRoutingControlStateRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    routing_control_state: Literal["Off", "On"] = Field(alias="RoutingControlState")
    safety_rules_to_override: Optional[Sequence[str]] = Field(
        default=None, alias="SafetyRulesToOverride"
    )


class GetRoutingControlStateResponseModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    routing_control_state: Literal["Off", "On"] = Field(alias="RoutingControlState")
    routing_control_name: str = Field(alias="RoutingControlName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutingControlsRequestListRoutingControlsPaginateModel(BaseModel):
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutingControlsResponseModel(BaseModel):
    routing_controls: List[RoutingControlModel] = Field(alias="RoutingControls")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoutingControlStatesRequestModel(BaseModel):
    update_routing_control_state_entries: Sequence[
        UpdateRoutingControlStateEntryModel
    ] = Field(alias="UpdateRoutingControlStateEntries")
    safety_rules_to_override: Optional[Sequence[str]] = Field(
        default=None, alias="SafetyRulesToOverride"
    )
