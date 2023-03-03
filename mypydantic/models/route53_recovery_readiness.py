# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CellOutputModel(BaseModel):
    cell_arn: str = Field(alias="CellArn")
    cell_name: str = Field(alias="CellName")
    cells: List[str] = Field(alias="Cells")
    parent_readiness_scopes: List[str] = Field(alias="ParentReadinessScopes")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class CreateCellRequestModel(BaseModel):
    cell_name: str = Field(alias="CellName")
    cells: Optional[Sequence[str]] = Field(default=None, alias="Cells")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateCrossAccountAuthorizationRequestModel(BaseModel):
    cross_account_authorization: str = Field(alias="CrossAccountAuthorization")


class CreateReadinessCheckRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_set_name: str = Field(alias="ResourceSetName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateRecoveryGroupRequestModel(BaseModel):
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    cells: Optional[Sequence[str]] = Field(default=None, alias="Cells")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteCellRequestModel(BaseModel):
    cell_name: str = Field(alias="CellName")


class DeleteCrossAccountAuthorizationRequestModel(BaseModel):
    cross_account_authorization: str = Field(alias="CrossAccountAuthorization")


class DeleteReadinessCheckRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")


class DeleteRecoveryGroupRequestModel(BaseModel):
    recovery_group_name: str = Field(alias="RecoveryGroupName")


class DeleteResourceSetRequestModel(BaseModel):
    resource_set_name: str = Field(alias="ResourceSetName")


class GetArchitectureRecommendationsRequestModel(BaseModel):
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RecommendationModel(BaseModel):
    recommendation_text: str = Field(alias="RecommendationText")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetCellReadinessSummaryRequestModel(BaseModel):
    cell_name: str = Field(alias="CellName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ReadinessCheckSummaryModel(BaseModel):
    readiness: Optional[
        Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"]
    ] = Field(default=None, alias="Readiness")
    readiness_check_name: Optional[str] = Field(
        default=None, alias="ReadinessCheckName"
    )


class GetCellRequestModel(BaseModel):
    cell_name: str = Field(alias="CellName")


class GetReadinessCheckRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")


class GetReadinessCheckResourceStatusRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_identifier: str = Field(alias="ResourceIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetReadinessCheckStatusRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MessageModel(BaseModel):
    message_text: Optional[str] = Field(default=None, alias="MessageText")


class ResourceResultModel(BaseModel):
    last_checked_timestamp: datetime = Field(alias="LastCheckedTimestamp")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class GetRecoveryGroupReadinessSummaryRequestModel(BaseModel):
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetRecoveryGroupRequestModel(BaseModel):
    recovery_group_name: str = Field(alias="RecoveryGroupName")


class GetResourceSetRequestModel(BaseModel):
    resource_set_name: str = Field(alias="ResourceSetName")


class ListCellsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCrossAccountAuthorizationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListReadinessChecksRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ReadinessCheckOutputModel(BaseModel):
    readiness_check_arn: str = Field(alias="ReadinessCheckArn")
    resource_set: str = Field(alias="ResourceSet")
    readiness_check_name: Optional[str] = Field(
        default=None, alias="ReadinessCheckName"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListRecoveryGroupsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RecoveryGroupOutputModel(BaseModel):
    cells: List[str] = Field(alias="Cells")
    recovery_group_arn: str = Field(alias="RecoveryGroupArn")
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListResourceSetsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRulesOutputModel(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    rule_description: str = Field(alias="RuleDescription")
    rule_id: str = Field(alias="RuleId")


class ListRulesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class ListTagsForResourcesRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NLBResourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class R53ResourceRecordModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    record_set_id: Optional[str] = Field(default=None, alias="RecordSetId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateCellRequestModel(BaseModel):
    cell_name: str = Field(alias="CellName")
    cells: Sequence[str] = Field(alias="Cells")


class UpdateReadinessCheckRequestModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_set_name: str = Field(alias="ResourceSetName")


class UpdateRecoveryGroupRequestModel(BaseModel):
    cells: Sequence[str] = Field(alias="Cells")
    recovery_group_name: str = Field(alias="RecoveryGroupName")


class CreateCellResponseModel(BaseModel):
    cell_arn: str = Field(alias="CellArn")
    cell_name: str = Field(alias="CellName")
    cells: List[str] = Field(alias="Cells")
    parent_readiness_scopes: List[str] = Field(alias="ParentReadinessScopes")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCrossAccountAuthorizationResponseModel(BaseModel):
    cross_account_authorization: str = Field(alias="CrossAccountAuthorization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateReadinessCheckResponseModel(BaseModel):
    readiness_check_arn: str = Field(alias="ReadinessCheckArn")
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_set: str = Field(alias="ResourceSet")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRecoveryGroupResponseModel(BaseModel):
    cells: List[str] = Field(alias="Cells")
    recovery_group_arn: str = Field(alias="RecoveryGroupArn")
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCellResponseModel(BaseModel):
    cell_arn: str = Field(alias="CellArn")
    cell_name: str = Field(alias="CellName")
    cells: List[str] = Field(alias="Cells")
    parent_readiness_scopes: List[str] = Field(alias="ParentReadinessScopes")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReadinessCheckResponseModel(BaseModel):
    readiness_check_arn: str = Field(alias="ReadinessCheckArn")
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_set: str = Field(alias="ResourceSet")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecoveryGroupResponseModel(BaseModel):
    cells: List[str] = Field(alias="Cells")
    recovery_group_arn: str = Field(alias="RecoveryGroupArn")
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCellsResponseModel(BaseModel):
    cells: List[CellOutputModel] = Field(alias="Cells")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCrossAccountAuthorizationsResponseModel(BaseModel):
    cross_account_authorizations: List[str] = Field(alias="CrossAccountAuthorizations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourcesResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCellResponseModel(BaseModel):
    cell_arn: str = Field(alias="CellArn")
    cell_name: str = Field(alias="CellName")
    cells: List[str] = Field(alias="Cells")
    parent_readiness_scopes: List[str] = Field(alias="ParentReadinessScopes")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateReadinessCheckResponseModel(BaseModel):
    readiness_check_arn: str = Field(alias="ReadinessCheckArn")
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_set: str = Field(alias="ResourceSet")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecoveryGroupResponseModel(BaseModel):
    cells: List[str] = Field(alias="Cells")
    recovery_group_arn: str = Field(alias="RecoveryGroupArn")
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetArchitectureRecommendationsResponseModel(BaseModel):
    last_audit_timestamp: datetime = Field(alias="LastAuditTimestamp")
    next_token: str = Field(alias="NextToken")
    recommendations: List[RecommendationModel] = Field(alias="Recommendations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateModel(BaseModel):
    cell_name: str = Field(alias="CellName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateModel(
    BaseModel
):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    resource_identifier: str = Field(alias="ResourceIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateModel(BaseModel):
    readiness_check_name: str = Field(alias="ReadinessCheckName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateModel(
    BaseModel
):
    recovery_group_name: str = Field(alias="RecoveryGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCellsRequestListCellsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListReadinessChecksRequestListReadinessChecksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRecoveryGroupsRequestListRecoveryGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceSetsRequestListResourceSetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRulesRequestListRulesPaginateModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCellReadinessSummaryResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    readiness_checks: List[ReadinessCheckSummaryModel] = Field(alias="ReadinessChecks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecoveryGroupReadinessSummaryResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    readiness_checks: List[ReadinessCheckSummaryModel] = Field(alias="ReadinessChecks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleResultModel(BaseModel):
    last_checked_timestamp: datetime = Field(alias="LastCheckedTimestamp")
    messages: List[MessageModel] = Field(alias="Messages")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    rule_id: str = Field(alias="RuleId")


class GetReadinessCheckStatusResponseModel(BaseModel):
    messages: List[MessageModel] = Field(alias="Messages")
    next_token: str = Field(alias="NextToken")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    resources: List[ResourceResultModel] = Field(alias="Resources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReadinessChecksResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    readiness_checks: List[ReadinessCheckOutputModel] = Field(alias="ReadinessChecks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecoveryGroupsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    recovery_groups: List[RecoveryGroupOutputModel] = Field(alias="RecoveryGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRulesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    rules: List[ListRulesOutputModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetResourceModel(BaseModel):
    nl_bresource: Optional[NLBResourceModel] = Field(default=None, alias="NLBResource")
    r53_resource: Optional[R53ResourceRecordModel] = Field(
        default=None, alias="R53Resource"
    )


class GetReadinessCheckResourceStatusResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    readiness: Literal["NOT_AUTHORIZED", "NOT_READY", "READY", "UNKNOWN"] = Field(
        alias="Readiness"
    )
    rules: List[RuleResultModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DNSTargetResourceModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    hosted_zone_arn: Optional[str] = Field(default=None, alias="HostedZoneArn")
    record_set_id: Optional[str] = Field(default=None, alias="RecordSetId")
    record_type: Optional[str] = Field(default=None, alias="RecordType")
    target_resource: Optional[TargetResourceModel] = Field(
        default=None, alias="TargetResource"
    )


class ResourceModel(BaseModel):
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    dns_target_resource: Optional[DNSTargetResourceModel] = Field(
        default=None, alias="DnsTargetResource"
    )
    readiness_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="ReadinessScopes"
    )
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class CreateResourceSetRequestModel(BaseModel):
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: Sequence[ResourceModel] = Field(alias="Resources")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateResourceSetResponseModel(BaseModel):
    resource_set_arn: str = Field(alias="ResourceSetArn")
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: List[ResourceModel] = Field(alias="Resources")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceSetResponseModel(BaseModel):
    resource_set_arn: str = Field(alias="ResourceSetArn")
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: List[ResourceModel] = Field(alias="Resources")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceSetOutputModel(BaseModel):
    resource_set_arn: str = Field(alias="ResourceSetArn")
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: List[ResourceModel] = Field(alias="Resources")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateResourceSetRequestModel(BaseModel):
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: Sequence[ResourceModel] = Field(alias="Resources")


class UpdateResourceSetResponseModel(BaseModel):
    resource_set_arn: str = Field(alias="ResourceSetArn")
    resource_set_name: str = Field(alias="ResourceSetName")
    resource_set_type: str = Field(alias="ResourceSetType")
    resources: List[ResourceModel] = Field(alias="Resources")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceSetsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    resource_sets: List[ResourceSetOutputModel] = Field(alias="ResourceSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
