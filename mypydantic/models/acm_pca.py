# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CustomAttributeModel(BaseModel):
    object_identifier: str = Field(alias="ObjectIdentifier")
    value: str = Field(alias="Value")


class AccessMethodModel(BaseModel):
    custom_object_identifier: Optional[str] = Field(
        default=None, alias="CustomObjectIdentifier"
    )
    access_method_type: Optional[
        Literal["CA_REPOSITORY", "RESOURCE_PKI_MANIFEST", "RESOURCE_PKI_NOTIFY"]
    ] = Field(default=None, alias="AccessMethodType")


class CreateCertificateAuthorityAuditReportRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    s3_bucket_name: str = Field(alias="S3BucketName")
    audit_report_response_format: Literal["CSV", "JSON"] = Field(
        alias="AuditReportResponseFormat"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CreatePermissionRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    principal: str = Field(alias="Principal")
    actions: Sequence[
        Literal["GetCertificate", "IssueCertificate", "ListPermissions"]
    ] = Field(alias="Actions")
    source_account: Optional[str] = Field(default=None, alias="SourceAccount")


class CrlConfigurationModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    expiration_in_days: Optional[int] = Field(default=None, alias="ExpirationInDays")
    custom_cname: Optional[str] = Field(default=None, alias="CustomCname")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_object_acl: Optional[
        Literal["BUCKET_OWNER_FULL_CONTROL", "PUBLIC_READ"]
    ] = Field(default=None, alias="S3ObjectAcl")


class KeyUsageModel(BaseModel):
    digital_signature: Optional[bool] = Field(default=None, alias="DigitalSignature")
    non_repudiation: Optional[bool] = Field(default=None, alias="NonRepudiation")
    key_encipherment: Optional[bool] = Field(default=None, alias="KeyEncipherment")
    data_encipherment: Optional[bool] = Field(default=None, alias="DataEncipherment")
    key_agreement: Optional[bool] = Field(default=None, alias="KeyAgreement")
    key_cert_sign: Optional[bool] = Field(default=None, alias="KeyCertSign")
    crl_sign: Optional[bool] = Field(default=None, alias="CRLSign")
    encipher_only: Optional[bool] = Field(default=None, alias="EncipherOnly")
    decipher_only: Optional[bool] = Field(default=None, alias="DecipherOnly")


class CustomExtensionModel(BaseModel):
    object_identifier: str = Field(alias="ObjectIdentifier")
    value: str = Field(alias="Value")
    critical: Optional[bool] = Field(default=None, alias="Critical")


class DeleteCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    permanent_deletion_time_in_days: Optional[int] = Field(
        default=None, alias="PermanentDeletionTimeInDays"
    )


class DeletePermissionRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    principal: str = Field(alias="Principal")
    source_account: Optional[str] = Field(default=None, alias="SourceAccount")


class DeletePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeCertificateAuthorityAuditReportRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    audit_report_id: str = Field(alias="AuditReportId")


class DescribeCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")


class EdiPartyNameModel(BaseModel):
    party_name: str = Field(alias="PartyName")
    name_assigner: Optional[str] = Field(default=None, alias="NameAssigner")


class ExtendedKeyUsageModel(BaseModel):
    extended_key_usage_type: Optional[
        Literal[
            "CERTIFICATE_TRANSPARENCY",
            "CLIENT_AUTH",
            "CODE_SIGNING",
            "DOCUMENT_SIGNING",
            "EMAIL_PROTECTION",
            "OCSP_SIGNING",
            "SERVER_AUTH",
            "SMART_CARD_LOGIN",
            "TIME_STAMPING",
        ]
    ] = Field(default=None, alias="ExtendedKeyUsageType")
    extended_key_usage_object_identifier: Optional[str] = Field(
        default=None, alias="ExtendedKeyUsageObjectIdentifier"
    )


class OtherNameModel(BaseModel):
    type_id: str = Field(alias="TypeId")
    value: str = Field(alias="Value")


class GetCertificateAuthorityCertificateRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")


class GetCertificateAuthorityCsrRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")


class GetCertificateRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    certificate_arn: str = Field(alias="CertificateArn")


class GetPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ImportCertificateAuthorityCertificateRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    certificate: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Certificate"
    )
    certificate_chain: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="CertificateChain")


