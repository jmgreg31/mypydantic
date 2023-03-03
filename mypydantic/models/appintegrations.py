# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ScheduleConfigurationModel(BaseModel):
    first_execution_from: Optional[str] = Field(
        default=None, alias="FirstExecutionFrom"
    )
    object: Optional[str] = Field(default=None, alias="Object")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EventFilterModel(BaseModel):
    source: str = Field(alias="Source")


class DataIntegrationAssociationSummaryModel(BaseModel):
    data_integration_association_arn: Optional[str] = Field(
        default=None, alias="DataIntegrationAssociationArn"
    )
    data_integration_arn: Optional[str] = Field(
        default=None, alias="DataIntegrationArn"
    )
    client_id: Optional[str] = Field(default=None, alias="ClientId")


class DataIntegrationSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    source_uri: Optional[str] = Field(default=None, alias="SourceURI")


class DeleteDataIntegrationRequestModel(BaseModel):
    data_integration_identifier: str = Field(alias="DataIntegrationIdentifier")


class DeleteEventIntegrationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class EventIntegrationAssociationModel(BaseModel):
    event_integration_association_arn: Optional[str] = Field(
        default=None, alias="EventIntegrationAssociationArn"
    )
    event_integration_association_id: Optional[str] = Field(
        default=None, alias="EventIntegrationAssociationId"
    )
    event_integration_name: Optional[str] = Field(
        default=None, alias="EventIntegrationName"
    )
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    event_bridge_rule_name: Optional[str] = Field(
        default=None, alias="EventBridgeRuleName"
    )
    client_association_metadata: Optional[Dict[str, str]] = Field(
        default=None, alias="ClientAssociationMetadata"
    )


class GetDataIntegrationRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetEventIntegrationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ListDataIntegrationAssociationsRequestModel(BaseModel):
    data_integration_identifier: str = Field(alias="DataIntegrationIdentifier")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataIntegrationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEventIntegrationAssociationsRequestModel(BaseModel):
    event_integration_name: str = Field(alias="EventIntegrationName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEventIntegrationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateDataIntegrationRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateEventIntegrationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateDataIntegrationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key: Optional[str] = Field(default=None, alias="KmsKey")
    source_uri: Optional[str] = Field(default=None, alias="SourceURI")
    schedule_config: Optional[ScheduleConfigurationModel] = Field(
        default=None, alias="ScheduleConfig"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateDataIntegrationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    kms_key: str = Field(alias="KmsKey")
    source_uri: str = Field(alias="SourceURI")
    schedule_configuration: ScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    client_token: str = Field(alias="ClientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventIntegrationResponseModel(BaseModel):
    event_integration_arn: str = Field(alias="EventIntegrationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataIntegrationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    kms_key: str = Field(alias="KmsKey")
    source_uri: str = Field(alias="SourceURI")
    schedule_configuration: ScheduleConfigurationModel = Field(
        alias="ScheduleConfiguration"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEventIntegrationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    event_filter: EventFilterModel = Field(alias="EventFilter")
    event_bridge_bus: str = Field(alias="EventBridgeBus")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class EventIntegrationModel(BaseModel):
    event_integration_arn: Optional[str] = Field(
        default=None, alias="EventIntegrationArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    event_filter: Optional[EventFilterModel] = Field(default=None, alias="EventFilter")
    event_bridge_bus: Optional[str] = Field(default=None, alias="EventBridgeBus")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetEventIntegrationResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    event_integration_arn: str = Field(alias="EventIntegrationArn")
    event_bridge_bus: str = Field(alias="EventBridgeBus")
    event_filter: EventFilterModel = Field(alias="EventFilter")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataIntegrationAssociationsResponseModel(BaseModel):
    data_integration_associations: List[DataIntegrationAssociationSummaryModel] = Field(
        alias="DataIntegrationAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataIntegrationsResponseModel(BaseModel):
    data_integrations: List[DataIntegrationSummaryModel] = Field(
        alias="DataIntegrations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventIntegrationAssociationsResponseModel(BaseModel):
    event_integration_associations: List[EventIntegrationAssociationModel] = Field(
        alias="EventIntegrationAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventIntegrationsResponseModel(BaseModel):
    event_integrations: List[EventIntegrationModel] = Field(alias="EventIntegrations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
