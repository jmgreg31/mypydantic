# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class SeverityCountsModel(BaseModel):
    all: Optional[int] = Field(default=None, alias="all")
    critical: Optional[int] = Field(default=None, alias="critical")
    high: Optional[int] = Field(default=None, alias="high")
    medium: Optional[int] = Field(default=None, alias="medium")


class AccountAggregationModel(BaseModel):
    finding_type: Optional[
        Literal["NETWORK_REACHABILITY", "PACKAGE_VULNERABILITY"]
    ] = Field(default=None, alias="findingType")
    resource_type: Optional[
        Literal["AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_LAMBDA_FUNCTION"]
    ] = Field(default=None, alias="resourceType")
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class StateModel(BaseModel):
    error_code: Literal[
        "ACCESS_DENIED",
        "ACCOUNT_IS_ISOLATED",
        "ALREADY_ENABLED",
        "DISABLE_IN_PROGRESS",
        "DISASSOCIATE_ALL_MEMBERS",
        "ENABLE_IN_PROGRESS",
        "EVENTBRIDGE_THROTTLED",
        "EVENTBRIDGE_UNAVAILABLE",
        "INTERNAL_ERROR",
        "RESOURCE_NOT_FOUND",
        "RESOURCE_SCAN_NOT_DISABLED",
        "SSM_THROTTLED",
        "SSM_UNAVAILABLE",
        "SUSPEND_IN_PROGRESS",
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    status: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
    ] = Field(alias="status")


class ResourceStatusModel(BaseModel):
    ec2: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
    ] = Field(alias="ec2")
    ecr: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
    ] = Field(alias="ecr")
    lambda_: Optional[
        Literal[
            "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
        ]
    ] = Field(default=None, alias="lambda")


class FindingTypeAggregationModel(BaseModel):
    finding_type: Optional[
        Literal["NETWORK_REACHABILITY", "PACKAGE_VULNERABILITY"]
    ] = Field(default=None, alias="findingType")
    resource_type: Optional[
        Literal["AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_LAMBDA_FUNCTION"]
    ] = Field(default=None, alias="resourceType")
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class StringFilterModel(BaseModel):
    comparison: Literal["EQUALS", "NOT_EQUALS", "PREFIX"] = Field(alias="comparison")
    value: str = Field(alias="value")


class AssociateMemberRequestModel(BaseModel):
    account_id: str = Field(alias="accountId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AutoEnableModel(BaseModel):
    ec2: bool = Field(alias="ec2")
    ecr: bool = Field(alias="ecr")
    lambda_: Optional[bool] = Field(default=None, alias="lambda")


class AwsEc2InstanceDetailsModel(BaseModel):
    iam_instance_profile_arn: Optional[str] = Field(
        default=None, alias="iamInstanceProfileArn"
    )
    image_id: Optional[str] = Field(default=None, alias="imageId")
    ip_v4_addresses: Optional[List[str]] = Field(default=None, alias="ipV4Addresses")
    ip_v6_addresses: Optional[List[str]] = Field(default=None, alias="ipV6Addresses")
    key_name: Optional[str] = Field(default=None, alias="keyName")
    launched_at: Optional[datetime] = Field(default=None, alias="launchedAt")
    platform: Optional[str] = Field(default=None, alias="platform")
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    type: Optional[str] = Field(default=None, alias="type")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class AwsEcrContainerImageDetailsModel(BaseModel):
    image_hash: str = Field(alias="imageHash")
    registry: str = Field(alias="registry")
    repository_name: str = Field(alias="repositoryName")
    architecture: Optional[str] = Field(default=None, alias="architecture")
    author: Optional[str] = Field(default=None, alias="author")
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    platform: Optional[str] = Field(default=None, alias="platform")
    pushed_at: Optional[datetime] = Field(default=None, alias="pushedAt")


class LambdaVpcConfigModel(BaseModel):
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class BatchGetAccountStatusRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")


class BatchGetFreeTrialInfoRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="accountIds")


class FreeTrialInfoErrorModel(BaseModel):
    account_id: str = Field(alias="accountId")
    code: Literal["ACCESS_DENIED", "INTERNAL_ERROR"] = Field(alias="code")
    message: str = Field(alias="message")


class CancelFindingsReportRequestModel(BaseModel):
    report_id: str = Field(alias="reportId")


class CountsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    group_key: Optional[
        Literal[
            "ACCOUNT_ID",
            "ECR_REPOSITORY_NAME",
            "RESOURCE_TYPE",
            "SCAN_STATUS_CODE",
            "SCAN_STATUS_REASON",
        ]
    ] = Field(default=None, alias="groupKey")


class CoverageMapFilterModel(BaseModel):
    comparison: Literal["EQUALS"] = Field(alias="comparison")
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class CoverageStringFilterModel(BaseModel):
    comparison: Literal["EQUALS", "NOT_EQUALS"] = Field(alias="comparison")
    value: str = Field(alias="value")


class ScanStatusModel(BaseModel):
    reason: Literal[
        "ACCESS_DENIED",
        "EC2_INSTANCE_STOPPED",
        "EXCLUDED_BY_TAG",
        "IMAGE_SIZE_EXCEEDED",
        "INTERNAL_ERROR",
        "NO_INVENTORY",
        "NO_RESOURCES_FOUND",
        "PENDING_DISABLE",
        "PENDING_INITIAL_SCAN",
        "RESOURCE_TERMINATED",
        "SCAN_ELIGIBILITY_EXPIRED",
        "SCAN_FREQUENCY_MANUAL",
        "SCAN_FREQUENCY_SCAN_ON_PUSH",
        "STALE_INVENTORY",
        "SUCCESSFUL",
        "UNMANAGED_EC2_INSTANCE",
        "UNSUPPORTED_OS",
        "UNSUPPORTED_RUNTIME",
    ] = Field(alias="reason")
    status_code: Literal["ACTIVE", "INACTIVE"] = Field(alias="statusCode")


class DestinationModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    kms_key_arn: str = Field(alias="kmsKeyArn")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class CvssScoreAdjustmentModel(BaseModel):
    metric: str = Field(alias="metric")
    reason: str = Field(alias="reason")


class CvssScoreModel(BaseModel):
    base_score: float = Field(alias="baseScore")
    scoring_vector: str = Field(alias="scoringVector")
    source: str = Field(alias="source")
    version: str = Field(alias="version")


class DateFilterModel(BaseModel):
    end_inclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="endInclusive"
    )
    start_inclusive: Optional[Union[datetime, str]] = Field(
        default=None, alias="startInclusive"
    )


class DelegatedAdminAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    status: Optional[Literal["DISABLE_IN_PROGRESS", "ENABLED"]] = Field(
        default=None, alias="status"
    )


class DelegatedAdminModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    relationship_status: Optional[
        Literal[
            "ACCOUNT_SUSPENDED",
            "CANNOT_CREATE_DETECTOR_IN_ORG_MASTER",
            "CREATED",
            "DELETED",
            "DISABLED",
            "EMAIL_VERIFICATION_FAILED",
            "EMAIL_VERIFICATION_IN_PROGRESS",
            "ENABLED",
            "INVITED",
            "REGION_DISABLED",
            "REMOVED",
            "RESIGNED",
        ]
    ] = Field(default=None, alias="relationshipStatus")


class DeleteFilterRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DisableDelegatedAdminAccountRequestModel(BaseModel):
    delegated_admin_account_id: str = Field(alias="delegatedAdminAccountId")


class DisableRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    resource_types: Optional[Sequence[Literal["EC2", "ECR", "LAMBDA"]]] = Field(
        default=None, alias="resourceTypes"
    )


class DisassociateMemberRequestModel(BaseModel):
    account_id: str = Field(alias="accountId")


