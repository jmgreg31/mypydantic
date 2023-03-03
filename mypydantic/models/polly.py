# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Type

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteLexiconInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeVoicesInputRequestModel(BaseModel):
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="Engine"
    )
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    include_additional_language_codes: Optional[bool] = Field(
        default=None, alias="IncludeAdditionalLanguageCodes"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class VoiceModel(BaseModel):
    gender: Optional[Literal["Female", "Male"]] = Field(default=None, alias="Gender")
    id: Optional[
        Literal[
            "Aditi",
            "Adriano",
            "Amy",
            "Andres",
            "Aria",
            "Arlet",
            "Arthur",
            "Astrid",
            "Ayanda",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Daniel",
            "Dora",
            "Elin",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Gabrielle",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hala",
            "Hannah",
            "Hans",
            "Hiujin",
            "Ida",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Kajal",
            "Karl",
            "Kazuha",
            "Kendra",
            "Kevin",
            "Kimberly",
            "Laura",
            "Lea",
            "Liam",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Ola",
            "Olivia",
            "Pedro",
            "Penelope",
            "Raveena",
            "Remi",
            "Ricardo",
            "Ruben",
            "Russell",
            "Ruth",
            "Salli",
            "Seoyeon",
            "Sergio",
            "Stephen",
            "Suvi",
            "Takumi",
            "Tatyana",
            "Thiago",
            "Tomoko",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ]
    ] = Field(default=None, alias="Id")
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    language_name: Optional[str] = Field(default=None, alias="LanguageName")
    name: Optional[str] = Field(default=None, alias="Name")
    additional_language_codes: Optional[
        List[
            Literal[
                "ar-AE",
                "arb",
                "ca-ES",
                "cmn-CN",
                "cy-GB",
                "da-DK",
                "de-AT",
                "de-DE",
                "en-AU",
                "en-GB",
                "en-GB-WLS",
                "en-IN",
                "en-NZ",
                "en-US",
                "en-ZA",
                "es-ES",
                "es-MX",
                "es-US",
                "fi-FI",
                "fr-CA",
                "fr-FR",
                "hi-IN",
                "is-IS",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "nb-NO",
                "nl-NL",
                "pl-PL",
                "pt-BR",
                "pt-PT",
                "ro-RO",
                "ru-RU",
                "sv-SE",
                "tr-TR",
                "yue-CN",
            ]
        ]
    ] = Field(default=None, alias="AdditionalLanguageCodes")
    supported_engines: Optional[List[Literal["neural", "standard"]]] = Field(
        default=None, alias="SupportedEngines"
    )


class GetLexiconInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class LexiconAttributesModel(BaseModel):
    alphabet: Optional[str] = Field(default=None, alias="Alphabet")
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    lexicon_arn: Optional[str] = Field(default=None, alias="LexiconArn")
    lexemes_count: Optional[int] = Field(default=None, alias="LexemesCount")
    size: Optional[int] = Field(default=None, alias="Size")


class LexiconModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="Content")
    name: Optional[str] = Field(default=None, alias="Name")


class GetSpeechSynthesisTaskInputRequestModel(BaseModel):
    task_id: str = Field(alias="TaskId")


