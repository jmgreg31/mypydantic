# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AWSAccountModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    email_address: Optional[str] = Field(default=None, alias="emailAddress")
    name: Optional[str] = Field(default=None, alias="name")


class AWSServiceModel(BaseModel):
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class DelegationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    status: Optional[Literal["COMPLETE", "IN_PROGRESS", "UNDER_REVIEW"]] = Field(
        default=None, alias="status"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    role_type: Optional[Literal["PROCESS_OWNER", "RESOURCE_OWNER"]] = Field(
        default=None, alias="roleType"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")
    control_set_id: Optional[str] = Field(default=None, alias="controlSetId")
    comment: Optional[str] = Field(default=None, alias="comment")
    created_by: Optional[str] = Field(default=None, alias="createdBy")


class RoleModel(BaseModel):
    role_type: Literal["PROCESS_OWNER", "RESOURCE_OWNER"] = Field(alias="roleType")
    role_arn: str = Field(alias="roleArn")


class ControlCommentModel(BaseModel):
    author_name: Optional[str] = Field(default=None, alias="authorName")
    comment_body: Optional[str] = Field(default=None, alias="commentBody")
    posted_date: Optional[datetime] = Field(default=None, alias="postedDate")


class AssessmentEvidenceFolderModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    date: Optional[datetime] = Field(default=None, alias="date")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    control_set_id: Optional[str] = Field(default=None, alias="controlSetId")
    control_id: Optional[str] = Field(default=None, alias="controlId")
    id: Optional[str] = Field(default=None, alias="id")
    data_source: Optional[str] = Field(default=None, alias="dataSource")
    author: Optional[str] = Field(default=None, alias="author")
    total_evidence: Optional[int] = Field(default=None, alias="totalEvidence")
    assessment_report_selection_count: Optional[int] = Field(
        default=None, alias="assessmentReportSelectionCount"
    )
    control_name: Optional[str] = Field(default=None, alias="controlName")
    evidence_resources_included_count: Optional[int] = Field(
        default=None, alias="evidenceResourcesIncludedCount"
    )
    evidence_by_type_configuration_data_count: Optional[int] = Field(
        default=None, alias="evidenceByTypeConfigurationDataCount"
    )
    evidence_by_type_manual_count: Optional[int] = Field(
        default=None, alias="evidenceByTypeManualCount"
    )
    evidence_by_type_compliance_check_count: Optional[int] = Field(
        default=None, alias="evidenceByTypeComplianceCheckCount"
    )
    evidence_by_type_compliance_check_issues_count: Optional[int] = Field(
        default=None, alias="evidenceByTypeComplianceCheckIssuesCount"
    )
    evidence_by_type_user_activity_count: Optional[int] = Field(
        default=None, alias="evidenceByTypeUserActivityCount"
    )
    evidence_aws_service_source_count: Optional[int] = Field(
        default=None, alias="evidenceAwsServiceSourceCount"
    )


class AssessmentFrameworkMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[Literal["Custom", "Standard"]] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")
    controls_count: Optional[int] = Field(default=None, alias="controlsCount")
    control_sets_count: Optional[int] = Field(default=None, alias="controlSetsCount")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class AssessmentFrameworkShareRequestModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    framework_id: Optional[str] = Field(default=None, alias="frameworkId")
    framework_name: Optional[str] = Field(default=None, alias="frameworkName")
    framework_description: Optional[str] = Field(
        default=None, alias="frameworkDescription"
    )
    status: Optional[
        Literal[
            "ACTIVE",
            "DECLINED",
            "EXPIRED",
            "EXPIRING",
            "FAILED",
            "REPLICATING",
            "REVOKED",
            "SHARED",
        ]
    ] = Field(default=None, alias="status")
    source_account: Optional[str] = Field(default=None, alias="sourceAccount")
    destination_account: Optional[str] = Field(default=None, alias="destinationAccount")
    destination_region: Optional[str] = Field(default=None, alias="destinationRegion")
    expiration_time: Optional[datetime] = Field(default=None, alias="expirationTime")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")
    comment: Optional[str] = Field(default=None, alias="comment")
    standard_controls_count: Optional[int] = Field(
        default=None, alias="standardControlsCount"
    )
    custom_controls_count: Optional[int] = Field(
        default=None, alias="customControlsCount"
    )
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")


class FrameworkMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")


class AssessmentReportsDestinationModel(BaseModel):
    destination_type: Optional[Literal["S3"]] = Field(
        default=None, alias="destinationType"
    )
    destination: Optional[str] = Field(default=None, alias="destination")


class AssessmentReportEvidenceErrorModel(BaseModel):
    evidence_id: Optional[str] = Field(default=None, alias="evidenceId")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class AssessmentReportMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    author: Optional[str] = Field(default=None, alias="author")
    status: Optional[Literal["COMPLETE", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")


class AssessmentReportModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    author: Optional[str] = Field(default=None, alias="author")
    status: Optional[Literal["COMPLETE", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")


class AssociateAssessmentReportEvidenceFolderRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")


class BatchAssociateAssessmentReportEvidenceRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")
    evidence_ids: Sequence[str] = Field(alias="evidenceIds")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateDelegationRequestModel(BaseModel):
    comment: Optional[str] = Field(default=None, alias="comment")
    control_set_id: Optional[str] = Field(default=None, alias="controlSetId")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    role_type: Optional[Literal["PROCESS_OWNER", "RESOURCE_OWNER"]] = Field(
        default=None, alias="roleType"
    )


class BatchDeleteDelegationByAssessmentErrorModel(BaseModel):
    delegation_id: Optional[str] = Field(default=None, alias="delegationId")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchDeleteDelegationByAssessmentRequestModel(BaseModel):
    delegation_ids: Sequence[str] = Field(alias="delegationIds")
    assessment_id: str = Field(alias="assessmentId")


class BatchDisassociateAssessmentReportEvidenceRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")
    evidence_ids: Sequence[str] = Field(alias="evidenceIds")


class ManualEvidenceModel(BaseModel):
    s3_resource_path: Optional[str] = Field(default=None, alias="s3ResourcePath")


class ChangeLogModel(BaseModel):
    object_type: Optional[
        Literal[
            "ASSESSMENT", "ASSESSMENT_REPORT", "CONTROL", "CONTROL_SET", "DELEGATION"
        ]
    ] = Field(default=None, alias="objectType")
    object_name: Optional[str] = Field(default=None, alias="objectName")
    action: Optional[
        Literal[
            "ACTIVE",
            "CREATE",
            "DELETE",
            "IMPORT_EVIDENCE",
            "INACTIVE",
            "REVIEWED",
            "UNDER_REVIEW",
            "UPDATE_METADATA",
        ]
    ] = Field(default=None, alias="action")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")


class EvidenceInsightsModel(BaseModel):
    noncompliant_evidence_count: Optional[int] = Field(
        default=None, alias="noncompliantEvidenceCount"
    )
    compliant_evidence_count: Optional[int] = Field(
        default=None, alias="compliantEvidenceCount"
    )
    inconclusive_evidence_count: Optional[int] = Field(
        default=None, alias="inconclusiveEvidenceCount"
    )


class SourceKeywordModel(BaseModel):
    keyword_input_type: Optional[Literal["SELECT_FROM_LIST"]] = Field(
        default=None, alias="keywordInputType"
    )
    keyword_value: Optional[str] = Field(default=None, alias="keywordValue")


class ControlMetadataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    control_sources: Optional[str] = Field(default=None, alias="controlSources")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")


class CreateAssessmentFrameworkControlModel(BaseModel):
    id: str = Field(alias="id")


class CreateAssessmentReportRequestModel(BaseModel):
    name: str = Field(alias="name")
    assessment_id: str = Field(alias="assessmentId")
    description: Optional[str] = Field(default=None, alias="description")
    query_statement: Optional[str] = Field(default=None, alias="queryStatement")


class DelegationMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    status: Optional[Literal["COMPLETE", "IN_PROGRESS", "UNDER_REVIEW"]] = Field(
        default=None, alias="status"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    control_set_name: Optional[str] = Field(default=None, alias="controlSetName")


class DeleteAssessmentFrameworkRequestModel(BaseModel):
    framework_id: str = Field(alias="frameworkId")


class DeleteAssessmentFrameworkShareRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    request_type: Literal["RECEIVED", "SENT"] = Field(alias="requestType")


class DeleteAssessmentReportRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    assessment_report_id: str = Field(alias="assessmentReportId")


class DeleteAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")


class DeleteControlRequestModel(BaseModel):
    control_id: str = Field(alias="controlId")


class DeregisterOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: Optional[str] = Field(default=None, alias="adminAccountId")


class DeregistrationPolicyModel(BaseModel):
    delete_resources: Optional[Literal["ALL", "DEFAULT"]] = Field(
        default=None, alias="deleteResources"
    )


class DisassociateAssessmentReportEvidenceFolderRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")


class EvidenceFinderEnablementModel(BaseModel):
    event_data_store_arn: Optional[str] = Field(default=None, alias="eventDataStoreArn")
    enablement_status: Optional[
        Literal["DISABLED", "DISABLE_IN_PROGRESS", "ENABLED", "ENABLE_IN_PROGRESS"]
    ] = Field(default=None, alias="enablementStatus")
    backfill_status: Optional[
        Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="backfillStatus")
    error: Optional[str] = Field(default=None, alias="error")


class ResourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    value: Optional[str] = Field(default=None, alias="value")
    compliance_check: Optional[str] = Field(default=None, alias="complianceCheck")


class GetAssessmentFrameworkRequestModel(BaseModel):
    framework_id: str = Field(alias="frameworkId")


class GetAssessmentReportUrlRequestModel(BaseModel):
    assessment_report_id: str = Field(alias="assessmentReportId")
    assessment_id: str = Field(alias="assessmentId")


class URLModel(BaseModel):
    hyperlink_name: Optional[str] = Field(default=None, alias="hyperlinkName")
    link: Optional[str] = Field(default=None, alias="link")


class GetAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")


class GetChangeLogsRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: Optional[str] = Field(default=None, alias="controlSetId")
    control_id: Optional[str] = Field(default=None, alias="controlId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetControlRequestModel(BaseModel):
    control_id: str = Field(alias="controlId")


class GetDelegationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEvidenceByEvidenceFolderRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEvidenceFolderRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")


class GetEvidenceFoldersByAssessmentControlRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    control_id: str = Field(alias="controlId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEvidenceFoldersByAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetEvidenceRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    evidence_folder_id: str = Field(alias="evidenceFolderId")
    evidence_id: str = Field(alias="evidenceId")


class GetInsightsByAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")


class InsightsByAssessmentModel(BaseModel):
    noncompliant_evidence_count: Optional[int] = Field(
        default=None, alias="noncompliantEvidenceCount"
    )
    compliant_evidence_count: Optional[int] = Field(
        default=None, alias="compliantEvidenceCount"
    )
    inconclusive_evidence_count: Optional[int] = Field(
        default=None, alias="inconclusiveEvidenceCount"
    )
    assessment_controls_count_by_noncompliant_evidence: Optional[int] = Field(
        default=None, alias="assessmentControlsCountByNoncompliantEvidence"
    )
    total_assessment_controls_count: Optional[int] = Field(
        default=None, alias="totalAssessmentControlsCount"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class InsightsModel(BaseModel):
    active_assessments_count: Optional[int] = Field(
        default=None, alias="activeAssessmentsCount"
    )
    noncompliant_evidence_count: Optional[int] = Field(
        default=None, alias="noncompliantEvidenceCount"
    )
    compliant_evidence_count: Optional[int] = Field(
        default=None, alias="compliantEvidenceCount"
    )
    inconclusive_evidence_count: Optional[int] = Field(
        default=None, alias="inconclusiveEvidenceCount"
    )
    assessment_controls_count_by_noncompliant_evidence: Optional[int] = Field(
        default=None, alias="assessmentControlsCountByNoncompliantEvidence"
    )
    total_assessment_controls_count: Optional[int] = Field(
        default=None, alias="totalAssessmentControlsCount"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class ServiceMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    description: Optional[str] = Field(default=None, alias="description")
    category: Optional[str] = Field(default=None, alias="category")


class GetSettingsRequestModel(BaseModel):
    attribute: Literal[
        "ALL",
        "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
        "DEFAULT_PROCESS_OWNERS",
        "DEREGISTRATION_POLICY",
        "EVIDENCE_FINDER_ENABLEMENT",
        "IS_AWS_ORG_ENABLED",
        "SNS_TOPIC",
    ] = Field(alias="attribute")


class ListAssessmentControlInsightsByControlDomainRequestModel(BaseModel):
    control_domain_id: str = Field(alias="controlDomainId")
    assessment_id: str = Field(alias="assessmentId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssessmentFrameworkShareRequestsRequestModel(BaseModel):
    request_type: Literal["RECEIVED", "SENT"] = Field(alias="requestType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssessmentFrameworksRequestModel(BaseModel):
    framework_type: Literal["Custom", "Standard"] = Field(alias="frameworkType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssessmentReportsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssessmentsRequestModel(BaseModel):
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListControlDomainInsightsByAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListControlDomainInsightsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListControlInsightsByControlDomainRequestModel(BaseModel):
    control_domain_id: str = Field(alias="controlDomainId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListControlsRequestModel(BaseModel):
    control_type: Literal["Custom", "Standard"] = Field(alias="controlType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListKeywordsForDataSourceRequestModel(BaseModel):
    source: Literal[
        "AWS_API_Call", "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "MANUAL"
    ] = Field(alias="source")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListNotificationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class NotificationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    assessment_id: Optional[str] = Field(default=None, alias="assessmentId")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    control_set_id: Optional[str] = Field(default=None, alias="controlSetId")
    control_set_name: Optional[str] = Field(default=None, alias="controlSetName")
    description: Optional[str] = Field(default=None, alias="description")
    event_time: Optional[datetime] = Field(default=None, alias="eventTime")
    source: Optional[str] = Field(default=None, alias="source")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class RegisterAccountRequestModel(BaseModel):
    kms_key: Optional[str] = Field(default=None, alias="kmsKey")
    delegated_admin_account: Optional[str] = Field(
        default=None, alias="delegatedAdminAccount"
    )


class RegisterOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="adminAccountId")


class StartAssessmentFrameworkShareRequestModel(BaseModel):
    framework_id: str = Field(alias="frameworkId")
    destination_account: str = Field(alias="destinationAccount")
    destination_region: str = Field(alias="destinationRegion")
    comment: Optional[str] = Field(default=None, alias="comment")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAssessmentControlRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    control_id: str = Field(alias="controlId")
    control_status: Optional[Literal["INACTIVE", "REVIEWED", "UNDER_REVIEW"]] = Field(
        default=None, alias="controlStatus"
    )
    comment_body: Optional[str] = Field(default=None, alias="commentBody")


class UpdateAssessmentControlSetStatusRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    status: Literal["ACTIVE", "REVIEWED", "UNDER_REVIEW"] = Field(alias="status")
    comment: str = Field(alias="comment")


class UpdateAssessmentFrameworkShareRequestModel(BaseModel):
    request_id: str = Field(alias="requestId")
    request_type: Literal["RECEIVED", "SENT"] = Field(alias="requestType")
    action: Literal["ACCEPT", "DECLINE", "REVOKE"] = Field(alias="action")


class UpdateAssessmentStatusRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias="status")


class ValidateAssessmentReportIntegrityRequestModel(BaseModel):
    s3_relative_path: str = Field(alias="s3RelativePath")


class ScopeModel(BaseModel):
    aws_accounts: Optional[Sequence[AWSAccountModel]] = Field(
        default=None, alias="awsAccounts"
    )
    aws_services: Optional[Sequence[AWSServiceModel]] = Field(
        default=None, alias="awsServices"
    )


class AssessmentMetadataItemModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    roles: Optional[List[RoleModel]] = Field(default=None, alias="roles")
    delegations: Optional[List[DelegationModel]] = Field(
        default=None, alias="delegations"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class AssessmentControlModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[Literal["INACTIVE", "REVIEWED", "UNDER_REVIEW"]] = Field(
        default=None, alias="status"
    )
    response: Optional[Literal["AUTOMATE", "DEFER", "IGNORE", "MANUAL"]] = Field(
        default=None, alias="response"
    )
    comments: Optional[List[ControlCommentModel]] = Field(
        default=None, alias="comments"
    )
    evidence_sources: Optional[List[str]] = Field(default=None, alias="evidenceSources")
    evidence_count: Optional[int] = Field(default=None, alias="evidenceCount")
    assessment_report_evidence_count: Optional[int] = Field(
        default=None, alias="assessmentReportEvidenceCount"
    )


class BatchAssociateAssessmentReportEvidenceResponseModel(BaseModel):
    evidence_ids: List[str] = Field(alias="evidenceIds")
    errors: List[AssessmentReportEvidenceErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateAssessmentReportEvidenceResponseModel(BaseModel):
    evidence_ids: List[str] = Field(alias="evidenceIds")
    errors: List[AssessmentReportEvidenceErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssessmentReportResponseModel(BaseModel):
    assessment_report: AssessmentReportModel = Field(alias="assessmentReport")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterAccountResponseModel(BaseModel):
    status: Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountStatusResponseModel(BaseModel):
    status: Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEvidenceFolderResponseModel(BaseModel):
    evidence_folder: AssessmentEvidenceFolderModel = Field(alias="evidenceFolder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEvidenceFoldersByAssessmentControlResponseModel(BaseModel):
    evidence_folders: List[AssessmentEvidenceFolderModel] = Field(
        alias="evidenceFolders"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEvidenceFoldersByAssessmentResponseModel(BaseModel):
    evidence_folders: List[AssessmentEvidenceFolderModel] = Field(
        alias="evidenceFolders"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrganizationAdminAccountResponseModel(BaseModel):
    admin_account_id: str = Field(alias="adminAccountId")
    organization_id: str = Field(alias="organizationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentFrameworkShareRequestsResponseModel(BaseModel):
    assessment_framework_share_requests: List[
        AssessmentFrameworkShareRequestModel
    ] = Field(alias="assessmentFrameworkShareRequests")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentFrameworksResponseModel(BaseModel):
    framework_metadata_list: List[AssessmentFrameworkMetadataModel] = Field(
        alias="frameworkMetadataList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentReportsResponseModel(BaseModel):
    assessment_reports: List[AssessmentReportMetadataModel] = Field(
        alias="assessmentReports"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKeywordsForDataSourceResponseModel(BaseModel):
    keywords: List[str] = Field(alias="keywords")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterAccountResponseModel(BaseModel):
    status: Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterOrganizationAdminAccountResponseModel(BaseModel):
    admin_account_id: str = Field(alias="adminAccountId")
    organization_id: str = Field(alias="organizationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAssessmentFrameworkShareResponseModel(BaseModel):
    assessment_framework_share_request: AssessmentFrameworkShareRequestModel = Field(
        alias="assessmentFrameworkShareRequest"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssessmentFrameworkShareResponseModel(BaseModel):
    assessment_framework_share_request: AssessmentFrameworkShareRequestModel = Field(
        alias="assessmentFrameworkShareRequest"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateAssessmentReportIntegrityResponseModel(BaseModel):
    signature_valid: bool = Field(alias="signatureValid")
    signature_algorithm: str = Field(alias="signatureAlgorithm")
    signature_date_time: str = Field(alias="signatureDateTime")
    signature_key_id: str = Field(alias="signatureKeyId")
    validation_errors: List[str] = Field(alias="validationErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateDelegationByAssessmentErrorModel(BaseModel):
    create_delegation_request: Optional[CreateDelegationRequestModel] = Field(
        default=None, alias="createDelegationRequest"
    )
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchCreateDelegationByAssessmentRequestModel(BaseModel):
    create_delegation_requests: Sequence[CreateDelegationRequestModel] = Field(
        alias="createDelegationRequests"
    )
    assessment_id: str = Field(alias="assessmentId")


class BatchDeleteDelegationByAssessmentResponseModel(BaseModel):
    errors: List[BatchDeleteDelegationByAssessmentErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchImportEvidenceToAssessmentControlErrorModel(BaseModel):
    manual_evidence: Optional[ManualEvidenceModel] = Field(
        default=None, alias="manualEvidence"
    )
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchImportEvidenceToAssessmentControlRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    control_set_id: str = Field(alias="controlSetId")
    control_id: str = Field(alias="controlId")
    manual_evidence: Sequence[ManualEvidenceModel] = Field(alias="manualEvidence")


class GetChangeLogsResponseModel(BaseModel):
    change_logs: List[ChangeLogModel] = Field(alias="changeLogs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ControlDomainInsightsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    controls_count_by_noncompliant_evidence: Optional[int] = Field(
        default=None, alias="controlsCountByNoncompliantEvidence"
    )
    total_controls_count: Optional[int] = Field(
        default=None, alias="totalControlsCount"
    )
    evidence_insights: Optional[EvidenceInsightsModel] = Field(
        default=None, alias="evidenceInsights"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class ControlInsightsMetadataByAssessmentItemModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    evidence_insights: Optional[EvidenceInsightsModel] = Field(
        default=None, alias="evidenceInsights"
    )
    control_set_name: Optional[str] = Field(default=None, alias="controlSetName")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class ControlInsightsMetadataItemModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    evidence_insights: Optional[EvidenceInsightsModel] = Field(
        default=None, alias="evidenceInsights"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class ControlMappingSourceModel(BaseModel):
    source_id: Optional[str] = Field(default=None, alias="sourceId")
    source_name: Optional[str] = Field(default=None, alias="sourceName")
    source_description: Optional[str] = Field(default=None, alias="sourceDescription")
    source_set_up_option: Optional[
        Literal["Procedural_Controls_Mapping", "System_Controls_Mapping"]
    ] = Field(default=None, alias="sourceSetUpOption")
    source_type: Optional[
        Literal[
            "AWS_API_Call", "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "MANUAL"
        ]
    ] = Field(default=None, alias="sourceType")
    source_keyword: Optional[SourceKeywordModel] = Field(
        default=None, alias="sourceKeyword"
    )
    source_frequency: Optional[Literal["DAILY", "MONTHLY", "WEEKLY"]] = Field(
        default=None, alias="sourceFrequency"
    )
    troubleshooting_text: Optional[str] = Field(
        default=None, alias="troubleshootingText"
    )


class CreateControlMappingSourceModel(BaseModel):
    source_name: Optional[str] = Field(default=None, alias="sourceName")
    source_description: Optional[str] = Field(default=None, alias="sourceDescription")
    source_set_up_option: Optional[
        Literal["Procedural_Controls_Mapping", "System_Controls_Mapping"]
    ] = Field(default=None, alias="sourceSetUpOption")
    source_type: Optional[
        Literal[
            "AWS_API_Call", "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "MANUAL"
        ]
    ] = Field(default=None, alias="sourceType")
    source_keyword: Optional[SourceKeywordModel] = Field(
        default=None, alias="sourceKeyword"
    )
    source_frequency: Optional[Literal["DAILY", "MONTHLY", "WEEKLY"]] = Field(
        default=None, alias="sourceFrequency"
    )
    troubleshooting_text: Optional[str] = Field(
        default=None, alias="troubleshootingText"
    )


class ListControlsResponseModel(BaseModel):
    control_metadata_list: List[ControlMetadataModel] = Field(
        alias="controlMetadataList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssessmentFrameworkControlSetModel(BaseModel):
    name: str = Field(alias="name")
    controls: Optional[Sequence[CreateAssessmentFrameworkControlModel]] = Field(
        default=None, alias="controls"
    )


class UpdateAssessmentFrameworkControlSetModel(BaseModel):
    name: str = Field(alias="name")
    controls: Sequence[CreateAssessmentFrameworkControlModel] = Field(alias="controls")
    id: Optional[str] = Field(default=None, alias="id")


class GetDelegationsResponseModel(BaseModel):
    delegations: List[DelegationMetadataModel] = Field(alias="delegations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSettingsRequestModel(BaseModel):
    sns_topic: Optional[str] = Field(default=None, alias="snsTopic")
    default_assessment_reports_destination: Optional[
        AssessmentReportsDestinationModel
    ] = Field(default=None, alias="defaultAssessmentReportsDestination")
    default_process_owners: Optional[Sequence[RoleModel]] = Field(
        default=None, alias="defaultProcessOwners"
    )
    kms_key: Optional[str] = Field(default=None, alias="kmsKey")
    evidence_finder_enabled: Optional[bool] = Field(
        default=None, alias="evidenceFinderEnabled"
    )
    deregistration_policy: Optional[DeregistrationPolicyModel] = Field(
        default=None, alias="deregistrationPolicy"
    )


class SettingsModel(BaseModel):
    is_aws_org_enabled: Optional[bool] = Field(default=None, alias="isAwsOrgEnabled")
    sns_topic: Optional[str] = Field(default=None, alias="snsTopic")
    default_assessment_reports_destination: Optional[
        AssessmentReportsDestinationModel
    ] = Field(default=None, alias="defaultAssessmentReportsDestination")
    default_process_owners: Optional[List[RoleModel]] = Field(
        default=None, alias="defaultProcessOwners"
    )
    kms_key: Optional[str] = Field(default=None, alias="kmsKey")
    evidence_finder_enablement: Optional[EvidenceFinderEnablementModel] = Field(
        default=None, alias="evidenceFinderEnablement"
    )
    deregistration_policy: Optional[DeregistrationPolicyModel] = Field(
        default=None, alias="deregistrationPolicy"
    )


class EvidenceModel(BaseModel):
    data_source: Optional[str] = Field(default=None, alias="dataSource")
    evidence_aws_account_id: Optional[str] = Field(
        default=None, alias="evidenceAwsAccountId"
    )
    time: Optional[datetime] = Field(default=None, alias="time")
    event_source: Optional[str] = Field(default=None, alias="eventSource")
    event_name: Optional[str] = Field(default=None, alias="eventName")
    evidence_by_type: Optional[str] = Field(default=None, alias="evidenceByType")
    resources_included: Optional[List[ResourceModel]] = Field(
        default=None, alias="resourcesIncluded"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="attributes")
    iam_id: Optional[str] = Field(default=None, alias="iamId")
    compliance_check: Optional[str] = Field(default=None, alias="complianceCheck")
    aws_organization: Optional[str] = Field(default=None, alias="awsOrganization")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    evidence_folder_id: Optional[str] = Field(default=None, alias="evidenceFolderId")
    id: Optional[str] = Field(default=None, alias="id")
    assessment_report_selection: Optional[str] = Field(
        default=None, alias="assessmentReportSelection"
    )


class GetAssessmentReportUrlResponseModel(BaseModel):
    pre_signed_url: URLModel = Field(alias="preSignedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightsByAssessmentResponseModel(BaseModel):
    insights: InsightsByAssessmentModel = Field(alias="insights")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInsightsResponseModel(BaseModel):
    insights: InsightsModel = Field(alias="insights")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServicesInScopeResponseModel(BaseModel):
    service_metadata: List[ServiceMetadataModel] = Field(alias="serviceMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotificationsResponseModel(BaseModel):
    notifications: List[NotificationModel] = Field(alias="notifications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    assessment_reports_destination: Optional[AssessmentReportsDestinationModel] = Field(
        default=None, alias="assessmentReportsDestination"
    )
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")
    roles: Optional[List[RoleModel]] = Field(default=None, alias="roles")
    delegations: Optional[List[DelegationModel]] = Field(
        default=None, alias="delegations"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")


class CreateAssessmentRequestModel(BaseModel):
    name: str = Field(alias="name")
    assessment_reports_destination: AssessmentReportsDestinationModel = Field(
        alias="assessmentReportsDestination"
    )
    scope: ScopeModel = Field(alias="scope")
    roles: Sequence[RoleModel] = Field(alias="roles")
    framework_id: str = Field(alias="frameworkId")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    scope: ScopeModel = Field(alias="scope")
    assessment_name: Optional[str] = Field(default=None, alias="assessmentName")
    assessment_description: Optional[str] = Field(
        default=None, alias="assessmentDescription"
    )
    assessment_reports_destination: Optional[AssessmentReportsDestinationModel] = Field(
        default=None, alias="assessmentReportsDestination"
    )
    roles: Optional[Sequence[RoleModel]] = Field(default=None, alias="roles")


class ListAssessmentsResponseModel(BaseModel):
    assessment_metadata: List[AssessmentMetadataItemModel] = Field(
        alias="assessmentMetadata"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentControlSetModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[Literal["ACTIVE", "REVIEWED", "UNDER_REVIEW"]] = Field(
        default=None, alias="status"
    )
    roles: Optional[List[RoleModel]] = Field(default=None, alias="roles")
    controls: Optional[List[AssessmentControlModel]] = Field(
        default=None, alias="controls"
    )
    delegations: Optional[List[DelegationModel]] = Field(
        default=None, alias="delegations"
    )
    system_evidence_count: Optional[int] = Field(
        default=None, alias="systemEvidenceCount"
    )
    manual_evidence_count: Optional[int] = Field(
        default=None, alias="manualEvidenceCount"
    )


class UpdateAssessmentControlResponseModel(BaseModel):
    control: AssessmentControlModel = Field(alias="control")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateDelegationByAssessmentResponseModel(BaseModel):
    delegations: List[DelegationModel] = Field(alias="delegations")
    errors: List[BatchCreateDelegationByAssessmentErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchImportEvidenceToAssessmentControlResponseModel(BaseModel):
    errors: List[BatchImportEvidenceToAssessmentControlErrorModel] = Field(
        alias="errors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListControlDomainInsightsByAssessmentResponseModel(BaseModel):
    control_domain_insights: List[ControlDomainInsightsModel] = Field(
        alias="controlDomainInsights"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListControlDomainInsightsResponseModel(BaseModel):
    control_domain_insights: List[ControlDomainInsightsModel] = Field(
        alias="controlDomainInsights"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssessmentControlInsightsByControlDomainResponseModel(BaseModel):
    control_insights_by_assessment: List[
        ControlInsightsMetadataByAssessmentItemModel
    ] = Field(alias="controlInsightsByAssessment")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListControlInsightsByControlDomainResponseModel(BaseModel):
    control_insights_metadata: List[ControlInsightsMetadataItemModel] = Field(
        alias="controlInsightsMetadata"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ControlModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[Literal["Custom", "Standard"]] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    testing_information: Optional[str] = Field(default=None, alias="testingInformation")
    action_plan_title: Optional[str] = Field(default=None, alias="actionPlanTitle")
    action_plan_instructions: Optional[str] = Field(
        default=None, alias="actionPlanInstructions"
    )
    control_sources: Optional[str] = Field(default=None, alias="controlSources")
    control_mapping_sources: Optional[List[ControlMappingSourceModel]] = Field(
        default=None, alias="controlMappingSources"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    last_updated_by: Optional[str] = Field(default=None, alias="lastUpdatedBy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateControlRequestModel(BaseModel):
    control_id: str = Field(alias="controlId")
    name: str = Field(alias="name")
    control_mapping_sources: Sequence[ControlMappingSourceModel] = Field(
        alias="controlMappingSources"
    )
    description: Optional[str] = Field(default=None, alias="description")
    testing_information: Optional[str] = Field(default=None, alias="testingInformation")
    action_plan_title: Optional[str] = Field(default=None, alias="actionPlanTitle")
    action_plan_instructions: Optional[str] = Field(
        default=None, alias="actionPlanInstructions"
    )


class CreateControlRequestModel(BaseModel):
    name: str = Field(alias="name")
    control_mapping_sources: Sequence[CreateControlMappingSourceModel] = Field(
        alias="controlMappingSources"
    )
    description: Optional[str] = Field(default=None, alias="description")
    testing_information: Optional[str] = Field(default=None, alias="testingInformation")
    action_plan_title: Optional[str] = Field(default=None, alias="actionPlanTitle")
    action_plan_instructions: Optional[str] = Field(
        default=None, alias="actionPlanInstructions"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateAssessmentFrameworkRequestModel(BaseModel):
    name: str = Field(alias="name")
    control_sets: Sequence[CreateAssessmentFrameworkControlSetModel] = Field(
        alias="controlSets"
    )
    description: Optional[str] = Field(default=None, alias="description")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateAssessmentFrameworkRequestModel(BaseModel):
    framework_id: str = Field(alias="frameworkId")
    name: str = Field(alias="name")
    control_sets: Sequence[UpdateAssessmentFrameworkControlSetModel] = Field(
        alias="controlSets"
    )
    description: Optional[str] = Field(default=None, alias="description")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")


class GetSettingsResponseModel(BaseModel):
    settings: SettingsModel = Field(alias="settings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSettingsResponseModel(BaseModel):
    settings: SettingsModel = Field(alias="settings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEvidenceByEvidenceFolderResponseModel(BaseModel):
    evidence: List[EvidenceModel] = Field(alias="evidence")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEvidenceResponseModel(BaseModel):
    evidence: EvidenceModel = Field(alias="evidence")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentFrameworkModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    metadata: Optional[FrameworkMetadataModel] = Field(default=None, alias="metadata")
    control_sets: Optional[List[AssessmentControlSetModel]] = Field(
        default=None, alias="controlSets"
    )


class UpdateAssessmentControlSetStatusResponseModel(BaseModel):
    control_set: AssessmentControlSetModel = Field(alias="controlSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ControlSetModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    controls: Optional[List[ControlModel]] = Field(default=None, alias="controls")


class CreateControlResponseModel(BaseModel):
    control: ControlModel = Field(alias="control")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetControlResponseModel(BaseModel):
    control: ControlModel = Field(alias="control")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateControlResponseModel(BaseModel):
    control: ControlModel = Field(alias="control")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssessmentModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    aws_account: Optional[AWSAccountModel] = Field(default=None, alias="awsAccount")
    metadata: Optional[AssessmentMetadataModel] = Field(default=None, alias="metadata")
    framework: Optional[AssessmentFrameworkModel] = Field(
        default=None, alias="framework"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class FrameworkModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["Custom", "Standard"]] = Field(default=None, alias="type")
    compliance_type: Optional[str] = Field(default=None, alias="complianceType")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    control_sources: Optional[str] = Field(default=None, alias="controlSources")
    control_sets: Optional[List[ControlSetModel]] = Field(
        default=None, alias="controlSets"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    last_updated_by: Optional[str] = Field(default=None, alias="lastUpdatedBy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateAssessmentResponseModel(BaseModel):
    assessment: AssessmentModel = Field(alias="assessment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssessmentResponseModel(BaseModel):
    assessment: AssessmentModel = Field(alias="assessment")
    user_role: RoleModel = Field(alias="userRole")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssessmentResponseModel(BaseModel):
    assessment: AssessmentModel = Field(alias="assessment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssessmentStatusResponseModel(BaseModel):
    assessment: AssessmentModel = Field(alias="assessment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssessmentFrameworkResponseModel(BaseModel):
    framework: FrameworkModel = Field(alias="framework")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssessmentFrameworkResponseModel(BaseModel):
    framework: FrameworkModel = Field(alias="framework")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssessmentFrameworkResponseModel(BaseModel):
    framework: FrameworkModel = Field(alias="framework")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
