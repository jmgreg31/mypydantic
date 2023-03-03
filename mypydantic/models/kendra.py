# Model Generated: Thu Mar  2 21:56:20 2023

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


class AccessControlConfigurationSummaryModel(BaseModel):
    id: str = Field(alias="Id")


class AccessControlListConfigurationModel(BaseModel):
    key_path: Optional[str] = Field(default=None, alias="KeyPath")


class AclConfigurationModel(BaseModel):
    allowed_groups_column_name: str = Field(alias="AllowedGroupsColumnName")


class DataSourceToIndexFieldMappingModel(BaseModel):
    data_source_field_name: str = Field(alias="DataSourceFieldName")
    index_field_name: str = Field(alias="IndexFieldName")
    date_field_format: Optional[str] = Field(default=None, alias="DateFieldFormat")


class DataSourceVpcConfigurationModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")


class S3PathModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")


class EntityConfigurationModel(BaseModel):
    entity_id: str = Field(alias="EntityId")
    entity_type: Literal["GROUP", "USER"] = Field(alias="EntityType")


class FailedEntityModel(BaseModel):
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EntityPersonaConfigurationModel(BaseModel):
    entity_id: str = Field(alias="EntityId")
    persona: Literal["OWNER", "VIEWER"] = Field(alias="Persona")


class BasicAuthenticationConfigurationModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    credentials: str = Field(alias="Credentials")


class DataSourceSyncJobMetricTargetModel(BaseModel):
    data_source_id: str = Field(alias="DataSourceId")
    data_source_sync_job_id: Optional[str] = Field(
        default=None, alias="DataSourceSyncJobId"
    )


class BatchDeleteDocumentResponseFailedDocumentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    error_code: Optional[Literal["InternalError", "InvalidRequest"]] = Field(
        default=None, alias="ErrorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class BatchGetDocumentStatusResponseErrorModel(BaseModel):
    document_id: Optional[str] = Field(default=None, alias="DocumentId")
    error_code: Optional[Literal["InternalError", "InvalidRequest"]] = Field(
        default=None, alias="ErrorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class StatusModel(BaseModel):
    document_id: Optional[str] = Field(default=None, alias="DocumentId")
    document_status: Optional[
        Literal[
            "FAILED", "INDEXED", "NOT_FOUND", "PROCESSING", "UPDATED", "UPDATE_FAILED"
        ]
    ] = Field(default=None, alias="DocumentStatus")
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class BatchPutDocumentResponseFailedDocumentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    error_code: Optional[Literal["InternalError", "InvalidRequest"]] = Field(
        default=None, alias="ErrorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class CapacityUnitsConfigurationModel(BaseModel):
    storage_capacity_units: int = Field(alias="StorageCapacityUnits")
    query_capacity_units: int = Field(alias="QueryCapacityUnits")


class ClearQuerySuggestionsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")


class ClickFeedbackModel(BaseModel):
    result_id: str = Field(alias="ResultId")
    click_time: Union[datetime, str] = Field(alias="ClickTime")


class ConfluenceAttachmentToIndexFieldMappingModel(BaseModel):
    data_source_field_name: Optional[
        Literal[
            "AUTHOR",
            "CONTENT_TYPE",
            "CREATED_DATE",
            "DISPLAY_URL",
            "FILE_SIZE",
            "ITEM_TYPE",
            "PARENT_ID",
            "SPACE_KEY",
            "SPACE_NAME",
            "URL",
            "VERSION",
        ]
    ] = Field(default=None, alias="DataSourceFieldName")
    date_field_format: Optional[str] = Field(default=None, alias="DateFieldFormat")
    index_field_name: Optional[str] = Field(default=None, alias="IndexFieldName")


class ConfluenceBlogToIndexFieldMappingModel(BaseModel):
    data_source_field_name: Optional[
        Literal[
            "AUTHOR",
            "DISPLAY_URL",
            "ITEM_TYPE",
            "LABELS",
            "PUBLISH_DATE",
            "SPACE_KEY",
            "SPACE_NAME",
            "URL",
            "VERSION",
        ]
    ] = Field(default=None, alias="DataSourceFieldName")
    date_field_format: Optional[str] = Field(default=None, alias="DateFieldFormat")
    index_field_name: Optional[str] = Field(default=None, alias="IndexFieldName")


class ProxyConfigurationModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    credentials: Optional[str] = Field(default=None, alias="Credentials")


class ConfluencePageToIndexFieldMappingModel(BaseModel):
    data_source_field_name: Optional[
        Literal[
            "AUTHOR",
            "CONTENT_STATUS",
            "CREATED_DATE",
            "DISPLAY_URL",
            "ITEM_TYPE",
            "LABELS",
            "MODIFIED_DATE",
            "PARENT_ID",
            "SPACE_KEY",
            "SPACE_NAME",
            "URL",
            "VERSION",
        ]
    ] = Field(default=None, alias="DataSourceFieldName")
    date_field_format: Optional[str] = Field(default=None, alias="DateFieldFormat")
    index_field_name: Optional[str] = Field(default=None, alias="IndexFieldName")


class ConfluenceSpaceToIndexFieldMappingModel(BaseModel):
    data_source_field_name: Optional[
        Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"]
    ] = Field(default=None, alias="DataSourceFieldName")
    date_field_format: Optional[str] = Field(default=None, alias="DateFieldFormat")
    index_field_name: Optional[str] = Field(default=None, alias="IndexFieldName")


class ConnectionConfigurationModel(BaseModel):
    database_host: str = Field(alias="DatabaseHost")
    database_port: int = Field(alias="DatabasePort")
    database_name: str = Field(alias="DatabaseName")
    table_name: str = Field(alias="TableName")
    secret_arn: str = Field(alias="SecretArn")


class ContentSourceConfigurationModel(BaseModel):
    data_source_ids: Optional[Sequence[str]] = Field(
        default=None, alias="DataSourceIds"
    )
    faq_ids: Optional[Sequence[str]] = Field(default=None, alias="FaqIds")
    direct_put_content: Optional[bool] = Field(default=None, alias="DirectPutContent")


class CorrectionModel(BaseModel):
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    term: Optional[str] = Field(default=None, alias="Term")
    corrected_term: Optional[str] = Field(default=None, alias="CorrectedTerm")


class PrincipalModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal["GROUP", "USER"] = Field(alias="Type")
    access: Literal["ALLOW", "DENY"] = Field(alias="Access")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ServerSideEncryptionConfigurationModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class UserGroupResolutionConfigurationModel(BaseModel):
    user_group_resolution_mode: Literal["AWS_SSO", "NONE"] = Field(
        alias="UserGroupResolutionMode"
    )


class TemplateConfigurationModel(BaseModel):
    template: Optional[Mapping[str, Any]] = Field(default=None, alias="Template")


class DataSourceGroupModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    data_source_id: str = Field(alias="DataSourceId")


class DataSourceSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[
        Literal[
            "ALFRESCO",
            "BOX",
            "CONFLUENCE",
            "CUSTOM",
            "DATABASE",
            "FSX",
            "GITHUB",
            "GOOGLEDRIVE",
            "JIRA",
            "ONEDRIVE",
            "QUIP",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SHAREPOINT",
            "SLACK",
            "TEMPLATE",
            "WEBCRAWLER",
            "WORKDOCS",
        ]
    ] = Field(default=None, alias="Type")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")


class DataSourceSyncJobMetricsModel(BaseModel):
    documents_added: Optional[str] = Field(default=None, alias="DocumentsAdded")
    documents_modified: Optional[str] = Field(default=None, alias="DocumentsModified")
    documents_deleted: Optional[str] = Field(default=None, alias="DocumentsDeleted")
    documents_failed: Optional[str] = Field(default=None, alias="DocumentsFailed")
    documents_scanned: Optional[str] = Field(default=None, alias="DocumentsScanned")


class SqlConfigurationModel(BaseModel):
    query_identifiers_enclosing_option: Optional[
        Literal["DOUBLE_QUOTES", "NONE"]
    ] = Field(default=None, alias="QueryIdentifiersEnclosingOption")


class DeleteAccessControlConfigurationRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")


class DeleteDataSourceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DeleteExperienceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DeleteFaqRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DeleteIndexRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeletePrincipalMappingRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    group_id: str = Field(alias="GroupId")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    ordering_id: Optional[int] = Field(default=None, alias="OrderingId")


class DeleteQuerySuggestionsBlockListRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")


class DeleteThesaurusRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DescribeAccessControlConfigurationRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")


class DescribeDataSourceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DescribeExperienceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class ExperienceEndpointModel(BaseModel):
    endpoint_type: Optional[Literal["HOME"]] = Field(default=None, alias="EndpointType")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")


class DescribeFaqRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DescribeIndexRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DescribePrincipalMappingRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    group_id: str = Field(alias="GroupId")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")


class GroupOrderingIdSummaryModel(BaseModel):
    status: Optional[
        Literal["DELETED", "DELETING", "FAILED", "PROCESSING", "SUCCEEDED"]
    ] = Field(default=None, alias="Status")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    received_at: Optional[datetime] = Field(default=None, alias="ReceivedAt")
    ordering_id: Optional[int] = Field(default=None, alias="OrderingId")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class DescribeQuerySuggestionsBlockListRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")


class DescribeQuerySuggestionsConfigRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")


class DescribeThesaurusRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class DisassociatePersonasFromEntitiesRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    entity_ids: Sequence[str] = Field(alias="EntityIds")


class DocumentAttributeValueModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    string_list_value: Optional[Sequence[str]] = Field(
        default=None, alias="StringListValue"
    )
    long_value: Optional[int] = Field(default=None, alias="LongValue")
    date_value: Optional[Union[datetime, str]] = Field(default=None, alias="DateValue")


class RelevanceModel(BaseModel):
    freshness: Optional[bool] = Field(default=None, alias="Freshness")
    importance: Optional[int] = Field(default=None, alias="Importance")
    duration: Optional[str] = Field(default=None, alias="Duration")
    rank_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="RankOrder"
    )
    value_importance_map: Optional[Dict[str, int]] = Field(
        default=None, alias="ValueImportanceMap"
    )


class SearchModel(BaseModel):
    facetable: Optional[bool] = Field(default=None, alias="Facetable")
    searchable: Optional[bool] = Field(default=None, alias="Searchable")
    displayable: Optional[bool] = Field(default=None, alias="Displayable")
    sortable: Optional[bool] = Field(default=None, alias="Sortable")


class DocumentsMetadataConfigurationModel(BaseModel):
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")


class EntityDisplayDataModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    identified_user_name: Optional[str] = Field(
        default=None, alias="IdentifiedUserName"
    )
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")


class UserIdentityConfigurationModel(BaseModel):
    identity_attribute_name: Optional[str] = Field(
        default=None, alias="IdentityAttributeName"
    )


class FacetResultModel(BaseModel):
    document_attribute_key: Optional[str] = Field(
        default=None, alias="DocumentAttributeKey"
    )
    document_attribute_value_type: Optional[
        Literal["DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"]
    ] = Field(default=None, alias="DocumentAttributeValueType")
    document_attribute_value_count_pairs: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="DocumentAttributeValueCountPairs"
    )


class FacetModel(BaseModel):
    document_attribute_key: Optional[str] = Field(
        default=None, alias="DocumentAttributeKey"
    )
    facets: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="Facets")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class FaqStatisticsModel(BaseModel):
    indexed_question_answers_count: int = Field(alias="IndexedQuestionAnswersCount")


class FaqSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    file_format: Optional[Literal["CSV", "CSV_WITH_HEADER", "JSON"]] = Field(
        default=None, alias="FileFormat"
    )
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")


class GetQuerySuggestionsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    query_text: str = Field(alias="QueryText")
    max_suggestions_count: Optional[int] = Field(
        default=None, alias="MaxSuggestionsCount"
    )


class GetSnapshotsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    interval: Literal[
        "ONE_MONTH_AGO",
        "ONE_WEEK_AGO",
        "THIS_MONTH",
        "THIS_WEEK",
        "TWO_MONTHS_AGO",
        "TWO_WEEKS_AGO",
    ] = Field(alias="Interval")
    metric_type: Literal[
        "AGG_QUERY_DOC_METRICS",
        "DOCS_BY_CLICK_COUNT",
        "QUERIES_BY_COUNT",
        "QUERIES_BY_ZERO_CLICK_RATE",
        "QUERIES_BY_ZERO_RESULT_RATE",
        "TREND_QUERY_DOC_METRICS",
    ] = Field(alias="MetricType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TimeRangeModel(BaseModel):
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class GitHubDocumentCrawlPropertiesModel(BaseModel):
    crawl_repository_documents: Optional[bool] = Field(
        default=None, alias="CrawlRepositoryDocuments"
    )
    crawl_issue: Optional[bool] = Field(default=None, alias="CrawlIssue")
    crawl_issue_comment: Optional[bool] = Field(default=None, alias="CrawlIssueComment")
    crawl_issue_comment_attachment: Optional[bool] = Field(
        default=None, alias="CrawlIssueCommentAttachment"
    )
    crawl_pull_request: Optional[bool] = Field(default=None, alias="CrawlPullRequest")
    crawl_pull_request_comment: Optional[bool] = Field(
        default=None, alias="CrawlPullRequestComment"
    )
    crawl_pull_request_comment_attachment: Optional[bool] = Field(
        default=None, alias="CrawlPullRequestCommentAttachment"
    )


class SaaSConfigurationModel(BaseModel):
    organization_name: str = Field(alias="OrganizationName")
    host_url: str = Field(alias="HostUrl")


class MemberGroupModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")


class MemberUserModel(BaseModel):
    user_id: str = Field(alias="UserId")


class GroupSummaryModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    ordering_id: Optional[int] = Field(default=None, alias="OrderingId")


class HighlightModel(BaseModel):
    begin_offset: int = Field(alias="BeginOffset")
    end_offset: int = Field(alias="EndOffset")
    top_answer: Optional[bool] = Field(default=None, alias="TopAnswer")
    type: Optional[Literal["STANDARD", "THESAURUS_SYNONYM"]] = Field(
        default=None, alias="Type"
    )


class IndexConfigurationSummaryModel(BaseModel):
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    status: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"
    ] = Field(alias="Status")
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    edition: Optional[Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]] = Field(
        default=None, alias="Edition"
    )


class TextDocumentStatisticsModel(BaseModel):
    indexed_text_documents_count: int = Field(alias="IndexedTextDocumentsCount")
    indexed_text_bytes: int = Field(alias="IndexedTextBytes")


class JsonTokenTypeConfigurationModel(BaseModel):
    user_name_attribute_field: str = Field(alias="UserNameAttributeField")
    group_attribute_field: str = Field(alias="GroupAttributeField")


class JwtTokenTypeConfigurationModel(BaseModel):
    key_location: Literal["SECRET_MANAGER", "URL"] = Field(alias="KeyLocation")
    url: Optional[str] = Field(default=None, alias="URL")
    secret_manager_arn: Optional[str] = Field(default=None, alias="SecretManagerArn")
    user_name_attribute_field: Optional[str] = Field(
        default=None, alias="UserNameAttributeField"
    )
    group_attribute_field: Optional[str] = Field(
        default=None, alias="GroupAttributeField"
    )
    issuer: Optional[str] = Field(default=None, alias="Issuer")
    claim_regex: Optional[str] = Field(default=None, alias="ClaimRegex")


class ListAccessControlConfigurationsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataSourcesRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEntityPersonasRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PersonasSummaryModel(BaseModel):
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    persona: Optional[Literal["OWNER", "VIEWER"]] = Field(default=None, alias="Persona")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class ListExperienceEntitiesRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExperiencesRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFaqsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGroupsOlderThanOrderingIdRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    ordering_id: int = Field(alias="OrderingId")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIndicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListQuerySuggestionsBlockListsRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class QuerySuggestionsBlockListSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "ACTIVE",
            "ACTIVE_BUT_UPDATE_FAILED",
            "CREATING",
            "DELETING",
            "FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class ListThesauriRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ThesaurusSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "ACTIVE",
            "ACTIVE_BUT_UPDATE_FAILED",
            "CREATING",
            "DELETING",
            "FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class SortingConfigurationModel(BaseModel):
    document_attribute_key: str = Field(alias="DocumentAttributeKey")
    sort_order: Literal["ASC", "DESC"] = Field(alias="SortOrder")


class SpellCorrectionConfigurationModel(BaseModel):
    include_query_spell_check_suggestions: bool = Field(
        alias="IncludeQuerySpellCheckSuggestions"
    )


class ScoreAttributesModel(BaseModel):
    score_confidence: Optional[
        Literal["HIGH", "LOW", "MEDIUM", "NOT_AVAILABLE", "VERY_HIGH"]
    ] = Field(default=None, alias="ScoreConfidence")


class WarningModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    code: Optional[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]] = Field(
        default=None, alias="Code"
    )


