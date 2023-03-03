# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptGrantRequestModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AutomatedDiscoveryInformationModel(BaseModel):
    last_run_time: Optional[datetime] = Field(default=None, alias="LastRunTime")


class BorrowConfigurationModel(BaseModel):
    allow_early_check_in: bool = Field(alias="AllowEarlyCheckIn")
    max_time_to_live_in_minutes: int = Field(alias="MaxTimeToLiveInMinutes")


class CheckInLicenseRequestModel(BaseModel):
    license_consumption_token: str = Field(alias="LicenseConsumptionToken")
    beneficiary: Optional[str] = Field(default=None, alias="Beneficiary")


class EntitlementDataModel(BaseModel):
    name: str = Field(alias="Name")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="Unit")
    value: Optional[str] = Field(default=None, alias="Value")


class MetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class ConsumedLicenseSummaryModel(BaseModel):
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    consumed_licenses: Optional[int] = Field(default=None, alias="ConsumedLicenses")


class ProvisionalConfigurationModel(BaseModel):
    max_time_to_live_in_minutes: int = Field(alias="MaxTimeToLiveInMinutes")


class CreateGrantRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    grant_name: str = Field(alias="GrantName")
    license_arn: str = Field(alias="LicenseArn")
    principals: Sequence[str] = Field(alias="Principals")
    home_region: str = Field(alias="HomeRegion")
    allowed_operations: Sequence[
        Literal[
            "CheckInLicense",
            "CheckoutBorrowLicense",
            "CheckoutLicense",
            "CreateGrant",
            "CreateToken",
            "ExtendConsumptionLicense",
            "ListPurchasedLicenses",
        ]
    ] = Field(alias="AllowedOperations")


class CreateGrantVersionRequestModel(BaseModel):
    client_token: str = Field(alias="ClientToken")
    grant_arn: str = Field(alias="GrantArn")
    grant_name: Optional[str] = Field(default=None, alias="GrantName")
    allowed_operations: Optional[
        Sequence[
            Literal[
                "CheckInLicense",
                "CheckoutBorrowLicense",
                "CheckoutLicense",
                "CreateGrant",
                "CreateToken",
                "ExtendConsumptionLicense",
                "ListPurchasedLicenses",
            ]
        ]
    ] = Field(default=None, alias="AllowedOperations")
    status: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DISABLED",
            "FAILED_WORKFLOW",
            "PENDING_ACCEPT",
            "PENDING_DELETE",
            "PENDING_WORKFLOW",
            "REJECTED",
            "WORKFLOW_COMPLETED",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    source_version: Optional[str] = Field(default=None, alias="SourceVersion")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class LicenseConversionContextModel(BaseModel):
    usage_operation: Optional[str] = Field(default=None, alias="UsageOperation")


class ReportContextModel(BaseModel):
    license_configuration_arns: Sequence[str] = Field(alias="licenseConfigurationArns")


class ReportFrequencyModel(BaseModel):
    value: Optional[int] = Field(default=None, alias="value")
    period: Optional[Literal["DAY", "MONTH", "WEEK"]] = Field(
        default=None, alias="period"
    )


class DatetimeRangeModel(BaseModel):
    begin: str = Field(alias="Begin")
    end: Optional[str] = Field(default=None, alias="End")


class EntitlementModel(BaseModel):
    name: str = Field(alias="Name")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="Unit")
    value: Optional[str] = Field(default=None, alias="Value")
    max_count: Optional[int] = Field(default=None, alias="MaxCount")
    overage: Optional[bool] = Field(default=None, alias="Overage")
    allow_check_in: Optional[bool] = Field(default=None, alias="AllowCheckIn")


class IssuerModel(BaseModel):
    name: str = Field(alias="Name")
    sign_key: Optional[str] = Field(default=None, alias="SignKey")


class CreateTokenRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    client_token: str = Field(alias="ClientToken")
    role_arns: Optional[Sequence[str]] = Field(default=None, alias="RoleArns")
    expiration_in_days: Optional[int] = Field(default=None, alias="ExpirationInDays")
    token_properties: Optional[Sequence[str]] = Field(
        default=None, alias="TokenProperties"
    )


class DeleteGrantRequestModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    version: str = Field(alias="Version")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")


class DeleteLicenseConfigurationRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")


