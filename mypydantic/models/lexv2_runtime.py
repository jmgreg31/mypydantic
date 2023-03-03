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
    time_to_live_in_seconds: int = Field(alias="timeToLiveInSeconds")
    turns_to_live: int = Field(alias="turnsToLive")


class ButtonModel(BaseModel):
    text: str = Field(alias="text")
    value: str = Field(alias="value")


class ConfidenceScoreModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="score")


class DeleteSessionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DialogActionModel(BaseModel):
    type: Literal[
        "Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot", "None"
    ] = Field(alias="type")
    slot_to_elicit: Optional[str] = Field(default=None, alias="slotToElicit")
    slot_elicitation_style: Optional[
        Literal["Default", "SpellByLetter", "SpellByWord"]
    ] = Field(default=None, alias="slotElicitationStyle")
    sub_slot_to_elicit: Optional[ElicitSubSlotModel] = Field(
        default=None, alias="subSlotToElicit"
    )


class ElicitSubSlotModel(BaseModel):
    name: str = Field(alias="name")
    sub_slot_to_elicit: Optional[Dict[str, Any]] = Field(
        default=None, alias="subSlotToElicit"
    )


class GetSessionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")


class IntentModel(BaseModel):
    name: str = Field(alias="name")
    slots: Optional[Dict[str, SlotModel]] = Field(default=None, alias="slots")
    state: Optional[
        Literal[
            "Failed",
            "Fulfilled",
            "FulfillmentInProgress",
            "InProgress",
            "ReadyForFulfillment",
            "Waiting",
        ]
    ] = Field(default=None, alias="state")
    confirmation_state: Optional[Literal["Confirmed", "Denied", "None"]] = Field(
        default=None, alias="confirmationState"
    )


class RecognizedBotMemberModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: Optional[str] = Field(default=None, alias="botName")


class RecognizeUtteranceRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")
    request_content_type: str = Field(alias="requestContentType")
    session_state: Optional[str] = Field(default=None, alias="sessionState")
    request_attributes: Optional[str] = Field(default=None, alias="requestAttributes")
    response_content_type: Optional[str] = Field(
        default=None, alias="responseContentType"
    )
    input_stream: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="inputStream")


class RuntimeHintValueModel(BaseModel):
    phrase: str = Field(alias="phrase")


class RuntimeHintsModel(BaseModel):
    slot_hints: Optional[Dict[str, Dict[str, RuntimeHintDetailsModel]]] = Field(
        default=None, alias="slotHints"
    )


class SentimentScoreModel(BaseModel):
    positive: Optional[float] = Field(default=None, alias="positive")
    negative: Optional[float] = Field(default=None, alias="negative")
    neutral: Optional[float] = Field(default=None, alias="neutral")
    mixed: Optional[float] = Field(default=None, alias="mixed")


class ValueModel(BaseModel):
    interpreted_value: str = Field(alias="interpretedValue")
    original_value: Optional[str] = Field(default=None, alias="originalValue")
    resolved_values: Optional[List[str]] = Field(default=None, alias="resolvedValues")


class ActiveContextModel(BaseModel):
    name: str = Field(alias="name")
    time_to_live: ActiveContextTimeToLiveModel = Field(alias="timeToLive")
    context_attributes: Dict[str, str] = Field(alias="contextAttributes")


class ImageResponseCardModel(BaseModel):
    title: str = Field(alias="title")
    subtitle: Optional[str] = Field(default=None, alias="subtitle")
    image_url: Optional[str] = Field(default=None, alias="imageUrl")
    buttons: Optional[List[ButtonModel]] = Field(default=None, alias="buttons")


class DeleteSessionResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSessionResponseModel(BaseModel):
    content_type: str = Field(alias="contentType")
    messages: str = Field(alias="messages")
    session_state: str = Field(alias="sessionState")
    request_attributes: str = Field(alias="requestAttributes")
    session_id: str = Field(alias="sessionId")
    audio_stream: Type[StreamingBody] = Field(alias="audioStream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecognizeUtteranceResponseModel(BaseModel):
    input_mode: str = Field(alias="inputMode")
    content_type: str = Field(alias="contentType")
    messages: str = Field(alias="messages")
    interpretations: str = Field(alias="interpretations")
    session_state: str = Field(alias="sessionState")
    request_attributes: str = Field(alias="requestAttributes")
    session_id: str = Field(alias="sessionId")
    input_transcript: str = Field(alias="inputTranscript")
    audio_stream: Type[StreamingBody] = Field(alias="audioStream")
    recognized_bot_member: str = Field(alias="recognizedBotMember")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuntimeHintDetailsModel(BaseModel):
    runtime_hint_values: Optional[List[RuntimeHintValueModel]] = Field(
        default=None, alias="runtimeHintValues"
    )
    sub_slot_hints: Optional[Dict[str, Dict[str, Any]]] = Field(
        default=None, alias="subSlotHints"
    )


class SentimentResponseModel(BaseModel):
    sentiment: Optional[Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]] = Field(
        default=None, alias="sentiment"
    )
    sentiment_score: Optional[SentimentScoreModel] = Field(
        default=None, alias="sentimentScore"
    )


class SlotModel(BaseModel):
    value: Optional[ValueModel] = Field(default=None, alias="value")
    shape: Optional[Literal["Composite", "List", "Scalar"]] = Field(
        default=None, alias="shape"
    )
    values: Optional[List[Dict[str, Any]]] = Field(default=None, alias="values")
    sub_slots: Optional[Dict[str, Dict[str, Any]]] = Field(
        default=None, alias="subSlots"
    )


class SessionStateModel(BaseModel):
    dialog_action: Optional[DialogActionModel] = Field(
        default=None, alias="dialogAction"
    )
    intent: Optional[IntentModel] = Field(default=None, alias="intent")
    active_contexts: Optional[List[ActiveContextModel]] = Field(
        default=None, alias="activeContexts"
    )
    session_attributes: Optional[Dict[str, str]] = Field(
        default=None, alias="sessionAttributes"
    )
    originating_request_id: Optional[str] = Field(
        default=None, alias="originatingRequestId"
    )
    runtime_hints: Optional[RuntimeHintsModel] = Field(
        default=None, alias="runtimeHints"
    )


class MessageModel(BaseModel):
    content_type: Literal[
        "CustomPayload", "ImageResponseCard", "PlainText", "SSML"
    ] = Field(alias="contentType")
    content: Optional[str] = Field(default=None, alias="content")
    image_response_card: Optional[ImageResponseCardModel] = Field(
        default=None, alias="imageResponseCard"
    )


class InterpretationModel(BaseModel):
    nlu_confidence: Optional[ConfidenceScoreModel] = Field(
        default=None, alias="nluConfidence"
    )
    sentiment_response: Optional[SentimentResponseModel] = Field(
        default=None, alias="sentimentResponse"
    )
    intent: Optional[IntentModel] = Field(default=None, alias="intent")


class RecognizeTextRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")
    text: str = Field(alias="text")
    session_state: Optional[SessionStateModel] = Field(
        default=None, alias="sessionState"
    )
    request_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestAttributes"
    )


class PutSessionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    locale_id: str = Field(alias="localeId")
    session_id: str = Field(alias="sessionId")
    session_state: SessionStateModel = Field(alias="sessionState")
    messages: Optional[Sequence[MessageModel]] = Field(default=None, alias="messages")
    request_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestAttributes"
    )
    response_content_type: Optional[str] = Field(
        default=None, alias="responseContentType"
    )


class GetSessionResponseModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    messages: List[MessageModel] = Field(alias="messages")
    interpretations: List[InterpretationModel] = Field(alias="interpretations")
    session_state: SessionStateModel = Field(alias="sessionState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecognizeTextResponseModel(BaseModel):
    messages: List[MessageModel] = Field(alias="messages")
    session_state: SessionStateModel = Field(alias="sessionState")
    interpretations: List[InterpretationModel] = Field(alias="interpretations")
    request_attributes: Dict[str, str] = Field(alias="requestAttributes")
    session_id: str = Field(alias="sessionId")
    recognized_bot_member: RecognizedBotMemberModel = Field(alias="recognizedBotMember")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