class MapFilterModel(BaseModel):
    comparison: Literal["EQUALS"] = Field(alias="comparison")
    key: str = Field(alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class Ec2MetadataModel(BaseModel):
    ami_id: Optional[str] = Field(default=None, alias="amiId")
    platform: Optional[Literal["LINUX", "UNKNOWN", "WINDOWS"]] = Field(
        default=None, alias="platform"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class EcrRescanDurationStateModel(BaseModel):
    rescan_duration: Optional[Literal["DAYS_180", "DAYS_30", "LIFETIME"]] = Field(
        default=None, alias="rescanDuration"
    )
    status: Optional[Literal["FAILED", "PENDING", "SUCCESS"]] = Field(
        default=None, alias="status"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class EcrConfigurationModel(BaseModel):
    rescan_duration: Literal["DAYS_180", "DAYS_30", "LIFETIME"] = Field(
        alias="rescanDuration"
    )


class EcrContainerImageMetadataModel(BaseModel):
    tags: Optional[List[str]] = Field(default=None, alias="tags")


class EcrRepositoryMetadataModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    scan_frequency: Optional[
        Literal["CONTINUOUS_SCAN", "MANUAL", "SCAN_ON_PUSH"]
    ] = Field(default=None, alias="scanFrequency")


class EnableDelegatedAdminAccountRequestModel(BaseModel):
    delegated_admin_account_id: str = Field(alias="delegatedAdminAccountId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class EnableRequestModel(BaseModel):
    resource_types: Sequence[Literal["EC2", "ECR", "LAMBDA"]] = Field(
        alias="resourceTypes"
    )
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ExploitabilityDetailsModel(BaseModel):
    last_known_exploit_at: Optional[datetime] = Field(
        default=None, alias="lastKnownExploitAt"
    )


class NumberFilterModel(BaseModel):
    lower_inclusive: Optional[float] = Field(default=None, alias="lowerInclusive")
    upper_inclusive: Optional[float] = Field(default=None, alias="upperInclusive")


class PortRangeFilterModel(BaseModel):
    begin_inclusive: Optional[int] = Field(default=None, alias="beginInclusive")
    end_inclusive: Optional[int] = Field(default=None, alias="endInclusive")


class FreeTrialInfoModel(BaseModel):
    end: datetime = Field(alias="end")
    start: datetime = Field(alias="start")
    status: Literal["ACTIVE", "INACTIVE"] = Field(alias="status")
    type: Literal["EC2", "ECR", "LAMBDA"] = Field(alias="type")


class GetFindingsReportStatusRequestModel(BaseModel):
    report_id: Optional[str] = Field(default=None, alias="reportId")


class GetMemberRequestModel(BaseModel):
    account_id: str = Field(alias="accountId")


class MemberModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    delegated_admin_account_id: Optional[str] = Field(
        default=None, alias="delegatedAdminAccountId"
    )
    relationship_status: Optional[
        Literal[
            "ACCOUNT_SUSPENDED",
            "CANNOT_CREATE_DETECTOR_IN_ORG_MASTER",
            "CREATED",
            "DELETED",
            "DISABLED",
            "EMAIL_VERIFICATION_FAILED",
            "EMAIL_VERIFICATION_IN_PROGRESS",
            "ENABLED",
            "INVITED",
            "REGION_DISABLED",
            "REMOVED",
            "RESIGNED",
        ]
    ] = Field(default=None, alias="relationshipStatus")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class LambdaFunctionMetadataModel(BaseModel):
    function_name: Optional[str] = Field(default=None, alias="functionName")
    function_tags: Optional[Dict[str, str]] = Field(default=None, alias="functionTags")
    layers: Optional[List[str]] = Field(default=None, alias="layers")
    runtime: Optional[
        Literal[
            "GO_1_X",
            "JAVA_11",
            "JAVA_8",
            "JAVA_8_AL2",
            "NODEJS",
            "NODEJS_12_X",
            "NODEJS_14_X",
            "NODEJS_16_X",
            "NODEJS_18_X",
            "PYTHON_3_7",
            "PYTHON_3_8",
            "PYTHON_3_9",
            "UNSUPPORTED",
        ]
    ] = Field(default=None, alias="runtime")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccountPermissionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    service: Optional[Literal["EC2", "ECR", "LAMBDA"]] = Field(
        default=None, alias="service"
    )


class PermissionModel(BaseModel):
    operation: Literal[
        "DISABLE_REPOSITORY", "DISABLE_SCANNING", "ENABLE_REPOSITORY", "ENABLE_SCANNING"
    ] = Field(alias="operation")
    service: Literal["EC2", "ECR", "LAMBDA"] = Field(alias="service")


class ListDelegatedAdminAccountsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListFiltersRequestModel(BaseModel):
    action: Optional[Literal["NONE", "SUPPRESS"]] = Field(default=None, alias="action")
    arns: Optional[Sequence[str]] = Field(default=None, alias="arns")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SortCriteriaModel(BaseModel):
    field: Literal[
        "AWS_ACCOUNT_ID",
        "COMPONENT_TYPE",
        "ECR_IMAGE_PUSHED_AT",
        "ECR_IMAGE_REGISTRY",
        "ECR_IMAGE_REPOSITORY_NAME",
        "FINDING_STATUS",
        "FINDING_TYPE",
        "FIRST_OBSERVED_AT",
        "INSPECTOR_SCORE",
        "LAST_OBSERVED_AT",
        "NETWORK_PROTOCOL",
        "RESOURCE_TYPE",
        "SEVERITY",
        "VENDOR_SEVERITY",
        "VULNERABILITY_ID",
        "VULNERABILITY_SOURCE",
    ] = Field(alias="field")
    sort_order: Literal["ASC", "DESC"] = Field(alias="sortOrder")


class ListMembersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    only_associated: Optional[bool] = Field(default=None, alias="onlyAssociated")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListUsageTotalsRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StepModel(BaseModel):
    component_id: str = Field(alias="componentId")
    component_type: str = Field(alias="componentType")


class PortRangeModel(BaseModel):
    begin: int = Field(alias="begin")
    end: int = Field(alias="end")


class VulnerablePackageModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    arch: Optional[str] = Field(default=None, alias="arch")
    epoch: Optional[int] = Field(default=None, alias="epoch")
    file_path: Optional[str] = Field(default=None, alias="filePath")
    fixed_in_version: Optional[str] = Field(default=None, alias="fixedInVersion")
    package_manager: Optional[
        Literal[
            "BUNDLER",
            "CARGO",
            "COMPOSER",
            "GOBINARY",
            "GOMOD",
            "JAR",
            "NODEPKG",
            "NPM",
            "NUGET",
            "OS",
            "PIP",
            "PIPENV",
            "POETRY",
            "POM",
            "PYTHONPKG",
            "YARN",
        ]
    ] = Field(default=None, alias="packageManager")
    release: Optional[str] = Field(default=None, alias="release")
    remediation: Optional[str] = Field(default=None, alias="remediation")
    source_lambda_layer_arn: Optional[str] = Field(
        default=None, alias="sourceLambdaLayerArn"
    )
    source_layer_hash: Optional[str] = Field(default=None, alias="sourceLayerHash")


class RecommendationModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    text: Optional[str] = Field(default=None, alias="text")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UsageModel(BaseModel):
    currency: Optional[Literal["USD"]] = Field(default=None, alias="currency")
    estimated_monthly_cost: Optional[float] = Field(
        default=None, alias="estimatedMonthlyCost"
    )
    total: Optional[float] = Field(default=None, alias="total")
    type: Optional[
        Literal[
            "EC2_INSTANCE_HOURS",
            "ECR_INITIAL_SCAN",
            "ECR_RESCAN",
            "LAMBDA_FUNCTION_HOURS",
        ]
    ] = Field(default=None, alias="type")


class AccountAggregationResponseModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class AmiAggregationResponseModel(BaseModel):
    ami: str = Field(alias="ami")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    affected_instances: Optional[int] = Field(default=None, alias="affectedInstances")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class AwsEcrContainerAggregationResponseModel(BaseModel):
    resource_id: str = Field(alias="resourceId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    architecture: Optional[str] = Field(default=None, alias="architecture")
    image_sha: Optional[str] = Field(default=None, alias="imageSha")
    image_tags: Optional[List[str]] = Field(default=None, alias="imageTags")
    repository: Optional[str] = Field(default=None, alias="repository")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class Ec2InstanceAggregationResponseModel(BaseModel):
    instance_id: str = Field(alias="instanceId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    ami: Optional[str] = Field(default=None, alias="ami")
    instance_tags: Optional[Dict[str, str]] = Field(default=None, alias="instanceTags")
    network_findings: Optional[int] = Field(default=None, alias="networkFindings")
    operating_system: Optional[str] = Field(default=None, alias="operatingSystem")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class FindingTypeAggregationResponseModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class ImageLayerAggregationResponseModel(BaseModel):
    account_id: str = Field(alias="accountId")
    layer_hash: str = Field(alias="layerHash")
    repository: str = Field(alias="repository")
    resource_id: str = Field(alias="resourceId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class LambdaFunctionAggregationResponseModel(BaseModel):
    resource_id: str = Field(alias="resourceId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    function_name: Optional[str] = Field(default=None, alias="functionName")
    lambda_tags: Optional[Dict[str, str]] = Field(default=None, alias="lambdaTags")
    last_modified_at: Optional[datetime] = Field(default=None, alias="lastModifiedAt")
    runtime: Optional[str] = Field(default=None, alias="runtime")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class LambdaLayerAggregationResponseModel(BaseModel):
    account_id: str = Field(alias="accountId")
    function_name: str = Field(alias="functionName")
    layer_arn: str = Field(alias="layerArn")
    resource_id: str = Field(alias="resourceId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class PackageAggregationResponseModel(BaseModel):
    package_name: str = Field(alias="packageName")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class RepositoryAggregationResponseModel(BaseModel):
    repository: str = Field(alias="repository")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    affected_images: Optional[int] = Field(default=None, alias="affectedImages")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )


class TitleAggregationResponseModel(BaseModel):
    title: str = Field(alias="title")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    severity_counts: Optional[SeverityCountsModel] = Field(
        default=None, alias="severityCounts"
    )
    vulnerability_id: Optional[str] = Field(default=None, alias="vulnerabilityId")


class ResourceStateModel(BaseModel):
    ec2: StateModel = Field(alias="ec2")
    ecr: StateModel = Field(alias="ecr")
    lambda_: Optional[StateModel] = Field(default=None, alias="lambda")


class AccountModel(BaseModel):
    account_id: str = Field(alias="accountId")
    resource_status: ResourceStatusModel = Field(alias="resourceStatus")
    status: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
    ] = Field(alias="status")


class FailedAccountModel(BaseModel):
    account_id: str = Field(alias="accountId")
    error_code: Literal[
        "ACCESS_DENIED",
        "ACCOUNT_IS_ISOLATED",
        "ALREADY_ENABLED",
        "DISABLE_IN_PROGRESS",
        "DISASSOCIATE_ALL_MEMBERS",
        "ENABLE_IN_PROGRESS",
        "EVENTBRIDGE_THROTTLED",
        "EVENTBRIDGE_UNAVAILABLE",
        "INTERNAL_ERROR",
        "RESOURCE_NOT_FOUND",
        "RESOURCE_SCAN_NOT_DISABLED",
        "SSM_THROTTLED",
        "SSM_UNAVAILABLE",
        "SUSPEND_IN_PROGRESS",
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    resource_status: Optional[ResourceStatusModel] = Field(
        default=None, alias="resourceStatus"
    )
    status: Optional[
        Literal[
            "DISABLED", "DISABLING", "ENABLED", "ENABLING", "SUSPENDED", "SUSPENDING"
        ]
    ] = Field(default=None, alias="status")


class AmiAggregationModel(BaseModel):
    amis: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="amis")
    sort_by: Optional[Literal["AFFECTED_INSTANCES", "ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class AwsEcrContainerAggregationModel(BaseModel):
    architectures: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="architectures"
    )
    image_shas: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="imageShas"
    )
    image_tags: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="imageTags"
    )
    repositories: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="repositories"
    )
    resource_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceIds"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class ImageLayerAggregationModel(BaseModel):
    layer_hashes: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="layerHashes"
    )
    repositories: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="repositories"
    )
    resource_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceIds"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class LambdaLayerAggregationModel(BaseModel):
    function_names: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="functionNames"
    )
    layer_arns: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="layerArns"
    )
    resource_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceIds"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class PackageAggregationModel(BaseModel):
    package_names: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="packageNames"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class RepositoryAggregationModel(BaseModel):
    repositories: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="repositories"
    )
    sort_by: Optional[Literal["AFFECTED_IMAGES", "ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class TitleAggregationModel(BaseModel):
    resource_type: Optional[
        Literal["AWS_EC2_INSTANCE", "AWS_ECR_CONTAINER_IMAGE", "AWS_LAMBDA_FUNCTION"]
    ] = Field(default=None, alias="resourceType")
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )
    titles: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="titles")
    vulnerability_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="vulnerabilityIds"
    )


