# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DocumentMetadataModel(BaseModel):
    pages: Optional[int] = Field(default=None, alias="Pages")


class HumanLoopActivationOutputModel(BaseModel):
    human_loop_arn: Optional[str] = Field(default=None, alias="HumanLoopArn")
    human_loop_activation_reasons: Optional[List[str]] = Field(
        default=None, alias="HumanLoopActivationReasons"
    )
    human_loop_activation_conditions_evaluation_results: Optional[str] = Field(
        default=None, alias="HumanLoopActivationConditionsEvaluationResults"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class NormalizedValueModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    value_type: Optional[Literal["DATE"]] = Field(default=None, alias="ValueType")


class QueryModel(BaseModel):
    text: str = Field(alias="Text")
    alias: Optional[str] = Field(default=None, alias="Alias")
    pages: Optional[Sequence[str]] = Field(default=None, alias="Pages")


class RelationshipModel(BaseModel):
    type: Optional[
        Literal["ANSWER", "CHILD", "COMPLEX_FEATURES", "MERGED_CELL", "TITLE", "VALUE"]
    ] = Field(default=None, alias="Type")
    ids: Optional[List[str]] = Field(default=None, alias="Ids")


class BoundingBoxModel(BaseModel):
    width: Optional[float] = Field(default=None, alias="Width")
    height: Optional[float] = Field(default=None, alias="Height")
    left: Optional[float] = Field(default=None, alias="Left")
    top: Optional[float] = Field(default=None, alias="Top")


class DetectedSignatureModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")


class SplitDocumentModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    pages: Optional[List[int]] = Field(default=None, alias="Pages")


class UndetectedSignatureModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")


class S3ObjectModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class ExpenseCurrencyModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class ExpenseGroupPropertyModel(BaseModel):
    types: Optional[List[str]] = Field(default=None, alias="Types")
    id: Optional[str] = Field(default=None, alias="Id")


class ExpenseTypeModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class PointModel(BaseModel):
    x: Optional[float] = Field(default=None, alias="X")
    y: Optional[float] = Field(default=None, alias="Y")


class GetDocumentAnalysisRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class WarningModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    pages: Optional[List[int]] = Field(default=None, alias="Pages")


class GetDocumentTextDetectionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetExpenseAnalysisRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetLendingAnalysisRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetLendingAnalysisSummaryRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class HumanLoopDataAttributesModel(BaseModel):
    content_classifiers: Optional[
        Sequence[
            Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
        ]
    ] = Field(default=None, alias="ContentClassifiers")


class NotificationChannelModel(BaseModel):
    s_ns_topic_arn: str = Field(alias="SNSTopicArn")
    role_arn: str = Field(alias="RoleArn")


class OutputConfigModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")


class PredictionModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class StartDocumentAnalysisResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDocumentTextDetectionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExpenseAnalysisResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartLendingAnalysisResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AnalyzeIDDetectionsModel(BaseModel):
    text: str = Field(alias="Text")
    normalized_value: Optional[NormalizedValueModel] = Field(
        default=None, alias="NormalizedValue"
    )
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class QueriesConfigModel(BaseModel):
    queries: Sequence[QueryModel] = Field(alias="Queries")


class DocumentGroupModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    split_documents: Optional[List[SplitDocumentModel]] = Field(
        default=None, alias="SplitDocuments"
    )
    detected_signatures: Optional[List[DetectedSignatureModel]] = Field(
        default=None, alias="DetectedSignatures"
    )
    undetected_signatures: Optional[List[UndetectedSignatureModel]] = Field(
        default=None, alias="UndetectedSignatures"
    )


class DocumentLocationModel(BaseModel):
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class DocumentModel(BaseModel):
    bytes: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Bytes"
    )
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class GeometryModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    polygon: Optional[List[PointModel]] = Field(default=None, alias="Polygon")


class HumanLoopConfigModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    data_attributes: Optional[HumanLoopDataAttributesModel] = Field(
        default=None, alias="DataAttributes"
    )


class PageClassificationModel(BaseModel):
    page_type: List[PredictionModel] = Field(alias="PageType")
    page_number: List[PredictionModel] = Field(alias="PageNumber")


class IdentityDocumentFieldModel(BaseModel):
    type: Optional[AnalyzeIDDetectionsModel] = Field(default=None, alias="Type")
    value_detection: Optional[AnalyzeIDDetectionsModel] = Field(
        default=None, alias="ValueDetection"
    )


class LendingSummaryModel(BaseModel):
    document_groups: Optional[List[DocumentGroupModel]] = Field(
        default=None, alias="DocumentGroups"
    )
    undetected_document_types: Optional[List[str]] = Field(
        default=None, alias="UndetectedDocumentTypes"
    )


