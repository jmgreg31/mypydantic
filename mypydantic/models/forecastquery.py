# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Mapping, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DataPointModel(BaseModel):
    timestamp: Optional[str] = Field(default=None, alias="Timestamp")
    value: Optional[float] = Field(default=None, alias="Value")


class QueryForecastRequestModel(BaseModel):
    forecast_arn: str = Field(alias="ForecastArn")
    filters: Mapping[str, str] = Field(alias="Filters")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class QueryWhatIfForecastRequestModel(BaseModel):
    what_if_forecast_arn: str = Field(alias="WhatIfForecastArn")
    filters: Mapping[str, str] = Field(alias="Filters")
    start_date: Optional[str] = Field(default=None, alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ForecastModel(BaseModel):
    predictions: Optional[Dict[str, List[DataPointModel]]] = Field(
        default=None, alias="Predictions"
    )


class QueryForecastResponseModel(BaseModel):
    forecast: ForecastModel = Field(alias="Forecast")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryWhatIfForecastResponseModel(BaseModel):
    forecast: ForecastModel = Field(alias="Forecast")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
