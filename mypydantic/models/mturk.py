# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptQualificationRequestRequestModel(BaseModel):
    qualification_request_id: str = Field(alias="QualificationRequestId")
    integer_value: Optional[int] = Field(default=None, alias="IntegerValue")


class ApproveAssignmentRequestModel(BaseModel):
    assignment_id: str = Field(alias="AssignmentId")
    requester_feedback: Optional[str] = Field(default=None, alias="RequesterFeedback")
    override_rejection: Optional[bool] = Field(default=None, alias="OverrideRejection")


class AssignmentModel(BaseModel):
    assignment_id: Optional[str] = Field(default=None, alias="AssignmentId")
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")
    hitid: Optional[str] = Field(default=None, alias="HITId")
    assignment_status: Optional[Literal["Approved", "Rejected", "Submitted"]] = Field(
        default=None, alias="AssignmentStatus"
    )
    auto_approval_time: Optional[datetime] = Field(
        default=None, alias="AutoApprovalTime"
    )
    accept_time: Optional[datetime] = Field(default=None, alias="AcceptTime")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    approval_time: Optional[datetime] = Field(default=None, alias="ApprovalTime")
    rejection_time: Optional[datetime] = Field(default=None, alias="RejectionTime")
    deadline: Optional[datetime] = Field(default=None, alias="Deadline")
    answer: Optional[str] = Field(default=None, alias="Answer")
    requester_feedback: Optional[str] = Field(default=None, alias="RequesterFeedback")


class AssociateQualificationWithWorkerRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    worker_id: str = Field(alias="WorkerId")
    integer_value: Optional[int] = Field(default=None, alias="IntegerValue")
    send_notification: Optional[bool] = Field(default=None, alias="SendNotification")


class BonusPaymentModel(BaseModel):
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")
    bonus_amount: Optional[str] = Field(default=None, alias="BonusAmount")
    assignment_id: Optional[str] = Field(default=None, alias="AssignmentId")
    reason: Optional[str] = Field(default=None, alias="Reason")
    grant_time: Optional[datetime] = Field(default=None, alias="GrantTime")


class CreateAdditionalAssignmentsForHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    number_of_additional_assignments: int = Field(alias="NumberOfAdditionalAssignments")
    unique_request_token: Optional[str] = Field(
        default=None, alias="UniqueRequestToken"
    )


class HITLayoutParameterModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateQualificationTypeRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    qualification_type_status: Literal["Active", "Inactive"] = Field(
        alias="QualificationTypeStatus"
    )
    keywords: Optional[str] = Field(default=None, alias="Keywords")
    retry_delay_in_seconds: Optional[int] = Field(
        default=None, alias="RetryDelayInSeconds"
    )
    test: Optional[str] = Field(default=None, alias="Test")
    answer_key: Optional[str] = Field(default=None, alias="AnswerKey")
    test_duration_in_seconds: Optional[int] = Field(
        default=None, alias="TestDurationInSeconds"
    )
    auto_granted: Optional[bool] = Field(default=None, alias="AutoGranted")
    auto_granted_value: Optional[int] = Field(default=None, alias="AutoGrantedValue")


class QualificationTypeModel(BaseModel):
    qualification_type_id: Optional[str] = Field(
        default=None, alias="QualificationTypeId"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    keywords: Optional[str] = Field(default=None, alias="Keywords")
    qualification_type_status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="QualificationTypeStatus"
    )
    test: Optional[str] = Field(default=None, alias="Test")
    test_duration_in_seconds: Optional[int] = Field(
        default=None, alias="TestDurationInSeconds"
    )
    answer_key: Optional[str] = Field(default=None, alias="AnswerKey")
    retry_delay_in_seconds: Optional[int] = Field(
        default=None, alias="RetryDelayInSeconds"
    )
    is_requestable: Optional[bool] = Field(default=None, alias="IsRequestable")
    auto_granted: Optional[bool] = Field(default=None, alias="AutoGranted")
    auto_granted_value: Optional[int] = Field(default=None, alias="AutoGrantedValue")