class StartDocumentAnalysisRequestModel(BaseModel):
    document_location: DocumentLocationModel = Field(alias="DocumentLocation")
    feature_types: Sequence[
        Literal["FORMS", "QUERIES", "SIGNATURES", "TABLES"]
    ] = Field(alias="FeatureTypes")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")
    queries_config: Optional[QueriesConfigModel] = Field(
        default=None, alias="QueriesConfig"
    )


class StartDocumentTextDetectionRequestModel(BaseModel):
    document_location: DocumentLocationModel = Field(alias="DocumentLocation")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")


class StartExpenseAnalysisRequestModel(BaseModel):
    document_location: DocumentLocationModel = Field(alias="DocumentLocation")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")


class StartLendingAnalysisRequestModel(BaseModel):
    document_location: DocumentLocationModel = Field(alias="DocumentLocation")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KMSKeyId")


class AnalyzeExpenseRequestModel(BaseModel):
    document: DocumentModel = Field(alias="Document")


class AnalyzeIDRequestModel(BaseModel):
    document_pages: Sequence[DocumentModel] = Field(alias="DocumentPages")


class DetectDocumentTextRequestModel(BaseModel):
    document: DocumentModel = Field(alias="Document")


class BlockModel(BaseModel):
    block_type: Optional[
        Literal[
            "CELL",
            "KEY_VALUE_SET",
            "LINE",
            "MERGED_CELL",
            "PAGE",
            "QUERY",
            "QUERY_RESULT",
            "SELECTION_ELEMENT",
            "SIGNATURE",
            "TABLE",
            "TITLE",
            "WORD",
        ]
    ] = Field(default=None, alias="BlockType")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    text: Optional[str] = Field(default=None, alias="Text")
    text_type: Optional[Literal["HANDWRITING", "PRINTED"]] = Field(
        default=None, alias="TextType"
    )
    row_index: Optional[int] = Field(default=None, alias="RowIndex")
    column_index: Optional[int] = Field(default=None, alias="ColumnIndex")
    row_span: Optional[int] = Field(default=None, alias="RowSpan")
    column_span: Optional[int] = Field(default=None, alias="ColumnSpan")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")
    id: Optional[str] = Field(default=None, alias="Id")
    relationships: Optional[List[RelationshipModel]] = Field(
        default=None, alias="Relationships"
    )
    entity_types: Optional[List[Literal["COLUMN_HEADER", "KEY", "VALUE"]]] = Field(
        default=None, alias="EntityTypes"
    )
    selection_status: Optional[Literal["NOT_SELECTED", "SELECTED"]] = Field(
        default=None, alias="SelectionStatus"
    )
    page: Optional[int] = Field(default=None, alias="Page")
    query: Optional[QueryModel] = Field(default=None, alias="Query")


class ExpenseDetectionModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class LendingDetectionModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    selection_status: Optional[Literal["NOT_SELECTED", "SELECTED"]] = Field(
        default=None, alias="SelectionStatus"
    )
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class SignatureDetectionModel(BaseModel):
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")


class AnalyzeDocumentRequestModel(BaseModel):
    document: DocumentModel = Field(alias="Document")
    feature_types: Sequence[
        Literal["FORMS", "QUERIES", "SIGNATURES", "TABLES"]
    ] = Field(alias="FeatureTypes")
    human_loop_config: Optional[HumanLoopConfigModel] = Field(
        default=None, alias="HumanLoopConfig"
    )
    queries_config: Optional[QueriesConfigModel] = Field(
        default=None, alias="QueriesConfig"
    )


class GetLendingAnalysisSummaryResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    job_status: Literal[
        "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"
    ] = Field(alias="JobStatus")
    summary: LendingSummaryModel = Field(alias="Summary")
    warnings: List[WarningModel] = Field(alias="Warnings")
    status_message: str = Field(alias="StatusMessage")
    analyze_lending_model_version: str = Field(alias="AnalyzeLendingModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AnalyzeDocumentResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    blocks: List[BlockModel] = Field(alias="Blocks")
    human_loop_activation_output: HumanLoopActivationOutputModel = Field(
        alias="HumanLoopActivationOutput"
    )
    analyze_document_model_version: str = Field(alias="AnalyzeDocumentModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectDocumentTextResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    blocks: List[BlockModel] = Field(alias="Blocks")
    detect_document_text_model_version: str = Field(
        alias="DetectDocumentTextModelVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDocumentAnalysisResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    job_status: Literal[
        "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"
    ] = Field(alias="JobStatus")
    next_token: str = Field(alias="NextToken")
    blocks: List[BlockModel] = Field(alias="Blocks")
    warnings: List[WarningModel] = Field(alias="Warnings")
    status_message: str = Field(alias="StatusMessage")
    analyze_document_model_version: str = Field(alias="AnalyzeDocumentModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDocumentTextDetectionResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    job_status: Literal[
        "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"
    ] = Field(alias="JobStatus")
    next_token: str = Field(alias="NextToken")
    blocks: List[BlockModel] = Field(alias="Blocks")
    warnings: List[WarningModel] = Field(alias="Warnings")
    status_message: str = Field(alias="StatusMessage")
    detect_document_text_model_version: str = Field(
        alias="DetectDocumentTextModelVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IdentityDocumentModel(BaseModel):
    document_index: Optional[int] = Field(default=None, alias="DocumentIndex")
    identity_document_fields: Optional[List[IdentityDocumentFieldModel]] = Field(
        default=None, alias="IdentityDocumentFields"
    )
    blocks: Optional[List[BlockModel]] = Field(default=None, alias="Blocks")


class ExpenseFieldModel(BaseModel):
    type: Optional[ExpenseTypeModel] = Field(default=None, alias="Type")
    label_detection: Optional[ExpenseDetectionModel] = Field(
        default=None, alias="LabelDetection"
    )
    value_detection: Optional[ExpenseDetectionModel] = Field(
        default=None, alias="ValueDetection"
    )
    page_number: Optional[int] = Field(default=None, alias="PageNumber")
    currency: Optional[ExpenseCurrencyModel] = Field(default=None, alias="Currency")
    group_properties: Optional[List[ExpenseGroupPropertyModel]] = Field(
        default=None, alias="GroupProperties"
    )


class LendingFieldModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    key_detection: Optional[LendingDetectionModel] = Field(
        default=None, alias="KeyDetection"
    )
    value_detections: Optional[List[LendingDetectionModel]] = Field(
        default=None, alias="ValueDetections"
    )


class AnalyzeIDResponseModel(BaseModel):
    identity_documents: List[IdentityDocumentModel] = Field(alias="IdentityDocuments")
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    analyze_idmodel_version: str = Field(alias="AnalyzeIDModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LineItemFieldsModel(BaseModel):
    line_item_expense_fields: Optional[List[ExpenseFieldModel]] = Field(
        default=None, alias="LineItemExpenseFields"
    )


class LendingDocumentModel(BaseModel):
    lending_fields: Optional[List[LendingFieldModel]] = Field(
        default=None, alias="LendingFields"
    )
    signature_detections: Optional[List[SignatureDetectionModel]] = Field(
        default=None, alias="SignatureDetections"
    )


class LineItemGroupModel(BaseModel):
    line_item_group_index: Optional[int] = Field(
        default=None, alias="LineItemGroupIndex"
    )
    line_items: Optional[List[LineItemFieldsModel]] = Field(
        default=None, alias="LineItems"
    )


class ExpenseDocumentModel(BaseModel):
    expense_index: Optional[int] = Field(default=None, alias="ExpenseIndex")
    summary_fields: Optional[List[ExpenseFieldModel]] = Field(
        default=None, alias="SummaryFields"
    )
    line_item_groups: Optional[List[LineItemGroupModel]] = Field(
        default=None, alias="LineItemGroups"
    )
    blocks: Optional[List[BlockModel]] = Field(default=None, alias="Blocks")


class AnalyzeExpenseResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    expense_documents: List[ExpenseDocumentModel] = Field(alias="ExpenseDocuments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExtractionModel(BaseModel):
    lending_document: Optional[LendingDocumentModel] = Field(
        default=None, alias="LendingDocument"
    )
    expense_document: Optional[ExpenseDocumentModel] = Field(
        default=None, alias="ExpenseDocument"
    )
    identity_document: Optional[IdentityDocumentModel] = Field(
        default=None, alias="IdentityDocument"
    )


class GetExpenseAnalysisResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    job_status: Literal[
        "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"
    ] = Field(alias="JobStatus")
    next_token: str = Field(alias="NextToken")
    expense_documents: List[ExpenseDocumentModel] = Field(alias="ExpenseDocuments")
    warnings: List[WarningModel] = Field(alias="Warnings")
    status_message: str = Field(alias="StatusMessage")
    analyze_expense_model_version: str = Field(alias="AnalyzeExpenseModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LendingResultModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")
    page_classification: Optional[PageClassificationModel] = Field(
        default=None, alias="PageClassification"
    )
    extractions: Optional[List[ExtractionModel]] = Field(
        default=None, alias="Extractions"
    )


class GetLendingAnalysisResponseModel(BaseModel):
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    job_status: Literal[
        "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"
    ] = Field(alias="JobStatus")
    next_token: str = Field(alias="NextToken")
    results: List[LendingResultModel] = Field(alias="Results")
    warnings: List[WarningModel] = Field(alias="Warnings")
    status_message: str = Field(alias="StatusMessage")
    analyze_lending_model_version: str = Field(alias="AnalyzeLendingModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
