# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AlternateContactModel(BaseModel):
    alternate_contact_type: Optional[
        Literal["BILLING", "OPERATIONS", "SECURITY"]
    ] = Field(default=None, alias="AlternateContactType")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    name: Optional[str] = Field(default=None, alias="Name")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    title: Optional[str] = Field(default=None, alias="Title")


class ContactInformationModel(BaseModel):
    address_line1: str = Field(alias="AddressLine1")
    city: str = Field(alias="City")
    country_code: str = Field(alias="CountryCode")
    full_name: str = Field(alias="FullName")
    phone_number: str = Field(alias="PhoneNumber")
    postal_code: str = Field(alias="PostalCode")
    address_line2: Optional[str] = Field(default=None, alias="AddressLine2")
    address_line3: Optional[str] = Field(default=None, alias="AddressLine3")
    company_name: Optional[str] = Field(default=None, alias="CompanyName")
    district_or_county: Optional[str] = Field(default=None, alias="DistrictOrCounty")
    state_or_region: Optional[str] = Field(default=None, alias="StateOrRegion")
    website_url: Optional[str] = Field(default=None, alias="WebsiteUrl")


class DeleteAlternateContactRequestModel(BaseModel):
    alternate_contact_type: Literal["BILLING", "OPERATIONS", "SECURITY"] = Field(
        alias="AlternateContactType"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class DisableRegionRequestModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EnableRegionRequestModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class GetAlternateContactRequestModel(BaseModel):
    alternate_contact_type: Literal["BILLING", "OPERATIONS", "SECURITY"] = Field(
        alias="AlternateContactType"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class GetContactInformationRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class GetRegionOptStatusRequestModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class ListRegionsRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    region_opt_status_contains: Optional[
        Sequence[
            Literal[
                "DISABLED", "DISABLING", "ENABLED", "ENABLED_BY_DEFAULT", "ENABLING"
            ]
        ]
    ] = Field(default=None, alias="RegionOptStatusContains")


class RegionModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    region_opt_status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLED_BY_DEFAULT", "ENABLING"]
    ] = Field(default=None, alias="RegionOptStatus")


class PutAlternateContactRequestModel(BaseModel):
    alternate_contact_type: Literal["BILLING", "OPERATIONS", "SECURITY"] = Field(
        alias="AlternateContactType"
    )
    email_address: str = Field(alias="EmailAddress")
    name: str = Field(alias="Name")
    phone_number: str = Field(alias="PhoneNumber")
    title: str = Field(alias="Title")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class PutContactInformationRequestModel(BaseModel):
    contact_information: ContactInformationModel = Field(alias="ContactInformation")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAlternateContactResponseModel(BaseModel):
    alternate_contact: AlternateContactModel = Field(alias="AlternateContact")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactInformationResponseModel(BaseModel):
    contact_information: ContactInformationModel = Field(alias="ContactInformation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegionOptStatusResponseModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    region_opt_status: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLED_BY_DEFAULT", "ENABLING"
    ] = Field(alias="RegionOptStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRegionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    regions: List[RegionModel] = Field(alias="Regions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
