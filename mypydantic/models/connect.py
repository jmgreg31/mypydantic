# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionSummaryModel(BaseModel):
    action_type: Literal[
        "ASSIGN_CONTACT_CATEGORY",
        "CREATE_TASK",
        "GENERATE_EVENTBRIDGE_EVENT",
        "SEND_NOTIFICATION",
    ] = Field(alias="ActionType")


class QueueReferenceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class AgentInfoModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    connected_to_agent_timestamp: Optional[datetime] = Field(
        default=None, alias="ConnectedToAgentTimestamp"
    )


class AgentStatusReferenceModel(BaseModel):
    status_start_timestamp: Optional[datetime] = Field(
        default=None, alias="StatusStartTimestamp"
    )
    status_arn: Optional[str] = Field(default=None, alias="StatusArn")
    status_name: Optional[str] = Field(default=None, alias="StatusName")


class AgentStatusSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["CUSTOM", "OFFLINE", "ROUTABLE"]] = Field(
        default=None, alias="Type"
    )


class AgentStatusModel(BaseModel):
    agent_status_arn: Optional[str] = Field(default=None, alias="AgentStatusARN")
    agent_status_id: Optional[str] = Field(default=None, alias="AgentStatusId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["CUSTOM", "OFFLINE", "ROUTABLE"]] = Field(
        default=None, alias="Type"
    )
    display_order: Optional[int] = Field(default=None, alias="DisplayOrder")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class AnswerMachineDetectionConfigModel(BaseModel):
    enable_answer_machine_detection: Optional[bool] = Field(
        default=None, alias="EnableAnswerMachineDetection"
    )
    await_answer_machine_prompt: Optional[bool] = Field(
        default=None, alias="AwaitAnswerMachinePrompt"
    )


class AssociateApprovedOriginRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    origin: str = Field(alias="Origin")


class LexBotModel(BaseModel):
    name: str = Field(alias="Name")
    lex_region: str = Field(alias="LexRegion")


class LexV2BotModel(BaseModel):
    alias_arn: Optional[str] = Field(default=None, alias="AliasArn")


class AssociateDefaultVocabularyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    language_code: Literal[
        "ar-AE",
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
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "pt-PT",
        "zh-CN",
    ] = Field(alias="LanguageCode")
    vocabulary_id: Optional[str] = Field(default=None, alias="VocabularyId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateLambdaFunctionRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    function_arn: str = Field(alias="FunctionArn")


class AssociatePhoneNumberContactFlowRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")


class AssociateQueueQuickConnectsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    quick_connect_ids: Sequence[str] = Field(alias="QuickConnectIds")


class AssociateSecurityKeyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    key: str = Field(alias="Key")


class AttachmentReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")
    status: Optional[Literal["APPROVED", "REJECTED"]] = Field(
        default=None, alias="Status"
    )


class AttributeModel(BaseModel):
    attribute_type: Optional[
        Literal[
            "AUTO_RESOLVE_BEST_VOICES",
            "CONTACTFLOW_LOGS",
            "CONTACT_LENS",
            "EARLY_MEDIA",
            "ENHANCED_CONTACT_MONITORING",
            "HIGH_VOLUME_OUTBOUND",
            "INBOUND_CALLS",
            "MULTI_PARTY_CONFERENCE",
            "OUTBOUND_CALLS",
            "USE_CUSTOM_TTS_VOICES",
        ]
    ] = Field(default=None, alias="AttributeType")
    value: Optional[str] = Field(default=None, alias="Value")


class AvailableNumberSummaryModel(BaseModel):
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_number_country_code: Optional[
        Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "Type[IO]",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCode")
    phone_number_type: Optional[Literal["DID", "TOLL_FREE"]] = Field(
        default=None, alias="PhoneNumberType"
    )


class ChatMessageModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    content: str = Field(alias="Content")


class ChatStreamingConfigurationModel(BaseModel):
    streaming_endpoint_arn: str = Field(alias="StreamingEndpointArn")


class ClaimPhoneNumberRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    phone_number: str = Field(alias="PhoneNumber")
    phone_number_description: Optional[str] = Field(
        default=None, alias="PhoneNumberDescription"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class PhoneNumberStatusModel(BaseModel):
    status: Optional[Literal["CLAIMED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="Status"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class ContactFilterModel(BaseModel):
    contact_states: Optional[
        Sequence[
            Literal[
                "CONNECTED",
                "CONNECTED_ONHOLD",
                "CONNECTING",
                "ENDED",
                "ERROR",
                "INCOMING",
                "MISSED",
                "PENDING",
                "REJECTED",
            ]
        ]
    ] = Field(default=None, alias="ContactStates")


class ContactFlowModuleSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias="State")


class ContactFlowModuleModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    content: Optional[str] = Field(default=None, alias="Content")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias="State")
    status: Optional[Literal["PUBLISHED", "SAVED"]] = Field(
        default=None, alias="Status"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ContactFlowSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    contact_flow_type: Optional[
        Literal[
            "AGENT_HOLD",
            "AGENT_TRANSFER",
            "AGENT_WHISPER",
            "CONTACT_FLOW",
            "CUSTOMER_HOLD",
            "CUSTOMER_QUEUE",
            "CUSTOMER_WHISPER",
            "OUTBOUND_WHISPER",
            "QUEUE_TRANSFER",
        ]
    ] = Field(default=None, alias="ContactFlowType")
    contact_flow_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="ContactFlowState"
    )


class ContactFlowModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[
        Literal[
            "AGENT_HOLD",
            "AGENT_TRANSFER",
            "AGENT_WHISPER",
            "CONTACT_FLOW",
            "CUSTOMER_HOLD",
            "CUSTOMER_QUEUE",
            "CUSTOMER_WHISPER",
            "OUTBOUND_WHISPER",
            "QUEUE_TRANSFER",
        ]
    ] = Field(default=None, alias="Type")
    state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    content: Optional[str] = Field(default=None, alias="Content")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class QueueInfoModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    enqueue_timestamp: Optional[datetime] = Field(
        default=None, alias="EnqueueTimestamp"
    )


class WisdomInfoModel(BaseModel):
    session_arn: Optional[str] = Field(default=None, alias="SessionArn")


class TagConditionModel(BaseModel):
    tag_key: Optional[str] = Field(default=None, alias="TagKey")
    tag_value: Optional[str] = Field(default=None, alias="TagValue")


class CreateAgentStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    display_order: Optional[int] = Field(default=None, alias="DisplayOrder")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateContactFlowModuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    content: str = Field(alias="Content")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateContactFlowRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    type: Literal[
        "AGENT_HOLD",
        "AGENT_TRANSFER",
        "AGENT_WHISPER",
        "CONTACT_FLOW",
        "CUSTOMER_HOLD",
        "CUSTOMER_QUEUE",
        "CUSTOMER_WHISPER",
        "OUTBOUND_WHISPER",
        "QUEUE_TRANSFER",
    ] = Field(alias="Type")
    content: str = Field(alias="Content")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateInstanceRequestModel(BaseModel):
    identity_management_type: Literal[
        "CONNECT_MANAGED", "EXISTING_DIRECTORY", "SAML"
    ] = Field(alias="IdentityManagementType")
    inbound_calls_enabled: bool = Field(alias="InboundCallsEnabled")
    outbound_calls_enabled: bool = Field(alias="OutboundCallsEnabled")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    instance_alias: Optional[str] = Field(default=None, alias="InstanceAlias")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")


class CreateIntegrationAssociationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_type: Literal[
        "CASES_DOMAIN",
        "EVENT",
        "PINPOINT_APP",
        "VOICE_ID",
        "WISDOM_ASSISTANT",
        "WISDOM_KNOWLEDGE_BASE",
    ] = Field(alias="IntegrationType")
    integration_arn: str = Field(alias="IntegrationArn")
    source_application_url: Optional[str] = Field(
        default=None, alias="SourceApplicationUrl"
    )
    source_application_name: Optional[str] = Field(
        default=None, alias="SourceApplicationName"
    )
    source_type: Optional[Literal["SALESFORCE", "ZENDESK"]] = Field(
        default=None, alias="SourceType"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class OutboundCallerConfigModel(BaseModel):
    outbound_caller_id_name: Optional[str] = Field(
        default=None, alias="OutboundCallerIdName"
    )
    outbound_caller_id_number_id: Optional[str] = Field(
        default=None, alias="OutboundCallerIdNumberId"
    )
    outbound_flow_id: Optional[str] = Field(default=None, alias="OutboundFlowId")


class MediaConcurrencyModel(BaseModel):
    channel: Literal["CHAT", "TASK", "VOICE"] = Field(alias="Channel")
    concurrency: int = Field(alias="Concurrency")


class RuleTriggerEventSourceModel(BaseModel):
    event_source_name: Literal[
        "OnPostCallAnalysisAvailable",
        "OnPostChatAnalysisAvailable",
        "OnRealTimeCallAnalysisAvailable",
        "OnSalesforceCaseCreate",
        "OnZendeskTicketCreate",
        "OnZendeskTicketStatusUpdate",
    ] = Field(alias="EventSourceName")
    integration_association_id: Optional[str] = Field(
        default=None, alias="IntegrationAssociationId"
    )


class CreateSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="SecurityProfileName")
    instance_id: str = Field(alias="InstanceId")
    description: Optional[str] = Field(default=None, alias="Description")
    permissions: Optional[Sequence[str]] = Field(default=None, alias="Permissions")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    allowed_access_control_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="AllowedAccessControlTags"
    )
    tag_restricted_resources: Optional[Sequence[str]] = Field(
        default=None, alias="TagRestrictedResources"
    )


class CreateTrafficDistributionGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_id: str = Field(alias="InstanceId")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateUseCaseRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_association_id: str = Field(alias="IntegrationAssociationId")
    use_case_type: Literal["CONNECT_CAMPAIGNS", "RULES_EVALUATION"] = Field(
        alias="UseCaseType"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateUserHierarchyGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_id: str = Field(alias="InstanceId")
    parent_group_id: Optional[str] = Field(default=None, alias="ParentGroupId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UserIdentityInfoModel(BaseModel):
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    email: Optional[str] = Field(default=None, alias="Email")
    secondary_email: Optional[str] = Field(default=None, alias="SecondaryEmail")
    mobile: Optional[str] = Field(default=None, alias="Mobile")


class UserPhoneConfigModel(BaseModel):
    phone_type: Literal["DESK_PHONE", "SOFT_PHONE"] = Field(alias="PhoneType")
    auto_accept: Optional[bool] = Field(default=None, alias="AutoAccept")
    after_contact_work_time_limit: Optional[int] = Field(
        default=None, alias="AfterContactWorkTimeLimit"
    )
    desk_phone_number: Optional[str] = Field(default=None, alias="DeskPhoneNumber")


class CreateVocabularyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    vocabulary_name: str = Field(alias="VocabularyName")
    language_code: Literal[
        "ar-AE",
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
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "pt-PT",
        "zh-CN",
    ] = Field(alias="LanguageCode")
    content: str = Field(alias="Content")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CredentialsModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="AccessToken")
    access_token_expiration: Optional[datetime] = Field(
        default=None, alias="AccessTokenExpiration"
    )
    refresh_token: Optional[str] = Field(default=None, alias="RefreshToken")
    refresh_token_expiration: Optional[datetime] = Field(
        default=None, alias="RefreshTokenExpiration"
    )


class CurrentMetricModel(BaseModel):
    name: Optional[
        Literal[
            "AGENTS_AFTER_CONTACT_WORK",
            "AGENTS_AVAILABLE",
            "AGENTS_ERROR",
            "AGENTS_NON_PRODUCTIVE",
            "AGENTS_ONLINE",
            "AGENTS_ON_CALL",
            "AGENTS_ON_CONTACT",
            "AGENTS_STAFFED",
            "CONTACTS_IN_QUEUE",
            "CONTACTS_SCHEDULED",
            "OLDEST_CONTACT_AGE",
            "SLOTS_ACTIVE",
            "SLOTS_AVAILABLE",
        ]
    ] = Field(default=None, alias="Name")
    unit: Optional[Literal["COUNT", "PERCENT", "SECONDS"]] = Field(
        default=None, alias="Unit"
    )


class CurrentMetricSortCriteriaModel(BaseModel):
    sort_by_metric: Optional[
        Literal[
            "AGENTS_AFTER_CONTACT_WORK",
            "AGENTS_AVAILABLE",
            "AGENTS_ERROR",
            "AGENTS_NON_PRODUCTIVE",
            "AGENTS_ONLINE",
            "AGENTS_ON_CALL",
            "AGENTS_ON_CONTACT",
            "AGENTS_STAFFED",
            "CONTACTS_IN_QUEUE",
            "CONTACTS_SCHEDULED",
            "OLDEST_CONTACT_AGE",
            "SLOTS_ACTIVE",
            "SLOTS_AVAILABLE",
        ]
    ] = Field(default=None, alias="SortByMetric")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class DateReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class DefaultVocabularyModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    language_code: Literal[
        "ar-AE",
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
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "pt-PT",
        "zh-CN",
    ] = Field(alias="LanguageCode")
    vocabulary_id: str = Field(alias="VocabularyId")
    vocabulary_name: str = Field(alias="VocabularyName")


class DeleteContactFlowModuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_module_id: str = Field(alias="ContactFlowModuleId")


class DeleteContactFlowRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")


class DeleteHoursOfOperationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")


class DeleteInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class DeleteIntegrationAssociationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_association_id: str = Field(alias="IntegrationAssociationId")


class DeleteQuickConnectRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    quick_connect_id: str = Field(alias="QuickConnectId")


class DeleteRuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    rule_id: str = Field(alias="RuleId")


class DeleteSecurityProfileRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    security_profile_id: str = Field(alias="SecurityProfileId")


class DeleteTaskTemplateRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    task_template_id: str = Field(alias="TaskTemplateId")


class DeleteTrafficDistributionGroupRequestModel(BaseModel):
    traffic_distribution_group_id: str = Field(alias="TrafficDistributionGroupId")


class DeleteUseCaseRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_association_id: str = Field(alias="IntegrationAssociationId")
    use_case_id: str = Field(alias="UseCaseId")


class DeleteUserHierarchyGroupRequestModel(BaseModel):
    hierarchy_group_id: str = Field(alias="HierarchyGroupId")
    instance_id: str = Field(alias="InstanceId")


class DeleteUserRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    user_id: str = Field(alias="UserId")


class DeleteVocabularyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    vocabulary_id: str = Field(alias="VocabularyId")


class DescribeAgentStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    agent_status_id: str = Field(alias="AgentStatusId")


class DescribeContactFlowModuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_module_id: str = Field(alias="ContactFlowModuleId")


class DescribeContactFlowRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")


class DescribeContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")


class DescribeHoursOfOperationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")


class DescribeInstanceAttributeRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    attribute_type: Literal[
        "AUTO_RESOLVE_BEST_VOICES",
        "CONTACTFLOW_LOGS",
        "CONTACT_LENS",
        "EARLY_MEDIA",
        "ENHANCED_CONTACT_MONITORING",
        "HIGH_VOLUME_OUTBOUND",
        "INBOUND_CALLS",
        "MULTI_PARTY_CONFERENCE",
        "OUTBOUND_CALLS",
        "USE_CUSTOM_TTS_VOICES",
    ] = Field(alias="AttributeType")


class DescribeInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class DescribeInstanceStorageConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    association_id: str = Field(alias="AssociationId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")


class DescribePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class DescribeQueueRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")


class DescribeQuickConnectRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    quick_connect_id: str = Field(alias="QuickConnectId")


class DescribeRoutingProfileRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")


class DescribeRuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    rule_id: str = Field(alias="RuleId")


class DescribeSecurityProfileRequestModel(BaseModel):
    security_profile_id: str = Field(alias="SecurityProfileId")
    instance_id: str = Field(alias="InstanceId")


class SecurityProfileModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    organization_resource_id: Optional[str] = Field(
        default=None, alias="OrganizationResourceId"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    security_profile_name: Optional[str] = Field(
        default=None, alias="SecurityProfileName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    allowed_access_control_tags: Optional[Dict[str, str]] = Field(
        default=None, alias="AllowedAccessControlTags"
    )
    tag_restricted_resources: Optional[List[str]] = Field(
        default=None, alias="TagRestrictedResources"
    )


class DescribeTrafficDistributionGroupRequestModel(BaseModel):
    traffic_distribution_group_id: str = Field(alias="TrafficDistributionGroupId")


class TrafficDistributionGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    instance_arn: Optional[str] = Field(default=None, alias="InstanceArn")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "DELETION_FAILED",
            "PENDING_DELETION",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DescribeUserHierarchyGroupRequestModel(BaseModel):
    hierarchy_group_id: str = Field(alias="HierarchyGroupId")
    instance_id: str = Field(alias="InstanceId")


class DescribeUserHierarchyStructureRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class DescribeUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")


class DescribeVocabularyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    vocabulary_id: str = Field(alias="VocabularyId")


class VocabularyModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    language_code: Literal[
        "ar-AE",
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
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "pt-PT",
        "zh-CN",
    ] = Field(alias="LanguageCode")
    state: Literal[
        "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
    ] = Field(alias="State")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    content: Optional[str] = Field(default=None, alias="Content")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class RoutingProfileReferenceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class DisassociateApprovedOriginRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    origin: str = Field(alias="Origin")


class DisassociateInstanceStorageConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    association_id: str = Field(alias="AssociationId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")


class DisassociateLambdaFunctionRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    function_arn: str = Field(alias="FunctionArn")


class DisassociateLexBotRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    bot_name: str = Field(alias="BotName")
    lex_region: str = Field(alias="LexRegion")


class DisassociatePhoneNumberContactFlowRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    instance_id: str = Field(alias="InstanceId")


class DisassociateQueueQuickConnectsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    quick_connect_ids: Sequence[str] = Field(alias="QuickConnectIds")


class RoutingProfileQueueReferenceModel(BaseModel):
    queue_id: str = Field(alias="QueueId")
    channel: Literal["CHAT", "TASK", "VOICE"] = Field(alias="Channel")


class DisassociateSecurityKeyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    association_id: str = Field(alias="AssociationId")


class DismissUserContactRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")


class DistributionModel(BaseModel):
    region: str = Field(alias="Region")
    percentage: int = Field(alias="Percentage")


class EmailReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class EncryptionConfigModel(BaseModel):
    encryption_type: Literal["KMS"] = Field(alias="EncryptionType")
    key_id: str = Field(alias="KeyId")


class EventBridgeActionDefinitionModel(BaseModel):
    name: str = Field(alias="Name")


class FiltersModel(BaseModel):
    queues: Optional[Sequence[str]] = Field(default=None, alias="Queues")
    channels: Optional[Sequence[Literal["CHAT", "TASK", "VOICE"]]] = Field(
        default=None, alias="Channels"
    )
    routing_profiles: Optional[Sequence[str]] = Field(
        default=None, alias="RoutingProfiles"
    )


class GetContactAttributesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    initial_contact_id: str = Field(alias="InitialContactId")


class GetFederationTokenRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetTaskTemplateRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    task_template_id: str = Field(alias="TaskTemplateId")
    snapshot_version: Optional[str] = Field(default=None, alias="SnapshotVersion")


class GetTrafficDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class HierarchyGroupConditionModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    hierarchy_group_match_type: Optional[Literal["EXACT", "WITH_CHILD_GROUPS"]] = Field(
        default=None, alias="HierarchyGroupMatchType"
    )


class HierarchyGroupSummaryReferenceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class HierarchyGroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class HierarchyLevelModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class HierarchyLevelUpdateModel(BaseModel):
    name: str = Field(alias="Name")


class ThresholdModel(BaseModel):
    comparison: Optional[Literal["LT"]] = Field(default=None, alias="Comparison")
    threshold_value: Optional[float] = Field(default=None, alias="ThresholdValue")


class HoursOfOperationTimeSliceModel(BaseModel):
    hours: int = Field(alias="Hours")
    minutes: int = Field(alias="Minutes")


class HoursOfOperationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class InstanceStatusReasonModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")


class KinesisFirehoseConfigModel(BaseModel):
    firehose_arn: str = Field(alias="FirehoseArn")


class KinesisStreamConfigModel(BaseModel):
    stream_arn: str = Field(alias="StreamArn")


class InstanceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    identity_management_type: Optional[
        Literal["CONNECT_MANAGED", "EXISTING_DIRECTORY", "SAML"]
    ] = Field(default=None, alias="IdentityManagementType")
    instance_alias: Optional[str] = Field(default=None, alias="InstanceAlias")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    instance_status: Optional[
        Literal["ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS"]
    ] = Field(default=None, alias="InstanceStatus")
    inbound_calls_enabled: Optional[bool] = Field(
        default=None, alias="InboundCallsEnabled"
    )
    outbound_calls_enabled: Optional[bool] = Field(
        default=None, alias="OutboundCallsEnabled"
    )


class IntegrationAssociationSummaryModel(BaseModel):
    integration_association_id: Optional[str] = Field(
        default=None, alias="IntegrationAssociationId"
    )
    integration_association_arn: Optional[str] = Field(
        default=None, alias="IntegrationAssociationArn"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    integration_type: Optional[
        Literal[
            "CASES_DOMAIN",
            "EVENT",
            "PINPOINT_APP",
            "VOICE_ID",
            "WISDOM_ASSISTANT",
            "WISDOM_KNOWLEDGE_BASE",
        ]
    ] = Field(default=None, alias="IntegrationType")
    integration_arn: Optional[str] = Field(default=None, alias="IntegrationArn")
    source_application_url: Optional[str] = Field(
        default=None, alias="SourceApplicationUrl"
    )
    source_application_name: Optional[str] = Field(
        default=None, alias="SourceApplicationName"
    )
    source_type: Optional[Literal["SALESFORCE", "ZENDESK"]] = Field(
        default=None, alias="SourceType"
    )


class TaskTemplateFieldIdentifierModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class ListAgentStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    agent_status_types: Optional[
        Sequence[Literal["CUSTOM", "OFFLINE", "ROUTABLE"]]
    ] = Field(default=None, alias="AgentStatusTypes")


class ListApprovedOriginsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListBotsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    lex_version: Literal["V1", "V2"] = Field(alias="LexVersion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListContactFlowModulesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    contact_flow_module_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="ContactFlowModuleState"
    )


class ListContactFlowsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_types: Optional[
        Sequence[
            Literal[
                "AGENT_HOLD",
                "AGENT_TRANSFER",
                "AGENT_WHISPER",
                "CONTACT_FLOW",
                "CUSTOMER_HOLD",
                "CUSTOMER_QUEUE",
                "CUSTOMER_WHISPER",
                "OUTBOUND_WHISPER",
                "QUEUE_TRANSFER",
            ]
        ]
    ] = Field(default=None, alias="ContactFlowTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListContactReferencesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    reference_types: Sequence[
        Literal["ATTACHMENT", "DATE", "EMAIL", "NUMBER", "STRING", "URL"]
    ] = Field(alias="ReferenceTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDefaultVocabulariesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    language_code: Optional[
        Literal[
            "ar-AE",
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
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "pt-PT",
            "zh-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHoursOfOperationsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInstanceAttributesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInstanceStorageConfigsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInstancesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIntegrationAssociationsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_type: Optional[
        Literal[
            "CASES_DOMAIN",
            "EVENT",
            "PINPOINT_APP",
            "VOICE_ID",
            "WISDOM_ASSISTANT",
            "WISDOM_KNOWLEDGE_BASE",
        ]
    ] = Field(default=None, alias="IntegrationType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLambdaFunctionsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLexBotsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPhoneNumbersRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    phone_number_types: Optional[Sequence[Literal["DID", "TOLL_FREE"]]] = Field(
        default=None, alias="PhoneNumberTypes"
    )
    phone_number_country_codes: Optional[
        Sequence[
            Literal[
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AN",
                "AO",
                "AQ",
                "AR",
                "AS",
                "AT",
                "AU",
                "AW",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BR",
                "BS",
                "BT",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CC",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CU",
                "CV",
                "CW",
                "CX",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FM",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GQ",
                "GR",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "Type[IO]",
                "IQ",
                "IR",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KP",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MH",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MP",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PT",
                "PW",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SD",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "ST",
                "SV",
                "SX",
                "SY",
                "SZ",
                "TC",
                "TD",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VI",
                "VN",
                "VU",
                "WF",
                "WS",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
            ]
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCodes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PhoneNumberSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_number_type: Optional[Literal["DID", "TOLL_FREE"]] = Field(
        default=None, alias="PhoneNumberType"
    )
    phone_number_country_code: Optional[
        Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "Type[IO]",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCode")


class ListPhoneNumbersSummaryModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    phone_number_arn: Optional[str] = Field(default=None, alias="PhoneNumberArn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_number_country_code: Optional[
        Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "Type[IO]",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCode")
    phone_number_type: Optional[Literal["DID", "TOLL_FREE"]] = Field(
        default=None, alias="PhoneNumberType"
    )
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")


class ListPhoneNumbersV2RequestModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    phone_number_country_codes: Optional[
        Sequence[
            Literal[
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AN",
                "AO",
                "AQ",
                "AR",
                "AS",
                "AT",
                "AU",
                "AW",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BR",
                "BS",
                "BT",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CC",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CU",
                "CV",
                "CW",
                "CX",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FM",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GQ",
                "GR",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "Type[IO]",
                "IQ",
                "IR",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KP",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MH",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MP",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PT",
                "PW",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SD",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "ST",
                "SV",
                "SX",
                "SY",
                "SZ",
                "TC",
                "TD",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VI",
                "VN",
                "VU",
                "WF",
                "WS",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
            ]
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCodes")
    phone_number_types: Optional[Sequence[Literal["DID", "TOLL_FREE"]]] = Field(
        default=None, alias="PhoneNumberTypes"
    )
    phone_number_prefix: Optional[str] = Field(default=None, alias="PhoneNumberPrefix")


class ListPromptsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PromptSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListQueueQuickConnectsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class QuickConnectSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    quick_connect_type: Optional[Literal["PHONE_NUMBER", "QUEUE", "USER"]] = Field(
        default=None, alias="QuickConnectType"
    )


class ListQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_types: Optional[Sequence[Literal["AGENT", "STANDARD"]]] = Field(
        default=None, alias="QueueTypes"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class QueueSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    queue_type: Optional[Literal["AGENT", "STANDARD"]] = Field(
        default=None, alias="QueueType"
    )


class ListQuickConnectsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    quick_connect_types: Optional[
        Sequence[Literal["PHONE_NUMBER", "QUEUE", "USER"]]
    ] = Field(default=None, alias="QuickConnectTypes")


class ListRoutingProfileQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RoutingProfileQueueConfigSummaryModel(BaseModel):
    queue_id: str = Field(alias="QueueId")
    queue_arn: str = Field(alias="QueueArn")
    queue_name: str = Field(alias="QueueName")
    priority: int = Field(alias="Priority")
    delay: int = Field(alias="Delay")
    channel: Literal["CHAT", "TASK", "VOICE"] = Field(alias="Channel")


class ListRoutingProfilesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RoutingProfileSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListRulesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    publish_status: Optional[Literal["DRAFT", "PUBLISHED"]] = Field(
        default=None, alias="PublishStatus"
    )
    event_source_name: Optional[
        Literal[
            "OnPostCallAnalysisAvailable",
            "OnPostChatAnalysisAvailable",
            "OnRealTimeCallAnalysisAvailable",
            "OnSalesforceCaseCreate",
            "OnZendeskTicketCreate",
            "OnZendeskTicketStatusUpdate",
        ]
    ] = Field(default=None, alias="EventSourceName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSecurityKeysRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SecurityKeyModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    key: Optional[str] = Field(default=None, alias="Key")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class ListSecurityProfilePermissionsRequestModel(BaseModel):
    security_profile_id: str = Field(alias="SecurityProfileId")
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSecurityProfilesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SecurityProfileSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTaskTemplatesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class TaskTemplateMetadataModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class ListTrafficDistributionGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class TrafficDistributionGroupSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    instance_arn: Optional[str] = Field(default=None, alias="InstanceArn")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "DELETION_FAILED",
            "PENDING_DELETION",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")


class ListUseCasesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_association_id: str = Field(alias="IntegrationAssociationId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class UseCaseModel(BaseModel):
    use_case_id: Optional[str] = Field(default=None, alias="UseCaseId")
    use_case_arn: Optional[str] = Field(default=None, alias="UseCaseArn")
    use_case_type: Optional[Literal["CONNECT_CAMPAIGNS", "RULES_EVALUATION"]] = Field(
        default=None, alias="UseCaseType"
    )


class ListUserHierarchyGroupsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListUsersRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class UserSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    username: Optional[str] = Field(default=None, alias="Username")


class MonitorContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    user_id: str = Field(alias="UserId")
    allowed_monitor_capabilities: Optional[
        Sequence[Literal["BARGE", "SILENT_MONITOR"]]
    ] = Field(default=None, alias="AllowedMonitorCapabilities")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class NotificationRecipientTypeModel(BaseModel):
    user_tags: Optional[Mapping[str, str]] = Field(default=None, alias="UserTags")
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="UserIds")


class NumberReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ParticipantDetailsModel(BaseModel):
    display_name: str = Field(alias="DisplayName")


class ParticipantTimerValueModel(BaseModel):
    participant_timer_action: Optional[Literal["Unset"]] = Field(
        default=None, alias="ParticipantTimerAction"
    )
    participant_timer_duration_in_minutes: Optional[int] = Field(
        default=None, alias="ParticipantTimerDurationInMinutes"
    )


class PersistentChatModel(BaseModel):
    rehydration_type: Optional[Literal["ENTIRE_PAST_SESSION", "FROM_SEGMENT"]] = Field(
        default=None, alias="RehydrationType"
    )
    source_contact_id: Optional[str] = Field(default=None, alias="SourceContactId")


class PhoneNumberQuickConnectConfigModel(BaseModel):
    phone_number: str = Field(alias="PhoneNumber")


class PutUserStatusRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")
    agent_status_id: str = Field(alias="AgentStatusId")


class QueueQuickConnectConfigModel(BaseModel):
    queue_id: str = Field(alias="QueueId")
    contact_flow_id: str = Field(alias="ContactFlowId")


class StringConditionModel(BaseModel):
    field_name: Optional[str] = Field(default=None, alias="FieldName")
    value: Optional[str] = Field(default=None, alias="Value")
    comparison_type: Optional[Literal["CONTAINS", "EXACT", "STARTS_WITH"]] = Field(
        default=None, alias="ComparisonType"
    )


class UserQuickConnectConfigModel(BaseModel):
    user_id: str = Field(alias="UserId")
    contact_flow_id: str = Field(alias="ContactFlowId")


class StringReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class UrlReferenceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ReferenceModel(BaseModel):
    value: str = Field(alias="Value")
    type: Literal["ATTACHMENT", "DATE", "EMAIL", "NUMBER", "STRING", "URL"] = Field(
        alias="Type"
    )


class ReleasePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ReplicateInstanceRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    replica_region: str = Field(alias="ReplicaRegion")
    replica_alias: str = Field(alias="ReplicaAlias")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ResumeContactRecordingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    initial_contact_id: str = Field(alias="InitialContactId")


class SearchAvailablePhoneNumbersRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    phone_number_country_code: Literal[
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AN",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GQ",
        "GR",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "Type[IO]",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW",
    ] = Field(alias="PhoneNumberCountryCode")
    phone_number_type: Literal["DID", "TOLL_FREE"] = Field(alias="PhoneNumberType")
    phone_number_prefix: Optional[str] = Field(default=None, alias="PhoneNumberPrefix")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SecurityProfileSearchSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    organization_resource_id: Optional[str] = Field(
        default=None, alias="OrganizationResourceId"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    security_profile_name: Optional[str] = Field(
        default=None, alias="SecurityProfileName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class SearchVocabulariesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    state: Optional[
        Literal[
            "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
        ]
    ] = Field(default=None, alias="State")
    name_starts_with: Optional[str] = Field(default=None, alias="NameStartsWith")
    language_code: Optional[
        Literal[
            "ar-AE",
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
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "pt-PT",
            "zh-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")


class VocabularySummaryModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    language_code: Literal[
        "ar-AE",
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
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "pt-PT",
        "zh-CN",
    ] = Field(alias="LanguageCode")
    state: Literal[
        "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
    ] = Field(alias="State")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class VoiceRecordingConfigurationModel(BaseModel):
    voice_recording_track: Optional[Literal["ALL", "FROM_AGENT", "TO_AGENT"]] = Field(
        default=None, alias="VoiceRecordingTrack"
    )


class StopContactRecordingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    initial_contact_id: str = Field(alias="InitialContactId")


class StopContactRequestModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    instance_id: str = Field(alias="InstanceId")


class StopContactStreamingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    streaming_id: str = Field(alias="StreamingId")


class SuspendContactRecordingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    initial_contact_id: str = Field(alias="InitialContactId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TransferContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    contact_flow_id: str = Field(alias="ContactFlowId")
    queue_id: Optional[str] = Field(default=None, alias="QueueId")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAgentStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    agent_status_id: str = Field(alias="AgentStatusId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    display_order: Optional[int] = Field(default=None, alias="DisplayOrder")
    reset_order_number: Optional[bool] = Field(default=None, alias="ResetOrderNumber")


class UpdateContactAttributesRequestModel(BaseModel):
    initial_contact_id: str = Field(alias="InitialContactId")
    instance_id: str = Field(alias="InstanceId")
    attributes: Mapping[str, str] = Field(alias="Attributes")


class UpdateContactFlowContentRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")
    content: str = Field(alias="Content")


class UpdateContactFlowMetadataRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    contact_flow_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="ContactFlowState"
    )


class UpdateContactFlowModuleContentRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_module_id: str = Field(alias="ContactFlowModuleId")
    content: str = Field(alias="Content")


class UpdateContactFlowModuleMetadataRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_module_id: str = Field(alias="ContactFlowModuleId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias="State")


class UpdateContactFlowNameRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateContactScheduleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    scheduled_time: Union[datetime, str] = Field(alias="ScheduledTime")


class UpdateInstanceAttributeRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    attribute_type: Literal[
        "AUTO_RESOLVE_BEST_VOICES",
        "CONTACTFLOW_LOGS",
        "CONTACT_LENS",
        "EARLY_MEDIA",
        "ENHANCED_CONTACT_MONITORING",
        "HIGH_VOLUME_OUTBOUND",
        "INBOUND_CALLS",
        "MULTI_PARTY_CONFERENCE",
        "OUTBOUND_CALLS",
        "USE_CUSTOM_TTS_VOICES",
    ] = Field(alias="AttributeType")
    value: str = Field(alias="Value")


class UpdatePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    target_arn: str = Field(alias="TargetArn")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UpdateQueueHoursOfOperationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")


class UpdateQueueMaxContactsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    max_contacts: Optional[int] = Field(default=None, alias="MaxContacts")


class UpdateQueueNameRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateQueueStatusRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class UpdateQuickConnectNameRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    quick_connect_id: str = Field(alias="QuickConnectId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateRoutingProfileDefaultOutboundQueueRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    default_outbound_queue_id: str = Field(alias="DefaultOutboundQueueId")


class UpdateRoutingProfileNameRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateSecurityProfileRequestModel(BaseModel):
    security_profile_id: str = Field(alias="SecurityProfileId")
    instance_id: str = Field(alias="InstanceId")
    description: Optional[str] = Field(default=None, alias="Description")
    permissions: Optional[Sequence[str]] = Field(default=None, alias="Permissions")
    allowed_access_control_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="AllowedAccessControlTags"
    )
    tag_restricted_resources: Optional[Sequence[str]] = Field(
        default=None, alias="TagRestrictedResources"
    )


class UpdateUserHierarchyGroupNameRequestModel(BaseModel):
    name: str = Field(alias="Name")
    hierarchy_group_id: str = Field(alias="HierarchyGroupId")
    instance_id: str = Field(alias="InstanceId")


class UpdateUserHierarchyRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")
    hierarchy_group_id: Optional[str] = Field(default=None, alias="HierarchyGroupId")


class UpdateUserRoutingProfileRequestModel(BaseModel):
    routing_profile_id: str = Field(alias="RoutingProfileId")
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")


class UpdateUserSecurityProfilesRequestModel(BaseModel):
    security_profile_ids: Sequence[str] = Field(alias="SecurityProfileIds")
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")


class UserReferenceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class UserIdentityInfoLiteModel(BaseModel):
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")


class RuleSummaryModel(BaseModel):
    name: str = Field(alias="Name")
    rule_id: str = Field(alias="RuleId")
    rule_arn: str = Field(alias="RuleArn")
    event_source_name: Literal[
        "OnPostCallAnalysisAvailable",
        "OnPostChatAnalysisAvailable",
        "OnRealTimeCallAnalysisAvailable",
        "OnSalesforceCaseCreate",
        "OnZendeskTicketCreate",
        "OnZendeskTicketStatusUpdate",
    ] = Field(alias="EventSourceName")
    publish_status: Literal["DRAFT", "PUBLISHED"] = Field(alias="PublishStatus")
    action_summaries: List[ActionSummaryModel] = Field(alias="ActionSummaries")
    created_time: datetime = Field(alias="CreatedTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")


class AgentContactReferenceModel(BaseModel):
    contact_id: Optional[str] = Field(default=None, alias="ContactId")
    channel: Optional[Literal["CHAT", "TASK", "VOICE"]] = Field(
        default=None, alias="Channel"
    )
    initiation_method: Optional[
        Literal[
            "API",
            "CALLBACK",
            "DISCONNECT",
            "INBOUND",
            "MONITOR",
            "OUTBOUND",
            "QUEUE_TRANSFER",
            "TRANSFER",
        ]
    ] = Field(default=None, alias="InitiationMethod")
    agent_contact_state: Optional[
        Literal[
            "CONNECTED",
            "CONNECTED_ONHOLD",
            "CONNECTING",
            "ENDED",
            "ERROR",
            "INCOMING",
            "MISSED",
            "PENDING",
            "REJECTED",
        ]
    ] = Field(default=None, alias="AgentContactState")
    state_start_timestamp: Optional[datetime] = Field(
        default=None, alias="StateStartTimestamp"
    )
    connected_to_agent_timestamp: Optional[datetime] = Field(
        default=None, alias="ConnectedToAgentTimestamp"
    )
    queue: Optional[QueueReferenceModel] = Field(default=None, alias="Queue")


class StartOutboundVoiceContactRequestModel(BaseModel):
    destination_phone_number: str = Field(alias="DestinationPhoneNumber")
    contact_flow_id: str = Field(alias="ContactFlowId")
    instance_id: str = Field(alias="InstanceId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    source_phone_number: Optional[str] = Field(default=None, alias="SourcePhoneNumber")
    queue_id: Optional[str] = Field(default=None, alias="QueueId")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    answer_machine_detection_config: Optional[
        AnswerMachineDetectionConfigModel
    ] = Field(default=None, alias="AnswerMachineDetectionConfig")
    campaign_id: Optional[str] = Field(default=None, alias="CampaignId")
    traffic_type: Optional[Literal["CAMPAIGN", "GENERAL"]] = Field(
        default=None, alias="TrafficType"
    )


class AssociateLexBotRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    lex_bot: LexBotModel = Field(alias="LexBot")


class AssociateBotRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    lex_bot: Optional[LexBotModel] = Field(default=None, alias="LexBot")
    lex_v2_bot: Optional[LexV2BotModel] = Field(default=None, alias="LexV2Bot")


class DisassociateBotRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    lex_bot: Optional[LexBotModel] = Field(default=None, alias="LexBot")
    lex_v2_bot: Optional[LexV2BotModel] = Field(default=None, alias="LexV2Bot")


class LexBotConfigModel(BaseModel):
    lex_bot: Optional[LexBotModel] = Field(default=None, alias="LexBot")
    lex_v2_bot: Optional[LexV2BotModel] = Field(default=None, alias="LexV2Bot")


class AssociateInstanceStorageConfigResponseModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateSecurityKeyResponseModel(BaseModel):
    association_id: str = Field(alias="AssociationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClaimPhoneNumberResponseModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAgentStatusResponseModel(BaseModel):
    agent_status_arn: str = Field(alias="AgentStatusARN")
    agent_status_id: str = Field(alias="AgentStatusId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContactFlowModuleResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContactFlowResponseModel(BaseModel):
    contact_flow_id: str = Field(alias="ContactFlowId")
    contact_flow_arn: str = Field(alias="ContactFlowArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHoursOfOperationResponseModel(BaseModel):
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")
    hours_of_operation_arn: str = Field(alias="HoursOfOperationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIntegrationAssociationResponseModel(BaseModel):
    integration_association_id: str = Field(alias="IntegrationAssociationId")
    integration_association_arn: str = Field(alias="IntegrationAssociationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQueueResponseModel(BaseModel):
    queue_arn: str = Field(alias="QueueArn")
    queue_id: str = Field(alias="QueueId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQuickConnectResponseModel(BaseModel):
    quick_connect_arn: str = Field(alias="QuickConnectARN")
    quick_connect_id: str = Field(alias="QuickConnectId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoutingProfileResponseModel(BaseModel):
    routing_profile_arn: str = Field(alias="RoutingProfileArn")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleResponseModel(BaseModel):
    rule_arn: str = Field(alias="RuleArn")
    rule_id: str = Field(alias="RuleId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSecurityProfileResponseModel(BaseModel):
    security_profile_id: str = Field(alias="SecurityProfileId")
    security_profile_arn: str = Field(alias="SecurityProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskTemplateResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrafficDistributionGroupResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUseCaseResponseModel(BaseModel):
    use_case_id: str = Field(alias="UseCaseId")
    use_case_arn: str = Field(alias="UseCaseArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserHierarchyGroupResponseModel(BaseModel):
    hierarchy_group_id: str = Field(alias="HierarchyGroupId")
    hierarchy_group_arn: str = Field(alias="HierarchyGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    user_arn: str = Field(alias="UserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVocabularyResponseModel(BaseModel):
    vocabulary_arn: str = Field(alias="VocabularyArn")
    vocabulary_id: str = Field(alias="VocabularyId")
    state: Literal[
        "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVocabularyResponseModel(BaseModel):
    vocabulary_arn: str = Field(alias="VocabularyArn")
    vocabulary_id: str = Field(alias="VocabularyId")
    state: Literal[
        "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAgentStatusResponseModel(BaseModel):
    agent_status: AgentStatusModel = Field(alias="AgentStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactAttributesResponseModel(BaseModel):
    attributes: Dict[str, str] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAgentStatusResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    agent_status_summary_list: List[AgentStatusSummaryModel] = Field(
        alias="AgentStatusSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApprovedOriginsResponseModel(BaseModel):
    origins: List[str] = Field(alias="Origins")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLambdaFunctionsResponseModel(BaseModel):
    lambda_functions: List[str] = Field(alias="LambdaFunctions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLexBotsResponseModel(BaseModel):
    lex_bots: List[LexBotModel] = Field(alias="LexBots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityProfilePermissionsResponseModel(BaseModel):
    permissions: List[str] = Field(alias="Permissions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MonitorContactResponseModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    contact_arn: str = Field(alias="ContactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicateInstanceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartChatContactResponseModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    participant_id: str = Field(alias="ParticipantId")
    participant_token: str = Field(alias="ParticipantToken")
    continued_from_contact_id: str = Field(alias="ContinuedFromContactId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContactStreamingResponseModel(BaseModel):
    streaming_id: str = Field(alias="StreamingId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartOutboundVoiceContactResponseModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTaskContactResponseModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransferContactResponseModel(BaseModel):
    contact_id: str = Field(alias="ContactId")
    contact_arn: str = Field(alias="ContactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePhoneNumberResponseModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstanceAttributeResponseModel(BaseModel):
    attribute: AttributeModel = Field(alias="Attribute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceAttributesResponseModel(BaseModel):
    attributes: List[AttributeModel] = Field(alias="Attributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAvailablePhoneNumbersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    available_numbers_list: List[AvailableNumberSummaryModel] = Field(
        alias="AvailableNumbersList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContactStreamingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    chat_streaming_configuration: ChatStreamingConfigurationModel = Field(
        alias="ChatStreamingConfiguration"
    )
    client_token: str = Field(alias="ClientToken")


class ClaimedPhoneNumberSummaryModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    phone_number_arn: Optional[str] = Field(default=None, alias="PhoneNumberArn")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_number_country_code: Optional[
        Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "Type[IO]",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCode")
    phone_number_type: Optional[Literal["DID", "TOLL_FREE"]] = Field(
        default=None, alias="PhoneNumberType"
    )
    phone_number_description: Optional[str] = Field(
        default=None, alias="PhoneNumberDescription"
    )
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    phone_number_status: Optional[PhoneNumberStatusModel] = Field(
        default=None, alias="PhoneNumberStatus"
    )


class UserDataFiltersModel(BaseModel):
    queues: Optional[Sequence[str]] = Field(default=None, alias="Queues")
    contact_filter: Optional[ContactFilterModel] = Field(
        default=None, alias="ContactFilter"
    )
    routing_profiles: Optional[Sequence[str]] = Field(
        default=None, alias="RoutingProfiles"
    )
    agents: Optional[Sequence[str]] = Field(default=None, alias="Agents")
    user_hierarchy_groups: Optional[Sequence[str]] = Field(
        default=None, alias="UserHierarchyGroups"
    )


class ListContactFlowModulesResponseModel(BaseModel):
    contact_flow_modules_summary_list: List[ContactFlowModuleSummaryModel] = Field(
        alias="ContactFlowModulesSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContactFlowModuleResponseModel(BaseModel):
    contact_flow_module: ContactFlowModuleModel = Field(alias="ContactFlowModule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContactFlowsResponseModel(BaseModel):
    contact_flow_summary_list: List[ContactFlowSummaryModel] = Field(
        alias="ContactFlowSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContactFlowResponseModel(BaseModel):
    contact_flow: ContactFlowModel = Field(alias="ContactFlow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContactModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    initial_contact_id: Optional[str] = Field(default=None, alias="InitialContactId")
    previous_contact_id: Optional[str] = Field(default=None, alias="PreviousContactId")
    initiation_method: Optional[
        Literal[
            "API",
            "CALLBACK",
            "DISCONNECT",
            "INBOUND",
            "MONITOR",
            "OUTBOUND",
            "QUEUE_TRANSFER",
            "TRANSFER",
        ]
    ] = Field(default=None, alias="InitiationMethod")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    channel: Optional[Literal["CHAT", "TASK", "VOICE"]] = Field(
        default=None, alias="Channel"
    )
    queue_info: Optional[QueueInfoModel] = Field(default=None, alias="QueueInfo")
    agent_info: Optional[AgentInfoModel] = Field(default=None, alias="AgentInfo")
    initiation_timestamp: Optional[datetime] = Field(
        default=None, alias="InitiationTimestamp"
    )
    disconnect_timestamp: Optional[datetime] = Field(
        default=None, alias="DisconnectTimestamp"
    )
    last_update_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdateTimestamp"
    )
    scheduled_timestamp: Optional[datetime] = Field(
        default=None, alias="ScheduledTimestamp"
    )
    related_contact_id: Optional[str] = Field(default=None, alias="RelatedContactId")
    wisdom_info: Optional[WisdomInfoModel] = Field(default=None, alias="WisdomInfo")


class ControlPlaneTagFilterModel(BaseModel):
    or_conditions: Optional[Sequence[Sequence[TagConditionModel]]] = Field(
        default=None, alias="OrConditions"
    )
    and_conditions: Optional[Sequence[TagConditionModel]] = Field(
        default=None, alias="AndConditions"
    )
    tag_condition: Optional[TagConditionModel] = Field(
        default=None, alias="TagCondition"
    )


class CreateQueueRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")
    description: Optional[str] = Field(default=None, alias="Description")
    outbound_caller_config: Optional[OutboundCallerConfigModel] = Field(
        default=None, alias="OutboundCallerConfig"
    )
    max_contacts: Optional[int] = Field(default=None, alias="MaxContacts")
    quick_connect_ids: Optional[Sequence[str]] = Field(
        default=None, alias="QuickConnectIds"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class QueueModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    queue_arn: Optional[str] = Field(default=None, alias="QueueArn")
    queue_id: Optional[str] = Field(default=None, alias="QueueId")
    description: Optional[str] = Field(default=None, alias="Description")
    outbound_caller_config: Optional[OutboundCallerConfigModel] = Field(
        default=None, alias="OutboundCallerConfig"
    )
    hours_of_operation_id: Optional[str] = Field(
        default=None, alias="HoursOfOperationId"
    )
    max_contacts: Optional[int] = Field(default=None, alias="MaxContacts")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateQueueOutboundCallerConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    outbound_caller_config: OutboundCallerConfigModel = Field(
        alias="OutboundCallerConfig"
    )


class RoutingProfileModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    name: Optional[str] = Field(default=None, alias="Name")
    routing_profile_arn: Optional[str] = Field(default=None, alias="RoutingProfileArn")
    routing_profile_id: Optional[str] = Field(default=None, alias="RoutingProfileId")
    description: Optional[str] = Field(default=None, alias="Description")
    media_concurrencies: Optional[List[MediaConcurrencyModel]] = Field(
        default=None, alias="MediaConcurrencies"
    )
    default_outbound_queue_id: Optional[str] = Field(
        default=None, alias="DefaultOutboundQueueId"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    number_of_associated_queues: Optional[int] = Field(
        default=None, alias="NumberOfAssociatedQueues"
    )
    number_of_associated_users: Optional[int] = Field(
        default=None, alias="NumberOfAssociatedUsers"
    )


class UpdateRoutingProfileConcurrencyRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    media_concurrencies: Sequence[MediaConcurrencyModel] = Field(
        alias="MediaConcurrencies"
    )


class UpdateUserIdentityInfoRequestModel(BaseModel):
    identity_info: UserIdentityInfoModel = Field(alias="IdentityInfo")
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")


class CreateUserRequestModel(BaseModel):
    username: str = Field(alias="Username")
    phone_config: UserPhoneConfigModel = Field(alias="PhoneConfig")
    security_profile_ids: Sequence[str] = Field(alias="SecurityProfileIds")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    instance_id: str = Field(alias="InstanceId")
    password: Optional[str] = Field(default=None, alias="Password")
    identity_info: Optional[UserIdentityInfoModel] = Field(
        default=None, alias="IdentityInfo"
    )
    directory_user_id: Optional[str] = Field(default=None, alias="DirectoryUserId")
    hierarchy_group_id: Optional[str] = Field(default=None, alias="HierarchyGroupId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateUserPhoneConfigRequestModel(BaseModel):
    phone_config: UserPhoneConfigModel = Field(alias="PhoneConfig")
    user_id: str = Field(alias="UserId")
    instance_id: str = Field(alias="InstanceId")


class UserModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    username: Optional[str] = Field(default=None, alias="Username")
    identity_info: Optional[UserIdentityInfoModel] = Field(
        default=None, alias="IdentityInfo"
    )
    phone_config: Optional[UserPhoneConfigModel] = Field(
        default=None, alias="PhoneConfig"
    )
    directory_user_id: Optional[str] = Field(default=None, alias="DirectoryUserId")
    security_profile_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityProfileIds"
    )
    routing_profile_id: Optional[str] = Field(default=None, alias="RoutingProfileId")
    hierarchy_group_id: Optional[str] = Field(default=None, alias="HierarchyGroupId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetFederationTokenResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    sign_in_url: str = Field(alias="SignInUrl")
    user_arn: str = Field(alias="UserArn")
    user_id: str = Field(alias="UserId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CurrentMetricDataModel(BaseModel):
    metric: Optional[CurrentMetricModel] = Field(default=None, alias="Metric")
    value: Optional[float] = Field(default=None, alias="Value")


class ListDefaultVocabulariesResponseModel(BaseModel):
    default_vocabulary_list: List[DefaultVocabularyModel] = Field(
        alias="DefaultVocabularyList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSecurityProfileResponseModel(BaseModel):
    security_profile: SecurityProfileModel = Field(alias="SecurityProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTrafficDistributionGroupResponseModel(BaseModel):
    traffic_distribution_group: TrafficDistributionGroupModel = Field(
        alias="TrafficDistributionGroup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVocabularyResponseModel(BaseModel):
    vocabulary: VocabularyModel = Field(alias="Vocabulary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DimensionsModel(BaseModel):
    queue: Optional[QueueReferenceModel] = Field(default=None, alias="Queue")
    channel: Optional[Literal["CHAT", "TASK", "VOICE"]] = Field(
        default=None, alias="Channel"
    )
    routing_profile: Optional[RoutingProfileReferenceModel] = Field(
        default=None, alias="RoutingProfile"
    )


class DisassociateRoutingProfileQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    queue_references: Sequence[RoutingProfileQueueReferenceModel] = Field(
        alias="QueueReferences"
    )


class RoutingProfileQueueConfigModel(BaseModel):
    queue_reference: RoutingProfileQueueReferenceModel = Field(alias="QueueReference")
    priority: int = Field(alias="Priority")
    delay: int = Field(alias="Delay")


class TelephonyConfigModel(BaseModel):
    distributions: List[DistributionModel] = Field(alias="Distributions")


class KinesisVideoStreamConfigModel(BaseModel):
    prefix: str = Field(alias="Prefix")
    retention_period_hours: int = Field(alias="RetentionPeriodHours")
    encryption_config: EncryptionConfigModel = Field(alias="EncryptionConfig")


class S3ConfigModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    bucket_prefix: str = Field(alias="BucketPrefix")
    encryption_config: Optional[EncryptionConfigModel] = Field(
        default=None, alias="EncryptionConfig"
    )


class GetCurrentMetricDataRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    filters: FiltersModel = Field(alias="Filters")
    current_metrics: Sequence[CurrentMetricModel] = Field(alias="CurrentMetrics")
    groupings: Optional[
        Sequence[Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE"]]
    ] = Field(default=None, alias="Groupings")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_criteria: Optional[Sequence[CurrentMetricSortCriteriaModel]] = Field(
        default=None, alias="SortCriteria"
    )


class ListAgentStatusRequestListAgentStatusesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    agent_status_types: Optional[
        Sequence[Literal["CUSTOM", "OFFLINE", "ROUTABLE"]]
    ] = Field(default=None, alias="AgentStatusTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApprovedOriginsRequestListApprovedOriginsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBotsRequestListBotsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    lex_version: Literal["V1", "V2"] = Field(alias="LexVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContactFlowModulesRequestListContactFlowModulesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_module_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="ContactFlowModuleState"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContactFlowsRequestListContactFlowsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_types: Optional[
        Sequence[
            Literal[
                "AGENT_HOLD",
                "AGENT_TRANSFER",
                "AGENT_WHISPER",
                "CONTACT_FLOW",
                "CUSTOMER_HOLD",
                "CUSTOMER_QUEUE",
                "CUSTOMER_WHISPER",
                "OUTBOUND_WHISPER",
                "QUEUE_TRANSFER",
            ]
        ]
    ] = Field(default=None, alias="ContactFlowTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContactReferencesRequestListContactReferencesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    reference_types: Sequence[
        Literal["ATTACHMENT", "DATE", "EMAIL", "NUMBER", "STRING", "URL"]
    ] = Field(alias="ReferenceTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDefaultVocabulariesRequestListDefaultVocabulariesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    language_code: Optional[
        Literal[
            "ar-AE",
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
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "pt-PT",
            "zh-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHoursOfOperationsRequestListHoursOfOperationsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceAttributesRequestListInstanceAttributesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateModel(
    BaseModel
):
    instance_id: str = Field(alias="InstanceId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstancesRequestListInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIntegrationAssociationsRequestListIntegrationAssociationsPaginateModel(
    BaseModel
):
    instance_id: str = Field(alias="InstanceId")
    integration_type: Optional[
        Literal[
            "CASES_DOMAIN",
            "EVENT",
            "PINPOINT_APP",
            "VOICE_ID",
            "WISDOM_ASSISTANT",
            "WISDOM_KNOWLEDGE_BASE",
        ]
    ] = Field(default=None, alias="IntegrationType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLambdaFunctionsRequestListLambdaFunctionsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLexBotsRequestListLexBotsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPhoneNumbersRequestListPhoneNumbersPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    phone_number_types: Optional[Sequence[Literal["DID", "TOLL_FREE"]]] = Field(
        default=None, alias="PhoneNumberTypes"
    )
    phone_number_country_codes: Optional[
        Sequence[
            Literal[
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AN",
                "AO",
                "AQ",
                "AR",
                "AS",
                "AT",
                "AU",
                "AW",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BR",
                "BS",
                "BT",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CC",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CU",
                "CV",
                "CW",
                "CX",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FM",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GQ",
                "GR",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "Type[IO]",
                "IQ",
                "IR",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KP",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MH",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MP",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PT",
                "PW",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SD",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "ST",
                "SV",
                "SX",
                "SY",
                "SZ",
                "TC",
                "TD",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VI",
                "VN",
                "VU",
                "WF",
                "WS",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
            ]
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCodes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    phone_number_country_codes: Optional[
        Sequence[
            Literal[
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AN",
                "AO",
                "AQ",
                "AR",
                "AS",
                "AT",
                "AU",
                "AW",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BR",
                "BS",
                "BT",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CC",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CU",
                "CV",
                "CW",
                "CX",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FM",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GQ",
                "GR",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "Type[IO]",
                "IQ",
                "IR",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KP",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MH",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MP",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PT",
                "PW",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SD",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "ST",
                "SV",
                "SX",
                "SY",
                "SZ",
                "TC",
                "TD",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VI",
                "VN",
                "VU",
                "WF",
                "WS",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
            ]
        ]
    ] = Field(default=None, alias="PhoneNumberCountryCodes")
    phone_number_types: Optional[Sequence[Literal["DID", "TOLL_FREE"]]] = Field(
        default=None, alias="PhoneNumberTypes"
    )
    phone_number_prefix: Optional[str] = Field(default=None, alias="PhoneNumberPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPromptsRequestListPromptsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueueQuickConnectsRequestListQueueQuickConnectsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_id: str = Field(alias="QueueId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueuesRequestListQueuesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    queue_types: Optional[Sequence[Literal["AGENT", "STANDARD"]]] = Field(
        default=None, alias="QueueTypes"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQuickConnectsRequestListQuickConnectsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    quick_connect_types: Optional[
        Sequence[Literal["PHONE_NUMBER", "QUEUE", "USER"]]
    ] = Field(default=None, alias="QuickConnectTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutingProfilesRequestListRoutingProfilesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesRequestListRulesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    publish_status: Optional[Literal["DRAFT", "PUBLISHED"]] = Field(
        default=None, alias="PublishStatus"
    )
    event_source_name: Optional[
        Literal[
            "OnPostCallAnalysisAvailable",
            "OnPostChatAnalysisAvailable",
            "OnRealTimeCallAnalysisAvailable",
            "OnSalesforceCaseCreate",
            "OnZendeskTicketCreate",
            "OnZendeskTicketStatusUpdate",
        ]
    ] = Field(default=None, alias="EventSourceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityKeysRequestListSecurityKeysPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateModel(
    BaseModel
):
    security_profile_id: str = Field(alias="SecurityProfileId")
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityProfilesRequestListSecurityProfilesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTaskTemplatesRequestListTaskTemplatesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateModel(
    BaseModel
):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUseCasesRequestListUseCasesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    integration_association_id: str = Field(alias="IntegrationAssociationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateModel(
    BaseModel
):
    target_arn: str = Field(alias="TargetArn")
    phone_number_country_code: Literal[
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AN",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GQ",
        "GR",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "Type[IO]",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW",
    ] = Field(alias="PhoneNumberCountryCode")
    phone_number_type: Literal["DID", "TOLL_FREE"] = Field(alias="PhoneNumberType")
    phone_number_prefix: Optional[str] = Field(default=None, alias="PhoneNumberPrefix")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchVocabulariesRequestSearchVocabulariesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    state: Optional[
        Literal[
            "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
        ]
    ] = Field(default=None, alias="State")
    name_starts_with: Optional[str] = Field(default=None, alias="NameStartsWith")
    language_code: Optional[
        Literal[
            "ar-AE",
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
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "pt-PT",
            "zh-CN",
        ]
    ] = Field(default=None, alias="LanguageCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class HierarchyPathReferenceModel(BaseModel):
    level_one: Optional[HierarchyGroupSummaryReferenceModel] = Field(
        default=None, alias="LevelOne"
    )
    level_two: Optional[HierarchyGroupSummaryReferenceModel] = Field(
        default=None, alias="LevelTwo"
    )
    level_three: Optional[HierarchyGroupSummaryReferenceModel] = Field(
        default=None, alias="LevelThree"
    )
    level_four: Optional[HierarchyGroupSummaryReferenceModel] = Field(
        default=None, alias="LevelFour"
    )
    level_five: Optional[HierarchyGroupSummaryReferenceModel] = Field(
        default=None, alias="LevelFive"
    )


class HierarchyPathModel(BaseModel):
    level_one: Optional[HierarchyGroupSummaryModel] = Field(
        default=None, alias="LevelOne"
    )
    level_two: Optional[HierarchyGroupSummaryModel] = Field(
        default=None, alias="LevelTwo"
    )
    level_three: Optional[HierarchyGroupSummaryModel] = Field(
        default=None, alias="LevelThree"
    )
    level_four: Optional[HierarchyGroupSummaryModel] = Field(
        default=None, alias="LevelFour"
    )
    level_five: Optional[HierarchyGroupSummaryModel] = Field(
        default=None, alias="LevelFive"
    )


class ListUserHierarchyGroupsResponseModel(BaseModel):
    user_hierarchy_group_summary_list: List[HierarchyGroupSummaryModel] = Field(
        alias="UserHierarchyGroupSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HierarchyStructureModel(BaseModel):
    level_one: Optional[HierarchyLevelModel] = Field(default=None, alias="LevelOne")
    level_two: Optional[HierarchyLevelModel] = Field(default=None, alias="LevelTwo")
    level_three: Optional[HierarchyLevelModel] = Field(default=None, alias="LevelThree")
    level_four: Optional[HierarchyLevelModel] = Field(default=None, alias="LevelFour")
    level_five: Optional[HierarchyLevelModel] = Field(default=None, alias="LevelFive")


class HierarchyStructureUpdateModel(BaseModel):
    level_one: Optional[HierarchyLevelUpdateModel] = Field(
        default=None, alias="LevelOne"
    )
    level_two: Optional[HierarchyLevelUpdateModel] = Field(
        default=None, alias="LevelTwo"
    )
    level_three: Optional[HierarchyLevelUpdateModel] = Field(
        default=None, alias="LevelThree"
    )
    level_four: Optional[HierarchyLevelUpdateModel] = Field(
        default=None, alias="LevelFour"
    )
    level_five: Optional[HierarchyLevelUpdateModel] = Field(
        default=None, alias="LevelFive"
    )


class HistoricalMetricModel(BaseModel):
    name: Optional[
        Literal[
            "ABANDON_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "API_CONTACTS_HANDLED",
            "CALLBACK_CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_CONSULTED",
            "CONTACTS_HANDLED",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_MISSED",
            "CONTACTS_QUEUED",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "HANDLE_TIME",
            "HOLD_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "INTERACTION_TIME",
            "OCCUPANCY",
            "QUEUED_TIME",
            "QUEUE_ANSWER_TIME",
            "SERVICE_LEVEL",
        ]
    ] = Field(default=None, alias="Name")
    threshold: Optional[ThresholdModel] = Field(default=None, alias="Threshold")
    statistic: Optional[Literal["AVG", "MAX", "SUM"]] = Field(
        default=None, alias="Statistic"
    )
    unit: Optional[Literal["COUNT", "PERCENT", "SECONDS"]] = Field(
        default=None, alias="Unit"
    )


class HoursOfOperationConfigModel(BaseModel):
    day: Literal[
        "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
    ] = Field(alias="Day")
    start_time: HoursOfOperationTimeSliceModel = Field(alias="StartTime")
    end_time: HoursOfOperationTimeSliceModel = Field(alias="EndTime")


class ListHoursOfOperationsResponseModel(BaseModel):
    hours_of_operation_summary_list: List[HoursOfOperationSummaryModel] = Field(
        alias="HoursOfOperationSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    identity_management_type: Optional[
        Literal["CONNECT_MANAGED", "EXISTING_DIRECTORY", "SAML"]
    ] = Field(default=None, alias="IdentityManagementType")
    instance_alias: Optional[str] = Field(default=None, alias="InstanceAlias")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    instance_status: Optional[
        Literal["ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS"]
    ] = Field(default=None, alias="InstanceStatus")
    status_reason: Optional[InstanceStatusReasonModel] = Field(
        default=None, alias="StatusReason"
    )
    inbound_calls_enabled: Optional[bool] = Field(
        default=None, alias="InboundCallsEnabled"
    )
    outbound_calls_enabled: Optional[bool] = Field(
        default=None, alias="OutboundCallsEnabled"
    )


class ListInstancesResponseModel(BaseModel):
    instance_summary_list: List[InstanceSummaryModel] = Field(
        alias="InstanceSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIntegrationAssociationsResponseModel(BaseModel):
    integration_association_summary_list: List[
        IntegrationAssociationSummaryModel
    ] = Field(alias="IntegrationAssociationSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvisibleFieldInfoModel(BaseModel):
    id: Optional[TaskTemplateFieldIdentifierModel] = Field(default=None, alias="Id")


class ReadOnlyFieldInfoModel(BaseModel):
    id: Optional[TaskTemplateFieldIdentifierModel] = Field(default=None, alias="Id")


class RequiredFieldInfoModel(BaseModel):
    id: Optional[TaskTemplateFieldIdentifierModel] = Field(default=None, alias="Id")


class TaskTemplateDefaultFieldValueModel(BaseModel):
    id: Optional[TaskTemplateFieldIdentifierModel] = Field(default=None, alias="Id")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class TaskTemplateFieldModel(BaseModel):
    id: TaskTemplateFieldIdentifierModel = Field(alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[
        Literal[
            "BOOLEAN",
            "DATE_TIME",
            "DESCRIPTION",
            "EMAIL",
            "NAME",
            "NUMBER",
            "QUICK_CONNECT",
            "SCHEDULED_TIME",
            "SINGLE_SELECT",
            "TEXT",
            "TEXT_AREA",
            "URL",
        ]
    ] = Field(default=None, alias="Type")
    single_select_options: Optional[Sequence[str]] = Field(
        default=None, alias="SingleSelectOptions"
    )


class ListPhoneNumbersResponseModel(BaseModel):
    phone_number_summary_list: List[PhoneNumberSummaryModel] = Field(
        alias="PhoneNumberSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumbersV2ResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    list_phone_numbers_summary_list: List[ListPhoneNumbersSummaryModel] = Field(
        alias="ListPhoneNumbersSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPromptsResponseModel(BaseModel):
    prompt_summary_list: List[PromptSummaryModel] = Field(alias="PromptSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueueQuickConnectsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    quick_connect_summary_list: List[QuickConnectSummaryModel] = Field(
        alias="QuickConnectSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQuickConnectsResponseModel(BaseModel):
    quick_connect_summary_list: List[QuickConnectSummaryModel] = Field(
        alias="QuickConnectSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueuesResponseModel(BaseModel):
    queue_summary_list: List[QueueSummaryModel] = Field(alias="QueueSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutingProfileQueuesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    routing_profile_queue_config_summary_list: List[
        RoutingProfileQueueConfigSummaryModel
    ] = Field(alias="RoutingProfileQueueConfigSummaryList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutingProfilesResponseModel(BaseModel):
    routing_profile_summary_list: List[RoutingProfileSummaryModel] = Field(
        alias="RoutingProfileSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityKeysResponseModel(BaseModel):
    security_keys: List[SecurityKeyModel] = Field(alias="SecurityKeys")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityProfilesResponseModel(BaseModel):
    security_profile_summary_list: List[SecurityProfileSummaryModel] = Field(
        alias="SecurityProfileSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTaskTemplatesResponseModel(BaseModel):
    task_templates: List[TaskTemplateMetadataModel] = Field(alias="TaskTemplates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficDistributionGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    traffic_distribution_group_summary_list: List[
        TrafficDistributionGroupSummaryModel
    ] = Field(alias="TrafficDistributionGroupSummaryList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUseCasesResponseModel(BaseModel):
    use_case_summary_list: List[UseCaseModel] = Field(alias="UseCaseSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    user_summary_list: List[UserSummaryModel] = Field(alias="UserSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendNotificationActionDefinitionModel(BaseModel):
    delivery_method: Literal["EMAIL"] = Field(alias="DeliveryMethod")
    content: str = Field(alias="Content")
    content_type: Literal["PLAIN_TEXT"] = Field(alias="ContentType")
    recipient: NotificationRecipientTypeModel = Field(alias="Recipient")
    subject: Optional[str] = Field(default=None, alias="Subject")


class ParticipantTimerConfigurationModel(BaseModel):
    participant_role: Literal["AGENT", "CUSTOMER"] = Field(alias="ParticipantRole")
    timer_type: Literal["DISCONNECT_NONCUSTOMER", "IDLE"] = Field(alias="TimerType")
    timer_value: ParticipantTimerValueModel = Field(alias="TimerValue")


class StartChatContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_flow_id: str = Field(alias="ContactFlowId")
    participant_details: ParticipantDetailsModel = Field(alias="ParticipantDetails")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    initial_message: Optional[ChatMessageModel] = Field(
        default=None, alias="InitialMessage"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    chat_duration_in_minutes: Optional[int] = Field(
        default=None, alias="ChatDurationInMinutes"
    )
    supported_messaging_content_types: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedMessagingContentTypes"
    )
    persistent_chat: Optional[PersistentChatModel] = Field(
        default=None, alias="PersistentChat"
    )


class QueueSearchCriteriaModel(BaseModel):
    or_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="OrConditions"
    )
    and_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="AndConditions"
    )
    string_condition: Optional[StringConditionModel] = Field(
        default=None, alias="StringCondition"
    )
    queue_type_condition: Optional[Literal["STANDARD"]] = Field(
        default=None, alias="QueueTypeCondition"
    )


class RoutingProfileSearchCriteriaModel(BaseModel):
    or_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="OrConditions"
    )
    and_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="AndConditions"
    )
    string_condition: Optional[StringConditionModel] = Field(
        default=None, alias="StringCondition"
    )


class SecurityProfileSearchCriteriaModel(BaseModel):
    or_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="OrConditions"
    )
    and_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="AndConditions"
    )
    string_condition: Optional[StringConditionModel] = Field(
        default=None, alias="StringCondition"
    )


class UserSearchCriteriaModel(BaseModel):
    or_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="OrConditions"
    )
    and_conditions: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="AndConditions"
    )
    string_condition: Optional[StringConditionModel] = Field(
        default=None, alias="StringCondition"
    )
    hierarchy_group_condition: Optional[HierarchyGroupConditionModel] = Field(
        default=None, alias="HierarchyGroupCondition"
    )


class QuickConnectConfigModel(BaseModel):
    quick_connect_type: Literal["PHONE_NUMBER", "QUEUE", "USER"] = Field(
        alias="QuickConnectType"
    )
    user_config: Optional[UserQuickConnectConfigModel] = Field(
        default=None, alias="UserConfig"
    )
    queue_config: Optional[QueueQuickConnectConfigModel] = Field(
        default=None, alias="QueueConfig"
    )
    phone_config: Optional[PhoneNumberQuickConnectConfigModel] = Field(
        default=None, alias="PhoneConfig"
    )


class ReferenceSummaryModel(BaseModel):
    url: Optional[UrlReferenceModel] = Field(default=None, alias="Url")
    attachment: Optional[AttachmentReferenceModel] = Field(
        default=None, alias="Attachment"
    )
    string: Optional[StringReferenceModel] = Field(default=None, alias="String")
    number: Optional[NumberReferenceModel] = Field(default=None, alias="Number")
    date: Optional[DateReferenceModel] = Field(default=None, alias="Date")
    email: Optional[EmailReferenceModel] = Field(default=None, alias="Email")


class StartTaskContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    previous_contact_id: Optional[str] = Field(default=None, alias="PreviousContactId")
    contact_flow_id: Optional[str] = Field(default=None, alias="ContactFlowId")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    references: Optional[Mapping[str, ReferenceModel]] = Field(
        default=None, alias="References"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    scheduled_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduledTime"
    )
    task_template_id: Optional[str] = Field(default=None, alias="TaskTemplateId")
    quick_connect_id: Optional[str] = Field(default=None, alias="QuickConnectId")
    related_contact_id: Optional[str] = Field(default=None, alias="RelatedContactId")


class TaskActionDefinitionModel(BaseModel):
    name: str = Field(alias="Name")
    contact_flow_id: str = Field(alias="ContactFlowId")
    description: Optional[str] = Field(default=None, alias="Description")
    references: Optional[Mapping[str, ReferenceModel]] = Field(
        default=None, alias="References"
    )


class UpdateContactRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    references: Optional[Mapping[str, ReferenceModel]] = Field(
        default=None, alias="References"
    )


class SearchSecurityProfilesResponseModel(BaseModel):
    security_profiles: List[SecurityProfileSearchSummaryModel] = Field(
        alias="SecurityProfiles"
    )
    next_token: str = Field(alias="NextToken")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchVocabulariesResponseModel(BaseModel):
    vocabulary_summary_list: List[VocabularySummaryModel] = Field(
        alias="VocabularySummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContactRecordingRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    initial_contact_id: str = Field(alias="InitialContactId")
    voice_recording_configuration: VoiceRecordingConfigurationModel = Field(
        alias="VoiceRecordingConfiguration"
    )


class UserSearchSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    directory_user_id: Optional[str] = Field(default=None, alias="DirectoryUserId")
    hierarchy_group_id: Optional[str] = Field(default=None, alias="HierarchyGroupId")
    id: Optional[str] = Field(default=None, alias="Id")
    identity_info: Optional[UserIdentityInfoLiteModel] = Field(
        default=None, alias="IdentityInfo"
    )
    phone_config: Optional[UserPhoneConfigModel] = Field(
        default=None, alias="PhoneConfig"
    )
    routing_profile_id: Optional[str] = Field(default=None, alias="RoutingProfileId")
    security_profile_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityProfileIds"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    username: Optional[str] = Field(default=None, alias="Username")


class ListRulesResponseModel(BaseModel):
    rule_summary_list: List[RuleSummaryModel] = Field(alias="RuleSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBotsResponseModel(BaseModel):
    lex_bots: List[LexBotConfigModel] = Field(alias="LexBots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePhoneNumberResponseModel(BaseModel):
    claimed_phone_number_summary: ClaimedPhoneNumberSummaryModel = Field(
        alias="ClaimedPhoneNumberSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCurrentUserDataRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    filters: UserDataFiltersModel = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeContactResponseModel(BaseModel):
    contact: ContactModel = Field(alias="Contact")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueueSearchFilterModel(BaseModel):
    tag_filter: Optional[ControlPlaneTagFilterModel] = Field(
        default=None, alias="TagFilter"
    )


class RoutingProfileSearchFilterModel(BaseModel):
    tag_filter: Optional[ControlPlaneTagFilterModel] = Field(
        default=None, alias="TagFilter"
    )


class SecurityProfilesSearchFilterModel(BaseModel):
    tag_filter: Optional[ControlPlaneTagFilterModel] = Field(
        default=None, alias="TagFilter"
    )


class UserSearchFilterModel(BaseModel):
    tag_filter: Optional[ControlPlaneTagFilterModel] = Field(
        default=None, alias="TagFilter"
    )


class DescribeQueueResponseModel(BaseModel):
    queue: QueueModel = Field(alias="Queue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchQueuesResponseModel(BaseModel):
    queues: List[QueueModel] = Field(alias="Queues")
    next_token: str = Field(alias="NextToken")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRoutingProfileResponseModel(BaseModel):
    routing_profile: RoutingProfileModel = Field(alias="RoutingProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchRoutingProfilesResponseModel(BaseModel):
    routing_profiles: List[RoutingProfileModel] = Field(alias="RoutingProfiles")
    next_token: str = Field(alias="NextToken")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CurrentMetricResultModel(BaseModel):
    dimensions: Optional[DimensionsModel] = Field(default=None, alias="Dimensions")
    collections: Optional[List[CurrentMetricDataModel]] = Field(
        default=None, alias="Collections"
    )


class AssociateRoutingProfileQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    queue_configs: Sequence[RoutingProfileQueueConfigModel] = Field(
        alias="QueueConfigs"
    )


class CreateRoutingProfileRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    default_outbound_queue_id: str = Field(alias="DefaultOutboundQueueId")
    media_concurrencies: Sequence[MediaConcurrencyModel] = Field(
        alias="MediaConcurrencies"
    )
    queue_configs: Optional[Sequence[RoutingProfileQueueConfigModel]] = Field(
        default=None, alias="QueueConfigs"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateRoutingProfileQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    routing_profile_id: str = Field(alias="RoutingProfileId")
    queue_configs: Sequence[RoutingProfileQueueConfigModel] = Field(
        alias="QueueConfigs"
    )


class GetTrafficDistributionResponseModel(BaseModel):
    telephony_config: TelephonyConfigModel = Field(alias="TelephonyConfig")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrafficDistributionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    telephony_config: Optional[TelephonyConfigModel] = Field(
        default=None, alias="TelephonyConfig"
    )


class InstanceStorageConfigModel(BaseModel):
    storage_type: Literal[
        "KINESIS_FIREHOSE", "KINESIS_STREAM", "KINESIS_VIDEO_STREAM", "S3"
    ] = Field(alias="StorageType")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    s3_config: Optional[S3ConfigModel] = Field(default=None, alias="S3Config")
    kinesis_video_stream_config: Optional[KinesisVideoStreamConfigModel] = Field(
        default=None, alias="KinesisVideoStreamConfig"
    )
    kinesis_stream_config: Optional[KinesisStreamConfigModel] = Field(
        default=None, alias="KinesisStreamConfig"
    )
    kinesis_firehose_config: Optional[KinesisFirehoseConfigModel] = Field(
        default=None, alias="KinesisFirehoseConfig"
    )


class UserDataModel(BaseModel):
    user: Optional[UserReferenceModel] = Field(default=None, alias="User")
    routing_profile: Optional[RoutingProfileReferenceModel] = Field(
        default=None, alias="RoutingProfile"
    )
    hierarchy_path: Optional[HierarchyPathReferenceModel] = Field(
        default=None, alias="HierarchyPath"
    )
    status: Optional[AgentStatusReferenceModel] = Field(default=None, alias="Status")
    available_slots_by_channel: Optional[
        Dict[Literal["CHAT", "TASK", "VOICE"], int]
    ] = Field(default=None, alias="AvailableSlotsByChannel")
    max_slots_by_channel: Optional[Dict[Literal["CHAT", "TASK", "VOICE"], int]] = Field(
        default=None, alias="MaxSlotsByChannel"
    )
    active_slots_by_channel: Optional[
        Dict[Literal["CHAT", "TASK", "VOICE"], int]
    ] = Field(default=None, alias="ActiveSlotsByChannel")
    contacts: Optional[List[AgentContactReferenceModel]] = Field(
        default=None, alias="Contacts"
    )
    next_status: Optional[str] = Field(default=None, alias="NextStatus")


class HierarchyGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    level_id: Optional[str] = Field(default=None, alias="LevelId")
    hierarchy_path: Optional[HierarchyPathModel] = Field(
        default=None, alias="HierarchyPath"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DescribeUserHierarchyStructureResponseModel(BaseModel):
    hierarchy_structure: HierarchyStructureModel = Field(alias="HierarchyStructure")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserHierarchyStructureRequestModel(BaseModel):
    hierarchy_structure: HierarchyStructureUpdateModel = Field(
        alias="HierarchyStructure"
    )
    instance_id: str = Field(alias="InstanceId")


class GetMetricDataRequestGetMetricDataPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    filters: FiltersModel = Field(alias="Filters")
    historical_metrics: Sequence[HistoricalMetricModel] = Field(
        alias="HistoricalMetrics"
    )
    groupings: Optional[
        Sequence[Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE"]]
    ] = Field(default=None, alias="Groupings")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetMetricDataRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")
    filters: FiltersModel = Field(alias="Filters")
    historical_metrics: Sequence[HistoricalMetricModel] = Field(
        alias="HistoricalMetrics"
    )
    groupings: Optional[
        Sequence[Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE"]]
    ] = Field(default=None, alias="Groupings")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class HistoricalMetricDataModel(BaseModel):
    metric: Optional[HistoricalMetricModel] = Field(default=None, alias="Metric")
    value: Optional[float] = Field(default=None, alias="Value")


class CreateHoursOfOperationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    time_zone: str = Field(alias="TimeZone")
    config: Sequence[HoursOfOperationConfigModel] = Field(alias="Config")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class HoursOfOperationModel(BaseModel):
    hours_of_operation_id: Optional[str] = Field(
        default=None, alias="HoursOfOperationId"
    )
    hours_of_operation_arn: Optional[str] = Field(
        default=None, alias="HoursOfOperationArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")
    config: Optional[List[HoursOfOperationConfigModel]] = Field(
        default=None, alias="Config"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateHoursOfOperationRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    hours_of_operation_id: str = Field(alias="HoursOfOperationId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")
    config: Optional[Sequence[HoursOfOperationConfigModel]] = Field(
        default=None, alias="Config"
    )


class DescribeInstanceResponseModel(BaseModel):
    instance: InstanceModel = Field(alias="Instance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaskTemplateConstraintsModel(BaseModel):
    required_fields: Optional[Sequence[RequiredFieldInfoModel]] = Field(
        default=None, alias="RequiredFields"
    )
    read_only_fields: Optional[Sequence[ReadOnlyFieldInfoModel]] = Field(
        default=None, alias="ReadOnlyFields"
    )
    invisible_fields: Optional[Sequence[InvisibleFieldInfoModel]] = Field(
        default=None, alias="InvisibleFields"
    )


class TaskTemplateDefaultsModel(BaseModel):
    default_field_values: Optional[
        Sequence[TaskTemplateDefaultFieldValueModel]
    ] = Field(default=None, alias="DefaultFieldValues")


class ChatParticipantRoleConfigModel(BaseModel):
    participant_timer_config_list: Sequence[ParticipantTimerConfigurationModel] = Field(
        alias="ParticipantTimerConfigList"
    )


class CreateQuickConnectRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    quick_connect_config: QuickConnectConfigModel = Field(alias="QuickConnectConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class QuickConnectModel(BaseModel):
    quick_connect_arn: Optional[str] = Field(default=None, alias="QuickConnectARN")
    quick_connect_id: Optional[str] = Field(default=None, alias="QuickConnectId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    quick_connect_config: Optional[QuickConnectConfigModel] = Field(
        default=None, alias="QuickConnectConfig"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateQuickConnectConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    quick_connect_id: str = Field(alias="QuickConnectId")
    quick_connect_config: QuickConnectConfigModel = Field(alias="QuickConnectConfig")


class ListContactReferencesResponseModel(BaseModel):
    reference_summary_list: List[ReferenceSummaryModel] = Field(
        alias="ReferenceSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleActionModel(BaseModel):
    action_type: Literal[
        "ASSIGN_CONTACT_CATEGORY",
        "CREATE_TASK",
        "GENERATE_EVENTBRIDGE_EVENT",
        "SEND_NOTIFICATION",
    ] = Field(alias="ActionType")
    task_action: Optional[TaskActionDefinitionModel] = Field(
        default=None, alias="TaskAction"
    )
    event_bridge_action: Optional[EventBridgeActionDefinitionModel] = Field(
        default=None, alias="EventBridgeAction"
    )
    assign_contact_category_action: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AssignContactCategoryAction"
    )
    send_notification_action: Optional[SendNotificationActionDefinitionModel] = Field(
        default=None, alias="SendNotificationAction"
    )


class SearchUsersResponseModel(BaseModel):
    users: List[UserSearchSummaryModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchQueuesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    search_filter: Optional[QueueSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[QueueSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )


class SearchQueuesRequestSearchQueuesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    search_filter: Optional[QueueSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[QueueSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchRoutingProfilesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    search_filter: Optional[RoutingProfileSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[RoutingProfileSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )


class SearchRoutingProfilesRequestSearchRoutingProfilesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    search_filter: Optional[RoutingProfileSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[RoutingProfileSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSecurityProfilesRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    search_criteria: Optional[SecurityProfileSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )
    search_filter: Optional[SecurityProfilesSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )


class SearchSecurityProfilesRequestSearchSecurityProfilesPaginateModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    search_criteria: Optional[SecurityProfileSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )
    search_filter: Optional[SecurityProfilesSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchUsersRequestModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    search_filter: Optional[UserSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[UserSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )


class SearchUsersRequestSearchUsersPaginateModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    search_filter: Optional[UserSearchFilterModel] = Field(
        default=None, alias="SearchFilter"
    )
    search_criteria: Optional[UserSearchCriteriaModel] = Field(
        default=None, alias="SearchCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCurrentMetricDataResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    metric_results: List[CurrentMetricResultModel] = Field(alias="MetricResults")
    data_snapshot_time: datetime = Field(alias="DataSnapshotTime")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateInstanceStorageConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")
    storage_config: InstanceStorageConfigModel = Field(alias="StorageConfig")


class DescribeInstanceStorageConfigResponseModel(BaseModel):
    storage_config: InstanceStorageConfigModel = Field(alias="StorageConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceStorageConfigsResponseModel(BaseModel):
    storage_configs: List[InstanceStorageConfigModel] = Field(alias="StorageConfigs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInstanceStorageConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    association_id: str = Field(alias="AssociationId")
    resource_type: Literal[
        "AGENT_EVENTS",
        "ATTACHMENTS",
        "CALL_RECORDINGS",
        "CHAT_TRANSCRIPTS",
        "CONTACT_EVALUATIONS",
        "CONTACT_TRACE_RECORDS",
        "MEDIA_STREAMS",
        "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
        "SCHEDULED_REPORTS",
    ] = Field(alias="ResourceType")
    storage_config: InstanceStorageConfigModel = Field(alias="StorageConfig")


class GetCurrentUserDataResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    user_data_list: List[UserDataModel] = Field(alias="UserDataList")
    approximate_total_count: int = Field(alias="ApproximateTotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserHierarchyGroupResponseModel(BaseModel):
    hierarchy_group: HierarchyGroupModel = Field(alias="HierarchyGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HistoricalMetricResultModel(BaseModel):
    dimensions: Optional[DimensionsModel] = Field(default=None, alias="Dimensions")
    collections: Optional[List[HistoricalMetricDataModel]] = Field(
        default=None, alias="Collections"
    )


class DescribeHoursOfOperationResponseModel(BaseModel):
    hours_of_operation: HoursOfOperationModel = Field(alias="HoursOfOperation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTaskTemplateRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    fields: Sequence[TaskTemplateFieldModel] = Field(alias="Fields")
    description: Optional[str] = Field(default=None, alias="Description")
    contact_flow_id: Optional[str] = Field(default=None, alias="ContactFlowId")
    constraints: Optional[TaskTemplateConstraintsModel] = Field(
        default=None, alias="Constraints"
    )
    defaults: Optional[TaskTemplateDefaultsModel] = Field(
        default=None, alias="Defaults"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class GetTaskTemplateResponseModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    contact_flow_id: str = Field(alias="ContactFlowId")
    constraints: TaskTemplateConstraintsModel = Field(alias="Constraints")
    defaults: TaskTemplateDefaultsModel = Field(alias="Defaults")
    fields: List[TaskTemplateFieldModel] = Field(alias="Fields")
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    created_time: datetime = Field(alias="CreatedTime")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTaskTemplateRequestModel(BaseModel):
    task_template_id: str = Field(alias="TaskTemplateId")
    instance_id: str = Field(alias="InstanceId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    contact_flow_id: Optional[str] = Field(default=None, alias="ContactFlowId")
    constraints: Optional[TaskTemplateConstraintsModel] = Field(
        default=None, alias="Constraints"
    )
    defaults: Optional[TaskTemplateDefaultsModel] = Field(
        default=None, alias="Defaults"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    fields: Optional[Sequence[TaskTemplateFieldModel]] = Field(
        default=None, alias="Fields"
    )


class UpdateTaskTemplateResponseModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    id: str = Field(alias="Id")
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    contact_flow_id: str = Field(alias="ContactFlowId")
    constraints: TaskTemplateConstraintsModel = Field(alias="Constraints")
    defaults: TaskTemplateDefaultsModel = Field(alias="Defaults")
    fields: List[TaskTemplateFieldModel] = Field(alias="Fields")
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias="Status")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    created_time: datetime = Field(alias="CreatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateParticipantRoleConfigChannelInfoModel(BaseModel):
    chat: Optional[ChatParticipantRoleConfigModel] = Field(default=None, alias="Chat")


class DescribeQuickConnectResponseModel(BaseModel):
    quick_connect: QuickConnectModel = Field(alias="QuickConnect")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    trigger_event_source: RuleTriggerEventSourceModel = Field(
        alias="TriggerEventSource"
    )
    function: str = Field(alias="Function")
    actions: Sequence[RuleActionModel] = Field(alias="Actions")
    publish_status: Literal["DRAFT", "PUBLISHED"] = Field(alias="PublishStatus")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class RuleModel(BaseModel):
    name: str = Field(alias="Name")
    rule_id: str = Field(alias="RuleId")
    rule_arn: str = Field(alias="RuleArn")
    trigger_event_source: RuleTriggerEventSourceModel = Field(
        alias="TriggerEventSource"
    )
    function: str = Field(alias="Function")
    actions: List[RuleActionModel] = Field(alias="Actions")
    publish_status: Literal["DRAFT", "PUBLISHED"] = Field(alias="PublishStatus")
    created_time: datetime = Field(alias="CreatedTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    last_updated_by: str = Field(alias="LastUpdatedBy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    instance_id: str = Field(alias="InstanceId")
    name: str = Field(alias="Name")
    function: str = Field(alias="Function")
    actions: Sequence[RuleActionModel] = Field(alias="Actions")
    publish_status: Literal["DRAFT", "PUBLISHED"] = Field(alias="PublishStatus")


class GetMetricDataResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    metric_results: List[HistoricalMetricResultModel] = Field(alias="MetricResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateParticipantRoleConfigRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    channel_configuration: UpdateParticipantRoleConfigChannelInfoModel = Field(
        alias="ChannelConfiguration"
    )


class DescribeRuleResponseModel(BaseModel):
    rule: RuleModel = Field(alias="Rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
