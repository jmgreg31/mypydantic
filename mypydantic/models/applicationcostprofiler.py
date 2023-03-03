# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteReportDefinitionRequestModel(BaseModel):
    report_id: str = Field(alias="reportId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetReportDefinitionRequestModel(BaseModel):
    report_id: str = Field(alias="reportId")


class S3LocationModel(BaseModel):
    bucket: str = Field(alias="bucket")
    prefix: str = Field(alias="prefix")


class SourceS3LocationModel(BaseModel):
    bucket: str = Field(alias="bucket")
    key: str = Field(alias="key")
    region: Optional[
        Literal["af-south-1", "ap-east-1", "eu-south-1", "me-south-1"]
    ] = Field(default=None, alias="region")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListReportDefinitionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DeleteReportDefinitionResultModel(BaseModel):
    report_id: str = Field(alias="reportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportApplicationUsageResultModel(BaseModel):
    import_id: str = Field(alias="importId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutReportDefinitionResultModel(BaseModel):
    report_id: str = Field(alias="reportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReportDefinitionResultModel(BaseModel):
    report_id: str = Field(alias="reportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReportDefinitionResultModel(BaseModel):
    report_id: str = Field(alias="reportId")
    report_description: str = Field(alias="reportDescription")
    report_frequency: Literal["ALL", "DAILY", "MONTHLY"] = Field(
        alias="reportFrequency"
    )
    format: Literal["CSV", "PARQUET"] = Field(alias="format")
    destination_s3_location: S3LocationModel = Field(alias="destinationS3Location")
    created_at: datetime = Field(alias="createdAt")
    last_updated: datetime = Field(alias="lastUpdated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutReportDefinitionRequestModel(BaseModel):
    report_id: str = Field(alias="reportId")
    report_description: str = Field(alias="reportDescription")
    report_frequency: Literal["ALL", "DAILY", "MONTHLY"] = Field(
        alias="reportFrequency"
    )
    format: Literal["CSV", "PARQUET"] = Field(alias="format")
    destination_s3_location: S3LocationModel = Field(alias="destinationS3Location")


class ReportDefinitionModel(BaseModel):
    report_id: Optional[str] = Field(default=None, alias="reportId")
    report_description: Optional[str] = Field(default=None, alias="reportDescription")
    report_frequency: Optional[Literal["ALL", "DAILY", "MONTHLY"]] = Field(
        default=None, alias="reportFrequency"
    )
    format: Optional[Literal["CSV", "PARQUET"]] = Field(default=None, alias="format")
    destination_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="destinationS3Location"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class UpdateReportDefinitionRequestModel(BaseModel):
    report_id: str = Field(alias="reportId")
    report_description: str = Field(alias="reportDescription")
    report_frequency: Literal["ALL", "DAILY", "MONTHLY"] = Field(
        alias="reportFrequency"
    )
    format: Literal["CSV", "PARQUET"] = Field(alias="format")
    destination_s3_location: S3LocationModel = Field(alias="destinationS3Location")


class ImportApplicationUsageRequestModel(BaseModel):
    source_s3_location: SourceS3LocationModel = Field(alias="sourceS3Location")


class ListReportDefinitionsRequestListReportDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReportDefinitionsResultModel(BaseModel):
    report_definitions: List[ReportDefinitionModel] = Field(alias="reportDefinitions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
