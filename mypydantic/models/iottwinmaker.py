# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BundleInformationModel(BaseModel):
    bundle_names: List[str] = Field(alias="bundleNames")
    pricing_tier: Optional[Literal["TIER_1", "TIER_2", "TIER_3", "TIER_4"]] = Field(
        default=None, alias="pricingTier"
    )


class ColumnDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["EDGE", "NODE", "VALUE"]] = Field(default=None, alias="type")


class ComponentPropertyGroupRequestModel(BaseModel):
    group_type: Optional[Literal["TABULAR"]] = Field(default=None, alias="groupType")
    property_names: Optional[Sequence[str]] = Field(default=None, alias="propertyNames")
    update_type: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="updateType"
    )


class ComponentPropertyGroupResponseModel(BaseModel):
    group_type: Literal["TABULAR"] = Field(alias="groupType")
    property_names: List[str] = Field(alias="propertyNames")
    is_inherited: bool = Field(alias="isInherited")


class PropertyDefinitionRequestModel(BaseModel):
    data_type: Optional[DataTypeModel] = Field(default=None, alias="dataType")
    is_required_in_entity: Optional[bool] = Field(
        default=None, alias="isRequiredInEntity"
    )
    is_external_id: Optional[bool] = Field(default=None, alias="isExternalId")
    is_stored_externally: Optional[bool] = Field(
        default=None, alias="isStoredExternally"
    )
    is_time_series: Optional[bool] = Field(default=None, alias="isTimeSeries")
    default_value: Optional[DataValueModel] = Field(default=None, alias="defaultValue")
    configuration: Optional[Mapping[str, str]] = Field(
        default=None, alias="configuration"
    )
    display_name: Optional[str] = Field(default=None, alias="displayName")


class PropertyGroupRequestModel(BaseModel):
    group_type: Optional[Literal["TABULAR"]] = Field(default=None, alias="groupType")
    property_names: Optional[Sequence[str]] = Field(default=None, alias="propertyNames")


class CreateSceneRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    scene_id: str = Field(alias="sceneId")
    content_location: str = Field(alias="contentLocation")
    description: Optional[str] = Field(default=None, alias="description")
    capabilities: Optional[Sequence[str]] = Field(default=None, alias="capabilities")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateSyncJobRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    sync_source: str = Field(alias="syncSource")
    sync_role: str = Field(alias="syncRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    s3_location: str = Field(alias="s3Location")
    role: str = Field(alias="role")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class LambdaFunctionModel(BaseModel):
    arn: str = Field(alias="arn")


class RelationshipModel(BaseModel):
    target_component_type_id: Optional[str] = Field(
        default=None, alias="targetComponentTypeId"
    )
    relationship_type: Optional[str] = Field(default=None, alias="relationshipType")


class RelationshipValueModel(BaseModel):
    target_entity_id: Optional[str] = Field(default=None, alias="targetEntityId")
    target_component_name: Optional[str] = Field(
        default=None, alias="targetComponentName"
    )


class DeleteComponentTypeRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    component_type_id: str = Field(alias="componentTypeId")


class DeleteEntityRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    entity_id: str = Field(alias="entityId")
    is_recursive: Optional[bool] = Field(default=None, alias="isRecursive")


class DeleteSceneRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    scene_id: str = Field(alias="sceneId")


class DeleteSyncJobRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    sync_source: str = Field(alias="syncSource")


class DeleteWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class EntityPropertyReferenceModel(BaseModel):
    property_name: str = Field(alias="propertyName")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    external_id_property: Optional[Mapping[str, str]] = Field(
        default=None, alias="externalIdProperty"
    )
    entity_id: Optional[str] = Field(default=None, alias="entityId")


class ErrorDetailsModel(BaseModel):
    code: Optional[
        Literal[
            "INTERNAL_FAILURE",
            "SYNC_CREATING_ERROR",
            "SYNC_INITIALIZING_ERROR",
            "SYNC_PROCESSING_ERROR",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class ExecuteQueryRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    query_statement: str = Field(alias="queryStatement")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RowModel(BaseModel):
    row_data: Optional[List[Dict[str, Any]]] = Field(default=None, alias="rowData")


class GetComponentTypeRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    component_type_id: str = Field(alias="componentTypeId")


class PropertyDefinitionResponseModel(BaseModel):
    data_type: DataTypeModel = Field(alias="dataType")
    is_time_series: bool = Field(alias="isTimeSeries")
    is_required_in_entity: bool = Field(alias="isRequiredInEntity")
    is_external_id: bool = Field(alias="isExternalId")
    is_stored_externally: bool = Field(alias="isStoredExternally")
    is_imported: bool = Field(alias="isImported")
    is_final: bool = Field(alias="isFinal")
    is_inherited: bool = Field(alias="isInherited")
    default_value: Optional[DataValueModel] = Field(default=None, alias="defaultValue")
    configuration: Optional[Dict[str, str]] = Field(default=None, alias="configuration")
    display_name: Optional[str] = Field(default=None, alias="displayName")


class PropertyGroupResponseModel(BaseModel):
    group_type: Literal["TABULAR"] = Field(alias="groupType")
    property_names: List[str] = Field(alias="propertyNames")
    is_inherited: bool = Field(alias="isInherited")


class GetEntityRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    entity_id: str = Field(alias="entityId")


class InterpolationParametersModel(BaseModel):
    interpolation_type: Optional[Literal["LINEAR"]] = Field(
        default=None, alias="interpolationType"
    )
    interval_in_seconds: Optional[int] = Field(default=None, alias="intervalInSeconds")


class PropertyFilterModel(BaseModel):
    property_name: Optional[str] = Field(default=None, alias="propertyName")
    operator: Optional[str] = Field(default=None, alias="operator")
    value: Optional[DataValueModel] = Field(default=None, alias="value")


class GetSceneRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    scene_id: str = Field(alias="sceneId")


class GetSyncJobRequestModel(BaseModel):
    sync_source: str = Field(alias="syncSource")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")


class GetWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")


class ListComponentTypesFilterModel(BaseModel):
    extends_from: Optional[str] = Field(default=None, alias="extendsFrom")
    namespace: Optional[str] = Field(default=None, alias="namespace")
    is_abstract: Optional[bool] = Field(default=None, alias="isAbstract")


class ListEntitiesFilterModel(BaseModel):
    parent_entity_id: Optional[str] = Field(default=None, alias="parentEntityId")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    external_id: Optional[str] = Field(default=None, alias="externalId")


class ListScenesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SceneSummaryModel(BaseModel):
    scene_id: str = Field(alias="sceneId")
    content_location: str = Field(alias="contentLocation")
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    description: Optional[str] = Field(default=None, alias="description")


class ListSyncJobsRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SyncResourceFilterModel(BaseModel):
    state: Optional[
        Literal["DELETED", "ERROR", "INITIALIZING", "IN_SYNC", "PROCESSING"]
    ] = Field(default=None, alias="state")
    resource_type: Optional[Literal["COMPONENT_TYPE", "ENTITY"]] = Field(
        default=None, alias="resourceType"
    )
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    external_id: Optional[str] = Field(default=None, alias="externalId")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListWorkspacesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class WorkspaceSummaryModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    description: Optional[str] = Field(default=None, alias="description")


class OrderByModel(BaseModel):
    property_name: str = Field(alias="propertyName")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="order"
    )


class ParentEntityUpdateRequestModel(BaseModel):
    update_type: Literal["DELETE", "UPDATE"] = Field(alias="updateType")
    parent_entity_id: Optional[str] = Field(default=None, alias="parentEntityId")


class PropertyValueModel(BaseModel):
    value: DataValueModel = Field(alias="value")
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="timestamp")
    time: Optional[str] = Field(default=None, alias="time")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdatePricingPlanRequestModel(BaseModel):
    pricing_mode: Literal["BASIC", "STANDARD", "TIERED_BUNDLE"] = Field(
        alias="pricingMode"
    )
    bundle_names: Optional[Sequence[str]] = Field(default=None, alias="bundleNames")


class UpdateSceneRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    scene_id: str = Field(alias="sceneId")
    content_location: Optional[str] = Field(default=None, alias="contentLocation")
    description: Optional[str] = Field(default=None, alias="description")
    capabilities: Optional[Sequence[str]] = Field(default=None, alias="capabilities")


class UpdateWorkspaceRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    description: Optional[str] = Field(default=None, alias="description")
    role: Optional[str] = Field(default=None, alias="role")


class CreateComponentTypeResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEntityResponseModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSceneResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSyncJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "INITIALIZING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkspaceResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteComponentTypeResponseModel(BaseModel):
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEntityResponseModel(BaseModel):
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSyncJobResponseModel(BaseModel):
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "INITIALIZING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSceneResponseModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    scene_id: str = Field(alias="sceneId")
    content_location: str = Field(alias="contentLocation")
    arn: str = Field(alias="arn")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    description: str = Field(alias="description")
    capabilities: List[str] = Field(alias="capabilities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkspaceResponseModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    s3_location: str = Field(alias="s3Location")
    role: str = Field(alias="role")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateComponentTypeResponseModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    arn: str = Field(alias="arn")
    component_type_id: str = Field(alias="componentTypeId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEntityResponseModel(BaseModel):
    update_date_time: datetime = Field(alias="updateDateTime")
    state: Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSceneResponseModel(BaseModel):
    update_date_time: datetime = Field(alias="updateDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkspaceResponseModel(BaseModel):
    update_date_time: datetime = Field(alias="updateDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PricingPlanModel(BaseModel):
    effective_date_time: datetime = Field(alias="effectiveDateTime")
    pricing_mode: Literal["BASIC", "STANDARD", "TIERED_BUNDLE"] = Field(
        alias="pricingMode"
    )
    update_date_time: datetime = Field(alias="updateDateTime")
    update_reason: Literal[
        "DEFAULT",
        "ENTITY_COUNT_UPDATE",
        "OVERWRITTEN",
        "PRICING_MODE_UPDATE",
        "PRICING_TIER_UPDATE",
    ] = Field(alias="updateReason")
    billable_entity_count: Optional[int] = Field(
        default=None, alias="billableEntityCount"
    )
    bundle_information: Optional[BundleInformationModel] = Field(
        default=None, alias="bundleInformation"
    )


class PropertyRequestModel(BaseModel):
    definition: Optional[PropertyDefinitionRequestModel] = Field(
        default=None, alias="definition"
    )
    value: Optional[DataValueModel] = Field(default=None, alias="value")
    update_type: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="updateType"
    )


class DataConnectorModel(BaseModel):
    lambda_: Optional[LambdaFunctionModel] = Field(default=None, alias="lambda")
    is_native: Optional[bool] = Field(default=None, alias="isNative")


class DataTypeModel(BaseModel):
    type: Literal[
        "BOOLEAN", "DOUBLE", "INTEGER", "LIST", "LONG", "MAP", "RELATIONSHIP", "STRING"
    ] = Field(alias="type")
    nested_type: Optional[Dict[str, Any]] = Field(default=None, alias="nestedType")
    allowed_values: Optional[Sequence[DataValueModel]] = Field(
        default=None, alias="allowedValues"
    )
    unit_of_measure: Optional[str] = Field(default=None, alias="unitOfMeasure")
    relationship: Optional[RelationshipModel] = Field(
        default=None, alias="relationship"
    )


class DataValueModel(BaseModel):
    boolean_value: Optional[bool] = Field(default=None, alias="booleanValue")
    double_value: Optional[float] = Field(default=None, alias="doubleValue")
    integer_value: Optional[int] = Field(default=None, alias="integerValue")
    long_value: Optional[int] = Field(default=None, alias="longValue")
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    list_value: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="listValue"
    )
    map_value: Optional[Mapping[str, Dict[str, Any]]] = Field(
        default=None, alias="mapValue"
    )
    relationship_value: Optional[RelationshipValueModel] = Field(
        default=None, alias="relationshipValue"
    )
    expression: Optional[str] = Field(default=None, alias="expression")


class PropertyLatestValueModel(BaseModel):
    property_reference: EntityPropertyReferenceModel = Field(alias="propertyReference")
    property_value: Optional[DataValueModel] = Field(
        default=None, alias="propertyValue"
    )


class StatusModel(BaseModel):
    state: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"]
    ] = Field(default=None, alias="state")
    error: Optional[ErrorDetailsModel] = Field(default=None, alias="error")


class SyncJobStatusModel(BaseModel):
    state: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "INITIALIZING"]
    ] = Field(default=None, alias="state")
    error: Optional[ErrorDetailsModel] = Field(default=None, alias="error")


