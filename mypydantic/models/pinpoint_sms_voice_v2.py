# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountAttributeModel(BaseModel):
    name: Literal["ACCOUNT_TIER"] = Field(alias="Name")
    value: str = Field(alias="Value")


class AccountLimitModel(BaseModel):
    name: Literal[
        "CONFIGURATION_SETS", "OPT_OUT_LISTS", "PHONE_NUMBERS", "POOLS"
    ] = Field(alias="Name")
    used: int = Field(alias="Used")
    max: int = Field(alias="Max")


class AssociateOriginationIdentityRequestModel(BaseModel):
    pool_id: str = Field(alias="PoolId")
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CloudWatchLogsDestinationModel(BaseModel):
    iam_role_arn: str = Field(alias="IamRoleArn")
    log_group_arn: str = Field(alias="LogGroupArn")


class ConfigurationSetFilterModel(BaseModel):
    name: Literal[
        "default-message-type",
        "default-sender-id",
        "event-destination-name",
        "matching-event-types",
    ] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class KinesisFirehoseDestinationModel(BaseModel):
    iam_role_arn: str = Field(alias="IamRoleArn")
    delivery_stream_arn: str = Field(alias="DeliveryStreamArn")


class SnsDestinationModel(BaseModel):
    topic_arn: str = Field(alias="TopicArn")


class DeleteConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteDefaultMessageTypeRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteDefaultSenderIdRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")


class DeleteEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")


class DeleteKeywordRequestModel(BaseModel):
    origination_identity: str = Field(alias="OriginationIdentity")
    keyword: str = Field(alias="Keyword")


class DeleteOptOutListRequestModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")


class DeleteOptedOutNumberRequestModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_number: str = Field(alias="OptedOutNumber")