class DeleteLicenseManagerReportGeneratorRequestModel(BaseModel):
    license_manager_report_generator_arn: str = Field(
        alias="LicenseManagerReportGeneratorArn"
    )


class DeleteLicenseRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    source_version: str = Field(alias="SourceVersion")


class DeleteTokenRequestModel(BaseModel):
    token_id: str = Field(alias="TokenId")


class EntitlementUsageModel(BaseModel):
    name: str = Field(alias="Name")
    consumed_value: str = Field(alias="ConsumedValue")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="Unit")
    max_count: Optional[str] = Field(default=None, alias="MaxCount")


class ExtendLicenseConsumptionRequestModel(BaseModel):
    license_consumption_token: str = Field(alias="LicenseConsumptionToken")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class GetAccessTokenRequestModel(BaseModel):
    token: str = Field(alias="Token")
    token_properties: Optional[Sequence[str]] = Field(
        default=None, alias="TokenProperties"
    )


class GetGrantRequestModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    version: Optional[str] = Field(default=None, alias="Version")


class GrantModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    grant_name: str = Field(alias="GrantName")
    parent_arn: str = Field(alias="ParentArn")
    license_arn: str = Field(alias="LicenseArn")
    grantee_principal_arn: str = Field(alias="GranteePrincipalArn")
    home_region: str = Field(alias="HomeRegion")
    grant_status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="GrantStatus")
    version: str = Field(alias="Version")
    granted_operations: List[
        Literal[
            "CheckInLicense",
            "CheckoutBorrowLicense",
            "CheckoutLicense",
            "CreateGrant",
            "CreateToken",
            "ExtendConsumptionLicense",
            "ListPurchasedLicenses",
        ]
    ] = Field(alias="GrantedOperations")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")


class GetLicenseConfigurationRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")


class ManagedResourceSummaryModel(BaseModel):
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    association_count: Optional[int] = Field(default=None, alias="AssociationCount")


class GetLicenseConversionTaskRequestModel(BaseModel):
    license_conversion_task_id: str = Field(alias="LicenseConversionTaskId")


class GetLicenseManagerReportGeneratorRequestModel(BaseModel):
    license_manager_report_generator_arn: str = Field(
        alias="LicenseManagerReportGeneratorArn"
    )


class GetLicenseRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    version: Optional[str] = Field(default=None, alias="Version")


class GetLicenseUsageRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")


class OrganizationConfigurationModel(BaseModel):
    enable_integration: bool = Field(alias="EnableIntegration")


class IssuerDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    sign_key: Optional[str] = Field(default=None, alias="SignKey")
    key_fingerprint: Optional[str] = Field(default=None, alias="KeyFingerprint")


class ReceivedMetadataModel(BaseModel):
    received_status: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DISABLED",
            "FAILED_WORKFLOW",
            "PENDING_ACCEPT",
            "PENDING_WORKFLOW",
            "REJECTED",
            "WORKFLOW_COMPLETED",
        ]
    ] = Field(default=None, alias="ReceivedStatus")
    received_status_reason: Optional[str] = Field(
        default=None, alias="ReceivedStatusReason"
    )
    allowed_operations: Optional[
        List[
            Literal[
                "CheckInLicense",
                "CheckoutBorrowLicense",
                "CheckoutLicense",
                "CreateGrant",
                "CreateToken",
                "ExtendConsumptionLicense",
                "ListPurchasedLicenses",
            ]
        ]
    ] = Field(default=None, alias="AllowedOperations")


class InventoryFilterModel(BaseModel):
    name: str = Field(alias="Name")
    condition: Literal["BEGINS_WITH", "CONTAINS", "EQUALS", "NOT_EQUALS"] = Field(
        alias="Condition"
    )
    value: Optional[str] = Field(default=None, alias="Value")


class LicenseConfigurationAssociationModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    resource_owner_id: Optional[str] = Field(default=None, alias="ResourceOwnerId")
    association_time: Optional[datetime] = Field(default=None, alias="AssociationTime")
    ami_association_scope: Optional[str] = Field(
        default=None, alias="AmiAssociationScope"
    )


class LicenseConfigurationUsageModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    resource_status: Optional[str] = Field(default=None, alias="ResourceStatus")
    resource_owner_id: Optional[str] = Field(default=None, alias="ResourceOwnerId")
    association_time: Optional[datetime] = Field(default=None, alias="AssociationTime")
    consumed_licenses: Optional[int] = Field(default=None, alias="ConsumedLicenses")


class LicenseSpecificationModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    ami_association_scope: Optional[str] = Field(
        default=None, alias="AmiAssociationScope"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAssociationsForLicenseConfigurationRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFailuresForLicenseConfigurationOperationsRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLicenseSpecificationsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLicenseVersionsRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ResourceInventoryModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    platform: Optional[str] = Field(default=None, alias="Platform")
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    resource_owning_account_id: Optional[str] = Field(
        default=None, alias="ResourceOwningAccountId"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TokenDataModel(BaseModel):
    token_id: Optional[str] = Field(default=None, alias="TokenId")
    token_type: Optional[str] = Field(default=None, alias="TokenType")
    license_arn: Optional[str] = Field(default=None, alias="LicenseArn")
    expiration_time: Optional[str] = Field(default=None, alias="ExpirationTime")
    token_properties: Optional[List[str]] = Field(default=None, alias="TokenProperties")
    role_arns: Optional[List[str]] = Field(default=None, alias="RoleArns")
    status: Optional[str] = Field(default=None, alias="Status")


class ProductInformationFilterModel(BaseModel):
    product_information_filter_name: str = Field(alias="ProductInformationFilterName")
    product_information_filter_comparator: str = Field(
        alias="ProductInformationFilterComparator"
    )
    product_information_filter_value: Optional[Sequence[str]] = Field(
        default=None, alias="ProductInformationFilterValue"
    )


class RejectGrantRequestModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AcceptGrantResponseModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGrantResponseModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGrantVersionResponseModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseConfigurationResponseModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseConversionTaskForResourceResponseModel(BaseModel):
    license_conversion_task_id: str = Field(alias="LicenseConversionTaskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseManagerReportGeneratorResponseModel(BaseModel):
    license_manager_report_generator_arn: str = Field(
        alias="LicenseManagerReportGeneratorArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseResponseModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    status: Literal[
        "AVAILABLE",
        "DEACTIVATED",
        "DELETED",
        "EXPIRED",
        "PENDING_AVAILABLE",
        "PENDING_DELETE",
        "SUSPENDED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseVersionResponseModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    version: str = Field(alias="Version")
    status: Literal[
        "AVAILABLE",
        "DEACTIVATED",
        "DELETED",
        "EXPIRED",
        "PENDING_AVAILABLE",
        "PENDING_DELETE",
        "SUSPENDED",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTokenResponseModel(BaseModel):
    token_id: str = Field(alias="TokenId")
    token_type: Literal["REFRESH_TOKEN"] = Field(alias="TokenType")
    token: str = Field(alias="Token")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGrantResponseModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLicenseResponseModel(BaseModel):
    status: Literal["DELETED", "PENDING_DELETE"] = Field(alias="Status")
    deletion_date: str = Field(alias="DeletionDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExtendLicenseConsumptionResponseModel(BaseModel):
    license_consumption_token: str = Field(alias="LicenseConsumptionToken")
    expiration: str = Field(alias="Expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessTokenResponseModel(BaseModel):
    access_token: str = Field(alias="AccessToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectGrantResponseModel(BaseModel):
    grant_arn: str = Field(alias="GrantArn")
    status: Literal[
        "ACTIVE",
        "DELETED",
        "DISABLED",
        "FAILED_WORKFLOW",
        "PENDING_ACCEPT",
        "PENDING_DELETE",
        "PENDING_WORKFLOW",
        "REJECTED",
        "WORKFLOW_COMPLETED",
    ] = Field(alias="Status")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckoutLicenseRequestModel(BaseModel):
    product_s_ku: str = Field(alias="ProductSKU")
    checkout_type: Literal["PERPETUAL", "PROVISIONAL"] = Field(alias="CheckoutType")
    key_fingerprint: str = Field(alias="KeyFingerprint")
    entitlements: Sequence[EntitlementDataModel] = Field(alias="Entitlements")
    client_token: str = Field(alias="ClientToken")
    beneficiary: Optional[str] = Field(default=None, alias="Beneficiary")
    node_id: Optional[str] = Field(default=None, alias="NodeId")


class CheckoutLicenseResponseModel(BaseModel):
    checkout_type: Literal["PERPETUAL", "PROVISIONAL"] = Field(alias="CheckoutType")
    license_consumption_token: str = Field(alias="LicenseConsumptionToken")
    entitlements_allowed: List[EntitlementDataModel] = Field(
        alias="EntitlementsAllowed"
    )
    signed_token: str = Field(alias="SignedToken")
    node_id: str = Field(alias="NodeId")
    issued_at: str = Field(alias="IssuedAt")
    expiration: str = Field(alias="Expiration")
    license_arn: str = Field(alias="LicenseArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckoutBorrowLicenseRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    entitlements: Sequence[EntitlementDataModel] = Field(alias="Entitlements")
    digital_signature_method: Literal["JWT_PS384"] = Field(
        alias="DigitalSignatureMethod"
    )
    client_token: str = Field(alias="ClientToken")
    node_id: Optional[str] = Field(default=None, alias="NodeId")
    checkout_metadata: Optional[Sequence[MetadataModel]] = Field(
        default=None, alias="CheckoutMetadata"
    )


class CheckoutBorrowLicenseResponseModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    license_consumption_token: str = Field(alias="LicenseConsumptionToken")
    entitlements_allowed: List[EntitlementDataModel] = Field(
        alias="EntitlementsAllowed"
    )
    node_id: str = Field(alias="NodeId")
    signed_token: str = Field(alias="SignedToken")
    issued_at: str = Field(alias="IssuedAt")
    expiration: str = Field(alias="Expiration")
    checkout_metadata: List[MetadataModel] = Field(alias="CheckoutMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LicenseOperationFailureModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[
        Literal[
            "EC2_AMI",
            "EC2_HOST",
            "EC2_INSTANCE",
            "RDS",
            "SYSTEMS_MANAGER_MANAGED_INSTANCE",
        ]
    ] = Field(default=None, alias="ResourceType")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    failure_time: Optional[datetime] = Field(default=None, alias="FailureTime")
    operation_name: Optional[str] = Field(default=None, alias="OperationName")
    resource_owner_id: Optional[str] = Field(default=None, alias="ResourceOwnerId")
    operation_requested_by: Optional[str] = Field(
        default=None, alias="OperationRequestedBy"
    )
    metadata_list: Optional[List[MetadataModel]] = Field(
        default=None, alias="MetadataList"
    )


class ConsumptionConfigurationModel(BaseModel):
    renew_type: Optional[Literal["Monthly", "None", "Weekly"]] = Field(
        default=None, alias="RenewType"
    )
    provisional_configuration: Optional[ProvisionalConfigurationModel] = Field(
        default=None, alias="ProvisionalConfiguration"
    )
    borrow_configuration: Optional[BorrowConfigurationModel] = Field(
        default=None, alias="BorrowConfiguration"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateLicenseConversionTaskForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    source_license_context: LicenseConversionContextModel = Field(
        alias="SourceLicenseContext"
    )
    destination_license_context: LicenseConversionContextModel = Field(
        alias="DestinationLicenseContext"
    )


class GetLicenseConversionTaskResponseModel(BaseModel):
    license_conversion_task_id: str = Field(alias="LicenseConversionTaskId")
    resource_arn: str = Field(alias="ResourceArn")
    source_license_context: LicenseConversionContextModel = Field(
        alias="SourceLicenseContext"
    )
    destination_license_context: LicenseConversionContextModel = Field(
        alias="DestinationLicenseContext"
    )
    status_message: str = Field(alias="StatusMessage")
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="Status")
    start_time: datetime = Field(alias="StartTime")
    license_conversion_time: datetime = Field(alias="LicenseConversionTime")
    end_time: datetime = Field(alias="EndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LicenseConversionTaskModel(BaseModel):
    license_conversion_task_id: Optional[str] = Field(
        default=None, alias="LicenseConversionTaskId"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    source_license_context: Optional[LicenseConversionContextModel] = Field(
        default=None, alias="SourceLicenseContext"
    )
    destination_license_context: Optional[LicenseConversionContextModel] = Field(
        default=None, alias="DestinationLicenseContext"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    license_conversion_time: Optional[datetime] = Field(
        default=None, alias="LicenseConversionTime"
    )
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class CreateLicenseManagerReportGeneratorRequestModel(BaseModel):
    report_generator_name: str = Field(alias="ReportGeneratorName")
    type: Sequence[
        Literal["LicenseConfigurationSummaryReport", "LicenseConfigurationUsageReport"]
    ] = Field(alias="Type")
    report_context: ReportContextModel = Field(alias="ReportContext")
    report_frequency: ReportFrequencyModel = Field(alias="ReportFrequency")
    client_token: str = Field(alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateLicenseManagerReportGeneratorRequestModel(BaseModel):
    license_manager_report_generator_arn: str = Field(
        alias="LicenseManagerReportGeneratorArn"
    )
    report_generator_name: str = Field(alias="ReportGeneratorName")
    type: Sequence[
        Literal["LicenseConfigurationSummaryReport", "LicenseConfigurationUsageReport"]
    ] = Field(alias="Type")
    report_context: ReportContextModel = Field(alias="ReportContext")
    report_frequency: ReportFrequencyModel = Field(alias="ReportFrequency")
    client_token: str = Field(alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")


class LicenseUsageModel(BaseModel):
    entitlement_usages: Optional[List[EntitlementUsageModel]] = Field(
        default=None, alias="EntitlementUsages"
    )


class ListDistributedGrantsRequestModel(BaseModel):
    grant_arns: Optional[Sequence[str]] = Field(default=None, alias="GrantArns")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLicenseConfigurationsRequestModel(BaseModel):
    license_configuration_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LicenseConfigurationArns"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListLicenseConversionTasksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListLicenseManagerReportGeneratorsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListLicensesRequestModel(BaseModel):
    license_arns: Optional[Sequence[str]] = Field(default=None, alias="LicenseArns")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReceivedGrantsForOrganizationRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReceivedGrantsRequestModel(BaseModel):
    grant_arns: Optional[Sequence[str]] = Field(default=None, alias="GrantArns")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReceivedLicensesForOrganizationRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListReceivedLicensesRequestModel(BaseModel):
    license_arns: Optional[Sequence[str]] = Field(default=None, alias="LicenseArns")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTokensRequestModel(BaseModel):
    token_ids: Optional[Sequence[str]] = Field(default=None, alias="TokenIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListUsageForLicenseConfigurationRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class GetGrantResponseModel(BaseModel):
    grant: GrantModel = Field(alias="Grant")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDistributedGrantsResponseModel(BaseModel):
    grants: List[GrantModel] = Field(alias="Grants")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReceivedGrantsForOrganizationResponseModel(BaseModel):
    grants: List[GrantModel] = Field(alias="Grants")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReceivedGrantsResponseModel(BaseModel):
    grants: List[GrantModel] = Field(alias="Grants")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceSettingsResponseModel(BaseModel):
    s3_bucket_arn: str = Field(alias="S3BucketArn")
    sns_topic_arn: str = Field(alias="SnsTopicArn")
    organization_configuration: OrganizationConfigurationModel = Field(
        alias="OrganizationConfiguration"
    )
    enable_cross_accounts_discovery: bool = Field(alias="EnableCrossAccountsDiscovery")
    license_manager_resource_share_arn: str = Field(
        alias="LicenseManagerResourceShareArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceSettingsRequestModel(BaseModel):
    s3_bucket_arn: Optional[str] = Field(default=None, alias="S3BucketArn")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    organization_configuration: Optional[OrganizationConfigurationModel] = Field(
        default=None, alias="OrganizationConfiguration"
    )
    enable_cross_accounts_discovery: Optional[bool] = Field(
        default=None, alias="EnableCrossAccountsDiscovery"
    )


class ListResourceInventoryRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[InventoryFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ListAssociationsForLicenseConfigurationResponseModel(BaseModel):
    license_configuration_associations: List[
        LicenseConfigurationAssociationModel
    ] = Field(alias="LicenseConfigurationAssociations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsageForLicenseConfigurationResponseModel(BaseModel):
    license_configuration_usage_list: List[LicenseConfigurationUsageModel] = Field(
        alias="LicenseConfigurationUsageList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLicenseSpecificationsForResourceResponseModel(BaseModel):
    license_specifications: List[LicenseSpecificationModel] = Field(
        alias="LicenseSpecifications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLicenseSpecificationsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    add_license_specifications: Optional[Sequence[LicenseSpecificationModel]] = Field(
        default=None, alias="AddLicenseSpecifications"
    )
    remove_license_specifications: Optional[
        Sequence[LicenseSpecificationModel]
    ] = Field(default=None, alias="RemoveLicenseSpecifications")


class ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateModel(
    BaseModel
):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateModel(BaseModel):
    license_configuration_arns: Optional[Sequence[str]] = Field(
        default=None, alias="LicenseConfigurationArns"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateModel(
    BaseModel
):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceInventoryRequestListResourceInventoryPaginateModel(BaseModel):
    filters: Optional[Sequence[InventoryFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateModel(
    BaseModel
):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceInventoryResponseModel(BaseModel):
    resource_inventory_list: List[ResourceInventoryModel] = Field(
        alias="ResourceInventoryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTokensResponseModel(BaseModel):
    tokens: List[TokenDataModel] = Field(alias="Tokens")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProductInformationModel(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    product_information_filter_list: Sequence[ProductInformationFilterModel] = Field(
        alias="ProductInformationFilterList"
    )


class ReportGeneratorModel(BaseModel):
    report_generator_name: Optional[str] = Field(
        default=None, alias="ReportGeneratorName"
    )
    report_type: Optional[
        List[
            Literal[
                "LicenseConfigurationSummaryReport", "LicenseConfigurationUsageReport"
            ]
        ]
    ] = Field(default=None, alias="ReportType")
    report_context: Optional[ReportContextModel] = Field(
        default=None, alias="ReportContext"
    )
    report_frequency: Optional[ReportFrequencyModel] = Field(
        default=None, alias="ReportFrequency"
    )
    license_manager_report_generator_arn: Optional[str] = Field(
        default=None, alias="LicenseManagerReportGeneratorArn"
    )
    last_run_status: Optional[str] = Field(default=None, alias="LastRunStatus")
    last_run_failure_reason: Optional[str] = Field(
        default=None, alias="LastRunFailureReason"
    )
    last_report_generation_time: Optional[str] = Field(
        default=None, alias="LastReportGenerationTime"
    )
    report_creator_account: Optional[str] = Field(
        default=None, alias="ReportCreatorAccount"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="S3Location")
    create_time: Optional[str] = Field(default=None, alias="CreateTime")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListFailuresForLicenseConfigurationOperationsResponseModel(BaseModel):
    license_operation_failure_list: List[LicenseOperationFailureModel] = Field(
        alias="LicenseOperationFailureList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseRequestModel(BaseModel):
    license_name: str = Field(alias="LicenseName")
    product_name: str = Field(alias="ProductName")
    product_s_ku: str = Field(alias="ProductSKU")
    issuer: IssuerModel = Field(alias="Issuer")
    home_region: str = Field(alias="HomeRegion")
    validity: DatetimeRangeModel = Field(alias="Validity")
    entitlements: Sequence[EntitlementModel] = Field(alias="Entitlements")
    beneficiary: str = Field(alias="Beneficiary")
    consumption_configuration: ConsumptionConfigurationModel = Field(
        alias="ConsumptionConfiguration"
    )
    client_token: str = Field(alias="ClientToken")
    license_metadata: Optional[Sequence[MetadataModel]] = Field(
        default=None, alias="LicenseMetadata"
    )


class CreateLicenseVersionRequestModel(BaseModel):
    license_arn: str = Field(alias="LicenseArn")
    license_name: str = Field(alias="LicenseName")
    product_name: str = Field(alias="ProductName")
    issuer: IssuerModel = Field(alias="Issuer")
    home_region: str = Field(alias="HomeRegion")
    validity: DatetimeRangeModel = Field(alias="Validity")
    entitlements: Sequence[EntitlementModel] = Field(alias="Entitlements")
    consumption_configuration: ConsumptionConfigurationModel = Field(
        alias="ConsumptionConfiguration"
    )
    status: Literal[
        "AVAILABLE",
        "DEACTIVATED",
        "DELETED",
        "EXPIRED",
        "PENDING_AVAILABLE",
        "PENDING_DELETE",
        "SUSPENDED",
    ] = Field(alias="Status")
    client_token: str = Field(alias="ClientToken")
    license_metadata: Optional[Sequence[MetadataModel]] = Field(
        default=None, alias="LicenseMetadata"
    )
    source_version: Optional[str] = Field(default=None, alias="SourceVersion")


class GrantedLicenseModel(BaseModel):
    license_arn: Optional[str] = Field(default=None, alias="LicenseArn")
    license_name: Optional[str] = Field(default=None, alias="LicenseName")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    product_s_ku: Optional[str] = Field(default=None, alias="ProductSKU")
    issuer: Optional[IssuerDetailsModel] = Field(default=None, alias="Issuer")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    status: Optional[
        Literal[
            "AVAILABLE",
            "DEACTIVATED",
            "DELETED",
            "EXPIRED",
            "PENDING_AVAILABLE",
            "PENDING_DELETE",
            "SUSPENDED",
        ]
    ] = Field(default=None, alias="Status")
    validity: Optional[DatetimeRangeModel] = Field(default=None, alias="Validity")
    beneficiary: Optional[str] = Field(default=None, alias="Beneficiary")
    entitlements: Optional[List[EntitlementModel]] = Field(
        default=None, alias="Entitlements"
    )
    consumption_configuration: Optional[ConsumptionConfigurationModel] = Field(
        default=None, alias="ConsumptionConfiguration"
    )
    license_metadata: Optional[List[MetadataModel]] = Field(
        default=None, alias="LicenseMetadata"
    )
    create_time: Optional[str] = Field(default=None, alias="CreateTime")
    version: Optional[str] = Field(default=None, alias="Version")
    received_metadata: Optional[ReceivedMetadataModel] = Field(
        default=None, alias="ReceivedMetadata"
    )


class LicenseModel(BaseModel):
    license_arn: Optional[str] = Field(default=None, alias="LicenseArn")
    license_name: Optional[str] = Field(default=None, alias="LicenseName")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    product_s_ku: Optional[str] = Field(default=None, alias="ProductSKU")
    issuer: Optional[IssuerDetailsModel] = Field(default=None, alias="Issuer")
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    status: Optional[
        Literal[
            "AVAILABLE",
            "DEACTIVATED",
            "DELETED",
            "EXPIRED",
            "PENDING_AVAILABLE",
            "PENDING_DELETE",
            "SUSPENDED",
        ]
    ] = Field(default=None, alias="Status")
    validity: Optional[DatetimeRangeModel] = Field(default=None, alias="Validity")
    beneficiary: Optional[str] = Field(default=None, alias="Beneficiary")
    entitlements: Optional[List[EntitlementModel]] = Field(
        default=None, alias="Entitlements"
    )
    consumption_configuration: Optional[ConsumptionConfigurationModel] = Field(
        default=None, alias="ConsumptionConfiguration"
    )
    license_metadata: Optional[List[MetadataModel]] = Field(
        default=None, alias="LicenseMetadata"
    )
    create_time: Optional[str] = Field(default=None, alias="CreateTime")
    version: Optional[str] = Field(default=None, alias="Version")


class ListLicenseConversionTasksResponseModel(BaseModel):
    license_conversion_tasks: List[LicenseConversionTaskModel] = Field(
        alias="LicenseConversionTasks"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLicenseUsageResponseModel(BaseModel):
    license_usage: LicenseUsageModel = Field(alias="LicenseUsage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLicenseConfigurationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    license_counting_type: Literal["Core", "Instance", "Socket", "vCPU"] = Field(
        alias="LicenseCountingType"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    license_count: Optional[int] = Field(default=None, alias="LicenseCount")
    license_count_hard_limit: Optional[bool] = Field(
        default=None, alias="LicenseCountHardLimit"
    )
    license_rules: Optional[Sequence[str]] = Field(default=None, alias="LicenseRules")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    disassociate_when_not_found: Optional[bool] = Field(
        default=None, alias="DisassociateWhenNotFound"
    )
    product_information_list: Optional[Sequence[ProductInformationModel]] = Field(
        default=None, alias="ProductInformationList"
    )


class GetLicenseConfigurationResponseModel(BaseModel):
    license_configuration_id: str = Field(alias="LicenseConfigurationId")
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    license_counting_type: Literal["Core", "Instance", "Socket", "vCPU"] = Field(
        alias="LicenseCountingType"
    )
    license_rules: List[str] = Field(alias="LicenseRules")
    license_count: int = Field(alias="LicenseCount")
    license_count_hard_limit: bool = Field(alias="LicenseCountHardLimit")
    consumed_licenses: int = Field(alias="ConsumedLicenses")
    status: str = Field(alias="Status")
    owner_account_id: str = Field(alias="OwnerAccountId")
    consumed_license_summary_list: List[ConsumedLicenseSummaryModel] = Field(
        alias="ConsumedLicenseSummaryList"
    )
    managed_resource_summary_list: List[ManagedResourceSummaryModel] = Field(
        alias="ManagedResourceSummaryList"
    )
    tags: List[TagModel] = Field(alias="Tags")
    product_information_list: List[ProductInformationModel] = Field(
        alias="ProductInformationList"
    )
    automated_discovery_information: AutomatedDiscoveryInformationModel = Field(
        alias="AutomatedDiscoveryInformation"
    )
    disassociate_when_not_found: bool = Field(alias="DisassociateWhenNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LicenseConfigurationModel(BaseModel):
    license_configuration_id: Optional[str] = Field(
        default=None, alias="LicenseConfigurationId"
    )
    license_configuration_arn: Optional[str] = Field(
        default=None, alias="LicenseConfigurationArn"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    license_counting_type: Optional[
        Literal["Core", "Instance", "Socket", "vCPU"]
    ] = Field(default=None, alias="LicenseCountingType")
    license_rules: Optional[List[str]] = Field(default=None, alias="LicenseRules")
    license_count: Optional[int] = Field(default=None, alias="LicenseCount")
    license_count_hard_limit: Optional[bool] = Field(
        default=None, alias="LicenseCountHardLimit"
    )
    disassociate_when_not_found: Optional[bool] = Field(
        default=None, alias="DisassociateWhenNotFound"
    )
    consumed_licenses: Optional[int] = Field(default=None, alias="ConsumedLicenses")
    status: Optional[str] = Field(default=None, alias="Status")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    consumed_license_summary_list: Optional[List[ConsumedLicenseSummaryModel]] = Field(
        default=None, alias="ConsumedLicenseSummaryList"
    )
    managed_resource_summary_list: Optional[List[ManagedResourceSummaryModel]] = Field(
        default=None, alias="ManagedResourceSummaryList"
    )
    product_information_list: Optional[List[ProductInformationModel]] = Field(
        default=None, alias="ProductInformationList"
    )
    automated_discovery_information: Optional[
        AutomatedDiscoveryInformationModel
    ] = Field(default=None, alias="AutomatedDiscoveryInformation")


class UpdateLicenseConfigurationRequestModel(BaseModel):
    license_configuration_arn: str = Field(alias="LicenseConfigurationArn")
    license_configuration_status: Optional[Literal["AVAILABLE", "DISABLED"]] = Field(
        default=None, alias="LicenseConfigurationStatus"
    )
    license_rules: Optional[Sequence[str]] = Field(default=None, alias="LicenseRules")
    license_count: Optional[int] = Field(default=None, alias="LicenseCount")
    license_count_hard_limit: Optional[bool] = Field(
        default=None, alias="LicenseCountHardLimit"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    product_information_list: Optional[Sequence[ProductInformationModel]] = Field(
        default=None, alias="ProductInformationList"
    )
    disassociate_when_not_found: Optional[bool] = Field(
        default=None, alias="DisassociateWhenNotFound"
    )


class GetLicenseManagerReportGeneratorResponseModel(BaseModel):
    report_generator: ReportGeneratorModel = Field(alias="ReportGenerator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLicenseManagerReportGeneratorsResponseModel(BaseModel):
    report_generators: List[ReportGeneratorModel] = Field(alias="ReportGenerators")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReceivedLicensesForOrganizationResponseModel(BaseModel):
    licenses: List[GrantedLicenseModel] = Field(alias="Licenses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReceivedLicensesResponseModel(BaseModel):
    licenses: List[GrantedLicenseModel] = Field(alias="Licenses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLicenseResponseModel(BaseModel):
    license: LicenseModel = Field(alias="License")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLicenseVersionsResponseModel(BaseModel):
    licenses: List[LicenseModel] = Field(alias="Licenses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLicensesResponseModel(BaseModel):
    licenses: List[LicenseModel] = Field(alias="Licenses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLicenseConfigurationsResponseModel(BaseModel):
    license_configurations: List[LicenseConfigurationModel] = Field(
        alias="LicenseConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
