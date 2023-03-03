# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddPermissionInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    label: str = Field(alias="Label")
    aws_account_id: Sequence[str] = Field(alias="AWSAccountId")
    action_name: Sequence[str] = Field(alias="ActionName")


class AddPermissionInputTopicAddPermissionModel(BaseModel):
    label: str = Field(alias="Label")
    aws_account_id: Sequence[str] = Field(alias="AWSAccountId")
    action_name: Sequence[str] = Field(alias="ActionName")


class BatchResultErrorEntryModel(BaseModel):
    id: str = Field(alias="Id")
    code: str = Field(alias="Code")
    sender_fault: bool = Field(alias="SenderFault")
    message: Optional[str] = Field(default=None, alias="Message")


class CheckIfPhoneNumberIsOptedOutInputRequestModel(BaseModel):
    phone_number: str = Field(alias="phoneNumber")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConfirmSubscriptionInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    token: str = Field(alias="Token")
    authenticate_on_unsubscribe: Optional[str] = Field(
        default=None, alias="AuthenticateOnUnsubscribe"
    )


class ConfirmSubscriptionInputTopicConfirmSubscriptionModel(BaseModel):
    token: str = Field(alias="Token")
    authenticate_on_unsubscribe: Optional[str] = Field(
        default=None, alias="AuthenticateOnUnsubscribe"
    )


class CreatePlatformApplicationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    platform: str = Field(alias="Platform")
    attributes: Mapping[str, str] = Field(alias="Attributes")


class CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationModel(
    BaseModel
):
    name: str = Field(alias="Name")
    platform: str = Field(alias="Platform")
    attributes: Mapping[str, str] = Field(alias="Attributes")


class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointModel(
    BaseModel
):
    token: str = Field(alias="Token")
    custom_user_data: Optional[str] = Field(default=None, alias="CustomUserData")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")


class CreatePlatformEndpointInputRequestModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")
    token: str = Field(alias="Token")
    custom_user_data: Optional[str] = Field(default=None, alias="CustomUserData")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")


