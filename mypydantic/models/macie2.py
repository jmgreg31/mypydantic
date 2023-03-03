# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptInvitationRequestModel(BaseModel):
    invitation_id: str = Field(alias="invitationId")
    administrator_account_id: Optional[str] = Field(
        default=None, alias="administratorAccountId"
    )
    master_account: Optional[str] = Field(default=None, alias="masterAccount")


class AccessControlListModel(BaseModel):
    allows_public_read_access: Optional[bool] = Field(
        default=None, alias="allowsPublicReadAccess"
    )
    allows_public_write_access: Optional[bool] = Field(
        default=None, alias="allowsPublicWriteAccess"
    )


class AccountDetailModel(BaseModel):
    account_id: str = Field(alias="accountId")
    email: str = Field(alias="email")


class BlockPublicAccessModel(BaseModel):
    block_public_acls: Optional[bool] = Field(default=None, alias="blockPublicAcls")
    block_public_policy: Optional[bool] = Field(default=None, alias="blockPublicPolicy")
    ignore_public_acls: Optional[bool] = Field(default=None, alias="ignorePublicAcls")
    restrict_public_buckets: Optional[bool] = Field(
        default=None, alias="restrictPublicBuckets"
    )


class AdminAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    status: Optional[Literal["DISABLING_IN_PROGRESS", "ENABLED"]] = Field(
        default=None, alias="status"
    )


class S3WordsListModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    object_key: str = Field(alias="objectKey")


class AllowListStatusModel(BaseModel):
    code: Literal[
        "OK",
        "S3_OBJECT_ACCESS_DENIED",
        "S3_OBJECT_EMPTY",
        "S3_OBJECT_NOT_FOUND",
        "S3_OBJECT_OVERSIZE",
        "S3_THROTTLED",
        "S3_USER_ACCESS_DENIED",
        "UNKNOWN_ERROR",
    ] = Field(alias="code")
    description: Optional[str] = Field(default=None, alias="description")


class AllowListSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class ApiCallDetailsModel(BaseModel):
    api: Optional[str] = Field(default=None, alias="api")
    api_service_name: Optional[str] = Field(default=None, alias="apiServiceName")
    first_seen: Optional[datetime] = Field(default=None, alias="firstSeen")
    last_seen: Optional[datetime] = Field(default=None, alias="lastSeen")


class AwsAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    principal_id: Optional[str] = Field(default=None, alias="principalId")


class AwsServiceModel(BaseModel):
    invoked_by: Optional[str] = Field(default=None, alias="invokedBy")


class BatchGetCustomDataIdentifierSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    deleted: Optional[bool] = Field(default=None, alias="deleted")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class BatchGetCustomDataIdentifiersRequestModel(BaseModel):
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BucketCountByEffectivePermissionModel(BaseModel):
    publicly_accessible: Optional[int] = Field(default=None, alias="publiclyAccessible")
    publicly_readable: Optional[int] = Field(default=None, alias="publiclyReadable")
    publicly_writable: Optional[int] = Field(default=None, alias="publiclyWritable")
    unknown: Optional[int] = Field(default=None, alias="unknown")


class BucketCountByEncryptionTypeModel(BaseModel):
    kms_managed: Optional[int] = Field(default=None, alias="kmsManaged")
    s3_managed: Optional[int] = Field(default=None, alias="s3Managed")
    unencrypted: Optional[int] = Field(default=None, alias="unencrypted")
    unknown: Optional[int] = Field(default=None, alias="unknown")


class BucketCountBySharedAccessTypeModel(BaseModel):
    external: Optional[int] = Field(default=None, alias="external")
    internal: Optional[int] = Field(default=None, alias="internal")
    not_shared: Optional[int] = Field(default=None, alias="notShared")
    unknown: Optional[int] = Field(default=None, alias="unknown")


class BucketCountPolicyAllowsUnencryptedObjectUploadsModel(BaseModel):
    allows_unencrypted_object_uploads: Optional[int] = Field(
        default=None, alias="allowsUnencryptedObjectUploads"
    )
    denies_unencrypted_object_uploads: Optional[int] = Field(
        default=None, alias="deniesUnencryptedObjectUploads"
    )
    unknown: Optional[int] = Field(default=None, alias="unknown")


class BucketCriteriaAdditionalPropertiesModel(BaseModel):
    eq: Optional[Sequence[str]] = Field(default=None, alias="eq")
    gt: Optional[int] = Field(default=None, alias="gt")
    gte: Optional[int] = Field(default=None, alias="gte")
    lt: Optional[int] = Field(default=None, alias="lt")
    lte: Optional[int] = Field(default=None, alias="lte")
    neq: Optional[Sequence[str]] = Field(default=None, alias="neq")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class BucketPolicyModel(BaseModel):
    allows_public_read_access: Optional[bool] = Field(
        default=None, alias="allowsPublicReadAccess"
    )
    allows_public_write_access: Optional[bool] = Field(
        default=None, alias="allowsPublicWriteAccess"
    )


class BucketServerSideEncryptionModel(BaseModel):
    kms_master_key_id: Optional[str] = Field(default=None, alias="kmsMasterKeyId")
    type: Optional[Literal["AES256", "NONE", "aws:kms"]] = Field(
        default=None, alias="type"
    )


class JobDetailsModel(BaseModel):
    is_defined_in_job: Optional[Literal["FALSE", "TRUE", "UNKNOWN"]] = Field(
        default=None, alias="isDefinedInJob"
    )
    is_monitored_by_job: Optional[Literal["FALSE", "TRUE", "UNKNOWN"]] = Field(
        default=None, alias="isMonitoredByJob"
    )
    last_job_id: Optional[str] = Field(default=None, alias="lastJobId")
    last_job_run_time: Optional[datetime] = Field(default=None, alias="lastJobRunTime")


class KeyValuePairModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ObjectCountByEncryptionTypeModel(BaseModel):
    customer_managed: Optional[int] = Field(default=None, alias="customerManaged")
    kms_managed: Optional[int] = Field(default=None, alias="kmsManaged")
    s3_managed: Optional[int] = Field(default=None, alias="s3Managed")
    unencrypted: Optional[int] = Field(default=None, alias="unencrypted")
    unknown: Optional[int] = Field(default=None, alias="unknown")


class ObjectLevelStatisticsModel(BaseModel):
    file_type: Optional[int] = Field(default=None, alias="fileType")
    storage_class: Optional[int] = Field(default=None, alias="storageClass")
    total: Optional[int] = Field(default=None, alias="total")


class ReplicationDetailsModel(BaseModel):
    replicated: Optional[bool] = Field(default=None, alias="replicated")
    replicated_externally: Optional[bool] = Field(
        default=None, alias="replicatedExternally"
    )
    replication_accounts: Optional[List[str]] = Field(
        default=None, alias="replicationAccounts"
    )


class BucketSortCriteriaModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class SensitivityAggregationsModel(BaseModel):
    classifiable_size_in_bytes: Optional[int] = Field(
        default=None, alias="classifiableSizeInBytes"
    )
    publicly_accessible_count: Optional[int] = Field(
        default=None, alias="publiclyAccessibleCount"
    )
    total_count: Optional[int] = Field(default=None, alias="totalCount")
    total_size_in_bytes: Optional[int] = Field(default=None, alias="totalSizeInBytes")


class CellModel(BaseModel):
    cell_reference: Optional[str] = Field(default=None, alias="cellReference")
    column: Optional[int] = Field(default=None, alias="column")
    column_name: Optional[str] = Field(default=None, alias="columnName")
    row: Optional[int] = Field(default=None, alias="row")


class S3DestinationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    kms_key_arn: str = Field(alias="kmsKeyArn")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class ClassificationResultStatusModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    reason: Optional[str] = Field(default=None, alias="reason")


class ClassificationScopeSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class SeverityLevelModel(BaseModel):
    occurrences_threshold: int = Field(alias="occurrencesThreshold")
    severity: Literal["HIGH", "LOW", "MEDIUM"] = Field(alias="severity")


class CreateInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="accountIds")
    disable_email_notification: Optional[bool] = Field(
        default=None, alias="disableEmailNotification"
    )
    message: Optional[str] = Field(default=None, alias="message")


class UnprocessedAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    error_code: Optional[Literal["ClientError", "InternalError"]] = Field(
        default=None, alias="errorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class CreateSampleFindingsRequestModel(BaseModel):
    finding_types: Optional[
        Sequence[
            Literal[
                "Policy:IAMUser/S3BlockPublicAccessDisabled",
                "Policy:IAMUser/S3BucketEncryptionDisabled",
                "Policy:IAMUser/S3BucketPublic",
                "Policy:IAMUser/S3BucketReplicatedExternally",
                "Policy:IAMUser/S3BucketSharedExternally",
                "Policy:IAMUser/S3BucketSharedWithCloudFront",
                "SensitiveData:S3Object/Credentials",
                "SensitiveData:S3Object/CustomIdentifier",
                "SensitiveData:S3Object/Financial",
                "SensitiveData:S3Object/Multiple",
                "SensitiveData:S3Object/Personal",
            ]
        ]
    ] = Field(default=None, alias="findingTypes")


class SimpleCriterionForJobModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
    ] = Field(default=None, alias="comparator")
    key: Optional[
        Literal[
            "ACCOUNT_ID",
            "S3_BUCKET_EFFECTIVE_PERMISSION",
            "S3_BUCKET_NAME",
            "S3_BUCKET_SHARED_ACCESS",
        ]
    ] = Field(default=None, alias="key")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class CriterionAdditionalPropertiesModel(BaseModel):
    eq: Optional[Sequence[str]] = Field(default=None, alias="eq")
    eq_exact_match: Optional[Sequence[str]] = Field(default=None, alias="eqExactMatch")
    gt: Optional[int] = Field(default=None, alias="gt")
    gte: Optional[int] = Field(default=None, alias="gte")
    lt: Optional[int] = Field(default=None, alias="lt")
    lte: Optional[int] = Field(default=None, alias="lte")
    neq: Optional[Sequence[str]] = Field(default=None, alias="neq")


class CustomDataIdentifierSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class DeclineInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="accountIds")


class DeleteAllowListRequestModel(BaseModel):
    id: str = Field(alias="id")
    ignore_job_checks: Optional[str] = Field(default=None, alias="ignoreJobChecks")


class DeleteCustomDataIdentifierRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteFindingsFilterRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="accountIds")


class DeleteMemberRequestModel(BaseModel):
    id: str = Field(alias="id")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeClassificationJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class LastRunErrorStatusModel(BaseModel):
    code: Optional[Literal["ERROR", "NONE"]] = Field(default=None, alias="code")


class StatisticsModel(BaseModel):
    approximate_number_of_objects_to_process: Optional[float] = Field(
        default=None, alias="approximateNumberOfObjectsToProcess"
    )
    number_of_runs: Optional[float] = Field(default=None, alias="numberOfRuns")


class UserPausedDetailsModel(BaseModel):
    job_expires_at: Optional[datetime] = Field(default=None, alias="jobExpiresAt")
    job_imminent_expiration_health_event_arn: Optional[str] = Field(
        default=None, alias="jobImminentExpirationHealthEventArn"
    )
    job_paused_at: Optional[datetime] = Field(default=None, alias="jobPausedAt")


class DetectedDataDetailsModel(BaseModel):
    value: str = Field(alias="value")


class DetectionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    count: Optional[int] = Field(default=None, alias="count")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    suppressed: Optional[bool] = Field(default=None, alias="suppressed")
    type: Optional[Literal["CUSTOM", "MANAGED"]] = Field(default=None, alias="type")


class DisableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="adminAccountId")


class DisassociateMemberRequestModel(BaseModel):
    id: str = Field(alias="id")


class DomainDetailsModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")


class EnableMacieRequestModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    finding_publishing_frequency: Optional[
        Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
    ] = Field(default=None, alias="findingPublishingFrequency")
    status: Optional[Literal["ENABLED", "PAUSED"]] = Field(default=None, alias="status")


class EnableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="adminAccountId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class FindingStatisticsSortCriteriaModel(BaseModel):
    attribute_name: Optional[Literal["count", "groupKey"]] = Field(
        default=None, alias="attributeName"
    )
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class SeverityModel(BaseModel):
    description: Optional[Literal["High", "Low", "Medium"]] = Field(
        default=None, alias="description"
    )
    score: Optional[int] = Field(default=None, alias="score")


class FindingsFilterListItemModel(BaseModel):
    action: Optional[Literal["ARCHIVE", "NOOP"]] = Field(default=None, alias="action")
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class InvitationModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    invitation_id: Optional[str] = Field(default=None, alias="invitationId")
    invited_at: Optional[datetime] = Field(default=None, alias="invitedAt")
    relationship_status: Optional[
        Literal[
            "AccountSuspended",
            "Created",
            "EmailVerificationFailed",
            "EmailVerificationInProgress",
            "Enabled",
            "Invited",
            "Paused",
            "RegionDisabled",
            "Removed",
            "Resigned",
        ]
    ] = Field(default=None, alias="relationshipStatus")


class GetAllowListRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetBucketStatisticsRequestModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")


class GetClassificationScopeRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetCustomDataIdentifierRequestModel(BaseModel):
    id: str = Field(alias="id")


class GroupCountModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    group_key: Optional[str] = Field(default=None, alias="groupKey")


class GetFindingsFilterRequestModel(BaseModel):
    id: str = Field(alias="id")


class SecurityHubConfigurationModel(BaseModel):
    publish_classification_findings: bool = Field(alias="publishClassificationFindings")
    publish_policy_findings: bool = Field(alias="publishPolicyFindings")


class SortCriteriaModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class GetMemberRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetResourceProfileRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ResourceStatisticsModel(BaseModel):
    total_bytes_classified: Optional[int] = Field(
        default=None, alias="totalBytesClassified"
    )
    total_detections: Optional[int] = Field(default=None, alias="totalDetections")
    total_detections_suppressed: Optional[int] = Field(
        default=None, alias="totalDetectionsSuppressed"
    )
    total_items_classified: Optional[int] = Field(
        default=None, alias="totalItemsClassified"
    )
    total_items_sensitive: Optional[int] = Field(
        default=None, alias="totalItemsSensitive"
    )
    total_items_skipped: Optional[int] = Field(default=None, alias="totalItemsSkipped")
    total_items_skipped_invalid_encryption: Optional[int] = Field(
        default=None, alias="totalItemsSkippedInvalidEncryption"
    )
    total_items_skipped_invalid_kms: Optional[int] = Field(
        default=None, alias="totalItemsSkippedInvalidKms"
    )
    total_items_skipped_permission_denied: Optional[int] = Field(
        default=None, alias="totalItemsSkippedPermissionDenied"
    )


class RevealConfigurationModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class GetSensitiveDataOccurrencesAvailabilityRequestModel(BaseModel):
    finding_id: str = Field(alias="findingId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetSensitiveDataOccurrencesRequestModel(BaseModel):
    finding_id: str = Field(alias="findingId")


class GetSensitivityInspectionTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class SensitivityInspectionTemplateExcludesModel(BaseModel):
    managed_data_identifier_ids: Optional[List[str]] = Field(
        default=None, alias="managedDataIdentifierIds"
    )


class SensitivityInspectionTemplateIncludesModel(BaseModel):
    allow_list_ids: Optional[List[str]] = Field(default=None, alias="allowListIds")
    custom_data_identifier_ids: Optional[List[str]] = Field(
        default=None, alias="customDataIdentifierIds"
    )
    managed_data_identifier_ids: Optional[List[str]] = Field(
        default=None, alias="managedDataIdentifierIds"
    )


class UsageStatisticsFilterModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE"]
    ] = Field(default=None, alias="comparator")
    key: Optional[
        Literal["accountId", "freeTrialStartDate", "serviceLimit", "total"]
    ] = Field(default=None, alias="key")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class UsageStatisticsSortByModel(BaseModel):
    key: Optional[
        Literal["accountId", "freeTrialStartDate", "serviceLimitValue", "total"]
    ] = Field(default=None, alias="key")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class GetUsageTotalsRequestModel(BaseModel):
    time_range: Optional[str] = Field(default=None, alias="timeRange")


