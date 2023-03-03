# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AbsoluteTimeRangeModel(BaseModel):
    start_time: Optional[int] = Field(default=None, alias="StartTime")
    end_time: Optional[int] = Field(default=None, alias="EndTime")
    first: Optional[int] = Field(default=None, alias="First")
    last: Optional[int] = Field(default=None, alias="Last")


class ContentRedactionModel(BaseModel):
    redaction_type: Literal["PII"] = Field(alias="RedactionType")
    redaction_output: Literal["redacted", "redacted_and_unredacted"] = Field(
        alias="RedactionOutput"
    )
    pii_entity_types: Optional[
        List[
            Literal[
                "ADDRESS",
                "ALL",
                "BANK_ACCOUNT_NUMBER",
                "BANK_ROUTING",
                "CREDIT_DEBIT_CVV",
                "CREDIT_DEBIT_EXPIRY",
                "CREDIT_DEBIT_NUMBER",
                "EMAIL",
                "NAME",
                "PHONE",
                "PIN",
                "SSN",
            ]
        ]
    ] = Field(default=None, alias="PiiEntityTypes")


class LanguageIdSettingsModel(BaseModel):
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    vocabulary_filter_name: Optional[str] = Field(
        default=None, alias="VocabularyFilterName"
    )
    language_model_name: Optional[str] = Field(default=None, alias="LanguageModelName")


