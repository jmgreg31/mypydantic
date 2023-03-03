# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ChoiceContentModel(BaseModel):
    display_text: Optional[str] = Field(default=None, alias="DisplayText")
    url: Optional[str] = Field(default=None, alias="Url")


class ChoiceAnswerSummaryModel(BaseModel):
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    status: Optional[Literal["NOT_APPLICABLE", "SELECTED", "UNSELECTED"]] = Field(
        default=None, alias="Status"
    )
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")


class ChoiceAnswerModel(BaseModel):
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    status: Optional[Literal["NOT_APPLICABLE", "SELECTED", "UNSELECTED"]] = Field(
        default=None, alias="Status"
    )
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")
    notes: Optional[str] = Field(default=None, alias="Notes")


class AssociateLensesInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_aliases: Sequence[str] = Field(alias="LensAliases")


class CheckDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    provider: Optional[Literal["TRUSTED_ADVISOR"]] = Field(
        default=None, alias="Provider"
    )
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    status: Optional[
        Literal["ERROR", "FETCH_FAILED", "NOT_AVAILABLE", "OKAY", "WARNING"]
    ] = Field(default=None, alias="Status")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    flagged_resources: Optional[int] = Field(default=None, alias="FlaggedResources")
    reason: Optional[
        Literal[
            "ACCESS_DENIED",
            "ASSUME_ROLE_ERROR",
            "PREMIUM_SUPPORT_REQUIRED",
            "UNKNOWN_ERROR",
        ]
    ] = Field(default=None, alias="Reason")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class CheckSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    provider: Optional[Literal["TRUSTED_ADVISOR"]] = Field(
        default=None, alias="Provider"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    status: Optional[
        Literal["ERROR", "FETCH_FAILED", "NOT_AVAILABLE", "OKAY", "WARNING"]
    ] = Field(default=None, alias="Status")
    account_summary: Optional[
        Dict[Literal["ERROR", "FETCH_FAILED", "NOT_AVAILABLE", "OKAY", "WARNING"], int]
    ] = Field(default=None, alias="AccountSummary")


class ChoiceImprovementPlanModel(BaseModel):
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    display_text: Optional[str] = Field(default=None, alias="DisplayText")
    improvement_plan_url: Optional[str] = Field(
        default=None, alias="ImprovementPlanUrl"
    )


class ChoiceUpdateModel(BaseModel):
    status: Literal["NOT_APPLICABLE", "SELECTED", "UNSELECTED"] = Field(alias="Status")
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")
    notes: Optional[str] = Field(default=None, alias="Notes")


class CreateLensShareInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    shared_with: str = Field(alias="SharedWith")
    client_request_token: str = Field(alias="ClientRequestToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateLensVersionInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    lens_version: str = Field(alias="LensVersion")
    client_request_token: str = Field(alias="ClientRequestToken")
    is_major_version: Optional[bool] = Field(default=None, alias="IsMajorVersion")


class CreateMilestoneInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_name: str = Field(alias="MilestoneName")
    client_request_token: str = Field(alias="ClientRequestToken")


class WorkloadDiscoveryConfigModel(BaseModel):
    trusted_advisor_integration_status: Optional[
        Literal["DISABLED", "ENABLED"]
    ] = Field(default=None, alias="TrustedAdvisorIntegrationStatus")


class CreateWorkloadShareInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    shared_with: str = Field(alias="SharedWith")
    permission_type: Literal["CONTRIBUTOR", "READONLY"] = Field(alias="PermissionType")
    client_request_token: str = Field(alias="ClientRequestToken")


class DeleteLensInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    client_request_token: str = Field(alias="ClientRequestToken")
    lens_status: Literal["ALL", "DRAFT", "PUBLISHED"] = Field(alias="LensStatus")


class DeleteLensShareInputRequestModel(BaseModel):
    share_id: str = Field(alias="ShareId")
    lens_alias: str = Field(alias="LensAlias")
    client_request_token: str = Field(alias="ClientRequestToken")


class DeleteWorkloadInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    client_request_token: str = Field(alias="ClientRequestToken")


class DeleteWorkloadShareInputRequestModel(BaseModel):
    share_id: str = Field(alias="ShareId")
    workload_id: str = Field(alias="WorkloadId")
    client_request_token: str = Field(alias="ClientRequestToken")


class DisassociateLensesInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_aliases: Sequence[str] = Field(alias="LensAliases")


class ExportLensInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")


class GetAnswerInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    question_id: str = Field(alias="QuestionId")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")


class GetLensInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")


class LensModel(BaseModel):
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    owner: Optional[str] = Field(default=None, alias="Owner")
    share_invitation_id: Optional[str] = Field(default=None, alias="ShareInvitationId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetLensReviewInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")


class GetLensReviewReportInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")


class LensReviewReportModel(BaseModel):
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    base64_string: Optional[str] = Field(default=None, alias="Base64String")


class GetLensVersionDifferenceInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    base_lens_version: Optional[str] = Field(default=None, alias="BaseLensVersion")
    target_lens_version: Optional[str] = Field(default=None, alias="TargetLensVersion")


class GetMilestoneInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")


class GetWorkloadInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")


class ImportLensInputRequestModel(BaseModel):
    js_onstring: str = Field(alias="JSONString")
    client_request_token: str = Field(alias="ClientRequestToken")
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class LensReviewSummaryModel(BaseModel):
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")
    lens_name: Optional[str] = Field(default=None, alias="LensName")
    lens_status: Optional[
        Literal["CURRENT", "DELETED", "DEPRECATED", "NOT_CURRENT", "UNSHARED"]
    ] = Field(default=None, alias="LensStatus")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    risk_counts: Optional[
        Dict[Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"], int]
    ] = Field(default=None, alias="RiskCounts")


class PillarReviewSummaryModel(BaseModel):
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    pillar_name: Optional[str] = Field(default=None, alias="PillarName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    risk_counts: Optional[
        Dict[Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"], int]
    ] = Field(default=None, alias="RiskCounts")


class LensShareSummaryModel(BaseModel):
    share_id: Optional[str] = Field(default=None, alias="ShareId")
    shared_with: Optional[str] = Field(default=None, alias="SharedWith")
    status: Optional[
        Literal[
            "ACCEPTED",
            "ASSOCIATED",
            "ASSOCIATING",
            "EXPIRED",
            "FAILED",
            "PENDING",
            "REJECTED",
            "REVOKED",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class LensSummaryModel(BaseModel):
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_name: Optional[str] = Field(default=None, alias="LensName")
    lens_type: Optional[
        Literal["AWS_OFFICIAL", "CUSTOM_SELF", "CUSTOM_SHARED"]
    ] = Field(default=None, alias="LensType")
    description: Optional[str] = Field(default=None, alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")
    owner: Optional[str] = Field(default=None, alias="Owner")
    lens_status: Optional[
        Literal["CURRENT", "DELETED", "DEPRECATED", "NOT_CURRENT", "UNSHARED"]
    ] = Field(default=None, alias="LensStatus")


class LensUpgradeSummaryModel(BaseModel):
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    current_lens_version: Optional[str] = Field(
        default=None, alias="CurrentLensVersion"
    )
    latest_lens_version: Optional[str] = Field(default=None, alias="LatestLensVersion")


class ListAnswersInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCheckDetailsInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_arn: str = Field(alias="LensArn")
    pillar_id: str = Field(alias="PillarId")
    question_id: str = Field(alias="QuestionId")
    choice_id: str = Field(alias="ChoiceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCheckSummariesInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_arn: str = Field(alias="LensArn")
    pillar_id: str = Field(alias="PillarId")
    question_id: str = Field(alias="QuestionId")
    choice_id: str = Field(alias="ChoiceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLensReviewImprovementsInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLensReviewsInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLensSharesInputRequestModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    shared_with_prefix: Optional[str] = Field(default=None, alias="SharedWithPrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[
        Literal[
            "ACCEPTED",
            "ASSOCIATED",
            "ASSOCIATING",
            "EXPIRED",
            "FAILED",
            "PENDING",
            "REJECTED",
            "REVOKED",
        ]
    ] = Field(default=None, alias="Status")


class ListLensesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    lens_type: Optional[
        Literal["AWS_OFFICIAL", "CUSTOM_SELF", "CUSTOM_SHARED"]
    ] = Field(default=None, alias="LensType")
    lens_status: Optional[Literal["ALL", "DRAFT", "PUBLISHED"]] = Field(
        default=None, alias="LensStatus"
    )
    lens_name: Optional[str] = Field(default=None, alias="LensName")


class ListMilestonesInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListNotificationsInputRequestModel(BaseModel):
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListShareInvitationsInputRequestModel(BaseModel):
    workload_name_prefix: Optional[str] = Field(
        default=None, alias="WorkloadNamePrefix"
    )
    lens_name_prefix: Optional[str] = Field(default=None, alias="LensNamePrefix")
    share_resource_type: Optional[Literal["LENS", "WORKLOAD"]] = Field(
        default=None, alias="ShareResourceType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ShareInvitationSummaryModel(BaseModel):
    share_invitation_id: Optional[str] = Field(default=None, alias="ShareInvitationId")
    shared_by: Optional[str] = Field(default=None, alias="SharedBy")
    shared_with: Optional[str] = Field(default=None, alias="SharedWith")
    permission_type: Optional[Literal["CONTRIBUTOR", "READONLY"]] = Field(
        default=None, alias="PermissionType"
    )
    share_resource_type: Optional[Literal["LENS", "WORKLOAD"]] = Field(
        default=None, alias="ShareResourceType"
    )
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    lens_name: Optional[str] = Field(default=None, alias="LensName")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")


class ListTagsForResourceInputRequestModel(BaseModel):
    workload_arn: str = Field(alias="WorkloadArn")


class ListWorkloadSharesInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    shared_with_prefix: Optional[str] = Field(default=None, alias="SharedWithPrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[
        Literal[
            "ACCEPTED",
            "ASSOCIATED",
            "ASSOCIATING",
            "EXPIRED",
            "FAILED",
            "PENDING",
            "REJECTED",
            "REVOKED",
        ]
    ] = Field(default=None, alias="Status")


class WorkloadShareSummaryModel(BaseModel):
    share_id: Optional[str] = Field(default=None, alias="ShareId")
    shared_with: Optional[str] = Field(default=None, alias="SharedWith")
    permission_type: Optional[Literal["CONTRIBUTOR", "READONLY"]] = Field(
        default=None, alias="PermissionType"
    )
    status: Optional[
        Literal[
            "ACCEPTED",
            "ASSOCIATED",
            "ASSOCIATING",
            "EXPIRED",
            "FAILED",
            "PENDING",
            "REJECTED",
            "REVOKED",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ListWorkloadsInputRequestModel(BaseModel):
    workload_name_prefix: Optional[str] = Field(
        default=None, alias="WorkloadNamePrefix"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class WorkloadSummaryModel(BaseModel):
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    workload_arn: Optional[str] = Field(default=None, alias="WorkloadArn")
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    lenses: Optional[List[str]] = Field(default=None, alias="Lenses")
    risk_counts: Optional[
        Dict[Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"], int]
    ] = Field(default=None, alias="RiskCounts")
    improvement_status: Optional[
        Literal[
            "COMPLETE",
            "IN_PROGRESS",
            "NOT_APPLICABLE",
            "NOT_STARTED",
            "RISK_ACKNOWLEDGED",
        ]
    ] = Field(default=None, alias="ImprovementStatus")


class QuestionDifferenceModel(BaseModel):
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    question_title: Optional[str] = Field(default=None, alias="QuestionTitle")
    difference_status: Optional[Literal["DELETED", "NEW", "UPDATED"]] = Field(
        default=None, alias="DifferenceStatus"
    )


class ShareInvitationModel(BaseModel):
    share_invitation_id: Optional[str] = Field(default=None, alias="ShareInvitationId")
    share_resource_type: Optional[Literal["LENS", "WORKLOAD"]] = Field(
        default=None, alias="ShareResourceType"
    )
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")


class TagResourceInputRequestModel(BaseModel):
    workload_arn: str = Field(alias="WorkloadArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceInputRequestModel(BaseModel):
    workload_arn: str = Field(alias="WorkloadArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateGlobalSettingsInputRequestModel(BaseModel):
    organization_sharing_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OrganizationSharingStatus"
    )


class UpdateLensReviewInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    lens_notes: Optional[str] = Field(default=None, alias="LensNotes")
    pillar_notes: Optional[Mapping[str, str]] = Field(default=None, alias="PillarNotes")


class UpdateShareInvitationInputRequestModel(BaseModel):
    share_invitation_id: str = Field(alias="ShareInvitationId")
    share_invitation_action: Literal["ACCEPT", "REJECT"] = Field(
        alias="ShareInvitationAction"
    )


class UpdateWorkloadShareInputRequestModel(BaseModel):
    share_id: str = Field(alias="ShareId")
    workload_id: str = Field(alias="WorkloadId")
    permission_type: Literal["CONTRIBUTOR", "READONLY"] = Field(alias="PermissionType")


class WorkloadShareModel(BaseModel):
    share_id: Optional[str] = Field(default=None, alias="ShareId")
    shared_by: Optional[str] = Field(default=None, alias="SharedBy")
    shared_with: Optional[str] = Field(default=None, alias="SharedWith")
    permission_type: Optional[Literal["CONTRIBUTOR", "READONLY"]] = Field(
        default=None, alias="PermissionType"
    )
    status: Optional[
        Literal[
            "ACCEPTED",
            "ASSOCIATED",
            "ASSOCIATING",
            "EXPIRED",
            "FAILED",
            "PENDING",
            "REJECTED",
            "REVOKED",
        ]
    ] = Field(default=None, alias="Status")
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")


class UpgradeLensReviewInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    milestone_name: str = Field(alias="MilestoneName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class AdditionalResourcesModel(BaseModel):
    type: Optional[Literal["HELPFUL_RESOURCE", "IMPROVEMENT_PLAN"]] = Field(
        default=None, alias="Type"
    )
    content: Optional[List[ChoiceContentModel]] = Field(default=None, alias="Content")


class ImprovementSummaryModel(BaseModel):
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    question_title: Optional[str] = Field(default=None, alias="QuestionTitle")
    risk: Optional[
        Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
    ] = Field(default=None, alias="Risk")
    improvement_plan_url: Optional[str] = Field(
        default=None, alias="ImprovementPlanUrl"
    )
    improvement_plans: Optional[List[ChoiceImprovementPlanModel]] = Field(
        default=None, alias="ImprovementPlans"
    )


class UpdateAnswerInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    question_id: str = Field(alias="QuestionId")
    selected_choices: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedChoices"
    )
    choice_updates: Optional[Mapping[str, ChoiceUpdateModel]] = Field(
        default=None, alias="ChoiceUpdates"
    )
    notes: Optional[str] = Field(default=None, alias="Notes")
    is_applicable: Optional[bool] = Field(default=None, alias="IsApplicable")
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")


class CreateLensShareOutputModel(BaseModel):
    share_id: str = Field(alias="ShareId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLensVersionOutputModel(BaseModel):
    lens_arn: str = Field(alias="LensArn")
    lens_version: str = Field(alias="LensVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMilestoneOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkloadOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    workload_arn: str = Field(alias="WorkloadArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkloadShareOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    share_id: str = Field(alias="ShareId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportLensOutputModel(BaseModel):
    lens_js_on: str = Field(alias="LensJSON")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportLensOutputModel(BaseModel):
    lens_arn: str = Field(alias="LensArn")
    status: Literal["COMPLETE", "ERROR", "IN_PROGRESS"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCheckDetailsOutputModel(BaseModel):
    check_details: List[CheckDetailModel] = Field(alias="CheckDetails")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCheckSummariesOutputModel(BaseModel):
    check_summaries: List[CheckSummaryModel] = Field(alias="CheckSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkloadInputRequestModel(BaseModel):
    workload_name: str = Field(alias="WorkloadName")
    description: str = Field(alias="Description")
    environment: Literal["PREPRODUCTION", "PRODUCTION"] = Field(alias="Environment")
    lenses: Sequence[str] = Field(alias="Lenses")
    client_request_token: str = Field(alias="ClientRequestToken")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    aws_regions: Optional[Sequence[str]] = Field(default=None, alias="AwsRegions")
    non_aws_regions: Optional[Sequence[str]] = Field(
        default=None, alias="NonAwsRegions"
    )
    pillar_priorities: Optional[Sequence[str]] = Field(
        default=None, alias="PillarPriorities"
    )
    architectural_design: Optional[str] = Field(
        default=None, alias="ArchitecturalDesign"
    )
    review_owner: Optional[str] = Field(default=None, alias="ReviewOwner")
    industry_type: Optional[str] = Field(default=None, alias="IndustryType")
    industry: Optional[str] = Field(default=None, alias="Industry")
    notes: Optional[str] = Field(default=None, alias="Notes")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    discovery_config: Optional[WorkloadDiscoveryConfigModel] = Field(
        default=None, alias="DiscoveryConfig"
    )
    applications: Optional[Sequence[str]] = Field(default=None, alias="Applications")


class UpdateWorkloadInputRequestModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    description: Optional[str] = Field(default=None, alias="Description")
    environment: Optional[Literal["PREPRODUCTION", "PRODUCTION"]] = Field(
        default=None, alias="Environment"
    )
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    aws_regions: Optional[Sequence[str]] = Field(default=None, alias="AwsRegions")
    non_aws_regions: Optional[Sequence[str]] = Field(
        default=None, alias="NonAwsRegions"
    )
    pillar_priorities: Optional[Sequence[str]] = Field(
        default=None, alias="PillarPriorities"
    )
    architectural_design: Optional[str] = Field(
        default=None, alias="ArchitecturalDesign"
    )
    review_owner: Optional[str] = Field(default=None, alias="ReviewOwner")
    is_review_owner_update_acknowledged: Optional[bool] = Field(
        default=None, alias="IsReviewOwnerUpdateAcknowledged"
    )
    industry_type: Optional[str] = Field(default=None, alias="IndustryType")
    industry: Optional[str] = Field(default=None, alias="Industry")
    notes: Optional[str] = Field(default=None, alias="Notes")
    improvement_status: Optional[
        Literal[
            "COMPLETE",
            "IN_PROGRESS",
            "NOT_APPLICABLE",
            "NOT_STARTED",
            "RISK_ACKNOWLEDGED",
        ]
    ] = Field(default=None, alias="ImprovementStatus")
    discovery_config: Optional[WorkloadDiscoveryConfigModel] = Field(
        default=None, alias="DiscoveryConfig"
    )
    applications: Optional[Sequence[str]] = Field(default=None, alias="Applications")


class WorkloadModel(BaseModel):
    workload_id: Optional[str] = Field(default=None, alias="WorkloadId")
    workload_arn: Optional[str] = Field(default=None, alias="WorkloadArn")
    workload_name: Optional[str] = Field(default=None, alias="WorkloadName")
    description: Optional[str] = Field(default=None, alias="Description")
    environment: Optional[Literal["PREPRODUCTION", "PRODUCTION"]] = Field(
        default=None, alias="Environment"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    account_ids: Optional[List[str]] = Field(default=None, alias="AccountIds")
    aws_regions: Optional[List[str]] = Field(default=None, alias="AwsRegions")
    non_aws_regions: Optional[List[str]] = Field(default=None, alias="NonAwsRegions")
    architectural_design: Optional[str] = Field(
        default=None, alias="ArchitecturalDesign"
    )
    review_owner: Optional[str] = Field(default=None, alias="ReviewOwner")
    review_restriction_date: Optional[datetime] = Field(
        default=None, alias="ReviewRestrictionDate"
    )
    is_review_owner_update_acknowledged: Optional[bool] = Field(
        default=None, alias="IsReviewOwnerUpdateAcknowledged"
    )
    industry_type: Optional[str] = Field(default=None, alias="IndustryType")
    industry: Optional[str] = Field(default=None, alias="Industry")
    notes: Optional[str] = Field(default=None, alias="Notes")
    improvement_status: Optional[
        Literal[
            "COMPLETE",
            "IN_PROGRESS",
            "NOT_APPLICABLE",
            "NOT_STARTED",
            "RISK_ACKNOWLEDGED",
        ]
    ] = Field(default=None, alias="ImprovementStatus")
    risk_counts: Optional[
        Dict[Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"], int]
    ] = Field(default=None, alias="RiskCounts")
    pillar_priorities: Optional[List[str]] = Field(
        default=None, alias="PillarPriorities"
    )
    lenses: Optional[List[str]] = Field(default=None, alias="Lenses")
    owner: Optional[str] = Field(default=None, alias="Owner")
    share_invitation_id: Optional[str] = Field(default=None, alias="ShareInvitationId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    discovery_config: Optional[WorkloadDiscoveryConfigModel] = Field(
        default=None, alias="DiscoveryConfig"
    )
    applications: Optional[List[str]] = Field(default=None, alias="Applications")


class GetLensOutputModel(BaseModel):
    lens: LensModel = Field(alias="Lens")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLensReviewReportOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_review_report: LensReviewReportModel = Field(alias="LensReviewReport")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLensReviewsOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_review_summaries: List[LensReviewSummaryModel] = Field(
        alias="LensReviewSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LensReviewModel(BaseModel):
    lens_alias: Optional[str] = Field(default=None, alias="LensAlias")
    lens_arn: Optional[str] = Field(default=None, alias="LensArn")
    lens_version: Optional[str] = Field(default=None, alias="LensVersion")
    lens_name: Optional[str] = Field(default=None, alias="LensName")
    lens_status: Optional[
        Literal["CURRENT", "DELETED", "DEPRECATED", "NOT_CURRENT", "UNSHARED"]
    ] = Field(default=None, alias="LensStatus")
    pillar_review_summaries: Optional[List[PillarReviewSummaryModel]] = Field(
        default=None, alias="PillarReviewSummaries"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    notes: Optional[str] = Field(default=None, alias="Notes")
    risk_counts: Optional[
        Dict[Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"], int]
    ] = Field(default=None, alias="RiskCounts")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLensSharesOutputModel(BaseModel):
    lens_share_summaries: List[LensShareSummaryModel] = Field(
        alias="LensShareSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLensesOutputModel(BaseModel):
    lens_summaries: List[LensSummaryModel] = Field(alias="LensSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NotificationSummaryModel(BaseModel):
    type: Optional[Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]] = Field(
        default=None, alias="Type"
    )
    lens_upgrade_summary: Optional[LensUpgradeSummaryModel] = Field(
        default=None, alias="LensUpgradeSummary"
    )


class ListShareInvitationsOutputModel(BaseModel):
    share_invitation_summaries: List[ShareInvitationSummaryModel] = Field(
        alias="ShareInvitationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkloadSharesOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    workload_share_summaries: List[WorkloadShareSummaryModel] = Field(
        alias="WorkloadShareSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkloadsOutputModel(BaseModel):
    workload_summaries: List[WorkloadSummaryModel] = Field(alias="WorkloadSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MilestoneSummaryModel(BaseModel):
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")
    milestone_name: Optional[str] = Field(default=None, alias="MilestoneName")
    recorded_at: Optional[datetime] = Field(default=None, alias="RecordedAt")
    workload_summary: Optional[WorkloadSummaryModel] = Field(
        default=None, alias="WorkloadSummary"
    )


class PillarDifferenceModel(BaseModel):
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    pillar_name: Optional[str] = Field(default=None, alias="PillarName")
    difference_status: Optional[Literal["DELETED", "NEW", "UPDATED"]] = Field(
        default=None, alias="DifferenceStatus"
    )
    question_differences: Optional[List[QuestionDifferenceModel]] = Field(
        default=None, alias="QuestionDifferences"
    )


class UpdateShareInvitationOutputModel(BaseModel):
    share_invitation: ShareInvitationModel = Field(alias="ShareInvitation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWorkloadShareOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    workload_share: WorkloadShareModel = Field(alias="WorkloadShare")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChoiceModel(BaseModel):
    choice_id: Optional[str] = Field(default=None, alias="ChoiceId")
    title: Optional[str] = Field(default=None, alias="Title")
    description: Optional[str] = Field(default=None, alias="Description")
    helpful_resource: Optional[ChoiceContentModel] = Field(
        default=None, alias="HelpfulResource"
    )
    improvement_plan: Optional[ChoiceContentModel] = Field(
        default=None, alias="ImprovementPlan"
    )
    additional_resources: Optional[List[AdditionalResourcesModel]] = Field(
        default=None, alias="AdditionalResources"
    )


class ListLensReviewImprovementsOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_alias: str = Field(alias="LensAlias")
    lens_arn: str = Field(alias="LensArn")
    improvement_summaries: List[ImprovementSummaryModel] = Field(
        alias="ImprovementSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkloadOutputModel(BaseModel):
    workload: WorkloadModel = Field(alias="Workload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MilestoneModel(BaseModel):
    milestone_number: Optional[int] = Field(default=None, alias="MilestoneNumber")
    milestone_name: Optional[str] = Field(default=None, alias="MilestoneName")
    recorded_at: Optional[datetime] = Field(default=None, alias="RecordedAt")
    workload: Optional[WorkloadModel] = Field(default=None, alias="Workload")


class UpdateWorkloadOutputModel(BaseModel):
    workload: WorkloadModel = Field(alias="Workload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLensReviewOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_review: LensReviewModel = Field(alias="LensReview")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLensReviewOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_review: LensReviewModel = Field(alias="LensReview")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNotificationsOutputModel(BaseModel):
    notification_summaries: List[NotificationSummaryModel] = Field(
        alias="NotificationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMilestonesOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_summaries: List[MilestoneSummaryModel] = Field(alias="MilestoneSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VersionDifferencesModel(BaseModel):
    pillar_differences: Optional[List[PillarDifferenceModel]] = Field(
        default=None, alias="PillarDifferences"
    )


class AnswerSummaryModel(BaseModel):
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    question_title: Optional[str] = Field(default=None, alias="QuestionTitle")
    choices: Optional[List[ChoiceModel]] = Field(default=None, alias="Choices")
    selected_choices: Optional[List[str]] = Field(default=None, alias="SelectedChoices")
    choice_answer_summaries: Optional[List[ChoiceAnswerSummaryModel]] = Field(
        default=None, alias="ChoiceAnswerSummaries"
    )
    is_applicable: Optional[bool] = Field(default=None, alias="IsApplicable")
    risk: Optional[
        Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
    ] = Field(default=None, alias="Risk")
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")


class AnswerModel(BaseModel):
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    pillar_id: Optional[str] = Field(default=None, alias="PillarId")
    question_title: Optional[str] = Field(default=None, alias="QuestionTitle")
    question_description: Optional[str] = Field(
        default=None, alias="QuestionDescription"
    )
    improvement_plan_url: Optional[str] = Field(
        default=None, alias="ImprovementPlanUrl"
    )
    helpful_resource_url: Optional[str] = Field(
        default=None, alias="HelpfulResourceUrl"
    )
    helpful_resource_display_text: Optional[str] = Field(
        default=None, alias="HelpfulResourceDisplayText"
    )
    choices: Optional[List[ChoiceModel]] = Field(default=None, alias="Choices")
    selected_choices: Optional[List[str]] = Field(default=None, alias="SelectedChoices")
    choice_answers: Optional[List[ChoiceAnswerModel]] = Field(
        default=None, alias="ChoiceAnswers"
    )
    is_applicable: Optional[bool] = Field(default=None, alias="IsApplicable")
    risk: Optional[
        Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
    ] = Field(default=None, alias="Risk")
    notes: Optional[str] = Field(default=None, alias="Notes")
    reason: Optional[
        Literal[
            "ARCHITECTURE_CONSTRAINTS",
            "BUSINESS_PRIORITIES",
            "NONE",
            "OTHER",
            "OUT_OF_SCOPE",
        ]
    ] = Field(default=None, alias="Reason")


class GetMilestoneOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone: MilestoneModel = Field(alias="Milestone")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLensVersionDifferenceOutputModel(BaseModel):
    lens_alias: str = Field(alias="LensAlias")
    lens_arn: str = Field(alias="LensArn")
    base_lens_version: str = Field(alias="BaseLensVersion")
    target_lens_version: str = Field(alias="TargetLensVersion")
    latest_lens_version: str = Field(alias="LatestLensVersion")
    version_differences: VersionDifferencesModel = Field(alias="VersionDifferences")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnswersOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_alias: str = Field(alias="LensAlias")
    lens_arn: str = Field(alias="LensArn")
    answer_summaries: List[AnswerSummaryModel] = Field(alias="AnswerSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnswerOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    milestone_number: int = Field(alias="MilestoneNumber")
    lens_alias: str = Field(alias="LensAlias")
    lens_arn: str = Field(alias="LensArn")
    answer: AnswerModel = Field(alias="Answer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnswerOutputModel(BaseModel):
    workload_id: str = Field(alias="WorkloadId")
    lens_alias: str = Field(alias="LensAlias")
    lens_arn: str = Field(alias="LensArn")
    answer: AnswerModel = Field(alias="Answer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
