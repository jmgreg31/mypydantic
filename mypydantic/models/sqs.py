# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

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


class AddPermissionRequestQueueAddPermissionModel(BaseModel):
    label: str = Field(alias="Label")
    aws_account_ids: Sequence[str] = Field(alias="AWSAccountIds")
    actions: Sequence[str] = Field(alias="Actions")


class AddPermissionRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    label: str = Field(alias="Label")
    aws_account_ids: Sequence[str] = Field(alias="AWSAccountIds")
    actions: Sequence[str] = Field(alias="Actions")


class BatchResultErrorEntryModel(BaseModel):
    id: str = Field(alias="Id")
    sender_fault: bool = Field(alias="SenderFault")
    code: str = Field(alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class ChangeMessageVisibilityBatchRequestEntryModel(BaseModel):
    id: str = Field(alias="Id")
    receipt_handle: str = Field(alias="ReceiptHandle")
    visibility_timeout: Optional[int] = Field(default=None, alias="VisibilityTimeout")


class ChangeMessageVisibilityBatchResultEntryModel(BaseModel):
    id: str = Field(alias="Id")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ChangeMessageVisibilityRequestMessageChangeVisibilityModel(BaseModel):
    visibility_timeout: int = Field(alias="VisibilityTimeout")


class ChangeMessageVisibilityRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    receipt_handle: str = Field(alias="ReceiptHandle")
    visibility_timeout: int = Field(alias="VisibilityTimeout")


class CreateQueueRequestModel(BaseModel):
    queue_name: str = Field(alias="QueueName")
    attributes: Optional[
        Mapping[
            Literal[
                "All",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesDelayed",
                "ApproximateNumberOfMessagesNotVisible",
                "ContentBasedDeduplication",
                "CreatedTimestamp",
                "DeduplicationScope",
                "DelaySeconds",
                "FifoQueue",
                "FifoThroughputLimit",
                "KmsDataKeyReusePeriodSeconds",
                "KmsMasterKeyId",
                "LastModifiedTimestamp",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "Policy",
                "QueueArn",
                "ReceiveMessageWaitTimeSeconds",
                "RedriveAllowPolicy",
                "RedrivePolicy",
                "SqsManagedSseEnabled",
                "VisibilityTimeout",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateQueueRequestServiceResourceCreateQueueModel(BaseModel):
    queue_name: str = Field(alias="QueueName")
    attributes: Optional[
        Mapping[
            Literal[
                "All",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesDelayed",
                "ApproximateNumberOfMessagesNotVisible",
                "ContentBasedDeduplication",
                "CreatedTimestamp",
                "DeduplicationScope",
                "DelaySeconds",
                "FifoQueue",
                "FifoThroughputLimit",
                "KmsDataKeyReusePeriodSeconds",
                "KmsMasterKeyId",
                "LastModifiedTimestamp",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "Policy",
                "QueueArn",
                "ReceiveMessageWaitTimeSeconds",
                "RedriveAllowPolicy",
                "RedrivePolicy",
                "SqsManagedSseEnabled",
                "VisibilityTimeout",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteMessageBatchRequestEntryModel(BaseModel):
    id: str = Field(alias="Id")
    receipt_handle: str = Field(alias="ReceiptHandle")


class DeleteMessageBatchResultEntryModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteMessageRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    receipt_handle: str = Field(alias="ReceiptHandle")


class DeleteQueueRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")


class GetQueueAttributesRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    attribute_names: Optional[
        Sequence[
            Literal[
                "AWSTraceHeader",
                "All",
                "ApproximateFirstReceiveTimestamp",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesDelayed",
                "ApproximateNumberOfMessagesNotVisible",
                "ApproximateReceiveCount",
                "ContentBasedDeduplication",
                "CreatedTimestamp",
                "DeduplicationScope",
                "DelaySeconds",
                "FifoQueue",
                "FifoThroughputLimit",
                "KmsDataKeyReusePeriodSeconds",
                "KmsMasterKeyId",
                "LastModifiedTimestamp",
                "MaximumMessageSize",
                "MessageDeduplicationId",
                "MessageGroupId",
                "MessageRetentionPeriod",
                "Policy",
                "QueueArn",
                "ReceiveMessageWaitTimeSeconds",
                "RedriveAllowPolicy",
                "RedrivePolicy",
                "SenderId",
                "SentTimestamp",
                "SequenceNumber",
                "SqsManagedSseEnabled",
                "VisibilityTimeout",
            ]
        ]
    ] = Field(default=None, alias="AttributeNames")


class GetQueueUrlRequestModel(BaseModel):
    queue_name: str = Field(alias="QueueName")
    queue_owner_aws_account_id: Optional[str] = Field(
        default=None, alias="QueueOwnerAWSAccountId"
    )


class GetQueueUrlRequestServiceResourceGetQueueByNameModel(BaseModel):
    queue_name: str = Field(alias="QueueName")
    queue_owner_aws_account_id: Optional[str] = Field(
        default=None, alias="QueueOwnerAWSAccountId"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDeadLetterSourceQueuesRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListQueueTagsRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")


class ListQueuesRequestModel(BaseModel):
    queue_name_prefix: Optional[str] = Field(default=None, alias="QueueNamePrefix")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MessageAttributeValueModel(BaseModel):
    data_type: str = Field(alias="DataType")
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    binary_value: Optional[bytes] = Field(default=None, alias="BinaryValue")
    string_list_values: Optional[List[str]] = Field(
        default=None, alias="StringListValues"
    )
    binary_list_values: Optional[List[bytes]] = Field(
        default=None, alias="BinaryListValues"
    )


class MessageSystemAttributeValueModel(BaseModel):
    data_type: str = Field(alias="DataType")
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    binary_value: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="BinaryValue")
    string_list_values: Optional[Sequence[str]] = Field(
        default=None, alias="StringListValues"
    )
    binary_list_values: Optional[
        Sequence[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]]
    ] = Field(default=None, alias="BinaryListValues")


class PurgeQueueRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")


class QueueMessageRequestModel(BaseModel):
    receipt_handle: str = Field(alias="receipt_handle")


class ReceiveMessageRequestQueueReceiveMessagesModel(BaseModel):
    attribute_names: Optional[
        Sequence[
            Literal[
                "AWSTraceHeader",
                "All",
                "ApproximateFirstReceiveTimestamp",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesDelayed",
                "ApproximateNumberOfMessagesNotVisible",
                "ApproximateReceiveCount",
                "ContentBasedDeduplication",
                "CreatedTimestamp",
                "DeduplicationScope",
                "DelaySeconds",
                "FifoQueue",
                "FifoThroughputLimit",
                "KmsDataKeyReusePeriodSeconds",
                "KmsMasterKeyId",
                "LastModifiedTimestamp",
                "MaximumMessageSize",
                "MessageDeduplicationId",
                "MessageGroupId",
                "MessageRetentionPeriod",
                "Policy",
                "QueueArn",
                "ReceiveMessageWaitTimeSeconds",
                "RedriveAllowPolicy",
                "RedrivePolicy",
                "SenderId",
                "SentTimestamp",
                "SequenceNumber",
                "SqsManagedSseEnabled",
                "VisibilityTimeout",
            ]
        ]
    ] = Field(default=None, alias="AttributeNames")
    message_attribute_names: Optional[Sequence[str]] = Field(
        default=None, alias="MessageAttributeNames"
    )
    max_number_of_messages: Optional[int] = Field(
        default=None, alias="MaxNumberOfMessages"
    )
    visibility_timeout: Optional[int] = Field(default=None, alias="VisibilityTimeout")
    wait_time_seconds: Optional[int] = Field(default=None, alias="WaitTimeSeconds")
    receive_request_attempt_id: Optional[str] = Field(
        default=None, alias="ReceiveRequestAttemptId"
    )


class ReceiveMessageRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    attribute_names: Optional[
        Sequence[
            Literal[
                "AWSTraceHeader",
                "All",
                "ApproximateFirstReceiveTimestamp",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesDelayed",
                "ApproximateNumberOfMessagesNotVisible",
                "ApproximateReceiveCount",
                "ContentBasedDeduplication",
                "CreatedTimestamp",
                "DeduplicationScope",
                "DelaySeconds",
                "FifoQueue",
                "FifoThroughputLimit",
                "KmsDataKeyReusePeriodSeconds",
                "KmsMasterKeyId",
                "LastModifiedTimestamp",
                "MaximumMessageSize",
                "MessageDeduplicationId",
                "MessageGroupId",
                "MessageRetentionPeriod",
                "Policy",
                "QueueArn",
                "ReceiveMessageWaitTimeSeconds",
                "RedriveAllowPolicy",
                "RedrivePolicy",
                "SenderId",
                "SentTimestamp",
                "SequenceNumber",
                "SqsManagedSseEnabled",
                "VisibilityTimeout",
            ]
        ]
    ] = Field(default=None, alias="AttributeNames")
    message_attribute_names: Optional[Sequence[str]] = Field(
        default=None, alias="MessageAttributeNames"
    )
    max_number_of_messages: Optional[int] = Field(
        default=None, alias="MaxNumberOfMessages"
    )
    visibility_timeout: Optional[int] = Field(default=None, alias="VisibilityTimeout")
    wait_time_seconds: Optional[int] = Field(default=None, alias="WaitTimeSeconds")
    receive_request_attempt_id: Optional[str] = Field(
        default=None, alias="ReceiveRequestAttemptId"
    )


class RemovePermissionRequestQueueRemovePermissionModel(BaseModel):
    label: str = Field(alias="Label")


class RemovePermissionRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    label: str = Field(alias="Label")


class SendMessageBatchResultEntryModel(BaseModel):
    id: str = Field(alias="Id")
    message_id: str = Field(alias="MessageId")
    md5_of_message_body: str = Field(alias="MD5OfMessageBody")
    md5_of_message_attributes: Optional[str] = Field(
        default=None, alias="MD5OfMessageAttributes"
    )
    md5_of_message_system_attributes: Optional[str] = Field(
        default=None, alias="MD5OfMessageSystemAttributes"
    )
    sequence_number: Optional[str] = Field(default=None, alias="SequenceNumber")


class ServiceResourceMessageRequestModel(BaseModel):
    queue_url: str = Field(alias="queue_url")
    receipt_handle: str = Field(alias="receipt_handle")


class ServiceResourceQueueRequestModel(BaseModel):
    url: str = Field(alias="url")


class SetQueueAttributesRequestQueueSetAttributesModel(BaseModel):
    attributes: Mapping[
        Literal[
            "All",
            "ApproximateNumberOfMessages",
            "ApproximateNumberOfMessagesDelayed",
            "ApproximateNumberOfMessagesNotVisible",
            "ContentBasedDeduplication",
            "CreatedTimestamp",
            "DeduplicationScope",
            "DelaySeconds",
            "FifoQueue",
            "FifoThroughputLimit",
            "KmsDataKeyReusePeriodSeconds",
            "KmsMasterKeyId",
            "LastModifiedTimestamp",
            "MaximumMessageSize",
            "MessageRetentionPeriod",
            "Policy",
            "QueueArn",
            "ReceiveMessageWaitTimeSeconds",
            "RedriveAllowPolicy",
            "RedrivePolicy",
            "SqsManagedSseEnabled",
            "VisibilityTimeout",
        ],
        str,
    ] = Field(alias="Attributes")


class SetQueueAttributesRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    attributes: Mapping[
        Literal[
            "All",
            "ApproximateNumberOfMessages",
            "ApproximateNumberOfMessagesDelayed",
            "ApproximateNumberOfMessagesNotVisible",
            "ContentBasedDeduplication",
            "CreatedTimestamp",
            "DeduplicationScope",
            "DelaySeconds",
            "FifoQueue",
            "FifoThroughputLimit",
            "KmsDataKeyReusePeriodSeconds",
            "KmsMasterKeyId",
            "LastModifiedTimestamp",
            "MaximumMessageSize",
            "MessageRetentionPeriod",
            "Policy",
            "QueueArn",
            "ReceiveMessageWaitTimeSeconds",
            "RedriveAllowPolicy",
            "RedrivePolicy",
            "SqsManagedSseEnabled",
            "VisibilityTimeout",
        ],
        str,
    ] = Field(alias="Attributes")


class TagQueueRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagQueueRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchModel(
    BaseModel
):
    entries: Sequence[ChangeMessageVisibilityBatchRequestEntryModel] = Field(
        alias="Entries"
    )


class ChangeMessageVisibilityBatchRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    entries: Sequence[ChangeMessageVisibilityBatchRequestEntryModel] = Field(
        alias="Entries"
    )


class ChangeMessageVisibilityBatchResultModel(BaseModel):
    successful: List[ChangeMessageVisibilityBatchResultEntryModel] = Field(
        alias="Successful"
    )
    failed: List[BatchResultErrorEntryModel] = Field(alias="Failed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQueueResultModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueueAttributesResultModel(BaseModel):
    attributes: Dict[
        Literal[
            "All",
            "ApproximateNumberOfMessages",
            "ApproximateNumberOfMessagesDelayed",
            "ApproximateNumberOfMessagesNotVisible",
            "ContentBasedDeduplication",
            "CreatedTimestamp",
            "DeduplicationScope",
            "DelaySeconds",
            "FifoQueue",
            "FifoThroughputLimit",
            "KmsDataKeyReusePeriodSeconds",
            "KmsMasterKeyId",
            "LastModifiedTimestamp",
            "MaximumMessageSize",
            "MessageRetentionPeriod",
            "Policy",
            "QueueArn",
            "ReceiveMessageWaitTimeSeconds",
            "RedriveAllowPolicy",
            "RedrivePolicy",
            "SqsManagedSseEnabled",
            "VisibilityTimeout",
        ],
        str,
    ] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueueUrlResultModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeadLetterSourceQueuesResultModel(BaseModel):
    queue_urls: List[str] = Field(alias="queueUrls")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueueTagsResultModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueuesResultModel(BaseModel):
    queue_urls: List[str] = Field(alias="QueueUrls")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendMessageResultModel(BaseModel):
    md5_of_message_body: str = Field(alias="MD5OfMessageBody")
    md5_of_message_attributes: str = Field(alias="MD5OfMessageAttributes")
    md5_of_message_system_attributes: str = Field(alias="MD5OfMessageSystemAttributes")
    message_id: str = Field(alias="MessageId")
    sequence_number: str = Field(alias="SequenceNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMessageBatchRequestQueueDeleteMessagesModel(BaseModel):
    entries: Sequence[DeleteMessageBatchRequestEntryModel] = Field(alias="Entries")


class DeleteMessageBatchRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    entries: Sequence[DeleteMessageBatchRequestEntryModel] = Field(alias="Entries")


class DeleteMessageBatchResultModel(BaseModel):
    successful: List[DeleteMessageBatchResultEntryModel] = Field(alias="Successful")
    failed: List[BatchResultErrorEntryModel] = Field(alias="Failed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateModel(
    BaseModel
):
    queue_url: str = Field(alias="QueueUrl")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueuesRequestListQueuesPaginateModel(BaseModel):
    queue_name_prefix: Optional[str] = Field(default=None, alias="QueueNamePrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MessageModel(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="MessageId")
    receipt_handle: Optional[str] = Field(default=None, alias="ReceiptHandle")
    md5_of_body: Optional[str] = Field(default=None, alias="MD5OfBody")
    body: Optional[str] = Field(default=None, alias="Body")
    attributes: Optional[
        Dict[
            Literal[
                "AWSTraceHeader",
                "ApproximateFirstReceiveTimestamp",
                "ApproximateReceiveCount",
                "MessageDeduplicationId",
                "MessageGroupId",
                "SenderId",
                "SentTimestamp",
                "SequenceNumber",
            ],
            str,
        ]
    ] = Field(default=None, alias="Attributes")
    md5_of_message_attributes: Optional[str] = Field(
        default=None, alias="MD5OfMessageAttributes"
    )
    message_attributes: Optional[Dict[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )


class SendMessageBatchRequestEntryModel(BaseModel):
    id: str = Field(alias="Id")
    message_body: str = Field(alias="MessageBody")
    delay_seconds: Optional[int] = Field(default=None, alias="DelaySeconds")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_system_attributes: Optional[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueModel]
    ] = Field(default=None, alias="MessageSystemAttributes")
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class SendMessageRequestQueueSendMessageModel(BaseModel):
    message_body: str = Field(alias="MessageBody")
    delay_seconds: Optional[int] = Field(default=None, alias="DelaySeconds")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_system_attributes: Optional[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueModel]
    ] = Field(default=None, alias="MessageSystemAttributes")
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class SendMessageRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    message_body: str = Field(alias="MessageBody")
    delay_seconds: Optional[int] = Field(default=None, alias="DelaySeconds")
    message_attributes: Optional[Mapping[str, MessageAttributeValueModel]] = Field(
        default=None, alias="MessageAttributes"
    )
    message_system_attributes: Optional[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueModel]
    ] = Field(default=None, alias="MessageSystemAttributes")
    message_deduplication_id: Optional[str] = Field(
        default=None, alias="MessageDeduplicationId"
    )
    message_group_id: Optional[str] = Field(default=None, alias="MessageGroupId")


class SendMessageBatchResultModel(BaseModel):
    successful: List[SendMessageBatchResultEntryModel] = Field(alias="Successful")
    failed: List[BatchResultErrorEntryModel] = Field(alias="Failed")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReceiveMessageResultModel(BaseModel):
    messages: List[MessageModel] = Field(alias="Messages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendMessageBatchRequestQueueSendMessagesModel(BaseModel):
    entries: Sequence[SendMessageBatchRequestEntryModel] = Field(alias="Entries")


class SendMessageBatchRequestModel(BaseModel):
    queue_url: str = Field(alias="QueueUrl")
    entries: Sequence[SendMessageBatchRequestEntryModel] = Field(alias="Entries")