class SynthesisTaskModel(BaseModel):
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="Engine"
    )
    task_id: Optional[str] = Field(default=None, alias="TaskId")
    task_status: Optional[
        Literal["completed", "failed", "inProgress", "scheduled"]
    ] = Field(default=None, alias="TaskStatus")
    task_status_reason: Optional[str] = Field(default=None, alias="TaskStatusReason")
    output_uri: Optional[str] = Field(default=None, alias="OutputUri")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    request_characters: Optional[int] = Field(default=None, alias="RequestCharacters")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    lexicon_names: Optional[List[str]] = Field(default=None, alias="LexiconNames")
    output_format: Optional[Literal["json", "mp3", "ogg_vorbis", "pcm"]] = Field(
        default=None, alias="OutputFormat"
    )
    sample_rate: Optional[str] = Field(default=None, alias="SampleRate")
    speech_mark_types: Optional[
        List[Literal["sentence", "ssml", "viseme", "word"]]
    ] = Field(default=None, alias="SpeechMarkTypes")
    text_type: Optional[Literal["ssml", "text"]] = Field(default=None, alias="TextType")
    voice_id: Optional[
        Literal[
            "Aditi",
            "Adriano",
            "Amy",
            "Andres",
            "Aria",
            "Arlet",
            "Arthur",
            "Astrid",
            "Ayanda",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Daniel",
            "Dora",
            "Elin",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Gabrielle",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hala",
            "Hannah",
            "Hans",
            "Hiujin",
            "Ida",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Kajal",
            "Karl",
            "Kazuha",
            "Kendra",
            "Kevin",
            "Kimberly",
            "Laura",
            "Lea",
            "Liam",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Ola",
            "Olivia",
            "Pedro",
            "Penelope",
            "Raveena",
            "Remi",
            "Ricardo",
            "Ruben",
            "Russell",
            "Ruth",
            "Salli",
            "Seoyeon",
            "Sergio",
            "Stephen",
            "Suvi",
            "Takumi",
            "Tatyana",
            "Thiago",
            "Tomoko",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ]
    ] = Field(default=None, alias="VoiceId")
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")


class ListLexiconsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSpeechSynthesisTasksInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    status: Optional[Literal["completed", "failed", "inProgress", "scheduled"]] = Field(
        default=None, alias="Status"
    )


class PutLexiconInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    content: str = Field(alias="Content")


class StartSpeechSynthesisTaskInputRequestModel(BaseModel):
    output_format: Literal["json", "mp3", "ogg_vorbis", "pcm"] = Field(
        alias="OutputFormat"
    )
    output_s3_bucket_name: str = Field(alias="OutputS3BucketName")
    text: str = Field(alias="Text")
    voice_id: Literal[
        "Aditi",
        "Adriano",
        "Amy",
        "Andres",
        "Aria",
        "Arlet",
        "Arthur",
        "Astrid",
        "Ayanda",
        "Bianca",
        "Brian",
        "Camila",
        "Carla",
        "Carmen",
        "Celine",
        "Chantal",
        "Conchita",
        "Cristiano",
        "Daniel",
        "Dora",
        "Elin",
        "Emma",
        "Enrique",
        "Ewa",
        "Filiz",
        "Gabrielle",
        "Geraint",
        "Giorgio",
        "Gwyneth",
        "Hala",
        "Hannah",
        "Hans",
        "Hiujin",
        "Ida",
        "Ines",
        "Ivy",
        "Jacek",
        "Jan",
        "Joanna",
        "Joey",
        "Justin",
        "Kajal",
        "Karl",
        "Kazuha",
        "Kendra",
        "Kevin",
        "Kimberly",
        "Laura",
        "Lea",
        "Liam",
        "Liv",
        "Lotte",
        "Lucia",
        "Lupe",
        "Mads",
        "Maja",
        "Marlene",
        "Mathieu",
        "Matthew",
        "Maxim",
        "Mia",
        "Miguel",
        "Mizuki",
        "Naja",
        "Nicole",
        "Ola",
        "Olivia",
        "Pedro",
        "Penelope",
        "Raveena",
        "Remi",
        "Ricardo",
        "Ruben",
        "Russell",
        "Ruth",
        "Salli",
        "Seoyeon",
        "Sergio",
        "Stephen",
        "Suvi",
        "Takumi",
        "Tatyana",
        "Thiago",
        "Tomoko",
        "Vicki",
        "Vitoria",
        "Zeina",
        "Zhiyu",
    ] = Field(alias="VoiceId")
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="Engine"
    )
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    lexicon_names: Optional[Sequence[str]] = Field(default=None, alias="LexiconNames")
    output_s3_key_prefix: Optional[str] = Field(default=None, alias="OutputS3KeyPrefix")
    sample_rate: Optional[str] = Field(default=None, alias="SampleRate")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    speech_mark_types: Optional[
        Sequence[Literal["sentence", "ssml", "viseme", "word"]]
    ] = Field(default=None, alias="SpeechMarkTypes")
    text_type: Optional[Literal["ssml", "text"]] = Field(default=None, alias="TextType")


