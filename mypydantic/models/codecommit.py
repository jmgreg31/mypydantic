# Model Generated: Thu Mar  2 21:56:17 2023

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


class ApprovalRuleEventMetadataModel(BaseModel):
    approval_rule_name: Optional[str] = Field(default=None, alias="approvalRuleName")
    approval_rule_id: Optional[str] = Field(default=None, alias="approvalRuleId")
    approval_rule_content: Optional[str] = Field(
        default=None, alias="approvalRuleContent"
    )


class ApprovalRuleOverriddenEventMetadataModel(BaseModel):
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    override_status: Optional[Literal["OVERRIDE", "REVOKE"]] = Field(
        default=None, alias="overrideStatus"
    )


class ApprovalRuleTemplateModel(BaseModel):
    approval_rule_template_id: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateId"
    )
    approval_rule_template_name: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateName"
    )
    approval_rule_template_description: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateDescription"
    )
    approval_rule_template_content: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateContent"
    )
    rule_content_sha256: Optional[str] = Field(default=None, alias="ruleContentSha256")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_user: Optional[str] = Field(default=None, alias="lastModifiedUser")


class OriginApprovalRuleTemplateModel(BaseModel):
    approval_rule_template_id: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateId"
    )
    approval_rule_template_name: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateName"
    )


class ApprovalStateChangedEventMetadataModel(BaseModel):
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    approval_status: Optional[Literal["APPROVE", "REVOKE"]] = Field(
        default=None, alias="approvalStatus"
    )


class ApprovalModel(BaseModel):
    user_arn: Optional[str] = Field(default=None, alias="userArn")
    approval_state: Optional[Literal["APPROVE", "REVOKE"]] = Field(
        default=None, alias="approvalState"
    )


class AssociateApprovalRuleTemplateWithRepositoryInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    repository_name: str = Field(alias="repositoryName")


class BatchAssociateApprovalRuleTemplateWithRepositoriesErrorModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    repository_names: Sequence[str] = Field(alias="repositoryNames")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDescribeMergeConflictsErrorModel(BaseModel):
    file_path: str = Field(alias="filePath")
    exception_name: str = Field(alias="exceptionName")
    message: str = Field(alias="message")


class BatchDescribeMergeConflictsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    merge_option: Literal[
        "FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"
    ] = Field(alias="mergeOption")
    max_merge_hunks: Optional[int] = Field(default=None, alias="maxMergeHunks")
    max_conflict_files: Optional[int] = Field(default=None, alias="maxConflictFiles")
    file_paths: Optional[Sequence[str]] = Field(default=None, alias="filePaths")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    repository_names: Sequence[str] = Field(alias="repositoryNames")


class BatchGetCommitsErrorModel(BaseModel):
    commit_id: Optional[str] = Field(default=None, alias="commitId")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class BatchGetCommitsInputRequestModel(BaseModel):
    commit_ids: Sequence[str] = Field(alias="commitIds")
    repository_name: str = Field(alias="repositoryName")


class BatchGetRepositoriesInputRequestModel(BaseModel):
    repository_names: Sequence[str] = Field(alias="repositoryNames")


class RepositoryMetadataModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    repository_id: Optional[str] = Field(default=None, alias="repositoryId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    repository_description: Optional[str] = Field(
        default=None, alias="repositoryDescription"
    )
    default_branch: Optional[str] = Field(default=None, alias="defaultBranch")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    clone_url_http: Optional[str] = Field(default=None, alias="cloneUrlHttp")
    clone_url_ssh: Optional[str] = Field(default=None, alias="cloneUrlSsh")
    arn: Optional[str] = Field(default=None, alias="Arn")


class BlobMetadataModel(BaseModel):
    blob_id: Optional[str] = Field(default=None, alias="blobId")
    path: Optional[str] = Field(default=None, alias="path")
    mode: Optional[str] = Field(default=None, alias="mode")


class BranchInfoModel(BaseModel):
    branch_name: Optional[str] = Field(default=None, alias="branchName")
    commit_id: Optional[str] = Field(default=None, alias="commitId")


class CommentModel(BaseModel):
    comment_id: Optional[str] = Field(default=None, alias="commentId")
    content: Optional[str] = Field(default=None, alias="content")
    in_reply_to: Optional[str] = Field(default=None, alias="inReplyTo")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    author_arn: Optional[str] = Field(default=None, alias="authorArn")
    deleted: Optional[bool] = Field(default=None, alias="deleted")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    caller_reactions: Optional[List[str]] = Field(default=None, alias="callerReactions")
    reaction_counts: Optional[Dict[str, int]] = Field(
        default=None, alias="reactionCounts"
    )


class LocationModel(BaseModel):
    file_path: Optional[str] = Field(default=None, alias="filePath")
    file_position: Optional[int] = Field(default=None, alias="filePosition")
    relative_file_version: Optional[Literal["AFTER", "BEFORE"]] = Field(
        default=None, alias="relativeFileVersion"
    )


class UserInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")
    date: Optional[str] = Field(default=None, alias="date")


class FileModesModel(BaseModel):
    source: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="source"
    )
    destination: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="destination"
    )
    base: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="base"
    )


class FileSizesModel(BaseModel):
    source: Optional[int] = Field(default=None, alias="source")
    destination: Optional[int] = Field(default=None, alias="destination")
    base: Optional[int] = Field(default=None, alias="base")


