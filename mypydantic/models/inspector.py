# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttributeModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class FailedItemDetailsModel(BaseModel):
    failure_code: Literal[
        "ACCESS_DENIED",
        "DUPLICATE_ARN",
        "INTERNAL_ERROR",
        "INVALID_ARN",
        "ITEM_DOES_NOT_EXIST",
        "LIMIT_EXCEEDED",
    ] = Field(alias="failureCode")
    retryable: bool = Field(alias="retryable")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AgentFilterModel(BaseModel):
    agent_healths: Sequence[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        alias="agentHealths"
    )
    agent_health_codes: Sequence[
        Literal["IDLE", "RUNNING", "SHUTDOWN", "THROTTLED", "UNHEALTHY", "UNKNOWN"]
    ] = Field(alias="agentHealthCodes")


class AgentPreviewModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    auto_scaling_group: Optional[str] = Field(default=None, alias="autoScalingGroup")
    agent_health: Optional[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        default=None, alias="agentHealth"
    )
    agent_version: Optional[str] = Field(default=None, alias="agentVersion")
    operating_system: Optional[str] = Field(default=None, alias="operatingSystem")
    kernel_version: Optional[str] = Field(default=None, alias="kernelVersion")
    ipv4_address: Optional[str] = Field(default=None, alias="ipv4Address")


class TelemetryMetadataModel(BaseModel):
    message_type: str = Field(alias="messageType")
    count: int = Field(alias="count")
    data_size: Optional[int] = Field(default=None, alias="dataSize")


class DurationRangeModel(BaseModel):
    min_seconds: Optional[int] = Field(default=None, alias="minSeconds")
    max_seconds: Optional[int] = Field(default=None, alias="maxSeconds")


class TimestampRangeModel(BaseModel):
    begin_date: Optional[Union[datetime, str]] = Field(default=None, alias="beginDate")
    end_date: Optional[Union[datetime, str]] = Field(default=None, alias="endDate")


class AssessmentRunNotificationModel(BaseModel):
    date: datetime = Field(alias="date")
    event: Literal[
        "ASSESSMENT_RUN_COMPLETED",
        "ASSESSMENT_RUN_STARTED",
        "ASSESSMENT_RUN_STATE_CHANGED",
        "FINDING_REPORTED",
        "OTHER",
    ] = Field(alias="event")
    error: bool = Field(alias="error")
    message: Optional[str] = Field(default=None, alias="message")
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicArn")
    sns_publish_status_code: Optional[
        Literal["ACCESS_DENIED", "INTERNAL_ERROR", "SUCCESS", "TOPIC_DOES_NOT_EXIST"]
    ] = Field(default=None, alias="snsPublishStatusCode")


class AssessmentRunStateChangeModel(BaseModel):
    state_changed_at: datetime = Field(alias="stateChangedAt")
    state: Literal[
        "CANCELED",
        "COLLECTING_DATA",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "CREATED",
        "DATA_COLLECTED",
        "ERROR",
        "EVALUATING_RULES",
        "FAILED",
        "START_DATA_COLLECTION_IN_PROGRESS",
        "START_DATA_COLLECTION_PENDING",
        "START_EVALUATING_RULES_PENDING",
        "STOP_DATA_COLLECTION_PENDING",
    ] = Field(alias="state")


class AssessmentTargetFilterModel(BaseModel):
    assessment_target_name_pattern: Optional[str] = Field(
        default=None, alias="assessmentTargetNamePattern"
    )


class AssessmentTargetModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    resource_group_arn: Optional[str] = Field(default=None, alias="resourceGroupArn")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class CreateAssessmentTargetRequestModel(BaseModel):
    assessment_target_name: str = Field(alias="assessmentTargetName")
    resource_group_arn: Optional[str] = Field(default=None, alias="resourceGroupArn")


class CreateExclusionsPreviewRequestModel(BaseModel):
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")


class ResourceGroupTagModel(BaseModel):
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class DeleteAssessmentRunRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")


