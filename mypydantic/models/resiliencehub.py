# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class RecommendationItemModel(BaseModel):
    already_implemented: Optional[bool] = Field(
        default=None, alias="alreadyImplemented"
    )
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    target_account_id: Optional[str] = Field(default=None, alias="targetAccountId")
    target_region: Optional[str] = Field(default=None, alias="targetRegion")


class CostModel(BaseModel):
    amount: float = Field(alias="amount")
    currency: str = Field(alias="currency")
    frequency: Literal["Daily", "Hourly", "Monthly", "Yearly"] = Field(
        alias="frequency"
    )


class DisruptionComplianceModel(BaseModel):
    compliance_status: Literal["PolicyBreached", "PolicyMet"] = Field(
        alias="complianceStatus"
    )
    achievable_rpo_in_secs: Optional[int] = Field(
        default=None, alias="achievableRpoInSecs"
    )
    achievable_rto_in_secs: Optional[int] = Field(
        default=None, alias="achievableRtoInSecs"
    )
    current_rpo_in_secs: Optional[int] = Field(default=None, alias="currentRpoInSecs")
    current_rto_in_secs: Optional[int] = Field(default=None, alias="currentRtoInSecs")
    message: Optional[str] = Field(default=None, alias="message")
    rpo_description: Optional[str] = Field(default=None, alias="rpoDescription")
    rpo_reference_id: Optional[str] = Field(default=None, alias="rpoReferenceId")
    rto_description: Optional[str] = Field(default=None, alias="rtoDescription")
    rto_reference_id: Optional[str] = Field(default=None, alias="rtoReferenceId")


class ResiliencyScoreModel(BaseModel):
    disruption_score: Dict[
        Literal["AZ", "Hardware", "Region", "Software"], float
    ] = Field(alias="disruptionScore")
    score: float = Field(alias="score")


class AppComponentModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    additional_info: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    id: Optional[str] = Field(default=None, alias="id")


class TerraformSourceModel(BaseModel):
    s3_state_file_url: str = Field(alias="s3StateFileUrl")


class AppSummaryModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    creation_time: datetime = Field(alias="creationTime")
    name: str = Field(alias="name")
    assessment_schedule: Optional[Literal["Daily", "Disabled"]] = Field(
        default=None, alias="assessmentSchedule"
    )
    compliance_status: Optional[
        Literal["ChangesDetected", "NotAssessed", "PolicyBreached", "PolicyMet"]
    ] = Field(default=None, alias="complianceStatus")
    description: Optional[str] = Field(default=None, alias="description")
    resiliency_score: Optional[float] = Field(default=None, alias="resiliencyScore")
    status: Optional[Literal["Active", "Deleting"]] = Field(
        default=None, alias="status"
    )


class AppModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    creation_time: datetime = Field(alias="creationTime")
    name: str = Field(alias="name")
    assessment_schedule: Optional[Literal["Daily", "Disabled"]] = Field(
        default=None, alias="assessmentSchedule"
    )
    compliance_status: Optional[
        Literal["ChangesDetected", "NotAssessed", "PolicyBreached", "PolicyMet"]
    ] = Field(default=None, alias="complianceStatus")
    description: Optional[str] = Field(default=None, alias="description")
    last_app_compliance_evaluation_time: Optional[datetime] = Field(
        default=None, alias="lastAppComplianceEvaluationTime"
    )
    last_resiliency_score_evaluation_time: Optional[datetime] = Field(
        default=None, alias="lastResiliencyScoreEvaluationTime"
    )
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")
    resiliency_score: Optional[float] = Field(default=None, alias="resiliencyScore")
    status: Optional[Literal["Active", "Deleting"]] = Field(
        default=None, alias="status"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AppVersionSummaryModel(BaseModel):
    app_version: str = Field(alias="appVersion")


class RecommendationDisruptionComplianceModel(BaseModel):
    expected_compliance_status: Literal["PolicyBreached", "PolicyMet"] = Field(
        alias="expectedComplianceStatus"
    )
    expected_rpo_description: Optional[str] = Field(
        default=None, alias="expectedRpoDescription"
    )
    expected_rpo_in_secs: Optional[int] = Field(default=None, alias="expectedRpoInSecs")
    expected_rto_description: Optional[str] = Field(
        default=None, alias="expectedRtoDescription"
    )
    expected_rto_in_secs: Optional[int] = Field(default=None, alias="expectedRtoInSecs")


class CreateAppRequestModel(BaseModel):
    name: str = Field(alias="name")
    assessment_schedule: Optional[Literal["Daily", "Disabled"]] = Field(
        default=None, alias="assessmentSchedule"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateAppVersionAppComponentRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    additional_info: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    id: Optional[str] = Field(default=None, alias="id")


class LogicalResourceIdModel(BaseModel):
    identifier: str = Field(alias="identifier")
    logical_stack_name: Optional[str] = Field(default=None, alias="logicalStackName")
    resource_group_name: Optional[str] = Field(default=None, alias="resourceGroupName")
    terraform_source_name: Optional[str] = Field(
        default=None, alias="terraformSourceName"
    )


class CreateRecommendationTemplateRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    name: str = Field(alias="name")
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    format: Optional[Literal["CfnJson", "CfnYaml"]] = Field(
        default=None, alias="format"
    )
    recommendation_ids: Optional[Sequence[str]] = Field(
        default=None, alias="recommendationIds"
    )
    recommendation_types: Optional[Sequence[Literal["Alarm", "Sop", "Test"]]] = Field(
        default=None, alias="recommendationTypes"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class FailurePolicyModel(BaseModel):
    rpo_in_secs: int = Field(alias="rpoInSecs")
    rto_in_secs: int = Field(alias="rtoInSecs")


class DeleteAppAssessmentRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteAppRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class DeleteAppVersionAppComponentRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteRecommendationTemplateRequestModel(BaseModel):
    recommendation_template_arn: str = Field(alias="recommendationTemplateArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteResiliencyPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DescribeAppAssessmentRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")


class DescribeAppRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")


class DescribeAppVersionAppComponentRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    id: str = Field(alias="id")


class DescribeAppVersionRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")


class DescribeAppVersionResourcesResolutionStatusRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    resolution_id: Optional[str] = Field(default=None, alias="resolutionId")


class DescribeAppVersionTemplateRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")


class DescribeDraftAppVersionResourcesImportStatusRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")


class DescribeResiliencyPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")


class ListAlarmRecommendationsRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppAssessmentsRequestModel(BaseModel):
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    assessment_status: Optional[
        Sequence[Literal["Failed", "InProgress", "Pending", "Success"]]
    ] = Field(default=None, alias="assessmentStatus")
    compliance_status: Optional[Literal["PolicyBreached", "PolicyMet"]] = Field(
        default=None, alias="complianceStatus"
    )
    invoker: Optional[Literal["System", "User"]] = Field(default=None, alias="invoker")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")


class ListAppComponentCompliancesRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppComponentRecommendationsRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppInputSourcesRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppVersionAppComponentsRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppVersionResourceMappingsRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppVersionResourcesRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    resolution_id: Optional[str] = Field(default=None, alias="resolutionId")


class ListAppVersionsRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAppsRequestModel(BaseModel):
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRecommendationTemplatesRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    recommendation_template_arn: Optional[str] = Field(
        default=None, alias="recommendationTemplateArn"
    )
    reverse_order: Optional[bool] = Field(default=None, alias="reverseOrder")
    status: Optional[
        Sequence[Literal["Failed", "InProgress", "Pending", "Success"]]
    ] = Field(default=None, alias="status")


class ListResiliencyPoliciesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    policy_name: Optional[str] = Field(default=None, alias="policyName")


class ListSopRecommendationsRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSuggestedResiliencyPoliciesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTestRecommendationsRequestModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListUnsupportedAppVersionResourcesRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    resolution_id: Optional[str] = Field(default=None, alias="resolutionId")


class PhysicalResourceIdModel(BaseModel):
    identifier: str = Field(alias="identifier")
    type: Literal["Arn", "Native"] = Field(alias="type")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")


class PublishAppVersionRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")


class PutDraftAppVersionTemplateRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_template_body: str = Field(alias="appTemplateBody")


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class RemoveDraftAppVersionResourceMappingsRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_registry_app_names: Optional[Sequence[str]] = Field(
        default=None, alias="appRegistryAppNames"
    )
    logical_stack_names: Optional[Sequence[str]] = Field(
        default=None, alias="logicalStackNames"
    )
    resource_group_names: Optional[Sequence[str]] = Field(
        default=None, alias="resourceGroupNames"
    )
    resource_names: Optional[Sequence[str]] = Field(default=None, alias="resourceNames")
    terraform_source_names: Optional[Sequence[str]] = Field(
        default=None, alias="terraformSourceNames"
    )


class ResolveAppVersionResourcesRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")


class ResourceErrorModel(BaseModel):
    logical_resource_id: Optional[str] = Field(default=None, alias="logicalResourceId")
    physical_resource_id: Optional[str] = Field(
        default=None, alias="physicalResourceId"
    )
    reason: Optional[str] = Field(default=None, alias="reason")


class StartAppAssessmentRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    assessment_name: str = Field(alias="assessmentName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAppRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    assessment_schedule: Optional[Literal["Daily", "Disabled"]] = Field(
        default=None, alias="assessmentSchedule"
    )
    clear_resiliency_policy_arn: Optional[bool] = Field(
        default=None, alias="clearResiliencyPolicyArn"
    )
    description: Optional[str] = Field(default=None, alias="description")
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")


class UpdateAppVersionAppComponentRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    id: str = Field(alias="id")
    additional_info: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")


class UpdateAppVersionRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    additional_info: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="additionalInfo"
    )


class DeleteAppAssessmentResponseModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    assessment_status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="assessmentStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRecommendationTemplateResponseModel(BaseModel):
    recommendation_template_arn: str = Field(alias="recommendationTemplateArn")
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResiliencyPolicyResponseModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppVersionResourcesResolutionStatusResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    error_message: str = Field(alias="errorMessage")
    resolution_id: str = Field(alias="resolutionId")
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppVersionResponseModel(BaseModel):
    additional_info: Dict[str, List[str]] = Field(alias="additionalInfo")
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppVersionTemplateResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_template_body: str = Field(alias="appTemplateBody")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDraftAppVersionResourcesImportStatusResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    error_message: str = Field(alias="errorMessage")
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    status_change_time: datetime = Field(alias="statusChangeTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishAppVersionResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDraftAppVersionTemplateResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveDraftAppVersionResourceMappingsResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResolveAppVersionResourcesResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    resolution_id: str = Field(alias="resolutionId")
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppVersionResponseModel(BaseModel):
    additional_info: Dict[str, List[str]] = Field(alias="additionalInfo")
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AlarmRecommendationModel(BaseModel):
    name: str = Field(alias="name")
    recommendation_id: str = Field(alias="recommendationId")
    reference_id: str = Field(alias="referenceId")
    type: Literal["Canary", "Composite", "Event", "Logs", "Metric"] = Field(
        alias="type"
    )
    app_component_name: Optional[str] = Field(default=None, alias="appComponentName")
    description: Optional[str] = Field(default=None, alias="description")
    items: Optional[List[RecommendationItemModel]] = Field(default=None, alias="items")
    prerequisite: Optional[str] = Field(default=None, alias="prerequisite")


class SopRecommendationModel(BaseModel):
    recommendation_id: str = Field(alias="recommendationId")
    reference_id: str = Field(alias="referenceId")
    service_type: Literal["SSM"] = Field(alias="serviceType")
    app_component_name: Optional[str] = Field(default=None, alias="appComponentName")
    description: Optional[str] = Field(default=None, alias="description")
    items: Optional[List[RecommendationItemModel]] = Field(default=None, alias="items")
    name: Optional[str] = Field(default=None, alias="name")
    prerequisite: Optional[str] = Field(default=None, alias="prerequisite")


class TestRecommendationModel(BaseModel):
    reference_id: str = Field(alias="referenceId")
    app_component_name: Optional[str] = Field(default=None, alias="appComponentName")
    depends_on_alarms: Optional[List[str]] = Field(
        default=None, alias="dependsOnAlarms"
    )
    description: Optional[str] = Field(default=None, alias="description")
    intent: Optional[str] = Field(default=None, alias="intent")
    items: Optional[List[RecommendationItemModel]] = Field(default=None, alias="items")
    name: Optional[str] = Field(default=None, alias="name")
    prerequisite: Optional[str] = Field(default=None, alias="prerequisite")
    recommendation_id: Optional[str] = Field(default=None, alias="recommendationId")
    risk: Optional[Literal["High", "Medium", "Small"]] = Field(
        default=None, alias="risk"
    )
    type: Optional[Literal["AZ", "Hardware", "Region", "Software"]] = Field(
        default=None, alias="type"
    )


class AppAssessmentSummaryModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    assessment_status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="assessmentStatus"
    )
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    app_version: Optional[str] = Field(default=None, alias="appVersion")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    compliance_status: Optional[Literal["PolicyBreached", "PolicyMet"]] = Field(
        default=None, alias="complianceStatus"
    )
    cost: Optional[CostModel] = Field(default=None, alias="cost")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    invoker: Optional[Literal["System", "User"]] = Field(default=None, alias="invoker")
    message: Optional[str] = Field(default=None, alias="message")
    resiliency_score: Optional[float] = Field(default=None, alias="resiliencyScore")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")


class AppComponentComplianceModel(BaseModel):
    app_component_name: Optional[str] = Field(default=None, alias="appComponentName")
    compliance: Optional[
        Dict[Literal["AZ", "Hardware", "Region", "Software"], DisruptionComplianceModel]
    ] = Field(default=None, alias="compliance")
    cost: Optional[CostModel] = Field(default=None, alias="cost")
    message: Optional[str] = Field(default=None, alias="message")
    resiliency_score: Optional[ResiliencyScoreModel] = Field(
        default=None, alias="resiliencyScore"
    )
    status: Optional[Literal["PolicyBreached", "PolicyMet"]] = Field(
        default=None, alias="status"
    )


class CreateAppVersionAppComponentResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_component: AppComponentModel = Field(alias="appComponent")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppVersionAppComponentResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_component: AppComponentModel = Field(alias="appComponent")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppVersionAppComponentResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_component: AppComponentModel = Field(alias="appComponent")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppVersionAppComponentsResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_components: List[AppComponentModel] = Field(alias="appComponents")
    app_version: str = Field(alias="appVersion")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppVersionAppComponentResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_component: AppComponentModel = Field(alias="appComponent")
    app_version: str = Field(alias="appVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AppInputSourceModel(BaseModel):
    import_type: Literal[
        "AppRegistryApp", "CfnStack", "Resource", "ResourceGroup", "Terraform"
    ] = Field(alias="importType")
    resource_count: Optional[int] = Field(default=None, alias="resourceCount")
    source_arn: Optional[str] = Field(default=None, alias="sourceArn")
    source_name: Optional[str] = Field(default=None, alias="sourceName")
    terraform_source: Optional[TerraformSourceModel] = Field(
        default=None, alias="terraformSource"
    )


class DeleteAppInputSourceRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    source_arn: Optional[str] = Field(default=None, alias="sourceArn")
    terraform_source: Optional[TerraformSourceModel] = Field(
        default=None, alias="terraformSource"
    )


class ImportResourcesToDraftAppVersionRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    import_strategy: Optional[Literal["AddOnly", "ReplaceAll"]] = Field(
        default=None, alias="importStrategy"
    )
    source_arns: Optional[Sequence[str]] = Field(default=None, alias="sourceArns")
    terraform_sources: Optional[Sequence[TerraformSourceModel]] = Field(
        default=None, alias="terraformSources"
    )


class ImportResourcesToDraftAppVersionResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    source_arns: List[str] = Field(alias="sourceArns")
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    terraform_sources: List[TerraformSourceModel] = Field(alias="terraformSources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppsResponseModel(BaseModel):
    app_summaries: List[AppSummaryModel] = Field(alias="appSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppResponseModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppResponseModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppResponseModel(BaseModel):
    app: AppModel = Field(alias="app")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppVersionsResponseModel(BaseModel):
    app_versions: List[AppVersionSummaryModel] = Field(alias="appVersions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigRecommendationModel(BaseModel):
    name: str = Field(alias="name")
    optimization_type: Literal[
        "BestAZRecovery",
        "BestAttainable",
        "BestRegionRecovery",
        "LeastChange",
        "LeastCost",
        "LeastErrors",
    ] = Field(alias="optimizationType")
    reference_id: str = Field(alias="referenceId")
    app_component_name: Optional[str] = Field(default=None, alias="appComponentName")
    compliance: Optional[
        Dict[Literal["AZ", "Hardware", "Region", "Software"], DisruptionComplianceModel]
    ] = Field(default=None, alias="compliance")
    cost: Optional[CostModel] = Field(default=None, alias="cost")
    description: Optional[str] = Field(default=None, alias="description")
    ha_architecture: Optional[
        Literal[
            "BackupAndRestore",
            "MultiSite",
            "NoRecoveryPlan",
            "PilotLight",
            "WarmStandby",
        ]
    ] = Field(default=None, alias="haArchitecture")
    recommendation_compliance: Optional[
        Dict[
            Literal["AZ", "Hardware", "Region", "Software"],
            RecommendationDisruptionComplianceModel,
        ]
    ] = Field(default=None, alias="recommendationCompliance")
    suggested_changes: Optional[List[str]] = Field(
        default=None, alias="suggestedChanges"
    )


class CreateAppVersionResourceRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_components: Sequence[str] = Field(alias="appComponents")
    logical_resource_id: LogicalResourceIdModel = Field(alias="logicalResourceId")
    physical_resource_id: str = Field(alias="physicalResourceId")
    resource_name: str = Field(alias="resourceName")
    resource_type: str = Field(alias="resourceType")
    additional_info: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteAppVersionResourceRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    logical_resource_id: Optional[LogicalResourceIdModel] = Field(
        default=None, alias="logicalResourceId"
    )
    physical_resource_id: Optional[str] = Field(
        default=None, alias="physicalResourceId"
    )
    resource_name: Optional[str] = Field(default=None, alias="resourceName")


class DescribeAppVersionResourceRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    logical_resource_id: Optional[LogicalResourceIdModel] = Field(
        default=None, alias="logicalResourceId"
    )
    physical_resource_id: Optional[str] = Field(
        default=None, alias="physicalResourceId"
    )
    resource_name: Optional[str] = Field(default=None, alias="resourceName")


class UpdateAppVersionResourceRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    additional_info: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    app_components: Optional[Sequence[str]] = Field(default=None, alias="appComponents")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    excluded: Optional[bool] = Field(default=None, alias="excluded")
    logical_resource_id: Optional[LogicalResourceIdModel] = Field(
        default=None, alias="logicalResourceId"
    )
    physical_resource_id: Optional[str] = Field(
        default=None, alias="physicalResourceId"
    )
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")


class CreateResiliencyPolicyRequestModel(BaseModel):
    policy: Mapping[
        Literal["AZ", "Hardware", "Region", "Software"], FailurePolicyModel
    ] = Field(alias="policy")
    policy_name: str = Field(alias="policyName")
    tier: Literal[
        "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical"
    ] = Field(alias="tier")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    data_location_constraint: Optional[
        Literal["AnyLocation", "SameContinent", "SameCountry"]
    ] = Field(default=None, alias="dataLocationConstraint")
    policy_description: Optional[str] = Field(default=None, alias="policyDescription")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResiliencyPolicyModel(BaseModel):
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    data_location_constraint: Optional[
        Literal["AnyLocation", "SameContinent", "SameCountry"]
    ] = Field(default=None, alias="dataLocationConstraint")
    estimated_cost_tier: Optional[Literal["L1", "L2", "L3", "L4"]] = Field(
        default=None, alias="estimatedCostTier"
    )
    policy: Optional[
        Dict[Literal["AZ", "Hardware", "Region", "Software"], FailurePolicyModel]
    ] = Field(default=None, alias="policy")
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")
    policy_description: Optional[str] = Field(default=None, alias="policyDescription")
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    tier: Optional[
        Literal[
            "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical"
        ]
    ] = Field(default=None, alias="tier")


class UpdateResiliencyPolicyRequestModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")
    data_location_constraint: Optional[
        Literal["AnyLocation", "SameContinent", "SameCountry"]
    ] = Field(default=None, alias="dataLocationConstraint")
    policy: Optional[
        Mapping[Literal["AZ", "Hardware", "Region", "Software"], FailurePolicyModel]
    ] = Field(default=None, alias="policy")
    policy_description: Optional[str] = Field(default=None, alias="policyDescription")
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    tier: Optional[
        Literal[
            "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical"
        ]
    ] = Field(default=None, alias="tier")


class PhysicalResourceModel(BaseModel):
    logical_resource_id: LogicalResourceIdModel = Field(alias="logicalResourceId")
    physical_resource_id: PhysicalResourceIdModel = Field(alias="physicalResourceId")
    resource_type: str = Field(alias="resourceType")
    additional_info: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="additionalInfo"
    )
    app_components: Optional[List[AppComponentModel]] = Field(
        default=None, alias="appComponents"
    )
    excluded: Optional[bool] = Field(default=None, alias="excluded")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")


class ResourceMappingModel(BaseModel):
    mapping_type: Literal[
        "AppRegistryApp", "CfnStack", "Resource", "ResourceGroup", "Terraform"
    ] = Field(alias="mappingType")
    physical_resource_id: PhysicalResourceIdModel = Field(alias="physicalResourceId")
    app_registry_app_name: Optional[str] = Field(
        default=None, alias="appRegistryAppName"
    )
    logical_stack_name: Optional[str] = Field(default=None, alias="logicalStackName")
    resource_group_name: Optional[str] = Field(default=None, alias="resourceGroupName")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    terraform_source_name: Optional[str] = Field(
        default=None, alias="terraformSourceName"
    )


class UnsupportedResourceModel(BaseModel):
    logical_resource_id: LogicalResourceIdModel = Field(alias="logicalResourceId")
    physical_resource_id: PhysicalResourceIdModel = Field(alias="physicalResourceId")
    resource_type: str = Field(alias="resourceType")


class RecommendationTemplateModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    format: Literal["CfnJson", "CfnYaml"] = Field(alias="format")
    name: str = Field(alias="name")
    recommendation_template_arn: str = Field(alias="recommendationTemplateArn")
    recommendation_types: List[Literal["Alarm", "Sop", "Test"]] = Field(
        alias="recommendationTypes"
    )
    status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="status"
    )
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    message: Optional[str] = Field(default=None, alias="message")
    needs_replacements: Optional[bool] = Field(default=None, alias="needsReplacements")
    recommendation_ids: Optional[List[str]] = Field(
        default=None, alias="recommendationIds"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    templates_location: Optional[S3LocationModel] = Field(
        default=None, alias="templatesLocation"
    )


class ResourceErrorsDetailsModel(BaseModel):
    has_more_errors: Optional[bool] = Field(default=None, alias="hasMoreErrors")
    resource_errors: Optional[List[ResourceErrorModel]] = Field(
        default=None, alias="resourceErrors"
    )


class ListAlarmRecommendationsResponseModel(BaseModel):
    alarm_recommendations: List[AlarmRecommendationModel] = Field(
        alias="alarmRecommendations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSopRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sop_recommendations: List[SopRecommendationModel] = Field(
        alias="sopRecommendations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTestRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    test_recommendations: List[TestRecommendationModel] = Field(
        alias="testRecommendations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppAssessmentsResponseModel(BaseModel):
    assessment_summaries: List[AppAssessmentSummaryModel] = Field(
        alias="assessmentSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppComponentCompliancesResponseModel(BaseModel):
    component_compliances: List[AppComponentComplianceModel] = Field(
        alias="componentCompliances"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppInputSourceResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_input_source: AppInputSourceModel = Field(alias="appInputSource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppInputSourcesResponseModel(BaseModel):
    app_input_sources: List[AppInputSourceModel] = Field(alias="appInputSources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentRecommendationModel(BaseModel):
    app_component_name: str = Field(alias="appComponentName")
    config_recommendations: List[ConfigRecommendationModel] = Field(
        alias="configRecommendations"
    )
    recommendation_status: Literal[
        "BreachedCanMeet", "BreachedUnattainable", "MetCanImprove"
    ] = Field(alias="recommendationStatus")


class CreateResiliencyPolicyResponseModel(BaseModel):
    policy: ResiliencyPolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResiliencyPolicyResponseModel(BaseModel):
    policy: ResiliencyPolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResiliencyPoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resiliency_policies: List[ResiliencyPolicyModel] = Field(alias="resiliencyPolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSuggestedResiliencyPoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resiliency_policies: List[ResiliencyPolicyModel] = Field(alias="resiliencyPolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResiliencyPolicyResponseModel(BaseModel):
    policy: ResiliencyPolicyModel = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppVersionResourceResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    physical_resource: PhysicalResourceModel = Field(alias="physicalResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAppVersionResourceResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    physical_resource: PhysicalResourceModel = Field(alias="physicalResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppVersionResourceResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    physical_resource: PhysicalResourceModel = Field(alias="physicalResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppVersionResourcesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    physical_resources: List[PhysicalResourceModel] = Field(alias="physicalResources")
    resolution_id: str = Field(alias="resolutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAppVersionResourceResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    physical_resource: PhysicalResourceModel = Field(alias="physicalResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddDraftAppVersionResourceMappingsRequestModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    resource_mappings: Sequence[ResourceMappingModel] = Field(alias="resourceMappings")


class AddDraftAppVersionResourceMappingsResponseModel(BaseModel):
    app_arn: str = Field(alias="appArn")
    app_version: str = Field(alias="appVersion")
    resource_mappings: List[ResourceMappingModel] = Field(alias="resourceMappings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppVersionResourceMappingsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resource_mappings: List[ResourceMappingModel] = Field(alias="resourceMappings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUnsupportedAppVersionResourcesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    resolution_id: str = Field(alias="resolutionId")
    unsupported_resources: List[UnsupportedResourceModel] = Field(
        alias="unsupportedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecommendationTemplateResponseModel(BaseModel):
    recommendation_template: RecommendationTemplateModel = Field(
        alias="recommendationTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecommendationTemplatesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    recommendation_templates: List[RecommendationTemplateModel] = Field(
        alias="recommendationTemplates"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AppAssessmentModel(BaseModel):
    assessment_arn: str = Field(alias="assessmentArn")
    assessment_status: Literal["Failed", "InProgress", "Pending", "Success"] = Field(
        alias="assessmentStatus"
    )
    invoker: Literal["System", "User"] = Field(alias="invoker")
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    app_version: Optional[str] = Field(default=None, alias="appVersion")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    compliance: Optional[
        Dict[Literal["AZ", "Hardware", "Region", "Software"], DisruptionComplianceModel]
    ] = Field(default=None, alias="compliance")
    compliance_status: Optional[Literal["PolicyBreached", "PolicyMet"]] = Field(
        default=None, alias="complianceStatus"
    )
    cost: Optional[CostModel] = Field(default=None, alias="cost")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    message: Optional[str] = Field(default=None, alias="message")
    policy: Optional[ResiliencyPolicyModel] = Field(default=None, alias="policy")
    resiliency_score: Optional[ResiliencyScoreModel] = Field(
        default=None, alias="resiliencyScore"
    )
    resource_errors_details: Optional[ResourceErrorsDetailsModel] = Field(
        default=None, alias="resourceErrorsDetails"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListAppComponentRecommendationsResponseModel(BaseModel):
    component_recommendations: List[ComponentRecommendationModel] = Field(
        alias="componentRecommendations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppAssessmentResponseModel(BaseModel):
    assessment: AppAssessmentModel = Field(alias="assessment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAppAssessmentResponseModel(BaseModel):
    assessment: AppAssessmentModel = Field(alias="assessment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
