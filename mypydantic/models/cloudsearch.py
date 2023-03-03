# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class OptionStatusModel(BaseModel):
    creation_date: datetime = Field(alias="CreationDate")
    update_date: datetime = Field(alias="UpdateDate")
    state: Literal[
        "Active", "FailedToValidate", "Processing", "RequiresIndexDocuments"
    ] = Field(alias="State")
    update_version: Optional[int] = Field(default=None, alias="UpdateVersion")
    pending_deletion: Optional[bool] = Field(default=None, alias="PendingDeletion")


class AnalysisOptionsModel(BaseModel):
    synonyms: Optional[str] = Field(default=None, alias="Synonyms")
    stopwords: Optional[str] = Field(default=None, alias="Stopwords")
    stemming_dictionary: Optional[str] = Field(default=None, alias="StemmingDictionary")
    japanese_tokenization_dictionary: Optional[str] = Field(
        default=None, alias="JapaneseTokenizationDictionary"
    )
    algorithmic_stemming: Optional[Literal["full", "light", "minimal", "none"]] = Field(
        default=None, alias="AlgorithmicStemming"
    )


class BuildSuggestersRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DateArrayOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_fields: Optional[str] = Field(default=None, alias="SourceFields")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")


class DateOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")


class ExpressionModel(BaseModel):
    expression_name: str = Field(alias="ExpressionName")
    expression_value: str = Field(alias="ExpressionValue")


class DeleteAnalysisSchemeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    analysis_scheme_name: str = Field(alias="AnalysisSchemeName")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteExpressionRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    expression_name: str = Field(alias="ExpressionName")


class DeleteIndexFieldRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    index_field_name: str = Field(alias="IndexFieldName")


class DeleteSuggesterRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    suggester_name: str = Field(alias="SuggesterName")


class DescribeAnalysisSchemesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    analysis_scheme_names: Optional[Sequence[str]] = Field(
        default=None, alias="AnalysisSchemeNames"
    )
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeAvailabilityOptionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeDomainEndpointOptionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeDomainsRequestModel(BaseModel):
    domain_names: Optional[Sequence[str]] = Field(default=None, alias="DomainNames")


class DescribeExpressionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    expression_names: Optional[Sequence[str]] = Field(
        default=None, alias="ExpressionNames"
    )
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeIndexFieldsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    field_names: Optional[Sequence[str]] = Field(default=None, alias="FieldNames")
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeScalingParametersRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DescribeServiceAccessPoliciesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DescribeSuggestersRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    suggester_names: Optional[Sequence[str]] = Field(
        default=None, alias="SuggesterNames"
    )
    deployed: Optional[bool] = Field(default=None, alias="Deployed")


class DocumentSuggesterOptionsModel(BaseModel):
    source_field: str = Field(alias="SourceField")
    fuzzy_matching: Optional[Literal["high", "low", "none"]] = Field(
        default=None, alias="FuzzyMatching"
    )
    sort_expression: Optional[str] = Field(default=None, alias="SortExpression")


class DomainEndpointOptionsModel(BaseModel):
    enforce_http_s: Optional[bool] = Field(default=None, alias="EnforceHTTPS")
    tl_s_security_policy: Optional[
        Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
    ] = Field(default=None, alias="TLSSecurityPolicy")


class LimitsModel(BaseModel):
    maximum_replication_count: int = Field(alias="MaximumReplicationCount")
    maximum_partition_count: int = Field(alias="MaximumPartitionCount")


class ServiceEndpointModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")


class DoubleArrayOptionsModel(BaseModel):
    default_value: Optional[float] = Field(default=None, alias="DefaultValue")
    source_fields: Optional[str] = Field(default=None, alias="SourceFields")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")


class DoubleOptionsModel(BaseModel):
    default_value: Optional[float] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")


class IndexDocumentsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class IntArrayOptionsModel(BaseModel):
    default_value: Optional[int] = Field(default=None, alias="DefaultValue")
    source_fields: Optional[str] = Field(default=None, alias="SourceFields")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")


class IntOptionsModel(BaseModel):
    default_value: Optional[int] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")


class LatLonOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")


class LiteralArrayOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_fields: Optional[str] = Field(default=None, alias="SourceFields")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")


class LiteralOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    facet_enabled: Optional[bool] = Field(default=None, alias="FacetEnabled")
    search_enabled: Optional[bool] = Field(default=None, alias="SearchEnabled")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")


class TextArrayOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_fields: Optional[str] = Field(default=None, alias="SourceFields")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    highlight_enabled: Optional[bool] = Field(default=None, alias="HighlightEnabled")
    analysis_scheme: Optional[str] = Field(default=None, alias="AnalysisScheme")


class TextOptionsModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    source_field: Optional[str] = Field(default=None, alias="SourceField")
    return_enabled: Optional[bool] = Field(default=None, alias="ReturnEnabled")
    sort_enabled: Optional[bool] = Field(default=None, alias="SortEnabled")
    highlight_enabled: Optional[bool] = Field(default=None, alias="HighlightEnabled")
    analysis_scheme: Optional[str] = Field(default=None, alias="AnalysisScheme")


class ScalingParametersModel(BaseModel):
    desired_instance_type: Optional[
        Literal[
            "search.2xlarge",
            "search.large",
            "search.m1.large",
            "search.m1.small",
            "search.m2.2xlarge",
            "search.m2.xlarge",
            "search.m3.2xlarge",
            "search.m3.large",
            "search.m3.medium",
            "search.m3.xlarge",
            "search.medium",
            "search.previousgeneration.2xlarge",
            "search.previousgeneration.large",
            "search.previousgeneration.small",
            "search.previousgeneration.xlarge",
            "search.small",
            "search.xlarge",
        ]
    ] = Field(default=None, alias="DesiredInstanceType")
    desired_replication_count: Optional[int] = Field(
        default=None, alias="DesiredReplicationCount"
    )
    desired_partition_count: Optional[int] = Field(
        default=None, alias="DesiredPartitionCount"
    )


class UpdateAvailabilityOptionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    multi_az: bool = Field(alias="MultiAZ")


class UpdateServiceAccessPoliciesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    access_policies: str = Field(alias="AccessPolicies")


class AccessPoliciesStatusModel(BaseModel):
    options: str = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AvailabilityOptionsStatusModel(BaseModel):
    options: bool = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AnalysisSchemeModel(BaseModel):
    analysis_scheme_name: str = Field(alias="AnalysisSchemeName")
    analysis_scheme_language: Literal[
        "ar",
        "bg",
        "ca",
        "cs",
        "da",
        "de",
        "el",
        "en",
        "es",
        "eu",
        "fa",
        "fi",
        "fr",
        "ga",
        "gl",
        "he",
        "hi",
        "hu",
        "hy",
        "id",
        "it",
        "ja",
        "ko",
        "lv",
        "mul",
        "nl",
        "no",
        "pt",
        "ro",
        "ru",
        "sv",
        "th",
        "tr",
        "zh-Hans",
        "zh-Hant",
    ] = Field(alias="AnalysisSchemeLanguage")
    analysis_options: Optional[AnalysisOptionsModel] = Field(
        default=None, alias="AnalysisOptions"
    )