class DeleteAssessmentTargetRequestModel(BaseModel):
    assessment_target_arn: str = Field(alias="assessmentTargetArn")


class DeleteAssessmentTemplateRequestModel(BaseModel):
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")


class DescribeAssessmentRunsRequestModel(BaseModel):
    assessment_run_arns: Sequence[str] = Field(alias="assessmentRunArns")


class DescribeAssessmentTargetsRequestModel(BaseModel):
    assessment_target_arns: Sequence[str] = Field(alias="assessmentTargetArns")


class DescribeAssessmentTemplatesRequestModel(BaseModel):
    assessment_template_arns: Sequence[str] = Field(alias="assessmentTemplateArns")


class DescribeExclusionsRequestModel(BaseModel):
    exclusion_arns: Sequence[str] = Field(alias="exclusionArns")
    locale: Optional[Literal["EN_US"]] = Field(default=None, alias="locale")


class DescribeFindingsRequestModel(BaseModel):
    finding_arns: Sequence[str] = Field(alias="findingArns")
    locale: Optional[Literal["EN_US"]] = Field(default=None, alias="locale")


class DescribeResourceGroupsRequestModel(BaseModel):
    resource_group_arns: Sequence[str] = Field(alias="resourceGroupArns")


class DescribeRulesPackagesRequestModel(BaseModel):
    rules_package_arns: Sequence[str] = Field(alias="rulesPackageArns")
    locale: Optional[Literal["EN_US"]] = Field(default=None, alias="locale")


class RulesPackageModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    provider: str = Field(alias="provider")
    description: Optional[str] = Field(default=None, alias="description")


class EventSubscriptionModel(BaseModel):
    event: Literal[
        "ASSESSMENT_RUN_COMPLETED",
        "ASSESSMENT_RUN_STARTED",
        "ASSESSMENT_RUN_STATE_CHANGED",
        "FINDING_REPORTED",
        "OTHER",
    ] = Field(alias="event")
    subscribed_at: datetime = Field(alias="subscribedAt")


class ScopeModel(BaseModel):
    key: Optional[Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"]] = Field(
        default=None, alias="key"
    )
    value: Optional[str] = Field(default=None, alias="value")


class InspectorServiceAttributesModel(BaseModel):
    schema_version: int = Field(alias="schemaVersion")
    assessment_run_arn: Optional[str] = Field(default=None, alias="assessmentRunArn")
    rules_package_arn: Optional[str] = Field(default=None, alias="rulesPackageArn")


class GetAssessmentReportRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    report_file_format: Literal["HTML", "PDF"] = Field(alias="reportFileFormat")
    report_type: Literal["FINDING", "FULL"] = Field(alias="reportType")


class GetExclusionsPreviewRequestModel(BaseModel):
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")
    preview_token: str = Field(alias="previewToken")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    locale: Optional[Literal["EN_US"]] = Field(default=None, alias="locale")


class GetTelemetryMetadataRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEventSubscriptionsRequestModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListExclusionsRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListRulesPackagesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PrivateIpModel(BaseModel):
    private_dns_name: Optional[str] = Field(default=None, alias="privateDnsName")
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")


class SecurityGroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="groupName")
    group_id: Optional[str] = Field(default=None, alias="groupId")