class CreateWorkerBlockRequestModel(BaseModel):
    worker_id: str = Field(alias="WorkerId")
    reason: str = Field(alias="Reason")


class DeleteHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")


class DeleteQualificationTypeRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")


class DeleteWorkerBlockRequestModel(BaseModel):
    worker_id: str = Field(alias="WorkerId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class DisassociateQualificationFromWorkerRequestModel(BaseModel):
    worker_id: str = Field(alias="WorkerId")
    qualification_type_id: str = Field(alias="QualificationTypeId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class GetAssignmentRequestModel(BaseModel):
    assignment_id: str = Field(alias="AssignmentId")


class GetFileUploadURLRequestModel(BaseModel):
    assignment_id: str = Field(alias="AssignmentId")
    question_identifier: str = Field(alias="QuestionIdentifier")


class GetHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")


class GetQualificationScoreRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    worker_id: str = Field(alias="WorkerId")


class GetQualificationTypeRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAssignmentsForHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    assignment_statuses: Optional[
        Sequence[Literal["Approved", "Rejected", "Submitted"]]
    ] = Field(default=None, alias="AssignmentStatuses")


class ListBonusPaymentsRequestModel(BaseModel):
    hitid: Optional[str] = Field(default=None, alias="HITId")
    assignment_id: Optional[str] = Field(default=None, alias="AssignmentId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListHITsForQualificationTypeRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListHITsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListQualificationRequestsRequestModel(BaseModel):
    qualification_type_id: Optional[str] = Field(
        default=None, alias="QualificationTypeId"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class QualificationRequestModel(BaseModel):
    qualification_request_id: Optional[str] = Field(
        default=None, alias="QualificationRequestId"
    )
    qualification_type_id: Optional[str] = Field(
        default=None, alias="QualificationTypeId"
    )
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")
    test: Optional[str] = Field(default=None, alias="Test")
    answer: Optional[str] = Field(default=None, alias="Answer")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")


class ListQualificationTypesRequestModel(BaseModel):
    must_be_requestable: bool = Field(alias="MustBeRequestable")
    query: Optional[str] = Field(default=None, alias="Query")
    must_be_owned_by_caller: Optional[bool] = Field(
        default=None, alias="MustBeOwnedByCaller"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReviewPolicyResultsForHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    policy_levels: Optional[Sequence[Literal["Assignment", "HIT"]]] = Field(
        default=None, alias="PolicyLevels"
    )
    retrieve_actions: Optional[bool] = Field(default=None, alias="RetrieveActions")
    retrieve_results: Optional[bool] = Field(default=None, alias="RetrieveResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReviewableHITsRequestModel(BaseModel):
    hittype_id: Optional[str] = Field(default=None, alias="HITTypeId")
    status: Optional[Literal["Reviewable", "Reviewing"]] = Field(
        default=None, alias="Status"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListWorkerBlocksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class WorkerBlockModel(BaseModel):
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class ListWorkersWithQualificationTypeRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    status: Optional[Literal["Granted", "Revoked"]] = Field(
        default=None, alias="Status"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class LocaleModel(BaseModel):
    country: str = Field(alias="Country")
    subdivision: Optional[str] = Field(default=None, alias="Subdivision")


class NotificationSpecificationModel(BaseModel):
    destination: str = Field(alias="Destination")
    transport: Literal["Email", "SNS", "SQS"] = Field(alias="Transport")
    version: str = Field(alias="Version")
    event_types: Sequence[
        Literal[
            "AssignmentAbandoned",
            "AssignmentAccepted",
            "AssignmentApproved",
            "AssignmentRejected",
            "AssignmentReturned",
            "AssignmentSubmitted",
            "HITCreated",
            "HITDisposed",
            "HITExpired",
            "HITExtended",
            "HITReviewable",
            "Ping",
        ]
    ] = Field(alias="EventTypes")


class NotifyWorkersFailureStatusModel(BaseModel):
    notify_workers_failure_code: Optional[
        Literal["HardFailure", "SoftFailure"]
    ] = Field(default=None, alias="NotifyWorkersFailureCode")
    notify_workers_failure_message: Optional[str] = Field(
        default=None, alias="NotifyWorkersFailureMessage"
    )
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")


class NotifyWorkersRequestModel(BaseModel):
    subject: str = Field(alias="Subject")
    message_text: str = Field(alias="MessageText")
    worker_ids: Sequence[str] = Field(alias="WorkerIds")


class ParameterMapEntryModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class RejectAssignmentRequestModel(BaseModel):
    assignment_id: str = Field(alias="AssignmentId")
    requester_feedback: str = Field(alias="RequesterFeedback")


class RejectQualificationRequestRequestModel(BaseModel):
    qualification_request_id: str = Field(alias="QualificationRequestId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class ReviewActionDetailModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="ActionId")
    action_name: Optional[str] = Field(default=None, alias="ActionName")
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    target_type: Optional[str] = Field(default=None, alias="TargetType")
    status: Optional[Literal["Cancelled", "Failed", "Intended", "Succeeded"]] = Field(
        default=None, alias="Status"
    )
    complete_time: Optional[datetime] = Field(default=None, alias="CompleteTime")
    result: Optional[str] = Field(default=None, alias="Result")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")


class ReviewResultDetailModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="ActionId")
    subject_id: Optional[str] = Field(default=None, alias="SubjectId")
    subject_type: Optional[str] = Field(default=None, alias="SubjectType")
    question_id: Optional[str] = Field(default=None, alias="QuestionId")
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class SendBonusRequestModel(BaseModel):
    worker_id: str = Field(alias="WorkerId")
    bonus_amount: str = Field(alias="BonusAmount")
    assignment_id: str = Field(alias="AssignmentId")
    reason: str = Field(alias="Reason")
    unique_request_token: Optional[str] = Field(
        default=None, alias="UniqueRequestToken"
    )


class UpdateExpirationForHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    expire_at: Union[datetime, str] = Field(alias="ExpireAt")


class UpdateHITReviewStatusRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    revert: Optional[bool] = Field(default=None, alias="Revert")


class UpdateHITTypeOfHITRequestModel(BaseModel):
    hitid: str = Field(alias="HITId")
    hittype_id: str = Field(alias="HITTypeId")


class UpdateQualificationTypeRequestModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    description: Optional[str] = Field(default=None, alias="Description")
    qualification_type_status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="QualificationTypeStatus"
    )
    test: Optional[str] = Field(default=None, alias="Test")
    answer_key: Optional[str] = Field(default=None, alias="AnswerKey")
    test_duration_in_seconds: Optional[int] = Field(
        default=None, alias="TestDurationInSeconds"
    )
    retry_delay_in_seconds: Optional[int] = Field(
        default=None, alias="RetryDelayInSeconds"
    )
    auto_granted: Optional[bool] = Field(default=None, alias="AutoGranted")
    auto_granted_value: Optional[int] = Field(default=None, alias="AutoGrantedValue")


class CreateHITTypeResponseModel(BaseModel):
    hittype_id: str = Field(alias="HITTypeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountBalanceResponseModel(BaseModel):
    available_balance: str = Field(alias="AvailableBalance")
    on_hold_balance: str = Field(alias="OnHoldBalance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFileUploadURLResponseModel(BaseModel):
    file_upload_url: str = Field(alias="FileUploadURL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssignmentsForHITResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    assignments: List[AssignmentModel] = Field(alias="Assignments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBonusPaymentsResponseModel(BaseModel):
    num_results: int = Field(alias="NumResults")
    next_token: str = Field(alias="NextToken")
    bonus_payments: List[BonusPaymentModel] = Field(alias="BonusPayments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQualificationTypeResponseModel(BaseModel):
    qualification_type: QualificationTypeModel = Field(alias="QualificationType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQualificationTypeResponseModel(BaseModel):
    qualification_type: QualificationTypeModel = Field(alias="QualificationType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQualificationTypesResponseModel(BaseModel):
    num_results: int = Field(alias="NumResults")
    next_token: str = Field(alias="NextToken")
    qualification_types: List[QualificationTypeModel] = Field(
        alias="QualificationTypes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateQualificationTypeResponseModel(BaseModel):
    qualification_type: QualificationTypeModel = Field(alias="QualificationType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssignmentsForHITRequestListAssignmentsForHITPaginateModel(BaseModel):
    hitid: str = Field(alias="HITId")
    assignment_statuses: Optional[
        Sequence[Literal["Approved", "Rejected", "Submitted"]]
    ] = Field(default=None, alias="AssignmentStatuses")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBonusPaymentsRequestListBonusPaymentsPaginateModel(BaseModel):
    hitid: Optional[str] = Field(default=None, alias="HITId")
    assignment_id: Optional[str] = Field(default=None, alias="AssignmentId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateModel(
    BaseModel
):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHITsRequestListHITsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQualificationRequestsRequestListQualificationRequestsPaginateModel(BaseModel):
    qualification_type_id: Optional[str] = Field(
        default=None, alias="QualificationTypeId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQualificationTypesRequestListQualificationTypesPaginateModel(BaseModel):
    must_be_requestable: bool = Field(alias="MustBeRequestable")
    query: Optional[str] = Field(default=None, alias="Query")
    must_be_owned_by_caller: Optional[bool] = Field(
        default=None, alias="MustBeOwnedByCaller"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReviewableHITsRequestListReviewableHITsPaginateModel(BaseModel):
    hittype_id: Optional[str] = Field(default=None, alias="HITTypeId")
    status: Optional[Literal["Reviewable", "Reviewing"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkerBlocksRequestListWorkerBlocksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateModel(
    BaseModel
):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    status: Optional[Literal["Granted", "Revoked"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQualificationRequestsResponseModel(BaseModel):
    num_results: int = Field(alias="NumResults")
    next_token: str = Field(alias="NextToken")
    qualification_requests: List[QualificationRequestModel] = Field(
        alias="QualificationRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkerBlocksResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    worker_blocks: List[WorkerBlockModel] = Field(alias="WorkerBlocks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QualificationRequirementModel(BaseModel):
    qualification_type_id: str = Field(alias="QualificationTypeId")
    comparator: Literal[
        "DoesNotExist",
        "EqualTo",
        "Exists",
        "GreaterThan",
        "GreaterThanOrEqualTo",
        "In",
        "LessThan",
        "LessThanOrEqualTo",
        "NotEqualTo",
        "NotIn",
    ] = Field(alias="Comparator")
    integer_values: Optional[Sequence[int]] = Field(default=None, alias="IntegerValues")
    locale_values: Optional[Sequence[LocaleModel]] = Field(
        default=None, alias="LocaleValues"
    )
    required_to_preview: Optional[bool] = Field(default=None, alias="RequiredToPreview")
    actions_guarded: Optional[
        Literal["Accept", "DiscoverPreviewAndAccept", "PreviewAndAccept"]
    ] = Field(default=None, alias="ActionsGuarded")


class QualificationModel(BaseModel):
    qualification_type_id: Optional[str] = Field(
        default=None, alias="QualificationTypeId"
    )
    worker_id: Optional[str] = Field(default=None, alias="WorkerId")
    grant_time: Optional[datetime] = Field(default=None, alias="GrantTime")
    integer_value: Optional[int] = Field(default=None, alias="IntegerValue")
    locale_value: Optional[LocaleModel] = Field(default=None, alias="LocaleValue")
    status: Optional[Literal["Granted", "Revoked"]] = Field(
        default=None, alias="Status"
    )


class SendTestEventNotificationRequestModel(BaseModel):
    notification: NotificationSpecificationModel = Field(alias="Notification")
    test_event_type: Literal[
        "AssignmentAbandoned",
        "AssignmentAccepted",
        "AssignmentApproved",
        "AssignmentRejected",
        "AssignmentReturned",
        "AssignmentSubmitted",
        "HITCreated",
        "HITDisposed",
        "HITExpired",
        "HITExtended",
        "HITReviewable",
        "Ping",
    ] = Field(alias="TestEventType")


class UpdateNotificationSettingsRequestModel(BaseModel):
    hittype_id: str = Field(alias="HITTypeId")
    notification: Optional[NotificationSpecificationModel] = Field(
        default=None, alias="Notification"
    )
    active: Optional[bool] = Field(default=None, alias="Active")


class NotifyWorkersResponseModel(BaseModel):
    notify_workers_failure_statuses: List[NotifyWorkersFailureStatusModel] = Field(
        alias="NotifyWorkersFailureStatuses"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    map_entries: Optional[Sequence[ParameterMapEntryModel]] = Field(
        default=None, alias="MapEntries"
    )


class ReviewReportModel(BaseModel):
    review_results: Optional[List[ReviewResultDetailModel]] = Field(
        default=None, alias="ReviewResults"
    )
    review_actions: Optional[List[ReviewActionDetailModel]] = Field(
        default=None, alias="ReviewActions"
    )


class CreateHITTypeRequestModel(BaseModel):
    assignment_duration_in_seconds: int = Field(alias="AssignmentDurationInSeconds")
    reward: str = Field(alias="Reward")
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    auto_approval_delay_in_seconds: Optional[int] = Field(
        default=None, alias="AutoApprovalDelayInSeconds"
    )
    keywords: Optional[str] = Field(default=None, alias="Keywords")
    qualification_requirements: Optional[
        Sequence[QualificationRequirementModel]
    ] = Field(default=None, alias="QualificationRequirements")


class HITModel(BaseModel):
    hitid: Optional[str] = Field(default=None, alias="HITId")
    hittype_id: Optional[str] = Field(default=None, alias="HITTypeId")
    hitgroup_id: Optional[str] = Field(default=None, alias="HITGroupId")
    hitlayout_id: Optional[str] = Field(default=None, alias="HITLayoutId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    title: Optional[str] = Field(default=None, alias="Title")
    description: Optional[str] = Field(default=None, alias="Description")
    question: Optional[str] = Field(default=None, alias="Question")
    keywords: Optional[str] = Field(default=None, alias="Keywords")
    hitstatus: Optional[
        Literal["Assignable", "Disposed", "Reviewable", "Reviewing", "Unassignable"]
    ] = Field(default=None, alias="HITStatus")
    max_assignments: Optional[int] = Field(default=None, alias="MaxAssignments")
    reward: Optional[str] = Field(default=None, alias="Reward")
    auto_approval_delay_in_seconds: Optional[int] = Field(
        default=None, alias="AutoApprovalDelayInSeconds"
    )
    expiration: Optional[datetime] = Field(default=None, alias="Expiration")
    assignment_duration_in_seconds: Optional[int] = Field(
        default=None, alias="AssignmentDurationInSeconds"
    )
    requester_annotation: Optional[str] = Field(
        default=None, alias="RequesterAnnotation"
    )
    qualification_requirements: Optional[List[QualificationRequirementModel]] = Field(
        default=None, alias="QualificationRequirements"
    )
    hitreview_status: Optional[
        Literal[
            "MarkedForReview",
            "NotReviewed",
            "ReviewedAppropriate",
            "ReviewedInappropriate",
        ]
    ] = Field(default=None, alias="HITReviewStatus")
    number_of_assignments_pending: Optional[int] = Field(
        default=None, alias="NumberOfAssignmentsPending"
    )
    number_of_assignments_available: Optional[int] = Field(
        default=None, alias="NumberOfAssignmentsAvailable"
    )
    number_of_assignments_completed: Optional[int] = Field(
        default=None, alias="NumberOfAssignmentsCompleted"
    )


class GetQualificationScoreResponseModel(BaseModel):
    qualification: QualificationModel = Field(alias="Qualification")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkersWithQualificationTypeResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    qualifications: List[QualificationModel] = Field(alias="Qualifications")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReviewPolicyModel(BaseModel):
    policy_name: str = Field(alias="PolicyName")
    parameters: Optional[Sequence[PolicyParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class CreateHITResponseModel(BaseModel):
    hit: HITModel = Field(alias="HIT")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHITWithHITTypeResponseModel(BaseModel):
    hit: HITModel = Field(alias="HIT")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssignmentResponseModel(BaseModel):
    assignment: AssignmentModel = Field(alias="Assignment")
    hit: HITModel = Field(alias="HIT")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHITResponseModel(BaseModel):
    hit: HITModel = Field(alias="HIT")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHITsForQualificationTypeResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    hits: List[HITModel] = Field(alias="HITs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHITsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    hits: List[HITModel] = Field(alias="HITs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReviewableHITsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    num_results: int = Field(alias="NumResults")
    hits: List[HITModel] = Field(alias="HITs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHITRequestModel(BaseModel):
    lifetime_in_seconds: int = Field(alias="LifetimeInSeconds")
    assignment_duration_in_seconds: int = Field(alias="AssignmentDurationInSeconds")
    reward: str = Field(alias="Reward")
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    max_assignments: Optional[int] = Field(default=None, alias="MaxAssignments")
    auto_approval_delay_in_seconds: Optional[int] = Field(
        default=None, alias="AutoApprovalDelayInSeconds"
    )
    keywords: Optional[str] = Field(default=None, alias="Keywords")
    question: Optional[str] = Field(default=None, alias="Question")
    requester_annotation: Optional[str] = Field(
        default=None, alias="RequesterAnnotation"
    )
    qualification_requirements: Optional[
        Sequence[QualificationRequirementModel]
    ] = Field(default=None, alias="QualificationRequirements")
    unique_request_token: Optional[str] = Field(
        default=None, alias="UniqueRequestToken"
    )
    assignment_review_policy: Optional[ReviewPolicyModel] = Field(
        default=None, alias="AssignmentReviewPolicy"
    )
    hitreview_policy: Optional[ReviewPolicyModel] = Field(
        default=None, alias="HITReviewPolicy"
    )
    hitlayout_id: Optional[str] = Field(default=None, alias="HITLayoutId")
    hitlayout_parameters: Optional[Sequence[HITLayoutParameterModel]] = Field(
        default=None, alias="HITLayoutParameters"
    )


class CreateHITWithHITTypeRequestModel(BaseModel):
    hittype_id: str = Field(alias="HITTypeId")
    lifetime_in_seconds: int = Field(alias="LifetimeInSeconds")
    max_assignments: Optional[int] = Field(default=None, alias="MaxAssignments")
    question: Optional[str] = Field(default=None, alias="Question")
    requester_annotation: Optional[str] = Field(
        default=None, alias="RequesterAnnotation"
    )
    unique_request_token: Optional[str] = Field(
        default=None, alias="UniqueRequestToken"
    )
    assignment_review_policy: Optional[ReviewPolicyModel] = Field(
        default=None, alias="AssignmentReviewPolicy"
    )
    hitreview_policy: Optional[ReviewPolicyModel] = Field(
        default=None, alias="HITReviewPolicy"
    )
    hitlayout_id: Optional[str] = Field(default=None, alias="HITLayoutId")
    hitlayout_parameters: Optional[Sequence[HITLayoutParameterModel]] = Field(
        default=None, alias="HITLayoutParameters"
    )


class ListReviewPolicyResultsForHITResponseModel(BaseModel):
    hitid: str = Field(alias="HITId")
    assignment_review_policy: ReviewPolicyModel = Field(alias="AssignmentReviewPolicy")
    hitreview_policy: ReviewPolicyModel = Field(alias="HITReviewPolicy")
    assignment_review_report: ReviewReportModel = Field(alias="AssignmentReviewReport")
    hitreview_report: ReviewReportModel = Field(alias="HITReviewReport")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