class CallAnalyticsJobSummaryModel(BaseModel):
    call_analytics_job_name: Optional[str] = Field(
        default=None, alias="CallAnalyticsJobName"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    call_analytics_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="CallAnalyticsJobStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class ChannelDefinitionModel(BaseModel):
    channel_id: Optional[int] = Field(default=None, alias="ChannelId")
    participant_role: Optional[Literal["AGENT", "CUSTOMER"]] = Field(
        default=None, alias="ParticipantRole"
    )


class MediaModel(BaseModel):
    media_file_uri: Optional[str] = Field(default=None, alias="MediaFileUri")
    redacted_media_file_uri: Optional[str] = Field(
        default=None, alias="RedactedMediaFileUri"
    )


class TranscriptModel(BaseModel):
    transcript_file_uri: Optional[str] = Field(default=None, alias="TranscriptFileUri")
    redacted_transcript_file_uri: Optional[str] = Field(
        default=None, alias="RedactedTranscriptFileUri"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class InputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    tuning_data_s3_uri: Optional[str] = Field(default=None, alias="TuningDataS3Uri")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DeleteCallAnalyticsCategoryRequestModel(BaseModel):
    category_name: str = Field(alias="CategoryName")


class DeleteCallAnalyticsJobRequestModel(BaseModel):
    call_analytics_job_name: str = Field(alias="CallAnalyticsJobName")


class DeleteLanguageModelRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class DeleteMedicalTranscriptionJobRequestModel(BaseModel):
    medical_transcription_job_name: str = Field(alias="MedicalTranscriptionJobName")


class DeleteMedicalVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")


class DeleteTranscriptionJobRequestModel(BaseModel):
    transcription_job_name: str = Field(alias="TranscriptionJobName")


class DeleteVocabularyFilterRequestModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")


class DeleteVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")


class DescribeLanguageModelRequestModel(BaseModel):
    model_name: str = Field(alias="ModelName")


class GetCallAnalyticsCategoryRequestModel(BaseModel):
    category_name: str = Field(alias="CategoryName")


class GetCallAnalyticsJobRequestModel(BaseModel):
    call_analytics_job_name: str = Field(alias="CallAnalyticsJobName")


class GetMedicalTranscriptionJobRequestModel(BaseModel):
    medical_transcription_job_name: str = Field(alias="MedicalTranscriptionJobName")


class GetMedicalVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")


class GetTranscriptionJobRequestModel(BaseModel):
    transcription_job_name: str = Field(alias="TranscriptionJobName")


class GetVocabularyFilterRequestModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")


class GetVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")


class RelativeTimeRangeModel(BaseModel):
    start_percentage: Optional[int] = Field(default=None, alias="StartPercentage")
    end_percentage: Optional[int] = Field(default=None, alias="EndPercentage")
    first: Optional[int] = Field(default=None, alias="First")
    last: Optional[int] = Field(default=None, alias="Last")


class JobExecutionSettingsModel(BaseModel):
    allow_deferred_execution: Optional[bool] = Field(
        default=None, alias="AllowDeferredExecution"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")


class LanguageCodeItemModel(BaseModel):
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    duration_in_seconds: Optional[float] = Field(
        default=None, alias="DurationInSeconds"
    )


class ListCallAnalyticsCategoriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCallAnalyticsJobsRequestModel(BaseModel):
    status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]] = Field(
        default=None, alias="Status"
    )
    job_name_contains: Optional[str] = Field(default=None, alias="JobNameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLanguageModelsRequestModel(BaseModel):
    status_equals: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="StatusEquals"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMedicalTranscriptionJobsRequestModel(BaseModel):
    status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]] = Field(
        default=None, alias="Status"
    )
    job_name_contains: Optional[str] = Field(default=None, alias="JobNameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MedicalTranscriptionJobSummaryModel(BaseModel):
    medical_transcription_job_name: Optional[str] = Field(
        default=None, alias="MedicalTranscriptionJobName"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    transcription_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="TranscriptionJobStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    output_location_type: Optional[
        Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"]
    ] = Field(default=None, alias="OutputLocationType")
    specialty: Optional[Literal["PRIMARYCARE"]] = Field(default=None, alias="Specialty")
    content_identification_type: Optional[Literal["PHI"]] = Field(
        default=None, alias="ContentIdentificationType"
    )
    type: Optional[Literal["CONVERSATION", "DICTATION"]] = Field(
        default=None, alias="Type"
    )


class ListMedicalVocabulariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    state_equals: Optional[Literal["FAILED", "PENDING", "READY"]] = Field(
        default=None, alias="StateEquals"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")


class VocabularyInfoModel(BaseModel):
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    vocabulary_state: Optional[Literal["FAILED", "PENDING", "READY"]] = Field(
        default=None, alias="VocabularyState"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListTranscriptionJobsRequestModel(BaseModel):
    status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]] = Field(
        default=None, alias="Status"
    )
    job_name_contains: Optional[str] = Field(default=None, alias="JobNameContains")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListVocabulariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    state_equals: Optional[Literal["FAILED", "PENDING", "READY"]] = Field(
        default=None, alias="StateEquals"
    )
    name_contains: Optional[str] = Field(default=None, alias="NameContains")


class ListVocabularyFiltersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    name_contains: Optional[str] = Field(default=None, alias="NameContains")


class VocabularyFilterInfoModel(BaseModel):
    vocabulary_filter_name: Optional[str] = Field(
        default=None, alias="VocabularyFilterName"
    )
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class MedicalTranscriptModel(BaseModel):
    transcript_file_uri: Optional[str] = Field(default=None, alias="TranscriptFileUri")


class MedicalTranscriptionSettingModel(BaseModel):
    show_speaker_labels: Optional[bool] = Field(default=None, alias="ShowSpeakerLabels")
    max_speaker_labels: Optional[int] = Field(default=None, alias="MaxSpeakerLabels")
    channel_identification: Optional[bool] = Field(
        default=None, alias="ChannelIdentification"
    )
    show_alternatives: Optional[bool] = Field(default=None, alias="ShowAlternatives")
    max_alternatives: Optional[int] = Field(default=None, alias="MaxAlternatives")
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")


class ModelSettingsModel(BaseModel):
    language_model_name: Optional[str] = Field(default=None, alias="LanguageModelName")


class SettingsModel(BaseModel):
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    show_speaker_labels: Optional[bool] = Field(default=None, alias="ShowSpeakerLabels")
    max_speaker_labels: Optional[int] = Field(default=None, alias="MaxSpeakerLabels")
    channel_identification: Optional[bool] = Field(
        default=None, alias="ChannelIdentification"
    )
    show_alternatives: Optional[bool] = Field(default=None, alias="ShowAlternatives")
    max_alternatives: Optional[int] = Field(default=None, alias="MaxAlternatives")
    vocabulary_filter_name: Optional[str] = Field(
        default=None, alias="VocabularyFilterName"
    )
    vocabulary_filter_method: Optional[Literal["mask", "remove", "tag"]] = Field(
        default=None, alias="VocabularyFilterMethod"
    )


class SubtitlesModel(BaseModel):
    formats: Optional[Sequence[Literal["srt", "vtt"]]] = Field(
        default=None, alias="Formats"
    )
    output_start_index: Optional[int] = Field(default=None, alias="OutputStartIndex")


class SubtitlesOutputModel(BaseModel):
    formats: Optional[List[Literal["srt", "vtt"]]] = Field(
        default=None, alias="Formats"
    )
    subtitle_file_uris: Optional[List[str]] = Field(
        default=None, alias="SubtitleFileUris"
    )
    output_start_index: Optional[int] = Field(default=None, alias="OutputStartIndex")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateMedicalVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_file_uri: str = Field(alias="VocabularyFileUri")


class UpdateVocabularyFilterRequestModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")
    words: Optional[Sequence[str]] = Field(default=None, alias="Words")
    vocabulary_filter_file_uri: Optional[str] = Field(
        default=None, alias="VocabularyFilterFileUri"
    )


class UpdateVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    phrases: Optional[Sequence[str]] = Field(default=None, alias="Phrases")
    vocabulary_file_uri: Optional[str] = Field(default=None, alias="VocabularyFileUri")


class CallAnalyticsJobSettingsModel(BaseModel):
    vocabulary_name: Optional[str] = Field(default=None, alias="VocabularyName")
    vocabulary_filter_name: Optional[str] = Field(
        default=None, alias="VocabularyFilterName"
    )
    vocabulary_filter_method: Optional[Literal["mask", "remove", "tag"]] = Field(
        default=None, alias="VocabularyFilterMethod"
    )
    language_model_name: Optional[str] = Field(default=None, alias="LanguageModelName")
    content_redaction: Optional[ContentRedactionModel] = Field(
        default=None, alias="ContentRedaction"
    )
    language_options: Optional[
        List[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ]
        ]
    ] = Field(default=None, alias="LanguageOptions")
    language_id_settings: Optional[
        Dict[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ],
            LanguageIdSettingsModel,
        ]
    ] = Field(default=None, alias="LanguageIdSettings")


class CreateMedicalVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVocabularyFilterResponseModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMedicalVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    download_uri: str = Field(alias="DownloadUri")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVocabularyFilterResponseModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    download_uri: str = Field(alias="DownloadUri")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: str = Field(alias="FailureReason")
    download_uri: str = Field(alias="DownloadUri")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCallAnalyticsJobsResponseModel(BaseModel):
    status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"] = Field(
        alias="Status"
    )
    next_token: str = Field(alias="NextToken")
    call_analytics_job_summaries: List[CallAnalyticsJobSummaryModel] = Field(
        alias="CallAnalyticsJobSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMedicalVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVocabularyFilterResponseModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVocabularyResponseModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    vocabulary_state: Literal["FAILED", "PENDING", "READY"] = Field(
        alias="VocabularyState"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLanguageModelResponseModel(BaseModel):
    language_code: Literal[
        "de-DE", "en-AU", "en-GB", "en-US", "es-US", "hi-IN", "ja-JP"
    ] = Field(alias="LanguageCode")
    base_model_name: Literal["NarrowBand", "WideBand"] = Field(alias="BaseModelName")
    model_name: str = Field(alias="ModelName")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    model_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS"] = Field(
        alias="ModelStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LanguageModelModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    language_code: Optional[
        Literal["de-DE", "en-AU", "en-GB", "en-US", "es-US", "hi-IN", "ja-JP"]
    ] = Field(default=None, alias="LanguageCode")
    base_model_name: Optional[Literal["NarrowBand", "WideBand"]] = Field(
        default=None, alias="BaseModelName"
    )
    model_status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="ModelStatus"
    )
    upgrade_availability: Optional[bool] = Field(
        default=None, alias="UpgradeAvailability"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )


