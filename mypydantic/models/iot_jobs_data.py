# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DescribeJobExecutionRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    thing_name: str = Field(alias="thingName")
    include_job_document: Optional[bool] = Field(
        default=None, alias="includeJobDocument"
    )
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")


class JobExecutionModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    status_details: Optional[Dict[str, str]] = Field(
        default=None, alias="statusDetails"
    )
    queued_at: Optional[int] = Field(default=None, alias="queuedAt")
    started_at: Optional[int] = Field(default=None, alias="startedAt")
    last_updated_at: Optional[int] = Field(default=None, alias="lastUpdatedAt")
    approximate_seconds_before_timed_out: Optional[int] = Field(
        default=None, alias="approximateSecondsBeforeTimedOut"
    )
    version_number: Optional[int] = Field(default=None, alias="versionNumber")
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")
    job_document: Optional[str] = Field(default=None, alias="jobDocument")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetPendingJobExecutionsRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")


class JobExecutionSummaryModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    queued_at: Optional[int] = Field(default=None, alias="queuedAt")
    started_at: Optional[int] = Field(default=None, alias="startedAt")
    last_updated_at: Optional[int] = Field(default=None, alias="lastUpdatedAt")
    version_number: Optional[int] = Field(default=None, alias="versionNumber")
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")


class JobExecutionStateModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    status_details: Optional[Dict[str, str]] = Field(
        default=None, alias="statusDetails"
    )
    version_number: Optional[int] = Field(default=None, alias="versionNumber")


class StartNextPendingJobExecutionRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    status_details: Optional[Mapping[str, str]] = Field(
        default=None, alias="statusDetails"
    )
    step_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="stepTimeoutInMinutes"
    )


class UpdateJobExecutionRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    thing_name: str = Field(alias="thingName")
    status: Literal[
        "CANCELED",
        "FAILED",
        "IN_PROGRESS",
        "QUEUED",
        "REJECTED",
        "REMOVED",
        "SUCCEEDED",
        "TIMED_OUT",
    ] = Field(alias="status")
    status_details: Optional[Mapping[str, str]] = Field(
        default=None, alias="statusDetails"
    )
    step_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="stepTimeoutInMinutes"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")
    include_job_execution_state: Optional[bool] = Field(
        default=None, alias="includeJobExecutionState"
    )
    include_job_document: Optional[bool] = Field(
        default=None, alias="includeJobDocument"
    )
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")


class DescribeJobExecutionResponseModel(BaseModel):
    execution: JobExecutionModel = Field(alias="execution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartNextPendingJobExecutionResponseModel(BaseModel):
    execution: JobExecutionModel = Field(alias="execution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPendingJobExecutionsResponseModel(BaseModel):
    in_progress_jobs: List[JobExecutionSummaryModel] = Field(alias="inProgressJobs")
    queued_jobs: List[JobExecutionSummaryModel] = Field(alias="queuedJobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobExecutionResponseModel(BaseModel):
    execution_state: JobExecutionStateModel = Field(alias="executionState")
    job_document: str = Field(alias="jobDocument")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
