# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressModel(BaseModel):
    street_name: Optional[str] = Field(default=None, alias="streetName")
    street_suffix: Optional[str] = Field(default=None, alias="streetSuffix")
    post_directional: Optional[str] = Field(default=None, alias="postDirectional")
    pre_directional: Optional[str] = Field(default=None, alias="preDirectional")
    street_number: Optional[str] = Field(default=None, alias="streetNumber")
    city: Optional[str] = Field(default=None, alias="city")
    state: Optional[str] = Field(default=None, alias="state")
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    postal_code_plus4: Optional[str] = Field(default=None, alias="postalCodePlus4")
    country: Optional[str] = Field(default=None, alias="country")


class AssociatePhoneNumbersWithVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")
    force_associate: Optional[bool] = Field(default=None, alias="ForceAssociate")


class PhoneNumberErrorModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "BadRequest",
            "Conflict",
            "Forbidden",
            "Gone",
            "NotFound",
            "PhoneNumberAssociationsExist",
            "PreconditionFailed",
            "ResourceLimitExceeded",
            "ServiceFailure",
            "ServiceUnavailable",
            "Throttled",
            "Throttling",
            "Unauthorized",
            "Unprocessable",
            "VoiceConnectorGroupAssociationsExist",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociatePhoneNumbersWithVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")
    force_associate: Optional[bool] = Field(default=None, alias="ForceAssociate")


class BatchDeletePhoneNumberRequestModel(BaseModel):
    phone_number_ids: Sequence[str] = Field(alias="PhoneNumberIds")


class UpdatePhoneNumberRequestItemModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    product_type: Optional[
        Literal["SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    calling_name: Optional[str] = Field(default=None, alias="CallingName")


class CandidateAddressModel(BaseModel):
    street_info: Optional[str] = Field(default=None, alias="streetInfo")
    street_number: Optional[str] = Field(default=None, alias="streetNumber")
    city: Optional[str] = Field(default=None, alias="city")
    state: Optional[str] = Field(default=None, alias="state")
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    postal_code_plus4: Optional[str] = Field(default=None, alias="postalCodePlus4")
    country: Optional[str] = Field(default=None, alias="country")


class CreatePhoneNumberOrderRequestModel(BaseModel):
    product_type: Literal["SipMediaApplicationDialIn", "VoiceConnector"] = Field(
        alias="ProductType"
    )
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class GeoMatchParamsModel(BaseModel):
    country: str = Field(alias="Country")
    area_code: str = Field(alias="AreaCode")


class CreateSipMediaApplicationCallRequestModel(BaseModel):
    from_phone_number: str = Field(alias="FromPhoneNumber")
    to_phone_number: str = Field(alias="ToPhoneNumber")
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    sip_headers: Optional[Mapping[str, str]] = Field(default=None, alias="SipHeaders")
    arguments_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="ArgumentsMap"
    )


class SipMediaApplicationCallModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")


class SipMediaApplicationEndpointModel(BaseModel):
    lambda_arn: Optional[str] = Field(default=None, alias="LambdaArn")


class SipRuleTargetApplicationModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class VoiceConnectorItemModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    priority: int = Field(alias="Priority")


class CreateVoiceConnectorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    require_encryption: bool = Field(alias="RequireEncryption")
    aws_region: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "us-east-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="AwsRegion")


class VoiceConnectorModel(BaseModel):
    voice_connector_id: Optional[str] = Field(default=None, alias="VoiceConnectorId")
    aws_region: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "us-east-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="AwsRegion")
    name: Optional[str] = Field(default=None, alias="Name")
    outbound_host_name: Optional[str] = Field(default=None, alias="OutboundHostName")
    require_encryption: Optional[bool] = Field(default=None, alias="RequireEncryption")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    voice_connector_arn: Optional[str] = Field(default=None, alias="VoiceConnectorArn")


class CredentialModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")


class DNISEmergencyCallingConfigurationModel(BaseModel):
    emergency_phone_number: str = Field(alias="EmergencyPhoneNumber")
    calling_country: str = Field(alias="CallingCountry")
    test_phone_number: Optional[str] = Field(default=None, alias="TestPhoneNumber")


class DeletePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class DeleteProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")


class DeleteSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class DeleteSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")


class DeleteVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")


class DeleteVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DeleteVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    usernames: Sequence[str] = Field(alias="Usernames")


class DeleteVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class DisassociatePhoneNumbersFromVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    e164_phone_numbers: Sequence[str] = Field(alias="E164PhoneNumbers")


class VoiceConnectorSettingsModel(BaseModel):
    cdr_bucket: Optional[str] = Field(default=None, alias="CdrBucket")


class GetPhoneNumberOrderRequestModel(BaseModel):
    phone_number_order_id: str = Field(alias="PhoneNumberOrderId")


class GetPhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class GetProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")


class GetSipMediaApplicationAlexaSkillConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class SipMediaApplicationAlexaSkillConfigurationModel(BaseModel):
    alexa_skill_status: Literal["ACTIVE", "INACTIVE"] = Field(alias="AlexaSkillStatus")
    alexa_skill_ids: List[str] = Field(alias="AlexaSkillIds")


class GetSipMediaApplicationLoggingConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class SipMediaApplicationLoggingConfigurationModel(BaseModel):
    enable_sip_media_application_message_logs: Optional[bool] = Field(
        default=None, alias="EnableSipMediaApplicationMessageLogs"
    )


class GetSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")


class GetSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")


class GetVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")


class GetVoiceConnectorLoggingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class LoggingConfigurationModel(BaseModel):
    enable_s_ip_logs: Optional[bool] = Field(default=None, alias="EnableSIPLogs")
    enable_media_metric_logs: Optional[bool] = Field(
        default=None, alias="EnableMediaMetricLogs"
    )


class GetVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class ProxyModel(BaseModel):
    default_session_expiry_minutes: Optional[int] = Field(
        default=None, alias="DefaultSessionExpiryMinutes"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    fall_back_phone_number: Optional[str] = Field(
        default=None, alias="FallBackPhoneNumber"
    )
    phone_number_countries: Optional[List[str]] = Field(
        default=None, alias="PhoneNumberCountries"
    )


class GetVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class GetVoiceConnectorTerminationHealthRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class TerminationHealthModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    source: Optional[str] = Field(default=None, alias="Source")


class GetVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class TerminationModel(BaseModel):
    cps_limit: Optional[int] = Field(default=None, alias="CpsLimit")
    default_phone_number: Optional[str] = Field(
        default=None, alias="DefaultPhoneNumber"
    )
    calling_regions: Optional[List[str]] = Field(default=None, alias="CallingRegions")
    cidr_allowed_list: Optional[List[str]] = Field(
        default=None, alias="CidrAllowedList"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class ListPhoneNumberOrdersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPhoneNumbersRequestModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    product_type: Optional[
        Literal["SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    filter_name: Optional[
        Literal["SipRuleId", "VoiceConnectorGroupId", "VoiceConnectorId"]
    ] = Field(default=None, alias="FilterName")
    filter_value: Optional[str] = Field(default=None, alias="FilterValue")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListProxySessionsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    status: Optional[Literal["Closed", "InProgress", "Open"]] = Field(
        default=None, alias="Status"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListSipMediaApplicationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSipRulesRequestModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSupportedPhoneNumberCountriesRequestModel(BaseModel):
    product_type: Literal["SipMediaApplicationDialIn", "VoiceConnector"] = Field(
        alias="ProductType"
    )


class PhoneNumberCountryModel(BaseModel):
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    supported_phone_number_types: Optional[List[Literal["Local", "TollFree"]]] = Field(
        default=None, alias="SupportedPhoneNumberTypes"
    )


class ListVoiceConnectorGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")


class ListVoiceConnectorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OrderedPhoneNumberModel(BaseModel):
    e164_phone_number: Optional[str] = Field(default=None, alias="E164PhoneNumber")
    status: Optional[Literal["Acquired", "Failed", "Processing"]] = Field(
        default=None, alias="Status"
    )


class OriginationRouteModel(BaseModel):
    host: Optional[str] = Field(default=None, alias="Host")
    port: Optional[int] = Field(default=None, alias="Port")
    protocol: Optional[Literal["TCP", "UDP"]] = Field(default=None, alias="Protocol")
    priority: Optional[int] = Field(default=None, alias="Priority")
    weight: Optional[int] = Field(default=None, alias="Weight")


class ParticipantModel(BaseModel):
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    proxy_phone_number: Optional[str] = Field(default=None, alias="ProxyPhoneNumber")


class PhoneNumberAssociationModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    name: Optional[
        Literal["SipRuleId", "VoiceConnectorGroupId", "VoiceConnectorId"]
    ] = Field(default=None, alias="Name")
    associated_timestamp: Optional[datetime] = Field(
        default=None, alias="AssociatedTimestamp"
    )


class PhoneNumberCapabilitiesModel(BaseModel):
    inbound_call: Optional[bool] = Field(default=None, alias="InboundCall")
    outbound_call: Optional[bool] = Field(default=None, alias="OutboundCall")
    inbound_s_ms: Optional[bool] = Field(default=None, alias="InboundSMS")
    outbound_s_ms: Optional[bool] = Field(default=None, alias="OutboundSMS")
    inbound_mms: Optional[bool] = Field(default=None, alias="InboundMMS")
    outbound_mms: Optional[bool] = Field(default=None, alias="OutboundMMS")


class PutVoiceConnectorProxyRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    default_session_expiry_minutes: int = Field(alias="DefaultSessionExpiryMinutes")
    phone_number_pool_countries: Sequence[str] = Field(alias="PhoneNumberPoolCountries")
    fall_back_phone_number: Optional[str] = Field(
        default=None, alias="FallBackPhoneNumber"
    )
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class RestorePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")


class SearchAvailablePhoneNumbersRequestModel(BaseModel):
    area_code: Optional[str] = Field(default=None, alias="AreaCode")
    city: Optional[str] = Field(default=None, alias="City")
    country: Optional[str] = Field(default=None, alias="Country")
    state: Optional[str] = Field(default=None, alias="State")
    toll_free_prefix: Optional[str] = Field(default=None, alias="TollFreePrefix")
    phone_number_type: Optional[Literal["Local", "TollFree"]] = Field(
        default=None, alias="PhoneNumberType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StreamingNotificationTargetModel(BaseModel):
    notification_target: Optional[Literal["EventBridge", "SNS", "SQS"]] = Field(
        default=None, alias="NotificationTarget"
    )


class UpdatePhoneNumberRequestModel(BaseModel):
    phone_number_id: str = Field(alias="PhoneNumberId")
    product_type: Optional[
        Literal["SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    calling_name: Optional[str] = Field(default=None, alias="CallingName")


class UpdatePhoneNumberSettingsRequestModel(BaseModel):
    calling_name: str = Field(alias="CallingName")


class UpdateProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    proxy_session_id: str = Field(alias="ProxySessionId")
    capabilities: Sequence[Literal["SMS", "Voice"]] = Field(alias="Capabilities")
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")


class UpdateSipMediaApplicationCallRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    transaction_id: str = Field(alias="TransactionId")
    arguments: Mapping[str, str] = Field(alias="Arguments")


class UpdateVoiceConnectorRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    name: str = Field(alias="Name")
    require_encryption: bool = Field(alias="RequireEncryption")


class ValidateE911AddressRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    street_number: str = Field(alias="StreetNumber")
    street_info: str = Field(alias="StreetInfo")
    city: str = Field(alias="City")
    state: str = Field(alias="State")
    country: str = Field(alias="Country")
    postal_code: str = Field(alias="PostalCode")


class AssociatePhoneNumbersWithVoiceConnectorGroupResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociatePhoneNumbersWithVoiceConnectorResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDeletePhoneNumberResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePhoneNumberResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePhoneNumbersFromVoiceConnectorResponseModel(BaseModel):
    phone_number_errors: List[PhoneNumberErrorModel] = Field(alias="PhoneNumberErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberSettingsResponseModel(BaseModel):
    calling_name: str = Field(alias="CallingName")
    calling_name_updated_timestamp: datetime = Field(
        alias="CallingNameUpdatedTimestamp"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableVoiceConnectorRegionsResponseModel(BaseModel):
    voice_connector_regions: List[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "us-east-1",
            "us-west-2",
        ]
    ] = Field(alias="VoiceConnectorRegions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorTerminationCredentialsResponseModel(BaseModel):
    usernames: List[str] = Field(alias="Usernames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAvailablePhoneNumbersResponseModel(BaseModel):
    e164_phone_numbers: List[str] = Field(alias="E164PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdatePhoneNumberRequestModel(BaseModel):
    update_phone_number_request_items: Sequence[
        UpdatePhoneNumberRequestItemModel
    ] = Field(alias="UpdatePhoneNumberRequestItems")


class ValidateE911AddressResponseModel(BaseModel):
    validation_result: int = Field(alias="ValidationResult")
    address_external_id: str = Field(alias="AddressExternalId")
    address: AddressModel = Field(alias="Address")
    candidate_address_list: List[CandidateAddressModel] = Field(
        alias="CandidateAddressList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProxySessionRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    participant_phone_numbers: Sequence[str] = Field(alias="ParticipantPhoneNumbers")
    capabilities: Sequence[Literal["SMS", "Voice"]] = Field(alias="Capabilities")
    name: Optional[str] = Field(default=None, alias="Name")
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")
    number_selection_behavior: Optional[Literal["AvoidSticky", "PreferSticky"]] = Field(
        default=None, alias="NumberSelectionBehavior"
    )
    geo_match_level: Optional[Literal["AreaCode", "Country"]] = Field(
        default=None, alias="GeoMatchLevel"
    )
    geo_match_params: Optional[GeoMatchParamsModel] = Field(
        default=None, alias="GeoMatchParams"
    )


class CreateSipMediaApplicationCallResponseModel(BaseModel):
    sip_media_application_call: SipMediaApplicationCallModel = Field(
        alias="SipMediaApplicationCall"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipMediaApplicationCallResponseModel(BaseModel):
    sip_media_application_call: SipMediaApplicationCallModel = Field(
        alias="SipMediaApplicationCall"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSipMediaApplicationRequestModel(BaseModel):
    aws_region: str = Field(alias="AwsRegion")
    name: str = Field(alias="Name")
    endpoints: Sequence[SipMediaApplicationEndpointModel] = Field(alias="Endpoints")


class SipMediaApplicationModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    name: Optional[str] = Field(default=None, alias="Name")
    endpoints: Optional[List[SipMediaApplicationEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class UpdateSipMediaApplicationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    name: Optional[str] = Field(default=None, alias="Name")
    endpoints: Optional[Sequence[SipMediaApplicationEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )


class CreateSipRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    trigger_type: Literal["RequestUriHostname", "ToPhoneNumber"] = Field(
        alias="TriggerType"
    )
    trigger_value: str = Field(alias="TriggerValue")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    target_applications: Optional[Sequence[SipRuleTargetApplicationModel]] = Field(
        default=None, alias="TargetApplications"
    )


class SipRuleModel(BaseModel):
    sip_rule_id: Optional[str] = Field(default=None, alias="SipRuleId")
    name: Optional[str] = Field(default=None, alias="Name")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    trigger_type: Optional[Literal["RequestUriHostname", "ToPhoneNumber"]] = Field(
        default=None, alias="TriggerType"
    )
    trigger_value: Optional[str] = Field(default=None, alias="TriggerValue")
    target_applications: Optional[List[SipRuleTargetApplicationModel]] = Field(
        default=None, alias="TargetApplications"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class UpdateSipRuleRequestModel(BaseModel):
    sip_rule_id: str = Field(alias="SipRuleId")
    name: str = Field(alias="Name")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    target_applications: Optional[Sequence[SipRuleTargetApplicationModel]] = Field(
        default=None, alias="TargetApplications"
    )


class CreateVoiceConnectorGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    voice_connector_items: Optional[Sequence[VoiceConnectorItemModel]] = Field(
        default=None, alias="VoiceConnectorItems"
    )


class UpdateVoiceConnectorGroupRequestModel(BaseModel):
    voice_connector_group_id: str = Field(alias="VoiceConnectorGroupId")
    name: str = Field(alias="Name")
    voice_connector_items: Sequence[VoiceConnectorItemModel] = Field(
        alias="VoiceConnectorItems"
    )


class VoiceConnectorGroupModel(BaseModel):
    voice_connector_group_id: Optional[str] = Field(
        default=None, alias="VoiceConnectorGroupId"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    voice_connector_items: Optional[List[VoiceConnectorItemModel]] = Field(
        default=None, alias="VoiceConnectorItems"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    voice_connector_group_arn: Optional[str] = Field(
        default=None, alias="VoiceConnectorGroupArn"
    )


class CreateVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorsResponseModel(BaseModel):
    voice_connectors: List[VoiceConnectorModel] = Field(alias="VoiceConnectors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceConnectorResponseModel(BaseModel):
    voice_connector: VoiceConnectorModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorTerminationCredentialsRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    credentials: Optional[Sequence[CredentialModel]] = Field(
        default=None, alias="Credentials"
    )


class EmergencyCallingConfigurationModel(BaseModel):
    dnis: Optional[List[DNISEmergencyCallingConfigurationModel]] = Field(
        default=None, alias="DNIS"
    )


class GetGlobalSettingsResponseModel(BaseModel):
    voice_connector: VoiceConnectorSettingsModel = Field(alias="VoiceConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGlobalSettingsRequestModel(BaseModel):
    voice_connector: Optional[VoiceConnectorSettingsModel] = Field(
        default=None, alias="VoiceConnector"
    )


class GetSipMediaApplicationAlexaSkillConfigurationResponseModel(BaseModel):
    sip_media_application_alexa_skill_configuration: SipMediaApplicationAlexaSkillConfigurationModel = Field(
        alias="SipMediaApplicationAlexaSkillConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSipMediaApplicationAlexaSkillConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    sip_media_application_alexa_skill_configuration: Optional[
        SipMediaApplicationAlexaSkillConfigurationModel
    ] = Field(default=None, alias="SipMediaApplicationAlexaSkillConfiguration")


class PutSipMediaApplicationAlexaSkillConfigurationResponseModel(BaseModel):
    sip_media_application_alexa_skill_configuration: SipMediaApplicationAlexaSkillConfigurationModel = Field(
        alias="SipMediaApplicationAlexaSkillConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipMediaApplicationLoggingConfigurationResponseModel(BaseModel):
    sip_media_application_logging_configuration: SipMediaApplicationLoggingConfigurationModel = Field(
        alias="SipMediaApplicationLoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSipMediaApplicationLoggingConfigurationRequestModel(BaseModel):
    sip_media_application_id: str = Field(alias="SipMediaApplicationId")
    sip_media_application_logging_configuration: Optional[
        SipMediaApplicationLoggingConfigurationModel
    ] = Field(default=None, alias="SipMediaApplicationLoggingConfiguration")


class PutSipMediaApplicationLoggingConfigurationResponseModel(BaseModel):
    sip_media_application_logging_configuration: SipMediaApplicationLoggingConfigurationModel = Field(
        alias="SipMediaApplicationLoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorLoggingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )


class PutVoiceConnectorLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorProxyResponseModel(BaseModel):
    proxy: ProxyModel = Field(alias="Proxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorProxyResponseModel(BaseModel):
    proxy: ProxyModel = Field(alias="Proxy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorTerminationHealthResponseModel(BaseModel):
    termination_health: TerminationHealthModel = Field(alias="TerminationHealth")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorTerminationResponseModel(BaseModel):
    termination: TerminationModel = Field(alias="Termination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorTerminationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    termination: TerminationModel = Field(alias="Termination")


class PutVoiceConnectorTerminationResponseModel(BaseModel):
    termination: TerminationModel = Field(alias="Termination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSipRulesRequestListSipRulesPaginateModel(BaseModel):
    sip_media_application_id: Optional[str] = Field(
        default=None, alias="SipMediaApplicationId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSupportedPhoneNumberCountriesResponseModel(BaseModel):
    phone_number_countries: List[PhoneNumberCountryModel] = Field(
        alias="PhoneNumberCountries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PhoneNumberOrderModel(BaseModel):
    phone_number_order_id: Optional[str] = Field(
        default=None, alias="PhoneNumberOrderId"
    )
    product_type: Optional[
        Literal["SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    status: Optional[
        Literal[
            "CancelRequested",
            "Cancelled",
            "ChangeRequested",
            "Exception",
            "FOC",
            "Failed",
            "Partial",
            "PendingDocuments",
            "Processing",
            "Submitted",
            "Successful",
        ]
    ] = Field(default=None, alias="Status")
    order_type: Optional[Literal["New", "Porting"]] = Field(
        default=None, alias="OrderType"
    )
    ordered_phone_numbers: Optional[List[OrderedPhoneNumberModel]] = Field(
        default=None, alias="OrderedPhoneNumbers"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )


class OriginationModel(BaseModel):
    routes: Optional[List[OriginationRouteModel]] = Field(default=None, alias="Routes")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")


class ProxySessionModel(BaseModel):
    voice_connector_id: Optional[str] = Field(default=None, alias="VoiceConnectorId")
    proxy_session_id: Optional[str] = Field(default=None, alias="ProxySessionId")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["Closed", "InProgress", "Open"]] = Field(
        default=None, alias="Status"
    )
    expiry_minutes: Optional[int] = Field(default=None, alias="ExpiryMinutes")
    capabilities: Optional[List[Literal["SMS", "Voice"]]] = Field(
        default=None, alias="Capabilities"
    )
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    ended_timestamp: Optional[datetime] = Field(default=None, alias="EndedTimestamp")
    participants: Optional[List[ParticipantModel]] = Field(
        default=None, alias="Participants"
    )
    number_selection_behavior: Optional[Literal["AvoidSticky", "PreferSticky"]] = Field(
        default=None, alias="NumberSelectionBehavior"
    )
    geo_match_level: Optional[Literal["AreaCode", "Country"]] = Field(
        default=None, alias="GeoMatchLevel"
    )
    geo_match_params: Optional[GeoMatchParamsModel] = Field(
        default=None, alias="GeoMatchParams"
    )


class PhoneNumberModel(BaseModel):
    phone_number_id: Optional[str] = Field(default=None, alias="PhoneNumberId")
    e164_phone_number: Optional[str] = Field(default=None, alias="E164PhoneNumber")
    country: Optional[str] = Field(default=None, alias="Country")
    type: Optional[Literal["Local", "TollFree"]] = Field(default=None, alias="Type")
    product_type: Optional[
        Literal["SipMediaApplicationDialIn", "VoiceConnector"]
    ] = Field(default=None, alias="ProductType")
    status: Optional[
        Literal[
            "AcquireFailed",
            "AcquireInProgress",
            "Assigned",
            "Cancelled",
            "DeleteFailed",
            "DeleteInProgress",
            "PortinCancelRequested",
            "PortinInProgress",
            "ReleaseFailed",
            "ReleaseInProgress",
            "Unassigned",
        ]
    ] = Field(default=None, alias="Status")
    capabilities: Optional[PhoneNumberCapabilitiesModel] = Field(
        default=None, alias="Capabilities"
    )
    associations: Optional[List[PhoneNumberAssociationModel]] = Field(
        default=None, alias="Associations"
    )
    calling_name: Optional[str] = Field(default=None, alias="CallingName")
    calling_name_status: Optional[
        Literal["Unassigned", "UpdateFailed", "UpdateInProgress", "UpdateSucceeded"]
    ] = Field(default=None, alias="CallingNameStatus")
    created_timestamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimestamp"
    )
    updated_timestamp: Optional[datetime] = Field(
        default=None, alias="UpdatedTimestamp"
    )
    deletion_timestamp: Optional[datetime] = Field(
        default=None, alias="DeletionTimestamp"
    )
    order_id: Optional[str] = Field(default=None, alias="OrderId")


class StreamingConfigurationModel(BaseModel):
    data_retention_in_hours: int = Field(alias="DataRetentionInHours")
    disabled: bool = Field(alias="Disabled")
    streaming_notification_targets: Optional[
        List[StreamingNotificationTargetModel]
    ] = Field(default=None, alias="StreamingNotificationTargets")


class CreateSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSipMediaApplicationsResponseModel(BaseModel):
    sip_media_applications: List[SipMediaApplicationModel] = Field(
        alias="SipMediaApplications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipMediaApplicationResponseModel(BaseModel):
    sip_media_application: SipMediaApplicationModel = Field(alias="SipMediaApplication")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSipRulesResponseModel(BaseModel):
    sip_rules: List[SipRuleModel] = Field(alias="SipRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSipRuleResponseModel(BaseModel):
    sip_rule: SipRuleModel = Field(alias="SipRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVoiceConnectorGroupsResponseModel(BaseModel):
    voice_connector_groups: List[VoiceConnectorGroupModel] = Field(
        alias="VoiceConnectorGroups"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVoiceConnectorGroupResponseModel(BaseModel):
    voice_connector_group: VoiceConnectorGroupModel = Field(alias="VoiceConnectorGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorEmergencyCallingConfigurationResponseModel(BaseModel):
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorEmergencyCallingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )


class PutVoiceConnectorEmergencyCallingConfigurationResponseModel(BaseModel):
    emergency_calling_configuration: EmergencyCallingConfigurationModel = Field(
        alias="EmergencyCallingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePhoneNumberOrderResponseModel(BaseModel):
    phone_number_order: PhoneNumberOrderModel = Field(alias="PhoneNumberOrder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberOrderResponseModel(BaseModel):
    phone_number_order: PhoneNumberOrderModel = Field(alias="PhoneNumberOrder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumberOrdersResponseModel(BaseModel):
    phone_number_orders: List[PhoneNumberOrderModel] = Field(alias="PhoneNumberOrders")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorOriginationResponseModel(BaseModel):
    origination: OriginationModel = Field(alias="Origination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorOriginationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    origination: OriginationModel = Field(alias="Origination")


class PutVoiceConnectorOriginationResponseModel(BaseModel):
    origination: OriginationModel = Field(alias="Origination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProxySessionsResponseModel(BaseModel):
    proxy_sessions: List[ProxySessionModel] = Field(alias="ProxySessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProxySessionResponseModel(BaseModel):
    proxy_session: ProxySessionModel = Field(alias="ProxySession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPhoneNumbersResponseModel(BaseModel):
    phone_numbers: List[PhoneNumberModel] = Field(alias="PhoneNumbers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestorePhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePhoneNumberResponseModel(BaseModel):
    phone_number: PhoneNumberModel = Field(alias="PhoneNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVoiceConnectorStreamingConfigurationResponseModel(BaseModel):
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutVoiceConnectorStreamingConfigurationRequestModel(BaseModel):
    voice_connector_id: str = Field(alias="VoiceConnectorId")
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )


class PutVoiceConnectorStreamingConfigurationResponseModel(BaseModel):
    streaming_configuration: StreamingConfigurationModel = Field(
        alias="StreamingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
