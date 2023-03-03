# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateDomainRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")
    acm_certificate_arn: str = Field(alias="AcmCertificateArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class AssociateWebsiteAuthorizationProviderRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    authorization_provider_type: Literal["SAML"] = Field(
        alias="AuthorizationProviderType"
    )
    domain_name: Optional[str] = Field(default=None, alias="DomainName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateWebsiteCertificateAuthorityRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    certificate: str = Field(alias="Certificate")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class CreateFleetRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    optimize_for_end_user_location: Optional[bool] = Field(
        default=None, alias="OptimizeForEndUserLocation"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteFleetRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeAuditStreamConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeCompanyNetworkConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeDevicePolicyConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeDeviceRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    device_id: str = Field(alias="DeviceId")


class DescribeDomainRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")


class DescribeFleetMetadataRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeIdentityProviderConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")


class DescribeWebsiteCertificateAuthorityRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    website_ca_id: str = Field(alias="WebsiteCaId")


class DeviceSummaryModel(BaseModel):
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    device_status: Optional[Literal["ACTIVE", "SIGNED_OUT"]] = Field(
        default=None, alias="DeviceStatus"
    )


class DisassociateDomainRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")


class DisassociateWebsiteAuthorizationProviderRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    authorization_provider_id: str = Field(alias="AuthorizationProviderId")


class DisassociateWebsiteCertificateAuthorityRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    website_ca_id: str = Field(alias="WebsiteCaId")


class DomainSummaryModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    created_time: datetime = Field(alias="CreatedTime")
    domain_status: Literal[
        "ACTIVE",
        "ASSOCIATING",
        "DISASSOCIATED",
        "DISASSOCIATING",
        "FAILED_TO_ASSOCIATE",
        "FAILED_TO_DISASSOCIATE",
        "INACTIVE",
        "PENDING_VALIDATION",
    ] = Field(alias="DomainStatus")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class FleetSummaryModel(BaseModel):
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    fleet_name: Optional[str] = Field(default=None, alias="FleetName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    company_code: Optional[str] = Field(default=None, alias="CompanyCode")
    fleet_status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "DELETED",
            "DELETING",
            "FAILED_TO_CREATE",
            "FAILED_TO_DELETE",
        ]
    ] = Field(default=None, alias="FleetStatus")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListDevicesRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDomainsRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFleetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListWebsiteAuthorizationProvidersRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class WebsiteAuthorizationProviderSummaryModel(BaseModel):
    authorization_provider_type: Literal["SAML"] = Field(
        alias="AuthorizationProviderType"
    )
    authorization_provider_id: Optional[str] = Field(
        default=None, alias="AuthorizationProviderId"
    )
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class ListWebsiteCertificateAuthoritiesRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class WebsiteCaSummaryModel(BaseModel):
    website_ca_id: Optional[str] = Field(default=None, alias="WebsiteCaId")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class RestoreDomainAccessRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")


class RevokeDomainAccessRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")


class SignOutUserRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    username: str = Field(alias="Username")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAuditStreamConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    audit_stream_arn: Optional[str] = Field(default=None, alias="AuditStreamArn")


class UpdateCompanyNetworkConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")


class UpdateDevicePolicyConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    device_ca_certificate: Optional[str] = Field(
        default=None, alias="DeviceCaCertificate"
    )


class UpdateDomainMetadataRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    domain_name: str = Field(alias="DomainName")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")


class UpdateFleetMetadataRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    optimize_for_end_user_location: Optional[bool] = Field(
        default=None, alias="OptimizeForEndUserLocation"
    )


class UpdateIdentityProviderConfigurationRequestModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    identity_provider_type: Literal["SAML"] = Field(alias="IdentityProviderType")
    identity_provider_saml_metadata: Optional[str] = Field(
        default=None, alias="IdentityProviderSamlMetadata"
    )


class AssociateWebsiteAuthorizationProviderResponseModel(BaseModel):
    authorization_provider_id: str = Field(alias="AuthorizationProviderId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateWebsiteCertificateAuthorityResponseModel(BaseModel):
    website_ca_id: str = Field(alias="WebsiteCaId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetResponseModel(BaseModel):
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAuditStreamConfigurationResponseModel(BaseModel):
    audit_stream_arn: str = Field(alias="AuditStreamArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCompanyNetworkConfigurationResponseModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDevicePolicyConfigurationResponseModel(BaseModel):
    device_ca_certificate: str = Field(alias="DeviceCaCertificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDeviceResponseModel(BaseModel):
    status: Literal["ACTIVE", "SIGNED_OUT"] = Field(alias="Status")
    model: str = Field(alias="Model")
    manufacturer: str = Field(alias="Manufacturer")
    operating_system: str = Field(alias="OperatingSystem")
    operating_system_version: str = Field(alias="OperatingSystemVersion")
    patch_level: str = Field(alias="PatchLevel")
    first_accessed_time: datetime = Field(alias="FirstAccessedTime")
    last_accessed_time: datetime = Field(alias="LastAccessedTime")
    username: str = Field(alias="Username")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    display_name: str = Field(alias="DisplayName")
    created_time: datetime = Field(alias="CreatedTime")
    domain_status: Literal[
        "ACTIVE",
        "ASSOCIATING",
        "DISASSOCIATED",
        "DISASSOCIATING",
        "FAILED_TO_ASSOCIATE",
        "FAILED_TO_DISASSOCIATE",
        "INACTIVE",
        "PENDING_VALIDATION",
    ] = Field(alias="DomainStatus")
    acm_certificate_arn: str = Field(alias="AcmCertificateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetMetadataResponseModel(BaseModel):
    created_time: datetime = Field(alias="CreatedTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    fleet_name: str = Field(alias="FleetName")
    display_name: str = Field(alias="DisplayName")
    optimize_for_end_user_location: bool = Field(alias="OptimizeForEndUserLocation")
    company_code: str = Field(alias="CompanyCode")
    fleet_status: Literal[
        "ACTIVE",
        "CREATING",
        "DELETED",
        "DELETING",
        "FAILED_TO_CREATE",
        "FAILED_TO_DELETE",
    ] = Field(alias="FleetStatus")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIdentityProviderConfigurationResponseModel(BaseModel):
    identity_provider_type: Literal["SAML"] = Field(alias="IdentityProviderType")
    service_provider_saml_metadata: str = Field(alias="ServiceProviderSamlMetadata")
    identity_provider_saml_metadata: str = Field(alias="IdentityProviderSamlMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeWebsiteCertificateAuthorityResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    created_time: datetime = Field(alias="CreatedTime")
    display_name: str = Field(alias="DisplayName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicesResponseModel(BaseModel):
    devices: List[DeviceSummaryModel] = Field(alias="Devices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsResponseModel(BaseModel):
    domains: List[DomainSummaryModel] = Field(alias="Domains")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFleetsResponseModel(BaseModel):
    fleet_summary_list: List[FleetSummaryModel] = Field(alias="FleetSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebsiteAuthorizationProvidersResponseModel(BaseModel):
    website_authorization_providers: List[
        WebsiteAuthorizationProviderSummaryModel
    ] = Field(alias="WebsiteAuthorizationProviders")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebsiteCertificateAuthoritiesResponseModel(BaseModel):
    website_certificate_authorities: List[WebsiteCaSummaryModel] = Field(
        alias="WebsiteCertificateAuthorities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