class SyncResourceStatusModel(BaseModel):
    state: Optional[
        Literal["DELETED", "ERROR", "INITIALIZING", "IN_SYNC", "PROCESSING"]
    ] = Field(default=None, alias="state")
    error: Optional[ErrorDetailsModel] = Field(default=None, alias="error")


class ExecuteQueryResponseModel(BaseModel):
    column_descriptions: List[ColumnDescriptionModel] = Field(
        alias="columnDescriptions"
    )
    rows: List[RowModel] = Field(alias="rows")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PropertyResponseModel(BaseModel):
    definition: Optional[PropertyDefinitionResponseModel] = Field(
        default=None, alias="definition"
    )
    value: Optional[DataValueModel] = Field(default=None, alias="value")


class GetPropertyValueHistoryRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    selected_properties: Sequence[str] = Field(alias="selectedProperties")
    entity_id: Optional[str] = Field(default=None, alias="entityId")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    property_filters: Optional[Sequence[PropertyFilterModel]] = Field(
        default=None, alias="propertyFilters"
    )
    start_date_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="startDateTime"
    )
    end_date_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="endDateTime"
    )
    interpolation: Optional[InterpolationParametersModel] = Field(
        default=None, alias="interpolation"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    order_by_time: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="orderByTime"
    )
    start_time: Optional[str] = Field(default=None, alias="startTime")
    end_time: Optional[str] = Field(default=None, alias="endTime")


class ListComponentTypesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    filters: Optional[Sequence[ListComponentTypesFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListEntitiesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    filters: Optional[Sequence[ListEntitiesFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListScenesResponseModel(BaseModel):
    scene_summaries: List[SceneSummaryModel] = Field(alias="sceneSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSyncResourcesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    sync_source: str = Field(alias="syncSource")
    filters: Optional[Sequence[SyncResourceFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListWorkspacesResponseModel(BaseModel):
    workspace_summaries: List[WorkspaceSummaryModel] = Field(alias="workspaceSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TabularConditionsModel(BaseModel):
    order_by: Optional[Sequence[OrderByModel]] = Field(default=None, alias="orderBy")
    property_filters: Optional[Sequence[PropertyFilterModel]] = Field(
        default=None, alias="propertyFilters"
    )


class PropertyValueEntryModel(BaseModel):
    entity_property_reference: EntityPropertyReferenceModel = Field(
        alias="entityPropertyReference"
    )
    property_values: Optional[Sequence[PropertyValueModel]] = Field(
        default=None, alias="propertyValues"
    )


class PropertyValueHistoryModel(BaseModel):
    entity_property_reference: EntityPropertyReferenceModel = Field(
        alias="entityPropertyReference"
    )
    values: Optional[List[PropertyValueModel]] = Field(default=None, alias="values")


class GetPricingPlanResponseModel(BaseModel):
    current_pricing_plan: PricingPlanModel = Field(alias="currentPricingPlan")
    pending_pricing_plan: PricingPlanModel = Field(alias="pendingPricingPlan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePricingPlanResponseModel(BaseModel):
    current_pricing_plan: PricingPlanModel = Field(alias="currentPricingPlan")
    pending_pricing_plan: PricingPlanModel = Field(alias="pendingPricingPlan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentRequestModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    properties: Optional[Mapping[str, PropertyRequestModel]] = Field(
        default=None, alias="properties"
    )
    property_groups: Optional[Mapping[str, ComponentPropertyGroupRequestModel]] = Field(
        default=None, alias="propertyGroups"
    )


class ComponentUpdateRequestModel(BaseModel):
    update_type: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="updateType"
    )
    description: Optional[str] = Field(default=None, alias="description")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    property_updates: Optional[Mapping[str, PropertyRequestModel]] = Field(
        default=None, alias="propertyUpdates"
    )
    property_group_updates: Optional[
        Mapping[str, ComponentPropertyGroupRequestModel]
    ] = Field(default=None, alias="propertyGroupUpdates")


class FunctionRequestModel(BaseModel):
    required_properties: Optional[Sequence[str]] = Field(
        default=None, alias="requiredProperties"
    )
    scope: Optional[Literal["ENTITY", "WORKSPACE"]] = Field(default=None, alias="scope")
    implemented_by: Optional[DataConnectorModel] = Field(
        default=None, alias="implementedBy"
    )


class FunctionResponseModel(BaseModel):
    required_properties: Optional[List[str]] = Field(
        default=None, alias="requiredProperties"
    )
    scope: Optional[Literal["ENTITY", "WORKSPACE"]] = Field(default=None, alias="scope")
    implemented_by: Optional[DataConnectorModel] = Field(
        default=None, alias="implementedBy"
    )
    is_inherited: Optional[bool] = Field(default=None, alias="isInherited")


class GetPropertyValueResponseModel(BaseModel):
    property_values: Dict[str, PropertyLatestValueModel] = Field(alias="propertyValues")
    next_token: str = Field(alias="nextToken")
    tabular_property_values: List[List[Dict[str, DataValueModel]]] = Field(
        alias="tabularPropertyValues"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentTypeSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    component_type_id: str = Field(alias="componentTypeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[StatusModel] = Field(default=None, alias="status")
    component_type_name: Optional[str] = Field(default=None, alias="componentTypeName")


class EntitySummaryModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    entity_name: str = Field(alias="entityName")
    arn: str = Field(alias="arn")
    status: StatusModel = Field(alias="status")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    parent_entity_id: Optional[str] = Field(default=None, alias="parentEntityId")
    description: Optional[str] = Field(default=None, alias="description")
    has_child_entities: Optional[bool] = Field(default=None, alias="hasChildEntities")


class GetSyncJobResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    workspace_id: str = Field(alias="workspaceId")
    sync_source: str = Field(alias="syncSource")
    sync_role: str = Field(alias="syncRole")
    status: SyncJobStatusModel = Field(alias="status")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SyncJobSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    sync_source: Optional[str] = Field(default=None, alias="syncSource")
    status: Optional[SyncJobStatusModel] = Field(default=None, alias="status")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    update_date_time: Optional[datetime] = Field(default=None, alias="updateDateTime")


class SyncResourceSummaryModel(BaseModel):
    resource_type: Optional[Literal["COMPONENT_TYPE", "ENTITY"]] = Field(
        default=None, alias="resourceType"
    )
    external_id: Optional[str] = Field(default=None, alias="externalId")
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    status: Optional[SyncResourceStatusModel] = Field(default=None, alias="status")
    update_date_time: Optional[datetime] = Field(default=None, alias="updateDateTime")


class ComponentResponseModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="componentName")
    description: Optional[str] = Field(default=None, alias="description")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    status: Optional[StatusModel] = Field(default=None, alias="status")
    defined_in: Optional[str] = Field(default=None, alias="definedIn")
    properties: Optional[Dict[str, PropertyResponseModel]] = Field(
        default=None, alias="properties"
    )
    property_groups: Optional[Dict[str, ComponentPropertyGroupResponseModel]] = Field(
        default=None, alias="propertyGroups"
    )
    sync_source: Optional[str] = Field(default=None, alias="syncSource")


class GetPropertyValueRequestModel(BaseModel):
    selected_properties: Sequence[str] = Field(alias="selectedProperties")
    workspace_id: str = Field(alias="workspaceId")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_type_id: Optional[str] = Field(default=None, alias="componentTypeId")
    entity_id: Optional[str] = Field(default=None, alias="entityId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    property_group_name: Optional[str] = Field(default=None, alias="propertyGroupName")
    tabular_conditions: Optional[TabularConditionsModel] = Field(
        default=None, alias="tabularConditions"
    )


class BatchPutPropertyErrorModel(BaseModel):
    error_code: str = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    entry: PropertyValueEntryModel = Field(alias="entry")


class BatchPutPropertyValuesRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    entries: Sequence[PropertyValueEntryModel] = Field(alias="entries")


class GetPropertyValueHistoryResponseModel(BaseModel):
    property_values: List[PropertyValueHistoryModel] = Field(alias="propertyValues")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEntityRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    entity_name: str = Field(alias="entityName")
    entity_id: Optional[str] = Field(default=None, alias="entityId")
    description: Optional[str] = Field(default=None, alias="description")
    components: Optional[Mapping[str, ComponentRequestModel]] = Field(
        default=None, alias="components"
    )
    parent_entity_id: Optional[str] = Field(default=None, alias="parentEntityId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateEntityRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    entity_id: str = Field(alias="entityId")
    entity_name: Optional[str] = Field(default=None, alias="entityName")
    description: Optional[str] = Field(default=None, alias="description")
    component_updates: Optional[Mapping[str, ComponentUpdateRequestModel]] = Field(
        default=None, alias="componentUpdates"
    )
    parent_entity_update: Optional[ParentEntityUpdateRequestModel] = Field(
        default=None, alias="parentEntityUpdate"
    )


class CreateComponentTypeRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    component_type_id: str = Field(alias="componentTypeId")
    is_singleton: Optional[bool] = Field(default=None, alias="isSingleton")
    description: Optional[str] = Field(default=None, alias="description")
    property_definitions: Optional[
        Mapping[str, PropertyDefinitionRequestModel]
    ] = Field(default=None, alias="propertyDefinitions")
    extends_from: Optional[Sequence[str]] = Field(default=None, alias="extendsFrom")
    functions: Optional[Mapping[str, FunctionRequestModel]] = Field(
        default=None, alias="functions"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    property_groups: Optional[Mapping[str, PropertyGroupRequestModel]] = Field(
        default=None, alias="propertyGroups"
    )
    component_type_name: Optional[str] = Field(default=None, alias="componentTypeName")


class UpdateComponentTypeRequestModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    component_type_id: str = Field(alias="componentTypeId")
    is_singleton: Optional[bool] = Field(default=None, alias="isSingleton")
    description: Optional[str] = Field(default=None, alias="description")
    property_definitions: Optional[
        Mapping[str, PropertyDefinitionRequestModel]
    ] = Field(default=None, alias="propertyDefinitions")
    extends_from: Optional[Sequence[str]] = Field(default=None, alias="extendsFrom")
    functions: Optional[Mapping[str, FunctionRequestModel]] = Field(
        default=None, alias="functions"
    )
    property_groups: Optional[Mapping[str, PropertyGroupRequestModel]] = Field(
        default=None, alias="propertyGroups"
    )
    component_type_name: Optional[str] = Field(default=None, alias="componentTypeName")


class GetComponentTypeResponseModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    is_singleton: bool = Field(alias="isSingleton")
    component_type_id: str = Field(alias="componentTypeId")
    description: str = Field(alias="description")
    property_definitions: Dict[str, PropertyDefinitionResponseModel] = Field(
        alias="propertyDefinitions"
    )
    extends_from: List[str] = Field(alias="extendsFrom")
    functions: Dict[str, FunctionResponseModel] = Field(alias="functions")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    arn: str = Field(alias="arn")
    is_abstract: bool = Field(alias="isAbstract")
    is_schema_initialized: bool = Field(alias="isSchemaInitialized")
    status: StatusModel = Field(alias="status")
    property_groups: Dict[str, PropertyGroupResponseModel] = Field(
        alias="propertyGroups"
    )
    sync_source: str = Field(alias="syncSource")
    component_type_name: str = Field(alias="componentTypeName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComponentTypesResponseModel(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    component_type_summaries: List[ComponentTypeSummaryModel] = Field(
        alias="componentTypeSummaries"
    )
    next_token: str = Field(alias="nextToken")
    max_results: int = Field(alias="maxResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEntitiesResponseModel(BaseModel):
    entity_summaries: List[EntitySummaryModel] = Field(alias="entitySummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSyncJobsResponseModel(BaseModel):
    sync_job_summaries: List[SyncJobSummaryModel] = Field(alias="syncJobSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSyncResourcesResponseModel(BaseModel):
    sync_resources: List[SyncResourceSummaryModel] = Field(alias="syncResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEntityResponseModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    entity_name: str = Field(alias="entityName")
    arn: str = Field(alias="arn")
    status: StatusModel = Field(alias="status")
    workspace_id: str = Field(alias="workspaceId")
    description: str = Field(alias="description")
    components: Dict[str, ComponentResponseModel] = Field(alias="components")
    parent_entity_id: str = Field(alias="parentEntityId")
    has_child_entities: bool = Field(alias="hasChildEntities")
    creation_date_time: datetime = Field(alias="creationDateTime")
    update_date_time: datetime = Field(alias="updateDateTime")
    sync_source: str = Field(alias="syncSource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutPropertyErrorEntryModel(BaseModel):
    errors: List[BatchPutPropertyErrorModel] = Field(alias="errors")


class BatchPutPropertyValuesResponseModel(BaseModel):
    error_entries: List[BatchPutPropertyErrorEntryModel] = Field(alias="errorEntries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
