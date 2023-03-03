# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AnswerMachineDetectionConfigModel(BaseModel):
    enable_answer_machine_detection: bool = Field(alias="enableAnswerMachineDetection")


class InstanceIdFilterModel(BaseModel):
    operator: Literal["Eq"] = Field(alias="operator")
    value: str = Field(alias="value")


class CampaignSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    connect_instance_id: str = Field(alias="connectInstanceId")
    id: str = Field(alias="id")
    name: str = Field(alias="name")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteConnectInstanceConfigRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")


class DeleteInstanceOnboardingJobRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")


class DescribeCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class DialRequestModel(BaseModel):
    attributes: Mapping[str, str] = Field(alias="attributes")
    client_token: str = Field(alias="clientToken")
    expiration_time: Union[datetime, str] = Field(alias="expirationTime")
    phone_number: str = Field(alias="phoneNumber")


class PredictiveDialerConfigModel(BaseModel):
    bandwidth_allocation: float = Field(alias="bandwidthAllocation")


class ProgressiveDialerConfigModel(BaseModel):
    bandwidth_allocation: float = Field(alias="bandwidthAllocation")


class EncryptionConfigModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    encryption_type: Optional[Literal["KMS"]] = Field(
        default=None, alias="encryptionType"
    )
    key_arn: Optional[str] = Field(default=None, alias="keyArn")


class FailedCampaignStateResponseModel(BaseModel):
    campaign_id: Optional[str] = Field(default=None, alias="campaignId")
    failure_code: Optional[Literal["ResourceNotFound", "UnknownError"]] = Field(
        default=None, alias="failureCode"
    )


class FailedRequestModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    failure_code: Optional[
        Literal["InvalidInput", "RequestThrottled", "UnknownError"]
    ] = Field(default=None, alias="failureCode")
    id: Optional[str] = Field(default=None, alias="id")


class GetCampaignStateBatchRequestModel(BaseModel):
    campaign_ids: Sequence[str] = Field(alias="campaignIds")


class SuccessfulCampaignStateResponseModel(BaseModel):
    campaign_id: Optional[str] = Field(default=None, alias="campaignId")
    state: Optional[
        Literal["Failed", "Initialized", "Paused", "Running", "Stopped"]
    ] = Field(default=None, alias="state")


class GetCampaignStateRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetConnectInstanceConfigRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")


class GetInstanceOnboardingJobStatusRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")


class InstanceOnboardingJobStatusModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="status")
    failure_code: Optional[
        Literal[
            "EVENT_BRIDGE_ACCESS_DENIED",
            "EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED",
            "IAM_ACCESS_DENIED",
            "INTERNAL_FAILURE",
            "KMS_ACCESS_DENIED",
            "KMS_KEY_NOT_FOUND",
        ]
    ] = Field(default=None, alias="failureCode")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListTagsForResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class PauseCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class SuccessfulRequestModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    id: Optional[str] = Field(default=None, alias="id")


class ResumeCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class StartCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class StopCampaignRequestModel(BaseModel):
    id: str = Field(alias="id")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateCampaignNameRequestModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")


class OutboundCallConfigModel(BaseModel):
    connect_contact_flow_id: str = Field(alias="connectContactFlowId")
    connect_queue_id: str = Field(alias="connectQueueId")
    answer_machine_detection_config: Optional[
        AnswerMachineDetectionConfigModel
    ] = Field(default=None, alias="answerMachineDetectionConfig")
    connect_source_phone_number: Optional[str] = Field(
        default=None, alias="connectSourcePhoneNumber"
    )


class UpdateCampaignOutboundCallConfigRequestModel(BaseModel):
    id: str = Field(alias="id")
    answer_machine_detection_config: Optional[
        AnswerMachineDetectionConfigModel
    ] = Field(default=None, alias="answerMachineDetectionConfig")
    connect_contact_flow_id: Optional[str] = Field(
        default=None, alias="connectContactFlowId"
    )
    connect_source_phone_number: Optional[str] = Field(
        default=None, alias="connectSourcePhoneNumber"
    )


class CampaignFiltersModel(BaseModel):
    instance_id_filter: Optional[InstanceIdFilterModel] = Field(
        default=None, alias="instanceIdFilter"
    )


class CreateCampaignResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCampaignStateResponseModel(BaseModel):
    state: Literal["Failed", "Initialized", "Paused", "Running", "Stopped"] = Field(
        alias="state"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCampaignsResponseModel(BaseModel):
    campaign_summary_list: List[CampaignSummaryModel] = Field(
        alias="campaignSummaryList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDialRequestBatchRequestModel(BaseModel):
    dial_requests: Sequence[DialRequestModel] = Field(alias="dialRequests")
    id: str = Field(alias="id")


class DialerConfigModel(BaseModel):
    predictive_dialer_config: Optional[PredictiveDialerConfigModel] = Field(
        default=None, alias="predictiveDialerConfig"
    )
    progressive_dialer_config: Optional[ProgressiveDialerConfigModel] = Field(
        default=None, alias="progressiveDialerConfig"
    )


class InstanceConfigModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")
    encryption_config: EncryptionConfigModel = Field(alias="encryptionConfig")
    service_linked_role_arn: str = Field(alias="serviceLinkedRoleArn")


class StartInstanceOnboardingJobRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")
    encryption_config: EncryptionConfigModel = Field(alias="encryptionConfig")


class GetCampaignStateBatchResponseModel(BaseModel):
    failed_requests: List[FailedCampaignStateResponseModel] = Field(
        alias="failedRequests"
    )
    successful_requests: List[SuccessfulCampaignStateResponseModel] = Field(
        alias="successfulRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceOnboardingJobStatusResponseModel(BaseModel):
    connect_instance_onboarding_job_status: InstanceOnboardingJobStatusModel = Field(
        alias="connectInstanceOnboardingJobStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartInstanceOnboardingJobResponseModel(BaseModel):
    connect_instance_onboarding_job_status: InstanceOnboardingJobStatusModel = Field(
        alias="connectInstanceOnboardingJobStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDialRequestBatchResponseModel(BaseModel):
    failed_requests: List[FailedRequestModel] = Field(alias="failedRequests")
    successful_requests: List[SuccessfulRequestModel] = Field(
        alias="successfulRequests"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCampaignsRequestListCampaignsPaginateModel(BaseModel):
    filters: Optional[CampaignFiltersModel] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCampaignsRequestModel(BaseModel):
    filters: Optional[CampaignFiltersModel] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class CampaignModel(BaseModel):
    arn: str = Field(alias="arn")
    connect_instance_id: str = Field(alias="connectInstanceId")
    dialer_config: DialerConfigModel = Field(alias="dialerConfig")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    outbound_call_config: OutboundCallConfigModel = Field(alias="outboundCallConfig")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateCampaignRequestModel(BaseModel):
    connect_instance_id: str = Field(alias="connectInstanceId")
    dialer_config: DialerConfigModel = Field(alias="dialerConfig")
    name: str = Field(alias="name")
    outbound_call_config: OutboundCallConfigModel = Field(alias="outboundCallConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateCampaignDialerConfigRequestModel(BaseModel):
    dialer_config: DialerConfigModel = Field(alias="dialerConfig")
    id: str = Field(alias="id")


class GetConnectInstanceConfigResponseModel(BaseModel):
    connect_instance_config: InstanceConfigModel = Field(alias="connectInstanceConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCampaignResponseModel(BaseModel):
    campaign: CampaignModel = Field(alias="campaign")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