class PreviewAgentsRequestModel(BaseModel):
    preview_agents_arn: str = Field(alias="previewAgentsArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RegisterCrossAccountAccessRoleRequestModel(BaseModel):
    role_arn: str = Field(alias="roleArn")


class RemoveAttributesFromFindingsRequestModel(BaseModel):
    finding_arns: Sequence[str] = Field(alias="findingArns")
    attribute_keys: Sequence[str] = Field(alias="attributeKeys")


class StartAssessmentRunRequestModel(BaseModel):
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")
    assessment_run_name: Optional[str] = Field(default=None, alias="assessmentRunName")


class StopAssessmentRunRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    stop_action: Optional[Literal["SKIP_EVALUATION", "START_EVALUATION"]] = Field(
        default=None, alias="stopAction"
    )


class SubscribeToEventRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    event: Literal[
        "ASSESSMENT_RUN_COMPLETED",
        "ASSESSMENT_RUN_STARTED",
        "ASSESSMENT_RUN_STATE_CHANGED",
        "FINDING_REPORTED",
        "OTHER",
    ] = Field(alias="event")
    topic_arn: str = Field(alias="topicArn")


class UnsubscribeFromEventRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    event: Literal[
        "ASSESSMENT_RUN_COMPLETED",
        "ASSESSMENT_RUN_STARTED",
        "ASSESSMENT_RUN_STATE_CHANGED",
        "FINDING_REPORTED",
        "OTHER",
    ] = Field(alias="event")
    topic_arn: str = Field(alias="topicArn")


class UpdateAssessmentTargetRequestModel(BaseModel):
    assessment_target_arn: str = Field(alias="assessmentTargetArn")
    assessment_target_name: str = Field(alias="assessmentTargetName")
    resource_group_arn: Optional[str] = Field(default=None, alias="resourceGroupArn")


class AddAttributesToFindingsRequestModel(BaseModel):
    finding_arns: Sequence[str] = Field(alias="findingArns")
    attributes: Sequence[AttributeModel] = Field(alias="attributes")


class AssessmentTemplateModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    assessment_target_arn: str = Field(alias="assessmentTargetArn")
    duration_in_seconds: int = Field(alias="durationInSeconds")
    rules_package_arns: List[str] = Field(alias="rulesPackageArns")
    user_attributes_for_findings: List[AttributeModel] = Field(
        alias="userAttributesForFindings"
    )
    assessment_run_count: int = Field(alias="assessmentRunCount")
    created_at: datetime = Field(alias="createdAt")
    last_assessment_run_arn: Optional[str] = Field(
        default=None, alias="lastAssessmentRunArn"
    )


class CreateAssessmentTemplateRequestModel(BaseModel):
    assessment_target_arn: str = Field(alias="assessmentTargetArn")
    assessment_template_name: str = Field(alias="assessmentTemplateName")
    duration_in_seconds: int = Field(alias="durationInSeconds")
    rules_package_arns: Sequence[str] = Field(alias="rulesPackageArns")
    user_attributes_for_findings: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="userAttributesForFindings"
    )


