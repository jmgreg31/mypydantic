# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessPreviewStatusReasonModel(BaseModel):
    code: Literal["INTERNAL_ERROR", "INVALID_CONFIGURATION"] = Field(alias="code")


class AclGranteeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    uri: Optional[str] = Field(default=None, alias="uri")


class AnalyzedResourceSummaryModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    resource_owner_account: str = Field(alias="resourceOwnerAccount")
    resource_type: Literal[
        "AWS::EC2::Snapshot",
        "AWS::ECR::Repository",
        "AWS::EFS::FileSystem",
        "AWS::IAM::Role",
        "AWS::KMS::Key",
        "AWS::Lambda::Function",
        "AWS::Lambda::LayerVersion",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBSnapshot",
        "AWS::S3::Bucket",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SecretsManager::Secret",
    ] = Field(alias="resourceType")


class AnalyzedResourceModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    resource_type: Literal[
        "AWS::EC2::Snapshot",
        "AWS::ECR::Repository",
        "AWS::EFS::FileSystem",
        "AWS::IAM::Role",
        "AWS::KMS::Key",
        "AWS::Lambda::Function",
        "AWS::Lambda::LayerVersion",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBSnapshot",
        "AWS::S3::Bucket",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SecretsManager::Secret",
    ] = Field(alias="resourceType")
    created_at: datetime = Field(alias="createdAt")
    analyzed_at: datetime = Field(alias="analyzedAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_public: bool = Field(alias="isPublic")
    resource_owner_account: str = Field(alias="resourceOwnerAccount")
    actions: Optional[List[str]] = Field(default=None, alias="actions")
    shared_via: Optional[List[str]] = Field(default=None, alias="sharedVia")
    status: Optional[Literal["ACTIVE", "ARCHIVED", "RESOLVED"]] = Field(
        default=None, alias="status"
    )
    error: Optional[str] = Field(default=None, alias="error")


class StatusReasonModel(BaseModel):
    code: Literal[
        "AWS_SERVICE_ACCESS_DISABLED",
        "DELEGATED_ADMINISTRATOR_DEREGISTERED",
        "ORGANIZATION_DELETED",
        "SERVICE_LINKED_ROLE_CREATION_FAILED",
    ] = Field(alias="code")


class ApplyArchiveRuleRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    rule_name: str = Field(alias="ruleName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CriterionModel(BaseModel):
    eq: Optional[Sequence[str]] = Field(default=None, alias="eq")
    neq: Optional[Sequence[str]] = Field(default=None, alias="neq")
    contains: Optional[Sequence[str]] = Field(default=None, alias="contains")
    exists: Optional[bool] = Field(default=None, alias="exists")


class CancelPolicyGenerationRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class TrailModel(BaseModel):
    cloud_trail_arn: str = Field(alias="cloudTrailArn")
    regions: Optional[Sequence[str]] = Field(default=None, alias="regions")
    all_regions: Optional[bool] = Field(default=None, alias="allRegions")


class TrailPropertiesModel(BaseModel):
    cloud_trail_arn: str = Field(alias="cloudTrailArn")
    regions: Optional[List[str]] = Field(default=None, alias="regions")
    all_regions: Optional[bool] = Field(default=None, alias="allRegions")


class EbsSnapshotConfigurationModel(BaseModel):
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="userIds")
    groups: Optional[Sequence[str]] = Field(default=None, alias="groups")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class EcrRepositoryConfigurationModel(BaseModel):
    repository_policy: Optional[str] = Field(default=None, alias="repositoryPolicy")


class EfsFileSystemConfigurationModel(BaseModel):
    file_system_policy: Optional[str] = Field(default=None, alias="fileSystemPolicy")


class IamRoleConfigurationModel(BaseModel):
    trust_policy: Optional[str] = Field(default=None, alias="trustPolicy")


class SecretsManagerSecretConfigurationModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    secret_policy: Optional[str] = Field(default=None, alias="secretPolicy")


class SnsTopicConfigurationModel(BaseModel):
    topic_policy: Optional[str] = Field(default=None, alias="topicPolicy")


class SqsQueueConfigurationModel(BaseModel):
    queue_policy: Optional[str] = Field(default=None, alias="queuePolicy")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteAnalyzerRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteArchiveRuleRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    rule_name: str = Field(alias="ruleName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class FindingSourceDetailModel(BaseModel):
    access_point_arn: Optional[str] = Field(default=None, alias="accessPointArn")
    access_point_account: Optional[str] = Field(
        default=None, alias="accessPointAccount"
    )


class GeneratedPolicyModel(BaseModel):
    policy: str = Field(alias="policy")


class GetAccessPreviewRequestModel(BaseModel):
    access_preview_id: str = Field(alias="accessPreviewId")
    analyzer_arn: str = Field(alias="analyzerArn")


class GetAnalyzedResourceRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    resource_arn: str = Field(alias="resourceArn")


class GetAnalyzerRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")


class GetArchiveRuleRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    rule_name: str = Field(alias="ruleName")


class GetFindingRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    id: str = Field(alias="id")


class GetGeneratedPolicyRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    include_resource_placeholders: Optional[bool] = Field(
        default=None, alias="includeResourcePlaceholders"
    )
    include_service_level_template: Optional[bool] = Field(
        default=None, alias="includeServiceLevelTemplate"
    )


class JobErrorModel(BaseModel):
    code: Literal[
        "AUTHORIZATION_ERROR",
        "RESOURCE_NOT_FOUND_ERROR",
        "SERVICE_ERROR",
        "SERVICE_QUOTA_EXCEEDED_ERROR",
    ] = Field(alias="code")
    message: str = Field(alias="message")


class KmsGrantConstraintsModel(BaseModel):
    encryption_context_equals: Optional[Mapping[str, str]] = Field(
        default=None, alias="encryptionContextEquals"
    )
    encryption_context_subset: Optional[Mapping[str, str]] = Field(
        default=None, alias="encryptionContextSubset"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccessPreviewsRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAnalyzedResourcesRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    resource_type: Optional[
        Literal[
            "AWS::EC2::Snapshot",
            "AWS::ECR::Repository",
            "AWS::EFS::FileSystem",
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBSnapshot",
            "AWS::S3::Bucket",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SecretsManager::Secret",
        ]
    ] = Field(default=None, alias="resourceType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAnalyzersRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    type: Optional[Literal["ACCOUNT", "ORGANIZATION"]] = Field(
        default=None, alias="type"
    )


class ListArchiveRulesRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SortCriteriaModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="orderBy")


class ListPolicyGenerationsRequestModel(BaseModel):
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PolicyGenerationModel(BaseModel):
    job_id: str = Field(alias="jobId")
    principal_arn: str = Field(alias="principalArn")
    status: Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="status"
    )
    started_on: datetime = Field(alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="completedOn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class VpcConfigurationModel(BaseModel):
    vpc_id: str = Field(alias="vpcId")


class SubstringModel(BaseModel):
    start: int = Field(alias="start")
    length: int = Field(alias="length")


class PolicyGenerationDetailsModel(BaseModel):
    principal_arn: str = Field(alias="principalArn")


class PositionModel(BaseModel):
    line: int = Field(alias="line")
    column: int = Field(alias="column")
    offset: int = Field(alias="offset")


class RdsDbClusterSnapshotAttributeValueModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")


class RdsDbSnapshotAttributeValueModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")


class S3PublicAccessBlockConfigurationModel(BaseModel):
    ignore_public_acls: bool = Field(alias="ignorePublicAcls")
    restrict_public_buckets: bool = Field(alias="restrictPublicBuckets")


class StartResourceScanRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    resource_arn: str = Field(alias="resourceArn")
    resource_owner_account: Optional[str] = Field(
        default=None, alias="resourceOwnerAccount"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateFindingsRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    status: Literal["ACTIVE", "ARCHIVED"] = Field(alias="status")
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ValidatePolicyRequestModel(BaseModel):
    policy_document: str = Field(alias="policyDocument")
    policy_type: Literal[
        "IDENTITY_POLICY", "RESOURCE_POLICY", "SERVICE_CONTROL_POLICY"
    ] = Field(alias="policyType")
    locale: Optional[
        Literal["DE", "EN", "ES", "FR", "IT", "JA", "KO", "PT_BR", "ZH_CN", "ZH_TW"]
    ] = Field(default=None, alias="locale")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    validate_policy_resource_type: Optional[
        Literal[
            "AWS::IAM::AssumeRolePolicyDocument",
            "AWS::S3::AccessPoint",
            "AWS::S3::Bucket",
            "AWS::S3::MultiRegionAccessPoint",
            "AWS::S3ObjectLambda::AccessPoint",
        ]
    ] = Field(default=None, alias="validatePolicyResourceType")


class AccessPreviewSummaryModel(BaseModel):
    id: str = Field(alias="id")
    analyzer_arn: str = Field(alias="analyzerArn")
    created_at: datetime = Field(alias="createdAt")
    status: Literal["COMPLETED", "CREATING", "FAILED"] = Field(alias="status")
    status_reason: Optional[AccessPreviewStatusReasonModel] = Field(
        default=None, alias="statusReason"
    )


class S3BucketAclGrantConfigurationModel(BaseModel):
    permission: Literal[
        "FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"
    ] = Field(alias="permission")
    grantee: AclGranteeModel = Field(alias="grantee")


class AnalyzerSummaryModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    type: Literal["ACCOUNT", "ORGANIZATION"] = Field(alias="type")
    created_at: datetime = Field(alias="createdAt")
    status: Literal["ACTIVE", "CREATING", "DISABLED", "FAILED"] = Field(alias="status")
    last_resource_analyzed: Optional[str] = Field(
        default=None, alias="lastResourceAnalyzed"
    )
    last_resource_analyzed_at: Optional[datetime] = Field(
        default=None, alias="lastResourceAnalyzedAt"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    status_reason: Optional[StatusReasonModel] = Field(
        default=None, alias="statusReason"
    )


class ArchiveRuleSummaryModel(BaseModel):
    rule_name: str = Field(alias="ruleName")
    filter: Dict[str, CriterionModel] = Field(alias="filter")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class CreateArchiveRuleRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    rule_name: str = Field(alias="ruleName")
    filter: Mapping[str, CriterionModel] = Field(alias="filter")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class InlineArchiveRuleModel(BaseModel):
    rule_name: str = Field(alias="ruleName")
    filter: Mapping[str, CriterionModel] = Field(alias="filter")


class ListAccessPreviewFindingsRequestModel(BaseModel):
    access_preview_id: str = Field(alias="accessPreviewId")
    analyzer_arn: str = Field(alias="analyzerArn")
    filter: Optional[Mapping[str, CriterionModel]] = Field(default=None, alias="filter")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class UpdateArchiveRuleRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    rule_name: str = Field(alias="ruleName")
    filter: Mapping[str, CriterionModel] = Field(alias="filter")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CloudTrailDetailsModel(BaseModel):
    trails: Sequence[TrailModel] = Field(alias="trails")
    access_role: str = Field(alias="accessRole")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")


class CloudTrailPropertiesModel(BaseModel):
    trail_properties: List[TrailPropertiesModel] = Field(alias="trailProperties")
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")


class CreateAccessPreviewResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnalyzerResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnalyzedResourceResponseModel(BaseModel):
    resource: AnalyzedResourceModel = Field(alias="resource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnalyzedResourcesResponseModel(BaseModel):
    analyzed_resources: List[AnalyzedResourceSummaryModel] = Field(
        alias="analyzedResources"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPolicyGenerationResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FindingSourceModel(BaseModel):
    type: Literal[
        "BUCKET_ACL", "POLICY", "S3_ACCESS_POINT", "S3_ACCESS_POINT_ACCOUNT"
    ] = Field(alias="type")
    detail: Optional[FindingSourceDetailModel] = Field(default=None, alias="detail")


class JobDetailsModel(BaseModel):
    job_id: str = Field(alias="jobId")
    status: Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="status"
    )
    started_on: datetime = Field(alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="completedOn")
    job_error: Optional[JobErrorModel] = Field(default=None, alias="jobError")


class KmsGrantConfigurationModel(BaseModel):
    operations: Sequence[
        Literal[
            "CreateGrant",
            "Decrypt",
            "DescribeKey",
            "Encrypt",
            "GenerateDataKey",
            "GenerateDataKeyPair",
            "GenerateDataKeyPairWithoutPlaintext",
            "GenerateDataKeyWithoutPlaintext",
            "GetPublicKey",
            "ReEncryptFrom",
            "ReEncryptTo",
            "RetireGrant",
            "Sign",
            "Verify",
        ]
    ] = Field(alias="operations")
    grantee_principal: str = Field(alias="granteePrincipal")
    issuing_account: str = Field(alias="issuingAccount")
    retiring_principal: Optional[str] = Field(default=None, alias="retiringPrincipal")
    constraints: Optional[KmsGrantConstraintsModel] = Field(
        default=None, alias="constraints"
    )


class ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateModel(BaseModel):
    access_preview_id: str = Field(alias="accessPreviewId")
    analyzer_arn: str = Field(alias="analyzerArn")
    filter: Optional[Mapping[str, CriterionModel]] = Field(default=None, alias="filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccessPreviewsRequestListAccessPreviewsPaginateModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    resource_type: Optional[
        Literal[
            "AWS::EC2::Snapshot",
            "AWS::ECR::Repository",
            "AWS::EFS::FileSystem",
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBSnapshot",
            "AWS::S3::Bucket",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SecretsManager::Secret",
        ]
    ] = Field(default=None, alias="resourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAnalyzersRequestListAnalyzersPaginateModel(BaseModel):
    type: Optional[Literal["ACCOUNT", "ORGANIZATION"]] = Field(
        default=None, alias="type"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListArchiveRulesRequestListArchiveRulesPaginateModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPolicyGenerationsRequestListPolicyGenerationsPaginateModel(BaseModel):
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ValidatePolicyRequestValidatePolicyPaginateModel(BaseModel):
    policy_document: str = Field(alias="policyDocument")
    policy_type: Literal[
        "IDENTITY_POLICY", "RESOURCE_POLICY", "SERVICE_CONTROL_POLICY"
    ] = Field(alias="policyType")
    locale: Optional[
        Literal["DE", "EN", "ES", "FR", "IT", "JA", "KO", "PT_BR", "ZH_CN", "ZH_TW"]
    ] = Field(default=None, alias="locale")
    validate_policy_resource_type: Optional[
        Literal[
            "AWS::IAM::AssumeRolePolicyDocument",
            "AWS::S3::AccessPoint",
            "AWS::S3::Bucket",
            "AWS::S3::MultiRegionAccessPoint",
            "AWS::S3ObjectLambda::AccessPoint",
        ]
    ] = Field(default=None, alias="validatePolicyResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestListFindingsPaginateModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    filter: Optional[Mapping[str, CriterionModel]] = Field(default=None, alias="filter")
    sort: Optional[SortCriteriaModel] = Field(default=None, alias="sort")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    filter: Optional[Mapping[str, CriterionModel]] = Field(default=None, alias="filter")
    sort: Optional[SortCriteriaModel] = Field(default=None, alias="sort")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListPolicyGenerationsResponseModel(BaseModel):
    policy_generations: List[PolicyGenerationModel] = Field(alias="policyGenerations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkOriginConfigurationModel(BaseModel):
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="vpcConfiguration"
    )
    internet_configuration: Optional[Mapping[str, Any]] = Field(
        default=None, alias="internetConfiguration"
    )


class PathElementModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="index")
    key: Optional[str] = Field(default=None, alias="key")
    substring: Optional[SubstringModel] = Field(default=None, alias="substring")
    value: Optional[str] = Field(default=None, alias="value")


class SpanModel(BaseModel):
    start: PositionModel = Field(alias="start")
    end: PositionModel = Field(alias="end")


class RdsDbClusterSnapshotConfigurationModel(BaseModel):
    attributes: Optional[Mapping[str, RdsDbClusterSnapshotAttributeValueModel]] = Field(
        default=None, alias="attributes"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class RdsDbSnapshotConfigurationModel(BaseModel):
    attributes: Optional[Mapping[str, RdsDbSnapshotAttributeValueModel]] = Field(
        default=None, alias="attributes"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class ListAccessPreviewsResponseModel(BaseModel):
    access_previews: List[AccessPreviewSummaryModel] = Field(alias="accessPreviews")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnalyzerResponseModel(BaseModel):
    analyzer: AnalyzerSummaryModel = Field(alias="analyzer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnalyzersResponseModel(BaseModel):
    analyzers: List[AnalyzerSummaryModel] = Field(alias="analyzers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetArchiveRuleResponseModel(BaseModel):
    archive_rule: ArchiveRuleSummaryModel = Field(alias="archiveRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListArchiveRulesResponseModel(BaseModel):
    archive_rules: List[ArchiveRuleSummaryModel] = Field(alias="archiveRules")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnalyzerRequestModel(BaseModel):
    analyzer_name: str = Field(alias="analyzerName")
    type: Literal["ACCOUNT", "ORGANIZATION"] = Field(alias="type")
    archive_rules: Optional[Sequence[InlineArchiveRuleModel]] = Field(
        default=None, alias="archiveRules"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StartPolicyGenerationRequestModel(BaseModel):
    policy_generation_details: PolicyGenerationDetailsModel = Field(
        alias="policyGenerationDetails"
    )
    cloud_trail_details: Optional[CloudTrailDetailsModel] = Field(
        default=None, alias="cloudTrailDetails"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GeneratedPolicyPropertiesModel(BaseModel):
    principal_arn: str = Field(alias="principalArn")
    is_complete: Optional[bool] = Field(default=None, alias="isComplete")
    cloud_trail_properties: Optional[CloudTrailPropertiesModel] = Field(
        default=None, alias="cloudTrailProperties"
    )


class AccessPreviewFindingModel(BaseModel):
    id: str = Field(alias="id")
    resource_type: Literal[
        "AWS::EC2::Snapshot",
        "AWS::ECR::Repository",
        "AWS::EFS::FileSystem",
        "AWS::IAM::Role",
        "AWS::KMS::Key",
        "AWS::Lambda::Function",
        "AWS::Lambda::LayerVersion",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBSnapshot",
        "AWS::S3::Bucket",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SecretsManager::Secret",
    ] = Field(alias="resourceType")
    created_at: datetime = Field(alias="createdAt")
    change_type: Literal["CHANGED", "NEW", "UNCHANGED"] = Field(alias="changeType")
    status: Literal["ACTIVE", "ARCHIVED", "RESOLVED"] = Field(alias="status")
    resource_owner_account: str = Field(alias="resourceOwnerAccount")
    existing_finding_id: Optional[str] = Field(default=None, alias="existingFindingId")
    existing_finding_status: Optional[
        Literal["ACTIVE", "ARCHIVED", "RESOLVED"]
    ] = Field(default=None, alias="existingFindingStatus")
    principal: Optional[Dict[str, str]] = Field(default=None, alias="principal")
    action: Optional[List[str]] = Field(default=None, alias="action")
    condition: Optional[Dict[str, str]] = Field(default=None, alias="condition")
    resource: Optional[str] = Field(default=None, alias="resource")
    is_public: Optional[bool] = Field(default=None, alias="isPublic")
    error: Optional[str] = Field(default=None, alias="error")
    sources: Optional[List[FindingSourceModel]] = Field(default=None, alias="sources")


class FindingSummaryModel(BaseModel):
    id: str = Field(alias="id")
    resource_type: Literal[
        "AWS::EC2::Snapshot",
        "AWS::ECR::Repository",
        "AWS::EFS::FileSystem",
        "AWS::IAM::Role",
        "AWS::KMS::Key",
        "AWS::Lambda::Function",
        "AWS::Lambda::LayerVersion",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBSnapshot",
        "AWS::S3::Bucket",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SecretsManager::Secret",
    ] = Field(alias="resourceType")
    condition: Dict[str, str] = Field(alias="condition")
    created_at: datetime = Field(alias="createdAt")
    analyzed_at: datetime = Field(alias="analyzedAt")
    updated_at: datetime = Field(alias="updatedAt")
    status: Literal["ACTIVE", "ARCHIVED", "RESOLVED"] = Field(alias="status")
    resource_owner_account: str = Field(alias="resourceOwnerAccount")
    principal: Optional[Dict[str, str]] = Field(default=None, alias="principal")
    action: Optional[List[str]] = Field(default=None, alias="action")
    resource: Optional[str] = Field(default=None, alias="resource")
    is_public: Optional[bool] = Field(default=None, alias="isPublic")
    error: Optional[str] = Field(default=None, alias="error")
    sources: Optional[List[FindingSourceModel]] = Field(default=None, alias="sources")


class FindingModel(BaseModel):
    id: str = Field(alias="id")
    resource_type: Literal[
        "AWS::EC2::Snapshot",
        "AWS::ECR::Repository",
        "AWS::EFS::FileSystem",
        "AWS::IAM::Role",
        "AWS::KMS::Key",
        "AWS::Lambda::Function",
        "AWS::Lambda::LayerVersion",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBSnapshot",
        "AWS::S3::Bucket",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SecretsManager::Secret",
    ] = Field(alias="resourceType")
    condition: Dict[str, str] = Field(alias="condition")
    created_at: datetime = Field(alias="createdAt")
    analyzed_at: datetime = Field(alias="analyzedAt")
    updated_at: datetime = Field(alias="updatedAt")
    status: Literal["ACTIVE", "ARCHIVED", "RESOLVED"] = Field(alias="status")
    resource_owner_account: str = Field(alias="resourceOwnerAccount")
    principal: Optional[Dict[str, str]] = Field(default=None, alias="principal")
    action: Optional[List[str]] = Field(default=None, alias="action")
    resource: Optional[str] = Field(default=None, alias="resource")
    is_public: Optional[bool] = Field(default=None, alias="isPublic")
    error: Optional[str] = Field(default=None, alias="error")
    sources: Optional[List[FindingSourceModel]] = Field(default=None, alias="sources")


class KmsKeyConfigurationModel(BaseModel):
    key_policies: Optional[Mapping[str, str]] = Field(default=None, alias="keyPolicies")
    grants: Optional[Sequence[KmsGrantConfigurationModel]] = Field(
        default=None, alias="grants"
    )


class S3AccessPointConfigurationModel(BaseModel):
    access_point_policy: Optional[str] = Field(default=None, alias="accessPointPolicy")
    public_access_block: Optional[S3PublicAccessBlockConfigurationModel] = Field(
        default=None, alias="publicAccessBlock"
    )
    network_origin: Optional[NetworkOriginConfigurationModel] = Field(
        default=None, alias="networkOrigin"
    )


class LocationModel(BaseModel):
    path: List[PathElementModel] = Field(alias="path")
    span: SpanModel = Field(alias="span")


class GeneratedPolicyResultModel(BaseModel):
    properties: GeneratedPolicyPropertiesModel = Field(alias="properties")
    generated_policies: Optional[List[GeneratedPolicyModel]] = Field(
        default=None, alias="generatedPolicies"
    )


class ListAccessPreviewFindingsResponseModel(BaseModel):
    findings: List[AccessPreviewFindingModel] = Field(alias="findings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsResponseModel(BaseModel):
    findings: List[FindingSummaryModel] = Field(alias="findings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFindingResponseModel(BaseModel):
    finding: FindingModel = Field(alias="finding")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3BucketConfigurationModel(BaseModel):
    bucket_policy: Optional[str] = Field(default=None, alias="bucketPolicy")
    bucket_acl_grants: Optional[Sequence[S3BucketAclGrantConfigurationModel]] = Field(
        default=None, alias="bucketAclGrants"
    )
    bucket_public_access_block: Optional[S3PublicAccessBlockConfigurationModel] = Field(
        default=None, alias="bucketPublicAccessBlock"
    )
    access_points: Optional[Mapping[str, S3AccessPointConfigurationModel]] = Field(
        default=None, alias="accessPoints"
    )


class ValidatePolicyFindingModel(BaseModel):
    finding_details: str = Field(alias="findingDetails")
    finding_type: Literal["ERROR", "SECURITY_WARNING", "SUGGESTION", "WARNING"] = Field(
        alias="findingType"
    )
    issue_code: str = Field(alias="issueCode")
    learn_more_link: str = Field(alias="learnMoreLink")
    locations: List[LocationModel] = Field(alias="locations")


class GetGeneratedPolicyResponseModel(BaseModel):
    job_details: JobDetailsModel = Field(alias="jobDetails")
    generated_policy_result: GeneratedPolicyResultModel = Field(
        alias="generatedPolicyResult"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationModel(BaseModel):
    ebs_snapshot: Optional[EbsSnapshotConfigurationModel] = Field(
        default=None, alias="ebsSnapshot"
    )
    ecr_repository: Optional[EcrRepositoryConfigurationModel] = Field(
        default=None, alias="ecrRepository"
    )
    iam_role: Optional[IamRoleConfigurationModel] = Field(default=None, alias="iamRole")
    efs_file_system: Optional[EfsFileSystemConfigurationModel] = Field(
        default=None, alias="efsFileSystem"
    )
    kms_key: Optional[KmsKeyConfigurationModel] = Field(default=None, alias="kmsKey")
    rds_db_cluster_snapshot: Optional[RdsDbClusterSnapshotConfigurationModel] = Field(
        default=None, alias="rdsDbClusterSnapshot"
    )
    rds_db_snapshot: Optional[RdsDbSnapshotConfigurationModel] = Field(
        default=None, alias="rdsDbSnapshot"
    )
    secrets_manager_secret: Optional[SecretsManagerSecretConfigurationModel] = Field(
        default=None, alias="secretsManagerSecret"
    )
    s3_bucket: Optional[S3BucketConfigurationModel] = Field(
        default=None, alias="s3Bucket"
    )
    sns_topic: Optional[SnsTopicConfigurationModel] = Field(
        default=None, alias="snsTopic"
    )
    sqs_queue: Optional[SqsQueueConfigurationModel] = Field(
        default=None, alias="sqsQueue"
    )


class ValidatePolicyResponseModel(BaseModel):
    findings: List[ValidatePolicyFindingModel] = Field(alias="findings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessPreviewModel(BaseModel):
    id: str = Field(alias="id")
    analyzer_arn: str = Field(alias="analyzerArn")
    configurations: Dict[str, ConfigurationModel] = Field(alias="configurations")
    created_at: datetime = Field(alias="createdAt")
    status: Literal["COMPLETED", "CREATING", "FAILED"] = Field(alias="status")
    status_reason: Optional[AccessPreviewStatusReasonModel] = Field(
        default=None, alias="statusReason"
    )


class CreateAccessPreviewRequestModel(BaseModel):
    analyzer_arn: str = Field(alias="analyzerArn")
    configurations: Mapping[str, ConfigurationModel] = Field(alias="configurations")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetAccessPreviewResponseModel(BaseModel):
    access_preview: AccessPreviewModel = Field(alias="accessPreview")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