class ValidityModel(BaseModel):
    value: int = Field(alias="Value")
    type: Literal["ABSOLUTE", "DAYS", "END_DATE", "MONTHS", "YEARS"] = Field(
        alias="Type"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListCertificateAuthoritiesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    resource_owner: Optional[Literal["OTHER_ACCOUNTS", "SELF"]] = Field(
        default=None, alias="ResourceOwner"
    )


class ListPermissionsRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PermissionModel(BaseModel):
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    principal: Optional[str] = Field(default=None, alias="Principal")
    source_account: Optional[str] = Field(default=None, alias="SourceAccount")
    actions: Optional[
        List[Literal["GetCertificate", "IssueCertificate", "ListPermissions"]]
    ] = Field(default=None, alias="Actions")
    policy: Optional[str] = Field(default=None, alias="Policy")


class ListTagsRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OcspConfigurationModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    ocsp_custom_cname: Optional[str] = Field(default=None, alias="OcspCustomCname")


class QualifierModel(BaseModel):
    cps_uri: str = Field(alias="CpsUri")


class PutPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")


class RestoreCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")


class RevokeCertificateRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    certificate_serial: str = Field(alias="CertificateSerial")
    revocation_reason: Literal[
        "AFFILIATION_CHANGED",
        "A_A_COMPROMISE",
        "CERTIFICATE_AUTHORITY_COMPROMISE",
        "CESSATION_OF_OPERATION",
        "KEY_COMPROMISE",
        "PRIVILEGE_WITHDRAWN",
        "SUPERSEDED",
        "UNSPECIFIED",
    ] = Field(alias="RevocationReason")


class ASN1SubjectModel(BaseModel):
    country: Optional[str] = Field(default=None, alias="Country")
    organization: Optional[str] = Field(default=None, alias="Organization")
    organizational_unit: Optional[str] = Field(default=None, alias="OrganizationalUnit")
    distinguished_name_qualifier: Optional[str] = Field(
        default=None, alias="DistinguishedNameQualifier"
    )
    state: Optional[str] = Field(default=None, alias="State")
    common_name: Optional[str] = Field(default=None, alias="CommonName")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    locality: Optional[str] = Field(default=None, alias="Locality")
    title: Optional[str] = Field(default=None, alias="Title")
    surname: Optional[str] = Field(default=None, alias="Surname")
    given_name: Optional[str] = Field(default=None, alias="GivenName")
    initials: Optional[str] = Field(default=None, alias="Initials")
    pseudonym: Optional[str] = Field(default=None, alias="Pseudonym")
    generation_qualifier: Optional[str] = Field(
        default=None, alias="GenerationQualifier"
    )
    custom_attributes: Optional[Sequence[CustomAttributeModel]] = Field(
        default=None, alias="CustomAttributes"
    )


class CreateCertificateAuthorityAuditReportResponseModel(BaseModel):
    audit_report_id: str = Field(alias="AuditReportId")
    s3_key: str = Field(alias="S3Key")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCertificateAuthorityResponseModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCertificateAuthorityAuditReportResponseModel(BaseModel):
    audit_report_status: Literal["CREATING", "FAILED", "SUCCESS"] = Field(
        alias="AuditReportStatus"
    )
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key: str = Field(alias="S3Key")
    created_at: datetime = Field(alias="CreatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCertificateAuthorityCertificateResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    certificate_chain: str = Field(alias="CertificateChain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCertificateAuthorityCsrResponseModel(BaseModel):
    csr: str = Field(alias="Csr")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCertificateResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    certificate_chain: str = Field(alias="CertificateChain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IssueCertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class UntagCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitModel(
    BaseModel
):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    audit_report_id: str = Field(alias="AuditReportId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitModel(
    BaseModel
):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetCertificateRequestCertificateIssuedWaitModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    certificate_arn: str = Field(alias="CertificateArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateModel(
    BaseModel
):
    resource_owner: Optional[Literal["OTHER_ACCOUNTS", "SELF"]] = Field(
        default=None, alias="ResourceOwner"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionsRequestListPermissionsPaginateModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsRequestListTagsPaginateModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionsResponseModel(BaseModel):
    permissions: List[PermissionModel] = Field(alias="Permissions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevocationConfigurationModel(BaseModel):
    crl_configuration: Optional[CrlConfigurationModel] = Field(
        default=None, alias="CrlConfiguration"
    )
    ocsp_configuration: Optional[OcspConfigurationModel] = Field(
        default=None, alias="OcspConfiguration"
    )


class PolicyQualifierInfoModel(BaseModel):
    policy_qualifier_id: Literal["CPS"] = Field(alias="PolicyQualifierId")
    qualifier: QualifierModel = Field(alias="Qualifier")


class GeneralNameModel(BaseModel):
    other_name: Optional[OtherNameModel] = Field(default=None, alias="OtherName")
    rfc822_name: Optional[str] = Field(default=None, alias="Rfc822Name")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    directory_name: Optional[ASN1SubjectModel] = Field(
        default=None, alias="DirectoryName"
    )
    edi_party_name: Optional[EdiPartyNameModel] = Field(
        default=None, alias="EdiPartyName"
    )
    uniform_resource_identifier: Optional[str] = Field(
        default=None, alias="UniformResourceIdentifier"
    )
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    registered_id: Optional[str] = Field(default=None, alias="RegisteredId")


class UpdateCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    revocation_configuration: Optional[RevocationConfigurationModel] = Field(
        default=None, alias="RevocationConfiguration"
    )
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "DELETED",
            "DISABLED",
            "EXPIRED",
            "FAILED",
            "PENDING_CERTIFICATE",
        ]
    ] = Field(default=None, alias="Status")


class PolicyInformationModel(BaseModel):
    cert_policy_id: str = Field(alias="CertPolicyId")
    policy_qualifiers: Optional[Sequence[PolicyQualifierInfoModel]] = Field(
        default=None, alias="PolicyQualifiers"
    )


class AccessDescriptionModel(BaseModel):
    access_method: AccessMethodModel = Field(alias="AccessMethod")
    access_location: GeneralNameModel = Field(alias="AccessLocation")


class ExtensionsModel(BaseModel):
    certificate_policies: Optional[Sequence[PolicyInformationModel]] = Field(
        default=None, alias="CertificatePolicies"
    )
    extended_key_usage: Optional[Sequence[ExtendedKeyUsageModel]] = Field(
        default=None, alias="ExtendedKeyUsage"
    )
    key_usage: Optional[KeyUsageModel] = Field(default=None, alias="KeyUsage")
    subject_alternative_names: Optional[Sequence[GeneralNameModel]] = Field(
        default=None, alias="SubjectAlternativeNames"
    )
    custom_extensions: Optional[Sequence[CustomExtensionModel]] = Field(
        default=None, alias="CustomExtensions"
    )


class CsrExtensionsModel(BaseModel):
    key_usage: Optional[KeyUsageModel] = Field(default=None, alias="KeyUsage")
    subject_information_access: Optional[Sequence[AccessDescriptionModel]] = Field(
        default=None, alias="SubjectInformationAccess"
    )


class ApiPassthroughModel(BaseModel):
    extensions: Optional[ExtensionsModel] = Field(default=None, alias="Extensions")
    subject: Optional[ASN1SubjectModel] = Field(default=None, alias="Subject")


class CertificateAuthorityConfigurationModel(BaseModel):
    key_algorithm: Literal[
        "EC_prime256v1", "EC_secp384r1", "RSA_2048", "RSA_4096"
    ] = Field(alias="KeyAlgorithm")
    signing_algorithm: Literal[
        "SHA256WITHECDSA",
        "SHA256WITHRSA",
        "SHA384WITHECDSA",
        "SHA384WITHRSA",
        "SHA512WITHECDSA",
        "SHA512WITHRSA",
    ] = Field(alias="SigningAlgorithm")
    subject: ASN1SubjectModel = Field(alias="Subject")
    csr_extensions: Optional[CsrExtensionsModel] = Field(
        default=None, alias="CsrExtensions"
    )


class IssueCertificateRequestModel(BaseModel):
    certificate_authority_arn: str = Field(alias="CertificateAuthorityArn")
    csr: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Csr")
    signing_algorithm: Literal[
        "SHA256WITHECDSA",
        "SHA256WITHRSA",
        "SHA384WITHECDSA",
        "SHA384WITHRSA",
        "SHA512WITHECDSA",
        "SHA512WITHRSA",
    ] = Field(alias="SigningAlgorithm")
    validity: ValidityModel = Field(alias="Validity")
    api_passthrough: Optional[ApiPassthroughModel] = Field(
        default=None, alias="ApiPassthrough"
    )
    template_arn: Optional[str] = Field(default=None, alias="TemplateArn")
    validity_not_before: Optional[ValidityModel] = Field(
        default=None, alias="ValidityNotBefore"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")


class CertificateAuthorityModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    owner_account: Optional[str] = Field(default=None, alias="OwnerAccount")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_state_change_at: Optional[datetime] = Field(
        default=None, alias="LastStateChangeAt"
    )
    type: Optional[Literal["ROOT", "SUBORDINATE"]] = Field(default=None, alias="Type")
    serial: Optional[str] = Field(default=None, alias="Serial")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "DELETED",
            "DISABLED",
            "EXPIRED",
            "FAILED",
            "PENDING_CERTIFICATE",
        ]
    ] = Field(default=None, alias="Status")
    not_before: Optional[datetime] = Field(default=None, alias="NotBefore")
    not_after: Optional[datetime] = Field(default=None, alias="NotAfter")
    failure_reason: Optional[
        Literal["OTHER", "REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM"]
    ] = Field(default=None, alias="FailureReason")
    certificate_authority_configuration: Optional[
        CertificateAuthorityConfigurationModel
    ] = Field(default=None, alias="CertificateAuthorityConfiguration")
    revocation_configuration: Optional[RevocationConfigurationModel] = Field(
        default=None, alias="RevocationConfiguration"
    )
    restorable_until: Optional[datetime] = Field(default=None, alias="RestorableUntil")
    key_storage_security_standard: Optional[
        Literal["FIPS_140_2_LEVEL_2_OR_HIGHER", "FIPS_140_2_LEVEL_3_OR_HIGHER"]
    ] = Field(default=None, alias="KeyStorageSecurityStandard")
    usage_mode: Optional[Literal["GENERAL_PURPOSE", "SHORT_LIVED_CERTIFICATE"]] = Field(
        default=None, alias="UsageMode"
    )


class CreateCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_configuration: CertificateAuthorityConfigurationModel = Field(
        alias="CertificateAuthorityConfiguration"
    )
    certificate_authority_type: Literal["ROOT", "SUBORDINATE"] = Field(
        alias="CertificateAuthorityType"
    )
    revocation_configuration: Optional[RevocationConfigurationModel] = Field(
        default=None, alias="RevocationConfiguration"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    key_storage_security_standard: Optional[
        Literal["FIPS_140_2_LEVEL_2_OR_HIGHER", "FIPS_140_2_LEVEL_3_OR_HIGHER"]
    ] = Field(default=None, alias="KeyStorageSecurityStandard")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    usage_mode: Optional[Literal["GENERAL_PURPOSE", "SHORT_LIVED_CERTIFICATE"]] = Field(
        default=None, alias="UsageMode"
    )


class DescribeCertificateAuthorityResponseModel(BaseModel):
    certificate_authority: CertificateAuthorityModel = Field(
        alias="CertificateAuthority"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCertificateAuthoritiesResponseModel(BaseModel):
    certificate_authorities: List[CertificateAuthorityModel] = Field(
        alias="CertificateAuthorities"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