class IsBinaryFileModel(BaseModel):
    source: Optional[bool] = Field(default=None, alias="source")
    destination: Optional[bool] = Field(default=None, alias="destination")
    base: Optional[bool] = Field(default=None, alias="base")


class MergeOperationsModel(BaseModel):
    source: Optional[Literal["A", "D", "M"]] = Field(default=None, alias="source")
    destination: Optional[Literal["A", "D", "M"]] = Field(
        default=None, alias="destination"
    )


class ObjectTypesModel(BaseModel):
    source: Optional[Literal["DIRECTORY", "FILE", "GIT_LINK", "SYMBOLIC_LINK"]] = Field(
        default=None, alias="source"
    )
    destination: Optional[
        Literal["DIRECTORY", "FILE", "GIT_LINK", "SYMBOLIC_LINK"]
    ] = Field(default=None, alias="destination")
    base: Optional[Literal["DIRECTORY", "FILE", "GIT_LINK", "SYMBOLIC_LINK"]] = Field(
        default=None, alias="base"
    )


class DeleteFileEntryModel(BaseModel):
    file_path: str = Field(alias="filePath")


class ReplaceContentEntryModel(BaseModel):
    file_path: str = Field(alias="filePath")
    replacement_type: Literal[
        "KEEP_BASE", "KEEP_DESTINATION", "KEEP_SOURCE", "USE_NEW_CONTENT"
    ] = Field(alias="replacementType")
    content: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="content"
    )
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )


class SetFileModeEntryModel(BaseModel):
    file_path: str = Field(alias="filePath")
    file_mode: Literal["EXECUTABLE", "NORMAL", "SYMLINK"] = Field(alias="fileMode")


class CreateApprovalRuleTemplateInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    approval_rule_template_content: str = Field(alias="approvalRuleTemplateContent")
    approval_rule_template_description: Optional[str] = Field(
        default=None, alias="approvalRuleTemplateDescription"
    )


class CreateBranchInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: str = Field(alias="branchName")
    commit_id: str = Field(alias="commitId")


class FileMetadataModel(BaseModel):
    absolute_path: Optional[str] = Field(default=None, alias="absolutePath")
    blob_id: Optional[str] = Field(default=None, alias="blobId")
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )


class CreatePullRequestApprovalRuleInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    approval_rule_name: str = Field(alias="approvalRuleName")
    approval_rule_content: str = Field(alias="approvalRuleContent")


class TargetModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_reference: str = Field(alias="sourceReference")
    destination_reference: Optional[str] = Field(
        default=None, alias="destinationReference"
    )


class CreateRepositoryInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    repository_description: Optional[str] = Field(
        default=None, alias="repositoryDescription"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteApprovalRuleTemplateInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")


class DeleteBranchInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: str = Field(alias="branchName")


class DeleteCommentContentInputRequestModel(BaseModel):
    comment_id: str = Field(alias="commentId")


class DeleteFileInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: str = Field(alias="branchName")
    file_path: str = Field(alias="filePath")
    parent_commit_id: str = Field(alias="parentCommitId")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")


class DeletePullRequestApprovalRuleInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    approval_rule_name: str = Field(alias="approvalRuleName")


class DeleteRepositoryInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")


class DescribeMergeConflictsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    merge_option: Literal[
        "FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"
    ] = Field(alias="mergeOption")
    file_path: str = Field(alias="filePath")
    max_merge_hunks: Optional[int] = Field(default=None, alias="maxMergeHunks")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribePullRequestEventsInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    pull_request_event_type: Optional[
        Literal[
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_STATUS_CHANGED",
        ]
    ] = Field(default=None, alias="pullRequestEventType")
    actor_arn: Optional[str] = Field(default=None, alias="actorArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DisassociateApprovalRuleTemplateFromRepositoryInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    repository_name: str = Field(alias="repositoryName")


class EvaluatePullRequestApprovalRulesInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    revision_id: str = Field(alias="revisionId")


class EvaluationModel(BaseModel):
    approved: Optional[bool] = Field(default=None, alias="approved")
    overridden: Optional[bool] = Field(default=None, alias="overridden")
    approval_rules_satisfied: Optional[List[str]] = Field(
        default=None, alias="approvalRulesSatisfied"
    )
    approval_rules_not_satisfied: Optional[List[str]] = Field(
        default=None, alias="approvalRulesNotSatisfied"
    )


class FileModel(BaseModel):
    blob_id: Optional[str] = Field(default=None, alias="blobId")
    absolute_path: Optional[str] = Field(default=None, alias="absolutePath")
    relative_path: Optional[str] = Field(default=None, alias="relativePath")
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )


class FolderModel(BaseModel):
    tree_id: Optional[str] = Field(default=None, alias="treeId")
    absolute_path: Optional[str] = Field(default=None, alias="absolutePath")
    relative_path: Optional[str] = Field(default=None, alias="relativePath")


class GetApprovalRuleTemplateInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")


class GetBlobInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    blob_id: str = Field(alias="blobId")


class GetBranchInputRequestModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    branch_name: Optional[str] = Field(default=None, alias="branchName")


class GetCommentInputRequestModel(BaseModel):
    comment_id: str = Field(alias="commentId")


class GetCommentReactionsInputRequestModel(BaseModel):
    comment_id: str = Field(alias="commentId")
    reaction_user_arn: Optional[str] = Field(default=None, alias="reactionUserArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetCommentsForComparedCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    after_commit_id: str = Field(alias="afterCommitId")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetCommentsForPullRequestInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    after_commit_id: Optional[str] = Field(default=None, alias="afterCommitId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    commit_id: str = Field(alias="commitId")


class GetDifferencesInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    after_commit_specifier: str = Field(alias="afterCommitSpecifier")
    before_commit_specifier: Optional[str] = Field(
        default=None, alias="beforeCommitSpecifier"
    )
    before_path: Optional[str] = Field(default=None, alias="beforePath")
    after_path: Optional[str] = Field(default=None, alias="afterPath")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetFileInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    file_path: str = Field(alias="filePath")
    commit_specifier: Optional[str] = Field(default=None, alias="commitSpecifier")


class GetFolderInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    folder_path: str = Field(alias="folderPath")
    commit_specifier: Optional[str] = Field(default=None, alias="commitSpecifier")


class SubModuleModel(BaseModel):
    commit_id: Optional[str] = Field(default=None, alias="commitId")
    absolute_path: Optional[str] = Field(default=None, alias="absolutePath")
    relative_path: Optional[str] = Field(default=None, alias="relativePath")


class SymbolicLinkModel(BaseModel):
    blob_id: Optional[str] = Field(default=None, alias="blobId")
    absolute_path: Optional[str] = Field(default=None, alias="absolutePath")
    relative_path: Optional[str] = Field(default=None, alias="relativePath")
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )


class GetMergeCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")


class GetMergeConflictsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    merge_option: Literal[
        "FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"
    ] = Field(alias="mergeOption")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    max_conflict_files: Optional[int] = Field(default=None, alias="maxConflictFiles")
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetMergeOptionsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")


class GetPullRequestApprovalStatesInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    revision_id: str = Field(alias="revisionId")


class GetPullRequestInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")


class GetPullRequestOverrideStateInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    revision_id: str = Field(alias="revisionId")


class GetRepositoryInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")


class GetRepositoryTriggersInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")


class RepositoryTriggerModel(BaseModel):
    name: str = Field(alias="name")
    destination_arn: str = Field(alias="destinationArn")
    events: List[
        Literal["all", "createReference", "deleteReference", "updateReference"]
    ] = Field(alias="events")
    custom_data: Optional[str] = Field(default=None, alias="customData")
    branches: Optional[List[str]] = Field(default=None, alias="branches")


class ListApprovalRuleTemplatesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListBranchesInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListPullRequestsInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    author_arn: Optional[str] = Field(default=None, alias="authorArn")
    pull_request_status: Optional[Literal["CLOSED", "OPEN"]] = Field(
        default=None, alias="pullRequestStatus"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListRepositoriesForApprovalRuleTemplateInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListRepositoriesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort_by: Optional[Literal["lastModifiedDate", "repositoryName"]] = Field(
        default=None, alias="sortBy"
    )
    order: Optional[Literal["ascending", "descending"]] = Field(
        default=None, alias="order"
    )


class RepositoryNameIdPairModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    repository_id: Optional[str] = Field(default=None, alias="repositoryId")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MergeBranchesByFastForwardInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    target_branch: Optional[str] = Field(default=None, alias="targetBranch")


class MergeHunkDetailModel(BaseModel):
    start_line: Optional[int] = Field(default=None, alias="startLine")
    end_line: Optional[int] = Field(default=None, alias="endLine")
    hunk_content: Optional[str] = Field(default=None, alias="hunkContent")


class MergeMetadataModel(BaseModel):
    is_merged: Optional[bool] = Field(default=None, alias="isMerged")
    merged_by: Optional[str] = Field(default=None, alias="mergedBy")
    merge_commit_id: Optional[str] = Field(default=None, alias="mergeCommitId")
    merge_option: Optional[
        Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]
    ] = Field(default=None, alias="mergeOption")


class MergePullRequestByFastForwardInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: str = Field(alias="repositoryName")
    source_commit_id: Optional[str] = Field(default=None, alias="sourceCommitId")


class OverridePullRequestApprovalRulesInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    revision_id: str = Field(alias="revisionId")
    override_status: Literal["OVERRIDE", "REVOKE"] = Field(alias="overrideStatus")


class PostCommentReplyInputRequestModel(BaseModel):
    in_reply_to: str = Field(alias="inReplyTo")
    content: str = Field(alias="content")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class PullRequestCreatedEventMetadataModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    source_commit_id: Optional[str] = Field(default=None, alias="sourceCommitId")
    destination_commit_id: Optional[str] = Field(
        default=None, alias="destinationCommitId"
    )
    merge_base: Optional[str] = Field(default=None, alias="mergeBase")


class PullRequestSourceReferenceUpdatedEventMetadataModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    after_commit_id: Optional[str] = Field(default=None, alias="afterCommitId")
    merge_base: Optional[str] = Field(default=None, alias="mergeBase")


class PullRequestStatusChangedEventMetadataModel(BaseModel):
    pull_request_status: Optional[Literal["CLOSED", "OPEN"]] = Field(
        default=None, alias="pullRequestStatus"
    )


class PutCommentReactionInputRequestModel(BaseModel):
    comment_id: str = Field(alias="commentId")
    reaction_value: str = Field(alias="reactionValue")


class SourceFileSpecifierModel(BaseModel):
    file_path: str = Field(alias="filePath")
    is_move: Optional[bool] = Field(default=None, alias="isMove")


class PutFileInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: str = Field(alias="branchName")
    file_content: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="fileContent"
    )
    file_path: str = Field(alias="filePath")
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )
    parent_commit_id: Optional[str] = Field(default=None, alias="parentCommitId")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")