class SynthesizeSpeechInputRequestModel(BaseModel):
    output_format: Literal["json", "mp3", "ogg_vorbis", "pcm"] = Field(
        alias="OutputFormat"
    )
    text: str = Field(alias="Text")
    voice_id: Literal[
        "Aditi",
        "Adriano",
        "Amy",
        "Andres",
        "Aria",
        "Arlet",
        "Arthur",
        "Astrid",
        "Ayanda",
        "Bianca",
        "Brian",
        "Camila",
        "Carla",
        "Carmen",
        "Celine",
        "Chantal",
        "Conchita",
        "Cristiano",
        "Daniel",
        "Dora",
        "Elin",
        "Emma",
        "Enrique",
        "Ewa",
        "Filiz",
        "Gabrielle",
        "Geraint",
        "Giorgio",
        "Gwyneth",
        "Hala",
        "Hannah",
        "Hans",
        "Hiujin",
        "Ida",
        "Ines",
        "Ivy",
        "Jacek",
        "Jan",
        "Joanna",
        "Joey",
        "Justin",
        "Kajal",
        "Karl",
        "Kazuha",
        "Kendra",
        "Kevin",
        "Kimberly",
        "Laura",
        "Lea",
        "Liam",
        "Liv",
        "Lotte",
        "Lucia",
        "Lupe",
        "Mads",
        "Maja",
        "Marlene",
        "Mathieu",
        "Matthew",
        "Maxim",
        "Mia",
        "Miguel",
        "Mizuki",
        "Naja",
        "Nicole",
        "Ola",
        "Olivia",
        "Pedro",
        "Penelope",
        "Raveena",
        "Remi",
        "Ricardo",
        "Ruben",
        "Russell",
        "Ruth",
        "Salli",
        "Seoyeon",
        "Sergio",
        "Stephen",
        "Suvi",
        "Takumi",
        "Tatyana",
        "Thiago",
        "Tomoko",
        "Vicki",
        "Vitoria",
        "Zeina",
        "Zhiyu",
    ] = Field(alias="VoiceId")
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="Engine"
    )
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    lexicon_names: Optional[Sequence[str]] = Field(default=None, alias="LexiconNames")
    sample_rate: Optional[str] = Field(default=None, alias="SampleRate")
    speech_mark_types: Optional[
        Sequence[Literal["sentence", "ssml", "viseme", "word"]]
    ] = Field(default=None, alias="SpeechMarkTypes")
    text_type: Optional[Literal["ssml", "text"]] = Field(default=None, alias="TextType")


class DescribeVoicesInputDescribeVoicesPaginateModel(BaseModel):
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="Engine"
    )
    language_code: Optional[
        Literal[
            "ar-AE",
            "arb",
            "ca-ES",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-NZ",
            "en-US",
            "en-ZA",
            "es-ES",
            "es-MX",
            "es-US",
            "fi-FI",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
            "yue-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    include_additional_language_codes: Optional[bool] = Field(
        default=None, alias="IncludeAdditionalLanguageCodes"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLexiconsInputListLexiconsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateModel(BaseModel):
    status: Optional[Literal["completed", "failed", "inProgress", "scheduled"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SynthesizeSpeechOutputModel(BaseModel):
    audio_stream: Type[StreamingBody] = Field(alias="AudioStream")
    content_type: str = Field(alias="ContentType")
    request_characters: int = Field(alias="RequestCharacters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVoicesOutputModel(BaseModel):
    voices: List[VoiceModel] = Field(alias="Voices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LexiconDescriptionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    attributes: Optional[LexiconAttributesModel] = Field(
        default=None, alias="Attributes"
    )


class GetLexiconOutputModel(BaseModel):
    lexicon: LexiconModel = Field(alias="Lexicon")
    lexicon_attributes: LexiconAttributesModel = Field(alias="LexiconAttributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSpeechSynthesisTaskOutputModel(BaseModel):
    synthesis_task: SynthesisTaskModel = Field(alias="SynthesisTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSpeechSynthesisTasksOutputModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    synthesis_tasks: List[SynthesisTaskModel] = Field(alias="SynthesisTasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSpeechSynthesisTaskOutputModel(BaseModel):
    synthesis_task: SynthesisTaskModel = Field(alias="SynthesisTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLexiconsOutputModel(BaseModel):
    lexicons: List[LexiconDescriptionModel] = Field(alias="Lexicons")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
