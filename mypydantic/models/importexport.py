# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ArtifactModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    url: Optional[str] = Field(default=None, alias="URL")


class CancelJobInputRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateJobInputRequestModel(BaseModel):
    job_type: Literal["Export", "Import"] = Field(alias="JobType")
    manifest: str = Field(alias="Manifest")
    validate_only: bool = Field(alias="ValidateOnly")
    manifest_addendum: Optional[str] = Field(default=None, alias="ManifestAddendum")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class GetShippingLabelInputRequestModel(BaseModel):
    job_ids: Sequence[str] = Field(alias="jobIds")
    name: Optional[str] = Field(default=None, alias="name")
    company: Optional[str] = Field(default=None, alias="company")
    phone_number: Optional[str] = Field(default=None, alias="phoneNumber")
    country: Optional[str] = Field(default=None, alias="country")
    state_or_province: Optional[str] = Field(default=None, alias="stateOrProvince")
    city: Optional[str] = Field(default=None, alias="city")
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    street1: Optional[str] = Field(default=None, alias="street1")
    street2: Optional[str] = Field(default=None, alias="street2")
    street3: Optional[str] = Field(default=None, alias="street3")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class GetStatusInputRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class JobModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    is_canceled: Optional[bool] = Field(default=None, alias="IsCanceled")
    job_type: Optional[Literal["Export", "Import"]] = Field(
        default=None, alias="JobType"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListJobsInputRequestModel(BaseModel):
    max_jobs: Optional[int] = Field(default=None, alias="MaxJobs")
    marker: Optional[str] = Field(default=None, alias="Marker")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class UpdateJobInputRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    manifest: str = Field(alias="Manifest")
    job_type: Literal["Export", "Import"] = Field(alias="JobType")
    validate_only: bool = Field(alias="ValidateOnly")
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")


class CancelJobOutputModel(BaseModel):
    success: bool = Field(alias="Success")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobOutputModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_type: Literal["Export", "Import"] = Field(alias="JobType")
    signature: str = Field(alias="Signature")
    signature_file_contents: str = Field(alias="SignatureFileContents")
    warning_message: str = Field(alias="WarningMessage")
    artifact_list: List[ArtifactModel] = Field(alias="ArtifactList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetShippingLabelOutputModel(BaseModel):
    shipping_label_url: str = Field(alias="ShippingLabelURL")
    warning: str = Field(alias="Warning")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStatusOutputModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_type: Literal["Export", "Import"] = Field(alias="JobType")
    location_code: str = Field(alias="LocationCode")
    location_message: str = Field(alias="LocationMessage")
    progress_code: str = Field(alias="ProgressCode")
    progress_message: str = Field(alias="ProgressMessage")
    carrier: str = Field(alias="Carrier")
    tracking_number: str = Field(alias="TrackingNumber")
    log_bucket: str = Field(alias="LogBucket")
    log_key: str = Field(alias="LogKey")
    error_count: int = Field(alias="ErrorCount")
    signature: str = Field(alias="Signature")
    signature_file_contents: str = Field(alias="SignatureFileContents")
    current_manifest: str = Field(alias="CurrentManifest")
    creation_date: datetime = Field(alias="CreationDate")
    artifact_list: List[ArtifactModel] = Field(alias="ArtifactList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobOutputModel(BaseModel):
    success: bool = Field(alias="Success")
    warning_message: str = Field(alias="WarningMessage")
    artifact_list: List[ArtifactModel] = Field(alias="ArtifactList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsOutputModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    is_truncated: bool = Field(alias="IsTruncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsInputListJobsPaginateModel(BaseModel):
    ap_iversion: Optional[str] = Field(default=None, alias="APIVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )
