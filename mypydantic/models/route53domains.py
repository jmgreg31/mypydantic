# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptDomainTransferFromAnotherAwsAccountRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    password: str = Field(alias="Password")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DnssecSigningAttributesModel(BaseModel):
    algorithm: Optional[int] = Field(default=None, alias="Algorithm")
    flags: Optional[int] = Field(default=None, alias="Flags")
    public_key: Optional[str] = Field(default=None, alias="PublicKey")


class BillingRecordModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    operation: Optional[
        Literal[
            "ADD_DNSSEC",
            "CHANGE_DOMAIN_OWNER",
            "CHANGE_PRIVACY_PROTECTION",
            "DELETE_DOMAIN",
            "DISABLE_AUTORENEW",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "EXPIRE_DOMAIN",
            "INTERNAL_TRANSFER_IN_DOMAIN",
            "INTERNAL_TRANSFER_OUT_DOMAIN",
            "PUSH_DOMAIN",
            "REGISTER_DOMAIN",
            "REMOVE_DNSSEC",
            "RENEW_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
        ]
    ] = Field(default=None, alias="Operation")
    invoice_id: Optional[str] = Field(default=None, alias="InvoiceId")
    bill_date: Optional[datetime] = Field(default=None, alias="BillDate")
    price: Optional[float] = Field(default=None, alias="Price")


class CancelDomainTransferToAnotherAwsAccountRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class CheckDomainAvailabilityRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    idn_lang_code: Optional[str] = Field(default=None, alias="IdnLangCode")


class CheckDomainTransferabilityRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    auth_code: Optional[str] = Field(default=None, alias="AuthCode")


class DomainTransferabilityModel(BaseModel):
    transferable: Optional[
        Literal[
            "DOMAIN_IN_ANOTHER_ACCOUNT",
            "DOMAIN_IN_OWN_ACCOUNT",
            "DONT_KNOW",
            "PREMIUM_DOMAIN",
            "TRANSFERABLE",
            "UNTRANSFERABLE",
        ]
    ] = Field(default=None, alias="Transferable")


class ConsentModel(BaseModel):
    max_price: float = Field(alias="MaxPrice")
    currency: str = Field(alias="Currency")


class ExtraParamModel(BaseModel):
    name: Literal[
        "AU_ID_NUMBER",
        "AU_ID_TYPE",
        "AU_PRIORITY_TOKEN",
        "BIRTH_CITY",
        "BIRTH_COUNTRY",
        "BIRTH_DATE_IN_YYYY_MM_DD",
        "BIRTH_DEPARTMENT",
        "BRAND_NUMBER",
        "CA_BUSINESS_ENTITY_TYPE",
        "CA_LEGAL_REPRESENTATIVE",
        "CA_LEGAL_REPRESENTATIVE_CAPACITY",
        "CA_LEGAL_TYPE",
        "DOCUMENT_NUMBER",
        "DUNS_NUMBER",
        "ES_IDENTIFICATION",
        "ES_IDENTIFICATION_TYPE",
        "ES_LEGAL_FORM",
        "EU_COUNTRY_OF_CITIZENSHIP",
        "FI_BUSINESS_NUMBER",
        "FI_ID_NUMBER",
        "FI_NATIONALITY",
        "FI_ORGANIZATION_TYPE",
        "IT_NATIONALITY",
        "IT_PIN",
        "IT_REGISTRANT_ENTITY_TYPE",
        "RU_PASSPORT_DATA",
        "SE_ID_NUMBER",
        "SG_ID_NUMBER",
        "UK_COMPANY_NUMBER",
        "UK_CONTACT_TYPE",
        "VAT_NUMBER",
    ] = Field(alias="Name")
    value: str = Field(alias="Value")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteTagsForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    tags_to_delete: Sequence[str] = Field(alias="TagsToDelete")


class DisableDomainAutoRenewRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DisableDomainTransferLockRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DisassociateDelegationSignerFromDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    id: str = Field(alias="Id")


class DnssecKeyModel(BaseModel):
    algorithm: Optional[int] = Field(default=None, alias="Algorithm")
    flags: Optional[int] = Field(default=None, alias="Flags")
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    digest_type: Optional[int] = Field(default=None, alias="DigestType")
    digest: Optional[str] = Field(default=None, alias="Digest")
    key_tag: Optional[int] = Field(default=None, alias="KeyTag")
    id: Optional[str] = Field(default=None, alias="Id")


