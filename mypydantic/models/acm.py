# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CertificateOptionsModel(BaseModel):
    certificate_transparency_logging_preference: Optional[
        Literal["DISABLED", "ENABLED"]
    ] = Field(default=None, alias="CertificateTransparencyLoggingPreference")


class ExtendedKeyUsageModel(BaseModel):
    name: Optional[
        Literal[
            "ANY",
            "CODE_SIGNING",
            "CUSTOM",
            "EMAIL_PROTECTION",
            "IPSEC_END_SYSTEM",
            "IPSEC_TUNNEL",
            "IPSEC_USER",
            "NONE",
            "OCSP_SIGNING",
            "TIME_STAMPING",
            "TLS_WEB_CLIENT_AUTHENTICATION",
            "TLS_WEB_SERVER_AUTHENTICATION",
        ]
    ] = Field(default=None, alias="Name")
    oid: Optional[str] = Field(default=None, alias="OID")


class KeyUsageModel(BaseModel):
    name: Optional[
        Literal[
            "ANY",
            "CERTIFICATE_SIGNING",
            "CRL_SIGNING",
            "CUSTOM",
            "DATA_ENCIPHERMENT",
            "DECIPHER_ONLY",
            "DIGITAL_SIGNATURE",
            "ENCIPHER_ONLY",
            "KEY_AGREEMENT",
            "KEY_ENCIPHERMENT",
            "NON_REPUDIATION",
        ]
    ] = Field(default=None, alias="Name")


class CertificateSummaryModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    subject_alternative_name_summaries: Optional[List[str]] = Field(
        default=None, alias="SubjectAlternativeNameSummaries"
    )
    has_additional_subject_alternative_names: Optional[bool] = Field(
        default=None, alias="HasAdditionalSubjectAlternativeNames"
    )
    status: Optional[
        Literal[
            "EXPIRED",
            "FAILED",
            "INACTIVE",
            "ISSUED",
            "PENDING_VALIDATION",
            "REVOKED",
            "VALIDATION_TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    type: Optional[Literal["AMAZON_ISSUED", "IMPORTED", "PRIVATE"]] = Field(
        default=None, alias="Type"
    )
    key_algorithm: Optional[
        Literal[
            "EC_prime256v1",
            "EC_secp384r1",
            "EC_secp521r1",
            "RSA_1024",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
        ]
    ] = Field(default=None, alias="KeyAlgorithm")
    key_usages: Optional[
        List[
            Literal[
                "ANY",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "CUSTOM",
                "DATA_ENCIPHERMENT",
                "DECIPHER_ONLY",
                "DIGITAL_SIGNATURE",
                "ENCIPHER_ONLY",
                "KEY_AGREEMENT",
                "KEY_ENCIPHERMENT",
                "NON_REPUDIATION",
            ]
        ]
    ] = Field(default=None, alias="KeyUsages")
    extended_key_usages: Optional[
        List[
            Literal[
                "ANY",
                "CODE_SIGNING",
                "CUSTOM",
                "EMAIL_PROTECTION",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "NONE",
                "OCSP_SIGNING",
                "TIME_STAMPING",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "TLS_WEB_SERVER_AUTHENTICATION",
            ]
        ]
    ] = Field(default=None, alias="ExtendedKeyUsages")
    in_use: Optional[bool] = Field(default=None, alias="InUse")
    exported: Optional[bool] = Field(default=None, alias="Exported")
    renewal_eligibility: Optional[Literal["ELIGIBLE", "INELIGIBLE"]] = Field(
        default=None, alias="RenewalEligibility"
    )
    not_before: Optional[datetime] = Field(default=None, alias="NotBefore")
    not_after: Optional[datetime] = Field(default=None, alias="NotAfter")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    issued_at: Optional[datetime] = Field(default=None, alias="IssuedAt")
    imported_at: Optional[datetime] = Field(default=None, alias="ImportedAt")
    revoked_at: Optional[datetime] = Field(default=None, alias="RevokedAt")


class DeleteCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DomainValidationOptionModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    validation_domain: str = Field(alias="ValidationDomain")


class ResourceRecordModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["CNAME"] = Field(alias="Type")
    value: str = Field(alias="Value")


class ExpiryEventsConfigurationModel(BaseModel):
    days_before_expiry: Optional[int] = Field(default=None, alias="DaysBeforeExpiry")


class ExportCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    passphrase: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Passphrase"
    )