class ReactionValueFormatsModel(BaseModel):
    emoji: Optional[str] = Field(default=None, alias="emoji")
    short_code: Optional[str] = Field(default=None, alias="shortCode")
    unicode: Optional[str] = Field(default=None, alias="unicode")


class RepositoryTriggerExecutionFailureModel(BaseModel):
    trigger: Optional[str] = Field(default=None, alias="trigger")
    failure_message: Optional[str] = Field(default=None, alias="failureMessage")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateApprovalRuleTemplateContentInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    new_rule_content: str = Field(alias="newRuleContent")
    existing_rule_content_sha256: Optional[str] = Field(
        default=None, alias="existingRuleContentSha256"
    )


class UpdateApprovalRuleTemplateDescriptionInputRequestModel(BaseModel):
    approval_rule_template_name: str = Field(alias="approvalRuleTemplateName")
    approval_rule_template_description: str = Field(
        alias="approvalRuleTemplateDescription"
    )


class UpdateApprovalRuleTemplateNameInputRequestModel(BaseModel):
    old_approval_rule_template_name: str = Field(alias="oldApprovalRuleTemplateName")
    new_approval_rule_template_name: str = Field(alias="newApprovalRuleTemplateName")


class UpdateCommentInputRequestModel(BaseModel):
    comment_id: str = Field(alias="commentId")
    content: str = Field(alias="content")


class UpdateDefaultBranchInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    default_branch_name: str = Field(alias="defaultBranchName")


class UpdatePullRequestApprovalRuleContentInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    approval_rule_name: str = Field(alias="approvalRuleName")
    new_rule_content: str = Field(alias="newRuleContent")
    existing_rule_content_sha256: Optional[str] = Field(
        default=None, alias="existingRuleContentSha256"
    )


class UpdatePullRequestApprovalStateInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    revision_id: str = Field(alias="revisionId")
    approval_state: Literal["APPROVE", "REVOKE"] = Field(alias="approvalState")


class UpdatePullRequestDescriptionInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    description: str = Field(alias="description")


class UpdatePullRequestStatusInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    pull_request_status: Literal["CLOSED", "OPEN"] = Field(alias="pullRequestStatus")


class UpdatePullRequestTitleInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    title: str = Field(alias="title")


class UpdateRepositoryDescriptionInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    repository_description: Optional[str] = Field(
        default=None, alias="repositoryDescription"
    )


class UpdateRepositoryNameInputRequestModel(BaseModel):
    old_name: str = Field(alias="oldName")
    new_name: str = Field(alias="newName")