class CreateLanguageModelRequestModel(BaseModel):
    language_code: Literal[
        "de-DE", "en-AU", "en-GB", "en-US", "es-US", "hi-IN", "ja-JP"
    ] = Field(alias="LanguageCode")
    base_model_name: Literal["NarrowBand", "WideBand"] = Field(alias="BaseModelName")
    model_name: str = Field(alias="ModelName")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateMedicalVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    vocabulary_file_uri: str = Field(alias="VocabularyFileUri")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateVocabularyFilterRequestModel(BaseModel):
    vocabulary_filter_name: str = Field(alias="VocabularyFilterName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    words: Optional[Sequence[str]] = Field(default=None, alias="Words")
    vocabulary_filter_file_uri: Optional[str] = Field(
        default=None, alias="VocabularyFilterFileUri"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateVocabularyRequestModel(BaseModel):
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    phrases: Optional[Sequence[str]] = Field(default=None, alias="Phrases")
    vocabulary_file_uri: Optional[str] = Field(default=None, alias="VocabularyFileUri")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class InterruptionFilterModel(BaseModel):
    threshold: Optional[int] = Field(default=None, alias="Threshold")
    participant_role: Optional[Literal["AGENT", "CUSTOMER"]] = Field(
        default=None, alias="ParticipantRole"
    )
    absolute_time_range: Optional[AbsoluteTimeRangeModel] = Field(
        default=None, alias="AbsoluteTimeRange"
    )
    relative_time_range: Optional[RelativeTimeRangeModel] = Field(
        default=None, alias="RelativeTimeRange"
    )
    negate: Optional[bool] = Field(default=None, alias="Negate")


class NonTalkTimeFilterModel(BaseModel):
    threshold: Optional[int] = Field(default=None, alias="Threshold")
    absolute_time_range: Optional[AbsoluteTimeRangeModel] = Field(
        default=None, alias="AbsoluteTimeRange"
    )
    relative_time_range: Optional[RelativeTimeRangeModel] = Field(
        default=None, alias="RelativeTimeRange"
    )
    negate: Optional[bool] = Field(default=None, alias="Negate")


class SentimentFilterModel(BaseModel):
    sentiments: Sequence[Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]] = Field(
        alias="Sentiments"
    )
    absolute_time_range: Optional[AbsoluteTimeRangeModel] = Field(
        default=None, alias="AbsoluteTimeRange"
    )
    relative_time_range: Optional[RelativeTimeRangeModel] = Field(
        default=None, alias="RelativeTimeRange"
    )
    participant_role: Optional[Literal["AGENT", "CUSTOMER"]] = Field(
        default=None, alias="ParticipantRole"
    )
    negate: Optional[bool] = Field(default=None, alias="Negate")


class TranscriptFilterModel(BaseModel):
    transcript_filter_type: Literal["EXACT"] = Field(alias="TranscriptFilterType")
    targets: Sequence[str] = Field(alias="Targets")
    absolute_time_range: Optional[AbsoluteTimeRangeModel] = Field(
        default=None, alias="AbsoluteTimeRange"
    )
    relative_time_range: Optional[RelativeTimeRangeModel] = Field(
        default=None, alias="RelativeTimeRange"
    )
    participant_role: Optional[Literal["AGENT", "CUSTOMER"]] = Field(
        default=None, alias="ParticipantRole"
    )
    negate: Optional[bool] = Field(default=None, alias="Negate")


class ListMedicalTranscriptionJobsResponseModel(BaseModel):
    status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"] = Field(
        alias="Status"
    )
    next_token: str = Field(alias="NextToken")
    medical_transcription_job_summaries: List[
        MedicalTranscriptionJobSummaryModel
    ] = Field(alias="MedicalTranscriptionJobSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMedicalVocabulariesResponseModel(BaseModel):
    status: Literal["FAILED", "PENDING", "READY"] = Field(alias="Status")
    next_token: str = Field(alias="NextToken")
    vocabularies: List[VocabularyInfoModel] = Field(alias="Vocabularies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVocabulariesResponseModel(BaseModel):
    status: Literal["FAILED", "PENDING", "READY"] = Field(alias="Status")
    next_token: str = Field(alias="NextToken")
    vocabularies: List[VocabularyInfoModel] = Field(alias="Vocabularies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVocabularyFiltersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    vocabulary_filters: List[VocabularyFilterInfoModel] = Field(
        alias="VocabularyFilters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MedicalTranscriptionJobModel(BaseModel):
    medical_transcription_job_name: Optional[str] = Field(
        default=None, alias="MedicalTranscriptionJobName"
    )
    transcription_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="TranscriptionJobStatus")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    media_sample_rate_hertz: Optional[int] = Field(
        default=None, alias="MediaSampleRateHertz"
    )
    media_format: Optional[
        Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
    ] = Field(default=None, alias="MediaFormat")
    media: Optional[MediaModel] = Field(default=None, alias="Media")
    transcript: Optional[MedicalTranscriptModel] = Field(
        default=None, alias="Transcript"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    settings: Optional[MedicalTranscriptionSettingModel] = Field(
        default=None, alias="Settings"
    )
    content_identification_type: Optional[Literal["PHI"]] = Field(
        default=None, alias="ContentIdentificationType"
    )
    specialty: Optional[Literal["PRIMARYCARE"]] = Field(default=None, alias="Specialty")
    type: Optional[Literal["CONVERSATION", "DICTATION"]] = Field(
        default=None, alias="Type"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class StartMedicalTranscriptionJobRequestModel(BaseModel):
    medical_transcription_job_name: str = Field(alias="MedicalTranscriptionJobName")
    language_code: Literal[
        "af-ZA",
        "ar-AE",
        "ar-SA",
        "da-DK",
        "de-CH",
        "de-DE",
        "en-AB",
        "en-AU",
        "en-GB",
        "en-IE",
        "en-IN",
        "en-NZ",
        "en-US",
        "en-WL",
        "en-ZA",
        "es-ES",
        "es-US",
        "fa-IR",
        "fr-CA",
        "fr-FR",
        "he-IL",
        "hi-IN",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "ms-MY",
        "nl-NL",
        "pt-BR",
        "pt-PT",
        "ru-RU",
        "sv-SE",
        "ta-IN",
        "te-IN",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ] = Field(alias="LanguageCode")
    media: MediaModel = Field(alias="Media")
    output_bucket_name: str = Field(alias="OutputBucketName")
    specialty: Literal["PRIMARYCARE"] = Field(alias="Specialty")
    type: Literal["CONVERSATION", "DICTATION"] = Field(alias="Type")
    media_sample_rate_hertz: Optional[int] = Field(
        default=None, alias="MediaSampleRateHertz"
    )
    media_format: Optional[
        Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
    ] = Field(default=None, alias="MediaFormat")
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="OutputEncryptionKMSKeyId"
    )
    kms_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="KMSEncryptionContext"
    )
    settings: Optional[MedicalTranscriptionSettingModel] = Field(
        default=None, alias="Settings"
    )
    content_identification_type: Optional[Literal["PHI"]] = Field(
        default=None, alias="ContentIdentificationType"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TranscriptionJobSummaryModel(BaseModel):
    transcription_job_name: Optional[str] = Field(
        default=None, alias="TranscriptionJobName"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    transcription_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="TranscriptionJobStatus")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    output_location_type: Optional[
        Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"]
    ] = Field(default=None, alias="OutputLocationType")
    content_redaction: Optional[ContentRedactionModel] = Field(
        default=None, alias="ContentRedaction"
    )
    model_settings: Optional[ModelSettingsModel] = Field(
        default=None, alias="ModelSettings"
    )
    identify_language: Optional[bool] = Field(default=None, alias="IdentifyLanguage")
    identify_multiple_languages: Optional[bool] = Field(
        default=None, alias="IdentifyMultipleLanguages"
    )
    identified_language_score: Optional[float] = Field(
        default=None, alias="IdentifiedLanguageScore"
    )
    language_codes: Optional[List[LanguageCodeItemModel]] = Field(
        default=None, alias="LanguageCodes"
    )


class StartTranscriptionJobRequestModel(BaseModel):
    transcription_job_name: str = Field(alias="TranscriptionJobName")
    media: MediaModel = Field(alias="Media")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    media_sample_rate_hertz: Optional[int] = Field(
        default=None, alias="MediaSampleRateHertz"
    )
    media_format: Optional[
        Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
    ] = Field(default=None, alias="MediaFormat")
    output_bucket_name: Optional[str] = Field(default=None, alias="OutputBucketName")
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="OutputEncryptionKMSKeyId"
    )
    kms_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="KMSEncryptionContext"
    )
    settings: Optional[SettingsModel] = Field(default=None, alias="Settings")
    model_settings: Optional[ModelSettingsModel] = Field(
        default=None, alias="ModelSettings"
    )
    job_execution_settings: Optional[JobExecutionSettingsModel] = Field(
        default=None, alias="JobExecutionSettings"
    )
    content_redaction: Optional[ContentRedactionModel] = Field(
        default=None, alias="ContentRedaction"
    )
    identify_language: Optional[bool] = Field(default=None, alias="IdentifyLanguage")
    identify_multiple_languages: Optional[bool] = Field(
        default=None, alias="IdentifyMultipleLanguages"
    )
    language_options: Optional[
        Sequence[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ]
        ]
    ] = Field(default=None, alias="LanguageOptions")
    subtitles: Optional[SubtitlesModel] = Field(default=None, alias="Subtitles")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    language_id_settings: Optional[
        Mapping[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ],
            LanguageIdSettingsModel,
        ]
    ] = Field(default=None, alias="LanguageIdSettings")