class RelevanceFeedbackModel(BaseModel):
    result_id: str = Field(alias="ResultId")
    relevance_value: Literal["NOT_RELEVANT", "RELEVANT"] = Field(alias="RelevanceValue")


class SeedUrlConfigurationModel(BaseModel):
    seed_urls: Sequence[str] = Field(alias="SeedUrls")
    web_crawler_mode: Optional[
        Literal["EVERYTHING", "HOST_ONLY", "SUBDOMAINS"]
    ] = Field(default=None, alias="WebCrawlerMode")


class SiteMapsConfigurationModel(BaseModel):
    site_maps: Sequence[str] = Field(alias="SiteMaps")


class StartDataSourceSyncJobRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class StopDataSourceSyncJobRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")


class SuggestionHighlightModel(BaseModel):
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")


class TableCellModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    top_answer: Optional[bool] = Field(default=None, alias="TopAnswer")
    highlighted: Optional[bool] = Field(default=None, alias="Highlighted")
    header: Optional[bool] = Field(default=None, alias="Header")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateQuerySuggestionsConfigRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    mode: Optional[Literal["ENABLED", "LEARN_ONLY"]] = Field(default=None, alias="Mode")
    query_log_look_back_window_in_days: Optional[int] = Field(
        default=None, alias="QueryLogLookBackWindowInDays"
    )
    include_queries_without_user_information: Optional[bool] = Field(
        default=None, alias="IncludeQueriesWithoutUserInformation"
    )
    minimum_number_of_querying_users: Optional[int] = Field(
        default=None, alias="MinimumNumberOfQueryingUsers"
    )
    minimum_query_count: Optional[int] = Field(default=None, alias="MinimumQueryCount")


class ColumnConfigurationModel(BaseModel):
    document_id_column_name: str = Field(alias="DocumentIdColumnName")
    document_data_column_name: str = Field(alias="DocumentDataColumnName")
    change_detecting_columns: Sequence[str] = Field(alias="ChangeDetectingColumns")
    document_title_column_name: Optional[str] = Field(
        default=None, alias="DocumentTitleColumnName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class GoogleDriveConfigurationModel(BaseModel):
    secret_arn: str = Field(alias="SecretArn")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )
    exclude_mime_types: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeMimeTypes"
    )
    exclude_user_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeUserAccounts"
    )
    exclude_shared_drives: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeSharedDrives"
    )


class SalesforceChatterFeedConfigurationModel(BaseModel):
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )
    include_filter_types: Optional[
        Sequence[Literal["ACTIVE_USER", "STANDARD_USER"]]
    ] = Field(default=None, alias="IncludeFilterTypes")


class SalesforceCustomKnowledgeArticleTypeConfigurationModel(BaseModel):
    name: str = Field(alias="Name")
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class SalesforceStandardKnowledgeArticleTypeConfigurationModel(BaseModel):
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class SalesforceStandardObjectAttachmentConfigurationModel(BaseModel):
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class SalesforceStandardObjectConfigurationModel(BaseModel):
    name: Literal[
        "ACCOUNT",
        "CAMPAIGN",
        "CASE",
        "CONTACT",
        "CONTRACT",
        "DOCUMENT",
        "GROUP",
        "IDEA",
        "LEAD",
        "OPPORTUNITY",
        "PARTNER",
        "PRICEBOOK",
        "PRODUCT",
        "PROFILE",
        "SOLUTION",
        "TASK",
        "USER",
    ] = Field(alias="Name")
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class ServiceNowKnowledgeArticleConfigurationModel(BaseModel):
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    include_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="IncludeAttachmentFilePatterns"
    )
    exclude_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeAttachmentFilePatterns"
    )
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )
    filter_query: Optional[str] = Field(default=None, alias="FilterQuery")


class ServiceNowServiceCatalogConfigurationModel(BaseModel):
    document_data_field_name: str = Field(alias="DocumentDataFieldName")
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    include_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="IncludeAttachmentFilePatterns"
    )
    exclude_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeAttachmentFilePatterns"
    )
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class WorkDocsConfigurationModel(BaseModel):
    organization_id: str = Field(alias="OrganizationId")
    crawl_comments: Optional[bool] = Field(default=None, alias="CrawlComments")
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class BoxConfigurationModel(BaseModel):
    enterprise_id: str = Field(alias="EnterpriseId")
    secret_arn: str = Field(alias="SecretArn")
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    crawl_comments: Optional[bool] = Field(default=None, alias="CrawlComments")
    crawl_tasks: Optional[bool] = Field(default=None, alias="CrawlTasks")
    crawl_web_links: Optional[bool] = Field(default=None, alias="CrawlWebLinks")
    file_field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FileFieldMappings"
    )
    task_field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="TaskFieldMappings"
    )
    comment_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="CommentFieldMappings")
    web_link_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="WebLinkFieldMappings")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class FsxConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="FileSystemId")
    file_system_type: Literal["WINDOWS"] = Field(alias="FileSystemType")
    vpc_configuration: DataSourceVpcConfigurationModel = Field(alias="VpcConfiguration")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class JiraConfigurationModel(BaseModel):
    jira_account_url: str = Field(alias="JiraAccountUrl")
    secret_arn: str = Field(alias="SecretArn")
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    project: Optional[Sequence[str]] = Field(default=None, alias="Project")
    issue_type: Optional[Sequence[str]] = Field(default=None, alias="IssueType")
    status: Optional[Sequence[str]] = Field(default=None, alias="Status")
    issue_sub_entity_filter: Optional[
        Sequence[Literal["ATTACHMENTS", "COMMENTS", "WORKLOGS"]]
    ] = Field(default=None, alias="IssueSubEntityFilter")
    attachment_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="AttachmentFieldMappings")
    comment_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="CommentFieldMappings")
    issue_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="IssueFieldMappings")
    project_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="ProjectFieldMappings")
    work_log_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="WorkLogFieldMappings")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class QuipConfigurationModel(BaseModel):
    domain: str = Field(alias="Domain")
    secret_arn: str = Field(alias="SecretArn")
    crawl_file_comments: Optional[bool] = Field(default=None, alias="CrawlFileComments")
    crawl_chat_rooms: Optional[bool] = Field(default=None, alias="CrawlChatRooms")
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    folder_ids: Optional[Sequence[str]] = Field(default=None, alias="FolderIds")
    thread_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="ThreadFieldMappings")
    message_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="MessageFieldMappings")
    attachment_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="AttachmentFieldMappings")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class SlackConfigurationModel(BaseModel):
    team_id: str = Field(alias="TeamId")
    secret_arn: str = Field(alias="SecretArn")
    slack_entity_list: Sequence[
        Literal["DIRECT_MESSAGE", "GROUP_MESSAGE", "PRIVATE_CHANNEL", "PUBLIC_CHANNEL"]
    ] = Field(alias="SlackEntityList")
    since_crawl_date: str = Field(alias="SinceCrawlDate")
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    crawl_bot_message: Optional[bool] = Field(default=None, alias="CrawlBotMessage")
    exclude_archived: Optional[bool] = Field(default=None, alias="ExcludeArchived")
    look_back_period: Optional[int] = Field(default=None, alias="LookBackPeriod")
    private_channel_filter: Optional[Sequence[str]] = Field(
        default=None, alias="PrivateChannelFilter"
    )
    public_channel_filter: Optional[Sequence[str]] = Field(
        default=None, alias="PublicChannelFilter"
    )
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )


class AlfrescoConfigurationModel(BaseModel):
    site_url: str = Field(alias="SiteUrl")
    site_id: str = Field(alias="SiteId")
    secret_arn: str = Field(alias="SecretArn")
    ssl_certificate_s3_path: S3PathModel = Field(alias="SslCertificateS3Path")
    crawl_system_folders: Optional[bool] = Field(
        default=None, alias="CrawlSystemFolders"
    )
    crawl_comments: Optional[bool] = Field(default=None, alias="CrawlComments")
    entity_filter: Optional[
        Sequence[Literal["blog", "documentLibrary", "wiki"]]
    ] = Field(default=None, alias="EntityFilter")
    document_library_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="DocumentLibraryFieldMappings")
    blog_field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="BlogFieldMappings"
    )
    wiki_field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="WikiFieldMappings"
    )
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class OnPremiseConfigurationModel(BaseModel):
    host_url: str = Field(alias="HostUrl")
    organization_name: str = Field(alias="OrganizationName")
    ssl_certificate_s3_path: S3PathModel = Field(alias="SslCertificateS3Path")


