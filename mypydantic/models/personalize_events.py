# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class MetricAttributionModel(BaseModel):
    event_attribution_source: str = Field(alias="eventAttributionSource")


class ItemModel(BaseModel):
    item_id: str = Field(alias="itemId")
    properties: Optional[str] = Field(default=None, alias="properties")


class UserModel(BaseModel):
    user_id: str = Field(alias="userId")
    properties: Optional[str] = Field(default=None, alias="properties")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventModel(BaseModel):
    event_type: str = Field(alias="eventType")
    sent_at: Union[datetime, str] = Field(alias="sentAt")
    event_id: Optional[str] = Field(default=None, alias="eventId")
    event_value: Optional[float] = Field(default=None, alias="eventValue")
    item_id: Optional[str] = Field(default=None, alias="itemId")
    properties: Optional[str] = Field(default=None, alias="properties")
    recommendation_id: Optional[str] = Field(default=None, alias="recommendationId")
    impression: Optional[Sequence[str]] = Field(default=None, alias="impression")
    metric_attribution: Optional[MetricAttributionModel] = Field(
        default=None, alias="metricAttribution"
    )


class PutItemsRequestModel(BaseModel):
    dataset_arn: str = Field(alias="datasetArn")
    items: Sequence[ItemModel] = Field(alias="items")


class PutUsersRequestModel(BaseModel):
    dataset_arn: str = Field(alias="datasetArn")
    users: Sequence[UserModel] = Field(alias="users")


class PutEventsRequestModel(BaseModel):
    tracking_id: str = Field(alias="trackingId")
    session_id: str = Field(alias="sessionId")
    event_list: Sequence[EventModel] = Field(alias="eventList")
    user_id: Optional[str] = Field(default=None, alias="userId")