class DeletePoolRequestModel(BaseModel):
    pool_id: str = Field(alias="PoolId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAccountAttributesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeAccountLimitsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class KeywordFilterModel(BaseModel):
    name: Literal["keyword-action"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class KeywordInformationModel(BaseModel):
    keyword: str = Field(alias="Keyword")
    keyword_message: str = Field(alias="KeywordMessage")
    keyword_action: Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"] = Field(
        alias="KeywordAction"
    )


class DescribeOptOutListsRequestModel(BaseModel):
    opt_out_list_names: Optional[Sequence[str]] = Field(
        default=None, alias="OptOutListNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OptOutListInformationModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")


class OptedOutFilterModel(BaseModel):
    name: Literal["end-user-opted-out"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class OptedOutNumberInformationModel(BaseModel):
    opted_out_number: str = Field(alias="OptedOutNumber")
    opted_out_timestamp: datetime = Field(alias="OptedOutTimestamp")
    end_user_opted_out: bool = Field(alias="EndUserOptedOut")


class PhoneNumberFilterModel(BaseModel):
    name: Literal[
        "deletion-protection-enabled",
        "iso-country-code",
        "message-type",
        "number-capability",
        "number-type",
        "opt-out-list-name",
        "self-managed-opt-outs-enabled",
        "status",
        "two-way-enabled",
    ] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class PhoneNumberInformationModel(BaseModel):
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    phone_number: str = Field(alias="PhoneNumber")
    status: Literal[
        "ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"
    ] = Field(alias="Status")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    number_capabilities: List[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )
    number_type: Literal["LONG_CODE", "SHORT_CODE", "TEN_DLC", "TOLL_FREE"] = Field(
        alias="NumberType"
    )
    monthly_leasing_price: str = Field(alias="MonthlyLeasingPrice")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    two_way_channel_arn: Optional[str] = Field(default=None, alias="TwoWayChannelArn")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")


class PoolFilterModel(BaseModel):
    name: Literal[
        "deletion-protection-enabled",
        "message-type",
        "opt-out-list-name",
        "self-managed-opt-outs-enabled",
        "shared-routes-enabled",
        "status",
        "two-way-enabled",
    ] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class PoolInformationModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(alias="Status")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    shared_routes_enabled: bool = Field(alias="SharedRoutesEnabled")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    two_way_channel_arn: Optional[str] = Field(default=None, alias="TwoWayChannelArn")


class SenderIdAndCountryModel(BaseModel):
    sender_id: str = Field(alias="SenderId")
    iso_country_code: str = Field(alias="IsoCountryCode")


class SenderIdFilterModel(BaseModel):
    name: Literal["iso-country-code", "message-type", "sender-id"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class SenderIdInformationModel(BaseModel):
    sender_id_arn: str = Field(alias="SenderIdArn")
    sender_id: str = Field(alias="SenderId")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_types: List[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        alias="MessageTypes"
    )
    monthly_leasing_price: str = Field(alias="MonthlyLeasingPrice")


class DescribeSpendLimitsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SpendLimitModel(BaseModel):
    name: Literal[
        "TEXT_MESSAGE_MONTHLY_SPEND_LIMIT", "VOICE_MESSAGE_MONTHLY_SPEND_LIMIT"
    ] = Field(alias="Name")
    enforced_limit: int = Field(alias="EnforcedLimit")
    max_limit: int = Field(alias="MaxLimit")
    overridden: bool = Field(alias="Overridden")


class DisassociateOriginationIdentityRequestModel(BaseModel):
    pool_id: str = Field(alias="PoolId")
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class PoolOriginationIdentitiesFilterModel(BaseModel):
    name: Literal["iso-country-code", "number-capability"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class OriginationIdentityMetadataModel(BaseModel):
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    number_capabilities: List[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PutKeywordRequestModel(BaseModel):
    origination_identity: str = Field(alias="OriginationIdentity")
    keyword: str = Field(alias="Keyword")
    keyword_message: str = Field(alias="KeywordMessage")
    keyword_action: Optional[
        Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"]
    ] = Field(default=None, alias="KeywordAction")


class PutOptedOutNumberRequestModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_number: str = Field(alias="OptedOutNumber")


class ReleasePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class SendTextMessageRequestModel(BaseModel):
    destination_phone_number: str = Field(alias="DestinationPhoneNumber")
    origination_identity: Optional[str] = Field(
        default=None, alias="OriginationIdentity"
    )
    message_body: Optional[str] = Field(default=None, alias="MessageBody")
    message_type: Optional[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        default=None, alias="MessageType"
    )
    keyword: Optional[str] = Field(default=None, alias="Keyword")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    max_price: Optional[str] = Field(default=None, alias="MaxPrice")
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    destination_country_parameters: Optional[
        Mapping[Literal["IN_ENTITY_ID", "IN_TEMPLATE_ID"], str]
    ] = Field(default=None, alias="DestinationCountryParameters")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class SendVoiceMessageRequestModel(BaseModel):
    destination_phone_number: str = Field(alias="DestinationPhoneNumber")
    origination_identity: str = Field(alias="OriginationIdentity")
    message_body: Optional[str] = Field(default=None, alias="MessageBody")
    message_body_text_type: Optional[Literal["SSML", "TEXT"]] = Field(
        default=None, alias="MessageBodyTextType"
    )
    voice_id: Optional[
        Literal[
            "AMY",
            "ASTRID",
            "BIANCA",
            "BRIAN",
            "CAMILA",
            "CARLA",
            "CARMEN",
            "CELINE",
            "CHANTAL",
            "CONCHITA",
            "CRISTIANO",
            "DORA",
            "EMMA",
            "ENRIQUE",
            "EWA",
            "FILIZ",
            "GERAINT",
            "GIORGIO",
            "GWYNETH",
            "HANS",
            "INES",
            "IVY",
            "JACEK",
            "JAN",
            "JOANNA",
            "JOEY",
            "JUSTIN",
            "KARL",
            "KENDRA",
            "KIMBERLY",
            "LEA",
            "LIV",
            "LOTTE",
            "LUCIA",
            "LUPE",
            "MADS",
            "MAJA",
            "MARLENE",
            "MATHIEU",
            "MATTHEW",
            "MAXIM",
            "MIA",
            "MIGUEL",
            "MIZUKI",
            "NAJA",
            "NICOLE",
            "PENELOPE",
            "RAVEENA",
            "RICARDO",
            "RUBEN",
            "RUSSELL",
            "SALLI",
            "SEOYEON",
            "TAKUMI",
            "TATYANA",
            "VICKI",
            "VITORIA",
            "ZEINA",
            "ZHIYU",
        ]
    ] = Field(default=None, alias="VoiceId")
    configuration_set_name: Optional[str] = Field(
        default=None, alias="ConfigurationSetName"
    )
    max_price_per_minute: Optional[str] = Field(default=None, alias="MaxPricePerMinute")
    time_to_live: Optional[int] = Field(default=None, alias="TimeToLive")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="Context")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class SetDefaultMessageTypeRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")


class SetDefaultSenderIdRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    sender_id: str = Field(alias="SenderId")


class SetTextMessageSpendLimitOverrideRequestModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")


class SetVoiceMessageSpendLimitOverrideRequestModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdatePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    two_way_enabled: Optional[bool] = Field(default=None, alias="TwoWayEnabled")
    two_way_channel_arn: Optional[str] = Field(default=None, alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: Optional[bool] = Field(
        default=None, alias="SelfManagedOptOutsEnabled"
    )
    opt_out_list_name: Optional[str] = Field(default=None, alias="OptOutListName")
    deletion_protection_enabled: Optional[bool] = Field(
        default=None, alias="DeletionProtectionEnabled"
    )


class UpdatePoolRequestModel(BaseModel):
    pool_id: str = Field(alias="PoolId")
    two_way_enabled: Optional[bool] = Field(default=None, alias="TwoWayEnabled")
    two_way_channel_arn: Optional[str] = Field(default=None, alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: Optional[bool] = Field(
        default=None, alias="SelfManagedOptOutsEnabled"
    )
    opt_out_list_name: Optional[str] = Field(default=None, alias="OptOutListName")
    shared_routes_enabled: Optional[bool] = Field(
        default=None, alias="SharedRoutesEnabled"
    )
    deletion_protection_enabled: Optional[bool] = Field(
        default=None, alias="DeletionProtectionEnabled"
    )


class AssociateOriginationIdentityResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDefaultMessageTypeResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDefaultSenderIdResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    sender_id: str = Field(alias="SenderId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteKeywordResultModel(BaseModel):
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    keyword: str = Field(alias="Keyword")
    keyword_message: str = Field(alias="KeywordMessage")
    keyword_action: Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"] = Field(
        alias="KeywordAction"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteOptOutListResultModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteOptedOutNumberResultModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_number: str = Field(alias="OptedOutNumber")
    opted_out_timestamp: datetime = Field(alias="OptedOutTimestamp")
    end_user_opted_out: bool = Field(alias="EndUserOptedOut")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePoolResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(alias="Status")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    shared_routes_enabled: bool = Field(alias="SharedRoutesEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTextMessageSpendLimitOverrideResultModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVoiceMessageSpendLimitOverrideResultModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAttributesResultModel(BaseModel):
    account_attributes: List[AccountAttributeModel] = Field(alias="AccountAttributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountLimitsResultModel(BaseModel):
    account_limits: List[AccountLimitModel] = Field(alias="AccountLimits")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateOriginationIdentityResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutKeywordResultModel(BaseModel):
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    keyword: str = Field(alias="Keyword")
    keyword_message: str = Field(alias="KeywordMessage")
    keyword_action: Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"] = Field(
        alias="KeywordAction"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutOptedOutNumberResultModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_number: str = Field(alias="OptedOutNumber")
    opted_out_timestamp: datetime = Field(alias="OptedOutTimestamp")
    end_user_opted_out: bool = Field(alias="EndUserOptedOut")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReleasePhoneNumberResultModel(BaseModel):
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    phone_number_id: str = Field(alias="PhoneNumberId")
    phone_number: str = Field(alias="PhoneNumber")
    status: Literal[
        "ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"
    ] = Field(alias="Status")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    number_capabilities: List[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )
    number_type: Literal["LONG_CODE", "SHORT_CODE", "TEN_DLC", "TOLL_FREE"] = Field(
        alias="NumberType"
    )
    monthly_leasing_price: str = Field(alias="MonthlyLeasingPrice")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendTextMessageResultModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendVoiceMessageResultModel(BaseModel):
    message_id: str = Field(alias="MessageId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetDefaultMessageTypeResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetDefaultSenderIdResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    sender_id: str = Field(alias="SenderId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetTextMessageSpendLimitOverrideResultModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetVoiceMessageSpendLimitOverrideResultModel(BaseModel):
    monthly_limit: int = Field(alias="MonthlyLimit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePhoneNumberResultModel(BaseModel):
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    phone_number_id: str = Field(alias="PhoneNumberId")
    phone_number: str = Field(alias="PhoneNumber")
    status: Literal[
        "ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"
    ] = Field(alias="Status")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    number_capabilities: List[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )
    number_type: Literal["LONG_CODE", "SHORT_CODE", "TEN_DLC", "TOLL_FREE"] = Field(
        alias="NumberType"
    )
    monthly_leasing_price: str = Field(alias="MonthlyLeasingPrice")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePoolResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(alias="Status")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    shared_routes_enabled: bool = Field(alias="SharedRoutesEnabled")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationSetsRequestModel(BaseModel):
    configuration_set_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationSetNames"
    )
    filters: Optional[Sequence[ConfigurationSetFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class CreateConfigurationSetRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateConfigurationSetResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    tags: List[TagModel] = Field(alias="Tags")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOptOutListRequestModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreateOptOutListResultModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    tags: List[TagModel] = Field(alias="Tags")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePoolRequestModel(BaseModel):
    origination_identity: str = Field(alias="OriginationIdentity")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    deletion_protection_enabled: Optional[bool] = Field(
        default=None, alias="DeletionProtectionEnabled"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CreatePoolResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    status: Literal["ACTIVE", "CREATING", "DELETING"] = Field(alias="Status")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    shared_routes_enabled: bool = Field(alias="SharedRoutesEnabled")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    tags: List[TagModel] = Field(alias="Tags")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResultModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestPhoneNumberRequestModel(BaseModel):
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    number_capabilities: Sequence[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )
    number_type: Literal["LONG_CODE", "TEN_DLC", "TOLL_FREE"] = Field(
        alias="NumberType"
    )
    opt_out_list_name: Optional[str] = Field(default=None, alias="OptOutListName")
    pool_id: Optional[str] = Field(default=None, alias="PoolId")
    registration_id: Optional[str] = Field(default=None, alias="RegistrationId")
    deletion_protection_enabled: Optional[bool] = Field(
        default=None, alias="DeletionProtectionEnabled"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class RequestPhoneNumberResultModel(BaseModel):
    phone_number_arn: str = Field(alias="PhoneNumberArn")
    phone_number_id: str = Field(alias="PhoneNumberId")
    phone_number: str = Field(alias="PhoneNumber")
    status: Literal[
        "ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"
    ] = Field(alias="Status")
    iso_country_code: str = Field(alias="IsoCountryCode")
    message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(alias="MessageType")
    number_capabilities: List[Literal["SMS", "VOICE"]] = Field(
        alias="NumberCapabilities"
    )
    number_type: Literal["LONG_CODE", "TEN_DLC", "TOLL_FREE"] = Field(
        alias="NumberType"
    )
    monthly_leasing_price: str = Field(alias="MonthlyLeasingPrice")
    two_way_enabled: bool = Field(alias="TwoWayEnabled")
    two_way_channel_arn: str = Field(alias="TwoWayChannelArn")
    self_managed_opt_outs_enabled: bool = Field(alias="SelfManagedOptOutsEnabled")
    opt_out_list_name: str = Field(alias="OptOutListName")
    deletion_protection_enabled: bool = Field(alias="DeletionProtectionEnabled")
    pool_id: str = Field(alias="PoolId")
    tags: List[TagModel] = Field(alias="Tags")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")
    matching_event_types: Sequence[
        Literal[
            "ALL",
            "TEXT_ALL",
            "TEXT_BLOCKED",
            "TEXT_CARRIER_BLOCKED",
            "TEXT_CARRIER_UNREACHABLE",
            "TEXT_DELIVERED",
            "TEXT_INVALID",
            "TEXT_INVALID_MESSAGE",
            "TEXT_PENDING",
            "TEXT_QUEUED",
            "TEXT_SENT",
            "TEXT_SPAM",
            "TEXT_SUCCESSFUL",
            "TEXT_TTL_EXPIRED",
            "TEXT_UNKNOWN",
            "TEXT_UNREACHABLE",
            "VOICE_ALL",
            "VOICE_ANSWERED",
            "VOICE_BUSY",
            "VOICE_COMPLETED",
            "VOICE_FAILED",
            "VOICE_INITIATED",
            "VOICE_NO_ANSWER",
            "VOICE_RINGING",
            "VOICE_TTL_EXPIRED",
        ]
    ] = Field(alias="MatchingEventTypes")
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="CloudWatchLogsDestination"
    )
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class EventDestinationModel(BaseModel):
    event_destination_name: str = Field(alias="EventDestinationName")
    enabled: bool = Field(alias="Enabled")
    matching_event_types: List[
        Literal[
            "ALL",
            "TEXT_ALL",
            "TEXT_BLOCKED",
            "TEXT_CARRIER_BLOCKED",
            "TEXT_CARRIER_UNREACHABLE",
            "TEXT_DELIVERED",
            "TEXT_INVALID",
            "TEXT_INVALID_MESSAGE",
            "TEXT_PENDING",
            "TEXT_QUEUED",
            "TEXT_SENT",
            "TEXT_SPAM",
            "TEXT_SUCCESSFUL",
            "TEXT_TTL_EXPIRED",
            "TEXT_UNKNOWN",
            "TEXT_UNREACHABLE",
            "VOICE_ALL",
            "VOICE_ANSWERED",
            "VOICE_BUSY",
            "VOICE_COMPLETED",
            "VOICE_FAILED",
            "VOICE_INITIATED",
            "VOICE_NO_ANSWER",
            "VOICE_RINGING",
            "VOICE_TTL_EXPIRED",
        ]
    ] = Field(alias="MatchingEventTypes")
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="CloudWatchLogsDestination"
    )
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )


class UpdateEventDestinationRequestModel(BaseModel):
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination_name: str = Field(alias="EventDestinationName")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    matching_event_types: Optional[
        Sequence[
            Literal[
                "ALL",
                "TEXT_ALL",
                "TEXT_BLOCKED",
                "TEXT_CARRIER_BLOCKED",
                "TEXT_CARRIER_UNREACHABLE",
                "TEXT_DELIVERED",
                "TEXT_INVALID",
                "TEXT_INVALID_MESSAGE",
                "TEXT_PENDING",
                "TEXT_QUEUED",
                "TEXT_SENT",
                "TEXT_SPAM",
                "TEXT_SUCCESSFUL",
                "TEXT_TTL_EXPIRED",
                "TEXT_UNKNOWN",
                "TEXT_UNREACHABLE",
                "VOICE_ALL",
                "VOICE_ANSWERED",
                "VOICE_BUSY",
                "VOICE_COMPLETED",
                "VOICE_FAILED",
                "VOICE_INITIATED",
                "VOICE_NO_ANSWER",
                "VOICE_RINGING",
                "VOICE_TTL_EXPIRED",
            ]
        ]
    ] = Field(default=None, alias="MatchingEventTypes")
    cloud_watch_logs_destination: Optional[CloudWatchLogsDestinationModel] = Field(
        default=None, alias="CloudWatchLogsDestination"
    )
    kinesis_firehose_destination: Optional[KinesisFirehoseDestinationModel] = Field(
        default=None, alias="KinesisFirehoseDestination"
    )
    sns_destination: Optional[SnsDestinationModel] = Field(
        default=None, alias="SnsDestination"
    )


class DescribeAccountAttributesRequestDescribeAccountAttributesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAccountLimitsRequestDescribeAccountLimitsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigurationSetsRequestDescribeConfigurationSetsPaginateModel(BaseModel):
    configuration_set_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationSetNames"
    )
    filters: Optional[Sequence[ConfigurationSetFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOptOutListsRequestDescribeOptOutListsPaginateModel(BaseModel):
    opt_out_list_names: Optional[Sequence[str]] = Field(
        default=None, alias="OptOutListNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSpendLimitsRequestDescribeSpendLimitsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeKeywordsRequestDescribeKeywordsPaginateModel(BaseModel):
    origination_identity: str = Field(alias="OriginationIdentity")
    keywords: Optional[Sequence[str]] = Field(default=None, alias="Keywords")
    filters: Optional[Sequence[KeywordFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeKeywordsRequestModel(BaseModel):
    origination_identity: str = Field(alias="OriginationIdentity")
    keywords: Optional[Sequence[str]] = Field(default=None, alias="Keywords")
    filters: Optional[Sequence[KeywordFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeKeywordsResultModel(BaseModel):
    origination_identity_arn: str = Field(alias="OriginationIdentityArn")
    origination_identity: str = Field(alias="OriginationIdentity")
    keywords: List[KeywordInformationModel] = Field(alias="Keywords")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOptOutListsResultModel(BaseModel):
    opt_out_lists: List[OptOutListInformationModel] = Field(alias="OptOutLists")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOptedOutNumbersRequestDescribeOptedOutNumbersPaginateModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_numbers: Optional[Sequence[str]] = Field(
        default=None, alias="OptedOutNumbers"
    )
    filters: Optional[Sequence[OptedOutFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOptedOutNumbersRequestModel(BaseModel):
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_numbers: Optional[Sequence[str]] = Field(
        default=None, alias="OptedOutNumbers"
    )
    filters: Optional[Sequence[OptedOutFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeOptedOutNumbersResultModel(BaseModel):
    opt_out_list_arn: str = Field(alias="OptOutListArn")
    opt_out_list_name: str = Field(alias="OptOutListName")
    opted_out_numbers: List[OptedOutNumberInformationModel] = Field(
        alias="OptedOutNumbers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePhoneNumbersRequestDescribePhoneNumbersPaginateModel(BaseModel):
    phone_number_ids: Optional[Sequence[str]] = Field(
        default=None, alias="PhoneNumberIds"
    )
    filters: Optional[Sequence[PhoneNumberFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePhoneNumbersRequestModel(BaseModel):
    phone_number_ids: Optional[Sequence[str]] = Field(
        default=None, alias="PhoneNumberIds"
    )
    filters: Optional[Sequence[PhoneNumberFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribePhoneNumbersResultModel(BaseModel):
    phone_numbers: List[PhoneNumberInformationModel] = Field(alias="PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePoolsRequestDescribePoolsPaginateModel(BaseModel):
    pool_ids: Optional[Sequence[str]] = Field(default=None, alias="PoolIds")
    filters: Optional[Sequence[PoolFilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePoolsRequestModel(BaseModel):
    pool_ids: Optional[Sequence[str]] = Field(default=None, alias="PoolIds")
    filters: Optional[Sequence[PoolFilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribePoolsResultModel(BaseModel):
    pools: List[PoolInformationModel] = Field(alias="Pools")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSenderIdsRequestDescribeSenderIdsPaginateModel(BaseModel):
    sender_ids: Optional[Sequence[SenderIdAndCountryModel]] = Field(
        default=None, alias="SenderIds"
    )
    filters: Optional[Sequence[SenderIdFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSenderIdsRequestModel(BaseModel):
    sender_ids: Optional[Sequence[SenderIdAndCountryModel]] = Field(
        default=None, alias="SenderIds"
    )
    filters: Optional[Sequence[SenderIdFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeSenderIdsResultModel(BaseModel):
    sender_ids: List[SenderIdInformationModel] = Field(alias="SenderIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSpendLimitsResultModel(BaseModel):
    spend_limits: List[SpendLimitModel] = Field(alias="SpendLimits")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoolOriginationIdentitiesRequestListPoolOriginationIdentitiesPaginateModel(
    BaseModel
):
    pool_id: str = Field(alias="PoolId")
    filters: Optional[Sequence[PoolOriginationIdentitiesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoolOriginationIdentitiesRequestModel(BaseModel):
    pool_id: str = Field(alias="PoolId")
    filters: Optional[Sequence[PoolOriginationIdentitiesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPoolOriginationIdentitiesResultModel(BaseModel):
    pool_arn: str = Field(alias="PoolArn")
    pool_id: str = Field(alias="PoolId")
    origination_identities: List[OriginationIdentityMetadataModel] = Field(
        alias="OriginationIdentities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationSetInformationModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destinations: List[EventDestinationModel] = Field(alias="EventDestinations")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    default_message_type: Optional[Literal["PROMOTIONAL", "TRANSACTIONAL"]] = Field(
        default=None, alias="DefaultMessageType"
    )
    default_sender_id: Optional[str] = Field(default=None, alias="DefaultSenderId")


class CreateEventDestinationResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: EventDestinationModel = Field(alias="EventDestination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConfigurationSetResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destinations: List[EventDestinationModel] = Field(alias="EventDestinations")
    default_message_type: Literal["PROMOTIONAL", "TRANSACTIONAL"] = Field(
        alias="DefaultMessageType"
    )
    default_sender_id: str = Field(alias="DefaultSenderId")
    created_timestamp: datetime = Field(alias="CreatedTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEventDestinationResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: EventDestinationModel = Field(alias="EventDestination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEventDestinationResultModel(BaseModel):
    configuration_set_arn: str = Field(alias="ConfigurationSetArn")
    configuration_set_name: str = Field(alias="ConfigurationSetName")
    event_destination: EventDestinationModel = Field(alias="EventDestination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationSetsResultModel(BaseModel):
    configuration_sets: List[ConfigurationSetInformationModel] = Field(
        alias="ConfigurationSets"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