class TranscriptionJobModel(BaseModel):
    transcription_job_name: Optional[str] = Field(
        default=None, alias="TranscriptionJobName"
    )
    transcription_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="TranscriptionJobStatus")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    media_sample_rate_hertz: Optional[int] = Field(
        default=None, alias="MediaSampleRateHertz"
    )
    media_format: Optional[
        Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
    ] = Field(default=None, alias="MediaFormat")
    media: Optional[MediaModel] = Field(default=None, alias="Media")
    transcript: Optional[TranscriptModel] = Field(default=None, alias="Transcript")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    settings: Optional[SettingsModel] = Field(default=None, alias="Settings")
    model_settings: Optional[ModelSettingsModel] = Field(
        default=None, alias="ModelSettings"
    )
    job_execution_settings: Optional[JobExecutionSettingsModel] = Field(
        default=None, alias="JobExecutionSettings"
    )
    content_redaction: Optional[ContentRedactionModel] = Field(
        default=None, alias="ContentRedaction"
    )
    identify_language: Optional[bool] = Field(default=None, alias="IdentifyLanguage")
    identify_multiple_languages: Optional[bool] = Field(
        default=None, alias="IdentifyMultipleLanguages"
    )
    language_options: Optional[
        List[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ]
        ]
    ] = Field(default=None, alias="LanguageOptions")
    identified_language_score: Optional[float] = Field(
        default=None, alias="IdentifiedLanguageScore"
    )
    language_codes: Optional[List[LanguageCodeItemModel]] = Field(
        default=None, alias="LanguageCodes"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    subtitles: Optional[SubtitlesOutputModel] = Field(default=None, alias="Subtitles")
    language_id_settings: Optional[
        Dict[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-WL",
                "en-ZA",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "sv-SE",
                "ta-IN",
                "te-IN",
                "th-TH",
                "tr-TR",
                "vi-VN",
                "zh-CN",
                "zh-TW",
            ],
            LanguageIdSettingsModel,
        ]
    ] = Field(default=None, alias="LanguageIdSettings")