class AddAttributesToFindingsResponseModel(BaseModel):
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssessmentTargetResponseModel(BaseModel):
    assessment_target_arn: str = Field(alias="assessmentTargetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssessmentTemplateResponseModel(BaseModel):
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExclusionsPreviewResponseModel(BaseModel):
    preview_token: str = Field(alias="previewToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceGroupResponseModel(BaseModel):
    resource_group_arn: str = Field(alias="resourceGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCrossAccountAccessRoleResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    valid: bool = Field(alias="valid")
    registered_at: datetime = Field(alias="registeredAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssessmentReportResponseModel(BaseModel):
    status: Literal["COMPLETED", "FAILED", "WORK_IN_PROGRESS"] = Field(alias="status")
    url: str = Field(alias="url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentRunsResponseModel(BaseModel):
    assessment_run_arns: List[str] = Field(alias="assessmentRunArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentTargetsResponseModel(BaseModel):
    assessment_target_arns: List[str] = Field(alias="assessmentTargetArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentTemplatesResponseModel(BaseModel):
    assessment_template_arns: List[str] = Field(alias="assessmentTemplateArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExclusionsResponseModel(BaseModel):
    exclusion_arns: List[str] = Field(alias="exclusionArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsResponseModel(BaseModel):
    finding_arns: List[str] = Field(alias="findingArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRulesPackagesResponseModel(BaseModel):
    rules_package_arns: List[str] = Field(alias="rulesPackageArns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveAttributesFromFindingsResponseModel(BaseModel):
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAssessmentRunResponseModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentRunAgentsRequestModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    filter: Optional[AgentFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PreviewAgentsResponseModel(BaseModel):
    agent_previews: List[AgentPreviewModel] = Field(alias="agentPreviews")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentRunAgentModel(BaseModel):
    agent_id: str = Field(alias="agentId")
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    agent_health: Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"] = Field(
        alias="agentHealth"
    )
    agent_health_code: Literal[
        "IDLE", "RUNNING", "SHUTDOWN", "THROTTLED", "UNHEALTHY", "UNKNOWN"
    ] = Field(alias="agentHealthCode")
    telemetry_metadata: List[TelemetryMetadataModel] = Field(alias="telemetryMetadata")
    agent_health_details: Optional[str] = Field(
        default=None, alias="agentHealthDetails"
    )
    auto_scaling_group: Optional[str] = Field(default=None, alias="autoScalingGroup")


class GetTelemetryMetadataResponseModel(BaseModel):
    telemetry_metadata: List[TelemetryMetadataModel] = Field(alias="telemetryMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentTemplateFilterModel(BaseModel):
    name_pattern: Optional[str] = Field(default=None, alias="namePattern")
    duration_range: Optional[DurationRangeModel] = Field(
        default=None, alias="durationRange"
    )
    rules_package_arns: Optional[Sequence[str]] = Field(
        default=None, alias="rulesPackageArns"
    )


class AssessmentRunFilterModel(BaseModel):
    name_pattern: Optional[str] = Field(default=None, alias="namePattern")
    states: Optional[
        Sequence[
            Literal[
                "CANCELED",
                "COLLECTING_DATA",
                "COMPLETED",
                "COMPLETED_WITH_ERRORS",
                "CREATED",
                "DATA_COLLECTED",
                "ERROR",
                "EVALUATING_RULES",
                "FAILED",
                "START_DATA_COLLECTION_IN_PROGRESS",
                "START_DATA_COLLECTION_PENDING",
                "START_EVALUATING_RULES_PENDING",
                "STOP_DATA_COLLECTION_PENDING",
            ]
        ]
    ] = Field(default=None, alias="states")
    duration_range: Optional[DurationRangeModel] = Field(
        default=None, alias="durationRange"
    )
    rules_package_arns: Optional[Sequence[str]] = Field(
        default=None, alias="rulesPackageArns"
    )
    start_time_range: Optional[TimestampRangeModel] = Field(
        default=None, alias="startTimeRange"
    )
    completion_time_range: Optional[TimestampRangeModel] = Field(
        default=None, alias="completionTimeRange"
    )
    state_change_time_range: Optional[TimestampRangeModel] = Field(
        default=None, alias="stateChangeTimeRange"
    )


class FindingFilterModel(BaseModel):
    agent_ids: Optional[Sequence[str]] = Field(default=None, alias="agentIds")
    auto_scaling_groups: Optional[Sequence[str]] = Field(
        default=None, alias="autoScalingGroups"
    )
    rule_names: Optional[Sequence[str]] = Field(default=None, alias="ruleNames")
    severities: Optional[
        Sequence[Literal["High", "Informational", "Low", "Medium", "Undefined"]]
    ] = Field(default=None, alias="severities")
    rules_package_arns: Optional[Sequence[str]] = Field(
        default=None, alias="rulesPackageArns"
    )
    attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="attributes"
    )
    user_attributes: Optional[Sequence[AttributeModel]] = Field(
        default=None, alias="userAttributes"
    )
    creation_time_range: Optional[TimestampRangeModel] = Field(
        default=None, alias="creationTimeRange"
    )


class AssessmentRunModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    assessment_template_arn: str = Field(alias="assessmentTemplateArn")
    state: Literal[
        "CANCELED",
        "COLLECTING_DATA",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "CREATED",
        "DATA_COLLECTED",
        "ERROR",
        "EVALUATING_RULES",
        "FAILED",
        "START_DATA_COLLECTION_IN_PROGRESS",
        "START_DATA_COLLECTION_PENDING",
        "START_EVALUATING_RULES_PENDING",
        "STOP_DATA_COLLECTION_PENDING",
    ] = Field(alias="state")
    duration_in_seconds: int = Field(alias="durationInSeconds")
    rules_package_arns: List[str] = Field(alias="rulesPackageArns")
    user_attributes_for_findings: List[AttributeModel] = Field(
        alias="userAttributesForFindings"
    )
    created_at: datetime = Field(alias="createdAt")
    state_changed_at: datetime = Field(alias="stateChangedAt")
    data_collected: bool = Field(alias="dataCollected")
    state_changes: List[AssessmentRunStateChangeModel] = Field(alias="stateChanges")
    notifications: List[AssessmentRunNotificationModel] = Field(alias="notifications")
    finding_counts: Dict[
        Literal["High", "Informational", "Low", "Medium", "Undefined"], int
    ] = Field(alias="findingCounts")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    completed_at: Optional[datetime] = Field(default=None, alias="completedAt")


class ListAssessmentTargetsRequestModel(BaseModel):
    filter: Optional[AssessmentTargetFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeAssessmentTargetsResponseModel(BaseModel):
    assessment_targets: List[AssessmentTargetModel] = Field(alias="assessmentTargets")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateResourceGroupRequestModel(BaseModel):
    resource_group_tags: Sequence[ResourceGroupTagModel] = Field(
        alias="resourceGroupTags"
    )


class ResourceGroupModel(BaseModel):
    arn: str = Field(alias="arn")
    tags: List[ResourceGroupTagModel] = Field(alias="tags")
    created_at: datetime = Field(alias="createdAt")


class DescribeRulesPackagesResponseModel(BaseModel):
    rules_packages: List[RulesPackageModel] = Field(alias="rulesPackages")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscriptionModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    topic_arn: str = Field(alias="topicArn")
    event_subscriptions: List[EventSubscriptionModel] = Field(
        alias="eventSubscriptions"
    )


class ExclusionPreviewModel(BaseModel):
    title: str = Field(alias="title")
    description: str = Field(alias="description")
    recommendation: str = Field(alias="recommendation")
    scopes: List[ScopeModel] = Field(alias="scopes")
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="attributes")


class ExclusionModel(BaseModel):
    arn: str = Field(alias="arn")
    title: str = Field(alias="title")
    description: str = Field(alias="description")
    recommendation: str = Field(alias="recommendation")
    scopes: List[ScopeModel] = Field(alias="scopes")
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="attributes")


class ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    filter: Optional[AgentFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssessmentTargetsRequestListAssessmentTargetsPaginateModel(BaseModel):
    filter: Optional[AssessmentTargetFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventSubscriptionsRequestListEventSubscriptionsPaginateModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExclusionsRequestListExclusionsPaginateModel(BaseModel):
    assessment_run_arn: str = Field(alias="assessmentRunArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesPackagesRequestListRulesPackagesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PreviewAgentsRequestPreviewAgentsPaginateModel(BaseModel):
    preview_agents_arn: str = Field(alias="previewAgentsArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class NetworkInterfaceModel(BaseModel):
    network_interface_id: Optional[str] = Field(
        default=None, alias="networkInterfaceId"
    )
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    private_dns_name: Optional[str] = Field(default=None, alias="privateDnsName")
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")
    private_ip_addresses: Optional[List[PrivateIpModel]] = Field(
        default=None, alias="privateIpAddresses"
    )
    public_dns_name: Optional[str] = Field(default=None, alias="publicDnsName")
    public_ip: Optional[str] = Field(default=None, alias="publicIp")
    ipv6_addresses: Optional[List[str]] = Field(default=None, alias="ipv6Addresses")
    security_groups: Optional[List[SecurityGroupModel]] = Field(
        default=None, alias="securityGroups"
    )


class DescribeAssessmentTemplatesResponseModel(BaseModel):
    assessment_templates: List[AssessmentTemplateModel] = Field(
        alias="assessmentTemplates"
    )
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentRunAgentsResponseModel(BaseModel):
    assessment_run_agents: List[AssessmentRunAgentModel] = Field(
        alias="assessmentRunAgents"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateModel(BaseModel):
    assessment_target_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentTargetArns"
    )
    filter: Optional[AssessmentTemplateFilterModel] = Field(
        default=None, alias="filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssessmentTemplatesRequestModel(BaseModel):
    assessment_target_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentTargetArns"
    )
    filter: Optional[AssessmentTemplateFilterModel] = Field(
        default=None, alias="filter"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssessmentRunsRequestListAssessmentRunsPaginateModel(BaseModel):
    assessment_template_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentTemplateArns"
    )
    filter: Optional[AssessmentRunFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssessmentRunsRequestModel(BaseModel):
    assessment_template_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentTemplateArns"
    )
    filter: Optional[AssessmentRunFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFindingsRequestListFindingsPaginateModel(BaseModel):
    assessment_run_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentRunArns"
    )
    filter: Optional[FindingFilterModel] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestModel(BaseModel):
    assessment_run_arns: Optional[Sequence[str]] = Field(
        default=None, alias="assessmentRunArns"
    )
    filter: Optional[FindingFilterModel] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeAssessmentRunsResponseModel(BaseModel):
    assessment_runs: List[AssessmentRunModel] = Field(alias="assessmentRuns")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourceGroupsResponseModel(BaseModel):
    resource_groups: List[ResourceGroupModel] = Field(alias="resourceGroups")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventSubscriptionsResponseModel(BaseModel):
    subscriptions: List[SubscriptionModel] = Field(alias="subscriptions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExclusionsPreviewResponseModel(BaseModel):
    preview_status: Literal["COMPLETED", "WORK_IN_PROGRESS"] = Field(
        alias="previewStatus"
    )
    exclusion_previews: List[ExclusionPreviewModel] = Field(alias="exclusionPreviews")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExclusionsResponseModel(BaseModel):
    exclusions: Dict[str, ExclusionModel] = Field(alias="exclusions")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssetAttributesModel(BaseModel):
    schema_version: int = Field(alias="schemaVersion")
    agent_id: Optional[str] = Field(default=None, alias="agentId")
    auto_scaling_group: Optional[str] = Field(default=None, alias="autoScalingGroup")
    ami_id: Optional[str] = Field(default=None, alias="amiId")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    ipv4_addresses: Optional[List[str]] = Field(default=None, alias="ipv4Addresses")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )


class FindingModel(BaseModel):
    arn: str = Field(alias="arn")
    attributes: List[AttributeModel] = Field(alias="attributes")
    user_attributes: List[AttributeModel] = Field(alias="userAttributes")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    schema_version: Optional[int] = Field(default=None, alias="schemaVersion")
    service: Optional[str] = Field(default=None, alias="service")
    service_attributes: Optional[InspectorServiceAttributesModel] = Field(
        default=None, alias="serviceAttributes"
    )
    asset_type: Optional[Literal["ec2-instance"]] = Field(
        default=None, alias="assetType"
    )
    asset_attributes: Optional[AssetAttributesModel] = Field(
        default=None, alias="assetAttributes"
    )
    id: Optional[str] = Field(default=None, alias="id")
    title: Optional[str] = Field(default=None, alias="title")
    description: Optional[str] = Field(default=None, alias="description")
    recommendation: Optional[str] = Field(default=None, alias="recommendation")
    severity: Optional[
        Literal["High", "Informational", "Low", "Medium", "Undefined"]
    ] = Field(default=None, alias="severity")
    numeric_severity: Optional[float] = Field(default=None, alias="numericSeverity")
    confidence: Optional[int] = Field(default=None, alias="confidence")
    indicator_of_compromise: Optional[bool] = Field(
        default=None, alias="indicatorOfCompromise"
    )


class DescribeFindingsResponseModel(BaseModel):
    findings: List[FindingModel] = Field(alias="findings")
    failed_items: Dict[str, FailedItemDetailsModel] = Field(alias="failedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