class FiltersModel(BaseModel):
    extended_key_usage: Optional[
        Sequence[
            Literal[
                "ANY",
                "CODE_SIGNING",
                "CUSTOM",
                "EMAIL_PROTECTION",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "NONE",
                "OCSP_SIGNING",
                "TIME_STAMPING",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "TLS_WEB_SERVER_AUTHENTICATION",
            ]
        ]
    ] = Field(default=None, alias="extendedKeyUsage")
    key_usage: Optional[
        Sequence[
            Literal[
                "ANY",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "CUSTOM",
                "DATA_ENCIPHERMENT",
                "DECIPHER_ONLY",
                "DIGITAL_SIGNATURE",
                "ENCIPHER_ONLY",
                "KEY_AGREEMENT",
                "KEY_ENCIPHERMENT",
                "NON_REPUDIATION",
            ]
        ]
    ] = Field(default=None, alias="keyUsage")
    key_types: Optional[
        Sequence[
            Literal[
                "EC_prime256v1",
                "EC_secp384r1",
                "EC_secp521r1",
                "RSA_1024",
                "RSA_2048",
                "RSA_3072",
                "RSA_4096",
            ]
        ]
    ] = Field(default=None, alias="keyTypes")


class GetCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListTagsForCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class RenewCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")


class ResendValidationEmailRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    domain: str = Field(alias="Domain")
    validation_domain: str = Field(alias="ValidationDomain")


class AddTagsToCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ImportCertificateRequestModel(BaseModel):
    certificate: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Certificate"
    )
    private_key: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="PrivateKey"
    )
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    certificate_chain: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="CertificateChain")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class RemoveTagsFromCertificateRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class UpdateCertificateOptionsRequestModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    options: CertificateOptionsModel = Field(alias="Options")


