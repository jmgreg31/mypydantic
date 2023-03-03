# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateEntityToThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    entity_id: str = Field(alias="entityId")
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")


class DefinitionDocumentModel(BaseModel):
    language: Literal["GRAPHQL"] = Field(alias="language")
    text: str = Field(alias="text")


class FlowTemplateSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    revision_number: Optional[int] = Field(default=None, alias="revisionNumber")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class MetricsConfigurationModel(BaseModel):
    cloud_metric_enabled: Optional[bool] = Field(
        default=None, alias="cloudMetricEnabled"
    )
    metric_rule_role_arn: Optional[str] = Field(default=None, alias="metricRuleRoleArn")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class SystemInstanceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[
        Literal[
            "BOOTSTRAP",
            "DELETED_IN_TARGET",
            "DEPLOYED_IN_TARGET",
            "DEPLOY_IN_PROGRESS",
            "FAILED",
            "NOT_DEPLOYED",
            "PENDING_DELETE",
            "UNDEPLOY_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="status")
    target: Optional[Literal["CLOUD", "GREENGRASS"]] = Field(
        default=None, alias="target"
    )
    greengrass_group_name: Optional[str] = Field(
        default=None, alias="greengrassGroupName"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    greengrass_group_id: Optional[str] = Field(default=None, alias="greengrassGroupId")
    greengrass_group_version_id: Optional[str] = Field(
        default=None, alias="greengrassGroupVersionId"
    )


class SystemTemplateSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    revision_number: Optional[int] = Field(default=None, alias="revisionNumber")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class DeleteFlowTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteSystemInstanceRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")


class DeleteSystemTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DependencyRevisionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    revision_number: Optional[int] = Field(default=None, alias="revisionNumber")


class DeploySystemInstanceRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")


class DeprecateFlowTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeprecateSystemTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DescribeNamespaceRequestModel(BaseModel):
    namespace_name: Optional[str] = Field(default=None, alias="namespaceName")


class DissociateEntityFromThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    entity_type: Literal[
        "ACTION",
        "CAPABILITY",
        "DEVICE",
        "DEVICE_MODEL",
        "ENUM",
        "EVENT",
        "MAPPING",
        "PROPERTY",
        "SERVICE",
        "STATE",
    ] = Field(alias="entityType")


class EntityFilterModel(BaseModel):
    name: Optional[
        Literal["NAME", "NAMESPACE", "REFERENCED_ENTITY_ID", "SEMANTIC_TYPE_PATH"]
    ] = Field(default=None, alias="name")
    value: Optional[Sequence[str]] = Field(default=None, alias="value")


class FlowExecutionMessageModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="messageId")
    event_type: Optional[
        Literal[
            "ACKNOWLEDGE_TASK_MESSAGE",
            "ACTIVITY_FAILED",
            "ACTIVITY_SCHEDULED",
            "ACTIVITY_STARTED",
            "ACTIVITY_SUCCEEDED",
            "EXECUTION_ABORTED",
            "EXECUTION_FAILED",
            "EXECUTION_STARTED",
            "EXECUTION_SUCCEEDED",
            "SCHEDULE_NEXT_READY_STEPS_TASK",
            "START_FLOW_EXECUTION_TASK",
            "STEP_FAILED",
            "STEP_STARTED",
            "STEP_SUCCEEDED",
            "THING_ACTION_TASK",
            "THING_ACTION_TASK_FAILED",
            "THING_ACTION_TASK_SUCCEEDED",
        ]
    ] = Field(default=None, alias="eventType")
    timestamp: Optional[datetime] = Field(default=None, alias="timestamp")
    payload: Optional[str] = Field(default=None, alias="payload")


class FlowExecutionSummaryModel(BaseModel):
    flow_execution_id: Optional[str] = Field(default=None, alias="flowExecutionId")
    status: Optional[Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="status"
    )
    system_instance_id: Optional[str] = Field(default=None, alias="systemInstanceId")
    flow_template_id: Optional[str] = Field(default=None, alias="flowTemplateId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class FlowTemplateFilterModel(BaseModel):
    name: Literal["DEVICE_MODEL_ID"] = Field(alias="name")
    value: Sequence[str] = Field(alias="value")


class GetEntitiesRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")


class GetFlowTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    revision_number: Optional[int] = Field(default=None, alias="revisionNumber")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetFlowTemplateRevisionsRequestModel(BaseModel):
    id: str = Field(alias="id")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetSystemInstanceRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetSystemTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    revision_number: Optional[int] = Field(default=None, alias="revisionNumber")


class GetSystemTemplateRevisionsRequestModel(BaseModel):
    id: str = Field(alias="id")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetUploadStatusRequestModel(BaseModel):
    upload_id: str = Field(alias="uploadId")


class ListFlowExecutionMessagesRequestModel(BaseModel):
    flow_execution_id: str = Field(alias="flowExecutionId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchFlowExecutionsRequestModel(BaseModel):
    system_instance_id: str = Field(alias="systemInstanceId")
    flow_execution_id: Optional[str] = Field(default=None, alias="flowExecutionId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SystemInstanceFilterModel(BaseModel):
    name: Optional[
        Literal["GREENGRASS_GROUP_NAME", "STATUS", "SYSTEM_TEMPLATE_ID"]
    ] = Field(default=None, alias="name")
    value: Optional[Sequence[str]] = Field(default=None, alias="value")


class SystemTemplateFilterModel(BaseModel):
    name: Literal["FLOW_TEMPLATE_ID"] = Field(alias="name")
    value: Sequence[str] = Field(alias="value")


class SearchThingsRequestModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")


class ThingModel(BaseModel):
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    thing_name: Optional[str] = Field(default=None, alias="thingName")


class UndeploySystemInstanceRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CreateFlowTemplateRequestModel(BaseModel):
    definition: DefinitionDocumentModel = Field(alias="definition")
    compatible_namespace_version: Optional[int] = Field(
        default=None, alias="compatibleNamespaceVersion"
    )


class CreateSystemTemplateRequestModel(BaseModel):
    definition: DefinitionDocumentModel = Field(alias="definition")
    compatible_namespace_version: Optional[int] = Field(
        default=None, alias="compatibleNamespaceVersion"
    )


class EntityDescriptionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[
        Literal[
            "ACTION",
            "CAPABILITY",
            "DEVICE",
            "DEVICE_MODEL",
            "ENUM",
            "EVENT",
            "MAPPING",
            "PROPERTY",
            "SERVICE",
            "STATE",
        ]
    ] = Field(default=None, alias="type")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    definition: Optional[DefinitionDocumentModel] = Field(
        default=None, alias="definition"
    )


class UpdateFlowTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    definition: DefinitionDocumentModel = Field(alias="definition")
    compatible_namespace_version: Optional[int] = Field(
        default=None, alias="compatibleNamespaceVersion"
    )


class UpdateSystemTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    definition: DefinitionDocumentModel = Field(alias="definition")
    compatible_namespace_version: Optional[int] = Field(
        default=None, alias="compatibleNamespaceVersion"
    )


class UploadEntityDefinitionsRequestModel(BaseModel):
    document: Optional[DefinitionDocumentModel] = Field(default=None, alias="document")
    sync_with_public_namespace: Optional[bool] = Field(
        default=None, alias="syncWithPublicNamespace"
    )
    deprecate_existing_entities: Optional[bool] = Field(
        default=None, alias="deprecateExistingEntities"
    )


class FlowTemplateDescriptionModel(BaseModel):
    summary: Optional[FlowTemplateSummaryModel] = Field(default=None, alias="summary")
    definition: Optional[DefinitionDocumentModel] = Field(
        default=None, alias="definition"
    )
    validated_namespace_version: Optional[int] = Field(
        default=None, alias="validatedNamespaceVersion"
    )


class CreateFlowTemplateResponseModel(BaseModel):
    summary: FlowTemplateSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNamespaceResponseModel(BaseModel):
    namespace_arn: str = Field(alias="namespaceArn")
    namespace_name: str = Field(alias="namespaceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNamespaceResponseModel(BaseModel):
    namespace_arn: str = Field(alias="namespaceArn")
    namespace_name: str = Field(alias="namespaceName")
    tracking_namespace_name: str = Field(alias="trackingNamespaceName")
    tracking_namespace_version: int = Field(alias="trackingNamespaceVersion")
    namespace_version: int = Field(alias="namespaceVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFlowTemplateRevisionsResponseModel(BaseModel):
    summaries: List[FlowTemplateSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNamespaceDeletionStatusResponseModel(BaseModel):
    namespace_arn: str = Field(alias="namespaceArn")
    namespace_name: str = Field(alias="namespaceName")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="status")
    error_code: Literal["VALIDATION_FAILED"] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUploadStatusResponseModel(BaseModel):
    upload_id: str = Field(alias="uploadId")
    upload_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="uploadStatus"
    )
    namespace_arn: str = Field(alias="namespaceArn")
    namespace_name: str = Field(alias="namespaceName")
    namespace_version: int = Field(alias="namespaceVersion")
    failure_reason: List[str] = Field(alias="failureReason")
    created_date: datetime = Field(alias="createdDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchFlowTemplatesResponseModel(BaseModel):
    summaries: List[FlowTemplateSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowTemplateResponseModel(BaseModel):
    summary: FlowTemplateSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UploadEntityDefinitionsResponseModel(BaseModel):
    upload_id: str = Field(alias="uploadId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSystemInstanceRequestModel(BaseModel):
    definition: DefinitionDocumentModel = Field(alias="definition")
    target: Literal["CLOUD", "GREENGRASS"] = Field(alias="target")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    greengrass_group_name: Optional[str] = Field(
        default=None, alias="greengrassGroupName"
    )
    s3_bucket_name: Optional[str] = Field(default=None, alias="s3BucketName")
    metrics_configuration: Optional[MetricsConfigurationModel] = Field(
        default=None, alias="metricsConfiguration"
    )
    flow_actions_role_arn: Optional[str] = Field(
        default=None, alias="flowActionsRoleArn"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateSystemInstanceResponseModel(BaseModel):
    summary: SystemInstanceSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploySystemInstanceResponseModel(BaseModel):
    summary: SystemInstanceSummaryModel = Field(alias="summary")
    greengrass_deployment_id: str = Field(alias="greengrassDeploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchSystemInstancesResponseModel(BaseModel):
    summaries: List[SystemInstanceSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UndeploySystemInstanceResponseModel(BaseModel):
    summary: SystemInstanceSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSystemTemplateResponseModel(BaseModel):
    summary: SystemTemplateSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSystemTemplateRevisionsResponseModel(BaseModel):
    summaries: List[SystemTemplateSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchSystemTemplatesResponseModel(BaseModel):
    summaries: List[SystemTemplateSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SystemTemplateDescriptionModel(BaseModel):
    summary: Optional[SystemTemplateSummaryModel] = Field(default=None, alias="summary")
    definition: Optional[DefinitionDocumentModel] = Field(
        default=None, alias="definition"
    )
    validated_namespace_version: Optional[int] = Field(
        default=None, alias="validatedNamespaceVersion"
    )


class UpdateSystemTemplateResponseModel(BaseModel):
    summary: SystemTemplateSummaryModel = Field(alias="summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SystemInstanceDescriptionModel(BaseModel):
    summary: Optional[SystemInstanceSummaryModel] = Field(default=None, alias="summary")
    definition: Optional[DefinitionDocumentModel] = Field(
        default=None, alias="definition"
    )
    s3_bucket_name: Optional[str] = Field(default=None, alias="s3BucketName")
    metrics_configuration: Optional[MetricsConfigurationModel] = Field(
        default=None, alias="metricsConfiguration"
    )
    validated_namespace_version: Optional[int] = Field(
        default=None, alias="validatedNamespaceVersion"
    )
    validated_dependency_revisions: Optional[List[DependencyRevisionModel]] = Field(
        default=None, alias="validatedDependencyRevisions"
    )
    flow_actions_role_arn: Optional[str] = Field(
        default=None, alias="flowActionsRoleArn"
    )


class SearchEntitiesRequestModel(BaseModel):
    entity_types: Sequence[
        Literal[
            "ACTION",
            "CAPABILITY",
            "DEVICE",
            "DEVICE_MODEL",
            "ENUM",
            "EVENT",
            "MAPPING",
            "PROPERTY",
            "SERVICE",
            "STATE",
        ]
    ] = Field(alias="entityTypes")
    filters: Optional[Sequence[EntityFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")


class ListFlowExecutionMessagesResponseModel(BaseModel):
    messages: List[FlowExecutionMessageModel] = Field(alias="messages")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchFlowExecutionsResponseModel(BaseModel):
    summaries: List[FlowExecutionSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchFlowTemplatesRequestModel(BaseModel):
    filters: Optional[Sequence[FlowTemplateFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateModel(BaseModel):
    id: str = Field(alias="id")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateModel(
    BaseModel
):
    id: str = Field(alias="id")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateModel(BaseModel):
    flow_execution_id: str = Field(alias="flowExecutionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchEntitiesRequestSearchEntitiesPaginateModel(BaseModel):
    entity_types: Sequence[
        Literal[
            "ACTION",
            "CAPABILITY",
            "DEVICE",
            "DEVICE_MODEL",
            "ENUM",
            "EVENT",
            "MAPPING",
            "PROPERTY",
            "SERVICE",
            "STATE",
        ]
    ] = Field(alias="entityTypes")
    filters: Optional[Sequence[EntityFilterModel]] = Field(
        default=None, alias="filters"
    )
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchFlowExecutionsRequestSearchFlowExecutionsPaginateModel(BaseModel):
    system_instance_id: str = Field(alias="systemInstanceId")
    flow_execution_id: Optional[str] = Field(default=None, alias="flowExecutionId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchFlowTemplatesRequestSearchFlowTemplatesPaginateModel(BaseModel):
    filters: Optional[Sequence[FlowTemplateFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchThingsRequestSearchThingsPaginateModel(BaseModel):
    entity_id: str = Field(alias="entityId")
    namespace_version: Optional[int] = Field(default=None, alias="namespaceVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSystemInstancesRequestModel(BaseModel):
    filters: Optional[Sequence[SystemInstanceFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SearchSystemInstancesRequestSearchSystemInstancesPaginateModel(BaseModel):
    filters: Optional[Sequence[SystemInstanceFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSystemTemplatesRequestModel(BaseModel):
    filters: Optional[Sequence[SystemTemplateFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SearchSystemTemplatesRequestSearchSystemTemplatesPaginateModel(BaseModel):
    filters: Optional[Sequence[SystemTemplateFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchThingsResponseModel(BaseModel):
    things: List[ThingModel] = Field(alias="things")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEntitiesResponseModel(BaseModel):
    descriptions: List[EntityDescriptionModel] = Field(alias="descriptions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchEntitiesResponseModel(BaseModel):
    descriptions: List[EntityDescriptionModel] = Field(alias="descriptions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFlowTemplateResponseModel(BaseModel):
    description: FlowTemplateDescriptionModel = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSystemTemplateResponseModel(BaseModel):
    description: SystemTemplateDescriptionModel = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSystemInstanceResponseModel(BaseModel):
    description: SystemInstanceDescriptionModel = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