class AssociateMemberResponseModel(BaseModel):
    account_id: str = Field(alias="accountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelFindingsReportResponseModel(BaseModel):
    report_id: str = Field(alias="reportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFilterResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFindingsReportResponseModel(BaseModel):
    report_id: str = Field(alias="reportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFilterResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableDelegatedAdminAccountResponseModel(BaseModel):
    delegated_admin_account_id: str = Field(alias="delegatedAdminAccountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateMemberResponseModel(BaseModel):
    account_id: str = Field(alias="accountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableDelegatedAdminAccountResponseModel(BaseModel):
    delegated_admin_account_id: str = Field(alias="delegatedAdminAccountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFilterResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: AutoEnableModel = Field(alias="autoEnable")
    max_account_limit_reached: bool = Field(alias="maxAccountLimitReached")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOrganizationConfigurationRequestModel(BaseModel):
    auto_enable: AutoEnableModel = Field(alias="autoEnable")


class UpdateOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: AutoEnableModel = Field(alias="autoEnable")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AwsLambdaFunctionDetailsModel(BaseModel):
    code_sha256: str = Field(alias="codeSha256")
    execution_role_arn: str = Field(alias="executionRoleArn")
    function_name: str = Field(alias="functionName")
    runtime: Literal[
        "GO_1_X",
        "JAVA_11",
        "JAVA_8",
        "JAVA_8_AL2",
        "NODEJS",
        "NODEJS_12_X",
        "NODEJS_14_X",
        "NODEJS_16_X",
        "NODEJS_18_X",
        "PYTHON_3_7",
        "PYTHON_3_8",
        "PYTHON_3_9",
        "UNSUPPORTED",
    ] = Field(alias="runtime")
    version: str = Field(alias="version")
    architectures: Optional[List[Literal["ARM64", "X86_64"]]] = Field(
        default=None, alias="architectures"
    )
    last_modified_at: Optional[datetime] = Field(default=None, alias="lastModifiedAt")
    layers: Optional[List[str]] = Field(default=None, alias="layers")
    package_type: Optional[Literal["IMAGE", "ZIP"]] = Field(
        default=None, alias="packageType"
    )
    vpc_config: Optional[LambdaVpcConfigModel] = Field(default=None, alias="vpcConfig")


class ListCoverageStatisticsResponseModel(BaseModel):
    counts_by_group: List[CountsModel] = Field(alias="countsByGroup")
    next_token: str = Field(alias="nextToken")
    total_counts: int = Field(alias="totalCounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CoverageFilterCriteriaModel(BaseModel):
    account_id: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="accountId"
    )
    ec2_instance_tags: Optional[Sequence[CoverageMapFilterModel]] = Field(
        default=None, alias="ec2InstanceTags"
    )
    ecr_image_tags: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="ecrImageTags"
    )
    ecr_repository_name: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="ecrRepositoryName"
    )
    lambda_function_name: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="lambdaFunctionName"
    )
    lambda_function_runtime: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="lambdaFunctionRuntime"
    )
    lambda_function_tags: Optional[Sequence[CoverageMapFilterModel]] = Field(
        default=None, alias="lambdaFunctionTags"
    )
    resource_id: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="resourceId"
    )
    resource_type: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="resourceType"
    )
    scan_status_code: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="scanStatusCode"
    )
    scan_status_reason: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="scanStatusReason"
    )
    scan_type: Optional[Sequence[CoverageStringFilterModel]] = Field(
        default=None, alias="scanType"
    )