class BuildSuggestersResponseModel(BaseModel):
    field_names: List[str] = Field(alias="FieldNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IndexDocumentsResponseModel(BaseModel):
    field_names: List[str] = Field(alias="FieldNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainNamesResponseModel(BaseModel):
    domain_names: Dict[str, str] = Field(alias="DomainNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineExpressionRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    expression: ExpressionModel = Field(alias="Expression")


class ExpressionStatusModel(BaseModel):
    options: ExpressionModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class SuggesterModel(BaseModel):
    suggester_name: str = Field(alias="SuggesterName")
    document_suggester_options: DocumentSuggesterOptionsModel = Field(
        alias="DocumentSuggesterOptions"
    )


class DomainEndpointOptionsStatusModel(BaseModel):
    options: DomainEndpointOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class UpdateDomainEndpointOptionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    domain_endpoint_options: DomainEndpointOptionsModel = Field(
        alias="DomainEndpointOptions"
    )


class DomainStatusModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    domain_name: str = Field(alias="DomainName")
    requires_index_documents: bool = Field(alias="RequiresIndexDocuments")
    arn: Optional[str] = Field(default=None, alias="ARN")
    created: Optional[bool] = Field(default=None, alias="Created")
    deleted: Optional[bool] = Field(default=None, alias="Deleted")
    doc_service: Optional[ServiceEndpointModel] = Field(
        default=None, alias="DocService"
    )
    search_service: Optional[ServiceEndpointModel] = Field(
        default=None, alias="SearchService"
    )
    processing: Optional[bool] = Field(default=None, alias="Processing")
    search_instance_type: Optional[str] = Field(
        default=None, alias="SearchInstanceType"
    )
    search_partition_count: Optional[int] = Field(
        default=None, alias="SearchPartitionCount"
    )
    search_instance_count: Optional[int] = Field(
        default=None, alias="SearchInstanceCount"
    )
    limits: Optional[LimitsModel] = Field(default=None, alias="Limits")


class IndexFieldModel(BaseModel):
    index_field_name: str = Field(alias="IndexFieldName")
    index_field_type: Literal[
        "date",
        "date-array",
        "double",
        "double-array",
        "int",
        "int-array",
        "latlon",
        "literal",
        "literal-array",
        "text",
        "text-array",
    ] = Field(alias="IndexFieldType")
    int_options: Optional[IntOptionsModel] = Field(default=None, alias="IntOptions")
    double_options: Optional[DoubleOptionsModel] = Field(
        default=None, alias="DoubleOptions"
    )
    literal_options: Optional[LiteralOptionsModel] = Field(
        default=None, alias="LiteralOptions"
    )
    text_options: Optional[TextOptionsModel] = Field(default=None, alias="TextOptions")
    date_options: Optional[DateOptionsModel] = Field(default=None, alias="DateOptions")
    lat_lon_options: Optional[LatLonOptionsModel] = Field(
        default=None, alias="LatLonOptions"
    )
    int_array_options: Optional[IntArrayOptionsModel] = Field(
        default=None, alias="IntArrayOptions"
    )
    double_array_options: Optional[DoubleArrayOptionsModel] = Field(
        default=None, alias="DoubleArrayOptions"
    )
    literal_array_options: Optional[LiteralArrayOptionsModel] = Field(
        default=None, alias="LiteralArrayOptions"
    )
    text_array_options: Optional[TextArrayOptionsModel] = Field(
        default=None, alias="TextArrayOptions"
    )
    date_array_options: Optional[DateArrayOptionsModel] = Field(
        default=None, alias="DateArrayOptions"
    )


class ScalingParametersStatusModel(BaseModel):
    options: ScalingParametersModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class UpdateScalingParametersRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    scaling_parameters: ScalingParametersModel = Field(alias="ScalingParameters")


class DescribeServiceAccessPoliciesResponseModel(BaseModel):
    access_policies: AccessPoliciesStatusModel = Field(alias="AccessPolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceAccessPoliciesResponseModel(BaseModel):
    access_policies: AccessPoliciesStatusModel = Field(alias="AccessPolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAvailabilityOptionsResponseModel(BaseModel):
    availability_options: AvailabilityOptionsStatusModel = Field(
        alias="AvailabilityOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAvailabilityOptionsResponseModel(BaseModel):
    availability_options: AvailabilityOptionsStatusModel = Field(
        alias="AvailabilityOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AnalysisSchemeStatusModel(BaseModel):
    options: AnalysisSchemeModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class DefineAnalysisSchemeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    analysis_scheme: AnalysisSchemeModel = Field(alias="AnalysisScheme")


class DefineExpressionResponseModel(BaseModel):
    expression: ExpressionStatusModel = Field(alias="Expression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteExpressionResponseModel(BaseModel):
    expression: ExpressionStatusModel = Field(alias="Expression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExpressionsResponseModel(BaseModel):
    expressions: List[ExpressionStatusModel] = Field(alias="Expressions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineSuggesterRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    suggester: SuggesterModel = Field(alias="Suggester")


class SuggesterStatusModel(BaseModel):
    options: SuggesterModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class DescribeDomainEndpointOptionsResponseModel(BaseModel):
    domain_endpoint_options: DomainEndpointOptionsStatusModel = Field(
        alias="DomainEndpointOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainEndpointOptionsResponseModel(BaseModel):
    domain_endpoint_options: DomainEndpointOptionsStatusModel = Field(
        alias="DomainEndpointOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainResponseModel(BaseModel):
    domain_status: DomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResponseModel(BaseModel):
    domain_status: DomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainsResponseModel(BaseModel):
    domain_status_list: List[DomainStatusModel] = Field(alias="DomainStatusList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineIndexFieldRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    index_field: IndexFieldModel = Field(alias="IndexField")


class IndexFieldStatusModel(BaseModel):
    options: IndexFieldModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class DescribeScalingParametersResponseModel(BaseModel):
    scaling_parameters: ScalingParametersStatusModel = Field(alias="ScalingParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScalingParametersResponseModel(BaseModel):
    scaling_parameters: ScalingParametersStatusModel = Field(alias="ScalingParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineAnalysisSchemeResponseModel(BaseModel):
    analysis_scheme: AnalysisSchemeStatusModel = Field(alias="AnalysisScheme")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAnalysisSchemeResponseModel(BaseModel):
    analysis_scheme: AnalysisSchemeStatusModel = Field(alias="AnalysisScheme")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAnalysisSchemesResponseModel(BaseModel):
    analysis_schemes: List[AnalysisSchemeStatusModel] = Field(alias="AnalysisSchemes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineSuggesterResponseModel(BaseModel):
    suggester: SuggesterStatusModel = Field(alias="Suggester")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSuggesterResponseModel(BaseModel):
    suggester: SuggesterStatusModel = Field(alias="Suggester")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSuggestersResponseModel(BaseModel):
    suggesters: List[SuggesterStatusModel] = Field(alias="Suggesters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefineIndexFieldResponseModel(BaseModel):
    index_field: IndexFieldStatusModel = Field(alias="IndexField")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIndexFieldResponseModel(BaseModel):
    index_field: IndexFieldStatusModel = Field(alias="IndexField")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIndexFieldsResponseModel(BaseModel):
    index_fields: List[IndexFieldStatusModel] = Field(alias="IndexFields")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
