# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AttachmentModel(BaseModel):
    file_name: Optional[str] = Field(default=None, alias="fileName")
    data: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="data"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddCommunicationToCaseRequestModel(BaseModel):
    communication_body: str = Field(alias="communicationBody")
    case_id: Optional[str] = Field(default=None, alias="caseId")
    cc_email_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ccEmailAddresses"
    )
    attachment_set_id: Optional[str] = Field(default=None, alias="attachmentSetId")


class AttachmentDetailsModel(BaseModel):
    attachment_id: Optional[str] = Field(default=None, alias="attachmentId")
    file_name: Optional[str] = Field(default=None, alias="fileName")


class CategoryModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    name: Optional[str] = Field(default=None, alias="name")


class CreateCaseRequestModel(BaseModel):
    subject: str = Field(alias="subject")
    communication_body: str = Field(alias="communicationBody")
    service_code: Optional[str] = Field(default=None, alias="serviceCode")
    severity_code: Optional[str] = Field(default=None, alias="severityCode")
    category_code: Optional[str] = Field(default=None, alias="categoryCode")
    cc_email_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="ccEmailAddresses"
    )
    language: Optional[str] = Field(default=None, alias="language")
    issue_type: Optional[str] = Field(default=None, alias="issueType")
    attachment_set_id: Optional[str] = Field(default=None, alias="attachmentSetId")


