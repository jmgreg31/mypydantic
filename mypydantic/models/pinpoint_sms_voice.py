# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CallInstructionsMessageTypeModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")


class CloudWatchLogsDestinationModel(BaseModel):
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    log_group_arn: Optional[str] = Field(default=None, alias="LogGroupArn")


class CreateConfigurationSetRequestModel(BaseModel):
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )


class DeleteConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")


class DeleteConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class KinesisFirehoseDestinationModel(BaseModel):
    delivery_stream_arn: Optional[str] = Field(default=None, alias="DeliveryStreamArn")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")


class SnsDestinationModel(BaseModel):
    topic_arn: Optional[str] = Field(default=None, alias="TopicArn")


class GetConfigurationSetEventDestinationsRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PlainTextMessageTypeModel(BaseModel):
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    text: Optional[str] = Field(default=None, alias="Text")
    voice_id: Optional[str] = Field(default=None, alias="VoiceId")


class SSMLMessageTypeModel(BaseModel):
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    text: Optional[str] = Field(default=None, alias="Text")
    voice_id: Optional[str] = Field(default=None, alias="VoiceId")


class EventDestinationDefinitionModel(BaseModel):
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="CloudWatchLogsDestination"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    matching_event_types: Optional[
        Sequence[
            Literal[
                "ANSWERED",
                "BUSY",
                "COMPLETED_CALL",
                "FAILED",
                "INITIATED_CALL",
                "NO_ANSWER",
                "RINGING",
            ]
        ]
    ] = Field(default=None, alias="MatchingEventTypes")
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )


class EventDestinationModel(BaseModel):
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="CloudWatchLogsDestination"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    matching_event_types: Optional[
        List[
            Literal[
                "ANSWERED",
                "BUSY",
                "COMPLETED_CALL",
                "FAILED",
                "INITIATED_CALL",
                "NO_ANSWER",
                "RINGING",
            ]
        ]
    ] = Field(default=None, alias="MatchingEventTypes")
    name: Optional[str] = Field(default=None, alias="Name")
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )


class SendVoiceMessageResponseModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VoiceMessageContentModel(BaseModel):
    call_instructions_message: Optional[CallInstructionsMessageTypeModel] = Field(
        default=None, alias="CallInstructionsMessage"
    )
    plain_text_message: Optional[PlainTextMessageTypeModel] = Field(
        default=None, alias="PlainTextMessage"
    )
    s_s_ml_message: Optional[SSMLMessageTypeModel] = Field(
        default=None, alias="SSMLMessage"
    )


class CreateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: Optional[EventDestinationDefinitionModel] = Field(
        default=None, alias="EventDestination"
    )
    event_destination_name: Optional[str] = Field(
        default=None, alias="EventDestinationName"
    )


class UpdateConfigurationSetEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")
    event_destination: Optional[EventDestinationDefinitionModel] = Field(
        default=None, alias="EventDestination"
    )


class GetConfigurationSetEventDestinationsResponseModel(BaseModel):
    event_destinations: List[EventDestinationModel] = Field(alias="EventDestinations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendVoiceMessageRequestModel(BaseModel):
    caller_id: Optional[str] = Field(default=None, alias="CallerId")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    content: Optional[VoiceMessageContentModel] = Field(default=None, alias="Content")
    destination_phone_number: Optional[str] = Field(
        default=None, alias="DestinationPhoneNumber"
    )
    origination_phone_number: Optional[str] = Field(
        default=None, alias="OriginationPhoneNumber"
    )