class DescribeCertificateRequestCertificateValidatedWaitModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportCertificateResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    certificate_chain: str = Field(alias="CertificateChain")
    private_key: str = Field(alias="PrivateKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCertificateResponseModel(BaseModel):
    certificate: str = Field(alias="Certificate")
    certificate_chain: str = Field(alias="CertificateChain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportCertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCertificatesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    certificate_summary_list: List[CertificateSummaryModel] = Field(
        alias="CertificateSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForCertificateResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestCertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestCertificateRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    validation_method: Optional[Literal["DNS", "EMAIL"]] = Field(
        default=None, alias="ValidationMethod"
    )
    subject_alternative_names: Optional[Sequence[str]] = Field(
        default=None, alias="SubjectAlternativeNames"
    )
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    domain_validation_options: Optional[Sequence[DomainValidationOptionModel]] = Field(
        default=None, alias="DomainValidationOptions"
    )
    options: Optional[CertificateOptionsModel] = Field(default=None, alias="Options")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    key_algorithm: Optional[
        Literal[
            "EC_prime256v1",
            "EC_secp384r1",
            "EC_secp521r1",
            "RSA_1024",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
        ]
    ] = Field(default=None, alias="KeyAlgorithm")


class DomainValidationModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    validation_emails: Optional[List[str]] = Field(
        default=None, alias="ValidationEmails"
    )
    validation_domain: Optional[str] = Field(default=None, alias="ValidationDomain")
    validation_status: Optional[
        Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
    ] = Field(default=None, alias="ValidationStatus")
    resource_record: Optional[ResourceRecordModel] = Field(
        default=None, alias="ResourceRecord"
    )
    validation_method: Optional[Literal["DNS", "EMAIL"]] = Field(
        default=None, alias="ValidationMethod"
    )


class GetAccountConfigurationResponseModel(BaseModel):
    expiry_events: ExpiryEventsConfigurationModel = Field(alias="ExpiryEvents")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAccountConfigurationRequestModel(BaseModel):
    idempotency_token: str = Field(alias="IdempotencyToken")
    expiry_events: Optional[ExpiryEventsConfigurationModel] = Field(
        default=None, alias="ExpiryEvents"
    )


class ListCertificatesRequestModel(BaseModel):
    certificate_statuses: Optional[
        Sequence[
            Literal[
                "EXPIRED",
                "FAILED",
                "INACTIVE",
                "ISSUED",
                "PENDING_VALIDATION",
                "REVOKED",
                "VALIDATION_TIMED_OUT",
            ]
        ]
    ] = Field(default=None, alias="CertificateStatuses")
    includes: Optional[FiltersModel] = Field(default=None, alias="Includes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    sort_by: Optional[Literal["CREATED_AT"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class ListCertificatesRequestListCertificatesPaginateModel(BaseModel):
    certificate_statuses: Optional[
        Sequence[
            Literal[
                "EXPIRED",
                "FAILED",
                "INACTIVE",
                "ISSUED",
                "PENDING_VALIDATION",
                "REVOKED",
                "VALIDATION_TIMED_OUT",
            ]
        ]
    ] = Field(default=None, alias="CertificateStatuses")
    includes: Optional[FiltersModel] = Field(default=None, alias="Includes")
    sort_by: Optional[Literal["CREATED_AT"]] = Field(default=None, alias="SortBy")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RenewalSummaryModel(BaseModel):
    renewal_status: Literal[
        "FAILED", "PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS"
    ] = Field(alias="RenewalStatus")
    domain_validation_options: List[DomainValidationModel] = Field(
        alias="DomainValidationOptions"
    )
    updated_at: datetime = Field(alias="UpdatedAt")
    renewal_status_reason: Optional[
        Literal[
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "CAA_ERROR",
            "DOMAIN_NOT_ALLOWED",
            "DOMAIN_VALIDATION_DENIED",
            "INVALID_PUBLIC_DOMAIN",
            "NO_AVAILABLE_CONTACTS",
            "OTHER",
            "PCA_ACCESS_DENIED",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_ARN",
            "PCA_INVALID_DURATION",
            "PCA_INVALID_STATE",
            "PCA_LIMIT_EXCEEDED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_REQUEST_FAILED",
            "PCA_RESOURCE_NOT_FOUND",
            "SLR_NOT_FOUND",
        ]
    ] = Field(default=None, alias="RenewalStatusReason")


class CertificateDetailModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    subject_alternative_names: Optional[List[str]] = Field(
        default=None, alias="SubjectAlternativeNames"
    )
    domain_validation_options: Optional[List[DomainValidationModel]] = Field(
        default=None, alias="DomainValidationOptions"
    )
    serial: Optional[str] = Field(default=None, alias="Serial")
    subject: Optional[str] = Field(default=None, alias="Subject")
    issuer: Optional[str] = Field(default=None, alias="Issuer")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    issued_at: Optional[datetime] = Field(default=None, alias="IssuedAt")
    imported_at: Optional[datetime] = Field(default=None, alias="ImportedAt")
    status: Optional[
        Literal[
            "EXPIRED",
            "FAILED",
            "INACTIVE",
            "ISSUED",
            "PENDING_VALIDATION",
            "REVOKED",
            "VALIDATION_TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    revoked_at: Optional[datetime] = Field(default=None, alias="RevokedAt")
    revocation_reason: Optional[
        Literal[
            "AFFILIATION_CHANGED",
            "A_A_COMPROMISE",
            "CA_COMPROMISE",
            "CERTIFICATE_HOLD",
            "CESSATION_OF_OPERATION",
            "KEY_COMPROMISE",
            "PRIVILEGE_WITHDRAWN",
            "REMOVE_FROM_CRL",
            "SUPERCEDED",
            "UNSPECIFIED",
        ]
    ] = Field(default=None, alias="RevocationReason")
    not_before: Optional[datetime] = Field(default=None, alias="NotBefore")
    not_after: Optional[datetime] = Field(default=None, alias="NotAfter")
    key_algorithm: Optional[
        Literal[
            "EC_prime256v1",
            "EC_secp384r1",
            "EC_secp521r1",
            "RSA_1024",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
        ]
    ] = Field(default=None, alias="KeyAlgorithm")
    signature_algorithm: Optional[str] = Field(default=None, alias="SignatureAlgorithm")
    in_use_by: Optional[List[str]] = Field(default=None, alias="InUseBy")
    failure_reason: Optional[
        Literal[
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "CAA_ERROR",
            "DOMAIN_NOT_ALLOWED",
            "DOMAIN_VALIDATION_DENIED",
            "INVALID_PUBLIC_DOMAIN",
            "NO_AVAILABLE_CONTACTS",
            "OTHER",
            "PCA_ACCESS_DENIED",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_ARN",
            "PCA_INVALID_DURATION",
            "PCA_INVALID_STATE",
            "PCA_LIMIT_EXCEEDED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_REQUEST_FAILED",
            "PCA_RESOURCE_NOT_FOUND",
            "SLR_NOT_FOUND",
        ]
    ] = Field(default=None, alias="FailureReason")
    type: Optional[Literal["AMAZON_ISSUED", "IMPORTED", "PRIVATE"]] = Field(
        default=None, alias="Type"
    )
    renewal_summary: Optional[RenewalSummaryModel] = Field(
        default=None, alias="RenewalSummary"
    )
    key_usages: Optional[List[KeyUsageModel]] = Field(default=None, alias="KeyUsages")
    extended_key_usages: Optional[List[ExtendedKeyUsageModel]] = Field(
        default=None, alias="ExtendedKeyUsages"
    )
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    renewal_eligibility: Optional[Literal["ELIGIBLE", "INELIGIBLE"]] = Field(
        default=None, alias="RenewalEligibility"
    )
    options: Optional[CertificateOptionsModel] = Field(default=None, alias="Options")


class DescribeCertificateResponseModel(BaseModel):
    certificate: CertificateDetailModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
