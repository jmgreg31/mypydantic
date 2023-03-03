# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptPageRequestModel(BaseModel):
    page_id: str = Field(alias="PageId")
    accept_type: Literal["DELIVERED", "READ"] = Field(alias="AcceptType")
    accept_code: str = Field(alias="AcceptCode")
    contact_channel_id: Optional[str] = Field(default=None, alias="ContactChannelId")
    note: Optional[str] = Field(default=None, alias="Note")
    accept_code_validation: Optional[Literal["ENFORCE", "IGNORE"]] = Field(
        default=None, alias="AcceptCodeValidation"
    )


class ActivateContactChannelRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")
    activation_code: str = Field(alias="ActivationCode")


class ChannelTargetInfoModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")
    retry_interval_in_minutes: Optional[int] = Field(
        default=None, alias="RetryIntervalInMinutes"
    )


class ContactChannelAddressModel(BaseModel):
    simple_address: Optional[str] = Field(default=None, alias="SimpleAddress")


class ContactTargetInfoModel(BaseModel):
    is_essential: bool = Field(alias="IsEssential")
    contact_id: Optional[str] = Field(default=None, alias="ContactId")


class ContactModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    alias: str = Field(alias="Alias")
    type: Literal["ESCALATION", "PERSONAL"] = Field(alias="Type")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class DeactivateContactChannelRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")


class DeleteContactChannelRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")


class DeleteContactRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")


class DescribeEngagementRequestModel(BaseModel):
    engagement_id: str = Field(alias="EngagementId")


class DescribePageRequestModel(BaseModel):
    page_id: str = Field(alias="PageId")


class EngagementModel(BaseModel):
    engagement_arn: str = Field(alias="EngagementArn")
    contact_arn: str = Field(alias="ContactArn")
    sender: str = Field(alias="Sender")
    incident_id: Optional[str] = Field(default=None, alias="IncidentId")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    stop_time: Optional[datetime] = Field(default=None, alias="StopTime")


class GetContactChannelRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")


class GetContactPolicyRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")


class GetContactRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListContactChannelsRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListContactsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    alias_prefix: Optional[str] = Field(default=None, alias="AliasPrefix")
    type: Optional[Literal["ESCALATION", "PERSONAL"]] = Field(
        default=None, alias="Type"
    )


class TimeRangeModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")


