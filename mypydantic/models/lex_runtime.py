# Model Generated: Thu Mar  2 21:56:20 2023

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


class ActiveContextTimeToLiveModel(BaseModel):
    time_to_live_in_seconds: Optional[int] = Field(
        default=None, alias="timeToLiveInSeconds"
    )
    turns_to_live: Optional[int] = Field(default=None, alias="turnsToLive")


class ButtonModel(BaseModel):
    text: str = Field(alias="text")
    value: str = Field(alias="value")


class DeleteSessionRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DialogActionModel(BaseModel):
    type: Literal[
        "Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot"
    ] = Field(alias="type")
    intent_name: Optional[str] = Field(default=None, alias="intentName")
    slots: Optional[Dict[str, str]] = Field(default=None, alias="slots")
    slot_to_elicit: Optional[str] = Field(default=None, alias="slotToElicit")
    fulfillment_state: Optional[
        Literal["Failed", "Fulfilled", "ReadyForFulfillment"]
    ] = Field(default=None, alias="fulfillmentState")
    message: Optional[str] = Field(default=None, alias="message")
    message_format: Optional[
        Literal["Composite", "CustomPayload", "PlainText", "SSML"]
    ] = Field(default=None, alias="messageFormat")


class GetSessionRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")
    checkpoint_label_filter: Optional[str] = Field(
        default=None, alias="checkpointLabelFilter"
    )


class IntentSummaryModel(BaseModel):
    dialog_action_type: Literal[
        "Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot"
    ] = Field(alias="dialogActionType")
    intent_name: Optional[str] = Field(default=None, alias="intentName")
    checkpoint_label: Optional[str] = Field(default=None, alias="checkpointLabel")
    slots: Optional[Dict[str, str]] = Field(default=None, alias="slots")
    confirmation_status: Optional[Literal["Confirmed", "Denied", "None"]] = Field(
        default=None, alias="confirmationStatus"
    )
    fulfillment_state: Optional[
        Literal["Failed", "Fulfilled", "ReadyForFulfillment"]
    ] = Field(default=None, alias="fulfillmentState")
    slot_to_elicit: Optional[str] = Field(default=None, alias="slotToElicit")


class IntentConfidenceModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="score")


class PostContentRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")
    content_type: str = Field(alias="contentType")
    input_stream: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="inputStream"
    )
    session_attributes: Optional[str] = Field(default=None, alias="sessionAttributes")
    request_attributes: Optional[str] = Field(default=None, alias="requestAttributes")
    accept: Optional[str] = Field(default=None, alias="accept")
    active_contexts: Optional[str] = Field(default=None, alias="activeContexts")


class SentimentResponseModel(BaseModel):
    sentiment_label: Optional[str] = Field(default=None, alias="sentimentLabel")
    sentiment_score: Optional[str] = Field(default=None, alias="sentimentScore")


class ActiveContextModel(BaseModel):
    name: str = Field(alias="name")
    time_to_live: ActiveContextTimeToLiveModel = Field(alias="timeToLive")
    parameters: Dict[str, str] = Field(alias="parameters")


class GenericAttachmentModel(BaseModel):
    title: Optional[str] = Field(default=None, alias="title")
    sub_title: Optional[str] = Field(default=None, alias="subTitle")
    attachment_link_url: Optional[str] = Field(default=None, alias="attachmentLinkUrl")
    image_url: Optional[str] = Field(default=None, alias="imageUrl")
    buttons: Optional[List[ButtonModel]] = Field(default=None, alias="buttons")


class DeleteSessionResponseModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")
    session_id: str = Field(alias="sessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PostContentResponseModel(BaseModel):
    content_type: str = Field(alias="contentType")
    intent_name: str = Field(alias="intentName")
    nlu_intent_confidence: str = Field(alias="nluIntentConfidence")
    alternative_intents: str = Field(alias="alternativeIntents")
    slots: str = Field(alias="slots")
    session_attributes: str = Field(alias="sessionAttributes")
    sentiment_response: str = Field(alias="sentimentResponse")
    message: str = Field(alias="message")
    encoded_message: str = Field(alias="encodedMessage")
    message_format: Literal["Composite", "CustomPayload", "PlainText", "SSML"] = Field(
        alias="messageFormat"
    )
    dialog_state: Literal[
        "ConfirmIntent",
        "ElicitIntent",
        "ElicitSlot",
        "Failed",
        "Fulfilled",
        "ReadyForFulfillment",
    ] = Field(alias="dialogState")
    slot_to_elicit: str = Field(alias="slotToElicit")
    input_transcript: str = Field(alias="inputTranscript")
    encoded_input_transcript: str = Field(alias="encodedInputTranscript")
    audio_stream: Type[StreamingBody] = Field(alias="audioStream")
    bot_version: str = Field(alias="botVersion")
    session_id: str = Field(alias="sessionId")
    active_contexts: str = Field(alias="activeContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSessionResponseModel(BaseModel):
    content_type: str = Field(alias="contentType")
    intent_name: str = Field(alias="intentName")
    slots: str = Field(alias="slots")
    session_attributes: str = Field(alias="sessionAttributes")
    message: str = Field(alias="message")
    encoded_message: str = Field(alias="encodedMessage")
    message_format: Literal["Composite", "CustomPayload", "PlainText", "SSML"] = Field(
        alias="messageFormat"
    )
    dialog_state: Literal[
        "ConfirmIntent",
        "ElicitIntent",
        "ElicitSlot",
        "Failed",
        "Fulfilled",
        "ReadyForFulfillment",
    ] = Field(alias="dialogState")
    slot_to_elicit: str = Field(alias="slotToElicit")
    audio_stream: Type[StreamingBody] = Field(alias="audioStream")
    session_id: str = Field(alias="sessionId")
    active_contexts: str = Field(alias="activeContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PredictedIntentModel(BaseModel):
    intent_name: Optional[str] = Field(default=None, alias="intentName")
    nlu_intent_confidence: Optional[IntentConfidenceModel] = Field(
        default=None, alias="nluIntentConfidence"
    )
    slots: Optional[Dict[str, str]] = Field(default=None, alias="slots")


class GetSessionResponseModel(BaseModel):
    recent_intent_summary_view: List[IntentSummaryModel] = Field(
        alias="recentIntentSummaryView"
    )
    session_attributes: Dict[str, str] = Field(alias="sessionAttributes")
    session_id: str = Field(alias="sessionId")
    dialog_action: DialogActionModel = Field(alias="dialogAction")
    active_contexts: List[ActiveContextModel] = Field(alias="activeContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PostTextRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")
    input_text: str = Field(alias="inputText")
    session_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="sessionAttributes"
    )
    request_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestAttributes"
    )
    active_contexts: Optional[Sequence[ActiveContextModel]] = Field(
        default=None, alias="activeContexts"
    )


class PutSessionRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    user_id: str = Field(alias="userId")
    session_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="sessionAttributes"
    )
    dialog_action: Optional[DialogActionModel] = Field(
        default=None, alias="dialogAction"
    )
    recent_intent_summary_view: Optional[Sequence[IntentSummaryModel]] = Field(
        default=None, alias="recentIntentSummaryView"
    )
    accept: Optional[str] = Field(default=None, alias="accept")
    active_contexts: Optional[Sequence[ActiveContextModel]] = Field(
        default=None, alias="activeContexts"
    )


class ResponseCardModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    content_type: Optional[Literal["application/vnd.amazonaws.card.generic"]] = Field(
        default=None, alias="contentType"
    )
    generic_attachments: Optional[List[GenericAttachmentModel]] = Field(
        default=None, alias="genericAttachments"
    )


class PostTextResponseModel(BaseModel):
    intent_name: str = Field(alias="intentName")
    nlu_intent_confidence: IntentConfidenceModel = Field(alias="nluIntentConfidence")
    alternative_intents: List[PredictedIntentModel] = Field(alias="alternativeIntents")
    slots: Dict[str, str] = Field(alias="slots")
    session_attributes: Dict[str, str] = Field(alias="sessionAttributes")
    message: str = Field(alias="message")
    sentiment_response: SentimentResponseModel = Field(alias="sentimentResponse")
    message_format: Literal["Composite", "CustomPayload", "PlainText", "SSML"] = Field(
        alias="messageFormat"
    )
    dialog_state: Literal[
        "ConfirmIntent",
        "ElicitIntent",
        "ElicitSlot",
        "Failed",
        "Fulfilled",
        "ReadyForFulfillment",
    ] = Field(alias="dialogState")
    slot_to_elicit: str = Field(alias="slotToElicit")
    response_card: ResponseCardModel = Field(alias="responseCard")
    session_id: str = Field(alias="sessionId")
    bot_version: str = Field(alias="botVersion")
    active_contexts: List[ActiveContextModel] = Field(alias="activeContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
