# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AdvancedRecognitionSettingModel(BaseModel):
    audio_recognition_strategy: Optional[
        Literal["UseSlotValuesAsCustomVocabulary"]
    ] = Field(default=None, alias="audioRecognitionStrategy")


class AggregatedUtterancesFilterModel(BaseModel):
    name: Literal["Utterance"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class AggregatedUtterancesSortByModel(BaseModel):
    attribute: Literal["HitCount", "MissedCount"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class AggregatedUtterancesSummaryModel(BaseModel):
    utterance: Optional[str] = Field(default=None, alias="utterance")
    hit_count: Optional[int] = Field(default=None, alias="hitCount")
    missed_count: Optional[int] = Field(default=None, alias="missedCount")
    utterance_first_recorded_in_aggregation_duration: Optional[datetime] = Field(
        default=None, alias="utteranceFirstRecordedInAggregationDuration"
    )
    utterance_last_recorded_in_aggregation_duration: Optional[datetime] = Field(
        default=None, alias="utteranceLastRecordedInAggregationDuration"
    )
    contains_data_from_deleted_resources: Optional[bool] = Field(
        default=None, alias="containsDataFromDeletedResources"
    )


class AllowedInputTypesModel(BaseModel):
    allow_audio_input: bool = Field(alias="allowAudioInput")
    allow_dtmfinput: bool = Field(alias="allowDTMFInput")


class AssociatedTranscriptFilterModel(BaseModel):
    name: Literal["IntentId", "SlotTypeId"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")


class AssociatedTranscriptModel(BaseModel):
    transcript: Optional[str] = Field(default=None, alias="transcript")


class AudioSpecificationModel(BaseModel):
    max_length_ms: int = Field(alias="maxLengthMs")
    end_timeout_ms: int = Field(alias="endTimeoutMs")


class DTMFSpecificationModel(BaseModel):
    max_length: int = Field(alias="maxLength")
    end_timeout_ms: int = Field(alias="endTimeoutMs")
    deletion_character: str = Field(alias="deletionCharacter")
    end_character: str = Field(alias="endCharacter")


class S3BucketLogDestinationModel(BaseModel):
    s3_bucket_arn: str = Field(alias="s3BucketArn")
    log_prefix: str = Field(alias="logPrefix")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class NewCustomVocabularyItemModel(BaseModel):
    phrase: str = Field(alias="phrase")
    weight: Optional[int] = Field(default=None, alias="weight")
    display_as: Optional[str] = Field(default=None, alias="displayAs")


class CustomVocabularyItemModel(BaseModel):
    item_id: str = Field(alias="itemId")
    phrase: str = Field(alias="phrase")
    weight: Optional[int] = Field(default=None, alias="weight")
    display_as: Optional[str] = Field(default=None, alias="displayAs")


class FailedCustomVocabularyItemModel(BaseModel):
    item_id: Optional[str] = Field(default=None, alias="itemId")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    error_code: Optional[
        Literal[
            "DUPLICATE_INPUT",
            "INTERNAL_SERVER_FAILURE",
            "RESOURCE_ALREADY_EXISTS",
            "RESOURCE_DOES_NOT_EXIST",
        ]
    ] = Field(default=None, alias="errorCode")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CustomVocabularyEntryIdModel(BaseModel):
    item_id: str = Field(alias="itemId")


class BotAliasHistoryEventModel(BaseModel):
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    start_date: Optional[datetime] = Field(default=None, alias="startDate")
    end_date: Optional[datetime] = Field(default=None, alias="endDate")


class BotAliasSummaryModel(BaseModel):
    bot_alias_id: Optional[str] = Field(default=None, alias="botAliasId")
    bot_alias_name: Optional[str] = Field(default=None, alias="botAliasName")
    description: Optional[str] = Field(default=None, alias="description")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    bot_alias_status: Optional[
        Literal["Available", "Creating", "Deleting", "Failed"]
    ] = Field(default=None, alias="botAliasStatus")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class BotExportSpecificationModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")


class BotFilterModel(BaseModel):
    name: Literal["BotName", "BotType"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ", "NE"] = Field(alias="operator")


class DataPrivacyModel(BaseModel):
    child_directed: bool = Field(alias="childDirected")


class BotLocaleExportSpecificationModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class BotLocaleFilterModel(BaseModel):
    name: Literal["BotLocaleName"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class BotLocaleHistoryEventModel(BaseModel):
    event: str = Field(alias="event")
    event_date: datetime = Field(alias="eventDate")


class VoiceSettingsModel(BaseModel):
    voice_id: str = Field(alias="voiceId")
    engine: Optional[Literal["neural", "standard"]] = Field(
        default=None, alias="engine"
    )


class BotLocaleSortByModel(BaseModel):
    attribute: Literal["BotLocaleName"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class BotLocaleSummaryModel(BaseModel):
    locale_id: Optional[str] = Field(default=None, alias="localeId")
    locale_name: Optional[str] = Field(default=None, alias="localeName")
    description: Optional[str] = Field(default=None, alias="description")
    bot_locale_status: Optional[
        Literal[
            "Building",
            "Built",
            "Creating",
            "Deleting",
            "Failed",
            "Importing",
            "NotBuilt",
            "Processing",
            "ReadyExpressTesting",
        ]
    ] = Field(default=None, alias="botLocaleStatus")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    last_build_submitted_date_time: Optional[datetime] = Field(
        default=None, alias="lastBuildSubmittedDateTime"
    )


class BotMemberModel(BaseModel):
    bot_member_id: str = Field(alias="botMemberId")
    bot_member_name: str = Field(alias="botMemberName")
    bot_member_alias_id: str = Field(alias="botMemberAliasId")
    bot_member_alias_name: str = Field(alias="botMemberAliasName")
    bot_member_version: str = Field(alias="botMemberVersion")


class IntentStatisticsModel(BaseModel):
    discovered_intent_count: Optional[int] = Field(
        default=None, alias="discoveredIntentCount"
    )


class SlotTypeStatisticsModel(BaseModel):
    discovered_slot_type_count: Optional[int] = Field(
        default=None, alias="discoveredSlotTypeCount"
    )


class BotRecommendationSummaryModel(BaseModel):
    bot_recommendation_status: Literal[
        "Available",
        "Deleted",
        "Deleting",
        "Downloading",
        "Failed",
        "Processing",
        "Stopped",
        "Stopping",
        "Updating",
    ] = Field(alias="botRecommendationStatus")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class BotSortByModel(BaseModel):
    attribute: Literal["BotName"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class BotSummaryModel(BaseModel):
    bot_id: Optional[str] = Field(default=None, alias="botId")
    bot_name: Optional[str] = Field(default=None, alias="botName")
    description: Optional[str] = Field(default=None, alias="description")
    bot_status: Optional[
        Literal[
            "Available",
            "Creating",
            "Deleting",
            "Failed",
            "Importing",
            "Inactive",
            "Updating",
            "Versioning",
        ]
    ] = Field(default=None, alias="botStatus")
    latest_bot_version: Optional[str] = Field(default=None, alias="latestBotVersion")
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    bot_type: Optional[Literal["Bot", "BotNetwork"]] = Field(
        default=None, alias="botType"
    )


class BotVersionLocaleDetailsModel(BaseModel):
    source_bot_version: str = Field(alias="sourceBotVersion")


class BotVersionSortByModel(BaseModel):
    attribute: Literal["BotVersion"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class BotVersionSummaryModel(BaseModel):
    bot_name: Optional[str] = Field(default=None, alias="botName")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    description: Optional[str] = Field(default=None, alias="description")
    bot_status: Optional[
        Literal[
            "Available",
            "Creating",
            "Deleting",
            "Failed",
            "Importing",
            "Inactive",
            "Updating",
            "Versioning",
        ]
    ] = Field(default=None, alias="botStatus")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )


class BuildBotLocaleRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class BuiltInIntentSortByModel(BaseModel):
    attribute: Literal["IntentSignature"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class BuiltInIntentSummaryModel(BaseModel):
    intent_signature: Optional[str] = Field(default=None, alias="intentSignature")
    description: Optional[str] = Field(default=None, alias="description")


class BuiltInSlotTypeSortByModel(BaseModel):
    attribute: Literal["SlotTypeSignature"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class BuiltInSlotTypeSummaryModel(BaseModel):
    slot_type_signature: Optional[str] = Field(default=None, alias="slotTypeSignature")
    description: Optional[str] = Field(default=None, alias="description")


class ButtonModel(BaseModel):
    text: str = Field(alias="text")
    value: str = Field(alias="value")


class CloudWatchLogGroupLogDestinationModel(BaseModel):
    cloud_watch_log_group_arn: str = Field(alias="cloudWatchLogGroupArn")
    log_prefix: str = Field(alias="logPrefix")


class LambdaCodeHookModel(BaseModel):
    lambda_arn: str = Field(alias="lambdaARN")
    code_hook_interface_version: str = Field(alias="codeHookInterfaceVersion")


class SubSlotTypeCompositionModel(BaseModel):
    name: str = Field(alias="name")
    slot_type_id: str = Field(alias="slotTypeId")


class ConditionModel(BaseModel):
    expression_string: str = Field(alias="expressionString")


class SentimentAnalysisSettingsModel(BaseModel):
    detect_sentiment: bool = Field(alias="detectSentiment")


class DialogCodeHookSettingsModel(BaseModel):
    enabled: bool = Field(alias="enabled")


class InputContextModel(BaseModel):
    name: str = Field(alias="name")


class KendraConfigurationModel(BaseModel):
    kendra_index: str = Field(alias="kendraIndex")
    query_filter_string_enabled: Optional[bool] = Field(
        default=None, alias="queryFilterStringEnabled"
    )
    query_filter_string: Optional[str] = Field(default=None, alias="queryFilterString")


class OutputContextModel(BaseModel):
    name: str = Field(alias="name")
    time_to_live_in_seconds: int = Field(alias="timeToLiveInSeconds")
    turns_to_live: int = Field(alias="turnsToLive")


class SampleUtteranceModel(BaseModel):
    utterance: str = Field(alias="utterance")


class CreateResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    policy: str = Field(alias="policy")


class PrincipalModel(BaseModel):
    service: Optional[str] = Field(default=None, alias="service")
    arn: Optional[str] = Field(default=None, alias="arn")


class MultipleValuesSettingModel(BaseModel):
    allow_multiple_values: Optional[bool] = Field(
        default=None, alias="allowMultipleValues"
    )


class ObfuscationSettingModel(BaseModel):
    obfuscation_setting_type: Literal["DefaultObfuscation", "None"] = Field(
        alias="obfuscationSettingType"
    )


class CustomPayloadModel(BaseModel):
    value: str = Field(alias="value")


class CustomVocabularyExportSpecificationModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class CustomVocabularyImportSpecificationModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DateRangeFilterModel(BaseModel):
    start_date_time: datetime = Field(alias="startDateTime")
    end_date_time: datetime = Field(alias="endDateTime")


class DeleteBotAliasRequestModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_id: str = Field(alias="botId")
    skip_resource_in_use_check: Optional[bool] = Field(
        default=None, alias="skipResourceInUseCheck"
    )


class DeleteBotLocaleRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DeleteBotRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    skip_resource_in_use_check: Optional[bool] = Field(
        default=None, alias="skipResourceInUseCheck"
    )


class DeleteBotVersionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    skip_resource_in_use_check: Optional[bool] = Field(
        default=None, alias="skipResourceInUseCheck"
    )


class DeleteCustomVocabularyRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DeleteExportRequestModel(BaseModel):
    export_id: str = Field(alias="exportId")


class DeleteImportRequestModel(BaseModel):
    import_id: str = Field(alias="importId")


class DeleteIntentRequestModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    expected_revision_id: Optional[str] = Field(
        default=None, alias="expectedRevisionId"
    )


class DeleteResourcePolicyStatementRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    statement_id: str = Field(alias="statementId")
    expected_revision_id: Optional[str] = Field(
        default=None, alias="expectedRevisionId"
    )


class DeleteSlotRequestModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")


class DeleteSlotTypeRequestModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    skip_resource_in_use_check: Optional[bool] = Field(
        default=None, alias="skipResourceInUseCheck"
    )


class DeleteUtterancesRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    locale_id: Optional[str] = Field(default=None, alias="localeId")
    session_id: Optional[str] = Field(default=None, alias="sessionId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeBotAliasRequestModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_id: str = Field(alias="botId")


class ParentBotNetworkModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")


class DescribeBotLocaleRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DescribeBotRecommendationRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")


class EncryptionSettingModel(BaseModel):
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    bot_locale_export_password: Optional[str] = Field(
        default=None, alias="botLocaleExportPassword"
    )
    associated_transcripts_password: Optional[str] = Field(
        default=None, alias="associatedTranscriptsPassword"
    )


class DescribeBotRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")


class DescribeBotVersionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")


class DescribeCustomVocabularyMetadataRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DescribeExportRequestModel(BaseModel):
    export_id: str = Field(alias="exportId")


class DescribeImportRequestModel(BaseModel):
    import_id: str = Field(alias="importId")


class DescribeIntentRequestModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class SlotPriorityModel(BaseModel):
    priority: int = Field(alias="priority")
    slot_id: str = Field(alias="slotId")


class DescribeResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class DescribeSlotRequestModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")


class DescribeSlotTypeRequestModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")


class DialogActionModel(BaseModel):
    type: Literal[
        "CloseIntent",
        "ConfirmIntent",
        "ElicitIntent",
        "ElicitSlot",
        "EndConversation",
        "EvaluateConditional",
        "FulfillIntent",
        "InvokeDialogCodeHook",
        "StartIntent",
    ] = Field(alias="type")
    slot_to_elicit: Optional[str] = Field(default=None, alias="slotToElicit")
    suppress_next_message: Optional[bool] = Field(
        default=None, alias="suppressNextMessage"
    )


class IntentOverrideModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    slots: Optional[Mapping[str, SlotValueOverrideModel]] = Field(
        default=None, alias="slots"
    )


class ElicitationCodeHookInvocationSettingModel(BaseModel):
    enable_code_hook_invocation: bool = Field(alias="enableCodeHookInvocation")
    invocation_label: Optional[str] = Field(default=None, alias="invocationLabel")


class ExportFilterModel(BaseModel):
    name: Literal["ExportResourceType"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class ExportSortByModel(BaseModel):
    attribute: Literal["LastUpdatedDateTime"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class GrammarSlotTypeSourceModel(BaseModel):
    s3_bucket_name: str = Field(alias="s3BucketName")
    s3_object_key: str = Field(alias="s3ObjectKey")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class ImportFilterModel(BaseModel):
    name: Literal["ImportResourceType"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class ImportSortByModel(BaseModel):
    attribute: Literal["LastUpdatedDateTime"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class ImportSummaryModel(BaseModel):
    import_id: Optional[str] = Field(default=None, alias="importId")
    imported_resource_id: Optional[str] = Field(
        default=None, alias="importedResourceId"
    )
    imported_resource_name: Optional[str] = Field(
        default=None, alias="importedResourceName"
    )
    import_status: Optional[
        Literal["Completed", "Deleting", "Failed", "InProgress"]
    ] = Field(default=None, alias="importStatus")
    merge_strategy: Optional[Literal["Append", "FailOnConflict", "Overwrite"]] = Field(
        default=None, alias="mergeStrategy"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    imported_resource_type: Optional[
        Literal["Bot", "BotLocale", "CustomVocabulary"]
    ] = Field(default=None, alias="importedResourceType")


class IntentFilterModel(BaseModel):
    name: Literal["IntentName"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class IntentSortByModel(BaseModel):
    attribute: Literal["IntentName", "LastUpdatedDateTime"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class ListBotAliasesRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBotRecommendationsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCustomVocabularyItemsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRecommendedIntentsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RecommendedIntentSummaryModel(BaseModel):
    intent_id: Optional[str] = Field(default=None, alias="intentId")
    intent_name: Optional[str] = Field(default=None, alias="intentName")
    sample_utterances_count: Optional[int] = Field(
        default=None, alias="sampleUtterancesCount"
    )


class SlotTypeFilterModel(BaseModel):
    name: Literal["ExternalSourceType", "SlotTypeName"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class SlotTypeSortByModel(BaseModel):
    attribute: Literal["LastUpdatedDateTime", "SlotTypeName"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class SlotTypeSummaryModel(BaseModel):
    slot_type_id: Optional[str] = Field(default=None, alias="slotTypeId")
    slot_type_name: Optional[str] = Field(default=None, alias="slotTypeName")
    description: Optional[str] = Field(default=None, alias="description")
    parent_slot_type_signature: Optional[str] = Field(
        default=None, alias="parentSlotTypeSignature"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )
    slot_type_category: Optional[
        Literal["Composite", "Custom", "Extended", "ExternalGrammar"]
    ] = Field(default=None, alias="slotTypeCategory")


class SlotFilterModel(BaseModel):
    name: Literal["SlotName"] = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    operator: Literal["CO", "EQ"] = Field(alias="operator")


class SlotSortByModel(BaseModel):
    attribute: Literal["LastUpdatedDateTime", "SlotName"] = Field(alias="attribute")
    order: Literal["Ascending", "Descending"] = Field(alias="order")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")


class PlainTextMessageModel(BaseModel):
    value: str = Field(alias="value")


class SSMLMessageModel(BaseModel):
    value: str = Field(alias="value")


class PathFormatModel(BaseModel):
    object_prefixes: Optional[List[str]] = Field(default=None, alias="objectPrefixes")


class TextInputSpecificationModel(BaseModel):
    start_timeout_ms: int = Field(alias="startTimeoutMs")


class RelativeAggregationDurationModel(BaseModel):
    time_dimension: Literal["Days", "Hours", "Weeks"] = Field(alias="timeDimension")
    time_value: int = Field(alias="timeValue")


class SampleValueModel(BaseModel):
    value: str = Field(alias="value")


class SlotDefaultValueModel(BaseModel):
    default_value: str = Field(alias="defaultValue")


class SlotValueModel(BaseModel):
    interpreted_value: Optional[str] = Field(default=None, alias="interpretedValue")


class SlotValueRegexFilterModel(BaseModel):
    pattern: str = Field(alias="pattern")


class StopBotRecommendationRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceARN")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateExportRequestModel(BaseModel):
    export_id: str = Field(alias="exportId")
    file_password: Optional[str] = Field(default=None, alias="filePassword")


class UpdateResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    policy: str = Field(alias="policy")
    expected_revision_id: Optional[str] = Field(
        default=None, alias="expectedRevisionId"
    )


class SearchAssociatedTranscriptsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    filters: Sequence[AssociatedTranscriptFilterModel] = Field(alias="filters")
    search_order: Optional[Literal["Ascending", "Descending"]] = Field(
        default=None, alias="searchOrder"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_index: Optional[int] = Field(default=None, alias="nextIndex")


class AudioAndDTMFInputSpecificationModel(BaseModel):
    start_timeout_ms: int = Field(alias="startTimeoutMs")
    audio_specification: Optional[AudioSpecificationModel] = Field(
        default=None, alias="audioSpecification"
    )
    dtmf_specification: Optional[DTMFSpecificationModel] = Field(
        default=None, alias="dtmfSpecification"
    )


class AudioLogDestinationModel(BaseModel):
    s3_bucket: S3BucketLogDestinationModel = Field(alias="s3Bucket")


class BatchCreateCustomVocabularyItemRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_item_list: Sequence[NewCustomVocabularyItemModel] = Field(
        alias="customVocabularyItemList"
    )


class BatchUpdateCustomVocabularyItemRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_item_list: Sequence[CustomVocabularyItemModel] = Field(
        alias="customVocabularyItemList"
    )


class BatchCreateCustomVocabularyItemResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    errors: List[FailedCustomVocabularyItemModel] = Field(alias="errors")
    resources: List[CustomVocabularyItemModel] = Field(alias="resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteCustomVocabularyItemResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    errors: List[FailedCustomVocabularyItemModel] = Field(alias="errors")
    resources: List[CustomVocabularyItemModel] = Field(alias="resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateCustomVocabularyItemResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    errors: List[FailedCustomVocabularyItemModel] = Field(alias="errors")
    resources: List[CustomVocabularyItemModel] = Field(alias="resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BuildBotLocaleResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_locale_status: Literal[
        "Building",
        "Built",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "NotBuilt",
        "Processing",
        "ReadyExpressTesting",
    ] = Field(alias="botLocaleStatus")
    last_build_submitted_date_time: datetime = Field(alias="lastBuildSubmittedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourcePolicyStatementResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUploadUrlResponseModel(BaseModel):
    import_id: str = Field(alias="importId")
    upload_url: str = Field(alias="uploadUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBotAliasResponseModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_id: str = Field(alias="botId")
    bot_alias_status: Literal["Available", "Creating", "Deleting", "Failed"] = Field(
        alias="botAliasStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBotLocaleResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_locale_status: Literal[
        "Building",
        "Built",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "NotBuilt",
        "Processing",
        "ReadyExpressTesting",
    ] = Field(alias="botLocaleStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBotResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBotVersionResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCustomVocabularyResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_status: Literal[
        "Creating", "Deleting", "Exporting", "Importing", "Ready"
    ] = Field(alias="customVocabularyStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteExportResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    export_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="exportStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImportResponseModel(BaseModel):
    import_id: str = Field(alias="importId")
    import_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="importStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResourcePolicyStatementResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomVocabularyMetadataResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_status: Literal[
        "Creating", "Deleting", "Exporting", "Importing", "Ready"
    ] = Field(alias="customVocabularyStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    policy: str = Field(alias="policy")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomVocabularyItemsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_items: List[CustomVocabularyItemModel] = Field(
        alias="customVocabularyItems"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAssociatedTranscriptsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    next_index: int = Field(alias="nextIndex")
    associated_transcripts: List[AssociatedTranscriptModel] = Field(
        alias="associatedTranscripts"
    )
    total_results: int = Field(alias="totalResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopBotRecommendationResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_status: Literal[
        "Available",
        "Deleted",
        "Deleting",
        "Downloading",
        "Failed",
        "Processing",
        "Stopped",
        "Stopping",
        "Updating",
    ] = Field(alias="botRecommendationStatus")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourcePolicyResponseModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    revision_id: str = Field(alias="revisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeleteCustomVocabularyItemRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    custom_vocabulary_item_list: Sequence[CustomVocabularyEntryIdModel] = Field(
        alias="customVocabularyItemList"
    )


class ListBotAliasesResponseModel(BaseModel):
    bot_alias_summaries: List[BotAliasSummaryModel] = Field(alias="botAliasSummaries")
    next_token: str = Field(alias="nextToken")
    bot_id: str = Field(alias="botId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BotImportSpecificationModel(BaseModel):
    bot_name: str = Field(alias="botName")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="idleSessionTTLInSeconds"
    )
    bot_tags: Optional[Dict[str, str]] = Field(default=None, alias="botTags")
    test_bot_alias_tags: Optional[Dict[str, str]] = Field(
        default=None, alias="testBotAliasTags"
    )


class BotLocaleImportSpecificationModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    nlu_intent_confidence_threshold: Optional[float] = Field(
        default=None, alias="nluIntentConfidenceThreshold"
    )
    voice_settings: Optional[VoiceSettingsModel] = Field(
        default=None, alias="voiceSettings"
    )


class CreateBotLocaleRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    description: Optional[str] = Field(default=None, alias="description")
    voice_settings: Optional[VoiceSettingsModel] = Field(
        default=None, alias="voiceSettings"
    )


class CreateBotLocaleResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_name: str = Field(alias="localeName")
    locale_id: str = Field(alias="localeId")
    description: str = Field(alias="description")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    voice_settings: VoiceSettingsModel = Field(alias="voiceSettings")
    bot_locale_status: Literal[
        "Building",
        "Built",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "NotBuilt",
        "Processing",
        "ReadyExpressTesting",
    ] = Field(alias="botLocaleStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBotLocaleResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    locale_name: str = Field(alias="localeName")
    description: str = Field(alias="description")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    voice_settings: VoiceSettingsModel = Field(alias="voiceSettings")
    intents_count: int = Field(alias="intentsCount")
    slot_types_count: int = Field(alias="slotTypesCount")
    bot_locale_status: Literal[
        "Building",
        "Built",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "NotBuilt",
        "Processing",
        "ReadyExpressTesting",
    ] = Field(alias="botLocaleStatus")
    failure_reasons: List[str] = Field(alias="failureReasons")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    last_build_submitted_date_time: datetime = Field(alias="lastBuildSubmittedDateTime")
    bot_locale_history_events: List[BotLocaleHistoryEventModel] = Field(
        alias="botLocaleHistoryEvents"
    )
    recommended_actions: List[str] = Field(alias="recommendedActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotLocaleRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    description: Optional[str] = Field(default=None, alias="description")
    voice_settings: Optional[VoiceSettingsModel] = Field(
        default=None, alias="voiceSettings"
    )


class UpdateBotLocaleResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    locale_name: str = Field(alias="localeName")
    description: str = Field(alias="description")
    nlu_intent_confidence_threshold: float = Field(alias="nluIntentConfidenceThreshold")
    voice_settings: VoiceSettingsModel = Field(alias="voiceSettings")
    bot_locale_status: Literal[
        "Building",
        "Built",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "NotBuilt",
        "Processing",
        "ReadyExpressTesting",
    ] = Field(alias="botLocaleStatus")
    failure_reasons: List[str] = Field(alias="failureReasons")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    recommended_actions: List[str] = Field(alias="recommendedActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBotLocalesRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    sort_by: Optional[BotLocaleSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[BotLocaleFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBotLocalesResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    next_token: str = Field(alias="nextToken")
    bot_locale_summaries: List[BotLocaleSummaryModel] = Field(
        alias="botLocaleSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBotRequestModel(BaseModel):
    bot_name: str = Field(alias="botName")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    description: Optional[str] = Field(default=None, alias="description")
    bot_tags: Optional[Mapping[str, str]] = Field(default=None, alias="botTags")
    test_bot_alias_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="testBotAliasTags"
    )
    bot_type: Optional[Literal["Bot", "BotNetwork"]] = Field(
        default=None, alias="botType"
    )
    bot_members: Optional[Sequence[BotMemberModel]] = Field(
        default=None, alias="botMembers"
    )


class CreateBotResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: str = Field(alias="botName")
    description: str = Field(alias="description")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    bot_tags: Dict[str, str] = Field(alias="botTags")
    test_bot_alias_tags: Dict[str, str] = Field(alias="testBotAliasTags")
    bot_type: Literal["Bot", "BotNetwork"] = Field(alias="botType")
    bot_members: List[BotMemberModel] = Field(alias="botMembers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBotResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: str = Field(alias="botName")
    description: str = Field(alias="description")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    bot_type: Literal["Bot", "BotNetwork"] = Field(alias="botType")
    bot_members: List[BotMemberModel] = Field(alias="botMembers")
    failure_reasons: List[str] = Field(alias="failureReasons")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: str = Field(alias="botName")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    description: Optional[str] = Field(default=None, alias="description")
    bot_type: Optional[Literal["Bot", "BotNetwork"]] = Field(
        default=None, alias="botType"
    )
    bot_members: Optional[Sequence[BotMemberModel]] = Field(
        default=None, alias="botMembers"
    )


class UpdateBotResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: str = Field(alias="botName")
    description: str = Field(alias="description")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    bot_type: Literal["Bot", "BotNetwork"] = Field(alias="botType")
    bot_members: List[BotMemberModel] = Field(alias="botMembers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BotRecommendationResultStatisticsModel(BaseModel):
    intents: Optional[IntentStatisticsModel] = Field(default=None, alias="intents")
    slot_types: Optional[SlotTypeStatisticsModel] = Field(
        default=None, alias="slotTypes"
    )


class ListBotRecommendationsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_summaries: List[BotRecommendationSummaryModel] = Field(
        alias="botRecommendationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBotsRequestModel(BaseModel):
    sort_by: Optional[BotSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[BotFilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBotsResponseModel(BaseModel):
    bot_summaries: List[BotSummaryModel] = Field(alias="botSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBotVersionRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version_locale_specification: Mapping[
        str, BotVersionLocaleDetailsModel
    ] = Field(alias="botVersionLocaleSpecification")
    description: Optional[str] = Field(default=None, alias="description")


class CreateBotVersionResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_version_locale_specification: Dict[str, BotVersionLocaleDetailsModel] = Field(
        alias="botVersionLocaleSpecification"
    )
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBotVersionsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    sort_by: Optional[BotVersionSortByModel] = Field(default=None, alias="sortBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBotVersionsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version_summaries: List[BotVersionSummaryModel] = Field(
        alias="botVersionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuiltInIntentsRequestModel(BaseModel):
    locale_id: str = Field(alias="localeId")
    sort_by: Optional[BuiltInIntentSortByModel] = Field(default=None, alias="sortBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBuiltInIntentsResponseModel(BaseModel):
    built_in_intent_summaries: List[BuiltInIntentSummaryModel] = Field(
        alias="builtInIntentSummaries"
    )
    next_token: str = Field(alias="nextToken")
    locale_id: str = Field(alias="localeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuiltInSlotTypesRequestModel(BaseModel):
    locale_id: str = Field(alias="localeId")
    sort_by: Optional[BuiltInSlotTypeSortByModel] = Field(default=None, alias="sortBy")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListBuiltInSlotTypesResponseModel(BaseModel):
    built_in_slot_type_summaries: List[BuiltInSlotTypeSummaryModel] = Field(
        alias="builtInSlotTypeSummaries"
    )
    next_token: str = Field(alias="nextToken")
    locale_id: str = Field(alias="localeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageResponseCardModel(BaseModel):
    title: str = Field(alias="title")
    subtitle: Optional[str] = Field(default=None, alias="subtitle")
    image_url: Optional[str] = Field(default=None, alias="imageUrl")
    buttons: Optional[Sequence[ButtonModel]] = Field(default=None, alias="buttons")


class TextLogDestinationModel(BaseModel):
    cloud_watch: CloudWatchLogGroupLogDestinationModel = Field(alias="cloudWatch")


class CodeHookSpecificationModel(BaseModel):
    lambda_code_hook: LambdaCodeHookModel = Field(alias="lambdaCodeHook")


class CompositeSlotTypeSettingModel(BaseModel):
    sub_slots: Optional[Sequence[SubSlotTypeCompositionModel]] = Field(
        default=None, alias="subSlots"
    )


class IntentSummaryModel(BaseModel):
    intent_id: Optional[str] = Field(default=None, alias="intentId")
    intent_name: Optional[str] = Field(default=None, alias="intentName")
    description: Optional[str] = Field(default=None, alias="description")
    parent_intent_signature: Optional[str] = Field(
        default=None, alias="parentIntentSignature"
    )
    input_contexts: Optional[List[InputContextModel]] = Field(
        default=None, alias="inputContexts"
    )
    output_contexts: Optional[List[OutputContextModel]] = Field(
        default=None, alias="outputContexts"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class CreateResourcePolicyStatementRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    statement_id: str = Field(alias="statementId")
    effect: Literal["Allow", "Deny"] = Field(alias="effect")
    principal: Sequence[PrincipalModel] = Field(alias="principal")
    action: Sequence[str] = Field(alias="action")
    condition: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="condition"
    )
    expected_revision_id: Optional[str] = Field(
        default=None, alias="expectedRevisionId"
    )


class ExportResourceSpecificationModel(BaseModel):
    bot_export_specification: Optional[BotExportSpecificationModel] = Field(
        default=None, alias="botExportSpecification"
    )
    bot_locale_export_specification: Optional[
        BotLocaleExportSpecificationModel
    ] = Field(default=None, alias="botLocaleExportSpecification")
    custom_vocabulary_export_specification: Optional[
        CustomVocabularyExportSpecificationModel
    ] = Field(default=None, alias="customVocabularyExportSpecification")


class LexTranscriptFilterModel(BaseModel):
    date_range_filter: Optional[DateRangeFilterModel] = Field(
        default=None, alias="dateRangeFilter"
    )


class DescribeBotAliasRequestBotAliasAvailableWaitModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_id: str = Field(alias="botId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotLocaleRequestBotLocaleBuiltWaitModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotLocaleRequestBotLocaleCreatedWaitModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotRequestBotAvailableWaitModel(BaseModel):
    bot_id: str = Field(alias="botId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotVersionRequestBotVersionAvailableWaitModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeExportRequestBotExportCompletedWaitModel(BaseModel):
    export_id: str = Field(alias="exportId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeImportRequestBotImportCompletedWaitModel(BaseModel):
    import_id: str = Field(alias="importId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeBotVersionResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_name: str = Field(alias="botName")
    bot_version: str = Field(alias="botVersion")
    description: str = Field(alias="description")
    role_arn: str = Field(alias="roleArn")
    data_privacy: DataPrivacyModel = Field(alias="dataPrivacy")
    idle_session_ttl_in_seconds: int = Field(alias="idleSessionTTLInSeconds")
    bot_status: Literal[
        "Available",
        "Creating",
        "Deleting",
        "Failed",
        "Importing",
        "Inactive",
        "Updating",
        "Versioning",
    ] = Field(alias="botStatus")
    failure_reasons: List[str] = Field(alias="failureReasons")
    creation_date_time: datetime = Field(alias="creationDateTime")
    parent_bot_networks: List[ParentBotNetworkModel] = Field(alias="parentBotNetworks")
    bot_type: Literal["Bot", "BotNetwork"] = Field(alias="botType")
    bot_members: List[BotMemberModel] = Field(alias="botMembers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotRecommendationRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    encryption_setting: EncryptionSettingModel = Field(alias="encryptionSetting")


class DialogStateModel(BaseModel):
    dialog_action: Optional[DialogActionModel] = Field(
        default=None, alias="dialogAction"
    )
    intent: Optional[IntentOverrideModel] = Field(default=None, alias="intent")
    session_attributes: Optional[Mapping[str, str]] = Field(
        default=None, alias="sessionAttributes"
    )


class ListExportsRequestModel(BaseModel):
    bot_id: Optional[str] = Field(default=None, alias="botId")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    sort_by: Optional[ExportSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[ExportFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    locale_id: Optional[str] = Field(default=None, alias="localeId")


class GrammarSlotTypeSettingModel(BaseModel):
    source: Optional[GrammarSlotTypeSourceModel] = Field(default=None, alias="source")


class ListImportsRequestModel(BaseModel):
    bot_id: Optional[str] = Field(default=None, alias="botId")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    sort_by: Optional[ImportSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[ImportFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    locale_id: Optional[str] = Field(default=None, alias="localeId")


class ListImportsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    import_summaries: List[ImportSummaryModel] = Field(alias="importSummaries")
    next_token: str = Field(alias="nextToken")
    locale_id: str = Field(alias="localeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIntentsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    sort_by: Optional[IntentSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[IntentFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRecommendedIntentsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    summary_list: List[RecommendedIntentSummaryModel] = Field(alias="summaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSlotTypesRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    sort_by: Optional[SlotTypeSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[SlotTypeFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSlotTypesResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    slot_type_summaries: List[SlotTypeSummaryModel] = Field(alias="slotTypeSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSlotsRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    sort_by: Optional[SlotSortByModel] = Field(default=None, alias="sortBy")
    filters: Optional[Sequence[SlotFilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UtteranceAggregationDurationModel(BaseModel):
    relative_aggregation_duration: RelativeAggregationDurationModel = Field(
        alias="relativeAggregationDuration"
    )


class SlotTypeValueModel(BaseModel):
    sample_value: Optional[SampleValueModel] = Field(default=None, alias="sampleValue")
    synonyms: Optional[Sequence[SampleValueModel]] = Field(
        default=None, alias="synonyms"
    )


class SlotDefaultValueSpecificationModel(BaseModel):
    default_value_list: Sequence[SlotDefaultValueModel] = Field(
        alias="defaultValueList"
    )


class SlotValueOverrideModel(BaseModel):
    shape: Optional[Literal["List", "Scalar"]] = Field(default=None, alias="shape")
    value: Optional[SlotValueModel] = Field(default=None, alias="value")
    values: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="values")


class SlotValueSelectionSettingModel(BaseModel):
    resolution_strategy: Literal[
        "Concatenation", "OriginalValue", "TopResolution"
    ] = Field(alias="resolutionStrategy")
    regex_filter: Optional[SlotValueRegexFilterModel] = Field(
        default=None, alias="regexFilter"
    )
    advanced_recognition_setting: Optional[AdvancedRecognitionSettingModel] = Field(
        default=None, alias="advancedRecognitionSetting"
    )


class PromptAttemptSpecificationModel(BaseModel):
    allowed_input_types: AllowedInputTypesModel = Field(alias="allowedInputTypes")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")
    audio_and_dtmfinput_specification: Optional[
        AudioAndDTMFInputSpecificationModel
    ] = Field(default=None, alias="audioAndDTMFInputSpecification")
    text_input_specification: Optional[TextInputSpecificationModel] = Field(
        default=None, alias="textInputSpecification"
    )


class AudioLogSettingModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    destination: AudioLogDestinationModel = Field(alias="destination")


class ImportResourceSpecificationModel(BaseModel):
    bot_import_specification: Optional[BotImportSpecificationModel] = Field(
        default=None, alias="botImportSpecification"
    )
    bot_locale_import_specification: Optional[
        BotLocaleImportSpecificationModel
    ] = Field(default=None, alias="botLocaleImportSpecification")
    custom_vocabulary_import_specification: Optional[
        CustomVocabularyImportSpecificationModel
    ] = Field(default=None, alias="customVocabularyImportSpecification")


class BotRecommendationResultsModel(BaseModel):
    bot_locale_export_url: Optional[str] = Field(
        default=None, alias="botLocaleExportUrl"
    )
    associated_transcripts_url: Optional[str] = Field(
        default=None, alias="associatedTranscriptsUrl"
    )
    statistics: Optional[BotRecommendationResultStatisticsModel] = Field(
        default=None, alias="statistics"
    )


class MessageModel(BaseModel):
    plain_text_message: Optional[PlainTextMessageModel] = Field(
        default=None, alias="plainTextMessage"
    )
    custom_payload: Optional[CustomPayloadModel] = Field(
        default=None, alias="customPayload"
    )
    ssml_message: Optional[SSMLMessageModel] = Field(default=None, alias="ssmlMessage")
    image_response_card: Optional[ImageResponseCardModel] = Field(
        default=None, alias="imageResponseCard"
    )


class TextLogSettingModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    destination: TextLogDestinationModel = Field(alias="destination")


class BotAliasLocaleSettingsModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    code_hook_specification: Optional[CodeHookSpecificationModel] = Field(
        default=None, alias="codeHookSpecification"
    )


class ListIntentsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_summaries: List[IntentSummaryModel] = Field(alias="intentSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExportRequestModel(BaseModel):
    resource_specification: ExportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    file_format: Literal["LexJson", "TSV"] = Field(alias="fileFormat")
    file_password: Optional[str] = Field(default=None, alias="filePassword")


class CreateExportResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    resource_specification: ExportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    file_format: Literal["LexJson", "TSV"] = Field(alias="fileFormat")
    export_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="exportStatus"
    )
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExportResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    resource_specification: ExportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    file_format: Literal["LexJson", "TSV"] = Field(alias="fileFormat")
    export_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="exportStatus"
    )
    failure_reasons: List[str] = Field(alias="failureReasons")
    download_url: str = Field(alias="downloadUrl")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportSummaryModel(BaseModel):
    export_id: Optional[str] = Field(default=None, alias="exportId")
    resource_specification: Optional[ExportResourceSpecificationModel] = Field(
        default=None, alias="resourceSpecification"
    )
    file_format: Optional[Literal["LexJson", "TSV"]] = Field(
        default=None, alias="fileFormat"
    )
    export_status: Optional[
        Literal["Completed", "Deleting", "Failed", "InProgress"]
    ] = Field(default=None, alias="exportStatus")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="creationDateTime"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class UpdateExportResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    resource_specification: ExportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    file_format: Literal["LexJson", "TSV"] = Field(alias="fileFormat")
    export_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="exportStatus"
    )
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TranscriptFilterModel(BaseModel):
    lex_transcript_filter: Optional[LexTranscriptFilterModel] = Field(
        default=None, alias="lexTranscriptFilter"
    )


class ExternalSourceSettingModel(BaseModel):
    grammar_slot_type_setting: Optional[GrammarSlotTypeSettingModel] = Field(
        default=None, alias="grammarSlotTypeSetting"
    )


class ListAggregatedUtterancesRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    locale_id: str = Field(alias="localeId")
    aggregation_duration: UtteranceAggregationDurationModel = Field(
        alias="aggregationDuration"
    )
    bot_alias_id: Optional[str] = Field(default=None, alias="botAliasId")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    sort_by: Optional[AggregatedUtterancesSortByModel] = Field(
        default=None, alias="sortBy"
    )
    filters: Optional[Sequence[AggregatedUtterancesFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAggregatedUtterancesResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_alias_id: str = Field(alias="botAliasId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    aggregation_duration: UtteranceAggregationDurationModel = Field(
        alias="aggregationDuration"
    )
    aggregation_window_start_time: datetime = Field(alias="aggregationWindowStartTime")
    aggregation_window_end_time: datetime = Field(alias="aggregationWindowEndTime")
    aggregation_last_refreshed_date_time: datetime = Field(
        alias="aggregationLastRefreshedDateTime"
    )
    aggregated_utterances_summaries: List[AggregatedUtterancesSummaryModel] = Field(
        alias="aggregatedUtterancesSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImportResponseModel(BaseModel):
    import_id: str = Field(alias="importId")
    resource_specification: ImportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    imported_resource_id: str = Field(alias="importedResourceId")
    imported_resource_name: str = Field(alias="importedResourceName")
    merge_strategy: Literal["Append", "FailOnConflict", "Overwrite"] = Field(
        alias="mergeStrategy"
    )
    import_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="importStatus"
    )
    failure_reasons: List[str] = Field(alias="failureReasons")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportRequestModel(BaseModel):
    import_id: str = Field(alias="importId")
    resource_specification: ImportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    merge_strategy: Literal["Append", "FailOnConflict", "Overwrite"] = Field(
        alias="mergeStrategy"
    )
    file_password: Optional[str] = Field(default=None, alias="filePassword")


class StartImportResponseModel(BaseModel):
    import_id: str = Field(alias="importId")
    resource_specification: ImportResourceSpecificationModel = Field(
        alias="resourceSpecification"
    )
    merge_strategy: Literal["Append", "FailOnConflict", "Overwrite"] = Field(
        alias="mergeStrategy"
    )
    import_status: Literal["Completed", "Deleting", "Failed", "InProgress"] = Field(
        alias="importStatus"
    )
    creation_date_time: datetime = Field(alias="creationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MessageGroupModel(BaseModel):
    message: MessageModel = Field(alias="message")
    variations: Optional[Sequence[MessageModel]] = Field(
        default=None, alias="variations"
    )


class ConversationLogSettingsModel(BaseModel):
    text_log_settings: Optional[Sequence[TextLogSettingModel]] = Field(
        default=None, alias="textLogSettings"
    )
    audio_log_settings: Optional[Sequence[AudioLogSettingModel]] = Field(
        default=None, alias="audioLogSettings"
    )


class ListExportsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    export_summaries: List[ExportSummaryModel] = Field(alias="exportSummaries")
    next_token: str = Field(alias="nextToken")
    locale_id: str = Field(alias="localeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3BucketTranscriptSourceModel(BaseModel):
    s3_bucket_name: str = Field(alias="s3BucketName")
    transcript_format: Literal["Lex"] = Field(alias="transcriptFormat")
    path_format: Optional[PathFormatModel] = Field(default=None, alias="pathFormat")
    transcript_filter: Optional[TranscriptFilterModel] = Field(
        default=None, alias="transcriptFilter"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class CreateSlotTypeRequestModel(BaseModel):
    slot_type_name: str = Field(alias="slotTypeName")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    description: Optional[str] = Field(default=None, alias="description")
    slot_type_values: Optional[Sequence[SlotTypeValueModel]] = Field(
        default=None, alias="slotTypeValues"
    )
    value_selection_setting: Optional[SlotValueSelectionSettingModel] = Field(
        default=None, alias="valueSelectionSetting"
    )
    parent_slot_type_signature: Optional[str] = Field(
        default=None, alias="parentSlotTypeSignature"
    )
    external_source_setting: Optional[ExternalSourceSettingModel] = Field(
        default=None, alias="externalSourceSetting"
    )
    composite_slot_type_setting: Optional[CompositeSlotTypeSettingModel] = Field(
        default=None, alias="compositeSlotTypeSetting"
    )


class CreateSlotTypeResponseModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    slot_type_name: str = Field(alias="slotTypeName")
    description: str = Field(alias="description")
    slot_type_values: List[SlotTypeValueModel] = Field(alias="slotTypeValues")
    value_selection_setting: SlotValueSelectionSettingModel = Field(
        alias="valueSelectionSetting"
    )
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    external_source_setting: ExternalSourceSettingModel = Field(
        alias="externalSourceSetting"
    )
    composite_slot_type_setting: CompositeSlotTypeSettingModel = Field(
        alias="compositeSlotTypeSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSlotTypeResponseModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    slot_type_name: str = Field(alias="slotTypeName")
    description: str = Field(alias="description")
    slot_type_values: List[SlotTypeValueModel] = Field(alias="slotTypeValues")
    value_selection_setting: SlotValueSelectionSettingModel = Field(
        alias="valueSelectionSetting"
    )
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    external_source_setting: ExternalSourceSettingModel = Field(
        alias="externalSourceSetting"
    )
    composite_slot_type_setting: CompositeSlotTypeSettingModel = Field(
        alias="compositeSlotTypeSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSlotTypeRequestModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    slot_type_name: str = Field(alias="slotTypeName")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    description: Optional[str] = Field(default=None, alias="description")
    slot_type_values: Optional[Sequence[SlotTypeValueModel]] = Field(
        default=None, alias="slotTypeValues"
    )
    value_selection_setting: Optional[SlotValueSelectionSettingModel] = Field(
        default=None, alias="valueSelectionSetting"
    )
    parent_slot_type_signature: Optional[str] = Field(
        default=None, alias="parentSlotTypeSignature"
    )
    external_source_setting: Optional[ExternalSourceSettingModel] = Field(
        default=None, alias="externalSourceSetting"
    )
    composite_slot_type_setting: Optional[CompositeSlotTypeSettingModel] = Field(
        default=None, alias="compositeSlotTypeSetting"
    )


class UpdateSlotTypeResponseModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    slot_type_name: str = Field(alias="slotTypeName")
    description: str = Field(alias="description")
    slot_type_values: List[SlotTypeValueModel] = Field(alias="slotTypeValues")
    value_selection_setting: SlotValueSelectionSettingModel = Field(
        alias="valueSelectionSetting"
    )
    parent_slot_type_signature: str = Field(alias="parentSlotTypeSignature")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    external_source_setting: ExternalSourceSettingModel = Field(
        alias="externalSourceSetting"
    )
    composite_slot_type_setting: CompositeSlotTypeSettingModel = Field(
        alias="compositeSlotTypeSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FulfillmentStartResponseSpecificationModel(BaseModel):
    delay_in_seconds: int = Field(alias="delayInSeconds")
    message_groups: Sequence[MessageGroupModel] = Field(alias="messageGroups")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")


class FulfillmentUpdateResponseSpecificationModel(BaseModel):
    frequency_in_seconds: int = Field(alias="frequencyInSeconds")
    message_groups: Sequence[MessageGroupModel] = Field(alias="messageGroups")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")


class PromptSpecificationModel(BaseModel):
    message_groups: Sequence[MessageGroupModel] = Field(alias="messageGroups")
    max_retries: int = Field(alias="maxRetries")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")
    message_selection_strategy: Optional[Literal["Ordered", "Random"]] = Field(
        default=None, alias="messageSelectionStrategy"
    )
    prompt_attempts_specification: Optional[
        Mapping[
            Literal["Initial", "Retry1", "Retry2", "Retry3", "Retry4", "Retry5"],
            PromptAttemptSpecificationModel,
        ]
    ] = Field(default=None, alias="promptAttemptsSpecification")


class ResponseSpecificationModel(BaseModel):
    message_groups: Sequence[MessageGroupModel] = Field(alias="messageGroups")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")


class StillWaitingResponseSpecificationModel(BaseModel):
    message_groups: Sequence[MessageGroupModel] = Field(alias="messageGroups")
    frequency_in_seconds: int = Field(alias="frequencyInSeconds")
    timeout_in_seconds: int = Field(alias="timeoutInSeconds")
    allow_interrupt: Optional[bool] = Field(default=None, alias="allowInterrupt")


class CreateBotAliasRequestModel(BaseModel):
    bot_alias_name: str = Field(alias="botAliasName")
    bot_id: str = Field(alias="botId")
    description: Optional[str] = Field(default=None, alias="description")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    bot_alias_locale_settings: Optional[
        Mapping[str, BotAliasLocaleSettingsModel]
    ] = Field(default=None, alias="botAliasLocaleSettings")
    conversation_log_settings: Optional[ConversationLogSettingsModel] = Field(
        default=None, alias="conversationLogSettings"
    )
    sentiment_analysis_settings: Optional[SentimentAnalysisSettingsModel] = Field(
        default=None, alias="sentimentAnalysisSettings"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateBotAliasResponseModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_alias_name: str = Field(alias="botAliasName")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_alias_locale_settings: Dict[str, BotAliasLocaleSettingsModel] = Field(
        alias="botAliasLocaleSettings"
    )
    conversation_log_settings: ConversationLogSettingsModel = Field(
        alias="conversationLogSettings"
    )
    sentiment_analysis_settings: SentimentAnalysisSettingsModel = Field(
        alias="sentimentAnalysisSettings"
    )
    bot_alias_status: Literal["Available", "Creating", "Deleting", "Failed"] = Field(
        alias="botAliasStatus"
    )
    bot_id: str = Field(alias="botId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBotAliasResponseModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_alias_name: str = Field(alias="botAliasName")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_alias_locale_settings: Dict[str, BotAliasLocaleSettingsModel] = Field(
        alias="botAliasLocaleSettings"
    )
    conversation_log_settings: ConversationLogSettingsModel = Field(
        alias="conversationLogSettings"
    )
    sentiment_analysis_settings: SentimentAnalysisSettingsModel = Field(
        alias="sentimentAnalysisSettings"
    )
    bot_alias_history_events: List[BotAliasHistoryEventModel] = Field(
        alias="botAliasHistoryEvents"
    )
    bot_alias_status: Literal["Available", "Creating", "Deleting", "Failed"] = Field(
        alias="botAliasStatus"
    )
    bot_id: str = Field(alias="botId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    parent_bot_networks: List[ParentBotNetworkModel] = Field(alias="parentBotNetworks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotAliasRequestModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_alias_name: str = Field(alias="botAliasName")
    bot_id: str = Field(alias="botId")
    description: Optional[str] = Field(default=None, alias="description")
    bot_version: Optional[str] = Field(default=None, alias="botVersion")
    bot_alias_locale_settings: Optional[
        Mapping[str, BotAliasLocaleSettingsModel]
    ] = Field(default=None, alias="botAliasLocaleSettings")
    conversation_log_settings: Optional[ConversationLogSettingsModel] = Field(
        default=None, alias="conversationLogSettings"
    )
    sentiment_analysis_settings: Optional[SentimentAnalysisSettingsModel] = Field(
        default=None, alias="sentimentAnalysisSettings"
    )


class UpdateBotAliasResponseModel(BaseModel):
    bot_alias_id: str = Field(alias="botAliasId")
    bot_alias_name: str = Field(alias="botAliasName")
    description: str = Field(alias="description")
    bot_version: str = Field(alias="botVersion")
    bot_alias_locale_settings: Dict[str, BotAliasLocaleSettingsModel] = Field(
        alias="botAliasLocaleSettings"
    )
    conversation_log_settings: ConversationLogSettingsModel = Field(
        alias="conversationLogSettings"
    )
    sentiment_analysis_settings: SentimentAnalysisSettingsModel = Field(
        alias="sentimentAnalysisSettings"
    )
    bot_alias_status: Literal["Available", "Creating", "Deleting", "Failed"] = Field(
        alias="botAliasStatus"
    )
    bot_id: str = Field(alias="botId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TranscriptSourceSettingModel(BaseModel):
    s3_bucket_transcript_source: Optional[S3BucketTranscriptSourceModel] = Field(
        default=None, alias="s3BucketTranscriptSource"
    )


class FulfillmentUpdatesSpecificationModel(BaseModel):
    active: bool = Field(alias="active")
    start_response: Optional[FulfillmentStartResponseSpecificationModel] = Field(
        default=None, alias="startResponse"
    )
    update_response: Optional[FulfillmentUpdateResponseSpecificationModel] = Field(
        default=None, alias="updateResponse"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")


class SlotSummaryModel(BaseModel):
    slot_id: Optional[str] = Field(default=None, alias="slotId")
    slot_name: Optional[str] = Field(default=None, alias="slotName")
    description: Optional[str] = Field(default=None, alias="description")
    slot_constraint: Optional[Literal["Optional", "Required"]] = Field(
        default=None, alias="slotConstraint"
    )
    slot_type_id: Optional[str] = Field(default=None, alias="slotTypeId")
    value_elicitation_prompt_specification: Optional[PromptSpecificationModel] = Field(
        default=None, alias="valueElicitationPromptSpecification"
    )
    last_updated_date_time: Optional[datetime] = Field(
        default=None, alias="lastUpdatedDateTime"
    )


class ConditionalBranchModel(BaseModel):
    name: str = Field(alias="name")
    condition: ConditionModel = Field(alias="condition")
    next_step: DialogStateModel = Field(alias="nextStep")
    response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="response"
    )


class DefaultConditionalBranchModel(BaseModel):
    next_step: Optional[DialogStateModel] = Field(default=None, alias="nextStep")
    response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="response"
    )


class WaitAndContinueSpecificationModel(BaseModel):
    waiting_response: ResponseSpecificationModel = Field(alias="waitingResponse")
    continue_response: ResponseSpecificationModel = Field(alias="continueResponse")
    still_waiting_response: Optional[StillWaitingResponseSpecificationModel] = Field(
        default=None, alias="stillWaitingResponse"
    )
    active: Optional[bool] = Field(default=None, alias="active")


class DescribeBotRecommendationResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_status: Literal[
        "Available",
        "Deleted",
        "Deleting",
        "Downloading",
        "Failed",
        "Processing",
        "Stopped",
        "Stopping",
        "Updating",
    ] = Field(alias="botRecommendationStatus")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    failure_reasons: List[str] = Field(alias="failureReasons")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    transcript_source_setting: TranscriptSourceSettingModel = Field(
        alias="transcriptSourceSetting"
    )
    encryption_setting: EncryptionSettingModel = Field(alias="encryptionSetting")
    bot_recommendation_results: BotRecommendationResultsModel = Field(
        alias="botRecommendationResults"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBotRecommendationRequestModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    transcript_source_setting: TranscriptSourceSettingModel = Field(
        alias="transcriptSourceSetting"
    )
    encryption_setting: Optional[EncryptionSettingModel] = Field(
        default=None, alias="encryptionSetting"
    )


class StartBotRecommendationResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_status: Literal[
        "Available",
        "Deleted",
        "Deleting",
        "Downloading",
        "Failed",
        "Processing",
        "Stopped",
        "Stopping",
        "Updating",
    ] = Field(alias="botRecommendationStatus")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    transcript_source_setting: TranscriptSourceSettingModel = Field(
        alias="transcriptSourceSetting"
    )
    encryption_setting: EncryptionSettingModel = Field(alias="encryptionSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBotRecommendationResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    bot_recommendation_status: Literal[
        "Available",
        "Deleted",
        "Deleting",
        "Downloading",
        "Failed",
        "Processing",
        "Stopped",
        "Stopping",
        "Updating",
    ] = Field(alias="botRecommendationStatus")
    bot_recommendation_id: str = Field(alias="botRecommendationId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    transcript_source_setting: TranscriptSourceSettingModel = Field(
        alias="transcriptSourceSetting"
    )
    encryption_setting: EncryptionSettingModel = Field(alias="encryptionSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSlotsResponseModel(BaseModel):
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    slot_summaries: List[SlotSummaryModel] = Field(alias="slotSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConditionalSpecificationModel(BaseModel):
    active: bool = Field(alias="active")
    conditional_branches: Sequence[ConditionalBranchModel] = Field(
        alias="conditionalBranches"
    )
    default_branch: DefaultConditionalBranchModel = Field(alias="defaultBranch")


class SubSlotValueElicitationSettingModel(BaseModel):
    prompt_specification: PromptSpecificationModel = Field(alias="promptSpecification")
    default_value_specification: Optional[SlotDefaultValueSpecificationModel] = Field(
        default=None, alias="defaultValueSpecification"
    )
    sample_utterances: Optional[Sequence[SampleUtteranceModel]] = Field(
        default=None, alias="sampleUtterances"
    )
    wait_and_continue_specification: Optional[
        WaitAndContinueSpecificationModel
    ] = Field(default=None, alias="waitAndContinueSpecification")


class IntentClosingSettingModel(BaseModel):
    closing_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="closingResponse"
    )
    active: Optional[bool] = Field(default=None, alias="active")
    next_step: Optional[DialogStateModel] = Field(default=None, alias="nextStep")
    conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="conditional"
    )


class PostDialogCodeHookInvocationSpecificationModel(BaseModel):
    success_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="successResponse"
    )
    success_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="successNextStep"
    )
    success_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="successConditional"
    )
    failure_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="failureResponse"
    )
    failure_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="failureNextStep"
    )
    failure_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="failureConditional"
    )
    timeout_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="timeoutResponse"
    )
    timeout_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="timeoutNextStep"
    )
    timeout_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="timeoutConditional"
    )


class PostFulfillmentStatusSpecificationModel(BaseModel):
    success_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="successResponse"
    )
    failure_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="failureResponse"
    )
    timeout_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="timeoutResponse"
    )
    success_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="successNextStep"
    )
    success_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="successConditional"
    )
    failure_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="failureNextStep"
    )
    failure_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="failureConditional"
    )
    timeout_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="timeoutNextStep"
    )
    timeout_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="timeoutConditional"
    )


class SpecificationsModel(BaseModel):
    slot_type_id: str = Field(alias="slotTypeId")
    value_elicitation_setting: SubSlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )


class DialogCodeHookInvocationSettingModel(BaseModel):
    enable_code_hook_invocation: bool = Field(alias="enableCodeHookInvocation")
    active: bool = Field(alias="active")
    post_code_hook_specification: PostDialogCodeHookInvocationSpecificationModel = (
        Field(alias="postCodeHookSpecification")
    )
    invocation_label: Optional[str] = Field(default=None, alias="invocationLabel")


class FulfillmentCodeHookSettingsModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    post_fulfillment_status_specification: Optional[
        PostFulfillmentStatusSpecificationModel
    ] = Field(default=None, alias="postFulfillmentStatusSpecification")
    fulfillment_updates_specification: Optional[
        FulfillmentUpdatesSpecificationModel
    ] = Field(default=None, alias="fulfillmentUpdatesSpecification")
    active: Optional[bool] = Field(default=None, alias="active")


class SubSlotSettingModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="expression")
    slot_specifications: Optional[Mapping[str, SpecificationsModel]] = Field(
        default=None, alias="slotSpecifications"
    )


class InitialResponseSettingModel(BaseModel):
    initial_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="initialResponse"
    )
    next_step: Optional[DialogStateModel] = Field(default=None, alias="nextStep")
    conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="conditional"
    )
    code_hook: Optional[DialogCodeHookInvocationSettingModel] = Field(
        default=None, alias="codeHook"
    )


class IntentConfirmationSettingModel(BaseModel):
    prompt_specification: PromptSpecificationModel = Field(alias="promptSpecification")
    declination_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="declinationResponse"
    )
    active: Optional[bool] = Field(default=None, alias="active")
    confirmation_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="confirmationResponse"
    )
    confirmation_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="confirmationNextStep"
    )
    confirmation_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="confirmationConditional"
    )
    declination_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="declinationNextStep"
    )
    declination_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="declinationConditional"
    )
    failure_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="failureResponse"
    )
    failure_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="failureNextStep"
    )
    failure_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="failureConditional"
    )
    code_hook: Optional[DialogCodeHookInvocationSettingModel] = Field(
        default=None, alias="codeHook"
    )
    elicitation_code_hook: Optional[ElicitationCodeHookInvocationSettingModel] = Field(
        default=None, alias="elicitationCodeHook"
    )


class SlotCaptureSettingModel(BaseModel):
    capture_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="captureResponse"
    )
    capture_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="captureNextStep"
    )
    capture_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="captureConditional"
    )
    failure_response: Optional[ResponseSpecificationModel] = Field(
        default=None, alias="failureResponse"
    )
    failure_next_step: Optional[DialogStateModel] = Field(
        default=None, alias="failureNextStep"
    )
    failure_conditional: Optional[ConditionalSpecificationModel] = Field(
        default=None, alias="failureConditional"
    )
    code_hook: Optional[DialogCodeHookInvocationSettingModel] = Field(
        default=None, alias="codeHook"
    )
    elicitation_code_hook: Optional[ElicitationCodeHookInvocationSettingModel] = Field(
        default=None, alias="elicitationCodeHook"
    )


class CreateIntentRequestModel(BaseModel):
    intent_name: str = Field(alias="intentName")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    description: Optional[str] = Field(default=None, alias="description")
    parent_intent_signature: Optional[str] = Field(
        default=None, alias="parentIntentSignature"
    )
    sample_utterances: Optional[Sequence[SampleUtteranceModel]] = Field(
        default=None, alias="sampleUtterances"
    )
    dialog_code_hook: Optional[DialogCodeHookSettingsModel] = Field(
        default=None, alias="dialogCodeHook"
    )
    fulfillment_code_hook: Optional[FulfillmentCodeHookSettingsModel] = Field(
        default=None, alias="fulfillmentCodeHook"
    )
    intent_confirmation_setting: Optional[IntentConfirmationSettingModel] = Field(
        default=None, alias="intentConfirmationSetting"
    )
    intent_closing_setting: Optional[IntentClosingSettingModel] = Field(
        default=None, alias="intentClosingSetting"
    )
    input_contexts: Optional[Sequence[InputContextModel]] = Field(
        default=None, alias="inputContexts"
    )
    output_contexts: Optional[Sequence[OutputContextModel]] = Field(
        default=None, alias="outputContexts"
    )
    kendra_configuration: Optional[KendraConfigurationModel] = Field(
        default=None, alias="kendraConfiguration"
    )
    initial_response_setting: Optional[InitialResponseSettingModel] = Field(
        default=None, alias="initialResponseSetting"
    )


class CreateIntentResponseModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    intent_name: str = Field(alias="intentName")
    description: str = Field(alias="description")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    sample_utterances: List[SampleUtteranceModel] = Field(alias="sampleUtterances")
    dialog_code_hook: DialogCodeHookSettingsModel = Field(alias="dialogCodeHook")
    fulfillment_code_hook: FulfillmentCodeHookSettingsModel = Field(
        alias="fulfillmentCodeHook"
    )
    intent_confirmation_setting: IntentConfirmationSettingModel = Field(
        alias="intentConfirmationSetting"
    )
    intent_closing_setting: IntentClosingSettingModel = Field(
        alias="intentClosingSetting"
    )
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    initial_response_setting: InitialResponseSettingModel = Field(
        alias="initialResponseSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIntentResponseModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    intent_name: str = Field(alias="intentName")
    description: str = Field(alias="description")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    sample_utterances: List[SampleUtteranceModel] = Field(alias="sampleUtterances")
    dialog_code_hook: DialogCodeHookSettingsModel = Field(alias="dialogCodeHook")
    fulfillment_code_hook: FulfillmentCodeHookSettingsModel = Field(
        alias="fulfillmentCodeHook"
    )
    slot_priorities: List[SlotPriorityModel] = Field(alias="slotPriorities")
    intent_confirmation_setting: IntentConfirmationSettingModel = Field(
        alias="intentConfirmationSetting"
    )
    intent_closing_setting: IntentClosingSettingModel = Field(
        alias="intentClosingSetting"
    )
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    initial_response_setting: InitialResponseSettingModel = Field(
        alias="initialResponseSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIntentRequestModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    intent_name: str = Field(alias="intentName")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    description: Optional[str] = Field(default=None, alias="description")
    parent_intent_signature: Optional[str] = Field(
        default=None, alias="parentIntentSignature"
    )
    sample_utterances: Optional[Sequence[SampleUtteranceModel]] = Field(
        default=None, alias="sampleUtterances"
    )
    dialog_code_hook: Optional[DialogCodeHookSettingsModel] = Field(
        default=None, alias="dialogCodeHook"
    )
    fulfillment_code_hook: Optional[FulfillmentCodeHookSettingsModel] = Field(
        default=None, alias="fulfillmentCodeHook"
    )
    slot_priorities: Optional[Sequence[SlotPriorityModel]] = Field(
        default=None, alias="slotPriorities"
    )
    intent_confirmation_setting: Optional[IntentConfirmationSettingModel] = Field(
        default=None, alias="intentConfirmationSetting"
    )
    intent_closing_setting: Optional[IntentClosingSettingModel] = Field(
        default=None, alias="intentClosingSetting"
    )
    input_contexts: Optional[Sequence[InputContextModel]] = Field(
        default=None, alias="inputContexts"
    )
    output_contexts: Optional[Sequence[OutputContextModel]] = Field(
        default=None, alias="outputContexts"
    )
    kendra_configuration: Optional[KendraConfigurationModel] = Field(
        default=None, alias="kendraConfiguration"
    )
    initial_response_setting: Optional[InitialResponseSettingModel] = Field(
        default=None, alias="initialResponseSetting"
    )


class UpdateIntentResponseModel(BaseModel):
    intent_id: str = Field(alias="intentId")
    intent_name: str = Field(alias="intentName")
    description: str = Field(alias="description")
    parent_intent_signature: str = Field(alias="parentIntentSignature")
    sample_utterances: List[SampleUtteranceModel] = Field(alias="sampleUtterances")
    dialog_code_hook: DialogCodeHookSettingsModel = Field(alias="dialogCodeHook")
    fulfillment_code_hook: FulfillmentCodeHookSettingsModel = Field(
        alias="fulfillmentCodeHook"
    )
    slot_priorities: List[SlotPriorityModel] = Field(alias="slotPriorities")
    intent_confirmation_setting: IntentConfirmationSettingModel = Field(
        alias="intentConfirmationSetting"
    )
    intent_closing_setting: IntentClosingSettingModel = Field(
        alias="intentClosingSetting"
    )
    input_contexts: List[InputContextModel] = Field(alias="inputContexts")
    output_contexts: List[OutputContextModel] = Field(alias="outputContexts")
    kendra_configuration: KendraConfigurationModel = Field(alias="kendraConfiguration")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    initial_response_setting: InitialResponseSettingModel = Field(
        alias="initialResponseSetting"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SlotValueElicitationSettingModel(BaseModel):
    slot_constraint: Literal["Optional", "Required"] = Field(alias="slotConstraint")
    default_value_specification: Optional[SlotDefaultValueSpecificationModel] = Field(
        default=None, alias="defaultValueSpecification"
    )
    prompt_specification: Optional[PromptSpecificationModel] = Field(
        default=None, alias="promptSpecification"
    )
    sample_utterances: Optional[Sequence[SampleUtteranceModel]] = Field(
        default=None, alias="sampleUtterances"
    )
    wait_and_continue_specification: Optional[
        WaitAndContinueSpecificationModel
    ] = Field(default=None, alias="waitAndContinueSpecification")
    slot_capture_setting: Optional[SlotCaptureSettingModel] = Field(
        default=None, alias="slotCaptureSetting"
    )


class CreateSlotRequestModel(BaseModel):
    slot_name: str = Field(alias="slotName")
    value_elicitation_setting: SlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    description: Optional[str] = Field(default=None, alias="description")
    slot_type_id: Optional[str] = Field(default=None, alias="slotTypeId")
    obfuscation_setting: Optional[ObfuscationSettingModel] = Field(
        default=None, alias="obfuscationSetting"
    )
    multiple_values_setting: Optional[MultipleValuesSettingModel] = Field(
        default=None, alias="multipleValuesSetting"
    )
    sub_slot_setting: Optional[SubSlotSettingModel] = Field(
        default=None, alias="subSlotSetting"
    )


class CreateSlotResponseModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    slot_name: str = Field(alias="slotName")
    description: str = Field(alias="description")
    slot_type_id: str = Field(alias="slotTypeId")
    value_elicitation_setting: SlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )
    obfuscation_setting: ObfuscationSettingModel = Field(alias="obfuscationSetting")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    multiple_values_setting: MultipleValuesSettingModel = Field(
        alias="multipleValuesSetting"
    )
    sub_slot_setting: SubSlotSettingModel = Field(alias="subSlotSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSlotResponseModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    slot_name: str = Field(alias="slotName")
    description: str = Field(alias="description")
    slot_type_id: str = Field(alias="slotTypeId")
    value_elicitation_setting: SlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )
    obfuscation_setting: ObfuscationSettingModel = Field(alias="obfuscationSetting")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    multiple_values_setting: MultipleValuesSettingModel = Field(
        alias="multipleValuesSetting"
    )
    sub_slot_setting: SubSlotSettingModel = Field(alias="subSlotSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSlotRequestModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    slot_name: str = Field(alias="slotName")
    value_elicitation_setting: SlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    description: Optional[str] = Field(default=None, alias="description")
    slot_type_id: Optional[str] = Field(default=None, alias="slotTypeId")
    obfuscation_setting: Optional[ObfuscationSettingModel] = Field(
        default=None, alias="obfuscationSetting"
    )
    multiple_values_setting: Optional[MultipleValuesSettingModel] = Field(
        default=None, alias="multipleValuesSetting"
    )
    sub_slot_setting: Optional[SubSlotSettingModel] = Field(
        default=None, alias="subSlotSetting"
    )


class UpdateSlotResponseModel(BaseModel):
    slot_id: str = Field(alias="slotId")
    slot_name: str = Field(alias="slotName")
    description: str = Field(alias="description")
    slot_type_id: str = Field(alias="slotTypeId")
    value_elicitation_setting: SlotValueElicitationSettingModel = Field(
        alias="valueElicitationSetting"
    )
    obfuscation_setting: ObfuscationSettingModel = Field(alias="obfuscationSetting")
    bot_id: str = Field(alias="botId")
    bot_version: str = Field(alias="botVersion")
    locale_id: str = Field(alias="localeId")
    intent_id: str = Field(alias="intentId")
    creation_date_time: datetime = Field(alias="creationDateTime")
    last_updated_date_time: datetime = Field(alias="lastUpdatedDateTime")
    multiple_values_setting: MultipleValuesSettingModel = Field(
        alias="multipleValuesSetting"
    )
    sub_slot_setting: SubSlotSettingModel = Field(alias="subSlotSetting")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
