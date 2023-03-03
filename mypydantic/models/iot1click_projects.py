# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateDeviceWithPlacementRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    placement_name: str = Field(alias="placementName")
    device_id: str = Field(alias="deviceId")
    device_template_name: str = Field(alias="deviceTemplateName")


class CreatePlacementRequestModel(BaseModel):
    placement_name: str = Field(alias="placementName")
    project_name: str = Field(alias="projectName")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")


class DeletePlacementRequestModel(BaseModel):
    placement_name: str = Field(alias="placementName")
    project_name: str = Field(alias="projectName")


class DeleteProjectRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")


class DescribePlacementRequestModel(BaseModel):
    placement_name: str = Field(alias="placementName")
    project_name: str = Field(alias="projectName")


class PlacementDescriptionModel(BaseModel):
    project_name: str = Field(alias="projectName")
    placement_name: str = Field(alias="placementName")
    attributes: Dict[str, str] = Field(alias="attributes")
    created_date: datetime = Field(alias="createdDate")
    updated_date: datetime = Field(alias="updatedDate")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeProjectRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")


class DeviceTemplateModel(BaseModel):
    device_type: Optional[str] = Field(default=None, alias="deviceType")
    callback_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="callbackOverrides"
    )


class DisassociateDeviceFromPlacementRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    placement_name: str = Field(alias="placementName")
    device_template_name: str = Field(alias="deviceTemplateName")


class GetDevicesInPlacementRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    placement_name: str = Field(alias="placementName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListPlacementsRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PlacementSummaryModel(BaseModel):
    project_name: str = Field(alias="projectName")
    placement_name: str = Field(alias="placementName")
    created_date: datetime = Field(alias="createdDate")
    updated_date: datetime = Field(alias="updatedDate")


class ListProjectsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ProjectSummaryModel(BaseModel):
    project_name: str = Field(alias="projectName")
    created_date: datetime = Field(alias="createdDate")
    updated_date: datetime = Field(alias="updatedDate")
    arn: Optional[str] = Field(default=None, alias="arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdatePlacementRequestModel(BaseModel):
    placement_name: str = Field(alias="placementName")
    project_name: str = Field(alias="projectName")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")


class DescribePlacementResponseModel(BaseModel):
    placement: PlacementDescriptionModel = Field(alias="placement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevicesInPlacementResponseModel(BaseModel):
    devices: Dict[str, str] = Field(alias="devices")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PlacementTemplateModel(BaseModel):
    default_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="defaultAttributes"
    )
    device_templates: Optional[Mapping[str, DeviceTemplateModel]] = Field(
        default=None, alias="deviceTemplates"
    )


class ListPlacementsRequestListPlacementsPaginateModel(BaseModel):
    project_name: str = Field(alias="projectName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlacementsResponseModel(BaseModel):
    placements: List[PlacementSummaryModel] = Field(alias="placements")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsResponseModel(BaseModel):
    projects: List[ProjectSummaryModel] = Field(alias="projects")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    description: Optional[str] = Field(default=None, alias="description")
    placement_template: Optional[PlacementTemplateModel] = Field(
        default=None, alias="placementTemplate"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ProjectDescriptionModel(BaseModel):
    project_name: str = Field(alias="projectName")
    created_date: datetime = Field(alias="createdDate")
    updated_date: datetime = Field(alias="updatedDate")
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")
    placement_template: Optional[PlacementTemplateModel] = Field(
        default=None, alias="placementTemplate"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateProjectRequestModel(BaseModel):
    project_name: str = Field(alias="projectName")
    description: Optional[str] = Field(default=None, alias="description")
    placement_template: Optional[PlacementTemplateModel] = Field(
        default=None, alias="placementTemplate"
    )


class DescribeProjectResponseModel(BaseModel):
    project: ProjectDescriptionModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
