# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BundleDetailsModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    title: Optional[str] = Field(default=None, alias="title")
    version: Optional[str] = Field(default=None, alias="version")
    description: Optional[str] = Field(default=None, alias="description")
    icon_url: Optional[str] = Field(default=None, alias="iconUrl")
    available_platforms: Optional[
        List[
            Literal["ANDROID", "JAVASCRIPT", "LINUX", "OBJC", "OSX", "SWIFT", "WINDOWS"]
        ]
    ] = Field(default=None, alias="availablePlatforms")


class CreateProjectRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    region: Optional[str] = Field(default=None, alias="region")
    contents: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="contents"
    )
    snapshot_id: Optional[str] = Field(default=None, alias="snapshotId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")


class ResourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    feature: Optional[str] = Field(default=None, alias="feature")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="attributes")


class DescribeBundleRequestModel(BaseModel):
    bundle_id: str = Field(alias="bundleId")


class DescribeProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    sync_from_resources: Optional[bool] = Field(default=None, alias="syncFromResources")


class ExportBundleRequestModel(BaseModel):
    bundle_id: str = Field(alias="bundleId")
    project_id: Optional[str] = Field(default=None, alias="projectId")
    platform: Optional[
        Literal["ANDROID", "JAVASCRIPT", "LINUX", "OBJC", "OSX", "SWIFT", "WINDOWS"]
    ] = Field(default=None, alias="platform")


class ExportProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBundlesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListProjectsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ProjectSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    project_id: Optional[str] = Field(default=None, alias="projectId")


class UpdateProjectRequestModel(BaseModel):
    project_id: str = Field(alias="projectId")
    contents: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="contents"
    )


class DescribeBundleResultModel(BaseModel):
    details: BundleDetailsModel = Field(alias="details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportBundleResultModel(BaseModel):
    download_url: str = Field(alias="downloadUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportProjectResultModel(BaseModel):
    download_url: str = Field(alias="downloadUrl")
    share_url: str = Field(alias="shareUrl")
    snapshot_id: str = Field(alias="snapshotId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBundlesResultModel(BaseModel):
    bundle_list: List[BundleDetailsModel] = Field(alias="bundleList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectResultModel(BaseModel):
    deleted_resources: List[ResourceModel] = Field(alias="deletedResources")
    orphaned_resources: List[ResourceModel] = Field(alias="orphanedResources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProjectDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    project_id: Optional[str] = Field(default=None, alias="projectId")
    region: Optional[str] = Field(default=None, alias="region")
    state: Optional[Literal["IMPORTING", "NORMAL", "SYNCING"]] = Field(
        default=None, alias="state"
    )
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    console_url: Optional[str] = Field(default=None, alias="consoleUrl")
    resources: Optional[List[ResourceModel]] = Field(default=None, alias="resources")


class ListBundlesRequestListBundlesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsResultModel(BaseModel):
    projects: List[ProjectSummaryModel] = Field(alias="projects")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResultModel(BaseModel):
    details: ProjectDetailsModel = Field(alias="details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProjectResultModel(BaseModel):
    details: ProjectDetailsModel = Field(alias="details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectResultModel(BaseModel):
    details: ProjectDetailsModel = Field(alias="details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
