# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BotChannelAssociationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    bot_alias: Optional[str] = Field(default=None, alias="botAlias")
    bot_name: Optional[str] = Field(default=None, alias="botName")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    type: Optional[Literal["Facebook", "Kik", "Slack", "Twilio-Sms"]] = Field(
        default=None, alias="type"
    )
    bot_configuration: Optional[Dict[str, str]] = Field(
        default=None, alias="botConfiguration"
    )
    status: Optional[Literal["CREATED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="status"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class BotMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[
        Literal["BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"]
    ] = Field(default=None, alias="status")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    version: Optional[str] = Field(default=None, alias="version")


class BuiltinIntentMetadataModel(BaseModel):
    signature: Optional[str] = Field(default=None, alias="signature")
    supported_locales: Optional[
        List[
            Literal[
                "de-DE",
                "en-AU",
                "en-GB",
                "en-IN",
                "en-US",
                "es-419",
                "es-ES",
                "es-US",
                "fr-CA",
                "fr-FR",
                "it-IT",
                "ja-JP",
                "ko-KR",
            ]
        ]
    ] = Field(default=None, alias="supportedLocales")


class BuiltinIntentSlotModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class BuiltinSlotTypeMetadataModel(BaseModel):
    signature: Optional[str] = Field(default=None, alias="signature")
    supported_locales: Optional[
        List[
            Literal[
                "de-DE",
                "en-AU",
                "en-GB",
                "en-IN",
                "en-US",
                "es-419",
                "es-ES",
                "es-US",
                "fr-CA",
                "fr-FR",
                "it-IT",
                "ja-JP",
                "ko-KR",
            ]
        ]
    ] = Field(default=None, alias="supportedLocales")


class CodeHookModel(BaseModel):
    uri: str = Field(alias="uri")
    message_version: str = Field(alias="messageVersion")


class LogSettingsRequestModel(BaseModel):
    log_type: Literal["AUDIO", "TEXT"] = Field(alias="logType")
    destination: Literal["CLOUDWATCH_LOGS", "S3"] = Field(alias="destination")
    resource_arn: str = Field(alias="resourceArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class LogSettingsResponseModel(BaseModel):
    log_type: Optional[Literal["AUDIO", "TEXT"]] = Field(default=None, alias="logType")
    destination: Optional[Literal["CLOUDWATCH_LOGS", "S3"]] = Field(
        default=None, alias="destination"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    resource_prefix: Optional[str] = Field(default=None, alias="resourcePrefix")


class CreateBotVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    checksum: Optional[str] = Field(default=None, alias="checksum")


class IntentModel(BaseModel):
    intent_name: str = Field(alias="intentName")
    intent_version: str = Field(alias="intentVersion")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateIntentVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    checksum: Optional[str] = Field(default=None, alias="checksum")


class InputContextModel(BaseModel):
    name: str = Field(alias="name")


class KendraConfigurationModel(BaseModel):
    kendra_index: str = Field(alias="kendraIndex")
    role: str = Field(alias="role")
    query_filter_string: Optional[str] = Field(default=None, alias="queryFilterString")


class OutputContextModel(BaseModel):
    name: str = Field(alias="name")
    time_to_live_in_seconds: int = Field(alias="timeToLiveInSeconds")
    turns_to_live: int = Field(alias="turnsToLive")


class CreateSlotTypeVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    checksum: Optional[str] = Field(default=None, alias="checksum")


class EnumerationValueModel(BaseModel):
    value: str = Field(alias="value")
    synonyms: Optional[List[str]] = Field(default=None, alias="synonyms")


class DeleteBotAliasRequestModel(BaseModel):
    name: str = Field(alias="name")
    bot_name: str = Field(alias="botName")


class DeleteBotChannelAssociationRequestModel(BaseModel):
    name: str = Field(alias="name")
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")


class DeleteBotRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteBotVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class DeleteIntentRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteIntentVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class DeleteSlotTypeRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteSlotTypeVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class DeleteUtterancesRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    user_id: str = Field(alias="userId")


class GetBotAliasRequestModel(BaseModel):
    name: str = Field(alias="name")
    bot_name: str = Field(alias="botName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetBotAliasesRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")


class GetBotChannelAssociationRequestModel(BaseModel):
    name: str = Field(alias="name")
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")


class GetBotChannelAssociationsRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")


class GetBotRequestModel(BaseModel):
    name: str = Field(alias="name")
    version_or_alias: str = Field(alias="versionOrAlias")


class GetBotVersionsRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetBotsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")


class GetBuiltinIntentRequestModel(BaseModel):
    signature: str = Field(alias="signature")


class GetBuiltinIntentsRequestModel(BaseModel):
    locale: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(default=None, alias="locale")
    signature_contains: Optional[str] = Field(default=None, alias="signatureContains")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetBuiltinSlotTypesRequestModel(BaseModel):
    locale: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(default=None, alias="locale")
    signature_contains: Optional[str] = Field(default=None, alias="signatureContains")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetExportRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    resource_type: Literal["BOT", "INTENT", "SLOT_TYPE"] = Field(alias="resourceType")
    export_type: Literal["ALEXA_SKILLS_KIT", "LEX"] = Field(alias="exportType")


class GetImportRequestModel(BaseModel):
    import_id: str = Field(alias="importId")


class GetIntentRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class GetIntentVersionsRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class IntentMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    version: Optional[str] = Field(default=None, alias="version")


class GetIntentsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")


class GetMigrationRequestModel(BaseModel):
    migration_id: str = Field(alias="migrationId")


class MigrationAlertModel(BaseModel):
    type: Optional[Literal["ERROR", "WARN"]] = Field(default=None, alias="type")
    message: Optional[str] = Field(default=None, alias="message")
    details: Optional[List[str]] = Field(default=None, alias="details")
    reference_urls: Optional[List[str]] = Field(default=None, alias="referenceURLs")


class GetMigrationsRequestModel(BaseModel):
    sort_by_attribute: Optional[Literal["MIGRATION_DATE_TIME", "V1_BOT_NAME"]] = Field(
        default=None, alias="sortByAttribute"
    )
    sort_by_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="sortByOrder"
    )
    v1_bot_name_contains: Optional[str] = Field(default=None, alias="v1BotNameContains")
    migration_status_equals: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="migrationStatusEquals")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MigrationSummaryModel(BaseModel):
    migration_id: Optional[str] = Field(default=None, alias="migrationId")
    v1_bot_name: Optional[str] = Field(default=None, alias="v1BotName")
    v1_bot_version: Optional[str] = Field(default=None, alias="v1BotVersion")
    v1_bot_locale: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(default=None, alias="v1BotLocale")
    v2_bot_id: Optional[str] = Field(default=None, alias="v2BotId")
    v2_bot_role: Optional[str] = Field(default=None, alias="v2BotRole")
    migration_status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="migrationStatus"
    )
    migration_strategy: Optional[Literal["CREATE_NEW", "UPDATE_EXISTING"]] = Field(
        default=None, alias="migrationStrategy"
    )
    migration_timestamp: Optional[datetime] = Field(
        default=None, alias="migrationTimestamp"
    )


class GetSlotTypeRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")


class GetSlotTypeVersionsRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SlotTypeMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    version: Optional[str] = Field(default=None, alias="version")


class GetSlotTypesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")


class GetUtterancesViewRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_versions: Sequence[str] = Field(alias="botVersions")
    status_type: Literal["Detected", "Missed"] = Field(alias="statusType")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class MessageModel(BaseModel):
    content_type: Literal["CustomPayload", "PlainText", "SSML"] = Field(
        alias="contentType"
    )
    content: str = Field(alias="content")
    group_number: Optional[int] = Field(default=None, alias="groupNumber")


class SlotDefaultValueModel(BaseModel):
    default_value: str = Field(alias="defaultValue")


class SlotTypeRegexConfigurationModel(BaseModel):
    pattern: str = Field(alias="pattern")


class StartMigrationRequestModel(BaseModel):
    v1_bot_name: str = Field(alias="v1BotName")
    v1_bot_version: str = Field(alias="v1BotVersion")
    v2_bot_name: str = Field(alias="v2BotName")
    v2_bot_role: str = Field(alias="v2BotRole")
    migration_strategy: Literal["CREATE_NEW", "UPDATE_EXISTING"] = Field(
        alias="migrationStrategy"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UtteranceDataModel(BaseModel):
    utterance_string: Optional[str] = Field(default=None, alias="utteranceString")
    count: Optional[int] = Field(default=None, alias="count")
    distinct_users: Optional[int] = Field(default=None, alias="distinctUsers")
    first_uttered_date: Optional[datetime] = Field(
        default=None, alias="firstUtteredDate"
    )
    last_uttered_date: Optional[datetime] = Field(default=None, alias="lastUtteredDate")


class FulfillmentActivityModel(BaseModel):
    type: Literal["CodeHook", "ReturnIntent"] = Field(alias="type")
    code_hook: Optional[CodeHookModel] = Field(default=None, alias="codeHook")


class ConversationLogsRequestModel(BaseModel):
    log_settings: Sequence[LogSettingsRequestModel] = Field(alias="logSettings")
    iam_role_arn: str = Field(alias="iamRoleArn")


class ConversationLogsResponseModel(BaseModel):
    log_settings: Optional[List[LogSettingsResponseModel]] = Field(
        default=None, alias="logSettings"
    )
    iam_role_arn: Optional[str] = Field(default=None, alias="iamRoleArn")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotChannelAssociationResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    bot_alias: str = Field(alias="botAlias")
    bot_name: str = Field(alias="botName")
    created_date: datetime = Field(alias="createdDate")
    type: Literal["Facebook", "Kik", "Slack", "Twilio-Sms"] = Field(alias="type")
    bot_configuration: Dict[str, str] = Field(alias="botConfiguration")
    status: Literal["CREATED", "FAILED", "IN_PROGRESS"] = Field(alias="status")
    failure_reason: str = Field(alias="failureReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotChannelAssociationsResponseModel(BaseModel):
    bot_channel_associations: List[BotChannelAssociationModel] = Field(
        alias="botChannelAssociations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotVersionsResponseModel(BaseModel):
    bots: List[BotMetadataModel] = Field(alias="bots")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotsResponseModel(BaseModel):
    bots: List[BotMetadataModel] = Field(alias="bots")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBuiltinIntentResponseModel(BaseModel):
    signature: str = Field(alias="signature")
    supported_locales: List[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(alias="supportedLocales")
    slots: List[BuiltinIntentSlotModel] = Field(alias="slots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBuiltinIntentsResponseModel(BaseModel):
    intents: List[BuiltinIntentMetadataModel] = Field(alias="intents")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBuiltinSlotTypesResponseModel(BaseModel):
    slot_types: List[BuiltinSlotTypeMetadataModel] = Field(alias="slotTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExportResponseModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    resource_type: Literal["BOT", "INTENT", "SLOT_TYPE"] = Field(alias="resourceType")
    export_type: Literal["ALEXA_SKILLS_KIT", "LEX"] = Field(alias="exportType")
    export_status: Literal["FAILED", "IN_PROGRESS", "READY"] = Field(
        alias="exportStatus"
    )
    failure_reason: str = Field(alias="failureReason")
    url: str = Field(alias="url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImportResponseModel(BaseModel):
    name: str = Field(alias="name")
    resource_type: Literal["BOT", "INTENT", "SLOT_TYPE"] = Field(alias="resourceType")
    merge_strategy: Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"] = Field(
        alias="mergeStrategy"
    )
    import_id: str = Field(alias="importId")
    import_status: Literal["COMPLETE", "FAILED", "IN_PROGRESS"] = Field(
        alias="importStatus"
    )
    failure_reason: List[str] = Field(alias="failureReason")
    created_date: datetime = Field(alias="createdDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMigrationResponseModel(BaseModel):
    v1_bot_name: str = Field(alias="v1BotName")
    v1_bot_version: str = Field(alias="v1BotVersion")
    v1_bot_locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="v1BotLocale")
    v2_bot_id: str = Field(alias="v2BotId")
    v2_bot_role: str = Field(alias="v2BotRole")
    migration_id: str = Field(alias="migrationId")
    migration_strategy: Literal["CREATE_NEW", "UPDATE_EXISTING"] = Field(
        alias="migrationStrategy"
    )
    migration_timestamp: datetime = Field(alias="migrationTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotAliasesRequestGetBotAliasesPaginateModel(BaseModel):
    bot_name: str = Field(alias="botName")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateModel(BaseModel):
    bot_name: str = Field(alias="botName")
    bot_alias: str = Field(alias="botAlias")
    name_contains: Optional[str] = Field(default=None, alias="nameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBotVersionsRequestGetBotVersionsPaginateModel(BaseModel):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBotsRequestGetBotsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="nameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBuiltinIntentsRequestGetBuiltinIntentsPaginateModel(BaseModel):
    locale: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(default=None, alias="locale")
    signature_contains: Optional[str] = Field(default=None, alias="signatureContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateModel(BaseModel):
    locale: Optional[
        Literal[
            "de-DE",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-US",
            "es-419",
            "es-ES",
            "es-US",
            "fr-CA",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
        ]
    ] = Field(default=None, alias="locale")
    signature_contains: Optional[str] = Field(default=None, alias="signatureContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntentVersionsRequestGetIntentVersionsPaginateModel(BaseModel):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntentsRequestGetIntentsPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="nameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateModel(BaseModel):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSlotTypesRequestGetSlotTypesPaginateModel(BaseModel):
    name_contains: Optional[str] = Field(default=None, alias="nameContains")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntentVersionsResponseModel(BaseModel):
    intents: List[IntentMetadataModel] = Field(alias="intents")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntentsResponseModel(BaseModel):
    intents: List[IntentMetadataModel] = Field(alias="intents")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMigrationResponseModel(BaseModel):
    migration_id: str = Field(alias="migrationId")
    v1_bot_name: str = Field(alias="v1BotName")
    v1_bot_version: str = Field(alias="v1BotVersion")
    v1_bot_locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="v1BotLocale")
    v2_bot_id: str = Field(alias="v2BotId")
    v2_bot_role: str = Field(alias="v2BotRole")
    migration_status: Literal["COMPLETED", "FAILED", "IN_PROGRESS"] = Field(
        alias="migrationStatus"
    )
    migration_strategy: Literal["CREATE_NEW", "UPDATE_EXISTING"] = Field(
        alias="migrationStrategy"
    )
    migration_timestamp: datetime = Field(alias="migrationTimestamp")
    alerts: List[MigrationAlertModel] = Field(alias="alerts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMigrationsResponseModel(BaseModel):
    migration_summaries: List[MigrationSummaryModel] = Field(alias="migrationSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSlotTypeVersionsResponseModel(BaseModel):
    slot_types: List[SlotTypeMetadataModel] = Field(alias="slotTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSlotTypesResponseModel(BaseModel):
    slot_types: List[SlotTypeMetadataModel] = Field(alias="slotTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportRequestModel(BaseModel):
    payload: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="payload"
    )
    resource_type: Literal["BOT", "INTENT", "SLOT_TYPE"] = Field(alias="resourceType")
    merge_strategy: Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"] = Field(
        alias="mergeStrategy"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class StartImportResponseModel(BaseModel):
    name: str = Field(alias="name")
    resource_type: Literal["BOT", "INTENT", "SLOT_TYPE"] = Field(alias="resourceType")
    merge_strategy: Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"] = Field(
        alias="mergeStrategy"
    )
    import_id: str = Field(alias="importId")
    import_status: Literal["COMPLETE", "FAILED", "IN_PROGRESS"] = Field(
        alias="importStatus"
    )
    tags: List[TagModel] = Field(alias="tags")
    created_date: datetime = Field(alias="createdDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class PromptModel(BaseModel):
    messages: List[MessageModel] = Field(alias="messages")
    max_attempts: int = Field(alias="maxAttempts")
    response_card: Optional[str] = Field(default=None, alias="responseCard")


class StatementModel(BaseModel):
    messages: List[MessageModel] = Field(alias="messages")
    response_card: Optional[str] = Field(default=None, alias="responseCard")


class SlotDefaultValueSpecModel(BaseModel):
    default_value_list: List[SlotDefaultValueModel] = Field(alias="defaultValueList")


class SlotTypeConfigurationModel(BaseModel):
    regex_configuration: Optional[SlotTypeRegexConfigurationModel] = Field(
        default=None, alias="regexConfiguration"
    )


class UtteranceListModel(BaseModel):
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    utterances: Optional[List[UtteranceDataModel]] = Field(
        default=None, alias="utterances"
    )


class PutBotAliasRequestModel(BaseModel):
    name: str = Field(alias="name")
    bot_version: str = Field(alias="botVersion")
    bot_name: str = Field(alias="botName")
    description: Optional[str] = Field(default=None, alias="description")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    conversation_logs: Optional[ConversationLogsRequestModel] = Field(
        default=None, alias="conversationLogs"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class BotAliasMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    bot_name: Optional[str] = Field(default=None, alias="botName")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    conversation_logs: Optional[ConversationLogsResponseModel] = Field(
        default=None, alias="conversationLogs"
    )


class GetBotAliasResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_name: str = Field(alias="botName")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    checksum: str = Field(alias="checksum")
    conversation_logs: ConversationLogsResponseModel = Field(alias="conversationLogs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBotAliasResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_name: str = Field(alias="botName")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    checksum: str = Field(alias="checksum")
    conversation_logs: ConversationLogsResponseModel = Field(alias="conversationLogs")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBotVersionResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    intents: List[IntentModel] = Field(alias="intents")
    clarification_prompt: PromptModel = Field(alias="clarificationPrompt")
    abort_statement: StatementModel = Field(alias="abortStatement")
    status: Literal[
        "BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"
    ] = Field(alias="status")
    failure_reason: str = Field(alias="failureReason")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    voice_id: str = Field(alias="voiceId")
    checksum: str = Field(alias="checksum")
    version: str = Field(alias="version")
    locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="locale")
    child_directed: bool = Field(alias="childDirected")
    enable_model_improvements: bool = Field(alias="enableModelImprovements")
    detect_sentiment: bool = Field(alias="detectSentiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FollowUpPromptModel(BaseModel):
    prompt: PromptModel = Field(alias="prompt")
    rejection_statement: StatementModel = Field(alias="rejectionStatement")


class GetBotResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    intents: List[IntentModel] = Field(alias="intents")
    enable_model_improvements: bool = Field(alias="enableModelImprovements")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    clarification_prompt: PromptModel = Field(alias="clarificationPrompt")
    abort_statement: StatementModel = Field(alias="abortStatement")
    status: Literal[
        "BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"
    ] = Field(alias="status")
    failure_reason: str = Field(alias="failureReason")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    voice_id: str = Field(alias="voiceId")
    checksum: str = Field(alias="checksum")
    version: str = Field(alias="version")
    locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="locale")
    child_directed: bool = Field(alias="childDirected")
    detect_sentiment: bool = Field(alias="detectSentiment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBotRequestModel(BaseModel):
    name: str = Field(alias="name")
    locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="locale")
    child_directed: bool = Field(alias="childDirected")
    description: Optional[str] = Field(default=None, alias="description")
    intents: Optional[Sequence[IntentModel]] = Field(default=None, alias="intents")
    enable_model_improvements: Optional[bool] = Field(
        default=None, alias="enableModelImprovements"
    )
    nlu_intent_confidence_threshold: Optional[float] = Field(
        default=None, alias="nluIntentConfidenceThreshold"
    )
    clarification_prompt: Optional[PromptModel] = Field(
        default=None, alias="clarificationPrompt"
    )
    abort_statement: Optional[StatementModel] = Field(
        default=None, alias="abortStatement"
    )
    idle_session_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="idleSessionTTLInSeconds"
    )
    voice_id: Optional[str] = Field(default=None, alias="voiceId")
    checksum: Optional[str] = Field(default=None, alias="checksum")
    process_behavior: Optional[Literal["BUILD", "SAVE"]] = Field(
        default=None, alias="processBehavior"
    )
    detect_sentiment: Optional[bool] = Field(default=None, alias="detectSentiment")
    create_version: Optional[bool] = Field(default=None, alias="createVersion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class PutBotResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    intents: List[IntentModel] = Field(alias="intents")
    enable_model_improvements: bool = Field(alias="enableModelImprovements")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    clarification_prompt: PromptModel = Field(alias="clarificationPrompt")
    abort_statement: StatementModel = Field(alias="abortStatement")
    status: Literal[
        "BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"
    ] = Field(alias="status")
    failure_reason: str = Field(alias="failureReason")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    voice_id: str = Field(alias="voiceId")
    checksum: str = Field(alias="checksum")
    version: str = Field(alias="version")
    locale: Literal[
        "de-DE",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-US",
        "es-419",
        "es-ES",
        "es-US",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "ko-KR",
    ] = Field(alias="locale")
    child_directed: bool = Field(alias="childDirected")
    create_version: bool = Field(alias="createVersion")
    detect_sentiment: bool = Field(alias="detectSentiment")
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SlotModel(BaseModel):
    name: str = Field(alias="name")
    slot_constraint: Literal["Optional", "Required"] = Field(alias="slotConstraint")
    description: Optional[str] = Field(default=None, alias="description")
    slot_type: Optional[str] = Field(default=None, alias="slotType")
    slot_type_version: Optional[str] = Field(default=None, alias="slotTypeVersion")
    value_elicitation_prompt: Optional[PromptModel] = Field(
        default=None, alias="valueElicitationPrompt"
    )
    priority: Optional[int] = Field(default=None, alias="priority")
    sample_utterances: Optional[List[str]] = Field(
        default=None, alias="sampleUtterances"
    )
    response_card: Optional[str] = Field(default=None, alias="responseCard")
    obfuscation_setting: Optional[Literal["DEFAULT_OBFUSCATION", "NONE"]] = Field(
        default=None, alias="obfuscationSetting"
    )
    default_value_spec: Optional[SlotDefaultValueSpecModel] = Field(
        default=None, alias="defaultValueSpec"
    )


class CreateSlotTypeVersionResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    enumeration_values: List[EnumerationValueModel] = Field(alias="enumerationValues")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    value_selection_strategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = Field(
        alias="valueSelectionStrategy"
    )
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    slot_type_configurations: List[SlotTypeConfigurationModel] = Field(
        alias="slotTypeConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSlotTypeResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    enumeration_values: List[EnumerationValueModel] = Field(alias="enumerationValues")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    value_selection_strategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = Field(
        alias="valueSelectionStrategy"
    )
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    slot_type_configurations: List[SlotTypeConfigurationModel] = Field(
        alias="slotTypeConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSlotTypeRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    enumeration_values: Optional[Sequence[EnumerationValueModel]] = Field(
        default=None, alias="enumerationValues"
    )
    checksum: Optional[str] = Field(default=None, alias="checksum")
    value_selection_strategy: Optional[
        Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"]
    ] = Field(default=None, alias="valueSelectionStrategy")
    create_version: Optional[bool] = Field(default=None, alias="createVersion")
    parent_slot_type_signature: Optional[str] = Field(
        default=None, alias="parentSlotTypeSignature"
    )
    slot_type_configurations: Optional[Sequence[SlotTypeConfigurationModel]] = Field(
        default=None, alias="slotTypeConfigurations"
    )


class PutSlotTypeResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    enumeration_values: List[EnumerationValueModel] = Field(alias="enumerationValues")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    value_selection_strategy: Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"] = Field(
        alias="valueSelectionStrategy"
    )
    create_version: bool = Field(alias="createVersion")
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    slot_type_configurations: List[SlotTypeConfigurationModel] = Field(
        alias="slotTypeConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUtterancesViewResponseModel(BaseModel):
    bot_name: str = Field(alias="botName")
    utterances: List[UtteranceListModel] = Field(alias="utterances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBotAliasesResponseModel(BaseModel):
    bot_aliases: List[BotAliasMetadataModel] = Field(alias="BotAliases")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIntentVersionResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    slots: List[SlotModel] = Field(alias="slots")
    sample_utterances: List[str] = Field(alias="sampleUtterances")
    confirmation_prompt: PromptModel = Field(alias="confirmationPrompt")
    rejection_statement: StatementModel = Field(alias="rejectionStatement")
    follow_up_prompt: FollowUpPromptModel = Field(alias="followUpPrompt")
    conclusion_statement: StatementModel = Field(alias="conclusionStatement")
    dialog_code_hook: CodeHookModel = Field(alias="dialogCodeHook")
    fulfillment_activity: FulfillmentActivityModel = Field(alias="fulfillmentActivity")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntentResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    slots: List[SlotModel] = Field(alias="slots")
    sample_utterances: List[str] = Field(alias="sampleUtterances")
    confirmation_prompt: PromptModel = Field(alias="confirmationPrompt")
    rejection_statement: StatementModel = Field(alias="rejectionStatement")
    follow_up_prompt: FollowUpPromptModel = Field(alias="followUpPrompt")
    conclusion_statement: StatementModel = Field(alias="conclusionStatement")
    dialog_code_hook: CodeHookModel = Field(alias="dialogCodeHook")
    fulfillment_activity: FulfillmentActivityModel = Field(alias="fulfillmentActivity")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutIntentRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    slots: Optional[Sequence[SlotModel]] = Field(default=None, alias="slots")
    sample_utterances: Optional[Sequence[str]] = Field(
        default=None, alias="sampleUtterances"
    )
    confirmation_prompt: Optional[PromptModel] = Field(
        default=None, alias="confirmationPrompt"
    )
    rejection_statement: Optional[StatementModel] = Field(
        default=None, alias="rejectionStatement"
    )
    follow_up_prompt: Optional[FollowUpPromptModel] = Field(
        default=None, alias="followUpPrompt"
    )
    conclusion_statement: Optional[StatementModel] = Field(
        default=None, alias="conclusionStatement"
    )
    dialog_code_hook: Optional[CodeHookModel] = Field(
        default=None, alias="dialogCodeHook"
    )
    fulfillment_activity: Optional[FulfillmentActivityModel] = Field(
        default=None, alias="fulfillmentActivity"
    )
    parent_intent_signature: Optional[str] = Field(
        default=None, alias="parentIntentSignature"
    )
    checksum: Optional[str] = Field(default=None, alias="checksum")
    create_version: Optional[bool] = Field(default=None, alias="createVersion")
    kendra_configuration: Optional[KendraConfigurationModel] = Field(
        default=None, alias="kendraConfiguration"
    )
    input_contexts: Optional[Sequence[InputContextModel]] = Field(
        default=None, alias="inputContexts"
    )
    output_contexts: Optional[Sequence[OutputContextModel]] = Field(
        default=None, alias="outputContexts"
    )


class PutIntentResponseModel(BaseModel):
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    slots: List[SlotModel] = Field(alias="slots")
    sample_utterances: List[str] = Field(alias="sampleUtterances")
    confirmation_prompt: PromptModel = Field(alias="confirmationPrompt")
    rejection_statement: StatementModel = Field(alias="rejectionStatement")
    follow_up_prompt: FollowUpPromptModel = Field(alias="followUpPrompt")
    conclusion_statement: StatementModel = Field(alias="conclusionStatement")
    dialog_code_hook: CodeHookModel = Field(alias="dialogCodeHook")
    fulfillment_activity: FulfillmentActivityModel = Field(alias="fulfillmentActivity")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    checksum: str = Field(alias="checksum")
    create_version: bool = Field(alias="createVersion")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
