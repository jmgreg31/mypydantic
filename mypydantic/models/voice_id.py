# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AuthenticationConfigurationModel(BaseModel):
    acceptance_threshold: int = Field(alias="AcceptanceThreshold")


class ServerSideEncryptionConfigurationModel(BaseModel):
    kms_key_id: str = Field(alias="KmsKeyId")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")


class DeleteFraudsterRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    fraudster_id: str = Field(alias="FraudsterId")


class DeleteSpeakerRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    speaker_id: str = Field(alias="SpeakerId")


class DescribeDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")


class DescribeFraudsterRegistrationJobRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    job_id: str = Field(alias="JobId")


class DescribeFraudsterRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    fraudster_id: str = Field(alias="FraudsterId")


class FraudsterModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    generated_fraudster_id: Optional[str] = Field(
        default=None, alias="GeneratedFraudsterId"
    )


class DescribeSpeakerEnrollmentJobRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    job_id: str = Field(alias="JobId")


class DescribeSpeakerRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    speaker_id: str = Field(alias="SpeakerId")


class SpeakerModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    customer_speaker_id: Optional[str] = Field(default=None, alias="CustomerSpeakerId")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    generated_speaker_id: Optional[str] = Field(
        default=None, alias="GeneratedSpeakerId"
    )
    last_accessed_at: Optional[datetime] = Field(default=None, alias="LastAccessedAt")
    status: Optional[Literal["ENROLLED", "EXPIRED", "OPTED_OUT", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class ServerSideEncryptionUpdateDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    old_kms_key_id: Optional[str] = Field(default=None, alias="OldKmsKeyId")
    update_status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="UpdateStatus"
    )


class EnrollmentJobFraudDetectionConfigModel(BaseModel):
    fraud_detection_action: Optional[Literal["FAIL", "IGNORE"]] = Field(
        default=None, alias="FraudDetectionAction"
    )
    risk_threshold: Optional[int] = Field(default=None, alias="RiskThreshold")


class EvaluateSessionRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    session_name_or_id: str = Field(alias="SessionNameOrId")


class FailureDetailsModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    status_code: Optional[int] = Field(default=None, alias="StatusCode")


class FraudDetectionConfigurationModel(BaseModel):
    risk_threshold: int = Field(alias="RiskThreshold")


class KnownFraudsterRiskModel(BaseModel):
    risk_score: int = Field(alias="RiskScore")
    generated_fraudster_id: Optional[str] = Field(
        default=None, alias="GeneratedFraudsterId"
    )


class VoiceSpoofingRiskModel(BaseModel):
    risk_score: int = Field(alias="RiskScore")


class JobProgressModel(BaseModel):
    percent_complete: Optional[int] = Field(default=None, alias="PercentComplete")


class InputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")


class OutputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class RegistrationConfigModel(BaseModel):
    duplicate_registration_action: Optional[Literal["REGISTER_AS_NEW", "SKIP"]] = Field(
        default=None, alias="DuplicateRegistrationAction"
    )
    fraudster_similarity_threshold: Optional[int] = Field(
        default=None, alias="FraudsterSimilarityThreshold"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDomainsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFraudsterRegistrationJobsRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSpeakerEnrollmentJobsRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSpeakersRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SpeakerSummaryModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    customer_speaker_id: Optional[str] = Field(default=None, alias="CustomerSpeakerId")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    generated_speaker_id: Optional[str] = Field(
        default=None, alias="GeneratedSpeakerId"
    )
    last_accessed_at: Optional[datetime] = Field(default=None, alias="LastAccessedAt")
    status: Optional[Literal["ENROLLED", "EXPIRED", "OPTED_OUT", "PENDING"]] = Field(
        default=None, alias="Status"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class OptOutSpeakerRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    speaker_id: str = Field(alias="SpeakerId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AuthenticationResultModel(BaseModel):
    audio_aggregation_ended_at: Optional[datetime] = Field(
        default=None, alias="AudioAggregationEndedAt"
    )
    audio_aggregation_started_at: Optional[datetime] = Field(
        default=None, alias="AudioAggregationStartedAt"
    )
    authentication_result_id: Optional[str] = Field(
        default=None, alias="AuthenticationResultId"
    )
    configuration: Optional[AuthenticationConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    customer_speaker_id: Optional[str] = Field(default=None, alias="CustomerSpeakerId")
    decision: Optional[
        Literal[
            "ACCEPT",
            "NOT_ENOUGH_SPEECH",
            "REJECT",
            "SPEAKER_EXPIRED",
            "SPEAKER_ID_NOT_PROVIDED",
            "SPEAKER_NOT_ENROLLED",
            "SPEAKER_OPTED_OUT",
        ]
    ] = Field(default=None, alias="Decision")
    generated_speaker_id: Optional[str] = Field(
        default=None, alias="GeneratedSpeakerId"
    )
    score: Optional[int] = Field(default=None, alias="Score")


class UpdateDomainRequestModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    name: str = Field(alias="Name")
    server_side_encryption_configuration: ServerSideEncryptionConfigurationModel = (
        Field(alias="ServerSideEncryptionConfiguration")
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateDomainRequestModel(BaseModel):
    name: str = Field(alias="Name")
    server_side_encryption_configuration: ServerSideEncryptionConfigurationModel = (
        Field(alias="ServerSideEncryptionConfiguration")
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFraudsterResponseModel(BaseModel):
    fraudster: FraudsterModel = Field(alias="Fraudster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSpeakerResponseModel(BaseModel):
    speaker: SpeakerModel = Field(alias="Speaker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OptOutSpeakerResponseModel(BaseModel):
    speaker: SpeakerModel = Field(alias="Speaker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    domain_status: Optional[Literal["ACTIVE", "PENDING", "SUSPENDED"]] = Field(
        default=None, alias="DomainStatus"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="ServerSideEncryptionConfiguration")
    server_side_encryption_update_details: Optional[
        ServerSideEncryptionUpdateDetailsModel
    ] = Field(default=None, alias="ServerSideEncryptionUpdateDetails")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class DomainModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    domain_status: Optional[Literal["ACTIVE", "PENDING", "SUSPENDED"]] = Field(
        default=None, alias="DomainStatus"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="ServerSideEncryptionConfiguration")
    server_side_encryption_update_details: Optional[
        ServerSideEncryptionUpdateDetailsModel
    ] = Field(default=None, alias="ServerSideEncryptionUpdateDetails")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class EnrollmentConfigModel(BaseModel):
    existing_enrollment_action: Optional[Literal["OVERWRITE", "SKIP"]] = Field(
        default=None, alias="ExistingEnrollmentAction"
    )
    fraud_detection_config: Optional[EnrollmentJobFraudDetectionConfigModel] = Field(
        default=None, alias="FraudDetectionConfig"
    )


class FraudRiskDetailsModel(BaseModel):
    known_fraudster_risk: KnownFraudsterRiskModel = Field(alias="KnownFraudsterRisk")
    voice_spoofing_risk: VoiceSpoofingRiskModel = Field(alias="VoiceSpoofingRisk")


class FraudsterRegistrationJobSummaryModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_progress: Optional[JobProgressModel] = Field(default=None, alias="JobProgress")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")


class SpeakerEnrollmentJobSummaryModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_progress: Optional[JobProgressModel] = Field(default=None, alias="JobProgress")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")


class FraudsterRegistrationJobModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_progress: Optional[JobProgressModel] = Field(default=None, alias="JobProgress")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    registration_config: Optional[RegistrationConfigModel] = Field(
        default=None, alias="RegistrationConfig"
    )


class StartFraudsterRegistrationJobRequestModel(BaseModel):
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    domain_id: str = Field(alias="DomainId")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    registration_config: Optional[RegistrationConfigModel] = Field(
        default=None, alias="RegistrationConfig"
    )


class ListDomainsRequestListDomainsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateModel(
    BaseModel
):
    domain_id: str = Field(alias="DomainId")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpeakersRequestListSpeakersPaginateModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpeakersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    speaker_summaries: List[SpeakerSummaryModel] = Field(alias="SpeakerSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsResponseModel(BaseModel):
    domain_summaries: List[DomainSummaryModel] = Field(alias="DomainSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainResponseModel(BaseModel):
    domain: DomainModel = Field(alias="Domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainResponseModel(BaseModel):
    domain: DomainModel = Field(alias="Domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainResponseModel(BaseModel):
    domain: DomainModel = Field(alias="Domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SpeakerEnrollmentJobModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    enrollment_config: Optional[EnrollmentConfigModel] = Field(
        default=None, alias="EnrollmentConfig"
    )
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_progress: Optional[JobProgressModel] = Field(default=None, alias="JobProgress")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )


class StartSpeakerEnrollmentJobRequestModel(BaseModel):
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    domain_id: str = Field(alias="DomainId")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    enrollment_config: Optional[EnrollmentConfigModel] = Field(
        default=None, alias="EnrollmentConfig"
    )
    job_name: Optional[str] = Field(default=None, alias="JobName")


class FraudDetectionResultModel(BaseModel):
    audio_aggregation_ended_at: Optional[datetime] = Field(
        default=None, alias="AudioAggregationEndedAt"
    )
    audio_aggregation_started_at: Optional[datetime] = Field(
        default=None, alias="AudioAggregationStartedAt"
    )
    configuration: Optional[FraudDetectionConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    decision: Optional[Literal["HIGH_RISK", "LOW_RISK", "NOT_ENOUGH_SPEECH"]] = Field(
        default=None, alias="Decision"
    )
    fraud_detection_result_id: Optional[str] = Field(
        default=None, alias="FraudDetectionResultId"
    )
    reasons: Optional[List[Literal["KNOWN_FRAUDSTER", "VOICE_SPOOFING"]]] = Field(
        default=None, alias="Reasons"
    )
    risk_details: Optional[FraudRiskDetailsModel] = Field(
        default=None, alias="RiskDetails"
    )


class ListFraudsterRegistrationJobsResponseModel(BaseModel):
    job_summaries: List[FraudsterRegistrationJobSummaryModel] = Field(
        alias="JobSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSpeakerEnrollmentJobsResponseModel(BaseModel):
    job_summaries: List[SpeakerEnrollmentJobSummaryModel] = Field(alias="JobSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFraudsterRegistrationJobResponseModel(BaseModel):
    job: FraudsterRegistrationJobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFraudsterRegistrationJobResponseModel(BaseModel):
    job: FraudsterRegistrationJobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSpeakerEnrollmentJobResponseModel(BaseModel):
    job: SpeakerEnrollmentJobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSpeakerEnrollmentJobResponseModel(BaseModel):
    job: SpeakerEnrollmentJobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluateSessionResponseModel(BaseModel):
    authentication_result: AuthenticationResultModel = Field(
        alias="AuthenticationResult"
    )
    domain_id: str = Field(alias="DomainId")
    fraud_detection_result: FraudDetectionResultModel = Field(
        alias="FraudDetectionResult"
    )
    session_id: str = Field(alias="SessionId")
    session_name: str = Field(alias="SessionName")
    streaming_status: Literal["ENDED", "ONGOING", "PENDING_CONFIGURATION"] = Field(
        alias="StreamingStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
