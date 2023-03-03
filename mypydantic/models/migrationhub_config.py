# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TargetModel(BaseModel):
    type: Literal["ACCOUNT"] = Field(alias="Type")
    id: Optional[str] = Field(default=None, alias="Id")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateHomeRegionControlRequestModel(BaseModel):
    home_region: str = Field(alias="HomeRegion")
    target: TargetModel = Field(alias="Target")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DescribeHomeRegionControlsRequestModel(BaseModel):
    control_id: Optional[str] = Field(default=None, alias="ControlId")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    target: Optional[TargetModel] = Field(default=None, alias="Target")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class HomeRegionControlModel(BaseModel):
    control_id: Optional[str] = Field(default=None, alias="ControlId")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    target: Optional[TargetModel] = Field(default=None, alias="Target")
    requested_time: Optional[datetime] = Field(default=None, alias="RequestedTime")


class GetHomeRegionResultModel(BaseModel):
    home_region: str = Field(alias="HomeRegion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHomeRegionControlResultModel(BaseModel):
    home_region_control: HomeRegionControlModel = Field(alias="HomeRegionControl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHomeRegionControlsResultModel(BaseModel):
    home_region_controls: List[HomeRegionControlModel] = Field(
        alias="HomeRegionControls"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