class CreateSMSSandboxPhoneNumberInputRequestModel(BaseModel):
    phone_number: str = Field(alias="PhoneNumber")
    language_code: Optional[
        Literal[
            "de-DE",
            "en-GB",
            "en-US",
            "es-419",
            "es-ES",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "kr-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteEndpointInputRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class DeletePlatformApplicationInputRequestModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")


class DeleteSMSSandboxPhoneNumberInputRequestModel(BaseModel):
    phone_number: str = Field(alias="PhoneNumber")


class DeleteTopicInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class EndpointModel(BaseModel):
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class GetDataProtectionPolicyInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetEndpointAttributesInputRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class GetPlatformApplicationAttributesInputRequestModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")


class GetSMSAttributesInputRequestModel(BaseModel):
    attributes: Optional[Sequence[str]] = Field(default=None, alias="attributes")


class GetSubscriptionAttributesInputRequestModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")


class GetTopicAttributesInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEndpointsByPlatformApplicationInputRequestModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOriginationNumbersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PhoneNumberInformationModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    status: Optional[str] = Field(default=None, alias="Status")
    iso2_country_code: Optional[str] = Field(default=None, alias="Iso2CountryCode")
    route_type: Optional[Literal["Premium", "Promotional", "Transactional"]] = Field(
        default=None, alias="RouteType"
    )
    number_capabilities: Optional[List[Literal["MMS", "SMS", "VOICE"]]] = Field(
        default=None, alias="NumberCapabilities"
    )


class ListPhoneNumbersOptedOutInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPlatformApplicationsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PlatformApplicationModel(BaseModel):
    platform_application_arn: Optional[str] = Field(
        default=None, alias="PlatformApplicationArn"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class ListSMSSandboxPhoneNumbersInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SMSSandboxPhoneNumberModel(BaseModel):
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    status: Optional[Literal["Pending", "Verified"]] = Field(
        default=None, alias="Status"
    )


class ListSubscriptionsByTopicInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SubscriptionModel(BaseModel):
    subscription_arn: Optional[str] = Field(default=None, alias="SubscriptionArn")
    owner: Optional[str] = Field(default=None, alias="Owner")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class ListSubscriptionsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListTopicsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TopicModel(BaseModel):
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class MessageAttributeValueModel(BaseModel):
    data_type: str = Field(alias="DataType")
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    binary_value: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="BinaryValue")


class OptInPhoneNumberInputRequestModel(BaseModel):
    phone_number: str = Field(alias="phoneNumber")


class PublishBatchResultEntryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")


class PutDataProtectionPolicyInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    data_protection_policy: str = Field(alias="DataProtectionPolicy")


class RemovePermissionInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    label: str = Field(alias="Label")


class RemovePermissionInputTopicRemovePermissionModel(BaseModel):
    label: str = Field(alias="Label")


class ServiceResourcePlatformApplicationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ServiceResourcePlatformEndpointRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ServiceResourceSubscriptionRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ServiceResourceTopicRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class SetEndpointAttributesInputPlatformEndpointSetAttributesModel(BaseModel):
    attributes: Mapping[str, str] = Field(alias="Attributes")


class SetEndpointAttributesInputRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    attributes: Mapping[str, str] = Field(alias="Attributes")


class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesModel(
    BaseModel
):
    attributes: Mapping[str, str] = Field(alias="Attributes")


class SetPlatformApplicationAttributesInputRequestModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")
    attributes: Mapping[str, str] = Field(alias="Attributes")


class SetSMSAttributesInputRequestModel(BaseModel):
    attributes: Mapping[str, str] = Field(alias="attributes")


class SetSubscriptionAttributesInputRequestModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class SetSubscriptionAttributesInputSubscriptionSetAttributesModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class SetTopicAttributesInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class SetTopicAttributesInputTopicSetAttributesModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_value: Optional[str] = Field(default=None, alias="AttributeValue")


class SubscribeInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    protocol: str = Field(alias="Protocol")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    return_subscription_arn: Optional[bool] = Field(
        default=None, alias="ReturnSubscriptionArn"
    )


class SubscribeInputTopicSubscribeModel(BaseModel):
    protocol: str = Field(alias="Protocol")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    return_subscription_arn: Optional[bool] = Field(
        default=None, alias="ReturnSubscriptionArn"
    )


class UnsubscribeInputRequestModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class VerifySMSSandboxPhoneNumberInputRequestModel(BaseModel):
    phone_number: str = Field(alias="PhoneNumber")
    one_time_password: str = Field(alias="OneTimePassword")


class CheckIfPhoneNumberIsOptedOutResponseModel(BaseModel):
    is_opted_out: bool = Field(alias="isOptedOut")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfirmSubscriptionResponseModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointResponseModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePlatformApplicationResponseModel(BaseModel):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTopicResponseModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataProtectionPolicyResponseModel(BaseModel):
    data_protection_policy: str = Field(alias="DataProtectionPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEndpointAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPlatformApplicationAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSMSAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSMSSandboxAccountStatusResultModel(BaseModel):
    is_in_sandbox: bool = Field(alias="IsInSandbox")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSubscriptionAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTopicAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumbersOptedOutResponseModel(BaseModel):
    phone_numbers: List[str] = Field(alias="phoneNumbers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    sequence_number: str = Field(alias="SequenceNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscribeResponseModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTopicInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    data_protection_policy: Optional[str] = Field(
        default=None, alias="DataProtectionPolicy"
    )


class CreateTopicInputServiceResourceCreateTopicModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    data_protection_policy: Optional[str] = Field(
        default=None, alias="DataProtectionPolicy"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListEndpointsByPlatformApplicationResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointsByPlatformApplicationInputListEndpointsByPlatformApplicationPaginateModel(
    BaseModel
):
    platform_application_arn: str = Field(alias="PlatformApplicationArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOriginationNumbersRequestListOriginationNumbersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlatformApplicationsInputListPlatformApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscriptionsInputListSubscriptionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTopicsInputListTopicsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOriginationNumbersResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    phone_numbers: List[PhoneNumberInformationModel] = Field(alias="PhoneNumbers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlatformApplicationsResponseModel(BaseModel):
    platform_applications: List[PlatformApplicationModel] = Field(
        alias="PlatformApplications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSMSSandboxPhoneNumbersResultModel(BaseModel):
    phone_numbers: List[SMSSandboxPhoneNumberModel] = Field(alias="PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscriptionsByTopicResponseModel(BaseModel):
    subscriptions: List[SubscriptionModel] = Field(alias="Subscriptions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscriptionsResponseModel(BaseModel):
    subscriptions: List[SubscriptionModel] = Field(alias="Subscriptions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTopicsResponseModel(BaseModel):
    topics: List[TopicModel] = Field(alias="Topics")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishBatchRequestEntryModel(BaseModel):
    id: str = Field(alias="Id")
    message: str = Field(alias="Message")
    subject: Optional[str] = Field(default=None, alias="Subject")
    message_structure: Optional[str] = Field(default=None, alias="MessageStructure")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class PublishInputPlatformEndpointPublishModel(BaseModel):
    message: str = Field(alias="Message")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    subject: Optional[str] = Field(default=None, alias="Subject")
    message_structure: Optional[str] = Field(default=None, alias="MessageStructure")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class PublishInputRequestModel(BaseModel):
    message: str = Field(alias="Message")
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    subject: Optional[str] = Field(default=None, alias="Subject")
    message_structure: Optional[str] = Field(default=None, alias="MessageStructure")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class PublishInputTopicPublishModel(BaseModel):
    message: str = Field(alias="Message")
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    subject: Optional[str] = Field(default=None, alias="Subject")
    message_structure: Optional[str] = Field(default=None, alias="MessageStructure")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class PublishBatchResponseModel(BaseModel):
    successful: List[PublishBatchResultEntryModel] = Field(alias="Successful")
    failed: List[BatchResultErrorEntryModel] = Field(alias="Failed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishBatchInputRequestModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")
    publish_batch_request_entries: Sequence[PublishBatchRequestEntryModel] = Field(
        alias="PublishBatchRequestEntries"
    )