class CallAnalyticsJobModel(BaseModel):
    call_analytics_job_name: Optional[str] = Field(
        default=None, alias="CallAnalyticsJobName"
    )
    call_analytics_job_status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
    ] = Field(default=None, alias="CallAnalyticsJobStatus")
    language_code: Optional[
        Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-WL",
            "en-ZA",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "sv-SE",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "vi-VN",
            "zh-CN",
            "zh-TW",
        ]
    ] = Field(default=None, alias="LanguageCode")
    media_sample_rate_hertz: Optional[int] = Field(
        default=None, alias="MediaSampleRateHertz"
    )
    media_format: Optional[
        Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
    ] = Field(default=None, alias="MediaFormat")
    media: Optional[MediaModel] = Field(default=None, alias="Media")
    transcript: Optional[TranscriptModel] = Field(default=None, alias="Transcript")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    completion_time: Optional[datetime] = Field(default=None, alias="CompletionTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    identified_language_score: Optional[float] = Field(
        default=None, alias="IdentifiedLanguageScore"
    )
    settings: Optional[CallAnalyticsJobSettingsModel] = Field(
        default=None, alias="Settings"
    )
    channel_definitions: Optional[List[ChannelDefinitionModel]] = Field(
        default=None, alias="ChannelDefinitions"
    )