class ListPageReceiptsRequestModel(BaseModel):
    page_id: str = Field(alias="PageId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ReceiptModel(BaseModel):
    receipt_type: Literal["DELIVERED", "ERROR", "READ", "SENT", "STOP"] = Field(
        alias="ReceiptType"
    )
    receipt_time: datetime = Field(alias="ReceiptTime")
    contact_channel_arn: Optional[str] = Field(default=None, alias="ContactChannelArn")
    receipt_info: Optional[str] = Field(default=None, alias="ReceiptInfo")


class ListPagesByContactRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PageModel(BaseModel):
    page_arn: str = Field(alias="PageArn")
    engagement_arn: str = Field(alias="EngagementArn")
    contact_arn: str = Field(alias="ContactArn")
    sender: str = Field(alias="Sender")
    incident_id: Optional[str] = Field(default=None, alias="IncidentId")
    sent_time: Optional[datetime] = Field(default=None, alias="SentTime")
    delivery_time: Optional[datetime] = Field(default=None, alias="DeliveryTime")
    read_time: Optional[datetime] = Field(default=None, alias="ReadTime")


class ListPagesByEngagementRequestModel(BaseModel):
    engagement_id: str = Field(alias="EngagementId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class PutContactPolicyRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    policy: str = Field(alias="Policy")


class SendActivationCodeRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")


class StartEngagementRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    sender: str = Field(alias="Sender")
    subject: str = Field(alias="Subject")
    content: str = Field(alias="Content")
    public_subject: Optional[str] = Field(default=None, alias="PublicSubject")
    public_content: Optional[str] = Field(default=None, alias="PublicContent")
    incident_id: Optional[str] = Field(default=None, alias="IncidentId")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class StopEngagementRequestModel(BaseModel):
    engagement_id: str = Field(alias="EngagementId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ContactChannelModel(BaseModel):
    contact_channel_arn: str = Field(alias="ContactChannelArn")
    contact_arn: str = Field(alias="ContactArn")
    name: str = Field(alias="Name")
    delivery_address: ContactChannelAddressModel = Field(alias="DeliveryAddress")
    activation_status: Literal["ACTIVATED", "NOT_ACTIVATED"] = Field(
        alias="ActivationStatus"
    )
    type: Optional[Literal["EMAIL", "SMS", "VOICE"]] = Field(default=None, alias="Type")


class CreateContactChannelRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    name: str = Field(alias="Name")
    type: Literal["EMAIL", "SMS", "VOICE"] = Field(alias="Type")
    delivery_address: ContactChannelAddressModel = Field(alias="DeliveryAddress")
    defer_activation: Optional[bool] = Field(default=None, alias="DeferActivation")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class UpdateContactChannelRequestModel(BaseModel):
    contact_channel_id: str = Field(alias="ContactChannelId")
    name: Optional[str] = Field(default=None, alias="Name")
    delivery_address: Optional[ContactChannelAddressModel] = Field(
        default=None, alias="DeliveryAddress"
    )


class TargetModel(BaseModel):
    channel_target_info: Optional[ChannelTargetInfoModel] = Field(
        default=None, alias="ChannelTargetInfo"
    )
    contact_target_info: Optional[ContactTargetInfoModel] = Field(
        default=None, alias="ContactTargetInfo"
    )


class CreateContactChannelResultModel(BaseModel):
    contact_channel_arn: str = Field(alias="ContactChannelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContactResultModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEngagementResultModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    engagement_arn: str = Field(alias="EngagementArn")
    sender: str = Field(alias="Sender")
    subject: str = Field(alias="Subject")
    content: str = Field(alias="Content")
    public_subject: str = Field(alias="PublicSubject")
    public_content: str = Field(alias="PublicContent")
    incident_id: str = Field(alias="IncidentId")
    start_time: datetime = Field(alias="StartTime")
    stop_time: datetime = Field(alias="StopTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePageResultModel(BaseModel):
    page_arn: str = Field(alias="PageArn")
    engagement_arn: str = Field(alias="EngagementArn")
    contact_arn: str = Field(alias="ContactArn")
    sender: str = Field(alias="Sender")
    subject: str = Field(alias="Subject")
    content: str = Field(alias="Content")
    public_subject: str = Field(alias="PublicSubject")
    public_content: str = Field(alias="PublicContent")
    incident_id: str = Field(alias="IncidentId")
    sent_time: datetime = Field(alias="SentTime")
    read_time: datetime = Field(alias="ReadTime")
    delivery_time: datetime = Field(alias="DeliveryTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactChannelResultModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    contact_channel_arn: str = Field(alias="ContactChannelArn")
    name: str = Field(alias="Name")
    type: Literal["EMAIL", "SMS", "VOICE"] = Field(alias="Type")
    delivery_address: ContactChannelAddressModel = Field(alias="DeliveryAddress")
    activation_status: Literal["ACTIVATED", "NOT_ACTIVATED"] = Field(
        alias="ActivationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactPolicyResultModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContactsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    contacts: List[ContactModel] = Field(alias="Contacts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartEngagementResultModel(BaseModel):
    engagement_arn: str = Field(alias="EngagementArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListEngagementsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    engagements: List[EngagementModel] = Field(alias="Engagements")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContactChannelsRequestListContactChannelsPaginateModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContactsRequestListContactsPaginateModel(BaseModel):
    alias_prefix: Optional[str] = Field(default=None, alias="AliasPrefix")
    type: Optional[Literal["ESCALATION", "PERSONAL"]] = Field(
        default=None, alias="Type"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPageReceiptsRequestListPageReceiptsPaginateModel(BaseModel):
    page_id: str = Field(alias="PageId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPagesByContactRequestListPagesByContactPaginateModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPagesByEngagementRequestListPagesByEngagementPaginateModel(BaseModel):
    engagement_id: str = Field(alias="EngagementId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEngagementsRequestListEngagementsPaginateModel(BaseModel):
    incident_id: Optional[str] = Field(default=None, alias="IncidentId")
    time_range_value: Optional[TimeRangeModel] = Field(
        default=None, alias="TimeRangeValue"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEngagementsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    incident_id: Optional[str] = Field(default=None, alias="IncidentId")
    time_range_value: Optional[TimeRangeModel] = Field(
        default=None, alias="TimeRangeValue"
    )


class ListPageReceiptsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    receipts: List[ReceiptModel] = Field(alias="Receipts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPagesByContactResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    pages: List[PageModel] = Field(alias="Pages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPagesByEngagementResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    pages: List[PageModel] = Field(alias="Pages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContactChannelsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    contact_channels: List[ContactChannelModel] = Field(alias="ContactChannels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StageModel(BaseModel):
    duration_in_minutes: int = Field(alias="DurationInMinutes")
    targets: Sequence[TargetModel] = Field(alias="Targets")


class PlanModel(BaseModel):
    stages: Sequence[StageModel] = Field(alias="Stages")


class CreateContactRequestModel(BaseModel):
    alias: str = Field(alias="Alias")
    type: Literal["ESCALATION", "PERSONAL"] = Field(alias="Type")
    plan: PlanModel = Field(alias="Plan")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class GetContactResultModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    alias: str = Field(alias="Alias")
    display_name: str = Field(alias="DisplayName")
    type: Literal["ESCALATION", "PERSONAL"] = Field(alias="Type")
    plan: PlanModel = Field(alias="Plan")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContactRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    plan: Optional[PlanModel] = Field(default=None, alias="Plan")
