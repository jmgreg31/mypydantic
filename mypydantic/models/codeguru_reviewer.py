# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class KMSKeyDetailsModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    encryption_option: Optional[
        Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
    ] = Field(default=None, alias="EncryptionOption")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BranchDiffSourceCodeTypeModel(BaseModel):
    source_branch_name: str = Field(alias="SourceBranchName")
    destination_branch_name: str = Field(alias="DestinationBranchName")


class CodeArtifactsModel(BaseModel):
    source_code_artifacts_object_key: str = Field(alias="SourceCodeArtifactsObjectKey")
    build_artifacts_object_key: Optional[str] = Field(
        default=None, alias="BuildArtifactsObjectKey"
    )


class CodeCommitRepositoryModel(BaseModel):
    name: str = Field(alias="Name")


class MetricsSummaryModel(BaseModel):
    metered_lines_of_code_count: Optional[int] = Field(
        default=None, alias="MeteredLinesOfCodeCount"
    )
    suppressed_lines_of_code_count: Optional[int] = Field(
        default=None, alias="SuppressedLinesOfCodeCount"
    )
    findings_count: Optional[int] = Field(default=None, alias="FindingsCount")


class MetricsModel(BaseModel):
    metered_lines_of_code_count: Optional[int] = Field(
        default=None, alias="MeteredLinesOfCodeCount"
    )
    suppressed_lines_of_code_count: Optional[int] = Field(
        default=None, alias="SuppressedLinesOfCodeCount"
    )
    findings_count: Optional[int] = Field(default=None, alias="FindingsCount")


class CommitDiffSourceCodeTypeModel(BaseModel):
    source_commit: Optional[str] = Field(default=None, alias="SourceCommit")
    destination_commit: Optional[str] = Field(default=None, alias="DestinationCommit")
    merge_base_commit: Optional[str] = Field(default=None, alias="MergeBaseCommit")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeCodeReviewRequestModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")


class DescribeRecommendationFeedbackRequestModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")
    recommendation_id: str = Field(alias="RecommendationId")
    user_id: Optional[str] = Field(default=None, alias="UserId")


class RecommendationFeedbackModel(BaseModel):
    code_review_arn: Optional[str] = Field(default=None, alias="CodeReviewArn")
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    reactions: Optional[List[Literal["ThumbsDown", "ThumbsUp"]]] = Field(
        default=None, alias="Reactions"
    )
    user_id: Optional[str] = Field(default=None, alias="UserId")
    created_time_stamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimeStamp"
    )
    last_updated_time_stamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimeStamp"
    )


class DescribeRepositoryAssociationRequestModel(BaseModel):
    association_arn: str = Field(alias="AssociationArn")


class DisassociateRepositoryRequestModel(BaseModel):
    association_arn: str = Field(alias="AssociationArn")


class EventInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[str] = Field(default=None, alias="State")


class ListCodeReviewsRequestModel(BaseModel):
    type: Literal["PullRequest", "RepositoryAnalysis"] = Field(alias="Type")
    provider_types: Optional[
        Sequence[
            Literal[
                "Bitbucket",
                "CodeCommit",
                "GitHub",
                "GitHubEnterpriseServer",
                "S3Bucket",
            ]
        ]
    ] = Field(default=None, alias="ProviderTypes")
    states: Optional[
        Sequence[Literal["Completed", "Deleting", "Failed", "Pending"]]
    ] = Field(default=None, alias="States")
    repository_names: Optional[Sequence[str]] = Field(
        default=None, alias="RepositoryNames"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRecommendationFeedbackRequestModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="UserIds")
    recommendation_ids: Optional[Sequence[str]] = Field(
        default=None, alias="RecommendationIds"
    )


class RecommendationFeedbackSummaryModel(BaseModel):
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    reactions: Optional[List[Literal["ThumbsDown", "ThumbsUp"]]] = Field(
        default=None, alias="Reactions"
    )
    user_id: Optional[str] = Field(default=None, alias="UserId")


class ListRecommendationsRequestModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRepositoryAssociationsRequestModel(BaseModel):
    provider_types: Optional[
        Sequence[
            Literal[
                "Bitbucket",
                "CodeCommit",
                "GitHub",
                "GitHubEnterpriseServer",
                "S3Bucket",
            ]
        ]
    ] = Field(default=None, alias="ProviderTypes")
    states: Optional[
        Sequence[
            Literal[
                "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
            ]
        ]
    ] = Field(default=None, alias="States")
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    owners: Optional[Sequence[str]] = Field(default=None, alias="Owners")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RepositoryAssociationSummaryModel(BaseModel):
    association_arn: Optional[str] = Field(default=None, alias="AssociationArn")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    last_updated_time_stamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimeStamp"
    )
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    name: Optional[str] = Field(default=None, alias="Name")
    owner: Optional[str] = Field(default=None, alias="Owner")
    provider_type: Optional[
        Literal[
            "Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer", "S3Bucket"
        ]
    ] = Field(default=None, alias="ProviderType")
    state: Optional[
        Literal[
            "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
        ]
    ] = Field(default=None, alias="State")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PutRecommendationFeedbackRequestModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")
    recommendation_id: str = Field(alias="RecommendationId")
    reactions: Sequence[Literal["ThumbsDown", "ThumbsUp"]] = Field(alias="Reactions")


class RuleMetadataModel(BaseModel):
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    short_description: Optional[str] = Field(default=None, alias="ShortDescription")
    long_description: Optional[str] = Field(default=None, alias="LongDescription")
    rule_tags: Optional[List[str]] = Field(default=None, alias="RuleTags")


class RepositoryHeadSourceCodeTypeModel(BaseModel):
    branch_name: str = Field(alias="BranchName")


class S3RepositoryModel(BaseModel):
    name: str = Field(alias="Name")
    bucket_name: str = Field(alias="BucketName")


class ThirdPartySourceRepositoryModel(BaseModel):
    name: str = Field(alias="Name")
    connection_arn: str = Field(alias="ConnectionArn")
    owner: str = Field(alias="Owner")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3RepositoryDetailsModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    code_artifacts: Optional[CodeArtifactsModel] = Field(
        default=None, alias="CodeArtifacts"
    )


