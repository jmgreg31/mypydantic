# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateBrowserSettingsRequestModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")
    portal_arn: str = Field(alias="portalArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateNetworkSettingsRequestModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")
    portal_arn: str = Field(alias="portalArn")


class AssociateTrustStoreRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    trust_store_arn: str = Field(alias="trustStoreArn")


class AssociateUserAccessLoggingSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")


class AssociateUserSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    user_settings_arn: str = Field(alias="userSettingsArn")


class BrowserSettingsSummaryModel(BaseModel):
    browser_settings_arn: Optional[str] = Field(
        default=None, alias="browserSettingsArn"
    )


class BrowserSettingsModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")
    associated_portal_arns: Optional[List[str]] = Field(
        default=None, alias="associatedPortalArns"
    )
    browser_policy: Optional[str] = Field(default=None, alias="browserPolicy")


class CertificateSummaryModel(BaseModel):
    issuer: Optional[str] = Field(default=None, alias="issuer")
    not_valid_after: Optional[datetime] = Field(default=None, alias="notValidAfter")
    not_valid_before: Optional[datetime] = Field(default=None, alias="notValidBefore")
    subject: Optional[str] = Field(default=None, alias="subject")
    thumbprint: Optional[str] = Field(default=None, alias="thumbprint")


class CertificateModel(BaseModel):
    body: Optional[bytes] = Field(default=None, alias="body")
    issuer: Optional[str] = Field(default=None, alias="issuer")
    not_valid_after: Optional[datetime] = Field(default=None, alias="notValidAfter")
    not_valid_before: Optional[datetime] = Field(default=None, alias="notValidBefore")
    subject: Optional[str] = Field(default=None, alias="subject")
    thumbprint: Optional[str] = Field(default=None, alias="thumbprint")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateIdentityProviderRequestModel(BaseModel):
    identity_provider_details: Mapping[str, str] = Field(
        alias="identityProviderDetails"
    )
    identity_provider_name: str = Field(alias="identityProviderName")
    identity_provider_type: Literal[
        "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
    ] = Field(alias="identityProviderType")
    portal_arn: str = Field(alias="portalArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteBrowserSettingsRequestModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")


class DeleteIdentityProviderRequestModel(BaseModel):
    identity_provider_arn: str = Field(alias="identityProviderArn")


class DeleteNetworkSettingsRequestModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")


class DeletePortalRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class DeleteTrustStoreRequestModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")


class DeleteUserAccessLoggingSettingsRequestModel(BaseModel):
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")


class DeleteUserSettingsRequestModel(BaseModel):
    user_settings_arn: str = Field(alias="userSettingsArn")


class DisassociateBrowserSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class DisassociateNetworkSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class DisassociateTrustStoreRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class DisassociateUserAccessLoggingSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class DisassociateUserSettingsRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class GetBrowserSettingsRequestModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")


class GetIdentityProviderRequestModel(BaseModel):
    identity_provider_arn: str = Field(alias="identityProviderArn")


class IdentityProviderModel(BaseModel):
    identity_provider_arn: str = Field(alias="identityProviderArn")
    identity_provider_details: Optional[Dict[str, str]] = Field(
        default=None, alias="identityProviderDetails"
    )
    identity_provider_name: Optional[str] = Field(
        default=None, alias="identityProviderName"
    )
    identity_provider_type: Optional[
        Literal[
            "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
        ]
    ] = Field(default=None, alias="identityProviderType")


class GetNetworkSettingsRequestModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")


class NetworkSettingsModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")
    associated_portal_arns: Optional[List[str]] = Field(
        default=None, alias="associatedPortalArns"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class GetPortalRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class PortalModel(BaseModel):
    authentication_type: Optional[Literal["IAM_Identity_Center", "Standard"]] = Field(
        default=None, alias="authenticationType"
    )
    browser_settings_arn: Optional[str] = Field(
        default=None, alias="browserSettingsArn"
    )
    browser_type: Optional[Literal["Chrome"]] = Field(default=None, alias="browserType")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    network_settings_arn: Optional[str] = Field(
        default=None, alias="networkSettingsArn"
    )
    portal_arn: Optional[str] = Field(default=None, alias="portalArn")
    portal_endpoint: Optional[str] = Field(default=None, alias="portalEndpoint")
    portal_status: Optional[Literal["Active", "Incomplete", "Pending"]] = Field(
        default=None, alias="portalStatus"
    )
    renderer_type: Optional[Literal["AppStream"]] = Field(
        default=None, alias="rendererType"
    )
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    trust_store_arn: Optional[str] = Field(default=None, alias="trustStoreArn")
    user_access_logging_settings_arn: Optional[str] = Field(
        default=None, alias="userAccessLoggingSettingsArn"
    )
    user_settings_arn: Optional[str] = Field(default=None, alias="userSettingsArn")


class GetPortalServiceProviderMetadataRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")


class GetTrustStoreCertificateRequestModel(BaseModel):
    thumbprint: str = Field(alias="thumbprint")
    trust_store_arn: str = Field(alias="trustStoreArn")


class GetTrustStoreRequestModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")


class TrustStoreModel(BaseModel):
    associated_portal_arns: Optional[List[str]] = Field(
        default=None, alias="associatedPortalArns"
    )
    trust_store_arn: Optional[str] = Field(default=None, alias="trustStoreArn")


class GetUserAccessLoggingSettingsRequestModel(BaseModel):
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")


class UserAccessLoggingSettingsModel(BaseModel):
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")
    associated_portal_arns: Optional[List[str]] = Field(
        default=None, alias="associatedPortalArns"
    )
    kinesis_stream_arn: Optional[str] = Field(default=None, alias="kinesisStreamArn")


class GetUserSettingsRequestModel(BaseModel):
    user_settings_arn: str = Field(alias="userSettingsArn")


class UserSettingsModel(BaseModel):
    user_settings_arn: str = Field(alias="userSettingsArn")
    associated_portal_arns: Optional[List[str]] = Field(
        default=None, alias="associatedPortalArns"
    )
    copy_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="copyAllowed"
    )
    disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="disconnectTimeoutInMinutes"
    )
    download_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="downloadAllowed"
    )
    idle_disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="idleDisconnectTimeoutInMinutes"
    )
    paste_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="pasteAllowed"
    )
    print_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="printAllowed"
    )
    upload_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="uploadAllowed"
    )


class IdentityProviderSummaryModel(BaseModel):
    identity_provider_arn: Optional[str] = Field(
        default=None, alias="identityProviderArn"
    )
    identity_provider_name: Optional[str] = Field(
        default=None, alias="identityProviderName"
    )
    identity_provider_type: Optional[
        Literal[
            "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
        ]
    ] = Field(default=None, alias="identityProviderType")


class ListBrowserSettingsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListIdentityProvidersRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListNetworkSettingsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class NetworkSettingsSummaryModel(BaseModel):
    network_settings_arn: Optional[str] = Field(
        default=None, alias="networkSettingsArn"
    )
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class ListPortalsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PortalSummaryModel(BaseModel):
    authentication_type: Optional[Literal["IAM_Identity_Center", "Standard"]] = Field(
        default=None, alias="authenticationType"
    )
    browser_settings_arn: Optional[str] = Field(
        default=None, alias="browserSettingsArn"
    )
    browser_type: Optional[Literal["Chrome"]] = Field(default=None, alias="browserType")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    network_settings_arn: Optional[str] = Field(
        default=None, alias="networkSettingsArn"
    )
    portal_arn: Optional[str] = Field(default=None, alias="portalArn")
    portal_endpoint: Optional[str] = Field(default=None, alias="portalEndpoint")
    portal_status: Optional[Literal["Active", "Incomplete", "Pending"]] = Field(
        default=None, alias="portalStatus"
    )
    renderer_type: Optional[Literal["AppStream"]] = Field(
        default=None, alias="rendererType"
    )
    trust_store_arn: Optional[str] = Field(default=None, alias="trustStoreArn")
    user_access_logging_settings_arn: Optional[str] = Field(
        default=None, alias="userAccessLoggingSettingsArn"
    )
    user_settings_arn: Optional[str] = Field(default=None, alias="userSettingsArn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTrustStoreCertificatesRequestModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTrustStoresRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TrustStoreSummaryModel(BaseModel):
    trust_store_arn: Optional[str] = Field(default=None, alias="trustStoreArn")


class ListUserAccessLoggingSettingsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UserAccessLoggingSettingsSummaryModel(BaseModel):
    kinesis_stream_arn: Optional[str] = Field(default=None, alias="kinesisStreamArn")
    user_access_logging_settings_arn: Optional[str] = Field(
        default=None, alias="userAccessLoggingSettingsArn"
    )


class ListUserSettingsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UserSettingsSummaryModel(BaseModel):
    copy_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="copyAllowed"
    )
    disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="disconnectTimeoutInMinutes"
    )
    download_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="downloadAllowed"
    )
    idle_disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="idleDisconnectTimeoutInMinutes"
    )
    paste_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="pasteAllowed"
    )
    print_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="printAllowed"
    )
    upload_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="uploadAllowed"
    )
    user_settings_arn: Optional[str] = Field(default=None, alias="userSettingsArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateBrowserSettingsRequestModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")
    browser_policy: Optional[str] = Field(default=None, alias="browserPolicy")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateIdentityProviderRequestModel(BaseModel):
    identity_provider_arn: str = Field(alias="identityProviderArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    identity_provider_details: Optional[Mapping[str, str]] = Field(
        default=None, alias="identityProviderDetails"
    )
    identity_provider_name: Optional[str] = Field(
        default=None, alias="identityProviderName"
    )
    identity_provider_type: Optional[
        Literal[
            "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
        ]
    ] = Field(default=None, alias="identityProviderType")


class UpdateNetworkSettingsRequestModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class UpdatePortalRequestModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    authentication_type: Optional[Literal["IAM_Identity_Center", "Standard"]] = Field(
        default=None, alias="authenticationType"
    )
    display_name: Optional[str] = Field(default=None, alias="displayName")


class UpdateTrustStoreRequestModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")
    certificates_to_add: Optional[
        Sequence[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]]
    ] = Field(default=None, alias="certificatesToAdd")
    certificates_to_delete: Optional[Sequence[str]] = Field(
        default=None, alias="certificatesToDelete"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateUserAccessLoggingSettingsRequestModel(BaseModel):
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    kinesis_stream_arn: Optional[str] = Field(default=None, alias="kinesisStreamArn")


class UpdateUserSettingsRequestModel(BaseModel):
    user_settings_arn: str = Field(alias="userSettingsArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    copy_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="copyAllowed"
    )
    disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="disconnectTimeoutInMinutes"
    )
    download_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="downloadAllowed"
    )
    idle_disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="idleDisconnectTimeoutInMinutes"
    )
    paste_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="pasteAllowed"
    )
    print_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="printAllowed"
    )
    upload_allowed: Optional[Literal["Disabled", "Enabled"]] = Field(
        default=None, alias="uploadAllowed"
    )


class AssociateBrowserSettingsResponseModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")
    portal_arn: str = Field(alias="portalArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateNetworkSettingsResponseModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")
    portal_arn: str = Field(alias="portalArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateTrustStoreResponseModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    trust_store_arn: str = Field(alias="trustStoreArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateUserAccessLoggingSettingsResponseModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateUserSettingsResponseModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    user_settings_arn: str = Field(alias="userSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBrowserSettingsResponseModel(BaseModel):
    browser_settings_arn: str = Field(alias="browserSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIdentityProviderResponseModel(BaseModel):
    identity_provider_arn: str = Field(alias="identityProviderArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkSettingsResponseModel(BaseModel):
    network_settings_arn: str = Field(alias="networkSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePortalResponseModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    portal_endpoint: str = Field(alias="portalEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrustStoreResponseModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserAccessLoggingSettingsResponseModel(BaseModel):
    user_access_logging_settings_arn: str = Field(alias="userAccessLoggingSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserSettingsResponseModel(BaseModel):
    user_settings_arn: str = Field(alias="userSettingsArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPortalServiceProviderMetadataResponseModel(BaseModel):
    portal_arn: str = Field(alias="portalArn")
    service_provider_saml_metadata: str = Field(alias="serviceProviderSamlMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrustStoreResponseModel(BaseModel):
    trust_store_arn: str = Field(alias="trustStoreArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBrowserSettingsResponseModel(BaseModel):
    browser_settings: List[BrowserSettingsSummaryModel] = Field(alias="browserSettings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBrowserSettingsResponseModel(BaseModel):
    browser_settings: BrowserSettingsModel = Field(alias="browserSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBrowserSettingsResponseModel(BaseModel):
    browser_settings: BrowserSettingsModel = Field(alias="browserSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrustStoreCertificatesResponseModel(BaseModel):
    certificate_list: List[CertificateSummaryModel] = Field(alias="certificateList")
    next_token: str = Field(alias="nextToken")
    trust_store_arn: str = Field(alias="trustStoreArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrustStoreCertificateResponseModel(BaseModel):
    certificate: CertificateModel = Field(alias="certificate")
    trust_store_arn: str = Field(alias="trustStoreArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBrowserSettingsRequestModel(BaseModel):
    browser_policy: str = Field(alias="browserPolicy")
    additional_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="additionalEncryptionContext"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    customer_managed_key: Optional[str] = Field(
        default=None, alias="customerManagedKey"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateNetworkSettingsRequestModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="securityGroupIds")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    vpc_id: str = Field(alias="vpcId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreatePortalRequestModel(BaseModel):
    additional_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="additionalEncryptionContext"
    )
    authentication_type: Optional[Literal["IAM_Identity_Center", "Standard"]] = Field(
        default=None, alias="authenticationType"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    customer_managed_key: Optional[str] = Field(
        default=None, alias="customerManagedKey"
    )
    display_name: Optional[str] = Field(default=None, alias="displayName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateTrustStoreRequestModel(BaseModel):
    certificate_list: Sequence[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(alias="certificateList")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateUserAccessLoggingSettingsRequestModel(BaseModel):
    kinesis_stream_arn: str = Field(alias="kinesisStreamArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateUserSettingsRequestModel(BaseModel):
    copy_allowed: Literal["Disabled", "Enabled"] = Field(alias="copyAllowed")
    download_allowed: Literal["Disabled", "Enabled"] = Field(alias="downloadAllowed")
    paste_allowed: Literal["Disabled", "Enabled"] = Field(alias="pasteAllowed")
    print_allowed: Literal["Disabled", "Enabled"] = Field(alias="printAllowed")
    upload_allowed: Literal["Disabled", "Enabled"] = Field(alias="uploadAllowed")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="disconnectTimeoutInMinutes"
    )
    idle_disconnect_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="idleDisconnectTimeoutInMinutes"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetIdentityProviderResponseModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="identityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIdentityProviderResponseModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="identityProvider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkSettingsResponseModel(BaseModel):
    network_settings: NetworkSettingsModel = Field(alias="networkSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNetworkSettingsResponseModel(BaseModel):
    network_settings: NetworkSettingsModel = Field(alias="networkSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPortalResponseModel(BaseModel):
    portal: PortalModel = Field(alias="portal")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePortalResponseModel(BaseModel):
    portal: PortalModel = Field(alias="portal")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrustStoreResponseModel(BaseModel):
    trust_store: TrustStoreModel = Field(alias="trustStore")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserAccessLoggingSettingsResponseModel(BaseModel):
    user_access_logging_settings: UserAccessLoggingSettingsModel = Field(
        alias="userAccessLoggingSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserAccessLoggingSettingsResponseModel(BaseModel):
    user_access_logging_settings: UserAccessLoggingSettingsModel = Field(
        alias="userAccessLoggingSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserSettingsResponseModel(BaseModel):
    user_settings: UserSettingsModel = Field(alias="userSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserSettingsResponseModel(BaseModel):
    user_settings: UserSettingsModel = Field(alias="userSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityProvidersResponseModel(BaseModel):
    identity_providers: List[IdentityProviderSummaryModel] = Field(
        alias="identityProviders"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworkSettingsResponseModel(BaseModel):
    network_settings: List[NetworkSettingsSummaryModel] = Field(alias="networkSettings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPortalsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    portals: List[PortalSummaryModel] = Field(alias="portals")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrustStoresResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    trust_stores: List[TrustStoreSummaryModel] = Field(alias="trustStores")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserAccessLoggingSettingsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    user_access_logging_settings: List[UserAccessLoggingSettingsSummaryModel] = Field(
        alias="userAccessLoggingSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserSettingsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    user_settings: List[UserSettingsSummaryModel] = Field(alias="userSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