class ApprovalRuleModel(BaseModel):
    approval_rule_id: Optional[str] = Field(default=None, alias="approvalRuleId")
    approval_rule_name: Optional[str] = Field(default=None, alias="approvalRuleName")
    approval_rule_content: Optional[str] = Field(
        default=None, alias="approvalRuleContent"
    )
    rule_content_sha256: Optional[str] = Field(default=None, alias="ruleContentSha256")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_user: Optional[str] = Field(default=None, alias="lastModifiedUser")
    origin_approval_rule_template: Optional[OriginApprovalRuleTemplateModel] = Field(
        default=None, alias="originApprovalRuleTemplate"
    )


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutputModel(BaseModel):
    associated_repository_names: List[str] = Field(alias="associatedRepositoryNames")
    errors: List[BatchAssociateApprovalRuleTemplateWithRepositoriesErrorModel] = Field(
        alias="errors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApprovalRuleTemplateOutputModel(BaseModel):
    approval_rule_template: ApprovalRuleTemplateModel = Field(
        alias="approvalRuleTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUnreferencedMergeCommitOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    tree_id: str = Field(alias="treeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApprovalRuleTemplateOutputModel(BaseModel):
    approval_rule_template_id: str = Field(alias="approvalRuleTemplateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFileOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    blob_id: str = Field(alias="blobId")
    tree_id: str = Field(alias="treeId")
    file_path: str = Field(alias="filePath")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePullRequestApprovalRuleOutputModel(BaseModel):
    approval_rule_id: str = Field(alias="approvalRuleId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRepositoryOutputModel(BaseModel):
    repository_id: str = Field(alias="repositoryId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApprovalRuleTemplateOutputModel(BaseModel):
    approval_rule_template: ApprovalRuleTemplateModel = Field(
        alias="approvalRuleTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlobOutputModel(BaseModel):
    content: bytes = Field(alias="content")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFileOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    blob_id: str = Field(alias="blobId")
    file_path: str = Field(alias="filePath")
    file_mode: Literal["EXECUTABLE", "NORMAL", "SYMLINK"] = Field(alias="fileMode")
    file_size: int = Field(alias="fileSize")
    file_content: bytes = Field(alias="fileContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMergeCommitOutputModel(BaseModel):
    source_commit_id: str = Field(alias="sourceCommitId")
    destination_commit_id: str = Field(alias="destinationCommitId")
    base_commit_id: str = Field(alias="baseCommitId")
    merged_commit_id: str = Field(alias="mergedCommitId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMergeOptionsOutputModel(BaseModel):
    merge_options: List[
        Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]
    ] = Field(alias="mergeOptions")
    source_commit_id: str = Field(alias="sourceCommitId")
    destination_commit_id: str = Field(alias="destinationCommitId")
    base_commit_id: str = Field(alias="baseCommitId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPullRequestApprovalStatesOutputModel(BaseModel):
    approvals: List[ApprovalModel] = Field(alias="approvals")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPullRequestOverrideStateOutputModel(BaseModel):
    overridden: bool = Field(alias="overridden")
    overrider: str = Field(alias="overrider")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApprovalRuleTemplatesOutputModel(BaseModel):
    approval_rule_template_names: List[str] = Field(alias="approvalRuleTemplateNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedApprovalRuleTemplatesForRepositoryOutputModel(BaseModel):
    approval_rule_template_names: List[str] = Field(alias="approvalRuleTemplateNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBranchesOutputModel(BaseModel):
    branches: List[str] = Field(alias="branches")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPullRequestsOutputModel(BaseModel):
    pull_request_ids: List[str] = Field(alias="pullRequestIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRepositoriesForApprovalRuleTemplateOutputModel(BaseModel):
    repository_names: List[str] = Field(alias="repositoryNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeBranchesByFastForwardOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    tree_id: str = Field(alias="treeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeBranchesBySquashOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    tree_id: str = Field(alias="treeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeBranchesByThreeWayOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    tree_id: str = Field(alias="treeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutFileOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    blob_id: str = Field(alias="blobId")
    tree_id: str = Field(alias="treeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRepositoryTriggersOutputModel(BaseModel):
    configuration_id: str = Field(alias="configurationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApprovalRuleTemplateContentOutputModel(BaseModel):
    approval_rule_template: ApprovalRuleTemplateModel = Field(
        alias="approvalRuleTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApprovalRuleTemplateDescriptionOutputModel(BaseModel):
    approval_rule_template: ApprovalRuleTemplateModel = Field(
        alias="approvalRuleTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApprovalRuleTemplateNameOutputModel(BaseModel):
    approval_rule_template: ApprovalRuleTemplateModel = Field(
        alias="approvalRuleTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputModel(BaseModel):
    disassociated_repository_names: List[str] = Field(
        alias="disassociatedRepositoryNames"
    )
    errors: List[
        BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorModel
    ] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetRepositoriesOutputModel(BaseModel):
    repositories: List[RepositoryMetadataModel] = Field(alias="repositories")
    repositories_not_found: List[str] = Field(alias="repositoriesNotFound")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRepositoryOutputModel(BaseModel):
    repository_metadata: RepositoryMetadataModel = Field(alias="repositoryMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryOutputModel(BaseModel):
    repository_metadata: RepositoryMetadataModel = Field(alias="repositoryMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DifferenceModel(BaseModel):
    before_blob: Optional[BlobMetadataModel] = Field(default=None, alias="beforeBlob")
    after_blob: Optional[BlobMetadataModel] = Field(default=None, alias="afterBlob")
    change_type: Optional[Literal["A", "D", "M"]] = Field(
        default=None, alias="changeType"
    )


class DeleteBranchOutputModel(BaseModel):
    deleted_branch: BranchInfoModel = Field(alias="deletedBranch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBranchOutputModel(BaseModel):
    branch: BranchInfoModel = Field(alias="branch")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCommentContentOutputModel(BaseModel):
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCommentOutputModel(BaseModel):
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PostCommentReplyOutputModel(BaseModel):
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCommentOutputModel(BaseModel):
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommentsForComparedCommitModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    after_commit_id: Optional[str] = Field(default=None, alias="afterCommitId")
    before_blob_id: Optional[str] = Field(default=None, alias="beforeBlobId")
    after_blob_id: Optional[str] = Field(default=None, alias="afterBlobId")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    comments: Optional[List[CommentModel]] = Field(default=None, alias="comments")


class CommentsForPullRequestModel(BaseModel):
    pull_request_id: Optional[str] = Field(default=None, alias="pullRequestId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    after_commit_id: Optional[str] = Field(default=None, alias="afterCommitId")
    before_blob_id: Optional[str] = Field(default=None, alias="beforeBlobId")
    after_blob_id: Optional[str] = Field(default=None, alias="afterBlobId")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    comments: Optional[List[CommentModel]] = Field(default=None, alias="comments")


class PostCommentForComparedCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    after_commit_id: str = Field(alias="afterCommitId")
    content: str = Field(alias="content")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class PostCommentForComparedCommitOutputModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    before_commit_id: str = Field(alias="beforeCommitId")
    after_commit_id: str = Field(alias="afterCommitId")
    before_blob_id: str = Field(alias="beforeBlobId")
    after_blob_id: str = Field(alias="afterBlobId")
    location: LocationModel = Field(alias="location")
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PostCommentForPullRequestInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: str = Field(alias="repositoryName")
    before_commit_id: str = Field(alias="beforeCommitId")
    after_commit_id: str = Field(alias="afterCommitId")
    content: str = Field(alias="content")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class PostCommentForPullRequestOutputModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    pull_request_id: str = Field(alias="pullRequestId")
    before_commit_id: str = Field(alias="beforeCommitId")
    after_commit_id: str = Field(alias="afterCommitId")
    before_blob_id: str = Field(alias="beforeBlobId")
    after_blob_id: str = Field(alias="afterBlobId")
    location: LocationModel = Field(alias="location")
    comment: CommentModel = Field(alias="comment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CommitModel(BaseModel):
    commit_id: Optional[str] = Field(default=None, alias="commitId")
    tree_id: Optional[str] = Field(default=None, alias="treeId")
    parents: Optional[List[str]] = Field(default=None, alias="parents")
    message: Optional[str] = Field(default=None, alias="message")
    author: Optional[UserInfoModel] = Field(default=None, alias="author")
    committer: Optional[UserInfoModel] = Field(default=None, alias="committer")
    additional_data: Optional[str] = Field(default=None, alias="additionalData")


class ConflictMetadataModel(BaseModel):
    file_path: Optional[str] = Field(default=None, alias="filePath")
    file_sizes: Optional[FileSizesModel] = Field(default=None, alias="fileSizes")
    file_modes: Optional[FileModesModel] = Field(default=None, alias="fileModes")
    object_types: Optional[ObjectTypesModel] = Field(default=None, alias="objectTypes")
    number_of_conflicts: Optional[int] = Field(default=None, alias="numberOfConflicts")
    is_binary_file: Optional[IsBinaryFileModel] = Field(
        default=None, alias="isBinaryFile"
    )
    content_conflict: Optional[bool] = Field(default=None, alias="contentConflict")
    file_mode_conflict: Optional[bool] = Field(default=None, alias="fileModeConflict")
    object_type_conflict: Optional[bool] = Field(
        default=None, alias="objectTypeConflict"
    )
    merge_operations: Optional[MergeOperationsModel] = Field(
        default=None, alias="mergeOperations"
    )


class ConflictResolutionModel(BaseModel):
    replace_contents: Optional[Sequence[ReplaceContentEntryModel]] = Field(
        default=None, alias="replaceContents"
    )
    delete_files: Optional[Sequence[DeleteFileEntryModel]] = Field(
        default=None, alias="deleteFiles"
    )
    set_file_modes: Optional[Sequence[SetFileModeEntryModel]] = Field(
        default=None, alias="setFileModes"
    )


class CreateCommitOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    tree_id: str = Field(alias="treeId")
    files_added: List[FileMetadataModel] = Field(alias="filesAdded")
    files_updated: List[FileMetadataModel] = Field(alias="filesUpdated")
    files_deleted: List[FileMetadataModel] = Field(alias="filesDeleted")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePullRequestInputRequestModel(BaseModel):
    title: str = Field(alias="title")
    targets: Sequence[TargetModel] = Field(alias="targets")
    description: Optional[str] = Field(default=None, alias="description")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class DescribePullRequestEventsInputDescribePullRequestEventsPaginateModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    pull_request_event_type: Optional[
        Literal[
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_STATUS_CHANGED",
        ]
    ] = Field(default=None, alias="pullRequestEventType")
    actor_arn: Optional[str] = Field(default=None, alias="actorArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCommentsForComparedCommitInputGetCommentsForComparedCommitPaginateModel(
    BaseModel
):
    repository_name: str = Field(alias="repositoryName")
    after_commit_id: str = Field(alias="afterCommitId")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCommentsForPullRequestInputGetCommentsForPullRequestPaginateModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    before_commit_id: Optional[str] = Field(default=None, alias="beforeCommitId")
    after_commit_id: Optional[str] = Field(default=None, alias="afterCommitId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDifferencesInputGetDifferencesPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    after_commit_specifier: str = Field(alias="afterCommitSpecifier")
    before_commit_specifier: Optional[str] = Field(
        default=None, alias="beforeCommitSpecifier"
    )
    before_path: Optional[str] = Field(default=None, alias="beforePath")
    after_path: Optional[str] = Field(default=None, alias="afterPath")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBranchesInputListBranchesPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPullRequestsInputListPullRequestsPaginateModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    author_arn: Optional[str] = Field(default=None, alias="authorArn")
    pull_request_status: Optional[Literal["CLOSED", "OPEN"]] = Field(
        default=None, alias="pullRequestStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRepositoriesInputListRepositoriesPaginateModel(BaseModel):
    sort_by: Optional[Literal["lastModifiedDate", "repositoryName"]] = Field(
        default=None, alias="sortBy"
    )
    order: Optional[Literal["ascending", "descending"]] = Field(
        default=None, alias="order"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class EvaluatePullRequestApprovalRulesOutputModel(BaseModel):
    evaluation: EvaluationModel = Field(alias="evaluation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFolderOutputModel(BaseModel):
    commit_id: str = Field(alias="commitId")
    folder_path: str = Field(alias="folderPath")
    tree_id: str = Field(alias="treeId")
    sub_folders: List[FolderModel] = Field(alias="subFolders")
    files: List[FileModel] = Field(alias="files")
    symbolic_links: List[SymbolicLinkModel] = Field(alias="symbolicLinks")
    sub_modules: List[SubModuleModel] = Field(alias="subModules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRepositoryTriggersOutputModel(BaseModel):
    configuration_id: str = Field(alias="configurationId")
    triggers: List[RepositoryTriggerModel] = Field(alias="triggers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRepositoryTriggersInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    triggers: Sequence[RepositoryTriggerModel] = Field(alias="triggers")


class TestRepositoryTriggersInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    triggers: Sequence[RepositoryTriggerModel] = Field(alias="triggers")


class ListRepositoriesOutputModel(BaseModel):
    repositories: List[RepositoryNameIdPairModel] = Field(alias="repositories")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeHunkModel(BaseModel):
    is_conflict: Optional[bool] = Field(default=None, alias="isConflict")
    source: Optional[MergeHunkDetailModel] = Field(default=None, alias="source")
    destination: Optional[MergeHunkDetailModel] = Field(
        default=None, alias="destination"
    )
    base: Optional[MergeHunkDetailModel] = Field(default=None, alias="base")


class PullRequestMergedStateChangedEventMetadataModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    destination_reference: Optional[str] = Field(
        default=None, alias="destinationReference"
    )
    merge_metadata: Optional[MergeMetadataModel] = Field(
        default=None, alias="mergeMetadata"
    )


class PullRequestTargetModel(BaseModel):
    repository_name: Optional[str] = Field(default=None, alias="repositoryName")
    source_reference: Optional[str] = Field(default=None, alias="sourceReference")
    destination_reference: Optional[str] = Field(
        default=None, alias="destinationReference"
    )
    destination_commit: Optional[str] = Field(default=None, alias="destinationCommit")
    source_commit: Optional[str] = Field(default=None, alias="sourceCommit")
    merge_base: Optional[str] = Field(default=None, alias="mergeBase")
    merge_metadata: Optional[MergeMetadataModel] = Field(
        default=None, alias="mergeMetadata"
    )


class PutFileEntryModel(BaseModel):
    file_path: str = Field(alias="filePath")
    file_mode: Optional[Literal["EXECUTABLE", "NORMAL", "SYMLINK"]] = Field(
        default=None, alias="fileMode"
    )
    file_content: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="fileContent")
    source_file: Optional[SourceFileSpecifierModel] = Field(
        default=None, alias="sourceFile"
    )


class ReactionForCommentModel(BaseModel):
    reaction: Optional[ReactionValueFormatsModel] = Field(
        default=None, alias="reaction"
    )
    reaction_users: Optional[List[str]] = Field(default=None, alias="reactionUsers")
    reactions_from_deleted_users_count: Optional[int] = Field(
        default=None, alias="reactionsFromDeletedUsersCount"
    )


class TestRepositoryTriggersOutputModel(BaseModel):
    successful_executions: List[str] = Field(alias="successfulExecutions")
    failed_executions: List[RepositoryTriggerExecutionFailureModel] = Field(
        alias="failedExecutions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePullRequestApprovalRuleOutputModel(BaseModel):
    approval_rule: ApprovalRuleModel = Field(alias="approvalRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePullRequestApprovalRuleContentOutputModel(BaseModel):
    approval_rule: ApprovalRuleModel = Field(alias="approvalRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDifferencesOutputModel(BaseModel):
    differences: List[DifferenceModel] = Field(alias="differences")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCommentsForComparedCommitOutputModel(BaseModel):
    comments_for_compared_commit_data: List[CommentsForComparedCommitModel] = Field(
        alias="commentsForComparedCommitData"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCommentsForPullRequestOutputModel(BaseModel):
    comments_for_pull_request_data: List[CommentsForPullRequestModel] = Field(
        alias="commentsForPullRequestData"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetCommitsOutputModel(BaseModel):
    commits: List[CommitModel] = Field(alias="commits")
    errors: List[BatchGetCommitsErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCommitOutputModel(BaseModel):
    commit: CommitModel = Field(alias="commit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMergeConflictsOutputModel(BaseModel):
    mergeable: bool = Field(alias="mergeable")
    destination_commit_id: str = Field(alias="destinationCommitId")
    source_commit_id: str = Field(alias="sourceCommitId")
    base_commit_id: str = Field(alias="baseCommitId")
    conflict_metadata_list: List[ConflictMetadataModel] = Field(
        alias="conflictMetadataList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUnreferencedMergeCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    merge_option: Literal[
        "FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"
    ] = Field(alias="mergeOption")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="conflictResolution"
    )


class MergeBranchesBySquashInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    target_branch: Optional[str] = Field(default=None, alias="targetBranch")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="conflictResolution"
    )


class MergeBranchesByThreeWayInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    source_commit_specifier: str = Field(alias="sourceCommitSpecifier")
    destination_commit_specifier: str = Field(alias="destinationCommitSpecifier")
    target_branch: Optional[str] = Field(default=None, alias="targetBranch")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="conflictResolution"
    )


class MergePullRequestBySquashInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: str = Field(alias="repositoryName")
    source_commit_id: Optional[str] = Field(default=None, alias="sourceCommitId")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="conflictResolution"
    )


class MergePullRequestByThreeWayInputRequestModel(BaseModel):
    pull_request_id: str = Field(alias="pullRequestId")
    repository_name: str = Field(alias="repositoryName")
    source_commit_id: Optional[str] = Field(default=None, alias="sourceCommitId")
    conflict_detail_level: Optional[Literal["FILE_LEVEL", "LINE_LEVEL"]] = Field(
        default=None, alias="conflictDetailLevel"
    )
    conflict_resolution_strategy: Optional[
        Literal["ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"]
    ] = Field(default=None, alias="conflictResolutionStrategy")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="conflictResolution"
    )


class ConflictModel(BaseModel):
    conflict_metadata: Optional[ConflictMetadataModel] = Field(
        default=None, alias="conflictMetadata"
    )
    merge_hunks: Optional[List[MergeHunkModel]] = Field(
        default=None, alias="mergeHunks"
    )


class DescribeMergeConflictsOutputModel(BaseModel):
    conflict_metadata: ConflictMetadataModel = Field(alias="conflictMetadata")
    merge_hunks: List[MergeHunkModel] = Field(alias="mergeHunks")
    next_token: str = Field(alias="nextToken")
    destination_commit_id: str = Field(alias="destinationCommitId")
    source_commit_id: str = Field(alias="sourceCommitId")
    base_commit_id: str = Field(alias="baseCommitId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PullRequestEventModel(BaseModel):
    pull_request_id: Optional[str] = Field(default=None, alias="pullRequestId")
    event_date: Optional[datetime] = Field(default=None, alias="eventDate")
    pull_request_event_type: Optional[
        Literal[
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_STATUS_CHANGED",
        ]
    ] = Field(default=None, alias="pullRequestEventType")
    actor_arn: Optional[str] = Field(default=None, alias="actorArn")
    pull_request_created_event_metadata: Optional[
        PullRequestCreatedEventMetadataModel
    ] = Field(default=None, alias="pullRequestCreatedEventMetadata")
    pull_request_status_changed_event_metadata: Optional[
        PullRequestStatusChangedEventMetadataModel
    ] = Field(default=None, alias="pullRequestStatusChangedEventMetadata")
    pull_request_source_reference_updated_event_metadata: Optional[
        PullRequestSourceReferenceUpdatedEventMetadataModel
    ] = Field(default=None, alias="pullRequestSourceReferenceUpdatedEventMetadata")
    pull_request_merged_state_changed_event_metadata: Optional[
        PullRequestMergedStateChangedEventMetadataModel
    ] = Field(default=None, alias="pullRequestMergedStateChangedEventMetadata")
    approval_rule_event_metadata: Optional[ApprovalRuleEventMetadataModel] = Field(
        default=None, alias="approvalRuleEventMetadata"
    )
    approval_state_changed_event_metadata: Optional[
        ApprovalStateChangedEventMetadataModel
    ] = Field(default=None, alias="approvalStateChangedEventMetadata")
    approval_rule_overridden_event_metadata: Optional[
        ApprovalRuleOverriddenEventMetadataModel
    ] = Field(default=None, alias="approvalRuleOverriddenEventMetadata")


class PullRequestModel(BaseModel):
    pull_request_id: Optional[str] = Field(default=None, alias="pullRequestId")
    title: Optional[str] = Field(default=None, alias="title")
    description: Optional[str] = Field(default=None, alias="description")
    last_activity_date: Optional[datetime] = Field(
        default=None, alias="lastActivityDate"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    pull_request_status: Optional[Literal["CLOSED", "OPEN"]] = Field(
        default=None, alias="pullRequestStatus"
    )
    author_arn: Optional[str] = Field(default=None, alias="authorArn")
    pull_request_targets: Optional[List[PullRequestTargetModel]] = Field(
        default=None, alias="pullRequestTargets"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    approval_rules: Optional[List[ApprovalRuleModel]] = Field(
        default=None, alias="approvalRules"
    )


class CreateCommitInputRequestModel(BaseModel):
    repository_name: str = Field(alias="repositoryName")
    branch_name: str = Field(alias="branchName")
    parent_commit_id: Optional[str] = Field(default=None, alias="parentCommitId")
    author_name: Optional[str] = Field(default=None, alias="authorName")
    email: Optional[str] = Field(default=None, alias="email")
    commit_message: Optional[str] = Field(default=None, alias="commitMessage")
    keep_empty_folders: Optional[bool] = Field(default=None, alias="keepEmptyFolders")
    put_files: Optional[Sequence[PutFileEntryModel]] = Field(
        default=None, alias="putFiles"
    )
    delete_files: Optional[Sequence[DeleteFileEntryModel]] = Field(
        default=None, alias="deleteFiles"
    )
    set_file_modes: Optional[Sequence[SetFileModeEntryModel]] = Field(
        default=None, alias="setFileModes"
    )


class GetCommentReactionsOutputModel(BaseModel):
    reactions_for_comment: List[ReactionForCommentModel] = Field(
        alias="reactionsForComment"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDescribeMergeConflictsOutputModel(BaseModel):
    conflicts: List[ConflictModel] = Field(alias="conflicts")
    next_token: str = Field(alias="nextToken")
    errors: List[BatchDescribeMergeConflictsErrorModel] = Field(alias="errors")
    destination_commit_id: str = Field(alias="destinationCommitId")
    source_commit_id: str = Field(alias="sourceCommitId")
    base_commit_id: str = Field(alias="baseCommitId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePullRequestEventsOutputModel(BaseModel):
    pull_request_events: List[PullRequestEventModel] = Field(alias="pullRequestEvents")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePullRequestOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPullRequestOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergePullRequestByFastForwardOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergePullRequestBySquashOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergePullRequestByThreeWayOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePullRequestDescriptionOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePullRequestStatusOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePullRequestTitleOutputModel(BaseModel):
    pull_request: PullRequestModel = Field(alias="pullRequest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