class DescribeAttachmentRequestModel(BaseModel):
    attachment_id: str = Field(alias="attachmentId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeCasesRequestModel(BaseModel):
    case_id_list: Optional[Sequence[str]] = Field(default=None, alias="caseIdList")
    display_id: Optional[str] = Field(default=None, alias="displayId")
    after_time: Optional[str] = Field(default=None, alias="afterTime")
    before_time: Optional[str] = Field(default=None, alias="beforeTime")
    include_resolved_cases: Optional[bool] = Field(
        default=None, alias="includeResolvedCases"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    language: Optional[str] = Field(default=None, alias="language")
    include_communications: Optional[bool] = Field(
        default=None, alias="includeCommunications"
    )


class DescribeCommunicationsRequestModel(BaseModel):
    case_id: str = Field(alias="caseId")
    before_time: Optional[str] = Field(default=None, alias="beforeTime")
    after_time: Optional[str] = Field(default=None, alias="afterTime")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeServicesRequestModel(BaseModel):
    service_code_list: Optional[Sequence[str]] = Field(
        default=None, alias="serviceCodeList"
    )
    language: Optional[str] = Field(default=None, alias="language")


class DescribeSeverityLevelsRequestModel(BaseModel):
    language: Optional[str] = Field(default=None, alias="language")


class SeverityLevelModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    name: Optional[str] = Field(default=None, alias="name")


class DescribeTrustedAdvisorCheckRefreshStatusesRequestModel(BaseModel):
    check_ids: Sequence[str] = Field(alias="checkIds")


class TrustedAdvisorCheckRefreshStatusModel(BaseModel):
    check_id: str = Field(alias="checkId")
    status: str = Field(alias="status")
    millis_until_next_refreshable: int = Field(alias="millisUntilNextRefreshable")


class DescribeTrustedAdvisorCheckResultRequestModel(BaseModel):
    check_id: str = Field(alias="checkId")
    language: Optional[str] = Field(default=None, alias="language")


class DescribeTrustedAdvisorCheckSummariesRequestModel(BaseModel):
    check_ids: Sequence[str] = Field(alias="checkIds")


class DescribeTrustedAdvisorChecksRequestModel(BaseModel):
    language: str = Field(alias="language")


class TrustedAdvisorCheckDescriptionModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    category: str = Field(alias="category")
    metadata: List[str] = Field(alias="metadata")


class RefreshTrustedAdvisorCheckRequestModel(BaseModel):
    check_id: str = Field(alias="checkId")


class ResolveCaseRequestModel(BaseModel):
    case_id: Optional[str] = Field(default=None, alias="caseId")


class TrustedAdvisorCostOptimizingSummaryModel(BaseModel):
    estimated_monthly_savings: float = Field(alias="estimatedMonthlySavings")
    estimated_percent_monthly_savings: float = Field(
        alias="estimatedPercentMonthlySavings"
    )


class TrustedAdvisorResourceDetailModel(BaseModel):
    status: str = Field(alias="status")
    resource_id: str = Field(alias="resourceId")
    metadata: List[str] = Field(alias="metadata")
    region: Optional[str] = Field(default=None, alias="region")
    is_suppressed: Optional[bool] = Field(default=None, alias="isSuppressed")


class TrustedAdvisorResourcesSummaryModel(BaseModel):
    resources_processed: int = Field(alias="resourcesProcessed")
    resources_flagged: int = Field(alias="resourcesFlagged")
    resources_ignored: int = Field(alias="resourcesIgnored")
    resources_suppressed: int = Field(alias="resourcesSuppressed")


class AddAttachmentsToSetRequestModel(BaseModel):
    attachments: Sequence[AttachmentModel] = Field(alias="attachments")
    attachment_set_id: Optional[str] = Field(default=None, alias="attachmentSetId")


class AddAttachmentsToSetResponseModel(BaseModel):
    attachment_set_id: str = Field(alias="attachmentSetId")
    expiry_time: str = Field(alias="expiryTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddCommunicationToCaseResponseModel(BaseModel):
    result: bool = Field(alias="result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCaseResponseModel(BaseModel):
    case_id: str = Field(alias="caseId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAttachmentResponseModel(BaseModel):
    attachment: AttachmentModel = Field(alias="attachment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResolveCaseResponseModel(BaseModel):
    initial_case_status: str = Field(alias="initialCaseStatus")
    final_case_status: str = Field(alias="finalCaseStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommunicationModel(BaseModel):
    case_id: Optional[str] = Field(default=None, alias="caseId")
    body: Optional[str] = Field(default=None, alias="body")
    submitted_by: Optional[str] = Field(default=None, alias="submittedBy")
    time_created: Optional[str] = Field(default=None, alias="timeCreated")
    attachment_set: Optional[List[AttachmentDetailsModel]] = Field(
        default=None, alias="attachmentSet"
    )


class ServiceModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    name: Optional[str] = Field(default=None, alias="name")
    categories: Optional[List[CategoryModel]] = Field(default=None, alias="categories")


class DescribeCasesRequestDescribeCasesPaginateModel(BaseModel):
    case_id_list: Optional[Sequence[str]] = Field(default=None, alias="caseIdList")
    display_id: Optional[str] = Field(default=None, alias="displayId")
    after_time: Optional[str] = Field(default=None, alias="afterTime")
    before_time: Optional[str] = Field(default=None, alias="beforeTime")
    include_resolved_cases: Optional[bool] = Field(
        default=None, alias="includeResolvedCases"
    )
    language: Optional[str] = Field(default=None, alias="language")
    include_communications: Optional[bool] = Field(
        default=None, alias="includeCommunications"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeCommunicationsRequestDescribeCommunicationsPaginateModel(BaseModel):
    case_id: str = Field(alias="caseId")
    before_time: Optional[str] = Field(default=None, alias="beforeTime")
    after_time: Optional[str] = Field(default=None, alias="afterTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSeverityLevelsResponseModel(BaseModel):
    severity_levels: List[SeverityLevelModel] = Field(alias="severityLevels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrustedAdvisorCheckRefreshStatusesResponseModel(BaseModel):
    statuses: List[TrustedAdvisorCheckRefreshStatusModel] = Field(alias="statuses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RefreshTrustedAdvisorCheckResponseModel(BaseModel):
    status: TrustedAdvisorCheckRefreshStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrustedAdvisorChecksResponseModel(BaseModel):
    checks: List[TrustedAdvisorCheckDescriptionModel] = Field(alias="checks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrustedAdvisorCategorySpecificSummaryModel(BaseModel):
    cost_optimizing: Optional[TrustedAdvisorCostOptimizingSummaryModel] = Field(
        default=None, alias="costOptimizing"
    )


class DescribeCommunicationsResponseModel(BaseModel):
    communications: List[CommunicationModel] = Field(alias="communications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecentCaseCommunicationsModel(BaseModel):
    communications: Optional[List[CommunicationModel]] = Field(
        default=None, alias="communications"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeServicesResponseModel(BaseModel):
    services: List[ServiceModel] = Field(alias="services")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrustedAdvisorCheckResultModel(BaseModel):
    check_id: str = Field(alias="checkId")
    timestamp: str = Field(alias="timestamp")
    status: str = Field(alias="status")
    resources_summary: TrustedAdvisorResourcesSummaryModel = Field(
        alias="resourcesSummary"
    )
    category_specific_summary: TrustedAdvisorCategorySpecificSummaryModel = Field(
        alias="categorySpecificSummary"
    )
    flagged_resources: List[TrustedAdvisorResourceDetailModel] = Field(
        alias="flaggedResources"
    )


class TrustedAdvisorCheckSummaryModel(BaseModel):
    check_id: str = Field(alias="checkId")
    timestamp: str = Field(alias="timestamp")
    status: str = Field(alias="status")
    resources_summary: TrustedAdvisorResourcesSummaryModel = Field(
        alias="resourcesSummary"
    )
    category_specific_summary: TrustedAdvisorCategorySpecificSummaryModel = Field(
        alias="categorySpecificSummary"
    )
    has_flagged_resources: Optional[bool] = Field(
        default=None, alias="hasFlaggedResources"
    )


class CaseDetailsModel(BaseModel):
    case_id: Optional[str] = Field(default=None, alias="caseId")
    display_id: Optional[str] = Field(default=None, alias="displayId")
    subject: Optional[str] = Field(default=None, alias="subject")
    status: Optional[str] = Field(default=None, alias="status")
    service_code: Optional[str] = Field(default=None, alias="serviceCode")
    category_code: Optional[str] = Field(default=None, alias="categoryCode")
    severity_code: Optional[str] = Field(default=None, alias="severityCode")
    submitted_by: Optional[str] = Field(default=None, alias="submittedBy")
    time_created: Optional[str] = Field(default=None, alias="timeCreated")
    recent_communications: Optional[RecentCaseCommunicationsModel] = Field(
        default=None, alias="recentCommunications"
    )
    cc_email_addresses: Optional[List[str]] = Field(
        default=None, alias="ccEmailAddresses"
    )
    language: Optional[str] = Field(default=None, alias="language")


class DescribeTrustedAdvisorCheckResultResponseModel(BaseModel):
    result: TrustedAdvisorCheckResultModel = Field(alias="result")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrustedAdvisorCheckSummariesResponseModel(BaseModel):
    summaries: List[TrustedAdvisorCheckSummaryModel] = Field(alias="summaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCasesResponseModel(BaseModel):
    cases: List[CaseDetailsModel] = Field(alias="cases")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
