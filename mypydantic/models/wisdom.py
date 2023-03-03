# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AppIntegrationsConfigurationModel(BaseModel):
    app_integration_arn: str = Field(alias="appIntegrationArn")
    object_fields: Sequence[str] = Field(alias="objectFields")


class AssistantAssociationInputDataModel(BaseModel):
    knowledge_base_id: Optional[str] = Field(default=None, alias="knowledgeBaseId")


class KnowledgeBaseAssociationDataModel(BaseModel):
    knowledge_base_arn: Optional[str] = Field(default=None, alias="knowledgeBaseArn")
    knowledge_base_id: Optional[str] = Field(default=None, alias="knowledgeBaseId")


class ServerSideEncryptionConfigurationModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class ContentDataModel(BaseModel):
    content_arn: str = Field(alias="contentArn")
    content_id: str = Field(alias="contentId")
    content_type: str = Field(alias="contentType")
    knowledge_base_arn: str = Field(alias="knowledgeBaseArn")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    metadata: Dict[str, str] = Field(alias="metadata")
    name: str = Field(alias="name")
    revision_id: str = Field(alias="revisionId")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_FAILED",
    ] = Field(alias="status")
    title: str = Field(alias="title")
    url: str = Field(alias="url")
    url_expiry: datetime = Field(alias="urlExpiry")
    link_out_uri: Optional[str] = Field(default=None, alias="linkOutUri")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ContentReferenceModel(BaseModel):
    content_arn: Optional[str] = Field(default=None, alias="contentArn")
    content_id: Optional[str] = Field(default=None, alias="contentId")
    knowledge_base_arn: Optional[str] = Field(default=None, alias="knowledgeBaseArn")
    knowledge_base_id: Optional[str] = Field(default=None, alias="knowledgeBaseId")


