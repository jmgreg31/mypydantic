# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AuditEventResultEntryModel(BaseModel):
    event_id: str = Field(alias="eventID")
    id: str = Field(alias="id")


class AuditEventModel(BaseModel):
    event_data: str = Field(alias="eventData")
    id: str = Field(alias="id")
    event_data_checksum: Optional[str] = Field(default=None, alias="eventDataChecksum")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ResultErrorEntryModel(BaseModel):
    error_code: str = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    id: str = Field(alias="id")


class PutAuditEventsRequestModel(BaseModel):
    audit_events: Sequence[AuditEventModel] = Field(alias="auditEvents")
    channel_arn: str = Field(alias="channelArn")
    external_id: Optional[str] = Field(default=None, alias="externalId")


class PutAuditEventsResponseModel(BaseModel):
    failed: List[ResultErrorEntryModel] = Field(alias="failed")
    successful: List[AuditEventResultEntryModel] = Field(alias="successful")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
