# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddRegionActionModel(BaseModel):
    region_name: str = Field(alias="regionName")
    sse_kms_key_id: Optional[str] = Field(default=None, alias="sseKmsKeyId")


class AttributeValueListModel(BaseModel):
    integer_values: Optional[Sequence[int]] = Field(default=None, alias="integerValues")
    string_values: Optional[Sequence[str]] = Field(default=None, alias="stringValues")


class AutomationExecutionModel(BaseModel):
    ssm_execution_arn: Optional[str] = Field(default=None, alias="ssmExecutionArn")


class ChatChannelModel(BaseModel):
    chatbot_sns: Optional[Sequence[str]] = Field(default=None, alias="chatbotSns")
    empty: Optional[Mapping[str, Any]] = Field(default=None, alias="empty")


class RegionMapInputValueModel(BaseModel):
    sse_kms_key_id: Optional[str] = Field(default=None, alias="sseKmsKeyId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EventReferenceModel(BaseModel):
    related_item_id: Optional[str] = Field(default=None, alias="relatedItemId")
    resource: Optional[str] = Field(default=None, alias="resource")


class DeleteIncidentRecordInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteRegionActionModel(BaseModel):
    region_name: str = Field(alias="regionName")


class DeleteReplicationSetInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteResourcePolicyInputRequestModel(BaseModel):
    policy_id: str = Field(alias="policyId")
    resource_arn: str = Field(alias="resourceArn")


class DeleteResponsePlanInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteTimelineEventInputRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    incident_record_arn: str = Field(alias="incidentRecordArn")


class DynamicSsmParameterValueModel(BaseModel):
    variable: Optional[Literal["INCIDENT_RECORD_ARN", "INVOLVED_RESOURCES"]] = Field(
        default=None, alias="variable"
    )


class GetIncidentRecordInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetReplicationSetInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetResourcePoliciesInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ResourcePolicyModel(BaseModel):
    policy_document: str = Field(alias="policyDocument")
    policy_id: str = Field(alias="policyId")
    ram_resource_share_region: str = Field(alias="ramResourceShareRegion")


class GetResponsePlanInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetTimelineEventInputRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    incident_record_arn: str = Field(alias="incidentRecordArn")


class IncidentRecordSourceModel(BaseModel):
    created_by: str = Field(alias="createdBy")
    source: str = Field(alias="source")
    invoked_by: Optional[str] = Field(default=None, alias="invokedBy")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")


class NotificationTargetItemModel(BaseModel):
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicArn")


class PagerDutyIncidentDetailModel(BaseModel):
    id: str = Field(alias="id")
    auto_resolve: Optional[bool] = Field(default=None, alias="autoResolve")
    secret_id: Optional[str] = Field(default=None, alias="secretId")


class ListRelatedItemsInputRequestModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListReplicationSetsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListResponsePlansInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ResponsePlanSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    display_name: Optional[str] = Field(default=None, alias="displayName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PagerDutyIncidentConfigurationModel(BaseModel):
    service_id: str = Field(alias="serviceId")


class PutResourcePolicyInputRequestModel(BaseModel):
    policy: str = Field(alias="policy")
    resource_arn: str = Field(alias="resourceArn")


class RegionInfoModel(BaseModel):
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="status")
    status_update_date_time: datetime = Field(alias="statusUpdateDateTime")
    sse_kms_key_id: Optional[str] = Field(default=None, alias="sseKmsKeyId")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class TriggerDetailsModel(BaseModel):
    source: str = Field(alias="source")
    timestamp: Union[datetime, str] = Field(alias="timestamp")
    raw_data: Optional[str] = Field(default=None, alias="rawData")
    trigger_arn: Optional[str] = Field(default=None, alias="triggerArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateDeletionProtectionInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    deletion_protected: bool = Field(alias="deletionProtected")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ConditionModel(BaseModel):
    after: Optional[Union[datetime, str]] = Field(default=None, alias="after")
    before: Optional[Union[datetime, str]] = Field(default=None, alias="before")
    equals: Optional[AttributeValueListModel] = Field(default=None, alias="equals")


class CreateReplicationSetInputRequestModel(BaseModel):
    regions: Mapping[str, RegionMapInputValueModel] = Field(alias="regions")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateReplicationSetOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResponsePlanOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTimelineEventOutputModel(BaseModel):
    event_id: str = Field(alias="eventId")
    incident_record_arn: str = Field(alias="incidentRecordArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReplicationSetsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    replication_set_arns: List[str] = Field(alias="replicationSetArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyOutputModel(BaseModel):
    policy_id: str = Field(alias="policyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartIncidentOutputModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTimelineEventInputRequestModel(BaseModel):
    event_data: str = Field(alias="eventData")
    event_time: Union[datetime, str] = Field(alias="eventTime")
    event_type: str = Field(alias="eventType")
    incident_record_arn: str = Field(alias="incidentRecordArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    event_references: Optional[Sequence[EventReferenceModel]] = Field(
        default=None, alias="eventReferences"
    )


class EventSummaryModel(BaseModel):
    event_id: str = Field(alias="eventId")
    event_time: datetime = Field(alias="eventTime")
    event_type: str = Field(alias="eventType")
    event_updated_time: datetime = Field(alias="eventUpdatedTime")
    incident_record_arn: str = Field(alias="incidentRecordArn")
    event_references: Optional[List[EventReferenceModel]] = Field(
        default=None, alias="eventReferences"
    )


class TimelineEventModel(BaseModel):
    event_data: str = Field(alias="eventData")
    event_id: str = Field(alias="eventId")
    event_time: datetime = Field(alias="eventTime")
    event_type: str = Field(alias="eventType")
    event_updated_time: datetime = Field(alias="eventUpdatedTime")
    incident_record_arn: str = Field(alias="incidentRecordArn")
    event_references: Optional[List[EventReferenceModel]] = Field(
        default=None, alias="eventReferences"
    )


class UpdateTimelineEventInputRequestModel(BaseModel):
    event_id: str = Field(alias="eventId")
    incident_record_arn: str = Field(alias="incidentRecordArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    event_data: Optional[str] = Field(default=None, alias="eventData")
    event_references: Optional[Sequence[EventReferenceModel]] = Field(
        default=None, alias="eventReferences"
    )
    event_time: Optional[Union[datetime, str]] = Field(default=None, alias="eventTime")
    event_type: Optional[str] = Field(default=None, alias="eventType")


class UpdateReplicationSetActionModel(BaseModel):
    add_region_action: Optional[AddRegionActionModel] = Field(
        default=None, alias="addRegionAction"
    )
    delete_region_action: Optional[DeleteRegionActionModel] = Field(
        default=None, alias="deleteRegionAction"
    )


class SsmAutomationModel(BaseModel):
    document_name: str = Field(alias="documentName")
    role_arn: str = Field(alias="roleArn")
    document_version: Optional[str] = Field(default=None, alias="documentVersion")
    dynamic_parameters: Optional[Mapping[str, DynamicSsmParameterValueModel]] = Field(
        default=None, alias="dynamicParameters"
    )
    parameters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="parameters"
    )
    target_account: Optional[
        Literal["IMPACTED_ACCOUNT", "RESPONSE_PLAN_OWNER_ACCOUNT"]
    ] = Field(default=None, alias="targetAccount")


class GetReplicationSetInputWaitForReplicationSetActiveWaitModel(BaseModel):
    arn: str = Field(alias="arn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetReplicationSetInputWaitForReplicationSetDeletedWaitModel(BaseModel):
    arn: str = Field(alias="arn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetResourcePoliciesInputGetResourcePoliciesPaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRelatedItemsInputListRelatedItemsPaginateModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReplicationSetsInputListReplicationSetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResponsePlansInputListResponsePlansPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourcePoliciesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resource_policies: List[ResourcePolicyModel] = Field(alias="resourcePolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IncidentRecordSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    impact: int = Field(alias="impact")
    incident_record_source: IncidentRecordSourceModel = Field(
        alias="incidentRecordSource"
    )
    status: Literal["OPEN", "RESOLVED"] = Field(alias="status")
    title: str = Field(alias="title")
    resolved_time: Optional[datetime] = Field(default=None, alias="resolvedTime")


class IncidentRecordModel(BaseModel):
    arn: str = Field(alias="arn")
    creation_time: datetime = Field(alias="creationTime")
    dedupe_string: str = Field(alias="dedupeString")
    impact: int = Field(alias="impact")
    incident_record_source: IncidentRecordSourceModel = Field(
        alias="incidentRecordSource"
    )
    last_modified_by: str = Field(alias="lastModifiedBy")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    status: Literal["OPEN", "RESOLVED"] = Field(alias="status")
    title: str = Field(alias="title")
    automation_executions: Optional[List[AutomationExecutionModel]] = Field(
        default=None, alias="automationExecutions"
    )
    chat_channel: Optional[ChatChannelModel] = Field(default=None, alias="chatChannel")
    notification_targets: Optional[List[NotificationTargetItemModel]] = Field(
        default=None, alias="notificationTargets"
    )
    resolved_time: Optional[datetime] = Field(default=None, alias="resolvedTime")
    summary: Optional[str] = Field(default=None, alias="summary")


class IncidentTemplateModel(BaseModel):
    impact: int = Field(alias="impact")
    title: str = Field(alias="title")
    dedupe_string: Optional[str] = Field(default=None, alias="dedupeString")
    incident_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="incidentTags"
    )
    notification_targets: Optional[Sequence[NotificationTargetItemModel]] = Field(
        default=None, alias="notificationTargets"
    )
    summary: Optional[str] = Field(default=None, alias="summary")


class UpdateIncidentRecordInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    chat_channel: Optional[ChatChannelModel] = Field(default=None, alias="chatChannel")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    impact: Optional[int] = Field(default=None, alias="impact")
    notification_targets: Optional[Sequence[NotificationTargetItemModel]] = Field(
        default=None, alias="notificationTargets"
    )
    status: Optional[Literal["OPEN", "RESOLVED"]] = Field(default=None, alias="status")
    summary: Optional[str] = Field(default=None, alias="summary")
    title: Optional[str] = Field(default=None, alias="title")


class ItemValueModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    metric_definition: Optional[str] = Field(default=None, alias="metricDefinition")
    pager_duty_incident_detail: Optional[PagerDutyIncidentDetailModel] = Field(
        default=None, alias="pagerDutyIncidentDetail"
    )
    url: Optional[str] = Field(default=None, alias="url")


class ListResponsePlansOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    response_plan_summaries: List[ResponsePlanSummaryModel] = Field(
        alias="responsePlanSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PagerDutyConfigurationModel(BaseModel):
    name: str = Field(alias="name")
    pager_duty_incident_configuration: PagerDutyIncidentConfigurationModel = Field(
        alias="pagerDutyIncidentConfiguration"
    )
    secret_id: str = Field(alias="secretId")


class ReplicationSetModel(BaseModel):
    created_by: str = Field(alias="createdBy")
    created_time: datetime = Field(alias="createdTime")
    deletion_protected: bool = Field(alias="deletionProtected")
    last_modified_by: str = Field(alias="lastModifiedBy")
    last_modified_time: datetime = Field(alias="lastModifiedTime")
    region_map: Dict[str, RegionInfoModel] = Field(alias="regionMap")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="status"
    )
    arn: Optional[str] = Field(default=None, alias="arn")


class FilterModel(BaseModel):
    condition: ConditionModel = Field(alias="condition")
    key: str = Field(alias="key")


class ListTimelineEventsOutputModel(BaseModel):
    event_summaries: List[EventSummaryModel] = Field(alias="eventSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTimelineEventOutputModel(BaseModel):
    event: TimelineEventModel = Field(alias="event")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReplicationSetInputRequestModel(BaseModel):
    actions: Sequence[UpdateReplicationSetActionModel] = Field(alias="actions")
    arn: str = Field(alias="arn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ActionModel(BaseModel):
    ssm_automation: Optional[SsmAutomationModel] = Field(
        default=None, alias="ssmAutomation"
    )


class ListIncidentRecordsOutputModel(BaseModel):
    incident_record_summaries: List[IncidentRecordSummaryModel] = Field(
        alias="incidentRecordSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIncidentRecordOutputModel(BaseModel):
    incident_record: IncidentRecordModel = Field(alias="incidentRecord")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ItemIdentifierModel(BaseModel):
    type: Literal[
        "ANALYSIS",
        "ATTACHMENT",
        "AUTOMATION",
        "INCIDENT",
        "INVOLVED_RESOURCE",
        "METRIC",
        "OTHER",
        "PARENT",
        "TASK",
    ] = Field(alias="type")
    value: ItemValueModel = Field(alias="value")


class IntegrationModel(BaseModel):
    pager_duty_configuration: Optional[PagerDutyConfigurationModel] = Field(
        default=None, alias="pagerDutyConfiguration"
    )


class GetReplicationSetOutputModel(BaseModel):
    replication_set: ReplicationSetModel = Field(alias="replicationSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIncidentRecordsInputListIncidentRecordsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIncidentRecordsInputRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTimelineEventsInputListTimelineEventsPaginateModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    sort_by: Optional[Literal["EVENT_TIME"]] = Field(default=None, alias="sortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTimelineEventsInputRequestModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_by: Optional[Literal["EVENT_TIME"]] = Field(default=None, alias="sortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortOrder"
    )


class RelatedItemModel(BaseModel):
    identifier: ItemIdentifierModel = Field(alias="identifier")
    generated_id: Optional[str] = Field(default=None, alias="generatedId")
    title: Optional[str] = Field(default=None, alias="title")


class CreateResponsePlanInputRequestModel(BaseModel):
    incident_template: IncidentTemplateModel = Field(alias="incidentTemplate")
    name: str = Field(alias="name")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="actions")
    chat_channel: Optional[ChatChannelModel] = Field(default=None, alias="chatChannel")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    engagements: Optional[Sequence[str]] = Field(default=None, alias="engagements")
    integrations: Optional[Sequence[IntegrationModel]] = Field(
        default=None, alias="integrations"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetResponsePlanOutputModel(BaseModel):
    actions: List[ActionModel] = Field(alias="actions")
    arn: str = Field(alias="arn")
    chat_channel: ChatChannelModel = Field(alias="chatChannel")
    display_name: str = Field(alias="displayName")
    engagements: List[str] = Field(alias="engagements")
    incident_template: IncidentTemplateModel = Field(alias="incidentTemplate")
    integrations: List[IntegrationModel] = Field(alias="integrations")
    name: str = Field(alias="name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResponsePlanInputRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="actions")
    chat_channel: Optional[ChatChannelModel] = Field(default=None, alias="chatChannel")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    engagements: Optional[Sequence[str]] = Field(default=None, alias="engagements")
    incident_template_dedupe_string: Optional[str] = Field(
        default=None, alias="incidentTemplateDedupeString"
    )
    incident_template_impact: Optional[int] = Field(
        default=None, alias="incidentTemplateImpact"
    )
    incident_template_notification_targets: Optional[
        Sequence[NotificationTargetItemModel]
    ] = Field(default=None, alias="incidentTemplateNotificationTargets")
    incident_template_summary: Optional[str] = Field(
        default=None, alias="incidentTemplateSummary"
    )
    incident_template_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="incidentTemplateTags"
    )
    incident_template_title: Optional[str] = Field(
        default=None, alias="incidentTemplateTitle"
    )
    integrations: Optional[Sequence[IntegrationModel]] = Field(
        default=None, alias="integrations"
    )


class ListRelatedItemsOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    related_items: List[RelatedItemModel] = Field(alias="relatedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RelatedItemsUpdateModel(BaseModel):
    item_to_add: Optional[RelatedItemModel] = Field(default=None, alias="itemToAdd")
    item_to_remove: Optional[ItemIdentifierModel] = Field(
        default=None, alias="itemToRemove"
    )


class StartIncidentInputRequestModel(BaseModel):
    response_plan_arn: str = Field(alias="responsePlanArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    impact: Optional[int] = Field(default=None, alias="impact")
    related_items: Optional[Sequence[RelatedItemModel]] = Field(
        default=None, alias="relatedItems"
    )
    title: Optional[str] = Field(default=None, alias="title")
    trigger_details: Optional[TriggerDetailsModel] = Field(
        default=None, alias="triggerDetails"
    )


class UpdateRelatedItemsInputRequestModel(BaseModel):
    incident_record_arn: str = Field(alias="incidentRecordArn")
    related_items_update: RelatedItemsUpdateModel = Field(alias="relatedItemsUpdate")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
