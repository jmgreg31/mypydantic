# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagQueryConfigurationModel(BaseModel):
    tag_key: Optional[str] = Field(default=None, alias="tagKey")


class ApplicationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class ApplicationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AssociateAttributeGroupRequestModel(BaseModel):
    application: str = Field(alias="application")
    attribute_group: str = Field(alias="attributeGroup")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateResourceRequestModel(BaseModel):
    application: str = Field(alias="application")
    resource_type: Literal["CFN_STACK", "RESOURCE_TAG_VALUE"] = Field(
        alias="resourceType"
    )
    resource: str = Field(alias="resource")


class AttributeGroupDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")


class AttributeGroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")


class AttributeGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateAttributeGroupRequestModel(BaseModel):
    name: str = Field(alias="name")
    attributes: str = Field(alias="attributes")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")


class DeleteAttributeGroupRequestModel(BaseModel):
    attribute_group: str = Field(alias="attributeGroup")


class DisassociateAttributeGroupRequestModel(BaseModel):
    application: str = Field(alias="application")
    attribute_group: str = Field(alias="attributeGroup")


class DisassociateResourceRequestModel(BaseModel):
    application: str = Field(alias="application")
    resource_type: Literal["CFN_STACK", "RESOURCE_TAG_VALUE"] = Field(
        alias="resourceType"
    )
    resource: str = Field(alias="resource")


class GetApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")


class GetAssociatedResourceRequestModel(BaseModel):
    application: str = Field(alias="application")
    resource_type: Literal["CFN_STACK", "RESOURCE_TAG_VALUE"] = Field(
        alias="resourceType"
    )
    resource: str = Field(alias="resource")


class GetAttributeGroupRequestModel(BaseModel):
    attribute_group: str = Field(alias="attributeGroup")


class ResourceGroupModel(BaseModel):
    state: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATING",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="state")
    arn: Optional[str] = Field(default=None, alias="arn")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssociatedAttributeGroupsRequestModel(BaseModel):
    application: str = Field(alias="application")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssociatedResourcesRequestModel(BaseModel):
    application: str = Field(alias="application")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAttributeGroupsForApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAttributeGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ResourceDetailsModel(BaseModel):
    tag_value: Optional[str] = Field(default=None, alias="tagValue")


class SyncResourceRequestModel(BaseModel):
    resource_type: Literal["CFN_STACK", "RESOURCE_TAG_VALUE"] = Field(
        alias="resourceType"
    )
    resource: str = Field(alias="resource")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateApplicationRequestModel(BaseModel):
    application: str = Field(alias="application")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateAttributeGroupRequestModel(BaseModel):
    attribute_group: str = Field(alias="attributeGroup")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    attributes: Optional[str] = Field(default=None, alias="attributes")


class AppRegistryConfigurationModel(BaseModel):
    tag_query_configuration: Optional[TagQueryConfigurationModel] = Field(
        default=None, alias="tagQueryConfiguration"
    )


class AssociateAttributeGroupResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    attribute_group_arn: str = Field(alias="attributeGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResourceResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationResponseModel(BaseModel):
    application: ApplicationModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationResponseModel(BaseModel):
    application: ApplicationSummaryModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateAttributeGroupResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    attribute_group_arn: str = Field(alias="attributeGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResourceResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    resource_arn: str = Field(alias="resourceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAttributeGroupResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    attributes: str = Field(alias="attributes")
    creation_time: datetime = Field(alias="creationTime")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsResponseModel(BaseModel):
    applications: List[ApplicationSummaryModel] = Field(alias="applications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedAttributeGroupsResponseModel(BaseModel):
    attribute_groups: List[str] = Field(alias="attributeGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SyncResourceResponseModel(BaseModel):
    application_arn: str = Field(alias="applicationArn")
    resource_arn: str = Field(alias="resourceArn")
    action_taken: Literal["NO_ACTION", "START_SYNC"] = Field(alias="actionTaken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApplicationResponseModel(BaseModel):
    application: ApplicationModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttributeGroupsForApplicationResponseModel(BaseModel):
    attribute_groups_details: List[AttributeGroupDetailsModel] = Field(
        alias="attributeGroupsDetails"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAttributeGroupResponseModel(BaseModel):
    attribute_group: AttributeGroupSummaryModel = Field(alias="attributeGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttributeGroupsResponseModel(BaseModel):
    attribute_groups: List[AttributeGroupSummaryModel] = Field(alias="attributeGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAttributeGroupResponseModel(BaseModel):
    attribute_group: AttributeGroupModel = Field(alias="attributeGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAttributeGroupResponseModel(BaseModel):
    attribute_group: AttributeGroupModel = Field(alias="attributeGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IntegrationsModel(BaseModel):
    resource_group: Optional[ResourceGroupModel] = Field(
        default=None, alias="resourceGroup"
    )


class ResourceIntegrationsModel(BaseModel):
    resource_group: Optional[ResourceGroupModel] = Field(
        default=None, alias="resourceGroup"
    )


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateModel(
    BaseModel
):
    application: str = Field(alias="application")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociatedResourcesRequestListAssociatedResourcesPaginateModel(BaseModel):
    application: str = Field(alias="application")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttributeGroupsForApplicationRequestListAttributeGroupsForApplicationPaginateModel(
    BaseModel
):
    application: str = Field(alias="application")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttributeGroupsRequestListAttributeGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ResourceInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    resource_type: Optional[Literal["CFN_STACK", "RESOURCE_TAG_VALUE"]] = Field(
        default=None, alias="resourceType"
    )
    resource_details: Optional[ResourceDetailsModel] = Field(
        default=None, alias="resourceDetails"
    )


class GetConfigurationResponseModel(BaseModel):
    configuration: AppRegistryConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConfigurationRequestModel(BaseModel):
    configuration: AppRegistryConfigurationModel = Field(alias="configuration")


class GetApplicationResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    creation_time: datetime = Field(alias="creationTime")
    last_update_time: datetime = Field(alias="lastUpdateTime")
    associated_resource_count: int = Field(alias="associatedResourceCount")
    tags: Dict[str, str] = Field(alias="tags")
    integrations: IntegrationsModel = Field(alias="integrations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    association_time: Optional[datetime] = Field(default=None, alias="associationTime")
    integrations: Optional[ResourceIntegrationsModel] = Field(
        default=None, alias="integrations"
    )


class ListAssociatedResourcesResponseModel(BaseModel):
    resources: List[ResourceInfoModel] = Field(alias="resources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssociatedResourceResponseModel(BaseModel):
    resource: ResourceModel = Field(alias="resource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
