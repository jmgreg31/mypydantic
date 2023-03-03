# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteReportDefinitionRequestModel(BaseModel):
    report_name: Optional[str] = Field(default=None, alias="ReportName")


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


class DescribeReportDefinitionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ReportDefinitionModel(BaseModel):
    report_name: str = Field(alias="ReportName")
    time_unit: Literal["DAILY", "HOURLY", "MONTHLY"] = Field(alias="TimeUnit")
    format: Literal["Parquet", "textORcsv"] = Field(alias="Format")
    compression: Literal["GZIP", "Parquet", "ZIP"] = Field(alias="Compression")
    additional_schema_elements: List[Literal["RESOURCES"]] = Field(
        alias="AdditionalSchemaElements"
    )
    s3_bucket: str = Field(alias="S3Bucket")
    s3_prefix: str = Field(alias="S3Prefix")
    s3_region: Literal[
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-north-1",
        "eu-south-1",
        "eu-south-2",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-central-1",
        "me-south-1",
        "sa-east-1",
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
    ] = Field(alias="S3Region")
    additional_artifacts: Optional[
        List[Literal["ATHENA", "QUICKSIGHT", "REDSHIFT"]]
    ] = Field(default=None, alias="AdditionalArtifacts")
    refresh_closed_reports: Optional[bool] = Field(
        default=None, alias="RefreshClosedReports"
    )
    report_versioning: Optional[
        Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"]
    ] = Field(default=None, alias="ReportVersioning")
    billing_view_arn: Optional[str] = Field(default=None, alias="BillingViewArn")


class DeleteReportDefinitionResponseModel(BaseModel):
    response_message: str = Field(alias="ResponseMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReportDefinitionsResponseModel(BaseModel):
    report_definitions: List[ReportDefinitionModel] = Field(alias="ReportDefinitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyReportDefinitionRequestModel(BaseModel):
    report_name: str = Field(alias="ReportName")
    report_definition: ReportDefinitionModel = Field(alias="ReportDefinition")


class PutReportDefinitionRequestModel(BaseModel):
    report_definition: ReportDefinitionModel = Field(alias="ReportDefinition")
