# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressBookDataModel(BaseModel):
    address_book_arn: Optional[str] = Field(default=None, alias="AddressBookArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class AddressBookModel(BaseModel):
    address_book_arn: Optional[str] = Field(default=None, alias="AddressBookArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class ApproveSkillRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")


class AssociateContactWithAddressBookRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    address_book_arn: str = Field(alias="AddressBookArn")


class AssociateDeviceWithNetworkProfileRequestModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    network_profile_arn: str = Field(alias="NetworkProfileArn")


class AssociateDeviceWithRoomRequestModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class AssociateSkillGroupWithRoomRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class AssociateSkillWithSkillGroupRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")


class AssociateSkillWithUsersRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")


class AudioModel(BaseModel):
    locale: Literal["en-US"] = Field(alias="Locale")
    location: str = Field(alias="Location")


class BusinessReportContentRangeModel(BaseModel):
    interval: Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"] = Field(alias="Interval")


class BusinessReportRecurrenceModel(BaseModel):
    start_date: Optional[str] = Field(default=None, alias="StartDate")


class BusinessReportS3LocationModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")


class CategoryModel(BaseModel):
    category_id: Optional[int] = Field(default=None, alias="CategoryId")
    category_name: Optional[str] = Field(default=None, alias="CategoryName")


class ConferencePreferenceModel(BaseModel):
    default_conference_provider_arn: Optional[str] = Field(
        default=None, alias="DefaultConferenceProviderArn"
    )


class IPDialInModel(BaseModel):
    endpoint: str = Field(alias="Endpoint")
    comms_protocol: Literal["H323", "SIP", "SIPS"] = Field(alias="CommsProtocol")


class MeetingSettingModel(BaseModel):
    require_pin: Literal["NO", "OPTIONAL", "YES"] = Field(alias="RequirePin")


class PSTNDialInModel(BaseModel):
    country_code: str = Field(alias="CountryCode")
    phone_number: str = Field(alias="PhoneNumber")
    one_click_id_delay: str = Field(alias="OneClickIdDelay")
    one_click_pin_delay: str = Field(alias="OneClickPinDelay")


class PhoneNumberModel(BaseModel):
    number: str = Field(alias="Number")
    type: Literal["HOME", "MOBILE", "WORK"] = Field(alias="Type")


class SipAddressModel(BaseModel):
    uri: str = Field(alias="Uri")
    type: Literal["WORK"] = Field(alias="Type")


class SsmlModel(BaseModel):
    locale: Literal["en-US"] = Field(alias="Locale")
    value: str = Field(alias="Value")


class TextModel(BaseModel):
    locale: Literal["en-US"] = Field(alias="Locale")
    value: str = Field(alias="Value")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateEndOfMeetingReminderModel(BaseModel):
    reminder_at_minutes: Sequence[int] = Field(alias="ReminderAtMinutes")
    reminder_type: Literal[
        "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
    ] = Field(alias="ReminderType")
    enabled: bool = Field(alias="Enabled")


class CreateInstantBookingModel(BaseModel):
    duration_in_minutes: int = Field(alias="DurationInMinutes")
    enabled: bool = Field(alias="Enabled")


class CreateRequireCheckInModel(BaseModel):
    release_after_minutes: int = Field(alias="ReleaseAfterMinutes")
    enabled: bool = Field(alias="Enabled")


class DeleteAddressBookRequestModel(BaseModel):
    address_book_arn: str = Field(alias="AddressBookArn")


class DeleteBusinessReportScheduleRequestModel(BaseModel):
    schedule_arn: str = Field(alias="ScheduleArn")


class DeleteConferenceProviderRequestModel(BaseModel):
    conference_provider_arn: str = Field(alias="ConferenceProviderArn")


class DeleteContactRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")


class DeleteDeviceRequestModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")


class DeleteDeviceUsageDataRequestModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    device_usage_type: Literal["VOICE"] = Field(alias="DeviceUsageType")


class DeleteGatewayGroupRequestModel(BaseModel):
    gateway_group_arn: str = Field(alias="GatewayGroupArn")


class DeleteNetworkProfileRequestModel(BaseModel):
    network_profile_arn: str = Field(alias="NetworkProfileArn")


class DeleteProfileRequestModel(BaseModel):
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")


class DeleteRoomRequestModel(BaseModel):
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class DeleteRoomSkillParameterRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    parameter_key: str = Field(alias="ParameterKey")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class DeleteSkillAuthorizationRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class DeleteSkillGroupRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")


class DeleteUserRequestModel(BaseModel):
    enrollment_id: str = Field(alias="EnrollmentId")
    user_arn: Optional[str] = Field(default=None, alias="UserArn")


class DeveloperInfoModel(BaseModel):
    developer_name: Optional[str] = Field(default=None, alias="DeveloperName")
    privacy_policy: Optional[str] = Field(default=None, alias="PrivacyPolicy")
    email: Optional[str] = Field(default=None, alias="Email")
    url: Optional[str] = Field(default=None, alias="Url")


class DeviceEventModel(BaseModel):
    type: Optional[Literal["CONNECTION_STATUS", "DEVICE_STATUS"]] = Field(
        default=None, alias="Type"
    )
    value: Optional[str] = Field(default=None, alias="Value")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class DeviceNetworkProfileInfoModel(BaseModel):
    network_profile_arn: Optional[str] = Field(default=None, alias="NetworkProfileArn")
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    certificate_expiration_time: Optional[datetime] = Field(
        default=None, alias="CertificateExpirationTime"
    )


class DeviceStatusDetailModel(BaseModel):
    feature: Optional[
        Literal[
            "ALL",
            "BLUETOOTH",
            "LISTS",
            "NETWORK_PROFILE",
            "NOTIFICATIONS",
            "SETTINGS",
            "SKILLS",
            "VOLUME",
        ]
    ] = Field(default=None, alias="Feature")
    code: Optional[
        Literal[
            "ASSOCIATION_REJECTION",
            "AUTHENTICATION_FAILURE",
            "CERTIFICATE_AUTHORITY_ACCESS_DENIED",
            "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
            "CREDENTIALS_ACCESS_FAILURE",
            "DEVICE_SOFTWARE_UPDATE_NEEDED",
            "DEVICE_WAS_OFFLINE",
            "DHCP_FAILURE",
            "DNS_FAILURE",
            "INTERNET_UNAVAILABLE",
            "INVALID_CERTIFICATE_AUTHORITY",
            "INVALID_PASSWORD_STATE",
            "NETWORK_PROFILE_NOT_FOUND",
            "PASSWORD_MANAGER_ACCESS_DENIED",
            "PASSWORD_NOT_FOUND",
            "TLS_VERSION_MISMATCH",
            "UNKNOWN_FAILURE",
        ]
    ] = Field(default=None, alias="Code")


class DisassociateContactFromAddressBookRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    address_book_arn: str = Field(alias="AddressBookArn")


class DisassociateDeviceFromRoomRequestModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")


class DisassociateSkillFromSkillGroupRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")


class DisassociateSkillFromUsersRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")


class DisassociateSkillGroupFromRoomRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class EndOfMeetingReminderModel(BaseModel):
    reminder_at_minutes: Optional[List[int]] = Field(
        default=None, alias="ReminderAtMinutes"
    )
    reminder_type: Optional[
        Literal[
            "ANNOUNCEMENT_TIME_CHECK",
            "ANNOUNCEMENT_VARIABLE_TIME_LEFT",
            "CHIME",
            "KNOCK",
        ]
    ] = Field(default=None, alias="ReminderType")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class FilterModel(BaseModel):
    key: str = Field(alias="Key")
    values: Sequence[str] = Field(alias="Values")


class ForgetSmartHomeAppliancesRequestModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")


class GatewayGroupSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class GatewayGroupModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class GatewaySummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    gateway_group_arn: Optional[str] = Field(default=None, alias="GatewayGroupArn")
    software_version: Optional[str] = Field(default=None, alias="SoftwareVersion")


class GatewayModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    gateway_group_arn: Optional[str] = Field(default=None, alias="GatewayGroupArn")
    software_version: Optional[str] = Field(default=None, alias="SoftwareVersion")


class GetAddressBookRequestModel(BaseModel):
    address_book_arn: str = Field(alias="AddressBookArn")


class GetConferenceProviderRequestModel(BaseModel):
    conference_provider_arn: str = Field(alias="ConferenceProviderArn")


class GetContactRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")


class GetDeviceRequestModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")


class GetGatewayGroupRequestModel(BaseModel):
    gateway_group_arn: str = Field(alias="GatewayGroupArn")


class GetGatewayRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")


class GetNetworkProfileRequestModel(BaseModel):
    network_profile_arn: str = Field(alias="NetworkProfileArn")


class NetworkProfileModel(BaseModel):
    network_profile_arn: Optional[str] = Field(default=None, alias="NetworkProfileArn")
    network_profile_name: Optional[str] = Field(
        default=None, alias="NetworkProfileName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    ssid: Optional[str] = Field(default=None, alias="Ssid")
    security_type: Optional[
        Literal["OPEN", "WEP", "WPA2_ENTERPRISE", "WPA2_PSK", "WPA_PSK"]
    ] = Field(default=None, alias="SecurityType")
    eap_method: Optional[Literal["EAP_TLS"]] = Field(default=None, alias="EapMethod")
    current_password: Optional[str] = Field(default=None, alias="CurrentPassword")
    next_password: Optional[str] = Field(default=None, alias="NextPassword")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    trust_anchors: Optional[List[str]] = Field(default=None, alias="TrustAnchors")


class GetProfileRequestModel(BaseModel):
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")


class GetRoomRequestModel(BaseModel):
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class RoomModel(BaseModel):
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    room_name: Optional[str] = Field(default=None, alias="RoomName")
    description: Optional[str] = Field(default=None, alias="Description")
    provider_calendar_id: Optional[str] = Field(
        default=None, alias="ProviderCalendarId"
    )
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")


class GetRoomSkillParameterRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    parameter_key: str = Field(alias="ParameterKey")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class RoomSkillParameterModel(BaseModel):
    parameter_key: str = Field(alias="ParameterKey")
    parameter_value: str = Field(alias="ParameterValue")


class GetSkillGroupRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")


class SkillGroupModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    skill_group_name: Optional[str] = Field(default=None, alias="SkillGroupName")
    description: Optional[str] = Field(default=None, alias="Description")


class InstantBookingModel(BaseModel):
    duration_in_minutes: Optional[int] = Field(default=None, alias="DurationInMinutes")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBusinessReportSchedulesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListConferenceProvidersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDeviceEventsRequestModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    event_type: Optional[Literal["CONNECTION_STATUS", "DEVICE_STATUS"]] = Field(
        default=None, alias="EventType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGatewayGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGatewaysRequestModel(BaseModel):
    gateway_group_arn: Optional[str] = Field(default=None, alias="GatewayGroupArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSkillsRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    enablement_type: Optional[Literal["ENABLED", "PENDING"]] = Field(
        default=None, alias="EnablementType"
    )
    skill_type: Optional[Literal["ALL", "PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="SkillType"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SkillSummaryModel(BaseModel):
    skill_id: Optional[str] = Field(default=None, alias="SkillId")
    skill_name: Optional[str] = Field(default=None, alias="SkillName")
    supports_linking: Optional[bool] = Field(default=None, alias="SupportsLinking")
    enablement_type: Optional[Literal["ENABLED", "PENDING"]] = Field(
        default=None, alias="EnablementType"
    )
    skill_type: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="SkillType"
    )


class ListSkillsStoreCategoriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSkillsStoreSkillsByCategoryRequestModel(BaseModel):
    category_id: int = Field(alias="CategoryId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSmartHomeAppliancesRequestModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SmartHomeApplianceModel(BaseModel):
    friendly_name: Optional[str] = Field(default=None, alias="FriendlyName")
    description: Optional[str] = Field(default=None, alias="Description")
    manufacturer_name: Optional[str] = Field(default=None, alias="ManufacturerName")


class ListTagsRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class RequireCheckInModel(BaseModel):
    release_after_minutes: Optional[int] = Field(
        default=None, alias="ReleaseAfterMinutes"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class NetworkProfileDataModel(BaseModel):
    network_profile_arn: Optional[str] = Field(default=None, alias="NetworkProfileArn")
    network_profile_name: Optional[str] = Field(
        default=None, alias="NetworkProfileName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    ssid: Optional[str] = Field(default=None, alias="Ssid")
    security_type: Optional[
        Literal["OPEN", "WEP", "WPA2_ENTERPRISE", "WPA2_PSK", "WPA_PSK"]
    ] = Field(default=None, alias="SecurityType")
    eap_method: Optional[Literal["EAP_TLS"]] = Field(default=None, alias="EapMethod")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )


class ProfileDataModel(BaseModel):
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")
    profile_name: Optional[str] = Field(default=None, alias="ProfileName")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")
    address: Optional[str] = Field(default=None, alias="Address")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    distance_unit: Optional[Literal["IMPERIAL", "METRIC"]] = Field(
        default=None, alias="DistanceUnit"
    )
    temperature_unit: Optional[Literal["CELSIUS", "FAHRENHEIT"]] = Field(
        default=None, alias="TemperatureUnit"
    )
    wake_word: Optional[Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"]] = Field(
        default=None, alias="WakeWord"
    )
    locale: Optional[str] = Field(default=None, alias="Locale")


class PutInvitationConfigurationRequestModel(BaseModel):
    organization_name: str = Field(alias="OrganizationName")
    contact_email: Optional[str] = Field(default=None, alias="ContactEmail")
    private_skill_ids: Optional[Sequence[str]] = Field(
        default=None, alias="PrivateSkillIds"
    )


class PutSkillAuthorizationRequestModel(BaseModel):
    authorization_result: Mapping[str, str] = Field(alias="AuthorizationResult")
    skill_id: str = Field(alias="SkillId")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class RejectSkillRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")


class ResolveRoomRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    skill_id: str = Field(alias="SkillId")


class RevokeInvitationRequestModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="UserArn")
    enrollment_id: Optional[str] = Field(default=None, alias="EnrollmentId")


class RoomDataModel(BaseModel):
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    room_name: Optional[str] = Field(default=None, alias="RoomName")
    description: Optional[str] = Field(default=None, alias="Description")
    provider_calendar_id: Optional[str] = Field(
        default=None, alias="ProviderCalendarId"
    )
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")
    profile_name: Optional[str] = Field(default=None, alias="ProfileName")


class SortModel(BaseModel):
    key: str = Field(alias="Key")
    value: Literal["ASC", "DESC"] = Field(alias="Value")


class SkillGroupDataModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    skill_group_name: Optional[str] = Field(default=None, alias="SkillGroupName")
    description: Optional[str] = Field(default=None, alias="Description")


class UserDataModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="UserArn")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    email: Optional[str] = Field(default=None, alias="Email")
    enrollment_status: Optional[
        Literal[
            "DEREGISTERING", "DISASSOCIATING", "INITIALIZED", "PENDING", "REGISTERED"
        ]
    ] = Field(default=None, alias="EnrollmentStatus")
    enrollment_id: Optional[str] = Field(default=None, alias="EnrollmentId")


class SendInvitationRequestModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="UserArn")


class StartDeviceSyncRequestModel(BaseModel):
    features: Sequence[
        Literal[
            "ALL",
            "BLUETOOTH",
            "LISTS",
            "NETWORK_PROFILE",
            "NOTIFICATIONS",
            "SETTINGS",
            "SKILLS",
            "VOLUME",
        ]
    ] = Field(alias="Features")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")


class StartSmartHomeApplianceDiscoveryRequestModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAddressBookRequestModel(BaseModel):
    address_book_arn: str = Field(alias="AddressBookArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateDeviceRequestModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")


class UpdateEndOfMeetingReminderModel(BaseModel):
    reminder_at_minutes: Optional[Sequence[int]] = Field(
        default=None, alias="ReminderAtMinutes"
    )
    reminder_type: Optional[
        Literal[
            "ANNOUNCEMENT_TIME_CHECK",
            "ANNOUNCEMENT_VARIABLE_TIME_LEFT",
            "CHIME",
            "KNOCK",
        ]
    ] = Field(default=None, alias="ReminderType")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdateGatewayGroupRequestModel(BaseModel):
    gateway_group_arn: str = Field(alias="GatewayGroupArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateGatewayRequestModel(BaseModel):
    gateway_arn: str = Field(alias="GatewayArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    software_version: Optional[str] = Field(default=None, alias="SoftwareVersion")


class UpdateInstantBookingModel(BaseModel):
    duration_in_minutes: Optional[int] = Field(default=None, alias="DurationInMinutes")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdateRequireCheckInModel(BaseModel):
    release_after_minutes: Optional[int] = Field(
        default=None, alias="ReleaseAfterMinutes"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdateNetworkProfileRequestModel(BaseModel):
    network_profile_arn: str = Field(alias="NetworkProfileArn")
    network_profile_name: Optional[str] = Field(
        default=None, alias="NetworkProfileName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    current_password: Optional[str] = Field(default=None, alias="CurrentPassword")
    next_password: Optional[str] = Field(default=None, alias="NextPassword")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    trust_anchors: Optional[Sequence[str]] = Field(default=None, alias="TrustAnchors")


class UpdateRoomRequestModel(BaseModel):
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    room_name: Optional[str] = Field(default=None, alias="RoomName")
    description: Optional[str] = Field(default=None, alias="Description")
    provider_calendar_id: Optional[str] = Field(
        default=None, alias="ProviderCalendarId"
    )
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")


class UpdateSkillGroupRequestModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    skill_group_name: Optional[str] = Field(default=None, alias="SkillGroupName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateBusinessReportScheduleRequestModel(BaseModel):
    schedule_arn: str = Field(alias="ScheduleArn")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    format: Optional[Literal["CSV", "CSV_ZIP"]] = Field(default=None, alias="Format")
    schedule_name: Optional[str] = Field(default=None, alias="ScheduleName")
    recurrence: Optional[BusinessReportRecurrenceModel] = Field(
        default=None, alias="Recurrence"
    )


class BusinessReportModel(BaseModel):
    status: Optional[Literal["FAILED", "RUNNING", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    failure_code: Optional[
        Literal["ACCESS_DENIED", "INTERNAL_FAILURE", "NO_SUCH_BUCKET"]
    ] = Field(default=None, alias="FailureCode")
    s3_location: Optional[BusinessReportS3LocationModel] = Field(
        default=None, alias="S3Location"
    )
    delivery_time: Optional[datetime] = Field(default=None, alias="DeliveryTime")
    download_url: Optional[str] = Field(default=None, alias="DownloadUrl")


class PutConferencePreferenceRequestModel(BaseModel):
    conference_preference: ConferencePreferenceModel = Field(
        alias="ConferencePreference"
    )


class ConferenceProviderModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[
        Literal[
            "BLUEJEANS",
            "CHIME",
            "CUSTOM",
            "FUZE",
            "GOOGLE_HANGOUTS",
            "POLYCOM",
            "RINGCENTRAL",
            "SKYPE_FOR_BUSINESS",
            "WEBEX",
            "ZOOM",
        ]
    ] = Field(default=None, alias="Type")
    ip_dial_in: Optional[IPDialInModel] = Field(default=None, alias="IPDialIn")
    p_s_tndial_in: Optional[PSTNDialInModel] = Field(default=None, alias="PSTNDialIn")
    meeting_setting: Optional[MeetingSettingModel] = Field(
        default=None, alias="MeetingSetting"
    )


class UpdateConferenceProviderRequestModel(BaseModel):
    conference_provider_arn: str = Field(alias="ConferenceProviderArn")
    conference_provider_type: Literal[
        "BLUEJEANS",
        "CHIME",
        "CUSTOM",
        "FUZE",
        "GOOGLE_HANGOUTS",
        "POLYCOM",
        "RINGCENTRAL",
        "SKYPE_FOR_BUSINESS",
        "WEBEX",
        "ZOOM",
    ] = Field(alias="ConferenceProviderType")
    meeting_setting: MeetingSettingModel = Field(alias="MeetingSetting")
    ip_dial_in: Optional[IPDialInModel] = Field(default=None, alias="IPDialIn")
    p_s_tndial_in: Optional[PSTNDialInModel] = Field(default=None, alias="PSTNDialIn")


class ContactDataModel(BaseModel):
    contact_arn: Optional[str] = Field(default=None, alias="ContactArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_numbers: Optional[List[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    sip_addresses: Optional[List[SipAddressModel]] = Field(
        default=None, alias="SipAddresses"
    )


class ContactModel(BaseModel):
    contact_arn: Optional[str] = Field(default=None, alias="ContactArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_numbers: Optional[List[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    sip_addresses: Optional[List[SipAddressModel]] = Field(
        default=None, alias="SipAddresses"
    )


class UpdateContactRequestModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_numbers: Optional[Sequence[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    sip_addresses: Optional[Sequence[SipAddressModel]] = Field(
        default=None, alias="SipAddresses"
    )


class ContentModel(BaseModel):
    text_list: Optional[Sequence[TextModel]] = Field(default=None, alias="TextList")
    ssml_list: Optional[Sequence[SsmlModel]] = Field(default=None, alias="SsmlList")
    audio_list: Optional[Sequence[AudioModel]] = Field(default=None, alias="AudioList")


class CreateAddressBookRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateBusinessReportScheduleRequestModel(BaseModel):
    format: Literal["CSV", "CSV_ZIP"] = Field(alias="Format")
    content_range: BusinessReportContentRangeModel = Field(alias="ContentRange")
    schedule_name: Optional[str] = Field(default=None, alias="ScheduleName")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    recurrence: Optional[BusinessReportRecurrenceModel] = Field(
        default=None, alias="Recurrence"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateConferenceProviderRequestModel(BaseModel):
    conference_provider_name: str = Field(alias="ConferenceProviderName")
    conference_provider_type: Literal[
        "BLUEJEANS",
        "CHIME",
        "CUSTOM",
        "FUZE",
        "GOOGLE_HANGOUTS",
        "POLYCOM",
        "RINGCENTRAL",
        "SKYPE_FOR_BUSINESS",
        "WEBEX",
        "ZOOM",
    ] = Field(alias="ConferenceProviderType")
    meeting_setting: MeetingSettingModel = Field(alias="MeetingSetting")
    ip_dial_in: Optional[IPDialInModel] = Field(default=None, alias="IPDialIn")
    p_s_tndial_in: Optional[PSTNDialInModel] = Field(default=None, alias="PSTNDialIn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateContactRequestModel(BaseModel):
    first_name: str = Field(alias="FirstName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    phone_numbers: Optional[Sequence[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    sip_addresses: Optional[Sequence[SipAddressModel]] = Field(
        default=None, alias="SipAddresses"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateGatewayGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_request_token: str = Field(alias="ClientRequestToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateNetworkProfileRequestModel(BaseModel):
    network_profile_name: str = Field(alias="NetworkProfileName")
    ssid: str = Field(alias="Ssid")
    security_type: Literal[
        "OPEN", "WEP", "WPA2_ENTERPRISE", "WPA2_PSK", "WPA_PSK"
    ] = Field(alias="SecurityType")
    client_request_token: str = Field(alias="ClientRequestToken")
    description: Optional[str] = Field(default=None, alias="Description")
    eap_method: Optional[Literal["EAP_TLS"]] = Field(default=None, alias="EapMethod")
    current_password: Optional[str] = Field(default=None, alias="CurrentPassword")
    next_password: Optional[str] = Field(default=None, alias="NextPassword")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    trust_anchors: Optional[Sequence[str]] = Field(default=None, alias="TrustAnchors")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateRoomRequestModel(BaseModel):
    room_name: str = Field(alias="RoomName")
    description: Optional[str] = Field(default=None, alias="Description")
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")
    provider_calendar_id: Optional[str] = Field(
        default=None, alias="ProviderCalendarId"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateSkillGroupRequestModel(BaseModel):
    skill_group_name: str = Field(alias="SkillGroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserRequestModel(BaseModel):
    user_id: str = Field(alias="UserId")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    email: Optional[str] = Field(default=None, alias="Email")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class RegisterAVSDeviceRequestModel(BaseModel):
    client_id: str = Field(alias="ClientId")
    user_code: str = Field(alias="UserCode")
    product_id: str = Field(alias="ProductId")
    amazon_id: str = Field(alias="AmazonId")
    device_serial_number: Optional[str] = Field(
        default=None, alias="DeviceSerialNumber"
    )
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateAddressBookResponseModel(BaseModel):
    address_book_arn: str = Field(alias="AddressBookArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBusinessReportScheduleResponseModel(BaseModel):
    schedule_arn: str = Field(alias="ScheduleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConferenceProviderResponseModel(BaseModel):
    conference_provider_arn: str = Field(alias="ConferenceProviderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContactResponseModel(BaseModel):
    contact_arn: str = Field(alias="ContactArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGatewayGroupResponseModel(BaseModel):
    gateway_group_arn: str = Field(alias="GatewayGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkProfileResponseModel(BaseModel):
    network_profile_arn: str = Field(alias="NetworkProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfileResponseModel(BaseModel):
    profile_arn: str = Field(alias="ProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoomResponseModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSkillGroupResponseModel(BaseModel):
    skill_group_arn: str = Field(alias="SkillGroupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user_arn: str = Field(alias="UserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAddressBookResponseModel(BaseModel):
    address_book: AddressBookModel = Field(alias="AddressBook")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConferencePreferenceResponseModel(BaseModel):
    preference: ConferencePreferenceModel = Field(alias="Preference")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInvitationConfigurationResponseModel(BaseModel):
    organization_name: str = Field(alias="OrganizationName")
    contact_email: str = Field(alias="ContactEmail")
    private_skill_ids: List[str] = Field(alias="PrivateSkillIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSkillsStoreCategoriesResponseModel(BaseModel):
    category_list: List[CategoryModel] = Field(alias="CategoryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterAVSDeviceResponseModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAddressBooksResponseModel(BaseModel):
    address_books: List[AddressBookDataModel] = Field(alias="AddressBooks")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendAnnouncementResponseModel(BaseModel):
    announcement_arn: str = Field(alias="AnnouncementArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMeetingRoomConfigurationModel(BaseModel):
    room_utilization_metrics_enabled: Optional[bool] = Field(
        default=None, alias="RoomUtilizationMetricsEnabled"
    )
    end_of_meeting_reminder: Optional[CreateEndOfMeetingReminderModel] = Field(
        default=None, alias="EndOfMeetingReminder"
    )
    instant_booking: Optional[CreateInstantBookingModel] = Field(
        default=None, alias="InstantBooking"
    )
    require_check_in: Optional[CreateRequireCheckInModel] = Field(
        default=None, alias="RequireCheckIn"
    )


class SkillDetailsModel(BaseModel):
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    invocation_phrase: Optional[str] = Field(default=None, alias="InvocationPhrase")
    release_date: Optional[str] = Field(default=None, alias="ReleaseDate")
    end_user_license_agreement: Optional[str] = Field(
        default=None, alias="EndUserLicenseAgreement"
    )
    generic_keywords: Optional[List[str]] = Field(default=None, alias="GenericKeywords")
    bullet_points: Optional[List[str]] = Field(default=None, alias="BulletPoints")
    new_in_this_version_bullet_points: Optional[List[str]] = Field(
        default=None, alias="NewInThisVersionBulletPoints"
    )
    skill_types: Optional[List[str]] = Field(default=None, alias="SkillTypes")
    reviews: Optional[Dict[str, str]] = Field(default=None, alias="Reviews")
    developer_info: Optional[DeveloperInfoModel] = Field(
        default=None, alias="DeveloperInfo"
    )


class ListDeviceEventsResponseModel(BaseModel):
    device_events: List[DeviceEventModel] = Field(alias="DeviceEvents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceStatusInfoModel(BaseModel):
    device_status_details: Optional[List[DeviceStatusDetailModel]] = Field(
        default=None, alias="DeviceStatusDetails"
    )
    connection_status: Optional[Literal["OFFLINE", "ONLINE"]] = Field(
        default=None, alias="ConnectionStatus"
    )
    connection_status_updated_time: Optional[datetime] = Field(
        default=None, alias="ConnectionStatusUpdatedTime"
    )


class ListGatewayGroupsResponseModel(BaseModel):
    gateway_groups: List[GatewayGroupSummaryModel] = Field(alias="GatewayGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGatewayGroupResponseModel(BaseModel):
    gateway_group: GatewayGroupModel = Field(alias="GatewayGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGatewaysResponseModel(BaseModel):
    gateways: List[GatewaySummaryModel] = Field(alias="Gateways")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGatewayResponseModel(BaseModel):
    gateway: GatewayModel = Field(alias="Gateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkProfileResponseModel(BaseModel):
    network_profile: NetworkProfileModel = Field(alias="NetworkProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoomResponseModel(BaseModel):
    room: RoomModel = Field(alias="Room")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoomSkillParameterResponseModel(BaseModel):
    room_skill_parameter: RoomSkillParameterModel = Field(alias="RoomSkillParameter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRoomSkillParameterRequestModel(BaseModel):
    skill_id: str = Field(alias="SkillId")
    room_skill_parameter: RoomSkillParameterModel = Field(alias="RoomSkillParameter")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")


class ResolveRoomResponseModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")
    room_name: str = Field(alias="RoomName")
    room_skill_parameters: List[RoomSkillParameterModel] = Field(
        alias="RoomSkillParameters"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSkillGroupResponseModel(BaseModel):
    skill_group: SkillGroupModel = Field(alias="SkillGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBusinessReportSchedulesRequestListBusinessReportSchedulesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConferenceProvidersRequestListConferenceProvidersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceEventsRequestListDeviceEventsPaginateModel(BaseModel):
    device_arn: str = Field(alias="DeviceArn")
    event_type: Optional[Literal["CONNECTION_STATUS", "DEVICE_STATUS"]] = Field(
        default=None, alias="EventType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSkillsRequestListSkillsPaginateModel(BaseModel):
    skill_group_arn: Optional[str] = Field(default=None, alias="SkillGroupArn")
    enablement_type: Optional[Literal["ENABLED", "PENDING"]] = Field(
        default=None, alias="EnablementType"
    )
    skill_type: Optional[Literal["ALL", "PRIVATE", "PUBLIC"]] = Field(
        default=None, alias="SkillType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSkillsStoreCategoriesRequestListSkillsStoreCategoriesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSkillsStoreSkillsByCategoryRequestListSkillsStoreSkillsByCategoryPaginateModel(
    BaseModel
):
    category_id: int = Field(alias="CategoryId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSmartHomeAppliancesRequestListSmartHomeAppliancesPaginateModel(BaseModel):
    room_arn: str = Field(alias="RoomArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsRequestListTagsPaginateModel(BaseModel):
    arn: str = Field(alias="Arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSkillsResponseModel(BaseModel):
    skill_summaries: List[SkillSummaryModel] = Field(alias="SkillSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSmartHomeAppliancesResponseModel(BaseModel):
    smart_home_appliances: List[SmartHomeApplianceModel] = Field(
        alias="SmartHomeAppliances"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MeetingRoomConfigurationModel(BaseModel):
    room_utilization_metrics_enabled: Optional[bool] = Field(
        default=None, alias="RoomUtilizationMetricsEnabled"
    )
    end_of_meeting_reminder: Optional[EndOfMeetingReminderModel] = Field(
        default=None, alias="EndOfMeetingReminder"
    )
    instant_booking: Optional[InstantBookingModel] = Field(
        default=None, alias="InstantBooking"
    )
    require_check_in: Optional[RequireCheckInModel] = Field(
        default=None, alias="RequireCheckIn"
    )


class SearchNetworkProfilesResponseModel(BaseModel):
    network_profiles: List[NetworkProfileDataModel] = Field(alias="NetworkProfiles")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchProfilesResponseModel(BaseModel):
    profiles: List[ProfileDataModel] = Field(alias="Profiles")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchRoomsResponseModel(BaseModel):
    rooms: List[RoomDataModel] = Field(alias="Rooms")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAddressBooksRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchContactsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchDevicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchDevicesRequestSearchDevicesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchNetworkProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchProfilesRequestSearchProfilesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchRoomsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchRoomsRequestSearchRoomsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSkillGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchSkillGroupsRequestSearchSkillGroupsPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchUsersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )


class SearchUsersRequestSearchUsersPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_criteria: Optional[Sequence[SortModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSkillGroupsResponseModel(BaseModel):
    skill_groups: List[SkillGroupDataModel] = Field(alias="SkillGroups")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchUsersResponseModel(BaseModel):
    users: List[UserDataModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMeetingRoomConfigurationModel(BaseModel):
    room_utilization_metrics_enabled: Optional[bool] = Field(
        default=None, alias="RoomUtilizationMetricsEnabled"
    )
    end_of_meeting_reminder: Optional[UpdateEndOfMeetingReminderModel] = Field(
        default=None, alias="EndOfMeetingReminder"
    )
    instant_booking: Optional[UpdateInstantBookingModel] = Field(
        default=None, alias="InstantBooking"
    )
    require_check_in: Optional[UpdateRequireCheckInModel] = Field(
        default=None, alias="RequireCheckIn"
    )


class BusinessReportScheduleModel(BaseModel):
    schedule_arn: Optional[str] = Field(default=None, alias="ScheduleArn")
    schedule_name: Optional[str] = Field(default=None, alias="ScheduleName")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    format: Optional[Literal["CSV", "CSV_ZIP"]] = Field(default=None, alias="Format")
    content_range: Optional[BusinessReportContentRangeModel] = Field(
        default=None, alias="ContentRange"
    )
    recurrence: Optional[BusinessReportRecurrenceModel] = Field(
        default=None, alias="Recurrence"
    )
    last_business_report: Optional[BusinessReportModel] = Field(
        default=None, alias="LastBusinessReport"
    )


class GetConferenceProviderResponseModel(BaseModel):
    conference_provider: ConferenceProviderModel = Field(alias="ConferenceProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConferenceProvidersResponseModel(BaseModel):
    conference_providers: List[ConferenceProviderModel] = Field(
        alias="ConferenceProviders"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchContactsResponseModel(BaseModel):
    contacts: List[ContactDataModel] = Field(alias="Contacts")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactResponseModel(BaseModel):
    contact: ContactModel = Field(alias="Contact")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendAnnouncementRequestModel(BaseModel):
    room_filters: Sequence[FilterModel] = Field(alias="RoomFilters")
    content: ContentModel = Field(alias="Content")
    client_request_token: str = Field(alias="ClientRequestToken")
    time_to_live_in_seconds: Optional[int] = Field(
        default=None, alias="TimeToLiveInSeconds"
    )


class CreateProfileRequestModel(BaseModel):
    profile_name: str = Field(alias="ProfileName")
    timezone: str = Field(alias="Timezone")
    address: str = Field(alias="Address")
    distance_unit: Literal["IMPERIAL", "METRIC"] = Field(alias="DistanceUnit")
    temperature_unit: Literal["CELSIUS", "FAHRENHEIT"] = Field(alias="TemperatureUnit")
    wake_word: Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"] = Field(alias="WakeWord")
    locale: Optional[str] = Field(default=None, alias="Locale")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    setup_mode_disabled: Optional[bool] = Field(default=None, alias="SetupModeDisabled")
    max_volume_limit: Optional[int] = Field(default=None, alias="MaxVolumeLimit")
    p_s_tnenabled: Optional[bool] = Field(default=None, alias="PSTNEnabled")
    data_retention_opt_in: Optional[bool] = Field(
        default=None, alias="DataRetentionOptIn"
    )
    meeting_room_configuration: Optional[CreateMeetingRoomConfigurationModel] = Field(
        default=None, alias="MeetingRoomConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class SkillsStoreSkillModel(BaseModel):
    skill_id: Optional[str] = Field(default=None, alias="SkillId")
    skill_name: Optional[str] = Field(default=None, alias="SkillName")
    short_description: Optional[str] = Field(default=None, alias="ShortDescription")
    icon_url: Optional[str] = Field(default=None, alias="IconUrl")
    sample_utterances: Optional[List[str]] = Field(
        default=None, alias="SampleUtterances"
    )
    skill_details: Optional[SkillDetailsModel] = Field(
        default=None, alias="SkillDetails"
    )
    supports_linking: Optional[bool] = Field(default=None, alias="SupportsLinking")


class DeviceDataModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")
    device_serial_number: Optional[str] = Field(
        default=None, alias="DeviceSerialNumber"
    )
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    software_version: Optional[str] = Field(default=None, alias="SoftwareVersion")
    mac_address: Optional[str] = Field(default=None, alias="MacAddress")
    device_status: Optional[
        Literal["DEREGISTERED", "FAILED", "PENDING", "READY", "WAS_OFFLINE"]
    ] = Field(default=None, alias="DeviceStatus")
    network_profile_arn: Optional[str] = Field(default=None, alias="NetworkProfileArn")
    network_profile_name: Optional[str] = Field(
        default=None, alias="NetworkProfileName"
    )
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    room_name: Optional[str] = Field(default=None, alias="RoomName")
    device_status_info: Optional[DeviceStatusInfoModel] = Field(
        default=None, alias="DeviceStatusInfo"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class DeviceModel(BaseModel):
    device_arn: Optional[str] = Field(default=None, alias="DeviceArn")
    device_serial_number: Optional[str] = Field(
        default=None, alias="DeviceSerialNumber"
    )
    device_type: Optional[str] = Field(default=None, alias="DeviceType")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    software_version: Optional[str] = Field(default=None, alias="SoftwareVersion")
    mac_address: Optional[str] = Field(default=None, alias="MacAddress")
    room_arn: Optional[str] = Field(default=None, alias="RoomArn")
    device_status: Optional[
        Literal["DEREGISTERED", "FAILED", "PENDING", "READY", "WAS_OFFLINE"]
    ] = Field(default=None, alias="DeviceStatus")
    device_status_info: Optional[DeviceStatusInfoModel] = Field(
        default=None, alias="DeviceStatusInfo"
    )
    network_profile_info: Optional[DeviceNetworkProfileInfoModel] = Field(
        default=None, alias="NetworkProfileInfo"
    )


class ProfileModel(BaseModel):
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")
    profile_name: Optional[str] = Field(default=None, alias="ProfileName")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")
    address: Optional[str] = Field(default=None, alias="Address")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    distance_unit: Optional[Literal["IMPERIAL", "METRIC"]] = Field(
        default=None, alias="DistanceUnit"
    )
    temperature_unit: Optional[Literal["CELSIUS", "FAHRENHEIT"]] = Field(
        default=None, alias="TemperatureUnit"
    )
    wake_word: Optional[Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"]] = Field(
        default=None, alias="WakeWord"
    )
    locale: Optional[str] = Field(default=None, alias="Locale")
    setup_mode_disabled: Optional[bool] = Field(default=None, alias="SetupModeDisabled")
    max_volume_limit: Optional[int] = Field(default=None, alias="MaxVolumeLimit")
    p_s_tnenabled: Optional[bool] = Field(default=None, alias="PSTNEnabled")
    data_retention_opt_in: Optional[bool] = Field(
        default=None, alias="DataRetentionOptIn"
    )
    address_book_arn: Optional[str] = Field(default=None, alias="AddressBookArn")
    meeting_room_configuration: Optional[MeetingRoomConfigurationModel] = Field(
        default=None, alias="MeetingRoomConfiguration"
    )


class UpdateProfileRequestModel(BaseModel):
    profile_arn: Optional[str] = Field(default=None, alias="ProfileArn")
    profile_name: Optional[str] = Field(default=None, alias="ProfileName")
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    address: Optional[str] = Field(default=None, alias="Address")
    distance_unit: Optional[Literal["IMPERIAL", "METRIC"]] = Field(
        default=None, alias="DistanceUnit"
    )
    temperature_unit: Optional[Literal["CELSIUS", "FAHRENHEIT"]] = Field(
        default=None, alias="TemperatureUnit"
    )
    wake_word: Optional[Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"]] = Field(
        default=None, alias="WakeWord"
    )
    locale: Optional[str] = Field(default=None, alias="Locale")
    setup_mode_disabled: Optional[bool] = Field(default=None, alias="SetupModeDisabled")
    max_volume_limit: Optional[int] = Field(default=None, alias="MaxVolumeLimit")
    p_s_tnenabled: Optional[bool] = Field(default=None, alias="PSTNEnabled")
    data_retention_opt_in: Optional[bool] = Field(
        default=None, alias="DataRetentionOptIn"
    )
    meeting_room_configuration: Optional[UpdateMeetingRoomConfigurationModel] = Field(
        default=None, alias="MeetingRoomConfiguration"
    )


class ListBusinessReportSchedulesResponseModel(BaseModel):
    business_report_schedules: List[BusinessReportScheduleModel] = Field(
        alias="BusinessReportSchedules"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSkillsStoreSkillsByCategoryResponseModel(BaseModel):
    skills_store_skills: List[SkillsStoreSkillModel] = Field(alias="SkillsStoreSkills")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchDevicesResponseModel(BaseModel):
    devices: List[DeviceDataModel] = Field(alias="Devices")
    next_token: str = Field(alias="NextToken")
    total_count: int = Field(alias="TotalCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceResponseModel(BaseModel):
    device: DeviceModel = Field(alias="Device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProfileResponseModel(BaseModel):
    profile: ProfileModel = Field(alias="Profile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