class StartCallAnalyticsJobRequestModel(BaseModel):
    call_analytics_job_name: str = Field(alias="CallAnalyticsJobName")
    media: MediaModel = Field(alias="Media")
    output_location: Optional[str] = Field(default=None, alias="OutputLocation")
    output_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="OutputEncryptionKMSKeyId"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    settings: Optional[CallAnalyticsJobSettingsModel] = Field(
        default=None, alias="Settings"
    )
    channel_definitions: Optional[Sequence[ChannelDefinitionModel]] = Field(
        default=None, alias="ChannelDefinitions"
    )


class DescribeLanguageModelResponseModel(BaseModel):
    language_model: LanguageModelModel = Field(alias="LanguageModel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLanguageModelsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    models: List[LanguageModelModel] = Field(alias="Models")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleModel(BaseModel):
    non_talk_time_filter: Optional[NonTalkTimeFilterModel] = Field(
        default=None, alias="NonTalkTimeFilter"
    )
    interruption_filter: Optional[InterruptionFilterModel] = Field(
        default=None, alias="InterruptionFilter"
    )
    transcript_filter: Optional[TranscriptFilterModel] = Field(
        default=None, alias="TranscriptFilter"
    )
    sentiment_filter: Optional[SentimentFilterModel] = Field(
        default=None, alias="SentimentFilter"
    )


class GetMedicalTranscriptionJobResponseModel(BaseModel):
    medical_transcription_job: MedicalTranscriptionJobModel = Field(
        alias="MedicalTranscriptionJob"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMedicalTranscriptionJobResponseModel(BaseModel):
    medical_transcription_job: MedicalTranscriptionJobModel = Field(
        alias="MedicalTranscriptionJob"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTranscriptionJobsResponseModel(BaseModel):
    status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"] = Field(
        alias="Status"
    )
    next_token: str = Field(alias="NextToken")
    transcription_job_summaries: List[TranscriptionJobSummaryModel] = Field(
        alias="TranscriptionJobSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTranscriptionJobResponseModel(BaseModel):
    transcription_job: TranscriptionJobModel = Field(alias="TranscriptionJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTranscriptionJobResponseModel(BaseModel):
    transcription_job: TranscriptionJobModel = Field(alias="TranscriptionJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCallAnalyticsJobResponseModel(BaseModel):
    call_analytics_job: CallAnalyticsJobModel = Field(alias="CallAnalyticsJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCallAnalyticsJobResponseModel(BaseModel):
    call_analytics_job: CallAnalyticsJobModel = Field(alias="CallAnalyticsJob")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CategoryPropertiesModel(BaseModel):
    category_name: Optional[str] = Field(default=None, alias="CategoryName")
    rules: Optional[List[RuleModel]] = Field(default=None, alias="Rules")
    create_time: Optional[datetime] = Field(default=None, alias="CreateTime")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    input_type: Optional[Literal["POST_CALL", "REAL_TIME"]] = Field(
        default=None, alias="InputType"
    )


class CreateCallAnalyticsCategoryRequestModel(BaseModel):
    category_name: str = Field(alias="CategoryName")
    rules: Sequence[RuleModel] = Field(alias="Rules")
    input_type: Optional[Literal["POST_CALL", "REAL_TIME"]] = Field(
        default=None, alias="InputType"
    )


class UpdateCallAnalyticsCategoryRequestModel(BaseModel):
    category_name: str = Field(alias="CategoryName")
    rules: Sequence[RuleModel] = Field(alias="Rules")
    input_type: Optional[Literal["POST_CALL", "REAL_TIME"]] = Field(
        default=None, alias="InputType"
    )


class CreateCallAnalyticsCategoryResponseModel(BaseModel):
    category_properties: CategoryPropertiesModel = Field(alias="CategoryProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCallAnalyticsCategoryResponseModel(BaseModel):
    category_properties: CategoryPropertiesModel = Field(alias="CategoryProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCallAnalyticsCategoriesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    categories: List[CategoryPropertiesModel] = Field(alias="Categories")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCallAnalyticsCategoryResponseModel(BaseModel):
    category_properties: CategoryPropertiesModel = Field(alias="CategoryProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