class CvssScoreDetailsModel(BaseModel):
    score: float = Field(alias="score")
    score_source: str = Field(alias="scoreSource")
    scoring_vector: str = Field(alias="scoringVector")
    version: str = Field(alias="version")
    adjustments: Optional[List[CvssScoreAdjustmentModel]] = Field(
        default=None, alias="adjustments"
    )
    cvss_source: Optional[str] = Field(default=None, alias="cvssSource")


class ListDelegatedAdminAccountsResponseModel(BaseModel):
    delegated_admin_accounts: List[DelegatedAdminAccountModel] = Field(
        alias="delegatedAdminAccounts"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDelegatedAdminAccountResponseModel(BaseModel):
    delegated_admin: DelegatedAdminModel = Field(alias="delegatedAdmin")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class Ec2InstanceAggregationModel(BaseModel):
    amis: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="amis")
    instance_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="instanceIds"
    )
    instance_tags: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="instanceTags"
    )
    operating_systems: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="operatingSystems"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH", "NETWORK_FINDINGS"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class LambdaFunctionAggregationModel(BaseModel):
    function_names: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="functionNames"
    )
    function_tags: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="functionTags"
    )
    resource_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceIds"
    )
    runtimes: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="runtimes"
    )
    sort_by: Optional[Literal["ALL", "CRITICAL", "HIGH"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class EcrConfigurationStateModel(BaseModel):
    rescan_duration_state: Optional[EcrRescanDurationStateModel] = Field(
        default=None, alias="rescanDurationState"
    )


class UpdateConfigurationRequestModel(BaseModel):
    ecr_configuration: EcrConfigurationModel = Field(alias="ecrConfiguration")


class PackageFilterModel(BaseModel):
    architecture: Optional[StringFilterModel] = Field(
        default=None, alias="architecture"
    )
    epoch: Optional[NumberFilterModel] = Field(default=None, alias="epoch")
    name: Optional[StringFilterModel] = Field(default=None, alias="name")
    release: Optional[StringFilterModel] = Field(default=None, alias="release")
    source_lambda_layer_arn: Optional[StringFilterModel] = Field(
        default=None, alias="sourceLambdaLayerArn"
    )
    source_layer_hash: Optional[StringFilterModel] = Field(
        default=None, alias="sourceLayerHash"
    )
    version: Optional[StringFilterModel] = Field(default=None, alias="version")


class FreeTrialAccountInfoModel(BaseModel):
    account_id: str = Field(alias="accountId")
    free_trial_info: List[FreeTrialInfoModel] = Field(alias="freeTrialInfo")


class GetMemberResponseModel(BaseModel):
    member: MemberModel = Field(alias="member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="members")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceScanMetadataModel(BaseModel):
    ec2: Optional[Ec2MetadataModel] = Field(default=None, alias="ec2")
    ecr_image: Optional[EcrContainerImageMetadataModel] = Field(
        default=None, alias="ecrImage"
    )
    ecr_repository: Optional[EcrRepositoryMetadataModel] = Field(
        default=None, alias="ecrRepository"
    )
    lambda_function: Optional[LambdaFunctionMetadataModel] = Field(
        default=None, alias="lambdaFunction"
    )


class ListAccountPermissionsRequestListAccountPermissionsPaginateModel(BaseModel):
    service: Optional[Literal["EC2", "ECR", "LAMBDA"]] = Field(
        default=None, alias="service"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFiltersRequestListFiltersPaginateModel(BaseModel):
    action: Optional[Literal["NONE", "SUPPRESS"]] = Field(default=None, alias="action")
    arns: Optional[Sequence[str]] = Field(default=None, alias="arns")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersRequestListMembersPaginateModel(BaseModel):
    only_associated: Optional[bool] = Field(default=None, alias="onlyAssociated")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsageTotalsRequestListUsageTotalsPaginateModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountPermissionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    permissions: List[PermissionModel] = Field(alias="permissions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkPathModel(BaseModel):
    steps: Optional[List[StepModel]] = Field(default=None, alias="steps")


class PackageVulnerabilityDetailsModel(BaseModel):
    source: str = Field(alias="source")
    vulnerability_id: str = Field(alias="vulnerabilityId")
    cvss: Optional[List[CvssScoreModel]] = Field(default=None, alias="cvss")
    reference_urls: Optional[List[str]] = Field(default=None, alias="referenceUrls")
    related_vulnerabilities: Optional[List[str]] = Field(
        default=None, alias="relatedVulnerabilities"
    )
    source_url: Optional[str] = Field(default=None, alias="sourceUrl")
    vendor_created_at: Optional[datetime] = Field(default=None, alias="vendorCreatedAt")
    vendor_severity: Optional[str] = Field(default=None, alias="vendorSeverity")
    vendor_updated_at: Optional[datetime] = Field(default=None, alias="vendorUpdatedAt")
    vulnerable_packages: Optional[List[VulnerablePackageModel]] = Field(
        default=None, alias="vulnerablePackages"
    )


class RemediationModel(BaseModel):
    recommendation: Optional[RecommendationModel] = Field(
        default=None, alias="recommendation"
    )


class UsageTotalModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    usage: Optional[List[UsageModel]] = Field(default=None, alias="usage")


class AggregationResponseModel(BaseModel):
    account_aggregation: Optional[AccountAggregationResponseModel] = Field(
        default=None, alias="accountAggregation"
    )
    ami_aggregation: Optional[AmiAggregationResponseModel] = Field(
        default=None, alias="amiAggregation"
    )
    aws_ecr_container_aggregation: Optional[
        AwsEcrContainerAggregationResponseModel
    ] = Field(default=None, alias="awsEcrContainerAggregation")
    ec2_instance_aggregation: Optional[Ec2InstanceAggregationResponseModel] = Field(
        default=None, alias="ec2InstanceAggregation"
    )
    finding_type_aggregation: Optional[FindingTypeAggregationResponseModel] = Field(
        default=None, alias="findingTypeAggregation"
    )
    image_layer_aggregation: Optional[ImageLayerAggregationResponseModel] = Field(
        default=None, alias="imageLayerAggregation"
    )
    lambda_function_aggregation: Optional[
        LambdaFunctionAggregationResponseModel
    ] = Field(default=None, alias="lambdaFunctionAggregation")
    lambda_layer_aggregation: Optional[LambdaLayerAggregationResponseModel] = Field(
        default=None, alias="lambdaLayerAggregation"
    )
    package_aggregation: Optional[PackageAggregationResponseModel] = Field(
        default=None, alias="packageAggregation"
    )
    repository_aggregation: Optional[RepositoryAggregationResponseModel] = Field(
        default=None, alias="repositoryAggregation"
    )
    title_aggregation: Optional[TitleAggregationResponseModel] = Field(
        default=None, alias="titleAggregation"
    )


class AccountStateModel(BaseModel):
    account_id: str = Field(alias="accountId")
    resource_state: ResourceStateModel = Field(alias="resourceState")
    state: StateModel = Field(alias="state")


class DisableResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="accounts")
    failed_accounts: List[FailedAccountModel] = Field(alias="failedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="accounts")
    failed_accounts: List[FailedAccountModel] = Field(alias="failedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceDetailsModel(BaseModel):
    aws_ec2_instance: Optional[AwsEc2InstanceDetailsModel] = Field(
        default=None, alias="awsEc2Instance"
    )
    aws_ecr_container_image: Optional[AwsEcrContainerImageDetailsModel] = Field(
        default=None, alias="awsEcrContainerImage"
    )
    aws_lambda_function: Optional[AwsLambdaFunctionDetailsModel] = Field(
        default=None, alias="awsLambdaFunction"
    )


class ListCoverageRequestListCoveragePaginateModel(BaseModel):
    filter_criteria: Optional[CoverageFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoverageRequestModel(BaseModel):
    filter_criteria: Optional[CoverageFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCoverageStatisticsRequestListCoverageStatisticsPaginateModel(BaseModel):
    filter_criteria: Optional[CoverageFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    group_by: Optional[
        Literal[
            "ACCOUNT_ID",
            "ECR_REPOSITORY_NAME",
            "RESOURCE_TYPE",
            "SCAN_STATUS_CODE",
            "SCAN_STATUS_REASON",
        ]
    ] = Field(default=None, alias="groupBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoverageStatisticsRequestModel(BaseModel):
    filter_criteria: Optional[CoverageFilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    group_by: Optional[
        Literal[
            "ACCOUNT_ID",
            "ECR_REPOSITORY_NAME",
            "RESOURCE_TYPE",
            "SCAN_STATUS_CODE",
            "SCAN_STATUS_REASON",
        ]
    ] = Field(default=None, alias="groupBy")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class InspectorScoreDetailsModel(BaseModel):
    adjusted_cvss: Optional[CvssScoreDetailsModel] = Field(
        default=None, alias="adjustedCvss"
    )


class AggregationRequestModel(BaseModel):
    account_aggregation: Optional[AccountAggregationModel] = Field(
        default=None, alias="accountAggregation"
    )
    ami_aggregation: Optional[AmiAggregationModel] = Field(
        default=None, alias="amiAggregation"
    )
    aws_ecr_container_aggregation: Optional[AwsEcrContainerAggregationModel] = Field(
        default=None, alias="awsEcrContainerAggregation"
    )
    ec2_instance_aggregation: Optional[Ec2InstanceAggregationModel] = Field(
        default=None, alias="ec2InstanceAggregation"
    )
    finding_type_aggregation: Optional[FindingTypeAggregationModel] = Field(
        default=None, alias="findingTypeAggregation"
    )
    image_layer_aggregation: Optional[ImageLayerAggregationModel] = Field(
        default=None, alias="imageLayerAggregation"
    )
    lambda_function_aggregation: Optional[LambdaFunctionAggregationModel] = Field(
        default=None, alias="lambdaFunctionAggregation"
    )
    lambda_layer_aggregation: Optional[LambdaLayerAggregationModel] = Field(
        default=None, alias="lambdaLayerAggregation"
    )
    package_aggregation: Optional[PackageAggregationModel] = Field(
        default=None, alias="packageAggregation"
    )
    repository_aggregation: Optional[RepositoryAggregationModel] = Field(
        default=None, alias="repositoryAggregation"
    )
    title_aggregation: Optional[TitleAggregationModel] = Field(
        default=None, alias="titleAggregation"
    )


class GetConfigurationResponseModel(BaseModel):
    ecr_configuration: EcrConfigurationStateModel = Field(alias="ecrConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FilterCriteriaModel(BaseModel):
    aws_account_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="awsAccountId"
    )
    component_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="componentId"
    )
    component_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="componentType"
    )
    ec2_instance_image_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ec2InstanceImageId"
    )
    ec2_instance_subnet_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ec2InstanceSubnetId"
    )
    ec2_instance_vpc_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ec2InstanceVpcId"
    )
    ecr_image_architecture: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ecrImageArchitecture"
    )
    ecr_image_hash: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ecrImageHash"
    )
    ecr_image_pushed_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ecrImagePushedAt"
    )
    ecr_image_registry: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ecrImageRegistry"
    )
    ecr_image_repository_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ecrImageRepositoryName"
    )
    ecr_image_tags: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ecrImageTags"
    )
    exploit_available: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="exploitAvailable"
    )
    finding_arn: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="findingArn"
    )
    finding_status: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="findingStatus"
    )
    finding_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="findingType"
    )
    first_observed_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="firstObservedAt"
    )
    fix_available: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="fixAvailable"
    )
    inspector_score: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="inspectorScore"
    )
    lambda_function_execution_role_arn: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="lambdaFunctionExecutionRoleArn"
    )
    lambda_function_last_modified_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="lambdaFunctionLastModifiedAt"
    )
    lambda_function_layers: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="lambdaFunctionLayers"
    )
    lambda_function_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="lambdaFunctionName"
    )
    lambda_function_runtime: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="lambdaFunctionRuntime"
    )
    last_observed_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="lastObservedAt"
    )
    network_protocol: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="networkProtocol"
    )
    port_range: Optional[Sequence[PortRangeFilterModel]] = Field(
        default=None, alias="portRange"
    )
    related_vulnerabilities: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="relatedVulnerabilities"
    )
    resource_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceId"
    )
    resource_tags: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="resourceTags"
    )
    resource_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="resourceType"
    )
    severity: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="severity"
    )
    title: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="title")
    updated_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="updatedAt"
    )
    vendor_severity: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="vendorSeverity"
    )
    vulnerability_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="vulnerabilityId"
    )
    vulnerability_source: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="vulnerabilitySource"
    )
    vulnerable_packages: Optional[Sequence[PackageFilterModel]] = Field(
        default=None, alias="vulnerablePackages"
    )