class PriceWithCurrencyModel(BaseModel):
    price: float = Field(alias="Price")
    currency: str = Field(alias="Currency")


class DomainSuggestionModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    availability: Optional[str] = Field(default=None, alias="Availability")


class DomainSummaryModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    auto_renew: Optional[bool] = Field(default=None, alias="AutoRenew")
    transfer_lock: Optional[bool] = Field(default=None, alias="TransferLock")
    expiry: Optional[datetime] = Field(default=None, alias="Expiry")


class EnableDomainAutoRenewRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class EnableDomainTransferLockRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class FilterConditionModel(BaseModel):
    name: Literal["DomainName", "Expiry"] = Field(alias="Name")
    operator: Literal["BEGINS_WITH", "GE", "LE"] = Field(alias="Operator")
    values: Sequence[str] = Field(alias="Values")


class GetContactReachabilityStatusRequestModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")


class GetDomainDetailRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class NameserverModel(BaseModel):
    name: str = Field(alias="Name")
    glue_ips: Optional[List[str]] = Field(default=None, alias="GlueIps")


class GetDomainSuggestionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    suggestion_count: int = Field(alias="SuggestionCount")
    only_available: bool = Field(alias="OnlyAvailable")


class GetOperationDetailRequestModel(BaseModel):
    operation_id: str = Field(alias="OperationId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class SortConditionModel(BaseModel):
    name: Literal["DomainName", "Expiry"] = Field(alias="Name")
    sort_order: Literal["ASC", "DESC"] = Field(alias="SortOrder")


class ListOperationsRequestModel(BaseModel):
    submitted_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedSince"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    status: Optional[
        Sequence[Literal["ERROR", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCESSFUL"]]
    ] = Field(default=None, alias="Status")
    type: Optional[
        Sequence[
            Literal[
                "ADD_DNSSEC",
                "CHANGE_DOMAIN_OWNER",
                "CHANGE_PRIVACY_PROTECTION",
                "DELETE_DOMAIN",
                "DISABLE_AUTORENEW",
                "DOMAIN_LOCK",
                "ENABLE_AUTORENEW",
                "EXPIRE_DOMAIN",
                "INTERNAL_TRANSFER_IN_DOMAIN",
                "INTERNAL_TRANSFER_OUT_DOMAIN",
                "PUSH_DOMAIN",
                "REGISTER_DOMAIN",
                "REMOVE_DNSSEC",
                "RENEW_DOMAIN",
                "TRANSFER_IN_DOMAIN",
                "TRANSFER_OUT_DOMAIN",
                "UPDATE_DOMAIN_CONTACT",
                "UPDATE_NAMESERVER",
            ]
        ]
    ] = Field(default=None, alias="Type")
    sort_by: Optional[Literal["SubmittedDate"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="SortOrder"
    )


class OperationSummaryModel(BaseModel):
    operation_id: Optional[str] = Field(default=None, alias="OperationId")
    status: Optional[
        Literal["ERROR", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCESSFUL"]
    ] = Field(default=None, alias="Status")
    type: Optional[
        Literal[
            "ADD_DNSSEC",
            "CHANGE_DOMAIN_OWNER",
            "CHANGE_PRIVACY_PROTECTION",
            "DELETE_DOMAIN",
            "DISABLE_AUTORENEW",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "EXPIRE_DOMAIN",
            "INTERNAL_TRANSFER_IN_DOMAIN",
            "INTERNAL_TRANSFER_OUT_DOMAIN",
            "PUSH_DOMAIN",
            "REGISTER_DOMAIN",
            "REMOVE_DNSSEC",
            "RENEW_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
        ]
    ] = Field(default=None, alias="Type")
    submitted_date: Optional[datetime] = Field(default=None, alias="SubmittedDate")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    message: Optional[str] = Field(default=None, alias="Message")
    status_flag: Optional[
        Literal[
            "PENDING_ACCEPTANCE",
            "PENDING_AUTHORIZATION",
            "PENDING_CUSTOMER_ACTION",
            "PENDING_PAYMENT_VERIFICATION",
            "PENDING_SUPPORT_CASE",
        ]
    ] = Field(default=None, alias="StatusFlag")
    last_updated_date: Optional[datetime] = Field(default=None, alias="LastUpdatedDate")


class ListPricesRequestModel(BaseModel):
    tld: Optional[str] = Field(default=None, alias="Tld")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListTagsForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class PushDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    target: str = Field(alias="Target")


class RejectDomainTransferFromAnotherAwsAccountRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class RenewDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    current_expiry_year: int = Field(alias="CurrentExpiryYear")
    duration_in_years: Optional[int] = Field(default=None, alias="DurationInYears")


class ResendContactReachabilityEmailRequestModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")


class ResendOperationAuthorizationRequestModel(BaseModel):
    operation_id: str = Field(alias="OperationId")


class RetrieveDomainAuthCodeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class TransferDomainToAnotherAwsAccountRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    account_id: str = Field(alias="AccountId")


class UpdateDomainContactPrivacyRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    admin_privacy: Optional[bool] = Field(default=None, alias="AdminPrivacy")
    registrant_privacy: Optional[bool] = Field(default=None, alias="RegistrantPrivacy")
    tech_privacy: Optional[bool] = Field(default=None, alias="TechPrivacy")


class ViewBillingRequestModel(BaseModel):
    start: Optional[Union[datetime, str]] = Field(default=None, alias="Start")
    end: Optional[Union[datetime, str]] = Field(default=None, alias="End")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class AcceptDomainTransferFromAnotherAwsAccountResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateDelegationSignerToDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelDomainTransferToAnotherAwsAccountResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckDomainAvailabilityResponseModel(BaseModel):
    availability: Literal[
        "AVAILABLE",
        "AVAILABLE_PREORDER",
        "AVAILABLE_RESERVED",
        "DONT_KNOW",
        "RESERVED",
        "UNAVAILABLE",
        "UNAVAILABLE_PREMIUM",
        "UNAVAILABLE_RESTRICTED",
    ] = Field(alias="Availability")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableDomainTransferLockResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateDelegationSignerFromDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableDomainTransferLockResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactReachabilityStatusResponseModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    status: Literal["DONE", "EXPIRED", "PENDING"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOperationDetailResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    status: Literal[
        "ERROR", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCESSFUL"
    ] = Field(alias="Status")
    message: str = Field(alias="Message")
    domain_name: str = Field(alias="DomainName")
    type: Literal[
        "ADD_DNSSEC",
        "CHANGE_DOMAIN_OWNER",
        "CHANGE_PRIVACY_PROTECTION",
        "DELETE_DOMAIN",
        "DISABLE_AUTORENEW",
        "DOMAIN_LOCK",
        "ENABLE_AUTORENEW",
        "EXPIRE_DOMAIN",
        "INTERNAL_TRANSFER_IN_DOMAIN",
        "INTERNAL_TRANSFER_OUT_DOMAIN",
        "PUSH_DOMAIN",
        "REGISTER_DOMAIN",
        "REMOVE_DNSSEC",
        "RENEW_DOMAIN",
        "TRANSFER_IN_DOMAIN",
        "TRANSFER_OUT_DOMAIN",
        "UPDATE_DOMAIN_CONTACT",
        "UPDATE_NAMESERVER",
    ] = Field(alias="Type")
    submitted_date: datetime = Field(alias="SubmittedDate")
    last_updated_date: datetime = Field(alias="LastUpdatedDate")
    status_flag: Literal[
        "PENDING_ACCEPTANCE",
        "PENDING_AUTHORIZATION",
        "PENDING_CUSTOMER_ACTION",
        "PENDING_PAYMENT_VERIFICATION",
        "PENDING_SUPPORT_CASE",
    ] = Field(alias="StatusFlag")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectDomainTransferFromAnotherAwsAccountResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RenewDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResendContactReachabilityEmailResponseModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    email_address: str = Field(alias="emailAddress")
    is_already_verified: bool = Field(alias="isAlreadyVerified")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RetrieveDomainAuthCodeResponseModel(BaseModel):
    auth_code: str = Field(alias="AuthCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransferDomainResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransferDomainToAnotherAwsAccountResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    password: str = Field(alias="Password")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainContactPrivacyResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainContactResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainNameserversResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateDelegationSignerToDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    signing_attributes: DnssecSigningAttributesModel = Field(alias="SigningAttributes")


class ViewBillingResponseModel(BaseModel):
    next_page_marker: str = Field(alias="NextPageMarker")
    billing_records: List[BillingRecordModel] = Field(alias="BillingRecords")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckDomainTransferabilityResponseModel(BaseModel):
    transferability: DomainTransferabilityModel = Field(alias="Transferability")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContactDetailModel(BaseModel):
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    contact_type: Optional[
        Literal["ASSOCIATION", "COMPANY", "PERSON", "PUBLIC_BODY", "RESELLER"]
    ] = Field(default=None, alias="ContactType")
    organization_name: Optional[str] = Field(default=None, alias="OrganizationName")
    address_line1: Optional[str] = Field(default=None, alias="AddressLine1")
    address_line2: Optional[str] = Field(default=None, alias="AddressLine2")
    city: Optional[str] = Field(default=None, alias="City")
    state: Optional[str] = Field(default=None, alias="State")
    country_code: Optional[
        Literal[
            "AC",
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
            "AX",
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
            "BQ",
            "BR",
            "BS",
            "BT",
            "BV",
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
            "GF",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GP",
            "GQ",
            "GR",
            "GS",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HM",
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
            "MQ",
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
            "NF",
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
            "PS",
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
            "SS",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TF",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TP",
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
    ] = Field(default=None, alias="CountryCode")
    zip_code: Optional[str] = Field(default=None, alias="ZipCode")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    email: Optional[str] = Field(default=None, alias="Email")
    fax: Optional[str] = Field(default=None, alias="Fax")
    extra_params: Optional[List[ExtraParamModel]] = Field(
        default=None, alias="ExtraParams"
    )


class DomainPriceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    registration_price: Optional[PriceWithCurrencyModel] = Field(
        default=None, alias="RegistrationPrice"
    )
    transfer_price: Optional[PriceWithCurrencyModel] = Field(
        default=None, alias="TransferPrice"
    )
    renewal_price: Optional[PriceWithCurrencyModel] = Field(
        default=None, alias="RenewalPrice"
    )
    change_ownership_price: Optional[PriceWithCurrencyModel] = Field(
        default=None, alias="ChangeOwnershipPrice"
    )
    restoration_price: Optional[PriceWithCurrencyModel] = Field(
        default=None, alias="RestorationPrice"
    )


class GetDomainSuggestionsResponseModel(BaseModel):
    suggestions_list: List[DomainSuggestionModel] = Field(alias="SuggestionsList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsResponseModel(BaseModel):
    domains: List[DomainSummaryModel] = Field(alias="Domains")
    next_page_marker: str = Field(alias="NextPageMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainNameserversRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    nameservers: Sequence[NameserverModel] = Field(alias="Nameservers")
    fiauth_key: Optional[str] = Field(default=None, alias="FIAuthKey")


class ListOperationsRequestListOperationsPaginateModel(BaseModel):
    submitted_since: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedSince"
    )
    status: Optional[
        Sequence[Literal["ERROR", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCESSFUL"]]
    ] = Field(default=None, alias="Status")
    type: Optional[
        Sequence[
            Literal[
                "ADD_DNSSEC",
                "CHANGE_DOMAIN_OWNER",
                "CHANGE_PRIVACY_PROTECTION",
                "DELETE_DOMAIN",
                "DISABLE_AUTORENEW",
                "DOMAIN_LOCK",
                "ENABLE_AUTORENEW",
                "EXPIRE_DOMAIN",
                "INTERNAL_TRANSFER_IN_DOMAIN",
                "INTERNAL_TRANSFER_OUT_DOMAIN",
                "PUSH_DOMAIN",
                "REGISTER_DOMAIN",
                "REMOVE_DNSSEC",
                "RENEW_DOMAIN",
                "TRANSFER_IN_DOMAIN",
                "TRANSFER_OUT_DOMAIN",
                "UPDATE_DOMAIN_CONTACT",
                "UPDATE_NAMESERVER",
            ]
        ]
    ] = Field(default=None, alias="Type")
    sort_by: Optional[Literal["SubmittedDate"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPricesRequestListPricesPaginateModel(BaseModel):
    tld: Optional[str] = Field(default=None, alias="Tld")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ViewBillingRequestViewBillingPaginateModel(BaseModel):
    start: Optional[Union[datetime, str]] = Field(default=None, alias="Start")
    end: Optional[Union[datetime, str]] = Field(default=None, alias="End")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainsRequestListDomainsPaginateModel(BaseModel):
    filter_conditions: Optional[Sequence[FilterConditionModel]] = Field(
        default=None, alias="FilterConditions"
    )
    sort_condition: Optional[SortConditionModel] = Field(
        default=None, alias="SortCondition"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainsRequestModel(BaseModel):
    filter_conditions: Optional[Sequence[FilterConditionModel]] = Field(
        default=None, alias="FilterConditions"
    )
    sort_condition: Optional[SortConditionModel] = Field(
        default=None, alias="SortCondition"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListOperationsResponseModel(BaseModel):
    operations: List[OperationSummaryModel] = Field(alias="Operations")
    next_page_marker: str = Field(alias="NextPageMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForDomainResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTagsForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    tags_to_update: Optional[Sequence[TagModel]] = Field(
        default=None, alias="TagsToUpdate"
    )


class GetDomainDetailResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    nameservers: List[NameserverModel] = Field(alias="Nameservers")
    auto_renew: bool = Field(alias="AutoRenew")
    admin_contact: ContactDetailModel = Field(alias="AdminContact")
    registrant_contact: ContactDetailModel = Field(alias="RegistrantContact")
    tech_contact: ContactDetailModel = Field(alias="TechContact")
    admin_privacy: bool = Field(alias="AdminPrivacy")
    registrant_privacy: bool = Field(alias="RegistrantPrivacy")
    tech_privacy: bool = Field(alias="TechPrivacy")
    registrar_name: str = Field(alias="RegistrarName")
    who_is_server: str = Field(alias="WhoIsServer")
    registrar_url: str = Field(alias="RegistrarUrl")
    abuse_contact_email: str = Field(alias="AbuseContactEmail")
    abuse_contact_phone: str = Field(alias="AbuseContactPhone")
    registry_domain_id: str = Field(alias="RegistryDomainId")
    creation_date: datetime = Field(alias="CreationDate")
    updated_date: datetime = Field(alias="UpdatedDate")
    expiration_date: datetime = Field(alias="ExpirationDate")
    reseller: str = Field(alias="Reseller")
    dns_sec: str = Field(alias="DnsSec")
    status_list: List[str] = Field(alias="StatusList")
    dnssec_keys: List[DnssecKeyModel] = Field(alias="DnssecKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    duration_in_years: int = Field(alias="DurationInYears")
    admin_contact: ContactDetailModel = Field(alias="AdminContact")
    registrant_contact: ContactDetailModel = Field(alias="RegistrantContact")
    tech_contact: ContactDetailModel = Field(alias="TechContact")
    idn_lang_code: Optional[str] = Field(default=None, alias="IdnLangCode")
    auto_renew: Optional[bool] = Field(default=None, alias="AutoRenew")
    privacy_protect_admin_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectAdminContact"
    )
    privacy_protect_registrant_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectRegistrantContact"
    )
    privacy_protect_tech_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectTechContact"
    )


class TransferDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    duration_in_years: int = Field(alias="DurationInYears")
    admin_contact: ContactDetailModel = Field(alias="AdminContact")
    registrant_contact: ContactDetailModel = Field(alias="RegistrantContact")
    tech_contact: ContactDetailModel = Field(alias="TechContact")
    idn_lang_code: Optional[str] = Field(default=None, alias="IdnLangCode")
    nameservers: Optional[Sequence[NameserverModel]] = Field(
        default=None, alias="Nameservers"
    )
    auth_code: Optional[str] = Field(default=None, alias="AuthCode")
    auto_renew: Optional[bool] = Field(default=None, alias="AutoRenew")
    privacy_protect_admin_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectAdminContact"
    )
    privacy_protect_registrant_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectRegistrantContact"
    )
    privacy_protect_tech_contact: Optional[bool] = Field(
        default=None, alias="PrivacyProtectTechContact"
    )


class UpdateDomainContactRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    admin_contact: Optional[ContactDetailModel] = Field(
        default=None, alias="AdminContact"
    )
    registrant_contact: Optional[ContactDetailModel] = Field(
        default=None, alias="RegistrantContact"
    )
    tech_contact: Optional[ContactDetailModel] = Field(
        default=None, alias="TechContact"
    )
    consent: Optional[ConsentModel] = Field(default=None, alias="Consent")


class ListPricesResponseModel(BaseModel):
    prices: List[DomainPriceModel] = Field(alias="Prices")
    next_page_marker: str = Field(alias="NextPageMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