class ContentSummaryModel(BaseModel):
    content_arn: str = Field(alias="contentArn")
    content_id: str = Field(alias="contentId")
    content_type: str = Field(alias="contentType")
    knowledge_base_arn: str = Field(alias="knowledgeBaseArn")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    metadata: Dict[str, str] = Field(alias="metadata")
    name: str = Field(alias="name")
    revision_id: str = Field(alias="revisionId")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_FAILED",
    ] = Field(alias="status")
    title: str = Field(alias="title")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateContentRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    name: str = Field(alias="name")
    upload_id: str = Field(alias="uploadId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="metadata")
    override_link_out_uri: Optional[str] = Field(
        default=None, alias="overrideLinkOutUri"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    title: Optional[str] = Field(default=None, alias="title")


class RenderingConfigurationModel(BaseModel):
    template_uri: Optional[str] = Field(default=None, alias="templateUri")


class CreateSessionRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class SessionDataModel(BaseModel):
    name: str = Field(alias="name")
    session_arn: str = Field(alias="sessionArn")
    session_id: str = Field(alias="sessionId")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DeleteAssistantAssociationRequestModel(BaseModel):
    assistant_association_id: str = Field(alias="assistantAssociationId")
    assistant_id: str = Field(alias="assistantId")


class DeleteAssistantRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")


class DeleteContentRequestModel(BaseModel):
    content_id: str = Field(alias="contentId")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class DeleteKnowledgeBaseRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class HighlightModel(BaseModel):
    begin_offset_inclusive: Optional[int] = Field(
        default=None, alias="beginOffsetInclusive"
    )
    end_offset_exclusive: Optional[int] = Field(
        default=None, alias="endOffsetExclusive"
    )


class FilterModel(BaseModel):
    field: Literal["NAME"] = Field(alias="field")
    operator: Literal["EQUALS"] = Field(alias="operator")
    value: str = Field(alias="value")


class GetAssistantAssociationRequestModel(BaseModel):
    assistant_association_id: str = Field(alias="assistantAssociationId")
    assistant_id: str = Field(alias="assistantId")


class GetAssistantRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")


class GetContentRequestModel(BaseModel):
    content_id: str = Field(alias="contentId")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class GetContentSummaryRequestModel(BaseModel):
    content_id: str = Field(alias="contentId")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class GetKnowledgeBaseRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class GetRecommendationsRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    session_id: str = Field(alias="sessionId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    wait_time_seconds: Optional[int] = Field(default=None, alias="waitTimeSeconds")


class GetSessionRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    session_id: str = Field(alias="sessionId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAssistantAssociationsRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAssistantsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListContentsRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListKnowledgeBasesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class NotifyRecommendationsReceivedErrorModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    recommendation_id: Optional[str] = Field(default=None, alias="recommendationId")


class NotifyRecommendationsReceivedRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    recommendation_ids: Sequence[str] = Field(alias="recommendationIds")
    session_id: str = Field(alias="sessionId")


class QueryAssistantRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    query_text: str = Field(alias="queryText")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class QueryRecommendationTriggerDataModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="text")


class RemoveKnowledgeBaseTemplateUriRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class SessionSummaryModel(BaseModel):
    assistant_arn: str = Field(alias="assistantArn")
    assistant_id: str = Field(alias="assistantId")
    session_arn: str = Field(alias="sessionArn")
    session_id: str = Field(alias="sessionId")


class StartContentUploadRequestModel(BaseModel):
    content_type: str = Field(alias="contentType")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateContentRequestModel(BaseModel):
    content_id: str = Field(alias="contentId")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    metadata: Optional[Mapping[str, str]] = Field(default=None, alias="metadata")
    override_link_out_uri: Optional[str] = Field(
        default=None, alias="overrideLinkOutUri"
    )
    remove_override_link_out_uri: Optional[bool] = Field(
        default=None, alias="removeOverrideLinkOutUri"
    )
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    title: Optional[str] = Field(default=None, alias="title")
    upload_id: Optional[str] = Field(default=None, alias="uploadId")


class UpdateKnowledgeBaseTemplateUriRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    template_uri: str = Field(alias="templateUri")


class SourceConfigurationModel(BaseModel):
    app_integrations: Optional[AppIntegrationsConfigurationModel] = Field(
        default=None, alias="appIntegrations"
    )


class CreateAssistantAssociationRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    association: AssistantAssociationInputDataModel = Field(alias="association")
    association_type: Literal["KNOWLEDGE_BASE"] = Field(alias="associationType")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class AssistantAssociationOutputDataModel(BaseModel):
    knowledge_base_association: Optional[KnowledgeBaseAssociationDataModel] = Field(
        default=None, alias="knowledgeBaseAssociation"
    )


class AssistantDataModel(BaseModel):
    assistant_arn: str = Field(alias="assistantArn")
    assistant_id: str = Field(alias="assistantId")
    name: str = Field(alias="name")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
    ] = Field(alias="status")
    type: Literal["AGENT"] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AssistantSummaryModel(BaseModel):
    assistant_arn: str = Field(alias="assistantArn")
    assistant_id: str = Field(alias="assistantId")
    name: str = Field(alias="name")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
    ] = Field(alias="status")
    type: Literal["AGENT"] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateAssistantRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["AGENT"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateContentResponseModel(BaseModel):
    content: ContentDataModel = Field(alias="content")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContentResponseModel(BaseModel):
    content: ContentDataModel = Field(alias="content")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContentSummaryResponseModel(BaseModel):
    content_summary: ContentSummaryModel = Field(alias="contentSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContentsResponseModel(BaseModel):
    content_summaries: List[ContentSummaryModel] = Field(alias="contentSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchContentResponseModel(BaseModel):
    content_summaries: List[ContentSummaryModel] = Field(alias="contentSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContentUploadResponseModel(BaseModel):
    headers_to_include: Dict[str, str] = Field(alias="headersToInclude")
    upload_id: str = Field(alias="uploadId")
    url: str = Field(alias="url")
    url_expiry: datetime = Field(alias="urlExpiry")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContentResponseModel(BaseModel):
    content: ContentDataModel = Field(alias="content")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSessionResponseModel(BaseModel):
    session: SessionDataModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSessionResponseModel(BaseModel):
    session: SessionDataModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentTextModel(BaseModel):
    highlights: Optional[List[HighlightModel]] = Field(default=None, alias="highlights")
    text: Optional[str] = Field(default=None, alias="text")


class SearchExpressionModel(BaseModel):
    filters: Sequence[FilterModel] = Field(alias="filters")


class ListAssistantAssociationsRequestListAssistantAssociationsPaginateModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssistantsRequestListAssistantsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListContentsRequestListContentsPaginateModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKnowledgeBasesRequestListKnowledgeBasesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class QueryAssistantRequestQueryAssistantPaginateModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    query_text: str = Field(alias="queryText")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class NotifyRecommendationsReceivedResponseModel(BaseModel):
    errors: List[NotifyRecommendationsReceivedErrorModel] = Field(alias="errors")
    recommendation_ids: List[str] = Field(alias="recommendationIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationTriggerDataModel(BaseModel):
    query: Optional[QueryRecommendationTriggerDataModel] = Field(
        default=None, alias="query"
    )


class SearchSessionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    session_summaries: List[SessionSummaryModel] = Field(alias="sessionSummaries")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateKnowledgeBaseRequestModel(BaseModel):
    knowledge_base_type: Literal["CUSTOM", "EXTERNAL"] = Field(
        alias="knowledgeBaseType"
    )
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    rendering_configuration: Optional[RenderingConfigurationModel] = Field(
        default=None, alias="renderingConfiguration"
    )
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="sourceConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class KnowledgeBaseDataModel(BaseModel):
    knowledge_base_arn: str = Field(alias="knowledgeBaseArn")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    knowledge_base_type: Literal["CUSTOM", "EXTERNAL"] = Field(
        alias="knowledgeBaseType"
    )
    name: str = Field(alias="name")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
    ] = Field(alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    last_content_modification_time: Optional[datetime] = Field(
        default=None, alias="lastContentModificationTime"
    )
    rendering_configuration: Optional[RenderingConfigurationModel] = Field(
        default=None, alias="renderingConfiguration"
    )
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="sourceConfiguration"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class KnowledgeBaseSummaryModel(BaseModel):
    knowledge_base_arn: str = Field(alias="knowledgeBaseArn")
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    knowledge_base_type: Literal["CUSTOM", "EXTERNAL"] = Field(
        alias="knowledgeBaseType"
    )
    name: str = Field(alias="name")
    status: Literal[
        "ACTIVE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETED",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
    ] = Field(alias="status")
    description: Optional[str] = Field(default=None, alias="description")
    rendering_configuration: Optional[RenderingConfigurationModel] = Field(
        default=None, alias="renderingConfiguration"
    )
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="serverSideEncryptionConfiguration")
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="sourceConfiguration"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AssistantAssociationDataModel(BaseModel):
    assistant_arn: str = Field(alias="assistantArn")
    assistant_association_arn: str = Field(alias="assistantAssociationArn")
    assistant_association_id: str = Field(alias="assistantAssociationId")
    assistant_id: str = Field(alias="assistantId")
    association_data: AssistantAssociationOutputDataModel = Field(
        alias="associationData"
    )
    association_type: Literal["KNOWLEDGE_BASE"] = Field(alias="associationType")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AssistantAssociationSummaryModel(BaseModel):
    assistant_arn: str = Field(alias="assistantArn")
    assistant_association_arn: str = Field(alias="assistantAssociationArn")
    assistant_association_id: str = Field(alias="assistantAssociationId")
    assistant_id: str = Field(alias="assistantId")
    association_data: AssistantAssociationOutputDataModel = Field(
        alias="associationData"
    )
    association_type: Literal["KNOWLEDGE_BASE"] = Field(alias="associationType")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateAssistantResponseModel(BaseModel):
    assistant: AssistantDataModel = Field(alias="assistant")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssistantResponseModel(BaseModel):
    assistant: AssistantDataModel = Field(alias="assistant")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssistantsResponseModel(BaseModel):
    assistant_summaries: List[AssistantSummaryModel] = Field(alias="assistantSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentModel(BaseModel):
    content_reference: ContentReferenceModel = Field(alias="contentReference")
    excerpt: Optional[DocumentTextModel] = Field(default=None, alias="excerpt")
    title: Optional[DocumentTextModel] = Field(default=None, alias="title")


class SearchContentRequestModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    search_expression: SearchExpressionModel = Field(alias="searchExpression")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchContentRequestSearchContentPaginateModel(BaseModel):
    knowledge_base_id: str = Field(alias="knowledgeBaseId")
    search_expression: SearchExpressionModel = Field(alias="searchExpression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchSessionsRequestModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    search_expression: SearchExpressionModel = Field(alias="searchExpression")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SearchSessionsRequestSearchSessionsPaginateModel(BaseModel):
    assistant_id: str = Field(alias="assistantId")
    search_expression: SearchExpressionModel = Field(alias="searchExpression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RecommendationTriggerModel(BaseModel):
    data: RecommendationTriggerDataModel = Field(alias="data")
    id: str = Field(alias="id")
    recommendation_ids: List[str] = Field(alias="recommendationIds")
    source: Literal["ISSUE_DETECTION", "OTHER", "RULE_EVALUATION"] = Field(
        alias="source"
    )
    type: Literal["QUERY"] = Field(alias="type")


class CreateKnowledgeBaseResponseModel(BaseModel):
    knowledge_base: KnowledgeBaseDataModel = Field(alias="knowledgeBase")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKnowledgeBaseResponseModel(BaseModel):
    knowledge_base: KnowledgeBaseDataModel = Field(alias="knowledgeBase")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateKnowledgeBaseTemplateUriResponseModel(BaseModel):
    knowledge_base: KnowledgeBaseDataModel = Field(alias="knowledgeBase")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKnowledgeBasesResponseModel(BaseModel):
    knowledge_base_summaries: List[KnowledgeBaseSummaryModel] = Field(
        alias="knowledgeBaseSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAssistantAssociationResponseModel(BaseModel):
    assistant_association: AssistantAssociationDataModel = Field(
        alias="assistantAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssistantAssociationResponseModel(BaseModel):
    assistant_association: AssistantAssociationDataModel = Field(
        alias="assistantAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssistantAssociationsResponseModel(BaseModel):
    assistant_association_summaries: List[AssistantAssociationSummaryModel] = Field(
        alias="assistantAssociationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationDataModel(BaseModel):
    document: DocumentModel = Field(alias="document")
    recommendation_id: str = Field(alias="recommendationId")
    relevance_level: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="relevanceLevel"
    )
    relevance_score: Optional[float] = Field(default=None, alias="relevanceScore")
    type: Optional[Literal["KNOWLEDGE_CONTENT"]] = Field(default=None, alias="type")


class ResultDataModel(BaseModel):
    document: DocumentModel = Field(alias="document")
    result_id: str = Field(alias="resultId")
    relevance_score: Optional[float] = Field(default=None, alias="relevanceScore")


class GetRecommendationsResponseModel(BaseModel):
    recommendations: List[RecommendationDataModel] = Field(alias="recommendations")
    triggers: List[RecommendationTriggerModel] = Field(alias="triggers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryAssistantResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    results: List[ResultDataModel] = Field(alias="results")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