class UsageTotalModel(BaseModel):
    currency: Optional[Literal["USD"]] = Field(default=None, alias="currency")
    estimated_cost: Optional[str] = Field(default=None, alias="estimatedCost")
    type: Optional[
        Literal[
            "AUTOMATED_OBJECT_MONITORING",
            "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
            "DATA_INVENTORY_EVALUATION",
            "SENSITIVE_DATA_DISCOVERY",
        ]
    ] = Field(default=None, alias="type")


class IamUserModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    arn: Optional[str] = Field(default=None, alias="arn")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    user_name: Optional[str] = Field(default=None, alias="userName")


class IpCityModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class IpCountryModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    name: Optional[str] = Field(default=None, alias="name")


class IpGeoLocationModel(BaseModel):
    lat: Optional[float] = Field(default=None, alias="lat")
    lon: Optional[float] = Field(default=None, alias="lon")


class IpOwnerModel(BaseModel):
    asn: Optional[str] = Field(default=None, alias="asn")
    asn_org: Optional[str] = Field(default=None, alias="asnOrg")
    isp: Optional[str] = Field(default=None, alias="isp")
    org: Optional[str] = Field(default=None, alias="org")


class MonthlyScheduleModel(BaseModel):
    day_of_month: Optional[int] = Field(default=None, alias="dayOfMonth")


class WeeklyScheduleModel(BaseModel):
    day_of_week: Optional[
        Literal[
            "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
        ]
    ] = Field(default=None, alias="dayOfWeek")


class SimpleScopeTermModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
    ] = Field(default=None, alias="comparator")
    key: Optional[
        Literal[
            "OBJECT_EXTENSION", "OBJECT_KEY", "OBJECT_LAST_MODIFIED_DATE", "OBJECT_SIZE"
        ]
    ] = Field(default=None, alias="key")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class S3BucketDefinitionForJobModel(BaseModel):
    account_id: str = Field(alias="accountId")
    buckets: Sequence[str] = Field(alias="buckets")


class ListAllowListsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobsSortCriteriaModel(BaseModel):
    attribute_name: Optional[
        Literal["createdAt", "jobStatus", "jobType", "name"]
    ] = Field(default=None, alias="attributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class ListClassificationScopesRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCustomDataIdentifiersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListFindingsFiltersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListInvitationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobsFilterTermModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
    ] = Field(default=None, alias="comparator")
    key: Optional[Literal["createdAt", "jobStatus", "jobType", "name"]] = Field(
        default=None, alias="key"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ListManagedDataIdentifiersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ManagedDataIdentifierSummaryModel(BaseModel):
    category: Optional[
        Literal[
            "CREDENTIALS",
            "CUSTOM_IDENTIFIER",
            "FINANCIAL_INFORMATION",
            "PERSONAL_INFORMATION",
        ]
    ] = Field(default=None, alias="category")
    id: Optional[str] = Field(default=None, alias="id")


class ListMembersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    only_associated: Optional[str] = Field(default=None, alias="onlyAssociated")


class MemberModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    administrator_account_id: Optional[str] = Field(
        default=None, alias="administratorAccountId"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    email: Optional[str] = Field(default=None, alias="email")
    invited_at: Optional[datetime] = Field(default=None, alias="invitedAt")
    master_account_id: Optional[str] = Field(default=None, alias="masterAccountId")
    relationship_status: Optional[
        Literal[
            "AccountSuspended",
            "Created",
            "EmailVerificationFailed",
            "EmailVerificationInProgress",
            "Enabled",
            "Invited",
            "Paused",
            "RegionDisabled",
            "Removed",
            "Resigned",
        ]
    ] = Field(default=None, alias="relationshipStatus")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class ListOrganizationAdminAccountsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListResourceProfileArtifactsRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ResourceProfileArtifactModel(BaseModel):
    arn: str = Field(alias="arn")
    classification_result_status: str = Field(alias="classificationResultStatus")
    sensitive: Optional[bool] = Field(default=None, alias="sensitive")


class ListResourceProfileDetectionsRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSensitivityInspectionTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SensitivityInspectionTemplatesEntryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class RangeModel(BaseModel):
    end: Optional[int] = Field(default=None, alias="end")
    start: Optional[int] = Field(default=None, alias="start")
    start_column: Optional[int] = Field(default=None, alias="startColumn")


class RecordModel(BaseModel):
    json_path: Optional[str] = Field(default=None, alias="jsonPath")
    record_index: Optional[int] = Field(default=None, alias="recordIndex")


class S3BucketOwnerModel(BaseModel):
    display_name: Optional[str] = Field(default=None, alias="displayName")
    id: Optional[str] = Field(default=None, alias="id")


class ServerSideEncryptionModel(BaseModel):
    encryption_type: Optional[Literal["AES256", "NONE", "UNKNOWN", "aws:kms"]] = Field(
        default=None, alias="encryptionType"
    )
    kms_master_key_id: Optional[str] = Field(default=None, alias="kmsMasterKeyId")


class S3ClassificationScopeExclusionModel(BaseModel):
    bucket_names: List[str] = Field(alias="bucketNames")


class S3ClassificationScopeExclusionUpdateModel(BaseModel):
    bucket_names: Sequence[str] = Field(alias="bucketNames")
    operation: Literal["ADD", "REMOVE", "REPLACE"] = Field(alias="operation")


class SearchResourcesSimpleCriterionModel(BaseModel):
    comparator: Optional[Literal["EQ", "NE"]] = Field(default=None, alias="comparator")
    key: Optional[
        Literal[
            "ACCOUNT_ID",
            "S3_BUCKET_EFFECTIVE_PERMISSION",
            "S3_BUCKET_NAME",
            "S3_BUCKET_SHARED_ACCESS",
        ]
    ] = Field(default=None, alias="key")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class SearchResourcesSortCriteriaModel(BaseModel):
    attribute_name: Optional[
        Literal[
            "ACCOUNT_ID",
            "RESOURCE_NAME",
            "S3_CLASSIFIABLE_OBJECT_COUNT",
            "S3_CLASSIFIABLE_SIZE_IN_BYTES",
        ]
    ] = Field(default=None, alias="attributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class SearchResourcesTagCriterionPairModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class ServiceLimitModel(BaseModel):
    is_service_limited: Optional[bool] = Field(default=None, alias="isServiceLimited")
    unit: Optional[Literal["TERABYTES"]] = Field(default=None, alias="unit")
    value: Optional[int] = Field(default=None, alias="value")


class SessionContextAttributesModel(BaseModel):
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    mfa_authenticated: Optional[bool] = Field(default=None, alias="mfaAuthenticated")


class SessionIssuerModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    arn: Optional[str] = Field(default=None, alias="arn")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    type: Optional[str] = Field(default=None, alias="type")
    user_name: Optional[str] = Field(default=None, alias="userName")


class SuppressDataIdentifierModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[Literal["CUSTOM", "MANAGED"]] = Field(default=None, alias="type")


class TagCriterionPairForJobModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TagValuePairModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class TestCustomDataIdentifierRequestModel(BaseModel):
    regex: str = Field(alias="regex")
    sample_text: str = Field(alias="sampleText")
    ignore_words: Optional[Sequence[str]] = Field(default=None, alias="ignoreWords")
    keywords: Optional[Sequence[str]] = Field(default=None, alias="keywords")
    maximum_match_distance: Optional[int] = Field(
        default=None, alias="maximumMatchDistance"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAutomatedDiscoveryConfigurationRequestModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")


class UpdateClassificationJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_status: Literal[
        "CANCELLED", "COMPLETE", "IDLE", "PAUSED", "RUNNING", "USER_PAUSED"
    ] = Field(alias="jobStatus")


class UpdateMacieSessionRequestModel(BaseModel):
    finding_publishing_frequency: Optional[
        Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
    ] = Field(default=None, alias="findingPublishingFrequency")
    status: Optional[Literal["ENABLED", "PAUSED"]] = Field(default=None, alias="status")


class UpdateMemberSessionRequestModel(BaseModel):
    id: str = Field(alias="id")
    status: Literal["ENABLED", "PAUSED"] = Field(alias="status")


class UpdateOrganizationConfigurationRequestModel(BaseModel):
    auto_enable: bool = Field(alias="autoEnable")


class UpdateResourceProfileRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    sensitivity_score_override: Optional[int] = Field(
        default=None, alias="sensitivityScoreOverride"
    )


class UserIdentityRootModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    arn: Optional[str] = Field(default=None, alias="arn")
    principal_id: Optional[str] = Field(default=None, alias="principalId")


class CreateMemberRequestModel(BaseModel):
    account: AccountDetailModel = Field(alias="account")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class AccountLevelPermissionsModel(BaseModel):
    block_public_access: Optional[BlockPublicAccessModel] = Field(
        default=None, alias="blockPublicAccess"
    )


class AllowListCriteriaModel(BaseModel):
    regex: Optional[str] = Field(default=None, alias="regex")
    s3_words_list: Optional[S3WordsListModel] = Field(default=None, alias="s3WordsList")


class FindingActionModel(BaseModel):
    action_type: Optional[Literal["AWS_API_CALL"]] = Field(
        default=None, alias="actionType"
    )
    api_call_details: Optional[ApiCallDetailsModel] = Field(
        default=None, alias="apiCallDetails"
    )


class BatchGetCustomDataIdentifiersResponseModel(BaseModel):
    custom_data_identifiers: List[BatchGetCustomDataIdentifierSummaryModel] = Field(
        alias="customDataIdentifiers"
    )
    not_found_identifier_ids: List[str] = Field(alias="notFoundIdentifierIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAllowListResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClassificationJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomDataIdentifierResponseModel(BaseModel):
    custom_data_identifier_id: str = Field(alias="customDataIdentifierId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFindingsFilterResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMemberResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: bool = Field(alias="autoEnable")
    max_account_limit_reached: bool = Field(alias="maxAccountLimitReached")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAutomatedDiscoveryConfigurationResponseModel(BaseModel):
    classification_scope_id: str = Field(alias="classificationScopeId")
    disabled_at: datetime = Field(alias="disabledAt")
    first_enabled_at: datetime = Field(alias="firstEnabledAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    sensitivity_inspection_template_id: str = Field(
        alias="sensitivityInspectionTemplateId"
    )
    status: Literal["DISABLED", "ENABLED"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInvitationsCountResponseModel(BaseModel):
    invitations_count: int = Field(alias="invitationsCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMacieSessionResponseModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    finding_publishing_frequency: Literal[
        "FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"
    ] = Field(alias="findingPublishingFrequency")
    service_role: str = Field(alias="serviceRole")
    status: Literal["ENABLED", "PAUSED"] = Field(alias="status")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMemberResponseModel(BaseModel):
    account_id: str = Field(alias="accountId")
    administrator_account_id: str = Field(alias="administratorAccountId")
    arn: str = Field(alias="arn")
    email: str = Field(alias="email")
    invited_at: datetime = Field(alias="invitedAt")
    master_account_id: str = Field(alias="masterAccountId")
    relationship_status: Literal[
        "AccountSuspended",
        "Created",
        "EmailVerificationFailed",
        "EmailVerificationInProgress",
        "Enabled",
        "Invited",
        "Paused",
        "RegionDisabled",
        "Removed",
        "Resigned",
    ] = Field(alias="relationshipStatus")
    tags: Dict[str, str] = Field(alias="tags")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSensitiveDataOccurrencesAvailabilityResponseModel(BaseModel):
    code: Literal["AVAILABLE", "UNAVAILABLE"] = Field(alias="code")
    reasons: List[
        Literal[
            "INVALID_CLASSIFICATION_RESULT",
            "OBJECT_EXCEEDS_SIZE_QUOTA",
            "OBJECT_UNAVAILABLE",
            "UNSUPPORTED_FINDING_TYPE",
            "UNSUPPORTED_OBJECT_TYPE",
        ]
    ] = Field(alias="reasons")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAllowListsResponseModel(BaseModel):
    allow_lists: List[AllowListSummaryModel] = Field(alias="allowLists")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsResponseModel(BaseModel):
    finding_ids: List[str] = Field(alias="findingIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationAdminAccountsResponseModel(BaseModel):
    admin_accounts: List[AdminAccountModel] = Field(alias="adminAccounts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestCustomDataIdentifierResponseModel(BaseModel):
    match_count: int = Field(alias="matchCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAllowListResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFindingsFilterResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BucketLevelPermissionsModel(BaseModel):
    access_control_list: Optional[AccessControlListModel] = Field(
        default=None, alias="accessControlList"
    )
    block_public_access: Optional[BlockPublicAccessModel] = Field(
        default=None, alias="blockPublicAccess"
    )
    bucket_policy: Optional[BucketPolicyModel] = Field(
        default=None, alias="bucketPolicy"
    )


class MatchingBucketModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    classifiable_object_count: Optional[int] = Field(
        default=None, alias="classifiableObjectCount"
    )
    classifiable_size_in_bytes: Optional[int] = Field(
        default=None, alias="classifiableSizeInBytes"
    )
    error_code: Optional[Literal["ACCESS_DENIED"]] = Field(
        default=None, alias="errorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    job_details: Optional[JobDetailsModel] = Field(default=None, alias="jobDetails")
    last_automated_discovery_time: Optional[datetime] = Field(
        default=None, alias="lastAutomatedDiscoveryTime"
    )
    object_count: Optional[int] = Field(default=None, alias="objectCount")
    object_count_by_encryption_type: Optional[ObjectCountByEncryptionTypeModel] = Field(
        default=None, alias="objectCountByEncryptionType"
    )
    sensitivity_score: Optional[int] = Field(default=None, alias="sensitivityScore")
    size_in_bytes: Optional[int] = Field(default=None, alias="sizeInBytes")
    size_in_bytes_compressed: Optional[int] = Field(
        default=None, alias="sizeInBytesCompressed"
    )
    unclassifiable_object_count: Optional[ObjectLevelStatisticsModel] = Field(
        default=None, alias="unclassifiableObjectCount"
    )
    unclassifiable_object_size_in_bytes: Optional[ObjectLevelStatisticsModel] = Field(
        default=None, alias="unclassifiableObjectSizeInBytes"
    )


class DescribeBucketsRequestModel(BaseModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesModel]] = Field(
        default=None, alias="criteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_criteria: Optional[BucketSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class BucketStatisticsBySensitivityModel(BaseModel):
    classification_error: Optional[SensitivityAggregationsModel] = Field(
        default=None, alias="classificationError"
    )
    not_classified: Optional[SensitivityAggregationsModel] = Field(
        default=None, alias="notClassified"
    )
    not_sensitive: Optional[SensitivityAggregationsModel] = Field(
        default=None, alias="notSensitive"
    )
    sensitive: Optional[SensitivityAggregationsModel] = Field(
        default=None, alias="sensitive"
    )


class ClassificationExportConfigurationModel(BaseModel):
    s3_destination: Optional[S3DestinationModel] = Field(
        default=None, alias="s3Destination"
    )


class ListClassificationScopesResponseModel(BaseModel):
    classification_scopes: List[ClassificationScopeSummaryModel] = Field(
        alias="classificationScopes"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomDataIdentifierRequestModel(BaseModel):
    name: str = Field(alias="name")
    regex: str = Field(alias="regex")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    ignore_words: Optional[Sequence[str]] = Field(default=None, alias="ignoreWords")
    keywords: Optional[Sequence[str]] = Field(default=None, alias="keywords")
    maximum_match_distance: Optional[int] = Field(
        default=None, alias="maximumMatchDistance"
    )
    severity_levels: Optional[Sequence[SeverityLevelModel]] = Field(
        default=None, alias="severityLevels"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetCustomDataIdentifierResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    deleted: bool = Field(alias="deleted")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    ignore_words: List[str] = Field(alias="ignoreWords")
    keywords: List[str] = Field(alias="keywords")
    maximum_match_distance: int = Field(alias="maximumMatchDistance")
    name: str = Field(alias="name")
    regex: str = Field(alias="regex")
    severity_levels: List[SeverityLevelModel] = Field(alias="severityLevels")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="unprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeclineInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="unprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="unprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FindingCriteriaModel(BaseModel):
    criterion: Optional[Mapping[str, CriterionAdditionalPropertiesModel]] = Field(
        default=None, alias="criterion"
    )


class ListCustomDataIdentifiersResponseModel(BaseModel):
    items: List[CustomDataIdentifierSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBucketsRequestDescribeBucketsPaginateModel(BaseModel):
    criteria: Optional[Mapping[str, BucketCriteriaAdditionalPropertiesModel]] = Field(
        default=None, alias="criteria"
    )
    sort_criteria: Optional[BucketSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAllowListsRequestListAllowListsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClassificationScopesRequestListClassificationScopesPaginateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsFiltersRequestListFindingsFiltersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInvitationsRequestListInvitationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersRequestListMembersPaginateModel(BaseModel):
    only_associated: Optional[str] = Field(default=None, alias="onlyAssociated")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateModel(
    BaseModel
):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateModel(
    BaseModel
):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSensitiveDataOccurrencesResponseModel(BaseModel):
    error: str = Field(alias="error")
    sensitive_data_occurrences: Dict[str, List[DetectedDataDetailsModel]] = Field(
        alias="sensitiveDataOccurrences"
    )
    status: Literal["ERROR", "PROCESSING", "SUCCESS"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceProfileDetectionsResponseModel(BaseModel):
    detections: List[DetectionModel] = Field(alias="detections")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsFiltersResponseModel(BaseModel):
    findings_filter_list_items: List[FindingsFilterListItemModel] = Field(
        alias="findingsFilterListItems"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAdministratorAccountResponseModel(BaseModel):
    administrator: InvitationModel = Field(alias="administrator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMasterAccountResponseModel(BaseModel):
    master: InvitationModel = Field(alias="master")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInvitationsResponseModel(BaseModel):
    invitations: List[InvitationModel] = Field(alias="invitations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFindingStatisticsResponseModel(BaseModel):
    counts_by_group: List[GroupCountModel] = Field(alias="countsByGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFindingsPublicationConfigurationResponseModel(BaseModel):
    security_hub_configuration: SecurityHubConfigurationModel = Field(
        alias="securityHubConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutFindingsPublicationConfigurationRequestModel(BaseModel):
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    security_hub_configuration: Optional[SecurityHubConfigurationModel] = Field(
        default=None, alias="securityHubConfiguration"
    )


class GetFindingsRequestModel(BaseModel):
    finding_ids: Sequence[str] = Field(alias="findingIds")
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class GetResourceProfileResponseModel(BaseModel):
    profile_updated_at: datetime = Field(alias="profileUpdatedAt")
    sensitivity_score: int = Field(alias="sensitivityScore")
    sensitivity_score_overridden: bool = Field(alias="sensitivityScoreOverridden")
    statistics: ResourceStatisticsModel = Field(alias="statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRevealConfigurationResponseModel(BaseModel):
    configuration: RevealConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRevealConfigurationRequestModel(BaseModel):
    configuration: RevealConfigurationModel = Field(alias="configuration")


class UpdateRevealConfigurationResponseModel(BaseModel):
    configuration: RevealConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSensitiveDataOccurrencesRequestFindingRevealedWaitModel(BaseModel):
    finding_id: str = Field(alias="findingId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetSensitivityInspectionTemplateResponseModel(BaseModel):
    description: str = Field(alias="description")
    excludes: SensitivityInspectionTemplateExcludesModel = Field(alias="excludes")
    includes: SensitivityInspectionTemplateIncludesModel = Field(alias="includes")
    name: str = Field(alias="name")
    sensitivity_inspection_template_id: str = Field(
        alias="sensitivityInspectionTemplateId"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSensitivityInspectionTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    excludes: Optional[SensitivityInspectionTemplateExcludesModel] = Field(
        default=None, alias="excludes"
    )
    includes: Optional[SensitivityInspectionTemplateIncludesModel] = Field(
        default=None, alias="includes"
    )


class GetUsageStatisticsRequestGetUsageStatisticsPaginateModel(BaseModel):
    filter_by: Optional[Sequence[UsageStatisticsFilterModel]] = Field(
        default=None, alias="filterBy"
    )
    sort_by: Optional[UsageStatisticsSortByModel] = Field(default=None, alias="sortBy")
    time_range: Optional[Literal["MONTH_TO_DATE", "PAST_30_DAYS"]] = Field(
        default=None, alias="timeRange"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUsageStatisticsRequestModel(BaseModel):
    filter_by: Optional[Sequence[UsageStatisticsFilterModel]] = Field(
        default=None, alias="filterBy"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_by: Optional[UsageStatisticsSortByModel] = Field(default=None, alias="sortBy")
    time_range: Optional[Literal["MONTH_TO_DATE", "PAST_30_DAYS"]] = Field(
        default=None, alias="timeRange"
    )


class GetUsageTotalsResponseModel(BaseModel):
    time_range: Literal["MONTH_TO_DATE", "PAST_30_DAYS"] = Field(alias="timeRange")
    usage_totals: List[UsageTotalModel] = Field(alias="usageTotals")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IpAddressDetailsModel(BaseModel):
    ip_address_v4: Optional[str] = Field(default=None, alias="ipAddressV4")
    ip_city: Optional[IpCityModel] = Field(default=None, alias="ipCity")
    ip_country: Optional[IpCountryModel] = Field(default=None, alias="ipCountry")
    ip_geo_location: Optional[IpGeoLocationModel] = Field(
        default=None, alias="ipGeoLocation"
    )
    ip_owner: Optional[IpOwnerModel] = Field(default=None, alias="ipOwner")


class JobScheduleFrequencyModel(BaseModel):
    daily_schedule: Optional[Mapping[str, Any]] = Field(
        default=None, alias="dailySchedule"
    )
    monthly_schedule: Optional[MonthlyScheduleModel] = Field(
        default=None, alias="monthlySchedule"
    )
    weekly_schedule: Optional[WeeklyScheduleModel] = Field(
        default=None, alias="weeklySchedule"
    )


class ListJobsFilterCriteriaModel(BaseModel):
    excludes: Optional[Sequence[ListJobsFilterTermModel]] = Field(
        default=None, alias="excludes"
    )
    includes: Optional[Sequence[ListJobsFilterTermModel]] = Field(
        default=None, alias="includes"
    )


class ListManagedDataIdentifiersResponseModel(BaseModel):
    items: List[ManagedDataIdentifierSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="members")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceProfileArtifactsResponseModel(BaseModel):
    artifacts: List[ResourceProfileArtifactModel] = Field(alias="artifacts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSensitivityInspectionTemplatesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sensitivity_inspection_templates: List[
        SensitivityInspectionTemplatesEntryModel
    ] = Field(alias="sensitivityInspectionTemplates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PageModel(BaseModel):
    line_range: Optional[RangeModel] = Field(default=None, alias="lineRange")
    offset_range: Optional[RangeModel] = Field(default=None, alias="offsetRange")
    page_number: Optional[int] = Field(default=None, alias="pageNumber")


class S3ObjectModel(BaseModel):
    bucket_arn: Optional[str] = Field(default=None, alias="bucketArn")
    etag: Optional[str] = Field(default=None, alias="eTag")
    extension: Optional[str] = Field(default=None, alias="extension")
    key: Optional[str] = Field(default=None, alias="key")
    last_modified: Optional[datetime] = Field(default=None, alias="lastModified")
    path: Optional[str] = Field(default=None, alias="path")
    public_access: Optional[bool] = Field(default=None, alias="publicAccess")
    server_side_encryption: Optional[ServerSideEncryptionModel] = Field(
        default=None, alias="serverSideEncryption"
    )
    size: Optional[int] = Field(default=None, alias="size")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "OUTPOSTS",
            "REDUCED_REDUNDANCY",
            "STANDARD",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="storageClass")
    tags: Optional[List[KeyValuePairModel]] = Field(default=None, alias="tags")
    version_id: Optional[str] = Field(default=None, alias="versionId")


class S3ClassificationScopeModel(BaseModel):
    excludes: S3ClassificationScopeExclusionModel = Field(alias="excludes")


class S3ClassificationScopeUpdateModel(BaseModel):
    excludes: S3ClassificationScopeExclusionUpdateModel = Field(alias="excludes")


class SearchResourcesTagCriterionModel(BaseModel):
    comparator: Optional[Literal["EQ", "NE"]] = Field(default=None, alias="comparator")
    tag_values: Optional[Sequence[SearchResourcesTagCriterionPairModel]] = Field(
        default=None, alias="tagValues"
    )


class UsageByAccountModel(BaseModel):
    currency: Optional[Literal["USD"]] = Field(default=None, alias="currency")
    estimated_cost: Optional[str] = Field(default=None, alias="estimatedCost")
    service_limit: Optional[ServiceLimitModel] = Field(
        default=None, alias="serviceLimit"
    )
    type: Optional[
        Literal[
            "AUTOMATED_OBJECT_MONITORING",
            "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
            "DATA_INVENTORY_EVALUATION",
            "SENSITIVE_DATA_DISCOVERY",
        ]
    ] = Field(default=None, alias="type")


class SessionContextModel(BaseModel):
    attributes: Optional[SessionContextAttributesModel] = Field(
        default=None, alias="attributes"
    )
    session_issuer: Optional[SessionIssuerModel] = Field(
        default=None, alias="sessionIssuer"
    )


class UpdateResourceProfileDetectionsRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    suppress_data_identifiers: Optional[Sequence[SuppressDataIdentifierModel]] = Field(
        default=None, alias="suppressDataIdentifiers"
    )


class TagCriterionForJobModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
    ] = Field(default=None, alias="comparator")
    tag_values: Optional[Sequence[TagCriterionPairForJobModel]] = Field(
        default=None, alias="tagValues"
    )


class TagScopeTermModel(BaseModel):
    comparator: Optional[
        Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
    ] = Field(default=None, alias="comparator")
    key: Optional[str] = Field(default=None, alias="key")
    tag_values: Optional[Sequence[TagValuePairModel]] = Field(
        default=None, alias="tagValues"
    )
    target: Optional[Literal["S3_OBJECT"]] = Field(default=None, alias="target")


class CreateAllowListRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    criteria: AllowListCriteriaModel = Field(alias="criteria")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetAllowListResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    criteria: AllowListCriteriaModel = Field(alias="criteria")
    description: str = Field(alias="description")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    status: AllowListStatusModel = Field(alias="status")
    tags: Dict[str, str] = Field(alias="tags")
    updated_at: datetime = Field(alias="updatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAllowListRequestModel(BaseModel):
    criteria: AllowListCriteriaModel = Field(alias="criteria")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class BucketPermissionConfigurationModel(BaseModel):
    account_level_permissions: Optional[AccountLevelPermissionsModel] = Field(
        default=None, alias="accountLevelPermissions"
    )
    bucket_level_permissions: Optional[BucketLevelPermissionsModel] = Field(
        default=None, alias="bucketLevelPermissions"
    )


class MatchingResourceModel(BaseModel):
    matching_bucket: Optional[MatchingBucketModel] = Field(
        default=None, alias="matchingBucket"
    )


class GetBucketStatisticsResponseModel(BaseModel):
    bucket_count: int = Field(alias="bucketCount")
    bucket_count_by_effective_permission: BucketCountByEffectivePermissionModel = Field(
        alias="bucketCountByEffectivePermission"
    )
    bucket_count_by_encryption_type: BucketCountByEncryptionTypeModel = Field(
        alias="bucketCountByEncryptionType"
    )
    bucket_count_by_object_encryption_requirement: BucketCountPolicyAllowsUnencryptedObjectUploadsModel = Field(
        alias="bucketCountByObjectEncryptionRequirement"
    )
    bucket_count_by_shared_access_type: BucketCountBySharedAccessTypeModel = Field(
        alias="bucketCountBySharedAccessType"
    )
    bucket_statistics_by_sensitivity: BucketStatisticsBySensitivityModel = Field(
        alias="bucketStatisticsBySensitivity"
    )
    classifiable_object_count: int = Field(alias="classifiableObjectCount")
    classifiable_size_in_bytes: int = Field(alias="classifiableSizeInBytes")
    last_updated: datetime = Field(alias="lastUpdated")
    object_count: int = Field(alias="objectCount")
    size_in_bytes: int = Field(alias="sizeInBytes")
    size_in_bytes_compressed: int = Field(alias="sizeInBytesCompressed")
    unclassifiable_object_count: ObjectLevelStatisticsModel = Field(
        alias="unclassifiableObjectCount"
    )
    unclassifiable_object_size_in_bytes: ObjectLevelStatisticsModel = Field(
        alias="unclassifiableObjectSizeInBytes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetClassificationExportConfigurationResponseModel(BaseModel):
    configuration: ClassificationExportConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutClassificationExportConfigurationRequestModel(BaseModel):
    configuration: ClassificationExportConfigurationModel = Field(alias="configuration")


class PutClassificationExportConfigurationResponseModel(BaseModel):
    configuration: ClassificationExportConfigurationModel = Field(alias="configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFindingsFilterRequestModel(BaseModel):
    action: Literal["ARCHIVE", "NOOP"] = Field(alias="action")
    finding_criteria: FindingCriteriaModel = Field(alias="findingCriteria")
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    position: Optional[int] = Field(default=None, alias="position")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetFindingStatisticsRequestModel(BaseModel):
    group_by: Literal[
        "classificationDetails.jobId",
        "resourcesAffected.s3Bucket.name",
        "severity.description",
        "type",
    ] = Field(alias="groupBy")
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="findingCriteria"
    )
    size: Optional[int] = Field(default=None, alias="size")
    sort_criteria: Optional[FindingStatisticsSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class GetFindingsFilterResponseModel(BaseModel):
    action: Literal["ARCHIVE", "NOOP"] = Field(alias="action")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    finding_criteria: FindingCriteriaModel = Field(alias="findingCriteria")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    position: int = Field(alias="position")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsRequestListFindingsPaginateModel(BaseModel):
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="findingCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestModel(BaseModel):
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="findingCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class UpdateFindingsFilterRequestModel(BaseModel):
    id: str = Field(alias="id")
    action: Optional[Literal["ARCHIVE", "NOOP"]] = Field(default=None, alias="action")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="findingCriteria"
    )
    name: Optional[str] = Field(default=None, alias="name")
    position: Optional[int] = Field(default=None, alias="position")


class ListClassificationJobsRequestListClassificationJobsPaginateModel(BaseModel):
    filter_criteria: Optional[ListJobsFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    sort_criteria: Optional[ListJobsSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClassificationJobsRequestModel(BaseModel):
    filter_criteria: Optional[ListJobsFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_criteria: Optional[ListJobsSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class OccurrencesModel(BaseModel):
    cells: Optional[List[CellModel]] = Field(default=None, alias="cells")
    line_ranges: Optional[List[RangeModel]] = Field(default=None, alias="lineRanges")
    offset_ranges: Optional[List[RangeModel]] = Field(
        default=None, alias="offsetRanges"
    )
    pages: Optional[List[PageModel]] = Field(default=None, alias="pages")
    records: Optional[List[RecordModel]] = Field(default=None, alias="records")


class GetClassificationScopeResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    s3: S3ClassificationScopeModel = Field(alias="s3")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClassificationScopeRequestModel(BaseModel):
    id: str = Field(alias="id")
    s3: Optional[S3ClassificationScopeUpdateModel] = Field(default=None, alias="s3")


class SearchResourcesCriteriaModel(BaseModel):
    simple_criterion: Optional[SearchResourcesSimpleCriterionModel] = Field(
        default=None, alias="simpleCriterion"
    )
    tag_criterion: Optional[SearchResourcesTagCriterionModel] = Field(
        default=None, alias="tagCriterion"
    )


class UsageRecordModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    automated_discovery_free_trial_start_date: Optional[datetime] = Field(
        default=None, alias="automatedDiscoveryFreeTrialStartDate"
    )
    free_trial_start_date: Optional[datetime] = Field(
        default=None, alias="freeTrialStartDate"
    )
    usage: Optional[List[UsageByAccountModel]] = Field(default=None, alias="usage")


class AssumedRoleModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    arn: Optional[str] = Field(default=None, alias="arn")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    session_context: Optional[SessionContextModel] = Field(
        default=None, alias="sessionContext"
    )


class FederatedUserModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    arn: Optional[str] = Field(default=None, alias="arn")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    session_context: Optional[SessionContextModel] = Field(
        default=None, alias="sessionContext"
    )


class CriteriaForJobModel(BaseModel):
    simple_criterion: Optional[SimpleCriterionForJobModel] = Field(
        default=None, alias="simpleCriterion"
    )
    tag_criterion: Optional[TagCriterionForJobModel] = Field(
        default=None, alias="tagCriterion"
    )


class JobScopeTermModel(BaseModel):
    simple_scope_term: Optional[SimpleScopeTermModel] = Field(
        default=None, alias="simpleScopeTerm"
    )
    tag_scope_term: Optional[TagScopeTermModel] = Field(
        default=None, alias="tagScopeTerm"
    )


class BucketPublicAccessModel(BaseModel):
    effective_permission: Optional[Literal["NOT_PUBLIC", "PUBLIC", "UNKNOWN"]] = Field(
        default=None, alias="effectivePermission"
    )
    permission_configuration: Optional[BucketPermissionConfigurationModel] = Field(
        default=None, alias="permissionConfiguration"
    )


class SearchResourcesResponseModel(BaseModel):
    matching_resources: List[MatchingResourceModel] = Field(alias="matchingResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomDetectionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    count: Optional[int] = Field(default=None, alias="count")
    name: Optional[str] = Field(default=None, alias="name")
    occurrences: Optional[OccurrencesModel] = Field(default=None, alias="occurrences")


class DefaultDetectionModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    occurrences: Optional[OccurrencesModel] = Field(default=None, alias="occurrences")
    type: Optional[str] = Field(default=None, alias="type")


class SearchResourcesCriteriaBlockModel(BaseModel):
    and_: Optional[Sequence[SearchResourcesCriteriaModel]] = Field(
        default=None, alias="and"
    )


class GetUsageStatisticsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    records: List[UsageRecordModel] = Field(alias="records")
    time_range: Literal["MONTH_TO_DATE", "PAST_30_DAYS"] = Field(alias="timeRange")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserIdentityModel(BaseModel):
    assumed_role: Optional[AssumedRoleModel] = Field(default=None, alias="assumedRole")
    aws_account: Optional[AwsAccountModel] = Field(default=None, alias="awsAccount")
    aws_service: Optional[AwsServiceModel] = Field(default=None, alias="awsService")
    federated_user: Optional[FederatedUserModel] = Field(
        default=None, alias="federatedUser"
    )
    iam_user: Optional[IamUserModel] = Field(default=None, alias="iamUser")
    root: Optional[UserIdentityRootModel] = Field(default=None, alias="root")
    type: Optional[
        Literal[
            "AWSAccount",
            "AWSService",
            "AssumedRole",
            "FederatedUser",
            "IAMUser",
            "Root",
        ]
    ] = Field(default=None, alias="type")


class CriteriaBlockForJobModel(BaseModel):
    and_: Optional[Sequence[CriteriaForJobModel]] = Field(default=None, alias="and")


class JobScopingBlockModel(BaseModel):
    and_: Optional[Sequence[JobScopeTermModel]] = Field(default=None, alias="and")


class BucketMetadataModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    allows_unencrypted_object_uploads: Optional[
        Literal["FALSE", "TRUE", "UNKNOWN"]
    ] = Field(default=None, alias="allowsUnencryptedObjectUploads")
    bucket_arn: Optional[str] = Field(default=None, alias="bucketArn")
    bucket_created_at: Optional[datetime] = Field(default=None, alias="bucketCreatedAt")
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    classifiable_object_count: Optional[int] = Field(
        default=None, alias="classifiableObjectCount"
    )
    classifiable_size_in_bytes: Optional[int] = Field(
        default=None, alias="classifiableSizeInBytes"
    )
    error_code: Optional[Literal["ACCESS_DENIED"]] = Field(
        default=None, alias="errorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    job_details: Optional[JobDetailsModel] = Field(default=None, alias="jobDetails")
    last_automated_discovery_time: Optional[datetime] = Field(
        default=None, alias="lastAutomatedDiscoveryTime"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")
    object_count: Optional[int] = Field(default=None, alias="objectCount")
    object_count_by_encryption_type: Optional[ObjectCountByEncryptionTypeModel] = Field(
        default=None, alias="objectCountByEncryptionType"
    )
    public_access: Optional[BucketPublicAccessModel] = Field(
        default=None, alias="publicAccess"
    )
    region: Optional[str] = Field(default=None, alias="region")
    replication_details: Optional[ReplicationDetailsModel] = Field(
        default=None, alias="replicationDetails"
    )
    sensitivity_score: Optional[int] = Field(default=None, alias="sensitivityScore")
    server_side_encryption: Optional[BucketServerSideEncryptionModel] = Field(
        default=None, alias="serverSideEncryption"
    )
    shared_access: Optional[
        Literal["EXTERNAL", "INTERNAL", "NOT_SHARED", "UNKNOWN"]
    ] = Field(default=None, alias="sharedAccess")
    size_in_bytes: Optional[int] = Field(default=None, alias="sizeInBytes")
    size_in_bytes_compressed: Optional[int] = Field(
        default=None, alias="sizeInBytesCompressed"
    )
    tags: Optional[List[KeyValuePairModel]] = Field(default=None, alias="tags")
    unclassifiable_object_count: Optional[ObjectLevelStatisticsModel] = Field(
        default=None, alias="unclassifiableObjectCount"
    )
    unclassifiable_object_size_in_bytes: Optional[ObjectLevelStatisticsModel] = Field(
        default=None, alias="unclassifiableObjectSizeInBytes"
    )
    versioning: Optional[bool] = Field(default=None, alias="versioning")


class S3BucketModel(BaseModel):
    allows_unencrypted_object_uploads: Optional[
        Literal["FALSE", "TRUE", "UNKNOWN"]
    ] = Field(default=None, alias="allowsUnencryptedObjectUploads")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    default_server_side_encryption: Optional[ServerSideEncryptionModel] = Field(
        default=None, alias="defaultServerSideEncryption"
    )
    name: Optional[str] = Field(default=None, alias="name")
    owner: Optional[S3BucketOwnerModel] = Field(default=None, alias="owner")
    public_access: Optional[BucketPublicAccessModel] = Field(
        default=None, alias="publicAccess"
    )
    tags: Optional[List[KeyValuePairModel]] = Field(default=None, alias="tags")


class CustomDataIdentifiersModel(BaseModel):
    detections: Optional[List[CustomDetectionModel]] = Field(
        default=None, alias="detections"
    )
    total_count: Optional[int] = Field(default=None, alias="totalCount")


class SensitiveDataItemModel(BaseModel):
    category: Optional[
        Literal[
            "CREDENTIALS",
            "CUSTOM_IDENTIFIER",
            "FINANCIAL_INFORMATION",
            "PERSONAL_INFORMATION",
        ]
    ] = Field(default=None, alias="category")
    detections: Optional[List[DefaultDetectionModel]] = Field(
        default=None, alias="detections"
    )
    total_count: Optional[int] = Field(default=None, alias="totalCount")


class SearchResourcesBucketCriteriaModel(BaseModel):
    excludes: Optional[SearchResourcesCriteriaBlockModel] = Field(
        default=None, alias="excludes"
    )
    includes: Optional[SearchResourcesCriteriaBlockModel] = Field(
        default=None, alias="includes"
    )


class FindingActorModel(BaseModel):
    domain_details: Optional[DomainDetailsModel] = Field(
        default=None, alias="domainDetails"
    )
    ip_address_details: Optional[IpAddressDetailsModel] = Field(
        default=None, alias="ipAddressDetails"
    )
    user_identity: Optional[UserIdentityModel] = Field(
        default=None, alias="userIdentity"
    )


class S3BucketCriteriaForJobModel(BaseModel):
    excludes: Optional[CriteriaBlockForJobModel] = Field(default=None, alias="excludes")
    includes: Optional[CriteriaBlockForJobModel] = Field(default=None, alias="includes")


class ScopingModel(BaseModel):
    excludes: Optional[JobScopingBlockModel] = Field(default=None, alias="excludes")
    includes: Optional[JobScopingBlockModel] = Field(default=None, alias="includes")


class DescribeBucketsResponseModel(BaseModel):
    buckets: List[BucketMetadataModel] = Field(alias="buckets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourcesAffectedModel(BaseModel):
    s3_bucket: Optional[S3BucketModel] = Field(default=None, alias="s3Bucket")
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="s3Object")


class ClassificationResultModel(BaseModel):
    additional_occurrences: Optional[bool] = Field(
        default=None, alias="additionalOccurrences"
    )
    custom_data_identifiers: Optional[CustomDataIdentifiersModel] = Field(
        default=None, alias="customDataIdentifiers"
    )
    mime_type: Optional[str] = Field(default=None, alias="mimeType")
    sensitive_data: Optional[List[SensitiveDataItemModel]] = Field(
        default=None, alias="sensitiveData"
    )
    size_classified: Optional[int] = Field(default=None, alias="sizeClassified")
    status: Optional[ClassificationResultStatusModel] = Field(
        default=None, alias="status"
    )


class SearchResourcesRequestModel(BaseModel):
    bucket_criteria: Optional[SearchResourcesBucketCriteriaModel] = Field(
        default=None, alias="bucketCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_criteria: Optional[SearchResourcesSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class SearchResourcesRequestSearchResourcesPaginateModel(BaseModel):
    bucket_criteria: Optional[SearchResourcesBucketCriteriaModel] = Field(
        default=None, alias="bucketCriteria"
    )
    sort_criteria: Optional[SearchResourcesSortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PolicyDetailsModel(BaseModel):
    action: Optional[FindingActionModel] = Field(default=None, alias="action")
    actor: Optional[FindingActorModel] = Field(default=None, alias="actor")


class JobSummaryModel(BaseModel):
    bucket_criteria: Optional[S3BucketCriteriaForJobModel] = Field(
        default=None, alias="bucketCriteria"
    )
    bucket_definitions: Optional[List[S3BucketDefinitionForJobModel]] = Field(
        default=None, alias="bucketDefinitions"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    job_status: Optional[
        Literal["CANCELLED", "COMPLETE", "IDLE", "PAUSED", "RUNNING", "USER_PAUSED"]
    ] = Field(default=None, alias="jobStatus")
    job_type: Optional[Literal["ONE_TIME", "SCHEDULED"]] = Field(
        default=None, alias="jobType"
    )
    last_run_error_status: Optional[LastRunErrorStatusModel] = Field(
        default=None, alias="lastRunErrorStatus"
    )
    name: Optional[str] = Field(default=None, alias="name")
    user_paused_details: Optional[UserPausedDetailsModel] = Field(
        default=None, alias="userPausedDetails"
    )


class S3JobDefinitionModel(BaseModel):
    bucket_criteria: Optional[S3BucketCriteriaForJobModel] = Field(
        default=None, alias="bucketCriteria"
    )
    bucket_definitions: Optional[Sequence[S3BucketDefinitionForJobModel]] = Field(
        default=None, alias="bucketDefinitions"
    )
    scoping: Optional[ScopingModel] = Field(default=None, alias="scoping")


class ClassificationDetailsModel(BaseModel):
    detailed_results_location: Optional[str] = Field(
        default=None, alias="detailedResultsLocation"
    )
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    origin_type: Optional[
        Literal["AUTOMATED_SENSITIVE_DATA_DISCOVERY", "SENSITIVE_DATA_DISCOVERY_JOB"]
    ] = Field(default=None, alias="originType")
    result: Optional[ClassificationResultModel] = Field(default=None, alias="result")


class ListClassificationJobsResponseModel(BaseModel):
    items: List[JobSummaryModel] = Field(alias="items")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClassificationJobRequestModel(BaseModel):
    client_token: str = Field(alias="clientToken")
    job_type: Literal["ONE_TIME", "SCHEDULED"] = Field(alias="jobType")
    name: str = Field(alias="name")
    s3_job_definition: S3JobDefinitionModel = Field(alias="s3JobDefinition")
    allow_list_ids: Optional[Sequence[str]] = Field(default=None, alias="allowListIds")
    custom_data_identifier_ids: Optional[Sequence[str]] = Field(
        default=None, alias="customDataIdentifierIds"
    )
    description: Optional[str] = Field(default=None, alias="description")
    initial_run: Optional[bool] = Field(default=None, alias="initialRun")
    managed_data_identifier_ids: Optional[Sequence[str]] = Field(
        default=None, alias="managedDataIdentifierIds"
    )
    managed_data_identifier_selector: Optional[
        Literal["ALL", "EXCLUDE", "INCLUDE", "NONE"]
    ] = Field(default=None, alias="managedDataIdentifierSelector")
    sampling_percentage: Optional[int] = Field(default=None, alias="samplingPercentage")
    schedule_frequency: Optional[JobScheduleFrequencyModel] = Field(
        default=None, alias="scheduleFrequency"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DescribeClassificationJobResponseModel(BaseModel):
    allow_list_ids: List[str] = Field(alias="allowListIds")
    client_token: str = Field(alias="clientToken")
    created_at: datetime = Field(alias="createdAt")
    custom_data_identifier_ids: List[str] = Field(alias="customDataIdentifierIds")
    description: str = Field(alias="description")
    initial_run: bool = Field(alias="initialRun")
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    job_status: Literal[
        "CANCELLED", "COMPLETE", "IDLE", "PAUSED", "RUNNING", "USER_PAUSED"
    ] = Field(alias="jobStatus")
    job_type: Literal["ONE_TIME", "SCHEDULED"] = Field(alias="jobType")
    last_run_error_status: LastRunErrorStatusModel = Field(alias="lastRunErrorStatus")
    last_run_time: datetime = Field(alias="lastRunTime")
    managed_data_identifier_ids: List[str] = Field(alias="managedDataIdentifierIds")
    managed_data_identifier_selector: Literal[
        "ALL", "EXCLUDE", "INCLUDE", "NONE"
    ] = Field(alias="managedDataIdentifierSelector")
    name: str = Field(alias="name")
    s3_job_definition: S3JobDefinitionModel = Field(alias="s3JobDefinition")
    sampling_percentage: int = Field(alias="samplingPercentage")
    schedule_frequency: JobScheduleFrequencyModel = Field(alias="scheduleFrequency")
    statistics: StatisticsModel = Field(alias="statistics")
    tags: Dict[str, str] = Field(alias="tags")
    user_paused_details: UserPausedDetailsModel = Field(alias="userPausedDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FindingModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    archived: Optional[bool] = Field(default=None, alias="archived")
    category: Optional[Literal["CLASSIFICATION", "POLICY"]] = Field(
        default=None, alias="category"
    )
    classification_details: Optional[ClassificationDetailsModel] = Field(
        default=None, alias="classificationDetails"
    )
    count: Optional[int] = Field(default=None, alias="count")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    partition: Optional[str] = Field(default=None, alias="partition")
    policy_details: Optional[PolicyDetailsModel] = Field(
        default=None, alias="policyDetails"
    )
    region: Optional[str] = Field(default=None, alias="region")
    resources_affected: Optional[ResourcesAffectedModel] = Field(
        default=None, alias="resourcesAffected"
    )
    sample: Optional[bool] = Field(default=None, alias="sample")
    schema_version: Optional[str] = Field(default=None, alias="schemaVersion")
    severity: Optional[SeverityModel] = Field(default=None, alias="severity")
    title: Optional[str] = Field(default=None, alias="title")
    type: Optional[
        Literal[
            "Policy:IAMUser/S3BlockPublicAccessDisabled",
            "Policy:IAMUser/S3BucketEncryptionDisabled",
            "Policy:IAMUser/S3BucketPublic",
            "Policy:IAMUser/S3BucketReplicatedExternally",
            "Policy:IAMUser/S3BucketSharedExternally",
            "Policy:IAMUser/S3BucketSharedWithCloudFront",
            "SensitiveData:S3Object/Credentials",
            "SensitiveData:S3Object/CustomIdentifier",
            "SensitiveData:S3Object/Financial",
            "SensitiveData:S3Object/Multiple",
            "SensitiveData:S3Object/Personal",
        ]
    ] = Field(default=None, alias="type")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class GetFindingsResponseModel(BaseModel):
    findings: List[FindingModel] = Field(alias="findings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