class DescribeCodeReviewRequestCodeReviewCompletedWaitModel(BaseModel):
    code_review_arn: str = Field(alias="CodeReviewArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitModel(
    BaseModel
):
    association_arn: str = Field(alias="AssociationArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeRecommendationFeedbackResponseModel(BaseModel):
    recommendation_feedback: RecommendationFeedbackModel = Field(
        alias="RecommendationFeedback"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestMetadataModel(BaseModel):
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    requester: Optional[str] = Field(default=None, alias="Requester")
    event_info: Optional[EventInfoModel] = Field(default=None, alias="EventInfo")
    vendor_name: Optional[Literal["GitHub", "GitLab", "NativeS3"]] = Field(
        default=None, alias="VendorName"
    )


class ListRecommendationFeedbackResponseModel(BaseModel):
    recommendation_feedback_summaries: List[RecommendationFeedbackSummaryModel] = Field(
        alias="RecommendationFeedbackSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateModel(
    BaseModel
):
    provider_types: Optional[
        Sequence[
            Literal[
                "Bitbucket",
                "CodeCommit",
                "GitHub",
                "GitHubEnterpriseServer",
                "S3Bucket",
            ]
        ]
    ] = Field(default=None, alias="ProviderTypes")
    states: Optional[
        Sequence[
            Literal[
                "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
            ]
        ]
    ] = Field(default=None, alias="States")
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    owners: Optional[Sequence[str]] = Field(default=None, alias="Owners")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositoryAssociationsResponseModel(BaseModel):
    repository_association_summaries: List[RepositoryAssociationSummaryModel] = Field(
        alias="RepositoryAssociationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationSummaryModel(BaseModel):
    file_path: Optional[str] = Field(default=None, alias="FilePath")
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    start_line: Optional[int] = Field(default=None, alias="StartLine")
    end_line: Optional[int] = Field(default=None, alias="EndLine")
    description: Optional[str] = Field(default=None, alias="Description")
    recommendation_category: Optional[
        Literal[
            "AWSBestPractices",
            "AWSCloudFormationIssues",
            "CodeInconsistencies",
            "CodeMaintenanceIssues",
            "ConcurrencyIssues",
            "DuplicateCode",
            "InputValidations",
            "JavaBestPractices",
            "PythonBestPractices",
            "ResourceLeaks",
            "SecurityIssues",
        ]
    ] = Field(default=None, alias="RecommendationCategory")
    rule_metadata: Optional[RuleMetadataModel] = Field(
        default=None, alias="RuleMetadata"
    )
    severity: Optional[Literal["Critical", "High", "Info", "Low", "Medium"]] = Field(
        default=None, alias="Severity"
    )


class RepositoryModel(BaseModel):
    code_commit: Optional[CodeCommitRepositoryModel] = Field(
        default=None, alias="CodeCommit"
    )
    bitbucket: Optional[ThirdPartySourceRepositoryModel] = Field(
        default=None, alias="Bitbucket"
    )
    git_hub_enterprise_server: Optional[ThirdPartySourceRepositoryModel] = Field(
        default=None, alias="GitHubEnterpriseServer"
    )
    s3_bucket: Optional[S3RepositoryModel] = Field(default=None, alias="S3Bucket")


class RepositoryAssociationModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    association_arn: Optional[str] = Field(default=None, alias="AssociationArn")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    name: Optional[str] = Field(default=None, alias="Name")
    owner: Optional[str] = Field(default=None, alias="Owner")
    provider_type: Optional[
        Literal[
            "Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer", "S3Bucket"
        ]
    ] = Field(default=None, alias="ProviderType")
    state: Optional[
        Literal[
            "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
        ]
    ] = Field(default=None, alias="State")
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    last_updated_time_stamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimeStamp"
    )
    created_time_stamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimeStamp"
    )
    kms_key_details: Optional[KMSKeyDetailsModel] = Field(
        default=None, alias="KMSKeyDetails"
    )
    s3_repository_details: Optional[S3RepositoryDetailsModel] = Field(
        default=None, alias="S3RepositoryDetails"
    )


class S3BucketRepositoryModel(BaseModel):
    name: str = Field(alias="Name")
    details: Optional[S3RepositoryDetailsModel] = Field(default=None, alias="Details")


class ListRecommendationsResponseModel(BaseModel):
    recommendation_summaries: List[RecommendationSummaryModel] = Field(
        alias="RecommendationSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateRepositoryRequestModel(BaseModel):
    repository: RepositoryModel = Field(alias="Repository")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    kms_key_details: Optional[KMSKeyDetailsModel] = Field(
        default=None, alias="KMSKeyDetails"
    )


class AssociateRepositoryResponseModel(BaseModel):
    repository_association: RepositoryAssociationModel = Field(
        alias="RepositoryAssociation"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRepositoryAssociationResponseModel(BaseModel):
    repository_association: RepositoryAssociationModel = Field(
        alias="RepositoryAssociation"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateRepositoryResponseModel(BaseModel):
    repository_association: RepositoryAssociationModel = Field(
        alias="RepositoryAssociation"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceCodeTypeModel(BaseModel):
    commit_diff: Optional[CommitDiffSourceCodeTypeModel] = Field(
        default=None, alias="CommitDiff"
    )
    repository_head: Optional[RepositoryHeadSourceCodeTypeModel] = Field(
        default=None, alias="RepositoryHead"
    )
    branch_diff: Optional[BranchDiffSourceCodeTypeModel] = Field(
        default=None, alias="BranchDiff"
    )
    s3_bucket_repository: Optional[S3BucketRepositoryModel] = Field(
        default=None, alias="S3BucketRepository"
    )
    request_metadata: Optional[RequestMetadataModel] = Field(
        default=None, alias="RequestMetadata"
    )


class CodeReviewSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    code_review_arn: Optional[str] = Field(default=None, alias="CodeReviewArn")
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    provider_type: Optional[
        Literal[
            "Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer", "S3Bucket"
        ]
    ] = Field(default=None, alias="ProviderType")
    state: Optional[Literal["Completed", "Deleting", "Failed", "Pending"]] = Field(
        default=None, alias="State"
    )
    created_time_stamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimeStamp"
    )
    last_updated_time_stamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimeStamp"
    )
    type: Optional[Literal["PullRequest", "RepositoryAnalysis"]] = Field(
        default=None, alias="Type"
    )
    pull_request_id: Optional[str] = Field(default=None, alias="PullRequestId")
    metrics_summary: Optional[MetricsSummaryModel] = Field(
        default=None, alias="MetricsSummary"
    )
    source_code_type: Optional[SourceCodeTypeModel] = Field(
        default=None, alias="SourceCodeType"
    )


class CodeReviewModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    code_review_arn: Optional[str] = Field(default=None, alias="CodeReviewArn")
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    provider_type: Optional[
        Literal[
            "Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer", "S3Bucket"
        ]
    ] = Field(default=None, alias="ProviderType")
    state: Optional[Literal["Completed", "Deleting", "Failed", "Pending"]] = Field(
        default=None, alias="State"
    )
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    created_time_stamp: Optional[datetime] = Field(
        default=None, alias="CreatedTimeStamp"
    )
    last_updated_time_stamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimeStamp"
    )
    type: Optional[Literal["PullRequest", "RepositoryAnalysis"]] = Field(
        default=None, alias="Type"
    )
    pull_request_id: Optional[str] = Field(default=None, alias="PullRequestId")
    source_code_type: Optional[SourceCodeTypeModel] = Field(
        default=None, alias="SourceCodeType"
    )
    association_arn: Optional[str] = Field(default=None, alias="AssociationArn")
    metrics: Optional[MetricsModel] = Field(default=None, alias="Metrics")
    analysis_types: Optional[List[Literal["CodeQuality", "Security"]]] = Field(
        default=None, alias="AnalysisTypes"
    )
    config_file_state: Optional[
        Literal["Absent", "Present", "PresentWithErrors"]
    ] = Field(default=None, alias="ConfigFileState")


class RepositoryAnalysisModel(BaseModel):
    repository_head: Optional[RepositoryHeadSourceCodeTypeModel] = Field(
        default=None, alias="RepositoryHead"
    )
    source_code_type: Optional[SourceCodeTypeModel] = Field(
        default=None, alias="SourceCodeType"
    )


class ListCodeReviewsResponseModel(BaseModel):
    code_review_summaries: List[CodeReviewSummaryModel] = Field(
        alias="CodeReviewSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCodeReviewResponseModel(BaseModel):
    code_review: CodeReviewModel = Field(alias="CodeReview")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCodeReviewResponseModel(BaseModel):
    code_review: CodeReviewModel = Field(alias="CodeReview")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CodeReviewTypeModel(BaseModel):
    repository_analysis: RepositoryAnalysisModel = Field(alias="RepositoryAnalysis")
    analysis_types: Optional[Sequence[Literal["CodeQuality", "Security"]]] = Field(
        default=None, alias="AnalysisTypes"
    )


class CreateCodeReviewRequestModel(BaseModel):
    name: str = Field(alias="Name")
    repository_association_arn: str = Field(alias="RepositoryAssociationArn")
    type: CodeReviewTypeModel = Field(alias="Type")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