class BatchGetFreeTrialInfoResponseModel(BaseModel):
    accounts: List[FreeTrialAccountInfoModel] = Field(alias="accounts")
    failed_accounts: List[FreeTrialInfoErrorModel] = Field(alias="failedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CoveredResourceModel(BaseModel):
    account_id: str = Field(alias="accountId")
    resource_id: str = Field(alias="resourceId")
    resource_type: Literal[
        "AWS_EC2_INSTANCE",
        "AWS_ECR_CONTAINER_IMAGE",
        "AWS_ECR_REPOSITORY",
        "AWS_LAMBDA_FUNCTION",
    ] = Field(alias="resourceType")
    scan_type: Literal["NETWORK", "PACKAGE"] = Field(alias="scanType")
    resource_metadata: Optional[ResourceScanMetadataModel] = Field(
        default=None, alias="resourceMetadata"
    )
    scan_status: Optional[ScanStatusModel] = Field(default=None, alias="scanStatus")


class NetworkReachabilityDetailsModel(BaseModel):
    network_path: NetworkPathModel = Field(alias="networkPath")
    open_port_range: PortRangeModel = Field(alias="openPortRange")
    protocol: Literal["TCP", "UDP"] = Field(alias="protocol")


class ListUsageTotalsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    totals: List[UsageTotalModel] = Field(alias="totals")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingAggregationsResponseModel(BaseModel):
    aggregation_type: Literal[
        "ACCOUNT",
        "AMI",
        "AWS_EC2_INSTANCE",
        "AWS_ECR_CONTAINER",
        "AWS_LAMBDA_FUNCTION",
        "FINDING_TYPE",
        "IMAGE_LAYER",
        "LAMBDA_LAYER",
        "PACKAGE",
        "REPOSITORY",
        "TITLE",
    ] = Field(alias="aggregationType")
    next_token: str = Field(alias="nextToken")
    responses: List[AggregationResponseModel] = Field(alias="responses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetAccountStatusResponseModel(BaseModel):
    accounts: List[AccountStateModel] = Field(alias="accounts")
    failed_accounts: List[FailedAccountModel] = Field(alias="failedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceModel(BaseModel):
    id: str = Field(alias="id")
    type: Literal[
        "AWS_EC2_INSTANCE",
        "AWS_ECR_CONTAINER_IMAGE",
        "AWS_ECR_REPOSITORY",
        "AWS_LAMBDA_FUNCTION",
    ] = Field(alias="type")
    details: Optional[ResourceDetailsModel] = Field(default=None, alias="details")
    partition: Optional[str] = Field(default=None, alias="partition")
    region: Optional[str] = Field(default=None, alias="region")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListFindingAggregationsRequestListFindingAggregationsPaginateModel(BaseModel):
    aggregation_type: Literal[
        "ACCOUNT",
        "AMI",
        "AWS_EC2_INSTANCE",
        "AWS_ECR_CONTAINER",
        "AWS_LAMBDA_FUNCTION",
        "FINDING_TYPE",
        "IMAGE_LAYER",
        "LAMBDA_LAYER",
        "PACKAGE",
        "REPOSITORY",
        "TITLE",
    ] = Field(alias="aggregationType")
    account_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="accountIds"
    )
    aggregation_request: Optional[AggregationRequestModel] = Field(
        default=None, alias="aggregationRequest"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingAggregationsRequestModel(BaseModel):
    aggregation_type: Literal[
        "ACCOUNT",
        "AMI",
        "AWS_EC2_INSTANCE",
        "AWS_ECR_CONTAINER",
        "AWS_LAMBDA_FUNCTION",
        "FINDING_TYPE",
        "IMAGE_LAYER",
        "LAMBDA_LAYER",
        "PACKAGE",
        "REPOSITORY",
        "TITLE",
    ] = Field(alias="aggregationType")
    account_ids: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="accountIds"
    )
    aggregation_request: Optional[AggregationRequestModel] = Field(
        default=None, alias="aggregationRequest"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class CreateFilterRequestModel(BaseModel):
    action: Literal["NONE", "SUPPRESS"] = Field(alias="action")
    filter_criteria: FilterCriteriaModel = Field(alias="filterCriteria")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    reason: Optional[str] = Field(default=None, alias="reason")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateFindingsReportRequestModel(BaseModel):
    report_format: Literal["CSV", "JSON"] = Field(alias="reportFormat")
    s3_destination: DestinationModel = Field(alias="s3Destination")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )


class FilterModel(BaseModel):
    action: Literal["NONE", "SUPPRESS"] = Field(alias="action")
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    criteria: FilterCriteriaModel = Field(alias="criteria")
    name: str = Field(alias="name")
    owner_id: str = Field(alias="ownerId")
    updated_at: datetime = Field(alias="updatedAt")
    description: Optional[str] = Field(default=None, alias="description")
    reason: Optional[str] = Field(default=None, alias="reason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class GetFindingsReportStatusResponseModel(BaseModel):
    destination: DestinationModel = Field(alias="destination")
    error_code: Literal[
        "BUCKET_NOT_FOUND",
        "INCOMPATIBLE_BUCKET_REGION",
        "INTERNAL_ERROR",
        "INVALID_PERMISSIONS",
        "MALFORMED_KMS_KEY",
        "NO_FINDINGS_FOUND",
    ] = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")
    filter_criteria: FilterCriteriaModel = Field(alias="filterCriteria")
    report_id: str = Field(alias="reportId")
    status: Literal["CANCELLED", "FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsRequestListFindingsPaginateModel(BaseModel):
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestModel(BaseModel):
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="sortCriteria"
    )


class UpdateFilterRequestModel(BaseModel):
    filter_arn: str = Field(alias="filterArn")
    action: Optional[Literal["NONE", "SUPPRESS"]] = Field(default=None, alias="action")
    description: Optional[str] = Field(default=None, alias="description")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="filterCriteria"
    )
    name: Optional[str] = Field(default=None, alias="name")
    reason: Optional[str] = Field(default=None, alias="reason")


class ListCoverageResponseModel(BaseModel):
    covered_resources: List[CoveredResourceModel] = Field(alias="coveredResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FindingModel(BaseModel):
    aws_account_id: str = Field(alias="awsAccountId")
    description: str = Field(alias="description")
    finding_arn: str = Field(alias="findingArn")
    first_observed_at: datetime = Field(alias="firstObservedAt")
    last_observed_at: datetime = Field(alias="lastObservedAt")
    remediation: RemediationModel = Field(alias="remediation")
    resources: List[ResourceModel] = Field(alias="resources")
    severity: Literal[
        "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNTRIAGED"
    ] = Field(alias="severity")
    status: Literal["ACTIVE", "CLOSED", "SUPPRESSED"] = Field(alias="status")
    type: Literal["NETWORK_REACHABILITY", "PACKAGE_VULNERABILITY"] = Field(alias="type")
    exploit_available: Optional[Literal["NO", "YES"]] = Field(
        default=None, alias="exploitAvailable"
    )
    exploitability_details: Optional[ExploitabilityDetailsModel] = Field(
        default=None, alias="exploitabilityDetails"
    )
    fix_available: Optional[Literal["NO", "PARTIAL", "YES"]] = Field(
        default=None, alias="fixAvailable"
    )
    inspector_score: Optional[float] = Field(default=None, alias="inspectorScore")
    inspector_score_details: Optional[InspectorScoreDetailsModel] = Field(
        default=None, alias="inspectorScoreDetails"
    )
    network_reachability_details: Optional[NetworkReachabilityDetailsModel] = Field(
        default=None, alias="networkReachabilityDetails"
    )
    package_vulnerability_details: Optional[PackageVulnerabilityDetailsModel] = Field(
        default=None, alias="packageVulnerabilityDetails"
    )
    title: Optional[str] = Field(default=None, alias="title")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class ListFiltersResponseModel(BaseModel):
    filters: List[FilterModel] = Field(alias="filters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsResponseModel(BaseModel):
    findings: List[FindingModel] = Field(alias="findings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
