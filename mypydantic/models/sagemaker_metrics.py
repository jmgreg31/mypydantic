# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchPutMetricsErrorModel(BaseModel):
    code: Optional[
        Literal[
            "CONFLICT_ERROR",
            "INTERNAL_ERROR",
            "METRIC_LIMIT_EXCEEDED",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    metric_index: Optional[int] = Field(default=None, alias="MetricIndex")


class RawMetricDataModel(BaseModel):
    metric_name: str = Field(alias="MetricName")
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    value: float = Field(alias="Value")
    step: Optional[int] = Field(default=None, alias="Step")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchPutMetricsRequestModel(BaseModel):
    trial_component_name: str = Field(alias="TrialComponentName")
    metric_data: Sequence[RawMetricDataModel] = Field(alias="MetricData")


class BatchPutMetricsResponseModel(BaseModel):
    errors: List[BatchPutMetricsErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