class OneDriveUsersModel(BaseModel):
    one_drive_user_list: Optional[Sequence[str]] = Field(
        default=None, alias="OneDriveUserList"
    )
    one_drive_user_s3_path: Optional[S3PathModel] = Field(
        default=None, alias="OneDriveUserS3Path"
    )


class UpdateQuerySuggestionsBlockListRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    source_s3_path: Optional[S3PathModel] = Field(default=None, alias="SourceS3Path")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class UpdateThesaurusRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    source_s3_path: Optional[S3PathModel] = Field(default=None, alias="SourceS3Path")


class AssociateEntitiesToExperienceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    entity_list: Sequence[EntityConfigurationModel] = Field(alias="EntityList")


class DisassociateEntitiesFromExperienceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    entity_list: Sequence[EntityConfigurationModel] = Field(alias="EntityList")


class AssociateEntitiesToExperienceResponseModel(BaseModel):
    failed_entity_list: List[FailedEntityModel] = Field(alias="FailedEntityList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociatePersonasToEntitiesResponseModel(BaseModel):
    failed_entity_list: List[FailedEntityModel] = Field(alias="FailedEntityList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessControlConfigurationResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperienceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFaqResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIndexResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQuerySuggestionsBlockListResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThesaurusResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFaqResponseModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    s3_path: S3PathModel = Field(alias="S3Path")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    role_arn: str = Field(alias="RoleArn")
    error_message: str = Field(alias="ErrorMessage")
    file_format: Literal["CSV", "CSV_WITH_HEADER", "JSON"] = Field(alias="FileFormat")
    language_code: str = Field(alias="LanguageCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeQuerySuggestionsBlockListResponseModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    status: Literal[
        "ACTIVE",
        "ACTIVE_BUT_UPDATE_FAILED",
        "CREATING",
        "DELETING",
        "FAILED",
        "UPDATING",
    ] = Field(alias="Status")
    error_message: str = Field(alias="ErrorMessage")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    source_s3_path: S3PathModel = Field(alias="SourceS3Path")
    item_count: int = Field(alias="ItemCount")
    file_size_bytes: int = Field(alias="FileSizeBytes")
    role_arn: str = Field(alias="RoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeQuerySuggestionsConfigResponseModel(BaseModel):
    mode: Literal["ENABLED", "LEARN_ONLY"] = Field(alias="Mode")
    status: Literal["ACTIVE", "UPDATING"] = Field(alias="Status")
    query_log_look_back_window_in_days: int = Field(
        alias="QueryLogLookBackWindowInDays"
    )
    include_queries_without_user_information: bool = Field(
        alias="IncludeQueriesWithoutUserInformation"
    )
    minimum_number_of_querying_users: int = Field(alias="MinimumNumberOfQueryingUsers")
    minimum_query_count: int = Field(alias="MinimumQueryCount")
    last_suggestions_build_time: datetime = Field(alias="LastSuggestionsBuildTime")
    last_clear_time: datetime = Field(alias="LastClearTime")
    total_suggestions_count: int = Field(alias="TotalSuggestionsCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThesaurusResponseModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    status: Literal[
        "ACTIVE",
        "ACTIVE_BUT_UPDATE_FAILED",
        "CREATING",
        "DELETING",
        "FAILED",
        "UPDATING",
    ] = Field(alias="Status")
    error_message: str = Field(alias="ErrorMessage")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    role_arn: str = Field(alias="RoleArn")
    source_s3_path: S3PathModel = Field(alias="SourceS3Path")
    file_size_bytes: int = Field(alias="FileSizeBytes")
    term_count: int = Field(alias="TermCount")
    synonym_rule_count: int = Field(alias="SynonymRuleCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateEntitiesFromExperienceResponseModel(BaseModel):
    failed_entity_list: List[FailedEntityModel] = Field(alias="FailedEntityList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePersonasFromEntitiesResponseModel(BaseModel):
    failed_entity_list: List[FailedEntityModel] = Field(alias="FailedEntityList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessControlConfigurationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    access_control_configurations: List[AccessControlConfigurationSummaryModel] = Field(
        alias="AccessControlConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataSourceSyncJobResponseModel(BaseModel):
    execution_id: str = Field(alias="ExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociatePersonasToEntitiesRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    personas: Sequence[EntityPersonaConfigurationModel] = Field(alias="Personas")


class AuthenticationConfigurationModel(BaseModel):
    basic_authentication: Optional[
        Sequence[BasicAuthenticationConfigurationModel]
    ] = Field(default=None, alias="BasicAuthentication")


class BatchDeleteDocumentRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    document_id_list: Sequence[str] = Field(alias="DocumentIdList")
    data_source_sync_job_metric_target: Optional[
        DataSourceSyncJobMetricTargetModel
    ] = Field(default=None, alias="DataSourceSyncJobMetricTarget")


class BatchDeleteDocumentResponseModel(BaseModel):
    failed_documents: List[BatchDeleteDocumentResponseFailedDocumentModel] = Field(
        alias="FailedDocuments"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetDocumentStatusResponseModel(BaseModel):
    errors: List[BatchGetDocumentStatusResponseErrorModel] = Field(alias="Errors")
    document_status_list: List[StatusModel] = Field(alias="DocumentStatusList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchPutDocumentResponseModel(BaseModel):
    failed_documents: List[BatchPutDocumentResponseFailedDocumentModel] = Field(
        alias="FailedDocuments"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfluenceAttachmentConfigurationModel(BaseModel):
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    attachment_field_mappings: Optional[
        Sequence[ConfluenceAttachmentToIndexFieldMappingModel]
    ] = Field(default=None, alias="AttachmentFieldMappings")


class ConfluenceBlogConfigurationModel(BaseModel):
    blog_field_mappings: Optional[
        Sequence[ConfluenceBlogToIndexFieldMappingModel]
    ] = Field(default=None, alias="BlogFieldMappings")


class SharePointConfigurationModel(BaseModel):
    share_point_version: Literal[
        "SHAREPOINT_2013", "SHAREPOINT_2016", "SHAREPOINT_2019", "SHAREPOINT_ONLINE"
    ] = Field(alias="SharePointVersion")
    urls: Sequence[str] = Field(alias="Urls")
    secret_arn: str = Field(alias="SecretArn")
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )
    document_title_field_name: Optional[str] = Field(
        default=None, alias="DocumentTitleFieldName"
    )
    disable_local_groups: Optional[bool] = Field(
        default=None, alias="DisableLocalGroups"
    )
    ssl_certificate_s3_path: Optional[S3PathModel] = Field(
        default=None, alias="SslCertificateS3Path"
    )
    authentication_type: Optional[Literal["HTTP_BASIC", "OAUTH2"]] = Field(
        default=None, alias="AuthenticationType"
    )
    proxy_configuration: Optional[ProxyConfigurationModel] = Field(
        default=None, alias="ProxyConfiguration"
    )


class ConfluencePageConfigurationModel(BaseModel):
    page_field_mappings: Optional[
        Sequence[ConfluencePageToIndexFieldMappingModel]
    ] = Field(default=None, alias="PageFieldMappings")


class ConfluenceSpaceConfigurationModel(BaseModel):
    crawl_personal_spaces: Optional[bool] = Field(
        default=None, alias="CrawlPersonalSpaces"
    )
    crawl_archived_spaces: Optional[bool] = Field(
        default=None, alias="CrawlArchivedSpaces"
    )
    include_spaces: Optional[Sequence[str]] = Field(default=None, alias="IncludeSpaces")
    exclude_spaces: Optional[Sequence[str]] = Field(default=None, alias="ExcludeSpaces")
    space_field_mappings: Optional[
        Sequence[ConfluenceSpaceToIndexFieldMappingModel]
    ] = Field(default=None, alias="SpaceFieldMappings")


class SpellCorrectedQueryModel(BaseModel):
    suggested_query_text: Optional[str] = Field(
        default=None, alias="SuggestedQueryText"
    )
    corrections: Optional[List[CorrectionModel]] = Field(
        default=None, alias="Corrections"
    )


class HierarchicalPrincipalModel(BaseModel):
    principal_list: Sequence[PrincipalModel] = Field(alias="PrincipalList")


class CreateFaqRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    s3_path: S3PathModel = Field(alias="S3Path")
    role_arn: str = Field(alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    file_format: Optional[Literal["CSV", "CSV_WITH_HEADER", "JSON"]] = Field(
        default=None, alias="FileFormat"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")


class CreateQuerySuggestionsBlockListRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    source_s3_path: S3PathModel = Field(alias="SourceS3Path")
    role_arn: str = Field(alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateThesaurusRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    source_s3_path: S3PathModel = Field(alias="SourceS3Path")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class UserContextModel(BaseModel):
    token: Optional[str] = Field(default=None, alias="Token")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")
    data_source_groups: Optional[Sequence[DataSourceGroupModel]] = Field(
        default=None, alias="DataSourceGroups"
    )


class ListDataSourcesResponseModel(BaseModel):
    summary_items: List[DataSourceSummaryModel] = Field(alias="SummaryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSourceSyncJobModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    status: Optional[
        Literal[
            "ABORTED",
            "FAILED",
            "INCOMPLETE",
            "STOPPING",
            "SUCCEEDED",
            "SYNCING",
            "SYNCING_INDEXING",
        ]
    ] = Field(default=None, alias="Status")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_code: Optional[Literal["InternalError", "InvalidRequest"]] = Field(
        default=None, alias="ErrorCode"
    )
    data_source_error_code: Optional[str] = Field(
        default=None, alias="DataSourceErrorCode"
    )
    metrics: Optional[DataSourceSyncJobMetricsModel] = Field(
        default=None, alias="Metrics"
    )


class ExperiencesSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    endpoints: Optional[List[ExperienceEndpointModel]] = Field(
        default=None, alias="Endpoints"
    )


class DescribePrincipalMappingResponseModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    data_source_id: str = Field(alias="DataSourceId")
    group_id: str = Field(alias="GroupId")
    group_ordering_id_summaries: List[GroupOrderingIdSummaryModel] = Field(
        alias="GroupOrderingIdSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentAttributeConditionModel(BaseModel):
    condition_document_attribute_key: str = Field(alias="ConditionDocumentAttributeKey")
    operator: Literal[
        "BeginsWith",
        "Contains",
        "Equals",
        "Exists",
        "GreaterThan",
        "GreaterThanOrEquals",
        "LessThan",
        "LessThanOrEquals",
        "NotContains",
        "NotEquals",
        "NotExists",
    ] = Field(alias="Operator")
    condition_on_value: Optional[DocumentAttributeValueModel] = Field(
        default=None, alias="ConditionOnValue"
    )


class DocumentAttributeTargetModel(BaseModel):
    target_document_attribute_key: Optional[str] = Field(
        default=None, alias="TargetDocumentAttributeKey"
    )
    target_document_attribute_value_deletion: Optional[bool] = Field(
        default=None, alias="TargetDocumentAttributeValueDeletion"
    )
    target_document_attribute_value: Optional[DocumentAttributeValueModel] = Field(
        default=None, alias="TargetDocumentAttributeValue"
    )


class DocumentAttributeModel(BaseModel):
    key: str = Field(alias="Key")
    value: DocumentAttributeValueModel = Field(alias="Value")


class DocumentAttributeValueCountPairModel(BaseModel):
    document_attribute_value: Optional[DocumentAttributeValueModel] = Field(
        default=None, alias="DocumentAttributeValue"
    )
    count: Optional[int] = Field(default=None, alias="Count")
    facet_results: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="FacetResults"
    )


class DocumentRelevanceConfigurationModel(BaseModel):
    name: str = Field(alias="Name")
    relevance: RelevanceModel = Field(alias="Relevance")


class DocumentMetadataConfigurationModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal[
        "DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"
    ] = Field(alias="Type")
    relevance: Optional[RelevanceModel] = Field(default=None, alias="Relevance")
    search: Optional[SearchModel] = Field(default=None, alias="Search")


class S3DataSourceConfigurationModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    inclusion_prefixes: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPrefixes"
    )
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    documents_metadata_configuration: Optional[
        DocumentsMetadataConfigurationModel
    ] = Field(default=None, alias="DocumentsMetadataConfiguration")
    access_control_list_configuration: Optional[
        AccessControlListConfigurationModel
    ] = Field(default=None, alias="AccessControlListConfiguration")


class ExperienceEntitiesSummaryModel(BaseModel):
    entity_id: Optional[str] = Field(default=None, alias="EntityId")
    entity_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="EntityType"
    )
    display_data: Optional[EntityDisplayDataModel] = Field(
        default=None, alias="DisplayData"
    )


class ExperienceConfigurationModel(BaseModel):
    content_source_configuration: Optional[ContentSourceConfigurationModel] = Field(
        default=None, alias="ContentSourceConfiguration"
    )
    user_identity_configuration: Optional[UserIdentityConfigurationModel] = Field(
        default=None, alias="UserIdentityConfiguration"
    )


class ListFaqsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    faq_summary_items: List[FaqSummaryModel] = Field(alias="FaqSummaryItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSnapshotsResponseModel(BaseModel):
    snap_shot_time_filter: TimeRangeModel = Field(alias="SnapShotTimeFilter")
    snapshots_data_header: List[str] = Field(alias="SnapshotsDataHeader")
    snapshots_data: List[List[str]] = Field(alias="SnapshotsData")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataSourceSyncJobsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    start_time_filter: Optional[TimeRangeModel] = Field(
        default=None, alias="StartTimeFilter"
    )
    status_filter: Optional[
        Literal[
            "ABORTED",
            "FAILED",
            "INCOMPLETE",
            "STOPPING",
            "SUCCEEDED",
            "SYNCING",
            "SYNCING_INDEXING",
        ]
    ] = Field(default=None, alias="StatusFilter")


class GroupMembersModel(BaseModel):
    member_groups: Optional[Sequence[MemberGroupModel]] = Field(
        default=None, alias="MemberGroups"
    )
    member_users: Optional[Sequence[MemberUserModel]] = Field(
        default=None, alias="MemberUsers"
    )
    s3_pathfor_group_members: Optional[S3PathModel] = Field(
        default=None, alias="S3PathforGroupMembers"
    )


class ListGroupsOlderThanOrderingIdResponseModel(BaseModel):
    groups_summaries: List[GroupSummaryModel] = Field(alias="GroupsSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TextWithHighlightsModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    highlights: Optional[List[HighlightModel]] = Field(default=None, alias="Highlights")


class ListIndicesResponseModel(BaseModel):
    index_configuration_summary_items: List[IndexConfigurationSummaryModel] = Field(
        alias="IndexConfigurationSummaryItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IndexStatisticsModel(BaseModel):
    faq_statistics: FaqStatisticsModel = Field(alias="FaqStatistics")
    text_document_statistics: TextDocumentStatisticsModel = Field(
        alias="TextDocumentStatistics"
    )


class UserTokenConfigurationModel(BaseModel):
    jwt_token_type_configuration: Optional[JwtTokenTypeConfigurationModel] = Field(
        default=None, alias="JwtTokenTypeConfiguration"
    )
    json_token_type_configuration: Optional[JsonTokenTypeConfigurationModel] = Field(
        default=None, alias="JsonTokenTypeConfiguration"
    )


class ListEntityPersonasResponseModel(BaseModel):
    summary_items: List[PersonasSummaryModel] = Field(alias="SummaryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQuerySuggestionsBlockListsResponseModel(BaseModel):
    block_list_summary_items: List[QuerySuggestionsBlockListSummaryModel] = Field(
        alias="BlockListSummaryItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThesauriResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    thesaurus_summary_items: List[ThesaurusSummaryModel] = Field(
        alias="ThesaurusSummaryItems"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitFeedbackRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    query_id: str = Field(alias="QueryId")
    click_feedback_items: Optional[Sequence[ClickFeedbackModel]] = Field(
        default=None, alias="ClickFeedbackItems"
    )
    relevance_feedback_items: Optional[Sequence[RelevanceFeedbackModel]] = Field(
        default=None, alias="RelevanceFeedbackItems"
    )


class UrlsModel(BaseModel):
    seed_url_configuration: Optional[SeedUrlConfigurationModel] = Field(
        default=None, alias="SeedUrlConfiguration"
    )
    site_maps_configuration: Optional[SiteMapsConfigurationModel] = Field(
        default=None, alias="SiteMapsConfiguration"
    )


class SuggestionTextWithHighlightsModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    highlights: Optional[List[SuggestionHighlightModel]] = Field(
        default=None, alias="Highlights"
    )


class TableRowModel(BaseModel):
    cells: Optional[List[TableCellModel]] = Field(default=None, alias="Cells")


class DatabaseConfigurationModel(BaseModel):
    database_engine_type: Literal[
        "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
    ] = Field(alias="DatabaseEngineType")
    connection_configuration: ConnectionConfigurationModel = Field(
        alias="ConnectionConfiguration"
    )
    column_configuration: ColumnConfigurationModel = Field(alias="ColumnConfiguration")
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    acl_configuration: Optional[AclConfigurationModel] = Field(
        default=None, alias="AclConfiguration"
    )
    sql_configuration: Optional[SqlConfigurationModel] = Field(
        default=None, alias="SqlConfiguration"
    )


class SalesforceKnowledgeArticleConfigurationModel(BaseModel):
    included_states: Sequence[Literal["ARCHIVED", "DRAFT", "PUBLISHED"]] = Field(
        alias="IncludedStates"
    )
    standard_knowledge_article_type_configuration: Optional[
        SalesforceStandardKnowledgeArticleTypeConfigurationModel
    ] = Field(default=None, alias="StandardKnowledgeArticleTypeConfiguration")
    custom_knowledge_article_type_configurations: Optional[
        Sequence[SalesforceCustomKnowledgeArticleTypeConfigurationModel]
    ] = Field(default=None, alias="CustomKnowledgeArticleTypeConfigurations")


class ServiceNowConfigurationModel(BaseModel):
    host_url: str = Field(alias="HostUrl")
    secret_arn: str = Field(alias="SecretArn")
    service_now_build_version: Literal["LONDON", "OTHERS"] = Field(
        alias="ServiceNowBuildVersion"
    )
    knowledge_article_configuration: Optional[
        ServiceNowKnowledgeArticleConfigurationModel
    ] = Field(default=None, alias="KnowledgeArticleConfiguration")
    service_catalog_configuration: Optional[
        ServiceNowServiceCatalogConfigurationModel
    ] = Field(default=None, alias="ServiceCatalogConfiguration")
    authentication_type: Optional[Literal["HTTP_BASIC", "OAUTH2"]] = Field(
        default=None, alias="AuthenticationType"
    )


class GitHubConfigurationModel(BaseModel):
    secret_arn: str = Field(alias="SecretArn")
    saa_s_configuration: Optional[SaaSConfigurationModel] = Field(
        default=None, alias="SaaSConfiguration"
    )
    on_premise_configuration: Optional[OnPremiseConfigurationModel] = Field(
        default=None, alias="OnPremiseConfiguration"
    )
    type: Optional[Literal["ON_PREMISE", "SAAS"]] = Field(default=None, alias="Type")
    use_change_log: Optional[bool] = Field(default=None, alias="UseChangeLog")
    git_hub_document_crawl_properties: Optional[
        GitHubDocumentCrawlPropertiesModel
    ] = Field(default=None, alias="GitHubDocumentCrawlProperties")
    repository_filter: Optional[Sequence[str]] = Field(
        default=None, alias="RepositoryFilter"
    )
    inclusion_folder_name_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionFolderNamePatterns"
    )
    inclusion_file_type_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionFileTypePatterns"
    )
    inclusion_file_name_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionFileNamePatterns"
    )
    exclusion_folder_name_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionFolderNamePatterns"
    )
    exclusion_file_type_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionFileTypePatterns"
    )
    exclusion_file_name_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionFileNamePatterns"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    git_hub_repository_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubRepositoryConfigurationFieldMappings")
    git_hub_commit_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubCommitConfigurationFieldMappings")
    git_hub_issue_document_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubIssueDocumentConfigurationFieldMappings")
    git_hub_issue_comment_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubIssueCommentConfigurationFieldMappings")
    git_hub_issue_attachment_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubIssueAttachmentConfigurationFieldMappings")
    git_hub_pull_request_comment_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubPullRequestCommentConfigurationFieldMappings")
    git_hub_pull_request_document_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(default=None, alias="GitHubPullRequestDocumentConfigurationFieldMappings")
    git_hub_pull_request_document_attachment_configuration_field_mappings: Optional[
        Sequence[DataSourceToIndexFieldMappingModel]
    ] = Field(
        default=None,
        alias="GitHubPullRequestDocumentAttachmentConfigurationFieldMappings",
    )


class OneDriveConfigurationModel(BaseModel):
    tenant_domain: str = Field(alias="TenantDomain")
    secret_arn: str = Field(alias="SecretArn")
    one_drive_users: OneDriveUsersModel = Field(alias="OneDriveUsers")
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    field_mappings: Optional[Sequence[DataSourceToIndexFieldMappingModel]] = Field(
        default=None, alias="FieldMappings"
    )
    disable_local_groups: Optional[bool] = Field(
        default=None, alias="DisableLocalGroups"
    )


class ConfluenceConfigurationModel(BaseModel):
    server_url: str = Field(alias="ServerUrl")
    secret_arn: str = Field(alias="SecretArn")
    version: Literal["CLOUD", "SERVER"] = Field(alias="Version")
    space_configuration: Optional[ConfluenceSpaceConfigurationModel] = Field(
        default=None, alias="SpaceConfiguration"
    )
    page_configuration: Optional[ConfluencePageConfigurationModel] = Field(
        default=None, alias="PageConfiguration"
    )
    blog_configuration: Optional[ConfluenceBlogConfigurationModel] = Field(
        default=None, alias="BlogConfiguration"
    )
    attachment_configuration: Optional[ConfluenceAttachmentConfigurationModel] = Field(
        default=None, alias="AttachmentConfiguration"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="InclusionPatterns"
    )
    exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExclusionPatterns"
    )
    proxy_configuration: Optional[ProxyConfigurationModel] = Field(
        default=None, alias="ProxyConfiguration"
    )
    authentication_type: Optional[Literal["HTTP_BASIC", "PAT"]] = Field(
        default=None, alias="AuthenticationType"
    )


class CreateAccessControlConfigurationRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    access_control_list: Optional[Sequence[PrincipalModel]] = Field(
        default=None, alias="AccessControlList"
    )
    hierarchical_access_control_list: Optional[
        Sequence[HierarchicalPrincipalModel]
    ] = Field(default=None, alias="HierarchicalAccessControlList")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribeAccessControlConfigurationResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    error_message: str = Field(alias="ErrorMessage")
    access_control_list: List[PrincipalModel] = Field(alias="AccessControlList")
    hierarchical_access_control_list: List[HierarchicalPrincipalModel] = Field(
        alias="HierarchicalAccessControlList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccessControlConfigurationRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    access_control_list: Optional[Sequence[PrincipalModel]] = Field(
        default=None, alias="AccessControlList"
    )
    hierarchical_access_control_list: Optional[
        Sequence[HierarchicalPrincipalModel]
    ] = Field(default=None, alias="HierarchicalAccessControlList")


class ListDataSourceSyncJobsResponseModel(BaseModel):
    history: List[DataSourceSyncJobModel] = Field(alias="History")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExperiencesResponseModel(BaseModel):
    summary_items: List[ExperiencesSummaryModel] = Field(alias="SummaryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HookConfigurationModel(BaseModel):
    lambda_arn: str = Field(alias="LambdaArn")
    s3_bucket: str = Field(alias="S3Bucket")
    invocation_condition: Optional[DocumentAttributeConditionModel] = Field(
        default=None, alias="InvocationCondition"
    )


class InlineCustomDocumentEnrichmentConfigurationModel(BaseModel):
    condition: Optional[DocumentAttributeConditionModel] = Field(
        default=None, alias="Condition"
    )
    target: Optional[DocumentAttributeTargetModel] = Field(default=None, alias="Target")
    document_content_deletion: Optional[bool] = Field(
        default=None, alias="DocumentContentDeletion"
    )


class AttributeFilterModel(BaseModel):
    and_all_filters: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="AndAllFilters"
    )
    or_all_filters: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="OrAllFilters"
    )
    not_filter: Optional[Dict[str, Any]] = Field(default=None, alias="NotFilter")
    equals_to: Optional[DocumentAttributeModel] = Field(default=None, alias="EqualsTo")
    contains_all: Optional[DocumentAttributeModel] = Field(
        default=None, alias="ContainsAll"
    )
    contains_any: Optional[DocumentAttributeModel] = Field(
        default=None, alias="ContainsAny"
    )
    greater_than: Optional[DocumentAttributeModel] = Field(
        default=None, alias="GreaterThan"
    )
    greater_than_or_equals: Optional[DocumentAttributeModel] = Field(
        default=None, alias="GreaterThanOrEquals"
    )
    less_than: Optional[DocumentAttributeModel] = Field(default=None, alias="LessThan")
    less_than_or_equals: Optional[DocumentAttributeModel] = Field(
        default=None, alias="LessThanOrEquals"
    )


class DocumentInfoModel(BaseModel):
    document_id: str = Field(alias="DocumentId")
    attributes: Optional[Sequence[DocumentAttributeModel]] = Field(
        default=None, alias="Attributes"
    )


class DocumentModel(BaseModel):
    id: str = Field(alias="Id")
    title: Optional[str] = Field(default=None, alias="Title")
    blob: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Blob"
    )
    s3_path: Optional[S3PathModel] = Field(default=None, alias="S3Path")
    attributes: Optional[Sequence[DocumentAttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    access_control_list: Optional[Sequence[PrincipalModel]] = Field(
        default=None, alias="AccessControlList"
    )
    hierarchical_access_control_list: Optional[
        Sequence[HierarchicalPrincipalModel]
    ] = Field(default=None, alias="HierarchicalAccessControlList")
    content_type: Optional[
        Literal[
            "CSV",
            "HTML",
            "JSON",
            "MD",
            "MS_EXCEL",
            "MS_WORD",
            "PDF",
            "PLAIN_TEXT",
            "PPT",
            "RTF",
            "XML",
            "XSLT",
        ]
    ] = Field(default=None, alias="ContentType")
    access_control_configuration_id: Optional[str] = Field(
        default=None, alias="AccessControlConfigurationId"
    )


class QueryRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    query_text: Optional[str] = Field(default=None, alias="QueryText")
    attribute_filter: Optional[AttributeFilterModel] = Field(
        default=None, alias="AttributeFilter"
    )
    facets: Optional[Sequence[FacetModel]] = Field(default=None, alias="Facets")
    requested_document_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="RequestedDocumentAttributes"
    )
    query_result_type_filter: Optional[
        Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]
    ] = Field(default=None, alias="QueryResultTypeFilter")
    document_relevance_override_configurations: Optional[
        Sequence[DocumentRelevanceConfigurationModel]
    ] = Field(default=None, alias="DocumentRelevanceOverrideConfigurations")
    page_number: Optional[int] = Field(default=None, alias="PageNumber")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    sorting_configuration: Optional[SortingConfigurationModel] = Field(
        default=None, alias="SortingConfiguration"
    )
    user_context: Optional[UserContextModel] = Field(default=None, alias="UserContext")
    visitor_id: Optional[str] = Field(default=None, alias="VisitorId")
    spell_correction_configuration: Optional[SpellCorrectionConfigurationModel] = Field(
        default=None, alias="SpellCorrectionConfiguration"
    )


class ListExperienceEntitiesResponseModel(BaseModel):
    summary_items: List[ExperienceEntitiesSummaryModel] = Field(alias="SummaryItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateExperienceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    index_id: str = Field(alias="IndexId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    configuration: Optional[ExperienceConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribeExperienceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    endpoints: List[ExperienceEndpointModel] = Field(alias="Endpoints")
    configuration: ExperienceConfigurationModel = Field(alias="Configuration")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    description: str = Field(alias="Description")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="Status")
    role_arn: str = Field(alias="RoleArn")
    error_message: str = Field(alias="ErrorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateExperienceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: Optional[str] = Field(default=None, alias="Name")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    configuration: Optional[ExperienceConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class PutPrincipalMappingRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    group_id: str = Field(alias="GroupId")
    group_members: GroupMembersModel = Field(alias="GroupMembers")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    ordering_id: Optional[int] = Field(default=None, alias="OrderingId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class AdditionalResultAttributeValueModel(BaseModel):
    text_with_highlights_value: Optional[TextWithHighlightsModel] = Field(
        default=None, alias="TextWithHighlightsValue"
    )


class CreateIndexRequestModel(BaseModel):
    name: str = Field(alias="Name")
    role_arn: str = Field(alias="RoleArn")
    edition: Optional[Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]] = Field(
        default=None, alias="Edition"
    )
    server_side_encryption_configuration: Optional[
        ServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="ServerSideEncryptionConfiguration")
    description: Optional[str] = Field(default=None, alias="Description")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    user_token_configurations: Optional[Sequence[UserTokenConfigurationModel]] = Field(
        default=None, alias="UserTokenConfigurations"
    )
    user_context_policy: Optional[Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]] = Field(
        default=None, alias="UserContextPolicy"
    )
    user_group_resolution_configuration: Optional[
        UserGroupResolutionConfigurationModel
    ] = Field(default=None, alias="UserGroupResolutionConfiguration")


class DescribeIndexResponseModel(BaseModel):
    name: str = Field(alias="Name")
    id: str = Field(alias="Id")
    edition: Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"] = Field(alias="Edition")
    role_arn: str = Field(alias="RoleArn")
    server_side_encryption_configuration: ServerSideEncryptionConfigurationModel = (
        Field(alias="ServerSideEncryptionConfiguration")
    )
    status: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"
    ] = Field(alias="Status")
    description: str = Field(alias="Description")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    document_metadata_configurations: List[DocumentMetadataConfigurationModel] = Field(
        alias="DocumentMetadataConfigurations"
    )
    index_statistics: IndexStatisticsModel = Field(alias="IndexStatistics")
    error_message: str = Field(alias="ErrorMessage")
    capacity_units: CapacityUnitsConfigurationModel = Field(alias="CapacityUnits")
    user_token_configurations: List[UserTokenConfigurationModel] = Field(
        alias="UserTokenConfigurations"
    )
    user_context_policy: Literal["ATTRIBUTE_FILTER", "USER_TOKEN"] = Field(
        alias="UserContextPolicy"
    )
    user_group_resolution_configuration: UserGroupResolutionConfigurationModel = Field(
        alias="UserGroupResolutionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIndexRequestModel(BaseModel):
    id: str = Field(alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    description: Optional[str] = Field(default=None, alias="Description")
    document_metadata_configuration_updates: Optional[
        Sequence[DocumentMetadataConfigurationModel]
    ] = Field(default=None, alias="DocumentMetadataConfigurationUpdates")
    capacity_units: Optional[CapacityUnitsConfigurationModel] = Field(
        default=None, alias="CapacityUnits"
    )
    user_token_configurations: Optional[Sequence[UserTokenConfigurationModel]] = Field(
        default=None, alias="UserTokenConfigurations"
    )
    user_context_policy: Optional[Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]] = Field(
        default=None, alias="UserContextPolicy"
    )
    user_group_resolution_configuration: Optional[
        UserGroupResolutionConfigurationModel
    ] = Field(default=None, alias="UserGroupResolutionConfiguration")


class WebCrawlerConfigurationModel(BaseModel):
    urls: UrlsModel = Field(alias="Urls")
    crawl_depth: Optional[int] = Field(default=None, alias="CrawlDepth")
    max_links_per_page: Optional[int] = Field(default=None, alias="MaxLinksPerPage")
    max_content_size_per_page_in_mega_bytes: Optional[float] = Field(
        default=None, alias="MaxContentSizePerPageInMegaBytes"
    )
    max_urls_per_minute_crawl_rate: Optional[int] = Field(
        default=None, alias="MaxUrlsPerMinuteCrawlRate"
    )
    url_inclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="UrlInclusionPatterns"
    )
    url_exclusion_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="UrlExclusionPatterns"
    )
    proxy_configuration: Optional[ProxyConfigurationModel] = Field(
        default=None, alias="ProxyConfiguration"
    )
    authentication_configuration: Optional[AuthenticationConfigurationModel] = Field(
        default=None, alias="AuthenticationConfiguration"
    )


class SuggestionValueModel(BaseModel):
    text: Optional[SuggestionTextWithHighlightsModel] = Field(
        default=None, alias="Text"
    )


class TableExcerptModel(BaseModel):
    rows: Optional[List[TableRowModel]] = Field(default=None, alias="Rows")
    total_number_of_rows: Optional[int] = Field(default=None, alias="TotalNumberOfRows")


class SalesforceConfigurationModel(BaseModel):
    server_url: str = Field(alias="ServerUrl")
    secret_arn: str = Field(alias="SecretArn")
    standard_object_configurations: Optional[
        Sequence[SalesforceStandardObjectConfigurationModel]
    ] = Field(default=None, alias="StandardObjectConfigurations")
    knowledge_article_configuration: Optional[
        SalesforceKnowledgeArticleConfigurationModel
    ] = Field(default=None, alias="KnowledgeArticleConfiguration")
    chatter_feed_configuration: Optional[
        SalesforceChatterFeedConfigurationModel
    ] = Field(default=None, alias="ChatterFeedConfiguration")
    crawl_attachments: Optional[bool] = Field(default=None, alias="CrawlAttachments")
    standard_object_attachment_configuration: Optional[
        SalesforceStandardObjectAttachmentConfigurationModel
    ] = Field(default=None, alias="StandardObjectAttachmentConfiguration")
    include_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="IncludeAttachmentFilePatterns"
    )
    exclude_attachment_file_patterns: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludeAttachmentFilePatterns"
    )


class CustomDocumentEnrichmentConfigurationModel(BaseModel):
    inline_configurations: Optional[
        Sequence[InlineCustomDocumentEnrichmentConfigurationModel]
    ] = Field(default=None, alias="InlineConfigurations")
    pre_extraction_hook_configuration: Optional[HookConfigurationModel] = Field(
        default=None, alias="PreExtractionHookConfiguration"
    )
    post_extraction_hook_configuration: Optional[HookConfigurationModel] = Field(
        default=None, alias="PostExtractionHookConfiguration"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class BatchGetDocumentStatusRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    document_info_list: Sequence[DocumentInfoModel] = Field(alias="DocumentInfoList")


class AdditionalResultAttributeModel(BaseModel):
    key: str = Field(alias="Key")
    value_type: Literal["TEXT_WITH_HIGHLIGHTS_VALUE"] = Field(alias="ValueType")
    value: AdditionalResultAttributeValueModel = Field(alias="Value")


class SuggestionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    value: Optional[SuggestionValueModel] = Field(default=None, alias="Value")


class DataSourceConfigurationModel(BaseModel):
    s3_configuration: Optional[S3DataSourceConfigurationModel] = Field(
        default=None, alias="S3Configuration"
    )
    share_point_configuration: Optional[SharePointConfigurationModel] = Field(
        default=None, alias="SharePointConfiguration"
    )
    database_configuration: Optional[DatabaseConfigurationModel] = Field(
        default=None, alias="DatabaseConfiguration"
    )
    salesforce_configuration: Optional[SalesforceConfigurationModel] = Field(
        default=None, alias="SalesforceConfiguration"
    )
    one_drive_configuration: Optional[OneDriveConfigurationModel] = Field(
        default=None, alias="OneDriveConfiguration"
    )
    service_now_configuration: Optional[ServiceNowConfigurationModel] = Field(
        default=None, alias="ServiceNowConfiguration"
    )
    confluence_configuration: Optional[ConfluenceConfigurationModel] = Field(
        default=None, alias="ConfluenceConfiguration"
    )
    google_drive_configuration: Optional[GoogleDriveConfigurationModel] = Field(
        default=None, alias="GoogleDriveConfiguration"
    )
    web_crawler_configuration: Optional[WebCrawlerConfigurationModel] = Field(
        default=None, alias="WebCrawlerConfiguration"
    )
    work_docs_configuration: Optional[WorkDocsConfigurationModel] = Field(
        default=None, alias="WorkDocsConfiguration"
    )
    fsx_configuration: Optional[FsxConfigurationModel] = Field(
        default=None, alias="FsxConfiguration"
    )
    slack_configuration: Optional[SlackConfigurationModel] = Field(
        default=None, alias="SlackConfiguration"
    )
    box_configuration: Optional[BoxConfigurationModel] = Field(
        default=None, alias="BoxConfiguration"
    )
    quip_configuration: Optional[QuipConfigurationModel] = Field(
        default=None, alias="QuipConfiguration"
    )
    jira_configuration: Optional[JiraConfigurationModel] = Field(
        default=None, alias="JiraConfiguration"
    )
    git_hub_configuration: Optional[GitHubConfigurationModel] = Field(
        default=None, alias="GitHubConfiguration"
    )
    alfresco_configuration: Optional[AlfrescoConfigurationModel] = Field(
        default=None, alias="AlfrescoConfiguration"
    )
    template_configuration: Optional[TemplateConfigurationModel] = Field(
        default=None, alias="TemplateConfiguration"
    )


class BatchPutDocumentRequestModel(BaseModel):
    index_id: str = Field(alias="IndexId")
    documents: Sequence[DocumentModel] = Field(alias="Documents")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    custom_document_enrichment_configuration: Optional[
        CustomDocumentEnrichmentConfigurationModel
    ] = Field(default=None, alias="CustomDocumentEnrichmentConfiguration")


class QueryResultItemModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]] = Field(
        default=None, alias="Type"
    )
    format: Optional[Literal["TABLE", "TEXT"]] = Field(default=None, alias="Format")
    additional_attributes: Optional[List[AdditionalResultAttributeModel]] = Field(
        default=None, alias="AdditionalAttributes"
    )
    document_id: Optional[str] = Field(default=None, alias="DocumentId")
    document_title: Optional[TextWithHighlightsModel] = Field(
        default=None, alias="DocumentTitle"
    )
    document_excerpt: Optional[TextWithHighlightsModel] = Field(
        default=None, alias="DocumentExcerpt"
    )
    document_uri: Optional[str] = Field(default=None, alias="DocumentURI")
    document_attributes: Optional[List[DocumentAttributeModel]] = Field(
        default=None, alias="DocumentAttributes"
    )
    score_attributes: Optional[ScoreAttributesModel] = Field(
        default=None, alias="ScoreAttributes"
    )
    feedback_token: Optional[str] = Field(default=None, alias="FeedbackToken")
    table_excerpt: Optional[TableExcerptModel] = Field(
        default=None, alias="TableExcerpt"
    )


class GetQuerySuggestionsResponseModel(BaseModel):
    query_suggestions_id: str = Field(alias="QuerySuggestionsId")
    suggestions: List[SuggestionModel] = Field(alias="Suggestions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    index_id: str = Field(alias="IndexId")
    type: Literal[
        "ALFRESCO",
        "BOX",
        "CONFLUENCE",
        "CUSTOM",
        "DATABASE",
        "FSX",
        "GITHUB",
        "GOOGLEDRIVE",
        "JIRA",
        "ONEDRIVE",
        "QUIP",
        "S3",
        "SALESFORCE",
        "SERVICENOW",
        "SHAREPOINT",
        "SLACK",
        "TEMPLATE",
        "WEBCRAWLER",
        "WORKDOCS",
    ] = Field(alias="Type")
    configuration: Optional[DataSourceConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    custom_document_enrichment_configuration: Optional[
        CustomDocumentEnrichmentConfigurationModel
    ] = Field(default=None, alias="CustomDocumentEnrichmentConfiguration")


class DescribeDataSourceResponseModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: str = Field(alias="Name")
    type: Literal[
        "ALFRESCO",
        "BOX",
        "CONFLUENCE",
        "CUSTOM",
        "DATABASE",
        "FSX",
        "GITHUB",
        "GOOGLEDRIVE",
        "JIRA",
        "ONEDRIVE",
        "QUIP",
        "S3",
        "SALESFORCE",
        "SERVICENOW",
        "SHAREPOINT",
        "SLACK",
        "TEMPLATE",
        "WEBCRAWLER",
        "WORKDOCS",
    ] = Field(alias="Type")
    configuration: DataSourceConfigurationModel = Field(alias="Configuration")
    vpc_configuration: DataSourceVpcConfigurationModel = Field(alias="VpcConfiguration")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    description: str = Field(alias="Description")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    schedule: str = Field(alias="Schedule")
    role_arn: str = Field(alias="RoleArn")
    error_message: str = Field(alias="ErrorMessage")
    language_code: str = Field(alias="LanguageCode")
    custom_document_enrichment_configuration: CustomDocumentEnrichmentConfigurationModel = Field(
        alias="CustomDocumentEnrichmentConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSourceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    index_id: str = Field(alias="IndexId")
    name: Optional[str] = Field(default=None, alias="Name")
    configuration: Optional[DataSourceConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    vpc_configuration: Optional[DataSourceVpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    schedule: Optional[str] = Field(default=None, alias="Schedule")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    custom_document_enrichment_configuration: Optional[
        CustomDocumentEnrichmentConfigurationModel
    ] = Field(default=None, alias="CustomDocumentEnrichmentConfiguration")


class QueryResultModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    result_items: List[QueryResultItemModel] = Field(alias="ResultItems")
    facet_results: List[FacetResultModel] = Field(alias="FacetResults")
    total_number_of_results: int = Field(alias="TotalNumberOfResults")
    warnings: List[WarningModel] = Field(alias="Warnings")
    spell_corrected_queries: List[SpellCorrectedQueryModel] = Field(
        alias="SpellCorrectedQueries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
